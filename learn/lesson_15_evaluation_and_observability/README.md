# 第 15 课：评测与可观测性

## 学习目标

掌握 Golden Set、基础 RAG eval、trace log、prompt log 和 retrieval log。

## 项目案例导读

阅读：

- `tests/`
- `agent/api.py` 的日志
- `agent/db_utils.py` 的会话与消息记录

重点问题：

- 当前测试覆盖了哪些内容？
- 评测 RAG 时应该看召回还是答案？
- 一次问答应该记录哪些 trace 信息？

## 自己编写 demo 验证

任务：

- 编写 5 条 golden questions。
- 记录每条问题的 expected answer 和 expected source。
- 运行检索并人工打分。
- 生成一次问答 trace JSON。

建议产物：

- `demo/golden_set.json`
- `demo/eval_runner.py`
- `demo/sample_trace.json`
- `summary.md`

## 学习总结

总结：

- RAG 评测指标：recall、faithfulness、answer relevance。
- Prompt log 和 retrieval log 的排障价值。
- 可观测性如何支持持续优化。

## 验收标准

- 能写出一个最小评测集。
- 能生成一次完整 trace。

