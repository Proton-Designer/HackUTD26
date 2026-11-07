# TreeHacks: project cards (7 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## TreeHacks 2025

### Portable Braille  (TreeHacks 2025)

- **Prizes:** NVIDIA: Robo Prize [unknown]; TreeHacks Grand Prize | 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Pocket-sized refreshable Braille device that lets blind and deaf-blind users read and write phone text and, via Ray-Ban Meta glasses and a Jetson, read facial expressions.
- **Problem / user:** Braille displays are unaffordable and inaccessible, and deaf-blind users depend on assistants to convert speech to tactile text. / blind and deaf-blind users
- **Domain / idea type:** accessibility + education / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_ios / True / vision; speech_or_voice
- **Stack:** langs C; frontend ; backend ; db ; hosting 
- **Tech/APIs:** NVIDIA Jetson Orin Nano (hardware_part, supporting, sponsor); ESP32 microcontroller (hardware_part, core); Braille module (200V) (hardware_part, core); Ray-Ban Meta glasses (hardware_part, supporting); Bluetooth Low Energy (other, core)
- **Sponsor APIs:** NVIDIA Jetson Orin Nano | fit: Won the NVIDIA Robo Prize (Jetson dev kit) for a hardware build that streams Ray-Ban Meta glasses video to a Jetson Orin Nano for offline facial-expression recognition, a secondary feature next to the Braille device.
- **Repo:** public, commits 19 (before/in/after event: 0/15/4), README solid
- **Demo/writeup:** video True, live none, screenshots 13, writeup medium, impact claims True (Claims blind literacy in the US is below 10% and that the device is faster than Be My Eyes and works offline.)
- **Notes:** Solo build: 3D-printed enclosure, 200V step-up for the Braille module, ESP32 with BLE to phone, six-key keypad; Ray-Ban Meta video was routed to a Jetson Orin Nano for offline facial-expression recognition via an analog hack.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note depth
- **Links:** [Devpost](https://devpost.com/software/portable-braille-cdq8v5) | [GitHub](https://github.com/Adil-Jussupov/PortableBraille)

### Ranger  (TreeHacks 2025)

- **Prizes:** NVIDIA: Best Accelerated Compute [unknown]  (tier: sponsor_winner)
- **Pitch:** Hat-mounted mic array plus Jetson Orin Nano that classifies and locates sounds and live-transcribes speech, showing icons and captions in a Meta Quest AR view for deaf users.
- **Problem / user:** Deaf and hard-of-hearing people miss the direction and type of surrounding sounds, from everyday cues to danger. / deaf and hard-of-hearing people
- **Domain / idea type:** accessibility + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; other / True / speech_or_voice; predictive_ml
- **Stack:** langs Python; C#; frontend Unity; backend Python; db ; hosting Jetson Orin Nano
- **Tech/APIs:** NVIDIA Jetson Orin Nano (hardware_part, core, sponsor); CUDA (Whisper on Jetson) (framework, supporting, sponsor); Whisper (ai_model, core); YAMNet sound classifier (ai_model, core); ReSpeaker 4-mic array (hardware_part, core); Meta Quest 3 / Unity (hardware_part, core)
- **Sponsor APIs:** NVIDIA Jetson Orin Nano; CUDA | fit: Targeted NVIDIA Best Accelerated Compute by running sound classification, direction-of-arrival processing and CUDA-accelerated Whisper transcription entirely on a Jetson Orin Nano with no cloud.
- **Repo:** public, commits 96 (before/in/after event: 0/96/0), README none
- **Demo/writeup:** video True, live none, screenshots 10, writeup long, impact claims False
- **Notes:** Fully on-edge: ReSpeaker 4-mic array direction-of-arrival, YAMNet-style sound classifier and Whisper on the Jetson, sent to a Quest 3 Unity app over USB with ADB; an NVIDIA engineer supplied a custom power cable.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; placement within prize tiers (page lists 5090 and 5080 tiers, tier not stated)
- **Links:** [Devpost](https://devpost.com/software/ranger-6jkv5s) | [GitHub](https://github.com/YuanSamuel/Treehacks2025)

### WiiWork  (TreeHacks 2025)

- **Prizes:** NVIDIA: Best Accelerated Compute [unknown]  (tier: sponsor_winner)
- **Pitch:** Proof-of-concept 'AI-native' website pattern where wrapped React components describe themselves so a multi-model voice agent can see and operate the page with a virtual cursor.
- **Problem / user:** Websites are not built for AI agents, which struggle to understand and operate page elements. / web developers building agent-friendly sites
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; speech_or_voice
- **Stack:** langs TypeScript; frontend React; Zustand; Tailwind CSS; shadcn/ui; Framer Motion; backend Convex; db Convex; hosting Vercel
- **Tech/APIs:** NVIDIA-hosted DeepSeek (ai_model, supporting, sponsor); OpenAI GPT-4 / GPT-4-mini / Whisper (ai_model, core); Anthropic Claude 3.5 Sonnet (ai_model, core); ElevenLabs (ai_model, supporting); Convex (database, core)
- **Sponsor APIs:** NVIDIA-hosted DeepSeek | fit: Targeted NVIDIA Best Accelerated Compute by routing complex-logic requests to an NVIDIA-hosted DeepSeek reasoning model within a four-model router; this is one of several models and not the core of the project.
- **Repo:** public, commits 50 (before/in/after event: 0/48/2), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 19, writeup medium, impact claims False
- **Notes:** Solo build with a higher-order-component system and Zustand state shared by user and agent; a router sends requests to GPT-4-mini, Claude 3.5 Sonnet, NVIDIA-hosted DeepSeek or GPT-4 by category, with voice input via phone pairing.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; placement within prize tiers (page lists 5090 and 5080 tiers, tier not stated)
- **Links:** [Devpost](https://devpost.com/software/wiiwork-8u1x62) | [GitHub](https://github.com/Alezander9/WiiWork)


## TreeHacks 2026

### CalTrack  (TreeHacks 2026)

- **Prizes:** [NVIDIA] Edge AI Track [unknown]  (tier: sponsor_winner)
- **Pitch:** California wildfire disaster-intelligence platform combining aggregated Wi-Fi-positioning population density, Earth-2 fire-risk forecasts and an AI voice 911 triage agent mesh.
- **Problem / user:** Emergency managers lack a unified view fusing 911 call data, population density and fire risk to decide where resources go first. / emergency managers and 911 operators
- **Domain / idea type:** safety_security + civic_legal / data_or_analytics
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; speech_or_voice; predictive_ml
- **Stack:** langs Python; frontend ; backend FastAPI; CrewAI; PyTorch; db SQLite; hosting Docker; NVIDIA DGX Spark
- **Tech/APIs:** NVIDIA DGX Spark (hardware_part, core, sponsor); NVIDIA Earth-2 (earth2studio) (ai_model, core, sponsor); NVIDIA Personaplex (planned) (ai_model, token, sponsor); VAPI (telecom, core); CrewAI (framework, core); HERE API (maps_geo, supporting); Apple Wi-Fi Positioning data (data_source, core)
- **Sponsor APIs:** NVIDIA DGX Spark; NVIDIA Earth-2 | fit: Targeted the NVIDIA Edge AI track by deploying Earth-2 on DGX Spark systems to generate predictive weather-based fire-risk overlays; the Personaplex voice model was dropped for VAPI after setup troubles.
- **Repo:** public, commits 38 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims True (States 650,000 devices mapped in 6 hours across the greater Palo Alto region.)
- **Notes:** Used DGX Spark to host NVIDIA Earth-2 for the fire-risk overlay; the planned Personaplex voice operator was replaced by VAPI after DGX Spark setup issues; mapped about 650,000 devices around Palo Alto via an Apple WPS dataset.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/caltrack-i0pq3n) | [GitHub](https://github.com/alangrewco/treehacks)

### Detour  (TreeHacks 2026)

- **Prizes:** [NVIDIA] Edge AI Track [unknown]  (tier: sponsor_winner)
- **Pitch:** Edge-run multi-agent system on a DGX Spark that screens live TLE orbital data for debris conjunctions and proposes fuel-constrained satellite avoidance maneuvers.
- **Problem / user:** Satellite operators are flooded with dense conjunction messages and must manually decide which close approaches justify a maneuver. / satellite operators
- **Domain / idea type:** ai_agents_infra + safety_security / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; Python; frontend Next.js; React; shadcn/ui; Three.js; backend vLLM; LangChain; SGP4; db ; hosting Vercel; Cloudflare; ASUS GX10 / DGX Spark
- **Tech/APIs:** NVIDIA DGX Spark (ASUS Ascent GX10) (hardware_part, core, sponsor); NVIDIA Nemotron-3-Nano-30B-A3B NVFP4 (ai_model, core, sponsor); vLLM (framework, core); LangChain agents (framework, supporting); TLE orbital data / SGP4 (data_source, core); Three.js globe (framework, supporting)
- **Sponsor APIs:** NVIDIA DGX Spark; NVIDIA Nemotron | fit: Targeted the NVIDIA Edge AI track by hosting a local Nemotron-3-Nano model via vLLM on a DGX Spark-class box so agents triage conjunctions and maneuvers without cloud round-trips.
- **Repo:** public, commits 81 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 16, writeup long, impact claims False
- **Notes:** Runs Nemotron-3-Nano-30B (NVFP4) via vLLM on an ASUS GX10 (DGX Spark) as an air-gapped edge setup; LLM calls Python SGP4 tools instead of doing orbital math; Gaussian sampling replaced full debris propagation for latency.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/detour-64kpds) | [GitHub](https://github.com/keanucz/detour)

### Sprout  (TreeHacks 2026)

- **Prizes:** [NVIDIA] Edge AI Track [unknown]  (tier: sponsor_winner)
- **Pitch:** Autonomous gantry-style robotic garden whose Jetson Nano camera identifies plant species and health on-device and pumps the right amount of water.
- **Problem / user:** Industrial robotics feels rigid; the team wanted a gentle autonomous gardener that tends plants precisely without waste. / home and community gardeners
- **Domain / idea type:** sustainability_climate + food_nutrition / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision; agent_or_tool_use
- **Stack:** langs Python; frontend ; backend Python; db ; hosting Jetson Nano
- **Tech/APIs:** NVIDIA Jetson Nano (hardware_part, core, sponsor); CUDA (framework, supporting, sponsor); Ollama / Qwen (ai_model, unclear); Arduino (hardware_part, core); Water pump + gantry motors (hardware_part, core)
- **Sponsor APIs:** NVIDIA Jetson Nano; CUDA | fit: Targeted the NVIDIA Edge AI track by running the plant-species and health classification model fully on-device on a Jetson Nano mounted on the gantry, which then drives watering via Python scripts.
- **Repo:** public, commits 27 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 34, writeup medium, impact claims False
- **Notes:** Hand-fabricated sheet-metal 2-3 axis gantry with vinyl-wrapped chassis, custom motor and pump driver circuits, Jetson Nano plus Arduino; built-with tags mention Ollama, Qwen and Claude though the text describes a custom edge model.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; event_start; event_end; ai_types depth
- **Links:** [Devpost](https://devpost.com/software/greenguardian-microfarm) | [GitHub](https://github.com/lethan3/cactushacks)

### TORQ  (TreeHacks 2026)

- **Prizes:** [NVIDIA] Edge AI Track [unknown]  (tier: sponsor_winner)
- **Pitch:** Retrofits a 2018 Honda Accord for self-driving with NVIDIA's Alpamayo R1 reasoning model on a Jetson AGX Thor plus a sunnypilot control layer, dispatched through an iOS rideshare app.
- **Problem / user:** Self-driving is limited to new vehicles; older cars lack it, and riders get no visibility into an autonomous car's reasoning. / riders and owners of existing cars
- **Domain / idea type:** mobility_transport + ai_agents_infra / hardware_gadget
- **Platforms / hardware / AI:** mobile_ios; hardware / True / vision; agent_or_tool_use; llm_chat
- **Stack:** langs C++; Python; Swift; frontend iOS app (Swift); backend sunnypilot; MQTT; CUDA; db ; hosting Jetson AGX Thor; Google Compute Engine (MQTT broker)
- **Tech/APIs:** NVIDIA Alpamayo R1 (ai_model, core, sponsor); NVIDIA Jetson AGX Thor (hardware_part, core, sponsor); NVIDIA Holoscan Sensor Bridge (hardware_part, core, sponsor); CUDA / TensorRT-Edge-LLM (planned) (framework, supporting, sponsor); sunnypilot / openpilot (framework, core); comma Red Panda CAN adapter (hardware_part, core); MQTT (other, supporting)
- **Sponsor APIs:** NVIDIA Alpamayo R1; NVIDIA Jetson AGX Thor; NVIDIA Holoscan Sensor Bridge; CUDA | fit: Targeted the NVIDIA Edge AI track by running Alpamayo R1 for high-level driving plans and explanations on a Jetson AGX Thor with Holoscan-bridged cameras, paired with a fast sunnypilot control loop.
- **Repo:** public, commits 28 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup long, impact claims False
- **Notes:** Two-layer design: Alpamayo R1 (10.5B VLA) plans slowly while sunnypilot controls at 100 Hz through a comma Red Panda CAN adapter; cameras feed GPU memory through the Holoscan Sensor Bridge; tested with a safety driver; MQTT via a GCE broker.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/torq) | [GitHub](https://github.com/bryandong24/treehacks2026)
