# Design & Construction（设计与构建）检查表

适用：Software Track（实现/重构/脚本/架构落地）。

---

## 触发条件

- 进入 Execute 之前想降低实现返工成本
- 需要从架构/方案落到具体模块、接口、数据流
- 重构或新增模块，担心复杂度蔓延

---

## A. 设计（Design）：先把边界与抽象说清楚

检查项：
- [ ] 模块边界明确（谁负责什么，谁不负责什么）
- [ ] 依赖方向明确（上层依赖抽象，不反向依赖实现细节）
- [ ] 关键接口（输入/输出/错误）写清楚（最少是文字 + 示例）
- [ ] 把“会变的细节”藏起来（信息隐藏），避免在多处重复出现同一规则

来源：
- `Reference/Software Engineering Body of Knowledge v4.0a/Software Engineering Body of Knowledge v4.0a.md` — Chapter 03 *Software Design*, §1.4 *Software Design Principles*
- `Reference/A Philosophy of Software Design/A Philosophy of Software Design.md` — Ch.4/5/7（deep modules / information hiding / different layer different abstraction）

---

## B. 构建（Construction）：把复杂度压下去，而不是扩散

检查项：
- [ ] 优先最小可验证实现（不要先搭大框架）
- [ ] 避免“浅封装”：一层包装只转发、不隐藏复杂度 → 通常是坏信号
- [ ] 错误设计：优先让错误不可能发生；其次让错误可诊断；兜底只允许按 Plan 明确策略且不掩盖错误
- [ ] 注释/文档作为设计工具：先写接口/高层说明，再写实现

来源：
- SWEBOK v4.0a — Chapter 04 *Software Construction*, §1.1 *Minimizing Complexity*, §1.2 *Anticipating and Embracing Change*
- Ousterhout — Ch.10/13/15（错误设计、注释作为设计工具）

---

## C. 任务拆分：把“设计”变成可执行 Task

检查项：
- [ ] 每个 Task 都能独立验收（产出物 + 验收方式）
- [ ] 复杂改动先钉边界：先写测试/最小验证，再实现
- [ ] 每次改动后立刻进入 Validate 写证据入口

来源：
- `Reference/Modern Software Engineering/Modern Software Engineering.md` — Ch.5 *Feedback*（prefer early feedback）
- `superpowers/skills/writing-plans/SKILL.md`（小步任务粒度）
