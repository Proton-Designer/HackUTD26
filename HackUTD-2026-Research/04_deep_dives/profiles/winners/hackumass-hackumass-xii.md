# HackUMass — HackUMass XII (24 projects)

### 2D fun game!!!
*HackUMass HackUMass XII · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best UI/UX

**What it is:** A small Godot pixel-art 2D platformer in which the player controls a character named Crimson through a setting, completing tasks and challenges with power-ups and visual cues. Distributed as a downloadable build via a shared drive folder.
**Problem / user:** Students and workers who want a simple game to relieve stress; also pushes back on the idea that 2D games feel flat or limited.

**Features**
- Platformer character — Crimson moves with double jumps and speed bursts *[claimed]*
- Pixel-art visuals and effects — Nostalgic style with visual effects throughout, sprites sourced online *[claimed]*
- Tasks and challenges — Player navigates a defined setting completing objectives *[claimed]*
- Power-ups and visual cues — Rewarding feedback for player actions *[claimed]*
- Simple storyline — Light narrative kept uncluttered *[claimed]*
- Planned expansion — More levels, environments, mechanics and storyline *[planned]*

**Flow:** Download the game from the linked Google Drive folder → Launch and control Crimson → Complete tasks and challenges using jumps, bursts and power-ups

**Prompt:** Best UI/UX: judges look for the nicest-looking design, with mention of Figma templates; prize a Kodak film camera.
**Fit (implied):** Emphasizes pixel-art visuals, effects and visual cues; page does not state it targeted the prize.  *(targeted: Best UI/UX)*
**AI:** none
**Architecture:** Single Godot game project with internet-sourced sprites and scenes; shared as a build in a Drive folder.
**Novelty:** Conventional pixel platformer; entry stands on its look and feel rather than a technical angle.
**Scope:** tiny · working: Downloadable build via Drive link; four screenshots; no repo or video. · polish: Visual effects and power-ups claimed; assets from internet.
**Gaps:** No repo; No gameplay video; Screenshots undescribed
Sources: https://devpost.com/software/2d-fun-game, https://hackumass-xii.devpost.com/

---

### Ai-Companion
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Wolfram Award

**What it is:** A Unity desktop pet-style AI companion with an animated character you talk to by voice; it replies in speech, remembers you through a local JSON profile, and can pull news and weather or add calendar entries on keyword triggers.
**Problem / user:** People with heavy screen time seeking a personalized, emotionally engaging presence and help with everyday tasks.

**Features**
- Voice conversation — Whisper speech-to-text in, OpenAI GPT reply, ElevenLabs speech out *[shown_working]*
- Persistent memory — Local JSON profile plus memory and sentiment logs; one LLM call finds profile updates, another injects relevant memories *[claimed]*
- Emotional responsiveness — Detects emotional cues in language and adapts tone and motivational phrases *[claimed]*
- Real-time info — Keyword-triggered NewsAPI and OpenWeatherMap data injection *[claimed]*
- System actions — Keyword scanning, Unity functions and a Windows DLL for things like calendar entries *[claimed]*
- Animated character — On-screen character with behaviors, commands and a pick-up interaction (GIFs on page) *[shown_working]*
- Modular design — Built for modding and expansion; multilingual via Whisper and ElevenLabs *[claimed]*

**Flow:** Speak to the on-screen companion → Whisper transcribes → First LLM call updates the profile → Second call injects memories and any news or weather → GPT replies and ElevenLabs speaks it → Keyword requests trigger actions such as calendar entries

**Prompt:** Wolfram Award: five winners get a year of Wolfram One Professional; the public page gives no description or criteria.
**Fit (none):** No visible connection to Wolfram tools or the award; no stated rationale.  *(targeted: Wolfram Award)*
**Sponsor tools:** OpenAI (gpt-4o-mini dialogue and profile logic, core); ElevenLabs (text-to-speech, supporting)
**AI:** gpt-4o-mini via the OpenAI-Unity package, prompt-engineered two-pass memory over JSON profiles, Whisper STT and ElevenLabs TTS.
**Architecture:** Unity/C# app with animated pet art (VPet), API calls to OpenAI, Whisper, ElevenLabs, NewsAPI, OpenWeatherMap, local JSON memory store and Windows DLL hooks.
**Novelty:** Adds a prompt-based memory layer and keyword-triggered tools to a desktop pet character using third-party Unity OpenAI package.
**Scope:** small · working: Screenshots and GIFs of character behaviors; real repo README is a one-line link; no demo video. · polish: Animated character with Figma-designed menus.
**Claims:** Multilingual support through Whisper and ElevenLabs | Memory turns the chatbot into a companion
**Gaps:** Queue github_url points to the third-party OpenAI-Unity package, not the project repo (haoranXie/AiCompanion on the page); Real repo README only links Devpost; No code or video reviewed
Sources: https://devpost.com/software/ai-companion-d3681a, https://raw.githubusercontent.com/haoranXie/AiCompanion/HEAD/README.md, https://hackumass-xii.devpost.com/

---

### Braille Assist
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Wolfram Award

**What it is:** An Arduino-driven hardware prototype that converts typed text into Braille and renders it on a physical tactile device, with motors raising and lowering cells inside a 3D-printed box.
**Problem / user:** Braille readers (implied) who would benefit from written information turned into tactile output rather than a screen.

**Features**
- Text to Braille conversion — Software maps typed letters to Braille patterns (Python and C++) *[claimed]*
- Tactile output — Motors move the right cells at the right time to show the characters *[claimed]*
- Physical enclosure — 3D-printed box houses the display and wiring *[shown_working]*
- Planned numbers and precision — Add number support and improve accuracy *[planned]*

**Flow:** Type text → Software converts it to Braille → Arduino drives motors to form the characters on the device

**Prompt:** Wolfram Award: five winners get a year of Wolfram One Professional; the public page gives no description or criteria.
**Fit (none):** No stated connection to Wolfram; accessibility hardware project.  *(targeted: Wolfram Award)*
**AI:** none
**Architecture:** Python/C++ software converts text to Braille and signals an Arduino that drives motors in a 3D-printed enclosure.
**Novelty:** Beginner-built mechanical Braille display from motors rather than a screen-only translator.
**Scope:** tiny · working: Photos of hardware and wiring on Devpost; repo is one Arduino folder with about 200 LOC and no README. · polish: 3D-printed final box; no demo video.
**Claims:** Team's only stated accomplishment is that they built everything
**Gaps:** Repo has no README; Mechanism of cells not described; No video
Sources: https://devpost.com/software/braille-assist-1683ru, evidence/braille-assist.json (no README, 5 files), https://hackumass-xii.devpost.com/

---

### Dice Aid
*HackUMass HackUMass XII · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Mechanical Hack

**What it is:** A Raspberry Pi device that launches a set of dice into a play area at the press of a button, photographs them, recognizes the pips, sweeps them back, and shows an image and total on an attached screen.
**Problem / user:** Players who struggle with traditional dice rolling, wanting accessible, unbiased rolls for any game.

**Features**
- Automatic rolling — Stepper motors launch the dice and later sweep them back up *[shown_working]*
- Dot recognition — Camera captures landed dice and software counts pips *[shown_working]*
- On-screen result — UI displays the camera image and sum total *[shown_working]*
- Custom shell — CAD-designed enclosure for the mechanism *[claimed]*

**Flow:** Place dice in the machine → Press a button → Dice launched into play area → Camera analyses them → Dice swept back → Screen shows image and total

**Prompt:** Best Mechanical Hack: projects using mechanical systems to the best of their ability; prize an electronics kit.
**Fit (implied):** Motorized launch and sweep mechanism with CAD shell plus vision recognition; page does not cite the prize.  *(targeted: Best Mechanical Hack)*
**AI:** Camera-based dot recognition; no model or library named.
**Architecture:** Raspberry Pi 4B with camera and stepper motors via an EE-built interface; Python UI and recognition; mechanical shell designed by a MechE.
**Novelty:** Closes the loop from physical roll to vision-read result with accessibility framing.
**Scope:** small · working: Page reports working camera, dot recognition and tuned steppers; four screenshots; no video or repo. · polish: Multidisciplinary build with custom shell; no metrics.
**Claims:** Unbiased rolling and precise score calculation (no tests reported)
**Gaps:** No repo; No video; Recognition method undescribed
Sources: https://devpost.com/software/dice-aid, https://hackumass-xii.devpost.com/

---

### FoundU
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Wolfram Award

**What it is:** A mobile app for returning lost UMass student ID cards: the finder photographs the card, OCR reads the name, a scraper finds the student's email in the campus directory, and an automated email goes out with the card photo and where it was found.
**Problem / user:** UMass students who lose UCards and finders who cannot reach the owner.

**Features**
- Card photo capture — React Native app uploads image to server via Multer *[claimed]*
- Name extraction — Google Cloud Vision OCR reads the student's name *[claimed]*
- Email lookup — Puppeteer scrapes UMass People Finder with cookie-based session *[claimed]*
- Location capture — Expo Location records where card was found; finder can add contact info *[claimed]*
- Automated email — Nodemailer sends owner the photo and retrieval details *[claimed]*

**Flow:** Finder photographs card → OCR extracts name → Scraper finds email → Finder adds location or contact → Email sent to cardholder

**Prompt:** Wolfram Award: five winners get a year of Wolfram One Professional; the public page gives no description or criteria (page says award was $1,700).
**Fit (none):** No stated link to Wolfram; campus utility project.  *(targeted: Wolfram Award)*
**Sponsor tools:** Google Cloud Vision (OCR of card name, core)
**AI:** Google Vision OCR extracts printed name text; no custom model.
**Architecture:** Expo React Native client posts image to Node/Express server that runs Vision OCR, Puppeteer lookup and Nodemailer email.
**Novelty:** Chains OCR, authenticated directory scraping and email into a no-typing lost-and-found flow.
**Scope:** small · working: Described as fully automated; only a LinkedIn post linked as demo; no repo. · polish: Team photo and logo; no metrics.
**Claims:** One in five students loses a UCard
**Gaps:** No repo; No video; Scraping of campus directory raises privacy questions, no safeguards stated
Sources: https://devpost.com/software/foundu, https://hackumass-xii.devpost.com/

---

### Infraflow
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [MLH] Best Use of Terraform; [HACKUMASS] Best Security Hack

**What it is:** Drag-and-drop editor for cloud architecture diagrams that outputs Terraform configuration for AWS, Azure and GCP. It targets beginners who find infrastructure as code intimidating.
**Problem / user:** Students and DevOps beginners put off by the learning curve of Terraform and cloud infrastructure.

**Features**
- Visual diagram canvas — Place cloud resources and connect them as blocks using a flow-diagram UI *[shown_working]*
- Live Terraform generation — Server translates the diagram schema into Terraform files as you edit *[claimed]*
- Multi-cloud resource sets — AWS, Azure and GCP resource icons and Terraform syntax *[claimed]*
- One-click deploy and lessons — Deploy from the UI and guided DevOps lessons *[planned]*

**Flow:** Open the web app → Drag resources onto canvas → Connect blocks → View generated Terraform → Copy and deploy it yourself

**Prompt:** MLH Best Use of Terraform: use HashiCorp Terraform in the project. Best Security Hack: asks whether you actually hacked something or found a vulnerability.
**Fit (implied):** Terraform generation is the core output. Page does not explain the security prize link, perhaps via beginner-friendly secure infrastructure.  *(targeted: [MLH] Best Use of Terraform, [HACKUMASS] Best Security Hack)*
**Sponsor tools:** Terraform (Output format generated from diagrams, core)
**AI:** none
**Architecture:** Next.js client using @xyflow/react for the canvas; Express/Bun TypeScript server generates Terraform files from diagram JSON.
**Novelty:** Turns a visual diagram directly into provider-specific Terraform rather than being a chat or template tool.
**Scope:** small · working: Live demo links at infraflow.tech and Vercel, screenshots and GIF; ~6.9k LOC. · polish: Polished UI with provider icons; README is one line.
**Claims:** Clean readable Terraform code deployable directly
**Gaps:** Frontend library not stated on page (inferred from package.json); Security prize rationale unstated
Sources: https://devpost.com/software/infraflow, https://hackumass-xii.devpost.com/

---

### Is my house on fire?
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Smart Home Hack

**What it is:** A Raspberry Pi webcam pointed at an oven, with cloud OpenCV checking for on-indicators, and a website that shows oven status, how long it has been on and recent history after pairing with a device code.
**Problem / user:** People in older, cramped apartments who worry about leaving the oven on.

**Features**
- Oven-on detection — Cloud Python/OpenCV looks for red lights, preheat lights and displayed temperature *[claimed]*
- Status website — React site shows current state *[shown_working]*
- Time-on tracking — Displays how long the oven has been on from MongoDB time-series history *[claimed]*
- Device pairing — User enters a device code to connect their Pi *[claimed]*
- Versioned API — Terraform deploys each API version on its own subdomain so older Pis keep working *[claimed]*

**Flow:** Set up Pi with webcam aimed at oven → Vision service checks feed → Open website and enter device code → View status, elapsed time and history

**Prompt:** Best Smart Home Hack: home automation that eases daily life (an AI home assistant is mentioned); prize a smart desk lamp.
**Fit (implied):** Smart-home monitor for an appliance with camera, cloud vision and website; page does not cite prize.  *(targeted: Best Smart Home Hack)*
**Sponsor tools:** MongoDB Atlas (time-series status store, core); Terraform / GCP (deploying site and versioned API, core)
**AI:** Classical computer vision with OpenCV; no trained model named.
**Architecture:** Raspberry Pi webcam uploads to GCP-hosted Python/OpenCV service storing status in MongoDB Atlas time series; React site reads versioned APIs deployed with Terraform.
**Novelty:** Retrofits a dumb appliance with camera-based status; emphasizes versioned IaC deployment for old devices.
**Scope:** small · working: Demo site and test device code on page; repo about 870 LOC with tests and Docker; client README is boilerplate. · polish: Figma logos; no alerts or accuracy numbers.
**Gaps:** Repo README is only Create React App boilerplate; Second repo (raspiHouseFire) not readable; No alerts described
Sources: https://devpost.com/software/is-my-house-on-fire, evidence/is-my-house-on-fire.json (CRA boilerplate README), https://hackumass-xii.devpost.com/

---

### Loop
*HackUMass HackUMass XII · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Android/IOS

**What it is:** A solo-built React Native news and releases app where users subscribe to Interests, each a topic node with AI-summarized newsletter snippets updated daily, with optional per-interest push notifications and a source bell for news surges.
**Problem / user:** People off social media who want to stay current on news and releases (albums, films, concerts) without doomscrolling or paid subscriptions.

**Features**
- Interests — Topic nodes holding summarized snippets with sources *[shown_working]*
- Daily auto-updates — Summaries from newsletters across the web refresh each day *[claimed]*
- Per-interest notifications — Push alerts for urgent relevant news *[claimed]*
- Source bell — Notifies surges from a source such as a local news outlet *[shown_working]*
- No account needed — Optional name entry only *[shown_working]*
- iOS-style UI — Landing page, start page, reader view *[shown_working]*

**Flow:** Open app and optionally enter a name → Subscribe to Interests → Read daily summaries on landing page → Enable notifications for priority Interests

**Prompt:** Best Android/IOS: mobile apps, e.g. a calorie tracker or dining reservation app; prize a power bank.
**Fit (implied):** Mobile app in React Native for Android and iOS; planned store release stated.  *(targeted: Best Android/IOS)*
**AI:** An unnamed AI API summarizes and scrapes web data for each interest; creator said it took longer than expected.
**Architecture:** React Native app plus backend scraping newsletters, summarizing with an AI API and pushing notifications.
**Novelty:** Interest-node feed built to replace social feeds and paid news, with source-surge alerts.
**Scope:** small · working: Five screenshots; repo clone failed so unverified; no demo video. · polish: iOS-style design highlighted; Kickstarter linked after event.
**Claims:** Planned store release about a month later
**Gaps:** Repo clone failed and raw README 404; AI provider unnamed
Sources: https://devpost.com/software/loop-5p83qv, https://hackumass-xii.devpost.com/

---

### Loopwise
*HackUMass HackUMass XII · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Use of ML/AI

**What it is:** A rideshare driver tool that clusters historical ride locations with DBSCAN, forecasts demand with LSTM models, and recommends driving loops through high-demand areas at the right time, shown in a web interface with adjustable radius.
**Problem / user:** Rideshare drivers who idle or roam looking for passengers, losing earnings and fuel.

**Features**
- Hotspot detection — DBSCAN clusters ride pickups by time of day *[claimed]*
- Demand forecasting — LSTM time-series model predicts ride demand *[claimed]*
- Loop generation — Open-source routing builds a loop through recommended coordinates *[claimed]*
- Radius filter — Driver changes loop radius to filter recommendations *[shown_working]*
- Data visualizations — Loss curves, hourly/weekday counts, heatmaps and Leaflet cluster maps *[shown_working]*
- Planned RL and weather — Adaptive learning, reinforcement learning, weather/event data, delivery drivers *[planned]*

**Flow:** Open homepage → View loop for recommended coordinates → Compare loops for other coordinates → Adjust radius to narrow results

**Prompt:** Best Use of ML/AI: intelligent systems using machine learning to solve real-world problems, with predictive analytics and computer vision as examples; $50 gift card.
**Fit (implied):** Applies DBSCAN clustering and LSTM forecasting to GPS ride data to guide drivers; page does not cite prize.  *(targeted: Best Use of ML/AI)*
**AI:** DBSCAN for demand hotspots and LSTM for time-series forecasts, built with scikit-learn and TensorFlow/PyTorch; dataset unnamed.
**Architecture:** Python data processing and models feed Flask/FastAPI backend; React/Next.js frontend with Leaflet maps and open-source routing for loops.
**Novelty:** Turns demand prediction into a closed driving loop rather than a heatmap.
**Scope:** small · working: Screenshots of results and charts; repo about 600 LOC; no demo. · polish: Plots and map visualizations; no numeric metrics.
**Claims:** Drivers save time and earn more (unmeasured)
**Gaps:** Dataset not named; No accuracy numbers
Sources: https://devpost.com/software/loopwise, evidence/loopwise.json (README), https://hackumass-xii.devpost.com/

---

### magic algorithms
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Wolfram Award

**What it is:** A browser-based visualizer where users draw their own graphs and watch Dijkstra shortest paths, minimum spanning tree, and network flow run on them. Built with Vue, TypeScript and HTML canvas and hosted on Netlify.
**Problem / user:** Students (the page mentions UMass CS311) who find graph algorithms hard to grasp from lectures alone and want something interactive.

**Features**
- Custom graph builder — User constructs nodes and weighted/capacity edges on a canvas to run algorithms on. *[claimed]*
- Dijkstra visualization — Shortest-path search on a weighted graph is shown visually; screenshot labeled dijkstras. *[shown_working]*
- Minimum spanning tree visualization — Shows connecting all nodes with minimal total edge weight; screenshot labeled min span tree. *[shown_working]*
- Network flow simulation — Explores capacities and flow through a network; screenshot labeled flow. *[shown_working]*

**Flow:** Open the Netlify web app → Pick one of the three algorithms → Build or define a graph on the canvas → Run the algorithm → Watch the visual step display

**Prompt:** Wolfram Award at HackUMass XII: no description text on the Devpost prize list; the prize is a year of Wolfram One Professional Edition.
**Fit (none):** No stated tie to Wolfram; page does not mention Wolfram tools. Award text has no criteria, so the link is only that it won the prize.  *(targeted: Wolfram Award)*
**AI:** none
**Architecture:** Single-page front end in Vue and TypeScript drawing on an HTML canvas; algorithms run client-side; deployed as a static site on Netlify.
**Novelty:** Education-focused visualizer covering three distinct graph topics in one tool with user-drawn graphs; fairly standard concept for algorithms courses.
**Scope:** small · working: Live Netlify demo link and three algorithm screenshots listed; repo not linked. · polish: Authors admit many bugs and plan a cleaner UI; no video.
**Claims:** Says it delivered a functional, interactive educational tool within the hackathon timeframe. | Hopes to become a standard in CS education (aspiration).
**Gaps:** No repo linked; live demo not opened; No sponsor tie to Wolfram stated; Next steps: UI polish, graph presets, more customizability
Sources: https://devpost.com/software/magic-w453qf, https://hackumass-xii.devpost.com/

---

### Maple.ai
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [MLH] Best AI Project with Databricks Open Source

**What it is:** AI chemistry tutor that listens to the student, reads emotion from their voice, and adapts replies. Retrieval over a MathWorld-derived knowledge base is meant to reduce hallucination, with quizzes and a mood gauge.
**Problem / user:** Students learning hard chemistry topics who get answers but no response to frustration or confusion.

**Features**
- Emotion-aware voice input — Hume EVI transcribes speech and returns the top five emotions when the mic stops *[claimed]*
- Fine-tuned LLM tutor replies — Backend sends text and emotions to an LLM that balances guidance and encouragement *[claimed]*
- RAG knowledge base — Wolfram MathWorld content indexed with DBRX, LanceDB, LlamaIndex and HuggingFace embeddings *[claimed]*
- Mood gauge and trends — Frontend charts emotional state over study sessions *[claimed]*
- Interactive quizzes — Track strengths and weak areas *[claimed]*
- Midnight DApp for student data — Dockerized blockchain app for private tamper-resistant records *[claimed]*

**Flow:** Open tutoring page → Turn on mic and speak → Mic off sends text plus emotions → Read tailored answer rendered with KaTeX → Check mood gauge → Take quizzes

**Prompt:** MLH Best AI Project with Databricks Open Source: build an AI project using Databricks open source projects.
**Fit (explicit):** README names Databricks: DBRX plus LanceDB and LlamaIndex RAG for grounding, and the Databricks chat UI library for the interface.  *(targeted: [MLH] Best AI Project with Databricks Open Source)*
**Sponsor tools:** Databricks (DBRX, chat-ui) (Open-source RAG knowledge base and chat UI, core); Hume EVI (Voice emotion detection, core); Midnight (Privacy-preserving data DApp, supporting)
**AI:** Hume EVI for speech and emotion; DBRX with LlamaIndex/LanceDB RAG over MathWorld; fine-tuned LLM generates replies.
**Architecture:** Next.js frontend with Flask/LangChain backend; Hume EVI input; separate Databricks RAG service; Midnight DApp in Docker.
**Novelty:** Combines affect detection from voice with a grounded tutor and three sponsor stacks in one prototype.
**Scope:** medium · working: ~4.9k LOC across backend, frontend, and sponsor examples; no demo or video; integration extent unclear. · polish: Architecture diagram on Devpost; challenges section empty.
**Claims:** Knowledge base prevents hallucination
**Gaps:** No demo to confirm integration
Sources: https://devpost.com/software/maple-ai, https://github.com/lonexreb/Maple, https://hackumass-xii.devpost.com/

---

### NekoPix
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Wolfram Award

**What it is:** A Next.js web tool where a user sketches a level layout on a drawing pad and gives a theme, then DALL-E 3 generates textures and sprites that are applied to a playable game level while generation continues in the background.
**Problem / user:** Aspiring game developers who find game creation intimidating because it needs many tools and CS background; wants a gentle way to get started.

**Features**
- Level drawing pad — Built-in canvas where the user sketches the layout of the level. *[claimed]*
- Theme input — User enters a theme that the generated level and art are built around. *[claimed]*
- DALL-E 3 texture and sprite generation — Server-side prompt-to-image calls produce textures and sprites from the theme. *[claimed]*
- Playable game from the sketch — Layout, generated textures, a pre-built game engine and controls are combined into a playable level. *[claimed]*
- Asynchronous texture loading — Separately hosted back end with a REST endpoint lets play start while images are still generating. *[claimed]*

**Flow:** Draw the level layout on the pad → Enter a theme → Back end turns drawing and theme into a level and requests DALL-E 3 textures → Play the level while textures arrive

**Prompt:** Wolfram Award at HackUMass XII: no description text on the prize list; prize is a year of Wolfram One Professional Edition.
**Fit (none):** Neither page nor README mentions Wolfram technology; no stated connection to the prize.  *(targeted: Wolfram Award)*
**AI:** OpenAI DALL-E 3 generates textures and sprites from theme-based prompts server-side; team mentions prompt engineering for texture creation. No other models described.
**Architecture:** Next.js/React front end with drawing pad and game renderer; a separately hosted server exposes a REST endpoint that calls the OpenAI image API asynchronously.
**Novelty:** Combines a hand-drawn layout with AI-generated art in a ready game engine, so the output is a playable level rather than just images.
**Scope:** small · working: Live demo domain and repo listed; about 1,000 lines of code; README is default create-next-app text. · polish: No video or screenshots described; no tests; boilerplate README.
**Claims:** Says it solved the separate-server setup so async image calls do not block gameplay.
**Gaps:** Live demo not opened; README is boilerplate; Next steps: custom enemies/obstacles, teleporters
Sources: https://devpost.com/software/gameify, https://github.com/waiwasabi/game2024 (evidence file README), https://hackumass-xii.devpost.com/

---

### onedef
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [MLH] Best .Tech Domain Name

**What it is:** A library and binary protocol that lets JavaScript call Python functions as if imported, over UNIX sockets. Demo site on AWS EC2 via Terraform lets a browser talk to a local LLM running in Python.
**Problem / user:** Developers wanting Python speed or ML libraries from JavaScript (and the reverse) with low overhead.

**Features**
- Cross-language function calls — Decorate Python functions and loadPY("file.py") from Node to call them locally *[claimed]*
- Custom binary IPC spec — Encodes types and arrays instead of JSON; server sends function manifest on handshake *[claimed]*
- Bidirectional roles — Either language can act as client or server *[claimed]*
- Demo site on EC2 — Express site at onedef.tech provisioned with Terraform *[claimed]*
- C and Rust support — Future language implementations *[planned]*

**Flow:** Write decorated Python functions → Load them from JavaScript → Client opens socket and receives manifest → Calls and results are exchanged as binary packets → Use the demo site with local LLM

**Prompt:** MLH Best .Tech Domain Name: win a .Tech domain for the project.
**Fit (implied):** Project hosted at onedef.tech; Terraform used for deployment.  *(targeted: [MLH] Best .Tech Domain Name)*
**Sponsor tools:** .Tech domain (Demo site address onedef.tech, token); Terraform / AWS (Provisioning EC2 host, supporting)
**AI:** Demo runs a local LLM in Python; not a core component.
**Architecture:** Node.js and Python implementations of one socket protocol (handshake, manifest, encoded call packets); Express site on EC2.
**Novelty:** Developer infrastructure project: a language-agnostic IPC spec built from scratch rather than an app.
**Scope:** small · working: ~1.5k LOC with Python, JS and C folders and tests; demo site claimed. · polish: Minimal README; separate project website.
**Claims:** Binary encoding avoids sending JSON | Pure Node and Python with no IPC framework
**Gaps:** No benchmarks
Sources: https://devpost.com/software/unicall, https://github.com/PianoPanda/HackUMASSXII

---

### Piano Rotation Analyzer
*HackUMass HackUMass XII · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Novel Hack

**What it is:** A Python script that reads fingered piano sheet music in MusicXML and, for each consecutive set of notes, reports the hand-rotation movement needed (single or double, left or right) based on a chart drawn from Taubman biomechanics research.
**Problem / user:** Pianists wanting to improve technique: right notes are not enough, forearm rotation shapes control and expression. User is implied, not named.

**Features**
- MusicXML fingering extraction — Uses Music21 to iterate through a fully fingered score and pull out the fingerings. *[claimed]*
- Previous-direction report — For each pair of consecutive fingerings, states the direction (right or left) the hand was already rotating. *[claimed]*
- Rotation classification — Matches each consecutive triple of notes against a chart of rotational motions to label single or double rotation. *[claimed]*
- New-direction report — Outputs the direction the hand will move after the rotation. *[claimed]*

**Flow:** Supply a fingered MusicXML file → Script parses fingerings with Music21 → Each note triple is matched to the rotation chart → Output lists previous direction, rotation type, new direction

**Prompt:** Best Novel Hack (event-run): "How is your project at being comfy, creative, or entertaining?" Prize was a Pac-Man mini game.
**Fit (implied):** Page does not name the prize; the idea is novel because it applies a piano-pedagogy biomechanics chart algorithmically to sheet music. Link inferred.  *(targeted: Best Novel Hack)*
**AI:** none
**Architecture:** Single Python script: Music21 parses MusicXML, an algorithm walks note triples and looks up an array-of-dictionaries rotation chart.
**Novelty:** Unusual domain: automates piano technique analysis using Taubman-style forearm rotation rules; no AI or sponsor tech involved.
**Scope:** tiny · working: Described algorithm and output fields only; no repo, demo, or screenshots linked. · polish: Single script; planned web upload app with looping demo videos not built.
**Gaps:** No repo or demo linked; No challenges section on page; Output format only described, not shown
Sources: https://devpost.com/software/piano-technique-analyzer, https://hackumass-xii.devpost.com/

---

### qSound
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Nord Security Add-On

**What it is:** A Python program that captures live audio, turns frequency, amplitude and phase into rotations on 12 simulated qubits via Qiskit, and renders the quantum state as waves and particles in OpenGL. A small PyTorch network scores musical intensity to change the visuals.
**Problem / user:** No problem framed; an experimental audiovisual piece for people curious about sound and quantum mechanics.

**Features**
- Live audio capture — PyAudio reads the device output (virtual device such as BlackHole) with selectable input; samples frequency, amplitude, phase every 16 ms over a 2 s window. *[claimed]*
- Sound to qubit mapping — Amplitude sets rotation strength, frequency sets oscillation rate, phase shifts orientation; qubit groups in plus/minus, 0/1 and Y-basis states, entangled across groups. *[claimed]*
- Neural intensity score — PyTorch model trained on about 60 song samples outputs -1.0 to 1.0 intensity from the buffer. *[claimed]*
- 3D quantum wave rendering — OpenGL draws the transformed state as a wave, computed on a separate thread. *[shown_working]*
- Intensity-driven particles — Particle color, speed, spread follow intensity: warm and fast when intense, cool and slow when soft. *[claimed]*
- Custom FFT feature extraction — Hand-built FFT features because existing libraries were too slow for real-time. *[claimed]*

**Flow:** Install dependencies and a virtual audio device → Run the main script → Play music → View waves and particles reacting; optionally project on a screen

**Prompt:** Nord Security Add-On: Devpost prize list gives no description or prize text.
**Fit (none):** Neither the page nor README mentions security; no stated link to the add-on.  *(targeted: Nord Security Add-On)*
**AI:** Small PyTorch neural network trained on a custom 60-sample music dataset classifies intensity on a -1 to 1 scale; librosa/FFT features feed it.
**Architecture:** Three threaded Python modules: audio_processing_pyaudio (features), quantum_process (Qiskit circuits), finalscript (coordinates threads and OpenGL rendering).
**Novelty:** Unusual pairing of quantum circuit simulation with real-time music visualization; README calls it deliberately overcomplicated.
**Scope:** small · working: About 1,600 lines of Python, NN training files, and one example wave image on the page. · polish: README is clear on structure and mapping; no tests, no demo video or live link.
**Claims:** Built a working algorithm in 36 hours. | Says its custom intensity model outperformed public datasets, no metrics given.
**Gaps:** No demo or video; Page says 12 qubits, README says six groups of registers
Sources: https://devpost.com/software/q-sound, https://github.com/odepoint/qSound (evidence file README), https://hackumass-xii.devpost.com/

---

### RealityPaint
*HackUMass HackUMass XII · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Third Prize [3rd]

**What it is:** Projection-mapping setup using a projector and a Kinect depth sensor so digital graphics land on physical surfaces and avoid objects. DALL-E 3 can generate images to project.
**Problem / user:** Artists and presenters who want to turn real surfaces into digital canvases; no stated pain point.

**Features**
- Projection mapping onto surfaces — Projector shows graphics on irregular real surfaces *[claimed]*
- Depth-based object masking — Kinect depth data and OpenCV mask objects so projection skips them *[claimed]*
- DALL-E 3 image generation — Generated images are projected *[claimed]*
- Drawing mode and object labeling — Planned interaction features *[planned]*

**Flow:** Set up projector and Kinect → Run Python wrapper → Project generated or stored graphics → Masking avoids objects in view

**Prompt:** HackUMass XII Third Prize: general overall prize, items only with no description.
**Fit (none):** General prize; no sponsor prompt.  *(targeted: Third Prize)*
**AI:** DALL-E 3 for image generation; classical computer vision with depth data for masking.
**Architecture:** Kinect with patched Python wrapper feeds OpenCV masking; output rendered to projector.
**Novelty:** Physical hardware and computer-vision build; switched from webcam to Kinect overnight.
**Scope:** small · working: ~1k LOC; team admits it works imperfectly; no video. · polish: Short README with setup steps; images folder.
**Gaps:** No demo footage
Sources: https://devpost.com/software/realitypaint, https://github.com/beaverbois/RealityPaint

---

### SafeSteps
*HackUMass HackUMass XII · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best UMass-Related Hack

**What it is:** A Flutter mobile app for UMass students that maps the campus HELP emergency phones, gives directions to the nearest one, shares live location with trusted contacts, and offers a one-tap emergency call and safer-route suggestions.
**Problem / user:** UMass students walking campus at night; HELP phones exist but are hard to find quickly and there was no easy way to share location with friends or security.

**Features**
- HELP phone map and directions — Custom markers on a campus Google map; one tap gives directions to the nearest phone using geolocation. *[shown_working]*
- Live location sharing / virtual escort — Share location with friends or family via Firebase; request a campus security escort by call. *[claimed]*
- Check-in notifications — README: periodic check-ins that alert a contact or campus safety if missed. *[claimed]*
- One-tap emergency call — Dedicated button launches a call to UMPD or 911 sharing GPS location. *[claimed]*
- Safe route planner — Suggests paths favoring well-lit areas and routes passing HELP phones. *[claimed]*
- Proximity alerts and push notifications — Alerts when a nearby HELP phone is activated; security can push incident notices. *[claimed]*
- Night mode and offline cache — Dark theme for night use; cached maps and phone locations for weak signal. *[claimed]*

**Flow:** Log in with Firebase auth → See map with HELP phone markers → Tap for directions to nearest phone or pick a destination → Share location or request escort → Press emergency button if needed

**Prompt:** Best UMass-Related Hack: "Does your project help UMass students, and add to our campus?" Prize: iFixit driver kit.
**Fit (explicit):** Built around UMass campus HELP phones and UMPD/security; README states it won the Best UMass Hack category. Targets campus student safety directly.  *(targeted: Best UMass-Related Hack)*
**AI:** none
**Architecture:** Flutter/Dart client with GetX state management; Firebase Auth and Firestore for users and live location; Google Maps, Directions and Places APIs; URL launcher for calls.
**Novelty:** Campus-specific safety companion centered on the existing HELP phone infrastructure, with escort request to campus security; offline mode and some alerts appear in README but not on the page.
**Scope:** medium · working: About 5,100 LOC across 170 files, Android/iOS targets, four screenshots; claims deployment on both platforms. · polish: Detailed README feature list; no video or live demo; one test file; installation section incomplete.
**Claims:** Deployed on Android and iOS in under 32 hours (page). | Mapped all UMass HELP phones with accurate coordinates. | Routes pass HELP phones without much extra travel time (no data).
**Gaps:** README lists offline mode, check-ins and alerts that the page lists as future or omits; Hours claim differs (36 in README, under 32 on page)
Sources: https://devpost.com/software/safesteps-62k5zb, https://github.com/adhirajj/safesteps (evidence file README), https://hackumass-xii.devpost.com/

---

### SpeedPUB
*HackUMass HackUMass XII · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Grand Prize [1st]

**What it is:** Python tool that rewrites EPUB books so words are coloured by part of speech, with optional bolding for speed reading. Works for English and Chinese and has a tkinter GUI.
**Problem / user:** Avid readers and language learners who want faster, deeper reading.

**Features**
- Part-of-speech colouring — NLTK (English) and HanLP (Chinese) tag words; XHTML is rewritten with colour spans *[shown_working]*
- Partial-word bolding — Bolds portions of words for speed-reading *[shown_working]*
- EPUB round trip — EbookLib reads, BeautifulSoup edits XHTML, repackaged as EPUB *[shown_working]*
- Tkinter GUI with colour customization — Create highlighted EPUBs and choose colours *[shown_working]*
- eReader app and more languages — Future work *[planned]*

**Flow:** Launch gooey.py GUI → Choose an EPUB and colours → Process it → Open the output in an ereader

**Prompt:** HackUMass XII Grand Prize: overall top prize, items only with no description.
**Fit (none):** General overall prize; no sponsor prompt.  *(targeted: Grand Prize)*
**AI:** Pretrained NLP models for POS tagging via NLTK and HanLP.
**Architecture:** Python pipeline: EbookLib, BeautifulSoup, POS tagger, repackage; tkinter front end.
**Novelty:** Applies syntax highlighting to prose including Chinese; output is a standard EPUB.
**Scope:** small · working: Pipeline described with gallery screenshots; ~600 LOC. · polish: Marketing folder with images and clear README.
**Claims:** Improves reading speed and comprehension (no measurements)
**Gaps:** No user testing
Sources: https://devpost.com/software/untitled-project-03byqsepgkdf, https://github.com/theokrueger/speedpub

---

### StoryBytes
*HackUMass HackUMass XII · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Use of GenAI

**What it is:** A React and Node web app that turns a short description into an illustrated, narrated short story or poem, shown as a paged book with clickable word definitions and a saved-story menu. Run modes trade cost for image and voice quality.
**Problem / user:** Children who want to see their ideas become stories, plus parents, early readers, language learners and writers seeking inspiration.

**Features**
- Story generation by genre, theme and difficulty — OpenAI chat completions write a story from the description at a chosen reading level. *[shown_working]*
- Poem mode — Option to produce rhyming, poem-like output. *[shown_working]*
- AI illustrations per page — getimg.ai images, or Black Forest Labs Flux 1.1 Pro in costlier modes. *[shown_working]*
- Text-to-speech narration — ElevenLabs voices, or a free gTTS fallback in cheaper modes. *[claimed]*
- Click-for-definition vocabulary — Free Dictionary API gives definition and part of speech for a clicked word. *[shown_working]*
- Story library and keyboard controls — Menu bar saves several stories; Enter, arrows and Space navigate and play. *[shown_working]*
- Multilingual queries — Queries and narration in other languages; screenshot shown. *[shown_working]*
- Four cost-based run modes — Free, cheap, expensive, super expensive mixes of text, image and voice providers. *[claimed]*

**Flow:** Type a story description → Choose reading difficulty and optionally poem mode → Watch page-flipping loading screen → Read the illustrated book with narration → Click words for definitions or save to library

**Prompt:** Best Use of GenAI: "If you used any generative AI (Text, Image, Video, Audio), you should be applying for this category." Prize: four drones.
**Fit (implied):** Chains text, image and audio generation into one product: LLM story, image model illustrations, TTS narration, with multi-step prompting and cost-aware modes.  *(targeted: Best Use of GenAI)*
**Sponsor tools:** ElevenLabs (Human-like narration in the cheap and super-expensive modes, supporting)
**AI:** GPT-4o chat completions write stories; getimg.ai or Flux 1.1 Pro generate page illustrations; ElevenLabs or gTTS narrate. Multi-step prompting for text, images and audio; DALL-E 3 was dropped due to access.
**Architecture:** React/TypeScript frontend calls an Express backend that orchestrates OpenAI, image APIs, ElevenLabs/gTTS and the dictionary API, and serves generated files from disk; run mode chosen at server start.
**Novelty:** Three-modality generation pipeline with explicit price tiers and a file-serving cache to cut API calls; also multilingual and dictionary-linked.
**Scope:** medium · working: About 2,600 LOC, frontend and backend, eight screenshots of working pages; no live demo. · polish: Loading animation, custom logo, saved library, keyboard shortcuts; README gives quickstart and run modes.
**Claims:** Resource-conscious backend adjusts to usage mode to control cost. | File serving speeds loading and reduces external API reliance.
**Gaps:** No demo or video; Page names ChatGPT 4o; README says Completions
Sources: https://devpost.com/software/storybytes, https://github.com/Citrus216/storybytes (evidence file README), https://hackumass-xii.devpost.com/

---

### The Miraculous Bits and Bytes Fuzzer
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Nord Security Add-On

**What it is:** A Go command-line fuzzer that mutates the bytes of an input file, runs a target program on the mutated file, and records the byte position and error output when the program crashes. A defensive testing tool for developers.
**Problem / user:** Developers of all levels who are unaware of vulnerabilities in their programs or lack an efficient way to locate them.

**Features**
- Byte-level file mutation — Alters bytes of an input file to create varied test inputs. *[claimed]*
- Run target on mutated input — Feeds the mutated file to a program that processes files. *[claimed]*
- Crash detection and logging — Detects unexpected crashes and writes crash byte position and error output to a separate file. *[claimed]*
- Input generators — Two input generators were implemented. *[claimed]*

**Flow:** Point fuzzer at a target program and input file (paths hardcoded in code) → Fuzzer mutates the file → Target runs on the mutated file → Crash byte and error written to a log file

**Prompt:** Nord Security Add-On: the Devpost prize list gives no description or prize text.
**Fit (implied):** Security-testing purpose (finding crash-causing inputs to improve software safety) fits a security-sponsored add-on; page does not name the prize. Link inferred.  *(targeted: Nord Security Add-On)*
**AI:** none
**Architecture:** Go program using standard file libraries: mutate input bytes, execute the target, watch for crashes, write results to a log file.
**Novelty:** A from-scratch byte-mutation fuzzer built by mostly first-time Go and fuzzing users; limited to file inputs and not concurrent.
**Scope:** tiny · working: Page says it was verified on public GitHub projects; no results, screenshots or demo shown. · polish: Self-listed limits: hardcoded paths, files only, no concurrency, no vulnerability classification.
**Claims:** Verified against public GitHub projects (no counts reported).
**Gaps:** Evidence clone failed; README on raw.githubusercontent returned 404 for HEAD/main/master/final; Repo link is a branch (tree/final); Nord prize has no public text
Sources: https://devpost.com/software/a-miraculous-fuzzer, https://hackumass-xii.devpost.com/

---

### The Wave
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [MLH] Best Use of MongoDB Atlas

**What it is:** Native iOS app showing a live map of nearby social activity such as pop-ups, bar shows and gatherings, with anonymous browsing. Flask API handles proximity search and MongoDB stores events.
**Problem / user:** People who miss spontaneous local events due to no central source.

**Features**
- Live map of nearby activity — Apple Maps view centered on user with events and venues *[claimed]*
- Proximity search — Flask backend queries events by location *[claimed]*
- Anonymous discovery — Browse without identity *[claimed]*
- Custom map styling — Camera angles and night mode *[claimed]*

**Flow:** Open app → See live map near you → Explore events and venues

**Prompt:** MLH Best Use of MongoDB Atlas: build a hack using MongoDB Atlas.
**Fit (explicit):** MongoDB stores user and event data behind the Flask API.  *(targeted: [MLH] Best Use of MongoDB Atlas)*
**Sponsor tools:** MongoDB Atlas (User and event storage, core)
**AI:** none
**Architecture:** SwiftUI app to Flask API to MongoDB; Terraform-provisioned cloud.
**Novelty:** Native SwiftUI rather than cross-platform; map of real-time local happenings.
**Scope:** small · working: Live site waveapp.tech and functional prototype claimed; no repo or video. · polish: Unclear; no screenshots read.
**Gaps:** No repo; What data fills the map unstated
Sources: https://devpost.com/software/the-wave-v21rau, https://hackumass-xii.devpost.com/

---

### Tomo
*HackUMass HackUMass XII · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Second Prize [2nd]

**What it is:** Space Invaders clone in Pygame where ChatGPT writes new gameplay code each level, adding mechanics, obstacles and boss fights. Main branch is controlled by Leap Motion hand tracking.
**Problem / user:** Retro arcade players; goal is infinite replayability and a hobby-meets-AI experiment.

**Features**
- LLM-generated mechanics per round — OpenAI API with a master prompt returns Python code that is executed to alter gameplay *[claimed]*
- Power-ups and obstacles — Shields, portals and black holes *[claimed]*
- Boss fights — Periodic bosses *[claimed]*
- Leap Motion control — C++ script maps hand gestures to keyboard input *[claimed]*

**Flow:** Start the game → Play a standard round → Next round runs AI-generated rules → Control by hand or keyboard

**Prompt:** HackUMass XII Second Prize: general prize, items only.
**Fit (none):** General prize; no sponsor prompt.  *(targeted: Second Prize)*
**AI:** ChatGPT given game state and master prompt generates executable Python mechanics each level.
**Architecture:** Pygame game; llm folder calls OpenAI and executes returned code; Leap Motion C++ bridge.
**Novelty:** Runtime LLM code generation inside a game plus gesture hardware.
**Scope:** small · working: ~2.4k LOC with leapmotion, llm and real_time folders; no video; AI code conversion was hard. · polish: Modest README.
**Claims:** No two playthroughs are the same
**Gaps:** No demo footage
Sources: https://devpost.com/software/tomo-dmajc3, https://github.com/Ben-Santana/AI-Space-Invaders

---

### VR Breadboard
*HackUMass HackUMass XII · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best AR/VR Hack

**What it is:** A Unity virtual-reality electronics simulator for Meta Quest where users place components, wires and ICs on a virtual breadboard and see circuit behavior simulated. The repo adds a natural-language circuit command generator and a 2D Pygame circuit tester.
**Problem / user:** Beginners and educators for whom physical breadboarding is intimidating and needs real components that can be damaged.

**Features**
- Interactive VR breadboard — Unity C# scripts handle placement of components and wires on a breadboard in VR. *[claimed]*
- Real-time circuit simulation — Custom algorithms analyze the built circuit and show behavior live; includes functioning IC units. *[claimed]*
- Circuit command generator — README: turns natural-language input or pictures of circuits into step-by-step commands for the simulator. *[claimed]*
- 2D circuit simulator and tester — Python/Pygame app for quickly editing and checking circuit designs; integrates with the VR tool. *[claimed]*
- Guided tutorials — README lists educational content; page lists tutorials as future. *[planned]*

**Flow:** Wear a Meta Quest headset with the Unity app → Place wires and components on the breadboard → Observe real-time circuit behavior → Optionally prototype in the 2D tool or generate commands from text

**Prompt:** Best AR/VR Hack: "We want you to beat Meta at the AR/VR Game!!" Prize: a projector.
**Fit (implied):** A full VR experience for Meta Quest built in Unity with VR interaction; the page lists Meta and XR tags. Link is implied by being a VR application.  *(targeted: Best AR/VR Hack)*
**AI:** Tags list OpenAI, RAG and vision; README says the command generator parses natural language and analyzes circuit pictures. Models and prompts are not described.
**Architecture:** Unity/C# VR app (Quest 3) with in-engine circuit simulation; companion Python tools: circuitCommandGen and a Pygame 2D simulator feeding commands.
**Novelty:** VR breadboard plus an LLM/vision command generator bridging text or photos into the simulator; most tags are not explained on the page.
**Scope:** small · working: Repo has about 3,300 LOC only in the 2D tool and command generator folders; the Unity project is not visible in the evidence tree. · polish: Emoji-styled README with template placeholders; three captioned screenshots; no video.
**Claims:** Claims fully functional VR simulator with accurate real-time circuit simulation (no metrics).
**Gaps:** Unity project files not in repo tree summary; AI role only in tags and README, not shown; README has an unfilled placeholder
Sources: https://devpost.com/software/circuit-simulator, https://github.com/Parth12358/Circuit-Simulator-Kit (evidence file README), https://hackumass-xii.devpost.com/

---

### WorldWide Rover
*HackUMass HackUMass XII · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Embedded System

**What it is:** A small wheeled rover driven by an Arduino and a Raspberry Pi that anyone can steer from a React web page over the internet. Commands go through a Flask server to the Pi, then over serial to the Arduino motor driver.
**Problem / user:** Learners, educators and researchers wanting hands-on, globally accessible remote robotics, inspired by remote Mars rover operation.

**Features**
- Web remote control — React page sends forward, backward, left, right and stop to a Flask /move endpoint. *[claimed]*
- Command interruption and immediate stop — A new direction stops the current action, waits about a second; stop is sent at once. *[claimed]*
- Repeated command sending — Server resends the movement command about once per second until a new command arrives. *[claimed]*
- Pi to Arduino serial control — Pi sends commands over UART/USB at 9600 baud; Arduino sets motor driver pins to move four DC motors. *[claimed]*
- Public access via ngrok — Tunnel exposes the control server for anyone with the link; AWS also listed for hosting. *[claimed]*
- Autonomous maze and obstacle avoidance — Page claims it; avoidance method not explained; sensor folder exists in repo. *[unclear]*

**Flow:** Open the shared web link → Press a direction or stop → Flask validates and queues the command → Raspberry Pi relays via serial to Arduino → Rover motors move

**Prompt:** Best Embedded System: "Projects that combine hardware and software through leveraging embedded computers." Prize: Fire TV Stick.
**Fit (implied):** Combines an Arduino and a Raspberry Pi with motors and a web stack; the Pi acts as the embedded server bridging network commands to hardware.  *(targeted: Best Embedded System)*
**AI:** none
**Architecture:** React front end to Flask server on a Raspberry Pi (ngrok tunnel), serial link to an Arduino Uno driving a motor module and four DC motors, powered by battery.
**Novelty:** Internet-reachable rover with simple command-interrupt logic; autonomous features are claimed but small in the repo.
**Scope:** small · working: README describes parts and run steps; about 400 LOC of Arduino and Python; three screenshots, no video. · polish: Plain-text README; backup-code folder; no tests or live link.
**Claims:** Working prototype demonstrating autonomous navigation and remote operation (no measurements).
**Gaps:** No latency or autonomy evidence; Page and README differ on autonomy: README lists only manual commands
Sources: https://devpost.com/software/worldwide-rover, https://github.com/Manujake/HackUMass2024 (evidence file README), https://hackumass-xii.devpost.com/

---

