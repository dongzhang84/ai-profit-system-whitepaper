## Table of Contents

- I. Principles: From Prehistory to Now
  - 1.1 The Prehistory: Two Paths for Code Tooling
  - 1.2 The Turning Point: How the GPT Series Changed the Game
  - 1.3 Why Code Is Especially Good Training Data
  - 1.4 RLVR: From "Able to Write" to "Able to Write Correctly"
- II. A Brief History of AI Coding Companies
  - 2.1 Origins: The Two Camps and Early Tools (2020 – 2022)
  - 2.2 Paradigm Shifts: From Editor Revolution to the Agent Era (2023 – 2026)
  - 2.3 The Chinese Market and the Non-Programmer Track
- III. The Road Ahead
  - 3.1 Building an App Is Systems Engineering; AI Coding Solves Only One Piece
  - 3.2 Will There Be a "One-Click App" Tool for Non-Programmers?
  - 3.3 Will This Wave of AI Coding Reshape the PC / Mobile App Ecosystem?
- IV. Closing Thoughts


Let's take stock of AI coding.

Back in 2021 it was still mostly an academic topic. Insider programmers treated it as a side tool. GitHub Copilot launched that year and got attention for a while; the debate was mostly "should I use this thing, will it make me dumber?"

By April 2026 the picture had changed completely. About 135,000 public GitHub commits per day are now produced directly by Claude Code, roughly 4% of all public commits across the platform. OpenAI's Codex CLI, one year after its relaunch, has crossed 3 million weekly active developers. Cursor's parent company Anysphere went from 0 to $2 billion in ARR over two years, the fastest curve in SaaS history.

In the span of four or five years, AI coding moved from "paper topic" to "tens-of-millions-DAU productivity tool."

I have been writing professional code for over ten years, and these tools have been part of my daily workflow for the last three. This article uses my own perspective to give a clean answer to three questions that get asked over and over but rarely answered systematically:

- How does AI manage to write code at all?
- How did this happen over the past five years?
- In the next few years, can ordinary people really build their own apps?

I'll go in order: principles, history, future. No technical background required.

# I. Principles: From Prehistory to Now

## 1.1 The Prehistory: Two Paths for Code Tooling

Before ChatGPT, getting machines to write code was being attempted along two separate paths.

One path was self-service for programmers, through forum-style platforms or IDE tools. Stack Overflow's pitch was "every error message and solution humanity has ever produced, all in one place." You wrote a piece of code, hit an error, pasted the message, and someone in the community answered. China's counterpart was CSDN, a developer community that started in 1999; by 2024 it had 40 million registered users and 12 million monthly actives, the Chinese-language external brain of the entire domestic programmer base. When I was learning to code in 2014, my daily loop was: write code, hit an error, copy-paste it into Stack Overflow, edit the answer, paste it back. That loop ran for a full 15 years before ChatGPT showed up.

The IDE layer was also trying to help. Microsoft Visual Studio (first released 1997) had IntelliSense; Eclipse (open-sourced by IBM in 2001) had Content Assist; JetBrains IntelliJ IDEA (2001) had smart completion. These were the canonical "intelligent prompts" of their era. But they were essentially dictionary lookups. You typed `str.` and the IDE listed every method on the String class. It didn't "understand" what you wanted. It looked up a table.

The other path was academic program synthesis: starting from a formal specification and deriving code through formal logic. This line dates back to the 1970s and was stuck at toy scale for half a century. The only industrial-grade result that came out of it was FlashFill, led by Sumit Gulwani at Microsoft Research and integrated into Excel in 2013, which guesses transformation rules across an entire column from a few examples you give it. But this approach demanded formal specifications or clean examples. It could not handle natural language at all.

Around 2020 there were also neural-network-based code tools, like Microsoft's CodeBERT (September 2020) and Salesforce's CodeT5 (2021). These were slightly smarter autocomplete. Their fundamental limitation was the same: they didn't understand natural language. You couldn't talk to them. They could complete a line of code, not take on a task.

Looking at all these lines together, the underlying problem becomes clear: for a machine to actually write code, it first has to understand natural language. Before 2018, nobody had cracked that.

## 1.2 The Turning Point: How the GPT Series Changed the Game

The turning point was the GPT series. In June 2018 OpenAI proposed an approach: pretrain on a massive corpus of natural text so the model learns the general skill of "guessing the next word," then fine-tune for specific tasks. GPT was the result. GPT-1 had 0.117B parameters and was a research prototype; GPT-2 (February 2019) jumped to 1.5B; GPT-3 (May 2020) hit 175B, 100 times bigger than GPT-2. Once the scale crossed that threshold, "understanding natural language" became real for the first time, and the path to code was wide open.

The model that writes code and the model that chats use the exact same Transformer network and do the exact same thing: look at the tokens that came before, predict the next token. To the model, a chunk of Python code looks just like a Chinese novel: both are token sequences. The model doesn't "know" it's writing code. It just runs the highest-probability next-token prediction along the context.

A concrete example. The simplest Fibonacci function:

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

The way the model generates this is one token at a time. Given `def fib(n):`, the highest-probability next token is a newline plus indentation. The next is `if`. The next is `n`. Then `<`. Then `2`. Then `:`. Then `return`. And it keeps guessing until the function closes. After seeing millions of lines of GitHub code several times over, this "guess the next token" probability distribution naturally encodes syntax, idioms, variable naming conventions, and comment style.

## 1.3 Why Code Is Especially Good Training Data

But code is uniquely well-suited to being learned by a language model, for several reasons.

The most direct one is regularity. After `for i in range(10):`, what comes next is an indented loop body. The rule is fixed, much more stable than natural language. The same idea can be expressed ten ways in natural language; in code there are usually two or three. This means the "compressed rules" the model extracts from a finite corpus are far denser in code than in ordinary text.

A deeper reason: code has objective right-or-wrong. Give a function and a test suite, run the tests, and you know whether it works. Natural language has nothing like this. Whether a poem is good, whether an essay moves you — there is no automatic grader. This property of code becomes a nuclear weapon later on.

Another reason is the data itself. Every open-source repo's README, every docstring before a function, every commit message — all of it is free "natural language ↔ code" parallel data. This is the data dividend that every code model after GPT-3 has been feeding on, and the volume is far beyond anything human annotation could produce.

The first wave of people walking this path treated code as a specialized skill to train. In 2021 OpenAI took GPT-3 and continued training it on over 100 GB of public code from GitHub (this technique is called continued pretraining). The result was a derived model, Codex. Codex hit 28.8% pass-at-1 on HumanEval (a 164-problem coding dataset OpenAI built), the SOTA at the time. During that period, OpenAI's API had `code-davinci` and `text-davinci` as two separate models — one wrote code, the other wrote prose.

After GPT-4, this split closed. Anthropic, OpenAI, and Google all started mixing large amounts of code directly into the pretraining data of their general models (public estimates put the share at 20% to 40%). There's no longer a separate code model; one Claude / GPT / Gemini handles both prose and code.

Why did the merge happen? Because of a counterintuitive finding: adding lots of code to training makes the model stronger at math, logic, and even natural language tasks. DeepMind, Google Brain, and OpenAI all observed this between 2022 and 2023. The intuition is straightforward: code as a corpus forces the model to learn "strict step-by-step reasoning" — every step has to hold, otherwise the next step collapses. Once that mode of thinking is learned, it transfers to non-code tasks. In other words, code training has become one of the core ingredients that makes general models smarter, well beyond a "side activity."

## 1.4 RLVR: From "Able to Write" to "Able to Write Correctly"

The killer technique unique to code models is reinforcement learning from execution feedback. The training loop looks like this: the model generates a piece of code, it gets dropped into a real runtime, the test suite runs, the result (pass / fail) is fed back as a reward signal, and the model learns to write better next time. This method is called RLVR (Reinforcement Learning from Verifiable Rewards). "Verifiable" is the keyword: the reward signal does not come from human annotation (expensive, slow, biased) but from automatic machine grading (cheap, scalable, objective). Code, math problems, and formal logic all satisfy "verifiable" — they are RLVR's natural homes.

The R1 model DeepSeek released in early 2025 pushed this approach to its extreme: train reasoning ability with reinforcement learning on math and code first, then transfer back to ordinary conversation, and on multiple benchmarks it caught up with the closed-source frontier models of the same period. The bulk of the training behind Claude Code, OpenAI o3, and Codex follows the same RLVR template. This only became mainstream after 2024, and it is the core reason coding ability has shot up so fast in the last two years.

A summary. Today's coding ability is a fusion of two things. One: code training has lifted general models to a new plateau, embedding "break a problem into steps, then make every step hold" into the model's default behavior. Two: large-scale reinforcement learning on tasks with objective right-or-wrong (code, math, reasoning) has been layered on top of real execution feedback, training the model from "can write" to "writes correctly." Together, these two are the actual engine of AI coding.

# II. A Brief History of AI Coding Companies

## 2.1 Origins: The Two Camps and Early Tools (2020 – 2022)

GPT-3 launched in May 2020 with 175B parameters. Once the scale was there, OpenAI for the first time had the confidence to sell a model to developers. In July 2021 they continued training GPT-3 on public GitHub code, got a 12B-parameter Codex, and shipped it inside GitHub's new Copilot product. This was the first time AI entered programmers' muscle memory. The habit of hitting Tab a few hundred times a day to accept completions started that summer.

But Copilot's form was limited then. The context window was only 2k to 8k tokens; it could only see a local slice of the current file; and it was passive — if you stopped typing, it stopped. It was good at completing a line, not at doing a task.

On the model side, Anthropic started almost in parallel. Its two leaders are Dario and Daniela Amodei, brother and sister. They left OpenAI at the end of 2020 and stood the company up by January 2021, taking with them a group of GPT-3-era core researchers including Tom Brown, Jared Kaplan, and Sam McCandlish. Anthropic positioned model honesty, controllability, and long-context understanding as its differentiators. That foundation later turned into Claude's natural advantage on coding tasks: it can read long codebases, follow complex instructions, and willingly say "I'm not sure" about parts where it isn't sure.

In November 2022 OpenAI released ChatGPT and the form of AI coding shifted from "completion tool" to "conversation partner." But early ChatGPT often confidently made things up when writing code, inventing APIs that did not exist. The Claude series that emerged at the same time had noticeably higher code accuracy in the engineering community's hands — a niche choice for engineers in the know.

After ChatGPT took off, the entire ecosystem of "external brains for programmers" started getting rewritten. Stack Overflow took the most direct hit. Founded September 2008 by Joel Spolsky and Jeff Atwood, the global Q&A site for programmers peaked in 2017: over 300,000 new questions per month, over 100 million monthly visits, 10 million registered users. After ChatGPT, monthly new questions slid from that 2017 peak to about 87,000 in 2023, then under 60,000 in 2024. By December 2025 the count was fewer than 4,000 — back to the level of 2008 when the site had just launched. CSDN was on the same slope. Kite, an early AI-completion startup founded in 2014, shut down in November 2022 with a parting line from its founder Adam Smith: the company "failed to deliver our vision of AI-assisted programming because we were 10+ years too early to market, i.e., the tech is not ready yet." Even 500,000 monthly actives could not keep it alive. Codecademy and W3Schools — the tutorial sites — kept losing traffic too.

## 2.2 Paradigm Shifts: From Editor Revolution to the Agent Era (2023 – 2026)

In 2023 GitHub extended Copilot into chat with Copilot Chat. But a sidebar chat plus an IDE main area for code was a split experience. The AI was kept in the corner.

The product that actually changed the paradigm was Cursor. Anysphere, the parent, was started by four MIT students in 2022. Their key bet was to fork all of VS Code and rewrite it. A fork is much harder than a plugin, but it lets you change the editor's interaction itself. Cursor's real technical contribution was codebase indexing: vectorizing the entire project so the AI could, for the first time, "see the whole codebase." This pattern later became the industry standard: use someone else's model (Anthropic / OpenAI), build your own engineering layer (project indexing, context organization, UI workflow).

In October 2024 the upgraded Claude 3.5 Sonnet launched, and its score on SWE-bench Verified (a real GitHub bug-fix benchmark with human-verified problems) jumped from the previous generation's 33% to 49%. "AI can really write code" became true for the first time at that moment. Cursor's experience changed qualitatively over the following months, and engineers migrated from Copilot to Cursor + Claude in large numbers. I made the switch myself in late 2024; within three months my code output felt like it had doubled.

Then, through 2024 and 2025, the whole line jumped from "completion inside the IDE" toward "agents." Devin, released by Cognition Labs in March 2024, was the first product that explicitly positioned itself as an "AI software engineer." The marketing ran ahead of the substance, but it did set the tone for the new product category: end-to-end task-level agents. Give it a goal; it breaks the task down, writes the code, runs the tests, fixes bugs.

Since then, the bulk of competition has fallen on three top products. Codex is OpenAI's second use of that name: first as a 2021 GPT-3 derivative powering Copilot, deprecated in 2023 in favor of GPT-4, and relaunched on April 16, 2025 as a "product name" — this time a Rust-written CLI agent. The relaunch picked up momentum fast. By March 2026 weekly actives had crossed 2 million; April pushed past 3 million, up 50% month over month. Inside ChatGPT Enterprise, Codex users grew six-fold from January to April.

Claude Code went deeper into the engineering community. Released by Anthropic in 2025, it leveraged Claude's natural advantage on long codebases, hit roughly $2.5 billion ARR by early 2026, and is producing about 135,000 public GitHub commits per day — 4% of all public commits on the platform. SemiAnalysis projects that share will pass 20% by end of 2026.

Cursor's own scale kept climbing. By February 2026 it was at $2 billion ARR. In April it raised at a $50 billion valuation — the fastest 0-to-$2-billion ARR curve in SaaS history.

A few other players have their own niches. Windsurf (formerly Codeium) is another AI-native IDE; things got complicated after it was acquired in mid-2025. The veteran GitHub upgraded Copilot into Agent Mode and Coding Agent; existing users converted naturally.

The overall layout in the engineering community today: the mainstream stack for senior programmers is Cursor + Claude Code, an IDE for writing code and a CLI for running large tasks.

## 2.3 The Chinese Market and the Non-Programmer Track

Beyond the main line, two threads deserve their own treatment: domestic Chinese vendors, and the non-programmer track.

The Chinese market developed in parallel with the overseas market. Several big tech companies each took their slot, and the open-source camp took its own.

ByteDance built Trae, the AI-native IDE in China most similar in feel to Cursor. It launched around late 2024. The strategy of being completely free for individual users helped it spread fast through the domestic developer community. Trae plugs into ByteDance's own Doubao model, and on Chinese-language projects with Chinese comments the experience is smoother than using Cursor directly. ByteDance also has an earlier product called MarsCode, more cloud-IDE oriented, forming an internal split.

Alibaba's Tongyi Lingma is one of the earliest Chinese AI coding assistants, released in 2023 as a plugin for VS Code and the JetBrains family, plugged into the Qwen series of Tongyi models. It has the deepest reach into enterprise customers inside the Alibaba Cloud ecosystem: DingTalk, Alibaba Cloud's internal teams, and many of their cloud customers all use it. Qwen is also the strongest open-source Chinese code LLM family.

Baidu's Wenxin Comate has one feature worth singling out: SPEC mode. It forces you to write a requirements document first, then has the AI write code against the document — packing the "PRD → design → development" engineering flow into the IDE. This approach has gained traction inside large Chinese enterprise R&D environments, because their code standards and compliance reviews are strict enough that freely-improvised AI code often can't pass review. Wenxin Comate is one of the few Chinese products to differentiate through engineering depth.

A few others. Tencent's CodeBuddy plugs into the Hunyuan model and lives inside the Tencent Cloud ecosystem. Zhipu's CodeGeeX is one of the earliest dedicated code models in China, going back to 2022, and today is the most fully open-sourced domestic code LLM. Huawei's CodeArts comes bundled with the Huawei Cloud DevOps suite and targets state-owned enterprises and large central-government clients.

Looking at the whole picture, China's real edges come down to three: noticeably better fit for Chinese-language scenarios, tight integration with domestic clouds, and a short path to enterprise deployment (plus mostly-free individual versions). The weak points are equally real: frontier model capability still lags Claude Opus and the GPT-5 line, and on complex multi-file, cross-repo agent tasks the gap is visible. The genuine room for differentiation runs along two lanes — one is to keep closing the model-capability gap, which DeepSeek, Qwen, and Zhipu are all working on; the other is to push specific industry workflows directly into the tool, which is exactly what Wenxin Comate's SPEC mode is doing.

Now the non-programmer track. Tools in this category — often labeled "Vibe Coding" — aim to let non-programmers build apps. You describe what you want in natural language, and the AI gives you a running app. This line has accelerated rapidly over the last year, with each player taking a different angle.

Lovable has been the runaway leader of this wave. Built by Swedish founder Anton Osika in 2024, it went from $0 to $400 million ARR in under a year, with only 146 employees. The product form is a chat box plus live preview: you type "I want a kanban board, draggable cards, syncing with Slack," and Lovable generates the full stack — frontend plus a Supabase database — that runs in your browser within minutes.

StackBlitz's Bolt.new takes a different route: it builds a complete full-stack app inside the browser, with no local backend, running inside an embedded WebContainer. You describe what you want, it generates the code, installs dependencies, and runs the app — all without you setting up any local environment. Bolt has spread fast in the founder and education segments.

Vercel's v0 carves out the UI design slice. You give it a description or a sketch, it generates a React component, and you can drop it straight into an existing project. v0 doesn't try to build whole apps. It nails the frontend component layer and is a high-frequency tool for designers and frontend engineers.

Replit Agent is the agent product from veteran online IDE Replit, released in September 2024. Its pitch is "from requirements to deployment, one agent runs the whole thing." Replit's edge is that it already has a complete cloud runtime; once the agent finishes, the app runs in their cloud immediately. Newer entrants like Base44, Mocha, and Glide target enterprise internal tooling — solving "a 5-person team needs an internal form or dashboard" type long-tail demand.

One sentence on the whole non-programmer track: Vibe Coding has driven the cost of building a demo to the floor. A person with product taste who has an idea used to need a week or more to build something demo-able. Now an afternoon is enough. But the gap between a demo and a real product still contains the entire software engineering industry. I'll get into that in Part III.

# III. The Road Ahead

## 3.1 Building an App Is Systems Engineering; AI Coding Solves Only One Piece

You see slogans these days: anyone who can't write a line of code can build an app and rake in money in their sleep. Set aside the demand side for a moment — let's look at the technical side first.

"A non-programmer can build an app directly" is partly true and partly needs discounting. To start, take a look at what building a serious feature inside a real company actually involves.

Software engineering breaks the work into stages, and there are formal standards for it. The most authoritative is ISO/IEC/IEEE 12207 — Systems and software engineering: Software life cycle processes. First released in 1995, last updated in 2017, it defines dozens of standard processes across the full software lifecycle. University software engineering textbooks across countries teach the same lifecycle: requirements, design, development, testing, release, operations.

Beyond the international standard, large Chinese companies have turned the lifecycle into their own published engineering specifications. In 2017 Alibaba released the Alibaba Java Coding Guidelines (project codename P3C), broken into six dimensions — coding rules, exception logging, unit testing, security rules, project structure, MySQL — with a companion IDE plugin downloaded over 1.6 million times. Meituan's tech blog (tech.meituan.com) has a long list of practical writeups on canary releases, incident postmortems, and launch flows. GitLab has gone the most extreme, open-sourcing its entire company R&D process as a public handbook (the GitLab Handbook, hundreds of thousands of words). All of these let outsiders see large-company R&D rhythms directly. Underneath, they all follow the same lifecycle.

A serious feature inside a large company runs through this flow: requirements (PRD + review), design (UI/UX + review + technical design + technical review), development (task breakdown + frontend/backend coding + integration + code review), testing (self-test + QA + bug loop + UAT), release (canary + full rollout + monitoring), and verification & wrap-up (data validation + retrospective + archiving). Two weeks on the short side, two to three months on the long side.

Every step in this flow plugs a real hole. PRD review plugs "what we built isn't what was wanted." Technical review plugs "we picked the wrong architecture and have to rebuild in six months." Code review plugs "the code runs but no one can maintain it." QA plugs "it crashes on launch." Canary release plugs "a bug ships to all users at once." Each step is the residue of decades of painful experience.

Back to AI. The pieces it can actually swallow today are not just code-writing. Walk through every stage and substep, and look at how much AI can really cut.

### 3.1.1 Requirements Stage (PRD + Review)

AI can already do quite a bit on the PRD itself: turn scattered ideas into a structured document (background, user persona, flow diagrams, acceptance criteria), scan for conflicts with existing features, list edge cases, even auto-generate analytics events and A/B test designs. But the PRD review meeting itself can't be replaced. The review needs four to six people from different roles in a room, arguing: business cares about ROI and release timing, product cares about user experience, engineering cares about implementation cost and tech debt, QA cares about testability. That kind of cross-role tug-of-war and consensus-building requires organizational coordination. AI can't help.

### 3.1.2 Design Stage (UI/UX and Technical Design)

The design stage actually has two tracks running in parallel: UI/UX and technical design. Each carries its own review.

The UI/UX track is the most thoroughly absorbed by AI. Tools like v0 and Figma AI can generate a runnable React component from a sentence in minutes, with the styling system wired up. The formal checks in design review — does the style match brand guidelines, are existing components being reused — can also be run by AI. But whether an interaction actually fits the brand voice, or what the user will do after this step, still needs a senior designer to call.

The technical-design track is also already useful with AI. Hand it a requirement, and it will list three candidate architectures with throughput, latency, and cost compared cleanly. But the final pick is still a human call, because the choice rides on a pile of organizational constraints AI doesn't know: which stack the team is fluent in, what compliance requirements apply, what SLA was promised externally, whether the key engineer is staying. And the technical review meeting is even more so. The arguments tend to be: why not X, why not Y, why does it have to be Z this time. Every line carries team history. AI hasn't sat through those meetings; it can't follow.

### 3.1.3 Development Stage (Coding and Review)

Development is AI's true main battlefield, but there are still hard bones inside it that AI can't crack.

Start with what AI directly handles. For task breakdown, Claude Code can already turn a PRD straight into an issue list and a dependency graph. Frontend and backend coding are the core use cases for Cursor + Claude / Codex; among senior engineers, 2x to 10x productivity gains are widely reported. For integration (getting frontend and backend talking through an API), AI can spin up a mock server, run contract tests, and flag schema mismatches. For code review, AI can run static analysis, check coding rules, and flag potential bugs.

But there is one layer of code review AI struggles with: architectural judgment. Will this change blur module boundaries, will this abstraction be maintainable three years out, does this decoupling fit the team's next-phase plan — those reviews still need a senior reviewer.

The harder bones are where the system meets the outside world. To wire up a third-party API (WeChat Pay, Stripe, Google Maps), AI can write the call code cleanly, but applying for the API key, negotiating commercial terms, passing KYC, registering callback URLs — those steps need a real person to walk the process. To set up access control (OAuth, SSO, internal IAM, cloud RBAC), AI can write the rule layer and the code layer, but who should have what access, whether GDPR compliance is met, who takes the blame when things go wrong — those remain organizational decisions. This class of blockers shares the same root cause as the problems the next section will hit on "non-programmer app building."

Putting it all together: in the development stage, 70% to 80% of the pure coding work is direct AI territory, and the remaining 20% to 30% splits between architectural judgment and gnarly debugging on one side, and external API integration / identity and permissions on the other — the parts that need humans to walk real-world processes.

### 3.1.4 Testing Stage (Automation and Human Acceptance)

The testing stage is AI's second main battlefield.

Self-test and QA — those two steps are almost fully AI's. In self-test, AI auto-generates unit and integration tests with much higher coverage than humans typically write by hand. In QA, AI can run full regression suites, do fuzzing (stress the program with random inputs to find crashes), and scan edge cases. Fuzzing used to be rarely run because the cost was too high relative to the payoff; AI has driven the marginal cost to nearly zero.

The bug loop is also closing in AI's favor. Locating code from a stack trace, generating a fix patch, submitting a PR — for many teams, 80% of P3 / P4 bugs now run end-to-end through an AI pipeline.

UAT (user acceptance testing) AI can't replace. This step needs real users in real scenarios clicking through to confirm the product matches expectations. AI can run every test for code correctness, but whether the product actually fits user demand only the user can judge.

### 3.1.5 Release Stage (Execution and Decision-Making)

Release splits into two sub-stages: execution and decision-making.

Execution, AI can fully take over. The details of canary release (release by percentage, by region, by user cohort) and full rollout can run automatically. Monitoring, alerting, anomaly detection, automatic rollback for predefined scenarios — all mature.

Decision-making is still on humans. Canary hits 10%, the core metric wobbles — do we keep pushing, roll back, or hold and investigate? Every action is a tradeoff: a 5% rollback cost moving forward, the risk of full release moving back. That kind of go/no-go call can't be made by staring at the dashboard. There's a layer of business rhythm, partner coordination, and market timing AI can't see.

A harder class is unprecedented incidents. A third-party dependency goes down and triggers cascading failures. A regional data center loses power. A security incident demands an emergency takedown. None of these are in the runbook, and the response plan is still set by the on-call engineer.

### 3.1.6 Verification and Wrap-up (Data Validation + Retrospective + Archiving)

Data validation: AI can pull metrics, build visualizations, and offer three to five plausible attribution explanations. But "this feature missed conversion targets — was it because users don't want it, the entry point is too deep, or pricing was wrong?" — that judgment needs a product manager combining qualitative data. The retrospective meeting AI can't replace. The core value of a retrospective is organizational learning: how this lesson becomes the next engineering rule, who takes what responsibility, whether the process needs to change. That's a human-to-human matter. Archiving is fully automatable: structuring the docs, linking the knowledge base, generating search indexes — those are AI's cleanest jobs.

Now compress the six stages into one picture.

The portion of total R&D work that AI can directly replace today, weighted by sub-step, is roughly 50% to 60%. Development and testing are the heaviest stages and AI is taking 70% to 85% of each. Requirements, design, and verification & wrap-up — AI can handle 30% to 50% of the substeps. In release, the execution side is nearly 100% automated, but go/no-go decision-making is still 0%.

Another way to put it: AI has driven the cost of "getting each stage done" way down. The cost of "calling it" at each stage still falls on humans.

Can the remaining 40% to 50% of human work keep getting eaten? That's the central question for predicting the next several years. There are two categories.

One is technically still short, but with a path forward: architecture choices grounded in team history, complex root-cause analysis, multi-file / cross-repo gnarly debugging, response to unprecedented incidents. Today AI can't do these mainly because context windows aren't long enough, organizational context isn't internalized, and long-term evolution isn't grasped. As models keep extending context, gain long-term memory, and get continually trained on team codebases, there's a real chance over five years of eating most of this work — pushing the overall pipeline to 70% to 80% AI.

The second category is what won't yield to more model capability: cross-person consensus, accountability, and dealing with the real world (KYC, commercial negotiation, compliance, legal liability). The blocker here is institutional, not capability-related. For AI to take over, it has to be able to exist as a legal entity — sign contracts, hold accounts, take consequences. There are already startups working on legal entities that "hold accounts, take responsibility, and carry insurance for AI agents," but this path involves law, regulation, and social acceptance. The window is 5 to 10 years. Once it opens, the remaining 20% to 30% gets eaten too, and software development moves to its next paradigm: humans reduced to two roles — problem-setter and final-decision-maker — and everything else is AI.

In the short term (next 2 to 3 years), pushing the pipeline from today's 50%-to-60% AI to 70%-to-80% AI is high-probability, driven by continued model capability gains and tooling fill-in. To go higher than 90%, model capability alone won't cut it. The institutional layer has to break.

This view has academic backing. The IEEE SWEBOK V4 (Software Engineering Body of Knowledge, released October 2024) lists 18 knowledge areas. AI Coding mainly covers "software construction" and parts of "software testing." For the remaining 16 areas (requirements engineering, software architecture, software security, software maintenance, software configuration management, software engineering economics, etc.), AI can only assist. Think of every app as a tree: AI has chopped off the tallest, thickest branch. The roots, trunk, and other branches still need a human to support them.

From an engineer's perspective, this shift is already redrawing the human-machine division of labor. My own feel: humans define problems, gate results, and handle the hard parts; AI writes code, runs tests, fixes routine bugs. From 2022 to 2026, the granularity of code review has been moving up a level. In 2022 programmers read every line. In 2024 they read PR-level diffs. In 2026, increasingly they read at the issue level — did the bug get fixed, did the feature actually work? Engineers haven't lost their jobs, but the share of code-writing in the job has dropped fast. Judgment, review, and acceptance are taking over.

## 3.2 Will There Be a "One-Click App" Tool for Non-Programmers?

To answer this, take the full enterprise R&D flow chart from the previous section and map it against the one-person scenario: which stages don't actually need AI replacement at all because they can simply be cut?

**Requirements stage**, almost entirely cut. You are the requester, decision-maker, and user all at once. What's in your head is enough to start. No PRD documentation, no cross-department review, no business alignment meetings.

**Design stage**, drastically reduced. Let AI auto-generate UI/UX; accept the vendor's default style; no brand-voice tug-of-war. The technical design is fixed by default inside Vibe Coding tools: Lovable gives you Next.js + Supabase, Bolt.new gives you WebContainer + embedded Vite. You don't choose, and you don't need to. The technical review meeting disappears entirely.

**Development stage** stays, but only the AI-writing-code part remains. No task breakdown meetings, no integration (frontend and backend live in the same generated stack), no code review (you check whether it runs and that's it).

**Testing stage**, sharply degraded. Self-test means clicking around yourself. QA and bug loop degrade to "do I find this comfortable?" In self-use scenarios there is no UAT. Lovable runs in the browser; if it crashes, regenerate.

**Release stage**, almost fully cut. One-person use has no canary. Full rollout means "open the URL myself." Monitoring and incident response don't apply at this scale. If something breaks, regenerate.

**Verification and wrap-up**, basically nonexistent. No data to validate (you're the only user), no retrospective, archiving handed to AI.

After all those cuts, the actual one-click flow has three steps left: you describe the requirement → AI generates and deploys → you use it yourself. Can this stripped-down flow be 100% AI-ized? The answer splits by scenario, and each scenario splits one more level.

### 3.2.1 Personal, Throwaway, Internal Tools

This category is essentially AI-ized today. But internally, there are two architectures.

The cleanest one is pure frontend, runs in the browser, and is gone when you close the tab. Anthropic's Artifact, OpenAI's Canvas, Vercel's v0, and Bolt.new all fall in this bucket. They generate tools with no backend, no database, no user login — just a chunk of HTML + JavaScript running in the browser, the stack as simple as React + Tailwind in one or two files. Throwaway calculators, UI prototypes, data visualizations, document format converters are typical use cases. Today these really are: one sentence to describe, a few minutes to get, no account needed. AI handles the whole thing end to end.

The slightly more complex case is a simple backend, with persistent data, possibly multi-user. Lovable's "frontend + Supabase" combo is the canonical example. Stack is roughly Next.js + Tailwind + Supabase (database + Auth) + Vercel deployment — basically the same standard stack I use myself for indie projects. AI writes 100% of the code, but the human still has to do a few dashboard operations: register a Supabase account, create a project, copy the URL and key; import the repo into Vercel, paste environment variables, hit Redeploy. AI can't open a browser console, so this part stays stuck. Personal expense tracking with cloud sync, small internal approval workflows, collaboration tools shared between a few friends — all in this tier.

Adding the two together, personal and internal small tools are about 95% AI-ized today, with the remaining 5% being a human pasting a few keys in a console.

### 3.2.2 Apps for Other People — App Store, or Anything That Takes Money

The reality here is: AI can write 95%+ of the code, and the human's main work is console clicking and going through compliance flows. Drilling down, the console-clicking layer further splits into technical and institutional pieces.

The technical layer: AI writes the code, the human pastes credentials. Spinning up a standard indie App stack (Next.js + Supabase + Stripe + Resend + Vercel), AI handles roughly: writing all the TypeScript code, writing the Prisma schema, running db push, writing Stripe checkout and webhook handlers, writing email templates, installing dependencies, git push to trigger deployment. The human still does dashboard work, for example:

- In Supabase: create a project, configure OAuth providers (paste Google / GitHub Client ID + Secret, which means going to Google Cloud Console and GitHub OAuth Apps to register first), configure redirect URLs.
- In Vercel: import the GitHub repo, paste environment variables, change the Build Command, manually Redeploy after editing env.
- In Stripe: create the Product, get the Price ID, after launch create a Webhook endpoint, copy the Webhook Secret back to Vercel.
- In Resend: get an API key, verify your sending domain.

External API integrations follow the same path. AI writes the call code; the human goes to each platform's console to handle key issuance, business negotiation, webhook URL registration, callback URL registration. AI can't open a browser today, so this can't be skipped.

The institutional layer is what AI will never handle:

- KYC identity verification (you bring an ID and bank account to register a corporate entity).
- Business qualifications (running payments in China requires ICP filing, business license, and sometimes a payment-license partnership).
- Legal liability (when user data leaks, fraud occurs, or IP is infringed, someone has to be on the hook).
- App Store distribution (Apple and Google won't issue developer accounts to AI agents; the annual real-name verification and fees go to a human).

Putting both layers together: an app meant for other people is roughly 90% AI plus 10% human dashboard today. "Build a real app from one sentence" is, strictly speaking, not possible. But "one sentence plus 10 console paste-keys" to build a real app — that we already have.

Does this match the "non-programmers can build apps" slogan? It matches it on the technical layer, and doesn't on the institutional one. A complete non-coder following Lovable + Stripe + Vercel onboarding docs can ship a SaaS that takes money. The precondition is that they're willing to register a company, pass Stripe KYC, sign compliance documents, and serve as the legal representative. That part has nothing to do with AI capability. It's about whether they're willing to be the boss.

### 3.2.3 Two Paths Forward

Can the remaining human work keep getting eaten? Two paths.

The technical path eats the 5% left in 3.2.1 and the 10% technical layer in 3.2.2. AI keeps absorbing more of the stripped-down flow: auto-wire payments, auto-handle OAuth, auto-deploy with domains and HTTPS, auto-monitor and auto-rollback. The bigger move is that browser agents are now product-ready — examples include Anthropic's Computer Use and OpenAI's Operator — letting AI log into Supabase, Vercel, and Stripe consoles, click around, paste keys, and Redeploy. Within one to two years, the two flavors of personal tooling in 3.2.1 will be 100% AI-ized. Most of the dozen-or-so dashboard ops in 3.2.2 will fall to browser agents. Pushing the technical layer of formal apps from today's 90/10 to 95/5 is high-probability.

The institutional path moves much slower and takes the institutional layer in 3.2.2. Whether AI legal entities can exist, hold accounts, sign contracts, and bear liability — those are questions for legislation and regulation, not for model capability. Some startups are building the legal scaffolding for "AI-agent-held accounts, with assigned liability and insurance coverage." But getting there requires legislation, case law, and social acceptance to align at once. The window is 5 to 10 years. Once it opens, real apps for strangers — apps that take money and ship to stores — become reachable through one-click tools too. The whole map of software distribution gets rewritten.

In one sentence: personal tools are one-click today; apps for others are at "one sentence plus 10 paste-keys"; in 1 to 2 years browser agents take the paste-key layer too; in 5 to 10 years AI legal entities go live and the last institutional blocker is finally crossed.

## 3.3 Will This Wave of AI Coding Reshape the PC / Mobile App Ecosystem?

Yes, but the direction of reshaping runs counter to most people's intuition. First, the variables.

### 3.3.1 100x Supply, 1x Demand

Sections 3.1 and 3.2 already covered the "cost of building an app." Today, with Lovable + Vercel + Stripe, what used to take 5 people 6 months can ship in 1 person 1 weekend. Supply-side capacity is up at least 10x to 100x.

But demand barely moved. Each person still has 24 hours a day. Average screen time on phones is already around 5 hours, near saturation. The apps a person actively uses on their phone is 10 to 20; they have 60 to 100 installed, and most of them got opened once and never again. That structure has been stable for the past decade.

Supply 100x, demand 1x: the only outcome is the middle layer gets crushed flat. Which layer specifically gets crushed depends on the type.

The first to fold is long-tail tool SaaS. Reimbursement systems, internal dashboards, personal expense tracking, vocabulary apps, step counters, ad-hoc form generators — small tools that lived on annual subscriptions can now be built by a user themselves in half an hour with Lovable. A SaaS company charging $100 a year and explaining its features is fighting an AI-generated version that's free and fits the user better. This layer disappearing wholesale is just a matter of time.

Vertical industry SaaS is more complicated. Contract management for law firms, scheduling for hospitals, parent-school communication for elementary schools — these have industry-specific knowledge built in and can't be one-shot generated. But they will face pressure: a customer's internal IT team can use the same AI tools to generate an internal version and stop paying the subscription. This layer will get squeezed by price wars and lose maybe half its market.

Social, content, e-commerce, maps — that layer barely moves. The value isn't in the code. The next section explains why.

### 3.3.2 Top Apps Won't Get Replaced; They'll Get Stronger

WeChat, TikTok, Taobao, Google Maps, Instagram, WhatsApp — AI coding can't touch these top apps' core. Four reasons.

Network effects. WeChat's value is 90% the other 1 billion users on it. You can't build a WeChat used only by yourself. Lovable can generate a WeChat-look-alike app overnight, but no one inside is someone you want to chat with.

Data accumulation. The 8 years of user behavior data TikTok has built up is the real moat behind its recommendation algorithm. A new "AI-generated short video app" starts with zero data; from day one its recommendation system is orders of magnitude worse.

Content and supply ecosystems. Taobao has millions of merchants, hundreds of millions of SKUs, stable logistics, and stable payment. AI generates "my own shopping app" and there's nothing inside it.

Distribution gates. Apple, Google, Meta, and ByteDance own the spot a user looks at first when they unlock their phone. AI coding can't touch this layer at all.

The counterintuitive part: AI coding will deepen these top apps' advantages. They use AI internally to ship 10x faster, to handle customer service, to do recommendations, to generate content, to fight fraud. Scale advantages plus AI widen the product-quality gap further. A new founder used to be able to dream of "make something better than WeChat" and ride that dream for a few years. In the AI coding era, even the dream is gone.

### 3.3.3 Long-Tail Apps Decay into On-Demand-Generated Capabilities

Combining 3.3.1 and 3.3.2, the mobile picture in a few years could look like this.

Top apps stay around 20 to 30, similar to today, but each one is stronger and harder to displace. WeChat, TikTok, Taobao, banking apps, maps, email, camera — these stay installed, used long-term, accumulating data across years.

The middle layer (tool / single-function / long-tail) collapses from today's dozens to under 10. Calendar, notes, password managers — anything where personal data accumulates over time — survive. Most other small tools get replaced.

What replaces them is on-the-fly generated Capabilities. You tell the AI assistant on your phone "I want to track expenses for this trip," and the AI assembles a form plus table plus simple chart on the spot. Trip ends, you delete it. Next trip generates a new one. Anthropic's Artifact, OpenAI's Canvas, and Apple Intelligence's App Intents are already moving in this direction. They just haven't reached every user yet.

These Capabilities have a distinct shape: throwaway, personalized, zero-install, no monthly fee, never in an App Store. They are a different form factor from today's apps.

### 3.3.4 The Reshaped Ecosystem: A Three-Layer Structure

Putting it all together, the App ecosystem in a few years looks like three layers stacked.

**Top-app layer**. WeChat, TikTok, Taobao, Apple, Google, Meta. Anchored by network effects, data, and content ecosystems. AI coding makes them stronger. The number of players in this layer shrinks; each remaining player's share grows.

**Assistant layer**. This is the one that emerges. The user's entry point shifts from opening a particular app to telling an AI assistant a sentence. The assistant calls underlying models to generate one-shot tools or calls a top app's API to get things done. The current prototypes for this layer are general assistants like ChatGPT, Claude, Apple Intelligence, and Google Gemini. Who owns this layer is the biggest battle of the next few years, because it could chip away at the App Store's distribution position.

**Model layer**. Anthropic, OpenAI, Google, plus DeepSeek, Alibaba's Qwen, ByteDance's Doubao. They make money selling tokens and capability. AI coding's prosperity flows to this layer first, because every Capability generation and every assistant call burns tokens.

The new ecosystem means different things for different players. Top app platforms keep growing; the model layer keeps growing. The middle assistant layer is the contested ground — there's room for one or two new giants, or for the existing players to split it. The hardest spot to be in is companies that built long-tail SaaS, unless they pivot in time to become Capability providers in the assistant layer, or go deep enough vertically to become a "small top" in their industry.

A regular person's view: the phone still has 20 to 30 frequently used apps, similar to today; an AI assistant on call generates throwaway tools as needed; the dozens of useless apps installed and never reopened are gone. The first action when picking up the phone shifts from finding the right app icon to telling the AI a sentence. That shift in entry-point form factor is the biggest since the iPhone.

# IV. Closing Thoughts

Compress the article into a few lines you can hold in your head.

**Principles**. AI writes code through a fusion of two things. One: code training has lifted general models to a new plateau, embedding "break a problem into steps, then make every step hold" into the model's default behavior. The most counterintuitive aspect is that the real beneficiaries of code training go far beyond the code-writing task itself — the entire language model's logic ability gets pulled up by it. Two: RLVR (reinforcement learning from real execution feedback) trained models from "able to write" to "able to write correctly," and over the past two years pushed coding ability to today's level. Code's three properties — strong regularity, objective right-or-wrong, built-in documentation — make it natural training material for models, and now a core ingredient in making general models smarter.

**Company history**. From OpenAI dropping Codex into GitHub Copilot's muscle memory in July 2021; through ChatGPT's takeoff in November 2022 flattening the pre-AI external-brain ecosystem (Stack Overflow, Kite, Codecademy); through October 2024 when the upgraded Claude 3.5 Sonnet made "AI can really write code" true for the first time and Cursor's codebase indexing defined the new IDE pattern; through the 2024-2025 pivot to agents; to the last year of three-way ARR competition in the billions among Codex CLI, Claude Code, and Cursor. In China, ByteDance Trae, Alibaba Tongyi Lingma, Baidu Wenxin Comate, and Zhipu CodeGeeX started in parallel. The non-programmer track — Lovable, Bolt.new, v0, Replit Agent — drove the cost of building a demo to the floor. These five years have been one of the fastest-evolving product surfaces in AI.

**Systems engineering**. Software engineering is a complete lifecycle defined by ISO/IEC/IEEE 12207, codified in Alibaba P3C and Meituan's tech blog, and covered across 18 knowledge areas in SWEBOK V4: requirements, design, development, testing, release, verification & wrap-up. The portion AI can directly replace today, weighted across substeps, is roughly 50% to 60%. Development and testing get hit hardest (70% to 85% each); requirements, design, and verification & wrap-up sit at 30% to 50%. Of the remaining 40% to 50% human work, the technical part still has room (architecture choice, complex root-cause analysis, gnarly debugging) — over a few years AI could push the whole pipeline to 70% to 80%. The institutional part (cross-person consensus, accountability, real-world interfacing) is for law and regulation to solve, not for model capability. Software engineering's complexity has been redistributed, not eliminated.

**One-click app**. Personal, throwaway, internal tools are basically one-click today (95% AI plus 5% console paste-keys). Apps meant for other people, the kind that ships to App Store or takes money, are roughly 90% AI plus 10% human dashboard today. "One sentence plus 10 paste-keys" can build a real app, but the precondition is the human is willing to register a company, pass KYC, and serve as legal representative. Two paths forward: in 1 to 2 years browser agents (Computer Use, Operator) eat the paste-key layer; in several years, if AI legal entities become viable, the institutional blocker finally falls.

**Ecosystem**. On the supply side, AI coding multiplies capacity 10x to 100x; demand barely moves. The middle layer gets flattened: long-tail SaaS disappears wholesale, vertical industry SaaS loses half its market. Top apps (WeChat, TikTok, Taobao, Apple, Google, Meta) don't get replaced. Network effects, data, content ecosystems, distribution gates, plus AI-driven internal speedups make them stronger. Long-tail apps decay into on-demand-generated Capabilities: throwaway, personalized, zero-install, never in an App Store. The few-years picture is three layers stacked: top-app platforms, AI assistant + Capability, model layer. The first action when picking up the phone shifts from finding an icon to telling the AI a sentence — the biggest entry-point shift since the iPhone.

**Where to position next**. Several paths are open in this new division of labor: an engineer who collaborates with AI, taking on more judgment, review, and acceptance work; a product person who can wield AI tools to solve real business problems, who knows clearly which steps to hand off to AI and which to keep on humans; a founder who uses AI to do solo what used to take ten people, betting on a position in the new AI-assistant + Capability ecosystem; or a vertical specialist building a "small top" inside an industry's domain knowledge that AI coding can't replicate. Each of these paths is wider than five years ago. But the dream of "starting from scratch and building the next WeChat" really is gone — AI coding makes the top deeper, replaces most of the long tail, and opens up an entirely new AI assistant layer waiting to be claimed.

One sentence: AI raised the floor on building software dramatically. The ceiling is still set by humans. The biggest winners in the new map are top apps, model companies, and the few players who manage to claim ground in the assistant layer. Everyone else has to find their own leverage point inside the new division of labor.

---

## Author's Other Articles

- [Brothers, the Real Vibe Writing Era Has Arrived](https://x.com/snowboat84/status/2047828585537548574)
- [The Most Detailed AI Learning Roadmap on the Internet](https://x.com/snowboat84/status/2047457686070141051)
- [The Three Most Useful Claude Skills Everyone Should Use](https://x.com/snowboat84/status/2047110768773197834)
- [SpaceX Origin Story (One): Betting Everything on the Last Launch](https://x.com/snowboat84/status/2046743964192276766)
- [Jensen vs. the Hawks - Can America Actually Win the Chip Blockade on China?](https://x.com/snowboat84/status/2046022377830801725)
- [How AI Will Disrupt Education, and How Ordinary People Should Claim the New Niche](https://x.com/snowboat84/status/2044932338262667509)
- [To All Physics Heroes: Physics Is Dead, Pivot to AI](https://x.com/snowboat84/status/2044584627046920278)
- [No Coding, No Funding, No Employees — How One Person Hit $20M a Year](https://x.com/snowboat84/status/2044216044575998136)
- [Brothers, Get Clear: Are You Working for X, or Is X Working for You?](https://x.com/snowboat84/status/2043842017260908743)
- [A One-Person Company Profiting $400M: Scam, or a Repeatable Bonus?](https://x.com/snowboat84/status/2043493870265422223)
- [The Q1 2026 Mass Layoffs: Is AI the Scapegoat?](https://x.com/snowboat84/status/2042766853404307931)
- [Return to the Stars: Does This Lunar Mission Matter?](https://x.com/snowboat84/status/2042405716380835998)
- [Why Zhang Xuefeng Couldn't Succeed in America](https://x.com/snowboat84/status/2042045634245746743)
- [The 2026 Corporate Autopsy: Without AI, Will Your Company Last the Year?](https://x.com/snowboat84/status/2041672997959057517)

---

## References

- [Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet (Anthropic, 2024-10)](https://www.anthropic.com/news/swe-bench-sonnet) - 49% on SWE-bench Verified
- [SWE-bench Verified Leaderboard (BenchLM)](https://benchlm.ai/benchmarks/sweVerified) - April 2026 SWE-bench Verified rankings
- [SWE-bench Pro Leaderboard (Scale)](https://labs.scale.com/leaderboard/swe_bench_pro_public) - SWE-bench Pro rankings
- [Why 46% Beats 81%: SWE-bench Pro Leaderboard (Morphllm, 2026)](https://www.morphllm.com/swe-bench-pro) - SWE-bench Pro vs Verified analysis
- [OpenAI Codex (AI agent) - Wikipedia](https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)) - Codex history and CLI relaunch timeline
- [OpenAI Codex Statistics 2026 (Gradually)](https://www.gradually.ai/en/codex-statistics/) - 3M weekly active developers
- [Claude Code Statistics 2026 (Gradually)](https://www.gradually.ai/en/claude-code-statistics/) - 4% of GitHub commits
- [Cursor's Anysphere nabs $9.9B valuation (TechCrunch, 2025-06)](https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/) - Cursor early data
- [Cursor in talks at $50B valuation hitting $2B ARR (TNW, 2026-04)](https://thenextweb.com/news/cursor-anysphere-2-billion-funding-50-billion-valuation-ai-coding) - Cursor's latest valuation
- [As Lovable hits $200M ARR (TechCrunch, 2025-11)](https://techcrunch.com/2025/11/19/as-lovable-hits-200m-arr-its-ceo-credits-staying-in-europe-for-its-success/) - Lovable growth curve
- [Guide to the SWEBOK v4.0 Has Been Released (basicinputoutput, 2024-10)](https://www.basicinputoutput.com/2024/10/guide-to-swebok-v40-has-been-released.html) - SWEBOK V4 release and 18 knowledge areas
- [SWEBOK Evolution (IEEE Computer Society)](https://www.computer.org/volunteering/boards-and-committees/professional-educational-activities/software-engineering-committee/swebok-evolution) - Official SWEBOK info
- [CodeBERT GitHub (Microsoft)](https://github.com/microsoft/CodeBERT) - CodeBERT repository and timeline
- [CodeT5 GitHub (Salesforce)](https://github.com/salesforce/CodeT5) - CodeT5 repository and timeline
- [ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes](https://www.iso.org/standard/63712.html) - International software lifecycle standard
- [Alibaba Java Coding Guidelines (P3C)](https://github.com/alibaba/p3c) - Alibaba's 2017 public engineering rules + IDE plugin, six dimensions
- [Meituan Tech Blog](https://tech.meituan.com/) - Practical writeups on canary releases, postmortems, launch flows
- [GitLab Handbook](https://handbook.gitlab.com/) - GitLab's full company R&D process, open-sourced
- [Kite is saying farewell (Adam Smith blog, 2022-11)](https://kite.com/blog/product/kite-is-saying-farewell-and-open-sourcing-its-code/) - Kite shutdown announcement, "10+ years too early to market"

---

## Appendix: Original Draft

> The original draft of this article is in Chinese, archived in the source piece "两万字科普：AI 为什么会编程——原理、历史与未来.md" (root directory of this repo). It is preserved verbatim there and not duplicated here.
