# SteelHacks — SteelHacks XIII (2026) (3 projects)

### Heard!
*SteelHacks SteelHacks XIII (2026) · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [NVIDIA] Beyond the Chatbot

**What it is:** An ambient voice agent that sits in a meeting: it transcribes speech, sorts ideas onto a live board, researches open questions with sub-agents, and speaks up when it has something to add. Nemotron classifies speech; Claude decides whether to talk.
**Problem / user:** Working teams in meetings who get only transcripts from AI tools, not participation.

**Features**
- Live notes — Notes agent rewrites meeting notes about every 20 s *[claimed]*
- Idea board — Fast classifier labels speech as idea, question or addressed to agent, creating cards *[claimed]*
- Background research — Claude front desk dispatches research sub-agents; results return in about 30 s *[claimed]*
- Spoken replies — Streamed ElevenLabs voice answers questions and interjects *[claimed]*
- Silence filter — Ignores off-topic and debugging chatter, with a harness limiting talking *[claimed]*

**Flow:** Speak in the meeting; speech is transcribed → Classifier sorts utterances into board cards → Agent decides to answer, research or stay silent → Spoken answer or research results delivered → Notes refresh in background

**Prompt:** NVIDIA 'Beyond the Chatbot' at SteelHacks XIII: build AI projects that go beyond a plain chatbot; no further brief extracted.
**Fit (explicit):** Ambient multi-agent that acts unprompted instead of waiting for chat; README lists the Beyond the Chatbot track.  *(targeted: [NVIDIA] Beyond the Chatbot)*
**Sponsor tools:** NVIDIA Nemotron Super 120B via NIM (Fast speech classifier and notes agent, core)
**AI:** Nemotron (reasoning off) classifies utterances and refreshes notes; a long-lived Claude Agent SDK session decides every audible action and spawns research sub-agents; ElevenLabs Scribe and TTS handle speech.
**Architecture:** FastAPI backend streams transcripts to a Nemotron classifier and notes agent; a Claude session acts as front desk; React/Vite board shows cards; ElevenLabs for voice.
**Novelty:** Agent chooses when to speak rather than answering on demand; team benchmarked Nemotron reasoning on/off; built largely with Claude Code.
**Scope:** medium · working: Repo with board, backend, eval folder and tests; screenshots; no demo video. · polish: Detailed README and docs; env example.
**Claims:** Cards appear within 5 s target | Research results in about 30 s
**Gaps:** no demo video; latency figures are targets not measurements
Sources: https://devpost.com/software/heard-puhs0f, https://github.com/jiazhenz026/heard-meeting (evidence README), sponsor_prompts_NVIDIA.jsonl

---

### SurrealEstate
*SteelHacks SteelHacks XIII (2026) · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [NVIDIA] Beyond the Chatbot

**What it is:** A home-buying assistant: paste a Zillow link or US address and a virtual agent, Sir Real Estate, gives a room-by-room interactive tour built from a labeled HouseGraph plus source-backed neighborhood research, and exports a one-page review sheet.
**Problem / user:** Home buyers, especially those relocating or buying remotely, who spend hours researching and visiting homes.

**Features**
- Listing intake — Starts from a Zillow link or U.S. address *[claimed]*
- HouseGraph tour — Floor plans, room IDs and panoramas converted into a navigable graph, rooms labeled by Nemotron vision *[claimed]*
- Virtual agent Q&A — Agent explains rooms and answers questions with ElevenLabs speech *[claimed]*
- Sourced neighborhood research — Evidence from Census, OpenStreetMap, FEMA, NCES, Yelp, Reddit with source IDs *[claimed]*
- One-page review sheet — Exportable flyer for comparing listings *[shown_working]*

**Flow:** Paste a Zillow link or address → System gathers neighborhood data → Explore rooms in the tour → Ask the agent questions → Export one-page sheet

**Prompt:** NVIDIA 'Beyond the Chatbot' at SteelHacks XIII: AI projects that go beyond a plain chatbot; no further brief extracted.
**Fit (implied):** Agentic pipeline where Nemotron orchestrates research, labels rooms with vision and verifies answers; page names the track win.  *(targeted: [NVIDIA] Beyond the Chatbot)*
**Sponsor tools:** NVIDIA Nemotron (Orchestration, vision room labeling, fact selection and verification, core)
**AI:** Nemotron orchestrates research, labels floor plans and verifies outputs; Gemini rewrites verified facts for buyers; ElevenLabs speaks.
**Architecture:** Research providers collect public data; Nemotron selects and verifies evidence; API layer keeps source IDs; frontend tour uses HouseGraph.
**Novelty:** Grounding with source IDs and fail-safe refusal when facts cannot be verified; team scrapped about 10 hours of work to refocus.
**Scope:** medium · working: Demo video, slides and landing/main/flyer screenshots linked; repo not read. · polish: Slide deck and exportable flyer.
**Claims:** Fails safely when information cannot be verified
**Gaps:** repo clone failed; video not watchable
Sources: https://devpost.com/software/surrealestate, sponsor_prompts_NVIDIA.jsonl

---

### Weave
*SteelHacks SteelHacks XIII (2026) · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [NVIDIA] Beyond the Chatbot; [MLH] Best Use of Gemini API

**What it is:** An Electron co-browser where a helper and a family member open the same site, each seeing a personalized accessible view, with shared cursors and annotations and an in-page jumping-spider assistant, Webb, that points to where to click.
**Problem / user:** Older relatives struggling with complex sites such as medical and banking, and the family members helping them.

**Features**
- Shared browsing sessions — Both users load the same page, with shared cursors and element-anchored annotations *[claimed]*
- Personal accessible views — Larger text, bigger targets, simplified wording, translation, or rebuilt clutter-free page per user *[claimed]*
- Webb assistant — Circles an element and explains it in the user's language, optional voice *[claimed]*
- Sanitized page model — Extracts labels and roles with deterministic IDs and classifies sensitive content before model calls *[claimed]*
- Audit log and host controls — Logs every outbound payload; host pause switch and field claims *[claimed]*
- Synthetic patient portal — Safe demo site *[shown_working]*

**Flow:** Both users open a site in Weave → Each picks personal display settings → See each other's cursors and notes → Ask Webb where to click → Webb highlights and explains, optionally by voice

**Prompt:** NVIDIA 'Beyond the Chatbot' at SteelHacks XIII: AI projects beyond a plain chatbot; MLH Best Use of Gemini API also won.
**Fit (implied):** Nemotron via NIM drives the in-page assistant and layouts, Gemini does translation and simplification; page lists both wins.  *(targeted: [NVIDIA] Beyond the Chatbot, [MLH] Best Use of Gemini API)*
**Sponsor tools:** NVIDIA Nemotron via NIM (Webb answers, element targeting, layout proposals, core); Gemini API (MLH) (Page translation and simpler wording, core)
**AI:** Nemotron handles assistant and layout; Gemini translates and simplifies; ElevenLabs voice; only sanitized labels reach models; hedged requests and provider fallback cut a 10-30 s latency tail to about 1 s.
**Architecture:** pnpm TypeScript monorepo: shared zod contracts, injectable overlay, Fastify coordinator server, Electron shell and synthetic patient portal.
**Novelty:** Privacy-first per-person page rebuilds with element-anchored annotations; heavy engineering around sanitization and latency.
**Scope:** large · working: Demo video embedded; latency fix reported; repo not read. · polish: Audit logging, host controls and fallback logic described.
**Claims:** Latency tail from 10-30 s to about 1 s | Every outbound payload audited
**Gaps:** repo clone failed; video not watchable; Snowflake tag unexplained
Sources: https://devpost.com/software/weave-z8t1i0, sponsor_prompts_NVIDIA.jsonl

---

