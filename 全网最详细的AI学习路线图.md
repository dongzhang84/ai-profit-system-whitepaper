

说句不太尊敬的话，我反对这个问题下不少高赞答案的路线图。

大部分回答的通病是不问你的目标就一刀切，花大量篇幅讲 CNN、LSTM 的内部结构却把 LLM 一句话带过，项目示例还在推一些十年前的教科书作业，中间还常夹带"限时免费"、"救你命的资料包"这类课程推广话术。

我给你的路线图反过来：先定目标，再选方法，再挑一个能 ship 的项目，倒推要学什么。

简单介绍一下我自己。我本科物理方向，一直是年级第一。博士读的是天体物理，一度以为这辈子就做物理学家了，后来判断整个物理学科走进了死胡同，果断转 AI，做到美国大厂的算法工程师。我的 AI 全是自学，从最基础的线性回归到 CNN、Transformer，再到现在每天在调的 LLM Agent。没有 CS 背景、没有人带，全是在 production 里边摸边学，走了六年。

这几年来我见过太多想自学AI的朋友，拿着一份看起来很全的路线图，最后卡在各种细节、教程、论文和项目里没出来。

所以今天这份内容不走完整路线图那套，只讲两个必须先回答的问题。

# 第一问：你学 AI 的目标是什么？

这个问题不先回答，后面全是浪费时间。大致上，你可能有以下四种目标之一：

- **大概知道一下（了解就够）**：你不打算以此为业，只是想跟得上行业话题。几门 Coursera 公开课加几篇科普文就够（比如我这篇），不用往下读了。
- **研究算法（写论文 / 搞前沿）**：目标是进入AI领域的学术圈或工业实验室。路径跟下面完全不同，需要数学根基、阅读论文、做 novel contribution 的能力。更关键的是，你要攀上学术界的大佬，效果无限大于自己埋头自学。
- **找工作 · 算法岗**：要会公式推导、会调模型、会做实验。顶端的纯研究岗（顶校 PhD + novel research）门槛仍然很高，但只会调模型、不会工程化的中低端，2026 年已经不好找。
- **找工作 · 工程岗**：要会把模型塞进 production、会部署、会优化 latency。这个方向的人才缺口最大。

如果你真的想集中一段时间内学到一定的 AI 知识，并且最终可以落地，我建议大多数人走第四条，即 AI/ML 工程岗。工程岗需求比算法岗大一个量级，这个差距在数据上很直观：

全球层面，LinkedIn 美国市场实时数据显示 ML 工程类岗位在招 85,000+ 个，ML Research Engineer 27,000+ 个，纯 ML Researcher 只有 11,000+ 个，工程岗对研究岗大约 8:1。AI Engineer 在 LinkedIn 2026 "Jobs on the Rise" 榜单上位列全球增速第一。

中国层面，纯研究型职位集中在百度研究院、阿里达摩院、字节 AI Lab、腾讯 AI Lab 这几家，全国加起来每年招聘名额只有几百到上千。部署 AI 的工程岗遍布几乎所有中大型互联网公司、金融、医疗、制造业。百度 2026 年 AI 扩招同比 +60%，其中绝大多数是能把模型落地的工程岗。

结构性原因很清楚：做 AI 基础研究的公司全球几百家，部署 AI 的公司 2026 年已经是几万家。研究岗是漏斗顶端的一小撮，工程岗是漏斗下游的大盘。真正有付费意愿的公司要的是能 ship 的人。只会推导 AI 模型背后数学公式的博士，面试反而卡在工程关。

但是具体的目标，还是要你自己来定。

# 第二问：你想写论文还是做项目？

如果是自学，我个人推荐做项目，远多于写论文。

原因很简单。你去看看 NeurIPS / ICML / ICLR 每年收几千篇 paper，arXiv 上每天新增几百篇 AI 论文。这些里面真正的原创工作不到 10%，剩下的基本是水文。换个数据集、换个 benchmark、调个参数、换个 loss 函数，就能发。

水文多到什么程度？连一线研究员自己都不看同行的 paper，只跟几个核心组的工作。

对自学者来说，追着读水文是最亏的。你以为在前沿，其实在消费别人的噪音。

做项目反过来。一个能跑、能 demo、能被人使用的 project，比读十篇 paper 更能验证你学会了。而且在找工作时，面试官看你做过什么，不看你读过什么。

所以接下来的路线图，全部围绕"做项目"这个假设展开。

# 一、AI 究竟学什么：三大方向拆解

AI 这个词太大，不拆分就没法学。当前主要分三块。

## 1.1 传统机器学习（Traditional ML）

**几大块**：

- 监督学习：分类、回归（线性回归、逻辑回归、SVM、决策树、Random Forest、XGBoost）
- 无监督学习：聚类（K-means）、降维（PCA）、密度估计
- 模型评估：交叉验证、过拟合、bias-variance tradeoff、各种 metrics

**数学框架**：

- 线性代数（矩阵运算、特征分解）
- 概率统计（贝叶斯、最大似然）
- 凸优化（梯度下降基础）

**现状**：这块在工业界还在用，最大的落地场景是推荐系统（字节、小红书、美团、快手这些大厂算法岗位的大半都是推荐系统）。表格数据、风控、搜索排序场景也离不开传统 ML。但它不是 2026 年的"火"点。

## 1.2 计算机视觉（CV）

**几大块**：

- 图像分类（classification）
- 目标检测（detection）：YOLO、Faster R-CNN
- 图像分割（segmentation）
- 图像生成（GAN、diffusion models）

**数学框架**：

- 卷积运算（CNN 的核心）
- 后期转向 Transformer（ViT、SAM）
- 扩散过程的概率框架（DDPM）

**现状**：CV 岗位需求还在，但增速明显放缓。图像生成领域 Stable Diffusion 和 Midjourney 这类把很多 CV 任务整合掉了。除非你有特定行业目标（医疗影像、自动驾驶、机器人），否则不建议把 CV 作为主攻方向。

## 1.3 NLP / LLM（大语言模型）

**几大块**：

- 预训练（pre-training）
- 微调（fine-tuning、instruction tuning、RLHF、DPO）
- 推理（inference、prompting、RAG）
- Agent 系统（function calling、multi-step reasoning）

**数学框架**：

- Transformer 的 attention 机制（必须吃透）
- 自回归语言模型的概率建模
- RLHF 的强化学习基础（PPO、DPO）
- 优化器（AdamW、各种学习率策略）

**现状**：2026 年最火的方向，没有之一。岗位需求、薪资水平、创业机会都集中在这里。如果你现在开始学 AI 且目标是找工作，直接从 LLM 切入。传统 ML 和 CV 需要时再补。

严格说这一块原本叫 NLP，LLM 是 Transformer 时代之后的演进形态。在 2026 年，NLP 里值得学的部分几乎都被 LLM 吸收了，所以我直接叫 LLM。

## 1.4 其他你可能听说过的方向

- **推荐系统**：不算独立方向，在传统 ML 里已经说过。中国互联网大厂最多的算法岗
- **多模态（Multimodal）**：CLIP / GPT-4V / Sora 这一支。既不是纯 CV 也不是纯 LLM，2026 年最热的新兴领域。等你把 LLM 主线走完再看
- **语音（Speech）**：ASR / TTS。小众方向，岗位少，除非你对这个领域有特殊兴趣，跳过
- **强化学习（RL）**：RL 在 LLM 里以 RLHF / DPO 形式存活下来，纯 RL 研究更多在机器人和游戏 AI 领域。学 LLM 会自然接触到 RL 基础

# 二、倒三角思考：从方向倒推学什么

选定方向之后，倒过来推"需要学什么"。这就是我前面说的反路线图。

假设你选 LLM 方向、工程岗、做项目。那你真正要学的是：

- Python（你多半已经会）
- PyTorch（能看懂、能改、能跑）
- Hugging Face Transformers（核心库，必须熟）
- Prompt engineering（能结构化地设计 prompt）
- RAG（向量数据库、embedding、检索管线）
- LangChain / LlamaIndex 之一（至少会一个）
- Fine-tuning 基础（LoRA、QLoRA，至少跑通过一次）
- 部署（FastAPI 加 Docker，或一个 serverless 平台）

这就是你的实际路线图。不包括线代入门、概率入门、CNN 内部原理、RNN 历史、BERT paper 精读。这些先放一边。真到不懂某个原理再回来查。

物理 PhD 背景的同学这里特别占便宜：线代、概率、优化本来就会，直接跳过。Python 也多半写过数值模拟。你真正要补的是工程那一块，版本控制、production 部署、API 设计、log 和 monitoring。

# 三、对应的项目选题

不同方向做不同 project。下面每个方向给 3 个我认为靠谱的选题。

## 3.1 传统 ML 项目

- **信用评分模型**：Kaggle 有现成数据，能讲清 feature engineering、模型选择、metric tradeoff
- **时间序列预测**：股价、电商销量、网站流量。重点讲异常检测、特征窗口设计
- **推荐系统**：Matrix factorization / 协同过滤入门，讲清 cold start 问题

## 3.2 CV 项目

- **特定场景分类器**：不要做 ImageNet（已经饱和），做一个垂直场景，比如皮肤病分类、工业质检、农作物病虫害
- **自己训一个小 diffusion model**：训不动原版就训 MNIST 或 CIFAR 级别的 tiny diffusion，能讲清 forward/reverse process
- **YOLO 微调到特定对象**：猫狗识别以外的东西，比如哈士奇 vs 阿拉斯加犬这种细分

## 3.3 LLM 项目（我最推荐）

- **RAG 系统**：找一个你熟悉的 domain（比如你自己的笔记、某本书、公司内部文档），搭一个能问答的 RAG。能讲清 chunking 策略、embedding 选择、检索质量评估
- **一个能调工具的 Agent**：写一个 agent，能调 3 到 5 个工具（查天气、算账、发邮件、搜索）。能讲清 function calling 的原理和坑
- **微调一个特定任务的 LLM**：用 LoRA 在某个特定任务上微调（比如中文文案生成、代码补全、SQL 生成）。能讲清数据准备、训练曲线、评估方法

我最最推荐第一个：RAG 系统。理由：门槛最低、最能 ship、最容易在面试里讲清楚、2026 年企业落地场景里 RAG 是最成熟的需求。

# 四、你真正要做的三步

1. **定目标**：研究、了解、算法岗、工程岗，选一个
2. **选方向**：ML、CV、LLM，选一个，不要贪
3. **挑项目**：上面那 9 个里挑一个，两周内跑通第一版

看到任何给你"五大阶段二百条目录"的路线图，关掉。那是作者炫技，对你的学习没帮助。

---

## 关于我

我是 [@snowboat84](https://x.com/snowboat84)，物理 PhD 转 AI 六年，现在主要精力放在 Claude Code、LLM 应用、独立开发上。

如果你想看更多关于"学术转 AI、AI 工程化、独立开发"的一手观察，欢迎关注我：

- X（Twitter）：[@snowboat84](https://x.com/snowboat84)
- 博客：[snowboat-blog](https://github.com/dongzhang84/snowboat-blog)（所有文章开源）

我写了很多篇关于转行、AI 工程、vibe writing、vibe reading 方法论的深度长文，可以去扒。

如果这篇回答对你有用，点个赞加关注。下一篇续集会讲"从第一份工到跳到算法岗的那一年，我做对和做错了什么"。

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
