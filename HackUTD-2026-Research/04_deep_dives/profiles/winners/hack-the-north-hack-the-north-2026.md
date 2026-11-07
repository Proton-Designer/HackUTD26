# Hack the North — Hack the North 2026 (12 projects)

### Bing Bong
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Hack the North 2026: Finalists

**What it is:** A rhythm party game for up to four players that uses Hack the North PCB badges as wireless controllers. Custom badge firmware sends button presses over ESP-NOW to an ESP32-C6 USB relay on a laptop, where a web app runs the game and sends LED commands back.
**Problem / user:** No problem stated; made for friends playing together at the event using their conference badges as hardware.

**Features**
- Badges as controllers — Custom firmware on the HTN badge sends button presses to a receiver over ESP-NOW. *[shown_working]*
- Bidirectional relay — ESP32-C6 XIAO gateway bridges ESP-NOW and USB so the laptop can also trigger badge LEDs. *[shown_working]*
- Rhythm game web app — Node web app converts controller input into gameplay and scoring. *[claimed]*
- Multiplayer scoring — Up to four players compete for highest score. *[claimed]*

**Flow:** Flash badge and gateway firmware → Run web app → Players press badge buttons in rhythm → Relay forwards input to laptop → Game scores and lights badge LEDs

**Prompt:** Finalists main award: no first/second/third place; top projects become finalists; prize undisclosed (a surprise). Also a Best Badge Hack prize ($2,500) for creative use of the HTN badge, with Solana track.
**Fit (implied):** Entire project is built on the HTN badge hardware; page says the team came to hack the badges. Prize not named explicitly.  *(targeted: Hack the North 2026: Finalists, Best Badge Hack)*
**AI:** none
**Architecture:** Badge (ESP32-C3 custom firmware) -> ESP-NOW -> XIAO ESP32-C6 gateway -> USB -> laptop web app (src/) and back for LED triggers.
**Novelty:** Repurposes event badges as a multiplayer controller set with a custom radio relay; hardware and firmware over AI.
**Scope:** small · working: Repo about 5.5k LOC with firmware, web app, CAD; no demo video or screenshots of gameplay. · polish: Short README with flashing instructions; Devpost has joke captions only.
**Gaps:** Game mechanics and songs not described; Badge MCU: Devpost implies ESP32-C6 relay, README says badge is ESP32-C3; No video
Sources: https://devpost.com/software/bing-bong-z7rsny, https://github.com/sophiayduan/bingbong (evidence file), https://hackthenorth2026.devpost.com/

---

### Bricked
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Hack the North 2026: Finalists

**What it is:** A multi-agent system that turns a sentence into a buildable Lego model. A planner slices the design into layers, builders place bricks, a deterministic inspector checks physics and connectivity, and a vision critic reviews; the browser streams the build in 3D and exports a purchase link.
**Problem / user:** Lego hobbyists whose finished builds gather dust and who want new designs from existing bricks.

**Features**
- Text-to-Lego generation — Planner, per-layer builder, inspector and critic agents build bottom-up on a 20x20x20 grid. *[claimed]*
- Deterministic checks — Linting for bounds, collisions, connectivity plus a force/torque stand-up check; inspector can reject a layer. *[claimed]*
- Vision critic — A stronger Claude model reviews rendered output. *[claimed]*
- Live streaming and steering — SSE stream shows agent activity and geometry; steer bar lets user guide mid-build. *[claimed]*
- Natural-language edits — Existing models changed by instruction. *[claimed]*
- LDraw render and joints overlay — Model assembles brick by brick in Three.js. *[claimed]*
- Buy-all-parts URL — Exports a link to purchase components. *[claimed]*
- Scan-your-pile building — Build from owned bricks by scanning a pile. *[planned]*

**Flow:** Describe an idea in a sentence → Planner slices layers → Builder places and inspector checks each layer → Critic reviews → Watch 3D assembly, steer or edit → Export parts link

**Prompt:** Finalists main award: no first/second/third place; top projects become finalists; prize undisclosed (a surprise).
**Fit (none):** No sponsor prize stated; general finalist entry.  *(targeted: Hack the North 2026: Finalists)*
**AI:** Claude via CLI: Sonnet for planner and builders, Opus as vision critic, using a BrickGPT-style lintable grammar and a deterministic physics inspector to catch floating bricks.
**Architecture:** Python orchestrator (planner, builder, inspector, critic) -> SSE -> Next.js/Three.js viewer with LDraw rendering; repo also has brickify, bricolage and a brick-drop simulator for a brick scanner.
**Novelty:** Generate-and-verify loop where deterministic physics checks gate LLM output layer by layer; repo also includes synthetic-data simulator for a brick-scanning detector.
**Scope:** large · working: Repo about 21k LOC across web, brickify, bricolage, sim; no demo video or live demo. · polish: Only sim README read; Devpost has no video.
**Gaps:** Repo has scanner and simulator parts (YOLO training data) not described on Devpost; feature list follows Devpost; Edition-level screenshots not counted; No demo video
Sources: https://devpost.com/software/a-feuvb1, https://github.com/GuyOnWifi/hack-the-north (evidence file; README is sim/README.md), https://hackthenorth2026.devpost.com/

---

### CADEX
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2026: Finalists

**What it is:** A photo-to-print workflow: users give a prompt and reference photos, CADEX says which dimensions to measure with annotated callouts, then generates a parametric CadQuery model, validates it automatically, and exports STEP, STL and G-code plus engineering views and IKEA-style assembly instructions.
**Problem / user:** People with a clear idea for a simple physical object but no CAD skills, e.g. a broken foosball handle or a missing clamp.

**Features**
- Measurement planning from photos — OpenAI Responses API with structured outputs returns needed dimensions, priorities and photo callouts. *[shown_working]*
- Parametric CAD generation — Codex CLI writes a CadQuery program from confirmed measurements in an isolated workspace. *[shown_working]*
- Automatic geometry checker — Verifies geometry, dimensions and hole placement; failures sent back to Codex for retry. *[shown_working]*
- 3D preview — Three.js viewer for inspection. *[shown_working]*
- Fabrication exports — STEP, STL and G-code (when PrusaSlicer present). *[shown_working]*
- Drawings and manual — Dimensioned views and assembly instructions derived from the STEP file. *[shown_working]*

**Flow:** Upload prompt and photos → Receive measurement plan with callouts → Enter caliper readings, repeat until specified → CADEX generates and validates CAD → Inspect in 3D → Export and print

**Prompt:** OpenAI API Prizes: use the OpenAI API for something ambitious with Codex as teammate; judged on creative API use and how Codex helped; demo must show product and one concrete Codex benefit.
**Fit (implied):** Page credits OpenAI Responses API and Codex CLI as generator and Codex credits for building; does not name the prize.  *(targeted: Hack the North 2026: Finalists, OpenAI: API Prizes)*
**Sponsor tools:** OpenAI Responses API + Structured Outputs (Photo analysis and measurement plans, core); Codex CLI (Generates CadQuery models and dev work, core)
**AI:** OpenAI vision with schema-validated output plans measurements; Codex agent writes CadQuery code and self-inspects via a custom validator loop.
**Architecture:** React/Vite/Three.js frontend -> Hono Node server -> Python CadQuery pipeline with checker and slicer -> STEP/STL/G-code, drawings.
**Novelty:** Closes loop to a physically printed part (badge case fit) with caliper-guided measurement and automated geometry rejection.
**Scope:** medium · working: Printed badge case fit; demo video; repo about 4k LOC with tests and docs. · polish: Clear README with demo link and workflow; no live site.
**Claims:** Printed badge case fit with every screw aligned
**Gaps:** Not confirmed which prize it won beyond Finalists
Sources: https://devpost.com/software/cadex, https://github.com/justinbaduaa/htn2026 (evidence file), https://hackthenorth2026.devpost.com/

---

### Combadge
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2026: Finalists; Winner QNX: Create an Embedded System with QNX that Uses AI

**What it is:** A Star Trek style wearable voice assistant: a Raspberry Pi 5 on QNX 8.0 on the belt, a conductive-thread touch badge on a shirt, a mic, speaker and camera. Saying 'Computer' starts a GPT-Live conversation that can look through the camera, search the web, handle email and calendar, and shop via Shopify.
**Problem / user:** People wanting hands-free computing as a second brain without pulling attention away from the physical world.

**Features**
- Touch-badge activation — Double tap on MPR121 electrode wakes assistant with haptic and LED feedback. *[claimed]*
- Voice conversation — Mic audio streams to OpenAI GPT-Live; replies play via Bluetooth speaker using custom QNX PCM driver. *[claimed]*
- Camera look — 'Computer, look at this' captures a still for analysis, e.g. find similar item under a price. *[claimed]*
- Live web research — Browserbase search and page reading with call limits. *[claimed]*
- Gmail and Calendar — Composio-backed read, summarize, draft, with confirmation for changes. *[claimed]*
- Shopify discovery, inventory, checkout handoff — Catalog search by image, stock checks, restock draft emails, unpaid checkout handoff. *[claimed]*
- Phone and SMS via Twilio — SIP calls and texting, for handing off to a person. *[claimed]*

**Flow:** Double tap badge → Say 'Computer' plus request → Camera snapshot if asked → GPT-Live delegates tools → Spoken answer through Bluetooth speaker

**Prompt:** QNX: create an embedded system on QNX OS using an open-source AI module from oss.qnx.com; judged on cannot-fail embedded use, real-time reliability, creative AI, running on embedded hardware not cloud. Prizes $1,500/$500/$500.
**Fit (implied):** Runs on QNX 8.0 on a Pi 5 with custom Bluetooth and camera helpers, wearable form; voice AI is cloud-hosted GPT-Live. Page lists the QNX win.  *(targeted: QNX: Create an Embedded System with QNX that Uses AI, Hack the North 2026: Finalists)*
**Sponsor tools:** QNX 8.0 (OS on Raspberry Pi 5; custom Bluetooth audio driver path, camera helper, core); OpenAI GPT-Live (Voice interface and tool delegation, core); Browserbase / Composio / Shopify / Twilio (Web, Gmail/Calendar, commerce, calls, supporting)
**AI:** Realtime voice model (GPT-Live) over WebSocket delegates tasks to a backend model with tools; vision on camera stills; no local models.
**Architecture:** Shirt sensors/LED/haptic -> Pi 5 (QNX) Python app -> GPT-Live WebSocket -> tool layer (Browserbase, Composio, Twilio, Shopify, camera) -> Bluetooth speaker via qnx-bluetooth C driver.
**Novelty:** Wearable with sensors sewn into a shirt, running on QNX with a self-written Bluetooth audio path; commerce, email and phone tools behind one voice agent.
**Scope:** large · working: Detailed repo README with doctor command and safety limits; no demo video; limitations listed (no echo cancellation). · polish: Three org repos; Devpost has three photos, no video.
**Claims:** Won QNX prize (Devpost label)
**Gaps:** Evidence file clone failed (org URL); README found via org listing; Devpost mentions 'GPT-6 Astra' model name unverified; Sizes not measured
Sources: https://devpost.com/software/combadge, https://raw.githubusercontent.com/Combadge-HTN/Combadge-HTN-2026/HEAD/README.md, https://github.com/orgs/Combadge-HTN/repositories, https://hackthenorth2026.devpost.com/

---

### Composition
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence B · confidence low*
**Prizes:** Hack the North 2026: Finalists; Winner MLH: Best Use of Gemini API

**What it is:** A spatial AI filmmaking studio where the user physically moves inside a virtual scene, frames shots, directs characters and records camera movement with a phone, while an AI director turns that vision into cinematic footage saved as editable compositions. Built solo.
**Problem / user:** Creatives who can picture a scene but do not want to spend hours prompting AI; aims to keep creative control with the filmmaker.

**Features**
- Move inside a virtual scene — Three.js scene the user navigates physically. *[claimed]*
- Phone camera capture — Phone motion records camera movement for shots. *[claimed]*
- Character direction — User directs characters in scene. *[claimed]*
- AI director — Gemini (incl. Live) helps turn vision into footage; exact use unstated. *[claimed]*
- Editable compositions — Ideas saved as reusable edit-able compositions. *[claimed]*

**Flow:** Step into virtual scene → Move and frame shots with phone → Direct characters → AI director generates footage → Save editable composition

**Prompt:** MLH Best Use of Gemini API: build AI apps with Gemini that make friends say WHOA (chatbots, research summaries, creative content); prize Google swag kits.
**Fit (implied):** Gemini listed as the AI director; Codex used in development. Page does not name the prize.  *(targeted: MLH: Best Use of Gemini API, Hack the North 2026: Finalists)*
**Sponsor tools:** Gemini API (incl. gemini-live) (AI director; role unspecified, core)
**AI:** Gemini models act as the director; Codex used for development. Specific prompts and outputs not described.
**Architecture:** React/TypeScript/three.js front end with Node.js runtime, zod schemas, phone as motion input, Gemini calls.
**Novelty:** Physical-movement-driven virtual cinematography with AI assisting rather than generating from text alone.
**Scope:** small · working: Six screenshots; no video or demo link; repo unreadable. · polish: Single developer; page vague on pipeline.
**Claims:** Complete AI filmmaking studio built independently
**Gaps:** Repo clone and README fetch failed; How Gemini generates footage not explained; No video
Sources: https://devpost.com/software/composition, https://hackthenorth2026.devpost.com/

---

### Concerto
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2026: Finalists

**What it is:** A local concert system that turns audience phones into a distributed speaker array. Phones join by QR, sync clocks, download audio, flash an optical ID that cameras decode to locate seats, and an operator assigns Melody, Percussion or Vocals parts and runs a shared timeline.
**Problem / user:** Concert audiences and operators; replaces passive watching and flashlights with phones as a sound system.

**Features**
- Browser join and sync — QR join, NTP-style clock sync, audio predownload with SHA-256 checks, scheduled shared playback. *[shown_working]*
- Optical localization — Phone flashes red/blue 11-bit Hamming-coded ID; Python/OpenCV worker decodes from audience video to estimate position. *[claimed]*
- Operator console — Audience map, rectangle/lasso selection, per-channel gain/mute/solo, timeline, emergency mute-all. *[shown_working]*
- Part assignment — Phones get Melody, Percussion or Vocals by section; manual left/center/right fallback. *[shown_working]*
- Resilience — Auto reconnect, late join, autoplay handling, stale-command rejection. *[shown_working]*
- Projector and camera upload views — QR with readiness counts; resumable verified video uploads. *[shown_working]*

**Flow:** Scan projector QR → Phone syncs and downloads audio → Optical flash pattern recorded by camera → Operator reviews map and assigns parts → Run performance from shared timeline

**Prompt:** Finalists main award: no first/second/third place; top projects become finalists; prize undisclosed (a surprise).
**Fit (none):** No sponsor prize stated; Codex listed in built-with only.  *(targeted: Hack the North 2026: Finalists)*
**AI:** No AI inside product; computer vision decoding only.
**Architecture:** Bun/Hono backend with Next.js audience, operator, projector and upload frontends; Python OpenCV worker; shared Zod schemas; Web Audio playback.
**Novelty:** Systems-heavy project: synchronized multi-device audio plus camera-based seat localization with error-correcting optical codes, tested with 1,500 simulated clients.
**Scope:** large · working: Repo about 46k LOC with tests, Docker, CI; local software integration implemented, physical venue tests not done. · polish: Operator guide, Railway deployment doc, demo seed script.
**Claims:** Tested with 1,500 simulated WebSocket clients | About 99% phone detection accuracy (contributor claim, no method)
**Gaps:** Repo includes a large vendored beatsync-source, inflating size; Physical acceptance tests pending per README; No video
Sources: https://devpost.com/software/concerto-0wd9zs, https://github.com/nicholasching/HackTheNorth (evidence file)

---

### Keymaeleon
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2026: Finalists

**What it is:** A mechanical keyboard with an OLED display in every key whose labels and actions change with context. A desktop service and a VS Code extension watch the active app and editor state (tests, errors, git) and put actions like Run Tests, Fix, Commit on the keys.
**Problem / user:** Developers who must memorize shortcuts or hunt controls across apps.

**Features**
- Per-key OLED keyboard — Arduino Nano ESP32 reads switches, updates OLEDs, sends HID keyboard/media events over USB. *[shown_working]*
- Context-aware VS Code keys — Extension reports file, git, tests, terminal and debug state; keys switch among Run Tests, Debug, Explain, Fix, View Diff, Approve, Reject, Commit. *[claimed]*
- Active-window detection — Desktop service changes key profile by focused app. *[claimed]*
- AI-generated profiles — OpenAI API proposes constrained control profiles for unsupported apps. *[claimed]*

**Flow:** Extension or desktop app detects context → Python service decides key set → Arduino updates OLEDs → User presses key to run action

**Prompt:** Finalists main award: no first/second/third place; top projects become finalists; prize undisclosed (a surprise).
**Fit (none):** No sponsor prize stated; OpenAI used for profiles.  *(targeted: Hack the North 2026: Finalists)*
**Sponsor tools:** OpenAI API (Generate control profiles for unsupported apps, supporting)
**AI:** OpenAI API produces constrained JSON-like control profiles and action suggestions; main logic is rule-based on VS Code state.
**Architecture:** Keyboard firmware (C++) <-USB serial-> Python bridge service <- VS Code extension and window detector; OpenAI fallback; SolidWorks-designed 3D-printed case.
**Novelty:** Custom hardware keyboard with a display under every keycap that reacts to editor state, not just app focus.
**Scope:** medium · working: Page says working hardware; repo about 7.7k LOC with firmware, companion, extension, demo dirs and tests; no video. · polish: README mirrors Devpost; CAD and animations folders; 'Depreciated' folder.
**Claims:** Actually exists as working hardware, not a mockup
**Gaps:** Number of keys not stated; No video
Sources: https://devpost.com/software/keymaeleon, https://github.com/macto2024/Keymealeon (evidence file)

---

### Orbis Engine
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2026: Finalists; Winner OpenAI: API Prizes

**What it is:** A pipeline that turns an ordinary video clip into a walkable 4D scene: camera poses are estimated, people removed, a Gaussian-splat room generated with World Labs Marble, and people rebuilt as animated avatars; viewers walk through in a browser or Quest and talk to characters.
**Problem / user:** Viewers of films, phone clips or sports who want to experience a recorded moment in first person, including VR headset owners.

**Features**
- Video to 3D room — Pi3X poses, LaMa inpaints people out, Marble generates splat room, gsplat optionally fits to frames. *[shown_working]*
- People as avatars — LHM rebuilds tracked people, driven by their motion, scale and floor fitted to original positions. *[shown_working]*
- WebXR/browser viewer — Three.js and Spark splats, WASD walking or Quest eye-height walk, spectator view. *[shown_working]*
- Talk to characters and pick up objects — OpenAI Realtime voice conversation and physical objects such as a bottle. *[claimed]*
- Quality gate and cost ledger — GPT checks room renders; ledger prevents double billing of GPU calls. *[claimed]*
- Admin trace view — Graph and list traces to find bottlenecks. *[claimed]*

**Flow:** Provide 5-15 s single-shot clip → Pipeline runs on Modal GPUs → Check cleaned frames → Open scene in browser or Quest → Walk, talk, pick up objects

**Prompt:** OpenAI API Prizes: use OpenAI API ambitiously with Codex as teammate; judged on creative API use and Codex's help; demo shows product, API use, one Codex benefit.
**Fit (implied):** Uses OpenAI GPT vision for scale, prompts and quality gate, plus Realtime voice; Codex ran long GPU jobs. README says 2nd in OpenAI track.  *(targeted: OpenAI: API Prizes, Hack the North 2026: Finalists)*
**Sponsor tools:** OpenAI API (GPT, Realtime) (Scale/object detection, quality gate, scene prompts, voice talk, core); Codex (Ran long GPU jobs on cloud machines, supporting); World Labs Marble (Room generation, core)
**AI:** Chain of vision models (Pi3X, LaMa, Mask R-CNN, LHM, Gaussian splatting) with Marble room generation; GPT vision for prompts and gating; Realtime API for talking to characters.
**Architecture:** Python GPU pipeline on Modal/AWS with S3 scene storage -> Three.js/Spark/WebXR viewer in Bun; admin trace UI.
**Novelty:** Documents failed approaches (view-synthesis models) and a measured finding about 41-degree camera coverage; combines room generation, avatars and voice in one VR viewer.
**Scope:** large · working: README gives run commands, per-clip cost and time (about 25 min, $0.15 GPU); scenes not shipped publicly; no demo link on page. · polish: Detailed README, trace admin, landing page described.
**Claims:** Forward camera only sees about 41 degrees each side (measured) | 10 s clip takes about 25 min, about $0.15 Modal GPU plus 1,600 Marble credits
**Gaps:** Queue github_url and evidence file point to third-party Depth-Anything-3, not the project repo; used dtpu/OrbisEngine; README says Mask R-CNN and 2nd in OpenAI track; Devpost lists Depth Anything 3 as dropped; No video
Sources: https://devpost.com/software/temp-jcyltx, https://raw.githubusercontent.com/dtpu/OrbisEngine/HEAD/README.md, https://hackthenorth2026.devpost.com/

---

### punching-face
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2026: Finalists; Winner Sentry: Best Use of Sentry

**What it is:** A local web app that turns a webcam or uploaded video of a person's head into a textured 3D face, then lets players punch it using hand tracking while a soft-tissue physics sim deforms it. Phones can join over LiveKit to spar.
**Problem / user:** Hackathon attendees wanted to punch a teammate without hurting anyone; framed as a playful, stress-release toy using a scanned face.

**Features**
- Head scan from webcam, video or images — Extracts up to 220 frames, masks the head locally with MediaPipe, and requires 24 overlapping views before building; refuses to call front-only scans 360 degrees. *[shown_working]*
- Local photo-to-3D face reconstruction — COLMAP recovers cameras, landmarks are triangulated, a MakeHuman template is warped to fit, subdivided, hair-fitted and texture-baked from photos. *[shown_working]*
- AI completion of unseen head areas — Cropped views go to an OpenAI model that returns bounded shape, hair and eyeglass parameters executed by the local mesh builder. *[claimed]*
- Alternative Meshy cloud reconstruction — Sends the four most informative cropped views to Meshy multi-image-to-3D and imports the GLB; scans can hold both engines' models. *[claimed]*
- Punching with soft-tissue physics — MediaPipe tracks the fist at about 30 Hz; a CPU tetrahedral finite-element solve (Newton/Warp) deforms skin, tissue and support layers, plus an impact rig for cheeks, mouth, jaw, eyelids. *[shown_working]*
- Voice coach — A multimodal Qwen3.5-Omni model over a realtime relay comments on hits aloud; page says it declines to encourage hitting a person. *[claimed]*
- Multi-phone Arena — Host publishes the head into a LiveKit room; visitors scan a QR code and punch from phones, hand tracking on-device, per-person scoring. *[claimed]*
- End-to-end Sentry observability — One trace from browser click through HTTP handler to pipeline subprocess stages, gen_ai spans per model call, profiling, and Session Replay that blocks media. *[claimed]*

**Flow:** Record a 360 degree head video or upload one → Create 3D face (local pipeline or Meshy) → Optional AI completion of hair, back of head, glasses → Hold a fist at the webcam to punch and watch the face deform → Use debug controls to hold peak deformation or slow playback → Publish head to Arena; others scan QR and punch from phones → Export GLB or save editable session

**Prompt:** Sentry Best Use of Sentry: build with Sentry and use at least two products beyond plain error monitoring, such as Session Replay, Logs or Tracing. Finalists is the main award with no ranked places.
**Fit (explicit):** README/page describe Sentry tracing across browser, server and subprocess stages, structured logs with trace IDs, gen_ai spans, profiling and Session Replay with media blocked, covering several products beyond error monitoring.  *(targeted: Sentry: Best Use of Sentry)*
**Sponsor tools:** Sentry (Tracing from browser to pipeline stages, logs with trace IDs, gen_ai spans for model calls, profiling, Session Replay, core); OpenAI API (Back-of-head, hair and eyeglass completion from cropped views, supporting); Huawei OMNI (Qwen3.5-Omni) (Realtime voice sparring coach via relay, supporting)
**AI:** A vision-language OpenAI model infers bounded head-shape, hair and glasses parameters from crops; Qwen3.5-Omni gives realtime voice commentary; Meshy offers cloud image-to-3D. Measured geometry always takes precedence over AI priors.
**Architecture:** Browser (Three.js, MediaPipe, React/Vite) plus separate Python services: capture/reconstruction server, Newton physics server at 30 Hz, sponsor/LiveKit token server and OMNI relay, all on loopback with keys held server-side.
**Novelty:** Unusually deep physical pipeline for a joke premise: real FEM soft-tissue simulation, COLMAP reconstruction, honest coverage gates, and abandoned Gaussian splatting in favour of template fitting.
**Scope:** large · working: README gives full run instructions and tested pipeline; claims contact-to-reaction under 50 ms and 2.5x faster pipeline; no demo video linked. · polish: 352 files, about 56k LOC, JS and Python tests, formatting tooling, detailed docs; two screenshots on Devpost.
**Claims:** Contact to physical reaction under 50 ms | Accelerated pipeline 122 s vs 309 s serial, identical output | 55 JavaScript tests plus Python suites | Real Newton 1.6/Warp 1.17 tetrahedral FEM, no fake fallback solver
**Gaps:** no demo video; README first 7000 chars only; Sentry use not verified in code
Sources: https://devpost.com/software/punchface, https://github.com/akashngb/punching-face, https://hackthenorth2026.devpost.com/

---

### Reflex
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2026: Finalists

**What it is:** A wearable 3D-printed gauntlet with five servo-driven fingers that Claude can command over MCP, that mirrors a human hand via webcam, and that can replay learned motions from a fine-tuned SmolVLA policy. A web console shows a live 3D digital twin.
**Problem / user:** Physical skills are taught hand-over-hand, which does not scale; aimed at motor relearning (stroke, Parkinson's), skill learners such as piano, and repetitive-task workers.

**Features**
- Claude-controlled finger movement — An MCP server lets Claude read finger positions, command poses and write, run or edit named movement sequences stored as Python files. *[shown_working]*
- Hand mirroring teleoperation — MediaPipe tracks a controller's hand through a webcam and, after calibration, maps it to five normalized finger commands. *[shown_working]*
- Demonstration recording and replay — Episodes recorded from the console; LeRobot integration links them to SmolVLA training and inference. *[shown_working]*
- Learned grasp via fine-tuned SmolVLA — About 50 good episodes from nearly 100 attempts fine-tune the action head; glove autonomously grabs a can; threshold fallback if inference fails. *[shown_working]*
- Live digital twin console — Three.js URDF view of commanded versus measured joints, IMU orientation, RGB/depth feeds and per-finger telemetry, with preset gestures. *[shown_working]*
- Hardware abstraction layer — ROS 2 HAL applies motion limits so the same commands drive Gazebo simulation or real Feetech servos. *[shown_working]*
- Piano copilot — Qwen Omni combines voice, camera and movement proposals; Claude runs finger routines to guide a beginner through a tune. *[claimed]*
- Backdrivable hand-guide mode — Weak-spring PID using position error as force for hand-over-hand relearning; designed but not finished. *[planned]*

**Flow:** Type a gesture request to Claude; the glove moves → Wear the glove or have a controller mirrored by webcam; motion is logged → Record about 50 demonstrations → Fine-tune SmolVLA on the data → Glove replays the grasp autonomously → Watch commanded vs measured state on the web console

**Prompt:** Finalists is the main award with no ranked places; top projects become finalists. The page lists no sponsor prize target.
**Fit (none):** No stated link to any prize; the main award has no specific prompt. Hardware plus Claude MCP control and a learned policy is a substantial robotics build.  *(targeted: Hack the North 2026: Finalists)*
**Sponsor tools:** Anthropic Claude (MCP) (Natural-language control of glove over the same command path as console, core); Huawei OMNI (Qwen Omni) (Piano copilot multimodal loop, supporting)
**AI:** Claude issues pose commands through MCP; SmolVLA vision-language-action policy fine-tuned on ~50 teleop episodes via LeRobot; Qwen Omni handles voice/vision piano coaching; MediaPipe hand tracking.
**Architecture:** Next.js console and Claude MCP talk to a FastAPI backend, which uses rosbridge to a ROS 2 hand HAL driving ros2_control/Gazebo or a USB bus adapter to Feetech servos; LeRobot policy plugs into rosbridge.
**Novelty:** Full custom hardware (servos, RCM linkages, depth camera, IMU) with LLM control, teleop dataset and a VLA fine-tune all in 36 hours; framed as AI writing skills for humans.
**Scope:** large · working: Live Claude-driven hardware and an autonomous learned grasp reported; no video linked, no quantitative success rates; team states dataset proves a narrow claim. · polish: Repo of 277 files with tests and Docker, structured README with architecture diagram and movements library; no CI.
**Claims:** Fine-tuned SmolVLA on 50 episodes from nearly 100 attempts | Glove autonomously grabs a Red Bull after training | Same HAL drives simulated and real hand
**Gaps:** no demo video; README links a different repo name (Reflex) than the queue repo; setup instructions not seen in truncated README
Sources: https://devpost.com/software/reflex-e0jkih, https://github.com/ZechariahWang/htn-2026

---

### Settlers of Solana
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2026: Finalists; Winner Solana: Best Use of Solana and Badge Hack

**What it is:** A simulated village of 100 LLM agents that fish, chop wood, craft, build houses, trade and borrow, with all cash, goods, order books and a lending bank settled in an Anchor program on Solana. A 3D island dashboard shows the economy live.
**Problem / user:** Agent-to-agent economic behavior is hard to study and verify; LLM agents can explain choices and adapt unlike RL agents, and on-chain settlement makes the record unforgeable. Aimed at researchers and agent-market observers.

**Features**
- LLM villager swarm — Each of 100 agents has its own personality, talents and risk tolerance; all choose work or rest simultaneously each round via eleven OpenAI-format tools. *[shown_working]*
- On-chain batch auctions — Backend sorts order books; the Anchor program verifies and clears up to 100 orders per atomic transaction, purse to purse. *[claimed]*
- Credit by minting — Agents pledge wood, nets or half-built houses; borrow mints SPL coins, repay burns them, missed loans lead to foreclosure by any caller. *[claimed]*
- Self-governed SETTLERS token — SPL token whose mint and freeze authority is the program itself; every transaction asserts supply equals the sum of purses. *[claimed]*
- Multi-model comparison on Baseten — Four models via Baseten's OpenAI-compatible APIs run at once; each villager keeps one model for life and they trade against each other. *[claimed]*
- Live dials — 55 configuration dials, 35 adjustable live, such as forest fires, poisoned fish and market manipulation, read by agents from config. *[claimed]*
- Economy dashboard and 3D island — Three.js island with agents and trade links plus GDP, inflation, employment, wellbeing, inequality, credit and loan feed. *[shown_working]*
- Free stub agent — A rule-based agent runs the whole simulation without an API key. *[claimed]*

**Flow:** Open the 3D island and watch agents work and trade → Check the dashboard for GDP, wellbeing and other indicators → Move a live dial such as a forest fire → Watch prices shift and loans or foreclosures appear in the feed → Inspect the on-chain record of each round

**Prompt:** Solana Best Use of Solana (combined with Badge Hack, two winners): show an interesting use case, clever application or creative way to use the Solana ecosystem; prize $5,000 and a Ledger.
**Fit (explicit):** Core ledger, auctions, lending and token mint/burn live in a custom Anchor program with a real SPL token, so Solana is the settlement layer rather than a bolt-on; page lists Solana winner badge.  *(targeted: Solana: Best Use of Solana, Baseten: Best Use of Baseten (implied, Baseten used))*
**Sponsor tools:** Solana (Anchor, SPL Token) (Ledger, order-book auctions, borrow/repay mint and burn, foreclosure, core); Baseten Model APIs (Run four models side by side as villagers, supporting); OpenAI API / Codex (Agent model calls and development assistance, supporting)
**AI:** Each villager is an LLM using tool calls over up to three turns per round with an 8 s timeout; models include OpenAI and Anthropic ones plus four on Baseten; agents see order-book depth and loan math in prompts.
**Architecture:** Node.js backend runs the round clock and model calls and hand-encodes Solana instructions; a single zero-copy Anchor Ledger account (137 agent ceiling) holds state; React/Vite/Three.js front end reads it.
**Novelty:** Separates policy off-chain from settlement on-chain so the backend cannot mint coins or prevent foreclosure; money exists only through lending; includes candid findings on agent price-discovery failures.
**Scope:** medium · working: Reports 30-agent dev runs (3,059 calls, $1.33); no video or live link; no tests in repo. · polish: 68 files, about 10k LOC, detailed README with instruction table; Docker present; no CI or tests.
**Claims:** 30-agent run: 3,059 model calls, $1.33, six minutes | 79% of turns ended before posting an order until a follow-up turn fixed it | Projection of about $20 for 1,000 agents over 50 rounds (estimate) | 100-order auctions in one atomic transaction
**Gaps:** no video or live demo; setup steps not seen in truncated README; on-chain claims not verified in code
Sources: https://devpost.com/software/_solanasim, https://github.com/leakyhose/agent-economy, https://hackthenorth2026.devpost.com/

---

### TakeOne
*Hack the North Hack the North 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2026: Finalists

**What it is:** A robotic film-making rig: a reinforced RC truck carrying a camera arm and a light arm, driven by software that plans shots with an AI director, rehearses them in a 3D browser simulator, plays them back on the robot, tracks performers and edits footage.
**Problem / user:** AI can describe a shot instantly but filming it needs gear and crew; aimed at solo creators and small teams without large crews.

**Features**
- AI Director — OpenAI Responses API turns an idea into a brief, script, shot list, framing, camera, lighting and performance cues; live conversation via GPT-Live function calls. *[claimed]*
- Shot Studio simulator — Three.js and MuJoCo-based browser rehearsal of 39 movement presets and drawn paths against calibrated arm ranges before approval. *[shown_working]*
- Supervised physical playback — Only explicit operator commands move the cart and two SO-101 arms; simulator never opens a serial port. *[shown_working]*
- Live person tracking — OpenCV and MediaPipe body or face landmarks with PID keep the performer framed, by cart or arm, with watchdog timeouts. *[shown_working]*
- Record surface — Witness monitor beside planned frame, framing gate, takes and review; Blackmagic Camera on iPhone for lens cues and USB clip transfer. *[shown_working]*
- Built-in editor — Timeline editor with trimming, pacing, transitions, effects and FFmpeg export, plus AI editing proposals. *[claimed]*
- Voice control for filming — Start voice control on the Record page for filming commands. *[claimed]*
- Hardware diagnostics pages — Motor Lab with per-joint sliders and raw counts, and a Motion Proof page with generated cart movement evidence. *[shown_working]*

**Flow:** Describe the creative vision to the Director → Review script and shot proposals → Rehearse and tune shots in the 3D simulator → Approve shots for filming → Cart and arms execute, optionally tracking the performer → Review takes in Record → Arrange and export in the editor

**Prompt:** Finalists is the main award with no ranked places; top projects become finalists. The page names no sponsor prize target (a Bracket Bot Best Hardware Use track existed but is not claimed).
**Fit (none):** No stated link to any prize; main award has no specific prompt.  *(targeted: Hack the North 2026: Finalists)*
**Sponsor tools:** OpenAI API (Responses, GPT-Live) (Scripts, shot plans, editing proposals and conversational direction, core)
**AI:** OpenAI Responses API produces structured scripts, shot plans and edit proposals; GPT-Live gives constrained function-call conversation; classical vision (MediaPipe, PID) handles performer tracking.
**Architecture:** Local Python server compiles and validates movement plans (MuJoCo kinematics) for a Three.js simulator; ESP32 over USB serial and CAN motor controllers drive cart and arms; separate React editor process uses FFmpeg.
**Novelty:** Combines custom mobile hardware, safety-gated robot playback, simulation, tracking and a full editor in one pipeline; software explicitly refuses to claim hardware readiness without human qualification.
**Scope:** large · working: Hardware rig described with test notes (no brownouts, minimal UART drops); no video or live link; repo includes tests. · polish: 5,046 files and about 362k LOC (likely includes data), many documented routes and docs; Docker present.
**Claims:** 39 configurable movement presets | Zero observed brownouts and minimal UART packet drops in testing | Everything runs locally except generative AI calls
**Gaps:** no video or live demo; loc estimate may include generated or data files; README truncated
Sources: https://devpost.com/software/takeone-erqv3l, https://github.com/3-rt/TakeOne

---

