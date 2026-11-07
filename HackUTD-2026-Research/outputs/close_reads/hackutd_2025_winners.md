# Q19 close read: HackUTD 2025 winners, compared with the 2025 non-winner baseline

Scope: every HackUTD 2025 winner in the dataset (37 records, 36 unique projects; the two ProDuh! listings share one Devpost page and are counted once). Compared against the 2025 non-winner baseline: `demo_ready` (50, the fair comparison) and `random` (50, the typical entry), kept separate throughout. This is the only event where winners can be compared with non-winners. Every difference below is an **association, not a cause**.

Sources read: the winner profiles (`04_deep_dives/profiles/winners/hackutd-hackutd-2025.md`, all of it); the baseline profiles (all 50 `demo_ready` in full, the 50 `random` skimmed); the matching rows in `deepdive_all.jsonl`, `01_winners/.../project_records.jsonl` and `02_baseline_non_winners/.../project_records.jsonl`; `prompts_cache/hackutd-2025.md`; `06_hackutd_2026_sponsors/t-mobile.md`; and the taglines and gallery counts in `data/pages/page_facts.jsonl`. I could not open Devpost pages myself (WebFetch got HTTP 403).

Where the numbers come from. Every count comes from `scripts/q19_hackutd2025_group_counts.py`, which writes:
- `data/tables/Q19_hackutd2025_group_counts.csv`: n of N per group per metric, with the names behind each count, plus a depth-A-only sensitivity view.
- `data/tables/Q19_hackutd2025_per_project.csv`
- `data/tables/Q19_hackutd2025_track_targeting.csv`
- `data/tables/Q19_hackutd2025_domain_track_prompt_fit.csv`
- `data/tables/Q19_hackutd2025_award_integration_counts.csv` and `data/tables/Q19_hackutd2025_named_user_counts.csv`. These two count my own close-read judgments, which are stored in `data/tagged/close_reads/`.

Labels used below:
- **Worked / claimed / planned** are the deep-dive `working_status` counts per feature. `shown_working` means a screenshot, video or README shows that feature working.
- **Integration depth for the won track**:
  - `core`: the sponsor's tech carries the demo.
  - `supporting`: the sponsor's tech is used but could be removed.
  - `problem-only`: the project solves the sponsor's stated business problem with no sponsor product.
  - `token` / `none visible`: a mention only, or no visible use.
- **Centerpiece visibility** uses the spec enum: `in_demo_output` / `shown_via_diagram_or_logs` / `described_only`.
- **Inference** is labeled. Placement within a track is not on Devpost. Some READMEs claim a placement themselves (marked "self-reported").

---

## 1. Per-winner notes (grouped by track won)

### General Track (3 winners)

**NLB (Nothing Left Behind)**: https://devpost.com/software/tbd-app
- Tracks: General Track.
- What / for whom: a native iOS app for roommates and families: a shared shopping list that sends a geofenced "you're near a store" alert, plus receipt scanning and bill splitting.
- Centerpiece: Apple Vision OCR, then Gemini to structure receipt items, plus CoreLocation geofencing. Visibility: `in_demo_output` (10–11 gallery screenshots, one per screen).
- Worked / claimed / planned: 5 / 0 / 0. All five features are shown working.
- Sponsor depth: n/a (Gemini supporting).
- Assets: no video per the first-pass record; 11 gallery items; README empty.
- Evidence: A / high. Small scope (~2.5k Swift lines, team of 2).
- Inference: the most completely evidenced consumer app in the set. The everyday problem is easy to grasp, with no sponsor framing.

**ProdigyPM**: https://devpost.com/software/prodigypm-kaqe09
- Tracks: General Track.
- What / for whom: product managers upload a PDF, or build a PRD with a chat agent, and get department subprojects that are pushed to Jira, plus a live dashboard.
- Centerpiece: three GPT-4 Turbo agents (PDF, decomposition, PRD consultant) and a Jira Cloud push. Visibility: `described_only` (4 gallery images; no repo, video or live link).
- Worked / claimed / planned: 0 / 5 / 0.
- Sponsor depth: n/a.
- Assets: no video, no repo. Long writeup with a real debugging narrative.
- Evidence: B / medium.
- Gap: the visible evidence is thin for a General winner. Its win is not explained by the available evidence.

**Working Memory**: https://devpost.com/software/working-memory
- Tracks: General Track (README self-reports "1st place grand prize").
- What / for whom: student and hobbyist developers juggling several projects. A VS Code extension (MCP) logs the files changed in a session, an LLM writes a summary of the session, and past sessions are searchable.
- Centerpiece: MCP server inside a VS Code extension, GitPython changelog, then a GPT-4.1-mini summary and embedding search. Visibility: `in_demo_output` per the deep dive (5 features shown working).
- Worked / claimed / planned: 5 / 1 / 0.
- Sponsor depth: n/a.
- Assets: the records conflict on video (first-pass URL true, profile says no video); live site workingmemory.vip; 1 gallery item; README with architecture.
- Evidence: A / high. Repo has tests; ~1.5k LOC excluding dependencies.
- Inference: a small build with a crisp, relatable pain ("lose the reasoning behind your work") and a working loop.

### T-Mobile (3 winners)

**InsighT**: https://devpost.com/software/t-insights
- Tracks: T-Mobile.
- What / for whom: T-Mobile product managers. It scrapes Reddit, news and DownDetector into a Customer Happiness Index (CHI) by product area, with a heatmap and outage markers, and Gemini writes prioritized opportunities and PRDs.
- Centerpiece: a multi-source scraper pipeline (cron) with sentiment, topic detection and dedup, then Gemini opportunities. Visibility: `in_demo_output` (5 of 6 features shown working).
- Worked / claimed / planned: 5 / 1 / 0.
- Sponsor depth: problem-only (no T-Mobile tech exists to integrate).
- Assets: video; live site insight-tmobile.us; 16 gallery items; detailed README.
- Evidence: A / high. ~20k LOC.
- Inference: the most fully evidenced T-Mobile entry, winner or not. It goes one step past the dashboard, to generated PRDs.

**Beacon**: https://devpost.com/software/na-504rkg
- Tracks: T-Mobile.
- What / for whom: a real-time 0–100 happiness index for T-Mobile call agents and PR teams. It fuses live call transcripts (Twilio), social posts and outage data, with role dashboards.
- Centerpiece: a live call pipeline: Twilio, then Presidio PII scrub, then Llama on Groq classification. Visibility: `in_demo_output` for the map and dashboards; the call pipeline is `described_only`.
- Worked / claimed / planned: 3 / 3 / 0.
- Sponsor depth: problem-only (uses the T-Mobile mascot and T-Mobile Tuesday offers in the UI).
- Assets: video; 6 gallery items; README is the default template.
- Evidence: A / high.
- Inference: privacy-first live data and branded role-specific views set it apart from the static-JSON T-Mobile dashboards.

**HarmoniQ**: https://devpost.com/software/x-yiqm81
- Tracks: T-Mobile, Best Use of Auth0.
- What / for whom: telecom product managers and network engineers. It joins network metrics with Reddit/X sentiment, adds outage-risk classifiers, and has a Gemini assistant.
- Centerpiece: scikit-learn Random Forest / gradient boosting outage models trained offline (Kaggle plus synthetic outages). Visibility: `described_only` for the models; the dashboard modules are shown.
- Worked / claimed / planned: 2 / 4 / 1 (Slack/Jira automation planned).
- Sponsor depth: T-Mobile problem-only; Auth0 supporting (login only).
- Assets: records conflict on video; 7 gallery items; README thin.
- Evidence: A / medium. Outage data partly synthetic.
- Full gap analysis is in `calibration_tmobile_2025.md`.

### PNC Bank (3 winners; PM-copilot theme)

**AutoPM**: https://devpost.com/software/autopm-2tjzu8
- Tracks: PNC Bank (README self-reports 2nd).
- What / for whom: product managers. Eight LangGraph agents on Gemini cover ideas, stories, market research, RICE, OKR mapping, wireframes, email and Jira.
- Centerpiece: multi-agent shared state with Zod-validated outputs and real Jira and Gmail side effects. Visibility: `in_demo_output` (screenshots of live Jira tickets).
- Worked / claimed / planned: 1 / 7 / 0.
- Sponsor depth: problem-only (no PNC link explained on the page).
- Assets: video; 5 gallery items; detailed README; ~15k LOC.
- Evidence: A / high.

**ProdPlex**: https://devpost.com/software/prodify-94vbpk
- Tracks: PNC Bank.
- What / for whom: product managers. Seven Nemotron specialist agents (strategy through GTM), plus a regulation agent framed as the PNC piece, produce a PRD.
- Centerpiece: LangGraph task graph with FAISS shared memory across agents. Visibility: `shown_via_diagram_or_logs` (architecture diagram).
- Worked / claimed / planned: 0 / 5 / 0, plus 1 unclear (Figma/Jira integrations are mocks per the README).
- Sponsor depth: problem-only.
- Assets: video; 4 gallery items; detailed README with diagram.
- Evidence: A / high.
- Inference: the bank-specific regulation agent is the visible tie to the sponsor.

**ProDuh!**: https://devpost.com/software/produh (listed twice in the data, counted once)
- Tracks: PNC Bank.
- What / for whom: product managers. A multi-agent "command center" turns notes and KPIs into Jira/ADO-ready stories, links Confluence pages, and runs an operate loop over mock analytics.
- Centerpiece: Gemini (Vertex) agents with human-in-the-loop, capped at three loops. Visibility: `described_only`.
- Worked / claimed / planned: 0 / 6 / 0. Most adapters are described as designed, not built.
- Sponsor depth: problem-only.
- Assets: records conflict on video; 9 gallery items; long structured README with roadmap and FAQ.
- Evidence: A / high.

### Northmark Compute & Cloud (NMC2) (3 winners; data-center technician challenge)

**DCDaddy**: https://devpost.com/software/fun-dashboard
- Tracks: Northmark.
- What / for whom: data-center technicians and admins. Email and Slack messages become tickets, which are bundled; technicians get multi-floor routing with health-aware warnings, inventory forecasts, a Gemini device assistant and a 3D rack viewer.
- Centerpiece: multi-floor Dijkstra routing with elevator penalties and hot/cold lanes, plus a ticket-bundling heuristic. Visibility: `in_demo_output`.
- Worked / claimed / planned: 3 / 4 / 0.
- Sponsor depth: problem-only. The README says it covers all five challenge areas (explicit fit).
- Assets: video; live site dcdaddy.us; 6 gallery items; detailed README.
- Evidence: A / high.

**DataDriver**: https://devpost.com/software/datadriver
- Tracks: Northmark and Nvidia.
- What / for whom: data-center technicians. A Nemotron ReAct agent turns a work order into steps, runs the automatable tool steps, escalates physical work to a technician, and replans when an issue is reported.
- Centerpiece: the agent decides between running a step itself and escalating it to a human. Visibility: `in_demo_output` for plan generation only (1 screenshot); execution and escalation are `described_only`.
- Worked / claimed / planned: 1 / 5 / 0.
- Sponsor depth: Northmark problem-only; Nvidia core (Nemotron nano 9B).
- Assets: no video per the first-pass record; 2 gallery items; detailed README; ~19k LOC.
- Evidence: A / high.
- Inference: a two-track stack (domain problem plus Nvidia) from one build in which Nemotron is the agent brain.

**TaskFlow**: https://devpost.com/software/d-68uye4
- Tracks: Northmark.
- What / for whom: a coordination suite for data-center engineers and on-site technicians: a technician web app (tickets, checklist, path), an engineer location/progress dashboard, and an iOS AR remote pointer placed on a server.
- Centerpiece: a SwiftUI/RealityKit AR remote pointer. Visibility: `in_demo_output` (3 features shown working).
- Worked / claimed / planned: 3 / 2 / 0.
- Sponsor depth: problem-only. No AI.
- Assets: video; 11 gallery items; web README is the unmodified Supabase starter.
- Evidence: A / medium.

### Nvidia (3 winners; DataDriver and Toyotron also listed under their domain tracks)

**Alchemetrics**: https://devpost.com/software/abc-xapnio
- Tracks: Nvidia.
- What / for whom: operators of the EOG potion-factory scenario. A Nemotron planner routes work to specialist agents (drain detection, ticket matching, auditing, overflow forecasting, OR-Tools routing) and logs its reasoning.
- Centerpiece: an explainable planner-trace multi-agent design over algorithmic agents. Visibility: `in_demo_output` for the dashboard and reasoning traces.
- Worked / claimed / planned: 1 / 6 / 0.
- Sponsor depth: Nvidia core.
- Assets: video; 2 gallery items; solid README; tests; ~5k LOC.
- Evidence: A / high.
- Inference: the same EOG dataset many non-winners used, re-aimed at the Nvidia agent track. It did not win EOG.

### Toyota Financial Services (3 winners)

**Toyotron**: https://devpost.com/software/toyotron
- Tracks: Toyota Financial Services and Nvidia (README self-reports "2x first place").
- What / for whom: Toyota car shoppers. A five-step quiz feeds recommendations; then come chat or a Retell phone call, trade-in estimate, test-drive booking (Google Calendar) and confirmation emails.
- Centerpiece: a four-agent Nemotron-super-49B orchestration (intent, vehicle, finance, report) with tool calls. Visibility: `in_demo_output` (4 of 6 features shown working) plus an architecture diagram.
- Worked / claimed / planned: 4 / 2 / 0.
- Sponsor depth: TFS problem-only; Nvidia core.
- Assets: live Vercel demo; 8 gallery items including the confirmation emails and a diagram; records conflict on video.
- Evidence: A / high. ~19k LOC.

**Hingine**: https://devpost.com/software/hingine
- Tracks: Toyota Financial Services.
- What / for whom: college students with thin credit. A Tinder-style swipe deck of Toyotas, finance micro-lessons with quizzes, and points that unlock financing perks.
- Centerpiece: none beyond the UI. A gamified education-to-incentive loop on Expo, no backend, no AI. Visibility: `in_demo_output` (swipe and lessons shown).
- Worked / claimed / planned: 2 / 3 / 1 (TFS API hookup planned).
- Sponsor depth: problem-only.
- Assets: 7 gallery items; records conflict on video; clear README.
- Evidence: A / high.
- Inference: a named user group plus a finance-literacy angle (TFS's business), not a generic car finder.

**Kachow**: https://devpost.com/software/car-thing-1dsxyk
- Tracks: Toyota Financial Services.
- What / for whom: car buyers (generic). A chatbot shows insurance, gas, maintenance and APR figures and advises using mock bank data.
- Centerpiece: a chat agent over car-cost data; the model is unclear (OpenAI vs Nemotron). Visibility: `described_only`.
- Worked / claimed / planned: 0 / 5 / 0.
- Sponsor depth: problem-only.
- Assets: video; live site kachow.biz; 5 gallery items; cites "46% buyer's remorse".
- Evidence: A / medium.
- Its win over stronger-looking TFS non-winners is not explained by the available evidence.

### State Farm (3 winners; API-versioning theme)

**qAPIbara**: https://devpost.com/software/in-progress-2awbie
- Tracks: State Farm (README self-reports 2nd).
- What / for whom: QA, DevOps and backend developers. It diffs two API versions, Nemotron generates and runs test cases, and Gemini explains regressions.
- Centerpiece: a deterministic diff engine that ignores noise, plus LLM test generation. Visibility: `in_demo_output` for the diff; the rest is claimed.
- Worked / claimed / planned: 1 / 5 / 0.
- Sponsor depth: problem-only. The README labels "Layer 0" as the State Farm core requirement (explicit fit).
- Assets: 4 gallery items; detailed README; unmeasured "80% faster" claim. Built by a team of 1.
- Evidence: A / high.

**MirrorAPI**: https://devpost.com/software/mirror-api
- Tracks: State Farm.
- What / for whom: developers maintaining API-dependent code. It fetches two endpoints, diffs the JSON field by field, gives a migration risk score, and a Nemotron RAG agent writes a report.
- Centerpiece: a deterministic diff (no AI) with an LLM narrative. Visibility: `in_demo_output` (diff table shown).
- Worked / claimed / planned: 2 / 4 / 0.
- Sponsor depth: problem-only. The page mentions gathering State Farm feedback.
- Assets: video; 5 gallery items; solid README.
- Evidence: A / high.

**UpGuardian**: https://devpost.com/software/upguard
- Tracks: State Farm.
- What / for whom: app developers upgrading API versions. A deterministic diff, Nemotron interpretation, and a Flutter dashboard.
- Centerpiece: the deterministic diff with a token-safe proxy. Visibility: `in_demo_output` for the dashboard only.
- Worked / claimed / planned: 1 / 4 / 0.
- Sponsor depth: problem-only.
- Assets: 4 gallery items; README nearly empty; tests.
- Evidence: A / medium.
- Inference: all three State Farm winners built the same "two API versions in, diff out" tool, which suggests a narrow, literal prompt.

### Goldman Sachs (3 winners; vendor/client onboarding theme)

**TrustIssues.AI**: https://devpost.com/software/coffee-overflow
- Tracks: Goldman Sachs.
- What / for whom: compliance teams. Four Nemotron agents extract a vendor PDF, screen it against mock sanctions and registries, compute a rules-based risk score (deliberately not by the LLM), explain it, and wait for human approval.
- Centerpiece: the agent split with a deterministic scorer and a JSON audit trail of agent thoughts. Visibility: `in_demo_output` (approval and audit shown) plus an architecture diagram.
- Worked / claimed / planned: 2 / 4 / 0.
- Sponsor depth: problem-only.
- Assets: video; 9 gallery items; detailed README.
- Evidence: A / high. Mock APIs only.

**AutoBoard**: https://devpost.com/software/404-not-found-us43mg
- Tracks: Goldman Sachs.
- What / for whom: compliance teams onboarding financial vendors. Textract extraction of W-9s and insurance certificates, an 18-field questionnaire, risk scoring, and one-click approval.
- Centerpiece: a full IaC serverless build (seven Lambdas, RDS in a VPC). Visibility: `shown_via_diagram_or_logs` (system design diagrams).
- Worked / claimed / planned: 0 / 5 / 0.
- Sponsor depth: problem-only. Names Goldman Sachs; explicit fit.
- Assets: video per the first-pass URL (the profile says no demo or video, a conflict); 7 gallery items; ~17k LOC.
- Evidence: A / high.

**Stamped**: https://devpost.com/software/stamped-6hnl4w
- Tracks: Goldman Sachs.
- What / for whom: bank staff, clients and vendors. A multi-role onboarding platform from lead to onboarded client.
- Centerpiece: none visible beyond the multi-role UI. The "AI features" are unspecified. Visibility: `in_demo_output` for the pipeline and login screens.
- Worked / claimed / planned: 2 / 3 / 0, plus 1 unclear.
- Sponsor depth: problem-only.
- Assets: live Netlify site; YouTube video per the profile; 7 gallery items; no repo.
- Evidence: B / medium.

### CBRE (3 winners)

**TrustEstate AI**: https://devpost.com/software/cbre-project
- Tracks: CBRE.
- What / for whom: home buyers and renters (generic). Map-based browsing where Gemini, using Google Search grounding, fact-checks listing data and assigns a trust score with a verification log.
- Centerpiece: AI as a verifier of listing data, not a recommender. Visibility: `described_only` for the fact-check; map, compare and analytics are shown.
- Worked / claimed / planned: 2 / 3 / 0.
- Sponsor depth: problem-only (CBRE-style mock data).
- Assets: video; 8 gallery items; no repo.
- Evidence: B / medium.

**Cura**: https://devpost.com/software/tbd-58ftpr
- Tracks: CBRE.
- What / for whom: commercial real estate beginners and investors. CrewAI agents on local Llama produce forecasts, pros/cons, comparisons and sentiment.
- Centerpiece: local open-weight agent crews and an "adaptive layout engine". Visibility: `described_only`.
- Worked / claimed / planned: 0 / 5 / 0, plus 1 unclear.
- Sponsor depth: problem-only. The README says it was built for the CBRE challenge.
- Assets: no video or demo; 2 gallery items; cites "21% of agents handle commercial".
- Evidence: A / medium.
- Its win is not explained by the available evidence.

**Pact**: https://devpost.com/software/autotract
- Tracks: CBRE and Best Use of Solana.
- What / for whom: vendors and clients negotiating B2B contracts. AI-assisted drafting, multi-party approval, Solana escrow and hash anchoring, documents on IPFS.
- Centerpiece: three Rust Anchor programs (PDAs, cross-program invocations) for escrow and reputation. Visibility: `described_only`; dashboard shown.
- Worked / claimed / planned: 1 / 5 / 0. The writeup also lists escrow and reputation as future phases, so built vs planned is unclear.
- Sponsor depth: CBRE problem-only (the real-estate link is not stated); Solana core.
- Assets: 5 gallery items; repo not readable.
- Evidence: B / medium.

### EOG Resources (2 winners; "potion cauldron" reconciliation dataset)

**Enchantress**: https://devpost.com/software/enchantress-w2li90
- Tracks: EOG Resources.
- What / for whom: an animated fantasy map of 12 cauldrons with per-cauldron weekly time series and flags where tickets disagree with drains.
- Centerpiece: ticket-vs-drain matching done client-side. Visibility: map and time series `in_demo_output`; matching `described_only`.
- Worked / claimed / planned: 2 / 2 / 1. Overflow forecasting is planned, and the page contradicts itself on it.
- Sponsor depth: sponsor data (the challenge dataset). No AI.
- Assets: video; 3 gallery items; README template.
- Evidence: A / medium. Small (~3.7k lines).

**PoyoLabs**: https://devpost.com/software/poyolabs-47n0fz
- Tracks: EOG Resources.
- What / for whom: a hand-drawn pixel-art game dashboard over the cauldron data, with a route map, playback and a Nemotron chatbot.
- Centerpiece: custom pixel art and animation. Visibility: `in_demo_output` for the art and overview.
- Worked / claimed / planned: 2 / 4 / 0.
- Sponsor depth: sponsor data (handling unspecified).
- Assets: live site poyolabs.us; 5 gallery items; no repo or video.
- Evidence: B / medium.
- Inference: both EOG winners lead with a distinctive visual theme. Several more complete EOG non-winners did not (see section 2).

### Capital One (1 winner) and Best Design

**SpendingWithSpendy**: https://devpost.com/software/spendingwithspendy
- Tracks: Capital One and Best Design.
- What / for whom: young kids and their parents. A physical NFC "Spendy card" authorizes in-game currency purchases; each dollar appears as a "spendy" mascot, and parents review and reload.
- Centerpiece: NFC card tap authentication in an Expo app. Visibility: `in_demo_output` (all 4 features shown working).
- Worked / claimed / planned: 4 / 0 / 0.
- Sponsor depth: Capital One problem-only. No AI.
- Assets: 6 gallery items; Figma file and slide deck; records conflict on video; short writeup.
- Evidence: A / high. Very small (~1.6k LOC).
- Inference: a physical object, a vivid user and polished design took two prizes with no AI.

### Side tracks: Best Startup, Best Hardware, Best Beginner

**PoyoPop** (Best Startup): https://devpost.com/software/poyopop
- What / for whom: small food pop-up vendors and the people looking for them. A map and list, "going" and "saved", vendor event creation and analytics; visit counts replace ratings.
- Centerpiece: none technical. A Figma Make generated prototype on mock data. Visibility: `in_demo_output` (5 features shown working).
- Worked / claimed / planned: 5 / 2 / 0.
- Assets: video; Figma prototype link; 11 gallery items; launch and growth plan in the writeup.
- Evidence: A / medium.

**VisionScout** (Best Hardware): https://devpost.com/software/coolproject69
- What / for whom: home and car buyers. Event-provided smart glasses record a car or property, a locally trained YOLO model detects damage and builds a scored listing, and a Gemini LangGraph agent matches buyer requests.
- Centerpiece: the custom YOLO model, plus a patched glasses SDK and recalibrated antennas. Visibility: recommender and browse UI `in_demo_output`; detection `described_only`.
- Worked / claimed / planned: 2 / 3 / 0.
- Assets: video; 6 gallery items; tests.
- Evidence: A / high.

**WiSPR** (Best Beginner): https://devpost.com/software/wispr-wireless-safety-pulse-relay
- What / for whom: technicians in loud, hazardous workplaces. Arduino badges with a DHT11 sensor that vibrate on heat or humidity and send silent short/long-press signals to each other.
- Centerpiece: badge-to-badge serial signaling. Visibility: `in_demo_output` (4 of 4 shown working); the dashboard uses simulated data.
- Assets: prototype video per the profile; 3 gallery items; AutoCAD and Figma.
- Evidence: A / medium.

### MLH / API prizes

**Kori** (Best Use of Gemini API): https://devpost.com/software/kori
- What / for whom: students and remote workers. A pixel-cat desk companion on a Pi 5 in a 3D-printed case; it senses sound, air and mood and rewards focus.
- Centerpiece: three coordinated runtimes (Pi Express server, Electron UI, React Native app) plus sensors. Visibility: `in_demo_output` (3 shown working).
- Sponsor depth: Gemini supporting (insights in the app).
- Assets: live site kori.study; YouTube video; 4 gallery items.
- Evidence: A / high.

**HealthSense** (Best Use of Vultr): https://devpost.com/software/healthsense-0qxrs4
- What / for whom: data-center workers. A wearable: Arduino sensors feed a Pi, which writes to Redis on Vultr; a Nemotron agent judges risk and triggers a vibration alert.
- Centerpiece: the hardware-to-cloud-to-agent-to-haptic loop. Visibility: `in_demo_output` (4 shown working, including the hardware photo) plus a flow diagram.
- Sponsor depth: Vultr supporting (hosting).
- Assets: 4 gallery items; no video.
- Evidence: A / medium.

**Relay** (Best Use of ElevenLabs): https://devpost.com/software/tbd-v8pqbk
- What / for whom: data-center technicians. A LangGraph agent turns a plain-language request into read-only SSH verification checks, plus a Jira chat and an AprilTag AR overlay.
- Centerpiece: a guarded YAML catalog of allowed SSH actions. Visibility: `described_only`; the Devpost narrative is blank.
- Worked / claimed / planned: 0 / 5 / 0.
- Sponsor depth: **none visible**. No ElevenLabs use was found in any source.
- Evidence: A / medium.

**bevinAI** (Best Use of DigitalOcean Gradient AI): https://devpost.com/software/bevinai
- What / for whom: enterprise PM and dev teams (PNC framing). From a one-line idea it produces market research, a stack choice, a Jira board, PR checks against requirements, and Solana audit hashes.
- Centerpiece: Nemotron-70B via NIM behind a FastAPI MCP server with prompt chaining. Visibility: `described_only` (video embedded, no repo).
- Worked / claimed / planned: 0 / 7 / 0.
- Sponsor depth: **none visible** (the page never mentions DigitalOcean).
- Evidence: B / medium.

**hyperlynx** (Best Domain Name, GoDaddy Registry): https://devpost.com/software/hyperlynx
- What / for whom: a Jira-based work-order layer for data-center technicians, with AI context (method unexplained) and Auth0.
- Visibility: `described_only`.
- Sponsor depth: token (registered hyperlynx.us).
- Assets: live site; 5 gallery items; README empty.
- Evidence: B / low.

(HarmoniQ / Auth0 and Pact / Solana are covered above.)

---

## 2. Winners vs demo_ready non-winners (HackUTD 2025)

### 2a. Same-track pairs: one sentence on the visible difference

Non-winner track targeting is inferred from page content (`Q19_hackutd2025_track_targeting.csv`). Pairs were chosen as the closest look-alike in the same track.

1. **InsighT (W) vs Read the Room (DR), T-Mobile.** Both are large multi-source sentiment pipelines (~20k LOC each). InsighT shows 5 of 6 features working, with a live site, video and 16 images, and goes on to generated PRDs. Read the Room has no demo link or video, five unlabeled screenshots, and unmeasured accuracy claims (85–95%).
2. **Beacon (W) vs T-Pulse (DR), T-Mobile.** Both stream a regional happiness index to a live map. Beacon ingests real phone calls (Twilio) with PII scrubbing and three role dashboards shown working. T-Pulse streams AI-generated synthetic reviews and has no video.
3. **HarmoniQ (W) vs MagentaMonitor (DR), T-Mobile.** Both join network quality with sentiment. HarmoniQ has trained outage classifiers, a Gemini assistant and 7 images. MagentaMonitor runs a hand-written JS regression over static JSON, and its repo was unreadable.
4. **InsighT (W) vs SentimentRadar (DR), T-Mobile.** Same heatmap-plus-agent idea. SentimentRadar's README admits the Nemotron diagnostic agent is "simulated with rule-based logic", and it shows one screenshot.
5. **Toyotron (W) vs AutoMatch (DR), TFS.** Both span recommendation, finance, trade-in and an AI phone call to book a test drive. Toyotron shows four flows working on a live Vercel deploy. AutoMatch lists every feature as claimed, with no demo or video link.
6. **Hingine (W) vs Toyota Path Finder (DR), TFS.** Both use a Tinder-style swipe deck. Hingine adds finance micro-lessons that unlock financing perks for a named user (college students), with 7 images. Path Finder has a one-line README and no demo.
7. **Kachow (W) vs RideOracle (DR), TFS.** Both are car-cost chatbots with a finance calculator, and neither shows a feature working. Kachow has a live site, a video and a cited statistic (46% buyer's remorse). The difference beyond those assets is not explained by the available evidence.
8. **Enchantress (W) vs Snitch the Witch (DR), EOG.** Snitch the Witch has a live demo, video, 7 captioned screenshots, forecasting and OR-Tools routing. Enchantress is a small no-AI map whose forecasting is only planned. **Counterexample:** the completeness gap runs the "wrong" way, and this is not explained by the available evidence.
9. **PoyoLabs (W) vs Witch Delivery Associates (DR), EOG.** WDA shows seven working tabs with a video. PoyoLabs shows less (no repo or video) but has hand-drawn pixel art and a live site. Inference: a distinctive visual identity was the visible differentiator.
10. **AutoPM (W) vs PrisM (DR), PNC.** Both are multi-agent PM tools that create Jira tickets. AutoPM's screenshots show real Jira tickets and Gmail being created, plus a video. PrisM shows its agent graph working, but Jira creation is only claimed and there is no video.
11. **ProdPlex (W) vs PMGenie (DR), PNC.** Both are Nemotron PM copilots with detailed READMEs and video. ProdPlex has an explicit bank-regulation agent tied to PNC, while PMGenie's tie is to the PM prototyping phase. Inference: the sponsor-specific piece is the visible difference.
12. **DCDaddy (W) vs KanbanSync (DR), Northmark.** DCDaddy says it covers all five challenge areas, with a live site and three algorithms shown working. KanbanSync's page says the team pivoted after misunderstanding the prompt, and it has no demo.
13. **DataDriver (W) vs Kramhtron.ai (DR), Northmark / Nvidia.** Kramhtron is arguably more ambitious (vision on a physical camera, an ElevenLabs voice agent, a coordinator) with 7 screenshots. DataDriver shows only plan generation. The visible difference is DataDriver's tight "execute or escalate" framing of the technician job (inference). It is otherwise not explained by the available evidence.
14. **TaskFlow (W) vs PulseLink (DR), Northmark.** Both are native multi-device technician apps with several features shown working (TaskFlow: AR remote pointer; PulseLink: five Apple platforms including Vision Pro). The difference is not explained by the available evidence. TaskFlow's AR pointer addresses the engineer-to-technician handoff named in the challenge (inference).
15. **TrustEstate AI (W) vs CBRE Intelligence Hub (DR), CBRE.** TrustEstate has a video, 8 images and a single sharp angle (AI as a fact-checker of listings). The Hub has a boilerplate README, no video and a generic "advisor chat plus value model".
16. **Relay (W) vs Kramhtron.ai (DR), ElevenLabs.** Kramhtron makes ElevenLabs a core voice agent. Relay shows no ElevenLabs use at all. Not explained by the available evidence; possibly a prize-mapping error (see section 3).
17. **NLB (W) vs ShelfSense (DR), General.** Both are consumer apps doing receipt OCR followed by LLM structuring. NLB shows all 5 features working in 11 screenshots of a native iOS app. ShelfSense's frontend is marked "in progress".
18. **Working Memory (W) vs Cursor on the Go! (DR), General.** Both are developer tools with a VS Code extension, and both show several features working. Working Memory adds semantic search and tests, and frames a common pain ("lose the reasoning behind your work"). Cursor on the Go! is a self-described joke-ARR hack with a security disclaimer. Inference: the seriousness of the problem framing differed.
19. **VisionScout (W) vs WitchWatch (DR), Best Hardware.** Both are real hardware builds with video. VisionScout trained its own YOLO model on event-provided glasses and claims an end-to-end flow. WitchWatch's README is empty and its ML is unnamed.
20. **SpendingWithSpendy (W) vs PF Tracker (DR), finance consumer.** PF Tracker is a conventional, well-documented tracker that names no track. Spendy pairs a physical NFC card with a vivid user (kids buying Robux). Note: PF Tracker did not target Capital One.

### 2b. Findings (spec §7 format)

Group sizes: winners N = 36 (unique projects), demo_ready N = 50, random N = 50. Percentages are unweighted (single event). "Depth A only" means records with evidence depth A: winners 29, demo_ready 30, random 18.

```
FINDING: Winners more often show at least one feature actually working; the number of features claimed is the same in every group.
SUPPORT: shown_working ≥1: winners 27 of 36 (75%), demo_ready 21 of 50 (42%), random 17 of 50 (34%). Depth A only: 23/29 (79%) vs 16/30 (53%) vs 11/18 (61%). ≥3 shown working: 12 of 36 (33%) [Beacon, DCDaddy, HealthSense, InsighT, Kori, NLB, PoyoPop, SpendingWithSpendy, TaskFlow, Toyotron, WiSPR, Working Memory] vs 8 of 50 (16%) [Cursor on the Go!, PF Tracker, PotionWatch, PrisM, PulseLink, T-Pulse, The Potion Police, Witch Delivery Associates] vs 7 of 50 (14%). Median features listed = 6 in all three groups; median shown working = 2 (winners) vs 0 (both baselines).
COUNTEREXAMPLES: 9 winners show no feature working: AutoBoard, bevinAI, Cura, hyperlynx, Kachow, ProdigyPM, ProdPlex, ProDuh!, Relay. Highly complete EOG non-winners: Witch Delivery Associates (7), The Potion Police (6), PotionWatch (4).
CONFIDENCE: medium. The gap survives the depth-A filter, but working_status was labeled by different reader passes for winners and baseline, and some baseline pages were read thinly.
TYPE: association
IMPLICATION FOR US: Freeze the claimed feature list early. Spend the effort on getting each core flow visibly working (screenshot or video per flow), not on adding features.
```

```
FINDING: Winners rarely present unbuilt features. Non-winners, especially typical entries, often list planned features.
SUPPORT: any feature marked planned: winners 3 of 36 (8%) [Enchantress, HarmoniQ, Hingine]; demo_ready 10 of 50 (20%) [Adjacent, BUYOTA, Catalyst, Destination 67, The Potion Police, TOYODA, ToyoQuest, Toyota Dream Finder, Toyota Path Finder, Witch Delivery Associates]; random 16 of 50 (32%). Depth A only: 3/29 (10%) vs 5/30 (17%) vs 7/18 (39%).
COUNTEREXAMPLES: all 3 winners above won despite planned items. low n (winners 3).
CONFIDENCE: low–medium (small counts; the planned label depends on what the writeup chose to mention).
TYPE: association
IMPLICATION FOR US: Put roadmap items only under "What's next", never in the feature list. Do not demo or caption anything not built.
```

```
FINDING: Large scope is more common among winners, but a third of winners are small builds, including a General winner.
SUPPORT: scope large: winners 7 of 36 (19%) [AutoBoard, AutoPM, DCDaddy, InsighT, Kori, Pact, Toyotron]; demo_ready 4 of 50 (8%) (low n) [AutoMatch, Read the Room, Sync, T-Time]; random 1 of 50 (2%). Scope small or tiny: winners 13 of 36 (36%) [incl. NLB (General), SpendingWithSpendy (2 prizes), MirrorAPI, Hingine]; demo_ready 22 of 50 (44%); random 38 of 50 (76%). LOC ≥5,000: 18 of 36 (50%) vs 20 of 50 (40%) vs 11 of 50 (22%).
COUNTEREXAMPLES: AutoMatch, Read the Room, Sync and T-Time are large and did not win. NLB (~2.5k lines) won General.
CONFIDENCE: medium (scope scale is a reader judgment; the depth-A view gives the same direction: 21% vs 10% vs 6%).
TYPE: association
IMPLICATION FOR US: Size is not the lever. A small build whose core journey visibly works is a proven winning shape. Cap scope at what can be shown working before the final submission.
```

```
FINDING: AI use is the same across groups. Agent or tool-use designs are more common among winners, yet a fifth of winners use no AI at all.
SUPPORT: ai_used: winners 29 of 36 (81%), demo_ready 38 of 50 (76%), random 34 of 50 (68%). agent_or_tool_use: winners 21 of 36 (58%) vs 17 of 50 (34%) vs 12 of 50 (24%); depth A only 17/29 (59%) vs 11/30 (37%) vs 6/18 (33%). No-AI winners: 7 of 36 (19%) [Enchantress, Hingine, PoyoPop, SpendingWithSpendy, Stamped, TaskFlow, WiSPR].
COUNTEREXAMPLES: agentic non-winners: Bridgit (7-agent LangGraph), Clarity (6 agents), PrisM (14 agents), Sync (8 agents), Kramhtron.ai.
CONFIDENCE: medium (ai_types come from first-pass tags; "agent" is self-described and often claimed, not shown).
TYPE: association
IMPLICATION FOR US: If we use AI, make it act (tool calls with a visible side effect such as a Jira ticket, email or booking), not only chat. Do not force AI into a track whose winners did without it (Capital One, Best Design, Startup, Beginner).
```

```
FINDING: In 2025's company-problem tracks, no winner integrated a sponsor product. Integration meant solving the sponsor's stated business problem. Sponsor-tech depth mattered only for API-depth prizes (Nvidia, Solana).
SUPPORT: (my close-read judgment, counted in Q19_hackutd2025_award_integration_counts.csv) 41 awards to 36 winners. Company-problem awards (T-Mobile, PNC, Goldman Sachs, State Farm, CBRE, TFS, Northmark, Capital One, EOG): 22 of 24 problem-only, 2 of 24 used the sponsor's dataset [Enchantress, PoyoLabs (EOG)]. Nvidia: 3 of 3 core [Alchemetrics, DataDriver, Toyotron]. MLH/API prizes: 1 core [Pact/Solana], 3 supporting [HarmoniQ/Auth0, HealthSense/Vultr, Kori/Gemini], 1 token [hyperlynx/GoDaddy], 2 none visible [Relay/ElevenLabs, bevinAI/DigitalOcean]. The derived "any sponsor tool core" flag is not higher for winners (14 of 36, 39%) than for demo_ready (26 of 50, 52%) or random (17 of 50, 34%), partly because baseline readers counted the EOG API as a sponsor tool.
COUNTEREXAMPLES: none for the company-problem tracks. Relay and bevinAI won API prizes with no visible use (possible data error).
CONFIDENCE: medium (integration depth is my judgment from the profiles; the derived flag is tagged inconsistently across datasets).
TYPE: fact (for counts) / inference (for "what judges wanted")
IMPLICATION FOR US: For a company-problem track, spend the effort on fidelity to the sponsor's business problem and user, not on hunting for a sponsor API. For an API-depth prize, make the sponsor tech the brain of the demo (as Nemotron was in DataDriver and Toyotron).
```

```
FINDING: Winners in company-problem tracks more often state plainly which sponsor challenge they answer.
SUPPORT: prompt fit "explicit", restricted to company-problem tracks (Q19_hackutd2025_domain_track_prompt_fit.csv): winners 11 of 24 (46%) [AutoBoard, AutoPM, Beacon, Cura, DCDaddy, Hingine, InsighT, ProdPlex, qAPIbara, SpendingWithSpendy, TrustEstate AI]; demo_ready 8 of 34 (24%) [Aethernet, Cauldron-FlowGuard AI, GenVis, PMGenie, PotionWatch, Snitch the Witch, The Potion Police, Witch Delivery Associates]; random 3 of 20 (15%; low n) [BudgetBrew, FinPath, lisTen.AI]. All tracks, depth A only: 13/29 (45%) vs 8/30 (27%) vs 3/18 (17%).
COUNTEREXAMPLES: 6 of the 8 explicit demo_ready entries are EOG entries that did not win. 13 winners fit only implicitly (e.g. DataDriver, MirrorAPI, Toyotron, TrustIssues.AI).
CONFIDENCE: low–medium. Winner pages list their prize, so readers may have rated their fit as explicit more readily. Non-winner targeting is inferred.
TYPE: association
IMPLICATION FOR US: Name the sponsor challenge and its stated user in the first two lines of the Devpost and in the pitch. Map each feature to a challenge requirement (as DCDaddy did with "all five challenge areas").
```

```
FINDING: Winners more often name a specific user role. The generic "car buyer" framing that dominated the Toyota entries is the main non-winner pattern.
SUPPORT: (my judgment, Q19_hackutd2025_named_user_counts.csv) specific named user: winners 31 of 36 (86%); demo_ready 33 of 50 (66%). Not specific: winners 5 [Kachow, PoyoLabs, Toyotron, TrustEstate AI, VisionScout]; demo_ready 17, of which 11 are car-buying/Toyota entries [AutoMatch, AutoMate, BuildYourRide, BUYOTA, CarCents, CarTender, ProToyotaAI, TOYODA, ToyoQuest, Toyota Dream Finder, Toyota Path Finder]. random not judged.
COUNTEREXAMPLES: Toyotron and Kachow won TFS with generic "car buyers". Many specific-user non-winners (Bridgit: drivers of tall vehicles).
CONFIDENCE: low (single-rater judgment, no pilot agreement; the gap is concentrated in one track).
TYPE: association
IMPLICATION FOR US: Name the user narrowly (role plus situation, e.g. Hingine's "college students with thin credit") in the tagline. In a crowded consumer track this is the cheapest way to stand out.
```

```
FINDING: Winners more often make impact claims, but no winner shows measured impact. The claims are asserted or unmeasured.
SUPPORT: has_impact_claims: winners 8 of 36 (22%) [AutoBoard, bevinAI, Cura, DCDaddy, hyperlynx, Kachow, qAPIbara, TrustIssues.AI]; demo_ready 3 of 50 (6%; low n) [Bait & Switch, Reflex Work Order Automation, ShelfSense]; random 2 of 50 (4%; low n). In the profiles every winner claim is unmeasured ("weeks to hours", "80% faster") or a cited outside statistic (Kachow 46% remorse, Cura 21%, TrustIssues "up to six months").
COUNTEREXAMPLES: Read the Room (DR) gives the most numeric claims (85–95% accuracy) and did not win. 28 of 36 winners make no impact claim.
CONFIDENCE: low (the field may have been applied differently across the two first-pass datasets; low n in the baselines).
TYPE: association
IMPLICATION FOR US: One cited statistic about the user's pain is common among winners and cheap to add. Measured impact is a gap nobody filled. A measured before/after comparison of the core task during the event would be distinctive.
```

```
FINDING: A live deployed URL is the one presentation asset clearly more common among winners. Video cannot be compared (the data conflicts), and architecture diagrams do not differ.
SUPPORT: live demo URL: winners 9 of 36 (25%) [DCDaddy, hyperlynx, InsighT, Kachow, Kori, PoyoLabs, PoyoPop (Figma), Stamped, Toyotron]; demo_ready 2 of 50 (4%; low n) [Snitch the Witch, T-Time]; random 6 of 50 (12%). Architecture diagram: 5 of 36 (14%) [AutoBoard, HealthSense, ProdPlex, Toyotron, TrustIssues.AI] vs 5 of 50 (10%) vs 1 of 50 (2%). Video: winners 17 of 36 (47%) by first-pass URL, but 35 of 36 by page-fetch embed detection; baseline URL field 40/50 and 39/50, including empty placeholder pages (JJKA, idk, Cortex), so it is unreliable.
COUNTEREXAMPLES: Snitch the Witch and T-Time had live sites and lost; NLB and Working Memory won without a live URL in the record.
CONFIDENCE: medium for live URL; none for video (see section 3).
TYPE: association
IMPLICATION FOR US: Deploy the build to a public URL and link it on Devpost (judges and sponsor reps can open it). Do not rely on the video to carry the submission.
```

```
FINDING: Winner writeups more often fill the full Devpost template. Length differs less.
SUPPORT: ≥6 writeup sections: winners 32 of 36 (89%), demo_ready 37 of 50 (74%), random 27 of 50 (54%); depth A only 26/29 (90%) vs 22/30 (73%) vs 13/18 (72%). Long writeup: 20 of 36 (56%) vs 22 of 50 (44%) vs 17 of 50 (34%). README "detailed": 10 of 36 vs 25 of 50 demo_ready (README is not a winner marker).
COUNTEREXAMPLES: AutoBoard, hyperlynx, Relay (blank narrative) and SpendingWithSpendy won with fewer sections.
CONFIDENCE: medium
TYPE: association
IMPLICATION FOR US: Fill every Devpost section (Inspiration through What's next) with specific content. A polished README is not a substitute.
```

```
FINDING: Five winners stacked two prizes from one build. Two of them paired a company-problem track with Nvidia by making Nemotron the agent core.
SUPPORT: multi-prize winners 5 of 36 (14%): DataDriver (Northmark + Nvidia), Toyotron (TFS + Nvidia), HarmoniQ (T-Mobile + Auth0), Pact (CBRE + Solana), SpendingWithSpendy (Capital One + Best Design). 2 of the 3 Nvidia winners came stacked with a domain track. Non-winners: 0 of 100 by definition (not a comparison).
COUNTEREXAMPLES: many demo_ready entries used Nemotron in a domain track and won nothing (GenVis, PMGenie, PrisM, CarTender, Kramhtron.ai, Reflex).
CONFIDENCE: high for the counts; low n.
TYPE: fact
IMPLICATION FOR US: Plan one build for a company-problem track plus Nvidia (if Nemotron is again the Nvidia ask), with the sponsor model doing the visible reasoning. Treat MLH API prizes as add-ons only where the API is genuinely used.
```

```
FINDING: Competition was very uneven across tracks. Tracks that drew many baseline entries (Toyota, T-Mobile, Nvidia) awarded the same 3 prizes as tracks no baseline project targeted (State Farm, Goldman Sachs).
SUPPORT: baseline projects (demo_ready + random) targeting each track vs winners (Q19_hackutd2025_track_targeting.csv): Toyota FS 16 of 100 (10 DR + 6 R) vs 3 winners; T-Mobile 16 of 100 (8 + 8) vs 3; EOG 8 of 100 (8 + 0) vs 2; Nvidia/Nemotron 26 of 100 (17 + 9; broad keyword) vs 3; State Farm 0 of 100 vs 3; Goldman Sachs 0 of 100 vs 3; CBRE 2 of 100 vs 3; PNC 4 of 100 vs 3; Northmark 5 of 100 vs 3.
COUNTEREXAMPLES: none in the sample. But the baseline is 100 of 325 non-winners, and targeting is inferred, so a few unsampled projects may have targeted State Farm or Goldman.
CONFIDENCE: medium for direction, low for exact ratios.
TYPE: association (inference on the cause: fewer entrants)
IMPLICATION FOR US: When tracks are announced, prefer the B2B or enterprise-problem tracks (insurance, banking operations) over consumer car-buying or sentiment-dashboard themes, unless we have a clearly different angle.
```

### 2c. What did not separate winners from demo_ready

- **AI use at all** (81% vs 76%) and **Nemotron use**: all three demo_ready PNC entries used Nemotron; 2 of 3 PNC winners used Gemini.
- **Feature count claimed** (median 6 everywhere).
- **Repo tests** (7 of 36 vs 12 of 50).
- **Architecture diagram** (14% vs 10%).
- **Detailed README** (10 of 36 vs 25 of 50).
- **Same-idea crowding**: the PNC, T-Mobile, State Farm and Northmark winners are close look-alikes of non-winners in the same track. The idea alone did not decide these tracks (inference).

---

## 3. Open questions / data issues

1. **Video fields are unusable for the winner vs baseline comparison.**
   - Winners: first-pass `demo_video_url` 17 of 36, deep-dive `has_video` 17 of 36, page-fetch `has_video_embed` 35 of 36 (`data/pages/page_facts.jsonl`).
   - Baseline: first-pass `demo_video_url` is 40 of 50 / 39 of 50, but it includes empty placeholder pages (JJKA, idk, Cortex, Food search). The deep-dive `has_video` is 7 of 50 / 2 of 50, even though `demo_ready` was selected for having a video.
   - Two winners conflict between profile and record (Working Memory, AutoBoard).
   - Needs: page-fetch embed detection run on the baseline, and a check of whether the embed detector catches non-demo iframes.
2. **Screenshot counts are not comparable.** Baseline first-pass `n_screenshots` counts all page images (Bridgit 31, demo_ready median 12.5), while the deep dive counts 3 (median). Use `page_facts.n_gallery_items` once the baseline is fetched.
3. **`share_commits_in_window` is blank for all winners** (their records use `commits_in_event_window`, mostly null), so the spec's "commit share in window" comparison could not be run.
4. **Prize-attribution doubts.**
   - Relay (Best Use of ElevenLabs) and bevinAI (Best Use of DigitalOcean Gradient AI) show no use of the prize's tech in any source. Either the page is incomplete or the prize was mapped to the wrong project. Re-check the badges on the Devpost pages.
   - Alchemetrics uses the EOG dataset but won Nvidia only.
5. **Self-reported placements** (from READMEs, not Devpost): Working Memory "1st place grand prize", Toyotron "2x first place" (TFS + Nvidia), AutoPM 2nd (PNC), qAPIbara 2nd (State Farm). Not verified. If the team accepts these, they add four placement points for Q1-style comparisons.
6. **Different reader passes.** Winner and baseline records came from different first-pass and deep-dive runs. Fields such as `working_status`, `has_impact_claims` and `sponsor_tool_use` (EOG API counted as a sponsor tool for the baseline but not for the EOG winners) may have been applied unevenly. The shown-working gap survives the depth-A filter, but the S3 blind re-tag should settle it.
7. **Evidence depth is unequal.** Depth A: winners 29 of 36 (81%), demo_ready 30 of 50 (60%), random 18 of 50 (36%); depth C: 0 / 2 / 8. Depth-A-only views are in the group-counts table. Every finding above was checked against them, and the direction held.
8. **Track targeting for non-winners is inferred** from content (`prompt_fit.targeted_prizes`); the Nvidia keyword ("nemotron") over-counts. HackUTD 2025 challenge statements were never public (hackerpack only).
9. **Manual judgments are single-rater.** Integration depth and named user (`data/tagged/close_reads/`) were not piloted for agreement.
10. **Unexplained wins.** These are not explained by the available evidence: ProdigyPM (General: no repo, video or live link), Cura (CBRE: no demo, nothing shown working), Kachow (TFS: nothing shown working), Enchantress (EOG, versus more complete EOG non-winners). Live Q&A and the expo demo are not in the data, and they may account for these.
11. **The baseline sample covers 100 of 325 non-winners.** The track-crowding counts are sample counts, not totals.
