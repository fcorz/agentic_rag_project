# 第 02 课：FastAPI、配置与服务边界

## 学习目标

掌握 FastAPI 生命周期、环境变量、Docker 网络和 SSE 流式响应。

## 项目案例导读

阅读：

- `agent/api.py`
- `ui/app.py`
- `agent/models.py`
- `docker-compose.yml`
- `.env`

重点问题：

- `lifespan` 在什么时候执行？
- Docker 容器内为什么使用 `http://api:8058`？
- 浏览器为什么使用 `http://localhost:8058`？
- `/chat/stream` 如何返回 SSE？

## 自己编写 demo 验证

任务：

- 写一个最小 FastAPI 服务，包含 `/health`。
- 写一个 `/stream` 接口，每秒返回一段文本。
- 写一个 Streamlit 页面消费该流式接口。

建议目录：

```text
demo/
├── api_demo.py
└── streamlit_demo.py
```

## 学习总结

总结：

- 本机、容器、浏览器三种访问地址差异。
- SSE 的事件格式。
- 配置错误如何通过日志排查。

## 验收标准

- 能独立写出一个 SSE demo。
- 能解释 `API_URL` 在本机部署和 Docker 部署中的不同值。

