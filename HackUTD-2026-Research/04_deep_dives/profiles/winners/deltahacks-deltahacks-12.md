# DeltaHacks — DeltaHacks 12 (3 projects)

### deltawash
*DeltaHacks DeltaHacks 12 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Second Place: Garmin Smartwatch [2nd]

**What it is:** Hand-hygiene compliance system: a Raspberry Pi camera runs a CNN plus LSTM ensemble to recognise WHO hand-washing steps, an ESP8266 lights LEDs per step, and a dashboard compares units.
**Problem / user:** Healthcare workers who often skip steps of the WHO hand-washing procedure, and hospitals wanting to verify compliance.

**Features**
- WHO step recognition — Pi camera frames go to a CNN and LSTM ensemble, running offline on the Pi, to identify the current step. *[claimed]*
- LED feedback — Pi tells an ESP8266 over WiFi to blink the detected step's LED and hold solid once the step lasted long enough. *[claimed]*
- Wash upload — After the wash, completed steps are posted to the website. *[claimed]*
- Compliance dashboard — deltawash.tech compares units and highlights commonly missed steps. *[claimed]*
- Deterministic demo replay — Repo has recorded sessions, a manifest and sample-inference mode to replay steps 2-7 without a sink. *[shown_working]*

**Flow:** Person starts washing at the sink → Camera feed reaches the Pi → Current step is detected and its LED blinks → LED turns solid when duration is met → Summary uploads to the dashboard

**Prompt:** DeltaHacks 12 second place (Garmin vivoactive 5); judged on social/industry impact, technical strength, originality and presentation. Also had Health Hack track, not claimed here.
**Fit (none):** No stated prize targeting; healthcare hygiene hardware plausibly fits a health track but the page only enters overall places.  *(targeted: Second Place: Garmin Smartwatch [2nd])*
**AI:** Ensemble of a CNN and an LSTM trained on labelled hand-washing videos, run locally on a Raspberry Pi; MediaPipe landmarks referenced in the demo README.
**Architecture:** Pi camera to Pi inference, WiFi to ESP8266 LEDs, session logs uploaded to a React/Tailwind dashboard; repo also has a CLI package, specs and tests.
**Novelty:** Edge hardware feedback loop with per-step timing gating, plus a spec-driven repo with replayable demo assets.
**Scope:** medium · working: About 19k lines with tests, Docker, dashboard and recorded fixtures; README read is only the demo-assets one; Devpost has video. · polish: Website at deltawash.tech, hardware folder and specs; no accuracy numbers.
**Claims:** About one third of doctors use the full WHO procedure (cited) | Offline processing on the Pi
**Gaps:** Evidence README is demos/README only; no root README feature list; No accuracy or latency measured; Screenshot count unknown
Sources: https://devpost.com/software/deltawash, https://github.com/Goldenstar2660/DeltaWash, evidence/deltahacks-deltahacks-12-deltawash.json, https://deltahacks-12.devpost.com/

---

### Quota
*DeltaHacks DeltaHacks 12 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** First Place: Bose Headphones [1st]

**What it is:** Cost-intelligence tooling for developers: a VS Code extension that flags expensive API calls in code with a heatmap and one-click cheaper fixes, plus a web sandbox for sketching architectures and forecasting their costs.
**Problem / user:** Developers and teams surprised by API, database and cloud bills that stay invisible until the invoice.

**Features**
- Cost heatmap in editor — Tree-sitter AST parsing and a token heuristic highlight costly calls like legacy GPT-4 usage as you type. *[shown_working]*
- Optimization suggestions — Proposes caching, batching or cheaper models/providers. *[claimed]*
- One-click fix — AST-based refactoring engine swaps in optimized models. *[claimed]*
- Bankruptcy Countdown — Projects runway and monthly burn at projected scale with budget alerts. *[claimed]*
- Architecture sandbox — Drag-and-drop React Flow canvas with built-in cost projection. *[shown_working]*
- AI Architect agent — Gemini with LangChain RAG over FAISS edits designs and generates graphs from descriptions. *[claimed]*
- CI/CD budget checks and cloud cost tracking — Block over-budget PRs and track AWS/GCP; future work. *[planned]*

**Flow:** Open code in VS Code with the extension → See highlighted expensive calls → Apply a one-click fix → Open web dashboard and design a system on the canvas → Ask the AI agent to optimize for cost

**Prompt:** DeltaHacks 12 first place (Bose QuietComfort headphones plus Vercel credits); judged on impact, technical strength, originality and presentation.
**Fit (none):** No stated prize targeting; a developer-cost tool entered for overall placement.  *(targeted: First Place: Bose Headphones [1st])*
**Sponsor tools:** MongoDB (database in dashboard stack, supporting); Gemini API (architecture reasoning and cost analysis, core)
**AI:** Gemini classifies and prices resource usage and edits architectures via LangChain, with FAISS RAG over pricing context.
**Architecture:** TypeScript VS Code extension with tree-sitter parser; Next.js and React Flow dashboard over a FastAPI backend with MongoDB and FAISS.
**Novelty:** Treats cost as a lint rule inside the editor and pairs it with a pre-code architecture cost simulator.
**Scope:** large · working: About 12k lines, two apps, Docker and tests, two live sites and demo video. · polish: Logo, live deployments, README with quick start; two screenshot captions.
**Claims:** Team used Quota to optimize Quota's own cost | No quantitative savings reported
**Gaps:** Pricing data source not stated; README workflow image sections have no text; Screenshot count unknown
Sources: https://devpost.com/software/quota-fg4pzi, https://github.com/dwseoh/Quota, evidence/deltahacks-deltahacks-12-quota.json, https://deltahacks-12.devpost.com/

---

### ReelJobs
*DeltaHacks DeltaHacks 12 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Third Place: Corsair Keyboard [3rd]

**What it is:** Mobile app that turns job listings into 15-30 second vertical videos with AI scripts and voices, with semantic job search and automated Greenhouse application filling.
**Problem / user:** Job seekers, especially Gen Z, tired of walls of text and repeated form filling.

**Features**
- Swipe video feed — Expo React Native vertical feed with HLS streaming, prefetching and seen-job tracking. *[shown_working]*
- Video generation pipeline — LLM script with dialogue, Fish.audio speech, FFmpeg captions, HLS transcode served via CDN. *[shown_working]*
- Semantic search — Gemini embeddings and MongoDB Atlas vector search over natural-language queries. *[claimed]*
- Greenhouse scraping — Playwright service collects job boards. *[claimed]*
- One-tap apply — Playwright fills application forms with AI answers tailored to each job. *[claimed]*
- Microservices — Three FastAPI services for auth, jobs and video with Docker Compose. *[shown_working]*
- Personalized recommendations and LinkedIn — Learning from swipes and more boards; future. *[planned]*

**Flow:** Open app to vertical feed → Swipe through job videos → Search in plain language → Tap apply → AI fills the Greenhouse form

**Prompt:** DeltaHacks 12 third place (Corsair K70 plus Vercel credits); judged on impact, technical strength, originality and presentation.
**Fit (none):** No stated prize targeting; entered in overall places.  *(targeted: Third Place: Corsair Keyboard [3rd])*
**Sponsor tools:** Gemini API (embeddings, search and application assistance, core); MongoDB Atlas (vector search store, core); Vultr (VM and object storage per tags, supporting)
**AI:** Gemini embeddings and generation for search and answers; LLM writes video scripts, Fish.audio does emotional TTS; Whisper tagged but role unclear.
**Architecture:** Expo app streams HLS from CDN; three FastAPI services plus Playwright service use MongoDB Atlas; FFmpeg pipeline caches scripts, audio and timestamps.
**Novelty:** Full TikTok-style content pipeline generating videos per job, joined to automated applying.
**Scope:** large · working: About 16k lines, Docker, CI and tests; README documents architecture; screenshots on Devpost. · polish: Production-style deployment claims; no demo video link on Devpost.
**Claims:** Sub-second video starts via HLS and CDN | Production-ready architecture
**Gaps:** README text cut before setup; Hosting provider unclear: DigitalOcean in text, Vultr in tags; Presenters appear to use celebrity-like characters per screenshots; No latency measurement
Sources: https://devpost.com/software/reeljobs, https://github.com/Scr4tch587/DeltaHacks12, evidence/deltahacks-deltahacks-12-reeljobs.json, https://deltahacks-12.devpost.com/

---

