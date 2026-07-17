# 第 06 课：Embedding 流水线

## 学习目标

掌握文本向量化、embedding 模型配置、批量 embedding 和向量入库。

## 项目案例导读

阅读：

- `ingestion/ingest.py`
- `agent/tools.py`
- `agent/providers.py`

重点问题：

- 文档入库时在哪里生成 embedding？
- 查询时在哪里生成 query embedding？
- 聊天模型和 embedding 模型为什么要分开配置？

## 自己编写 demo 验证

任务：

- 对 3 段文本生成 embedding。
- 计算两两 cosine similarity。
- 将 embedding 写入 PostgreSQL。

建议产物：

- `demo/embed_texts.py`
- `demo/similarity.py`
- `summary.md`

## 学习总结

总结：

- embedding 的输入、输出和维度。
- base_url/key 对聊天模型和 embedding 模型的影响。
- 如果网关不支持 embedding，应如何拆分配置。

## 验收标准

- 能生成一条文本向量。
- 能解释 embedding 维度和 pgvector 字段的关系。

