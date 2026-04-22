# Research & Evidence Standard（调研与证据标准）

适用：
- Track：Research / Software / Writing
- Level：L2（建议）/ L3（强制）

目的：
把“我查过了/我看过了”变成可复查的事实：
- 查了哪些来源（可打开、可定位）
- 抽取了哪些关键事实（短句）
- 这些事实如何改变方案/验收/验证（Impact）
- 哪些仍不确定（Open questions）

对应协议：
- `protocols/02-deep-reading-and-research.md`（深读与外部检索）
- `protocols/00-hard-gates.md`：G2/G3/G8

---

## 1) 研究不是堆链接：必须服务于“可落地 Plan”

Research 的输出必须能直接推动 Plan 的关键段落：
- Candidate Solutions（路线对比）
- Tech Stack / Versions / License Notes
- 风险登记与边界条件
- 验证矩阵（用什么数据、怎么验）

如果 Research Brief 不能回答“这条来源让我们做出了什么不同决策”，就不算有效研究。

---

## 2) Source Ranking（来源优先级）

从高到低：
1) 官方文档 / 标准 / RFC / 论文原文 / 源码（第一优先）
2) 权威二手总结（需要交叉验证）
3) 社区帖子/博客（只能当线索，不得作为唯一依据）

强制要求：
- 涉及“最新/当前/版本变化/兼容性/许可证”时，必须以一手资料为主，并记录日期/版本号。

---

## 3) 最低研究包（建议写进 Plan 的门禁）

当任务属于 L3 且需要外部事实时：
- 来源数量：≥ 8
- 一手来源：≥ 3
- 源码/issue 证据：≥ 1
- 每条来源必须写：Extracted facts + Impact

当用户明确禁止联网：
- G3 必须标记为 blocked
- Plan 必须把缺失事实写成 blocker，并列出最小替代输入（用户提供文档/版本/内部说明）

---

## 4) Research Log（结构化记录格式）

建议记录到 Plan 的 Research Log 表，或单独文件（模板见 `templates/ResearchLog.template.md`）。

每条条目至少包含：

- Query：检索关键词
- Source：链接或可定位入口
- Source type：official/standard/paper/source-code/other
- Extracted facts：≤ 5 条短句
- Impact on plan：影响了哪条路线/哪个验收/哪个风险/哪个验证点
- Open questions：仍待确认

---

## 5) 深读（Deep Reading）与 Research 的分工

深读（Deep Reading）优先读：
- 用户材料（需求/约束/失败样例）
- 仓库现状（入口/模块/数据/验证入口）

Research（Web Research）补外部事实：
- 库的边界行为、版本差异、已知坑
- 标准、论文与基线
- 许可证与合规风险

两者都必须落盘；不落盘就是不可交接、不可复查。

---

## 6) Evidence Index（证据索引）最小要求

任何关键结论都必须指向一个证据入口：
- 文件路径（报告/日志/截图）
- 命令行与退出码
- 引用条目（链接/doi/版本）

建议把 Evidence 按层次组织（与 Validate scope 对齐）：
- micro-check
- checkpoint
- milestone
- final

---

## 7) Research 的输出模板（Brief）

Research Brief 建议按下面结构输出（每段 3–7 行，避免散）：

1) **Current state**：主流做法/共识
2) **Gaps**：痛点/局限/争议点
3) **Candidate paths**：2–3 条可落地路线（含成本/风险/验证）
4) **Validation plan**：指标/基线/数据/最小实验（或工程验证）
5) **Risks**：合规/数据/版本/性能/可维护性

