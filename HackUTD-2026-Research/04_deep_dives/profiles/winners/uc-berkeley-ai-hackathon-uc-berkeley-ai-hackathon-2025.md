# UC Berkeley AI Hackathon — UC Berkeley AI Hackathon 2025 (7 projects)

### MayDay
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Fetch AI: Best Use of Fetch AI; Unify: Best Use of Multimodal AI Agent

**What it is:** MayDay is an assistant layer for air traffic controllers that ingests live ATC radio, transcribes it in 5-second chunks with an aviation-tuned Whisper model, structures it with LLMs, and uses agents to flag emergencies and phone first responders.
**Problem / user:** Tower air traffic controllers juggle many aircraft at once, with heavy cognitive load; the team frames the tool as support for them, not a replacement.

**Features**
- Live ATC audio transcription — Streams LiveATC audio and transcribes 5-second chunks with a Whisper model fine-tuned for ATC, run on Groq. *[claimed]*
- LLM parsing of transcripts — LLMs turn raw transcript text into structured data about flights and instructions. *[claimed]*
- Multi-agent anomaly detection — Fetch.ai uAgents handle transcription, parsing and emergency detection, flagging runway incursions and communication anomalies. *[claimed]*
- Automated first-responder call — On an emergency, a Vapi phone call alerts and briefs first responders. *[claimed]*
- Radar-style dashboard — Next.js UI over WebSockets shows aircraft positions, alerts and communication logs in real time. *[claimed]*
- Shift handoff with memory — An End Shift tab uses Letta memory to pass full context to the next controller. *[claimed]*
- Flight info view — Dashboard view of flight details. *[claimed]*

**Flow:** Live ATC audio is streamed from LiveATC → Audio is transcribed in 5-second chunks → LLMs parse transcripts into structured data → Agents check for anomalies, conflicts and emergencies → Dashboard shows positions, alerts and logs → In a simulated emergency a Vapi call alerts first responders → End Shift tab hands off context via Letta

**Prompt:** Fetch AI: best use of Fetch AI (3 winners, $3,000 cash; no description given). Unify: best use of a multimodal AI agent ($2,500 and an onsite interview chance for open Unify roles).
**Fit (implied):** Built the transcribe-parse-detect pipeline as distributed Fetch.ai uAgents (Agentverse, ASI:One) and combined voice (Whisper, Vapi), memory (Letta) and LLMs. Unify itself is not named on the page.  *(targeted: Fetch AI: Best Use of Fetch AI, Unify: Best Use of Multimodal AI Agent)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse / ASI:One (agents for transcription, parsing and emergency detection, core); Vapi (automated phone call to first responders, supporting); Letta (memory for end-of-shift handoff, supporting); Groq (fast inference of fine-tuned Whisper, supporting)
**AI:** Fine-tuned Whisper (medium.en for ATC, from Hugging Face) on Groq for speech-to-text; Gemini and Claude parse transcripts; uAgents detect anomalies; Letta stores memory.
**Architecture:** LiveATC audio -> FastAPI backend with WebSockets -> Whisper transcription -> LLM parsing -> Fetch.ai agents (REST/WebSocket) -> Next.js radar dashboard; Vapi for calls, Letta for handoff memory.
**Novelty:** Targets a specialized safety domain (tower ATC) using a domain-tuned speech model on real LiveATC streams, and chains agents to a real phone-call action.
**Scope:** medium · working: Claims a functioning real-time system and embeds a demo video; no metrics; repo not readable here. · polish: Radar-style dashboard and multiple integrated services shown in screenshots.
**Claims:** Claims a fully functional real-time ATC monitoring system | No accuracy, latency or detection metrics reported
**Gaps:** GitHub repo README unreachable (clone failed, raw 404); Video not watched; Same Devpost page appears twice in the queue under two project ids; Queue id suggests a bundle (HireSense, MayDay, AlphaRescue) but only MayDay appears on this Devpost page
Sources: https://devpost.com/software/mayday-l74dub, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### MayDay
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
> Same Devpost page as `uc-berkeley-ai-hackathon-uc-berkeley-ai-hackathon-2025-hiresense-mayday-alpharescue-mayday` (duplicate listing).
**Prizes:** Unify: Best Use of Multimodal AI Agent; Fetch AI: Best Use of Fetch AI

**What it is:** MayDay is an assistant layer for air traffic controllers that ingests live ATC radio, transcribes it in 5-second chunks with an aviation-tuned Whisper model, structures it with LLMs, and uses agents to flag emergencies and phone first responders.
**Problem / user:** Tower air traffic controllers juggle many aircraft at once, with heavy cognitive load; the team frames the tool as support for them, not a replacement.

**Features**
- Live ATC audio transcription — Streams LiveATC audio and transcribes 5-second chunks with a Whisper model fine-tuned for ATC, run on Groq. *[claimed]*
- LLM parsing of transcripts — LLMs turn raw transcript text into structured data about flights and instructions. *[claimed]*
- Multi-agent anomaly detection — Fetch.ai uAgents handle transcription, parsing and emergency detection, flagging runway incursions and communication anomalies. *[claimed]*
- Automated first-responder call — On an emergency, a Vapi phone call alerts and briefs first responders. *[claimed]*
- Radar-style dashboard — Next.js UI over WebSockets shows aircraft positions, alerts and communication logs in real time. *[claimed]*
- Shift handoff with memory — An End Shift tab uses Letta memory to pass full context to the next controller. *[claimed]*
- Flight info view — Dashboard view of flight details. *[claimed]*

**Flow:** Live ATC audio is streamed from LiveATC → Audio is transcribed in 5-second chunks → LLMs parse transcripts into structured data → Agents check for anomalies, conflicts and emergencies → Dashboard shows positions, alerts and logs → In a simulated emergency a Vapi call alerts first responders → End Shift tab hands off context via Letta

**Prompt:** Fetch AI: best use of Fetch AI (3 winners, $3,000 cash; no description given). Unify: best use of a multimodal AI agent ($2,500 and an onsite interview chance for open Unify roles).
**Fit (implied):** Built the transcribe-parse-detect pipeline as distributed Fetch.ai uAgents (Agentverse, ASI:One) and combined voice (Whisper, Vapi), memory (Letta) and LLMs. Unify itself is not named on the page.  *(targeted: Fetch AI: Best Use of Fetch AI, Unify: Best Use of Multimodal AI Agent)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse / ASI:One (agents for transcription, parsing and emergency detection, core); Vapi (automated phone call to first responders, supporting); Letta (memory for end-of-shift handoff, supporting); Groq (fast inference of fine-tuned Whisper, supporting)
**AI:** Fine-tuned Whisper (medium.en for ATC, from Hugging Face) on Groq for speech-to-text; Gemini and Claude parse transcripts; uAgents detect anomalies; Letta stores memory.
**Architecture:** LiveATC audio -> FastAPI backend with WebSockets -> Whisper transcription -> LLM parsing -> Fetch.ai agents (REST/WebSocket) -> Next.js radar dashboard; Vapi for calls, Letta for handoff memory.
**Novelty:** Targets a specialized safety domain (tower ATC) using a domain-tuned speech model on real LiveATC streams, and chains agents to a real phone-call action.
**Scope:** medium · working: Claims a functioning real-time system and embeds a demo video; no metrics; repo not readable here. · polish: Radar-style dashboard and multiple integrated services shown in screenshots.
**Claims:** Claims a fully functional real-time ATC monitoring system | No accuracy, latency or detection metrics reported
**Gaps:** GitHub repo README unreachable (clone failed, raw 404); Video not watched; Same Devpost page appears twice in the queue under two project ids
Sources: https://devpost.com/software/mayday-l74dub, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### MediBuddy
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Vapi: Best Voice-Powered AI Project

**What it is:** A doctor-patient web platform that transcribes visits by voice, structures and summarizes them, and has agents match the patient to clinical trials; the patient must consent before limited data goes to a trial sponsor.
**Problem / user:** Trials are under-enrolled because patients do not know they qualify and doctors lack time to screen; targets patients and doctors who also carry note-taking overhead.

**Features**
- Appointment booking with approval — Patients request appointments; doctors approve them from a role-based dashboard. *[claimed]*
- Real-time visit transcription — Groq-hosted Whisper v3 Large Turbo transcribes the voice conversation during the appointment. *[claimed]*
- Structured summary and report — Gemini extracts conditions, age, comorbidities and produces a report from the transcript. *[claimed]*
- Agent-based trial matching — ASI-1 (Fetch.ai) simulates sponsor agents that match extracted patient data to trials; README also lists a ClinicalTrials.gov API setting. *[claimed]*
- Patient consent flow — Dedicated interface where the patient approves sharing limited data; sponsor is notified on approval. *[claimed]*
- Doctor and patient dashboards — Doctors manage requests and suggest trials; patients review transcripts, summaries and suggested trials. *[claimed]*
- Role-based authentication — Clerk-based auth for doctors and patients with Convex real-time data. *[claimed]*

**Flow:** Patient books appointment; doctor approves → Visit conversation captured by voice and transcribed → Gemini structures info and generates report → Agents match patient against trials → Patient reviews consent screen and approves limited sharing → Both sides review results on their dashboards

**Prompt:** Vapi: Best Voice-Powered AI Project; prize is 500 Vapi credits for one winner; no further description published.
**Fit (implied):** Voice is the primary input: visits are captured and transcribed by speech-to-text, feeding the whole pipeline. No Vapi integration is listed; the voice fit is via Groq Whisper.  *(targeted: Vapi: Best Voice-Powered AI Project)*
**Sponsor tools:** Fetch.ai ASI-1 (simulated sponsor agents for trial matching, core); Groq (Whisper v3 Large Turbo) (speech-to-text of visits, core); Vapi (not listed on page or README, unclear)
**AI:** Whisper v3 Large Turbo on Groq for transcription; Gemini with tuned prompts for entity extraction and summaries; ASI-1 agents for trial matching.
**Architecture:** React/TypeScript/Tailwind frontend on Vercel; Convex backend and real-time DB with Clerk auth; audio -> Groq -> Gemini -> ASI-1 sponsor agents -> consent step.
**Novelty:** Combines ambient visit transcription with automatic trial matching and an explicit consent gate in one workflow, using simulated sponsor agents.
**Scope:** medium · working: Live Vercel demo link and a roughly 22k-LOC repo; README calls it an end-to-end prototype built in under 24 hours. · polish: Role-based dashboards, many Radix UI components, setup docs and .env example; no tests.
**Claims:** End-to-end prototype built in under 24 hours | Privacy-first with patient-controlled consent | No enrollment or accuracy metrics given
**Gaps:** No demo video; Sponsor agents are simulated; trial registry use unclear; README mentions OpenAI key and Supabase dep not described on Devpost
Sources: https://devpost.com/software/medibuddy-y7t65f, evidence/medibuddy.json (README), https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### Navo
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Nobel Era Group: Best Projects Leveraging LLM (truncated)

**What it is:** Navi (listed as Navo in the queue) is an AI route planner pitched as an AI chauffeur: the user types a plain-language request such as a fitness loop, scenic drive or food crawl and gets a tailored route built on Google Maps services.
**Problem / user:** Implied: people who want personalized, activity-specific routes rather than plain point-to-point directions; the page states no explicit problem.

**Features**
- Prompt-to-route generation — User describes a journey in natural language and the app returns a route tailored to it. *[claimed]*
- Journey types — Fitness loops, scenic drives and foodie crawls are the named route styles. *[claimed]*
- Google Maps integration — Uses Google Maps, Directions and Geocoding for route building. *[claimed]*
- LLM routing brain — OpenAI and ASI1 models listed as the AI layer; the team plans to keep refining it. *[unclear]*

**Flow:** Open the app → Type a simple prompt for the journey → Receive a tailored route

**Prompt:** Nobel Era Group: Best Projects Leveraging LLM Agents (with Berkeley RDI); $4,000 across three tiers; no description published.
**Fit (implied):** LLM interprets a free-text request and plans a route; agent use is only hinted by Fetch.ai and ASI1 tags and is not explained.  *(targeted: Nobel Era Group: Best Projects Leveraging LLM Agents)*
**Sponsor tools:** Fetch.ai / ASI1 (listed in tags; role not described, unclear)
**AI:** LLMs (OpenAI, ASI1) turn natural-language prompts into route plans using Google Directions and Geocoding; details not described.
**Architecture:** Not described; stack tags show Python, TypeScript, JavaScript and Swift with Google Maps APIs, a Replit-hosted web demo and an iOS plan.
**Novelty:** Frames routing around intent (workout, scenery, food) instead of destination; page is thin on how it works.
**Scope:** small · working: A Replit demo link is listed but not exercised; no video or repo. · polish: Very short writeup; MVP planned for App Store.
**Claims:** Won Nobel Era Group LLM Agents award
**Gaps:** No repo; Thin description; Queue prize label was truncated; page says Best Projects Leveraging LLM Agents; Live demo not visited
Sources: https://devpost.com/software/navi-google-maps-but-better, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### Octavo
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Orkes: Best Use of Orkes

**What it is:** A search engine over collective lived experience: each user gets a Letta memory agent, anonymized memories feed domain-level collective agents, and Orkes workflows run relevant agents in parallel to synthesize an answer with confidence scoring.
**Problem / user:** People with nuanced personal questions (career changers, first-gen students, founders) who find generic web results miss real experiences.

**Features**
- Per-user memory agents — Each user has a Letta agent storing background, decisions and experiences. *[claimed]*
- Collective domain agents — Anonymized memories aggregate into sub-agents like cs-careers or founder-journeys. *[claimed]*
- Orkes workflow orchestration — Orkes coordinates multiple agents in parallel for cross-domain queries. *[claimed]*
- Automatic agent selection — The system picks relevant domains from the query. *[claimed]*
- Time-versioned memory — Memory branches allow comparing advice from different years. *[claimed]*
- Reasoning transparency — Users can inspect tool calls, memory blocks and confidence scores behind answers. *[claimed]*
- Live workflow visualization — Shows the multi-agent reasoning process in real time. *[claimed]*

**Flow:** Ask a natural-language question → System selects relevant memory domains → Orkes runs Letta agents in parallel → Groq and Claude synthesize patterns with confidence score → User inspects reasoning and compares across time

**Prompt:** Orkes: Best Use of Orkes; one winner receiving a $200 gift card; no further description published.
**Fit (explicit):** Orkes is the orchestration layer that dynamically selects and runs several Letta memory agents in parallel and drives a real-time workflow visualization.  *(targeted: Orkes: Best Use of Orkes)*
**Sponsor tools:** Orkes (workflow orchestration of memory agents, core); Letta (per-user and collective memory agents, core); Groq (fast synthesis and confidence scoring, supporting)
**AI:** Letta memory agents with PostgreSQL persistence; Groq for fast pattern detection and confidence scores; Claude 4 for nuanced synthesis.
**Architecture:** Next.js frontend; Orkes workflows call Letta agents (individual and domain) in parallel; Groq/Claude synthesize results; Python backend.
**Novelty:** Treats anonymized personal memory as the search corpus and exposes memory versioning and reasoning internals.
**Scope:** medium · working: Live Vercel demo link; claims sub-second responses without benchmarks; no repo or video. · polish: Detailed writeup with example queries and visualizations; live site not visited.
**Claims:** World's first search engine powered by persistent collective memory (self-described) | Sub-second responses on complex queries | Example answer drawing on 86+ people
**Gaps:** No repo; Anonymization method undescribed; Claims unverified
Sources: https://devpost.com/software/octopus-pzv5l0, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### pFOG: Parkinson's Medical Aid Device
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** GRAND PRIZE - Social Impact Track; Cal Hacks: Hacker's Choice

**What it is:** A wearable prototype for Parkinson's freezing of gait: an IMU on an ESP32 feeds a CNN-LSTM that detects freezing onset and a servo-driven arm delivers a physical poke to the leg, plus a web tool to record and label gait data.
**Problem / user:** People with Parkinson's who suddenly cannot walk during freezing episodes; motivated by a family member's condition.

**Features**
- Freezing-of-gait prediction — PyTorch 1D-CNN feeding an LSTM classifies accelerometer and gyroscope streams to detect FOG onset in real time. *[claimed]*
- Servo stimulation — On detection a servo-actuated robotic arm pokes the frozen leg to mimic targeted muscle stimulation. *[claimed]*
- Wearable sensing module — Adafruit MPU-6050 IMU and ESP32 sending CSV samples over UART serial. *[shown_working]*
- Live data collection web app — Next.js UI with live accelerometer and gyroscope charts over WebSocket from a Flask backend, with SQLite storage. *[shown_working]*
- Keyboard state labeling — Press W, S or F to label walking, standing or freezing during a recording session. *[shown_working]*
- Session history and CSV export — Sessions are stored with IDs and statistics and exported as CSV for model training. *[shown_working]*
- Per-user fine-tuning — Users record their own gait to fine-tune the model for gait variability. *[claimed]*

**Flow:** Wear the IMU module → Optionally record a session in the web UI and label states with W/S/F → Export CSV to train or fine-tune the model → Live sensor data is analyzed on the device pipeline → Model flags freezing → Servo arm pokes the leg to help the patient resume walking

**Prompt:** Grand Prize Social Impact Track: $5,000 cash plus API credits, selected by a panel of expert VCs. Cal Hacks Hacker's Choice: custom backpacks, no description.
**Fit (implied):** Health-focused assistive device for a neurological condition affecting daily mobility; Devpost does not state which prize it targeted.  *(targeted: GRAND PRIZE - Social Impact Track, Cal Hacks: Hacker's Choice)*
**AI:** Hybrid 1D-CNN plus LSTM in PyTorch on 6-axis IMU windows to classify walking, standing and freezing; trained on the team's own limited, noisy recordings.
**Architecture:** ESP32 reads MPU-6050 and streams CSV over serial to a Python connector, then a Flask API with WebSocket and SQLite, then a Next.js dashboard; model drives the servo.
**Novelty:** Closes the loop from sensing to a physical actuation aimed at breaking a freeze, pairing custom hardware with a labeling tool for collecting its own training data.
**Scope:** small · working: README documents the working data pipeline and labeling tool; Devpost claims a working prototype; no demo video. · polish: Hand-assembled hardware with improvised wiring; README is clear on setup and API; about 5k LOC, no tests.
**Claims:** Detects FOG episodes with over 90% accuracy and responds in real time | No test methodology or clinical validation given
**Gaps:** README covers only data-collection system, not model training or servo firmware; No video; Accuracy claim unverified
Sources: https://devpost.com/software/foggy, evidence/pfog (README), https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### Vocal AI
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Vapi: Most Ambitious Vapi Project

**What it is:** A web-based vocal coaching app that analyzes a singer's voice in the browser, then pairs a proactive Fetch.ai analysis agent with a Letta conversational coach and a Vapi voice coach to give lessons and feedback.
**Problem / user:** Singers, speakers and voice actors who practice alone with no real-time feedback, personalized coaching or progress tracking in one place.

**Features**
- Real-time pitch detection — Web Audio API captures the mic and shows live pitch visualization during practice. *[claimed]*
- Deep vocal metrics and voice type — Custom analyzer computes jitter, shimmer, vibrato rate and range, and classifies soprano, alto, tenor or bass. *[claimed]*
- Dual-agent AI coach — Proactive Fetch.ai agent produces analysis and daily reports; reactive Letta agent chats with long-term memory of progress. *[claimed]*
- Personalized lessons and exercises — Lesson plans and exercises generated from vocal analysis and goals, with retrieval-based tips and a feedback loop. *[claimed]*
- Vapi voice conversations — Real-time spoken sessions with the coach, using a custom-tuned Vapi voice model. *[claimed]*
- Progress tracking and reports — Supabase stores sessions and history; LLM-based Vocal Scores and daily summaries show trends. *[claimed]*
- Groq music-file analysis — Groq analyzes uploaded music files to generate feedback insights. *[claimed]*
- Community and export — Progress sharing, challenges and export of analyses and plans. *[claimed]*

**Flow:** Sign in and set profile: voice type, skill level, goals, range → Practice with live pitch visualization → Analysis results feed lessons and practice reports → Chat or talk to the Letta/Vapi coach about progress → Complete lessons; feedback is stored → Review daily AI summaries and progress

**Prompt:** Vapi: Most Ambitious Vapi Project; 1,000 Vapi credits for one winner; no further description published.
**Fit (explicit):** Vapi voice agent is one layer of a larger multi-agent stack (Vapi, Letta, Fetch.ai, Groq) with a custom-tuned Vapi voice model trained on song material.  *(targeted: Vapi: Most Ambitious Vapi Project)*
**Sponsor tools:** Vapi (real-time voice coaching conversations with custom-tuned voice, core); Letta (stateful coach with long-term memory, core); Fetch.ai (proactive analysis and report agent, supporting); Groq (music-file analysis, supporting)
**AI:** Letta memory agent for coaching chat, Fetch.ai agent for proactive reports, Vapi voice agent, LLM scoring, RAG over vocal-technique tips, few-shot lesson generation, intent router with function calling.
**Architecture:** React/Vite app on Netlify does in-browser audio analysis; FastAPI backend in Docker on Cloud Run routes to Letta, Fetch.ai, Vapi and Groq; Supabase holds data with RLS.
**Novelty:** Pairs in-browser acoustic voice metrics with three separate agent platforms and a voice model tuned on specific songs, an unusually wide integration surface for a hackathon.
**Scope:** medium · working: Live Netlify demo and YouTube demo linked in README; about 15k LOC repo; page admits known errors with Supabase storage. · polish: Many screens (dashboard, lessons, practice, coach); detailed README; no tests.
**Claims:** Won Most Ambitious Vapi Project | Vapi agent trained over 180 minutes on two songs | README: over 1,200 developers competed | No accuracy or latency metrics
**Gaps:** Devpost has no video but README links a YouTube demo (not watched); Model used for voice-type classification unnamed
Sources: https://devpost.com/software/vocai-ai-coach, evidence/vocal-ai (README), https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

