from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path(__file__).parent / "cover.png"

W, H = 2400, 1350
BG = (0, 0, 0)
COLOR_LINE1 = (245, 245, 245)
COLOR_LINE2 = (242, 107, 44)

FONT_PATH = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_INDEX = 2

LINES = [
    ("每个人都应该使用的", COLOR_LINE1),
    ("三个最有用的 Claude Skill", COLOR_LINE2),
]

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

max_text_width = int(W * 0.88)
size = 100
while size < 700:
    font_trial = ImageFont.truetype(FONT_PATH, size, index=FONT_INDEX)
    widest = max(draw.textlength(t, font=font_trial) for t, _ in LINES)
    if widest >= max_text_width:
        break
    size += 10
size -= 10
font = ImageFont.truetype(FONT_PATH, size, index=FONT_INDEX)

widths = [draw.textlength(t, font=font) for t, _ in LINES]
heights = [draw.textbbox((0, 0), t, font=font)[3] - draw.textbbox((0, 0), t, font=font)[1] for t, _ in LINES]

line_gap = int(size * 0.22)
block_h = sum(heights) + line_gap
y_start = (H - block_h) // 2 - int(size * 0.05)

block_w = max(widths)
x_start = (W - block_w) // 2

y = y_start
for (text, color), w, h in zip(LINES, widths, heights):
    draw.text((x_start, y), text, font=font, fill=color)
    y += h + line_gap

img.save(OUT, "PNG", optimize=True)
print(f"saved: {OUT}")
print(f"font size: {size} (W6 no stroke)")
print(f"size: {OUT.stat().st_size / 1024:.1f} KB")
