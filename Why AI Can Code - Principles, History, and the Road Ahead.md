## Table of Contents

- I. Principles: From Prehistory to Now
  - 1.1 The Prehistory: Two Paths for Code Tooling
  - 1.2 The Turning Point: How the GPT Series Changed the Game
  - 1.3 Why Code Is Especially Good Training Data
  - 1.4 RLVR: From "Able to Write" to "Able to Write Correctly"
- II. A Brief History of AI Coding Companies
  - 2.1 Origins: The Two Camps and Early Tools (2020 – 2022)
  - 2.2 From Editor Tools to Agents (2023 – 2026)
  - 2.3 The Chinese Market and the Non-Programmer Track
- III. The Road Ahead
  - 3.1 Building an App Is Systems Engineering; AI Coding Solves Only One Piece
  - 3.2 Will There Be a "One-Click App" Tool for Non-Programmers?
  - 3.3 Will This Wave of AI Coding Reshape the PC / Mobile App Ecosystem?
- IV. Closing Thoughts


Let's review AI coding.

Back in 2021, AI coding was still mostly an academic topic. Programmers treated it as a side tool. GitHub Copilot launched that year and got a burst of attention, but the debate was narrow: should I use this thing, and will it make me dumber?

By April 2026, the picture is completely different. About 135,000 public GitHub commits a day are now produced directly by Claude Code, roughly 4% of all public commits across the platform. OpenAI's Codex CLI, one year after its relaunch, has crossed 3 million weekly active developers. Cursor's parent company Anysphere went from 0 to $2 billion in ARR over two years, the fastest curve in SaaS history.

In four or five years, AI coding went from a research demo to a daily tool for tens of millions of people.

I've been writing professional code for over ten years, and these tools have been part of my daily workflow for the last three. This piece is my attempt to answer three questions people keep asking, but rarely get a clean answer to:

- How does AI manage to write code at all?
- How did this happen over the past five years?
- In the next few years, can ordinary people really build their own apps?

I'll go in order: how it works, how we got here, and what comes next. You don't need a technical background.

# I. Principles: From Prehistory to Now

## 1.1 The Prehistory: Two Paths for Code Tooling

Before ChatGPT, there were two ways people tried to get machines to write code.

One path was self-service for programmers, through forums and IDE tools. Stack Overflow's promise was simple: every error message and every fix humanity had ever found, all in one place. You wrote code, hit an error, pasted the message, and waited for someone in the community to answer. China's version was CSDN, a developer community founded in 1999. By 2024 it had 40 million registered users and 12 million monthly actives, making it the Chinese-language external brain for domestic programmers. When I was learning to code in 2014, my daily loop was simple: write code, hit an error, paste it into Stack Overflow, edit the answer, paste it back. That loop lasted for about 15 years before ChatGPT arrived.

IDEs were trying to help too. Microsoft Visual Studio, first released in 1997, had IntelliSense. Eclipse, open-sourced by IBM in 2001, had Content Assist. JetBrains IntelliJ IDEA, also from 2001, had smart completion. These were the "intelligent" prompts of their time, but in practice they were closer to dictionary lookups. You typed `str.`, and the IDE listed every method on the String class. It didn't understand what you wanted. It looked up a table.

The other path was academic program synthesis: start with a formal specification, then derive code through formal logic. That line goes back to the 1970s and stayed at toy scale for half a century. The only industrial-strength example most people ever used was FlashFill, led by Sumit Gulwani at Microsoft Research and built into Excel in 2013. Give it a few examples, and it guesses the transformation rule for the whole column. But this approach needed formal specs or clean examples. It couldn't deal with plain language.

Around 2020, neural-network-based code tools also started showing up, including Microsoft's CodeBERT in September 2020 and Salesforce's CodeT5 in 2021. They were smarter autocomplete, but the same wall was still there: they didn't really understand natural language. You couldn't talk to them. They could finish a line of code, but they couldn't take on a task.

Put these threads next to each other, and the real bottleneck becomes clear. If a machine is going to write code for you, it first has to understand what you're asking for. Before 2018, nobody had really solved that.

## 1.2 The Turning Point: How the GPT Series Broke the Door Open

The GPT series changed that. In June 2018, OpenAI put forward a simple recipe: pretrain a model on a huge amount of text so it learns to guess the next word, then fine-tune it for specific tasks. GPT-1 had 0.117B parameters and was still a research prototype. GPT-2, released in February 2019, jumped to 1.5B. GPT-3, released in May 2020, hit 175B, about 100 times larger than GPT-2. Once models reached that scale, they understood natural language well enough that writing code suddenly looked within reach.

The model that writes code and the model that chats are built on the same Transformer architecture. They do the same basic thing: look at the tokens before, then predict the next token. To the model, Python code and a Chinese novel are both token sequences. It doesn't "know" it's writing code. It's just picking the next likely token from the context.

Take the simplest Fibonacci function:

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

The model writes this one token at a time. After `def fib(n):`, the likely next token is a newline plus indentation. Then `if`. Then `n`. Then `<`. Then `2`. Then `:`. Then `return`. It keeps going until the function is done. After seeing millions of lines of GitHub code again and again, this next-token game ends up encoding syntax, idioms, variable names, and comment style.

## 1.3 Why Code Is Especially Good Training Data

Code turns out to be unusually good material for language models. Here's why.

The most obvious reason is regularity. After `for i in range(10):`, the next thing is an indented loop body. The rule is fixed, much more stable than natural language. In normal writing, you can say the same thing ten different ways. In code, there are usually only two or three natural ways to write it. That makes the patterns much easier for a model to compress.

The deeper reason is that code has objective right and wrong. Give a function a test suite, run the tests, and you know whether it works. Natural language has nothing like that. Whether a poem is good, or whether an essay moves you, can't be graded automatically. This property of code becomes decisive later.

The data is also unusually clean. Every README, every docstring before a function, every commit message in an open-source repo is free "natural language ↔ code" training data. Every code model after GPT-3 has fed on that dividend, and the volume is far beyond anything humans could label by hand.

The first wave treated code as its own specialized skill. In 2021, OpenAI took GPT-3 and kept training it on more than 100 GB of public GitHub code, a technique called continued pretraining. The result was Codex. On HumanEval, OpenAI's 164-problem coding benchmark, Codex reached 28.8% pass-at-1, the best result at the time. Back then, OpenAI's API had `code-davinci` and `text-davinci` as separate models. One wrote code. The other wrote prose.

After GPT-4, that split disappeared. Anthropic, OpenAI, and Google all started mixing large amounts of code straight into the pretraining data for their general models. Public estimates put the share at 20% to 40%. There's no longer a separate code model. One Claude, GPT, or Gemini handles both prose and code.

Why merge them? Because adding a lot of code to training makes the model better at math, logic, and even ordinary language tasks. DeepMind, Google Brain, and OpenAI all saw this between 2022 and 2023. The intuition is simple: code forces the model to reason step by step. Each step has to hold, or the whole thing breaks. Once the model learns that habit, it transfers to non-code tasks too. Code training is now one of the main ingredients behind stronger general models.

## 1.4 RLVR: From "Able to Write" to "Able to Write Correctly"

The key technique for code models is reinforcement learning from execution feedback. The loop is simple: the model writes code, the code runs in a real runtime, the test suite runs, the pass/fail result comes back as a reward, and the model learns from it. This is called RLVR, or Reinforcement Learning from Verifiable Rewards. "Verifiable" is the important word. The reward doesn't come from human annotation, which is expensive and noisy. It comes from automatic machine grading. Code, math problems, and formal logic all fit this setup.

DeepSeek pushed this approach hard with R1 in early 2025: first train reasoning with reinforcement learning on math and code, then transfer that ability back to normal conversation. On several benchmarks, it caught up with the closed-source frontier models of the time. The same RLVR template sits behind much of the training for Claude Code, OpenAI o3, and Codex. It only became mainstream after 2024, and it's the main reason coding ability improved so quickly over the last two years.

So today's coding ability comes from two things. First, code training has made general models much stronger, pushing the habit of "break a problem into steps, then make every step hold" into their default behavior. Second, large-scale reinforcement learning on tasks with objective right and wrong, like code, math, and reasoning, has trained models from "can write" to "writes correctly." Put those together, and you get the engine behind AI coding.

# II. A Brief History of AI Coding Companies

## 2.1 Origins: The Two Camps and Early Tools (2020 – 2022)

GPT-3 launched in May 2020 with 175B parameters. Once the scale was there, OpenAI finally had a model it could sell to developers. In July 2021, it kept training GPT-3 on public GitHub code, produced a 12B-parameter model called Codex, and shipped it inside GitHub's new Copilot product. That was the first time AI entered programmers' muscle memory. The habit of hitting Tab hundreds of times a day to accept completions started that summer.

But Copilot was still limited. The context window was only 2k to 8k tokens. It could see only a local slice of the current file. And it was passive: if you stopped typing, it stopped too. It was good at finishing a line, not doing a task.

Anthropic started almost in parallel. Its two leaders, Dario and Daniela Amodei, are siblings. They left OpenAI at the end of 2020 and got the company off the ground by January 2021, bringing several GPT-3-era core researchers with them, including Tom Brown, Jared Kaplan, and Sam McCandlish. Anthropic built its identity around honesty, controllability, and long-context understanding. That later became Claude's natural edge in coding: it can read long codebases, follow complex instructions, and say "I'm not sure" when it isn't sure.

In November 2022, OpenAI released ChatGPT, and AI coding shifted from "completion tool" to "conversation partner." Early ChatGPT still made things up when writing code, often with full confidence, including APIs that didn't exist. Claude, arriving around the same time, felt noticeably more accurate to many engineers. It became the quiet favorite among people who were paying close attention.

After ChatGPT took off, the old "external brain for programmers" ecosystem started to break. Stack Overflow took the cleanest hit. Founded in September 2008 by Joel Spolsky and Jeff Atwood, the programmer Q&A site peaked in 2017 with more than 300,000 new questions per month, more than 100 million monthly visits, and 10 million registered users. After ChatGPT, monthly new questions fell to about 87,000 in 2023 and under 60,000 in 2024. By December 2025, the count was below 4,000, back near the level of 2008, when the site had just launched. CSDN moved in the same direction. Kite, an early AI-completion startup founded in 2014, shut down in November 2022. Founder Adam Smith wrote that the company "failed to deliver our vision of AI-assisted programming because we were 10+ years too early to market, i.e., the tech is not ready yet." Even 500,000 monthly active users couldn't keep it alive. Tutorial sites like Codecademy and W3Schools kept losing traffic too.

## 2.2 From Editor Tools to Agents (2023 – 2026)

In 2023, GitHub added chat to Copilot. But Copilot Chat still felt bolted on: code in the main editor, AI in the sidebar. The AI was literally kept in the corner.

Cursor was the product that changed the editor itself. Its parent company, Anysphere, was started by four MIT students in 2022. Their key bet was to fork VS Code instead of writing another plugin. A fork is much harder to maintain, but it lets you redesign the editor around AI. Cursor's real technical contribution was codebase indexing: vectorize the whole project so the AI can finally see the whole codebase. That pattern became the industry default: use someone else's model, usually Anthropic's or OpenAI's, then build your own layer around indexing, context, and workflow.

In October 2024, the upgraded Claude 3.5 Sonnet launched. On SWE-bench Verified, a real GitHub bug-fix benchmark with human-verified problems, its score jumped from the previous generation's 33% to 49%. That was the first moment when "AI can really write code" felt true. Cursor changed noticeably over the following months, and engineers moved from Copilot to Cursor + Claude in large numbers. I switched in late 2024. Within three months, my code output felt like it had doubled.

Through 2024 and 2025, the whole category moved from "completion inside the IDE" toward "agents." Devin, released by Cognition Labs in March 2024, was the first product to call itself an "AI software engineer." The marketing ran ahead of the substance, but it set the tone for the next product category: end-to-end task agents. Give the agent a goal; it breaks the task down, writes the code, runs the tests, and fixes the bugs.

Since then, competition has centered on three products. Codex is OpenAI's second use of that name. The first Codex was a 2021 GPT-3 derivative that powered Copilot, then was deprecated in 2023 in favor of GPT-4. On April 16, 2025, OpenAI brought the name back for a new product: a Rust-written CLI agent. The relaunch picked up momentum fast. By March 2026, weekly active users had crossed 2 million. In April, they passed 3 million, up 50% month over month. Inside ChatGPT Enterprise, Codex users grew six-fold from January to April.

Claude Code went deepest with working engineers. Released by Anthropic in 2025, it leaned on Claude's strength with long codebases, hit roughly $2.5 billion ARR by early 2026, and now produces about 135,000 public GitHub commits per day, around 4% of all public commits on the platform. SemiAnalysis projects that the share will pass 20% by the end of 2026.

Cursor's own scale kept climbing. By February 2026 it was at $2 billion ARR. In April it raised at a $50 billion valuation — the fastest 0-to-$2-billion ARR curve in SaaS history.

A few other players have their own niches. Windsurf, formerly Codeium, is another AI-native IDE, though things got complicated after it was acquired in mid-2025. GitHub upgraded Copilot into Agent Mode and Coding Agent, and many existing users simply followed the upgrade path.

Among senior engineers today, the mainstream stack is Cursor plus Claude Code: an IDE for writing code, and a CLI for handing off larger tasks.

## 2.3 The Chinese Market and the Non-Programmer Track

Two side tracks deserve their own section: Chinese vendors, and tools for non-programmers.

The Chinese market developed in parallel with the overseas market. Big tech companies each claimed a lane, while the open-source camp built its own.

ByteDance built Trae, the Chinese AI-native IDE that feels closest to Cursor. It launched around late 2024. Free access for individual users helped it spread quickly through the domestic developer community. Trae plugs into ByteDance's own Doubao model, and on Chinese-language projects with Chinese comments it often feels smoother than using Cursor directly. ByteDance also has an earlier product, MarsCode, which is closer to a cloud IDE.

Alibaba's Tongyi Lingma is one of the earliest Chinese AI coding assistants. It launched in 2023 as a plugin for VS Code and JetBrains IDEs, powered by the Qwen family of Tongyi models. Its strongest position is inside the Alibaba Cloud ecosystem: DingTalk, Alibaba Cloud's internal teams, and many cloud customers all use it. Qwen is also the strongest open-source Chinese code LLM family.

Baidu's Wenxin Comate has one feature worth calling out: SPEC mode. It makes you write a requirements document first, then has the AI write code against that document. In other words, it packs the "PRD → design → development" flow into the IDE. That fits large Chinese enterprise R&D environments, where code standards and compliance reviews are strict enough that improvised AI code often can't pass review. Wenxin Comate is one of the few Chinese products that stands out through engineering process rather than just model access.

There are others. Tencent's CodeBuddy plugs into the Hunyuan model and lives inside the Tencent Cloud ecosystem. Zhipu's CodeGeeX is one of China's earliest dedicated code models, going back to 2022, and is now the most fully open-sourced domestic code LLM. Huawei's CodeArts comes bundled with the Huawei Cloud DevOps suite and targets state-owned enterprises and large central-government clients.

China's real advantages are clear: better fit for Chinese-language work, tight integration with domestic clouds, and easier enterprise deployment, often with free individual versions. The weak points are just as clear. Frontier model capability still trails Claude Opus and the GPT-5 line, and the gap shows up on complex multi-file, cross-repo agent tasks. Differentiation now has two paths. One is to keep closing the model gap, which DeepSeek, Qwen, and Zhipu are all trying to do. The other is to bake specific industry workflows into the tool, which is exactly what Wenxin Comate's SPEC mode is doing.

Then there's the non-programmer track. These tools, often called "Vibe Coding" tools, try to let non-programmers build apps. You describe what you want in plain English, and the AI gives you a running app. The market has moved fast over the last year, with each product taking a different angle.

Lovable has been the clear leader. Built by Swedish founder Anton Osika in 2024, it went from $0 to $400 million ARR in under a year, with only 146 employees. The product is a chat box plus a live preview. You type, "I want a kanban board, draggable cards, syncing with Slack," and Lovable generates the full stack, frontend plus a Supabase database, running in your browser within minutes.

StackBlitz's Bolt.new takes a different route. It builds a complete full-stack app inside the browser, with no local backend, running inside an embedded WebContainer. You describe what you want, it generates the code, installs dependencies, and runs the app, all without asking you to set up a local environment. Bolt has spread quickly among founders and educators.

Vercel's v0 focuses on UI. Give it a description or a sketch, and it generates a React component you can drop into an existing project. v0 doesn't try to build whole apps. It stays on the frontend component layer, which makes it a high-frequency tool for designers and frontend engineers.

Replit Agent is the agent product from veteran online IDE Replit, released in September 2024. Its pitch is "from requirements to deployment, one agent runs the whole thing." Replit's edge is that it already has a full cloud runtime. Once the agent finishes, the app runs in Replit's cloud immediately. Newer entrants like Base44, Mocha, and Glide target internal enterprise tools, the kind of long-tail demand where a five-person team just needs a form or dashboard.

The takeaway: Vibe Coding has crushed the cost of building a demo. A person with product taste used to need a week or more to build something demo-able. Now an afternoon can be enough. But the gap between a demo and a real product is still where most of software engineering lives. That's what Part III is about.

# III. The Road Ahead

## 3.1 Building an App Is Systems Engineering; AI Coding Solves Only One Piece

You see slogans everywhere now: anyone can build an app, even if they can't write a line of code, and maybe even make money while they sleep. Put the demand side aside for a moment. First, look at the technical side.

"A non-programmer can build an app directly" is partly true, but only with a big discount applied. Start with what it actually takes to build a serious feature inside a real company.

Software engineering breaks the work into stages, and there are formal standards for it. The most authoritative one is ISO/IEC/IEEE 12207, "Systems and software engineering — Software life cycle processes." It was first released in 1995, last updated in 2017, and defines dozens of standard processes across the full lifecycle. Software engineering textbooks around the world teach the same basic flow: requirements, design, development, testing, release, operations.

Large Chinese tech companies have turned the same lifecycle into their own public engineering rules. In 2017, Alibaba released the Alibaba Java Coding Guidelines, project codename P3C, covering six areas: coding rules, exception logging, unit testing, security rules, project structure, and MySQL. Its companion IDE plugin has been downloaded more than 1.6 million times. Meituan's tech blog has a long list of practical writeups on canary releases, incident postmortems, and launch flows. GitLab went even further and published its company R&D process as a public handbook with hundreds of thousands of words. Different companies, same underlying lifecycle.

A serious feature inside a large company usually runs through this flow: requirements (PRD + review), design (UI/UX + review + technical design + technical review), development (task breakdown + frontend/backend coding + integration + code review), testing (self-test + QA + bug loop + UAT), release (canary + full rollout + monitoring), and verification & wrap-up (data validation + retrospective + archiving). A small one takes two weeks. A larger one takes two or three months.

Every step exists because something painful happened before. PRD review prevents "we built the wrong thing." Technical review prevents "we picked the wrong architecture and need to rebuild in six months." Code review prevents "it runs, but nobody can maintain it." QA prevents "it crashes on launch." Canary release prevents "one bug reaches every user at once." These steps aren't ceremony. They're scar tissue.

So what can AI actually take over? More than code-writing, but not everything. Walk through the stages, and the limits become easier to see.

### 3.1.1 Requirements Stage (PRD + Review)

AI can already do quite a lot with the PRD itself. It can turn scattered ideas into a structured document with background, personas, flows, and acceptance criteria. It can scan for conflicts with existing features, list edge cases, and even generate analytics events and A/B test designs. But it can't replace the PRD review meeting. That meeting needs four to six people from different roles in a room arguing through tradeoffs: business cares about ROI and release timing, product cares about user experience, engineering cares about cost and tech debt, QA cares about testability. AI can help prepare the meeting. It can't do the organizational work of reaching agreement.

### 3.1.2 Design Stage (UI/UX and Technical Design)

Design has two tracks running in parallel: UI/UX and technical design. Each has its own review.

UI/UX has already been absorbed the most. Tools like v0 and Figma AI can turn a sentence into a runnable React component in minutes, with the styling system wired up. AI can also help with the formal checks in design review: does this match the brand guidelines, are we reusing existing components? But whether an interaction fits the brand voice, or what the user will do after this step, still needs a senior designer's judgment.

AI is useful in technical design too. Give it a requirement, and it can list three candidate architectures with throughput, latency, and cost compared clearly. But the final choice is still human, because it depends on constraints AI usually doesn't know: which stack the team is fluent in, what compliance rules apply, what SLA was promised externally, whether the key engineer is staying. Technical review is even more context-heavy. The arguments are usually: why not X, why not Y, why does it have to be Z this time? Every line carries team history. AI hasn't lived through that history.

### 3.1.3 Development Stage (Coding and Review)

Development is where AI is strongest, but some parts are still hard.

Start with what AI can handle directly. Claude Code can turn a PRD into an issue list and a dependency graph. Frontend and backend coding are the core use cases for Cursor + Claude or Codex; among senior engineers, 2x to 10x productivity gains are widely reported. For integration, AI can spin up a mock server, run contract tests, and flag schema mismatches. For code review, it can run static analysis, check coding rules, and flag likely bugs.

But AI still struggles with one layer of code review: architectural judgment. Will this change blur module boundaries? Will this abstraction still make sense three years from now? Does this decoupling fit the team's next plan? Those calls still need a senior reviewer.

The harder parts show up where the system touches the outside world. For a third-party API like WeChat Pay, Stripe, or Google Maps, AI can write the call code cleanly. But applying for the API key, negotiating commercial terms, passing KYC, and registering callback URLs still require a real person. For access control, such as OAuth, SSO, internal IAM, or cloud RBAC, AI can write the rules and the code. But who should have access, whether GDPR compliance is satisfied, and who takes blame when things go wrong are organizational decisions. The next section on non-programmer app building runs into the same wall.

Put it together, and 70% to 80% of the pure coding work in development is already AI territory. The remaining 20% to 30% splits between architectural judgment and hard debugging on one side, and external APIs, identity, and permissions on the other. Those are the parts that still need humans to deal with real-world processes.

### 3.1.4 Testing Stage (Automation and Human Acceptance)

Testing is AI's second strongest area.

Self-test and QA are almost fully in AI's reach. For self-test, AI can generate unit and integration tests with much higher coverage than humans usually write by hand. For QA, AI can run full regression suites, do fuzzing, and scan edge cases. Fuzzing means hammering the program with random inputs to find crashes. It used to be rare because the cost was too high for the payoff. AI drops the marginal cost close to zero.

The bug loop is also moving toward AI. For many teams, locating the relevant code from a stack trace, generating a patch, and submitting a PR is already automated for most P3 and P4 bugs.

UAT, or user acceptance testing, is different. This step needs real users clicking through real scenarios to confirm that the product matches expectations. AI can test code correctness. Only users can judge whether the product actually fits their needs.

### 3.1.5 Release Stage (Execution and Decision-Making)

Release splits into execution and decision-making.

AI can take over release execution. Canary release by percentage, region, or user cohort can run automatically. So can full rollout, monitoring, alerting, anomaly detection, and automatic rollback for predefined scenarios. That part is mature.

The decision is still human. Suppose the canary reaches 10%, and the core metric starts wobbling. Do we keep pushing, roll back, or hold and investigate? Every option has a cost: rollback hurts short-term progress, but pushing forward risks a full-release incident. You can't make that call by staring at a dashboard. Business rhythm, partner coordination, and market timing all matter, and AI usually can't see them.

Unprecedented incidents are harder. A third-party dependency goes down and triggers cascading failures. A regional data center loses power. A security incident demands an emergency takedown. None of these fits neatly into the runbook. The response still comes from the on-call engineer.

### 3.1.6 Verification and Wrap-up (Data Validation + Retrospective + Archiving)

For data validation, AI can pull metrics, build charts, and offer three to five plausible explanations. But if a feature misses conversion targets, the real question is harder: did users not want it, was the entry point too deep, or was the pricing wrong? That judgment needs a product manager combining qualitative and quantitative data. AI also can't replace the retrospective meeting. The point of a retrospective is organizational learning: what rule changes, who takes responsibility, and whether the process needs to change. That's human-to-human work. Archiving, on the other hand, is easy to automate: structure the docs, link the knowledge base, generate search indexes.

Now put the six stages together.

Weighted across substeps, AI can directly replace roughly 50% to 60% of total R&D work today. Development and testing are the heaviest stages, and AI can take 70% to 85% of each. In requirements, design, and verification & wrap-up, AI handles 30% to 50% of the substeps. In release, execution is nearly 100% automatable, but the go/no-go decision is still 0%.

Another way to put it: AI has cut the cost of doing the work way down. The cost of deciding whether the work is good enough still sits with humans.

Can AI keep eating into the remaining 40% to 50%? That's the central question for the next few years. The answer splits into two categories.

One category is technically hard, but there's a path forward: architecture choices grounded in team history, complex root-cause analysis, multi-file and cross-repo debugging, and responses to incidents no one has seen before. AI struggles with these today because context windows are still too short, organizational context isn't internalized, and long-term system evolution is hard to model. As models get longer context, better memory, and continual training on team codebases, there's a real shot at AI taking over most of this work within five years. That would push the whole pipeline to 70% to 80% AI.

The second category won't yield just because models get smarter: cross-person consensus, accountability, and real-world processes like KYC, commercial negotiation, compliance, and legal liability. The blocker is institutional, not technical. For AI to take over this layer, it has to exist as a legal entity: sign contracts, hold accounts, and bear consequences. Some startups are already working on legal structures that let AI agents hold accounts, take responsibility, and carry insurance. But that path depends on law, regulation, and social acceptance. The window is probably 5 to 10 years. If it opens, the remaining 20% to 30% gets eaten too, and software development moves into a new phase: humans set the problem, humans make the final call, and AI handles the rest.

In the short term, meaning the next two to three years, moving from today's 50% to 60% AI pipeline to 70% to 80% looks very likely. Better models and better tooling are enough for that. Going above 90% is different. Model capability alone won't do it. The institutional layer has to change.

This view also matches the academic map. IEEE SWEBOK V4, the Software Engineering Body of Knowledge released in October 2024, lists 18 knowledge areas. AI coding mainly covers software construction and parts of software testing. For the other areas, including requirements engineering, architecture, security, maintenance, configuration management, and engineering economics, AI can mostly assist. Think of an app as a tree. AI has chopped off the tallest, thickest branch. The roots, trunk, and other branches still need humans.

For engineers, this shift is already changing the division of labor. My own take: humans define problems, gate results, and handle the hard parts; AI writes code, runs tests, and fixes routine bugs. From 2022 to 2026, code review has moved up a level. In 2022, programmers read every line. In 2024, they read PR-level diffs. In 2026, more and more of the review happens at the issue level: did the bug get fixed, did the feature actually work? Engineers haven't disappeared, but code-writing is taking up a smaller slice of the job. Judgment, review, and acceptance are taking over.

## 3.2 Will There Be a "One-Click App" Tool for Non-Programmers?

To answer this, take the full enterprise R&D flow from the previous section and lay it next to a one-person project. Which stages still need AI, and which ones can just disappear?

**Requirements stage**, almost entirely gone. You're the requester, decision-maker, and user at the same time. What's in your head is enough to start. No PRD, no cross-department review, no business alignment meeting.

**Design stage**, heavily reduced. Let AI generate the UI. Accept the vendor's default style. No brand-voice debate. The technical design is also fixed by the tool: Lovable gives you Next.js + Supabase, Bolt.new gives you WebContainer + embedded Vite. You don't choose, and you don't need to. The technical review meeting disappears.

**Development stage** stays, but only the AI-writing-code part remains. No task breakdown meeting, no integration meeting, no code review. Frontend and backend live in the same generated stack. You check whether it runs, and that's it.

**Testing stage**, sharply reduced. Self-test means clicking around yourself. QA and the bug loop become "does this feel okay to me?" In a self-use scenario, there's no UAT. If a Lovable app crashes in the browser, you regenerate it.

**Release stage**, almost gone. One-person use has no canary. Full rollout means "open the URL myself." Monitoring and incident response don't apply at this scale. If something breaks, regenerate.

**Verification and wrap-up**, basically gone too. There's no data to validate, because you're the only user. No retrospective. Archiving can be handed to AI.

After those cuts, the real one-click flow has only three steps left: describe what you want, let AI generate and deploy it, then use it yourself. Can that stripped-down flow become 100% AI? It depends on the scenario.

### 3.2.1 Personal, Throwaway, Internal Tools

This category is already mostly handled by AI. But there are two versions of it.

The cleanest version is pure frontend. It runs in the browser and disappears when you close the tab. Anthropic's Artifact, OpenAI's Canvas, Vercel's v0, and Bolt.new all fit here. They generate tools with no backend, no database, no login, just HTML and JavaScript running in the browser, often with a stack as simple as React + Tailwind in one or two files. Typical use cases include throwaway calculators, UI prototypes, data visualizations, and document converters. Today, you can describe one of these tools with a prompt, wait a few minutes, and use it without creating an account. AI handles the whole thing.

The slightly more complex version has a simple backend, persistent data, and maybe a few users. Lovable's "frontend + Supabase" setup is the standard example. The stack is roughly Next.js + Tailwind + Supabase (database + auth) + Vercel for deployment, basically the same stack I use for indie projects. AI writes all the code, but the human still has to do a few dashboard steps: register a Supabase account, create a project, copy the URL and key; import the repo into Vercel, paste environment variables, hit Redeploy. AI can't reliably drive those browser consoles yet, so this part is still stuck. Personal expense trackers with cloud sync, small internal approval flows, and tiny collaboration tools for a few friends all sit in this tier.

Add the two together, and personal or internal small tools are about 95% AI today. The remaining 5% is a human pasting keys into dashboards.

### 3.2.2 Apps for Other People — App Store, or Anything That Takes Money

Here's what actually happens: AI can write more than 95% of the code, while the human mostly clicks through dashboards and compliance steps. Look closer, and that leftover work splits into technical work and institutional work.

On the technical layer, AI writes the code and the human pastes credentials. For a standard indie app stack, say Next.js + Supabase + Stripe + Resend + Vercel, AI can handle almost everything: TypeScript code, Prisma schema, db push, Stripe checkout and webhooks, email templates, dependency installation, and git push for deployment. The human still has to do dashboard work:

- In Supabase: create a project, configure OAuth providers (paste Google / GitHub Client ID + Secret, which means going to Google Cloud Console and GitHub OAuth Apps to register first), configure redirect URLs.
- In Vercel: import the GitHub repo, paste environment variables, change the Build Command, manually Redeploy after editing env.
- In Stripe: create the Product, get the Price ID, after launch create a Webhook endpoint, copy the Webhook Secret back to Vercel.
- In Resend: get an API key, verify your sending domain.

External API integrations work the same way. AI writes the call code. The human goes to each platform's console to issue keys, handle business terms, register webhook URLs, and set callback URLs. AI can't reliably drive a browser today, so this step can't be skipped.

The institutional layer is the part AI can't handle today:

- KYC identity verification (you bring an ID and bank account to register a corporate entity).
- Business qualifications (running payments in China requires ICP filing, business license, and sometimes a payment-license partnership).
- Legal liability (when user data leaks, fraud occurs, or IP is infringed, someone has to be on the hook).
- App Store distribution (Apple and Google won't issue developer accounts to AI agents; the annual real-name verification and fees go to a human).

Put the two layers together, and an app meant for other people is roughly 90% AI and 10% human dashboard work today. "Build a real app from a prompt" isn't quite true. But a prompt plus 10 console paste-keys can already get you a real app.

So does the "non-programmers can build apps" slogan hold up? Technically, yes. Institutionally, only partly. A complete non-coder following Lovable + Stripe + Vercel onboarding docs can ship a SaaS that takes money. The precondition is that they're willing to register a company, pass Stripe KYC, sign compliance documents, and serve as the legal representative. That part has nothing to do with AI capability. It's about whether they're willing to be the boss.

### 3.2.3 Two Paths Forward

Can AI keep eating the remaining human work? There are two paths.

The technical path eats the last 5% in 3.2.1 and the technical 10% in 3.2.2. AI keeps absorbing more of the stripped-down flow: auto-wire payments, auto-handle OAuth, auto-deploy with domains and HTTPS, auto-monitor and auto-rollback. The bigger move is browser agents. Products like Anthropic's Computer Use and OpenAI's Operator can log into Supabase, Vercel, and Stripe, click through consoles, paste keys, and redeploy. Within a year or two, the two personal-tooling cases in 3.2.1 should be 100% AI. Most of the dashboard work in 3.2.2 will fall to browser agents too. Moving formal apps from today's 90/10 to 95/5 on the technical layer looks very likely.

The institutional path moves much more slowly. It's about whether AI legal entities can exist, hold accounts, sign contracts, and bear liability. Those are questions for law and regulation, not model capability. Some startups are building legal scaffolding for AI-agent-held accounts, assigned liability, and insurance coverage. But getting there requires legislation, case law, and social acceptance to line up. The window is 5 to 10 years. Once it opens, real apps for strangers, including apps that take money and ship to stores, become reachable through one-click tools too. The map of software distribution changes completely.

The takeaway: personal tools are one-click today; apps for other people are at "prompt plus 10 paste-keys"; in 1 to 2 years, browser agents take over the paste-key layer; in 5 to 10 years, if AI legal entities become real, the last institutional blocker starts to fall.

## 3.3 Will This Wave of AI Coding Reshape the PC / Mobile App Ecosystem?

Yes, but probably not in the way most people expect. Start with the basic variables.

### 3.3.1 100x Supply, 1x Demand

Sections 3.1 and 3.2 already covered the cost of building an app. Today, with Lovable + Vercel + Stripe, something that once took five people six months can sometimes ship with one person over a weekend. Supply-side capacity is up at least 10x to 100x.

But demand has barely moved. Each person still has 24 hours a day. Average phone screen time is already around 5 hours, close to saturation. Most people actively use 10 to 20 apps on their phone. They may have 60 to 100 installed, but most get opened once and then forgotten. That structure has been stable for the past decade.

Supply goes up 100x, demand stays roughly 1x, and the middle layer gets crushed. Which part gets hit first depends on the app category.

Long-tail tool SaaS is the first to fold. Reimbursement systems, internal dashboards, personal expense trackers, vocabulary apps, step counters, ad-hoc form generators: small tools that lived on annual subscriptions can now be built by a user in half an hour with Lovable. A SaaS company charging $100 a year is now competing with an AI-generated version that's free and fits the user's exact need. That layer will have a hard time surviving.

Vertical industry SaaS is more complicated. Contract management for law firms, scheduling for hospitals, parent-school communication for elementary schools: these products contain industry-specific knowledge and can't be generated in one shot. But they will still face pressure. A customer's internal IT team can use the same AI tools to build an internal version and stop paying the subscription. This layer gets squeezed by price wars and may lose half its market.

Social, content, e-commerce, and maps barely move. Their value isn't in the code. The next section explains why.

### 3.3.2 Top Apps Won't Get Replaced; They'll Get Stronger

WeChat, TikTok, Taobao, Google Maps, Instagram, WhatsApp: AI coding can't touch the core of these top apps. There are four reasons.

Network effects. WeChat's value is 90% the other 1 billion users on it. You can't build a WeChat that only you use. Lovable can generate a WeChat-looking app overnight, but no one inside is someone you want to talk to.

Data accumulation. The 8 years of user behavior data TikTok has built up is the real moat behind its recommendation system. A new AI-generated short-video app starts with zero data. On day one, its recommendations are orders of magnitude worse.

Content and supply ecosystems. Taobao has millions of merchants, hundreds of millions of SKUs, stable logistics, and stable payments. AI can generate "my own shopping app," but there's nothing inside it.

Distribution gates. Apple, Google, Meta, and ByteDance own the first screen people see when they pick up their phones. AI coding doesn't change that.

The counterintuitive part is that AI coding will make these top apps stronger. They use AI internally to ship faster, handle customer service, improve recommendations, generate content, and fight fraud. Scale plus AI widens the product-quality gap. A new founder used to be able to dream of "building something better than WeChat" and ride that dream for a few years. In the AI coding era, even that dream gets harder to believe.

### 3.3.3 Long-Tail Apps Decay into On-Demand-Generated Capabilities

Put 3.3.1 and 3.3.2 together, and the mobile world in a few years could look like this.

Top apps stay around 20 to 30, similar to today, but each one becomes stronger and harder to displace. WeChat, TikTok, Taobao, banking apps, maps, email, camera: these stay installed, get used for years, and keep accumulating data.

The middle layer, meaning tools, single-function apps, and long-tail apps, shrinks from today's dozens to fewer than 10. Calendar, notes, password managers, and anything where personal data accumulates over time survive. Most other small tools get replaced.

What replaces them is on-the-fly generated Capabilities. You tell the AI assistant on your phone, "I want to track expenses for this trip," and it builds a form, a table, and a simple chart on the spot. The trip ends, and you delete it. Next trip, you generate a new one. Anthropic's Artifact, OpenAI's Canvas, and Apple Intelligence's App Intents are already moving in this direction. They just haven't reached every user yet.

These Capabilities have a different shape from today's apps: throwaway, personalized, zero-install, no monthly fee, and never listed in an App Store.

### 3.3.4 The Reshaped Ecosystem: A Three-Layer Structure

Put it all together, and the app ecosystem in a few years has three layers.

**Top-app layer**. WeChat, TikTok, Taobao, Apple, Google, Meta. They're anchored by network effects, data, and content ecosystems. AI coding makes them stronger. The number of players in this layer shrinks, and each remaining player gets more powerful.

**Assistant layer**. This is the new one. The user's entry point shifts from opening a specific app to telling an AI assistant what they want. The assistant either generates a one-off tool or calls a top app's API to get the job done. Today's prototypes are general assistants like ChatGPT, Claude, Apple Intelligence, and Google Gemini. Whoever owns this layer wins one of the biggest fights of the next few years, because it could chip away at the App Store's distribution position.

**Model layer**. Anthropic, OpenAI, Google, plus DeepSeek, Alibaba's Qwen, and ByteDance's Doubao. They make money selling tokens and capability. AI coding sends value to this layer first, because every generated Capability and every assistant call burns tokens.

The new ecosystem means different things for different players. Top app platforms keep growing. So does the model layer. The assistant layer is the contested ground, with room for one or two new giants, or for existing players to split it. The hardest spot is long-tail SaaS, unless those companies pivot fast enough to become Capability providers for the assistant layer, or go deep enough vertically to become a "small top" in their industry.

For a normal user, the phone still has 20 to 30 frequently used apps, much like today. But an AI assistant is always there, generating throwaway tools as needed. The dozens of useless apps that were installed once and never reopened are gone. The first action after picking up the phone shifts from finding the right app icon to telling the AI what you want. That's the biggest change in user entry point since the iPhone.

# IV. Closing Thoughts

Here's the whole argument in a tighter form.

**Principles**. AI can code because of two things. First, code training made general models smarter. It pushed the habit of "break the problem into steps, then make every step hold" into the model's default behavior. That helps far beyond code. It improves general reasoning too. Second, RLVR, reinforcement learning from real execution feedback, moved models from "can write code" to "can write correct code." Code has three rare properties: strong regularity, objective right and wrong, and built-in documentation. That makes it natural training material for models, and now one of the main ingredients behind smarter general models.

**Company history**. OpenAI put Codex into GitHub Copilot in July 2021. ChatGPT took off in November 2022 and broke the old external-brain ecosystem for programmers: Stack Overflow, Kite, Codecademy. In October 2024, the upgraded Claude 3.5 Sonnet made "AI can really write code" feel true for the first time, while Cursor's codebase indexing defined the new IDE pattern. Then came the 2024-2025 shift to agents, followed by a three-way ARR race in the billions among Codex CLI, Claude Code, and Cursor. In China, ByteDance Trae, Alibaba Tongyi Lingma, Baidu Wenxin Comate, and Zhipu CodeGeeX grew in parallel. The non-programmer track, including Lovable, Bolt.new, v0, and Replit Agent, crushed the cost of building a demo. These five years have been one of the fastest-moving product surfaces in AI.

**Systems engineering**. Software engineering is a full lifecycle: requirements, design, development, testing, release, verification, and wrap-up. ISO/IEC/IEEE 12207 defines it, Alibaba P3C and Meituan's engineering writing show how large companies practice it, and SWEBOK V4 maps it across 18 knowledge areas. Today, AI can directly replace roughly 50% to 60% of that work. Development and testing are hit hardest, at 70% to 85% each. Requirements, design, and verification sit closer to 30% to 50%. Of the remaining human work, the technical part still has room to shrink: architecture choices, root-cause analysis, and hard debugging. Over a few years, AI could push the whole pipeline to 70% to 80%. The institutional part, including consensus, accountability, and real-world processes, needs law and regulation, not just better models. Software engineering's complexity has been redistributed, not eliminated.

**One-click app**. Personal, throwaway, internal tools are almost one-click today: 95% AI, 5% console paste-keys. Apps meant for other people, especially apps that ship to an App Store or take money, are closer to 90% AI and 10% human dashboard work. A prompt plus 10 paste-keys can build a real app, but only if the human is willing to register a company, pass KYC, and serve as the legal representative. The next steps are clear: in 1 to 2 years, browser agents like Computer Use and Operator eat the paste-key layer; later, if AI legal entities become viable, the institutional blocker starts to fall.

**Ecosystem**. On the supply side, AI coding multiplies capacity 10x to 100x. Demand barely moves. The middle layer gets flattened: long-tail SaaS disappears, and vertical industry SaaS may lose half its market. Top apps like WeChat, TikTok, Taobao, Apple, Google, and Meta don't get replaced. Network effects, data, content ecosystems, distribution gates, and AI-driven internal speed make them stronger. Long-tail apps turn into on-demand Capabilities: throwaway, personalized, zero-install, and never listed in an App Store. The next ecosystem has three layers: top-app platforms, AI assistant + Capability, and model layer. The first action when picking up the phone shifts from finding an icon to telling the AI what you want. That's the biggest entry-point change since the iPhone.

**Where to position next**. There are still a few good paths. Be an engineer who works well with AI and takes on more judgment, review, and acceptance work. Be a product person who can use AI tools against real business problems, with a clear sense of what to hand off to AI and what to keep with humans. Be a founder who uses AI to do alone what used to take ten people, betting on a position in the new AI assistant + Capability layer. Or be a vertical specialist building a "small top" inside an industry's domain knowledge that AI coding can't easily copy. Each path is wider than it was five years ago. But the dream of starting from scratch and building the next WeChat is fading. AI coding makes the top deeper, replaces most of the long tail, and opens a new assistant layer waiting to be claimed.

AI has dramatically raised the floor for building software. The ceiling is still set by humans. The biggest winners are top apps, model companies, and the few players that claim ground in the assistant layer. Everyone else has to find a position where AI helps them more than it helps their competitors.

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

> The original draft of this article is in Chinese, archived in the source piece "两万字科普：AI 为什么会编程——原理、历史与未来.md" (root directory of this repo). It's preserved verbatim there and not duplicated here.
