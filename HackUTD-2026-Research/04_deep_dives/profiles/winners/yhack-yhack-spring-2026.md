# YHack — YHack Spring 2026 (4 projects)

### Circa
*YHack YHack Spring 2026 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** First Place Overall [1st]; Societal Impact

**What it is:** Precision irrigation platform: ESP32 soil-moisture nodes report over ESP-NOW, a two-axis motorized turret aims a nozzle at specific field coordinates, and a React dashboard offers manual control, automated sweeps, drawn arc paths and ML next-day soil-moisture forecasts, plus a Kimi K2 chatbot that writes IFTTT rules.
**Problem / user:** Farmers with rectangular or irregular plots, where center-pivot systems miss corners and ignore soil variability; chatbot lowers the barrier for non-technical users.

**Features**
- Aimable turret — NEMA17 stepper yaw (TMC2209, 5:1 gear) and servo pitch aim at coordinates via polar-to-Cartesian math, pump and valve *[claimed]*
- Distributed soil sensor nodes — Capacitive moisture sensors on ESP32 nodes send zone readings over ESP-NOW; DHT11 gives ambient data *[claimed]*
- Live dashboard, configure and control pages — Socket.IO and MQTT stream data; register stations, joystick aim, pump bursts, e-stop *[claimed]*
- Three automated irrigation modes — Zone burst, full-plot sweep, custom arc path drawn on a field map; threshold-triggered targeting *[claimed]*
- Next-day soil moisture forecasts — XGBoost per spatial cluster with confidence intervals, irrigate-now-or-wait advice polled every 30 s *[claimed]*
- Natural-language automation chatbot — Kimi K2 converts multilingual requests into IFTTT workflows *[claimed]*
- Simulation versus live toggle and 3D field view — React Three Fiber demo without hardware *[claimed]*

**Flow:** Open dashboard to view stations and soil moisture → Register stations and nodes in Configure → Choose manual control or an Irrigate mode → Turret waters targeted zones → Check Prediction page for forecasts and advice

**Prompt:** YHack Spring 2026 (Yale's 12th): First/Second/Third Overall ($4k/$2k/$1k cash); Societal Impact (5 winners, ASUS Ascent GX10 supercomputer for 1st); Most Creative Hack (a 'useless prize'); Built With Zed (mentorship and credits). Hackers chose up to two of five tracks: Societal Impact, Personal AI Agents, Entertainment, Prediction Markets, Hardware.
**Fit (implied):** Water-waste problem for farming communities worldwide matches the Societal Impact and Hardware tracks; page cites worldwide accessibility.  *(targeted: First Place Overall, Societal Impact)*
**AI:** XGBoost (plus Random Forest, Optuna, SHAP) forecasts volumetric water content per cluster from a 224-row dataset and OpenWeatherMap; Kimi K2 LLM turns language into IFTTT rules.
**Architecture:** ESP32 nodes -> ESP-NOW -> base station -> MQTT (Mosquitto) -> Node/Express with Socket.IO -> React/Vite dashboard; FastAPI predictor with MLflow and PostgreSQL via Docker Compose; turret on SoftAP HTTP.
**Novelty:** Replaces fixed pivot geometry with a single targeted turret plus sensor mesh, ML forecasting and chat-based rule creation, with a hardware-free simulation mode.
**Scope:** large · working: Live site circaorg.github.io, video embed and detailed hardware list; no field measurements; repo not linked. · polish: Multi-page UI, 3D visualization, Docker Compose stack; known gaps (Supabase inconsistency, in-memory predictor data).
**Claims:** 90% water saving figure is for pivot vs flood irrigation, not measured for Circa
**Gaps:** No repository linked or read; Demo site and video not opened
Sources: https://devpost.com/software/circa-u1fsx5, https://yhack-2026.devpost.com/

---

### GaitGuard
*YHack YHack Spring 2026 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Third Place Overall [3rd]; Built With Zed

**What it is:** Three-unit wearable (shin, ankle, foot) with ESP32 IMUs streaming to a Raspberry Pi 5 on QNX. A per-patient LSTM learns the therapist-shown movement, predicts the correct continuation of each rep, scores deviation as a 0-100 Gait Health Score and triggers haptic vibration patterns.
**Problem / user:** Outpatient physical-therapy patients doing home rehab who lose consistency and get little feedback after leaving the clinic.

**Features**
- Personalized digital twin of correct movement — Two-layer PyTorch LSTM trained only on the patient's calibration reps after rep segmentation, 6 Hz filtering and normalization *[claimed]*
- Real-time haptic feedback — ESP32 vibrates with distinct patterns for error types when predicted and actual data diverge *[claimed]*
- Gait Health Score 0-100 — Compared per time step; alert when below clinical threshold *[claimed]*
- Joint angle estimation — Complementary filter (alpha 0.98) fuses accelerometer and gyro for shin, ankle, foot *[claimed]*
- Custom 3D-printed wearable hardware — SolidWorks enclosures, LiPo packs, 1.69 inch touch display on foot unit *[claimed]*
- Live sensor preview page — Served from the Raspberry Pi *[claimed]*
- On-device inference, therapist dashboard — Listed next steps *[planned]*

**Flow:** Therapist demonstrates the movement → Patient performs clean reps to calibrate → System builds the personal LSTM → During reps it predicts the correct remainder and scores deviation → Haptic pattern fires if the score drops

**Prompt:** YHack Spring 2026 (Yale's 12th): First/Second/Third Overall ($4k/$2k/$1k cash); Societal Impact (5 winners, ASUS Ascent GX10 supercomputer for 1st); Most Creative Hack (a 'useless prize'); Built With Zed (mentorship and credits). Hackers chose up to two of five tracks: Societal Impact, Personal AI Agents, Entertainment, Prediction Markets, Hardware.
**Fit (implied):** Hardware-track wearable for healthcare; page tags Zed and Claude though use is not described.  *(targeted: Third Place Overall, Built With Zed)*
**Sponsor tools:** Zed (Listed as built-with for the Built With Zed prize; role not described, unclear); QNX (OS on the Raspberry Pi hub, supporting)
**AI:** Per-patient stacked LSTM in PyTorch predicts the correct continuation of sensor sequences; deviation from prediction yields the GHS.
**Architecture:** Three ESP32 IMU units sample 50 Hz over WiFi to a Raspberry Pi 5 (QNX) running Python calibration and inference; commands return to the ESP32 haptic motor.
**Novelty:** Personalizes the movement model from a handful of reps instead of population norms and closes the loop with wearable haptics.
**Scope:** medium · working: Page says pipeline runs end to end from IMU to haptics; repo not readable; no video link. · polish: Custom printed enclosures press-fit on first print; no accuracy or clinical data.
**Claims:** Pipeline runs end to end with immediate in-rep haptic feedback | Enclosures press-fit on first print
**Gaps:** Repo clone failed and GitHub not fetchable; README unread; Demo video mentioned but not linked
Sources: https://devpost.com/software/gaitguard, https://yhack-2026.devpost.com/

---

### HandFlow - Smart Glasses For Productivity
*YHack YHack Spring 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best First Hack

**What it is:** HandFlow turns a cheap head-mounted camera into an input system: on-screen and origami paper macro pads, knuckle hotkeys, seven mid-air gestures, a virtual touchscreen via ArUco, and Gemini-assisted screen capture.
**Problem / user:** Heavy computer users repeating menu actions; macropads are costly.

**Features**
- Gesture recognition — MediaPipe 21 landmarks to 96 features to TCN, 16 classes, ~5 ms. *[shown_working]*
- Paper macro pad — Folded A4 with 24 buttons tracked via ArUco. *[shown_working]*
- Virtual touchscreen — ArUco calibration makes non-touch display respond. *[shown_working]*
- Knuckle buttons — Seven hotkeys by palm orientation. *[claimed]*
- Live capture with Gemini — Pinch selects region, copies to clipboard, Gemini suggests actions. *[claimed]*

**Flow:** Mount camera → Raise hand for on-screen pad → Use paper pad or knuckles → Gesture or pinch capture → Configure in GUI

**Prompt:** not public / not found
**Fit (none):** No stated link.  *(targeted: Best First Hack)*
**Sponsor tools:** Akash GPU cloud (model training in Docker, supporting); Gemini 2.5 Flash (visual understanding of capture, supporting)
**AI:** Self-built dataset, TCN gesture classifier on CPU, Gemini for captured content.
**Architecture:** Webcam to MediaPipe/OpenCV to TCN to actions; NiceGUI and CustomTkinter UI.
**Novelty:** Multi-input system from one camera including paper macro pad.
**Scope:** medium · working: Two YouTube demos (V1, V2) in README; 18k LOC. · polish: Detailed README; no tests.
**Claims:** Sub-5 ms inference | ~$5 camera | Real-time on CPU
**Gaps:** No prize text found; Devpost lacks demo video; README has two
Sources: https://devpost.com/software/handflow, evidence/yhack-yhack-spring-2026-handflow-smart-glasses-for-productivity.json

---

### LifeSaver
*YHack YHack Spring 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Second Place Overall [2nd]; Most Creative Hack

**What it is:** Browser 3D operating-room simulator where webcam hand tracking (MediaPipe) moves surgical instruments. Learning mode has Gemini explain clicked organs aloud via ElevenLabs; Practice mode guides a gallbladder-removal run with AI coaching; sessions are scored as 32-dimensional vectors to track progress.
**Problem / user:** Medical students and residents with minimal hands-on practice time; page says simulators cost over $100,000 and give about 30 minutes per semester.

**Features**
- 3D operating room in the browser — React Three Fiber scene with table, instruments, doctor and skeleton; needs only laptop and webcam *[claimed]*
- Learning mode with spoken organ explanations — Click an organ to highlight it; Gemini text via ElevenLabs voice; voice follow-up questions answered *[claimed]*
- Practice mode for laparoscopic cholecystectomy — Instrument prompts, glowing target zones, danger-zone warnings, real-time AI coaching *[claimed]*
- Webcam hand tracking — MediaPipe maps hand positions to instrument control *[claimed]*
- Surgery mode on organs — Heart, kidney, digestive system with tighter zones *[claimed]*
- Performance vectors and progress comparison — 32-dim fingerprint of speed, choices, danger entries; cosine similarity against history *[claimed]*
- Instructor mode, more procedures, Atlas Vector Search — Listed next steps *[planned]*

**Flow:** Open site and allow webcam → Explore the operating room → Click organs for voice lessons → Start a practice run and follow prompts with hand movements → Review session vector and past-session comparison

**Prompt:** YHack Spring 2026 (Yale's 12th): First/Second/Third Overall ($4k/$2k/$1k cash); Societal Impact (5 winners, ASUS Ascent GX10 supercomputer for 1st); Most Creative Hack (a 'useless prize'); Built With Zed (mentorship and credits). Hackers chose up to two of five tracks: Societal Impact, Personal AI Agents, Entertainment, Prediction Markets, Hardware.
**Fit (none):** Healthcare education simulator; page does not name tracks or prizes targeted.  *(targeted: Second Place Overall, Most Creative Hack)*
**Sponsor tools:** ElevenLabs (Spoken organ explanations and coach replies, core); MongoDB Atlas (Session storage; vector search planned, supporting)
**AI:** Gemini 2.5 Flash generates coaching tips, organ explanations and answers to voice questions; MediaPipe hand tracking; custom 32-d performance embeddings with cosine similarity.
**Architecture:** React 19/Vite with React Three Fiber on the client; Gemini and ElevenLabs services; Express/Node backend with MongoDB Atlas stores sessions and vectors.
**Novelty:** Zero-hardware surgical practice with hand-tracked instruments, voice tutor and longitudinal skill vectors in a web page.
**Scope:** large · working: Repo about 12k lines with tests and docs folder; four gallery screenshots; no video or live link on Devpost. · polish: README has env setup and service docs; API keys exposed client-side by design for prototype.
**Claims:** Simulators cost over $100,000 each | Medical errors third leading cause of death (unsourced)
**Gaps:** No demo video; Hand-tracking accuracy not evidenced
Sources: https://devpost.com/software/lifesaver-lnm0tz, https://github.com/akhilm2223/yale (evidence file README), https://yhack-2026.devpost.com/

---

