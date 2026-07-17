# Agentic RAG 项目

一个现代化的 Agentic RAG（检索增强生成）系统，基于 Pydantic AI、FastAPI 和 PostgreSQL（pgvector）构建。该项目为文档问答类 AI 应用提供了可扩展、模块化、接近生产实践的基础实现。

## 目录

- 功能特性
- 技术栈
- 安装
- 使用
- API 参考
- 项目结构
- 开发
- 测试
- 配置
- 故障排查
- 许可证

## 功能特性

- 基于 Pydantic AI 的智能 Agent 系统
- 多种搜索策略：向量搜索和混合搜索
- 高级 PDF 处理：使用 Docling 提取表格和图片信息
- 数据库：PostgreSQL + pgvector 扩展
- 实时流式响应：通过 Server-Sent Events 输出实时回答
- 会话管理：保留对话历史和上下文
- Docker 容器化：便于部署和复现
- 类型安全：使用 Pydantic 模型处理数据校验
- 即时入库：上传或放置文档后即可构建索引并查询

## 技术栈

### 后端

- Pydantic AI：AI Agent 框架
- FastAPI：现代 Python Web 框架
- LangChain：文档处理和 Embedding
- Docling：PDF 提取和分析
- AsyncPG：PostgreSQL 异步客户端
- pgvector：向量相似度搜索

### 前端

- Streamlit：交互式 Web 界面

### 基础设施

- PostgreSQL 17：主数据库
- Docker Compose：多容器编排
- uv：快速 Python 包安装工具

## 安装

### 前置条件

- Python 3.12+
- Docker 和 Docker Compose
- Git

### 1. 克隆仓库

```bash
git clone https://github.com/serkanyasr/ntt_rag_project.git
cd ntt_rag_project
```

### 2. 设置环境变量

创建 `.env` 文件：

```bash
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
```

### 3. 使用 Docker 启动

```bash
docker compose up -d
docker compose logs -f
```

## 使用

### Web 界面

访问 Streamlit UI：

```text
http://localhost:8501
```

Web 界面包含：

- 交互式聊天：围绕已入库文档提问
- 健康检查：检查 API 连接状态
- 会话管理：保留持续对话上下文

### API 使用

FastAPI 文档：

```text
http://localhost:8058/docs
```

#### Chat 接口示例

```python
import requests

response = requests.post("http://localhost:8058/chat", json={
    "message": "Hello, how can I help you?",
    "session_id": "optional-session-id",
    "user_id": "user-123",
    "search_type": "hybrid"
})
print(response.json())
```

#### 流式 Chat 示例

```python
import requests
import json

response = requests.post(
    "http://localhost:8058/chat/stream",
    json={
        "message": "Give a long explanation",
        "search_type": "hybrid"
    },
    stream=True
)

for line in response.iter_lines():
    if line.startswith(b"data: "):
        data = json.loads(line[6:])
        if data.get("type") == "text":
            print(data.get("content"), end="")
```

### 文档入库

命令行入库：

```bash
cp your_document.pdf documents/
python -m ingestion.ingest --documents documents/
```

## API 参考

### Chat 接口

- `POST /chat`：发送单条聊天消息
- `POST /chat/stream`：流式聊天响应
- `GET /sessions/{session_id}`：获取会话信息

### Search 接口

- `POST /search/vector`：向量搜索
- `POST /search/hybrid`：混合搜索

### 健康检查

- `GET /health`：系统状态检查

### Chat 请求

```json
{
  "message": "Your question",
  "session_id": "optional-session-id",
  "user_id": "user-id",
  "search_type": "hybrid",
  "metadata": {}
}
```

### Search 请求

```json
{
  "query": "Search query",
  "search_type": "vector",
  "limit": 10,
  "filters": {}
}
```

## 项目结构

```text
ntt_rag_project/
├── agent/                  # AI Agent 和业务逻辑
│   ├── agent.py            # Pydantic AI Agent 定义和工具注册
│   ├── api.py              # FastAPI 接口
│   ├── db_utils.py         # 数据库操作
│   ├── models.py           # Pydantic 模型
│   ├── prompts.py          # 系统提示词
│   ├── providers.py        # LLM 和 Embedding Provider
│   └── tools.py            # Agent 工具
├── ingestion/              # 文档处理
│   ├── chunker.py          # 文本分块
│   ├── extract_files.py    # PDF 提取
│   └── ingest.py           # 主入库流水线
├── ui/                     # Streamlit UI
│   └── app.py
├── sql/                    # 数据库 Schema
│   └── schema.sql
├── tests/                  # 测试
├── documents/              # PDF 文档
├── docker-compose.yml      # 容器编排
├── Dockerfile
└── pyproject.toml          # Python 依赖
```

## 主要组件

### Agent

- `agent.py`：Pydantic AI Agent 定义和工具注册
- `api.py`：FastAPI Web 服务和接口
- `tools.py`：向量搜索、混合搜索和文档检索工具
- `db_utils.py`：PostgreSQL 操作和连接管理
- `models.py`：Pydantic 数据模型和校验

### Ingestion

- `ingest.py`：主文档处理流水线
- `extract_files.py`：PDF 文本、表格和图片提取
- `chunker.py`：智能文本分块策略

## 测试

### 运行测试

```bash
pytest
pytest tests/agent/test_models.py
pytest --cov=agent --cov=ingestion
```

### 测试类别

- 模型测试：Pydantic 模型校验
- Agent 测试：AI Agent 功能
- 数据库测试：PostgreSQL 操作
- 入库测试：文档处理

## 开发

### 开发环境设置

```bash
python -m venv venv
source venv/bin/activate
pip install uv
uv pip install -e .
pre-commit install
```

### 日志

```bash
export LOG_LEVEL=DEBUG
docker compose logs -f api
```

## 配置

### 环境变量

| 变量 | 说明 | 默认值 |
|---|---|---|
| `DB_NAME` | PostgreSQL 数据库名 | `rag_db` |
| `DB_USER` | PostgreSQL 用户 | `rag_user` |
| `DB_PASSWORD` | PostgreSQL 密码 | 无 |
| `OPENAI_API_KEY` | OpenAI API Key | 无 |
| `OPENAI_BASE_URL` | OpenAI-compatible API 地址 | 无 |
| `OPENAI_API_MODE` | API 调用模式，可选 `chat` 或 `responses` | `chat` |
| `APP_PORT` | FastAPI 端口 | `8058` |
| `SERVER_PORT` | Streamlit 端口 | `8501` |
| `LLM_CHOICE` | LLM 模型 | `gpt-4o-mini` |
| `EMBEDDING_MODEL` | Embedding 模型 | `text-embedding-3-small` |

### Docker Compose 覆盖配置

可以创建或修改 `docker-compose.override.yml` 来调整开发环境配置，例如挂载本地代码、开启 API 热重载等。

## 故障排查

### 数据库连接错误

```bash
docker compose ps postgres
docker compose logs postgres
```

### OpenAI API 错误

```bash
echo $OPENAI_API_KEY
```

### 端口冲突

```bash
netstat -an | grep :8058
netstat -an | grep :8501
```

## 许可证

MIT License。详见 `LICENSE` 文件。
