# 06-delivery-and-review：交付与评审协议

适用范围：
- Track：Research / Software / Writing
- Level：L2 / L3（强制）

目标：
交付必须可复查：做了什么、改了什么、怎么验证、证据在哪里、结论是否通过、剩余风险是什么。评审必须可执行：打分与整改清单绑定证据门禁。

相关门禁：
- `protocols/00-hard-gates.md`：G8（Evidence）
- `stages/review/SKILL.md`：评分与返工规则

---

## 1) 交付物必须包含哪些信息

交付回执必须包含：
- What was done：本次完成的目标与范围
- Files changed：改动文件清单（路径）
- Acceptance results：每条 AC 的结论（pass/fail/blocked/partial/missing）
- Validation summary：数据类型 + 命令 + 关键证据入口
- Review score：按维度打分（含过程合规）
- Residual risks：剩余风险与后续建议
- Limits：已知限制与不支持范围

模板参考：
- `templates/DeliveryReport.template.md`

---

## 2) 评审与返工规则（硬门禁）

评审必须：
- 绑定证据（没有证据则不能给通过结论）
- 给出整改清单（可执行、可验证）
- 明确是否通过（PASS / NEEDS_REWORK / BLOCKED）

返工触发（至少）：
- 验证不通过或证据缺失
- 真实数据门禁违规
- 执行期擅自兜底/降级
- 过程合规不通过（越权执行/偏离 Plan/Task 等）

---

## 3) 反馈闭环（Plan→Execute→Validate→Review→Plan）

用户反馈“不满意/新想法/发现偏离”时：
1) 回到 Plan Mode
2) 走 Change Control（记录变化与影响）
3) 更新 Plan/Task/Acceptance/Matrix
4) 重新请求授权（如涉及执行）

模板参考：
- `templates/ChangeControl.template.md`

