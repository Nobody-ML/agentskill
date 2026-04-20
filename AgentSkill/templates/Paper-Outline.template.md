# Paper Outline（论文结构）模板

> 注意：本模板仅提供参考结构，不是执行规范；实际输出必须遵循本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md`。模板与规则冲突时，以规则为准。
>
> 用途：把论文写作变成可执行的 Task（先结构后填充、先证据后结论）。
>
> 启用建议：Research + Writing（论文/技术报告）。

---

## 0. 元信息

- 题目（暂定）：
- 目标会议/期刊（如有）：
- 贡献点（一句话）：

---

## 1. Abstract（摘要）

- 问题：
- 方法：
- 结果：
- 意义：

---

## 2. Introduction（引言）

- 背景与痛点：
- 研究问题（Research Question）：
- 主要贡献（Contributions，3–5 条）：
- 结果预览（可量化）：

---

## 3. Related Work（相关工作）

> 维护 `Literature Review Matrix`，并在这里组织叙事逻辑（按问题/方法/评测维度分组）。

- 相关工作分组与差异点：

---

## 4. Method（方法）

- 总体框架图（建议 Mermaid/PlantUML）：
- 关键设计选择与取舍（引用 ADR/Decision Log）：
- 算法/模型细节（必要时）：

---

## 5. Experimental Setup（实验设置）

- 数据集与许可：
- 预处理：
- 指标定义：
- 基线与实现来源：
- 训练/推理设置（seed/超参）：

---

## 6. Results（结果）

- 主结果表：
- 关键对比与解释：
- 失败案例/误差分析（如需要）：

---

## 7. Ablations（消融）

- 消融列表（验证哪些假设）：
- 结论：

---

## 8. Limitations & Risks（局限与风险）

- 局限：
- 风险（合规/可误用）：

---

## 9. Reproducibility（复现）

> 绑定 `ReproProtocol-Research.template.md`，并把证据入口写入 State.md Evidence Index。

- 一键复现命令：
- 产物与日志结构：

---

## 10. References（参考文献）

- 引用条目清单（最少）：
