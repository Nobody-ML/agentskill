# Requirements & Acceptance（需求与验收）检查表

适用：Software / Writing / Research（任何需要“可验收”的交付物）

---

## 触发条件（何时必须查这份清单）

- 需求/范围含糊（例如“优化一下”“做个架构”“写篇教程”）
- 交付物需要被第三方验收（团队/用户/审稿人/上级）
- Level ≥ L2（尤其 L3）

---

## A. 需求分类（先分清再讨论）

1) 写清需求类别：
   - 功能（Functional）
   - 非功能（Nonfunctional）：性能/可靠性/安全/可维护性/可复现性等
   - 技术约束（Technology Constraints）

来源：
- `Reference/Software Engineering Body of Knowledge v4.0a/Software Engineering Body of Knowledge v4.0a.md` — Chapter 01 *Software Requirements*, §1.4–1.7（Functional / Nonfunctional / Technology constraints）

2) 对每个非功能需求给出“度量或可观察证据”：
   - 性能：延迟/吞吐/资源上限
   - 可靠性：失败率/降级策略（降级必须显式设计并经用户确认，不能在执行阶段擅自降级来“假装满足需求”）
   - 安全：威胁模型范围、禁止项

来源：
- SWEBOK v4.0a — Chapter 01 *Software Requirements*, §1.5（Nonfunctional requirements）、§3.2（Economics of QoS constraints）

---

## B. 验收标准（Acceptance Criteria）

硬要求：每条验收标准必须满足“可测试/可观察/可复现”。

1) 最少 2 条验收标准：
   - 形如“当……时，系统……，证据是……（命令/截图/实验记录/引用）”。

2) 不允许的验收描述（必须改写）：
   - “更好/更优/更快/更稳定”（无测量与证据）
   - “差不多/看起来可以”（无可复查结果）

来源：
- SWEBOK v4.0a — Chapter 01 *Software Requirements*, §4.3 *Acceptance Criteria-Based Requirements Specification*

---

## C. 验收契约（Acceptance Contract，L3 强制）

当任务达到 L3 或者存在高风险：把验收标准升级为“验收契约”，用可追踪 ID 管理。

### 结构（建议）

- `AC-XXX`：一句话标题
  - 行为描述（可测试断言）
  - 证据要求（必须提供的证据类型）
  - 失败判据（什么算失败）

### 最小规则

- 每条契约都必须能映射到 Task 中的至少一个任务
- Task 完成后必须能给出该契约的证据入口（写入 State.md Evidence Index）

来源（为什么要这样做）：
- SWEBOK v4.0a — Chapter 01 *Software Requirements*, §4.3（验收标准驱动规格）
- `Reference/Modern Software Engineering/Modern Software Engineering.md` — Part II *Optimize for Learning*, Ch.5 *Feedback*（把反馈与验证做早、做小）

---

## D. 冲突与范围控制

1) 识别冲突：当需求之间互相挤压（例如“更快”与“更省成本”）时，必须写出取舍原则。
2) 对范围做显式边界：写 Non-goals，防止任务漂移。

来源：
- SWEBOK v4.0a — Chapter 01 *Software Requirements*, §3.4 *Addressing Conflict in Requirements*
- `Reference/Modern Software Engineering/Modern Software Engineering.md` — Ch.4 *Working Iteratively*（迭代降低计划幻觉）

---

## E. 需求 → Task 的可追踪性

最小规则：
- Task 中每条实现类任务都要写明“验证哪个验收标准/契约（AC-XXX）”。
- 任何新增需求都要：更新 Plan（验收契约）→ 更新 Task（引用 AC-XXX）→ 再进入 Execute。

来源：
- SWEBOK v4.0a — Chapter 01 *Software Requirements*, §4.6 *Incremental and Comprehensive Requirements Specification*
