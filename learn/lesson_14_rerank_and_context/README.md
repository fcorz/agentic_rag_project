# 第 14 课：Rerank 与上下文构建

## 学习目标

掌握 Rerank、Context Builder、Citation Builder 和答案 grounding。

## 项目案例导读

阅读：

- `agent/tools.py` 的检索结果结构
- `agent/models.py` 的 `ChunkResult`
- `agent/prompts.py`

重点问题：

- 当前项目是否有显式 rerank？
- 检索结果如何进入模型上下文？
- 如何让回答带来源？

## 自己编写 demo 验证

任务：

- 对 top-10 chunks 做规则 rerank。
- 写一个 LLM rerank prompt。
- 构建带来源编号的 context。
- 输出带 citation 的回答样例。

建议产物：

- `demo/rerank_demo.py`
- `demo/context_builder.py`
- `summary.md`

## 学习总结

总结：

- Rerank 如何降低 token 消耗。
- Context Builder 如何去重、截断、保留来源。
- Citation Builder 如何增强可信度。

## 验收标准

- 能实现一个轻量 rerank。
- 能设计一个可追溯回答格式。

