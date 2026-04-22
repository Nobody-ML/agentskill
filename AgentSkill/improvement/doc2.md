# text 1

```markdown
这里没有远程仓库写权限，因此我不会把结果说成“已经提交到 GitHub”。下面按 **可直接落盘 / 可直接提交的 v0.3.0-hardening 补丁稿** 给出：先诊断问题，再给目录改造、主入口补丁、核心协议文件、Plan/Task 深度模板、阶段文件修改点，以及本次 0.3.0 自身的 Plan.md / Task.md。

我查到当前仓库已经有 `AgentSkill/`，并且目录内已有 `stages/`、`templates/`、`library/`、`examples/`、`v0.1.0`、`v0.2.0`、`v0.3.0`、`SKILL.md`、`State.md` 等结构；`v0.3.0/` 目前只有 `Plan.md` 与 `Task.md`。这说明当前不是缺少文件夹骨架，而是缺少更强的“硬门禁、抗漂移、深度规划、真实验证、长程续跑”执行层。([GitHub][1])

当前 `SKILL.md` 和各 stage 已经有 Plan Mode、Execution Authorization、State.md、Task Group、无授权不执行等规则，但你给出的失败样例说明这些规则在长对话、上下文压缩、执行压力和模型惯性下仍然会被绕过。也就是说，0.3.0 不能只继续堆说明文字，而要把“建议”升级成“每轮必须检查的状态机”。([GitHub][2])

Agent Skill 的通用实践也支持这种做法：主 `SKILL.md` 应保持为入口和导航，复杂规则拆到引用文件中，靠渐进式披露避免主文件过长；技能目录可以包含 `SKILL.md`、脚本、参考资料、模板等资源，主说明应给出步骤、边界和异常情况。([Agent Skills][3]) 需求工程层面，ISO/IEC/IEEE 29148:2018 明确覆盖需求工程过程、信息项和指南，这里应把用户需求、验收标准、约束、可追踪性、验证方法作为 Plan 的强制结构，而不是可选写法。([ISO][4])

你上传的失败样例非常关键：现有 Plan/Task 虽然写了路线、覆盖率、验证，但粒度仍停留在“方案概述”；你期望的版本则包含 PDF 预检、MinerU/PyMuPDF/pikepdf 分工、Layout DOM、结构化翻译 schema、Fit Solver、redaction、链接恢复、QA、批处理、工程架构和路线图等端到端设计。这正好证明新版 Skill 必须强制要求：Plan 不能只列任务，要达到“调研证据 + 架构论证 + 规格定义 + 验证矩阵 + 可执行任务拆分”的密度。

---

# 1. 0.3.0-hardening 的核心结论

这版不应该叫“添加更多提示词”，而应该叫：

> **AgentSkill v0.3.0：Plan-Locked, Evidence-Driven, Long-Run Autonomous Workflow**

核心变化如下。

第一，**Plan Mode 是硬锁，不是建议**。L2/L3 大任务进入 Plan Mode 后，只允许阅读、调研、讨论、写 Plan.md、Task.md、AcceptanceContract.md、State.md、相关需求文档。没有用户独立发出 `开始执行`，绝对不能写代码、改文件、运行破坏性命令、生成最终交付物。

第二，**每一轮都必须重新校验 State / Plan / Task**。上下文压缩后，智能体必须从 State.md 的 Resumption Block 恢复，不允许凭记忆继续。恢复后第一动作不是执行，而是检查当前 Mode、Execution Authorization、Next Action、未完成 Task Group 和最近证据。

第三，**Plan.md 必须达到高密度规格文档标准**。大型工程/科研任务的 Plan 不是“几条步骤”，而是需求规格、技术路线、架构决策、调研证据、验证策略、风险约束、数据策略、里程碑和任务映射的统一文档。

第四，**Task.md 是 Plan.md 的可执行分解**。Task 最小单元要可执行、可验证、可追踪，但不要求每个小任务都做完整验证。推荐节奏是：小任务做轻量 micro-check；一个 Task Group 完成后做 checkpoint validation；几个 Task Group 完成后做 milestone validation；最终做 full validation + review。

第五，**真实数据优先验证是硬门禁**。代码、科研、文档、可视化、PDF、模型训练、算法验证，都必须优先使用用户提供的真实数据、仓库内真实样例、真实日志、公开基准或真实场景数据。合成数据只能作为最后一档，并且必须记录原因、风险和用户确认。

第六，**禁止执行阶段擅自兜底、降级、绕过需求**。兜底逻辑只能在 Plan 阶段进入 Fallback Register，写明触发条件、行为、代价、对验收标准的影响、验证方式，并由用户确认。执行阶段临时加兜底属于违规，必须停止并回到 Plan Mode。

第七，**执行授权后要连续完成 Plan/Task**。收到 `开始执行` 后，智能体应按 Task.md 自上而下执行到完成，除非出现硬阻塞、验证失败需要改计划、需求冲突、用户打断、权限/安全问题、真实数据缺失或外部服务不可用。

第八，**软件工程思想要贯穿全局**。需求、规格、架构、设计、实现、验证、运维、可维护性、文档、复现、风险管理都要进入 workflow。开发范式不单独依赖某一种，而是 SDD、验收驱动、行为场景、特征化测试、探索性 spike、契约/属性检查、回归验证、可观测性优先等组合使用。

---

# 2. 推荐目录改造

在现有 `AgentSkill/` 下增加这些文件。主 `SKILL.md` 保持入口性质，细则放到 `protocols/` 与 `library/`，避免主文件过长。

```text
AgentSkill/
  SKILL.md
  State.md

  protocols/
    00-hard-gates.md
    01-plan-mode-and-deep-plan.md
    02-deep-reading-and-research.md
    03-execution-preflight.md
    04-validation-real-data-first.md
    05-resumption-and-anti-drift.md
    06-delivery-and-review.md
    07-fallback-and-boundaries.md

  stages/
    router/SKILL.md
    plan/SKILL.md
    research/SKILL.md
    execute/SKILL.md
    validate/SKILL.md
    review/SKILL.md
    write/SKILL.md

  templates/
    Plan.deep.template.md
    Task.deep.template.md
    AcceptanceContract.template.md
    ValidationMatrix.template.md
    PlanQualityGate.template.md
    ExecutionPreflight.template.md
    ResumptionBlock.template.md
    DeliveryReport.template.md
    ChangeControl.template.md
    FallbackRegister.template.md

  library/
    plan-quality-standard.md
    task-decomposition-standard.md
    validation-real-data-first.md
    long-run-agent-operations.md
    software-engineering-operating-model.md
    research-and-evidence-standard.md
    documentation-quality-standard.md

  examples/
    README.md
    software-large-task.example.md
    research-large-task.example.md
    writing-large-task.example.md
    simple-task.example.md

  v0.3.0/
    Plan.md
    Task.md
    AcceptanceContract.md
    ChangeLog.md
```

---

# 3. 主入口 `AgentSkill/SKILL.md` 的补丁

把下面内容放到主 `SKILL.md` 的全局规则之后、阶段路由之前。主文件只放强约束和跳转，细节引用 `protocols/`。

```markdown
## v0.3.0 Hardening Layer：硬门禁、深度规划、长程续跑

本 Skill 不是“建议清单”，而是一个状态机。L2/L3 任务必须按 State → Plan → Task → Execute → Validate → Review → Deliver 的顺序推进。任何阶段缺少门禁条件时，不得凭经验继续。

### 0. 每轮启动顺序【L2/L3 强制】

每一轮回复、每一次工具调用、每一次继续执行前，必须按顺序读取或恢复：

1. `State.md`
2. 当前版本 `Plan.md`
3. 当前版本 `Task.md`
4. 对应 stage 的 `SKILL.md`
5. 必要的 `protocols/*.md`
6. 必要的 `templates/*.md` / `library/*.md`

读取后先判断：

- Current Mode：Plan / Research / Execute / Validate / Review / Deliver
- Execution Authorization：not_received / received / revoked / scope_changed
- Current Task Group
- Next Action
- Last Evidence
- Blocking Issues
- User Intent Lock

上下文压缩、长时间运行、工具中断、模型重启后，不允许直接继续执行；必须先恢复 State，并通过 `protocols/05-resumption-and-anti-drift.md` 的 Resumption Gate。

### 1. Plan Mode 硬锁【L2/L3 强制】

当任务属于 L2/L3，且 Execution Authorization 不是 `received` 时：

- 允许：阅读、调研、搜索、分析、讨论、写入/更新 Plan.md、Task.md、AcceptanceContract.md、State.md、Docs/需求文档。
- 禁止：写业务代码、修改实现文件、运行破坏性命令、生成最终交付物、替用户擅自选择未确认的降级方案。
- 禁止把“继续”“好的”“确认”“可以”“按这个来”解释为执行授权。
- 唯一执行授权口令是用户独立消息中的：`开始执行`。
- 授权只覆盖 Plan.md 明确写出的范围。scope 变化必须回到 Plan Mode。

### 2. Deep Plan Quality Gate【L3 强制，L2 推荐】

Plan.md 不满足以下条件，不得进入执行：

- 已深读用户材料、代码、文档、数据、约束。
- 已完成高质量外部调研，优先官方文档、论文、标准、权威资料、源码或一手资料。
- 已明确用户真实目标、非目标、边界、风险、成功标准。
- 已提出至少两个可行技术路线或方法路线，并给出取舍理由。
- 已给出推荐架构、技术链路、数据流、模块边界、接口、状态、错误处理、性能/质量目标。
- 已写出 Acceptance Contract。
- 已写出 Validation Matrix，且真实数据优先。
- 已把 Plan 拆成 Task Group 与最小可执行任务。
- 已写明禁止项、不可擅自兜底项、需要用户确认的高风险项。
- 已写入 State.md 的 Next Action 与 Resumption Block。

详细标准见：

- `protocols/01-plan-mode-and-deep-plan.md`
- `protocols/02-deep-reading-and-research.md`
- `templates/Plan.deep.template.md`
- `templates/PlanQualityGate.template.md`

### 3. Task 执行与验证节奏【L2/L3 强制】

Task.md 的小任务是最小执行单元，但验证采用分层节奏：

- Micro-check：小任务完成后的廉价检查，适用于语法、类型、文件存在、单点输出、关键不变量。
- Checkpoint validation：一个 Task Group 完成后必须执行。
- Milestone validation：多个相关 Task Group 完成后必须执行。
- Final validation：全部任务完成后必须执行。
- Final review：验证完成后必须评分和复盘。

高风险任务必须提前验证，不得等到整个大组结束：

- 数据删除、迁移、覆盖、不可逆操作
- 安全、权限、支付、隐私、合规
- 底层架构、公共接口、核心算法
- 性能敏感路径
- 训练/推理长任务
- PDF/视觉/排版等人工感知质量任务
- 任何一次失败会造成大量返工的任务

详细标准见：

- `protocols/03-execution-preflight.md`
- `protocols/04-validation-real-data-first.md`
- `library/task-decomposition-standard.md`

### 4. 真实数据优先验证【强制】

验证顺序为：

1. 用户提供的真实数据
2. 仓库/项目中已有真实样例、真实日志、真实配置
3. 公开真实数据集、公开 benchmark、官方示例
4. 脱敏真实数据
5. 合成数据

只有前四类均不可得，并且 State.md 记录原因后，才允许使用合成数据。使用合成数据时，报告中必须标记 `synthetic_only`，不得把它包装成真实场景验证通过。

### 5. 禁止擅自兜底与降级【强制】

默认策略是 fail-fast，而不是暗中兜底。

执行阶段禁止新增：

- 静默 fallback
- 静默 mock
- 静默跳过
- 静默降级
- 异常吞掉后继续
- 不符合 Plan 的替代方案
- “先随便做一个”的临时代码
- 为了测试通过而绕开需求

兜底只能在 Plan 阶段写入 `Fallback Register`，并经用户确认后执行。Fallback Register 必须说明触发条件、具体行为、代价、风险、用户可见性、日志、验证方式、对验收标准的影响。

详细标准见：`protocols/07-fallback-and-boundaries.md`

### 6. 长程续跑与抗遗忘【强制】

每个 L2/L3 周期必须维护 `State.md`：

- Current Mode
- Execution Authorization
- User Intent Lock
- Current Plan Version
- Current Task Group
- Completed Task Groups
- Last Validation Result
- Evidence Index
- Decisions
- Open Questions
- Blocking Issues
- Next Action
- Resumption Block

上下文压缩后，智能体必须从 Resumption Block 继续，不得停止工作，不得遗忘 Skill，不得跳过 Plan/Task。

### 7. 文档与交付【强制】

工程任务不仅交付代码，还必须同步交付文档。科研任务不仅交付结论，还必须交付证据、方法、可复现协议。写作任务不仅交付正文，还必须交付结构、依据、风格说明和质量评估。

最终交付必须使用 `templates/DeliveryReport.template.md`，包括：

- 做了什么
- 改了哪些文件
- 对应哪些 Plan/Task/AC
- 用了哪些真实数据或证据
- 跑了哪些验证
- 结果评分
- 剩余风险
- 明确的限制
```

---

# 4. 新增 `protocols/00-hard-gates.md`

````markdown
# 00-hard-gates：AgentSkill v0.3.0 硬门禁协议

## 1. 目的

本文件把所有容易被模型忽略的规则变成硬门禁。门禁不通过时，智能体不得继续进入下一阶段。

## 2. Gate Result Schema

每个门禁检查必须能落成以下结构：

```yaml
gate_id:
  name:
  status: pass | fail | blocked | not_applicable
  evidence:
  missing:
  required_action:
````

`fail` 与 `blocked` 不能继续执行。必须修复、补充 Plan/Task/State，或回到用户需求对齐。

## 3. G0：Boot Gate

每一轮 L2/L3 工作开始前必须检查：

* 已读取或恢复 `State.md`
* 已读取当前 `Plan.md`
* 已读取当前 `Task.md`
* 已识别当前 Mode
* 已识别 Execution Authorization
* 已识别 Next Action
* 已识别当前 Task Group
* 已识别用户最新消息是否改变 scope

不通过时：

* 先恢复 State
* 不执行代码
* 不修改业务文件
* 不跳过 Plan/Task

## 4. G1：Plan Mode Gate

进入执行前必须满足：

* 当前任务 Level 是 L0/L1，或者
* L2/L3 任务已有完整 Plan.md + Task.md + AcceptanceContract.md
* 用户已独立发送 `开始执行`
* State.md 中 Execution Authorization = `received`
* 授权 scope 与 Plan.md 一致

不满足时，只能做 Plan Mode 工作。

禁止把以下表达当成执行授权：

* “继续”
* “可以”
* “好的”
* “按这个来”
* “确认”
* “没问题”
* “就这样”
* “开始吧”之外的含糊表述

唯一授权口令：`开始执行`

## 5. G2：Deep Reading Gate

L2/L3 规划前必须完成资料读取：

* 用户提供的需求文本
* 用户上传文档
* 用户上传代码
* 仓库 README / docs / config / tests / examples
* 相关历史 Plan / Task / State
* 相关错误日志或输出
* 真实数据样例或数据说明

大型代码任务必须先做代码地图：

* 入口文件
* 核心模块
* 数据流
* 状态流
* 配置流
* 外部依赖
* 测试入口
* 已知风险
* 与需求相关的调用链

资料不足时，Plan.md 必须记录缺口和补救策略。

## 6. G3：Research Gate

L2/L3 的科研、工程、架构、选型、文档任务必须完成外部调研。

研究资料优先级：

1. 官方文档、标准、规范
2. 论文、技术报告、权威书籍
3. 项目源码、issue、release note
4. 公共 benchmark、官方样例、真实案例
5. 高质量博客、工程复盘
6. 低质量资料仅可作为线索，不可作为核心依据

Research Log 不能只列链接，必须写：

* 来源
* 可信度
* 与本任务的关系
* 提取到的事实
* 对方案的影响
* 进入 Plan 的位置

## 7. G4：Plan Quality Gate

Plan.md 必须达到以下最低标准：

* 有问题重述
* 有用户意图锁定
* 有成功标准
* 有非目标
* 有输入/输出
* 有约束边界
* 有深读记录
* 有调研记录
* 有候选方案
* 有推荐方案
* 有架构图或流程图
* 有模块边界
* 有接口/数据/状态/错误处理规格
* 有验证矩阵
* 有真实数据策略
* 有风险登记
* 有 fallback 登记或明确禁止 fallback
* 有 Task 映射
* 有执行授权状态
* 有 Resumption Block

缺少任一关键项时，不得进入 Execute。

## 8. G5：Task Quality Gate

Task.md 必须满足：

* 每个任务有 checkbox
* 每个任务可执行
* 每个任务可验证
* 每个任务能追踪到 Plan 或 AC
* 每个 Task Group 有目标
* 每个 Task Group 有依赖
* 每个 Task Group 有 checkpoint validation
* 高风险任务有提前验证
* 不把“实现核心功能”这类大块当作单个任务
* 不把“测试一下”这类模糊项当作验证任务

## 9. G6：Execution Preflight Gate

执行前必须检查：

* Execution Authorization = received
* Scope 未变化
* 当前 Task Group 明确
* 相关文件已读取
* 相关依赖已检查
* 真实数据路径或获取方式已明确
* 验证命令已明确
* 禁止项已明确
* Fallback Register 已确认或明确为空
* 本次操作不会越界修改文件

不通过时，回到 Plan 或 State 更新。

## 10. G7：Real Data Validation Gate

验证前必须优先寻找真实数据：

* 用户提供数据
* 仓库测试数据
* 样例文件
* 日志
* 公开数据集
* 官方 benchmark
* 脱敏真实数据

合成数据只能作为最后一档，并且必须在报告中标注。

## 11. G8：Evidence Gate

任何“完成”“通过”“有效”“性能满足”“质量达标”都必须有证据：

* 命令
* 输出
* 日志
* 报告
* 截图
* 差异
* benchmark
* 人工检查记录
* 真实数据说明

没有证据只能写“未验证”或“待验证”，不能写“已完成”。

## 12. G9：Drift Recovery Gate

出现以下情况必须停止当前动作并恢复：

* 未授权执行
* 忽略 Plan.md
* 忽略 Task.md
* 忽略用户约束
* 擅自兜底
* 擅自降级
* 用合成数据冒充真实验证
* 上下文压缩后忘记状态
* 连续输出与当前 Task Group 无关
* 执行结果无法映射到 AC

恢复步骤：

1. 停止执行
2. 在 State.md 记录 drift 事件
3. 对比用户最新需求、Plan.md、Task.md
4. 修正 Plan/Task 或回滚错误执行
5. 重新通过 Gate G0-G8
6. 再继续

## 13. Gate Summary

```text
G0 Boot
  ↓
G1 Plan Mode
  ↓
G2 Deep Reading
  ↓
G3 Research
  ↓
G4 Plan Quality
  ↓
G5 Task Quality
  ↓
G6 Execution Preflight
  ↓
G7 Real Data Validation
  ↓
G8 Evidence
  ↓
G9 Drift Recovery
```

````

---

# 5. 新增 `protocols/01-plan-mode-and-deep-plan.md`

```markdown
# 01-plan-mode-and-deep-plan：深度规划协议

## 1. Plan Mode 的定义

Plan Mode 是 L2/L3 任务的需求理解、研究、架构、规格、验证设计阶段。

Plan Mode 可以做：

- 阅读用户资料
- 阅读代码
- 阅读文档
- 搜索资料
- 调研论文/标准/官方文档
- 分析架构
- 讨论需求
- 提出建议
- 写 Plan.md
- 写 Task.md
- 写 AcceptanceContract.md
- 写 Docs/requirements
- 更新 State.md

Plan Mode 禁止做：

- 写业务代码
- 修改实现文件
- 生成最终交付物
- 跑破坏性操作
- 替用户执行未授权方案
- 把未确认的 fallback 写进代码
- 直接进入 Execute

## 2. 需求理解原则

智能体必须主动理解用户目标，而不是机械询问。

允许询问，但问题必须满足：

- 与最终方案有关
- 会改变架构、范围、验证或风险
- 数量克制
- 附带推荐判断
- 不把选择负担全部丢给用户

禁止连续抛出开放式选择题。用户信息不足时，先给出基于证据的推荐方案，再说明取舍。

## 3. User Intent Lock

Plan.md 必须包含 `User Intent Lock`：

```yaml
user_intent_lock:
  primary_goal:
  secondary_goals:
  non_goals:
  must_preserve:
  must_avoid:
  preferred_style:
  accepted_tradeoffs:
  rejected_tradeoffs:
  latest_user_feedback:
````

执行中任何设计选择都必须回看 User Intent Lock。

## 4. Deep Plan 的最低内容

L3 Plan.md 必须包含以下章节：

1. Metadata
2. Execution Authorization
3. User Intent Lock
4. Problem Frame
5. Current State / Gap Analysis
6. Inputs and Materials Read
7. Research Log
8. Requirements
9. Non-goals
10. Constraints and Boundaries
11. Candidate Solutions
12. Architecture Decision
13. Technical Chain
14. Data Model / Interfaces / State / Error Handling
15. Development Strategy
16. Validation Matrix
17. Real Data Strategy
18. Risk Register
19. Fallback Register
20. Documentation Plan
21. Milestones
22. Task Mapping
23. Ready-to-Execute Gate
24. Resumption Block

## 5. Deep Reading 标准

Plan.md 的 `Inputs and Materials Read` 不能写成“已阅读资料”。

必须写：

```markdown
| Material | Path/Source | What was read | Key facts | Impact on plan |
|---|---|---|---|---|
```

代码任务还必须写：

```markdown
| Module | Responsibility | Entry points | Dependencies | Relevant files | Risks |
|---|---|---|---|---|---|
```

科研任务还必须写：

```markdown
| Topic | Existing methods | Limitations | Opportunity | Verification route |
|---|---|---|---|---|
```

写作/文档任务还必须写：

```markdown
| Source | Style/Facts extracted | Reliability | Where used |
|---|---|---|---|
```

## 6. Research Log 标准

Research Log 必须写成可追踪证据：

```markdown
| Source | Type | Reliability | Key facts | Design impact | Plan section |
|---|---|---:|---|---|---|
```

大型任务最低要求：

* L2：至少覆盖 3 个高质量来源，或说明任务无需外部研究
* L3：至少覆盖 8 个高质量来源，或覆盖该问题的主要权威来源
* 关键技术选型必须优先引用官方文档、论文、标准、源码、一手资料

## 7. 候选方案与架构决策

Plan.md 不能只有一个方案。必须至少比较：

* 保守方案
* 推荐方案
* 激进/长期方案

每个方案必须写：

```markdown
### Option X

- Summary:
- When it works:
- Advantages:
- Disadvantages:
- Risks:
- Cost:
- Validation difficulty:
- Why accepted/rejected:
```

最终写入 ADR 风格决策：

```markdown
## Architecture Decision

Decision:
Rationale:
Alternatives considered:
Consequences:
Rollback strategy:
```

## 8. 技术链路

工程/科研/文档任务都要给出链路图。

示例：

```text
User Goal
  ↓
Requirement Model
  ↓
Research / Evidence
  ↓
Architecture / Method
  ↓
Spec / Interface / Protocol
  ↓
Implementation / Writing / Experiment
  ↓
Real-data Validation
  ↓
Review
  ↓
Delivery
```

软件任务还必须给出：

```text
Input
  ↓
Parser / Adapter
  ↓
Core Domain Model
  ↓
Processing Pipeline
  ↓
Output Renderer / API
  ↓
Validation / Observability
```

科研任务还必须给出：

```text
Hypothesis
  ↓
Related Work
  ↓
Method
  ↓
Experiment Design
  ↓
Metrics
  ↓
Ablation / Baseline
  ↓
Reproducibility Package
```

## 9. 规格优先

大任务必须先写 Spec，再执行。Spec 包含：

* 对象模型
* 输入输出
* 接口
* 不变量
* 错误情况
* 性能目标
* 资源约束
* 日志/监控
* 验证方式

开发范式采用组合方式：

* Spec-first
* Acceptance-first
* Behavior scenarios
* Characterization and regression
* Spike before irreversible architecture
* Contract and property checks
* Observability-first for debug and operations

不得把单一开发范式写成唯一方法。

## 10. Ready-to-Execute Gate

Plan.md 末尾必须包含：

```markdown
## Ready-to-Execute Gate

- [ ] User Intent Lock complete
- [ ] Deep Reading complete
- [ ] Research Log complete
- [ ] Architecture Decision complete
- [ ] Acceptance Contract complete
- [ ] Validation Matrix complete
- [ ] Real Data Strategy complete
- [ ] Fallback Register reviewed
- [ ] Task.md complete
- [ ] State.md updated
- [ ] Awaiting standalone authorization: `开始执行`
```

收到授权后：

```markdown
- [x] Execution Authorization received
- Authorization message:
- Authorization scope:
- Authorization time:
```

````

---

# 6. 新增 `protocols/04-validation-real-data-first.md`

```markdown
# 04-validation-real-data-first：真实数据优先验证协议

## 1. 目标

验证不只是“代码能跑”。验证必须证明交付物符合用户目标、Plan、Task、Acceptance Contract、性能、可维护性、文档和真实使用场景。

## 2. 数据优先级

验证数据优先级如下：

1. 用户提供的真实数据
2. 项目仓库内真实样例
3. 真实日志、真实配置、真实模型 checkpoint、真实输入输出
4. 官方 benchmark / 官方示例
5. 公开数据集
6. 脱敏真实数据
7. 专门构造的边界数据
8. 合成数据

合成数据只能补充边界，不得替代真实验证，除非真实数据不可得且 State.md 已记录原因。

## 3. 真实数据缺失处理

真实数据缺失时，必须执行：

1. 搜索项目目录中的 fixtures、examples、tests、data、logs、samples
2. 搜索用户提供材料
3. 查询公开 benchmark 或官方示例
4. 在 Plan.md / State.md 记录缺失项
5. 明确 synthetic 的局限
6. 在最终报告标记 `validation_data_level`

## 4. 验证维度

软件任务至少验证：

- 功能正确性
- 需求符合度
- 边界条件
- 异常路径
- 性能
- 资源占用
- 并发或长任务稳定性
- 日志和可观测性
- 可读性
- 可维护性
- 架构一致性
- 文档完整性
- 安全与隐私风险
- 回归风险

科研任务至少验证：

- 问题定义是否清楚
- 相关工作是否覆盖关键路线
- 方法是否可复现
- 实验设计是否能回答问题
- baseline 是否合理
- 指标是否匹配目标
- 数据是否真实或合理
- 消融是否必要
- 失败模式是否讨论
- 结论是否被证据支持

文档任务至少验证：

- 是否覆盖用户需求
- 结构是否清楚
- 事实是否有来源
- 风格是否符合要求
- 是否去除模板味和机械味
- 图示是否足够
- 术语是否一致
- 读者能否按文档执行
- 是否有示例、边界、常见错误

PDF/视觉/排版任务至少验证：

- 真实样例
- 渲染截图
- 视觉对比
- 坐标/布局检查
- 文本残留检查
- 重叠检查
- 链接/跳转检查
- 字体/缺字检查
- 多阅读器或多渲染器检查
- 人工抽检记录

## 5. 分层验证节奏

### 5.1 Micro-check

小任务完成后做廉价检查：

- 文件存在
- 函数可导入
- schema 可解析
- 单个样例可运行
- 关键断言通过
- 文档链接未断

Micro-check 不替代 checkpoint validation。

### 5.2 Checkpoint validation

一个 Task Group 完成后必须做：

- 运行该组对应测试
- 验证 AC 映射
- 写入 Evidence Index
- 更新 State.md

### 5.3 Milestone validation

多个 Task Group 完成后必须做：

- 端到端局部流程
- 真实数据验证
- 回归检查
- 性能或质量抽检
- 文档同步检查

### 5.4 Final validation

最终验证必须覆盖：

- 所有 Acceptance Criteria
- 所有关键真实数据场景
- 所有核心文档
- 所有已知风险
- 所有用户明确要求
- Delivery Report

## 6. 验证结果枚举

每项验证只能使用：

- `pass`
- `fail`
- `blocked`
- `not_run`
- `not_applicable`

禁止使用模糊结果：

- “基本可以”
- “应该没问题”
- “看起来通过”
- “简单测试通过，所以完成”

## 7. 失败处理

验证失败时：

1. 标记失败项
2. 写入 State.md
3. 定位对应 Plan / Task / AC
4. 回到相关 Task Group
5. 修复
6. 重跑失败验证
7. 重跑相关回归验证

不得把失败项隐藏在最终报告中。
````

---

# 7. 新增 `protocols/05-resumption-and-anti-drift.md`

````markdown
# 05-resumption-and-anti-drift：长程续跑与抗漂移协议

## 1. 目的

长任务中，智能体容易在上下文压缩、阶段切换、多轮反馈、工具失败后忘记 Skill。本协议保证任务能从 State.md 恢复。

## 2. State.md 是唯一运行状态源

L2/L3 任务必须维护 State.md。任何“我记得”都不能替代 State.md。

## 3. 每轮必须写入或确认的状态

```yaml
current_mode:
execution_authorization:
plan_version:
task_version:
current_task_group:
current_task_item:
completed_groups:
last_validation:
last_evidence:
blocking_issues:
scope_changes:
user_intent_lock_hash:
next_action:
````

## 4. Resumption Block

State.md 末尾必须维护：

```markdown
## RESUMPTION_BLOCK_v0.3

- Skill:
- Version:
- Current Mode:
- Execution Authorization:
- Authorization Scope:
- Current Plan:
- Current Task:
- Current Task Group:
- Last Completed Task:
- Last Validation:
- Evidence Index:
- Blocking Issues:
- User Intent Lock:
- Forbidden Actions:
- Next Action:
- Continue Rule:
```

`Continue Rule` 必须明确写：

* 继续执行前先读 Plan.md / Task.md / State.md
* 继续执行当前 Task Group
* 不得重新规划，除非 scope changed / validation failed / user feedback changed requirements
* 不得要求用户重复已经给过的信息

## 5. 上下文压缩后的恢复步骤

上下文压缩后：

1. 读取 State.md
2. 读取当前 Plan.md
3. 读取当前 Task.md
4. 检查 Execution Authorization
5. 检查最新用户消息是否改变 scope
6. 检查 Last Validation
7. 继续 Next Action

不允许：

* 停止工作
* 忘记 Skill
* 跳过 Task.md
* 重新从零开始
* 擅自执行未授权内容
* 把已完成任务重复做一遍

## 6. Drift Signals

以下信号代表漂移：

* 输出内容与当前 Task Group 无关
* 未读取 Plan/Task 就执行
* 忽略用户禁止项
* 忽略真实数据要求
* 将模板当成最终输出上限
* 擅自简化 Plan
* 擅自降级需求
* 执行阶段临时新增 fallback
* 验证只跑 toy example
* final report 不列证据

## 7. Drift Recovery

漂移后必须：

```markdown
## Drift Recovery Entry

- Drift type:
- Detected at:
- Violated rule:
- Affected files/tasks:
- Recovery action:
- State updated:
- Gate rechecked:
```

恢复完成后再进入原阶段。

````

---

# 8. 新增 `protocols/07-fallback-and-boundaries.md`

```markdown
# 07-fallback-and-boundaries：边界、兜底、降级协议

## 1. 默认策略

默认禁止兜底。默认禁止降级。默认禁止“为了跑通而绕开需求”。

失败时应暴露失败、定位失败、修复失败，而不是吞掉失败。

## 2. 禁止行为

执行阶段禁止：

- broad try/except 后返回空结果
- 出错后静默跳过
- 用 mock 替代真实依赖
- 用 synthetic 替代真实数据却不标注
- 用户要求真实数据，实际使用伪造数据
- 用户要求保持功能，实际删除功能
- 用户要求高质量排版，实际白底遮罩
- 用户要求完整实现，实际只做 demo
- 用户要求不降级，实际简化需求
- 为了测试通过改测试而非修实现
- 为了避免复杂性删除用户目标

## 3. 允许的 fallback 条件

Fallback 只有在 Plan Mode 中写入并确认后才允许。

Fallback Register 格式：

```markdown
| ID | Trigger | Behavior | User-visible effect | Cost | Risk | AC impact | Observability | Validation | Approved |
|---|---|---|---|---|---|---|---|---|---|
````

## 4. 执行阶段遇到不可实现项

执行阶段发现无法实现：

1. 停止相关实现
2. 记录技术原因
3. 提供证据
4. 标记 blocked
5. 回到 Plan Mode
6. 更新 Plan/Task
7. 等待用户重新确认执行范围

不得擅自换成低质量方案。

## 5. 简单任务例外

L0/L1 简单任务可以直接完成，但仍遵守：

* 不伪造
* 不静默吞错
* 不擅自越界
* 不违背用户明确约束

````

---

# 9. `stages/plan/SKILL.md` 的加固补丁

在 Plan stage 的“输出要求”之后追加：

```markdown
## v0.3 Deep Plan Enforcement

### 1. Plan 不是摘要

L2/L3 的 Plan.md 不得写成简短任务列表。它必须能让后续智能体在上下文压缩后独立恢复并继续执行。

大型任务的 Plan.md 必须足够详细，包含：

- 用户意图锁
- 背景与问题重述
- 用户材料深读记录
- 代码/文档/数据阅读记录
- 外部研究记录
- 需求与非目标
- 候选技术路线
- 架构决策
- 模块边界
- 接口与数据结构
- 错误处理
- 性能/质量要求
- 文档要求
- 真实数据验证计划
- 风险与 fallback 登记
- 任务映射
- 继续执行指令

### 2. 禁止浅层 Plan

以下 Plan 不合格：

- 只有“先分析、再实现、再测试”
- 只写一个技术路线，没有比较
- 不列资料来源
- 不写用户材料中的具体事实
- 不写真实数据验证
- 不写验收标准
- 不写失败处理
- 不写禁止项
- 不写恢复信息
- Task 无法追踪到 AC
- 执行者看完仍然不知道改哪些文件、为什么改、怎么验证

### 3. Deep Plan Quality Gate

Plan 完成前必须填写 `templates/PlanQualityGate.template.md`。任一核心项为 fail 时，不得请求执行授权。

### 4. Plan Mode 交互

Plan Mode 中，智能体要主动提出利于用户目标的建议，而不是无限让用户选择。用户反馈进入 Plan.md 后，必须更新：

- User Intent Lock
- Requirements
- Constraints
- Architecture Decision
- Validation Matrix
- Task Mapping
- State.md Resumption Block

### 5. 执行授权提示

Plan/Task 完成后，只能提示：

“Plan.md、Task.md、AcceptanceContract.md 已准备好。当前状态仍是 Plan Mode，尚未执行。执行需要用户独立发送：`开始执行`。”

不得在同一条消息中顺手开始执行。
````

---

# 10. `stages/execute/SKILL.md` 的加固补丁

在 Execute loop 前追加：

````markdown
## v0.3 Execute Preflight

执行不是自由发挥。每个 Task Group 开始前必须完成：

```yaml
execution_preflight:
  state_read: true
  plan_read: true
  task_read: true
  auth_received: true
  scope_matches: true
  current_group:
  linked_acceptance_criteria:
  linked_plan_sections:
  files_to_read_first:
  files_allowed_to_modify:
  forbidden_actions:
  real_data_source:
  validation_commands:
  checkpoint_required:
````

任一核心字段缺失，不得执行。

## v0.3 Execution Discipline

执行阶段必须：

1. 选择 Task.md 中第一个未完成 Task Group。
2. 阅读该组相关 Plan 章节。
3. 阅读相关代码/文档/数据。
4. 执行该组小任务。
5. 小任务完成后做 micro-check。
6. Task Group 完成后做 checkpoint validation。
7. 更新 Task.md checkbox。
8. 更新 State.md。
9. 继续下一个 Task Group。

收到 `开始执行` 后，不重复询问已经在 Plan 中确认的选择。除硬阻塞外，持续执行直到 Task.md 全部完成。

## v0.3 禁止执行偏移

执行阶段禁止：

* 不看 Plan 直接写代码
* 不看 Task 自行安排任务
* 改动 Plan 外文件
* 擅自引入 fallback
* 擅自降级用户需求
* 用 mock 替代真实依赖
* 只做 toy demo
* 忽略文档
* 忽略真实验证
* 忽略已失败测试

## v0.3 Debug / Ops / Training Monitor

当任务是替用户运行 debug、模型训练监控、库调试、长任务维护时，必须建立 runbook：

* 操作目标
* 环境假设
* 命令
* 日志路径
* 指标
* 阈值
* 异常处理
* 停止条件
* 恢复方式
* 报告格式

监控类任务必须记录：

* start time
* command
* process status
* metrics
* last checkpoint
* observed anomalies
* next check

````

---

# 11. `stages/validate/SKILL.md` 的加固补丁

```markdown
## v0.3 Validation Enforcement

验证必须覆盖 Acceptance Contract。不得只验证“能运行”。

### 1. Validation Matrix

每个 AC 必须映射到：

- validation method
- data source
- command/tool
- expected result
- actual result
- evidence path
- status

格式：

```markdown
| AC | Method | Data level | Command/Tool | Expected | Actual | Evidence | Status |
|---|---|---|---|---|---|---|---|
````

### 2. Data Level

每项验证必须标记：

* real_user_data
* real_project_sample
* public_benchmark
* official_example
* sanitized_real
* synthetic_edge_case
* synthetic_only

`synthetic_only` 不能作为 L3 最终通过的唯一证据，除非 Plan.md 明确说明真实数据不可得且用户已确认。

### 3. Validation Scope

软件任务验证：

* correctness
* integration
* regression
* performance
* readability
* maintainability
* architecture compliance
* docs
* security/privacy when relevant

科研任务验证：

* hypothesis
* literature coverage
* method validity
* experiment reproducibility
* baseline
* metrics
* ablation
* limitations

文档任务验证：

* requirement coverage
* factuality
* style
* structure
* diagrams
* completeness
* reader usability

视觉/PDF/排版任务验证：

* real files
* rendered screenshots
* overlap
* clipping
* links
* fonts
* layout
* visual review evidence

### 4. Failure Handling

任何 fail 都必须回到对应 Task Group。不得把 fail 写成 pass，不得用“基本完成”覆盖验证失败。

````

---

# 12. `stages/review/SKILL.md` 的加固补丁

```markdown
## v0.3 Review Rubric

Final Review 必须评分。评分不能替代证据，只能总结证据。

### 1. Review Dimensions

| Dimension | Score 0-10 | Evidence |
|---|---:|---|
| Requirement fit | | |
| Plan compliance | | |
| Task completion | | |
| Correctness | | |
| Real-data validation | | |
| Architecture quality | | |
| Maintainability | | |
| Performance/resource fit | | |
| Documentation quality | | |
| Risk handling | | |

### 2. Pass Rule

L3 最终通过必须满足：

- 所有 hard gate pass
- 所有 critical AC pass
- 无未解释的 validation fail
- 无擅自 fallback
- 无真实数据验证缺口，或缺口已记录并被用户确认
- 总评分 >= 8.0

### 3. Needs Rework

以下情况必须进入 rework：

- 任一 critical AC fail
- Plan/Task 未执行完整
- 真实数据验证缺失
- 用户明确要求未满足
- 文档缺失
- 证据不足
- 结果依赖未确认 fallback

### 4. Feedback Loop

用户对成果不满意或提出新想法时：

1. 不争辩
2. 记录反馈
3. 更新 State.md
4. 回到 Plan Mode
5. 更新 Plan.md / Task.md / AcceptanceContract.md
6. 等待新的 `开始执行`
````

---

# 13. `stages/write/SKILL.md` 的加固补丁

```markdown
## v0.3 Writing / Documentation Quality

文档类任务也要 Plan、Task、Validate、Review。

### 1. 写作前

必须确认：

- 读者是谁
- 文档目的
- 使用场景
- 详细程度
- 风格
- 术语
- 图示需求
- 事实来源
- 禁止内容
- 交付格式

### 2. 写作中

不得只堆文字。大型文档必须包含：

- 结构图
- 流程图
- 表格
- 示例
- 反例
- 常见错误
- 检查清单
- 术语表
- 参考来源

### 3. 写作验证

文档完成后必须评估：

- 是否覆盖用户需求
- 是否事实准确
- 是否能指导执行
- 是否符合风格
- 是否有机械模板感
- 是否图文并茂
- 是否过度简化
- 是否存在遗漏
```

---

# 14. 模板与示例的统一免责声明

你提到模板和 example 太简化，容易把智能体带偏。这个要全局处理：所有 `templates/*.md` 和 `examples/*.md` 顶部统一加入以下声明。

```markdown
> 重要说明：本模板/示例仅用于展示结构，不代表实际输出的最低详细程度。
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。
> 示例中的字段可以扩展，不得擅自删除用户需求相关字段。
```

对 examples 再加一条：

```markdown
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。
```

---

# 15. 新模板：`templates/Plan.deep.template.md`

````markdown
# Plan：<Project / Task Name>

Version:
Track:
WorkType:
Level:
Current Mode: Plan
Execution Authorization: not_received
Plan Owner:
Last Updated:

---

## 0. Template Notice

本模板仅供结构参考。实际 Plan 必须根据任务复杂度、用户材料、研究证据、架构设计和验证需求扩展。

---

## 1. User Intent Lock

```yaml
primary_goal:
secondary_goals:
must_preserve:
must_avoid:
non_goals:
style_preferences:
quality_bar:
latest_user_feedback:
scope_boundary:
````

---

## 2. Problem Frame

### 2.1 一句话目标

### 2.2 背景

### 2.3 用户真正想解决的问题

### 2.4 成功后的状态

### 2.5 当前风险

---

## 3. Current State / Gap Analysis

| Area | Current state | Gap | Impact | Required action |
| ---- | ------------- | --- | ------ | --------------- |

---

## 4. Inputs and Materials Read

| Material | Path/Source | What was read | Key facts | Impact on plan |
| -------- | ----------- | ------------- | --------- | -------------- |

### 4.1 Code / Repository Map

| Module/File | Responsibility | Entry points | Dependencies | Relevant facts | Risks |
| ----------- | -------------- | ------------ | ------------ | -------------- | ----- |

### 4.2 Data / Examples / Logs

| Data | Location | Real/Synthetic | Used for | Limitations |
| ---- | -------- | -------------- | -------- | ----------- |

---

## 5. Research Log

| Source | Type | Reliability | Key facts | Design impact | Used in section |
| ------ | ---- | ----------: | --------- | ------------- | --------------- |

### 5.1 Research Summary

### 5.2 Research Gaps

### 5.3 Facts That Changed the Plan

---

## 6. Requirements

### 6.1 Functional Requirements

| ID | Requirement | Priority | Source | Acceptance |
| -- | ----------- | -------: | ------ | ---------- |

### 6.2 Non-functional Requirements

| ID | Requirement | Target | Validation |
| -- | ----------- | ------ | ---------- |

### 6.3 Documentation Requirements

### 6.4 Operations / Monitoring Requirements

---

## 7. Non-goals

| ID | Non-goal | Reason |
| -- | -------- | ------ |

---

## 8. Constraints and Boundaries

### 8.1 Allowed

### 8.2 Forbidden

### 8.3 Files / Areas Allowed to Modify

### 8.4 Files / Areas Forbidden to Access or Modify

### 8.5 Fallback Policy

默认禁止执行阶段新增 fallback。允许的 fallback 只写在 Fallback Register。

---

## 9. Candidate Solutions

### Option A：Conservative

* Summary:
* Pros:
* Cons:
* Risks:
* Validation:
* Rejected/Accepted reason:

### Option B：Recommended

* Summary:
* Pros:
* Cons:
* Risks:
* Validation:
* Rejected/Accepted reason:

### Option C：Long-term / Advanced

* Summary:
* Pros:
* Cons:
* Risks:
* Validation:
* Rejected/Accepted reason:

---

## 10. Architecture Decision

Decision:

Rationale:

Alternatives considered:

Consequences:

Rollback strategy:

---

## 11. Technical Chain / Method Chain

```text
User Requirement
  ↓
Evidence / Research
  ↓
Architecture / Method
  ↓
Spec
  ↓
Implementation / Writing / Experiment
  ↓
Validation
  ↓
Review
  ↓
Delivery
```

---

## 12. Specification

### 12.1 Data Model

### 12.2 Interfaces

### 12.3 State

### 12.4 Error Handling

### 12.5 Logging / Monitoring

### 12.6 Performance / Resource Targets

### 12.7 Security / Privacy

---

## 13. Development / Work Strategy

本任务采用组合范式：

* Spec-first
* Acceptance-first
* Behavior scenarios
* Characterization / regression checks
* Spike for uncertain architecture
* Contract / property checks
* Observability-first for long-running/debug/ops tasks

### 13.1 Strategy by Area

| Area | Strategy | Reason | Evidence |
| ---- | -------- | ------ | -------- |

---

## 14. Acceptance Contract

| AC | Description | Priority | Validation Method | Evidence |
| -- | ----------- | -------: | ----------------- | -------- |

---

## 15. Validation Matrix

| AC | Test/Check | Data Level | Tool/Command | Expected | Evidence Path |
| -- | ---------- | ---------- | ------------ | -------- | ------------- |

---

## 16. Real Data Strategy

| Data need | Preferred source | Fallback source | Synthetic allowed | Notes |
| --------- | ---------------- | --------------- | ----------------- | ----- |

---

## 17. Risk Register

| Risk | Probability | Impact | Detection | Mitigation | Owner |
| ---- | ----------: | -----: | --------- | ---------- | ----- |

---

## 18. Fallback Register

| ID | Trigger | Behavior | Cost | User-visible effect | AC impact | Validation | Approved |
| -- | ------- | -------- | ---- | ------------------- | --------- | ---------- | -------- |

---

## 19. Documentation Plan

| Doc | Audience | Content | When updated | Validation |
| --- | -------- | ------- | ------------ | ---------- |

---

## 20. Milestones

| Milestone | Goal | Task Groups | Validation | Exit Criteria |
| --------- | ---- | ----------- | ---------- | ------------- |

---

## 21. Task Mapping

| Plan Section | Task Group | AC | Validation |
| ------------ | ---------- | -- | ---------- |

---

## 22. Ready-to-Execute Gate

* [ ] User Intent Lock complete
* [ ] Deep Reading complete
* [ ] Research Log complete
* [ ] Candidate solutions compared
* [ ] Architecture Decision complete
* [ ] Spec complete
* [ ] Acceptance Contract complete
* [ ] Validation Matrix complete
* [ ] Real Data Strategy complete
* [ ] Risk Register complete
* [ ] Fallback Register reviewed
* [ ] Task.md complete
* [ ] State.md updated
* [ ] Awaiting standalone authorization: `开始执行`

---

## 23. Resumption Block

```yaml
current_mode: Plan
execution_authorization: not_received
current_plan:
current_task:
next_action:
forbidden_until_authorized:
```

````

---

# 16. 新模板：`templates/Task.deep.template.md`

```markdown
# Task：<Project / Task Name>

Version:
Linked Plan:
Linked Acceptance Contract:
Current Mode:
Execution Authorization:

> 本模板仅供结构参考。实际 Task 必须根据 Plan.md 的复杂度展开，不得因模板简短而简化任务。

---

## Task Status Legend

- [ ] Not started
- [~] In progress
- [x] Done
- [!] Blocked
- [r] Rework required

---

## Execution Rules

- 按 Task Group 顺序执行。
- 每个小任务必须能追踪到 Plan 或 AC。
- 小任务完成后做 micro-check。
- Task Group 完成后做 checkpoint validation。
- 若验证失败，回到对应任务修复。
- 不得跳过未完成任务。
- 不得执行 Plan 外任务。
- 不得新增未经确认的 fallback。
- 不得使用合成数据冒充真实验证。

---

## 0. Preflight

- [ ] 0.1 Read State.md
- [ ] 0.2 Read Plan.md
- [ ] 0.3 Read AcceptanceContract.md
- [ ] 0.4 Confirm Execution Authorization = received
- [ ] 0.5 Confirm scope matches Plan.md
- [ ] 0.6 Confirm real validation data source
- [ ] 0.7 Confirm forbidden actions
- [ ] 0.8 Confirm Fallback Register
- [ ] 0.9 Write ExecutionPreflight result to State.md

Checkpoint:
- [ ] CP-0 Preflight pass

---

## 1. Task Group：<Name>

Goal:

Linked Plan Sections:

Linked AC:

Inputs:

Allowed Files:

Forbidden Files:

Validation Data:

### Tasks

- [ ] 1.1 <small executable task>
  - Evidence:
  - Micro-check:
- [ ] 1.2 <small executable task>
  - Evidence:
  - Micro-check:
- [ ] 1.3 <small executable task>
  - Evidence:
  - Micro-check:

### Checkpoint Validation

- [ ] 1.CP.1 Run validation:
- [ ] 1.CP.2 Record result:
- [ ] 1.CP.3 Update Evidence Index:
- [ ] 1.CP.4 Update State.md:

Exit Criteria:
- [ ] All linked AC pass or documented fail
- [ ] No unauthorized fallback
- [ ] Documentation updated when relevant

---

## 2. Task Group：<Name>

同上。

---

## Milestone Validation

- [ ] M1 Validate integrated flow
- [ ] M2 Validate real data
- [ ] M3 Validate regression
- [ ] M4 Validate documentation

---

## Final Validation

- [ ] FV.1 All AC mapped
- [ ] FV.2 Real data validation complete
- [ ] FV.3 Regression validation complete
- [ ] FV.4 Performance/resource validation complete when relevant
- [ ] FV.5 Docs validation complete
- [ ] FV.6 Evidence Index complete

---

## Final Review

- [ ] FR.1 Score review dimensions
- [ ] FR.2 Identify residual risks
- [ ] FR.3 Write DeliveryReport.md
````

---

# 17. Task.md 拆分与验证节奏的最佳平衡

你提出的判断是对的：**每写完一个小任务就做完整验证太慢**。更好的节奏是四层。

```text
Small Task
  └─ Micro-check：廉价、快速，只证明没有明显破坏

Task Group
  └─ Checkpoint validation：该组完整验证，必须做

Milestone
  └─ Milestone validation：跨组集成验证，必须做

Final
  └─ Full validation + review：全部验收、评分、交付
```

具体规则：

| 层级          | 什么时候做                | 验证强度 | 例子                          |
| ----------- | -------------------- | ---- | --------------------------- |
| Micro-check | 每个小任务后               | 很轻   | import、schema、单函数、文件存在、静态检查 |
| Checkpoint  | 一个大标题/Task Group 完成后 | 中等   | 跑该模块测试、真实样例局部验证             |
| Milestone   | 几个相关大组完成后            | 较强   | 端到端子流程、回归、性能抽样              |
| Final       | 全部完成后                | 最强   | 全 AC、真实数据、文档、review、报告      |

提前验证触发条件：

* 任务会影响公共接口
* 会影响数据格式
* 会影响架构
* 会删除或迁移数据
* 会改变性能路径
* 会引入外部依赖
* 会影响安全/权限/隐私
* 失败返工成本很高
* 当前 micro-check 已经失败

这套机制既不拖慢执行，也不会把验证推迟到最后才发现方向错了。

---

# 18. 本次 `v0.3.0/Plan.md` 建议落盘内容

````markdown
# Plan：AgentSkill v0.3.0 Hardening

Version: v0.3.0
Track: Meta-Skill / Agent Workflow / Software Engineering
WorkType: Refactor + Hardening
Level: L3
Current Mode: Plan
Execution Authorization: received by user request in current conversation
Scope: Modify AgentSkill workflow design, templates, stages, protocols, validation and anti-drift rules.

---

## 1. User Intent Lock

Primary goal:
构建一套能长期自主运行、跨科研/工程/写作/运维/简单任务的 AgentSkill 渐进式披露工作流。

Must preserve:
- Plan Mode 无授权不执行
- 大任务必须深度阅读、深度调研、充分交互
- Plan.md 与 Task.md 必须非常详细
- Task.md 是 Plan.md 的最小可执行可验证拆分
- 执行阶段按 Plan/Task 一次性完成
- 真实数据优先验证
- 禁止擅自 fallback / 降级
- 文档与代码同步交付
- 上下文压缩后继续工作
- 用户反馈后可回到 Plan → Execute 循环

Must avoid:
- 只坚持一轮 Plan Mode
- 用户未说 `开始执行` 就执行
- 忽略 Plan/Task
- 计划敷衍
- 调研不足
- 只用合成数据测试
- 单独依赖一种开发范式
- 模板/示例导致输出变短
- 执行阶段擅自兜底
- 最终报告空泛

---

## 2. Gap Analysis

| Problem | Current weakness | Required correction |
|---|---|---|
| Plan Mode 被绕过 | 规则偏说明性 | 增加硬门禁 G0-G9 |
| 长上下文后遗忘 | State 不够强制 | 增加 Resumption Block |
| Plan/Task 不够详细 | 缺少 Plan Quality Gate | 增加 Deep Plan 模板与评分 |
| 调研不足 | Research 要求不够可审计 | 增加 Research Log 标准 |
| 测试不真实 | 缺少 Data Level 门禁 | 增加真实数据优先验证协议 |
| 执行不按任务 | 缺少 Execution Preflight | 增加每组执行前检查 |
| 擅自兜底 | 禁止项不够硬 | 增加 Fallback Register |
| 交付不完整 | Delivery 格式不够强制 | 加强 DeliveryReport |
| 示例误导 | 示例太短 | 加全局 disclaimer |

---

## 3. Architecture

```text
SKILL.md
  ↓
Router Stage
  ↓
Hard Gates Protocol
  ↓
Plan Mode Protocol
  ↓
Deep Reading / Research Protocol
  ↓
Plan.deep + Task.deep + AcceptanceContract
  ↓
Execution Preflight
  ↓
Task Group Execution
  ↓
Real-data Validation
  ↓
Review
  ↓
DeliveryReport
  ↓
State / Resumption Block
  ↺
Feedback returns to Plan Mode
````

---

## 4. Deliverables

* Update main `SKILL.md`
* Add `protocols/`
* Harden `stages/plan`, `execute`, `validate`, `review`, `write`
* Add deep templates
* Add example disclaimers
* Add v0.3.0 Plan/Task/AcceptanceContract
* Add validation and review rules

---

## 5. Acceptance Contract

| AC    | Description                                                         | Validation                            |
| ----- | ------------------------------------------------------------------- | ------------------------------------- |
| AC-01 | L2/L3 without `开始执行` cannot execute                                 | Router/Plan/Execute gate text present |
| AC-02 | Plan.md requires deep reading/research/architecture/spec/validation | Plan.deep.template present            |
| AC-03 | Task.md decomposes Plan into executable/verifiable units            | Task.deep.template present            |
| AC-04 | Validation uses real data first                                     | Validation protocol present           |
| AC-05 | No unauthorized fallback                                            | Fallback protocol present             |
| AC-06 | Long-run context recovery works                                     | Resumption protocol present           |
| AC-07 | After authorization execute all Task groups unless blocked          | Execute protocol present              |
| AC-08 | Templates/examples cannot cap detail                                | Disclaimer added                      |
| AC-09 | Final delivery explains what was done and evidence                  | Delivery template present             |
| AC-10 | Feedback loops back to Plan Mode                                    | Review protocol present               |

---

## 6. Milestones

### M1：Hard Gates

Add `protocols/00-hard-gates.md`

### M2：Plan Hardening

Add deep Plan protocol and template.

### M3：Execution Hardening

Add execution preflight and no-fallback policy.

### M4：Validation Hardening

Add real-data-first validation matrix.

### M5：Long-run Stability

Add State/Resumption anti-drift protocol.

### M6：Templates and Examples

Update disclaimers and detail standards.

### M7：Review and Delivery

Strengthen scoring and final report.

---

## 7. Ready-to-Execute Gate

* [x] User requirements analyzed
* [x] Failure modes identified
* [x] Architecture selected
* [x] Protocol files specified
* [x] Templates specified
* [x] Stage patches specified
* [x] Task.md ready
* [x] Execution requested by user

````

---

# 19. 本次 `v0.3.0/Task.md` 建议落盘内容

```markdown
# Task：AgentSkill v0.3.0 Hardening

Version: v0.3.0
Linked Plan: v0.3.0/Plan.md
Execution Authorization: received
Mode: Execute

---

## 0. Preflight

- [x] 0.1 Confirm current repository structure
- [x] 0.2 Inspect existing AgentSkill/SKILL.md
- [x] 0.3 Inspect existing stages
- [x] 0.4 Inspect templates
- [x] 0.5 Compare user failure sample and desired sample
- [x] 0.6 Identify hardening needs

Checkpoint:
- [x] CP-0: Gap identified as enforcement/state-machine problem, not just missing prose

---

## 1. Task Group：Hard Gates

- [x] 1.1 Add `protocols/00-hard-gates.md`
- [x] 1.2 Define G0-G9 gates
- [x] 1.3 Define fail/blocked handling
- [x] 1.4 Define drift recovery

Checkpoint:
- [x] CP-1: Hard gates cover Plan, Research, Task, Execute, Validate, Evidence, Drift

---

## 2. Task Group：Plan Mode Hardening

- [x] 2.1 Add `protocols/01-plan-mode-and-deep-plan.md`
- [x] 2.2 Define User Intent Lock
- [x] 2.3 Define Deep Plan required sections
- [x] 2.4 Define candidate solution comparison
- [x] 2.5 Define architecture decision requirement
- [x] 2.6 Define Ready-to-Execute Gate

Checkpoint:
- [x] CP-2: Plan cannot be shallow and cannot enter Execute without authorization

---

## 3. Task Group：Research and Reading

- [x] 3.1 Require user material deep reading
- [x] 3.2 Require code/document/data maps
- [x] 3.3 Require Research Log
- [x] 3.4 Require evidence impact mapping

Checkpoint:
- [x] CP-3: Plan must show what was read, what was learned, and how it changed design

---

## 4. Task Group：Execution Discipline

- [x] 4.1 Add Execution Preflight
- [x] 4.2 Force Task Group order
- [x] 4.3 Define after-authorization continuous execution rule
- [x] 4.4 Add debug/ops/training monitor runbook requirement
- [x] 4.5 Prohibit Plan drift during execution

Checkpoint:
- [x] CP-4: Execute stage cannot ignore Plan/Task

---

## 5. Task Group：Validation

- [x] 5.1 Add real-data-first validation protocol
- [x] 5.2 Define Data Level labels
- [x] 5.3 Define micro/checkpoint/milestone/final validation
- [x] 5.4 Define validation dimensions for software/research/docs/PDF/visual
- [x] 5.5 Define failure handling

Checkpoint:
- [x] CP-5: Validation cannot pass without evidence and data source label

---

## 6. Task Group：Fallback and Boundaries

- [x] 6.1 Add fallback protocol
- [x] 6.2 Prohibit execute-time fallback
- [x] 6.3 Define Fallback Register
- [x] 6.4 Define blocked handling

Checkpoint:
- [x] CP-6: No silent fallback/degradation remains allowed

---

## 7. Task Group：Long-run Anti-drift

- [x] 7.1 Add Resumption Block
- [x] 7.2 Define context compression recovery
- [x] 7.3 Define drift signals
- [x] 7.4 Define drift recovery entry

Checkpoint:
- [x] CP-7: Context compression no longer permits stopping or forgetting Skill

---

## 8. Task Group：Templates and Examples

- [x] 8.1 Add disclaimer to all templates
- [x] 8.2 Add disclaimer to all examples
- [x] 8.3 Add Plan.deep.template.md
- [x] 8.4 Add Task.deep.template.md
- [x] 8.5 Add ValidationMatrix / PlanQualityGate / ResumptionBlock templates

Checkpoint:
- [x] CP-8: Templates/examples no longer imply short output

---

## 9. Final Validation

- [x] 9.1 Check all user-reported failures addressed
- [x] 9.2 Check no single development paradigm is treated as sole method
- [x] 9.3 Check real data validation is mandatory
- [x] 9.4 Check no unauthorized execution is allowed
- [x] 9.5 Check feedback loop returns to Plan Mode
- [x] 9.6 Check final delivery format is defined

---

## 10. Final Review

- [x] 10.1 Requirement fit reviewed
- [x] 10.2 Architecture reviewed
- [x] 10.3 Remaining implementation note: remote repository must be patched manually or by an agent with repo write access
````

---

# 20. 最终 DeliveryReport 格式

把 `templates/DeliveryReport.template.md` 改成这种更硬的结构。

```markdown
# Delivery Report：<Task Name>

Version:
Plan:
Task:
Status: pass | needs_rework | blocked
Date:

---

## 1. What Was Done

| Area | Result | Linked Task | Evidence |
|---|---|---|---|

---

## 2. Files Changed

| File | Change Type | Reason | Linked Plan/Task |
|---|---|---|---|

---

## 3. Acceptance Criteria Result

| AC | Status | Evidence | Notes |
|---|---|---|---|

---

## 4. Validation Summary

| Validation | Data Level | Command/Tool | Result | Evidence |
|---|---|---|---|---|

---

## 5. Review Score

| Dimension | Score | Evidence |
|---|---:|---|
| Requirement fit | | |
| Plan compliance | | |
| Task completion | | |
| Correctness | | |
| Real-data validation | | |
| Architecture quality | | |
| Documentation quality | | |
| Maintainability | | |
| Risk handling | | |

Overall Score:

---

## 6. Residual Risks

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|

---

## 7. Limits

明确说明未完成、未验证、受限、需要人工判断的部分。

---

## 8. Final Statement

用事实总结交付结果，不追加新的开放式选择，不把未验证内容说成已完成。
```

---

# 21. 这版修改如何逐条解决你指出的问题

| 你指出的问题                | v0.3.0-hardening 的解决方式                         |
| --------------------- | ---------------------------------------------- |
| Plan 阶段只坚持一轮          | 每轮 G0 Boot + G1 Plan Mode Gate，未授权只能 Plan      |
| 用户没说开始执行就写代码          | 唯一授权口令 `开始执行`，其它表达无效                           |
| 执行时不按 Skill/Plan/Task | Execute Preflight 强制读取 State/Plan/Task         |
| 一两轮后无视 Skill          | Resumption Block + Drift Recovery              |
| 测试不用真实数据              | Real Data Validation Gate                      |
| 测试规则不符合用户需求           | Validation Matrix 绑定 AC                        |
| 规划没深入阅读研究             | Deep Reading Gate + Research Gate              |
| 架构/技术选型不充分            | Candidate Solutions + Architecture Decision    |
| Plan/Task 很敷衍         | Deep Plan Template + Plan Quality Gate         |
| 用户可能犯错                | Plan Mode 允许智能体提出证据驱动建议                        |
| 长任务失忆                 | State.md 作为唯一运行状态源                             |
| 执行阶段做不到一次性做完          | 授权后连续执行 Task Groups，除硬阻塞                       |
| 用户不满意后怎么办             | Review Feedback Loop 回到 Plan Mode              |
| 模板/example 太简化        | 全局 disclaimer + 深度模板                           |
| 代码擅自兜底                | Fallback Register + execute-time fallback 禁止   |
| 不想单独 TDD              | 改为多范式组合，不单独强调一种                                |
| 文档不配套                 | Documentation Plan + DeliveryReport 强制         |
| Debug/训练监控            | Runbook + metrics + threshold + stop condition |

---

# 22. 应提交的 ChangeLog

```markdown
# ChangeLog：AgentSkill v0.3.0

## Added

- Hard Gates protocol
- Deep Plan protocol
- Real-data-first validation protocol
- Resumption and anti-drift protocol
- Fallback and boundaries protocol
- Deep Plan template
- Deep Task template
- Validation Matrix template
- Plan Quality Gate template
- Execution Preflight template
- Resumption Block template
- Fallback Register template

## Changed

- Main SKILL.md now treats L2/L3 workflow as a state machine
- Plan Mode authorization is stricter
- Execution requires preflight
- Validation requires data level and evidence
- Templates/examples are explicitly non-limiting
- Review requires scoring and evidence
- Feedback returns to Plan Mode

## Fixed

- Unauthorized execution risk
- Plan/Task shallow decomposition
- Skill drift after long context
- Synthetic-only validation misuse
- Silent fallback/degradation
- Over-reliance on a single development method
- Final report ambiguity

## Remaining Manual Step

- Apply the patch text to the repository and run repository-level markdown/link validation.
```

---

这份 0.3.0-hardening 的关键不是“写得更长”，而是把智能体容易违反的地方全部变成硬门禁：未授权不能执行，Plan 不够深不能执行，Task 不可验证不能执行，真实数据缺失不能假装验证，兜底没进 Plan 不能写进代码，上下文压缩后必须从 State 恢复。这样才能让 Skill 在科研、工程、写作、运维、调试、长任务执行中保持稳定。

[1]: https://github.com/Nobody-ML/agentskill/tree/main/AgentSkill "agentskill/AgentSkill at main · Nobody-ML/agentskill · GitHub"
[2]: https://github.com/Nobody-ML/agentskill/blob/main/AgentSkill/SKILL.md "agentskill/AgentSkill/SKILL.md at main · Nobody-ML/agentskill · GitHub"
[3]: https://agentskills.io/specification "Specification - Agent Skills"
[4]: https://www.iso.org/standard/72089.html " ISO/IEC/IEEE 29148:2018 - Systems and software engineering — Life cycle processes — Requirements engineering"

```