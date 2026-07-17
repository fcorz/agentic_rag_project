# 第 07 课：向量检索

## 学习目标

掌握 pgvector 相似度搜索，以及 query embedding 到 chunk 召回的流程。

## 项目案例导读

阅读：

- `sql/schema.sql` 的 `match_chunks`
- `agent/db_utils.py` 的 `vector_search`
- `agent/tools.py` 的 `vector_search_tool`

重点问题：

- `<=>` 运算符表示什么？
- 为什么返回 similarity 要用 `1 - distance`？
- 向量检索擅长和不擅长什么？

## 自己编写 demo 验证

任务：

- 写一个最小 query -> embedding -> vector search 脚本。
- 调整 `limit`，观察召回结果。
- 记录相似度分数。

建议产物：

- `demo/vector_search_demo.py`
- `demo/results.md`
- `summary.md`

## 学习总结

总结：

- 向量检索的核心 SQL。
- top-k 的选择对上下文质量的影响。
- 当前项目向量检索还能如何增强。

## 验收标准

- 能写出向量检索 SQL。
- 能解释为什么语义相近不等于事实正确。

