# HackUTD — HackUTD 2025 (100 projects)

### Adjacent
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** An AI project manager that turns meeting recordings, transcripts and documents into extracted tasks, dependencies and risks, assigns owners, and shows them on an editable Kanban board backed by Supabase.
**Problem / user:** Teams whose decisions, dependencies and follow-ups get lost in meetings and documents outside normal project tools.

**Features**
- Multi-source ingest — Zoom/Meet connection or uploads of recordings, transcripts, PDFs and slide decks *[claimed]*
- Transcription — Whisper converts audio and video into transcripts *[claimed]*
- Task extraction — Nemotron agents pull tasks, dependencies and risks from text *[claimed]*
- Assignee, priority and deadline suggestions — Matches tasks to people using workload and availability signals *[claimed]*
- Kanban board — Editable board with real-time tracking, data in Supabase *[claimed]*
- Landing page — README covers a dark animated Next.js landing page with tracks, agents and vision sections *[shown_working]*
- Chat-based edits — Interactive chatbot for board changes *[planned]*

**Flow:** Upload content or connect Zoom/Meet → Whisper transcribes → Agents extract tasks, risks and owners → Review and edit tasks on Kanban board

**Prompt:** not public / not found
**Fit (implied):** Landing page lists PNC, NVIDIA and Startup tracks; NVIDIA public text is prizes only, so alignment is inferred from Nemotron use.  *(targeted: HackUTD 2025 (Lost in the Pages); NVIDIA Nemotron tools used)*
**Sponsor tools:** NVIDIA Nemotron (Agents that extract and assign tasks, core); Supabase (Database, auth, storage and real-time task sync, supporting)
**AI:** Whisper for speech; NVIDIA Nemotron agents (a three-agent network per landing page) extract tasks, dependencies, risks and suggest owners; no fine-tuning mentioned.
**Architecture:** Next.js 14 front end with Supabase; Flask backend for media handling and agent orchestration; Zoom and Meet integrations.
**Novelty:** Agent network that links meeting content to a project board with workload-aware assignment; README itself documents mainly the landing page.
**Scope:** medium · working: Repo about 10k lines with Next.js app, Supabase migrations and Flask folder; Devpost calls it a prototype; video linked. · polish: Animated dark landing page, CI workflow present; README describes marketing site not product.
**Claims:** Functioning prototype handling multi-format inputs | Agents autonomously propose and assign tasks
**Gaps:** README documents the landing page, not the agent pipeline; video not viewable; no prize shown
Sources: https://devpost.com/software/adjacent-3inhew, evidence/hackutd-hackutd-2025-adjacent.json (README), prompts_cache/hackutd-2025.md

---

### Aether
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence low*

**What it is:** An iOS app that takes voice requests (schedule a meeting, summarize a document, generate a report) and has a connected computer carry them out, relaying commands through Firebase.
**Problem / user:** People who switch between devices and want hands-free productivity from a phone.

**Features**
- Voice control from phone — Swift iOS app captures spoken requests *[claimed]*
- Phone-to-computer relay — Firebase real-time channel carries commands to a Python agent on the computer *[claimed]*
- Task execution — Scheduling meetings, summarizing text, generating reports *[claimed]*

**Flow:** Speak a request into the iOS app → Firebase delivers command to the computer → Computer performs the task

**Prompt:** not public / not found
**Fit (none):** Page lists Nemotron but does not say how it is used or which track was entered.  *(targeted: HackUTD 2025 (Lost in the Pages); Nemotron tag present)*
**Sponsor tools:** NVIDIA Nemotron (Listed in built-with tags; role not explained, unclear)
**AI:** Nemotron listed in tags; page does not describe model use.
**Architecture:** Swift mobile client, Firebase as message bus, Python process on the computer executing commands.
**Novelty:** Remote voice-to-computer control concept; page detail is thin.
**Scope:** small · working: Devpost claims a working real-time backend; no demo, video or readable repo. · polish: Claims a polished front end; none verified.
**Claims:** Beautiful user-friendly front end | Working back end for real-time voice-command execution
**Gaps:** repo clone failed and GitHub/raw fetches errored; no video or demo; Nemotron role unexplained
Sources: https://devpost.com/software/aether-cqgmxy

---

### Aethernet
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A React and Mapbox dashboard for the HackUTD potion-factory data challenge: it shows cauldron levels live on a map, replays past periods, and matches date-only transport tickets to timestamped drain events to flag suspicious or unlogged drains.
**Problem / user:** Factory managers and investigators who must reconcile potion transport tickets with actual cauldron drains in an EOG-style monitoring scenario.

**Features**
- Cauldron network map — Mapbox map shows each cauldron's location and level with the market *[claimed]*
- Historical replay — Time-travel through minute-level level data *[claimed]*
- Ticket matching — Compares ticket volumes with drain events, adjusting for level change and fill during drains *[claimed]*
- Discrepancy flagging — Marks suspicious tickets and possible unlogged drains *[claimed]*
- Resilient data handling — Retries and buffering for delayed or incomplete API responses; adapts as tickets change *[claimed]*
- Courier route optimization — Bonus in the challenge brief; Devpost does not claim it *[unclear]*

**Flow:** Open dashboard → See cauldron states on the map → Replay a past period → Review flagged tickets and suspected unlogged drains

**Prompt:** Challenge asks for a real-time dashboard over cauldron level data and transport tickets that visualizes the network, replays history, matches tickets to drains despite changing data, flags discrepancies, with bonus minimum-witch route scheduling.
**Fit (explicit):** README quotes the brief and Devpost describes the map, replay and matching deliverables; the bonus routing is not claimed.  *(targeted: HackUTD 2025 EOG data challenge (Lost in the Pages theme))*
**Sponsor tools:** EOG potion API (Cauldron level and ticket data feeds, core); Mapbox (Map visualization, supporting)
**AI:** none
**Architecture:** React frontend with Mapbox; backend folder polls the challenge API for levels and tickets and applies custom matching logic; data buffered with retries.
**Novelty:** Pure algorithmic reconciliation (no ML) with replay; ML only listed as future work.
**Scope:** small · working: Repo about 2.9k lines split into frontend and backend; no demo or video. · polish: README mostly repeats the challenge brief; no screenshots described.
**Claims:** Handles ticket data changing during judging
**Gaps:** README is challenge brief, not own docs; no prize shown
Sources: https://devpost.com/software/aethernet, evidence/hackutd-hackutd-2025-aethernet.json (README), prompts_cache/hackutd-2025.md

---

### AutoDoc
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A tool that clones a Git repository, builds a function-dependency graph, uses an NVIDIA Nemotron model through LangChain to write documentation, and serves it as a Docusaurus site in its own Docker container at an NGINX-assigned URL.
**Problem / user:** Developers who dislike writing documentation and want it generated and hosted automatically.

**Features**
- Repo ingest — Shallow clone (depth 1) then tree-sitter scan of code grammar *[claimed]*
- LLM documentation — Nemotron (70B, 64k context) via LangChain writes docs from a function-dependency graph to cut tokens *[claimed]*
- Per-repo doc servers — Each Docusaurus site runs in its own Docker container *[claimed]*
- Automatic URLs — NGINX assigns a unique domain per documentation server *[claimed]*
- Web UI — Homepage, Repos Explorer and Upload page *[shown_working]*

**Flow:** Submit a repo in the web UI → Backend clones and parses it → Nemotron generates docs → Docusaurus container launches at a unique URL → Open the live docs

**Prompt:** not public / not found
**Fit (implied):** Uses Nemotron as the only model; NVIDIA public text lists prizes only, so fit is inferred.  *(targeted: HackUTD 2025 NVIDIA track (inferred from repo name nvidia-track))*
**Sponsor tools:** NVIDIA Nemotron (Generating documentation text, core)
**AI:** Nemotron 70B on a tuned inference server with 64k context limit, LangChain agent features, and a call-graph built with tree-sitter to compress the prompt; vector DB left as future work.
**Architecture:** Vite/React UI; Flask backends spawn Docusaurus builds in Docker; NGINX routes subdomains; Nemotron inference called with trimmed graph context.
**Novelty:** Combines doc generation with automatic per-repo deployment infrastructure.
**Scope:** medium · working: Live demo URL nvidia.weabonie.com listed; repo about 6.9k lines with Docker and env example. · polish: Three-page UI with screenshots; README is the Vite template.
**Claims:** Fast processing via shallow cloning | Unlimited documentation servers each with a unique URL
**Gaps:** README is Vite boilerplate; live demo not opened; no prize shown
Sources: https://devpost.com/software/nvidia-track, evidence/hackutd-hackutd-2025-autodoc.json (template README only)

---

### AutoMatch
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A one-stop car-buying web app: browse cars or swipe through recommendations, compare weekly gas cost, predict loan approval and trade-in value, chat with a RAG assistant, and have an ElevenLabs voice agent phone a dealership to book a test drive.
**Problem / user:** Car shoppers balancing what they want against what they can afford across search, financing and test drives.

**Features**
- Car catalog and swipe view — Dashboard of 2020-onward models with specs and a dating-app style swipe mode *[claimed]*
- Gas cost comparison — Recharts side-by-side comparison using the user's commute *[claimed]*
- Loan approval predictor — Short quiz feeds a RandomForest model claimed at 97% accuracy *[claimed]*
- Trade-in estimate — MarketCheck API valuation by car and location *[claimed]*
- Voice scheduling agent Alex — ElevenLabs agent places a call to a dealership to book a test drive *[claimed]*
- Autobot assistant — Gemini with RAG over a Chroma vector store of car data *[claimed]*
- Image pipeline — Automatically finds images for new models via SerpAPI *[claimed]*

**Flow:** Browse or swipe cars and like some → Compare liked cars and gas costs → Fill the finance quiz for loan prediction and trade-in → Ask Autobot for suggestions → Have Alex call to schedule a test drive

**Prompt:** not public / not found
**Fit (none):** Page names no prize; car-buying with financing suggests a finance-oriented sponsor track, not stated.  *(targeted: HackUTD 2025 (Lost in the Pages); no sponsor track named)*
**Sponsor tools:** ElevenLabs (Voice agent that phones dealerships, core); Gemini API (Autobot recommendations with RAG, core)
**AI:** Gemini prompted over retrieved car data (Chroma plus Sentence Transformers); RandomForest classifier for loan approval; ElevenLabs conversational voice agent.
**Architecture:** React/TypeScript/Tailwind front end; Flask backend integrating KBB and SerpAPI data, MarketCheck, Chroma vector store, Gemini, ElevenLabs and a scikit-learn loan model.
**Novelty:** Spans search, finance prediction, trade-in and real phone booking in one flow.
**Scope:** large · working: Repo about 13k lines with separate frontend and backend; Devpost lists many integrations but no video. · polish: Detailed README and feature narrative; no tests or demo link.
**Claims:** Loan model 97% accuracy (self-reported) | Alex can start, hold and end a full phone call | Database of real 2020-present models
**Gaps:** README cut at 7000 chars of tail setup; no demo or video; no prize shown
Sources: https://devpost.com/software/tbd-6hwkg4, evidence/hackutd-hackutd-2025-automatch.json (README)

---

### AutoMate
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence low*

**What it is:** A car-shopping assistant that recommends models from budget and driving habits, projects lease or finance payments, and lets users explore vehicle interiors in a 3D viewer, with a WebSocket chat backed by OpenAI RAG over scraped data.
**Problem / user:** Car buyers overwhelmed by choice who want guided selection through financing.

**Features**
- AI recommendations — OpenAI with RAG over a team-scraped car database *[claimed]*
- Financing plans — Lease or finance options with monthly payment projections *[claimed]*
- 3D vehicle explorer — Interactive viewer including interiors *[claimed]*
- Overlay assistant — Guides selection, comparison and financing steps *[claimed]*
- WebSocket chat — Real-time AI conversation *[claimed]*

**Flow:** Enter budget, preferences and credit information → Receive recommended models → Explore vehicles in 3D → Review financing projections → Ask the assistant questions

**Prompt:** not public / not found
**Fit (none):** NVIDIA listed in tags without explanation; no prize named.  *(targeted: HackUTD 2025 (Lost in the Pages); NVIDIA tag, no track stated)*
**Sponsor tools:** NVIDIA (Listed in built-with tags; role not explained, unclear)
**AI:** OpenAI APIs with a retrieval layer over a scraped car database for recommendations and answers.
**Architecture:** React/TypeScript front end, Node backend with WebSocket chat, Python scraping, OpenAI RAG, 3D vehicle viewer.
**Novelty:** Similar domain to AutoMatch but emphasizes 3D interior viewing and lease/finance projections.
**Scope:** small · working: Devpost claims interiors displayed and AI answering from database; repo unreadable, no demo. · polish: Not verifiable.
**Claims:** Interior views of vehicles | AI trained to answer from scraped database
**Gaps:** repo clone failed and raw README fetch errored; NVIDIA role unexplained; no demo or video
Sources: https://devpost.com/software/notthat

---

### Bait & Switch
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence C · confidence low*

**What it is:** A small Godot video game meant to teach players to recognize phishing and financial-scam types through play. Devpost and README give only a one-line purpose.
**Problem / user:** People and organizations exposed to financial scams, for whom scam-prevention training is dull and hard to reach.

**Features**
- Phishing-awareness game — Godot game intended to teach scam types interactively; mechanics not described *[claimed]*

**Flow:** Play the Godot game → Encounter phishing scenarios (details not published)

**Prompt:** not public / not found
**Fit (none):** Fraud-awareness theme could fit a finance sponsor, but the page names none.  *(targeted: HackUTD 2025 (Lost in the Pages); no track named)*
**AI:** none
**Architecture:** Single Godot project folder of scenes and assets; no code files detected by the analysis.
**Novelty:** Game format for scam training; nothing else is documented.
**Scope:** tiny · working: Repo has 53 files in a Godot project folder; no build, demo or video. · polish: Minimal; two-line README and sparse Devpost text.
**Gaps:** no gameplay description; README boilerplate-thin
Sources: https://devpost.com/software/bait-switch, evidence/hackutd-hackutd-2025-bait-switch.json (one-line README)

---

### BankDojo Jr.
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A classroom financial-literacy platform for grades 1-5 where students complete quests to earn coins, split them into Save and Spend jars, shop in a virtual store and compete on a live leaderboard; teachers approve spending. Built with Lovable and Auth0.
**Problem / user:** Young students who learn about money too late, plus teachers and parents guiding them.

**Features**
- Step-by-step quests — Interactive quests teach financial habits and award digital coins *[claimed]*
- Save and Spend jars — Students divide coins between jars *[claimed]*
- Virtual store — Spend coins on items, with teacher approval *[claimed]*
- Leaderboard and class competitions — Real-time rankings tied to progress *[claimed]*
- Teacher tools — Monitor progress, approve spending *[claimed]*
- Social login by role — Auth0 with Google, Apple or Microsoft for students, teachers, parents *[claimed]*

**Flow:** Log in via Auth0 → Complete quests to earn coins → Allocate to Save or Spend jars → Buy from the store → Teacher reviews progress and approvals

**Prompt:** not public / not found
**Fit (none):** Banking-themed education product; no sponsor or prize stated on the page.  *(targeted: HackUTD 2025 (Lost in the Pages); no track named)*
**Sponsor tools:** Auth0 (Social login and roles, supporting)
**AI:** none
**Architecture:** Vite/React/shadcn front end generated via Lovable, small Node server folder, Auth0 login, a database with real-time sync for the leaderboard.
**Novelty:** Targets elementary classrooms with a teacher-approval loop; platform generated mostly through Lovable.
**Scope:** medium · working: Devpost claims working MVP with auth, dashboard and quests; repo about 18k lines; no demo or video. · polish: Lovable-generated UI; README is Lovable template.
**Claims:** Working MVP with authentication, dashboard and multiple quests
**Gaps:** README is template; repo link was not on the Devpost page; queue repo assumed to match; no demo
Sources: https://devpost.com/software/finance-dojo, evidence/hackutd-hackutd-2025-bankdojo-jr.json (Lovable template README)

---

### Beyond Ordinary Browsing
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A product-manager automation tool: a natural-language task launches parallel browser agents that gather data, with Nemotron planning and summarizing, an Excalidraw-style flow diagram, an auto-generated n8n workflow to re-run it, and Google Sheets export.
**Problem / user:** Product managers who repeat research, messaging and data-aggregation tasks.

**Features**
- Prompt-driven research — Natural-language task is planned by Nemotron *[claimed]*
- Parallel browser agents — browser-use sessions gather data simultaneously *[claimed]*
- Flow diagram — Excalidraw-style graph of the process, updated live *[claimed]*
- n8n workflow generation — Creates a re-runnable automation from the task *[claimed]*
- Sheets export — Composio exports tabular results to Google Sheets *[claimed]*
- History and replay — Convex stores sessions and tasks for rerun *[claimed]*

**Flow:** Enter a task prompt → Agents browse in parallel → Nemotron summarizes → View diagram and n8n flow → Export to Sheets or re-run

**Prompt:** not public / not found
**Fit (implied):** Page references the Product Manager challenge and Nemotron use; no public challenge text found.  *(targeted: HackUTD 2025 NVIDIA track / Product Manager challenge (text mention))*
**Sponsor tools:** NVIDIA Nemotron (via OpenRouter) (Planning, reasoning and summarizing, nemotron-super-49b, core)
**AI:** Nemotron super 49B reasons about what to fetch and synthesizes results; browser-use agents do the page work; n8n flows are generated automatically.
**Architecture:** Next.js/shadcn/Excalidraw front end, FastAPI backend, browser-use agents, Convex storage, Clerk auth, Composio for Sheets, n8n for generated automations.
**Novelty:** Chains agentic browsing, live process diagram and automatic automation export.
**Scope:** medium · working: Devpost claims end-to-end system with five screenshots; no repo, demo or video. · polish: Multiple integrations claimed; unverified.
**Claims:** Working end-to-end combination of Nemotron, browser agents, visualization and n8n
**Gaps:** no repo; no demo; track not formally named
Sources: https://devpost.com/software/project-good-ai

---

### BlackJack Practice Simulator
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence low*

**What it is:** A solo-built responsive web page for practicing blackjack, written in plain HTML, CSS and JavaScript with a card-dealing animation, hosted on Netlify.
**Problem / user:** No problem statement; blackjack hobbyists wanting to practice.

**Features**
- Blackjack practice — Browser game of blackjack; rules and options not described *[claimed]*
- Card-dealing animation — Animated dealing, noted as hardest part *[claimed]*
- Responsive layout — Layout holds across screen sizes *[claimed]*

**Flow:** Open bjsimulator.netlify.app → Play practice hands

**Prompt:** not public / not found
**Fit (none):** No sponsor or prize connection stated.  *(targeted: HackUTD 2025 (Lost in the Pages); no track named)*
**AI:** none
**Architecture:** Static front-end site of HTML, CSS and vanilla JavaScript.
**Novelty:** Minimal solo project; first solo build for its creator.
**Scope:** tiny · working: Live Netlify link listed; not opened. · polish: Responsive design claimed; no repo or video.
**Gaps:** no repo; live site not opened; feature list very thin
Sources: https://devpost.com/software/blackjack-practice-simulator

---

### breve
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A solo-built command-line GPU operations agent. The user states a GPU job in plain English; a Nemotron-labelled model drafts a JSON plan, a safety critic revises it, and a simulated run provisions, monitors and tears down the workload.
**Problem / user:** Anyone wanting to train models on GPUs without hand-managing Docker configs, dependency conflicts and idle-cost leaks.

**Features**
- Natural-language objective to plan — Model produces a reasoning trace and a JSON multi-step plan (provision, clone/install, run, monitor, teardown) *[shown_working]*
- Safety critic and patch loop — A second pass reviews the plan and patches unsafe steps; regex and JSON guardrails block destructive commands like rm -rf *[claimed]*
- Cost estimate and runtime cap — Estimates cost before running and enforces time limits and idle teardown *[claimed]*
- Interactive confirmation — User approves the plan in the terminal before execution *[claimed]*
- Rich terminal execution timeline — Animated progress bars and simulated GPU utilization logs *[shown_working]*
- Run report and artifacts — Jinja2-generated structured report with a judging-criteria checklist at the end *[claimed]*
- Extensible tool adapters — Modular tools (create_instance, run_command, monitor) meant to extend to Docker, WandB or other clouds *[claimed]*

**Flow:** State objective in natural language → View model reasoning trace and JSON plan → Safety critic reviews and patches plan → Guardrails applied and cost estimated → Confirm interactively → Watch simulated execution timeline → Read report and artifacts

**Prompt:** not public / not found
**Fit (explicit):** Devpost frames it as an answer to the NVIDIA challenge of AI that takes action rather than only responding: a Nemotron agent that plans and executes GPU workflows with guardrails.  *(targeted: Nvidia track (Nemotron / AI that acts))*
**Sponsor tools:** NVIDIA Nemotron (planning and self-critique of GPU workflows (page also labels the model Llama 3.1 70B Instruct), core); Brev (listed in tags and a 'brev hosting' screenshot; actual GPU orchestration was simulated, unclear)
**AI:** Nemotron via OpenAI-compatible client generates a JSON plan with reasoning, then a critic pass revises it before schema validation and guardrail checks.
**Architecture:** demo.py drives agent/ (planning, validation, guardrails), exec/ (orchestrator, monitor, reporting) and tools/ adapters; Objective -> Plan -> Critic -> validated simulated execution.
**Novelty:** Agentic infra-ops framing with an explicit critic and guardrail loop; execution is simulated locally because no GPU/container environment was available.
**Scope:** tiny · working: Python demo script with simulated execution; about 280 lines in repo; page admits GPU telemetry is simulated. · polish: Rich terminal UI with animations; three screenshots; README is two lines.
**Claims:** Built end to end solo in about 24 hours | Blocks unsafe commands with JSON guardrails and regex filters | No quantitative results reported
**Gaps:** Repo README is a two-line stub, so only Devpost describes features; No video; Execution is simulated; no real GPU run shown
Sources: https://devpost.com/software/prateek-s-project, evidence/hackutd-hackutd-2025-breve.json

---

### Brew View
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A Flask web dashboard for the fictional potion-factory dataset: it maps cauldrons, replays fill levels over time, lists delivery tickets with suspicious ones highlighted, charts trends and computes courier routes.
**Problem / user:** Operations staff of a potion factory who need to prevent cauldron overflow and catch fraudulent courier deliveries.

**Features**
- Interactive cauldron map — Leaflet/OpenStreetMap markers colour-coded by fill level with year/month/day/hour timeline playback *[shown_working]*
- 3D visualization tab — Three.js view of the cauldron network with particle effects and timeline controls *[claimed]*
- Ticket log with suspicious flagging — Filter by date, cauldron, courier and status; suspicious tickets shown in red *[claimed]*
- Fraud detection — Browser-side algorithm comparing cauldron fill trends with delivery records *[claimed]*
- Trend charts — Chart.js per-cauldron history and multi-cauldron comparison *[claimed]*
- Analytics dashboard — Collection efficiency, courier performance and health indicators *[claimed]*
- Route optimization — TSP-style algorithms produce a daily schedule with timing and routes for witches *[claimed]*
- Themes and caching — Light/dark theme persisted; data caching for smoother use *[claimed]*

**Flow:** Open map tab → Pick date and hour, click Show → Inspect overflow warnings → Review ticket logs for suspicious couriers → Check trends and analytics → Generate optimized routes

**Prompt:** EOG Resources 'Lost in the Pages' challenge (second-hand, from winner pages): reconcile potion transport tickets against cauldron drain levels, forecast overflow, and plan witch pickup routes, an oil-flow analogue.
**Fit (implied):** Covers each part of the EOG theme: level monitoring with overflow warnings, ticket-versus-drain fraud flagging, and route/schedule optimization over the provided API data.  *(targeted: EOG Resources challenge (implied; no prize listed))*
**Sponsor tools:** EOG API (cauldron, ticket, market, network endpoints) (source of fill levels, tickets and network data for all views, core)
**AI:** none
**Architecture:** Flask backend proxies and caches the EOG api/* endpoints; a single-page JS front end renders Leaflet map, Three.js, Chart.js and does fraud and routing logic in the browser.
**Novelty:** Adds a 3D Three.js view and hour-level historical playback on top of the standard map, tickets and routing; pixel-art assets are a stylistic touch.
**Scope:** medium · working: About 9.6k LOC Flask app with start.sh and documented tabs; no demo link or video. · polish: Detailed README, theme toggle, animated hint button, four screenshots; no tests.
**Claims:** Fraud detection flags suspicious courier activity | Route optimization yields a daily schedule with precise timing | Drain and flow rates derived per cauldron using 2-sigma distribution methods
**Gaps:** No video or live demo; Fraud-detection thresholds and route-optimizer details not documented; EOG challenge text is not public
Sources: https://devpost.com/software/brew-view, evidence/hackutd-hackutd-2025-brew-view.json

---

### Bridgit
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A web app that estimates a truck or RV's height from a photo using a seven-agent Nemotron pipeline, then plans a route avoiding low bridges and warns the driver by distance as they approach each one.
**Problem / user:** Truck, RV, rental-van drivers and fleet managers who risk bridge strikes because they do not know their exact vehicle height.

**Features**
- Photo height estimate — Vision model measures vehicle height using a license plate as scale and adds AC unit/antenna allowances with confidence scores *[claimed]*
- Seven-agent pipeline — LangGraph chains Vision, Measurement, Location, Bridge Query, Weather, Risk and Recommendation agents over shared state *[claimed]*
- Bridge-aware route planning — Origin, destination and height give risk-graded routes (SAFE to CRITICAL), bridges to avoid and alternatives *[claimed]*
- Live monitoring alerts — Escalating warnings at 5 mi, 1 mi and 500 ft showing clearance and margin *[claimed]*
- Vehicle library — Presets for U-Haul and Penske trucks and RVs with roof-equipment toggles updating height *[claimed]*
- Incident reporting — Crowdsourced near-miss and strike reports to supplement bridge data *[claimed]*
- Weather adjustment — Clearance adjusted for conditions such as snow or flooding *[claimed]*

**Flow:** Upload vehicle photo or pick preset → Watch agent pipeline and read measured height → Enter origin and destination → Review risk-rated route and alternatives → Start route → Receive tiered bridge alerts while driving

**Prompt:** not public / not found
**Fit (implied):** Uses Nemotron-served models for vision and planning inside a multi-agent LangGraph system; no prize is stated on the page.  *(targeted: Nvidia track (Nemotron agents))*
**Sponsor tools:** NVIDIA Nemotron (Llama 3.1 70B Instruct and a VLM via NVIDIA API) (vision analysis, measurement and route planning agents, core)
**AI:** LangGraph orchestrates seven sequential agents; Nemotron models do photo analysis and route reasoning, with OSM, Mapbox and OpenWeather data. Later repo makes the photo estimate the only AI step.
**Architecture:** React/Vite front end, FastAPI backend, LangGraph agent chain calling Overpass (bridges), Mapbox geocoding, OpenWeather and NVIDIA API. Current repo instead uses Valhalla routing plus Overpass.
**Novelty:** Combines photo-based height measurement with bridge clearance data and tiered driving alerts, a safety application uncommon among car-themed entries.
**Scope:** medium · working: Repo has backend and frontend with tests (about 2.5k LOC); Devpost has no demo link or video. · polish: Detailed README, vehicle library, alert tiers, documented API; repo README reflects a later cleaned-up version.
**Claims:** Seven specialised agents in a LangGraph pipeline | Alerts at 5 miles, 1 mile and 500 feet | No accuracy figures reported
**Gaps:** Repo README describes a later version (Valhalla routing, optional photo AI, no AI in fit decision) that conflicts with the Devpost seven-agent description; features follow Devpost; Devpost links no repo or demo; Hackathon-era write-ups are in docs/archive, not read
Sources: https://devpost.com/software/bridgit-xem67c, evidence/hackutd-hackutd-2025-bridgit.json

---

### BudgetBrew
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A fantasy-themed budgeting web app for college students that turns tracking spending into a quest, with a competitive budget score and AI insights. The repo README describes an earlier Flutter app called FinFit.
**Problem / user:** College students who find budgeting apps boring and forget to track their accounts.

**Features**
- Budget tracking — Set monthly limit and track spending against it *[claimed]*
- Competitive budget score — FinScore weights budget adherence, utilization, account age, recent activity and activity mix like a FICO score *[claimed]*
- Quest and brewing metaphor — Saving and spending presented as a fantasy adventure with Poyo guide planned *[claimed]*
- AI recommendations — Gemini/OpenAI listed in tags for insights; use not explained *[unclear]*
- Leaderboards and streaks (README) — Global and team leaderboards, streak counters, financial-literacy quiz in the Flutter README *[claimed]*
- Savings and investment goals (README) — Goal setting with notifications for deviations *[claimed]*
- Mini-games and social challenges — Listed as next steps *[planned]*

**Flow:** Set name, monthly budget and savings goal → View dashboard with score and progress → See recent transactions and streak → Check leaderboard → Take finance quiz (README version)

**Prompt:** not public / not found
**Fit (explicit):** README states it was made for Capital One's best financial hack track: a gamified financial-health tracker with a credit-score-style metric and literacy education.  *(targeted: Capital One: The Best Financial Hack)*
**Sponsor tools:** Firebase / Gemini / OpenAI (non-sponsor) (partial Firebase backend; AI use unexplained, token)
**AI:** Gemini and OpenAI are listed as built-with tags; the page does not say how they are used.
**Architecture:** Devpost: React front end with partial Firebase. README: Flutter app with Firestore, anonymous Auth, Provider state and local notifications.
**Novelty:** Quest-themed gamification plus a credit-score-like FinScore; team pivoted from Flutter mobile to React web mid-event.
**Scope:** small · working: Flutter source (about 5.8k LOC) and a web version described; no demo or video; backend integration admitted as limited. · polish: Five screenshots and a structured README, but plans for real data and mini-games unfinished.
**Claims:** FinScore uses five FICO-like weights (35/30/15/10/10) | No metrics reported
**Gaps:** README describes the abandoned Flutter FinFit version while Devpost describes the React web BudgetBrew; features blend both; Page does not say what the AI does; Hackathon theme text is not public
Sources: https://devpost.com/software/finup, evidence/hackutd-hackutd-2025-budgetbrew.json

---

### BuildYourRide
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A Nuxt web app where a user clicks wheels, headlights or engine on a 3D Toyota, swaps parts from a carousel with animations, and is then matched to the real Toyota model closest to the build.
**Problem / user:** Toyota shoppers who find spec sheets dull and want a more visual, playful way to explore options.

**Features**
- Interactive 3D configurator — Blender-made models rendered with TresJS; clicking a part opens a carousel of options *[shown_working]*
- Animated part swaps — Selections update the model in real time; picking an engine lifts it out of the hood *[shown_working]*
- Exterior and interior views — Page lists both views of the configured car *[claimed]*
- Build-to-model recommendation — Matches the chosen configuration to the closest real Toyota and shows specs *[claimed]*
- Needs-based filtering — Screenshot caption mentions filtering by user needs *[unclear]*
- Branding — Logo and slogan Dream It, Design It, Drive It *[claimed]*

**Flow:** Open site to see base Toyota in 3D → Click a part → Browse option carousel → See model update with animation → Receive matching real Toyota with specs

**Prompt:** not public / not found
**Fit (implied):** README frames it as a Toyota dream-car finder with search, compare and finance/lease options, delivered as a 3D build-your-own-car experience.  *(targeted: Toyota Financial Services track (implied), Best Design (implied))*
**AI:** No AI described; the recommendation method is not explained. ElevenLabs appears only as a tag.
**Architecture:** Nuxt full-stack app with TresJS/Three.js 3D scene, Blender assets, MongoDB via Mongoose for part and spec data.
**Novelty:** Custom Blender part models and a build-then-match flow rather than a questionnaire; team hand-built the parts dataset.
**Scope:** small · working: About 1.9k LOC Nuxt app with 3D assets and server routes; no demo link or video. · polish: Figma flow, logo/slogan, Canva deck; README is narrative plus Nuxt starter text.
**Claims:** Built a recommendation system that matches builds to real Toyota models
**Gaps:** Matching logic and finance/lease features from README intro not evidenced; ElevenLabs role unexplained; No video
Sources: https://devpost.com/software/buildyourride, evidence/hackutd-hackutd-2025-buildyourride.json

---

### BUYOTA
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A React site where the user picks a vehicle type and sets budget, credit score and down payment sliders; Claude 3.5 Sonnet with a web-search tool returns 4-6 current Toyota matches with estimated payments and pros and cons.
**Problem / user:** Toyota shoppers who want quick recommendations with monthly financing or lease estimates instead of long research.

**Features**
- Preference form — Vehicle type buttons (sedan, SUV, truck, hybrid, any) plus budget, credit score, down payment sliders *[shown_working]*
- Live web search recommendations — Claude with google_search tool finds current 2024-2025 Toyota models *[claimed]*
- Payment estimates — Financing and lease payments computed from credit score *[claimed]*
- Match cards — 4-6 results each with pros, cons and Toyota.com link *[claimed]*
- Dealership-style UI — Framer Motion animations and Tailwind red theme *[shown_working]*
- Trade-in, voice, multi-brand, price alerts — Listed future work *[planned]*

**Flow:** Open homepage → Choose vehicle type → Set sliders → Click Find My Toyota → Review recommendations and links

**Prompt:** not public / not found
**Fit (implied):** A Toyota recommender that folds credit score and down payment into payment estimates; no prize is named on the page.  *(targeted: Toyota Financial Services track (implied))*
**AI:** Claude 3.5 Sonnet through the Anthropic API with the google_search tool; parses tool results into structured matches and payment estimates.
**Architecture:** React/Vite/Tailwind single-page front end calling the Anthropic API directly with web search; no database described.
**Novelty:** Relies on live model web search instead of a fixed Toyota dataset; page claims it was built in 48 hours.
**Scope:** tiny · working: Single screenshot of homepage; no video or live link; repo unreachable. · polish: Animated, themed UI claimed; bug notes (tool_result parsing, env loading) indicate rough edges.
**Claims:** Turns 30 minutes of research into 30 seconds | Production-ready app built in 48 hours
**Gaps:** Evidence clone failed and raw/github README fetches failed; Payment formula not described; No video or live demo
Sources: https://devpost.com/software/jo-jo-focus

---

### Car Vibes
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A web app that asks the user for the vibe they want from a car, embeds the answers with Gemini, and recommends matching Toyota vehicles with Gemini-written insights on a chosen car.
**Problem / user:** Car shoppers, including the team themselves, lacking knowledge of leases and the buying process.

**Features**
- Preference form — Questionnaire gathers vibe, personality and needs, aiming also to surface unconsidered cars *[claimed]*
- Embedding-based matching — Gemini embeddings used to compare user inputs with Toyota vehicles *[claimed]*
- Toyota recommendations — Returns feedback on cars that fit the inputs *[claimed]*
- Gemini car insights — Selecting a car shows model-generated insights *[claimed]*

**Flow:** Fill vibe/preference form → See recommended Toyotas → Select a car → Read Gemini insights

**Prompt:** not public / not found
**Fit (implied):** Targets confusion in car buying with a Toyota recommender; page states no prize.  *(targeted: Toyota Financial Services track (implied))*
**AI:** Google Gemini API for token embeddings of preferences and for generating insights on a selected car.
**Architecture:** React/Tailwind/ShadCN front end from a Figma design; Express backend with MongoDB for car data and calls to Gemini.
**Novelty:** Vibe/personality-first framing rather than spec filters.
**Scope:** tiny · working: Backend connecting form to Gemini claimed; two screenshots only; no repo, demo or video. · polish: Admits styling bugs and unreliable testing; next step is a better UI.
**Gaps:** No repo linked; Matching method and car data source not detailed; No video
Sources: https://devpost.com/software/hackutd-25-tamusa-team-1

---

### CarCents
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A Toyota comparison and financing helper: scikit-learn models predict APR and default risk to suggest a down payment, plus a RAG chatbot whose answers filter a list of real car listings.
**Problem / user:** Car buyers confused by how credit score, APR, down payment and loan term drive monthly cost.

**Features**
- Side-by-side Toyota comparison — Dashboard compares models *[claimed]*
- APR prediction — ML model uses credit score, term, price, vehicle age and down payment rate; updates as sliders change *[claimed]*
- Down payment recommendation — Default-probability model yields Increase Down Payment or Good Standing *[claimed]*
- RAG car chatbot — Answers questions such as best SUV under 30k from a car dataset *[claimed]*
- Chatbot-driven filtering — Chat responses filter the listings shown in the frontend *[claimed]*
- Dynamic forms — Credit score and budget inputs with real-time updates *[claimed]*

**Flow:** Enter credit score and budget → Get recommended down payment and APR → Adjust down payment and term → Compare models → Ask chatbot and see list filter

**Prompt:** not public / not found
**Fit (implied):** Financing-focused Toyota tool combining ML loan predictions and a recommender chatbot; page lists no prize.  *(targeted: Toyota Financial Services track (implied))*
**AI:** scikit-learn APR and default-risk models trained on a car dataset (no real loan data per next steps) plus an unnamed LLM in a RAG chatbot.
**Architecture:** React/TypeScript/Tailwind client, Flask API serving model predictions, Firebase, RAG chatbot over car data.
**Novelty:** Pairs trained financing-prediction models with a chatbot that drives UI filters; hosted locally only.
**Scope:** medium · working: Client and Flask server exist (evidence LOC inflated by vendored server files); no demo or video. · polish: Figma design, dynamic forms; repo README is a stub.
**Claims:** Models deliver meaningful financial insights; no accuracy numbers
**Gaps:** Repo README is a stub with no feature content; Dataset and LLM unnamed; No video
Sources: https://devpost.com/software/carcents, evidence/hackutd-hackutd-2025-carcents.json

---

### cars.compare
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A solo Python script that compares Toyota vehicles with competitors using public safety and government data, then asks an LLM to write a verbal argument for Toyota from the inputs.
**Problem / user:** Car shoppers wanting facts without marketing, modelled on Texas's Power to Choose site.

**Features**
- Toyota versus competitor comparison — Pulls real-world data from DOT, NHTSA and IIHS APIs *[claimed]*
- LLM verbal argument — API call turns input parameters into a spoken-style case for Toyota *[claimed]*
- Wayback Machine proxy — Fetches blocked sites through archive snapshots *[claimed]*
- Caching layer — Buffers slow or inaccessible resources *[claimed]*

**Flow:** Supply comparison parameters → Script gathers data from public sources → LLM writes argument for Toyota

**Prompt:** not public / not found
**Fit (none):** Page names no prize; it addresses Toyota shoppers comparing vehicles.  *(targeted: )*
**AI:** One LLM API call (model unnamed) generates the argument; author says ChatGPT helped find endpoints.
**Architecture:** Python script aggregating NHTSA, DOT and IIHS APIs with a Wayback-based fallback proxy and cache.
**Novelty:** Data from government safety sources and archive proxy rather than a curated dataset.
**Scope:** tiny · working: Script described only; no repo, demo or video. · polish: No UI mentioned; author notes the proxy is slow and unreliable.
**Gaps:** No repo, demo, video or tags; Output format and user interface unknown
Sources: https://devpost.com/software/cars-compare

---

### CarTender
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A Tinder-style car matchmaker: after finance and must-have questions, LangGraph agents on Nemotron Nano 9B gather reviews and listings and present cars to swipe on, then guide financing, insurance and inspection.
**Problem / user:** Car buyers who want a personalized, less laborious route from preferences to a purchasable car.

**Features**
- Onboarding questions — Finances and must-haves such as CarPlay or no American cars *[claimed]*
- Agent research — Agents aggregate reviews, listings, rankings and sentiment from external APIs *[claimed]*
- Swipe cards and Like page — Swipe left/right on suggestions; liked cars collected *[shown_working]*
- Embedding personalization — Semantic embeddings capture subtle preferences *[claimed]*
- Vehicle history and safety view — Per-car details after choosing *[claimed]*
- Financing summary and purchase guidance — Agents find rates, insurance quotes, maintenance and inspection plans *[claimed]*

**Flow:** Answer finance and must-have questions → Agents research cars → Swipe on suggestions → Review Like page → Open history and safety → See financing and purchase guidance

**Prompt:** not public / not found
**Fit (implied):** Multi-agent Nemotron system hosted on Brev that supports car purchasing and financing; no prize stated on page.  *(targeted: Nvidia track / Brev (implied), Toyota Financial Services (implied))*
**Sponsor tools:** NVIDIA Nemotron Nano 9B v2 (LangGraph agent reasoning, core); Brev (NVIDIA L4 24GB) (hosting model and compute, core)
**AI:** LangGraph multi-agent orchestration on Nemotron Nano 9B v2 served from a Brev L4 GPU, plus embeddings for personalization and external car/review APIs.
**Architecture:** Vue/React frontend (repo ships a Vite shadcn app), Flask backend running LangGraph agents calling car, review and finance APIs, LLM on Brev.
**Novelty:** Dating-app swipe metaphor combined with agent-driven purchase guidance and self-hosted Nemotron.
**Scope:** medium · working: About 11k LOC with backend and frontend plus tests; no video or demo; screenshots caption the flow. · polish: Multi-screen flow described; README is the Devpost text with no setup instructions.
**Claims:** Fully agentic end-to-end matchmaking platform in 24 hours
**Gaps:** Named APIs not given; Devpost says Vue, manifests show React/shadcn frontend; No video
Sources: https://devpost.com/software/automatch-4jd2g8, evidence/hackutd-hackutd-2025-cartender.json

---

### Catalyst
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** An AI product-manager assistant. Devpost describes turning meeting transcripts into sprint tickets with RAG analytics and tool integrations; the repo implements a Nemotron service that turns pasted notes into PRDs, user stories, action items or summaries and exports to Notion.
**Problem / user:** Product and team leads whose meeting notes rarely become tasks and whose tools and analytics are siloed.

**Features**
- Notes to deliverables (repo) — Paste notes, pick Summary, PRD, User Stories or Action Items, Nemotron generates output *[shown_working]*
- Notion export (repo) — Backend creates a Notion page and returns its URL *[claimed]*
- Sprint tickets from meetings (Devpost) — Tickets from real-time transcripts or notes *[claimed]*
- RAG analytics engine (Devpost) — Retrieval over multiple sources for insights and ticket recommendations *[claimed]*
- Gemini summaries and stakeholder updates (Devpost) — Generated meeting summaries and updates *[claimed]*
- Integrations and drawing board (Devpost) — Slack, email, calendar, Excalidraw board, Firebase auth *[claimed]*
- Jira/Asana, forecasting, voice — Listed next steps *[planned]*

**Flow:** Paste meeting notes → Choose output type → Generate with Nemotron → Read result in right panel → Enter title and export to Notion

**Prompt:** not public / not found
**Fit (implied):** Repo is built on Nemotron Super 49B; Devpost names Gemini and lists no prize, so alignment is inferred.  *(targeted: Nvidia track (implied by repo))*
**Sponsor tools:** NVIDIA Nemotron Super 49B v1.5 (generating PRDs, stories, action items and summaries (repo), core)
**AI:** Repo: Nemotron via OpenAI SDK with prompts per output type. Devpost: Gemini for context and summaries plus RAG pipelines.
**Architecture:** Next.js 14 frontend with shadcn/ui; FastAPI backend with nemotron_service and notion_service; Devpost adds Firebase and SQLite.
**Novelty:** Broad integration vision for a PM operating system; repo covers the narrower notes-to-docs path.
**Scope:** medium · working: About 8.4k LOC two-tier app with API docs and setup steps; RAG and Slack features not seen in README. · polish: Clean README with endpoints and env example; no tests, video or live demo.
**Claims:** Smooth synchronization between Gemini, Notion and FastAPI with minimal lag
**Gaps:** Devpost (Gemini, RAG, tickets, Slack) and repo README (Nemotron, Notion, documents) disagree; feature list marks source; Devpost links only the backend folder; No video
Sources: https://devpost.com/software/my-pm-tool, evidence/hackutd-hackutd-2025-catalyst.json

---

### Cauldron-FlowGuard AI
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A Flask and React dashboard for the potion-factory dataset that compares ticketed volumes with actual cauldron drain, ranks discrepancies by severity, forecasts levels, and uses OpenAI to summarize risk, plus a courier scheduling module.
**Problem / user:** Operators facing unreliable reporting and overflow risk; framed as applicable across industries.

**Features**
- Ticket versus drain verification — Detects mismatches between reported and drained volumes, flagged by severity *[claimed]*
- Dashboard metrics — Total discrepancies, average difference, largest overflow, greatest loss *[claimed]*
- Multi-page views — Overview, History, Discrepancies, Forecast and a time-series heat map *[shown_working]*
- OpenAI risk summaries — Model interprets discrepancies and summarizes risk *[claimed]*
- Courier scheduling bonus — Finds fewest couriers to avoid overflow given travel times, drain and fill rates *[claimed]*
- Route visualization — Real-time route display and trend indicators *[claimed]*

**Flow:** Open Overview → Review ranked Discrepancies → Check History and heat map → Open Forecast and schedules

**Prompt:** EOG Resources 'Lost in the Pages' challenge (second-hand): reconcile potion tickets against cauldron drain levels, forecast overflow, and plan pickup routes; bonus asks for minimum couriers.
**Fit (explicit):** Page names the EOG challenge and its bonus: discrepancy detection, forecasting and minimum-courier scheduling over the EOG API.  *(targeted: EOG Resources challenge incl. bonus scheduling)*
**Sponsor tools:** EOG API (cauldron levels, tickets and network data, core)
**AI:** OpenAI API summarizes detected discrepancies; detection and scheduling are algorithmic (time-series comparison, anomaly detection).
**Architecture:** Flask backend ingesting the EOG API, React/Tailwind frontend; repo shows backend and potionwatch frontend with a database.
**Novelty:** Explicit drain-while-filling correction and date-versus-timestamp ticket matching in the planning guide; adds LLM risk narration.
**Scope:** medium · working: About 14k LOC with tests; Devpost calls it a functional prototype; no demo or video. · polish: Five screenshots; README is a team planning guide, not usage docs.
**Claims:** Identifies discrepancies in real time | Generates optimized courier schedules
**Gaps:** README is a hackathon planning guide (five-role team, FastAPI suggested), not a product README, and differs from Devpost's Flask; No video; Algorithm thresholds unknown
Sources: https://devpost.com/software/cauldron-flowguard-ai, evidence/hackutd-hackutd-2025-cauldron-flowguard-ai.json

---

### CauldronCare
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A gamified plant-care system: an ESP32 with a capacitive soil-moisture sensor streams readings over BLE to a React Native app that turns them into a Brew Score, streaks and guild leaderboards, with optional tap-to-spray and Gemini photo tips.
**Problem / user:** Houseplant owners who forget or overdo watering; friend groups and campus clubs motivated by competition.

**Features**
- Live moisture streaming — ESP32 normalizes sensor readings to a percentage and notifies the phone over BLE (Wi-Fi optional) *[claimed]*
- Brew Score — Score rises or falls depending on moisture relative to a target band; overflowing/underfilled cauldron penalties *[claimed]*
- Streaks, badges, guilds — Friends join guilds and compare weekly totals on a leaderboard *[claimed]*
- Insights screen — Moisture trend graphs and drift nudges *[claimed]*
- Tap-to-spray — PWM-driven spray mechanism with dose presets *[claimed]*
- Gemini photo hints — Photo of plant yields species hint, watering range and red flags *[claimed]*
- Two-point calibration and offline cache — Guided calibration, smoothing, local caching *[claimed]*
- Auth0 login — Hosted login and token storage *[claimed]*

**Flow:** Sign up via Auth0 → Onboard plant and target band → Pair ESP32 sensor → Watch score and graphs → Optionally photograph plant → Spray or add water → Join a guild

**Prompt:** not public / not found
**Fit (implied):** Real ESP32 sensing plus Auth0 and Gemini tags; page lists no prize, and it reuses the cauldron/brew theme.  *(targeted: Best Hardware (implied), Auth0 (MLH, implied), Best Use of Gemini API (implied))*
**Sponsor tools:** Auth0 (login and token storage, supporting); Google Gemini API (photo-based care tips, supporting)
**AI:** Gemini analyzes an optional plant photo for species hints and care guidance; scoring is rule-based on-device.
**Architecture:** ESP32 firmware reads sensor and drives spray; BLE notify to Expo React Native app (Zustand, TypeScript); Auth0 and Gemini in cloud.
**Novelty:** Pairs real hardware sensing and actuation with social gamification and theme-matched naming.
**Scope:** small · working: Hardware and app described in detail but no repo, video or demo to confirm. · polish: Multi-tab app with onboarding and calibration described; screenshots only.
**Claims:** Onboarding from zero to paired sensor in minutes | No metrics reported
**Gaps:** No repo, video or demo; Screenshot count not determined; Features unverified
Sources: https://devpost.com/software/cauldroncare

---

### CBRE Intelligence Hub
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A Next.js and Flask hub where users upload real-estate PDFs, chat with an AI Estate Advisor, and get extracted features run through a boosted-tree model for property value and future-value projections, with voice I/O and analytics.
**Problem / user:** Property managers and investors who spend hours searching unstructured contracts, reports and appraisals.

**Features**
- Document upload and extraction — PDFs parsed by a transformer-based extractor into features *[claimed]*
- Advisor chat — OpenAI model collects user needs and answers on value, maintenance and market *[claimed]*
- Value prediction — Categorical boosted regression trees on Zillow Kaggle data plus extracted maintenance costs *[claimed]*
- Voice input and output — Speech-to-text and text-to-speech *[claimed]*
- Explainable answers — Reasoning and source highlights *[claimed]*
- Analytics dashboard — Trends and predictions summaries *[shown_working]*

**Flow:** Upload property PDF → Chat with advisor → Extraction feeds model → Receive value and future-value estimate → Review analytics dashboard

**Prompt:** not public / not found
**Fit (implied):** Title and framing address CBRE's real-estate document insight problem; page lists no prize.  *(targeted: CBRE track)*
**AI:** Transformer extracts PDF features, gradient-boosted trees predict value (trained in Colab), OpenAI API drives chat and information gathering.
**Architecture:** Next.js/Tailwind frontend, Flask backend with pdf parsing and model scripts, trained on Zillow Kaggle dataset; repo has backend, uploads and catboost output.
**Novelty:** Chains document extraction into a tabular value model, plus voice I/O.
**Scope:** medium · working: About 1.8k LOC; catboost artifacts and uploads folder; no demo or video. · polish: Four screenshots, Canva deck; repo README is the Next.js template.
**Claims:** Model improves as more documents are added; no evidence given
**Gaps:** README is create-next-app boilerplate; Accuracy not reported; No video
Sources: https://devpost.com/software/john-project, evidence/hackutd-hackutd-2025-cbre-intelligence-hub.json

---

### Clarity
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A web tool where the user enters a public GitHub repo; a six-agent Nemotron system clusters issues, labels, prioritizes them, writes fix plans and on-demand code patches, and formats a Markdown report.
**Problem / user:** Engineers and maintainers facing many issues who need to decide which to tackle first.

**Features**
- Issue clustering — Summarizer groups issues, PRs and comments by topic *[claimed]*
- Label suggestions — Labeler proposes labels per cluster *[claimed]*
- Prioritization — Scores severity, impact and effort to rank top issues *[claimed]*
- Fix plans — Actionable steps per top issue *[claimed]*
- On-demand code patches — Code generator drafts patches; falls back to raw code extraction if JSON parse fails *[claimed]*
- Markdown report and web UI — Editor agent formats report; dark UI with progress *[claimed]*
- ReAct context fetching and caching — Agents fetch more context; 5-minute GitHub cache *[claimed]*

**Flow:** Enter repo → Fetch issues, PRs, comments → Agents analyze → View ranked issues with severity and fix → Request patch → Read report

**Prompt:** not public / not found
**Fit (explicit):** README and Devpost state it is built for the Nemotron track: six cooperating agents on Nemotron Nano 9B v2 with thinking tokens and tool calling.  *(targeted: Nvidia Nemotron prize track)*
**Sponsor tools:** NVIDIA Nemotron Nano 9B v2 (NIM API) (powers all six agents with thinking tokens and JSON output, core)
**AI:** Six agents (summarizer, labeler, prioritizer, fix-plan, code generator, editor) on Nemotron Nano via NIM, ReAct pattern, JSON mode and tool calling.
**Architecture:** FastAPI server with router orchestrator; GitHub REST client with TTL cache; LLM client (NIM, OpenRouter alternative); Pydantic schemas.
**Novelty:** Full pipeline from raw issues to patches with documented per-agent roles; team pivoted into it late.
**Scope:** small · working: About 2.5k LOC FastAPI app with REST API and UI; no tests or video. · polish: Very detailed README with diagrams and endpoint tables.
**Claims:** Production-ready with REST API, error handling and caching
**Gaps:** Only first part of README read; Devpost mentions only pseudocode fixes while README adds code patches; No video
Sources: https://devpost.com/software/clarity-9ow1qk, evidence/hackutd-hackutd-2025-clarity.json

---

### CometNow
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A campus-events web app with an interactive Leaflet map, user-added events (clubs, study groups, sports), a Gemini-powered advisor for campus questions, and points redeemable for rewards.
**Problem / user:** Students missing events because they are scattered across group chats and apps.

**Features**
- Event posting — Anyone can add club, study or sports events *[claimed]*
- Campus map — Leaflet map of nearby happenings *[claimed]*
- Smart advisor — Gemini answers common campus questions *[claimed]*
- Points and rewards — Points for participation redeemable for rewards *[claimed]*
- Auth and realtime data — Firebase auth and database *[claimed]*

**Flow:** Sign in → Browse events on map → Ask advisor → Join events → Earn points

**Prompt:** not public / not found
**Fit (implied):** Uses Gemini for the advisor; no prize named on page.  *(targeted: Best Use of Gemini API (implied))*
**Sponsor tools:** Google Gemini API (campus advisor, supporting)
**AI:** Gemini API drives a question-answering advisor; details not given.
**Architecture:** Next.js/TypeScript front end deployed on Vercel at cometnow.us, Leaflet map, Firebase auth and database.
**Novelty:** Campus-wide open event posting with points incentives; has a registered domain.
**Scope:** small · working: Live demo URL listed (not visited); six screenshots. · polish: Custom domain and Vercel hosting; no repo.
**Gaps:** No repo; Live site not visited; Reward catalog and advisor behaviour unknown
Sources: https://devpost.com/software/cometnow

---

### Cortex
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence C · confidence low*

**What it is:** An effectively empty Devpost submission: the template headings contain no text, the description is a placeholder, and only a Python tag and a video link exist. What the project does cannot be determined.
**Problem / user:** 

**Prompt:** not public / not found
**Fit (none):** No content to compare.  *(targeted: )*
**AI:** none
**Architecture:** 
**Novelty:** 
**Scope:** tiny · working: None; video link present but not watchable. · polish: None; empty sections.
**Gaps:** All description sections empty; No repo; Video not reviewable
Sources: https://devpost.com/software/cortex-3rsnv0

---

### Cursor on the Go!
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A phone-friendly remote for a desktop Cursor editor: JavaScript injected into Cursor's DevTools relays prompts and streamed answers over WebSockets to a Next.js mobile chat, with Auth0 login, a joke Stripe upgrade and a VS Code helper extension.
**Problem / user:** Developers who vibe-code and want to keep prompting Cursor when away from their laptop.

**Features**
- Remote prompting — Mobile or browser sends prompt; injected payload enters it in Cursor and streams answers back *[shown_working]*
- DOM injection payload — Console script hooks Cursor's UI, watches messages and talks to relay *[shown_working]*
- Relay server — FastAPI WebSocket server forwards messages between devices *[shown_working]*
- VS Code extension — Helps copy and inject the payload *[claimed]*
- Completion notifications — Alert when prompt finishes *[claimed]*
- Auth0 and Stripe — Account login and a $2 upgrade screen *[claimed]*
- Session sync — Mobile session mirrors desktop *[claimed]*

**Flow:** Start relay server and frontend → Paste payload into Cursor DevTools → Open mobile UI → Send prompt → Watch streamed response and get notified → Send follow-ups

**Prompt:** not public / not found
**Fit (implied):** Page lists no prize; it uses Auth0 and Stripe, with a lighthearted pitch.  *(targeted: Auth0 (MLH, implied))*
**Sponsor tools:** Auth0 (account management, supporting)
**AI:** none
**Architecture:** Injected JS in Cursor <-> FastAPI relay (WebSocket) <-> Next.js mobile frontend; VS Code extension generates payload.
**Novelty:** Hacks an unsupported editor via DevTools injection; README includes explicit security disclaimer that it can execute arbitrary code with limited authentication.
**Scope:** medium · working: About 8.9k LOC across frontend, relay, extension, docs; README demo video link and expected console output. · polish: Detailed README, disclaimer, docs folder, screenshots and YouTube demo; no tests.
**Claims:** $2 ARR (joke figure) | Core functionality works
**Gaps:** Video not watched; Only first part of README read
Sources: https://devpost.com/software/goon-cursor, evidence/hackutd-hackutd-2025-cursor-on-the-go.json

---

### Destination 67
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A cross-platform desktop assistant (Tauri, Windows and Mac) that indexes a user's local files in a vector store and lets them ask an AI agent to find, sort, delete or answer questions about those files.
**Problem / user:** People who accumulate years of files and find file explorers clumsy; also those who switch between work and home machines on different operating systems.

**Features**
- Natural-language file queries — User asks the agent about files on their machine; it answers using an index of their file system. *[claimed]*
- Sort and delete files by request — Agentic services carry out file actions the user asks for at any time. *[claimed]*
- File explorer vector store — Local files are embedded into a LanceDB vector database for retrieval. *[claimed]*
- Cross-platform desktop app — Tauri shell with a Rust backend and React/TypeScript frontend, aimed at Windows and Mac parity. *[claimed]*
- Multi-model agent setup — Uses three NVIDIA Nemotron 3 models for the agentic features. *[claimed]*
- Email integration — Attempted but dropped for other priorities. *[planned]*

**Flow:** Install and open the desktop app → App indexes local files into the vector store → User types a request (find, sort, delete, or a general question) → Agent acts on or answers about the files

**Prompt:** not public / not found
**Fit (implied):** Submitted to the general HackUTD 2025 'Lost in the Pages' theme; a file-understanding assistant loosely fits the documents theme and uses Nemotron, but no track is named.  *(targeted: )*
**Sponsor tools:** NVIDIA Nemotron 3 (Three models powering the file agent, core)
**AI:** Agentic assistant over a local-file vector index (LanceDB), driven by three Nemotron 3 models; the page says most agent-integration attempts worked.
**Architecture:** Tauri desktop shell: Rust backend plus Vite/React/TypeScript UI; file contents embedded into LanceDB; Nemotron-based agent services call file operations.
**Novelty:** A local, OS-level file agent with cross-platform packaging rather than a web app; scope is ambitious but the page documents little behavior.
**Scope:** small · working: Page claims working agentic services and vector store; no demo, video or README retrievable (repo clone failed). · polish: Only uncaptioned screenshots; no walkthrough.
**Claims:** Cross-platform operation ending Windows/Mac friction | Working agentic services and file-explorer vector store
**Gaps:** Repo README not retrievable (clone failed, raw README 404); No demo flow or metrics on page
Sources: https://devpost.com/software/file67

---

### Dev Friendly
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A JIRA-styled web tool where a developer enters a ticket title and a GitHub repo URL and gets a repo-aware, Markdown ticket description with action items, risks and a test plan. The Devpost page describes the web UI; the known pitch mentions a browser add-on, which the page lists only as a future idea.
**Problem / user:** Early-career developers joining new teams who need more than a one-line ticket to know where changes belong and what done means.

**Features**
- Generate Developer Action Items button — Takes ticket summary plus repo URL and calls a FastAPI /action-items endpoint that returns the plan into the Description field. *[shown_working]*
- Repo ingestion and embedding — Shallow-clones the repo, chunks code with overlap, embeds with Gemini embeddings into a FAISS index. *[shown_working]*
- Top-K context retrieval — Cosine-similarity search selects the most relevant snippets as context for the model. *[claimed]*
- Seven-section plan — Gemini drafts Summary, Assumptions, Risks, Action Items, Acceptance Criteria, Test Plan and Files to Touch under a strict system prompt. *[claimed]*
- Rendered ticket view — Markdown description is shown as a formatted ticket after Create. *[claimed]*
- Embedding cache — Repos already processed skip re-embedding on later runs. *[claimed]*
- Noise filtering and subdirectory scoping — Skips noisy files and can scope retrieval to subfolders. *[claimed]*
- Model fallback — Normalizes model names and falls back if a model is not enabled. *[claimed]*

**Flow:** Open the JIRA-like Create issue screen → Enter ticket summary and GitHub repo URL → Click Generate Developer Action Items → Backend clones, embeds, retrieves, and drafts with Gemini → Markdown plan fills Description → Click Create to view the rendered ticket

**Prompt:** not public / not found
**Fit (none):** No prize named. Uses Gemini (an MLH API-usage prize existed) and addresses a PM-to-developer workflow, but the link is inferred.  *(targeted: )*
**Sponsor tools:** Google Gemini API (Code embeddings and plan generation, core)
**AI:** Retrieval-augmented generation: Gemini embeddings of the cloned repo in FAISS, top-K chunks fed to Gemini with a strict seven-section prompt.
**Architecture:** Static HTML/JS front end mounted on FastAPI; python scripts clone the repo (gitpython), embed to FAISS, then call Gemini; response rendered as Markdown.
**Novelty:** Ties ticket writing to the actual codebase via RAG, outputting files-to-touch and test plan; UI is a JIRA mock because direct JIRA integration was not possible.
**Scope:** small · working: Pipeline described end to end with a README and example request; about 1k LOC; no demo or video. · polish: README is a generic quickstart; UI is a basic JIRA lookalike.
**Claims:** Embedding a codebase takes about 1 to 2 minutes | Reliable end-to-end flow with fallbacks and logging
**Gaps:** No demo video; Known pitch says browser add-on; Devpost lists Chrome extension as future
Sources: https://devpost.com/software/jirag, evidence/hackutd-hackutd-2025-dev-friendly.json (README)

---

### DreaMatcher
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A Toyota car-buying platform concept covering three pieces: a matcher that recommends a model and trim, an AI estimate of loan APR, term and payment, and an OCR/vision pre-screen of uploaded approval documents before a loan officer reviews.
**Problem / user:** Car buyers overwhelmed by choosing a vehicle, comparing financing and gathering documents, plus loan officers who review applications.

**Features**
- Dream Car Matcher — Recommends the model and trim fitting a customer's preferences, lifestyle and budget. *[claimed]*
- AI-generated loan terms — Estimates APR, term and monthly payment from credit profile, income and car price, blended with standard formulas. *[claimed]*
- Document pre-screening — OCR/vision pipeline checks uploads for completeness, legibility and required info before a human approver. *[claimed]*
- Multi-format uploads — Pipeline intended to handle many file types. *[claimed]*
- Two-sided use — Serves customers and loan approvers in one flow. *[claimed]*

**Flow:** Customer uses the matcher to choose a vehicle → Receives estimated loan terms → Uploads approval documents → Screener flags gaps before loan officer review

**Prompt:** not public / not found
**Fit (implied):** Page frames itself around Toyota Financial Services customers and approvers, covering the vehicle choice, financing and approval journey; no track is named.  *(targeted: Toyota Financial Services (implied))*
**AI:** Recommendation system, formula-blended loan-term generator and OCR/vision document checker; no models or providers named.
**Architecture:** Angular frontend, Node/Express backend with MongoDB (mongoose), OpenAI and pdf-parse dependencies, components talk over REST.
**Novelty:** Combines buyer-side matching with lender-side document triage in one concept.
**Scope:** small · working: Backend repo has about 2k LOC with Express, mongoose, openai and pdf-parse deps; README is a boilerplate; no demo. · polish: Five uncaptioned screenshots; frontend README is Angular boilerplate.
**Claims:** Document checker dramatically cuts loan officer review time (no data)
**Gaps:** Repos' READMEs are boilerplate; No demo or models named
Sources: https://devpost.com/software/project-dreamcatchers, evidence backend README (boilerplate), raw frontend README (Angular boilerplate)

---

### EasyBreathe
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** An iOS Swift app that guides a breathing cycle with an animated circle and timer cues for inhale, hold and exhale, showing live heart rate from HealthKit.
**Problem / user:** The author, a tennis player, whose breathing spirals under pressure; useful for anyone wanting to regain composure.

**Features**
- Guided breathing animation — A circle view expands and contracts to cue inhale, hold and exhale phases. *[claimed]*
- Visual timer and cues — Timer and visual prompts track the breathing cycle. *[claimed]*
- Live heart rate display — Queries HealthKit and shows heart rate during breathing. *[claimed]*

**Flow:** Open the app → Start a breathing session → Follow the expanding and contracting circle through phases → Watch heart rate shown alongside

**Prompt:** not public / not found
**Fit (none):** No prize named; the page does not connect to the theme or a sponsor.  *(targeted: )*
**AI:** none
**Architecture:** SwiftUI-style structure: breathingCircleView, a view model managing phases and the HealthKit heart-rate query, and ContentView.
**Novelty:** Single-purpose wellness utility with biometric feedback; no AI or backend.
**Scope:** tiny · working: Page says HealthKit heart rate integrated; no repo, demo or video. · polish: Author spent time smoothing animation; polish and watchOS version listed as future.
**Claims:** Heart rate shown during breathing helped display the app's effect
**Gaps:** No repo, video or demo
Sources: https://devpost.com/software/easybreathe-wl5s60

---

### Feynman Flow
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A web study tool combining flashcards with spaced repetition, Gemini-generated questions (including from uploaded PDFs) and a Socratic Sidekick that quizzes the learner and turns answers into blog-style notes.
**Problem / user:** Students who forget material because they self-test and review too little, and find writing flashcards slow.

**Features**
- Decks and flashcards — Create decks and cards for active recall. *[claimed]*
- Spaced repetition — Review buttons schedule next review: again in 1 minute, good in 10 minutes, easy in 1 day. *[claimed]*
- PDF to Q&A — Upload a PDF; text is extracted and Gemini generates questions and answers to bootstrap a deck. *[claimed]*
- Socratic Sidekick — Gemini asks topic-driven questions and answers contextual follow-ups, keeping session state. *[claimed]*
- Notes as blog posts — User responses are auto-formatted into structured notes stored as private flashcards or public blog-style posts. *[claimed]*
- Deployed demo — Frontend on Netlify proxying /api to a Railway backend. *[claimed]*

**Flow:** Create a deck or upload a PDF → Gemini generates Q&A → Review cards on the spaced schedule → Chat with the Sidekick on a topic → Save refined notes as a post

**Prompt:** not public / not found
**Fit (none):** No prize named; uses Gemini, which fits an MLH-style API prize, but the page does not claim it.  *(targeted: )*
**Sponsor tools:** Google Gemini API (Question generation, Sidekick dialogue, contextual Q&A, core)
**AI:** Gemini generates questions from PDFs or topics and runs a Socratic dialogue that restructures answers into notes.
**Architecture:** Vanilla JS frontend on Netlify; FastAPI plus SQLModel/SQLite backend on Railway with endpoints for decks, cards, PDF ingestion and posts; pypdf for extraction.
**Novelty:** Merges Feynman-style explanation, learning-in-public posts and spaced repetition in one small tool.
**Scope:** small · working: Live Netlify demo and a demo video linked; repo includes tests and a full backend; no README. · polish: Simple UI, one screenshot; repo tree is bloated with a vendored environment.
**Claims:** Built solo in 24 hours across frontend, backend and deployment
**Gaps:** Repo has no README; Video not watched; Page says Flask/Uvicorn tags but repo shows FastAPI
Sources: https://devpost.com/software/socratic-study-tool, evidence/hackutd-hackutd-2025-feynman-flow.json (no README; manifests only)

---

### FindingNemo
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A self-evolving agent system: a Nemotron generalist answers queries, a router logs intents, and when an intent recurs past a threshold the system synthesizes training data, filters it with a reward model and fine-tunes a smaller specialist (LoRA) that the router then uses.
**Problem / user:** Teams running AI where large general models are costly for simple, repetitive tasks and deployed models stop learning.

**Features**
- Intent router — Embeds queries (FAISS, cosine) and checks an agent registry to route to a specialist or the generalist. *[shown_working]*
- Recurring-intent detection — Counts similar queries in a log and flags a threshold crossing to create a specialist. *[shown_working]*
- Synthetic dataset generation — A teacher LLM generates prompt-response pairs with templates and semantic noise. *[claimed]*
- Reward-model filtering — Nemotron-70B-Reward scores examples; top 75% kept. *[claimed]*
- Automatic LoRA fine-tuning — PEFT/LoRA trains small models (Mistral-7B, Phi-3-mini, LLaMA-3-8B) on filtered JSONL. *[claimed]*
- Intent drift handling — Temporal clustering and adaptive variance thresholds merge or adapt agents. *[claimed]*
- Streamlit UI — Interface for sending prompts and viewing routing. *[claimed]*

**Flow:** Submit a query such as an SQL request → Generalist answers while router logs it → Similar queries accumulate to threshold → System generates, filters and fine-tunes a specialist → A later query is routed to the matching agent

**Prompt:** not public / not found
**Fit (implied):** No prize named; builds on Nemotron, NeMo and NIM, so it plausibly targets the Nvidia track, but this is inferred.  *(targeted: )*
**Sponsor tools:** NVIDIA Nemotron-253B / Nemotron-70B-Reward (Generalist and reward scoring, core); NVIDIA NIM / NeMo API (Model access, supporting)
**AI:** Distillation loop: Nemotron teacher generates synthetic data, a reward model filters it, PEFT/LoRA fine-tunes small students, FAISS embeddings route queries.
**Architecture:** Python microservices: router (FAISS plus SQLite registry and query log), trainer, fine-tuner with reward filter, JSONL pipelines, Streamlit front end.
**Novelty:** Aims at autonomous creation of specialist models from observed traffic, an unusual scope; demonstrated mainly through screenshots of the loop stages.
**Scope:** medium · working: Screenshots of threshold detection and routing; repo with about 3.5k LOC and tests; deployment and dashboard are future work. · polish: README with framework diagram; unresolved merge-conflict markers in requirements.txt.
**Claims:** Fully autonomous evolution loop | Claims 90% of real queries are simple (unsourced)
**Gaps:** No quantitative results; Page inconsistent on teacher model (Nemotron vs mixtral)
Sources: https://devpost.com/software/codenamebandage, evidence README

---

### FindMyToyota - Vehicle Finder
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A React single-page Toyota inventory browser with about a dozen filters, sorting, a live monthly-payment estimate on every car card driven by credit score and down payment sliders, favorites and a comparison modal. The AI assistant and dealer finder are mockups only.
**Problem / user:** Online Toyota shoppers who cannot see true monthly cost until late in the process.

**Features**
- Live payment estimator — Credit score slider and down payment update estimated monthly payment on every card. *[shown_working]*
- Advanced filters — Price, year, mileage, body type, fuel, MPG, color, seats, features. *[shown_working]*
- Sorting — By price, MPG or recommended. *[shown_working]*
- My Garage favorites — Saved in localStorage across sessions. *[shown_working]*
- Compare up to 3 cars — Side-by-side modal of specs. *[shown_working]*
- AI assistant ToyoBot — High-fidelity mockup only. *[planned]*
- Find nearby dealers — Mockup only. *[planned]*

**Flow:** Browse stock and set filters → Set credit score and down payment → See payments on cards → Favorite cars → Compare finalists

**Prompt:** not public / not found
**Fit (implied):** Toyota-themed shopping with financing transparency; no track named on the page.  *(targeted: Toyota Financial Services (implied))*
**AI:** None in current build; Gemini planned for the assistant.
**Architecture:** Vite React 19 SPA with Tailwind; memoized pipeline over a mock JSON car list (DB_CARS) to carsWithPayments to filteredCars; localStorage favorites.
**Novelty:** Front-end only prototype putting the financing estimate on every listing; data is scraped-style mock inventory.
**Scope:** small · working: README plus repo with about 1.6k LOC and 33 public images; features described as working; no live link. · polish: Tailwind UI, README with setup; demo movie mentioned but not linked.
**Claims:** Built in about 12 hours | Payments update instantly using useMemo
**Gaps:** No demo link; AI and dealer features are mock
Sources: https://devpost.com/software/team-registration-5btfpm, evidence README

---

### FinPath
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A Next.js web app that takes a short quiz about a life event (baby, home, career change, marriage, retirement, business) and uses GPT-4o to produce a personalized financial roadmap with dated milestones, plus a tool to compare options such as daycare versus nanny.
**Problem / user:** People facing major life transitions who cannot afford a $200-400/hr advisor and find generic advice unhelpful.

**Features**
- Life transition quiz — Collects income, location, timeline and event details. *[shown_working]*
- AI roadmap — GPT-4o returns prioritized milestones with dollar amounts and deadlines as Zod-validated JSON. *[claimed]*
- Decision comparison — Compares choices with upfront, monthly and 1- and 5-year costs and pros and cons. *[claimed]*
- Interactive timeline and progress — Visual journey and milestone completion stored locally. *[claimed]*
- Validation guardrails — Flags unrealistic figures such as an oversized emergency fund. *[claimed]*
- Six supported transitions — Baby, first home, career change, marriage, retirement, business. *[claimed]*

**Flow:** Take onboarding quiz → Receive roadmap → Mark milestones → Compare decisions

**Prompt:** README says it was built for Capital One's Best Financial Hack track; official text not public.
**Fit (explicit):** README states it targets Capital One's financial hack track with AI roadmaps for life transitions; Devpost names no track.  *(targeted: Capital One Best Financial Hack)*
**AI:** GPT-4o with structured prompts, few-shot good/bad advice examples, Zod schema validation and temperature tuning.
**Architecture:** Next.js 14 App Router with serverless API routes calling OpenAI; browser localStorage for data; Supabase planned; Vercel hosting.
**Novelty:** Frames finance help around life events rather than budgeting, with explicit business-model pitch.
**Scope:** small · working: Live Vercel demo link and a detailed README; some demo data is mock; no video. · polish: shadcn/ui, Framer Motion and a judge-facing README; roadmap cut features.
**Claims:** MVP in 12 hours | About $0.05 per roadmap | Claims 10x better personalization (no method) | 200M+ Americans per year face transitions (unsourced)
**Gaps:** No video; Repo shows differences from Devpost (Devpost says Supabase planned)
Sources: https://devpost.com/software/finpath-13muy0, evidence README

---

### Food search
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence C · confidence low*

**What it is:** An essentially empty submission: a React tag and one sentence saying the project recommends food stores, with a stated goal of matching a specific dish to restaurants that actually serve it.
**Problem / user:** People craving a specific dish whose map search returns places based on stale review mentions.

**Features**
- Food store recommendations — Only stated function; the goal is dish-to-restaurant understanding for queries like best X near me. *[claimed]*

**Prompt:** not public / not found
**Fit (none):** No prize or track connection stated.  *(targeted: )*
**AI:** none
**Architecture:** Only a React tag listed; nothing else documented.
**Novelty:** Not assessable beyond the stated dish-to-restaurant matching idea.
**Scope:** tiny · working: None on the page; no repo. · polish: Template headings empty.
**Gaps:** Empty description sections; No repo (a video link was noted in the queue but not confirmed on the page)
Sources: https://devpost.com/software/food-search

---

### GenVis
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A React dashboard with a FastAPI backend that uses NVIDIA Nemotron to help product managers brainstorm ideas and personas, generate user stories and acceptance criteria, and write sprint reports, with Jira task push and Slack broadcast.
**Problem / user:** Product managers and hackathon teams who struggle to turn raw ideas into structured plans and reports.

**Features**
- Ideation assistant — /api/ideate generates product ideas, pain points and personas. *[claimed]*
- Requirements generator — /api/requirements creates user stories and acceptance criteria. *[claimed]*
- Jira push — Sends generated tasks to Jira via REST API. *[claimed]*
- Sprint reporting — /api/report summarizes progress for stakeholders. *[claimed]*
- Slack broadcast — Posts reports to a channel through webhooks. *[claimed]*
- Tabbed dashboard — Forms per step with cards, grids and metrics panels in a bank-inspired theme. *[claimed]*
- Caching and timestamps — AI and API responses cached with last-used times. *[claimed]*

**Flow:** Open ideation tab and enter prompt → Move to requirements and generate stories → Push stories to Jira → Generate report and send to Slack

**Prompt:** README says it was built for PNC Bank's Product Innovation Challenge and another HackUTD challenge; text not public.
**Fit (explicit):** README states it targets PNC's product innovation challenge by covering ideation, planning and reporting for PMs, using Nemotron for the Nvidia side.  *(targeted: PNC Product Innovation Challenge, Nvidia (Nemotron))*
**Sponsor tools:** NVIDIA Nemotron-Nano-9B (Ideas, requirements and report generation, core)
**AI:** Prompted Nemotron-Nano-9B-v2 via NVIDIA API for generation of ideas, requirements and summaries.
**Architecture:** React frontend calls FastAPI (mock_api, agent_backend, integrations) which calls Nemotron and Jira/Slack APIs.
**Novelty:** Covers the full PM loop in one tool with enterprise integrations; otherwise a standard LLM-wrapper pattern.
**Scope:** small · working: Detailed README with setup and about 2k LOC; no demo or video. · polish: Themed UI; README mentions planned deployment and analytics.
**Gaps:** No demo or video; Devpost does not name PNC; README does
Sources: https://devpost.com/software/genvis, evidence README

---

### Homefull
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A React Native (Expo) mobile app with a map that shows nearby shelters, food and other resources for people experiencing homelessness, backed by a FastAPI server running Nemotron 70B as an agent that searches the web for events like food drives.
**Problem / user:** People experiencing or leaving homelessness who do not know what help is nearby; designed for phones.

**Features**
- Resource map — Map of nearby shelters, food, restrooms and support with search and menu. *[shown_working]*
- Agentic event research — Nemotron generates searches, narrows results and decides if an event is worth showing. *[claimed]*
- Free meals and outreach — Finds church meals and harm-reduction schedules. *[claimed]*
- Map data from OpenStreetMap — Nominatim and Overpass supply place data. *[claimed]*
- Single-call frontend — One API call followed by an O(n) sort. *[claimed]*

**Flow:** App sends user GPS to the API → Nemotron generates searches and filters events → Results appear on the map → User searches or browses the menu

**Prompt:** not public / not found
**Fit (implied):** No track named; uses Nemotron with tool-calling for social good, so an Nvidia fit is inferred.  *(targeted: )*
**Sponsor tools:** NVIDIA Nemotron 70B (Ollama) (Agent that searches and filters resources, core); DigitalOcean (Hosting VM with GPU credits, supporting)
**AI:** Nemotron 70B served via Ollama with Python helper functions as tools, including URL reading; DuckDuckGo search feeds it.
**Architecture:** Expo app with react-native-maps; FastAPI in Docker on DigitalOcean; Nemotron run on host for CUDA; OSM APIs for data.
**Novelty:** Agentic web research to surface ephemeral local resources beyond static map data.
**Scope:** small · working: Six screenshots and an agentic pipeline said running; README only gives a run command; no video. · polish: Fixed map library issues; ElevenLabs cues dropped.
**Gaps:** README almost empty; No demo video
Sources: https://devpost.com/software/kinda-homeless, evidence README (minimal)

---

### id8
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A backend that ingests product documents (PDF, DOCX, text) into a ChromaDB store and, through a /generate-epics endpoint, uses an LLM to produce prioritized Jira-ready epics and stories with acceptance criteria.
**Problem / user:** Product managers and teams spending time converting scattered documentation into a backlog.

**Features**
- Document ingestion — Loads and sanitizes PDF, DOCX and text and indexes them in ChromaDB. *[claimed]*
- Epic generation endpoint — /generate-epics retrieves context and returns prioritized epics with descriptions and acceptance criteria. *[claimed]*
- Jira-shaped output — Structured JSON organized as epics and user stories. *[claimed]*
- Go-to-market generation — Release notes and marketing copy from docs. *[planned]*
- Wireframe and test-case agent — Drafts test cases from epics. *[planned]*
- Backlog grooming agent — Flags conflicting requirements. *[planned]*

**Flow:** Upload product documents → Documents are cleaned and embedded → Call /generate-epics → Receive prioritized epics and stories

**Prompt:** not public / not found
**Fit (implied):** No prize named; Nemotron named as example model via OpenRouter, so an Nvidia fit is inferred.  *(targeted: )*
**Sponsor tools:** NVIDIA Nemotron via OpenRouter (Structured JSON epic generation, core)
**AI:** LangChain RAG over HuggingFace MiniLM embeddings in ChromaDB; Nemotron through OpenRouter prompted for structured JSON.
**Architecture:** FastAPI service with PyPDF/Docx loaders, sanitization, ChromaDB vector store and LLM generation; React and PostgreSQL tagged but unexplained.
**Novelty:** Backlog generation from existing docs with planned grooming and GTM agents; mostly a standard RAG pipeline.
**Scope:** small · working: Endpoint described; no repo, demo or video linked. · polish: Text-only page.
**Claims:** Endpoints described as blazing-fast (no data)
**Gaps:** No repo, video or demo
Sources: https://devpost.com/software/id8-xvm60c

---

### idk
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence C · confidence high*

**What it is:** An empty placeholder submission whose only content is the word idk in the tagline and What it does, with a single idk tag.
**Problem / user:** 

**Prompt:** not public / not found
**Fit (none):** None stated.  *(targeted: )*
**AI:** none
**Architecture:** 
**Novelty:** No project content.
**Scope:** tiny · working: None. · polish: None.
**Gaps:** No description, repo or media
Sources: https://devpost.com/software/idk-ay90x2

---

### IKARIS
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A chatbot for CBRE commercial real-estate analysts that answers questions over lease contracts, reports and CSVs, returning a confidence level and inline sources, with predictive analysis from regression and random forest models on synthetic quarterly data.
**Problem / user:** CRE analysts juggling many PDFs, spreadsheets and tabs to assess lease risk and operating expense spikes.

**Features**
- Document Q&A — RAG over chunked CBRE report PDFs and contracts. *[shown_working]*
- Confidence and sources — Each answer includes a confidence level and inline sources. *[claimed]*
- Predictive analysis — Multiple linear regression and random forest over trends in structured data. *[claimed]*
- Synthetic dataset generator — Algorithm builds sample data mimicking CBRE quarterly data. *[claimed]*
- Conversational chat — Trained to hold basic conversation; screenshots show greeting and complex answer. *[shown_working]*
- Embeddable front end — React UI planned to integrate into existing tools. *[planned]*

**Flow:** Open chat interface → Ask a multi-part question about leases or OPEX → System retrieves chunks and data → Answer with confidence and sources

**Prompt:** not public / not found
**Fit (implied):** Page targets CBRE analysts and lease-risk and OPEX questions using Nemotron; no explicit track statement.  *(targeted: CBRE (implied), Nvidia (Nemotron))*
**Sponsor tools:** NVIDIA Nemotron (Main model adapted to CBRE context, core)
**AI:** Hybrid: Nemotron with RAG over PDFs (LangChain, Chroma) plus scikit-learn regression and random forest on synthetic structured data.
**Architecture:** Flask backend with LangChain, Chroma and scikit-learn; Node/React front end; synthetic data generator.
**Novelty:** Combines document RAG and classical ML forecasting for CRE questions; meta description oddly says humanoid but body describes software.
**Scope:** small · working: Three screenshots of chat responses; no repo, demo or video. · polish: Basic chat UI.
**Claims:** RAG with small models can beat one large model on niche data (lesson, no data)
**Gaps:** No repo or video; No metrics
Sources: https://devpost.com/software/ikaris

---

### inteliBudget
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A Nuxt/Vue budgeting app meant to build a budget from a user's bank transactions (Capital One Nessie API), with AI agents orchestrated in Azure and Nemotron writing a short financial summary. The page says the backend was not finished.
**Problem / user:** Individuals with no financial advice source besides their bank.

**Features**
- Budget generation — Creates a budget from transactions and savings. *[planned]*
- Nessie data pull — Reads transactions and savings via Capital One Nessie API. *[claimed]*
- Nemotron summary — Writes a text summary of the financial situation. *[claimed]*
- Multi-agent orchestration — Azure OpenAI o3-mini orchestrates agents. *[claimed]*
- Azure infrastructure — Functions, Storage, Key Vault and App Insights. *[claimed]*
- Frontend dashboard — Vue UI showing how the app should work. *[shown_working]*

**Flow:** Sign in via Auth0 (dependency) → Data pulled from Nessie → Agents produce budget options → View charts and summary

**Prompt:** not public / not found
**Fit (implied):** Uses Capital One's Nessie API for budgeting; no track named.  *(targeted: Capital One (implied))*
**Sponsor tools:** Capital One Nessie API (Transactions and savings, core); NVIDIA Nemotron (Summary blurb, supporting)
**AI:** Azure OpenAI o3-mini orchestrates agents; Nemotron generates the summary.
**Architecture:** Nuxt UI frontend with Auth0 and unovis charts; Azure Functions, Storage tables and Key Vault backend; Nessie as data.
**Novelty:** Cloud-engineering oriented build around Azure services.
**Scope:** small · working: Page admits backend incomplete; repo about 2.4k LOC, README minimal, has CI. · polish: One screenshot of Function App keys.
**Gaps:** Backend unfinished; No demo
Sources: https://devpost.com/software/intelibudget, evidence README (minimal)

---

### JJKA
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence C · confidence high*

**What it is:** A placeholder submission: the inspiration reads 'friendship and happiness', built-with tags are friendship, love and magic, and the repo contains three non-code files.
**Problem / user:** 

**Prompt:** not public / not found
**Fit (none):** None stated.  *(targeted: )*
**AI:** none
**Architecture:** 
**Novelty:** No project content.
**Scope:** tiny · working: None; repo has no README or code. · polish: One screenshot.
**Gaps:** No description of any product
Sources: https://devpost.com/software/jjka, evidence repo (no README, 3 files)

---

### KanbanSync
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A Next.js Kanban board for datacenter engineers where natural-language instructions become structured tickets, validated by a dual RAG pipeline against technical manuals, prioritized with reasoning, and grouped into route-minimizing work blocks.
**Problem / user:** Datacenter engineers working with outdated ticketing, task planning and routing.

**Features**
- NL to ticket — GPT-4o-mini parses instructions into structured tickets. *[claimed]*
- Dual-RAG validation — Technical and datacenter manuals retrieved via Ada embeddings in Supabase; model confirms or denies instruction. *[claimed]*
- Inventory and procedure suggestions — Suggests parts and steps automatically. *[claimed]*
- LLM prioritization — Assigns priority and explains reasoning. *[claimed]*
- Work blocks — Optimizes tasks to shorten walking paths. *[claimed]*
- Sidebar assistant — Chat for inventory, procedures and hardware. *[claimed]*
- Real-time board — Drag-and-drop Kanban updated by WebSockets. *[claimed]*

**Flow:** Type instruction → Ticket created and validated → See suggestions and priority → Arrange on board → Follow work blocks → Ask sidebar

**Prompt:** Northmark data-center technician challenge: work-order ticketing, routing of tasks, inventory and human-error prevention for technicians (secondary description from a winner's README; official text not public).
**Fit (implied):** Covers ticketing, routing and error prevention for datacenter technicians; page says the team pivoted after misunderstanding the prompt.  *(targeted: Northmark (implied))*
**AI:** GPT-4o-mini for parsing, prioritization and validation; OpenAI Ada embeddings with Supabase pgvector retrieval.
**Architecture:** Next.js/TypeScript frontend with Clerk auth and WebSockets; FastAPI backend; Supabase storing board, users, vectors.
**Novelty:** Safety gate validating instructions against manuals before execution.
**Scope:** medium · working: Claimed working pipeline and UI; about 3.8k LOC repo with README; no demo or video. · polish: Animated drag-and-drop UI.
**Gaps:** No demo or video; Northmark challenge text is secondhand
Sources: https://devpost.com/software/kanbansync, evidence README, prompts_cache/hackutd-2025.md

---

### Kramhtron.ai
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A multi-agent maintenance system for data center technicians: camera frames analyzed by Nemotron vision, a voice agent with RAG over Dell server manuals, ReAct ticket triage, and a coordinator that assigns tickets, all on a Convex realtime backend.
**Problem / user:** Data center floor technicians burdened by tedious ticketing, communication, inventory and human error.

**Features**
- Vision agents — Nemotron analyzes camera frames for safety violations and errors, with dedup and caching. *[claimed]*
- Voice agent — ElevenLabs agent with RAG over Dell manuals handles questions, tickets and inventory. *[claimed]*
- ReAct triage — Reason-act-observe workflow fills ticket details. *[shown_working]*
- Supervisor and coordinator — Summarize feeds and assign tickets by skills and urgency. *[claimed]*
- Live video via Convex — Frames stored and broadcast to the front end; mock streaming from files. *[shown_working]*
- Voice alert throttling — At most two alerts per five minutes. *[claimed]*
- Auth0 access control — Limits data access. *[claimed]*

**Flow:** Register technicians and cameras → Stream video → Vision flags an issue → Ticket created or voice alert → Coordinator assigns → Technician asks voice agent

**Prompt:** Northmark data-center technician challenge: work-order ticketing, routing of tasks, inventory and human-error prevention for technicians (secondary description from a winner's README; official text not public).
**Fit (implied):** Addresses technician ticketing, inventory and error prevention using Nemotron and ElevenLabs; no explicit track statement.  *(targeted: Northmark (implied), Nvidia (implied), ElevenLabs (implied))*
**Sponsor tools:** NVIDIA Nemotron via OpenRouter (Vision analysis, core); ElevenLabs (Voice guidance and agent, core); Auth0 (Authentication, supporting)
**AI:** Nemotron multimodal reasoning on frames with caching and batching; ReAct agents; ElevenLabs voice with RAG on service manuals.
**Architecture:** Convex backend and database, React/Tailwind frontend, Python OpenCV server for physical.inc camera frames, frame extraction scripts, OpenRouter and ElevenLabs.
**Novelty:** Uses a physical camera dev kit with multi-agent coordination, beyond typical chatbot builds.
**Scope:** medium · working: About 9.8k LOC repo, API endpoints and scripts documented; no demo or video. · polish: Detailed README, seven screenshots.
**Claims:** 24-hour frame cache and batching of 5 frames (README)
**Gaps:** No demo or video; Name spelled two ways
Sources: https://devpost.com/software/project-ducjxoi3254e, evidence README, prompts_cache/hackutd-2025.md

---

### Kynetic
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A car-shopping web dashboard where users browse and filter vehicles, compare models, save favorites to a garage, book test drives and explore leases, with a chat assistant. Devpost frames it as AI-assisted discovery; the README says the assistant is purely local heuristics.
**Problem / user:** Car shoppers overwhelmed by specs, trims and reviews who want a simpler, personalized way to find and compare vehicles.

**Features**
- Browse and filter cars — Filters by body type, powertrain, region, year and budget in a React dashboard backed by an Express API. *[shown_working]*
- Model comparison summary — POST /api/compare-summary returns a short heuristic text comparing two cars, with no external LLM. *[shown_working]*
- Chat assistant — Local NLP heuristics using the compromise parser to detect intents and entities in typed queries. *[shown_working]*
- My Garage favorites — Authenticated users save cars to a personal garage via JWT-protected endpoints. *[shown_working]*
- Test drive booking — Protected /api/testdrive endpoint lets a logged-in user book a test drive. *[shown_working]*
- Lease workflow — Protected /api/lease endpoint supports exploring lease options. *[shown_working]*
- Preference learning over time — Devpost says the system learns user preferences and personalizes recommendations; the README shows no such mechanism. *[claimed]*

**Flow:** Open the dashboard and sign in → Filter or search cars by type, powertrain, budget → Ask the chat assistant to refine results → Compare two models for a summary → Save favorites, book a test drive or explore a lease

**Prompt:** not public / not found
**Fit (none):** No prize or sponsor track is named on either source. The car-discovery theme could relate to a Toyota-style mobility challenge, but nothing confirms that link.  *(targeted: )*
**AI:** Described on Devpost as natural-language search and ranking; README states no external AI is used and chat is local heuristics via the compromise NLP library.
**Architecture:** React 19/Vite/Tailwind/Zustand frontend talks to a Node/Express API with JWT auth and JSON-file storage; chat and compare use rule-based logic in the backend.
**Novelty:** A fairly full car-shopping flow (garage, test drives, leases) for a hackathon, but the AI is heuristic rather than model-based, which the README admits and Devpost glosses over.
**Scope:** medium · working: About 9k lines across 70 code files; README documents endpoints and run steps. No live link or video. · polish: Tailwind UI with demo images and animation libraries in dependencies; no tests.
**Claims:** Devpost: learns user preferences over time and personalizes recommendations | README: no external AI services, all responses local/heuristic
**Gaps:** Devpost and README disagree on how AI-driven the assistant is; features follow the README; No video or live demo; Personalization claim unverified
Sources: https://devpost.com/software/driveselect, https://github.com/Kushal3121/hackutd-2025 (evidence file README)

---

### lisTen.AI
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A web portal for T-Mobile staff that pulls customer complaints from the r/tmobile subreddit, runs them through a LangGraph multi-agent pipeline using Nemotron, and presents sentiment, validity and impact scores plus generated reports.
**Problem / user:** T-Mobile employees who miss regional or group-specific network problems because customer feedback is scattered and unanalyzed.

**Features**
- Reddit fetch agent — Collects posts from the r/tmobile subreddit through Reddit's public API as raw input. *[claimed]*
- Evaluator agent — Scores posts for sentiment, validity and impact and categorizes issues, using Nemotron via OpenRouter plus FAISS retrieval over NVIDIA embeddings. *[claimed]*
- Report agent — Generates human-readable natural-language reports for T-Mobile teams that employees can read and interact with. *[claimed]*
- Supabase persistence — Stores posts, scores and reports in a PostgreSQL database so data survives across sessions. *[claimed]*
- Branded reports portal — React/TypeScript frontend behind Auth0 login shows reports and analytics in a T-Mobile styled dashboard. *[claimed]*
- Issue spread tracking — Devpost says it identifies current issues and tracks how they spread across customers. *[claimed]*

**Flow:** Employee signs in via Auth0 → Agents are run (python -m agents.workflow) to fetch and evaluate Reddit posts → Results are written to Supabase → Employee opens the portal to read generated reports and analytics

**Prompt:** T-Mobile challenge (per project framing): measure a customer happiness signal from social data. NVIDIA challenge: agentic multi-step workflows. No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (explicit):** README states it was built for the T-Mobile and NVIDIA challenges: live Reddit sentiment feeds a Customer Happiness Index style portal, with Nemotron-driven agents handling analysis and reporting.  *(targeted: T-Mobile track, NVIDIA track)*
**Sponsor tools:** NVIDIA Nemotron (via OpenRouter) (Sentiment, validity and impact analysis and report writing inside agents, core); NVIDIA embeddings (FAISS vector store for RAG categorization, supporting)
**AI:** Three LangGraph agents (fetch, evaluator, report) call Nemotron through OpenRouter; RAG with FAISS and NVIDIA embeddings categorizes issues before report generation.
**Architecture:** Python/Flask backend with LangGraph workflow reads Reddit, calls Nemotron, writes to Supabase Postgres; React/TypeScript/Tailwind frontend with Auth0 reads the reports.
**Novelty:** Uses real Reddit data rather than simulated posts, which many same-track entries used, and splits the work into distinct agents; includes a PRD and setup checklist.
**Scope:** medium · working: About 4k lines in 43 code files with tests present; setup docs. No video or live link, and the README admits data is thin. · polish: Dedicated documentation folder with PRD and checklist, branded portal; no Docker or CI.
**Claims:** Fetches live Reddit opinions to gauge customer happiness | Built a coherent backend data flow despite little prior Supabase/OpenRouter experience
**Gaps:** No demo video or screenshots; Output quality not shown; Repo file count inflated by a vendored directory
Sources: https://devpost.com/software/listen-ai, https://github.com/Idid118first/HackUTDProject2025Public (evidence file README)

---

### Lotus AI
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A voice and video virtual nurse that holds a natural conversation, tracks symptoms over time, searches the web and nearby hospitals, can book appointments through browser automation and email follow-ups, and hands a clinical summary to a provider.
**Problem / user:** Patients facing slow, repetitive intake and confusing care, plus clinics that want structured pre-visit data.

**Features**
- Voice conversation — Speech is transcribed with ElevenLabs and answered with short, empathetic voice-friendly replies. *[claimed]*
- Video feed interpretation — NVIDIA NIM vision model reads camera input alongside speech to understand symptoms. *[claimed]*
- Symptom tracking and memory — Backend phase manager tracks timing, context and past symptoms across the conversation. *[claimed]*
- Agentic web and hospital search — Tag-based reasoning triggers real-time web search or nearby-hospital lookup using the user's location. *[claimed]*
- Appointment booking — Selenium automation books appointments only when the user opts in. *[claimed]*
- Optional follow-up email — Sends a follow-up email under user control (the repo lists an AgentMail dependency). *[claimed]*
- Clinical summary for provider — Produces a clean summary of the intake for the clinician. *[claimed]*
- Frontend experience — Next.js UI with 3D model, sidebar, transcript, dark mode. *[shown_working]*

**Flow:** Start a voice (optionally video) chat with the nurse → Nurse asks follow-ups and tracks symptoms → Search or hospital lookup triggers when needed → User optionally approves booking and follow-up email → Provider receives a clinical summary

**Prompt:** No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (implied):** No prize named. Uses Nemotron and ElevenLabs, which map to the NVIDIA and MLH ElevenLabs prizes, but the pages never state a target.  *(targeted: )*
**Sponsor tools:** NVIDIA NIM / Nemotron (Reasoning and vision over text and video, core); ElevenLabs (Speech transcription, core)
**AI:** LLM agent on Nemotron/NIM with a tag-based reasoning framework that triggers tools (search, location, booking, email); vision model interprets video frames; ElevenLabs handles speech.
**Architecture:** Next.js frontend (3D model, transcript, sidebar) streams voice/video to a FastAPI backend that manages conversation phases and calls NIM, ElevenLabs, Selenium and email.
**Novelty:** Combines video understanding, tool-triggering and opt-in actions like booking and email in one nurse persona, a wider scope than typical symptom chatbots.
**Scope:** medium · working: About 16k lines and 46 code files with tests; Devpost screenshots of chat, booking and email. No video. · polish: Screenshots show dark mode and a 3D model; README is only setup commands.
**Claims:** Fully functional multimodal nurse assistant built from scratch | Real-time web and hospital search with optional user-controlled booking and email
**Gaps:** README has no project description, so features come from Devpost only; No demo video; Booking and search flows not confirmed in code
Sources: https://devpost.com/software/nurseai-2hp5d0, https://github.com/AnSingh1/nurseai (evidence file; README is setup-only)

---

### MagentaMonitor
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A React dashboard that overlays a Customer Happiness Index and Reddit sentiment on 5G, wireless and cellular quality and outage data, with a click-to-filter scatter plot and a slider-based happiness predictor.
**Problem / user:** T-Mobile teams wanting to see how outages and poor 5G quality translate into customer unhappiness.

**Features**
- KPI cards — Show overall Customer Happiness Index, live sentiment, posts analyzed and average 5G quality with a blinking red alert state. *[claimed]*
- Sentiment vs CHI chart — Time series of positive, negative and neutral Reddit sentiment against CHI with live-update pulse. *[claimed]*
- Network quality and outages chart — Plots 5G, wireless and cellular quality over time with outages as red bars. *[claimed]*
- CHI predictor — Sliders for network quality plus an outage toggle feed a JavaScript linear regression via a simulated async API. *[claimed]*
- Correlation scatter with filter — Scatter of CHI vs 5G quality; clicking a month filters the post table. *[claimed]*
- Filterable post table and breakdowns — Recent Reddit posts plus pie and bar charts of happiness levels and top sources. *[claimed]*
- Simulated live refresh — Static JSON files re-fetched every 10 seconds to mimic streaming. *[claimed]*

**Flow:** Open dashboard and read KPI cards → Watch sentiment and network charts update → Click a month on the scatter plot to filter posts → Adjust sliders and run the CHI prediction

**Prompt:** T-Mobile challenge (as framed by entries): correlate customer happiness signals with network performance. No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (implied):** Directly ties a happiness index and Reddit sentiment to network and outage data, the apparent T-Mobile theme; the page does not name the prize.  *(targeted: T-Mobile track)*
**AI:** Only a hand-written JavaScript linear regression relating 5G quality to CHI; sentiment scoring method unstated. Hugging Face/Flask tags are unexplained and proposed for later.
**Architecture:** Single-page React app with Recharts loads three static JSON files (CHI, Reddit, network), merges by date, and runs the regression in the browser.
**Novelty:** Joins sentiment to network-quality data in one interactive view with a what-if predictor; data is static and the API simulated.
**Scope:** small · working: Devpost describes charts and predictor in detail but repo was unreadable and no video or demo link. · polish: Dark theme, animations and responsive grid described; nothing independently seen.
**Claims:** Click-to-filter scatter plot linked to the post table | Predictor wired to a simulated API and regression model
**Gaps:** Repo clone failed and raw README fetch failed on HEAD and main; Data origin and sentiment method unclear
Sources: https://devpost.com/software/magentamatrix

---

### mimimimimi
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A dashboard design that gathers T-Mobile customer feedback from calls, reviews and forums, clusters complaints geographically with DBSCAN into scored hotspots, overlays coverage maps against competitors, and uses Gemini to suggest actions.
**Problem / user:** T-Mobile technicians and managers who cannot easily find problem areas or well-performing regions across scattered feedback.

**Features**
- Multi-source feedback ingestion — Pulls call speech-to-text, ElevenLabs tone detection, web reports and month-old Google, ConsumerAffairs and community forum reviews. *[claimed]*
- Sentiment and severity scoring — Fast-BERT sentiment and BERT embeddings assign severity and mark satisfied regions. *[claimed]*
- DBSCAN hotspot clustering — Complaints cluster spatially, scored by sentiment and cluster density into risk values. *[claimed]*
- Coverage map overlays — T-Mobile and competitor coverage layers shown to compare strengths. *[claimed]*
- Trends and fix log pages — Regional time-trend page and a log of fix history. *[claimed]*
- Gemini recommendations — LLM flags areas needing attention, strong regions, and suggested interventions. *[claimed]*
- Hourly refresh — Hotspot data updates hourly in the dashboard. *[claimed]*
- Graph/GNN representation — Feedback restructured as a graph linking complaints, places and severity; GNNs mentioned. *[unclear]*

**Flow:** Open main page for overall trends and coverage maps → Check Hotspots page for clusters and severity → Review Trends page per region → Consult Log page for past fixes

**Prompt:** T-Mobile challenge (as framed by entries): turn customer feedback into insight on where service issues sit. No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (implied):** Targets T-Mobile technicians and management directly, clustering feedback into geographic hotspots and sentiment scores; prize not stated.  *(targeted: T-Mobile track)*
**Sponsor tools:** ElevenLabs API (Tone detection on call audio, supporting)
**AI:** Fast-BERT sentiment, BERT embeddings, DBSCAN spatial clustering, possibly GNNs, and a Gemini LLM for recommendations.
**Architecture:** Python pipeline stores feedback in MongoDB; Next.js plus Shiny/Geopandas views show hotspots, trends and coverage overlays.
**Novelty:** Spatial clustering with competitor coverage overlay and a fix log is more geographic than most sentiment dashboards; no repo, so implementation depth is unknown.
**Scope:** medium · working: Devpost describes four dashboard pages but links no repo, video or demo. · polish: Unverifiable; no screenshots described.
**Claims:** Hotspots update hourly | Severity score combines sentiment analysis and clustering
**Gaps:** No repo, demo or video; GNN use stated only in learnings; Unclear which parts were built vs planned
Sources: https://devpost.com/software/mimimimimi

---

### Monkey C
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence C · confidence low*

**What it is:** An abandoned placeholder submission; the page says only that it was never finished and lists React as the sole technology.
**Problem / user:** Not stated.

**Prompt:** not public / not found
**Fit (none):** Nothing to evaluate; no project content.  *(targeted: )*
**AI:** none
**Architecture:** 
**Novelty:** None; empty entry.
**Scope:** tiny · working: None; author says it was not finished. · polish: None.
**Gaps:** No description, repo, demo or video
Sources: https://devpost.com/software/monkey-c

---

### MoodWave
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A Streamlit dashboard that simulates social posts and call emotions, labels them happy, frustrated or neutral with a keyword classifier, and shows a Happiness Index, trendline, city heatmap, anomaly alerts and a call-analysis consent panel.
**Problem / user:** T-Mobile service and customer-response teams that want to spot sentiment drops quickly.

**Features**
- Simulated data stream — Generates fake social posts, app feedback and call emotions refreshed every few seconds, because live API access was not available in time. *[shown_working]*
- Keyword sentiment classifier — Labels each message happy, frustrated or neutral by keyword matching. *[shown_working]*
- Customer Happiness Index — H = (happy minus frustrated) / total, ranging -1 to +1. *[shown_working]*
- Trendline and recent feed — Plotly line chart of the index over time with latest posts and calls. *[shown_working]*
- Geographic heatmap — Sentiment intensity by U.S. city. *[shown_working]*
- Anomaly alerts — Warns when the index drops sharply. *[shown_working]*
- Call-analysis consent panel — User chooses whether call data may be analyzed. *[shown_working]*
- Live Hume AI / Reddit / Twitter integration — Planned replacement of simulated data with real APIs and outage feeds. *[planned]*

**Flow:** Run streamlit app → Choose consent for call analysis → Watch the index, trendline and heatmap update → See alert when happiness drops

**Prompt:** T-Mobile challenge (as framed by entries): gauge customer sentiment from social and call data. No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (implied):** Builds a Happiness Index dashboard for T-Mobile teams; the README names T-Mobile users but no prize text is cited.  *(targeted: T-Mobile track)*
**AI:** Keyword-based sentiment classifier plus a simple drop detector; Hume AI emotion detection and real NLP are only future plans. Requirements list google-genai but it is unreferenced in the README.
**Architecture:** Single Streamlit app.py with pandas/numpy simulation, keyword classifier, index calculation and Plotly charts.
**Novelty:** Includes an explicit consent toggle for call analysis, uncommon in sentiment demos; otherwise a small simulated-data prototype.
**Scope:** tiny · working: One Python file of about 170 lines; runs locally; two Devpost screenshots; no live data. · polish: Plotly charts and mobile-friendly Streamlit layout; no tests or video.
**Claims:** Customer Happiness Index updates every few seconds | Simulation keeps the pipeline testable without live APIs
**Gaps:** All data simulated; Devpost wording on model vs keyword classifier is ambiguous; follows README
Sources: https://devpost.com/software/moodwave-wv3x8m, https://github.com/poojasrisundaresan/HackUTD (evidence file README)

---

### NAVI
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** An Electron/React desktop assistant meant to be controlled hands-free by voice and gestures, planning multi-step tasks such as summarizing a PDF and emailing it, using Nemotron for reasoning, Riva for speech, TensorRT for gesture tracking and ElevenLabs for spoken replies.
**Problem / user:** Desktop users juggling files and tabs, with explicit mention of people with limited mobility.

**Features**
- Voice commands — NVIDIA Riva ASR (README) captures spoken requests; Whisper appears in tags. *[claimed]*
- Gesture control — TensorRT-accelerated pose and gesture detection from a camera for common actions. *[claimed]*
- Natural-language task chaining — Nemotron plans multi-step workflows with live progress, e.g. summarize a PDF then email it. *[claimed]*
- File actions — Read, summarize, tag, move and share files. *[claimed]*
- App automation — Open, navigate, click and type in desktop apps. *[claimed]*
- Connectors — Gmail, Google Drive and Notion integrations. *[claimed]*
- Spoken responses — ElevenLabs text to speech. *[claimed]*
- Permission prompts — Privacy controls and prompts before sensitive actions. *[claimed]*

**Flow:** Say wake phrase and request, e.g. summarize this PDF and email it → NAVI reads the file and drafts a summary → It sends the email and reports progress by voice → Optionally control actions by gesture

**Prompt:** NVIDIA challenge as framed by entries: agentic multi-step workflows on Nemotron. No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (implied):** Uses Nemotron, Riva and TensorRT, with chained tasks; the README does not name a prize.  *(targeted: NVIDIA track)*
**Sponsor tools:** NVIDIA Nemotron (Reasoning and task planning, core); NVIDIA Riva (Low-latency speech recognition, core); TensorRT (Gesture and pose inference, core); ElevenLabs (Spoken replies, supporting)
**AI:** Nemotron plans actions from transcribed speech; vision pipeline runs pose estimation on TensorRT; TTS answers via ElevenLabs.
**Architecture:** Electron/React desktop app capturing mic and camera, sending speech to Riva and plans to Nemotron, then executing via Gmail/Drive/Notion connectors and OS automation.
**Novelty:** Pairs voice and gesture input with GPU-accelerated vision and an agent that acts across real apps, a heavy multimodal scope.
**Scope:** small · working: About 1.8k lines over 13 code files; README is largely the Devpost text and requires GPU, Riva server and OAuth; no demo shown. · polish: Setup guide present; no screenshots or video.
**Claims:** Real-time gesture control runs smoothly with TensorRT | Completes end-to-end workflows hands-free
**Gaps:** No video; claims of smooth FPS unquantified; README setup placeholder URL
Sources: https://devpost.com/software/navi-jp2be3, https://github.com/cheeky4life/navi (evidence file README)

---

### Nexus One
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A React and Firebase onboarding portal where clients, vendors and admins upload compliance documents such as SOC 2 reports, which Gemini analyzes to produce a compliance score, risk level, findings and an audit report.
**Problem / user:** Compliance reviewers and onboarding teams who manually read long vendor and client documents.

**Features**
- Role-based accounts — Signup and login for client, vendor and admin roles on Firebase. *[claimed]*
- Multi-document upload — Upload and categorize files with temporary storage during review and permanent storage after approval. *[claimed]*
- Gemini compliance analysis — Gemini reviews documents against internal standards, returning 0 to 100 score and issues. *[claimed]*
- Risk assessment — Assigns low, medium, high or critical risk levels. *[claimed]*
- Audit report generation — Automatically builds an audit report from findings. *[claimed]*
- Website chatbot — Planned but not completed per Devpost. *[planned]*

**Flow:** Sign up as client, vendor or admin → Upload compliance documents → Gemini analyzes them against standards → View score, risk level and findings → Admin approves for permanent storage

**Prompt:** No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (none):** No prize named. Gemini use could fit an MLH Gemini prize and the compliance theme resembles sponsor tracks, but neither source says so.  *(targeted: )*
**Sponsor tools:** Google Gemini API (Document compliance analysis and scoring, core)
**AI:** Gemini called from a TypeScript service layer to analyze uploaded documents and return a score, risk level and findings used to draft audit reports.
**Architecture:** Vite React frontend with services for Gemini, compliance, audit and users, backed by Firebase auth and storage.
**Novelty:** Workflow covers both vendors and clients with an audit-report output; repo carries unusually many status and setup documents.
**Scope:** medium · working: About 4k lines, tests present, extensive setup docs; no demo or video linked. · polish: Four screenshots, Spline and Figma design; many redundant docs.
**Claims:** Automated compliance verification producing a compliance score | Devpost lists Plaid and ComplyAdvantage but these appear only as learnings
**Gaps:** No demo video; Plaid/ComplyAdvantage integration unconfirmed; Devpost says React used for backend, likely an error
Sources: https://devpost.com/software/nexus-f7z2nk, https://github.com/ShalyJay/HackUTD-Nexus (evidence file README)

---

### On Your Terms
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A browser extension that spots links to terms of service and privacy policies, sends their content to an n8n workflow that scores how serious the terms are, shows key points in a side panel, and offers a Nemotron chat for follow-up questions.
**Problem / user:** Everyday web users who accept terms they never read; cites a Pew figure that 9% of U.S. adults always read privacy policies.

**Features**
- Policy link detection — Extension scans the current page and flags links to policies and terms. *[claimed]*
- Background analysis and score — Scraped text goes to an n8n endpoint, stored, analyzed, and a seriousness score returns. *[claimed]*
- Key-point side panel — Highlights the major points to consider in a side window. *[claimed]*
- Policy chat — One-on-one chat via LangChain with Nemotron, described as RAG, answers questions about the terms. *[claimed]*
- Per-user chatbot with history — Planned individualized memory. *[planned]*

**Flow:** Install extension and browse to a site → Extension flags policy links → Terms are analyzed in the background and scored → Read highlights in side panel → Chat with AI about specific clauses

**Prompt:** NVIDIA challenge as framed by entries: agentic workflows on Nemotron. No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (implied):** Uses Nemotron through LangChain inside an n8n automated workflow; prize target not stated.  *(targeted: NVIDIA track)*
**Sponsor tools:** NVIDIA Nemotron (Terms analysis and chat, core)
**AI:** Nemotron via LangChain scores and summarizes policy text and powers a RAG chatbot; orchestration is by an n8n workflow with Supabase storage.
**Architecture:** Manifest-based browser extension scrapes pages and posts to an n8n webhook that stores data in Supabase, calls LangChain/Nemotron and returns scores and chat replies.
**Novelty:** Low-code n8n workflow as the backend for an extension; practical everyday consumer angle.
**Scope:** small · working: About 6k lines across 57 code files; Devpost screenshots show the interface and n8n workflow; no video. · polish: Side-window UI and n8n canvas shots; no tests or setup guide.
**Claims:** Reads terms in minutes instead of hours | Team self-rated 10/10 on complexity and impact
**Gaps:** No video or live demo; Scoring method unspecified
Sources: https://devpost.com/software/on-your-terms, https://github.com/an-siuu-man/HackUTD-2025 (evidence file README, a copy of the Devpost text)

---

### OnboardIQ
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence C · confidence low*

**What it is:** A near-empty submission: the page has only a tagline about intelligence, security and efficiency and lists React; no product is described.
**Problem / user:** Not stated.

**Prompt:** not public / not found
**Fit (none):** No content to evaluate.  *(targeted: )*
**AI:** none
**Architecture:** 
**Novelty:** None; empty entry.
**Scope:** tiny · working: None. · polish: None.
**Gaps:** No description, repo, demo or video
Sources: https://devpost.com/software/onboardiq-9qt2ie

---

### Only Good Vibes
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** An embedded vibration monitor on an ESP32 with an MPU6050 accelerometer that trains an isolation forest on the device and flags anomalous vibration in real time.
**Problem / user:** Manufacturing operators facing costly machine downtime who need cheap condition monitoring.

**Features**
- Onboard anomaly detection — Isolation forest is trained and run on the ESP32 itself, not in the cloud. *[claimed]*
- Feature extraction — Computes kurtosis, RMS and variance from X, Y and Z acceleration. *[claimed]*
- Dual-core scheduling — FreeRTOS runs sampling on one core with timed ordering. *[claimed]*
- Anomaly warning — Issues a warning when an anomalous signal is seen. *[claimed]*
- Warning LED and drill test — Planned LED and testing on a handheld drill. *[planned]*

**Flow:** Device samples vibration to learn normal behavior → Isolation forest is built → Inference begins → Warning appears if an anomaly is detected

**Prompt:** No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (none):** No prize stated; a hardware project that could compete in Best Hardware, but not claimed.  *(targeted: )*
**AI:** Classical machine learning: an isolation forest trained on-device on kurtosis, RMS and variance features; no neural networks or LLMs.
**Architecture:** Adafruit MPU6050 feeds an ESP32 running Arduino C++ with FreeRTOS tasks for sampling, feature extraction, training and inference.
**Novelty:** Genuine on-device training on a tiny microcontroller, distinct from the cloud and LLM projects around it.
**Scope:** small · working: Devpost describes sampling, training and inference, but no repo, video or measurements; FFT features were dropped for memory. · polish: No screenshots or demo noted.
**Claims:** Runs sampling, training and inference in real time on a low-cost ESP32
**Gaps:** No repo, video or numbers; Page URL slug is a team-registration leftover; Not verified on hardware
Sources: https://devpost.com/software/team-registration-pas1cf

---

### PF Tracker
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A full-stack personal finance dashboard with transaction tracking across accounts, category budgets, card and subscription management, Auth0 login and a Gemini chat assistant that advises from the user's own transaction data.
**Problem / user:** Individuals with many accounts and cards who struggle to track spending and avoid unnecessary payments.

**Features**
- Dashboard and transactions — Income, expense and net worth overview with monthly transaction grouping and filtering. *[shown_working]*
- Category budgets — Monthly per-category budgets with visual progress indicators. *[claimed]*
- Card management — Add and manage credit and debit cards with balances. *[shown_working]*
- Subscription tracking — Tracks recurring payments with renewal reminders and unsubscribe options. *[claimed]*
- Gemini AI assistant — Backend fetches the user's transactions and sends them with the message to Gemini for advice. *[shown_working]*
- Auth0 login with 2-step verification — Email check against MongoDB accounts after Auth0 callback. *[claimed]*
- Bank data normalization — Converts differing bank transaction formats into one schema. *[claimed]*

**Flow:** Log in via Auth0 with 2-step verification → View dashboard and transactions → Set category budgets and add cards → Review subscriptions → Chat with the AI assistant for insights

**Prompt:** No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (none):** No prize stated; fintech theme fits finance sponsor tracks and Gemini use fits an MLH Gemini prize, but nothing confirms either.  *(targeted: )*
**Sponsor tools:** Google Gemini API (Financial insights chat assistant, core); Auth0 (Authentication with 2-step verification, supporting)
**AI:** Gemini API receives the user's transactions plus the question and returns spending insights; no other ML.
**Architecture:** React 19 frontend with Auth0 calls an Express API on MongoDB (Mongoose) that normalizes transactions and proxies prompts to Gemini.
**Novelty:** Conventional finance tracker; notable for working with normalized multi-bank data and a documented screenshot tour.
**Scope:** medium · working: About 6k lines, tests present, README with nine screenshots; bank API access was not achieved, so real accounts are not connected. · polish: Landing page, responsive styling and screenshot gallery; no video or live link.
**Claims:** Auth0 2-step verification protects financial data | Efficient conversion of each bank's transactions to one format
**Gaps:** Real bank connectivity not demonstrated; No video
Sources: https://devpost.com/software/pf-tracker, https://github.com/koolname99/hackUTD2025 (evidence file README)

---

### Placeholder
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence C · confidence low*

**What it is:** A placeholder submission whose title, description and tags all read Placeholder; no project exists.
**Problem / user:** Not stated.

**Prompt:** not public / not found
**Fit (none):** No content.  *(targeted: )*
**AI:** none
**Architecture:** 
**Novelty:** None; empty entry.
**Scope:** tiny · working: None. · polish: None.
**Gaps:** Page contains only the word Placeholder
Sources: https://devpost.com/software/mr-greenz

---

### PM_Ticket_Manager
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A PM tool where GPT-4o-mini assigns development tickets to developers based on workload, skills, experience, title and availability, with reasoning shown and an approve, deny or reassign step before assignments are saved.
**Problem / user:** Product managers who spend hours manually balancing ticket assignments across developers.

**Features**
- AI ticket assignment — GPT-4o-mini picks a developer per ticket using multiple parameters, processed in parallel threads. *[shown_working]*
- Transparent reasoning — Each suggestion carries an explanation. *[shown_working]*
- Approval workflow — PM approves or denies suggestions, then finalizes approved ones. *[shown_working]*
- Filters — Select ticket count, story point range and priority before assigning. *[shown_working]*
- Developer profiles — View assigned and rejected tickets and stats; reassign or remove. *[shown_working]*
- Charts — Recharts views of priority distribution, workload and due-date trends. *[shown_working]*
- SQLite persistence and audit history — Stores developers, tickets, assignments and history; CSV loaded at init. *[shown_working]*
- Jira/GitHub integration — Planned. *[planned]*

**Flow:** Load tickets and developers from CSV into SQLite → Set optional filters → Click Assign Tickets → Review AI suggestions with reasons → Approve or deny, then finalize → Inspect developer profiles and charts

**Prompt:** PNC challenge as quoted in sibling projects: AI-powered productivity for product managers across lifecycle phases. No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (implied):** README brands the UI with PNC colors and targets PM ticket workflow; Devpost does not name the prize.  *(targeted: PNC track)*
**AI:** Prompted GPT-4o-mini returns JSON assignments and reasons per ticket; prompt tuning needed for consistent JSON.
**Architecture:** React/Vite/Tailwind frontend calls a FastAPI backend with SQLAlchemy/SQLite and an AI engine module calling OpenAI.
**Novelty:** Human-in-the-loop approval and audit history around LLM assignment; PNC-branded UI.
**Scope:** medium · working: About 4.9k lines, documented endpoints and setup, sample CSVs of 40 tickets; no video or live link. · polish: Detailed README, charts and branding; no tests.
**Claims:** Fully functional AI-driven ticket system with transparent reasoning
**Gaps:** No demo video; Assignment quality not measured
Sources: https://devpost.com/software/ticket_manager, https://github.com/santib12/AI_Ticket_Manager (evidence file README)

---

### PMGenie
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A product manager dashboard that generates HTML mockups from prompts with Nemotron, edits them by AI instruction or code editor, stores them as past projects, and generates prioritized Jira tickets from a mockup compared with a GitHub repo.
**Problem / user:** Product managers, especially in regulated banking, who lose days on mockups, feedback cycles and manual ticketing.

**Features**
- Prompt-to-mockup — Nemotron produces HTML mockups after a two-step suggest-then-confirm chat, with iframe preview. *[claimed]*
- Context-aware generation — Uses existing mockups, chat history and GitHub README analysis to match project style. *[claimed]*
- AI and manual editing — Natural-language edit commands plus a syntax-highlighted code editor and auto-save. *[claimed]*
- Past Projects — SQLite stores mockups and edits shown in a grid. *[claimed]*
- Smart Jira tickets — AI compares mockup to repo and creates prioritized tickets with difficulty and acceptance criteria. *[claimed]*
- Jira board and chatbot access — View tickets, query status and assignees via the chat. *[claimed]*
- Auth0 login — Protects dashboard routes. *[claimed]*
- MCP server — README lists a Model Context Protocol server for GitHub-aware generation. *[claimed]*

**Flow:** Log in via Auth0 → Enter a prompt, confirm suggestions → Preview and refine mockup by AI or code → Save to Past Projects → Generate Jira tickets from the mockup

**Prompt:** PNC: AI-powered productivity for product managers (Prototyping and Testing phase). NVIDIA: intelligent agents with multi-step workflows beyond a single prompt. No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (explicit):** README has a section tying mockup generation to the PNC prototyping phase and the multi-step prompt-to-ticket workflow to the NVIDIA agents challenge.  *(targeted: PNC track, NVIDIA track)*
**Sponsor tools:** NVIDIA Nemotron (llama-3.3-nemotron-super-49b) (Mockup generation, editing, repo analysis and ticket generation, core); Auth0 (Login, supporting)
**AI:** Nemotron prompted for HTML generation, edits and structured ticket JSON, with chat history and repo README as context.
**Architecture:** React dashboard on Flask API (port 5001) with SQLite, calling NVIDIA API, Jira REST and GitHub REST; html2image makes previews.
**Novelty:** Chains design mockup to repository-aware Jira tickets in one flow, linking design and engineering handoff.
**Scope:** medium · working: About 7.3k lines, long README with architecture and setup, Devpost screenshots and an embedded YouTube video. · polish: Golden glassmorphism UI, detailed docs; no tests.
**Claims:** End-to-end workflow from vague idea to developer-ready Jira tickets | Chat-history context produced more relevant mockups
**Gaps:** Video not watched; Devpost lists React though it describes Tailwind and JavaScript
Sources: https://devpost.com/software/pmgenie, https://github.com/ParthBotre/hackutd_25 (evidence file README)

---

### PotionWatch
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A Flask and React tool for the EOG themed challenge that detects potion drain events from cauldron level data, compares daily totals with witch transport tickets and classifies mismatches; Devpost also describes a cauldron map and courier route optimization.
**Problem / user:** Operators auditing inventory flow who must reconcile measured drains against reported tickets and prevent overflow (an oil-flow analogue).

**Features**
- Drain event detection — Rate of change in levels with a std_multiplier threshold and min_duration yields drain start, end and volume. *[shown_working]*
- Discrepancy classification — Per cauldron and date: match, mismatch, ticket missing, drain not detected within a tolerance. *[shown_working]*
- Compare API — POST /compare takes a date range and parameters and returns summary and per-row results; GET /health. *[shown_working]*
- Discrepancy dashboard — React summary cards and a color-coded table with tunable parameters. *[shown_working]*
- Cauldron map — Shows cauldrons, neighbors, market travel times and live levels. *[claimed]*
- Time-series view with ticket times — Plots levels beside ticket submission times. *[claimed]*
- Courier route optimization — Plans witch routes to collect from cauldrons and deliver to the market without overflow. *[claimed]*

**Flow:** Start Flask backend and React dashboard → Choose dates and tolerance parameters → Dashboard calls /compare → Review summary cards and color-coded table

**Prompt:** EOG Resources track (as framed in winners' READMEs): potion cauldron dataset, reconcile transport tickets against drains, forecast overflow, plan pickup routes. No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (explicit):** README titled as an EOG sponsor challenge entry; implements ticket-versus-drain reconciliation, the core task; routing and forecasting are only described on Devpost.  *(targeted: EOG Resources track)*
**Sponsor tools:** EOG challenge Data/Tickets/metadata APIs (Source of potion levels and tickets, core)
**AI:** none
**Architecture:** React dashboard proxies to Flask (port 5003) which pulls /Data and /Tickets, uses Pandas for statistical drain detection and returns JSON.
**Novelty:** Purely statistical, explicit non-ML approach with configurable thresholds; README's category descriptions for match/mismatch appear swapped.
**Scope:** small · working: About 3k lines, API examples and sample response in README; no video or live link; route optimization not shown in README. · polish: Color-coded table and summary cards; no tests.
**Claims:** Dashboard with minimal hassle and clear results | Configurable tolerance, std_multiplier and min_duration
**Gaps:** Cauldron map and route optimization not in README; No screenshots in sources
Sources: https://devpost.com/software/potionwatch, https://github.com/Kartik11082/EOG-HackUTD25 (evidence file README)

---

### PrisM
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A product strategy platform with 14 LLM agents across five PM workflow stages, shown as an interactive ReactFlow graph, with branch exploration, convergence analysis and automatic Jira project and ticket creation for approved nodes.
**Problem / user:** Product managers and teams spending weeks coordinating, analyzing fragmented data and prioritizing from ideation to launch.

**Features**
- 14 specialized agents — Ideation, requirements, research, prototyping/testing and go-to-market agents each take context and give structured output. *[shown_working]*
- Interactive strategy graph — ReactFlow nodes show agent runs and relationships. *[shown_working]*
- Branch exploration — Runs parallel variations of an agent's output. *[claimed]*
- Convergence analysis — Synthesizes branches into one recommendation. *[claimed]*
- Jira integration — Creates a project per feature and tickets when nodes are approved. *[claimed]*
- Feature dashboard — Create and track features by name and problem statement. *[claimed]*
- Auth0 login — Protects the app. *[shown_working]*

**Flow:** Create a feature with a problem statement → Jira project auto-created → Run agent nodes in the graph → Review outputs, run branches → Approve nodes to create Jira tickets

**Prompt:** PNC: AI productivity across product management lifecycle phases; NVIDIA: agentic multi-step workflows. No public sponsor challenge text for HackUTD 2025 (statements were in the kickoff hackerpack).
**Fit (implied):** Agent categories map to PM lifecycle phases (including Prototyping and Testing) and use Nemotron; prizes not named in sources.  *(targeted: PNC track, NVIDIA track)*
**Sponsor tools:** NVIDIA API endpoints / Nemotron (LLM calls for all agents, core)
**AI:** FastAPI runs prompt-driven agents through an OpenAI-compatible client on NVIDIA endpoints; outputs are structured and chained, with branching and a convergence step.
**Architecture:** React/TypeScript/ReactFlow/shadcn frontend with Auth0, FastAPI backend with Pydantic, JSON file storage and Jira REST v3.
**Novelty:** Models PM work as an explorable agent graph with branching, broader than a single assistant.
**Scope:** medium · working: About 8.5k lines across 39 code files, setup steps and usage walkthrough; seven captioned Devpost screenshots; no video. · polish: Graph UI with shadcn components; no tests or CI.
**Claims:** 14 specialized agents across five workflows | Automated Jira project and ticket creation
**Gaps:** No video; Agent output quality not shown
Sources: https://devpost.com/software/prism-l2nb54, https://github.com/Hawkings232/Prism (evidence file README)

---

### Prodigy
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A web workspace for project managers and student teams that aims to put task tracking, deadlines and live progress updates in one place. Built as a React front end with a Flask back end; the page calls it an almost fully functioning interface.
**Problem / user:** Project managers and student teams who juggle many separate collaboration tools and have no single shared space for tasks and deadlines.

**Features**
- Task tracking — Teams create and follow tasks inside a shared workspace. *[claimed]*
- Deadline awareness — A shared work space keeps everyone current on due dates. *[claimed]*
- Real-time progress updates — Updates reflect completion and progress; live updates are listed among the hard parts. *[unclear]*
- AI calendar automation — Goal of automating sprints and deadlines in the calendar; page lists AI as a challenge, not delivered. *[planned]*

**Flow:** Team opens the shared workspace → Adds and tracks tasks and deadlines → Sees progress updates as work completes

**Prompt:** not public / not found
**Fit (none):** Page names no prize or track; it is a general productivity tool.  *(targeted: )*
**AI:** No AI implemented per the Devpost page; AI calendar automation is only a goal.
**Architecture:** React (Vite) front end with custom CSS calls a Flask back end through Axios.
**Novelty:** Standard project-management pitch; the stated differentiator is consolidating collaboration tools into one interface.
**Scope:** small · working: Page claims an almost functioning interface; repo has about 24 code files and a boilerplate README. · polish: No demo, video or screenshots described; README is only a greeting.
**Gaps:** README is a greeting only, no feature content; no demo or video; track not stated
Sources: https://devpost.com/software/prodigy-3yvkpf, evidence/hackutd-hackutd-2025-prodigy.json

---

### ProductAI
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence low*

**What it is:** A full-stack platform meant to give product managers AI-assisted tools across the product lifecycle, covering market research, strategy and launch readiness. Built with a Django REST back end and a React/TypeScript front end; the page gives few concrete feature details.
**Problem / user:** Product managers who need one platform instead of scattered tools for research, strategy and launch planning.

**Features**
- Market research assistance — AI tooling for research; the page gives no mechanism. *[unclear]*
- Strategy assistance — AI help with product strategy; no detail provided. *[unclear]*
- Launch readiness assistance — AI support for launch preparation; no detail provided. *[unclear]*
- User authentication, expanded API, deployment — Listed as upcoming work. *[planned]*

**Prompt:** not public / not found
**Fit (none):** No prize or track stated; a general productivity project.  *(targeted: )*
**AI:** Page says it leverages AI but names no model or service.
**Architecture:** Django REST framework API backend consumed by a React/TypeScript front end built with Vite.
**Novelty:** Aims to cover the whole product lifecycle in one app; description stays high level.
**Scope:** small · working: Page says a full-stack app was built, but no repo, demo or screenshots are given. · polish: None visible; authentication and database models are still listed as next steps.
**Gaps:** no repo linked; no demo or video; features described only in general terms
Sources: https://devpost.com/software/productai

---

### ProToyotaAI
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A React web app that helps shoppers choose a Toyota. A chatbot asks about budget, family size and driving purpose and recommends models, alongside a catalog, side-by-side comparison, finance calculator and dealership finder. The chatbot calls OpenRouter.
**Problem / user:** Car shoppers overwhelmed by many models, features and jargon who want guidance like a dealership specialist.

**Features**
- AI chat advisor — Chatbot asks targeted questions and recommends Toyota models; recommended cars are highlighted green and scrolled into view. *[claimed]*
- Vehicle catalog — Browse all models from local JSON data, with search by category. *[claimed]*
- Two-car comparison — Side-by-side specs with indicators for which vehicle is better. *[claimed]*
- Finance calculator — Monthly payment from down payment, interest rate and loan term. *[claimed]*
- Dealership locator — Finds nearby Toyota dealerships for a chosen vehicle. *[claimed]*
- Expert review data — Shows 2024 review ratings, pros and cons per model. *[claimed]*
- UI polish — Light/dark mode, responsive layout, slide page transitions and animated home page. *[claimed]*

**Flow:** Answer chatbot questions on budget, family and use → Receive recommended models → Browse catalog or search by category → Compare two vehicles → Estimate monthly payments → Find a nearby dealership

**Prompt:** not public / not found
**Fit (implied):** Toyota-focused car-shopping helper with finance calculator; page lists no prize.  *(targeted: Toyota Financial Services track (implied))*
**AI:** Chatbot logic and API calls live in a service module and use OpenRouter; page does not name the model.
**Architecture:** Create React App front end with components, pages and context; car data in local JSON; chatbot service calls OpenRouter; calculators run client side.
**Novelty:** Conversational model recommendation combined with finance and dealer tools; a fairly common car-advisor pattern.
**Scope:** small · working: README gives full feature list and setup; about 2.7k lines of code, no live demo. · polish: Dark mode, transitions and responsive layout described; README warns the client-side API key is public.
**Gaps:** no video or live demo; track not stated; repo name differs from Devpost slug (findmytoyota)
Sources: https://devpost.com/software/findmytoyota, evidence/hackutd-hackutd-2025-protoyotaai.json

---

### PulseLink
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A five-platform Apple app (Watch, iPhone, iPad, Mac, Vision Pro) that shares technicians' live heart rate, oxygen and energy data alongside a work-order system and Gemini troubleshooting help, aimed at data center staff.
**Problem / user:** Data center technicians and managers: monitoring tracks systems but not the physical state of the people maintaining them.

**Features**
- Live vitals sharing — Watch reads heart rate, oxygen and energy via HealthKit and sends them to the iPhone over WatchConnectivity; iPhone relays via MultipeerConnectivity. *[shown_working]*
- Work order management — Create, prioritize and track maintenance tickets in the iPhone app. *[shown_working]*
- Gemini troubleshooting — Gemini API answers hardware questions and suggests repair steps during incidents. *[shown_working]*
- Large-format dashboard — iPad and Mac view all active technicians and their metrics. *[claimed]*
- Vision Pro spatial dashboard — Immersive visionOS view of technician status and tasks. *[shown_working]*
- Animated employee card — Per-technician card shown in a README demo GIF. *[shown_working]*

**Flow:** Launch app and grant health permissions → Set a name → View and open work orders → Create a new work order → Watch devices share technician vitals → Ask Gemini for troubleshooting help

**Prompt:** not public / not found
**Fit (implied):** Combines technician health telemetry with work-order tracking, matching the data-center technician and ticketing theme.  *(targeted: Northmark (NMC) data-center technician challenge (implied))*
**AI:** Gemini API embedded in the iOS app for contextual troubleshooting and emergency guidance.
**Architecture:** watchOS collects HealthKit data to iPhone hub; iPhone distributes via MultipeerConnectivity to iPad, Mac and Vision Pro, hosts SwiftUI work orders and Gemini calls.
**Novelty:** Covers five Apple platforms including visionOS in 24 hours and pairs wearable biometrics with ticketing.
**Scope:** medium · working: README shows demo GIFs and screenshots; native Swift projects for several targets, about 4.4k lines. · polish: Neumorphic UI, animated cards, multi-device screenshots; no tests.
**Claims:** Built across five Apple platforms in 24 hours
**Gaps:** no demo video; no prize stated; Devpost lists AVFoundation, Speech, FoundationDB without explaining use
Sources: https://devpost.com/software/pulselink-0bliud, evidence/hackutd-hackutd-2025-pulselink.json

---

### PulseScore
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A bot-based ticketing system for telecom support that scores customer sentiment live during chat conversations and flags the ticket when frustration appears, with a dashboard blending network health data.
**Problem / user:** Telecom support teams: customers hit network issues, and companies want sentiment and network health in one place to respond faster.

**Features**
- Live sentiment scoring — OpenAI analyzes the customer conversation in real time. *[claimed]*
- Auto-flag tickets — Ticket flagged when frustration or negative sentiment is detected. *[claimed]*
- Real-time chat — Socket.IO powered customer chat. *[claimed]*
- Network health data — Pulls from the Internet Health Report to track network performance. *[claimed]*
- Live graphs dashboard — System dashboard with real-time charts; screenshots show AI analysis and forum ticket views. *[claimed]*

**Flow:** Customer chats with the bot → AI scores sentiment during the conversation → Frustrated conversations are flagged as tickets → Staff review the dashboard

**Prompt:** not public / not found
**Fit (implied):** Combines customer sentiment with network health for a telecom, fitting the T-Mobile happiness theme.  *(targeted: T-Mobile track (implied))*
**AI:** OpenAI model (unnamed) classifies sentiment from conversations; no other ML described.
**Architecture:** React/Tailwind front end; Node/Express with Socket.IO and MongoDB; OpenAI for sentiment; Internet Health Report for network data.
**Novelty:** Pairs per-conversation sentiment flagging with a network health feed.
**Scope:** small · working: Page lists five captioned screenshots but no repo, demo or video. · polish: Unknown; no walkthrough.
**Gaps:** no repo linked; no demo or video; extent of network alerts unclear
Sources: https://devpost.com/software/pulsescore

---

### PulseWire
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A dashboard that streams customer feedback, runs sentiment analysis and surfaces spikes in complaints or praise for product managers, with a login page. React client and FastAPI server using TextBlob.
**Problem / user:** Product managers who track sales and usage but rarely use emotional customer feedback across platforms.

**Features**
- Live feedback stream — Feedback is processed by the server and shown on a live dashboard. *[claimed]*
- Sentiment classification — TextBlob classifies each response; results return as JSON. *[claimed]*
- Spike detection — Highlights surges in complaints or praise. *[claimed]*
- Actionable AI insights — AI used as a co-pilot for analysis; details thin. *[unclear]*
- Authentication — Login/sign-up page secures data per user. *[claimed]*

**Flow:** Sign up or log in → Feedback streams in → Sentiment is analyzed → Spikes show on the dashboard

**Prompt:** not public / not found
**Fit (implied):** Real-time customer sentiment dashboard in the T-Mobile happiness style; no prize named.  *(targeted: T-Mobile track (implied))*
**AI:** TextBlob sentiment classifier; requirements also include scikit-learn and huggingface_hub; page mentions AI as co-pilot.
**Architecture:** React/MUI/Recharts client calls a FastAPI server with SQLAlchemy and JWT auth, which runs sentiment analysis and returns JSON.
**Novelty:** Basic sentiment dashboard; uses lightweight TextBlob instead of an LLM.
**Scope:** small · working: Repo has client and server and about 3.4k lines with tests; page says proof of concept. · polish: No README, demo or screenshots.
**Gaps:** repo has no README; no demo or video; feedback data source not named
Sources: https://devpost.com/software/pulsewire, evidence/hackutd-hackutd-2025-pulsewire.json

---

### Raven
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A wearable assistant on an M5GO ESP32 device that watches temperature, humidity and noise around a data center technician, warns when thresholds are exceeded, and uses Gemini to turn long server documentation into step-by-step task lists.
**Problem / user:** Data center technicians working in loud, hot, unpredictable spaces who must follow dense technical documentation.

**Features**
- Environmental sensing — M5GO reads temperature, humidity and sound level and streams to a backend over USB serial. *[shown_working]*
- Threshold alerts — Red warning light and alerts when heat or noise pass limits (README example above 90F or 85 dB). *[shown_working]*
- Noise exposure warning — Monitors prolonged high-decibel exposure. *[claimed]*
- Gemini step lists — Gemini 2.0 Flash summarizes server documentation into procedural steps. *[shown_working]*
- Device step navigation — Forward and back buttons move between steps; ticket marked complete from the interface. *[claimed]*
- Streamlit dashboard — Plots live sensor data, shows alert and step logs, allows log download. *[shown_working]*
- Doc-to-task pipeline — New documentation automatically becomes a Gemini task list. *[claimed]*

**Flow:** Technician wears the M5GO → Device shows sensor status and red light when unsafe → Documentation is summarized into steps → Technician steps through tasks with buttons → Ticket marked done; dashboard logs data

**Prompt:** not public / not found
**Fit (implied):** Hardware wearable plus Gemini guidance for data center technicians; Devpost lists no prize.  *(targeted: Northmark (NMC) data-center technician challenge, Gemini API (MLH))*
**Sponsor tools:** Gemini API (Summarizing server documentation into step-by-step instructions, core)
**AI:** Gemini 2.0 Flash through the FastAPI backend condenses documents (tested on a 96-page NVIDIA GB200 NVL72 manual) into ordered steps.
**Architecture:** M5GO MicroPython streams sensor data via USB to a reader script, which feeds a FastAPI backend that applies thresholds, logs events and calls Gemini; Streamlit shows results.
**Novelty:** Combines IoT body-worn sensing with LLM documentation summarization on a small ESP32 device.
**Scope:** small · working: Four captioned screenshots on Devpost; 12-file repo with run instructions and device code. · polish: Basic; Wi-Fi blocked so USB and hotspot used; vibration alerts still planned.
**Claims:** Tested summarization on a 96-page NVIDIA server manual
**Gaps:** no video; no prize stated
Sources: https://devpost.com/software/raven-71m3uk, evidence/hackutd-hackutd-2025-raven.json

---

### Read the Room
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A T-Mobile customer intelligence dashboard that pulls Reddit, X, Trustpilot reviews and DownDetector outages, scores call transcripts with Gemini, and presents everything on a unified executive dashboard.
**Problem / user:** T-Mobile customer service teams and executives facing a flood of unstructured feedback across channels.

**Features**
- Social ingestion — Reddit via PRAW and X via Tweepy with backoff, dedup and retries. *[claimed]*
- Review classification — Trustpilot reviews scraped and tagged with zero-shot BART for issues, churn risk and sentiment. *[claimed]*
- Call transcript scoring — Gemini 2.5 Flash returns schema-constrained sentiment label, -1 to 1 score and CSAT 1-5 for 500+ transcripts. *[claimed]*
- Accuracy evaluation — scikit-learn MAE, RMSE, correlation and confusion matrices for the CSAT predictions. *[claimed]*
- Outage intelligence — Headless DownDetector scraping, geographic mapping, priority queue and cached snapshots. *[claimed]*
- Executive dashboard — Unified feed with cycling stats matrix and trend charts using TanStack Query caching. *[claimed]*

**Flow:** Sources are ingested and cached → Models classify reviews and transcripts → Executive opens dashboard → Reviews trends, outages and feeds

**Prompt:** not public / not found
**Fit (implied):** Turns unstructured feedback from many channels into sentiment insight for T-Mobile, matching the customer-happiness theme.  *(targeted: T-Mobile track (implied))*
**Sponsor tools:** Google Gemini 2.5 Flash (Scoring call transcripts, core)
**AI:** BART-large-mnli zero-shot labels reviews; Gemini 2.5 Flash with schema-constrained JSON scores transcripts; scikit-learn evaluates.
**Architecture:** React/TypeScript/ShadCN dashboard with TanStack Query over a FastAPI backend using Pandas, scrapers and APIs plus time-windowed caches.
**Novelty:** Four different signal sources plus transcript evaluation against ground truth, unusually broad pipeline.
**Scope:** large · working: About 20k lines, backend and frontend plus testing folder; detailed README. · polish: Rich README and caching; no demo link or video; five unlabeled screenshots.
**Claims:** 85-95% multi-label review accuracy | about 95% churn detection | processed 500+ transcripts | social sentiment leads tickets by 24-48 hours
**Gaps:** accuracy measurement method not given; no demo or video; Devpost and README closely match
Sources: https://devpost.com/software/cool-project-w4h7ob, evidence/hackutd-hackutd-2025-read-the-room.json

---

### Reflex Work Order Automation
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A system that turns Jira maintenance tickets into guided work orders for GPU data centers, backed by a two-layer agentic RAG pipeline (OpenAI embeddings plus Nemotron generation) and a React dashboard with chat.
**Problem / user:** Datacenter engineers and technicians: filing Jira tickets is tedious, work orders take months, and downtime wastes thousands of dollars of GPU time daily.

**Features**
- Jira to work order — Converts tickets into step-by-step work orders and marks issues done in Jira. *[claimed]*
- Agentic RAG — Embedding layer over specs, tickets and notes, plus Nemotron generation of maintenance instructions. *[claimed]*
- Dashboard and detail views — React views for work orders, a detail page and a chat interface. *[claimed]*
- Work Order API — Documented with Swagger, along with RAG endpoints. *[claimed]*
- Existing workflow integration — Works within Jira so engineers keep their process. *[claimed]*

**Flow:** Maintenance issue filed in Jira → Reflex builds a work order → Technician follows guided steps → Issue marked complete in Jira

**Prompt:** not public / not found
**Fit (implied):** Automates data-center maintenance work orders using Nemotron on Brev, matching the Northmark and NVIDIA challenges.  *(targeted: Northmark (NMC) technician work-order challenge, NVIDIA Nemotron)*
**Sponsor tools:** NVIDIA NIM / Nemotron (Generative layer producing maintenance instructions, core); NVIDIA Brev (GPU deployment, supporting)
**AI:** Dual-layer agentic RAG orchestrated with LangGraph: OpenAI embeddings of multimodal inputs, then Nemotron via NIM generates guidance.
**Architecture:** React/Vite front end; FastAPI Python 3.13 backend with LangGraph agentic RAG and Jira REST integration; Nemotron on Brev.
**Novelty:** Combines Jira integration with an agentic RAG pipeline; original scope also covered cable optimization and edge devices.
**Scope:** medium · working: Repo has frontend, backend, agenticRAG and nemotron folders with tests; Devpost shows dashboard and Swagger screenshots. · polish: README is just the word initial; no demo or video.
**Gaps:** README essentially empty; no demo or video; no measured results
Sources: https://devpost.com/software/reflex-work-order-automation, evidence/hackutd-hackutd-2025-reflex-work-order-automation.json

---

### RideOracle
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A Toyota car-finder web app where a 10-question quiz yields a deterministic compatibility score per vehicle, with review sentiment, a finance/lease calculator, up-to-three-car comparison and an inventory chatbot.
**Problem / user:** First-time and cost-conscious car buyers who bounce between dealer sites, loan calculators and review forums.

**Features**
- Preference quiz — 10 questions on use, priorities, features, fuel, passengers, budget and driving style. *[claimed]*
- Match score — Deterministic scoring (not LLM) per vehicle, with explanations of fit. *[claimed]*
- Review sentiment — VADER scores real Toyota reviews gathered with a Selenium scraper. *[claimed]*
- Comparison — Side-by-side view of up to 3 cars. *[claimed]*
- Finance and lease calculator — APR based on credit score. *[claimed]*
- Inventory chatbot — OpenRouter-backed assistant with vehicle data context. *[claimed]*

**Flow:** Take the quiz → Backend scores vehicles → See ranked matches with sentiment → Compare cars and run finance calculator → Ask chatbot questions

**Prompt:** not public / not found
**Fit (implied):** Car shopping aid with finance calculator for Toyota buyers; no prize on page.  *(targeted: Toyota Financial Services track (implied))*
**AI:** VADER sentiment on scraped reviews; page also mentions a small neural net with sigmoid; README stresses deterministic scoring; chatbot via OpenRouter.
**Architecture:** Next.js 15 front end posts quiz data to a FastAPI model server with data pipeline; chatbot uses OpenRouter.
**Novelty:** Pairs explainable numeric match scoring with sentiment and finance rather than a chat-only advisor.
**Scope:** medium · working: About 11k lines with frontend and backend folders and a detailed feature README; no demo link. · polish: Framer Motion animations, finance calculator; no tests.
**Gaps:** Devpost describes a neural net while README says deterministic scoring; no demo or video
Sources: https://devpost.com/software/rideoracle, evidence/hackutd-hackutd-2025-rideoracle.json

---

### Satisfaction Visual Analytics (SAM)
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A web dashboard of Tableau visualizations of T-Mobile customer happiness drawn from seven survey questions, aimed at a Customer Experience Leader, with login, a profile page, data visuals and geographic analytics.
**Problem / user:** T-Mobile customer experience leaders who need survey responses turned into readable visuals.

**Features**
- Login for CX leader — Entry page for the leader's dashboard. *[claimed]*
- Profile setup — First dashboard page for setting up the profile. *[claimed]*
- Interactive Tableau visuals — Page of figures for seven core survey questions highlighting satisfaction trends. *[claimed]*
- Geographic analytics — Third page maps customer happiness by area. *[claimed]*

**Flow:** Log in → Set up profile → Explore interactive visuals → View geographic analytics

**Prompt:** not public / not found
**Fit (implied):** Visualizes customer happiness survey data for T-Mobile.  *(targeted: T-Mobile track (implied))*
**AI:** Survey dataset was synthesized with GenAI; AI analysis is a future step.
**Architecture:** HTML/CSS/JavaScript pages embedding Tableau dashboards over a JSON dataset; run locally with Node.
**Novelty:** Beginner-friendly Tableau approach; synthetic data.
**Scope:** tiny · working: Page describes three-page flow; repo has about 850 lines and README is just a title. · polish: No screenshots, video or live link.
**Gaps:** README is only a title; no demo or video; dataset is AI-generated
Sources: https://devpost.com/software/t-mobile-customer-happiness-index-edc5y9, evidence/hackutd-hackutd-2025-satisfaction-visual-analytics.json

---

### SentimentRadar
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A dark-themed Next.js dashboard with a US heatmap of customer happiness by region, trend views and an agent-style diagnostic flow that proposes resolution recommendations for telecom teams. The README notes the Nemotron agent is simulated with rules.
**Problem / user:** Telecom customer service and operations teams that react late to satisfaction problems and want regional, proactive visibility.

**Features**
- Happiness heatmap — Leaflet map colors US regions by happiness score. *[claimed]*
- Sentiment aggregation — Aggregated sentiment from several sources stored in Supabase, with HuggingFace sentiment and fallback. *[claimed]*
- Diagnostic agent — Multi-step workflow diagnoses issues and recommends fixes; README says simulated with rule-based logic, Nemotron optional. *[claimed]*
- Auto-refresh and trends — Data refreshes every 30 seconds with trend and spike tracking. *[claimed]*
- Customer update drafts — Real-time generation of customer-facing updates. *[claimed]*

**Flow:** Open the heatmap → Spot low-happiness regions → See trends and spikes → Read AI diagnostics and recommended actions

**Prompt:** not public / not found
**Fit (implied):** Regional happiness dashboard with a Nemotron-style diagnostic agent for a telecom.  *(targeted: T-Mobile track, NVIDIA Nemotron (implied))*
**Sponsor tools:** NVIDIA Nemotron (Diagnostic agent; README says simulated with rules, optional API key, supporting); Supabase (Data storage, supporting)
**AI:** HuggingFace API sentiment with fallback; Nemotron agent for multi-step diagnosis, rule-simulated unless an NVIDIA key is set.
**Architecture:** Next.js 14 front end with Leaflet; Next.js API routes over Supabase PostgreSQL; seed script and migration.
**Novelty:** Map-first happiness view with an agent-style diagnosis step; automated ticketing planned.
**Scope:** medium · working: About 4.6k lines with seed script and setup; one screenshot on Devpost. · polish: Setup docs good; no demo or video.
**Gaps:** Nemotron simulated per README; no demo or video
Sources: https://devpost.com/software/sentimentradar, evidence/hackutd-hackutd-2025-sentimentradar.json

---

### ShelfSense
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A food-waste app: scan a grocery receipt with OCR to fill a virtual fridge, track expiry, and get recipes built around items nearing expiration from NVIDIA Nemotron, with a FastAPI backend and an in-progress Expo app.
**Problem / user:** Households that throw out food because they forget what they have or cannot work out how to use it.

**Features**
- Receipt scanning — OCR.space reads receipts and fills the virtual fridge via /scan/receipt. *[claimed]*
- Inventory tracking — SQLite stores items, quantities, expiry dates and remaining shelf life, with CRUD endpoints. *[claimed]*
- Expiry detection — Flags items with 25% or less shelf life left. *[claimed]*
- AI recipes — Nemotron Llama 3.3 49B on NVIDIA NIM writes recipes using expiring items as JSON. *[claimed]*
- Recipe fallback — API-Ninjas supplies recipes if generation fails. *[claimed]*
- Notifications and recommendations — Endpoints for recipes and expiring items; screenshots show notifications. *[claimed]*

**Flow:** Scan receipt after shopping → Review parsed items → Inventory tracks expiry → App flags items near expiry → Receive recipe suggestions

**Prompt:** not public / not found
**Fit (implied):** Uses Llama-3.3-Nemotron on NIM for recipe generation; README frames it as leveraging Nemotron.  *(targeted: NVIDIA Nemotron track (implied))*
**Sponsor tools:** NVIDIA NIM / Nemotron (Recipe generation, core)
**AI:** Nemotron Llama 3.3 49B prompts for varied recipes from expiring items with JSON output; OCR.space parses receipts.
**Architecture:** Expo React Native front end (in progress); FastAPI with receipt, inventory and recommendation modules over SQLite via SQLAlchemy; external OCR, NIM and recipe APIs.
**Novelty:** Zero-input flow from receipt to expiring-item recipes with percent-shelf-life rule.
**Scope:** medium · working: Screenshots of scanning, inventory, recommendations; about 3.8k lines; Swagger docs. · polish: Logo, screenshots; frontend marked in progress; no video.
**Gaps:** no video; no quantified results
Sources: https://devpost.com/software/foodconcious, evidence/hackutd-hackutd-2025-shelfsense.json

---

### Snitch the Witch
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A potion-themed logistics dashboard for the EOG challenge: it compares expected and actual cauldron levels, audits unlogged drains, forecasts overflow, and plans courier pickup routes, with a live demo site.
**Problem / user:** Operators of a potion network, an analogue for oil operations, facing mismatched tank readings, delayed pickups and untracked flows.

**Features**
- Discrepancy graphs — Interactive charts of actual versus expected cauldron drops. *[claimed]*
- Audit reports — Per-cauldron summary of unlogged drains with affected tickets and courier actions. *[claimed]*
- Network playback — Real-time visualization of fills and transports with timestamps and speed controls. *[claimed]*
- Overflow forecast — Time to overflow with high/medium/low risk, using random forest rate estimates. *[claimed]*
- Route optimization — OR-Tools timeline-based courier routes and plans showing couriers required. *[claimed]*
- Alerts — Real-time flags for suspicious activity. *[claimed]*

**Flow:** Land on dashboard → Inspect discrepancy graph per cauldron → Open audit report and witch flags → View overflow forecast → Generate route plan → Watch network playback

**Prompt:** not public / not found
**Fit (explicit):** Reconciles transport tickets with drain levels, forecasts overflow and plans routes, matching the EOG framing the page cites.  *(targeted: EOG Resources challenge (Lost in the Pages))*
**AI:** Scikit-learn random forest estimates fill/drain rates and overflow; OR-Tools for routing; page also mentions an MLP and VRPNet.
**Architecture:** React/TypeScript/Recharts dashboard over the challenge API with Prophet and optimization services in Python.
**Novelty:** Combines anomaly auditing, forecast and routing in one themed dashboard.
**Scope:** medium · working: Live demo site, YouTube video and about 10k lines. · polish: Seven captioned screenshots; README is a generic dashboard guide.
**Claims:** Reduces total work time by up to 25% | Operators said monitoring is faster and more reliable
**Gaps:** README does not mention forecast or audit features; 25% claim unsupported; no prize shown
Sources: https://devpost.com/software/brew-logic, evidence/hackutd-hackutd-2025-snitch-the-witch.json

---

### Sync
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** An adaptive AI concept for T-Mobile that combines customer sentiment and network health, uses multiple agents to detect anomalies, predict problems and simulate repair plans, and shows results on a landing page and dashboard.
**Problem / user:** T-Mobile network operations and customer-experience teams that want to sense issues before customers complain.

**Features**
- Stream monitoring — Watches reviews, network metrics and APIs including Reddit. *[claimed]*
- Anomaly detection and prediction — Agents flag sentiment or performance anomalies and predict issues. *[claimed]*
- Repair simulation — Simulates fix options and picks a plan before human action. *[claimed]*
- Multi-agent workflow — Eight agents in README, with a governing agent prioritizing actions. *[claimed]*
- Dashboard — Heatmaps, trend graphs, churn and regional performance indicators. *[claimed]*
- Agentic RAG and ReAct — Context retrieval and reason-act loops. *[claimed]*

**Flow:** Open landing page → Go to /dashboard → See live sentiment and network health → Review predicted issues and simulated repairs

**Prompt:** not public / not found
**Fit (implied):** Inspiration cites an NVIDIA challenge for agents that plan and act; applied to T-Mobile network repair.  *(targeted: NVIDIA reasoning-agent challenge, T-Mobile track)*
**Sponsor tools:** NVIDIA Nemotron / Brev (Agent reasoning and GPU simulation per Devpost; README lists Gemini with NIM support, unclear)
**AI:** Multi-agent ReAct with agentic RAG; Devpost cites Nemotron, README Gemini default with NVIDIA NIM option.
**Architecture:** React 19/Vite dashboard with Node/Express TypeScript backend hosting eight agents; PostgreSQL listed.
**Novelty:** Frames a self-healing network via a governing agent over specialist agents.
**Scope:** large · working: About 12k lines; README gives quick start; GIF and landing screenshot only. · polish: Dark pink/purple theme; root src is an old landing page.
**Gaps:** Devpost says Nemotron, README says Gemini; autonomous healing probably aspirational; no video
Sources: https://devpost.com/software/sync-ai-gltbhz, evidence/hackutd-hackutd-2025-sync.json

---

### T-Care
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** An AI customer-care site for T-Mobile combining a VAPI voice agent, webcam-based emotion and sentiment sensing that adapts the page, a coverage map, SMS outage updates and an admin dashboard with competitor analysis.
**Problem / user:** Telecom customers frustrated by tickets, long calls and store visits, and the support teams serving them.

**Features**
- Voice support agent — VAPI-based conversational agent for customer issues. *[claimed]*
- Sentiment-adaptive UI — Computer vision infers sentiment and the agent adjusts tone and page content. *[claimed]*
- Feedback loop — Sentiment data returns to the business. *[claimed]*
- Admin competitor analysis — Parallel AI and Gemini scrape the web to compare feedback with competitors. *[claimed]*
- Coverage and outage map — Mapbox map of outages and reported problems. *[claimed]*
- SMS and Telegram alerts — Email/Telegram services send tower status and SOS notices. *[claimed]*

**Flow:** Customer talks to the support AI → Sentiment detected, page adapts → Outage updates via SMS → Employee reviews admin dashboard

**Prompt:** not public / not found
**Fit (implied):** Agentic customer-care assistant for T-Mobile using Nemotron for vision sentiment.  *(targeted: T-Mobile track, NVIDIA Nemotron (implied))*
**Sponsor tools:** NVIDIA Nemotron (Vision sentiment analysis and central AI config, supporting)
**AI:** Nemotron CV sentiment, VAPI voice, Gemini and Parallel AI for competitive research; guardrails for hallucinated UI updates.
**Architecture:** Vite/React front end with Express backend providing WebSocket sentiment, decision engine and notifications; Supabase auth.
**Novelty:** Multimodal customer care where facial sentiment changes the interface.
**Scope:** large · working: About 31k lines, backend endpoints documented; no video or live demo. · polish: README describes admin tools; .next build included.
**Gaps:** README covers admin dashboard only; no video; tagline claims unexplained
Sources: https://devpost.com/software/t-care-4ynlev, evidence/hackutd-hackutd-2025-t-care.json

---

### T-Data
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A dashboard that scrapes Reddit and other social posts for consumer feedback, clusters reviews with Nemotron embeddings and K-Means, labels clusters and runs sentiment per query, and shows trends by location.
**Problem / user:** Businesses, especially T-Mobile, wanting to understand consumer opinion from scattered online posts.

**Features**
- Feedback scraper — Collects posts from Reddit and other platforms. *[shown_working]*
- Clustering — Nemotron embeddings plus K-Means group reviews, and two models label clusters. *[claimed]*
- Sentiment per query — Runs sentiment analysis for each query. *[claimed]*
- Dashboard views — Home page, trend line graph, location map and topic page. *[shown_working]*

**Flow:** Open home page → Query a topic → View trend line → Browse map → Open topic page

**Prompt:** not public / not found
**Fit (implied):** Consumer sentiment dashboard using Nemotron embeddings.  *(targeted: T-Mobile track, NVIDIA Nemotron (implied))*
**Sponsor tools:** NVIDIA Nemotron (Embeddings for clustering, core)
**AI:** Nemotron embeddings clustered with K-Means; two unnamed models label clusters and score sentiment.
**Architecture:** React/Tailwind front end over Flask backend with scraper and models.
**Novelty:** Topic clustering rather than only positive/negative scoring.
**Scope:** small · working: Four screenshots and scraper claimed collected data; repo has about 2.4k lines. · polish: Empty README; no demo.
**Gaps:** README empty; no demo or video; model names for labeling not given
Sources: https://devpost.com/software/t-data, evidence/hackutd-hackutd-2025-t-data.json

---

### T-Mobile Happiness Index
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A real-time dashboard that shows a Happiness Index, live sentiment feed, trend charts, alerts and a regional heatmap over streamed customer feedback, with FastAPI/MongoDB backend and optional Gemini enrichment service.
**Problem / user:** T-Mobile teams who see problems only after they spread online and need early sentiment-shift alerts.

**Features**
- Happiness Index — Score updates instantly as feedback arrives. *[claimed]*
- AI enrichment — Gemini/OpenAI return sentiment, topic, severity as JSON; falls back to neutral if unavailable. *[claimed]*
- Live feed and charts — WebSocket pushes feedback, alerts and scores without reload. *[claimed]*
- Alert engine — Flags negative shifts. *[claimed]*
- Regional heatmap — Updates dynamically with new feedback. *[claimed]*
- Mock generator — Script streams synthetic tickets. *[shown_working]*

**Flow:** Start backend and optional AI service → Seed with mock tickets → Open dashboard → Watch index, heatmap and alerts update

**Prompt:** not public / not found
**Fit (implied):** Real-time customer happiness index with alerts, matching the T-Mobile prompt.  *(targeted: T-Mobile track (implied))*
**Sponsor tools:** Google Gemini (AI enrichment of feedback, supporting)
**AI:** Gemini (and OpenAI per Devpost) classifies sentiment, topic and severity per ticket.
**Architecture:** React dashboard consumes FastAPI REST and /ws/reviews WebSocket; MongoDB persistence; separate AI service.
**Novelty:** Admin and user panels share a live pipeline; standard sentiment dashboard otherwise.
**Scope:** small · working: About 940 lines; README has setup for backend, AI service, mock data; one screenshot. · polish: Has tests; no demo or video.
**Gaps:** data is synthetic; no video
Sources: https://devpost.com/software/t-mobile-happiness-index-3szd41, evidence/hackutd-hackutd-2025-t-mobile-happiness-index.json

---

### T-Mobile Happy Assesment Dashboard
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A FastAPI plus React demo that colors a US state map by a T-Mobile sentiment score and shows details on hover. The Devpost text pitches a broader Happiness Index mixing feedback NLP and network metrics, but the repo only serves randomly generated mock scores.
**Problem / user:** T-Mobile wants a nationwide view of how customers feel, tied to network quality, to act early on trouble spots; no specific internal role is named.

**Features**
- State-level sentiment map — React map with state polygons colored by sentiment score, with hover tooltips showing state details. *[shown_working]*
- Mock sentiment API — FastAPI endpoints return per-state data, one state, summary stats; an endpoint regenerates random values. *[shown_working]*
- Summary statistics header — Aggregated stats shown at top of the page from the summary endpoint. *[shown_working]*
- Customer Happiness Index from feedback — Devpost says NLP over tweets, reviews and support messages yields regional and national index. *[claimed]*
- Network metrics fusion — Devpost says signal strength, latency and outages are combined with sentiment. *[claimed]*
- Alerts and heatmaps — Devpost claims alerts for areas of satisfaction or concern plus heatmaps. *[claimed]*

**Flow:** Start the FastAPI backend and Vite frontend locally → Open the map page → Hover over a state to see its sentiment details → Read the summary statistics at top → Call regenerate to reshuffle the mock data

**Prompt:** HackUTD 2025 T-Mobile sponsor track (customer happiness / sentiment). Challenge text not public; project pages frame it as building a Customer Happiness Index from customer feedback and network experience data.
**Fit (implied):** Presents a customer sentiment map and a happiness index concept; the working part is a mock-data map only, README says real scraping could be added later.  *(targeted: T-Mobile track (inferred from page title and content))*
**AI:** No AI in the repo (mock data). Devpost describes unspecified NLP sentiment analysis over social posts, reviews and support messages.
**Architecture:** React/Vite frontend with react-simple-maps and Tailwind calls a FastAPI backend that holds randomly generated per-state mock sentiment in memory; no database.
**Novelty:** Mock-data prototype built in roughly two hours per the README; the network-metrics plus sentiment index idea appears only in prose.
**Scope:** small · working: README gives runnable setup and endpoints for a mock-data map; no live data. · polish: Basic color-coded map with tooltips; no screenshots, demo or video.
**Claims:** README: fully functional, setup under 2 hours, realistic mock data | Devpost: analyzes thousands of posts (no method or result given)
**Gaps:** Devpost lists a wrong repo link; a team update points to this repo as the official one; No NLP or network-metric code evidenced; Prize challenge text not public
Sources: https://devpost.com/software/t-mobile-happy-assesment-dashboard, https://github.com/ArpitKhavate/t-mobile-happy (evidence README)

---

### T-Pulse
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A real-time dashboard that scores customer emotion toward T-Mobile with Google Cloud Natural Language and shows a US heatmap with a Happiness Index. Data is synthetic: AI-generated reviews streamed through a Redis/Celery pipeline over websockets.
**Problem / user:** T-Mobile lacks a live view of how customers feel across regions; target is teams who need to catch sentiment surges early.

**Features**
- Geo-emotion heatmap — Live US heatmap whose region colors update from the per-region Happiness Index as records arrive. *[shown_working]*
- Happiness Index scoring — Celery worker calls Google Cloud Natural Language for emotion classification, then aggregates by region. *[shown_working]*
- Simulated real-time ingestion — Synthetic reviews generated with generative AI flow as JSON into Redis Streams and out via websockets. *[shown_working]*
- Anomaly and surge flagging — System flags surges in frustration or delight so T-Mobile can act early. *[claimed]*
- Sentiment dashboard view — Separate dashboard view of sentiment metrics (per screenshot captions). *[shown_working]*
- Chatbot view — Screenshot caption shows a chatbot page; its behavior is not described. *[unclear]*
- Interactive globe UI — Teammate description mentions a globe visualization. *[claimed]*

**Flow:** Synthetic review JSON is queued in Redis → Enrichment worker scores emotion → Aggregation rolls scores into regional Happiness Index → Dashboard and heatmap update live over websockets → User browses heatmap, dashboard and chatbot views

**Prompt:** HackUTD 2025 T-Mobile sponsor track (customer happiness / sentiment). Challenge text not public; project pages frame it as building a Customer Happiness Index from customer feedback and network experience data.
**Fit (implied):** Delivers a customer Happiness Index and geographic emotion heatmap with anomaly flagging; network performance integration is listed as future work.  *(targeted: T-Mobile track (README/Devpost frame it as T-Mobile customer emotion analytics))*
**Sponsor tools:** Gemini API (Listed built-with tag; README only plans it to give actionable insights from the data, token)
**AI:** Google Cloud Natural Language API classifies emotion per review; generative AI creates synthetic reviews to simulate live traffic; Gemini listed for future insights.
**Architecture:** JSON stream to Redis Streams, Celery enrichment worker with NLP scoring, aggregation by region, FastAPI backend (with PostgreSQL/SQLAlchemy deps) pushing over websockets to a Next.js/shadcn frontend; Docker present.
**Novelty:** Streaming queue-and-worker pipeline for a sentiment demo, with synthetic data standing in for unavailable real data; team calls it their first live-stream system.
**Scope:** medium · working: README claims a working end-to-end pipeline; repo has ~2.5k LOC across backend and frontend with Docker. · polish: Three screenshots, branded UI via shadcn; no video or live link.
**Claims:** Fully functional real-time pipeline from ingestion to visualization | First time building a live stream system
**Gaps:** No demo video; Chatbot behavior undescribed; Challenge text not public
Sources: https://devpost.com/software/t-pulse, https://github.com/axdyv/T-Pulse (evidence README)

---

### T-Time
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence high*

**What it is:** An agentic RAG web app that scrapes T-Mobile talk from Reddit, Consumer Affairs and Threads into a Pinecone index and lets staff chat with it in plain English. It also has a generated metrics dashboard, a sentiment map and email alerts.
**Problem / user:** Customer sentiment about T-Mobile is spread across platforms; customer-experience teams want answers without writing SQL or building dashboards.

**Features**
- RAG chat over customer feedback — Query is embedded, top-20 Pinecone matches are injected with last 10 messages into the LLM for a grounded answer. *[shown_working]*
- Multi-source scraping and dedupe — Reddit (PRAW), Consumer Affairs and Threads normalized to one schema with MD5 deduplication; 40,000+ vectors claimed. *[claimed]*
- AI-generated metrics dashboard — Happiness index, sentiment trends and period comparisons computed from the data. *[claimed]*
- Global sentiment map — Gemini extracts locations from text, geocodes them, and map click shows local sentiment. *[claimed]*
- Sentiment classification — CardiffNLP Twitter-RoBERTa 3-class model replaced an SST-2 model that skewed negative. *[claimed]*
- Dual LLM serving with fallback — Nemotron-mini via Ollama on an A100 behind a FastAPI wrapper; Gemini is the fallback with retries. *[claimed]*
- Email alerts — Notifies teams on significant sentiment shifts; authors say found already in codebase. *[claimed]*
- Agent tools — Five tools exposed for Google ADK agents; MCP folder in repo. *[claimed]*

**Flow:** Sign in with GitHub OAuth or email/password → Ask a plain-English question in chat → System retrieves matching feedback and answers → Open metrics dashboard for happiness index and trends → Click a map location for regional sentiment

**Prompt:** HackUTD 2025 T-Mobile sponsor track (customer happiness / sentiment). Challenge text not public; project pages frame it as building a Customer Happiness Index from customer feedback and network experience data.
**Fit (implied):** Aggregates customer sentiment about T-Mobile from public sources into one chat-and-dashboard tool with a happiness index, the sponsor challenge theme.  *(targeted: T-Mobile track, NVIDIA (Nemotron tag))*
**Sponsor tools:** NVIDIA Nemotron-mini (Ollama on A100) (Primary LLM for chat answers and metric inference, core); Gemini API (Fallback LLM and location extraction, supporting)
**AI:** RAG: e5-base-v2 embeddings in Pinecone, top-20 retrieval, Nemotron-mini generation with Gemini fallback; RoBERTa sentiment classifier; Gemini location parsing; Google ADK agent tools.
**Architecture:** Next.js/tRPC client with Better Auth and Postgres (Drizzle); embedding FastAPI service, LLM FastAPI service on GPU, Pinecone, cron scrapers, MCP and botdas agent folders; Docker.
**Novelty:** Self-hosted GPU LLM with cloud fallback, three-source ingestion and an agent/MCP layer: broader than typical dashboard entries.
**Scope:** large · working: Live site at t-time.club listed; ~7k LOC across five services with Docker. · polish: Custom domain, auth, map and dashboard; no video; client README is the T3 template.
**Claims:** 40,000+ vectors indexed | 2-5 second query latency | 99.9% uptime with fallback (no method given) | Cold start cut from 120s to 30s | Zero duplicates across three platforms
**Gaps:** Repo README is boilerplate; features rest on Devpost text; Live site not opened; Challenge text not public
Sources: https://devpost.com/software/t-time, https://github.com/Lewin-B/T-Time (evidence; client README is template, details from Devpost and manifests)

---

### TaskLens
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A progressive web app where a user photographs a hands-on task setup and gets a safety-aware, ordered checklist with visual overlays. A vision model reads the photo and a second model plans the steps.
**Problem / user:** People attempting unfamiliar manual or hardware tasks find tutorials hard to follow for unconventional cases; aimed at the average person doing such tasks.

**Features**
- Photo task analysis — GPT-4 Vision looks at the submitted photo to infer the goal and identify components and their current state. *[claimed]*
- Safety hazard assessment — Image analysis output is used to flag hazards before steps are given. *[claimed]*
- Safest ordered task list — GPT-4o-mini, acting as an architect agent, turns the vision output into a chronologically optimized safe list. *[claimed]*
- Strict structured output — JSON schema enforces precise targets such as pin names and valve IDs for each step. *[claimed]*
- Canvas visual overlays — Frontend draws HTML Canvas overlays on the guide using the structured target data. *[claimed]*
- PWA delivery — Built as a progressive web app; FastAPI backend orchestrates the two AI agents. *[claimed]*
- Live video guidance — Replacing verification photos with a live video feed alongside the user. *[planned]*

**Flow:** User photographs the task setup → Vision model identifies components, state and hazards → Planner model produces ordered safest steps as strict JSON → Frontend overlays targets on the visual guide → User sends verification photos while progressing

**Prompt:** not public / not found
**Fit (none):** Page mentions trying NVIDIA Nemotron Nano agents and a live video API but not using them; no sponsor track is named.  *(targeted: )*
**AI:** Two-agent chain: GPT-4 Vision describes the image and hazards, GPT-4o-mini plans steps under a strict JSON schema consumed by the frontend.
**Architecture:** PWA frontend with Canvas overlays sends photos to a FastAPI backend that calls GPT-4 Vision, then GPT-4o-mini, returning schema-validated JSON.
**Novelty:** Pairs a vision pass with a planner pass and renders machine-readable targets as on-image overlays instead of plain text steps.
**Scope:** small · working: Described pipeline only; no repo, demo or video linked. · polish: Unknown; page has text only.
**Gaps:** No repo, demo or video; No evidence features were working; Target prize unstated
Sources: https://devpost.com/software/tasklens-4vz5di

---

### Team registration
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence C · confidence low*

**What it is:** A placeholder-style submission (project URL slug hackutd-y4x29r, titled Team registration) whose text describes AtlasOps, a fleet of autonomous agents monitoring customer sentiment and network experience. Most sections are empty.
**Problem / user:** Implied: a client needs timely action from live customer and network signals; no user role or problem is spelled out.

**Features**
- Real-time sentiment and network experience platform — Captures and analyzes customer sentiment and network signals across channels into live insights. *[claimed]*
- Autonomous goal-driven agents — Agents ingest live data, reason, decide actions and communicate with tools or people to resolve issues. *[claimed]*

**Prompt:** not public / not found
**Fit (none):** Wording about customer sentiment and network experience matches the T-Mobile theme, but no prize is stated.  *(targeted: )*
**AI:** Only described as agentic AI; no model or technique named.
**Architecture:** Not described; built-with tags are agentic, ai, data, machine-learning, python.
**Novelty:** Pitch of an agent fleet as monitoring teammates; no build details.
**Scope:** tiny · working: None; no repo, demo or video. · polish: Sections for how built, challenges, accomplishments and next steps are blank.
**Gaps:** Nearly empty page; No repo; Name differs from AtlasOps text; queue notes template-like page
Sources: https://devpost.com/software/hackutd-y4x29r

---

### Team Registration
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence C · confidence low*

**What it is:** A near-empty Devpost stub (slug leftover-logic, titled Team Registration) with only a built-with list: Nuxt, Vue, Node.js, TypeScript, Prisma, MySQL and Tailwind. No description of what it does.
**Problem / user:** 

**Prompt:** not public / not found
**Fit (none):** Nothing stated.  *(targeted: )*
**AI:** none
**Architecture:** Stack tags suggest a Nuxt/Vue web app with a Node/TypeScript backend using Prisma over MySQL; unconfirmed.
**Novelty:** 
**Scope:** tiny · working: None: no description, repo, demo or video. · polish: None visible.
**Gaps:** No project description; No repo; Project name unknown (Leftover Logic per URL)
Sources: https://devpost.com/software/leftover-logic

---

### The Potion Police
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A Streamlit dashboard on EOG's cauldron API data that tracks potion volumes by the minute and surfaces mismatches between what clients report and what the company records. Screens include a map home page, ticket views and graphs.
**Problem / user:** EOG needs to catch discrepancies between courier ticket records and actual cauldron levels quickly; framed around safety, accountability and efficiency.

**Features**
- Real-time potion flow monitoring — Pulls EOG API data with Requests and Pandas and plots volumes minute by minute in Streamlit. *[shown_working]*
- Mismatch detection — Compares client-side and company-side numbers to flag discrepancies. *[shown_working]*
- Daily mismatch heatmap — Heatmap of mismatches per day, per screenshot caption. *[shown_working]*
- Ticket Overview and Ticket Inspector — Two ticket views plus a graph of tickets over time. *[shown_working]*
- Dynamic map home screen — Home page shows cauldrons on a map. *[shown_working]*
- Current fill and potion level graphs — Charts of cauldron levels over time. *[shown_working]*
- Courier route optimization and forecasting — Listed as next steps, not built. *[planned]*

**Flow:** Open Streamlit app on a home map of cauldrons → Check potion level and current fill graphs → Review ticket overview and inspect individual tickets → Look at the daily mismatch heatmap

**Prompt:** HackUTD 2025 EOG Resources challenge (CauldronWatch, potion-flow monitoring): reconcile potion transport tickets against cauldron drain levels, detect mismatches, forecast overflow, plan witch pickup routes. Official statement not public; summary from winning-project descriptions and submissions.
**Fit (explicit):** README says it was chosen for EOG's clarity and values; delivers the monitoring and discrepancy half of the challenge, leaving routing and forecasting as future work.  *(targeted: EOG Resources challenge)*
**Sponsor tools:** EOG CauldronWatch API (Source of cauldron levels and tickets, core)
**AI:** none
**Architecture:** Python script fetches EOG API data with Requests, Pandas computes volume and mismatch analytics, Streamlit renders charts, map and heatmap.
**Novelty:** Straightforward analytics dashboard; themed as a potion guard with ticket inspection views.
**Scope:** small · working: Demo video on YouTube linked in README; ~1.3k LOC repo with Streamlit app. · polish: Logo, screenshot set, themed naming; no tests.
**Gaps:** YouTube video not watched; Challenge text not public
Sources: https://devpost.com/software/the-potion-police, https://github.com/calla-goeun-lee/ThePotionPolice (evidence README)

---

### TOYODA
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A concept for an AI agent that phones Toyota dealerships for a buyer to collect and negotiate prices. The Devpost promises 100+ dealer calls; the repo only has a Go API fetching dealer inventory from CARFAX by ZIP code and a planned architecture.
**Problem / user:** Car buyers waste days phoning dealers, repeating themselves and waiting on hold to compare prices and availability for one model.

**Features**
- Dealer and inventory search by ZIP — Go REST endpoint queries CARFAX Helix API for sellers within a radius. *[shown_working]*
- Multi-agent calling to 100+ dealers — AI voice agents (ElevenLabs, Gemini, Nemotron) ring dealers for prices, availability and offers. *[claimed]*
- Automated price negotiation — Agent negotiates with dealers on the user's behalf. *[claimed]*
- Side-by-side quote comparison — Results from all calls shown in one view. *[claimed]*
- Social login — Auth0 login via Google, Facebook or Microsoft. *[planned]*
- Real-time call tracking and follow-ups — README plan: batch caller status, quote recording, follow-up automation on Convex. *[planned]*

**Flow:** Sign in via Auth0 → Enter model, color and ZIP code → Agents call local dealers → Compare quotes in one place → Agent negotiates for the user

**Prompt:** HackUTD 2025 Toyota Financial Services track (car discovery/purchase help). Official challenge text not public; submissions frame it as helping buyers find and finance the right Toyota.
**Fit (implied):** Reframes Toyota buying as delegated dealer outreach with price comparison; the page does not name a prize.  *(targeted: Toyota Financial Services track (inferred from content), ElevenLabs/NVIDIA/Gemini tags)*
**Sponsor tools:** ElevenLabs (Human-sounding voice calls (batch caller planned), unclear); NVIDIA Nemotron (Inference for simultaneous calls (claimed), unclear); Gemini (Conversation handling (claimed), unclear); Auth0 (Login (planned in README), unclear)
**AI:** Claimed multi-agent voice calling with ElevenLabs voices, Gemini dialogue and Nemotron inference; none visible in the code beyond planning docs.
**Architecture:** Implemented: Go gorilla/mux API over CARFAX. Planned: React/Vite frontend, Convex backend and scheduler, Auth0, ElevenLabs batch caller. Devpost instead says Node/Express.
**Novelty:** Delegating phone negotiation to an AI caller is an unusual angle for car shopping; repo also holds heavy agent-generated planning docs.
**Scope:** medium · working: README: backend v1 complete, frontend and calling still planned; ~8k LOC, 110 files incl. docs and frontend scaffold. · polish: API docs and Makefile; no demo or video.
**Claims:** Calls over 100 local dealerships (page)
**Gaps:** Devpost has no repo link (found via queue); Devpost and README disagree on stack (Node/Express vs Go/Convex) and on how much is built; features follow Devpost for claimed, README for working status; No demo
Sources: https://devpost.com/software/toyoda, https://github.com/unclethien/toyoda-hackutd2025 (evidence README)

---

### ToyoQuest
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A short quiz web app: four lifestyle questions lead to one recommended Toyota, with Gemini behind the recommendation and scraped Toyota data stored in Firebase.
**Problem / user:** Toyota offers 100+ variants, overwhelming shoppers; target is a buyer wanting a lifestyle fit without hours of comparison.

**Features**
- Four-question lifestyle quiz — User answers four short questions in a clean interface. *[claimed]*
- Single best-fit Toyota recommendation — Gemini picks a vehicle from the collected data based on answers. *[claimed]*
- Scraped vehicle data — BeautifulSoup collects data into Firebase. *[claimed]*
- RAG-based personalization — Listed for later, along with real-time data, dealership info and used cars. *[planned]*

**Flow:** Open the Next.js app → Answer four lifestyle questions → Receive one recommended Toyota

**Prompt:** HackUTD 2025 Toyota Financial Services track (car discovery/purchase help). Official challenge text not public; submissions frame it as helping buyers find and finance the right Toyota.
**Fit (implied):** Quiz narrows the many Toyota variants to one pick by lifestyle.  *(targeted: Toyota track (page says it solves the given challenge))*
**Sponsor tools:** Gemini API (Recommendation logic and data handling, core)
**AI:** Gemini maps quiz answers to a Toyota recommendation from scraped data; no RAG yet.
**Architecture:** Next.js/TypeScript frontend, Flask backend, Firebase database, BeautifulSoup scraper, Gemini API.
**Novelty:** Minimal four-question funnel; otherwise a common quiz-recommender pattern.
**Scope:** small · working: Repo has Next.js app and questions folder (~1.9k LOC); README is the create-next-app template. · polish: Page says UI is cute; no screenshots, video or live link.
**Gaps:** README boilerplate; No demo; Working status unverified
Sources: https://devpost.com/software/toyoquest-fdtxsb, https://github.com/vishyyyyyyyyy/ToyoQuest (template README only)

---

### Toyota AI
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A Toyota shopping website with sign-up, login and forgot-password, a financial info form, and a Gemini/LangChain chat that suggests cars and dealerships from data scraped off Toyota's site.
**Problem / user:** Car shoppers spend long hours researching and comparing models; target is a time-poor buyer with budget constraints.

**Features**
- Account system — Login, signup and forgot password; user info saved in a database. *[shown_working]*
- Financial information form — After signup, user enters financial details used to match models and dealerships. *[claimed]*
- AI car chat — Home page chat where user states preferences and the model suggests cars. *[claimed]*
- Spec-based filtering — Suggestions filtered by body style, seat count and other specs. *[claimed]*
- Scraped Toyota data in Firebase — BeautifulSoup car data stored for the AI to reference. *[claimed]*

**Flow:** Sign up or log in → Enter financial information → Chat with the AI about preferences → Browse recommended models and dealerships

**Prompt:** HackUTD 2025 Toyota Financial Services track (car discovery/purchase help). Official challenge text not public; submissions frame it as helping buyers find and finance the right Toyota.
**Fit (none):** Pairs buyer finances and preferences with Toyota models; no prize stated.  *(targeted: )*
**Sponsor tools:** Gemini API (Language model powering recommendations via LangChain, core)
**AI:** Gemini through LangChain takes preferences plus financial background and structured Firebase car data to recommend models.
**Architecture:** React/TypeScript/Tailwind frontend, Flask backend, Firebase data store, BeautifulSoup scraper, LangChain + Gemini.
**Novelty:** Uses financial profile as an input to the recommendation, with Toyota/Capital One-inspired design.
**Scope:** small · working: Two screenshots (sign in, sign up) only; no repo or demo. · polish: Auth screens shown; remainder unseen.
**Gaps:** No repo; Only auth screenshots as evidence; Next steps blank
Sources: https://devpost.com/software/hackutd-project-2wxrdy

---

### Toyota Discover
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence medium*

**What it is:** A React and Express car-shopping companion for Toyota buyers that mixes a lifestyle recommender, driving-personality quiz, weighted comparison sliders, a true-cost calculator and financing comparison, plus a speech-to-text chatbot.
**Problem / user:** Standard filters miss real-life needs like a coming baby or a quiet cabin; target is a Toyota shopper wanting concierge-style guidance.

**Features**
- Lifestyle recommender — Questions on family size, trips, commute and plans produce matched Toyota models. *[claimed]*
- Driving personality quiz — Matches cars to styles such as cautious, gadget-lover or noise-sensitive and maintenance preference. *[claimed]*
- Weighted comparison engine — Importance sliders like Safety 10/10 re-rank vehicles. *[claimed]*
- True cost calculator — Estimates finance vs lease vs used, maintenance, insurance and fuel over ownership. *[claimed]*
- Financing options side by side — Compares lease, finance and used paths. *[claimed]*
- Speech-to-text chatbot — Spoken long queries to a chatbot about vehicles (ElevenLabs). *[claimed]*
- Upgrade nudge — Pop-up suggesting a nearby higher model when price gap is small. *[claimed]*
- Community reviews and friend comparison — Browse reviews and compare with friends. *[claimed]*

**Flow:** Open homepage → Answer lifestyle or personality questions or speak to the chatbot → Adjust priority sliders → Review ranked matches and cost estimates → Compare financing options

**Prompt:** HackUTD 2025 Toyota Financial Services track (car discovery/purchase help). Official challenge text not public; submissions frame it as helping buyers find and finance the right Toyota.
**Fit (implied):** Combines personalized vehicle matching with cost-of-ownership and financing comparison, the finance angle of the sponsor.  *(targeted: Toyota Financial Services track (inferred))*
**Sponsor tools:** ElevenLabs (Speech-to-text chat input, supporting)
**AI:** Custom hybrid scoring over lifestyle and personality variables for ranking; chatbot with speech input; no named model.
**Architecture:** React/Tailwind frontend (about 78 src files) with Node/Express API for questionnaires, comparisons and vehicle data.
**Novelty:** Unusually wide feature set for the track: sensory preferences, upgrade nudge and cost model beyond spec filters.
**Scope:** medium · working: Four screenshots on Devpost; ~7.5k LOC repo; no demo link. · polish: Screenshots of homepage, recommender, quiz, financing; no video.
**Gaps:** README repeats Devpost text; implementation of each feature not checked; No demo
Sources: https://devpost.com/software/toyota-6q79we, https://github.com/RishiNatarajan6932/carshop-express (evidence README)

---

### Toyota Dream Finder
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A Django web page where a buyer enters several search criteria (max cost, mileage, transmission, fuel type, mpg, budget, horsepower) and gets matching cars from a Pandas-queried CSV dataset. No AI in this version.
**Problem / user:** Buyers do not know which model fits; aimed at prospective car buyers wanting to find a dream model.

**Features**
- Criteria search form — HTML/Tailwind page takes cost, mileage, transmission, fuel, mpg, budget and horsepower inputs. *[claimed]*
- CSV-backed matching — Django hands the query to Pandas which filters a compiled CSV of cars and returns best matches. *[claimed]*
- Real-time Toyota data and AI recommendations — Listed as future work. *[planned]*

**Flow:** Open the page → Enter search parameters → Django queries the CSV with Pandas → View best matching cars

**Prompt:** HackUTD 2025 Toyota Financial Services track (car discovery/purchase help). Official challenge text not public; submissions frame it as helping buyers find and finance the right Toyota.
**Fit (none):** Helps buyers find a dream model by filtering; no prize stated.  *(targeted: )*
**AI:** none
**Architecture:** Django backend with Pandas filtering a CSV dataset gathered from online databases; HTML and Tailwind frontend.
**Novelty:** Plain filter tool; page says eight parameters but lists seven.
**Scope:** small · working: Repo has backend with ~2.7k LOC; page says a running page and working backend exist. · polish: No screenshots, video or demo; README says only "hi".
**Gaps:** README empty; No demo
Sources: https://devpost.com/software/hackutd-d5hojq, https://github.com/ByteBangshu/HackUTD2025 (README near-empty)

---

### Toyota DreamDrive
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence low*

**What it is:** A web platform concept for finding, comparing and financing Toyota vehicles with AI-based natural-language help and live financing and lease calculations. The page is feature-list only, with no demo or repo.
**Problem / user:** Shoppers struggle to search, compare and finance Toyotas; target is any Toyota shopper.

**Features**
- Lifestyle-based recommendations — Personalized car suggestions from lifestyle, driving preferences and budget. *[claimed]*
- Side-by-side comparison — Compare models with dynamic filters and intelligent search. *[claimed]*
- Financing and leasing calculators — Real-time payment and lease calculations. *[claimed]*
- AI natural-language assistant — Conversational help for questions about the lineup. *[claimed]*
- Mobile app, AR previews, in-car integration — Listed as next steps. *[planned]*

**Flow:** Enter lifestyle, driving and budget details (inferred) → Receive recommendations → Filter and compare models → Calculate financing or lease

**Prompt:** HackUTD 2025 Toyota Financial Services track (car discovery/purchase help). Official challenge text not public; submissions frame it as helping buyers find and finance the right Toyota.
**Fit (implied):** Covers vehicle search, comparison and financing in one AI-assisted site; no prize stated on page.  *(targeted: Toyota Financial Services track (inferred))*
**AI:** Unnamed models for personalization and a natural-language assistant; external pricing and financing APIs claimed without names.
**Architecture:** HTML/CSS/JS frontend with Python and Node.js backend calling unnamed external APIs; roles not specified.
**Novelty:** Generic Toyota shopping assistant; no distinguishing mechanism described.
**Scope:** small · working: None shown; no repo, demo, video or screenshots noted. · polish: Claims smooth animations and responsive design, unverified.
**Gaps:** No repo; No demo evidence; Challenge text not public
Sources: https://devpost.com/software/toyota-dreamdrive

---

### Toyota Path Finder
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A React and Express app where a lifestyle quiz feeds an LLM that recommends Toyota models; users swipe through matches Tinder-style, save favorites and compare cars with AI-written financial and lifestyle analysis.
**Problem / user:** Car buying is confusing and spec-focused; aimed at prospective Toyota buyers wanting lifestyle-based picks and clear comparison.

**Features**
- Lifestyle quiz — Questions on commute, family plans, adventure and tech priorities generated through backend endpoint. *[claimed]*
- AI model matching — LLM matches answers to curated Toyota JSON data and writes user-specific analysis. *[claimed]*
- Swipe interface — Tinder-style swipe through recommended cars; likes saved to a favorites collection. *[claimed]*
- Comparison page — Selected cars shown with price, mpg and lease estimate. *[claimed]*
- AI financial analysis — Five-year total cost of ownership, insurance and maintenance estimates plus lifestyle fit. *[claimed]*
- Failure fallbacks — Fallback parsing and images so app works if AI or services fail. *[claimed]*
- Dealership inventory, test drives, TFS pre-qualification — Listed as future work. *[planned]*

**Flow:** Answer the quiz → AI returns matched Toyota models → Swipe and like cars into favorites → Open comparison with price, mpg and lease → Expand dropdowns for cost and lifestyle analysis

**Prompt:** HackUTD 2025 Toyota Financial Services track (car discovery/purchase help). Official challenge text not public; submissions frame it as helping buyers find and finance the right Toyota.
**Fit (implied):** Quiz-driven Toyota matching plus cost-of-ownership and lease analysis for buyers.  *(targeted: Toyota Financial Services track (inferred; next steps mention TFS pre-qualification))*
**AI:** LLM (Claude-3-Haiku via OpenRouter per page) generates questions, matches vehicles and writes comparison analysis, with JSON-parsing fallbacks.
**Architecture:** React/Vite frontend with Context state; Node/Express REST API for question generation, matching and comparisons; curated Toyota JSON dataset; LLM via OpenRouter.
**Novelty:** Swipe-to-like interaction layered on an LLM matcher.
**Scope:** small · working: Page describes full flow with screenshot; repo ~2.2k LOC with a test; README one line. · polish: Toyota-branded design, loading states and fallbacks claimed; no demo or video.
**Gaps:** README minimal; No demo; Page names OpenAI and Claude-3-Haiku via OpenRouter ambiguously
Sources: https://devpost.com/software/toyota-dreamcar, https://github.com/divyayalam/toyotaHack (one-line README)

---

### Toyota Vision
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** An AI agent called Yota that analyzes a ZIP code's weather, population and road quality to recommend a Toyota and financing, then lets the user virtually drive it in a 3D simulator on real roads via Google Maps and Street View.
**Problem / user:** Buyers cannot test-drive on their own familiar roads and many lack nearby dealers; aimed at Toyota shoppers wanting a location-aware try-before-visit.

**Features**
- ZIP-based recommendation — scikit-learn/pandas model on cleaned local data suggests a car fitted to area conditions. *[claimed]*
- Yota AI assistant — Gemini-backed assistant recommends cars and financing options. *[claimed]*
- 3D driving simulator — Virtually drive the chosen Toyota with weather conditions and day/night modes. *[claimed]*
- Real-road routes — Google Maps, Street View and geocoding visualize drives on actual roads. *[claimed]*
- VR, live traffic, steering hardware — Listed as next steps. *[planned]*

**Flow:** Enter ZIP code and basic details → Yota analyzes local conditions → Receive car and financing recommendation → Drive the car in the 3D simulator, switching weather and time of day

**Prompt:** HackUTD 2025 Toyota Financial Services track (car discovery/purchase help). Official challenge text not public; submissions frame it as helping buyers find and finance the right Toyota.
**Fit (implied):** Ties vehicle and financing recommendations to local conditions and adds a virtual test drive.  *(targeted: Toyota Financial Services track (inferred))*
**Sponsor tools:** Gemini API (Recommendations on frontend and backend, and debugging help, supporting)
**AI:** scikit-learn model on ZIP-level features for recommendations; Gemini for conversational recommendations.
**Architecture:** React/Tailwind frontend with 3D simulator and Google Maps/Street View, Flask backend for Gemini and user data, ML model on engineered ZIP data.
**Novelty:** Combines location-aware recommendation with a driving simulator on real routes, uncommon for this track.
**Scope:** small · working: Page says functional prototype; no repo, demo or video. · polish: Unverified.
**Gaps:** No repo; No demo; Datasets unnamed
Sources: https://devpost.com/software/toyota-drivesphere

---

### ToyoTrack
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence medium*

**What it is:** A Toyota explorer with budget filters, payment and lease calculators, side-by-side comparison, user accounts and a Gemini chat box grounded in its own car and financing data. Frontend and backend are sizable (~14k LOC, Docker).
**Problem / user:** Dealership financing feels intimidating; aimed at buyers shopping a Toyota within a budget who want plain-language financing help.

**Features**
- Vehicle catalog browse and filters — Explore page with filters and preferences against car spec tables. *[shown_working]*
- AI chat box — Gemini answers natural-language questions (trim comparisons, SUV under $40k, poor-credit financing) kept to app data via system prompts. *[shown_working]*
- Payment calculator — Financing estimate view. *[shown_working]*
- Lease calculator — Separate leasing payment view. *[shown_working]*
- Two-vehicle comparison — Side-by-side compare page. *[shown_working]*
- Accounts and sessions — Profile creation, authentication and session storage. *[shown_working]*
- Used-car sales and finance consultant AI — Planned expansion. *[planned]*

**Flow:** Create profile and authenticate → Browse catalog → Apply budget filters → Compare two vehicles → Run payment or lease calculators → Ask the chat box questions

**Prompt:** HackUTD 2025 Toyota Financial Services track (car discovery/purchase help). Official challenge text not public; submissions frame it as helping buyers find and finance the right Toyota.
**Fit (implied):** Page emphasizes making financing and leasing clear for budget-limited buyers.  *(targeted: Toyota Financial Services track (inferred))*
**Sponsor tools:** Gemini API (Chat box grounded in app data, core)
**AI:** Gemini treated as stateless, with context passed per request and system prompts restricting answers to the app's car and financing data; Claude used to help parse JSON datasets.
**Architecture:** React/TypeScript/Tailwind frontend, Node/Express API with Swagger, PostgreSQL for users and cars, CarsXE data plus curated JSON, Docker.
**Novelty:** Financing and lease calculators with plain-language explanation are central rather than just recommendation.
**Scope:** medium · working: Seven screenshots of each screen and ~14k LOC repo with Docker. · polish: Figma-designed UI, Swagger docs; no video or live demo.
**Gaps:** README minimal; No demo
Sources: https://devpost.com/software/toyotrack, https://github.com/dblopez04/toyotrack (one-line README)

---

### Witch Delivery Associates
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence A · confidence high*

**What it is:** A Streamlit dashboard on EOG's CauldronWatch API that shows cauldron levels on a Mapbox map, replays fill and drain cycles, summarizes courier tickets and flags discrepancies between drains and tickets, in a witch-themed UI.
**Problem / user:** Operators need to confirm potion collected matches logged tickets and spot missing or unlogged collections.

**Features**
- Time series chronicle — Essence levels over time per cauldron. *[shown_working]*
- Live map — Mapbox map with cauldrons colored as filling, emptying or stable. *[shown_working]*
- Live playback — Animated progress bars replaying fill and drain cycles. *[shown_working]*
- Daily essence summary — Average, sum, min and max per day per cauldron. *[shown_working]*
- Witch courier logs — Ticket totals, trip averages and collected volume. *[shown_working]*
- Discrepancy detection — Compares drain events with tickets to flag unlogged activity. *[shown_working]*
- Ancient records — Raw data view with CSV export. *[shown_working]*
- Overflow forecasting, route optimization, alerts — Listed as future enhancements. *[planned]*

**Flow:** Run Streamlit app → Pick a tab from Time Series to Ancient Records → Watch live map or playback → Open discrepancy tab to review flagged mismatches → Export raw data

**Prompt:** HackUTD 2025 EOG Resources challenge (CauldronWatch, potion-flow monitoring): reconcile potion transport tickets against cauldron drain levels, detect mismatches, forecast overflow, plan witch pickup routes. Official statement not public; summary from winning-project descriptions and submissions.
**Fit (explicit):** README states it was built for the CauldronWatch challenge and covers monitoring and ticket discrepancy detection; forecasting and routing left as future work.  *(targeted: EOG Resources CauldronWatch challenge)*
**Sponsor tools:** EOG CauldronWatch API (Cauldron metadata, time series, tickets, market location, core)
**AI:** none
**Architecture:** Single Streamlit app using Requests and Pandas against five EOG API endpoints, Plotly/Mapbox visualizations, Hydralit components for styling.
**Novelty:** Playback animation and witch-themed naming; the team notes drain and fill curves were non-linear, shaping its understanding.
**Scope:** small · working: README lists seven working tabs; demo video on YouTube; ~1k LOC single app file. · polish: Themed UI and Devpost screenshots; 9 likes.
**Gaps:** Video not watched; Challenge text not public
Sources: https://devpost.com/software/eog-potion-alert, https://github.com/Leoxoo/HackUTD2025 (evidence README)

---

### WitchWatch
*HackUTD HackUTD 2025 · dataset: baseline · tier: baseline_non_winner · evidence B · confidence high*

**What it is:** A hardware plus software take on EOG's CauldronWatch: a Raspberry Pi Pico 2 rig with servo, keypad, potentiometers, LEDs, buzzer, OLED and E-ink lets a person act as a thieving witch courier, while a Flask/React dashboard checks drains against tickets and shows routes.
**Problem / user:** Potion (oil) flow must be tracked and mismatches between drains and transport tickets caught; users are cauldron network operators.

**Features**
- Live cauldron monitoring — Reads real-time cauldron data from EOG API and shows levels, fill rates and time-to-full. *[claimed]*
- Physical fill indicator — Servo on a 3D-printed structure shows a cauldron's level. *[claimed]*
- Hardware theft simulation — Keypad picks a cauldron; potentiometers and buttons simulate courier stealing potion. *[claimed]*
- Discrepancy detection — Backend compares drain events with tickets, described as ML-based, and sends alerts. *[claimed]*
- Multi-channel alerts — LEDs, buzzer, E-ink, OLED and dashboard notifications. *[claimed]*
- Route optimization — Computed routes sent back to hardware and dashboard via Mapbox. *[claimed]*
- Dashboard pages — Map, per-cauldron, witch view, forecast details, live data, discrepancies and tickets. *[claimed]*

**Flow:** Select a cauldron on the keypad → Use dials and buttons to simulate collecting potion → Servo and LEDs react; Pico sends JSON over serial to backend → Backend checks against tickets → Review alerts, tickets and routes on dashboard

**Prompt:** HackUTD 2025 EOG Resources challenge (CauldronWatch, potion-flow monitoring): reconcile potion transport tickets against cauldron drain levels, detect mismatches, forecast overflow, plan witch pickup routes. Official statement not public; summary from winning-project descriptions and submissions.
**Fit (implied):** Page says it responds to the EOG track; adds physical embedded demo of cauldron states and theft alerts atop discrepancy checks and route planning.  *(targeted: EOG Resources challenge, Best Hardware (inferred from hardware build))*
**Sponsor tools:** EOG CauldronWatch API (Live cauldron data and ticket records, core); Mapbox API (Maps and routing, supporting)
**AI:** Page claims ML-based discrepancy detection; no model or method named.
**Architecture:** Pico 2 sends JSON over serial relayed by TCP to Flask/Pandas backend, which pulls EOG API, returns state, alarms and routes to hardware and a React/TypeScript dashboard.
**Novelty:** Physical cauldron rig with theft role-play and bidirectional hardware link is rare among the track's dashboard-only entries.
**Scope:** medium · working: Embedded YouTube demo video and ~7.5k LOC repo across frontend and backend. · polish: 3D-printed enclosure, themed storytelling, multi-display hardware; README empty.
**Claims:** Fully functional real-time hardware plus software integration (page)
**Gaps:** README empty; Video not watched; Prize targeting inferred
Sources: https://devpost.com/software/cauldronwatch, https://github.com/syedkazmi14/PotionTracker (README is title only)

---

