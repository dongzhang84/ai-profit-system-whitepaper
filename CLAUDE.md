# CLAUDE.md

## 项目简介

这是一个中文写作项目，包含多篇深度分析文章，涵盖AI与商业、教育、科技等话题。文章以 Markdown 格式存储在项目根目录。

## 写作规范

- 语言：中文为主，关键术语可保留英文
- **绝对不要使用破折号（——）**，用逗号、句号或重新组织句子来替代
- **避免 AI 味**：否定平行句式"不是X，是Y"默认 0 次；AI 高频词（至关重要、意义重大、标志着、见证、根植于 等）零容忍；结尾尤其是 AI 味重灾区。完整清单见 `.claude/skills/write-article/writing-rules.md`
- 风格：直接、有观点、用数据说话，避免空话套话
- 每篇文章末尾必须包含**作者其它文章**、**本文参考文献**（带超链接）、**附录：原始草稿**
- 文章中涉及的事实、数据、时间、人名必须通过 WebSearch 核查后再写入

## 可用 Skill

- `/write-article [文件路径或主题]`：把零散笔记整理成结构完整的文章。流程：收集素材 → 分析规划 → 事实核查 → 撰写 → 输出带参考文献的 Markdown 文件
- `/traffic-review [时间范围或文章编号]`：基于 README 里的 X 流量数据和文章开头，分析题材/标题/开头框架与流量的关系，输出复盘到 `analysis/` 文件夹
- `/baoyu-diagram`：生成 SVG 示意图到 `diagram/{slug}/`。本地设计规则见 `.claude/skills/baoyu-diagram/references/design-system.md`（反推自已有四张图）

## 图表转 PNG

SVG 用 CSS 变量做亮暗切换，rsvg-convert 不支持，直接转会一片漆黑。必须用 `python3 scripts/svg-to-png.py <svg> [-w 1600]`，它会先剥掉 `@media dark` 块、把 `:root` 亮色 hex 值就地替换再转。

## 项目结构

- `*.md`（根目录）：各篇文章
- `archive/`：10 天以上的旧文章
- `analysis/`：流量复盘分析
- `diagram/{slug}/`：示意图（`diagram.svg` + `diagram.png` + `plan.md`）
- `scripts/svg-to-png.py`：SVG → PNG 转换脚本
- `.claude/skills/write-article/`：文章整理 skill
- `.claude/skills/traffic-review/`：流量复盘 skill
- `.claude/skills/baoyu-diagram/references/`：本地 diagram 设计规则
- `reading-list.md`：推荐阅读书单

## 流量观察工作流

- **周中碎碎念**：随时把流量数据、读者反馈、传播路径等原始观察记到 `analysis/pending-notes-YYYY-MM-DD起.md` 这一个临时文件里，每天/每次观察追加一段即可
- **周末复盘**：写 weekly report 时把 pending-notes 吸收进正式复盘文件，复盘和下周计划合并在同一份 md 里（不新开文件），完成后删掉 pending-notes
- **文件命名**：正式复盘用 `YYYY-MM-DD至MM-DD N 篇文章流量复盘.md`
