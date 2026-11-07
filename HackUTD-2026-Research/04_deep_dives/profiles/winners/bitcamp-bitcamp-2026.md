# Bitcamp — Bitcamp 2026 (48 projects)

### Aether
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Bitcamp Hack - Bitcamp; TerpAI Ultimate Agent Showdown - Cloudforce/Microsoft

**What it is:** Aether is a student 'command center' web app: a Morning Brief dashboard, AI triage that marks assignments Healthy or Danger, and a fluid transition into a focused AI chat, anchored by an animated orb and voice briefings.
**Problem / user:** Students face scattered notifications, dead-end dashboards and information spread across email, LMS and project trackers.

**Features**
- Morning Brief — Dashboard summarizing the day, upcoming deadlines and cross-domain insights. *[shown_working]*
- Autonomous triage — AI engine sorts assignments into Healthy or Danger states by priority and time, color-coded. *[claimed]*
- Fluid workspace — State-driven UI morphs from briefing to deep-focus chat, with a persistent top-bar pill. *[shown_working]*
- Aether Orb — Animated visual AI core giving real-time feedback using SVG filters. *[shown_working]*
- Voice briefings — ElevenLabs text-to-speech reads the briefing. *[claimed]*
- Data extraction fallbacks — Playwright scraping and pdfplumber parsing when integrations are unavailable. *[claimed]*
- Network graph and flashcard artifact — Screenshots show Aether Network, TerpAI Agent and Flashcard views; not described in text. *[unclear]*

**Flow:** Open the Morning Brief hub → Review deadlines and triaged assignments → Listen to voice brief → Transition via the pill into AI chat workspace → Use TerpAI agent and flashcard views

**Prompt:** TerpAI Ultimate Agent Showdown: build at least one TerpAI agent students or faculty cannot live without, solving real campus problems for everyday Terp life, with a shark-tank style pitch.
**Fit (explicit):** Student academic assistant that uses the TerpAI Ghost-Pilot for academic automation alongside Gemini; page lists the showdown among its awards.  *(targeted: Best Bitcamp Hack - Bitcamp, TerpAI Ultimate Agent Showdown - Cloudforce/Microsoft)*
**Sponsor tools:** TerpAI Ghost-Pilot (Complex academic automation, core); ElevenLabs TTS (Voice-first briefings, supporting); Google Gemini (Reasoning, core)
**AI:** Gemini for reasoning and triage, TerpAI agent for academic automation, ElevenLabs for speech, Playwright and pdfplumber for data extraction, orchestrated as multiple agents by FastAPI.
**Architecture:** React/Vite/Zustand frontend with Three.js, force-graph and particles; FastAPI backend orchestrating Gemini, TerpAI, ElevenLabs and scraping/PDF agents.
**Novelty:** Heavy emphasis on a fluid animated interface (orb, pill, morphing layout) over a multi-agent student assistant.
**Scope:** large · working: About 20k LOC repo with 84 frontend and 47 backend files; demo video embedded; no live site. · polish: Glassmorphism, particles, orb animation and layout transitions; no tests; Claude config directory present.
**Claims:** Seamless transition from dashboard to chat without layout jitter
**Gaps:** Which data integrations are actually built is not stated; Video not watched; Flashcard feature undescribed
Sources: https://devpost.com/software/aether-d4v6sb, evidence/bitcamp-bitcamp-2026-aether.json, https://bitcamp-2026.devpost.com/

---

### AGastIa
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence low*
**Prizes:** Best Champion of Open Source w/ Featherless - Featherless

**What it is:** A medical-report understanding platform: upload a report, OCR it, extract entities with a clinical LLM, score severity, map findings to organs and show them on an interactive 3D body model and causal graph, with separate patient and clinician summaries.
**Problem / user:** Medical reports are dense with numbers and acronyms; patients are the main audience, with clinicians and admins also supported.

**Features**
- Report OCR and entity extraction — PaddleOCR reads uploads; Bio-ClinicalBERT and MedGemma identify medical entities. *[claimed]*
- Organ mapping and severity scoring — Findings are mapped to organs and scored for severity. *[claimed]*
- 3D body model and causal graph — Interactive visualization of findings and links across organs. *[claimed]*
- Dual summaries — Gemini produces clinician and patient-friendly summaries; RAG handles long reports. *[claimed]*
- Imaging analysis — MedSAM segmentation and vision inference for scans. *[claimed]*
- Role-based login — Auth0 with patient, doctor and admin roles. *[claimed]*

**Flow:** Log in via Auth0 with a role → Upload a medical report → OCR and LLM extract and score findings → View 3D body model and causal graph → Read patient or clinician summary

**Prompt:** Best Champion of Open Source w/ Featherless: highlight people who contribute to, build with, or care about open source; credits for top three.
**Fit (explicit):** Builds on open models (MedGemma, Bio-ClinicalBERT, MedSAM, PaddleOCR) and lists Featherless among services. Page lists many prizes as fits; only open-source is a recorded win.  *(targeted: Best Champion of Open Source w/ Featherless - Featherless, Best Machine Learning Track Hack, Best Data Visualization Experience, MLH Best Use of Gemini API, MLH Best Use of Auth0, MLH Best Domain Name (GoDaddy), Best Moonshot Hack, Best Bitcamp Hack, Best UI/UX Hack)*
**Sponsor tools:** Featherless (Open-source models and tools, unclear); Auth0 (Authentication with roles, supporting); Gemini API (Reasoning and summarization, core)
**AI:** Pipeline of open and hosted models: PaddleOCR, Bio-ClinicalBERT, MedGemma, MedSAM for segmentation, RAG for long reports, and Gemini for summaries.
**Architecture:** React/Vite frontend; FastAPI backend with Celery and Redis workers; PostgreSQL via SQLAlchemy; PyTorch/Transformers medical models; Auth0 login.
**Novelty:** Combines document NLP, imaging segmentation and a 3D anatomical visualization with a causal graph in one explainable report tool.
**Scope:** large · working: Demo video embedded; claimed full stack with async workers; repo not readable here. · polish: 3D model and guided flows described; no live demo; quality of end-to-end operation unverified.
**Claims:** Working end to end and demo-ready (no metrics)
**Gaps:** Repo SriRammSS/AGastIa could not be fetched (clone failed; raw README returned errors on HEAD, main, master); No accuracy data; Video not watched
Sources: https://devpost.com/software/agastiya, https://bitcamp-2026.devpost.com/

---

### ani.mate
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Gemini API

**What it is:** A document-to-video app: upload notes, slides or a paper and a pipeline plans segments, has an LLM write Manim animation code and ElevenLabs narration, renders each segment and stitches a final explainer video in the style of 3Blue1Brown.
**Problem / user:** Visual learners and students who find class notes, slides and papers hard to absorb.

**Features**
- Multi-format document upload — Accepts txt, md, pdf, ppt and pptx and parses them to text. *[shown_working]*
- Multi-stage planning — Builds outline, segment plans and beat-level narration before coding scenes. *[claimed]*
- Manim scene code generation — Selectable LLM (TerpAI, Gemini or Claude) writes animation code grounded by retrieval. *[claimed]*
- ElevenLabs multilingual narration — Synthesizes voiceover per beat in a chosen language. *[claimed]*
- Validation and repair loops — Syntax checks, linting, render retries with failure context, ffmpeg duration fixes. *[claimed]*
- Parallel segment rendering — Workers render segments, then merge audio and video into one MP4. *[claimed]*
- Auth0 dashboard with live logs — Next.js dashboard streams pipeline progress; playback and downloads. *[claimed]*
- Cloud-synced library — Firebase sync with browser-local fallback. *[claimed]*

**Flow:** Log in via Auth0 → Upload a document → Choose language and LLM provider → Start render and watch live logs → Play or download the final video

**Prompt:** Use the Gemini API to build AI-powered apps (MLH Best Use of Gemini API).
**Fit (implied):** Gemini is one of three selectable planners and Manim code generators in the pipeline; the app also uses ElevenLabs and Auth0.  *(targeted: [MLH] Best Use of Gemini API)*
**Sponsor tools:** Gemini API (Optional LLM provider for planning and Manim code, supporting); ElevenLabs (Narration synthesis, core); Auth0 (Dashboard login, supporting); TerpAI (Default LLM provider option, supporting)
**AI:** LLM agents (TerpAI/Gemini/Claude) plan outline, segments and beats then emit Manim code with retrieval grounding; sanitize/lint/retry loops fix failures; ElevenLabs does TTS.
**Architecture:** Next.js frontend with Auth0 calls a FastAPI backend: parse, plan, generate Manim, synthesize audio, render in parallel, ffmpeg merge, serve URL; Firebase for library.
**Novelty:** End-to-end generated Manim explainer videos with robust repair loops and provider-swappable LLMs.
**Scope:** medium · working: Repo ~82 files, ~7k LOC with detailed run instructions; screenshots; no demo link or video. · polish: Dashboard UI with logo and multilingual screenshot; no tests.
**Gaps:** no video or live demo
Sources: https://devpost.com/software/ani-mate, evidence/bitcamp-bitcamp-2026-ani-mate.json (README), https://bitcamp-2026.devpost.com/

---

### Apsora Brief
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Data Visualization Experience - Peraton

**What it is:** A satellite collision-risk dashboard: it scrapes live SOCRATES conjunction data, ranks close approaches, has Claude write a plain-language brief and shows every orbit on a 3D Cesium globe with a closest-approach playback scrubber.
**Problem / user:** Low Earth orbit is crowded and an untracked collision can cascade; aimed at satellite operators needing a quick actionable summary.

**Features**
- Live conjunction data — Fetches top close-approach events from SOCRATES/CelesTrak and caches them. *[shown_working]*
- Risk ranking — Scores events by miss distance, collision probability, relative speed and TLE age. *[shown_working]*
- AI brief — Claude API writes a plain-language situational brief readable in about 30 seconds. *[shown_working]*
- 3D orbit globe — SGP4-propagated orbits for every tracked satellite on CesiumJS. *[shown_working]*
- TCA playback — Scrubber over a plus-minus 45 minute window with 91 positions per satellite and a Go to TCA button. *[shown_working]*
- Confidence coloring — Track, marker and ring colors reflect data confidence (red, amber, grey). *[shown_working]*

**Flow:** Open the dashboard with ranked events → Read the AI brief → Select an event → Scrub the TCA window on the globe → Click Go to TCA

**Prompt:** Best Data Visualization Experience (Peraton): turn complex data into a clear engaging visual experience with interactive exploration such as filtering or drill-downs, using modern visualization tools.
**Fit (explicit):** Interactive 3D globe with time scrubber and confidence color system over orbital data; page lists the prize as won.  *(targeted: Best Data Visualization Experience - Peraton)*
**Sponsor tools:** Anthropic Claude API (Generating situational briefs, supporting)
**AI:** Claude Sonnet via Anthropic API summarizes the ranked event set into a brief; orbit propagation uses deterministic SGP4, not ML.
**Architecture:** Next.js 15 dashboard with CesiumJS and Recharts calls a FastAPI REST backend that scrapes SOCRATES, propagates orbits with SGP4, ranks events, caches in memory and calls Claude.
**Novelty:** Real scraped orbital data with physically propagated tracks and a closest-approach time scrubber, rather than a static chart.
**Scope:** medium · working: Pipeline described as working end to end live; repo has backend endpoints and large Cesium frontend (~13k LOC); video linked. · polish: Detailed README with architecture and setup; no tests or hosted demo.
**Claims:** Camera snaps within a second of true closest approach | 91 propagated positions per satellite in TCA mode
**Gaps:** Video not watched; Page says 91 positions; README says 60 s steps; No live demo
Sources: https://devpost.com/software/oribital-breif, evidence/bitcamp-bitcamp-2026-apsora-brief.json, https://bitcamp-2026.devpost.com/

---

### Arcane Shell
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Bitcamp Game Jam Track Hack - Bitcamp

**What it is:** A first-person wizard combat game in the browser (Three.js) where a Wii Remote acts as the wand and gestures cast spells, plus a 7-inch touch screen in a 3D-printed grimoire case for crafting spells and solving altar mini-games.
**Problem / user:** Existing wizard games reduce spellcasting to button clicks; aimed at players who want to physically cast spells.

**Features**
- Wii Remote wand — WiimoteHook sends gyro and accelerometer data over UDP to a bridge; used for pointer aim and gesture detection. *[claimed]*
- Gesture spellcasting — Specific wand gestures cast spells against enemies in first-person PVE stages. *[claimed]*
- Haptic feedback — Rumble sent to the Wii Remote through xinput-ffi. *[claimed]*
- Grimoire second screen — Separate web page on a touch LCD syncs over WebSockets for crafting spells and altar mini-games. *[claimed]*
- Procedural assets — All props, maps, enemies and spell animations built in code, no 3D asset files. *[shown_working]*
- Keyboard and mouse fallback — Game runs without the Wii bridge. *[shown_working]*

**Flow:** Start the dev server and open the game → Aim with the wand or mouse → Cast spells by gesture to fight enemies → Reach an altar that triggers a grimoire mini-game → Solve it on the tablet and craft new spells

**Prompt:** Best Bitcamp Game Jam Track Hack: theme Echo, freely interpreted if justified; game must run on Windows or in the browser, be free, and have no NSFW content.
**Fit (none):** Browser game with a custom hardware wand and grimoire; page and README do not explain how it connects to the Echo theme.  *(targeted: Best Bitcamp Game Jam Track Hack - Bitcamp)*
**AI:** Mediapipe is listed as a dependency; its role is not explained and no AI is described.
**Architecture:** Vite/TypeScript/Three.js game with a Node WebSocket bridge reading WiimoteHook DSU data; separate crafting page (craft.html) on a second display synced via WebSockets.
**Novelty:** Physical motion wand and 3D-printed grimoire second screen with fully procedural 3D content.
**Scope:** medium · working: About 23k LOC repo with run instructions and Wii bridge; demo video linked; no hosted build. · polish: Custom animations and sounds; hardware issues and a misprinted case reported.
**Claims:** Minimal Wii Remote latency over Bluetooth | Gesture detection consistent and resistant to misfires (qualitative)
**Gaps:** Echo theme link not stated; Mediapipe role unexplained; Video not watched
Sources: https://devpost.com/software/arcane-shell, evidence/bitcamp-bitcamp-2026-arcane-shell.json, https://bitcamp-2026.devpost.com/

---

### arena
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Neelbauer Agentic Revolution Award (NARA) - Alumni Prize

**What it is:** An autonomous red-team versus blue-team loop running against a deliberately vulnerable FastAPI server. A local llama3 attacker probes it, a rule-based defender reacts, and Gemini writes patches that are verified by replaying the original exploit.
**Problem / user:** Security tools find vulnerabilities but rarely prove a fix works; aimed at developers and security teams (not named explicitly).

**Features**
- Red team agent — Ollama llama3 chooses the next attack on the live target, with a programmatic override forcing endpoint diversity. *[claimed]*
- Blue team — Rule-based defender detects and mitigates attacks in real time. *[claimed]*
- Entropy pruning of telemetry — SEMA-style structural entropy cuts 28 log attributes to 8-10 high-signal ones before LLM calls. *[claimed]*
- Gemini reports and patches — At episode boundaries Gemini writes a vulnerability report and code patch. *[claimed]*
- Exploit-replay verification — The original exploit is re-run against the patched endpoint; patch rejected if it still works; passes get verified=True badge. *[claimed]*
- Live patching — Fetches source of running FastAPI route, execs patch in controlled namespace, atomically swaps route.endpoint. *[claimed]*
- Web dashboard — React/TypeScript/Tailwind UI with WebSocket updates of the simulation. *[claimed]*

**Flow:** Target API and arena loop start in one uvicorn process → LangGraph runs red, blue, prune, evaluate, risk nodes each step → Red picks an attack; blue detects and mitigates → Telemetry is pruned before LLM calls → Gemini reports and patches at episode end → Patch applied live and verified by replaying exploit → Next episode attacks the patched app

**Prompt:** Alumni-sponsored award for the best example of trained and initially prompted AI agents launched at Bitcamp that autonomously red team.
**Fit (implied):** Autonomous attacker and defender agents (LLM red team, Gemini patcher) close an attack-patch-verify loop without human input; page does not name the prize itself.  *(targeted: Neelbauer Agentic Revolution Award (NARA) - Alumni Prize)*
**Sponsor tools:** Google Gemini API (Vulnerability reports and patch generation, core)
**AI:** Local llama3 via Ollama drives attacks; Gemini generates reports and patches; SEMA-style structural entropy pruning reduces telemetry; LangGraph orchestrates nodes.
**Architecture:** One uvicorn process hosts the vulnerable FastAPI target and a LangGraph StateGraph background thread (shared STATE_LOCK); WebSocket feeds a React dashboard; Gemini called at episode boundaries.
**Novelty:** Uses the system's own exploits as regression tests for generated patches, and adapts an RTS-agent entropy pruning method to security logs; runs on free tiers and local inference.
**Scope:** small · working: Detailed description of live patching and threading fixes; no repo or demo video linked. · polish: React dashboard described; no screenshots or video confirmed.
**Claims:** Claims first application of SEMA-style entropy pruning outside RTS agents | Gemini patches often fail verification, making the badge meaningful | Runs entirely on free-tier APIs and local inference
**Gaps:** No repo linked on Devpost; No demo video; Gemini model given as gemini-1.5-flash in tags
Sources: https://devpost.com/software/arena-o718na, https://bitcamp-2026.devpost.com/

---

### BlindSight
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best App Dev Track Hack - Bitcamp

**What it is:** An iPhone app that guides blind users through indoor spaces. A spoken or typed destination is broken into subgoals by Gemini, found by on-device YOLOE detection, and followed using LiDAR obstacle zones, haptics and spatial audio.
**Problem / user:** Blind and visually impaired people needing independent indoor navigation where canes warn only on contact and guide dogs are scarce.

**Features**
- Destination to subgoals — Gemini sees camera snapshots and picks secondary goals (e.g. find hallway, then elevator) used as YOLOE text prompts. *[shown_working]*
- Open-vocabulary detection — YOLOE11S Core ML model tracks the current prompt on-device from sampled camera frames. *[shown_working]*
- ARKit SLAM and waypoint tracking — Tracks position, maps environment, re-routes user after abrupt turns. *[claimed]*
- LiDAR obstacle avoidance — ARKit scene depth/mesh defines obstacle zones; haptic alerts and beeps for nearby obstacles. *[shown_working]*
- Spatial audio guidance — AVAudioEngine spatial graph with head tracking points toward the path/target. *[shown_working]*
- Voice commands — Wake word routes follow-up questions with latest snapshot to Gemini; TTS replies. *[shown_working]*

**Flow:** Grant camera and speech permissions → Speak or type a destination → Full-screen navigation starts with ARKit session → Gemini picks subgoals from snapshots → YOLOE tracks the subgoal; audio and haptics guide → Voice wake word to ask questions

**Prompt:** Best hack demonstrating app development principles and incorporating App Dev workshop content.
**Fit (implied):** A native SwiftUI iOS app using ARKit, Core ML, Core Haptics and spatial audio; no explicit mention of workshop content.  *(targeted: Best App Dev Track Hack - Bitcamp)*
**AI:** Gemini (README: gemini-2.5-flash; Devpost: Gemini 3) for subgoals and Q&A; YOLOE open-vocabulary detection exported to Core ML and run on-device; LiDAR depth for avoidance.
**Architecture:** SwiftUI app; SpatialAudioTestEngine owns ARSession, YOLOEService (Core ML), GeminiService (REST), speech and voice command services, and an AVAudioEngine spatial graph; Python scripts export models.
**Novelty:** Combines LLM subgoal planning, open-vocabulary detection, LiDAR and head-tracked spatial audio on one phone for zero-shot indoor navigation.
**Scope:** medium · working: About 8k LOC Swift app, demo video, tested on iPhone 15 Pro; arrival detection weak. · polish: Architecture diagram in README; overheating forced frame throttling.
**Claims:** Spatial audio can autonomously guide around obstacles to a destination | Waypoint tracking redirects after abrupt turns | Frames processed every 1-2 seconds to limit overheating
**Gaps:** Gemini version differs (README 2.5-flash vs Devpost Gemini 3); feature list follows both; Video not viewable
Sources: https://devpost.com/software/blindnav-yzd8fh, https://github.com/aidenjcheng/blindsight, evidence/bitcamp-bitcamp-2026-blindsight.json

---

### Catan Tactics
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Neelbauer Agentic Revolution Award (NARA) - Alumni Prize

**What it is:** Four AI players with distinct personalities play and negotiate full games of Catan locally. A self-trained value network scores moves, a local LLM calls tools to choose actions, and AlphaBeta lookahead verifies them.
**Problem / user:** Catan has randomness and hidden information, and existing bots rely on hardcoded rules; no named user, an experiment in agentic game play.

**Features**
- RL value network — Feedforward net on 30 board features predicts win probability per legal action; trained via random, AlphaBeta, then self-play curriculum. *[claimed]*
- Agentic tool-calling LLM — qwen2.5:14b via Ollama calls analyze_position, check_threats, get_best_move, simulate_outcome, execute_action as JSON, max 6 calls per turn. *[shown_working]*
- AlphaBeta lookahead — Used as a verification tool on a single candidate action. *[shown_working]*
- Negotiation after dice rolls — Favor requests need reciprocal offers; accept/decline uses VP gaps and reputation. *[claimed]*
- Reputation system — Honored and broken promises scored and injected into LLM context. *[claimed]*
- Live web UI and negotiation viewer — Docker-hosted board at localhost:3000 with timeline of negotiation conversation. *[claimed]*
- Fully local — No cloud API calls in the final system. *[claimed]*

**Flow:** Start Docker UI and local Ollama → Dice roll triggers negotiation phase → LLM gets board state and legal actions → LLM calls tools one at a time → Turn ends with execute_action → Watch board and negotiation timeline

**Prompt:** Alumni-sponsored award for the best example of trained and initially prompted AI agents launched at Bitcamp that autonomously red team.
**Fit (implied):** Multi-agent LLM system with tool-calling over RL and search tools; README is about game agents, not red teaming.  *(targeted: Neelbauer Agentic Revolution Award (NARA) - Alumni Prize)*
**AI:** PyTorch value net via supervised AlphaBeta imitation and curriculum self-play; qwen2.5:14b agent orchestrates tools with JSON fallback; AlphaBeta search as verifier.
**Architecture:** Fork of Catanatron simulator plus agent_tools, AgentPlayer, favor system and RL value network; Flask/PostgreSQL/React UI in Docker; Ollama local LLM.
**Novelty:** Layers LLM goal-setting over an RL scorer and search verifier, with a promise-based negotiation economy; built on the open-source Catanatron fork.
**Scope:** medium · working: Video embedded; README documents pipeline files; repo is a full Catanatron fork (~23k LOC, most upstream). · polish: Docker UI and custom negotiation viewer; no results reported.
**Claims:** Final system runs with no cloud APIs | Value network trained from self-play with no human Catan knowledge | No win rates reported
**Gaps:** README top is upstream Catanatron; project section only partly read (first 7000 chars); Unexplained Canva link
Sources: https://devpost.com/software/catan-tactics, https://github.com/DarekYu/Catanatron, evidence/bitcamp-bitcamp-2026-catan-tactics.json

---

### Cherry Canary
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Social Good Hack - Bitcamp

**What it is:** A chest-worn wearable plus dashboard for people with COPD or asthma that watches the heart rate versus breathing rate relationship to warn before blood oxygen falls. Gemini explains alerts and long-term trends.
**Problem / user:** People with respiratory conditions; pulse oximeters and wearables alert only after SpO2 has already dropped.

**Features**
- Divergence engine — Compares heart rate and breathing rate to a personal baseline and maps four patterns to states from info to emergency. *[shown_working]*
- Chest sensor hardware — ESP32 with MAX30102 and MPU-6050 posts JSON every 2s (README: 25Hz); IMU gives breathing rate and depth. *[shown_working]*
- Gemini alerts and long-term insights — Explains detected pattern and summarizes multi-day vitals for wellness insights. *[shown_working]*
- Dead Man's Switch — If both vitals drop, asks for confirmation; no reply in 30s alerts emergency contact (README mentions SMS). *[claimed]*
- 3D breathing visualization — Three.js live view of breath depth and rhythm. *[shown_working]*
- Clinical export and session replay — Downloadable session history and analysis for a pulmonologist; session record/replay. *[claimed]*
- Mock and ML modes — Simulator patterns, data collection, Random Forest/1D CNN training with rules fallback. *[shown_working]*

**Flow:** Onboarding sets baselines → Wearable streams data to backend → Dashboard shows vitals and 3D breathing → Engine flags divergence and Gemini writes alert → Dead Man's Switch prompts on dual drop → Review insights and export report

**Prompt:** Does the hack solve a social problem or help empower a marginalized community?
**Fit (implied):** Targets early warning for respiratory patients, citing COPD/asthma prevalence and readmission data; Devpost also lists a GoDaddy domain.  *(targeted: Best Social Good Hack - Bitcamp)*
**Sponsor tools:** Google Gemini API (Real-time alert text and long-term analysis, core); Featherless.ai and Netcore SMS (README) (Coaching and caregiver SMS, supporting); GoDaddy domain (Project domain, token)
**AI:** Rule-based state machine with optional Random Forest/1D CNN classifier; Gemini generates alerts and summaries; Featherless Llama for coaching per README.
**Architecture:** ESP32 posts to FastAPI backend (README) with rolling buffer, signal processor, classifier, MongoDB; WebSocket to Next.js dashboard. Devpost says Flask.
**Novelty:** Targets a heart/breath divergence signal prior to desaturation using custom IMU plus PPG hardware, with a dual-drop safety check.
**Scope:** medium · working: Hardware build, ~13k LOC backend/frontend, mock mode, demo video. · polish: Three.js visuals, Figma design, clinical export.
**Claims:** Compensation may start 10-30 minutes before oximeter alarms (unvalidated) | Built end to end in 36 hours | Cites 85% inhaler misuse among COPD patients
**Gaps:** Devpost says Flask and 2s posts; README says FastAPI and 25Hz; feature list follows both; Devpost tags MongoDB/React
Sources: https://devpost.com/software/cherry-canary, https://github.com/ShreeyaG3/Cherry_Canary, evidence/bitcamp-bitcamp-2026-cherry-canary.json

---

### Circuitry with Neural Networks
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Most LIT Hack - Alumni Prize

**What it is:** A physical LED neural network display. A user draws a digit on a computer, the net classifies it, and LED strips arranged as layers light up the activated neurons, color-coded by layer.
**Problem / user:** Learners who find neural network basics abstract; meant for classroom or museum style displays.

**Features**
- Digit drawing and classification — User draws a digit in a JavaScript frontend which classifies it with a discrete-weight network. *[claimed]*
- Physical LED activation — Frontend sends serial signals to an Arduino UNO that lights LEDs for activated neurons. *[claimed]*
- Color-coded layers — Each layer shown in a different color on hundreds of soldered LEDs. *[claimed]*
- Hover to trace causes — Hovering an activated neuron shows which previous-layer neurons contributed. *[claimed]*

**Flow:** Draw a digit on the computer → Network classifies it → LEDs light activated neurons by layer → Hover a neuron to see contributing neurons

**Prompt:** Most LIT Hack, judged by the number of LEDs used (screens do not count).
**Fit (implied):** Hundreds of LEDs hand-soldered into a visible network; the LED count is the judging criterion.  *(targeted: Most LIT Hack - Alumni Prize)*
**AI:** Small digit classifier with discrete weights; architecture and training not described; backpropagation training listed as future work.
**Architecture:** JavaScript/HTML frontend classifies drawn digits and sends serial commands to an Arduino UNO driving LED strips.
**Novelty:** Turns a neural network into a physical LED artifact; pivoted from a conductance-based physical network idea.
**Scope:** small · working: Devpost states frontend-to-Arduino serial control works; no video. · polish: Minimal README (~900 LOC); no demo video or screenshots confirmed.
**Claims:** Dynamic LED updates from the computer frontend over serial
**Gaps:** Model architecture and training not documented; LED count not stated
Sources: https://devpost.com/software/circuitry-with-neural-networks, https://github.com/ahamme2330/Neural-Number-Recognizer, evidence/bitcamp-bitcamp-2026-circuitry-with-neural-networks.json

---

### Clarify
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence C · confidence low*
**Prizes:** Best Digital Forensics Related Hack - Cipher Tech Solutions

**What it is:** A digital forensics project whose Devpost page gives only a tagline about revolutionizing digital forensics through novel data modeling, a built-with list and a note that the team will keep building. No description, repo or video is published.
**Problem / user:** Not stated beyond the digital forensics domain.

**Features**
- Digital forensics data modeling — Only the tagline 'novel data modeling' is given; mechanism not described. *[unclear]*

**Prompt:** Best application pertaining to digital forensics or reverse engineering (Cipher Tech Solutions).
**Fit (implied):** Tagline places it in digital forensics; no details on what it does.  *(targeted: Best Digital Forensics Related Hack - Cipher Tech Solutions)*
**AI:** none
**Architecture:** Stack tags only: FastAPI backend, Next.js/React/TypeScript frontend.
**Novelty:** Cannot be assessed; page has no content beyond tagline.
**Scope:** small · working: None published. · polish: None published.
**Gaps:** No description, repo, video; Page shows Winner in one read and an update listing Runner Up in another
Sources: https://devpost.com/software/clarify-ztm49p (WebFetch and Chrome), https://bitcamp-2026.devpost.com/

---

### CrisisMatch
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Beginner Data Science Track Hack

**What it is:** A web app that shows global crises on a live map with ship and plane positions, has several AI agents debate the situation, and then automatically ranks volunteers to match the need. Every feature has hardcoded fallbacks for demos.
**Problem / user:** People who want to act on disasters and volunteers who could be matched to relief needs; news shows crises without a way to help.

**Features**
- Live crisis map — Leaflet map with AISStream ship markers, OpenSky planes, crisis zones, NGO locations; six preloaded crises. *[claimed]*
- Multi-agent AI debate — Claude, Gemini and a Gemini-search news agent run in parallel; a synthesizer reports consensus and verdict. *[claimed]*
- Autonomous volunteer matching — Runs automatically after each debate; ranks volunteers by weighted skill score. *[claimed]*
- Auth0 volunteer login — Login creates a volunteer profile used in matching; names hidden for safety. *[claimed]*
- Crisis timeline — Chronological events per crisis. *[claimed]*
- Fallback data — Hardcoded realistic fallbacks when APIs or keys are missing. *[claimed]*

**Flow:** Open dashboard and pick a crisis → Watch ships and planes on the map → Agents debate and synthesize → Volunteers matched automatically → Optional Auth0 login for profile

**Prompt:** No criteria text on the Devpost page; only a certificate of recognition is listed.
**Fit (implied):** Combines live ship, plane and weather data feeds with AI analysis; README also lists many other prizes it targeted.  *(targeted: Best Beginner Data Science Track Hack)*
**Sponsor tools:** Auth0 (Volunteer login and identity for matching, supporting); Google Gemini API (Debate and news agents, core); Claude API (Geopolitical agent and synthesizer, core)
**AI:** Three parallel LLM agents (Claude, Gemini, Gemini with search) plus a synthesizer; volunteer ranking by weighted sum of skill matches.
**Architecture:** React/Vite/Leaflet frontend with Auth0; Express backend routes for debate, crises, volunteers, map proxy; WebSocket ship feed.
**Novelty:** Joins live logistics feeds with multi-model debate and automatic volunteer matching.
**Scope:** medium · working: Repo ~5.5k LOC with quick start; no demo or video. · polish: Dark map UI and fallbacks; project name inside repo is 'HormuzWatch'.
**Claims:** Map refreshes every few seconds with real ship positions | Agents run concurrently to cut wait | Autonomous crisis discovery is not yet built
**Gaps:** Devpost says three brains but names two; README names three; Evidence from default branch of a shared repo; project is on the crisis-match branch; No track criteria text
Sources: https://devpost.com/software/crisismatch, https://github.com/Bharathisthe/habibi/tree/crisis-match, evidence/bitcamp-bitcamp-2026-crisismatch.json

---

### Cropora - Field Intelligence Platform
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Sustainability Hack - Bitcamp

**What it is:** A Streamlit dashboard for Iowa cropland that classifies every pixel as rotation, monoculture or irregular from 11 years of USDA crop maps, predicts crop type with random forests and scores field resilience.
**Problem / user:** Farmers, lenders, insurers and agronomists who commit to inputs or loans before knowing the season's crop outcome.

**Features**
- NDVI phenology analysis — Crop-specific NDVI curves for corn and soybean across the season. *[claimed]*
- Rotation classification — Every Iowa cropland pixel labeled regular, monoculture or irregular using CDL 2013-2023. *[claimed]*
- Crop-type prediction — Two random forests: NDVI-only (78%) and CDL history (96%); projects 2024 with per-pixel confidence. *[claimed]*
- Field Resilience Score — 0-100 composite of rotation consistency, diversity and recent stability. *[claimed]*
- Interactive dashboard — Iowa region map, rotation threshold what-if slider, field lookup with plain-English lending advice. *[claimed]*

**Flow:** Open Streamlit dashboard → Select an Iowa region → Adjust rotation threshold → Look up a field for recommendation

**Prompt:** Does the hack help the environment or solve a sustainability issue?
**Fit (implied):** Uses satellite and soil moisture data to expose rotation and monoculture patterns, framing resilience for lending and risk; no explicit prize statement.  *(targeted: Best Sustainability Hack - Bitcamp)*
**AI:** scikit-learn random forests on NDVI features and multi-year crop history; no LLM.
**Architecture:** Three Colab notebooks (data prep, models, analysis) aligned with rasterio, outputs served by Streamlit/Plotly app.
**Novelty:** Uses rotation history as a lending-risk signal and compresses a 4.7GB 30m stack to 47MB at 300m.
**Scope:** small · working: Live Streamlit link and stated accuracies; repo not published. · polish: Dashboard with map and slider; no video.
**Claims:** NDVI model 78% accuracy, CDL history 96% | Downsample cut stack from 4.7GB to 47MB | Predicted 2023 map visually indistinguishable from ground truth
**Gaps:** No repo linked; Dashboard not opened
Sources: https://devpost.com/software/cropora-field-intelligence-platform

---

### cryptX by Moonshot
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Financial Hack - Capital One; Best App Dev Track Hack - Bitcamp

**What it is:** A DIY hardware wallet for Solana built on an Arduino Uno with an LCD and two buttons. Keys and signing stay on the device; a Next.js dashboard builds and relays transactions on testnet and uses Gemini to flag suspicious device behavior.
**Problem / user:** Crypto users who want hardware-backed transaction signing without the roughly $150 cost of a commercial hardware wallet.

**Features**
- On-device signing with button approval — Dashboard builds the transaction, the Arduino signs after physical confirm, dashboard relays signed bytes to Solana testnet. *[shown_working]*
- PIN and BIP-39 seed backup — 6-digit PIN setup; seed words shown one by one on the LCD and verified before signing. *[shown_working]*
- Challenge-response device auth — SipHash-2-4 keyed from chip hardware signature, fresh challenge per connection. *[claimed]*
- Self-destruct wipe — Three wrong PIN attempts reset EEPROM and erase wallet state. *[claimed]*
- Gemini fraud detection — Device logs analyzed for repeated auth failures, mid-transaction disconnects, odd signing velocity, unknown signatures. *[claimed]*
- Device blacklist — Flagged devices are written to a blacklist and blocked from submitting transactions. *[claimed]*
- Live dashboard — Balance, on-chain history, AI risk reports and device status; Web Serial over USB at 115200 baud. *[shown_working]*

**Flow:** Set PIN on device → Back up seed phrase on LCD → Connect device to dashboard over USB → Dashboard builds a SOL transfer → Approve on device button → Signed tx submitted to Solana testnet → Gemini audits logs and may blacklist

**Prompt:** Capital One track: the best financial hack, intentionally vague. App Dev track: demonstrate app development principles using workshop content.
**Fit (explicit):** A low-cost hardware wallet for moving money on Solana with fraud monitoring; README banner lists the Capital One win and a 2nd place App Dev note.  *(targeted: Best Financial Hack - Capital One, Best App Dev Track Hack - Bitcamp)*
**Sponsor tools:** Google Gemini API (Log audit, risk reports, fraud flags, core); Auth0 (Dashboard login, supporting); Solana (testnet) (Transactions and balances, core)
**AI:** Gemini agent via Vercel AI SDK reads device event logs through /api/audit and /api/insights and produces risk reports and blacklist decisions.
**Architecture:** Arduino Uno firmware (PIN state machine, BIP-39, SipHash, EEPROM, LCD) talks over USB serial to a Next.js app using Solana Web3.js, MongoDB logs/blacklist, Gemini, Auth0, on Vercel.
**Novelty:** Working microcontroller hardware wallet reverse-engineered from Ledger-style flow with an AI audit layer, built by a team new to hardware.
**Scope:** medium · working: Hardware build, live site, YouTube demo in README, ~7.9k LOC firmware and dashboard. · polish: Polished README with API reference, shadcn UI, domain.
**Claims:** Built working hardware wallet in 36 hours with no hardware experience | Private key never leaves the device | Three wrong PINs wipe the device
**Gaps:** README says 2nd place App Dev; queue lists as App Dev prize; Testnet only; no security audit
Sources: https://devpost.com/software/cryptx-zceo69, https://github.com/navincodesalot/cryptx/, evidence/bitcamp-bitcamp-2026-cryptx-by-moonshot.json

---

### Crystal Forge
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Computational Quantum Track Hack

**What it is:** A solver-routing and measurement-planning framework for strongly correlated electron models (Fermi-Hubbard, TFIM). A classifier decides whether cheap classical solvers can be trusted, and a planner picks observables to measure, with a Minecraft mod as 3D front end.
**Problem / user:** Quantum materials researchers who cannot tell in advance where mean-field or tensor-network solvers silently fail and waste quantum measurements.

**Features**
- CorrMap classifier — MLP on 49 features (22 physics plus 27 intrinsic diagnostics) labels regimes classical_scalable or quantum_frontier; held out on 8x8 lattices. *[shown_working]*
- QProbe planner — Adaptive choice of observables (charge, spin, transport, pairing) to measure next; rebuilt around superconductivity channels. *[claimed]*
- Physics solvers — Backend solvers and Qiskit-based VQE paths for the models. *[claimed]*
- FastAPI workflow endpoint — POST /api/minecraft/workflow returns scene, routing verdict and observables. *[shown_working]*
- React dashboard — Runs workflows and inspects results; integration called incomplete. *[claimed]*
- Minecraft Fabric mod — Renders the lattice in 3D with control wall to change model and parameters live. *[claimed]*

**Flow:** Start backend → Launch dashboard or Minecraft client → Mod fetches default TFIM preset on join → Right-click control wall to change parameters → Scene updates with routing verdict and observables

**Prompt:** For people with little quantum experience: use classical algorithms or solvers to solve a quantum-related problem.
**Fit (implied):** Uses classical ML and solvers to decide when quantum treatment is needed and to allocate quantum shots.  *(targeted: Best Computational Quantum Track Hack)*
**AI:** PyTorch MLP classifier (CorrMap) on physics and diagnostic features; QProbe adaptive measurement planning over posterior.
**Architecture:** FastAPI backend (physics, solvers, ML, API) is source of truth; React/Vite dashboard and Fabric 1.20.4 Java mod call the same REST endpoint.
**Novelty:** Pairs a regime-routing classifier with measurement planning and a Minecraft walk-through visualization.
**Scope:** large · working: Backend, frontend and mod in repo; tests present; no video. · polish: README with architecture and quick start; Devpost admits frontend integration incomplete.
**Claims:** CorrMap 85% accuracy on quantum-need classification | Measurement workflow more than tripled hard-sector coverage vs naive | Generalizes to unseen 8x8 lattices
**Gaps:** File count inflated by committed node_modules; Mod not confirmed running
Sources: https://devpost.com/software/crystal-forge, https://github.com/Pvphantom/bitcamp2026-crystal-forge, evidence/bitcamp-bitcamp-2026-crystal-forge.json

---

### Diabuddy
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Gamification Hack - Bitcamp

**What it is:** A mobile app with a virtual pet for children with type 1 diabetes. Kids log blood sugar and insulin in a diary, chat with a supportive bot, earn coins from healthy logging and minigames, and spend them on pet skins and room items.
**Problem / user:** Children with diabetes, who face stress and anxiety managing it; caregivers and clinicians are a planned secondary audience.

**Features**
- Virtual pet — Pet to care for and customize with skins, accessories and room decor. *[shown_working]*
- Diary log — Entries for blood sugar, insulin, carbs, activities and notes. *[shown_working]*
- Blood sugar graph — Home screen line graph of logged glucose. *[shown_working]*
- Child-friendly chatbot — Encouragement and simple guidance; repo backend includes an OpenAI client. *[shown_working]*
- Coin rewards and store — Coins for healthy logs and minigames, spent in a store on skins and accessories. *[shown_working]*
- Minigames — Flashcards and Food Collector (avoid unhealthy foods, collect healthier ones). *[shown_working]*
- Parent or provider reports — PDF-style shareable reports. *[planned]*

**Flow:** Log glucose and insulin in diary → Earn coins for healthy logs → Play flashcards or Food Collector → Spend coins in store → Chat with the pet bot

**Prompt:** Created a hack that gamifies an everyday task.
**Fit (implied):** Turns daily diabetes logging into pet care with coins, minigames and a store; page does not name the prize.  *(targeted: Best Gamification Hack - Bitcamp)*
**AI:** Chatbot companion (OpenAI client in backend); app itself generated with Appifex, with Claude and ChatGPT used for prompt refinement and debugging.
**Architecture:** Expo React Native mobile app with FastAPI/SQLAlchemy/PostgreSQL backend; repo README is the Appifex stub.
**Novelty:** Pairs a Finch-style pet loop with diabetes self-management for children; app was generated largely through an AI app builder.
**Scope:** small · working: Screenshots listed for seven screens; ~5.9k LOC; no video. · polish: Pastel child-friendly UI iterated by prompting; no tests or real README.
**Claims:** No outcomes or user testing reported
**Gaps:** README is a generator stub; Chatbot model not stated on Devpost
Sources: https://devpost.com/software/diabuddy-oqa67v, https://github.com/nannapat-tippayarat/diabuddy.git, evidence/bitcamp-bitcamp-2026-diabuddy.json

---

### Docket
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [MLH] Best Use of Auth0

**What it is:** A web app that layers context onto GitHub history: it shows repositories and an interactive SVG branch/commit graph, has Gemini summarize what each commit changed, and lets developers attach permanent notes explaining why.
**Problem / user:** Developers, teams and students who forget or lose the reasoning behind commits because GitHub records only what and who.

**Features**
- GitHub sign-in via Auth0 — Auth0 with GitHub OAuth requesting repo access; needed read:user_idp_tokens scope. *[shown_working]*
- Repository dashboard — Cards with live stats and a count of undocumented commits. *[shown_working]*
- Interactive branch and commit graph — SVG graph; hover previews, click opens detail panel. *[shown_working]*
- Gemini commit summaries — Compares each commit to the previous on its branch and explains functional change. *[shown_working]*
- Per-commit developer notes — Saved in Supabase; also lets users correct AI errors. *[shown_working]*
- TerpAI profile assistant — Answers questions about GitHub activity. *[claimed]*
- Vulnerability report tab, team notes, VS Code extension — Listed future work. *[planned]*

**Flow:** Sign in with GitHub through Auth0 → Browse repo cards → Open a repo branch graph → Hover or click a commit → Read AI summary and add a note → Optionally ask TerpAI

**Prompt:** Use any Auth0 APIs in the project (MLH Best Use of Auth0).
**Fit (implied):** Auth0 is the login layer for GitHub OAuth and supplies the identity provider token used for all GitHub API calls.  *(targeted: [MLH] Best Use of Auth0)*
**Sponsor tools:** Auth0 (GitHub/Google/email login and IdP token for GitHub API, core); Gemini API (Commit summaries, core)
**AI:** Gemini summarizes diffs between consecutive commits on a branch; a TerpAI assistant answers profile questions.
**Architecture:** Next.js App Router on Vercel; Auth0 login; GitHub REST v3 for data; Supabase for notes and commit metadata; Gemini for summaries; SVG graph.
**Novelty:** Adds a durable human-reasoning layer over git history rather than just visualizing it.
**Scope:** small · working: Live deployment at trydocket.us; four screenshots; no repo listed. · polish: Deployed on Vercel with login; no video.
**Claims:** Fully deployed at trydocket.us
**Gaps:** no repo; no video; site not opened
Sources: https://devpost.com/software/docket-2r9wke, https://bitcamp-2026.devpost.com/

---

### DoortectiveAI
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** People's Choice Hack - Bitcamp; [MLH] Best Use of ElevenLabs

**What it is:** A smart door device built on a Raspberry Pi with camera and mic that recognizes known faces, converses with visitors using an ElevenLabs voice, judges intent with Gemini, and phones the homeowner via Twilio when a visit looks threatening.
**Problem / user:** Homeowners whose security systems only record and notify after a break-in rather than acting at the door.

**Features**
- Visitor detection and tracking — OpenCV with YOLOv8n at about 10-15 FPS detects and tracks people. *[claimed]*
- Face recognition — Matches against stored embeddings, labels unknowns and raises a suspicion score. *[claimed]*
- Gemini intent reasoning — Combines vision signals, transcribed speech and behavior to label normal, suspicious or threat. *[claimed]*
- ElevenLabs conversational voice — Speaks in normal, suspicious or threat tone, multilingual. *[claimed]*
- Code-based guest verification — Visitors authenticate with a secure code. *[claimed]*
- Twilio emergency call — Phones homeowner with an AI voice summary on high risk. *[claimed]*
- LED state indicators and dashboard — LEDs show system state; web dashboard has history and profiles. *[shown_working]*

**Flow:** Camera detects a person → OpenCV classifies known/unknown/multiple → Visitor speech is transcribed → Gemini decides intent and tone → ElevenLabs replies at the door → Twilio calls homeowner if high risk

**Prompt:** ElevenLabs prize: win wireless earbuds (no challenge text published beyond the name); People's Choice: hackers vote on favorites.
**Fit (implied):** ElevenLabs conversational agents give the door its spoken replies with tone modes; People's Choice is a vote and not tied to a brief.  *(targeted: People's Choice Hack - Bitcamp, [MLH] Best Use of ElevenLabs)*
**Sponsor tools:** ElevenLabs (Low-latency voice replies with tone modes, core); Gemini API (Intent and threat reasoning, core); Twilio (Escalation phone calls, supporting)
**AI:** YOLOv8n and face embeddings for vision; Gemini reasons over speech, vision and behavior to classify; ElevenLabs agent produces speech.
**Architecture:** Raspberry Pi streams camera/mic to a FastAPI event-driven backend that orchestrates OpenCV, Gemini, ElevenLabs and Twilio; Next.js dashboard.
**Novelty:** Active, conversational door agent with hardware, tone-aware responses and phone escalation rather than passive recording.
**Scope:** medium · working: Demo video, hardware setup screenshot, project site doortective.us; repo only an org page. · polish: Dashboard screens and website; stated latencies per stage.
**Claims:** Vision ~50-100 ms per frame | Reasoning ~300-800 ms; voice ~300-700 ms | End-to-end response about 1-2 s
**Gaps:** repo clone failed; org page only; video not watched
Sources: https://devpost.com/software/doortective, https://bitcamp-2026.devpost.com/

---

### EchoLocate
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Moonshot Hack - Bitcamp

**What it is:** A browser game where players run a cyber forensics investigation on a pixel-art lunar city. They deploy specialist AI agents to sectors, question them by chat or voice, and assemble evidence into a case board and graph to trace a simulated breach.
**Problem / user:** Analysts and learners who must reconstruct how a breach moved across systems; framed as a guided, game-like way to practice investigation workflows.

**Features**
- Specialist agents — LOGIS (logs), NEXUS (network), FILER (artifacts), CHRONO (timeline) answer tasks with tool calls; up to 8 in parallel. *[shown_working]*
- Phaser moon-city map — Tiled/Aseprite tile map of Netropolis sectors with incident alerts. *[shown_working]*
- Streamed agent chat — Socket.IO streams thoughts, tool activity and replies. *[shown_working]*
- Evidence feed, case board and graph — Agent JSON becomes graph nodes and edges reconstructing the attack path. *[shown_working]*
- Agent marketplace — Funds, starter specialists and purchasable agents. *[shown_working]*
- Voice radio — ElevenLabs speech interface to talk to agents. *[claimed]*
- Proposal and remediation scoring — Submit claim, execute remediations, final evaluation without revealing the hidden answer. *[shown_working]*
- Tutorial mode — Guided steps with optional text-to-speech. *[shown_working]*

**Flow:** Start investigation from landing page → Build team of agents → Watch map for sector alerts → Deploy agents and send prompts → Evidence fills case board and graph → Submit proposal and remediate → Endgame evaluates the claim

**Prompt:** Most creative, innovative, well-developed hack that shoots for the moon.
**Fit (implied):** Ambitious game fusing multi-agent forensics, a custom map, voice and evidence graphing; it is a fictional training simulation, not real intrusion tooling.  *(targeted: Best Moonshot Hack - Bitcamp)*
**Sponsor tools:** ElevenLabs (Voice radio interface, supporting); Featherless-hosted Qwen (Investigator agent model, core); GoDaddy Registry domain (echolocate.us, token)
**AI:** LangChain tool-calling investigator agents on Claude-compatible/Qwen models (Featherless); role prompts, routing and context injection; JSON findings mapped to graph.
**Architecture:** Next.js/Phaser frontend and Socket.IO to FastAPI backend with in-memory sessions, agent tools, evidence and scoring.
**Novelty:** Frames digital forensics as a multi-agent management game with marketplace and live evidence graph.
**Scope:** large · working: Live site, itch.io build, demo video, ~46k LOC (incl. assets), tests. · polish: Custom pixel art, tutorial, screenshots.
**Claims:** Up to 8 agents in parallel | Level scenarios with controlled randomness
**Gaps:** README is a later personal case study and says Claude models; Devpost says Featherless Qwen, OpenAI and Gemini tags; Legacy modules in repo
Sources: https://devpost.com/software/echolocate-e4k3dg, https://github.com/SujayCh07/bitcamp, evidence/bitcamp-bitcamp-2026-echolocate.json

---

### EcoBuddy
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** TerpAI Ultimate Agent Showdown - Cloudforce/Microsoft

**What it is:** A gamified sustainability companion for UMD students. Users log eco actions by voice or text, can upload a photo as proof, get a 0-100 sustainability score, grow a Terp Turtle buddy and unlock campus-style rewards and event quests.
**Problem / user:** UMD students whose small eco-friendly choices go unnoticed and unrewarded.

**Features**
- Voice or text logging — Gemini extracts intent from the spoken or typed action. *[claimed]*
- Image verification — Hugging Face vision model checks photo against described action; text and image cross-validated. *[claimed]*
- Sustainability score — 0-100 across transport, waste, energy, food and water. *[claimed]*
- Terp Turtle buddy — Mascot evolves as user levels up. *[shown_working]*
- Rewards — Dining credits and promo codes (aspirational). *[claimed]*
- Quests from Today@UMD — Real-time quests generated from scraped campus events. *[claimed]*
- Map and location suggestions — Google Maps for nearby spots like refill stations; stats screen. *[shown_working]*

**Flow:** Log an action by voice or text → Optionally upload photo → Get score and tip → Buddy levels up → Unlock rewards or quests

**Prompt:** Build at least one TerpAI agent that students and/or faculty cannot live without.
**Fit (explicit):** Campus-specific agent layer for UMD students; Devpost gives conflicting accounts of reverse-engineering TerpAI versus building a TerpAI-like Gemini layer.  *(targeted: TerpAI Ultimate Agent Showdown - Cloudforce/Microsoft)*
**Sponsor tools:** TerpAI (Claimed scoring/quest engine, or imitated via Gemini (conflicting), unclear); Google Gemini API (Intent extraction, core)
**AI:** Gemini for NLU, Hugging Face image classifier, LightGBM scoring model chosen over an overfitting decision tree.
**Architecture:** Lovable-built React/Supabase front end; Node/Express orchestration plus Python FastAPI model code; Gemini, Hugging Face and Maps APIs.
**Novelty:** Multimodal verification of eco actions tied to campus events and a mascot.
**Scope:** medium · working: Live Lovable app, demo video, ~11k LOC with tests. · polish: Mascot and shadcn UI; README has placeholder architecture note.
**Claims:** LightGBM improved accuracy on unseen data (no numbers) | Cross-validates text and image output
**Gaps:** TerpAI integration contradicts itself on Devpost; Reward partners not real
Sources: https://devpost.com/software/ecobuddy-i4dyre, https://github.com/KaushalGorla/eco-buddy-voice, evidence/bitcamp-bitcamp-2026-ecobuddy.json

---

### eleQt
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Computational Quantum Track Hack

**What it is:** A quantum-secure electronic voting protocol demo. It applies the GMW multi-party computation scheme with oblivious transfer whose key exchange uses simulated E91 quantum key distribution, plus a simulated zero-knowledge check against double voting, tallying votes without a trusted party.
**Problem / user:** Election integrity if future quantum computers break classical cryptography; aimed at voters and campaigns needing verifiable, trustless tallies without a blockchain.

**Features**
- Quantum oblivious transfer — OT built on E91 QKD instead of classical key exchange, used to evaluate gates of a vote-adder circuit. *[shown_working]*
- GMW multi-party tally — Voters secret-share votes (BCCS 2-to-1) and evaluate a ripple adder; robust to semi-honest adversaries. *[shown_working]*
- Simulated ZKP vote validity — Checks that each voter votes once. *[claimed]*
- Multi-candidate (m,n) simulation — Notebook verifies m-candidate, n-voter election with simulated QKD. *[shown_working]*
- IBM hardware benchmark — 3-voter toy run on a 127-qubit IBM Eagle (Kingston) in about 6 minutes. *[shown_working]*
- Complexity analysis — Main loop derived as O(m n log n). *[claimed]*
- Web demo — FastAPI backend with React/Vite frontend. *[claimed]*

**Flow:** Start backend and Vite site → Configure voters and candidates → Run protocol with simulated QKD → Reveal tally → Optional run on IBM hardware via notebook

**Prompt:** For people with little quantum or physics experience: use classical algorithms or solvers to solve a quantum-related problem.
**Fit (explicit):** Implements quantum cryptography protocols in simulation and on IBM hardware; README title cites 2nd place in the quantum track while Devpost lists Winner.  *(targeted: Best Computational Quantum Track Hack)*
**Sponsor tools:** IBM Quantum (Qiskit) (Hardware run and simulation of OT/QKD circuits, core)
**AI:** No AI core; Claude and Gemini appear only as tags.
**Architecture:** Jupyter notebooks implement GMW, OT and E91 in Qiskit; FastAPI backend serves a React/Vite site.
**Novelty:** Combines GMW MPC with QKD-based oblivious transfer for voting and runs a toy case on real hardware.
**Scope:** small · working: Notebooks with hardware run described, small codebase (~700 LOC), demo video. · polish: Detailed README with theory and complexity doc; modest web UI.
**Claims:** 3-voter run on IBM Kingston in about 6 minutes | Complexity O(m n log n) | Thousands of voters verifiable in under a day on NISQ (inferred)
**Gaps:** README says 2nd place, queue/Devpost say winner; Notebook contents not read
Sources: https://devpost.com/software/qrypt, https://github.com/prakriti-shahi/bitcamp, evidence/bitcamp-bitcamp-2026-eleqt.json

---

### Extract
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Solana

**What it is:** A Solana-based traceability app for vanilla: every handoff from farmer to retailer is dual-signed on-chain, plotted on a map, and visible to consumers who scan a QR code, with organization trust scores and anomaly detection computed from the on-chain history.
**Problem / user:** Vanilla farmers, middlemen and consumers in a supply chain with huge markups, adulterated products and paper records nobody can verify.

**Features**
- Dual-signed handoffs — Anchor program requires sender and receiver to sign each transfer, recording weight, price, grade, GPS and lab results. *[claimed]*
- Consumer QR journey page — Scan shows the full route, badges, lab results, prices and explorer links with no wallet needed. *[claimed]*
- Interactive supply-chain map — Leaflet/Mapbox plots each waypoint and route. *[claimed]*
- Organization trust scores — Computed from confirmation rate, price fairness, weight consistency and lab authenticity, replayable from chain data. *[claimed]*
- Anomaly detection — Flags abnormal weight loss, out-of-range markups and repeated authenticity failures. *[claimed]*
- Org dashboard with Phantom wallet — Organizations start and confirm handoffs. *[claimed]*
- Local validator mode — Single env var switches from devnet to a local validator after faucet rate limits. *[shown_working]*

**Flow:** Farmer logs a harvest on-chain → Each org initiates and confirms a handoff via dashboard → Map plots each hop → Consumer scans QR code on package → Trust scores update from event history

**Prompt:** Show how you can innovate with Solana (MLH Best Use of Solana); prize for each team member.
**Fit (implied):** Core logic lives in a custom Anchor program on Solana: org registration, harvests, two-party signing, lab verification and trust scoring.  *(targeted: [MLH] Best Use of Solana)*
**Sponsor tools:** Solana (Anchor) (On-chain handoffs, verification and trust score computation, core)
**AI:** none
**Architecture:** Rust/Anchor Solana program; Express/Postgres backend with node-cron indexing; Next.js frontend with Leaflet/Mapbox, Recharts and Phantom wallet.
**Novelty:** Full-stack provenance system with on-chain trust scoring and consumer QR verification, built by a team new to Solana.
**Scope:** large · working: Repo ~248 files, ~15k LOC, tests and Docker; no live demo or video. · polish: Detailed README with market statistics and architecture; maps and charts in UI.
**Claims:** Cites up to 80% of pure vanilla products adulterated | Farmers earn $2-3/kg vs $500+ retail
**Gaps:** no video or live demo
Sources: https://devpost.com/software/vanillatrail, evidence/bitcamp-bitcamp-2026-extract.json (README), https://bitcamp-2026.devpost.com/

---

### EyeQ
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Social Good Hack - Bitcamp

**What it is:** A caregiver-abuse detection prototype (repo name CareWatch). Pose estimation on a camera feed flags risky close, fast interactions or long caregiver absence, Gemini reviews the frames, and a guardian gets a push alert plus a saved 30-second clip.
**Problem / user:** Guardians of dependents who cannot report mistreatment (disabilities, dementia, children); cites elder-abuse statistics and the burden of watching footage.

**Features**
- Pose-based flagging — YOLO pose model flags proximity plus fast motion or long caretaker absence. *[shown_working]*
- Gemini verification — Flagged frames are classified for possible physical violence; cooldowns limit calls. *[shown_working]*
- Rolling clip capture — 30-second buffer saves evidence clips with AI explanation. *[shown_working]*
- Push alerts — APNs notifications to iOS app with 5-minute severity dedupe. *[claimed]*
- Dashboard — React live monitoring plus uploaded recording review, alert feed and clip playback. *[shown_working]*
- iOS guardian app — SwiftUI client. *[claimed]*
- Verbal abuse detection — Microphone-based detection. *[planned]*

**Flow:** Start monitoring on dashboard → Camera feed analyzed by pose detector → Flagged frames sent to Gemini → Guardian receives push notification → Review 30s clip with reason and suggested action

**Prompt:** Does the hack solve a social problem or help empower a marginalized community?
**Fit (implied):** Targets protection of vulnerable dependents from caregiver abuse; no explicit prize statement.  *(targeted: Best Social Good Hack - Bitcamp)*
**Sponsor tools:** Google Gemini API (Scene verification of flagged frames, core)
**AI:** YOLO pose heuristics gate frames; Gemini (or OpenRouter model per README) classifies flagged frames; prompt tuned for reliability.
**Architecture:** Python pipeline (detector, classifier, clip saver, alerts) with FastAPI, SQLite log, React dashboard and SwiftUI iOS client.
**Novelty:** Two-stage pose-then-VLM filter so families review short flagged clips rather than hours of footage. Page states no consent or privacy safeguards for monitored people.
**Scope:** medium · working: Backend, dashboard and iOS app in repo (~5k LOC), demo script, video; no accuracy data. · polish: Judge demo script in README; no tests.
**Claims:** Calls itself first intelligent caregiver-abuse detection system | Cites ~30% mistreatment of dependent disabled people
**Gaps:** README names project CareWatch; No evaluation or privacy safeguards stated
Sources: https://devpost.com/software/eyeq-0c8wdl, https://github.com/Haadesx/EyeQ, evidence/bitcamp-bitcamp-2026-eyeq.json

---

### fundingflow
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Real World Prize - Ambrook

**What it is:** A web tool that helps farmers find and apply for government funding. It scrapes USDA program pages with an LLM, recommends programs from a natural-language problem, writes tier-specific application plans and fills government PDF forms.
**Problem / user:** Farmers who cannot find funding they qualify for; existing tools have stale data and no application guidance.

**Features**
- Program discovery — Scrapes government sites with Cheerio and parses with LLM; 82+ deduplicated programs in a Funding Library. *[shown_working]*
- Natural-language matching — Farmer describes a problem (e.g. broken tractor) and gets recommended programs from profile. *[shown_working]*
- Application plans — Personalized, tier-specific plan templates. *[claimed]*
- Form-filling help — AI assistance answering form questions. *[claimed]*
- Auto-filled PDFs — pdf-lib fills government PDF forms. *[claimed]*
- Farm profile — Profile page, shown as a mock. *[claimed]*

**Flow:** Browse Funding Library → Describe a problem → Get recommended programs → Open program page → Generate plan → Download filled PDF

**Prompt:** Ambrook: build a creative project that has a real world component.
**Fit (implied):** Uses real USDA program data and real PDF forms for an end-to-end farm funding workflow; next steps mention Ambrook's platform.  *(targeted: Real World Prize - Ambrook)*
**Sponsor tools:** Featherless.ai (Qwen3-32B) (Four LLM applications: extraction, matching, planning, form help, core)
**AI:** Qwen3-32B via OpenAI SDK on Featherless with strict-schema, low-temperature extraction and context-rich plan generation; HTML cleaned to cut tokens.
**Architecture:** Express backend with Cheerio scraper, LLM services and pdf-lib; plain HTML/JS frontend.
**Novelty:** End-to-end from problem statement to filled PDF using scraped live program data.
**Scope:** small · working: Live demo link and ~4.9k LOC backend with tests; no README or video. · polish: Mock profile page; no daily scraping or auth.
**Claims:** 82+ programs scraped and deduplicated | Four distinct AI applications | Real USDA data, not mocks
**Gaps:** Repo has no README (evidence only has file tree/manifest); Live demo not opened
Sources: https://devpost.com/software/fundingflow, evidence/bitcamp-bitcamp-2026-fundingflow.json

---

### Furrow
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Bitcamp Hack - Bitcamp

**What it is:** A voice-first farm assistant delivered over iMessage/SMS. Farmers text voice notes, photos or messages; Furrow turns them into structured farm logs with chemical compliance checks, answers research questions and sends proactive daily briefings.
**Problem / user:** Farmers making quick field decisions who will not use farm software that needs a laptop, login and training.

**Features**
- Conversational logging — Transcribes voice, reads photos, extracts structured log entries and checks REI/PHI chemical intervals. *[shown_working]*
- Photo classification — Vision model separates crop problems (disease, pest, drought) from purchase receipts and auto-logs applications. *[claimed]*
- Daily briefings (FarmPulse) — Weather, commodity prices, budget burn, soil sensors, deadlines and a recommended action; reply to drill down. *[shown_working]*
- Market and climate research — Exa web search for USDA reports, drought outlooks and input prices. *[claimed]*
- Three-tier routing — Reflex (gpt-4o-mini), Composer (parallel specialists plus Kimi K2.5), Hermes Docker agent for multi-step tasks. *[shown_working]*
- Gmail/Calendar specialists — Composio integrations and Gemini image generation triggered by intent. *[claimed]*
- Proactive alerts — Cron monitor checks thresholds and decides text-now versus batch. *[claimed]*
- Onboarding and dashboard — Signed SMS link to 60-second profile form; React views for alerts, farm log, compliance. *[shown_working]*

**Flow:** Get SMS link and fill profile → Text, voice note or photo to Furrow → Intent router picks tier and specialists → Receive 1-3 reply bubbles → Morning briefing; reply to drill down → Review logs in web dashboard

**Prompt:** Best Bitcamp Hack: hacks that force you to unearth your potential and make organizers want to join the winners by the campfire.
**Fit (none):** Broad, polished multi-agent system with messaging, vision, voice, research and dashboard; page does not tie to the prize wording.  *(targeted: Best Bitcamp Hack - Bitcamp)*
**Sponsor tools:** Featherless (Kimi K2.5) (Reply composition and Hermes agent model, core); Exa (Market and climate research, supporting); Composio (Gmail and Calendar, supporting); Sendblue (iMessage/SMS gateway, core)
**AI:** Intent classifier routes to GPT-4o-mini, parallel specialists with Kimi K2.5 composer, or a Hermes agent; Groq Whisper transcription; GPT-4o vision; images pre-analyzed to avoid tool-call truncation.
**Architecture:** Sendblue webhook to FastAPI/PostgreSQL, IntentRouter, specialist pipelines, BubbleDispatcher; cron MonitorService; Dockerized Hermes agent; Vite/React dashboard.
**Novelty:** Delivers a multi-agent farm operations stack through texting with humanized bubble timing and compliance-aware logging.
**Scope:** large · working: About 16.7k LOC, Docker compose, tests, demo video; Devpost reports end-to-end pipeline. · polish: Architecture images, onboarding page, dashboard screenshots, detailed README.
**Claims:** Simple replies in about one second | Market answers grounded in real 2026 USDA data | Full voice-to-reply pipeline from one message
**Gaps:** README orchestrator wording differs slightly (Kimi vs Groq orchestrator); feature list follows both; Backend internally named CropTalk/FarmPulse
Sources: https://devpost.com/software/furrow, https://github.com/IshaanKalra2103/Furrow/tree/main, evidence/bitcamp-bitcamp-2026-furrow.json

---

### GaitGuard
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Most Philanthropic Hack - Bloomberg

**What it is:** A wearable fall-detection prototype built from an ESP32 and accelerometer. A rules-plus-logistic-regression risk score drives a four-state machine, and a confirmed fall pushes an alert to the caregiver's phone and lights a 600-LED panel.
**Problem / user:** Older adults living alone, including stroke and heart patients, who may lie unattended after a fall, and their caregivers.

**Features**
- Posture baseline and filtering — 120-sample personal calibration, low-pass smoothing and 25-sample rolling window. *[shown_working]*
- Fall risk model — Logistic regression on five motion/posture features blended 0.4 rules plus 0.6 probability. *[shown_working]*
- State machine — NORMAL, SUSPECT, FALL, CANCELLED with exercise abort and PIR confirmation. *[shown_working]*
- Fall direction — Left, right, forward or backward from dominant deviation at impact. *[claimed]*
- Caregiver push alert — ntfy.sh notification with direction, risk, uptime and location link. *[shown_working]*
- LED panel and local feedback — 600 WS2812B LEDs via Arduino Uno show state colors; RGB LED, buzzer. *[shown_working]*
- False-alarm cancel and dashboard — Button cancels; Flask SSE dashboard shows live posture, probability and event log. *[shown_working]*

**Flow:** Device calibrates baseline → Impact spike enters SUSPECT → Stillness plus abnormal posture confirms FALL → Alert sent to caregiver phone → Wearer can cancel with button → Watch live dashboard and LED panel

**Prompt:** Bloomberg prize celebrating the project that best leverages technology to create meaningful social impact.
**Fit (explicit):** Targets elder safety and faster help after falls; README banner cites the Bloomberg philanthropic prize.  *(targeted: Most Philanthropic Hack - Bloomberg)*
**AI:** scikit-learn logistic regression with hand-designed features (no labeled real fall data) blended with rule score.
**Architecture:** ESP32 sensors and FSM, serial link to Arduino Uno LED panel, Flask server with pyserial and SSE dashboard, ntfy alerts.
**Novelty:** Solo hardware build combining ML, state machine and a large physical LED status panel.
**Scope:** small · working: Working prototype with 3D-printed case, ~2.3k LOC, screenshots; no video or accuracy tests. · polish: Detailed README, enclosure, LED panel.
**Claims:** Alert delivered in under 2 seconds | Built solo in 36 hours | No accuracy figures reported
**Gaps:** No training data described; No demo video
Sources: https://devpost.com/software/gaitguard-fk2tb7, https://github.com/Schugh26/GaitGuard, evidence/bitcamp-bitcamp-2026-gaitguard.json

---

### GhostDieDie
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Razzle Dazzle Hack - Bitcamp

**What it is:** Browser-based 3D multiplayer fighting game where each player's real body movements, read from a laptop webcam, control a character. Opponents see each other's live video during matches.
**Problem / user:** Casual players wanting a physical, social motion game without VR headsets or controllers; only a laptop webcam is needed and nothing to install.

**Features**
- Webcam body-pose control — MediaPipe runs in-browser via WebAssembly/GPU, tracking 33 body points at about 20 fps; custom detectors turn poses into punch, kick, jump, headbutt and movement *[shown_working]*
- Noise-tolerant action rules — Thresholds, cooldowns and action priority filter raw tracking; jump counted on landing *[claimed]*
- 4-second calibration — Pre-match step adapts to camera angle, posture and distance *[claimed]*
- Server-side combat — FastAPI computes hit detection and damage; actions flow over WebSocket *[claimed]*
- Live opponent video — WebRTC peer video kept separate from game traffic *[claimed]*
- Rooms, arenas, characters — Create or join room, choose one of 2 arenas and 4 models; player face image applied to head *[claimed]*
- Best-of-3 rounds with accounts and leaderboard — Supabase stores users, rooms and results *[claimed]*

**Flow:** Open site and log in → Create or join a room → Pick arena and character → Complete webcam calibration → Fight a best-of-3 match using real punches, kicks, jumps → See result and leaderboard

**Prompt:** Event-run award for the most unique project; given to two projects that best entertain the judges.
**Fit (implied):** Entertainment-first novelty: turning the player's whole body into the controller of a multiplayer fighting game in a plain browser.  *(targeted: Best Razzle Dazzle Hack - Bitcamp)*
**AI:** Pre-built MediaPipe pose estimation in the browser; hand-written rule-based detectors convert landmarks to game actions. No custom model.
**Architecture:** React Three Fiber/Rapier client runs MediaPipe locally, sends actions over WebSocket to a FastAPI server computing combat; WebRTC carries video; Supabase and R2 for data; hosted on Vercel and Railway.
**Novelty:** Full-body motion fighting with no hardware beyond a webcam, plus live peer video, all in-browser.
**Scope:** medium · working: Live demo site, full login-to-result flow and demo video described; no repo link. · polish: 3D arenas, four models, face mapping, measured latency figure.
**Claims:** Total latency about 65 to 70 ms | Pose tracking at about 20 fps | Tracks 33 body points
**Gaps:** no repo linked; video not watched; screenshot count not captured
Sources: https://devpost.com/software/ghostdiedie, https://bitcamp-2026.devpost.com/

---

### GhostKode
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Auth0 AI Agents

**What it is:** A forensic code tool that connects to your GitHub repos, scores each line by how troubled its commit history is, and overlays ghost icons on the worst lines. Clicking one streams a narrated GPT-4o analysis naming authors and quoting commits, then a suggested fix.
**Problem / user:** Developers new to a codebase who cannot tell why code is fragile because the reasons live in git history.

**Features**
- Git blame and commit forensics — GitHub GraphQL for line blame plus REST commit history. *[shown_working]*
- Semantic haunt scoring — Commit messages embedded with OpenAI and compared to a corpus of bad-commit patterns, weighted with keywords and churn. *[claimed]*
- AST-aware filtering — Excludes comments, docstrings and blank lines from candidates. *[claimed]*
- Ghost overlay — Icons glow brighter on more unstable lines after Summon Ghosts. *[shown_working]*
- Streaming forensic briefing — GPT-4o streams analysis over SSE, followed by an automatic fix suggestion. *[claimed]*
- Follow-up chat — Conversation context persists per ghost. *[claimed]*
- Auth0 GitHub login — Agent acts with the user's GitHub token via a Post Login Action. *[shown_working]*

**Flow:** Log in with GitHub through Auth0 → Pick repo and file → Click Summon Ghosts → Click a ghost → Read streamed analysis and fix → Ask follow-ups

**Prompt:** Most innovative implementation of Auth0 for AI Agents (MLH Best Use of Auth0 AI Agents).
**Fit (implied):** Auth0 passes the user's GitHub token into the session so the AI agent reads private repos with the user's permissions.  *(targeted: [MLH] Best Use of Auth0 AI Agents)*
**Sponsor tools:** Auth0 (GitHub OAuth login and token passed to the agent, core)
**AI:** OpenAI text-embedding-3-small scores commits by cosine similarity to a bad-pattern corpus; GPT-4o narrates and suggests fixes, streamed via SSE.
**Architecture:** Next.js 16 app with Auth0; /api/haunt runs blame, commits and embeddings in parallel; /api/ask streams GPT-4o responses.
**Novelty:** Turns git blame into a themed, semantic instability score and narrated forensics rather than a plain blame view.
**Scope:** small · working: Repo ~29 files, ~2k LOC with documented algorithm; no demo or video. · polish: Thorough README; three screenshots.
**Claims:** Under 300 ms from click to first streamed token
**Gaps:** no video or live demo
Sources: https://devpost.com/software/ghostkode, evidence/bitcamp-bitcamp-2026-ghostkode.json (README), https://bitcamp-2026.devpost.com/

---

### Helix
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Most Philanthropic Hack - Bloomberg

**What it is:** Devpost presents a cancer drug-candidate screener: per-target ML models narrow about 14,000 ChEMBL compounds to 10, then a VQE quantum-chemistry step scores them. The repo README instead describes a quantum drug-safety toolkit for polypharmacy.
**Problem / user:** Researchers choosing a cancer protein target who want better early screening, since most drugs fail trials. README version targets patients, clinicians and researchers checking drug-regimen safety.

**Features**
- Target selection and ML screening — Per-target fingerprint models trained on ChEMBL bioactivity rank ~14,000 compounds down to 10 *[claimed]*
- VQE scoring of top 10 — Qiskit variational quantum eigensolver estimates molecular stability; custom preprocessing fixes odd electron counts *[claimed]*
- Quantum docking report, compound visualization, AI insights — Result pages shown in screenshots *[claimed]*
- Drug interaction simulator — Report plus 3D interaction visualization *[claimed]*
- Graceful fallbacks — Similarity screening if model missing; frontend uses cached data if backend offline *[claimed]*
- README: quantum kernel interaction prediction — PennyLane 4-qubit kernel SVM over fingerprints via /predict_interaction *[shown_working]*
- README: QAOA regimen optimizer — Qiskit QAOA on a 6-variable QUBO honoring condition coverage and cost *[shown_working]*
- README: three front-ends — Next.js patient scan and clinician views, Streamlit researcher workbench *[shown_working]*

**Flow:** Pick cancer type and protein target → ML narrows compounds to 10 → VQE runs on candidates → Review docking report and visuals → Open AI insights and interaction simulator

**Prompt:** Bloomberg prize for the project using technology for meaningful social impact (healthcare, education, sustainability, accessibility); judged on problem choice, real-world relevance, scalability.
**Fit (implied):** Applies ML and quantum chemistry to cancer drug discovery, a healthcare impact problem.  *(targeted: Most Philanthropic Hack - Bloomberg)*
**AI:** Per-target fingerprint ML scorers trained on ChEMBL data; quantum kernel SVM, QAOA and VQE on local simulators; README says VQE energies are cached and no IBM hardware is used.
**Architecture:** Data/training layer pulls ChEMBL, FastAPI backend with PennyLane/Qiskit, Next.js and Streamlit front-ends, cached VQE and JSON reference data.
**Novelty:** Combines classical ML screening with several quantum algorithms in one pipeline; README openly separates live-run from cached quantum steps.
**Scope:** large · working: Backend, three front-ends, tests and CI present; video linked; quantum parts simulated. · polish: Contract doc, pitch folder, critique doc and multiple UIs; README states limits candidly.
**Claims:** Narrows about 14,000 compounds to 10 | Trained on thousands of real lab experiments | IBM hardware integration built but not enabled
**Gaps:** Devpost (cancer screening) and README (polypharmacy safety) describe different scopes; feature list merges both and marks origin; no live demo
Sources: https://devpost.com/software/helix-yp73wi, evidence/bitcamp-bitcamp-2026-helix.json (README), https://bitcamp-2026.devpost.com/

---

### HushMap
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best UI/UX Hack - Bitcamp

**What it is:** Live campus map of study-space noise built from M5GO microphone nodes, with a spoken TerpAI assistant that answers questions from sensor history and YOLOv8 webcam occupancy estimates.
**Problem / user:** Students, especially neurodivergent ones, who cannot tell which study spots are quiet or free before walking there.

**Features**
- Live noise map and heatmaps — M5GO nodes POST decibel averages every few seconds; backend fans out via WebSocket to the map *[shown_working]*
- Historical views — 24-hour playback and per-location charts from MongoDB readings *[claimed]*
- TerpAI voice assistant — Browser audio over WebSocket to faster-whisper, LLM with injected dB stats (Gemini fallback), ElevenLabs speech reply *[shown_working]*
- Occupancy estimation — YOLOv8 endpoint counts people and free seats in webcam images *[claimed]*
- Hardware nodes — MicroPython I2S mic sampling; can audibly remind people to keep quiet *[claimed]*
- PWA with accessibility modes — SvelteKit Svelte 5 app with multiple visual modes *[claimed]*
- Push notifications — Alerts when a favorite spot gets quiet *[planned]*

**Flow:** Open map and see current noise → Check playback or location charts → Ask the voice assistant where is quiet → Hear a spoken answer from live data

**Prompt:** Event-run award for best overall UX/UI design among weekend hacks, judged on innovation, aesthetics, service to the project and process.
**Fit (implied):** Polished map interface with themes, accessibility modes and a voice interface on top of real hardware data.  *(targeted: Best UI/UX Hack - Bitcamp)*
**Sponsor tools:** TerpAI (LLM behind the voice assistant, with Gemini fallback, core); ElevenLabs (text-to-speech for assistant replies, supporting); Auth0 (auth SPA SDK in frontend dependencies, unclear)
**AI:** faster-whisper transcribes speech, TerpAI (Gemini 2.5 Flash fallback) answers with noise stats injected as context, ElevenLabs speaks; YOLOv8 counts people.
**Architecture:** M5GO nodes POST to FastAPI, stored in MongoDB (or simulated), pushed by WebSocket to a SvelteKit PWA; separate voice socket and vision endpoint; Docker compose.
**Novelty:** Real custom IoT microphones feeding a map plus voice assistant; unusual hardware-to-UI scope for a campus app.
**Scope:** medium · working: Live demo domain, video, Docker compose, working backend endpoints described. · polish: Themed Svelte PWA, charts, voice modal; no tests.
**Claims:** End-to-end IoT pipeline built in under 36 hours
**Gaps:** camera node on ESP32-S3 failed, occupancy via webcam instead
Sources: https://devpost.com/software/hushmap-193nia, evidence/bitcamp-bitcamp-2026-hushmap.json (README), https://bitcamp-2026.devpost.com/

---

### Jib Camp
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Friendship Hack - Alumni Prize

**What it is:** Shared real-time pixel-art camp where each attendee designs a small creature (a Jib) that wanders, fishes, picnics and befriends others, logging each activity as a polaroid.
**Problem / user:** Bitcamp attendees wanting a playful shared artifact; the page states no problem beyond a Tamagotchi-like idea for everyone.

**Features**
- Jib creator — Mix bodies, faces, hats and accessories from layered PNG sprites *[shown_working]*
- Autonomous behavior — Server timer pairs Jibs randomly and generates activities such as campfire, fishing, picnic *[claimed]*
- Polaroid activity capture and live feed — Each event becomes a polaroid and a feed entry *[claimed]*
- Best-friend tracking — Counts time Jibs spend together *[claimed]*
- Profiles and PNG export — Click a Jib for history; canvas exports sprite *[claimed]*
- Real-time shared world — Socket.io broadcasts new Jibs and events; pan around camp *[claimed]*

**Flow:** Design a Jib → Drop it into the world → Watch feed and polaroids → Click Jibs to see profiles and best friends → Export sprite as PNG

**Prompt:** Alumni prize celebrating connections that make Bitcamp special; teams submit a small digital artifact plus a reflection on how they bonded.
**Fit (explicit):** A shared world of attendee-made creatures whose friendships emerge from time together; artifact and video reflection links attached.  *(targeted: Best Friendship Hack - Alumni Prize)*
**AI:** none
**Architecture:** React/Vite canvas front-end with Windows 95 styling; Express and Socket.io on Railway generating activity events; Supabase for DB and image storage.
**Novelty:** Playful social toy with original art and hand-built retro UI rather than a utility; Figma MCP used for design context.
**Scope:** small · working: Deployed live site and project video; described as finished full-stack app. · polish: Handmade sprites and Windows 95 UI; post-deploy CORS and socket fixes.
**Claims:** First hackathon for the team and a deployed full-stack app
**Gaps:** no repo linked
Sources: https://devpost.com/software/jib-camp, https://bitcamp-2026.devpost.com/

---

### Lasagna
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Moonshot Hack - Bitcamp

**What it is:** Drag-and-drop web editor for assembling hybrid classical (PyTorch) and quantum (PennyLane) neural networks, validating them, exporting runnable code and training them from the browser.
**Problem / user:** Students and researchers who want to prototype ML and quantum ML models without deep coding knowledge of PyTorch and PennyLane.

**Features**
- Visual layer canvas — Drag classical and quantum layers from a library, connect sequentially, edit parameters (React Flow) *[shown_working]*
- Live type and shape validation — Checks adjacent layer dimensions; quantum segments must end in a measurement node *[shown_working]*
- Code export — Transpiler maps layers to torch.nn and PennyLane qnodes wrapped in TorchLayer *[shown_working]*
- JSON model save — Error-free graph stored as LasagnaModel schema *[shown_working]*
- In-app training and inference — /train and /inference endpoints run background training loops with adjustable hyperparameters *[claimed]*
- LLM Copilot and Debug Copilot — Gemini-based helpers seen in screenshots *[unclear]*
- Branching architectures and live loss dashboard — Residual/U-Net graphs, dashboards, JAX and cloud quantum export *[planned]*

**Flow:** Open editor → Drag layers and connect them → Fix validation errors → Export code or save JSON → Train and run inference

**Prompt:** Event-run award for the most creative, innovative and well-developed hack that shoots for the moon.
**Fit (implied):** Ambitious developer tooling that makes quantum machine learning accessible visually.  *(targeted: Best Moonshot Hack - Bitcamp)*
**AI:** Gemini listed for LLM and debug copilots; core is a deterministic graph-to-code transpiler for PyTorch and PennyLane.
**Architecture:** React/Vite and React Flow front-end emits LasagnaModel JSON; FastAPI backend transpiles to Python files, trains in background threads and serves inference.
**Novelty:** Visual builder that mixes classical and quantum layers with a transpiler, uncommon even among ML no-code tools.
**Scope:** medium · working: Repo with frontend, backend, transpiler and saved models; demo video linked. · polish: Setup docs and user guide in README; no tests or live deployment.
**Claims:** Transpiler guarantees quantum segments end with measurement nodes
**Gaps:** Copilot integration details not documented
Sources: https://devpost.com/software/lasagna-hongpv, evidence/bitcamp-bitcamp-2026-lasagna.json (README), https://bitcamp-2026.devpost.com/

---

### Methods for Computing the ANNNI Model Phase Diagram
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence low*
**Prizes:** Best Scientific Quantum Track Hack

**What it is:** Quantum-physics theory submission computing the phase diagram of the ANNNI spin model with exact diagonalization, VQE and Trotterized time evolution, with an external Overleaf paper as the main writeup.
**Problem / user:** Physics-track entrants mapping ANNNI phases (and their noise robustness); the page names no end user.

**Features**
- Exact diagonalization — Optimized code raises classically solvable size from 8 to 12 spins *[claimed]*
- VQE phase mapping — Variational eigensolver approach for phase diagram, up to 20 qubits per summary *[claimed]*
- Trotterized time evolution — Dynamics-based method for phase signatures *[claimed]*
- Written analysis — Paper-style writeup hosted on Overleaf *[unclear]*

**Flow:** No demo or user flow; judges read the notebook/paper and presentation

**Prompt:** Quantum track prize for hacks using quantum algorithms to solve a physics problem. The track handout (in the repo) asks to map the 1D ANNNI phase diagram with PennyLane and study depolarizing-noise effects, scored on accuracy, noise analysis, insight, sophistication, presentation.
**Fit (implied):** Directly addresses the ANNNI phase-diagram task using three methods at larger sizes; page does not state how noise was handled.  *(targeted: Best Scientific Quantum Track Hack)*
**AI:** none
**Architecture:** Python notebooks/scripts running diagonalization, VQE and Trotter simulations; results written up externally.
**Novelty:** Compares multiple methods on one model and pushes system size beyond the handout's baseline, a stated bonus item.
**Scope:** small · working: Repo holds the track starter kit and handout; own code not visible in evidence summary; no video. · polish: Page is terse; details live in the linked paper.
**Claims:** Supports up to 20 qubits | Classical solvable size raised from 8 to 12 spins
**Gaps:** Overleaf paper not read; repo README is the organizer handout so project results unknown; noise analysis unconfirmed
Sources: https://devpost.com/software/methods-of-computing-the-annni-model-phase-diagram, evidence/bitcamp-bitcamp-2026-methods-for-computing-the-annni-model-phase-diagram.json (README), https://bitcamp-2026.devpost.com/

---

### MindMirror
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Advanced Data Science Track Hack - Bitcamp

**What it is:** Web app that ingests exported AI chat histories, has an LLM build a cognitive profile (fingerprint, dependencies, uncomfortable questions, archetype), and maps topics to predicted brain activation with Meta's TRIBE v2.
**Problem / user:** Heavy chatbot users curious what their usage reveals about their thinking habits and skills outsourced to AI.

**Features**
- Export parsing — Auto-detects Claude, ChatGPT (and in README Gemini) export formats and normalizes conversations *[shown_working]*
- Cognitive fingerprint — Six 0-100 scores such as systems thinking and uncertainty tolerance, shown as radar chart *[shown_working]*
- Topic graph and dependency audit — Bubble map of topics; outsourced skills rated habit, dependency or atrophy *[shown_working]*
- Uncomfortable questions, knowledge edge, archetype — LLM generates 5-7 second-person questions, unusual interests and a short label *[shown_working]*
- Neural Mirror — Text-only TRIBE v2 service predicts cortical activation per topic; atlas ROI mapping drives a 3D brain heatmap *[claimed]*
- Shareable PNG card — Archetype card exported as image *[claimed]*
- Longitudinal tracking, team profiles — Monthly deltas and aggregate team views *[planned]*

**Flow:** Upload export JSON → Wait on processing screen → Read dashboard sections → Hover topics to light up brain/neural visual → Download share card

**Prompt:** Track prize listed without description beyond its name (advanced data science track).
**Fit (implied):** Combines LLM-based text analysis with a recent brain-encoding foundation model and atlas-based statistics.  *(targeted: Best Advanced Data Science Track Hack - Bitcamp)*
**AI:** LLM returns schema-constrained JSON analysis (Devpost says Gemini 1.5 Pro; README says Claude Sonnet via API streaming); separate TRIBE v2 PyTorch service predicts cortical activity from text, mapped with the Destrieux atlas.
**Architecture:** Next.js client parses exports, calls analysis API (LLM), results kept in sessionStorage; Python brain-service microservice runs TRIBE v2; Three.js renders cortex, D3 and Recharts for other charts.
**Novelty:** Early use of a newly released brain-activity prediction model in a consumer-style app, paired with a privacy-first in-browser parsing story.
**Scope:** medium · working: Repo with parsers, API routes, brain-service and CI; demo video; page says deployed but gives no URL. · polish: Dark themed dashboard, 3D visuals, share card; no tests.
**Claims:** Built end-to-end in under 10 hours | Among first consumer apps using TRIBE v2 | No faked demo data
**Gaps:** Devpost names Gemini 1.5 Pro as analyzer while README uses Claude API; feature list follows Devpost with README additions; brain service not confirmed in README excerpt; live URL not given
Sources: https://devpost.com/software/mindmirror-2aizuh, evidence/bitcamp-bitcamp-2026-mindmirror.json (README), https://bitcamp-2026.devpost.com/

---

### Nara - Autonomous Red Teaming Agent
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Champion of Open Source w/ Featherless - Featherless; Neelbauer Agentic Revolution Award (NARA) - Alumni Prize

**What it is:** Command-line platform where several AI agents scan a codebase with static analyzers, plan a MITRE ATT&CK-style chain, run it against a disposable Docker target with a viewable desktop, then get defensive advice. It is a security-training and demonstration tool.
**Problem / user:** Developers and security teams who get vulnerability lists but no proof of real-world impact; also learners studying red and blue team work.

**Features**
- Scanner agent — Runs Semgrep and Bandit on a local path or GitHub URL; LLM dedupes and ranks by exploitability *[shown_working]*
- Planner agent — Builds ordered kill chain mapped to ATT&CK tactics from the findings *[shown_working]*
- Exploiter agent — Runs steps inside a throwaway container, LLM assesses each result and retries or aborts *[shown_working]*
- Live observability — noVNC desktop and log window show the simulated impact in the container *[shown_working]*
- Blue Team Advisor — Streams remediation and detection advice from UMD's TerpAI *[claimed]*
- Interactive CLI — Intent router handles pipeline, scan, plan, exploit, report and natural-language questions *[shown_working]*
- Swappable LLM backends — Featherless (Phi-4-mini default), Claude API or local Ollama via .env *[shown_working]*
- PDF reports, CI integration, authenticated scans — Planned extensions *[planned]*

**Flow:** Start the nara CLI → Run pipeline on a vulnerable demo repo → See ranked findings and kill chain → Watch exploitation in the sandbox desktop → Read blue-team advice → Reset sandbox

**Prompt:** Featherless prize recognizes open-source contributors and builders. NARA (alumni) honors best use of trained, prompted AI agents, including agents that autonomously red-team other software or agents.
**Fit (explicit):** Multi-agent autonomous red-team pipeline (NARA prize) running on open models hosted by Featherless or local Ollama.  *(targeted: Best Champion of Open Source w/ Featherless - Featherless, Neelbauer Agentic Revolution Award (NARA) - Alumni Prize)*
**Sponsor tools:** Featherless AI (Phi-4-mini) (default LLM backend for scanner, planner and exploiter reasoning, core); TerpAI (blue team advice, accessed through its web streaming interface, supporting)
**AI:** Prompted LLM agents (Phi-4-mini, Claude or Ollama qwen2.5) rank findings, write plans and judge step outcomes, with a hardcoded fallback chain and tolerant JSON parser for weak models.
**Architecture:** Python CLI orchestrator with four agent modules sharing one session dict; host does scan/plan/LLM, Docker Ubuntu+XFCE+noVNC container is the target; TerpAI called over streaming HTTP.
**Novelty:** Pairs autonomous attack-chain reasoning with a visible sandbox desktop and a defensive feedback loop; offline mode via Ollama. Safeguard: runs only in a disposable local container; page says authorization and scope were considered.
**Scope:** medium · working: Repo with CLI, Docker image and demo transcript; README links a demo video (Devpost lists none). · polish: ASCII-art CLI, docs, setup steps; no tests.
**Claims:** Built in 36 hours by four people | Runs free with local Ollama and no API keys | Found and reported a stored XSS in TerpAI
**Gaps:** README says three agents, Devpost says four (blue team advisor); feature list follows Devpost; video only linked in README
Sources: https://devpost.com/software/nara-autonomous-red-teaming-agent, evidence/bitcamp-bitcamp-2026-nara-autonomous-red-teaming-agent.json (README), https://bitcamp-2026.devpost.com/

---

### Proof of Code
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Davis Prize for Human Ingenuity in Computing - Alumni Prize

**What it is:** A VS Code extension plus website that records a student's edits while they work on an assignment, flags suspicious events such as sudden large insertions, and lets an instructor replay the edit history.
**Problem / user:** CS instructors who cannot tell whether AI tools wrote student code, and honest students at risk of false accusations.

**Features**
- Edit recording extension — Captures text-document change events in VS Code in real time *[claimed]*
- Opt-in via .submit file — Only records in projects containing a .submit marker *[claimed]*
- Ingest server — Instructor-hosted Rust server logs streamed edits *[claimed]*
- Anomaly flagging — Flags events like large pastes or sudden additions *[claimed]*
- Replay site — Web viewer replays a student's history in real time (Monaco) *[claimed]*
- Google sign-in — OAuth login; UMD CAS planned *[claimed]*

**Flow:** Install extension from the Marketplace → Work in a project with a .submit file → Edits stream to server → Server flags anomalies → Instructor replays history on the site

**Prompt:** Alumni prize for tools helping hackathon organizers detect whether and how much AI was used in a project; must be open source and freely usable by organizers.
**Fit (implied):** Detects AI-assisted work through edit-history provenance, aimed at courses rather than hackathons.  *(targeted: Davis Prize for Human Ingenuity in Computing - Alumni Prize)*
**AI:** none
**Architecture:** TypeScript VS Code extension streams edit events to a Rust ingest server; web front-end with Monaco replays them; Google OAuth.
**Novelty:** Detects AI use by process evidence (edit timeline) instead of text classifiers; published in the VS Code Marketplace.
**Scope:** small · working: Marketplace extension, demo website and video linked; no repo on page. · polish: Live site and published extension; details of anomaly rules not documented.
**Claims:** Says it works and solves a real problem
**Gaps:** no repo linked; open-source status unconfirmed; flagging heuristics unspecified
Sources: https://devpost.com/software/proof-of-code, https://bitcamp-2026.devpost.com/

---

### QuantumQuest QCNN
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence B · confidence low*
**Prizes:** Best Scientific Quantum Track Hack

**What it is:** Notebook-style quantum machine-learning project using a quantum convolutional neural network, written in JAX and PennyLane, to classify ANNNI-model Hamiltonian parameters into phases under noise.
**Problem / user:** Quantum-track entrants mapping the ANNNI phase diagram under noise; no end user named.

**Features**
- QCNN phase classifier — Takes Hamiltonian parameters and outputs a phase class *[claimed]*
- Noisy phase diagram — Aims to map the diagram under noise *[unclear]*
- Trotterization and noise reduction — Listed as next steps *[planned]*

**Flow:** No demo; reviewers read the linked write-up and notebooks

**Prompt:** Quantum track prize for hacks using quantum algorithms to solve a physics problem; the track task is mapping the ANNNI phase diagram with PennyLane and analyzing noise.
**Fit (implied):** Page states it uses a QCNN to map the ANNNI diagram under noise, matching the track task.  *(targeted: Best Scientific Quantum Track Hack)*
**AI:** Quantum convolutional neural network trained with JAX/Optax on PennyLane circuits.
**Architecture:** Python Jupyter notebooks with JAX, Optax and PennyLane; results in a linked document.
**Novelty:** Uses a learned QCNN classifier rather than direct simulation for the phase map.
**Scope:** tiny · working: Page gives no results; repo on Codeberg and write-up PDF not read. · polish: Terse, joking page text; 12 uncaptioned screenshots.
**Gaps:** Codeberg repo and Drive write-up not read; no results or metrics on page
Sources: https://devpost.com/software/quantumquest-qcnn, https://bitcamp-2026.devpost.com/

---

### QWave
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Digital Forensics Related Hack - Cipher Tech Solutions

**What it is:** Streamlit tool that checks audio for hidden malicious manipulation by combining classical features with Qiskit noise-channel simulation, labels it clean, natural noise or malicious, and can monitor an email inbox for audio attachments.
**Problem / user:** Security teams and audio-processing systems facing normal-sounding audio carrying adversarial or ultrasonic perturbations.

**Features**
- Audio upload and demo generation — Upload, generate healthy or malicious demo audio, inject chosen attack type *[shown_working]*
- Chunked classical features — RMS, spectral centroid, high-frequency ratio, flatness, phase instability, discontinuity per chunk *[claimed]*
- Quantum fingerprinting — ZZFeatureMap encoding run under ideal, bit-flip, phase-flip and depolarizing noise in Aer, compared by Jensen-Shannon divergence *[claimed]*
- Hybrid classification — Weighted fusion yields label, attack family, confidence and chunk evidence *[shown_working]*
- Rectified audio output — README adds a cleaned audio download tab *[claimed]*
- Inbox monitoring — Gmail IMAP/SMTP scans attachments and sends alerts *[claimed]*
- Arduino LED alert — README: LED alerts when hardware connected *[claimed]*

**Flow:** Upload or generate audio → Optionally inject a demo attack → Run detection and inspect chunk evidence → Download rectified audio → Or let inbox monitor scan attachments

**Prompt:** Cipher Tech prize for projects aiding digital forensics or investigations, such as data recovery, steganography detection or finding objects in image collections.
**Fit (implied):** Forensic-style audio analysis that distinguishes natural noise from adversarial perturbation and files incident-style reports.  *(targeted: Best Digital Forensics Related Hack - Cipher Tech Solutions)*
**AI:** No trained model; hand-built signal features plus quantum circuit simulation, fused by weighted rules.
**Architecture:** Streamlit app: ingest and chunk audio, extract features, encode to Qiskit circuit, simulate under noise channels, compute divergences, classify; Gmail inbox watcher; deployed on Cloud Run.
**Novelty:** Uses quantum-noise simulation as an extra feature for audio attack detection; defensive-only demo with synthetic attacks generated in-app.
**Scope:** medium · working: Demo site, Cloud Run deployment, tests and video; example files labeled correctly per page. · polish: Four-tab UI, charts, rectified output and hardware alert.
**Claims:** Correctly separates BitFlip.wav from naturalHiss.wav | Classifies four attack families plus clean and natural
**Gaps:** no accuracy metrics; Devpost slug is quanterp, name QWave/Q-wave
Sources: https://devpost.com/software/quanterp, evidence/bitcamp-bitcamp-2026-qwave.json (README), https://bitcamp-2026.devpost.com/

---

### Recall
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Most Philanthropic Hack - Bloomberg

**What it is:** iOS app (with a local Flask backend) for people in early dementia: point the phone camera at someone to see who they are, their relationship and what was last discussed, record chats that a local LLM summarizes, and practice recall with a memory game.
**Problem / user:** Early-stage dementia patients who struggle to recognize important people, and caregivers who manage the enrolled contacts.

**Features**
- Face enrollment by caregivers — Caregiver adds family and friends with photos, names and relationships; InsightFace ArcFace embeddings stored *[shown_working]*
- Live face recognition — Camera frame matched by cosine similarity; shows relationship and last conversation, optional voice read-aloud *[shown_working]*
- Conversation recording and summary — iOS speech recognition transcribes on device; Ollama Mistral 7B writes short summary (3-word per README) *[claimed]*
- Face Frenzy memory game — Who-is-this, who-is-name and conversation-recall questions generated from stored data *[claimed]*
- Local-only processing — No paid cloud or external APIs; backend runs on a Mac *[claimed]*
- Smart-glasses version — Hands-free identification *[planned]*

**Flow:** Caregiver enrolls people → Patient points phone camera at a person → App names them and shows last topic → Patient records a conversation to be summarized → Patient plays memory quiz

**Prompt:** Bloomberg prize for the project that best uses technology for meaningful social impact (healthcare, education, sustainability, accessibility), judged on problem choice, relevance and scalability.
**Fit (implied):** Healthcare accessibility aid for early dementia with privacy-preserving local processing.  *(targeted: Most Philanthropic Hack - Bloomberg)*
**AI:** InsightFace ArcFace embeddings with cosine matching for recognition; Mistral 7B via Ollama summarizes conversations and drives quiz questions; iOS Speech for transcription.
**Architecture:** SwiftUI iPhone app talks over local WiFi to a Flask server on a Mac holding face embeddings JSON and photos and calling Ollama.
**Novelty:** Fully local face recognition and LLM pipeline for a sensitive medical use, bridging a phone UI to a laptop backend.
**Scope:** small · working: Repo with backend and SwiftUI app, demo video; requires Mac and iPhone on same network. · polish: Banner screenshots and hand-drawn background; JSON file as database.
**Claims:** No external servers or paid APIs
**Gaps:** Devpost calls recall practice quizzes while README names a Face Frenzy game; both listed; no accuracy numbers
Sources: https://devpost.com/software/recall-1wr8y9, evidence/bitcamp-bitcamp-2026-recall.json (README), https://bitcamp-2026.devpost.com/

---

### Sleeply
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best First Time Hack - Bitcamp

**What it is:** Interactive React web app that simulates a night of sleep from a short profile questionnaire and displays a stage timeline, pulsing 3D brain, brainwave graph and sleep score.
**Problem / user:** Curious general users, with accessibility emphasis, who find brainwaves and sleep hard to picture; creator wanted to explain them visually.

**Features**
- Profile builder — Questionnaire for sleep duration, stress and substances like caffeine or alcohol *[shown_working]*
- Simulated sleep model and timeline — Generates stage timeline from inputs (method not described) *[shown_working]*
- 3D brain visualizer — Three.js brain model with pulses of activity *[shown_working]*
- Brainwave graph — 2D waveform view claimed accurate to real EEG *[claimed]*
- Sleep score and summary — Reveal screen quantifying quality *[shown_working]*
- Interactive tutorials — Explain the 3D brain and brainwaves *[claimed]*
- 18 color themes plus light/dark — Accessibility-driven UI customization *[claimed]*
- EEG upload and community profiles — Upload real data, share profiles *[planned]*

**Flow:** Fill in the profile questionnaire → Receive simulated sleep model → View home screen with timeline, brain and waves → Open tutorials → See sleep score and summary

**Prompt:** Prize for the best hack by a first-time hacker showing the most growth; at least half the team must be first-time Bitcamp hackers.
**Fit (none):** Solo creator's polished visualization project; the page does not mention first-timer status explicitly.  *(targeted: Best First Time Hack - Bitcamp)*
**AI:** none
**Architecture:** Single-page React/Vite app with React Three Fiber rendering a credited third-party brain model; simulation runs client-side; hosted on Vercel.
**Novelty:** Educational neuroscience visualization with a credited 3D brain and unusual theming/accessibility depth for a solo build.
**Scope:** small · working: Live Vercel demo and video; about 7 testers per page; no repo. · polish: 18 themes, tutorials and single-screen windowed layout.
**Claims:** Brainwaves accurate to true EEG readings (unvalidated) | About 7 people tested it
**Gaps:** no repo; simulation method undocumented
Sources: https://devpost.com/software/sleeply, https://bitcamp-2026.devpost.com/

---

### Still Here
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Use of Netcore - Netcore

**What it is:** Installable PWA for people living alone: a one-tap daily check-in, and if missed, escalation through push, email, SMS to emergency contacts and finally a request for a non-emergency wellness check.
**Problem / user:** Young adults in a first apartment who live alone; existing alert products feel clinical, subscription-based and aimed at older adults.

**Features**
- Daily one-tap check-in — User taps Still Here at a configured time; scheduler polls every minute in UTC *[claimed]*
- Escalation chain — Push and email with check-in link, then SMS to contacts, then wellness-check call request *[claimed]*
- Configurable grace period — E.g. 10 days for a camping trip before escalation *[claimed]*
- One-time signed confirm links — Contacts confirm via token link instead of reply SMS *[claimed]*
- Auth options — JWT, optional Auth0 Google login (live), API keys for IoT *[claimed]*
- PWA with no app store — Vanilla JS, Docker Compose on a VPS behind Caddy *[claimed]*
- Duplicate-fire guard — checkin_fires table prevents repeated triggers *[claimed]*
- AI voice wellness agent — Possible future direction *[planned]*

**Flow:** Sign up and set check-in time, grace period and contacts → Tap Still Here each day → On a miss, get push/email → After grace, contacts get SMS → Chain can request local non-emergency wellness check

**Prompt:** Netcore prize, broad in scope, requires connecting at least two devices using Netcore's SDK.
**Fit (none):** Multi-channel notification escalation across devices and contacts; the page does not name a Netcore SDK or product.  *(targeted: Best Use of Netcore - Netcore)*
**AI:** none
**Architecture:** FastAPI with Celery Beat and Redis timers, Supabase Postgres via raw SQL, Resend email, FCM push, AWS SNS SMS and Twilio voice, vanilla JS PWA.
**Novelty:** Pragmatic safety design that avoids 911 integration limits by calling non-emergency lines; rebuilt SMS confirmation after a vendor rejection.
**Scope:** medium · working: Live site, demo page and video; Auth0 Google login stated live. Repo README unreadable. · polish: Custom domain, Dockerized deployment, documented provider pivots.
**Claims:** Scheduler scales fine until tens of thousands of users (untested) | Cites 36 million Americans living alone
**Gaps:** repo clone failed and raw README returned 404; SMS provider inconsistent on page (Twilio vs AWS SNS); Netcore usage not stated
Sources: https://devpost.com/software/still-here, https://bitcamp-2026.devpost.com/

---

### TeleGrid
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Real World Prize - Ambrook

**What it is:** Low-cost acoustic sensor node (ESP32 plus MEMS microphone) that listens for corona discharge on power lines, extracts FFT features, classifies with a random forest and streams alerts to a live web dashboard. Repo is named VoltVigil; Devpost slug is linewatch.
**Problem / user:** Utilities that find line faults late through slow, costly periodic inspections; faults can cause outages or wildfires.

**Features**
- Acoustic corona detection — INMP441 microphone sampled by ESP32; 14 FFT band averages plus peak frequency *[shown_working]*
- Random forest classification — Scikit-learn model trained on a self-built labeled set; README runs it in a Flask service *[claimed]*
- Immediate threshold severity — Backend scores severity on arrival before ML result *[claimed]*
- Live dashboard — React map, sensor list and notification log updated by Socket.io *[shown_working]*
- Email alerts — Nodemailer notifies subscribers on high/critical with per-node cooldown (README) *[claimed]*
- 3D-printable housing — STL enclosure for the sensor node *[claimed]*
- Pole-mountable multi-sensor unit with on-device AI — Future work *[planned]*

**Flow:** Sensor listens near a power line → Features POSTed over WiFi → Backend stores and broadcasts alert → ML result updates it → Dashboard map shows alert and email may go out

**Prompt:** Ambrook prize for creative projects with a real-world component, such as moving something physical or using natural resources.
**Fit (implied):** Physical sensor hardware deployed at infrastructure, with a real-time monitoring pipeline.  *(targeted: Real World Prize - Ambrook)*
**AI:** Random forest / gradient boosting on FFT features from audio, trained on a small team-made dataset with noise conditions.
**Architecture:** ESP32 posts to Express/Socket.io/MongoDB backend, which asynchronously calls a Flask ML service and pushes updates to a React/Vite dashboard; email via Nodemailer.
**Novelty:** Passive audio-based line monitoring on a cheap microcontroller, with custom dataset and printed enclosure.
**Scope:** medium · working: Demo video and screenshots; repo has firmware, backend, ML service, dashboard and STL files. · polish: Component READMEs and enclosure; no tests or live deployment.
**Claims:** Working prototype streaming live predictions to dashboard
**Gaps:** Devpost implies classification on ESP32 while README classifies in backend ML service; feature list follows README for data flow; no accuracy metrics
Sources: https://devpost.com/software/linewatch, evidence/bitcamp-bitcamp-2026-telegrid.json (README), https://bitcamp-2026.devpost.com/

---

### TerpWallet AI
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** TerpAI Ultimate Agent Showdown - Cloudforce/Microsoft

**What it is:** Next.js dashboard that reads a student's bank data through Capital One's Nessie sandbox, detects financial distress with a rule engine, and recommends specific free UMD resources, backed by a custom TerpAI agent restricted to a 36-item campus knowledge base.
**Problem / user:** UMD students who overspend on things the campus already provides free (pantry, meals, emergency funds) because they learn of them too late.

**Features**
- Bank connection — Capital One Nessie API transactions, with mock snapshot fallback and seed script *[shown_working]*
- Distress detection — Deterministic rules on spending velocity, balance runway and food spend concentration *[shown_working]*
- Proactive alert card — Slide-in message recommending 1-2 matched free resources *[shown_working]*
- Campus resource knowledge base — 36 researched UMD resources with hours, location, cost and savings *[shown_working]*
- TerpAI Safety Agent — Custom agent answering only from the knowledge base in under 120 words, linked from dashboard *[claimed]*
- Details view and map — Show me details with location map *[claimed]*
- Auth0 login, dark mode — Session verified server-side *[shown_working]*

**Flow:** Log in with Auth0 → Dashboard shows balance, runway and transactions → Rule engine flags distress → Alert card suggests resources → Open details/map or consult TerpAI agent

**Prompt:** Cloudforce/Microsoft challenge: build a tool solving real campus problems, including at least one TerpAI agent, pitched shark-tank style.
**Fit (explicit):** Builds a custom TerpAI agent grounded in UMD resources and integrates it into a student-facing finance safety net.  *(targeted: TerpAI Ultimate Agent Showdown - Cloudforce/Microsoft)*
**Sponsor tools:** TerpAI (Cloudforce/Microsoft Azure) (custom Safety Agent with campus knowledge source, core); Capital One Nessie API (bank accounts and transactions, core); Auth0 (login and session, supporting)
**AI:** Distress detection is rule-based by design; the TerpAI agent (page says GPT-5.2 on Azure) answers from a curated JSON knowledge source with no vector DB or RAG framework.
**Architecture:** Next.js 14 app with Auth0, lib/nessie client and lib/distress engine reading campus_resources.json; alerts render in UI and link to external TerpAI agent; Vercel hosting.
**Novelty:** Frames finance help as routing to institutional resources instead of budgeting, built around a platform agent with strict scope.
**Scope:** small · working: Repo, video and screenshots; Nessie was unreachable at venue so mock mode used for demo; page says solo build in under 24 hours. · polish: Light/dark modes, animations, README screenshots; no tests.
**Claims:** 36 hand-researched resources | Agent replies under 120 words | 90-second demo
**Gaps:** agent URL not on page
Sources: https://devpost.com/software/terpwallet-ai, evidence/bitcamp-bitcamp-2026-terpwallet-ai.json (README), https://bitcamp-2026.devpost.com/

---

### Terrametric
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Real World Prize - Ambrook; Best Champion of Open Source w/ Featherless - Featherless; Best Intermediate Data Science Track Hack - Bitcamp

**What it is:** Farm monitoring console that scores crop stress per field from satellite signals, estimates dollar loss, forecasts yield for 14 days, prescribes irrigation, and offers a Qwen-based agronomy copilot, shown on a 3D globe of the portfolio.
**Problem / user:** Farmers and agronomists (later crop insurers) who act too late because satellite stress signals do not reach them in decision-ready form.

**Features**
- Field stress scores — XGBoost turns NDVI, NDWI, SWIR, NASA SMAP soil moisture and rainfall deficit into a 0-1 score *[claimed]*
- Dollar-loss estimates — Second model converts stress using field size and crop type; portfolio loss counter *[claimed]*
- 3D globe portfolio view — GLSL globe colors fields green, amber or red *[shown_working]*
- 14-day yield forecast — Forecast per field *[claimed]*
- Irrigation prescriptions — How many inches, by when, cost and loss prevented *[claimed]*
- AI copilot — Qwen 2.5 with 11 agronomic tools over live data and indexed USDA extension reports *[claimed]*
- Optical plus radar fusion — SMAP radar covers cloud cover gaps *[claimed]*

**Flow:** Open console → Globe scans portfolio and fields change color → Open a field to see prescription → Ask copilot plain-English questions

**Prompt:** Ambrook: creative project with a real-world component (physical or natural resources). Featherless: highlight open-source builders. Intermediate data science track listed with no description.
**Fit (implied):** Agricultural decision tool built on open satellite data and open Qwen model, with trained ML models.  *(targeted: Real World Prize - Ambrook, Best Champion of Open Source w/ Featherless - Featherless, Best Intermediate Data Science Track Hack - Bitcamp)*
**Sponsor tools:** Qwen 2.5 (open model; Featherless named only in queue) (agronomy copilot, unclear)
**AI:** XGBoost for stress and loss, Qwen 2.5 tool-using copilot grounded in live field data and USDA reports.
**Architecture:** FastAPI/SQLite backend serving model outputs from satellite-derived signals; Next.js/React frontend with GLSL globe on Vercel; Story County, Iowa as pilot region.
**Novelty:** Leads with a decision and dollar figure rather than raw indices, and fuses radar with optical data.
**Scope:** medium · working: Live Vercel demo and video; no repo; Story County only. · polish: Custom globe shader and six rewrites of prescription screen.
**Claims:** Five satellite signals fused | 11 copilot tools | Detects stress weeks earlier than visible symptoms
**Gaps:** no repo; no model accuracy; Featherless not named on page
Sources: https://devpost.com/software/terrametric, https://bitcamp-2026.devpost.com/

---

### Thats My Echo
*Bitcamp Bitcamp 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Domain Name from GoDaddy Registry

**What it is:** A Unity 2D platformer where you play a breath of wind and drop echoes that replay your exact earlier movements. A dormant enemy called the Listener wakes and hunts any echo, so your past self becomes both a tool and a lure.
**Problem / user:** Platformer players; creators wanted failures and past actions to persist and matter instead of resetting.

**Features**
- Echo record and replay — Records player movement and replays it in real time as a persistent object that can interact with the world. *[shown_working]*
- The Listener enemy — Stays dormant until an echo exists, then hunts it. *[shown_working]*
- Custom character controller — Breath character with wall jumping and collision handling. *[shown_working]*
- Level goal — Reach the Ancient Ones; ending cutscene planned. *[planned]*

**Flow:** Move as the breath through a mountain level → Place an echo → Listener wakes and chases the echo → Navigate around it using the replay → Reach the Ancient Ones

**Prompt:** Register a domain name with GoDaddy Registry (MLH Best Domain Name from GoDaddy Registry). The Game Jam track theme was "Echo".
**Fit (implied):** Page lists a catecholl.us link under Try it out; the game name matches the Echo jam theme. Domain use is not explained in the text.  *(targeted: [MLH] Best Domain Name from GoDaddy Registry)*
**Sponsor tools:** GoDaddy Registry domain (Custom domain link listed on the project page, token)
**AI:** none
**Architecture:** Unity/C# game with a recording-and-playback system for echoes and a state-triggered enemy AI; itch.io build.
**Novelty:** Echo-replay mechanic tied to a trigger-based enemy; narrative theme built into the mechanic.
**Scope:** small · working: Playable itch.io build, repo with ~290 files (Unity project), four screenshots. · polish: Hand-drawn art via Photoshop/Procreate; no video.
**Gaps:** no video; domain usage not described
Sources: https://devpost.com/software/thatsmyecho, evidence/bitcamp-bitcamp-2026-thats-my-echo.json (README), https://bitcamp-2026.devpost.com/

---

### The Unspillable
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Hardware Hack - Bitcamp

**What it is:** Arduino-based smart spoon that uses an MPU6050 motion sensor and two servos in a two-axis arrangement to keep the bowl level against hand tremors, housed in a 3D-printed handle.
**Problem / user:** People with Parkinson's disease or essential tremor who want to eat comfortably; commercial stabilizing spoons cost over $300.

**Features**
- Two-axis stabilization — MPU6050 reads tilt and two servos counter it to keep the bowl level *[claimed]*
- Low-cost parts — Arduino Nano, servos and sensor instead of costly commercial units *[claimed]*
- Battery-powered handle — 3D-printed SolidWorks-designed case holds electronics, button and battery *[claimed]*
- Smaller rechargeable redesign — Future *[planned]*

**Flow:** Power on with the button → Hold the spoon by the handle → Bowl stays level as the hand tilts or shakes

**Prompt:** Award for the most creative, technical and innovative use of circuitry, electronics or microcontrollers.
**Fit (implied):** Closed-loop sensor-servo hardware prototype for an accessibility problem.  *(targeted: Best Hardware Hack - Bitcamp)*
**AI:** none
**Architecture:** MPU6050 to Arduino Nano (C++) controlling two servos; button and battery inside a printed handle.
**Novelty:** Affordable build of an assistive device normally sold at high cost; hardware-only scope with no software layer.
**Scope:** tiny · working: Page says motor-sensor system worked within 24 hours; no video, demo or repo. · polish: Custom CAD enclosure; no measurements or user testing.
**Claims:** Bowl remains perfectly level at any handle angle (unmeasured) | Commercial equivalents exceed $300
**Gaps:** no repo, video or demo; stabilization algorithm not described
Sources: https://devpost.com/software/the-unspillable, https://bitcamp-2026.devpost.com/

---

### Tseda
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Machine Learning Track Hack - Bitcamp

**What it is:** Next.js web app for early drug discovery. A user describes a reference drug or a disease; Claude proposes novel candidate molecules, a ChemDoodle editor lets them draw or tweak structures, and a fine-tuned MLM-FG model scores side-effect risk.
**Problem / user:** Drug discovery is slow and costly, with much spending in preclinical design; aimed at researchers who want faster candidate generation and early risk screening (page names no specific user).

**Features**
- Candidate generation from a query — Two modes: molecules similar to a named drug ('like') or for a disease hypothesis ('for'); Claude returns SMILES, rationale, confidence and computed properties via /api/generate. *[shown_working]*
- Candidate list and detail pages — Generated compounds are listed with details, rationale and synthesis information per compound, shown in screenshots. *[shown_working]*
- In-browser molecule editor — ChemDoodle canvas to draw molecules, import MOL files and edit generated candidates. *[shown_working]*
- Gemini-assisted drafting / Magic Edit — Gemini drafts or edits a compound from a text prompt inside the editor. *[shown_working]*
- Side-effect risk prediction — MLM-FG (fine-tuned on the SIDER dataset) scores a structure on side-effect categories via /api/predict, shown as indicators. *[claimed]*
- IUPAC naming — STOUT Python package names molecules, called from the server with a timeout. *[claimed]*
- Mock inference mode — Backend can run in a mock mode without GPU or trained weights; README says trained checkpoint is not in the repo. *[shown_working]*

**Flow:** Open landing page and enter a drug name or disease → Choose 'like' or 'for' mode and generate candidates → Browse the candidate list and open a candidate's details → Open the editor to redraw or Gemini-edit the molecule → Run prediction to see risk indicators per side-effect category

**Prompt:** Best Machine Learning Track Hack at Bitcamp 2026; no criteria text found on the prize listing.
**Fit (implied):** Fine-tunes and serves a pretrained molecular model (MLM-FG on SIDER) for risk scoring, after dropping ChemBERTa, and pairs it with LLM generation. Page says it won the ML track.  *(targeted: Best Machine Learning Track Hack - Bitcamp)*
**AI:** Claude (Haiku) generates molecules as structured JSON; Gemini 3 Flash drafts/edits in the editor; MLM-FG (fine-tuned via Claude Code-driven training) predicts side-effect scores; STOUT names compounds.
**Architecture:** Next.js/React frontend with API routes calling Claude and a Python bridge to the MLM-FG SIDER inference script; separate FastAPI backend and frontend inside mlm-fg-sider-app; ChemDoodle for structure editing.
**Novelty:** Chains LLM molecule generation with a domain-specific fine-tuned chemistry model and a structure editor, unusual scope for a hackathon; team says most members were new to ML.
**Scope:** large · working: Demo video and screenshots of generation, editor and indicators; ~20k LOC, 475 files, tests present; README admits trained weights not shipped. · polish: Multiple UI iterations designed with Google Stitch; page notes generation is slow and accuracy limited by compute.
**Claims:** No quantitative accuracy reported | Says inference accuracy was limited by hackathon compute | Won Best Machine Learning Track Hack
**Gaps:** Video not watched; No model metrics; README shows Claude generation; Devpost mentions Anthropic API too
Sources: https://devpost.com/software/tseda, evidence/bitcamp-bitcamp-2026-tseda.json (LittleWhole/Tseda README), https://github.com/LittleWhole/Tseda

---

### X - Protocol
*Bitcamp Bitcamp 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Bitcamp Unwrapped - Bitcamp

**What it is:** A proximity-art installation: it passively scans nearby Bluetooth devices, draws them as orbiting nodes around a central 'X' on a live star map, has an LLM write short invitation letters per device, and lets visitors answer through a QR-code chat portal.
**Problem / user:** People sharing a physical space are invisible to each other; aimed at strangers in crowded places such as a lecture hall who might meet nearby people.

**Features**
- Passive BLE scanning — Python bleak scans phones, laptops, earbuds and displays and reads RSSI signal strength. *[claimed]*
- Constellation star map — React canvas shows devices as glowing nodes orbiting X, positioned by signal-derived distance. *[shown_working]*
- Proximity zones with smoothing — RSSI dBm values smoothed and classed as next to you, in room or far away. *[claimed]*
- AI invitation letters — GPT-4o-mini writes a short personalized letter per device type and proximity, shown in a modal. *[claimed]*
- QR portal chat — Per-session QR code opens a no-app, no-login chat page; conversation mirrors on the star map. *[claimed]*
- Constellation intelligence — Gemini produces proximity-pattern insights shown in a Footprint panel with session history. *[claimed]*
- Live WebSocket updates — FastAPI streams device state; frames batched at 40 ms flush intervals to avoid React re-renders. *[claimed]*

**Flow:** X scans for nearby Bluetooth devices → Devices appear as orbiting nodes on the star map → A letter is drafted for a nearby device and shown → Visitor scans the QR code and opens the chat portal → Conversation mirrors live on the map; Footprint logs the session

**Prompt:** Bitcamp Unwrapped: best hack that is not centered on being an AI wrapper.
**Fit (implied):** Core experience is BLE sensing and a spatial visualization, with LLMs used only for letters and insights; page does not state which prize it targeted.  *(targeted: Bitcamp Unwrapped - Bitcamp)*
**Sponsor tools:** GoDaddy Registry domain (xprotocol.us hosted via Cloudflare Tunnel, supporting); Gemini API (proximity insights for the Footprint panel, supporting)
**AI:** GPT-4o-mini drafts letters conditioned on device type and proximity; Google Gemini generates 'constellation intelligence' insights and multimodal interpretation of who is nearby.
**Architecture:** Python bleak scanner and FastAPI/asyncio backend pushing device frames over WebSockets to a React+Vite canvas frontend; qrcode generates per-session portals; Cloudflare Tunnel exposes it publicly.
**Novelty:** Turns ambient Bluetooth advertisements into an art/social interface rather than an app feature; physical-proximity sensing is unusual for AI-letter projects.
**Scope:** medium · working: Live site listed at xprotocol.us and YouTube demo embed; no repo linked so code size unknown. · polish: Smoothing layer, frame batching and tunnel routing described as solved challenges.
**Claims:** WebSocket frames flushed every 40 ms | Won Bitcamp Unwrapped
**Gaps:** No repo linked; Video not watched; Privacy or consent safeguards for scanning nearby devices not described
Sources: https://devpost.com/software/x-ai

---

