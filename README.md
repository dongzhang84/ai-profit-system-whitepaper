# Snowboat Blog

Deep-analysis articles in Chinese by [@snowboat84](https://x.com/snowboat84), covering AI & business, education, space exploration, physics & math, and more.

## Articles

| # | Date | Article | X Post | X Views | 知乎 |
|---|------|---------|--------|---------|------|
| 13 | 4/22 | [SpaceX 立志传（一）：赌上全部的最后一次发射](SpaceX%20立志传（一）：赌上全部的最后一次发射.md) | [link](https://x.com/snowboat84/status/2046743964192276766) | — | [link](https://zhuanlan.zhihu.com/p/2028372635839394803) |
| 12 | 4/20 | [估值290亿美元的套壳公司，正在被自己的房东杀死](估值290亿美元的套壳公司，正在被自己的房东杀死.md) | [link](https://x.com/snowboat84/status/2046380497627230607) | — | [link](https://www.zhihu.com/question/1946791222762014096/answer/2029844198262673431) |
| 11 | 4/19 | [黄仁勋和主持人吵红了脸：芯片封锁中国，美国到底能不能打赢？](黄仁勋和主持人吵红了脸：芯片封锁中国，美国到底能不能打赢？（长篇分析）.md) | [link](https://x.com/snowboat84/status/2046022377830801725) | — | [link](https://www.zhihu.com/question/2028405023437014568/answer/2029458215104988529) |
| 10 | 4/16 | [AI将如何颠覆教育，普通人又应该如何抢夺教育新的生态位](AI将如何颠覆教育，普通人又应该如何抢夺教育新的生态位.md) | [link](https://x.com/snowboat84/status/2044932338262667509) | 3.5k | [link](https://zhuanlan.zhihu.com/p/2027582531520708691) |
| 9 | 4/15 | [学物理的八方英雄们，物理学已死，请转行搞AI](学物理的八方英雄们，物理学已死，请转行搞AI.md) | [link](https://x.com/snowboat84/status/2044584627046920278) | 1.3k | [link](https://zhuanlan.zhihu.com/p/2027392166075406203) |
| 8 | 4/14 | [不会编程、没有融资、没有员工，他怎么一个人做到年入2000万](不会编程、没有融资、没有员工，他怎么一个人做到年入2000万.md) | [link](https://x.com/snowboat84/status/2044216044575998136) | 3.3k | [link](https://zhuanlan.zhihu.com/p/2027291547884897412) |
| 7 | 4/13 | [兄弟们想清楚：究竟是你为X打工，还是X为你打工？](兄弟们想清楚：究竟是你为X打工，还是X为你打工？.md) | [link](https://x.com/snowboat84/status/2043842017260908743) | 3.8k | — |
| 6 | 4/12 | [一人公司盈利四亿美元：是骗子，还是可复制的红利？](一人公司盈利四亿美元：是骗子，还是可复制的红利？.md) | [link](https://x.com/snowboat84/status/2043493870265422223) | 0.8k | [link](https://zhuanlan.zhihu.com/p/2026950177747903194) |
| 5 | 4/10 | [2026第一季度大裁员，AI是背锅侠吗？](2026第一季度大裁员，AI是背锅侠吗？.md) | [link](https://x.com/snowboat84/status/2042766853404307931) | 2.8k | — |
| 4 | 4/9 | [重返星辰大海：这次绕月飞行有意义吗？](archive/重返星辰大海：这次绕月飞行有意义吗？.md) | [link](https://x.com/snowboat84/status/2042405716380835998) | 4.6k | [link](https://zhuanlan.zhihu.com/p/2026252685142242468) |
| 3 | 4/8 | [张雪峰在美国为什么无法成功](archive/张雪峰在美国为什么无法成功.md) | [link](https://x.com/snowboat84/status/2042045634245746743) | 2.3k | [link](https://zhuanlan.zhihu.com/p/2026250301347243657) |
| 2 | 4/7 | [2026 企业尸检报告：不用AI，你的公司能活过今年吗？](archive/2026%20企业尸检报告：不用AI，你的公司能活过今年吗？.md) | [link](https://x.com/snowboat84/status/2041672997959057517) | 100+ | — |
| 1 | 4/5 | 兄弟们，我创业失败了，人生完整了 | [link](https://x.com/snowboat84/status/2040948420391940272) | 1.4k | — |

## Writing Workflow

Articles are drafted as rough notes, then expanded into structured pieces using the `/write-article` Claude Code skill from [vibe-writing-skills](https://github.com/dongzhang84/vibe-writing-skills) (my open-source writing skill repo). Each article includes:

- Fact-checked data via web search
- References with source links
- Original draft appended as an appendix

## Cover Images

Article covers use a single house style: **typography-dark**. Black background, two-line Chinese title, line 1 in off-white (setup), line 2 in orange (the main claim). No illustrations, no decoration. 16:9, 2400×1350.

### How to make a new cover

One command:

```bash
python3 scripts/cover-typography-dark.py \
  --out cover-image/<slug>/cover.png \
  --line1 "<setup line>" \
  --line2 "<payload line>"
```

Where:

- `<slug>` is a short kebab-case folder name for the article (e.g. `three-claude-skills`)
- `<setup line>` is the first, softer half of the title — rendered in off-white
- `<payload line>` carries the main claim — rendered in orange so the eye lands on it

Example:

```bash
python3 scripts/cover-typography-dark.py \
  --out cover-image/three-claude-skills/cover.png \
  --line1 "每个人都应该使用的" \
  --line2 "三个最有用的 Claude Skill"
```

### Design defaults

| Setting | Value |
|---|---|
| Background | `#000000` |
| Line 1 color | `#F5F5F5` (off-white) |
| Line 2 color | `#F26B2C` (orange) |
| Font | Hiragino Sans GB W6 (macOS system font) |
| Aspect | 16:9 |
| Canvas | 2400×1350 |

Font size is auto-computed so the longer of the two lines fills 88% of canvas width.

### Overrides

The script accepts flags if you need to deviate (rarely — the house style should stay consistent):

- `--color1 HEX` / `--color2 HEX` · change per-line colors (e.g. `--color2 FFFFFF` for an all-white variant)
- `--bg HEX` · change background (e.g. `--bg FAFAFA` for a light variant)
- `--width 1080` · smaller canvas
- `--aspect 1:1` · square for Xiaohongshu / `--aspect 3:2` for 公众号

### When Claude asks about cover design

When invoking `/baoyu-cover-image`, Claude loads `.claude/skills/baoyu-cover-image/EXTEND.md` which points to this preset by default. Unless you explicitly ask for a different palette or layout, it should go straight to running the command above, no questions asked.

### Output location

Covers live in `cover-image/<slug>/`, one folder per article:

```
cover-image/
└── three-claude-skills/
    ├── cover.png              # the rendered cover
    ├── render_cover.py        # article-specific wrapper (optional, historical)
    └── prompts/cover.md       # design prompt (for reference / variants)
```

## Reading List

A curated reading list ([reading-list.md](reading-list.md)) on AI & business transformation, organized in four stages:

1. **Death Traps**: understanding why traditional businesses fail
2. **AI-Native Architecture**: the new paradigm
3. **Acquisition & Growth**: rebuilding the customer engine
4. **Data Sources**: McKinsey, a16z, CB Insights, BLS, and more

## Status

Work in progress.
