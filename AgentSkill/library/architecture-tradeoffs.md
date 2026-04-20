# Architecture & Trade-offs（架构与取舍）检查表

适用：Software（尤其 L3）、以及任何“要做技术选型/架构决策”的 Research。

---

## 触发条件

- 需要选型（单体/微服务、存储、消息、缓存、DSL/编译链路等）
- 影响范围跨模块/跨团队/跨部署
- 非功能需求是关键（性能/可靠性/安全/可维护性）

---

## A. 先把“架构”讲清楚：谁关心什么

1) 列出 Stakeholders（至少）：
   - 用户/使用者
   - 维护者（未来改代码的人）
   - 运营/部署者（运行系统的人）
   - 安全与合规（如果涉及数据/外部接口）

2) 对每个 stakeholder 写“关注点（Concerns）”：
   - 性能/可用性/成本/可观测性/扩展性/安全等

来源：
- `Reference/Software Engineering Body of Knowledge v4.0a/Software Engineering Body of Knowledge v4.0a.md` — Chapter 02 *Software Architecture*, §1.2 *Stakeholders and Concerns*

落盘模板（推荐）：
- `templates/Stakeholders-Concerns.template.md`

---

## B. 质量属性优先（Architectural characteristics）

架构决策首先服务质量属性，而不是“用什么框架”。

检查项：
- [ ] 明确 3–7 个最重要质量属性（优先级排序）
- [ ] 对每个质量属性给出可验证方式（指标/测试/演练）
- [ ] 明确放弃什么（trade-offs）：例如一致性 vs 可用性、性能 vs 可维护性

来源：
- `Reference/Head First Software Architecture/Head First Software Architecture.md` — Chapter 1（*Architectural characteristics* / *Architectural decisions* / *trade-offs* 相关目录项）
- SWEBOK v4.0a — Chapter 02 *Software Architecture*, §1.3 *Uses of Architecture*

落盘模板（推荐）：
- `templates/Quality-Attributes.template.md`

---

## C. 决策记录（ADR：Architecture Decision Record）

每个“会影响后续成本”的决策必须落盘：
- 问题（Context）
- 决策（Decision）
- 备选方案（Alternatives）
- 拒绝理由（Why not）
- 后果（Consequences）：带风险与缓解

要求：ADR 必须在 `State.md` 的 Decision Log 中可追踪（至少 DEC-XXX 指针）。

落盘模板（可选）：
- `templates/ADR.template.md`

来源：
- SWEBOK v4.0a — Chapter 02 *Software Architecture*, §1.3（架构用于沟通与约束）

---

## D. 架构描述（让结构可读）

最低要求：给出“组件边界 + 依赖方向 + 数据流/调用流”。

建议图示：
- C4 风格（Context/Container/Component）：先大后小
- 时序图（关键交互路径）

来源：
- SWEBOK v4.0a — Chapter 02 *Software Architecture*, §2 *Software Architecture Description*
- `Reference/Head First Software Architecture/Head First Software Architecture.md` — Chapter 1（逻辑组件、架构风格维度）

---

## E. 演化与可变更性（避免“一次性大设计”）

检查项：
- [ ] 先定义最小可验证架构（Walking Skeleton），再迭代演化
- [ ] 每次迭代都能得到反馈（测试/性能基准/用户路径）
- [ ] 用里程碑边界做验证，而不是等到最后

来源：
- `Reference/Modern Software Engineering/Modern Software Engineering.md` — Part II *Optimize for Learning*, Ch.4 *Working Iteratively*, Ch.5 *Feedback*, Ch.6 *Incrementalism*
