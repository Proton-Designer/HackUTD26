# ShellHacks — ShellHacks 2026 (1 projects)

### Halo
*ShellHacks ShellHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner State Farm

**What it is:** A smart bike helmet built on a Raspberry Pi 5 with a rear camera and side ultrasonic sensors that tracks vehicles approaching from behind and warns the rider by display, spatial audio, voice and haptics. Gemini writes incident reports off the safety path; an iOS app shows a live 3D rear view.
**Problem / user:** Cyclists, especially in high-risk states like Florida, who cannot see traffic behind them.

**Features**
- On-device vehicle detection and tracking — YOLO26n via NCNN on the Pi estimates time-to-contact from bounding-box growth *[claimed]*
- Side-sensor fusion — Ultrasonic sensors measure close-pass clearance after a car leaves camera view *[claimed]*
- Multi-channel alerts — OLED arrow, panned earbud beep, spoken callouts and vibration from one shared state *[claimed]*
- Incident clips and Gemini reports — Danger alerts save a 10 s clip and Gemini returns a structured incident summary *[claimed]*
- Fail-safes — 250 ms Arduino heartbeat, camera-offline fallback, Gemini circuit breaker *[claimed]*
- Phone 3D mirror and iOS app — Pi streams small JSON over SSE to a three.js view and a SwiftUI app *[claimed]*
- Traffic simulator — Scripted scenes run through the real pipeline for demos without cars *[shown_working]*

**Flow:** Wear the helmet; detection runs on the Pi → Car approaches and is tracked → Rider gets arrow, beep and callout → Close pass is measured and a clip saved → Review live view and history on phone

**Prompt:** State Farm ShellHacks 2026: simplify auto insurance and help students reduce everyday risks like theft, fire or accidents; Waymo also won.
**Fit (implied):** Targets rider safety and risk reduction with measured close-pass data tied to a passing law; team switched to this idea after reviewing tracks.  *(targeted: State Farm, Waymo)*
**AI:** YOLO runs locally for all safety decisions; Gemini only summarizes incidents from six key frames plus measured facts and answers voice questions, rate-limited and non-blocking.
**Architecture:** Pi 5 runs camera, YOLO, tracker, fusion and policy; Arduino handles ultrasonics, haptics and watchdog; SSE feeds a three.js page and SwiftUI iOS app; Gemini gateway is asynchronous.
**Novelty:** Full hardware stack with fail-safes and sensor-grounded AI reports; includes a simulator.
**Scope:** large · working: Detailed hardware build description, tests, simulator, three prototype screenshots; no demo link. · polish: Docs folder, iOS app, tests, env example; no CI or Docker.
**Claims:** Close-pass distance measured, e.g. 0.32 m example | Runs fully on-device and offline | 1,105 US cyclist deaths in 2022 cited as motivation
**Gaps:** no video; not road-tested
Sources: https://devpost.com/software/halo-1q59hf, https://github.com/billpquach/halo (evidence README), sponsor_prompts_*.jsonl (ShellHacks 2026)

---

