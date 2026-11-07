# HackUTD — HackUTD 2025 (37 projects)

### Alchemetrics
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Nvidia

**What it is:** Dashboard for a fictional potion factory where an NVIDIA Nemotron planner coordinates specialist agents. They detect when cauldrons are drained, match transport tickets, flag discrepancies, forecast overflow and plan witch collection routes.
**Problem / user:** Operators of the themed potion factory whose cauldron logs and collection tickets do not always match reality, so potion goes missing or overflows.

**Features**
- Drain event detection — Slope/hysteresis analysis of level data finds collection events and true volumes *[claimed]*
- Ticket matching — Matches transport tickets to detected events, handling outliers *[claimed]*
- Discrepancy auditor — Flags under-, over-reported or missing potion by tolerance rules *[claimed]*
- Overflow forecasting — Predicts cauldron fill level and overflow timing *[claimed]*
- Route optimization — OR-Tools plans efficient witch collection routes *[claimed]*
- Live dashboard — Map, timeline, tables and planner reasoning traces via aggregated state endpoint *[shown_working]*
- Nemotron planner — LLM decides which agent or tool runs next and logs its reasoning *[claimed]*

**Flow:** Data from cauldron sensors and tickets enters FastAPI → Planner routes work to agents → Dashboard shows map, timeline and anomalies → User reads reasoning traces

**Prompt:** not public / not found
**Fit (explicit):** Core orchestration uses NVIDIA Nemotron as planning agent, matching an NVIDIA agentic-AI track; Devpost challenge text not public.  *(targeted: Nvidia)*
**Sponsor tools:** NVIDIA Nemotron (Planner agent orchestrating specialist agents and logging reasoning, core)
**AI:** Nemotron acts as planner choosing among rule/algorithm-based agents; forecasting and optimization use NumPy, Pandas and OR-Tools; early mock responses before full integration.
**Architecture:** FastAPI backend with agent modules and a database; Next.js/Tailwind dashboard reads an aggregated overview endpoint.
**Novelty:** Explicit multi-agent design with explainable planner trace for an operations puzzle.
**Scope:** medium · working: Demo video embedded; repo has tests and about 5k LOC; README documents agents. · polish: Detailed README with architecture; demo scripts for no-factory runs.
**Gaps:** No NVIDIA challenge text; Database inconsistency in page
Sources: https://devpost.com/software/abc-xapnio, evidence/hackutd-2025-alchemetrics.json, https://hackutd-2025.devpost.com/

---

### AutoBoard
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Goldman Sachs

**What it is:** AWS serverless platform for onboarding financial vendors. It extracts data from tax and insurance documents, guides vendors through an 18-field KY3P questionnaire, scores risk and lets compliance staff approve in one click.
**Problem / user:** Compliance teams at large financial institutions slowed for weeks by manual vendor document review, and the vendors they onboard.

**Features**
- Document intake — AWS Textract extracts and validates W-9s and insurance certificates *[claimed]*
- KY3P questionnaire — 18-field questionnaire with real-time validation *[claimed]*
- Risk scoring — Scores compliance, cybersecurity, financial health and ESG *[claimed]*
- One-click approval — Review, approve and provision with an immutable audit trail *[claimed]*
- Tracking portal — Live status for internal staff and vendors *[claimed]*

**Flow:** Vendor registers → Uploads documents; data extracted → Fills questionnaire → Risk score computed → Compliance approves and provisions → Both sides track status

**Prompt:** not public / not found
**Fit (explicit):** Automates vendor onboarding at financial institutions, naming Goldman Sachs, and was awarded their track.  *(targeted: Goldman Sachs)*
**AI:** AWS Textract for document extraction; Gemini listed in tags with unstated role; risk scoring method not detailed.
**Architecture:** React/Vite/Tailwind portal, API Gateway, seven Python Lambda functions, RDS in VPC, defined as infrastructure as code.
**Novelty:** Full IaC serverless build with separate vendor and bank-side designs.
**Scope:** large · working: About 17k LOC, 116 files; no demo or video. · polish: README mirrors Devpost with system design diagrams; no tests.
**Claims:** Cuts compliance timelines from weeks to hours (unmeasured)
**Gaps:** No Goldman challenge text; No demo
Sources: https://devpost.com/software/404-not-found-us43mg, evidence/hackutd-2025-autoboard.json

---

### AutoPM
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner PNC Bank

**What it is:** Product-management copilot of Gemini-driven LangGraph agents inside per-project Spaces. Agents generate ideas, stories, market research, RICE rankings, OKR mapping, wireframes, stakeholder emails and Jira tickets.
**Problem / user:** Product managers juggling ideation, prioritization, wireframes, communication and ticketing under time pressure.

**Features**
- Idea generation — Researches problem and proposes sourced solutions *[claimed]*
- Story agent — Expands chosen solution into user stories, acceptance criteria, tech notes *[claimed]*
- Market research — Tavily web search for feedback, trends, competitors; themes not sentiment scores *[claimed]*
- RICE agent — Splits work into features and ranks by sortable RICE score *[claimed]*
- OKR alignment — Reads uploaded OKR PDF and maps work to goals *[claimed]*
- Wireframe agent — Generates interactive multi-page HTML/CSS mockups *[claimed]*
- Email and Jira agents — Sends Gmail updates; creates live Jira tickets from RICE output *[shown_working]*
- Context assistant — Chat aware of project history *[claimed]*

**Flow:** Create a Space → Run idea generation and pick a solution → Generate stories and research → Rank with RICE and align OKRs → Create wireframes → Send email and create Jira tickets

**Prompt:** not public / not found
**Fit (explicit):** README banner says 2nd place in the PNC Bank track; the product-management workflow link to PNC is not explained on the page.  *(targeted: PNC Bank)*
**AI:** Eight LangGraph/LangChain agents on Gemini 2.0 Flash with Zod-validated structured outputs and Tavily search; shared state passes outputs between agents.
**Architecture:** Next.js 14 front end and API routes, MongoDB via Mongoose, Auth0, LangGraph agents calling Gmail, Jira Cloud, Tavily and PDF ingestion.
**Novelty:** Covers the whole PM workflow end to end with real Jira and Gmail side effects.
**Scope:** large · working: Video embedded; screenshots of Spaces and live Jira tickets; about 15k LOC. · polish: Detailed README; auth, persistence and progress UI.
**Claims:** 7+ cooperating agents with type-safe outputs | Generated live Jira tickets end to end
**Gaps:** No PNC challenge text
Sources: https://devpost.com/software/autopm-2tjzu8, evidence/hackutd-2025-autopm.json

---

### Beacon
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** T-Mobile

**What it is:** Real-time customer happiness index for T-Mobile. It fuses live call transcripts, social posts and outage data into a 0-100 score shown on a map, plus dashboards for call agents and PR teams.
**Problem / user:** T-Mobile customer service agents and campaign teams lacking one real-time view of customer sentiment across calls, social and outages.

**Features**
- Happiness index map — Live 0-100 score by region and service from sentiment and network data *[shown_working]*
- Call pipeline — Twilio calls to Flask, Presidio removes PII, Llama on Groq classifies sentiment and issue, stored in MongoDB *[claimed]*
- Social and outage analysis — ForumScout posts and Downdetector trends analyzed for sentiment and emotion *[claimed]*
- Agent dashboard — Scrubbed live transcripts, sentiment, resolution suggestions, proactive alerts *[shown_working]*
- PR dashboard — Social triage and AI campaign generator, T-Mobile Tuesday offer planning *[shown_working]*
- Role-based login — Auth0 *[claimed]*

**Flow:** Log in via Auth0 → View national map of happiness → Agent sees live call sentiment → PR team triages social and generates campaign

**Prompt:** not public / not found
**Fit (explicit):** Directly builds a customer happiness index for T-Mobile, using branded mascot and offers; challenge statement not public.  *(targeted: T-Mobile)*
**AI:** Llama via Groq classifies sentiment, issue type and emotion; Presidio scrubs PII before model use.
**Architecture:** Twilio to Flask via ngrok to Presidio to Groq to MongoDB Atlas; Next.js dashboards with Auth0.
**Novelty:** Privacy-first PII scrubbing before LLM analysis and fusion of calls, social and outage feeds; dashboards update without WebSockets or polling.
**Scope:** medium · working: Video link and five screenshots; about 8k LOC; README is default template. · polish: Branded mascot and multiple dashboards.
**Claims:** Built in under 24 hours
**Gaps:** No T-Mobile challenge text; README is template
Sources: https://devpost.com/software/na-504rkg, evidence/hackutd-2025-beacon.json

---

### bevinAI
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Use of DigitalOcean Gradient AI by MLH

**What it is:** An AI project-management assistant framed for a bank. From a one-line idea it researches the market, recommends a tech stack, and generates a linked Jira board; later it checks pull requests against ticket requirements and records audit hashes on Solana.
**Problem / user:** Project managers and dev teams in regulated enterprises (PNC framing) who lose time between business goals, planning and development.

**Features**
- Idea to Jira board — Chained prompts analyze the idea, compare three tech stacks, then emit structured JSON for epics, stories and tasks pushed to Jira *[claimed]*
- Cost and functionality report — Market and tool research output with stack pros, cons and costs *[claimed]*
- Meeting-aware tickets — Meeting summaries mapped to tickets and kept in sync when decisions change *[claimed]*
- PR validation — Reads diff plus linked ticket acceptance criteria and flags missing requirements or scope creep *[claimed]*
- Solana audit trail — Hashes ticket sets, spec updates and PR approvals and anchors them on-chain *[claimed]*
- Post-deploy cost optimization report — Evidence-based report flagging redundant processes and over-provisioned resources *[claimed]*
- Unified dashboard — Single view of Jira and GitHub data *[claimed]*

**Flow:** Enter a one-sentence product idea → System researches market and feasibility → Receive cost report and stack recommendation → Linked Jira board is generated → PRs are validated against ticket requirements → Audit hashes anchored on Solana → After deploy, cost optimization report

**Prompt:** MLH prize for the best use of DigitalOcean Gradient AI; no challenge text public.
**Fit (none):** Page does not mention DigitalOcean Gradient AI; the AI brain is described as NVIDIA NIM (Nemotron-70B). Link to the MLH prize is not stated.  *(targeted: Best Use of DigitalOcean Gradient AI by MLH)*
**Sponsor tools:** NVIDIA NIM (Nemotron-70B) (reasoning, research, Jira ticket generation, PR validation, core); Solana (anchoring audit hashes, supporting)
**AI:** Nemotron-70B via NVIDIA NIM behind a FastAPI MCP server; multi-stage prompt chaining with structured JSON output; semantic comparison of code diffs to acceptance criteria.
**Architecture:** React dashboard on AWS Amplify captures intent; Django backend schedules async jobs and holds state; a FastAPI MCP server calls NIM; integrations with Jira, GitHub, Slack, Confluence; Solana for hashing.
**Novelty:** Combines planning, PR-to-requirement checking and blockchain-anchored audit trail in one flow; broad integration scope for a weekend.
**Scope:** medium · working: Demo video embedded; no repo linked, so build is unverifiable. · polish: Detailed writeup; no screenshots read.
**Claims:** Idea to Jira project in under 10 minutes | Could cut speed-to-market by weeks to months (projection)
**Gaps:** no repo; video not watched; prize challenge text
Sources: https://devpost.com/software/bevinai

---

### Cura
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** CBRE

**What it is:** A commercial real estate intelligence web app. CrewAI agents with a local Llama model produce forecasts, pros and cons, comparisons and market sentiment for listings, shown in Next.js dashboards backed by MongoDB.
**Problem / user:** Beginners and investors who lack access to commercial property knowledge, since few agents handle commercial real estate.

**Features**
- Property forecasting and insights — Agent crews generate analytics and reports for listings *[claimed]*
- Pros and cons analysis — Per-property evaluation against the user's financial goals *[claimed]*
- Property comparison — Interactive side-by-side comparison of listings *[claimed]*
- Market sentiment and trends — Sentiment and trend data combined with forecasts *[claimed]*
- Reasoning-based layout engine — UI layout and responses adapt to user input and context *[claimed]*
- Listing ingestion — parser directory does OCR and property data parsing; listings stored in MongoDB Atlas *[unclear]*

**Flow:** Open the dashboard and browse commercial listings → Ask the agent or navigate; reasoning agents use web search and analytics → View forecasts, sentiment and pros/cons → Compare properties against goals

**Prompt:** CBRE sponsor track; challenge text not public. README says it was built for the CBRE Challenge.
**Fit (explicit):** README states it was built for the CBRE challenge; it offers commercial property analytics, forecasting and comparison.  *(targeted: CBRE)*
**Sponsor tools:** NVIDIA models (Nemo/Nemotron per page) (agent LLMs; README lists Llama 3.1 via Ollama/vLLM with Gemini fallback, unclear); MongoDB Atlas (listings and analytics storage, supporting)
**AI:** CrewAI crews (Property Insights, Report Generation) with web and file tools on Llama 3.1 served locally; optional Gemini fallback.
**Architecture:** Next.js frontends call a FastAPI server running CrewAI agents; MongoDB Atlas holds data; a parser module handles OCR of property documents.
**Novelty:** Local open-weight LLM agents for a commercial real estate dashboard with an adaptive layout engine.
**Scope:** medium · working: Two Next.js apps and a FastAPI backend with start script; no demo or video. · polish: README with badges and quickstart; no tests.
**Claims:** Cites that only 21% of US agents work with commercial properties
**Gaps:** no demo flow; CBRE challenge text
Sources: https://devpost.com/software/tbd-58ftpr, evidence/hackutd-2025-cura.json

---

### DataDriver
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Northmark Compute & Cloud; Winner Nvidia

**What it is:** A work-order copilot for data centers. An agent running on NVIDIA Nemotron breaks a maintenance request into steps, runs tool actions it can do itself, escalates physical work to technicians, and regenerates the plan when an issue is reported.
**Problem / user:** Data center technicians who rely on clipboards and old docs and waste time guessing procedures.

**Features**
- Agent-generated workflows — LangChain/LangGraph agent turns a work order into step-by-step plan *[shown_working]*
- Automated tool execution — Agent runs tools such as reboots, diagnostics, temperature checks *[claimed]*
- Technician escalation — Detects steps needing physical work and hands off *[claimed]*
- Inventory check — Looks up stock for needed parts in MongoDB *[claimed]*
- Issue reporting and replanning — Reported problem triggers regenerated steps *[claimed]*
- Agent log and approvals — Logs reasoning and actions; approval requests for critical ops *[claimed]*

**Flow:** Create a work order → Agent plans steps and checks inventory → Agent executes automatable steps and logs reasoning → Physical steps escalate to a technician → Technician reports an issue and plan regenerates

**Prompt:** Northmark Compute & Cloud data-center technician challenge and the Nvidia track; no public challenge text.
**Fit (implied):** Targets data-center technician workflows with a Nemotron-powered agent; prize link not stated beyond the writeup's framing.  *(targeted: Northmark Compute & Cloud, Nvidia)*
**Sponsor tools:** NVIDIA Nemotron nano 9B v2 / NVIDIA AI Endpoints (agent reasoning, core); NeMo toolkit (listed in tags, unclear)
**AI:** ReAct-style LangChain/LangGraph agent on nemotron-nano-9b-v2 with a tool set for server operations and inventory.
**Architecture:** React/Vite frontend calls Flask REST API; agent module with tools; MongoDB via MongoEngine stores work orders, plan steps, logs, inventory.
**Novelty:** Agent that both executes remote tasks and decides when to escalate to a human, with replanning on reported issues.
**Scope:** medium · working: Full-stack repo with seed data and setup steps; one screenshot, no video. · polish: Detailed README; Tailwind and Framer Motion UI; no tests.
**Gaps:** no demo video; challenge text
Sources: https://devpost.com/software/datadriver, evidence/hackutd-2025-datadriver.json

---

### DCDaddy
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Northmark Compute & Cloud

**What it is:** An operations cockpit for NVIDIA-fabric data centers. It turns emails and Slack messages into tickets, bundles parallel tasks, routes technicians across multi-floor plans with health-aware warnings, forecasts inventory depletion, and offers a Gemini device assistant.
**Problem / user:** Data center technicians and ops admins using fragmented tools where errors are costly.

**Features**
- Ticket ingestion from email and Slack — LLM prompts normalize Gmail threads and Slack DMs into structured tickets *[claimed]*
- Ticket bundling — Heuristic engine groups parallel-safe tickets by severity, location, time *[shown_working]*
- Technician routing on floor plans — Multi-floor Dijkstra with elevator penalties and hot/cold lanes *[shown_working]*
- Health-aware assignment — Flags demanding tasks for technicians with listed conditions *[claimed]*
- Predictive inventory — Weeks-remaining formula from usage trend with status colours *[shown_working]*
- Field-ops device assistant — Gemini answers install/troubleshoot questions for about 10 devices *[claimed]*
- 3D rack viewer — GLTF server model with clickable hotspots *[claimed]*

**Flow:** Incoming email or Slack creates a ticket → Admin reviews dashboard and bundles → Technician sees routed tasks → Opens floor plan route and health cautions → Asks device assistant or views 3D rack → Checks inventory forecast

**Prompt:** Northmark NMC2 HPC data-center challenge; README frames covers admin and technician workflows, comms parsing, inventory, human-error prevention.
**Fit (explicit):** README titled for the NMC2 track and covers all five challenge areas in one app.  *(targeted: Northmark Compute & Cloud)*
**AI:** Gemini 2.0 Flash for the device assistant; GPT-4.1 prompts parse email and Slack into tickets; routing and forecasting are heuristic algorithms.
**Architecture:** Next.js 16 app with API routes; MongoDB Atlas for inventory; Gmail and Slack ingestion; localStorage shares tickets across pages.
**Novelty:** Health-profile-aware routing and a 3D rack overlay are unusual additions to a ticketing dashboard.
**Scope:** large · working: Live site dcdaddy.us linked; extensive route and algorithm files. · polish: Custom dark theme, five screenshots, detailed README.
**Claims:** Zero manual entry for ticket creation | Five-constraint routing algorithm | Marked Production Ready
**Gaps:** no video
Sources: https://devpost.com/software/fun-dashboard, evidence/hackutd-2025-dcdaddy.json

---

### Enchantress
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** EOG Resources

**What it is:** A fantasy-themed monitoring map: twelve potion cauldrons fill and drain while witches collect from them. The app plots levels over a week and flags where transport tickets disagree with actual drained volumes.
**Problem / user:** Operators tracking fluid or resource flow who must catch mismatches between logged transport and measured drain (oil-flow analogue).

**Features**
- Cauldron map — Interactive map of 12 cauldrons with different fill/drain rates *[shown_working]*
- Per-cauldron time series — Click a cauldron for minute-level levels over a week *[shown_working]*
- Ticket-vs-drain discrepancy detection — Compares collection tickets with drain events, flags over/under reporting and unlogged drains *[claimed]*
- Discrepancy dashboard — Weekly state per cauldron, inconsistent ones marked *[claimed]*
- Overflow forecasting — Predicting overflow and pickup schedules; page contradicts itself on whether built *[planned]*

**Flow:** Open map of cauldrons → Click a cauldron for its weekly graph → Open discrepancy dashboard → Inspect flagged cauldrons

**Prompt:** EOG Resources challenge in the potion/oil-flow dataset theme: reconcile transport tickets with measured drains.
**Fit (implied):** Reframes oil transport reconciliation as a potion game and builds ticket-versus-drain mismatch detection.  *(targeted: EOG Resources)*
**AI:** none
**Architecture:** TypeScript React single-page app (Vite) visualizing provided or simulated cauldron and ticket data with matching logic client-side.
**Novelty:** Gamified fantasy skin over an oil-reconciliation problem.
**Scope:** small · working: Video embedded; repo is a Vite app of about 3.7k lines with the default template README. · polish: Animated themed map; no setup docs.
**Gaps:** README is template; video not watched
Sources: https://devpost.com/software/enchantress-w2li90, evidence/hackutd-2025-enchantress.json

---

### HarmoniQ
*HackUTD HackUTD 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Winner T-Mobile [3rd]; Winner Best Use of Auth0

**What it is:** A dashboard for telecom product teams that joins network performance data with social sentiment from Reddit and X. It predicts regional outage risk with trained classifiers and has a Gemini assistant that explains correlations and proposes actions.
**Problem / user:** T-Mobile product managers and network engineers who see network metrics and customer sentiment as separate worlds.

**Features**
- Live sentiment tracking — Pulls posts from Reddit and X and scores them against network history *[claimed]*
- Outage prediction — Random Forest and Gradient Boosting models on latency, packet loss, complaint frequency *[claimed]*
- Customer Happiness Index — Real-time composite metric on the dashboard *[claimed]*
- Gemini insights assistant — Explains correlations and suggests next actions *[claimed]*
- Dashboard modules — Network Health, Sentiment, CHI, AI Insights, Outage Predictor, hotspots *[shown_working]*
- Auth0 login — Login and landing pages *[shown_working]*
- Alert automation to Slack or Jira — Gemini-triggered workflows *[planned]*

**Flow:** Land and log in via Auth0 → Open dashboard → Review network health, sentiment and CHI → Check outage predictions and AI insights → Allocate resources or assign tasks

**Prompt:** T-Mobile track (customer sentiment versus network data) and MLH Auth0 prize; challenge text not public.
**Fit (implied):** Writeup targets T-Mobile product managers by fusing network and sentiment data; Auth0 used for login.  *(targeted: T-Mobile, Best Use of Auth0)*
**Sponsor tools:** Auth0 (authentication, supporting); Gemini API (insight assistant, core)
**AI:** scikit-learn Random Forest and Gradient Boosting trained offline on Kaggle data plus synthetic outages; Gemini grounded in live data with tuned prompts.
**Architecture:** React/Vite/Tailwind frontend; Python FastAPI/Flask backend serving models and data; Reddit and X feeds; Kaggle historical data; Auth0.
**Novelty:** Fuses social sentiment with outage prediction in one product-manager view.
**Scope:** medium · working: Repo of about 12k lines; no demo or video; outage data partly synthetic. · polish: Six screenshots; README empty in evidence.
**Claims:** Claims strong outage forecast accuracy, no metrics
**Gaps:** README empty; no demo
Sources: https://devpost.com/software/x-yiqm81, evidence/hackutd-2025-harmoniq.json

---

### HealthSense
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best Use of Vultr

**What it is:** A wearable vitals kit for data center workers. An Arduino reads accelerometer, heart rate and temperature sensors; a Raspberry Pi 5 streams them to Redis on Vultr; a Nemotron agent judges whether the wearer is in trouble and triggers a vibration alert.
**Problem / user:** Data center workers in hot, stressful environments who need prompts to take breaks.

**Features**
- Sensor capture — Arduino UNO samples accelerometer, heart-rate and temperature sensors *[shown_working]*
- Cloud streaming — Pi 5 forwards readings into Redis streams hosted on Vultr *[shown_working]*
- Agentic trouble detection — Nemotron agent compares recent and past data to judge risk *[claimed]*
- Vibration alert with dismiss button — Wearable buzzes on concern; button says user is fine *[claimed]*
- Anomaly model — Repo has PyTorch next-value forecasting on sliding windows; large errors flag anomalies; synthetic data seeding *[shown_working]*
- Web front end — Shows worker feedback and single-worker sensor data *[shown_working]*

**Flow:** Wear sensors → Arduino sends to Pi → Pi writes to Redis on Vultr → Agent reviews data → Wearable vibrates if concerning → Wearer presses button if fine → Web UI shows worker data

**Prompt:** MLH Vultr prize for best use of Vultr cloud; no challenge text found.
**Fit (implied):** Redis database and ML training host are on a Vultr server.  *(targeted: Best Use of Vultr)*
**Sponsor tools:** Vultr (hosting Redis and GPU training instance, supporting); NVIDIA Nemotron (agentic analysis of sensor data, core)
**AI:** Nemotron agent reviews recent versus historical readings; separate PyTorch window-prediction model for anomaly signal; README mentions synthetic data for bootstrapping.
**Architecture:** Arduino sensors to Raspberry Pi 5 to Flask receiver to Redis streams on Vultr; ML module and agent read history; web front end plus vibration actuator.
**Novelty:** Physical wearable with hardware-to-cloud-to-agent loop and haptic feedback, uncommon among the dashboard-heavy entries.
**Scope:** medium · working: Three screenshots including hardware setup; repo has tests and server/ml code; no video. · polish: README with flow diagram; team notes sensor reliability issues.
**Claims:** 5 sensors, 2 boards, 1 cloud service, 1 database, 1 agent
**Gaps:** no video; agent code not inspected
Sources: https://devpost.com/software/healthsense-0qxrs4, evidence/hackutd-2025-healthsense.json

---

### Hingine
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Toyota Financial Services

**What it is:** A Expo/React Native mobile app for students shopping for a Toyota. It has a Tinder-style swipe deck of vehicles, finance micro-lessons with quizzes that earn points, a rewards wallet of financing perks, and a dream garage for goals.
**Problem / user:** College students intimidated by car financing and leasing with little credit history.

**Features**
- Match Lab swipe deck — Animated swipe gestures over Toyota vehicles with financing highlights *[shown_working]*
- Learn tab — Micro-lessons plus quizzes awarding points *[shown_working]*
- Rewards wallet — Points unlock perks such as rate boosts, lease cash, down-payment match *[claimed]*
- Dream garage — Track saved vehicles and savings goals *[claimed]*
- Profile hub — Personal details and financial snapshot *[claimed]*
- Toyota Financial Services connection — README says API hookup pending *[planned]*

**Flow:** Swipe through cars → Save favorites to garage → Complete lessons and quizzes → Earn points → Unlock APR or lease incentives

**Prompt:** Toyota Financial Services sponsor track; challenge text not public.
**Fit (explicit):** README titled as the Toyota Financial hackathon MVP; ties financial literacy to simulated TFS rewards for young buyers.  *(targeted: Toyota Financial Services)*
**Sponsor tools:** Toyota Financial Services data (vehicle and financing content; real API integration listed as next step, unclear)
**AI:** none
**Architecture:** Expo 51 React Native app with bottom-tab navigation and Context API state; no backend.
**Novelty:** Pairs dating-app swiping with gamified financial education that unlocks financing incentives.
**Scope:** small · working: Runnable Expo MVP, about 3.9k lines; demo video and six screenshots. · polish: Clear README and tabbed UI; no tests or backend.
**Gaps:** video not watched
Sources: https://devpost.com/software/hingine, evidence/hackutd-2025-hingine.json

---

### hyperlynx
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence low*
**Prizes:** Best Domain Name from GoDaddy Registry

**What it is:** A layer over a custom Jira instance that simulates data center work orders. It aims to add AI context to tickets for technicians and give managers tracking and compliance help, with Auth0 login and a hand-drawn branding package.
**Problem / user:** Data center technicians and managers who struggle to get context from tickets; also pitched at emergency dispatch.

**Features**
- Jira-based ticket workflow — Custom Jira instance fed by API calls to simulate work orders *[claimed]*
- AI ticket context — Gemini listed as adding context; method not explained *[unclear]*
- Manager oversight — Tracking of work orders for compliance and error reduction *[claimed]*
- Auth0 authentication — Login security *[claimed]*

**Flow:** Work order arrives in Jira → AI adds context → Technician responds → Manager tracks progress

**Prompt:** MLH/GoDaddy Registry prize for best domain name; plus project targeted data-center ticketing (NMC2).
**Fit (implied):** Registered the hyperlynx.us domain; the page also frames the project around the NMC2 data center challenge.  *(targeted: Best Domain Name from GoDaddy Registry)*
**Sponsor tools:** GoDaddy Registry domain (hyperlynx.us demo site, token); Auth0 (authentication, supporting); Vultr (hosting Django backend, supporting)
**AI:** Gemini listed in tags; page gives no detail on prompts or usage.
**Architecture:** React/Bootstrap frontend with a Django backend on Vultr, custom Jira instance, Auth0.
**Novelty:** Builds on Jira rather than a bespoke ticket system, because the target organization uses it.
**Scope:** small · working: Live site hyperlynx.us and repo of about 2.5k lines; no video. · polish: Branding package and four screenshots; README empty.
**Gaps:** README empty; AI use unexplained; no demo walkthrough
Sources: https://devpost.com/software/hyperlynx, evidence/hackutd-2025-hyperlynx.json

---

### InsighT
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner T-Mobile

**What it is:** A customer-intelligence dashboard for T-Mobile product managers. It scrapes Reddit, news and outage trackers, scores sentiment into a Customer Happiness Index by product area, maps hotspots and outages, and uses Gemini to write prioritized opportunities, PRDs and user stories.
**Problem / user:** T-Mobile product managers who cannot tell where customers are hurting amid scattered feedback.

**Features**
- Multi-source ingestion — Scrapers for Reddit, Google News, DownDetector and others behind a cron-secured endpoint *[shown_working]*
- CHI and trends — Sentiment index by Network, App, Billing, Home Internet *[shown_working]*
- Geographic heatmap with outage markers — Leaflet heat layer with Nominatim geocoding *[shown_working]*
- Top emerging issues and early warning — Ranked by intensity and sentiment with deduplication *[shown_working]*
- Gemini opportunities — Priority, root cause, actions, stakeholders per issue *[shown_working]*
- PRD and user story generation — AI generates documents from signals *[claimed]*

**Flow:** Open dashboard → Check CHI by product area → Inspect heatmap and outages → Review top emerging issues → Read AI opportunities or generate PRD

**Prompt:** T-Mobile sponsor track; challenge text not public.
**Fit (explicit):** README and page aimed at T-Mobile PMs; gives prioritized, location-aware actions from customer signals.  *(targeted: T-Mobile)*
**AI:** Gemini 2.0 Flash via server routes for insights, PRDs and stories; sentiment scoring, topic detection and dedup are in the pipeline.
**Architecture:** Next.js App Router on Vercel; Supabase Postgres; scrapers feed tables via cron; Gemini API routes; Leaflet and Recharts front end.
**Novelty:** Goes from signal to generated PRD and stories rather than stopping at a dashboard.
**Scope:** large · working: Live site insight-tmobile.us, demo video, about 20k lines. · polish: 15 screenshots, detailed README; no tests.
**Claims:** Self-described production-ready
**Gaps:** none
Sources: https://devpost.com/software/t-insights, evidence/hackutd-2025-insight.json

---

### Kachow
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Toyota Financial Services

**What it is:** A car-buying guide with a chatbot (KaBot) that surfaces prices, insurance, gas, maintenance and APR figures and nudges users toward financing decisions using connected (mock) bank data.
**Problem / user:** Car buyers facing dozens of research hours and hidden costs; cites 46% buyer's remorse.

**Features**
- KaBot assistant — Chatbot answering car questions with an OpenAI-based agent *[claimed]*
- Real-time cost figures — Shows insurance, gas, maintenance and APR for chosen car *[claimed]*
- Mood and need based car picking — Recommends cars by user feelings and needs *[claimed]*
- Bank connection — Mock bank data informs financing advice *[claimed]*
- Hidden ownership costs — Explains responsibilities beyond sticker price *[claimed]*

**Flow:** Choose a car → Review costs and APRs → Ask KaBot → Connect (mock) bank account → Finalize decision

**Prompt:** Toyota Financial Services sponsor track; challenge text not public.
**Fit (implied):** Helps buyers understand financing and APR via chatbot and bank data; link to the prompt is inferred.  *(targeted: Toyota Financial Services)*
**Sponsor tools:** NVIDIA Nemotron (listed in tags; text mentions OpenAI agent, unclear)
**AI:** Chat agent over car price data; page claims no hallucinations but gives no method; model unclear (OpenAI vs Nemotron).
**Architecture:** React frontend, Node.js backend with an agent layer, MongoDB, mock banking data.
**Novelty:** Combines buyer-remorse framing with bank-linked cost advice.
**Scope:** small · working: Website kachow.biz, demo video on GitHub README, about 4k lines. · polish: Four screenshots; styled README; no tests.
**Claims:** 46% of Americans have buyer's remorse | No AI hallucinations
**Gaps:** model ambiguity; video not watched
Sources: https://devpost.com/software/car-thing-1dsxyk, evidence/hackutd-2025-kachow.json

---

### Kori
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of Gemini API by MLH

**What it is:** A pixel-cat desk companion on a Raspberry Pi 5 touchscreen in a 3D-printed case. It senses sound, air, temperature and mood cues, rewards focus with coins for decorating its room, and syncs to a React Native app showing history and Gemini insights.
**Problem / user:** Students and remote workers who find long solo study sessions isolating and want gentle, non-judging company.

**Features**
- Focus-session companion — Wakes on session start, tolerates pauses, sleeps at day end *[shown_working]*
- Environment sensing — BME280, air-quality sensor, mic loudness, camera mood cues *[shown_working]*
- Gentle check-ins — Asks at most hourly with Yes or Later *[claimed]*
- Touch gestures — Tap to pause or end, pet, slide for brightness *[claimed]*
- Coins and room decorating — Consistent work earns coins *[claimed]*
- Mobile app — Session history, trends, shared room, settings, Gemini insights *[shown_working]*
- Privacy design — Camera and mic not stored or identifying *[claimed]*

**Flow:** Start a focus session on the device → Kori reacts to environment and mood → Pause, resume or pet via touch → Answer hourly check-in → Earn coins and decorate → Review trends in the phone app

**Prompt:** MLH prize for best use of the Gemini API; no challenge text found.
**Fit (implied):** Gemini generates the insights shown in the companion mobile app from sensor data.  *(targeted: Best Use of Gemini API by MLH)*
**Sponsor tools:** Gemini API (insights from environment and session data in the app, supporting)
**AI:** Gemini processes sensor data to produce insights; camera used for general mood recognition without storing images.
**Architecture:** Pi runs Express server for state and sensors plus an Electron UI; React Native (Expo) app syncs with the Pi; GPIO/I2C sensors.
**Novelty:** Custom-cased physical device with three coordinated runtimes and a pet-game reward loop.
**Scope:** large · working: Hardware build, demo site kori.study, YouTube video; repo about 69k lines. · polish: CAD-designed case, themed UI, has tests; README mostly RN boilerplate.
**Gaps:** video not watched
Sources: https://devpost.com/software/kori, evidence/hackutd-2025-kori.json

---

### MirrorAPI
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** StateFarm

**What it is:** A developer tool that compares the JSON responses of two API versions, lists added, removed and type-changed fields, scores migration risk, and exports a Markdown change report. A Nemotron RAG agent writes the narrative report.
**Problem / user:** Developers at firms with many API dependencies who must manually spot differences when an API upgrade changes its JSON.

**Features**
- Two-endpoint comparison — User pastes old and new API URLs or sample files; the app fetches both responses *[shown_working]*
- Field-level diff — Deterministic engine finds added, removed and type-changed fields shown in grouped table *[shown_working]*
- Migration risk score — README says a 0 to 100 score is computed *[claimed]*
- Nemotron change report — RAG agent writes insights on API design changes *[claimed]*
- Markdown export — Downloadable migration report *[claimed]*
- OAuth employee sign-in — Sign-in page *[claimed]*

**Flow:** Sign in → Enter two API endpoints → App fetches both responses → View grouped conflicts and risk score → Read or export generated report

**Prompt:** State Farm sponsor track; challenge statement not public (winners appeared to be API tooling).
**Fit (implied):** Page says the team won the StateFarm challenge and gathered sponsor feedback; the tool addresses API versioning documentation and compliance.  *(targeted: StateFarm)*
**Sponsor tools:** NVIDIA Nemotron (RAG report generation, chosen over Llama, core)
**AI:** Deterministic JSON diff for detection; Nemotron agent with retrieval writes the change report. README notes the diff itself is not AI.
**Architecture:** Next.js 14 TypeScript frontend with client-side diff; FastAPI Python service (nemotron folder) calls the model; OAuth sign-in.
**Novelty:** Pairs a deterministic diff with an LLM report, plus a numeric migration risk score.
**Scope:** small · working: Run instructions, sample public APIs named, four screenshots, video embedded. · polish: shadcn/ui interface; no tests.
**Claims:** Deterministic detection with no hallucination
**Gaps:** video not watched
Sources: https://devpost.com/software/mirror-api, evidence/hackutd-2025-mirrorapi.json

---

### NLB (Nothing Left Behind)
*HackUTD HackUTD 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner General Track

**What it is:** A native iOS app for roommates and families with shared shopping lists that notify members when they are near a store, and a receipt splitter that scans a receipt, extracts items and tallies what each person owes.
**Problem / user:** Roommates, families and friend groups who forget small errands and do manual math on shared bills.

**Features**
- Shared shopping lists — Group members see one combined list stored in Firestore *[shown_working]*
- Nearby-store reminders — CoreLocation geofencing triggers a notification, including while driving *[shown_working]*
- Receipt scanning — Vision OCR reads text and Gemini structures it into items *[shown_working]*
- Bill splitting — Assign receipt items to members and see totals owed *[shown_working]*
- Groups and login — Firebase auth with add/view members *[shown_working]*

**Flow:** Sign up and join a group → Add items to shared list → Get a notification near a store → Upload a receipt → Assign items to members → See totals owed

**Prompt:** General Track: open prize for the best overall hack, no theme.
**Fit (none):** Not tied to a sponsor challenge; a complete consumer app.  *(targeted: General Track)*
**Sponsor tools:** Gemini API (turning OCR text into structured item list, supporting)
**AI:** Apple Vision OCR then Gemini API converts raw text into an item list after OCR alone gave errors.
**Architecture:** SwiftUI iOS app; Firebase Auth and Firestore; CoreLocation geofences; Vision then Gemini receipt pipeline.
**Novelty:** Combines location-triggered group reminders with AI receipt splitting in one app.
**Scope:** small · working: Ten screenshots of each screen; about 2.5k lines of Swift; no video. · polish: Complete flow shown in screenshots; README empty.
**Claims:** Built in 24 hours on an unfamiliar stack
**Gaps:** no video
Sources: https://devpost.com/software/tbd-app, evidence/hackutd-2025-nlb.json

---

### Pact
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner CBRE; Winner Best Use of Solana

**What it is:** A B2B contract platform where vendors and clients draft with AI help, route changes through multi-party approval, tie payment milestones to escrow vaults on Solana, and anchor final contract hashes on-chain with documents on IPFS.
**Problem / user:** Vendors and clients who face slow, opaque partnership agreement and signing processes.

**Features**
- AI-assisted drafting and compliance — Gemini extracts security requirements and validates documents *[claimed]*
- Multi-party approval and versioning — Git-like change tracking and role permissions *[claimed]*
- Solana hash anchoring — Finalized contract hash recorded via Anchor programs *[claimed]*
- Milestone escrow — Vaults release funds when approval threshold met *[claimed]*
- Reputation and fraud scoring — Weighted reputation; 0-100 fraud score with on-chain and off-chain signals *[claimed]*
- Dashboard — Contracts, approvals, tasks, calendar, leaderboards *[shown_working]*

**Flow:** Create contract with AI help → Invite parties and approve changes → Approve milestone payments → Anchor final hash on Solana

**Prompt:** CBRE sponsor track and MLH Solana prize; challenge texts not public.
**Fit (implied):** Solana programs anchor contract hashes and escrow; contracts/deals framing fits a real estate sponsor but link is not stated.  *(targeted: CBRE, Best Use of Solana)*
**Sponsor tools:** Solana (Anchor) (deals, reputation and escrow programs, hash anchoring, core); Gemini API (contract extraction and risk scoring, supporting)
**AI:** Gemini extracts contract requirements, validates compliance documents and contributes to fraud risk scoring.
**Architecture:** Next.js frontend with Solana web3 and Anchor client; three Rust Anchor programs using PDAs and cross-program invocations; IPFS storage; Gemini calls.
**Novelty:** Substantial on-chain design (escrow, reputation, CPIs) beyond simple hash anchoring.
**Scope:** large · working: Page says Solana verification and IPFS work; writeup also lists escrow and reputation as future phases. · polish: Four screenshots; repo not fetched (clone failed).
**Claims:** Fraud score above 70 blocks or flags deals
**Gaps:** repo not readable; built vs planned unclear; no video
Sources: https://devpost.com/software/autotract

---

### PoyoLabs
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** EOG Resources

**What it is:** A pixel-art game-style dashboard for the potion cauldron dataset. It shows cauldrons, a network map, optimal routes and distances, historical playback, and an agentic chatbot enhanced with Nemotron.
**Problem / user:** Gamers and operators wanting potion collection, depletion and possible theft analytics in a retro game interface.

**Features**
- Cauldron overview — Gamified dashboard of multiple cauldrons *[shown_working]*
- Network map and route map — Optimal routes and distances between cauldrons *[claimed]*
- Historical playback — Replay of past data *[claimed]*
- Agentic chatbot — Poyo bot using Nemotron *[claimed]*
- Depletion and theft analytics — Collection and depletion rates and potential thievery *[claimed]*
- Pixel art and animation — Hand-made art, start screen *[shown_working]*

**Flow:** Open start screen → View cauldron overview → Open route map → Chat with bot

**Prompt:** EOG Resources potion-cauldron data challenge; no public text.
**Fit (implied):** Visualizes cauldron data with routes and anomaly analytics in a themed UI.  *(targeted: EOG Resources)*
**Sponsor tools:** NVIDIA Nemotron (chatbot, supporting); Auth0 (authentication, supporting); GoDaddy domain (hosting poyolabs.us, token)
**AI:** Autonomous chatbot on NVIDIA Nemotron inside a Flask app; details not given.
**Architecture:** Flask backend serving data to an HTML/CSS/JS pixel-art frontend; Auth0; hosted at poyolabs.us.
**Novelty:** Retro pixel-art game skin with hand-drawn animations over analytics.
**Scope:** small · working: Live site poyolabs.us listed; no repo or video. · polish: Custom pixel art and animations; details of backend unknown.
**Gaps:** no repo; no video; data handling unspecified
Sources: https://devpost.com/software/poyolabs-47n0fz

---

### PoyoPop
*HackUTD HackUTD 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Startup

**What it is:** A mobile-style app prototype that maps nearby food and drink pop-ups. Consumers browse, search, mark going or save; vendors create events and see analytics, with visit counts shown instead of ratings.
**Problem / user:** Small food vendors without large followings and consumers who cannot easily discover pop-ups nearby.

**Features**
- Pop-up map and list — Location-based map and scrollable curated list *[shown_working]*
- Pop-up details — Vendor, menu and estimated attendance *[shown_working]*
- Going and saved — Mark attendance or save *[shown_working]*
- Vendor event creation — Set time, place, offerings *[shown_working]*
- Visit counts instead of ratings — Vendor profiles show visits *[claimed]*
- Business analytics — Two vendor analytics screens *[shown_working]*
- Personalized recommendations — Based on prior visits *[claimed]*

**Flow:** Open home screen → View map or search → Open a pop-up → Mark going or save → Vendor creates event and reviews analytics

**Prompt:** Best Startup award: judged on startup viability; no text found.
**Fit (implied):** Page includes target users, launch and growth plan (influencers, city beta, markets), framing it as a business.  *(targeted: Best Startup)*
**AI:** none
**Architecture:** Figma Make generated React prototype with mock data; repo is a Vite bundle exported from Figma.
**Novelty:** Visit counts replace ratings to avoid discouraging new vendors; design-led prototype.
**Scope:** small · working: Interactive Figma Make prototype and demo video; no backend evident. · polish: About 9.7k lines generated UI, multiple screens; README is Figma template.
**Gaps:** map API unspecified
Sources: https://devpost.com/software/poyopop, evidence/hackutd-2025-poyopop.json

---

### ProdigyPM
*HackUTD HackUTD 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Winner General Track

**What it is:** An AI console that reads a product PDF, or builds a PRD through a chat consultant, splits it into department subprojects with estimates, priorities and acceptance criteria, pushes them to Jira in one click, and shows a live progress dashboard.
**Problem / user:** Product managers who spend hours reading documents, estimating and creating Jira tickets.

**Features**
- PDF analysis — pdfplumber extracts text; GPT-4 Turbo pulls goals, requirements and departments *[claimed]*
- Department subprojects — Decomposition agent adds estimate bands, priority, dependencies, criteria *[claimed]*
- PRD consultant chat — Agent asks questions and drafts PRD when no PDF exists *[claimed]*
- One-click Jira creation — Creates issues for all subprojects via Jira Cloud API *[claimed]*
- Live dashboard — Polls every 2 seconds for status, completion and department breakdown *[claimed]*

**Flow:** Upload PDF or open PRD chat → AI generates subprojects → Review them → Sync to Jira → Track dashboard until completion

**Prompt:** General Track: open prize, no theme.
**Fit (none):** Open category; project not tied to a sponsor challenge.  *(targeted: General Track)*
**AI:** Three GPT-4 Turbo agents (PDF, decomposition, PRD consultant) at temperature 0.3 with JSON output.
**Architecture:** Next.js 14 frontend polling a FastAPI backend; pdfplumber, OpenAI, Jira Cloud; local or S3 storage.
**Novelty:** End-to-end from document to tracked Jira work with session-scoped dashboards.
**Scope:** medium · working: Detailed technical writeup and screenshots described; no repo, live link or video. · polish: Dark mode UI; challenges section describes real debugging.
**Claims:** PDF to Jira tickets in minutes, not hours
**Gaps:** no repo; no demo link
Sources: https://devpost.com/software/prodigypm-kaqe09

---

### ProdPlex
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner PNC Bank

**What it is:** A multi-agent copilot for product managers in which different NVIDIA Nemotron models act as specialist agents (strategy, research, dev, prototype, GTM, automation, regulation). Users run one agent or combine them to draft a PRD, with Figma hooks for design output.
**Problem / user:** Product managers who spend too much time on documentation, research and coordination instead of strategy.

**Features**
- Seven specialist agents — Strategy, Research, Dev, Prototype, GTM, Automation and Regulation agents each handle a PM task, coordinated with LangGraph. *[claimed]*
- PRD generation — All agents combined to produce a product requirements document in minutes. *[claimed]*
- RAG-enhanced Nemotron — FAISS vector memory shares context between agents and adds retrieval to a Nemotron model. *[claimed]*
- Figma integration — Connects AI-generated PRDs to design mockup generation; README marks integrations as stubs/mocks. *[unclear]*
- Live dashboard and chat — React UI with agent panels, activity feed, chat and analytics pages, with WebSocket status updates. *[claimed]*
- Local LLM option — Ollama-served Llama 3 or Mistral as alternative to Nemotron API. *[claimed]*

**Flow:** Open dashboard and describe a product idea in chat → Pick a single agent (e.g. market research or prototype) or run all agents → Agents exchange shared context via vector memory → Review the generated research, strategy, stories and PRD → Optionally push to Figma/Jira (mock integrations)

**Prompt:** PNC Bank sponsor track at HackUTD 2025, framed (per the project pages) as reimagining the life of a product manager with generative AI; the official challenge text was only in the private hackerpack.
**Fit (explicit):** Devpost says it was built for the PNC challenge on reimagining the product manager's life with GenAI; agents cover PM tasks from research to PRD, plus a regulation/compliance agent labeled as the PNC challenge piece.  *(targeted: PNC Bank)*
**Sponsor tools:** NVIDIA Nemotron (Reasoning model behind the agents (small and medium variants), core)
**AI:** Several Nemotron models (small and medium) each power an agent; LangGraph orchestrates, FAISS vector memory provides shared context, optional Ollama local models; prompt structuring and caching for stability.
**Architecture:** React/TypeScript frontend talks to a FastAPI backend over REST and WebSocket; LangGraph task graph dispatches to seven agents, FAISS memory and SQLite context store, Nemotron bridge, mock Jira/Slack/Figma/Reddit adapters.
**Novelty:** Claims coordination without a central orchestrator, though the README describes a LangGraph task graph; includes a regulation-check agent specific to a bank sponsor.
**Scope:** medium · working: Full backend/frontend structure and setup steps in README; integrations are described as mock for MVP; demo video exists. · polish: Animated Tailwind/Framer Motion UI and detailed README; three screenshots.
**Claims:** Produces a PRD in minutes by combining agents | Multi-agent coordination without a central orchestrator | Nemotron budget kept under $40
**Gaps:** Official PNC challenge text not public; Video not watchable
Sources: https://devpost.com/software/prodify-94vbpk, https://github.com/Ka2507/hackutd2025, https://hackutd-2025.devpost.com/

---

### ProDuh!
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner PNC Bank

**What it is:** A multi-agent LLM command center for product managers covering discovery through deprecation. It turns goals and KPIs into Jira or Azure DevOps ready stories, keeps Confluence pages linked, and runs an operate loop that proposes backlog changes, with a human approving.
**Problem / user:** Product managers losing hours to copy-paste between Jira/ADO, Confluence and chat, with strategy and KPIs not reaching stories.

**Features**
- Strategy-to-stories — Generates briefs, KPIs and roadmap, then epics/stories/subtasks with acceptance criteria and QA checklist ready for Jira/ADO. *[claimed]*
- Jira enhancements — RICE/WSJF prioritization hints, dependency detection, sprint goal drafting, definition-of-done checklists, risk radar. *[claimed]*
- Operate loop — Agent monitors signals from a mock analytics CSV, opens bugs/incidents and proposes backlog deltas, capped at three loops. *[claimed]*
- App-agnostic adapters — Universal layer meant to work with Jira or ADO plus Confluence, MS Graph, ServiceNow and read-only GitHub. *[claimed]*
- Docs auto-linking — Creates and updates Confluence pages, keeps one canonical page per phase, and a My Notes area for links. *[claimed]*
- Portfolio view — Manage multiple products with per-product tabs across lifecycle phases. *[claimed]*

**Flow:** Paste messy discovery notes or goals → System structures them into KPIs and a roadmap → Generate backlog items shaped as Jira/ADO stories → Review, accept, edit or regenerate each draft → Operate loop feeds mock analytics back into backlog suggestions

**Prompt:** PNC Bank sponsor track at HackUTD 2025, framed (per the project pages) as reimagining the life of a product manager with generative AI; the official challenge text was only in the private hackerpack.
**Fit (implied):** Page lists a PNC Bank win; the tool addresses product-manager workload across the whole lifecycle with agents, though no PNC-specific API or compliance angle is stated.  *(targeted: PNC Bank)*
**AI:** Gemini 1.5 via Google Vertex AI with prompt templates that output Jira-ready formats; multi-agent loops built on Google ADK ideas, human-in-the-loop with a three-loop cap against drift.
**Architecture:** React/Vite client calls a Node/TypeScript Express API; Vertex AI Gemini generates content; Postgres via Prisma stores data; Jira Cloud REST integration, other drivers described as designed.
**Novelty:** Spans the full product lifecycle including deprecation and a continuous operate loop, with Jira and ADO parity as a stated goal; most integrations are future work.
**Scope:** medium · working: Jira integration and Gemini generation described with env setup; no live demo or video; analytics are a mock CSV. · polish: Long structured README with roadmap, API reference and FAQ; Devpost has no demo video.
**Claims:** End-to-end flow from messy notes to Jira/ADO-ready stories | Priority and dependency intelligence in planning | Tight 2-minute demo
**Gaps:** Official PNC challenge text not public; Screenshot count unknown; Two project ids in the dataset point to the same Devpost page
Sources: https://devpost.com/software/produh, https://github.com/christinaduthie/produh

---

### ProDuh! - The "duh" way to ship smarter
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
> Same Devpost page as `hackutd-2025-produh` (duplicate listing).
**Prizes:** PNC Bank

**What it is:** A multi-agent LLM command center for product managers covering discovery through deprecation. It turns goals and KPIs into Jira or Azure DevOps ready stories, keeps Confluence pages linked, and runs an operate loop that proposes backlog changes, with a human approving.
**Problem / user:** Product managers losing hours to copy-paste between Jira/ADO, Confluence and chat, with strategy and KPIs not reaching stories.

**Features**
- Strategy-to-stories — Generates briefs, KPIs and roadmap, then epics/stories/subtasks with acceptance criteria and QA checklist ready for Jira/ADO. *[claimed]*
- Jira enhancements — RICE/WSJF prioritization hints, dependency detection, sprint goal drafting, definition-of-done checklists, risk radar. *[claimed]*
- Operate loop — Agent monitors signals from a mock analytics CSV, opens bugs/incidents and proposes backlog deltas, capped at three loops. *[claimed]*
- App-agnostic adapters — Universal layer meant to work with Jira or ADO plus Confluence, MS Graph, ServiceNow and read-only GitHub. *[claimed]*
- Docs auto-linking — Creates and updates Confluence pages, keeps one canonical page per phase, and a My Notes area for links. *[claimed]*
- Portfolio view — Manage multiple products with per-product tabs across lifecycle phases. *[claimed]*

**Flow:** Paste messy discovery notes or goals → System structures them into KPIs and a roadmap → Generate backlog items shaped as Jira/ADO stories → Review, accept, edit or regenerate each draft → Operate loop feeds mock analytics back into backlog suggestions

**Prompt:** PNC Bank sponsor track at HackUTD 2025, framed (per the project pages) as reimagining the life of a product manager with generative AI; the official challenge text was only in the private hackerpack.
**Fit (implied):** Page lists a PNC Bank win; the tool addresses product-manager workload across the whole lifecycle with agents, though no PNC-specific API or compliance angle is stated.  *(targeted: PNC Bank)*
**AI:** Gemini 1.5 via Google Vertex AI with prompt templates that output Jira-ready formats; multi-agent loops built on Google ADK ideas, human-in-the-loop with a three-loop cap against drift.
**Architecture:** React/Vite client calls a Node/TypeScript Express API; Vertex AI Gemini generates content; Postgres via Prisma stores data; Jira Cloud REST integration, other drivers described as designed.
**Novelty:** Spans the full product lifecycle including deprecation and a continuous operate loop, with Jira and ADO parity as a stated goal; most integrations are future work.
**Scope:** medium · working: Jira integration and Gemini generation described with env setup; no live demo or video; analytics are a mock CSV. · polish: Long structured README with roadmap, API reference and FAQ; Devpost has no demo video.
**Claims:** End-to-end flow from messy notes to Jira/ADO-ready stories | Priority and dependency intelligence in planning | Tight 2-minute demo
**Gaps:** Official PNC challenge text not public; Screenshot count unknown; Two project ids in the dataset point to the same Devpost page
Sources: https://devpost.com/software/produh, https://github.com/christinaduthie/produh

---

### qAPIbara
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** StateFarm

**What it is:** An API regression tool that compares two versions of an API, flags structural and semantic differences, has Nemotron generate and run test cases, and has Gemini explain regressions and suggest fixes. Results appear in a dashboard with heatmaps and health scores.
**Problem / user:** QA engineers, DevOps and backend developers who manually diff JSON and write tests when API versions change.

**Features**
- Version diff engine — Calls mock v1 and v2 endpoints and diffs JSON responses, aiming to ignore noise like timestamps and IDs. *[shown_working]*
- Request builder and side-by-side compare — Postman-like builder with JSON import and visual diff of v1 vs v2 responses. *[claimed]*
- Nemotron test generation — Designs test cases from a service description, runs them in bulk, exports to JSON. *[claimed]*
- Gemini explanations — Plain-English regression summaries, fix suggestions with confidence scores, and a chat interface. *[claimed]*
- Health dashboards — Regression heatmap, endpoint map, trend chart and service health score. *[claimed]*
- Auth0 access and audit — Role-based access and audit logging for multi-user use. *[claimed]*

**Flow:** Enter or import two API versions → Run automated diff → Review visual JSON diff and AI summary → Generate and execute test cases, export them → Open dashboards for health and trends

**Prompt:** State Farm sponsor track at HackUTD 2025; challenge text was in the private hackerpack. README describes the core requirement as comparing two API versions and detecting regressions.
**Fit (explicit):** README labels a Layer 0 core requirement for State Farm (two mock APIs, diff engine, regression summary) and builds AI, predictive and security layers on top; says it placed 2nd in the State Farm track.  *(targeted: StateFarm)*
**Sponsor tools:** NVIDIA Nemotron (Workflow planning and test-case generation, core); Auth0 (Authentication and audit logging, supporting); Vultr (Backend deployment target, supporting)
**AI:** Nemotron plans comparison workflows and designs test cases; Gemini turns diffs into plain-language explanations, fix suggestions and chat answers.
**Architecture:** React/Vite frontend with diff viewer and charts; FastAPI backend with mock v1/v2 routers, diff engine and AI router; Firestore storage; Auth0 for login; deployed on Vultr.
**Novelty:** Pairs deterministic JSON diffing with LLM-generated test suites and a heatmap-style health view, layered into four stated tiers.
**Scope:** medium · working: README with full setup and feature checklist marked complete; three screenshots; no demo video. · polish: Dark neon UI with Framer Motion and multiple dashboard components.
**Claims:** Up to 80% faster regression diagnosis | Test generation in under 1 minute | Built in under 24 hours | 25,000+ QA engineers as potential users
**Gaps:** Official State Farm challenge text not public; Percent claims unmeasured
Sources: https://devpost.com/software/in-progress-2awbie, https://github.com/nathanhanxp/qAPIbara, https://hackutd-2025.devpost.com/

---

### Relay
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best Use of ElevenLabs by MLH

**What it is:** An assistant for data center technicians that turns a plain-language request into a verification plan, runs allowed read-only SSH checks on a server, and streams validated results. The repo also holds a Jira chat agent and an OpenCV AprilTag AR overlay showing server health.
**Problem / user:** Data center technicians who lose time typing tests on a laptop and waiting for an engineer to review.

**Features**
- Natural-language test building — POST a prompt and target host; a LangGraph deep agent writes a todo list and verification plan. *[claimed]*
- SSH verification engine — Compiles plan via a YAML catalog of allowed read-only actions, runs over asyncssh, parses and validates output. *[claimed]*
- Streaming results — Writes events to a database and exposes REST and SSE endpoints for tests and results. *[claimed]*
- Jira chat companion — LangChain plus Claude agent with Flask API for conversational ticket workflows. *[claimed]*
- AR server overlay — OpenCV and AprilTags project live server health onto a tag on the hardware. *[claimed]*

**Flow:** Technician describes a check (e.g. verify memory health) → Agent builds todos and a verification plan → Guardrails validate and plan runs over SSH → Output is parsed, streamed and a verdict stored → Optionally view status via AR tag or Jira chat

**Prompt:** MLH prize for the best use of ElevenLabs at HackUTD 2025; listed prize is one winner receiving wireless earbuds. No detailed rubric on the page.
**Fit (none):** Devpost lists the ElevenLabs prize but its narrative is blank, and the README and evidence never mention ElevenLabs or voice, so the connection is only the award listing.  *(targeted: Best Use of ElevenLabs by MLH)*
**Sponsor tools:** ElevenLabs (Not described in any source read, unclear); NVIDIA (Llama via API) (Agent model in demo scripts, supporting)
**AI:** LangGraph deepagents agent turns natural language into verification plans and calls verifier tools; separate LangChain Claude agent for Jira; NVIDIA-hosted Llama used in scratch scripts.
**Architecture:** Flask API with SQLAlchemy/Postgres; deep agent runner calls the codex_verifier engine (YAML catalog, asyncssh, parsers); SSE streams; separate Jira agent and VisualServer AR module.
**Novelty:** Safety-guarded catalog of read-only SSH actions between the agent and servers, plus an AprilTag AR status overlay in the same repo.
**Scope:** medium · working: README gives curl workflow and standalone runner; no demo or video; Devpost narrative empty. · polish: Detailed repo layout table, but Devpost says sections would not save.
**Gaps:** ElevenLabs usage not found; Devpost narrative blank
Sources: https://devpost.com/software/tbd-v8pqbk, https://github.com/Squidtoon99/hackutd-legend, https://hackutd-2025.devpost.com/

---

### SpendingWithSpendy
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Capital One; Best Design

**What it is:** An iOS React Native app where kids hold an NFC Spendy card tied to in-game currency like Robux or Valorant Points. Each dollar is visualized as a spendy; the child taps the card to authorize purchases while parents review history and reload funds.
**Problem / user:** Young kids and their parents, as digital spending makes money feel less tangible.

**Features**
- NFC card authorization — Child taps a physical Spendy card to authenticate an in-game currency purchase. *[shown_working]*
- Money visualization — Main screen shows balance with each dollar as a 'spendy' with mascot. *[shown_working]*
- Store screen — Purchase options for Robux and Valorant Points. *[shown_working]*
- Parent controls — Parent views purchase history and reloads the card. *[shown_working]*

**Flow:** Child sees balance on main screen → Browses store and picks Robux or Valorant Points → Taps NFC card to authenticate → Parent reviews history and reloads card

**Prompt:** Capital One sponsor prize at HackUTD 2025 (one winner, $300 gift card); the README calls it Capital One's Best Financial Hack. Best Design is a separate award for one winner.
**Fit (explicit):** A kid-focused banking app teaching spending habits fits a financial-hack prize; design was highlighted in the README and a Figma file is linked.  *(targeted: Capital One, Best Design)*
**AI:** none
**Architecture:** Expo React Native iOS app styled with Tailwind, reading an NFC card; Figma design; no backend described in sources read.
**Novelty:** Pairs a physical NFC card with online game purchases as a teaching device for kids; no AI.
**Scope:** small · working: README says NFC reading and parental controls work; no video link on Devpost page (README has a short link). · polish: Won Best Design; Figma file and slide deck referenced.
**Claims:** Won two prizes among 1,154 hackers and 367 projects | Working NFC and parental controls in 24 hours
**Gaps:** Capital One challenge text not public; How purchases settle is unexplained
Sources: https://devpost.com/software/spendingwithspendy, https://github.com/brendanshen24/SpendWithSpendy, https://hackutd-2025.devpost.com/

---

### Stamped
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Goldman Sachs

**What it is:** A web onboarding platform for banks that follows a client from lead prospecting through full onboarding. It has separate client, vendor and employee roles, plus a sales pipeline, risk assessment and client list views, with Supabase login.
**Problem / user:** Financial institutions with slow, manual client and vendor onboarding.

**Features**
- Lead-to-onboarding lifecycle — Tracks a client from prospect through completed onboarding. *[claimed]*
- Multi-role workflows — Clients, vendors and employees get separate interconnected views. *[claimed]*
- Sales pipeline view — Employee-facing pipeline screen shown in screenshots. *[shown_working]*
- Risk assessment view — Screen for assessing client risk, shown in screenshots; scoring method not described. *[unclear]*
- Auth and landing page — Supabase authentication, login screen and a public landing page. *[shown_working]*
- Compliance and AI features — Described only generically as comprehensive compliance tools and AI-powered features. *[claimed]*

**Flow:** Visit landing page and log in → Role-specific dashboard loads → Employee views sales pipeline and client list → Open risk assessment for a client → Client or vendor completes onboarding steps

**Prompt:** Goldman Sachs sponsor track at HackUTD 2025 (three winners); challenge text was in the private hackerpack.
**Fit (implied):** Page does not cite the challenge; the bank client and vendor onboarding theme with compliance and risk views suggests the fit.  *(targeted: Goldman Sachs)*
**AI:** Page mentions AI-powered features but names no model or use.
**Architecture:** Next.js 14 and TypeScript frontend with custom component library; Supabase for auth and database; deployed on Netlify.
**Novelty:** Covers both client and vendor onboarding in one multi-role app; scope appears UI-centric.
**Scope:** small · working: Live Netlify demo and YouTube video linked; no repo. · polish: Has landing page and multiple screenshots.
**Gaps:** No repo; AI features unspecified; Challenge text not public
Sources: https://devpost.com/software/stamped-6hnl4w, https://hackutd-2025.devpost.com/

---

### TaskFlow
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Northmark Compute & Cloud

**What it is:** A datacenter work coordination suite: a mobile web app where technicians see tickets, checklists and a planned path, an engineer dashboard showing technician locations and progress, and an iOS AR app where a remote person places a pointer on a server for the on-site technician.
**Problem / user:** Datacenter engineers and on-site technicians, to shorten the gap between a ticket being filed and completed.

**Features**
- Technician mobile web app — Ticket view, per-task checklist, chat with engineer and updated path planning. *[shown_working]*
- Engineer dashboard — Shows where technicians are working and their progress. *[shown_working]*
- AR remote pointer — SwiftUI/RealityKit iOS app lets a remote worker place a pointer on a server model for the technician. *[shown_working]*
- Current-item highlight — Highlights the server item to change. *[claimed]*
- Jira tracking — Tickets can be tracked on a Jira board. *[claimed]*

**Flow:** Engineer watches technician locations on dashboard → Technician opens ticket, follows path and checklist → Technician and engineer chat → Remote worker places AR pointer on a server → Progress appears on dashboard and Jira

**Prompt:** Northmark Compute & Cloud track at HackUTD 2025 (three winners picking prizes in placement order); challenge text was in the private hackerpack.
**Fit (implied):** Directly targets datacenter technician coordination, which the Devpost frames around a real-time view of datacenter workers.  *(targeted: Northmark Compute & Cloud)*
**AI:** none
**Architecture:** Next.js and Supabase web app plus engineer dashboard; separate iOS app in SwiftUI/RealityKit with USDZ models; Jira board for tickets.
**Novelty:** Combines web ticketing, dashboard and a native AR remote-pointing app in one datacenter workflow; no AI.
**Scope:** medium · working: Two repos (web ~91 files, iOS); screenshots; team says iOS app working; AR app polling is still manual. · polish: Web README is the unmodified Supabase starter template; no video.
**Gaps:** README is a starter template; iOS repo not read; Challenge text not public
Sources: https://devpost.com/software/d-68uye4, https://github.com/NEjim2001/hackutd-2025, https://hackutd-2025.devpost.com/

---

### Toyotron
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Toyota Financial Services; Nvidia

**What it is:** A Toyota car-shopping assistant. After a five-step preference quiz it recommends vehicles, answers questions by chat or a simulated/Retell phone call, estimates trade-in, books test drives with Google Calendar, and emails confirmations and recommendations.
**Problem / user:** Car shoppers who hesitate for lack of confidence, time or knowledge.

**Features**
- Preference quiz — Five steps on budget, vehicle type, passengers, use and fuel priorities, stored in Supabase. *[shown_working]*
- Multi-agent chat — Intent, Vehicle, Finance and Report agents on Nemotron answer vehicle questions and compute financing. *[shown_working]*
- Voice and phone — Browser speech in/out and a Retell phone agent number. *[claimed]*
- Trade-in analysis — Estimates trade-in value for the shopper's current car. *[shown_working]*
- Test-drive booking — Books appointments, syncs Google Calendar, sends emails via Resend. *[shown_working]*
- Shared session — Keeps context across chat, call and forms; recovers when preferences change. *[claimed]*

**Flow:** Land on home page, take the quiz → See recommendations → Run trade-in analysis → Chat or call the AI with questions → Book a test drive → Receive confirmation and recommendation emails

**Prompt:** Toyota Financial Services and Nvidia sponsor tracks at HackUTD 2025; challenge text was in the private hackerpack. Nvidia prizes were GPUs and Brev credits.
**Fit (implied):** Builds a Toyota-only buying concierge with finance calculation, using Nemotron for the multi-agent reasoning; README says 2x first place winner.  *(targeted: Toyota Financial Services, Nvidia)*
**Sponsor tools:** NVIDIA Nemotron (Nemotron super 49B via OpenRouter powering the agents, core); Retell (Voice agent phone integration, supporting)
**AI:** Nemotron-super-49B via OpenRouter in a four-agent orchestration (intent, vehicle, finance, report) with tool calls for search, email, calendar and trade-in.
**Architecture:** Next.js 16 / React 19 frontend with API routes orchestrating agents; Supabase for auth and data; Resend email, Google Calendar, Retell voice; deployed on Vercel.
**Novelty:** Offers a simulated phone-call interface alongside chat and cites a prior HackUTD winner as inspiration; large repo for a hackathon.
**Scope:** large · working: Live Vercel demo, about 19k lines in 160 files, README feature docs. · polish: Toyota-branded UI, seven screenshots incl. emails and diagram; no video link.
**Claims:** 2x first place winner at HackUTD 2025
**Gaps:** Challenge text not public; Dealership data source unclear
Sources: https://devpost.com/software/toyotron, https://github.com/anbguye/hackutd-Toyota-Toyotron, https://hackutd-2025.devpost.com/

---

### TrustEstate AI
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** CBRE

**What it is:** A property browsing app on a Google Maps interface where a Gemini assistant cross-checks listing data against live Google Search and assigns each property a trust score with a verification log. Includes favorites, compare, filters and analytics views.
**Problem / user:** Home buyers and renters who cannot tell whether listing data is accurate or current.

**Features**
- Map-based browsing — Google Maps view of properties with profiles, photos and past sales. *[shown_working]*
- Trust score — Gemini compares internal data to outside sources and rates confidence with visual meters. *[claimed]*
- AI fact-check — Gemini tool-calls Google Search to verify facts in real time. *[claimed]*
- Property Q&A and summaries — Assistant answers questions and summarizes histories. *[claimed]*
- Save and compare — Favorites and compare view stored in localStorage; filters and analytics charts. *[shown_working]*

**Flow:** Open map and pick a property → Read profile and trust score → Open verification details → Ask the assistant or request a fact check → Save and compare properties

**Prompt:** CBRE sponsor track at HackUTD 2025 (three gift-card winners); challenge text was in the private hackerpack.
**Fit (explicit):** Page says it won the CBRE track and builds profiles modeled on CBRE-style property data, which was private so mock data was used.  *(targeted: CBRE)*
**Sponsor tools:** Google Gemini and Maps (Fact-checking with search grounding and map UI, core)
**AI:** Gemini reads property records and uses search tool calls to verify them, then outputs a trust score and explanation.
**Architecture:** React/TypeScript/Vite SPA with Tailwind, shadcn, Recharts; Google Maps; Gemini; properties.json simulated data; localStorage only, no backend.
**Novelty:** Frames AI as a verifier of listing data rather than a recommender.
**Scope:** small · working: Video and screenshots of multiple views; no repo or live link. · polish: Rich UI with charts and verification logs.
**Gaps:** No repo; Challenge text not public
Sources: https://devpost.com/software/cbre-project, https://hackutd-2025.devpost.com/

---

### TrustIssues.AI
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Goldman Sachs

**What it is:** A four-agent system (coordinator, extractor, verifier, risk analyst) that reads a vendor's PDF, screens it against mock registry and sanctions data, computes a rules-based risk score, explains it in plain language, and waits for a human manager to approve access.
**Problem / user:** Compliance teams doing slow, subjective vendor onboarding.

**Features**
- PDF extraction — Pulls company data from vendor PDFs with PyPDF2 and regex. *[claimed]*
- Sanctions and registry check — Fuzzy-matches against mock sanctions and registry APIs. *[claimed]*
- Deterministic risk score — Python rules compute score; the LLM only explains it. *[claimed]*
- Access recommendation — Suggests access level such as standard or reject. *[claimed]*
- Human approval and audit — Manager reviews JSON audit trail of agent thoughts and tool calls before access. *[shown_working]*
- Web screens — Streamlit login, vendor and admin dashboards, upload and pending approvals. *[shown_working]*

**Flow:** Log in → Upload vendor PDF → Agents extract, verify, score → Read explanation and recommendation → Manager approves or rejects

**Prompt:** Goldman Sachs sponsor track at HackUTD 2025; challenge text was in the private hackerpack.
**Fit (implied):** Automates vendor/client onboarding with compliance screening and human sign-off, matching the finance-onboarding theme; not explicitly tied to the prompt.  *(targeted: Goldman Sachs)*
**Sponsor tools:** NVIDIA Nemotron (Agent reasoning and function calling, core)
**AI:** ReAct-style agents on Nemotron (49B/70B per sources) via OpenAI SDK function calling; LLM reasons and explains, scoring stays deterministic.
**Architecture:** Streamlit UI over a coordinator agent delegating to extractor, verifier and risk agents; tools for PDF parsing, FuzzyWuzzy sanctions, rules engine; mock registries; JSON audit log.
**Novelty:** Deliberately keeps risk scoring out of the LLM and logs every agent step.
**Scope:** medium · working: Video and eight screenshots; ~7k lines; mock APIs only. · polish: Detailed README with architecture diagram.
**Claims:** Manual onboarding can take up to six months
**Gaps:** Challenge text not public; Model size differs between sources
Sources: https://devpost.com/software/coffee-overflow, https://github.com/ybavgito/TrustIssues.AI, https://hackutd-2025.devpost.com/

---

### UpGuardian
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** StateFarm

**What it is:** A developer service for upgrading to new API versions: it deterministically diffs old and new response formats, and a Nemotron agent helps interpret the changes and build a set of known changes. A Flutter dashboard configures endpoints and shows test results.
**Problem / user:** Application developers migrating to a new API version who must compare responses by hand.

**Features**
- Deterministic diffing — Detects differences between old and new API response formats. *[claimed]*
- Agent interpretation — Nemotron agent explains diffs and builds known-change set. *[claimed]*
- Dashboard — Flutter UI to configure endpoints and view test results, GitHub/IntelliJ-styled. *[shown_working]*
- Request log upload — Upload known request logs to inform which APIs are used. *[claimed]*
- Token-safe proxying — Service mediates API calls so tokens are not exposed to the dashboard. *[claimed]*

**Flow:** Configure endpoints in dashboard → Upload known request logs → Run tests across versions → Review diffs and AI interpretation

**Prompt:** State Farm sponsor track at HackUTD 2025; challenge text was in the private hackerpack.
**Fit (implied):** Detects breaking changes across API versions; page does not cite the prompt.  *(targeted: StateFarm)*
**Sponsor tools:** NVIDIA Nemotron (Agent interpreting response changes, core)
**AI:** Nemotron agent interprets deterministic diff output and curates known changes.
**Architecture:** Flutter dashboard, FastAPI Python service proxying API calls, SQLite behind a modular database layer.
**Novelty:** Keeps detection deterministic and uses the LLM only for interpretation; auth/isolation groundwork unfinished.
**Scope:** small · working: Repo with tests (~2.8k lines); screenshots only, no demo. · polish: README minimal; UI mimics GitHub style.
**Gaps:** README nearly empty; Challenge text not public
Sources: https://devpost.com/software/upguard, https://github.com/Arian04/UpGuardian, https://hackutd-2025.devpost.com/

---

### VisionScout
*HackUTD HackUTD 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Hardware

**What it is:** Smart glasses record short videos of a car or property; a locally trained YOLO model detects damage and features and produces a structured listing with a condition score. A React app lets buyers browse listings and chat with an agent that matches natural-language wishes to listings.
**Problem / user:** Home and car buyers who cannot tell the real condition from hand-written listings.

**Features**
- Property mode — Detects wall damage, appliances, flooring and room size from video, outputs condition confidence. *[claimed]*
- Car mode — Detects dents, scratches, tire wear, windshield damage and make/model with lighting normalization. *[claimed]*
- Auto-built listings — Turns detections into a structured listing. *[claimed]*
- Chat recommender — LangGraph agent on Gemini 2.5 Pro matches requests using weighted similarity over Zillow and scraped Cars.com data. *[shown_working]*
- Browse UI — Toggle car/property, filters, sort, condition scores. *[shown_working]*

**Flow:** Record video with glasses → Detection builds a listing and score → Browse and filter listings → Describe wishes in chat → Receive ranked matches

**Prompt:** Best Hardware award at HackUTD 2025: one winner receiving an ELEGOO UNO starter kit; no rubric text on the page.
**Fit (implied):** Uses event-provided smart glasses (with recalibrated antennas and patched SDK) as the capture device feeding a vision pipeline.  *(targeted: Best Hardware)*
**Sponsor tools:** Smart glasses hardware (event-provided) (Video capture, core)
**AI:** Custom YOLO detection model trained locally; Gemini 2.5 Pro with LangGraph for intent and ranking via a merge-score of trust, value, relevance.
**Architecture:** Glasses (Python/Flask) feed YOLO detection; Flask REST backend; React/TypeScript/Tailwind frontend; Zillow API and Selenium/BS4 scraped Cars.com data.
**Novelty:** Turns wearable video into listings with condition scores across two asset types.
**Scope:** medium · working: ~9.5k lines, tests present; Devpost claims working end-to-end; no video. · polish: Five screenshots incl. light mode; hardware README sparse.
**Claims:** Working end-to-end demo from vision to recommendations
**Gaps:** No accuracy figures; Sponsor API keys never arrived
Sources: https://devpost.com/software/coolproject69, https://github.com/ClosetCoderSad/VisionScout, https://hackutd-2025.devpost.com/

---

### WiSPR - Wireless Safety Pulse Relay
*HackUTD HackUTD 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Beginner

**What it is:** A wearable Arduino badge with a DHT11 sensor, LCD, LEDs, buzzer and vibration that warns of heat or humidity hazards. Two badges signal each other with short/long button presses, and a React ticket dashboard simulates alerts.
**Problem / user:** Technicians in loud, hazardous workplaces who cannot talk or notice danger.

**Features**
- Hazard detection — DHT11 readings trigger vibration, LED and LCD warnings. *[shown_working]*
- Silent team signals — Short press asks help, long press signals hazard, sent between two Arduinos over TX/RX. *[shown_working]*
- Status display — LCD shows temperature, humidity and state. *[shown_working]*
- Web dashboard — React page with Safe/Warning/Emergency modes, alerts and tickets using simulated data. *[shown_working]*

**Flow:** Wear badge → Hazard triggers local alert → Press button to signal teammate → Teammate badge shows pattern → Dashboard shows and resolves ticket

**Prompt:** Best Beginner award at HackUTD 2025: one winner receiving an Anker power bank.
**Fit (explicit):** Page says most team members were beginners who took hardware, firmware, CAD and web UI to a working prototype.  *(targeted: Best Beginner)*
**AI:** none
**Architecture:** Two breadboard Arduinos with C++ firmware linked over serial; AutoCAD badge model; React dashboard from Figma with simulated sensor data.
**Novelty:** Silent vibration-pattern messaging between badges rather than a screen app; dashboard not tied to real sensor data.
**Scope:** small · working: Video of prototype; repo; dashboard uses simulated data. · polish: AutoCAD model, Figma prototype.
**Claims:** Emergency mode at 30C or 70% humidity
**Gaps:** README not read in detail
Sources: https://devpost.com/software/wispr-wireless-safety-pulse-relay, https://github.com/ParisUNgo/HackUTD-WiSPR, https://hackutd-2025.devpost.com/

---

### Working Memory
*HackUTD HackUTD 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner General Track

**What it is:** A tool that tracks files changed during a coding session in VS Code, then sends the changelog and git status to an LLM to write a summary of what was done. Past sessions are searchable in a web dashboard, so a developer can recover context.
**Problem / user:** Students and developers who juggle several projects and lose the reasoning behind their work.

**Features**
- Session tracking — Start/stop a session in the dashboard; modified and new files are logged. *[shown_working]*
- AI summary — GPT-4.1-mini writes an overview with actionable insights plus git status metadata. *[shown_working]*
- Past workflows — History in list and calendar views. *[shown_working]*
- Vector search — Search past sessions semantically. *[shown_working]*
- MCP project path — VS Code extension MCP server exposes active project path. *[shown_working]*
- Empty-output fallback — Validates LLM content, not just status codes. *[claimed]*

**Flow:** Start session in dashboard → Code as usual → Stop session → Changelog is summarized → Search history later

**Prompt:** General Track at HackUTD 2025: three winners (Mac M4, iPad Air, keyboard); README calls it 1st place grand prize.
**Fit (explicit):** Open general track, no theme; README claims 1st place.  *(targeted: General Track)*
**AI:** GPT-4.1-mini via OpenRouter and OpenAI Agents SDK summarizes changelogs with large context window; embeddings-based search.
**Architecture:** React/Tailwind dashboard; Python FastAPI agent using GitPython; TypeScript VS Code extension MCP server; OpenRouter LLM.
**Novelty:** Uses MCP in a VS Code extension to pass project context to the agent; website at workingmemory.vip.
**Scope:** medium · working: Live website, repo with tests; no video. · polish: Glassmorphism UI; README with architecture.
**Claims:** 1st place grand prize at HackUTD 2025
**Gaps:** Repo size inflated by deps
Sources: https://devpost.com/software/working-memory, https://github.com/Mihirz/HackUTDProject, https://hackutd-2025.devpost.com/

---

