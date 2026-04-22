---
name: research
description: 资料检索与证据管理：把“听说/印象/猜测”变成可追溯来源与可复现证据，供 Plan/Write/Execute 使用
---

# Research（资料检索与证据）

## 进入条件

满足任一：
- 需要论文/标准/官方文档支持关键结论
- 需要对比“最新进展/最佳实践/主流基线”
- 需要把模糊方向缩小到可验证问题
- 写作任务要求引用与出处

---

## Stage Contract（阶段契约）

### 输入（Inputs）
- Router 的路由结果（Track/Level/风险）
- 已知问题陈述/约束/材料（State.md）

### 输出（Outputs）
- Source List（来源清单）
- Research Brief（结构化摘要）
- Evidence Index 更新（结论 → 来源/证据入口）

### 工件更新（Artifacts Updated）
- `State.md`：Evidence Index（来源条目、关键结论映射）
- `Plan.md`：把 Research Brief 作为“方案依据”（下一阶段引用）

### 退出条件（Exit Criteria）
- 有足够证据支撑 Plan 的关键决策与验收/验证设计

### 返回用户条件（Return to User）
- 外部资料需要账号/付费/授权
- 用户禁止联网但又要求“最新”结论

---

## 必读协议（L2/L3 强制加载）

- 深读与调研协议：`protocols/02-deep-reading-and-research.md`
- 门禁状态机：`protocols/00-hard-gates.md`（G2/G3）

---

## 说明：Research 属于 Plan Mode（不进入执行）

在未收到用户单独回复 `开始执行` 前：
- 允许：读材料、联网检索、更新 `State.md`（Evidence Index）、把 Research Brief 写入 Plan，要非常深入地研究
- 禁止：修改任何交付物（代码/脚本/配置/文档/实验产物）、运行不可逆/破坏性操作

## library 索引（按触发条件查）

- 调研与证据标准（来源质量/Impact/证据链）：`library/research-and-evidence-standard.md`
- 迭代/反馈/经验主义：`library/iteration-feedback.md`
- 复现协议（实验记录要求）：`library/reproducibility.md`
- 风险/合规：`library/risk-security.md`

---

## 论文/综述写作触发（Research → Writing 的桥）

当用户目标包含“论文/报告/综述”：
- 先维护相关工作矩阵：`templates/Literature-Review-Matrix.template.md`
- 再写论文结构：`templates/Paper-Outline.template.md`

门禁：关键主张必须能映射到来源条目（写入 State.md Evidence Index）。

---

## 输出（必须产出）

（Level≥L2 建议强制）每轮对外回复开头必须带：

```text
【Mode】Research | Level=<L?> | ExecutionAuth=<required/not_required>
```

1) **来源清单（Source List）**：至少 5 条（复杂任务更多）
2) **Research Brief**：可直接写入 Plan 的要点
3) **证据索引更新**：把来源与关键结论写入 `State.md` 的 Evidence Index
4) （可选）**Research Log 文件**：当来源很多或需要长期维护时，使用 `templates/ResearchLog.template.md` 单独落盘，并在 Plan/State 中引用入口

（L3 默认强制）
- 来源 ≥ 8，且至少包含：≥ 3 条一手资料（官方/标准/论文/源码）+ ≥ 1 条源码/issue 证据
- 必须记录版本/日期与许可证风险点（当涉及第三方库/工具/格式内核）
- 详细规则以 `protocols/02-deep-reading-and-research.md` 为准

落盘的“可追溯”最低标准（避免写成名词堆）：
- 每条来源必须可定位：给出 URL/DOI/arXiv/官方文档入口/仓库 issue 链接等
- 禁止只写“某某 docs / 某某 GitHub”：必须能点开验证

---

## 来源优先级（先看什么）

从高到低：
1) 用户提供材料（论文/代码/数据/内部文档）
2) 项目内文档与源码（真实行为与约束）
3) 官方文档/标准（RFC、IEEE/ACM、厂商文档）
4) 同行评审论文/权威教材
5) 可靠工程博客/会议演讲（需交叉验证）

禁止：把无来源的结论当成事实写进 Plan/论文/教程。

---

## 工作步骤

### Step 1：明确检索目标

把目标写成 1–3 条可检索的问题，例如：
- “2024–2026 年在 <方向> 的主流方法与评测基准是什么？”
- “<库/框架> 在 <场景> 的推荐用法与反模式是什么？”

### Step 2：关键词扩展（Query Expansion）

输出一个关键词表：
- 核心词（2–5 个）
- 同义词/缩写
- 关键指标/数据集/会议
- 反向词（用于排除无关方向）

### Step 3：筛选与快速阅读

对每个来源记录：
- 题目/作者/年份/链接
- 可信度理由（为什么选它）
- 与任务的关联点（1–3 条）
- 可复用的关键结论（必须能定位出处）

### Step 4：写 Research Brief（结构化摘要）

模板：
- **现状**：主流做法/共识
- **缺口**：已知痛点/未解决问题
- **可落地方向**：2–3 条候选路线
- **验证建议**：指标/基线/最小实验
- **风险**：合规/算力/数据依赖

### Step 5：更新 State.md（证据落盘）

至少写入：
- 来源清单
- 每条关键结论对应的来源
- 后续验证要用的实验/命令/脚本入口（如果已知）

---

## 研究/算法的复现要素检查表（建议直接贴到 Plan）

- 环境：OS/CPU/GPU/驱动/依赖版本
- 数据：数据集版本、切分、预处理、许可
- 训练/推理：seed、超参、训练步数、batch、precision
- 指标：计算方法、置信区间（如需要）
- 基线：选择理由、实现来源
- 消融：要验证哪些关键假设
- 失败判据：什么情况下结论不成立

---

## 何时必须返回用户

- 外部资料需要授权/付费/账号
- 任务对“最新”要求严格，但用户不允许联网检索
- 关键材料缺失（代码/数据/论文链接）导致无法继续
