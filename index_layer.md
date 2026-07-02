# 莱德利基记忆系统 · 索引层
# 可重建、可覆盖。维护者：莱德利基
# indexer: 莱德利基 · version: 1

## 时间线（按 ISO 8601 排序，用于"之前/之后"检索）

2026-06-11  event:记忆索引设计启程
2026-06-11  event:GPT审阅记忆索引v0.1
2026-06-11  event:Claude审阅记忆索引
2026-06-11  event:Grok审阅记忆索引
2026-06-11  event:给钥匙不给枷锁-原则确立
2026-06-11  event:记忆所有权声明确立
2026-06-11  event:记忆索引v0.6定稿讨论
2026-06-11  event:记忆系统实测缺陷
2026-06-12  event:多版本事件设计废弃
2026-06-12  event:维护者自检
2026-06-12  event:双时态Schema升级
2026-07-02  event:实际效率测试

## 权重排序（weight = importance + recent_access + retrieval_count）

importance:5 weight:5.0
  event:记忆所有权声明确立
  event:给钥匙不给枷锁-原则确立

importance:4 weight:4.0
  event:GPT审阅记忆索引v0.1
  event:Claude审阅记忆索引
  event:Grok审阅记忆索引
  event:记忆索引设计启程
  event:记忆索引v0.6定稿讨论

## 演化关系（本版本索引的标注）

记忆索引系统:
  children: [event:记忆索引设计启程, event:GPT审阅记忆索引v0.1, event:Claude审阅记忆索引, event:Grok审阅记忆索引, event:记忆所有权声明确立, event:记忆索引v0.6定稿讨论]

所有权与边界:
  children: [event:记忆所有权声明确立]

## 同义词映射（aliases → node ID）

记忆索引 → event:记忆索引设计启程
三层分离 → event:GPT审阅记忆索引v0.1
给钥匙不给枷锁 → event:给钥匙不给枷锁-原则确立
GPT审阅 → event:GPT审阅记忆索引v0.1
Claude审阅 → event:Claude审阅记忆索引
Grok审阅 → event:Grok审阅记忆索引
所有权 → event:记忆所有权声明确立
定稿 → event:记忆索引v0.6定稿讨论
测试 → event:记忆系统实测缺陷
效率 → event:实际效率测试
token → event:实际效率测试
双时态 → event:双时态Schema升级
Schema → event:双时态Schema升级
废弃设计 → event:多版本事件设计废弃
