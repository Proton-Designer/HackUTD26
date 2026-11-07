# Cal Hacks — Cal Hacks 12.0 (2025) (11 projects)

### ADLOVIN
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner AppLovin: Ad Intelligence Challenge

**What it is:** A pipeline that turns ad images and videos into structured marketing signals and embeddings: keyframes, OCR text, face presence, audio mood and Claude vision analysis, stored in ChromaDB for ad-performance analysis.
**Problem / user:** Ad-tech and recommendation-model teams who need rich features describing what ad creatives show, say and sound like.

**Features**
- Video keyframe extraction with dedup — Samples frames at an interval and drops near-duplicates by embedding similarity, reportedly cutting frames 60-80%. *[claimed]*
- Claude vision signal extraction — Frames go to Claude Vision for brand, product, promo codes, call-to-action, colors and style; results are voted into a video summary. *[shown_working]*
- Image pipeline — Face detection plus EasyOCR text, then Claude parses text into structured marketing JSON. *[shown_working]*
- Audio features — FFmpeg and Librosa give duration, pitch, rough gender estimate, spectral bandwidth and HuBERT-based emotion. *[shown_working]*
- Embedding storage and context — Frame embeddings live in ChromaDB and give frame type, similar frames and scene change context. *[claimed]*
- Test frontend and API — React page uploads an image for human detection or a video for audio analysis against a Flask API. *[shown_working]*

**Flow:** Put ad videos or images in a data folder → Run the video or image orchestrator script → Visual and audio tracks process in parallel → Receive JSON with brands, promos, CTAs, audio features → Optionally test via the React/Flask demo page

**Prompt:** AppLovin Ad Intelligence Challenge ($3,000): the page gives no description and refers to criteria in an external document.
**Fit (explicit):** Extracts visual, text and audio features from ad creatives into embeddings and signals, which the README itself labels as an Ad Intelligence Challenge submission.  *(targeted: AppLovin: Ad Intelligence Challenge)*
**Sponsor tools:** Claude API (Anthropic) (Vision analysis of frames and parsing OCR text into marketing signals, core)
**AI:** Claude Vision and text analysis for signals; embedding-based frame dedup and context in ChromaDB; HuBERT audio emotion; OpenCV face detection; EasyOCR.
**Architecture:** Python orchestrators split video into visual and audio tracks (dedup agent, human detection, audio processor, embedding context, Claude vision, consolidation); ChromaDB stores embeddings; small Flask API plus React frontend.
**Novelty:** Multimodal agent pipeline combining dedup, audio emotion and an LLM consolidation step for ad creatives; the Devpost and README differ on the model stack.
**Scope:** medium · working: Detailed README with CLI usage and output formats; evidence repo is only the test frontend (~0.8k LOC), the main pipeline lives in a second repo. · polish: Thorough README but inconsistent numbers; no demo or video.
**Claims:** 30-second ad processed in roughly 45-70 seconds | Promo detection 85-90% on clear text (no method given) | Frame dedup removes an estimated 60-80% of frames
**Gaps:** Devpost lists a vision transformer and CLIP; the README describes Claude Vision, so the feature list follows the README for the visual stage; README is a second repo, not the linked SisuKah repo; Challenge criteria not public
Sources: https://devpost.com/software/adlovin-media-intelligence, evidence/cal-hacks-cal-hacks-12-0-2025-adlovin.json (frontend repo), https://raw.githubusercontent.com/abtonmoy/calhacks12/HEAD/README.md, https://cal-hacks-12-0.devpost.com/

---

### Bob
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Winner Cal Hacks: Most Creative Hack

**What it is:** An agent for Snap Spectacles AR glasses that watches what the wearer is doing, answers spoken questions through Gemini Live, highlights objects with boxes in the display and can message teammates, to guide hands-on tasks like circuits or repairs.
**Problem / user:** Homeowners, vocational learners and tradespeople doing physical tasks, framed against a shortage of electricians and mechanics.

**Features**
- Live multimodal assistant — Spectacles stream video and audio over WebSocket to a Python server that holds a Gemini Live session. *[claimed]*
- Spoken step-by-step guidance and warnings — Gemini Live replies after voice-activity detection with next steps, object details and safety warnings. *[claimed]*
- Text-prompted object highlighting — YOLOE-11 finds named objects and the Lens draws bounding boxes on the display. *[claimed]*
- Tools — Search and Maps via Google, and email (SMTP) or Slack messages to teammates. *[claimed]*
- Task memory — Keeps coherence across a multi-step physical task. *[claimed]*

**Flow:** Wear Spectacles running the Lens → Server opens a Gemini Live session on connect → Wearer speaks a question while working → Agent calls tools such as detection, search or email → Overlay and box highlights appear on the glasses

**Prompt:** Cal Hacks Most Creative Hack: a prize (iPad and Apple Pencil) with no description on the prize page.
**Fit (implied):** An AR agent that converses and instructs through physical tasks; the page calls it a first of its kind but names no explicit target.  *(targeted: Cal Hacks: Most Creative Hack)*
**Sponsor tools:** Snap Spectacles / Lens Studio (AR hardware, camera capture and overlay UI, core); Gemini Live (Core multimodal agent, core)
**AI:** Gemini Live as the conversational vision agent with tool calls; YOLOE-11 text-prompted detection; local Ollama and OpenRouter paths also exist in the repo.
**Architecture:** Lens Studio TypeScript on Spectacles sends camera frames to a Python WebSocket server (serve.py) that runs Gemini Live, YOLO grounding and tools, then returns text and box coordinates.
**Novelty:** Live (non-turn-based) agent on AR glasses with coordinate projection from camera to display; the team notes no member had used AR glasses before.
**Scope:** medium · working: Repo has Lens project, server, grounding and clients (~5.8k LOC); no demo video linked. · polish: Architecture-oriented README; no video or screenshots described.
**Claims:** Described as the first AR glasses with a conversational multimodal agent that instructs through physical tasks
**Gaps:** No demo video; Repo README is titled Tethyr Labs, the Devpost calls the project Bob
Sources: https://devpost.com/software/bob-vj43mq, evidence/cal-hacks-cal-hacks-12-0-2025-bob.json, https://cal-hacks-12-0.devpost.com/

---

### Duck Duck Goose
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner AppLovin: Query Planner Challenge

**What it is:** A query engine layered on DuckDB for AppLovin's query-planner challenge. It converts data to parquet shards, precomputes aggregate tables, rewrites incoming queries to hit the cheapest feasible table, and warms caches.
**Problem / user:** Challenge participants optimizing analytical queries over a 245M-row ad-events table; baseline ~45 s.

**Features**
- Parquet on-disk layout — Per-thread parquet shards with large row groups instead of rereading CSV; ~22x gain alone per README. *[shown_working]*
- Materialized-view tables — Pre-aggregated tables by day, country and id types, large and small variants, defined in a registry. *[shown_working]*
- Query planner and rewriter — Checks which pre-aggregates cover a query's group-by and aggregates (AVG from SUM and COUNT), then scores by estimated rows. *[shown_working]*
- Caching and warmup — Preload computes row counts, distinct counts and top-k stats and warms caches. *[shown_working]*
- Benchmark harness — Scripts run query sets, compare to expected results and plot speedups. *[shown_working]*

**Flow:** Run preprocessing (~5 minutes) → Run the benchmark script on a JSON query set → Planner rewrites each query to a view → Results are checked against expected output → Compare timing figures

**Prompt:** AppLovin Query Planner Challenge ($10,000): no description on the page; criteria in an external document.
**Fit (explicit):** README states it is a submission to the query planner challenge and reports speedup over the supplied baseline.  *(targeted: AppLovin: Query Planner Challenge)*
**AI:** none
**Architecture:** Python over DuckDB: preprocess CSV to parquet shards, build materialized tables, planner (src/planner.py) picks and rewrites to a table, benchmark scripts compare against baseline.
**Novelty:** Classic database tuning rather than ML; README quantifies each technique's contribution and gives an asciinema demo.
**Scope:** small · working: README reports benchmark numbers and links an example run; ~1.1k LOC with benchmark and queries folders. · polish: Clear design write-up with figures; no tests or CI.
**Claims:** About 1300x speedup, ~45 s to ~30 ms on an M3 Pro | ~120x speedup on 25 additional validation queries | Preprocessing takes about 5 minutes
**Gaps:** Challenge criteria not public; Only first ~5000 chars of README read
Sources: https://devpost.com/software/duck-duck-goose-jelxr9, evidence/cal-hacks-cal-hacks-12-0-2025-duck-duck-goose.json, https://cal-hacks-12-0.devpost.com/

---

### Elda AI
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner Claude: Best Use of Claude

**What it is:** A voice-first eldercare system: an elderly person talks to a mobile app, Claude reads intent and mood, Letta and Chroma track behavior patterns over time, and doctors or caregivers get daily and monthly summaries on a web dashboard.
**Problem / user:** Older adults with declining memory (inspired by a grandmother with dementia), their caregivers and doctors, who need medication and wellbeing monitoring.

**Features**
- Voice-first mobile app — React Native/Expo app lets seniors talk instead of tapping. *[claimed]*
- Intent, sentiment and emotion analysis — Claude interprets speech for health intent and mood. *[claimed]*
- Behavior memory and pattern detection — Letta learns daily patterns; Chroma finds semantic patterns and changes over time. *[claimed]*
- Caregiver dashboard — Next.js dashboard charts daily mood and medication adherence with alerts. *[claimed]*
- Automatic doctor summaries — Daily and monthly summaries on compliance, mood shifts and possible cognitive decline. *[claimed]*
- Reminders, calls and push — APScheduler reminders, Twilio voice calls and Firebase push. *[claimed]*

**Flow:** Senior talks to the app by voice → Claude extracts intent and emotion → Letta and Chroma update behavior history → Reminders and calls go out → Caregiver reviews the dashboard and summaries

**Prompt:** Anthropic Best Use of Claude: judged on technical complexity of Claude Code use, creative use case, and impact/practicality for real-world problems.
**Fit (implied):** Claude handles speech, intent and emotion understanding in an eldercare product aimed at a real-world need; the page does not discuss Claude Code specifically.  *(targeted: Claude: Best Use of Claude)*
**Sponsor tools:** Claude (Anthropic) (Intent, sentiment and emotion analysis of conversations; summaries, core); Letta (Behavioral memory, supporting); Chroma (Semantic pattern detection, supporting)
**AI:** Claude for intent, sentiment and emotion; Letta memory agent for routines; Chroma vector search to compare patterns over time and generate summaries.
**Architecture:** FastAPI/PostgreSQL backend (JWT, APScheduler) on Railway; Expo mobile app; Next.js dashboard on Vercel; Twilio and Firebase for calls and push; Claude, Letta and Chroma as AI layer.
**Novelty:** Combines persistent behavioral memory with longitudinal summaries for doctors, with three client surfaces built in two days.
**Scope:** medium · working: Devpost describes a functional prototype of the mobile and web apps with nine screenshots; repo could not be read. · polish: Multiple deployments named and many integrations; no demo video.
**Claims:** Functional prototype of mobile app and caregiver app in two days | Real-time AI health summaries from daily conversations
**Gaps:** Repo clone failed and README fetch returned an error; No walkthrough, so flow is inferred; Medication-error prevention mechanism not described
Sources: https://devpost.com/software/elda-ai, https://cal-hacks-12-0.devpost.com/

---

### Expungo
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner Promise: Public Impact Prize (sponsored by Promise); Winner Cal Hacks: Greatest Social Impact

**What it is:** A web app that reads an uploaded court or RAP sheet, checks the person's expungement eligibility against state law, suggests next steps if not eligible, auto-fills forms if eligible, and offers a live voice agent for guidance.
**Problem / user:** People with past convictions who find the expungement process hard to navigate; legal aid groups named as future partners.

**Features**
- Eligibility questionnaire — Asks a few simple questions before reviewing documents. *[claimed]*
- RAP sheet parsing — Gemini parses uploaded PDFs into case numbers, conviction codes and court details. *[claimed]*
- State statute RAG — LangChain and ChromaDB hold statutes for all 50 states; GPT-4 reasons over retrieved text to judge eligibility. *[claimed]*
- Next steps or form filling — Ineligible users get a path to eligibility; eligible users get forms filled automatically. *[claimed]*
- Live voice agent — LiveKit Agents with WebRTC and Silero VAD, JWT-protected sessions, for hands-free guidance. *[claimed]*
- In-memory data handling — User documents are processed in memory with no external database, per the page. *[claimed]*

**Flow:** Answer a few intake questions → Upload a court record or RAP sheet → System extracts case data and checks state law → Receive eligibility result and next steps or filled forms → Talk to the voice agent about the case

**Prompt:** Promise Public Impact: impact on underserved communities, AI (voice/chat) for accessibility, innovation, usefulness and pragmatism. Greatest Social Impact: prize only, no description.
**Fit (implied):** A voice and document assistant that lowers barriers to a legal process for people with records, matching the underserved-community and AI-accessibility criteria; the page does not name the prize.  *(targeted: Promise: Public Impact Prize, Cal Hacks: Greatest Social Impact)*
**Sponsor tools:** LiveKit Agents (Real-time voice agent, core); Google Gemini (PDF parsing, supporting)
**AI:** Gemini extracts structured data from PDFs; RAG over state statutes in ChromaDB with GPT-4 for reasoning; LiveKit voice agent with VAD.
**Architecture:** Next.js 15 frontend; FastAPI async backend for uploads, RAG queries and voice tokens; Gemini parsing, LangChain+Chroma statutes, GPT-4; LiveKit voice service.
**Novelty:** Combines document extraction, 50-state legal retrieval, form filling and voice in one flow for a legal-access use case.
**Scope:** medium · working: Devpost describes components in detail but links no repo, demo or video. · polish: Responsive multi-step form claimed; no visual evidence read.
**Claims:** Covers expungement statutes from all 50 states | User data stays in memory, not stored externally
**Gaps:** No repo linked; No demo; flow from description only; Accuracy of eligibility logic not shown
Sources: https://devpost.com/software/clearpathai, https://cal-hacks-12-0.devpost.com/

---

### FaceTimeOS: AI Mac Agent
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Cal Hacks: 1st Overall [1st]

**What it is:** Lets a user remotely control their Mac by FaceTiming or iMessaging it. An AI agent answers, talks through the task by voice, drives the mouse and keyboard with a computer-use framework, and texts back a screenshot when done.
**Problem / user:** Remote-first workers and developers who want to run local scripts or fetch files from their Mac without clunky remote-desktop apps.

**Features**
- Answers FaceTime calls to the Mac — Audio is routed through virtual devices; speech is transcribed, answered by the model and spoken back into the call *[shown_working]*
- iMessage command channel — Text a task to the Mac; agent performs it and replies in the thread *[shown_working]*
- Computer-use task execution — Forked Agent-S framework clicks and types on the Mac for multi-step jobs like finding a file and uploading it *[shown_working]*
- Progress narration — A summarizer watches the agent trajectory and reports status by voice or text *[claimed]*
- Screenshot confirmation — Sends a screenshot to the phone via iMessage when the task finishes *[shown_working]*
- Electron UI to view agent actions — Frontend shows what the agent is doing and accepts prompts *[shown_working]*
- Proactive monitoring (e.g. failed training script) — Agent would watch the computer and alert about errors *[planned]*

**Flow:** Call or iMessage your Mac → Agent answers and takes a spoken or typed command → Claude decides whether to answer, delegate summary, or call the backend for a system action → Computer-use agent executes the task on the Mac → Status summaries are spoken or texted → Screenshot of the result arrives on the phone

**Prompt:** Overall prize: 1st Overall at Cal Hacks 12.0 (laptop prize); no track-specific text. General judging: real-life application, functionality/quality, creativity, technical complexity.
**Fit (none):** Not tied to a track; a working end-to-end voice-and-text agent that operates a real computer, matching the application and technical-complexity criteria.  *(targeted: Cal Hacks: 1st Overall)*
**Sponsor tools:** Claude (orchestrator deciding between answering, delegating, or calling backend (per Devpost), core); Fish Audio (speech-to-text/text-to-speech bridge for FaceTime audio, core); Fetch.ai (agent watching the computer-use trajectory to summarize, supporting); Groq (fast summary generation, supporting)
**AI:** Claude routes intent; Agent-S3 fork (Grok/OpenAI configurable) does screenshot-based computer use with optional UI-TARS grounding; Fish Audio does STT/TTS; Groq/Fetch.ai agent summarize progress.
**Architecture:** Flask backend bridges iMessage/FaceTime and audio (BlackHole virtual devices) to the LLM; Agent-S fork executes GUI actions; Electron/React frontend shows live actions.
**Novelty:** Uses native Apple FaceTime/iMessage as the remote-control interface instead of a remote-desktop client; bridges call audio through virtual audio devices without an official API.
**Scope:** medium · working: README has YouTube FaceTime demo and iMessage clip; setup scripts and run.sh. · polish: Electron UI, setup docs with permission screenshots; grounding endpoint no longer live.
**Claims:** README claims state-of-the-art OSWorld-verified performance via extended Agent S3 | Won 1st place at Cal Hacks 12.0
**Gaps:** Devpost lists no video; README links YouTube demo not watched; Devpost says Claude orchestrates while README configures Grok/OpenAI
Sources: https://devpost.com/software/facetime-macos-ai-agent, https://github.com/ThePickleGawd/calhacks-25 (evidence file), https://cal-hacks-12-0.devpost.com/

---

### Hardware Context Protocol (MCP for Hardware)
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Crater: Play-Do Prize; Winner Cal Hacks: Best Hardware Hack

**What it is:** An SDK and protocol, like MCP but for physical devices, where a JSON description of a hardware node is turned into a TCP pub/sub layer so an LLM can discover and control it. Demoed as a voice-driven chef robot using an SO-ARM101 arm and a camera.
**Problem / user:** Builders wanting LLMs to act in the physical world; the motivating example is a household assistant that prepares food.

**Features**
- Node definition and generated networking — A minimal JSON spec of a node and its actions yields a custom TCP client for the microcontroller. *[claimed]*
- Discovery and pub/sub orchestration — Nodes subscribe to the LLM side and exchange context in an HCP schema. *[claimed]*
- Arm control via inverse kinematics — Custom single-chain IK solver commands the SO-ARM101 in world coordinates, supports elbow up/down. *[shown_working]*
- Simulator — Custom simulator checks forward/inverse kinematics and rejects null-space solutions. *[claimed]*
- AprilTag object sensing — OpenCV detects tags and publishes object type and position into the protocol. *[shown_working]*
- Voice chef-robot demo — User speaks a food request; LLM reads ingredient locations and drives the arm. *[shown_working]*

**Flow:** Speak what you want to eat → LLM interprets the request → Camera reports ingredient positions via AprilTags → LLM issues arm actions over HCP → Arm picks and assembles the dish

**Prompt:** Crater Play-Do Prize: the hack with the most composable, iterative and playful design across software, hardware or deep tech. Best Hardware Hack: prize only.
**Fit (implied):** A composable protocol where any hardware node can be plugged into an LLM, demonstrated on real robot hardware; the page does not name the prizes.  *(targeted: Crater: Play-Do Prize, Cal Hacks: Best Hardware Hack)*
**AI:** An LLM interprets prompts and orchestrates hardware actions through the HCP schema; the page lists ASI:One without explaining its role.
**Architecture:** Python SDK generates TCP nodes; hcp_client on the LLM side; actuator module with kinematics for the arm; vision module with OpenCV/AprilTags; Flask GUI.
**Novelty:** Frames a general protocol layer for LLM-to-hardware rather than a single robot; includes a hand-written IK solver and simulator.
**Scope:** medium · working: Devpost describes a deployed chef-robot demo with screenshots; repo ~3.2k LOC with actuator, SDK, client and vision folders. · polish: Repo README is only setup steps; kinematics docs exist; no video.
**Claims:** Bootstraps hardware nodes at near-zero integration cost
**Gaps:** No demo video; Role of ASI:One unstated; Arm named SO-ARM101 and SOARM-100 on page
Sources: https://devpost.com/software/hardware-context-protocol, evidence/cal-hacks-cal-hacks-12-0-2025-hardware-context-protocol-mcp-for-hardware.json, https://cal-hacks-12-0.devpost.com/

---

### Haven
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Fetch AI: Best Use of Fetch AI; Winner Y Combinator: Build an Iconic YC Company - 1st Place [1st]; Winner LiveKit: Best Start-up Idea

**What it is:** Multi-agent hospital assistant: a LiveKit voice agent talks with patients or families and logs structured needs, monitoring agents watch vitals, and nurses get a live 3D hospital map and natural-language queries with summary reports.
**Problem / user:** Understaffed hospitals where patients wait long for nurses and nurses lose time to documentation and checking multiple systems.

**Features**
- HavenAI voice assistant — LiveKit plus Whisper and OpenAI Realtime hold a conversation, ask follow-ups, pull EHR data, and push validated structured data *[shown_working]*
- Vitals monitoring and alerting — Fetch.ai agents track vitals and a vitals agent hands off to an alert-response agent *[claimed]*
- Facial photoplethysmography — OpenCV pipeline estimates heart rate and stress from video and feeds the monitor *[claimed]*
- Live 3D hospital map — Rooms colored by alerts; Claude tool-calling agent updates overlays from agent events *[shown_working]*
- Natural-language patient queries — Nurse asks e.g. about one patient last 6 hours; chained tool calls return consolidated answer *[shown_working]*
- Patient summary reports — Summaries generated from patient-assistant conversations *[claimed]*
- Transcript compression — Pipeline shortens long conversations while keeping key clinical details *[claimed]*

**Flow:** Patient or family speaks with HavenAI → Assistant asks follow-ups and logs structured record → Monitoring agents raise or dismiss alerts → Nurse opens 3D map with color-coded rooms → Nurse asks natural-language question about a patient → Nurse generates a summary report

**Prompt:** Fetch.ai: agents registered on Agentverse with Chat Protocol, judged on function, Fetch tech use, innovation, impact, UX. YC: build an iconic YC company (no criteria). LiveKit Start-up Idea: market potential, value, monetization.
**Fit (implied):** Fetch.ai agents handle vitals and alerts; LiveKit powers the voice front end; framed as a startup addressing nurse workload.  *(targeted: Fetch.ai: Best Use of Fetch AI, Y Combinator: Build an Iconic YC Company, LiveKit: Best Start-up Idea)*
**Sponsor tools:** LiveKit (WebRTC voice assistant with OpenAI realtime, core); Fetch.ai (vitals and alert-response agents, core); Claude (tool-calling agent for 3D map and nurse queries, core)
**AI:** OpenAI Realtime/Whisper for voice; Claude chain-of-tools agent for spatial map and queries; Fetch.ai agents for monitoring; OpenCV rPPG vitals; summarization to fit context.
**Architecture:** LiveKit voice agent, Fetch.ai agent network and Claude agent communicate over WebSockets to a web dashboard with 3D map; EHR data feeds the agents.
**Novelty:** Combines voice intake, remote heart-rate estimation from video, agent-based alerting and a spatial 3D hospital view in one nurse workflow.
**Scope:** large · working: GIF demos of voice, dashboard and 3D map on the Devpost page; sizeable repo. · polish: Tech stack diagram, multiple GIFs; no video or live link.
**Claims:** Aims to turn a 20-minute nurse wait into an instant documented interaction | Nurses spend up to 50% of shift on documentation (context claim)
**Gaps:** No video; GIFs only; Grok in tags unexplained
Sources: https://devpost.com/software/haven-536r1q, https://github.com/scrappydevs/haven (evidence file), https://cal-hacks-12-0.devpost.com/

---

### Orbit
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Fetch AI: Best Use of Fetch AI

**What it is:** A voice and meeting automation assistant: an Omi wearable mic and meeting transcripts are turned into structured actions by an LLM, and a middleware agent (Nexus) routes them through MCP servers to Jira, calendar, email and an Uber booking automation.
**Problem / user:** Professionals and teams whose meeting action items go unexecuted; the page pitches a freemium and a team subscription tier.

**Features**
- Voice command capture — Omi device webhooks batch speech with a 5-second silence window. *[shown_working]*
- LLM command extraction — Extracts intent such as ride booking, Jira update or scheduling and corrects spelling. *[shown_working]*
- Uber ride booking automation — Playwright browser automation books rides after account authentication. *[claimed]*
- Nexus middleware over MCP — Routes parsed commands to Jira, calendar and other MCP servers; hosted on Fetch.ai Agentverse. *[claimed]*
- Meeting-to-action pipeline — Transcript intent is validated as JSON and executed through Composio MCP (Jira tickets, emails, events). *[claimed]*

**Flow:** Speak a command or hold a meeting → Omi sends transcript segments to the webhook → LLM extracts a structured action → Nexus routes it to the right MCP server → User receives confirmation or reviews actions

**Prompt:** Fetch.ai Best Use: agents registered on Agentverse with Chat Protocol; weighted for functionality, Fetch tech use, innovation, impact and UX.
**Fit (explicit):** The Nexus agent is hosted on Agentverse and collaborates with other agents; the page says the agent runs there.  *(targeted: Fetch AI: Best Use of Fetch AI)*
**Sponsor tools:** Fetch.ai Agentverse (Hosting the Nexus agent, core); Composio MCP (Jira, Gmail, calendar integrations, supporting); Sim.ai (Intent extraction from transcripts, supporting); Omi (Wearable voice input, core)
**AI:** LLM (OpenAI) extracts commands from voice segments; Sim.ai described for transcript reasoning; agent routes via MCP.
**Architecture:** Omi webhook into FastAPI (main.py), LLM command extraction, Nexus agent with MCP client to services, Playwright Uber automation, Docker/Railway deploy.
**Novelty:** Combines wearable voice capture, MCP routing and Agentverse hosting; Devpost (meetings, Composio) and README (voice, Uber, OpenAI) emphasize different parts.
**Scope:** medium · working: README gives endpoints, commands and deployment; repo ~2.7k LOC with Dockerfile; no video. · polish: Documentation folder, env example, Railway config; business tiers described.
**Claims:** Meetings average 11.3 hours per week (market stat, not a result)
**Gaps:** Devpost features follow Sim.ai/Composio meeting flow; README follows Omi voice, OpenAI and Uber; both recorded; No demo video
Sources: https://devpost.com/software/orbit-n97hqz, evidence/cal-hacks-cal-hacks-12-0-2025-orbit.json, https://cal-hacks-12-0.devpost.com/

---

### Physical Digital Darts (Wii Darts)
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Cal Hacks: Best Beginner Hack

**What it is:** A 3D-printed dart containing an Arduino Nano and MPU6050 motion sensor. A throwing motion is read, filtered and sent over serial to a Python dartboard simulator that launches a virtual dart when the button is released.
**Problem / user:** Casual gamers wanting an affordable, open-source physical alternative to keyboard-and-mouse play.

**Features**
- Orientation capture — MPU6050 roll, pitch and yaw filtered on the Arduino Nano. *[shown_working]*
- Button-gated throw — Hold marks throw start and release launches the dart in the sensed direction. *[shown_working]*
- Double-tap recalibration — Two quick taps reset the dart orientation to counter drift. *[shown_working]*
- Python dartboard simulator — pygame/pyserial reads serial data and animates the dart on a 2D board. *[shown_working]*
- Printed casing — CAD-designed dart-shaped case with compact wiring. *[shown_working]*

**Flow:** Double-tap to calibrate → Press and hold the button → Make a throwing motion → Release the button → Virtual dart flies to the board position

**Prompt:** Best Beginner Hack: a prize (Polaroid camera) with no description on the prize page.
**Fit (none):** A first-time-friendly hardware plus software build; the page does not mention the prize.  *(targeted: Cal Hacks: Best Beginner Hack)*
**AI:** none
**Architecture:** MPU6050 to Arduino Nano (Rust firmware, filtering) over serial to a Python pygame simulator; 3D-printed casing from CAD.
**Novelty:** Wii-style physical input built from scratch with a custom drift filter; position tracking was dropped due to sensor drift.
**Scope:** small · working: Devpost photos of testing and circuit; repo has firmware, simulator and CAD (~0.8k LOC); no video. · polish: Clear README; simulator is 2D only.
**Gaps:** No demo video; Accuracy of throws not measured
Sources: https://devpost.com/software/digital-physical-darts-wii-darts, evidence/cal-hacks-cal-hacks-12-0-2025-physical-digital-darts-wii-darts.json, https://cal-hacks-12-0.devpost.com/

---

### Ted.AI
*Cal Hacks Cal Hacks 12.0 (2025) · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Winner Cal Hacks: 2nd Overall [2nd]; Winner LiveKit: Most Creative Project

**What it is:** Sensor-equipped teddy bear that senses hugs, motion and heart rate, converses with a child via an LLM, guides calming exercises, and streams emotional data to a caregiver dashboard.
**Problem / user:** Children with anxiety, ADHD or loneliness; dashboard serves parents, teachers and clinicians.

**Features**
- Biosensing in the bear — ESP32 reads pulse sensor, capacitive touch and MPU6050 accelerometer *[claimed]*
- Empathetic conversation — Whisper transcribes speech, RoBERTa detects emotion, GPT dialogue via LangChain replies *[claimed]*
- Guided calming routines — Breathing exercises and focus routines triggered by emotional state *[claimed]*
- On-device emotion inference — TensorFlow Lite Micro on the microcontroller *[claimed]*
- Caregiver dashboard — React/D3 shows emotion timelines, sentiment trends and simulated brain-region activations *[claimed]*
- Sensor fusion pipeline — MQTT feeds Flask backend with MongoDB and InfluxDB storage *[claimed]*

**Flow:** Child hugs and talks to the bear → Sensors and speech go to the AI → Bear responds and guides calming → Data appears on caregiver dashboard

**Prompt:** Cal Hacks 2nd Overall (no criteria beyond general judging) and LiveKit Most Creative: unique or unexpected application of LiveKit voice or video agents.
**Fit (implied):** A hugging, talking therapeutic toy is an unusual voice-agent application; the page does not describe how LiveKit is used.  *(targeted: Cal Hacks: 2nd Overall, LiveKit: Most Creative Project)*
**Sponsor tools:** LiveKit (not described in writeup, unclear); Fetch.ai (listed in built-with only, unclear)
**AI:** Whisper STT, RoBERTa emotion classifier, GPT dialogue orchestrated with LangChain, TFLite Micro edge inference.
**Architecture:** ESP32 sensors to MQTT to Flask backend (MongoDB/InfluxDB), AI services for speech/emotion/dialogue, React+D3 dashboard.
**Novelty:** Merges physical affective sensing (hugs, pulse, motion) with an LLM companion and a neuro-style visualization dashboard.
**Scope:** medium · working: Claims fully functional prototype; no repo, video or demo on page. · polish: Detailed hardware and model list but no visible assets inspected.
**Claims:** Fully functional prototype detecting emotion and reacting in real time
**Gaps:** No repo; LiveKit and Fetch.ai roles not described; No quantitative results
Sources: https://devpost.com/software/ted-ai-x8537t, https://cal-hacks-12-0.devpost.com/

---

