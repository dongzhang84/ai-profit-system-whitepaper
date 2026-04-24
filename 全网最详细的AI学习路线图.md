

说句不太尊敬的话，我反对这个问题下不少高赞答案的路线图。

大部分回答的通病是不问你的目标就一刀切，花大量篇幅讲述某些模型和算法的内部结构，却把 LLM 一句话带过，项目示例还在推一些十年前的教科书作业，中间还常夹带"限时免费"、"救你命的资料包"这类课程推广话术。更大的问题是，“报菜名”的现象严重，却没有宏观总体的把握。

庄子云：吾生也有涯，而知也无涯。以有涯随无涯，殆已！

你要学会：急用先学，活学活用！

我给你的路线图反过来：先定目标，再选方法，再挑一个能 ship 的项目，倒推要学什么。

简单介绍一下我自己。我本科物理方向，一直是年级第一。博士读的是天体物理，一度以为这辈子就做物理学家了，后来判断整个物理学科走进了死胡同，果断转 AI，做到美国大厂的算法工程师。我的 AI 全是自学，从最基础的线性回归到 CNN、Transformer，再到现在流行的 LLM Agent。没有 CS 背景、没有人带，全是自己边摸边学，走了六年。

这几年来我见过太多想自学AI的朋友，拿着一份看起来很全的路线图，最后卡在各种细节、教程、论文和项目里没出来。

所以今天这份内容不走完整路线图那套，只讲两个必须先回答的问题。

# 第一问：你学 AI 的目标是什么？

这个问题不先回答，后面全是浪费时间。大致上，你可能有以下四种目标之一：

- **大概知道一下**：你不打算以此为业，只是想跟得上行业话题，平时可以吹吹牛。几门 Coursera 公开课加几篇科普文就够（比如我这篇），不用往下读了。
- **研究算法（写论文 / 搞前沿）**：目标是进入AI领域的学术圈或工业实验室。路径跟下面完全不同，需要数学根基、阅读论文、做 novel contribution 的能力。更关键的是，你要攀上学术界的大佬，效果无限大于自己埋头学习。
- **找工作 · 算法岗**：要会公式推导、会调模型、会做实验。顶端的纯研究岗（顶校 PhD + novel research）门槛仍然很高，但只会调模型、不会工程化的中低端，2026 年已经不好找。
- **找工作 · 工程岗**：要会把模型塞进 production、会部署、会优化 latency。这个方向的人才缺口最大。

如果你真的想集中一段时间内学到一定的 AI 知识，并且最终可以落地，我建议大多数人走第四条，即 AI/ML 工程岗。工程岗需求比算法岗大一个量级，这个差距在数据上很直观：

全球层面，LinkedIn 美国市场实时数据显示 ML 工程类岗位在招 85,000+ 个，ML Research Engineer 27,000+ 个，纯 ML Researcher 只有 11,000+ 个，工程岗对研究岗大约 8:1。AI Engineer 在 LinkedIn 2026 "Jobs on the Rise" 榜单上位列全球增速第一。国内层面，纯研究型职位集中在百度研究院、阿里达摩院、字节 AI Lab、腾讯 AI Lab 这几家，全国加起来每年招聘名额只有几百到上千。部署 AI 的工程岗遍布几乎所有中大型互联网公司、金融、医疗、制造业。百度 2026 年 AI 扩招同比 +60%，其中绝大多数是能把模型落地的工程岗。

结构性原因很清楚：做 AI 基础研究的公司全球几百家，头部的研究公司估计就那几家；另一方面，部署 AI 的公司 2026 年已经是几万家。研究岗是漏斗顶端的一小撮，工程岗是漏斗下游的大盘。真正有付费意愿的公司要的是能 ship 的人。只会推导 AI 模型背后数学公式的博士，面试反而卡在工程关。

当然我说了不算，你具体的目标，当然要你自己来定。想清楚，谋定而后动，这才能分清主次。

# 第二问：你想写论文还是做项目？

你知道现在市面上存在多少 AI 文章吗？你知道 AI 的大部分文章有多不值钱吗？

光 arXiv 一家，2026 年 4 月一个月，cs.AI 板块收了 2,953 篇，cs.LG 板块 2,624 篇，两块加起来一个月 5500 篇以上，年化 6-7 万篇。再算上 CV、NLP、ML 各种 workshop 以及非 arXiv 渠道，再加上各大公司内部的papers，论文的实际数量已经到达天文数字。

即便是 NeurIPS 这种顶会，2025 年录取了 4,841 篇论文。听起来厉害，但只有 1.7% 的论文最终能拿到 1000+ 引用，16.5% 能拿到 100+ 引用。也就是 NeurIPS 录取的论文里 83.5% 一辈子的影响力不超过 100 引用，最常见的引用区间是 10-50。这是顶会的数字，arXiv 预印本的均值比这还低一档。顺便一提，GPTZero 扫过 NeurIPS 2025 全部 4,841 篇论文，发现 51 篇里一共 100 条 AI 编造的假引用漏过了同行评审。这是 NeurIPS，不是野鸡会议。

真相是 AI 领域的论文供给已经严重过剩。大部分你读到的"最新论文"两年后没人再提。换个数据集、换个 benchmark、调个超参、加个 loss 项，就能发一篇。

所以不管你是有导师带还是自学，我都推荐把做项目当主要目标。如果你的博士项目要求必须发论文才能毕业，那就按最低标准应付一下就行，别把项目时间让给论文。

我见过太多 AI 方向的 PhD，毕业时回头看，整个五、六年的博士生涯产出就是几篇没人读的垃圾 paper，此外啥都没有。五年、六年，你知道在 AI 领域意味着什么吗？2020 到 2026 这六年，AI 行业换了三代：BERT 微调、GPT 生成、RAG和Agent。每一代都把上一代的做法打翻重来。你花整段时间憋几篇水文，这不是浪费生命，什么是浪费生命？

项目，项目，项目。重要的事说三遍。

所以接下来的路线图，全部围绕"做项目"这个假设展开。

当然，你一定要说你的人生就是为了读paper，写paper，再读paper，再写paper，那也没办法拦着你。我接下来的话你不要读了，对你来说都是废话。

# 一、AI 究竟学什么：四大方向拆解

AI 这个词太大，不拆分就没法学，但也不能拆得太细，太细就成了报菜名，把没吃过山珍海味的小朋友吓跑。真正有规模、有明确工具栈、有对应工业界岗位族的方向，当前只有四个。

## 1.1 传统机器学习（Traditional ML）

这是 AI 最老牌的那一块，也是其他所有方向的地基。方法上以各种统计学方法为主，线性模型、树模型、集成方法那一堆，不需要一开始就钻进每个算法的数学细节。真正重要的是你能用它解决什么问题。

举几个具体例子。Kaggle 上的入门赛 Titanic，给你每个乘客的年龄、舱位、性别、家人数量，让你预测谁能活下来，这就是最经典的分类问题。House Prices 比赛给你房子的面积、地段、年份，让你预测成交价，这是回归。工业界里，银行拿你的流水和征信记录算一个"会不会逾期"的分数，保险公司拿你的病史算保费，电商平台给每个订单算一个"会不会被退货"的概率，底层都是这套传统 ML。

这一块在"看起来更酷"的方向面前显得朴素。CV、LLM、推荐系统话题性强、媒体曝光多，但工业界绝大多数的 AI 岗位目前还基本限制在传统 ML 的领域。风控、搜索排序的底层、表格数据预测、时间序列这些场景里，"谁也打不过 XGBoost 加特征工程"一直是行话。

当然事情正在悄悄变化。尤其今年，公司 AI 化（本质是 agent 化）的口号越来越响。要澄清的是，传统 ML 的应用场景并没有被挤走：风控依然在算逾期分，保险依然在算保费，电商依然在算退货概率。变的是围在这些模型外面的人。以前一个欺诈警报出来，要几个 risk analyst 看、审、过一道；现在 agent 读到警报直接冻账户、发短信给用户、调历史数据写处置报告。ML 模型还在原位产出分数和概率，被一层层吃掉的是 human-in-the-loop 的环节。

## 1.2 计算机视觉（CV）

CV 的故事要从 1980 年代末讲起。Yann LeCun在贝尔实验室做手写数字识别，用的是反向传播加卷积网络，美国邮政当年就用这套系统自动分拣信封上的邮编。下一个大转折点在 2009 年。斯坦福的李飞飞（Fei-Fei Li）牵头做出 ImageNet，一个有 1400 万张带人工标注的图像数据集。她的贡献不是某个具体算法，而是给整个深度学习提供了"足够的燃料"。2012 年 AlexNet 在 ImageNet 图像分类比赛上碾压传统方法，深度学习这一波工业革命从这里真正起步。

后来 CV的算法在2016 年 DeepMind 的 AlphaGo 在围棋上击败李世石，一时间成为大新闻。医疗影像识别在几类癌症筛查和眼底病变检测上达到甚至超过专业放射科医生的水平。自动驾驶这一整个产业靠的是多路摄像头加 CV 模型做实时目标检测、车道线识别、障碍物判断。过去十年特斯拉、Waymo、Cruise 几乎全是 CV 工程师的主场。

到了 2026 年，CV 的焦点已经从"识别"转向"生成"。Stable Diffusion、Midjourney、DALL-E、Flux 这一批工具底层当然还是 CV 的延伸，仍然需要理解图像的像素分布、结构、风格，只是目标从"判断这是什么"变成了"画出一张符合描述的图"。技术栈的重心也从过去的 CNN，转到了 Vision Transformer（ViT）和 diffusion models 这两条主线（这些菜名，我们后面会说到）。

所以今天学 CV 要想清楚：经典的分类、检测、分割那条线已经不是主流就业方向，除非你锁定医疗影像、自动驾驶、工业质检、机器人视觉这几个仍然有硬需求的垂直行业。更火的是 CV 和 LLM 结合的多模态，以及图像生成方向。但后者作为纯"工程岗"的饭碗主要集中在几家做 image generation 产品的公司，岗位池比 传统机器学习和LLM （下一小节）本身窄得多。

## 1.3 大语言模型（NLP / LLM）

这一块的分水岭非常清晰：2022 年 11 月底 ChatGPT 问世（背后是 GPT-3.5），之前和之后是两个世界。

在 ChatGPT 出现之前，NLP 是一堆互相隔离的子任务拼起来的学科：分词、词性标注、命名实体识别、情感分析、机器翻译、摘要、问答、对话。每一个任务对应一套专用数据集、一个专用模型、一支专用团队。工业界的 NLP 工程师日常就是给某个特定任务标数据、调 BERT 模型、抠一两个百分点的准确率。这个时代的代表性工作是谷歌 2018 年发布的 BERT 和它一大家子衍生模型。

ChatGPT 之后，这堆任务几乎全被一个通用大模型收编了。翻译、摘要、问答、情感分析、甚至写代码、做数学推理，今天都是同一个 LLM 接不同 prompt 就能完成。以前一个团队半年做的事，现在一个工程师一个下午用 API 就能跑通。传统 NLP 这个学科实际上已经被 LLM 吞并，只剩少数边角任务（比如垂直领域的规则系统）还保留独立形态。

这是 2026 年最火的方向，没有之一。热度不是凭感觉说的，有几条量化信号可以印证。LinkedIn 2026 "Jobs on the Rise" 榜单全球增速第一的岗位是 AI Engineer，基本就是 LLM 工程师。ChatGPT 全球周活用户已经到 8 亿量级，OpenAI 最新估值 5000 亿美元，Anthropic 估值 1000 亿美元以上，国产阵营 DeepSeek、Qwen、智谱、Kimi、百川全部在高速扩张。过去两年美股涨幅里绝大多数头部公司都和 LLM 直接相关。国内中大型互联网公司几乎每家都在搭自己的大模型团队。

岗位需求、薪资水平、创业机会这三条线，这个方向全部压过其他任何方向。如果你是零基础转 AI 且目标是找工作，我直接从这里切入，别的方向真需要时再补。

## 1.4 推荐系统（Recommendation Systems）

这是在中国互联网语境下最大的 AI 应用，但国外的 AI 课程体系里经常轻视它。抖音、小红书、美团、拼多多、淘宝、知乎，你每天打开的所有 app 背后，把内容或商品端到你眼前的都是一套推荐系统。它的学术根子在"信息检索"这个子领域（arXiv 的 cs.IR 分类），但工业界用的框架早就和纯学术分道扬镳，自成一套工具栈。

一个现代推荐系统通常是四层流水线：召回在千万级候选里捞出几千条，粗排筛成几百条，精排打分产出几十条，最后重排按业务策略排列。每一层都有自己的模型，双塔网络、深度兴趣模型，这两年又吸收进来不少 Transformer 结构。工程上还要处理 online learning、特征服务、A/B 测试平台这一大摞纯工程问题。顶尖推荐系统团队的综合工资经常比 CV 和 NLP 研究岗更高，因为推荐效果直接和公司 DAU 与 GMV 挂钩。

中国互联网大厂"算法工程师"这个 title，一半以上实际做的就是推荐。如果你看到某个 JD 写"熟悉 embedding、双塔、ctr 模型"，那就是推荐岗。这是我最建议中国读者认真考虑的第四条主线，在国内的落地机会甚至比 LLM 本身还多。

## 1.5 其他你可能听说过的方向，报些菜名

下面这几个方向你一定听说过。它们各自都有独立的学术社区、顶会和工业玩家，算得上 AI 的独立分支，只是规模比前面四大主线小一档。

- **语音（Speech）** · 语音识别（ASR）、语音合成（TTS）、声纹、语音克隆。学术上有 Interspeech、ICASSP 这些独立顶会，工业界有 OpenAI Whisper、ElevenLabs、科大讯飞这批代表玩家。岗位池比 CV 小，但在智能客服、数字人、有声书、播客生成这些场景一直有稳定需求。
- **机器人与具身智能（Robotics / Embodied AI）** · 学术上有 ICRA、IROS、CoRL 这些顶会，工业界在 2025-2026 集体爆发：Figure AI、Physical Intelligence、Boston Dynamics、Tesla Optimus、宇树、智元、银河通用这一批。入行门槛高（需要真实硬件经验），但天花板也高，对机械、控制、自动化背景过来的人是自然的延续。
- **AI for Science** · AI 在科研领域的应用。DeepMind 的 AlphaFold 拿了 2024 年诺贝尔化学奖，相关还有 AlphaMissense（基因致病性）、材料发现、气候建模、天体物理数据分析、数学定理证明（AlphaProof）。对有理工科博士背景的人来说，这是一条很自然的切入路径：用本行学科的专业知识加 AI 工具即可。
- **AI 安全与对齐（AI Safety / Alignment）** · 学术社区独立（Alignment Forum、NeurIPS safety workshops），工业界玩家是 Anthropic、OpenAI safety team、DeepMind alignment team，以及 METR、Redwood、Apollo 这些独立研究机构。岗位少但每个都很硬核，适合走纯研究路线。

这四个方向的共同点是规模比前面四大主线小一个量级，岗位池更窄，入行通常需要特定的学科或产品背景做铺垫。一旦你的兴趣和背景能对上某一条，它会是非常好的差异化选择。

# 二、倒三角思考：从方向倒推学什么

**谋定而后动。** 

学 AI 最大的一笔浪费是漫天无边地乱学：哪个新概念火就补一下，哪篇新论文热就读一遍，一年过去手里还没落地一个能跑的东西。正确的顺序是先把定位敲定。方向选一个，岗位选一条，然后再决定要学什么。比如你决定"做 LLM 方向、面向工程岗"，知识的边界就清晰了，边界之外的先放着。

**项目驱动学习。** 

AI 这一行的知识是做会的，光看不会。模型接口每半年一换、框架每季度一升、最佳实践随时在改，你花三个月啃完一本教材，书里的示例代码可能已经跑不通了。我坚持项目驱动学习（project-based learning）的原因就在这里：通过动手做一个具体能跑的东西来掌握需要用到的知识。大部头的书和长视频教程是查漏补缺用的工具，不应该当成学习的主路。

**三三制节奏。** 

光说"做项目"还不够，项目和项目之间需要能力阶梯的概念，不然容易反复做同一个难度级的东西原地打转。在这个方面，我特别喜欢 101 元帅的三三制方式：一个战斗小组三人配合前进。放到学习上，每三个项目打磨一层能力，然后整组推进到下一层。每一层都是一个具体可验证的技能落地点。

**Vibe Coding + 费曼学习法。** 

做项目一行代码都不会写怎么办？用 Vibe Coding：用自然语言描述你想要什么，让 Claude 或 Cursor 帮你写，再一起迭代。但 vibe coding 有副作用，容易跑通一个东西其实不懂它在做什么。配上费曼学习法校验：写完合上编辑器，用白话把这段代码完整讲一遍，讲不下去的地方就是要补的知识。vibe 让你快速出活，费曼让你真正内化。

下面以"LLM 方向 + 工程岗"为例，把这套阶梯摆开。


# 三、三三制的项目学习法（示范）


## 3.1 第一层：运用 API

这一层的目标是能独立用 LLM API 搭一个别人能访问的 app。但动手之前，先理解这一层的学习方式：自主学习。

自主学习不是翻开一本 Python 教程从第一页看到最后一页，也不是把一份 API 文档从头啃到尾。那是书本时代的打法，2026 年已经过时了。今天的做法是带着问题去找 AI 对话。AI 是你的"问题提示机"，你每抛一个问题，它就应该带你再往深追三四层。

作为启发者，我在下面每个项目下面都埋了几个由浅入深的问题。别急着动手敲代码，先把问题和 AI 聊透，聊到能用费曼法讲给完全不懂的朋友听，再动项目。

### 项目 1 · 命令行 chatbot

任选一个大模型，调用一个 LLM API，写一个最简单的命令行聊天工具。目标是打通"你的程序 → 网络 → 模型服务器 → 回复你"这条完整链路。

带着这些问题做：

1. 你打开 ChatGPT 和模型聊天的时候，背后到底在哪里运行？服务器、你的电脑、模型各自扮演什么角色？
2. API 这个词在 AI 出现之前就存在了，它在别的场景里一般干什么？为什么 LLM 时代顺手借来用？
3. 一次 API 调用里，你的程序和服务器之间到底传递了什么？为什么要打包成 JSON 这种格式？
4. 为什么 Python 成了 AI 的默认语言？如果我不会 Python，能先把 API 调通吗？
5. system prompt、user prompt、assistant 这三个角色为什么要分开？如果都混在一起会怎样？
6. 当我让模型连续回答几个问题时，它其实"记得"我之前说过什么吗？多轮对话靠什么机制存续？

### 项目 2 · Web 界面 + prompt engineering

把命令行 chatbot 套上 Web 界面，让别人在浏览器里和它聊天。这个项目会第一次把 prompt engineering 和前端这两个话题同时推到你面前。

带着这些问题做：

1. Prompt Engineering (PE) 到底是"工程"还是"玄学"？为什么差不多一段话，换一种写法，模型的回答质量能差很多？
2. 除了换写法，还有哪些技巧能让模型更听话？few-shot 示例、chain-of-thought、角色设定、结构化输出分别解决什么问题？
3. 你能自己整理出一套可复用的 PE 原则吗？试着让 AI 陪你把它写成一份 checklist。
4. Web 界面有哪些框架可以用？最轻的是一个 HTML 文件加 fetch，中间有 Gradio、Streamlit，重的有 Next.js、Vue、React。这些分别适合什么场景？
5. 这些 Web 框架和 AI 开发的关系是什么？为什么做 AI 应用的人也要懂一点前端？
6. 用户在浏览器里输入一句话，这句话怎么从浏览器一路送到 OpenAI 服务器，再把回复带回来？中间经过几跳？

### 项目 3 · 部署上线

把 app 部署到一个公网可访问的地方（Vercel、Netlify、Railway 这类 serverless 平台），让真的用户能用、能花钱、能给你反馈。

带着这些问题做：

1. 一个完整的 LLM app 从用户打开页面到拿到模型回复，中间涉及哪些组件？能不能亲手画一张流程图？
2. 一个完整的 chatbot 的 sequence diagram 长什么样？请求经过多少跳、每一跳做什么？
3. 部署到 Vercel、Modal、Railway 这些平台上，"serverless" 到底 serverless 在哪里？和传统 VPS 部署有什么差别？
4. API key 为什么不能提交到 git？如果真泄露了会发生什么？怎么安全地管理它？
5. streaming 返回的用户体验为什么比"等全部生成完再返回"好？底层是怎么实现的？
6. 你怎么知道自己的 app 被用了多少次、花了多少钱？监控该看哪些指标？

### 带着问题去读几本书

问题聊透了、项目做完了，这时候你已经用自己的概念搭起一个框架。这时候再挑几本书去系统补完。注意别从第一页翻到最后一页地顺读，带着你已经存下的具体问题去索引，哪一章能回答哪个问题就读哪一章。

- **《AI Engineering》· Chip Huyen**（2025, O'Reilly）· LLM 工程岗事实上的入门圣经。Chip Huyen 自己是顶级 ML 工程师，书覆盖从 prompt engineering 到 RAG、fine-tuning、评估的全链路
- **《Hands-On Large Language Models》· Jay Alammar & Maarten Grootendorst**（2024, O'Reilly）· Jay Alammar 以图解 Transformer 系列博客闻名，这本书把 LLM 的概念用可视化方式拆开，适合补直觉
- **《Prompt Engineering for LLMs》· John Berryman & Albert Ziegler**（2024, O'Reilly）· GitHub Copilot 团队写的 prompt engineering 系统化手册，把项目 2 里"玄学"的部分讲得很扎实
- **《Designing Machine Learning Systems》· Chip Huyen**（2022, O'Reilly）· 传统 ML 工程经典，讲 ML 系统怎么上线、监控、迭代。很多原则直接可以移植到 LLM app

### 基础知识回补

做到这一层你会发现 API 这件事情坐在几个更基础的 web 和编程概念上。下面 5 条是值得扫一眼"地图级"的基础。

- **HTTP 协议** · 所有 API 都跑在 HTTP 上。入口：MDN Web Docs 的 HTTP overview（developer.mozilla.org），读 overview 加 request/response 那几页即可
- **JSON** · API 里数据交换的默认格式。入口：json.org 官方简介加 Python json 标准库文档，半小时搞定
- **Python 基础** · AI 时代事实上的母语。入口：Corey Schafer 的 YouTube Python 系列（免费、系统），或者《Python Crash Course》（Eric Matthes 著），挑一个过一遍
- **Git 与版本控制** · 部署和协作都绕不过。入口：《Pro Git》免费中文版（git-scm.com/book/zh/v2），读前两章就够
- **基础 web 架构** · 前端/后端、client/server、DNS、HTTPS 这套概念。入口：MDN 的 "How the web works" 入门教程，一小时过完

做完三个项目、书里的关键章节翻过一遍、5 条基础也有个地图级印象，这一层就通关了。通关标准：把部署版本讲给另一个做技术的朋友听，他能听明白从"用户按 Enter"到"AI 返回答案"中间发生了什么。

## 3.2 第二层：能搭一个 RAG 系统

这一层的目标是让 LLM 能接入外部知识，不再只能依赖训练时内置的那些数据。学习方式延续第一层：每个项目下先带着问题去和 AI 对话，问透之后再动手。

### 项目 4 · 单文档 RAG

选一本书或一份 PDF 报告，用 embedding 模型（OpenAI embeddings 或 bge-small 等）配合向量数据库（ChromaDB、Pinecone 等任选），搭一个能对这份文档问答的简单 RAG。打通"文档 → 切片 → embedding → 向量库 → 检索 → 塞回 prompt → 回答"这条完整链路。

带着这些问题做：

1. 为什么不能直接把整本书塞进 prompt 让模型回答？
2. Embedding 到底是什么意思？一段文字怎么就变成了一串数字？这串数字又怎么表达"意思"？
3. 为什么可以用向量的距离（余弦相似度、欧氏距离）来衡量语义相似度？
4. 向量数据库是什么？和你熟悉的 MySQL、PostgreSQL 相比，它解决了后者解决不了的什么问题？
5. 一次完整的 RAG 查询里，embedding、向量检索、把检索结果塞回 prompt 这三步分别在做什么？
6. 为什么要绕这么一圈，而不让 LLM 自己直接去文档里找答案？

你可能不知道什么叫 embedding，甚至不知道什么叫 MySQL。这是好事，你遇到了可以学习的东西！可以去查书、查文献、查视频教程了。几个省时间的入口：

- Jay Alammar 的博客《Illustrated Word2Vec》· embedding 最好的直觉入门，一个下午能过完
- 3Blue1Brown 的 YouTube 系列《线性代数的本质》· 理解向量距离为什么能衡量语义相似
- MySQL 或 PostgreSQL 的官方 tutorial · 半天补完 SQL 和数据库的底层概念
- 第一层推过的《Hands-On Large Language Models》· 里面讲 embedding 的章节这里也直接适用

自主学习的套路是挑你卡住的那一个概念，找一份合适的材料读透它，别想着把整本教程从头翻到尾。

### 项目 5 · 复杂 RAG

在项目 4 的基础上加上 chunking 策略对比（按段落、按 token、按语义）、多路召回（dense 加 BM25 keyword）和重排模型（cohere rerank 或 bge-reranker 等任选），用 hit rate、MRR 这些指标量化你的检索质量。

带着这些问题做：

1. Chunking 为什么会成为 RAG 的关键决策点？把一个文档切成 128 token 的小块和切成 1024 token 的大块，检索效果会差在哪里？
2. 按段落切、按 token 切、按语义切，这三种策略各自的优劣是什么？什么样的文档应该用哪种？
3. 为什么单靠 embedding 向量检索不够？把 BM25 这种"老式"的关键词检索加回来，它补的是什么？
4. 重排（reranking）在做什么？它和第一轮检索有什么本质区别？为什么多这一步常常能显著提升效果？
5. hit rate、MRR、nDCG 这几个检索指标分别衡量什么？如果只能盯一个指标，你会选哪个？
6. "recall-precision 平衡"在 RAG 里怎么体现？多返回几条候选和精确返回少几条，各自的代价是什么？

什么？你感觉这里又报了一大堆菜名？你有能力让自己获得"最小认知层"吗？也就是抓住这层优先级最高的知识，忽略掉别的细节。比如我上面提到的 hit rate、MRR、nDCG，第一次做 RAG 你完全可以先跳过。

但是有两个词你必须懂：precision 和 recall，以及它们之间的 tradeoff。不需要回头翻大部头的统计学教材，几份轻量资料就够：

- 维基百科《Precision and recall》条目 · 看最上面的 Basic concepts 段落就够，15 分钟搞定
- StatQuest（Josh Starmer）的 YouTube 频道 · 统计概念可视化讲解界的头牌，搜 precision、recall、sensitivity、specificity 都有专门的短视频
- 或者最省事：直接问 Claude 或 ChatGPT"用一个医学检测或垃圾邮件过滤的例子讲 precision 和 recall，再讲它们为什么存在 tradeoff"，让它讲完再出三道题考你

"最小认知层"在这一步就是 precision、recall 两个词和它们之间的 tradeoff。至于 hit rate、MRR、nDCG 是怎么精确定义和计算的，等真的卡在检索质量、需要量化比较两个版本的时候再回头补。那时候带着具体痛点去学，比提前啃一遍快十倍。

### 项目 6 · 垂直领域 RAG 产品

选一个你熟悉的 domain，比如你自己的笔记、公司内部文档、某个行业知识库，把 RAG 做到能让目标用户真的用起来，能接住真实反馈，能迭代。

带着这些问题做：

1. 把一个"能 demo 的 RAG"变成"能让真人用的产品"，中间会冒出哪些问题？从 10 个用户扩到 100 个会发生什么变化？
2. 当用户说"检索不准"或"模型胡说"时，你怎么定位问题出在哪一步？是 chunking、检索、还是生成？
3. RAG 里的 hallucination 和纯 LLM 的 hallucination 有什么不同？怎么让模型在"检索结果不够好"时老实说"我不知道"？
4. 真实用户的查询长什么样？和你自己在 demo 时想到的问题有什么差距？这个差距怎么缩小？
5. RAG 的成本结构是什么？embedding、检索、生成三段各占多少钱？延迟瓶颈通常在哪一段？
6. 一个 RAG 系统从 v1 到 v10 的迭代路径上，哪些参数是你该持续调的，哪些是你一开始就应该锁死的？

在这一层你会学到一项埋头死读书永远学不会的技能：和客户交流。从这里开始，产品迭代不靠你自己拍脑袋，靠客户反馈驱动。

什么？你说你找不到客户？你说自己内向，开口找人聊天就想钻地缝？那换一个打法：让内向的你学会在暗处偷窥。去 Discord、微信群、小红书、X、Reddit 搜你的产品关键词，看别人怎么讨论它。那些自发的吐槽、抱怨、求助、推荐，比一次正襟危坐的"您觉得我产品怎么样"访谈真实十倍。这也是客户反馈，只不过你是潜伏着收集的。

### 带着问题去读的几本书

这一层的概念梯度比第一层陡一些。项目做到中期会积累出很多具体疑问，这时候翻书最划算。仍然是索引式读，带着问题去找答案。

- **《AI Engineering》· Chip Huyen**（2025, O'Reilly）· 第一层里也推过。RAG 那一章是整本书最精华的章节之一，把常见的坑和解法列得很全
- **《Relevant Search》· Doug Turnbull & John Berryman**（2016, Manning）· 经典信息检索教科书，RAG 的检索层本质上是信息检索的延伸，BM25、重排、relevance 这些概念在这里讲得最扎实
- **《Building LLMs for Production》· Louis-François Bouchard & Louie Peters**（2024）· 偏 production 的视角，讲 RAG 从原型到上线要处理的那些工程问题
- **LlamaIndex 与 LangChain 官方文档**· 严格说不是书，但对 RAG 这一层，这两个框架的文档和 cookbook 才是最一线的教材。配合上面的书一起翻

### 基础知识回补

做到这一层你会发现 RAG 不是凭空而起，它坐在几门成熟学科的肩膀上。下面 5 条是跟 RAG 最直接相关的基础，每条给一个最省时间的入口，别陷进去读大部头。目标是建立"地图级"的理解，真卡住的时候带着具体痛点回来找对应章节。

- **信息检索（Information Retrieval）** · RAG 的 "R" 完全长在这门学科上。入口：《Introduction to Information Retrieval》（Manning、Raghavan、Schütze，Stanford 免费读 nlp.stanford.edu/IR-book）
- **线性代数 · 向量距离与维度诅咒** · 理解"向量距离为什么能表示语义"和"高维空间里距离为什么会失真"。入口：3Blue1Brown 的《线性代数的本质》YouTube 系列，再加一篇维基 curse of dimensionality 扫完
- **近似最近邻搜索（ANN）** · 向量库能在百万条向量里毫秒级返回，核心算法是 HNSW、IVF、LSH 这几种。入口：Pinecone 官方博客的 ANN 系列（pinecone.io/learn），工程角度讲得最清楚
- **对比学习（Contrastive Learning）** · 你用的 OpenAI embeddings / bge / voyage 这些 embedding 模型都是用对比学习训出来的。入口：SBERT 项目主页（sbert.net）加 SimCSE 原论文（arxiv 2104.08821）
- **向量数据库 vs 传统数据库** · 为什么 PostgreSQL 加 pgvector 能做 RAG，但专用向量库在大规模下更强？根源在存储和索引的假设差异。入口：pgvector 官方 README，看它支持的索引类型就理解

做完三个项目、书里的检索章节翻过一遍、上面 5 条基础也补了个地图级印象，这一层就通关了。通关标准：把项目 6 的系统讲给另一个做技术的朋友听，他能听明白用户一次查询经过的 7-8 个组件各自在做什么、每一步可能怎么出错。

## 3.3 第三层：能写 Agent

这一层的目标是让模型能替你执行任务。学习方式延续前两层：每个项目下先把问题和 AI 问透，再动手。

### 项目 7 · Function Calling 入门

写一个能调 3-5 个工具的 agent：查天气、算账、搜邮件、查本地数据库都行。打通"LLM 看到问题 → 决定调哪个工具 → 调完拿到结果 → 把结果写成自然语言返回"这条最基础的 agent 链路。

带着这些问题做：

1. "Agent" 这个词最近有被滥用的倾向，到底什么叫 agent？它和普通 chatbot 的本质区别在哪里？
2. LLM 本身只会出文字，它怎么"调用"一个外部工具？function calling 背后到底发生了什么？
3. 你给 LLM 的工具定义（tool schema）里的几个字段（name、description、parameters）分别影响什么？写得好和写得潦草，模型的调用成功率能差多少？
4. 模型偶尔会选错工具，或者把参数填错。你有什么办法能在代码里接住这种错误、让它自己重试？
5. function calling 和"让 LLM 直接用 Python 写一段代码然后执行"是同一件事吗？各自适合什么场景？
6. 一个最简单的 agent 从接到问题到返回答案，中间会发生几步模型调用、几步工具调用？能不能亲手画一张流程图？

### 项目 8 · 多步 agent

让 agent 能做 planning、执行、反思、重试的完整循环，而不只是一次 function calling。参考 ReAct、Reflexion 这类经典范式，做一个你自己场景下能跑通的版本（写作助手、代码修改助手、deep research agent 都行）。

带着这些问题做：

1. ReAct 这篇 2022 年的论文提出的核心思路是什么？为什么"让模型边思考边调用工具"比"先想完再调"效果好？
2. Reflexion 在 ReAct 之上又加了一层"反思"。它具体反思什么？和直接重跑一次相比，反思带来的增量在哪里？
3. 一个 agent 在 planning-execution-observation-replan 的循环里，怎么判断"该停了"还是"该继续"？死循环怎么避免？
4. 多步 agent 的成本很容易翻好几倍。一次任务平均调用 5 次模型还是 50 次？哪些步骤是你能省掉的？
5. 当 agent 跑出一个错误结果时，你怎么回溯它的决策轨迹？为什么 logging 和 tracing 在 agent 系统里比在单轮 chatbot 里重要得多？
6. 同样一个任务让 GPT-4、Claude、DeepSeek 各自跑一遍 agent loop，你会发现它们的"决策风格"差别很大。这说明什么？

### 项目 9 · 多 agent 协作

搭一个场景，让 2-3 个不同角色的 agent 协作完成一个复杂任务。比如一个负责检索资料、一个负责写初稿、一个负责校对和修订的协作链。

带着这些问题做：

1. 为什么要把一个任务拆给多个 agent 做，而不让一个"更强"的 agent 独立搞定？拆分到底带来什么优势？
2. 多个 agent 之间怎么交流？共享同一份 memory 好，还是通过消息传递好？各自有什么坑？
3. 协调模式有哪几种经典范式（hierarchical 调度、debate 辩论、sequential 串联、parallel 投票）？什么任务适合什么模式？
4. 两个 agent 互相在等对方先动，或者在某一步反复纠结不往下走，这种"死锁"怎么识别和打破？
5. 多 agent 系统比单 agent 的 cost 高、latency 长、debug 难。什么样的任务配得上这些代价？
6. 现在很多"multi-agent"宣传本质上是一个 orchestrator agent 调几个专家 agent。这算真正的多 agent 吗？真正的多 agent 应该长什么样？

### 带着问题去读的几本书

Agent 领域严格意义上的"经典书"还不多，更多养分来自论文和工程博客。下面 4 份是做 agent 项目必过的材料，都不长。

- **Lilian Weng 的博客《LLM Powered Autonomous Agents》**（2023）· 原 OpenAI 研究员写的 agent 综述，一篇博客相当于半本书，agent 领域的入门圣经
- **Anthropic 工程博客《Building effective agents》**（2024）· 一线团队的实战建议，非常反炒作，专门治"堆 agent 不如堆 prompt"的毛病
- **《AI Engineering》· Chip Huyen**（第一层推过）· Agent 章节单独拎出来也是这本书最精华的部分之一
- **LangGraph 官方文档**· 主流 agent 编排框架，文档本身就是一份 agent 工程教材。比抽象讨论更值得花时间

### 基础知识回补

这一层的基础比前两层深一档，因为 agent 这个词在 LLM 之前就有几十年的研究传统。下面 5 条是值得扫一眼"地图级"的基础。

- **经典 AI 的 agent 与 planning** · agent 这个概念 classical AI 从 1950 年代就在研究。入口：Stuart Russell & Peter Norvig《Artificial Intelligence: A Modern Approach》里的 Agent 和 Planning 两章，别通读全书
- **强化学习基础** · MDP、policy、reward、exploration/exploitation 是所有 agent 的底层语言。入口：Sutton & Barto《Reinforcement Learning: An Introduction》前三章（网上有免费 PDF）
- **JSON Schema 与类型系统** · function calling 的底层就是 schema。入口：json-schema.org 官方文档加 Pydantic 官方入门教程
- **可观测性（Observability）** · tracing、logging、metrics 是 agent 系统最大的工程痛点。入口：LangSmith 或 Langfuse 任选一个的官方文档，里面讲 agent 为什么需要 tracing 最接地气
- **分布式系统与消息传递** · 多 agent 本质是分布式系统，actor model、消息队列、一致性这些概念会反复出现。入口：Martin Kleppmann《Designing Data-Intensive Applications》第 1-4 章

做完三个项目、材料扫过一遍、5 条基础有个地图级印象，这一层就通关了。通关标准：把项目 9 的多 agent 系统讲给另一个做技术的朋友听，他能听明白你为什么选这套协作模式、每个 agent 的职责边界在哪里、整个系统在哪些地方可能失控。

## 3.4 三三制小结：做完前三层你获得了什么

前面讲过三三制在每一层内部的用法（三个项目打磨一层）。它还有一个更高阶的应用：**每走完三层，停下来思考一次**。不思考的人只是在做项目，思考的人在真正积累。

做完第一、二、三层之后，你的能力画像应该是这样一个具象的形象：

- 你能独立用 API 搭一个能上线的 LLM app
- 你能给它接入外部知识，搭出企业级的 RAG 产品
- 你能让它替用户执行多步任务，甚至让几个 agent 协同干活

换成市场话语：你的简历和项目集合已经足够让你进入绝大多数国内外 LLM 工程岗的面试池，也足够支撑一个自己的 indie AI 产品。去真实 SaaS 市场里看一眼，过去两年冒出来的 AI 产品有相当比例的复杂度就停留在这三层之内。

这时候停下来问自己几个问题：

1. 这三层里哪一层我是最喜欢的？哪一层让我痛苦最少、做项目时间过得最快？
2. 我做过的三到六个项目里，有没有哪一个是真的让身边人用起来了？如果没有，为什么？
3. 我现在能不能用这三层的组合做出一个有人愿意付钱的产品？还不能的话差在哪里？是技术、选题、还是执行？
4. 我下一步的目标是什么：继续深化工程（进第四层）、all-in 一个产品、去找一份工作、还是换方向？
5. 过去几个月里我最大的收获和最大的后悔分别是什么？把这两个答案合在一起，能告诉我下一步最应该做什么。

这一步想清楚之后，下一步要分人。继续往上走会分叉：

**如果你想理解 LLM 背后的模型原理**，不愿意被别人一问就一问三不知，那下一层的重点是 Transformer 架构学习，继续走项目驱动路线，别陷进去啃 paper。

**如果你想深化工程岗的技术栈、建立更大的工程壁垒**，再上面两层带你往下走：数据和训练一套、推理和 Production 一套，这才是工程护城河真正落地的地方。

多数有野心的读者两者都要。既要懂一点黑盒子里在发生什么，也要把工程护城河做深。下面按"两者都做"的路径排：第四层走 LLM 原理（偏理论，但依然项目驱动），第五、第六层工程深化。走完这三层，你就是能同时进 research 面试房和工程 staff 面试房的那种人。

## 3.5 第四层：LLM 背后的原理

这一层的目标是知道"黑盒子里到底在做什么"。不追求发论文级的深度，但要让你在面试和工程决策里，不会被"你对 attention 怎么理解"这种问题难住，同时给第五、第六层的工程深化打下理解底座。方法依然是项目驱动，不啃 paper 啃代码。

### 项目 10 · 手搓一个 mini-Transformer

从零用 PyTorch 写一个小型 Transformer（GPT 风格，约 100-200 行代码），在莎士比亚数据集或任何小语料上训练，让它能生成出像那么回事的文本。Karpathy 的 nanoGPT / minGPT 是最好的参考。

带着这些问题做：

1. PyTorch是什么？
2. Transformer 之前主流的是 RNN / LSTM。Transformer 出来之后为什么一举取代了它们？本质上解决了什么问题？
3. self-attention是什么？
4. positional encoding 是什么？
5. 训练时模型用 causal mask（只看前面的 token），推理时每次只生成一个 token。为什么训练和推理的流程不完全对称？
6. 你的 mini-GPT 训完 loss 从 10 降到 2，它到底学到了什么？能不能分析出一两种它"记住"的模式？

### 项目 11 · Attention 可视化

给你训好的（或任何开源的）小 Transformer 做 attention 可视化。在一段文本上跑 forward，把每一层每一头的 attention weights 画出来，观察模型在"看"什么。

带着这些问题做：

1. 不同层的 attention 为什么看起来完全不一样？浅层和深层分别关注什么？
2. 有些 head 像在做"下一个词预测"，有些像在做"回指消解"，有些似乎什么都没学到。这种分化为什么会发生？
3. Anthropic 提出的 induction head 指的是哪一种 attention 模式？为什么被认为是 in-context learning 的关键？
4. 如果把某个看似重要的 attention head 权重随机化（ablation），模型输出会怎么变？为什么 ablation 是理解大模型的核心工具？
5. 对一个真正的大模型做 attention 可视化比小模型难得多，为什么？logit lens、activation patching 这些替代手段各自补了什么？
6. Mechanistic Interpretability 这个方向具体在做什么？和传统 XAI（explainable AI）有什么区别？

### 项目 12 · 从头训一个 tokenizer

给你手头的数据（中文古文、代码、法律文档任选），从零训练一个 BPE tokenizer，和 GPT-4 或 Claude 的 tokenizer 对比同一段文本的切分结果。

带着这些问题做：

1. Tokenization 为什么不走 character-level 或 word-level？BPE 到底为什么赢了？
2. BPE 训练过程的每一步在做什么？从字符出发、不断合并最高频 pair，为什么最后会收敛出 "ing" / "##tion" 这样有意义的片段？
3. 你的 tokenizer 切中文和 GPT-4 的 tokenizer 切中文，差在哪？为什么中文在很多模型上 token 效率明显比英文差？
4. 为什么 context window 说的是 "128K token" 而不是 "128K 字符"？tokenization 是不是模型"有效容量"的决定因素？
5. 模型遇到训练里没见过的词（OOV），BPE 怎么处理？和 word-level tokenizer 的 `<unk>` 相比好在哪？
6. tokenizer 一旦训好就很难替换，这带来了什么 lock-in 后果？GPT-4 换 tokenizer 的代价会有多大？

### 带着问题去读的几本书

LLM 原理这一层，好资料集中在论文 + 交互式可视化 + 开源实现，书反而不多。

- **Karpathy 的 "Let's build GPT: from scratch" 视频系列**（YouTube）· 2 小时手搓 GPT，整个 AI 圈公认的启蒙课，看完项目 10 直接能做
- **《The Illustrated Transformer》· Jay Alammar**（博客）· 最好的 Transformer 图解，十年老博客，今天依然是入门首选
- **Anthropic 的 Transformer Circuits Thread**（transformer-circuits.pub）· Mechanistic Interpretability 的权威材料库，项目 11 的主要参考
- **《Build a Large Language Model (From Scratch)》· Sebastian Raschka**（2024, Manning）· 想看一本正经书就这一本，用 PyTorch 从零实现 GPT，和项目 10 互为补充

### 基础知识回补

- **深度学习基础** · 反向传播、梯度下降、优化器（SGD、Adam、AdamW）、loss。入口：3Blue1Brown 的《深度学习》YouTube 三集
- **PyTorch 核心** · tensor、autograd、nn.Module、DataLoader。入口：PyTorch 官方的 60-Minute Blitz 教程
- **自注意力（Attention）的历史** · attention 不是 Transformer 发明的，2014 Bahdanau 就有。入口：Bahdanau 原论文加 Jay Alammar 的 "Visualizing Neural Machine Translation"
- **信息论基础** · cross-entropy、KL divergence、perplexity 在 loss 和评估里反复出现。入口：3Blue1Brown 的信息论相关视频
- **几篇必过的 transformer 经典 paper** · Attention Is All You Need（2017）、BERT（2018）、GPT-2（2019）、GPT-3（2020）。入口：arxiv 原文，每篇只读 abstract + intro + conclusion 即可

做完三个项目、Karpathy 视频看过、几篇经典 paper 的 abstract 翻过，这一层就通关了。通关标准：别人问你"什么是 attention"，你能解释为什么需要、怎么计算、在真实模型里怎么表现，不停留在背一段 Q·K·V 公式的水平。

## 3.6 第五层：微调一个属于你的模型

这一层的目标是把前四层的知识串起来做一件事：为一个你关心的具体任务，微调出一个真正可用的 LLM。要求自己端到端搭一条"数据 → 训练 → 评估 → 上线"的完整链路，走完一份教程的水平不算。

### 项目 13 · 数据准备

选一个具体任务（你公司的 SQL 生成、某个小众语种的翻译、你自己的写作风格复刻、domain-specific 客服机器人都行），建立一份 2000-10000 条的高质量训练集。

带着这些问题做：

1. 一份"高质量"微调数据到底长什么样？quality 和 quantity 哪个更重要？
2. 合成数据（用更大模型造训练集）和真实人工数据各自的优劣是什么？混用时比例怎么控？
3. 数据清洗、near-duplicate detection、质量评估用哪些工具和方法？为什么这几步决定了微调效果的上限？
4. 什么是 instruction tuning 格式？Alpaca、ShareGPT、ChatML 这几种格式差在哪，你选哪个？
5. 训练集、验证集、测试集怎么划分？对微调而言和传统 ML 的划分原则有什么不同？
6. 如何避免数据泄露（训练集里悄悄混进了评估题）？这件事在微调里为什么特别容易发生？

### 项目 14 · LoRA 微调

用 Hugging Face PEFT（或 Unsloth、LLaMA-Factory 任选）在你的数据集上做 LoRA 微调。起步选一个 7B 级别的开源模型（Qwen、LLaMA、Mistral 都行），一张消费级 GPU 能跑完。

带着这些问题做：

1. LoRA 的核心思路是"在每个权重矩阵上加两个小 rank 的矩阵"。为什么只更新 0.1% 的参数却能达到接近全参微调的效果？
2. rank、alpha、target modules 这三个 LoRA 超参分别控制什么？起始值怎么选？
3. learning rate、batch size、epoch 数这几个训练超参的选择原则？为什么微调的 lr 通常比预训练小一到两个量级？
4. Training loss 一直降但 eval loss 开始上升，这是 overfitting。怎么检测、怎么救？early stopping 的触发点怎么定？
5. QLoRA 在 LoRA 上加了 4-bit 量化。它怎么做到"一张 24G 卡训 70B 模型"？
6. DPO、ORPO、SimPO 这几种偏好优化方法是什么？和普通 SFT 什么时候该用、什么时候不该用？

### 项目 15 · 评估与上线

为你的微调模型搭一套完整的评估体系，把它部署到一个能让别人试用的地方。

带着这些问题做：

1. 微调模型的评估比普通 LLM 难在哪？为什么 LLM-as-judge（用 GPT-4 打分）会变成事实上的标准？
2. 怎么设计一份能真正诊断你模型强弱项的 eval set？100 条精心挑选的样例和 10000 条随机样例，哪个更有价值？
3. 微调完要不要保留原模型的通用能力？怎么避免 catastrophic forgetting（学了新任务、丢了原本的通用能力）？
4. 把你的微调模型、原版开源 base model、GPT/Claude 并排对比，你发现什么 pattern？什么场景下你的微调真的赢了？
5. 部署微调模型到 production 有哪几条路径？vLLM + 自建 API / Together AI / Fireworks 这些托管平台 / 私有化部署，各自的 tradeoff？
6. 用户反馈"效果不如 GPT-4"，你怎么回应、怎么定位根因？

### 带着问题去读的几本书

微调方向的好资料在官方文档 + 博客 + 社区帖子，传统书滞后明显。

- **Hugging Face PEFT 官方文档 + blog**· LoRA / QLoRA / DPO 的权威教材，社区实战最多
- **Philipp Schmid 的博客**（philschmid.de）· 微调教程最接地气的来源，经常有 end-to-end 的可跑案例
- **《AI Engineering》· Chip Huyen**（前面层推过）· Fine-tuning 和 Eval 两章是这本书的精华
- **Unsloth 官方文档**· 单卡微调速度最快的开源实现，文档本身就是极好的 tutorial

### 基础知识回补

- **深度学习的"训练循环"** · dataloader → forward → loss → backward → optimizer.step()。入口：PyTorch Fundamentals 的 Training 章节
- **梯度检查点（gradient checkpointing）** · 训练大模型时的显存优化关键技术。入口：Hugging Face blog 的 gradient checkpointing 文章
- **混合精度训练（fp16 / bf16 / fp8）** · 为什么 bf16 训练更稳。入口：NVIDIA 的 Mixed Precision Training 白皮书
- **评估指标体系（BLEU、ROUGE、BERTScore、LLM-as-judge）** · 每个指标适合什么任务。入口：维基百科相关词条加 Hugging Face evaluate 库文档
- **分布式训练基础（DDP、FSDP、DeepSpeed）** · 一张卡不够用时的逃生路径。入口：PyTorch 官方的 Distributed Training tutorial

做完三个项目、资料翻过、基础有地图级印象，这一层就通关了。通关标准：别人看你的微调模型 demo，问"为什么这个 case 你的模型比 GPT-4 好/差"，你能从数据质量、训练超参、评估盲区里至少挑一个角度说清楚。

## 3.7 第六层：Ship 一个 production-grade AI 产品

这一层把前五层的所有能力集中到一件事上：做一个能让陌生人付费使用的 AI 产品。重心从"做得动"转向"跑得稳 + 跑得省 + 扛得住"。

### 项目 16 · 多租户架构 + 付费

为前面做过的任何一个 app（或新做一个）加上多用户系统、API key 管理、按量计费、登录鉴权、用户 dashboard。从免费 demo 升级到能收费的 SaaS。

带着这些问题做：

1. Multi-tenancy 是什么？单租户架构在用户过 100 人之后为什么通常扛不住？
2. 用户身份系统怎么设计？托管方案（Supabase、Clerk）和自建（NextAuth）各自的坑？
3. Usage-based billing 怎么做？Stripe Meter、Metronome、Orb 这些工具各自擅长什么？自己做账单系统难在哪？
4. API key 的生命周期（生成、分发、轮换、吊销）怎么设计才安全？常见的几种泄露渠道是什么？
5. 不同用户的数据怎么隔离？向量库里的 tenant isolation、日志中的 PII 屏蔽怎么做？
6. Free / Pro / Enterprise 三档的功能边界怎么划？feature flag 还是 config 驱动？

### 项目 17 · Observability + 事故响应

给产品搭一套完整的可观测性栈：traces、metrics、logs、alerts。至少模拟一次事故（rate limit 被打爆、上游模型 API 宕机、数据库连接池耗尽任选），走一遍从告警到回滚的完整流程。

带着这些问题做：

1. Observability 的三支柱（traces、metrics、logs）各自解决什么问题？在 LLM 系统里哪一支最重要？
2. OpenTelemetry 为什么正在成为事实标准？LangSmith、Langfuse、Helicone 这些 LLM 专用工具和它什么关系？
3. SLO 和 SLI 怎么为一个 LLM 产品定义？"模型回答得不好"算不算 SLO 违规？
4. 事故响应（detect → triage → mitigate → resolve → postmortem）每一步的具体动作是什么？
5. 上游 API（OpenAI、Anthropic）宕机时，你的产品应该自己挂还是 fallback 到备用模型？graceful degradation 怎么实现？
6. Postmortem 为什么要写成 blameless？这个文化背后的工程哲学是什么？

### 项目 18 · 成本优化 + SLA 保证

把产品的单位成本（每用户每月、每次调用）降下来，同时把可靠性指标（uptime、p99 latency）拉起来。这两件事看似冲突但经常能同时做。

带着这些问题做：

1. LLM 产品的成本结构怎么拆？token cost、infra cost、storage cost、egress cost 各占多少？
2. Prompt caching、response caching、embedding cache 这三层缓存分别适合什么场景？命中率能到多少？
3. 小模型兜底 + 大模型托底的 routing 策略怎么设计？怎么衡量"省了多少钱 vs 掉了多少质量"？
4. Batching 和 streaming 的 tradeoff：哪种能降成本、哪种能改善用户体验？能兼得吗？
5. 你承诺 99.9% uptime，但上游 OpenAI 只给 99.5%。架构上怎么补上这 0.4%？
6. Scaling 到 10000 并发用户时，瓶颈通常先出在哪？数据库、向量库、模型 API、自己的 app 服务器？怎么提前预防？

### 带着问题去读的几本书

Production 工程这一层的经典书反而不是 AI 专属的。

- **《Designing Data-Intensive Applications》· Martin Kleppmann**（前面层提过）· Production 系统设计的事实标准教材，AI 产品本质也是数据密集型应用
- **《Site Reliability Engineering》· Google SRE 团队**（免费在线 sre.google/books）· Observability、SLO、事故响应的工程鼻祖
- **《The Art of Scalability》· Martin Abbott & Michael Fisher** · Scale 架构的经典，原则直接可用
- **Increment 杂志的 incident response 相关文章** · 行业一线团队的事故 postmortem 分享，比书更实战

### 基础知识回补

- **分布式系统（再一次）** · 第三层已经点过 Kleppmann DDIA，这层深读 Chapter 5-9（replication、partitioning、transaction、consensus）
- **云平台基础** · AWS / GCP / 阿里云的核心服务（compute、storage、networking、identity）。入口：AWS Solutions Architect Associate 的官方学习路径，不考证，过一遍知识点
- **网络基础** · TCP、TLS、HTTP/2、CDN、DNS。入口：Cloudflare Learning Center（learn.cloudflare.com）
- **数据库 production 能力** · read replica、sharding、transaction isolation。入口：PostgreSQL 官方文档 Chapter 13 Concurrency Control
- **安全基础（OWASP Top 10）** · 做 production 不懂安全迟早出事。入口：OWASP 官方的 Top 10 页面加 PortSwigger 的 Web Security Academy

做完三个项目、至少一次真实事故演练、资料扫过，这一层就通关了。通关标准：把你的 production app 讲给一个运维或 SRE 背景的朋友听，他不会觉得你是"AI 工程师但不懂工程"。




# 四、小结：这只是一条路径

写到这里六层走完，快一万字。动笔之前回头再把方法论重述一次，这些原则比任何一个具体项目都更值得你带走。

**谋定而后动。** 学 AI 最大的一笔浪费是漫天乱学。选定方向、岗位、学习方式再动手。"LLM 方向 + 工程岗 + 项目驱动"是我给自己和读者锁定的那一组坐标。你的目标可能不同，但先把这三件事定下来，再决定要学什么。

**项目驱动学习。** AI 这一行的知识是做会的，光看不会。书和视频是查漏补缺的工具。每一层的产出都是一个能 demo、能讲清楚的具体作品。

**三三制节奏。** 每三个项目升一层能力，每三层停下来思考一次。既抵抗"漫天乱学"，也抵抗"死磕一条路停不下来"。每一层都是可验证的技能落地点，而不是泛泛的"我懂了 XX"。

**Vibe Coding + 费曼学习法。** 用 AI 陪你磨代码加速出活，用白话复讲做费曼校验锁死理解。前者让你快速出活，后者让你真正内化。

**自主学习 · 问题驱动。** 不再翻教材第一页到最后一页。带着问题找 AI 对话，让 AI 做你的"问题提示机"，每抛一个问题追三四层下去。

**最小认知层。** 每一层只抓住最关键的几个概念，细节留到卡住时再补。别让完备性焦虑拖慢你的进度。

## 学习和做产品，是同一件事

都是一个不断迭代的过程。产品的路线图是 MVP → beta → v1 → v2 ……你不会也不该一上来就做出 v10。你先做一个能跑的 MVP，放到用户手里拿反馈，再决定下一版改什么。

学习也一样。第一层就是你的 MVP：能调 API，能 ship 一个 app，这就是你的 hello world。拿给朋友用、问他们意见、把反馈写进第二层。做到第三层你是一个 "LLM 工程师 beta 版"；做到第六层你就是 production-grade 的全栈 LLM 工程师。每一层是一次迭代，层与层之间你都有权停下来调整方向。

最常见的陷阱是"我先把六层的东西全看一遍再动手"。不要这样做。学习是一轮一轮的加载和内化，一次性装满装不下。Vibe-reading 一遍读物、Vibe-coding 一遍项目、费曼一遍讲给自己听，这是一个循环式的过程，得一轮一轮来。

## 这只是一条路径

这篇文章只覆盖了"LLM 方向 + 工程岗"这一条路径，因为它是 2026 年最多人关心的。但其他路径同样有市场、同样值得走：

- **传统 ML + 推荐系统** · 中国互联网大厂岗位的半壁江山
- **CV + 自动驾驶 / 机器人** · 硬件派的产业机会
- **AI for Science** · 对有理工科博士背景的人最友好的切入路径
- **AI 安全与对齐** · 纯研究路线
- **AI 独立开发者** · 技术 + 产品 + 营销 + 社区构建的全栈人

每一条都值得一篇同样篇幅的文章。如果你对其中某一条特别感兴趣，评论区告诉我，我会优先写下一篇。或者你可以直接 fork 掉这篇的结构，按"三三制 + 项目驱动 + 自主学习"的方法论给自己画一张专属路线图。这套方法和具体方向无关，任何细分领域都能套进来。


> 没有完美的路径图，只有你动起来的第一步。

这篇读完没去打开编辑器写第一行代码、也没去和 AI 问第一个问题，那这篇就是白读了。

---

## 关于我

我是 [@snowboat84](https://x.com/snowboat84)，物理 PhD 转 AI 六年，现在主要精力放在 Claude Code、LLM 应用、独立开发上。

如果你想看更多关于"学术转 AI、AI 工程化、独立开发"的一手观察，欢迎关注我：

- X（Twitter）：[@snowboat84](https://x.com/snowboat84)
- 博客：[snowboat-blog](https://github.com/dongzhang84/snowboat-blog)（所有文章开源）

我写了很多篇关于转行、AI 工程、vibe writing、vibe reading 方法论的深度长文，可以去扒。

如果这篇回答对你有用，点个赞加关注。下一篇续集会讲"从第一份工跳到算法岗的那一年，我做对和做错了什么"。

---

## 作者其它文章

- [每个人都应该使用的三个最有用的 Claude Skill](https://x.com/snowboat84/status/2047110768773197834)
- [SpaceX 立志传（一）：赌上全部的最后一次发射](https://x.com/snowboat84/status/2046743964192276766)
- [估值290亿美元的套壳公司，正在被自己的房东杀死](https://x.com/snowboat84/status/2046380497627230607)
- [黄仁勋和主持人吵红了脸：芯片封锁中国，美国到底能不能打赢？](https://x.com/snowboat84/status/2046022377830801725)
- [AI将如何颠覆教育，普通人又应该如何抢夺教育新的生态位](https://x.com/snowboat84/status/2044932338262667509)
- [学物理的八方英雄们，物理学已死，请转行搞AI](https://x.com/snowboat84/status/2044584627046920278)
- [不会编程、没有融资、没有员工，他怎么一个人做到年入2000万](https://x.com/snowboat84/status/2044216044575998136)
- [一人公司盈利四亿美元：是骗子，还是可复制的红利？](https://x.com/snowboat84/status/2043493870265422223)
- [2026第一季度大裁员，AI是背锅侠吗？](https://x.com/snowboat84/status/2042766853404307931)
- [重返星辰大海：这次绕月飞行有意义吗？](https://x.com/snowboat84/status/2042405716380835998)
- [张雪峰在美国为什么无法成功](https://x.com/snowboat84/status/2042045634245746743)
- [兄弟们，我创业失败了，人生完整了](https://x.com/snowboat84/status/2040948420391940272)

---

## 本文参考文献

- [Hugging Face Transformers 官方文档](https://huggingface.co/docs/transformers/index) · 正文里推的核心库
- [PyTorch 官方文档](https://pytorch.org/docs/stable/index.html) · 深度学习主流框架
- [LangChain 官方](https://python.langchain.com/docs/) · LLM 应用编排框架
- [LlamaIndex 官方](https://docs.llamaindex.ai/) · RAG 方向的核心工具
- [NeurIPS 官方](https://neurips.cc/) · AI 顶级学术会议
- [ICML 官方](https://icml.cc/) · 机器学习顶级学术会议
- [arXiv cs.LG](https://arxiv.org/list/cs.LG/recent) · 机器学习预印本每日更新
- [arXiv cs.AI](https://arxiv.org/list/cs.AI/recent) · 人工智能预印本每日更新
- [Paper Copilot · NeurIPS Statistics](https://papercopilot.com/statistics/neurips-statistics/) · NeurIPS 历年录取与引用分布
- [GPTZero · 100 AI hallucinations in NeurIPS 2025 papers](https://gptzero.me/news/neurips/) · NeurIPS 2025 论文里 AI 假引用的扫描报告
- [LoRA 原论文](https://arxiv.org/abs/2106.09685) · 正文里提到的主流微调方法
- [LinkedIn ML jobs](https://www.linkedin.com/jobs/machine-learning-jobs) · 正文里工程岗 vs 算法岗实时供给数据
- [HR Leader · AI Engineer tops LinkedIn 2026 Jobs on the Rise](https://www.hrleader.com.au/business/27698-ai-engineer-tops-linkedin-s-2026-jobs-on-the-rise-list) · LinkedIn 2026 增速第一的职位榜
- [Global Times · Chinese tech giants AI talent recruitment](https://www.globaltimes.cn/page/202506/1336180.shtml) · 中国大厂 AI 扩招数据
- [snowboat-blog](https://github.com/dongzhang84/snowboat-blog) · 我的文章仓库

---

## 附录：原始草稿

> 学 AI 的目标是什么，是去研究算法，还是大概知道一下？还是为了找工作，算法的工作还是工程的工作？要带着目标去学，否则穷经皓首都在细节上面。
>
> 之后你的目标，是写论文还是做项目？因为是自学，个人推荐做项目多于写论文。看看每年 NeurIPS、ICML 之类的会议，arXiv 上的水文究竟有多少。
>
> 接下来说人工智能的分类。过去传统的机器学习，CV，还有语言方面的大语言模型。机器学习需要知道什么几大块？CV 是什么？LLM 是什么？它们的数学框架是什么？这样你才能倒三角知道到底要学什么。
>
> 然后，机器学习准备做什么项目。CV 做项目吗？现在最火的是 LLM，那么做 LLM 的项目。
