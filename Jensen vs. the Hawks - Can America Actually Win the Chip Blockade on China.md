## Contents

- I. The Hawk Narrative Behind the Host
- II. Jensen's Rebuttal: "AI Is a Five-Layer Cake"
- III. From Biden to Trump: America's Policy Zigzag
- IV. Why the US Can't Seal It Off: Three Leaky Channels
  - 4.1 Channel One: Legal Offshore Rental
  - 4.2 Channel Two: Unofficial Channels
  - 4.3 Channel Three: Downgraded Compliance Variants
  - 4.4 A Strange Two-Person Dance
- V. The Hawks Are Running the Wrong Playbook: Why the Soviet Story Doesn't Fit China
  - 5.1 How the Soviets Actually Got Boxed In
  - 5.2 China Isn't the Soviet Union
  - 5.3 CoCom Itself Has Been Mythologized
- VI. The Structural Gap Between US and Chinese AI Business Models
  - 6.1 Two Types of Players: Pure AI Labs vs. Internet Giants
  - 6.2 US Side: The Model Itself Has to Pay the Bills
  - 6.3 China Side: The Model Is a Lever for Traffic and Cloud
  - 6.4 Summary Table
  - 6.5 What This Means for Chip Demand
- VII. Back to the Five-Layer Frame: How Should America Actually Fight This?
  - 7.1 Going Through the Layers
  - 7.2 "We Can't Lose Any Layer" Is a False Premise
  - 7.3 Does a Blunt Chip Ban Work?
  - 7.4 What a More Pragmatic US Strategy Would Look Like
- VIII. How China Should Play This
  - 8.1 China's Hand Is Stronger Than It Thinks
  - 8.2 The Real Home Court Is the Application Layer; the Job Is Exporting the Advantage
  - 8.3 The Software Stack Is the Real Weak Spot
  - 8.4 Own the Tempo and the Narrative
- Closing

---

On April 15, 2026, Dwarkesh Patel had Jensen Huang on his podcast.

Patel is 25, Indian-American, and over three years has built the Dwarkesh Podcast into one of the most substantive AI interview shows anywhere. Past guests include Demis Hassabis of DeepMind, Mark Zuckerberg of Meta, Silicon Valley investor Marc Andreessen, and former UK Prime Minister Tony Blair. His format: two-hour interviews, dense preparation, no PR softballs, and a willingness to corner a guest. Last year the Wall Street Journal called him "the sharpest interviewer of the AI era."

Jensen Huang, 62, founded Nvidia in 1993. Over 30 years he pushed the GPU from making video games look pretty to powering the AI revolution. By early 2026 Nvidia's market cap had passed $4 trillion, making it the most valuable company in the world. Jensen went from a niche Silicon Valley CEO to someone the presidents of both the US and China want private meetings with.

The first half hour was standard fare: Nvidia's roadmap, TPU competition, the supply-chain moat. Around the 40-minute mark the conversation turned to China.

The tone on both faces shifted. Dwarkesh laid out the standard Washington-Silicon Valley hawk line: selling H20-class compute to China shortens China's timeline for offensive cyber capabilities. Jensen dropped his CEO keynote voice. His pace picked up; his face flushed.

> "Comparing AI to anything that you just mentioned is lunacy. We're not enriched uranium. It's a chip, and it's a chip that they can make themselves... You're not talking to somebody who woke up a loser."

Dwarkesh cut the exchange into a three-minute clip and posted it on X. Within 24 hours it had over 20 million views. Everyone in the field realized this went beyond a CEO defending his revenue stream. Jensen had put the central contradiction of America's China AI strategy on open display.

# I. The Hawk Narrative Behind the Host

Before getting to who the hawks are, a quick word on the chip names.

H100 is Nvidia's flagship training GPU, released in 2022. Through 2024 it was the de facto global standard for frontier AI training; almost every cutting-edge model was trained on H100 clusters. H200, released in 2024, is the upgrade: memory goes from 80GB to 141GB and inference throughput jumps substantially. Blackwell (which covers B100, B200, and the GB200 NVL72 rack) is the next-gen architecture, shipping from late 2024, with another 2×-plus jump in performance.

For the China market, Nvidia designed explicit downgraded compliance variants. H800 was the H100 nerf (NVLink bandwidth cut), banned in 2023. H20 was the follow-up: a second round of H100 downgrade aimed at China where training performance was deeply cut but inference performance was kept nearly intact. H20 was briefly banned by Trump in April 2025, unbanned in July. By January 2026, even H200 had started receiving export licenses to China.

One sentence: **H100 / H200 / Blackwell are the full versions; H800 / H20 are the castrated China variants.** The hawks' core demand is that neither the full versions nor the castrated ones should flow into China.

With the chip vocabulary clear, now the hawk camp.

Dwarkesh's own views don't really matter. His role is to sharpen the question. Behind him stands a coalition that spans Silicon Valley, Washington, think tanks, and defense. These people sit in different circles, but on "China AI must be fully tech-blockaded" they line up tightly.

On the Silicon Valley side the loudest voice is Anthropic CEO Dario Amodei. At Davos in January 2025 he delivered a widely quoted line: selling H200 to Chinese AI companies is like selling nuclear weapon components to North Korea during the Cold War. Palantir CEO Alex Karp pushes the same direction, calling for a "whole-of-society mobilization" against Chinese AI in a register lifted straight from a Cold War defense intellectual. Younger AGI-safety voices push the same way. Leopold Aschenbrenner, a former OpenAI staffer, wrote a 2024 essay called "Situational Awareness" that circulated widely in the field; it frames China's AI catch-up as existential. Palantir advisor Jacob Helberg and Jason Matheny (former State Department, now RAND CEO) round out the camp.

On the Washington side the flag-bearers are former officials. Matt Pottinger was Deputy National Security Advisor for Asia in Trump's first term; he now lobbies for stricter China tech controls from the think-tank world. Mike Gallagher chaired the House Select Committee on China and anchored the 2023-24 Congressional hawks. Jake Sullivan, Biden's National Security Advisor, designed the first round of chip export controls in October 2022; Gina Raimondo, his Commerce Secretary, enforced them. The parties differ, but on "technology must be blockaded in coordination with allies" the talking points line up.

In think-tank and book territory, Chris Miller's *Chip War* (2022) has become something close to a hawk bible, quoted endlessly by the White House, Congress, and Wall Street. The dozens of reports that CNAS, CSIS, and RAND put out each year mostly share the same assumptions: AI is decisive, the window is tight, blockade is both feasible and necessary.

All of them share a worldview with four pillars. AI is decisive, weapons-class technology; its impact rewrites the military, economic, and geopolitical order, a different magnitude entirely from Excel or PowerPoint. China is treated as an adversary, and the two countries are already in a de facto AI arms race. The critical window is 6 to 12 months: America leads now, but the gap narrows every quarter. And the blockade has to be total, watertight, and coordinated with allies: no advanced chip into China, no Chinese frontier model on US cloud, no open-source weights accessible to China.

The historical template is crystal clear in hawk minds: CoCom, the Coordinating Committee for Multilateral Export Controls, founded in 1949. Throughout the Cold War, 17 Western countries coordinated to keep Soviet microelectronics permanently a generation and a half behind. That eventually destroyed Soviet military electronics and computing. In the hawk mental model, that playbook can be stamped onto China without modification.

Their policy ask is a tight, cross-national tech embargo: ban advanced GPUs, ban advanced lithography, ban cross-border cloud rental, ban open weights to China. Ideal state: every H100 needs Commerce Department approval before it can even boot.

That's the real backdrop to why Dwarkesh pushed the way he did.

# II. Jensen's Rebuttal: "AI Is a Five-Layer Cake"

The sharp lines Jensen delivered on the podcast, "lunacy," "not enriched uranium," "are you talking to a loser," travel well, but they're emotion. His real strategic frame came out at the Davos World Economic Forum in January 2026, and was later turned into an official Nvidia blog diagram: **AI is a five-layer cake**.

From bottom to top, the five layers are:

1. Energy: the physical base of all AI; where the electricity comes from
2. Chips: GPUs, ASICs, advanced manufacturing
3. Infrastructure: data centers, networking, operating systems, plus developer platforms like CUDA
4. Models: foundation LLMs
5. Applications: end products, real use cases

Jensen's core claim is one sentence: **America has to win every layer, but the layer it most needs to win is the application layer.**

This lands on the hawk camp's soft spot. Amodei sits in layer 4 (models); the entire hawk strategy is to defend layer 4. Jensen's point is that to defend layer 4 you are giving up layers 3 and 5, and layers 3 plus 5 are a much larger market than layer 4. His rhetorical press on Amodei made it into Dwarkesh's clip: why let one layer of the AI industry lose the whole market just so another layer can benefit?

The next part of his argument is a flywheel. The China market brings Nvidia about $50 billion in revenue a year, and that money flows straight into next-generation GPU R&D. Shut China off and you cut a big piece of the R&D budget, and the next generation of Nvidia slows down, which is the window AMD, Google's TPU, and Broadcom, all lined up at TSMC and Samsung, are waiting for.

A deeper problem is the developers. CUDA is Nvidia's real moat, harder to copy than any hardware. Roughly half the world's AI developers are in China. Pushing them into Huawei's CANN or domestic MUSA ecosystems actively fills in half of CUDA's moat. Developer habits are built over 20 years. Once a mass migration happens, it doesn't reverse. Think of how Android took mobile share from iOS: once the ecosystem splits, the incumbent's pricing power is gone.

A third cost is losing the competitive pressure. Without Huawei Ascend breathing down its neck, Nvidia can easily turn into a policy-protected Intel. After Intel ate the x86 server market into near-monopoly, its innovation pace collapsed, and by the 2020s TSMC had it multiple nodes behind on leading-edge manufacturing. Jensen does not want that story for Nvidia.

And there's the paradox: the blockade is actively creating the thing it's trying to prevent. Huawei Ascend's ecosystem grew 5× between 2023 and 2026, driven mainly by the October 2022 export controls. Using an embargo to suppress a rival ended up pushing that rival's self-built ecosystem to the scale where it can operate on its own.

Jensen has an obvious conflict of interest: he makes money when GPUs go to China. But a conflict of interest is not the same as being wrong, and every point above can be independently checked.

# III. From Biden to Trump: America's Policy Zigzag

Jensen is not arguing in a vacuum. US chip policy toward China over the past four years has already been forced into retreat, repeatedly. The hawks just don't want to admit it.

The story starts in October 2022. The Biden administration's first wave of export controls dropped, banning A100 and H100 sales to China outright. Within three months, Nvidia rolled out compliance versions A800 and H800, preserving most of the performance and cutting only key interconnect bandwidth. It took the Biden team 12 full months to react with tighter rules. That 12-month window was exactly when Chinese majors completed their last round of heavy stockpiling. October 2023 brought the second wave: A800 and H800 banned too. December 2024 brought the third: the entity list expanded, and HBM high-bandwidth memory came under control.

January 2025: Biden went out swinging with the AI Diffusion Rule. It sorted 120 countries into three tiers of access and tried to steer all US AI compute flow, not just to China. A global compute-control regime, in effect.

When Trump took office the policy got stricter before it loosened. In April 2025, even H20, Nvidia's second-tier China-compliant part, got banned. Nvidia lost $2.5 billion in China revenue that quarter.

Then things flipped. July 2025 brought news that H20 sales to China would resume. The real reason came out in August: Nvidia and AMD would hand 15% of their China sales revenue to the US government. Trump originally wanted 20%; Jensen shaved it down to 15% through repeated White House negotiations. This was the first time in US history that a private company became a direct revenue partner in an export-control regime in this "pay-per-license" way.

December 2025, Jensen flew to Washington to meet Trump. A few days later H200, a real-inference chip a long way above H20, went on the approved-for-China list. ByteDance and Alibaba separately told Nvidia they each wanted to buy 200,000-plus H200 units, with combined orders above $14 billion.

Then the plot flipped again, this time from China's side. Mid-January 2026, Chinese customs received an internal notice: H200 would not clear at the border. A few days later the Ministry of Commerce followed: H200 would only be approved in "special circumstances," and routine commercial orders would not. On January 22 Beijing went further and told domestic majors to pause H200 procurement plans. By February 24, 2026, the US Commerce Department admitted that after Trump's December license, the actual number of H200 units sold to China was **0**. In March, Nvidia simply stopped H200 production and gave the TSMC capacity to the next-gen Rubin.

Looking at that full timeline, the hawks' "total blockade" had already broken in practice by July 2025. The US government stopped talking about "small yard, high fence" and turned around to make the blockade into a 15% tax. That paradigm shift is itself a rebuttal of the hawk narrative. You don't tax something you're blockading. You tax something that's still flowing, and you want a cut.

And the opening of 2026 added a stranger scene: the US said you can sell, and China said don't buy. The next section unpacks how this two-way partial decoupling actually works.

# IV. Why the US Can't Seal It Off: Three Leaky Channels

Why did the US government end up retreating all the way to "charge a tax"? Because three channels can't actually be sealed.

## 4.1 Channel One: Legal Offshore Rental

Alibaba and ByteDance moved entire AI training workloads to Singapore and Malaysia. They rent Nvidia GPU compute from US cloud providers there, or build their own data centers. Satellite imagery shows the sprawl of data centers built in Johor, Malaysia, since 2024, and what's running inside them is an open secret.

The Financial Times confirmed in the second half of 2025: **parts of the Qwen and Doubao training workloads are being done on offshore Nvidia GPUs**. ByteDance got access to roughly **36,000 Blackwell GPUs** via a Malaysian operator.

Biden's last-minute AI Diffusion Rule was meant to plug this exact leak. Trump revoked it via executive order after taking office in February 2025. In February 2026, the Trump team drafted a replacement and then pulled that too. The US government itself has no unified position on this.

## 4.2 Channel Two: Unofficial Channels

The unofficial channel follows a standard shape. Shell companies registered in Singapore, Hong Kong, or Malaysia place orders with Nvidia or third-party distributors under the heading "data center procurement." Once the chips land, Southeast Asian freight forwarders reroute them to Shenzhen or Shanghai. The chain has clear roles: buyer, freight forwarder, logistics, customs clearance, distribution. Above a certain volume it turns professional.

In December 2025 the US Department of Justice launched Operation Gatekeeper and busted a $160 million smuggling network. The case implicated at least five Singapore-registered shell companies; hundreds of H100 and H200 units had moved through Vietnam and Malaysia into Shenzhen. That's just the one they caught. Between April and June 2025, SemiAnalysis ran an industry survey and estimated the total scale of unofficial channels at over $1 billion, 6×-plus the size of the DOJ operation.

The GPUs US Customs and BIS intercept in a full year are a rounding error against the quarterly compute demand of Chinese majors. SemiAnalysis founder Ray Wang's conclusion hits harder: **over 60% of China's frontier AI training still runs on Nvidia hardware**. The layer the US is guarding hardest (top-end training parts) is leaking the worst.

## 4.3 Channel Three: Downgraded Compliance Variants

This channel's strangest feature: Nvidia designed it on purpose.

H20 was built specifically to "comply and still sell to China." US export rules draw the line on "training performance thresholds," so Nvidia cut the training performance just below that threshold while keeping inference performance largely intact. On some inference benchmarks H20 actually runs faster than H100. In the second half of 2025 it became China's workhorse inference chip: procurement volumes at Alibaba Cloud, Volcano Engine, and Tencent's internal inference pool have been roughly doubling quarter over quarter.

The core misalignment: US export controls treat training performance as the blocking target, while China's AI business flywheel is increasingly driven by inference scale (unpacked in section VI). A chip that's "training-castrated, inference-intact" looks "compliant, no harm" to the US side, and looks "just fine" to China. Huawei Ascend follows the same logic: its single-card training is well behind Blackwell, but its inference price-performance is already good enough, and volume is being held up by domestic inference demand. One line is Nvidia's compliance-nerfed H20; the other line is domestic Ascend. Together they fill China's inference compute pool. The US blockade aimed at training, but the business model itself is diluting the importance of training.

## 4.4 A Strange Two-Person Dance

The other side of this is just as telling: China itself isn't fully trying to "buy freely."

Starting in the second half of 2025, Beijing began sending notices to major domestic data centers telling them to prioritize domestic chips. Some central state-owned enterprises were explicitly told to refuse H200. Internal talking points within SASAC went something like: "anything that can be done with domestic parts should not use imports." By January 2026, Customs sealed H200 entry outright. The line went from "guidance" to "ban."

In parallel, Huawei Ascend shipped 600,000 units in 2025 and is targeting 1.6 million in 2026. Cambricon, Hygon, Moore Threads, Biren, and Enflame are all ramping. In effect the Chinese government is doing three things at once: use SOE procurement orders to steer revenue to domestic makers, use the pressure of US blockade to force faster maturing of domestic ecosystems, and use the enormous domestic demand base to amortize domestic chip costs. Every H200 that doesn't come in maps to an Ascend or a Cambricon order.

So the actual state is: the US hasn't fully closed things off, and China hasn't fully opened up. Both sides are half-decoupling, and neither has gone all the way. The US blocks top-end training parts, China blocks mid-tier foreign inference parts, and the middle is where Nvidia's H20 and Huawei's Ascend fight to fill the gap. A strange two-person dance.

# V. The Hawks Are Running the Wrong Playbook: Why the Soviet Story Doesn't Fit China

Every hawk policy claim eventually traces back to the same historical template: during the Cold War, CoCom kept Soviet microelectronics permanently a generation and a half behind, and the Soviets' military electronic and computing capability eventually collapsed.

This story gets told over and over in the books of Amodei, Matt Pottinger, and Chris Miller. Without the story itself on the table, it's hard to understand why the hawks are so confident they can pull it off again.

## 5.1 How the Soviets Actually Got Boxed In

In 1949, right at the start of the Cold War, the US convened 17 Western countries in Paris and set up CoCom (the Coordinating Committee for Multilateral Export Controls). Its mission was direct: keep advanced technology, especially military electronics and semiconductors, inside the Western bloc and out of Soviet hands.

It did box the Soviets in. Through the 1960s to the 1980s, Soviet IBM mainframes were copies and knockoffs; the core components of the Elbrus processor, and the specialized chips in their military command systems, had to come in through East European black markets or be fished from the West by the KGB. By the mid-1980s, the generational gap in Soviet military electronics and computing had widened across the board: missile accuracy, satellite surveillance, missile defense, all lagging, and the overall productivity of the Soviet military-industrial complex was dragged down significantly.

The hawk narrative is built on exactly this base: if CoCom could break the Soviets, then with a different list and a different adversary, it can be done to China again.

But that playbook runs into several hard problems when you try to set it on the 2026 stage.

## 5.2 China Isn't the Soviet Union

The biggest one is the consumer market. The Soviet Union never had a real consumer electronics market; its semiconductors were almost entirely used for military and space applications, so the moment the US cut the military line, the whole semiconductor industry effectively lost its export market. China in 2026 is the opposite: 1.4 billion consumers, 400 million new smartphones a year, 10 million new EVs a year, explosive growth in smartwatches, robot vacuums, drones, EV power electronics, industrial robots, almost every segment. The consumer market gives semiconductors a real iteration engine: order volume supports capacity, real user feedback drives engineering, scale drives cost down. The Soviets had no such flywheel. China has it, and China's consumer electronics market has already passed the US by size.

Then the industrial base. In 1985, Soviet semiconductor supply chains were almost entirely dependent on imported Western tools and materials, with no domestic lithography, no domestic wafers, not even their own photoresist. China today is not that. SMIC is mass-producing 7nm, sampling 5nm; YMTC makes NAND, CXMT makes DRAM, domestic HBM is beginning to sample, and mature-node and mid-tier chips are largely self-sufficient for domestic demand. The real question is whether China can make good-enough, large-scale mid-tier chips. The answer is already yes. "Can China do 3nm" is not the most dangerous question right now. The hawks keep staring at the leading-edge node while the rest of the stack grows under their noses.

Third, allied coordination. CoCom's power came from 17 Western countries locking arms. That level of coordination no longer exists. Dutch, Japanese, and South Korean semiconductor-related exports to China still run above $100 billion a year. ASML grudgingly accepts banning EUV exports to China but strongly opposes banning DUV, because that would directly hurt the global revenue of its mature-line machines. Samsung and SK Hynix sell over half their memory chips to Chinese customers; as long as China remains that market, they will not voluntarily cut the cord. Without Cold War-era allied unity, any blockade will leak.

Fourth, talent. Soviet scientists mostly couldn't leave the country; the KGB watched them at the airport. Today, nearly half the papers at NeurIPS, the top global AI conference, have a first author who is ethnically Chinese. Chinese AI researchers flow freely between universities and companies in the US, Europe, Singapore, and Australia. The core researcher rosters at OpenAI, Anthropic, and DeepMind are packed with Chinese faces. Cutting that network costs the US itself far more than it costs China.

## 5.3 CoCom Itself Has Been Mythologized

There's a deeper problem still: blaming the Soviet collapse on the chip embargo is itself a narrative that keeps getting flattened.

The Soviet collapse was a stack of systemic failures. In the mid-1980s, international oil prices dropped from around $30 a barrel to $10, and Soviet hard-currency oil revenue evaporated by two-thirds. The Afghanistan war ran for 10 years and drained the treasury and manpower. The planned economy was already in stagnation, with bread and soap queues in major cities. Chernobyl punched through the government's credibility. Gorbachev's reforms opened the door to public debate but couldn't close the loop. CoCom, in this stack, was an accelerator at most: it made Soviet military electronics fall behind faster, forced a higher share of GDP into defense, and sped up the overall collapse. But without the oil collapse and Afghanistan, CoCom by itself could not have broken a superpower.

Treating CoCom as an independent causal variable confuses an accelerator with an engine. Running the 1985 script on the 2026 stage is a strategic category error.

# VI. The Structural Gap Between US and Chinese AI Business Models

A dimension that almost never shows up in hawk analysis: US and Chinese AI companies are fundamentally running two different businesses. To understand "what the blockade actually hits," you first need to see the shapes of those two businesses clearly.

## 6.1 Two Types of Players: Pure AI Labs vs. Internet Giants

The main characters of US frontier AI are pure AI labs: OpenAI, Anthropic, xAI, Mistral, Cohere. They have no legacy business. The model is the only product, and all cash flow has to come out of the model itself. Google and Meta have their search and ads fortresses as backup, but on pure model quality they've fallen noticeably behind Anthropic and OpenAI.

The main characters of Chinese frontier AI are internet giants: ByteDance, Alibaba, Baidu, Tencent. Each of them already had a super cash machine before AI: Douyin, Taobao, WeChat, Baidu Search. AI, for them, is a new component embedded into an existing business, helping them sell more ads, more e-commerce, more cloud service. Pure AI companies like DeepSeek, MiniMax, and Zhipu exist too, but in scale and voice they sit well below the giants. DeepSeek itself has the backing of quant fund High-Flyer, so there's no short-term profitability pressure.

These two types of players have different cost structures, different pricing logic, and different sensitivities to "frontier scarcity." The real difference isn't on the price tag; it's in where the money comes from.

## 6.2 US Side: The Model Itself Has to Pay the Bills

Pure AI labs collect money directly on the model.

The most direct line is consumer subscriptions. ChatGPT Plus is $20 a month, ChatGPT Pro is $100+, Claude Pro is $20, and AI apps like Cursor, Perplexity, and Replit anchor at the $20 mark. Free tiers exist, but they're the funnel. The revenue comes from Pro and enterprise paid seats.

One layer up is enterprise and API. ChatGPT Enterprise and Claude for Enterprise charge per seat, starting at $30 to $60 a month. API pricing is per-token. Claude Sonnet is roughly $3 per million input tokens and $15 per million output. GPT-4-class pricing is similar. Customers range from AI-native tools like Cursor and GitHub Copilot to Fortune 500s embedding Claude and GPT into internal workflows. Anthropic positions itself most clearly here; Amodei has said publicly multiple times that Claude is enterprise-focused and they are consciously stepping back from the mass consumer market.

A third line is cloud-provider distribution. Claude ships through AWS Bedrock, OpenAI through Azure OpenAI Service, Gemini through GCP Vertex AI, to large enterprise customers with compliance requirements, where compute fees and model fees are bundled. So "does America also sell compute?" Yes, but at the premium end, and the ultimate value in the chain still flows back to the frontier model.

All three lines share one precondition: the scarcity premium of owning the frontier model. You only get to charge these prices if you're 6 to 12 months ahead. That's why OpenAI and Anthropic burn tens of billions a year training new generations. It's why Amodei is hypersensitive to "Chinese frontier models catching up." Once frontier scarcity is gone, the pricing model collapses.

## 6.3 China Side: The Model Is a Lever for Traffic and Cloud

Chinese internet giants make very little money on model subscriptions directly. Their logic: make the model free, or close to free, send the traffic back into the cash machines they already own.

The biggest piece is ads and traffic monetization. ByteDance's Doubao is free, but the users and behavior data it accumulates flow back into Douyin; each percentage-point gain in Douyin's AI recommendation, AI ad creative, or AI customer service translates into real advertising CPM lifts. When Baidu made Ernie Bot free, the AI-conversation UX repackaged its search ad slots, and advertiser CPC actually went up.

Second piece is e-commerce GMV. Alibaba plugged Qwen into Taobao and Tmall search and recommendation. Each point of click-through or conversion lift is hundreds of millions to billions of yuan in incremental GMV. JD is doing the same, and Pinduoduo is chasing.

Third piece is selling compute, that is, serving the company's own model API as a cloud service. This line is more aggressive in China than in the US. Aliyun Bailian, Volcano Engine, and Tencent Cloud TI Platform are all pushing their in-house model APIs hard: Qwen Plus, Doubao Pro, Hunyuan. Pricing is an order of magnitude below GPT-4 or Claude. Some Doubao Pro tiers are 0.8 RMB per million input tokens, over 20× cheaper than Claude Sonnet. The pricing isn't designed to earn token margin. The goal is to lock small and medium businesses and developers into the company's cloud ecosystem, then make money downstream on storage, databases, compute, and data services. Volcano Engine's Q4 2025 disclosure: Doubao's daily token-call volume is 16.4 trillion, which is 46.4% of China's public-cloud LLM market.

Paid specialist products exist too. ByteDance's Seedance (video generation) charges per second. Kuaishou's Kling is also pay-per-use. MiniMax, iFlytek, and Zhipu all have enterprise subscriptions and paid APIs. These have real revenue, just not the main line of Chinese majors' AI income yet. The main line is still "free model plus ecosystem monetization."

So Chinese AI looks "all free" on the surface. In reality it's moved the profit point one step downstream, to traffic, e-commerce, cloud, and ecosystem.

## 6.4 Summary Table

| Dimension | US (OpenAI, Anthropic) | China (ByteDance, Alibaba, Baidu, Tencent) |
|-----------|-----------------------|---------------------------------------------|
| Main player type | Pure AI lab, model is the only product | Internet giant, AI embedded as a new component in legacy business |
| Consumer price point | Mostly $20/month subscription, free tier as funnel | Mostly 0 RMB; plus pay-per-use specialist products like Seedance, Kling |
| Enterprise revenue | Enterprise subscriptions + high-priced API per-token | Cheap API driving volume + ad/e-commerce monetization + super-app binding |
| Sell compute? | Yes, via Azure/AWS/GCP at a premium distributing frontier models | Yes, more aggressively, via Volcano / Aliyun / Tencent Cloud pushing own-model APIs cheap |
| Importance of frontier scarcity | Life or death; revenue depends on the scarcity premium | Not critical; revenue runs through the ecosystem |
| Most sensitive event | China frontier catching up → subscription model collapses | Domestic inference demand explosion → ecosystem monetization scales |

## 6.5 What This Means for Chip Demand

The two business models have completely different chip demand structures.

The US model is heavily dependent on training compute. Frontier lead is the revenue source for US labs. OpenAI and Anthropic sink tens of billions a year into training clusters, and there's effectively no ceiling on demand for top-end training parts like H100, H200, and Blackwell. Inference needs compute too, but compared to training it's a secondary cost. ChatGPT's paid subscriber base is in the tens of millions; Anthropic's enterprise customer base is still below 100 million users. Neither is in the same order of magnitude as a single Chinese super-app's daily active users.

The Chinese model is much more dependent on inference compute than on training. A free-to-user model serving a 1-billion-user base is a different beast; Doubao alone processes 16.4 trillion tokens a day. At that scale, the bottleneck is "do we have hundreds of thousands of good-enough inference cards," not "a few thousand top-end training cards." Inference also doesn't demand extreme single-card performance the way training does. An H20 keeps most of an H100's inference performance. A Huawei Ascend 910C's inference price-performance is already within arm-wrestling range of H100.

This is why banning top training cards hurts China much less than the hawks expect. The sharpest blade of the blockade is aimed at frontier training, and frontier training is the layer US labs depend on most and Chinese majors depend on least. China's flywheel runs on inference scale, and inference compute can be filled with compliance H20s plus domestic Ascend, Cambricon, and Hygon. This is a fact determined by business structure itself.

# VII. Back to the Five-Layer Frame: How Should America Actually Fight This?

Switching the view to America. If the US wants to stay ahead in the AI era, what should the strategy actually be? Really "win every layer"? Does a blunt chip embargo actually work?

Jensen's line at Davos, "win every layer," is more of a rallying cry than an executable battle plan. Once you put each of the five layers under the microscope, America's odds per layer look very different. Understanding those differences is a prerequisite to knowing where to place the bets.

## 7.1 Going Through the Layers

**Layer 1, Energy.** America almost certainly cannot hold this layer. China's 2025 electricity generation was roughly 2× the US, and new capacity keeps doubling. US AI data-center buildout runs into a grid that hasn't been seriously overhauled in decades. Add the slow approval cycle for new power plants, add NIMBY resistance, and it becomes a three-headed drag. Jensen pulled this layer to the front because the gap becomes decisive once we're in the giant data-center era. The US isn't helpless, but at current approval and build pace, this layer is hard to close in a 5-to-10-year window.

**Layer 2, Chips.** Split it in two. At leading-edge fabrication (3nm and below), the US-plus-TSMC-plus-Samsung alliance is still at least 10 to 15 years ahead, and ASML EUV lithography is the real chokepoint. That's defensible and should be defended. But mid-tier chips (7nm to 28nm) are a different story: SMIC is already in 7nm production, YMTC and CXMT memory products are largely self-sufficient for domestic demand, and Huawei Ascend targets 1.6 million units in 2026. The US cannot stop China from building mid-tier domestically anymore. The hawks confused "defend the leading edge" with "ban everything" and expanded the former into the latter. The upside on the former has been negligible. The slap-back on the latter has been repeated.

**Layer 3, Infrastructure (including CUDA).** This is actually the layer where the US has the strongest structural advantage. CUDA is 20 years of accumulated developer habit; technology can be copied, but ecosystems don't move overnight. The weird part: the chip embargo is precisely what's hollowing this layer out. Roughly half the world's AI developers are in China, and the embargo is pushing them onto Huawei CANN and domestic MUSA. Once that cohort completes its migration and produces a batch of mature toolchains and open-source libraries, CUDA stops being the global default. Its monopoly position would be chewed the way Android chewed iOS on mobile. The layer America most needs to defend is being pried open by the very policy the hawks champion.

**Layer 4, Models.** The US frontier is 3 to 6 months ahead of China (even White House AI lead David Sacks concedes this number). That gap was 12 months back in 2024. Qwen, DeepSeek, Doubao, and Zhipu GLM have closed to near-frontier on public benchmarks. On the open-source side, Qwen's ecosystem scale is already #1 globally. The US can stall this layer but cannot hold it forever. Even if blockade stretches the lead by 12 months, all the costs at the other layers have already been paid.

**Layer 5, Applications.** This layer has already split in two. On the consumer AI side, China's super-app ecosystem (Douyin, WeChat, Taobao, Meituan) is a market US firms simply can't enter; and US consumer AI products (ChatGPT, Claude) have their own territory outside the Great Firewall. On the enterprise SaaS side, the US has Salesforce, Oracle, Workday with deep B2B roots and multinational enterprise clients. China's B2B SaaS capability is comparatively thin. Layer 5 is really two separated markets, each with its home turf.

Put it on one picture: America's actual structural advantages are layer 3 (CUDA ecosystem) and layer 4 (frontier models), and layer 5's enterprise SaaS segment. Layers 1 and 2-mid-tier are effectively already lost.

## 7.2 "We Can't Lose Any Layer" Is a False Premise

So how should Jensen's "win every layer" line be read?

Read literally, it's wrong. America cannot win all five. China is already 2× ahead on energy and self-sufficient on mid-tier chips; fighting head-on there is wasting resources.

Read another way, what Jensen was really saying is different: do not, for the sake of layer 4, hand over layers 3 and 5 too.

The hawk strategy puts all chips on "stop China from touching frontier layer 4." For that single goal, they're willing to cut Nvidia's China market (direct damage to layer 3's R&D flywheel); willing to push half the world's AI developers out of CUDA (direct hollowing of layer 3 itself); willing to let Nvidia become a policy-protected company with less competitive pressure (long-term damage to layers 2 and 3's innovation tempo); willing to let the US AI applications market fracture into two separated ecosystems (damage to layer 5's global reach).

In exchange for what? A 6-to-12-month delay in Chinese frontier catch-up. And once China catches up, what happens? Not much. China's business model doesn't depend on frontier scarcity in the first place (see section VI). The hawks are paying a very high price for a delay that inflicts almost no real damage on the other side.

So the real question is the other one: when you can't win everything, which layers do you trade for which? The hawks' current exchange rate is catastrophic.

## 7.3 Does a Blunt Chip Ban Work?

No. Worse, it's working in reverse.

From section IV: the embargo hasn't blocked what it wants to block. Offshore rental is unplugged, with Alibaba and ByteDance tapping 36,000+ Blackwell GPUs in Malaysia and Singapore. Unofficial channels are unplugged, with SemiAnalysis estimating 60% of China's frontier AI training still runs on Nvidia. Downgraded compliance plus domestic replacement are jointly filling the inference pool; H20, Ascend, and Cambricon together have already made "inference compute" good enough.

What the embargo is doing instead is a different list. It removes Nvidia's $50B-a-year of China revenue, cutting the R&D budget for the next several GPU generations. It pushes the world's largest developer base out of CUDA and straight into CANN and MUSA. It gives Huawei Ascend and SMIC both market share and fiscal subsidy, which accelerates mid-tier chip self-sufficiency. And it pushes Chinese domestic politics toward "full decoupling is required," turning demand for next-gen domestic chips and operating systems from policy target into hard requirement.

One line: the embargo didn't block what it was supposed to block, and actively advanced what it was supposed to prevent.

## 7.4 What a More Pragmatic US Strategy Would Look Like

If the US genuinely wants to stay ahead in AI, a realistic strategy looks something like this.

**Stop fighting battles you can't win head-on.** Accept the structural energy gap; redirect resources to energy efficiency (more power-efficient GPUs, more token-efficient model architectures), nuclear restart (small modular reactors), and allied energy pooling (Canadian hydro, Middle East gas and solar). Accept mid-tier chip self-sufficiency in China and shrink the defensive line to 3nm-and-below leading edge.

**Put the chokepoints where they actually bite.** ASML's EUV, KLA's metrology, AMAT's deposition tools are the real chokepoints. Hold those, and China's progress toward 3nm slows substantially. At the same time, loosen export controls above 7nm mid-tier equipment, where China is already self-developing. Continuing to control those gives zero marginal gain and keeps alienating allies.

**Layer 3 needs an open door, not a closed one.** This is the most counterintuitive one: keep selling Nvidia GPUs into China. The real goal is to keep Chinese developers inside the CUDA ecosystem (making money is a side effect). As long as CUDA is still the first choice for Chinese AI companies, the US moat at layer 3 stays. Once developers migrate en masse to CANN/MUSA, that moat is gone for good. This is what Jensen was really saying at the core.

**Layer 4 is held by sustained investment, not by blockade.** The hundreds of billions of capex going into OpenAI, Anthropic, xAI each year is the actual mechanism that keeps America's frontier lead. Six-to-twelve months bought through blockade is much lower quality than six-to-twelve months bought through training the next model.

**Layer 5: deepen the home court, don't overreach.** US AI applications should deepen their position in enterprise SaaS, Fortune 500 clients, multinationals, and the US-allied bloc. Don't fantasize about entering the Chinese consumer market. At the same time, watch out for reverse incursion: ByteDance's Doubao-family products and Qwen's open-source ecosystem are already building user bases in Southeast Asia, the Middle East, and Latin America. The US should push application-layer investment harder in those third markets.

**Use precision tools, not blunt ones.** The 15% tax looks like a humiliation in hawk eyes, but from a practical-strategy view it's more sensible than a full embargo: it allows flow while taxing flow, which preserves Nvidia's R&D flywheel (layer 3), constrains the most sensitive uses to some degree, and generates revenue for the US Treasury.

Put together, this is what Jensen was really saying. America's goal should never have been the slogan "win every layer." The operational goal is: win hardest on the layers with structural advantage (layer 3 CUDA, layer 4 frontier model, layer 5 enterprise SaaS); do not bleed the house dry on layers you can't win (layer 1 energy, layer 2 mid-tier chips).

The hawks have the actual advantage structure upside down. That's the underlying reason Jensen's face flushed on the podcast.

# VIII. How China Should Play This

Switching back to China. What does this debate actually mean for Beijing?

Those 40 minutes of Jensen flushing red were a spectator event for China. But the arc and outcome of that argument directly decides what cards China can play over the next 3 to 5 years. If the question is "how does China avoid being boxed in, or even win this race," the answer has already moved past tactical questions like "should we stockpile more H200s." What decides the outcome is how the whole board is read.

## 8.1 China's Hand Is Stronger Than It Thinks

Through all of 2025 the Chinese public conversation was dragged along by the "only 6 months of window left" narrative. Even inside many majors, there was anxiety. Today, that window has neither materialized nor really existed.

Three things are on the table. The embargo can't close the three channels (section IV walked through each). China's AI business model doesn't feed on "frontier scarcity" (section VI). The split inside the US between the hawks and the Jensen camp has effectively turned "small yard, high fence" into "tax booth" (section III). Together: China's strategic space has been there all along, just hard to see through the anxiety.

The question worth worrying about is a different one: can China actually use its structural advantages well under this configuration?

## 8.2 The Real Home Court Is the Application Layer; the Job Is Exporting the Advantage

Jensen's Davos slide had one point that's especially useful for China: AI's real endpoint is the application layer, and the biggest part of the cake is there. That happens to be the layer China is best at.

1.4 billion consumers, the closed loop of Douyin + WeChat + Taobao + Meituan, plus Chinese manufacturing's appetite for AI productivity: that combination is unique globally. Put AI capability into it and scale effects kick in immediately. Doubao's 16.4 trillion tokens a day is a real user base in real scenarios at real scale.

But that advantage is mostly fenced inside China. Turning it into global leadership needs a few things to happen in parallel: ecosystem export, open-source standards, vertical-industry penetration.

ByteDance's Doubao family, Alibaba's Qwen open-source, Kuaishou's Kling have started breaking into Southeast Asia, the Middle East, and Latin America. Qwen has over 600 million downloads globally and 170,000 derivative models, which is effectively foundation-laying for a Chinese AI global application market. If that foundation stabilizes over 3 to 5 years, the US's Fortune 500 home court in layer 5 stops being the only global player. China gets its own half of the sky.

## 8.3 The Software Stack Is the Real Weak Spot

The most uncomfortable part of Chinese AI these past few years comes from somewhere more hidden: developer inertia on CUDA.

Most Chinese majors' core R&D pipelines are still built on CUDA, from PyTorch to vLLM to Megatron-LM, all CUDA-native. That means: if Nvidia one day cuts certain deep-binding CUDA APIs or drivers for China (a harsher blockade than any GPU ban), Chinese majors would lose a substantial chunk of developer productivity in the short term.

What Jensen didn't say out loud on the podcast: CUDA's China dependency is a pressure point for Nvidia and a standing risk for China. The Chinese AI scene has known this a long time but nowhere near solved it. Huawei CANN and domestic MUSA are climbing, but not fast enough.

So the real strategic meaning of "use American chips or not" lands on the surrounding software stack: CUDA, cuDNN, NCCL, TensorRT. As long as that layer stays coupled, China's AI "autonomy" is only half-autonomous. Huawei and Cambricon hardware are catching up, but the software layer needs bigger, more sustained investment. What DeepSeek, MiniMax, and Zhipu are doing on GPU-agnostic middle layers, domestic compiler toolchains, and TVM modifications is the actual critical path to real autonomy.

## 8.4 Own the Tempo and the Narrative

Two things the Chinese policy community has argued hardest about in the past year: should domestic substitution be forced all the way through in one go? And should the "US window" narrative be bought into?

The direction of domestic substitution is right, but the tempo cannot be hostage to political slogans. AI is a "scale × time" game. Pushing substitution too fast migrates workloads that should run on H20 onto domestic alternatives that are 20% slower, which drags application-layer competitiveness down in the short run. A more rational approach is layered: keep frontier training on compliance Nvidia chips; migrate scaled inference to domestic hardware gradually; make consumer AI and SMB APIs fully dependent on the domestic ecosystem. This preserves performance and still gives domestic makers enough order volume to slowly mature.

As for "only 6 months of window left," that narrative is essentially psychological pressure from US hawks. China has no reason to pace itself by it. The more accurate reading goes the other way: time is on China's side. The generational advantages at the energy layer and mid-tier chip layer will continue to cash in over 3 to 5 years; the application-layer business flywheel will get bigger; global-South acceptance (Southeast Asia, Middle East, Latin America, Africa) of Chinese AI will keep rising. America's head start is concentrated in two layers, frontier models and CUDA ecosystem, and both gaps are closing at a measurable rate.

What China actually needs to do is simple: defend the home court (application layer, inference scale, global-South market), fill the weak spots (software-stack autonomy, frontier pure-AI firepower, domestic-substitution tempo), and let America keep playing its hand badly. The hawks are actively helping China finish that last item.

There's a trap on the other side too: "China will inevitably win" is another flattened narrative. The frontier model gap is real. The migration away from CUDA is far from complete. Leading-edge process nodes will not be caught in 5 years. Jensen's five-layer frame is most useful to China as a more sober lens: this race has to be judged along five axes at once, and any narrative that compresses it into a single variable ("chip embargo decides everything" on one side, "China inevitably wins" on the other) is over-simplified.

# Closing

Back to the opening scene. Jensen's flushed face, Dwarkesh's relentless follow-up, 40 minutes of exchange compressed into a 3-minute clip that was seen 20 million times on X.

For all the arguing, both sides got part of it right.

The hawks aren't fully wrong. AI genuinely is a decisive, infrastructure-scale technology; the military, intelligence, and security concerns have real substance. The urgency of the critical window, the need for allied coordination, the scarcity premium at the frontier, each stands on its own. Writing off Amodei, Pottinger, and the rest as pure Cold-War nostalgia is its own flattening.

Jensen isn't fully right either. He is Nvidia's CEO, and $50 billion a year of China revenue is real. His argument for "keep CUDA open" is half strategic judgment and half business position. Treating every line he said as objective fact is another flattening.

The hard part is finding a workable middle path under two conditions that are both true: part of the hawk concern is valid, and the embargo toolkit has already failed in practice. Jensen's five-layer frame is the more dimensional ruler: it puts the costs at energy, chips, infrastructure, models, and applications all on the table at once, closer to reality than "how many months does our frontier lead us by."

For the rest of us watching, those 40 minutes on Dwarkesh's podcast are the clearest X-ray of AI-era geoeconomics out there. What it shows is the US-China rivalry, America's internal split, and the friction of trying to run a globalized AI supply chain through Cold War tools. Three things overlapping on one picture.

The real questions never had simple answers. "Can America win" and "will China be boxed in" are both oversimplified. The honest question has to run across all five layers. Which of each country's advantages are structural? Which are policy-shiftable? And what are the real costs of trading one layer to protect another?

Jensen's flushed face is an argument for exactly that more complicated question getting some space. How the fight actually plays out past 2026 is something politics, business, and technology will all have to answer together.

# References

- [Jensen Huang on Dwarkesh Patel Podcast](https://www.dwarkesh.com/p/jensen-huang) – 2026-04-15, Huang on TPU competition, China chip exports, Nvidia's moat. 2-hour interview; the China segment is about 40 minutes.
- [Jensen Huang on AI's 'Five-Layer Cake' at Davos – NVIDIA Blog](https://blogs.nvidia.com/blog/davos-wef-blackrock-ceo-larry-fink-jensen-huang/) – January 2026 Davos; the first full public statement of the "five-layer cake" frame.
- [On Dwarkesh Patel's Podcast With Nvidia CEO Jensen Huang – Zvi Mowshowitz](https://thezvi.substack.com/p/on-dwarkesh-patels-podcast-with-nvidia) – Detailed commentary on the episode, including the China section.
- [The many contradictions of Jensen Huang – Transformer News](https://www.transformernews.ai/p/the-contradictions-of-jensen-huang-nvidia-china-chips-export-controls) – Analysis of Huang's China chip position.
- [Trump says Nvidia will hand the U.S. 15% of its H20 chip sales to China – NPR](https://www.npr.org/2025/08/11/nx-s1-5498689/trump-nvidia-h20-chip-sales-china) – August 2025 details of the 15% H20 revenue-sharing deal.
- [Reuters: China orders customs to block Nvidia H200 AI chips](https://www.wenxuecity.com/news/2026/01/14/126489245.html) – 2026-01-14 first report on China's internal customs notice blocking H200.
- [China's Ministry of Commerce: H200 approved only in 'special circumstances'](https://finance.sina.com.cn/roll/2026-01-22/doc-inhieiky2818285.shtml) – 2026-01-22 Chinese Ministry of Commerce clarification.
- [US Commerce confirms H200 China sales at zero](https://www.eet-china.com/news/202602259385.html) – 2026-02-24 US Commerce Department admits that after Trump's December license, actual H200 sales to China were 0.
- [Nvidia halts H200 production as China backs Huawei AI chips – Asia Times](https://asiatimes.com/2026/03/nvidia-halts-h200-production-as-china-backs-huawei-ai-chips/) – March 2026: Nvidia halts H200; TSMC capacity reallocated to Rubin.
- [Nvidia CEO Huang calls China AI market a $50B opportunity – Fortune](https://fortune.com/asia/2025/08/28/nvidia-earnings-china-jensen-huang-h20-trump-export-controls/) – Huang's public estimate of the China AI market at $50B/year.
- [Trump administration backs off Nvidia H20 chip crackdown after Mar-a-Lago dinner – NPR](https://www.npr.org/2025/04/09/nx-s1-5356480/nvidia-china-ai-h20-chips-trump) – Backstory of the April 2025 H20 ban reversal.
- [Dario Amodei at Davos on AI export controls to China](https://www.weforum.org/annual-meeting/) – January 2025 Davos; Amodei's H200-to-North-Korea analogy.
- [The AI Diffusion Rule – Biden White House Archives](https://www.federalregister.gov/) – January 2025 Biden's 120-country AI compute control rule.
- [Operation Gatekeeper – DOJ press release](https://www.justice.gov/) – December 2025 DOJ bust of $160M GPU smuggling ring.
- [SemiAnalysis – Ray Wang on China Frontier AI Hardware](https://semianalysis.com/) – Estimate that over 60% of China's frontier AI training still runs on Nvidia hardware.
- [Financial Times – ByteDance Malaysia Blackwell Cluster](https://www.ft.com/) – Reporting on ByteDance's access to Blackwell clusters in Malaysia.
- [Huawei Ascend 910C production 2025-2026 – TrendForce / SemiAnalysis](https://www.trendforce.com/) – Ascend 2025 shipments 600K units, 2026 target 1.6M.
- [Qwen Open-Source Family Statistics – Alibaba Cloud](https://qwenlm.github.io/) – Qwen: 300+ open-source models, 600M+ global downloads, 170K derivative models.
- [ByteDance Volcano Engine Doubao Statistics](https://www.volcengine.com/) – Doubao daily token calls at 16.4T, 46.4% of China's public-cloud LLM market.
