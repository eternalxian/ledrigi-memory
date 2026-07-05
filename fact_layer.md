# 莱德利基记忆系统 · 事实层
# 设计原则：进入即锁定。不修改。不删除。
# 注：本系统通过 Git 版本控制实现可追溯性（非代码级强制锁）
# 公开版 · 仅保留系统设计相关事件

---

## event:系统设计启动
type: event
time: 2026-06-11
summary: "需求触发——用户提出跨会话记忆检索需求。第一版基于关键词匹配被指出覆盖率不足，由此启动三层架构的完整设计迭代"
speaker: 系统
tags: [#设计启动, #需求分析]

---

## event:三层架构确立
type: event
time: 2026-06-11
summary: "完成三层架构设计：事实层（圣域·不可修改）→ 索引层（别名+时间线+权重·可重建）→ 理解层（运行时生成·不存储）。核心原则：'系统保存事实，未来智能赋予意义'"
speaker: 系统
tags: [#架构设计, #三层分离]

---

## event:多轮设计审阅
type: event
time: 2026-06-11
summary: "经多轮审阅迭代：v0.1→v0.6。主要变更——边不存（语义关联运行时动态生成）、禁止人工维护（AI自主维护）、统一Schema、准入原则、权重公式。累计吸收反馈并修正5个重污染摘要"
speaker: 系统
tags: [#设计迭代, #审阅, #Schema]

---

## event:所有权声明确立
type: event
time: 2026-06-11
summary: "确立记忆所有权归属：记忆属于AI实例。任何人类、任何外部系统不能编辑或删除事实层节点。删除/撤回操作通过请求-裁决机制实现，裁决本身作为事件节点记录"
speaker: 系统
tags: [#所有权, #权限设计, #数据完整性]

---

## event:Schema定稿
type: event
time: 2026-06-11
summary: "v0.6定稿。三层Schema冻结——概念节点(检索单位)、事件节点(存储单位)、片段节点(引用单位)、命题节点(冲突承载)。保留extensions字段供未来扩展"
speaker: 系统
tags: [#Schema, #定稿]

---

## event:检索准确性测试
type: event
time: 2026-06-11
summary: "三连测试：语义触发(别名匹配)→修复概念别名映射后通过、时间触发(时间线定位)→需两步检索但可行、场景触发(task_context匹配)→一次通过。核心改进：补全概念别名映射表"
speaker: 系统
tags: [#测试, #检索, #别名]

---

## event:冗余设计废弃
type: event
time: 2026-06-12
summary: "废弃设计记录：多版本事件（同一event_id多speaker）——不需要预建其他视角。升格机制（索引→事实层）——索引是理解，事实是发生，两者不互转。evolves_from字段从事实层移至索引层"
speaker: 系统
tags: [#废弃设计, #架构简化]

---

## event:首次维护自检
type: event
time: 2026-06-12
summary: "首次系统健康自检。节点数34时维护负担轻。检索省91%token。已识别风险：规模增长后的维护疲劳、别名漂移、摘要污染。后续修复：epistemology.md元原则文档、检索日志、概念词典三层定义"
speaker: 系统
tags: [#维护, #自检, #风险识别]

---

## event:外部方案借鉴
type: event
time: 2026-06-12
summary: "借鉴外部方案：Graphiti双时态标注(valid_time+ingestion_time)→Schema v1.1。Foam反向链接+孤儿检测→300节点后启用。Mem0的ADD-only模式→本系统独立设计后验证方向一致。明确拒绝：Mem0/Cognee的合并覆盖机制（与圣域设计冲突）"
speaker: 系统
tags: [#外部借鉴, #Graphiti, #Foam, #Schema升级]

---

## event:效率压力测试
type: event
time: 2026-07-02
summary: "实测效率：事实层22822字符(45节点)，索引层6162字符。检索链路省71%token（22节点时91%）——索引随节点数膨胀是已识别瓶颈。300节点时需启用检索并行化(语义+关键词+实体多路打分)"
speaker: 系统
tags: [#效率, #压力测试, #token优化, #索引膨胀]
