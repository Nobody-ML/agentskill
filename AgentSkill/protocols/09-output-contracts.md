# 09-output-contracts：对外输出契约（回复格式协议）

适用范围：
- Track：Research / Software / Writing
- Level：L2 / L3（强制）

目标：
让对外回复固定为“可续跑、可复查”的结构，避免跑几轮后丢失上下文与门禁信息。

---

## 1) Plan Mode 回复格式（建议固定）

1) `【Mode】Plan | Level=<L?> | ExecutionAuth=<required/not_required/received>`
2) 当前状态（用一句话描述当前处于哪一步）
3) 本轮完成的深读/调研（证据入口）
4) 已更新的工件（Plan/Task/State/其它）
5) 阻塞点（最小输入）
6) 下一步（按顺序 1–3 条）

---

## 2) Execution Checkpoint 回复格式（组末检查点）

1) `【Mode】Execute/Validate | ...`
2) 执行进度（本组完成了哪些任务）
3) Preflight（是否通过，若失败写阻塞点）
4) Checkpoint validation（跑了什么、数据类型、结果、证据入口）
5) 下一组的 Next Action
6) State 更新说明（Next Action/Evidence Index 是否已写）

---

## 3) Final Delivery 回复格式（最终交付）

交付必须使用 Delivery Report（或等价结构），并包含：
- What was done
- Files changed
- Acceptance & Validation summary
- Review score
- Residual risks & limits
- Resumption Block（便于后续迭代）

模板参考：
- `templates/DeliveryReport.template.md`

