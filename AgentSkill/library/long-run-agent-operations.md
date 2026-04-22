# Long-run Agent Operations（长任务续跑 / Ops 作战手册）

适用：
- Track：Software / Research（长实验/训练）/ Writing（长文档项目）
- Level：L3（强制），L2 命中长任务信号时同样适用

目的：
解决长任务常见失控点：
- 跑着跑着忘规则、忘边界、忘 Plan/Task
- 上下文压缩后停机或乱续跑
- 长任务无记录、无 checkpoint，出问题不可复盘
- 训练/批处理只“盯屏幕”，没有证据与恢复步骤

对应协议：
- `protocols/05-resumption-and-anti-drift.md`
- `protocols/08-long-running-ops.md`
- `protocols/00-hard-gates.md`：G0/G6/G8/G9

---

## 1) Long-run 的定义（触发信号）

命中任一信号就按 long-run 处理：
- 预计跨多轮对话/多天推进
- 运行时长 > 30–60 分钟（训练/批处理/爬取/大规模测试）
- 会产生大量产物（多文件、多页、多实验）
- 失败代价高（失败会导致大量返工）

---

## 2) 必备工件（没有就不允许运行）

最小工件集合：
- `State.md`：Next Action + Resumption Block + Evidence Index
- `Task.md`：任务组 + checkpoint/milestone/final
- Runbook（Ops/训练/长实验）：建议用 `templates/Ops-Runbook.template.md`
- 工作目录（workdir）规范：产物可定位、可清理、可复跑

---

## 3) 工作目录（workdir）标准

建议结构（可按项目改名，但不要混乱）：

```text
.work/job_id/
  runbook.md
  inputs/
  logs/
  checkpoints/
  outputs/
  reports/
  evidence/
  resume_markers/
```

要求：
- outputs 与 reports 必须能映射到 Task Group 与验证 scope
- 每次关键操作产生证据入口（日志/报告/截图）

---

## 4) Checkpoint 策略（长任务的生命线）

硬规则：
- 长任务必须有 checkpoint（周期性保存点）
- checkpoint 必须可恢复（写清恢复命令与前置条件）

建议：
- 每 N 分钟或每 N 单位（step/page/file）保存一次
- 每个 milestone 前做一次“更宽验证”

---

## 5) Monitoring Loop（训练/服务/批处理监控循环）

最小闭环：
1) 采集：logs/metrics/关键产物
2) 判断：阈值与失败判据（Plan/Runbook 明确）
3) 处置：暂停/降载/重启/回滚（Runbook 明确）
4) 记录：把“做了什么 + 为什么 + 结果”写进 Evidence Index

禁止：
- 无阈值的“盯盘”
- 无记录的“手工操作”

---

## 6) 上下文压缩/中断恢复（Resumption Discipline）

恢复顺序（必须按这个来）：
1) 读 `State.md`（Resumption Block）
2) 读当前 `Plan.md` / `Task.md`
3) 判断当前 Mode/Auth/Task Group/Next Action
4) 继续推进到下一个 checkpoint（不要跳组）

恢复后第一件事不是执行，而是确认：
- 边界（Allowed/Forbidden）
- 本轮要推进的任务组
- 验证 scope 与 data_type

---

## 7) 失败处理（Stop-the-line）

一旦出现任一问题，必须停线并回到 Plan/Preflight：
- 权限/数据缺失
- 关键指标异常（loss 发散、OOM、吞吐骤降）
- 输出明显偏离验收（例如视觉/排版崩）
- 需要新增兜底/降级（Plan 未登记）

停线时必须输出：
- 失败点（哪个阶段/哪个任务）
- 证据入口（日志/截图/报告）
- 最小修复路径（下一步 1–3 条）

