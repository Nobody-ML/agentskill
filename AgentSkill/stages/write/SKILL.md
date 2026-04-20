---
name: write
description: 写作交付：先对齐受众与结构，再逐段写作并补图示与引用；最后做一致性与可运行性验证
---

# Write（写作）

## 进入条件

- Simple/L1：Router 判定可直接写作
- Level ≥ L2：Plan/Task 就绪，且用户已明确授权执行（Execution Authorization = received；为避免误判，用户需单独回复口令：`开始执行`）

---

## Stage Contract（阶段契约）

### 输入（Inputs）
- `Plan.md`（受众/风格/结构/图示要求/验收）
- `State.md`（来源条目、术语表、边界与风险）
- （如有）Acceptance Contract（AC-XXX）与对应验收标准
- Execution Authorization（Level≥L2 时必须已 received）

### 输出（Outputs）
- 文档正文 + 图示 + 引用清单
- 可运行示例（如文档包含命令/代码）

### 工件更新（Artifacts Updated）
- `State.md`：来源条目、图示清单、示例可运行证据

### 退出条件（Exit Criteria）
- 文档达到 Plan 的验收标准，并通过 Validate（引用/一致性/示例可运行）

### 返回用户条件（Return to User）
- 受众/语气/长度/必须图示要求不明确，会导致文档重写
- Level≥L2 且未授权执行（未收到用户单独回复 `开始执行`）

---

## library 索引（按触发条件查）

- 写作结构/图示/引用/无AI味：`library/documentation-writing.md`
- 复现协议（含可运行示例）：`library/reproducibility.md`
- 验收标准：`library/requirements-acceptance.md`

---

## 论文/技术报告写作（加强）

当交付物是论文/技术报告：
- 使用结构模板：`templates/Paper-Outline.template.md`
- 使用相关工作矩阵：`templates/Literature-Review-Matrix.template.md`
- 强制复现章节（Research）：`templates/ReproProtocol-Research.template.md`

门禁：
- 没有来源映射，不写确定性结论（必须标注假设/待验证）。

---

## 输出（必须产出）

（Level≥L2 强制）每轮对外回复开头必须带：

```text
【Mode】Write | Level=<L?> | ExecutionAuth=received
```

- 文档正文（按用户要求的长度与风格）
- 图示（按需：Mermaid/PlantUML/ASCII/表格）
- 来源与引用清单（需要引用时必有）
- State.md：图示清单、来源条目、示例可运行证据

---

## 写作原则（无“AI味”约束）

- 不写自述（不写“我作为…/我不能…/抱歉…”这类口吻）
- 用事实与约束驱动表达：结论必须能追溯到来源/实验/代码
- 句子短、结构清楚：段落只讲一个点
- 先结构后段落：先写目录与要点，再填充正文

---

## 工作步骤

### Step 1：对齐受众与风格

最少确认四件事：
- 目标读者（小白/工程师/审稿人/管理者）
- 语气（口语/严谨/学术/工程说明）
- 长度目标（精简/标准/超详细）
- 图示密度（至少 1 张总览图；其余按需要）

### Step 2：搭结构（Outline）

结构必须体现“读者路径”：
- 先让读者知道要解决什么
- 再给整体地图（总览图）
- 再分段讲步骤/概念/实现

### Step 3：逐段写作（短闭环）

每段都回答：
- 这段解决什么问题？
- 读者要做什么/理解什么？
- 是否需要例子或图？

### Step 4：补图示（按场景选工具）

选型建议：
- Mermaid：流程、系统关系、路由与状态机
- PlantUML：类图/时序图（当读者关心对象关系或交互）
- ASCII/表格：对比、清单、参数表

图示要求：
- 图必须服务于理解关键关系，不做装饰
- 每张图必须有图名与一句话说明用途

### Step 5：引用与来源（需要时强制）

- 关键事实/数据/主张：必须能定位来源
- 把来源条目与“对应结论”写进 State.md（Evidence Index）

### Step 6：写作验证（进入 Validate）

- 引用可追溯
- 术语一致
- 示例可运行（如有代码/命令）
- 图示可读（图注完整）

---

## 论文/学术写作（可选扩展）

当用户目标是论文/报告：
- 强制包含：问题定义、相关工作、方法、实验设置、结果、消融、局限性、复现附录
- 所有实验必须能复现（环境/seed/数据版本/脚本）
