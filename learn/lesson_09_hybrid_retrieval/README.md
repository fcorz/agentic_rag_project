# 第 09 课：混合检索

## 学习目标

掌握 Vector + Keyword 的融合召回、分数加权和排序策略。

## 项目案例导读

阅读：

- `sql/schema.sql` 的 `hybrid_search`
- `agent/db_utils.py` 的 `hybrid_search`
- `agent/tools.py` 的 `hybrid_search_tool`

重点问题：

- 当前项目如何合并 vector results 和 text results？
- `text_weight` 如何影响排序？
- 混合检索为什么比单一路径更稳？

## 自己编写 demo 验证

任务：

- 写一个最小 hybrid search SQL。
- 分别设置 `text_weight=0.1/0.3/0.7`。
- 对同一问题比较排序变化。

建议产物：

- `demo/hybrid_search.sql`
- `demo/weight_experiment.md`
- `summary.md`

## 学习总结

总结：

- 分数归一化和权重融合的问题。
- 去重策略。
- metadata filter 在混合检索中的位置。

## 验收标准

- 能解释混合检索流程。
- 能设计一个带 metadata filter 的检索方案。

