# Pre-LLM 的 ML 工程师怎么看现在的 LLM

**日期** · 2026-05-01 (周五★) | **支柱** · B · 六年亲历

---

## 核心论点

2021 年我调了 6 个月 BERT。现在写 prompt 30 秒搞定。这个差距不是技术飞跃，是抽象层级上移。

## 钩子候选

- 2021 年我调了 6 个月 BERT。现在写个 prompt 30 秒搞定。这个差距是什么？
- Pre-LLM 训过模型的人看 prompt engineering，第一反应是"这就是 hyperparameter search 换皮"。

## 主干

- **当年每个 project 都要 train-from-scratch**。feature engineering、data cleaning、hp search 的泥潭
- **现在 prompt + eval 是新调参**，但本质是更高抽象层级
- **Pre-LLM 的工程纪律在 LLM 时代反而稀缺**——reproducibility、ablation study、error analysis。没人教新人这些
- **最大的错位感**：以前 1% 的 accuracy 提升要 2 周。现在换个 prompt 5% 就上去。但 1% → 0.1% 的 eval 纪律还是要的
- **一个真实对比**：同一个文本分类任务，2021 vs 2024 的时间分配

## 结论候选

- LLM 不是 ML 的延续，是 ML 的封装。但下面一层的工程素养还是核心竞争力。

## 长文公式

B

## 待补素材

- 2021 年那个 BERT 项目的 milestone 和耗时
- 2024 年同类任务用 Claude 的 30 分钟实录
