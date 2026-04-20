# library（工程参考检查表）索引

> 目标：把 `Reference/` 里的材料提炼成“可执行的检查表/门禁语句”，并在 stages 中以索引方式挂接。

本目录是**可复用清单库**：
- library 负责“清单与门禁”
- stages 负责“触发条件与工件契约”（不要在 stages 里堆长清单）

---

## 如何使用（渐进式披露）

1) 先路由：`stages/router/SKILL.md`
2) Router 决定下一阶段：只读一个 stage
3) stage 内遇到触发条件时，再按索引查 library 里的对应清单

---

## library 文件一览

- `requirements-acceptance.md`
  - 需求分类、验收标准、验收契约（可测试断言）
- `architecture-tradeoffs.md`
  - 架构维度、质量属性、取舍、决策记录（ADR）
- `design-construction.md`
  - 设计原则、构建实践、降低复杂度、把设计落到 Task
- `complexity-modularity.md`
  - 复杂度管理、模块深度、信息隐藏、耦合/内聚
- `iteration-feedback.md`
  - 迭代、反馈回路、经验主义、实验驱动
- `testing-verification.md`
  - 测试策略、证据门禁、验证矩阵、失败判据
- `plan-mode-interaction.md`
  - Plan Mode 的对齐与提问收敛（少而关键、默认值策略、执行授权门禁）
- `development-paradigms.md`
  - 开发范式协同：SDD/Characterization/Spike/BDD/契约优先/可观测性排障
- `quality-operations-maintenance.md`
  - 质量目标、运维可运行性、维护与演化
- `documentation-writing.md`
  - 文档/教程/论文写作的结构、图示、引用与一致性
- `reproducibility.md`
  - Research/Software/Writing 的复现协议与实验记录
- `risk-security.md`
  - 风险识别、合规门禁、安全检查
- `project-governance.md`
  - 里程碑/依赖/风险矩阵/验收契约的组织与更新时机
- `traceability.md`
  - 用户诉求 → stage/template/工件 的追溯表（用于审计“一条需求落到了哪里”）

---

## Stage → library（常见挂接）

| Stage | 何时需要查 library | 推荐文件 |
|---|---|---|
| Router | 复杂度不确定/风险信号/要不要上 L3 治理 | `risk-security.md`, `project-governance.md` |
| Brainstorm | 方案对比、架构取舍、可验证性不足 | `architecture-tradeoffs.md`, `iteration-feedback.md` |
| Research | 要找基线/指标/相关工作/证据链 | `iteration-feedback.md`, `reproducibility.md` |
| Plan | 写验收、拆里程碑、定义验证与复现、对齐与收敛 | `plan-mode-interaction.md`, `requirements-acceptance.md`, `architecture-tradeoffs.md`, `project-governance.md`, `testing-verification.md` |
| Execute | 设计/实现细化、控制复杂度与耦合、选择合适范式 | `development-paradigms.md`, `design-construction.md`, `complexity-modularity.md`, `iteration-feedback.md`, `testing-verification.md` |
| Validate | 需要证据门禁与验证矩阵 | `testing-verification.md`, `reproducibility.md` |
| Review | 按证据打分、决定返工 | `testing-verification.md`, `quality-operations-maintenance.md`, `project-governance.md` |
| Write | 要写结构/图示/引用/可运行示例 | `documentation-writing.md`, `reproducibility.md` |

---

## 主要来源（Reference）

以下来源被用于 library 的清单提炼（每条清单会标注具体章节）：

- `Reference/Software Engineering Body of Knowledge v4.0a/Software Engineering Body of Knowledge v4.0a.md`
  - 知识域覆盖：requirements / architecture / design / construction / testing / maintenance / quality / security / management 等
- `Reference/Modern Software Engineering/Modern Software Engineering.md`（David Farley）
  - 迭代、反馈回路、经验主义、增量设计、复杂度管理
- `Reference/A Philosophy of Software Design/A Philosophy of Software Design.md`（John Ousterhout）
  - 复杂度、信息隐藏、深模块、错误设计、注释作为设计工具
- `Reference/Head First Software Architecture/Head First Software Architecture.md`（Gandhi/Richards/Ford）
  - 架构维度、质量属性、架构决策与风格取舍
- `Reference/The Software Engineers Guidbook/The Software Engineers Guidbook.md`（Gergely Orosz）
  - 生产力、协作、工程实践、测试、架构与交付
