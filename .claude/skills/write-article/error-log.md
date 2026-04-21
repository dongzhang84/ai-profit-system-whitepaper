# 错题本

本文件是 **append-only** 错题清单。每次用户反馈"别再 X"，追加一条，不修改历史记录。

写作时必须把每一条当作硬性约束。写完后对照自检。

## 条目格式

```
## [YYYY-MM-DD] 错误类型简述
- ❌ **错误示范**：...
- ✅ **正确做法**：...
- 🔒 **硬性约束**：...
- 📍 **背景**（可选）：什么情况下用户反馈的
```

---

## [2026-04-07] 使用破折号（——）

- ❌ **错误示范**：文章中出现任何形式的破折号 `——`
- ✅ **正确做法**：用逗号、句号或重新组织句子来替代
- 🔒 **硬性约束**：写完后必须用 Grep 搜索 `——` 确认全文为零。**例外**：附录里的用户原始草稿保留原样，不修改其中的破折号
- 📍 **背景**：用户明确要求，多次反馈，零容忍

## [2026-04-13] 油腻暴富话术

- ❌ **错误示范**："躺赚""睡后收入""财富自由""暴富""月入百万"
- ✅ **正确做法**：用具体数字和可复现路径描述收入，不做情绪化承诺
- 🔒 **硬性约束**：写完后搜索这几个词，出现即删除改写
- 📍 **背景**：人设硬性规则，作者是理科生不是微商

## [2026-04-14] 段落太长

- ❌ **错误示范**：一个段落塞 5 句以上，包含多个概念
- ✅ **正确做法**：每段 2-4 句，聚焦一个观点，写完就换段
- 🔒 **硬性约束**：自检时扫描段落长度，超过 4 句考虑拆分
- 📍 **背景**：用户反馈"写得太长了"，要求和卡拉比-丘上中篇风格统一

## [2026-04-15] 理论和现实脱节（科普文章）

- ❌ **错误示范**：数学/物理概念连篇铺陈，无实验佐证，无现实映射
- ✅ **正确做法**：每介绍一个理论概念后，紧跟"实验怎么说？"或"这和我们的世界有什么关系？"。没有实验验证也要明确写出来
- 🔒 **硬性约束**：科普文章自检时检查每个主要理论段落后是否有实验或现实连接
- 📍 **背景**：用户反馈卡拉比-丘下篇"和实际脱节，完全没有写到实验方面的佐证"

## [2026-04-14] 数字可读性差

- ❌ **错误示范**：30,000、91,679、$796.25、4.43 亿
- ✅ **正确做法**：3 万、近 10 万、约 796 美元、约 4.4 亿
- 🔒 **硬性约束**：写完通读全文，把所有"零太多"的数字改为中文单位
- 📍 **背景**：零多的数字对中文读者不友好。百分比和倍数例外（保持精确）

## [2026-04-14] 地域范围错配

- ❌ **错误示范**：写"美国大裁员"却混入全球数据
- ✅ **正确做法**：主题指向某个地区，数据也只用该地区的
- 🔒 **硬性约束**：自检时确认文章地域范围和数据范围一致
- 📍 **背景**：数据范围错配会误导读者

## [2026-04-14] 案例无名无姓无数据

- ❌ **错误示范**："某公司做到了很高的收入"
- ✅ **正确做法**："Pieter Levels 一个人做了 7 个产品，年入约 300 万美元，利润率超过 90%"
- 🔒 **硬性约束**：所有案例必须有名有姓有数据，没有就查，查不到就不用
- 📍 **背景**：无名案例等于没写

## [2026-04-17] AI 高频中文词汇（零容忍）

- ❌ **错误示范**：正文出现"至关重要、意义重大、不可或缺、举足轻重、标志着、见证、根植于、反映出更广泛的、不断变化的格局、不可磨灭、蓬勃发展、日新月异、服务于、赋能、稳稳地、悄然、前所未有地"等 AI 味高频词
- ✅ **正确做法**：用具体动词和数据替代。"至关重要" → "直接决定" 或 "关键差异在于"；"意义重大" → 给出具体影响数字；"见证" → "看到"、"经历"；"标志着" → "是" 或直接描述发生了什么
- 🔒 **硬性约束**：写完对照下列清单逐个 Grep：`至关重要 意义重大 不可或缺 举足轻重 标志着 见证 根植于 反映出 不断变化 不可磨灭 蓬勃发展 日新月异 服务于 赋能 稳稳地 悄然 前所未有`。正文出现即删除或改写
- 📍 **背景**：中文 Wikipedia "AI 生成文的特征" 条目列为 AI 典型词汇；中文读者一眼嗅出 AI 味

## [2026-04-17] AI 高频英文词汇（零容忍）

- ❌ **错误示范**：英文或中英混写正文里出现 delve / tapestry / landscape / realm / harness / illuminate / pivotal / underscore / multifaceted / foster / testament / paramount / crucial / robust / seamless / navigate / leverage（商业语境外）
- ❌ **错误示范**：英文短语 "at its core" / "in today's fast-paced world" / "that being said" / "to put it simply" / "in the ever-evolving landscape of" / "embark on a journey" / "a deep dive into" / "unlock the potential of"
- ✅ **正确做法**：用朴素英文。delve → examine / look at；tapestry → network / mix；harness → use；illuminate → show；pivotal → key / important
- 🔒 **硬性约束**：文章含英文段落或中英混写时，写完 Grep 上述词清单
- 📍 **背景**：Originality.AI / Medium / Walter Writes AI 等英文社区公认的 AI 识别词

## [2026-04-17] 否定平行句式（尽量完全避开）

- ❌ **错误示范**："不是 X，是 Y" / "不是 X，而是 Y" / "不仅仅是 X，更是 Y" / "与其说 X 不如说 Y"。中文 Wikipedia 和英文社区都把这个句式列为 AI 最典型的句式，有一处读者就能察觉一次 AI 味
- ✅ **正确做法**：**默认完全改成正面陈述**。常见改写：
  - "不是 X，是 Y" → "真正的 Y 是……（X 只是表面）"
  - "不是因为 X，是因为 Y" → "原因其实是 Y"（或 "X 不成立，原因是 Y"）
  - "问题不是 X，而是 Y" → "问题出在 Y 上"（或 "真正的问题在 Y"）
  - "不是 A 不能 B，是有人 C" → "A 本身没问题，堕落发生在有人 C"
- 🔒 **硬性约束**：写完 Grep `不是.*\(而是\|，是\)`。**正文默认目标为 0 次**。只有在以下严格情况才允许保留 1 次：该句是全文核心定义、没有任何等价的正面陈述能替代、且该句承担关键的叙事转折作用
- 📍 **背景**：AI 生成文最有代表性的句式，连密度很低（5000 字 3 处）都能被读者嗅出。早前规则"不超过 3 次"实测仍显 AI 味，升级为"尽量为零"

## [2026-04-17] 模糊归属与无来源数据

- ❌ **错误示范**："通常被认为" / "广泛认为" / "业界普遍认为" / "常常被提到" / "有声音指出" / "有观点认为" / "多方来源表明" / "研究表明" / "数据显示" 等没有具体人名/机构/时间的归属
- ✅ **正确做法**：要么给出具体来源（"Stanford RegLab 2024 年研究表明"），要么删掉这一句用作者自己的判断替代
- 🔒 **硬性约束**：写完 Grep 这几个词。**每一处**要么改成具体归属，要么删掉
- 📍 **背景**：AI 最爱用模糊归属凑字数，同时回避观点责任。作者必须有立场

## [2026-04-17] 万能结构公式

- ❌ **错误示范**：
  - 开头公式："在这个 X 日益 Y 的时代" / "当我们谈到 X 时"
  - 结尾公式："总之 / 综上所述 / 归根结底" + "让我们共同期待 / 拥抱变化"
  - 段落承转公式："首先、其次、再者、此外、最后" / "值得注意的是" / "更重要的是"
  - **"承认挑战 + 正面评估" 万能结尾**：先两段"尽管存在 X、Y、Z 挑战"，再来一段"但我们有理由相信……"
- ✅ **正确做法**：开头从具体场景、人物、数据切入；结尾用具体的判断或建议；段落间用上一段关键词承接
- 🔒 **硬性约束**：文章里不得出现"综上所述""总而言之""归根结底""让我们共同""拥抱 XX"；段首不得用"首先/其次/再者/此外/最后"
- 📍 **背景**：AI 写文章的"安全公式"，读者一读就知道套路

## [2026-04-17] 内容平均化与过度中立

- ❌ **错误示范**：
  - 每个小节字数几乎相等，没有详略
  - 每个观点后面都跟"当然，这也要视具体情况而定"
  - 每个判断都要加"不可否认，X 也有其局限"
  - 每一段都先复述上一段的结论再推进
  - 重复已经说过的概念换不同说法再讲一遍（内容注水）
- ✅ **正确做法**：
  - 作者必须有明确立场，敢说谁对谁错
  - 重点段落写得远长于次要段落
  - 不搞"两手都要抓"的万能平衡
  - 每段必须推进一步，不能原地复述
- 🔒 **硬性约束**：自检时问一句"拿走所有'当然'、'不可否认'、'视具体情况'，文章的观点是否还完整？" 完整就保留，不完整说明观点本来就立不住。过度中立 = 没有作者
- 📍 **背景**：AI 底层训练倾向中立和平均，真作者必须有判断

## [2026-04-17] 气质类陷阱：没有"我"的痕迹

- ❌ **错误示范**：
  - 过度热情：对普通事实表达惊叹（"令人惊叹的"、"不禁让人感慨"、"堪称奇迹"）
  - 过度谦虚：不断声明"这只是一种观点"、"仅供参考"
  - 学术腔装点：用学术词汇假装严谨但没有引用
  - 广告腔：对主题总是正面赞美
  - 鸡汤语气：把具体话题抽象成人生哲理
  - 没有"我"的痕迹：没有第一人称体感、没有具体经历、没有踩过的坑
- ✅ **正确做法**：
  - 第一人称体感优先（"我试过"、"我踩过"、"比我预想的难"）
  - 对普通事实保持平淡，对真正惊人的事才惊叹
  - 判断就是判断，不加"这只是一种观点"
- 🔒 **硬性约束**：自检"文章里有没有至少一处第一人称体感？" 没有就补
- 📍 **背景**：AI 没有身体和经历，所以它的默认语气是没有主语、没有体感的"全知旁白"

## [2026-04-17] 结尾 AI 化陷阱

- ❌ **错误示范**：
  - **三项递进式排比**："从 X，到 Y，到 Z，[主体] 用了十年"
  - **装饰性过渡词**："只是序章" / "新篇章" / "新阶段" / "新的一页" / "新纪元"
  - **过度强调重要性**："真正让 X 从 A 变成 B" / "最重要的" / "最具里程碑意义" / "一个时代就此开启"
  - **万能收尾公式**："尽管 X 挑战重重，但我们有理由相信……"
  - **号召式结尾**："让我们共同" / "拥抱变化" / "值得我们期待" / "值得我们深思"
  - **文艺腔装饰**："那个画面" / "那一刻" / "历史将记住" / "定格在这一刻"
  - **结尾第一段过长**，信息密度松垮，和正文其他段落不在一个水平
- ✅ **正确做法**：
  - 结尾用 2-3 个短段落，每段一个作用（总结 / 画面 / 钩子），不堆砌
  - 写具体的人和事，不抽象成"历史""时代""力量"这类大词
  - 预告下一篇用短句直给，不用"且听下回分解"式装饰
  - 信息密度对齐正文段落
- 🔒 **硬性约束**：自检时把结尾（最后 3 段）**单独拎出来再扫一遍**所有 AI 规则。额外 Grep 结尾两段内是否有："从.*到.*到" 三项递进、"序章\|新篇章\|新阶段\|新的一页\|新纪元"、"最重要的\|最具里程碑"、"让我们\|共同\|期待\|拥抱"、"那个画面\|那一刻\|历史将记住"
- 📍 **背景**：SpaceX 立志传（二）结尾初版撞了三项递进 + "只是序章" + "最重要的商业力量" + "稳稳地"。用户反馈像 AI。结尾是 AI 味重灾区，因为写作者到结尾容易松弛、想"升华"一下

## [2026-04-18] 编号式并列陈述当叙事

- ❌ **错误示范**：
  - 段首机械编号的并列陈述：`第一，……。第二，……。第三，……。第四，……。`
  - 以分类词编号：`差异一，……。差异二，……。差异三，……。`
  - 看起来是散文，其实骨架是 PPT bullet，每段起首都一模一样
- ✅ **正确做法**：用自然递进的叙事过渡把并列点串起来
  - `最大的一条是X。紧接着是Y。第三重代价是Z。还有一层悖论是……`
  - `先说一件事……另一件……最麻烦的一件……`
  - `最直观的是X。再上一层是Y。第三条路径是Z。`
- 🔒 **硬性约束**：正文（非真正的清单、非表格）里段首不得出现 `第一，` `第二，` `第三，` `差异一，` `差异二，` 等编号。N ≥ 3 个并列点用编号尤其致命。Grep `^\*?\*?第[一二三四五六]\(，\|、\)` 和 `^\*?\*?差异[一二三四]\(，\|、\)`，正文命中 = 0
- 📍 **背景**：Jensen Huang 文章第 5 节（差异一/二/三/四）和第 8 节（第一/二/三/四）两次被用户打回："太 AI 味了""像 PPT 不像文章"

## [2026-04-18] 粗体滥用

- ❌ **错误示范**：
  - 整段整句加粗做"强调"：`**美国政府不再声称"小院高墙"是目标，开始用 15% 抽税把封锁当成收税工具**`
  - 给抽象概念/长短语挂粗体：`**研发飞轮** **平台护城河** **竞争压力** **自我实现的预言**`
  - 每段挑一两个词加粗，让整节像花式标注的教科书
  - 粗体作为 PPT 式关键词醒目提示，读者读起来一阵一阵被打断
- ✅ **正确做法**：粗体只用在三类地方
  - (a) **专名首次出现**：政策名、行动名、机构名的首次引入（`**AI Diffusion Rule**`、`**Operation Gatekeeper**`）
  - (b) **短数据点的冲击性收尾**：1-3 字符的关键数字，作为句子的最后一个重音（`实际卖到中国的 H200 数量是 **0**`）
  - (c) **真正的结构性小标题**：一节下面有 ≥3 个并列小标题同款处理时（如 7.4 的"放弃/chokepoint/开门/持续投入"六条各自加粗作为小节头）
- 🔒 **硬性约束**：一节粗体处数 ≤ 3。不允许整句（> 10 字）加粗。自检时 Grep `\*\*[^*]\{10,\}\*\*` 找出所有长粗体，逐个改掉
- 📍 **背景**：Jensen Huang 第三节用户反馈"黑体字太多，不必要的去掉"。整篇回看，原稿每节平均 4-6 处粗体，实际有意义的 ≤ 2 处

## [2026-04-18] 辩论型文章结尾站队

- ❌ **错误示范**：长篇分析两派观点的文章，结尾一边倒
  - `X 说的是事实。Y 在赢一场假想的战争。`
  - `X 可能是有利益冲突，但他说的是事实。`
  - 只挑一方的金句做结尾 quote
- ✅ **正确做法**：结尾必须给两派各一段公道话，把问题重新框定为更本质的多轴问题
  - 结构模板：`回到开场` → `两边都说对了一部分` → `X 派没完全错（原因）` → `Y 派也没完全对（原因）` → `真正难的是在两者同时成立的情况下……` → `更诚实的问法是……`
- 🔒 **硬性约束**：文章涉及两派或多派观点辩论时，结尾至少有一段承认 A 派部分正确，一段承认 B 派部分正确，之后才收束到作者自己的判断。自检时问："拿掉这段承认 A、承认 B 的话，文章会不会变成替某一方打广告？" 如果会，说明站队太深
- 📍 **背景**：Jensen Huang 文章结尾初版偏护黄仁勋（"他说的是事实""鹰派在赢假想冷战"），用户反馈"经过了这样的长篇大论，再说一些公正的不站队的话"

## [2026-04-18] PPT 风格成文：结构骨架外露，缺乏叙事感

- ❌ **错误示范**：
  - 开头直接"先不讲术语。两个场景，你自己感受一下"然后甩两个场景块，像 PPT 翻页
  - 每一节像独立幻灯片：标题 → 要点 → 下一张。段落之间没有叙事过渡，读者感觉在看提纲而不是读文章
  - 过渡段用"看完这两个场景，你有没有发现一个规律？"这种教科书式设问，像老师在课堂上提问
  - 场景和论述之间缺乏温度，像在做功能演示
- ✅ **正确做法**：
  - 开头要有**读者代入感**：从读者自己的困惑切入（"你听说过 X、Y、Z 这些词吗？"），先建立共鸣再展开
  - 场景要**娓娓道来**，像在跟朋友讲一件事，有节奏有呼吸，而不是"场景一：""场景二："这种编号式陈列
  - 段落之间要有**叙事连接**，上一段的尾巴自然引出下一段的开头，读者感觉被牵着走而不是被翻页
  - 论述穿插在故事里，让读者在故事里"自己发现"规律，而不是作者跳出来宣布"你有没有发现一个规律"
- 🔒 **硬性约束**：写完后通读开头 3 段，问自己"这像是一个人在跟朋友聊天，还是像在做 PPT 演讲？"如果是后者，重写。开头必须有读者代入（问题、困惑、共鸣），不能直接甩内容块
- 📍 **背景**：Harness Engineering 文章初版开头直接"先不讲术语，两个场景"，用户反馈"开头生硬""PPT风格成文还是没有变化""根本不是故事娓娓道来的感觉"

## [2026-04-20] 戏剧化隐喻膨胀：视觉动词套抽象名词

- ❌ **错误示范**：
  - `[抽象名词] 被 [视觉动词] 了` 是中文 AI 最标志性句型：内核被掏空、秩序被击穿、格局被重塑、根基被撼动、底色被改写、边界被击穿、意义被解构、张力被放大
  - 抽象主语做拟人动作：时代在呼唤、历史在转向、技术在叩问、叙事在自我繁殖
  - 高危抽象名词反复点名（内核、底色、脉络、肌理、褶皱、场域、张力、势能、图景、毛细血管），单篇 ≥ 4 次即失声
- ✅ **正确做法**：
  - 戏剧动词换朴素动词：`秩序被击穿` → `规则失效了` / `规则不管用了`
  - 抽象主语换具体主语：`时代在呼唤新的范式` → `越来越多工程师开始用 X`
  - 高危抽象名词单篇内限 ≤ 3 处，且必须跟实指内容，不做空转
- 🔒 **硬性约束**：
  - 写完 Grep `被.*(掏空\|击穿\|撕裂\|重塑\|改写\|解构\|瓦解\|撼动\|折叠\|缝合)`，命中即改写
  - 段首出现"时代在 / 历史在 / 技术在 / 叙事在"等无生命主语的拟人动作，出现 1 次即改写
- 📍 **背景**：读者反馈"一看到'内核被掏空'就知道是 AI 文"。单个词无辜，但句式密度稍高全篇报废。把三个子模式（视觉动词套抽象、抽象主语拟人、抽象名词堆叠）合进一条，避免规则膨胀

## [2026-04-21] No back-translation of direct quotes

- ❌ **Wrong**: Translating content inside direct-quote marks from a rendered translation back into its original language without verifying the actual source-language text. Example: a Chinese article's 引号 around an English speaker's words; I translate those Chinese characters back into English without checking what the speaker actually said on the original podcast / press conference / paper.
- ✅ **Right**: For anything inside direct-quote marks (`"..."`, `「...」`, `> blockquote`), find the source-language verbatim via WebSearch before including it. If the quote is paraphrased or compressed by the Chinese author, drop the quote marks and render as indirect speech instead.
- 🔒 **Hard constraint**: Before starting any cross-language translation, Grep every `"..."`, `「...」`, and `> ` block in the source. For each, either (a) WebSearch the source-language verbatim and use it, or (b) unquote and render as indirect speech. Never translate the rendered version back to its original language.
- 📍 **Context**: Jensen Huang's "enriched uranium" / "woke up a loser" lines on Dwarkesh's podcast are English originals. The Chinese article's 引号 content was the author's compressed translation. First-pass English translation re-translated the Chinese back, which would have misquoted him. Caught before publish.

## [2026-04-21] English register and sentence rhythm

- ❌ **Wrong**:
  - Runs of 3+ short 5-to-7-word sentences in a row (staccato rhythm)
  - Sentences with 4+ commas or three stacked subclauses
  - Narrative paragraphs opening with `First, ... Second, ... Third, ... Fourth, ...` enumeration
  - Sentence fragments where a full clause is needed (e.g. "X, former official Y, now Z" with no verb)
  - Filler phrases: "in some respects," "that being said," "on the other hand," "to some degree," "in many ways"
  - Weak verb + adverb where a strong verb works (`said loudly` vs `shouted`)
- ✅ **Right**:
  - Alternate short (5-10 word) and medium (12-20 word) sentences; an occasional longer sentence for texture
  - Max 2-3 commas per sentence; above that, split or restructure with semicolon
  - Narrative connectors over numeric enumeration: "The biggest one is ..." / "A deeper problem is ..." / "And there's the paradox ..."
  - Strong verbs (pushed, anchored, flooded, dropped), not weak verb + adverb
  - Register target: The Economist / The Atlantic argument-driven long-form. Plain words, concrete nouns, active voice
  - Em dash `—` is allowed in English for rhythm (the `——` ban applies only to Chinese prose)
- 🔒 **Hard constraint**: After first draft of any English content, Grep `,[^,]*,[^,]*,[^,]*,` (4+ commas in one sentence) and rewrite each hit. Scan visually for runs of 3+ short sentences and merge one with a semicolon or restructure.
- 📍 **Context**: First English translation of the Jensen Huang article had too-long subclause-stacked sentences in some paragraphs and too-choppy 5-word sentences in others. User flagged: "sentences sometimes too long, sometimes too many commas, sometimes broken into too many short pieces."
