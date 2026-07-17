# 第 13 课：查询理解与改写

## 学习目标

掌握 Query Rewrite、Intent Detection 和 Structured Planning 的最小实现。

## 项目案例导读

阅读：

- `agent/api.py` 中构建历史上下文的逻辑
- `agent/prompts.py`
- `agent/tools.py`

重点问题：

- 用户原始问题为什么不总适合直接检索？
- 历史会话如何影响当前问题？
- 什么问题应该拒绝检索或要求澄清？

## 自己编写 demo 验证

任务：

- 写一个 query rewrite prompt。
- 输入 5 个口语化问题，输出检索友好问题。
- 实现 intent 分类：事实、总结、比较、无关、澄清。

建议产物：

- `demo/query_rewrite.py`
- `demo/intent_examples.md`
- `summary.md`

## 学习总结

总结：

- Query Rewrite 对召回质量的影响。
- Intent Detection 如何决定检索策略。
- Structured Planning 如何转成 Agent 状态。

## 验收标准

- 能写出 query rewrite demo。
- 能解释查询理解在 RAG 链路中的位置。

