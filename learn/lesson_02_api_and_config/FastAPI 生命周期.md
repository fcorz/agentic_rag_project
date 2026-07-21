# 一、一个请求的生命周期怎么走

以访问 `/health` 为例，请求大致会经历下面这些阶段：

## 1）应用启动阶段
在任何请求到来之前：

- 创建 `app = FastAPI(...)`
- 执行 `lifespan` 启动部分
- 初始化数据库、模型、缓存等资源

也就是：

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.xxx = ...
    yield
    # shutdown cleanup
```

---

## 2）请求进入 ASGI 服务器
比如 Uvicorn 收到一个请求：

```http
GET /health HTTP/1.1
```

Uvicorn 会把请求交给 FastAPI 应用。

---

## 3）路由匹配
FastAPI 会去找：

- path 是否是 `/health`
- method 是否是 `GET`

如果匹配到：

```python
@app.get("/health")
```

就进入这个处理函数。

---

## 4）依赖注入处理
如果你的接口定义里有 `Depends(...)`，FastAPI 会先解析依赖。

例如：

```python
@app.get("/health")
def health(db=Depends(get_db)):
    ...
```

这时会先执行 `get_db()`。

---

## 5）执行你的接口函数
比如：

```python
@app.get("/health", response_model=HealthStatus)
def health():
    return {"status": "ok"}
```

FastAPI 调用这个函数，得到返回值。

---

## 6）响应模型校验和转换
因为你写了：

```python
response_model=HealthStatus
```

FastAPI 会把返回值按 `HealthStatus` 做：

- 数据校验
- 字段过滤
- 序列化转换

例如如果 `HealthStatus` 是：

```python
class HealthStatus(BaseModel):
    status: str
```

那么返回：

```python
{"status": "ok"}
```

会被检查并转换成标准 JSON 响应。

---

## 7）返回 HTTP 响应
最终 FastAPI 把结果包装成响应发回客户端。

---

# 二、请求生命周期可以简单理解成

```text
应用启动
  -> lifespan 初始化
    -> 收到请求
      -> 路由匹配
        -> 依赖解析
          -> 调用接口函数
            -> response_model 校验/序列化
              -> 返回响应
    -> 应用关闭
  -> lifespan 清理
```

---

# 三、一个请求级别的更完整流程

如果你想更精确地理解，一个请求通常还会经历：

- 中间件进入
- 解析请求体 / query / header / cookie
- 参数校验
- 依赖注入
- 执行视图函数
- 异常处理
- 响应序列化
- 中间件退出

---

# 四、`app` 对象和请求的关系

## `app` 是全局对象
它负责：

- 注册路由
- 管理生命周期
- 持有共享状态 `app.state`
- 管理中间件、依赖、异常处理等

## 请求不是 `app` 本身
每个请求都是一个独立的 `Request`。

你可以理解为：

- `app`：服务整体
- `request`：一次访问

---

# 五、`app.state` 和请求共享

如果你在 `lifespan` 中放了：

```python
app.state.db = db_pool
```

那么每个请求都可以通过：

```python
request.app.state.db
```

访问这个全局资源。

这就是为什么 `lifespan` 初始化的东西能被所有请求共享。

---

# 六、一个简单例子

```python
from fastapi import FastAPI, Request
from pydantic import BaseModel
from contextlib import asynccontextmanager

class HealthStatus(BaseModel):
    status: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.service_name = "Agentic RAG"
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/health", response_model=HealthStatus)
async def health(request: Request):
    return {"status": f"{request.app.state.service_name} is healthy"}
```

这里：

- `lifespan` 启动时设置了全局状态
- `/health` 请求到来时读取 `app.state`
- 返回值再经过 `response_model` 校验

---

# 七、总结一句话

**是的，`@app.get(...)` 就是在使用全局 `app = FastAPI(...)` 对象。**  
一个请求的生命周期大致是：

> 应用启动 → lifespan 初始化 → 请求进入 → 路由匹配 → 依赖解析 → 执行接口 → response_model 处理 → 返回响应 → 应用关闭时清理

---