# 第 04 课：文档解析

## 学习目标

掌握 PDF 文档如何被解析成 Markdown 文本和 metadata。

## 项目案例导读

阅读：

- `ingestion/extract_files.py`
- `ingestion/ingest.py`

重点问题：

- Docling 输出了哪些内容？
- metadata 中的 pages、tables、pictures 有什么用途？
- 文档解析失败时应该如何处理？

## 自己编写 demo 验证

任务：

- 用 Docling 解析一个 PDF。
- 打印 Markdown 文本前 1000 字。
- 打印 metadata。
- 对比开启和关闭 table/image 解析的效果。

建议产物：

- `demo/parse_pdf.py`
- `demo/output.md`
- `summary.md`

## 学习总结

总结：

- 非结构化文档如何进入 RAG。
- 表格和图片信息对知识库的影响。
- 如果扩展 DOCX、Markdown、TXT，入口应如何设计。

## 验收标准

- 能独立解析 PDF 并得到文本。
- 能说明为什么解析质量会影响最终问答质量。

