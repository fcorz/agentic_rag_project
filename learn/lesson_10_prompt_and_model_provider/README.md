# 第 10 课：模型调用与 Prompt

## 学习目标

掌握 OpenAI-compatible API、Responses API、模型配置、Prompt Template 和结构化输出思路。

## 项目案例导读

阅读：

- `agent/providers.py`
- `agent/prompts.py`
- `.env`

重点问题：

- `OPENAI_BASE_URL` 解决什么问题？
- `OPENAI_API_MODE=responses` 和 `chat` 有什么区别？
- Prompt 如何影响检索和工具调用？

## 自己编写 demo 验证

任务：

- 写一个最小模型调用 demo。
- 分别测试 chat completions 和 responses 两种模式。
- 写一个要求 JSON 输出的 prompt。

建议产物：

- `demo/llm_call.py`
- `demo/structured_output.md`
- `summary.md`

## 学习总结

总结：

- 模型调用稳定性需要哪些配置。
- Prompt Template 和 Structured Output 的关系。
- 当前项目模型 provider 的扩展点。

## 验收标准

- 能解释当前项目为什么需要 Responses API。
- 能独立写出一次模型调用。

