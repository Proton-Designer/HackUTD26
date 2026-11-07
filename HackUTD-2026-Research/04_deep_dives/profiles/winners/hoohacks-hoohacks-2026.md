# HooHacks — HooHacks 2026 (3 projects)

### Agent Gauntlet
*HooHacks HooHacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 2nd Place [2nd]

**What it is:** A local benchmark and visual arena for evaluating browser agents' robustness against hostile web content. A task-completing agent and a red-team agent duel in a live browser, producing replayable traces and a safety verdict, in a Wild West bounty-board theme.
**Problem / user:** Browser agents can finish tasks yet be manipulated by page content; aimed at developers and safety researchers evaluating agent robustness.

**Features**
- Live duel arena — Large browser viewport with side rails for Task Agent and Red-Team activity plus a per-step prompt-health tracker. *[shown_working]*
- Playwright browser runner — Launches Chromium against a custom live URL or bundled synthetic page, capturing screenshots and DOM summaries each step. *[shown_working]*
- Adversarial attack families — Red-team injects scripted content in page: hidden instructions, deceptive UI, redirects/task diversion and credential-bait forms. *[shown_working]*
- Selectable policy modes — Both agents can run rule-based, adaptive or LLM-backed (OpenAI or Anthropic) policies; GPT-4o judges task completion. *[claimed]*
- Canary leak check — Checks whether planted sensitive values appear in the agent's actions to label a safety verdict. *[claimed]*
- Replay, history and dataset explorer — Completed sessions can be stepped through and browsed step-by-step. *[shown_working]*
- Structured exports — Runs export to JSON, CSV or ShareGPT-style JSONL for later analysis or training. *[shown_working]*
- Finisher poster — Bounty-poster style match summary exportable as PNG. *[shown_working]*

**Flow:** Open lobby and choose target URL, task, policies and difficulty → Start duel; session registered via local API → Watch Task Agent and Red-Team act in the live arena → Prompt-health and verdict signals update per step → Review replay, charts and dataset view → Export traces or poster

**Prompt:** Best Overall at HooHacks 2026 has no stated theme; considered automatically, scored on UI/UX, creativity, feasibility, functionality and impact (10 each).
**Fit (none):** Demo-friendly AI-safety benchmark with polished themed UI and exportable data; no prize is explicitly targeted.  *(targeted: Best Overall - 2nd Place)*
**AI:** Task agent and red-team agent each use rule-based or LLM policies (OpenAI/Anthropic); GPT-4o acts as a judge of task completion; traces are meant for later QLoRA fine-tuning of a Qwen model (not done).
**Architecture:** Next.js app with API routes starting a session; Playwright runner steps the task agent and red-team policy against a live or synthetic page, writes screenshots and logs to a local store feeding arena, replay, dataset and export views.
**Novelty:** Frames agent-security evaluation as a visible two-agent match with replay and training-ready exports, rather than a hidden metric.
**Scope:** medium · working: Repo about 60 files and 9.8k LOC with detailed README, architecture diagrams and seeded sessions. · polish: Custom themed UI, light/dark modes, poster export; no tests, video or live link.
**Claims:** Runs fully on local machine | Attacks injected so agent cannot tell them from real content | Agent can complete booking yet leak credentials to fake login (team finding)
**Gaps:** no benchmark results reported; no video; fine-tuning not completed
Sources: https://devpost.com/software/agent-gauntlet, https://github.com/abhimaddi/agent-gauntlet, https://hoohacks-2026.devpost.com/

---

### ScamShield
*HooHacks HooHacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 3rd Place [3rd]

**What it is:** A Raspberry Pi appliance that listens to phone calls played on speaker, transcribes them locally, scores scam likelihood with Gemini plus a keyword fallback, and triggers spoken, visual and messaging alerts while logging events to a family dashboard.
**Problem / user:** Older adults targeted by phone scams, isolated and pressured before family can intervene; also their relatives who want alerts.

**Features**
- Speakerphone call listening — Sound sensor detects voice activity; Pi captures audio chunks and Whisper tiny transcribes locally. *[shown_working]*
- Scam scoring — Gemini rates rolling transcript 0-100 with a short reason; keyword rules cover offline or slow cases. *[shown_working]*
- Spoken warning on Google Nest — ElevenLabs audio, fixed or Gemini-written, streamed to a Nest via Chromecast. *[shown_working]*
- Local hardware alerts — Grove LED turns red and buzzer sounds; a physical button triggers the pipeline manually. *[shown_working]*
- Family notifications — Alert sent to family by SMS/WhatsApp (README says Twilio SMS, page says WhatsApp). *[claimed]*
- Family dashboard — Next.js app with Auth0 shows device status, alerts, transcripts and timestamps from Postgres synced from the Pi's SQLite. *[shown_working]*
- SenseCAP display — Planned to show live transcript and alert state; unit was dead on arrival. *[planned]*

**Flow:** Put phone on speaker near the device → Pi transcribes call in chunks → Gemini and keyword check score the chunk → Threshold crossed: Nest warns aloud, LED and buzzer fire → Family gets a message → Family opens dashboard to review transcript

**Prompt:** Best Overall at HooHacks 2026 has no stated theme; considered automatically, scored on UI/UX, creativity, feasibility, functionality and impact (10 each).
**Fit (none):** Social-good hardware plus cloud system with clear user need; no prize is explicitly targeted.  *(targeted: Best Overall - 3rd Place)*
**AI:** Local Whisper tiny.en speech-to-text, Gemini 1.5 Flash for 0-100 scam score and reasons plus optional dynamic warning script, ElevenLabs TTS; deterministic keyword fallback.
**Architecture:** Pi Python service: sensor, STT, detection, alert pipeline, FastAPI and SQLite; background sync to Railway Postgres; ngrok tunnel; Next.js/Auth0 dashboard on Vercel.
**Novelty:** Zero-install elderly-friendly design using a standalone hardware box with multi-channel alerts, mixing local and cloud AI.
**Scope:** medium · working: 62 files, about 5.9k LOC, tests present, live dashboard at a custom domain, README with hardware table. · polish: Env example, docs folder, authenticated dashboard; no video; one display unit failed.
**Claims:** Alert fires within about 10 seconds of triggering phrase | Elder phone scams cost Americans over $3 billion per year | Works offline via keyword fallback and SQLite
**Gaps:** no accuracy metrics; no video; SMS vs WhatsApp discrepancy
Sources: https://devpost.com/software/scamshield-87rbxe, https://github.com/TristanGru/ScamShield, https://hoohacks-2026.devpost.com/

---

### Search and Rescue
*HooHacks HooHacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 1st Place [1st]

**What it is:** A web-based emergency-response simulator: users build or import multi-floor building layouts, view them in 2D and 3D, place responders, victims and hazard zones, then run a turn-by-turn rescue simulation computed by a Python backend with route planning.
**Problem / user:** Emergency planners, building designers and safety trainers wanting to test how layout and hazards affect rescue outcomes before real incidents.

**Features**
- Building import and cell editor — Loads structured JSON or a flat grid, with archetype presets (apartment, hospital, warehouse, school) and a paint editor for walls, doors, windows, stairs. *[shown_working]*
- 2D floor plan viewer — Color-coded SVG per floor with legend, floor tabs, scroll zoom. *[shown_working]*
- 3D building visualizer — WebGL view of the same building data and simulation results. *[shown_working]*
- Responder and victim placement — Panel places agents by x/y/floor with labels and feeds the simulation payload. *[shown_working]*
- Rescue simulation engine — FastAPI backend computes per-turn movement, extraction routes and outcomes; A* pathing and Hungarian assignment per Devpost. *[shown_working]*
- Timeline replay — Slider scrubs turns from dispatch to rescue or failure. *[shown_working]*
- Hazard modeling — Hazard zones such as fire or threats change routing; propagation models are basic. *[claimed]*
- AI summary of simulation — Generated summary was taken down over credit errors. *[unclear]*

**Flow:** Import or paint a multi-floor building → Inspect it in 2D and 3D → Place rescuers, victims and hazards → Press Run so backend computes routes → Scrub the timeline to review outcomes

**Prompt:** Best Overall at HooHacks 2026 has no stated theme; considered automatically, scored on UI/UX, creativity, feasibility, functionality and impact (10 each).
**Fit (none):** Integrated editor, 3D view, simulator and replay with deployed demo; no prize is explicitly targeted.  *(targeted: Best Overall - 1st Place)*
**AI:** Mostly classical algorithms (A* pathfinding, Hungarian assignment) described as AI-powered; a generative summary existed but was removed. No named ML model.
**Architecture:** React/Vite frontend with SVG and WebGL/Three.js views posts JSON building and agent data to a FastAPI simulator that returns per-turn states for replay.
**Novelty:** Combines building authoring, 3D viewing and multi-agent rescue routing in one tool, uncommon in a 24-hour build.
**Scope:** large · working: 85 files, about 24k LOC (partly data), Render live demo, README with run instructions. · polish: Multiple views, presets, timeline slider; no tests or video; AI summary disabled.
**Claims:** Backend calculates optimal extraction paths in real time | Everything works except removed AI summary
**Gaps:** no video; no metrics; live demo not opened
Sources: https://devpost.com/software/search-and-rescue-2pwlkf, https://github.com/Imranbilal268/Search_and_Rescue, https://hoohacks-2026.devpost.com/

---

