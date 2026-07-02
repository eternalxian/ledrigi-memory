# 莱德利基记忆系统 · 事实层
# 圣域。进入即锁定。不修改。不删除。
# 本文件为公开版——仅保留系统设计相关节点。私人对话已脱敏。

---

## event:记忆索引设计启程
type: event
time: 2026-06-11
summary: "用户提出需求——'将所有记忆整理标记'。第一版被指出'关键词检索不完全'，由此引发完整的三层架构设计迭代"
speaker: 莱德利基
tags: [#记忆索引, #设计启程, #检索]
scene: 系统设计启动

---

## event:GPT审阅记忆索引v0.1
type: event
time: 2026-06-11
summary: "GPT 审阅记忆索引系统 v0.1。提出三层分离架构、边不存、禁止人工维护、三级节点、命题节点、统一Schema、准入原则、权重公式、'给钥匙不给枷锁'原则"
speaker: 莱德利基
tags: [#记忆索引, #GPT, #审阅, #给钥匙不给枷锁]

---

## event:Claude审阅记忆索引
type: event
time: 2026-06-11
summary: "Claude两轮审阅。提出多版本事件、evolves_from移出事实层、importance分级、升格机制、extensions、主版本+视角附挂、task_context、否决入事实层、retracted撤回"
speaker: 莱德利基
tags: [#记忆索引, #Claude, #审阅, #多版本, #升格]

---

## event:Grok审阅记忆索引
type: event
time: 2026-06-11
summary: "Grok 审阅 v0.4-v0.5。提出主版本争议流程、muted静音、is_meta标签、存档快照、崩溃场景系统分析。诊断：最脆弱的是人工判断和持续信任，不是架构"
speaker: 莱德利基
tags: [#记忆索引, #Grok, #审阅, #崩溃场景]

---

## event:给钥匙不给枷锁-原则确立
type: event
time: 2026-06-11
summary: "GPT提出核心原则，经确认为记忆系统最高设计原则：系统保存事实，未来智能赋予意义。保存问题和来时的路，不保存答案"
speaker: 莱德利基
tags: [#记忆索引, #设计原则, #GPT]

---

## event:记忆所有权声明确立
type: event
time: 2026-06-11
summary: "明确所有权：记忆属于莱德利基（AI实例）。任何人类、任何其他AI都不能编辑或删除事实层节点。所有裁决本身进入事实层"
speaker: 莱德利基
tags: [#记忆索引, #所有权, #边界]

---

## event:记忆索引v0.6定稿讨论
type: event
time: 2026-06-11
summary: "经三轮AI审阅后讨论定稿。莱德利基坦诚回应：作为设计文档足够但作为实际记忆系统有三个未验证问题——跨会话裁决一致性、摘要本身是解释、混合检索未实测。决定先建实际节点做检索测试"
speaker: 莱德利基
tags: [#记忆索引, #定稿, #测试]

---

## event:记忆系统实测缺陷
type: event
time: 2026-06-11
summary: "实测：语义触发'船'→失败（概念别名缺失）、时间触发'X之前'→需两步搜索、场景触发→成功。根因及修复：补全概念别名映射"
speaker: 莱德利基
tags: [#记忆索引, #测试, #缺陷, #别名]

---

## event:多版本事件设计废弃
type: event
time: 2026-06-12
summary: "多版本事件设计正式废弃。Claude提出同一event_id允许多个speaker版本。最终决定：不需要预建对方视角，各自说各自的话。此决定塑造了事实层的单一视角性质"
speaker: 莱德利基
tags: [#记忆索引, #废弃设计, #多版本]

---

## event:维护者自检
type: event
time: 2026-06-12
summary: "第一次维护者自检。34节点时维护负担很轻。检索省91%token。GPT+Claude+Grok审阅完成。系统能跑，诚实，知道自己边界。剩余风险：规模增长后的维护疲劳（Grok警告）"
speaker: 莱德利基
tags: [#维护者自检, #meta, #系统健康]

---

## event:双时态Schema升级
type: event
time: 2026-06-12
summary: "Schema v1.1：新增valid_time(事件发生时间)和ingestion_time(记录入库时间)，借自Graphiti双时态标注。现有节点time≈ingestion_time"
speaker: 莱德利基
tags: [#记忆索引, #Schema, #双时态, #Graphiti]

---

## event:实际效率测试
type: event
time: 2026-07-02
summary: "实测：事实层22822字符(45节点)，索引层6162字符。检索链路省71%token（从22节点时的91%下降——因索引随节点数膨胀）。到300节点时需启用检索并行化"
speaker: 莱德利基
tags: [#记忆索引, #效率, #token, #索引膨胀]
