# Cover Image Preferences

## Default preset: typography-dark

When no explicit dimensions are specified, use this preset:

- **Type**: typography
- **Palette**: custom (black + two-color text)
- **Rendering**: flat-vector
- **Text**: title-only, split into 2 lines
- **Mood**: bold
- **Font**: clean (Hiragino Sans GB W6 or comparable)
- **Aspect**: 16:9

### Color scheme

- Background: `#000000` (pure black)
- Line 1 (setup / lead-in): `#F5F5F5` (off-white)
- Line 2 (payload / main claim): `#F26B2C` (orange)

The second line should carry the main claim of the title so the orange draws the eye to the key message.

### Layout

- Center-aligned horizontally, centered vertically
- 88% max text width of canvas
- Line gap: 22% of font size
- Auto-size font so the longer line fills the target width

## Render path

Instead of calling an AI image backend, use the local typography renderer:

```bash
python3 scripts/cover-typography-dark.py \
    --out cover-image/<slug>/cover.png \
    --line1 "<first line>" \
    --line2 "<second line>"
```

The script accepts `--color1 / --color2 / --bg / --width / --aspect` for overrides.

## When to deviate from this preset

Only deviate when the user explicitly requests:
- Non-dark palette (e.g., "做一个亮色版")
- Non-typography type (e.g., "要有插图")
- Different aspect (e.g., "方图给小红书")

Otherwise default to this preset without asking.

## Reference articles using this preset

- `每个人都应该使用的三个最有用的 Claude Skill` → `cover-image/three-claude-skills/cover.png`
