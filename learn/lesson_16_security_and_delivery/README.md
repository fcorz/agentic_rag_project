# 第 16 课：安全与工程交付

## 学习目标

掌握权限过滤、Prompt Injection 防护、PII Masking、Docker 部署和上线检查。

## 项目案例导读

阅读：

- `docker-compose.yml`
- `Dockerfile`
- `docs/Docker部署.md`
- `docs/线上单机服务部署.md`
- `agent/models.py`
- `sql/schema.sql`

重点问题：

- 企业知识库为什么必须先做权限过滤？
- Prompt Injection 可能来自用户输入还是文档内容？
- 生产部署需要哪些检查项？

## 自己编写 demo 验证

任务：

- 给文档 metadata 加 `tenant_id`。
- 检索时增加 metadata filter。
- 写一个 prompt injection 检测 demo。
- 写一个手机号/邮箱 PII masking demo。
- 整理上线 checklist。

建议产物：

- `demo/tenant_filter.sql`
- `demo/prompt_injection_guard.py`
- `demo/pii_masking.py`
- `delivery_checklist.md`
- `summary.md`

## 学习总结

总结：

- 权限过滤应该发生在检索前。
- Prompt Injection 防护的边界。
- Docker Compose、迁移、CI、Makefile 分别解决什么工程问题。

## 验收标准

- 能设计 tenant 级权限过滤。
- 能写出基础 PII masking。
- 能列出一份上线前检查清单。

