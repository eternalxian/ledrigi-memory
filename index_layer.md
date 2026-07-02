# 莱德利基记忆系统 · 索引层
# 可重建、可覆盖。version: 1

## 时间线

2026-06-11  event:系统设计启动
2026-06-11  event:三层架构确立
2026-06-11  event:多轮设计审阅
2026-06-11  event:所有权声明确立
2026-06-11  event:Schema定稿
2026-06-11  event:检索准确性测试
2026-06-12  event:冗余设计废弃
2026-06-12  event:首次维护自检
2026-06-12  event:外部方案借鉴
2026-07-02  event:效率压力测试

## 权重排序（weight = importance + recent_access + retrieval_count）

importance:5
  event:所有权声明确立
  event:三层架构确立

importance:4
  event:多轮设计审阅
  event:Schema定稿
  event:系统设计启动

## 概念映射

架构设计:
  children: [event:系统设计启动, event:三层架构确立, event:Schema定稿]

数据完整性:
  children: [event:所有权声明确立]

迭代与测试:
  children: [event:多轮设计审阅, event:检索准确性测试, event:效率压力测试]

架构简化:
  children: [event:冗余设计废弃]

运维:
  children: [event:首次维护自检, event:外部方案借鉴]

## 检索入口（aliases → node ID）

架构 → event:三层架构确立
Schema → event:Schema定稿
所有权 → event:所有权声明确立
测试 → event:检索准确性测试
效率 → event:效率压力测试
token → event:效率压力测试
废弃 → event:冗余设计废弃
借鉴 → event:外部方案借鉴
双时态 → event:外部方案借鉴
设计 → event:系统设计启动
审阅 → event:多轮设计审阅
自检 → event:首次维护自检
