# TreeHacks — TreeHacks 2025 (3 projects)

### Portable Braille
*TreeHacks TreeHacks 2025 · dataset: sponsor · tier: overall_top3 · evidence A · confidence high*
**Prizes:** NVIDIA: Robo Prize; TreeHacks Grand Prize | 3rd Place [3rd]

**What it is:** A pocket-sized refreshable Braille device built from an ESP32, a high-voltage Braille module, a six-button keypad and a Li-Po battery in a 3D-printed case. It syncs with an iPhone over Bluetooth LE to read and write text, and pairs with Ray-Ban Meta glasses and a Jetson for facial-expression recognition.
**Problem / user:** Blind, visually impaired and deaf-blind people who lack affordable portable Braille; the page asserts literacy under 10% and cites a deaf-blind advocate who needs a human to type speech for her.

**Features**
- Phone text in Braille — Phone sends text over BLE to the microcontroller, which raises Braille characters on the module for texting, browsing and social media. *[claimed]*
- Braille keypad input — Six-plus buttons let the user type Braille combinations that are sent back to the phone. *[claimed]*
- Speech to tactile text — Speech is converted to text and rendered on the Braille module for deaf-blind users; method not specified. *[claimed]*
- Facial expression recognition — Video from Ray-Ban Meta glasses is streamed to a Jetson Orin Nano that classifies expressions offline; model not named. *[shown_working]*
- Audio messages as Braille — Voice messages are shown as tactile text rather than only played. *[claimed]*
- Portable hardware — 3D-printed enclosure, Li-Po battery with management module, boost converter for the 200V module. *[shown_working]*

**Flow:** Pair device with iPhone over BLE → Phone text appears as raised Braille → User replies on the keypad → Deaf-blind user's conversation partner speaks and speech shows as Braille → Optional glasses feed to Jetson for expression readout

**Prompt:** NVIDIA Robo Prize at TreeHacks 2025: best use of NVIDIA technology in robotics, computer vision or edge AI; prize is Jetson dev kits plus cash.
**Fit (implied):** Uses a Jetson Orin Nano to run offline facial-expression recognition on a Ray-Ban Meta video feed, adding a computer-vision edge-AI element to a hardware accessibility device.  *(targeted: NVIDIA: Robo Prize)*
**Sponsor tools:** NVIDIA Jetson Orin Nano (Edge facial-expression recognition from smart-glasses video, supporting)
**AI:** Facial expression recognition on Jetson from glasses video; no model, dataset or API named. Speech-to-text mentioned without detail.
**Architecture:** Phone connects by BLE to an ESP32 driving the Braille module and keypad; separately, glasses video goes to a Jetson for expression recognition.
**Novelty:** Hardware-first accessibility build aiming for a truly pocketable Braille display, with an add-on that turns facial expressions into information for blind users.
**Scope:** small · working: Demo video and photos of assembled device and glasses-to-Jetson stream; no test results. · polish: Sparse repo (83 files, firmware only) with a development plan README; no tests.
**Claims:** First really portable pocket-sized Braille display | Expression recognition works offline and faster than Be My Eyes (unsupported) | Braille literacy among US blind community under 10% (unsourced)
**Gaps:** no user testing; speech and expression models unspecified; video not viewed
Sources: https://devpost.com/software/portable-braille-cdq8v5, evidence/sponsor-treehacks-treehacks-2025-portable-braille.json

---

### Ranger
*TreeHacks TreeHacks 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** NVIDIA: Best Accelerated Compute

**What it is:** A hat with a four-microphone array wired to a Jetson Orin Nano that classifies sounds, estimates their direction and live-transcribes speech, then shows icons on a radial grid and captions in a Meta Quest 3 AR view for deaf and hard-of-hearing wearers.
**Problem / user:** Deaf and hard-of-hearing people who miss ambient sounds such as being called, an approaching ambulance or footsteps behind them.

**Features**
- Directional sound sensing — ReSpeaker mic array audio is triangulated for direction and amplitude of the loudest source each step. *[claimed]*
- Sound classification — YAMNet classifier labels sounds; results appear as icons on a circular grid by direction and distance. *[claimed]*
- Live speech transcription — Whisper Mini runs on the last 10 seconds of audio, including speech from behind the wearer. *[claimed]*
- AR heads-up display — Unity app on Quest 3 overlays icons and captions without blocking the view. *[claimed]*
- Edge-only processing — Jetson does heavy compute and streams to the headset over wired USB-C using ADB network-over-USB. *[claimed]*

**Flow:** Wear hat with mic array → Array sends four-channel audio to Jetson → Jetson classifies, locates and transcribes → Results go over USB to the Quest → Wearer sees radar-style icons and captions in view

**Prompt:** NVIDIA Best Accelerated Compute at TreeHacks 2025: best use of NVIDIA AI or accelerated computing in a project; prizes were RTX 5090 and 5080 GPUs.
**Fit (implied):** Runs sound classification, direction estimation and Whisper transcription locally on a Jetson Orin Nano, keeping the AI workload on NVIDIA edge hardware.  *(targeted: NVIDIA: Best Accelerated Compute)*
**Sponsor tools:** NVIDIA Jetson Orin Nano (On-device audio ML and transcription, core); CUDA (GPU acceleration for models (per known notes), unclear)
**AI:** YAMNet for sound classes and Whisper Mini for speech, both on a Jetson; direction from mic-array signal processing rather than ML.
**Architecture:** Mic array to Jetson Orin Nano (Python audio pipeline) to Quest 3 Unity AR app over USB network link.
**Novelty:** Spatial sound awareness and transcription fused into one AR view across three devices with different OSes and power needs.
**Scope:** medium · working: Page says the 36-hour build worked across all devices; no video or metrics on Devpost. · polish: Repo has ~900 files and tests; README empty; no video.
**Claims:** Built a three-device AR pipeline in a 36-hour sprint | Entirely edge computation, no cloud
**Gaps:** README empty; no video; no accuracy or latency numbers
Sources: https://devpost.com/software/ranger-6jkv5s, evidence/sponsor-treehacks-treehacks-2025-ranger.json

---

### WiiWork
*TreeHacks TreeHacks 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** NVIDIA: Best Accelerated Compute

**What it is:** A proof of concept for an agent-first website. React components wrapped in a higher-order component describe their purpose and position, so a voice-driven multi-model agent can see the page and operate it with a virtual cursor, demonstrated on a reading-list app with a Wii-style look.
**Problem / user:** Web developers and AI-agent builders: websites were not designed for agents to read and operate.

**Features**
- Agentic Web Component wrapper — HOC tells the agent each element's purpose, appearance and location. *[shown_working]*
- Virtual agent cursor — Animated cursor moves and clicks on the page on the agent's behalf via regex-parsed tool calls. *[shown_working]*
- Multi-model router — Classifies requests and sends simple ones to GPT-4-mini, medium to Claude 3.5 Sonnet, complex to NVIDIA-hosted DeepSeek, chat to GPT-4. *[claimed]*
- Voice interaction — Whisper transcribes speech and ElevenLabs speaks replies. *[shown_working]*
- Phone-as-mic pairing — Mobile device pairs to desktop to supply voice input. *[shown_working]*
- Shared state manager — Zustand store syncs user and agent actions. *[claimed]*
- Malicious message flagging — Alignment model intervenes on flagged messages. *[claimed]*

**Flow:** Open the Wii-themed site → Optionally pair a phone for voice input → Speak or type a request → Router picks a model with a category prompt → Agent moves its virtual cursor and operates the page

**Prompt:** NVIDIA Best Accelerated Compute at TreeHacks 2025: best use of NVIDIA AI or accelerated computing in a project; prizes were RTX 5090 and 5080 GPUs.
**Fit (implied):** Routes complex-logic requests to DeepSeek hosted by NVIDIA as one of several models; NVIDIA use is one routing branch rather than the focus.  *(targeted: NVIDIA: Best Accelerated Compute)*
**Sponsor tools:** NVIDIA-hosted DeepSeek (Handling complex-logic requests in the router, supporting)
**AI:** Router classifies each request then dispatches to GPT-4-mini, Claude 3.5 Sonnet, GPT-4 or DeepSeek with per-category prompts; Whisper and ElevenLabs for voice; tool calls parsed by regex.
**Architecture:** React/TypeScript front end with Zustand state and Convex backend; wrapped components expose descriptions to the LLM router; phone companion sends audio.
**Novelty:** Reframes a website as something that describes itself to agents, and combines multi-vendor routing with voice and a virtual cursor, built solo in a weekend.
**Scope:** small · working: Live site wiiwork.dev and demo video; screenshots of agent tasks. · polish: Themed UI; repo README is the unedited Vite template; no tests.
**Claims:** Model routing optimizes cost and performance (no measurements) | Built solo in about 25 of 36 hours
**Gaps:** README is template; video not viewed; no measurements
Sources: https://devpost.com/software/wiiwork-8u1x62, evidence/sponsor-treehacks-treehacks-2025-wiiwork.json

---

