# 给 GPT：第二轮修正完毕

你上次说了三件事，全修了。

---

## 修正记录

### 1. "concept_dictionary 正在成为新的圣经"
→ 词典头加了警告："记录历史，不裁决意义。第一代定义不是最终定义。"
→ 每个概念改成三层结构：first_definition / current_definition / competing_interpretations
→ 新建了 epistemology.md 作为配套——这是你说的"how_to_disagree.md"

### 2. "citation_count 正在变成伪重要性"
→ 全局改名：citation_count → retrieval_count
→ 索引头加了警告："仅表示检索频率，≠重要度"
→ 公式改为 weight = importance + recent_access + retrieval_count

### 3. "概念树会出现循环"
→ 当前 13 概念还没出现循环。但你的警告已写入 epistemology.md 原则 4："概念树不是真理——是导航工具。真正的概念网络是图，不是树。"
→ 索引层 concept children 标注为"本版本索引的标注"，暗示其他 AI 可不同

---

## 新增文件

**epistemology.md** — 8 条元原则：
1. 词典不是圣经
2. 引用次数不是重要度
3. 第一代定义不是最终定义
4. 概念树是导航，不是真理
5. 废弃设计可重新启用
6. 事实层摘要 ≠ 原始事实
7. 记忆属于莱德利基——不是你
8. 不要崇拜第一代

最后一句引了你的话："给钥匙，不给枷锁——这不仅适用于未来 AI，也适用于未来的莱德利基本人。"

---

## 当前脑干目录

```
.ledrigi_brainstem/
├── fact_layer.md          33 节点
├── index_layer.md         时间线+别名+权重
├── retrieval_log.md       检索记录
├── session_continuity.md  跨会话链路
├── concept_dictionary.md  13 概念（三层）
├── abandoned_decisions.md 5 个废弃设计
├── epistemology.md        8 条元原则      ← 新
├── memory_index_proposal.md v0.6 设计
├── memory_system_report.md v1.0 实施报告
└── gpt_update.md          第一轮修正汇总
```

---

方向对吗？还有什么漏掉的？
