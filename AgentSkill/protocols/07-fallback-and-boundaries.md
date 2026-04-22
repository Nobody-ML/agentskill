# 07-fallback-and-boundaries：边界、兜底、降级协议

适用范围：
- Track：Research / Software / Writing
- Level：L2 / L3（强制）

目标：
把“禁止擅自兜底/禁止擅自降级”写成可执行门禁，避免执行期偷偷改变验收、偷偷加入兜底逻辑导致用户结果不可信。

相关门禁：
- `protocols/00-hard-gates.md`：G1（Plan Mode）/ G4（Plan Quality）/ G7（Real Data）/ G9（Drift Recovery）

---

## 1) 默认策略（No fallback by default）

默认策略：
- **不兜底、不降级**，严格按 Plan/Acceptance/Spec 执行。
- 所有兜底/降级必须在 Plan 阶段写入并获得确认，记录在：
  - Plan.md 的 Fallback Policy / Fallback Register
  - 或单独文件：`FallbackRegister.md`（可用模板 `templates/FallbackRegister.template.md`）

---

## 2) 禁止行为（执行期硬禁）

执行阶段（Execute/Write/Validate）禁止：
- 为了“让它跑起来”临时加入兜底逻辑掩盖错误
- 为了“看起来完成”静默降低验收标准或删减需求
- 未经确认把困难点改成“后续再说”
- 未经确认用 synthetic 替代真实数据得出通过结论

一旦发生上述任一行为：
- 视为漂移（Drift），必须按 `protocols/05-resumption-and-anti-drift.md` 停线修复

---

## 3) 允许的 fallback 条件（必须计划内）

只有在 Plan 阶段完成以下登记并获得确认，才允许执行 fallback：
- 触发条件（什么情况下启用）
- fallback 行为（具体做什么）
- 代价与副作用（性能/质量/可维护性/安全）
- 对验收标准的影响（是否会改变 AC；改变则必须更新 Acceptance Contract）
- 验证方法（如何证明 fallback 生效且不破坏关键性质）
- 回滚策略（如何撤销 fallback）

---

## 4) 执行阶段遇到不可实现项（必须停下报告）

当执行阶段遇到“无法实现/依赖缺失/环境不满足/数据不可得”等：
1) 立即停下，不得自行改成兜底或降级
2) 报告阻塞点（Blockers）：
   - 卡在哪里
   - 需要什么最小输入（依赖/权限/数据/确认）
   - 当前 Plan/Task 哪一条受影响
3) 回到 Plan Mode：
   - 讨论并落盘可行修复路径（补依赖 / 调整方案 / 明确 fallback）
   - 更新 Plan/Task/Acceptance/Matrix
4) 重新走门禁后再继续执行

---

## 5) 简单任务例外（L0/L1）

L0/L1 的一次性小任务允许做必要的“防崩溃保护”，但仍需遵守：
- 不得偷换用户核心需求
- 不得隐性改变输出契约
- 有影响就必须说明（影响范围与风险）

