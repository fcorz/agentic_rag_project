# 第 03 课：数据模型与 pgvector 底座

## 学习目标

理解 RAG 系统的数据表设计、pgvector 字段、索引和数据库函数。

## 项目案例导读

阅读：

- `sql/schema.sql`
- `agent/db_utils.py`

重点问题：

- `documents` 和 `chunks` 为什么分开？
- `sessions` 和 `messages` 如何支持会话？
- `match_chunks` 如何完成向量检索？
- `hybrid_search` 如何融合向量和关键词？

## 自己编写 demo 验证

任务：

- 建一个最小 `demo_documents`、`demo_chunks` 表。
- 插入 3 条手工向量。
- 使用 pgvector 查询最相似文本。

建议产物：

- `demo/schema.sql`
- `demo/query.sql`
- `summary.md`

## 学习总结

总结：

- pgvector 的向量字段和距离运算。
- ivfflat、GIN、trigram 索引的职责差异。
- 当前 schema 的优点和不足。

## 验收标准

- 能写出一个最小 pgvector 查询。
- 能解释 embedding 维度为什么必须和字段定义一致。

