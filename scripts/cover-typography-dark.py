#!/usr/bin/env python3
"""
Cover image generator: typography-dark preset
Black background, two-line Chinese title with per-line color (default white + orange).
Used for snowboat-blog article covers.

Usage:
  python3 scripts/cover-typography-dark.py \
      --out cover-image/<slug>/cover.png \
      --line1 "每个人都应该使用的" \
      --line2 "三个最有用的 Claude Skill"

Optional:
  --color1 FFFFFF      hex for line 1 (default white)
  --color2 F26B2C      hex for line 2 (default orange)
  --bg 000000          hex for background (default black)
  --width 2400         canvas width (default 2400)
  --aspect 16:9        aspect ratio (default 16:9)
"""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_INDEX = 2


def hex_to_rgb(h: str) -> tuple:
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def parse_aspect(s: str) -> float:
    a, b = s.split(":")
    return float(a) / float(b)


def fit_font_size(draw, lines, max_width, font_path, font_index, start=100, cap=700, step=10):
    size = start
    while size < cap:
        trial = ImageFont.truetype(font_path, size, index=font_index)
        widest = max(draw.textlength(t, font=trial) for t in lines)
        if widest >= max_width:
            break
        size += step
    return size - step


def render(out_path, line1, line2, color1_hex, color2_hex, bg_hex, width, aspect):
    W = width
    H = int(W / aspect)
    BG = hex_to_rgb(bg_hex)
    C1 = hex_to_rgb(color1_hex)
    C2 = hex_to_rgb(color2_hex)

    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    texts = [line1, line2]
    max_text_width = int(W * 0.88)
    size = fit_font_size(draw, texts, max_text_width, FONT_PATH, FONT_INDEX)
    font = ImageFont.truetype(FONT_PATH, size, index=FONT_INDEX)

    widths = [draw.textlength(t, font=font) for t in texts]
    heights = [
        draw.textbbox((0, 0), t, font=font)[3] - draw.textbbox((0, 0), t, font=font)[1]
        for t in texts
    ]
    line_gap = int(size * 0.22)
    block_h = sum(heights) + line_gap
    y = (H - block_h) // 2 - int(size * 0.05)
    x = (W - max(widths)) // 2

    for t, color, h in zip(texts, [C1, C2], heights):
        draw.text((x, y), t, font=font, fill=color)
        y += h + line_gap

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "PNG", optimize=True)
    print(f"saved: {out_path}  ({W}x{H}, font W6 @ {size}px, {out_path.stat().st_size / 1024:.1f} KB)")


def main():
    ap = argparse.ArgumentParser(description="Typography-dark cover image generator")
    ap.add_argument("--out", required=True, help="Output PNG path")
    ap.add_argument("--line1", required=True, help="First line text")
    ap.add_argument("--line2", required=True, help="Second line text")
    ap.add_argument("--color1", default="F5F5F5", help="Line 1 color hex (default off-white)")
    ap.add_argument("--color2", default="F26B2C", help="Line 2 color hex (default orange)")
    ap.add_argument("--bg", default="000000", help="Background hex (default black)")
    ap.add_argument("--width", type=int, default=2400, help="Canvas width")
    ap.add_argument("--aspect", default="16:9", help="Aspect ratio e.g. 16:9, 1:1, 3:2")
    args = ap.parse_args()
    render(args.out, args.line1, args.line2, args.color1, args.color2, args.bg, args.width, parse_aspect(args.aspect))


if __name__ == "__main__":
    main()
