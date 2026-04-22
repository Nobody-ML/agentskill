> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Validation Matrix（验收 → 验证 → 证据映射）

适用：Level≥L2（建议），Level=L3（强制）。

目的：
- 让每条验收标准都有对应的验证方法与证据入口。
- 让“通过”可以复跑、可审计、可复现。

---

## 1) Data Acquisition Log（数据获取记录）

| Need | Priority | Attempt | Result | Evidence | Next |
|---|---|---|---|---|---|
| `<what data>` | real | `<attempt>` | `<ok/failed>` | `<path/link>` | `<...>` |

---

## 2) Matrix

字段说明：
- `AC`：验收条目编号（AC-001…）
- `Dimension`：验证维度（Correctness / Spec / Robustness / Performance / Security / Visual / Repro / Ops）
- `Data`：real / sanitized-real / synthetic
- `Cadence`：micro-check / checkpoint / milestone / final
- `Method`：测试/脚本/手动检查/截图对比/实验
- `Command`：可复跑命令（或步骤）
- `Evidence`：证据入口（文件/日志/截图/报告）

| AC | Dimension | Data | Cadence | Method | Command / Steps | Pass Criteria | Evidence | Status |
|---|---|---|---|---|---|---|---|---|
| AC-001 | Correctness | real | checkpoint | test | `<cmd>` | `<...>` | `<path>` | pending |

---

## 3) Summary

- 覆盖率（AC 覆盖）：`<...>`
- 真实数据覆盖（real/sanitized-real）：`<...>`
- 仍阻塞的验证：`<...>`
