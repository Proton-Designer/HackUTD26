# Cal Hacks — Cal Hacks 13.0 (2026) (16 projects)

### ANNEAL
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Hyphenate] The Hyphenated Enterprise: Autonomous Systems for Finance

**What it is:** Formula 1 cost-cap finance system for a team like Williams: detects a crash from telemetry, classifies damaged parts, drafts spares, work orders, freight and accounting entries, and posts them through a permissioned, audited database gate with role-specific views.
**Problem / user:** F1 team finance, garage, strategy and CFO roles, who learn crash costs weeks later via invoices while each function tracks its own numbers.

**Features**
- Crash detection from race data — Timing, telemetry and race-control feeds flagged Williams 2024 impacts 9-26 s before red flag *[claimed]*
- Part-impact classification — Jev (TypeSafe System One) classifies impact and likely parts with confidence gates *[claimed]*
- Response plan drafting — Reserves spares, creates work orders, schedules freight, prepares accounting; Claude writes plans and role briefs *[claimed]*
- Gated accounting postings — All money decisions pass one SpacetimeDB gate with audit row; precedent lines auto-post, others wait for Head of Cost Cap *[claimed]*
- 22-part tracking with cost-cap treatment — Condition, life, spares and cap status updated by laps, kerbs, crashes *[claimed]*
- Monte Carlo season model — 10,000 runs about 80 ms per update showing finishing-position odds and ranges *[claimed]*
- Role views and Microsoft connectors — Garage, Strategy, Accounting, CFO screens in sync; Business Central, Teams/Outlook approvals, Azure auditor *[claimed]*

**Flow:** Replay of Sao Paulo 2024 weekend runs → Crash flagged and parts classified → Agent drafts response plan → Chief of Staff approves or edits in plain language → Precedent lines post; others await cost-cap head → Season outlook and all role screens update

**Prompt:** Hyphenate track "The Hyphenated Enterprise: Autonomous Systems for Finance": only title and prizes published (cash for top 3, expedited interviews for top 5); no detailed brief.
**Fit (implied):** An autonomous finance workflow that turns a physical event into postings, with code-enforced approval gates and audit trail.  *(targeted: Hyphenate: Hyphenated Enterprise (Autonomous Systems for Finance))*
**Sponsor tools:** SpacetimeDB (rules, permissions, audit log and realtime sync, core); Claude (repair plans, edits, briefs, core); Apify (collecting FIA documents, supporting); Microsoft (Business Central/Teams/Azure OpenAI) (connectors; auditor built but not enabled, supporting)
**AI:** Claude drafts plans and briefs; Jev classifier with confidence gates; NumPy Monte Carlo; agents cannot approve their own work.
**Architecture:** Python/FastAPI services consume OpenF1/Jolpica feeds and write through SpacetimeDB reducers (permission + audit); React/Vite role views subscribe live; Azure deployment templates.
**Novelty:** Applies agent finance automation to F1 cost-cap compliance, with replay on real 2024 race data and a transactional approval gate that audits refusals too.
**Scope:** large · working: Replay results quoted (2,549 events, 18 replacements); repo with tests, Docker, 66k LOC estimate. · polish: Role-specific UIs, three.js pitch page, Azure/Bicep templates; no video or live link.
**Claims:** Flagged Williams crashes 9 to 26 seconds before the red flag | Weekend sealed at $3.77M vs nearly $4M reported | 96% of events correct in backtest | 10,000 Monte Carlo runs in about 80 ms
**Gaps:** No video or live demo; Numbers self-reported
Sources: https://devpost.com/software/anneal-u3xh1o, https://github.com/gaviiin/calhacks (evidence file), https://cal-hacks-13-0.devpost.com/

---

### Arigami
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Cal Hacks Best Beginner Hack

**What it is:** A Chrome/Edge extension (named Access in the repo) that replaces the current page, in place and at the same URL, with a redesigned version for focus, motor-impairment or screen-reader needs, keeping the site's own colors, fonts and images. An optional AI redesign uses Apify and Claude.
**Problem / user:** People with ADHD, motor impairment or blindness/low vision who struggle with sites not built for them; inspired by a child with a motor-impairment disease.

**Features**
- Focus mode — Rebuilds the page as a slide-style deck: one idea at a time, key points, progress bar and reading line. *[shown_working]*
- Motor-impairment mode — Huge targets, big tiles with few choices, dwell-to-click, on-screen keyboard and scroll zones. *[shown_working]*
- Head-controlled mouse — Python/MediaPipe webcam tracking moves the cursor (Windows) and a held right-eye wink clicks. *[claimed]*
- Screen-reader mode — Adds landmarks, a single heading outline, skip links, clear link names and real tables; optional AI picture descriptions. *[shown_working]*
- AI redesign — Apify reads the whole site to build a site map, then Claude plans the layout; user consents first. *[claimed]*
- Original-page restore — One click returns the original page; everything except AI and head control works without keys or server. *[shown_working]*

**Flow:** Install the extension and start the local server (optional) → Open any website and click the Access icon → Choose Focus, Motor impairment or Screen reader → Click Redesign this page → Navigate with big targets, dwell or head control → Restore the original with one click

**Prompt:** Best Beginner Hack: prize only (AirPods 4 per team member), no description on the prize list.
**Fit (implied):** The page stresses first-time use of Chrome extensions, Figma and Apify; prize text itself defines no criteria.  *(targeted: Cal Hacks Best Beginner Hack)*
**Sponsor tools:** Claude (Anthropic SDK) (Page plans, tile titles, picture descriptions; also used to write code, core); Apify (Cheerio Scraper) (Reads the whole site for the AI redesign, supporting)
**AI:** Claude plans page layouts from a scanned page model and an Apify site map, writes tile titles and image descriptions; MediaPipe landmark tracking drives head control. A local server keeps keys off the extension.
**Architecture:** Manifest V3 extension scans the page into structured data and rebuilds it per mode; local Node server (127.0.0.1:4173) calls Claude and Apify; optional Python head-control process; includes test suite and CI.
**Novelty:** Redesigns arbitrary live pages in place rather than overlays; adds head and wink control; unusually large beginner repo with tests and CI.
**Scope:** large · working: README has quick start and demo video; ~5.9k LOC across extension, server, eye-tracking and 15 test files. · polish: Detailed README, MOTOR_ACCESS doc, consent dialog, CI, Figma prototypes.
**Claims:** Team found head/gaze tracking very seamless in its own testing
**Gaps:** Not tested with motor-impaired users, per page; Repo README describes a later version (head-control wink); Devpost mentions gaze, voice and switch control; feature list follows the README
Sources: https://devpost.com/software/arigami-web-accessibility, evidence/cal-hacks-cal-hacks-13-0-2026-arigami.json, https://cal-hacks-13-0.devpost.com/

---

### BrainSync
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Cal Hacks Most Technically Complex Hack

**What it is:** A brain-computer interface where flickering on-screen squares are chosen by gaze: an 8-channel EEG board reads SSVEP responses and a CCA decoder picks the target. Its main demo, BCI Voice, has Claude propose ranked replies that the user selects and speaks aloud.
**Problem / user:** People whose tremor, stiffness or weak voice make typing, pointing or speaking hard (Parkinson's, ALS, cerebral palsy), for whom eye trackers and clinical BCIs are limited or costly.

**Features**
- Two-target SSVEP decoder — 15 and 17 Hz squares; training-free CCA or filter-bank CCA on posterior channels decides which one is viewed. *[shown_working]*
- BCI Voice — Partner's speech is transcribed; Claude writes three ranked replies, each beside a flickering square, plus NEXT for more. *[claimed]*
- Confirm-before-speaking — Looking at a reply opens Say it/Back; the Cartesia voice speaks only after a second look. *[claimed]*
- Conservative online decoding — Scores every 0.25 s over 1.5 s windows and abstains unless a lead and resting-baseline margin hold for four windows. *[shown_working]*
- Gaze apps — BrainPoint extension picks clickable elements via Claude; BrainScroll, BrainSwipe and BrainChess demos. *[claimed]*
- Live brain map and partner view — Browser scalp map of EEG metrics; partner mirror with a Stop button and an iPhone app. *[claimed]*
- Jetson appliance (BrainSyncOS) — Installer image turns a Jetson Orin Nano into a headset-and-decoder server. *[claimed]*

**Flow:** Partner speaks and speech is transcribed → Claude proposes three ranked replies → Squares flicker beside each reply → User looks at one reply and a confirm screen opens → User looks at Say it and the reply is spoken

**Prompt:** Cal Hacks Most Technically Complex Hack: prize only (NuPhy keyboard per member); the general criterion asks for command of frameworks and infrastructure and engineering depth.
**Fit (implied):** Spans EEG signal processing, a real-time decoder, hardware deployment and multi-client software, which is the depth the technical-complexity criterion describes; no explicit targeting.  *(targeted: Cal Hacks Most Technically Complex Hack)*
**Sponsor tools:** Claude (Ranked reply proposals via forced tool call; clickable-target ranking, core); Cartesia (Spoken output with cached audio, supporting); OpenBCI/Cerelog X8 with BrainFlow (EEG acquisition, core)
**AI:** Claude, with strict validation and keyword fallbacks, proposes replies in the user's voice; the decoder itself is classical CCA/FBCCA signal processing and the LLM never selects.
**Architecture:** PsychoPy stimulus and Cerelog X8 via BrainFlow into a FastAPI event-driven state machine; versioned WebSocket protocol to browser, iPhone and voice clients; Jetson deployment via Cloudflare tunnel.
**Novelty:** Reports cued-session accuracies with permutation statistics and negative controls; large repo (~120k LOC) with ~2,900 tests and an installable device image.
**Scope:** large · working: Devpost reports three cued sessions and a public-dataset benchmark; repo has 488 files, tests and Docker. · polish: Detailed README, photosensitivity warnings and fallbacks; no video or live demo link on page.
**Claims:** 89%, 82% and 93% accuracy on three two-target recordings | Median 1.24 s to a correct pick on reference session | CCA and FBCCA 92.2% and 93.7% on the 12-target Nakanishi dataset | About 2,900 automated tests
**Gaps:** Only part of README read; Accuracy figures self-reported on small samples; Not tested with target users; BCI Voice end-to-end status relies on writeup
Sources: https://devpost.com/software/brainsync, evidence/cal-hacks-cal-hacks-13-0-2026-brainsync.json (README first ~3500 chars), https://cal-hacks-13-0.devpost.com/

---

### Drigil
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Anthropic] Claude for Public Benefit

**What it is:** Wearable job coach for workers with intellectual and developmental disabilities. A supervisor records a narrated video, Claude turns it into steps, and a camera on glasses checks work live, speaks gentle corrections in the supervisor's cloned voice, and fades support as the worker masters steps.
**Problem / user:** Workers with IDD in the first weeks of a job, plus supervisors and job coaches who are scarce.

**Features**
- Teach once from video — Claude generates 4-8 steps with instruction, correction, reason, praise and cue *[shown_working]*
- Live camera step checking — Sonnet checks each frame against whole step list; box drawn on mistake *[shown_working]*
- Consented supervisor voice clone — Cartesia clones narration and speaks coaching in it *[shown_working]*
- Voice Q&A — Always-on mic answers questions about what the camera sees *[shown_working]*
- Per-worker memory and support fading — Moss recalls tricky points; SpacetimeDB rule raises/lowers support level by recent runs *[shown_working]*
- Agentic re-teaching — Factory Droid rewrites a problematic step in sandbox; supervisor approves *[shown_working]*
- Help routing and wristband — Buddy paged first, escalates to supervisor after 20 s; Arduino touch wristband *[shown_working]*
- Dignity and privacy rules — Faces blurred in browser, two mistakes before correction, no worker video stored *[claimed]*

**Flow:** Supervisor records narrated task video → Claude produces steps; voice cloned with consent → Worker starts; glasses camera streams blurred frames → Coach announces steps and gentle corrections → Worker asks questions aloud → Support fades; level-ups celebrated → Supervisor dashboard and re-teach approval

**Prompt:** Anthropic "Claude for Public Benefit": listed prize is Claude credits, Claude Max for a year and office hours; no track description published.
**Fit (implied):** Uses Claude Opus/Sonnet for teaching-step generation and live vision checks to support disabled workers in employment.  *(targeted: Anthropic: Claude for Public Benefit)*
**Sponsor tools:** Claude (step generation and live frame checks, core); Cartesia (voice clone TTS and STT, core); SpacetimeDB (shared live state, atomic help claims, escalation, core); Moss (per-worker memory recall, core); Factory Droid SDK (sandboxed step re-teaching, core); Bitdeer (benchmarking vision models, supporting)
**AI:** Claude Opus builds steps from video; Claude Sonnet runs per-frame vision checks with full step list; Cartesia voice; Moss retrieval; Droid agent edits steps under validator and approval.
**Architecture:** React browser (MediaPipe, face blur, mic) to Python FastAPI edge app calling Claude/Cartesia/Moss; SpacetimeDB holds sessions, outcomes, help requests; Raspberry Pi camera and Arduino wristband.
**Novelty:** Combines vision coaching, voice cloning, support-fading logic, sandboxed agent self-edit and physical wearables, with dignity rules enforced in code.
**Scope:** large · working: Live Vercel demo, measured results on 30-frame test set, real hardware loop reported. · polish: Detailed writeup with latency tables and real-vs-simulated labeling; no video.
**Claims:** Live Sonnet check 73% accuracy, 44% mistakes caught, 2.2 s median latency on 30-frame set | Moss recall p50 1.43 ms | Cartesia first audio 723 ms | Droid re-teach run took about 35 s
**Gaps:** No demo video; Gemini/OpenAI/OpenCV tags unexplained
Sources: https://devpost.com/software/drigil, https://github.com/shraddha11-408/CalHacks-13.0 (evidence file), https://cal-hacks-13-0.devpost.com/

---

### Eve: event finances handled
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Hyphenate] The Hyphenated Enterprise: Autonomous Systems for Finance

**What it is:** AI finance back office for hackathons and events: reads receipts, checks travel claims, analyzes prize payouts and tax forms, proposes payments for a controller to release, and drives sponsor portals with computer use, stopping before Submit.
**Problem / user:** Hackathon organizers, controllers and attendees facing slow, error-prone prize payouts, reimbursements and cross-border tax paperwork.

**Features**
- Receipt reading and claim checks — Claude extracts receipts, converts currency, checks caps, duplicates and fare comparisons, then pays or flags *[claimed]*
- Prize analysis and team splits — Compares shipping, local purchase and cash; each team member confirms split *[claimed]*
- Tax form handling — Collects W-9/W-8BEN and computes withholding, fees and FX before approval *[claimed]*
- Fraud guards — Flags padded fares, escalates suspicious claims, freezes payout after bank change until confirmed *[claimed]*
- Controller-only release with Slack approvals — Code prevents organizers or agent from releasing; DM approvals *[claimed]*
- Sponsor portal automation — Claude computer use on E2B desktop fills forms and stops before Submit; reconciles remittances *[claimed]*
- Immutable double-entry ledger and exports — Journal export for QuickBooks, 1099/1042-S worksheets *[claimed]*

**Flow:** Organizer sets budgets and rules → Attendees upload receipts and claim prizes → Eve checks and pays or flags claims → Payout proposals show gross, withholding, fees, net → Controller approves, including from Slack → Computer-use agent fills sponsor portal, human submits → Ledger posts; books exported

**Prompt:** Hyphenate track "The Hyphenated Enterprise: Autonomous Systems for Finance": only title and prizes published (cash for top 3, expedited interviews for top 5); no detailed brief.
**Fit (implied):** Autonomous finance agent that handles claims, tax and payouts end to end with deterministic limits and human release.  *(targeted: Hyphenate: Hyphenated Enterprise (Autonomous Systems for Finance))*
**Sponsor tools:** Claude (Anthropic SDK, computer use) (receipt extraction, review agent, portal entry, core); E2B (sandboxed Linux desktop, supporting); PlanetScale (Postgres database, supporting)
**AI:** Claude extracts structured data and runs a nightly review agent; Claude computer use operates sponsor portals; amounts and rules are deterministic code, uncertain reads go to humans.
**Architecture:** Next.js 16 app with server actions, Postgres/Drizzle, Better Auth, Vercel Workflow jobs; Slack integration; E2B desktop for computer use.
**Novelty:** Targets event-finance workflows with agent permission limits enforced in code and a seeded 300-person test event with planted problems.
**Scope:** large · working: Live demo site and seeded event; repo with tests, 44k LOC estimate. Money movement is simulated. · polish: Role-based app, Slack, ledger and exports; no video.
**Claims:** Caught 40 of 40 planted problems with no false positives (self-reported) | Fake 300-person event with 160 travel claims and 25 prizes
**Gaps:** No video; Fare data source unnamed
Sources: https://devpost.com/software/eve-event-finances-handled, https://github.com/uijincho/eve (evidence file), https://cal-hacks-13-0.devpost.com/

---

### FortWatch
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Cal Hacks Best Hardware Hack

**What it is:** A low-cost wrist-worn display built on an ESP32-S3 touch-screen board that recognizes ten important everyday sounds and shows a full-screen alert with a distinct vibration pattern, aimed at deaf and hard-of-hearing wearers.
**Problem / user:** Deaf and hard-of-hearing people who want sound awareness without an Apple Watch-priced device; inspired by a deaf college student who felt dependent when out alone.

**Features**
- Ten-class sound alerts: alarm, car horn, glass, shout, baby, knock, doorbell, phone, dog, speech — YAMNet classifier scores the last second of audio twice per second; per-class thresholds were tuned on the ESC-50 clips. *[shown_working]*
- Full-screen visual alert with icon and large label — The ESP32-S3 touch LCD switches from a listening screen with level bar to a designed alert screen; tap dismisses it. *[shown_working]*
- Urgency-coded vibration — Three long pulses for safety sounds, two short for attention sounds, one short for low priority. *[claimed]*
- iPhone companion that does recognition and direction estimate, then sends alerts over Bluetooth LE — Bundled converted YAMNet maps 36 source classes to the ten alerts and estimates dominant sound direction; no Mac or server needed. *[claimed]*
- Mac listener fallback path — Python program takes Mac or iPhone-continuity mic audio, runs YAMNet and pushes alerts to the band over Bluetooth or USB. *[shown_working]*
- Live event dashboard — Alerts sync over Wi-Fi to a SpacetimeDB database (hosted via Mana) and a web dashboard shows what sounds happened and when. *[claimed]*
- 3D-printable snap-on wristband case — OpenSCAD source, STLs, viewer and pre-print check tools in the repo; powered by a USB-C power bank. *[shown_working]*
- Privacy by design — Audio is classified on the wearable or phone and is not uploaded; only alert events are sent onward. *[claimed]*

**Flow:** Power the wristband; it shows a waiting screen then LISTENING with a live level bar → Wearer goes about their day while audio is classified twice a second → A relevant sound fills the screen with its icon and name and the motor vibrates by urgency → Wearer taps to dismiss → Alert event appears on the live dashboard

**Prompt:** Cal Hacks Best Hardware Hack: official brief not found on the public hackathon page; prize name only.
**Fit (implied):** A physical custom-assembled device: ESP32-S3 touch display, mic and vibration motor in a printed case, with firmware and on-device ML. Connection to the prize is inferred from the name only.  *(targeted: Cal Hacks Best Hardware Hack)*
**Sponsor tools:** SpacetimeDB (via Mana) (Real-time storage of alert events for the dashboard, supporting); Claude Code (Co-authored most of the code and hardware learning (per Devpost), supporting)
**AI:** Pretrained Google YAMNet (521 audio classes) run on-device, with a hand-built mapping of relevant classes to ten alerts, tuned thresholds, and a knock-vs-glass suppression heuristic. No generative model at runtime.
**Architecture:** Microphone audio goes to YAMNet (on ESP32-S3 per Devpost; on iPhone or Mac in the repo) and then via Bluetooth LE to the ESP32-S3 wristband firmware, which draws alerts and drives the motor; events also post to SpacetimeDB for the dashboard.
**Novelty:** Cheap wearable alternative to smartwatches, with a published threshold calibration against ESC-50 and several input paths (band, iPhone, Mac); built by a team without a hardware engineer.
**Scope:** medium · working: Repo has about 20k LOC, firmware, iOS app, Mac demo and tests; README says real iPhone capture and BLE/motor validation are still pending. · polish: Designed alert screens, 3D case with checks, extensive docs and release notes; no video on Devpost.
**Claims:** Detects ten sound classes; ESC-50 catch rates of 72 to 97 percent per class (README, optimistic by its own admission) | Runs with no phone or internet on the wristband (Devpost) | Claude Code co-wrote over 85 percent of the code | Component cost might fall to about $10 (unverified estimate)
**Gaps:** Devpost says YAMNet runs on the ESP32-S3 and syncs by Wi-Fi; README describes the iPhone or Mac running recognition and Bluetooth to the band; feature list merges both; Devpost mentions Bluetooth and Wi-Fi inconsistently; No video or accuracy/latency measurement of the hardware; Official prize text not found
Sources: https://devpost.com/software/fortwatch, evidence/cal-hacks-cal-hacks-13-0-2026-fortwatch.json (README)

---

### GovTok
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Cal Hacks Most Creative Hack

**What it is:** A mobile web app presenting neighborhood problems as a TikTok-style swipe feed of short videos pinned to location. Claude screens each post, and a problem only closes when a verified repair video plays as a before/after reveal on the original card.
**Problem / user:** Residents who find city reporting forms impersonal and never learn if a problem got fixed; also municipal staff (the team targeted the City of Mableton, GA and its 311 challenge).

**Features**
- Vertical swipe feed of 20-second video reports or photo slideshows — Recorded in the phone browser, converted client-side, uploaded to Convex storage; a small pool of reused video players keeps scrolling smooth. *[shown_working]*
- Duplicate check and Me too — Before posting, finds open reports within 50 m and offers a Me too tap that raises the existing report's count in real time. *[shown_working]*
- AI screening before publishing — Claude gets about six frames plus a Whisper transcript and returns a verdict: retake for faces or plates, reject non-public issues, mute audio with names or addresses, 911 notice for emergencies. *[shown_working]*
- Auto category, title and agency routing — Claude outputs structured JSON with category and short title; a fixed routing table assigns City, Cobb County or the utility. *[shown_working]*
- Fix verification by video — Claude compares repair footage with the original for same spot (curbs, poles, drains), resolution and privacy, or says what to re-film. *[shown_working]*
- Before/after reveal stamped FIXED — Verified repair video plays on the original card. *[shown_working]*
- Clustered map of reports — Google Maps view groups reports to show hot spots, with street-level reverse geocoding without house numbers. *[claimed]*
- Resident sign-in and staff accounts — Planned so Me too counts can be trusted and city staff use existing logins. *[planned]*

**Flow:** Resident films a short clip or photo slideshow in the browser, pinned to location → App shows nearby open reports; resident taps Me too or continues → Claude screens the post live and returns retake, reject, muted or 911 guidance → Report is categorized, routed and appears in feed and map → Neighbors add Me too; counts update live → Crew or neighbor films the repair; Claude verifies it → Card shows before/after reveal marked FIXED

**Prompt:** Cal Hacks Most Creative Hack: no public brief found; prize name only.
**Fit (implied):** Applies the short-video social feed format to civic issue reporting and closes the loop with proof of repair. Link to the prize is inferred from its name.  *(targeted: Cal Hacks Most Creative Hack)*
**Sponsor tools:** Convex (Database, file storage, live updates and server actions, core); Claude API (Opus) (Post screening and fix verification from frames and transcripts, core); Claude Code (Planning, implementation and review, supporting)
**AI:** Claude Opus vision reads about six frames plus a Groq Whisper (large-v3-turbo) transcript and returns structured JSON for moderation, categorization and same-spot fix verification; transcripts are treated as untrusted to resist prompt injection.
**Architecture:** Next.js App Router mobile web app on Vercel records and converts video in-browser; Convex stores media and syncs live data; Claude and Whisper called server-side; Google Maps and Geocoding for map and place names.
**Novelty:** Combines social-video UX with automated privacy moderation and a closed-loop proof-of-fix check; no human moderation queue; aimed at a real municipal pilot.
**Scope:** medium · working: Live demo domain, about 20k LOC repo with tests; Devpost says the whole film-to-fixed loop works live. · polish: Design decisions document, mobile-first UX, detailed README; team to present to a city at a 311 challenge.
**Claims:** Won Most Creative Hack at Cal Hacks 13.0 | Built by two people in one weekend | Full loop from film to FIXED reveal works live | Scheduled to present to City of Mableton at the Georgia 311 Challenge
**Gaps:** No demo video link on Devpost; Official prize text not found; No usage metrics
Sources: https://devpost.com/software/govtok, evidence/cal-hacks-cal-hacks-13-0-2026-govtok.json (README)

---

### GroundTruth
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Hyphenate] The Hyphenated Enterprise: Autonomous Systems for Finance

**What it is:** Claims-settlement system for satellite ground-station operators. A fast tabular model auto-settles confident SLA credit disputes, an LLM investigates hard ones with citations, AWS Cedar policy decides what may auto-pay, and rules learned from human decisions are replayed on history before a controller promotes them.
**Problem / user:** Finance dispute analysts and controllers at ground-station operators who settle failed-pass credit claims by hand and inconsistently.

**Features**
- Live orbital overview — Globe from CelesTrak and SGP4 with stations and space-weather band *[claimed]*
- Dual-speed decisioning — System 1 tabular model auto-settles at 95%+ confidence with SHAP; System 2 LLM cites pass log, weather, contracts *[claimed]*
- Cedar policy gate — Permit/forbid decisions with escalation by confidence or dollar thresholds *[claimed]*
- Policy learning with replay — After 3 consistent human decisions, drafts a rule, replays on history, controller promotes *[claimed]*
- Decision audit trail — Shows features, SHAP drivers, citations, Cedar statement, human override *[claimed]*
- Ledger with segregation of duties — Approver cannot submit to ERP; append-only entries and KPIs *[claimed]*
- Break It red-team suite — Planted attacks run against old vs current policy *[claimed]*

**Flow:** A claim arrives on overview → System 1 unsure, System 2 investigates with citations → Cedar refuses auto-pay; human decides → Rule learned, policy moves v4 to v6 after replay → Break It tests new policy → Click a decision to see audit evidence → Credit lands in ledger under SoD

**Prompt:** Hyphenate track "The Hyphenated Enterprise: Autonomous Systems for Finance": only title and prizes published (cash for top 3, expedited interviews for top 5); no detailed brief.
**Fit (implied):** Autonomous settlement of billing disputes with deterministic policy guardrails, learning from human overrides, and audit.  *(targeted: Hyphenate: Hyphenated Enterprise (Autonomous Systems for Finance))*
**Sponsor tools:** SpacetimeDB (system of record with reducers and live subscriptions, core); AWS Cedar (policy engine, core)
**AI:** Tabular ML with SHAP for routine claims; LLM for evidence-citing investigation; rules mined from human decisions and replay-validated.
**Architecture:** React/TS frontend on Vercel; Rust reducers and SpacetimeDB Maincloud; Python ML analysis; Cedar policies.
**Novelty:** Policy that learns from human decisions yet cannot self-promote; red-team suite compares policy versions; blends real orbital data with simulated claims.
**Scope:** large · working: Repo of 44k LOC estimate with tests; claims escalations fell 3,406 to 1,660 in replay (simulated data). · polish: Multiple screens (overview, claims, decisions, ledger, Break It); demo video referenced but no URL.
**Claims:** Escalations dropped from 3,406 at v4 to 1,660 at v6 | Zero regressions allowed before promotion
**Gaps:** Claims data largely simulated; Video not seen
Sources: https://devpost.com/software/groundtruth-k3g5v6, https://github.com/AamirAbatiyow/CalHacks26 (evidence file), https://cal-hacks-13-0.devpost.com/

---

### half full
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Cal Hacks Third Overall [3rd]

**What it is:** Mobile-first daily news app for young people showing 3-5 curated stories with AI illustrations, narration and source "receipts", ending with a caught-up message instead of an infinite feed.
**Problem / user:** Gen Z readers worn out by crisis-framed news feeds who want to stay informed without doomscrolling.

**Features**
- Curated daily edition — 3-5 stories swiped horizontally, readable, watchable or listenable *[shown_working]*
- See the Receipts — Custom Apify Actor gathers reporting; app exposes supporting sources and provenance *[shown_working]*
- Claude editorial pipeline — Selects stories, compares evidence, writes explanations, rejects weak coverage *[claimed]*
- AI illustrations and narration — Recraft images and Cartesia voices with selectable narrators *[shown_working]*
- Your Jar reactions — Reading history and reactions shown as illustrated characters *[shown_working]*
- Mini crossword and calendar — Daily crossword and archive of past editions *[shown_working]*
- Image-to-video experiments — Runway animated explainers in exploration *[planned]*

**Flow:** Open PWA as guest or Google sign-in → Receive 3-5 stories → Swipe, read, watch or listen → Open Receipts to inspect sources → React in Your Jar → Play crossword, see caught-up message → Browse earlier editions via calendar

**Prompt:** Cal Hacks Third Overall: Google eyewear per member; no track-specific text. General judging: application, intentionality, functionality, creativity, technical complexity.
**Fit (none):** General-purpose consumer product; no track targeted.  *(targeted: Cal Hacks: Third Overall)*
**Sponsor tools:** Apify (custom News Receipts Actor for retrieval, core); Claude (editorial selection and validation, core); Cartesia (narration, supporting)
**AI:** Claude evaluates evidence, selects stories, writes explanations and storyboards under structured validation; Recraft images; Cartesia voice; Runway video experiments.
**Architecture:** Next.js PWA on Vercel with Firebase Auth/Firestore; Apify Actor retrieval feeds Claude pipeline; assets reused across stored editions.
**Novelty:** Finite daily edition with source-evidence view and a character-based mood journal instead of an engagement feed.
**Scope:** large · working: Live Vercel demo; repo 31k LOC estimate with tests, Docker, CI. · polish: Original visual identity, PWA gestures, illustrated characters; no video.
**Gaps:** No video; Video generation described only as exploration
Sources: https://devpost.com/software/half-full, https://github.com/rainazab/half-full (evidence file), https://cal-hacks-13-0.devpost.com/

---

### muselet
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Cal Hacks Best Solo Hack

**What it is:** A push-to-talk voice agent that operates macOS entirely on Apple Silicon. A tiny fine-tuned router handles simple commands instantly, while a local planner drives apps through accessibility, OCR and a ghost cursor and verifies each outcome.
**Problem / user:** Power users and people who find mouse and keyboard hard, who want a computer-use agent that is fast and does not stream their screen to a cloud model.

**Features**
- Push-to-talk on-device speech to text — Hold right Option; Parakeet TDT v2 runs on the Neural Engine via FluidAudio with streaming partial transcripts. *[shown_working]*
- Fine-tuned instant router — Qwen3.5-4B LoRA scores 43 options (OS skills plus multi-step, ask, refuse, answer) in one forward pass, about 60 ms. *[shown_working]*
- Local planner for multi-step tasks — Qwen3.5-4B picks one UI tool per turn from accessibility tree and on-device OCR observations, then replans if the goal is unmet. *[shown_working]*
- Ghost cursor and mascot bubbles — A cursor flies to each target before the click so intent is visible; replies are bubbles of 12 words or fewer. *[shown_working]*
- Vision grounding fallback — eyes-4b with two-stage zoom, capped at 1 MP, used when the accessibility tree is blind. *[claimed]*
- Outcome verification — Checks fresh screen state after each action and never trusts a DONE signal alone. *[claimed]*
- Safety gates — Spoken confirmation before send, delete, buy, post or shell; ambiguity triggers ask; destructive requests are refused. *[claimed]*
- Task demos across apps and web — Timers, notes, messages, browser shopping without checkout, Premiere Pro speed changes; README says live reliability is still being validated. *[shown_working]*

**Flow:** Hold right Option and speak → Router decides skill, planner, ask or refuse → Single commands run instantly; others go to the planner → Ghost cursor moves to target and the action executes → System checks the screen and replans if needed → Risky actions ask for spoken confirmation → Short text bubble reports the result

**Prompt:** Cal Hacks Best Solo Hack: no public brief; prize name only, awarded to an individual entrant.
**Fit (implied):** Single-author system covering speech, a trained router, a planner, grounding and a Swift app. Fit is inferred from the entry being solo.  *(targeted: Cal Hacks Best Solo Hack)*
**Sponsor tools:** Tinker (Fine-tuning the router LoRA, core); MLX (Local 4-bit model inference on Apple Silicon, core); Claude / Devin / OpenAI (Listed tools; likely coding help or data generation, role unclear, unclear)
**AI:** Local-only stack: Parakeet STT, a LoRA-tuned Qwen3.5-4B router trained on synthetic noisy utterances with soft labels from a larger Qwen teacher and judge audits, a base Qwen3.5-4B planner, eyes-4b grounder.
**Architecture:** Swift menu-bar app (HandsKit) captures speech and acts on the OS, talking over localhost WebSocket to a Python MLX brain with router, planner and grounder; actions prefer native skill, then accessibility, keys, pixel click.
**Novelty:** Fully on-device computer-use agent with a trained fast router splitting instant commands from planned ones, reported benchmarks and a hermetic regression suite; about 90k LOC solo.
**Scope:** large · working: Large repo with tests; README demos app tasks, but says live Premiere and finance task validation is pending and planner LoRA is not used in the demo. · polish: Architecture diagram, mascot, screenshots, detailed README and eval reporting.
**Claims:** Router ~60 ms median and 94.5 percent accuracy on route_v2 | Fine-tuning cost under $150 of Tinker compute | Two-stage zoom lifted grounding from 36.0 to 63.5 percent on a 200-sample ScreenSpot-Pro subset | Zero cloud inference | First action lands about 190 ms after key release (README)
**Gaps:** No video or demo link; Setup instructions not checked in README tail; Official prize text not found
Sources: https://devpost.com/software/museles, evidence/cal-hacks-cal-hacks-13-0-2026-muselet.json (README)

---

### Orbit Health
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Cal Hacks Best Planet-First Social Impact Hack

**What it is:** A village health-post system for rural Zambia: a pod with camera, microphone, speaker and pulse oximeter runs a nurse-style voice triage in the patient's language, turns findings into supply orders, and a satellite-aware planner routes deliveries around floods.
**Problem / user:** Rural patients and health workers in Zambia where clinics run out of malaria drugs and rain cuts villages off; also district planners who manage supply distribution.

**Features**
- Voice triage pod — Grok Voice transcribes the patient's language; questions follow a nurse order (danger signs, history, relevant follow-ups) capped at seven steps; 'nothing found' is allowed. *[shown_working]*
- Camera and oximeter signs — Camera bursts read visual cues and a finger oximeter records vitals; serious signs must persist over three bursts, with a smile test and second-model review for stroke. *[claimed]*
- Clinical decision layer — Jev scores 96 findings from the transcript each turn and names a condition only with strong evidence; Claude only words questions, advice and handover notes. *[claimed]*
- Automatic supply orders and live delivery map — Each condition triggers orders shipped from the post shelf, a neighbor or the Chipata hub; SpacetimeDB reducers move deliveries every second. *[shown_working]*
- Flood-aware distribution planner — Ranks and batches shipments into multi-stop runs and checks legs against rain, river and NASA flood data, rerouting every ten minutes, including to motorbike or boat. *[shown_working]*
- Global village map — 23,206 villages found by counting 4.3 million roofs in satellite imagery, each openable in Google Earth. *[claimed]*
- Mosquito listener — Uses Oxford HumBug wingbeat models to identify species and raise a village's malaria likelihood. *[claimed]*
- Village dialect learning and voice cloning — Learns local vocabulary and with consent clones a patient's voice for that village; Chewa and Nyanja voices are planned. *[claimed]*

**Flow:** Patient speaks to the pod in their language → Pod asks danger-sign then history questions while camera and oximeter read signs → Decision layer scores findings or reports nothing found → Pod orders the needed supplies and Claude drafts advice and handover note → Order appears as a delivery on the live map from nearest stock → Planner batches and routes it around floods and picks a vehicle → Crisis scenario with 26 needy posts is replanned in about 30 seconds

**Prompt:** Cal Hacks Best Planet-First Social Impact Hack: no public brief found; prize name only.
**Fit (implied):** Targets rural healthcare access under climate-driven flooding using satellite weather and flood data. Link to the prize is inferred from the theme.  *(targeted: Cal Hacks Best Planet-First Social Impact Hack)*
**Sponsor tools:** SpacetimeDB (17-table backend, reducers, live subscriptions and scheduled delivery tick, core); Claude (Wording of questions, advice, handover notes and second opinions on camera signs, supporting); Grok Voice (xAI) (Speech to text and streamed text to speech, core); Jev (TypeSafe) (Clinical scoring of transcript findings, core)
**AI:** Grok Voice for speech, grok-4-fast and a 61-trait camera analysis for vision, Jev for clinical scoring, Claude restricted to wording; a TensorFlow classifier for mosquito sounds and terrain cost maps.
**Architecture:** Next.js 15 app (22 screens, 24 API routes) on SpacetimeDB; Seeed XIAO nRF52840 with pulse sensor and Grove Vision AI camera over USB; planner pulls keyless NASA, Copernicus, ESA, OSM data.
**Novelty:** Joins patient triage hardware with a logistics planner using open satellite data, and reports a large-scale simulation; very broad scope for a single entrant.
**Scope:** large · working: About 56k LOC repo with tests, demo video, Mac app packaging, firmware tested on boards; some satellite data labeled preliminary and drones only proposed. · polish: Plan docs, transparency labels, quantified simulation results, native app packaging.
**Claims:** 841 orders become 83 vehicle movements, saving 112,849 km and 2,044 driving hours (simulation) | 4.3 million roofs counted to map 23,206 villages | Triage turn latency cut from about 16 s to about 3 s | Planner resolves 26-post crisis in about 30 seconds
**Gaps:** Video content not watched (YouTube link only); Repo README is short; features come from Devpost; Official prize text not found
Sources: https://devpost.com/software/orbit-health, evidence/cal-hacks-cal-hacks-13-0-2026-orbit-health.json (README)

---

### Rouge
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Cal Hacks Hacker's Choice

**What it is:** A Windows desktop companion drawn as an animated red ribbon. It can point to and follow on-screen controls, carry out browser tasks through Windows UI Automation, explain errors, search local documents and remind about meetings.
**Problem / user:** People doing everyday work on a Windows PC who want an assistant that acts on the screen they are looking at rather than just talking about their work.

**Features**
- Ribbon pointing — Animated ribbon drawn in Canvas/WebGL wraps the requested control and follows it as the page scrolls; README also supports positional requests like top left without API calls. *[shown_working]*
- Computer agent for browser tasks — Loop of inspect screen via UI Automation, act, verify, report within turn and time limits; example finds cheapest flight on Google Flights and never books. *[claimed]*
- Hotkey explanations — Hold a hotkey over an error, menu or slide to get an on-the-spot explanation. *[claimed]*
- Local document Q&A — Indexes folders of PDFs, Word files and notes with BM25 locally and answers from them. *[claimed]*
- Meeting reminders and conflict flags — Reads timed events from a local calendar file and reminds 15 minutes ahead. *[shown_working]*
- Model routing — A local check sends simple replies to Haiku, lookups and computer use to Sonnet, hard reasoning to Opus. *[claimed]*
- Safety and privacy controls — User's own Anthropic key encrypted at rest, confirmation before send or delete, password and card fields intended to be hidden from the model. *[claimed]*
- Extras: price comparison, lookup, form autofill, file shelf — Listed on Devpost with no detail. *[claimed]*

**Flow:** Type or speak a request to the ribbon → For location questions the ribbon unwinds and circles the control → For tasks the agent drives Chrome via UI Automation and highlights the result → Hold hotkey over content for an explanation → Type stop or close to retract the ribbon

**Prompt:** Cal Hacks Hacker's Choice: peer-voted style award; no brief found, prize name only.
**Fit (none):** No stated connection; the page does not mention the prize beyond being a Cal Hacks entry.  *(targeted: Cal Hacks Hacker's Choice)*
**Sponsor tools:** Anthropic API (Haiku, Sonnet, Opus) (Reasoning and computer-use agent with tiered model routing, core); Serper API (Listed; use not described, unclear)
**AI:** Claude models tiered by task difficulty drive an observe-act-verify loop over Windows UI Automation element text rather than screenshots; BM25 for local retrieval. Devpost also lists a vision model and Qwen3.5 without explaining roles.
**Architecture:** Electron JavaScript shell with Canvas/WebGL ribbon; a persistent PowerShell and C# helper reads UI Automation, clicks, types and watches hotkeys; Anthropic API for reasoning.
**Novelty:** Characterful animated pointer that tracks controls, using accessibility trees instead of screenshots, with measured helper speedups (window lookups 71 ms to 2 ms).
**Scope:** medium · working: About 22k LOC with tests; README labels it early stage with open safety and reliability audit findings. · polish: Animated visual identity and audit docs; no video or demo link, two screenshots.
**Claims:** Idle CPU cut from about 34 to about 7 percent of one core | Window lookups about 35x faster (71 ms to 2 ms) | Old and new helpers gave identical results side by side
**Gaps:** No video or demo; Official prize text not found; Roles of vision model and Qwen unexplained
Sources: https://devpost.com/software/rouge-cm8jig, evidence/cal-hacks-cal-hacks-13-0-2026-rouge-sees-your-screen-and-points-the-way.json (README)

---

### Silent Voice
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Cal Hacks Second Overall [2nd]; [Cartesia] Best Use of Cartesia

**What it is:** Silent-speech system for people without a voice box: the user mouths words to a camera while face-muscle pads are read, and the words are spoken into a normal phone call in their own cloned voice with live captions of the caller.
**Problem / user:** Laryngectomees and their families, whose electrolarynx devices restore sound but not their familiar voice.

**Features**
- Real-time lip reading — Auto-AVSR with trained add-on re-decodes every 100 ms, passes under 40 ms *[claimed]*
- Facial muscle sensing — Four BioAmp pads on Arduino at 1 kHz feed a model fine-tuned on the demo speaker *[claimed]*
- Claude next-word prediction and correction — Haiku forecasts upcoming words; Opus fixes only look-alike swaps *[claimed]*
- Cloned voice into phone call — Cartesia Sonic streams short phrases via Twilio so caller installs nothing *[shown_working]*
- Live caller captions — Cartesia Ink transcribes the caller *[claimed]*
- Emotion carry-through — HSEmotion vs recent baseline makes voice happier or louder *[claimed]*
- Please-repeat fallback — Plays a repeat request instead of guessing when unsure *[claimed]*

**Flow:** Caller speaks on a normal phone line; captions appear → Silent speaker mouths words with pads attached → Lips and muscles combined with language predictions → Each word spoken in cloned voice about 0.7 s later → Unsure words trigger "Please repeat"

**Prompt:** Cartesia "Best Use of Cartesia": prize listed (cash plus Meta glasses TBD), no description. Cal Hacks 2nd Overall: Switch 2 per member. General judging: application, intentionality, functionality, creativity, technical complexity.
**Fit (implied):** Cartesia is the output and caption layer: voice cloning, streaming Sonic speech into a phone call, and Ink transcription of the caller.  *(targeted: Cal Hacks: Second Overall, Cartesia: Best Use of Cartesia)*
**Sponsor tools:** Cartesia (Sonic, Ink, voice cloning) (cloned voice output and caller captions, core); Claude Haiku/Opus (next-word prediction and caption correction, core); Twilio (phone call transport, core)
**AI:** Open-source Auto-AVSR lip reader with face-specific add-on, own EMG model, custom 72M-word dialogue LM, Claude Haiku prediction and Opus correction, HSEmotion for tone.
**Architecture:** Camera and EMG streams feed lip and muscle readers on one RTX laptop; fusion plus LM yields words over ZeroMQ to Cartesia Sonic into Twilio, with dashboard and replay logs.
**Novelty:** Multimodal silent speech (video plus EMG plus LM prediction) output to a live phone call in a cloned voice, with self-reported error rates against a baseline.
**Scope:** large · working: Demo with teammate as speaker; self-reported error rates; repo 30k LOC estimate with tests and CI. · polish: Technical writeup site and hardware rig; not tested with laryngectomees.
**Claims:** Lip reader word error 9.8% vs 20.9% for Auto-AVSR | Muscle model picked correct sentence among 10 look-alikes 72.3% vs 27.7% | Speech starts about 0.7 s after lips move | Built in 36 hours
**Gaps:** No video seen; Results self-reported on one speaker
Sources: https://devpost.com/software/silent-voice-s1f74p, https://github.com/thaimtl/Silent-Voice (evidence file), https://cal-hacks-13-0.devpost.com/

---

### Sophi - The Physical Augmentation Walker
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Cal Hacks First Overall [1st]

**What it is:** Smart walker for older and disabled people with an always-on voice agent, touchscreen, GPS navigation, obstacle sensors with haptics, robotic arms on a linear lift for picking up objects, and a caregiver app showing location and camera.
**Problem / user:** Older adults and people with mobility or vision limits at risk from falls, plus caregivers checking in.

**Features**
- Voice agent — Handle button, Cartesia speech, Claude tool loop fetching sensors, location, weather *[claimed]*
- Robotic arms and lift — SO-101 arms on linear lift open doors and pick up items, driven by iPhone teleop harness *[claimed]*
- Obstacle sensing with haptics — Distance sensors trigger haptic feedback *[claimed]*
- GPS navigation — Voice-started route with map screen *[claimed]*
- Caregiver app — Location, camera check-in, messages, live care circle via SpacetimeDB *[claimed]*
- AI onboarding site — Asks needs and recommends hardware modules *[claimed]*

**Flow:** Press handle button and speak → Speech recognized and sent to Claude agent → Agent calls sensor, location or screen tools → Walker responds by voice, screen, motion → Obstacles trigger haptics → Caregiver checks location and messages

**Prompt:** Cal Hacks First Overall: $3,600 plus laptop per member; no track-specific text. General judging: application, intentionality, functionality, creativity, technical complexity.
**Fit (none):** Integrated physical product spanning hardware, firmware, AI agent, and caregiver software for accessibility.  *(targeted: Cal Hacks: First Overall)*
**Sponsor tools:** Claude (agent reasoning and tool use, core); Cartesia (speech recognition and voice, core); SpacetimeDB (live care-circle membership, supporting)
**AI:** Cloud Claude agent with tool calls over sensors and location; Cartesia STT/TTS; AI-guided module recommendation; custom iPhone-based arm control after GPT harness proved too slow.
**Architecture:** Raspberry Pi 5 with three ESP32 modules for sensors and controls talk to cloud agent; Next.js/Supabase caregiver and onboarding apps.
**Novelty:** Full walker hardware build (30+ printed parts, four soldered boards) with arms and lift rather than a software-only assistive app.
**Scope:** large · working: Claims working integrated prototype; live site; repo 104k LOC estimate with tests and CI. · polish: Onshape CAD, soldered boards, product website.
**Claims:** Won first overall | Connected with a major prosthetics nonprofit
**Gaps:** No video; No quantitative testing; collision avoidance and fall detection not described
Sources: https://devpost.com/software/sophi, https://github.com/mzhao1599/sophi (evidence file), https://cal-hacks-13-0.devpost.com/

---

### Standard Response
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Cal Hacks Best People-First Social Impact Hack; [Microsoft] Built for the Real World (1st), Customer Impact Award (2nd); [Convex] Best use of Convex; [Apify] Best Use of Apify; [Moss] Best Use of Moss; [Anthropic] Claude for Public Benefit

**What it is:** Phone-based evacuation dispatch for people who cannot self-evacuate in wildfires. A voice agent calls every household, pairs residents with nearby drivers, an optimizer builds vehicle plans for dispatcher approval, and residents get callbacks with driver and ETA.
**Problem / user:** Emergency dispatchers and paratransit agencies, and residents needing rides, after failures like the Eaton Fire.

**Features**
- Ready check and neighbor pairing — Calls or signup record needs and pair homes to nearest willing driver within 900 m *[claimed]*
- Mass warning calls — Dispatcher zones or an Apify Actor trigger calls; life threats ranked first *[claimed]*
- ALNS dispatch optimizer — Matches requests to vehicles by seats, wheelchair, stretcher space on OSMnx graph *[shown_working]*
- Driver acceptance and callback — Drivers accept on phones; resident called with name and ETA; unreached homes retried *[claimed]*
- Code-enforced honesty rule — Agent never says help is coming before a driver accepts *[claimed]*
- Multilingual adaptive voice — Cartesia speech in five languages with pace and volume changes *[claimed]*
- Moss policy retrieval — Principles and approved answers retrieved within 80 ms; below 0.7 match says unknown *[shown_working]*
- Dispatcher map and call floor — Homes, crews, fire forecast, road closures, live transcripts *[claimed]*

**Flow:** Ready check collects needs and pairs → Warning triggers calls to every home → Agent records answers and escalates threats → Optimizer builds plans, dispatcher approves → Driver accepts → Resident gets callback with ETA → Unanswered homes texted then field crew

**Prompt:** Microsoft Built for the Real World (1st)/Customer Impact (2nd): prizes only. Convex: use real features like live queries. Apify: meaningful use. Moss: prize listed. Anthropic Claude for Public Benefit and People-First Social Impact: title/prize only. General judging: application, intentionality, functionality, creativity, technical complexity.
**Fit (implied):** Convex is the only inter-service channel; Apify Actor feeds warning calls; Moss serves principles; Claude handles calls; pitched as real emergency agency use.  *(targeted: People-First Social Impact, Microsoft Built for the Real World, Convex Best Use, Apify Best Use, Moss Best Use, Anthropic Claude for Public Benefit)*
**Sponsor tools:** Convex (realtime backend, workflows, scheduled expiry, core); Apify (California evacuation status Actor, core); Moss (policy and principle retrieval, core); Claude Haiku/Sonnet/Opus (extraction, ranking, grading, core); Cartesia (STT and TTS on phone audio, core); Mana (adversarial testing, 29 tests, supporting)
**AI:** Haiku extracts fields and writes replies; Sonnet ranks calls; Opus grades practice calls; Moss retrieval; ALNS optimization with SimPy simulation; promises controlled by code.
**Architecture:** Twilio and Cartesia voice server on Fly.io; Convex backend; ALNS solver service; Next.js app on Vercel; Apify Actor merges Cal OES, CAL FIRE and Caltrans data.
**Novelty:** Pairs voice agent with optimizer, simulation of a real fire night, and code-enforced promise limits; includes a public Apify Actor and self-reported failure analysis.
**Scope:** large · working: Live site, simulation results file, stress tests; repo 96k LOC estimate with tests and Docker. · polish: Public QR demo, evals with reported failures, blog and Actor page.
**Claims:** Simulated: 641 of 662 households on time (97%) vs 6% current process | 200 simulated callers all addresses correct | Moss 61 of 66 questions correct vs none without | Median voice turn 0.86 s
**Gaps:** Pitch video mentioned, no link; Results simulated
Sources: https://devpost.com/software/standard-response, https://github.com/Imhaohao/calhacks (evidence file), https://cal-hacks-13-0.devpost.com/

---

### TouchSpace
*Cal Hacks Cal Hacks 13.0 (2026) · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Anthropic] Claude for Public Benefit

**What it is:** Pipeline that scans an indoor space with an iPhone LiDAR, turns it into a labeled floor plan and route graph, and renders it as raised pins and braille on a Dot Pad tactile display, with a voice assistant answering spatial questions from map data.
**Problem / user:** Blind and visually impaired people who need a sense of indoor layout beyond turn-by-turn directions.

**Features**
- LiDAR room scanning — iOS app uses RoomPlan to capture walls, doors, furniture *[claimed]*
- Landmark labeling and map file — Labels bundled into .touchspacemap with walkable route graph *[claimed]*
- Tactile Dot Pad rendering — 60x40 pin grid shows walls, doorways, landmarks, routes; braille room labels *[claimed]*
- Grounded voice assistant — Claude interprets questions; routes computed by deterministic functions *[claimed]*
- Community map sharing — Upload and download maps via web drive *[claimed]*

**Flow:** Scan room with LiDAR device → Label rooms and landmarks → Generate floor plan and route graph → Share or download map → Open in web app and send to Dot Pad → Explore tactile map and ask voice questions

**Prompt:** Anthropic "Claude for Public Benefit": prize listed as Claude credits and a year of Claude Max plus office hours; no description.
**Fit (implied):** Claude handles free-form questions on accessibility mapping; designed so AI does not plan routes itself.  *(targeted: Anthropic: Claude for Public Benefit)*
**Sponsor tools:** Claude (interpreting spatial questions with tool calls, core); Dot Pad (tactile output hardware, core)
**AI:** Claude interprets spoken questions and calls deterministic functions over map geometry; no AI route planning for safety.
**Architecture:** Swift/RoomPlan app exports maps to FastAPI/SQLite backend; React web app drives Dot Pad via SDK.
**Novelty:** Turns LiDAR scans into tactile maps on a refreshable pin display with grounded AI guidance.
**Scope:** medium · working: Repo 24k LOC estimate with tests; team says end-to-end validation on real devices still pending. · polish: 12 screenshots; no demo link or video.
**Gaps:** No demo or video; No user testing
Sources: https://devpost.com/software/touchspace, https://github.com/holokcheung/touchspace (evidence file), https://cal-hacks-13-0.devpost.com/

---

