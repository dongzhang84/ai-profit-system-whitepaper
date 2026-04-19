# Baoyu Diagram Design System (本地最小版)

本文件是 **项目本地版** 的 design-system 参考，不是 baoyu 原版。原 skill 的 references 没随 skill 分发下来，这份是从已有四张图（`diagram/huang-ai-five-layers/`、`diagram/chip-ban-three-channels/`、`diagram/us-five-layer-strategy/`、`diagram/china-three-pillar-strategy/`）反推并固化的设计语言。保持这套规则，新图和旧图视觉一致，文章里多图排版不突兀。

---

## 1. 画布

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="100%"
     viewBox="0 0 680 H"
     font-family="-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', 'Segoe UI', sans-serif">
```

- **宽度永远是 680**。H 按内容算（见第 3 节）。
- **外边距 x=60**，所以内容区 60-640，宽度 580。
- 没有 HTML 注释（`<!-- -->`），SVG 直出。

## 2. 必须内嵌的 `<style>`（逐字复制）

```xml
<style>
:root { --fg: #111827; --fg-muted: #6b7280; --fg-soft: #9ca3af; --bg: #ffffff; --layer-bg: #f9fafb; --layer-stroke: #e5e7eb; --divider: #e5e7eb; --accent: #fb7185; --accent-bg: #fff1f2; --accent-stroke: #fca5b1; }
@media (prefers-color-scheme: dark) { :root { --fg: #f3f4f6; --fg-muted: #9ca3af; --fg-soft: #6b7280; --bg: #0b0f17; --layer-bg: #1f2937; --layer-stroke: #374151; --divider: #374151; --accent: #fda4af; --accent-bg: #3f1d24; --accent-stroke: #9f1239; } }
.bg { fill: var(--bg); }
.layer { fill: var(--layer-bg); stroke: var(--layer-stroke); stroke-width: 1.2; }
.layer-key { fill: var(--accent-bg); stroke: var(--accent-stroke); stroke-width: 1.4; }
.title { font-size: 18px; font-weight: 600; fill: var(--fg); }
.subtitle { font-size: 12px; font-weight: 400; fill: var(--fg-muted); }
.t { font-size: 14px; font-weight: 400; fill: var(--fg); }
.th { font-size: 14px; font-weight: 600; fill: var(--fg); }
.ts { font-size: 12px; font-weight: 400; fill: var(--fg-muted); }
.eyebrow { font-size: 12px; font-weight: 500; fill: var(--fg-soft); letter-spacing: 0.08em; }
.eyebrow-accent { fill: var(--accent); }
.caption { font-size: 12px; font-weight: 400; fill: var(--fg-muted); }
.caption-strong { font-size: 14px; font-weight: 500; fill: var(--fg); }
.divider { stroke: var(--divider); stroke-width: 1; }
.divider-accent { stroke: var(--accent-stroke); stroke-width: 1; }
</style>
```

CSS 变量 + `@media (prefers-color-scheme: dark)` 做亮暗自动切换。必须用变量，不要硬编码 hex 到每个 `<text fill="...">`。

**转 PNG 注意**：rsvg-convert 不解析 CSS 变量，会全部渲染成黑色。用 `scripts/svg-to-png.py`，它在转换前把变量替换成亮色 hex。不要绕过这个脚本。

## 3. 高度 H 的算法

```
H = 标题区(80) + N×容器高 + (N-1)×间距 + 尾注区(~80)
```

- 标题区：title y=42，subtitle y=64。第一个容器起点 y=96。
- 容器高：2 行正文 → 100；3 行正文 → 125。
- 容器间距：12–16。
- 尾注区：caption-strong 在第一行（容器底部 + 32），caption 再 +22。

常用组合：
- 3 容器 × 125 高 × 16 间距 + 尾注 → H=580（chip-ban, china-three-pillar）
- 5 容器 × 100 高 × 12 间距 + 尾注 → H=720（us-five-layer-strategy）
- 5 容器 × 96 高 × 10 间距 + 尾注 → H=700（huang-five-layers）

底部留 20 px buffer，不要贴边。

## 4. 容器内部布局（左窄右宽）

```
x=60 ────────┬─────── x=640
             │
 左栏        │  右栏
 eyebrow     │
 th          │  body line 1
 ts          │  body line 2
             │  body line 3
             │
  x=82     x=220   x=238
```

- 左栏 60–220：放 eyebrow（+22）、th（+50 或 +54）、ts（+70 或 +74）
- 中间：`<line class="divider" x1="220" y1="+14" x2="220" y2="-18">`（+14 到容器底 -18）
- 右栏 238–640：body 正文，行高 22，和 th/ts 同 y 对齐

### 右上角 accent 标签（punchy takeaway）

```xml
<text class="eyebrow eyebrow-accent" x="618" y="y_top+22" text-anchor="end">→ 数字或口号</text>
```

- 用来放每行最刺眼的那个数据或动作（"→ 14 亿用户"、"→ 估算 10 亿美元 / 年"、"→ 开门卖 · 留住开发者"）。
- Latin 箭头 `→`（U+2192）开头统一格式。
- 长度 ≤ 10 CJK 字（约 130 px），确保不跨过一半画布。

## 5. 颜色使用

**≤ 2 个 accent ramp**。本模板里 accent 只有一个 coral (`#fb7185`)，搭配 accent-bg / accent-stroke。

accent 的合法用法（只在这些场合出现）：
1. 一个容器的 `class="layer-key"`（用 `layer-bg=#fff1f2`，突出"最关键的一行"）。整图最多 1 个。
2. 该容器里的 `eyebrow-accent` 文本
3. 所有容器的右上角 punchy 标签（每行一个，意思是"这里有个刺眼数字"）
4. `divider-accent` 分隔线（跟 layer-key 搭配用）

**不要做的事**：
- 不要每个容器一种颜色
- 不要用 accent 色做 title / subtitle
- 不要在同一张图里同时用 coral + teal + amber 多套 ramp

## 6. 正文字符长度预算

- 14px 字体，CJK 约 14 px/字，Latin 约 7–8 px/字
- 右栏宽度 402 px（238→640）
- CJK 约 28 字上限；混合中英约 24–26 字
- 超出就换行或换更短的表达，不要让文字贴边或溢出

## 7. 行高和间距

- 正文 body 行高 22 px（y 间隔 22）
- eyebrow 到 th：28 px
- th 到 ts：20 px
- 容器内底部 padding：15–18 px
- 容器间距：12–16 px
- 尾注离容器底 32 px；两行尾注间距 22 px

## 8. 预保存检查

每张图提交前过一遍：

1. viewBox H 覆盖最后一行 + 20 px buffer
2. 没有 rect / line / text 跨过 x=640
3. 每个 `<text>` 都带 class，没有硬编码 fill
4. 没有 `text-anchor="end"` 在 x < 200 的位置（会截到画布外）
5. CSS 变量完整，`@media dark` 还在
6. 最多 1 个 `layer-key` 容器
7. 没有 `<!-- comments -->`
8. 跑一遍 `python3 scripts/svg-to-png.py diagram/.../diagram.svg`，Read 生成的 PNG 目视检查，不是黑的

---

## 附：已有图的对照

| 图 | 容器数 | 容器高 | 间距 | accent 用法 | viewBox |
|---|---|---|---|---|---|
| huang-ai-five-layers | 5 | 96 | 10 | layer-top + eyebrow-accent（顶层） | 680×700 |
| chip-ban-three-channels | 3 | 125 | 16 | 右上角标签 | 680×580 |
| us-five-layer-strategy | 5 | 100 | 12 | layer-key + eyebrow-accent + divider-accent（中层） | 680×720 |
| china-three-pillar-strategy | 3 | 125 | 16 | 右上角标签 | 680×580 |

新图先对照这四张，挑最接近的模板改，不要从零发明布局。
