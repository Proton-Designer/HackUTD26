# HackIllinois — HackIllinois 2026 (13 projects)

### Cat Vision Copilot
*HackIllinois HackIllinois 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Track: Best AI Inspection (2nd Place) [2nd]

**What it is:** A web inspection copilot styled after Caterpillar's Cat Inspect: it analyzes live video, images and voice of equipment, flags and ranks issues by severity, suggests parts, builds reports and answers questions through a chatbot.
**Problem / user:** Equipment inspectors for whom field inspections are manual, slow and inconsistent; stated user is a Cat Inspect user, with fleet operators later.

**Features**
- Multimodal inspection input — Takes live video, images and voice and captures frames for AI models to look for anomalies with real-time feedback. *[claimed]*
- Issue detection with severity ranking — Detected issues are ranked so the inspector can prioritize urgent safety items. *[claimed]*
- Part identification and replacement suggestions — Identifies parts from visual input and proposes possible replacements. *[claimed]*
- Automatic report generation — Structures findings into reports stored in a Supabase database. *[claimed]*
- Inspection data chatbot — Answers questions and produces charts and insights from past inspections. *[claimed]*
- Cat Inspect-like interface — Frontend mirrors Cat Inspect structure and keeps the inspector making final decisions. *[claimed]*

**Flow:** Start an inspection with video, images or voice → AI flags anomalies and ranks severity → Review identified parts and suggestions → Report is generated and saved → Ask the chatbot about past inspections

**Prompt:** Caterpillar-sponsored Best AI Inspection track: build AI for field operations and logistics that makes inspections, parts identification and site planning smarter, faster and safer.
**Fit (implied):** Covers inspections, parts identification and reporting for Cat equipment in one interface, matching the track's themes; Devpost states the track result.  *(targeted: Track: Best AI Inspection)*
**Sponsor tools:** ElevenLabs (Voice output/input for hands-free inspection (listed in tags), unclear)
**AI:** Listed stack: YOLO, OpenCV and TensorFlow for vision, Hugging Face Transformers, scikit-learn, OpenAI and Ollama LLMs, ElevenLabs for voice; exact roles not described.
**Architecture:** React/TypeScript web frontend, Node and Python backend, Supabase storage, vision models processing captured frames, LLM chatbot over stored inspection data.
**Novelty:** Designed as a drop-in companion to an existing Caterpillar tool, combining detection, parts lookup, reporting and analytics chat in one flow.
**Scope:** unclear · working: Video exists but no repo or live link; all features are described in text only. · polish: Seven screenshots and video listed; no metrics.
**Claims:** Ranks severity, identifies parts and generates reports in one interface
**Gaps:** no repo; video not watched; no metrics
Sources: https://devpost.com/software/cat-vision, https://hackillinois-2026.devpost.com/

---

### Cat-AR-pillar
*HackIllinois HackIllinois 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Track: Best AI Inspection (3rd Place) [3rd]

**What it is:** A Meta Quest 3 mixed-reality app that identifies excavator components with an on-device YOLO model, highlights them in the inspector's view, and files voice notes, issues and short videos under the detected part, hands-free.
**Problem / user:** Heavy-equipment inspectors doing repetitive daily inspections who juggle paper checklists, tablets and the machine.

**Features**
- Real-time component detection — YOLOv12 Nano segments cab, boom, stick, bucket and wheels from the headset camera, running fully on-device. *[shown_working]*
- AR overlay and checklist progress — Bounding boxes and labels highlight parts in view and show checklist progress. *[shown_working]*
- Auto-assigned notes — Notes, issues and clips attach to the identified part without manual selection; manual selection remains a fallback. *[shown_working]*
- Gaze and hand menu — A floating menu opens when the inspector looks at the left hand. *[shown_working]*
- Voice comments and video snippets — Speech-to-text comments and short recordings are matched to labeled parts for later filtering. *[claimed]*
- Offline operation — No cloud APIs or jobsite connectivity required. *[claimed]*

**Flow:** Wear Quest 3 and look at a machine part → System detects and highlights the component → Look at left hand to open menu → Log issue, dictate comment or record clip → Entry is filed under the detected part

**Prompt:** Caterpillar-sponsored Best AI Inspection track: AI for field operations that makes inspections, parts identification and site planning smarter, faster and safer.
**Fit (implied):** Hands-free AR inspection tool with automatic part identification for Cat-style excavators; Devpost states track placement.  *(targeted: Track: Best AI Inspection)*
**AI:** YOLOv12 Nano trained on a hand-labeled set of about 60 excavator images (Roboflow, Label Studio) with heavy augmentation, run on device for detection and segmentation; speech-to-text for notes.
**Architecture:** Unity/C# mixed-reality app on Quest 3 reading the camera feed, running YOLO inference, drawing overlays, logging structured inspection entries; Python ML training pipeline.
**Novelty:** Headset-based hands-free inspection with a tiny custom dataset and fully local inference, rather than a phone or cloud app.
**Scope:** small · working: Demo video shows detection on a Cat excavator; no repo or numbers; page says prototype. · polish: Video and screenshots of varied views; no repo documentation.
**Claims:** Fully local on-device inference | Trained on about 60 images
**Gaps:** no repo; video not watched; no accuracy or latency metrics
Sources: https://devpost.com/software/cat-ar-pillar, https://hackillinois-2026.devpost.com/

---

### ease 'n spect
*HackIllinois HackIllinois 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Track: Best AI Inspection (1st Place) [1st]

**What it is:** A React Native (Expo) app that walks an inspector through a five-step excavator inspection with 3D camera-angle cues, then runs Gemini vision, Whisper transcription and Qwen 3 parts suggestions on Modal to produce an AI summary card.
**Problem / user:** Field inspectors facing disorganized excavator inspections with inconsistent checklists and poor records.

**Features**
- Guided five-step inspection — Steps: front cab window, left track, arm joint/hydraulic pump, two bucket-teeth views. *[claimed]*
- 3D camera-angle cue — React Three Fiber excavator model mimics the angle the inspector should photograph. *[claimed]*
- Per-step capture — Photo, Good/Needs Attention/Bad rating and voice note recorded at each step. *[claimed]*
- Gemini vision analysis — gemini-2.5-flash assesses wear and fitness from multiple images in one prompt. *[claimed]*
- Whisper transcription and Qwen parts suggestions — Voice notes transcribed; Qwen 3 proposes replacement parts. *[claimed]*
- Summary card — Separates user input from AI assessment with wear indicators and next steps; reused for history. *[claimed]*

**Flow:** Tap Start Inspection → Follow 3D cue, take photo, rate, record note for each step → Upload to AI pipeline on Modal → Review summary card

**Prompt:** Caterpillar-sponsored Best AI Inspection track: AI for field operations that makes inspections, parts identification and site planning smarter, faster and safer.
**Fit (implied):** Guided inspection with AI wear assessment and parts suggestion for excavators; Devpost states the 1st place track result.  *(targeted: Track: Best AI Inspection)*
**Sponsor tools:** Modal (Hosts the vision, transcription and parts-suggestion AI workloads, supporting)
**AI:** Gemini 2.5 Flash for multi-image vision analysis, open-source Whisper for speech-to-text, Qwen 3 for parts suggestions; Pydantic-validated schema-first outputs.
**Architecture:** Expo React Native app with R3F 3D views uploads to FastAPI and Supabase Postgres; AI jobs run on Modal; async offload keeps UI responsive.
**Novelty:** 3D viewpoint cues that tell inspectors where to point the camera, plus a summary that keeps human and AI judgments separate.
**Scope:** small · working: Describes an end-to-end flow with a demo video; no repo or live link found. · polish: Video on Devpost; mobile UI with 3D models.
**Claims:** Simpler process enables more frequent inspections
**Gaps:** no repo; video not watched; no metrics
Sources: https://devpost.com/software/inspectus, https://hackillinois-2026.devpost.com/

---

### EcoApi(Recost)
*HackIllinois HackIllinois 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: Best Web API (1st Place) [1st]

**What it is:** A developer tool that scans a codebase for API calls, estimates monthly cost and rate-limit risk, flags N+1 and uncached patterns, and estimates electricity, water and CO2 footprint; delivered as a Cloudflare Workers REST API, React dashboard and VS Code extension.
**Problem / user:** Developers, including those shipping quickly with AI help, who lack visibility into surprise API spend, rate-limit key revocations and environmental impact.

**Features**
- Workspace API-call scanner in VS Code — Regex patterns detect calls in TS, JS, Python, Go, Java and Ruby and show results in a sidebar without a remote server. *[shown_working]*
- Cost analytics and endpoint diagnostics — Analysis engine applies per-provider pricing to estimate monthly spend and flags cacheable endpoints, rate-limit hotspots and N+1 patterns. *[shown_working]*
- Optimization suggestions — Generates caching, batching and N+1 fixes with estimated savings and severity. *[shown_working]*
- Sustainability estimates — Maps call volume to kWh, litres of water and grams CO2 using per-provider constants, split AI versus non-AI. *[shown_working]*
- D3 dependency graph and dashboard — React SPA with endpoint filters and network graph clustered by provider, file or cost. *[shown_working]*
- AI chat — Extension chat uses OpenAI to explain issues; the cloud API chat route uses Llama 3.1 8B on Cloudflare AI. *[shown_working]*
- Public REST API with docs — Hono on Workers with D1 storage, KV rate limiting, pagination; hosted at api.ecoapi.dev with docs site. *[shown_working]*

**Flow:** Install the VS Code extension or .vsix → Open a workspace and run a scan → Review cost and risk results in the sidebar → Ask the AI chat to explain or fix issues → Open the local dashboard for graph, endpoints and sustainability charts

**Prompt:** Stripe-sponsored Best Web API track: build a well-crafted API focused on surface design, developer experience and correctness, with clear predictable behavior and useful documentation.
**Fit (implied):** Ships a documented, live REST API with validation, pagination and rate limiting as the core service, with dashboard and extension as clients; Devpost lists the track win.  *(targeted: Track: Best Web API)*
**Sponsor tools:** Cloudflare Workers, D1, KV, Pages, Workers AI (API runtime, storage, rate limiting, dashboard hosting and Llama chat, core)
**AI:** Chat only: OpenAI in the extension and Llama 3.1 8B on Cloudflare AI via the API; the analysis itself is rule and regex based with hand-set pricing and sustainability constants.
**Architecture:** VS Code extension scans workspace and runs an embedded local server serving the dashboard; alternatively parsed call data goes to Hono API on Workers backed by D1; dashboard queries via TanStack Query.
**Novelty:** Combines API cost linting with environmental impact estimates in an IDE plugin; also mentions an upstream PR to an open-source project from findings.
**Scope:** large · working: Live API and docs site, packaged .vsix, seeded demo data, about 20k LOC across API, dashboard, extension and docs. · polish: Themes, animated graph, docs site, extension landing page; no tests.
**Claims:** Reported finding a vulnerability in an open-source project and proposing a fix | Estimates kWh, water and CO2 from call volume
**Gaps:** pricing constants unsourced; no measured savings
Sources: https://devpost.com/software/ecoapi, https://github.com/AndresL230/ecoapi, https://hackillinois-2026.devpost.com/

---

### LARYNX
*HackIllinois HackIllinois 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: Best AI Inference (2nd Place) [2nd]

**What it is:** A deepfake voice forensics tool that infers tongue, jaw and lip movement from audio and shows, in a 3D skull visualization, when the implied articulator speeds exceed human limits; a gradient-boosted classifier scores real versus synthetic speech.
**Problem / user:** Journalists, judges and analysts who get only an opaque confidence score from deepfake detectors and need explainable evidence.

**Features**
- Acoustic-to-articulatory inversion — HuBERT Large features go through an inversion model giving 12D EMA tongue, jaw and lip trajectories at 200Hz on a Modal B200 GPU. *[shown_working]*
- Kinematic forensic classifier — 108 velocity, acceleration, jerk and cross-correlation features feed HistGradientBoosting; README reports 89.2 percent accuracy over 73 TTS architectures. *[shown_working]*
- 3D skull visualization — React Three Fiber x-ray head animates tongue motion; deepfakes show velocity gauges spiking and tongue clipping through bone with red glitch effects. *[shown_working]*
- Generate-and-compare — Pastes text, produces TTS via OpenAI or Gemini, and compares against a real recording side by side. *[shown_working]*
- Streaming analysis — Results stream over server-sent events through a Cloudflare Worker proxy. *[shown_working]*
- Sonification and history — Tone.js alarms rise with anomalies; D1, R2 and Vectorize store history, audio and voice similarity. *[claimed]*

**Flow:** Upload real voice clip and watch smooth tongue animation → Generate a deepfake of the same text with TTS → Upload it and see velocity spike and skull glitch → Read the physical-impossibility verdict

**Prompt:** Modal-sponsored Best AI Inference track: build ambitious applications that run inference on Modal GPU compute to solve a real-world problem.
**Fit (explicit):** README names the Modal track and runs the full HuBERT, inversion and classifier pipeline on a B200 GPU with streaming results.  *(targeted: Track: Best AI Inference)*
**Sponsor tools:** Modal (B200 GPU inference for HuBERT, inversion and classification with SSE streaming, core); Cloudflare (Pages, Workers, D1, R2, Vectorize, AI Gateway) (Hosting, API proxy, storage and similarity search, supporting); OpenAI TTS / Gemini TTS (Live deepfake generation for comparison, supporting)
**AI:** Self-supervised HuBERT speech features mapped to articulatory trajectories, then handcrafted kinematic features into a gradient boosting classifier trained on about 5,800 samples; based on a 2022 academic paper idea.
**Architecture:** React/R3F frontend on Cloudflare Pages, Hono Worker proxying SSE to FastAPI endpoints on Modal that run the GPU pipeline; D1/R2/Vectorize for persistence.
**Novelty:** Explains detection with vocal-tract physics and a dramatic 3D visualization instead of a bare score; solo build.
**Scope:** large · working: Live site, health endpoint, trained model file, demo script and credits in repo; demo mode noted as enabled for reliability. · polish: Sound design, 3D effects, detailed README with accuracy and attribution.
**Claims:** 89.2 percent cross-validated accuracy across 73 TTS architectures | Example velocity above 184 cm/s versus about 20 cm/s human tip limit
**Gaps:** generalization to unseen architectures untested; repo size not in evidence
Sources: https://devpost.com/software/voxlarynx, https://github.com/Gladdonilli/hackillinois-2026, https://hackillinois-2026.devpost.com/

---

### LinkCare
*HackIllinois HackIllinois 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of Actian VectorAI DB (3rd Place) [3rd]

**What it is:** A patient-support web app (CareLink) where a person types or speaks a diagnosis, the system retrieves similar patient experiences from Actian VectorAI DB, ranks doctors with a composite score, and three AI personas vote to a consensus that can be read aloud.
**Problem / user:** Newly diagnosed patients who feel lost and want guidance from others with the same condition and stage, and from doctors those peers trust.

**Features**
- Semantic doctor recommendation (RAG) — Condition is embedded with gemini-embedding-001 and matched in HNSW collections; doctors ranked 0.45 similarity, 0.35 outcome, 0.20 sentiment. *[shown_working]*
- Multi-agent consensus engine — Clinical Specialist, Patient Advocate and Data Scientist personas run in parallel on Gemini Flash and produce an agreement score. *[shown_working]*
- Voice input — Browser audio converted with ffmpeg and transcribed by Whisper on a Modal T4 GPU, then condition extracted by Gemini. *[shown_working]*
- Spoken recommendations — ElevenLabs turbo model streams audio of the AI summary. *[shown_working]*
- Community circles — Vector collection of condition-specific posts plus a Gemini guardrail route blocking specific medical advice. *[claimed]*
- Emotional-state awareness — Consensus accepts an emotional category to tailor tone; voice-based after the face SDK failed. *[claimed]*

**Flow:** Type or speak condition → Condition is embedded and similar experiences retrieved → Doctors ranked by composite score → Three personas assess and produce agreement → Read or listen to the summary

**Prompt:** Build an AI application using Actian VectorAI DB, for example RAG, recommendation, semantic search or real-time AI; prizes quality-gated and feedback to Actian required.
**Fit (explicit):** Four HNSW cosine collections hold patient experiences, doctors, posts and emotional states, with a FastAPI gRPC bridge; retrieval drives all recommendations.  *(targeted: Best Use of Actian VectorAI DB)*
**Sponsor tools:** Actian VectorAI DB (Vector store for experiences, doctors, community posts via REST bridge, core); Modal (Whisper GPU transcription and consensus endpoint, supporting)
**AI:** Gemini embeddings (3072-d) for retrieval, Gemini Flash Lite for extraction, summaries and three-persona voting, Whisper for speech, ElevenLabs for speech output.
**Architecture:** Next.js frontend calls API routes to Modal Whisper and consensus endpoints and a FastAPI bridge over Actian gRPC running in Docker; seed scripts generate 60 experiences, 15 doctors and 20 posts.
**Novelty:** Doctor ranking from peer-experience outcomes plus a visible multi-persona disagreement, with end-to-end voice in and out.
**Scope:** medium · working: Setup scripts, schema, seeded synthetic data and API routes in repo; no live demo; data is generated. · polish: Detailed README and architecture diagram; has tests and Docker.
**Claims:** Full RAG pipeline works end to end from voice to ranked doctors
**Gaps:** seed data synthetic; no evaluation metrics
Sources: https://devpost.com/software/linkcare-2fj4ya, https://github.com/prabas007/patient-hub, https://hackillinois-2026.devpost.com/

---

### Logian
*HackIllinois HackIllinois 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of Actian VectorAI DB (2nd Place) [2nd]

**What it is:** A stock sentiment layer that continuously scrapes Yahoo Finance news, embeds it into Actian VectorAI DB, scores headlines with FinBERT and keeps precomputed per-ticker scores and BUY/SELL/HOLD labels ready for a trading engine or a live dashboard.
**Problem / user:** Algorithmic and high-frequency trading systems that cannot wait on LLM inference at decision time; also humans monitoring sentiment.

**Features**
- Background news pipeline — Async workers scrape Yahoo Finance RSS with HTML fallback and backoff, embed with MiniLM, store, then score. *[shown_working]*
- FinBERT sentiment scoring — Confidence-weighted score from -1 to 1 per ticker; above 0.3 BUY, below -0.3 SELL, else HOLD. *[shown_working]*
- Live React dashboard — WebSocket-fed cards, pipeline progress, bar and history charts, mock or live feed toggle. *[shown_working]*
- Vector search lookup tool — Local UI queries VectorAI by ticker or natural-language text with deduplicated results. *[shown_working]*
- CLI single-ticker report — python src/main.py prints score, label and top influential articles. *[shown_working]*
- Query endpoint for trading engines — /api/scores returns precomputed values; sub-millisecond retrieval is stated as a goal. *[claimed]*

**Flow:** Start Actian DB container and app → Select tickers on dashboard → Watch pipeline stages and live scores → Run semantic search over stored articles → Trading engine polls scores

**Prompt:** Build an AI application using Actian VectorAI DB, such as RAG, recommendation, semantic search or real-time AI; quality-gated prizes and feedback required.
**Fit (implied):** Uses VectorAI over gRPC for batch upserts, health checks and cosine semantic search of article embeddings alongside the sentiment pipeline.  *(targeted: Best Use of Actian VectorAI DB)*
**Sponsor tools:** Actian VectorAI DB (Stores article embeddings and serves semantic search, core)
**AI:** FinBERT for financial sentiment, sentence-transformers MiniLM for 384-d embeddings, inference in thread pools off the request path.
**Architecture:** FastAPI with asyncio workers (scrape, embed, store, score), in-memory shared state broadcast over WebSockets to a React/Vite dashboard; Actian VectorAI via gRPC in Docker.
**Novelty:** Decouples ML inference from the query path to serve precomputed sentiment, framed as a drop-in layer for trading systems.
**Scope:** medium · working: README shows CLI output and three runnable interfaces; mock feed of 1000+ synthetic articles; no live link or tests. · polish: Run script, env example, dashboard with charts.
**Claims:** Scores served instantly because inference is off the query path | Sub-millisecond query is a stated target, not measured
**Gaps:** no price-backtest of signals; scraper depends on unstable source
Sources: https://devpost.com/software/team-habs, https://github.com/bilalarif3197/LogianHackIllinois, https://hackillinois-2026.devpost.com/

---

### OpenReality
*HackIllinois HackIllinois 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Most Creative; Track: Best AI Inference (1st Place) [1st]; [MLH] Best Use of Gemini API

**What it is:** A cloud spatial-AI platform: the user states a mission, streams a phone camera through a link, and a live 3D map builds on a Modal H100 while an agent detects named targets, pins them in 3D and answers spatial questions.
**Problem / user:** First responders, search-and-rescue teams and visually impaired people who need spatial awareness without expensive LiDAR rigs or trained operators.

**Features**
- Mission-driven spatial plan — Plain-English goal becomes a typed plan of targets to find and how to move, tailored per role. *[shown_working]*
- Live 3D mapping from phone — Browser camera stream with no app builds a dense point cloud using a 1B-parameter vision SLAM model on H100. *[shown_working]*
- Continuous target detection — CLIP scoring and SAM3 segmentation scan each new submap and pin labeled objects in 3D. *[shown_working]*
- Retroactive re-search — Adding a target mid-scan re-runs detection over previously seen submaps. *[shown_working]*
- Spatial Q&A — LLM answers questions from detected objects, positions and camera path. *[shown_working]*
- Multiple input modes — Live camera, uploaded video, or folder of image frames. *[shown_working]*
- Extensible agent platform — WebSocket access and extendable agent tools; one-command Modal deployment. *[claimed]*

**Flow:** Type a mission → Receive a spatial plan → Open phone stream link and walk the space → Watch 3D map and detected pins appear → Add targets mid-scan → Ask spatial follow-up questions

**Prompt:** Modal Best AI Inference: ambitious apps running inference on Modal GPUs for real-world problems. Also Most Creative (originality) and MLH Best Use of Gemini API (apps built with Gemini).
**Fit (explicit):** README is titled around the Modal track and explains why H100 inference is required; Gemini and Claude listed as agent models.  *(targeted: Track: Best AI Inference (1st), Most Creative, [MLH] Best Use of Gemini API)*
**Sponsor tools:** Modal (H100 inference, Volumes for weights, tunnel for phone streaming, core); Gemini API (Agent reasoning among listed LLMs; exact role not stated, unclear)
**AI:** VGGT-based streaming SLAM with CLIP and SAM3 for open-vocabulary detection, plus LLM agents (Claude and Gemini listed) for planning and spatial Q&A.
**Architecture:** Phone browser streams frames to a Flask/Socket.io service on Modal H100; Three.js viewer shows the point cloud; agent layer handles planning, detection scheduling and Q&A.
**Novelty:** Brings research-grade feed-forward SLAM and open-vocabulary search to a no-install phone browser with retroactive search.
**Scope:** large · working: Live Modal demo URL, demo GIF, about 22k LOC and deploy instructions. · polish: Detailed README with architecture, multiple input modes and screenshots.
**Claims:** Deployment in about ten seconds | First inference in seconds not minutes | No hardware or app needed
**Gaps:** no accuracy metrics; which LLM does which step not stated
Sources: https://devpost.com/software/real-eyes-mra8n6, https://github.com/bdavidzhang/Open-Reality, https://hackillinois-2026.devpost.com/

---

### Sparsh Mukthi
*HackIllinois HackIllinois 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** First Place – Frostbyte Champion [1st]; Second Place – Frostbyte Runner-Up [2nd]; Special Mentions & Jury Commendations; Participation & Completion Recognition

**What it is:** A Python desktop prototype for touchless computer control by hand gestures (MediaPipe/OpenCV) and voice, with a marketing site, Firebase login and a referral-and-usage access model; the repo is a Lovable-generated React site.
**Problem / user:** Hospital and lab staff in sterile settings, elderly users, and VR users who need to avoid touch interfaces.

**Features**
- Hand-gesture control — OpenCV and MediaPipe detect hand gestures that drive mouse/keyboard actions via pyautogui/pynput. *[claimed]*
- Voice commands — speech_recognition handles commands with pyttsx3 spoken feedback. *[claimed]*
- Download website — Site sparsh-mukthi.xyz offers app download, tutorials and demo video. *[claimed]*
- Firebase login, usage and referrals — Accounts, usage tracking and referral-based access tiers in Firebase. *[claimed]*
- VR extension — Touchless gaming model in early development. *[planned]*

**Flow:** Visit website and download app → Log in → Control computer by voice or gesture

**Prompt:** not public / not found
**Fit (none):** Listed prizes refer to a different event (Frostbyte) and generic recognitions; no HackIllinois track text matches.  *(targeted: Frostbyte Champion/Runner-Up (listed))*
**AI:** MediaPipe/OpenCV gesture detection and speech recognition libraries; scikit-learn tagged but unexplained.
**Architecture:** Python desktop app with camera and microphone input mapping to OS input; Firebase backend; React/Vite marketing site.
**Novelty:** Touchless interface pitched for sterile environments with a referral-based business model.
**Scope:** small · working: Page claims macOS prototype; repo shown is a Lovable web template, not the Python app; no video link. · polish: Business slides (market, scalability); no demo evidence.
**Claims:** Working macOS voice and gesture prototype
**Gaps:** repo is website template only; prize text mismatch; no demo video
Sources: https://devpost.com/software/sparsh-mukthi-ay0cwf, https://github.com/Ishaan-Gpt/gesture-studio

---

### Superstyle
*HackIllinois HackIllinois 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Use of Supermemory; Track: Best Web API (2nd Place) [2nd]

**What it is:** A fashion platform with a consumer app (search, selfie virtual try-on, 3D avatar, voice stylist with memory) and a Stripe-style developer API plus embeddable widget that adds try-on to any e-commerce site.
**Problem / user:** Online clothing shoppers who cannot tell if an item suits them, and retailers wanting virtual try-on.

**Features**
- AI virtual try-on — Gemini image generation renders the user's selfie wearing a chosen outfit. *[claimed]*
- Voice and text stylist — ElevenLabs voice agent and OpenAI LLM recommend shoppable products found via Serper. *[claimed]*
- Style memory — Supermemory profiles and graph memory store preferences, importable across sites. *[claimed]*
- 3D avatars — Meshy.ai generates .glb avatars rendered with Three.js. *[claimed]*
- Try-on, outfit analysis and stylist APIs — REST endpoints on AWS Lambda/Hono with API keys, idempotency, rate limits, DynamoDB usage. *[claimed]*
- Embeddable widget and dev portal — One script tag adds Try On overlay; portal manages keys and analytics; docs site. *[claimed]*
- Privacy controls — Optional deletion of images after one day via S3 lifecycle. *[claimed]*

**Flow:** Sign in and upload a selfie → Search or talk to the stylist → Get product links → Click try on for a generated image → Preferences stored to memory

**Prompt:** Supermemory: use its Context Engineering APIs to build apps that remember and adapt to users. Stripe Best Web API: well-crafted API with strong developer experience, correctness and documentation.
**Fit (explicit):** Supermemory holds user profiles and graph memory; the product ships a documented, key-authenticated REST API and widget in Stripe style.  *(targeted: Best Use of Supermemory, Track: Best Web API (2nd))*
**Sponsor tools:** Supermemory (User profiles, graph memory and cross-site preference storage, core); Gemini (Clothing vision analysis and try-on image generation, core); ElevenLabs (Real-time voice stylist, supporting)
**AI:** Gemini 2.5 Flash for vision extraction and Gemini image generation for try-on; OpenAI LLM for stylist; ElevenLabs voice agent; Meshy for avatars; Supermemory for RAG.
**Architecture:** Next.js frontend and AWS Lambda Hono API with DynamoDB and S3; widget bundled by esbuild; external AI services behind the API.
**Novelty:** Pairs a consumer try-on app with a developer API and drop-in widget, with cross-site memory.
**Scope:** large · working: Live demo and docs URLs, repo and video; repo not cloned so size unknown. · polish: Developer portal, docs and widget described in detail.
**Claims:** Photorealistic try-on | Rate limit of 20 requests per day | Production-grade AWS deployment
**Gaps:** repo clone failed in evidence; no accuracy metrics
Sources: https://devpost.com/software/superstyle, https://hackillinois-2026.devpost.com/

---

### TerraGlide
*HackIllinois HackIllinois 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Track: Best Hardware Hack (John Deere Mechathon) (1st Place) [1st]; Track: Best Hardware Hack (John Deere Mechathon) (Easy Track Winner)

**What it is:** A semi-autonomous sand-leveling rover built on a SunFounder Galaxy-RVR with custom dozer and grader attachments, teleoperated from a phone or laptop, with a YOLO pedestrian safety check and ultrasonic auto-lift of the blade.
**Problem / user:** Operators of earthmoving machines in unpredictable terrain, and bystanders near active work zones.

**Features**
- Teleoperation UI — Custom React/Python UI drives the rover over Wi-Fi through an ESP32 on laptop or smartphone. *[shown_working]*
- Pedestrian safety protocol — Onboard webcam with YOLO watches the perimeter and flashes LEDs when a person gets too close. *[claimed]*
- Terrain-aware blade lift — Ultrasonic sensors detect over-digging and automatically lift the blade, overriding manual control. *[claimed]*
- Custom attachments — CAD-designed, laser-cut and 3D-printed front dozer and rear grader fitted to hand-measured mount points. *[shown_working]*
- Reverse-engineered kit protocol — Bypassed the kit's proprietary command protocol to control it from their own stack. *[claimed]*

**Flow:** Open control UI on phone or laptop → Drive rover over sand → Rover flashes LEDs if a person enters the zone → Blade lifts automatically if digging gets too deep

**Prompt:** John Deere Mechathon hardware track: recognizes the team best integrating hardware such as IoT or robotics into physical computing solutions and interactive experiences; includes an Easy Track winner.
**Fit (implied):** Earthmoving rover with safety and terrain sensing fits the construction/agriculture machinery hardware theme; Devpost reports both awards.  *(targeted: Track: Best Hardware Hack (John Deere Mechathon) 1st, Easy Track Winner)*
**AI:** YOLO object detection on the webcam feed for pedestrian detection; terrain handling uses ultrasonic thresholds rather than ML.
**Architecture:** Laptop/phone UI to ESP32 over Wi-Fi, Arduino for sensor polling and motor control, webcam and ultrasonic sensors, YOLO model on the control side.
**Novelty:** Mechanical attachments built blind from calipers, with safety interrupts layered over teleoperation.
**Scope:** small · working: Demo video of the physical rover; no repo or measurements. · polish: Custom fabricated parts and UI; page describes a sand-trap failure and fixes.
**Claims:** Parts fit on first assembly from hand-measured CAD
**Gaps:** no repo; video not watched; John Deere track PDF not read
Sources: https://devpost.com/software/terraglide-ai, https://hackillinois-2026.devpost.com/

---

### Vigilante AI
*HackIllinois HackIllinois 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of Actian VectorAI DB (1st Place) [1st]

**What it is:** A surveillance-video intelligence system: upload CCTV footage, a Modal GPU pipeline detects people, embeds and captions clips and grades threats, and a chat interface answers plain-English queries and exports incident reports.
**Problem / user:** Security teams for whom reviewing hours of multi-camera footage manually is impractical after an incident.

**Features**
- Parallel GPU video analysis — Video split into overlapping chunks processed with .map on Modal A100 running YOLO11-L, CLIP ViT-L/14 and Qwen2.5-VL-7B captioning, with Gemini vision in parallel. *[shown_working]*
- Three-stage threat classification — Alert scoring from motion, people count and label confidence yields Stage A suspicious, B concerning, C critical. *[shown_working]*
- Holistic synthesis — Gemini 2.5 Flash gives overall risk, behavioral intent and named key moments, validated so computer-vision labels outrank model text. *[shown_working]*
- Natural-language search and chat — Hybrid CLIP vector search in Actian VectorAI plus SQLite keyword search; SSE streams clips first, then narrative. *[shown_working]*
- Cross-video memory — Supermemory stores behavioral intelligence so users can ask whether behavior has been seen before. *[shown_working]*
- Incident reports — One-click TXT or PDF with timeline, severity breakdown and narrative. *[shown_working]*
- Benchmark dashboards — Shows Modal speedup, VRAM and Actian latency metrics. *[shown_working]*

**Flow:** Upload a video → Watch progress streamed → Review events and risk levels → Ask plain-English questions in chat → Download an incident report

**Prompt:** Build an AI application using Actian VectorAI DB (RAG, recommendation, semantic search, real-time AI); quality-gated prizes with feedback required.
**Fit (explicit):** Stores 768-d CLIP clip embeddings in VectorAI for semantic video search combined with keyword fallback, with a latency dashboard; README has a sponsor tracks section.  *(targeted: Best Use of Actian VectorAI DB)*
**Sponsor tools:** Actian VectorAI DB (Semantic clip search over CLIP embeddings, core); Modal (A100 parallel video processing, core); Supermemory (Cross-video behavioral memory, supporting); Gemini (Captions and risk synthesis, supporting)
**AI:** YOLO11-L detection, CLIP embeddings, Qwen2.5-VL and Gemini captions merged, Gemini 2.5 Flash synthesis with a CV-over-VLM authority rule and contextual alert phrases.
**Architecture:** React/TS frontend and FastAPI backend spawn Modal pipelines (chunk, extract); events ingested into SQLite, Actian VectorAI and Supermemory; hybrid search streams over SSE.
**Novelty:** Uses several models together and a hierarchy rule to reduce LLM under-calling; many sponsor tools combined.
**Scope:** large · working: Detailed README, tests and Docker present; repo evidence is huge (about 1.25M LOC likely includes vendored files); no demo link. · polish: Report export, dashboards, API reference in README.
**Claims:** Search merged in under 100 ms | Three networks on one A100 using about 19 GB VRAM | Built in under 48 hours
**Gaps:** no accuracy metrics; no video or demo; LOC inflated by vendored files
Sources: https://devpost.com/software/vigilante-ai, https://github.com/GALGALLOR/vigilant-ai, https://hackillinois-2026.devpost.com/

---

### Vizem Flow (the Voicepill mogger)
*HackIllinois HackIllinois 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: Best AI Inference (3rd Place) [3rd]

**What it is:** A silent speech-to-text prototype: lip geometry from video is matched to a personalized viseme reference set, converted to phonemes, and an LLM with Supermemory context turns them into a sentence, served as a Modal FastAPI endpoint.
**Problem / user:** People in libraries, meetings or noisy places where speaking to voice typing is awkward, and people with speech difficulties.

**Features**
- Lip geometry extraction — MediaPipe face landmarker per frame yields lip width, height and ratio vectors. *[shown_working]*
- Personalized viseme reference — Labeled photos of the speaker saying sounds are averaged into reference_features.json; frames match nearest viseme. *[shown_working]*
- LLM sentence decoding — Phoneme sequence plus optional Supermemory context passed to OpenAI to produce one clean sentence. *[shown_working]*
- Serverless decode API — FastAPI /decode_video on Modal accepts an MP4 and returns decoded text. *[shown_working]*
- Background any-app typing — Keypress starts capture and text types at cursor via pynput. *[claimed]*
- Per-user adaptation — Supermemory stores decodes and profile to improve over time. *[claimed]*

**Flow:** Press a key to start → Camera captures lips → Frames matched to visemes then phonemes → LLM decodes a sentence → Text appears at cursor

**Prompt:** Modal Best AI Inference: ambitious apps running inference on Modal to solve a real-world problem.
**Fit (implied):** Runs the video-to-phoneme pipeline in Modal serverless containers behind a FastAPI endpoint; Supermemory and OpenAI add decoding.  *(targeted: Track: Best AI Inference (3rd))*
**Sponsor tools:** Modal (Serverless container running decode pipeline, core); Supermemory (Per-user context and stored decodes, supporting)
**AI:** Classical geometric viseme matching from MediaPipe landmarks, then an OpenAI LLM to infer a sentence from noisy phonemes with memory context.
**Architecture:** MP4 posted to Modal FastAPI; decode_mp4 runs MediaPipe, nearest-viseme matching, phoneme sequence, Supermemory lookup, OpenAI decode, store result, return.
**Novelty:** Lipreading without a trained neural network, using personal reference photos and an LLM as the decoder.
**Scope:** tiny · working: 28 files, about 1k LOC, Mermaid architecture and setup; no demo video. · polish: Clear README with architecture; no tests; speed claim unmeasured.
**Claims:** About 5x faster than typing, unmeasured
**Gaps:** no accuracy data; no demo video
Sources: https://devpost.com/software/vizem-flow, https://github.com/Akshath-Nagulapally/lipvisemes, https://hackillinois-2026.devpost.com/

---

