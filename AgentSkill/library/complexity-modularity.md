# Complexity & Modularity（复杂度与模块化）检查表

适用：Software（重构/架构/实现细化）、以及任何需要“降低认知负担”的 Writing。

---

## 触发条件

- 代码开始“越改越乱”、改 A 影响 B、边界不清
- 出现大量 pass-through、重复接口、无意义拆分
- 需要做重构/模块拆分/抽象设计

---

## A. 复杂度信号（先识别）

症状检查：
- [ ] 修改一个点，需要理解很多无关细节
- [ ] 小改动引发连锁修改
- [ ] “为了兜底”引入大量分支/特判
- [ ] 接口看起来简单，但隐藏大量规则（信息泄漏）

来源：
- `Reference/A Philosophy of Software Design/A Philosophy of Software Design.md` — Ch.2 *The Nature of Complexity*（定义、症状、原因）

---

## B. 深模块（Deep Modules）而不是浅封装

检查项：
- [ ] 模块接口（Interface）尽量小、稳定
- [ ] 模块内部承担复杂度，不把复杂度泄漏给调用方
- [ ] 避免“类泛滥（classitis）”式的浅包装

来源：
- Ousterhout — Ch.4 *Modules Should Be Deep*（Deep vs Shallow、classitis）

---

## C. 信息隐藏（Information Hiding）与信息泄漏

检查项：
- [ ] 每个模块隐藏至少一个“会变化的细节”（否则它不配叫抽象）
- [ ] 如果同一知识点在多个模块出现 → 信息泄漏，必须收敛
- [ ] 避免按时间顺序拆分（temporal decomposition），优先按“变化原因”拆分

来源：
- Ousterhout — Ch.5 *Information Hiding (and Leakage)*（信息泄漏、时间分解）
- `Reference/Modern Software Engineering/Modern Software Engineering.md` — Part III, Ch.11 *Separation of Concerns*, Ch.12 *Information Hiding and Abstraction*
- SWEBOK v4.0a — Chapter 03 *Software Design*, §1.4 *Software Design Principles*

---

## D. 耦合/内聚与分层抽象

检查项：
- [ ] 高内聚：模块内职责围绕同一概念
- [ ] 低耦合：模块间依赖方向清晰、避免环
- [ ] 不同层用不同抽象（不要把底层细节透到上层）

来源：
- Farley — Part III, Ch.9 *Modularity*, Ch.10 *Cohesion*, Ch.13 *Managing Coupling*
- Ousterhout — Ch.7 *Different Layer, Different Abstraction*

---

## E. 错误设计：把错误“设计掉”

优先级：
1) 设计 API 让错误不可能发生
2) 错误发生时可诊断（明确错误信息）
3) 兜底不掩盖错误（默认不写兜底；确需兜底必须在 Plan 中预先约定触发条件与成本，并明确对验收的影响）

来源：
- Ousterhout — Ch.10 *Define Errors Out Of Existence*

---

## F. 注释作为设计工具（不是事后补丁）

检查项：
- [ ] 先写接口文档/高层注释，再写实现（用注释暴露设计缺陷）
- [ ] 注释写“为什么”和“抽象边界”，不重复代码

来源：
- Ousterhout — Ch.15 *Write The Comments First*, Ch.13 *Comments Should Describe Things that Aren’t Obvious*
