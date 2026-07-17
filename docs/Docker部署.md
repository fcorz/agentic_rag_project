# Docker 部署

本文用于通过 Docker Compose 一键启动 PostgreSQL、FastAPI API 和 Streamlit UI。适合快速演示和本地完整环境复现。

## 前置条件

- Docker
- Docker Compose
- OpenAI API Key

## 1. 创建环境变量

在项目根目录创建 `.env`：

```bash
cat > .env <<'EOF'
APP_ENV=development
LOG_LEVEL=INFO
APP_HOST=0.0.0.0
APP_PORT=8058
API_URL=http://api:8058

SERVER_PORT=8501
SERVER_HOST=0.0.0.0

DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432
DB_NAME=vector_db

OPENAI_API_KEY=your_openai_api_key
OPENAI_BASE_URL=https://cc.addcn.com/droid/claude
OPENAI_API_MODE=responses
LLM_CHOICE=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small
EOF
```

注意：

- 容器内服务连接 PostgreSQL 时，`DB_HOST=postgres`，`DB_PORT=5432`。
- UI 容器访问 API 容器时，`API_URL=http://api:8058`。
- 如果使用 OpenAI-compatible 模型网关，配置 `OPENAI_BASE_URL`。
- 如果模型网关只支持 OpenAI Responses API，配置 `OPENAI_API_MODE=responses`；默认值是 `chat`，会调用 `/chat/completions`。
- PostgreSQL 暴露到宿主机的端口是 `6543`，这是给宿主机工具连接数据库用的。

## 2. 构建并启动服务

```bash
docker compose up -d --build
```

查看服务状态：

```bash
docker compose ps
```

查看日志：

```bash
docker compose logs -f api
docker compose logs -f ui
docker compose logs -f postgres
```

## 3. 验证服务

API 健康检查：

```bash
curl http://localhost:8058/health
```

API 文档：

```text
http://localhost:8058/docs
```

Streamlit UI：

```text
http://localhost:8501
```

## 4. 执行文档入库

项目中的 `documents/` 目录会被复制进镜像；开发环境下 `docker-compose.override.yml` 会把当前目录挂载到容器 `/app`，因此也可以直接把 PDF 放到宿主机 `documents/`。

执行入库：

```bash
docker compose exec api python -m ingestion.ingest --documents documents/ --clean
```

查看文档列表：

```bash
curl http://localhost:8058/documents
```

## 5. 调用问答接口

```bash
curl -X POST http://localhost:8058/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "请根据知识库回答问题",
    "user_id": "docker-user",
    "search_type": "hybrid"
  }'
```

## 6. 停止和清理

停止服务：

```bash
docker compose down
```

停止并删除数据库卷：

```bash
docker compose down -v
```

删除数据库卷会清空已入库文档、会话和消息。

## 7. 更新代码后重新部署

```bash
docker compose up -d --build
docker compose logs -f api
```

如果只是 Python 代码变更，并且当前启用了 `docker-compose.override.yml` 的卷挂载和 `--reload`，开发环境通常不需要重建镜像。

## 常见问题

### API 容器启动失败

查看日志：

```bash
docker compose logs api
```

重点检查：

- `.env` 是否存在。
- `OPENAI_API_KEY` 是否配置。
- `DB_HOST` 是否为 `postgres`。
- `DB_PORT` 是否为 `5432`。

### UI 健康检查失败

容器部署时 UI 默认访问：

```text
http://api:8058
```

如果你在浏览器侧边栏手动改 API URL，应使用宿主机地址：

```text
http://localhost:8058
```

### 本机数据库工具如何连接 PostgreSQL

使用：

```text
host: localhost
port: 6543
database: vector_db
user: postgres
password: postgres
```
