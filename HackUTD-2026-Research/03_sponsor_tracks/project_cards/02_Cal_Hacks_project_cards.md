# Cal Hacks: project cards (9 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## Cal Hacks 13.0

### Bandit - The only band you need  (Cal Hacks 13.0)

- **Prizes:** [Spacetime] Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** ESP32 wristbands for concert attendees that sense crowd density, flash SOS circles on falls, guide exits, auto-process insurance claims and generate post-event recaps, all backed by a SpacetimeDB module.
- **Problem / user:** Falls in dense crowds can go unnoticed and crush people; attendees also lose connections and merch, and injury claims take weeks. / festival/concert attendees, medics and event organizers
- **Domain / idea type:** safety_security + fintech_finance / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / llm_chat; agent_or_tool_use; rag_or_search; recommendation
- **Stack:** langs Rust; TypeScript; C++; Python; SQL; frontend React; Sigma.js; Bun; backend Rust; SpacetimeDB; Elasticsearch; db SpacetimeDB; hosting Vultr; Caddy; SpacetimeDB Maincloud
- **Tech/APIs:** SpacetimeDB (Maincloud, reducers, subscriptions, SpacetimeAuth) (database, core, sponsor); Elastic (Agent Builder, ES|QL, semantic_text, Kibana) (database, core, sponsor); Anthropic Claude (ai_model, core, sponsor); Bright Data Web MCP (data_source, core, sponsor); Capital One Nessie API (payments, supporting, sponsor); Vultr (cloud, supporting, sponsor); Seeed XIAO ESP32-C3 + WS2812B + MPU-6050 + NTAG215 (hardware_part, core); OpenCV (framework, unclear)
- **Sponsor APIs:** SpacetimeDB; Elastic; Anthropic Claude; Bright Data Web MCP; Capital One Nessie API; Vultr | fit: Ran the entire live event as one SpacetimeDB Maincloud module: reducers as the only write path (SOS incident, light circle and escalation commit together), scheduled reducers for zone state, SpacetimeAuth and per-caller views for access control.
- **Repo:** public, commits 726 (before/in/after event: 0/726/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 14, writeup long, impact claims True (Cites National Safety Council accident statistics for motivation; reports 245 scraped records and demo claim savings figures.)
- **Notes:** Wearable bands with LED ring, NFC and ESP-NOW mesh work offline; one Rust SpacetimeDB module is the live event state; claims agent uses Claude plus Elastic with code deciding amounts; event data is Cal Hacks itself scraped via Bright Data (245 records).
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/bandit-the-only-band-you-need) | [GitHub](https://github.com/viktorinkov/cal-hacks-13)

### Ender's Bench  (Cal Hacks 13.0)

- **Prizes:** [Spacetime] Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** AI-behavior benchmark with a live survival simulation and a finance (credit sandbox) desk benchmark, run inside SpacetimeDB, comparing how models follow ethical policies under pressure.
- **Problem / user:** Explaining a rule differs from following it when it costs something; the team wanted visible evidence of whether models obey policies under pressure. / AI safety/evaluation researchers and model developers
- **Domain / idea type:** ai_agents_infra + fintech_finance / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; predictive_ml
- **Stack:** langs TypeScript; Python; JavaScript; frontend React; React Three Fiber; Three.js; Vite; backend SpacetimeDB module (TypeScript); Node.js; db SpacetimeDB; hosting SpacetimeDB Maincloud; Apify; Runpod
- **Tech/APIs:** SpacetimeDB (20 Hz tick, scheduled procedures, views, Maincloud) (database, core, sponsor); Anthropic Claude Haiku (ai_model, supporting); OpenAI GPT (ai_model, supporting); Bitdeer Model Studio (DeepSeek, GLM, Qwen) (ai_model, supporting); CRS credit sandbox (data_source, core); Apify Actor (cloud, supporting); NVIDIA DGX Spark LoRA fine-tuning (hardware_part, supporting); Runpod vLLM (cloud, supporting); Figma (other, token)
- **Sponsor APIs:** SpacetimeDB | fit: Used SpacetimeDB as game server, agent runtime and scorekeeper in one TypeScript module: 30+ tables, reducer-per-action commits with policy-detector records, scheduled procedures calling model providers over HTTP, and a public leaderboard view.
- **Repo:** public, commits 366 (before/in/after event: 0/366/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims True (Reports own experiment results, e.g. rule-breaking cut from 6.0% to 2.9% across 126 runs and 231 finance cases.)
- **Notes:** Models are called from inside SpacetimeDB via scheduled procedures with HTTP fetch (126 overnight runs, 8 models); also fine-tunes its own LoRA model on DGX Spark and ships an Apify Actor; reports quantitative findings.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; team_size
- **Links:** [Devpost](https://devpost.com/software/ender-s-bench) | [GitHub](https://github.com/BeanyZoldyck/endersbench)

### GeonosisAI  (Cal Hacks 13.0)

- **Prizes:** [Spacetime] Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** Agent-run factory that deploys a robot policy end to end: baselines, diagnoses failures, buys targeted demonstration data from phone-based contributors, fine-tunes pi0.5 and re-evaluates.
- **Problem / user:** Robot data collection and deployment loops are manual, slow and costly; the author wanted agents to buy the exact data a robot needs from paid contributors. / robotics teams deploying manipulation policies
- **Domain / idea type:** ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; agent_or_tool_use; vision; predictive_ml
- **Stack:** langs Python; TypeScript; frontend Next.js; Three.js; Tailwind CSS; backend FastAPI; SpacetimeDB; Modal; db SpacetimeDB; hosting Vercel; Modal; Cloudflare tunnels
- **Tech/APIs:** SpacetimeDB (maincloud, reducers, event log) (database, core, sponsor); Anthropic Claude (API / Claude Code) (ai_model, core); Factory Droid (other, core); Modal H100 (pi0.5 LoRA) (cloud, core); LeRobot / openpi (framework, core); I2RT YAM arm + NVIDIA Jetson (hardware_part, core); MuJoCo (framework, supporting); Stripe (test mode) (payments, supporting); Discord / iMessage (other, supporting)
- **Sponsor APIs:** SpacetimeDB | fit: Used SpacetimeDB maincloud as the shared bus for all services, agents, robots and phones, with reducers enforcing one arm-control lease per robot, per-payout budget checks and an append-only event log, targeting Best Use of Spacetime.
- **Repo:** public, commits 289 (before/in/after event: 0/289/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 11, writeup long, impact claims False
- **Notes:** Solo build on a real I2RT YAM arm (Jetson) plus MuJoCo sim; agents park on database predicates and are woken by a resume bridge; payouts via Stripe test mode; sim/real rows labelled; backend runs on author's laptop behind tunnels.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/robofactory) | [GitHub](https://github.com/jaximus808/GeonosisAI)

### Luyten  (Cal Hacks 13.0)

- **Prizes:** [Spacetime] Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** Multi-agent month-end close for SaaS startups where worker agents only propose, a cross-vendor Red Team critiques, an Advisor rules and the CFO confirms material items before anything posts to the ledger.
- **Problem / user:** Month-end close takes about ten days and CFOs will not let an unsupervised model post to the general ledger. / startup CFOs and finance teams
- **Domain / idea type:** fintech_finance + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; frontend SvelteKit; Vite; backend SpacetimeDB; Node.js; Claude Agent SDK; Vercel AI SDK; db SpacetimeDB; hosting GitHub Pages
- **Tech/APIs:** SpacetimeDB (ledger, approval queue, audit trail, message bus, identities) (database, core, sponsor); Claude Agent SDK / Anthropic (ai_model, core); Grok + Gemini (Red Team) (ai_model, core); CRS Credit API (via MCP) (data_source, core); Bright Data (data_source, supporting); Fetch.ai Agentverse (other, supporting); Apify (other, token); Moss (other, unclear)
- **Sponsor APIs:** SpacetimeDB | fit: Used SpacetimeDB as the whole backend (ledger, approval queue, audit trail, agent message bus), with reducers checking caller identity so the approval gate is enforced in the database; CI smoke-tests every gate against a real SpacetimeDB.
- **Repo:** public, commits 223 (before/in/after event: 0/223/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 2, writeup long, impact claims True (Cites a ten-day month-end close; reports 156 engine tests and a demo close producing 52 Proposals.)
- **Notes:** Approval gate enforced in SpacetimeDB reducers with per-role identities rather than prompts; six agents across Claude, Grok, Gemini and OpenAI; CRS credit cascade via MCP and Bright Data for counterparty checks; recorded stand-ins allow keyless demo; also on Fetch.ai Agentverse.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/cafoo) | [GitHub](https://github.com/3nvyx/luyten.git)

### Orkio  (Cal Hacks 13.0)

- **Prizes:** [Spacetime] Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** Real-time coordination layer that lets AI coding agents on different laptops share intentions via MCP, snapshot unfinished work through Git and resolve integration conflicts with a Factory Droid orchestrator.
- **Problem / user:** Parallel AI coding agents produce branches that merge cleanly but do not work together because they share no live context. / developer teams using multiple AI coding agents
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web; cli / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; JavaScript; frontend React; Vite; backend Node.js; SpacetimeDB; Factory Droid SDK; MCP; db SpacetimeDB; hosting 
- **Tech/APIs:** SpacetimeDB (subscriptions, transactional reducers) (database, core, sponsor); Factory Droid SDK (framework, core); Claude Code hooks / Claude API (ai_model, core); Model Context Protocol (framework, core); Git snapshots (other, core); Vitest (framework, token)
- **Sponsor APIs:** SpacetimeDB | fit: Used SpacetimeDB as the shared coordination backbone for agent status, code snapshots, intentions, tasks, conflicts and repair assignments, using subscriptions to sync agents and the dashboard and reducers to record a conflict and its assignment together.
- **Repo:** public, commits 59 (before/in/after event: 0/59/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims True (Single benchmark: 78% fewer prompts, 37.5% faster, about 11.6% fewer tokens, with a caveat that it is not statistically validated.)
- **Notes:** Claude Code hooks push wip/<agent> Git snapshots; SpacetimeDB holds shared agent state with subscriptions and transactional reducers; one Flappy Bird benchmark reports 2 vs 9 prompts and 10 vs 16 minutes against GitHub-only; setup reported hard for others to install.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/gehub) | [GitHub](https://github.com/chuddrw/CalHacks26)

### Pacioli  (Cal Hacks 13.0)

- **Prizes:** [Spacetime] Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** Collaborative canvas where a Bookkeeper agent categorizes bank, Stripe and QuickBooks transactions, flags uncertain items for human review, emails vendors and learns patterns from the user's answers.
- **Problem / user:** Small companies postpone accounting; the team wanted an autonomous back office that only escalates the judgment calls. / small business owners and founders
- **Domain / idea type:** fintech_finance + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; frontend Next.js; React; React Flow; backend SpacetimeDB; Factory Droid API; AgentMail; db SpacetimeDB; hosting Vercel
- **Tech/APIs:** SpacetimeDB (real-time sync) (database, core, sponsor); Factory Droid API (framework, core); Capital One Nessie API (payments, supporting); AgentMail (other, supporting); React Flow (framework, supporting); Figma (other, token)
- **Sponsor APIs:** SpacetimeDB | fit: Built the app on SpacetimeDB so ledger and agent events sync live to every collaborator on the shared canvas, targeting Best Use of Spacetime; the page gives little detail on specific reducers or tables.
- **Repo:** public, commits 100 (before/in/after event: 0/99/1), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup short, impact claims False
- **Notes:** Agents run on Factory Droid in a cloud computer using a self-built cloud-agent SDK; Nessie supplies deliberately messy bank data; AgentMail sends vendor emails; React Flow canvas.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots; team_size (second member private)
- **Links:** [Devpost](https://devpost.com/software/pacioli) | [GitHub](https://github.com/Rahuchpred/Pacilio)

### Rally  (Cal Hacks 13.0)

- **Prizes:** [Spacetime] Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** Browser badminton game where the laptop shows a 3D court and a phone's motion sensors act as the racket, for 1v1 over the internet or against a CPU, with SpacetimeDB as the server-side referee.
- **Problem / user:** Wii-Sports-style motion sports normally need a console; the team used phones and laptops people already own. / casual players wanting remote multiplayer sports games
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web; mobile_cross / False / False
- **Stack:** langs TypeScript; JavaScript; frontend Three.js; Vite; Web Audio API; DeviceMotion API; backend SpacetimeDB; Node.js; db SpacetimeDB; hosting Cloudflare Tunnel
- **Tech/APIs:** SpacetimeDB (private tables, views, scheduled reducers) (database, core, sponsor); Three.js (framework, core); DeviceMotion / DeviceOrientation API (other, core); Cloudflare Tunnel (cloud, supporting)
- **Sponsor APIs:** SpacetimeDB | fit: Used SpacetimeDB as database, game server and real-time sync: server-authoritative shot resolution, clock-checked swings, and private tables and views so the opponent's shot is withheld until it crosses the net.
- **Repo:** public, commits 201 (before/in/after event: 0/201/0), README solid
- **Demo/writeup:** video True, live none, screenshots 15, writeup short, impact claims False
- **Notes:** Server-authoritative design: SpacetimeDB decides shots, landings, points and CPU moves, checks swing timing against its own clock, and enforces fog of war with private tables and views; page shows badminton, ping pong and bowling screens.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/locomotion-5i4gzy) | [GitHub](https://github.com/JacobQuion/Cal-Hacks-Final-Project)

### skyFall  (Cal Hacks 13.0)

- **Prizes:** [Spacetime] Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** Live 3D globe forecasting when decaying satellites re-enter and which components survive, using GPU Monte Carlo physics, with SpacetimeDB as the only backend.
- **Problem / user:** The public only gets a single re-entry date and no insight into surviving debris; analyses stay inside agencies. / public, space-situational-awareness enthusiasts and researchers
- **Domain / idea type:** safety_security + other / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; Python; frontend React; CesiumJS; Three.js; backend SpacetimeDB module; PyTorch GPU workers; db SpacetimeDB; hosting Vultr
- **Tech/APIs:** SpacetimeDB (scheduled procedures, job leases, SGP4 in module, subscriptions) (database, core, sponsor); CelesTrak orbit data (data_source, core); NOAA SWPC space weather (data_source, core); PyTorch GPU Monte Carlo (NRLMSIS 2.1) (framework, core); CesiumJS (maps_geo, core); Cursor / Grok / Claude (dev agents) (ai_model, supporting); Vultr (cloud, supporting)
- **Sponsor APIs:** SpacetimeDB | fit: Made SpacetimeDB the entire backend: scheduled procedures make outbound HTTP ingest calls, reducers run a leased job queue with database-rule failover, SGP4 runs inside the module, and the globe subscribes directly to tables with no API layer.
- **Repo:** public, commits 58 (before/in/after event: 0/58/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 5, writeup long, impact claims True (Reports 32.7 million simulated futures, 752 billion steps, 22x GPU speedup, and early forecasts running 7 to 11 hours late versus official predictions.)
- **Notes:** One 2,400-line TypeScript SpacetimeDB module (32 tables, 29 reducers, 6 schedules) ingests CelesTrak/NOAA via procedures, runs a lease-based job queue with GPU-to-CPU failover (7 s measured) and scores its own forecasts; physics runs on an ASUS Ascent GX10.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/skyfall-uca4i9) | [GitHub](http://github.com/bobbybendola/skyFall)

### Vouch  (Cal Hacks 13.0)

- **Prizes:** [Spacetime] Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** Video-based refund claims investigated by Factory Droid and CREAO agents into evidence-backed merchant recommendations and a portable shopper trust score, tested on a 10,000-shopper simulated economy in SpacetimeDB.
- **Problem / user:** Refunds are slow for honest customers while merchants lose billions to fraudulent returns, and agent-driven commerce needs a trusted reliability signal. / online merchants and shoppers requesting refunds
- **Domain / idea type:** fintech_finance + retail_consumer / automation_or_agent
- **Platforms / hardware / AI:** web; mobile_cross / False / agent_or_tool_use; vision; speech_or_voice; llm_chat
- **Stack:** langs TypeScript; Python; frontend Next.js; React; react-globe.gl; Recharts; Three.js; backend Node.js; Fastify; SpacetimeDB; FFmpeg; faster-whisper; DuckDB; db SpacetimeDB; DuckDB; hosting Cloudflare Tunnel
- **Tech/APIs:** SpacetimeDB (scheduled reducers, subscriptions, credential registry) (database, core, sponsor); Factory Droid SDK (custom MCP tools) (framework, core); CREAO agents (ai_model, core); CRS Fraud Finder / TransUnion TruValidate (data_source, supporting); FFmpeg + faster-whisper (ai_model, supporting); Ed25519 signed credentials (auth, supporting)
- **Sponsor APIs:** SpacetimeDB | fit: Used SpacetimeDB for shared case state, a scheduled 10,000-shopper economy, and reducers enforcing authorization, controller escalation above $500 and once-only score updates, calling it the operational backbone.
- **Repo:** public, commits 86 (before/in/after event: 0/86/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 15, writeup long, impact claims True (Cites $103 billion US fraudulent-return losses (Appriss/Deloitte) and an NRF consumer survey; reports a 155-second recorded review.)
- **Notes:** Claims are video plus spoken explanation with an in-video challenge; findings must cite artifact timestamps; SpacetimeDB runs a deterministic economy of 10,000 shoppers and 100 merchants plus bounded score and approval reducers; CRS identity screening only partly wired; payouts simulated.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/vouch-7i3bft) | [GitHub](https://github.com/shubhaych/vouch)
