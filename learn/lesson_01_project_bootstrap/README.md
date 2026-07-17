# 第 01 课：项目启动与系统全景

## 学习目标

跑通项目，并能解释 API、UI、PostgreSQL、文档入库和 Agent 问答之间的关系。

## 项目案例导读

阅读：

- `README.md`
- `docker-compose.yml`
- `agent/api.py`
- `ingestion/ingest.py`
- `sql/schema.sql`

重点问题：

- 项目启动后有哪些服务？
- 文档入库链路和问答链路分别经过哪些模块？
- API、UI、数据库之间如何通信？

## 自己编写 demo 验证

任务：

- 画一张 RAG 全链路图。
- 使用 curl 调用 `/health`、`/documents`。
- 在 UI 中完成一次对话，并记录 API 日志。

建议产物：

- `summary.md`
- `rag-flow.md`

## 学习总结

总结：

- 当前项目的系统边界。
- 一次文档入库的完整流程。
- 一次用户提问的完整流程。

## 验收标准

- 能画出完整调用链。
- 能说清每个目录的职责。
- 能解释为什么访问 `/` 返回 Not Found，但 `/health` 正常。

