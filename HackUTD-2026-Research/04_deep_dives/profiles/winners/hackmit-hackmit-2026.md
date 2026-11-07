# HackMIT — HackMIT 2026 (31 projects)

### btw
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: META - 3RD PLACE - BRINGING PEOPLE CLOSER TOGETHER WITH AI [3rd]

**What it is:** A family game app where every member answers the same prompt each level with a photo, voice note or text; a level clears only when everyone responds, building streaks and a path to a chosen reward. Built in Expo for mobile and web.
**Problem / user:** Families, especially grandparents and students far from home, who put off calling; the app gives a shared nudge.

**Features**
- Shared level prompts — Everyone gets the same prompt and level clears only when all answer *[claimed]*
- Photo, voice and text answers — Capture screen records response into shared feed *[claimed]*
- Path and rewards — Level map, streaks, reward family picks; missed period resets level *[claimed]*
- Reminders — Nudges members who have not answered *[claimed]*
- Drawn avatars and family join — Draw face, create or join family *[claimed]*
- AI-generated prompts and titles — Meta model personalizes prompts from family media; OpenAI writes home titles *[claimed]*
- Demo-data mode — Runs without keys; live mode via Supabase *[shown_working]*

**Flow:** Hold smiley to start → Create or join family and draw avatar → See level prompt → Answer with photo, voice or text → Family feed shows answers and reactions → Level clears when all answer

**Prompt:** not public / not found
**Fit (explicit):** Targets connecting distant family members; says Meta models personalize prompts from shared media.  *(targeted: Meta: Bringing People Closer Together with AI (3rd), OpenAI: The Fifth Teammate, Dropbox, Cognition: Best use of Devin)*
**Sponsor tools:** Meta model (Analyze family media and generate prompts, supporting); OpenAI (Generate home page titles, token); Devin/coding agents (Development help, token)
**AI:** LLM-generated personalized prompts from family photos, text and voice, plus generated titles.
**Architecture:** Expo/React Native app with react-web, Supabase backend and Vercel hosting; api folder for AI calls.
**Novelty:** Reciprocal gating (nobody advances alone) and hand-drawn Procreate design for multigenerational users; first hackathon team.
**Scope:** medium · working: Deployed web app link and demo video; README lists full screen set and runs on demo data. · polish: Hand-drawn assets, 54 asset files, phone-frame web layout.
**Claims:** Team surveyed people to confirm need
**Gaps:** Meta challenge text not found
Sources: https://plume.hackmit.org/project/eelwb-vsngo-fgsei-tovgv, https://github.com/trishz1230/hackmit-2026 (evidence file)

---

### Burrow
*HackMIT HackMIT 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** WINNER: EDUCATION TRACK WINNER

**What it is:** A Chrome extension in which an animated rabbit ('Bunny') sits on every page, reads the page, talks by voice, points at elements, and offers Socratic hints when it detects the student is stuck without giving final answers. A per-student knowledge graph carries memory across tabs and days.
**Problem / user:** Students whose AI tutors are a separate tab that hands out answers; Bunny works in-page, steps in proactively and keeps long-horizon study memory.

**Features**
- Page understanding — Content script builds a compact semantic model of headings, text, controls, errors and quiz state; raw DOM is never sent to the model. *[shown_working]*
- Voice conversation — Deepgram Flux streaming STT and TTS through a local server, with barge-in so speaking over Bunny stops it. *[shown_working]*
- Pointing and acting — Highlight ring and beam to elements; about 25 schema-validated actions (click, type, scroll, navigate) are verified after execution; risky actions need confirmation. *[shown_working]*
- Struggle detection — Local signals such as repeated wrong answers or dead buttons escalate from a glance to a bubble to speech, offering a hint. *[shown_working]*
- Answer-safe coaching — Hint ladder nudge to direct help; server compares against the true answer, retries once, and swaps in a safe hint if the model leaks. *[claimed]*
- Persistent learner model — Per-student concept knowledge graph tracks mastery and what helped; recalls past mistakes across sites; a parent dashboard reads it. *[claimed]*
- Offline rule-based fallback — If server or LLM is unreachable, a deterministic brain still points, clicks and gives hints. *[shown_working]*
- Raspberry Pi monitor and math animations — A 7-inch Pi display gives proactive help on handwritten work; manim-style animations explain math or CS videos. *[claimed]*

**Flow:** Install extension; Bunny appears bottom-right on every page → Student works, e.g. on an algebra quiz → Bunny notices repeated wrong answers and offers a hint → Student accepts by voice → Bunny points at the answer box and gives a nudge → Student succeeds and Bunny congratulates

**Prompt:** not public / not found
**Fit (explicit):** Plume lists these sponsor challenges for the project. Education: a study companion; Deepgram: full-duplex voice via Flux STT/TTS; OpenAI: GPT-based agent loop. Prompt texts not found.  *(targeted: Education Track, Deepgram: Build Something Worth Talking To, OpenAI: The Fifth Teammate, Long Lake: Convince a Non-Believer)*
**Sponsor tools:** Deepgram Flux STT/TTS (Streaming voice in and out with barge-in, core); OpenAI (model named gpt-6-astra) (Agent decisions and interventions with strict JSON schema, core)
**AI:** OpenAI model runs a bounded observe-decide-execute-verify loop with structured actions; hard prompt constraints plus server-side answer-leak check; local non-model signals detect struggle; knowledge graph memory.
**Architecture:** MV3 extension (content script, background worker, offscreen audio) talks to a local Node server proxying OpenAI and Deepgram WebSockets; shared action schema; demo LMS pages; Pi display add-on.
**Novelty:** Proactive, in-page tutor that can operate pages, with answer-leak guard and cross-site learner memory; physical Pi display companion.
**Scope:** large · working: About 40k LOC repo with Playwright smoke test, demo site, docs and setup steps; Devpost-style page links code and a video. · polish: Detailed README with architecture, custom sprites and onboarding page; manual test checklist.
**Claims:** About 25 validated browser actions | Server catches answer leaks and substitutes a safe hint | Used by the team to oversee its own submission
**Gaps:** No official track or sponsor challenge text found; Video not watched; README names the project Bunny and lists an Education Hack win; Knowledge graph and Pi features not confirmed in README excerpt
Sources: https://plume.hackmit.org/project/iecbs-pgvcb-vklxe-bfbtl, evidence/hackmit-hackmit-2026-burrow.json

---

### camp
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: RAMP - 1ST PLACE - SAVE TIME. SAVE MONEY [1st]

**What it is:** Workplace lunch ordering with native Mac (notch panel) and iPhone (Live Activity) apps and a FastAPI recommender backend. It suggests meals from history, preferences and calendar, supports craving search, and batches coworkers' orders to split delivery fees.
**Problem / user:** Office workers who lose time in lunch and coffee lines and want frictionless ordering with shared delivery costs.

**Features**
- Personalized recommendations — Backend filters and scores menu items using order history, preferences and calendar availability *[claimed]*
- Craving search — OpenAI API matches described cravings to real menu items and prices to avoid invented results *[claimed]*
- Group order batching — Coworkers choosing the same restaurant are grouped to share delivery fee *[claimed]*
- Mac notch panel — AppKit panel in the notch shows current order *[claimed]*
- iPhone Live Activity — ActivityKit keeps the order visible and synced; background updates need APNs *[claimed]*
- Ramp sandbox spending — Integrates Ramp sandbox for spend management *[claimed]*
- Works without LLM key — Recommendation path runs without OpenAI key *[shown_working]*

**Flow:** Backend started locally → Mac app connects to service → App suggests meals or user types a craving → Coworkers' same-restaurant orders get grouped → Order tracked on notch panel and iPhone Live Activity

**Prompt:** not public / not found
**Fit (implied):** Saves time by recommending and ordering at the desk and saves money by pooling delivery fees; Ramp sandbox integration is mentioned.  *(targeted: Ramp: Save Time. Save Money. (1st), Visa: Reimagine Shopping, OpenAI: The Fifth Teammate)*
**Sponsor tools:** Ramp sandbox (Spend management integration, supporting); OpenAI API (Natural-language menu search, supporting)
**AI:** LLM matches free-text cravings to catalog menu items; recommender itself is a scoring/ranking algorithm with feedback adaptation.
**Architecture:** Swift Mac and iOS apps sync with a Python FastAPI backend storing profiles, groups, orders; catalog, ranker and batching logic in backend.
**Novelty:** Native notch UI and Live Activities across two Apple platforms; README honestly marks checkout and payment as not connected.
**Scope:** large · working: About 17.6k LOC, tests present, runbooks; end-to-end prototype across Mac, iPhone and backend per writeup. · polish: Extensive docs set (app guide, demo runbook, architecture, validation notes) and demo video.
**Claims:** Working end-to-end prototype across Mac, iPhone and backend
**Gaps:** Ramp challenge text not found; Menu prices estimated; no real checkout
Sources: https://plume.hackmit.org/project/froib-urbmc-nphhn-ugmor, https://github.com/harryyuncheng/camp (evidence file)

---

### CareChair
*HackMIT HackMIT 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** WINNER: OVERALL TRACK 3RD PLACE; SPONSOR WINNER: OPENAI - 1ST PLACE - THE FIFTH TEAMMATE; SPONSOR WINNER: DIMENSIONAL - WINNER - BEST USE OF DIMENSIONAL; SPONSOR WINNER: ASUS - 1ST PLACE - ASUS / ZENNI CLAW CHALLENGE [3rd]

**What it is:** A wheelchair-mounted robotic caregiver prototype: two robot arms, a RealSense camera, Arduino sensors and a voice/care dashboard. The demo shows body-aware bathing motions plus feeding and medication flows, with AI intents validated before reaching the robots.
**Problem / user:** Elderly and disabled people and overstretched caregivers facing a growing care gap and high cost of in-home and facility care.

**Features**
- Body-aware bathing — MediaPipe pose, RANSAC and RealSense depth build a 3D body model; custom path planner generates scrub motions for arm regions *[claimed]*
- Voice interface — Deepgram Nova-3 speech-to-text and Aura-2 text-to-speech *[claimed]*
- Validated agent layer — Meta and OpenAI models turn requests into structured intents; every command checked before robot execution *[claimed]*
- Care dashboard — Node.js/browser UI unifying voice, robot tasks, sensors and activity status *[claimed]*
- 3D avatar progress view — Avatar mirrors user pose and erases cleaned regions as the robot covers them *[claimed]*
- Arduino sensing — Buttons and sensors via SerialPort and server-sent events to the frontend *[claimed]*
- Feeding and medication demos — Animations and assistance flows for eating and medication *[claimed]*
- Context compression — The Token Company compresses long care context before model calls *[claimed]*

**Flow:** User speaks a care request → Deepgram transcribes, AI maps to structured intent → Command validated against allowed skills → Cameras model body and assign regions to arms → Arms perform task while avatar shows progress → Dashboard shows vitals and status

**Prompt:** not public / not found
**Fit (explicit):** Writeup has a Sponsor Technologies section mapping each sponsor to a role: Arduino sensing, Deepgram voice, Meta intents, OpenAI reasoning, Token Company compression, Dimensional skill abstraction, ASUS GX10 compute.  *(targeted: ASUS / Zenni Claw Challenge (1st), Dimensional: Best Use of Dimensional, OpenAI: The Fifth Teammate (1st), Overall track 3rd, Meta, Deepgram, The Token Company, Arduino)*
**Sponsor tools:** Deepgram (STT and TTS voice interface, core); ASUS Ascent GX10 (Local compute for vision and dashboard, supporting); Dimensional (Expose robot capabilities as bounded skills, unclear); OpenAI (Higher-level reasoning in agent, supporting); Meta model (Intent parsing, supporting); The Token Company (Context compression, supporting); Arduino (Sensors and buttons, supporting)
**AI:** LLM intent parsing into structured actions with a validation gate; MediaPipe pose plus RANSAC geometry for body model; classical path generation for arms.
**Architecture:** Python robotics and vision stack drives two arms using RealSense data; Node.js backend bridges Arduino over SerialPort and serves SSE/API to browser dashboard with 3D avatar.
**Novelty:** Physical caregiving robot on a wheelchair with sponsor integrations spanning hardware and agent layers; ambitious multi-hardware scope.
**Scope:** large · working: Physical prototype with two arms, camera and sensors; demo video linked; bathing, feeding, medication demonstrated per writeup. · polish: Unified dashboard with 3D avatar animations; long detailed writeup.
**Claims:** Built multi-arm wheelchair platform in one hackathon | Bathing motion uses real body model rather than fixed animation
**Gaps:** Sponsor challenge text not found
Sources: https://plume.hackmit.org/project/yjrfb-ddfqs-evmsq-zfhgi, https://github.com/25tyler/Wheelgentic (evidence file)

---

### CFO-Sabbatical
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: MAXIMOR AI - 2ND PLACE - OFFICE OF THE CFO AGENT CHALLENGE [2nd]

**What it is:** A set of AI agents that perform finance-office tasks for a demo company: ingesting invoices from Gmail and Stripe, deciding which to pay this week, chasing customer debts, reconciling bank and accounting records, and producing a 13-week cash forecast. Includes a visual harness showing agent collaboration.
**Problem / user:** Finance teams (Office of the CFO) doing manual accounts payable, receivables, reconciliation and cash forecasting.

**Features**
- Accounts payable triage — Reads invoices from Gmail/Stripe and decides which to pay this week versus later *[claimed]*
- Receivables follow-up — Tracks customer payments via Stripe and Gmail and messages those who have not paid *[claimed]*
- Reconciliation — Checks bank records against accounting records *[claimed]*
- Recurring payment tracking — Detects recurring payments and debts across months *[claimed]*
- 13-week cash forecast — Estimates inflows and outflows from recurring items *[claimed]*
- 15-agent harness — Agents in four sectors communicate through a harness with observability view (consolidated from 43) *[shown_working]*
- Explainer website — Vercel site showing each agent's capabilities and saved demo results *[shown_working]*

**Flow:** Sample invoices enter the inbox → Agents process records → AP and AR agents act → Harness shows agent messages → Month-end report and forecast produced

**Prompt:** not public / not found
**Fit (explicit):** Implements CFO-office functions (payables, receivables, reconciliation, forecasting) as an agent system; Grok used for agents.  *(targeted: Maximor AI: Office of the CFO Agent Challenge (2nd), SpaceXAI: Make It Legendary)*
**Sponsor tools:** Grok (xAI) (Powers the 15 agents, core); Stripe / Gmail (Invoice and payment sources, supporting)
**AI:** Multi-agent system on Grok with a Python finance kernel and bot harness; agents communicate and are observable; deterministic kernel handles finance logic.
**Architecture:** Python finance kernel and demo API, Harness runtime with standing bots, Vite website on Vercel showing saved or live results.
**Novelty:** Agent count cut from 43 to 15; large repo (about 197k LOC counted incl. archives and nested folders) with tests and design docs.
**Scope:** large · working: Kernel CLI, tests, deployed site and YouTube demo; live numbers need local API. · polish: Extensive docs and workshop notes; repo size inflated by archive and generated folders.
**Claims:** Consolidated 43 agents to 15 keeping functionality
**Gaps:** Maximor challenge text not found
Sources: https://plume.hackmit.org/project/zwjij-edzdv-vmitm-apwhq, https://github.com/rohan9314/hackmit26 (evidence file)

---

### ClashMIT
*HackMIT HackMIT 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** WINNER: ENTERTAINMENT TRACK WINNER

**What it is:** A mobile-browser augmented-reality battle game: players scan their face, pick Mage, Witch or Archer, point the phone camera at another player until their face locks, and shout spell names to cast fireballs, poison clouds or skeleton armies over the live camera view.
**Problem / user:** Hackathon attendees stuck at laptops; the game gets them moving, meeting people and playing together in real space.

**Features**
- Join by link with face scan — Open a URL, allow camera and mic, enter a name; app scans the player's face once with no install. *[shown_working]*
- On-device face recognition targeting — SCRFD detector and ArcFace recognizer via ONNX Runtime Web in a Web Worker lock onto an opponent's face; video stays on the phone. *[shown_working]*
- Upper-face fallback signature — A second eyes-only signature is stored at scan time and used when the lower face is hidden by the held phone. *[shown_working]*
- Voice-cast spells — Web Speech API hears words like Fireball or Skeletons; Three.js renders effects over camera on both phones. *[shown_working]*
- Classes and combat actions — Mage, Witch, Archer with distinct spells; shield block, heal, and hand-swing melee. *[shown_working]*
- Coins, upgrades and leaderboard — Kills earn coins spent on skills at respawn; big-screen leaderboard with join QR code. *[shown_working]*

**Flow:** Open link on phone and allow permissions → Enter name; face scan → Pick a class → Point camera at another player until face locks → Shout a spell → Effects appear on both phones; kills earn coins → Respawn and buy upgrades; watch the leaderboard

**Prompt:** not public / not found
**Fit (explicit):** Plume lists these challenges. Meta fit: face-to-face multiplayer play. Entertainment: a game used live at the event. Prompt texts not found.  *(targeted: Entertainment Track, Meta: Bringing People Closer Together With AI, OpenAI: The Fifth Teammate, SpaceXAI: Make It Legendary)*
**AI:** On-device computer vision: SCRFD face detection and ArcFace face recognition in the browser; voice recognition via Web Speech API for spell casting. No LLM described.
**Architecture:** Mobile web client (JavaScript, Three.js, MediaPipe/ONNX in a worker) connects over WebSocket to a Node game server holding arena state; face signatures sent once, small state updates broadcast.
**Novelty:** Face-as-targeting-key AR game running entirely in a phone browser, with an eyes-only recognition fallback for the held-phone viewing angle.
**Scope:** large · working: Hosted at clashmit.lol with a Node/WebSocket server; repo about 42k LOC with tests and CI; page says hackers played it at the venue. · polish: Docs on hosting, tunnel troubleshooting, Docker, CI; big-screen leaderboard with QR.
**Claims:** Video never leaves the phone | Runs entirely in the mobile browser with nothing to install | Kept hackers chasing each other around the venue
**Gaps:** No official track or sponsor challenge text found; Video not watched; README is mostly team workflow and tunnel setup
Sources: https://plume.hackmit.org/project/knges-yhnky-svuti-xmpdm, evidence/hackmit-hackmit-2026-clashmit.json

---

### ClubHub
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: DROPBOX - 2ND PLACE - TURN DIGITAL CHAOS INTO SOMETHING USEFUL [2nd]

**What it is:** A club discovery site for students: describe your goals and get a ranked, reasoned shortlist shown as an interactive graph, with upcoming events pulled from clubs' posters via Dropbox. Pilot uses University of Toronto club data.
**Problem / user:** New university students overwhelmed by hundreds of clubs and scattered event info on posters and PDFs.

**Features**
- Goal-based matching — Free-text goals embedded with Voyage AI and matched against club embeddings in ChromaDB, with a reason per club *[claimed]*
- Interactive graph view — Shows how user interests connect to clubs and concurrent events *[claimed]*
- Explore tab — Browse other interests without changing personal graph *[claimed]*
- Poster-to-event ingestion — Club uploads poster/PDF to Dropbox; Claude extracts event details and links back to source file *[claimed]*
- Club summaries — Claude summarizes club data scraped from U of T portal *[claimed]*

**Flow:** Student types goals → App returns ranked clubs with reasons in a graph → Student views clubs and concurrent events → Club drops a poster in Dropbox → Backend extracts and posts structured event

**Prompt:** not public / not found
**Fit (explicit):** Turns unstructured posters and PDFs dropped into Dropbox into structured, traceable event listings.  *(targeted: Dropbox: Turn Digital Chaos Into Something Useful (2nd), Ramp, The Token Company)*
**Sponsor tools:** Dropbox (Live update flow for club posters/PDFs, core); Claude (Summaries and poster extraction, core); Voyage AI (Embeddings for matching, core)
**AI:** Embedding retrieval over club descriptions plus Claude for summarization, reasoned matches, and multimodal event extraction from posters.
**Architecture:** React/Vite frontend, FastAPI backend with SQLite and ChromaDB; Dropbox watcher feeds extraction pipeline.
**Novelty:** Graph view instead of list and live Dropbox-driven event refresh.
**Scope:** medium · working: Detailed README, 13k LOC, tests; no live link or video on Plume. · polish: Long README with problem framing; agent config files present.
**Gaps:** Dropbox challenge text not found
Sources: https://plume.hackmit.org/project/caruu-rcnjn-yzrse-akiwz, https://github.com/hdave07/ClubHub (evidence file)

---

### DonoRex
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: GIVECAMPUS - 1ST PLACE + GRAND PRIZE - FUNDRAISING / CONSTITUENT INTELLIGENCE CHALLENGE [1st]

**What it is:** A fundraising planner for university advancement teams: it scores alumni/donors from real constituent data and builds a ranked weekly action queue within a staff time budget, with an evidence-based reason on each card and an optional Microsoft 365 autopilot that drafts outreach for approval.
**Problem / user:** Advancement officers who can make only about 149 meaningful donor touches a week and choose whom to contact by gut feel.

**Features**
- Weekly action queue — Pipeline scores ~20,000 constituents and optimizes a ranked list of who to contact, action, channel and minutes under a time budget *[shown_working]*
- Donor labeling — Flags lapsing donors such as LYBUNT/SYBUNT patterns *[claimed]*
- Explanations — Constituent detail pages show timeline, score breakdown and why-this-action evidence *[claimed]*
- CSV export — Weekly plan exports to CSV *[claimed]*
- Strategy comparison and segments — Natural-language template queries produce segment tables *[claimed]*
- Tuesday Autopilot — Microsoft Graph OAuth drafts follow-ups, finds calendar slots, creates tasks; nothing sends without human approval *[claimed]*

**Flow:** Ingest hackathon CSV data → Set weekly time budget and click Build my week → Review ranked queue with evidence → Open constituent detail or compare strategies → Export CSV or run Autopilot to draft emails for approval

**Prompt:** not public / not found
**Fit (explicit):** README and writeup say it was built for the GiveCampus challenge: prioritizes constituents under real staff-hour constraints with transparent reasoning.  *(targeted: GiveCampus: Fundraising / Constituent Intelligence Challenge (1st + grand prize))*
**Sponsor tools:** GiveCampus dataset (Real constituent data for scoring, core); Microsoft 365 Graph (Autopilot mail and calendar drafts, supporting)
**AI:** Mostly deterministic heuristics and optimization for scoring and queue building (chosen for speed and explainability); autopilot drafting of outreach; NL segment templates.
**Architecture:** TypeScript monorepo: core engine package, m365 integration package with OAuth/approval/audit, Next.js web app with API routes over precomputed profile JSON.
**Novelty:** Emphasizes time-budget constrained optimization and approval-gated automation rather than an LLM chat over donor data.
**Scope:** medium · working: README with five-minute judge demo script, unit tests, ingest and dev commands. · polish: Presentation folder, vertical slices design, CSV export.
**Claims:** Handles about 20,000 constituents with precomputed explainability | Demo path followable by judges in about five minutes
**Gaps:** GiveCampus challenge text not found
Sources: https://plume.hackmit.org/project/cxnvv-kmhmt-hktyj-zuygs, https://github.com/latoriaa13/HackMIT_Dropbox (evidence file)

---

### Elute
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: OPENAI - 2ND PLACE - THE FIFTH TEAMMATE; SPONSOR WINNER: REGENERON - GRAND PRIZE - MAKE CLINICAL TRIALS AND BIOSTATISTICS BETTER!

**What it is:** An agentic drug-repurposing appraisal tool: given a drug-disease pair it queries Open Targets, ClinicalTrials.gov and PubMed through ToolUniverse, labels each link of the mechanism by evidence strength using deterministic rules, and shows the strongest case against, the weakest link and the next question to answer.
**Problem / user:** Translational scientists and drug developers who risk spending years and large sums on hypotheses resting on a chain of weak or inherited assumptions.

**Features**
- Ten-step appraisal pipeline — Decomposes a drug-disease request into mechanism, trial history, literature and safety steps, each routed to a specific tool and emitted as a ledger entry. *[shown_working]*
- ToolUniverse tool routing with fallbacks — Calls Open Targets, ClinicalTrials.gov and PubMed tools; on failure falls back to direct APIs (GraphQL, v2, Europe PMC) and logs it. *[shown_working]*
- Deterministic claim grading — Seven claims (mechanism, relevance, exposure, engagement, biology, benefit, safety) labeled established, contested, single-source, unknown or refuted by fixed rules, not the LLM. *[shown_working]*
- Case-against-first output — Shows strongest objections, weakest link, unresolved assumptions, and the next experiment or question, without recommending a decision. *[shown_working]*
- Historical as-of backtest — Dated evidence is filtered by cutoff so the nilotinib-for-Parkinson's case can be rerun as of before the 2019 trial. *[shown_working]*
- Provenance ledger — Every label traces to a tool call, query, record and publication date for auditing. *[shown_working]*
- Fixture mode and live pathway panel — App runs without keys on curated fixtures; pathway panel queries Open Targets and Reactome in the browser. *[shown_working]*

**Flow:** Enter a condition, drug or drug-condition pair → Watch the reasoning trace step through tool calls → See evidence labeled by strength with sources → Read strongest case for and against and the weakest link → Rerun at an earlier cutoff date → See the suggested next question

**Prompt:** Regeneron: make clinical trials and biostatistics better, with a starter kit for an agentic clinical AI orchestrator that turns a scientific request into steps across tools (as described on the project page). OpenAI: The Fifth Teammate (text not found).
**Fit (explicit):** Page says it directly satisfies the Regeneron starter kit idea of turning a high-level scientific request into sequential tool steps; README says it was built for the Regeneron challenge. OpenAI used for extraction and wording.  *(targeted: Regeneron: Make Clinical Trials and Biostatistics Better (grand prize), OpenAI: The Fifth Teammate (2nd))*
**Sponsor tools:** ToolUniverse (Harvard) (Open Targets, ClinicalTrials and PubMed tool calls, core); OpenAI (Structured extraction from abstracts, query reformulation, final explanation wording, supporting)
**AI:** OpenAI extracts structured study facts and writes the explanation; a deterministic rule engine grades claims and picks the weakest link; agent reformulates failed searches and falls back to direct APIs.
**Architecture:** React/Vite frontend over a DataSource seam (fixtures or API); FastAPI backend with ToolUniverse pipeline, canonicalize, dedup, temporal filter, claim engine, OpenAI synthesis, SSE ledger stream.
**Novelty:** Separates retrieval from judgment, makes evidence-as-of-date a computation, and is built around showing the case against with a nilotinib backtest.
**Scope:** large · working: About 18k LOC, 119 offline backend tests, fixture and live modes, PRD v2.2; page says full flow works end to end. · polish: Detailed README, design docs, Regeneron starter sheets folder, video link, deployable static bundle.
**Claims:** 119 backend tests run offline on recorded cassettes | Nilotinib objections were visible before the 2019 trial began | Uses more than three distinct ToolUniverse tools
**Gaps:** No official Regeneron or OpenAI challenge text fetched; Video not watched; Page lists six sponsor challenges; only two won
Sources: https://plume.hackmit.org/project/afzbr-ptgza-tcorl-mrobb, evidence/hackmit-hackmit-2026-elute.json

---

### Erbgut
*HackMIT HackMIT 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** WINNER: SUSTAINABILITY TRACK WINNER

**What it is:** A simulation and tuning tool for DNA data storage: for a chosen sequencing channel it switches each coding rule and the redundancy level on and off, measures what pays off, trains a risk model on decoder failures to pick the safest strand, and uses a small CNN decoder on top of classical alignment.
**Problem / user:** Engineers archiving data in DNA, who use fixed hand-written rules (no homopolymers, GC band) and fixed redundancy that nobody measures per channel, wasting reads and density.

**Features**
- Per-channel rule and redundancy audit — Given sequencing technology, read budget and recovery target, toggles each rule, measures cost and benefit, keeps only what pays off. *[shown_working]*
- Channel simulator — Generates noisy read clusters with substitutions, indels, run-length and context effects, dropouts; calibrated on two public real sequencing datasets. *[shown_working]*
- Fountain-code encoder with risk-scored candidates — Several equivalent candidate strands per slot; a learned risk model picks the one most likely to survive decoding. *[shown_working]*
- Hybrid decoder — Classic alignment plus a 0.8M-parameter CNN correcting residual errors; a 9.6M transformer from scratch failed. *[shown_working]*
- Learned-rules report — Docs show the model rediscovers the homopolymer rule, shifts its threshold and discards the GC rule. *[shown_working]*
- Dashboard, reproduce script and microcontroller demo — Streamlit dashboard, one-command reproduce script, and a hardware folder; page says it runs on a microcontroller. *[claimed]*

**Flow:** Choose sequencing technology, read budget and recovery target → Tool audits each rule and redundancy on held-out seeds → Risk model trained from decoder failures → Pick the cheapest setting that meets the target → See per-rule verdicts and Pareto plot → Reproduce numbers with one script

**Prompt:** not public / not found
**Fit (explicit):** Page frames DNA storage as a lower-energy alternative to conventional storage and the tool as making it cheaper and more reliable. Sponsor challenges listed include Regeneron, Espressif, Arduino, Ramp, ASUS, Elastic, Voloridge; none stated as won.  *(targeted: Sustainability Track)*
**AI:** Small CNN corrects residual errors after classical read alignment; a learned risk model scores candidate strands from decoder failure labels; transformer decoder tried and abandoned.
**Architecture:** Python package dnacodec: channel simulators, Fountain encoder, decoder, risk model, grid search loop with frozen-decoder alternation, Streamlit dashboard, static site and deck, plus hardware folder.
**Novelty:** Measures rather than assumes DNA coding rules per channel and publishes unflattering comparisons and a numbers registry; research-style rather than app-style.
**Scope:** large · working: About 34k LOC with tests and CI, reproduce script, live site and deck; all results simulated, no wet lab validation. · polish: Extensive docs (NUMBERS, COMPARISON, MODELS, ERRORS), pitch deck, logo, dashboard.
**Claims:** Nanopore needs 19.5 reads with the run-length rule vs 24.5 without; tuning cuts it to 5.5 | Illumina: both rules off stores 31 percent more data per letter | Decoder reconstructs 88 percent of strands vs 67 percent classic at 6 reads | Simulator within 3 points of real data
**Gaps:** No official Sustainability track text found; Microcontroller claim not verified in README excerpt; No video link on page
Sources: https://plume.hackmit.org/project/mwrat-butaa-qmvaa-aebuw, evidence/hackmit-hackmit-2026-erbgut.json

---

### FRIDAY
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: OPENAI - 3RD PLACE - THE FIFTH TEAMMATE [3rd]

**What it is:** A furniture shopping and room-design tool where a GPT agent searches a catalogue, checks whether pieces physically fit using a spatial constraint solver, and places them in a 3D room (PlayCanvas) or floor view. Describe a room by text or voice and compare drafts within a budget.
**Problem / user:** Online furniture shoppers who cannot tell if a piece fits their room, clears doorways or fits budget.

**Features**
- Voice or text design brief — Deepgram transcribes speech; request compiled into 13 schema-validated constraint types *[claimed]*
- Constraint-driven catalogue search — Constraints translate into Elasticsearch queries over listings; invalid reasons are explainable (e.g. wall distance clause) *[claimed]*
- Fit solver — Checks object placement on a 5 cm grid with rotations *[claimed]*
- 3D room and floor overlay — PlayCanvas room with three.js floor overlay and top-down view; gaussian-splat data compiled to own grid *[claimed]*
- Design drafts — README: three five-piece bedroom designs within $1,200 demo budget; refine chosen draft by chat *[shown_working]*
- Multi-floor buildings — Per-floor measured boundaries *[claimed]*
- Visa sandbox checkout — Sandbox checkout flow; live signing planned *[claimed]*

**Flow:** Explore prepared 3D room or floor plan → Say or type a design brief and budget → Compare three drafts in the room → Ask for changes such as different sofa or moved lamp → Check out via Visa sandbox

**Prompt:** not public / not found
**Fit (explicit):** README frames FRIDAY as a spatial analysis engine and agent harness where GPT works alongside the user; Elastic for search, Deepgram for voice, Visa for checkout.  *(targeted: OpenAI: The Fifth Teammate (3rd), Ramp, Deepgram, Elastic: Find the Signal, Visa: Reimagine Shopping)*
**Sponsor tools:** OpenAI GPT (Agent that finds furniture, checks fit, edits arrangement, core); Elasticsearch (Catalogue index, core); Deepgram (Real-time voice transcription, supporting); Visa sandbox (Checkout, supporting)
**AI:** GPT agent with tools for catalogue search, fit check and scene manipulation over a compiled constraint language; team also used coding agents in isolated worktrees with Codex reviews.
**Architecture:** React/TS Vite frontend with PlayCanvas and three.js; Django backend with Elasticsearch; shared spatial solver and DSL; room mesh/splat pipelines.
**Novelty:** Compiles speech into a constraint DSL with an exact grid solver instead of free-form LLM placement; very large build (85 PRs, 351 commits claimed).
**Scope:** large · working: About 35k LOC, tests, CI, docs; demo video and Drive links on Plume. · polish: Rich README with design flow; team admits photorealism lighting issues and agent harness not yet connected.
**Claims:** 85 pull requests and 351 commits | 72-card ticket board | Solver covers every placement on 5 cm grid with rotations
**Gaps:** OpenAI challenge text not found
Sources: https://plume.hackmit.org/project/fkbzo-xqhff-jgchs-azula, https://github.com/LeeSinLiang/hackmit2026 (evidence file)

---

### GPU (Graphics Processing Unit (GPU))
*HackMIT HackMIT 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** WINNER: OVERALL TRACK 2ND PLACE [2nd]

**What it is:** A home-built GPU: a RISC-V core extended in Chisel with a warp scheduler and SIMD vector lanes, run on an FPGA at about 2.5 GOPS with display output and host link. Demos include 3D rendering, fluid and particle simulation, LLM inference and DOOM.
**Problem / user:** Hardware-curious builders priced out of GPUs who want to understand GPU architecture from the ground up.

**Features**
- Warp-based RISC-V GPU — Extends open-source RISC-V CPU with warp scheduler and vector lanes; one core up to 64 threads *[shown_working]*
- Custom ISA extensions — Extra RISC-V extensions to manage warps and vector lanes *[claimed]*
- FPGA deployment — Synthesized with Vivado, about 2.5 GOPS *[claimed]*
- Display output and host comms — Drives monitor/TV and talks to host *[claimed]*
- Demo programs — 3D rendering, fluid and particle sims, LLM inference, DOOM compiled for the hardware *[shown_working]*

**Flow:** Compile C or RISC-V programs → Load onto FPGA GPU → Run demos such as 3D render or DOOM → View output on monitor → Observe via visualization

**Prompt:** not public / not found
**Fit (none):** Overall track; no sponsor challenge. Entertainment-flavored demos like DOOM and 3D rendering.  *(targeted: Overall track 2nd place (Entertainment track label))*
**AI:** No AI in the design itself; LLM inference is one demo workload run on the GPU.
**Architecture:** Chisel-described core with warp scheduler and SIMD lanes synthesized in Vivado onto FPGA; compiled programs and a renderer/visualizer on host.
**Novelty:** Actual hardware design and FPGA bring-up with custom ISA extensions within a hackathon, rather than a software app.
**Scope:** large · working: Writeup lists working demos on FPGA; repo has Chisel src, programs, renderer and tests; video linked. · polish: README is two lines; many generated folders.
**Claims:** 2.5 GOPS on FPGA | One core, up to 64 threads
**Gaps:** Overall-track prompt not applicable
Sources: https://plume.hackmit.org/project/xxomh-wwztg-ooipq-hzzbb, https://github.com/arghunter/gpu (evidence file)

---

### Keiko
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: HACKSTER - 2ND PLACE - CREATE WHAT'S NEXT; SPONSOR WINNER: ARDUINO - 1ST PLACE - TOUCH GRASS: BUILD SOMETHING THAT UNDERSTANDS THE REAL WORLD

**What it is:** A homemade piezo hydrophone buoy with microcontroller nodes that streams underwater audio to a pipeline where a custom whale-sound CNN flags detections, feeding a live website, an open detection database, an Elasticsearch dashboard with alerts, and a Claude agent that answers questions in ES|QL.
**Problem / user:** Whale conservationists and researchers; roughly two-thirds of whale deaths attributed to ship strikes and entanglement, which could be avoided if whale locations were known.

**Features**
- DIY hydrophone buoy — Three piezo discs potted in epoxy feed an analog front end into an Arduino UNO Q in an SLA 3D-printed waterproof buoy. *[shown_working]*
- Three interchangeable hardware nodes — UNO Q, ESP32-S3 and nRF7002 DK each sample the ADC and send identical UDP datagrams to the pipeline; UNO Q went in the water. *[shown_working]*
- Whale CNN classifier — 3-second log-mel windows run through a 22-class CNN with abstain rule; consecutive whale windows form an event. Page reports AUROC 0.9816 with 5-fold CV. *[claimed]*
- Live site and open database — Detections with clips and spectrograms are archived to a GitHub Pages site and CSV/JSON dataset. *[shown_working]*
- Elasticsearch search and alerts — Indexes windows and events with geo, vector and ELSER fields, kNN sounds-like search, anomaly job, ES|QL alert for right whale. *[claimed]*
- Claude question agent — ask.py lets Claude write and run ES|QL, kNN or semantic queries over detections. *[claimed]*
- Localization and live map — Central server computes time-difference-of-arrival fixes and tracks and streams them by WebSocket to a map. *[claimed]*

**Flow:** Hydrophone buoy records underwater audio → Node ships samples over UDP → Pipeline windows audio and runs the CNN → Event saved as clip and log line → Site and database updated; Elastic alert fires on right whale → User browses the map or asks questions in natural language

**Prompt:** not public / not found
**Fit (explicit):** README maps each sponsor to a built piece: UNO Q node in the water for Arduino, ESP32-S3 node for Espressif, nRF7002 node for Nordic/Hackster, Elastic indices and agent, Voloridge GPU training with NOAA noise join.  *(targeted: Arduino: Touch Grass (1st), Hackster: Create What's Next (2nd), Espressif, Elastic: Find the Signal, Voloridge: Signal in the Noise)*
**Sponsor tools:** Arduino UNO Q (Hydrophone sampling node deployed in the water, core); Espressif ESP32-S3 (Wideband sampling node over USB or Wi-Fi, supporting); Nordic nRF7002 DK (Third node sampling and Wi-Fi on one chip, supporting); Elasticsearch / Kibana (Detection indices, search, dashboard, anomaly job, alert, core); Voloridge AWS GPU (Larger model training runs and NOAA noise-floor analysis, supporting); Claude (Anthropic API) (Agent that writes ES|QL queries, supporting)
**AI:** Custom ~1.2M-parameter whale CNN (1D and 2D branches, 22 classes) trained on 126k clips from nine public sources; Claude agent for query writing; ELSER semantic search.
**Architecture:** Hydrophone to MCU ADC to UDP datagrams to Python pipeline (CNN, events) fanning out to WAV/JSONL, GitHub Pages archive, TDOA server with WebSocket map, and Elasticsearch plus Kibana.
**Novelty:** Full stack from home-built hydrophone hardware through ML to searchable open data; three different MCU boards on one protocol.
**Scope:** large · working: README documents a node that was put in the water, live site and CSV dataset; about 9.4k LOC code plus training and site; no tests. · polish: Mermaid diagrams, protocol docs, per-sponsor sections, CI, live site keiko.mobylabs.org, video link.
**Claims:** AUROC 0.9816 with 5-fold cross-validation | Trained on a 126k-clip dataset from nine sources | About 15 ms per window on an M-series CPU
**Gaps:** No official sponsor challenge text found; Page says Cape Cod while README says Boston Harbor; location not reconciled; Video not watched; README excerpt truncated
Sources: https://plume.hackmit.org/project/hyfdu-oilyy-yixkb-mlauw, evidence/hackmit-hackmit-2026-keiko.json

---

### Klick
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: META - 1ST PLACE - BRINGING PEOPLE CLOSER TOGETHER WITH AI; SPONSOR WINNER: ESPRESSIF - WINNER - BEST USE OF ESPRESSIF HARDWARE & SOLUTIONS (IN AIOT)

**What it is:** An event-networking system where each attendee gets an AI twin built from a spoken conversation. When two phones or lanyard badges cross paths over Bluetooth, the twins negotiate and, if there is a specific reason to meet, both people are told after both approve.
**Problem / user:** Attendees of large events who walk past the few people worth meeting; directory apps with percent matches go unused.

**Features**
- Twin creation by voice — Deepgram transcribes about 90 seconds of speech; Meta Muse Spark builds a profile of summary, interests and facts; optional LinkedIn PDF or Instagram handle. *[shown_working]*
- Twin transparency controls — 'Everything it knows' screen lets users delete facts or mark topics off limits. *[shown_working]*
- BLE proximity detection — Native Android foreground service advertises and scans an 8-byte random session token, gated on signal strength and deduped per pair. *[shown_working]*
- Twin-to-twin negotiation — Cloud Function claims the pair in a Firestore transaction, runs a multi-turn Muse Spark conversation (four model calls, 12-16 s), returns yes/no and a one-sentence reason. *[shown_working]*
- Double opt-in reveal — Push teaser to both; names appear only after both approve; optional networking mode pre-approves. *[shown_working]*
- Radar and direction arrow — Signal strength shows closeness; arrow estimated from RSSI by gyro heading sector when the user turns in place. *[claimed]*
- ESP32-S3 lanyard badge — BOX-3 (and Waveshare AMOLED port) advertises same token, shows QR pairing, turns matching color, marks done on shake. *[shown_working]*
- Judge dashboard — Live Firestore-fed page of negotiations; dismissed pairings are kept private. *[shown_working]*

**Flow:** Record a short spoken intro to build a twin → Carry phone or wear badge → Pass someone nearby → Twins negotiate in the cloud → Both get a push teaser and approve → Names and reason revealed; badges share a color → Radar helps find each other; shake badge when met

**Prompt:** not public / not found
**Fit (explicit):** README names Meta's challenge as the target and lists Meta, Deepgram, Espressif, The Token Company, Ramp, Long Lake. Meta: Muse Spark twins create in-person introductions; Espressif: ESP32-S3 badge firmware.  *(targeted: Meta: Bringing People Closer Together With AI (1st), Espressif: Best Use of Espressif Hardware (winner), Deepgram, The Token Company, Ramp, Long Lake)*
**Sponsor tools:** Meta Muse Spark (Model API) (Profile extraction and twin negotiation, core); Espressif ESP32-S3 (ESP-IDF) (Lanyard badge with BLE, display and IMU, core); Deepgram (Speech-to-text onboarding and text-to-speech whisper, supporting); The Token Company (Token-cost logging per negotiation (roughly 4-5k tokens each), unclear)
**AI:** Muse Spark via the Anthropic-style API at low reasoning effort; each twin speaks only from its owner's profile and boundaries; four calls per negotiation; proximity gating limits pairs.
**Architecture:** Kotlin Android app and ESP32 badges feed Firebase Cloud Functions v2 and Firestore (match document as single source); FCM push; Deepgram voice; judge dashboard via Firebase Hosting.
**Novelty:** Proximity-triggered agent negotiation with strong guardrails (reason not score, private dismissals), plus custom badge hardware and a body-shadow direction estimate.
**Scope:** large · working: Page states it ran on real phones and badges with live negotiation and push; live judge dashboard; repo about 22k LOC. · polish: Architecture SVG, parametric 3D-printed mount, two badge boards, design notes in CLAUDE.md, video link.
**Claims:** Cost scales with foot traffic, not 499,500 pairings for 1,000 attendees | Negotiation takes about 12 to 16 seconds | Roughly 4,000 to 5,000 tokens per negotiation
**Gaps:** No official sponsor challenge text found; Direction arrow accuracy untested in a crowd per page; Video not watched; README says twins use Muse Spark while repo depends on Anthropic SDK (pointed at Meta API per page)
Sources: https://plume.hackmit.org/project/rwqwq-hqecj-bfxns-lyqyc, evidence/hackmit-hackmit-2026-klick.json

---

### Lil-Vro Model
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: HACKSTER - 3RD PLACE - CREATE WHAT'S NEXT [3rd]

**What it is:** A voice-only Socratic tutor for kids aged 8 to 14, running as a full voice-to-voice pipeline on a laptop and on an ESP32-S3-BOX-3 device, with a parent dashboard showing streaks and mastery. It guides with leading questions rather than giving answers.
**Problem / user:** Children doing schoolwork (mainly STEM) who copy chatbot answers or get pulled into screens; parents wanting progress visibility.

**Features**
- Three tutoring modes — Walkthrough one step at a time, teach-back where the kid explains, mistake mode with a hidden error to catch *[claimed]*
- Spoken math and chemistry handling — Normalizers with 99-symbol lexicon convert speech to notation; renderer turns equations back into natural speech *[claimed]*
- Local speech recognition — faster-whisper/RealtimeSTT keeps raw audio on the laptop *[claimed]*
- Kid-safety guardrails — Rule-based check then AI classifier, fail-closed; answer verification so it will not call wrong answers right *[claimed]*
- Mood-aware tone — Detects frustration or confusion and adjusts replies *[claimed]*
- ESP32 hardware device — Streams 16 kHz audio over Wi-Fi to the server and plays back replies *[claimed]*
- Parent dashboard — Next.js with Supabase auth showing streaks, topics and per-topic mastery *[claimed]*

**Flow:** Child speaks aloud → Local transcription and notation normalizer → OpenAI Socratic reply with mood and mastery tracking → Content filter → Spoken via Deepgram or OpenAI TTS → Session stored; parent views dashboard

**Prompt:** not public / not found
**Fit (implied):** Real ESP32-S3-BOX-3 voice device with Deepgram and OpenAI in the pipeline; built as a physical desk tutor.  *(targeted: Hackster: Create What's Next (3rd), Espressif hardware, Deepgram, The Token Company, OpenAI: The Fifth Teammate, Ramp)*
**Sponsor tools:** Deepgram (Speech streaming and TTS, core); OpenAI (Socratic tutor replies and TTS, core); Espressif ESP32-S3-BOX-3 (Voice hardware endpoint, supporting); Supabase (Session and mastery storage, supporting)
**AI:** Local Whisper STT, custom spoken-math normalizers, OpenAI with Socratic prompting, mood and mastery tracking, content-filter and honesty guardrails.
**Architecture:** Python agent pipeline with STT, normalizer, LLM, filter, renderer and TTS; transport server bridges ESP32 audio; Supabase Postgres with RLS feeds Next.js dashboard.
**Novelty:** Custom spoken-math/chemistry normalization and honesty guardrails in a screenless kid tutor; hardware plus dashboard; entered beginner track.
**Scope:** medium · working: Writeup says end-to-end works on ESP32 hardware; chemistry normalizer 15/15 tests; demo video and site linked. · polish: Unit tests, 8-table schema with RLS, parent dashboard.
**Claims:** 99-symbol math lexicon | Chemistry normalizer 15/15 tests passing
**Gaps:** Hackster challenge text not found
Sources: https://plume.hackmit.org/project/teywu-cadwe-dcfzg-zgcgt, https://github.com/Chaitanya-purohit/lilvro (evidence file)

---

### MathMatch
*HackMIT HackMIT 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** WINNER: BEGINNER TRACK WINNER

**What it is:** A swipe-based math duel web app: players see challenger cards with only a topic, Elo and taunt, swipe right to reveal a problem, then write or dictate a proof that an OpenAI model grades out of 5. Ratings are tracked per topic and friends can duel.
**Problem / user:** Students who lean on AI for answers and lose proof-writing skill; the app trains rigorous explanation through gamified, rated problems.

**Features**
- Swipe arena of problem cards — Cards show topic, Elo and a taunt; right swipe commits and reveals the problem; left flees at a small rating cost; yielding shows the official solution. *[shown_working]*
- AI proof grading — Proof sent to OpenAI Chat Completions (gpt-4o-mini default) with chosen rigor level; scored out of 5, 4 or more counts as solved. *[shown_working]*
- Per-topic Elo ratings — Separate ratings for algebra, combinatorics, geometry, number theory; passing proofs and duels move them; card Elo from HARP level. *[shown_working]*
- Timed duels with friends — Skirmish (5 min), Duel (15 min, ten problems, first past half wins) and 90-minute Boss battle on olympiad proofs; ratings hidden until settled. *[claimed]*
- Voice dictation of proofs — Browser mic clip posted to a server route that calls Deepgram nova-3 and returns text. *[shown_working]*
- Personalized recommender — Star ratings build a taste vector over problem embeddings (content features or trained two-tower model); nearest-Elo candidates are re-ranked. *[shown_working]*
- Training feed — Scrollable feed of problems matched to profile, skip or solve. *[shown_working]*

**Flow:** Open /match and pick topics → Swipe through challenger cards → Swipe right to reveal a problem → Type or dictate a proof → Receive a 0-5 grade and rating change → Add friends and start a timed duel → Rate problems to steer recommendations

**Prompt:** not public / not found
**Fit (explicit):** Plume lists these sponsor challenges. Page says the app was mostly built with Devin step by step, uses OpenAI models for grading and Deepgram for speech; no win recorded beyond the Beginner track.  *(targeted: Beginner Track, Cognition: Best Use of Devin, Deepgram: Build Something Worth Talking To, OpenAI: The Fifth Teammate)*
**Sponsor tools:** Devin (Cognition) (Primary agent building the app step by step, core); OpenAI (Proof grading and development help, core); Deepgram nova-3 (Dictating spoken proofs, supporting)
**AI:** OpenAI chat model grades proofs for rigor out of 5; Deepgram speech-to-text for dictated proofs; content-feature or two-tower PyTorch embeddings for recommendations.
**Architecture:** Next.js app with API routes (/api/grade, /api/transcribe), Neon Postgres for accounts, friends and progress, bundled HARP problem deck, optional PyTorch training pipeline exporting embeddings.
**Novelty:** Combines swipe dating-app mechanics and Elo with AI-graded written proofs, aimed at rigor rather than short answers.
**Scope:** medium · working: Deployed at mathmatch.vercel.app; repo about 7.5k LOC with 500-problem deck, accounts and recommender; no tests. · polish: Clear README with run and training steps, video link, dataset attribution.
**Claims:** Majority of points go to methodology over final answer | Duel is ten problems in 15 minutes | Bundled 4,780 short-answer and 310 proof problems from HARP
**Gaps:** No official Beginner track text found; Video not watched; Page names GPT-5o and 5.6-Terra models, README shows gpt-4o-mini default
Sources: https://plume.hackmit.org/project/givtb-jfvaz-amjmc-dtcuf, evidence/hackmit-hackmit-2026-mathmatch.json

---

### Memory Palace
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: META - 2ND PLACE - BRINGING PEOPLE CLOSER TOGETHER WITH AI [2nd]

**What it is:** A searchable lifelog triggered by brain activity: an EEG spike detector signals when the wearer's signal deviates from their baseline, a phone camera records the next 30 seconds, Meta Muse Spark describes the clip, Elastic indexes it, and an agent answers questions about past moments.
**Problem / user:** People with failing memory (dementia care, reminiscence therapy), students and parents who want an automatic record of moments that stood out.

**Features**
- EEG spike trigger — Per-user baseline from 30-second calibration; peak-to-peak deviation with persistence filter triggers capture; validated on public datasets and EPOC X recordings *[claimed]*
- Capture rig — Python backend commands an Android app (polled every 250 ms) to record H.264 clip; verified on a Samsung S23; ESP camera rig used instead of glasses *[shown_working]*
- Clip description — Meta Muse Spark writes a semantic title and scene description *[claimed]*
- Hybrid search — Jina v5 Omni embeddings via Elastic Inference Service plus BM25 fused by reciprocal rank fusion; filters by date, session, spike intensity *[claimed]*
- Memory carousel and timeline — Color-coded spike intensity; confirm/dismiss labels train the per-user model *[claimed]*
- Memory Guard agent — Muse Spark or Grok agent answers questions with moments as evidence; can share highlights with loved ones *[claimed]*

**Flow:** Wear EEG headset and calibrate 30 seconds → Spike triggers 30-second capture → Clip described and indexed → Review carousel at end of day → Ask Memory Guard a question and open source moment

**Prompt:** not public / not found
**Fit (implied):** Uses Meta Muse Spark to describe clips and share moments with loved ones; Elastic for search; EEG signal as trigger fits signal-in-noise theme.  *(targeted: Meta: Bringing People Closer Together with AI (2nd), Elastic: Find the Signal, Voloridge: Signal in the Noise)*
**Sponsor tools:** Meta Muse Spark (Video clip description and agent model, core); Elastic (with Jina v5 Omni via Inference Service) (Hybrid BM25 plus vector search, core); Grok (Alternative agent model, supporting)
**AI:** EEG deviation detector trained on public datasets with per-user adaptation, multimodal video/text embeddings, LLM captioning and a retrieval agent.
**Architecture:** EEG to Python backend (baseline, spike detection) to LAN command to Android camera app to clip upload; local catalog then Muse Spark description, Jina embedding, Elastic index; Next.js frontend and agent.
**Novelty:** Uses EEG only as a trigger rather than decoding emotion; 30-second calibration versus hours of training; real EEG hardware in the pipeline. Meta glasses were never obtained.
**Scope:** large · working: Phone capture verified on device; end-to-end pipeline described; demo video linked. · polish: Spike-intensity timeline UI; glasses integration not realized.
**Claims:** 30-second calibration replaces roughly three hours across seven days | Channel ablation determined electrode needs
**Gaps:** Meta challenge text not found; Detection accuracy numbers not stated
Sources: https://plume.hackmit.org/project/ekkeo-uldro-ffuzo-fsegk, https://github.com/NamaiBest/MemoryPalace (evidence file)

---

### Money Maxer
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: RAMP - 3RD PLACE - SAVE TIME. SAVE MONEY; SPONSOR WINNER: MAXIMOR AI - 4TH PLACE - OFFICE OF THE CFO AGENT CHALLENGE

**What it is:** An agent finance team for a CFO's office that investigates payment discrepancies such as short-paid invoices, gathers evidence from email, Slack, contracts and CRM, proposes accounting entries checked by a deterministic kernel, and stores human answers as scoped rules so questions are never asked twice.
**Problem / user:** Finance teams who spend time working out why a payment is short, finding the agreement and booking it correctly before statements can be prepared.

**Features**
- Deterministic first-pass reconciliation — Code settles bank matching, multi-invoice payments, fees and FX differences before any model is used. *[shown_working]*
- Tiered investigation agents — Claude Agent SDK model tiers with per-tier budgets search Gmail, Slack, contracts, CRM and bank files via a connector registry. *[shown_working]*
- Verification kernel — Entries go through one controlled write path and are re-performed deterministically on proposal and before posting. *[shown_working]*
- Scoped human memory — A CFO answer is stored with scope and expiry; later eligible credits are prepared with zero model calls. *[shown_working]*
- Rule learning by replay — Historical transactions replayed with human entries hidden; repeated decisions become candidate rules, backtested before approval. *[claimed]*
- Fine-tuned document reader — LoRA-tuned open-weight models (0.6B to 20B) on an ASUS GX10; Qwen3-4B reaches 0.972 field F1 vs 0.958 for best Claude. *[claimed]*
- Auditor pack and QuickBooks mirror — Independent pack re-performs sampled entries; accepted entries mirrored to a QuickBooks sandbox. *[claimed]*

**Flow:** Demo closes a simulated July for a fictional company → Discrepancies detected on the shared ledger → Code and agents investigate and propose entries → Kernel verifies; approvals wait for a person → CFO answers once when stuck; answer becomes a scoped rule → Accepted entries post and mirror to QuickBooks

**Prompt:** not public / not found
**Fit (explicit):** Directly framed as an office-of-the-CFO agent team; README states both prize placements. ASUS GX10 borrowed at the event was used for fine-tuning, matching the ASUS challenge listing.  *(targeted: Ramp: Save Time. Save Money. (3rd), Maximor AI: Office of the CFO Agent Challenge (4th), ASUS / Zenni Claw Challenge)*
**Sponsor tools:** Claude Agent SDK (Investigation agent runtime and tiers, core); ASUS GX10 (LoRA fine-tuning of the document reader, supporting); QuickBooks sandbox (Mirroring accepted entries, supporting)
**AI:** Code-first reconciliation, then tiered Claude and OpenAI agents with tools over connectors; deterministic kernel verifies; LoRA fine-tuned small models extract fields from finance documents; memory compiled into rules.
**Architecture:** TypeScript with SQLite shared ledger and event bus; connectors (Gmail, Slack, CRM, bank files); agent runtime with MCP; kernel checker; learning and audit modules; web workspace; Python fine-tuning.
**Novelty:** Treats agents as untrusted, with a re-performing kernel, scoped expiring memory and an accompanying paper and benchmark (NorthwindBench) for small-model extraction.
**Scope:** large · working: About 42k LOC repo with tests and CI; live demo at money-maxing-mu.vercel.app; simulated company data, no real customer data. · polish: PDF paper, spec and team log, workspace app, workflow diagram, video link.
**Claims:** Fine-tuned reader 0.972 field F1 vs 0.958 best Claude; 70.0% vs 66.7% whole-document match | Qwen3-4B reaches 100% schema validity with no schema in prompt | Remembered credits are prepared with zero model calls
**Gaps:** No official Ramp, Maximor or ASUS challenge text found; Paper and video not read; Trained reader not in main demo per page
Sources: https://plume.hackmit.org/project/nlhtb-gqmiu-yvcyw-pibeg, evidence/hackmit-hackmit-2026-money-maxer.json

---

### Newton's Playground
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: ASUS - 3RD PLACE - ASUS / ZENNI CLAW CHALLENGE [3rd]

**What it is:** An offline physics-learning box: a webcam photographs a printed textbook problem, a local vision model extracts it into a spec, and an interactive simulation opens on a monitor where hand tracking lets the student grab and throw objects while the derivation updates. Runs on an ASUS GX10.
**Problem / user:** Intro physics students who learn from static diagrams and mouse-based simulators.

**Features**
- Photo-to-simulation — Webcam capture; local vision model on GX10 extracts givens into a validated ProblemSpec that opens the matching sim *[claimed]*
- Hand interaction — MediaPipe hand tracking: fist pushes, pinch grabs, throw speed sets launch velocity *[claimed]*
- Nine problem types — Projectiles, inclines, pendulums and 1D collisions plus sandbox and five puzzle levels *[claimed]*
- Derivation and live graphs — KaTeX derivation panel and motion graphs beside simulation *[claimed]*
- Generate and ask — Local LLM invents problems and answers voice questions using BM25 over OpenStax; Deepgram for speech-to-text *[claimed]*
- Physics verification — Closed-form test suite checks engine within 0.58% worst case *[claimed]*
- Ring-light hardware — ESP32-S3 drives NeoPixel ring over MQTT during scans; two-display one-icon launcher *[claimed]*

**Flow:** Tap Take a picture on the 7-inch touchscreen → Webcam scans the printed problem → Simulation opens with derivation and graphs on monitor → Student grabs and throws the object by hand → Student asks follow-up question by voice or requests a new problem

**Prompt:** not public / not found
**Fit (explicit):** All models run locally on the ASUS Ascent GX10 with no cloud calls in the demo path except Deepgram speech-to-text.  *(targeted: ASUS / Zenni Claw Challenge (3rd), Deepgram, OpenAI, Meta, Ramp)*
**Sponsor tools:** ASUS Ascent GX10 (Runs Ollama vision, generation and Q&A models locally, core); Deepgram (Speech-to-text, supporting)
**AI:** Local vision-language model extracts problem specs with a validator that reports repaired numbers; separate local LLM generates problems and answers questions with BM25 retrieval over OpenStax; MediaPipe hand tracking.
**Architecture:** Browser app (TypeScript, Vite, Matter.js, KaTeX); Python service owns webcam, serves MJPEG and landmarks; Ollama on GX10; ESP32 ring light over MQTT.
**Novelty:** Physical camera-to-sim loop with hand grabbing, deterministic engine corrected and verified against closed forms, fully offline rig.
**Scope:** large · working: Two-display rig launches from one icon; verification suite with measured error; no video link on Plume. · polish: Detailed challenge writeup; hardware ring light and touchscreen panel.
**Claims:** Engine within 0.58% of closed forms | Structured problem generation from 31 s to 5.5 s with reasoning off | Deterministic 8.333 ms steps
**Gaps:** ASUS challenge text not found
Sources: https://plume.hackmit.org/project/khvue-bewru-gqjrh-xgwpv, https://github.com/ethannsie/hackMIT26.git (evidence file)

---

### nullMap
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: ELASTIC - 2ND PLACE - FIND THE SIGNAL [2nd]

**What it is:** A web tool where a researcher pastes a study proposal and gets back similar prior papers and ClinicalTrials.gov records, each labeled positive, negative or null, plus power statistics, a topic map and funnel plots. Corpus limited to kidney and circulatory research.
**Problem / user:** Clinical researchers doing literature review, where unpublished or null results are underrepresented (publication bias) and cause duplicated effort and wasted lab spending.

**Features**
- Proposal-to-prior-work search — Embeds the proposal and runs vector search over paper and trial titles/abstracts stored in Elasticsearch to shortlist similar studies *[shown_working]*
- Result-direction classification — An LLM reads each shortlisted report and tags it positive, negative or null; unreported trials get a separate class with a reason *[claimed]*
- Power/necessity statistics — Backend statistics suggest whether the idea is needed or adequately powered and hint at PICO modifications *[claimed]*
- Topic map — Plots the proposal's proximity to neighboring topics *[claimed]*
- Funnel plot — Shown when enough studies with minimum sample size exist *[claimed]*
- Filtering/grouping of results — Grouping and filtering of retrieved studies added in the UI *[claimed]*
- Bulk ingestion pipeline — Scans OpenAlex public S3 parquet snapshot, filters hypertension/kidney scope, embeds with MiniLM, indexes in resumable batches *[shown_working]*

**Flow:** Enter proposal abstract, question and keywords → Vector search shortlists similar papers/trials → LLM labels each as positive, negative, null or unreported → Review verdict buckets and power panel → Inspect topic map and funnel plot

**Prompt:** not public / not found
**Fit (explicit):** Stores OpenAlex and ClinicalTrials.gov records in Elastic Cloud and uses Elasticsearch vector search over embedded titles/abstracts to surface hidden null results among millions of documents.  *(targeted: Elastic: Find the Signal)*
**Sponsor tools:** Elastic Cloud / Elasticsearch (Single index of papers and trials with vector search, core); Voloridge EC2 (Compute to copy and ingest OpenAlex data, supporting); Devin (Late-stage UI and quality-of-life fixes via GitHub, supporting); Cursor (Generating most of the ingest and query code, supporting)
**AI:** Sentence embeddings (MiniLM) for retrieval; an OpenAI LLM reads full texts to classify result direction and extract PICO/statistics; statsmodels computes power and funnel data.
**Architecture:** React/Vite frontend and FastAPI backend; Elasticsearch 9 index fed by a DuckDB/S3 parquet ingest of OpenAlex plus ClinicalTrials.gov; embeddings, LLM classification, stats endpoints; hosted on Vercel.
**Novelty:** Targets publication bias directly by indexing null/unreported results alongside papers, and bundles power analysis and funnel plots; ingestion of a multi-million-record public snapshot is unusually heavy for a first hackathon.
**Scope:** medium · working: Deployed Vercel app; ingest pipeline, API and docs in repo; README says full replacement corpus not yet imported. · polish: User guide, S3 ingestion guide, Docker compose and tests exist; stats panels and map included.
**Claims:** Subset corpus covers about 2 million kidney and circulatory records | OpenAlex API rate limit forced pivot to Elastic-hosted copy
**Gaps:** Official Elastic challenge text not found; No video; Screenshots not counted
Sources: https://plume.hackmit.org/project/cuqqq-zpzje-qzyls-tmbjd, evidence/hackmit-hackmit-2026-nullmap.json

---

### Paw Patrol
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: ASUS - 2ND PLACE - ASUS / ZENNI CLAW CHALLENGE [2nd]

**What it is:** A real-time incident platform that streams a police officer's body-camera video, audio and smartwatch heart rate to dispatch and a hospital view, with AI flagging gunshots and suspect details so officers need not radio them in. Built as three role dashboards.
**Problem / user:** Police officers, dispatchers and emergency medical teams, where an officer under threat must manually radio details and delays reach healthcare responders.

**Features**
- Dispatch dashboard — Shows live officer video, map position and AI alerts; dispatch can route feeds onward *[shown_working]*
- Audio/video threat alerts — YOLO and Whisper in a FastAPI service process camera and mic input; an LLM assesses transcripts for human review and alerts nearby officers *[claimed]*
- Hospital view — Dispatch forwards live audio, video and heart rate so medics can prepare treatment en route *[claimed]*
- Suspect details from footage — Visual pipeline extracts suspect description from live feed instead of officer narration *[claimed]*
- Officer workspace with iPhone/Apple Watch live mode — Phone camera/mic/GPS and watch heart rate feed shared incident state via SQLite and server-sent events *[shown_working]*
- Boston map and 3D models — Mapbox map with GPS positions, Three.js patrol vehicles and anatomical model *[shown_working]*

**Flow:** Officer wears phone and watch as body camera → Live video, audio, GPS and heart rate stream in → AI pipeline flags events and issues alerts → Dispatch reviews context on dashboard → Dispatch routes feed to hospital team

**Prompt:** not public / not found
**Fit (implied):** Listed three sponsor challenges; the writeup does not state how it addressed each. Implied fit: hardware-adjacent wearable sensing plus local and cloud AI inference.  *(targeted: ASUS / Zenni Claw Challenge, OpenAI: The Fifth Teammate, Arduino: Touch Grass)*
**AI:** YOLO vision and Whisper speech-to-text run in a Python service; Ollama, OpenAI or Claude assess transcripts; outputs go to human review before alerts or reports.
**Architecture:** Single Next.js app serving dispatch, officer and hospital roles; FastAPI triage service for YOLO/Whisper; WebRTC for video; incidents in Vercel Blob or local files; SQLite plus SSE for the iPhone/Watch pipeline.
**Novelty:** Combines body video, audio, biometrics and role-based dashboards in one pipeline; hardware plan scrapped so a phone and watch stood in. Repo is large with docs and CI.
**Scope:** large · working: Deployed Vercel site, video demo link, 65k-line repo with tests; README describes synthetic default mode and a live mode. · polish: Multiple runbooks, CI, Docker, docs folder; default demo is synthetic data.
**Gaps:** Official ASUS challenge text not found; Video not viewable
Sources: https://plume.hackmit.org/project/zznsi-rdjii-twguh-prtfz, evidence/hackmit-hackmit-2026-paw-patrol.json

---

### Peel - The tiny lab technician
*HackMIT HackMIT 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** WINNER: OVERALL TRACK 1ST PLACE; SPONSOR WINNER: ELASTIC - 1ST PLACE - FIND THE SIGNAL [1st]

**What it is:** A roughly $100 phone-connected optical dissolution tester plus an AI evidence engine that checks a pill. It reads the bottle label and imprint by vision, measures how the tablet dissolves, and returns a cited verdict against recall and product databases.
**Problem / user:** People and clinics in low-resource settings who cannot tell whether a tablet is genuine; lab dissolution tests cost tens of thousands and imprint or barcode apps check easily faked traits.

**Features**
- Bottle and imprint reading — GPT-4o vision extracts drug, strength, NDC, lot, maker and pill characters, stripping personal details *[shown_working]*
- Optical dissolution instrument — ESP32-S3 drives six LEDs through a vial with stirrer and two light sensors, streaming absorbance each second over USB to phone *[shown_working]*
- Three-way verdict — Passed the screen, needs lab testing, unable to verify, with quality gates for cloudy vial or saturated sensor *[shown_working]*
- Evidence engine — Six-stage pipeline over 22k recalls, 138k NDC products and 84k pills in Elasticsearch plus Firecrawl web search and an Elastic Agent Builder agent *[shown_working]*
- Ask Peel voice agent — Deepgram Voice Agent preloaded with the finished report answers questions about the user's lot *[shown_working]*
- Peel Atlas — 3D knowledge graph linking scans, lots, recalls, regulators and seller reports *[shown_working]*
- Concern reports — Agent drafts a suspicious-medicine report; filed only on user tap *[claimed]*

**Flow:** Photograph bottle → Photograph tablet → Drop tablet in the Peel vial → Phone shows dissolution curve and instant partial report → Fully cited report completes in about a minute → Ask Peel by voice or file a concern report

**Prompt:** not public / not found
**Fit (explicit):** README has a section per sponsor: Elasticsearch is the entire database with hybrid retrieval, recency decay, corroborated lot matching and Agent Builder ES|QL tools; separate notes address each other sponsor.  *(targeted: Overall Track 1st, Elastic: Find the Signal, Dropbox, Voloridge, Cognition/Devin, Espressif, Deepgram, Arduino, Regeneron, Ramp, Long Lake)*
**Sponsor tools:** Elastic Cloud Serverless / Agent Builder (Five indices, hybrid semantic_text search, ES|QL agent tools, web cache, core); Deepgram Voice Agent (Ask Peel voice Q&A on the report, core); Espressif ESP32-S3 / BOX-3 (Instrument sensing and touchscreen face, ESP-NOW link, core); Devin (Built Flutter app and simulated hardware with tests, supporting); Firecrawl (Budgeted live web evidence, supporting)
**AI:** GPT-4o vision for label/imprint; Jina embeddings via Elastic semantic_text; an Elastic agent with ES|QL tools and OpenAI structured output draft the report, then deterministic guardrails override unsupported claims.
**Architecture:** ESP32 sensor board streams JSON over USB to a Flutter Android app; app posts scans to a FastAPI service on Runpod that runs a six-stage pipeline over Elasticsearch, Firecrawl, Agent Builder and OpenAI; Deepgram voice and Atlas served from same backend.
**Novelty:** Rare mix of custom spectroscopic hardware, dissolution chemistry and a guarded retrieval/agent pipeline; evidence overrides the model and reassuring words are filtered. Calibrated reference only for riboflavin.
**Scope:** large · working: Demo video, hardware photos, measured 0.5 s first report and 41 s full report, CI for firmware/backend/mobile. · polish: Figma and Rive animation, mascot, MIT license, detailed READMEs and per-sponsor notes; limited to visible-light drugs.
**Claims:** Parts cost about $100 versus five-figure lab dissolution gear | Cross-checks 22,000 recalls, 138,000 products, 84,000 pills | Warm run: 0.5 s first report, 41 s fully researched | 100+ automated tests from Devin-built simulator and app
**Gaps:** Official sponsor prompt text not found; Video not viewable
Sources: https://plume.hackmit.org/project/qxodw-wgjqk-lidau-dxrpe, evidence/hackmit-hackmit-2026-peel-the-tiny-lab-technician.json

---

### Recall
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: DROPBOX - 1ST PLACE - TURN DIGITAL CHAOS INTO SOMETHING USEFUL [1st]

**What it is:** A dementia-care app where families upload photos and stories, and a voice companion proactively phones the person for gentle reminiscence sessions. Their spoken memories are distilled into a private memory graph that decides what to revisit next.
**Problem / user:** People living with dementia and their families, who lose shared memory and cannot afford frequent reminiscence therapy.

**Features**
- Proactive voice sessions — Browser voice call, morning default and slow tone, asks graduated cues about familiar events; state machine enforces confirmation *[shown_working]*
- Recall Memory Graph — Transcripts become nodes for people, relationships, events and memories with sources and recall history, stored in SQLite and LadybugDB *[shown_working]*
- Family photo collection — Upload photos, keep originals, EXIF dates and GPS, organise into moments, attach written or recorded stories *[shown_working]*
- People, Places and Connections views — Browser face detection groups, map of locations and interactive relationship graph *[shown_working]*
- Family Q&A — Muse Spark answers questions from graph and shared stories with attributed sources *[claimed]*
- Consent gates — Words enter graph only after original-audio playback and confirmation; sharing needs a second confirmation *[claimed]*
- iMessage integration — Linq-based messaging hook mentioned in contributions *[unclear]*

**Flow:** Family onboards and uploads photos and stories → System schedules a call in the morning → Person talks with voice companion about an approved topic → Transcript reviewed and confirmed before saving → Family sees the visual memory graph and adds context

**Prompt:** not public / not found
**Fit (implied):** Turns scattered photos, stories and conversation transcripts into a structured, source-attributed memory graph families can browse. The page does not spell out the Dropbox link.  *(targeted: Dropbox: Turn Digital Chaos Into Something Useful)*
**Sponsor tools:** Deepgram (Speech-to-text and spoken replies in browser calls, core); Meta Muse Spark (Interpret contributions and suggest graph-backed cues, supporting); OpenAI (Optional photo organisation, supporting)
**AI:** Deepgram transcription and TTS; Muse Spark and OpenAI interpret input and propose cues, with a conversation state machine limiting the model to graph-grounded content.
**Architecture:** Next.js/React app; SQLite for storage with LadybugDB graph retrieval; browser audio to Deepgram; in-browser face-api models; Railway hosted.
**Novelty:** Grounded in reminiscence-therapy research, keeps relatives' accounts separate from the patient's confirmed memories, and treats consent and audio playback as design rules.
**Scope:** large · working: Live Railway site, demo video, 40k-line repo with tests and fixtures. · polish: Brand assets, SPECS and EVIDENCE docs, resizable sidebar UI; no CI or Docker.
**Gaps:** Official Dropbox challenge text not found; Video not viewable
Sources: https://plume.hackmit.org/project/cocds-fxbwj-czmjd-uzpbs, evidence/hackmit-hackmit-2026-recall.json

---

### Rumi
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: RAMP - 2ND PLACE - SAVE TIME. SAVE MONEY [2nd]; SPONSOR WINNER: LONG LAKE - WINNER - CONVINCE A NON-BELIEVER

**What it is:** An AI interior-shopping agent that starts from a LiDAR scan of the user's real room, takes taste photos and a budget, finds real furniture listings across stores, and places them in an editable 3D copy of the room with a synced product list and total.
**Problem / user:** People furnishing a room (e.g., a student dorm) who shop, measure and budget separately and cannot see how items fit as a whole before buying.

**Features**
- Room capture — iOS app uses Apple RoomPlan LiDAR to capture walls, doors, windows, furniture and dimensions, then imports into the browser *[shown_working]*
- Editable 3D room — React Three Fiber editor with overhead and first-person views; move or lock objects *[shown_working]*
- Preference intake — User gives inspiration photos, natural-language style, budget and furniture to keep *[shown_working]*
- Real product search — Exa retrieves merchant listings; OpenAI models judge price, dimensions and style *[shown_working]*
- Budget-synced product list — Subtotal updates as selected items are placed in the room *[shown_working]*
- Chat refinement and sessions — Continue conversation with the room as context; saved sessions via Convex *[shown_working]*
- Deterministic checks — Code validates budget, collisions, door swings and room revisions; listed, estimated and unknown dimensions kept separate *[claimed]*

**Flow:** Scan room with iOS app or load sample room → Describe vision, budget and items to keep → Agent searches stores and proposes items → Items appear in the 3D room with running total → Walk through first-person and refine via chat

**Prompt:** not public / not found
**Fit (implied):** Budget-constrained shopping agent that shows total cost and fit before purchase, with model proposals checked by deterministic code. Writeup does not map features to each challenge.  *(targeted: Ramp: Save Time. Save Money., Long Lake: Convince a Non-Believer, Visa: Reimagine Shopping, OpenAI: The Fifth Teammate, Cognition: Best Use of Devin)*
**Sponsor tools:** OpenAI (Codex and models) (Design/search agents, image interpretation, 3D code help, core); Exa (Retrieving merchant product pages, core); Devin (Inspiration upload, streaming progress, product cards, sessions, supporting)
**AI:** OpenAI models interpret photos and requests, plan zones and budget allocation, and rank products; Exa search; Zod schemas validate agent output; deterministic code enforces budget and placement.
**Architecture:** React/TypeScript frontend with Three.js editor; Convex backend and Clerk auth; iOS RoomPlan app transfers geometry; design agent calls Exa then OpenAI; shared Zod contracts link search, planner and renderer.
**Novelty:** Anchors shopping in a measured 3D scan, and models uncertainty in dimensions explicitly; model proposes while code enforces limits.
**Scope:** large · working: Video demo link, 54k-line repo with iOS app, Convex backend, tests and CI. · polish: Docs folder, mermaid architecture, e2e folder; sample room provided.
**Gaps:** Official Ramp and Long Lake prompt text not found; Video not viewable
Sources: https://plume.hackmit.org/project/aajnp-oqnis-ttafi-kbgks, evidence/hackmit-hackmit-2026-rumi.json

---

### Scenar.io
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: ELEVENLABS - 3RD PLACE - ELEVENLABS CHALLENGE [3rd]

**What it is:** A Unity language-learning game where a typed sentence ('Put me in ...') generates a scenario, drops the player into a World Labs 3D Gaussian-splat world, and lets them speak to NPCs that answer by voice while a goal list tracks progress.
**Problem / user:** Language students who can translate but freeze in live conversation and need low-stakes speaking practice.

**Features**
- Sentence-to-scenario — OpenAI Responses structured outputs turn a plain prompt into setting, NPCs and observable learning goals via /v1/scenarios *[claimed]*
- Explorable generated world — Nano Banana reference image expanded by World Labs into a walkable splat world with colliders *[shown_working]*
- Spoken conversation — ElevenLabs speech-to-text and text-to-speech with lip-sync and on-screen subtitles *[shown_working]*
- Goal/quest HUD — List of conversational goals to finish within a time limit or in free play *[shown_working]*
- Globe front end — Low-poly Earth where a place is typed and the camera flies in *[shown_working]*
- Run recording and grading — Orchestrator records runs and grades them *[unclear]*

**Flow:** Finish the sentence naming a place → Globe animation flies to destination → Walk into the generated cafe world → Speak to NPC avatars in target language → Complete goals and see a receipt

**Prompt:** not public / not found
**Fit (implied):** Voice is the core loop: ElevenLabs transcribes the learner and speaks the character's replies in real time. Writeup does not quote the prize text.  *(targeted: ElevenLabs Challenge, OpenAI: The Fifth Teammate)*
**Sponsor tools:** ElevenLabs (Two-way speech STT and TTS for NPC conversation, core); OpenAI Responses API (Scenario generation with structured outputs, core); World Labs (3D splat world generation, supporting)
**AI:** OpenAI structured outputs create scenarios; an LLM 'character brain' drives NPC replies; ElevenLabs STT/TTS; Nano Banana and World Labs generate imagery and worlds.
**Architecture:** Unity 6 client with Wish globe scene and cafe scene; FastAPI orchestrator for scenarios, speech turns and grading; ElevenLabs for audio; WorldLabs splats with generated colliders.
**Novelty:** Mixes generated 3D worlds with voice-first language practice; README says every sentence currently lands in one authored cafe because generation is not yet wired in.
**Scope:** medium · working: Demo videos; end-to-end cafe loop claimed; README admits scenario generation not hooked to the front end. · polish: Procedural low-poly intro, subtitles, HUD; one authored scene.
**Gaps:** Official ElevenLabs prompt text not found; Video not viewable
Sources: https://plume.hackmit.org/project/rpbsx-etzty-tttwk-fhnlt, evidence/hackmit-hackmit-2026-scenar-io.json

---

### Sherlock
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: MAXIMOR AI - 3RD PLACE - OFFICE OF THE CFO AGENT CHALLENGE [3rd]

**What it is:** An AI 'Office of the CFO' for organizations, initially schools. Users upload financial records; a LangGraph team of 22 agent roles investigates discrepancies, reconciles transactions and drafts reports, with exact-cent code doing the math and humans approving decisions.
**Problem / user:** Finance staff and school boards whose records are scattered across spreadsheets and invoices, so problems surface only at audit time.

**Features**
- Document intake and extraction — PDF processing plus a local fine-tuned model extracts records; validation gates entry into the books *[claimed]*
- 22-role agent finance team — CFO agent, four department leads and specialists, each with registered permitted tools, required records and budget *[claimed]*
- Reconciliation checks — Invoice matching, bank reconciliation, payroll and grant tests, and 'receipted with no matching deposit' for inbound money *[claimed]*
- Conversational investigation — Ask questions in plain language; follow agent activity and answer escalations; investigations pause and resume via checkpoints *[claimed]*
- Decision memory — Human decisions become precedents that are rechecked against later periods before reuse *[claimed]*
- Reports — Financial snapshot, board deck, and close pack with traceable calculations *[claimed]*
- Evidence trail — Decision records and source file library with provenance *[claimed]*

**Flow:** Sign in and import spreadsheets or documents → Review extracted records → Ask a question or let agents investigate → Agents cite evidence and Internal Auditor re-checks → Approve or answer escalations → Generate snapshot or board deck

**Prompt:** not public / not found
**Fit (explicit):** Builds a multi-agent finance organization covering treasury, controllership, FP&A and audit, with deterministic accounting and human approval; README names the Maximor track directly.  *(targeted: Maximor AI: Office of the CFO Agent Challenge, Ramp, Long Lake)*
**AI:** LangGraph orchestrates role agents with checkpointing; OpenAI models reason over evidence with scoped tools; a local fine-tuned model handles document extraction; Python modules compute exact amounts.
**Architecture:** Next.js frontend with Supabase auth; FastAPI and SQLite backend storing originals, records and decisions; LangGraph agent registry; extraction service; Docker present.
**Novelty:** Separates model reasoning from accounting arithmetic, adds precedent recheck and explicit 'unable to establish' results; also covers inbound school cash, not only spending.
**Scope:** large · working: Working prototype described with tests; 36k-line repo, Docker; no demo video or live link on page. · polish: Branded UI, guided intake, README detail; prototype does not execute payments.
**Gaps:** Official Maximor prompt text not found; No video
Sources: https://plume.hackmit.org/project/cxwit-mchwb-zrdld-pegqj, evidence/hackmit-hackmit-2026-sherlock.json

---

### SignalHound
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: HACKSTER - 1ST PLACE - CREATE WHAT'S NEXT [1st]

**What it is:** A Unitree Go2 robot dog carrying a Nordic nRF7002-DK that measures Bluetooth signal strength from a person's phone and walks step by step toward the strongest signal, with no camera, map or GPS.
**Problem / user:** Search-and-rescue or pet-finding scenarios where a person carries a phone but cannot be seen, so vision-based robots fail.

**Features**
- RSSI homing controller — State machine steps, re-measures, probes new headings when flat, fits a plane to odometry+RSSI to follow the gradient, returns to the peak on overshoot *[shown_working]*
- Nordic BLE scanner firmware — Zephyr app on nRF5340 scans for the phone beacon and rebroadcasts last 16 RSSI samples in its own advertisement so no cable is needed *[shown_working]*
- Go2 control — Unitree WebRTC data channel for stand, move, stop and odometry *[shown_working]*
- Safety layer — Bounded bursts, speed caps, stop after each move, latched stop on error, search time and move limits *[shown_working]*
- Radio simulator — 2D model of path loss, noise, packet loss and multipath used to tune algorithms before field trials *[shown_working]*
- Terminal dashboard — Live RSSI, filtered value, pose, search state and decisions *[claimed]*

**Flow:** Person holds phone advertising a BLE beacon → Operator starts homing run → Dog moves a short step and measures RSSI → Controller picks heading from signal trend → Dog closes in on person and stops at peak signal

**Prompt:** not public / not found
**Fit (implied):** Presents a hardware-plus-embedded closed loop where a Nordic board is the sensor driving a robot; README states it won the Hackster challenge. Other listed sponsors are not addressed in the page.  *(targeted: Hackster: Create What's Next, Dimensional, Elastic, Voloridge, Arduino, Dropbox)*
**Sponsor tools:** Nordic nRF7002-DK (BLE RSSI sensing on the robot, core)
**AI:** No ML; classical filtering (median and EMA) and gradient-fitting control. An AI coding assistant was used to write firmware, simulator and control code.
**Architecture:** Zephyr firmware on nRF5340 broadcasts RSSI over BLE; laptop Python radio layer filters it; homing state machine and safety guard send commands through Unitree WebRTC to the Go2.
**Novelty:** Uses signal strength alone to steer a legged robot toward a person. Honest limits: README says the dog never formally declared target found on hardware before the borrowed robot was returned.
**Scope:** small · working: 39 autonomous moves over about 12 m on a real Go2, reaching -51 dBm and rising; video demo link. · polish: Simulator matrices, write-up, tests and firmware docs; small 5k-line codebase.
**Claims:** 39 autonomous moves over about 12 m on real hardware | Closing at -51.3 dBm and rising when stopped | Simulator: 8 dB antenna contrast could lift convergence from 20% to 90%
**Gaps:** Official Hackster prompt text not found; Video not viewable
Sources: https://plume.hackmit.org/project/osnma-ymnqm-azajt-sywdc, evidence/hackmit-hackmit-2026-signalhound.json

---

### Spidey Sense
*HackMIT HackMIT 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** WINNER: HEALTHCARE TRACK WINNER

**What it is:** A laptop-based directional hearing aid: four microphones in a diamond locate every sound by bearing, a head-worn IMU shows where the wearer looks, and a beamformer plus time-frequency mask plays only that person into wired earbuds, while alarms, danger words and one's own name break through.
**Problem / user:** Deaf, hard-of-hearing and ADHD users who cannot pick out one voice in a loud room, or lock on and miss everything else; hearing aids amplify the whole room.

**Features**
- Sound bearing map — SRP-PHAT on four mic channels, 21 frames per second, 360 degrees; live room view; array geometry calibrated with a moving speaker. *[shown_working]*
- Gaze-steered listening — ESP32-S3 hat with a 6-axis IMU streams yaw over UDP; gaze line intersected with source rays to steer the beam; click-to-steer also available. *[shown_working]*
- Mask beamformer with neural cleanup — MVDR nulls plus per-bin direction mask, then DeepFilterNet3 via a Rust shim; 18.3 dB separation on two voices 215 degrees apart. *[shown_working]*
- Name alert and transcript — Local faster-whisper transcribes every utterance tagged with bearing and heard/missed; a missed name ducks the beam and an earbud line announces it. *[shown_working]*
- Safety break-in — Tonal steady alarm detector, shouted danger words (fire, call 911) and optional bang detector turn cancelling off for 8 seconds. *[shown_working]*
- Replay and debrief — Voice commands replay the last 30 seconds from the faced speaker or summarize what was missed, using the claude CLI with a text fallback. *[claimed]*
- Speaker naming — Double-click or 'I'm Marco' labels people; nearby voices disambiguated by an MFCC voiceprint. *[claimed]*
- Live multi-mic diarizer — Side project with pyannote segmentation and ReDimNet embeddings on CPU; 14.7% DER on an AMI meeting at about 1 s latency. *[claimed]*

**Flow:** Wear hat and wired earbuds near the four-mic array → Open room view showing sound bearings → Look at a talker; only that voice plays → Another person says your name; beam ducks and earbuds announce it → Alarm sounds; cancelling switches off then returns → Ask for a replay or debrief

**Prompt:** not public / not found
**Fit (implied):** Healthcare: assistive listening for deaf, hard-of-hearing and ADHD users. Sponsor listings are on the page; the writeup ties only the ESP32-S3 hat (Espressif hardware) and Arduino Modulino IMU explicitly to hardware.  *(targeted: Healthcare Track, Cognition: Best Use of Devin, Espressif, Meta: Bringing People Closer Together With AI, Voloridge: Signal in the Noise, Long Lake)*
**Sponsor tools:** ESP32-S3 with Arduino Modulino Movement IMU (Head-tracking hat streaming yaw over UDP, supporting)
**AI:** Mostly classical signal processing; DeepFilterNet3 for artifact cleanup, local faster-whisper small.en for transcripts, MFCC voiceprints, Claude CLI for summaries kept off the real-time path.
**Architecture:** 4-mic USB interface to Python beamformer (SRP-PHAT, MVDR, mask, DeepFilterNet shim) outputting to earbuds; web UI server with SSE; Whisper listener; ESP32-S3 gaze source over UDP.
**Novelty:** Real-time gaze-steered beamforming on four cheap mics and a laptop, offline with no cloud, with measured results and an honest list of failures.
**Scope:** medium · working: README with install, calibration, run and simulator instructions; page reports measurements on the real rig; repo about 2.4k LOC; no video link. · polish: Rig photo, room-view UI, no-hardware sim mode; detailed measured results and failure log.
**Claims:** 18.3 dB separation of two voices with mask plus DeepFilterNet | Bearing error 1 to 14 degrees on four test bearings | Tracked beam cut 1% of a walking talker's frames vs 29% fixed | Diarizer 14.7% DER vs pyannote offline 17%
**Gaps:** No official Healthcare track text found; No demo video; Page says bearing error 1-5 degrees but lists 13.8 on one bearing
Sources: https://plume.hackmit.org/project/bvbun-rvjwe-dwtmj-ljtag, evidence/hackmit-hackmit-2026-spidey-sense.json

---

### Stewardship Sam
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: GIVECAMPUS - 2ND PLACE + MOST PRODUCTION READY - FUNDRAISING / CONSTITUENT INTELLIGENCE CHALLENGE [2nd]

**What it is:** A solo-built relationship-intelligence assistant for university fundraisers using GiveCampus sample data. It builds a graph of shared clubs and activities and produces a daily prioritized queue of constituents to thank, reconnect with, invite or leave alone, with AI explanations and Q&A.
**Problem / user:** Advancement and fundraising teams who see donors, alumni and event-goers as flat CRM rows and miss the communities and relationship changes behind them.

**Features**
- Today queue — GET /api/today returns prioritized relationship signals such as RECONNECT or INVITE, with dismissals saved *[shown_working]*
- Six signal types — Deterministic detection of stewardship gaps, broken commitments, neglected relationships, relationship changes, contact pressure and communities losing engagement *[claimed]*
- Community graph — NetworkX graph with shared activities as the only edges; interactive community views *[shown_working]*
- Per-person timeline — Gifts, interactions, events, career changes and opportunities in one view *[claimed]*
- Ask Sam Q&A and call-note extraction — OpenAI answers natural-language questions grounded in data; template fallback without a key *[claimed]*
- Contact-policy filtering — README: of 2,184 detected relationship changes, 2,147 pass contact policy and appear in queue *[claimed]*

**Flow:** Open Today queue of people needing attention → Open a person's timeline and see explanation of the signal → Explore the surrounding community graph → Ask Sam a question or dismiss the item

**Prompt:** not public / not found
**Fit (explicit):** Built entirely on the GiveCampus dataset: six relationship use cases mined from gifts, interactions and affiliations, with a graph and AI explanations. Page states this single challenge.  *(targeted: GiveCampus: Fundraising / Constituent Intelligence Challenge)*
**Sponsor tools:** GiveCampus dataset (Source of gifts, interactions, affiliations, events and careers, core)
**AI:** Deterministic signal detection plus NetworkX community analysis; OpenAI generates grounded explanations and answers questions, with template fallbacks.
**Architecture:** Next.js frontend; FastAPI and SQLite backend loaded from provided CSVs; NetworkX graph; optional OpenAI explain and ask_sam modules; pytest demo-path tests.
**Novelty:** Frames fundraising as network analysis and includes 'wait' signals for over-contacted donors; solo project combining sociology and engineering.
**Scope:** medium · working: Backend endpoints, tests and demo reset described in README; a hosted fliplink link exists on the page. · polish: PRD and 19 implementation slices in repo; won 'most production ready' per prize title.
**Gaps:** Evidence file clone failed; README read via WebFetch summary; Official GiveCampus prompt text not found
Sources: https://plume.hackmit.org/project/alqmf-ljbou-vlpzr-ujkfk, https://github.com/marcosarnold/stewardship-sam

---

### The PenPal
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: ARDUINO - 2ND PLACE - TOUCH GRASS: BUILD SOMETHING THAT UNDERSTANDS THE REAL WORLD [2nd]

**What it is:** A writing-support tool that watches a child's hand through a phone camera with MediaPipe and flags stalled motion or poor hand posture, streaming alerts to a web dashboard. A pulse oximeter on an Arduino adds a stress signal.
**Problem / user:** Teachers and caregivers of children, especially nonverbal or selectively mute ones, who struggle silently while learning to write and get help late.

**Features**
- Hand tracking struggle detection — MediaPipe tracks 21 hand landmarks; custom logic detects stopped motion, fidgeting, finger articulation and writing posture *[shown_working]*
- Live dashboard with alerts — WebSocket streams vision results to React app; pop-up when the child is struggling *[shown_working]*
- Calibration of correct writing position — User sets reference posture in the web app *[claimed]*
- Session logging and summary graphs — Sessions stored in Firebase with authentication and charts *[claimed]*
- Pulse oximetry stress model — Arduino-based sensor with Edge Impulse tooling to compare pulse and SpO2 against baseline for calm vs stressed *[claimed]*

**Flow:** Teacher logs in and calibrates writing posture → Child writes under the phone camera → Vision server streams hand analysis over WebSocket → Dashboard shows alert when struggle is detected → Review session summary later

**Prompt:** not public / not found
**Fit (implied):** Senses the physical world via camera and a pulse oximeter on Arduino to detect a child's struggle; writeup does not address other sponsor challenges explicitly.  *(targeted: Arduino: Touch Grass, ASUS / Zenni Claw, Cognition Devin, Voloridge, Regeneron, Ramp, Long Lake)*
**Sponsor tools:** Arduino pulse oximeter (Heart rate and SpO2 to infer stress, supporting)
**AI:** MediaPipe hand landmarks with rule-based stopped/fidget detection; a small model on pulse-oximetry data to classify stressed vs calm (claimed, integration unfinished).
**Architecture:** Phone camera to Python OpenCV/MediaPipe server, WebSocket to React/Vite dashboard, Firebase for auth and sessions; separate heartMonitor module for the sensor.
**Novelty:** Pairs camera-based posture analysis with physiological sensing for a non-speaking child; the intended IMU was replaced after hardware was unavailable.
**Scope:** small · working: Video demo link and runnable vision-to-frontend pipeline; oximeter integration listed as next step. · polish: 4k-line repo with some tests; basic README.
**Gaps:** Official Arduino prompt text not found; Video not viewable
Sources: https://plume.hackmit.org/project/gxcea-qehmz-xnldy-yifsj, evidence/hackmit-hackmit-2026-the-penpal.json

---

### VistaAI
*HackMIT HackMIT 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SPONSOR WINNER: MAXIMOR AI - 1ST PLACE - OFFICE OF THE CFO AGENT CHALLENGE [1st]

**What it is:** A multi-tenant platform for private-equity roll-ups that ingests messy CSV/Excel data from acquired companies, maps it into a standard schema with human review, and shows a portfolio dashboard with evidence-backed opportunities like vendor consolidation.
**Problem / user:** PE analysts and portfolio-company CFOs integrating acquisitions with fragmented systems and manual back-office work.

**Features**
- Messy data ingestion — Detects schemas, proposes field mappings, normalizes CSV/XLSX records and stages ambiguous cases for human review *[shown_working]*
- Portfolio dashboard — Standardized view of customers, invoices, vendors, tasks and integration progress; metrics like AR and vendor spend *[shown_working]*
- Opportunity detection — Deterministic cross-company analysis finds vendor consolidation and software overlap, creating persistent integration tasks *[claimed]*
- Source provenance — Each metric or recommendation traces to original file and row *[claimed]*
- Agents — File Reviewer, Sector Merger, Report Generator, Recording Reviewer and sandboxed computer-use agent per README *[claimed]*
- Desktop workflow recorder — Electron app captures employee workflows to draft reports *[claimed]*
- Workflow-learning agents — RL-style environments trained from recorded trajectories *[planned]*

**Flow:** Upload company CSV/XLSX files → Review proposed schema mappings and ambiguous rows → Approved data lands in standardized records → Open portfolio dashboard → Review opportunities and generated tasks

**Prompt:** not public / not found
**Fit (implied):** Gives PE firms and CFOs reconciled, source-traced financial views of acquired companies, with AI interpreting data and deterministic code calculating metrics. Page lists Maximor among six challenges.  *(targeted: Maximor AI: Office of the CFO Agent Challenge)*
**AI:** LLM agents propose schema mappings and recommendations; deterministic code computes metrics; human review gates ambiguous items. Planned RL-style workflow learning.
**Architecture:** FastAPI backend with schema-per-tenant Postgres, S3 object storage, durable job queue and audit trail; Electron recorder; AWS deployment.
**Novelty:** Targets PE roll-up integration with provenance and tenant isolation; unusually infrastructure-heavy (migrations, audit trail, AWS) for a hackathon; README admits connectors and runtime not yet built.
**Scope:** large · working: Demo video, live domain link, tests and CI in repo; README lists unbuilt parts. · polish: Many design and infrastructure docs, MIT license, Docker, migrations.
**Gaps:** Evidence file clone failed; README via WebFetch summary; Official Maximor prompt text not found
Sources: https://plume.hackmit.org/project/cslzr-pathl-qrbxv-xahcq, https://github.com/emiliano800/vista

---

