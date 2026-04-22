# Task Decomposition Standard（Task 拆分标准 / 执行与可验证性的平衡）

适用：
- Track：Research / Software / Writing
- Level：L2（建议）/ L3（强制）

目的：
把 Plan.md 的意图与规格拆成“可执行、可验证、可追溯”的最小单元，同时避免两种极端：
- 极端 A：每写一行就做全量验证（慢、碎、不可持续）
- 极端 B：攒一大坨再测（返工爆炸、证据链断裂）

对应硬门禁：
- `protocols/00-hard-gates.md`：G5（Task Quality Gate）、G6（Preflight）、G7/G8（验证与证据）
- `stages/execute/SKILL.md`：任务组推进到 checkpoint

---

## 1) Task.md 的基本结构（强制）

Task 必须按 **Task Group（任务组）**组织。每组必须包含：
- Tasks（可勾选的最小任务）
- Checkpoint Validation（组末检查点验证）

并且必须存在：
- Milestone Validation（里程碑验证，覆盖多个组）
- Final Validation（最终验证）
- Final Review（评分与返工清单）

推荐模板：
- `templates/Task.deep.template.md`（L3）

---

## 2) “最小任务”怎么判定（Atomic Task Definition）

一个小任务应满足：
- **可执行**：一句话能说清要做什么；能指向要改的模块/文件/实验脚本/章节
- **可验证**：至少能做一个 micro-check（廉价验证）或能产出一个可检查的工件
- **可追溯**：能映射回 Plan 的某一段（需求/阶段/风险/验收条目）

常见反例（应拆小或重写）：
- “完善功能”“优化性能”“改进文档”（不可执行、不可验）
- “重构所有模块”（范围爆炸）
- “把 X 全部搞好”（无法定位完成边界）

---

## 3) 验证节奏：micro-check → checkpoint → milestone → final

这是推荐的“快慢平衡”：

1) **micro-check（廉价检查）**
   - 发生时机：每个小任务完成后（或同一小批任务完成后）
   - 目标：防止把明显错误带到 checkpoint
   - 例子：
     - Software：类型检查/最小运行/关键函数自测/简单 lint
     - Research：指标能算、脚本能跑、配置能加载
     - Writing：章节结构一致、引用占位无缺失、示例语法无错误

2) **checkpoint validation（组末检查点）**
   - 发生时机：一个 Task Group 完成后必须做
   - 目标：证明“这一组没把系统搞坏”，并生成可复查证据

3) **milestone validation（里程碑验证）**
   - 发生时机：多个组完成后；或计划中的阶段性交付点
   - 目标：更宽的回归 + 性能/资源 smoke check + 规范/文档一致性

4) **final validation（最终验证）**
   - 发生时机：全部任务完成后
   - 目标：覆盖 Acceptance Contract / Validation Matrix 的所有关键断言

硬规则：
- 小任务可以批量做完再 checkpoint，但每组结束必须 checkpoint。
- 高风险变更不得拖到组末：必须提前验证（见第 4 节）。

---

## 4) 什么时候必须“提前验证”（风险驱动早停）

命中任一信号，必须把验证前置到更早的 checkpoint：

- 不可逆操作：删除/覆盖/迁移/格式破坏
- 核心接口：公共 API、数据模型、配置格式、协议兼容
- 性能敏感路径：训练/推理主循环、IO/并发热点
- 可感知质量：排版/渲染/UI/图示（不等到最终才看）
- 功能层保持：链接/目录/注释/表单（外科任务）
- 长任务：训练/批处理（无 checkpoint=不可控）

---

## 5) Task Group 的划分方法（建议）

三种常见分法（选一种即可，别混乱）：

1) 按流水线阶段（推荐给复杂系统）
   - Preflight → Extract → IR/Schema → Core Transform → QA/Validate → Delivery
2) 按组件边界（推荐给中大型工程）
   - CLI/Config → Core Lib → Integrations → Tests → Docs
3) 按里程碑交付（推荐给长项目）
   - MVP → Beta → Production

要求：
- 每个组都要有明确产出物（artifact），并在组末 checkpoint 验证它。

---

## 6) Task 写法规范（每条任务都要“落地”）

建议每条任务包含这些要素（可简写，但不能缺关键项）：
- 目标：做什么
- 产出：生成/修改的工件（路径/接口/报告）
- 约束：must_preserve/must_avoid 的影响点
- 验证：micro-check 或 checkpoint 的对应关系
- 证据：Evidence Index 入口（日志/截图/输出文件）

---

## 7) 批量推进的上限（避免攒一大坨）

同一 Task Group 内允许批量推进，但建议设置上限：
- 时间上限：60–90 分钟未到 checkpoint → 插入 checkpoint 或缩小改动面
- 变更上限：连续跨 3+ 个关键模块/公共接口 → 插入 checkpoint
- 不稳定信号：任何 micro-check 已出现异常 → 立即停线到 checkpoint 验证/修复

---

## 8) 对“你提出的节奏”的结论（写进 Skill 的可执行规则）

你的思路是正确的：Task 的原子拆分用于可执行性与可追溯性，但验证不应每步全量跑。

推荐落地方式：
- 小任务：做 micro-check（廉价）
- 一个大标题（Task Group）结束：做 checkpoint validation（强制）
- 多个组完成：做 milestone validation（更宽）
- 全部完成：final validation + review（总评）

并用“提前验证触发器”避免把高风险赌到最后。

