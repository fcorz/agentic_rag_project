# 第 08 课：关键词检索

## 学习目标

掌握 PostgreSQL FTS，并理解 BM25 思路和关键词召回的价值。

## 项目案例导读

阅读：

- `sql/schema.sql` 的 `to_tsvector`
- `sql/schema.sql` 的 `plainto_tsquery`
- `sql/schema.sql` 的 `ts_rank_cd`
- `idx_chunks_content_trgm`

重点问题：

- 关键词检索适合哪些问题？
- FTS 和 trigram 索引分别解决什么？
- 为什么向量检索对精确词可能不敏感？

## 自己编写 demo 验证

任务：

- 建一个最小文本表。
- 用 PostgreSQL FTS 查询关键词。
- 用包含产品名、编号、人名的问题做实验。

建议产物：

- `demo/fts_demo.sql`
- `demo/keyword_vs_vector.md`
- `summary.md`

## 学习总结

总结：

- 关键词召回和语义召回的差异。
- BM25 思路和 `ts_rank_cd` 的关系。
- 中文场景下 FTS 可能遇到的问题。

## 验收标准

- 能写出 FTS 查询。
- 能举例说明关键词检索比向量检索更好的场景。

