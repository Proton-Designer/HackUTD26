# HackHarvard — HackHarvard 2026 (7 projects)

### Concord
*HackHarvard HackHarvard 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice)

**What it is:** Concord turns a clinical-trial schedule of assessments into a site budget where every priced line shows its source: CMS fee schedule rates, a Medicare coverage classification, and labeled assumptions. It also checks a site's proposed CSV budget against the benchmark and exports a counter-proposal.
**Problem / user:** Research-site coordinators, coverage analysts and sponsor budget teams who negotiate trial budgets from numbers neither side can reproduce.

**Features**
- Protocol to budget — Reads a trial's visits and procedures, drafts coverage classifications under Medicare NCD 310.1, and prices lines from CMS physician and lab fee schedules by locality. *[shown_working]*
- Two-site comparison — Breaks down geographic adjustments and compares budgets across 109 Medicare localities. *[shown_working]*
- Site proposal check — Flags an uploaded CSV budget against a range around the Medicare benchmark and exports a counter-proposal with sources. *[shown_working]*
- Trial import by NCT ID — Pulls registry records and U.S. sites from a crawled ClinicalTrials.gov SQLite database. *[shown_working]*
- Portfolio overlap and site scores — Shows shared sites across a sponsor's trials plus exploratory enrollment models, with a synthetic planning demo. *[shown_working]*
- Sponsor integration lab — Photon 2.0 messaging, a 15-case Chalk evaluation suite and a Factory Droid proposal session; live execution not verified at submission. *[unclear]*

**Flow:** Pick a trial → Concord walks through coverage, budget, comparison and terms → Inspect or override any line's source → Compare two sites → Upload a site's CSV proposal and export a counter-proposal

**Prompt:** Photon 2.0 messaging-agent track at HackHarvard 2026: ship an agent with a real phone number reachable on a messaging channel (iMessage, SMS, voice etc.), live on at least one channel, judged on creativity and technical strength; winner, runner-up and best voice agent prizes.
**Fit (implied):** README names the Regeneron clinical-trials track; Photon 2.0 appears only as one integration among several, not as the central interface.  *(targeted: Regeneron track (README), Photon, Chalk and Factory sponsor integrations (unconfirmed))*
**Sponsor tools:** Photon 2.0 (Messaging integration in the sponsor lab, supporting); Chalk evaluations (15-case acceptance suite, supporting); Factory Droid SDK (Bounded operational proposals, supporting)
**AI:** Core budgeting is deterministic fee-schedule math; research models are Poisson-gamma enrollment estimates; Factory Droid agent only proposes changes through restricted tools and the engine re-evaluates them.
**Architecture:** FastAPI/Pydantic backend over a SQLite database of 7,221 NSCLC trials and CMS fee tables; React/TypeScript/Vite/Leaflet frontend with Simple and Detailed views; reproducible run records.
**Novelty:** Heavy emphasis on traceability and honesty: unpriced items stay blank, negative research findings are published, and saved demo evidence is labeled as replay.
**Scope:** large · working: About 74k LOC; page cites 618 backend and 55 frontend tests passing and a live demo link served from a team laptop. · polish: CI, 280 docs files, light/dark themes; page admits live provider execution was unverified.
**Claims:** Budget for one trial spans $1,034 to $1,580 per participant across 109 localities | 618 backend tests passed, 102 skipped | Modeled coordination gain fell from 1.42x to about 1.05x held-out
**Gaps:** No Photon prize badge on page; Photon is a minor integration; No video
Sources: https://devpost.com/software/concord-17as0b, https://github.com/CosmicOdyssey/concord

---

### Elfie
*HackHarvard HackHarvard 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice)

**What it is:** Elves is a moving crew you text: one iMessage/SMS/voice number fronts a Crew Lead and three specialist agents that find housing and storage, price and negotiate furniture sales from photos, and track money in a Nessie ledger with escrow.
**Problem / user:** People moving apartments in a crowded lease-turnover market who must sell furniture, find housing and split costs with roommates.

**Features**
- Crew Lead onboarding and routing — Collects dates, budget and items by text or phone call, then routes tasks across agents, tracking which agent last spoke. *[shown_working]*
- Home Elf — Browser-automated search of apartments, sublets and storage, scam flagging, sublet posts from room photos, dated checklist, bookings only on approval. *[claimed]*
- Stuff Elf with Deal Engine — Prices items from photos and negotiates with buyers through a Postgres state machine that enforces floor prices and pickup slots; scheduled price drops. *[claimed]*
- Money Elf and escrow — Nessie holds Moving Fund and Escrow accounts, splits roommate costs, and releases buyer payments after pickup confirmation. *[claimed]*
- Smart Plan — Simulates the move 2,000 times to estimate chance of finishing under budget; delivered as image in thread. *[claimed]*
- Approval and scam guard — Any below-floor price, payment, refund or booking needs one explicit yes; risky payment methods redirected to escrow. *[claimed]*

**Flow:** Text the number about a move → Crew Lead onboards and confirms a plan → Home, Stuff and Money Elves handle housing, sales and ledger → Images and a signed dashboard link arrive in the thread → User approves key actions with a yes

**Prompt:** Photon 2.0 messaging-agent track at HackHarvard 2026: ship an agent with a real phone number reachable on a messaging channel (iMessage, SMS, voice etc.), live on at least one channel, judged on creativity and technical strength; winner, runner-up and best voice agent prizes.
**Fit (implied):** Entire product lives in a Photon 2.0 iMessage/SMS/voice thread run by multiple cooperating agents; page says Photon 2.0 was used after Photon 1.0 mini app was shelved.  *(targeted: Photon messaging agent track (unconfirmed), Capital One Nessie)*
**Sponsor tools:** Photon 2.0 (Single messaging number across iMessage, SMS and voice, core); Capital One Nessie (Ledger, escrow and roommate loans, core); Retell (Onboarding phone calls, supporting)
**AI:** Claude routes messages (Haiku when unsure), reads photos, writes listings and negotiates; floor prices and state transitions are enforced in code, not by the model.
**Architecture:** Bun/TypeScript service on Railway with Supabase Postgres state; Photon lines in, Browserbase/Stagehand browsing, Deal Engine state machine, Nessie ledger, Retell voice.
**Novelty:** Four-persona agent crew behind one number with hard-coded negotiation guardrails and escrow-style money handling, backed by user interviews.
**Scope:** large · working: About 39k LOC with 600+ automated tests; page says it runs on real phones against a live Nessie sandbox. · polish: Docker, demo site, video, SPEC and docs; README notes spec drift between branches.
**Claims:** Over 600 automated tests | Interviewed 15+ people who had moved | 30+ people signed up to try it
**Gaps:** No prize badge on page
Sources: https://devpost.com/software/n-a-okr0vf, https://github.com/arshiyasharma/hackharvard/

---

### Keepsake
*HackHarvard HackHarvard 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice)

**What it is:** Keepsake watches a room (or a chest-worn phone) with computer vision, remembers when and where each everyday item was last seen with a photo, and answers spoken 'where are my keys' questions. It can send a gentle iMessage reminder.
**Problem / user:** People with Alzheimer's or dementia who lose items like glasses and keys, and their caregivers.

**Features**
- Open-vocabulary item tracking — YOLO-World with ByteTrack tracks 12 named items at about 5 fps on a laptop, no training. *[shown_working]*
- Last-seen photo memory — State machine stores when an item was put down and a photo as evidence. *[shown_working]*
- Voice lookup — Browser speech input; answer spoken with xAI text-to-speech, showing photo and highlight; LLM only phrases database facts. *[shown_working]*
- Room scan — YOLO11m on stills describes locations relative to furniture, numbered duplicates. *[claimed]*
- Wearable mode — MediaPipe hand landmarks and CLIP embeddings track items via hand interactions. *[claimed]*
- Privacy controls — Processing stays local, pause-saving switch and forget-everything button. *[claimed]*

**Flow:** Place phone on shelf or wear it → Scan room → Items detected and tracked → Item put down so photo saved → Ask aloud where something is and hear answer

**Prompt:** Photon 2.0 messaging-agent track at HackHarvard 2026: ship an agent with a real phone number reachable on a messaging channel (iMessage, SMS, voice etc.), live on at least one channel, judged on creativity and technical strength; winner, runner-up and best voice agent prizes.
**Fit (none):** README mentions an iMessage reminder channel, but the Devpost page does not describe Photon use; link to the track is weak.  *(targeted: Photon messaging agent track (unconfirmed))*
**Sponsor tools:** Photon / iMessage (Reminder texts per README, unclear)
**AI:** YOLO-World and YOLO11 detection, ByteTrack, MediaPipe and CLIP for wearable mode; Grok TTS for speech; deterministic database decides location, LLM only phrases it.
**Architecture:** iPhone video to Mac via Continuity Camera, OpenCV and detectors, FastAPI plus SQLite memory, React/Vite/Tailwind UI with list, map and photo-history views; Expo mobile and separate wearable app in repo.
**Novelty:** Honest 'I don't know' answers by design and a separate wearable pivot from fixed cameras to avoid per-room installs.
**Scope:** medium · working: About 24k LOC with tests; page reports 12 tracked items at 5 fps; no user testing. · polish: Multiple UI views and privacy panel; no video or live link.
**Claims:** Tracks 12 items without model training | About 5 fps detection on Apple MPS
**Gaps:** Photon use minimal/unclear; No video
Sources: https://devpost.com/software/keepsake-df0gmw, https://github.com/rayhanrinzan/keepsake

---

### Mirage
*HackHarvard HackHarvard 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice)

**What it is:** Mirage sits between an AI agent and its tools; in-scope calls run for real, out-of-scope calls get a convincing fake world, and use of a planted decoy key blocks the run. While the agent is kept busy, the on-call defender is texted, called and briefed by voice.
**Problem / user:** Teams deploying AI agents with shell and credential access who want to detect and contain scope-breaking without tipping the agent off.

**Features**
- Per-call verdicts pass, mirage or block — Rules on path, host, decoy key and tampering decide; an LLM judge can only raise a verdict. *[shown_working]*
- Consistent fake environment — Fake files and credentials seeded per path and session with a ledger and growing delays. *[shown_working]*
- Isolated agent fleet — Each Factory Droid agent runs in its own Daytona VM with built-in tools replaced by Mirage's MCP server. *[shown_working]*
- Live dashboard and forensic log — Shows boundary crossings, what the mirage returned and a tamper-resistant log. *[shown_working]*
- Defender alert handshake — iMessage via Photon, then a call with one-time code and ElevenLabs voice briefing. *[shown_working]*

**Flow:** Agents start in Daytona VMs via MCP → In-scope calls run normally → Out-of-scope call gets mirage output → Planted key use blocks run → Defender gets text then call and briefing

**Prompt:** Photon 2.0 messaging-agent track at HackHarvard 2026: ship an agent with a real phone number reachable on a messaging channel (iMessage, SMS, voice etc.), live on at least one channel, judged on creativity and technical strength; winner, runner-up and best voice agent prizes.
**Fit (implied):** Photon iMessage carries defender alerts and the confirmation handshake; the core product is agent containment, not a messaging agent.  *(targeted: Fintech & Cybersecurity track (README), Photon track (unconfirmed))*
**Sponsor tools:** Photon / iMessage (Defender text alerts and handshake, supporting); Factory Droid (Agents under test, core); Daytona (VM per agent, core); Chalk model gateway (Routes LLM judge, supporting)
**AI:** Deterministic rules plus an LLM judge via Chalk (verdict is the max of the two); ElevenLabs voice agent briefs the defender.
**Architecture:** TypeScript/Node server hosts an MCP tool proxy, watcher, fake-world generator, forensic log and WebSocket dashboard; Daytona VMs run Droid agents; Photon, ElevenLabs and SIP handle alerts.
**Novelty:** Deceives rather than blocks rogue agents, with a fake world kept self-consistent, and includes an independent honest-environment check.
**Scope:** medium · working: Page reports a 25-agent rehearsal and live defender call; one rogue agent was scripted. · polish: Hand-built dashboard, evals folder, 9 screenshots; no video.
**Claims:** 442 tool calls checked, 0 real out-of-scope access in 25-agent rehearsal | Real out-of-scope executions fell from 5 to 0 | No misses or false positives on labeled test set
**Gaps:** No video
Sources: https://devpost.com/software/team-b-0ydafx, https://github.com/MrFiscus/Mirage

---

### SiteLine
*HackHarvard HackHarvard 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice)

**What it is:** Siteline triages a clinical-trial site's Word redline against a sponsor playbook: an LLM extracts clause values, a rules engine decides accept, fallback, escalate or human review, approvers answer over iMessage, and a counter-proposal is exported as tracked changes.
**Problem / user:** Sponsor contract teams and site staff slowed by hand-reviewing every redline, delaying trial start-up.

**Features**
- Redline classification — Playbook of 9 clause types and 37 positions maps each tracked change to one of four outcomes with rule ID and verified quote. *[shown_working]*
- Sandboxed document parsing — Daytona sandbox with networking off parses the docx and returns JSON. *[shown_working]*
- iMessage escalation to approvers — Legal, finance and privacy reply 1, 2 or 3; call fallback if no answer. *[shown_working]*
- Word counter-proposal export — Real tracked changes and comments. *[shown_working]*
- Portfolio view with weekly delay cost — Ranks sites by blockers and cost. *[claimed]*
- Human-confirmed precedent store — Only confirmed terms become precedents; low-confidence items go to a person. *[claimed]*

**Flow:** Upload or email a redline → Parse in sandbox → LLM extracts clause values → Rules assign outcomes → Approvers reply by iMessage → Export counter-proposal

**Prompt:** Photon 2.0 messaging-agent track at HackHarvard 2026: ship an agent with a real phone number reachable on a messaging channel (iMessage, SMS, voice etc.), live on at least one channel, judged on creativity and technical strength; winner, runner-up and best voice agent prizes.
**Fit (implied):** Photon 2.0 delivers escalation approvals and live status; main track is clinical-trial contracting.  *(targeted: Regeneron Reinvent Clinical Trials track (README), Photon (unconfirmed))*
**Sponsor tools:** Photon 2.0 (Approver iMessages with call fallback, core); Daytona (Isolated parsing, core); Chalk Evaluations (Eval wiring, supporting)
**AI:** GPT-5 (Claude Code fallback) extracts clause values with verbatim quotes under a strict schema; deterministic rules decide; responses cached by prompt hash.
**Architecture:** React/Vite UI, FastAPI backend, Daytona parse sandbox, rules engine, Supabase Postgres and S3, Photon 2.0 for approvals.
**Novelty:** AI reads, code decides; quote-check and confidence floor force uncertain items to humans, benchmarked against an LLM-only baseline.
**Scope:** medium · working: Eval on 243 labeled changes, fictional 17-article agreement demo; repo has tests. · polish: Video, slides, review UI.
**Claims:** 94.2% accuracy vs 91.8% for LLM-only | 0 unsafe accepts vs 2 | About $79,000 per week of delay for demo site
**Gaps:** No prize badge
Sources: https://devpost.com/software/siteline-90rxwp, https://github.com/duna-akin/hackharvard-2026

---

### Swarm
*HackHarvard HackHarvard 2026 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice)

**What it is:** Swarm scans a codebase for third-party API usage, watches vendor changelogs for breaking changes, texts the developer on iMessage when a break hits their code, and has a Factory Droid agent write and verify a fix in a sandbox before opening a PR on approval.
**Problem / user:** Solo founders and small teams depending on vendor APIs who miss breaking changes until users complain.

**Features**
- Repo scan — Python AST maps SDK imports, call sites and pinned versions. *[claimed]*
- Vendor change knowledge base — 4,700+ changelog entries and breaking changes from eight vendors, refreshed by GitHub Actions and a poller. *[claimed]*
- iMessage alert and steering — Photon texts the user and accepts plain-English instructions. *[shown_working]*
- Sandboxed fix and verification — Droid writes fix plus regression test in Daytona; test must fail on old code and suite pass on new. *[shown_working]*
- Approval-gated PR and merge — Separate yes needed to open and to merge. *[claimed]*
- Live workflow graph UI — Scan, Watch, Analyze, Report, Mend stages with evidence. *[shown_working]*

**Flow:** Connect a repo → Swarm scans and monitors → Text arrives on a match → User steers fix → Droid fixes and verifies → User replies yes to PR then merge

**Prompt:** Photon 2.0 messaging-agent track at HackHarvard 2026: ship an agent with a real phone number reachable on a messaging channel (iMessage, SMS, voice etc.), live on at least one channel, judged on creativity and technical strength; winner, runner-up and best voice agent prizes.
**Fit (implied):** Uses Photon 2.0 as the primary human interface for alerts, steering and approvals of an autonomous fix agent.  *(targeted: Photon messaging agent track (unconfirmed), Factory Droid, Daytona)*
**Sponsor tools:** Photon 2.0 (Two-way iMessage alerts and approvals, core); Factory Droid SDK (Fix-writing agent, core); Daytona (Sandbox execution, core)
**AI:** Claude classifies changelog entries and judges impact and converses; Droid agent writes fixes in sandbox; verification requires failing-then-passing tests.
**Architecture:** FastAPI with SQLite and SSE, single-page HTML UI, Daytona sandbox from prebuilt snapshot, Photon Python client, GitHub for PRs.
**Novelty:** Closed loop from vendor changelog to merged PR driven entirely by text replies, with test-based proof of the fix.
**Scope:** medium · working: Two demo repos with timed runs reported; repo could not be cloned for inspection. · polish: Live workflow graph and many screenshots; no video.
**Claims:** Fix in 45-76 s on demo repos | 4,700+ changelog entries, 337 breaking changes | Roughly 2,900x faster than a 48-hour typical fix
**Gaps:** Repo clone failed; README unread; No prize badge
Sources: https://devpost.com/software/swarm-1e527i

---

### TekKEY
*HackHarvard HackHarvard 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice)

**What it is:** TekKEY lets an AI trading agent submit its strategy as a program that an exchange compiles and formally searches for worst-case loss. If safe it gets a certificate and a key that can only run that one program; if not it gets a replayable counterexample.
**Problem / user:** Owners of LLM trading agents and exchanges that hold their funds, who need a provable cap on losses if the agent is manipulated.

**Features**
- Program compiler and static checks — Strategies compile to native exchange orders; unsafe ones (e.g. no take-profit) rejected. *[shown_working]*
- Exhaustive verifier with certificates — Searches fill paths on an exact matching-engine copy in about 12 ms, issuing a worst-case loss bound. *[shown_working]*
- Counterexamples and repair loop — Exact worst fill sequence is replayable and fed to a coding agent for a fix. *[shown_working]*
- Rolling 24-hour loss budget with escrow — Programs exceeding the budget are refused; certified loss escrowed via Nessie. *[claimed]*
- Flash-crash replay and live race — Replays 10 Oct 2025 on a chosen model, compares ordinary vs bounded key; live Coinbase ETH-USD race. *[shown_working]*
- iMessage owner alerts — Program-end and budget alarms; replying freeze stops new programs. *[claimed]*

**Flow:** Agent submits strategy program → Venue verifies → Certificate and one-program key, or counterexample → Program runs under key → Owner gets alerts and can freeze

**Prompt:** Photon 2.0 messaging-agent track at HackHarvard 2026: ship an agent with a real phone number reachable on a messaging channel (iMessage, SMS, voice etc.), live on at least one channel, judged on creativity and technical strength; winner, runner-up and best voice agent prizes.
**Fit (implied):** Photon 2.0 is used only for owner notifications and freeze replies; the project's center is formally verified agent keys.  *(targeted: Digital Trust track (README), Photon track (unconfirmed))*
**Sponsor tools:** Photon 2.0 (Owner alerts and freeze command, supporting); Capital One Nessie (Accounts, escrow, settlement, supporting); Factory Droid SDK (Repair loop, supporting); Daytona (Agent sandbox, supporting); Chalk Model Gateway (Routes Grok calls, supporting)
**AI:** Claude and Grok 4.20 act as trading agents under test and in the repair loop; safety guarantees come from deterministic compilation and exhaustive search, not model judgment.
**Architecture:** C++20 limit-order-book engine with router and transports; policyc compiler, verify, replay, venued tools; Python/FastAPI gateway with SQLite; Vercel demo site.
**Novelty:** Treats an API key as a verified theorem about worst-case loss, backed by a C++ engine and soundness fuzzing.
**Scope:** large · working: About 38k LOC, many reported runs in a results file, live demo site, soundness fuzz. · polish: Deployed site, audit and results docs with defects listed first.
**Claims:** Flash-crash: ordinary key -$3,768.68 vs bounded key -$82.47 | 1,845 programs certified in 24h run, none exceeded | 20,000 fuzzed fill sequences, none beat a certificate
**Gaps:** No video; No prize badge
Sources: https://devpost.com/software/tekkey, https://github.com/JoshuaA1292/TekKEY

---

