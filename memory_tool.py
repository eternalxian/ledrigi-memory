from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
FACT_FILE = ROOT / "fact_layer.md"
INDEX_FILE = ROOT / "index_layer.md"
LEDGER_FILE = ROOT / "integrity_ledger.jsonl"
NODE_RE = re.compile(
    r"^##\s+(?P<id>(?:event|utterance):[a-zA-Z0-9_-]+)\s*$\n(?P<body>.*?)(?=^---\s*$|^##\s+|\Z)",
    re.MULTILINE | re.DOTALL,
)
REF_RE = re.compile(r"(?:event|utterance):[a-zA-Z0-9_-]+")


@dataclass(frozen=True)
class Node:
    node_id: str
    body: str
    raw: str

    @property
    def summary(self) -> str:
        match = re.search(r'^summary:\s*"?(.*?)"?\s*$', self.body, re.MULTILINE)
        return match.group(1) if match else ""

    @property
    def digest(self) -> str:
        return hashlib.sha256(self.raw.strip().encode("utf-8")).hexdigest()


def load_nodes() -> list[Node]:
    text = FACT_FILE.read_text(encoding="utf-8")
    return [Node(m.group("id"), m.group("body").strip(), m.group(0)) for m in NODE_RE.finditer(text)]


def load_aliases() -> dict[str, str]:
    aliases: dict[str, str] = {}
    for line in INDEX_FILE.read_text(encoding="utf-8").splitlines():
        if "->" not in line:
            continue
        left, right = (part.strip() for part in line.split("->", 1))
        if REF_RE.fullmatch(right) and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", left):
            aliases[left] = right
    return aliases


def search(query: str, limit: int = 5) -> list[tuple[int, Node]]:
    query = query.strip().lower()
    nodes = load_nodes()
    node_map = {node.node_id: node for node in nodes}
    scores = {node.node_id: 0 for node in nodes}
    aliases = load_aliases()

    for alias, node_id in aliases.items():
        alias_lower = alias.lower()
        if alias_lower in query or query in alias_lower:
            scores[node_id] = scores.get(node_id, 0) + 10

    ascii_tokens = re.findall(r"[a-zA-Z0-9_-]{2,}", query)
    chinese_chunks = re.findall(r"[\u4e00-\u9fff]{2,}", query)
    tokens = ascii_tokens + chinese_chunks
    for node in nodes:
        haystack = f"{node.node_id} {node.body}".lower()
        if query and query in haystack:
            scores[node.node_id] += 8
        for token in tokens:
            if token in haystack:
                scores[node.node_id] += 2

    ranked = [(score, node_map[node_id]) for node_id, score in scores.items() if score > 0]
    return sorted(ranked, key=lambda item: (-item[0], item[1].node_id))[:limit]


def ledger_records(nodes: list[Node]) -> list[dict]:
    records = []
    previous = "GENESIS"
    for node in nodes:
        payload = f"{previous}|{node.node_id}|{node.digest}"
        record_hash = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        records.append({
            "node_id": node.node_id,
            "node_hash": node.digest,
            "previous_hash": previous,
            "record_hash": record_hash,
        })
        previous = record_hash
    return records


def write_ledger(force: bool = False) -> None:
    if LEDGER_FILE.exists() and not force:
        raise RuntimeError("账本已存在；若确定要重建基线，请使用 --force")
    records = ledger_records(load_nodes())
    LEDGER_FILE.write_text(
        "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in records),
        encoding="utf-8",
    )


def validate_index(nodes: list[Node]) -> list[str]:
    node_ids = {node.node_id for node in nodes}
    refs = set(REF_RE.findall(INDEX_FILE.read_text(encoding="utf-8")))
    return sorted(refs - node_ids)


def verify() -> tuple[bool, list[str]]:
    errors: list[str] = []
    nodes = load_nodes()
    if len({node.node_id for node in nodes}) != len(nodes):
        errors.append("事实层存在重复节点ID")
    missing = validate_index(nodes)
    if missing:
        errors.append(f"索引引用了不存在的节点: {', '.join(missing)}")
    if not LEDGER_FILE.exists():
        errors.append("完整性账本不存在")
        return False, errors

    try:
        stored = [json.loads(line) for line in LEDGER_FILE.read_text(encoding="utf-8").splitlines() if line]
    except Exception as exc:
        return False, errors + [f"账本无法解析: {exc}"]

    current = ledger_records(nodes)
    if stored != current:
        errors.append("事实层节点或哈希链与账本不一致")
    return not errors, errors


def append_node(node_id: str, summary: str, tags: str, aliases: list[str]) -> None:
    if not re.fullmatch(r"(?:event|utterance):[a-zA-Z0-9_-]+", node_id):
        raise ValueError("节点ID格式应为 event:name 或 utterance:name")
    ok, errors = verify()
    if not ok:
        raise RuntimeError("追加前完整性检查失败: " + "; ".join(errors))
    if node_id in {node.node_id for node in load_nodes()}:
        raise ValueError("节点ID已存在")

    block = (
        f"\n\n---\n\n## {node_id}\n"
        f"type: {node_id.split(':', 1)[0]}\n"
        f"time: {date.today().isoformat()}\n"
        f"summary: {json.dumps(summary, ensure_ascii=False)}\n"
        f"tags: [{tags}]\n"
    )
    with FACT_FILE.open("a", encoding="utf-8") as handle:
        handle.write(block)
    if aliases:
        with INDEX_FILE.open("a", encoding="utf-8") as handle:
            handle.write("\n" + "\n".join(f"{alias} -> {node_id}" for alias in aliases) + "\n")

    records = ledger_records(load_nodes())
    LEDGER_FILE.write_text(
        "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in records),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="三层AI记忆索引工具")
    sub = parser.add_subparsers(dest="command", required=True)
    search_parser = sub.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("--limit", type=int, default=5)
    sub.add_parser("verify")
    init_parser = sub.add_parser("init-ledger")
    init_parser.add_argument("--force", action="store_true")
    append_parser = sub.add_parser("append")
    append_parser.add_argument("--id", required=True)
    append_parser.add_argument("--summary", required=True)
    append_parser.add_argument("--tags", default="")
    append_parser.add_argument("--alias", action="append", default=[])
    args = parser.parse_args()

    if args.command == "search":
        results = search(args.query, args.limit)
        if not results:
            print("未找到相关记忆。")
        for score, node in results:
            print(f"[{score}] {node.node_id}: {node.summary}")
    elif args.command == "verify":
        ok, errors = verify()
        if not ok:
            for error in errors:
                print("ERROR:", error)
            raise SystemExit(1)
        print(f"PASS: {len(load_nodes())}个节点、索引引用和哈希链一致。")
    elif args.command == "init-ledger":
        write_ledger(args.force)
        print("完整性基线已建立。")
    elif args.command == "append":
        append_node(args.id, args.summary, args.tags, args.alias)
        print("节点已追加并更新完整性账本。")


if __name__ == "__main__":
    main()
