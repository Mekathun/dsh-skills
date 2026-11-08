# DSH Skills 仓库

这台机器上 DeepSeek Harness 的 skill 全集，共 **153 个**、1862 个文件、约 58.5 MB。仓库根目录就是 `~/.dsh/skills` 的目录结构，clone 下来直接可用。

## 怎么用

```bash
# 第一次在新电脑上同步（会先备份已有的 skills 目录）
bash bootstrap.sh https://github.com/Mekathun/dsh-skills.git

# 以后更新：拉最新，推本机改动
cd ~/.dsh/skills && git pull && git push
```

仓库是私有的，新电脑要先登录过 GitHub（`git` 会走系统凭据管理器），或者用 `git clone git@github.com:Mekathun/dsh-skills.git`（需要该机器已加 SSH key）。

手动安装：
```bash
mv ~/.dsh/skills ~/.dsh/skills.bak.$(date +%s)
git clone https://github.com/Mekathun/dsh-skills.git ~/.dsh/skills
```

> 不在本仓库里的 skill（`office`、`music-studio`、`fishtalk`、`nekowhale-stickers`、`browser-skill`、`diagnose-windows-sandbox-acl` 等）是 DSH 或插件自带的，装好对应的 DSH / 插件就有，不用同步。

## 清单

### 学术与研究（18）

| skill | 简介 | 文件 |
| --- | --- | ---: |
| `academic-paper` | 12-agent academic paper writing pipeline. 11 modes… | 63 |
| `academic-paper-reviewer` | Multi-perspective academic paper review with dynamic reviewer personas. Runs a 5-seat, role-separated review panel (Journal-Fit… | 28 |
| `academic-pipeline` | Orchestrator for the full academic research pipeline: research -> write -> integrity check -> review -> revise -> re-review ->… | 30 |
| `deep-research` | Universal deep research agent team. 13-agent pipeline for rigorous academic research on any topic. 8 modes: full research, quick… | 53 |
| `research` | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo | 2 |
| `sr-screener` | Protocol-driven study screening for systematic, scoping and rapid reviews. Turns a proposal or PROSPERO protocol into confirmed… | 25 |
| `to-questionnaire` | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. | 2 |
| `to-spec` | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what… | 2 |
| `to-tickets` | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published… | 2 |
| `understand` | Analyze a codebase to produce an interactive knowledge graph for understanding architecture, components, and relationships | 55 |
| `understand-chat` | Use when you need to ask questions about a codebase or understand code using a knowledge graph | 1 |
| `understand-dashboard` | Launch the interactive web dashboard to visualize a codebase's knowledge graph | 1 |
| `understand-diff` | Use when you need to analyze git diffs or pull requests to understand what changed, affected components, and risks | 1 |
| `understand-domain` | Extract business domain knowledge from a codebase and generate an interactive domain flow graph. Works standalone (lightweight… | 2 |
| `understand-explain` | Use when you need a deep-dive explanation of a specific file, function, or module in the codebase | 1 |
| `understand-figma` | Analyze a Figma file via the Figma REST API and generate an interactive design knowledge graph (pages, screens, components,… | 3 |
| `understand-knowledge` | Analyze a Karpathy-pattern LLM wiki knowledge base and generate an interactive knowledge graph with entity extraction, implicit… | 3 |
| `understand-onboard` | Use when you need to generate an onboarding guide for new team members joining a project | 1 |

### 工程与代码（93）

| skill | 简介 | 文件 |
| --- | --- | ---: |
| `ask-sonner` | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading… | 2 |
| `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or… | 8 |
| `cavecrew` | When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder` (1-2 file edit) or `cavecrew-reviewer` (diff… | 2 |
| `caveman` | Terse caveman voice: answer first, fluff gone, every technical fact kept | 2 |
| `caveman-commit` | Write a Conventional Commits message compressed to intent only | 2 |
| `caveman-compress` | Compress a memory file such as CLAUDE.md or a todo list into caveman format to save input tokens, keeping a readable backup.… | 10 |
| `caveman-discover` | Find and label every LLM workflow in the repository so Caveman Cloud groups spend by workflow instead of one bucket | 1 |
| `caveman-evidence-review` | Read-only review of Caveman Cloud evidence: cost, Cave Score, workflows, traces, latency, errors, routing, savings | 1 |
| `caveman-explore` | Read-only repository explorer for cold-start orientation, broad cross-file localization, or when a direct search failed. Skip it… | 3 |
| `caveman-help` | Quick-reference card for the three caveman skills and their commands. Trigger: /caveman-help or "caveman help". | 2 |
| `caveman-learn` | Act on a Caveman learn report - review the ranked token sinks, apply cost-lowering fixes with per-edit consent, and report what… | 6 |
| `caveman-manage` | Inspect Caveman Cloud's experiment lifecycle and block unsafe execution | 1 |
| `caveman-optimize` | Turn a Caveman optimization observation into an operator-chosen candidate with a paired baseline evaluation | 1 |
| `caveman-review` | Compressed code review - one line per finding with location, problem and fix | 2 |
| `caveman-setup` | Wire a repository through the Caveman Cloud gateway so every LLM request is measured, with no behavior change | 1 |
| `caveman-stats` | Show recorded output and cache-read token usage and mode attribution for the current Claude Code session, or locate the host's… | 2 |
| `code-review` | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this… | 2 |
| `codebase-design` | Shared vocabulary for designing deep modules | 4 |
| `diagnosing-bugs` | Diagnosis loop for hard bugs and performance regressions | 3 |
| `diagnosing-superpowers` | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor… | 20 |
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | 1 |
| `domain-modeling` | Build and sharpen a project's domain model | 4 |
| `ds-adopt` | Takes over an existing PR, branch or agent thread and finishes its original goal while keeping credit for the first contributors | 1 |
| `ds-best-of-n` | Run N independent attempts at the same task in parallel, pick the strongest as the base, and graft the best parts of the others… | 1 |
| `ds-blast-radius` | Find what a change could break outside its own diff, then prove the key safety fact by running real code | 1 |
| `ds-blueprint` | Design the types, function signatures and module layout first, agree on that shape, then implement against it | 1 |
| `ds-catchup` | Give the user a short plain-language catch-up on what changed since their last message, followed by every decision still waiting… | 1 |
| `ds-context-reset` | Keep a PROGRESS.md for long tasks and move to a fresh session or subagent that reads only that file when the context gets long or… | 1 |
| `ds-design` | Builds a frontend with a clear visual direction instead of the generic AI look | 1 |
| `ds-design-audit` | Reviews an existing UI with scores based on evidence, then fixes the highest-impact problems | 1 |
| `ds-explain` | Explain how a piece of code works, why it is built that way, and what that means, in plain language a person can follow | 1 |
| `ds-help` | Pick the right deepseek-stack skill for a task and explain how the pack fits together | 1 |
| `ds-jury` | Gets independent reviews of a change from two or three different models or providers and loops on fixes until they agree | 1 |
| `ds-ledger` | Keep a one-row-per-decision log during long or unattended runs, and re-read it before each step so the run does not drift from… | 1 |
| `ds-lessons` | Find mistakes agents keep repeating in this repo and turn each into structure that blocks it, preferring types over lint over… | 1 |
| `ds-mode` | Always-on working style for DeepSeek agents: restate the task, read before editing, small verified steps, evidence before done,… | 1 |
| `ds-plan-loop` | Write a numbered plan with an acceptance check for each step, critique it once in a fresh pass, revise it, then execute one step… | 1 |
| `ds-pr` | Files a short, clear pull request for the current branch | 1 |
| `ds-pr-comments` | Formats and posts GitHub comments written by an agent on the user's behalf, with clear attribution and no leaked secrets. Use… | 1 |
| `ds-principles` | Compact engineering principles for design, debugging, verification, and delegation, each with a trigger | 1 |
| `ds-ready` | Runs the full ds-ship workflow but stops with the pull request ready for a human to merge, and never merges | 1 |
| `ds-review-loop` | Runs an author and a fresh-context reviewer in a loop on the current change until both agree it is correct, for at most four… | 1 |
| `ds-revive` | Brings an old PR up to date by checking if its idea still fits the current code, then rebasing, reworking or recommending it be… | 1 |
| `ds-sharpen` | Restate the user's goal, make the task deeper rather than bigger, rewrite the prompt, and optionally attack the plan to find weak… | 1 |
| `ds-ship` | Takes a change all the way from code to a merged pull request without supervision: build it, prove it, review it, file the PR,… | 1 |
| `ds-swarm` | Fan out N parallel workers on slices of a job or on a race, collect every result, and return one evidence-backed report | 1 |
| `ds-tdd` | Fix a bug by first writing a focused test that fails for the right reason, then making the smallest change that makes it pass | 1 |
| `ds-unslop` | Remove AI writing tells from prose and code comments, then rewrite in plain, specific English | 1 |
| `ds-unstick` | Break out of a repeating failure: name the assumption behind all the failed fixes, test it directly, list three other approaches,… | 1 |
| `ds-verify-loop` | Run edit, real check, read the actual error, fix the root cause, rerun, until the check passes or the cap is hit | 1 |
| `ds-watch-pr` | Watches a pull request through CI and review, fixes real findings and stops when it is ready, merged or blocked | 2 |
| `executing-plans` | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline… | 3 |
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | 1 |
| `git-guardrails-claude-code` | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute | 3 |
| `implement` | Implement a piece of work based on a spec or set of tickets. | 2 |
| `implement-spec` | Implement the result of /to-spec and /to-tickets in code. | 2 |
| `improve-codebase-architecture` | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | 3 |
| `investigate-first` | Diagnose ambiguous failures before editing | 2 |
| `karpathy-guidelines` | Behavioral guidelines to reduce common LLM coding mistakes | 1 |
| `lean-build` | Build feature work with high overbuilding risk | 2 |
| `megacave` | Caveman in Classical Chinese: 文言文 register, far fewer characters, technical terms verbatim. Invoke only with /megacave or… | 2 |
| `migrate-to-shoehorn` | Migrate test files from `as` type assertions to @total-typescript/shoehorn | 2 |
| `migration` | Implement reversible compatibility-safe transitions | 2 |
| `mp-prototype` | Build a throwaway prototype to answer a design question | 4 |
| `ponytail` | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. Use on… | 1 |
| `ponytail-audit` | Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what… | 1 |
| `ponytail-debt` | List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. One-shot report, changes nothing | 1 |
| `ponytail-gain` | Show ponytail's measured savings (code, cost, speed) from the benchmark. One-shot display | 1 |
| `ponytail-help` | Quick reference for ponytail levels, skills and commands. One-shot display | 1 |
| `ponytail-review` | Quality review of a change: is the logic right, is it safe, does it hold under real load, is risky code tested, is it fast… | 1 |
| `prototype` | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through… | 2 |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically… | 1 |
| `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | 2 |
| `safe-refactor` | Restructure code while preserving behavior | 2 |
| `scaffold-exercises` | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting | 2 |
| `setup-pre-commit` | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo | 2 |
| `setup-ts-deep-modules` | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and… | 3 |
| `software-factory` | Shared language for designing a software factory: the tasks it runs and the services it plugs into. | 6 |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session | 14 |
| `surgical-patch` | Fix bugs and small behavior changes at the narrowest responsible layer | 2 |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | 11 |
| `tdd` | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or… | 4 |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code | 2 |
| `triage` | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready… | 4 |
| `ultracave` | Caveman at maximum compression: fragments, one word when one word is enough, each fact once. Invoke only with /ultracave or… | 2 |
| `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an… | 1 |
| `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response… | 8 |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification… | 1 |
| `verify-and-stop` | Prove existing work meets acceptance conditions without expanding scope | 2 |
| `wait-what` | Stop. That last message did not land: re-pitch it. | 2 |
| `wayfinder` | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and… | 2 |
| `write-swift` | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent,… | 1 |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code | 1 |

### 设计与前端（23）

| skill | 简介 | 文件 |
| --- | --- | ---: |
| `animate` | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at… | 2 |
| `animate-expo` | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it… | 2 |
| `animation-performance` | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is… | 1 |
| `animation-vocabulary` | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing… | 1 |
| `apple-design` | Apple's approach to interface design and fluid, physical motion, translated for the web | 1 |
| `break-ui` | Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge… | 2 |
| `emil-design-eng` | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that… | 1 |
| `find-animation-opportunities` | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes… | 1 |
| `gsap-core` | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia()… | 1 |
| `gsap-frameworks` | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount | 1 |
| `gsap-performance` | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching | 1 |
| `gsap-plugins` | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer,… | 1 |
| `gsap-react` | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup | 1 |
| `gsap-scrolltrigger` | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers | 1 |
| `gsap-timeline` | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback | 1 |
| `gsap-utils` | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe | 1 |
| `impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, simplify, harden, animate, or otherwise improve a… | 58 |
| `improve-animations` | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained… | 3 |
| `mobile-native` | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something… | 1 |
| `pick-ui-library` | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus,… | 1 |
| `remove-animations` | Find the animations an interface doesn't need and remove them — motion on keyboard actions, high-frequency surfaces, functional… | 1 |
| `review-animations` | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to… | 2 |
| `video-shotcraft` | Create cinematic product videos from frontend projects or webpages with Remotion, real page captures, shot cards, the Ink Press… | 1218 |

### 像素与建模（1）

| skill | 简介 | 文件 |
| --- | --- | ---: |
| `blockbench-mcp-modeling` | Build high-quality Minecraft / GeckoLib / Bedrock models, textures and animations in Blockbench through the BlockbenchMCP server… | 5 |

### 写作与表达（18）

| skill | 简介 | 文件 |
| --- | --- | ---: |
| `ask-matt` | Ask which skill or flow fits your situation. A router over the skills in this repo. | 3 |
| `chief-of-staff` | Pursue a long-running goal in a single session by co-ordinating subagents. | 2 |
| `claude-handoff` | Hand the current conversation off to a fresh background agent that picks up the work immediately. | 2 |
| `grill-me` | A relentless interview to sharpen a plan or design. | 2 |
| `grill-with-docs` | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. | 2 |
| `grilling` | Grill the user relentlessly about a plan, decision, or idea | 2 |
| `handoff` | Compact the current conversation into a handoff document for another agent to pick up. | 2 |
| `loop-me` | Grill me about specs for the workflows I want to build, within this workspace. | 2 |
| `pr` | Use when writing a PR body. | 3 |
| `retro` | Conduct a retrospective on a coding session. | 2 |
| `setup-matt-pocock-skills` | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run… | 7 |
| `teach` | Teach the user a new skill or concept, within this workspace. | 6 |
| `wizard` | Generate an interactive bash wizard that walks a human through steps only they can perform | 3 |
| `writing-beats` | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. | 2 |
| `writing-for-agents` | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. | 3 |
| `writing-fragments` | Writing, explore: mine raw fragments, no structure yet. | 2 |
| `writing-shape` | Writing, exploit: shape raw material into an article, paragraph by paragraph. | 2 |
| `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment | 10 |
