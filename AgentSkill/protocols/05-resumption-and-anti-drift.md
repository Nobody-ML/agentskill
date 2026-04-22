# 05-resumption-and-anti-drift：长程续跑与抗漂移协议

适用范围：
- Track：Research / Software / Writing
- Level：L2 / L3（强制）

目标：
解决三类失控：
1) 跑几轮后忘了 Skill 规则、忘了门禁、忘了 Plan/Task；
2) 上下文压缩/重启/中断后无法继续；
3) 执行中发生漂移（越权执行、偷换验收、跳过真实数据、擅自兜底）。

相关门禁：
- `protocols/00-hard-gates.md`：G0（Boot）/ G9（Drift Recovery）

---

## 1) State.md 是唯一运行状态源（Single Source of Truth）

硬规则：
- 长任务不得依赖对话记忆；一切关键事实必须落盘在 `State.md`。
- 任何“完成/通过/已实现”的结论，必须能在 `State.md` 的 Evidence Index 找到证据入口。

State.md 必须长期保存：
- 边界与禁区（Allowed/Forbidden）
- Execution Authorization 状态与授权范围
- 当前 Mode、当前 Task Group、Next Action
- 决策记录（Decision Log）
- 证据索引（Evidence Index）

---

## 2) 每轮必须写入或确认的最小状态

每轮结束前，至少确认/写入以下字段（写在 State.md）：

- `Current Mode`：Plan / Execute / Validate / Review / Write / Repair
- `ExecutionAuth`：required / received / not_required / revoked / scope_changed
- `Current Task Group`：当前任务组名
- `Next Action`：下一步 1–3 个动作（按顺序）
- `Blockers`：阻塞点与最小输入
- `Evidence Index`：新增证据入口
- `Files read recently`：本轮深读范围（路径或链接）
- `Commands run recently`：本轮运行命令（若有）

---

## 3) Resumption Block（可续跑块）

Resumption Block 用于对话压缩、交接、重启后的快速恢复；它既要短，也要足够“可执行”。

推荐格式（写入 State.md；也可在 Plan.md 的末尾冗余一份）：

```yaml
RESUMPTION_BLOCK_v0.3:
  mode: "Plan"
  track: "Software"
  work_type: "Build"
  level: "L3"
  execution_auth: "required"
  intent_lock_ref: "Plan.md#User-Intent-Lock"
  current_task_group: "Task Group: <name>"
  checkpoint_level: "checkpoint" # micro-check | checkpoint | milestone | final
  next_actions:
    - "action 1"
    - "action 2"
  blockers:
    - "blocker 1 (minimal input)"
  last_evidence:
    - "path/to/evidence"
  risks:
    - "risk 1"
  forbidden:
    - "no unauthorized execution"
    - "no unplanned fallback"
```

模板参考：
- `templates/ResumptionBlock.template.md`

---

## 4) 上下文压缩 / 中断恢复步骤（强制）

当出现以下任一情况：上下文变短、收到交接摘要请求、工具中断、会话重启、长时间未推进。

恢复步骤（必须按顺序执行）：
1) 读取 `State.md`：定位 Mode/ExecutionAuth/Next Action/Blockers
2) 读取当前版本 `Plan.md` 与 `Task.md`：确认意图锁、边界、验收、验证矩阵、任务组
3) 运行 G0（Boot Gate）并写入 Gate Summary
4) 对照最新用户消息检查：
   - scope 是否变化（新增想法/不满意/新约束）
   - 是否撤销/改变授权（scope_changed/revoked）
5) 若 scope 变化：回 Plan Mode 更新 Plan/Task，再重新走 Ready-to-Execute Gate
6) 若 scope 未变且已授权：回到 Execute/Validate，按 Task Group 继续推进

---

## 5) Drift Signals（漂移信号）

出现任一信号视为“需要停线”的漂移：
- 未授权进入执行（ExecutionAuth!=received 但修改实现/跑训练/生成交付物）
- 忽视 Plan/Task：执行内容无法映射到 Task
- 需求偷换：验收标准在执行中被静默降低
- 真实数据门禁被绕过：可得真实数据却用 synthetic 且无记录与确认
- 擅自兜底/降级：Plan 未登记却在执行中加入 fallback
- 不更新 State：连续多轮不写 Next Action / Evidence Index
- 上下文压缩后直接“继续干活”，没有恢复步骤

---

## 6) Drift Recovery（漂移恢复流程）

一旦命中 Drift Signals：
1) 立即停线：不继续执行、不扩范围、不加兜底
2) 记录事故：在 State Decision Log 写清“发生了什么、影响范围、如何修复”
3) 回到 Plan Mode：
   - 重读核心材料（State/Plan/Task）
   - 修复 Plan/Task（补验收/补边界/补验证矩阵/补兜底登记）
   - 必要时走 Change Control（见 `templates/ChangeControl.template.md`）
4) 重新过门禁（G4/G5/G6/G7/G8），再继续推进

