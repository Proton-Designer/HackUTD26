# DubHacks — DubHacks '26 (24 projects)

### Brawlmegle
*DubHacks DubHacks '26 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Chef's Kitchen: 2nd Place [2nd]

**What it is:** A browser fighting game where the webcam scans the player into a stylized rigged 3D fighter in about 40 seconds, then lets two players box online peer-to-peer. A motion intent reader turns body movement into punches, blocks and dodges.
**Problem / user:** Players who want a camera-controlled fighting game with arcade impact that VR or Kinect-style boxing lacks.

**Features**
- Webcam-to-fighter scan — GPT writes a backstory and character sheet, self-hosted TRELLIS.2 generates a 3D model, a custom Blender auto-rigger adds a skeleton, and the face is repainted. *[claimed]*
- Intent reader — MediaPipe pose in a Web Worker at about 30 fps; motion is classified as punch, hook, uppercut, block, duck, dodge or kick rather than mapping the skeleton directly. *[claimed]*
- Fight engine — One laptop acts as referee with combos, counters and guard breaks; the other mirrors state and sends input. *[claimed]*
- Peer-to-peer matchmaking — WebRTC with a small matchmaking and relay server on an EC2 instance, Omegle-style with live cameras. *[claimed]*
- AI live commentary — ElevenLabs voice commentary aware of game events. *[claimed]*
- Arcade presentation — Hero entrances, VS screens and a custom Mount Rainier arena. *[claimed]*

**Flow:** Open the site and stand before the camera → Watch the scan form into a 3D fighter in under a minute → Get matched with another player → Fight using body motions → Hear live AI commentary

**Prompt:** not public / not found
**Fit (none):** Chef's Kitchen is a title track described only as open-ended; the project is a full game submitted to it. No stated link to prompt text.  *(targeted: Chef's Kitchen: 2nd Place)*
**Sponsor tools:** ElevenLabs (Live AI commentator voice, supporting)
**AI:** MediaPipe pose tracking with a custom motion-intent classifier; GPT for backstory and character sheet; TRELLIS.2 image-to-3D on own AWS GPU; ElevenLabs TTS commentary.
**Architecture:** React/TypeScript/Three.js client, MediaPipe in a Web Worker, WebRTC peer link with EC2 matchmaker/relay, referee-client fight engine, AWS GPU server running TRELLIS.2 plus Blender rigging pipeline.
**Novelty:** Generates a personalized rigged 3D avatar from a webcam scan on self-hosted GPU and fights peer-to-peer in browser; built its own rig checker after hollow meshes broke rigs.
**Scope:** large · working: Live site brawlmegle.vip listed; no repo; descriptions of tuned config from recorded fights. · polish: Arena model, VS screens, commentary, 15 gallery images.
**Claims:** Scan to playable fighter in about 40 seconds | Camera read at about 30 fps
**Gaps:** no repo; track text not published; video not seen
Sources: https://devpost.com/software/brawlmegle, https://dubhacks-2026.devpost.com/

---

### Codegraph
*DubHacks DubHacks '26 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Cook Smarter: 2nd Place [2nd]

**What it is:** A VS Code extension that parses a C or C++ folder with tree-sitter and draws files, classes and functions as an interactive nested graph with calls, includes, inheritance and overrides. A side panel offers AI node summaries, an Ask AI investigator and change-impact risk scoring.
**Problem / user:** Developers, especially newcomers, who struggle to understand large or AI-generated C/C++ codebases from long files and many linked headers.

**Features**
- Interactive code graph — ELK left-to-right layout; files open into functions and classes; relationships drawn as bundled or per-node arrows; node size by connectivity. *[shown_working]*
- Tree-sitter parsing — WASM C/C++ grammars, no compiler needed; names resolved project-wide, name-only matches marked uncertain. *[shown_working]*
- AI node summaries — Selected function, type or file described by the VS Code language model, cached per workspace. *[shown_working]*
- Ask AI with trace mode — Tool-calling investigation searches symbols and reads code, shows a step timeline, cites source lines with confidence, and highlights the path on the graph. *[shown_working]*
- Change-impact scoring — Predicts which nodes are affected by renaming, changing or deleting a node and colours them red, orange or yellow by risk. *[shown_working]*
- Concept tagging — Optional AI layer tags functions with concepts such as logging, highlighting all tagged nodes. *[claimed]*
- Git commit compare — Button and command exist but are not wired up yet. *[planned]*

**Flow:** Open a C/C++ folder in VS Code → Run Open Code Graph from the command palette → Click files to expand and functions to see code cards → Open the panel for details or AI summary → Ask a question or run impact analysis and see highlights on the graph

**Prompt:** not public / not found
**Fit (none):** Cook Smarter is described only as an open title track; the project is a developer-productivity tool for understanding code. No stated connection.  *(targeted: Cook Smarter: 2nd Place)*
**AI:** Uses VS Code Language Model API (GitHub Copilot Chat or GPT-4o) for summaries, a tool-calling Ask AI agent with evidence and confidence, impact scoring and concept tagging; falls back to name matching without a model.
**Architecture:** Extension host in TypeScript with tree-sitter parser and graph builder; webview using Cytoscape.js with cytoscape-elk; AI modules call the VS Code LM API; results cached per workspace.
**Novelty:** Combines a compiler-free C/C++ graph with an agentic Ask AI whose reasoning steps glow on the graph and a risk-scored what-if impact view.
**Scope:** medium · working: Detailed README with commands and settings; reports a 92-file kernel parsing in about 0.1 s; one feature explicitly unfinished. · polish: Settings table, shortcuts table, caching and history; 88 files, about 15.8k lines, has tests.
**Claims:** 92-file teaching kernel parses in about 0.1 s
**Gaps:** track text not published; no video link
Sources: https://devpost.com/software/codegraph-1nj2ku, evidence file README (kx1100/Dubhacks-26), https://dubhacks-2026.devpost.com/

---

### Delta
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** 2nd Place Perceptron: Perception [2nd]

**What it is:** Git-style version control for physical electronics work. An overhead webcam on a Jetson watches a breadboard, logs a commit with before/after photos, a bounding box and an AI description whenever something changes, and offers a web timeline with queries and rewind.
**Problem / user:** Hardware makers and student labs who lose track of what changed on a bench (wrong resistor, undocumented wiring) and have no history like software has.

**Features**
- Automatic change commits — OpenCV waits 1.5 s for the scene to settle, diffs per colour channel with gain correction, filters small noise, and logs a commit. *[shown_working]*
- Component naming — Perceptron Mk 1.5 names parts from zoomed before/after crops and returns structured JSON with boxes, e.g. a 10k resistor at specific holes. *[shown_working]*
- Natural-language queries — Ask when a part was added or what the circuit looked like earlier; answers from commit history. *[claimed]*
- Rewind and compare — Timeline slider, checkpoints, works/broken marks, and a compare-two-points view with restore checklist. *[claimed]*
- Build-guide generation — One button produces a Markdown guide to rebuild the circuit. *[claimed]*
- Multi-user sessions — Supabase row-level security and email invites attribute changes to team members. *[claimed]*

**Flow:** Place a part on the breadboard under the camera → Jetson detects the change and uploads before/after images → Perceptron describes the change; commit appears in the web log → User scrubs the timeline or compares two moments → User asks a question or exports build instructions

**Prompt:** not public / not found
**Fit (implied):** Uses Perceptron Mk 1.5 as the vision-language model for naming components and writing change summaries, with pixel diffing deciding when to call it. Track text itself not found.  *(targeted: 2nd Place Perceptron: Perception)*
**Sponsor tools:** Perceptron Mk 1.5 (Naming components, bounding boxes, scene inventory and change descriptions from image crops, core); NVIDIA Jetson Orin Nano (On-device capture and OpenCV change detection, supporting)
**AI:** Hybrid: deterministic OpenCV pixel diff decides if something changed; Perceptron VLM (low reasoning effort, strict JSON schema, PNG crops, previous scene passed as context) identifies parts; LLM-style Q&A and build guides.
**Architecture:** USB webcam to Jetson (Python/OpenCV) to Perceptron API; commits and JPEGs stored in Supabase Postgres/Storage with realtime push to a React 19 + Vite web app.
**Novelty:** Applies the version-control metaphor to a physical bench with tuned noise thresholds and a split of pixel detection versus VLM naming; includes a custom 3D-printed camera arm and enclosure.
**Scope:** medium · working: Writeup reports end-to-end commits within seconds and 0 false positives over 100 stills; repo clone failed so not verified. · polish: 61 backend and 12 frontend tests plus smoke test claimed; full web UI with many views.
**Claims:** Zero false positives across 100 still frames | All 8 resistor add/remove/no-change cases correct | 61 backend and 12 frontend tests | Low reasoning effort about 5 s per call vs 11-25 s high
**Gaps:** repo clone failed; Perceptron track text not published; video not seen
Sources: https://devpost.com/software/delta-o91du3, https://dubhacks-2026.devpost.com/

---

### Drone Perceptron Relief System
*DubHacks DubHacks '26 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Winner Community Kitchen: 1st Place [1st]

**What it is:** A semi-automatic disaster-relief drone loop: drone footage goes to the Perceptron vision model to find people and estimate distance, detections are written to TigerData, a 2D map of people in need is rendered, and an optimizer chooses the next drone action. The repo is mainly a Monte Carlo simulator and dashboard for a UW campus earthquake scenario.
**Problem / user:** Disaster responders; current drone relief is manual, error-prone under stress and hard to standardize.

**Features**
- Person detection and distance — Perceptron model classifies people in drone footage and estimates their distance. *[claimed]*
- Time-series storage — Detections and telemetry are written to TigerData (Postgres time-series). *[claimed]*
- 2D need map — Projects camera-based 3D positions onto a 2D map of people needing help. *[claimed]*
- Next-drone-decision optimizer — Multi-variable optimizer, reported about 8x faster median response than brute force on benchmarks. *[claimed]*
- Campus Monte Carlo simulator — Event-driven simulation of n drones searching a real UW OpenStreetMap campus for p people and ferrying supplies from a depot, with peak-group search algorithms. *[shown_working]*
- Dashboard and benchmarks — Local web dashboard with replay, time curves and seed-paired benchmarks with 95% confidence intervals. *[shown_working]*

**Flow:** Drones stream footage and telemetry → Perceptron labels people and distances → Data saved to TigerData and shown on a 2D map → Optimizer picks the next drone assignment → Decision feeds back to drones; dashboard replays and compares algorithms

**Prompt:** not public / not found
**Fit (implied):** Community Kitchen title track has no published text found; project addresses disaster response, and also uses Perceptron and TigerData sponsor tools.  *(targeted: Winner Community Kitchen: 1st Place)*
**Sponsor tools:** Perceptron (Classify people in drone footage and estimate distance, core); TigerData (Store time-series detections, supporting)
**AI:** Perceptron vision model for person detection with depth; optimizer is algorithmic search (expected-value and peak-group heuristics against brute force) using a prior density surface from building visitor data.
**Architecture:** Drone feeds to Perceptron to TigerData to 2D map to optimizer back to drones; separate Python simulator, density model from OpenStreetMap building data, and local web dashboard.
**Novelty:** Pairs a perception-to-decision loop with a campus-scale Monte Carlo benchmark using real OSM footprints and building-visitor priors for search and resupply.
**Scope:** medium · working: Repo has simulator, benchmarking and dashboard; the live perception pipeline is described but not evidenced in the README. · polish: Detailed README with demo presets and algorithm notes; 45 files, no tests.
**Claims:** About 8x faster median response than brute force on benchmarks
**Gaps:** track text not published; video not viewable; no evidence the Perceptron-to-TigerData stage is in the repo
Sources: https://devpost.com/software/drone-perceptron-relief-system, evidence file README (ashwin-builds/optimized-drone-search), https://dubhacks-2026.devpost.com/

---

### dump
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** VEYZL: First Place [1st]

**What it is:** A mobile web app where each event gets a temporary photo-and-video room opened by QR code, link or iMessage, with no app or account. Uploads are indexed by AI so guests can find themselves by selfie, search by content, and everything auto-deletes after 24, 48 or 72 hours.
**Problem / user:** Friend groups and event attendees who struggle to pool photos across devices and then find the ones they appear in.

**Features**
- Account-free rooms — Create a dumpster from the site or by texting an iMessage line; unguessable ID link and QR code; PWA; resilient uploads. *[claimed]*
- Find yourself — Sign in with name and selfie; InsightFace groups faces into a gallery; tapping a face filters to that person's media. *[claimed]*
- Universal search and Ask the dump — Search over objects, in-image text, places and spoken words; Backboard answers free-form questions from captions, tags and transcripts. *[claimed]*
- iMessage alerts via Photon — Opt-in texts for new photos of you, your name spoken in a video, and expiry warning; batched about every 90 s. *[claimed]*
- Moments, map, stickers, stage — Time/place bundling with map pins, BiRefNet sticker cutouts, live TV/projector view. *[claimed]*
- Dumpster Fire leaderboard — Emoji reactions with a custom reaction ranking the funniest shots. *[claimed]*
- Auto-deletion and privacy checks — Cleanup worker plus database TTL; CI fails if retention, face-data exposure or identity storage rules are violated. *[claimed]*

**Flow:** Create a dumpster on the site or by texting → Share link or QR code → Guests upload from the phone browser → Guests sign in with a selfie and browse their face gallery or search → Opt in to alerts and react → Room burns after the chosen time and all data is deleted

**Prompt:** VEYZL track text was not published on the Devpost page; the project describes it as auditing AI endpoints for safety. MLH Backboard and Vultr prompts are on the page.
**Fit (explicit):** Pointed VEYZL audits at the public vision endpoint, then added refusals, PII redaction and a second safety check until probes passed; also states the Vultr deployment and also integrates Photon, Perceptron, Backboard, MongoDB and TigerData.  *(targeted: VEYZL: First Place, [MLH] Best Use of Vultr)*
**Sponsor tools:** Perceptron (Captions, tags, objects, OCR text and face boxes per upload, core); VEYZL (Audits of the public vision endpoint and CI privacy rules, core); Photon (iMessage line for creating rooms, sign-in codes and alerts, core); Backboard (Per-dumpster assistant for Ask the dump and iMessage questions, supporting); Vultr (Production Docker Compose host, supporting); MongoDB (App data with TTL expiry, supporting); TigerData (Event metrics and cleanup audit trail, supporting)
**AI:** Hybrid: hosted Perceptron for image understanding, self-hosted InsightFace, faster-whisper and BiRefNet, Backboard LLM assistant for Q&A and command interpretation; every model optional so uploads never block.
**Architecture:** Next.js 15 PWA, background worker for metadata stripping, dedup and model calls, R2 storage, MongoDB plus TigerData, private face and transcription services, all on one Vultr server behind Caddy.
**Novelty:** Privacy-by-design ephemeral photo rooms with no host identity, automated retention checks in CI and a seven-sponsor integration at its own domain.
**Scope:** large · working: Live at dumpster.photo; detailed pipeline and infrastructure description. · polish: Custom visual identity, PWA, copy rewritten for users, deploy health checks.
**Claims:** Integrated seven sponsor tools into one product in a weekend | Vision endpoint moved from failing to passing VEYZL probes before submission
**Gaps:** no repo link; VEYZL track text not published; video not seen
Sources: https://devpost.com/software/dump-imwsvx, https://dubhacks-2026.devpost.com/

---

### Formly - the secure, fast form filler
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** T-Mobile: 1st Place [1st]

**What it is:** A drop-in Fill with Formly button for business forms. A popup lets the user upload files or connect Google, iCloud or T-Mobile, builds a private fact profile (digital twin), fills the form with per-field sources, and returns only the answers the user approves.
**Problem / user:** People who retype the same personal data into long signups and applications; businesses losing users to long forms.

**Features**
- Digital twin — Gemini transcribes uploaded PDFs/images once, DOCX via mammoth, merges into one profile with typed facts tagged by source and sensitivity. *[shown_working]*
- Structured form fill — Business supplies a JSON schema; Gemini returns value, source and confidence per field and leaves blanks when data is missing. *[shown_working]*
- Grounded short answers — Model must quote twin facts before drafting a word-limited answer; code drops answers whose quotes or numbers are absent. *[shown_working]*
- Permission prompts — Ask every time, auto-share basics, or share everything; sensitive fields such as SSN need explicit allow once, always or deny. *[shown_working]*
- Connectors — File upload live; Google and iCloud are mock sign-ins with persona data; T-Mobile mock sign-in calls the real sandbox API. *[shown_working]*
- Four demo merchant forms — T-Mobile signup, SpaceXAI job application, Chase card and California DMV, filled for nine synthetic personas. *[shown_working]*

**Flow:** Press Fill with Formly on a merchant form → Popup asks to connect accounts or upload documents → Formly builds the twin and fills the form → User reviews each answer with its source and approves sensitive fields → Approved answers return to the merchant page via postMessage

**Prompt:** T-Mobile sponsor challenge text was not published on the DubHacks page; the project says it used T-Mobile's hackathon sandbox data.
**Fit (implied):** Includes a T-Mobile connector pulling plan, lines and billing from the hackathon sandbox API plus a T-Mobile signup demo form; the writeup does not explicitly name the challenge.  *(targeted: T-Mobile: 1st Place)*
**Sponsor tools:** T-Mobile sandbox API (Customer context and billing data feeding the twin and the signup demo, supporting); Gemini API (All file reading, twin building, form filling and writing, core); SpaceXAI (Job application demo form, token)
**AI:** Gemini (Flash-Lite and Flash, low thinking, structured JSON output, model fallback) for transcription, twin building, fill and writing; quote-verification step against twin; optional Claude backend with the same prompts.
**Architecture:** Next.js 16 app with SQLite; ingest to twin to /api/fill with merchant schema; popup returns results by postMessage; connectors for uploads, mock Google/iCloud, T-Mobile sandbox.
**Novelty:** Frames form filling as a Stripe-like embeddable button with per-field provenance, Claude Code-style permission prompts and a hallucination guard that blanks unsupported answers.
**Scope:** large · working: Live formly.select, four styled demo forms, nine personas, 107 of 108 field checks reported; 261 files. · polish: Dockerfile, reset tooling, flowchart and UI screenshots, narrated video.
**Claims:** 107 of 108 field checks correct on synthetic set | Fills every field on four demo forms from one Google or iCloud connection
**Gaps:** T-Mobile challenge text not published
Sources: https://devpost.com/software/formly-the-secure-fast-form-filler, evidence file README (salvobonsma/DubHacks2026), https://dubhacks-2026.devpost.com/

---

### Husky Dormers
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** CloudForce: Raffle

**What it is:** A website where UW dorm residents post cooking nights and other gatherings, RSVP with just a name, and share a live editable list of what each person brings. Built by first-time hackers with React/Next.js.
**Problem / user:** UW dorm students with poor dining options, tiny pantries and shared lounge kitchens who struggle to find cooking partners quickly.

**Features**
- Guest RSVP — One tap with only a name; README adds yes/maybe/can't states and a capacity cap, host accounts use username and password. *[shown_working]*
- Event creation with templates — Hosts create events (potluck, pizza night, study break, cooking night) shown in a dorm-level feed with a dorm and floor profile. *[claimed]*
- Live bring-list — Shared list of items with quantities and dietary tags that clients poll about every 2.5 seconds; used to delegate cooking tasks. *[claimed]*
- Quiet-hours warning — Warns when a weeknight event runs past 10pm (README only). *[claimed]*
- Floormate connections and dorm event view — Profiles let students find floormates and browse all events the dorm hosts. *[claimed]*
- AI recipe and event help — Listed on the page as a future goal, not built. *[planned]*

**Flow:** Open the site and browse the dorm's event feed → RSVP with a name as a guest → Sign in as a host and create an event from a template → Participants add items to the shared bring-list

**Prompt:** not public / not found
**Fit (none):** Prize is a raffle with no published challenge; the page names no CloudForce tools. Project fits the cooking-themed title tracks loosely but names none.  *(targeted: CloudForce: Raffle)*
**Sponsor tools:** Tiger Data Postgres (README) (Database via Drizzle ORM; Devpost says Drizzle was dropped but remnants remain, unclear); GoDaddy domain (README deploy notes) (Custom domain huskydormers.us pointed to Vercel, unclear)
**AI:** none
**Architecture:** Next.js 16 App Router with TypeScript and Tailwind, Auth.js credentials login with JWT sessions, Drizzle ORM over a Postgres database, deployed to Vercel; bring-list updates by polling.
**Novelty:** Narrow campus-specific social cooking planner; the shared bring-list with dietary tags is the distinctive piece. No AI in the shipped version.
**Scope:** small · working: Live site huskydormers.us and a README with setup; no video; no tests. · polish: 87 files, about 12k LOC, roadmap and deploy docs; one screenshot captioned main event page.
**Claims:** Design, ease of use and functionality exceeded team expectations
**Gaps:** Devpost lists fewer features than README; feature list follows README plus Devpost; Devpost says Drizzle was removed while README still documents it; no per-prize text for CloudForce Raffle; demo site not opened
Sources: https://devpost.com/software/husky-dormers, https://github.com/agent965/dormplanner, https://dubhacks-2026.devpost.com/

---

### Kill-Switch
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** T-Mobile: 3rd Place [3rd]

**What it is:** An ESP32 breadboard device that turns website risk into physical cues: three LEDs, a buzzer and short LCD messages, driven by a Gemini screen assessment and an APIVoid URL risk score. A kill-switch button texts a caregiver through Twilio.
**Problem / user:** Older adults and people with visual, motor or cognitive disabilities who miss screen-based fraud warnings; caregivers who want to be alerted.

**Features**
- LED risk levels — Three LEDs show low to high risk from a combined AI screen assessment and URL score. *[claimed]*
- Buzzer alerts — Buzzer intensity rises with risk level. *[claimed]*
- Plain-text LCD message — Simple safe, suspicious or risky wording per level. *[claimed]*
- AI screen check — Python captures what is on screen and Gemini judges trustworthiness; result sent to the ESP32 over a COM port. *[claimed]*
- URL risk lookup — ESP32 over Wi-Fi calls APIVoid for the current URL's risk score. *[claimed]*
- Caregiver kill-switch — Pressing the button sends a Twilio SMS to a trusted contact and acknowledges the warning. *[claimed]*

**Flow:** User opens a shopping page → User triggers a screen check → Gemini and APIVoid produce a risk score → LEDs, buzzer and LCD signal the level → User presses the kill-switch to notify a caregiver

**Prompt:** T-Mobile challenge text not published on the DubHacks page.
**Fit (none):** Writeup does not mention T-Mobile; it is an accessibility and fraud-protection hardware device with SMS alerts, so any fit to the sponsor challenge is not stated.  *(targeted: T-Mobile: 3rd Place)*
**AI:** Gemini API assesses a screenshot of the user's current screen for trustworthiness; combined with APIVoid reputation score.
**Architecture:** ESP32 running FreeRTOS tasks for LEDs, LCD, buzzer and URL checks; Python on a PC does screen capture and Gemini calls and talks to the board over serial; Twilio for SMS.
**Novelty:** Moves fraud warnings from the screen into physical signals and a caregiver button, built from leftover university hardware.
**Scope:** tiny · working: Breadboard prototype described; repo has 2 files and about 430 lines, no README. · polish: Authors say it is rough; screen check needs a manual trigger.
**Claims:** Cites $7.7 billion losses to online fraud for Americans 60+ in 2025
**Gaps:** no README; T-Mobile track text not published; no video seen
Sources: https://devpost.com/software/kill-switch-sb82du, evidence file (turboz23/killSwitch, no README), https://dubhacks-2026.devpost.com/

---

### KO.rbit
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SpaceXAI: 1st Place [1st]

**What it is:** A two-player lightsaber duel played with laptop webcam body tracking and an iPhone gyroscope as the blade, preceded by a 3D cockpit where you fly through 31,266 real space objects guided by a Grok voice copilot. Fights happen on Mars (NASA terrain) or Neptune arenas.
**Problem / user:** Players wanting a controller-free, full-body saber duel set in a real-data universe; no stated pain beyond fun.

**Features**
- Real-data universe explorer — 31,266 stars, exoplanets, galaxies, satellites and SpaceX craft from NASA, JPL, CelesTrak and HYG with fact cards, search and 1x/60x/600x time-lapse. *[shown_working]*
- Body plus phone saber — MediaPipe Pose streams at about 30 Hz; iPhone motion sensors aim the saber at about 60 Hz via QR pairing. *[shown_working]*
- Server-authoritative combat — Node/Socket.IO 33 ms tick decides every hit; 100 HP, 15 damage, stamina, guard breaks, rematches, reconnect grace. *[shown_working]*
- LYRA voice copilot — Grok Voice realtime session with short-lived server-minted tokens; read-only access to match state. *[shown_working]*
- Planetary roulette arenas — Random Mars (256x256 NASA MOLA Jezero heightmap) or Neptune arena after a travel cinematic. *[shown_working]*
- Perceptron KO replay — Opt-in clip of up to 45 s; Perceptron Mk1.5 returns scenes and boxes that drive director cuts ending on the server-confirmed finishing blow. *[claimed]*

**Flow:** Commission a pilot and enter the cockpit → Explore or search the real space catalog, ask LYRA → Pick an online rival from the radar → Scan QR code to pair phone saber → Planetary roulette picks arena; duel with body and phone → Optionally generate a cinematic replay

**Prompt:** SpaceXAI track text not published on the DubHacks page; the writeup lists the sponsor tools it used.
**Fit (explicit):** Writeup has a Tracks targeted section naming SpaceXAI: Grok Voice for LYRA, Grok TTS for duel cues, Grok Imagine for the avatar, Grok agents for research and design, Cursor for building, plus SpaceX real-data content.  *(targeted: SpaceXAI: 1st Place)*
**Sponsor tools:** Grok Voice / xAI API (LYRA live voice copilot and duel cue TTS, core); Grok Imagine (LYRA hologram portrait and idle animation, supporting); Cursor (Agent sessions that built much of the code, supporting); Perceptron Mk1.5 (Scene and box extraction for the KO replay, supporting)
**AI:** Grok Voice realtime copilot with read-only tools, Grok TTS and Imagine, Perceptron Mk1.5 for replay scene detection, MediaPipe Pose for body tracking; AI agents also used to build and write.
**Architecture:** React Three Fiber client with MediaPipe on the laptop and phone sensor page; authoritative Node/Socket.IO server; build-time Python importers for space catalogs with SHA-256 provenance.
**Novelty:** Combines a large provenance-tracked real astronomy catalog with a cheat-resistant two-device saber duel; camera input treated as commands that the server verifies.
**Scope:** large · working: Demo video and screenshots; 339 passing tests reported; no hosted URL, runs locally with tunnel. · polish: Attribution file, credits dialog, scene-aware audio; some polish stuck on an unmerged branch.
**Claims:** 31,266 catalogued objects | 339 passing tests (121 server, 218 web) | Built in about 24 hours
**Gaps:** SpaceXAI track text not published; video not viewable
Sources: https://devpost.com/software/space-battles-aei3wz, evidence file README (alnnguyen/Dubhacks26), https://dubhacks-2026.devpost.com/

---

### Lapse
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Visa: Reimagine Shopping; SideShift: 3rd Place [3rd]

**What it is:** A Chrome extension plus backend that collects reward emails forwarded to a private inbox, extracts the offers with a small trained classifier and NER cascade, and at checkout uses a constraint solver to stack coupons, memberships and the best Visa card cashback. A dashboard tracks expiring rewards and savings.
**Problem / user:** Shoppers who hold many loyalty programs and coupons but forget or misuse them; framed around Visa research on unused memberships.

**Features**
- Private reward inbox — Postmark inbound email per user, dedup by Message-ID and content hash, PII redaction before storage. *[shown_working]*
- Reward extraction — SetFit-trained classifier flags reward emails; cascade of JSON-LD, regex, then GLiNER with per-field confidence; low confidence goes to a review queue. *[shown_working]*
- Checkout stacking — OR-Tools CP-SAT enforces one promo code, minimum spend, exclusions and non-combinable pairs and selects the best card; greedy fallback after 200 ms. *[shown_working]*
- Expiry-aware ranking — Rewards expiring within 7 days outrank larger later ones; search score is match x value x urgency without an LLM. *[shown_working]*
- Lapse Sense — Extension recognizes known merchant sites and shows matching rewards before checkout. *[claimed]*
- Dashboard and live updates — React dashboard with savings and calendar, server-sent events, mark-as-used ledger, merchant console previewing email versus extraction. *[shown_working]*

**Flow:** Forward a reward email to the Lapse inbox → Reward appears in the wallet via live toast → Browse to a merchant checkout → Extension popup shows the optimal stack, final price, card and promo code → Click Mark used; savings recorded on the dashboard

**Prompt:** Visa Reimagine Shopping track text was not published on the DubHacks page; README frames the commerce-impact and trust angle for it.
**Fit (explicit):** README has Innovation, User Experience, Technical Execution, Commerce Impact and Trust sections, picks the best Visa card per cart and argues AI only reads emails while spending decisions stay deterministic.  *(targeted: Visa: Reimagine Shopping, SideShift: 3rd Place)*
**Sponsor tools:** Visa (card benefits as domain input) (Best-card cashback selection in the stacking model, supporting); Postmark (Inbound email inboxes, supporting)
**AI:** Self-trained SetFit reward classifier, pretrained GLiNER entity extraction, Presidio redaction and optional MiniLM search; AI only reads emails and all money decisions come from the CP-SAT solver and arithmetic.
**Architecture:** Postmark intake into FastAPI/Postgres (pgvector, pgcrypto), classification and extraction pipeline, CP-SAT stacking engine, WXT React MV3 extension and React dashboard with SSE.
**Novelty:** Treats checkout as a constraint-satisfaction problem and deliberately keeps the LLM out of financial decisions to resist prompt injection from emails.
**Scope:** large · working: Runs locally in memory mode; 494 backend tests pass per README; 296 files, about 24.7k lines. · polish: Brutalist visual identity, merchant console, detailed README and awards badges.
**Claims:** 494 backend tests pass | Two sequential 10% discounts yield 19% savings, modelled correctly | Runs fully locally with no outside calls
**Gaps:** Visa and SideShift track text not published; video not seen; Devpost says everything runs locally but README lists Postmark inbound email
Sources: https://devpost.com/software/vouch-ld4voh, evidence file README (asyaafv/DubHacks26), https://dubhacks-2026.devpost.com/

---

### Make a Drink!
*DubHacks DubHacks '26 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Freshman Beginner Project

**What it is:** A browser-based 3D virtual bar where players learn cocktail recipes, pour and mix drinks, and serve customers generated by Gemini. A memory service tracks each player's recurring mistakes to steer practice.
**Problem / user:** Aspiring bartenders under 21 or without bar access cannot buy alcohol or get licensed, so they have no hands-on way to learn mixology.

**Features**
- Virtual bar for recipe practice — Three.js/react-three-fiber bar station where the player learns and mixes cocktails and serves them. *[claimed]*
- Guide toggle — Player can turn the recipe guide off to pour from memory. *[claimed]*
- AI-generated customers and orders — Gemini creates each customer and their order, with adjustable preferences; hard-coded fallback orders when no Gemini API is available. *[claimed]*
- Gemini drink scoring — Gemini rates each served drink for accuracy against the recipe. *[claimed]*
- Per-player memory — Backboard stores common mistakes so later practice targets weak spots. *[claimed]*
- Physics ice tray — Rapier physics simulates ice in an ice tray. *[claimed]*

**Flow:** Open the web bar → Learn a recipe with the guide on, or turn it off → Mix the drink at the station → Serve the Gemini-generated customer → Receive an accuracy score → Memory shapes later practice

**Prompt:** not public / not found
**Fit (none):** Event-run beginner award with no published criteria; page makes no claim about it.  *(targeted: Best Freshman Beginner Project)*
**Sponsor tools:** Backboard (Per-player memory of frequent mistakes, supporting); Google Gemini (Customer and order generation and drink scoring, core)
**AI:** Gemini generates customer personas and orders and grades drink accuracy; Backboard supplies persistent per-player memory to bias practice; Claude is listed in built-with without a described role.
**Architecture:** Next.js/TypeScript app with Three.js scene and Rapier physics deployed on Vercel; server calls to Gemini and Backboard.
**Novelty:** Pairs a 3D pouring game with LLM-generated customers and persistent weakness tracking, aimed at a legal-age barrier to learning mixology.
**Scope:** small · working: Live Vercel demo linked; no repo or video; page gives no measured results. · polish: Page lists a coherent stack; no screenshots or video were described.
**Gaps:** no repository linked; live demo not opened; no challenges or next steps on page
Sources: https://devpost.com/software/make-a-drink-3ful2k

---

### Noxen
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SideShift: 2nd Place [2nd]; DubHacks Next: 1st Place [1st]

**What it is:** An automated nightly facility-inspection loop: a Unitree L2 LiDAR plus camera scans a space and is diffed against a baseline, Perceptron triages each change as routine or flagged, and a camera-only Scout drone is dispatched to flagged spots. Engineers get a map dashboard and iMessage alerts.
**Problem / user:** Facility operators and construction managers whose inspections are manual, costly and infrequent, leaving problems unseen between visits.

**Features**
- Baseline and change detection — Open3D aligns each scan to a baseline and finds added, removed, moved or recoloured objects, with ray casting to separate occluded from removed; thresholds tuned to about 2 cm sensor noise. *[shown_working]*
- VLM triage — Perceptron Mk1.5 classifies each before/after pair into a configured category with severity and one-line rationale; routine moves stay quiet. *[claimed]*
- Engineer dashboard — FastAPI + React + three.js app pins issues on a 3D map with before/after crops, live websocket feed and confirm or false-alarm feedback. *[shown_working]*
- Photon iMessage alerts — Texts flagged changes with crops; a reply such as LOOK dispatches the Scout. *[claimed]*
- Camera-only Scout drone — Localizes in the prior LiDAR map from camera landmarks, avoids new obstacles with Depth Anything V2 scaled by the map plus a YOLO backup. *[claimed]*
- Battery hot-swap — Mechanism lets the Scout land, swap packs and relaunch without powering down. *[claimed]*

**Flow:** Scan the space once to set the baseline → Nightly scan is aligned and diffed → Perceptron triages changes; dashboard pins flagged ones → Engineer receives an iMessage alert and replies to send the Scout → Scout flies to the spot and returns close-up footage → Engineer marks confirmed or false alarm

**Prompt:** DubHacks Next, SideShift and Cook Smarter track texts not published on the DubHacks page.
**Fit (explicit):** Writeup has an explicit section titled why this is Cook Smarter, arguing it automates inspection triage; also pitches a startup path with customer calls and per-system subscription, relevant to the startup-oriented tracks.  *(targeted: SideShift: 2nd Place, DubHacks Next: 1st Place, Cook Smarter)*
**Sponsor tools:** Perceptron Mk1.5 (Classifying each change with severity and rationale, core); Photon (iMessage alerts and reply-to-dispatch, supporting)
**AI:** Perceptron VLM for change triage; Depth Anything V2 monocular depth scaled with the LiDAR map; YOLO safety check; OpenAI as fallback classifier; feedback logged for learning.
**Architecture:** ROS 2 and Python capture from L2 and camera, Open3D registration and diff, classifier adapter, FastAPI server with websockets and React dashboard, Photon alerts, separate Scout flight stack with PX4.
**Novelty:** Camera-only drone localization inside a LiDAR-built map plus a custom battery hot-swap, built by a two-person team across hardware and software.
**Scope:** large · working: Status table: pipeline tests pass on synthetic and recorded L2 data; Scout stability flight-tested; live hardware run and relocalization on real map pending at README time. · polish: Dashboard, docs folder with decisions and setup, synthetic scenarios; 301 files, about 23.8k lines, tests present.
**Claims:** Built by a team of two in one weekend | No-change scans must produce zero events (required test)
**Gaps:** track texts not published; video not viewable
Sources: https://devpost.com/software/noxen, evidence file README (RonRastorguev/noxendh), https://dubhacks-2026.devpost.com/

---

### Octaby
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** SideShift: 1st Place [1st]

**What it is:** A soft fabric wristband with four vibration motors, one per cardinal direction, that tells blind or low-vision users which way to move their hand to reach an object. A spoken request and a phone camera feed a grounding backend that is meant to drive the motors via BLE.
**Problem / user:** Blind and low-vision users who lack tools for small tasks such as finding and reaching an object on a table; inspired by a friend temporarily unable to see.

**Features**
- Four-motor directional wristband — Sewn fabric band with conductive thread; motor combinations signal the direction to move the hand. *[shown_working]*
- Spoken object request — Phone posts audio and camera frame to a FastAPI endpoint; OpenAI transcribes and extracts intent, then Perceptron grounds the object. *[claimed]*
- Guidance logic and BLE output — Swift packages with guidance logic, an output gate and BLE link to a Circuit Playground Bluefruit. *[claimed]*
- Object memory — Saves specific objects for later; backend memory routes are still stubs per README. *[planned]*
- ARKit/LiDAR geometry — Live reaching integration and GeometryCore remain incomplete. *[planned]*

**Flow:** User states which object they want → Phone camera frame and audio go to the backend → Perceptron locates the object and guidance is computed → Wristband vibrates to indicate the direction to move the hand

**Prompt:** SideShift track text not published on the DubHacks page; track prizes include cash plus interview or work trial.
**Fit (none):** Writeup does not name the track; it is an assistive wearable prototype. Link to the sponsor challenge is not stated.  *(targeted: SideShift: 1st Place)*
**Sponsor tools:** Perceptron (Visual grounding of the requested object and conversion to guidance signals, core)
**AI:** OpenAI for speech transcription and intent extraction; Perceptron for object grounding in the camera frame; Swift ARKit/LiDAR for geometry (incomplete).
**Architecture:** Swift iPhone app, FastAPI backend on AWS, Circuit Playground Bluefruit firmware over BLE driving four haptic motors; contracts and fixtures shared in one repo; separate synthetic world-model viewer.
**Novelty:** Pivoted mid-event from a rigid servo bracelet to a sewn haptic wristband; repo shows extensive spec-driven agentic planning documents.
**Scope:** large · working: Photos of the final fabric band; README admits memory routes are 501 stubs and live reaching integration unfinished. · polish: 992 files, about 98k lines, tests, runbooks and specs; final-product and testing photos.
**Gaps:** SideShift text not published; repo is much larger than the described hackathon prototype; only README read
Sources: https://devpost.com/software/octaby, evidence file README (Eddwal/haptic-reach-demo), https://dubhacks-2026.devpost.com/

---

### OpenCanopy
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** DubHacks Next: 2nd Place [2nd]; 1st Place Perceptron: Perception [1st]

**What it is:** A web tool that checks one land plot in one click for forest cleared after the EU deforestation cutoff of end 2020. It combines Sentinel-2 imagery, Hansen loss and JRC forest maps with Perceptron vision outlines of converted areas, and outputs a printable evidence case file.
**Problem / user:** Regulators, importers and communities who must verify EU Deforestation Regulation compliance per plot but find GIS-based checks slow and expert-only.

**Features**
- Plot input — Draw a box or shape, or upload GeoJSON, KML or GPX. *[shown_working]*
- Satellite record — Clearest Sentinel-2 scene before cutoff and now plus a yearly series with slider and playback; Hansen loss-year and JRC 2020 forest overlays. *[shown_working]*
- Perceptron conversion detection — Perceptron Mk1.5 reads before/after pairs or a year-by-year video and boxes regions that look like plantations, roads or blocks. *[shown_working]*
- Loss-map cross-check — Region confirmed only if at least 25% of it has post-2020 loss; otherwise marked inconclusive for a human. *[shown_working]*
- Printable case file — Evidence dossier with numbered exhibits, scene IDs, dates, cloud cover, before/after slider, flicker mode and loss-by-year chart. *[shown_working]*
- Global clearing sweep — Indexed 10-degree tiles worldwide, polygonized clearings over 10 ha, asked Perceptron per chip on UW Hyak via Slurm; 69 flagged as plantation. *[claimed]*

**Flow:** Draw or upload a plot on the map → Pipeline fetches imagery and loss layers → Scrub years and view overlays → Perceptron regions are cross-checked against loss pixels → Open the printable case file with the single permitted conclusion sentence

**Prompt:** Perceptron: Perception and DubHacks Next track texts not published on the DubHacks page.
**Fit (explicit):** Has a Why Perceptron section: Mk1.5 is the engine for judging land conversion from time-lapse imagery with boxes, benchmarked on labeled chips (100% precision, 67% recall) and used in a global sweep.  *(targeted: 1st Place Perceptron: Perception, DubHacks Next: 2nd Place)*
**Sponsor tools:** Perceptron Mk1.5 (Conversion detection from image pairs and yearly video, with localization boxes, core); Cursor (Writing the pipeline, server and site, supporting)
**AI:** Perceptron Mk1.5 vision-language model with a prompt tuned for oil palm texture; outputs gated by deterministic comparison to Hansen loss pixels; one-word answers with reasoning off for batch runs.
**Architecture:** Python server /api/analyze pulling Sentinel-2 from Microsoft Planetary Computer and clipping Hansen/JRC rasters with rasterio; Perceptron calls; plain HTML/JS front end with MapLibre and printable dossier.
**Novelty:** Deliberately constrained output (one allowed sentence, inconclusive state) and a planet-wide sweep of post-2020 clearings, with measured prompt tuning (8/16 generic prompt vs 16/16 precision tuned).
**Scope:** medium · working: Live opencanopy.world and sample Borneo plot result (about 880 ha lost); benchmark numbers reported; no public repo in our data. · polish: Scroll-driven landing page, print-ready dossier, careful wording, sources list.
**Claims:** About 880 ha cleared (20% of sample Borneo plot), mostly 2023 | 100% precision, 67% recall on a 48-chip test | 69 clearings flagged as plantation worldwide | Perceptron call averages 6.8 s
**Gaps:** no repo link; track texts not published; video not seen
Sources: https://devpost.com/software/clearcut-p5hmfx, https://dubhacks-2026.devpost.com/

---

### PathWise
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** CloudForce: Most Creative

**What it is:** A React Native walking app for the UW campus area that offers a fastest route and a safer route weighted by streetlights, open places, sidewalks and crosswalks, with opt-in iMessage alerts to a friend who watches the walk.
**Problem / user:** People walking home near UW, especially after dark, who get shortest-path routes through dark or empty blocks, and friends who want to know they arrived.

**Features**
- Fastest versus safer route — OpenStreetMap pedestrian graph; safer cost multiplies time by one plus lambda times an edge penalty, capped at 1.3 times fastest time. *[shown_working]*
- Four-signal safety penalty — Weights streetlights 0.40, open places 0.30, sidewalks 0.20, crosswalks 0.10 from Seattle open data; missing data is not penalized. *[claimed]*
- Heading card and off-path reroute — Shows current street and miles left; detects leaving the path and recalculates from the real location. *[claimed]*
- Opt-in friend watching over iMessage — Friend texts an assigned Photon number once as consent; watcher is texted if walker stops, leaves path, reroutes or arrives. *[shown_working]*
- Stillness heartbeat — Periodic heartbeat keeps the stillness timer running when phones stop sending location. *[claimed]*
- Walk Buddy Q&A — README: OpenAI-backed question answering, answers optionally recorded for a VEYZL audit; not mentioned on Devpost. *[claimed]*

**Flow:** Pick a destination near campus → Compare fastest and safer routes → Select watchers who already texted their number → Walk following the heading card → Rerouting and alerts trigger if the walker strays or stops → Watcher is notified on arrival

**Prompt:** not public / not found
**Fit (none):** CloudForce prize text is not published; the page does not name CloudForce or Salesforce tools. Photon iMessage is used for watcher alerts, but a Photon prize is not listed.  *(targeted: CloudForce: Most Creative)*
**Sponsor tools:** Photon (Shared iMessage lines giving each friend a number for alerts, core); VEYZL (README only: optional audit logging of Walk Buddy answers, token)
**AI:** No ML in routing on the Devpost page; README mentions an OpenAI-backed Walk Buddy Q&A feature.
**Architecture:** Expo React Native app talks to a FastAPI server with PostgreSQL/SQLAlchemy and JWT auth; routing runs on a precomputed OSM walk graph enriched with Seattle open data; Photon sends iMessage alerts.
**Novelty:** Concrete weighted safety cost model with a bounded detour, and consent-based friend alerts that require no app install for watchers.
**Scope:** medium · working: Demo video linked and detailed README with ingest script; no hosted app, no tests. · polish: 139 files, about 7k LOC, thorough setup docs; requires Expo Go and Python/Node setup.
**Claims:** Safer route capped at 30 percent longer than fastest | Four weighted safety signals from city open data
**Gaps:** video not viewed; CloudForce prize text unavailable; Walk Buddy and VEYZL appear only in README
Sources: https://devpost.com/software/pathwise-zm305y, https://github.com/Ethant06/PathWise, https://dubhacks-2026.devpost.com/

---

### Pollensight
*DubHacks DubHacks '26 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Community Kitchen: 2nd Place [2nd]

**What it is:** A pipeline and web app that turns fixed-camera field video into per-flower insect visit records, forecasts the insect's next path, and plans a robot pollination route to missed flowers. It also includes an RL-trained bee simulated in 3D and in MuJoCo with a Crazyflie drone model.
**Problem / user:** Growers and pollination robotics researchers who need to know which flowers pollinators visited; framed around pollinator decline.

**Features**
- Insect tracking and visit detection — OpenCV background subtraction and DP path linking; 160 px crops every 0.5 s verified by Perceptron Mk1.5, path kept if at least 70% confirmed; flowers boxed by Mk1.5 for stable IDs. *[shown_working]*
- Natural-language search — Plain-English queries across clips jump the video to the matching moment. *[shown_working]*
- Analytics — Visits, dwell, transit time, flight speed, revisits and a time-spent heatmap. *[shown_working]*
- Path and next-flower forecast — kNN path fan for the next 2 s, gradient-boosted next-flower odds and Monte Carlo rollouts, trained on 2,335 real flights. *[shown_working]*
- Field route planner — Flowers coloured by remaining visits and a greedy plus 2-opt orienteering route within a time budget. *[shown_working]*
- RL bee simulation — Gymnasium PPO bee flies over unseen random fields in a three.js view and a MuJoCo replay. *[shown_working]*
- Upload your own video — Runs the pipeline on a user's fixed-camera clip. *[claimed]*

**Flow:** Pick a clip or upload a fixed-camera video → Watch tracked insects and flower boxes light up on visits → Search or review analytics and heatmap → Open Forecast to see predicted path and next flower → Open Field for the robot route, or Simulations for the RL bee

**Prompt:** Community Kitchen track text not published on the DubHacks page.
**Fit (none):** Writeup does not name the track; it is an agricultural-perception and robotics project using Perceptron as the verifier. Connection to the open track is not stated.  *(targeted: Winner Community Kitchen: 2nd Place)*
**Sponsor tools:** Perceptron Mk1.5 (Verify insect crops, detect flowers, search and video clip annotations; cached client, core); Cursor (Listed in built-with, token)
**AI:** Hybrid classical tracker plus Perceptron Mk1.5 verification, scikit-learn forecasting, PPO reinforcement learning bee, orienteering planner.
**Architecture:** Python perception writes JSON contract files (tracks, field, plan, search) validated by a script; analytics/forecast/sim modules read them; React/Vite app serves video and runs Python via API routes.
**Novelty:** Cheap tracker plus VLM spot-check cut false visits; fixed JSON contracts among four developers; sim links perception to a robot-route and RL drone demo, with a reproducible cached offline replay.
**Scope:** large · working: Results table on 48 public clips with accuracy numbers, 45 offline tests and 144 validated data files reported. · polish: Architecture diagram, dataset audits, contract doc; 11k files, about 15.7k code lines.
**Claims:** 90% of detected visits real with Mk1.5 vs 64% without | Flower detection 98% precision, 87% recall | Next-flower right in top 3 79% of the time on unseen cameras | Robot route delivers 39-56% of missed visits in 30 s | 45 tests and 144/144 data files validate
**Gaps:** track text not published; video not viewable
Sources: https://devpost.com/software/beebot-zbaxvy, evidence file README (b-ananya/pollensight), https://dubhacks-2026.devpost.com/

---

### ReMind
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** 2nd Place Perceptron: Robotics [2nd]; [MLH] Best Use of Backboard

**What it is:** A voice companion for people with dementia that a caregiver sets up and supervises. The resident talks to it, a calm screen shows a photo or words, and an SO-101 robot arm shuffles three keychains for a remember-the-order game; worrying statements trigger a text to the caregiver.
**Problem / user:** Nursing home residents with dementia who need staff-led activities and understaffed carers; caregivers get plain session notes.

**Features**
- Remember the Order shuffle game — Resident asks by voice; SO-101 arm shuffles keychains using taught positions with camera verification; resident reorders by hand. *[shown_working]*
- Cognitive Stimulation conversation games — Famous faces, finishing sayings and everyday sounds, no scores and no wrong answers. *[claimed]*
- Voice companion — Gemini Live through Backboard Realtime with long-term memory per resident; backend relays audio; 1.2 s silence before replying. *[claimed]*
- Caregiver alert — Gemini judges worrying statements such as a fall or chest pain, reassures the resident and texts a summary via Photon. *[claimed]*
- Allowlisted robot control — AI may only request jobs from a short list; server and robot worker re-check allowlist and joint limits. *[shown_working]*
- Nurse dashboard — Session summaries and care-profile edits stored in MongoDB. *[claimed]*

**Flow:** Caregiver enters the resident name and picks games → Resident talks to ReMind by voice → Asks for the shuffle game; arm shuffles keychains → Resident reorders them by hand → Caregiver reads plain notes; urgent statements trigger an iMessage

**Prompt:** Perceptron Robotics track text not published on the DubHacks page; MLH Backboard prize text is on the page (stateless APIs need persistent memory; one unified API for memory, RAG and routing).
**Fit (explicit):** README header names Community Kitchen, Perceptron Robotics and MongoDB; policies trained on Perceptron's cloud and run on the arm; every voice call and long-term resident memory goes through Backboard.  *(targeted: 2nd Place Perceptron: Robotics, [MLH] Best Use of Backboard)*
**Sponsor tools:** Perceptron Robotics platform (Training SO-101 policies from 60 demonstrations; worker has a perceptron mode, supporting); Backboard (Realtime voice via Gemini Live plus long-term resident memory, core); Photon (iMessage caregiver alerts via a Node service, supporting); MongoDB Atlas (Persist residents, profiles and session summaries, supporting)
**AI:** Gemini Live voice agent with a validated tool allowlist, Gemini deciding which statements need an alert, LeRobot imitation-learning policies (weak grasp); demo uses scripted taught positions with camera check.
**Architecture:** Next.js frontend, FastAPI orchestrator with state machine and MongoDB, robot_worker on port 8001 (mock or Perceptron mode), small Node Photon service; Backboard relays Gemini Live audio.
**Novelty:** Safety enforced in server and robot code rather than prompt; candid reporting that the learned policy cannot grasp and the demo uses camera-verified scripted moves.
**Scope:** medium · working: Two of five shuffles verified in both directions; three stall; learned grasp unreliable after 1,000 steps; mock-mode runs out of the box. · polish: Spec, contracts, training docs, calm design system, 204 files, about 22.9k lines, tests.
**Claims:** 60 demonstrations recorded (12 for each of five shuffles) | Re-picks at the empty slot worked 5 out of 7 times
**Gaps:** Perceptron Robotics track text not published; video not seen
Sources: https://devpost.com/software/remind-y8kg9s, evidence file README (remind-dubhacks/dubhacks-2026), https://dubhacks-2026.devpost.com/

---

### Robo-view
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** 1st Place Perceptron: Robotics [1st]

**What it is:** A phone web app where a user speaks or types a request and an SO-101 robot arm with a wrist camera films a product with one of three cinematic moves, then returns the clip to the app at the requested length. Perceptron Mk1.5 parses the request and picks the angle.
**Problem / user:** Small sellers and creators who want dynamic product-ad footage without manual camera work.

**Features**
- Voice or text command — PWA sends the request to a FastAPI orchestrator; Mk1.5 interprets it and chooses the angle. *[claimed]*
- Three cinematic arm movements — Arm rotates and traverses around a product using a trained movement policy; about 25 demonstrations per move, roughly 75 total. *[shown_working]*
- Video return — Arm records and the clip is sent back to the app at the requested duration. *[claimed]*
- Adaptation to object position — Policy trained to replicate moves for different object placements and requested angles. *[claimed]*

**Flow:** User opens the phone app and states the shot wanted → Mk1.5 parses request into an angle and length → Arm performs the move and records → Clip returns to the app

**Prompt:** Perceptron Robotics track text not published on the DubHacks page (README refers to a workshop doc covering the Isaac 0.5 API, Mk1.5 and the arm contract).
**Fit (explicit):** README states DubHacks 2026 Perceptron Robotics track; uses Mk1.5 for request parsing and angle choice, Isaac 0.5 policy trained on teleoperated SO-101 demos, and Perceptron API for bounding-box relabelling.  *(targeted: 1st Place Perceptron: Robotics)*
**Sponsor tools:** Perceptron Mk1.5 (Parse user request and pick camera angle; relabel demos with boxes, core); Isaac 0.5 (Train the arm movement policy from demonstrations, core)
**AI:** Perceptron Mk1.5 for language-to-shot decisions; Isaac 0.5 vision-language-action style model trained on leader-follower teleoperation data.
**Architecture:** Vite/React PWA, FastAPI server orchestrating, robot module for arm control and VLA client, ml module for prompts and training, shared schemas.
**Novelty:** Applies imitation-learned robot motion to automated product cinematography with phone-driven requests.
**Scope:** small · working: Writeup says the arm was trained and ran successfully; photo of the arm; no demo link in data. · polish: Repo has planning docs and tests across 100 files, about 7.7k lines; Devpost writeup is brief.
**Claims:** About 75 demonstrations recorded, 25 per movement
**Gaps:** track text not published; video not seen
Sources: https://devpost.com/software/robo-view, evidence file README (kaleturner/dubhacks_2026), https://dubhacks-2026.devpost.com/

---

### Saykind
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** CloudForce: Most Viral

**What it is:** A calm browser app for adults with aphasia: four levels from single-word practice to ordering at a talking cafe to everyday phrases, plus a help-message drafter and a shareable report for clinicians. Designed to avoid scores, timers and baby talk.
**Problem / user:** Adults with aphasia after stroke, plus caregivers and speech-language pathologists, who lack dignified, low-pressure ways to practice everyday words and real conversations.

**Features**
- Level 1 word practice — Six words (e.g. chair, mug) with picture, syllables, normal and slow audio, first-sound hints and unlimited speaking tries. *[shown_working]*
- Level 2 camera object discovery — Perceptron object detection on camera frames labels items; tap to hear and say the word; optional with Skip. *[claimed]*
- Level 3 cafe with barista Sam — Order by voice or tapping menu; Claude plays Sam asking one short question at a time, ElevenLabs speech in and out, server validates the order. *[shown_working]*
- Level 4 real-world phrases — Ready phrases to rehearse, play aloud or show at a counter, with optional recording. *[claimed]*
- Get Help drafter — Call button and drafted message the user edits and sends from their own phone; app never sends on its own. *[claimed]*
- Doctor report and caregiver view — Claude writes a short summary previewed before Email, Share, PDF or Copy; caregiver page shows only enabled data; template fallback. *[claimed]*
- Dignity-first tone and privacy — Phrase filter blocks pity and baby talk; no scores or wrong messages; logs stay on device; per-visitor rate limits. *[claimed]*

**Flow:** Open the site in a phone or desktop browser at Level 1 → Hear a word, use hints, say it → Optionally scan the room with the camera → Order at the cafe by voice or tapping → Rehearse real-world phrases → Draft a help message or doctor report and share it from their own device

**Prompt:** not public / not found
**Fit (none):** CloudForce prize text is not published and page names no CloudForce tools; it does use Perceptron, ElevenLabs and Claude, but no matching prize is stated.  *(targeted: CloudForce: Most Viral)*
**Sponsor tools:** Perceptron (Native bounding-box object detection for Level 2, supporting); ElevenLabs (Scribe speech-to-text and Flash v2.5 voice for Sam, core); Anthropic Claude Haiku (Plays Sam and writes the doctor report, core)
**AI:** Claude Haiku roleplays the barista under server-side schema validation (zod) with one correction pass; ElevenLabs does speech in and out; Perceptron detects objects; phrase filters enforce tone; OpenAI optional fallback.
**Architecture:** Next.js 16 / React 19 web app using React Native Web, server routes call AI providers with keys kept server-side; state stays on device; 86 pre-made practice audio files; deployed on Vercel.
**Novelty:** Accessibility-first design for aphasia with explicit status labelling (working/prototype/not done) in the README and a ban on scoring or pity language.
**Scope:** medium · working: Live Vercel demo and YouTube video; README marks what was tested, notes nothing tried on a real phone and mocked providers in browser suite. · polish: 328 files, about 23k LOC, 205 unit tests, axe and UI audit, original artwork, UI integration docs.
**Claims:** 205 unit tests plus mocked-provider browser suites | Camera latency cut from about 2.6 s to 0.6 to 1.2 s | Zero axe or UI-audit findings across 13 screens | About 1 in 3 stroke survivors develop aphasia
**Gaps:** video not viewed; CloudForce prize text unavailable; README (truncated) rates Level 2 and adaptive difficulty as prototype
Sources: https://devpost.com/software/saykind, https://github.com/pranay-ratan/saykind, https://dubhacks-2026.devpost.com/

---

### SonoRocky
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** 3rd Place Perceptron: Perception [3rd]

**What it is:** A phone web app that narrates the camera view in short spoken language, paired with an ESP8266 ultrasonic sensor clamped on a cane that sends distance over Wi-Fi and is turned into variable-frequency beeps. Users can also ask questions about what is ahead and have text read aloud.
**Problem / user:** Visually impaired students and pedestrians whose cane detects only nearby obstacles; cites mobility-injury survey data from campus experience.

**Features**
- Scene narration — Perceptron Mk1.5 reads still frames at a dynamic frame rate and returns natural-language descriptions with hazard alerts in under 2 s. *[shown_working]*
- Spoken output — ElevenLabs TTS streams the descriptions; hazards come before minor details and output length is capped for speed. *[shown_working]*
- Cane distance beeps — Ultrasonic sensor on an ESP8266 posts distances to the backend; app plays beeps whose frequency varies with distance. *[shown_working]*
- Questions and text reading — User prompts the model about the surroundings or asks it to read text on walls. *[claimed]*
- Stair estimation — Estimates the minimal number of stairs to prevent trips. *[claimed]*
- 3D-printed clamp housing — Fusion 360 / Prusa-printed housing that fits rods of varying diameters. *[shown_working]*

**Flow:** User opens the app on a phone and clamps the sensor on a cane → Camera frames are analysed and spoken as short hazard-first descriptions → Cane sensor distance becomes faster or higher beeps near obstacles → User asks a question or asks to read text

**Prompt:** Perceptron: Perception track text not published on the DubHacks page.
**Fit (implied):** Perceptron Mk1.5 is the vision engine for real-time scene description with hazard prioritisation; writeup thanks a Perceptron mentor but does not state the track.  *(targeted: 3rd Place Perceptron: Perception)*
**Sponsor tools:** Perceptron Mk1.5 (Frame-by-frame scene description and hazard alerts, core); ElevenLabs (Streaming TTS of descriptions, supporting)
**AI:** Perceptron Mk1.5 vision-language model on camera stills at adaptive FPS; ElevenLabs TTS; no custom model training.
**Architecture:** Phone browser frontend captures camera; backend routes frames to Perceptron and audio to ElevenLabs, and receives POST distance packets from the ESP8266; supports multiple client devices.
**Novelty:** Combines VLM narration with a sub-$15 cane sensor that sonifies distance; hazards-first short phrasing tuned for latency and rate limits.
**Scope:** small · working: Five screenshots incl. debug UI and cane prototype; repo has narrator code, about 3.9k lines, no tests. · polish: Printed housing and history/voice UI shown; repo README minimal.
**Claims:** Hardware cost under $15 | Description latency under 2 seconds
**Gaps:** track text not published; README has no feature content
Sources: https://devpost.com/software/walk-safer, evidence file (tsengjohn44-lgtm/dh26-project, README is a stub), https://dubhacks-2026.devpost.com/

---

### Starward
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** T-Mobile: 2nd Place [2nd]

**What it is:** A Flask web app for planning hikes with satellite texting. Given a trail, date, phone and carrier, it estimates where satellite messaging will work, suggests check-in spots and whether a satellite add-on is worth buying, and shares the plan with an emergency contact by text.
**Problem / user:** Hikers in the Pacific Northwest who lose cell coverage, and the contacts who worry about them; avoids buying costly satellite gear unnecessarily.

**Features**
- Satellite coverage estimate along a trail — Combines CelesTrak orbit data (Skyfield/SGP4), OpenStreetMap routes, Copernicus terrain horizons and a hand-estimated canopy to score sky openness per point. *[shown_working]*
- Color-coded Folium coverage map — Shows stronger and weaker estimated connectivity along four built trails, with a toggle previewing a T-Satellite add-on. *[shown_working]*
- Check-in spot and time suggestions — Uses hiking-pace estimates and satellite pass windows when a trip date is given. *[shown_working]*
- Plan recommendation engine — Matches phone and carrier to a catalog and favors the cheapest option, including recommending no purchase; also handles groups. *[shown_working]*
- Trip-plan sharing by text — Flask calls a Node Photon/Spectrum bridge to send the plan; Demo Mode only previews messages. *[claimed]*
- Missed check-in alert — Drafts or sends an alert to the emergency contact, never to emergency services. *[claimed]*
- Group planning and T-Mobile pitch page — Lets extra hikers be added for a joint recommendation; a /pitch/tmobile page exists. *[claimed]*

**Flow:** Enter trail, date, start time, phone, carrier → Generate trip plan → Review coverage map and check-in suggestions → Toggle T-Satellite to compare → Read the buy or do-not-buy recommendation → Share plan with emergency contact → Preview a missed check-in alert

**Prompt:** not public / not found
**Fit (explicit):** Recommendation engine centers on T-Mobile T-Satellite versus other satellite plans, with a dedicated pitch page; Photon bridge carries trip sharing and check-ins. T-Mobile challenge text itself was not published.  *(targeted: T-Mobile (2nd place), Photon agent track (README mentions Track D))*
**Sponsor tools:** Photon Spectrum (Outbound trip-plan texts and inbound check-ins through a Node bridge, supporting); T-Mobile T-Satellite (Modelled as a purchasable add-on in the recommendation engine, supporting)
**AI:** No model inference in the product; coverage and recommendations are deterministic orbit, terrain and catalog logic. Cursor and Claude Code were used to build it.
**Architecture:** Flask app (coverage.py, orbits.py, recommend.py, guardian.py) reading JSON trail, phone and carrier data; Folium renders the map; a Node bridge talks to Photon Spectrum for SMS.
**Novelty:** Combines real satellite orbit propagation and terrain horizons with a carrier-plan purchase advisor that may say buy nothing; unusual for a hackathon safety app.
**Scope:** medium · working: Live Render demo link, localhost Demo Mode, scripted two-minute demo, tests directory. · polish: Detailed README with endpoints and honest real-vs-estimated section; no video.
**Claims:** Predictions are labelled estimates, not guarantees | Recommendation avoids pushing purchases
**Gaps:** T-Mobile challenge text not published; no video
Sources: https://devpost.com/software/starward, evidence/dubhacks-dubhacks-26-starward.json (README), https://dubhacks-2026.devpost.com/

---

### Tenant
*DubHacks DubHacks '26 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Photon: Track Winner

**What it is:** Scan a QR card in a room and chat with the room to borrow nearby devices (a phone's flashlight, a Mac's music, volume and speech) for a ten-minute lease, with no app or account. Also reachable over iMessage via a Photon number.
**Problem / user:** Guests in spaces they do not own (hospital, hotel, rental) cannot use the room's devices without staff or the owner's accounts; hosts need access that ends cleanly.

**Features**
- QR join and chat control — Scanning the card opens a chat; an agent turns plain requests like turn on a light into device commands and replies in one sentence. *[shown_working]*
- Ten-minute device leases — Access is a time-limited lease on specific devices checked at each action; text leave ends it early and later requests are refused. *[shown_working]*
- Host reset key — One key ends all leases, turns off lights and music, rotates the room code and clears the log in about a second. *[shown_working]*
- Real device control — iPhone web pages drive the torch via Safari with Wake Lock; a Mac script uses AppleScript for Music, volume and speech. *[shown_working]*
- iMessage access — Photon 2.0 provides a real phone number carrying the same room conversation. *[claimed]*
- Stale-command safety — Commands are versioned against the lease, absolute not toggles, and timeouts reported unknown, never retried elsewhere. *[claimed]*
- Host story screen — Shows who is present, devices online and a plain-language event history, no IDs or tokens visible. *[shown_working]*
- Self-registering devices — Devices announce capabilities on connect so new ones need no code changes. *[claimed]*

**Flow:** Guest scans the QR card → Guest chats a request such as turn on a light → The Brain checks the lease and routes the command → A device acts and the room replies in one sentence → Guest says leave or the lease expires → Next request is refused and guest is told to rescan

**Prompt:** Photon track: build an agent on Photon 2.0 with a real phone number reachable over iMessage and other channels; voice agents count toward a separate best-voice-agent prize. No detailed rubric published.
**Fit (explicit):** Gives the room agent a real iMessage-reachable phone number via Photon 2.0 so guests can control devices by text with the same room and conversation.  *(targeted: Photon: Track Winner)*
**Sponsor tools:** Photon 2.0 (Real phone number and iMessage delivery to the room agent, core); OpenAI Codex (Agent conversation, signed in locally on host Mac, core)
**AI:** A single OpenAI Codex agent interprets guest requests and issues device actions through the Brain, which enforces leases; no custom models.
**Architecture:** FastAPI/WebSocket Python Brain with in-memory device registry and leases; iPhones as HTTPS web-page devices, Mac as AppleScript device; chat page plus Photon iMessage front ends.
**Novelty:** Treats access as an expiring lease rather than an account, with careful handling of in-flight commands and honest tracking of message acceptance versus delivery.
**Scope:** small · working: Real devices run end to end including full ten-minute expiry; three clean runs reported; demo video linked; notes logs in repo. · polish: 100 files, about 3.5k LOC, ARCHITECTURE doc, timestamped run notes and demo script; one room, in-memory state.
**Claims:** Reset ends all leases and clears devices and logs in about one second | Flashlight turns on within seconds with nothing installed | Three clean end-to-end runs in a row
**Gaps:** video not viewed; Photon track text is a short paraphrase from shared cache; setup instructions not seen in truncated README
Sources: https://devpost.com/software/tenant-lpy96k, https://github.com/owen-tsao/tenant, https://dubhacks-2026.devpost.com/

---

### tensormew
*DubHacks DubHacks '26 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Chef's Kitchen: 1st Place [1st]

**What it is:** An autonomous agent that plays Pokemon Crystal in the PyBoy emulator through the opening of Johto to the first gym badge. Cheap reinforcement-learning policies and scripted macros handle most steps; an LLM is called only when triggers like stuck tiles or hard battles fire.
**Problem / user:** Game-agent builders asking how few steps truly need an LLM; calling a model on every frame is slow and costly and screenshots miss game state.

**Features**
- Three-actor control loop — RL policy walks the overworld, macros handle dialogue and routine battles, an LLM director steps in on triggers. *[shown_working]*
- LLM tool calling with logged reasons — Gemini tools like go_to, use_cut, choose_move each require a one-sentence reason that is logged only. *[shown_working]*
- Two RL policies — Small 17-input NumPy actor-critic and a 13.2M-parameter GRU vision policy trained with PPO on parallel PyBoy workers. *[shown_working]*
- RAM-based state reading — Reads map, flags and badges through pret symbols with a SHA1-pinned ROM. *[shown_working]*
- Type-chart battle selection and party gate — Picks moves by Gen 2 type matchups; blocks the gym until party is level 10+. *[shown_working]*
- Streamlit thought log and live HUD — Shows actor, tool, reason, tokens and estimated dollars per decision. *[shown_working]*
- Checkpoint manifest — Labeled saves let gym attempts resume from Violet City. *[shown_working]*
- Cost comparison of trigger-only vs always-on LLM — Page lists publishing this table as future work. *[planned]*

**Flow:** Run starts in New Bark Town with no badges → RL policy walks Route 29 and Cherrygrove → Macros clear Elm and rival dialogue → Agent reaches Violet City and enters the gym → LLM director and battle module defeat Falkner → Zephyr Badge flag set; decision log viewable in Streamlit

**Prompt:** not public / not found
**Fit (none):** Title tracks have no published description; project is a complete agent that clears a defined game milestone.  *(targeted: Chef's Kitchen title track (1st))*
**Sponsor tools:** Gemini API (LLM director via forced tool calls on game triggers, core)
**AI:** PPO-trained policies (small MLP and ResNet+GRU vision net) do routine movement; Gemini tool calling decides only at event triggers with state text; reward shaping with waypoint and story-flag bonuses.
**Architecture:** Four layers: emulator/RAM parser/collision, RL envs and policies, trigger-based LLM supervisor with tool dispatch, and macros/battle logic; SQLite and JSONL decision logs feed a Streamlit viewer.
**Novelty:** Hybrid RL plus event-triggered LLM design for a long-horizon game, with cost logged per decision; large repo with trained weights and recordings.
**Scope:** large · working: Page reports Zephyr Badge earned; 34 test modules; trained weights in repo. · polish: SPEC docs, HUD, Streamlit viewer, website; no video, 15 gallery items.
**Claims:** Earned first badge (EVENT_BEAT_FALKNER set) | Walking steps cost $0 in LLM spend | 13.2M-parameter vision policy | 34 test modules
**Gaps:** no title-track description; no video
Sources: https://devpost.com/software/tensor-mew, evidence/dubhacks-dubhacks-26-tensormew.json (README), https://dubhacks-2026.devpost.com/

---

### Tool Distill
*DubHacks DubHacks '26 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Cook Smarter: 1st Place [1st]

**What it is:** A Python library (plus CLI and Claude Code plugin) that converts an agent's long trial-and-error tool-call runs into verified reusable "distilled tools", and tracks their health as underlying tools change.
**Problem / user:** Teams running production agents that waste 20-30 tool calls rediscovering a path needing 4, and engineers hand-writing the tool the agent keeps reinventing.

**Features**
- Trace recording — Wraps tool execution to log every base tool call and usage in a SQLite trace. *[shown_working]*
- Distill nudge and proposal — After a successful costly run the agent gets one turn to propose a small Python tool calling base tools in fixed order. *[shown_working]*
- Three-stage verification — Static AST/import allowlist check, replay against recorded responses, and an efficiency threshold against the source run. *[shown_working]*
- Evidence-based lifecycle — Tools move draft, verified, active, suspect, deprecated based on measured outcomes. *[shown_working]*
- Reaction to base tool changes — Schema changes trigger re-verification; recovered tools trigger rebuild into shorter versions. *[shown_working]*
- Claude Code plugin and MCP support — Hooks record calls, an MCP server serves verified tools; base tools may be MCP servers. *[shown_working]*
- Hosted shared team store — Paid-tier registry for team agents. *[planned]*

**Flow:** Wire ToolDistill into an agent loop → Agent solves task while trace records calls → Library nudges for a proposal after an expensive success → Proposal passes static, replay, efficiency checks → Later runs call the single distilled tool → On failure agent falls back and seeds a new version

**Prompt:** not public / not found
**Fit (none):** Title track has no published description; project makes agents cheaper by reusing verified paths.  *(targeted: Cook Smarter title track (1st))*
**AI:** Claude via Anthropic SDK writes tool proposals (structured outputs); the library itself verifies via static analysis, replay and measured call counts rather than trusting model claims.
**Architecture:** Python library with trace recorder, verifier, SQLite WAL store, lifecycle manager, MCP adapter on a background thread, Typer CLI and Claude Code plugin hooks.
**Novelty:** Focus on verification and lifecycle upkeep of generated tools, not just generation; published on PyPI with a plugin marketplace install.
**Scope:** medium · working: PyPI release 0.1.0, 338 tests, four-step demo against real model and Claude Code. · polish: Detailed README with install and SDK snippet, spec-first docs, examples; no video.
**Claims:** 338 tests pass | Invoice demo: 20-30 calls become one distilled call with four inside | Published on PyPI
**Gaps:** no title-track description; no video
Sources: https://devpost.com/software/tool-distill, evidence/dubhacks-dubhacks-26-tool-distill.json (README), https://dubhacks-2026.devpost.com/

---

