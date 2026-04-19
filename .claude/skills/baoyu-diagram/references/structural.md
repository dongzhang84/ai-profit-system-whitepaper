# Structural Diagrams

本项目只用两套结构模板，都是垂直堆叠的 sibling 容器。新图先套模板，不要从零发明。

---

## 模板 A：三支柱（sibling containers）

用于：三个并列的概念 / 策略 / 通道，每个都有独立内容。

**参考图**：
- `diagram/chip-ban-three-channels/diagram.svg` — 三条封锁不住的通道
- `diagram/china-three-pillar-strategy/diagram.svg` — 中国的三支柱策略

**骨架**：

```
viewBox 0 0 680 580

y=42  title
y=64  subtitle

Container 1: y=96,  h=125  (bottom=221)
Container 2: y=237, h=125  (bottom=362)
Container 3: y=378, h=125  (bottom=503)

Footer: caption-strong y=535, caption y=557
```

**容器内布局**（左栏 label，右栏 body）：

```
eyebrow       x=82  y=y_top+22
right-tag     x=618 y=y_top+22  text-anchor=end  class="eyebrow eyebrow-accent"
th            x=82  y=y_top+54
ts            x=82  y=y_top+74
divider       x=220 y1=y_top+14 y2=y_top+110
body line 1   x=238 y=y_top+54
body line 2   x=238 y=y_top+76
body line 3   x=238 y=y_top+98
```

三个容器都用 `class="layer"`（neutral gray）。accent 只出现在每个容器右上角的 punchy 标签。不要把其中一个容器做成 `layer-key`（会打破"三者平级"的语义）。

---

## 模板 B：五层蛋糕（stacked layers）

用于：一个分层框架（能源 / 芯片 / 基础设施 / 模型 / 应用），每层是独立的一层，可能其中一层特别重要。

**参考图**：
- `diagram/huang-ai-five-layers/diagram.svg` — 黄仁勋的五层蛋糕
- `diagram/us-five-layer-strategy/diagram.svg` — 美国五层战略

**骨架**（viewBox H 根据容器高度变化）：

```
viewBox 0 0 680 H

y=42  title
y=64  subtitle

Layer 5 (top):    y=96       h=100 or 96
Layer 4:          y=+112     h=100 or 96
Layer 3:          y=+112     h=100 or 96  ← 如果要 highlight，用 layer-key
Layer 2:          y=+112     h=100 or 96
Layer 1 (bottom): y=+112     h=100 or 96

Footer: caption-strong, caption
```

**允许的 highlight**：整图最多 1 个 `layer-key` 容器（accent bg + stroke）。约定：
- huang 模板里 highlight 的是"最重要的一层"（顶层 = 应用）
- us-strategy 模板里 highlight 的是"最关键但被搞砸的一层"（第 3 层 = CUDA）

右上角 punchy 标签每层都可以有，内容是该层的一句话战略口号。

---

## 选型

| 内容形状 | 用哪个模板 |
|---|---|
| 三个并列概念 / 原因 / 通道 / 策略 | 模板 A |
| 一个分层系统（能源 → 应用 这种） | 模板 B |
| 两个对比的 subsystem | 暂无模板，按 baoyu 原 SKILL.md 的 "Structural subsystem" 画（但 references 没给，需要现推） |

---

## 其他类型

flowchart / sequence / illustrative / class 这四种目前本项目没画过。真要画时先读 SKILL.md 里对应的类型描述，然后从 `design-system.md` 的第 1–2 节（画布 + style）起手，layout math 自己推。
