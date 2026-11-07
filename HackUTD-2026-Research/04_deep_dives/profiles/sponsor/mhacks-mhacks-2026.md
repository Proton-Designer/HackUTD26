# MHacks — MHacks 2026 (5 projects)

### CoClip
*MHacks MHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of Spacetime

**What it is:** CoClip is a fork of the OpenCut web video editor made multiplayer: several editors share one timeline through SpacetimeDB with live cursors and permissions, and a Gemini assistant edits the same timeline using the editor's own tools.
**Problem / user:** Video editors and creative teams who cannot co-edit one timeline with peers and an AI at the same time.

**Features**
- Link-based shared projects — Sharing a link gives co-editors the timeline, media and state; SpacetimeDB reducers keep everyone in sync and persisted. *[shown_working]*
- Live presence and cursors — Collaborator names, cursors and presence shown in the editor. *[claimed]*
- Read/write permissions and user removal — Owner controls who can edit or is removed. *[claimed]*
- Gemini timeline agent — Editor tools are exposed to Gemini so prompts perform actions on the shared timeline. *[claimed]*
- Large media handling — Optimized upload, display, sync and deletion of shared video files. *[claimed]*

**Flow:** Open a project → Share a link → Co-editor joins the same timeline → Both edit in real time → Prompt the AI assistant to act on the timeline

**Prompt:** MHacks 2026 sponsor prize from Clockwork Labs: use Spacetime/SpacetimeDB meaningfully in the project; the public listing gives only the prize name and amounts, no detailed brief.
**Fit (implied):** SpacetimeDB is the shared source of truth for timeline, media and collaboration state; all edits flow through its reducers.  *(targeted: Best Use of Spacetime)*
**Sponsor tools:** SpacetimeDB (Real-time shared timeline, media and permissions state, core)
**AI:** Google Gemini as a multimodal assistant calling OpenCut's existing editing tools against the shared project; audio analysis mentioned as expansion.
**Architecture:** Forked OpenCut web editor (Next/TypeScript monorepo plus Rust bits) with a collaboration module on SpacetimeDB cloud; Vercel hosting.
**Novelty:** Treats humans and an AI agent as peers editing one SpacetimeDB-backed timeline; large existing editor codebase reused.
**Scope:** large · working: Deployed demo on Vercel and 112k LOC repo with CI, Docker and tests (mostly inherited OpenCut). · polish: Custom branding and redesigned collaboration UI; no video.
**Claims:** Reliable shared state with persistence | Seamless real-time collaboration
**Gaps:** Repo mostly inherited code so team-added scope hard to size
Sources: https://devpost.com/software/coclip, https://github.com/anuragsk05/CoClip

---

### Concierge
*MHacks MHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Photon iMessage Agents Track Winner

**What it is:** Concierge lets a small-business owner text a problem like a broken walk-in fridge; it calls every relevant vendor in parallel with AI voice agents, negotiates, ranks quotes in code, texts a recommendation, and books on a YES reply. Other agents handle reviews, vendor email and deadlines.
**Problem / user:** Owner-operators of small businesses who lose time phoning repair shops and tracking admin deadlines.

**Features**
- iMessage-only owner interface — Photon Spectrum receives requests and sends proactive updates in three tiers: silent, FYI, needs-decision. *[shown_working]*
- Parallel AI voice negotiation — ElevenLabs agents call each vendor, disclose being AI, ask price and availability, and counter once using other quotes. *[shown_working]*
- Quote extraction and ranking — Transcripts become structured quotes ranked in code against budget, preferred and banned vendors; LLM writes only the explanation. *[claimed]*
- Reviews, Email and Deadlines agents — Tool-calling TypeScript runner drafts review replies, vendor emails after approval, and permit alerts. *[claimed]*
- Memory and Nessie money data — Supabase stores vendors, jobs and approvals; Nessie provides balances and payments. *[claimed]*
- Safety allowlists and approvals — Calls and emails only to allowed targets; no spend without an approval record. *[claimed]*

**Flow:** Owner texts 'walk-in is down, fix it' → Brain splits into jobs and calls all shops → Thread shows live quote updates → Concierge ranks and texts its pick → Owner replies YES to book

**Prompt:** MHacks 2026 Photon track: build iMessage agents on Photon; two placements with cash and Photon credits. The public listing gives no detailed brief.
**Fit (explicit):** Whole product is operated through an iMessage thread via Photon Spectrum with proactive messaging and approvals.  *(targeted: Photon iMessage Agents Track)*
**Sponsor tools:** Photon Spectrum (Owner iMessage interface, core); Capital One Nessie (Balances and payments data, supporting)
**AI:** OpenAI structured outputs split and route jobs and explain picks; ElevenLabs voice agents place calls; ranking and safety checks are deterministic code with zod validation.
**Architecture:** Photon iMessage in; brain service routes to ElevenLabs voice calls or TypeScript software agents; Supabase Postgres memory; Nessie for money.
**Novelty:** Parallel AI phone calls that cite competing quotes, combined with an iMessage-only interface and code-enforced approvals.
**Scope:** medium · working: 11.8k LOC with tests; demo video exists on Devpost; README placeholders for links. · polish: Docs folder and clear README; no live link.
**Claims:** Cites 36.2 million US small businesses, 8 in 10 with no employees
**Gaps:** Video not watchable
Sources: https://devpost.com/software/concierge-o38bu5, https://github.com/sszz01/zero-knowledge-team

---

### scalpal.
*MHacks MHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of Spacetime

**What it is:** Scalpal is a Meta Quest 3S surgical training app: pick a synthetic patient chart, interview them by voice, then perform an open appendectomy in VR or mixed reality while a voice coach talks you through. Controller motion also trains a simulated robot arm.
**Problem / user:** Surgical residents wanting whole-case practice, and robotics researchers needing demonstration data.

**Features**
- Chart-driven office visit — Synthetic FinchNode patients with derived risk flags; ElevenLabs voice patient; choose among four options per step. *[shown_working]*
- Voice coach with Time-Out — Claude-powered coach uses risks found or missed and coaches through the procedure. *[shown_working]*
- Appendectomy simulation — Mark and incise skin, split muscle, clamp and tie vessels; bleeding shows on a monitor and can end the case. *[shown_working]*
- Presage vitals — Phone camera reads a volunteer's pulse and breathing to set baseline vitals in mixed reality. *[claimed]*
- SpacetimeDB live dashboard — Shared tables and reducers drive physiology, session state and a web OR dashboard. *[shown_working]*
- Robot learning from demos — Controller demonstrations retargeted to a MuJoCo Franka arm; behavior-cloning policy graded and replayed. *[claimed]*
- Case authoring skill — Agent skill turns any FinchNode chart into a playable case. *[claimed]*

**Flow:** Choose patient and review chart → Interview in office → Commit to diagnosis → Enter VR or mixed-reality OR → Time-Out and operation with coaching → Recap, dashboard and robot replay

**Prompt:** MHacks 2026 sponsor prize from Clockwork Labs: use Spacetime/SpacetimeDB meaningfully in the project; the public listing gives only the prize name and amounts, no detailed brief.
**Fit (explicit):** SpacetimeDB module (25 tables, 52 reducers) holds sessions, coach transcript, headset commands and scheduled physiology, so all clients share state.  *(targeted: Best Use of Spacetime)*
**Sponsor tools:** SpacetimeDB (Shared simulation state, scheduled physiology, dashboard signaling, core); ElevenLabs (Patient and coach voices, speech-to-text, core); Presage SmartSpectra (Pulse and breathing from camera, supporting)
**AI:** Claude Sonnet runs patient and coach agents, Haiku classifies answers to options; scoring, risk flags and warnings are deterministic code; behavior-cloning policy trained in simulation.
**Architecture:** Unity 6 Quest app; TypeScript Hono case service; SpacetimeDB module; Python MuJoCo robotics; Next.js dashboard and docs.
**Novelty:** Combines voice-AI patient and coach, cross-engine parity-tested surgical physics, and a robot-learning loop in one VR training product.
**Scope:** large · working: 130k LOC, downloadable APK, live dashboard and demo video reported. · polish: Docs site, website, Docker, parity tests; cholecystectomy not yet playable.
**Claims:** Trained policy clearly outperformed replaying demos in simulation | Both engines reproduce a 41-action golden log
**Gaps:** Video not watchable
Sources: https://devpost.com/software/scalpal, https://github.com/stephenhungg/scalpal

---

### Tab: Groupchat Accountant
*MHacks MHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Photon iMessage Agents Track Winner

**What it is:** Tab is an iMessage group-chat bot that logs shared expenses from plain text or receipt photos, splits them, and posts settlement requests. Money only moves when the payer reacts with a thumbs-up. SpacetimeDB holds all state.
**Problem / user:** Friend groups sharing costs who dislike spreadsheets and splitting apps that make everyone download something.

**Features**
- Natural-language expense logging — Classifier filters money messages; Grok extracts amounts and splits, and every amount must appear in the original text. *[shown_working]*
- Receipt photo itemization — Grok vision reads items, tax and tip, checks totals, and members claim items. *[claimed]*
- Reaction-gated settlement — Thumbs-up from the payer completes a simulated transfer; thumbs-down opens a dispute on that share. *[shown_working]*
- Balance Q&A and live ledger — Templated answers for 'what do I owe' and a private web ledger with a money-flow graph. *[claimed]*
- Privacy handling — Non-money chatter is ignored and its text cleared from the database. *[claimed]*

**Flow:** Add Tab to a group chat → Post an expense → Tab replies with shares → Say settle up → React thumbs-up to pay or thumbs-down to dispute → Ask @tab ledger for the web view

**Prompt:** MHacks 2026 Photon track: build iMessage agents on Photon; two placements with cash and Photon credits. The public listing gives no detailed brief.
**Fit (implied):** Group-chat iMessage agent with tapback-driven actions; Mac bridge for messaging and SpacetimeDB backend.  *(targeted: Photon iMessage Agents Track, Best Use of Spacetime (mentioned stack))*
**Sponsor tools:** SpacetimeDB (Single source of truth, split math and settlement reducers, core); Capital One Nessie (Demo accounts and mirrored settlements, supporting); Photon (iMessage track (client uses a Mac bridge per page), unclear)
**AI:** Two stages: fast relevance classifier, then Grok for structured extraction and receipt vision; numbers validated by code and balances stated via templates.
**Architecture:** Mac iMessage bridge to Node/TypeScript service; SpacetimeDB Maincloud module with reducers; React/Vite/React Flow ledger.
**Novelty:** Uses emoji reactions as the consent mechanism for moving money and validates LLM numbers against source text.
**Scope:** medium · working: Page reports 250+ tests with simulated chat harness; repo unreadable here. · polish: Browser playground, demo mode; no video.
**Claims:** 250+ backend tests | 40+ reviewed PRs in one weekend
**Gaps:** Repo clone failed
Sources: https://devpost.com/software/tab-groupchat-finances

---

### Traycer: Food-waste Intelligence
*MHacks MHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of Spacetime

**What it is:** Traycer watches returned dining-hall trays with a phone camera, detects and estimates leftover food, and shows cost, carbon and water on a dashboard. A 3D cafeteria of AI diners tests menu changes, and two Relay characters advise by text, voice or video.
**Problem / user:** Kitchen and dining staff who cannot see what food is wasted or why.

**Features**
- Tray detection and tracking — YOLO-World and ByteTrack find trays and food; OpenAI vision estimates leftovers; staff accept or reject captures. *[shown_working]*
- Waste dashboard — Live totals by food with cost, grams, carbon, water and dish rankings. *[shown_working]*
- Gemini live insights — Gemini 2.5 Flash summarises a running service in two sentences. *[shown_working]*
- 3D cafeteria simulation — SpacetimeDB scheduled reducer runs the world every 200 ms; OpenAI drives diner choices and conversations. *[shown_working]*
- Menu-change simulator — Compares baseline and proposed menus on the same seeded diners with repeated baselines. *[claimed]*
- Relay advisors LeBron and Gordon — Characters query tray data and simulations over text, voice (ElevenLabs, Pipecat) or video and save recommendations. *[claimed]*

**Flow:** Phone camera watches trays → Vision estimates leftovers; staff review → Dashboard totals update → Gemini summary appears → Ask an advisor → Test change in simulation and verify next service

**Prompt:** MHacks 2026 sponsor prize from Clockwork Labs: use Spacetime/SpacetimeDB meaningfully in the project; the public listing gives only the prize name and amounts, no detailed brief.
**Fit (explicit):** Two SpacetimeDB modules (25 tables) store tray data and run the simulation in-database, with agents reading the same tables as the dashboard.  *(targeted: Best Use of Spacetime, Relay Interactive Agents, ElevenLabs, Gemini API)*
**Sponsor tools:** SpacetimeDB (Tray observations and in-database cafeteria simulation, core); Relay SDK (Two AI advisor characters, supporting); ElevenLabs (Voice output and listening, supporting)
**AI:** YOLO-World plus ByteTrack for detection, OpenAI vision for leftovers, OpenAI agents for simulated diners, Gemini 2.5 Flash for insights, Relay and Pipecat for conversational advisors.
**Architecture:** React/Three.js frontend; Python FastAPI vision service; Node simulation worker; SpacetimeDB modules plus SQLite linking recommendations to evidence.
**Novelty:** Connects real camera measurements to an agent-based simulation to test menu changes before service.
**Scope:** large · working: Live site and video listed; vision tests 14 of 17 pass per notes; no measured waste reduction. · polish: 3D landing page, accessibility features, design system.
**Claims:** 14 of 17 vision-model tests passed | Cites 1.05 billion tonnes food wasted in 2022 (UNEP)
**Gaps:** Conversion factors for carbon/water not stated
Sources: https://devpost.com/software/traycer-ai-food-waste-intelligence, https://github.com/anton-3/traycer

---

