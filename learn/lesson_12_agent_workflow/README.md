# 第 12 课：Agent 工作流

## 学习目标

理解当前项目的 Agent 编排方式，并能设计多阶段 Agent 工作流。

## 项目案例导读

阅读：

- `agent/agent.py`
- `agent/api.py` 的 `execute_agent`
- `agent/api.py` 的 `chat_stream`
- `agent/db_utils.py` 的会话函数

重点问题：

- 当前项目如何将历史会话加入 prompt？
- Agent 如何选择工具？
- 流式输出时如何保存消息？

## 自己编写 demo 验证

任务：

- 写一个三阶段伪工作流：plan -> retrieve -> answer。
- 每一步输出 state。
- 加一个失败分支：检索为空时要求澄清。

建议产物：

- `demo/simple_agent_workflow.py`
- `demo/state_trace.json`
- `summary.md`

## 学习总结

总结：

- Pydantic AI 工具驱动 Agent 的优点。
- LangGraph 或自研状态机适合什么场景。
- Verifier / Repair Agent 应放在哪一步。

## 验收标准

- 能画出当前项目 Agent 调用链。
- 能描述一个多阶段 Agent 工作流。

