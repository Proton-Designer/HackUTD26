# TreeHacks — TreeHacks 2026 (9 projects)

### ChromaChord
*TreeHacks TreeHacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Winner Treehacks Grand Prize (3rd) [3rd]; Winner [Suno] Best Musical Hack

**What it is:** Real-time jazz improvisation helper: plays notes from a MIDI keyboard or guitar become chroma vectors, a graph harmonic model suggests next chords and visualizes harmony, Perplexity finds songs with similar progressions, and Claude generates harmony and backing tracks.
**Problem / user:** Jazz learners and improvisers who want interpretable chord guidance rather than LLM-only suggestions.

**Features**
- Live chord detection and suggestions — MIDI input to chroma vectors, deterministic chord/key analysis, WebSocket UI *[shown_working]*
- Harmonic graph visualization — Graph of chord transitions and overtone relations updated in real time *[claimed]*
- Dissonance ranking — Ranks about 4,000 chords by physics-based dissonance *[claimed]*
- Similar-song retrieval — Perplexity Sonar finds popular songs with similar progressions *[claimed]*
- AI harmony, melody and backing tracks — Claude / Agent SDK generates material from played progression *[claimed]*

**Flow:** Play MIDI keyboard or guitar → Notes become chroma vectors → App suggests next chords and shows graph → Perplexity surfaces similar songs → AI generates harmony, melody, backing track

**Prompt:** Suno Best Musical Hack: prize is interview and Suno subscription; no criteria beyond name. Grand Prize 3rd: iPhone per member.
**Fit (implied):** Music tool combining deterministic harmony theory with AI generation; no Suno API use described.  *(targeted: TreeHacks Grand Prize (3rd), Suno: Best Musical Hack)*
**Sponsor tools:** Perplexity Sonar (song retrieval by progression, supporting); Claude Agent SDK (harmony and melody generation, supporting)
**AI:** Deterministic signal and graph harmony analysis locally; Perplexity for retrieval; Claude for generation, kept separate for responsiveness.
**Architecture:** FastAPI WebSocket backend captures MIDI and runs chord graph; Next.js frontend visualizes; external AI calls for songs and generation.
**Novelty:** Interpretable graph-based harmony engine grounded in music-theory papers, with AI layered on top.
**Scope:** small · working: README gives run steps for backend and frontend; no demo or video; 7k LOC estimate. · polish: No tests or deploy link beyond Vercel mention.
**Claims:** Ranks all about 4,000 octave chords by dissonance (no metrics)
**Gaps:** No demo; Generation and backing track maybe not in README
Sources: https://devpost.com/software/chromachord, https://github.com/J4Joshua/JASS-APP (evidence file), https://treehacks-2026.devpost.com/

---

### diffuji
*TreeHacks TreeHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Most Creative; [Neo] Most Likely to Become a Product

**What it is:** Handheld instant camera built on a Raspberry Pi that takes a photo, restyles it with image-diffusion models, dithers it and prints it on a thermal sticker; also has a price-check mode that prints web-searched prices for photographed objects.
**Problem / user:** Playful consumer toy; no formal problem stated. Price-check mode targets thrift shoppers or resellers.

**Features**
- AI photo filters — Scene to 1846, muscle mode, ducks, Ghibli, Sam mode via Gemini, gpt-image-1.5, FLUX *[shown_working]*
- Thermal sticker printing — Ordered Bayer dithering with gamma and contrast tuning *[shown_working]*
- Price check mode — Perplexity search prints reference-backed price *[claimed]*
- Physical UI — Rotary encoder, shutter, OLED mode display *[shown_working]*
- Cloud API — Railway server reports modes and processes images *[shown_working]*

**Flow:** Power on → Pick mode on OLED → Press shutter → Image processed on device or cloud → Dithered print emerges

**Prompt:** Most Creative: projects that make judges say wow. Neo Most Likely to Become a Product: retreat travel and mentors, no criteria.
**Fit (implied):** Novel physical device with fun AI filters and compact battery shell; pitched as possibly mass-produced.  *(targeted: Most Creative, Neo: Most Likely to Become a Product)*
**AI:** Image-edit models (Gemini 2.5 Flash Image, gpt-image-1.5, FLUX Kontext on Modal H100) restyle photos; Perplexity search for prices.
**Architecture:** Pi Zero 2W with camera, printer, OLED runs Python; Railway API proxies to model providers; results dithered and printed.
**Novelty:** Generative-AI instant camera with a custom 3D-printed shell and inkless printing.
**Scope:** small · working: Photos of printed results; demo site; repo about 2k LOC. · polish: Custom Fusion 360 shell, battery UPS, soldered build.
**Gaps:** No video; On-device diffusion too slow
Sources: https://devpost.com/software/diffuji, http://github.com/alexkranias/dispo (evidence file), https://treehacks-2026.devpost.com/

---

### Freak in the Sheets
*TreeHacks TreeHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Most Technically Complex; Winner [Human Capital] Human Capital Fellowship Prize ($50k equity-free per team member, up to $200k)

**What it is:** A compiler backend that lets C or Rust programs run inside Google Sheets: a custom instruction set and 2D memory layout compile to a spreadsheet-formula interpreter stepped by iterative calculation.
**Problem / user:** No problem statement; a systems stunt aimed at compiler and low-level programmers.

**Features**
- LLVM backend targeting Sheets — clang --target=google-sheets emits custom ISA *[claimed]*
- Formula bytecode interpreter — Interpreter built from spreadsheet formulas runs compiled code *[shown_working]*
- Unattended execution — Iterative calculation steps the VM; claimed backend validation exploit keeps it running *[claimed]*
- Dense memory encoding — 16,666 32-bit ints per cell via Unicode packing *[claimed]*
- Two-pass assembler — Assembles code into sheet memory *[claimed]*

**Flow:** Compile with clang for google-sheets → Open linked Sheet → Program runs in real time in cells

**Prompt:** Most Technically Complex: judges hope to see beautiful code or hardware under the hood. Human Capital Fellowship: $50k per member for exceptional engineers.
**Fit (implied):** Low-level compiler engineering project creating a new ISA and LLVM target.  *(targeted: Most Technically Complex, Human Capital Fellowship Prize)*
**AI:** none
**Architecture:** Clang/LLVM fork with new backend produces assembly; assembler packs it into sheet cells; formula-based VM advances by iterative calculation.
**Novelty:** Runs compiled arbitrary-language code inside a spreadsheet via a new ISA and encoding.
**Scope:** medium · working: Public Sheets demo link; this repo holds about 10% of work (rest in LLVM fork). · polish: Clear README; no video.
**Claims:** Packs 16,666 integers per cell vs 1 | Runs indefinitely via unpatched Sheets validation exploit
**Gaps:** LLVM fork not inspected; No timings
Sources: https://devpost.com/software/freak-in-the-sheets-7jl542, https://github.com/kognise/freak-in-the-sheets (evidence file), https://treehacks-2026.devpost.com/

---

### HeartStart
*TreeHacks TreeHacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Winner Best Beginner Hack

**What it is:** A home robot prototype that watches a wearable heart-rate sensor, phones for help through Twilio when the signal flatlines for 15 seconds, drives to the patient using camera tracking and an AprilTag on the chest, and runs a 3D-printed CPR compression mechanism.
**Problem / user:** People at risk of out-of-hospital cardiac arrest and their families, where bystanders may not know CPR and EMS can take over seven minutes.

**Features**
- Heart-rate monitoring and flatline detection — BLE wearable sensor feeds an Arduino, then serial to a Python (PySerial) backend that triggers after 15 seconds of flatline. *[claimed]*
- Automated emergency call — Twilio places a call with a scripted cardiac-arrest message; in the demo it went to a friend's phone, not 911. *[claimed]*
- Autonomous approach to patient — ROS2 nodes on a Raspberry Pi use single-camera body tracking; speed scales with log of bounding-box area ratio. *[claimed]*
- AprilTag fine positioning over the sternum — Once the chest tag is visible the robot aligns and stops above it. *[claimed]*
- CPR compression mechanism — 3D-printed PLA cranker shaft converts rotary motor motion to linear compressions. *[claimed]*
- Responder dashboard — Web page shows live heart rate, IR signal and patient history, with a Blender 3D heart that pulses per beat. *[claimed]*

**Flow:** Patient wears heart-rate sensor → Backend watches signal for flatline → After 15 s a Twilio call goes out → Laptop commands the Pi on the robot → Robot tracks and approaches, then aligns on AprilTag → CPR mechanism starts → Dashboard shows vitals to responders

**Prompt:** not public / not found
**Fit (none):** Beginner-track entry: a multi-part hardware and software system built by a team new to robotics; the page does not state the prize criteria or claim a prize target.  *(targeted: Winner Best Beginner Hack)*
**Sponsor tools:** Twilio (Automated emergency phone call on flatline, supporting)
**AI:** No trained model named; body tracking uses computer vision with bounding-box projection and AprilTag detection.
**Architecture:** Wearable sensor to Arduino to laptop (Python backend, dashboard, Twilio) to Raspberry Pi on a mobile base running ROS2 vision and motor nodes, plus a CPR mechanism.
**Novelty:** End-to-end chain from vitals to a mobile robot that performs compressions, using only one camera for approach and fine positioning.
**Scope:** medium · working: Page claims working sensor, Twilio, navigation and dashboard pipelines; no demo video; repo about 2.3k LOC with motor, servo and pump test folders. · polish: Repo has no README; two screenshots; no performance measurements.
**Claims:** Flatline of 15 seconds triggers an automated call | Approach speed scales with log of bounding-box area ratio
**Gaps:** Repo has no README, only directory tree read; No official Beginner Hack prize text; No video; No tested CPR depth or rate data
Sources: https://devpost.com/software/heartstart, evidence/treehacks-treehacks-2026-heartstart.json

---

### Mira
*TreeHacks TreeHacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Most Impactful; Winner [OpenAI] Artificial Intelligence Track

**What it is:** Voice assistant on Ray-Ban Meta glasses for dementia patients: it finds lost objects in a 3D reconstruction of the home built from phone video, answers medication questions with sourced evidence grades, reports falls, and updates a live caregiver dashboard.
**Problem / user:** Dementia patients who lose items and repeat questions, and family caregivers who cannot be present around the clock.

**Features**
- 3D object localization — Point cloud with detected object graph plus live pose tracking; viewer flies to object *[shown_working]*
- Medication Q&A — Agent queries de-identified FHIR data, Perplexity and OpenEvidence with evidence-graded citations *[claimed]*
- Fall reporting and escalation — Voice triggers email alert via Twilio with context *[claimed]*
- Caregiver dashboard — Realtime health summaries and event timeline on Supabase *[claimed]*
- Audit log — Immutable timestamped record of questions and tool calls *[claimed]*
- De-identification — Age ranges and conditions only before LLM sees records *[claimed]*

**Flow:** Home walkthrough video reconstructed to 3D map → Patient asks by voice through glasses → Agent calls spatial, patient or medication tool → Mira answers and moves 3D viewer → Emergencies email caregiver, events log

**Prompt:** Most Impactful: hacks that will impact future generations on pressing concerns. OpenAI AI Track: three prizes (interview, ChatGPT Pro, backpacks); no track-specific criteria.
**Fit (implied):** Healthcare assistive application using LLM agent with tool calls and multimodal 3D perception.  *(targeted: Most Impactful, OpenAI Artificial Intelligence Track)*
**Sponsor tools:** OpenAI (gpt-5-mini, Whisper, TTS) (agent reasoning and voice, supporting); Perplexity Sonar (medication evidence lookup, supporting)
**AI:** LLM tool-calling agent via OpenRouter; Whisper/OpenAI TTS; Grounding DINO, SfM, DPVO, HLoc for 3D mapping and pose; evidence grading for medication answers.
**Architecture:** Glasses stream via Android phone and RTMP/WebRTC to laptop; Modal GPUs build maps; FastAPI agent; Supabase realtime dashboard.
**Novelty:** Combines wearable video, 3D scene reconstruction and live pose tracking for object finding.
**Scope:** large · working: Claims under ten seconds end-to-end; repo 27k LOC estimate with Docker. · polish: Heavy ML pipeline; no demo video.
**Claims:** Voice-to-3D object localization in under ten seconds
**Gaps:** No video; Latency self-reported
Sources: https://devpost.com/software/mira-w65b0a, https://github.com/nathanjzhao/treehacks2026 (evidence file), https://treehacks-2026.devpost.com/

---

### Robosurge
*TreeHacks TreeHacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Treehacks Grand Prize (2nd) [2nd]

**What it is:** A four-arm robotic surgery demo station where a surgeon wearing a Quest 3 headset moves a physical camera arm by head tracking and issues natural-language commands that LLMs turn into arm motions. Includes a custom kinematics stack and Lean proofs that trajectories stay in safe bounds.
**Problem / user:** Surgeons facing OR cost and specialist shortages; current surgical robots add precision but not automation because AI spatial vision and AI-to-robot control are weak.

**Features**
- Natural-language arm control — LLMs (GPT-5.2 plus Gemini Robotics-ER 1.5) interpret camera views and commands and orchestrate moves of four magnetically driven arms *[claimed]*
- Quest 3 head-tracked camera — VR headset head pose drives a physical camera arm in real time *[claimed]*
- Depth-based coordinate mapping — RealSense depth plus ArUco tags and an affine transform align camera and robot frames for all four arms *[claimed]*
- Object segmentation — SAM and YOLOv11 on edge hardware and an ASUS GX10 identify targets *[claimed]*
- Custom inverse kinematics — Own IK solver replaces vendor SDK, claimed faster and with safety guarantees *[claimed]*
- Lean-verified trajectories — Lean 4 proofs that lemniscate, wave, spring and helix paths remain within physical bounds; custom RK4 solver *[claimed]*
- Web control panel and streaming — FastAPI server with WebSocket/REST, MJPEG and WebRTC video, TanStack frontend *[claimed]*

**Flow:** Surgeon puts on Quest 3 synced to camera arm → Head movement steers the camera view → Surgeon gives a natural-language command → LLMs interpret the scene and plan moves → Custom IK drives the four arms → Operator monitors via web panel

**Prompt:** Treehacks Grand Prize; page lists only general judging: creativity, technical complexity, social impact. No track-specific challenge text.
**Fit (implied):** Writeup does not name a prize; hardware-plus-AI-plus-formal-verification scope maps to the general technical-complexity criterion.  *(targeted: Treehacks Grand Prize)*
**Sponsor tools:** ASUS Ascent GX10 (Edge compute for segmentation models, supporting)
**AI:** Two-level LLM fusion (GPT-5.2 and Gemini Robotics-ER 1.5) for scene understanding and move orchestration, SAM and YOLOv11 for segmentation, with grounding harnesses translating intent to robot actions.
**Architecture:** Python/FastAPI server talks to roarm arms and RealSense camera; agent module calls LLMs and vision models; web UI and Quest client connect over WebSocket/WebRTC; Lean project verifies trajectories; built with Nix.
**Novelty:** Combines agentic robot control with Lean formal verification of trajectory safety, unusual for a hackathon; hardware built by first-time robotics team in 36 hours.
**Scope:** large · working: Repo of about 14k LOC across agent, control, motion controller, VR and Lean dirs; no demo video listed. · polish: Three screenshots on Devpost; repo README is a single line.
**Claims:** Built in 36 hours by first-time hardware engineers | Likely one of the first extensive Lean uses at a hackathon of this scale | Custom IK faster than vendor SDK
**Gaps:** No demo video; No quantitative results
Sources: https://devpost.com/software/we-use-nix, https://github.com/quantum9Innovation/treehacks2026 (evidence file), https://treehacks-2026.devpost.com/

---

### Sentinel
*TreeHacks TreeHacks 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Winner Best Hardware Hack

**What it is:** A multi-agent system that takes a GitHub repo and a task, has parallel Claude-based workers write bare-metal ARM code, flashes and tests it on real Raspberry Pi Zero W boards, and uses an FPGA pin tracer for feedback. Its demo output is an OS written by the agents.
**Problem / user:** Embedded developers and teams who want AI agents to implement bare-metal features, where datasheets are scattered, there is no debugger or print output, and hardware hangs.

**Features**
- Orchestrator and research agents — Orchestrator forks the repo, splits work with non-overlapping file ownership, merges and opens a PR; a research agent searches datasheets and register maps. *[shown_working]*
- Parallel worker agents with build and test — Workers write code, build with arm-none-eabi-gcc and submit binaries to the Pi run queue. *[shown_working]*
- Pi server — Auto-detects Pis over USB serial, one worker per board, flashes over UART bootloader with CRC32 and returns output. *[shown_working]*
- FPGA pin tracer (pintrace6) — PYNQ-Z2 logic records 6 pin states with 10 ns timestamps into BRAM; HTTP API lets agents diff expected and actual traces. *[shown_working]*
- Live dashboard — Next.js UI submits jobs and streams orchestrator reasoning, edits, commands and Pi results, plus Pi cluster status. *[shown_working]*
- Structured event logging — 15+ event types written to JSONL for replay and debugging of agent decisions. *[claimed]*
- Sentinel OS generated by agents — Bare-metal GPIO, UART, SD and FAT32, MMU, interrupts, threads, Bluetooth keyboard, HDMI shell; about 16k lines of C. *[shown_working]*

**Flow:** Submit repo URL and task in dashboard → Orchestrator forks repo and plans work → Research agent finds datasheets → Workers write and build code → Pi server flashes binaries; FPGA traces pins → Orchestrator merges, pushes and opens a PR → Final demo: Pi boots the generated OS with a Bluetooth keyboard on a display

**Prompt:** not public / not found
**Fit (implied):** Hardware-heavy build: real Pi boards in the loop, custom Verilog FPGA debug core, UART bootloader. The page does not quote the prize text or name a target.  *(targeted: Winner Best Hardware Hack)*
**Sponsor tools:** Claude Agent SDK (Claude Opus 4.6) (Orchestrator, research and worker agents with file, bash and web-search tools, core); Fetch.ai Agentverse (Mentioned as a planned expansion route, token)
**AI:** Claude Opus 4.6 agents run as Agent SDK subprocesses with read, edit, bash and web-search tools; orchestrator holds full codebase context and hardware testing is mandatory in prompts.
**Architecture:** Next.js dashboard to FastAPI backend with SSE; agents build with arm-none-eabi-gcc; Pi server flashes Pi Zero W boards over UART; PYNQ-Z2 FPGA traces GPIO and exposes HTTP API back to agents.
**Novelty:** Closes the agent loop with physical hardware and a custom FPGA logic-analyzer-like core, rather than a software sandbox.
**Scope:** large · working: Page reports about 16k lines of C and 40+ test programs run on physical Pi Zero W boards, ending in an OS demo; no video listed. · polish: Three screenshots, detailed page and dashboard; repo not read (clone failed).
**Claims:** Wrote roughly 16,000 lines of bare-metal C in 24 hours | 40+ test programs validated on physical Pi Zero W devices | Task would take an experienced programmer weeks or months
**Gaps:** Evidence clone failed and raw README fetch failed; No official Best Hardware Hack prize text; No demo video; Figures are self-reported
Sources: https://devpost.com/software/sentinel-c8ki50

---

### Shepherd
*TreeHacks TreeHacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Treehacks Grand Prize (1st) [1st]; Winner [OpenEvidence] Healthcare Track Grand Prize; Winner [OpenEvidence] Best Use of Clinical Information (4x Apple Watches)

**What it is:** A low-cost open-source smart white cane: an iPhone on the handle senses obstacles with LiDAR and an ESP32-driven omni wheel physically nudges the user toward the clearest path. Also gives voice GPS pedestrian and wheelchair-accessible routing.
**Problem / user:** Blind and visually impaired pedestrians, including wheelchair users; existing smart canes cost around $800-1,150 and depend on slow cloud AI.

**Features**
- Physical steering — Motorized omni wheel at cane base pushes laterally toward free space, driven over BLE at 10 Hz *[shown_working]*
- Gap-seeking obstacle avoidance — iPhone LiDAR depth split into 16 columns; picks direction of max clearance with EMA smoothing *[claimed]*
- Haptic proximity feedback — Pulses speed up as obstacles approach *[claimed]*
- GPS and wheelchair routing — Google geocoding, OpenRouteService step-free profile, Overpass crosswalk data, micro-waypoints every 6 m *[claimed]*
- Voice assistant — Vapi conversational guidance with situational awareness *[claimed]*
- Person and terrain detection — Apple Vision people detection; HSV color analysis flags grass/mulch as virtual obstacle *[claimed]*
- Safety watchdogs — 500 ms iOS and 250 ms ESP32 timeouts zero the motor *[claimed]*
- Debug and tuning UI — In-app sliders, BLE pairing view, obstacle test tools *[claimed]*

**Flow:** Mount iPhone on cane handle → Give a destination by voice → App computes accessible route and speaks turns → LiDAR and camera detect obstacles while walking → Cane motor steers user to clear path with haptic pulses → Watchdogs stop motor if link drops

**Prompt:** OpenEvidence healthcare prizes: $4,000 plus interview for track grand prize; Apple Watches for best use of clinical information. No challenge text published. Grand Prize judged on creativity, technical complexity, social impact.
**Fit (implied):** Accessibility and assistive-health framing fits the healthcare track; neither README nor Devpost mentions OpenEvidence or clinical information.  *(targeted: Treehacks Grand Prize, OpenEvidence Healthcare Track, OpenEvidence Best Use of Clinical Information)*
**AI:** Mostly on-device perception: LiDAR depth heuristics and Apple Vision person detection, color-based terrain detection; Vapi for voice. CoreML/DeepLabV3 listed in tags without described use.
**Architecture:** iPhone (ARKit, Vision, GPS) computes steering command and sends 12-byte BLE packets to an ESP32-S3 running FreeRTOS that drives the motor; cloud APIs only for routing and voice.
**Novelty:** Builds on Stanford's Augmented Cane idea but adds on-device AI, routing, and open CAD/BOM; physical hardware with firmware and phone app.
**Scope:** large · working: Full README, hardware CAD, iOS app and firmware; photos of built cane referenced but demo video not yet posted. · polish: Detailed README with architecture, metrics, roadmap and build instructions.
**Claims:** Under 100 ms latency, 30-50x faster than cloud | About $50 to build, 1/20 of commercial canes | Sub-50 ms obstacle-to-motor pipeline | 4-6 hour battery
**Gaps:** Demo video not posted
Sources: https://devpost.com/software/raising-cane, https://github.com/tonywangs/shepherd (evidence file), https://treehacks-2026.devpost.com/

---

### VisionOS
*TreeHacks TreeHacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Winner [OpenAI] Artificial Intelligence Track

**What it is:** A voice-first agentic layer for blind users: speak requests and a multi-agent system drives the browser and desktop, searches the web and remembers preferences, shown through an Electron overlay.
**Problem / user:** Blind and visually impaired computer users stuck with linear screen readers and inaccessible sites.

**Features**
- Conversational voice interface — Speech in, spoken replies via Cartesia, user can interrupt and refine *[claimed]*
- Intent routing — GPT-4.1 mini classifier routes requests to scoped worker agents in a LangGraph supervisor *[claimed]*
- Browser agent — Stagehand uses vision and DOM parsing for multi-step web tasks *[claimed]*
- Desktop control — Agent-S controls apps such as Spotify and VSCode *[claimed]*
- Grounded web search — Perplexity Sonar for comparisons before acting *[claimed]*
- Persistent memory — Elasticsearch with Jina embeddings stores preferences, budget, allergies across sessions *[claimed]*
- Fetch.ai Agentverse agents — Directory includes uAgents integration *[claimed]*

**Flow:** User speaks a request → Router picks a specialist agent → Agent searches or browses and acts → System asks clarifying questions, e.g. allergies → User interrupts or resumes later with memory kept

**Prompt:** OpenAI Artificial Intelligence Track: prizes listed (office tour, ChatGPT Pro, interview); no challenge text. General criteria creativity, complexity, social impact.
**Fit (explicit):** Uses GPT-4.1 mini as conversational brain, STT and routing classifier for the multi-agent workflow.  *(targeted: OpenAI Artificial Intelligence Track)*
**Sponsor tools:** OpenAI GPT-4.1 mini (Central brain, speech-to-text, routing classification, core); Cartesia (Text-to-speech, supporting); Stagehand/Browserbase (Browser automation, supporting); Agent-S (Simular) (Desktop automation, supporting); Perplexity Sonar (Web search, supporting); Elasticsearch + Jina (Semantic memory, supporting); Fetch.ai Agentverse (Agent hosting (repo dir), unclear)
**AI:** LangGraph multi-agent supervisor with GPT-4.1 mini classification and worker agents; vision/DOM browser agent; embedding-based memory in Elasticsearch.
**Architecture:** Electron/React overlay talks via socket.io to a server that runs LangGraph agents calling OpenAI, Stagehand, Agent-S, Perplexity, and Elasticsearch memory; Cartesia speaks replies.
**Novelty:** Pitches an accessible OS layer rather than a screen reader plug-in; stitches many sponsor agent tools together.
**Scope:** medium · working: Repo of about 8.5k LOC with server, client, electron overlay; no demo or video listed. · polish: Liquid-glass Electron overlay; README is two lines.
**Claims:** Cites $7B yearly company loss from inaccessible tools (unsourced)
**Gaps:** No demo; Screenshot count unknown
Sources: https://devpost.com/software/visionos-5euxo7, https://github.com/ledaniel0/treehacks2026 (evidence file), https://treehacks-2026.devpost.com/

---

