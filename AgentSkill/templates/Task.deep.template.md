> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Task：<Project / Task Name>

Version:
Track:
WorkType:
Level:
Execution Authorization: not_received
Last Updated:

---

## Task Status Legend

- `[ ]` pending
- `[~]` in progress
- `[x]` done
- `[!]` blocked (needs input)

---

## Execution Rules

1) 未收到执行授权口令前（Execution Authorization!=received）不得进入执行。
2) 执行必须映射到 Task；不在 Task 中的改动不得发生。
3) 验证采用分层节奏：micro-check → checkpoint → milestone → final（见 `protocols/04-validation-real-data-first.md`）。
   - micro-check：廉价、快速、用于避免把明显错误带到检查点（不等于正式验证）
   - checkpoint：每个 Task Group 结束必须执行；通过后再把本组任务统一标记为 `[x]`
   - milestone/final：更宽覆盖，用于支撑阶段性交付与最终 PASS
4) 当任务包含“可感知质量/交互功能/格式保持”（例如 PDF/排版/渲染产物）：
   - checkpoint/milestone/final 必须包含渲染证据（截图/报告）与几何检查（溢出/重叠/越界）
   - 涉及链接/目录/跳转的，必须包含功能检查与证据入口
5) 禁止执行期擅自兜底/降级；需要 fallback 只能在 Plan 阶段登记并确认。
6) 每个 Task Group 结束必须做 Checkpoint Validation 并更新证据索引。

---

## 0. Preflight

- [ ] 确认 Execution Authorization=received（已落盘）
- [ ] 确认 Allowed/Forbidden 边界
- [ ] 确认本轮要处理的 Task Group 与验证层级
- [ ] 确认数据来源与 data_type（real/sanitized-real/synthetic）
- [ ] 记录将运行的命令与将修改的文件范围
- [ ] 预估成本（时间/资源）与回滚点

---

## 1. Task Group：<Name>

### Tasks

- [ ] <atomic task 1>
- [ ] <atomic task 2>
- [ ] <atomic task 3>

### Checkpoint Validation

- data_type:
- commands:
- expected evidence:
- pass/fail criteria:
- evidence links:

---

## 2. Task Group：<Name>

（同上结构）

---

## Milestone Validation

- scope:
- data_type:
- commands:
- evidence:

---

## Final Validation

- acceptance contract coverage:
- evidence index updated:
- residual risks:

---

## Final Review

- score:
- defects:
- rework list:
