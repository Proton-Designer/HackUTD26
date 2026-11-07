# VTHacks — VTHacks - 14 (8 projects)

### aftercare.
*VTHacks VTHacks - 14 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** VTHacks - 3rd Place Prize; [MLH] Best Use of Vultr [3rd]

**What it is:** Post-discharge follow-up system where an AI agent proactively checks in with patients by voice or text in English or Spanish, scores urgency with fixed server rules, and gives nurses a risk-sorted worklist with transcript-linked briefings and verified escalation to a physician.
**Problem / user:** Patients leaving hospital are on their own just when readmission risk peaks; nurses and physicians need the system to reach out first and surface worrying answers.

**Features**
- Bilingual proactive check-in — Voice (ElevenLabs), browser voice simulation, text or live nurse handoff; patient answers naturally in English or Spanish while original words are preserved. *[shown_working]*
- Deterministic safety routing — Server-side rules classify emergency, wound, medication, barrier or uncertainty before any LLM is consulted; emergency language interrupts the questionnaire. *[shown_working]*
- Bounded adaptive clarification — Gemini only rephrases the current question when the rules cannot interpret an answer (~0.9s); server keeps control of progression and escalation. *[shown_working]*
- Source-linked clinical briefing — Each generated summary line cites the transcript lines that support it; nurse notes stored separately from automated text. *[shown_working]*
- Risk-sorted nurse worklist — Dashboard ranks a cohort (40 synthetic patients per demo) with risk level, transcript, concerns, briefing and escalation status. *[shown_working]*
- Callsign escalation gate — Six checks (identity, certificate, transparency log, signature, provider policy, content verification) before an escalation reaches a provider. *[shown_working]*
- Offline deterministic simulation — Full scenario (~13s wound-concern run) runs locally with no cloud, phone number or API credits. *[shown_working]*

**Flow:** Patient is contacted for check-in by voice or text in English or Spanish → Structured questions with adaptive clarification → Rules engine flags emergency, wound, medication or barrier concerns → Case lands in nurse worklist sorted by risk with cited briefing → Nurse reviews transcript and adds notes → Escalation passes verification gate and goes to provider

**Prompt:** MLH Best Use of Vultr: Vultr is described as letting hackers bring high-performance projects to life instantly; prize for projects that make good use of its cloud hosting.
**Fit (implied):** Devpost lists Vultr hosting and Docker deployment among the stack, with a live app at its own domain; the writeup does not describe Vultr services beyond hosting.  *(targeted: MLH Best Use of Vultr, VTHacks 3rd Place)*
**Sponsor tools:** Vultr (hosting the live app per Devpost tags, supporting); GoDaddy (domain / ANS-style identity) (domain; Callsign identity gate, unclear)
**AI:** Gemini rephrases questions and drafts briefings, but urgency and escalation are decided by deterministic rules; ElevenLabs provides live voice; summaries are tied to transcript citations.
**Architecture:** React/Vite front end and Node/Express API with SQLite; rules engine and questionnaire state on server; ElevenLabs voice via LiveKit/WebRTC; Gemini for clarification and briefings; Callsign verification service gates escalations; Docker on Vultr.
**Novelty:** Explicit separation of LLM language understanding from rule-based safety decisions, plus cryptographic verification of escalations and citation-backed briefings, is unusual for a health hackathon demo.
**Scope:** large · working: Live app URL, demo video, README with latency and scenario figures and an offline simulation mode. · polish: Detailed README with diagrams, tests present, Docker, about 43k LOC.
**Claims:** ~0.9s adaptive clarification latency | Six verification checks on each escalation | 40 synthetic patients per demo; ~13s full scenario | Cites 3.6M 30-day readmissions at ~$20k each (2022)
**Gaps:** Vultr usage detail not described; video not watched
Sources: https://devpost.com/software/aftercare-b9di1l, evidence/vthacks-vthacks-14-aftercare.json (README), https://vthacks-14.devpost.com/

---

### Bubu-Dins
*VTHacks VTHacks - 14 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** VTHacks - 2nd Place Prize; [Cloudforce] Most Interesting Use of HokieAI [2nd]

**What it is:** Gamified financial-literacy course built on the PathMX platform: learners walk a map through housing, banking and investing stops, complete a Learn, Try it, Review loop with saved progress, and chat with AI characters such as tutor Dr.Bos and banker Tram.
**Problem / user:** Middle-school to college students learn money mistakes the costly way; the app lets them rehearse leases, cards and investing decisions first.

**Features**
- Map-based learning path with saved progress — Sign-in per learner; lessons are Markdown; completing a stop unlocks the next and persists across refreshes. *[shown_working]*
- Learn / Try it / Review loop — Housing practice gets AI feedback against four beginner criteria with unlimited revisions; passing records completion and 100 coins. *[shown_working]*
- Dr.Bos AI tutor — Gemini-backed office-hours chat that explains but cannot grade or award credit; reference index built from textbook PDFs. *[claimed]*
- Bank scene with Tram — Fictional banker character asks about tradeoffs rather than selling accounts. *[shown_working]*
- Capital One Nessie dashboard — Read-only GET calls to the sandbox from the server show practice account data; key kept off the browser. *[shown_working]*
- Storyworld — Walkable world with empty lots reserved for later decision scenarios. *[planned]*
- Investing portfolio lesson — Separate zyBook-style interactive portfolio lesson backed by Nessie sandbox. *[claimed]*

**Flow:** Sign in as a learner → Open Learn map and pick first stop → Read lesson and mark complete → Try housing or investing practice with Dr.Bos feedback → Visit Bank and talk to Tram → Refresh to confirm progress persists

**Prompt:** Cloudforce: Most Interesting Use of HokieAI; the official page gives only the prize name and a $500 award, with no description.
**Fit (implied):** HokieAI is listed in built-with tags, but the writeup attributes the tutor to Gemini and does not explain what HokieAI did.  *(targeted: Cloudforce Most Interesting Use of HokieAI, VTHacks 2nd Place)*
**Sponsor tools:** HokieAI (listed in built-with; role not described, unclear); Capital One Nessie API (read-only sandbox bank data dashboard, supporting)
**AI:** Dr.Bos and Tram are server-side LLM characters (Gemini per Devpost) with strict limits: no financial advice, no declaring learners passed, no invented rates; practice answers scored against fixed criteria.
**Architecture:** Bun/TypeScript PathMX app with plugins for map, portfolio board and dashboard; Markdown content and character agent files; server routes for Gemini and Nessie; completion files stored per learner.
**Novelty:** Content, characters and lessons live as plain Markdown files on a template platform; tests keep sandbox money, practice cash and learning credit separate.
**Scope:** medium · working: README describes working sign-in, saved completion and a three-stop housing journey; no live URL. · polish: Large repo (about 17k LOC) with tests, UX folder and art guides, but built on a provided template.
**Claims:** Full sign-in, try, refresh, progress-persists loop works | Nessie data used read-only with tests guarding the API key
**Gaps:** HokieAI role unexplained; README is a template starter text so partly not original
Sources: https://devpost.com/software/bubu-dins, evidence/vthacks-vthacks-14-bubu-dins.json (README), https://vthacks-14.devpost.com/

---

### CuraVox
*VTHacks VTHacks - 14 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Impiricus] Build the Next HCP Engagement Tool — 2nd Place [2nd]

**What it is:** Voice-first medication companion: a physician generates a QR code in about thirty seconds, the patient scans it and talks to an AI named Cora in Spanish, French or English. Cora answers only from approved drug info and the doctor visit notes and routes other questions to the physician inbox.
**Problem / user:** Patients, especially those with limited English, often mis-take or abandon prescriptions in the first week; physicians and pharma lack a channel in that gap.

**Features**
- QR companion setup — Physician picks drug, language, patient first name, notes and contacts; record is compressed into the QR link so no database or login is needed. *[shown_working]*
- Tap-to-talk multilingual voice — Deepgram Nova-3 transcribes and Aura-2 speaks; chat and voice in Spanish, French or English. *[shown_working]*
- Grounded answers — Gemini 2.5 Flash prompt restricted to a drug monograph plus physician notes; handles missed doses, OTC, alcohol. *[shown_working]*
- Escalation inbox — Out-of-plan questions, appointment requests and urgent flags are emitted as tags, filed to an in-memory inbox the doctor sees. *[shown_working]*
- Translated physician reply — Doctor writes in English and Cora speaks it to the patient in their language. *[shown_working]*
- Safety rules — Says she is AI, never changes doses, puts call 911 first for serious symptoms; DOB and phone never sent to companion. *[claimed]*

**Flow:** Physician logs into demo dashboard and builds a companion → QR code is shown and updates when notes change → Patient scans on phone and taps once → Patient asks questions aloud in Spanish → Cora answers from the plan or escalates → Physician replies in English and patient hears it in Spanish

**Prompt:** Impiricus: Build the Next HCP Engagement Tool; the official page lists only the title and cash prizes, no description.
**Fit (explicit):** README calls it an extension of Impiricus; gives physicians and brand partners a patient-side channel in week one, with future brand-partner medication files and anonymized question trends.  *(targeted: Impiricus Build the Next HCP Engagement Tool)*
**AI:** Gemini 2.5 Flash with fallback across four models answers from structured monograph and notes; structured action tags in replies; Deepgram handles speech-to-text and text-to-speech.
**Architecture:** Single Next.js 16 app for physician and patient sides; server routes proxy Gemini and Deepgram; patient record carried in lz-string QR payload; in-memory inbox polled by both pages.
**Novelty:** No database: the link itself carries the record; round trip through translation back to the doctor reply was tested on a real phone.
**Scope:** small · working: Devpost says full loop ran on a real phone over Wi-Fi; README has run steps; no live URL. · polish: About 7.5k LOC Next.js app with animation libraries, HTTPS dev mode, no tests.
**Claims:** About five cents per conversation | Cora Spanish speech round-tripped word for word | One in five prescriptions never filled (CDC cited)
**Gaps:** no video link on page
Sources: https://devpost.com/software/curavox, evidence/vthacks-vthacks-14-curavox.json (README), https://vthacks-14.devpost.com/

---

### Deadbolt
*VTHacks VTHacks - 14 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** VTHacks - 1st Place Prize [1st]

**What it is:** Chrome (Manifest V3) extension that intercepts a prompt before it is sent to an AI chat site, detects sensitive content locally, and either blocks it, auto-redacts it with undo, or only highlights it, then lets the user hover to reveal redacted values in the reply.
**Problem / user:** Individuals paste customer data, HR text or live API keys into chatbots without noticing; enterprise tools are heavy and send data to third parties.

**Features**
- Pre-send prompt gate — Content script catches Enter or Send on the chat composer and cancels the send if a rewrite cannot be verified. *[shown_working]*
- Tiered detection — Block tier for classification markings; high tier (keys, JWTs, SSN, cards via Luhn, IBAN) and medium (email, phone, address, DOB) via regex plus checksums. *[shown_working]*
- Auto-redact with undo — Sensitive values become placeholders; toast lists what changed and offers undo. *[shown_working]*
- Hover-to-reveal — In-memory per-tab vault maps placeholders to originals; reveal is painted locally, response DOM is not rewritten. *[shown_working]*
- Dashboard and receipt — Options page shows catch counts, a shareable receipt and a tokenizer explainer; popup and badge show counts. *[shown_working]*
- UI harness and labelled eval set — Standalone pages render every overlay; test suite runs detector tests and a labelled set. *[shown_working]*
- Local name/org NER (low tier) — Highlight-only names and organisations. *[planned]*

**Flow:** Install unpacked extension and open claude.ai → Type a prompt containing a secret and press Enter → Panel blocks or toast shows redactions with undo → Prompt sends with placeholders → Hover a placeholder in reply to see original → Open dashboard for counts and receipt

**Prompt:** VTHacks 1st Place overall prize (MacBook Pro 14 inch per member); no theme description on the prize page. Project also tagged HokieAI.
**Fit (none):** No stated prize targeting; general overall prize. HokieAI appears only as a built-with tag.  *(targeted: VTHacks 1st Place)*
**Sponsor tools:** HokieAI (listed in built-with tags only, token)
**AI:** Detection is deterministic regex and checksums, deliberately not ML; a classifier or NER is mentioned but the NER tier is not implemented. Claude was used per tags.
**Architecture:** Pure-function detector and redaction engine, content script adapter and overlays, MV3 service worker holding the vault and usage log, popup and options pages, shared message contract.
**Novelty:** Friction scales with detector confidence and failures cancel the send rather than leak; limitations are published openly in the README; tool runs fully on-device.
**Scope:** medium · working: Demo video, loadable build, tests and eval set; README lists deliberate limitations. · polish: About 13k LOC strict TypeScript, UI harness, dashboard, PRD document.
**Claims:** Never sends an unscrubbed prompt due to its own error | No account, no server, prompt text never stored
**Gaps:** no precision/recall figures
Sources: https://devpost.com/software/deadbolt-vs2xlp, evidence/vthacks-vthacks-14-deadbolt.json (README), https://vthacks-14.devpost.com/

---

### FalsePay
*VTHacks VTHacks - 14 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Impiricus] Build the Next HCP Engagement Tool — 1st Place [1st]

**What it is:** Outbound engagement platform for physicians built on public CMS Open Payments data: it matches reported industry payments to a doctor NPI, enriches identity from the live NPPES registry, sends a zero-login audit link, and helps the doctor draft a dispute and opt into ongoing monitoring.
**Problem / user:** Physicians have a short window to review and dispute possibly inaccurate payment records; campaign teams need an engagement hook that physicians actually want.

**Features**
- Live NPI enrichment — Searches a 10-digit NPI against the CMS NPPES API for name, credentials, taxonomy and location. *[shown_working]*
- Open Payments review — Physician-level view of reported dollars, transaction counts, manufacturers, status and history from CMS data. *[shown_working]*
- Risk triage — Flags unusual payment velocity (TimescaleDB monthly buckets) and specialty-to-product mismatch (pgvector); framed as review signals not fraud findings. *[shown_working]*
- Tokenized audit links — Random time-limited revocable tokens, only hashes stored, no account needed to view own records. *[shown_working]*
- Dispute draft generator — Physician selects questionable records and gets a reviewable draft; nothing is filed. *[shown_working]*
- Protection enrollment — Explicit opt-in to ongoing alerts after the audit. *[shown_working]*
- Campaign command center — Review queue and funnel of dispatched, opened, dispute drafted, protected from append-only events. *[shown_working]*

**Flow:** Campaign team browses risk-sorted physician queue → Dispatches an audit invitation → Physician opens tokenized link with no login → Reviews NPPES-verified details and flagged payments → Selects records and generates a dispute draft → Opts into protection alerts

**Prompt:** Impiricus: Build the Next HCP Engagement Tool; the official page gives only the title and prize amounts. The repo README frames the goal as inventing a new way to engage HCPs.
**Fit (explicit):** README concept uses an Open Payments audit-and-defense alert as the cold-outreach hook that converts a physician into an opted-in Impiricus channel.  *(targeted: Impiricus Build the Next HCP Engagement Tool)*
**Sponsor tools:** Tiger Data (managed Postgres with TimescaleDB and pgvector) (time-series payment velocity and vector mismatch scoring, core)
**AI:** Semantic specialty-versus-product mismatch via pgvector embeddings and AI-prioritized ranking; Gemini key optional in backend env; models not named.
**Architecture:** Next.js/TypeScript frontend; FastAPI backend with SQLAlchemy and asyncpg; Tiger Data Postgres hypertable plus pgvector; CMS and NPPES adapters; versioned REST with OpenAPI-generated types; Docker images.
**Novelty:** Uses a physician-protective compliance angle on public payment data as the engagement hook, with string-typed money and draft-only disputes to avoid overpromising.
**Scope:** medium · working: Live site falsepay.health, video, tests and Dockerfiles; production gaps such as staff auth are listed as not done. · polish: About 5k LOC with unit, contract and e2e tests, typed API contracts.
**Claims:** Tagline cites $14 billion in pharma reporting fraud (unsourced) | Complete physician-focused workflow with live NPPES lookup
**Gaps:** no quantitative results
Sources: https://devpost.com/software/falsepay, evidence/vthacks-vthacks-14-falsepay.json (README), https://vthacks-14.devpost.com/

---

### HireWire
*VTHacks VTHacks - 14 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** [GoDaddy] Best Use of ANS — 3rd Place; [MLH] Best Use of Presage [3rd]

**What it is:** Voice-first job application agent: a student agent reads the resume and coursework, finds fitting roles and drafts materials, while a recruiter agent represents a posted role; the two agents verify each other with domain-anchored certificates before any private data is exchanged.
**Problem / user:** Students retype the same details into dozens of applications and recruiters drown in fake ones; neither side can prove who they are.

**Features**
- Voice navigation — Whole student flow can run hands-free by voice (ElevenLabs listed). *[claimed]*
- Agent-to-agent handshake — User agent and employer agent verify certificate-backed domain identities; refuse aloud and release nothing if the employer cannot prove itself. *[claimed]*
- Student mode — Reads resume and coursework, finds matching roles and writes tailored application materials. *[claimed]*
- Recruiter mode — Publish a role once and an agent answers for it; applications arrive from verified agents. *[claimed]*
- Human approval gate — Every external action requires explicit approval by the person. *[claimed]*

**Flow:** Student uploads resume and coursework by voice → Agent suggests roles and drafts materials → Recruiter publishes a role with an agent → Agents perform identity handshake → If verified, details are shared; otherwise agent refuses → Human approves each external action

**Prompt:** GoDaddy: Best Use of ANS; official page names the prize and 1st/2nd/3rd gifts but does not define ANS or give a description. MLH Best Use of Presage: about a human-sensing layer for apps.
**Fit (implied):** Certificate-backed agent identities and a verified A2A handshake match the agent-name-service idea; Presage use is not described on the page.  *(targeted: GoDaddy Best Use of ANS (3rd), MLH Best Use of Presage (3rd))*
**Sponsor tools:** GoDaddy ANS (domain-anchored agent identity (inferred from prize and description), unclear); Presage (prize placement; usage not described, unclear)
**AI:** Gemini for resume matching and drafting; ElevenLabs for voice; Databricks listed without explanation.
**Architecture:** Next.js/React front end with Python backend, MongoDB and Databricks per tags; agents exchange verified messages over certificates. Repo was not retrievable so layout unknown.
**Novelty:** Frames job application as a mutual identity verification problem between two agents rather than a form-filling convenience tool.
**Scope:** small · working: Live site hirewire.biz and demo video are linked; no measurements reported. · polish: Own domain; Devpost text is brief with no challenges or next steps.
**Claims:** Applying to forty jobs takes about twelve hours (motivating estimate)
**Gaps:** repo README unreachable (clone failed, raw 404); how sponsor tools were used not stated
Sources: https://devpost.com/software/hirewire, https://vthacks-14.devpost.com/

---

### Persist Health
*VTHacks VTHacks - 14 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Impiricus] Build the Next HCP Engagement Tool — 3rd Place [3rd]

**What it is:** Clinician dashboard plus patient logging app that gathers mood, sleep, pain and wearable vitals between visits, produces AI reports and a one-page history summary, and shows disclosed pharma-sponsored clinical matches alongside the analysis.
**Problem / user:** Visits rely on patient recall and raw wearable exports are hard to read; the project wants doctors to see trends and keeps tools free by pharma sponsorship.

**Features**
- Patient logging — Mood, sleep, pain, energy and journals logged daily, with wearables syncing heart rate, HRV and breathing rate. *[shown_working]*
- Clinician EMA view — Doctor sees trends, check-in compliance, journals and vitals per patient. *[shown_working]*
- AI clinical report and summary — Generates a one-page summary of the period since the last session. *[claimed]*
- Alerts and trend detection — Detects correlations and prompts follow-ups or urgent care. *[claimed]*
- Patient notification center — Automatic or clinician-sent notifications. *[claimed]*
- Sponsored pharma matches — Disclosed sponsored placements mixed with non-sponsored resources, framed to avoid Anti-Kickback issues; README says matches are simulated. *[claimed]*
- Hokie AI sidekick — Assistant built on Hokie AI. *[claimed]*

**Flow:** Patient logs mood, sleep and journal or syncs wearable → Data accumulates between visits → Clinician opens patient view → Reads AI report and summary → Sees labelled sponsored matches → Sends notification to patient

**Prompt:** Impiricus: Build the Next HCP Engagement Tool; official page gives only the title and prize amounts.
**Fit (explicit):** Pharma-funded sponsored placement inside the clinician view is the engagement channel to doctors, with compliance disclosure.  *(targeted: Impiricus Build the Next HCP Engagement Tool)*
**Sponsor tools:** Vultr (hosting database and Express server, supporting); GoDaddy (persist.health domain, token); Hokie AI (sidekick assistant, supporting)
**AI:** OpenRouter-based LLM calls generate patient reports; Hokie AI powers a sidekick; specific models unnamed.
**Architecture:** React web client, Express/Node server and MySQL on Vultr; demo patient data and simulated clinical matches; domain via GoDaddy and Cloudflare.
**Novelty:** Funding model where pharma sponsorship pays for free doctor and patient tools, with compliance-aware labelling, is the distinctive angle.
**Scope:** small · working: Live site persist.health, video, demo data; README says prototype with simulated matches. · polish: About 9.5k LOC, no tests, brief README.
**Claims:** Free for doctors and patients, funded by pharma sponsorship
**Gaps:** no metrics
Sources: https://devpost.com/software/pied-piper-test, evidence/vthacks-vthacks-14-persist-health.json (README), https://vthacks-14.devpost.com/

---

### Radar
*VTHacks VTHacks - 14 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** VTHacks - Best UI/UX Hack; [GoDaddy] Best Use of ANS — 2nd Place

**What it is:** Home-emergency system of seven agents with their own cryptographic identities: Wi-Fi CSI sensing detects motion, a servo pulls a physical shield off a camera, a vision agent narrates the scene to the resident watch, and only if the resident starts an incident does a caller agent phone 911 and relay what the camera sees.
**Problem / user:** False burglar alarms dominate police dispatches and cameras that always record are a privacy cost; residents and dispatchers need verified context.

**Features**
- Wi-Fi motion trigger — Laptop reads channel state information on home WiFi and emits a motion claim. *[shown_working]*
- Physical camera shield — Servo rotates 90 degrees to expose the lens; shutter agent verifies a signed grant first. *[shown_working]*
- Vision narration — Gemini Live describes the room; text reaches iPhone and Apple Watch in about three seconds. *[shown_working]*
- Human-initiated 911 call — Caller agent (ElevenLabs, Retell) calls only after the resident starts the incident and answers questions from live vision. *[shown_working]*
- Hash-chained incident record — Replay agent seals footage, detections, transcripts into a timeline and emails the department. *[shown_working]*
- Web dashboard — Review timeline, clips and transcripts after the incident. *[shown_working]*
- Per-agent cryptographic identity — Agents sign claims and grants; identities tied to ANS and domain. *[claimed]*

**Flow:** Motion crosses threshold from Wi-Fi sensing → Shutter opens and vision starts narrating → Resident sees description on watch → Resident starts incident from wrist → Caller agent talks to dispatcher with live context → Incident record is sealed and emailed

**Prompt:** VTHacks Best UI/UX Hack (Polaroid camera; no description) and GoDaddy Best Use of ANS (title and gifts only, ANS undefined).
**Fit (explicit):** README states seven agents each hold a cryptographic identity and verify signed grants, matching the ANS theme; watch-first interaction supports UI/UX.  *(targeted: VTHacks Best UI/UX Hack, GoDaddy Best Use of ANS (2nd))*
**Sponsor tools:** GoDaddy (ANS, domain/DNS) (agent identities and domain, core); Vultr (hosting web dashboard, supporting)
**AI:** Gemini Live for video analysis and narration; ElevenLabs and Retell for realtime voice and phone; computer vision for people tracking; claims are cross-checked across agents.
**Architecture:** Python multi-agent backend (master, presence, shutter, vision, caller, replay) with signed messages; MongoDB store; SwiftUI iOS/watchOS apps; web dashboard on Vultr; Resend email.
**Novelty:** Hardware lens shield as a privacy guarantee, human-in-the-loop 911 calling, and per-agent cryptographic identities with a timed latency budget are unusual.
**Scope:** large · working: README gives a per-second latency budget with tests behind it; hardware demo with servo and watch app in video. · polish: About 57k LOC, 447 files, tests, docs and hero images.
**Claims:** 94 to 98% of police alarm responses are false | First narration reaches the watch in about 3 seconds | Radar never calls 911 without a human decision
**Gaps:** README read only partly (first ~7k chars); Devpost says simulated emergency call
Sources: https://devpost.com/software/boom-hmsdki, evidence/vthacks-vthacks-14-radar.json (README), https://vthacks-14.devpost.com/

---

