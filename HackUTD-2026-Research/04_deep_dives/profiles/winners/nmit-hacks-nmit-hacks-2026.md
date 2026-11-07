# NMIT Hacks — NMIT HACKS 2026 (5 projects)

### Mandamus
*NMIT Hacks NMIT HACKS 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Third Prize [3rd]; Best Use of Gemini API (MLH); Third Prize (Render) [3rd]

**What it is:** An AI platform aimed at the Indian court system: anonymous sensitive-crime reporting logged on Solana, Gemini analysis of uploaded evidence, a voice legal assistant, and virtual hearings with synced courtroom state. The README adds summariser, precedent, drafting and scheduling modules.
**Problem / user:** India has tens of millions of pending cases; judges, lawyers, victims and ordinary citizens face delays and poor access to the system.

**Features**
- Silent Justice anonymous vault — Sensitive-crime reports are submitted anonymously and their hashes logged on Solana as a chain of custody. *[claimed]*
- Multimodal evidence analysis — Uploads to Google Cloud Storage trigger Gemini 1.5 Flash to read images, CCTV logs and documents and give strength summaries. *[claimed]*
- Voice legal assistant — Explains law in plain regional language; ElevenLabs speech delivered as Base64 JSON to fix browser audio errors. *[claimed]*
- Virtual hearings — WebRTC courtroom; signaling moved to Managed Redis so sessions survive restarts. *[claimed]*
- Real-time courtroom sync — Backboard.io keeps judge and lawyer dashboards in sync without polling. *[claimed]*
- n8n report routing — Workflow automation routes, analyses and logs reports to authority channels asynchronously. *[claimed]*
- README: summariser, precedents, draft RAG — OCR plus Pegasus/BART summaries, sentence-transformer precedent search over a mock JSON, and RAG judgement drafts with diff audit. *[claimed]*
- README: readiness scheduler and biometrics — Rule-based readiness check against e-Courts data and face/voice/liveness gate with judge ADMIT action. *[planned]*

**Flow:** Victim files anonymous report; logged on Solana and routed by n8n → Evidence upload to GCS triggers Gemini analysis → Results show on judicial dashboard → Judge invites lawyers to virtual hearing → Citizens use voice assistant for guidance

**Prompt:** not public / not found
**Fit (explicit):** Devpost lists these tracks; Gemini reads evidence, ElevenLabs voices the assistant, Backboard syncs hearings, Render hosts the app.  *(targeted: AI & ML, ElevenLabs, Google Gemini (MLH), MongoDB Atlas (MLH), Backboard (MLH), Render)*
**Sponsor tools:** Gemini API (Multimodal evidence reading and summaries, core); ElevenLabs (Voice output for legal assistant, core); Backboard.io (Real-time courtroom state sync, supporting); MongoDB Atlas (Primary datastore, supporting); Render (Backend deployment, supporting)
**AI:** Gemini 1.5 Flash for multimodal evidence analysis; ElevenLabs text-to-speech; README also describes Pegasus/BART summarisation, sentence-transformer retrieval and an Amazon Nova RAG draft generator.
**Architecture:** React/Vite frontend on Vercel; FastAPI backend (Render, Vultr) with MongoDB Atlas, GCS, Redis-backed Node signaling for WebRTC, Backboard sync, n8n workflows and Solana logging.
**Novelty:** Unusually wide scope across the judicial workflow, mixing blockchain custody, voice AI and live hearings; many modules are described but unproven.
**Scope:** large · working: Live frontend and backend URLs listed; repo about 32k lines with FastAPI, signaling and n8n folders; no demo video. · polish: Long README with diagrams and ASCII logo, logo, 3D guide component; no tests.
**Claims:** Over 50 million pending cases targeted | Summarise 500+ pages into 1 page in under 60 seconds (README) | Cut drafting time by up to 80% (README)
**Gaps:** Devpost (Gemini, Solana, ElevenLabs, Snowflake, Redis) and README (Nova Pro, Delta Lake, biometrics, Firebase) differ; first six features follow Devpost, last two follow README; README calls precedents_db.json a mock; Prize text not published
Sources: https://devfolio.co/projects/mandamus-ai-judicial-infrastructure-platform-a842, evidence/nmit-hacks-nmit-hacks-2026-mandamus.json, https://github.com/KISHORE0709-LEO/Mandamus (README), https://nmithacks26.devfolio.co/

---

### Peer2Play
*NMIT Hacks NMIT HACKS 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Second Prize [2nd]

**What it is:** A browser demo where players of a WebAssembly game share cached assets such as levels and textures directly with each other over WebRTC instead of always fetching from the origin server, with a metrics UI. Built on the OpenLara Tomb Raider engine.
**Problem / user:** Streaming games suffer latency, single-server failure and repeated downloads of identical heavy assets; relevant to players and hosts paying bandwidth.

**Features**
- Peer asset sharing over WebRTC — Peers with cached assets send them via DataChannels; origin server is the fallback. *[shown_working]*
- Browser-level request interception — Devpost says a Service Worker intercepts requests; README says a bootstrap script wraps window.fetch with no engine changes. *[claimed]*
- Signaling server — Node, Express and WebSockets let peers discover who holds an asset. *[shown_working]*
- IndexedDB persistence — Downloaded assets cached locally for later redistribution. *[claimed]*
- SHA-256 integrity check — Receivers rehash assets and compare to origin signature to block tampering. *[claimed]*
- Throttled demo — Dev server artificially slows origin so a second tab loading the same level visibly loads instantly from the first. *[shown_working]*
- Metrics dashboard — Console interception extracts draw calls and triangles; React UI shows P2P megabits per second via a rAF-batched buffer. *[claimed]*

**Flow:** Run npm run dev and open localhost:3000 → Tab A loads a level slowly from throttled origin → Tab B loads the same level → Assets arrive from Tab A over WebRTC → Metrics panel shows P2P feed

**Prompt:** not public / not found
**Fit (implied):** Page lists Open Innovation and Gemini tracks; the project is a decentralized asset delivery layer, README says built for a decentralized game assets hackathon; no Gemini use described.  *(targeted: Open Innovation, Google Gemini (MLH), Second Prize)*
**AI:** none
**Architecture:** OpenLara compiled to WASM/WebGL; fetch wrapper or Service Worker asks a P2PManager; Node WebSocket signaling brokers WebRTC DataChannels; IndexedDB cache; React metrics UI.
**Novelty:** Applies CDN-style peer caching to a WASM game with no engine changes; repo mostly vendored OpenLara, so original code is small.
**Scope:** medium · working: README gives a two-tab test showing instant load from a peer; no video or measured savings. · polish: Clear README with security note; repo bloated by bundled engines (774 files).
**Claims:** Second tab loads a level instantly from the first (README) | Zero engine modification
**Gaps:** Devpost mentions Service Worker, BitTorrent, Rust and Three.js; README mentions fetch wrapper and WebRTC only; features follow README for mechanics; No quantitative bandwidth results; No video
Sources: https://devfolio.co/projects/gamestream-876b, evidence/nmit-hacks-nmit-hacks-2026-peer2play.json, https://nmithacks26.devfolio.co/

---

### Preflight-ai
*NMIT Hacks NMIT HACKS 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** First Prize (Render) [1st]

**What it is:** A GitHub Action plus FastAPI service that reviews npm dependency upgrades in pull requests before they run, combining install-script diffs, static code scanning and maintainer reputation with a Gemini summary to post a PASS, WARN or BLOCK verdict.
**Problem / user:** Signature-based scanners only flag packages after they are reported, leaving a window for hijacked npm releases; aimed at developers and CI pipelines.

**Features**
- Script diff stage — Compares package tarballs to flag new install lifecycle hooks. *[claimed]*
- AST scan — Acorn-based static analysis looks for risky pairings such as environment access with outbound requests. *[claimed]*
- Maintainer risk scoring — Uses npm metadata: inactivity, key rotation, provenance attestations. *[claimed]*
- Gemini synthesis — Gemini 2.0 Flash merges signals into a verdict and narrative; deterministic findings cannot be overridden by the model. *[claimed]*
- PR comment and merge block — Action parses lockfile, calls the API, comments on the PR and fails CI on BLOCK. *[shown_working]*
- Dashboard — Next.js dashboard lists scans, scan detail with reasoning and top-threat packages. *[shown_working]*
- Scan API — POST /analyze, GET /scans, /scans/{id}, /packages/top-threats stored in MongoDB. *[shown_working]*
- Ops controls — Sequential queue (3 packages per PR, 1 s delay) and a keep-alive ping to avoid Render cold starts. *[claimed]*

**Flow:** Developer opens PR changing dependencies → Action sends lockfile changes to API → Deterministic scanners gather signals → Gemini produces verdict → PR gets comment; BLOCK stops merge → Review scans on dashboard

**Prompt:** not public / not found
**Fit (explicit):** Devpost lists these tracks; Gemini synthesis, MongoDB storage and Render hosting of the API and dashboard.  *(targeted: Render First Prize, AI & ML, Blockchain/Cybersecurity, Google Gemini, MongoDB Atlas)*
**Sponsor tools:** Gemini API (Synthesising scanner signals into a verdict, core); MongoDB Atlas (Scan records, supporting); Render (Hosting the API and keep-alive, supporting)
**AI:** Deterministic parsers run first; Gemini 2.0 Flash only synthesises their output, with hard overrides so the LLM cannot suppress findings.
**Architecture:** GitHub Action posts lockfile changes to FastAPI /analyze; pipeline of script diff, AST scan, npm metadata and Gemini; results in MongoDB; Next.js dashboard reads them; verdict returned to Action.
**Novelty:** Defence-in-depth design keeps the LLM subordinate to rule findings; ships a separate test-target repo of blocked PRs.
**Scope:** medium · working: Live Vercel and Render URLs, API reference, and companion test-target repo with blocked PRs referenced. · polish: README with Mermaid diagrams, docs folder, demo folder, themed dashboard; no tests.
**Claims:** Most runs under 5 seconds within a 45 s CI budget | Dashboard 60fps with zero layout shifts | Catches account hijacks and env exfiltration
**Gaps:** No false-positive rate; Devpost says Node/Python backend, README says FastAPI; Companion test-target repo not read
Sources: https://devfolio.co/projects/preflightai-2fbe, evidence/nmit-hacks-nmit-hacks-2026-preflight-ai.json, https://nmithacks26.devfolio.co/

---

### PrivaSense
*NMIT Hacks NMIT HACKS 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Second Prize (Render) [2nd]

**What it is:** A web platform that monitors elderly users for early cognitive decline by analysing speech, motor and behaviour signals from home, with local Whisper transcription, a dynamic risk score, SHAP explanations and alerts to caregivers.
**Problem / user:** Early dementia signs go unnoticed and clinical tests are costly and infrequent; for older adults, caregivers and clinicians.

**Features**
- Speech analysis — Whisper transcribes locally and Librosa extracts audio features so sensitive audio stays off third-party AI. *[claimed]*
- Motor and behavioural assessment — Remote tests from home feed the drift analysis. *[claimed]*
- Dynamic risk score — Scores combine features over time to show cognitive drift. *[claimed]*
- SHAP explanations — Explainable AI shows what drove each score. *[claimed]*
- Caregiver alerts — Real-time alerts on sudden decline. *[claimed]*
- Multilingual support — Assessments available across languages. *[claimed]*

**Flow:** User completes remote speech/motor/behaviour assessment → Audio processed locally → Risk score and SHAP explanation produced → Caregivers alerted on sharp decline

**Prompt:** not public / not found
**Fit (explicit):** Devpost lists these tracks; MongoDB stores data and Render hosts, but Gemini use is not confirmed.  *(targeted: Render Second Prize, AI & ML, Google Gemini, MongoDB Atlas)*
**Sponsor tools:** MongoDB Atlas (Database, supporting); Render (Hosting backend and frontend, supporting)
**AI:** Local Whisper transcription, Librosa features, ML scoring with SHAP; no external AI services per page.
**Architecture:** React and Tailwind frontend (Vercel and Render), FastAPI async backend with Whisper, Librosa and SHAP, MongoDB Atlas storage.
**Novelty:** Privacy-first local audio processing paired with explainability for a health-screening idea.
**Scope:** small · working: Two deployed demo URLs listed; no repo, video or metrics. · polish: Deployment issues documented; accuracy not reported.
**Claims:** Keeps sensitive audio off external AI services
**Gaps:** No repo; Specific motor and behavior tests not described; Demo sites not opened; Gemini use unconfirmed
Sources: https://devfolio.co/projects/privasense-11a1, https://nmithacks26.devfolio.co/

---

### Resonator
*NMIT Hacks NMIT HACKS 2026 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** First Prize [1st]

**What it is:** A first-person psychological horror game made in Godot, set in a research facility gone wrong, where the player is a researcher exploring designed rooms; character dialogue and sound effects are generated with ElevenLabs.
**Problem / user:** No problem; aims to give players an absorbing escape through single-player horror.

**Features**
- First-person horror exploration — Player explores a failed research facility with handcrafted rooms and interactions. *[claimed]*
- Handcrafted story and mechanics — Original plot and mechanics designed by the three-person team. *[claimed]*
- ElevenLabs dialogue — Character conversations are generated voices. *[claimed]*
- ElevenLabs sound effects — Atmospheric effects and audio produced with the API. *[claimed]*
- Configurable keybinds — Input actions mapped to keys. *[claimed]*

**Flow:** Start as a researcher in the facility → Move through rooms and interact with objects → Hear generated character dialogue → Progress through the story

**Prompt:** not public / not found
**Fit (explicit):** Page lists these tracks; Godot game uses ElevenLabs for dialogue and effects.  *(targeted: Game Development track, ElevenLabs track, First Prize)*
**Sponsor tools:** ElevenLabs (Generated character dialogue and sound effects, core)
**AI:** Generative voice and sound via ElevenLabs; no other AI described.
**Architecture:** Godot project with Blender models and a Mixamo character; Python used for tooling; generated audio imported as assets.
**Novelty:** Game entry in a hackathon where most entries are apps; audio-first atmosphere from generated voices; team had no artist.
**Scope:** small · working: Devpost lists a promo video link and four images; repo unreadable. · polish: Promo video exists; challenges mention broken animation rig and missing keybinds.
**Gaps:** Repo README unreadable (clone and fetch failed); No build or level count; Video not watchable
Sources: https://devfolio.co/projects/resonator-c239, https://www.youtube.com/watch?v=srbZeDAlJCo (title only: Resonator Promo), https://nmithacks26.devfolio.co/

---

