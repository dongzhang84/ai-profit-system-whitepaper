#!/usr/bin/env python3
"""
生成封面图 · typography-dark 风格（黑底 + 第一行白 + 第二行橙）

用法：
    python3 scripts/cover.py <slug> "第一行文字" "第二行文字"

例：
    python3 scripts/cover.py three-claude-skills \
        "每个人都应该使用的" \
        "三个最有用的 Claude Skill"

输出：cover-image/<slug>/cover.png
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_INDEX = 2
W, H = 2400, 1350
BG = (0, 0, 0)
C1 = (245, 245, 245)
C2 = (242, 107, 44)


def render(slug, line1, line2):
    out = Path("cover-image") / slug / "cover.png"
    out.parent.mkdir(parents=True, exist_ok=True)

    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    max_w = int(W * 0.88)
    size = 100
    while size < 700:
        f = ImageFont.truetype(FONT_PATH, size, index=FONT_INDEX)
        if max(draw.textlength(line1, font=f), draw.textlength(line2, font=f)) >= max_w:
            break
        size += 10
    size -= 10
    font = ImageFont.truetype(FONT_PATH, size, index=FONT_INDEX)

    w1, w2 = draw.textlength(line1, font=font), draw.textlength(line2, font=font)
    b1 = draw.textbbox((0, 0), line1, font=font)
    b2 = draw.textbbox((0, 0), line2, font=font)
    h1, h2 = b1[3] - b1[1], b2[3] - b2[1]
    gap = int(size * 0.22)
    y = (H - (h1 + gap + h2)) // 2 - int(size * 0.05)
    x = (W - max(w1, w2)) // 2

    draw.text((x, y), line1, font=font, fill=C1)
    draw.text((x, y + h1 + gap), line2, font=font, fill=C2)

    img.save(out, "PNG", optimize=True)
    print(f"saved: {out}  ({out.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    render(sys.argv[1], sys.argv[2], sys.argv[3])
