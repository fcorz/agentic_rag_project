# 第 05 课：分块策略

## 学习目标

掌握 recursive chunking、semantic chunking，以及 parent-child chunking 的设计思路。

## 项目案例导读

阅读：

- `ingestion/chunker.py`
- `agent/models.py` 的 `IngestionConfig`

重点问题：

- chunk size 和 chunk overlap 如何影响召回？
- semantic chunking 为什么需要 embedding？
- 当前项目如何在 semantic chunking 失败时 fallback？

## 自己编写 demo 验证

任务：

- 手写一个基于字符长度的 chunker。
- 调用当前项目的 `PDFSemanticChunker`。
- 对同一文本分别设置 300、800、1500 三种 chunk size。
- 记录 chunk 数量和内容完整性。

建议产物：

- `demo/simple_chunker.py`
- `demo/chunking_experiment.md`
- `summary.md`

## 学习总结

总结：

- 分块策略和召回质量的关系。
- 什么时候适合 parent-child chunking。
- 当前项目分块策略的改造方向。

## 验收标准

- 能独立实现一个基础 chunker。
- 能解释 overlap 的作用。

