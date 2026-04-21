# Write-Article Skill 工程化方案

本文档定义 `write-article` skill 的工程化架构、文件职责与迁移计划。

## 目标

把个人写作流程从"经验 + 口头约定"升级为**可追加、可审计、可复用的工程化系统**：

- 每一条写作规则有明确归属文件，不散落在对话里
- 规则可追加沉淀，下次写作自动读入，不靠记忆
- 流程、人设、风格、结构互相解耦，改一处不污染另一处
- 维护者（人）看任何一个维度只看一个文件，不在 wall of text 里翻找

## 非目标

以下明确不做：

- 多智能体编排（style-checker agent、reviewer agent 等）
- 写作前的 Document Spec / DoD 清单
- PDF 入库、AI 味检测 API、LaTeX 自愈
- Memory JSON 数据库（hard/soft memory）

原因：单人博客场景，以上机制的维护成本远超收益。

## 架构原则

1. **单一职责**：每个文件只管一个维度（流程 / 人设 / 风格 / 规则 / 结构 / 输出 / 引用）
2. **显式导入**：`SKILL.md` 执行开头明确 Read 所有配套文件，不依赖隐式加载
3. **独立演化**：高频变化的文件（`writing-rules.md`）与低频变化的文件（`persona.md`）物理分离
4. **可追加优先**：`writing-rules.md` 为 append-only，不做结构化重组，降低写入阻力
5. **工程化 ≠ token 优化**：多文件方案的 token 成本与单文件相同，价值在维护者的认知负担

## 文件结构

```
.claude/skills/write-article/
├── SKILL.md           # 入口与编排层
├── persona.md         # 作者身份与硬性人设规则
├── style.md           # 语气、段落、标题、数字、地域范围
├── structure.md       # 章节编号、案例要求、对比表格规范
├── writing-rules.md       # 写作规则（append-only）
├── output-format.md   # 参考文献 + 原始草稿附录模板
├── references/
│   └── images.md      # 配图来源清单（Wikimedia、NASA 等）
└── ARCHITECTURE.md    # 本文件
```

## 各文件职责

### SKILL.md（编排层）

**只做两件事**：

1. 执行开始前 Read 所有配套文件（`persona.md` / `style.md` / `structure.md` / `writing-rules.md` / `output-format.md`）
2. 定义流程步骤：收集素材 → 分析规划 → 事实核查 → 扩写 → 自检 → 输出

**不包含具体规则**。所有"怎么写""写成什么样"的规则下沉到配套文件。

目标行数：< 60 行。

### persona.md

作者的三重身份、写作底色、硬性人设规则（禁油腻话术等）。

低频变化，基本稳定。

### style.md

- 语言偏好（中文为主，关键术语保留英文）
- 段落长度要求（2-4 句）
- 数字可读性（3万而非 30,000）
- 地域范围规则（美国话题只用美国数据）
- 标题原则

低频变化。

### structure.md

- 主节编号（中文数字 + `##`）
- 子节（`###` + 关键词）
- 案例要求（有名有姓有数据、优先 2024-2026 案例）
- 表格对比规则
- 结论分量要求

低频变化。

### writing-rules.md

**Append-only 规则清单**。每条包含：

- 日期
- 错误类型简述
- ❌ 错误示范
- ✅ 正确做法
- 🔒 硬性约束指令

初始内容从现有 SKILL.md 的"第五步：质量自检"与用户历史反馈（feedback memory）中提取：

- 禁破折号（——）
- 禁油腻话术（躺赚 / 睡后收入 / 财富自由 / 暴富 / 月入百万）
- 段落要短（2-4 句）
- 理论必须联系实验和现实
- 地域范围必须对齐主题

**高频变化**。每次用户反馈"别再 X"，追加一条。

### output-format.md

- 参考文献格式：`[标题](URL) - 来源`
- 附录：原始草稿必须原样保留（包括其中的破折号）
- 文件命名规则（基于标题）

低频变化。

### references/images.md

配图来源优先级清单（Wikimedia Commons → NASA / 政府公共领域 → 其他）。

偶尔追加。

## 迁移计划

1. **创建骨架**：建立所有配套文件，空内容
2. **拆分 SKILL.md**：把现有 ~130 行 SKILL.md 按维度拆进各配套文件
3. **精简 SKILL.md**：只保留编排层（流程 + Read 指令）
4. **初始化 writing-rules.md**：从现有质量自检清单 + 用户 feedback memory 里提取初始规则
5. **验证**：用一篇现有草稿跑一次 `/write-article`，确认所有配套文件被读取、规则生效
6. **迭代**：后续每次用户反馈 → append 到 `writing-rules.md`，不改 `SKILL.md`

## 未来扩展（不现在做）

如果后续出现以下需求再考虑：

- 多 skill 复用 `style.md` / `writing-rules.md`：提取到 repo 根的 `.claude/shared/`
- 写作规则膨胀到难以维护：按主题分文件（`writing-rules-facts.md` / `writing-rules-tone.md`）
- 需要 spec-driven 写作：新增 `spec-template.md`，流程插入 spec 阶段

以上均为 YAGNI，当前不实现。
