# LA Hacks — LA Hacks 2026 (20 projects)

### Accent
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Track: Light The Way; Winner Figma Make Challenge; Track: Light The Way

**What it is:** A local macOS menu-bar assistant. A shortcut starts voice capture, the screen is grabbed, an RF-DETR UI detector finds clickable elements, Gemini resolves intent, and the app highlights the target and speaks the direction in the user's language.
**Problem / user:** Older adults, non-English speakers and non-technical users who can't find on-screen controls such as unmute or camera in video calls; inspired by the creators' grandparents.

**Features**
- Voice request in any language — Keyboard shortcut opens a command bar; ElevenLabs realtime speech-to-text transcribes, and screen capture fires when speech ends. *[shown_working]*
- UI element detection — RF-DETR-based UI-DETR-1 model boxes buttons, menus and regions; results normalized to a JSON schema. *[shown_working]*
- Crop sheets for labeling — Individual element crops are assembled into a sheet so the LLM can label elements without overlap confusion. *[shown_working]*
- Intent resolution — Gemini 3.1 (or Ollama fallback) uses speech, labeled screenshot and context to classify command/question/UI action; handles vague requests. *[shown_working]*
- Highlight and spoken guidance — Native overlay marks the element to press; text appears in a Gradio UI and ElevenLabs speaks it in the user's language. *[shown_working]*
- Animated mascot — Figma Make mascot shows while the pipeline is thinking. *[claimed]*
- Teach Me and memory shortcuts — Planned step-by-step mode, personalization from frequent actions, mobile support. *[planned]*

**Flow:** Press the keyboard shortcut → Speak a request in any language → Screen captured at end of speech → Detector annotates clickable elements → Intent model picks the target element → Overlay highlights it and spoken text instructions play

**Prompt:** Light The Way (education): make learning accessible to all via accessibility features or interactive learning. Figma Make Challenge: show how Figma Make was used in the workflow for ideation, prototyping or pitching.
**Fit (explicit):** Accessibility tool that makes software learnable for elderly and non-English users; README lists both awards and the page credits Figma Make for the mascot.  *(targeted: Track: Light The Way, Figma Make Challenge)*
**Sponsor tools:** Figma Make (Animated mascot, supporting); ElevenLabs (Realtime speech-to-text and text-to-speech, core); Google Gemini 3.1 (Intent resolution over labeled screenshots, core)
**AI:** RF-DETR UI detector produces boxes; crop sheets plus structured prompts let Gemini (LangChain, strict Pydantic schemas) choose the target element; local Ollama Gemma tried and dropped as too slow.
**Architecture:** Swift/AppKit menu-bar app captures voice and screen, calls a Gradio detector server and Python pipeline (detect, label, resolve), and a local Node/overlay returns the highlight.
**Novelty:** Pairs UI-element detection with LLM intent reasoning to point at screen controls, rather than controlling them, for non-technical and multilingual users.
**Scope:** medium · working: About 14.5k LOC, Swift app plus Python pipeline, README with setup; screenshots of Google Meet and Spanish prompts; no video. · polish: Overlay, mascot and fallback logic; no tests or CI.
**Claims:** End-to-end prototype built in under 36 hours | Handles vague requests such as 'Why can't you hear me?'
**Gaps:** No demo video; No accuracy or latency numbers; Aramco sponsorship of the track not described on the hackathon page
Sources: https://devpost.com/software/accent-cdw2qi, https://github.com/RyloRiz/accent, https://la-hacks-2026.devpost.com/

---

### Autopsy
*LA Hacks LA Hacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner 3rd Overall; Winner Cognition Company Challenge [3rd]; 3rd Overall [3rd]

**What it is:** A blackbox recorder for AI coding agents that wraps the opencode runtime, logs every tool call and rejection, builds a failure graph in Postgres with pgvector, and injects warnings into the agent's prompt before future similar tasks.
**Problem / user:** Developers using coding agents that repeat the same mistakes (skipped migrations, type drift, no tests) because each run starts with no memory of past failures.

**Features**
- Event recorder plugin — TypeScript opencode plugin batches tool calls, edits, chat and rejections to the service, fire-and-forget *[shown_working]*
- Failure classifier — Five deterministic rules (e.g., schema changed but no migration) plus optional Gemma analysis of diffs *[shown_working]*
- Failure knowledge graph — Postgres tables of nodes and edges (nine node types) with confidence, temporal decay and counter-evidence *[shown_working]*
- Preflight retrieval — Embeds new task, nearest-neighbour search and 3-hop walk to inject warnings or hard-block tool calls *[shown_working]*
- Postflight checks — Runs lint, typecheck and tests after the agent finishes and logs failures as rejections *[claimed]*
- Dashboard — Run timelines, autopsy reports, 3D force-directed graph, badges for mistakes caught early *[shown_working]*
- One-line installer — curl script starts local stack and links plugin into the project *[shown_working]*

**Flow:** Run installer in a project → Agent works and is rejected or fails → Autopsy classifies the failure and updates graph → Similar task starts and preflight warns the agent → Dashboard shows caught-before-it-happened badges

**Prompt:** Cognition Company Challenge: build a tool, integration or product that makes AI coding agents more capable or removes toil they cannot handle alone, something a real engineering team would use; suggestions include verification, context retrieval, MCP plugins and handoffs.
**Fit (implied):** Adds persistent failure memory and guardrails to coding agents, so past rejections are retrieved and injected as warnings before new runs. Page lists Devin among built-with tools.  *(targeted: Cognition Company Challenge, 3rd Overall)*
**Sponsor tools:** Devin (Listed as a build tool and a future adapter target, unclear)
**AI:** Gemini embeddings (768-d) for task and patch retrieval; rule-based failure classifier with optional Gemma LLM analysis; the LLM is kept out of the preflight path.
**Architecture:** opencode plugin posts events to a FastAPI service backed by Postgres+pgvector; classifier builds graph; /v1/preflight returns prompt addenda; Next.js dashboard with SSE; Docker Compose.
**Novelty:** Treats agent failures as a persistent graph with decay and counter-evidence and feeds it back into prompts; fail-open and additive design. Page admits no measurement of mistake reduction.
**Scope:** large · working: Live site and installer, 165 service tests, CI, Docker; closed loop described working in a real opencode runtime. · polish: Architecture and demo-script docs, custom domains, themed dashboard.
**Claims:** 165 service tests passing | One-line install brings up whole stack | Preflight has 800 ms hard timeout
**Gaps:** No demo video listed; Effectiveness not measured
Sources: https://devpost.com/software/autopsy-zq5d84, evidence/la-hacks-la-hacks-2026-autopsy.json, https://la-hacks-2026.devpost.com/

---

### beehyv
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Winner Organizers' Choice

**What it is:** A research-gap explorer: about 100k arXiv papers are embedded, clustered and flattened into a 2D semantic map, empty regions are found geometrically and named by an LLM, and a swarm of 'bee' agents proposes, codes and judges new model ideas that combine papers around each gap.
**Problem / user:** Researchers and academia facing superficial AI literature, hallucinations and non-replicable code; page asks how far verifiable, automated research can go.

**Features**
- Semantic paper graph — Precomputed embeddings of ~100k arXiv papers clustered with MiniBatchKMeans, LLM-titled clusters, UMAP to 2D, shown in a WebGL frontend. *[shown_working]*
- Void discovery — Voronoi diagram plus alpha shape locate maximal empty circles; filtered by angular coverage; LLM names the top voids. *[shown_working]*
- Border-paper scoring — Papers around a void get OpenAlex metadata, scored on citations and recency; eight picked via angular buckets plus score fill. *[claimed]*
- Queen/Worker Bee ideation — Orchestrator agent has paper agents propose ideas with rationale and code changes; workers pair up for hybrid ideas. *[claimed]*
- Plan, code and judge loop — Planner writes a plan, coder implements, judge tests and feeds back until a target accuracy. *[claimed]*
- MCP memory — FastMCP plus SQL store lets agents categorize and persist information. *[claimed]*
- Local and cloud inference — OpenRouter Nemotron 3 Super in cloud; Gemma4 on an ASUS GX10 locally with a few seconds delay. *[claimed]*

**Flow:** Open the 2D semantic map of papers → See highlighted research voids and their names → Select a void and view its border papers → Watch the swarm cross-pollinate ideas and produce a model → Review results from judge feedback loop

**Prompt:** not public / not found
**Fit (none):** Organizers' Choice has no public description; the project is an ambitious automated-research pipeline with a visual map and agent swarm.  *(targeted: Winner Organizers' Choice)*
**Sponsor tools:** ASUS GX10 AI Supercomputer (Local Gemma4 inference, supporting); OpenRouter (Nemotron 3 Super) (Cloud LLM inference, supporting)
**AI:** Embedding clustering and geometry for gap finding, LLMs to name clusters and voids, and a multi-agent swarm (orchestrator, workers, planner, coder, judge) over MCP memory that writes and tests code.
**Architecture:** Ingestion and embeddings feed UMAP/Voronoi void analysis and a React/WebGL visualizer; an agentswarm plus paper2code pipeline run via a CLI over papers, using MCP/SQLite memory.
**Novelty:** Treats empty regions of embedding space as research gaps and chains gap-finding straight into agent-driven code generation and judging.
**Scope:** large · working: 250 files, about 25k LOC in visualizer, ingestion, agentswarm and paper2code; embedded video and write-up; no result numbers. · polish: Multiple modules; README in repo is a merge-conflicted generalresearch version; no tests.
**Claims:** About 100k papers sampled | Eight papers per void | More than six coordinated agents | Local Gemma4 inference with a few seconds of delay
**Gaps:** Repo README starts with a merge conflict marker and describes a generalresearch pipeline (ingest, discuss, codegen); feature list follows the Devpost page; Google Doc write-up and video not read; No accuracy results; target accuracy unspecified; Organizers' Choice prompt has no public text
Sources: https://devpost.com/software/beehyv, https://github.com/justanotherinternetguy/Beehyv, https://la-hacks-2026.devpost.com/

---

### Bridge
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Hardware Hack

**What it is:** A low-cost refreshable braille prototype for deaf-blind students. A web app takes an image or lecture audio, Claude and Whisper turn it into a short summary, and an ESP32 with stepper motors drives a 3D-printed rotating cylinder to raise pins.
**Problem / user:** Deaf-blind students (page cites 160 million deafblind people) who depend on human interpreters; commercial braille displays cost $3,000 to $15,000 and cannot process photos or lectures.

**Features**
- Image and audio capture — Web UI accepts photo uploads or camera captures and audio uploads or recordings via /image and /lecture endpoints. *[shown_working]*
- Transcription and image-to-text — Whisper (faster-whisper) transcribes audio and Claude reads images such as handwritten notes. *[shown_working]*
- Essential summary — Claude reduces content to a short idea suitable for slow tactile playback. *[shown_working]*
- Braille conversion and chunking — Text becomes braille patterns (devpost) or 4-character chunks (README) streamed over USB serial. *[shown_working]*
- Motor-driven tactile display — ESP32 firmware rotates stepper motors to calibrated positions; a cylinder with bumps lifts pins, holding each chunk about 5 seconds. *[shown_working]*
- Standalone device — Planned on-device camera, audio, battery and offline processing. *[planned]*

**Flow:** Submit an image or record audio on the connected computer → Backend transcribes and summarizes → Text is converted to braille or chunked characters → Chunks sent over serial to the ESP32 → Motors rotate and pins rise to display each chunk

**Prompt:** not public / not found
**Fit (implied):** Built physical hardware (3D-printed mechanism, steppers, ESP32) that works end to end with software; the prize page gives only the label, no description.  *(targeted: Best Hardware Hack)*
**Sponsor tools:** Anthropic Claude API (Image understanding and summarizing, core)
**AI:** Claude summarizes images and text into brief essentials; Whisper handles speech-to-text; braille conversion uses a built-in table with liblouis as an optional dependency.
**Architecture:** HTML/JS frontend posts to a FastAPI backend (vision, audio, summarizer, braille, serial modules) that sends chunks via pyserial to ESP32 firmware driving the motors.
**Novelty:** Targets a far cheaper tactile display and adds AI summarization of classroom images and lectures, using a rotating cylinder instead of per-cell actuators.
**Scope:** small · working: Team reports full pipeline tested to moving pins; repo 14 files, about 2.2k LOC with firmware; screenshots of hardware and CAD. · polish: Home page and demo UI; no tests; no video.
**Claims:** Existing braille displays cost $3,000-$15,000 | 160 million deafblind people worldwide
**Gaps:** Devpost says braille patterns on a bump cylinder; README describes 4 motors showing 4-character text chunks; feature list notes both; No video; No accuracy or cost figures for the built device; Best Hardware Hack has no public prompt text
Sources: https://devpost.com/software/bridge-4euwyt, https://github.com/lozlrc/Bridge/, https://la-hacks-2026.devpost.com/

---

### codebreaker
*LA Hacks LA Hacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner 1st Overall [1st]; Winner Cognition Company Challenge

**What it is:** A security platform for AI agents: ECVE-Bench, a benchmark of real GitHub-advisory vulnerabilities across ecosystems, a security-tuned agent harness with sandboxed tools, a live results dashboard, and a Devin-driven loop that reproduces, patches and opens PRs for findings.
**Problem / user:** Developers, security teams and AI-security researchers facing growing supply-chain attacks, with benchmarks mostly limited to C/C++ memory bugs and no agent-native tooling.

**Features**
- ECVE-Bench — Tasks built from GitHub Advisory records over the CWE Top 25 in npm, pip, maven, go; four hint levels L0-L3; 13 vulnerability classes *[shown_working]*
- Security agent harness — Tailored prompts, skills and tools (DeepWiki, scoped HTTP, finding submission, Modal sandbox) in tiered toolsets *[shown_working]*
- Multi-model evaluation — Vercel AI SDK routes Anthropic, OpenAI, Google models through Cloudflare AI Gateway on identical tasks *[shown_working]*
- Sandboxed, journaled runs — Cloning and PoC execution in Modal containers; runs logged for deterministic replay and scoring *[claimed]*
- Live dashboard — Streams agent traces, tool calls and scores over WebSockets with side-by-side comparison *[shown_working]*
- Autonomous CVE follow-up loop — Triage, de-duplicate, enrich with CVE/CWE data, then Devin reproduces, writes test, patches and opens a PR *[claimed]*
- Devin-driven benchmark curation — Three-stage filter/select/dispatch pipeline creates each task as a reviewable PR *[claimed]*

**Flow:** Run a model or audit against a target repo in a sandbox → Candidate finding is produced and scored → Triage de-duplicates and enriches it → Devin session reproduces and patches the issue → PR opens with patch and validation evidence → Researchers compare runs on dashboard

**Prompt:** Cognition Company Challenge: build a tool, integration or product that makes AI coding agents more capable or removes toil they cannot handle alone, something a real engineering team would use; suggestions include verification, context retrieval, MCP plugins and handoffs.
**Fit (explicit):** Uses Devin as an autonomous engineer for benchmark curation and for vulnerability reproduction, patching and PR creation, with an agent harness and benchmark evaluating coding agents on security tasks.  *(targeted: 1st Overall, Cognition Company Challenge)*
**Sponsor tools:** Devin (Benchmark curation PRs and autonomous CVE remediation, core); Cloudflare Workers/AI Gateway/Agents (Control plane, model routing, live dashboard, core); Modal (Sandboxed exploit execution, supporting)
**AI:** Frontier models (GPT-5, Kimi K2.6, Claude Sonnet) run in a security-specific harness; Devin sessions handle curation and patching.
**Architecture:** TypeScript monorepo: Cloudflare Workers/Hono/D1 control plane, Modal sandboxes, benchmark runner, React dashboard over Cloudflare Agents websockets, Devin API and GitHub integration.
**Novelty:** Ships a new multi-ecosystem vulnerability benchmark plus harness and automated remediation loop; benchmark data curated largely by Devin. Repo has about 1,000 benchmark files.
**Scope:** large · working: Reported scores, landing page, dashboard screenshots; 50k-line repo with Docker; no tests directory or video. · polish: Leaderboard and architecture screenshots; monorepo structure; no CI.
**Claims:** Benchmark consumed over 280 million tokens in 36 hours | GPT-5 averaged 24% per task | Kimi K2.6 rose from 35% to 47% inside harness | Claude Sonnet scored 48%
**Gaps:** README is one line; No video
Sources: https://devpost.com/software/codebreaker-la, evidence/la-hacks-la-hacks-2026-codebreaker.json, https://la-hacks-2026.devpost.com/

---

### Conjure
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: Agentverse - Search & Discovery of Agents

**What it is:** A text-to-building generator. A prompt like a cozy cabin passes through a pipeline of 14 Gemini-backed agents registered on Agentverse, producing a shared WorldSpec that a React Three Fiber frontend renders as a walkable first-person 3D interior, editable through chat.
**Problem / user:** People who can describe a space but cannot model it in 3D; no specific user group named.

**Features**
- Prompt to world plan — Intent parser and blueprint architect agents turn the prompt into rooms, dimensions, style, lighting, furniture and navigation. *[shown_working]*
- Sequential and parallel agent pipeline — FastAPI orchestrator runs planning agents in sequence, then geometry, lighting and material agents in parallel, then furniture, validation and pricing. *[shown_working]*
- Live progress streaming — WebSocket updates show which agent is working from intent parsing to final assembly. *[shown_working]*
- Walkable 3D render — React Three Fiber/Three.js builds the world from procedural assets; WASD and mouse walk, spawn point included. *[shown_working]*
- Natural-language editing — Toggle chat with T to edit the world, regenerating while preserving design intent. *[claimed]*
- Geometric guardrails — Grid/dimension validation and schema constraints prevent overlapping rooms and placement drift. *[claimed]*
- Agentverse registration — 14 agents registered with the Chat Protocol so they are discoverable. *[shown_working]*

**Flow:** Type a prompt describing a building → Watch agents plan and build with live progress → Spawn inside the generated 3D interior → Walk around with WASD and mouse → Press T to chat and edit the world

**Prompt:** Agentverse - Search & Discovery of Agents: build and register AI agents on Agentverse, discoverable via ASI:One, that turn user intent into executable outcomes.
**Fit (explicit):** README says it was built for the Agentverse track with 14 agents registered with the Chat Protocol, and generation runs through them to turn a text intent into a built world.  *(targeted: Track: Agentverse - Search & Discovery of Agents)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse (Registering 14 pipeline agents with Chat Protocol, core); Google Gemini (Backs each planning/building agent, core); Cloudinary (Listed in frontend dependencies; role not explained, unclear)
**AI:** Gemini-backed specialist agents (intent, architect, compliance critic, geometry, lighting, materials, furniture, validator, pricing, navigation) share and update one WorldSpec; LLM spatial weaknesses handled with schema validation.
**Architecture:** FastAPI orchestrator runs staged agents over a canonical Pydantic WorldSpec mirrored in TypeScript; WebSockets stream progress to a Next.js/R3F client.
**Novelty:** Splits 3D scene authoring across many named agents with one canonical spec and validators; roadmap pivoted from vendor-product matching to bigger procedural buildings.
**Scope:** large · working: 284 files, about 14.8k LOC, tests, quick-start and controls documented; screenshots of a conjured living room; no video. · polish: Docs folder with roadmap, pytest suite; no Docker or CI.
**Claims:** 14 agents registered on Agentverse | Turn language into a walkable world in minutes, not days
**Gaps:** README mentions legacy real-product matching being phased out; Devpost says procedural assets only; feature list follows Devpost; No demo video; Cloudinary role unclear
Sources: https://devpost.com/software/conjure-m960jz, https://github.com/pauligwe/WorldEdit, https://la-hacks-2026.devpost.com/

---

### Dots
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Track: Catalyst For Care; Winner Track: Agentverse - Search & Discovery of Agents

**What it is:** Converts a floor plan into a high-contrast tactile-style map for printing or embossing and a map-specific QR code. Scanning it opens a text or ElevenLabs voice assistant that answers orientation questions grounded in that map.
**Problem / user:** Blind and low-vision people who get no usable orientation from visual floor plans, plus architects and venues needing scalable ADA-style accessibility.

**Features**
- Tactile map generation — Gemini turns an uploaded floor plan into a black-on-white map with patterns and symbols and no numeric legend, suitable for print or emboss. *[shown_working]*
- Map-specific QR link — Each map gets a unique map_id; /m/{map_id} serves chat and /m/{map_id}/voice serves voice. *[shown_working]*
- Text Q&A — Fetch.ai ASI:One answers questions like entrance or exit count using stored map context as the system prompt. *[shown_working]*
- Voice Q&A — ElevenLabs Conversational AI sessions with server-minted short-lived tokens and per-map prompts. *[shown_working]*
- Map context extraction — Gemini builds a compact text context from the floor plan; fallbacks cover imperfect extraction. *[claimed]*
- ADA-style summary — Compliance summary from the extracted layout when available. *[claimed]*
- Per-map isolation and history — SQLite stores context and chat history keyed by map_id plus session_id. *[shown_working]*
- Agentverse agents — uAgents for room scan intake, testFET payment, floorplan-to-tactile, and wayfinding Q&A. *[claimed]*

**Flow:** Upload a floor plan → Dots creates tactile map image and map context → QR code attached to the printed or embossed map → User scans QR to open chat or voice page → Ask questions like where the entrance is and hear grounded answers

**Prompt:** Catalyst For Care: healthcare-oriented solutions. Agentverse - Search & Discovery of Agents: build and register AI agents on Agentverse, discoverable via ASI:One, turning intent into executable outcomes.
**Fit (implied):** README describes Agentverse-hosted uAgents and ASI:One Q&A; the accessibility aim for blind users is the only link to the care track, not stated explicitly.  *(targeted: Winner Track: Catalyst For Care, Winner Track: Agentverse - Search & Discovery of Agents)*
**Sponsor tools:** Fetch.ai ASI:One / Agentverse (Text Q&A and hosted agents, core); ElevenLabs (Voice conversations, core); Google Gemini (Tactile generation and map context, core); Vultr (Intended backend hosting, supporting); Cloudinary (Dashboard dependency; role unclear, unclear)
**AI:** Gemini image model produces tactile maps and extracts map context; ASI:One answers text questions with that context as prompt; ElevenLabs handles voice; fallbacks reduce vision errors.
**Architecture:** FastAPI backend with SQLite map store serves chat and voice pages per map_id; Gemini pipeline generates assets; uAgents on Agentverse wrap intake, payment, generation and Q&A; web demo on Vercel.
**Novelty:** Bridges a physical printed tactile map with a scannable conversational layer so one map answers venue questions; broadcast mode reuses maps without regeneration.
**Scope:** large · working: 207 files, about 20k LOC, curl-able endpoints, Vercel demo link and architecture diagram; no video. · polish: Detailed README with limitations; no tests or CI.
**Claims:** End-to-end pipeline from floor plan to tactile output to QR to text/voice Q&A | Secrets never reach the client in voice setup
**Gaps:** No video; Live demo not opened; No accuracy results; Catalyst For Care fit not stated by team
Sources: https://devpost.com/software/dots-y5r21j, https://github.com/aryanmudgal-tech/dots, https://la-hacks-2026.devpost.com/

---

### Drip
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Track: Sustain The Spark

**What it is:** A hardware and software demo that uses AI compute waste heat to make freshwater. A Raspberry Pi 5 running deployed agent containers is liquid-cooled into a homemade membrane distillation chamber that desalinates seawater, with a one-click deployer, telemetry dashboard and U.S. data center impact map.
**Problem / user:** Data centers and AI operators whose evaporative cooling consumes freshwater; framed by the team from drought-hit Florida, with no single named user.

**Features**
- One-click agent deployer — Website deploys PicoClaw agent containers onto the Pi 5 edge node via a Go server and Docker, exposed through ngrok. *[shown_working]*
- Shared LLM inference — Agents call Ollama Gemma 4 on an ASUS server over Tailscale or ngrok through a custom async engine handling multiple users. *[claimed]*
- Closed-loop liquid cooling — Custom cooling block on the Pi 5 moves heat into water without evaporative loss. *[shown_working]*
- Membrane distillation chamber — Waste heat warms saline water on one side of a hydrophobic membrane; a Peltier-cooled side condenses vapor into freshwater. *[shown_working]*
- Live telemetry dashboard — WebSocket feed shows thermal output, chamber temperatures, runtime status and projected water yield. *[shown_working]*
- National impact map — Uses a public U.S. data center dataset to show potential water generation if MD were adopted. *[claimed]*

**Flow:** Deploy an agent from the PicoClaw website → Container runs on the Pi and sends requests to Gemma on the ASUS server → Pi heat flows to the hot distillation chamber → Vapor crosses the membrane and condenses to freshwater → View telemetry, projected yield and impact map

**Prompt:** Sustain The Spark (sustainability): grassroots projects addressing climate change, waste reduction or the shift to clean energy.
**Fit (implied):** Reuses AI processor waste heat to produce freshwater and avoid water-hungry cooling; the framing is explicitly about AI data center water use.  *(targeted: Winner Track: Sustain The Spark)*
**Sponsor tools:** ASUS GX10 server (Hosting Gemma 4 inference via Ollama, core); Cloudinary (AI React Starter Kit in the frontend, token); Arista (Mentioned as a sponsor technology; use not described, unclear)
**AI:** Gemma 4 E4B served through Ollama on an ASUS server for agent inference; the AI role is mainly to generate compute heat and run the deployed agents rather than analysis.
**Architecture:** Next.js deployer and dashboard call a Go server that runs Docker containers on a Pi 5; Pi telemetry streams over WebSockets; an ASUS FastAPI hub proxies Gemma; heat feeds a physical MD chamber.
**Novelty:** Couples a software-agent deployer to a physical desalination loop powered by the compute's own waste heat, with homemade apparatus.
**Scope:** large · working: 101 files and 6.6k LOC across Go, Next.js, Python telemetry; team says MD produced freshwater; live Vercel demo; no yield numbers. · polish: Docker present; repo README is a Next.js default template; page has 33 likes.
**Claims:** MD process verified to generate fresh water (no volumes given) | Projected yield computed from heat and temperature gradient
**Gaps:** README is boilerplate Next.js text; No video; No measured water yield; Arista and Cloudinary roles vague
Sources: https://devpost.com/software/drip-6ao9m2, https://github.com/Lewin-B/lahacks2026, https://la-hacks-2026.devpost.com/

---

### Jarvis
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Track: Agentverse - Search & Discovery of Agents

**What it is:** A Chrome extension that watches Gmail and proactively briefs the user in a friendly tone, spots meeting requests, handles accept/decline with Google Calendar, and consults a restaurant-recommendation agent on Agentverse.
**Problem / user:** People who live in their inbox and calendar; the page argues most AI assistants are reactive chat boxes and wants one that acts before being asked.

**Features**
- Proactive Gmail briefing — On opening Gmail the extension reads emails and one ASI:One call returns a casual briefing plus a structured meetings list. *[claimed]*
- Meeting detection with inline accept/decline — Detected requests show buttons; accept writes a Google Calendar event, decline sends a polite email automatically. *[claimed]*
- Regex fallback for meeting times — Deterministic scan of email text for time patterns so detection does not depend only on the model. *[claimed]*
- Restaurant recommendation agent — Agentverse agent keeps per-user lifestyle profiles and scores options by cuisine, distance, price and dietary constraints. *[claimed]*
- Alerts on any tab — New emails and upcoming meetings surface in a Shadow DOM overlay on whichever tab is active. *[claimed]*
- Duplicate suppression and persistence — Gmail message-ID dedup with a daily reset; state kept in chrome.storage.local to survive MV3 worker restarts. *[claimed]*
- Friendly chat about day and inbox — Personality-prompted ASI:One chat grounded in schedule and inbox context. *[claimed]*

**Flow:** Install the extension and grant Google OAuth → Open Gmail and receive the briefing → Accept or decline detected meetings inline → Browse other tabs and get new-mail or meeting alerts → Chat with the assistant or ask for restaurant suggestions

**Prompt:** Build and register AI agents on Agentverse that are discoverable through ASI:One and turn a user's intent into executable outcomes.
**Fit (explicit):** Inference goes through ASI:One and a restaurant-recommendation agent is deployed on Agentverse behind a bridge server, with a Python orchestrator coordinating specialized agents for the extension.  *(targeted: Track: Agentverse - Search & Discovery of Agents)*
**Sponsor tools:** Fetch.ai ASI:One (asi1-mini) (Briefing, meeting extraction and chat inference, core); Fetch.ai Agentverse / uAgents (Hosts restaurant agent and orchestrator reached through a bridge server, core)
**AI:** asi1-mini returns structured JSON (briefing plus meetings) from one combined call; regex backstops it; a restaurant agent applies a weighted preference model per user profile. Requirements also list anthropic.
**Architecture:** MV3 extension (service worker handles OAuth, Gmail/Calendar calls, ASI:One) with Shadow DOM overlay; FastAPI bridge server links it to Python uAgents (orchestrator, restaurant agent) on Agentverse.
**Novelty:** Frames the assistant as proactive rather than chat-first and pairs a browser extension with a deployed agent network; the restaurant branch of the repo holds the agent code.
**Scope:** small · working: Repo has ~4.7k LOC of extension and Python code; page describes bug fixes found while running it. No video or live link. · polish: Personality tuning and dedup show iteration, but there are no tests and no README.
**Claims:** Detection reliability formula combining AI and regex failure probabilities | No quantitative metrics reported
**Gaps:** Repo has no README; evidence is file tree and requirements only; No demo video; Screenshot count not checked
Sources: https://devpost.com/software/jarvis-eifsyq, evidence/la-hacks-la-hacks-2026-jarvis.json (restaurant-agent branch; no README, manifests only), https://la-hacks-2026.devpost.com/

---

### MultiEval
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: Agentverse - Search & Discovery of Agents

**What it is:** An agent-evaluation platform for multi-agent orchestration: a graph and Gantt trace viewer, statistical A/B comparison of harnesses, and a meta-agent that writes and tests new harness variants. Built on Inspect AI and OpenHands.
**Problem / user:** Teams building multi-agent systems who cannot see coordination failures with single-agent tracing tools (Langfuse, LangSmith etc.) and want statistically sound harness comparisons.

**Features**
- Graph trace view — Per-agent lanes with causal edges (spawn, context-inject, broadcast), clustering events within 250 ms, causal-chain dimming and a replay slider. *[claimed]*
- Gantt trace view — Wall-clock lanes by agent and event category, adaptive ruler down to 100 ms, search filter, shared inspection panel. *[claimed]*
- A/B compare modal — Wilson intervals for pass rate, Welch t on tokens and time, z-test parity, Cohen's d, and a minimum-runs guard. *[claimed]*
- Agentic Evolve meta-agent — Frontier model reads a harness, proposes a variant, extends a benchmark, runs inspect eval, iterates until budget or three flat rounds. *[claimed]*
- Harness library — Multi++ (12 specialists), Kim-Gate delegation gate, Structured-Delegation, Cross-Sibling-Discovery bus, and a stock baseline. *[shown_working]*
- Structured-Delegation uplift — README reports pass rate 0.87 versus 0.79 for vague delegation, backed by the A/B tooling. *[claimed]*
- Genesis++ economic-simulation agent — Public uAgent on Agentverse (chat and payment protocols) spawns participant agents; demo is a 50-agent simplified economy. *[claimed]*

**Flow:** Write or generate a harness as an Inspect @task → Run it to produce an .eval log with multi-agent events → Find the run in the harness-aware log grid → Inspect it in Graph or Gantt view → Select two harnesses and open A/B compare → Optionally query the Genesis++ agent on ASI:One

**Prompt:** Build and register AI agents on Agentverse that are discoverable through ASI:One and turn a user's intent into executable outcomes.
**Fit (implied):** Core product is eval tooling, but one harness (Genesis++, produced by the meta-agent) deploys an Agentverse uAgent on ASI:One that spawns economic-simulation agents; Devin and Windsurf are tagged for the Cognition prize.  *(targeted: Track: Agentverse - Search & Discovery of Agents, Cognition Company Challenge)*
**Sponsor tools:** Fetch.ai Agentverse / ASI:One (Genesis++ public agent with chat and payment protocols, supporting); Devin / Windsurf (Listed in built-with; role not described, unclear)
**AI:** Meta-agent (Claude Opus 4.7 or Gemini 3.1 Pro per page) evolves harnesses against benchmarks; an auditor model drives structured delegation and sibling discovery; OpenHands sub-agents do the tasks.
**Architecture:** OpenHands agents wrapped in Inspect AI tasks emit normalized event metadata into .eval logs; a React/TypeScript viewer renders graph, Gantt and A/B stats; meta-agent loop writes harness variants to a registry.
**Novelty:** Treats orchestration harnesses as the object of study with causal multi-agent traces and a self-evolving harness loop; repo vendors OpenHands, Inspect and the agent SDK (~900k LOC, mostly vendored).
**Scope:** large · working: Large repo with tests, Docker, thousands of recorded OpenHands sessions, demo video and hosted page; benchmark size and run counts are not given. · polish: Detailed README with harness table and statistics rationale, demo site, challenge write-up of fixes.
**Claims:** Structured-Delegation pass rate 0.87 vs 0.79 baseline | Genesis++ demo of a 50-agent economy | Self-described first eval platform for multi-agent orchestration
**Gaps:** Benchmark definition and run counts not stated; YouTube video not opened; Page also lists a Cognition win; track listing shows only Agentverse
Sources: https://devpost.com/software/multival, evidence/la-hacks-la-hacks-2026-multieval.json, https://la-hacks-2026.devpost.com/

---

### NeighborFridge
*LA Hacks LA Hacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best UI/UX; Figma Make Challenge

**What it is:** A full-stack food-rescue web app: users scan grocery receipts into a pantry with expiry estimates, list surplus food for neighbors to claim, and hand it off via simulated shared lockers, with an impact dashboard.
**Problem / user:** Students, households and roommates who lose groceries to spoilage and have no easy way to pass surplus food to neighbors.

**Features**
- Receipt scanning to pantry — OCR (Tesseract, optional Veryfi) parses store, total and line items; user confirms; items get estimated shelf life. *[shown_working]*
- Expiry reminders and value-at-risk — Dashboard flags items nearing expiry; page says email reminders are sent. *[claimed]*
- Neighborhood marketplace — Post surplus, browse nearby listings with map pins, request pickup; exact location unlocks after approval. *[shown_working]*
- Households and inbox — Shared households with invitations and an inbox tied to approved requests. *[shown_working]*
- Smart locker proof of concept — Credits, site selection, reserve, drop-off and pickup codes in a simulated locker flow. *[shown_working]*
- Impact tracking and leaderboard — Shows dollars saved, items rescued, CO2 avoided and a household leaderboard. *[shown_working]*
- Item enrichment — Cache of shelf-life knowledge, fuzzy grocery matching, optional local Ollama gemma2. *[claimed]*
- Email receipt import via OAuth — Listed as future work. *[planned]*

**Flow:** Sign in and upload a receipt → Review and confirm parsed items into the pantry → Watch expiry flags and reminders → Post surplus to the marketplace → Neighbor requests; owner approves and pickup details unlock → Hand off at a locker or pickup spot → See impact stats

**Prompt:** Figma Make Challenge: show how Figma Make was used in the workflow for ideation, prototyping, iteration or pitching; no design experience needed. Best UI/UX has no description on the page.
**Fit (explicit):** Page says Figma and Figma Make were used for ideation, moodboards, UI direction and prototyping, then the React/Tailwind frontend was built with ChatGPT Codex; design drew on receipts and fruit stickers.  *(targeted: Best UI/UX, Figma Make Challenge)*
**Sponsor tools:** Figma Make (Prototyping and generating the frontend design, core)
**AI:** Receipt text from OCR is enriched by a local fuzzy matcher and an optional Gemma 2 model via Ollama (Gemini free tier was tried first, dropped for rate limits).
**Architecture:** React 19/Vite frontend proxying to a Django REST backend (apps for users, households, posts, lockers, receipts) on SQLite with JWT cookies; OCR and geocoding via Nominatim.
**Novelty:** Combines pantry tracking, a neighbor marketplace and a simulated locker network in one MVP, with a distinct receipt and fruit-sticker visual theme.
**Scope:** medium · working: ~25k LOC across React and Django with docs and a live domain listed; no tests and no video. · polish: Responsive layout, toasts, map, themed branding; README documents setup scripts.
**Claims:** Fully responsive on desktop, mostly mobile | Real-time simulated locker MVP | No waste or savings metrics reported
**Gaps:** Best UI/UX has no public prompt text; Live site not opened
Sources: https://devpost.com/software/neighborfridge, evidence/la-hacks-la-hacks-2026-neighborfridge.json, https://la-hacks-2026.devpost.com/

---

### NeuralLens
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: Agentverse - Search & Discovery of Agents

**What it is:** A six-agent pipeline on Agentverse, reachable from ASI:One chat, that takes a marketing image URL, predicts gaze and brain response, scores it, and returns an edited image with rewritten copy and explanations. The repo also has a web app that does iterative optimization of webpages.
**Problem / user:** Small businesses (a bakery is the example) that cannot afford neuromarketing studies costing tens of thousands of dollars.

**Features**
- Gaze saliency heatmaps — DeepGaze IIE predicts fixation order and duration over the image or rendered page. *[claimed]*
- Brain-response scoring — Meta TRIBE v2 predicts activation; 70k voxels mapped to seven regions (amygdala, striatum, hippocampus, PFC and more). *[claimed]*
- Neural Engagement Score — 0-100 score with zone classification (power zones, attention traps, hidden value, dead zones). *[claimed]*
- Automated image and copy edits — Strategist agent writes instructions; Cloudinary generative edits recolor, replace background, overlay text, remove objects; ready-to-paste copy. *[claimed]*
- Payment gate — Payment agent validates FET or Stripe payment before the pipeline runs. *[claimed]*
- Web app optimization loop — Repo web app: URL or HTML upload, score, one LLM edit, re-score, accept only gains, SSE progress. *[shown_working]*
- Before/after heatmaps — Returns both heatmap sets and NES with plain-English reasons. *[claimed]*

**Flow:** Message NeuralLens on ASI:One with an image URL and request → Payment agent validates payment → Orchestrator runs Sensor, Interpreter, Strategist, Executor → Receive NES before/after, zone analysis, edited image, copy, heatmaps

**Prompt:** Build and register AI agents on Agentverse that are discoverable through ASI:One and turn a user's intent into executable outcomes.
**Fit (explicit):** Six agents (Payment, Orchestrator, Sensor, Interpreter, Strategist, Executor) are registered on Agentverse with Chat and Payment protocols and invoked via ASI:One without a custom frontend.  *(targeted: Track: Agentverse - Search & Discovery of Agents)*
**Sponsor tools:** Fetch.ai Agentverse / uAgents (Six-agent pipeline and payment protocol, core); ASI:One (User entry point and orchestration LLM, core); Cloudinary (Generative image edits, supporting)
**AI:** TRIBE v2 fMRI-encoder and DeepGaze IIE as predictors served from an A100; an LLM agent proposes edits and ASI:One orchestrates; Cloudinary AI applies image changes.
**Architecture:** Playwright renders pages; GPU endpoint serves TRIBE and gaze models; agents pass JSON strings through Agentverse; FastAPI/React web app streams the optimization loop over SSE.
**Novelty:** Applies a newly released brain-encoding model to small-business marketing; team built its own serving layer and voxel-to-region mapping. Scores are predictions, unvalidated.
**Scope:** medium · working: ~18k LOC, tests, separate web app, CLI and agent integrations; page reports no outcome measurements. · polish: README with architecture diagram; six screenshots on page; no video.
**Claims:** First team to apply TRIBE v2 to small-business marketing | Neuromarketing studies cost about $50,000 each versus planned $99/month SaaS | Page counts five agents in one place, six in another
**Gaps:** NES not validated; Web app optimization loop is README-described; Agentverse flow not shown on video
Sources: https://devpost.com/software/neurolens-2qgdm8, evidence/la-hacks-la-hacks-2026-neurallens.json, https://la-hacks-2026.devpost.com/

---

### Nimbus
*LA Hacks LA Hacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Arista Networks: Connect the Dots Challenge; Winner High Quality Sponsormaxxing

**What it is:** A self-hosted cloud platform, packaged as one Go binary, that gives a Proxmox cluster an EC2-like portal: provision VMs with static IPs in about 30-60 seconds, expose them via public HTTPS tunnels, plus MinIO storage and a GPU inference plane.
**Problem / user:** Student orgs and self-hosters with spare hardware; the origin story is a club paying about $3,600/year to AWS while manual Proxmox provisioning was a chore.

**Features**
- Two-click VM provisioning — Nine-step flow over the Proxmox API: reserve IP, score nodes, clone, cloud-init, boot, wait for guest agent. *[shown_working]*
- Setup wizard and dashboard — Connect Proxmox token, choose IP range, create admin; dashboard shows nodes, VMs, IP pool and gauges. *[shown_working]*
- Public tunnels — Gopher reverse-tunnel integration gives public SSH and per-port HTTP/TCP/UDP subdomains with Caddy TLS. *[claimed]*
- Multi-tenant auth — Email, GitHub and Google OAuth, access code, org allow-list, per-user quotas, audit log. *[claimed]*
- SSH key vault — Generate Ed25519 pairs server-side or import keys; private halves stored and downloadable. *[claimed]*
- Object storage — One-click MinIO with per-user buckets, S3 compatible. *[claimed]*
- GPU plane — Always-on OpenAI-compatible vLLM on an NVIDIA GX10 plus FIFO container job worker; VMs get OPENAI_BASE_URL. *[claimed]*
- Cluster ops — Cordon, drain, live migrate and SDN modes (standalone or VPC) described in README. *[claimed]*

**Flow:** Run setup wizard against a Proxmox cluster → Sign in via GitHub, Google or password → Create a machine: hostname, OS, tier → Watch provisioning progress → Get SSH details and optional public tunnel → Manage machines, storage or GPU jobs

**Prompt:** Arista Networks Connect the Dots: apply networking to build a software solution that improves everyday life. High Quality Sponsormaxxing has no description on the page.
**Fit (implied):** Networking is central: per-VM SDN subnets, VXLAN VPC mode, IP pool management and reverse-tunnel gateway with automatic HTTPS subdomains, aimed at replacing paid cloud for clubs. Page does not name Arista products.  *(targeted: Arista Networks: Connect the Dots Challenge, High Quality Sponsormaxxing)*
**AI:** No AI in the provisioning logic; GX10 hosts a Phi-3-mini vLLM inference server and GPU job runner as a platform service.
**Architecture:** Single Go binary embeds a React SPA, drives Proxmox REST, stores state in SQLite; Gopher/rathole plus Caddy for tunnels, MinIO for S3, vLLM on the GPU host.
**Novelty:** Infrastructure product rather than app: full provisioning, tenancy, tunneling, storage and GPU planes built on five laptops in 36 hours; builds on an earlier tunnel project.
**Scope:** large · working: ~82k LOC Go and React, CI present, live instance listed, hardware cluster described; no tests directory detected. · polish: Extensive README with install wizard and architecture notes; multi-tenant hardening described.
**Claims:** VM ready in 30-60 seconds | Club saves roughly $3,600/year versus AWS | Built multi-node cluster, tunnels, S3 and GPU plane in 36 hours
**Gaps:** README likely describes later work than the hackathon build (features beyond the Devpost list); High Quality Sponsormaxxing criteria not public
Sources: https://devpost.com/software/nimbus-q025jc, evidence/la-hacks-la-hacks-2026-nimbus.json, https://la-hacks-2026.devpost.com/

---

### Northstar
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Track: Agentverse - Search & Discovery of Agents

**What it is:** A hiking-safety mobile app that detects falls, runs voice triage with on-device models, estimates vitals with the camera, uses Agentverse agents to find care, and phones the emergency contact with an assessment.
**Problem / user:** Solo hikers and bikers who get injured in areas with poor signal and may be unable to type or conscious.

**Features**
- Fall detection — Accelerometer spikes plus YAMNet audio classification for pain sounds trigger a check-in. *[claimed]*
- Offline voice triage — Local Qwen 3.5-4B via Zetic Melange builds an injury assessment in the background. *[claimed]*
- Camera vitals — Photoplethysmography from back camera and flash estimates heart rate and blood pressure. *[claimed]*
- Agent swarm — Specialized Agentverse agents locate nearest care and other key information. *[claimed]*
- Automated emergency call and SMS — Twilio plus ElevenLabs voice place a call to the contact with the assessment, via satellite connectivity. *[claimed]*
- 3D map UI scaffold — Expo app with photorealistic Google 3D tiles map and brand UI; README says ML modules still to land. *[shown_working]*

**Flow:** App detects a fall or pain sound → Voice triage runs on device → Vitals measured with the camera → Agents search for help → Call and text sent to emergency contact

**Prompt:** Build and register AI agents on Agentverse that are discoverable through ASI:One and turn a user's intent into executable outcomes.
**Fit (explicit):** Rescue coordination is handled by specialized Agentverse agents (README names Location Scout, Medical Coordinator, Contact Orchestrator), while triage and detection run on-device with Zetic Melange.  *(targeted: Track: Agentverse - Search & Discovery of Agents, Zetic Company Challenge)*
**Sponsor tools:** Fetch.ai Agentverse (Agent swarm for locating care and coordinating contact, core); Zetic Melange (On-device Qwen triage and YAMNet audio, core); ElevenLabs / Twilio (Voice dispatch call and SMS, supporting)
**AI:** Local Qwen 3.5-4B for triage and summaries, YAMNet for pain-sound detection, optical PPG for vitals, and Agentverse agents for lookup; ElevenLabs voices the call.
**Architecture:** Expo/React Native app with a Swift bridge for Zetic models; Agentverse agents in agents/; a bridge process connects data to ElevenLabs and Twilio calls.
**Novelty:** Offline-first emergency flow that combines on-device LLM triage, optical vitals and an agent-driven outbound call, aimed at users who cannot interact.
**Scope:** medium · working: ~15k LOC with ios, agents and app dirs; README itself says the ML modules had not yet landed in the scaffold. · polish: Polished map UI and design tokens; no demo video or live link; no tests.
**Claims:** Over half of hiking injuries are slips and falls (cited, not measured) | Got Qwen and YAMNet running on mobile hardware | No accuracy or latency figures given
**Gaps:** README describes a scaffold and says ML parts pending, Devpost claims them working; feature list follows Devpost with status claimed; Satellite connectivity mechanism unclear; No demo video
Sources: https://devpost.com/software/northstar-7lcg45, evidence/la-hacks-la-hacks-2026-northstar.json, https://la-hacks-2026.devpost.com/

---

### Polaris
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Best Social Impact Hack

**What it is:** MedPage, a realtime hospital paging system: an operator types or speaks an alert, agents classify priority, pick the best available clinician by specialty, zone and caseload, page them, escalate on timeout, and write a short SBAR brief on acceptance.
**Problem / user:** Floor nurses and operators who page doctors manually, and clinicians who arrive at the bedside with little context.

**Features**
- Alert intake and triage — Text or voice (voice endpoint) alerts are classified P1-P4 with room, specialty and symptoms extracted; EHR looked up by room. *[shown_working]*
- Clinician ranking — Scores by specialty, zone proximity, on-call status and caseload, LLM re-rank with deterministic fallback, spreads load among near ties. *[shown_working]*
- Autonomy and guardrails — Per-zone and priority rules decide operator review; no repeat paging within 5 minutes; workload caps on low-priority pages. *[claimed]*
- Auto-escalation — Timeout-tracked queue moves to backup clinicians on decline or timeout. *[shown_working]*
- Clinician accept/decline view — One-tap response on phone or tablet page; SBAR under 100 words generated on accept. *[shown_working]*
- Sentinel agent — Every 30 seconds looks for zone concentration, coverage gaps and overloaded clinicians and advises the operator only. *[claimed]*
- Operator dashboard and realtime — Shows decision reasoning, queue, escalation chain; Socket.IO pushes updates. *[shown_working]*
- ASI:One access — Agents callable through the uAgents Chat Protocol. *[claimed]*

**Flow:** Operator opens /operator and submits a text or voice alert → Pipeline classifies, finds EHR, ranks clinicians → Autonomy policy decides if review is needed → Page created and queued; operator sees reasoning and backups → Clinician accepts or declines → Accept yields an SBAR brief; decline or timeout escalates

**Prompt:** Best Social Impact Hack is listed on the hackathon page as a prize with no description.
**Fit (implied):** Addresses hospital paging delays and unsafe escalation; no sponsor or prize statement on the page says how. Also uses Fetch.ai agents callable from ASI:One.  *(targeted: Best Social Impact Hack)*
**Sponsor tools:** Fetch.ai uAgents / ASI-1 Mini (Four agents and LLM classification, re-ranking, SBAR and sentinel interpretation, core)
**AI:** ASI-1 Mini classifies priority, re-ranks candidates, writes SBAR briefs and interprets sentinel patterns, with regex or deterministic fallback and an 8-second SBAR cap.
**Architecture:** Next.js operator and clinician UIs behind nginx; FastAPI dispatch and Flask plus Socket.IO management API; four uAgents (operator, priority, case, sentinel); TinyDB mock EHR; EC2 deployment.
**Novelty:** Models paging as a guarded, auditable pipeline with autonomy levels and a passive observer agent; fallbacks at every LLM step; mock EHR only.
**Scope:** medium · working: ~19k LOC, live EC2 demo URL, documented REST endpoints; mock data, no tests. · polish: Two role-specific UIs, systemd deploy script, README endpoint tables; no video.
**Claims:** End-to-end dispatch in about 2-5 seconds including LLM calls | SBAR briefs under 100 words | No clinical accuracy or pilot data
**Gaps:** Social Impact prize text not public; Project is called MedPage in README, Polaris on Devpost; Live demo not opened
Sources: https://devpost.com/software/polaris-mh7rd8, evidence/la-hacks-la-hacks-2026-polaris.json, https://la-hacks-2026.devpost.com/

---

### Pols 15
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: Agentverse - Search & Discovery of Agents

**What it is:** Stump, a campaign toolbox on Agentverse: a candidate uploads a policy and agents simulate how seven demographic clusters react, produce a decision brief and 3D impact map, let the candidate chat with cluster personas, draft social posts, and compare real replies to predictions.
**Problem / user:** First-time and local candidates (school board, city council) who cannot afford polling and learn voter reaction only after announcing a position.

**Features**
- Policy upload and simulation — PDF, text or ASI:1 chat input; seven cluster agents run multi-round persona debates in parallel. *[shown_working]*
- Decision brief — Report agent synthesizes verdicts and quotes per cluster in markdown. *[shown_working]*
- 3D impact globe and stakeholder graph — Forked Mapbox globe with clickable cluster zones plus D3 knowledge graph. *[claimed]*
- Chat with cluster personas — Each cluster agent stays in character with memory, e.g. a gig worker. *[claimed]*
- Social drafts and posting — Drafts for Twitter, Reddit, Facebook; posting via Composio gated by $1 Stripe payment per platform. *[claimed]*
- Reality check — Comparison agent classifies actual replies into clusters and compares to simulated predictions. *[claimed]*
- Single-chat orchestration — Orchestrator runs six phases from one ASI:1 message and returns brief, map URL, chat handles and drafts. *[shown_working]*

**Flow:** Upload a policy PDF or type a request in ASI:1 chat → Orchestrator runs six phases (60-120 s) → Receive brief, map URL, cluster handles, drafts → Chat with a cluster persona → Pay and post to social platforms → Run reality check on real replies

**Prompt:** Build and register AI agents on Agentverse that are discoverable through ASI:One and turn a user's intent into executable outcomes.
**Fit (explicit):** README states 12-14 discoverable agents on Agentverse with an ASI:1 chat entry point, mailbox plus HTTP agent-to-agent transport, a shared state envelope, and a Stripe payment protocol.  *(targeted: Track: Agentverse - Search & Discovery of Agents)*
**Sponsor tools:** Fetch.ai Agentverse / ASI:1 (All agents, chat entry, LLM work and payment protocol, core); Stripe and Composio (Payment gate and social posting, supporting)
**AI:** ASI:1 does parsing, persona generation, 8 calls per cluster across rounds, brief synthesis, reply classification and draft writing; GraphRAG-style agent extracts entities from policy text.
**Architecture:** Orchestrator chains graphrag, env-config, cluster, report, map, social and comparison agents passing a SharedAgentState over HTTP; Vite/React frontend with Mapbox and D3.
**Novelty:** Large agent count with every agent individually discoverable, a closed loop from simulation to posting to measured reaction, and a payment-gated posting step.
**Scope:** medium · working: README gives live ASI:1 chat link and agent profile URLs; ~7.5k LOC; video embedded on page; no tests. · polish: Detailed README table of agents, web frontend with embed mode.
**Claims:** Pipeline runs in 60-120 seconds | Inter-agent latency cut from 60-90 s to about 1 s per hop | Page says twelve agents but lists about fourteen
**Gaps:** Agent count inconsistent; Cluster accuracy not measured; Video not opened
Sources: https://devpost.com/software/pols-15, evidence/la-hacks-la-hacks-2026-pols-15.json, https://la-hacks-2026.devpost.com/

---

### Residue
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: Agentverse - Search & Discovery of Agents

**What it is:** A study-environment web app that listens to room sound, estimates productivity from screen activity and self-reports, learns a personal best acoustic profile, then recommends or generates soundscapes and matches study buddies by acoustic similarity. A Swift iPhone companion tracks phone distraction.
**Problem / user:** College students who track study time but guess at which noise level or sound environment helps them focus.

**Features**
- Live acoustic analysis — Web Audio API computes dB, FFT, seven bands, dominant frequency and spectral centroid in the browser. *[shown_working]*
- Productivity estimate — Screen Capture frame differences give a 0-100 activity score plus 1-5 self-reports. *[claimed]*
- Personal focus profile — Buckets sound levels and frequency profiles at best moments; recommends if too quiet, loud or mismatched. *[claimed]*
- Soundscapes — Browser noise, rain, cafe and binaural overlays; ElevenLabs generates a saved ambient bed from the profile. *[claimed]*
- Study buddy matching — Cosine similarity on frequency vectors, optionally Atlas Vector Search, with location and status. *[claimed]*
- iOS phone companion — Pairing code, open/close/heartbeat events, unlock counts; Zetic Melange Qwen produces on-device distraction reports. *[claimed]*
- Multi-agent layer — Perception, correlation, intervention, orchestrator and matching agents on uAgents with ASI1-Mini fallback. *[claimed]*
- Bayesian profile model — Posterior estimates and confounders; page says not fully wired into the dashboard. *[planned]*

**Flow:** Sign in and choose a study mode → Start a session and allow microphone → Screen activity and self-reports track productivity → Optionally pair the phone → Profile learns across sessions → Get recommendations, soundscapes or buddy matches

**Prompt:** Build and register AI agents on Agentverse that are discoverable through ASI:One and turn a user's intent into executable outcomes.
**Fit (explicit):** README describes a four-to-five agent system on Fetch.ai uAgents with ASI1-Mini reasoning, plus helper agents reachable via ASI:One chat; the core study tool is a standalone web app.  *(targeted: Track: Agentverse - Search & Discovery of Agents)*
**Sponsor tools:** Fetch.ai uAgents / ASI1-Mini (Perception, correlation, intervention and matching agents, core); ZETIC Melange (On-device Qwen distraction report on iOS, supporting); MongoDB Atlas (Persistence and optional vector search, supporting); ElevenLabs (Generated ambient beds, supporting)
**AI:** Closed-loop personal model of sound to productivity; ASI1-Mini reasons over perception and interventions; ElevenLabs sound generation; local Qwen on iPhone; cosine similarity for matching.
**Architecture:** Next.js app with browser audio and screen analysis, MongoDB persistence, Python uAgents orchestrator with Next.js API fallback, and an iOS Swift companion app.
**Novelty:** Frames personalized acoustic biofeedback as a learning loop and spans web, agents and phone; team pivoted from a map app mid-hackathon, leaving the Bayesian part unfinished.
**Scope:** medium · working: ~17k LOC across src, ios and scripts with a demo video; no tests. · polish: README with mermaid architecture; self-described unwired parts show integration gaps.
**Claims:** Called the first consumer application of personalized acoustic biofeedback | No user studies or productivity measurements
**Gaps:** Real-time frequency shaping in README versus soundscape overlay on page: feature list follows the Devpost page; Video not opened
Sources: https://devpost.com/software/residue, evidence/la-hacks-la-hacks-2026-residue.json, https://la-hacks-2026.devpost.com/

---

### RIIS
*LA Hacks LA Hacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner 2nd Overall [2nd]; Winner Fetch.ai: Best Use of ASI:One

**What it is:** A search-and-rescue system: a sub-$200 PiCar-X rover enters a collapsed structure, detects survivors with pose detection, triggers a four-agent Fetch.ai chain that writes a triage report and speaks to them in their language, and reconstructs the scene as a 3D Gaussian Splat for a VR walkthrough.
**Problem / user:** Incident commanders and first responders who cannot safely enter collapsed buildings, and trapped survivors who need contact and care early.

**Features**
- Rover scouting — PiCar-X on Raspberry Pi 5 navigates and streams JPEG frames over WebSocket to the dashboard *[shown_working]*
- Survivor pose detection — YOLOv8-pose on the operator laptop draws skeleton overlays, with a latch against frame dropouts *[shown_working]*
- Four-agent chain — Scout detects, Triage drafts an SBAR report with ASI-1 Mini, Comms voices contact, Mapping starts reconstruction *[shown_working]*
- Multilingual voice contact — ElevenLabs pre-rendered audio, Spanish in demo, English and Chinese supported *[shown_working]*
- 3D reconstruction and VR — MASt3R poses plus InstantSplat build a splat viewed in Unity on Meta Quest 2 with breadcrumb trail and survivor marker *[shown_working]*
- Operator dashboard — Dark browser UI with live annotated video, SSE events and rover control; replay mode without rover *[shown_working]*
- Offline Gemma triage extraction — Gemma 2 extracts triage fields for the dashboard *[claimed]*

**Flow:** Send rover into the structure → Dashboard shows live video with skeleton overlay → Detection triggers agent chain → SBAR report generated and Spanish audio plays at rover → Frames reconstructed into splat → Commander walks through scene in Quest 2

**Prompt:** Fetch.ai Best Use of ASI:One: listed only as a late add-on challenge with no description on the main Devpost page. Overall prizes judged on technical depth, product impact, execution and originality.
**Fit (explicit):** README's sponsor table maps ASI-1 Mini to generating the SBAR triage report from each detection event and Fetch.ai uAgents to a four-agent chain on Agentverse.  *(targeted: 2nd Overall, Fetch.ai: Best Use of ASI:One)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse (Scout, Triage, Comms, Mapping agent chain, core); ASI-1 Mini (Generate SBAR triage report, core); ElevenLabs (Multilingual survivor audio, supporting); Gemma 2 (Offline triage extraction, supporting)
**AI:** YOLOv8n-pose detection; ASI-1 Mini writes SBAR reports; MASt3R and InstantSplat for 3D reconstruction; ElevenLabs TTS; Gemma 2 for offline extraction.
**Architecture:** Rover streams over WebSocket to a FastAPI dashboard running YOLO; detection event fires uAgents chain; frames archived to a GPU pipeline producing a .ply/.splat for Unity on Quest 2.
**Novelty:** Combines low-cost robot, agent triage, multilingual voice and splat-based VR reconstruction in one pipeline; five independently runnable components with mock modes.
**Scope:** medium · working: Claims end-to-end run with real rover hardware, screenshots of splat and detection; no video or measured results. · polish: Clear README with sponsor table and fallbacks for off-hardware running; tests present.
**Claims:** Rover costs under $200 | Target of under 60 seconds for reconstruction listed as next step
**Gaps:** No demo video listed; ASI:One prize has no public description
Sources: https://devpost.com/software/riis, evidence/la-hacks-la-hacks-2026-riis.json, https://la-hacks-2026.devpost.com/

---

### SPECTRA
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Track: Flicker To Flow

**What it is:** SPECTRA turns the sparse 192x256 depth from an iPhone Pro's LiDAR into a dense 768x1024 metric depth map using a 2 MB RGB-guided network (SPECTRANet), shown in an iOS app that can run on-device via CoreML or on a remote edge GPU.
**Problem / user:** Robotics, AR and accessibility developers who want cheap consumer LiDAR to give usable dense depth for obstacles like chair legs and wires.

**Features**
- SPECTRANet depth upsampler — MobileNetV2 RGB encoder plus depth and confidence encoder; predicts a residual over bicubic upsampling. *[claimed]*
- On-device inference — fp16 CoreML model (~2 MB) loaded through ZeticMLange; 15 Hz ARFrame processing. *[claimed]*
- Remote backend — FastAPI server on an ASUS Ascent GX10 can serve the model; app switches backends. *[claimed]*
- Live Depth mode — Raw LiDAR colormap overlay in the SwiftUI/ARKit app. *[claimed]*
- A/B Demo mode — Flip between raw LiDAR and SPECTRANet output on the same frame. *[claimed]*
- Capture and share — Shutter saves an RGB plus depth composite. *[claimed]*
- Temporal consistency and mesh export — Future work: recurrent prior and TSDF mesh. *[planned]*

**Flow:** Open SPECTRALive on an iPhone Pro → View raw LiDAR overlay → Switch to SPECTRANet on-device or remote → Use Demo mode to flip A/B → Capture a composite

**Prompt:** Flicker To Flow track: how can we turn the flickers of a chaotic world into a flow state, improving how people work, play and connect.
**Fit (implied):** Page does not tie the work to the track theme; it targets embodied-AI depth perception and uses ZeticMLange for on-device deployment, which is how it ties to the Zetic challenge.  *(targeted: Track: Flicker To Flow, Zetic Company Challenge)*
**Sponsor tools:** ZeticMLange (Run the CoreML depth model on iPhone, core); ASUS Ascent GX10 (Training and remote inference server, supporting)
**AI:** Trained a lightweight guided depth-upsampling CNN on ARKitScenes with laser-scan ground truth; converted to CoreML; no LLM.
**Architecture:** PyTorch SPECTRANet trained on GX10, exported to CoreML; SwiftUI/ARKit app with processor managing on-device and FastAPI remote backends; Vercel demo website.
**Novelty:** A trained vision model deployed on a phone with an offline/edge switch, unusual for a productivity-track entry; no repo link on the page.
**Scope:** small · working: Describes trained model, iOS app and demo website but no repo, video or metrics were available to check. · polish: Demo website at a Vercel URL; challenges section details real conversion work.
**Claims:** ~2 MB fp16 model beats bicubic on edges (qualitative) | Industrial LiDAR $8k-75k versus iPhone sensor $3-25 component cost | No quantitative depth error reported
**Gaps:** No repo linked; No video; Demo site not opened; Page also credits a Zetic challenge win beyond the listed track
Sources: https://devpost.com/software/spectra-qbj2gf, https://la-hacks-2026.devpost.com/

---

### YES? or YES!
*LA Hacks LA Hacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Most Questionable Use of 36 Hours

**What it is:** A joke installation where a caller phones a snarky fish voice agent, gets two bad options shown on a TV behind a tank, three guppies vote by which side they swim on, and a second MacBook automatically carries out the winning action.
**Problem / user:** No practical problem; a deliberately absurd entry for people who want to hand life decisions to fish.

**Features**
- Phone voice agent — Twilio audio goes to Deepgram STT, Claude Haiku 4.5 and ElevenLabs TTS with a sarcastic fish persona locked to three scenarios. *[shown_working]*
- Option display and countdown — Claude calls present_options; the TV page shows A versus B with a timer. *[shown_working]*
- Guppy vote by computer vision — Overhead camera plus OpenCV blob detection counts fish per side at 30 Hz with a 1-second rolling majority. *[shown_working]*
- Real-world dispatch — Remote agent on another MacBook runs Playwright and osascript flows such as iMessage, Outlook draft, LinkedIn post. *[claimed]*
- Realtime event bus — Redis state and five Pusher channels link bridge, display, vision and agent. *[shown_working]*
- Safe fallback — Unrecognized dispatch text does nothing instead of running a default script. *[claimed]*

**Flow:** Call the Twilio number → Fish asks about the situation → Two options appear on the TV → Guppies swim during a countdown → Majority side wins → Second MacBook performs the action on screen

**Prompt:** Most Questionable Use of 36 Hours is listed as a prize with no description on the hackathon page.
**Fit (explicit):** The page calls it the most unhinged use of 36 hours, delegating real decisions to guppies backed by live vision and agent automation.  *(targeted: Most Questionable Use of 36 Hours)*
**AI:** Claude Haiku 4.5 with tools (present_options, wait_for_decision, dispatch_action, report_done) runs the call; Deepgram and ElevenLabs for speech; Anthropic computer use was replaced by scripted runners.
**Architecture:** Node bridge on Fly.io (Twilio, Deepgram, Claude, ElevenLabs), Next.js web with Redis and Pusher, Python OpenCV vision on a Mac mini, Node remote agent on a second MacBook.
**Novelty:** Physical, multi-device build with live animals as the voting input and real side effects on a laptop; scripted runners cut a scenario from about 60 s to 5 s.
**Scope:** medium · working: Four-service repo (~4.5k LOC) with Docker, docs and a demo video; hardware setup described in detail. · polish: Tuned for live demo: debouncing, blob splitting and click fallbacks; no tests.
**Claims:** Sub-second perceived call latency | Scripted scenario about 5 s versus about 60 s with computer use
**Gaps:** Phone number not public; Video not opened; Prize description not public
Sources: https://devpost.com/software/yes-or-yes, evidence/la-hacks-la-hacks-2026-yes-or-yes.json, https://la-hacks-2026.devpost.com/

---

