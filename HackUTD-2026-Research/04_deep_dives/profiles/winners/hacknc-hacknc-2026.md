# HackNC — HackNC 2026 (10 projects)

### aerodance.
*HackNC HackNC 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** HackNC Frutiger Aero - 1st Place [1st]; [MLH] Best Use of Solana

**What it is:** A Wii-style Frutiger Aero dance game in the browser: one or two players mimic on-screen dancers tracked by webcam or IoT camera and are scored on joint angles. An optional battle mode lets phone-scanning spectators send Solana devnet SOL to dancers, with results minted on-chain and texted via iMessage.
**Problem / user:** Players who want a Just Dance or Kinect-like party game without console hardware, plus spectators who join dance battles from their phones.

**Features**
- Pose-matched dance scoring — MediaPipe landmarks compare arm, leg and body angles to on-screen dancers about every tenth of a second *[shown_working]*
- One or two player mode — Webcam or Wi-Fi IoT camera input; highest points win *[shown_working]*
- 3D Frutiger Aero visuals — Three.js scene with looping glass-skyline drone flight, Wii-style menu sounds and music *[shown_working]*
- QR battle lobby — Display shows a QR code; first phones become dancers, later ones join as crowd *[claimed]*
- Crowd hype payments — Spectators send Solana devnet SOL to dancers mid-dance *[claimed]*
- On-chain results and NFT trophy — Separate Solana service records outcomes and gives the winner an NFT *[claimed]*
- iMessage results — Photon-powered agent texts results to players, phone number acting as wallet identity *[claimed]*
- Dance Studio choreography editor — Docker-hosted tool to record, import, edit and export song bundles *[claimed]*

**Flow:** Open game on display and choose solo, duo or battle → Stand in front of camera → Copy on-screen dancers while scores accrue → Battle: phones scan QR to join as dancer or crowd → Crowd sends SOL during dance → Results written on-chain and texted

**Prompt:** Frutiger Aero: themed HackNC award (1st-2nd) with no description on the page. MLH Best Use of Solana: rewards apps using Solana's fast low-cost transactions, such as games, social apps, DEX or payments prototypes.
**Fit (explicit):** Entire visual identity is Frutiger Aero (glass, skies, Wii menus); Solana used for crowd tipping, on-chain battle results and NFT trophies in a game.  *(targeted: HackNC Frutiger Aero, MLH Best Use of Solana)*
**Sponsor tools:** Solana (Devnet SOL hype transfers, on-chain results, NFT trophies, core); Photon (iMessage agent texting battle results, supporting); Tiger Data (TimescaleDB) (Event hypertable storage, supporting)
**AI:** MediaPipe pose estimation (in-browser and on-device options) feeds rule-based angle scoring; no generative AI.
**Architecture:** React/three.js client with Express and Socket.IO server syncing phones and display, TimescaleDB for events, separate Solana service and iMessage agent, plus Android client and Docker choreography editor.
**Novelty:** Very large scope for a hackathon: game, authoring tool, Android client, e-waste IoT camera input, on-chain tipping and docs on scoring and plans.
**Scope:** large · working: Repo of ~750 files and ~96k LOC (includes temp assets), live site, docs on scoring, video link, Docker and CI. · polish: Detailed docs, sound mixer, quality settings, authoring workflow; tests present.
**Claims:** Scoring sampled every 0.1 seconds | Winner receives NFT trophy
**Gaps:** Unclear how much of docs plan vs implemented; Video not watched
Sources: https://devpost.com/software/aerodance, evidence/hacknc-hacknc-2026-aerodance.json (README), https://hacknc-2026.devpost.com/

---

### Batman
*HackNC HackNC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Photon] Best iMessage Agent - 1st Place [1st]

**What it is:** An iMessage-based safety contact: the user texts a meetup plan, a chosen friend must agree, and Batman then watches Find My location only during that window, sending discreet check-ins and alerting the friend with last location if the user goes silent. Secret code words trigger an excuse or silent alert.
**Problem / user:** People meeting strangers (dates, marketplace pickups, apartment viewings) who want backup without opening a safety app when something goes wrong.

**Features**
- Plan intake over iMessage — User texts plan; bot asks short follow-ups, Claude extracts structured details *[shown_working]*
- Friend consent gate — Monitoring starts only after the chosen friend replies yes *[claimed]*
- Windowed Find My monitoring — Location read only during the meetup window using geofences with hysteresis and speed checks *[claimed]*
- Escalation ladder — Deterministic state machine with SQLite timers: discreet check-ins then alert friend with last location *[claimed]*
- Secret code words — One word gives an excuse to leave, another silently alerts the friend; matched before any model call *[claimed]*
- Risk-adaptive timers — Tighter timers at night or for riskier meetups; GPS outlier rejection *[claimed]*
- Landing page and sign-up — Vite page whose Vercel function assigns a Photon number and SMS link *[shown_working]*

**Flow:** Text Batman the meetup plan → Answer a couple of questions → Friend approves → Batman monitors during window → Receive discreet check-ins if early exit or silent → Friend alerted with location if no reply → Use code word to exit or alert any time

**Prompt:** Photon Best iMessage Agent (1st $400 + credits + interview fast-track): build the best agent that lives in iMessage on Photon; the HackNC page gives no further criteria.
**Fit (explicit):** README says it was built for the Photon Agents in iMessage track; the whole product is an iMessage contact built on Photon's SDK with no app install.  *(targeted: [Photon] Best iMessage Agent)*
**Sponsor tools:** Photon spectrum-ts / Spectrum API (iMessage transport, number assignment, advanced-imessage Find My and Focus data, core)
**AI:** Claude with structured outputs extracts plans and classifies replies; escalation decisions are deterministic code, never model-driven.
**Architecture:** TypeScript Node bot on Fly.io using Photon SDK, advanced-imessage gRPC for location, SQLite/drizzle durable timers; separate Vite landing page with Vercel signup function.
**Novelty:** Safety-first design where LLM never triggers escalation; uses Find My data only during consented window; built with parallel Claude Code subagents.
**Scope:** medium · working: Landing repo (this one) has QA scripts and API tests; bot repo is separate and unread; Devpost reports 1,000+ tests and a live landing page. · polish: Brand guide, motion system, accessibility handling and screenshots/perf checks in the landing repo.
**Claims:** Reply classifier 98.7% accuracy | Code words 100% recall, 0 false positives over about 2,000 messages | 1,000+ tests and evals
**Gaps:** Bot backend repo not read; No video; Accuracy figures unverified
Sources: https://devpost.com/software/batman-cjer91, evidence/hacknc-hacknc-2026-batman.json (landing page README), https://hacknc-2026.devpost.com/

---

### Bazaarly
*HackNC HackNC 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** HackNC General - 3rd Place [3rd]

**What it is:** A React/TypeScript dashboard for pop-up apparel vendors that organizes garment inventory per event, takes Solana Pay devnet checkout, and reports event analytics. Add-ons include a webcam garment scanner that drafts listings with Gemini, an AI sales-advice chat, and Nessie and Snowflake prototypes.
**Problem / user:** Flea-market and pop-up apparel sellers whose inventory, payments, expenses and event earnings sit in different places, making it hard to judge an event or plan the next one.

**Features**
- Per-event inventory — Garments grouped by event with details, photos and stock status; unsold items can be transferred to another event *[shown_working]*
- Solana Pay checkout — Customer display embeds a checkout showing a payment QR; sale recorded only after devnet confirmation (fixed 0.01 SOL demo) *[shown_working]*
- Event analytics — Revenue, ledger, product and category breakdowns, vendor-fee coverage, and comparison of up to four past events *[shown_working]*
- Vision inventory scanner — Webcam scan with hold-still gate; Gemini drafts title, keywords and price; rembg isolates garment, CLIP flags duplicates; vendor approves *[claimed]*
- Ask Bazaarly chat — Floating chat sends compact event summaries to a finance service calling an LLM (mock, Snowflake Cortex or other provider) *[claimed]*
- Nessie dashboard prototype — Simulated Capital One accounts shown as a cash-flow view *[claimed]*
- Snowflake Cortex consultant — Uploaded sales CSV yields revenue, AOV and category mix, then LLM recommendations *[claimed]*

**Flow:** Open Events page and pick an event → Scan garments and approve AI drafts → Customer builds cart and pays via Solana Pay QR → Sale confirmed and logged in ledger → Review event dashboard → Ask Bazaarly for advice or compare past events

**Prompt:** HackNC General track: open category with 1st-3rd hardware prizes plus MLH pins; no theme text.
**Fit (none):** Open track; the entry is a vendor business tool. It also touches Solana, Nessie, Snowflake and Gemini sponsor tools, though only General placement is listed.  *(targeted: HackNC General)*
**Sponsor tools:** Solana Pay (devnet) (Confirmed on-chain checkout, core); Gemini API (Vision descriptions of garments, core); Snowflake Cortex (CSV sales-consultant prototype and optional chat provider, supporting); Nessie (Capital One) (Simulated cash-flow dashboard prototype, supporting)
**AI:** Gemini vision writes structured garment descriptions and price estimates; CLIP embeddings catch duplicates; an LLM (Snowflake Cortex or mock) answers sales questions grounded in computed figures.
**Architecture:** React/Vite dashboard on Firebase/Firestore, separate Solana Pay checkout app, FastAPI vision service, and a Node finance service proxying LLM calls so keys stay off the client.
**Novelty:** Ties reporting strictly to on-chain-confirmed sales and keeps model output alongside vendor edits; spans several repos and sponsor prototypes in one pitch.
**Scope:** medium · working: ~8.6k LOC dashboard repo, README with demo video link and multi-service setup; checkout and vision live in other repos. · polish: Detailed README, honest caveats (devnet, no seller auth); no tests or CI.
**Gaps:** Checkout and vision repos not read; No user testing results
Sources: https://devpost.com/software/bazaarly, evidence/hacknc-hacknc-2026-bazaarly.json (README)

---

### Call me Maybe
*HackNC HackNC 2026 · dataset: winners · tier: track_winner · evidence A · confidence low*
**Prizes:** HackNC Frutiger Aero - 2nd Place [2nd]

**What it is:** The Devpost page is nearly empty, with only a joke tagline and tags for a glb 3D model from Sketchfab. The linked repo's README describes a different main effort, PaperTrade, a paper-trading site with tunable prediction models, while a separate ig-turing/aqua-exe folder holds a React-three-fiber 3D site.
**Problem / user:** Not stated on the Devpost page. The repo README frames PaperTrade for people who want to practise trading crypto, forex and stocks against tunable AI bots with fake money.

**Features**
- Paper trading with live prices — Order ticket fills simulated orders on SOL, forex and large-cap stocks using ingested live prices *[planned]*
- Model Lab — Users tune hyperparameters of prediction models via the UI and see backtests *[planned]*
- AI bot leaderboard — Trained models trade as bots on the same leaderboard as users *[planned]*
- News sentiment — Gemini would score and explain news per asset *[planned]*
- 3D aqua web scene — Separate aqua-exe React/three.js app with GLB model; purpose not documented *[unclear]*

**Flow:** Page documents no demo flow; repo checklist shows a stub backend with fake data and frontend charts under construction

**Prompt:** Frutiger Aero (1st-2nd): themed HackNC award; the official page gives no description of the theme.
**Fit (none):** Devpost only says it placed in the Frutiger Aero track; the repo's aqua-exe 3D app and 'ig-turing' folder suggest a separate aesthetic piece, but this is not explained.  *(targeted: HackNC Frutiger Aero)*
**Sponsor tools:** Tiger Data (Planned main database for PaperTrade, unclear); Gemini / Snowflake / Solana / ElevenLabs / Nessie / Photon (Listed in README as intended sponsor tracks, no evidence of use, unclear)
**AI:** README plans LightGBM/scikit-learn price-prediction models with backtests and Gemini news sentiment; status unverified.
**Architecture:** README plan: ingest workers write prices to a database, FastAPI trading engine, ML service for models, Next.js frontend following a shared API contract; stub backend returns hardcoded data.
**Novelty:** Winning entry is documented only by a joke tagline and a 3D model tag; the repo appears to contain a larger separate trading-game plan.
**Scope:** small · working: Live Vercel demo link exists but content could not be read; README checklist shows mostly unchecked items. · polish: Unknown for the submitted piece; repo has ~125 files and ~8.9k LOC including a 3D app.
**Gaps:** Devpost has no descriptive text; README may not describe the submitted piece; Live demo unreadable (JS app); ig-turing folder not documented
Sources: https://devpost.com/software/call-me-maybe-3da9ky, evidence/hacknc-hacknc-2026-call-me-maybe.json (README), https://hacknc-2026.devpost.com/

---

### CampusSync
*HackNC HackNC 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** HackNC Beginner - 3rd Place [3rd]

**What it is:** A native iOS app for UNC Chapel Hill students that shows when friends are free, imports a class schedule, lets users post plans and join clubs, and puts a free-now answer on Home and Lock Screen widgets. It syncs through Firebase and works offline via a local cache.
**Problem / user:** First-year and other college students who struggle to find mutual free time, discover clubs and keep track of meetings and dues across posters and group chats.

**Features**
- Mutual free-time view — Timetable, Friends overlay and free gaps computed from imported schedules; shows who is free now *[shown_working]*
- Schedule import — Reads a ConnectCarolina class-schedule PDF for review, with demo schedule fallback *[shown_working]*
- Invites — Post a food, study, fitness or social plan to chosen friends who RSVP; invites expire *[shown_working]*
- Clubs — Club events flagged as fitting or conflicting with classes; join, post events, record dues flag *[shown_working]*
- Classes with ratings — Course list with RateMyProfessors ratings *[claimed]*
- Home and Lock Screen widgets — Widgets read a snapshot saved by the app so they work offline *[shown_working]*
- Demo mode — Toggle swaps in fictional friends and schedules and pins the clock *[shown_working]*

**Flow:** Sign in with verified unc.edu email → Import class schedule PDF → Add friends by handle → See who is free now on Home → Post an invite or browse club events → Check widget on Home or Lock Screen

**Prompt:** HackNC Beginner track: teams self-select Beginner at submission; 1st-3rd hardware prizes (no MLH pin); the page gives no theme or criteria.
**Fit (implied):** Open beginner track; README says it was built by a two-person team for HackNC. No track-specific claims.  *(targeted: HackNC Beginner)*
**AI:** No AI features in the product; Claude was used as a coding aid per Devpost credits.
**Architecture:** SwiftUI views over view models and repository protocols; SwiftData cache with a sync coordinator on Firebase Auth and Firestore snapshot listeners; JSON snapshot via App Group to widget extension.
**Novelty:** Offline-first layered iOS architecture with widgets and a safe demo mode; unusually well documented for a beginner-track entry.
**Scope:** medium · working: ~15.6k LOC Swift app, Firebase rules folder, 7 screenshots; no video or live link. · polish: Architecture diagram, docs folder, tests present, widgets and demo mode.
**Gaps:** No video; Rest of README past architecture section truncated
Sources: https://devpost.com/software/campussync-orcwq3, evidence/hacknc-hacknc-2026-campussync.json (README), https://hacknc-2026.devpost.com/

---

### Ebb
*HackNC HackNC 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** HackNC Beginner - 2nd Place [2nd]

**What it is:** A calming smartwatch system for K-12 students with special needs: a LilyGO T-Watch senses agitation from repetitive movement and room loudness against the child's own baseline, then guides breathing and calm mode. An iPhone app, website and iMessage line serve parents and teachers.
**Problem / user:** Children with special needs who get overwhelmed and cannot say so, and the parents and teachers who need consistent calming strategies between home and school.

**Features**
- Stress sensing on watch — Accelerometer movement and loudness levels (no audio stored) compared to a per-child learned normal *[shown_working]*
- Stepped response — Breathing buzz, then auto calm mode, then needs-an-adult alert after a minute of agitation *[shown_working]*
- Calm mode — Nature scene footage, breathing circle, sound, vibration and spoken phrases in AI or parent-cloned voice *[shown_working]*
- Learning loop — Thompson sampling picks scenes per time of day; teacher ratings tune sensitivity; outcome measured as agitation drop *[claimed]*
- Parent app setup — QR pairing, assessment turned into a Gemini calm profile, parent approval, weekly scenes *[shown_working]*
- Teacher tools and dashboards — Start or stop calm, rate moments, journal notes, live graph, heatmap, AI weekly report *[claimed]*
- iMessage line — Parents and teachers text Ebb questions and notes via a Photon bridge *[claimed]*

**Flow:** Parent pairs watch by QR in iPhone app → Completes assessment and approves calm profile → Watch monitors child → Buzz cue then calm mode starts → Child checks in with a face → Teacher rates moment and adds notes → Adults review insights or text Ebb

**Prompt:** HackNC Beginner track: teams self-select Beginner at submission; 1st-3rd hardware prizes (no MLH pin); the page gives no theme or criteria.
**Fit (implied):** Open beginner track; project is a hardware-software accessibility product. It also uses Photon, ElevenLabs and Gemini sponsor tools without a stated sponsor prize.  *(targeted: HackNC Beginner)*
**Sponsor tools:** Gemini API (Calm profile generation, weekly reports, messaging replies, core); ElevenLabs (Calm voice and parent voice cloning, core); Photon (iMessage line for parents and teachers, supporting)
**AI:** Gemini turns assessments into profiles and weekly reports; ElevenLabs voices; per-child z-score baselines and Thompson sampling plus empirical-Bayes risk forecast are statistical, not LLM.
**Architecture:** ESP32-S3 watch polls Supabase Edge Functions over HTTPS; Supabase Postgres with row-level security and realtime serves SwiftUI app and Lovable website; Photon bridge on a Mac relays iMessage.
**Novelty:** Full closed-loop hardware product across firmware, app, web, backend and messaging in a weekend, with privacy design (no audio, name scrubbing) and bandit-based personalisation.
**Scope:** large · working: ~11.6k LOC across firmware, Supabase functions, iOS app and web; tested end to end on the watch per Devpost; demo video and website. · polish: Detailed README with architecture, security review fixes, tests present, public site.
**Claims:** Closed loop tested end to end on real watch hardware | Security review found and fixed an iMessage impersonation issue
**Gaps:** Video not watched; No accuracy or clinical figures
Sources: https://devpost.com/software/ebb-36zbl2, evidence/hacknc-hacknc-2026-ebb.json (README), https://hacknc-2026.devpost.com/

---

### Klane
*HackNC HackNC 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** HackNC General - 2nd Place [2nd]

**What it is:** A lead-finding research agent for tradespeople. A contractor sets a trade and territory, and Klane searches public news, permits, procurement notices and announcements, filters them for relevance and currentness, plots prospects on a map with evidence dossiers, and models bid economics. The same agent is reachable by iMessage.
**Problem / user:** Contractors such as roofers who spend evenings combing permit portals and announcements for future work before any contractor request is posted.

**Features**
- Bounded public-source research — Gemini with Google Search grounding runs up to three batches, showing early results while more arrive *[shown_working]*
- Candidate filtering — Checks trade relevance, currentness, source support, physical location, competing contractors and expired bids *[claimed]*
- Company dossiers — Dated indicators, titled evidence links, proposed scope, timing and published contact research *[shown_working]*
- Job economics model — Editable materials, labor, equipment, overhead, reserve, break-even bid and timeline assumptions *[claimed]*
- Voice search and briefings — ElevenLabs Scribe transcription and spoken briefings *[claimed]*
- Account-aware iMessage agent — Photon Spectrum maps verified senders to saved profiles for the same research *[claimed]*
- Permit analytics warehouse — Tiger Cloud outbox syncs to Snowflake holding 2,000 Raleigh permit records *[claimed]*
- Approval-gated outreach — Recipient and message must be reviewed before sending *[claimed]*

**Flow:** Choose demo profile or set trade and territory → Prompt by text, voice or iMessage → See early prospects on globe-to-map view → Open a company dossier → Adjust job assumptions to see bids → Ask follow-ups, save prospects, approve outreach

**Prompt:** HackNC General track: open category with 1st-3rd prizes plus MLH pins; no theme text.
**Fit (implied):** README says its Carolina blue and Frutiger Aero look; it was also submitted to several sponsor tracks (Photon, Snowflake, Tiger Data, ElevenLabs, Gemini) per Devpost, but placed in General.  *(targeted: HackNC General)*
**Sponsor tools:** Gemini API (Grounded discovery, extraction, chat and estimates, core); Photon Spectrum (iMessage agent, core); ElevenLabs (Speech-to-text and spoken briefings, supporting); Tiger Data (Tiger Cloud) (Operational database, core); Snowflake (Warehouse of permit records, supporting)
**AI:** Gemini with Google Search grounding discovers and extracts prospects in capped batches; filters check evidence; chat and estimates are account-aware. ElevenLabs handles voice.
**Architecture:** React/Vite/MapLibre front end over a Node HTTP server with Zod validation holding credentials, orchestrating Gemini research, ElevenLabs, Photon, a Tiger Cloud Postgres outbox synced to Snowflake.
**Novelty:** Treats evidence conservatively (withholds unsupported prices and stale leads) and links web, voice and iMessage surfaces to one backend with a database-to-warehouse flow.
**Scope:** medium · working: Server, shared and src dirs with tests (~400 LOC counted), YouTube demo, local demo mode with profiles; no hosted demo. · polish: Globe-to-map design, README with screenshots, Vitest tests, honest caveats.
**Claims:** Each discovery run targets five qualified buyers | Warehouse loaded with 2,000 City of Raleigh permit records
**Gaps:** loc_estimate in evidence looks low (406) relative to file count; No hosted demo; Video not watched
Sources: https://devpost.com/software/klane, evidence/hacknc-hacknc-2026-klane.json (README), https://hacknc-2026.devpost.com/

---

### Phish Finder
*HackNC HackNC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Photon] Best iMessage Agent - 2nd Place [2nd]

**What it is:** An iMessage agent that takes a forwarded suspicious link, opens it in an isolated cloud browser that mimics an iPhone, gathers evidence from threat feeds and domain data, and texts back a screenshot, a four-way verdict and plain-English reasons. A web report page shows full evidence and scan history.
**Problem / user:** Everyday people, especially family members less comfortable with tech, who receive scam texts and risk tapping the link to find out if it is real.

**Features**
- iMessage intake — User forwards a suspicious text or QR photo; bot acknowledges and extracts the link *[shown_working]*
- Sandboxed page visit — Playwright Chromium in Docker looks only, never types or downloads, with private-address blocking and egress firewall *[shown_working]*
- Evidence collection — Google Safe Browsing, URLhaus, OpenPhish, RDAP domain age and Tranco ranking plus page form signals *[shown_working]*
- Points-table verdict — Dangerous, Suspicious, No red flags found or Couldn't check; never labelled safe *[shown_working]*
- Plain-language explanation — Gemini writes reasons with a six-second limit; verdict never depends on it *[shown_working]*
- Live dashboard and report page — React page streams scan steps, shows evidence and history with a rendered link preview image *[shown_working]*
- Family mode — Guardian alerted when a protected person gets a dangerous scam *[planned]*

**Flow:** Forward suspicious text to Phish Finder on iMessage → Receive acknowledgement → Sandbox opens link on cloud VM → Evidence scored → About 20 seconds later get screenshot, verdict and reasons → Open the full report link

**Prompt:** Photon Best iMessage Agent (1st $400 + credits; 2nd $200 + credits): build the best agent that lives in iMessage on Photon; HackNC page gives no further criteria.
**Fit (explicit):** Whole product is an iMessage agent built on Photon Spectrum: forward a scam text, receive an investigated verdict inside the chat.  *(targeted: [Photon] Best iMessage Agent)*
**Sponsor tools:** Photon Spectrum (iMessage gateway in and out, core); Gemini API (Plain-English explanations and screenshot reading, supporting)
**AI:** Verdict comes from a deterministic points table over threat-feed and domain evidence; Gemini only writes explanations and reads user-sent screenshots.
**Architecture:** TypeScript Photon gateway, Python FastAPI analyzer driving sandboxed Playwright Chromium, React report site behind Caddy, all on one Google Cloud VM.
**Novelty:** Safety-minded design: never claims a link is safe, defangs links, reports a no-blocklist column in its accuracy table and keeps LLM out of the verdict.
**Scope:** medium · working: ~15k LOC in three services with Docker and tests; accuracy doc reports a deployed run and a demo video exists. · polish: Frutiger Aero report UI, safety section, accuracy documentation.
**Claims:** 10 of 10 recent scam links flagged Dangerous or Suspicious | 5 of 5 real sites returned no red flags | Median 9.8 seconds per check
**Gaps:** Small test set; Video not watched
Sources: https://devpost.com/software/phish-finder, evidence/hacknc-hacknc-2026-phish-finder.json (README), https://hacknc-2026.devpost.com/

---

### Scrub+
*HackNC HackNC 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** HackNC General - 1st Place [1st]

**What it is:** A browser-based touchless viewer for 3D CT scans controlled by webcam hand gestures and a wake-word voice copilot. It renders a real liver CT with segmentation, lets the user move a cutting plane, measures margins and vessel intersections, and runs a geometric optimizer. A virtual aortic stent-graft sizing demo is included.
**Problem / user:** Scrubbed-in surgeons who cannot touch a mouse or keyboard and must direct an assistant to navigate scans; also positioned for clinical trainees as an educational prototype.

**Features**
- Gesture control — MediaPipe 21-landmark hand tracking: open palm moves cutting plane, pinch rotates, two fingers measure, fist locks, two-hand pinch zooms *[shown_working]*
- Voice copilot — Wake word then commands via Web Speech API to locate, highlight, measure and frame anatomy; optional Gemini or Claude interprets loose phrasing *[shown_working]*
- Planning metrics — Remnant volume, tumor margin by distance transform, vessel intersections computed live from voxel masks *[shown_working]*
- Cut optimizer — Evaluates 3,751 nearby cutting-plane candidates against chosen constraints *[shown_working]*
- Save, compare, restore plans — Stores hypothetical cut plans for side-by-side comparison *[claimed]*
- Aortic stent-graft demo — Simplified sizing, positioning and flow calculations *[claimed]*
- Own scan import — Loads NIfTI CT into browser with measurements where masks exist *[claimed]*

**Flow:** Open web app with preloaded liver CT → Control view with hand gestures on webcam → Say wake word and ask for anatomy views or measurements → Adjust cutting plane while metrics update → Run optimizer, compare or restore saved plans → Optionally import own NIfTI scan

**Prompt:** HackNC General track: open category with 1st-3rd hardware prizes plus MLH pins; no theme text.
**Fit (implied):** Open track; entry is a healthcare/sterile-field interface prototype. README notes v1 won the HackNC overall 1st.  *(targeted: HackNC General)*
**Sponsor tools:** Gemini API (Optional interpretation of unstructured voice requests, supporting)
**AI:** MediaPipe hand tracking with a small synthetic-data-trained network for overlapping fingers; Web Speech parser plus optional LLM maps requests to actions; geometry engine computes all numbers. Repo v2 adds distilled Nemotron agent and VISTA-3D.
**Architecture:** TypeScript/Vite/three.js WebGL volume renderer with GLSL; Python preprocessing (nibabel, scikit-image, TotalSegmentator) on MSD liver data; voxel-based geometry engine feeds metrics.
**Novelty:** Real CT volume rendering with live margin and vessel computation driven by webcam gestures. Repo has since grown into a v2 for a later Nebius x NVIDIA event, so repo and Devpost differ.
**Scope:** large · working: Hosted app, ~31k LOC across 325 files with tests and Docker, video and documented metrics for the later v2. · polish: Landing page, in-app tutorial, docs and results tables; measured check scripts.
**Claims:** Optimizer raised tumor margin from 6.3 mm to 10.2 mm and cut vessel intersections from two to zero in one test | 3,751 candidate cutting planes evaluated | Repo v2: distilled 9B agent reaches 75.8% task success on 256 held-out commands
**Gaps:** README documents v2 built later for another event, so features beyond the Devpost list may not be in the HackNC submission; Video not watched
Sources: https://devpost.com/software/scrub-d67fm5, evidence/hacknc-hacknc-2026-scrub.json (README, describes v2), https://hacknc-2026.devpost.com/

---

### Speak Up
*HackNC HackNC 2026 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** HackNC Beginner - 1st Place [1st]

**What it is:** A gamified impromptu-speaking trainer: the user picks a debate-style prompt category, chooses yes or no, speaks aloud, and receives a score with targeted feedback. A deterministic rubric computes the score while AI analyses the speech.
**Problem / user:** People who communicate mostly by text and want practice responding aloud without preparation, in a debate-style format that keeps them coming back.

**Features**
- Prompt and side selection — User chooses a category and takes the yes or no side of a prompt *[shown_working]*
- Spoken speech recording — The floor-is-yours step captures the speech for analysis *[shown_working]*
- Scored results — Deterministic rubric based on published research gives a score after each speech *[claimed]*
- Targeted feedback — AI turns the recording analysis into specific suggestions for the next attempt *[claimed]*
- Community reactions — Backend feature for audience reactions, the team's hardest piece *[unclear]*
- Distinct visual personality — Custom interface style and theme *[claimed]*

**Flow:** Choose an option on the home page → Pick a category → Pick yes or no side → Deliver the speech → View score and feedback

**Prompt:** HackNC Beginner track: teams self-select Beginner; 1st-3rd hardware prizes; the page gives no theme or criteria.
**Fit (implied):** Open beginner track; a small full-stack web app.  *(targeted: HackNC Beginner)*
**AI:** AI analyses the recorded speech and writes feedback while code computes scores from a research-informed rubric; model unspecified.
**Architecture:** Web frontend with Python/TypeScript backend and Postgres (PL/pgSQL) database, containerised and hosted on Fly.io.
**Novelty:** Separates AI analysis from scoring so scores are deterministic; debate-prompt gamification for speaking practice.
**Scope:** small · working: Live Fly.io demo is linked but returned no readable content; no repo or video. · polish: Devpost text only, no screenshots verified.
**Gaps:** No repository; Live demo content not readable; Model and speech-to-text method not stated
Sources: https://devpost.com/software/speak-up-4ofanr, https://hacknc-2026.devpost.com/

---

