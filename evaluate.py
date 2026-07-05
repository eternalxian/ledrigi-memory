import json
from pathlib import Path

from memory_tool import FACT_FILE, INDEX_FILE, search

ROOT = Path(__file__).parent


def main() -> None:
    cases = json.loads((ROOT / "evaluation_cases.json").read_text(encoding="utf-8"))
    passed = 0
    reductions = []
    fact_chars = len(FACT_FILE.read_text(encoding="utf-8"))
    index_chars = len(INDEX_FILE.read_text(encoding="utf-8"))

    for case in cases:
        results = search(case["query"], limit=1)
        actual = results[0][1].node_id if results else None
        ok = actual == case["expected"]
        passed += int(ok)
        if results:
            loaded = index_chars + len(results[0][1].raw)
            reductions.append(max(0.0, 1 - loaded / fact_chars))
        print(f"{'PASS' if ok else 'FAIL'} | {case['query']} | {actual}")

    average = sum(reductions) / len(reductions) if reductions else 0
    print(f"\n检索命中: {passed}/{len(cases)}")
    print(f"平均字符加载量缩减: {average:.1%}")
    if passed != len(cases):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
