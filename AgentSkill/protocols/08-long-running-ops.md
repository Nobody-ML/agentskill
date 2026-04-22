# 08-long-running-ops：长任务运行与监控协议（Ops / Debug / Training Monitor）

适用范围：
- Track：Software（WorkType=Ops/Debug），以及 Research 的长实验/训练任务
- Level：L2 / L3（强制）

目标：
让“替用户跑任务/盯训练/排障”变成有 Runbook、有观测点、有证据的可控流程，避免只盯屏幕不记录、出问题无法复盘。

相关门禁：
- `protocols/00-hard-gates.md`：G6（Preflight）/ G8（Evidence）
- `templates/Ops-Runbook.template.md`

---

## 1) Operation Record（运行记录，必须落盘）

每次长任务运行必须记录：
- 启动命令与参数
- 环境信息（版本、GPU/驱动、关键依赖）
- 输入数据与数据类型（real/sanitized-real/synthetic）
- 输出产物路径与命名约定
- 监控指标与阈值
- Checkpoints（周期性保存点）
- 失败原因与恢复步骤

建议工件：
- Runbook：`templates/Ops-Runbook.template.md`
- State Evidence Index：记录日志与指标入口

---

## 2) Monitoring Loop（监控循环）

监控必须包含：
- 采集：日志/指标/关键产物
- 判断：阈值与失败判据（例如 loss 不下降、OOM、吞吐退化）
- 处置：降载/重启/回滚/暂停（按 Runbook）
- 记录：把每次处置写入 Operation Record

---

## 3) Debug Loop（排障循环）

排障顺序：
1) 复现（最小复现/最小数据）
2) 观测（补足 logs/metrics/trace）
3) 定位（缩小到模块/提交/配置）
4) 修复（小步改动）
5) 回归（同层验证 + 至少一个更宽验证）

---

## 4) No untracked jobs（禁止无记录运行）

禁止：
- 没有 Runbook 就开跑长任务
- 没有 Checkpoint 就开跑长训练
- 没有证据索引就宣称“跑过了/没问题”

