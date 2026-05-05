
市面上的 Claude Skill 仓库少说几百个，官方的、社区的、个人博主随手扔在 GitHub 的，看不完。我写过、抄过、改过 十多个，到如今，仍在每周使用的只剩三个。

今天把这 3 个拎出来讲一遍。我强烈建议每个人都装上这 3 个 skill。至于剩下的那些 skills 为什么被我弃用，我后面再说。

# 一、/write-article 

**来源**：这是我自己写的，已完整开源在 [vibe-writing-skills](https://github.com/dongzhang84/vibe-writing-skills)。

干的事：零散的中文笔记、会议记录、网页截图 → 一篇结构完整的、按照你风格写作的中文长文。

SKILL.md 的核心流程：

```
第一步 · 加载配置（persona / style / structure / writing-rules / output-format）
第二步 · 读取用户指定的素材文件
第三步 · 分析规划（核心论点 + 大纲 + 标题）
第四步 · 事实核查（WebSearch 核实时间 / 数据 / 人名）
第五步 · 撰写（按 persona + style + structure 展开）
第六步 · 自检（对照 writing-rules 逐条 grep）
第七步 · 输出（Markdown + 参考文献 + 原始草稿附录）
```

为啥隆重推荐：这个 skill 之所以能持续用下来，靠的是 references/ 目录里那一堆配套文件。persona.md 写明作者是谁、style.md 写明段落怎么切、writing-rules.md 写明哪些词不能用。每次调用都必读这些规则。

举一个最具体的例子：writing-rules.md 里有一条"AI 高频词零容忍"，几十个具体词（至关重要 / 意义重大 / 标志着 / 见证 等等）列在那里，写完必 grep 自检。模型再有想象力也不敢在这几十个词上瞎编。

你完全可以 fork 这个仓库，把 persona.md 换成你自己的人设，把 writing-rules.md 换成你自己常踩的坑。骨架我搭好了，填自己的真实材料就行。

提醒一句：vibe writing 这套方法论本身涉及人设沉淀、规则迭代、事实核查闭环几个更底层的东西，今天这篇只讲 skill 这一层，改天我会单独写一篇把 vibe writing 这个概念系统讲清楚。

# 二、/code-review 

**来源**：Anthropic 官方 [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) 仓库里的 code-review 插件。也是 Anthropic 内部每个 PR 都在跑的那套系统。

干的事：对一个 PR branch 启动 4 个 agent 并行 review，每个 agent 看不同类别的 bug（逻辑、类型、安全、可读性），打一个置信度分数，只保留 80+ 的 issue 作为 inline comment。

为啥强烈推荐：这是官方自家产线跑出来的 skill，不是社区实验品。更关键的是它解决了一个大部分独立开发者都有的问题：没人给你 review PR。一个人写，一个人合，第二天自己再看也抓不出什么。

我装这个之前每周至少有一次"上线后才发现一个傻 bug"。装上以后 agent 会在合之前指出来，命中率不算高（大概三成），但那三成里有至少一条是真能救你的。对比手动请同事 review 要排期等反馈，这个 3 分钟就能跑完。

安装门槛也低：Claude Code 官方插件，按 [Anthropic 官方文档](https://claude.com/plugins/code-review) 里的步骤在 Claude Code 里启用就行，不用自己写 SKILL.md，也不用 clone 仓库。命令行小白跟着文档点几下就能装上。

# 三、/baoyu-diagram 以及宝玉整套 skill

**来源**：宝玉（[@dotey](https://x.com/dotey)）的 [baoyu-skills](https://github.com/JimLiu/baoyu-skills) 仓库。

宝玉这个仓库里装着一整套中文内容生产的全家桶，diagram 只是其中一个：

- `baoyu-diagram` · 概念示意图 / 流程图 / 架构图，输出 SVG
- `baoyu-infographic` · 高信息密度信息图
- `baoyu-cover-image` · 文章封面图
- `baoyu-article-illustrator` · 文内智能配图
- `baoyu-comic` · 知识漫画
- `baoyu-slide-deck` · 幻灯片 / PPT
- `baoyu-xhs-images` · 小红书九宫格图文
- `baoyu-post-to-x` · X 发布自动化
- `baoyu-post-to-wechat` · 公众号发布

一篇长文从构思、画图、配图、封面一直到跨平台分发，宝玉这一整套基本能全流程接住。我在根本没有设计师的情况下能把视觉这一块做到看得过去，全靠这一套。

我挑 /baoyu-diagram 细讲，因为它最能说明宝玉这一套为啥值得推荐。

干的事：从一个概念或数据点，生成可嵌入文章的 SVG（概念示意图、流程图、架构图都通吃）。自带亮 / 暗模式切换，有统一的设计系统。

为啥强烈推荐：中文读者对配图很敏感。纯文字长文在 X 上的划走率明显高一档。以前我每次画图要在 Figma 里手搓 30 分钟，现在 3 分钟一张。

但这个 skill 真正值钱的地方不是速度，是 references/design-system.md 这个文件。它沉淀了配色 hex、字号、间距比例、箭头粗细这些设计约束。Skill 调用时必读这个文件。我十篇文章里的图摆在一起看，风格一致到像一家设计工作室出的货。

这是 skill 最被低估的能力。references/ 目录让"一致性"不靠记忆，靠写在文件里的约束。以前我每次画图都要翻之前的文件看"上次那个蓝用的是哪个 hex"，现在这些值都在 reference 文件里，skill 自动遵守。

宝玉这套仓库里别的 skill 也都沿用同一套设计系统，diagram / infographic / cover-image 三张图放在一起看视觉风格完全对齐。这是单独写 9 个 skill 很难做到的。

# 四、反面参考：被我弃用的 各种skills，我挑 5 个说

如果你只看留下的 3 个会觉得"skill 都值得写"，这是误读。大部分 skill 都进不了"每周跑一次"的门槛。挑 5 个弃用理由有代表性的说。

`/daily-summary` · 我自己写的，灵感源 Notion AI / Readwise Daily Review。每天自动扫笔记 + commits + 阅读记录，输出结构化日志条目。弃用理由：Claude 编了 60% 内容。我一天真实做的事比它产出的"当日完成"少一半。没有可信输入源的 skill 必弃，模型想象力越好越危险。

`/daily-schedule` · 我自己写的。每天早上读 Google Calendar + Linear ticket + GitHub notifications，输出当日优先级和时间块建议。跑了两周还行，一个月后彻底没在用了。弃用理由不在 skill 本身，在生态：我换到 [Cowork](https://cowork.ai) 之后整个日程管理被它端到端托管，排会议、定优先级、挡打扰全包了，skill 这一层的价值直接归零。启示：写 skill 之前先扫一圈有没有现成的独立产品已经把这件事做到了产品级。产品级工具会越来越多地把 skill 吃掉。

**Nuwa Skill** · 社区高星。GitHub Trending 过一阵子的 [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill)，号称能"蒸馏"乔布斯、马斯克、费曼、芒格、张雪峰的认知操作系统，让 Claude 用他们的思维框架分析问题。弃用理由：前三天新鲜，第四天开始怀疑"这真是他会说的话吗"。蒸馏下来的是语言表面，而非思想本体。用来娱乐可以，用来做决策风险极大。

`/resume-optimizer` · 我自己写的，灵感源 Teal / Rezi 类。改简历、生成 cover letter、按岗位定制关键词。弃用理由：一年用一次的东西不值得 skill 化。低频动作的封装成本全浪费在了维护上，两周后 skill 本身就过时了。

`/social-matrix` · 我自己写的。给自媒体朋友推的"一条内容分发到 X / 公众号"。弃用理由：优化一个你根本没有的东西。我连 X 一个平台都没更新稳定，谈什么矩阵。Skill 只能放大你已经在做的动作，救不了你本来就不做的动作。

剩下 4 个弃用理由大同小异。把 9 个弃用理由归到一块看，只有三条模式。

**使用频率被高估**："我每周可能会用一次"的 skill，大概率一个月用不到两次。Skill 化的前置条件是你每周真的在做 3 次以上这个动作，低于这条阈值就不要封装。封早了变成维护负担，你还没把 skill 用熟 Claude Code 本身就升级了。

**让 Claude 编数据**：没有可靠输入源的 skill 必弃。/daily-summary 被放弃就在于"让 Claude 想当天做了什么"这一步。模型在缺数据时的默认行为是 hallucinate。它不会 fail，它会编得像真的一样，你一开始还信。

**优化你根本没在做的事**：/social-matrix 和其他几个被我弃用的 skill 都犯了这个错。Skill 是工程手段，你没养成的习惯工程手段救不回来。

# 五、一条判准

把 9 弃 3 留摆在一起看，能抽出一条判准：

> Skill 值不值得持续用满 2 周，只看一件事：这个动作，你每周真的都在做吗？

判断的标尺很粗暴：每周五下午 3 点你真的会不会去做这件事。"理论上应该做"和"做起来应该不错"都不算。

粗暴，但准。被弃用的 9 个都没过这一关。留下的 3 个都过了。

写 skill 之前花 10 秒问自己这条，能帮你省一个月的绕路。

还有一个反直觉的含义：你不需要写很多 skill，也不必都是自己写的。

留下的 3 个里，一个我自己写，一个来自 Anthropic 官方，一个来自宝玉。工程师的本能是"自己造"，但 skill 这一层，借用大于自造。品味对得上、维护节奏稳、开源且更新快的 skill，没理由重写一遍。把写新 skill 的时间花在"改别人 skill 让它更贴合我的工作流"上，投产比高得多。

我的 `.claude/skills/` 目录下现在就这 3 个 skill 在每周跑。配置和 references 加起来不到 30 个文件。剩下的时间我宁愿花在改规则上，让这 3 个在更多 edge case 下稳定。

工程师的直觉是"多造工具"。Skill 的反直觉是"少造、深用、敢借"。

这是我 `.claude/skills/` 目录当前的清单。你的目录里装着几个？每周真在跑的又有几个？写过又弃用的又是哪几个？评论区交换一下你的清单。我最想收集的是：有哪个 skill 你觉得每个人都该装、但我这篇没写到？下次 refresh 我把你推荐的补进来。

---

## 作者其它文章

- [SpaceX 立志传（一）：赌上全部的最后一次发射](https://x.com/snowboat84/status/2046743964192276766)
- [估值290亿美元的套壳公司，正在被自己的房东杀死](https://x.com/snowboat84/status/2046380497627230607)
- [黄仁勋和主持人吵红了脸：芯片封锁中国，美国到底能不能打赢？](https://x.com/snowboat84/status/2046022377830801725)
- [AI将如何颠覆教育，普通人又应该如何抢夺教育新的生态位](https://x.com/snowboat84/status/2044932338262667509)
- [学物理的八方英雄们，物理学已死，请转行搞AI](https://x.com/snowboat84/status/2044584627046920278)
- [不会编程、没有融资、没有员工，他怎么一个人做到年入2000万](https://x.com/snowboat84/status/2044216044575998136)
- [兄弟们想清楚：究竟是你为X打工，还是X为你打工？](https://x.com/snowboat84/status/2043842017260908743)
- [一人公司盈利四亿美元：是骗子，还是可复制的红利？](https://x.com/snowboat84/status/2043493870265422223)
- [2026第一季度大裁员，AI是背锅侠吗？](https://x.com/snowboat84/status/2042766853404307931)
- [重返星辰大海：这次绕月飞行有意义吗？](https://x.com/snowboat84/status/2042405716380835998)
- [张雪峰在美国为什么无法成功](https://x.com/snowboat84/status/2042045634245746743)
- [2026 企业尸检报告：不用AI，你的公司能活过今年吗？](https://x.com/snowboat84/status/2041672997959057517)
- [兄弟们，我创业失败了，人生完整了](https://x.com/snowboat84/status/2040948420391940272)

---

## 本文参考文献

- [vibe-writing-skills - GitHub](https://github.com/dongzhang84/vibe-writing-skills) - /write-article skill 完整开源，含 persona / style / structure / writing-rules / output-format 全套配置
- [claude-plugins-official - Anthropic 官方](https://github.com/anthropics/claude-plugins-official) - Anthropic 官方维护的 Claude Code plugin 仓库，code-review 插件的来源
- [Code Review for Claude Code - Anthropic Blog](https://claude.com/blog/code-review) - /code-review 机制说明：多 agent 并行 review + 置信度过滤
- [baoyu-skills - GitHub](https://github.com/JimLiu/baoyu-skills) - 宝玉的 skill 集合，/baoyu-diagram 的来源
- [宝玉 (@dotey) on X](https://x.com/dotey) - 中文 AI 圈最活跃的 prompt 工程实践者之一
- [alchaincyf/nuwa-skill - GitHub](https://github.com/alchaincyf/nuwa-skill) - 号称"蒸馏乔布斯 / 马斯克 / 张雪峰认知操作系统"的社区 skill 框架
- [Claude Code 官方 Skill 文档](https://docs.claude.com/en/docs/claude-code/skills) - Skill 的机制和 SKILL.md 规范

---

## 附录：原始草稿

> 重写后的提纲
>
> 标题候选
>
> - 每个人都应该使用的 3 个最有用的 Claude Skill
> - Skill 写了十几个，每周都用的只有 3 个
>
> 开头反转钩子 · 50-80 字
>
> ▎ 市面上 skill 几百个，我写过改过 12 个，每周在跑的只剩 3 个。
> ▎ 今天先说这 3 个每个人都该装的 skill，坟场放后面。
>
> Part 1 · 活下来的 3 个（正主）
>
> ① /write-article · 自己写的 · vibe-writing-skills 仓库
> ② /code-review · Anthropic 官方 claude-plugins-official
> ③ /baoyu-diagram · 宝玉 baoyu-skills
>
> 每个讲：来源 / 干啥 / 为啥每个人都该装 / fork 成本
>
> Part 2 · 反面参考：坟场 4 个
>
> - /daily-summary · Claude 编了 60% 内容
> - Nuwa Skill · 社区高星 · 蒸馏名人 · 真伪无法验证
> - /resume-optimizer · 一年用一次不值得 skill 化
> - /social-matrix · 优化你根本没有的东西
>
> 三条共同死因：高估使用频率 / 让 Claude 编数据 / 优化你根本没做的事
>
> 结论金句
>
> ▎ Skill 能不能活过 2 周，只看一件事：
> ▎ 这个动作你每周真的都在做吗？
>
> 反直觉收尾
>
> 活下来的 3 个里 2 个不是我写的。工程师的直觉是多造，skill 的反直觉是少造、深用、敢借。
>
> 尾句
>
> ▎ 你的 skill 坟场里躺着哪几个？死因一句话。
