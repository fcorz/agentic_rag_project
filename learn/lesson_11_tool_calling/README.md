# 第 11 课：工具调用

## 学习目标

掌握 Tool Calling、工具输入 schema、工具注册和结果转换。

## 项目案例导读

阅读：

- `agent/agent.py`
- `agent/tools.py`
- `agent/models.py` 的 `ToolCall`

重点问题：

- 工具函数的 docstring 为什么重要？
- Pydantic 输入模型如何约束工具参数？
- Agent 如何把检索结果转成回答上下文？

## 自己编写 demo 验证

任务：

- 注册一个 `calculator` 工具。
- 注册一个 `lookup_user` 工具。
- 让模型判断什么时候调用工具。
- 打印 tool name、args、result。

建议产物：

- `demo/tool_calling_demo.py`
- `summary.md`

## 学习总结

总结：

- Tool Registry 的意义。
- Tool Calling 和普通函数调用的区别。
- MCP-like contract 可以如何设计。

## 验收标准

- 能独立定义一个工具并让 Agent 调用。
- 能解释工具输入输出 schema 的价值。

