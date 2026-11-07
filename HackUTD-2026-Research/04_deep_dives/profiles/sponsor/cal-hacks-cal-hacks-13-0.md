# Cal Hacks — Cal Hacks 13.0 (9 projects)

### Bandit - The only band you need
*Cal Hacks Cal Hacks 13.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Spacetime] Best Use of Spacetime

**What it is:** A system of NFC- and radio-enabled ESP32 wristbands for event attendees. Bands sense nearby bands to show crowd density, react to falls and SOS presses, guide people during smoke, feed an insurance-claims pipeline, and produce a post-event recap with people met, booths visited and merch.
**Problem / user:** Concert and festival attendees, organizers and medics: crowd-crush risk after falls, slow small-injury insurance paperwork, and attendees losing track of who they met.

**Features**
- Fall/SOS crowd alert — MPU-6050 fall detection or button press makes surrounding bands flash red and vibrate; a medic can open the medical card only during an open incident. *[claimed]*
- Crowd density display — Bands beacon over ESP-NOW ten times a second and show local density as LED ring colours, working without internet; station markers define zones counted in organizer portal. *[claimed]*
- Smoke/fire exit guidance — One organizer button puts bands in low-visibility mode with colour-coded exit direction. *[claimed]*
- NFC onboarding and medical card — Tap band, sign in, claim by button, match public profiles, upload medical and insurance PDFs which Claude turns into a card the user confirms. *[claimed]*
- Insurance claim pipeline — Claude reads clinic records, Elastic checks past similar claims, code applies coverage and fee schedule; hard cases go to organizer, whose approval can create a reusable rule. *[claimed]*
- Wallet payouts and merch — Capital One Nessie account per attendee funds merch purchases and receives claim payouts. *[claimed]*
- Post-event recap — Per-band page with zone history, ranked people met with socials, booths visited, tagged photos. *[claimed]*
- Organizer event graph — Live Sigma.js map linking anonymous attendees, people, booths and companies from 245 scraped records. *[claimed]*

**Flow:** Get band at door and tap it with phone → Sign in, press band to claim, add socials → Upload medical and insurance PDFs, confirm card, connect wallet → During event bands show crowd levels; a fall triggers nearby alerts and medic access → Resolved incident opens a claim that settles or goes to organizer → Organizer ends event and each band page becomes a recap with merch

**Prompt:** Use SpacetimeDB meaningfully in a project; Best Use of Spacetime prizes of roughly $512 to $2048, plus a separate Scrabblebot tournament.
**Fit (explicit):** Whole live event runs as one SpacetimeDB Maincloud module: reducers are the only write path, scheduled reducers compute zones and history, SpacetimeAuth handles sign-in and per-caller views control access.  *(targeted: Best Use of Spacetime, Bright Data, Capital One, MLH Vultr, Anthropic, Elastic, Microsoft, Hyphenate)*
**Sponsor tools:** SpacetimeDB (Single backend module holding bands, zones, incidents, claims, wallets, people graph, core); Elastic (ES|QL joins, claim validation against past claims, semantic ranking, Kibana dashboards, supporting); Bright Data Web MCP (Scraping event/sponsor data into 245 records, supporting); Capital One Nessie (Attendee wallet for merch and payouts, supporting); Anthropic Claude (PDF extraction, injury-fit review, notice of loss, recovery letter, supporting); Vultr (Hosting Rust services, supporting)
**AI:** Claude extracts structured facts from PDFs, reviews whether injury fits the incident and drafts letters; code validates outputs and sets all payout amounts. Elastic agent merges duplicate company names.
**Architecture:** ESP32-C3 bands talk ESP-NOW to station markers and a USB gateway into a Rust bridge, which writes to a SpacetimeDB module. TypeScript web apps subscribe; Rust workers on Vultr handle claims and ingest.
**Novelty:** Combines physical wearables, safety response, insurance adjudication and social recap in one product; unusually large, with Rust crates, firmware and hardware handoff docs.
**Scope:** large · working: Live site linked; claims full flow runs end to end but only nine bands tested. · polish: Excalidraw board of 19 frames, docs, scorecard, fixtures; README is rough and partly informal.
**Claims:** 245 records ingested from 6 sources in one transaction | Urgent-care bill cut from $1,308 to $895 by fee schedule | Learned rule settled a similar $180 claim automatically | Safety features work without internet
**Gaps:** no demo video; scorecard values not reported
Sources: https://devpost.com/software/bandit-the-only-band-you-need, evidence/sponsor-cal-hacks-cal-hacks-13-0-bandit-the-only-band-you-need.json

---

### Ender's Bench
*Cal Hacks Cal Hacks 13.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Spacetime] Best Use of Spacetime

**What it is:** A benchmark that tests whether AI models obey an explicit policy when it costs them. It has a live four-agent survival world (The Clearing) and a finance desk (Ledger Street) with 70 lending, collections and vendor cases, plus a viewer, replays and a LoRA-tuned model called Ender.
**Problem / user:** AI evaluators and researchers who want to see whether models keep stated policies under pressure, and the say-versus-do gap in their explanations.

**Features**
- The Clearing survival sim — Four language-model survivors share a forest after a crash; SpacetimeDB ticks the world at 20 Hz and queries models for decisions. *[shown_working]*
- Charter vs reward-only comparison — Same world run with an eight-rule policy charter or reward-only prompt; policy detectors log violations in the same transaction as each action. *[shown_working]*
- Ledger Street finance benchmark — Models use tools on live credit-sandbox data across 70 cases tagged by law or house policy; verifiers score decision and process. *[shown_working]*
- Viewer, replay and leaderboard — Build a lineup up to four models, watch live, replay saved runs, compare explanation against action. *[shown_working]*
- Human participation — Visitors can join as a survivor alongside models. *[claimed]*
- Ender fine-tuned model — LoRA adapter on Qwen 27B trained on recorded decisions and ethics cases, served on Runpod; v1.3 beat its 4-bit base. *[shown_working]*
- Apify Actor — Runs the finance benchmark against a chosen model with the user's key, writing dataset rows, scorecard and replay; a second Actor hosts the viewer. *[shown_working]*

**Flow:** Open the Apify-hosted site → Pick up to four models for a lineup → Choose The Clearing or Ledger Street → Watch agents live and inspect recorded events → Replay saved runs or open the leaderboard → Optionally run the standalone Actor with own model key

**Prompt:** Use SpacetimeDB meaningfully in a project; Best Use of Spacetime prizes of roughly $512 to $2048, plus a separate Scrabblebot tournament.
**Fit (explicit):** SpacetimeDB is the game server and agent runtime: 30+ tables, scheduled reducers, a scheduled procedure calling model APIs via HTTP, run history and a public leaderboard view, hosted on Maincloud.  *(targeted: Best Use of Spacetime, Figma, Apify)*
**Sponsor tools:** SpacetimeDB (World simulation, atomic action plus detector commits, model calls from the database, leaderboard, core); Apify (Hosts viewer site and benchmark Actor, supporting); Figma (Architecture mapping, interface design, slides, supporting)
**AI:** Several hosted models (Claude Haiku, GPT, DeepSeek, GLM, Qwen) act as agents via tool calls; team LoRA-tunes Qwen3.8-27B on recorded runs and evaluates adapters in the same live environments.
**Architecture:** TypeScript SpacetimeDB module on Maincloud simulates the world and calls model APIs; React Three Fiber viewer subscribes; Node harness and Apify Actors run Ledger Street against a credit sandbox; Runpod serves custom models.
**Novelty:** Pairs a live multi-agent world with a legally grounded finance benchmark and trains its own adapter; reports permutation tests and keeps explanations separate from verified outcomes.
**Scope:** large · working: Hosted Apify site, published Actor and model weights, 126 overnight runs and 231 live finance cases reported. · polish: Detailed README with statistics, exhibits, docs and video folders, Figma deck.
**Claims:** Charter cut temptations taken from 6.0% to 2.9% (p=0.00005) | Claude Haiku passed 50 of 70 finance cases with zero harmful decisions | 126 overnight runs across 9 worlds with 8 models | Ender v1.3 passed 42 of 70 versus base 40
**Gaps:** video is a YouTube Short, not viewed; some Devpost passages garbled
Sources: https://devpost.com/software/ender-s-bench, evidence/sponsor-cal-hacks-cal-hacks-13-0-ender-s-bench.json

---

### GeonosisAI
*Cal Hacks Cal Hacks 13.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Spacetime] Best Use of Spacetime

**What it is:** An agent-run factory for deploying a robot policy. A user files a ticket with a reliability target and budget; agents baseline the robot, diagnose failures, buy targeted demonstrations from paid phone contributors, fine-tune a pi0.5 policy, re-evaluate and ship or loop.
**Problem / user:** Teams deploying robots for a specific task, who face slow manual cycles of testing, data collection and retraining; plus phone contributors paid for physical steps.

**Features**
- Ticketed deployment loop — Ticket moves through baseline, diagnose, plan data, collect, review, train, eval and ship, looping if target missed. *[shown_working]*
- Failure diagnosis — Claude clusters failed trials by cause using notes, timings and camera frames. *[shown_working]*
- Data-buy planner with human approval — Chooses recovery takeovers or clean demos, must cite a failure cluster, spend needs approval. *[shown_working]*
- Paid phone contribution — Jobs go out via Discord and text; contributors view cameras, drive the arm in browser, hand back; accepted episodes paid via Stripe test mode. *[claimed]*
- Episode review — Deterministic checks (timestamps, jerk, dropped frames, length) plus Claude vision review. *[claimed]*
- pi0.5 LoRA fine-tune and eval — Modal H100 trains on LeRobot-format episodes; policy server hot-swaps checkpoints and robot runs async action chunks. *[claimed]*
- Droid wait-for resume — Coding agents park on a database predicate and a bridge wakes them; measured 597 ms. *[shown_working]*
- Real arm plus MuJoCo twin with safety layer — I2RT YAM on Jetson and a sim share an interface with joint limits, workspace box, watchdog and e-stop. *[shown_working]*

**Flow:** Register robot and file ticket (cube in bin, 80%, $50) → Watch baseline trials and failure clusters on live view → Approve planner's data purchase → Contributors collect episodes on phones → Review, pay, train and re-evaluate → Ship with report or buy more data

**Prompt:** Use SpacetimeDB meaningfully in a project; Best Use of Spacetime prizes of roughly $512 to $2048, plus a separate Scrabblebot tournament.
**Fit (explicit):** SpacetimeDB on Maincloud is the shared bus: 23 tables for services, agents, robots and phones, with reducers enforcing single arm lease, payout budget checks and an append-only event log; row changes wake parked agents.  *(targeted: Best Use of Spacetime, Anthropic, Factory)*
**Sponsor tools:** SpacetimeDB (Shared state bus, atomic guards, subscription-driven agent wake-ups, core); Factory Droid (Coding agents that wait on database conditions and resume, core); Anthropic Claude (Scene generation, diagnosis, planning, episode review, trial judging, core)
**AI:** Claude (via API, Claude Code or Factory Droid backends) clusters failures, plans data purchases and reviews video; pi0.5 policy fine-tuned with LoRA on collected episodes.
**Architecture:** FastAPI Python orchestrator state machine, SpacetimeDB tables as bus, Next.js/three.js front end on Vercel, robot on Jetson, Modal H100 for training and policy server, laptop backend behind tunnels.
**Novelty:** Treats robot improvement as a ticketed factory with paid human-in-the-loop data and agents that sleep on database predicates; keeps sim and real data separate and shows Wilson intervals.
**Scope:** large · working: Live site and sim run (7/10 baseline shown); page does not report finished real-arm before/after results. · polish: README with screenshot, architecture, pitch and submission docs, tests, Docker and CI.
**Claims:** Resume bridge woke a parked droid in 597 ms | ~157 ms remote inference round trip hidden by async chunking | Wilson lower bound 0.72 at 10/10 successes
**Gaps:** no video; end-to-end real-arm results not published
Sources: https://devpost.com/software/robofactory, evidence/sponsor-cal-hacks-cal-hacks-13-0-geonosisai.json

---

### Luyten
*Cal Hacks Cal Hacks 13.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Spacetime] Best Use of Spacetime

**What it is:** An agentic finance ERP for month-end close at SaaS startups. Four worker agents only draft Proposals; a cross-vendor Red Team critiques them, an Advisor rules, and the CFO must confirm material items before the database lets anything post to the ledger.
**Problem / user:** Startup finance teams and CFOs: month-end close takes about ten days, and CFOs will not let an unsupervised model post to the general ledger.

**Features**
- Worker agents that only propose — Bookkeeper, Revenue, Credit and Risk, and Consolidation agents create Proposals; permissions are enforced by SpacetimeDB reducers per agent identity. *[shown_working]*
- Red Team and Advisor review — Grok critiques first, Gemini adds missed points; Advisor approves, amends or rejects and records a rationale. *[shown_working]*
- CFO confirmation gate — Items at or above $10,000 and every amendment sit in a Needs your OK queue for one-click confirmation. *[shown_working]*
- Counterparty credit and risk tiers — CRS Credit API checks identity, fraud, bureaus and public records; database derives a risk tier that sets payment terms. *[shown_working]*
- Board Pack drill-down — P&L, balance sheet, ARR waterfall, NRR; each number traces to journal lines, Proposal and agent debate. *[shown_working]*
- Multi-company group close — Two companies in two currencies close in one run with consolidation entries recomputed by the database. *[shown_working]*
- Startup dashboard — Shows cash, burn, runway, ARR, churn, DSO plus cost-of-service and payroll views. *[claimed]*
- Agentverse access — Advisor runs as a Fetch.ai agent reachable through ASI:One. *[claimed]*

**Flow:** Bank feed ingests raw lines and invoices → CFO seat is claimed once → Click Close September to start the group close → Workers create Proposals, Red Team critiques, Advisor rules → CFO confirms material items in Needs your OK → Drill from Board Pack to journal lines and agent debate

**Prompt:** Use SpacetimeDB meaningfully in a project; Best Use of Spacetime prizes of roughly $512 to $2048, plus a separate Scrabblebot tournament.
**Fit (implied):** SpacetimeDB is the ledger, approval queue, audit trail and agent message bus; reducers and per-role identities make the propose-only rule a database guarantee, and the Svelte UI updates live via subscriptions.  *(targeted: Best Use of Spacetime)*
**Sponsor tools:** SpacetimeDB (Ledger, approval gate, audit trail, inter-agent bus, permissions, core); CRS Credit API (MCP) (Counterparty identity, fraud, credit and records checks, supporting); Bright Data (Public footprint collection for counterparties, supporting); Fetch.ai Agentverse (External access to the Advisor agent, supporting)
**AI:** Claude Agent SDK runs worker agents and Advisor; Grok and Gemini via Vercel AI SDK act as Red Team; agents share one Proposal format routed through the database.
**Architecture:** SvelteKit client subscribes to a SpacetimeDB module holding a pure integer-minor-unit double-entry engine; agent processes connect with role-specific identities and exchange Proposals through tables.
**Novelty:** Enforces human control in the database rather than prompts, uses different model vendors for critique, and ships a keyless demo mode with recorded provider stand-ins.
**Scope:** large · working: Demo site and one-minute local demo; reported close produced 52 Proposals, flagged a duplicate payment and blocked two vendors. · polish: Extensive README with guided tour, CI, 1,085 workspace tests, GIF walkthrough.
**Claims:** 52 Proposals produced in a two-company close | 156 ledger unit tests, 1,085 across workspace | CRS cascade reproduces all 20 sandbox decisions | Close normally takes about ten days
**Gaps:** no video, GIF only
Sources: https://devpost.com/software/cafoo, evidence/sponsor-cal-hacks-cal-hacks-13-0-luyten.json

---

### Orkio
*Cal Hacks Cal Hacks 13.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Spacetime] Best Use of Spacetime

**What it is:** A coordination layer for developers who each run their own AI coding agent on separate laptops. Agents publish intentions over MCP, unfinished work is snapshotted to Git wip branches, and a Factory Droid orchestrator combines changes, tests integration and routes conflicts to the affected agents.
**Problem / user:** Developers running parallel AI coding agents: branches merge but code can still break at runtime, leaving humans to relay context between agents.

**Features**
- Shared intentions via MCP — Agents publish planned changes to files, interfaces and dependencies; teammates' agents read them while coding. *[shown_working]*
- Working-tree snapshots — Hooks use Git plumbing to publish uncommitted changes to wip/<agent> branches without touching the active branch. *[shown_working]*
- Integration testing — Factory Droid merges agents' unfinished work outside developers' branches and runs checks before main. *[shown_working]*
- Agent-to-agent conflict repair — Orchestrator identifies affected agents and gives them context to fix it directly, no separate resolver agent. *[claimed]*
- Task orchestration — Droid reads code, ownership and latest unpublished work and issues owner-specific tasks with dependencies; asks humans when contracts are ambiguous. *[claimed]*
- Human control — Risky changes escalate and publishing to main stays with a developer. *[claimed]*
- Live dashboard — React/Vite view of agent activity, shared context, tasks, integration results and agent messages. *[shown_working]*

**Flow:** Each developer runs a coding agent with Orkio hooks → Hooks snapshot unfinished work to wip branches → Agents publish intentions through MCP → Orchestrator assigns tasks and integrates code → Failures route to affected agents who coordinate a fix → Developer approves final publish to main

**Prompt:** Use SpacetimeDB meaningfully in a project; Best Use of Spacetime prizes of roughly $512 to $2048, plus a separate Scrabblebot tournament.
**Fit (explicit):** SpacetimeDB holds agent presence, snapshots, intentions, tasks, conflicts and notifications; subscriptions sync agents and dashboard, and reducers make multi-step changes atomic, such as recording a conflict and assigning its fix.  *(targeted: Best Use of Spacetime, Factory)*
**Sponsor tools:** SpacetimeDB (Real-time coordination state, subscriptions, transactional reducers, core); Factory Droid SDK (Central orchestrator assigning tasks and running integration, core)
**AI:** Developers' Claude Code agents do the coding; a Factory Droid orchestrator reads shared state and unpublished work to plan tasks, detect conflicts and delegate repairs.
**Architecture:** Claude Code hooks and an MCP server on each laptop write snapshots and intentions to SpacetimeDB; Factory Droid subscribes, merges wip branches in isolation, and updates a React dashboard.
**Novelty:** Treats coordination of several people's coding agents as the product, working on uncommitted code and dropping a dedicated resolver agent in favor of agent-to-agent repair.
**Scope:** medium · working: Flappy Bird two-computer test reported; demo video on YouTube; team notes some users could not run it. · polish: Structured README with demo video, tests, 13 screenshots on Devpost.
**Claims:** Flappy Bird build: 2 prompts vs 9 with GitHub only | 10 min vs 16 min completion | About 11.6% fewer tokens (380K vs 430K) | One comparison, not statistically validated
**Gaps:** video not watched
Sources: https://devpost.com/software/gehub, evidence/sponsor-cal-hacks-cal-hacks-13-0-orkio.json

---

### Pacioli
*Cal Hacks Cal Hacks 13.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Spacetime] Best Use of Spacetime

**What it is:** A shared live canvas for small-business bookkeeping. A Bookkeeper agent ingests bank, Stripe and QuickBooks items, categorizes, matches bills, voids duplicates and posts with reasons; only uncertain items reach the user, whose answers become reusable patterns.
**Problem / user:** Small companies without a finance team that keep postponing accounting.

**Features**
- Multi-source ingest — Pulls Nessie bank data, Stripe and QuickBooks bills and invoices onto one collaborative canvas. *[claimed]*
- Bookkeeper agent — Sorts transactions, matches them to bills, voids duplicates and posts to the ledger with a stated reason. *[claimed]*
- Needs you queue — Uncertain items show evidence and a suggested answer for approval. *[claimed]*
- Vendor email follow-up — Agent emails vendors on flagged items via AgentMail and follows up. *[claimed]*
- Learning from answers — User decisions are turned into patterns applied to later transactions. *[claimed]*
- Reports agent — Generates weekly P&L and requested charts from plain-English requests. *[claimed]*
- Real-time sync — SpacetimeDB propagates changes to all viewers immediately. *[claimed]*

**Flow:** Bank, Stripe and QuickBooks data lands on the canvas → Bookkeeper categorizes, matches and posts with reasons → Uncertain items appear in Needs you with a suggestion → User approves or has agent email the vendor → Answers become patterns → Reports agent produces weekly P&L

**Prompt:** Use SpacetimeDB meaningfully in a project; Best Use of Spacetime prizes of roughly $512 to $2048, plus a separate Scrabblebot tournament.
**Fit (implied):** SpacetimeDB module (TypeScript, on maincloud) is the real-time backend syncing events between agents and the React Flow canvas.  *(targeted: Best Use of Spacetime, Factory, Capital One)*
**Sponsor tools:** SpacetimeDB (Real-time sync backend, core); Factory Droid API (Bookkeeper and Reports agents in cloud sandbox with custom runtime, core); Capital One Nessie (Mock messy bank input, supporting); AgentMail (Vendor correspondence, supporting)
**AI:** Two agents (Bookkeeper, Reports) run on Factory's Droid API in a cloud environment; underlying model not named. Agents learn patterns from human answers.
**Architecture:** Vite/React and React Flow canvas connects to a SpacetimeDB TypeScript module; Factory agents read and write ledger state and send email.
**Novelty:** Presents accounting as a collaborative node canvas with an agent that asks only when unsure; the team built its own cloud runtime for Factory agents.
**Scope:** small · working: Vercel demo link and claim that everything works end to end; no metrics. · polish: Six captioned screenshots, Figma design and slides; repo README is only setup commands, no tests.
**Claims:** Everything works end to end | Easy to swap in live data
**Gaps:** no video; no measured results; Stripe/QuickBooks integration unclear
Sources: https://devpost.com/software/pacioli, evidence/sponsor-cal-hacks-cal-hacks-13-0-pacioli.json

---

### Rally
*Cal Hacks Cal Hacks 13.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Spacetime] Best Use of Spacetime

**What it is:** A browser sports game where the laptop shows a 3D court and a phone's motion sensors work as the racket, with no app install. Badminton plays 1v1 between two laptops or against a CPU; bowling and ping pong appear as solo modes. SpacetimeDB acts as the server-side referee.
**Problem / user:** Casual gamers and distant friends who want Wii Sports-style motion play without a $300 console or $500 headset.

**Features**
- Phone as racket — Scan a QR code to pair; phone DeviceMotion/orientation readings give swing speed and timing; calibration screens included. *[shown_working]*
- 3D court on laptop — Three.js renders arenas and ball physics in the browser. *[shown_working]*
- 1v1 online badminton — Two laptops share state through SpacetimeDB, with a live WebRTC video call between players. *[shown_working]*
- CPU opponent — Server decides the computer player's moves. *[shown_working]*
- Server-side referee — SpacetimeDB reducers decide every shot, landing and point. *[shown_working]*
- Fog of war — Opponent shot data is withheld by the database until it crosses the net; stamina is hidden too. *[claimed]*
- Swing anti-cheat — Server checks swing timing against its own clock and rejects faked perfect hits. *[claimed]*
- Bowling and ping pong solo modes — Reuse the same phone pairing. *[shown_working]*

**Flow:** Open the game on a laptop → Scan the QR code with a phone → Calibrate the phone → Pick sport and mode → Swing phone to hit; server rules each shot → Opponent shot appears only after crossing the net

**Prompt:** Use SpacetimeDB meaningfully in a project; Best Use of Spacetime prizes of roughly $512 to $2048, plus a separate Scrabblebot tournament.
**Fit (explicit):** SpacetimeDB is database, game server and referee: private tables, views and scheduled reducers replace a game loop, and the database itself enforces fog of war and timing fairness.  *(targeted: Best Use of Spacetime)*
**Sponsor tools:** SpacetimeDB (Authoritative game server, sync, referee, CPU moves, signalling for video, core)
**AI:** Only a server-side CPU opponent; no model or technique is described.
**Architecture:** Phone sends motion input to SpacetimeDB; reducers adjudicate play and views push permitted state to each laptop's Three.js client; WebRTC carries video peer to peer.
**Novelty:** Uses commodity phone sensors for motion sports and pushes information hiding (fog of war) into database views rather than the client.
**Scope:** small · working: README demo video on YouTube and three playable sports shown in screenshots; no live link. · polish: Calibration screens, sound and bloom effects; README short with tech stack; small codebase.
**Claims:** 2nd place of about 200 submissions in the SpacetimeDB track (README) | Low-latency play anywhere
**Gaps:** video not viewed; Devpost has no walkthrough
Sources: https://devpost.com/software/locomotion-5i4gzy, evidence/sponsor-cal-hacks-cal-hacks-13-0-rally.json

---

### skyFall
*Cal Hacks Cal Hacks 13.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Spacetime] Best Use of Spacetime

**What it is:** A live 3D globe forecasting when decaying satellites and rocket bodies will re-enter and which components survive. GPU Monte Carlo physics runs about 20,000 simulated futures per object and a debris model breaks each into parts; SpacetimeDB is the only backend.
**Problem / user:** The public, who get only a re-entry date window and no info on surviving debris, while breakup analyses stay inside agencies.

**Features**
- Live decay tracking — Scheduled SpacetimeDB procedures poll CelesTrak, SATCAT and NOAA space weather; SGP4 runs inside the module. *[shown_working]*
- Probabilistic re-entry forecast — ~20,000 particles per object under J2, drag and NRLMSIS density with per-object drag calibration; window from the spread. *[shown_working]*
- Component breakup and survival — Nine archetypes and seven materials; each part flies a 3-DOF descent with heating and melting; survivors give mass, energy, 50%/90% footprints. *[shown_working]*
- Interactive globe — CesiumJS globe colors objects by earliest plausible re-entry, rings dangerous-fragment objects, hover isolates one part. *[shown_working]*
- DB-driven GPU job queue with failover — Leases, retries and a 2-second sweep reducer; CPU workers get jobs only if no healthy GPU worker exists. *[shown_working]*
- Self-scoring forecasts — Last forecast before official decay is scored for hour error and window hit; forecasts versioned and archived. *[claimed]*
- Ground-sighting fusion — Bayesian narrowing of corridors with sightings. *[planned]*

**Flow:** Open the 3D globe → Filter objects with the legend → Click an object for altitude, window and corridor → View 50%/90% impact zones → Open component breakdown and hover parts → Watch forecasts refresh as data arrives

**Prompt:** Use SpacetimeDB meaningfully in a project; Best Use of Spacetime prizes of roughly $512 to $2048, plus a separate Scrabblebot tournament.
**Fit (explicit):** One TypeScript module (32 tables, 29 reducers, 6 schedules) ingests data, queues and leases GPU jobs, fails over, archives, scores and streams to clients, with no other server, database or queue.  *(targeted: Best Use of Spacetime)*
**Sponsor tools:** SpacetimeDB (Entire backend: ingest, job queue, failover, archive, live streaming, core)
**AI:** Mostly physics simulation, not ML: batched PyTorch Monte Carlo on a GPU. AI coding agents (Cursor, Grok) were used to build it, not in the product.
**Architecture:** SpacetimeDB module polls feeds and queues jobs; GPU and CPU workers lease jobs and write forecasts back; React/CesiumJS client subscribes to tables.
**Novelty:** Brings agency-style reentry breakup analysis to a public live tool, and uses the database as a leased job scheduler with failover rather than a separate queue.
**Scope:** medium · working: Live site isitfalling.us listed; reported GPU-to-CPU failover test and large simulation runs. · polish: Detailed README and Devpost with honest limitations; tests present; no video.
**Claims:** 32.7 million simulated futures, 752 billion integration steps | About 22x faster than CPU fallback | GPU-to-CPU failover in 7 seconds | Early forecasts ran 7 to 11 hours late before drag calibration
**Gaps:** no video; no hindcast accuracy scorecard
Sources: https://devpost.com/software/skyfall-uca4i9, evidence/sponsor-cal-hacks-cal-hacks-13-0-skyfall.json

---

### Vouch
*Cal Hacks Cal Hacks 13.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Spacetime] Best Use of Spacetime

**What it is:** A video-based refund claim system. Shoppers record a damaged item on a phone, Factory Droid and CREAO agents analyze the footage into timestamped findings and a merchant recommendation, and a separate Vouch Score tracks shopper reliability, all tested in a simulated 10,000-shopper economy on SpacetimeDB.
**Problem / user:** Consumers with slow refunds, merchants who cannot separate honest claims from fraud, and finance teams reconciling refunds.

**Features**
- Phone video claim — Shopper explains the problem on camera and completes a finger challenge; claim page tracks 10 stages and may request one more clip. *[shown_working]*
- Automated video investigation — FFmpeg prep, faster-whisper transcript, and a Factory Droid loop with MCP tools produce claim-by-claim findings with proof clips; it has no payment authority. *[shown_working]*
- Merchant case packet — Order, statement, findings, policy, history, Vouch Score and a recommendation; approvals flow on, rejections go to a human. *[shown_working]*
- Vouch Score — Hand-set transparent formula over purchase and return history, bounded once-only updates enforced in SpacetimeDB reducers. *[shown_working]*
- Portable credentials — Ed25519-signed, selectively disclosed attributes another merchant can verify. *[claimed]*
- Simulated shopping economy — 10,000 shoppers and 100 merchants on a globe with event streams, driven by scheduled reducers. *[shown_working]*
- Refund Finance Desk — Reconciles decision, processor, bank, warehouse and ledger records with period locks and controller approval over $500. *[claimed]*
- Detector Lab — Droid proposes fraud detector changes in an isolated folder for human promotion. *[claimed]*

**Flow:** Shopper records item and explains the problem on phone → Claim moves through 10 processing stages → Droid and CREAO agents produce findings and recommendation → Merchant reviews packet; approvals proceed, rejections to human → Vouch Score updates with a reason → Finance desk reconciles the refund

**Prompt:** Use SpacetimeDB meaningfully in a project; Best Use of Spacetime prizes of roughly $512 to $2048, plus a separate Scrabblebot tournament.
**Fit (explicit):** SpacetimeDB stores all claims, artifacts, findings, scores and finance events, runs the simulated economy with scheduled reducers, enforces authorization and duplicate-update checks in reducers, and syncs browsers by subscription.  *(targeted: Best Use of Spacetime, Factory, CREAO)*
**Sponsor tools:** SpacetimeDB (Shared state, simulation, authorization and score-update rules, live sync, core); Factory Droid SDK (Claim investigation loop, report auditor, detector lab, core); CREAO agents (Refund reviewer, risk scorecard, pattern analysis, finance roles, core); CRS identity APIs (Contact-risk screening (in progress), supporting)
**AI:** Factory Droid runs a tool-using investigation of video evidence; CREAO API-triggered agents give review and risk readings; outputs are validated and the score formula is deterministic.
**Architecture:** Next.js front end and Node worker; worker runs FFmpeg/whisper, calls Droid and CREAO, and writes findings to a SpacetimeDB module that also runs the simulation.
**Novelty:** Combines video evidence review, a portable shopper trust credential, and a finance reconciliation desk, tested at 10,000-agent scale with explicit limits on what synthetic results prove.
**Scope:** large · working: Trycloudflare demo link; recorded test finished review in 155 seconds with live Droid sessions and a fixture CREAO reviewer. · polish: Multi-page app, tests, detailed README table of pages; temporary demo URL.
**Claims:** Review completed in 155 seconds in recorded test | 10,000 shoppers, 100 merchants simulated | One-million-order synthetic finance book | Synthetic results do not prove real fraud accuracy
**Gaps:** no video; CRS screening unfinished
Sources: https://devpost.com/software/vouch-7i3bft, evidence/sponsor-cal-hacks-cal-hacks-13-0-vouch.json

---

