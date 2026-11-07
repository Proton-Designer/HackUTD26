# Knight Hacks — Knight Hacks IX (2025) (3 projects)

### Farsight
*Knight Hacks Knight Hacks IX (2025) · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** NVIDIA: Best Use of Jetson Nano; Hugging Face: Best Use of Open Source AI; Full Sail: Pathways & Perception, A Serious Games & Simulation Challenge; Encompass: Data Capturing Hardware

**What it is:** A rescue rover driven from a Meta Quest headset that carries a LiDAR iPhone and a Jetson Orin Nano, detects people and answers questions with local models, then builds a walkable Gaussian-splat reconstruction of the room with face sightings linked back to camera frames.
**Problem / user:** Search-and-rescue responders who need to inspect an unfamiliar room before entering; also usable for search training.

**Features**
- VR rover driving and autonomous Explore — Quest shows live camera; joystick drives manually, A button starts Nav2 autonomous exploration, B stops. *[shown_working]*
- Onboard person and face detection — YOLO11n-pose on Jetson via TensorRT; face boxes derived from head keypoints. *[shown_working]*
- Local voice and vision assistant — Qwen3-VL-2B, Whisper and Piper answer typed or spoken questions about the live view in English and Spanish. *[shown_working]*
- Mission report — Encounter snapshots plus draft SBAR notes written by the vision-language model for responder review. *[shown_working]*
- Post-run Gaussian-splat room — Mac trains Brush on posed photos seeded with LiDAR points; about 114 seconds on a 60-second sample. *[shown_working]*
- Browser and Quest walkthrough with face pins — Minimap shows route and pins; clicking a pin jumps to its viewpoint and shows the boxed source frame. *[shown_working]*

**Flow:** Put on Quest and see rover camera → Drive manually or press A for Explore → Perception flags people and logs snapshots → Ask the assistant about the view → After the run, Mac builds the splat room → Review walkthrough and click face pins to see original frames

**Prompt:** NVIDIA Best Use of Jetson Nano: projects making use of a Jetson Nano-class edge device; the overview gives only the prize listing. Hugging Face, Full Sail and Encompass track text not found.
**Fit (explicit):** Runs rover server, perception and speech/vision models on a Jetson Orin Nano using open Hugging Face models; captures data hardware for reconstruction.  *(targeted: NVIDIA Best Use of Jetson Nano, Hugging Face Best Use of Open Source AI, Full Sail Pathways & Perception, Encompass Data Capturing Hardware)*
**Sponsor tools:** NVIDIA Jetson Orin Nano / TensorRT (onboard camera, detection, rover server and local models, core); Hugging Face open models (Qwen3-VL, Whisper, Piper) (local vision-language, speech-to-text and voice output, core)
**AI:** Local models: YOLO11n-pose for people, Qwen3-VL-2B via llama.cpp for answers and SBAR drafts, Whisper base.en for speech, Piper for voices, plus Brush Gaussian-splat training.
**Architecture:** ELEGOO rover with Arduino motor control, iPhone LiDAR and Jetson FastAPI server (ROS 2 Nav2, perception) streaming to a WebXR Quest relay; a Mac pulls captures and trains the splat for browser and Quest viewers.
**Novelty:** Chains VR teleoperation, autonomy, local AI and 3D reconstruction with evidence-linked face pins across several devices; far larger than typical hackathon scope.
**Scope:** large · working: Demo video and timing measurements; about 135k LOC across 906 files with tests, Docker and CI. · polish: Detailed README with hero art, architecture and run guide; docs folder and diagrams.
**Claims:** Won four sponsor tracks of 212 projects | About 114 seconds to build room and face evidence locally on 60-second sample | Integrated headset driving, onboard perception, autonomy and mission evidence in one prototype
**Gaps:** Hugging Face, Full Sail, Encompass prompts not found; video not viewed
Sources: https://devpost.com/software/farsight-t4qyli, https://github.com/azizu06/farsight

---

### Fireline
*Knight Hacks Knight Hacks IX (2025) · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** NVIDIA: Best Use of Jetson Nano; OneEthos: Innovation for Good

**What it is:** A wildfire early-warning system of tree-mounted camera units that detect smoke on a Jetson, are woken by an ESP32 weather sensor, and send a tiny satellite-sized alert packet to a hosted crew console with map, incidents and AI summaries.
**Problem / user:** Ground crews and land managers covering remote forest with no power, cell signal or watchers, where satellites revisit too rarely to catch small fires; cites Florida wildfire statistics.

**Features**
- On-device smoke detection — Pyronear YOLO model on Jetson via TensorRT; smoke must show in 4 of last 6 frames. *[shown_working]*
- Weather-gated scanning — ESP32 with DHT11 sets fire-risk tier and wakes Jetson over MQTT at 30-minute, 5-minute or continuous intervals. *[shown_working]*
- 340-byte satellite alert packet — Unit builds a compact packet sized for Iridium bursts (178 bytes measured); images never sent; simulated link adds delay and drops. *[shown_working]*
- Interest score — Confidence times smoke-frame fraction times fire-weather weight; alert at 0.5. *[claimed]*
- Live fleet console — React/Leaflet map with unit states, alarms, notifications, weather charts and packet log. *[shown_working]*
- Incident grouping and AI summaries — Alerts group into incidents; template summary shown instantly, Gemma 3 4B rewrites and double-checks the crop. *[shown_working]*
- Out-of-order packet handling — Newest packet sets unit state; duplicates identified by unit, counter and timestamp. *[claimed]*

**Flow:** Lower humidity at the sensor with a hair dryer → LED changes and Jetson starts scanning → Hold smoke video up to the camera → Console alarm sounds and map flies to unit → Alert card shows packet and plain-language summary

**Prompt:** NVIDIA Best Use of Jetson Nano: projects making use of a Jetson Nano-class edge device; overview gives only prize listing. OneEthos Innovation for Good text not found.
**Fit (explicit):** Runs the smoke-detection model on a Jetson Orin Nano at the edge so only a small verdict leaves the device; wildfire detection as social good.  *(targeted: NVIDIA Best Use of Jetson Nano, OneEthos Innovation for Good)*
**Sponsor tools:** NVIDIA Jetson Orin Nano / TensorRT (on-device smoke detection, core); Hugging Face (Pyronear model, Gemma 3) (pretrained smoke model and local summary LLM, supporting)
**AI:** Pretrained Pyronear YOLO smoke model run on Jetson without extra training; Gemma 3 4B via Ollama writes incident summaries and a second opinion on the smoke crop.
**Architecture:** DHT11 to ESP32 to MQTT to Jetson detector, then a 340-byte packet over a simulated satellite link to a FastAPI/SQLite ground station on an Azure VM, pushed by WebSocket to a React console.
**Novelty:** Designs around a satellite byte budget and sleeping-edge power pattern; ties weather sensing to inference scheduling. Satellite link and most fleet are simulated.
**Scope:** medium · working: Hosted site fire-line.tech, demo steps with real hardware, 69 files and about 4.3k LOC, Docker used. · polish: README with badges and website; docs folder; team states false-alarm rate and range were not measured.
**Claims:** Smoke event packet measured at 178 bytes against a 340-byte limit | Satellite link and most fleet are simulated, false-alarm rate unmeasured
**Gaps:** OneEthos prompt not found; no video
Sources: https://devpost.com/software/fireline-764nir, https://github.com/kateye31/fireline

---

### Permanence
*Knight Hacks Knight Hacks IX (2025) · dataset: sponsor · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall Hack [1st]; NVIDIA: Best Use of Jetson Nano; Hugging Face: Best Use of Open Source AI

**What it is:** A rover that keeps persistent 3D memory of objects on a Jetson Orin Nano, tracking them even when hidden under cups, and driving to a target chosen by a plain-language request through a 3D vision-language model.
**Problem / user:** Robotics builders: robot perception forgets objects once occluded or carried away; goal is object permanence, later assistive robots and finding lost items.

**Features**
- Autonomous table scan — Rover turns, stops, captures keyframes from an iPhone LiDAR feed and builds a 3D scene. *[shown_working]*
- Natural-language target grounding — Quantized Qwen-3D reads 18 views and resolves requests like the cup next to the green ball in about 4.5 s with a confidence score. *[shown_working]*
- Occlusion-aware 3D tracking — YOLOE TensorRT detector at 15 fps plus a custom 3D tracker treats a ball under a cup as moving with it. *[shown_working]*
- Navigation to remembered object — Rover plans a route around other cups to a target no camera sees. *[shown_working]*
- Shell-game demo — Cups shuffled, robot guesses, cup lifted to verify the answer. *[shown_working]*
- Live 3D dashboard and voice — Three.js view of seen versus remembered objects, X-ray through cups, map, Jetson memory; Chrome speech commands. *[shown_working]*
- Rover self-calibration — Measures speed to tune motor power, auto-stops, detects swapped left/right motors. *[claimed]*

**Flow:** Cover colored balls with cups on a table → Rover scans and builds 3D memory → Shuffle cups and ask a question by text or voice → Model selects the target with confidence → Say drive and rover plans a route to it → Lift cup to verify

**Prompt:** NVIDIA Best Use of Jetson Nano: projects making use of a Jetson Nano-class edge device; overview gives only prize listing. Best Overall and Hugging Face prompts not found.
**Fit (explicit):** Runs a 3B vision-language model and real-time tracker on one 8 GB Jetson Orin Nano with custom quantization and a memory handoff; README claims 1st place in all three.  *(targeted: Best Overall Hack, NVIDIA Best Use of Jetson Nano, Hugging Face Best Use of Open Source AI)*
**Sponsor tools:** NVIDIA Jetson Orin Nano / TensorRT (all perception, language, memory and visualization, core); Hugging Face open models (Qwen-3D, YOLOE) (language grounding and open-vocabulary detection, core)
**AI:** Qwen-3D (3B 3D vision-language model, self-quantized to 4.5 GB) grounds the request once then exits; YOLOE in TensorRT FP16 tracks continuously; a custom 3D tracker keeps identities through occlusion.
**Architecture:** iPhone LiDAR via Record3D to Jetson: scene capture, one-shot Qwen-3D grounding, YOLOE tracking, world-state memory, planner to Arduino motors; Three.js dashboard; Pico W head steering.
**Novelty:** Two-stage understand-once, track-continuously design with explicit world state fitted into 8 GB memory; custom quantization and shell-game verification test.
**Scope:** large · working: Screenshots including dashboard, tests present, no-hardware quick start; about 19.6k LOC, 614 files; no video link. · polish: Paper-style README with contents, performance and limitations sections; benchmarks and citation.
**Claims:** Qwen-3D reduced from 7.1 GB to 4.5 GB | Full run peaks at about 6.1 of 7.4 GB | Language selection about 4.5 s; tracker 15 fps with 22 MB engine
**Gaps:** Best Overall and Hugging Face prompts not found; shell-game accuracy not reported
Sources: https://devpost.com/software/permanence, https://github.com/billpquach/permanence

---

