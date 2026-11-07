# TreeHacks — TreeHacks 2025 (17 projects)

### BAS Buddy (Climate Action Matcher)
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Sustainability Prize: Best prototyping process ($800 Cash); Winner Intersystems: Best Use of GenAI using InterSystems IRIS Vector Search ($2k 1st / $1.5k 2nd / $1k 3rd)

**What it is:** An agentic assistant, built with Race to Zero, that takes a company, finds peer companies, retrieves their real climate actions from a vector database of sustainability reports, and matches the company to UN-catalogued cooperative climate initiatives, with source links.
**Problem / user:** Companies that struggle to find concrete carbon-cutting actions that also fit business goals, and want inspiration from peers and relevant UN initiatives.

**Features**
- Company-to-initiative matching — Matches the user's company to UN-catalogued cooperative climate initiatives; 172 initiatives are embedded with descriptions. *[shown_working]*
- RAG over sustainability reports — Over 17,000 paragraphs from scraped reports are chunked with LangChain and embedded with NVIDIA nv-embedqa into InterSystems IRIS for vector search. *[shown_working]*
- Similar-company discovery — Gemini classifies the company's sector, and a tool finds peers by sector and country. *[claimed]*
- Brainstorm-then-verify retrieval — Agent brainstorms initiatives the company could pursue, then checks them against actual actions found in reports to work around vague report text. *[claimed]*
- Action scoring and ranking — Gemini scores corporate actions for reproducibility and ROI, ranks them and ties them to initiatives. *[claimed]*
- Web scraping tools — Selenium scrapes zerotracker.net and nzdpu.com; a Scrapybara agent finds deep PDF links on company sites. *[claimed]*
- Source-linked, formatted answers — DAIN Butterfly orchestrates tools and renders results with DAIN UI components, including links for verification. *[shown_working]*
- Knowledge graph and reporting dashboard — Planned dynamic graph of action impacts, extra scoring dimensions and a standardized reporting dashboard. *[planned]*

**Flow:** User gives their company → Agent classifies sector and finds similar companies → Agent brainstorms candidate initiatives → Agent verifies them with real actions from report database and scrapers → Gemini scores and ranks actions and matches to initiatives → Formatted response with source links is returned

**Prompt:** Sustainability Best Prototyping Process: reward multiple iterations with user feedback, clear hypotheses per prototype, and quickest or cheapest tests. InterSystems prize: innovative GenAI built on IRIS (vector search, AutoML, interoperability, SQL, LangChain connectors).
**Fit (implied):** Uses IRIS as the embedding database for initiatives and report paragraphs, directly on the InterSystems prompt. The page says nothing about iteration or user feedback, so the sustainability fit is not documented.  *(targeted: Sustainability Prize: Best prototyping process, InterSystems: Best Use of GenAI using IRIS Vector Search)*
**Sponsor tools:** InterSystems IRIS vector database (Embedding store for 172 initiatives and 17k report paragraphs, core); DAIN Butterfly (Agent orchestration and UI components, core); NVIDIA nv-embedqa embedding model (Embeddings for documents and queries, supporting); Scrapybara (Agent that finds PDF links, supporting)
**AI:** Tool-using agent: Gemini Flash 2.0 classifies sectors and scores actions; retrieval over IRIS vectors; a brainstorm-then-verify pattern; prompt engineering and clearer tool descriptions to make the agent use all tools.
**Architecture:** DAIN Butterfly agent calls custom tools (sector classifier, peer finder, initiative matcher, report search on IRIS, Selenium and Scrapybara scrapers); results rendered via DAIN UI.
**Novelty:** Corporate-climate peer benchmarking via a purpose-built embedding database of reports and UN initiatives; team plans to open-source the database.
**Scope:** small · working: Demo video on Devpost; README repeats Devpost text; repo code is small (about 2.5k LOC) but folder holds data. · polish: Screenshot, video with transcript, structured writeup; no live URL.
**Claims:** 172 UN initiatives embedded | Over 17,000 report paragraphs embedded | Hundreds of sustainability reports in the database
**Gaps:** Devpost does not say which InterSystems place was won; Video not watched; Working status of scoring and scrapers is from text only
Sources: https://devpost.com/software/bas-climate-action-matcher, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-bas-climate-action-matcher.json (README)

---

### BlinkAI
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Winner Best Beginner Hack (Keychron K8 Pro keyboard per team member)

**What it is:** A webcam-based accessibility prototype that treats deliberate eye blinks as Morse code, decodes them into text and forwards the text to an AI assistant, then returns the reply.
**Problem / user:** People with Parkinson's, ALS or other mobility limits who cannot use voice or keyboard to reach digital assistants.

**Features**
- Intentional blink detection — Camera tracking (OpenCV and MediaPipe/cvzone per manifests) filters out natural blinking and measures blink duration and frequency. *[claimed]*
- Blinks to Morse — Short and long blinks are classified as dots and dashes by timing thresholds. *[claimed]*
- Morse decoding to text — The dot-dash sequence is decoded into readable text. *[claimed]*
- AI assistant query and reply — Decoded text is sent to an unnamed external AI model as ordinary input and the answer is shown to the user. *[claimed]*
- Web interface — Flask with Socket.IO and a static/template front end in the repo. *[unclear]*
- Per-user adaptation and more assistants — Listed as next steps. *[planned]*

**Flow:** User sits in front of the webcam → Deliberate blinks are separated from natural ones → Blinks become dots and dashes then text → Text goes to an AI assistant → The response is returned to the user

**Prompt:** Best Beginner Hack: for teams with limited coding or hackathon experience, rewarding creativity, effort and progress at a first hackathon.
**Fit (none):** Page does not say whether the team were beginners; the connection is limited to the prize being won, with an accessibility-themed, small working prototype.  *(targeted: Best Beginner Hack)*
**AI:** Computer vision for blink detection (OpenCV, MediaPipe) and an unspecified external LLM assistant for answers; no training described.
**Architecture:** Python Flask server with Socket.IO reading webcam via OpenCV, Morse decoder, relay to an AI model, results displayed in a small web front end.
**Novelty:** Uses Morse-coded blinks as an input channel to a general AI assistant, rather than a fixed menu or communication board.
**Scope:** tiny · working: Six-file repo, about 1.4k LOC, no tests; Devpost calls it a functioning prototype with no metrics. · polish: Minimal: empty README, no screenshots, no video.
**Claims:** Fully functional prototype translating blinks to AI communication | Among one of the first Morse-code blink detection systems | Filters natural blinks to avoid false inputs
**Gaps:** Repo README is empty so implementation detail is inferred from requirements; Which AI assistant is used is not stated; No demo, video or accuracy figures
Sources: https://devpost.com/software/blinkai, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-blinkai.json (empty README, manifests)

---

### BrailleBot
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Best Hardware Hack

**What it is:** A braille printer made by mounting a 3D-printed, spring-loaded embossing head on a cheap 3D printer. AI transcribes documents, describes images and summarizes Zoom lectures, and a Flask backend converts the text to braille G-code sent over USB.
**Problem / user:** Teachers and students, especially in low-income settings, and deafblind readers who need physical braille when dedicated printers cost around $1,500.

**Features**
- Spring-loaded embossing head — Snap-action mechanism turns a quarter rotation of the printer's extruder motor into a fast punch; screw sets spring compression for depth; cork sheet used as impact material. *[shown_working]*
- Document to braille G-code — Flask backend converts transcribed ASCII text to braille cells and Marlin G-code, sent to the printer via USB serial. *[shown_working]*
- Multi-format ingestion — Handles PDFs, Word files and scanned images through OCR and transcription with Llama models on Groq. *[claimed]*
- AI image descriptions — Llama vision model writes text descriptions of images so they print as braille. *[claimed]*
- Zoom lecture summaries — Pulls transcripts through the Zoom API and summarizes them for printing. *[claimed]*
- Live print preview — JS canvas in the Next.js front end shows the print in real time. *[shown_working]*
- Punch rate — Stock extruder gives up to ten punches per second. *[claimed]*

**Flow:** User uploads a document or picks a Zoom lecture → AI transcribes it and describes images → Backend converts text to braille and G-code → Canvas preview shows the layout → G-code streams over USB and the modified printer embosses the page

**Prompt:** Best Hardware Hack: strong hardware integration, such as IoT, robotics or physical computing producing interactive solutions.
**Fit (explicit):** README states it won Best Hardware Hack; the mechanical add-on to an off-the-shelf printer plus firmware-level G-code control is the hardware integration. Explicit mention of the win, not of the criteria.  *(targeted: Best Hardware Hack)*
**Sponsor tools:** Groq inference (Llama 3 8B and vision) (Transcription, image descriptions and summaries, core); Zoom API (Lecture transcripts, supporting)
**AI:** Llama3-8B and Llama vision on Groq for fast transcription, image descriptions and lecture summaries; braille translation itself is rule-based in the backend.
**Architecture:** Next.js/Chakra front end with canvas preview talks to Python Flask backend that calls Groq and Zoom, converts text to braille and Marlin G-code, and streams it to the 3D printer over USB serial.
**Novelty:** Retrofits a sub-$15 printed punch onto any commodity 3D printer instead of building a dedicated embosser, roughly 100x cheaper than the stated market price.
**Scope:** small · working: Working embossing hardware iterated over punch heads and materials; repo about 2.8k LOC without tests; no quantitative accuracy figures. · polish: README with intro video link, design details and clear cost claim; live preview UI.
**Claims:** Embossing mechanism costs under $15 | Almost 100x cheaper than the roughly $1,500 cheapest braille printers | Up to 10 punches per second | Only about 3 percent of the internet is accessible to visually impaired users
**Gaps:** Video not watched; No setup instructions in README; No accuracy numbers
Sources: https://devpost.com/software/readable-ai-braille-printer, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-braillebot-make-every-document-accessible.json (README)

---

### ECGO
*TreeHacks TreeHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Web3 Prize: Most Crazy Idea ($7k Cash + 7k EIGEN)

**What it is:** A battery-powered handheld ECG built around an ESP32 and AD8232 front end. It records three seconds of heartbeat, uploads it to InfluxDB, a server-side CNN-Transformer returns an arrhythmia diagnosis to the device, and a Streamlit app shows data by sample ID.
**Problem / user:** People in developing regions and crisis areas where ECG machines and the clinicians to read them are costly or missing.

**Features**
- Three-second ECG capture — AD8232 electrodes feed the ESP32 ADC; firmware in C; powered by AA batteries. *[shown_working]*
- Wi-Fi upload to InfluxDB — Device posts each sample over HTTP to a remote InfluxDB instance and gets a random ID from 0 to 10000. *[shown_working]*
- AI arrhythmia diagnosis — Server polls the database, runs a PyTorch CNN-Transformer pretrained on open ECG data, writes the result back for the device to read. *[shown_working]*
- On-device waveform display — Two 0.96 inch OLEDs over I2C (one address clash fixed by moving a resistor) show the trace; joystick pans and zooms. *[shown_working]*
- Streamlit lookup app — User enters the sample ID to see stored data queried from the database. *[shown_working]*
- AI agent for medical suggestions — Planned for the Web3 track but dropped as too hard in the time. *[planned]*

**Flow:** Attach electrodes and power the device → Take a three-second sample → ESP32 uploads it over Wi-Fi → Server model diagnoses and writes the result → Device shows diagnosis and a sample ID → User later enters the ID in the web app

**Prompt:** Web3 Most Crazy Idea (EigenLayer): rewards boldness and creativity, especially unexpected AI use that redefines how on-chain and off-chain systems interact; $7k plus 7k EIGEN.
**Fit (none):** README says it won this prize. Neither page shows blockchain use; Devpost says the planned agent integration was dropped. Fit rests on the unusual pocket ECG with AI diagnosis idea.  *(targeted: Web3 Prize: Most Crazy Idea)*
**AI:** Pretrained CNN-Transformer (PyTorch, informed by a published transformer arrhythmia paper) classifies 3 s ECG samples server-side; tested only qualitatively on noisy and regular signals.
**Architecture:** ESP32 firmware reads ECG, sends HTTP to InfluxDB; a Python model server watches for new series and writes diagnoses back; device reads the result; Streamlit queries InfluxDB.
**Novelty:** Full loop from custom-soldered ECG PCB to cloud AI diagnosis and back to the device screen, built by two people; deliberately no AI agent or chain despite the prize.
**Scope:** small · working: Repo about 2.1k LOC with firmware and model code, no tests; Devpost calls the pipeline reliable but gives no accuracy numbers. · polish: Soldered final PCB and dual-OLED UI; README is minimal (paper credit); demo video mentioned but not linked.
**Claims:** Complete device to database to model to device pipeline works reliably | Model gave positive diagnosis on very noisy signals and negative on a regular heartbeat | Moved from prototype to final soldered PCB without major issues
**Gaps:** README has almost no content; Demo video referenced but no link; No accuracy figures; blockchain role absent
Sources: https://devpost.com/software/ecgo, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-ecgo.json (README, credit-only)

---

### Edith
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Winner Most Technically Complex Hack

**What it is:** Raspberry Pi Zero 2W smart glasses with camera, IMU, haptic motors and LEDs. Video streams to a four-A100 server for depth, segmentation and point clouds, and Gemini uses the results to tell where a requested object is while vibration guides the wearer toward it.
**Problem / user:** Blind and visually impaired people who need to find objects and move safely and independently.

**Features**
- Any-object 3D segmentation — GPU server runs segmentation, depth and point-cloud models on the camera stream, intended to generalize beyond COCO classes; models not named. *[claimed]*
- Object location via Gemini — Gemini live multimodal prompting gets the object's heading and depth to place it relative to the user. *[claimed]*
- Haptic direction guidance — Vibration motors grow or fade in intensity as the wearer turns toward or away from the target. *[claimed]*
- Fall detection — IMU yaw, pitch and roll with a complementary filter detect falls. *[claimed]*
- Night LED strip — Onboard LEDs illuminate surroundings in the dark. *[claimed]*
- Camera stream forwarding — Pi forwards video to other devices and the A100 server via file/video transfer and simple HTTPS routes. *[claimed]*
- Custom hardware — 3D-printed modular frame with brass elements, perf-board PCBs, LiPo batteries and boost converters. *[claimed]*

**Flow:** Wear the glasses with camera, IMU, motors and LEDs → Camera stream goes to the GPU server for depth and segmentation → Wearer asks for an object → Gemini works out its heading and depth → Vibration intensity guides the wearer to face it → IMU watches for falls and LEDs help at night

**Prompt:** Most Technically Complex Hack: recognizes advanced technical skill and sophistication, such as algorithms, data structures or machine learning.
**Fit (implied):** Combines custom hardware, multi-GPU depth and segmentation inference, multimodal LLM and haptic control into a low-latency pipeline. Devpost names the prize as won but does not map features to criteria.  *(targeted: Most Technically Complex Hack)*
**Sponsor tools:** Gemini live multimodal API (Locating requested objects from heading and depth, core); NVIDIA A100 GPUs (Parallel depth, segmentation and point-cloud inference, core)
**AI:** Parallel inference on four A100s for depth, segmentation and point clouds with unnamed state-of-the-art models, plus Gemini live prompting that fuses heading and depth to answer where an object is.
**Architecture:** Pi Zero 2W collects camera, IMU and drives motors/LEDs; streams to A100 server over HTTPS and file transfer (an earlier websocket mesh was replaced); results and Gemini output drive haptics.
**Novelty:** Combines open-vocabulary 3D scene understanding with directional haptic feedback and fall detection on custom wearable hardware, all in 36 hours.
**Scope:** medium · working: Devpost claims near-real-time operation; no metrics, video or repo content could be read. · polish: Custom PCB and compact printed frame described; no demo link.
**Claims:** Near-real-time operation through low-latency device communication | Built compact custom PCB with makerspace resources | Whole build completed in 36 hours
**Gaps:** Repo clone failed and README raw fetch returned 404; GitHub page unreachable; Models not named; No video, metrics or next steps
Sources: https://devpost.com/software/edith-bvh014, https://treehacks-2025.devpost.com/

---

### ERWIN (Enhanced Rock Weathering Impact Navigator)
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Sustainability Prize: Best solves the user's pain point of a provided challenge ($800 Cash)

**What it is:** A map-based web tool that forecasts CO2 removal from enhanced rock weathering. Users pick a region and rock type, the app fetches soil and climate data, runs a geochemical simulation (CrunchFlow in Docker) and charts removal rate and pH with uncertainty, plus nearby quarry suggestions.
**Problem / user:** Carbon-credit investors, project planners and ERW researchers, for whom forecasts are uncertain or require PhD-level, poorly documented Fortran models.

**Features**
- Region selection on a map — Mapbox map where the user bounds a target region. *[claimed]*
- Project inputs — Rock type, project area, feedstock surface density and time series length; Basic and Advanced UI modes. *[claimed]*
- Automatic soil and climate data — Fetches SoilGrids soil composition and Open-Meteo precipitation for the region's center coordinates. *[claimed]*
- Geochemical simulation — Runs CrunchFlow in a Docker container via Flask; stoichiometry converts ion concentration and pH series to CO2 removal rates. *[claimed]*
- Uncertainty charts and total estimate — Plots removal rate per square meter and pH over years with mean and one standard deviation, then integrates for total CO2 removed. *[claimed]*
- Quantum sampling for distributions — Qiskit random sampling, said to run on IBM Quantum Cloud, generates probability distributions. *[claimed]*
- Quarry explorer — Up to 50 recommended quarries for the chosen rock within the region, from National Mine Map Repository data scraped to CSVs. *[claimed]*

**Flow:** Pick a region on the map → Set rock type, area, surface density and duration → Optionally toggle quarry suggestions → Click Run; app fetches soil and climate data and simulates → View CO2 removal and pH graphs and the total estimate

**Prompt:** Sustainability Prize, best solves the user's pain point of a provided challenge ($800): rated on how well a solution addresses a pain point from a supplied sustainability challenge, with users rating solutions.
**Fit (implied):** Targets the pain of hard-to-use ERW forecast models by wrapping them in a map UI with automatic data retrieval; Devpost names the prize but not the provided challenge, and mentions an academic collaborator for user input.  *(targeted: Sustainability Prize: Best solves the user's pain point)*
**Sponsor tools:** IBM Quantum Cloud / Qiskit (Random sampling for distributions, supporting); Mapbox (Region selection map, supporting)
**AI:** No machine learning; a mechanistic geochemical model (CrunchFlow) with quantum-derived random sampling for uncertainty.
**Architecture:** JavaScript front end with Mapbox calls Flask backend that gathers SoilGrids and Open-Meteo data, runs CrunchFlow input files in Docker, post-processes to CO2 curves; quarry CSVs served from a GitHub repo.
**Novelty:** Wraps a research-grade reactive-transport code and quantum sampling in a consumer-style map tool; team reverse-engineered undocumented model input files.
**Scope:** small · working: About 2.7k LOC repo with Docker setup; README is a to-do and run notes; no validation metrics or video. · polish: Docker packaging, Basic/Advanced modes; README unpolished; demo linked only as a Canva design.
**Claims:** Built infrastructure, UI and multi-API backend within 36 hours | Quantum sampling improves efficiency and accuracy (stated, not measured) | Science-backed forecasts should raise confidence in carbon removal projects
**Gaps:** Provided sustainability challenge text not found; Feature status is from Devpost; README only has Docker run notes; No demo video
Sources: https://devpost.com/software/erwin-enhanced-rock-weathering-impact-navigator, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-erwin-enhanced-rock-weathering-impact-navigator.json (README)

---

### HawkWatch
*TreeHacks TreeHacks 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Winner TreeHacks Grand Prize | 1st Place ($11k Cash) [1st]

**What it is:** Browser-based AI surveillance dashboard that analyzes camera livestreams or uploaded MP4s with Gemini plus TensorFlow body-pose data to detect crime or medical emergencies, alert security by email, and keep timelines and statistics.
**Problem / user:** Businesses such as grocery stores, hospitals and malls where staff cannot watch many camera feeds at once.

**Features**
- Real-time incident detection — Audio, video and TensorFlow.js pose data sent to Gemini VLM flag crime, fainting, choking *[claimed]*
- Instant alerts — Email and phone alerts through Resend *[claimed]*
- Multi-camera dashboard — Live feeds with call-security option *[claimed]*
- Upload analysis and library — MP4 uploads and saved streams with security timelines and downloadable footage *[claimed]*
- Statistics page — AI summary, charts, CSV export *[claimed]*
- Emergency assistant — OpenAI chat uses recent event context to advise e.g. on someone passed out *[claimed]*

**Flow:** Sign in and open dashboard → Connect cameras or upload MP4 → System flags incidents and alerts security → User calls security or asks assistant → Review library, timelines, stats, export

**Prompt:** TreeHacks Grand Prize 1st ($11,000): awarded for exceptional innovation, functionality and overall excellence; general criteria creativity, technical complexity, social impact.
**Fit (none):** General-purpose security product; no track targeted.  *(targeted: TreeHacks Grand Prize)*
**AI:** Gemini VLM analyzes video, audio and pose from TensorFlow.js; OpenAI model answers questions from recent event context.
**Architecture:** Next.js/TypeScript client processes streams in browser, WebSockets for live updates, Supabase auth/DB, Resend notifications.
**Novelty:** Runs pose estimation client-side and sends multimodal context to a VLM, covering medical emergencies as well as crime.
**Scope:** medium · working: Devpost claims functional system; repo not inspected (no evidence file). · polish: Dashboard, stats and library features listed; no video/screenshots verified.
**Claims:** Built functional AI surveillance system in 36 hours | Real-time processing with minimal latency (no metrics)
**Gaps:** No evidence file or README read; Video/screens unverified
Sources: https://devpost.com/software/hawkwatch, https://treehacks-2025.devpost.com/

---

### HeartI
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Winner Most Impactful Hack (JBL Partybox 110 per team member)

**What it is:** A web tool that turns cardiac MRI scans into an interactive 3D heart model, labels chambers and vessels with a custom segmentation model, and classifies likely congenital heart disease type and severity with a confidence score. Doctors can accept or reject findings.
**Problem / user:** Doctors and patients managing congenital heart disease, which needs lifelong monitoring as more children reach adulthood.

**Features**
- 3D heart model from cardiac MRI — Algorithm maps MRI intensity to volumes, strips background and builds smooth surface meshes; chambers and vessels can be shown or hidden for lighter rendering. *[shown_working]*
- Custom segmentation model — PyTorch model trained on an A100 labels eight structures (four chambers, four vessels) in CMRI volumes; trained on 59 hearts, with manual segmentation still needed. *[claimed]*
- CHD category and severity classification — Embeddings paired with CHD labels are searched in Vespa with angular distance; returns likely categories, severity and a confidence score. *[claimed]*
- Doctor feedback form — Clinician accepts or rejects findings and explains reasoning, intended for later fine-tuning. *[claimed]*
- AI voice chat — Discuss the model output and reasoning by voice; ElevenLabs is listed but its role is not explained. *[claimed]*
- 4D and style-transfer extensions — Planned time-series reconstructions and realistic tissue textures. *[planned]*

**Flow:** Upload a cardiac MRI scan → Receive a 3D model with CHD categories, severity and confidence → Toggle chambers and vessels in the viewer → Doctor accepts or rejects and records reasoning → Ask questions through voice chat

**Prompt:** Most Impactful Hack: rewards potential for significant positive change or response to a pressing social issue such as environmental, accessibility or justice concerns.
**Fit (implied):** Aims to ease diagnosis and monitoring of congenital heart disease for clinicians worldwide. Devpost states the win but not the criteria mapping.  *(targeted: Most Impactful Hack)*
**Sponsor tools:** Vespa (Vector similarity search over labeled scan embeddings, supporting); Brev (NVIDIA A100) (Training the segmentation model, supporting); ElevenLabs (Listed, probably voice chat; unstated, unclear)
**AI:** Custom 3D cardiac segmentation network plus embedding-based nearest-neighbor retrieval for CHD labels with confidence; a voice assistant for explanations. No accuracy numbers reported.
**Architecture:** Next.js/React/TypeScript front end with 3D viewer; FastAPI backend runs segmentation, mesh generation and Vespa lookups; PyTorch trained offline.
**Novelty:** Pairs 3D reconstruction from MRI with retrieval-based CHD classification and a clinician-feedback loop, from a tiny public dataset.
**Scope:** small · working: Live Vercel demo and about 2.6k LOC repo with Docker; no metrics, tests or video; model limited by 59-heart dataset. · polish: Deployed site and five screenshots; README is the unedited Next.js template.
**Claims:** Built 3D models from 2D CMRI scans | Segmentation identified regions of interest despite limited data | Optimized for varied devices and browsers
**Gaps:** README is create-next-app boilerplate; No accuracy or validation numbers; Roles of Luma AI, Meta Quest and ElevenLabs unexplained
Sources: https://devpost.com/software/hearti, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-hearti.json (README, boilerplate)

---

### HiveMind
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Education Grand Prize

**What it is:** A peer-learning platform that classifies each student's comprehension from AI quizzes, assigns them to four-person learning hubs and pairs stronger with weaker students for Zoom sessions watched by an AI agent. Progress is shown on a 3D brain visualization.
**Problem / user:** Students in mixed-level classes who fall behind in standardized instruction, and stronger classmates with no structured way to tutor them.

**Features**
- AI quizzes and comprehension levels — Student responses are embedded and analyzed (Perplexity Sonar reasoning) into four levels of understanding. *[claimed]*
- Four-person learning hubs — Custom matching algorithm places students into hubs from foundational support to mastery. *[claimed]*
- Strong-weak peer pairing — Higher scorers are matched with lower scorers within the system. *[claimed]*
- Vector storage of learning states — IRIS Vector database stores embeddings; README proposes capturing cognitive state, mental-model evolution, misconceptions and frustration versus flow. *[claimed]*
- Monitored Zoom peer sessions — An AI agent evaluates student and hub progress; Zoom transcription and suggestions are listed as next steps. *[planned]*
- 3D brain progress dashboard — Three.js interactive brain visualization built in Next.js tracks learning progress. *[shown_working]*
- Gamification and week-by-week framework — Badges and leaderboards planned; weekly class improvement framework described. *[planned]*

**Flow:** Student logs in → Completes AI quizzes → System embeds responses and assigns a comprehension level → Student is placed in a four-person hub and matched with a peer → Peers meet on Zoom with an AI monitor → Student tracks progress on the 3D brain dashboard

**Prompt:** Education Grand Prize (Zoom): the most creative and impactful solution that rethinks how people learn, connect and grow; lowers barriers, boosts engagement, inclusivity.
**Fit (implied):** Builds a peer-tutoring structure around Zoom sessions, with comprehension grouping and engagement visuals. Devpost names the prize and Zoom use but does not map features to the criteria.  *(targeted: Education Grand Prize)*
**Sponsor tools:** InterSystems IRIS Vector (Storing learning-state embeddings, core); Perplexity Sonar API (Analyzing and categorizing responses, supporting); Zoom (Peer sessions; transcription integration planned, supporting)
**AI:** Vector embeddings of student responses plus LLM reasoning (Perplexity Sonar, Gemini listed) to classify understanding and drive peer matching; ChromaDB and Vespa also listed without explanation.
**Architecture:** Python backend handles auth, assessment and matching with vector storage; Next.js/TypeScript front end with Three.js dashboard; team migrated to new repos after merge conflicts.
**Novelty:** Treats learning states as embeddings for retrieval and matching, and gives a 3D brain metaphor for progress; ambition is documented more in plan text than finished features.
**Scope:** medium · working: About 12.7k LOC across several repos, no tests; README is a design plan for data points; Devpost claims real-time assessment without metrics. · polish: 3D brain visual; no video or live demo; repos fragmented.
**Claims:** Real-time AI assessment with accurate comprehension categorization (no figures) | Scalable backend (no numbers)
**Gaps:** README is a design plan, only first part read; reflects intended data model; Two other repos linked on Devpost not read; Many tags (Flask, Streamlit, Supabase, Vespa, ChromaDB) unexplained
Sources: https://devpost.com/software/hivemind-18cula, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-hivemind.json (README)

---

### Iris
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Edge AI Prize: Most Creative On-Device AI Deployment ($10k Cash)

**What it is:** A 3D-printed headset that holds an iPhone as camera for blind users. An agent system of captioning, classification, segmentation and depth models detects hazards, triggers a haptic buzz and speaks step-by-step directions; voice questions are answered through chained vision models.
**Problem / user:** Blind and visually impaired people who face head-height collisions, street crossings and unseen hazards, and need affordable guidance.

**Features**
- Real-time hazard detection — Specialist agents (captioning, classification, segmentation, depth) run on a tuned VLM pipeline; claimed under 100 ms. *[claimed]*
- Haptic buzz alert — Buzz fires when a danger is identified; directional haptics are a next step. *[claimed]*
- Spoken step-by-step guidance — TTS gives instructions to avoid obstacles, cross streets or reorient. *[claimed]*
- Voice queries — Speech-to-text triggers workflows such as 'Where's the door?' or 'Can I cross the street?' via Groq LPU APIs for detection and scene similarity. *[claimed]*
- Latency optimization — PyTorch compiler, cuDNN, flash/paged attention, quantized dtypes and CUDA graphs reduce time to detection. *[claimed]*
- Custom streaming protocol — Datagram protocol replaces JSON to push tokens and data to clients. *[claimed]*
- Expo cross-platform app and printed headset — Expo app on iPhone; STL-designed headset holds the phone. *[shown_working]*

**Flow:** Clip iPhone into the printed headset → App streams camera input to the agent backend → Agents detect hazards and the user feels a buzz → Spoken directions guide around the hazard → User asks voice questions at any time

**Prompt:** Edge AI Most Creative On-Device AI Deployment (Liquid AI, $10k, 3 winners): groundbreaking AI demos on edge devices like laptops or phones, using novel architectures or modalities under resource limits.
**Fit (implied):** Phone as camera and sensor with latency-tuned models; README names Brev GPU compute and Groq for inference, so how much runs on the device is unclear. Prize named as won, no stated mapping.  *(targeted: Edge AI Prize: Most Creative On-Device AI Deployment)*
**Sponsor tools:** Groq LPU APIs (Object detection and voice-triggered workflows, supporting); Brev.dev (NVIDIA GPUs) (Training and inference compute, core)
**AI:** Real-time tuned VLM plus captioning, classification, segmentation and depth agents, chained for queries; heavy GPU optimization (compiler, flash and paged attention, quantization).
**Architecture:** iPhone streams to a Python backend (uv) via custom datagram protocol; agent models on Brev GPUs; results return as haptic cues and TTS in an Expo app.
**Novelty:** Combines aggressive inference optimization and a bespoke wire protocol with an inexpensive printed headset; opens with sourced mobility accident statistics.
**Scope:** small · working: About 900 LOC with some tests; README and Devpost claim a functioning multimodal system but give no measured latency or user tests. · polish: Detailed README, two headset images; no demo video.
**Claims:** Hazard detection in under 100 ms | About 40 percent of surveyed blind people have head-height collisions at least yearly | 46 percent higher road crash risk among visually impaired people
**Gaps:** No measured TTD values; Unclear which models run on-device vs remote; No video
Sources: https://devpost.com/software/iris-vlnzp0, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-iris.json (README)

---

### Lemon
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Sustainability Prize: Best incorporation of broader context to enhance venture viability ($800 Cash)

**What it is:** A FlutterFlow mobile marketplace where farmers list surplus or cosmetically imperfect produce at a discount, and consumers and businesses buy it, with bulk requests, local advertising and farmer partnerships for business accounts.
**Problem / user:** Farmers whose edible but unattractive produce is discarded, plus eco-minded shoppers and businesses wanting cheaper local produce.

**Features**
- Customer shopping — Customers browse discounted listings showing source details, search, add to cart and buy when they choose, like an online grocery store. *[shown_working]*
- Farmer listings — Producers create listings for surplus or wonky produce. *[shown_working]*
- Business accounts — Businesses shop like customers, request bulk orders, advertise to nearby users and seek long-term farmer partnerships. *[claimed]*
- Sustainability spotlights — Main page shows local-area sustainability highlights to customers. *[claimed]*
- Authentication, search and cart — Supabase/PostgreSQL backend with custom Flutter functions for auth, product query and cart. *[shown_working]*
- Share buttons — Users share the initiative with friends. *[claimed]*

**Flow:** Customer signs up and browses discounted produce with source info → Adds items to cart and buys → Farmer posts surplus listings → Business signs up, requests bulk and finds nearby producers

**Prompt:** Sustainability Prize, best incorporation of broader context ($800): judges how well a team handles factors affecting viability such as regulation, purchaser versus user, equitable access and unintended impacts.
**Fit (implied):** Three-sided marketplace (consumer, farmer, business) addresses who buys versus sells and supply side incentives. Pages name the prize but do not explain the mapping.  *(targeted: Sustainability Prize: Best incorporation of broader context to enhance venture viability)*
**Sponsor tools:** FlutterFlow (Building the app with sponsored access, core); Supabase (PostgreSQL backend, core)
**AI:** none
**Architecture:** FlutterFlow (Flutter/Dart) mobile app with custom functions on a Supabase PostgreSQL backend handling listings, auth, search and cart.
**Novelty:** Combines imperfect-produce discounts with business bulk requests and local advertising; first hackathon team built with a low-code tool.
**Scope:** small · working: README admits only the mobile app works; repo about 19k LOC (mostly generated) with tests; FlutterFlow demo link exists. · polish: Branded app, share buttons, live FlutterFlow demo; no video.
**Claims:** Over 50 percent of US produce is thrown away for looking too ugly (context, not app result) | Food waste footprint 248x bigger than plastic (context claim)
**Gaps:** Business features' implementation status unclear; No usage metrics; Which pages work beyond mobile not specified
Sources: https://devpost.com/software/lemon-7gn5hq, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-lemon.json (README)

---

### MediLedger
*TreeHacks TreeHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Web3 Prize: Best AI Agents ($8k Cash + 8k EIGEN [1st] & $7k Cash + 7k EIGEN [2nd])

**What it is:** Privacy-preserving drug-availability check between hospitals: each hospital commits its inventory as a Merkle tree root on EigenDA, and an AI agent finds neighbors with stock by verifying Merkle proofs without exposing full inventories.
**Problem / user:** Hospitals facing drug stockouts that rely on manual calls and will not share full inventories with competitors.

**Features**
- Merkle-tree inventory commitments — Leaves hash drug name plus quantity; root published to EigenDA for tamper detection *[claimed]*
- Local stock check by agent — Agent checks own inventory, triggers network search when out or trending low *[claimed]*
- Proof-based availability search — Hospitals with the drug produce Merkle proofs verified against the stored roots *[claimed]*
- Validated hospital list output — Returns hospitals whose proofs validated *[claimed]*
- On-chain roots, zkProofs, prediction, wallet auth — Future work *[planned]*

**Flow:** Agent checks local stock → If low, fetch other hospitals roots from EigenDA → Hospitals generate Merkle proofs → System verifies proofs against roots → List of hospitals with stock returned

**Prompt:** EigenLayer Web3 Prize: Best AI Agents; seeks robust agents that plan, act, verify; criteria technical prowess, completeness, usability, wow; bonus for meaningful EigenLayer or off-chain service use.
**Fit (implied):** Agent checks stock and triggers cryptographic verification, with EigenDA as the commitment layer and an EigenLayer agent-framework adapter.  *(targeted: Web3 Prize: Best AI Agents)*
**Sponsor tools:** EigenDA / EigenLayer agent framework (storing inventory roots and verifiable logging, core)
**AI:** An AI agent (model unnamed) decides when to search and triggers proof verification; the verification itself is deterministic hashing.
**Architecture:** Express/TypeScript backend builds SHA256 Merkle trees and checks proofs against roots on EigenDA; FlutterFlow frontend; off-chain verification.
**Novelty:** Applies Merkle commitments and a data-availability layer to inter-hospital inventory discovery, not typical agent chat apps.
**Scope:** medium · working: Demo video linked; repo 20k LOC estimate with tests; ZK proofs not implemented. · polish: FlutterFlow template UI; team reports backend and integration issues.
**Claims:** Working decentralized inventory proof-of-concept
**Gaps:** Video not watched; Placement within prize unclear
Sources: https://devpost.com/software/mediledger, https://github.com/shayaansultan/treehacks-final (evidence file), https://treehacks-2025.devpost.com/

---

### OmNom
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Winner Most Creative Hack (Pioneer DJ DDJ-FLX4 Pack per team member)

**What it is:** A custom-built roughly six-foot delivery robot that takes a natural-language food order from a website, drives to a campus eatery by GPS, finds the kiosk indoors, taps the touchscreen with a robotic arm, and returns holding food on a rope the recipient cuts.
**Problem / user:** Late-night Stanford students who want a snack without walking across cold campus or queuing; future uses include people unable to visit restaurants.

**Features**
- Natural-language ordering website — React/FastAPI site; OpenAI parses the request into start and end points and order details. *[shown_working]*
- Outdoor waypoint navigation — OpenRouteService waypoints go to a Jetson computer; RTK GPS and BNO055 IMU steer, but GNSS drift made it unreliable. *[claimed]*
- Indoor vision navigation — Stereo camera depth (DPT) plus YOLOv8, CLIP and sentence-transformer search locate entrance, line and kiosk after SLAM was dropped. *[claimed]*
- Touchscreen ordering — A GPT-4 state machine reads gridded wide-angle frames; a 5-DOF arm with a 250 mm stylus taps the kiosk; tested against a simulated ordering app. *[shown_working]*
- Live location tracking — Robot position streams to the site over WebSockets and Google Maps. *[claimed]*
- Rope-cut handoff — Kevlar rope lift holds food; recipient cuts the rope to receive it. *[shown_working]*

**Flow:** User types an order on the website → OpenAI parses locations and items → Robot drives outdoors by waypoints to the eatery → Indoors it finds the kiosk and taps through the order → Robot returns while user watches its map → User cuts the rope to take the food

**Prompt:** Most Creative Hack: celebrates original, imaginative work with unconventional thinking or novel ideas and approaches.
**Fit (implied):** Unusual end-to-end physical agent that orders food itself and hands it off via a cut-the-rope mechanism. Devpost notes the prize win but does not map to criteria.  *(targeted: Most Creative Hack)*
**AI:** GPT-4 parses orders and drives the kiosk state machine from camera frames; YOLOv8, CLIP, DPT depth and sentence-transformer semantic search handle perception; no ROS, custom PID control.
**Architecture:** Jetson Orin main computer with Arduino Mega/UNO, RoboClaw motor controllers and ten sensors; FastAPI/WebSocket backend and Vite React site; custom drivers and closed-loop control.
**Novelty:** Full from-scratch mobile manipulator (22 laser-cut parts) that operates a touchscreen kiosk itself; team states the whole sequence was never reliably run end-to-end.
**Scope:** large · working: Hardware built in 36 hours with about 6.7k LOC; team says outdoor GNSS drift prevented a reliable full demo; test ordering app is live. · polish: Detailed hardware writeup and mechanical design; README is a Vite template with port notes; no video.
**Claims:** About 6 ft tall with 10 sensors and 22 laser-cut parts | About 30 A peak power from three lead-acid batteries | Built and programmed in 36 hours
**Gaps:** README is template text, so details come from Devpost; No success rates or video; Devpost mentions a 'convex database' that is probably a vector database
Sources: https://devpost.com/software/omnom-hg16v3, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-omnom.json (README, template)

---

### PUSHPA (Pyro UAV System for High-risk Patrol and Alerting)
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Winner Edge AI Prize: Operator Optimization Champion ($5k Cash)

**What it is:** An offline-capable firefighter support concept: hacked Meta glasses and a Samsung phone run a vision-language model for AR hazard overlays, a LangChain agent turns spoken or WhatsApp commands into drone tasks, and a web dashboard merges telemetry and findings.
**Problem / user:** Firefighters and responders who lose Wi-Fi and cell coverage in fires and need hazard awareness and drone reconnaissance without the cloud.

**Features**
- On-device scene understanding — MobileVLM via llama.cpp, OCR and object detection run on a Samsung Galaxy with no cloud, with optional SAM v2 and Gemini. *[claimed]*
- Optimized convolution kernel — Custom PyTorch/CPU convolution with Winograd F(2,3) and 256-channel blocking, claimed 20x faster on edge hardware. *[claimed]*
- AR overlays and spoken alerts on glasses — Glasses hacked via a community tutorial display hazards and results and warn of structural weaknesses. *[claimed]*
- Agentic drone control — LangChain splits commands like 'scan that building' into sub-steps sent over MAVLink; commands via WhatsApp or glasses. *[claimed]*
- Live telemetry dashboard — Next.js/Socket.IO page shows drone video, sensor readings, bounding boxes, routes and AI findings. *[claimed]*
- Security hardening — Token handling, authentication and input checks against prompt injection. *[claimed]*

**Flow:** Responder issues a command by WhatsApp or glasses → Node service passes it to the LangChain agent → Agent calls the flight controller or the on-device vision pipeline → Drone streams video while glasses run inference → Results return as AR overlays, WhatsApp text and dashboard updates

**Prompt:** Edge AI Operator Optimization Champion (Liquid AI, $5k per operator, 2 winners): optimize convolution or recurrence operators on a Samsung Galaxy S24, judged on peak memory and latency from profiling scripts with accurate results.
**Fit (explicit):** Includes a custom Winograd-based convolution kernel on a Samsung Galaxy, a direct match to the operator-optimization challenge; the 20x claim has no stated baseline or profile numbers.  *(targeted: Edge AI Prize: Operator Optimization Champion)*
**Sponsor tools:** Gemini (Advanced tasks and synthetic wildfire test data, supporting); ExecuTorch / llama.cpp (On-device inference runtimes, supporting)
**AI:** MobileVLM and OCR on-device with partial quantization, optional SAM v2 and Gemini, a LangChain agent for task planning, and a hand-written Winograd convolution kernel.
**Architecture:** Drone (MAVLink), glasses and Samsung phone feed an on-device vision pipeline; Node.js and LangChain service orchestrates tasks; Next.js dashboard over Socket.IO.
**Novelty:** Unusually broad stack mixing a low-level operator optimization with drone, smart-glasses hacking and agentic control; many extra awards listed on the page are unsupported.
**Scope:** medium · working: Live Vercel dashboard link; repo clone failed so code unverified; no latency or accuracy numbers beyond 20x speedup claim. · polish: Detailed writeup and dashboard; no video; project name varies across the page.
**Claims:** 20x inference speedup on edge devices versus naive baselines | Near-zero-latency AR overlays without Wi-Fi or cloud | Operates without cloud connectivity
**Gaps:** Repo clone failed and README raw fetch returned 404; 20x baseline unspecified; extra awards listed on page unverified; Features inferred from Devpost architecture description
Sources: https://devpost.com/software/pushpa-pyro-uav-system-for-high-risk-patrol-and-alerting, https://treehacks-2025.devpost.com/

---

### SurviveX
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Edge AI Prize: Most Creative On-Device AI Deployment ($10k Cash)

**What it is:** An offline survival assistant: a Llama-3.2-1B model fine-tuned with LoRA on survival scenarios and run on-device through ExecuTorch in a SwiftUI app for Apple Vision Pro (also iPhone and iPad), giving hands-free spoken step-by-step guidance that can adapt to simulated vitals.
**Problem / user:** Hikers, soldiers, first responders and people lost at sea who have no connectivity and need immediate expert guidance.

**Features**
- Offline on-device LLM — Llama-3.2-1B-Instruct compiled to ExecuTorch .pte files and linked into a Swift app; 3B was too slow. *[shown_working]*
- Survival-tuned model — LoRA fine-tune via torchtune on an H100 (Brev) with GPT-4-generated scenario prompt/completion pairs to fix poor fire-starting answers. *[shown_working]*
- Step-by-step guidance with clarification — Gives one small step, asks for confirmation, lets the user ask follow-ups at any point. *[shown_working]*
- Hands-free speech interaction — Spoken requests and voice replies on Vision Pro, with touch as a supplement. *[claimed]*
- Vitals-aware tone — Terra API supplies heartbeat and vitals (simulated in the prototype) to adjust tone and focus. *[claimed]*
- Adjustable context length — Context window set by device capability; longer contexts improved output on iPhone and Vision Pro. *[shown_working]*

**Flow:** User speaks a request such as starting a fire without matches → Assistant gives one small step, for example gathering dry tinder → User confirms or asks for clarification → Vitals shape tone and focus when available → Process continues step by step

**Prompt:** Edge AI Most Creative On-Device AI Deployment (Liquid AI, $10k, 3 winners): groundbreaking AI demos on edge devices such as laptops or phones, using novel architectures or modalities under resource limits.
**Fit (explicit):** Runs a fine-tuned small LLM fully offline on a headset, phone and tablet via ExecuTorch under memory limits. README frames it as an offline-first embedded assistant for hands-free devices.  *(targeted: Edge AI Prize: Most Creative On-Device AI Deployment)*
**Sponsor tools:** ExecuTorch (On-device inference runtime, core); Terra API (Simulated vital signs, supporting); Brev.dev (H100) (LoRA fine-tuning compute, supporting)
**AI:** Llama-3.2-1B-Instruct fine-tuned with LoRA on GPT-4-generated survival Q&A, exported to ExecuTorch and run locally; vitals conditioning is simulated.
**Architecture:** SwiftUI app on Vision Pro/iPhone/iPad links ExecuTorch binaries running the .pte model; prompting layer adds vitals context; training done offline on Brev H100.
**Novelty:** Runs a custom fine-tuned LLM on Apple Vision Pro through ExecuTorch with no network; fine-tuned model grew too large for Vision Pro memory.
**Scope:** small · working: Repo about 1k LOC with tests and demo video; Devpost reports ExecuTorch ran, but no accuracy or latency figures. · polish: Demo video, README with problem statement, extra Drive files; Vision Pro memory limits noted.
**Claims:** 30 percent of people lost in the wilderness never return (context claim) | Changing context length improved output quality on iPhone and Vision Pro
**Gaps:** Video not watched; Fine-tuned model size exceeded Vision Pro memory so which device runs it is unclear; No metrics
Sources: https://devpost.com/software/survivex, https://treehacks-2025.devpost.com/, evidence/treehacks-treehacks-2025-survivex.json (README)

---

### Therms - Thermoregulation Wearables with AI-powered Insights
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Healthcare Grand Prize; Scrapybara: Capy Prize

**What it is:** A shoe-sole wearable that uses reversible Peltier modules to heat or cool the feet, paired with a Next.js web app that combines shoe data and other wearable data, produces GPT-based insights, and uses a computer-use agent to book appointments.
**Problem / user:** People who need body temperature control (athletes, soldiers, laborers, people with thermoregulation dysfunction such as spinal cord injury or diabetes, elderly) where liquid cooling rigs are bulky and cooling gloves block the hands.

**Features**
- Heating and cooling through the foot sole — Peltier modules with reversible polarity on heat sinks and a copper spreader layer, driven by a motor controller, battery powered and pump-less. *[claimed]*
- Foot temperature and motion sensing — Embedded temperature sensor beside the copper layer plus an IMU, read by a microcontroller to drive heating or cooling. *[claimed]*
- Device pairing and data sync — Shoes pair with the web app via Firebase; the Next.js interface shows data visuals and lets users personalize settings. *[claimed]*
- Outside wearable data import — Terra API brings heart rate, sleep, activity and condition data from other wearables into the same dashboard. *[claimed]*
- AI insights and anomaly detection — OpenAI analyzes combined thermal and health data to find anomalies (e.g. abnormal foot warming in a diabetic user) and suggest stimulus strategies. *[claimed]*
- Automated appointment booking and prescriptions — Scrapybara computer-use agent acts on detected health trends to book medical appointments and manage prescriptions. *[claimed]*
- Modular sole frame — 3D-printed frame with replaceable parts that fits different footwear. *[claimed]*

**Flow:** Wear shoe with Therms sole → Sensor reads foot temperature; controller switches heating or cooling → Pair device in web app and view live data → Terra data merges with shoe data → OpenAI flags anomalies and strategies → Scrapybara books an appointment if a trend warrants it

**Prompt:** not public / not found
**Fit (implied):** Healthcare: a wearable for thermoregulation conditions with monitoring and insights. Scrapybara: its agent turns detected trends into booked appointments and prescription handling. Page lists Scrapybara in the data pipeline but does not name the prize it targeted.  *(targeted: Healthcare Grand Prize, Scrapybara: Capy Prize)*
**Sponsor tools:** Scrapybara (Computer-use agent that automates appointment booking and prescription management after trend detection, core); Terra API (Ingesting heart rate, sleep and activity data from other wearables, supporting)
**AI:** OpenAI models analyze merged shoe and Terra data for anomalies and stimulus strategy; Scrapybara agent executes follow-up web actions. Page also mentions biological models for stimulus response.
**Architecture:** Shoe hardware (Peltier, temp sensor, IMU, microcontroller, motor controller) syncs through Firebase to a Next.js/Node app; Terra data plus shoe data go to OpenAI, whose output triggers Scrapybara automation.
**Novelty:** Combines custom thermoelectric hardware in a shoe sole with a health data and agent layer; targets the foot as a thermal window, unlike gloves or liquid cooling.
**Scope:** medium · working: Page claims a working pump-less prototype built in 36 hours; repo has about 4.4k LOC web app; no video or live demo. · polish: README is the default Next.js template; page includes citations and CAD iterations but no screenshots verified.
**Claims:** Working battery-powered heating and cooling prototype in 36 hours | Palm-cooling self-experiments gave more strength reps and nearly doubled running time in a 100F room (anecdotal)
**Gaps:** README is default template; No official Healthcare or Scrapybara prize text in cache; No demo video; Unclear which hardware parts were shown working at demo
Sources: https://devpost.com/software/therms-thermoregulation-wearables-with-ai-powered-insights, evidence/treehacks-treehacks-2025-therms-thermoregulation-wearables-with-ai-powered-insights.json, prompts_cache/treehacks-2025.md

---

### VisionGuard: smart vision for smarter driving
*TreeHacks TreeHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Autonomy Grand Prize; Tesla: Excellence Prize

**What it is:** A pipeline that feeds in-car video to vision-language models (Gemini, Pixtral) with chain-of-thought prompting and majority-vote ensembling to describe driver behavior and road hazards, plus a GPT-4 layer for driver feedback and a failed GRPO fine-tune of Qwen VL-2B.
**Problem / user:** Drivers in icy or congested conditions, and insurers, fleet managers and autonomous-vehicle teams wanting explainable detection of distracted or reckless driving.

**Features**
- Driver behavior transcription from in-car video — Sampled video frames are passed to VLMs (Gemini Pro 2.0, Pixtral) that describe safe and unsafe actions. *[claimed]*
- Detection of distraction, reckless maneuvers and hazardous conditions — Prompted VLMs flag phone use, drowsiness, sudden lane changes, low visibility and icy roads. *[claimed]*
- Chain-of-thought prompting — Prompts adapted from OpenEMMA, an open reproduction of Waymo's EMMA, to elicit driving-scene reasoning. *[claimed]*
- Majority-vote ensembling with option shuffling — Multiple runs vote; answer choices are shuffled to offset the models' bias toward first and last options. *[claimed]*
- Natural-language driver feedback — GPT-4 turns detected behaviors into messages like a distraction warning or a slow-down advice, with causal explanations. *[claimed]*
- GRPO fine-tune of Qwen VL-2B — TRL with DeepSpeed tensor sharding on 4 A100s using NuScenes-QA; result underperformed API models. *[shown_working]*

**Flow:** Provide in-car video clip → Frames are sampled and sent to VLMs → Ensemble vote yields behavior or hazard answers → GPT-4 produces human-readable alert

**Prompt:** not public / not found
**Fit (implied):** Works on driving-scene question answering over real-world video, similar to Tesla-provided data, using VLM inference tricks and an RL fine-tune. Page and README do not state the prize challenge text or name the target prize.  *(targeted: Autonomy Grand Prize, Tesla: Excellence Prize)*
**AI:** Prompted VLMs (Gemini Pro 2.0, Pixtral 13B) with chain of thought, majority voting and few-shot; GPT-4 for feedback text; GRPO fine-tuning of Qwen VL-2B on NuScenes-QA, which did not beat APIs.
**Architecture:** Video frames to parallel VLM calls, ensemble voting, GPT-4 reasoning layer for alerts; separate offline GRPO training job on multi-GPU. Repo holds notebooks and a Q&A folder.
**Novelty:** Candid about a failed RL fine-tune; applies inference-time techniques (shuffling against option bias, voting) to a driving video QA task rather than building a UI.
**Scope:** small · working: Repo is tiny (about 24 LOC code, mostly notebooks); no demo video; page claims a functional prototype but gives no numbers. · polish: README duplicates Devpost text; slide deck linked; no screenshots verified.
**Claims:** Functional prototype analyzing driving video with low-latency alerts (README); Devpost says real-time was not achieved | GRPO-trained Qwen VL-2B performed worse than API benchmarks
**Gaps:** No official Autonomy or Tesla prize text found; README says real-time low latency while Devpost says it was not achieved; No evaluation numbers; Slide deck not read
Sources: https://devpost.com/software/visionguard-smart-vision-for-smarter-driving, evidence/treehacks-treehacks-2025-visionguard-smart-vision-for-smarter-driving.json

---

