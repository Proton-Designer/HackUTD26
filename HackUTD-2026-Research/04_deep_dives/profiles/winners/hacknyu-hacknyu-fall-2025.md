# HackNYU — HackNYU - Fall 2025 (1 projects)

### Agora Socrates
*HackNYU HackNYU - Fall 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** MLH - Best Use of Vultr Cloud; Best First Time Hack

**What it is:** A voice-first AI tutor that ingests a student's notes, PDFs or photos, then teaches Socratically by speech while drawing notes and visuals on an infinite Tldraw whiteboard, backed by a LangGraph agent, Gemini and a Qdrant vector store.
**Problem / user:** Students who study passively from their own notes and benefit from guided questioning and active recall.

**Features**
- Materials ingest — Uploads of PDFs, images and text parsed with Docling, embedded with Gemini and stored in Qdrant per user and course *[claimed]*
- Push-to-talk voice loop — Deepgram speech-to-text, LangGraph routing, RAG, Socratic reply, ElevenLabs speech back *[claimed]*
- Socratic prompting — Guiding questions and analogies rather than answers, with frustration monitoring and a quiz mode per README *[claimed]*
- Whiteboard actions — Backend emits create, highlight and load-image messages that Tldraw renders *[claimed]*
- Long-term memory — Qdrant stores student memory and tracks confused topics *[claimed]*
- Spaced repetition and self-explanation scoring — Review quizzes at session start and scoring of explanations against sources *[planned]*

**Flow:** Upload notes, PDFs or lecture photos → Hold push-to-talk and speak → Speech transcribed and routed through the agent → Relevant notes retrieved → Tutor answers aloud with questions and draws on the whiteboard → Confused topics saved

**Prompt:** MLH Best Use of Vultr Cloud: Vultr is pitched for quick launches via one-click deployment, scalable compute and GPUs for AI. Best First Time Hack: whole team must be first-time hackers ($200).
**Fit (none):** Both prizes are shown on the page but it says nothing about Vultr use; the repo has Dockerfiles and compose for a full-stack deploy, with no Vultr reference seen in the README.  *(targeted: MLH - Best Use of Vultr Cloud, Best First Time Hack)*
**Sponsor tools:** Vultr Cloud (Not described anywhere read; likely hosting, unclear)
**AI:** Gemini 2.5 Pro for reasoning and vision, a stateful LangGraph agent with RAG over Qdrant, Deepgram STT and ElevenLabs TTS; Socratic system prompt with guardrails for idk and poor retrievals.
**Architecture:** Next.js client with Tldraw and Socket.IO; FastAPI backend hosting LangGraph nodes, Gemini, Qdrant and speech services; shared Pydantic/Zod message schemas; Docker Compose.
**Novelty:** Combines voice tutoring, retrieval over personal notes and an AI that draws on a shared whiteboard, with typed message contracts.
**Scope:** medium · working: About 14k lines, tests, Dockerfiles and compose; Devpost says full voice-to-visual loop achieved. · polish: Structured README, env examples, logging; no demo link or video.
**Claims:** Full multimodal loop from voice to speech and canvas visuals | AI drew a whiteboard note from its own reasoning
**Gaps:** Vultr usage not described; Devpost lists Gemini only while README adds Deepgram and ElevenLabs
Sources: https://devpost.com/software/agora-socrates, evidence/hacknyu-hacknyu-fall-2025-agora-socrates.json (README), https://hacknyu-fall-2025.devpost.com/

---

