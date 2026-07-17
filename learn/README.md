# Agentic RAG 项目学习课程

本目录用于把当前项目拆解成一套可执行的学习课程。目标不是只看懂代码，而是在学完后能掌握 `docs/知识库项目计划.md` 中「技术栈规划」覆盖的核心能力，并沉淀出自己的 demo、笔记和分享材料。

## 学习目标

学完本课程后，你应该能够：

- 解释一个 Agentic RAG 系统从文档入库到问答返回的完整链路。
- 独立实现文档解析、分块、Embedding、向量检索、关键词检索和混合检索 demo。
- 理解 Pydantic AI Agent 如何通过工具调用连接检索系统。
- 能设计 Query Rewrite、Rerank、Context Builder、Verifier 等增强模块。
- 能为 RAG 系统补充评测、日志、可观测性、安全和部署闭环。
- 能基于当前项目做二次改造，并整理成技术分享。

## 课程结构

每一课都遵循固定结构：

```text
项目案例导读
  -> 阅读当前项目中的真实实现

自己编写 demo 验证
  -> 在 learn 或独立实验目录中写最小可运行 demo

学习总结
  -> 总结原理、项目实现、改造方向和踩坑点
```

## 推荐学习节奏

- 每课 1.5 到 3 小时。
- 每 4 课做一次阶段复盘。
- 不急着改主项目，先用 demo 验证单点能力。
- 每课结束都写 `summary.md`，为后续分享做素材。

## 课时列表

| 课时 | 主题 | 主要能力 |
|---:|---|---|
| 01 | 项目启动与系统全景 | 运行、架构、链路总览 |
| 02 | FastAPI、配置与服务边界 | API、SSE、Docker 配置 |
| 03 | 数据模型与 pgvector 底座 | 表设计、索引、SQL 函数 |
| 04 | 文档解析 | PDF 到 Markdown 文本 |
| 05 | 分块策略 | Recursive / Semantic Chunking |
| 06 | Embedding 流水线 | 向量生成、模型配置 |
| 07 | 向量检索 | pgvector 相似度召回 |
| 08 | 关键词检索 | PostgreSQL FTS / BM25 思路 |
| 09 | 混合检索 | Vector + Keyword 融合排序 |
| 10 | 模型调用与 Prompt | OpenAI-compatible / Responses / Prompt |
| 11 | 工具调用 | Tool schema、Tool registry |
| 12 | Agent 工作流 | Agent 编排、状态、会话 |
| 13 | 查询理解与改写 | Query Rewrite、Intent Detection |
| 14 | Rerank 与上下文构建 | Top-k 优化、引用、上下文压缩 |
| 15 | 评测与可观测性 | Golden Set、Trace Log、Prompt Log |
| 16 | 安全与工程交付 | 权限、注入防护、Docker、CI |

## 配套文档

- [课程总览](课程总览.md)
- [技术栈知识点映射](技术栈知识点映射.md)
- [课程执行模板](课程执行模板.md)

