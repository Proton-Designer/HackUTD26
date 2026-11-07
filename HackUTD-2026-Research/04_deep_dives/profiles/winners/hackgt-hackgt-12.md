# HackGT — HackGT 12 (25 projects)

### Atlas
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Cedar - Best Use of CedarOS; Ergo - Best Use of Mastra Agent Framework for Productivity

**What it is:** A cross-platform desktop overlay (Electron) that indexes a code repository into a shared 'context memory', visualises it as a 3D call graph with summaries, and lets users pull saved context blocks or prompts into any AI tool via a global shortcut.
**Problem / user:** Engineers and teams hit 'context amnesia' re-explaining codebases to AI tools and during slow onboarding (page cites 6 to 8 months to full productivity).

**Features**
- Repository ingestion and indexing — User enters a repo link or connects a local repo; a Node pipeline analyses the file tree with chunking and parallel processing. *[claimed]*
- 3D codebase visualisation — Three.js call graphs with summaries from function level up to whole repo. *[claimed]*
- Context blocks from many sources — Code, docs and communication from GitHub, Slack, databases and doc apps are synthesised into searchable blocks. *[claimed]*
- Global shortcut overlay — Ctrl/Cmd+/ opens an overlay over any desktop app to search and insert context blocks. *[claimed]*
- Prompt library — Users store and chain setup prompts to feed context into any AI tool. *[claimed]*
- Persistent shareable memory — Memory engine with semantic search and referencing for chats, code reviews and documents. *[claimed]*
- Email/password login — Better Auth with an external Express backend. *[claimed]*

**Flow:** Sign up or log in → Enter a repo link or connect a local repo → Atlas indexes it and shows the visualisation with summaries → Connected sources are synthesised into context blocks → From any app press Ctrl/Cmd+/ to search and insert blocks or prompts

**Prompt:** Cedar track: agentic copilot interfaces built with CedarOS that go beyond a chat box. Ergo track: a productivity agent built with the Mastra framework.
**Fit (implied):** Agent layer is built on Mastra, the Vercel AI SDK and the OpenAI Agents SDK, with CedarOS listed in the stack; the product is a developer-productivity memory tool. Page does not spell out per-prize details.  *(targeted: Cedar - Best Use of CedarOS, Ergo - Best Use of Mastra Agent Framework for Productivity)*
**Sponsor tools:** CedarOS (Agent/copilot UI framework listed in stack, unclear); Mastra (Agent framework for the context agent layer, supporting)
**AI:** Mastra agents with Vercel AI SDK and OpenAI Agents SDK, structured outputs validated with Zod, plus a semantic-search context memory; Gemini and Composio also appear in tags.
**Architecture:** Electron app (React 19, Tailwind, Three.js) with a Node main process for file-tree analysis, context pipeline and overlay; Express backend with Better Auth; AI via Mastra and OpenAI SDKs.
**Novelty:** System-wide desktop overlay and global shortcut rather than a web app, aimed at sharing one code-context memory across humans and many AI tools.
**Scope:** medium · working: Page claims a shippable app with macOS and Windows overlay; no demo, video or repo link on the page. · polish: Detailed stack description and claimed polished UI; nothing independently viewable.
**Claims:** Subsecond search on repos with thousands of files and millions of lines (no methodology) | Shippable cross-platform macOS and Windows overlay | Cuts context-switching and onboarding cost
**Gaps:** No GitHub repo linked; No video or demo link; Which integrations (Slack, databases) actually work is unverified; Cedar and Mastra prize text only from hackathon page summary
Sources: https://devpost.com/software/atlas-tlfpkz, prompts_cache/hackgt-12.md

---

### BikeBuddy
*HackGT HackGT 12 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** The Gadget Gallery - 1st Place [1st]

**What it is:** A bike safety kit: a handlebar controller with turn-signal switches, a rear box with an LCD showing turn, hazard and brake states plus a camera, and a React Native app that streams the rear view and auto-triggers brake lights from phone sensors.
**Problem / user:** Georgia Tech campus cyclists who feel unsafe in mixed traffic and find one-handed hand signals unclear.

**Features**
- Handlebar turn-signal controller — ESP32 controller sends HTTP requests to the main unit when a signal is toggled. *[shown_working]*
- Rear signal and brake display — TFT/LCD on rear box shows turn, hazard and brake states. *[shown_working]*
- Rear-view camera feed — Camera on the main unit streams MJPEG to the app via WebView. *[shown_working]*
- Auto brake light — App fuses phone accelerometer, gyro, magnetometer and GPS to detect slowing and trigger brake display. *[claimed]*
- Speed and location view — GPS speed plus Apple Maps guidance in the app. *[claimed]*

**Flow:** Mount rear box, controller and phone on bike → Toggle a turn signal on handlebar → Rear display shows signal → App shows camera, speed and location → Slowing triggers brake light

**Prompt:** Prize page for The Gadget Gallery lists only its prizes (3D printer, monitor); no description text found.
**Fit (implied):** A physical hardware build with custom electronics, firmware and enclosure, matching a gadget-themed track by name only.  *(targeted: The Gadget Gallery)*
**AI:** none
**Architecture:** Main ESP32 acts as WiFi access point and web server, driving the display and camera; handlebar ESP32 sends HTTP commands; Expo app connects to the AP for video and sends brake state.
**Novelty:** Full hardware stack with custom enclosure and sensor-fusion brake detection; also helmet-related firmware folders in repo.
**Scope:** medium · working: Demo video and photos of equipped bike; repo has app, firmware and controller code; ran continuously after board swap. · polish: Soldered wiring, laser-cut acrylic case, 3D-printed mounts; repo has tests flag but minimal README.
**Claims:** Braking detection described as pretty accurate (no figures)
**Gaps:** track description absent; README is just a title
Sources: https://devpost.com/software/bikebuddy, evidence/hackgt-hackgt-12-bikebuddy.json, https://hackgt-12.devpost.com/

---

### Caladrius
*HackGT HackGT 12 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** The Curator's Cause - 2nd Place [2nd]

**What it is:** An ER triage system with a patient-held mobile 'medical passport' shared by a short-lived QR code, then LangGraph agents ask adaptive questions and produce a ranked differential diagnosis feeding a nurse priority queue.
**Problem / user:** Triage nurses and EMS crews who lack patient history, plus patients who want to own their records; cites about a third of triage decisions being erroneous.

**Features**
- Patient medical passport app — React Native app stores allergies, prescriptions, surgeries and history on the patient's device. *[shown_working]*
- QR consent sharing — Nurse generates QR; patient scans; data lands in a temporary S3 cache keyed by a session ID that rotates every 60 seconds. *[claimed]*
- Adaptive AI questioning — LangGraph question agent picks follow-ups from vitals, history and prior answers. *[shown_working]*
- Differential diagnosis report — Final agent outputs JSON with ranked diagnoses, confidence, urgency and next steps. *[shown_working]*
- Priority queue dashboard — Nurses see ranked patients and reorder them live; data wiped after treatment. *[shown_working]*
- Live consult transcription — Amazon Transcribe Medical in a separate branch. *[planned]*

**Flow:** Patient updates passport → Nurse generates QR, patient scans and consents → AI asks adaptive questions → Differential diagnosis goes to HCP system → Nurse works the priority queue

**Prompt:** Prize page for The Curator's Cause lists only prizes (Quest 3S, Ninja Creami); no description text found.
**Fit (implied):** Healthcare problem with patient data ownership; page does not tie it to track text.  *(targeted: The Curator's Cause)*
**Sponsor tools:** AWS S3 (temporary consent-based passport cache, supporting); Amazon Transcribe Medical (planned consult transcription (branch), unclear)
**AI:** LangGraph with a question agent and Final Diagnosis Agent; page says GPT-5 via OpenAI API used instead of a local model.
**Architecture:** Monorepo: React Native Expo passport app, Next.js plus FastAPI triage client, admin dashboard, patient-doctor module; S3 cache and MongoDB proof of concept.
**Novelty:** Patient-owned records with rotating session identifier; team openly notes planned AES encryption was not implemented.
**Scope:** large · working: README embeds end-to-end video demo; repo with four apps and ~10k LOC. · polish: Structured README with file map; no tests.
**Claims:** A third of triage decisions are erroneous (cited) | Described as HIPAA compliant though encryption not built
**Gaps:** track description absent
Sources: https://devpost.com/software/caladrius, evidence/hackgt-hackgt-12-caladrius.json, https://hackgt-12.devpost.com/

---

### CanDraw
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Ergo - Best Use of Mastra Agent Framework for Productivity

**What it is:** An AI diagramming copilot on an Excalidraw canvas: describe tables and relationships in plain English (or by voice) and it draws them, then exports the diagram as SQL CREATE TABLE statements. Devpost frames it as system-design and UML help, but the working demo is database schemas.
**Problem / user:** Engineers who find Figma, Lucidchart and draw.io clunky and their AI features paywalled, and want fast draft diagrams, mainly database schemas.

**Features**
- Text-to-schema diagramming — Prompt describing tables, columns and relations makes the Mastra agent draw tables then relationships onto the canvas. *[shown_working]*
- Diagram-to-SQL export — Canvas rectangles, text and arrows are sent to an LLM that returns structured tables, relationships and SQL. *[shown_working]*
- Arrow snapping to table edges — useEffect layer over Excalidraw elements snaps relationship arrows to table borders. *[shown_working]*
- Voice input (beta) — Spoken commands transcribed and mapped to canvas actions; README notes occasional infinite loops. *[unclear]*
- UML and architecture diagrams — Mentioned in purpose but listed under next steps. *[planned]*
- More SQL dialects and live DB sync — Postgres, MySQL, SQLite export and two-way sync with databases listed as next steps. *[planned]*

**Flow:** Open landing page and type a prompt describing the system → Agent generates tables, then relationships, on the canvas → Review or edit the diagram → Choose the diagram-to-SQL option → Export the generated SQL schema

**Prompt:** Ergo track: build a productivity agent using the Mastra agent framework.
**Fit (explicit):** Mastra runs the backend agent workflows and all OpenAI calls, with Cedar-OS on the frontend letting the model draw directly on the canvas; the tool speeds up engineering design work.  *(targeted: Ergo - Best Use of Mastra Agent Framework for Productivity)*
**Sponsor tools:** Mastra (Backend agent orchestration, tools and OpenAI communication, core); Cedar-OS (Chat/voice UI and agent-to-canvas bridge, core)
**AI:** OpenAI model through Mastra agents; an export tool prompts the LLM to parse filtered Excalidraw elements into a structured tables/relationships/SQL object instead of parsing geometry.
**Architecture:** Next.js frontend with Excalidraw canvas and Cedar-OS chat on port 3000, Mastra backend on 4111 in one TypeScript monorepo, started from the Cedar-OS and Mastra starter template.
**Novelty:** Uses an LLM to read drawn shapes back into SQL rather than only generating drawings; custom arrow-edge snapping on top of Excalidraw.
**Scope:** small · working: README and Devpost screenshots show landing, generation and SQL export; voice flagged as flaky; no live link. · polish: Honest README with usage; no tests, no video; built on a starter template.
**Claims:** Built in 36 hours | Schema diagrams generated in seconds from a few words
**Gaps:** No demo video; README (later, personal-portfolio text) says whiteboard is for DB schemas; Devpost pitches UML/system design too, feature list follows the README for what works
Sources: https://devpost.com/software/s-hrncfi, evidence/hackgt-hackgt-12-candraw.json, prompts_cache/hackgt-12.md

---

### CommitSense
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** MLH - Best Domain Name from GoDaddy Registry

**What it is:** A developer tool that stores a company's code, commit history and tickets in Snowflake and uses retrieval-augmented generation with Gemini to explain a highlighted legacy snippet as one narrative covering what it does, who changed it, when and why.
**Problem / user:** Developers and new hires in legacy codebases who lose weeks decoding undocumented fixes and cryptic comments by digging through old commits and tickets.

**Features**
- Highlight-to-explain — User selects a code snippet and gets a narrative of function, authorship, timing and reasoning. *[shown_working]*
- Commit and ticket history per snippet — Commit messages, ticket histories and developer comments pulled together for the selected lines. *[claimed]*
- Snowflake-backed project store — Codebases, commits and tickets stored in Snowflake with tuned schemas and queries; Cortex listed in tags. *[claimed]*
- RAG with Gemini — Retrieval supplies context per query; Gemini writes line-by-line explanations combining function, history and intent. *[claimed]*
- Developer login — Login screen shown in screenshots; repo includes a Supabase folder. *[unclear]*
- Live commit insights and analytics — Real-time version-control integration and code-quality analytics listed as next steps. *[planned]*

**Flow:** Developer logs in → Opens the code explanation view → Highlights a snippet → Receives a narrative with function, history, authorship and rationale

**Prompt:** not public / not found
**Fit (none):** Prize is for registering a domain through GoDaddy Registry; the Devpost page and repo do not mention a domain, so the link to the prize is not stated. Project is otherwise built on Snowflake Cortex and Gemini.  *(targeted: MLH - Best Domain Name from GoDaddy Registry)*
**Sponsor tools:** Snowflake Cortex (Storage and retrieval layer for code, commits and tickets, supporting); Gemini API (Generating narrative explanations, core)
**AI:** RAG: Snowflake-stored code, commits and tickets retrieved per query, then Gemini writes the narrative explanation; prompt engineering and context weighting tuned for messy legacy repos.
**Architecture:** React/Vite/shadcn frontend with a Supabase client folder; Snowflake holds codebase, commit and ticket data; retrieval feeds Gemini for explanations.
**Novelty:** Frames code understanding as a history narrative joining commits, tickets and comments rather than summarising code alone.
**Scope:** small · working: Screenshots of login and a code explanation demo; no video or live link. · polish: Repo is a Vite/shadcn UI of about 7.6k LOC with no README or tests.
**Claims:** Faster onboarding for legacy code (unmeasured) | Turns undocumented code into searchable knowledge
**Gaps:** Repo has no README; backend wiring to Snowflake not visible; No video or demo; GoDaddy domain not mentioned anywhere
Sources: https://devpost.com/software/commitsense-da5h6s, evidence/hackgt-hackgt-12-commitsense.json

---

### Dispatch
*HackGT HackGT 12 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Hall of Illusions - 1st Place [1st]

**What it is:** A VR firefighter training game where the player walks or runs in place wearing a chest IMU tracker, which a custom SteamVR driver turns into locomotion in a burning maze with spreading fire, audio cues and rescue objectives.
**Problem / user:** Firefighters, EMTs and rescue teams needing low-cost realistic VR training without treadmills or joysticks.

**Features**
- Walk-in-place locomotion — Wearable ESP-based IMU sends motion wirelessly; a C++ OpenVR driver converts it to speed and direction. *[shown_working]*
- Burning maze with fire spread — Unity scene progresses smoke to flames with falling beams and obstacles. *[shown_working]*
- Audio-guided rescue objectives — Fire grows louder and victims call out; player rescues randomized dummies. *[shown_working]*
- HUD and fail state — Tracks progress, survival time and decisions; screen fades black with breathing audio on failure. *[shown_working]*
- AI performance feedback — LLM review of hesitation and route choices. *[planned]*

**Flow:** Put on VR headset and chest tracker → Walk in place to move through maze → Find and rescue dummies as fire spreads → Escape or collapse to fail screen

**Prompt:** Prize page for Hall of Illusions lists only prizes (Meta Ray-Ban, record player); no description text found.
**Fit (implied):** VR experience with custom locomotion hardware; matches an illusions/VR theme by name only.  *(targeted: Hall of Illusions)*
**Sponsor tools:** SteamVR/OpenVR (custom driver feeding IMU data as locomotion, core)
**AI:** none
**Architecture:** Wearable microcontroller (PlatformIO firmware) streams IMU data wirelessly to a C++ SteamVR driver; Unity C# game consumes locomotion input.
**Novelty:** Builds both custom wearable hardware and a SteamVR driver in a weekend; repo includes Unity project and driver source (very large file count).
**Scope:** large · working: Seven screenshots and pitch deck; no video; repo contains Unity project and driver. · polish: 3D-printed tracker casings; README is title only.
**Gaps:** no demo video; track description absent
Sources: https://devpost.com/software/dispatch-u7fwrv, evidence/hackgt-hackgt-12-dispatch.json, https://hackgt-12.devpost.com/

---

### Doc McQuery
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Impiricus

**What it is:** A clinician web app: pick a hospital and patient, type visit observations, and get summaries of the three most relevant PubMed case studies plus summaries of similar patients' records from the same hospital's (synthetic) EMR database.
**Problem / user:** Busy clinicians who have no time to find and read case studies or consult similar in-house cases when new conditions and treatments keep emerging.

**Features**
- Free-text visit input parsing — OpenAI sorts typed notes into conditions, symptoms, medications, treatments and diagnoses. *[shown_working]*
- EMR history summary — Pulls patient demographics, past conditions, symptoms and observations from PostgreSQL and has OpenAI summarise them. *[shown_working]*
- Tiered PubMed case-study search — LLM builds a query for the NIH API; four tiers progressively drop demographics, treatments, then most symptoms, stopping at three relevant articles; each summarised. *[shown_working]*
- Similar-patient search — Each symptom is embedded with Sentence Transformers and matched against embedded observations in pgvector; candidates re-ranked by demographics. *[shown_working]*
- Hospital login, patient dropdown, search-again — React/Vite front end calling a Flask API with POST for input and GET for results. *[shown_working]*
- Dockerised multi-service setup — Docker container centralises services for portable deployment. *[claimed]*
- RAG, wider sources, hover EMR preview — Listed as next steps along with a Learn More link to originals. *[planned]*

**Flow:** Select hospital and log in → Pick a patient from the list → Enter symptoms, diagnoses and observations from the visit → Wait on a loading page while searches run → See three case-study summaries and similar-patient summaries → Optionally search again

**Prompt:** Impiricus: build technology-enabled healthcare provider engagement tools that deliver the right information at the right time, such as EMR literature discovery or study relevance alerts.
**Fit (implied):** Matches the example of EMR-driven literature discovery: it surfaces relevant PubMed case studies and similar in-hospital cases from a patient's record at point of care. No Impiricus-specific tool is used.  *(targeted: Impiricus)*
**AI:** OpenAI API for input parsing, PubMed query generation and summarisation; Sentence Transformers embeddings in pgvector for symptom-level similar-patient retrieval; tiered keyword relaxation for search.
**Architecture:** React/TypeScript/Vite front end calls a Flask API; backend uses PostgreSQL with pgvector (1,000 Synthea patients), OpenAI and the NIH PubMed API; Docker packaging.
**Novelty:** Combines external literature search with in-hospital similar-patient retrieval; tiered query relaxation and per-symptom embedding were designed to fix empty or homogeneous results.
**Scope:** small · working: Detailed README and Devpost describe the full pipeline; YouTube demo and six screenshots; runs on synthetic data only. · polish: Well-written README, Docker, login and loading screens; no tests or live link.
**Claims:** First time the team used embeddings and API endpoints | Four-tier search stops at three relevant articles
**Gaps:** Video not watched; README setup section truncated in evidence
Sources: https://devpost.com/software/dr-mcquery, evidence/hackgt-hackgt-12-doc-mcquery.json, prompts_cache/hackgt-12.md

---

### Dose
*HackGT HackGT 12 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Best Overall - 1st Place [1st]

**What it is:** A smart pill bottle with a load cell and ESP32 that detects pill removal, plus a Next.js dashboard showing patient profile, dosing windows, adherence percentage, anomalies, pill-count trends and an event log.
**Problem / user:** Clinicians, caregivers and researchers tracking medication adherence; cites 30-50% non-adherence and $100-300B yearly cost.

**Features**
- Load-cell pill detection — HX711-read TAL220 load cell in bottle senses weight changes as pills move. *[claimed]*
- Wi-Fi telemetry — ESP32-C3 firmware sends data to a backend receiver that computes statistics into Supabase. *[claimed]*
- Subject dashboard — Profile card, prescription and dosing windows, adherence stats, anomaly flags. *[shown_working]*
- Pill count charts and event log — Recharts line chart and table with anomaly highlighting, updated live. *[shown_working]*

**Flow:** Patient takes pills from bottle → Sensor data sent to backend → Stats saved to Supabase → Clinician views dashboard

**Prompt:** Best Overall page lists prizes (Disney trip, iPad, PS5); judging criteria point to an external site; no description text.
**Fit (none):** Overall award; combined hardware sensor and dashboard for adherence.  *(targeted: Best Overall)*
**Sponsor tools:** Supabase (real-time database for dashboard, supporting)
**AI:** none
**Architecture:** Bottle load cell to ESP32-C3 over Wi-Fi to a receiver that computes adherence and writes to Supabase; Next.js dashboard reads real-time.
**Novelty:** Hardware plus dashboard for clinical-trial style adherence; CAD enclosure included.
**Scope:** medium · working: Four screenshots; no video; repo has dashboard, firmware and CAD folders. · polish: 3D-printed enclosure; README documents dashboard features; no tests.
**Claims:** Tamper-resistant record of medication use (unverified)
**Gaps:** no video; judging criteria external
Sources: https://devpost.com/software/dose-ebmo9z, evidence/hackgt-hackgt-12-dose.json, https://hackgt-12.devpost.com/

---

### Dotify
*HackGT HackGT 12 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** The Gadget Gallery - 2nd Place [2nd]

**What it is:** A portable device that photographs an object through a web app, gets a short description from Google Gemini, and has an Arduino drive six servos to emboss the text as Braille on paper advanced by a DC motor.
**Problem / user:** Visually impaired people, and shops or households, since everyday packaged goods rarely carry Braille.

**Features**
- Photo to description — Web app captures image; Gemini returns a concise text description. *[claimed]*
- Braille embossing — Arduino UNO R4 converts text to Braille cells and six micro servos press pins to emboss dots. *[claimed]*
- Paper feed — DC motor with driver advances paper between characters on fixed timing. *[claimed]*
- Portable battery enclosure — Four AA batteries in a 3D-printed housing. *[claimed]*

**Flow:** Photograph an object → Gemini describes it → Arduino translates text to Braille → Servos emboss dots and paper advances → Take the tactile label

**Prompt:** Prize page for The Gadget Gallery lists only prizes (3D printer, monitor); no description text found.
**Fit (implied):** Physical accessibility gadget combining web, AI and custom electronics; track link by name only.  *(targeted: The Gadget Gallery)*
**Sponsor tools:** Google Gemini API (image-to-text description, core)
**AI:** Google Gemini API turns the captured image into a short description; no other ML.
**Architecture:** Web app (TypeScript frontend, Python backend) sends Gemini text over serial to Arduino firmware in C++ that actuates servos and a paper-feed motor.
**Novelty:** Closes the loop from camera to physical Braille output on a low-cost mechanism with one embossing cell.
**Scope:** small · working: README and Devpost describe an end-to-end pipeline; no video; repo has src, api and arduino folders. · polish: CAD housing and detailed README; no tests.
**Gaps:** no video; track description absent
Sources: https://devpost.com/software/dotify, evidence/hackgt-hackgt-12-dotify.json, https://hackgt-12.devpost.com/

---

### graphaura
*HackGT HackGT 12 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Crypt of Data - 1st Place [1st]

**What it is:** A web app that ingests photos and documents through the R2R service, extracts people, places and moments into a Neo4j graph, and shows them in an interactive 3D force graph with hybrid search and RAG.
**Problem / user:** Individuals wanting to explore personal memories; the page states no explicit problem, only a tagline about reviving memories.

**Features**
- Document and photo upload — POST endpoint hands files to R2R for chunking, NER and embeddings. *[shown_working]*
- Knowledge graph build — Endpoint creates entities and relationships stored in Neo4j. *[shown_working]*
- 3D graph visualization — Next.js frontend with react-force-graph-3d for exploring entities. *[shown_working]*
- Hybrid search and RAG — Combines R2R vector document search with graph traversal. *[claimed]*
- Health and metrics endpoints — Report service status and vector/graph counts. *[claimed]*

**Flow:** Upload files → R2R extracts entities and embeddings → Build graph → Explore 3D graph or run hybrid search

**Prompt:** Prize page for Crypt of Data lists only prizes (drone, projector); no description text found.
**Fit (implied):** A data and knowledge-graph tool; link to the data-themed track by name only.  *(targeted: Crypt of Data)*
**AI:** R2R handles ingestion, chunking, entity extraction, embeddings and RAG; no specific LLM named.
**Architecture:** Next.js frontend, FastAPI backend, R2R external service, Neo4j graph, Postgres with pgvector, Redis; README has mermaid architecture and data-flow diagrams.
**Novelty:** Graph-RAG over personal multimodal memories with a 3D visualizer; deployed at graphaura.dev.
**Scope:** medium · working: Live domain graphaura.dev, six screenshots, documented API endpoints. · polish: README with mermaid diagrams, Docker present; no tests.
**Gaps:** no video; problem statement and challenges absent
Sources: https://devpost.com/software/graphaura, evidence/hackgt-hackgt-12-graphaura.json, https://hackgt-12.devpost.com/

---

### Grindstone
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** MLH - Best AI Application Built with Cloudflare

**What it is:** A native iOS goal tracker where Mastra agents turn a rough goal into an achievable goal with start and end dates, then a SMART goal with milestones that account for the user's calendar and reminders. Backend runs on Cloudflare Workers with D1.
**Problem / user:** People who find habit trackers shallow and unfun and want real, schedule-aware milestones for personal goals.

**Features**
- Goal refinement agent — Mastra agent converts a rough goal into an achievable goal with specific start and end dates. *[claimed]*
- SMART goal with milestones — Second refinement step produces SMART goals and dated milestones. *[claimed]*
- Schedule-aware planning — Reminders and calendar events synced to the database via EventsKit; a Mastra tool lets the agent fetch them to judge workload. *[claimed]*
- Gamified goal tracking — Described as a goal tracker that gamifies goals, with hand-drawn art in a SwiftUI app. *[claimed]*
- Stats, trackers, joining others — Listed as unbuilt future features. *[planned]*

**Flow:** Open the iOS app and enter a rough goal → Grant calendar and reminders access → Agent proposes an achievable goal with dates → Agent refines it into a SMART goal with milestones → Track the milestones in the app

**Prompt:** not public / not found
**Fit (implied):** Backend deployed on Cloudflare Workers with D1 as its database and AI agents doing the planning. MLH prize text not retrieved, so fit rests on the stated hosting and AI use.  *(targeted: MLH - Best AI Application Built with Cloudflare)*
**Sponsor tools:** Cloudflare Workers (Hosting the Next.js/Mastra backend, core); Cloudflare D1 (Database for synced events and goals, core)
**AI:** Mastra agent pipeline with Gemini and OpenAI models via ai-sdk; an agent tool fetches the user's synced calendar events to ground milestone planning.
**Architecture:** SwiftUI iOS client syncs reminders and calendar to a Next.js and Mastra backend on Cloudflare Workers backed by D1; the app lives in a separate repo.
**Novelty:** Chains two refinement agents (achievable goal then SMART goal) and feeds real calendar load into planning.
**Scope:** small · working: Devpost links an app repo and a demo video; backend repo is about 12k LOC; no live link. · polish: Native iOS UI with liquid glass and hand-drawn art; backend README is the unmodified create-next-app text.
**Claims:** Built in 24 hours after a late start
**Gaps:** Evidence repo is only the backend; iOS app repo (ScorelineSocial/app) not read; Video not watched; MLH Cloudflare prize text not fetched
Sources: https://devpost.com/software/grindstone, evidence/hackgt-hackgt-12-grindstone.json

---

### Hall of Us
*HackGT HackGT 12 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Hall of Illusions - 2nd Place [2nd]

**What it is:** A web uploader where hackathon photos and videos are AI-tagged and captioned, stored in S3, and shown as spatially anchored exhibits in a Quest 3 mixed-reality museum placed around the venue.
**Problem / user:** Hackathon participants, sponsors and judges whose event photos stay buried on phones.

**Features**
- Photo and video upload — Next.js web app with FastAPI backend and S3 storage by user and tag. *[claimed]*
- AI tagging, captions and enhancement — OpenAI/LangChain pipeline and Cedar integration label and enhance uploads. *[claimed]*
- Mixed-reality museum — Unity MetaXR app on Quest 3 anchors exhibits near booths and tables. *[claimed]*
- Natural-language filtering — Prompts surface specific memories in the museum. *[claimed]*

**Flow:** Upload media on the web → AI tags and enhances it → Exhibit appears at a spatial anchor in Quest 3 → Visitors explore or filter by prompt

**Prompt:** Prize page for Hall of Illusions lists only prizes (Meta Ray-Ban, record player); no description text found.
**Fit (implied):** Mixed-reality museum built around the event theme; page mentions Cedar for AI features.  *(targeted: Hall of Illusions, Cedar: Best Use of CedarOS)*
**Sponsor tools:** CedarOS (AI tagging and editing interface in the web app, supporting); Meta Quest 3 / MetaXR SDK (spatial anchors and museum rendering, core)
**AI:** OpenAI models via a custom LangChain backend generate tags and captions and enhance photos; Cedar surfaces them in the UI.
**Architecture:** Next.js web app and Unity Quest 3 client share FastAPI/Pydantic models; Postgres, S3, deployed on own VPS via Coolify.
**Novelty:** Bridges web upload to anchored mixed-reality exhibits at the actual venue.
**Scope:** medium · working: Single screenshot and a demo domain; no video; repo not cloneable for evidence. · polish: Shared type-safe models across three codebases; repo details unverified.
**Gaps:** repo clone failed so no README or code stats; track description absent; demo domain not opened
Sources: https://devpost.com/software/hall-of-us, https://hackgt-12.devpost.com/

---

### InfraBlocks
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Warp - Best Developer Tool

**What it is:** A drag-and-drop web editor where users assemble cloud services as blocks on a React Flow canvas, ask an AI assistant named Rex to build the diagram from plain English, and generate Terraform that can be deployed with a click.
**Problem / user:** Developers who want to deploy to the cloud without weeks of certification study; the page cites 60-80 hours and hundreds of dollars to learn the basics.

**Features**
- Visual block canvas — Drag service blocks (VMs, databases, functions) from a catalog onto a canvas and connect them, with connection validation and config panels. *[shown_working]*
- Rex AI assistant — OpenAI-based agent via Cedar-OS reads a plain-English request and adds, connects or edits blocks directly in app state. *[shown_working]*
- Terraform generation — Diagram converts to main.tf, variables.tf, outputs.tf and providers.tf, viewable and downloadable. *[shown_working]*
- One-click deploy — Deploy button provisions the stack on the chosen provider using stored credentials, with progress status. *[claimed]*
- Multi-cloud support — README lists AWS, GCP and Azure service sets; Devpost says only one provider so far and others are next. *[unclear]*
- Project workspace — Multi-project dashboard with version history per README. *[claimed]*

**Flow:** Create a project and pick a cloud provider → Drag blocks onto the canvas or describe needs to Rex → Connect and configure resources → Review generated Terraform files → Press Deploy to provision

**Prompt:** not public / not found
**Fit (explicit):** A developer tool for cloud infrastructure; writeup says the team used Warp as its main environment for terminal work, Terraform runs and agentic debugging. Official Warp prize text was not found.  *(targeted: Warp - Best Developer Tool)*
**Sponsor tools:** Warp (Development environment and agentic debugging of Rex, supporting); Cedar-OS (Connects user intent to application state for Rex, core)
**AI:** Rex uses OpenAI models through Cedar-OS with structured reasoning and Zod-validated outputs so generated infrastructure is valid and mutates canvas state in real time.
**Architecture:** Next.js and TypeScript front end with React Flow canvas and Zustand state; OpenAI-backed assistant; Terraform generator and cloud-SDK deploy layer.
**Novelty:** Pairs a block editor with an agent that edits the canvas directly and emits runnable Terraform rather than only suggesting configs.
**Scope:** medium · working: Devpost calls it fully functional with a demo video; README documents deploy flow; no live link. · polish: About 27k LOC, logo, detailed README with service lists; no tests or CI.
**Claims:** Fully functional visual-to-Terraform editor | Complex stack provisioned with a single click
**Gaps:** README (later snapshot) lists AWS, GCP and Azure while Devpost says one provider; feature list follows Devpost for working status; Warp prize text not found
Sources: https://devpost.com/software/infrablocks, evidence/hackgt-hackgt-12-infrablocks.json

---

### Medicus
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Impiricus

**What it is:** A platform where medical-product sales reps upload clinical and safety material and doctors use AI search and a chat copilot to preview relevant products before a visit, with AI-generated, trackable email campaigns to providers.
**Problem / user:** Healthcare providers drowning in irrelevant vendor information, and sales reps who travel to hospitals without knowing whether a visit will be useful.

**Features**
- Product and clinical data upload — Reps add products with trials, prescribing info and safety evidence; README frames these as prescription drugs, Devpost as medical devices. *[claimed]*
- AI search for doctors — README says BioBERT embeddings power search so doctors can preview relevant items before a sales visit. *[claimed]*
- AI email campaign generation — OpenAI drafts personalised campaigns for chosen specialties; React Email templates sent via Gmail. *[claimed]*
- Trackable smart links and analytics — Links to product pages and a dashboard tracking campaign and engagement. *[claimed]*
- Cedar-OS chat for doctors — In-app copilot answers questions on product information and clinical evidence. *[claimed]*
- HCP database — Manage provider contacts and specialties. *[claimed]*
- Cedar-policy access control — Devpost says access to sensitive data is defined with Cedar policies. *[unclear]*

**Flow:** Rep registers a product with supporting clinical documents → Rep generates a personalised email campaign for target specialties → Provider receives email with smart link → Provider previews product info and asks the chat or search → Rep views engagement analytics

**Prompt:** Impiricus: build technology-enabled healthcare provider engagement tools that deliver the right information at the right time, such as literature discovery, relevance alerts or pre-visit questionnaires.
**Fit (explicit):** Writeup states the goal as the right information to the right provider at the right time and says the team looked to Impiricus for guidance on avoiding jargon overload. No sponsor API used.  *(targeted: Impiricus)*
**AI:** OpenAI GPT-4 for campaign generation, Mastra for agent orchestration, BioBERT embeddings for search per README; Perplexity listed in tags without explanation.
**Architecture:** Next.js 15 and React 19 front end with Cedar-OS chat; Mastra backend on port 4111 with LibSQL; a Python service for data processing; React Email and Gmail delivery; Docker.
**Novelty:** Targets the rep side as well as the doctor side of provider engagement, adding email campaigns and analytics to AI search.
**Scope:** medium · working: Video and four screenshots; README gives run steps; no live link. · polish: About 21k LOC, detailed README with workflows; no tests or CI.
**Claims:** Functional prototype in under 36 hours | Could widen access for rural and underfunded hospitals
**Gaps:** Devpost says medical devices, README says prescription drugs; BioBERT and Cedar policies each mentioned in only one source; README Docker claim but no Dockerfile flagged in evidence; Video not watched
Sources: https://devpost.com/software/medicous, evidence/hackgt-hackgt-12-medicus.json, prompts_cache/hackgt-12.md

---

### Ming Management Training, a personalized AI-native L&D coach
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** MLH - Best Use of Gemini API

**What it is:** A multi-agent LLM role-play trainer where engineers moving into management hold a realtime voice conversation with an AI character in hard scenarios (performance review, conflict, layoff), then get an annotated transcript, feedback and new scenarios tailored to their weak spots.
**Problem / user:** Engineers and new managers who lack affordable, effective soft-skills training; generic modules are criticised and hiring outside managers is costly.

**Features**
- Voice role-play with LLM characters — User speaks live with an NPC in scenarios like performance reviews, conflict resolution and layoffs; manager, employee and coach roles are separate agents. *[shown_working]*
- Live sentiment analysis — Sentiment signals shown on the conversation screen during the call, via Gemini and Google NLP. *[shown_working]*
- Scenario overview on main screen — Detailed briefing of the situation shown next to the conversation. *[shown_working]*
- Analysis page with annotated transcript — After the call: transcript with annotations, summary, and actionable feedback. *[shown_working]*
- Voice follow-up chat on feedback — User can ask spoken questions about the analysis for more detail. *[shown_working]*
- Adaptive scenarios — New scenarios generated from the user's strengths and weaknesses inferred from earlier conversations. *[claimed]*
- Multi-person scenarios, AR/VR, mobile — Two-coworker conflicts, immersive AR/VR and mobile support listed as next steps. *[planned]*

**Flow:** Land on the home page and pick a scenario → Read the scenario overview → Hold a realtime voice conversation while sentiment is displayed → Open the analysis page for transcript, summary and feedback → Ask follow-up questions by voice → Receive tailored new scenarios

**Prompt:** not public / not found
**Fit (explicit):** Gemini models power NPC dialogue, feedback and sentiment analysis in the Mastra multi-agent pipeline; README itself advertises the Gemini prize. MLH prize text itself was not fetched.  *(targeted: MLH - Best Use of Gemini API)*
**Sponsor tools:** Gemini API (NPC conversation, feedback generation and sentiment analysis, core); Cloudflare Workers (Production deployment via Wrangler on a custom domain, supporting); Mastra (Multi-agent orchestration backend, core); CedarOS (Connects frontend to multi-agent runtime, supporting)
**AI:** Mastra multi-agent orchestrator with manager, employee and coach agents on Gemini; OpenAI live voice by default (Deepgram optional); parser rewritten repeatedly to cope with variable LLM output.
**Architecture:** Next.js/React front end with CedarOS; separate Mastra backend on port 4111 with a gateway token; Gemini text and analysis, OpenAI or Deepgram voice; deployed to Cloudflare in two servers.
**Novelty:** Treats leadership coaching as simulated multi-role conversations with live sentiment and an adaptive curriculum; live video generation was dropped for cost (about $9 per minute).
**Scope:** large · working: Live Cloudflare site, demo video, and README quickstart; full stack deployed to production. · polish: 358 files with tests, Docker, CI and a docs folder of 84 files; README badges and screenshots.
**Claims:** Deployed full stack to production on Cloudflare | Parser rewritten about six times for variable LLM output | Live video generation cost about $9 per minute
**Gaps:** README is a later maintained version (no login, provider switches, Deepgram option) while Devpost describes the hackathon build; feature list follows the Devpost; Video not watched; MLH Gemini prize text not fetched
Sources: https://devpost.com/software/ming-management-training-a-personalized-ai-native-l-d-coach, evidence/hackgt-hackgt-12-ming-management-training-a-personalized-ai-native-l-d-coach.json

---

### Orion
*HackGT HackGT 12 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Best Emerging - 2nd Place [2nd]

**What it is:** An onboarding assistant that ingests GitHub PRs, Slack threads, PDFs and captured terminal commands into a hybrid dense and sparse index, then answers newcomer questions with cited sources and a reference timeline.
**Problem / user:** New engineers who lose weeks hunting context scattered across Slack, READMEs, CI logs and PRs.

**Features**
- Cited question answering — RAG over dense nomic-embed-text vectors in ChromaDB plus TF-IDF; Gemini answers with source references. *[shown_working]*
- GitHub and Slack ingestion — Python clients poll for new PRs, reviews and messages and re-index incrementally. *[claimed]*
- Terminal command capture — Bash script records key commands as documentation. *[claimed]*
- PDF and doc ingestion — Local documents embedded alongside other sources. *[shown_working]*
- Reference timeline — UI lists exact sources used with timestamps. *[claimed]*

**Flow:** Ingest sources → Ask a question in chat → Hybrid retrieval picks top documents → Answer shown with citations → Reference timeline shows sources

**Prompt:** Best Emerging prize page lists only prizes (headphones, Nespresso); no description text found.
**Fit (none):** General newcomer-category award; developer onboarding RAG tool.  *(targeted: Best Emerging)*
**Sponsor tools:** Gemini API (answer generation (best of Llama3, Gemini, GPT-5 tested), core)
**AI:** RAG with Ollama nomic-embed-text embeddings, TF-IDF sparse index, ChromaDB, Gemini generation; model comparison against Llama3 and GPT-5.
**Architecture:** Flask API with LangChain chunking, GitHub/Slack ingesters, ChromaDB and Postgres/Supabase stores, React chat UI with timeline.
**Novelty:** Builds living documentation from observed terminal workflows, not only static docs.
**Scope:** small · working: YouTube demo linked in README; quickstart scripts; ~2k LOC. · polish: Custom UI and setup scripts; no tests.
**Claims:** Built end-to-end RAG across four sources in 36 hours | Polls GitHub and Slack every second
**Gaps:** Devpost lists no video; README links one; track description absent
Sources: https://devpost.com/software/orion-owa3ry, evidence/hackgt-hackgt-12-orion.json, https://hackgt-12.devpost.com/

---

### RefNet
*HackGT HackGT 12 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Best Overall - 2nd Place [2nd]

**What it is:** Web app for searching academic papers via OpenAlex and exploring their citation links as an interactive D3 graph. A Cedar OS assistant backed by GPT-4o can answer questions about selected papers and directly move, highlight and add nodes. Includes notes and several export formats.
**Problem / user:** Student researchers doing literature reviews who lose time tracing who cited whom and hand-entering citations into reference managers.

**Features**
- OpenAlex paper search — Flask API queries OpenAlex by title, author, keyword; sort/filter by citations, relevance, date; multi-select papers. *[shown_working]*
- Interactive citation graph — D3 force graph; node size = citations, color = year; depth controls expand references and citations; drag/zoom. *[shown_working]*
- Graph-aware AI assistant — Cedar OS overlay sends selected papers and graph state to Mastra/GPT-4o for summaries, comparisons, gap spotting. *[shown_working]*
- AI manipulates the graph — Assistant can highlight nodes, rearrange layout and add papers it finds, not just chat. *[shown_working]*
- Whiteboard notes — Color-coded draggable text boxes on the graph; assistant can read and rephrase them. *[shown_working]*
- Exports — JSON graph state, BibTeX, PNG, MLA citations, and an AI-written review paper PDF. *[shown_working]*
- Import saved graph — Reload a previously exported JSON graph. *[claimed]*

**Flow:** Search for a paper or topic → Pick one or several papers and build the citation graph → Adjust reference/citation depth, select nodes → Ask the Cedar assistant about papers or ask it to rearrange/add nodes → Add notes on the canvas → Export JSON, BibTeX, PNG or review-paper PDF

**Prompt:** Best Overall at HackGT 12 is a prize-only track; the event says build anything, with judging criteria deferred to the organizers' live site. The project also used sponsor tools Cedar OS and Mastra.
**Fit (implied):** No open prompt to answer; project built on the Cedar agentic-copilot framework so the assistant acts on the UI, and Mastra orchestrates the AI backend.  *(targeted: Best Overall - 2nd, (sponsor tools: Cedar OS, Mastra))*
**Sponsor tools:** Cedar OS (floating context-aware assistant that edits the graph, core); Mastra (Node backend orchestrating GPT-4o analysis and review generation, core)
**AI:** GPT-4o via a Mastra Express backend receives selected papers, graph structure and notes as context; used for paper deep dives, comparisons, gap finding, and review-paper generation; Cedar triggers graph actions.
**Architecture:** React + D3 frontend (Vercel) with Cedar overlay; Flask/NetworkX service fetches OpenAlex data; Mastra/Express service calls GPT-4o; Flask and Mastra on AWS EC2.
**Novelty:** The assistant performs direct graph edits (highlight, relayout, add papers) rather than only chatting; combines graph, whiteboard notes and review-paper export in one tool.
**Scope:** medium · working: Live Vercel demo link, three-service stack with Docker compose and start script in repo. · polish: PWA manifest, many export formats, README with setup; no demo video listed.
**Claims:** Handles graphs with thousands of citations | Access to millions of papers via OpenAlex | One-click export compatible with Zotero/BibTeX
**Gaps:** no video; screenshot count not captured
Sources: https://devpost.com/software/refnet-c04g9n, https://github.com/Shreyas765/RefNet, https://hackgt-12.devpost.com/

---

### Sideline
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** PrizePicks - The Second Screen Experience

**What it is:** A React Native second-screen app for live NFL games: sponsor-backed community micro-bets generated by AI during play, private team rooms with leaderboards and coins, and a chatbot that explains the game to beginners.
**Problem / user:** Sports fans, especially friend groups and beginners, who find watching games passive and want to engage with each play together.

**Features**
- Live game room with microbets — Game events from a WebSocket wrapper over the NFL Sportradar API (simulated live) trigger pop-up microbets on every play. *[claimed]*
- Sponsor-backed community microbets — More accurate community votes generate larger donations from sponsors to people in need. *[claimed]*
- AI-generated bet prompts — GPT retrieval models write engaging microbet questions from game state. *[claimed]*
- Private teams and custom bets — Friends join teams, pick a live game, and create their own bets in a team betting interface. *[claimed]*
- Leaderboards, coins, profiles, awards — Coins tracked per user, team and group leaderboards, redeemable awards, backed by Firebase. *[claimed]*
- Beginner AI chatbot — OpenAI API chatbot explains plays and rules to new fans. *[claimed]*

**Flow:** Open profile and see teams → Select a live game within a team → Enter the live game room → Get a pop-up when a microbet is posted and place a bet or vote → Create or join custom bets in the team → Check the team leaderboard and redeem awards

**Prompt:** not public / not found
**Fit (implied):** Built as a second-screen companion to live football with in-game micro-bets, social teams and an explainer chatbot; Devpost does not quote the prize text, and the prize wording was not found.  *(targeted: PrizePicks - The Second Screen Experience)*
**Sponsor tools:** Sportradar NFL API (Live game event feed wrapped in a WebSocket server, core)
**AI:** OpenAI/GPT retrieval generates microbet prompts from live events; OpenAI API chatbot answers beginner questions.
**Architecture:** React Native/Expo client; Node/Express with ws WebSocket server wrapping Sportradar events; Firebase auth, Firestore and real-time sync for leaderboards.
**Novelty:** Ties betting-style engagement to charity: proceeds from sponsor donations scale with community accuracy, pitched as a non-profit ad model.
**Scope:** small · working: Screenshots of profile, teams, game room, pop-ups and leaderboards; no video, repo or live link. · polish: UI with animations and gradients per the page; nothing else verifiable.
**Claims:** Combines live sports data, AI bets and social features without clutter | Donations rise with community accuracy
**Gaps:** No repo (only the hackathon org page linked); No video or demo; Live data was simulated; PrizePicks prize text not found
Sources: https://devpost.com/software/sideline

---

### The Kick is Good
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** PrizePicks - Signal from the Noise

**What it is:** A semi-automatic computer-vision pipeline in Python and OpenCV that measures how far a field-goal kick travelled from broadcast video: the user calibrates the field and marks the ball on a few frames, and the program tracks it and fits a 3D ballistic path. A React prototype adds a guess-the-distance game.
**Problem / user:** Football fans who cannot tell from TV how far a kick was really good from; motivating case was a game-ending 55-yard field goal.

**Features**
- Field calibration — User clicks yard-line intersections and enters their distances; program computes homography and camera calibration. *[shown_working]*
- Interactive ball annotation — User steps through frames and clicks the ball at key points; the rest are interpolated. *[shown_working]*
- Automated tracking — HSV color detection refines clicks, CSRT tracker fills gaps, Kalman filter smooths, camera-motion compensation uses field features. *[shown_working]*
- 3D ballistic fit — Physics-based model fit constrained to start at ground height, giving yard coordinates and where the ball crosses 3.33 yards height. *[shown_working]*
- Annotated output video — Boxes, trajectory line, live 3D coordinates, height-vs-distance graph and crossing marker. *[shown_working]*
- Guessing game front end — React prototype where fans guess kick distance; backend data not yet connected, so the 1 to 3 yard result is an estimate. *[claimed]*

**Flow:** Calibrate field by clicking yard-line points → Annotate the ball on selected frames → Run tracking and 3D analysis → View the output video with graph and crossing point → Send final distance to the guessing game

**Prompt:** not public / not found
**Fit (explicit):** Extracts a new sports statistic (kick distance and height crossing) from raw game video and pitches a fan guessing game for PrizePicks; the prize text itself was not found.  *(targeted: PrizePicks - Signal from the Noise)*
**AI:** Classical computer vision, not a trained model: HSV segmentation, CSRT tracking, Kalman filtering, homography and a physics ballistic fit.
**Architecture:** Python OpenCV, NumPy, SciPy and Matplotlib pipeline producing an annotated video; separate React (and mobile) front end for the guessing game, not yet wired to backend output.
**Novelty:** Brings 3D ball-flight reconstruction from single-camera broadcast footage to college football, where no RFID ball tracking data exists; team pivoted from full automation to assisted tracking.
**Scope:** small · working: README documents the CLI phases, past outputs folder and demo video; no accuracy metrics; front end not connected. · polish: README is clear with CLI options and keyboard controls; no tests; about 3.6k LOC.
**Claims:** Kick estimated good from 1 to 3 yards beyond the shown point | Novel versus NFL RFID tracking since college has no public equivalent
**Gaps:** Video not watched; No accuracy or error metrics; PrizePicks prize text not found
Sources: https://devpost.com/software/the-kick-is-good, evidence/hackgt-hackgt-12-the-kick-is-good.json

---

### Tradegist
*HackGT HackGT 12 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Crypt of Data - 2nd Place [2nd]

**What it is:** Solo-built platform where a trader uploads a CSV of trade history and gets behavioral-bias analysis (revenge trading, overtrading, loss spirals) plus a chat-style AI coach and downloadable PDF report. Uses layered detection from rules to a small ML model to an LLM.
**Problem / user:** Retail traders who know their strategy but fall into emotional traps; most tools predict markets or log P&L rather than explain behavior.

**Features**
- CSV ingestion — Normalizes and dedupes uploaded trades, rebuilds round trips, stores in Supabase/Postgres. *[shown_working]*
- Heuristic bias flags — Rule engine tags too many trades per day, rapid re-entry after loss, averaging down, revenge trades. *[shown_working]*
- Logistic-regression scoring — Scores overtrading and loss-chasing tendencies from frequency, size escalation, recovery attempts. *[shown_working]*
- LLM sequence classifier — Small LLaMA-style model reads trade sequences to spot loss spirals and tilt escalation. *[claimed]*
- AI behavior coach — RAG-style chat over the user's trades and scores; README says GPT-3.5 and quick-request buttons, voice via Cedar. *[shown_working]*
- Analytics dashboard — Eight-axis behavioral radar, win rate/P&L, top tickers, best/worst trades, recent trades with mood tags. *[shown_working]*
- PDF behavioral report — ReportLab generates a downloadable report. *[shown_working]*

**Flow:** Upload trade-history CSV → Backend cleans data and tags behaviors → View dashboard and behavior radar → Select trades and ask the coach for analysis → Download PDF report

**Prompt:** Crypt of Data is a prize-only HackGT 12 themed track with no published description; the event brief was simply to build anything.
**Fit (implied):** Data-analysis project that mines raw trade data for hidden behavioral patterns; link to the track theme is inferred from the name only.  *(targeted: Crypt of Data - 2nd)*
**Sponsor tools:** Cedar OS (coach chat UI with voice input, supporting)
**AI:** Three layers: heuristics, logistic regression, and an LLM sequence classifier; coach uses OpenAI/Claude with retrieval over the user's trades and scores (README states GPT-3.5-turbo).
**Architecture:** React/TypeScript + Recharts frontend with Cedar; FastAPI backend with pandas feature engineering, ML scoring and LLM calls; Supabase Postgres store; ReportLab PDFs.
**Novelty:** Targets trader psychology instead of price prediction and stacks rule-based, statistical and LLM detectors; solo build.
**Scope:** medium · working: Repo with ~7k LOC, dashboard and ingestion described; video exists but is silent; no live link. · polish: README admits being AI-written; no tests; no reported accuracy validation.
**Claims:** Detects revenge trading and tilt (self-reported, no accuracy figures)
**Gaps:** video has no audio and was not viewable; README and Devpost differ on which LLMs are used
Sources: https://devpost.com/software/tradegist, https://github.com/SohamAg/tradegist-ai, https://hackgt-12.devpost.com/

---

### Vertex A11y
*HackGT HackGT 12 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Best Emerging - 1st Place [1st]

**What it is:** Manifest V3 Chrome extension that scans the current page for accessibility problems against WCAG 2.1, highlights offending elements on the page, scores compliance, and asks OpenAI for plain-language explanations and fix suggestions. Can export a PDF report.
**Problem / user:** Web developers who treat accessibility as an afterthought; cites that over 96% of top sites fail WCAG/ADA checks.

**Features**
- Page scanner — Custom checks for alt text, color contrast ratios, keyboard access, form labels, landmarks/headings, video captions, zoom-blocking viewport. *[shown_working]*
- On-page highlighting — 'Reveal on page' marks the offending element in the live DOM. *[shown_working]*
- Compliance score — Percent score and A/AA/AAA/Needs Work tier from passed vs total checks. *[shown_working]*
- Filtering — Filter issues by scope (all vs fixable), type and severity. *[shown_working]*
- AI explanations and fixes — OpenAI call returns contextual explanation and code-level fix for an issue. *[shown_working]*
- PDF export — Generates an accessibility report. *[claimed]*

**Flow:** Open extension on a page and run scan → See issue counts, score and tier → Filter by type or severity → Click an issue to reveal it on the page → Request AI explanation and fix → Export PDF

**Prompt:** Best Emerging is a prize-only HackGT 12 track with no published description; the brief was open ('build anything').
**Fit (none):** No stated link to the track; README labels it the Emerging Track winner.  *(targeted: Best Emerging - 1st)*
**AI:** OpenAI GPT (README says GPT-4) given the detected issue context to generate explanations and code fixes; detection itself is deterministic custom code.
**Architecture:** Vanilla-JS content script walks DOM and computes luminance contrast; popup UI with Motion animations; message passing to background that calls OpenAI; bundled with ESBuild.
**Novelty:** Standard accessibility-audit idea (similar to axe/Lighthouse) with in-page reveal and LLM fix explanations; hand-rolled scanner rather than an existing engine.
**Scope:** small · working: Extension repo with built dist, demo video and screenshots of highlight and AI features. · polish: Animated dark UI; no tests; little documentation beyond README.
**Claims:** Checks against WCAG 2.1 and ADA | 96% of top million sites noncompliant (cited WebAIM figure, not own result)
**Gaps:** PDF export only listed in flow
Sources: https://devpost.com/software/vertex-a11y, https://github.com/karandeol-26/vertex_A11y, https://hackgt-12.devpost.com/

---

### vibesB2B
*HackGT HackGT 12 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Winner Best Overall - 3rd Place [3rd]

**What it is:** Electron desktop app that records meetings, then aligns the transcript with per-frame audience emotion analysis to build a timeline and generate coaching notes. A Mastra agent sends the feedback to Slack, Google Docs and Attio CRM. Analysis runs after the meeting, not live.
**Problem / user:** Presenters and pitchers who leave meetings unsure how the audience reacted or where people got confused.

**Features**
- Automatic meeting capture — Electron app with Recall.ai desktop SDK detects and records meetings. *[shown_working]*
- Word-level transcription — AssemblyAI returns timestamped transcript. *[shown_working]*
- Facial emotion analysis — MediaPipe Face Mesh landmarks plus ResNet50-LSTM emotion model; custom brow-furrow metric approximates confusion. *[shown_working]*
- Transcript-emotion timeline — Merges transcript and emotion outputs by timestamp, with emotion peak detection. *[shown_working]*
- Gemini coaching notes — LLM writes supportive feedback on engaging moments, confusion spots, next-time suggestions. *[shown_working]*
- Workflow delivery — Mastra agent posts feedback to Slack, Docs and Attio. *[claimed]*

**Flow:** Launch desktop app and join a meeting → App detects and records it → After the meeting transcript and video are processed → Timeline of speech vs audience reaction is built → Coaching notes generated → Results routed to Slack, Docs and Attio

**Prompt:** Best Overall (3rd) is prize-only. The project also used sponsor tools: Ergo's Mastra productivity-agent prize asks for a productivity agent built on Mastra; Attio integration is also used.
**Fit (implied):** Productivity agent that coaches presenters and pushes results into workplace tools via Mastra; prize targeting not stated.  *(targeted: Best Overall - 3rd, (Mastra for Productivity track likely))*
**Sponsor tools:** Mastra (orchestrating the pipeline and delivery agent, core); Attio (CRM destination for feedback, supporting); Recall.ai (meeting recording SDK, supporting)
**AI:** Computer vision (MediaPipe landmarks, ResNet50+LSTM trained on AffectNet/Aff-Wild2), AssemblyAI speech-to-text, and Gemini for coaching text; Mastra orchestrates.
**Architecture:** Electron/Recall capture -> Flask+SQLite backend (WebSocket, ngrok) -> AssemblyAI + OpenCV/MediaPipe emotion pipeline -> timestamp merge -> Gemini -> Mastra to Slack/Docs/Attio.
**Novelty:** Combines custom confusion detection from face geometry with transcript alignment; pivoted from live to post-meeting after live video dropped to about 2 fps.
**Scope:** medium · working: Devpost links a live site and demo video; repo could not be cloned for inspection. · polish: Multi-service integration; no accuracy metrics reported.
**Claims:** Processes a 30-60 minute meeting in a few minutes
**Gaps:** repo clone failed, no README read
Sources: https://devpost.com/software/vibesb2b, https://hackgt-12.devpost.com/

---

### VisionNav
*HackGT HackGT 12 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** The Curator's Cause - 1st Place [1st]

**What it is:** iPhone app that streams camera and LiDAR data to a Python backend, then guides blind or low-vision users with spatial audio in AirPods: steering around obstacles, finding named objects and guiding the hand to them, plus a Gemini voice assistant.
**Problem / user:** Visually impaired people wanting affordable mobility and independence; cites 7.3 million visually impaired US adults.

**Features**
- Obstacle avoidance audio — Depth frame split into five columns to pick clearest heading; left/right AirPod cues, ticking tempo rises near obstacles, tone for imminent collision. *[shown_working]*
- Hand guidance to objects — User names an item, YOLO finds it, user raises hand (MediaPipe) and pitch/ticking guides reach. *[shown_working]*
- Gemini AI mode — Gemini interprets voice commands, describes surroundings, reads text, and switches modes. *[shown_working]*
- Voice commands — Speech-to-text and text-to-speech for hands-free control. *[shown_working]*
- Live visualization — Camera and depth shown in the app; claims over 20 fps. *[shown_working]*

**Flow:** Wear AirPods and hold iPhone → Say or pick a mode → Obstacle mode: walk with left/right and ticking audio cues → Hand mode: name an object, raise hand, follow pitch to the item → AI mode: ask Gemini to describe or read

**Prompt:** The Curator's Cause is a prize-only HackGT 12 themed track with no published description.
**Fit (implied):** Accessibility tool for visually impaired users; connection to the track theme is inferred only.  *(targeted: The Curator's Cause - 1st)*
**AI:** Ultralytics YOLO on Apple MPS for object detection, MediaPipe for hand tracking, LiDAR depth for headings, Gemini for command understanding and general assistance.
**Architecture:** Swift iOS app captures camera + LiDAR and serves MJPEG video and WebSocket depth packets; Python service runs YOLO/MediaPipe, speech, Gemini and a spatial-audio engine feeding AirPods.
**Novelty:** Custom audio language (panning, tempo, pitch) for both walking and reaching; uses phone LiDAR rather than a cane or glasses hardware.
**Scope:** medium · working: Devpost screenshots show detection and audio alerts; repo ~3.5k LOC across iOS, vision and audio modules. · polish: Project website; no tests; demo video not linked.
**Claims:** Processes video and depth at over 20 fps | Near real-time video with negligible lag
**Gaps:** demo video not linked
Sources: https://devpost.com/software/vision-app, https://github.com/jaeheonshim/VisionNav, https://hackgt-12.devpost.com/

---

### Vital
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Impiricus

**What it is:** A clinician dashboard built on Cedar-OS with a real-time research stream fed by Impiricus data that matches new guidelines to the provider's own patients, shown as draggable patient cards on a canvas that an AI helper can sort and annotate.
**Problem / user:** Physicians swamped by new literature, drug approvals and policy updates who need to know which of their patients a change affects.

**Features**
- Real-time research stream — Impiricus data feed plus OpenAI extraction of criteria from new guidelines and policy updates. *[claimed]*
- Impacted-patient matching — Dashboard highlights patients in the provider's panel affected by an update; match can generate a treatment plan per screenshots. *[claimed]*
- Drag-and-drop patient canvas — Patient cards move freely, can be grouped with notes, and viewed zoomed out. *[claimed]*
- Promptable AI helper — Agent sorts patient cards into separate groups from a natural-language prompt. *[claimed]*
- Cedar-OS spells and radial wheel — Right-click context actions trigger matching patients or generating explainers. *[claimed]*
- AI explainers and patient-education drafts — Quick summaries of a guideline and drafted patient material. *[claimed]*

**Flow:** Open the dashboard and see the research stream → Prompt the AI helper to organise patient cards → Zoom out over the patient canvas → Right-click or use the radial wheel to match patients to a guideline → Generate a treatment plan or explainer → Group patients and add notes

**Prompt:** Impiricus: build technology-enabled healthcare provider engagement tools that deliver the right information at the right time, such as EMR literature discovery, study relevance alerts and pre-visit questionnaires.
**Fit (explicit):** Integrates the sponsor's data feed into a guideline-alert stream that maps new evidence to a clinician's patients, a study-relevance alert use case.  *(targeted: Impiricus)*
**Sponsor tools:** Impiricus data feed (Source of guideline and policy updates for the research stream, core); Cedar-OS (Agentic UI: spells, radial wheel, AI helper, core)
**AI:** OpenAI extracts matching criteria from new literature and powers the card-sorting helper and explainers inside Cedar-OS; patient data kept in Supabase.
**Architecture:** Next.js/React/Tailwind/shadcn front end generated with v0, Cedar-OS agent layer, Supabase database, OpenAI calls, dnd-kit drag-and-drop.
**Novelty:** Spatial canvas of patient cards plus context-menu AI actions instead of a chat or form flow.
**Scope:** medium · working: Page claims a working demo in under 36 hours with screenshot captions; no video or live link. · polish: About 10k LOC across 90 files with many UI components; no README or tests.
**Claims:** Working demo built in under 36 hours | Goal of an LLM for evidence-based care
**Gaps:** Repo has no README; 'Live patient data' source unclear (likely synthetic); No video
Sources: https://devpost.com/software/vital-1qsh6u, evidence/hackgt-hackgt-12-vital.json, prompts_cache/hackgt-12.md

---

### Waste2Taste
*HackGT HackGT 12 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** MLH - Best Use of Snowflake API

**What it is:** A system that photographs leftover plates on a dining-hall dish-return conveyor, estimates the grams of each uneaten food with vision models, stores them in Supabase and Snowflake, and shows chefs ranked waste plus AI recipe alternatives for disliked dishes.
**Problem / user:** Dining-hall chefs who need to know which dishes students leave uneaten so menus match what students enjoy, reducing food waste.

**Features**
- Camera plate capture — Camera over the dish return, connected to Raspberry Pis, captures leftover plates. *[claimed]*
- Leftover mass estimation — OWL-ViT and GroundingDINO detect items, segmentation masks leftovers, Depth-Anything V2 gives height, plate size gives scale, and preset densities convert volume to grams. *[claimed]*
- Waste dashboard — React app with Today page, ranked dish list and Analytics (trends, frequency, reduction metrics). *[shown_working]*
- Ranking by waste — Dishes ordered most to least wasted as a proxy for student preference. *[shown_working]*
- AI recipe alternatives — Snowflake Cortex (Mixtral-8x7b) proposes similar-ingredient recipes with prep time and ingredient lists for unpopular dishes. *[shown_working]*
- Supabase to Snowflake ingestion — Flask API stores measurements in Supabase, ingests them into Snowflake and serves analytics endpoints. *[shown_working]*
- Trained food classifier and multi-angle depth — Nutrition5k-trained models and depth sensors listed as next steps. *[planned]*

**Flow:** Plate passes under the dish-return camera → Pipeline names the food and estimates leftover grams → Data lands in Supabase then Snowflake → Chef opens Today page to see tracked dishes and the most-disliked item → Recommendations page lists ranked dishes and recipe alternatives → Analytics page shows trends over time

**Prompt:** not public / not found
**Fit (explicit):** Snowflake is the processing and analytics store, and Snowflake Cortex generates the recipe recommendations; API README also carries a badge for this prize. MLH prize text not fetched.  *(targeted: MLH - Best Use of Snowflake API)*
**Sponsor tools:** Snowflake (Warehouse, ingestion from Supabase and analytics, core); Snowflake Cortex (Mixtral-based recipe recommendations, core)
**AI:** Open-vocabulary detection (OWL-ViT, GroundingDINO), segmentation, Depth-Anything V2 depth, geometry-based mass estimates; Snowflake Cortex LLM writes recipe swaps.
**Architecture:** Camera and Raspberry Pis feed a Python vision pipeline; Flask API (separate repo) writes to Supabase, ingests to Snowflake with Pandas analysis and Cortex; React/Vite dashboard (separate repo) reads recommendations and analytics.
**Novelty:** Uses a hardware camera plus monocular depth to estimate leftover weight per item, and closes the loop to menu recommendations.
**Scope:** medium · working: Three repos, API README with endpoints and demo video badge, dashboard screenshots; no accuracy figures reported. · polish: API README is polished with logo and screenshot; the Devpost-linked evidence repo itself is a stub with a 72-line script.
**Claims:** Working pipeline from image capture to dashboard insights | Real-time grams of waste per item
**Gaps:** Devpost lists no video but the API README links one; not watched; UI repo not read; Primary repo is a near-empty demo stub; repo_signals reflect it; No accuracy metrics for detection or weight
Sources: https://devpost.com/software/waste2taste-etwp34, evidence/hackgt-hackgt-12-waste2taste.json, https://raw.githubusercontent.com/NavadeepBudda/waste2taste-api/HEAD/README.md

---

