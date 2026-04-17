---
name: write-article
description: 把零散的笔记、想法、要点整理成一篇结构完整、逻辑清晰的中文文章。支持指定风格和目标读者。
allowed-tools: Read Edit Write Glob Grep WebSearch WebFetch
argument-hint: [输入文件或内容描述]
---

# 整理文章

将用户提供的零散内容整理成一篇结构完整的中文文章。

## 第零步：加载配置（必做）

开始任何素材处理前，用 Read 工具依次加载以下配置文件（路径相对项目根目录），把其中所有规则作为硬性约束：

1. `.claude/skills/write-article/persona.md`：作者人设
2. `.claude/skills/write-article/style.md`：语言、段落、标题、数字、地域范围
3. `.claude/skills/write-article/structure.md`：章节编号、案例、数据、理论联系现实、结论要求
4. `.claude/skills/write-article/error-log.md`：错题本（append-only 禁区清单）
5. `.claude/skills/write-article/output-format.md`：参考文献与原始草稿附录格式

配图相关（`.claude/skills/write-article/references/images.md`）只在用户主动询问配图时加载。

## 第一步：收集素材

- 若 `$ARGUMENTS` 包含文件路径，读取所有指定文件
- 若直接描述主题和要点，从 `$ARGUMENTS` 提取
- 两者可结合
- 提取所有关键观点、数据、案例、引用；识别核心主题

## 第二步：分析与规划

- 确定核心论点（一句话概括）
- 按逻辑关系分组归类素材
- 设计大纲：标题、引言、3-5 个核心主节、结尾
- 大纲遵循 `structure.md` 的章节编号规范

## 第三步：事实核查

- 用 WebSearch 逐一核查时间、数据、人名、事件细节
- 必要时用 WebFetch 抓取权威来源（官方网站、Wikipedia、NASA 等）
- 记录所有引用的来源 URL
- **原始草稿里的数据可能有误**，主动核查并修正，不要照抄

## 第四步：撰写

按大纲扩写，同时遵守第零步加载的 persona / style / structure 三份规则。

去除重复，合并相似观点，补充必要过渡句。

## 第五步：自检

对照 `error-log.md` **逐条**自检（现 16 条），特别注意：

- 用 Grep 搜索 `——`，确认正文（不含原始草稿附录）为零
- 油腻话术关键词搜索
- 段落长度扫描（2-4 句）
- 数字可读性通读
- 地域范围与主题一致
- 案例有名有姓有数据
- 科普文章：每个理论概念后有实验或现实连接
- **AI 味扫描**：Grep 否定平行句式 `不是.*\(而是\|，是\)`（目标 0 次，严格例外最多 1 次）+ AI 中英文高频词清单（至关重要/意义重大/标志着/见证/根植于/delve/tapestry 等）+ 模糊归属（"通常被认为""研究表明" 等）
- **结尾单独过一遍**：对最后 3 段额外扫 "从.*到.*到" 三项递进、"序章/新篇章/新阶段"、"让我们/共同期待/拥抱"、"那个画面/那一刻/历史将记住"、"最重要的/最具里程碑"

每发现一条违规，立即修正。

## 第六步：输出

按 `output-format.md` 的规范：

- 写入 Markdown 文件（项目根目录）
- 末尾附参考文献（超链接格式）
- 末尾附原始草稿（引用格式，原样保留）
- 向用户返回：文件路径、主节标题清单、大致字数、参考文献条数

## 错题追加

用户反馈"别再 X"时，向 `.claude/skills/write-article/error-log.md` 追加一条新条目（append-only，不修改历史条目），不要动 `SKILL.md` 或其他配置文件。
