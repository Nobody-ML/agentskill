> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Plan：<任务/项目名称>

版本：`vX.Y.Z`（或日期）  
Track：Research / Software / Writing / Simple  
Level：L0 / L1 / L2 / L3  
WorkType（仅 Software）：Build / Debug / Ops  
Execution Authorization（L2/L3 强制）：required / received / not_required

---

## 0. 执行授权（Execution Authorization）【L2/L3 强制】

> 门禁：状态不是 `received` 时，不进入 Execute/Write（保持 Plan Mode）。

- 状态：required / received / not_required
- 授权口令：`开始执行`
- 授权方式：为避免误判，建议用户独立消息或独立一行回复 `开始执行`
- 授权时间：YYYY-MM-DD HH:MM
- 授权范围（scope）：允许执行的目录/环境/边界

---

## 1. 目标（Goal）

一句话目标：

### 1.0 用户意图锁定（User Intent Lock）【L2/L3 强制】

> 目的：防止“执行阶段跑偏/忽视用户想法/改着改着忘了原需求”。这部分在 Plan 通过后应同步到 `State.md` 的 Memory。

- 用户原始诉求摘要（3–10 条要点，尽量贴近原话但不长段引用）：
- 用户明确要求的不可违背项（与 Non-negotiables 一致）：
- 用户已有想法/方案（如有，写清哪些是用户坚持的，哪些是待讨论的）：
- 已确认决策快照（Decision Snapshot，写成可执行断言）：
  - 决策1：
  - 决策2：

### 1.1 成功标准（验收）
- [ ] 标准1：可观察/可验证
- [ ] 标准2：可观察/可验证

### 1.2 非目标（Non-goals）
- 不做：
- 不做：

### 1.3 不可违背项（Non-negotiables）

> 目的：把用户的硬要求钉住，防止执行过程中“悄悄改方向/偷换验收/擅自降级”。

- 不允许的行为（例如：擅自兜底/降级、跳过真数据验证、跳过证据门禁）：
- 交付必须满足的底线：

---

## 2. 输入材料（Inputs）

> 先写清楚“读了什么”，避免闭门造车。

- 用户提供：文件/链接/数据/约束
- 仓库内资料：路径清单
- 外部资料（如允许）：来源清单

### 2.1 阅读与理解（Read Log）【L2/L3 强制】

> 要求：不是“列文件名”，而是写清读到了什么约束/接口/风险；能直接指导架构与 Task 拆分。

| 条目 | 类型（doc/code/data/log） | 路径/链接 | 摘要（读到的事实） | 关键约束/坑点 | 需要追问/待验证 |
|---|---|---|---|---|---|
| R-001 |  |  |  |  |  |

### 2.2 外部检索与基线（Research Log）【按需；L2/L3 建议强制】

> 要求：优先高质量来源（官方文档/标准/论文/权威博客）；每条必须写“它如何影响本方案”（决策/约束/验证）。

| 条目 | 主题 | 来源（可追溯） | 关键结论 | 对本方案的影响（决策/约束/验证） |
|---|---|---|---|---|
| S-001 |  |  |  |  |

---

## 3. 产出物（Deliverables）

- 交付物1：位置/格式
- 交付物2：位置/格式
- Delivery Report（交付回执，固定格式）：`templates/DeliveryReport.template.md`

（WorkType=Ops 建议）
- Ops Runbook（运行/监控/排障说明）：`templates/Ops-Runbook.template.md`

（论文/报告可选）
- Literature Review Matrix：`templates/Literature-Review-Matrix.template.md`
- Paper Outline：`templates/Paper-Outline.template.md`

---

## 4. 受众与风格（仅 Writing 或对外输出时必填）

- 目标读者：
- 语气与风格：口语/严谨/学术/工程说明
- 长度目标：精简/标准/超详细
- 必须包含的图示：

---

## 5. 约束与边界

- 不能做的事（安全/合规/生产环境/敏感数据）：
- 工具与环境限制：
- 时间/资源预算：
- 兜底/降级策略（默认禁止；如确需，必须写清并经用户确认）：触发条件 → 行为 → 成本/副作用 → 对验收影响 → 验证方式（Decision Log 引用）

---

## 6. 方案概览（Approach）

> 只写“可执行”的方案：结构、关键决策、取舍，不写空泛口号。

### 6.0 候选方案与推荐（Brainstorm Summary）【L2/L3 建议强制】

> 要求：至少 2 个候选路线 + 1 个推荐；不要把选择权丢给用户“随便选”，要给明确默认推荐与理由。

- 方案 A（摘要 + 主要取舍）：
- 方案 B（摘要 + 主要取舍）：
- 推荐方案（为什么它更符合验收/约束/风险）：

（Software 可选）技术选型对比表：

| 维度 | 选项 A | 选项 B | 推荐 |
|---|---|---|---|
| 语言/运行时 |  |  |  |
| 框架/库 |  |  |  |
| 部署/运行方式 |  |  |  |
| 主要风险 |  |  |  |

### 6.0.1 技术链路图（Tech Chain / System Flow）【L2/L3 建议强制】

> 目的：把“从输入到产出”的关键链路画出来，让执行阶段能严格对照，不走偏、不丢验证入口。

- 图示（Mermaid/PlantUML/ASCII 均可）：
- 图注：这张图解释了什么？关键风险点在哪里？

### 6.1 方案摘要
- 路线：
- 关键假设：

### 6.2 关键决策（Decision Log 引用）
- DEC-xxx：

### 6.3 Stakeholders & Concerns【L3 建议强制】

> 使用模板：`templates/Stakeholders-Concerns.template.md`

- 文件位置：
- 关键 stakeholders（摘要）：
- Top concerns（摘要）：

### 6.4 Quality Attributes（质量属性）【L3 建议强制】

> 使用模板：`templates/Quality-Attributes.template.md`

- 文件位置：
- Top attributes（摘要）：

### 6.5 ADR（架构决策记录）【重大决策建议】

> 使用模板：`templates/ADR.template.md`（或写入 State.md Decision Log）

- ADR 存放方式：State.md / 独立文件
- ADR 列表：ADR-001, ADR-002, ...

### 6.6 Development Strategy（开发范式组合）【L2 建议 / L3 强制】

> 参考：`library/development-paradigms.md`

- 采用范式组合（例如：Characterization + 小步修改 + 回归；或 Contract-first + SDD + 最小集成验证）：
- 选择理由（结合风险/约束）：
- 证据策略（这些范式如何产出可复查证据）：

---

## 7. 里程碑（Milestones）

> L3 任务必须拆里程碑；L2 任务建议拆。

- M1：
  - 产出物：
  - 验证方式：
- M2：

---

## 7.0 架构描述（Architecture Description）【L3 建议强制】

最低要求：组件边界 + 依赖方向 + 关键交互路径。

- 组件/边界图：
- 关键时序图：
- 数据流/接口摘要：

## 7.0.1 可执行规范（Spec，SDD）【L2/L3 建议强制】

> 目的：把“需求”落成可实现/可验证的规范，避免 Execute 阶段边写边猜。

- 核心对象/概念（名词表）：
- 外部接口（CLI/API/函数签名/协议）：
- 输入输出示例（含边界与失败示例）：
- 错误语义（错误码/异常类型/错误信息原则）：
- 数据约束与不变量（invariants）：
- 安全/合规边界（不允许出现什么数据/行为）：
- 性能/资源预算（必要时）：

---

## 7.1 依赖与前置条件（Dependency Map）【L3 建议强制】

> 规则：依赖没满足就标记阻塞，不要在 Execute 阶段“硬推”。

| 依赖 | 类型（外部/内部） | Owner/来源 | 获取方式 | 阻塞等级 | 备注 |
|---|---|---|---|---|---|
|  |  |  |  | P0/P1/P2 |  |

---

## 7.2 验收契约（Acceptance Contract）【L3 强制】

> 使用模板：`templates/AcceptanceContract.template.md`

- 契约文件位置：
- 断言数量（预估）：

门禁：缺少验收契约不得进入 Execute（L3）。

---

## 8. 验证方案（Validation Plan）

> “完成/通过”必须绑定证据。

### 8.0 验证数据（Validation Data）【L2/L3 强制】

> 规则：真实数据优先（允许脱敏）；只有在用户确认没有真实样本后，才允许 synthetic。

- data_type：real / sanitized-real / synthetic
- 数据来源入口（文件/链接/采集命令/数据集版本）：
- 敏感信息处理（脱敏/裁剪/权限边界）：
- synthetic（如使用）差距说明与补真数据计划：

### 8.0.1 验证节奏（Cadence）【L2/L3 建议强制】

> 目标：在“不把流程做重”的前提下保持可验证性：组内小批量推进，组末检查点验证，里程碑再做宽验证，最后做总验证与总评审。

- `checkpoint`：任务组级验证（Task.md 的一个大标题末尾）
  - 覆盖：本组改动影响的关键路径/失败模式/边界
  - 维度（Dimensions）：Correctness + Failure Modes（按需加 Spec/Docs）
  - 输出：命令/结果摘要 + data_type 标注 + Evidence Index 入口
- `milestone`：里程碑级验证（Plan.md 的 M1/M2/... 结束）
  - 覆盖：更宽回归 + 性能/资源 smoke check + 规范与文档一致性
  - 维度（Dimensions）：Correctness + Failure Modes + Performance/Resource + Docs/Operability（按需加 Spec/Security）
- `final`：最终总验证（交付前）
  - 覆盖：对照验收标准/验收契约逐条覆盖（尤其 L3）+ 复现要素 + 交付文档与 Runbook
  - 维度（Dimensions）：里程碑维度 + Spec/Consistency +（按风险）Security/Compliance +（Writing/UI）Visual/UX

### 8.1 Software（示例）
- 单元/集成测试：
- 静态检查（lint/typecheck）：
- 手动走通：

### 8.2 Research（示例）
- 指标与基线：
- 最小可行实验（MVE）：
- 复现要素：环境/seed/数据版本/脚本

### 8.3 Writing（示例）
- 引用与来源：
- 示例可运行性：
- 图示可读性：

---

## 8.4 复现协议（Repro Protocol）【按 Track 选择】

- Research：`templates/ReproProtocol-Research.template.md`
- Software：`templates/ReproProtocol-Software.template.md`
- Writing：`templates/ReproProtocol-Writing.template.md`

门禁：涉及实验/指标对比/可运行示例时，复现协议必须可执行。

---

## 9. 评审与打分（Review Plan）

- 评分模板：`templates/ReviewRubric-*.template.md`
- 通过/返工规则：
  - 硬门禁：验证不通过 → 必须返工并复评
  - 软门禁：总分 < 7.0/10 → 需提醒用户并按反馈决定是否返工

---

## 9.1 变更控制（Scope Change）【L3 建议强制】

- 新需求/范围变化：必须回到 Plan 更新验收契约与 Task，再进入 Execute
- 任何跳过验证的决定：必须写入 `State.md` Decision Log

---

## 10. 风险与应对

| 风险 | 影响 | 缓解 |
|---|---|---|
|  |  |  |

---

## 11. 待确认问题（Open Questions）

- Q1：
- Q2：

---

## 12. Plan Mode 退出门禁（Ready-to-Execute Gate）【L2/L3 强制】

> 规则：只有当本门禁满足，才允许请求用户单独回复 `开始执行` 进入 Execution Mode。

- [ ] 目标可复述（1 句话）
- [ ] ≥2 条可验收标准（可观察/可测试/可复现）
- [ ] Non-goals 明确（不会偷换范围）
- [ ] Read Log 已完成（读到的事实/约束/坑点清楚）
- [ ] Research Log 已完成或标注 N/A（基线/来源可追溯）
- [ ] 候选方案与推荐已给出（有取舍理由，不把选择权无限外包给用户）
- [ ] 架构描述 + 可执行规范（Spec）已落盘（接口/错误语义/示例/不变量）
- [ ] 验证数据已明确（real/sanitized-real 优先；synthetic 需用户确认无真实样本）
- [ ] 验证节奏已映射到 Task（checkpoint/milestone/final）
- [ ] Task 已拆到可执行可验收（每条有产出物与验收方式）
- [ ] 兜底/降级策略：默认禁止；如允许已写清并经用户确认（Decision Log）
- [ ] Open Questions 已清空，或已转为 Assumptions 并安排验证任务
