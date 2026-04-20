# Reproducibility（复现协议）检查表

适用：Research（强制）、Software（建议）、Writing（当含代码/实验/命令时强制）。

---

## 触发条件

- 任何需要“可验证/可复现”的结论
- 任何实验结果、性能对比、算法验证
- 任何需要他人照做的教程

---

## A. Research 复现协议（强制）

必须记录：
- [ ] 环境：OS/CPU/GPU/驱动/依赖版本
- [ ] 数据：数据集版本、切分、预处理、许可
- [ ] 参数：seed、超参、训练/推理设置
- [ ] 指标：定义与计算脚本
- [ ] 基线：来源与理由
- [ ] 消融：验证哪些假设
- [ ] 失败判据：什么情况下结论不成立

证据要求：
- [ ] 一条可重复运行的命令（或脚本入口）
- [ ] 结果摘要与日志路径写入 State.md Evidence Index

来源：
- `Reference/Modern Software Engineering/Modern Software Engineering.md` — Ch.7 *Empiricism*（避免自我欺骗）

---

## B. Software 复现协议（建议 L3 强制）

必须记录：
- [ ] 运行/测试命令（含必要环境变量）
- [ ] 依赖安装方式与版本（lockfile 或明确版本）
- [ ] 最小验证集合（测试/手动路径）

证据要求：
- [ ] 关键命令的 exit code + 输出摘要 + 日志路径

来源：
- `superpowers/skills/verification-before-completion/SKILL.md`（完成前验证门禁）

---

## C. Writing 复现协议（当文档包含“照做步骤”时强制）

必须包含：
- [ ] 前置条件（环境、依赖、权限、数据）
- [ ] 步骤可执行（命令/点击路径明确）
- [ ] 期望输出（读者如何判断成功）

证据要求：
- [ ] 至少一次真实跑通记录（写入 State.md Evidence Index）

---

## D. 复现信息的落盘位置

- `State.md`：Evidence Index（复现命令/脚本/日志入口）
- `Plan.md`：Validation Plan（复现策略与失败判据）
- `Task.md`：每个关键任务写“验收方式/证据入口”
