# Hack the North — Hack the North 2025 (12 projects)

### ChessMate
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Winner Hack the North 2025: Finalists

**What it is:** A physical chessboard with a motorized 2D gantry and electromagnet that moves magnetized pieces. A webcam with computer vision tracks the human's moves, a chess engine replies, and the same game can be played remotely from a web app with voice control and AI coaching.
**Problem / user:** Families separated by distance who want to play real chess together, plus players with mobility or vision difficulties and people wanting practice coaching.

**Features**
- Motorized physical board — Two NEMA 17 steppers with DRV8825 drivers move an electromagnet gantry under the board, driven by an Arduino from Raspberry Pi 5 instructions. *[claimed]*
- Computer vision move detection — Webcam plus a vision model detects which piece moved on the physical board. *[claimed]*
- Engine and collision-free pathfinding — Chess engine picks the reply move; a pathfinding step plans a route for the piece avoiding others. *[claimed]*
- Remote play — A remote player's web-app moves physically move pieces on the board in real time. *[claimed]*
- Voice commands — Move pieces by voice for accessibility. *[claimed]*
- AI coaching agents — Agents integrated with the board and web app give instant guidance and practice help. *[claimed]*
- Built-in remote video — Camera so remote players can be seen and heard during play. *[planned]*

**Flow:** Start a game on the web app or physical board → Move is detected by camera or entered by app or voice → Engine decides the response → Pathfinding routes the gantry to move the magnetized piece → AI coach offers guidance

**Prompt:** Finalists track: official text only says these are the finalists of Hack the North 2025; no further criteria.
**Fit (none):** Finalists track states no requirements; no stated fit.  *(targeted: Hack the North 2025: Finalists)*
**Sponsor tools:** Groq (Listed in tags, likely LLM coaching; role not described, unclear)
**AI:** Computer vision model for piece detection, chess engine for moves, LLM agents (Groq listed) for coaching and voice control; details not described.
**Architecture:** Raspberry Pi 5 runs vision, engine and pathfinding, sends commands to an Arduino driving the stepper gantry and electromagnet; Next.js web app with agents connects remote players.
**Novelty:** Real moving pieces linked to remote players via a self-built gantry, combining hardware, vision and LLM coaching in one weekend.
**Scope:** medium · working: Team says gantry works flawlessly; photos of chessboard, wiring and cutting; no video or demo; repo about 5k LOC. · polish: Physical stand and board built; no README or metrics.
**Claims:** Gantry works flawlessly | AI agents merged with physical board and web app
**Gaps:** Repo has no README, so evidence adds only size; No video or demo; Groq role unspecified
Sources: https://devpost.com/software/chessmate-nwygvq, https://github.com/o-bm/ChessMate (evidence: no README text, 33 files), https://hackthenorth2025.devpost.com/ via prompts_cache

---

### Coach Bob!
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Hack the North 2025: Finalists

**What it is:** An AR boxing-style warm-up game: wearing XReal glasses, the user sees coloured targets on a punching bag, an IMU on the bag registers hits and force from wobble, and a Gemini/ElevenLabs persona 'Coach Bob' taunts and motivates. A dashboard shows speed, force and time afterwards.
**Problem / user:** Athletes, especially martial artists, who skip or rush warm-ups and risk injury; aims to make warm-ups engaging.

**Features**
- AR target overlay — OpenCV overlays coloured nodes on the bag in XReal glasses indicating kick, knee, hook, jab, or head/body strike. *[shown_working]*
- Hit and force detection — MPU-6050 IMU on the bag senses wobble after impact to register hits and estimate force. *[claimed]*
- Coach Bob voice — Gemini writes playful insults and ElevenLabs speaks them to motivate the user. *[claimed]*
- Pose-based game logic — Repo uses MediaPipe pose detection on an OAK-1 AF camera with dynamic hit zones, combo scoring, campaign boss battles and cutscenes. *[shown_working]*
- ESP32 health system — ESP32 can set and report in-game health via an API, relocating hit zones when health changes. *[claimed]*
- Performance dashboard — Shows speed, force and time after the session. *[claimed]*

**Flow:** Put on AR glasses and helmet → Coach Bob taunts to start → Coloured targets appear on bag → Strike the target; IMU registers hit and force → Review speed, force and time on dashboard

**Prompt:** Finalists track: official text only says these are the finalists of Hack the North 2025; no further criteria.
**Fit (none):** Finalists track states no requirements; no stated fit.  *(targeted: Hack the North 2025: Finalists)*
**Sponsor tools:** ElevenLabs (Coach Bob voice, supporting); Gemini (Coach Bob taunt text, supporting)
**AI:** MediaPipe pose detection on an OAK camera for hit zones in the repo; Gemini generates coach dialogue and ElevenLabs voices it; hit force is sensor-derived, not ML.
**Architecture:** Python and C++ game loop with OAK-1 AF camera and OpenCV overlay streamed to XReal glasses; MPU-6050 IMU and optional ESP32 supply hit and health signals; Gemini and ElevenLabs for voice.
**Novelty:** Improvised hit sensing from bag wobble plus AR glasses overlay on a real punching bag, with a comedic AI coach persona.
**Scope:** small · working: Working game described, repo has test scripts and music/cutscene handling; no video or live demo; about 2k LOC. · polish: Controls, campaign mode, boss battles and music in README; Devpost admits choppy streaming and late start.
**Claims:** Athletes reportedly enjoyed it | Smoother without live streaming
**Gaps:** README describes an OAK/MediaPipe boxing trainer while Devpost describes AR glasses plus IMU on a bag; features merge both, repo README follows an earlier or different build; No video
Sources: https://devpost.com/software/coach-bob, https://github.com/ultratrikx/oak_camera_project (evidence README), https://hackthenorth2025.devpost.com/ via prompts_cache

---

### DUM-E
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Winner Hack the North 2025: Finalists

**What it is:** A 5-degree-of-freedom robotic arm, named after the Iron Man workshop robot, that takes spoken or typed commands, looks at the desk through a webcam and has a multimodal LLM decide where to move to pick, sort or hold objects.
**Problem / user:** Hobbyist and workspace users who want a robot arm driven by natural language instead of fixed pre-programmed routines.

**Features**
- Voice and text commands — Whisper Large V3 transcribes speech; typed input also accepted and passed to the LLM. *[claimed]*
- Camera scene understanding — Webcam frame is warped to a bird's-eye view by homography, then a segmentation model draws bounding boxes with coordinates. *[claimed]*
- LLM-planned pick and place — Detections and image go to a Llama multimodal model on Groq, which chooses actions such as sorting parts or holding tools. *[claimed]*
- Inverse-kinematics arm control — Flask server on a Raspberry Pi relays to an Arduino Uno; 5-DOF IK converts targets into servo angles. *[claimed]*
- Position feedback loop — Real-time arm positions are returned to the LLM so later moves stay consistent. *[claimed]*
- Gesture expression — Arm can wave or show sentiment through gestures. *[claimed]*

**Flow:** Speak or type a command → Whisper transcribes → Webcam frame rectified and objects boxed → LLM picks actions from positions → Pi/Arduino turn IK output into servo moves → Arm position fed back to LLM

**Prompt:** Finalists track plus Groq sponsor prize ($500 swag-store credit for 4 winners); finalists text gives no criteria.
**Fit (implied):** Uses Groq-hosted multimodal Llama for the perception-to-action planning step; page does not state which prize it targets.  *(targeted: Hack the North 2025: Finalists, Groq)*
**Sponsor tools:** Groq API (Runs the multimodal LLM that decides arm actions, core)
**AI:** Multimodal Llama (about 109B) via Groq reasons over rectified camera frame plus detections; Whisper Large V3 for speech; segmentation and hand-joint vision models.
**Architecture:** Mic and webcam on PC (Python/OpenCV) -> Whisper + Groq LLM -> Flask server on Raspberry Pi -> Arduino Uno -> servos, with arm state looped back to the LLM.
**Novelty:** Full hardware stack (CAD parts, 9A multi-servo power, IK) combined with LLM planning from a homography top-down view; hobby arm driven by language rather than scripts.
**Scope:** medium · working: Repo of about 3.9k LOC with arm, camera, object detection, backend dirs; no demo video on page, README links only an inspiration video. · polish: Minimal README; Devpost has photos and CV screenshot, no measured results.
**Claims:** Low-latency, smooth multi-DOF movement (no numbers given) | Generalizes to new tasks without custom programming
**Gaps:** README holds only an inspiration video link; No demo video or measured results; Which prize it targeted not stated
Sources: https://devpost.com/software/dum-e-kgx6at, https://github.com/pekachoo/htn-DUM-E (evidence file), https://hackthenorth2025.devpost.com/

---

### Lattice
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2025: Finalists

**What it is:** A live volumetric capture system: three Kinect v2 sensors on separate laptops stream point clouds to a hub that aligns and merges them into one 3D scene, which a HoloLens app shows as a hologram.
**Problem / user:** Anyone wanting real-world people and objects inside AR/VR; page cites remote collaboration, medical training and live entertainment, with a goal of cheap hardware.

**Features**
- Multi-Kinect capture — C++ client per sensor turns color+depth into a bounded colored point cloud and sends it over TCP. *[shown_working]*
- Marker-based calibration — Printed marker found with OpenCV gives each sensor's pose into shared world space; pose cached on disk. *[shown_working]*
- ICP refinement — Hub calls a C++ ICP library to tighten alignment of every sensor onto the first connected one. *[shown_working]*
- Real-time fusion hub — C# server merges frames, renders them in an OpenGL viewport; devpost reports over 20 FPS (peak 23). *[shown_working]*
- Network rebroadcast — Merged cloud is sent on a second port so other viewers, such as the HoloLens Unity app, can subscribe. *[shown_working]*
- Kinect noise filter — Custom filter cleans sensor noise. *[claimed]*
- Replay viewer — Standalone C# viewer for saved captures. *[shown_working]*

**Flow:** Each Kinect connects to its own laptop running the client → Laptops join the same network as the hub → Calibrate with marker sheet; ICP refines → Hub merges streams → HoloLens user views the live hologram

**Prompt:** Finalists track: official text is only 'The finalists of Hack the North 2025!'; no further criteria published.
**Fit (none):** No sponsor prize stated; entered for the general finalist selection. README says it later won Best Overall and a YC Unicorn Prize demo slot.  *(targeted: Hack the North 2025: Finalists)*
**AI:** none
**Architecture:** Per-sensor C++ capture clients -> TCP binary protocol -> C# hub (merge, ICP via C++ lib, OpenGL view) -> second TCP port -> Unity HoloLens viewer (separate repo).
**Novelty:** Pure sensor-fusion and graphics engineering on discontinued hardware (Kinect v2, HoloLens) with no AI; multi-machine real-time point-cloud merge.
**Scope:** medium · working: Demo video linked; four code modules (capture, hub, align, replay); reported 20+ FPS prototype. · polish: Detailed README on architecture; HoloLens app lives in another repo; screenshots of server and depth views.
**Claims:** More than 20 FPS, record 23 FPS real-time reconstruction | README says it won Best Overall and YC Unicorn Prize demo selection
**Gaps:** Unity HoloLens viewer is in a separate repo not read; Evidence file lacks repo size fields
Sources: https://devpost.com/software/lattice-flck7q, https://github.com/KenC2006/Lattice (evidence file)

---

### Maatchaa
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Winner Hack the North 2025: Finalists

**What it is:** A matching platform that connects Shopify merchants with YouTube Shorts creators. Product and video embeddings are compared, brands swipe through ranked creator cards, and an accepted partnership puts sponsor links into the video description automatically.
**Problem / user:** Small Shopify brands lacking agency budgets and micro-creators with engaged audiences who have no easy way to find each other.

**Features**
- Shopify product ingestion — OAuth connects a store; catalog text and images are embedded with Cohere Embed v3. *[claimed]*
- YouTube Shorts discovery — Background worker finds Shorts, pulls transcripts, analyzes content with Gemini Flash, embeds into Pinecone. *[claimed]*
- Embedding-based matching — Cosine similarity between product and video vectors ranks creators for each product. *[claimed]*
- Swipe dashboard — Tinder-style card interface lets merchants swipe right on creators. *[shown_working]*
- Partnership confirmation — Creator is notified and accepts; sponsor links are then added to the video description via YouTube API. *[claimed]*
- AI product-set imagery — Nano Banana image model generates sponsored product sets, thumbnails and social visuals. *[claimed]*

**Flow:** Merchant connects Shopify store → Products embedded → Worker indexes Shorts → Merchant swipes ranked creator cards → Creator accepts → Description updated with sponsor link

**Prompt:** Finalists track: official text is only 'The finalists of Hack the North 2025!'; no further criteria published. Shopify sponsor track was 'Hack Shopping with AI'; Cohere track was best use of Cohere API.
**Fit (implied):** Built on Shopify catalogs and Cohere embeddings for retail matching; page does not name target prizes.  *(targeted: Hack the North 2025: Finalists, Shopify: Hack Shopping with AI, Cohere: Best Use of Cohere API)*
**Sponsor tools:** Cohere Embed v3 (Multimodal embeddings of products and videos for matching, core); Shopify API/OAuth (Store auth and product sync, core)
**AI:** Cohere embeddings plus Pinecone vector search for matching; Gemini Flash analyzes video frames and transcripts; Nano Banana generates product-set imagery.
**Architecture:** Next.js frontend (Vercel) -> Python BlackSheep backend (Cloud Run) with ARQ/Upstash Redis workers -> Supabase Postgres, Pinecone, YouTube, Shopify, Gemini, Cohere.
**Novelty:** Two-sided marketplace flow that closes the loop by editing the creator's live YouTube description after acceptance, not only recommending matches.
**Scope:** large · working: Live site at maatchaa.co, README describes deployed stack, tests directory and Docker, Prometheus metrics endpoint. · polish: Polished README with architecture table, hero screenshots, frontend/backend setup; README appears revised after the hackathon.
**Claims:** Sub-100ms similarity search (README) | Functional prototype linking Shopify products to Shorts
**Gaps:** Devpost says Nano Banana images; README omits them and says Gemini 1.5 Flash; Evidence file lacks size fields; No demo video
Sources: https://devpost.com/software/maatchaa, https://github.com/StockerMC/Maatchaa (evidence file)

---

### Puppeteer
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Winner Hack the North 2025: Finalists; Winner Warp: Best Developer Tool by Warp

**What it is:** A proof-of-concept 'AI runtime' for Python: probes placed in a target program forward selected instructions to an LLM agent, which can monitor, override or simulate them. A terminal UI lets a developer add probes and prompt the agent.
**Problem / user:** Frontend developers blocked by an unfinished backend, and developers wanting to test apps under simulated data and traffic.

**Features**
- Runtime probes — Probes inserted into target code hand chosen instructions to the agent instead of the Python interpreter alone. *[shown_working]*
- Variable tampering and event reporting — Agent overrides values, stops on complex conditions, reports events back in natural language. *[shown_working]*
- Simulated database/backend — Agent fakes backend responses so a frontend runs; README has a database mock demo. *[shown_working]*
- Terminal UI with CLI probe insertion — Run against a target path; LLM decides where to add probes. *[shown_working]*
- Martian-routed models — Changed items routed by rule to image, smarter text or lighter text models to cut cost. *[claimed]*
- Traffic simulation — Orchestrated simulated traffic for pre-scale testing. *[claimed]*

**Flow:** Point CLI at project path → Ask it to add probes → Install puppeteer library into target env → Run program normally → Prompt the AI runtime from the terminal UI → Receive natural-language trigger notices

**Prompt:** Warp Best Developer Tool: improve developer experience; judged on wow factor, difficulty, originality, design; Warp use optional; Keychron keyboards. Also Martian LLM routing track.
**Fit (implied):** Developer tool that unblocks frontend work with simulated backends; uses Martian routing. Page does not state Warp targeting.  *(targeted: Hack the North 2025: Finalists, Warp: Best Developer Tool by Warp, Martian: LLM Routing with Martian)*
**Sponsor tools:** Martian LLM router (Rule-based routing of runtime items to different models, supporting); Cohere (Mentioned as a model used; role not described, unclear); Warp (Prize entered; no Warp use described, token)
**AI:** LLM agent sits in the execution path via probes, deciding overrides and simulations; Martian router picks image, strong text or light text model.
**Architecture:** Python library (probes) in target app <-> AI agent; terminal UI (terminal/app.py) for prompting; Martian router to multiple LLMs.
**Novelty:** Puts an LLM inside program execution as a swappable runtime layer rather than a code-generating assistant.
**Scope:** small · working: README has two demo videos (database mock, debugging) and install steps; Devpost has demo video. · polish: README says later refactored for better UI and logic; not on PyPI.
**Claims:** Working product built in 30 hours | Won Warp Best Developer Tool
**Gaps:** Gemini and Cohere roles unexplained; Evidence lacks size fields; README is post-hackathon revision
Sources: https://devpost.com/software/puppeteer-7429qv, https://github.com/BrianLi23/puppeteer (evidence file), https://hackthenorth2025.devpost.com/

---

### ROSS - Remote Operated Semantic Sketching
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Winner Hack the North 2025: Finalists

**What it is:** A two-axis robot that draws a painting's outlines on a blind user's palm, using a cold brush with sanitizer and a warm brush with a heated resistor, while a Bob Ross-style voice narrates the content and music matches the mood.
**Problem / user:** Blind and visually impaired people who cannot enjoy 2D visual art; project turns images into touch, temperature and sound.

**Features**
- Semantic segmentation to strokes — SAM isolates elements, simplified outlines become stroke graphs ordered for drawing, smoothed with Ramer-Douglas-Peucker. *[shown_working]*
- Millimetre coordinate mapping — Digital paths converted to physical mm for stepper rails, claimed 1 mm spacing. *[claimed]*
- Palm-drawing robot — Arduino drives NEMA steppers and servos lifting two brushes over outstretched palms. *[shown_working]*
- Warm/cool lines — Regions classed red-ish or blue-ish; heated resistor vs alcohol brush; page says not fully working, demo single brush. *[claimed]*
- Narration — Fine-tuned XTTS Bob Ross voice describes each drawn component. *[claimed]*
- Mood music — Emotion-themed tracks (10 themes) played per painting sentiment. *[claimed]*
- Voice-triggered capture — Webcam grabs image on voice command. *[claimed]*

**Flow:** Say a command to capture a painting via webcam → SAM segments elements → Strokes planned and converted to mm → Robot draws on palms → Narration and music play

**Prompt:** Finalists track: official text is only 'The finalists of Hack the North 2025!'; no further criteria published.
**Fit (none):** Accessibility hardware project; no sponsor prize stated. Cohere and Gemini appear in tags.  *(targeted: Hack the North 2025: Finalists)*
**Sponsor tools:** Cohere (Listed in tags; repo has cohere-multimodal dir, role not described, unclear)
**AI:** Meta SAM for segmentation; LLM tried for simplification but dropped for math methods; Gemini and Cohere for sentiment/labeling (unclear); fine-tuned XTTS voice.
**Architecture:** Python pipeline (preprocess, vectorize, sentiment, TTS, music) -> numeric paths -> Arduino firmware -> steppers/servos.
**Novelty:** Translates visual art into thermal and tactile strokes on the palm with narration, an unusual multisensory accessibility device built from custom hardware.
**Scope:** medium · working: Repo about 14k LOC across vectorization, firmware, music, TTS; page admits warm/cold part incomplete. · polish: Devpost has no video; README in evidence is the music-player sub-readme.
**Claims:** 1 mm spacing accuracy target | Complete end-to-end system from vision to hardware
**Gaps:** Evidence README covers only the music player; No demo video; Cohere role unclear
Sources: https://devpost.com/software/ross-42pnvi, https://github.com/FowlFarmer/HTN2025 (evidence file)

---

### S-KBD67
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Hack the North 2025: Finalists

**What it is:** Nerf blasters modified with ESP8266/ESP32 boards, an MPU6050 gyroscope, joystick and buttons that act as a wireless game controller: motion aims the mouse, the joystick moves, the trigger shoots, and a Python app on the PC turns UDP packets into mouse and keyboard events.
**Problem / user:** FPS players who want to play a PC shooter physically with a real-feeling gun instead of a mouse.

**Features**
- Gyro aiming — MPU6050 orientation drives mouse movement and turning. *[shown_working]*
- Trigger, reload, weapon switch — Trigger and feature buttons mapped to fire, reload and weapon change. *[shown_working]*
- Joystick movement — Joystick module sends movement keys. *[shown_working]*
- Wi-Fi UDP transport — Microcontroller streams sensor packets to the PC at high rate. *[shown_working]*
- PC input translation — Python app decodes packets and injects mouse/keyboard events. *[shown_working]*
- Sensor calibration — Calibration step for smoother, natural input. *[claimed]*
- Multiplayer and VR/AR — Listed as next steps. *[planned]*

**Flow:** Hold modded blaster → Move and aim; sensors read → Microcontroller sends UDP over Wi-Fi → Python decodes to mouse/keyboard → Game reacts

**Prompt:** Finalists track: official text is only 'The finalists of Hack the North 2025!'; no further criteria published.
**Fit (none):** Hardware controller project; no sponsor tool or prize stated.  *(targeted: Hack the North 2025: Finalists)*
**AI:** none
**Architecture:** Blaster (ESP8266/ESP32 C++ via PlatformIO, MPU6050, joystick) -> UDP over Wi-Fi -> Python backend on PC -> synthetic mouse/keyboard input.
**Novelty:** Physical game-controller hack turning toy blasters into low-latency wireless mouse/keyboard devices, with split hardware and backend work.
**Scope:** small · working: Demo video linked; repo has firmware src, a backend dir and a test dir (about 300 LOC). · polish: Repo README is the default PlatformIO lib stub; Devpost explains hardware and challenges such as anti-cheat.
**Claims:** Low-latency wireless transmission of high-frequency sensor data
**Gaps:** README is boilerplate; Supported games not named; No latency figures
Sources: https://devpost.com/software/s-kbd67, https://github.com/Amelia1110/Valorant-Nerf-Gun (evidence file)

---

### Sauron
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence B · confidence medium*
**Prizes:** Hack the North 2025: Finalists

**What it is:** An investigation platform that ingests location pings of many devices into PostGIS, shows historical trajectories on a Mapbox map, estimates paths ('Crime Track') for who was near a crime scene, and answers spatio-temporal questions through a Cohere tool-use chatbot. Pitched at police and private investigators.
**Problem / user:** Law enforcement and private investigators facing roughly 50% violent-crime clearance; the page pitches faster identification of people near an incident.

**Features**
- Trajectory map — Interactive Mapbox view of historical device paths over a chosen period. *[claimed]*
- Crime Track — Estimates paths from location data to find who was at a crime location and where they went. *[claimed]*
- Natural-language investigator chatbot — Cohere Tool Use calls a Python function that queries the DB, e.g. who was near a spot in a 15-minute window. *[claimed]*
- Server-side filtering — Backend filters and aggregates so the UI renders only relevant points. *[claimed]*
- Location ping ingestion — Atomic transactions and error handling for API failures; hundreds of thousands of pings collected. *[claimed]*
- Resizable panel UI — Map, search and filter panels. *[claimed]*

**Flow:** Pick time range and area → View device paths on map → Use Crime Track at a location → Ask chatbot follow-ups

**Prompt:** Finalists track: official text is only 'The finalists of Hack the North 2025!'; no further criteria published. Cohere track: best use of Cohere API.
**Fit (implied):** Cohere tool use drives the investigator chatbot; page does not state target prizes.  *(targeted: Hack the North 2025: Finalists, Cohere: Best Use of Cohere API)*
**Sponsor tools:** Cohere (Tool Use) (Natural-language queries translated to spatio-temporal DB function calls, core)
**AI:** Cohere LLM with a defined tool/function that runs PostGIS queries; no other ML described.
**Architecture:** Location pings from undocumented APIs -> Flask + Psycopg2 -> Supabase PostgreSQL/PostGIS (GIST indexes) -> Next.js/Mapbox UI and Cohere chatbot.
**Novelty:** Combines large spatio-temporal geodata with an LLM tool-use interface. The data comes from reverse-engineered APIs; page mentions no consent or safeguards for tracked individuals.
**Scope:** medium · working: Page claims hundreds of devices tracked live and hundreds of thousands of pings; no video or live demo. · polish: Screenshots only; repo could not be read.
**Claims:** Tracked hundreds of devices at once | Hundreds of thousands of location pings | 10x more efficient investigations (stated aim)
**Gaps:** Repo clone failed and README fetch failed; No demo video; Data-source details not described beyond undocumented APIs
Sources: https://devpost.com/software/sauron-zvo2je, https://hackthenorth2025.devpost.com/

---

### SpeakEasy
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence B · confidence medium*
**Prizes:** Winner Hack the North 2025: Finalists

**What it is:** A behavioral-interview practice tool for job seekers. Users pick topics, record video answers to LLM-generated questions, and receive scored verbal feedback (relevance, STARR structure, depth, vocabulary, filler words) plus nonverbal feedback from MediaPipe pose and face analysis.
**Problem / user:** Job seekers who meet recruiter-side AI screening but lack applicant-facing practice with real verbal and nonverbal analytics.

**Features**
- Topic and question setup — Up to 3 of 6 topics, subtopics, question count, prep and response times; one-sentence questions generated per subtopic. *[claimed]*
- Video answer recording — Responses recorded and stored in Firebase. *[claimed]*
- Transcription keeping filler words — AssemblyAI transcript with fillers plus cleaned versions. *[claimed]*
- Five verbal subscores — LLM and spaCy score relevance, STARR clarity, depth, vocabulary, filler words with a pro and con each. *[claimed]*
- Validated feedback — Output checked for tone, length, format and regenerated until it passes. *[claimed]*
- Nonverbal scoring — MediaPipe models yield facial expression, eye movement, pausing, screen position and gesture scores. *[claimed]*

**Flow:** Choose up to 3 topics → Pick subtopics and timing → Get generated questions → Record answers → Transcription and analysis run → Read subscores and tips

**Prompt:** Finalists track: official text is only 'The finalists of Hack the North 2025!'; no further criteria published. Martian track: LLM routing with Martian.
**Fit (implied):** Uses Martian chat-completions API for questions and feedback; page does not state target prize.  *(targeted: Hack the North 2025: Finalists, Martian: LLM Routing with Martian)*
**Sponsor tools:** Martian chat completions (gpt-4.1-nano calls for questions and verbal feedback, supporting)
**AI:** LLM via Martian generates questions and feedback with validation-retry loop; AssemblyAI speech-to-text; spaCy for vocabulary/fillers; three MediaPipe models for body signals.
**Architecture:** Node/Express app with PostgreSQL and Firebase video storage; FastAPI service for spaCy; external LLM, AssemblyAI and MediaPipe analysis in parallel.
**Novelty:** Pairs verbal rubric scoring with MediaPipe nonverbal metrics, and enforces a generate-validate-regenerate loop on LLM feedback; applicant-side rather than recruiter-side.
**Scope:** medium · working: Demo video linked and detailed pipeline described; no live site. · polish: Rich feature description; repo unreadable.
**Claims:** Real-time AI scoring (stated) | Benchmarked LLM providers, chose OpenAI over Anthropic
**Gaps:** Repo clone and README fetch failed; No challenges or next steps on page
Sources: https://devpost.com/software/speakeasy-vdkc9n, https://hackthenorth2025.devpost.com/

---

### Stu3dio (Vibe Director)
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Hack the North 2025: Finalists

**What it is:** An AI film-making studio where users talk to role-specific AI 'workers' (Director, Scriptwriter, Character Artist) in a 3D studio map, edit characters and scene frames by scribbling on images, and generate scene clips stitched into a final short film.
**Problem / user:** Aspiring creators wanting an AI-generated short film without a traditional production pipeline.

**Features**
- Director and Scriptwriter chat — Brainstorm concept, characters, outline, dialogue and actions. *[claimed]*
- Scribble-to-edit character art — Draw on a character image to change style or clothing via image AI. *[claimed]*
- Timeline frame editing — View scenes and frames and edit images by scribbling. *[claimed]*
- Video generation and stitching — Per-scene clips generated and joined into a final film. *[claimed]*
- Project node tree — Nodes for logline, characters, objects, scenes, film; editing a parent marks descendants stale to regenerate. *[claimed]*
- Job queue — Each AI action is a Redis job processed by workers calling LLM, image, video providers. *[claimed]*
- 3D studio map navigation — Move around studio rooms in 3D. *[claimed]*

**Flow:** Brainstorm with Director → Write with Scriptwriter → Refine characters by scribbling → Review timeline and edit frames → Generate video, get stitched film

**Prompt:** Finalists track: official text is only 'The finalists of Hack the North 2025!'; no further criteria published.
**Fit (none):** No sponsor prize stated. Repo README says first place at Hack the North.  *(targeted: Hack the North 2025: Finalists)*
**AI:** LLM for plot and script, image-generation model for character sheets and frame edits, video-generation provider for clips; specific models not named.
**Architecture:** Next.js/React frontend -> Fastify backend with Supabase, Redis job queue and workers -> LLM/image/video providers -> blob storage artifacts.
**Novelty:** Staleness-propagating node tree limits context per regeneration, and the studio metaphor of 3D 'workers' wraps a full script-to-film pipeline.
**Scope:** large · working: Demo video linked; repo about 20k LOC with frontend and backend (tests present). · polish: README is two lines pointing to Devpost; page has 38 likes.
**Claims:** README: first place at Hack the North
**Gaps:** Models and providers unnamed; README claims first place while Devpost lists Finalists; No problem statement
Sources: https://devpost.com/software/vibe-director, https://github.com/Jeff15321/Stu3dio-HackTheNorth2025 (evidence file)

---

### Tango
*Hack the North Hack the North 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Hack the North 2025: Finalists

**What it is:** A macOS voice and clipboard assistant: after a wake word, a spoken request acts on clipboard text or a screenshot, rewriting text, making memes, removing image backgrounds, searching the web, and optionally remembering preferences.
**Problem / user:** Mac users who are tired of copy-paste round trips to an LLM chat; positioned as 'Siri if it worked'.

**Features**
- Wake word and end-of-speech detection — WebRTC voice activity detection plus hotword detect when to act and speed up replies. *[claimed]*
- Clipboard rewrite — Reformat, rephrase, synonym lookup or CSV conversion pasted back. *[claimed]*
- Meme from screenshot — Captions a captured image on request. *[claimed]*
- Web search — Gemini mode adds real-time search for queries with words like latest or news. *[claimed]*
- Optional persistent memory — ChromaDB memory with search and save actions, off by default. *[claimed]*
- Provider switch — Groq llama-3.3-70b by default or Gemini 2.5 flash-lite with fallback. *[shown_working]*
- Code help — Explains code or library equivalents. *[claimed]*

**Flow:** Say wake word and request → Tango detects end of sentence → Reads clipboard or screenshot → LLM returns action → Result copied or shown as notification

**Prompt:** Finalists track: official text is only 'The finalists of Hack the North 2025!'; no further criteria published. Graphite: Engineering Dream Team (AirPods Pro) and Groq prize also exist.
**Fit (implied):** Fast-LLM assistant on Groq/Gemini; page credits Graphite for team workflow and lists Graphite award.  *(targeted: Hack the North 2025: Finalists, Graphite: Engineering Dream Team, Groq)*
**Sponsor tools:** Groq (Default fast LLM provider, core); Graphite (Async team code review workflow, token)
**AI:** LLM agent (Groq Llama or Gemini) chooses actions over clipboard content; optional ChromaDB memory; guardrails judged too slow.
**Architecture:** Python macOS app: VAD and hotword -> speech to text -> LLM provider -> clipboard and notification APIs, optional ChromaDB memory.
**Novelty:** Clipboard as the interface surface for an always-listening assistant; trades guardrails and memory for latency.
**Scope:** small · working: Demo video in README and Devpost; about 2.4k LOC in app dir. · polish: Clear README with env-variable setup; no tests or Docker.
**Claims:** Faster than guarded LLM agents (no numbers)
**Gaps:** Devpost mentions Linux shortcut despite macOS focus; Speech-to-text component not named
Sources: https://devpost.com/software/tango-q37d4z, https://github.com/demanr/tango (evidence file)

---

