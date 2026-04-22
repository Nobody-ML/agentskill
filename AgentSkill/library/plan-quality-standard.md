# Plan Quality Standard（深计划质量标准 / 反敷衍门禁）

适用：
- Track：Research / Software / Writing
- Level：L2（强烈建议）/ L3（默认强制）

目的：
把“写个大纲”升级为“可执行规格（spec）”。当任务变大时，Plan 必须做到：
- 能指导实现（按图施工）
- 能指导验证（证据门禁）
- 能支持复盘与复现（可追溯、可续跑）
- 能抵抗长对话漂移（State/Resumption Block）

对应硬门禁：
- `protocols/00-hard-gates.md`：G4（Plan Quality Gate）
- `protocols/01-plan-mode-and-deep-plan.md`：Deep Plan 最低结构

---

## 1) 什么是“敷衍的 Plan”（反例信号）

命中任一项，基本可以判定 Plan 会在执行阶段失控：

- 只有“步骤列表”，没有**验收标准**与**失败判据**
- 只有“用某某库实现”，没有**候选方案对比**与取舍理由
- 没有把任务拆到 Task Group，并且没有 checkpoint/milestone/final 的验证节奏
- 没有明确**真实数据策略**，默认用 synthetic 跑通当作完成
- 没有写 Workdir/Resume Strategy，任务中断后无法续跑
- “风险/依赖/权限/数据”没有落盘，执行期才发现缺口
- 出现“兜底/降级”但没有 Plan 阶段登记与确认（执行期偷偷补）

把这些信号写进 Review 的门禁（或 Gate Summary）是必要的：它们不是“文风问题”，而是工程失控的前兆。

---

## 2) 深计划的最小结构（L3 必须具备）

最低要求（少一个都不算 Plan 就绪）：

1) **User Intent Lock**
   - must_preserve / must_avoid / non_goals（防漂移、防偷换验收）
2) **Inputs & Deep Reading**
   - 读过什么、结论是什么、如何影响方案
3) **Research Log（当需要外部事实时强制）**
   - 来源、抽取事实、Impact、Open questions（可追溯）
4) **Candidate Solutions + 推荐路线**
   - 至少 2 个候选 + 1 个推荐；必须写拒绝理由
5) **Architecture / Method Chain**
   - 端到端链路图（输入→处理→产出→失败恢复）
6) **Pipeline Stages 表（阶段→技术→验证）**
   - 每阶段：输入输出工件、候选技术、推荐技术、关键风险、验证与证据
7) **Specification**
   - Data Model / Interfaces / State / Error handling / Observability
8) **Acceptance Contract + Validation Matrix**
   - 验收断言可执行；验收→验证→证据能闭环
9) **Real Data Strategy**
   - real/sanitized-real 优先；synthetic 必须有确认与风险说明
10) **Workdir & Resume Strategy**
    - 断点续跑、失败隔离、恢复标记
11) **Fallback Register（默认空）**
    - 需要兜底必须 Plan 阶段登记并确认；执行期不得新增
12) **Resumption Block**
    - 上下文压缩后只靠这个也能继续推进到下一个 checkpoint

建议模板：
- `templates/Plan.deep.template.md`
- `templates/PlanQualityGate.template.md`
- `templates/ValidationMatrix.template.md`

---

## 3) Pipeline Stages（阶段→技术→验证）怎么写才算“有密度”

目标：让执行阶段“只要按表走”就能稳定推进，并且每个阶段都有停线条件。

### 3.1 最小字段（每行都必须写）

| 字段 | 含义 | 典型错误 |
|---|---|---|
| Stage | 阶段名 | 把整个系统写成 2 个大阶段（会失控） |
| Goal | 该阶段解决什么 | 写成空话（“处理数据”“完成实现”） |
| Inputs → Outputs | 输入/产出工件 | 只写“输入=数据，输出=结果”（不可追溯） |
| Candidate tech | 至少 2 个候选 | 只写一个库名（没有取舍） |
| Recommended tech | 选哪个、为什么 | “推荐=某库”（没有理由与边界） |
| Key risks | 2–5 个风险点 | 不写风险（后面必爆） |
| Validation & evidence | 怎么验、证据产物 | 只写“测试一下”或“不需要验证” |

### 3.2 写“验证”时必须显式声明三件事

1) scope：checkpoint / milestone / final  
2) data_type：real / sanitized-real / synthetic  
3) evidence：日志/截图/报告/命令输出/基准数据入口  

---

## 4) Plan Mode 的收敛节奏（多轮对齐）

Plan Mode 不是“一轮问完”，而是每轮都要：
- 新增理解（锁定/边界/验收更清）
- 新增证据（读了/查了什么）
- 新增落盘（Plan/Task/State 更新）
- 新增下一步（Next Action 1–3 条，按顺序）

提问规则（防“无限选择题”）：
- 每轮最多 3–6 个问题
- 每个问题都必须“会改变方案/验收/边界/验证方式”之一
- 必须给一个推荐默认值（收敛式）

参考：`library/plan-mode-interaction.md`

---

## 5) 深计划评分（用于 Review/自检）

评分目的：不是追求“写得长”，而是保证“写得可执行、可验证、可续跑”。

建议维度（每项 0–2，总分 10）：
1) Intent Lock（防漂移）
2) Evidence（深读+调研可追溯）
3) Spec（接口/错误/状态/观测）
4) Pipeline（阶段→技术→验证密度）
5) Validation（真实数据策略+矩阵+节奏）

门禁建议：
- < 7：不要请求执行授权；先补齐 Plan
- ≥ 7：允许请求执行授权（仍需通过 G4/G5）

