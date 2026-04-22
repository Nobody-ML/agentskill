# Validation: Real Data First（真实数据优先验证清单）

适用：
- Track：Research / Software / Writing
- Level：L2 / L3（强制）

目的：
把“真实数据优先”从口号变成可执行门禁：能记录尝试、能明确阻塞、能避免 synthetic 造成虚假安全感。

对应协议：
- `protocols/04-validation-real-data-first.md`
- `stages/validate/SKILL.md`
- `protocols/00-hard-gates.md`：G7/G8

---

## 1) 数据类型（必须标注）

- real：真实数据/真实场景样本
- sanitized-real：脱敏真实样本（允许裁剪/打码/去标识）
- synthetic：模拟数据（最后一档，需用户确认）

硬规则：
- Level≥L2：默认至少一次关键路径验证必须使用 real 或 sanitized-real。

---

## 2) 数据获取优先级（从上到下，命中即停）

1) 用户提供的真实样本（可脱敏）
2) 仓库内真实样本/fixture（来自真实分布或真实历史）
3) 最小真实日志采集（只读、脱敏、最小化）
4) 权威公开数据集（研究常用）
5) synthetic（仅当用户确认无真实/脱敏样本）

---

## 3) 当只能用 synthetic（必须同时满足）

- 已尝试 1–4 的入口，并记录不可用原因（权限/合规/不可获得）
- Plan/State 中有用户确认记录：“确实没有可用真实样本（含脱敏样本）”
- 验证结论必须显式标记 synthetic 风险：可能遗漏哪些失败模式
- Task 中必须安排“补真实数据回归验证”的后续任务（否则结论只能算临时通过）

---

## 4) 证据（Evidence）最小要求

每次验证至少记录：
- scope：checkpoint / milestone / final
- data_type：real / sanitized-real / synthetic
- command / action
- exit code（如有）
- artifact 路径（日志/报告/截图）

并写入：
- `State.md` 的 Evidence Index

