# UNIHACK — UNIHACK 2026 (17 projects)

### Anchor (Monash)
*UNIHACK UNIHACK 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** THE EU SHARED FUTURE PRIZE (by the European Union)

**What it is:** Anchor is a natural-disaster alert app (bushfire focus) that, instead of a generic broadcast, tells each user why a specific incident threatens their location and suggests evacuation. Built as an Expo/React Native app plus a demo website, running on mock data by default.
**Problem / user:** Residents (initially Australian) who get generic regional warnings with no wind, distance or route context; the app also stresses elderly users and plain-English briefs.

**Features**
- Personalised WHY explanation — GPT-4o-mini generates a plain-language reason the incident matters for the user's GPS position, using the risk engine output. *[claimed]*
- Risk engine — Computes HIGH/MED/LOW per incident from distance, wind and similar factors with tunable thresholds. *[claimed]*
- Live fire and weather data aggregation — Aggregator service merges NASA FIRMS hotspots, OpenWeatherMap and BoM alerts; ships with USE_MOCK_DATA on. *[claimed]*
- Map and incident detail screens — react-native-maps map with markers and an incident screen showing risk badge and AI brief. *[claimed]*
- Push alerts — Expo Notifications registration for alerts. *[claimed]*
- Evacuation plans — Device-specific evacuation guidance in the pitch; real pathfinding routes listed as future work. *[planned]*
- Standalone web demo and animated pitch — index.html, phone-demo.html and a self-playing demo-video.html are included in the repo. *[shown_working]*

**Flow:** Open the app and see incidents on a map → Open an incident → See a risk badge for the user's location → Read the AI brief on why it affects them → Receive push alert and evacuation suggestion

**Prompt:** not public / not found
**Fit (implied):** Public-safety disaster alerts; page and README say the architecture can add EU sources (EFFIS, Copernicus, GDACS) by editing two files, plus planned EU expansion.  *(targeted: THE EU SHARED FUTURE PRIZE (by the European Union))*
**AI:** OpenAI GPT-4o(-mini) turns structured risk-engine output into per-user plain-English explanations; README says briefs could be translated.
**Architecture:** Expo app: aggregator pulls NASA FIRMS and weather APIs, riskEngine scores incidents, aiSummary calls OpenAI, Zustand store feeds map and detail screens.
**Novelty:** Differentiator is explaining personal reasons for risk (same fire yields different messages per person) rather than broadcasting; data-source layer designed for adding regions.
**Scope:** small · working: Runs on mock data; Devpost says mobile demo was dropped for a computer-run demo; live API wiring unverified. · polish: Netlify website, pitch animation, accessibility notes, API key guide; no tests.
**Claims:** Prototype and pitch delivered within 48 hours | README claims WCAG AA compliance (unverified) | Adding a region needs changes to two files
**Gaps:** No official EU Shared Future prize text found; Devpost page says Anchor is called AlertAU for now; Evacuation routes not implemented per page
Sources: https://devpost.com/software/fire-tracker-d9uokc (via Chrome), evidence/unihack-unihack-2026-anchor-monash.json, prompts_cache/unihack-2026.md

---

### Antrum MK 1
*UNIHACK UNIHACK 2026 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** FIRST PLACE [1st]

**What it is:** A pair of leg-strapped handheld devices for cavers and miners that track each other without GPS or cell signal. Motion sensors and a 2.4 GHz radio give a direction indicator to the partner or back to the entrance, and trips upload to a web dashboard afterwards.
**Problem / user:** Cave explorers and miners who can get disoriented, separated or trapped underground with no GPS, signal or visibility.

**Features**
- Paired partner tracking — Two ESP32 units exchange position over RF24 radio in a master-slave packet scheme because the link is half-duplex *[claimed]*
- Directional LED indicator — Shows which way the partner lies from the current position *[claimed]*
- Return-to-entrance mode — Guides user back to where recording began *[claimed]*
- Dead reckoning with ZUPT — IMU motion integrated for position; zero-velocity updates stop drift when stationary *[claimed]*
- Movement gating — Integrates only meaningful steps, rejecting small jitter *[claimed]*
- Shared coordinate frame — Yaw offset alignment lets both devices' positions be compared *[claimed]*
- Custom hardware — ICM20948 IMU, XC4508 radio, custom PCB, LM317 power and SolidWorks-designed 3D-printed PLA casing *[shown_working]*
- Antrum DASH web app — After surfacing, data uploads to cloud and the app plots both users' paths *[shown_working]*

**Flow:** Pair both devices before the trip → Strap one to each leg and enter the cave → Use LED indicator to find partner if separated → Switch mode to navigate back to the entrance → Surface and upload exploration data → View both paths on Antrum DASH

**Prompt:** First Place: the best idea that best meets the judging criteria (UNIHACK 2026, $5,000 cash).
**Fit (none):** General-criteria prize; entry is a full hardware, firmware, cloud and web stack addressing underground safety. No sponsor tie.  *(targeted: First Place (Main Prize))*
**AI:** No ML; Claude Code and ChatGPT Codex used as development tools. Positioning uses classical dead reckoning with zero-velocity updates.
**Architecture:** ESP32 firmware (PlatformIO C/C++) with IMU and RF24 radio; after trip uploads to Hono/TypeScript backend with MongoDB on a Google Cloud VM; Angular dashboard on Vercel.
**Novelty:** Custom PCB and inertial navigation hardware with no infrastructure, built with a 3D-printed enclosure within a weekend.
**Scope:** large · working: Devpost reports an integrated system of firmware, hardware and web app with live dashboard link; no accuracy numbers. · polish: Custom PCB, printed casing, deployed backend and dashboard; no demo video.
**Claims:** Needs no infrastructure in the cave | Underwater Mark 2 with UWB planned
**Gaps:** repo github.com/jenul-ferdinand/unihack2026 not read; no demo video; accuracy not reported
Sources: https://devpost.com/software/antrum-mk-1, https://unihack2026.devpost.com/

---

### BeeSafe (Monash)
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** SOCIAL IMPACT PRIZE, 4th

**What it is:** BeeSafe is a web-native driving-safety app that runs on a phone browser: it watches the driver's face for drowsiness, detects road hazards, detects crashes from motion sensors and places an emergency call, and hashes dashcam footage to a blockchain.
**Problem / user:** Australian drivers facing fatigue, distraction, slow crash response and disputes or insurance fraud, without costly dashcam hardware.

**Features**
- Driver drowsiness/distraction monitoring — MediaPipe FaceLandmarker (468 landmarks) tracks eye closure and attention in-browser with a voice alert. *[claimed]*
- Road hazard detection — YOLOv8 via ONNX Runtime Web on WebGPU detects vehicles and hazards and estimates following distance. *[claimed]*
- Crash and harsh-braking detection — DeviceMotion G-force thresholds flag impacts. *[claimed]*
- Automatic 000 call with AI voice — On crash, calls emergency services with GPS and an Amazon Polly generated spoken message. *[claimed]*
- Blockchain-verified footage — SHA-256 hash of video recorded in a Base Sepolia transaction to prove no tampering. *[claimed]*
- Pull-over suggestions — After repeated fatigue, suggests nearby safe stops via live location. *[claimed]*
- Drive reports, score and leaderboard — Per-trip log of fatigue, distraction, braking, crashes plus driver score. *[claimed]*

**Flow:** Open the web link on a phone → Start a drive session with face and road cameras → Receive voice alerts on fatigue → Crash triggers emergency call flow → Footage hash verified on chain and trip report saved

**Prompt:** UNIHACK 2026 Social Impact Prize: best idea addressing an issue in the local community.
**Fit (implied):** Addresses Australian road deaths with statistics cited; no explicit prize targeting statement on the page.  *(targeted: SOCIAL IMPACT PRIZE, 4th)*
**AI:** Edge/in-browser vision: MediaPipe face landmarks and YOLOv8 on WebGPU; Polly TTS for emergency message; Anthropic SDK and Google Generative AI tags with unexplained roles.
**Architecture:** TanStack Start React app with oRPC/Zod API, Prisma/Postgres (Supabase), S3 pre-signed uploads, Base Sepolia hashing, Vercel hosting.
**Novelty:** Packs driver monitoring, hazard detection, crash response and chain-of-custody for footage into a no-install web app; unusual breadth for a weekend.
**Scope:** medium · working: Live demo URL listed (beesafe.unihack.me); team tested on real road trips; no videos or metrics. · polish: Many integrations and screenshots; crash thresholds iterated.
**Claims:** Drowsiness detection with sub-33ms latency (own claim) | Cites over 1,500 Australian road deaths and fatigue in up to 35% of fatal crashes | No accuracy metrics
**Gaps:** No repo linked; Prize rank listed as 4th in queue; page shows no prize; Anthropic/Gemini/Alchemy use unexplained
Sources: https://devpost.com/software/beesafe-njd4hi, prompts_cache/unihack-2026.md

---

### Cowdar
*UNIHACK UNIHACK 2026 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** THIRD PLACE [3rd]

**What it is:** An open-source iPhone app that estimates a cow's weight from a LiDAR scan plus a photo. A custom pose model finds body landmarks, the server measures 3D distances between them, and a variant of Schaeffer's formula yields the weight.
**Problem / user:** Small-scale farmers for whom commercial livestock weight systems are expensive, subscription-based or abandoned.

**Features**
- LiDAR plus photo capture — iOS app using ARKit LiDAR sensor and camera *[shown_working]*
- Cow pose keypoints — YOLOv8m-pose trained on 1,042 labelled images from Roboflow, 100 epochs on a T4 GPU *[shown_working]*
- 3D measurement — Point cloud projected to 2D; keypoints matched to nearest points to compute body length and radius *[claimed]*
- Weight prediction — Variant of Schaeffer's formula from measured distances *[claimed]*
- Scan history — View past scans and predictions *[claimed]*
- Extra feature input — Optional additional inputs on a separate screen *[claimed]*

**Flow:** Scan cow with LiDAR and take photo → Optionally add extra features → Server detects pose points → Distances computed in 3D → App shows predicted weight → Review past scans later

**Prompt:** Third Place: the bronze medal in UNIHACK 2026 main prizes.
**Fit (none):** General placement prize; project is a free tool to give small farmers phone-based weight estimates. No sponsor tie.  *(targeted: Third Place (Main Prize))*
**AI:** Custom-trained YOLOv8m-pose model detects labelled points on cows; 3D geometry from LiDAR then feeds a Schaeffer-style formula. Dark Angus hides and small dataset were limits.
**Architecture:** Swift ARKit iOS app sends LiDAR and photo to Python FastAPI server running the pose model and distance matching; results returned to app.
**Novelty:** Uses consumer phone LiDAR for livestock weighing with a self-trained pose model; open-source for small farmers.
**Scope:** medium · working: Devpost claims working proof of concept pipeline; screenshots only; no accuracy figures. · polish: Several screens, GitHub repo listed, no video.
**Claims:** Accurate weight estimates, no error metrics given
**Gaps:** repo github.com/boblao8/CowDar not read; no video; no accuracy measurements
Sources: https://devpost.com/software/cowdar, https://unihack2026.devpost.com/

---

### Echo (UNSW/USYD)
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** BEST DESIGN

**What it is:** Echo is a privacy-first app where a user types a hard thought, the thought is anonymised and embedded, and the app reports how many others felt similarly and shows their anonymised experiences and what helped them.
**Problem / user:** People with intrusive or isolating thoughts who find therapy waitlists, chatbots and affirmation apps unsatisfying and want proof others share the feeling.

**Features**
- Thought submission and match count — Pipeline anonymises, rewrites and embeds the text, then Elasticsearch kNN returns a count like 'N people felt this'. *[shown_working]*
- Three-stage AI pipeline — Qwen3.5-0.8B (Ollama) strips PII, NanoGPT humanises to 50-60 words and tags a theme, MiniLM makes 384-d vectors. *[shown_working]*
- What Helped notes — Resolved thoughts can carry advice shown verbatim; advice-first toggle filters to them. *[shown_working]*
- Breathing With Others — Home animation intensity follows weekly co-presence counts from Elastic aggregates. *[shown_working]*
- Future You letters — Local notes to self resurfaced when same theme recurs. *[shown_working]*
- Crisis guardrails — Static helpline block for risk themes, rendered client-side with no logging. *[shown_working]*
- Local trends and history — Encrypted (AES-GCM) localStorage history, theme frequency, recurrence and quiet-win insights. *[shown_working]*
- Topic bubbles and constellation graph — Browse by theme without typing. *[shown_working]*

**Flow:** Tap logo and type or dictate a thought → Breathing animation while pipeline runs → See similar-people count → Scroll anonymised cards, optionally advice-only → Resolve thought and leave advice or Future You note → Review trends

**Prompt:** UNIHACK 2026 Best Design: most usable and best-looking user interface.
**Fit (explicit):** README lists Best Design with the breathing animation, count reveal, card scroll UX and Future You letters; also targets AI Solutions, Elastic and Social Impact.  *(targeted: BEST DESIGN)*
**Sponsor tools:** Elasticsearch (vector similarity search, search_after pagination, aggregates, core)
**AI:** Small self-hosted model for anonymisation, 122B hosted model for rewrite and theme classification, local sentence embeddings for semantic matching.
**Architecture:** Next.js/Capacitor client, FastAPI + Postgres backend, Ollama, Elasticsearch, five-service Docker Compose.
**Novelty:** Enforces a no-raw-text-stored invariant with documented breach analysis; no chatbot or feed.
**Scope:** large · working: Deployed Vercel demo and video; 399 backend tests and Playwright E2E claimed. · polish: 15 documented features, docs folder, Android APK build, CI.
**Claims:** 399 pytest tests | 30+ theme categories | Raw text never persisted server-side
**Gaps:** Seed data is demo data, dataset size unverified
Sources: https://devpost.com/software/echo-107u6c, evidence/unihack-unihack-2026-echo-unsw-usyd.json, prompts_cache/unihack-2026.md

---

### Guardia
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** SOCIAL IMPACT PRIZE, 3rd [3rd]

**What it is:** A safety-aware walking navigation web app for women out alone at night. It scores routes using about 10,000 public incident records for Melbourne, shows incident areas, gives voice alerts near past incidents, and offers a one-tap AI companion call and SOS button.
**Problem / user:** Women walking alone at night, since navigation apps recommend only the fastest route rather than the safest.

**Features**
- Safest-route recommendation — FastAPI backend scores candidate walking paths against incident data stored in Elasticsearch *[claimed]*
- Incident map — Mapbox map displays nearby incident areas with live location tracking *[claimed]*
- Voice alerts — Spoken warnings as the user nears past incident locations *[claimed]*
- AI safety companion — One-tap live call using a HeyGen avatar for guidance and emotional support *[claimed]*
- SOS button — One-tap access to help *[claimed]*
- Incident dataset — Elastic web crawler collected 10,000+ public records, Melbourne only *[claimed]*

**Flow:** Enter destination → Receive a safer route instead of fastest → Walk with nearby incident areas on map → Hear alerts near past incidents → Tap to call AI companion → Tap SOS if unsafe

**Prompt:** Social Impact Prize: the best idea that addresses an issue in your local community. Elastic also offered a Best Use of Elastic Technology prize.
**Fit (implied):** Addresses women's night-walking safety in Melbourne; Elasticsearch and its crawler hold the incident data. Page names no specific target prize.  *(targeted: Social Impact Prize, Best Use of Elastic Technology (possible))*
**Sponsor tools:** Elasticsearch and Elastic web crawler (Collecting and querying incident records for route scoring, core)
**AI:** HeyGen API drives the interactive avatar companion; no language model named. Route scoring is rule-based against incident data.
**Architecture:** React/TypeScript frontend with Mapbox on Vercel; FastAPI route-scoring service on AWS App Runner querying Elasticsearch incident index.
**Novelty:** Reframes navigation around safety using crawled local crime data and a conversational avatar for companionship.
**Scope:** medium · working: Live demo safetyroute.vercel.app; prototype with all components connected per Devpost. · polish: Figma-designed UI, slide-style screenshots; no video; 36 likes.
**Claims:** Processed more than 10,000 public incident records
**Gaps:** repo github.com/dinhanhduytran/unihack2026-guardia not read; no video; no safety validation
Sources: https://devpost.com/software/guardia-9ghij1, https://unihack2026.devpost.com/

---

### HABITMON
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** BEST DESIGN, 2nd [2nd]

**What it is:** A learning-habit game where a user enters a skill goal, gets a roadmap of small tasks from a fairy guide named Lumi, and earns a random gacha monster for each completed task. Monsters roam a habitat and ask daily AI-written revision questions.
**Problem / user:** Learners who lose motivation or get stuck in tutorial hell and find productivity apps like chores.

**Features**
- Personalized learning path — Elasticsearch indexes skills, roadmap steps and resources; backend matches the user's query to a roadmap *[shown_working]*
- Small tasks from Lumi — Fairy companion presents next quest with linked learning resources *[shown_working]*
- Gacha reward — Completing a task spins a reel that reveals a random monster with rarity *[shown_working]*
- Habitat field — Collected monsters wander randomly using timer-based movement *[shown_working]*
- Collection gallery — Owned monsters in colour, unowned as silhouettes *[shown_working]*
- Daily revision — Monsters with exclamation marks ask AI-generated multiple-choice questions and react kindly either way *[claimed]*
- Local save — Progress and monster positions kept in localStorage *[shown_working]*

**Flow:** Type a skill goal such as learn Python → Lumi gives first task with resources → Click Complete Task → Watch gacha reel reveal a monster → Monster joins the habitat → Answer daily revision questions from monsters

**Prompt:** Best Design: awarded to the most usable and best looking user interface (UNIHACK 2026). Also Best Use of Elastic Technology prize existed.
**Fit (implied):** Pixel-art monster collection, animated gacha reveal and habitat UI form the visual identity; Elasticsearch also supplies roadmap search. No stated prize targeting.  *(targeted: Best Design (2nd))*
**Sponsor tools:** Elasticsearch (Search over skills, roadmap steps, resources and topic relationships, core)
**AI:** OpenAI ChatGPT API generates revision questions and surfaces resources per topic; roadmap retrieval relies on Elasticsearch over structured datasets.
**Architecture:** React frontend with CSS keyframe animations and localStorage; Flask REST backend connecting Elasticsearch and OpenAI.
**Novelty:** Applies gacha collection mechanics and virtual pets to skill learning, with monsters delivering spaced-style revision; five first-time hackers on team.
**Scope:** medium · working: Live site habitmon.life; team says prototype reached about 85% of vision; no repo or video. · polish: Animated reveal, pixel-art GIFs; 113 likes and 50 comments.
**Claims:** Roughly 85% of original vision done, self-reported
**Gaps:** no repo; no video
Sources: https://devpost.com/software/habit-habitat, https://unihack2026.devpost.com/

---

### Hooked (UTS)
*UNIHACK UNIHACK 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** BEST USE OF ELASTIC TECHNOLOGY (by Elastic)

**What it is:** Hooked is a fishing social and tracking app for Australian beginner anglers: log catches, identify species (native versus invasive) with Gemini, earn XP, and feed an Elastic dashboard for fisheries agencies.
**Problem / user:** Beginner recreational anglers and environmental agencies lacking localised data on invasive fish.

**Features**
- FishDex catch logging — Catches stored with media and metadata; full-text search through Elasticsearch. *[claimed]*
- AI species ID — Gemini analyses a fish photo and flags native versus invasive. *[claimed]*
- Gamification — XP, levels, achievements, localised challenges, Leonardo AI badges and avatars. *[claimed]*
- Hotspot map — Geospatial Elastic queries and Mapbox endpoint to share hidden spots and mark restricted/invasive areas. *[claimed]*
- Insights dashboard — Tides, lunar, weather and water conditions plus AI summaries. *[claimed]*
- Agency dashboards — Elastic dashboards aggregate catches to track invasive and endangered species. *[claimed]*
- Social features — Home feed, comments, notifications, leaderboard, personal bests. *[claimed]*

**Flow:** Sign up and onboard → Start fishing session from feed → Upload fish photo for AI detection → Log catch; map, XP and badge update → Data flows to Elastic fisheries dashboard

**Prompt:** Best Use of Elastic Technology: most innovative and effective use of Elastic in the project.
**Fit (explicit):** Page describes a Catch-to-Elastic-to-Insights pipeline using Elastic for geospatial queries, full-text search and aggregated agency dashboards.  *(targeted: BEST USE OF ELASTIC TECHNOLOGY (by Elastic))*
**Sponsor tools:** Elastic / Elasticsearch (geospatial queries, FishDex search, fisheries dashboards, core)
**AI:** Gemini for image species ID, NLP and advice; Leonardo AI for generated badges, avatars and FishDex art.
**Architecture:** .NET MAUI Blazor client with C# services, Supabase DB, Elasticsearch indices, Mapbox endpoint.
**Novelty:** Pairs a consumer fishing game with an agency-facing invasive-species data pipeline.
**Scope:** medium · working: Repo ~20k LOC with Supabase schema; no demo or video; README is mostly vision. · polish: Screenshots only; no tests.
**Claims:** End-to-end Catch-to-Elastic-to-Insights pipeline | AI reduces beginner research time (no data)
**Gaps:** README is vision, setup steps absent; Elastic usage not verified in code
Sources: https://devpost.com/software/hooked-47pm25, evidence/unihack-unihack-2026-hooked-uts.json, prompts_cache/unihack-2026.md

---

### MeshMap (UNSW)
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** SOCIAL IMPACT PRIZE

**What it is:** MeshMap (MeshChat) is an off-grid Bluetooth Low Energy mesh for iOS and Android with group chat, map-based event posting, encrypted DMs, SOS alerts and web-of-trust scoring, plus a MeshNews website that turns mesh data into LLM-written reports.
**Problem / user:** Civilians in internet shutdowns or disasters (Iran blackout cited) who cannot reach help or family.

**Features**
- BLE mesh chat — Dual-role advertise/scan, TTL relay, dedupe by envelope id, 512-byte cap, image chunking. *[shown_working]*
- Map events and labels — Hazard, help, emergency posts within 5 km, clustered by distance and time. *[claimed]*
- Encrypted DMs — X25519 ECDH, HKDF-SHA256, AES-GCM routed through nodes. *[claimed]*
- SOS alerts — Broadcasts location and rebroadcasts after 0.3 s. *[claimed]*
- Web of Trust — Vouch/deny votes, proximity and 2-hour time decay. *[claimed]*
- MeshNews — Nodes upload data over Wi-Fi; Claude generates reports; Twilio escalation. *[claimed]*
- Offline app sharing — Android distributes the app via Bluetooth. *[claimed]*

**Flow:** Install and get persistent identity → Join public chat across nearby phones → Post or browse map events → Vouch or dispute alerts → Trigger SOS → Upload data to MeshNews when online

**Prompt:** UNIHACK 2026 Social Impact Prize: best idea addressing an issue in the local community.
**Fit (implied):** Frames communication during shutdowns and outages as a humanitarian problem; no explicit prize statement.  *(targeted: SOCIAL IMPACT PRIZE)*
**AI:** Claude API generates news-style reports from aggregated mesh events; no AI in the mesh.
**Architecture:** Swift and Kotlin apps over BLE GATT mesh; Next.js/Supabase MeshNews server for aggregation, reports and SOS escalation.
**Novelty:** Native BLE mesh on both platforms plus trust scoring, image chunking and a news-aggregation layer, built by mostly first-time hackers.
**Scope:** large · working: Two native apps and web app (~19k LOC), YouTube demo and Vercel site; no field tests reported. · polish: Whitepaper, architecture docs, dark mode, multilingual UI; no tests.
**Claims:** ~100 m per hop, up to seven hops | Images compressed to 12 KB | Design figures only, no measured delivery rates
**Gaps:** Twilio role beyond SOS escalation unclear; README image chunk size (40 bytes) differs from Devpost image sizing
Sources: https://devpost.com/software/meshnet, evidence/unihack-unihack-2026-meshmap-unsw.json, prompts_cache/unihack-2026.md

---

### Peersuade
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** BEST DESIGN, 3rd [3rd]; MOST FUN IDEA

**What it is:** A real-time browser party game where two players on separate devices debate a randomized policy topic as generated political candidates. Five AI voters with distinct personalities judge them, and players can hit an OBJECTION! button to take the floor.
**Problem / user:** Young voters, especially Gen Z, disengaged from politics; debates feel dull. Also pitched for party play and classrooms.

**Features**
- 1v1 live debate lobby — Two players join from separate devices; server-authoritative state pushed via Socket.io *[shown_working]*
- Candidate and topic generation — Generated profiles with serious and absurd policy topics *[shown_working]*
- Voice and live transcription — Agora RTC carries audio; Groq Whisper transcribes in streamed chunks *[shown_working]*
- OBJECTION! interrupt — Button lets a player seize the floor mid-speech *[shown_working]*
- AI jury — Five Gemini Flash voters with personalities vote after two rounds and give short reasons *[shown_working]*
- Reconnect recovery — Rejoining player gets full current state without desyncing opponent *[claimed]*
- Party-mode visuals — Jackbox-style presentation of results and winner reveal *[shown_working]*

**Flow:** Join lobby from two devices → Receive candidate profile and topic → Debate aloud for two rounds with live transcript → Optionally shout OBJECTION! → Five AI voters deliberate and vote → See reasoning, results and winner reveal

**Prompt:** Most Fun Idea: create the most fun and delightful experience, whether a game, bot or something else; Best Design 3rd also won.
**Fit (implied):** A party game with comedic AI jurors and an interrupt mechanic fits the fun-experience prize; Jackbox-like UI supports the design placing.  *(targeted: Most Fun Idea, Best Design (3rd))*
**AI:** Gemini Flash agents prompted with individual voter personalities and scoring guidance; prompts tuned to remove bias toward last or longer speaker. Groq Whisper does speech to text.
**Architecture:** Next.js 15/React 19 client with Express and Socket.io server holding all game state; Agora RTC for audio; Whisper and Gemini APIs.
**Novelty:** Turns political debate into a voice-driven party game with AI jurors; prompt iteration to equalize win chances.
**Scope:** medium · working: Live demo politics-game.vercel.app; team says full loop works across two devices. · polish: Jackbox-style UI, party-mode GIF; no repo link or video; 86 likes.
**Claims:** Full lobby to winner loop works in real time across devices | About 47% of Australian Gen Z voters cited fines as motivation (cited stat)
**Gaps:** no repo; no video
Sources: https://devpost.com/software/peersuade, https://unihack2026.devpost.com/

---

### Safe Trace (UQ/Monash)
*UNIHACK UNIHACK 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** AI SOLUTIONS PRIZE (by Quantium)

**What it is:** Safe Trace uses a Raspberry Pi camera streaming to a PC, where a YOLO model checks whether workers wear selected PPE and computes a daily safety score. A Node.js UI shows footage. This is workplace-safety monitoring; the page states no consent or privacy safeguards.
**Problem / user:** Employers who want to verify procedures and PPE compliance to reduce preventable workplace accidents.

**Features**
- PPE detection — Self-trained CV model scans camera footage for which PPE each person has or lacks. *[claimed]*
- Pi to PC streaming — Raspberry Pi camera streams over WiFi to a home computer acting as server. *[claimed]*
- Selectable PPE types — UI lets the user choose which PPE to check. *[claimed]*
- Safety score — End-of-day score of violations divided by possible violations. *[claimed]*
- Node.js footage UI — Browser UI for watching footage. *[claimed]*

**Flow:** Pi streams video to server → Model scans for PPE → User opens UI and picks PPE types → End-of-day safety score computed

**Prompt:** AI Solutions Prize (Quantium): team that best uses AI as an impactful part of its solution.
**Fit (implied):** A trained computer-vision model is the core of the product; page does not mention the prize.  *(targeted: AI SOLUTIONS PRIZE (by Quantium))*
**AI:** YOLO (Ultralytics) trained on a PPE dataset for detection; Claude and Gemini tags with unexplained roles.
**Architecture:** Pi camera streams to PC running Flask/FastAPI inference; Node.js UI and score computation.
**Novelty:** Hardware-in-the-loop edge camera plus self-trained model, unusual for a first-time team.
**Scope:** small · working: Page says model trained and UI built; no demo, repo or video. · polish: Two screenshots-level page; no metrics.
**Claims:** Trained own model in short time | No accuracy figures
**Gaps:** No repo; No consent or privacy safeguards stated; Dataset unnamed
Sources: https://devpost.com/software/safe-trace, prompts_cache/unihack-2026.md

---

### Sentinel AI
*UNIHACK UNIHACK 2026 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** SECOND PLACE [2nd]

**What it is:** Web app that lets a user direct a DJI drone in plain language, typed or spoken. An Android app bridges the drone to a server where an OpenAI-based agent reads telemetry and vision output and sends commands; it can also analyze saved footage.
**Problem / user:** Piloting drones needs skill and training, and hiring operators is costly; the team wants simple tasks like checking a field or monitoring property to be done by describing the goal.

**Features**
- Natural-language drone control — agent turns typed or spoken goals into commands sent through an Android bridge app to a supported DJI drone *[claimed]*
- Android bridge app — Kotlin app on DJI Mobile SDK handles connection, controls, telemetry and video *[claimed]*
- Live telemetry stream — drone state, GPS and sensor data pushed to the server over WebSockets and shown in the dashboard *[claimed]*
- Live video to server — FFmpeg pushes drone video over RTMP; YOLO and vision models interpret frames *[claimed]*
- Footage analysis — user asks questions about existing footage in natural language; Elastic stores object timestamps *[claimed]*
- Web command center — Next.js UI with command center, mobile view and video analysis view *[shown_working]*
- Arduino long-range telemetry bridge — Arduino with GPS, radio module, barometer and other sensors for longer-distance telemetry *[claimed]*
- Drone swarm coordination — scaling to 10-100 drones *[planned]*

**Flow:** Open the web app → Type or speak a goal such as checking a field for people → Agent combines telemetry, GPS and vision output → Commands go to the drone through the Android bridge → Live video streams back to the server → Optionally query saved footage in natural language

**Prompt:** not public / not found
**Fit (none):** Overall placement prize; no specific track text found. Project is a general-purpose autonomous-drone agent with stated uses in monitoring and bushfire detection.  *(targeted: SECOND PLACE (overall))*
**Sponsor tools:** Elastic (storing and retrieving object timestamps from video analysis, supporting)
**AI:** OpenAI API agent with custom tools in an agentic loop using telemetry, GPS and drone state; YOLO for image recognition; RunPod used to test video-editing models and Hugging Face fine-tunes.
**Architecture:** Android app (DJI MSDK, FFmpeg RTMP) <-> Express.js telemetry server (WebSockets) <-> OpenAI agent; Next.js frontend on Vercel; Elastic for timestamp storage; simulated Android environment for pre-flight testing.
**Novelty:** Ties a consumer DJI drone to an LLM agent through a custom Android bridge and adds an Arduino telemetry module; hardware plus real-time video pipeline is unusually broad for a student hackathon.
**Scope:** medium · working: Demo site, repo link and YouTube video exist; the page gives no flight results or metrics. · polish: Deployed Next.js site with animations, CI checks, simulation environment mentioned.
**Claims:** Won second place at UNIHACK 2026 | Supports long-range missions, property monitoring and bushfire detection | Planned scaling to 10-100 drone swarms
**Gaps:** GitHub repo (GabrielRips/Sentinal_OS) not read; no prize text; demo video not watchable
Sources: https://devpost.com/software/sentinel-ai-rzp29l

---

### SlothMotion
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** SOCIAL IMPACT PRIZE, 2nd [2nd]

**What it is:** Browser-based home exercise coach for adults 65 and over. A webcam tracks body pose with MediaPipe, compares it to a recorded reference routine, and tells the user in real time whether the movement is correct and safe, in a large high-contrast interface.
**Problem / user:** 57% of Australians 65+ miss activity guidelines; mobility limits, health conditions and gym discomfort get in the way. Targets older adults who may find technology intimidating.

**Features**
- Webcam pose tracking — MediaPipe Pose extracts landmarks (shoulders, elbows, hips, knees) from the live camera feed *[shown_working]*
- Reference-routine comparison — normalizes detected pose and compares joint positions to a pre-recorded exercise reference with tolerance thresholds *[shown_working]*
- Real-time feedback — tells user whether movement is done correctly and safely *[shown_working]*
- Difficulty selection and guided routines — user picks level and follows a routine *[claimed]*
- Elder-friendly UI — large fonts, high contrast, clear instructions, simple navigation *[shown_working]*
- Ailment-tailored routines — personalization for physical conditions; more conditions listed as future *[claimed]*
- Voice control, AI assistant, daily reminders — hands-free navigation, Q&A helper, notifications *[planned]*

**Flow:** Open the web app and choose difficulty → Start a guided routine → Webcam tracks joints → App compares pose against the reference → Gets immediate correct/incorrect feedback

**Prompt:** not public / not found
**Fit (implied):** Addresses health and accessibility for older Australians; the page frames it around inactivity statistics and barriers, though it does not cite the prize text.  *(targeted: SOCIAL IMPACT PRIZE, 2nd)*
**AI:** MediaPipe Pose for real-time landmark estimation; custom rule-based pose normalization and joint-difference comparison. No LLM; AI assistant is only planned.
**Architecture:** React + Vite + TypeScript frontend reads webcam, runs MediaPipe in the client, custom comparison logic against stored reference pose; Supabase listed as a tag but role not described.
**Novelty:** Narrow demographic focus with accessibility-first UI; pose comparison against a recorded reference rather than generic rep counting.
**Scope:** small · working: Page states a functional prototype; four screenshots, one GIF and a video exist; no live link. · polish: Accessibility styling is a stated focus; no metrics or user testing.
**Claims:** 57% of Australians 65+ do not meet activity guidelines (cited stat) | Functional prototype built despite no prior computer vision experience
**Gaps:** repo mymikody/slothmotion not read; prize text not found
Sources: https://devpost.com/software/slothmotion

---

### StepFlow
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** FIRST TIMERS PRIZE (by Atlassian)

**What it is:** StepFlow is a gamified study planner for university students: enter tasks and tests with topics, upload notes, rate confidence, then run a day in one of two game modes while a Q-learning scheduler and LLM-generated quizzes adapt revision timing.
**Problem / user:** University students overwhelmed by too many tasks and unsure when to revise.

**Features**
- Task and test entry — Tests carry topics, uploads and 1-10 confidence ratings. *[claimed]*
- Start Day study modes — Shoot-targets mode or spinning wheel with one fun task picks next task. *[claimed]*
- Task timers — Per-task timers for focus. *[claimed]*
- RAG recall quizzes — PDFs chunked into ChromaDB; Llama 3 via Ollama writes JSON questions. *[claimed]*
- Adaptive scheduling — Ebbinghaus retention model R(t)=e^(-t/S) with Q-learning over up to 60 weekly candidate schedules. *[claimed]*
- End-of-day reflection — Asks what blocked missed tasks. *[claimed]*

**Flow:** Enter tasks and tests → Upload notes and rate confidence → Press Start Day → Pick a mode and work tasks with timers → Take recall quizzes → Reflect at day end

**Prompt:** First Timers Prize (Atlassian): best project by first-time hackathon participants.
**Fit (implied):** Page lists the win; the team built a full-stack scheduler plus quiz system as first-timers.  *(targeted: FIRST TIMERS PRIZE (by Atlassian))*
**AI:** Local Llama 3 with RAG for quizzes; Q-learning scheduler simulating weeks ahead; Ebbinghaus memory model.
**Architecture:** React/Vite frontend, FastAPI backend with SQLite, ChromaDB and LangChain, Ollama; Firebase tag.
**Novelty:** Uses a forgetting-curve simulation with reinforcement learning to choose revision timing and wraps tasks in game modes.
**Scope:** medium · working: Demo video embedded; repo README is the Vite template only; no metrics. · polish: Six screenshots, Canva design; README unhelpful.
**Claims:** Q-learning scheduler integrated with frontend | Up to 60 schedules simulated | No quantitative results
**Gaps:** README is the default Vite template; Page calls the scheduler both unsupervised and Q-learning
Sources: https://devpost.com/software/stepflow, https://raw.githubusercontent.com/nayc-599/revise-right/HEAD/README.md, prompts_cache/unihack-2026.md

---

### ToiletGO (Monash/UniMelb)
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** MOST ENTERTAINING PITCH

**What it is:** ToiletGO (Devpost title Orion) is a desktop web app for finding nearby public toilets with ratings, reviews, filters, a Gemini photo-based cleanliness estimate for unreviewed toilets, and a built-in endless-runner-style game with leaderboard.
**Problem / user:** People needing a public toilet who cannot judge its condition from a star rating.

**Features**
- Nearby toilet search — Browser geolocation plus toilet data scraped from the national toilet map. *[claimed]*
- Reviews and ratings — Users write reviews; stored in local storage. *[claimed]*
- Photo cleanliness estimate — Uploaded image goes to Gemini for a visible condition rating. *[claimed]*
- Filters and dark mode — Filter results; dark mode. *[claimed]*
- Toilet game — Subway Surfers-inspired game with Express-backed leaderboard. *[claimed]*

**Flow:** Sign in → Allow location → Browse nearby list → Open toilet to see facilities and reviews → Write review or upload photo → Play game

**Prompt:** not public / not found
**Fit (none):** Humorous concept and a toilet-themed game; no prize text found and the page does not mention pitching.  *(targeted: MOST ENTERTAINING PITCH)*
**AI:** Gemini image analysis rates cleanliness from uploaded photos.
**Architecture:** React/Vite TypeScript client, Express server for leaderboard, Gemini API key via .env, local storage for reviews.
**Novelty:** Comedic scope with a game bolted on; data source licensed for personal use only.
**Scope:** small · working: ~2.9k LOC and install steps; no demo or video. · polish: Six screenshots; no tests.
**Claims:** Finished a working product after dropping first idea
**Gaps:** No official prize text for Most Entertaining Pitch (not in 2026 cache); Python tag unexplained
Sources: https://devpost.com/software/orion-15qdnf, evidence/unihack-unihack-2026-toiletgo-monash-unimelb.json

---

### Tracksync (UNSW)
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** MOST CREATIVE IDEA

**What it is:** TrackSync is 'git for music': producers push WAV stems from a modified LMMS plugin to a FastAPI/GitPython backend, review pull requests in a browser with side-by-side waveforms, and resolve conflicts by listening.
**Problem / user:** Remote music co-producers who swap files by hand with no versioning and find command-line git too hard.

**Features**
- LMMS push/pull plugin — C++ Qt sidebar renders tracks to WAV and uploads or downloads them. *[shown_working]*
- Branches and pull requests — Project stored as a server-side git repo with tracks per branch. *[shown_working]*
- Waveform review — Wavesurfer.js side-by-side comparison in the web app. *[shown_working]*
- Audio conflict resolution — Conflicts when same track name has different audio; user listens and chooses. *[shown_working]*
- Auto-mixed preview — FFmpeg mixes stems into main.mp3. *[claimed]*
- Issues board — Screenshots show an issues view. *[unclear]*

**Flow:** Create project and copy ID → Connect LMMS plugin on a feature branch → Push stems → Open pull request on web → Resolve conflicts and merge → Pull merged tracks

**Prompt:** UNIHACK 2026 Most Creative Idea: most original idea or reinvention.
**Fit (implied):** Reinvents git workflow for audio; no explicit prize statement.  *(targeted: MOST CREATIVE IDEA)*
**AI:** none
**Architecture:** LMMS plugin calls FastAPI on Railway; GitPython repos on volume; React on Vercel; Supabase optional.
**Novelty:** Modifies a real DAW to integrate version control and audio-aware conflict resolution.
**Scope:** medium · working: Deployed web and backend URLs and YouTube demo in README. · polish: Deployment guide; no tests; auth not implemented.
**Claims:** Emulates git features for audio files
**Gaps:** Issues board not described in README
Sources: https://devpost.com/software/tracksync, evidence/unihack-unihack-2026-tracksync-unsw.json, prompts_cache/unihack-2026.md

---

### UniAid (Monash)
*UNIHACK UNIHACK 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** PEOPLE'S CHOICE

**What it is:** UniAid is a mentor-matching web app for new university students and parents: users describe needs in free text and an embedding model plus learning-to-rank returns mentors covering visa, housing, culture and career.
**Problem / user:** International and new students (and worried parents) who cannot find university guidance in one place.

**Features**
- Natural-language mentor search — Sentence embeddings with nearest-neighbour index over mentor profiles. *[claimed]*
- Requirement-aware ranking — Learning-to-rank (LightGBM-style) plus checks like visa and language. *[claimed]*
- Auth and profiles — Sign-up, login, mentor profile browsing. *[claimed]*
- Dataset sync — CSV mentors, mentees, interactions loaded into Postgres. *[shown_working]*

**Flow:** Sign up or log in → Type request → Receive ranked mentors → Browse profiles

**Prompt:** UNIHACK 2026 People's Choice: voted prize, no description given.
**Fit (none):** No stated link; relatable student-support concept with a deployed demo.  *(targeted: PEOPLE'S CHOICE)*
**Sponsor tools:** Elasticsearch (listed in built-with only; role not described, unclear)
**AI:** Sentence-transformer embeddings and learning-to-rank trained on mentor and interaction data; CPU-only.
**Architecture:** React/Vite on Netlify, FastAPI + Postgres + ML recommender on one VM.
**Novelty:** Explainable hybrid of semantic and constraint matching with a trained ranker.
**Scope:** medium · working: Netlify demo URL and ~10k LOC repo with ML build scripts; dataset is synthetic CSV. · polish: Five screenshots; backend README only.
**Claims:** End-to-end working in production | No metrics
**Gaps:** Elasticsearch and LLM tags unexplained; Dataset origin unclear
Sources: https://devpost.com/software/uniaid-tvojlk, evidence/unihack-unihack-2026-uniaid-monash.json, prompts_cache/unihack-2026.md

---

