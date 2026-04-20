# Repro Protocol（Research）模板

> 注意：本模板仅提供参考结构，不是执行规范；实际输出必须遵循本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md`。模板与规则冲突时，以规则为准。

> 目的：任何实验/算法验证结论都能被第三方复现。

---

## 1. 环境（Environment）

- OS：
- CPU：
- GPU：
- Driver/CUDA：
- Python/Compiler：
- 依赖（关键版本）：

---

## 2. 数据（Data）

- 数据集名称：
- 版本/下载链接：
- 许可/合规说明：
- 切分（train/val/test）：
- 预处理：

---

## 3. 实验配置（Config）

- 随机种子（seed）：
- 超参（lr/batch/epochs/...）：
- 训练设置（precision、梯度累计、并行）：
- 推理设置（beam、temperature、topk...）：

---

## 4. 指标与基线（Metrics & Baselines）

- 指标定义与计算脚本：
- 基线（baseline）列表与来源：
- 对照实验：
- 消融（ablation）计划：
- 失败判据（什么情况算失败）：

---

## 5. 复现入口（Reproduction Entry）

- 一键运行命令：
- 输出产物位置（日志/模型/图表）：
- 预期输出摘要（成功判据）：

---

## 6. Evidence Index 写入

把以下信息写入 `State.md` 的 Evidence Index：
- 运行命令
- 关键输出摘要
- 日志/产物路径
