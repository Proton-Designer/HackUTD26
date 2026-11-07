# Hack the Valley — Hack the Valley 11 (3 projects)

### Premiere
*Hack the Valley Hack the Valley 11 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 3rd Place Prize [3rd]; Hack the Valley x School of Cities

**What it is:** Rover-plus-iPhone building inspection system: a mission map picks low-scoring Toronto apartment buildings and plans a route, a Raspberry Pi car drives a path with an iPhone LiDAR scan at each stop, and a browser studio turns scans into measurable 3D point clouds and splats.
**Problem / user:** City building inspectors and firefighters facing dangerous, slow inspections of deteriorating or abandoned buildings.

**Features**
- Mission map — Shows 557,694 Toronto building outlines colored by evaluation score and plans a walking route to the lowest scores. *[shown_working]*
- Replay and telemetry — Scrubbable mission log with trail and battery, signal, speed and scan progress card. *[shown_working]*
- LiDAR import — Backend removes pose spikes, filters floating points and thins clouds from LOTA app captures. *[claimed]*
- Gaussian splats — Trains photoreal splats with Brush and views them via SparkJS. *[claimed]*
- Inspection tools — Two-point measure and 3D-pinned notes with evidence photos. *[claimed]*
- Proposed building preview — Procedural house placed in the scan with the old building cut out. *[claimed]*
- Rover control — Draw a path on laptop, Pi runs it open-loop after cable unplug, with calibration tools. *[claimed]*
- Autonomy, damage detection, soil sensing — Listed future work. *[planned]*

**Flow:** Open the mission map → Pick buildings and route → Rover drives to a stop → iPhone scans with LiDAR → Import into the capture studio → Measure, annotate and preview a proposed building

**Prompt:** Hack the Valley x School of Cities: civic tech for a real Toronto urban problem using Toronto data, not predicting elections. Overall prizes judged on technicality, design, impact, presentation, inspiration and authenticity.
**Fit (implied):** Uses Toronto building outlines and apartment evaluation scores to prioritize inspection routes, directly supplying the civic data the School of Cities track requested; listed as a prize.  *(targeted: 3rd Place Prize [3rd], Hack the Valley x School of Cities)*
**AI:** Gaussian splat training with Brush; no LLM damage detection (listed as future).
**Architecture:** Toronto datasets feed a React/MapLibre mission map; Pi rover and iPhone LOTA capture upload to a FastAPI backend that cleans clouds and trains splats; Three.js/SparkJS studio.
**Novelty:** Hardware rover linked to civic open data, scan processing and a design-proposal viewer in one pipeline.
**Scope:** large · working: Repo about 8.6k lines with tests and synthetic fixtures; README says backend and build tests passed; demo video. · polish: Detailed README with mermaid diagram and docs; Devpost admits limits of reconstruction accuracy.
**Claims:** 557,694 Toronto building outlines loaded | Reconstruction is not engineering-grade measurement (stated)
**Gaps:** Autonomous navigation not built; Devpost frames inspections of abandoned houses while README frames apartment survey; Starter code credited to Project Spark; Rover tail of README not read
Sources: https://devpost.com/software/estate-o-bot, https://github.com/Vedthakar/HTV11, evidence/hack-the-valley-hack-the-valley-11-premiere.json, https://hack-the-valley-11.devpost.com/

---

### Pyrosense
*Hack the Valley Hack the Valley 11 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** 1st Place Prize [1st]

**What it is:** Helmet-mounted sensing unit for firefighters that maps a building with LiDAR SLAM, tracks position and logs VOC readings, feeding a live 3D dashboard where an incident commander sees gas heat maps and unsampled areas.
**Problem / user:** Firefighters entering smoky unfamiliar buildings, and incident commanders lacking a shared picture of hazards.

**Features**
- Live gas heat map — VOC readings tied to position are streamed into TimescaleDB and rendered as a floor-painted field. *[claimed]*
- SLAM mapping and localization — LiDAR with ROS 2 builds layout and tracks indoor position, IMU rejects tilted scans. *[claimed]*
- Alerts — Visual and audible warnings for rising gas or high-hazard zones. *[claimed]*
- Commander markers — One-click victims, fire, blocked exits and entry points. *[claimed]*
- Views and replay — Overhead and first-person, follow mode, exposure history and time-range replay. *[claimed]*
- Unsampled-area identification — Highlights regions without readings. *[claimed]*
- Gaussian-process gas prediction — Short-term hazard prediction and source estimation need more tuning. *[claimed]*
- mmWave radar and thermal fusion — Future. *[planned]*

**Flow:** Helmet unit builds map as firefighter walks → Pi streams readings over Tailscale → Backend makes heat map → Commander views dashboard → Firefighter gets alerts

**Prompt:** Hack the Valley 11 overall first place (Pixel 10a) judged on technicality, design, impact, presentation, inspiration, authenticity; Tiger Data and Vultr were MLH sponsor tracks.
**Fit (none):** No stated prize targeting; sponsor stack (Tiger Cloud, Vultr, Tailscale) is used in deployment, though no sponsor track is claimed.  *(targeted: 1st Place Prize [1st])*
**Sponsor tools:** Tiger Cloud (TimescaleDB) (stores readings and generates heat map, core); Vultr (VM hosting backend and dashboard, supporting); Tailscale (secure Pi-to-backend stream, supporting)
**AI:** Gaussian process regression for gas concentration mapping and short-term prediction; no LLM.
**Architecture:** Raspberry Pi 5 with LiDAR, IMU and VOC sensor streams to FastAPI on Vultr via Tailscale; TimescaleDB heat map; three.js dashboard behind nginx in Docker Compose.
**Novelty:** Full hardware-to-dashboard stack with SLAM and gas field modeling aimed at a first-responder workflow.
**Scope:** medium · working: Project site and sensor hardware prototype described with latency numbers; no repo or video found. · polish: Landing page, five screenshots, single deploy script.
**Claims:** Pi-to-frontend latency cut by 50% | Traffic reduced about 10x by sending only new readings | Wearable prototype works in real time
**Gaps:** No repo linked; No demo video linked; Landing site not opened; Prediction accuracy not given
Sources: https://devpost.com/software/pyrosafe, https://hack-the-valley-11.devpost.com/

---

### Soundscape
*Hack the Valley Hack the Valley 11 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 2nd Place Prize [2nd]

**What it is:** System that captions meaningful non-speech sounds (door slam, siren, glass break) as timed WebVTT by first classifying each scene's environment from frames and audio, then reweighting sound detections, with a local dashboard and a YouTube Chrome extension.
**Problem / user:** Deaf and hard-of-hearing viewers who miss non-speech sound information in video.

**Features**
- Environment classification — PySceneDetect shots scored by SigLIP and CLAP; low confidence falls back to general. *[shown_working]*
- Environment-conditioned sound detection — PANNs CNN14 windows reweighted by per-environment priors with an always-on safety set. *[shown_working]*
- Speech masking — Silero VAD separates speech regions. *[shown_working]*
- Caption output — Writes WebVTT/SRT and can merge with supplied speech subtitles. *[shown_working]*
- Local backend and dashboard — FastAPI endpoints for upload, status, video and captions. *[claimed]*
- Chrome extension — Overlays synchronized captions and direction waves on YouTube. *[claimed]*
- Evaluation harness — Event F1 and false positives per minute on AudioSet with Optuna tuning. *[shown_working]*
- Smart-glasses live feed and mobile app — Future. *[planned]*

**Flow:** Upload a video or open YouTube → System extracts audio and frames → Environment inferred per shot → Sounds detected and filtered → Captions appear with direction hints

**Prompt:** Hack the Valley 11 overall second place (keyboard) judged on technicality, design, impact, presentation, inspiration, authenticity.
**Fit (none):** No stated prize targeting; an accessibility tool entered for overall places.  *(targeted: 2nd Place Prize [2nd])*
**AI:** Pretrained PANNs CNN14, SigLIP, CLAP and Silero VAD with environment priors and thresholding; precision-first post-processing; baseline vs conditioned comparison.
**Architecture:** ffmpeg extraction feeds environment classifier then event detector; YAML configs and versioned JSON contracts; FastAPI server and MV3 extension display captions.
**Novelty:** Uses scene context to filter noisy sound detectors and measures the effect with baseline versus conditioned runs.
**Scope:** large · working: About 28k lines, tests and CI, evaluation harness; README documents pipeline; demo video. · polish: Docs folder, AGENTS.md, config-driven design.
**Claims:** Recognizes 500+ sounds | A dozen environment presets | All processing runs locally
**Gaps:** No accuracy results on Devpost; README setup section truncated; Claude, Codex and Gemini tags with no stated use
Sources: https://devpost.com/software/sound-thing, https://github.com/soundthing/Soundscape, evidence/hack-the-valley-hack-the-valley-11-soundscape.json, https://hack-the-valley-11.devpost.com/

---

