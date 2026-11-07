# SBU Hacks: project cards (1 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## 2026

### A.U.R.A. (Awareness Understanding and Ranging Assistant)  (2026)

- **Prizes:** BEST HARDWARE TRACK (prize item: NVIDIA Jetson Orin Nano Super; NVIDIA is the prize, not a confirmed sponsor challenge) [unknown]  (tier: sponsor_winner)
- **Pitch:** Chest-worn assistive device pairing a 2D lidar with YOLO object detection on a Jetson Orin Nano to beep and speak obstacle names and distances to low-vision users.
- **Problem / user:** White canes sense only nearby ground-level obstacles and cannot identify objects or warn of approaching ones. / people with low vision
- **Domain / idea type:** accessibility + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision; speech_or_voice
- **Stack:** langs Python; frontend HTML canvas; backend Python; Server-Sent Events; db ; hosting Jetson Orin Nano
- **Tech/APIs:** NVIDIA Jetson Orin Nano (hardware_part, core, sponsor); TensorRT FP16 (framework, core, sponsor); YOLO11n (Ultralytics) (ai_model, core); Hokuyo UST-10LX lidar (hardware_part, core); espeak-ng (other, supporting); Fusion 360 / 3D printing (other, supporting)
- **Sponsor APIs:** NVIDIA Jetson Orin Nano; NVIDIA TensorRT | fit: Won the Best Hardware Track whose prize named the NVIDIA Jetson Orin Nano, and the project is built around a Jetson Orin Nano running a TensorRT-optimized YOLO model beside a lidar.
- **Repo:** public, commits 1 (before/in/after event: 0/1/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 28, writeup long, impact claims False
- **Notes:** Custom Python driver for a Hokuyo UST-10LX lidar, YOLO11n in TensorRT FP16 on the Orin, camera-angle-to-lidar fusion, offline espeak-ng speech, CAD-printed mount, USB-powered 5V-to-12V boost and a live browser dashboard.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; sponsor_challenge_link
- **Links:** [Devpost](https://devpost.com/software/a-u-r-a-assistive-understanding-and-ranging-assistant) | [GitHub](https://github.com/jeras0/chest-lidar)
