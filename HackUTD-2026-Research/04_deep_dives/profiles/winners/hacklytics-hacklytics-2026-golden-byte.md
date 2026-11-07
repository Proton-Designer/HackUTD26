# Hacklytics — Hacklytics - 2026: Golden Byte (15 projects)

### A Spark in the Dark
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** First in Entertainment [1st]

**What it is:** Browser platformer with Hollow Knight-inspired hand-drawn art, controlled by hand movement tracked through the webcam (MediaPipe). A Gemini-written story is voiced by an ElevenLabs narrator across cave, forest and mountain worlds.
**Problem / user:** No stated problem; players wanting an interactive indie game with motion control and narrated story.

**Features**
- Hand-tracking control — MediaPipe maps hand motion to a platform carrying the sprite across the map. *[shown_working]*
- Obstacle dodging and timed jumps — Player avoids hazards like brambles and icicles to reach level ends. *[shown_working]*
- AI narrator — Gemini generates story text and ElevenLabs speaks it. *[claimed]*
- Three themed worlds — Cave, forest and mountain with distinct colors and obstacles (README). *[claimed]*
- Hand-drawn art — All assets drawn by team. *[shown_working]*
- Vercel deployment with server-side keys — Public site; API keys held server-side. *[shown_working]*

**Flow:** Open the site and allow webcam → Move hand to steer the platform → Dodge obstacles and time jumps → Hear narration advance the story → Finish level

**Prompt:** Entertainment track: how AI is transforming movies, gaming and interactive experiences, covering storytelling, content creation and immersive media.
**Fit (implied):** A gesture-controlled game with an AI storyteller directly matches interactive gaming and AI storytelling.  *(targeted: First in Entertainment, MLH Best Use of ElevenLabs, MLH Best Use of Gemini API)*
**Sponsor tools:** ElevenLabs (voice narration, core); Google Gemini API (story generation, core)
**AI:** Gemini generates narrative text, ElevenLabs converts it to voice; MediaPipe hand landmarks provide input.
**Architecture:** JavaScript browser game with MediaPipe hand tracking, a small API folder proxying Gemini and ElevenLabs, deployed on Vercel.
**Novelty:** Webcam hand-gesture platformer with generated narration; team says first use of APIs and motion tracking.
**Scope:** small · working: Live Vercel demo, video, seven screenshots; repo about 3,100 LOC. · polish: Hand-drawn art and world design notes; README holds only world-building notes.
**Gaps:** narrator timing not described; video not watched
Sources: https://devpost.com/software/a-spark-in-the-dark, evidence/hacklytics-hacklytics-2026-golden-byte-a-spark-in-the-dark.json, https://hacklytics-2026.devpost.com/

---

### Alleaf
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall Hack - 1st Place [1st]

**What it is:** Wearable stress-relief system: an ESP32 with an optical sensor reads RR intervals, a model estimates stress from heart rate, HRV and age, and the device triggers alternating-vibration (EMDR-style) haptics while a LangChain agent with RAG offers meditation guidance.
**Problem / user:** People with stress, anxiety or low mindfulness who want on-demand calming support.

**Features**
- Real-time stress classification — scikit-learn model trained on WESAD, served as a Flask endpoint. *[claimed]*
- Bilateral haptic stimulation — Automated alternating vibrations triggered when stress is detected. *[claimed]*
- RAG meditation and mindfulness agent — LangChain agents retrieve from Actian Vector DB. *[claimed]*
- ESP32 Bluetooth sensor — Red LED optical sensor measures RR intervals. *[claimed]*
- Next.js interface — Minimal frontend connecting to Flask API. *[claimed]*
- Progress dashboard — Tracking stress over time; listed as future work. *[planned]*

**Flow:** Wear the sensor device → Device streams heartbeat intervals over Bluetooth → Model classifies stress → Haptics trigger or agent offers a meditation

**Prompt:** Best Overall Hack: top prize across all tracks; no separate challenge text beyond general judging.
**Fit (implied):** Wearable biosensing, ML and agentic guidance addressing mental health; Actian vector store is used for retrieval.  *(targeted: Best Overall Hack, Best Use of Actian VectorAI DB (possible))*
**Sponsor tools:** Actian VectorAI DB (retrieval store for meditation RAG, supporting); Google Gemini (listed in stack, role not stated, unclear)
**AI:** Scikit-learn stress model on heart-rate features (WESAD); LangChain RAG agents over a vector DB for therapy guidance.
**Architecture:** ESP32 sensor to Bluetooth to Flask backend with model endpoint and LangChain/Actian RAG, Next.js frontend, haptic hardware output.
**Novelty:** Closes a hardware loop from biosignal to haptic therapy plus an agent; README mentions GSR while Devpost describes RR intervals.
**Scope:** medium · working: Repo with 13k LOC and Docker; Devpost claims working hardware, no live link. · polish: Polished README with feature table; no tests; video embedded.
**Gaps:** no accuracy metrics; README and Devpost differ on sensors; video not watched
Sources: https://devpost.com/software/alleaf, evidence/hacklytics-hacklytics-2026-golden-byte-alleaf.json, https://hacklytics-2026.devpost.com/

---

### BlindSpot
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Second in Finance [2nd]

**What it is:** Streamlit dashboard (repo titled TRIAGE) that scores humanitarian crisis severity per country with PCA on UN data in Databricks, allocates a user budget by severity, forecasts with XGBoost, and answers questions via Gemini plus TF-IDF retrieval of 2,388 UN documents in Actian.
**Problem / user:** Donors, journalists and UN coordinators who allocate humanitarian funds; funding follows media attention instead of severity.

**Features**
- Crisis severity score 0-100 — PCA over conflict, displacement, food insecurity, funding gap and IDP data. *[shown_working]*
- Capital allocation engine — SciPy SLSQP splits a user budget proportionally with diminishing returns. *[shown_working]*
- Lives-lost misallocation metric — Headline estimate recomputed from UN data on load. *[claimed]*
- Gemini assistant — Gemini 2.5 Flash restricted to humanitarian queries grounded in Databricks tables. *[claimed]*
- Persona briefs via RAG — Donor, Journalist and UN Coordinator briefs from UN documents in Actian VectorAI. *[claimed]*
- XGBoost forecasts — Predicts severity and funding gaps. *[claimed]*
- CSV fallback mode — Dashboard runs without the warehouse. *[claimed]*

**Flow:** Open dashboard and read misallocation metric → Browse country severity and funding gaps → Enter budget for ranked allocation → Ask the Gemini assistant → Generate persona brief

**Prompt:** Finance track: analyze market trends, predict movements and build fintech solutions, including risk analysis, fraud detection and trading strategies.
**Fit (implied):** Treats humanitarian aid as capital allocation using risk scoring and optimization, and builds on Databricks and Actian.  *(targeted: Second in Finance, Databricks Geo-Insight, Best Use of Actian VectorAI DB)*
**Sponsor tools:** Databricks (PySpark ETL, PCA scoring and live data tables, core); Actian VectorAI DB (document store for TF-IDF RAG, core); Google Gemini (domain-restricted assistant, core)
**AI:** PCA severity scoring, XGBoost forecasts, Gemini 2.5 Flash assistant, and TF-IDF bigram cosine retrieval instead of neural embeddings.
**Architecture:** Five UN datasets cleaned in Databricks, scores in Unity Catalog, Streamlit/Plotly dashboard, Actian search module and Gemini; CSV fallback offline.
**Novelty:** Reframes aid as optimization with a computed misallocation cost; uses sparse retrieval after torch embedding incompatibility.
**Scope:** medium · working: Live Streamlit app, video, repo with app, databricks and vector_rag code. · polish: Architecture diagram in README, persona outputs; no tests.
**Claims:** Every number traces to a real UN source | Corpus deduplicated from about 4,000 to 2,388 documents
**Gaps:** lives-lost methodology not given; video not watched
Sources: https://devpost.com/software/blindspot-azf0i1, evidence/hacklytics-hacklytics-2026-golden-byte-blindspot.json, https://hacklytics-2026.devpost.com/

---

### BraceML
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** First in Sports; Figma Make Most Creative Data Visualization [1st]

**What it is:** Camera-based biomechanics platform: browser, iOS and Quest 3 clients stream video to a FastAPI backend that tracks skeletons, scores injury risk and fatigue per person, runs a basketball team mode, and a sideline concussion pipeline using head velocity.
**Problem / user:** Athletes needing affordable injury screening and coaches who guess who is fatigued; sideline staff for concussions.

**Features**
- Live skeleton tracking and 12+ metrics — Webcam frames over WebSocket give knee valgus, hip drop, trunk lean and more at about 30fps. *[shown_working]*
- Injury intake and thresholds — Gemini chat builds a profile that adjusts risk thresholds. *[claimed]*
- Fatigue detection — Spectral median frequency and change-point statistics flag form decay. *[claimed]*
- Team basketball mode — Jersey and team detection, identity merging, GREEN/YELLOW/RED status per player. *[claimed]*
- Concussion pipeline — iPhone streams head landmarks; collision triggers a clip scored for velocity and impact area. *[claimed]*
- Voice coaching — ElevenLabs speaks cues. *[claimed]*
- iOS and Quest VR clients — SwiftUI and Unity apps share backend protocol. *[claimed]*
- Motion embeddings search — Actian VectorAI stores embeddings for re-identification and similarity. *[claimed]*

**Flow:** Describe past injuries to the chat agent → Start live session and see skeleton overlay → Get voice cues and risk flags → Upload workout or game footage → Review dashboard trends

**Prompt:** Sports Analytics track: player performance, game strategy and the future of sports data; optimize team decisions or enhance fan engagement.
**Fit (explicit):** Injury-risk and fatigue analytics to guide athlete and coach decisions; dashboards were designed in Figma Make.  *(targeted: First in Sports, Figma Make Most Creative Data Visualization)*
**Sponsor tools:** Google Gemini (injury intake, activity classification, jersey vision, core); ElevenLabs (spoken coaching alerts, supporting); Actian VectorAI DB (embedding similarity search, supporting); Figma Make (dashboard design, supporting)
**AI:** YOLO11 and RTMW3D pose, BoT-SORT tracking, CLIP-ReID embeddings, Isolation Forest anomalies, spectral fatigue scores; Gemini for text and vision.
**Architecture:** FastAPI backend with binary WebSocket protocol, Next.js, iOS and Quest clients, MongoDB plus Actian store, Docker Compose with CUDA or CPU profiles behind Caddy.
**Novelty:** Multi-client scope (web, iOS, VR) with team tracking and concussion detection; repo includes a gait-anomaly module with reported separation on a public dataset.
**Scope:** large · working: Live braceml.com, video, 76k LOC repo with tests. · polish: Docker, 626 tests claimed, three clients; thresholds not clinically validated.
**Claims:** 130-260 ms end-to-end latency | 626 tests across 32 test files | 70s NBA clip 30+ IDs merged to 10 players | VR bandwidth cut about 10x
**Gaps:** README covers only gait-anomaly core, not full platform; 35% earlier-warning claim not validated
Sources: https://devpost.com/software/braceml, evidence/hacklytics-hacklytics-2026-golden-byte-braceml.json, https://hacklytics-2026.devpost.com/

---

### Conduit
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Second in Healthcare [2nd]

**What it is:** Accessibility layer that converts four input types, voice, EEG from a Muse headband, webcam eye tracking and ASL hand signs, into standard computer input events in an Electron app, with a shared event schema and visualization tab.
**Problem / user:** People who cannot use a mouse, keyboard or screen conventionally; cites over 30% of disabled people.

**Features**
- Voice commands — ElevenLabs transcribes speech and Gemini interprets commands. *[claimed]*
- EEG mouse intent — Muse EEG windows, band-filtered features, binary intent classifier with vote smoothing. *[claimed]*
- Eye-tracking cursor — Face and iris landmarks, 3D sphere calibration, One Euro filter. *[claimed]*
- ASL letter recognition — Custom MobileNetV2 with channel attention, smoothed predictions emit keystrokes. *[claimed]*
- Unified event pipeline — All modalities emit one canonical event schema, run concurrently. *[claimed]*
- Visualization tab — Heatmap, EEG waves and ASL visualizer. *[shown_working]*

**Flow:** Launch Electron app and calibrate eye tracking → Choose or combine modalities → Speak, gaze, think or sign → Events control mouse and keyboard → Watch visualizations

**Prompt:** Healthcare track: bioinformatics, patient care and personal health technology for better outcomes, decisions and access.
**Fit (implied):** Assistive technology giving disabled users computer access through biosignals and vision, a personal-health and care-accessibility angle.  *(targeted: Second in Healthcare, MLH ElevenLabs and Gemini (possible))*
**Sponsor tools:** ElevenLabs (speech transcription, core); Google Gemini (command interpretation, core)
**AI:** Custom MobileNetV2 ASL classifier, EEG intent classifier, iris-landmark gaze geometry, Gemini intent parsing.
**Architecture:** Electron/TypeScript frontend, FastAPI Python backend, separate modules for ASL, eye gaze, EEG and voice emitting events to a camera broker.
**Novelty:** Four simultaneous modalities including consumer EEG and ASL in one event schema; team notes latency mismatch of gaze versus speech.
**Scope:** large · working: Embedded demo video; repo 24k LOC with tests across ASLCV, eyegaze, muse, VoiceTTS. · polish: Calibration and visualization UIs; README is a title only.
**Claims:** Gaze responsiveness under 50 ms | Speech-to-text 300-800 ms | ASL classifier recognizes all 26 letters
**Gaps:** no accuracy metrics; README empty; video not watched
Sources: https://devpost.com/software/conduit-y8gqoj, evidence/hacklytics-hacklytics-2026-golden-byte-conduit.json, https://hacklytics-2026.devpost.com/

---

### Crisis Averted
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 3rd Overall Hack [3rd]

**What it is:** A 3D globe command center (Crisis Topography) that renders humanitarian funding gaps as raised terrain and is driven by a voice agent named Pablo, who flies the camera to regions and speaks intelligence briefings built from structured and vector queries.
**Problem / user:** Aid allocation is reactive and sentiment-driven; intended for funders, crisis managers and responders (UN-type organizations named as future users) who need to see where need outpaces funding.

**Features**
- 3D globe with funding-gap extrusion — A Severity-to-Funding Gap Ratio is computed per region and drawn as raised geometry on a Three.js globe *[claimed]*
- Voice-only agent Pablo — Speech is cleaned by ElevenLabs Voice Isolator, then Gemini function-calls to drive the app and answer *[claimed]*
- Voice-commanded camera flights — Requests like going to a country border make the globe fly there and adjust altitude and glow *[claimed]*
- Text-to-SQL analysis on Databricks — Questions become SQL run against Databricks Genie Spaces over HAPI humanitarian data *[claimed]*
- Semantic search over aid projects — Thousands of project descriptions embedded with all-mpnet-base-v2 and searched in Actian Vector DB *[claimed]*
- Spoken intelligence briefings — Gemini Flash turns anomaly scores and ROI deltas into a narrative voiced via ElevenLabs *[claimed]*
- Kafka command and result buses — Two streams carry UI commands out and aggregated results back to keep globe and narrator in sync *[claimed]*
- Predictive risk models for migration/famine — Listed as future work *[planned]*

**Flow:** User speaks a request to Pablo → Audio is denoised and sent to Gemini for function calling → Command goes via Kafka to the globe and backend → Databricks SQL and Actian vector search run in parallel → Results are merged and Gemini writes a briefing → ElevenLabs speaks it while the globe moves and extrudes gaps

**Prompt:** Overall prize ranks the best hack across all tracks (1st/2nd/3rd); no overall-specific criteria are given on the hackathon page, which lists finance, sports, healthcare, entertainment and imagination tracks plus sponsor prizes.
**Fit (implied):** README badges and sections credit Databricks, Actian, Vultr and ElevenLabs; the project spans data engineering, voice agent and 3D visualization, an overall-scope build.  *(targeted: 3rd Overall Hack, Databricks Geo-Insight, Actian VectorAI DB, ElevenLabs, Vultr)*
**Sponsor tools:** Databricks (Lakehouse ingestion of HAPI data and Genie text-to-SQL, core); Actian Vector DB (semantic search over embedded aid projects, hosted on Vultr, core); ElevenLabs (voice isolation and spoken output via WebRTC agent, core); Vultr (high-compute VMs hosting backend and vector DB, supporting); Gemini (function-calling orchestrator and briefing writer, core)
**AI:** Gemini Pro does function calling to turn speech into commands; Gemini Flash writes briefings; Databricks Genie generates SQL; mpnet embeddings feed Actian retrieval; Llama/Qwen listed without clear role.
**Architecture:** Next.js/react-globe.gl frontend; FastAPI backend; voice in through ElevenLabs to Gemini; commands over Kafka to client and to Databricks plus Actian; results aggregated on a second Kafka stream; narrative to ElevenLabs.
**Novelty:** Turns a funding-gap metric into physical globe terrain and puts the whole interface behind a voice agent, combined with a Kafka event bus and a self-hosted vector DB on a large Vultr cluster.
**Scope:** large · working: Repo of about 110 files and 11.7k LOC with frontend, backend, Databricks and docs; no live link; demo video exists. · polish: Extensive README with mermaid diagram and phase breakdown; no tests, CI or Docker in repo.
**Claims:** Embeds 18,000+ humanitarian projects (README says 8,000+) | Sub-100ms vector similarity search | Sub-second voice loop and sub-millisecond Kafka dispatch (self-reported) | Gemini 3.0 per Devpost vs Gemini 1.5 per README
**Gaps:** video not watched; no benchmark data; Llama/Qwen role unstated; README vs Devpost disagree on model versions and project count
Sources: https://devpost.com/software/crisis-averted, evidence/hacklytics-hacklytics-2026-golden-byte-crisis-averted.json, prompts_cache/hacklytics-2026.md

---

### DarkHorse
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Third in Sports [3rd]

**What it is:** A World Cup match tool that produces a DarkScore for each matchup, an upset-likelihood number built from Elo gaps, team and player aggregate features and historical results, served by a React app and FastAPI XGBoost backend.
**Problem / user:** Favorites usually win but some matches are quietly unstable; aimed at fans and analysts who want to spot high-impact upset-prone games before kickoff.

**Features**
- Matchup tool with DarkScore — User picks two teams and the backend returns win and upset probabilities plus a score *[shown_working]*
- Readable score tiers and contributors — Score is explained through tiers and 'Dark Knight' contributor factors *[claimed]*
- Team roster overview and detail — Pages list nations and per-team rosters from generated static artifacts *[shown_working]*
- Player radar charts — Six-axis charts (pace, shooting, passing, dribbling, defending, physical) per player *[claimed]*
- Top-upset players and goalkeeper wall ranking — API endpoints rank players by upset impact and goalkeepers by wall rating *[claimed]*
- Supabase authenticated profile and dashboard — Login plus profile pages in the frontend *[claimed]*
- 2026 group-stage probability tables — Precomputed win/upset probabilities and simulated standings used as data *[claimed]*

**Flow:** Sign in via Supabase → Open the matchup page → Choose two nations → Backend predicts and returns DarkScore with tier → Browse rosters and player radar views

**Prompt:** Sports Analytics track: player performance, game strategy and the future of sports data; optimize team decisions or enhance fan engagement.
**Fit (explicit):** Predicts upset risk for World Cup matches from Elo, matchup and player features, giving fans a pre-kickoff decision signal; README has a Sphinx usage section.  *(targeted: Sports track, Sphinx)*
**Sponsor tools:** Sphinx (helped engineer the DarkScore formula and build player radar visualizations, supporting)
**AI:** XGBoost model trained on scraped 2018 and 2022 World Cup matchup data with Elo differentials and FC26 player aggregates to score upset likelihood.
**Architecture:** Vite React frontend on Vercel with Supabase auth; FastAPI backend on Render with CSV datasets and a trained model; static roster artifacts generated into public/data.
**Novelty:** Frames prediction as an upset-risk score instead of a winner pick, and draws on video-game player ratings as features.
**Scope:** medium · working: Live Vercel site, deployed backend config and 187-file repo with about 12.9k LOC and endpoint list. · polish: README documents setup, deploy, endpoints and datasets; no tests or CI.
**Claims:** No accuracy or backtest numbers reported
**Gaps:** Devpost has no walkthrough, challenges or next steps; model metrics absent
Sources: https://devpost.com/software/darkhorse, evidence/hacklytics-hacklytics-2026-golden-byte-darkhorse.json, prompts_cache/hacklytics-2026.md

---

### DataFables
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Third in Entertainment [3rd]

**What it is:** A pixel-art kids' storybook web app where a child designs a character, picks a topic, age and language, and gets an illustrated branching story written by Gemini from Snowflake-stored facts, screened for safety and read aloud.
**Problem / user:** Children's games favor entertainment over learning; targets young kids, with parents and teachers implied as later users via planned dashboards.

**Features**
- Personalized branching stories — Gemini writes multi-page stories with choices from topic, age range, genre and custom protagonist *[shown_working]*
- Snowflake-grounded facts — Verified educational facts for the topic and age are fetched from Snowflake and fed into generation *[claimed]*
- Pixel-art character designer — Hair, skin, outfit, shoes and accessories are chosen in a chibi designer *[shown_working]*
- ElevenLabs narration in 10 languages — Each page can be voiced on demand; UI and story text also localized *[claimed]*
- Pronunciation practice and struggle-word recall — Feedback on spoken words, with Actian VectorAI semantic recall for later vocabulary reinforcement (Devpost) *[claimed]*
- Child-safety screening — SafetyKit moderates each story, with Gemini fallback, and a safety badge is shown *[shown_working]*
- Similar-story recommendations — Titles and topics are embedded and top 3 matches shown after a story (README) *[claimed]*
- XP, coins, badges and shop — Reading earns rewards that unlock character items *[shown_working]*

**Flow:** Design a character → Enter topic, choose age range, genre and language → Facts retrieved and Gemini generates story with images → Safety check runs → Read and make branching choices, listen to narration → Earn XP and coins, spend in shop

**Prompt:** Entertainment track: how AI is transforming movies, gaming, interactive experiences, storytelling, content creation and immersive media.
**Fit (implied):** Interactive AI storytelling game for children with generated art, voice and gamified rewards; several sponsor tools are wired into the pipeline.  *(targeted: Entertainment track, Snowflake, ElevenLabs, Actian VectorAI DB, SafetyKit, Gemini)*
**Sponsor tools:** Snowflake (stores facts and story data, Cortex fact retrieval to ground stories, core); ElevenLabs (multilingual narration, core); SafetyKit (child-safety moderation of stories, supporting); Actian VectorAI (vector similarity for recommendations and struggle words, supporting); Gemini (story and image generation, core)
**AI:** Gemini generates branching stories and illustrations grounded in retrieved facts and adapts tone per age and language; sentence-transformer embeddings in Actian drive recommendations; safety moderation gates output.
**Architecture:** Next.js 15 app with API routes for generate, narrate and recommend; Snowflake REST for facts; Python FastAPI proxy to a Dockerized Actian VectorAI DB; SafetyKit call before display.
**Novelty:** Combines fact-grounded generation, 10-language support, pronunciation feedback and a game economy in one kids' product with a cohesive Stardew-style pixel look.
**Scope:** medium · working: Repo of 66 files, about 8.4k LOC with API routes and components; no live link. · polish: Custom pixel-art assets, README with flow and structure; Docker for Actian only; no tests.
**Claims:** Stories generated in the child's own language across 10 languages | Topic to narrated story pipeline 'in seconds'
**Gaps:** video link not on Devpost page; README does not mention pronunciation practice that Devpost lists; README calls Actian use similar-story recommendation while Devpost says struggle-word recall
Sources: https://devpost.com/software/hacklytics-2026, evidence/hacklytics-hacklytics-2026-golden-byte-datafables.json, prompts_cache/hacklytics-2026.md

---

### HeartScape
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Third in Healthcare [3rd]

**What it is:** A browser 3D viewer that turns segmented pediatric cardiac MRI (HVSMR-2.0) into rotatable heart meshes, places each patient in a PCA morphology space against 60 annotated congenital cases, and offers a Gemini 'Lens' that explains selected regions.
**Problem / user:** Reading congenital heart disease from 2D MRI slices is slow and unintuitive; aimed at students, researchers, clinicians and patients wanting awareness.

**Features**
- Interactive 3D heart models — Segmented NIfTI scans become marching-cubes meshes viewed in Three.js with rotate, zoom and slicing slider *[shown_working]*
- Healthy vs diseased comparison — Side-by-side meshes and a distance-based difference visualization *[claimed]*
- PCA morphology landscape — Chamber and vessel volumes in mL are scaled and projected to 2D PCA; nearest neighbors and a severity score from PC1 *[shown_working]*
- Vector-search soft diagnosis — Actian VectorAI holds six collections of volume vectors; six parallel searches give condition attribution via softmax over distances *[claimed]*
- Condition simulation via mesh morphing — Condition effect multipliers deform the reference heart to simulate named conditions *[claimed]*
- AI Lens region explainer — User drags a selection and Gemini 2.5 returns an educational explanation in an overlay *[claimed]*
- Annotation tools — Comment pins, sticky notes and 3D drawings placed on the model *[claimed]*
- Sphinx notebooks for mesh distance — Rigid ICP alignment and nearest-neighbor distance heatmaps exported as Plotly *[claimed]*

**Flow:** Open a healthy or congenital heart model → Rotate, zoom and slice → Compare against a diseased model or distance map → Upload a scan to see nearest patients and attribution → Drag a region to open the Lens explanation → Add annotations

**Prompt:** Healthcare track: bioinformatics, patient care and personal health technology aimed at better outcomes, medical decision-making and care accessibility.
**Fit (implied):** Makes congenital heart anatomy explorable and comparable in 3D with patient-similarity retrieval and AI explanations, supporting education and decision support.  *(targeted: Healthcare track, Actian VectorAI DB, Sphinx, Gemini)*
**Sponsor tools:** Actian VectorAI (six-collection volume-vector search for patient matching and attribution, core); Sphinx.AI (generated analysis notebooks for ICP and distance heatmaps, supporting); Gemini (Lens region explanations, supporting)
**AI:** Not learned embeddings: vectors are volumetric measurements compared by Euclidean distance after z-scoring; PCA gives severity; Gemini 2.5 explains selected regions.
**Architecture:** Flask API with PyVista mesh export, scikit-learn PCA and VectorAI client; static Three.js frontend (index.html, heart-scene.js, lens-module.js) consuming OBJ meshes and API results.
**Novelty:** Brings rarely available congenital-heart 3D models into the browser and uses simple volumetric vectors with vector search for soft attribution; team switched from cosine to Euclidean after cosine failed.
**Scope:** medium · working: 37-file repo, about 6k LOC with pipeline, trained PCA files and holdout patients; demo video. · polish: Detailed README with pipeline and dataset tables; no tests, CI or live link.
**Claims:** Uses 60 annotated CHD patients across 15+ condition categories | Five holdout patients kept unseen for demo | No clinical accuracy metrics reported
**Gaps:** README read only to ~7000 chars; video not watched
Sources: https://devpost.com/software/heartscape, evidence/hacklytics-hacklytics-2026-golden-byte-heartscape.json, prompts_cache/hacklytics-2026.md

---

### Lumos AI
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 2nd Overall Hack [2nd]

**What it is:** A web and PWA safety platform that gives any US address a 0-100 safety score from an XGBoost model on FBI NIBRS agency profiles, blended with live incidents, weather and events, plus safest-route comparison and an AI voice agent that can place a 911 call.
**Problem / user:** Safety apps say only 'high crime area' without crime types or timing, and people in danger may be unable to speak to dispatch; aimed at travelers, students, joggers and anyone needing emergency help.

**Features**
- Location safety score — 25-feature XGBoost regression blended 60/40 with a formula fallback, gives 0-100 for an address or coordinate *[shown_working]*
- Crime-type breakdown and 24-hour risk timeline — Predicted offense types ranked by probability with hourly multipliers from BJS tables *[claimed]*
- Crime heatmap globe — Mapbox 3D map seeded from Socrata open data and NIBRS distributions *[shown_working]*
- Live incident adjustment — Citizen app incidents lower the score by distance, recency, severity and credibility, capped at 25 points *[claimed]*
- Safest route comparison — Up to three Google Routes alternatives scored and the safest recommended *[claimed]*
- Gemini safety tips and chat bot — Context-aware tips and persistent chat using location, time, weather and crime profile *[claimed]*
- AI 911 voice operator — VAPI call with prefilled medical profile, live GPS streaming, typed mid-call messages, 50+ country numbers *[claimed]*
- Nearby safety centers and weather context — Aggregates nearby services, NWS and OpenWeatherMap data, Ticketmaster events *[claimed]*

**Flow:** Search an address or landmark → See score, crime breakdown, timeline and heatmap → Plan a route and compare safety → View live incidents and nearby safety centers → Ask the Lumos bot for tips → In an emergency start the voice AI to place the call

**Prompt:** Overall prize ranks the best hack across all tracks (1st/2nd/3rd); no overall-specific criteria are stated on the hackathon page.
**Fit (implied):** Full-stack data-science product combining a large FBI data pipeline, a trained model, live feeds and an emergency voice agent; built-with tags show sponsor tools.  *(targeted: 2nd Overall Hack, Vultr, ElevenLabs, Gemini)*
**Sponsor tools:** Vultr (hosts the FastAPI backend, supporting); ElevenLabs (text-to-speech for the emergency voice agent, supporting); Gemini (score sanity check, chat, descriptions and the voice agent LLM, core)
**AI:** XGBoost trained on sigmoid-calibrated crime-rate labels with 25 features; Gemini 2.5 Flash post-checks scores, writes tips and powers the 911 call through VAPI with ElevenLabs speech.
**Architecture:** React/Vite frontend on Netlify; async FastAPI on Vultr fans out 11 parallel API calls; precomputed NIBRS profiles; Firebase Cloud Functions bridge VAPI telephony with Realtime DB GPS context.
**Novelty:** Unusually heavy data work (tens of GB of NIBRS reduced to agency profiles, 30+ city portals) plus a working emergency-call agent in a consumer safety map.
**Scope:** large · working: Live Netlify demo, 171-file repo with about 23k LOC and tests, backend API reference. · polish: Elaborate README with badges, ToC, API reference and troubleshooting; PWA; no CI or Docker.
**Claims:** 48 GB raw NIBRS reduced to 43 MB across 7,717 agency profiles | 136,626 cities covered with 4-tier fallback | Sub-second scoring; enriched responses under 2 seconds (page says both) | Covers every US address (broad claim, no validation shown)
**Gaps:** no video on Devpost; no accuracy validation; 911 calling not independently shown
Sources: https://devpost.com/software/lumos-ai, evidence/hacklytics-hacklytics-2026-golden-byte-lumos-ai.json, prompts_cache/hacklytics-2026.md

---

### MomentumShift
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Second in Sports [2nd]

**What it is:** An NBA analytics web app that charts game momentum as it shifts, predicts upcoming scoring runs with scikit-learn models, and finds historical games with similar momentum patterns ('Game DNA'), backed by a FastAPI service and Supabase.
**Problem / user:** Traditional box-score stats miss momentum swings; README targets fans, analysts and coaches wanting deeper game-flow insight.

**Features**
- Real-time momentum chart — Color-coded home/away momentum line refreshed about every 15 seconds with play tooltips (README) *[claimed]*
- Run predictor — ML model flags a likely scoring run above 60% probability with high/medium/low confidence, refreshed about every 30 seconds *[claimed]*
- Game DNA pattern matcher — Cosine similarity compares current momentum to historical games and lists top 3 matches with possible outcomes *[claimed]*
- Play-by-play feed — Live event list showing each play's momentum impact, colored by team *[claimed]*
- AI game intelligence narratives — Generated text about game flow (README lists it) *[unclear]*
- Interactive time-period analysis — User selects spans of the game to inspect *[claimed]*

**Flow:** Open a game → Watch momentum chart update → See run-prediction alerts → Check top similar historical games → Scan play-by-play feed

**Prompt:** Sports Analytics track: player performance, game strategy and the future of sports data; optimize team decisions or enhance fan engagement.
**Fit (implied):** Quantifies in-game momentum and predicts scoring runs for fans, analysts and coaches.  *(targeted: Sports track)*
**AI:** Proprietary momentum score from play data; scikit-learn models predict runs; cosine similarity matches historical game momentum patterns.
**Architecture:** React/TypeScript frontend, Node proxy, Python FastAPI backend with scikit-learn, Supabase for stored games, NBA play data feed.
**Novelty:** Focuses on a derived momentum metric with predictive alerts and historical lookalike matching rather than raw stat display.
**Scope:** small · working: 44-file repo, about 2.7k LOC with setup steps; no live link or video. · polish: Clear README with feature sections; Devpost thin; no tests.
**Claims:** No quantitative results reported | Compares to 'thousands' of historical games (README)
**Gaps:** no demo or video; NBA API deprecation noted as challenge; live data status unclear
Sources: https://devpost.com/software/momentumshift, evidence/hacklytics-hacklytics-2026-golden-byte-momentumshift.json, https://raw.githubusercontent.com/rishyendra333/hacklytics-2026/main/momentum-shift/README.md, prompts_cache/hacklytics-2026.md

---

### Nexus
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Third in Finance [3rd]

**What it is:** A finance dashboard with a Mapbox 3D globe that shows how news events spread as market shocks across countries, sectors and S&P 100 stocks, with LSTM price forecasts, a RAG analyst chat and a what-if event simulator.
**Problem / user:** Headlines about outages, export limits and strikes are read in isolation although they move markets; aimed at learners and, later, institutional desks lacking expensive terminals.

**Features**
- Shockwave globe — Mapbox GL layers draw shock heatmaps, stock dots and arcs from event origin to affected places *[shown_working]*
- Composite shock scoring — Each tracked stock scored from semantic similarity, historical sensitivity, geography and supply-chain links *[claimed]*
- Event classification pipeline — Custom BART-MNLI zero-shot classifier on ingested news, with fallback to OpenAI then stubs *[claimed]*
- Per-ticker LSTM forecasts — 117 LSTM models give price predictions with Monte Carlo confidence bands over OHLC charts *[claimed]*
- What-if simulation — Modal for hypothetical geopolitical events; results streamed in staggered socket updates *[shown_working]*
- RAG financial analyst chat — SSE-streamed chat panel grounded in live market data and Actian vector retrieval *[claimed]*
- OSINT image upload — Drag-and-drop satellite or CCTV image analysis through OpenAI Vision (README) *[claimed]*
- Search, ticker bar and sector panel — Cmd+K search, scrolling quotes, stocks grouped by sector with impact scores *[shown_working]*

**Flow:** Open dashboard and watch globe and ticker → Click events or stocks to see shock scores and sector breakdown → View stock chart with AI prediction overlay → Run a what-if event in the simulation form → Ask the AI analyst in the chat panel

**Prompt:** Finance track: analyze market trends, predict stock movements, build fintech solutions, including risk analysis, fraud detection and trading strategies.
**Fit (explicit):** Predicts stock-level impact of news and geopolitical events with forecasts and simulation; README states it was built for the Finance track.  *(targeted: Finance track, Actian VectorAI DB, Sphinx)*
**Sponsor tools:** Actian VectorAI DB (vector similarity and historical event matching via FastAPI gRPC proxy, supporting); Sphinx (NLP orchestration layer with fallback cascade (Devpost), supporting)
**AI:** BART-large-MNLI zero-shot event classification, MiniLM embeddings for similarity search, 117 LSTMs with Monte Carlo intervals, RAG chat, OpenAI fallback and vision for images.
**Architecture:** Vite React frontend (this repo) with Socket.io; NestJS backend with 16 modules; Python model server; FastAPI proxy to Actian; AWS ECS Fargate, CloudFront and CDK.
**Novelty:** Links geopolitical news to per-stock shock scores on a globe, with self-trained classifier to avoid API latency and LSTMs trained on a university supercomputer cluster.
**Scope:** large · working: Live CloudFront demo, separate frontend and backend repos, Playwright tests, GitHub Actions deploy to S3; frontend alone about 5.6k LOC. · polish: Designed terminal aesthetic, README with layout diagram and graceful mock-data fallback.
**Claims:** Sub-100ms classifier inference versus 200-500ms for OpenAI | 117 per-ticker LSTM models | Fargate 'millions of vector comparisons per second' (unmeasured) | Only the frontend repo was in evidence; backend repo is separate
**Gaps:** backend repo README not read; video not watched
Sources: https://devpost.com/software/nexus-6tr249, evidence/hacklytics-hacklytics-2026-golden-byte-nexus.json, prompts_cache/hacklytics-2026.md

---

### Tempr
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Second in Entertainment [2nd]

**What it is:** An Expo React Native app that logs into Spotify, takes a mood typed as text or shown in a photo, has Gemini turn it into a target vibe, and builds a queue from the user's own liked songs, plus calendar-driven playlists and a Discover swipe feed.
**Problem / user:** Listeners with big liked-song libraries struggle to pick music for a moment ('choice paralysis'); aimed at Spotify users wanting mood- or event-matched queues.

**Features**
- Mood to queue from text or image — Gemini interprets the prompt or photo into suggestions and a vibe vector, matched to liked songs *[claimed]*
- Audio-feature matching — Tracks embedded by acousticness, danceability, energy and valence, ranked by cosine similarity to the target *[claimed]*
- Add to Spotify queue — Matched tracks are searched in batches and pushed to the Spotify playback queue *[claimed]*
- Calendar-driven playlists — Upcoming events get generated playlists and a notification 10 minutes before they start *[claimed]*
- Memories library — Past queues saved and re-added to Spotify with one tap *[claimed]*
- Discover feed — Swipe to like tracks with YouTube video previews *[claimed]*
- Spotify login through Supabase — OAuth with deep-link redirect and session handling (README setup) *[shown_working]*
- Caching and retry states — AsyncStorage for queues, likes and previews; retry UI when APIs fail *[claimed]*

**Flow:** Log in with Spotify → Type a mood or upload a photo → Wait up to ~30 seconds for generation → Queue is added to Spotify and can be saved to Memories → Connect calendar for per-event playlists → Swipe in Discover

**Prompt:** Entertainment track: how AI is transforming movies, gaming, interactive experiences, storytelling, content creation and immersive media.
**Fit (implied):** Uses generative AI to personalize music listening from mood, image and calendar context.  *(targeted: Entertainment track)*
**AI:** Gemini converts text or image into queue suggestions and a vibe vector with strict prompt formatting; cosine similarity over Spotify audio features ranks liked songs.
**Architecture:** Expo/TypeScript app with expo-router; Supabase Auth for Spotify OAuth; Spotify Web API, Gemini API, Apple Calendar and YouTube Data API; AsyncStorage cache.
**Novelty:** Grounds generation in the user's own liked songs and accepts photos and calendar events as mood inputs.
**Scope:** medium · working: Demo video and 48-file repo of about 7.3k LOC with tests; README covers only auth setup. · polish: Mobile UI with several tabs per Devpost; README thin on features; no CI.
**Claims:** No quantitative metrics | Generation can take up to 30 seconds
**Gaps:** README documents only login/setup and not the queue features Devpost lists; video not watched
Sources: https://devpost.com/software/tempr, evidence/hacklytics-hacklytics-2026-golden-byte-tempr.json, prompts_cache/hacklytics-2026.md

---

### Veritais
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** First in Finance [1st]

**What it is:** A multimodal pipeline that finds executive videos on YouTube, extracts verifiable claims, scores each speaker's facial action units and vocal features against their own baseline, checks the claims later against public sources, and publishes a per-company Truth Index and CEO leaderboard.
**Problem / user:** Executives can mislead investors and the cues are hard to spot; aimed at retail investors and journalists who lack analysts' informal tools.

**Features**
- Automated video discovery — LLM-generated topics and relevance judging scrape YouTube for executive statements *[claimed]*
- Speaker identification — Whisper V3 transcripts plus a RAG agent and face/voice fingerprints in a vector database *[claimed]*
- Proposition extraction — Pulls verifiable claims from transcripts and links them to frames via a vision-language model *[claimed]*
- Facial and vocal feature scoring — Action Units at 2 fps and prosody/voice-quality measures, normalized to each speaker's own baseline *[claimed]*
- Claim verification loop — Agentic LLM with web search checks claims against filings and earnings, rechecking later ones *[claimed]*
- Learned conviction score — Classifier fuses facial and audio signals per statement, weights updated by Bayesian average *[claimed]*
- Truth Index and leaderboard — Recency-weighted accuracy per company, ranked CEO list and timeline graph *[shown_working]*
- Live inference on new streams — Scores statements on new video; streaming near-real-time scoring listed as next step *[planned]*

**Flow:** System discovers and transcribes executive videos → Speaker and claims are extracted → Behavioral signals scored per statement → Claims verified later against public sources → User views leaderboard and Truth Index graph

**Prompt:** Finance track: analyze market trends, predict stock movements, build fintech solutions; also risk analysis, fraud detection and trading strategies.
**Fit (implied):** Treats executive honesty as an investor-risk signal, scoring statements and tracking outcomes per company.  *(targeted: Finance track)*
**AI:** Whisper V3 transcription, LLM agents for discovery, speaker inference and verification, a vision-language model, PyFeat and librosa/Praat features, and a scikit-learn composite classifier with Bayesian weight updates.
**Architecture:** Staged backend pipeline (discovery, transcription and fingerprinting, proposition extraction, feature analysis, verification) in Python/FastAPI; Next.js frontend with leaderboard and graphs; vector DB for fingerprints.
**Novelty:** Frames deception as behavior-versus-later-outcome learning with within-person baselines rather than binary lie detection; grounded in earnings-call research.
**Scope:** large · working: Hosted demo site, 114-file repo with about 13.9k LOC and tests; Devpost shows only a homepage screenshot. · polish: README is only a short description with architecture image; Devpost is detailed; no live metrics shown.
**Claims:** About 4,000 hours of recordings used in baseline work | No accuracy or benchmark results reported | Uses only public data
**Gaps:** README minimal; no accuracy numbers; demo site not opened
Sources: https://devpost.com/software/veritais, evidence/hacklytics-hacklytics-2026-golden-byte-veritais.json, https://raw.githubusercontent.com/8pxl/veritas/main/README.md, prompts_cache/hacklytics-2026.md

---

### Vigil
*Hacklytics Hacklytics - 2026: Golden Byte · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** First in Healthcare [1st]

**What it is:** An event-safety prototype that pairs a Galaxy Watch (heart rate and vitals) with camera-based posture analysis on a server to detect fainting or dizziness in at-risk attendees, then alerts staff through a companion app with location and an AI-written incident summary.
**Problem / user:** People with conditions such as POTS risk fainting in long, crowded event lines where response is slow; aimed at at-risk attendees and event medical staff.

**Features**
- Wearable vitals monitoring — Wear OS app reads heart rate and other metrics via Health Connect and Data Layer and alerts the wearer *[claimed]*
- Camera person detection and tracking — YOLOv8 Nano with ByteTrack finds and follows people in the video stream *[shown_working]*
- Posture and collapse analysis — Pose estimation plus a custom LSTM and anomaly classifier flag fall, collapse or erratic motion *[claimed]*
- Wearable and vision fusion — Alerts fire only when both signal types agree, reducing false positives *[claimed]*
- BLE localization — Raspberry Pi units use RSSI and UUID from staff phones' advertising to place the attendee without personal identifiers *[claimed]*
- Staff alerting app — Flutter/Android app shows dashboard, camera feed overlay and incident report with location *[claimed]*
- AI incident summary — LLM writes a real-time report for medics; Devpost says Gemini, README says GPT with email via SMTP *[claimed]*

**Flow:** Attendee wears the watch → Camera streams to the central server → Models detect person, movement and anomaly → Wearable and vision signals are fused → Staff app receives alert with location → AI summary helps medics respond

**Prompt:** Healthcare track: bioinformatics, patient care and personal health technology aimed at better outcomes, medical decision-making and care accessibility.
**Fit (implied):** Personal health technology that detects collapse risk in people with conditions like POTS and speeds medical response at events.  *(targeted: Healthcare track)*
**AI:** YOLOv8 Nano detection, ByteTrack, MediaPipe pose, a custom PyTorch LSTM trained on team-recorded data, rule-based anomaly checks, and an LLM report writer.
**Architecture:** Galaxy Watch to Flutter/Kotlin phone app; camera frames over WebSocket to a FastAPI CV backend (Dockerized) with detector, tracker, pose and anomaly modules; Raspberry Pi BLE localization; LLM report endpoint.
**Novelty:** Hardware-heavy build combining watch, Raspberry Pi, camera and BLE localization into one fused alerting loop for a specific medical condition.
**Scope:** large · working: 219-file repo with Flutter app, Wear OS code, CV backend and Pi files; demo video; Devpost calls it a working end-to-end prototype. · polish: README with architecture and setup; some placeholder package names; no CI; no metrics.
**Claims:** Working end-to-end prototype across watch, Pi, server and phone | Aims for HIPAA compliance and affordable hardware (stated goals) | No accuracy or false-positive figures
**Gaps:** README lacks watch Pi and LSTM detail; README names OpenAI and MediaPipe, Devpost names Gemini; video not watched
Sources: https://devpost.com/software/vigil-b8uatr, evidence/hacklytics-hacklytics-2026-golden-byte-vigil.json, prompts_cache/hacklytics-2026.md

---

