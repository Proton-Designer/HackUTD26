# NMIT Hacks — NMIT HACKS 2025 (3 projects)

### AirCommand
*NMIT Hacks NMIT HACKS 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Third Prize [3rd]

**What it is:** A webcam-only hand-gesture controller that recognises gestures in real time with OpenCV and maps them with PyAutoGUI to actions in slideshows, media players and the camera. Tagline: control your world with hand gestures.
**Problem / user:** Touch-based control of presentations, media and cameras is inconvenient and less hygienic; aimed at classrooms, kitchens, gyms and hands-busy settings.

**Features**
- Presentation control — Gestures trigger slide navigation commands sent to the foreground app. *[claimed]*
- Media playback control — Gestures mapped to play, pause and similar media actions. *[claimed]*
- Camera functions — Gestures operate camera actions such as capture. *[claimed]*
- Webcam-only recognition — Python and OpenCV detect hand gestures in real time with no extra hardware. *[claimed]*
- Extensible gesture mapping — New gestures can be added and linked to software actions through PyAutoGUI. *[claimed]*

**Flow:** Webcam captures the hand → Gesture is recognised → PyAutoGUI sends the mapped command to the target app

**Prompt:** not public / not found
**Fit (implied):** Page states Open Innovation track; project offers a general-purpose touch-free interface and suggests VR, healthcare and smart-home extensions.  *(targeted: Open Innovation track, Third Prize)*
**AI:** Computer-vision gesture recognition with OpenCV; no trained model or MediaPipe use is confirmed on the page.
**Architecture:** Webcam frames to Python/OpenCV recognizer, then PyAutoGUI keystroke or mouse automation. Flask, React and Node.js appear in tags without a described role.
**Novelty:** Common hackathon pattern (gesture to keyboard shortcut); selling point is zero extra hardware and user-extensible mappings.
**Scope:** small · working: Only text on Devpost; no demo, video or readable repo. · polish: Page lists detailed challenges (lighting, latency, false detections) but no visuals.
**Claims:** Real-time, low-cost gesture control with a standard webcam | Works across multiple applications
**Gaps:** Repo exists but README unreadable (fetch failed, clone failed); Which gestures exist is not listed; Roles of Flask/React/Node unknown; Track descriptions not published
Sources: https://devfolio.co/projects/aircommand-c16d, https://nmithacks25.devfolio.co/

---

### ANTI-TAPP
*NMIT Hacks NMIT HACKS 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Second Prize [2nd]

**What it is:** An ESP32-based unit for electric poles that measures voltage and current, computes power, compares use to expected profiles and sounds a buzzer when current exceeds a threshold, with event logging toward a central system.
**Problem / user:** Illegal power tapping from poles causes utility revenue loss and unfair billing; utilities currently rely on manual pole inspection.

**Features**
- Voltage and current sensing — Sensors on the ESP32 read line voltage and current; current sensor calibrated against a multimeter. *[claimed]*
- Power calculation — Firmware computes consumption from the readings. *[claimed]*
- Expected-usage comparison — Readings compared to expected profile to flag anomalies. *[claimed]*
- Buzzer alarm — Buzzer sounds when current passes a set threshold. *[claimed]*
- Event logging to central system — Events logged or sent upstream; page lists cloud integration as a challenge. *[unclear]*
- OLED display — Planned local readout; page says it was unresponsive during development. *[unclear]*

**Flow:** Sensors measure pole voltage and current → Device calculates power → Compare against expected usage → Buzzer sounds above threshold → Event logged or sent for investigation

**Prompt:** not public / not found
**Fit (implied):** Page states IoT track; hardware sensing node for utility theft detection.  *(targeted: IoT track, Second Prize)*
**AI:** none
**Architecture:** ESP32 with voltage and current sensors, OLED and buzzer, programmed in Arduino IDE; optional upstream link to a central monitor.
**Novelty:** Targets a regionally relevant utility-theft problem with low-cost embedded sensing rather than software only.
**Scope:** tiny · working: Devpost says a working hardware demo was built; repo contains only a README stub and no code. · polish: Honest challenge list; no video, images or code published.
**Claims:** Built a working hardware demonstration | Current sensor calibrated with a multimeter
**Gaps:** Repo has no code (named Vivid-Connect); No images or video; Threshold values and logging transport unspecified
Sources: https://devfolio.co/projects/antitapp-7bfb, evidence/nmit-hacks-nmit-hacks-2025-anti-tapp.json (README is a one-line title only), https://nmithacks25.devfolio.co/

---

### Medivision
*NMIT Hacks NMIT HACKS 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** First Prize [1st]

**What it is:** A web platform where users upload X-ray, ultrasound, CT or MRI scans and get an AI-generated plain-language report with confidence scores, a downloadable PDF, a chat to question the report, and a map-based search for nearby doctors.
**Problem / user:** Radiologist shortages and slow scan reads leave patients, especially in remote areas, waiting and confused by technical reports.

**Features**
- Multi-modality upload — Accepts X-ray, ultrasound, 2D/3D CT and 3D MRI; DICOM, PNG, JPG and NIfTI are preprocessed before inference. *[shown_working]*
- Per-modality prediction routes — FastAPI endpoints for xray, ct 2d/3d, mri 3d and ultrasound run pretrained vision models (timm/Torch). *[claimed]*
- LLM report generation — Gemini Pro turns model output into a structured report per modality, with confidence scores and next steps. *[shown_working]*
- Chat with report — Users ask follow-up questions about their report answered by Gemini. *[claimed]*
- PDF export — Report exported as branded PDF with watermark from the frontend. *[claimed]*
- Doctor search — Leaflet map and geopy-based location search for nearby doctors. *[claimed]*
- Accounts — Clerk-based sign-in on the frontend. *[claimed]*

**Flow:** Sign in and open upload page → Upload a scan → Backend preprocesses and runs the modality model → Read the plain-language report with confidence → Chat about the report or download PDF → Find nearby doctors on the map

**Prompt:** not public / not found
**Fit (explicit):** Devpost says it applied to AI and ML and Gemini API tracks; Gemini generates reports and powers report chat over computer-vision predictions.  *(targeted: AI & ML track, Gemini API track, First Prize)*
**Sponsor tools:** Gemini API (Gemini Pro) (Report writing and chat with report in backend, core)
**AI:** Pretrained image models per modality produce findings; Gemini Pro writes the report and answers questions. Devpost says fast.ai; README says PyTorch/timm.
**Architecture:** React/Vite/Tailwind frontend with Clerk and Leaflet; FastAPI backend with PyTorch, pydicom and OpenCV inference, Gemini calls and geopy doctor lookup; sample_reports folder.
**Novelty:** Covers four imaging types in one flow and adds report chat and doctor lookup; no accuracy evaluation is shown.
**Scope:** medium · working: README gives API routes, UI preview images and sample reports; about 6,900 lines; no live demo or video. · polish: README with screenshots, tests and Docker present; polished UI components via ShadCN.
**Claims:** Accurate diagnostics with user-friendly results (no metrics given)
**Gaps:** Devpost says fast.ai and Node.js; README says PyTorch/timm, Gemini Pro, Clerk; feature list follows README; Model names and training data not given; No accuracy figures
Sources: https://devfolio.co/projects/medivision-31e0, evidence/nmit-hacks-nmit-hacks-2025-medivision.json (README), https://nmithacks25.devfolio.co/

---

