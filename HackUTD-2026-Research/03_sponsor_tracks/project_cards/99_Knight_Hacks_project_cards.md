# Knight Hacks: project cards (3 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## Knight Hacks IX (2025)

### Farsight  (Knight Hacks IX (2025))

- **Prizes:** NVIDIA: Best Use of Jetson Nano [unknown]; Hugging Face: Best Use of Open Source AI [unknown]; Full Sail: Pathways & Perception, A Serious Games & Simulation Challenge [unknown]; Encompass: Data Capturing Hardware [unknown]  (tier: sponsor_winner)
- **Pitch:** Search-and-rescue rover system: a Meta Quest VR headset drives a Jetson-equipped rover with live person detection, a local voice/vision assistant and post-run Gaussian-splat room maps.
- **Problem / user:** Responders should inspect an unfamiliar room before entering, with live view, person-finding and spatial context. / search-and-rescue responders
- **Domain / idea type:** safety_security + ai_agents_infra / hardware_gadget
- **Platforms / hardware / AI:** web; hardware; other / True / vision; speech_or_voice; llm_chat; agent_or_tool_use
- **Stack:** langs Python; Swift; TypeScript; Rust; frontend Three.js; WebXR; backend FastAPI; ROS2; Nav2; db ; hosting Tailscale
- **Tech/APIs:** NVIDIA Jetson Orin Nano (hardware_part, core, sponsor); TensorRT (YOLO11n-pose) (framework, core, sponsor); Qwen3-VL-2B (llama.cpp) (ai_model, core); Whisper (whisper.cpp) (ai_model, core); ROS2 Nav2 (framework, core); Meta Quest WebXR (hardware_part, core); iPhone LiDAR/ARKit (hardware_part, core); Brush Gaussian splatting (framework, supporting)
- **Sponsor APIs:** NVIDIA Jetson Orin Nano; NVIDIA TensorRT | fit: Targeted NVIDIA Best Use of Jetson Nano by mounting a Jetson Orin Nano on the rover to run onboard person detection with TensorRT, local AI, Nav2 navigation, camera streaming and motor control.
- **Repo:** public, commits 300 (before/in/after event: 0/509/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 19, writeup long, impact claims False
- **Notes:** Rover carries a LiDAR iPhone and Jetson Orin Nano; YOLO11n-pose via TensorRT, Nav2 autonomy, local Qwen3-VL, Whisper and Piper; Mac trains Brush splats seeded with LiDAR. Won four sponsor prizes.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/farsight-t4qyli) | [GitHub](https://github.com/azizu06/farsight)

### Fireline  (Knight Hacks IX (2025))

- **Prizes:** NVIDIA: Best Use of Jetson Nano [unknown]; OneEthos: Innovation for Good [unknown]  (tier: sponsor_winner)
- **Pitch:** Tree-mounted camera units that detect wildfire smoke on an NVIDIA Jetson, wake on dry-weather risk, and send tiny 340-byte alerts over a simulated satellite link to a live crew console.
- **Problem / user:** Satellites spot wildfires only once large, and ground cameras need towers, power and internet in remote areas. / forest and wildfire crews
- **Domain / idea type:** sustainability_climate + safety_security / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision; llm_chat
- **Stack:** langs Python; TypeScript; C++ (Arduino); frontend React; Vite; Leaflet; backend FastAPI; MQTT; WebSockets; db SQLite; hosting Azure VM; Docker; Caddy
- **Tech/APIs:** NVIDIA Jetson Orin Nano (hardware_part, core, sponsor); TensorRT (framework, core, sponsor); Pyronear YOLO smoke model (Hugging Face) (ai_model, core); Ultralytics (framework, supporting); ESP32 + DHT11 (hardware_part, core); Gemma 3 via Ollama (ai_model, supporting); Azure VM (cloud, supporting)
- **Sponsor APIs:** NVIDIA Jetson Orin Nano; NVIDIA TensorRT | fit: Targeted NVIDIA Best Use of Jetson Nano by running the smoke-detection model on a Jetson Orin Nano GPU with TensorRT inside each field unit so only a small verdict crosses the satellite link.
- **Repo:** public, commits 18 (before/in/after event: 0/18/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 34, writeup long, impact claims True (Cites Florida wildfire statistics (1,300 fires, 57,025 acres) and satellite revisit figures as motivation; admits false-alarm rate is unmeasured.)
- **Notes:** Jetson Orin Nano runs Pyronear's open YOLO smoke model via TensorRT, gated by an ESP32 humidity sensor; alerts fit an Iridium-sized 340-byte packet; satellite link and most fleet units are simulated; Gemma 3 writes incident summaries.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/fireline-764nir) | [GitHub](https://github.com/kateye31/fireline)

### Permanence  (Knight Hacks IX (2025))

- **Prizes:** Best Overall Hack [1st]; NVIDIA: Best Use of Jetson Nano [unknown]; Hugging Face: Best Use of Open Source AI [unknown]  (tier: overall_top3)
- **Pitch:** Rover with persistent 3D object memory on a Jetson Orin Nano that tracks hidden balls under shuffled cups and drives to remembered targets via a 3D vision-language model.
- **Problem / user:** Robots forget objects when detectors lose sight of them; the team wanted object-permanence-style memory instead of 'I detected it'. / robotics developers and assistive-robot researchers
- **Domain / idea type:** ai_agents_infra + accessibility / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision; llm_chat; speech_or_voice; agent_or_tool_use
- **Stack:** langs Python; C++; JavaScript; frontend Three.js; backend PyTorch; OpenCV; db ; hosting Jetson Orin Nano
- **Tech/APIs:** NVIDIA Jetson Orin Nano (8 GB) (hardware_part, core, sponsor); TensorRT FP16 (framework, core, sponsor); CUDA (framework, core, sponsor); Qwen-3D VLM (ai_model, core); YOLOE (ai_model, core); Record3D + iPhone LiDAR (hardware_part, core); Arduino + L298N motors (hardware_part, supporting)
- **Sponsor APIs:** NVIDIA Jetson Orin Nano; NVIDIA TensorRT; NVIDIA CUDA | fit: Targeted NVIDIA Best Use of Jetson Nano by running a quantized 3B Qwen-3D model and a TensorRT FP16 YOLOE tracker together on one Jetson Orin Nano (8 GB), with a custom handoff to keep peak memory near 6.1 GB.
- **Repo:** public, commits 107 (before/in/after event: 0/105/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 22, writeup long, impact claims False
- **Notes:** Qwen-3D (3B) custom 8-bit quantized to fit with YOLOE TensorRT in 8 GB; shell-game demo is verified by lifting the cup; iPhone LiDAR streams via Record3D; won overall first plus two sponsor prizes.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/permanence) | [GitHub](https://github.com/billpquach/permanence)
