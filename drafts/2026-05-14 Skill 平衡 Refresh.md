# Skill 写肥 / 写瘦 · 两个翻车 case

**日期** · 2026-05-14 (周四★) | **支柱** · A · Claude Code

---

## 核心论点

之前讲过 Skill 长度平衡点。今天给你 2 个具体翻车案例 + 教训。

## 钩子候选

- 之前讲过 Skill 的长度平衡。今天给你看两个翻车的真实案例。
- 我讲过 Skill 不要肥不要瘦。但理论不如翻车。

## 主干

- **Case 1 · 写肥翻车**：/write-article 初版 800 行，全是 if/else 规则
  - 症状：模型"过度遵从"，丢掉 LLM 本身的判断力
  - 修复：拆成 "intent（正向）+ examples（2 个完整样例）+ constraints（3-5 条硬约束）"
- **Case 2 · 写瘦翻车**：/traffic-review 初版 60 行
  - 症状：模型每次问我要 metric 阈值、要 report 格式、要 audience，把 skill 变成 clarification loop
  - 修复：补 2 个 example + 3 条 default value

## 结论候选

- 在例子上学 Skill 的长度，不要在规则上学。

## 长文公式

A

## 待补素材

- 2 个 case 的前后版本 diff
- 呼应 04-23 的原版帖
