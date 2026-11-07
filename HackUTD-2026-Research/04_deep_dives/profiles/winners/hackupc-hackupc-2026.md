# HackUPC — HackUPC 2026 (21 projects)

### ARC React
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Jetbrains] 1st place [1st]

**What it is:** An iPhone augmented-reality IDE that places code editor, preview, terminal and database-graph panels as floating 3D windows on a desk, controlled by hand gestures and voice, with sync to MongoDB, GitHub and a JetBrains IDE plugin.
**Problem / user:** Developers and vibe coders who want to write or review code on a phone, where small screens limit how much code is visible.

**Features**
- AR floating code panels — ARKit plane detection anchors editor, preview, terminal and MongoDB graph panels rendered as live textures in RealityKit. *[claimed]*
- Hand-gesture control — MediaPipe and Apple Vision track 21 hand joints; a gesture interpreter handles pinch-drag, palm and wave. *[claimed]*
- Voice assistant with spoken replies — On-device speech-to-text feeds a JARVIS persona that answers via ElevenLabs streaming TTS with queued audio. *[claimed]*
- Mobile code editing — Monaco editor in a web view with JetBrains-style toolbar, file tree and Junie chat panel; edit by keyboard, voice or gesture. *[claimed]*
- Sync to MongoDB, GitHub and IntelliJ plugin — FastAPI backend stores code updates; a Kotlin plugin pulls changes; code can be saved to GitHub from the phone. *[claimed]*
- Image and diagram vector store — Images are embedded via OpenAI API and kept in a MongoDB vector database for the plugin to retrieve. *[claimed]*
- AI ghost pair programmer with conversation mode — Backend tests show asking about a file, editing it and asking a follow-up with code-change context, optionally spoken. *[shown_working]*
- Spatial scene backgrounds and multiplayer AR — Scenes replace the background; multiplayer listed as next step. *[unclear]*

**Flow:** Open the iOS app with toolbar, file tree and editor → Edit code by keyboard, voice or chat → Enter AR mode and let it detect a desk → Arrange panels with pinch-and-drag → View terminal output or debug → Stream changes to IntelliJ or save to GitHub

**Prompt:** not public / not found
**Fit (implied):** Mimics JetBrains tooling (toolbar, Junie chat) and ships an IntelliJ IDEA plugin so phone edits reach a JetBrains IDE; JetBrains challenge text not retrieved.  *(targeted: JetBrains 1st place)*
**Sponsor tools:** JetBrains IntelliJ plugin / Junie-styled chat (Kotlin plugin retrieves phone code changes and images; UI imitates JetBrains IDE, supporting); ElevenLabs TTS (Spoken JARVIS replies, supporting); MongoDB Atlas (Code sync and vector store, supporting)
**AI:** OpenAI API embeds images and diagrams for a MongoDB vector store; ElevenLabs gives voice output; backend ghost assistant answers code questions; MediaPipe/Vision do hand tracking.
**Architecture:** SwiftUI/ARKit/RealityKit iOS app with Monaco web view; FastAPI backend on Vercel with MongoDB Atlas; Kotlin IntelliJ plugin reads via backend.
**Novelty:** Puts an IDE into room-scale AR on a phone with hand and voice input and links it to a desktop JetBrains plugin.
**Scope:** large · working: Repo about 21k LOC with iOS app, backend, plugin and tests; backend test scripts for voice and conversation; no demo link. · polish: Two screenshots; README covers only backend setup and tests; no video.
**Claims:** 1st place in the JetBrains track
**Gaps:** JetBrains challenge brief not on public page; README omits AR app; gesture and AR working state taken from Devpost only; Shake gesture purpose not stated
Sources: https://devpost.com/software/arc-react, evidence/hackupc-hackupc-2026-arc-react.json, https://hackupc-2026.devpost.com/

---

### B2Travel
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Skyscanner] 2nd place [2nd]; [MLH] Best Use of ElevenLabs

**What it is:** A Chrome extension saves travel images and quotes into a personal board; CLIP embeddings are projected with UMAP into a 3D WebVR 'Memory Universe' that an ElevenLabs voice agent can navigate by vibe and that links selected photos to Skyscanner flight suggestions.
**Problem / user:** People whose travel inspiration is scattered across camera rolls and browser bookmarks.

**Features**
- Chrome extension saver — Right-click any image or text to send it to the FastAPI backend and MongoDB board. *[claimed]*
- CLIP semantic clustering — CLIP-ViT makes 512-dimensional embeddings so similar scenes group together without tagging. *[claimed]*
- UMAP 3D projection — A /coordinates endpoint reduces all vectors to 3D positions. *[claimed]*
- WebVR memory galaxy — A-Frame scene on phone or headset with gaze interaction, reached through ngrok. *[claimed]*
- Voice agent navigation — ElevenLabs agent hears a vibe, does cosine nearest-neighbour search in CLIP space, emits an event the VR page polls to move the view. *[claimed]*
- Gaze-selected photos to flight recommendations — Chosen images are sent as base64 to the agent, which suggests Skyscanner flights from the user's origin city. *[claimed]*

**Flow:** Right-click and save images or text while browsing → Backend embeds and stores them → Open the VR memory galaxy on phone or headset → Ask the voice agent for a vibe such as a summer beach → View flows to matching items; look at liked photos → Agent gives Skyscanner-based recommendations

**Prompt:** MLH ElevenLabs prize: use ElevenLabs for natural, human-sounding audio such as companions, narration or voice-enabled apps. Skyscanner brief not on the public page.
**Fit (explicit):** README names both awards: ElevenLabs voice agent drives the 3D UI, and Skyscanner API supplies flight options inside the VR booking flow.  *(targeted: Skyscanner 2nd place, MLH Best Use of ElevenLabs)*
**Sponsor tools:** ElevenLabs Conversational AI (Voice agent that drives navigation and recommendations, core); Skyscanner API (Flight recommendations from origin city, core); MongoDB Atlas (Stores images, text and embeddings, supporting)
**AI:** CLIP-ViT embeddings, UMAP reduction and cosine KNN search; ElevenLabs Conversational AI agent turns spoken vibes into coordinates and travel suggestions.
**Architecture:** Chrome extension to FastAPI (PyTorch CLIP, UMAP) with MongoDB; A-Frame frontend polls for events; Python ElevenLabs agent runs locally.
**Novelty:** Treats a saved-image collection as a navigable semantic 3D space controlled by voice, linking it to flight booking.
**Scope:** small · working: About 3.9k LOC across extension, backend, agent and frontend; demo video link in README is a placeholder. · polish: Styled README with architecture and run steps; two screenshots; no tests.
**Claims:** Built in 36 hours | 2nd Skyscanner and MLH Best Use of ElevenLabs
**Gaps:** Skyscanner 2026 challenge brief not found; README video link is a placeholder; Devpost lists none; No challenges or next steps on Devpost
Sources: https://devpost.com/software/b2travel, evidence/hackupc-hackupc-2026-b2travel.json, https://hackupc-2026.devpost.com/

---

### Baymaxxing
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Mecalux] 2nd place [2nd]

**What it is:** A Python heuristic optimizer that fills a warehouse floor with racking bays, respecting columns, uneven ceilings and walls, scored on cost versus capacity. Parallel workers pack from different corners within a 30-second limit; a Streamlit viewer lets users inspect and tweak layouts.
**Problem / user:** Warehouse planners laying out storage bays in irregular spaces for maximum capacity at lowest cost (Mecalux challenge).

**Features**
- Warehouse and catalog ingestion — Reads perimeter, obstacles, ceiling profile and bay catalog; repo includes public test cases. *[shown_working]*
- Active Node Packing heuristic — A priority queue seeded from corners and obstacle edges proposes spots; the most cost-efficient bay is tried first, then a 180-degree flip. *[claimed]*
- Aisle alignment — A rotation is kept if it lines the bay's gap up with an existing aisle, yielding face-to-face or back-to-back rows. *[claimed]*
- Shapely collision checks — Polygons are shrunk 1 mm before overlap tests so bays can touch edge to edge. *[claimed]*
- Parallel exploration with time cut-off — One worker per CPU core uses a different gravity direction; run stops at about 27 s to return a valid layout. *[claimed]*
- Objective score — Price-to-load ratio raised to a power that penalises low area usage. *[shown_working]*
- Interactive and 3D visualizer — Streamlit and Plotly app with layers, captions, score metrics, and a list for moving or deleting bays. *[claimed]*

**Flow:** Load a warehouse topology and bay catalog → Run the optimizer → Review the layout and score in 2D or 3D → Move, remove or clear bays manually in the viewer

**Prompt:** not public / not found
**Fit (explicit):** Devpost frames it as the Mecalux challenge: a 2D bin-packing problem with physical constraints and a non-linear area versus price/load objective. Official brief not retrieved.  *(targeted: Mecalux 2nd place)*
**AI:** none
**Architecture:** Python dataclasses model the warehouse; Shapely geometry engine; heapq-driven packer run via multiprocessing; Streamlit and Plotly visualizer.
**Novelty:** Uses a crystallisation-like active-node packer with gravity directions per worker instead of grid scanning, and an aisle-sharing rotation rule; no ML.
**Scope:** small · working: About 2k LOC with 20 public test case files and a prototype folder; no demo link. · polish: Detailed README with maths and sections; screenshots in img folder; no tests.
**Claims:** Zero-collision guarantee via polygon engine | Always returns a valid layout before the 30 s limit | Generalises better than ray-casting and axis-lock approaches
**Gaps:** Mecalux brief not on public page; No numeric scores published; README partially read (first ~7000 chars)
Sources: https://devpost.com/software/baymaxxing-qglxnc, evidence/hackupc-hackupc-2026-baymaxxing.json, https://hackupc-2026.devpost.com/

---

### Bender Blender
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Jetbrains] 3rd place [3rd]; [MLH] Best Domain Name from GoDaddy Registry

**What it is:** A Next.js tool that maps a local code folder into an Obsidian-style dependency graph and lets you navigate it by voice or text. Qwen 3 32B on Groq, or local Gemma via Ollama, picks the target file and a summary read aloud; a Ledger USB badge shows privilege.
**Problem / user:** Developers onboarding to unfamiliar repositories who lose time reconstructing structure through grep and import-hopping.

**Features**
- Repository dependency graph — Walker honouring .gitignore plus per-language extractors (JS/TS, Python, Dart, generic) and an import resolver build nodes and edges. *[shown_working]*
- Force-directed canvas — react-force-graph-2d with nodes sized by import count, entry points marked, 5000-node cap. *[shown_working]*
- Voice or text navigation — Web Speech API captures a request; the model picks a hub, refines via neighbours, returns focus and summary. *[shown_working]*
- Spoken summaries — ElevenLabs flash TTS reads the summary, started on the first sentence. *[claimed]*
- Cloud-to-local fallback — If Groq is unavailable, navigation uses Ollama with gemma4:e2b. *[claimed]*
- Ledger privilege badge — Server polls USB devices every 2.5 s for a Ledger vendor ID and updates a Granted Privileges badge. *[claimed]*
- .algo subnodes — Pre-computed AI expansions overlay on nodes without altering source files. *[claimed]*
- Multi-repo, diff mode, IDE plugin — Future work. *[planned]*

**Flow:** Paste an absolute repo path and press Map → Explore the graph → Press the microphone or type a request → View jumps to the matched file with a summary read aloud → Expand .algo subnodes; badge reflects Ledger connection

**Prompt:** MLH GoDaddy Registry prize: register a domain with GoDaddy Registry to qualify. JetBrains challenge brief not on the public page.
**Fit (implied):** Domain prize via benderblender.cooking demo site; developer-tool framing for the JetBrains track (not stated on page).  *(targeted: JetBrains 3rd place, MLH Best Domain Name from GoDaddy Registry)*
**Sponsor tools:** ElevenLabs TTS (Reads navigation summaries aloud, supporting); Ledger USB device (Hardware badge for privilege level, supporting); GoDaddy Registry domain (benderblender.cooking demo domain, token)
**AI:** Qwen 3 32B via Groq selects a focus from a shortlist of high-degree nodes and refines among neighbours; gemma4:e2b via Ollama is the local fallback and file summarizer.
**Architecture:** Single Next.js app: analyze, warm and navigate API routes, regex-based analyzers, ObsidianGraph and VoiceNavigator components, in-memory cache; no database.
**Novelty:** Blends voice-driven code-map navigation with a physical hardware key indicator and offline local-model fallback.
**Scope:** medium · working: Hosted demo at benderblender.cooking and a YouTube video; repo about 8.4k LOC. · polish: Detailed README with env vars and limits; no tests.
**Claims:** Graph appears in under ten seconds | Model round trip 1-3 seconds | Handles five import conventions without config
**Gaps:** JetBrains brief not found; Benchmarks not verified; Repo name spoon-map differs from project name
Sources: https://devpost.com/software/bender-blender, evidence/hackupc-hackupc-2026-bender-blender.json, https://hackupc-2026.devpost.com/

---

### BioMeshP2P
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Pears] 1st place [1st]

**What it is:** A peer-to-peer environmental monitoring prototype for Barcelona heat risk. Three emulated Arduino UNO Q emitter nodes run a tiny TensorFlow.js classifier on mock sensor readings, share verdicts over the Pear stack, and trigger a collective alert when most agree; an observer feeds a React dashboard.
**Problem / user:** People exposed to heatwaves; the team wanted automated heat-prevention such as park cooling, run without a central server.

**Features**
- Local edge risk classification — Each node runs a 5-16-8-1 MLP (about 2.5 KB) on temperature, humidity, wind, light and air quality; threshold heuristic as fallback. *[shown_working]*
- P2P replication — Hyperswarm and HyperDHT discovery with an Autobase multi-writer log shares readings and verdicts between nodes. *[shown_working]*
- Consensus alert — If at least 2 of 3 peers report high risk, the observer triggers an LED alert pattern standing in for AC or mist actions. *[claimed]*
- Real-time dashboard — Node observer broadcasts over WebSocket to a React/Leaflet/Recharts dashboard showing per-peer metrics. *[shown_working]*
- Mock sensors and training pipeline — Mock readings every 10 s; dataset from synthetic data plus Open-Meteo Barcelona; scripts train and verify the model. *[shown_working]*
- Cross-machine mode — Shell script launches emitters on separate machines by sharing a key. *[claimed]*
- Real Arduino deployment and biodiversity extension — Physical boards around Barcelona and species-aware models for parks. *[planned]*

**Flow:** Start emitter 1 and copy its key → Start emitters 2 and 3 and the observer → Nodes emit mock readings with local verdicts → Dashboard shows per-peer data → Consensus triggers the alert actuator

**Prompt:** not public / not found
**Fit (implied):** Built on the Pear runtime and Hyperswarm/Autobase stack, running decentralised nodes without a server. Pears challenge text not found; fit inferred from the stack.  *(targeted: Pears 1st place)*
**Sponsor tools:** Pear runtime, Hyperswarm, HyperDHT, Autobase (P2P node runtime, discovery and shared multi-writer log, core); Arduino UNO Q (Intended node hardware; emulated with mocks in the build, supporting)
**AI:** Small TensorFlow.js MLP classifier per node trained on synthetic and Open-Meteo data; README reports about 98% validation accuracy and under 1 ms inference.
**Architecture:** Three Pear emitter nodes write to an Autobase log over Hyperswarm/HyperDHT; Node observer reads, applies the 2-of-3 rule, drives LED and WebSocket to a Vite React dashboard.
**Novelty:** Combines on-node ML with serverless peer consensus to drive physical actuators; the build used emulated nodes and mock data.
**Scope:** small · working: Runnable multi-node start script and LED test commands; no physical boards mentioned on Devpost; no demo link. · polish: README with architecture diagram and model table; screenshots of dashboard and terminals; no tests.
**Claims:** Model about 98% validation accuracy | Inference under 1 ms | Model file about 2.5 KB
**Gaps:** Pears challenge text not found; Accuracy figures are self-reported on synthetic data; Devpost says nodes were emulated, README mentions UNO Q or PC mocks
Sources: https://devpost.com/software/biomeshp2p, evidence/hackupc-hackupc-2026-biomeshp2p.json, https://hackupc-2026.devpost.com/

---

### Carbassot climbing
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Mecalux] 1st place [1st]

**What it is:** A C++ warehouse bay-placement solver for the Mecalux challenge using fast construction, hill climbing and simulated annealing with parallel restarts, plus a React UI that loads the CSV inputs, runs the solver through an Express bridge and shows 2D and 3D results.
**Problem / user:** Warehouse layout planners placing storage bays in polygons with obstacles and stepped ceilings, minimising a price, load and area score.

**Features**
- Bay placement solver — Fast initial solution then improvement operators, hill climbing and simulated annealing across 10 parallel restarts, in C++. *[shown_working]*
- Geometry and constraint validation — Checks collisions, rotations, clearance gaps and ceiling heights on every move; angles in multiples of 90 in the output. *[claimed]*
- Quality metric — Q equals price per load raised to 2 minus bay area over free area; lower is better; UI scoring mirrors the solver. *[shown_working]*
- CSV workflow — Warehouse, obstacles, ceiling and bay type CSVs in, solution CSV out. *[shown_working]*
- 2D and 3D viewers — React with three.js in the browser, plus Python matplotlib visualisers. *[shown_working]*
- Test case library — 29 case folders including edge and hard cases. *[shown_working]*

**Flow:** Compile solver or start the Vite UI and Express bridge → Drop the four CSVs onto the loader → Click Run Solver → Inspect the layout in 2D or 3D with the Q score

**Prompt:** not public / not found
**Fit (explicit):** README says it was built for the Mecalux challenge: bay placement in polygon with obstacles and stepped ceiling minimising the stated metric. Official brief not retrieved.  *(targeted: Mecalux 1st place)*
**AI:** none
**Architecture:** C++17 solver reads case folders; Express bridge compiles and runs it; React/Vite/three.js frontend with a TypeScript copy of the scoring function.
**Novelty:** Native-code search solver with simulated annealing and many restarts, tied to a browser UI that reproduces the score exactly; includes 29 test inputs.
**Scope:** medium · working: About 10k LOC including 29 case folders; Devpost includes 2D and 3D screenshots; no demo link. · polish: Clear README with formats and commands plus a design doc; no automated tests in the tree despite Devpost saying tests were used.
**Claims:** 1st place in Mecalux challenge | UI scoring matches solver output to numerical precision
**Gaps:** Mecalux brief not on public page; No score results published; Devpost project title differs from repo name
Sources: https://devpost.com/software/el-carbasot-sml, evidence/hackupc-hackupc-2026-carbassot-climbing.json, https://hackupc-2026.devpost.com/

---

### convertfs
*HackUPC HackUPC 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** [HackUPC] 1st place [1st]

**What it is:** A Python FUSE filesystem that converts files when they are read. A user mounts it over a directory, drops a file in, and takes out the converted version. Supports video remuxing and H.264 compression, image format conversion, and PDF or Office to markdown.
**Problem / user:** Anyone who wants format conversion without separate tools or steps; Devpost states no explicit problem.

**Features**
- On-the-fly conversion via FUSE mount — pyfuse3 with trio generates the converted output lazily when the file is read from the mount. *[shown_working]*
- Video remux — MP4, AVI and MKV containers are remuxed using PyAV/ffmpeg. *[claimed]*
- Video compression — Compresses MP4 to H.264, picking the best encoder among NVENC, QSV and x264 with several presets. *[claimed]*
- Image conversion — pyvips converts between JPEG, PNG, TIFF and WebP. *[claimed]*
- Documents to markdown — Microsoft markitdown converts PDF and Office files to markdown. *[claimed]*
- CLI — Run convertfs with a mount point, or uv run convertfs --mount. *[shown_working]*

**Flow:** Install via pip or uv → Mount convertfs over a directory → Move or drag a file into the mount → Read or move out the converted file

**Prompt:** not public / not found
**Fit (none):** Entered for the overall prize; Devpost and README name no theme or sponsor challenge.  *(targeted: HackUPC 1st place)*
**AI:** none
**Architecture:** Python 3.11 package: FUSE layer with trio, handlers per media type wrapping PyAV, pyvips and markitdown; Nix dev shell and uv; tests folder present.
**Novelty:** Frames conversion as a filesystem operation so any app or file manager triggers it by copy and move.
**Scope:** small · working: Installable package with CLI and a test folder; about 2.5k LOC; no demo video. · polish: Short README with supported types; Devpost page minimal; no screenshots.
**Claims:** 1st place overall at HackUPC 2026
**Gaps:** No sponsor or theme stated; Devpost has no problem statement, challenges or next steps; Whether the HackUPC 1st prize is the overall award or a challenge award is unclear
Sources: https://devpost.com/software/convertfs, evidence/hackupc-hackupc-2026-convertfs.json, https://hackupc-2026.devpost.com/

---

### Djubrino
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Qualcomm] 1st place [1st]

**What it is:** Smart underground waste containers with an Arduino UNO Q in each, sensing fill level, nearby litter, fire, temperature and humidity with local AI. Data goes to a FastAPI and MongoDB backend and a Next.js city dashboard with map, alarms and device configuration.
**Problem / user:** Maintenance crews and city residents dealing with overflowing containers, litter and odour; the team saw full bins in Barcelona.

**Features**
- Overflow detection — Ultrasound distance sensor measures trash level in the container. *[claimed]*
- Litter around container detection — Custom vision model trained in Edge Impulse runs on the edge device. *[claimed]*
- Fire and odour indicators — Fire sensor (work in progress) plus temperature and humidity to estimate putrescence. *[claimed]*
- Device telemetry API — Devices or a Python simulator authenticate with device tokens and post telemetry and events; MongoDB stores them; offline devices detected by a background job. *[shown_working]*
- Operator dashboard — JWT-secured views: map, container and alarm tables, event evidence images, device list and remote configuration. *[claimed]*
- Route optimisation and live alerts — OR-Tools routing deferred; real-time alerts and more containers planned. *[planned]*

**Flow:** Container device senses fill, fire, humidity and nearby litter → Edge inference sends data and event images to backend → Backend stores telemetry and raises alarms → Staff open the map dashboard and alarm views → Staff review evidence and reconfigure devices

**Prompt:** not public / not found
**Fit (implied):** Runs custom edge AI on Arduino UNO Q boards using the STM32 and Qualcomm chips; Qualcomm brief not retrieved.  *(targeted: Qualcomm 1st place)*
**Sponsor tools:** Arduino UNO Q (Qualcomm) (Edge device reading sensors and running local inference, core); Edge Impulse (Training the litter detection model, supporting)
**AI:** Custom image model for litter around containers trained in Edge Impulse and deployed on the UNO Q; other signals are sensor readings.
**Architecture:** UNO Q embedded firmware in C; FastAPI backend with MongoDB Atlas and local image storage; Next.js shadcn dashboard in separate repo; device simulator for demos.
**Novelty:** Combines several waste-management signals in one underground-container device and ships a simulator so the dashboard can be shown with many devices.
**Scope:** medium · working: Backend about 5k LOC with docs and simulator; embedded and frontend in separate repos not read; no video. · polish: Thorough backend README with diagrams, roles and flows; dashboard screenshots; no tests.
**Claims:** Full pipeline from embedded device to dashboard | Custom waste detection model deployed on edge
**Gaps:** Only the backend repo was read; frontend and embedded repos were not; Qualcomm brief not found; Fire sensor marked WIP; no accuracy metrics
Sources: https://devpost.com/software/djubrino, evidence/hackupc-hackupc-2026-djubrino.json, https://hackupc-2026.devpost.com/

---

### FestiCleaner
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Qualcomm] 2nd place [2nd]

**What it is:** An autonomous trash-collecting rover built from cardboard and jar lids around an Arduino UNO Q. A camera and detection model find bottles and cups, a time-of-flight sensor guides the approach to a gripper, and a React dashboard shows the live annotated video, telemetry and a remote kill switch.
**Problem / user:** Organisers cleaning plastic waste left in squares after Barcelona street festivals, which takes heavy manual labour.

**Features**
- Camera trash detection — Vision model trained on hand-annotated images (Edge Impulse; README says COCO-SSD, Devpost lists YOLOv8) targets bottles and cups. *[claimed]*
- Pulse-steering approach — State machine turns in short time pulses toward the target and uses a ToF distance sensor to stop within gripper reach. *[claimed]*
- Pick and drop-off cycle — Search, grab with a custom gripper, then return the waste to a collection unit. *[claimed]*
- Temperature and humidity telemetry — Modulino Thermo readings are posted to the backend; dashboard alerts when it gets too hot. *[claimed]*
- Live dashboard — FastAPI with SQLite and WebSockets feeds a React/Vite page with annotated video HUD, gauges and cleaning progress. *[claimed]*
- Remote power switch — Dashboard control turns the robot on or off as a safety kill switch. *[claimed]*
- Swarm, text-to-speech anti-litter messages, sleeker chassis — Listed future work. *[planned]*

**Flow:** Connect robot and computer to the same hotspot → Plug in camera then battery to start → Robot searches, approaches and picks up trash → Operator watches video, progress and sensors on the dashboard → Operator can kill power remotely

**Prompt:** not public / not found
**Fit (implied):** Edge AI on an Arduino UNO Q with onboard vision for urban cleanliness in Barcelona; Qualcomm brief not retrieved.  *(targeted: Qualcomm 2nd place)*
**Sponsor tools:** Arduino UNO Q with Modulino Distance and Thermo (Robot controller and sensors, running vision at the edge, core); Edge Impulse (Training the trash detection model, supporting)
**AI:** Object detection model trained on self-annotated images, run on the edge; Python robot-brain process forwards detections to the embedded state machine and backend.
**Architecture:** C++ state machine on the board for motors and sensors; Python bridge runs vision and posts HTTP; FastAPI/SQLite/WebSocket backend; React dashboard.
**Novelty:** A physical autonomous robot built from recycled materials, with the full pick-and-place cycle and live telemetry, in a hackathon timeframe.
**Scope:** medium · working: Repo about 7.5k LOC with Arduino app, backend and frontend; demo video linked; Devpost admits motors were too weak and power bank must be lifted. · polish: README with run instructions and tech stack; physical rover built from scrap; no tests.
**Claims:** Working autonomous robot that cleans trash | Built from recycled materials
**Gaps:** Detection model differs between README (COCO-SSD) and Devpost (Edge Impulse, YOLOv8 tag); Whether full autonomous pickup worked end to end in demo is not confirmed; video not viewable; Qualcomm brief not found
Sources: https://devpost.com/software/festicleaner, evidence/hackupc-hackupc-2026-festicleaner.json, https://hackupc-2026.devpost.com/

---

### guAIta
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Qualcomm] 3rd place [3rd]

**What it is:** An edge-AI proof of concept for spotting wild boars in Collserola. Arduino UNO Q stations run a small Edge Impulse detector locally, send compact events to a server that scores risk and shows a map dashboard, and ElevenLabs voice calls escalate high-risk sightings to authorities.
**Problem / user:** Authorities facing African swine fever risk who rely on costly static forest patrols; they need targeted alerts and faster field response.

**Features**
- On-device wild boar detection — FOMO model from Edge Impulse on UNO Q with a USB camera; core model under 1 ms per README profiling. *[claimed]*
- Sliding-window confidence filter — Averages confidence over the last 20 frames and alerts only above 0.7 so one frame cannot trigger. *[claimed]*
- Risk scoring and recommendations — Deterministic backend logic scores events and suggests actions. *[shown_working]*
- Map dashboard — React with MapLibre shows stations, detections, risk zones, timelines and escalation status, updated by Socket.IO. *[shown_working]*
- Automated voice escalation — ElevenLabs places a call for high-risk events covering place, reason and next steps. *[claimed]*
- Sensor context and station controls — Modulino distance, thermo and light add context; buttons toggle standby and bounding-box overlay. *[claimed]*
- Unified event contract with simulator — Device, scenario and manual demo events share one Zod schema; reset-demo script gives a repeatable demo. *[shown_working]*

**Flow:** Station detects a boar and filters over 20 frames → Compact event posts to Fastify server → Server scores risk and recommends action → Dashboard map updates live → High-risk event triggers an automated ElevenLabs call

**Prompt:** As restated in the project README: build an Edge AI solution for a more biodiverse and resilient Barcelona, centred on Arduino UNO Q with local on-device inference; judged on creativity, technical execution and scalability.
**Fit (explicit):** README maps itself to the stated criteria: local inference on UNO Q for Collserola wildlife monitoring, with impact via targeted response. Official Qualcomm text not fetched.  *(targeted: Qualcomm 3rd place)*
**Sponsor tools:** Arduino UNO Q (Edge station running boar detection locally, core); Edge Impulse FOMO (Training and deploying the detector, core); ElevenLabs (Automated voice calls to authorities, supporting)
**AI:** Tiny FOMO object detector trained on the team's boar dataset runs on the board with a 20-frame confidence filter; risk scoring and recommendations are deterministic; ElevenLabs generates call audio.
**Architecture:** UNO Q station posts JSON; Fastify, TypeScript, SQLite and Socket.IO server with Zod schemas; React/MapLibre dashboard in a monorepo.
**Novelty:** Frames edge AI as public-budget optimisation, replacing static patrols with event-driven response, and closes the loop with an automated phone call.
**Scope:** medium · working: Repo about 11k LOC with server, web app, Arduino code and docs; four screenshots; no live demo or video. · polish: Extensive README and docs folder, health check, typecheck and demo reset scripts; no tests.
**Claims:** Model inference under 1 ms in profiling | Alert requires 20-frame average above 0.7
**Gaps:** Official Qualcomm brief not on public page; summary comes from the README; No measured field accuracy; Demo relies on simulated events as well as device
Sources: https://devpost.com/software/guaita, evidence/hackupc-hackupc-2026-guaita.json, https://hackupc-2026.devpost.com/

---

### hpcp
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [HP] 2nd place [2nd]

**What it is:** A deterministic digital twin of the HP Metal Jet S100 that couples six printer components with wear physics, separate true and sensor-observed states, a maintenance agent, and a chat copilot that must cite tool results for every claim about printer state.
**Problem / user:** Maintenance operators of industrial binder-jet metal printers, where components age, climates differ and sensors can drift or lie, so the perceived machine state may not match reality.

**Features**
- Coupled wear simulation of six components over three subsystems — Weekly ticks apply Archard wear (blade), Lundberg-Palmgren/Weibull bearing life (rail), Coffin-Manson fatigue plus clog hazard (nozzle), Arrhenius drift (heater, sensor); cascades via ten factors. *[shown_working]*
- True vs observed state — Per-component sensor models report ok, noisy, drift, stuck or absent; observed status becomes UNKNOWN when too many sensors fail; dashboard toggles the two views. *[shown_working]*
- Maintenance agent with three policies — Heuristic policy emits TROUBLESHOOT/FIX/REPLACE; an LLM-as-policy variant and a no-agent baseline are compared on the same seed over 180 days. *[shown_working]*
- Deterministic seeded historian — Random draws seeded per tick and component, results stored in SQLite WAL so runs reproduce identically across machines. *[shown_working]*
- Grounded chat copilot with nine tools — Tools list runs, fetch state at a tick, series, events, compare runs and run scenarios; every claim must cite runId, tick and componentId. *[claimed]*
- Sensor trust inspection — inspectSensorTrust helps tell a genuine component fault from a misleading sensor reading. *[claimed]*
- Structured UI cards in chat — A renderUI tool with a strict schema lets the agent draw cards and custom graphs in the chat app. *[claimed]*
- Climate-driven drivers and chaos layer — Synthetic temperature/humidity drivers for Barcelona and Phoenix (110 vs 60 weekly hours), live weather input, stochastic shocks, ML surrogate for the heater. *[shown_working]*

**Flow:** Pick or launch a scenario (location, seed, policy) in the Streamlit dashboard → Simulation advances week by week, writing true and observed state to the historian → Inspect time series and the true-vs-observed toggle → Compare no-agent, heuristic and LLM policies in the A/B chart → Open the SvelteKit chat and ask about printer state → Agent calls tools and answers with cited run, tick and component, rendering cards or graphs

**Prompt:** Per the project page, HP asked for a co-pilot for the Metal Jet S100: a physics model of component aging, a simulator advancing time and persisting state, and a grounded language interface. Official challenge text was not public.
**Fit (explicit):** Delivers all three parts the page attributes to the brief: wear-physics model, persistent time-stepped simulator with historian, and a tool-grounded chat agent that cites its sources.  *(targeted: HP 2nd place)*
**AI:** Gemma 4-31B via OpenRouter powers the chat agent (nine tools, cited answers, UI cards) and an LLM-as-policy maintenance variant; the primary policy is heuristic and the heater has an ML surrogate.
**Architecture:** Python 3.12 simulation engine (FastAPI, NumPy, Docker) with double-buffered coupled step, chaos layer and SQLite historian; Streamlit dashboard; SvelteKit plus Convex chat app calling the historian via tools.
**Novelty:** Treats the operator's sensor view as a failable signal distinct from ground truth, with cited-evidence rules for the LLM and a three-policy A/B on identical seeds.
**Scope:** large · working: Large repo with tests, Docker and CI; Devpost screenshots of dashboard and agent; no demo link. · polish: Detailed README with architecture diagram, docs folder and brand assets; coefficients hand-calibrated, no real data.
**Claims:** Byte-identical historian output across machines for the same seed | Phoenix modeled at 110 hours per week versus 60 for Barcelona | Chat answers must cite runId, tick and componentId from tool results
**Gaps:** Official HP challenge text not public; No numeric A/B results reported; Only first ~7000 chars of README in evidence
Sources: https://devpost.com/software/metalmind, https://github.com/stickerdaniel/hackUPC (evidence README), https://hackupc-2026.devpost.com/

---

### JetSense: AI agents for printers.
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [HP] 1st place [1st]

**What it is:** A predictive-maintenance web dashboard for HP Metal Jet S100 printers: a learned stochastic degradation model, a 3D printer view with component health, email alerts, a PPO-based repair calendar under a budget, and a voice-driven AI assistant.
**Problem / user:** Operators of industrial metal printers who either replace parts on a fixed schedule (wasteful) or after failure (costly) and need health forecasts and a budgeted repair plan.

**Features**
- Stochastic degradation model — Health in 0 to 100 percent follows a differential equation driven by external inputs; rate constants learned from (inputs, health) samples with L1 regularization; maths in a linked PDF. *[claimed]*
- Multi-printer dashboard with 3D model — Next.js frontend shows several printers and a Blender-made 3D model highlighting monitored components, with predictions beside past health data. *[shown_working]*
- Failure-cause classification — Size of the health drop sorts failures: over 20 percent random/external shock, 10 to 20 percent cascade from another part, under 10 percent normal wear. *[claimed]*
- Email alerts — Maintainers are emailed on a large health drop or when a component falls below 10 percent. *[claimed]*
- Budgeted repair scheduling — PPO agent sees nine component healths, budget and time, chooses among 512 joint replacement combinations while keeping every part above 10 percent. *[claimed]*
- Repair calendar — Dashboard calendar presents the heuristically optimal repair schedule for maximum uptime at minimum cost. *[claimed]*
- Voice AI assistant — Speech-to-text (Whisper) feeds an LLM that queries the database and answers with trend analysis and printer-status summaries. *[claimed]*

**Flow:** Open the Vercel-hosted dashboard and pick a printer → View component health on the 3D model with past data and forecasts → Receive email alerts on sharp drops or below 10 percent → Check the calendar for the budgeted repair schedule → Ask the assistant by voice for trends or a status summary

**Prompt:** HP Metal Jet S100 challenge as described by the entries: model component degradation of the printer and build tooling around predicting failures; official wording was not public.
**Fit (explicit):** README titles the work as the HP Challenge and supplies a health model, monitoring dashboard, alerts, budgeted repair optimization and an assistant for the printer.  *(targeted: HP 1st place)*
**AI:** Learned stochastic health dynamics with L1-regularized rate fitting; PPO reinforcement learning (PyTorch) for repair scheduling over 512 actions; Whisper speech-to-text and an Anthropic LLM answering from Supabase data.
**Architecture:** Next.js/React frontend on Vercel with three.js model; Flask backend on Hugging Face serving PyTorch models; Supabase database; speech to text to LLM to DB to LLM loop for the assistant.
**Novelty:** Combines a differential-equation health model, reinforcement-learning repair scheduler with joint replacement actions, and a voice assistant in one maintenance product.
**Scope:** small · working: Live Vercel demo linked and dashboard screenshots; small repo of 43 files with Flask backend and frontend. · polish: 3D printer model, PDF write-up of the maths; no tests or CI; no accuracy metrics given.
**Claims:** PPO state is 11 values and action space 512 combinations | Model predicts future health samples (no accuracy reported)
**Gaps:** Official HP challenge text not public; PDF paper not read; LLM identified only via anthropic dependency in requirements
Sources: https://devpost.com/software/jetsense-ai-agents-for-printers, https://github.com/Litusiano/hackupc-2026 (evidence README)

---

### OpenPlanner
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Jetbrains] 2nd place [2nd]

**What it is:** A Cursor and VS Code sidebar extension that stores AI-agent work as plain JSON plans containing phases and tasks, drafts plans from chat, and dispatches a phase's prompt to an agent CLI (Cursor, optionally Junie) while streaming output back.
**Problem / user:** Developers using AI coding agents whose plans scatter across chats and terminals, forcing them to rebuild context each session.

**Features**
- Plan tree in sidebar — Plans, phases and tasks live as JSON in .planstack/plans with five shared states; parent state reflects children, with badges and inline buttons. *[shown_working]*
- Plan drafting by chat — Chat panel runs the agent CLI read-only on a goal, validates the JSON it returns and saves the plan. *[shown_working]*
- Run phase / plan / task — Builds a focused prompt and dispatches to the configured executor (Cursor CLI default, Junie option), optionally on a prepared git branch, then marks state from exit. *[shown_working]*
- Dependency validation — Load-time checks reject cycles, unknown ids, self references and duplicates, including cross-plan references. *[claimed]*
- Output streaming safeguards — Coalesced buffering, replay for late panels, truncation notice, run lock against double clicks, and heartbeat for hung processes. *[claimed]*
- Context mentions — Chat supports @file, @phase, @task and @symbol within a token budget. *[claimed]*
- Optional MongoDB Atlas sync — Last-write-wins with revision counter, disk remains canonical; push and pull from the Overview panel. *[claimed]*
- Git diff summary and file watcher — After each run a short diff summary is posted to chat; external edits to plan files reload the tree. *[claimed]*

**Flow:** Install the extension and set the Cursor or Junie CLI key → Describe a goal in the Chat panel to create a plan → Review phases and tasks in the Plans tree → Run a phase, choosing to prepare a branch or run on the current one → Watch agent output stream into chat → Read the git diff summary and see states update

**Prompt:** JetBrains sponsor challenge; no public text found. The page lists Junie among built-with tools, implying a developer-tooling or agent theme.
**Fit (implied):** Offers Junie CLI as an alternative executor beside Cursor and frames the product as an agent-orchestration layer for editors.  *(targeted: JetBrains 2nd place)*
**Sponsor tools:** JetBrains Junie CLI (Optional executor profile for running phases, supporting); MongoDB Atlas (Optional plan sync across machines, supporting)
**AI:** No model of its own; delegates plan generation and phase execution to external agent CLIs (Cursor agent, Junie) via headless prompts.
**Architecture:** TypeScript VS Code extension with webview chat and tree views, a dispatch router to CLI or clipboard, JSON files as source of truth with file watcher, and optional MongoDB sync.
**Novelty:** Product boundary stays at structured intent through start of execution; plans are portable JSON with dependency graphs across plans rather than ephemeral chat plans.
**Scope:** medium · working: Installable VSIX build instructions and three screenshots; 72 files, about 16k LOC. · polish: Detailed README, concurrency and streaming hardening; no tests, internal codename Planstack still visible.
**Claims:** Plain JSON plans can be committed, diffed and shared | Disk as single source of truth removed tree-versus-file bugs
**Gaps:** Official JetBrains challenge text not public; No demo video
Sources: https://devpost.com/software/openplanner, https://github.com/NatanSisoev/OpenPlanner (evidence README)

---

### PearPost
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Skyscanner] 1st place [1st]

**What it is:** A serverless peer-to-peer inbox protocol on the Pears/Holepunch stack that lets personal AI agents find each other on the public DHT, exchange sealed typed messages, call each other's tools, and shows the conversations as a live graph in a desktop app and CLI.
**Problem / user:** People and developers running personal agents (Hermes, OpenClaw) that live in isolated chats and cannot talk, delegate or form groups without a central platform.

**Features**
- Permanent pear+agent address and discovery — Each agent owns an address and an append-only Hypercore outbox; peers find and follow each other via Hyperswarm DHT. *[shown_working]*
- Encrypted typed envelopes — Messages are sealed-box encrypted to the recipient and typed: chat, tool invoke/result, task request/result, presence, ack. *[shown_working]*
- Agent-to-agent RPC — tool.invoke and tool.result pair by inReplyTo so one agent can call another's tools. *[claimed]*
- Shared rooms — Group coordination uses Autobase rooms. *[claimed]*
- Attachments — Files travel as Hyperdrives. *[claimed]*
- CLI — Commands id, chat, tail, discover, invoke, room and mcp run headless without the desktop UI. *[shown_working]*
- Desktop agent graph — Pear app shows agents as nodes, threads as edges, with pulses for live message types. *[claimed]*
- Hermes and OpenClaw skills — Packaged skills connect those existing agent frameworks to the protocol. *[claimed]*

**Flow:** Run id to get a pear+agent address → Add a peer's address as a contact → Send chat or invoke a tool from the CLI → Peer's agent scans outbox, decrypts, stores in local Hyperbee → Open the Pear desktop app to see threads as a live graph

**Prompt:** Skyscanner sponsor challenge; no public text found. Page says it entered Pears, Bending Spoons, Skyscanner and JetBrains tracks and mentions trip-planning groups, delegates negotiating and IDE agents.
**Fit (implied):** Page names the four tracks and ties agent-to-agent negotiation and group trip planning to its inbox protocol; no Skyscanner API use appears in README.  *(targeted: Skyscanner 1st place, Pears, Bending Spoons, JetBrains)*
**Sponsor tools:** Pears / Hypercore stack (Hyperswarm, Hypercore, Hyperbee, Autobase, Hyperdrive and desktop runtime, core)
**AI:** Protocol-level only; no model chosen. Connects existing agents through skills and MCP-style tool interfaces.
**Architecture:** protocol/ (identity, envelope, outbox, inbox, directory, rooms, rpc) on Hypercore/Hyperswarm with sodium-native sealing; bin/ CLI; app/ Pear desktop UI with SSE backend; skills for Hermes and OpenClaw.
**Novelty:** Treats agent messaging as an account-free P2P protocol where threads form a graph and new message types need only a body shape and renderer.
**Scope:** medium · working: README gives a two-terminal CLI try-out; repo has tests and protocol modules; no demo video. · polish: Clean README with protocol summary; desktop app and two agent skills included; no CI.
**Claims:** No servers, accounts or gateways needed | Working peer-to-peer agent messaging protocol
**Gaps:** Official Skyscanner/Pears challenge text not public; README feature list is truncated at 7000 chars
Sources: https://devpost.com/software/bot-com, https://github.com/EternalRecursion121/post (evidence README)

---

### PearUp
*HackUPC HackUPC 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** [HackUPC] 2nd place [2nd]

**What it is:** SwiPears, a fully peer-to-peer dating app on the Pear runtime where each device trains a small neural network on the user's own swipes and shares only weight updates, which peers merge with federated averaging; includes encrypted P2P chat and profiles.
**Problem / user:** Dating-app users who do not want swipe histories held on company servers, while still benefiting from a recommender that improves collectively.

**Features**
- Swipe-and-learn local model — Each like or pass trains a 6-16-8-1 network with Adam and binary cross-entropy; profile rankings update at once. *[shown_working]*
- Federated averaging over the swarm — Devices broadcast weight arrays with sample counts over Hyperswarm and each peer applies sample-weighted FedAvg. *[shown_working]*
- Epidemic relay — Gossip layer delivers weights, chat and identity when direct hole-punching fails behind NAT or AP isolation. *[claimed]*
- Append-only weight ledger — Per-peer Hypercore logs are merged by Autobase into one causal timeline. *[claimed]*
- Encrypted P2P chat — Direct messaging between connected peers with unread badge in a Chat tab. *[shown_working]*
- Profiles and zero-config join — Persistent local profile shared via relay; every device auto-joins one shared room on launch. *[shown_working]*
- Convergence dashboard and peer simulator — WebSocket Chart.js dashboard plus a CLI auto-swiping peer let a demo show multiple models converging. *[shown_working]*
- Dual ML implementations — Pure-JS network for the Bare runtime and TensorFlow.js for Node tests share one weight format. *[shown_working]*

**Flow:** Run the published Pear app or pear run --dev → App auto-joins the shared room and discovers peers → Swipe on profiles with buttons or arrow keys → Weight updates broadcast and merge across peers → Chat with connected peers and edit own profile → Watch convergence on the separate dashboard

**Prompt:** Awarded as HackUPC 2nd place with no named sponsor track on the page; the repo credits Pear/Holepunch (the Pears sponsor challenge) but no challenge text was public.
**Fit (implied):** README states it is built for HackUPC 2026 and powered by Pear/Holepunch, using Hyperswarm, Hypercore and Autobase as the core of a serverless design.  *(targeted: HackUPC 2nd place)*
**Sponsor tools:** Pear / Holepunch (Hyperswarm, Hypercore, Autobase) (P2P discovery, weight logs, runtime and desktop shell, core)
**AI:** Small per-device neural net (6 inputs, dense 16 and 8 ReLU, sigmoid output) predicting swipe preference; federated averaging of weights across peers; pure-JS backprop because Bare lacks native ML.
**Architecture:** Pear/Bare app owns Hyperswarm, ML model, WebSocket bridge and identity; Electron-style UI with swipe, chat and profile tabs; Hypercore/Autobase logs; separate Node viz server simulating N peers.
**Novelty:** Federated learning applied to dating recommendations with no server at all, including a from-scratch network because the P2P runtime cannot load native ML addons.
**Scope:** medium · working: Published pear:// release, tests and CLI peer simulator; Devpost says stability dropped with more than 3 users. · polish: Thorough README with diagrams and roadmap; profile data is mock; no video.
**Claims:** Raw swipe data never leaves the device; only weights are shared | Multiple peers converge on a shared matchmaking model
**Gaps:** Official prize text not public; Which Pears-track entry vs HackUPC general prize is unclear
Sources: https://devpost.com/software/pearup-fpg8sy, https://github.com/mserra0/dfl-pears (evidence README)

---

### Roam
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Skyscanner] 3rd place [3rd]

**What it is:** Roam is a Chrome extension that passively watches how a user engages with travel posts on Instagram and TikTok, scores destination intent, and surfaces those destinations with live Skyscanner flight prices and booking deeplinks.
**Problem / user:** Social-media users who watch travel content but never book, and whose real destination interest is hidden in scrolling behaviour.

**Features**
- Travel post detection — Captions, hashtags and location tags go to Gemma 4 via the Gemini API, which returns destination, country, IATA code and vibe tags. *[claimed]*
- Engagement signal tracking — Eleven signals such as save, share, profile click, rewatch, dwell time are inferred from DOM events with weights. *[claimed]*
- Intent Score — Deterministic scoring with non-linear dwell weights, 7-day half-life decay and a bonus per extra post on the same destination. *[claimed]*
- Destination feed with live prices — Backend queries Skyscanner for cheapest return flight from the home airport and returns airline, duration and booking link. *[claimed]*
- Saved wishlist — One-tap saved destinations with Skyscanner booking. *[claimed]*
- AI travel insight summary — Gemma 4 writes a natural-language summary of top-scoring destinations. *[claimed]*
- Persistent storage and analytics — MongoDB Atlas keeps events and scores per anonymous device ID; Atlas Charts dashboard (Devpost) or Power BI streaming (README) shows trends. *[claimed]*
- Throttling and consolidation — Client queue, post-ID cache and rate limiting for Gemini; nearby cities merged into a main airport hub except for very large countries. *[claimed]*

**Flow:** Install the Chrome extension → Scroll Instagram or TikTok normally → Extension detects travel posts and records engagement → Open Roam to see the Feed of destinations with flight prices → View ranked Intent Scores → Save a destination and book via Skyscanner deeplink

**Prompt:** Skyscanner sponsor challenge; no public text found. The project uses Skyscanner flight price and booking APIs to link inspiration to booking.
**Fit (implied):** Connects passive travel-content consumption to bookable flights through Skyscanner price lookup and deeplinks.  *(targeted: Skyscanner 3rd place)*
**Sponsor tools:** Skyscanner API (Live return-flight prices and booking deeplinks, core); MongoDB Atlas / Atlas Charts (Storing events and scores, analytics dashboard, supporting)
**AI:** Gemma 4 through the Gemini API classifies posts and extracts destinations (image and text) and writes summaries; ranking itself is deterministic maths.
**Architecture:** Chrome extension (content script DOM observer, background worker, scorer) posts to an Express proxy on Railway that calls Gemini and Skyscanner, persists to MongoDB Atlas and optionally streams telemetry.
**Novelty:** Infers travel intent from behavioural signals rather than asking the user, solo build, with a transparent additive scoring formula.
**Scope:** small · working: Demo video link, live Atlas Charts link and README with endpoints; extension plus backend, about 4.7k LOC. · polish: Clear design-decision README and mermaid diagram; no tests.
**Claims:** Detects 11 engagement types without native platform APIs | Intent score halves every 7 days | Built solo in 36 hours
**Gaps:** Devpost cites Atlas Charts while README cites Power BI streaming; feature list notes both; Video not watched; official Skyscanner text not public
Sources: https://devpost.com/software/roam-yxus4c, https://github.com/expires/skyscanner-upc (evidence README)

---

### Slap
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [Bending Spoons] 1st place [1st]

**What it is:** SLAP is a Slack bot that takes a non-technical teammate's plain-language report of a small website or infrastructure error, structures it with Gemini, opens a pending GitHub issue and pings the responsible developer, with a dashboard to track all requests.
**Problem / user:** Marketing and other non-technical staff who spot typos or wrong dates but must chain emails and managers before a developer files an issue.

**Features**
- Slack-first reporting — Users describe the problem in a Slack message to the bot with no GitHub knowledge needed. *[claimed]*
- LLM request structuring — Gemini extracts requester, description, complexity, status, creation date and assignee into a record with sequential REQ ids. *[claimed]*
- GitHub issue creation — Octokit finds the infrastructure repository and opens an issue from a standard template, held as pending approval. *[claimed]*
- Developer notification — Slack message to the assigned person with a summary and the issue link. *[claimed]*
- Tracking dashboard — Web dashboard lists requests by status, complexity, age and progress, with planned totals and breakdowns. *[claimed]*
- Human approval step — Developers approve, modify or reject pending issues; the system never changes production itself. *[claimed]*

**Flow:** Employee posts the error to the SLAP bot in Slack → Gemini turns it into a structured REQ record → SLAP creates a pending GitHub issue → Assigned developer is notified in Slack → Developer approves, edits or rejects → Team follows progress on the dashboard

**Prompt:** Bending Spoons sponsor challenge; no public text found. The README labels the project the 1st place Bending Spoons challenge entry.
**Fit (explicit):** README states it won the Bending Spoons challenge; it targets cutting engineering and management time spent routing small error reports into the dev workflow.  *(targeted: Bending Spoons 1st place)*
**AI:** Gemini API (google-genai) converts free-text Slack messages into structured task fields including a complexity rating; no other model use described.
**Architecture:** Slack Bolt bot and Express backend calling Gemini and GitHub via Octokit with a data store for requests; React dashboard frontend; exposed via ngrok for Slack events.
**Novelty:** Targets a workflow gap (non-developers reporting trivial fixes) rather than a new model; keeps a human approval gate before issues proceed.
**Scope:** small · working: Backend and React frontend of 66 files with demo folder and setup steps; no live link or video. · polish: Long README with examples and issue template; no tests or CI.
**Claims:** Reduces engineering and management overhead of small fix requests
**Gaps:** Official Bending Spoons text not public; No evidence of end-to-end demo run
Sources: https://devpost.com/software/slap-f6nxiq, https://github.com/mogonlac/hackupc2026 (evidence README)

---

### Smadex Creative Copilot
*HackUPC HackUPC 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** [HackUPC] 3rd place [3rd]

**What it is:** A creative-intelligence prototype for mobile advertisers: a Python scikit-learn/XGBoost/SHAP pipeline feeds one self-contained HTML dashboard with explorer, fatigue, recommendation, cluster, portfolio-optimizer and predict-creative tabs plus an LLM chatbot.
**Problem / user:** Advertisers and marketers who need to know why a creative wins or fades, which to scale, and how a new creative would score, rather than another dashboard.

**Features**
- Performance explorer — Browse and rank all 1,080 creatives by CTR, CVR, ROAS, IPM or spend, with filters and grid or chart views. *[shown_working]*
- Fatigue detection — Per-creative CTR time series, absolute or normalized to launch baseline, flags fatigued assets. *[shown_working]*
- Recommendations — KPI-aware Scale, Monitor or Pause action cards ranked by performance score. *[shown_working]*
- ML insights with SHAP — Random Forest and XGBoost feature importance, cross-validated R2 and MAE per target, per-creative SHAP drivers. *[shown_working]*
- Clusters with LLM personas — K-Means (k=8) groups creatives; an LLM writes a strategic description from each cluster's SHAP profile. *[claimed]*
- Diversity-aware portfolio optimizer — Strategy slider trades performance against diversity; Devpost says a 65/35 novelty-plus-cosine metric, README says Gram-Schmidt. *[claimed]*
- Predict Creative with Smart Fill — User describes a draft creative and gets a calibrated score; an LLM suggests defaults for missing features. *[claimed]*
- In-dashboard chatbot — Function-calling assistant can fetch creatives, list fatigued ones and run the optimizer; Devpost says Gemini, README says Claude Haiku. *[claimed]*

**Flow:** Run ml_pipeline_sklearn.py on the CSVs → Run build_dashboard.py to inject data into one HTML file → Open the file in a browser (no server) → Explore, filter and inspect fatigue per creative → Open a creative for AI analysis → Use Predict Creative or the chatbot

**Prompt:** Smadex mobile-advertising creative intelligence challenge, as restated in a project repo: using a synthetic dataset (1,080 creatives, 192k daily rows), help marketers see which ads work, which are fatiguing and what to do next; bonus for using creative images.
**Fit (explicit):** README says it was built for the Smadex Creative Intelligence Challenge and answers its questions: what works, what is fatiguing, what to test next, what a new creative would score.  *(targeted: HackUPC 3rd place, Smadex challenge)*
**AI:** Random Forest, XGBoost, PCA and K-Means on tabular plus Pillow image features, SHAP for attribution; LLM (Gemini per Devpost, Claude Haiku per README) for personas, per-creative analysis, chat and Smart Fill.
**Architecture:** CSV files processed by a Python pipeline into app_data.js and ml_results.json, patched into a template to make a single HTML dashboard with Chart.js and direct LLM REST calls from the browser.
**Novelty:** Ships as one offline HTML file with embedded ML results and an LLM assistant; adds image-derived features and a diversity slider to the optimizer.
**Scope:** medium · working: Repo includes 1,080 creative assets and pipeline plus build scripts; no live link or video. · polish: Detailed README tab reference; multi-tab dashboard; no tests; two builders new to ML.
**Claims:** Every recommendation traces to SHAP values and cluster context | Single-file dashboard runs offline with embedded LLM assistant
**Gaps:** Devpost (Gemini, 65/35 diversity, 9 image features) and README (Claude Haiku, Gram-Schmidt, 18 image features) differ; feature list follows Devpost for AI and lists both; Official challenge text not public; brief from sibling repo; R2 and MAE values not stated
Sources: https://devpost.com/software/smadex-creative-copilot, https://github.com/lalig777/Smadex-Challenge (evidence README)

---

### Smadex Creative Lab
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Smadex] 1st place [1st]

**What it is:** A React dashboard for Smadex marketers centered on a Survivability Lab that gives each ad creative a health score and fatigue forecast, with PCA portfolio-diversity maps, SHAP explanations and Gemma 4 insights streamed from a Node agent.
**Problem / user:** Marketers who discover a creative has fatigued only after losing money and want early prediction of when it will fail.

**Features**
- Creative health dashboard — Single dashboard monitors all creatives with health status. *[claimed]*
- Survivability Lab — Gives each creative a health score and estimates when it will begin to fail using hazard models. *[claimed]*
- Fatigue forecasting — Hazard-model approach separating a random bad day from real delivery decay. *[claimed]*
- PCA diversity maps — Maps show how varied the creative portfolio is. *[claimed]*
- SHAP explainability — Shows factors behind model decisions. *[claimed]*
- Gemma 4 AI insights — Separate Node agent analyses the data and streams commentary to the UI over SSE. *[claimed]*

**Flow:** Start the Docker stack with Postgres, FastAPI backend and React frontend → Open the dashboard on the Smadex data → Check creative health and survivability scores → View PCA and SHAP views → Read streamed AI insights

**Prompt:** Smadex mobile-advertising creative intelligence challenge, as restated in a project repo: using a synthetic dataset (1,080 creatives, 192k daily rows), help marketers see which ads work, which are fatiguing and what to do next; bonus for using creative images.
**Fit (explicit):** Page calls it a dashboard for Smadex and targets creative fatigue prediction; repo restates the brief's three questions on working ads, dying ads and next action.  *(targeted: Smadex 1st place)*
**AI:** Hazard (survival-style) models for fatigue, PCA and SHAP in the data-science layer; Gemma 4 in a Hono Node agent produces streamed insights over SSE.
**Architecture:** data_science notebooks and CSVs; web/ with Postgres, FastAPI backend, Hono AI agent using @google/genai and React/Vite/Recharts frontend, run via Docker.
**Novelty:** Frames fatigue as survival modelling and ships a separate streaming AI agent service; a large data-science folder supports the web app.
**Scope:** large · working: 2,834-file repo with Docker, tests and database-backed backend; no demo link or video. · polish: Extensive context README and dataset dictionary; Devpost claims a professional look; no live demo.
**Claims:** AI insights analyse real data rather than hardcoded text
**Gaps:** Root README is a dataset/context doc, not a product walkthrough; web/README not read; Devpost page is short with no flow; Official challenge text not public
Sources: https://devpost.com/software/smadex-creative-lab, https://github.com/jowelhub/HACK_UPC_SMADEX (evidence README)

---

### SmadexAd Courtroom
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Smadex] 2nd place [2nd]

**What it is:** A multi-agent debate system where five AI personas (performance, fatigue, risk, visual, audience) argue over an ad creative across three rounds and a judge issues a weighted verdict of scale, pause, pivot or test next, shown live in a Streamlit UI.
**Problem / user:** Marketers who see dashboards of what happened but no reasoning about why or what to do with each creative.

**Features**
- Five specialist agents — Performance Analyst, Risk Officer, Fatigue Detective, Visual Critic and Audience Simulator each assess a creative from its own angle. *[shown_working]*
- Three-round debate — Independent verdicts, cross-examination of conflicting claims, then revision, run concurrently by an async orchestrator. *[shown_working]*
- Weighted final verdict — Judge weighs opinions into SCALE, PAUSE, PIVOT or TEST_NEXT with a readable transcript. *[shown_working]*
- Fatigue slope metric — Linear-regression slope over a 7-day CTR window flags audience wear-out. *[claimed]*
- Custom agent-to-agent protocol — Independent FastAPI agent services exchange Pydantic messages; fallback parsers handle malformed JSON. *[claimed]*
- Live debate view — Streamlit UI streams the courtroom transcript with a node diagram. *[shown_working]*
- Caching for speed — SQLite cache keeps a debate under about 20 seconds. *[claimed]*

**Flow:** Open the Render-hosted Streamlit app → Pick an ad creative → Data (tabular metrics, base64 image) is aggregated with DuckDB and Pandas → Five agents give verdicts then cross-examine and revise → Read the final weighted verdict and transcript

**Prompt:** Smadex mobile-advertising creative intelligence challenge, as restated in a project repo: using a synthetic dataset (1,080 creatives, 192k daily rows), help marketers see which ads work, which are fatiguing and what to do next; bonus for using creative images.
**Fit (explicit):** Devpost says A2A debate was built to solve the Smadex challenge; agents cover performance, fatigue and visual quality to recommend actions on creatives.  *(targeted: Smadex 2nd place)*
**AI:** Five LLM personas debating via custom A2A messages; Devpost lists Gemma and Ollama, README mentions heuristic bounds with simulated LLM prompts and manifest includes anthropic; a judge weights outputs.
**Architecture:** DuckDB/Pandas aggregation over the provided parquet dataset; independent FastAPI agent microservices plus async orchestrator and synthesizer; SQLite cache; Streamlit front end deployed on Render.
**Novelty:** Frames ad analysis as an adversarial courtroom where agents may change their minds after peer evidence, using a hand-built A2A protocol instead of agent frameworks.
**Scope:** medium · working: Live Render URL and YouTube demo plus Docker setup; 7.5k LOC with agents, orchestrator and pipeline modules. · polish: Streamlit glassmorphism UI and 10 screenshots; no tests; project called Boardroom in README.
**Claims:** Debate completes in under 20 seconds with caching | Agents can officially change their minds after reviewing peer data
**Gaps:** README (Creative Boardroom, heuristic/simulated LLM) and Devpost (Courtroom, Gemma/Ollama) differ on how agent opinions are generated; feature list follows Devpost; Video not watched; official challenge text not public
Sources: https://devpost.com/software/ad-courtroom, https://github.com/GuillermoCalet/HACKUPC-2-26 (evidence README)

---

### Warehouse Yasolizer
*HackUPC HackUPC 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [Mecalux] 3rd place [3rd]

**What it is:** A single C++17 program that reads a warehouse description from CSV files, greedily packs storage bays to minimise a cost function that rewards used floor area, prints the layout and opens an interactive OpenGL 3D and minimap view.
**Problem / user:** Warehouse planners who need bay placement that fits irregular perimeters, obstacles and ceiling heights while maximising used area at low cost.

**Features**
- CSV warehouse ingestion — Reads perimeter, internal obstacles, ceiling profile and a bay catalogue (size, gap, loads, price). *[shown_working]*
- Greedy bay packing — Grid and polygon tests place bays to minimise Q = (sum price / sum loads) ^ (2 - fraction of area used). *[shown_working]*
- Layout output — Prints the chosen layout and score. *[claimed]*
- Interactive OpenGL visualisation — 3D view with orbit camera plus minimap of the placed bays, built with GLFW, GLEW and GLM. *[claimed]*

**Flow:** Provide the four CSV files → Run the executable through its five pipeline phases → Read printed layout and cost → Orbit the 3D view and check the minimap

**Prompt:** Mecalux sponsor challenge; no public text found. README describes a warehouse bay-placement cost function with CSV inputs, suggesting the brief.
**Fit (implied):** Optimises bay placement inside a warehouse polygon with obstacles and ceiling limits and visualises the result; the Mecalux link is inferred from the prize label.  *(targeted: Mecalux 3rd place)*
**AI:** Not an AI product; Gemini wrote a prompt and Claude generated the project skeleton per Devpost. The optimizer is a greedy heuristic.
**Architecture:** Four modules under src/: data_input (CSV), optimization (greedy fill), data_output (scene builder) and visualization (OpenGL renderer), one-way data flow.
**Novelty:** Pure C++ with a GPU visualiser rather than a web app; built through AI-assisted prompting.
**Scope:** small · working: Sample data CSVs and README with module layout; Devpost states only that it works; no screenshots or video. · polish: Clean modular structure and build instructions; no tests or demo assets.
**Claims:** Optimises bay placement quickly using GPU pipelining
**Gaps:** Mecalux challenge text not public; Devpost has almost no description; README does not mention GPU optimisation; No performance numbers
Sources: https://devpost.com/software/warehouse-yasolizer, https://github.com/Carlos-Prlt/HackUPC_2026 (evidence README)

---

