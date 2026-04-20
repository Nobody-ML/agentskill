# Documentation & Writing（文档/教程/论文）检查表

适用：Writing Track，或任何需要对外解释/复盘的交付物。

---

## 触发条件

- 交付物主要是文本（教程/文档/论文/报告）
- 需要“图文并茂”、受众明确、风格贴合
- 需要引用来源或复现说明

---

## A. 先对齐四件事（否则不要开写）

- [ ] 目标读者是谁（小白/工程师/审稿人/管理者）
- [ ] 语气与风格（口语/严谨/学术/工程说明）
- [ ] 长度目标（精简/标准/超详细）
- [ ] 必须包含的图示类型与数量（至少 1 张总览图）

---

## B. 结构优先：先给读者“地图”

检查项：
- [ ] 开头交代：要解决什么、为什么重要、读完能做什么
- [ ] 早期给总览图（系统/流程/概念图）
- [ ] 章节按读者路径组织（先能跑通/理解，再深入）

来源：
- `Reference/Head First Software Architecture/Head First Software Architecture.md` — Intro/Chapter 1（强调“why”和架构思维路径）

---

## C. 图示要求（允许混用，但必须有图注）

- Mermaid：流程、状态机、组件关系
- PlantUML：类图/时序图
- ASCII/表格：对比、参数表、异常/边界可读性

硬要求：
- [ ] 每张图都有图名 + 1 句话图注（解释它在回答什么问题）

---

## D. 来源与可追溯性

检查项：
- [ ] 关键事实/数据/结论必须能定位来源
- [ ] 把来源条目写入 `State.md` Evidence Index（结论 → 来源）
- [ ] 不确定内容必须标注“假设/待验证”

来源：
- `Reference/Software Engineering Body of Knowledge v4.0a/Software Engineering Body of Knowledge v4.0a.md` — Chapter 01 §4.1–4.3（不同规格写法与验收）

---

## E. “无 AI 味”检查

禁止项（出现即删）：
- 自述式口吻（“作为…我…”）
- 空泛鼓励/道歉
- 用形容词代替证据（“非常”“极其”“很强”但无测量）

替代写法：
- 用约束、证据、步骤说话：命令/截图/引用/实验记录

---

## F. 把文字当成设计工具

检查项：
- [ ] 先写高层说明/接口说明，再写细节（用文字暴露设计不清）
- [ ] 写“为什么”和“抽象边界”，不重复显而易见的内容

来源：
- `Reference/A Philosophy of Software Design/A Philosophy of Software Design.md` — Ch.12–13（为什么写注释；注释应描述非显然内容）
- Ousterhout — Ch.15（先写注释作为设计工具）
