# TreeHacks — TreeHacks 2026 (4 projects)

### CalTrack
*TreeHacks TreeHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [NVIDIA] Edge AI Track

**What it is:** A California wildfire disaster-intelligence platform for emergency managers. It maps population density from aggregated Wi-Fi positioning data, overlays Earth-2 fire-risk forecasts, and prototypes an AI voice 911 triage line whose agent mesh extracts addresses and medical details for operators.
**Problem / user:** Emergency managers, 911 operators, responders and hospitals lacking a unified view combining live 911 information with population density for wildfire response.

**Features**
- Population density map — Aggregated Wi-Fi Positioning System data from network devices is parsed from Protobuf and shown as density; 650,000 devices mapped around Palo Alto. *[shown_working]*
- Fire-risk overlay — NVIDIA Earth-2 (FCN3 via earth2studio) forecasts fire-favorable weather served by a GPU FastAPI service. *[claimed]*
- 911 agent mesh — CrewAI agents parse call text in real time; healthcare agents record conditions and triage level, geolocation agents extract addresses and place map markers. *[claimed]*
- AI voice call center — Voice operator prototyped on VAPI (Personaplex plan dropped) to take overflow calls; repo has a Twilio bridge to PersonaPlex. *[claimed]*
- Resource allocation recommendations — Density and risk overlays inform suggested emergency resource placement. *[claimed]*
- Hazard map — Flask backend normalizes public hazard feeds to GeoJSON for a Mapbox React map. *[shown_working]*

**Flow:** Open the California hazard map and density overlay → Demo on historical Palo Alto data → A 911-style call is parsed by agents → Address becomes a marker on operator map → Medical and triage details go to hospitals and ambulances

**Prompt:** Edge AI track at TreeHacks 2026: build projects running AI on NVIDIA edge hardware; prizes include DGX Spark, Jetson Orin Nano Super and Brev credits. Detailed criteria not on overview page.
**Fit (explicit):** Runs NVIDIA Earth-2 forecasts and open models on DGX Spark hardware; the page says voice model deployment on the DGX failed during onboarding so VAPI was used instead.  *(targeted: [NVIDIA] Edge AI Track)*
**Sponsor tools:** NVIDIA DGX Spark (Hosting open models and forecasting, core); NVIDIA Earth-2 (Fire-risk weather forecasting, core); NVIDIA PersonaPlex (Planned voice 911 operator, not deployed, token)
**AI:** Earth-2 FCN3 weather forecasts; CrewAI multi-agent mesh for call parsing and triage; voice via VAPI. Humans stay in the loop.
**Architecture:** React/Mapbox frontend, Flask hazard aggregator, FastAPI GPU forecast service, Twilio voice bridge, and a Postgres-backed WPS crawler.
**Novelty:** Uses Wi-Fi positioning data as an aggregate population signal, combined with weather forecasting and a voice triage prototype; monorepo bundles several services.
**Scope:** medium · working: Historical Palo Alto demo and three screenshots; no demo link or video. · polish: Multi-service monorepo with README, Docker, tests; some components stubbed.
**Claims:** Mapped 650,000 network devices in 6 hours around Palo Alto | Voice 911 operator prototyped with real-time detail extraction
**Gaps:** no video; privacy framing inconsistent on page
Sources: https://devpost.com/software/caltrack-i0pq3n, evidence/sponsor-treehacks-treehacks-2026-caltrack.json

---

### Detour
*TreeHacks TreeHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [NVIDIA] Edge AI Track

**What it is:** An on-board satellite collision-avoidance assistant. A LangGraph-style pipeline of agents on a GX10 screens live TLE data for debris conjunctions, assesses risk, designs fuel-constrained avoidance burns and explains its reasoning, with deterministic SGP4 physics handling all orbital math.
**Problem / user:** Satellite operators and ground stations swamped by conjunction messages who cannot easily tell which need a maneuver.

**Features**
- Live conjunction screening — Ingests live TLEs, propagates 24 hours with SGP4 and ranks conjunction events. *[shown_working]*
- Maneuver planning — Planning agent evaluates several candidate burns and generates path-adjustment commands. *[claimed]*
- Safety validation — Checks burns against fuel budget, burn limits and mission horizon before execution. *[claimed]*
- Agent trace and audit log — Terminal panel shows each agent step as it screens, ranks and triages. *[shown_working]*
- Dashboard — NORAD ID lookup, live feed, constraint inputs and a 3D globe of orbit and debris, with simulation mode. *[shown_working]*
- Probabilistic debris modeling — Gaussian sampling models debris paths and a collision probability method is cited in the README. *[claimed]*

**Flow:** Open dashboard and look up a satellite by NORAD ID → Set fuel and burn constraints → Watch agents screen threats in the terminal trace → Review proposed maneuver → See orbit and debris on the globe or run simulation

**Prompt:** Edge AI track at TreeHacks 2026: build projects running AI on NVIDIA edge hardware; prizes include DGX Spark, Jetson Orin Nano Super and Brev credits. Detailed criteria not on overview page.
**Fit (explicit):** Runs a Nemotron 30B model with vLLM on an ASUS GX10 (DGX Spark class) to simulate an air-gapped, on-board satellite decision system without ground-station latency.  *(targeted: [NVIDIA] Edge AI Track)*
**Sponsor tools:** NVIDIA DGX Spark (ASUS GX10) (Local hosting of all agents, physics and visualization, core); NVIDIA Nemotron-3-Nano-30B (NVFP4) (Agent reasoning and maneuver triage via vLLM, core)
**AI:** Nemotron LLM agents (Scout, Analyst, Planner, Safety, Ops brief) decide and triage; all orbital math forced through a deterministic physics tool because the LLM guessed burn outcomes poorly.
**Architecture:** Next.js/Three.js dashboard; agent pipeline over a deterministic physics engine (SGP4, RK4, relative-motion dynamics) and a satellite fuel/power model, served from vLLM on the GX10.
**Novelty:** Frames debris avoidance as edge autonomy and keeps the LLM strictly on decisions with physics in tools; README labels it an honourable mention.
**Scope:** small · working: Two Vercel/Cloudflare demo links; no benchmarks or video. · polish: Architecture diagram in README, dashboard with globe; no tests.
**Claims:** Evaluates multiple maneuver candidates in seconds | Agents run in parallel on the GX10 without VRAM bottlenecks
**Gaps:** no video; no accuracy numbers
Sources: https://devpost.com/software/detour-64kpds, evidence/sponsor-treehacks-treehacks-2026-detour.json

---

### Sprout
*TreeHacks TreeHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [NVIDIA] Edge AI Track

**What it is:** A small gantry-style robotic garden. A camera on the gantry feeds a Jetson Nano that identifies each plant's species and health on-device, then Python scripts pump a calculated amount of water through a positioned nozzle.
**Problem / user:** No explicit user; aims to automate plant care with a companion-like robotic gardener.

**Features**
- Gantry camera sweep — Gantry moves a camera over the bed, streaming live video to the Jetson Nano. *[shown_working]*
- On-device plant identification — Custom edge model on the Jetson Nano identifies species offline. *[claimed]*
- Plant health assessment — Same model rates health in real time. *[claimed]*
- Calculated watering — Water volume derived from species and health, then pump triggered and nozzle positioned via GPIO/I2C and an Arduino. *[claimed]*
- Custom hardware build — Riveted metal frame, 3D-printed parts, custom motor and pump circuits. *[shown_working]*

**Flow:** Gantry moves camera over the bed → Jetson identifies plant and health → System computes water volume → Gantry aligns nozzle and pump delivers water

**Prompt:** Edge AI track at TreeHacks 2026: build projects running AI on NVIDIA edge hardware; prizes include DGX Spark, Jetson Orin Nano Super and Brev credits. Detailed criteria not on overview page.
**Fit (implied):** Vision inference for species and health runs fully offline on a Jetson Nano with CUDA, driving physical actuation.  *(targeted: [NVIDIA] Edge AI Track)*
**Sponsor tools:** NVIDIA Jetson Nano (On-device vision inference and control, core); CUDA (GPU acceleration for model, supporting)
**AI:** Custom vision model on the Jetson Nano for species and health; tags also list Qwen, Ollama and Claude without explaining their role.
**Architecture:** Camera on gantry to Jetson Nano running the model; Python scripts and an Arduino drive pump and gantry motors.
**Novelty:** Fully built mechanical gantry and electronics in one weekend, tying on-device vision to dosing water per plant; page gives conflicting 2-axis and 3-axis descriptions.
**Scope:** small · working: Gallery photo of a final working model and a YouTube demo link in README; no metrics. · polish: Poster image and README; small repo with no tests.
**Claims:** Health model runs entirely offline on the Jetson Nano | Reliable CNC-style gantry built from scratch in a weekend
**Gaps:** no accuracy or water-saving numbers; model details unclear; video not viewed
Sources: https://devpost.com/software/greenguardian-microfarm, evidence/sponsor-treehacks-treehacks-2026-sprout.json

---

### TORQ
*TreeHacks TreeHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [NVIDIA] Edge AI Track

**What it is:** A retrofit that makes a 2018 Honda Accord drive itself using a Jetson AGX Thor. NVIDIA's Alpamayo R1 reasoning model sets high-level plans and explains them in words, while a sunnypilot-derived control stack and a CAN adapter handle steering and speed. Riders dispatch the car from an iOS app.
**Problem / user:** Owners of older cars that cannot get self-driving, and riders who want rideshare pickup with explanations of the car's decisions.

**Features**
- Retrofit autonomy — Cameras to Thor to vision and policy models to controls, translated into CAN frames by a Red Panda adapter wired to the Honda. *[shown_working]*
- Reasoning layer — Alpamayo R1 (10.5B) takes wide and telephoto frames plus motion history and outputs plans and natural-language explanations. *[claimed]*
- Fast control layer — Vision at 20 Hz and control loop at 100 Hz keep lane and following distance even if reasoning stalls. *[shown_working]*
- iOS rideshare dispatch — Rider requests pickup; car and app exchange messages over an MQTT broker on Google Cloud. *[claimed]*
- Live reasoning feed and chat — App shows what the car sees, does and why; riders can question it or state route preferences. *[claimed]*
- Safety layers — Steering or brake override, driver attentiveness monitoring, and CAN frame range validation. *[claimed]*

**Flow:** Rider requests a pickup in the iOS app → Car drives to the rider with a safety driver aboard → App streams perception and reasoning during the ride → Rider asks questions or gives route feedback → Driver can override with wheel or brake

**Prompt:** Edge AI track at TreeHacks 2026: build projects running AI on NVIDIA edge hardware; prizes include DGX Spark, Jetson Orin Nano Super and Brev credits. Detailed criteria not on overview page.
**Fit (explicit):** All inference runs on a Jetson AGX Thor in the car: ONNX driving models on CUDA, Holoscan Sensor Bridge camera path, and Alpamayo R1 for reasoning.  *(targeted: [NVIDIA] Edge AI Track)*
**Sponsor tools:** NVIDIA Alpamayo R1 (High-level driving plans and explanations, core); NVIDIA Jetson AGX Thor (On-car compute for vision, policy and reasoning, core); Holoscan Sensor Bridge (Camera ingest into GPU memory, core); CUDA / JetPack (GPU inference and image preprocessing, supporting)
**AI:** Alpamayo R1 vision-language-action model for slow reasoning and explanation; openpilot-style ONNX vision and policy models for 20 Hz control; language output kept off the control path.
**Architecture:** Cameras via Holoscan into Jetson Thor; vision and policy models feed controlsd and pandad over CAN to the Honda; IMU and GPS feed localization; MQTT links car to the iOS app.
**Novelty:** Real-vehicle integration across NVIDIA, Lattice, comma.ai and Honda parts, pairing a slow reasoning model with a fast control loop and exposing explanations to riders.
**Scope:** large · working: README reports GPU pipeline latency (~8 ms per cycle); Devpost says car was integrated to drive with a safety driver; no video. · polish: Detailed hardware README, tests and Docker; repo is huge because it vendors a driving stack.
**Claims:** Driving pipeline about 8 ms total, within 50 ms budget (README) | Vision 20 Hz and control 100 Hz | Research prototype tested only with a safety driver
**Gaps:** no driving metrics or video; Alpamayo not shown running in README excerpt
Sources: https://devpost.com/software/torq, evidence/sponsor-treehacks-treehacks-2026-torq.json

---

