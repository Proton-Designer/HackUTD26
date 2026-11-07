# TAMUhack — TAMUhack 2026 (15 projects)

### AIsle0
*TAMUhack TAMUhack 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** First Place for American Airlines Challenge [1st]

**What it is:** A web and React Native platform that links airline ground and flight crews by flight number so they share live turnaround task status and carry out guided, photo-backed inspections with AI risk tagging.
**Problem / user:** Ground, flight and service crews on the same flight lack a shared flight-specific channel, causing delays and miscoordination during aircraft turnarounds.

**Features**
- Flight-number crew linking — Workers pick a flight and see everyone assigned to it; selection saved in a user_flights table. *[shown_working]*
- Live task status — Statuses like fueling in progress, completed or temporarily restricted sync across web and mobile through Supabase WebSockets. *[shown_working]*
- Role-specific inspection checkoffs — Inspection sessions with step instances, progress percentage and photo uploads per step. *[shown_working]*
- AI hazard tagging with audit log — OpenAI analyzes steps and stores an ai_severity per step; log kept for audit. *[shown_working]*
- Workday shift loading — Shifts pulled from Workday, described as an AA API. *[claimed]*
- 3D plane model and map — Web client uses three.js and Leaflet to show the aircraft and location. *[shown_working]*
- Team-wide task view — Overview of all inspection tasks across the crew. *[shown_working]*

**Flow:** Land on app and choose flight crew role → Shifts load from Workday → Select a flight → View 3D plane and map → Complete role-specific inspection checkoffs with photos → AI tags hazards to the audit log → See whole team task status

**Prompt:** American Airlines challenge: create a unique hack that improves passenger experience, employee experience, or operational efficiency for the airline.
**Fit (implied):** Targets employee experience and operational efficiency in aircraft turnarounds with shared status and inspection tools.  *(targeted: American Airlines Challenge)*
**AI:** OpenAI used to analyze inspection steps, plan work and tag risk severity per step with an audit trail.
**Architecture:** React/Vite web and Expo mobile clients talk to Supabase (Postgres, Auth, WebSockets, Edge Functions) with an API on Render; OpenAI analysis results written back and synced live.
**Novelty:** Frames airline ops as a shared real-time inspection and compliance record with AI hazard tagging, across web and mobile.
**Scope:** medium · working: Web, mobile and Supabase folders (~7.4k LOC); demo video; screenshots of each stage. · polish: Custom drawings/GIFs, detailed README with schema; no tests.
**Claims:** Real-time synchronization between web and mobile users implemented
**Gaps:** video not watched; Workday integration depth unclear
Sources: https://devpost.com/software/idk-yet-8ba2hz, evidence/tamuhack-tamuhack-2026-aisle0.json, https://th26.devpost.com/

---

### Aria: The Multimodal AI Kiosk
*TAMUhack TAMUhack 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Second Place for American Airlines Challenge [2nd]; [MLH] Best Use of Vultr

**What it is:** A voice-first airport kiosk assistant that recognizes a passenger by face or QR code, answers flight, weather, map and airport questions by voice, and shows a 3D audio-reactive particle sphere.
**Problem / user:** Air travelers facing touchscreen kiosks that are unhygienic, awkward with luggage and impersonal, especially when they miss connections or lose their gate.

**Features**
- Face or QR passenger login — DeepFace Facenet512 embeddings matched via MongoDB Atlas; QR alternative; loads passenger flight and profile. *[shown_working]*
- Voice and text assistant — LangGraph agent on Vultr-hosted Kimi-K2-Instruct streams over WebSocket with ElevenLabs speech and character-aligned text reveal. *[shown_working]*
- Airport knowledge RAG — Atlas Vector Search with 384-dim embeddings over an airport FAQ for baggage, security and facilities. *[shown_working]*
- Flight and rebooking help — Tools for gate, boarding, delay, cancellation, rebooking and overbooking offers from a flight database. *[shown_working]*
- Weather and maps — Weather for origin/destination and map views of gates, restrooms and services. *[shown_working]*
- 3D audio-reactive sphere — Three.js particle sphere (20k+ particles) deformed by FFT bass/mid/high bands. *[shown_working]*
- Resilient agent loop — Self-correcting retries, tool timeouts and plain-language error messages. *[shown_working]*

**Flow:** Authenticate with face or QR → Land on home screen → Speak or type request → Aria answers with voice and text reveal while sphere animates → View flight, weather, map or rebooking info → Errors shown as friendly messages

**Prompt:** American Airlines challenge: create a unique hack that improves passenger experience, employee experience, or operational efficiency for the airline. Also MLH Best Use of Vultr: build a project on Vultr cloud infrastructure such as serverless inference or GPUs.
**Fit (explicit):** Passenger-experience kiosk for airports; LLM inference runs on Vultr Serverless Inference.  *(targeted: American Airlines Challenge, [MLH] Best Use of Vultr)*
**Sponsor tools:** Vultr Serverless Inference (Kimi-K2-Instruct) (LLM behind the LangGraph agent, core); MongoDB Atlas (Vector search for RAG, flight and user/face databases, core); ElevenLabs (TTS with alignment timestamps, core)
**AI:** LangGraph agent with tool calling and self-correction on Kimi-K2 via Vultr; RAG over airport FAQ with sentence-transformer embeddings; DeepFace face recognition; ElevenLabs TTS.
**Architecture:** React/Three.js frontend over WebSocket to FastAPI; layers: transport, session manager, agent orchestrator, then LLM, tools, RAG and TTS; MongoDB Atlas stores flights, users, embeddings.
**Novelty:** Combines biometric login, agentic voice concierge and a custom 3D audio visual; includes layered backend refactor and separate registration module.
**Scope:** large · working: Demo video, Figma, ~21.8k LOC across frontend, backend, registration and test folders; many labeled screenshots. · polish: Extensive architecture README; 60fps tuning; .env.example; RAG tool noted as stub in README.
**Claims:** 60fps with 20,000+ particles during real-time audio | Exception hierarchy that never crashes (claimed)
**Gaps:** README says RAG service is a stub while Devpost claims working Atlas RAG; video not watched
Sources: https://devpost.com/software/aria-the-multimodal-ai-kiosk, evidence/tamuhack-tamuhack-2026-aria-the-multimodal-ai-kiosk.json, https://th26.devpost.com/

---

### Autonomous Surgical Light
*TAMUhack TAMUhack 2026 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Second Overall Hardware Hack [2nd]

**What it is:** A pan/tilt spotlight that follows where a surgeon looks: a webcam and MediaPipe estimate head pose, a browser relays commands over USB or Bluetooth to Arduino-driven servos, and a React dashboard handles calibration and manual override.
**Problem / user:** Surgeons who must stay sterile yet need light repositioned; manual handles or nurse help break workflow and headlamps raise sterility concerns.

**Features**
- Head-pose gaze tracking — MediaPipe Face Landmarker landmarks plus PnP and vector math produce a gaze vector from webcam video. *[shown_working]*
- Hands-free light aiming — Servos pan and tilt the spotlight toward the focal point; MG995 servos on a 3D-printed base. *[shown_working]*
- Dual control modes — Stability mode over USB Web Serial, wireless mode over Web Bluetooth BLE. *[shown_working]*
- Motion smoothing — Exponential smoothing alpha 0.2, 3 degree adaptive deadband and dynamic throttling reduce jitter. *[shown_working]*
- React calibration dashboard — Visualizes 3D tracking, calibrates and allows manual override; live demo page published. *[shown_working]*
- Multi-controller hardware — Arduino Nano 33 BLE runs kinematics, Uno drives NeoPixel LED ring over master/slave serial, separate power rails. *[shown_working]*
- Voice control — Commands like Light Off; attempts crashed from data load. *[planned]*

**Flow:** Surgeon looks at a spot → Webcam captures face → Python/MediaPipe computes gaze → Browser sends commands via USB or BLE → Servos aim light with smoothing → Operator calibrates or overrides in dashboard

**Prompt:** Overall Hardware Hack (1st-3rd): opt-in track for top hardware projects; prizes include scooter, 3D printer, headphones.
**Fit (implied):** Integrated hardware build combining computer vision, servos, LEDs and a web control bridge.  *(targeted: Overall Hardware Hack)*
**AI:** MediaPipe Face Landmarker for 3D facial landmarks; geometric PnP gaze estimation; no generative AI.
**Architecture:** Webcam to Flask/Python vision, WebSocket to React app, then Web Serial or Web Bluetooth to Arduino Nano 33 BLE (servos) and Uno (LED ring).
**Novelty:** Browser as hardware bridge using Web Serial and Web Bluetooth, applied to a surgical-lighting use case.
**Scope:** medium · working: YouTube demo and live dashboard page; hardware, wiring and 3D-printed base photos; no repo link. · polish: Documented tuning of voltages, batteries and smoothing; no quantitative tests.
**Claims:** Cites manual light adjustment about every 7.5 minutes | Cites 25 to 50 percent of surgeons reporting eye strain from lighting
**Gaps:** no repo; no performance measurements; video not watched
Sources: https://devpost.com/software/autonomous-surgical-light, https://th26.devpost.com/

---

### CarBaba
*TAMUhack TAMUhack 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Second Place for Toyota Challenge [2nd]

**What it is:** A car search and recommendation web app where shoppers state preferences by text or voice, set weights on each preference, get matched vehicles with 3D models, and compare any two cars side by side.
**Problem / user:** Choosy car buyers who must hop between sites that show fancy names but not full options and who end up polling many people.

**Features**
- Preference-weighted recommendations — Custom algorithm ranks cars by exact feature requests with per-preference weights. *[shown_working]*
- Natural-language AI bot — Gemini API interprets requests conversationally. *[shown_working]*
- Voice interaction — ElevenLabs speech-to-text and text-to-speech. *[shown_working]*
- 3D car models — Scraped models shown in the React UI. *[shown_working]*
- Two-car comparison — Side-by-side comparison across all parameters. *[shown_working]*
- Scraped car data in MongoDB — Specs collected from multiple sites and stored in Atlas; FastAPI on a GCP VM. *[shown_working]*

**Flow:** State preferences by text or voice → Set preference weights → Receive matched cars → Inspect 3D models → Compare two cars side by side

**Prompt:** Toyota challenge: recommendation engine for a caravan marketplace so every search returns meaningful results, using semantic search, personalization, constraint relaxation and inventory-aware fallbacks.
**Fit (implied):** Delivers personalized car search with weighting and AI chat; no caravan, inventory or constraint-relaxation logic is described.  *(targeted: Toyota Challenge)*
**Sponsor tools:** MongoDB Atlas (Car data storage, supporting); ElevenLabs (Speech-to-text and text-to-speech, supporting)
**AI:** Gemini API powers a natural-language assistant; team-built scoring algorithm drives recommendations; ElevenLabs handles voice.
**Architecture:** React/Vite on Vercel calls FastAPI on a GCP VM backed by MongoDB Atlas, with Gemini and ElevenLabs APIs.
**Novelty:** Adds 3D vehicle viewing and voice to a weighted car-matching tool.
**Scope:** medium · working: Live Vercel demo and repo with ~6.6k LOC frontend and backend. · polish: Animations noted; README is only a title; no video.
**Claims:** Granular per-preference control over results
**Gaps:** README empty; algorithm details unknown
Sources: https://devpost.com/software/carbaba, evidence/tamuhack-tamuhack-2026-carbaba.json, https://th26.devpost.com/

---

### Celcii PixiPen
*TAMUhack TAMUhack 2026 · dataset: winners · tier: overall_top3 · evidence C · confidence low*
**Prizes:** Third Overall Hardware Hack [3rd]

**What it is:** A hardware pen project built around an ESP32 and custom PCB with the tagline write anywhere, anytime; the Devpost page gives no functional description.
**Problem / user:** Not stated on the page.

**Features**
- Pen on ESP32 and custom PCB — Electronics inside the pen; C++/Python written in Arduino IDE; actual sensing or output function not described. *[unclear]*
- Write on any surface or in air — Tagline implies surface-independent writing; mechanism unspecified. *[claimed]*

**Prompt:** Overall Hardware Hack (1st-3rd): opt-in track for top hardware projects.
**Fit (none):** Custom-PCB hardware pen; page states no prize target.  *(targeted: Overall Hardware Hack)*
**AI:** none
**Architecture:** ESP32 microcontroller on a custom PCB inside a pen body; further detail not given.
**Novelty:** Custom PCB in a pen form factor; mechanism not documented.
**Scope:** small · working: One photo captioned inside the pen; no video, repo or demo. · polish: Very sparse page.
**Gaps:** no description of function; no repo, video or demo
Sources: https://devpost.com/software/pixipen, https://th26.devpost.com/

---

### Cinder Control
*TAMUhack TAMUhack 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Second Place for NorthMark Compute & Cloud Challenge [2nd]; Best Solo Hack

**What it is:** A solo-built wildfire dashboard where a user types or speaks fire conditions, a Python cellular-automata model projects spread up to 96 hours, and the map flags infrastructure in the path and evacuation routes, with spoken replies.
**Problem / user:** Incident commanders, first responders and residents in fire-prone areas who need faster, easier-to-use tools to see where a fire is heading and what it will hit.

**Features**
- Conversational control — OpenAI parses typed or spoken requests to start a simulation or pull an alert; works on desktop and mobile. *[shown_working]*
- Fire spread simulation — Parallelized cellular-automata model in FastAPI projects spread up to 96 hours given wind and other parameters. *[shown_working]*
- Infrastructure impact warnings — Cross-references simulation with OpenStreetMap/Overpass data to list landmarks and infrastructure with estimated time to impact. *[shown_working]*
- Evacuation and access routing — Plans routes between points around the predicted burn area on a Mapbox map. *[shown_working]*
- Voice narration — Responses synthesized and narrated via ElevenLabs. *[shown_working]*
- Alert list of past simulations — Previously simulated fires saved as alerts to recall. *[shown_working]*
- Live wildfire data and other hazards — Auto-ingest real fires and extend to hazards like smog. *[planned]*

**Flow:** Type or speak fire parameters → Backend parses intent → Simulation runs or alert loaded → Map shows vulnerable locations and impact times → Request evacuation route → Hear narrated answer

**Prompt:** NorthMark Compute & Cloud challenge: design and prototype an app letting a non-expert submit a compute job to an HPC cluster (or simulated one) without understanding HPC; judged on input structuring, abstraction of large-scale processing, result presentation, and creative gen/agentic AI use.
**Fit (implied):** Wraps a heavy parallel simulation behind a conversational interface so non-experts can run it; the author notes the map-load issue would also matter on HPC.  *(targeted: NorthMark Compute & Cloud Challenge, Best Solo Hack)*
**AI:** OpenAI parses natural language into simulation actions and generates responses; ElevenLabs TTS narration; Gemini only used for UI styling ideas.
**Architecture:** Next.js/TypeScript Mapbox frontend calls FastAPI backend running numpy/scipy cellular automata; OpenStreetMap Overpass and NOAA NWS supply geo and weather context.
**Novelty:** Puts a spread simulator and evacuation routing behind voice/text chat; built solo in 36 hours.
**Scope:** small · working: Demo video, README with run steps, ~1.9k LOC, backend plus Next.js app. · polish: Mobile-friendly layout, voice narration; no tests; author states first map project.
**Claims:** Projects spread up to 96 hours ahead | Built solo in 36 hours
**Gaps:** no accuracy validation of spread model; video not watched
Sources: https://devpost.com/software/fsim, evidence/tamuhack-tamuhack-2026-cinder-control.json, https://th26.devpost.com/

---

### Constellation
*TAMUhack TAMUhack 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** First Place for NorthMark Compute & Cloud Challenge [1st]

**What it is:** A web-based HPC-native IDE where users describe a goal, an agentic Gemini-driven assistant builds a visual dataflow graph of a parallel workflow, and it runs locally or on AWS Batch with autoscaling workers.
**Problem / user:** Researchers and newcomers blocked by the terminal-heavy complexity of HPC who want to run parallel workloads without schedulers or a CS background.

**Features**
- Visual execution graph — Parallel computing modeled as data flow; nodes accept single or many input files pipelined like a superscalar processor. *[shown_working]*
- Agentic workflow builder — AI orchestrator and worker models construct, run and debug workflows from a natural-language goal, including autopilot debugging. *[shown_working]*
- AWS Batch cluster execution — Real deployment on AWS Batch with dynamically scaled EC2 workers and S3 object handles. *[shown_working]*
- Local test mode — Backend runs small files locally for quick checks. *[shown_working]*
- Data and code editors — Spreadsheet-style CSV editor and Monaco code editor views. *[shown_working]*
- Auth and persistence — NextAuth/Firebase login stores graph and chat history per project. *[shown_working]*
- Scheduler abstraction — Hides batch script and job syntax from the user. *[shown_working]*

**Flow:** Log in and open project → Upload data and state goal → AI builds graph with input nodes → Run locally or deploy to AWS Batch → Edit CSV or code, use autopilot debug → Graph and chat saved

**Prompt:** NorthMark Compute & Cloud challenge: design and prototype an app letting a non-expert submit a compute job to an HPC cluster (or simulated one) without understanding HPC; judged on input structuring, abstraction of large-scale processing, result presentation, and creative gen/agentic AI use.
**Fit (implied):** Non-expert HPC access via an agentic visual IDE with real cloud cluster execution and abstracted scheduling.  *(targeted: NorthMark Compute & Cloud Challenge)*
**AI:** Gemini-based orchestrator and worker agents that build, modify and debug workflow graphs from natural language, with constrained edits.
**Architecture:** Next.js/React front end with reagraph and Monaco; backend dispatches to local runner or AWS Batch/Step Functions with S3 storage; Firebase auth.
**Novelty:** Dataflow-graph abstraction of parallelism with an agent editing the graph; real AWS Batch deployment rather than simulation.
**Scope:** large · working: Live Railway demo, demo video, ~19k LOC with Docker and AWS SDK usage. · polish: Dark/light modes, many editor views; README is default Next.js boilerplate.
**Claims:** Real cluster deployment, not simulated workload | Frictionless agentic AI integration (self-described)
**Gaps:** README boilerplate; video not watched
Sources: https://devpost.com/software/constellation-qcb483, evidence/tamuhack-tamuhack-2026-constellation.json, https://th26.devpost.com/

---

### cortex
*TAMUhack TAMUhack 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** First Overall Software Hack [1st]

**What it is:** A traveler companion with an iOS app and web dashboard that remembers where you set items down, alerts you when a checked bag reaches the carousel, logs bags on Solana, and answers flight questions with a fast voice agent.
**Problem / user:** Air travelers who misplace small items or cannot spot their checked bag, including a low-vision creator, plus airlines facing lost-baggage costs.

**Features**
- Item location memory — iOS ARKit/Vision/CoreML hand and object tracking saves where an item was put down and guides you back. *[claimed]*
- Bag carousel alert — OpenCV bag detection scanned at check-in pings the phone when the bag reaches the carousel via WebSockets. *[claimed]*
- Solana bag ledger — Checked bags recorded on-chain; fee-and-refund incentive model proposed. *[claimed]*
- Voice agent — Gemini 2.0 Flash with ElevenLabs STT/TTS answers flight and gate questions, sub-2-second claimed. *[claimed]*
- 3D Gaussian splat terminal view — Three.js viewer shows scanned terminal with item locations; scans processed on Vultr GPU VMs. *[shown_working]*
- Live baggage and flight views — Web dashboard with map, inbound/outbound flights, missing-bag claim and item info sheet. *[shown_working]*

**Flow:** Sign in with Auth0 → Put an item down and app saves its spot → Tap find to be guided back → Scan bag at check-in → Receive carousel alert → Ask voice agent about flight → View 3D terminal and live map

**Prompt:** Overall Software Hack (1st-3rd): opt-in track for the top software projects overall. Also American Airlines Challenge: improve passenger or employee experience or operations.
**Fit (implied):** Passenger-experience tool for lost items and baggage tracking built around an airline partner pitch.  *(targeted: Overall Software Hack, American Airlines Challenge)*
**Sponsor tools:** Vultr GPU VMs (Processing Gaussian splat scans, supporting); ElevenLabs (Speech-to-text and text-to-speech voice agent, core); MongoDB Atlas (Data storage, supporting); Auth0 (Authentication, supporting)
**AI:** On-device CoreML/Vision hand and object tracking, OpenCV bag detection, Gemini 2.0 Flash voice agent with ElevenLabs speech, Gaussian splatting for 3D scans.
**Architecture:** Swift iOS app and Next.js web app talk to a Node backend with WebSockets and MongoDB; OpenCV service for bags; Solana program via Anchor; Vultr GPUs for splats.
**Novelty:** Mixes AR object memory, blockchain bag ledger, voice agent and Gaussian splat terminal in one travel app.
**Scope:** large · working: Demo video, project site, two repos (~11k LOC web/cv/lostObject) including iOS app. · polish: Workflow charts folder, 3D visuals; README is two lines; no tests.
**Claims:** Voice responses under 2 seconds | Airlines lose over $2 billion a year to lost luggage and fraud | Built in 24 hours by four people
**Gaps:** iOS repo not read; claims unmeasured
Sources: https://devpost.com/software/cortex-67ueyq, evidence/tamuhack-tamuhack-2026-cortex.json, https://th26.devpost.com/

---

### Haggle
*TAMUhack TAMUhack 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Third Overall Software Hack [3rd]

**What it is:** A voice negotiation trainer where users bargain with an AI counterpart that reads their stress from iPhone-camera vitals and adapts tactics in real time, then shows a reveal page with its hidden budget and the stress timeline.
**Problem / user:** People who underprepare or crack under pressure when negotiating salary, business or consumer deals; the page cites 78% never negotiating pay.

**Features**
- Stress-adaptive AI negotiator — Gemini 2.5 Flash via ElevenLabs Conversational AI gets stress context every 2 seconds and shifts tactics without revealing it. *[shown_working]*
- Contactless biometrics — Presage SmartSpectra iOS SDK reads heart rate, breathing rate and depth, speech; 10-second baseline calibration. *[shown_working]*
- Stress score — 0 to 100 score from HR and breathing deviations, EWMA smoothing; sent over Socket.IO. *[shown_working]*
- Negotiation scenarios — Salary, B2B or consumer, with a hidden budget and research-based tactics (Fisher and Ury, Voss, Kahneman). *[shown_working]*
- Reveal page — Shows hidden budget, stress timeline, money left on the table, logged context beside replies and a finance lesson. *[shown_working]*
- QR phone pairing — Web app shows QR with session and server URL to configure the iOS app. *[shown_working]*

**Flow:** Pick scenario → Scan QR with iPhone app → 10-second calibration → Negotiate by voice with Hal → Stress context injected every 2 seconds → Review reveal page

**Prompt:** Overall Software Hack (1st-3rd): opt-in track for the top software projects overall.
**Fit (none):** General software entry; no sponsor challenge targeted on the page.  *(targeted: Overall Software Hack)*
**Sponsor tools:** ElevenLabs Conversational AI (Voice agent hosting Gemini and receiving contextual updates, core)
**AI:** Gemini 2.5 Flash behind ElevenLabs agent with a negotiation knowledge base and biometric context injected every 2 seconds.
**Architecture:** iPhone SwiftUI app (Presage) sends vitals via Socket.IO to a custom Node/Next.js server, which pushes context to ElevenLabs; results rendered with Recharts; hosted on Railway.
**Novelty:** Feeds physiological signals into an LLM mid-conversation as a counterpart that exploits stress.
**Scope:** medium · working: Live Railway demo, demo video and detailed README with algorithm and pipeline. · polish: Reveal page logs every context update to prove adaptation; README includes diagrams.
**Claims:** Stress score reacts to real changes in 3 to 4 seconds | Built in 24 hours | Context updates every 2 seconds
**Gaps:** no validation of stress detection; README truncated at 7k chars
Sources: https://devpost.com/software/haggle-admqhc, evidence/tamuhack-tamuhack-2026-haggle.json, https://th26.devpost.com/

---

### HPC Runner
*TAMUhack TAMUhack 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Second Overall Software Hack [2nd]

**What it is:** A web IDE for submitting jobs to a SLURM cluster: users upload a zip and describe the goal, Gemini analyzes the code to pick an entrypoint and resources, and an MCP server lets AI agents submit and fetch jobs too.
**Problem / user:** Researchers, students and analysts who need large-scale compute but are blocked by schedulers and scripts; also AI agents needing programmatic cluster access.

**Features**
- Zip upload with auto entrypoint — Extracts files with Zip Slip protection; Gemini finds entrypoint and classifies workload as sweep, single or distributed. *[shown_working]*
- Resource estimation — Layered L0-L6 pipeline then deterministic calculation capped to cluster limits (4 CPUs, 4GB, 0 GPUs). *[shown_working]*
- SLURM job submission — Custom FastAPI SLURM API generates batch scripts, installs dependencies, streams logs and returns results zip. *[shown_working]*
- IDE-like file tree and editor — Drag-and-drop tree, inline editing, job configuration and status tracking. *[shown_working]*
- MCP server for agents — LLMs package files, submit and manage jobs, fetch results and analyze them. *[shown_working]*
- Auth and persistence — JWT/Auth0 login with MongoDB per-user jobs. *[shown_working]*
- Demo workloads — MNIST training, weather prediction and 100 blackjack hands run through it. *[shown_working]*

**Flow:** Log in → Upload zip and describe goal → Review detected entrypoint and resources → Submit job → Monitor progress and logs → Download results

**Prompt:** NorthMark Compute & Cloud challenge: design and prototype an app letting a non-expert submit a compute job to an HPC cluster (or simulated one) without understanding HPC; judged on input structuring, abstraction of large-scale processing, result presentation, and creative gen/agentic AI use.
**Fit (implied):** Matches the non-expert HPC job submission brief: AI infers entrypoint and resources, abstracts SLURM, presents logs and results.  *(targeted: NorthMark Compute & Cloud Challenge, Overall Software Hack)*
**AI:** Multi-stage Gemini pipeline for code structure analysis, entrypoint detection, workload classification with confidence, then rule-based resource calculation and validation.
**Architecture:** Vite React frontend and Next.js API with MongoDB; custom Python SLURM API on a cluster; Gemini analysis layer; MCP server on top.
**Novelty:** Offers both human UI and MCP interface for agents over the same SLURM backend.
**Scope:** large · working: Demo video, screenshots of running and failed jobs, detailed README with setup. · polish: Multiple services, validation and fallbacks; team used laptop without GPU.
**Claims:** Built at massive scope | Runs MNIST, weather prediction and blackjack simulation jobs
**Gaps:** cluster scale unclear; video not watched
Sources: https://devpost.com/software/slurmglue, evidence/tamuhack-tamuhack-2026-hpc-runner.json, https://th26.devpost.com/

---

### MediBot
*TAMUhack TAMUhack 2026 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** First Overall Hardware Hack [1st]

**What it is:** A first-aid robot concept: a Raspberry Pi camera watches for falls, vision AI classifies the injury, a custom robot arm hands over the matching supplies from a kit, and a live voice agent coaches the bystander.
**Problem / user:** Bystanders who panic in medical emergencies and need guidance and supplies before professionals arrive.

**Features**
- Fall monitoring — Raspberry Pi with CSI camera builds a voxel map to detect falls. *[claimed]*
- Injury classification — GPT-4 Vision and Gemini classify injuries such as burns, lacerations and sprains. *[claimed]*
- Robotic arm retrieval — Custom arm with Python control picks and presents the right first-aid items. *[shown_working]*
- Voice guidance — LiveKit agent with Deepgram STT, Groq Llama 3.3 70B and ElevenLabs TTS gives calm step-by-step instructions. *[claimed]*
- Live video sync — Video feed synchronized with the voice agent so it can see the situation. *[claimed]*

**Flow:** Camera monitors for a fall → Vision AI classifies injury → Arm retrieves matching supplies → Voice agent walks user through steps

**Prompt:** Overall Hardware Hack (1st-3rd): opt-in track for top hardware projects (scooter, 3D printer, headphones).
**Fit (none):** Robotics plus vision and voice AI system for medical emergencies.  *(targeted: Overall Hardware Hack)*
**AI:** GPT-4 Vision and Gemini for injury classification, Groq-hosted Llama 3.3 70B for decisions, Deepgram STT and ElevenLabs TTS orchestrated with LiveKit Agents; LeRobot and Roboflow listed.
**Architecture:** Pi/CSI camera and robot arm feed vision models; LiveKit agent combines video, speech and LLM reasoning to speak instructions and trigger arm.
**Novelty:** Combines physical robotic retrieval of supplies with real-time voice-and-vision coaching.
**Scope:** medium · working: Embedded demo video; custom arm and Pi hardware; no repo. · polish: No metrics or latency numbers reported.
**Claims:** Synchronized a live video feed with an AI voice agent
**Gaps:** no repo; video not watched; roles of LeRobot, Roboflow unexplained
Sources: https://devpost.com/software/medibot-as2980, https://th26.devpost.com/

---

### PocketPlay
*TAMUhack TAMUhack 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Third Place for NorthMark Compute & Cloud Challenge [3rd]; Best Beginner Hack (Software)

**What it is:** A football play simulator with Coach mode and NFL mode: pick offensive and defensive schemes on a field graphic, run an ML simulator trained on nflfastR data, and get an AI agent critique; NFL mode simulates thousands of team matchups.
**Problem / user:** Coaches, fans and analysts wanting to test plays and matchups; the page calls football play simulation underexplored.

**Features**
- Scheme selection on field graphic — Drop-downs reposition offensive and defensive markers. *[shown_working]*
- ML play simulator — Python model trained on nflfastR reports success rate, yards per attempt and completion, turnover and touchdown counts. *[shown_working]*
- AI play advisor — Gemini-based agent evaluates a play and suggests alternatives against a defensive scheme. *[shown_working]*
- Route animation and 3D POV — Receivers animate routes; street-view style 3D result view. *[claimed]*
- Player profiles — Adjust strengths and weaknesses to produce team ratings. *[shown_working]*
- NFL mode — Madden 26 player data and thousands of simulated iterations to estimate win probability. *[shown_working]*
- Auth0 sign-in — Welcome page login. *[shown_working]*

**Flow:** Sign in → Choose Coach or NFL mode → Select schemes or teams → Run simulation → Review stats → Ask AI agent or view 3D POV

**Prompt:** NorthMark Compute & Cloud challenge: design and prototype an app letting a non-expert submit a compute job to an HPC cluster (or simulated one) without understanding HPC; judged on input structuring, abstraction of large-scale processing, result presentation, and creative gen/agentic AI use. Also Best Beginner Hack (Software): best software hack by first-time hackers.
**Fit (implied):** Frames thousands of play simulations as an HPC-style workload with a friendly interface; no real cluster named.  *(targeted: NorthMark Compute & Cloud Challenge, Best Beginner Hack (Software))*
**AI:** Python ML play simulator trained on nflfastR data; Gemini-powered agent suggests plays; Madden 26 ratings for strength.
**Architecture:** Next.js/React/TypeScript app with Konva field and three.js view, Auth0, Python simulator and a worker script, Gemini agent.
**Novelty:** Football simulation combining ML outcomes, route animation and a Madden-ratings NFL matchup mode.
**Scope:** medium · working: Demo video and repo with ~12.7k LOC; no live link. · polish: README is default boilerplate; team notes chatbot idea dropped for drop-downs.
**Claims:** Simulates thousands of iterations between NFL teams
**Gaps:** no accuracy metrics; README boilerplate
Sources: https://devpost.com/software/pocketplay, evidence/tamuhack-tamuhack-2026-pocketplay.json, https://th26.devpost.com/

---

### RideIQ
*TAMUhack TAMUhack 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** First Place for Toyota Challenge [1st]

**What it is:** A car marketplace search app using pgvector semantic search over listings, progressive constraint relaxation with explanations, zero-match fallbacks, personalization, and a four-car comparison page with charts and AI analysis.
**Problem / user:** Car buyers frustrated by rigid filters and keyword search who would rather describe needs in plain language.

**Features**
- Semantic search — Natural-language queries like AWD family SUV under 25k Dallas matched via vector embeddings in Supabase pgvector. *[shown_working]*
- Constraint relaxation — Progressively loosens strict filters and explains why when results are scarce. *[claimed]*
- Zero-match fallbacks — Always returns comparables, nearby deals or best available options. *[claimed]*
- Personalization — Recommendations based on behavior and preferences, with seeded demo interactions. *[shown_working]*
- Filters and favorites — Filter by make, year, price, mileage, drivetrain, fuel, seats, location; save favorites. *[shown_working]*
- Compare up to four cars — Metrics table, price/MPG/mileage charts, radar and AI analysis. *[shown_working]*
- Test-drive email — Resend email confirmations for test drives. *[claimed]*

**Flow:** Search in plain English → Browse filtered results → Open car details → Add cars to compare → View charts and AI analysis → Favorite or book test drive

**Prompt:** Toyota challenge: build an e-commerce recommendation engine for a caravan marketplace so every search returns meaningful results, with semantic search, personalization, constraint relaxation, inventory-aware logic and fallback recommendations.
**Fit (explicit):** README says it is built for the Toyota challenge and implements semantic search, personalization, constraint relaxation and zero-match fallbacks for a car marketplace.  *(targeted: Toyota Challenge)*
**AI:** Embeddings (Xenova transformers with hashed fallback) in pgvector for semantic search; AI-generated comparison analysis.
**Architecture:** Next.js App Router with API routes over Supabase Postgres + pgvector and Supabase Auth; CSV ingestion of 43k vehicles and generated listings.
**Novelty:** Directly implements each element of the challenge brief, with 60k synthetic listings from a 47k-row vehicle dataset.
**Scope:** medium · working: Demo video, repo with migrations and seed scripts, live demo via Zoom invite. · polish: Detailed README with setup and .env.example.
**Claims:** Every search returns meaningful results even with strict constraints | Imports about 43,000 vehicles and generates 60,000+ listings
**Gaps:** listings are synthetic; video not watched
Sources: https://devpost.com/software/rideiq, evidence/tamuhack-tamuhack-2026-rideiq.json, https://th26.devpost.com/

---

### Stowed
*TAMUhack TAMUhack 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Third Place for American Airlines Challenge [3rd]

**What it is:** A Next.js web app for air travelers that combines an AI image-matching lost-and-found for checked bags with a Smart-Cabin predictor that estimates when a flight's overhead bins will be full from carry-ons logged at check-in.
**Problem / user:** Air travelers whose bag tags fall off or whose carry-ons get gate-checked because bins fill up; flight attendants are also mentioned as users of capacity data.

**Features**
- Account sign-up and login with personal luggage registry — Users register each bag in a Prisma-backed database tied to their account. *[claimed]*
- Visual ID / reverse image search for lost bags — Bag photos are compared by visual traits (zippers, scratches, stains) using an OpenAI-API-based matcher; team admits accuracy is limited. *[claimed]*
- Smart-Cabin overhead bin capacity prediction — Carry-ons logged at check-in feed a capacity calculation that predicts when bins fill and alerts passengers. *[claimed]*
- Baggage tracking through the flight process — Registered bags show status along the journey in the dashboard. *[claimed]*
- Real-time flight tracking — An aviation API supplies live flight paths rendered client-side. *[claimed]*

**Flow:** Sign up or log in → Register luggage in the database → View a flight and see predicted cabin capacity → If a bag goes missing, search the online lost-and-found by image

**Prompt:** not public / not found
**Fit (implied):** Addresses airline passenger pain points of lost baggage and gate-checked carry-ons; the challenge text could not be retrieved, so the link is inferred from the sponsor theme.  *(targeted: American Airlines Challenge)*
**AI:** OpenAI API used for image-based bag matching; team says it trained the model to recognize bag features but names no model or method. Antigravity AI assisted coding.
**Architecture:** Next.js/React/TypeScript/Tailwind frontend on Vercel, Prisma ORM with auth adapter and bcrypt, OpenAI image matching, and an aviation API for flight data.
**Novelty:** Pairs two separate airline pain points (lost-bag matching and bin-capacity forecasting) in one app; crowd-sourced carry-on logging as the capacity signal is uncommon.
**Scope:** medium · working: Live Vercel demo and about 11.8k LOC repo with Prisma schema; no tests; team concedes visual ID is inaccurate. · polish: v0-generated shadcn UI with many components; four screenshots and a video.
**Claims:** Identifies luggage without tags via visual fingerprint | Gives passengers and attendants real-time bin-capacity data
**Gaps:** AA challenge text not retrievable; no accuracy numbers; video not watched
Sources: https://devpost.com/software/stowed, https://github.com/joshuale2007/STOWED-TAMUHACK-2026

---

### Treat Me To A Toyota
*TAMUhack TAMUhack 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Third Place for Toyota Challenge [3rd]

**What it is:** A voice-driven Toyota shopping assistant: the user talks about lifestyle, budget and must-haves, an LLM queries a vehicle database, and an image carousel updates live to show matching cars and requested features.
**Problem / user:** Car shoppers who find endless clicking and rigid filters tedious and would rather describe needs in natural language.

**Features**
- Voice agent conversation — Vapi human-sounding voice agent listens to preferences and asks follow-up questions to refine them. *[claimed]*
- LLM tool-calling against vehicle database — Model generates SQL queries against Postgres on Supabase to find matching vehicles. *[claimed]*
- Live feature-aware image carousel — Carousel updates as preferences are identified and alternates images to show asked-for features such as white leather seats. *[claimed]*
- Listings, discovery and listing pages — Screenshots show a home page with search, car listings, a discovery page and a listing detail page. *[claimed]*
- Payment form — A checkout-style payment form page appears in screenshots. *[unclear]*

**Flow:** Open home page → Speak preferences to the voice agent → Answer follow-up questions while carousel updates → Browse listings and discovery page → Open a listing → Reach the payment form

**Prompt:** not public / not found
**Fit (implied):** A conversational way to find a matching Toyota; challenge text could not be retrieved so fit is inferred from Toyota-only inventory and car-buying theme.  *(targeted: Toyota Challenge)*
**AI:** Claude Opus 4.5 and other models with tool-calling to generate SQL over the car database; Vapi for voice; Groq SDK in dependencies though its role is unstated.
**Architecture:** Next.js client with Vapi web SDK for voice, LLM tool calls to Supabase Postgres, framer-motion carousel; repo also includes better-sqlite3.
**Novelty:** Voice-first interface that drives a visual carousel in real time, rather than a text chatbot over filters.
**Scope:** small · working: Vercel demo and video link; about 5.4k LOC Next.js app with tests present. · polish: Multiple pages with animation; default create-next-app README; three screenshots.
**Claims:** Carousel is engaging and loads images seamlessly from voice requests
**Gaps:** Toyota challenge text not retrievable; README is boilerplate; vehicle data source not stated
Sources: https://devpost.com/software/toyota-truefit, https://github.com/Lukeyp43/TamuHack-2026-Dream-Team

---

