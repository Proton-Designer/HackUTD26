# DubHacks — DubHacks 2025 (14 projects)

### Artemis
*DubHacks DubHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** GROW - The Advocate

**What it is:** An Electron desktop system that reads gaze and typing signals and then reshapes the environment: closes or minimizes unrelated Chrome tabs, shifts smart-bulb colour, adapts Spotify tempo, and silences phone notifications through an Android app.
**Problem / user:** People with ADHD or focus trouble, especially knowledge workers and developers, whose attention is lost to tab drifting; whole-site blockers are too blunt.

**Features**
- Gaze and blink tracking — MediaPipe plus EyeTrax with calibration quality metrics, Kalman smoothing and variance scaling yield gaze, blink and fixation signals. *[shown_working]*
- Focus metrics and phases — TypeScript computes focus stability, cognitive load, task coherence and a FlowScore; a four-phase model runs Calibration, Engagement, Flow, Recovery. *[claimed]*
- Task-aware Chrome tab control — Chrome DevTools Protocol reads page content; Claude Haiku interprets it so unrelated tabs minimize while relevant docs stay; Focus Lock guards closures. *[shown_working]*
- Adaptive smart lighting — WiZ/LIFX bulbs shift between cool white focus and warm break presets with eased transitions. *[shown_working]*
- Spotify tempo adaptation — Spotify OAuth control ties music tempo and volume to focus intensity. *[shown_working]*
- Android notification and traffic control — Kotlin app uses VpnService with a token-bucket limiter and classifies notifications as surface, delay or suppress. *[claimed]*
- Temporal memory — Stores significant moments with semantic tags and significance scores and retrieves by recency and importance. *[claimed]*
- Real-time dashboard — Glassmorphic Electron UI shows cognitive rhythm graph and live metrics. *[shown_working]*

**Flow:** Start a session with one click and calibrate gaze → Live metrics and rhythm graph update from blinks and keystrokes → Distracting tabs close or minimize while relevant ones stay → Lights and music shift with focus intensity → Phone notifications are silenced for the session

**Prompt:** GROW: The Advocate track celebrates technology strengthening ties between people, rewarding human-centered projects that build belonging and drive positive community change; no prize listed.
**Fit (implied):** Page frames Artemis as support for people with ADHD; it links to the human-centered track only by that accessibility angle, and does not state how it addresses belonging or community.  *(targeted: GROW - The Advocate)*
**Sponsor tools:** Anthropic Claude 3.5 Haiku (Interpreting pre-computed metrics and tab content for tab decisions, core); Spotify Web API (Focus-linked music control, supporting)
**AI:** Claude 3.5 Haiku interprets metrics computed in TypeScript and decides which tabs fit the task, with caching, hashing and rate limits (2-4 calls per hour). Gaze is classical vision plus filtering.
**Architecture:** Perception (webcam gaze via Python JSON-RPC, Chrome CDP, window monitor), interpretation (metrics, LLM), and orchestration layers in an Electron app driving Python lighting and music controllers and an Android companion.
**Novelty:** Joins gaze tracking, LLM tab relevance, ambient light, music and phone notifications in one loop; conservative automation rule and LLM-interprets-only-computed-metrics design.
**Scope:** large · working: Demo video shows tabs closing, lighting and music changes; README marks components Active; self-reported accuracy figures unverified. · polish: 1,155 files, about 16k LOC, Mermaid architecture diagram and detailed README; no tests listed.
**Claims:** Gaze error reduced from 80-150 px to roughly 40-80 px | Kalman filtering cut jitter 60-80% | Over 80% fewer API calls via caching | 2-4 LLM calls per hour
**Gaps:** README mentions Visa payment micro-transactions absent from Devpost body (Devpost mentions Payment API once); feature list follows Devpost; Built-with lists Gemini and Raspberry Pi with no description; video not viewed
Sources: https://devpost.com/software/artemis-kxd36i, https://github.com/tgondil/artemis, https://dubhacks25.devpost.com/

---

### BloomSync AI; CRISPR Apples; Mango
*DubHacks DubHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Okanagan - Hack the Farm of the Future

**What it is:** Three separate Okanagan-track entries: BloomSync AI (RL agent proposing apple flowering-gene edits), CRISPR Apples (Streamlit app mapping plain-language tree traits to candidate genes via Gemini), and Mango (drag-and-drop data science canvas). Grouped here as one queue entry.
**Problem / user:** Apple trees fruit on old wood, hampering mechanized harvest; breeders and agri-tech developers need trait-to-gene design help. Mango targets non-programmers wanting to explore data.

**Features**
- BloomSync gene data aggregation — Gathers Malus domestica data from NCBI, UniProt and GDR and aligns flowering genes FT, TFL1 and AP1 across species. *[claimed]*
- BloomSync RL edit proposals — A REINFORCE-style agent explores sequence edits scored by a neural reward combining FT/TFL1 similarity, edit count and motif feasibility. *[shown_working]*
- BloomSync Tkinter demo — README toy GUI trains in a background thread with selectable objectives such as fruiting on new wood or picking height; explicitly a non-actionable toy. *[shown_working]*
- CRISPR Apples trait interpretation — Gemini extracts traits from plain-language requests like short trees fruiting on new wood. *[shown_working]*
- CRISPR Apples gene suggestions — A curated dictionary maps legacy gene symbols to genome IDs and sequences; app proposes upregulation or knockout strategies and exports sequences for a design tool. *[shown_working]*
- Mango drag-and-drop data canvas — Canvas for cleaning, imputing, transforming data, linear regression, time series and matplotlib graphs with explanations of each step. *[claimed]*

**Flow:** BloomSync: gather genomic data, align genes, RL agent proposes edits, reward model scores them → CRISPR Apples: describe desired traits in the Streamlit app → Gemini extracts traits and app lists candidate genes → App shows edit strategy and sequences → Mango: load data on the canvas and apply cleaning and analysis steps

**Prompt:** Okanagan Hack the Farm of the Future: use bioinformatics, AI and CRISPR gene-editing ideas to design apple tree traits for a resilient food system; three winners.
**Fit (explicit):** BloomSync and CRISPR Apples design apple flowering and architecture traits for orchard automation; Mango is a general data-science tool whose link to apples is not stated on its page (it lists Grow and Okanagan only as README tags).  *(targeted: Okanagan - Hack the Farm of the Future)*
**Sponsor tools:** Google Gemini (CRISPR Apples trait extraction; Mango lists Gemini without explaining, supporting); Amazon Web Services (Hosting/tooling listed for BloomSync and CRISPR Apples, unclear)
**AI:** BloomSync: reinforcement learning agent with neural reward model. CRISPR Apples: Gemini natural-language trait extraction over curated gene dictionary. Mango: Gemini listed, role unspecified.
**Architecture:** BloomSync: Python RL environment, agent, reward model and Tkinter GUI. CRISPR Apples: Streamlit app over curated gene mapping. Mango: React/TypeScript front end with FastAPI backend and matplotlib.
**Novelty:** Applies RL and LLM interfaces to plant genome trait design for orchard automation; entry bundles three unrelated builds.
**Scope:** small · working: CRISPR Apples has a live Streamlit demo link; BloomSync repo is a labelled toy with smoke tests; no videos for any of the three. · polish: BloomSync repo 53 files, about 2.7k LOC; CRISPR Apples shows screenshots; Mango README only has setup.
**Claims:** BloomSync reports no quantitative results and notes limited wet-lab validation data | CRISPR Apples claims a working prototype returning candidate genes and strategies
**Gaps:** queue entry bundles three projects; evidence repo covers BloomSync only; CRISPR Apples repo README fetch failed; Mango README has no feature text so features come from Devpost; unclear which of the three the prize was awarded to; live CRISPR Apples demo not opened
Sources: https://devpost.com/software/bloomsync-ai, https://devpost.com/software/crispr-apples, https://devpost.com/software/mango-1u6a7x, https://github.com/ericyuxuanye/dubhacks25, https://raw.githubusercontent.com/aealni/DubHacksProject/HEAD/README.md, https://dubhacks25.devpost.com/

---

### CareLens; Roam
*DubHacks DubHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** T-Mobile: 5G Challenge

**What it is:** Two separate T-Mobile 5G Challenge entries bundled in one queue item: CareLens, an offline Raspberry Pi camera fall detector that alerts caregivers, and Roam, a pay-per-minute Wi-Fi hotspot marketplace with a Pi gateway and a planned local language model for network management.
**Problem / user:** CareLens: elderly or at-risk people whose pendants fail in emergencies, plus caregivers. Roam: travelers needing paid Wi-Fi and businesses wanting to sell access.

**Features**
- CareLens camera fall detection — OpenCV HOG person detector with centroid tracking and an aspect-ratio and low-motion heuristic on a Raspberry Pi; no cloud needed. *[shown_working]*
- CareLens cancel timer and alerts — A 5-10 second grace period (optional GPIO button) then siren and spoken alert; optional Twilio SMS or call. *[claimed]*
- CareLens multi-agent claim — Devpost says multi-agent AI architecture, offline; README describes only a heuristic pipeline and no agents. *[unclear]*
- Roam map of hotspots — React Native app shows opted-in businesses on Google Maps with prices and offers. *[shown_working]*
- Roam Stripe payment and timed access — Payment triggers a webhook session; Go captive portal on a Pi validates a token and iptables blocks the device on expiry; 20/80 revenue split. *[claimed]*
- Roam SLM network manager — A local Qwen2.5 1.5B model on the Pi meant to flag bad actors, throttle, and turn plain-text commands into scripts; not integrated. *[planned]*

**Flow:** CareLens: camera watches; fall heuristic fires; cancel countdown; local siren/voice alert and optional SMS → Roam: customer opens map and taps a business → Customer pays via Stripe → Within range the device is granted timed Wi-Fi via the Pi captive portal

**Prompt:** T-Mobile 5G Challenge: build AI-driven assistants, broadband apps or autonomous workflows that enhance T-Mobile 5G Home Internet, using a Raspberry Pi to simulate the gateway device; two winners share $2,000.
**Fit (implied):** Both run on Raspberry Pi edge devices; Roam resells network access through a Pi gateway with an on-device language model for network control, CareLens is an offline edge AI app. Neither page cites T-Mobile 5G explicitly.  *(targeted: T-Mobile: 5G Challenge)*
**Sponsor tools:** Stripe (Roam payments for timed Wi-Fi access, core); Google Maps (Roam hotspot map, supporting); Raspberry Pi (CareLens edge detector; Roam gateway, core)
**AI:** CareLens: classical OpenCV HOG detection and rule-based fall heuristic. Roam: planned local Qwen2.5-1.5B quantized model via llama to translate commands to network scripts, not integrated.
**Architecture:** CareLens: single Python script on Pi. Roam: Expo React Native app, Spring Boot backend with Redis and Supabase, Go captive portal on Pi using iptables.
**Novelty:** Roam combines hardware captive portal, Stripe payments and a local LLM idea in a day; CareLens is a minimal offline detector. Bundled entry covers two unrelated projects.
**Scope:** small · working: Roam has a demo site, video and a README with a full payment flow; CareLens repo is 8 files, 319 LOC with a demo heuristic and no video. · polish: Roam README documents endpoints, mock mode and setup; CareLens README gives quick start and config; no tests.
**Claims:** Roam built in a day | CareLens runs fully offline on edge devices | No metrics reported for either
**Gaps:** queue lists only the CareLens repo; Roam repo is separate and repo_signals describe CareLens only; unclear which entry won the prize; CareLens multi-agent claim is not supported by README; videos and live demo not opened
Sources: https://devpost.com/software/carelens-edy2b8, https://devpost.com/software/roam-7h8vbm, https://github.com/jeanchoe/hackaques, https://raw.githubusercontent.com/purelyKai/Roam/HEAD/README.md, https://dubhacks25.devpost.com/

---

### Chameleon
*DubHacks DubHacks 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** DubHacks NEXT

**What it is:** A Chrome extension named Chameleon (repo bridgeui-hub) that detects signs of limited motor control or reading difficulty and adapts web pages, with per-disability settings, Gemini-driven adaptations and Statsig-based interaction analytics.
**Problem / user:** Children, the elderly and people with ADHD, dyslexia, low vision or limited motor control who face standard websites that ignore their needs.

**Features**
- Motor-control detection — Notices repeated missed clicks and enlarges interactive elements and spacing. *[claimed]*
- Disability presets — User picks ADHD, dyslexia, low-vision or motor settings that adjust the page for that need. *[claimed]*
- ADHD mode — Reduces animations, highlights key elements and hides distracting UI. *[claimed]*
- Dyslexia mode — Switches to OpenDyslexic font, adjusts spacing and clarifies link styling. *[claimed]*
- Low-vision mode — Raises zoom and contrast and generates alt-text for user content with Gemini 2.5 Flash. *[claimed]*
- Hands-free control — Python, OpenCV and MediaPipe head-movement and voice control with dwell click. *[claimed]*
- Statsig behavior analytics — Captures clicks, near-misses and hovers on any site without direct integration to optimize layouts in real time. *[claimed]*

**Flow:** Install the Chrome extension → Choose accessibility settings by need → Extension restyles the page → Repeated missed clicks trigger larger targets → Optionally enable head and voice hands-free mode

**Prompt:** DubHacks NEXT: project must demonstrate an innovation that disrupts a market with a clear path to commercial viability; winners got $200 and an expedited interview.
**Fit (none):** Page does not discuss market or commercial path; it positions the extension as an accessibility layer for any website. Statsig is listed in tags.  *(targeted: DubHacks NEXT)*
**Sponsor tools:** Statsig (Interaction telemetry and dynamic UI optimization, supporting); Google Gemini 2.5 Flash (Adapting experiences and generating alt-text, supporting)
**AI:** Gemini 2.5 Flash adapts interfaces and writes alt-text; MediaPipe/OpenCV track head movement for hands-free input; Statsig analytics tune layouts.
**Architecture:** React/TypeScript Chrome extension injecting adaptations into pages, a separate Python OpenCV/MediaPipe hands-free module, Gemini API and Statsig as services.
**Novelty:** Targets several disabilities in one extension and infers motor difficulty from missed clicks; works on arbitrary sites without site cooperation.
**Scope:** small · working: Demo video embedded; no live link; no user testing or metrics reported. · polish: Devpost text is detailed; repo README could not be fetched.
**Claims:** Analytics work on any website without direct integration
**Gaps:** repo clone failed and raw README fetch failed; video not viewed; no stated tie to the NEXT prize criteria
Sources: https://devpost.com/software/robyn-6i4v2u, https://dubhacks25.devpost.com/

---

### ClearVision
*DubHacks DubHacks 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Freshman Beginner's Project

**What it is:** A wearable haptic wristband system that turns depth-camera and vision-language output into directional vibration and spoken alerts for visually impaired users. A Raspberry Pi and cloud pipeline sends intensities over Bluetooth to a microcontroller driving motors.
**Problem / user:** Visually impaired people who rely on a white cane and find existing adaptive tech stigmatizing or unaffordable; wants a discreet wearable.

**Features**
- Object detection with distance — RealSense RGB-D frames; DINO segments labelled objects into masks; masks over depth map give average depth in three vertical regions. *[claimed]*
- Directional haptic feedback — Per-region depth scales vibration intensity; left obstacle buzzes left, closer objects buzz harder. *[claimed]*
- BLE wristband firmware — Pi sends four intensity values over BLE to a Feather nRF52840 that drives DRV2605L drivers through an I2C multiplexer. *[claimed]*
- VLM scene alerts — About every two seconds the latest frame goes to Gemini with a prompt that returns Alert or NA. *[claimed]*
- Spoken alerts — Alert text is converted by ElevenLabs text-to-speech and played on the Pi speaker. *[claimed]*
- Cloud-programmable haptics — Control logic on AWS can trigger preconfigured or real-time haptic patterns remotely. *[claimed]*
- Latency optimizations — Image compression, LRU cache, vectorized depth filtering and lightweight segmentation; SAM removed. *[claimed]*

**Flow:** Camera captures RGB and depth → DINO and depth module compute per-region proximity → Pi sends intensities over BLE to the wristband → Motors vibrate by direction and closeness → Gemini flags scene hazards that ElevenLabs speaks aloud

**Prompt:** Best Freshman Beginner's Project: open only to teams of freshmen new to development; prize an Amazon Echo Pop. MLH Best Use of ElevenLabs (also won) is about natural human-sounding audio.
**Fit (implied):** ElevenLabs text-to-speech delivers spoken hazard alerts; freshman status is implied by the beginner prize but not discussed on the page (team notes first custom firmware).  *(targeted: Best Freshman Beginner's Project, MLH: Best Use of ElevenLabs)*
**Sponsor tools:** ElevenLabs (Text-to-speech for spoken obstacle alerts, core); Google Gemini (Scene-level hazard alert classification, core); AWS (Cloud-hosted control logic and pipeline, supporting)
**AI:** Two-phase perception: DINO segmentation plus depth for per-region proximity, and Gemini as a VLM at about 0.5 Hz for scene alerts, voiced by ElevenLabs.
**Architecture:** RealSense to Raspberry Pi 4B running vision pipeline with AWS offload, BLE to Feather nRF52840 firmware modules, I2C multiplexer and four haptic drivers.
**Novelty:** Full-stack hardware build including first-time custom BLE and I2C firmware, combining segmentation, depth and a VLM into touch plus voice feedback.
**Scope:** small · working: Demo video linked; no latency, accuracy or user-test numbers; claims latency improvements without figures. · polish: Repo 14 files, about 1.4k LOC with an effectively empty README; detailed Devpost write-up.
**Claims:** Significant latency improvements without losing detection accuracy | Two-phase VLM plus segmentation and depth pipeline
**Gaps:** repo README holds only a link so no feature text; video not viewed; Devpost says three buzzers but lists four haptic drivers; queue lists only Best Freshman prize but page also claims ElevenLabs win
Sources: https://devpost.com/software/clearvision, https://github.com/aditya0shah/clearVision, https://dubhacks25.devpost.com/

---

### CodeGraph
*DubHacks DubHacks 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Atlassian: Best Use of Forge Agents

**What it is:** CodeGraph is an Atlassian Forge app inside Jira that takes a GitHub repository, uses Gemini models to classify functions, classes and dependencies, and renders an interactive directed-graph map of the code, with a Rovo agent bridge.
**Problem / user:** New contributors, especially UW student developers inheriting hackathon, lab or club codebases, lose hours working out how an unfamiliar repo fits together.

**Features**
- Repo to dependency graph — Ingests a GitHub repository and builds a directed graph of files, functions, classes and architectural blocks through Gemini parsing. *[shown_working]*
- Cross-file DAG abstraction layer — Custom layer links inter-file and intra-file dependencies and groups logic into flows such as routing to controllers to utilities to I/O. *[claimed]*
- Incremental batching — Large repositories are analyzed in batches to avoid timeouts and context-window limits. *[claimed]*
- PageRank node sizing and interactive UI — Nodes scale with PageRank; the UI offers graph components, themes and node interactions. *[shown_working]*
- Forge app in Jira — Runs as an Atlassian Forge app reachable from Jira. *[shown_working]*
- Rovo CodeGraph agent bridge — A Forge Bridge shim exposes graph data to a Rovo agent; direct invocation from custom UI is not yet supported. *[claimed]*
- Contribution scoring — Planned measure of contribution beyond commits and lines. *[planned]*

**Flow:** Open the Jira Forge app → Submit a GitHub repository → Gemini-backed analysis builds the graph → Explore nodes and themes in the interactive map → Optionally ask the Rovo agent about the graph

**Prompt:** Atlassian Best Use of Forge Agents: build apps or automations on Forge that extend Jira, Confluence, Bitbucket or Trello to improve collaboration, productivity or DevOps; three winners.
**Fit (explicit):** Delivered as a Forge app in Jira with a Rovo agent integration and Forge Bridge shim; page also says it uses Forge beyond UI extensions by combining several APIs.  *(targeted: Atlassian: Best Use of Forge Agents)*
**Sponsor tools:** Atlassian Forge (Host app inside Jira and bridge shim, core); Atlassian Rovo (CodeGraph agent reading graph data, supporting); Google Gemini (Parsing and classifying code structure and dependencies, core)
**AI:** Gemini models parse code into functions, classes and blocks and infer dependencies; strict prompting and grounding limit hallucinated edges; batching handles context limits.
**Architecture:** React/Node Forge app calls GitHub API, runs batched Gemini analysis into a custom DAG layer with PageRank, renders in the UI and exposes data to Rovo via a bridge shim.
**Novelty:** Uses an LLM agent for semantic program analysis packaged as a Jira-native Forge app, with PageRank weighting of nodes.
**Scope:** medium · working: Live Jira app link and Loom demo listed; no accuracy numbers. · polish: Repo README is only a title and counts about 9.4k files, likely vendored dependencies; screenshots in gallery.
**Claims:** Winner of Best Use of Forge Agents | Scales to large repos via incremental batching
**Gaps:** repo README contains only a title; video and Jira demo not opened; queue slug also names Spendify and TaskFlow, which are separate entries in this repo not covered
Sources: https://devpost.com/software/directedacycliccodebase, https://github.com/CosmicOdyssey/DubHacks-2025/, https://dubhacks25.devpost.com/

---

### DubOps; Wellify.AI; Bond - Find Your Own Community
*DubHacks DubHacks 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Use of AI by AWS

**What it is:** Three AWS-track entries: DubOps analyzes a GitHub repo with an LLM and opens a pull request with Terraform and Dockerfiles; Wellify.AI is a Bedrock health-navigation assistant; Bond is an Android app that finds nearby people with shared interests over Bluetooth and tracks time together.
**Problem / user:** DubOps: developers who find deployment config tedious. Wellify.AI: students confused by insurance and care options. Bond: students and newcomers who rarely learn who shares their interests.

**Features**
- DubOps repo analysis — Flask backend sends directory and file structure to an LLM on Bedrock to infer stack and deployment settings, with schema-strict JSON. *[claimed]*
- DubOps IaC and pull request — Generates Terraform scripts and Dockerfiles and opens a GitHub PR via GitPython after the user reviews and fills missing inputs. *[claimed]*
- Wellify symptom checker — Text or speech input classified for urgency (campus clinic, urgent care, home care) by a SageMaker LLM; Transcribe handles speech. *[claimed]*
- Wellify insurance assistant — Bedrock chatbot extracts coverage details from insurance documents to show covered providers. *[claimed]*
- Wellify logistics connectors — Modular connectors for rides, meal delivery and pharmacy ordering with OAuth, rate limiting and token storage. *[claimed]*
- Bond BLE proximity — Android phones advertise and scan Bluetooth Low Energy under a Heart Rate UUID payload to find nearby users indoors. *[claimed]*
- Bond AI matching — Voice note transcribed by Transcribe, distilled by Nova Micro, embedded by Titan; similarity score and shared-interest icebreakers. *[claimed]*
- Bond Time With dashboard — Counts shared minutes between bonded users in BLE range, one write per minute, with weekly stats and streaks. *[claimed]*

**Flow:** DubOps: analyze repo, review and fill inputs, generate files and PR, deploy → Wellify: log in, ask a question or describe symptoms, get urgency and logistics options → Bond: record a voice note, see nearby matches sorted by similarity, send and accept bond requests, track time together

**Prompt:** Best Use of AI by AWS: use SageMaker AI and Bedrock to build AI-powered, distributed, student-focused applications such as tutoring or study tools; three winners.
**Fit (explicit):** DubOps uses Bedrock as its LLM gateway; Wellify uses Bedrock, SageMaker, Cognito and Transcribe; Bond uses Bedrock Nova models and Transcribe. Wellify and Bond are student-oriented.  *(targeted: Best Use of AI by AWS)*
**Sponsor tools:** AWS Bedrock (LLM access for DubOps analysis, Wellify chat and Bond profile distillation and embeddings, core); AWS SageMaker (Wellify symptom reasoning model, supporting); Amazon Transcribe (Speech to text in Wellify and Bond, supporting)
**AI:** DubOps prompts an LLM with few-shot and chain-of-thought examples and enforces JSON schema; Wellify uses Bedrock chat plus a SageMaker classifier; Bond uses Nova Micro and Titan embeddings for similarity.
**Architecture:** DubOps: Next.js front end, Flask backend, Bedrock, GitHub API. Wellify: React, FastAPI, Cognito, Bedrock/SageMaker, DynamoDB. Bond: Kotlin Compose app, BLE, Firebase and Cloud Functions calling AWS.
**Novelty:** Entry bundles three unrelated AWS builds; DubOps generates deployment IaC as a reviewable PR, Bond uses BLE time-together tracking.
**Scope:** small · working: DubOps has a Loom demo, Bond a Vimeo demo, Wellify a described working prototype; no live links or measured results. · polish: Devpost pages are detailed; DubOps repo evidence was unreadable (clone failed).
**Claims:** DubOps one click zero DevOps hassle headline, though flow needs review and PR acceptance | Bond self-scores 8/8 on functionality, design, creativity and track fit
**Gaps:** DubOps repo clone and raw README fetch both failed; queue entry bundles three projects with only the DubOps repo; unclear which entry(ies) won the prize; Wellify and Bond pages each state the win; videos not viewed
Sources: https://devpost.com/software/dubops, https://devpost.com/software/wellify-ai, https://devpost.com/software/bond-xuhodw, https://dubhacks25.devpost.com/

---

### glimpse
*DubHacks DubHacks 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Statsig Hackathon Challenge: AI That Learns What Works

**What it is:** A web photo editor with an AI chatbot beside it that can read the current edit state, apply requested edits in natural language, and predict suggestions from the user's editing behavior. Statsig tracks usage and configures the model.
**Problem / user:** Beginner photo editors face steep learning curves and prices; two photographers wanted an easier editor that still serves experienced users.

**Features**
- Natural-language editing chatbot — Chat panel reads the image state and applies edits, such as raising saturation and contrast when asked to make colors pop. *[shown_working]*
- Predictive suggestions — Watches repeated edit actions, e.g. lowering brightness, and suggests continuing to a target level. *[claimed]*
- Fast CSS-filter preview — Edits preview instantly with CSS filters; actual pixel changes are applied only when the user downloads. *[shown_working]*
- Cost-saving image state — Photo state is stored in a compact LLM-readable form instead of resending the image to the model. *[claimed]*
- Statsig analytics and dynamic config — Logs front-end and back-end operations, derives global usage trends and configures the LLM dynamically. *[claimed]*

**Flow:** Open the photo in the editor → Edit manually or ask the chatbot for a change → Receive predicted suggestions based on actions → Preview edits instantly → Download to apply pixel changes

**Prompt:** Statsig Challenge, AI That Learns What Works: build an AI-powered product that uses Statsig to experiment, personalize or optimize; judged on AI creativity, effective Statsig use (flags, experiments, dynamic configs), impact metrics and polished demos.
**Fit (explicit):** Uses Statsig for analytics, operation logging, dynamic LLM configuration and global user-trend insights to improve the editor, alongside predictive suggestions.  *(targeted: Statsig: AI That Learns What Works)*
**Sponsor tools:** Statsig (User analytics, operation logging, dynamic LLM configuration, global trend insights, core); Google Gemini (Chatbot, later replacing local Gemma 2B, core)
**AI:** Chat LLM first Gemma 2B via Ollama, later Gemini API; edits are driven by a compact state description of the image rather than pixels; suggestions are predicted from the user's action history.
**Architecture:** Next.js/React/Tailwind front end with Python FastAPI backend calling Gemini and Statsig; browser applies CSS filters for preview and processes pixels at export.
**Novelty:** Pairs a deliberately lightweight editor with an agent that edits via state description to avoid image-processing costs, using Statsig to feed back usage trends.
**Scope:** small · working: Two screenshots of a sample edit and a conversation; no demo link or video. · polish: Detailed Devpost write-up; repo not readable; no metrics.
**Claims:** Gemini gave much more detailed responses than Gemma 2B (qualitative)
**Gaps:** repo clone and raw README fetch failed; repo is named DUBHACKS-2026 though event is DubHacks 2025; no video or demo
Sources: https://devpost.com/software/glimpse-sd9p2y, https://dubhacks25.devpost.com/

---

### Math Sandbox
*DubHacks DubHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** INVENT - The Innovator

**What it is:** A projector-and-camera tabletop where handwritten equations on paper are read by Gemini, converted to SymPy and graphed live on the workspace, inspired by Dynamicland. Cards with math formatting can be added and interact.
**Problem / user:** People exploring functions together who want a shared physical space for math; no specific audience named.

**Features**
- Handwriting to SymPy — Gemini reads a handwritten equation from the camera and outputs SymPy syntax, returning a sentinel string when unsure. *[shown_working]*
- Live graphing on the table — SymPy with matplotlib plots the parsed function and the projector shows it on the workspace. *[shown_working]*
- Paper as dynamic media — Any paper placed on the surface becomes interactive via projector-camera alignment with OpenCV. *[shown_working]*
- Add card — Creates cards rendering formatted math; cards interact with each other. *[claimed]*
- Parse-failure handling — Sentinel output flags low-confidence or malformed input instead of a fabricated answer. *[claimed]*

**Flow:** Write an equation on paper → Place the paper on the workspace → Camera captures it and Gemini converts to SymPy → Graph appears projected on the sandbox → Add cards to explore interactions

**Prompt:** INVENT: The Innovator: unconventional ideas welcome if they solve real problems; rewards bold, experimental projects that challenge norms with disruptive technologies. No prize listed.
**Fit (implied):** Page offers no explicit link; the physical projector-camera approach to collaborative math, inspired by Dynamicland, is an unconventional interface.  *(targeted: INVENT - The Innovator)*
**Sponsor tools:** Google Gemini (Handwritten equation recognition into SymPy, core)
**AI:** Gemini converts camera images of handwriting to SymPy; prompt tuned to emit SymPy instead of Python code and to return a sentinel when not confident.
**Architecture:** Python app: camera frames to Gemini, SymPy and matplotlib render graphs, OpenCV aligns projector output with camera input.
**Novelty:** Physical, projector-based interface for shared math exploration rather than a screen app; relies on paper as the input medium.
**Scope:** tiny · working: Demo video linked; team calls it a proof of concept with real-time graphing barely optimized. · polish: Repo 18 files, about 800 LOC with a brief README; no live demo.
**Claims:** Proof-of-concept of an ambitious Dynamicland-style idea
**Gaps:** README only gives a short intro and install hint; video not viewed; hardware models not stated
Sources: https://devpost.com/software/interactive-grapher-thingy, https://github.com/lukasmwerner/desmos-in-the-world, https://dubhacks25.devpost.com/

---

### Minty: Digital Tooth Fairy
*DubHacks DubHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** VISA - Play, Pay, Repeat: Reinventing Childhood Joy...

**What it is:** A web app where children earn growing 'value' for each baby tooth by proving daily toothbrushing with a camera photo checked by Gemini Vision; parents set the increment rate and pay out through Stripe when a tooth falls out.
**Problem / user:** Parents who struggle to motivate kids to brush; traditional tooth-fairy money rewards only the end event, not the daily habit. Kids get a lightweight lesson in saving and compound growth.

**Features**
- Tooth portfolio — Each of 20 baby teeth has a monetary value that rises with verified brushes, framed as a stock price *[shown_working]*
- AI brushing verification — Child submits a photo; Gemini Vision checks that a toothbrush is present before value is added *[shown_working]*
- Parent dashboard — Parents create a family, add children, set brushing goals, tooth values and per-brush increment, view history *[shown_working]*
- Child login by family code — Child enters name plus family demo code to see own teeth and balance *[shown_working]*
- Tooth payout via Stripe — Parent approves payment when a tooth falls out; test-mode Stripe transaction recorded in history *[shown_working]*
- Streak and progress tracking — Brush sessions stored per child with streak records and stats *[claimed]*
- Planned social and reward extensions — Leaderboards, sibling gifting, dentist partnership multipliers, marketplace for rewards or charity *[planned]*

**Flow:** Parent creates family account and receives a family code → Parent adds children, sets increment rate and goals → Child logs in with name and code → Child photographs brushing and submits → Gemini verifies and tooth value rises → Child watches portfolio grow daily → Parent approves payout when a tooth falls out

**Prompt:** Reimagine childhood experiences (allowance, trading cards, arcade games) with Visa's payment network: use a public payment API, add gamification or nostalgia, build in security and inclusivity such as parental controls, and deliver a working prototype with demo.
**Fit (explicit):** Turns the tooth-fairy tradition into an allowance-like game with parent-controlled payouts through a public payment API (Stripe, after a failed Visa API attempt), with parental approval as the control.  *(targeted: VISA - Play, Pay, Repeat: Reinventing Childhood Joy with Modern Payments)*
**Sponsor tools:** Visa API (Attempted first for payments; abandoned after config errors, replaced by Stripe, token); Stripe (Test-mode payment of tooth payouts, supporting)
**AI:** Google Gemini Vision API checks whether a submitted photo contains a toothbrush; no other models or prompting detail described.
**Architecture:** Next.js 15 / React 19 / Tailwind frontend with API routes (family, children, brush, verify-brush, purchase, goals); Prisma over PostgreSQL; Gemini for image check; Stripe test mode for payments.
**Novelty:** Casts toothbrushing as an appreciating asset to teach investing and compound growth; combines vision verification with a parent-controlled payout ledger.
**Scope:** small · working: Live Vercel demo link, YouTube video, and README with endpoints and schema; about 3.5k LOC across 37 code files. · polish: Radix/Tailwind component library, Figma planning, custom art; no tests; simple family-code auth.
**Claims:** Delivered functional core product in hackathon time | Vision AI works well when properly prompted
**Gaps:** Video not watched; README says payments and verification work but 'real-time' camera capture vs photo upload differs between Devpost and README; feature list follows README (photo submit)
Sources: https://devpost.com/software/minty-4vcu9m, evidence/dubhacks-dubhacks-2025-minty-digital-tooth-fairy.json (README), https://dubhacks25.devpost.com/

---

### NeuroMapping: Low-Cost Cognitive Safety System
*DubHacks DubHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Prizes in Kind

**What it is:** A mostly conceptual, software-first cognitive-risk system that takes simulated EEG signals through a CNN plus Transformer ensemble and presents risk scores, brain-region heatmaps and community engagement tracking in a dashboard.
**Problem / user:** Early cognitive-risk detection is costly and out of reach in low-resource communities; aimed at elderly people and caregivers, with clinics, NGOs and workplaces as secondary users.

**Features**
- Cognitive heatmaps from EEG — Simulated EEG is filtered and feature-extracted, then rendered as topographic or ASCII heatmaps of brain regions *[claimed]*
- CNN plus Transformer ensemble — CNN reads spatial patterns, Transformer reads temporal sequences; outputs combined into a risk score *[claimed]*
- Risk score with confidence — Dashboard shows calibrated score, confidence interval, and risk trend over time *[claimed]*
- Explainability and recommendations — Shows which features (e.g. theta band, asymmetry) drove a result and suggests next steps such as seeing a neurologist *[claimed]*
- Community gamification — Challenges with points, leaderboard, session logs and KPI tracking for awareness and engagement *[claimed]*
- Privacy stack — AES-256 encryption, anonymization, federated learning, local training; HIPAA/GDPR compliance asserted *[claimed]*
- Clinical validation roadmap — Phased plan: IRB approval, n=500+ trial, clinic pilots, EHR integration *[planned]*

**Flow:** Feed simulated or headband EEG input → Preprocessing filters noise and extracts features → Ensemble model produces risk score and confidence → Dashboard shows score, trend, heatmap, explanations → Community tracker logs sessions and challenge points

**Prompt:** not public / not found
**Fit (none):** No sponsor challenge is described; Devpost lists a single 'Prizes in Kind' win under an AI Innovation Challenge. The page presents it as an AI health-awareness tool.  *(targeted: Prizes in Kind, AI Innovation Challenge (listed on Devpost page))*
**AI:** CNN and Transformer ensemble on EEG for risk scoring, said to be trained on synthetic plus public data (TUH, CHB-MIT, SEED); no architecture details or real results shown. Tags also list OpenAI, PyTorch, TensorFlow.
**Architecture:** Pipeline of EEG input, preprocessing, CNN/Transformer ensemble, risk scoring, dashboard; README names modules bio_core, neurosync, cloud_map, feedback, gamification; Streamlit/Dash/Plotly listed.
**Novelty:** Pitches a $50-100 headband plus cloud dashboard cost model; scope is broad (clinical, workplace, energy) but evidence is largely descriptive.
**Scope:** small · working: README shows only a short Python snippet; Figma and Netlify prototypes linked; demo uses simulated data; repo could not be cloned. · polish: Rich documentation and badges, but placeholder GIF, inconsistent phase percentages, unexplained metrics.
**Claims:** 91% prediction accuracy, 87% awareness, 76% engagement | 120 ms average response time | First month deployment about $150-200, under $10/month after | 47 awareness sessions, 12 peers educated, 3 risk assessments | HIPAA and GDPR compliance
**Gaps:** Evidence clone failed; README read via raw fetch (summarized); Metrics are unsupported by methods; Project was submitted to 19 hackathons so the DubHacks-specific build is unclear; Prizes in Kind not on DubHacks prize page
Sources: https://devpost.com/software/neuromapping-low-cost-cognitive-safety-system, https://raw.githubusercontent.com/senushidinara/NeuroMapping/HEAD/README.md, https://dubhacks25.devpost.com/

---

### Optivise
*DubHacks DubHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** DubHacks NEXT

**What it is:** A Next.js platform where a user describes a website change in plain language, Gemini writes real HTML/CSS variants, and Statsig tracks impressions and clicks across randomly served variants, followed by AI analysis of the winner.
**Problem / user:** Most companies rarely run A/B experiments; aimed at small teams who want experimentation to be accessible and scalable without specialist tooling.

**Features**
- Natural-language variant generation — Gemini turns a prompt such as 'make the signup button more prominent' into actual HTML/CSS changes, 1 to 3 variants *[claimed]*
- AI-suggested prompts — Gemini inspects current variant and proposes UX-best-practice optimization prompts *[claimed]*
- Live preview — Variants render in a Shadow DOM for isolated styling with instant switching *[claimed]*
- Event tracking — Automatic impressions and click capture; metrics: impressions, clicks, CTR, conversions, conversion rate, logged via Statsig *[claimed]*
- Standalone test site — A /site URL serves each visitor a random active variant to simulate real traffic *[claimed]*
- AI result analysis — Identifies winner with statistics, plain-language recommendations and next steps *[claimed]*
- Upload your own site — Let users bring their own website instead of editing code *[planned]*

**Flow:** Enter a change request or accept AI suggestion → Gemini generates variants → Preview variants live → Share /site link so visitors see random variants → Events logged to Statsig → View analytics and AI recommendation

**Prompt:** DubHacks NEXT rewards the project with highest potential to become a successful startup product, showing market-disrupting innovation and a clear path to commercial viability.
**Fit (implied):** Frames experimentation as a product for teams of any size ('autopilot for growth optimization'); a startup-style SaaS idea. Also built on Statsig, which had its own challenge, but page names only DubHacks NEXT.  *(targeted: DubHacks NEXT)*
**Sponsor tools:** Statsig (Client SDK, event logging and experiment tracking for variants, core); Gemini API (Variant code generation, prompt suggestions, result insights, core)
**AI:** Gemini generates HTML/CSS variants from natural language, suggests prompts, and writes analysis of results; no fine-tuning or agents described.
**Architecture:** Next.js app with API routes calling Gemini; variants applied in Shadow DOM preview; Statsig client/node SDKs record events; /site page serves random variants; in-memory event storage.
**Novelty:** Generates real code diffs rather than mockups and closes the loop from generation to traffic split to AI-read results in one tool.
**Scope:** small · working: README describes features and deployment; around 5.5k LOC, 32 code files; no demo link or video on Devpost. · polish: Detailed README with Vercel deploy guide; no tests, CI, or screenshots listed.
**Claims:** Described as autopilot for growth optimization
**Gaps:** Devpost page is very thin; feature list follows README; No demo or video; Whether features work not verified
Sources: https://devpost.com/software/optivise-6ag1nm, evidence/dubhacks-dubhacks-2025-optivise.json (README), https://dubhacks25.devpost.com/

---

### Spendify
*DubHacks DubHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Atlassian: Best Use of Forge Agents

**What it is:** A Forge app that adds three Jira issue panels (Dashboard, Add Expense, Reports) for tracking college spending by category, with Chart.js charts and a Rovo agent called 'College Money Coach' for budgeting advice.
**Problem / user:** College students, especially freshmen, who start managing money independently and do not track where it goes.

**Features**
- Categorized expense entry — Add Expense panel records spending under customizable categories like food, transport, entertainment *[shown_working]*
- Spending dashboard — Dashboard panel with monthly spending shown in pie and bar charts built with Chart.js *[shown_working]*
- Reports panel — Third Jira panel for reports sharing the same in-memory store *[shown_working]*
- Rovo agent money coach — Finance-prompted Rovo agent analyzes spending and suggests saving strategies and answers budgeting questions *[claimed]*
- Forge storage and resolver backend — Resolvers handle data logic; README notes panels share an in-memory per-runtime store that resets *[shown_working]*
- Gamification and prediction — Shared saving goals, friend challenges, spending prediction models *[planned]*

**Flow:** Install Forge app on a Jira site → Open an issue and use Apps sidebar to pick a Spendify panel → Add expenses by category → View charts on the dashboard → Ask the Rovo coach for advice

**Prompt:** Build apps or automations on Atlassian's Forge platform that extend Jira, Confluence, Bitbucket or Trello for collaboration, productivity or DevOps, and show how Forge Agents make work smarter, faster and more fun.
**Fit (explicit):** Whole product is a Forge app inside Jira, with panels, resolvers and a Rovo agent as the AI helper; repurposes Jira as a personal finance surface.  *(targeted: Atlassian: Best Use of Forge Agents)*
**Sponsor tools:** Atlassian Forge (Hosts three Jira issue panels, resolvers, storage, core); Rovo Agents (College Money Coach chatbot with finance prompt, core); Jira (Host surface for the panels, core)
**AI:** Rovo agent configured with a finance-focused prompt to analyze spending and give budgeting tips; underlying model not named.
**Architecture:** Forge manifest with three Custom UI Jira issue panels (React), resolver backend using @forge/api and resolver, Chart.js charts, Forge storage per Devpost versus in-memory store per README.
**Novelty:** Uses Jira, a work tracker, as a student budgeting tool; team states first hackathon and first Forge/Rovo use.
**Scope:** small · working: README with deploy steps, Loom and YouTube demos; about 2.3k LOC, two Forge package setups. · polish: Charts and custom dashboard; data resets on restart; no tests; two Forge versions caused issues.
**Claims:** First working Jira dashboard and app built from scratch by team
**Gaps:** Devpost says Forge storage API is used; README says in-memory store with no persistence; feature list notes both; Rovo agent config not in repo; Videos not watched
Sources: https://devpost.com/software/spendify, evidence/dubhacks-dubhacks-2025-codegraph-spendify-taskflow-spendify.json (README), https://dubhacks25.devpost.com/

---

### TaskFlow
*DubHacks DubHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Atlassian: Best Use of Forge Agents

**What it is:** A Chrome extension plus Forge backend that screenshots a Canvas assignment page, has Rovo agents read the assignment details, and creates labeled Jira tasks with due dates automatically.
**Problem / user:** Students who use Canvas and find it tedious to copy each assignment into a task manager by hand.

**Features**
- Screenshot capture of Canvas — Chrome extension captures the assignment page image *[claimed]*
- Assignment parsing — Rovo agents extract title, description and due date from the screenshot *[claimed]*
- Jira task creation — Forge backend calls Jira REST API to create a Task with summary, description, labels, due date *[shown_working]*
- Automatic labeling — Labels by class, assignment type and due date; backend can also index existing issues by 'category:value' labels *[claimed]*
- Auto scheduling — Tasks scheduled from extracted due dates *[claimed]*
- Notion and Google Tasks support — Expand beyond Jira; improve extraction, adaptive prioritization *[planned]*

**Flow:** Student opens a Canvas assignment page → Clicks extension to capture screenshot → Request reaches Forge backend → Rovo agents parse assignment info → Labeled, scheduled Jira task appears

**Prompt:** Build apps or automations on Atlassian's Forge platform that extend Jira, Confluence, Bitbucket or Trello for collaboration, productivity or DevOps, and show how Forge Agents make work smarter, faster and more fun.
**Fit (explicit):** Rovo agents plus a Forge backend automate the Canvas-to-Jira task entry workflow, a productivity automation on Jira.  *(targeted: Atlassian: Best Use of Forge Agents)*
**Sponsor tools:** Rovo Agents (Parse screenshots and create tasks, core); Atlassian Forge (Backend handling API requests, Jira REST calls, core); Jira (Task destination, core)
**AI:** Rovo agents parse assignment information from screenshots and create tasks; underlying model not named. A separate image-processing server repo is linked.
**Architecture:** Chrome extension sends screenshot to image-processing server and Forge backend; Forge module (@forge/api) exposes addIssues and fetchLabels over Jira REST; Rovo agents orchestrate parsing.
**Novelty:** Uses screenshots as the integration path since Canvas offers no direct link; pivoted from Trello to Jira midway.
**Scope:** tiny · working: Linked main repo has one ~100 LOC source file with no README; four repos total; no demo or video. · polish: No video, README or screenshots; Devpost is brief.
**Claims:** Automated task creation drastically reduced manual work
**Gaps:** Main repo has no README; other three repos (extension, image server, jira-task-adder) not readable; Extension and screenshot parsing not seen working
Sources: https://devpost.com/software/taskflow-qv6z7m, evidence/dubhacks-dubhacks-2025-codegraph-spendify-taskflow-taskflow.json, https://raw.githubusercontent.com/Achintya72/task-flow-agent/HEAD/src/index.js, https://dubhacks25.devpost.com/

---

