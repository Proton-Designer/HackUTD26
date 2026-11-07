# SBU Hacks — 2026 (1 projects)

### A.U.R.A. (Awareness, Understanding and Ranging Assistant)
*SBU Hacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** BEST HARDWARE TRACK (prize item: NVIDIA Jetson Orin Nano Super; NVIDIA is the prize, not a confirmed sponsor challenge)

**What it is:** A chest-mounted wearable for blind or low-vision users: a 2D lidar gives proximity beeps, a webcam with YOLO names nearby objects, and fused distance and direction are spoken aloud through a Bluetooth speaker, with a browser dashboard for caregivers.
**Problem / user:** People with low vision who rely on a white cane, which only senses what it touches near the ground; caregivers are a secondary user of the dashboard.

**Features**
- Lidar proximity beeps — Hokuyo UST-10LX scans 40 times per second over 270 degrees; beeps speed up from 2 m and go solid under 0.75 m. *[shown_working]*
- Object recognition — YOLO11n with TensorRT FP16 on Jetson Orin Nano, filtered to 22 walking-relevant COCO classes. *[shown_working]*
- Sensor fusion and spoken alerts — Pixel position mapped to lidar angle gives distance; espeak-ng says things like "chair on the left, 1 meter", nearest first, after 3 frames and with cooldown. *[shown_working]*
- Live web dashboard — Orin hotspot serves radar map, alert zones and camera boxes to any browser. *[shown_working]*
- Custom 3D-printed chest mount and power — Fusion 360 design, USB-boost 12 V supply for lidar. *[shown_working]*
- Haptics, stairs/door detection, battery, bone-conduction audio — Listed next steps. *[planned]*

**Flow:** Wear the chest unit → Lidar scans and beeps as obstacles approach → Camera identifies objects and matches lidar distances → Hear nearest-object speech alerts → Caregiver opens dashboard on the Orin Wi-Fi

**Prompt:** Best Hardware Track rewards creative, functional use of physical components such as sensors, microcontrollers and cameras; winner receives a Jetson Orin Nano Super kit, runner-up a Raspberry Pi 5.
**Fit (implied):** Combines lidar, camera, Jetson compute, speaker and custom mount into a working accessibility wearable; hardware centered. NVIDIA is the prize, though the build already runs on an Orin Nano.  *(targeted: Best Hardware Track)*
**Sponsor tools:** NVIDIA Jetson Orin Nano (edge compute running YOLO via TensorRT, core); NVIDIA TensorRT (FP16 YOLO optimization, supporting)
**AI:** Pretrained YOLO11n object detection (COCO, 22 classes) accelerated with TensorRT; lidar-camera geometric fusion; no training.
**Architecture:** Lidar over Ethernet to Jetson; Python SCIP 2.0 driver, obstacle_alert program with buzzer GPIO, vision.py for YOLO and TTS, built-in web server streaming to browser via Server-Sent Events.
**Novelty:** Lidar-first design that keeps working without vision, plus custom lidar driver; physical prototype with 3D-printed enclosure.
**Scope:** small · working: Repo with driver, alert program, viewer and service file plus a simulator mode; gallery photos and CAD per Devpost; no video. · polish: Detailed setup guide and writeup; only about 860 lines of code.
**Claims:** 40 Hz, 270 degree, 10 m lidar | Alerts need 3 consecutive frames | Works offline
**Gaps:** no video; no accuracy or user testing
Sources: https://devpost.com/software/a-u-r-a-assistive-understanding-and-ranging-assistant, https://github.com/jeras0/chest-lidar (evidence README), https://sbuhacks-2026.devpost.com/

---

