# HackGT — HackGT 11 (19 projects)

### 90°
*HackGT HackGT 11 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner Best Use of MATLAB

**What it is:** A mobile photo-assistant: a person sorts and likes photos of themselves in categories, a classifier learns which angles they prefer, and the camera view then shows on-screen guidelines so a friend taking the photo frames shots the way the subject likes.
**Problem / user:** Anyone who hands their phone to a friend for photos and gets unusable angles, and finds it awkward to explain what they want.

**Features**
- Accounts and photo categories — Email signup; upload photos into pre-made (full body, half body) or custom categories; stored in MongoDB and S3. *[claimed]*
- Like-based preference learning — Liked photos become labelled good/bad data for the angle classifier. *[claimed]*
- Angle classifier in MATLAB — Pretrained AlexNet fc7 features feed a linear SVM; 80/20 split, confusion matrix; training cut from about 35 min in Python to about 2 min. *[claimed]*
- Live camera guidelines — Camera view overlays guidelines for the photographer; photos save to AWS and the phone gallery. *[claimed]*
- Terraform deployment — IaC for S3, IAM, Lambda, EC2 and MongoDB with remote state. *[claimed]*
- Accessibility, lighting, object angles — Listed as future work. *[planned]*

**Flow:** Create account → Upload and categorize photos → Like favorites so the model learns → Open camera with guidelines → Photographer frames shot and saves it

**Prompt:** Best Use of MATLAB (MathWorks): use MATLAB and/or Simulink exclusively or integrated into another tool.
**Fit (explicit):** Angle-detection model was trained and deployed with four MATLAB scripts (dataset creation, resize, training, deployment) after switching from Python prototypes; MATLAB also simulated the camera feedback.  *(targeted: Best Use of MATLAB)*
**Sponsor tools:** MATLAB (AlexNet feature extraction plus SVM training and deployment script, core)
**AI:** Transfer learning: pretrained AlexNet features with a linear SVM classifying good versus bad angles per user from liked photos; earlier PyTorch and Keras attempts dropped.
**Architecture:** Expo React Native app, Node/Mongoose backend with register, login and upload endpoints, MongoDB Atlas, S3 and EC2 on AWS via Terraform, MATLAB model scripts.
**Novelty:** Personalized pose-angle coaching rather than generic filters, with infrastructure-as-code in a small mobile project.
**Scope:** small · working: Page claims a prototype with login, camera saving to AWS and a model that worked with friends; no accuracy figures, no repo linked. · polish: Figma prototype, website and demo video listed; page has leftover Firebase instructions inconsistent with the stack.
**Claims:** Training time about 35 min (Python) to about 2 min (MATLAB) | Model worked with a group of friends | No accuracy reported
**Gaps:** No repo linked; code in Drive links not read; Page mentions a leaked and rotated cloud key (not recorded); Website and video not opened; Class 0/1 labels undefined
Sources: https://devpost.com/software/90, https://hackgt-11-circus-of-invention.devpost.com/

---

### AerLock
*HackGT HackGT 11 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Analytics Arcade - 1st Place [1st]

**What it is:** A remote 'airgap' button: an Android app sends a lock command over MQTT (HiveMQ Cloud, TLS) and Windows and Linux endpoint clients switch off Wi-Fi and Bluetooth, while the phone prompts for airplane mode. An unlock command restores connectivity.
**Problem / user:** Everyday users who want to quickly cut a set of devices off the network during an attack, for confidential work, or when traveling in high-risk areas.

**Features**
- One-tap lock/unlock — Android app publishes lock or unlock messages to the MQTT broker *[shown_working]*
- Windows and Linux endpoints — Clients subscribe to MQTT and disable or restore Wi-Fi and Bluetooth *[shown_working]*
- Android airplane-mode handling — App prompts the user to toggle airplane mode on lock/unlock and updates its UI state *[shown_working]*
- TLS-secured broker link — Connections to HiveMQ Cloud use TLS with credentials *[claimed]*
- Wider radios and ports control — Page claims cellular, NFC and physical ports can also be disabled *[claimed]*
- Customizable self-hosted broker — Users can run their own MQTT broker with custom endpoints *[claimed]*
- iOS and IoT endpoints — Future expansion and automated threat triggers *[planned]*

**Flow:** Install app and endpoints, connect to broker → Press lock button in Android app → Broker relays command to endpoints → Wi-Fi and Bluetooth turn off and phone enters airplane mode → Press unlock to restore

**Prompt:** not public / not found
**Fit (none):** Page does not state track text or how it relates; the project is a device-security tool with no analytics component on the page.  *(targeted: Analytics Arcade 1st place)*
**Sponsor tools:** HiveMQ Cloud (MQTT broker relaying lock/unlock commands, core)
**AI:** none
**Architecture:** Kotlin/Java Android app publishes MQTT commands over TLS to HiveMQ Cloud; Python/C-based Windows and Linux clients subscribe and run OS commands to toggle radios.
**Novelty:** Simple multi-device kill switch for radios; very small codebase (about 500 lines in repo across three platform folders).
**Scope:** tiny · working: Claims a deployed product with website and embedded demo video; repo has 7 files. · polish: Product site at aerlock.co and clear README; no tests.
**Claims:** Page calls it a fully deployed product | TLS 1.2 encryption between devices and server
**Gaps:** HackGT 11 track text not retrievable; Video not viewable
Sources: https://devpost.com/software/aerlock, evidence/hackgt-hackgt-11-aerlock.json

---

### Clarity
*HackGT HackGT 11 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** PHRI Challenge - 1st Place [1st]

**What it is:** A multimodal fatigue detector for doctors. A live webcam stream gets a face box labeled fatigued or active, and a recorded voice clip gets a fatigue label, mel-spectrogram, saliency map and transcript.
**Problem / user:** Doctors working while fatigued, with hospitals as the implied deployer; fatigue is linked to misdiagnosis and burnout, and the team says systems do not support tired clinicians.

**Features**
- Live face fatigue classification — Camera frames stream over WebRTC; a Haar cascade finds the face, a fine-tuned ViT labels fatigued/active, box drawn on the frame. *[shown_working]*
- Voice fatigue classification — User records audio; server computes a mel-spectrogram and a HuBERT-based emotion model labels fatigue/active. *[shown_working]*
- Saliency map over spectrogram — Smoothed gradients of the spectrogram against model output highlight which regions drove the prediction. *[shown_working]*
- Transcript alongside plot — Whisper-tiny transcribes the clip so users can match spectrogram regions to spoken words. *[shown_working]*

**Flow:** Open client; camera streams to backend → See live bounding box labeled fatigued or active → Record a voice clip and stop → Server builds spectrogram, saliency overlay, label and transcript → Combined plot and results returned to the client

**Prompt:** not public / not found
**Fit (implied):** Detects clinician fatigue to reduce misdiagnosis, a health-focused problem; the page names the PHRI prize but gives no stated fit.  *(targeted: PHRI Challenge)*
**AI:** Fine-tuned ViT (ImageNet pretrained, FEF Kaggle dataset) for faces, pretrained HuBERT-base for voice, Whisper-tiny for speech, gradient saliency for explainability; inference on a remote RTX 4090.
**Architecture:** Browser client streams video over WebRTC to a Python backend with parallel video and audio tracks; PyTorch models run on a remote GPU; Matplotlib renders plots server-side and returns them.
**Novelty:** Combines face and voice signals with an explainability layer, aimed at clinician wellbeing rather than patients; fine-tuned model published on Hugging Face.
**Scope:** small · working: Demo video embedded; README and Devpost describe a working pipeline with remote GPU inference. · polish: Hugging Face model card and explainability plots; no tests or deployment config.
**Claims:** Facial fatigue model about 92% accuracy on unseen data (evaluation not described) | Misdiagnosis 38% more likely when doctor fatigued (cited)
**Gaps:** PHRI challenge official text not found; no audio model metrics
Sources: https://devpost.com/software/clarity-kuv9xn, evidence/hackgt-hackgt-11-clarity.json, https://hackgt-11.devpost.com/ (not fetchable)

---

### EVA
*HackGT HackGT 11 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** AI Funhouse - 1st Place [1st]

**What it is:** A web-based voice companion for language learners that converses with the user, corrects grammar with GPT-4o as they speak, and checks pronunciation with a language-independent phoneme recognizer.
**Problem / user:** Learners of English or other languages who lack native-speaker conversation practice and get delayed feedback from apps like Duolingo.

**Features**
- Voice-to-voice conversation tutor — User speaks, AI replies in speech to keep a human-like exchange. *[claimed]*
- Instant grammar correction — GPT-4o with prompt engineering returns corrections during the conversation. *[claimed]*
- Language-independent pronunciation check — Zero-shot cross-lingual phoneme recognition compares what was said to the target. *[claimed]*
- Multi-language support — Listed in build text but next steps treat it as future. *[planned]*

**Flow:** Open the web app → Speak to the AI companion → Hear a spoken reply → See grammar corrections and pronunciation feedback

**Prompt:** not public / not found
**Fit (implied):** An LLM-based conversation tutor; the page names the prize it won but does not tie features to the track text.  *(targeted: AI Funhouse)*
**AI:** GPT-4o prompted for grammar correction; zero-shot cross-lingual phoneme recognition (Hugging Face model) for pronunciation; speech in/out services per requirements (Azure speech, ElevenLabs); chroma/langchain present.
**Architecture:** Flask backend with MySQL, Tailwind web frontend; audio goes through speech recognition, GPT-4o and phoneme models, with speech synthesis for replies.
**Novelty:** Pronunciation checking is language-independent via phoneme recognition; team first tried Snap Spectacles then pivoted to the web.
**Scope:** small · working: Demo video and screenshot on Devpost; repo has Flask app code (~4k LOC counting vendored files). · polish: Committed venv folder; no tests; README sparse.
**Gaps:** no step-by-step flow on page; AI Funhouse text not found
Sources: https://devpost.com/software/eva-jmb5et, evidence/hackgt-hackgt-11-eva.json

---

### Fight and Furious
*HackGT HackGT 11 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 2nd Place [2nd]

**What it is:** A React web app that teaches Krav Maga self-defense moves through modules and videos, then scores the user's live webcam attempt against a reference pose using MediaPipe.
**Problem / user:** People, especially women and marginalized groups, who want accessible practical self-defense training without classes.

**Features**
- Module and technique pages — Home, modules list and descriptions with example videos of each Krav Maga move. *[shown_working]*
- Live pose scoring — MediaPipe pose landmarks form limb vectors; mean squared error of angles against a reference gives an accuracy score. *[shown_working]*
- Encouraging feedback messages — Congratulation-style messages shown after practice. *[shown_working]*
- Real-time form correction and VR/AR — Listed as future work with custom Krav Maga dataset. *[planned]*

**Flow:** Land on home page → Pick a module → Read description and watch example video → Practice live in front of webcam → Get accuracy score and encouragement

**Prompt:** not public / not found
**Fit (none):** General overall award; app addresses gender-based violence with a working CV scoring prototype.  *(targeted: Best Overall)*
**AI:** MediaPipe pose estimation with OpenCV/NumPy; accuracy computed as MSE of limb-vector angles versus a reference pose; no trained model.
**Architecture:** React frontend embeds a Streamlit live-video analysis app via iframe; Python FastAPI/Uvicorn backend runs the pose comparison.
**Novelty:** Uses classical pose-angle comparison for martial-arts coaching built by a first-time CV team; Streamlit iframe workaround for video relay.
**Scope:** small · working: Demo video and screenshots; tested with participants, adjusting for lighting and clothing. · polish: Themed UI with panda mascot; small repo, no tests.
**Gaps:** Best Overall criteria not found; no numeric accuracy
Sources: https://devpost.com/software/fight-and-furious, evidence/hackgt-hackgt-11-fight-and-furious.json

---

### FirefightAR
*HackGT HackGT 11 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** SnapAR Elexa Power Bank (20000mAH)

**What it is:** A Snap Spectacles AR app for firefighters that overlays hazards, detected people and heat sources, room layout and routes to the nearest person or exit, with Firebase syncing data across team members.
**Problem / user:** Firefighters who search burning buildings by hand along walls, which is slow and risks disorientation or entrapment.

**Features**
- Real-time AR overlay — Spectacles show live camera view with information about surroundings, built in Lens Studio. *[shown_working]*
- Person and heat-source detection — Pre-trained YOLOv5 with fire-related datasets identifies people and heat sources. *[claimed]*
- Hazard mapping and layout — Marks dangers and room layout in the overlay. *[claimed]*
- Path guidance — Shortest path to nearest person plus exit directions. *[claimed]*
- Team sync — Firebase storage shares situational data between members. *[claimed]*
- Thermal imaging — Listed as future work. *[planned]*

**Flow:** Firefighter wears Spectacles → Camera view shows overlays for hazards, people and heat → Follow path to nearest person or exit → Teammates see shared data

**Prompt:** SnapAR Elexa Power Bank: take on Snapchat's challenge to build an AR experience showcasing AI on AR glasses; live or video demo allowed.
**Fit (implied):** Spectacles Lens uses an object-detection model in an AR rescue-navigation experience; page mentions no explicit prize target beyond the SnapAR win.  *(targeted: SnapAR Elexa Power Bank (20000mAH))*
**Sponsor tools:** Snap Spectacles / Lens Studio (AR headset, Spectacles Interaction Kit and overlay development, core)
**AI:** Pre-trained YOLOv5 used without custom training to detect people and heat sources; pathfinding to targets in the overlay.
**Architecture:** Lens Studio app (JavaScript/TypeScript) on Spectacles with a Python detection component and Firebase storage for sync; architecture diagram on page not described in text.
**Novelty:** Targets a high-stakes first-responder use case on week-old Spectacles hardware by a team new to AR.
**Scope:** small · working: Demo video and Spectacles screenshot on page; repo content could not be read; no metrics. · polish: Page includes architecture diagram and two repos, one containing little visible content.
**Claims:** AR interface needs minimal training | No accuracy or latency figures
**Gaps:** Evidence clone failed and primary repo was unreachable via WebFetch and raw; Second repo showed only a Lens Studio project file listing; Detection pipeline details unclear (YOLO in Python vs Lens Studio)
Sources: https://devpost.com/software/firefightar, https://hackgt-11-circus-of-invention.devpost.com/, https://github.com/Chanakya-TS/Firefight-AR (file list only)

---

### Lightning McScream
*HackGT HackGT 11 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Domain Name from GoDaddy Registry

**What it is:** A laser-cut ESP-controlled toy car whose speed follows how loud and high a player screams into a Quest 2 headset, raced on a custom Unity AR track with timing and top-speed readouts.
**Problem / user:** No stated problem; a carnival-themed novelty for players who want a voice-driven racing game.

**Features**
- Scream-controlled speed — Headset audio becomes integer volume and pitch values streamed via a FastAPI server to the car's microcontroller, which sets rear axle speed. *[shown_working]*
- Physical car — Laser-cut frame, rear-wheel drive via two gear motors and 30:10 gears, servo steering, 12V supply, LEGO parts. *[shown_working]*
- AR track in Unity — Custom boundaries, track and start menu on Oculus Quest 2. *[shown_working]*
- Run telemetry — Accelerometer and position processing yield duration and top speed for best-time competition. *[claimed]*
- User-defined drag races — Players set up virtual races in the AR menu. *[claimed]*

**Flow:** Wear Quest 2 and open AR menu → Choose or define a drag race → Scream into the headset → Car accelerates based on volume and pitch → Read run time and top speed

**Prompt:** Best Domain Name from GoDaddy Registry: register a domain with GoDaddy Registry to enter; prize is a Hack from Home Kit.
**Fit (none):** Page mentions no domain name or GoDaddy product; the connection to the prize cannot be seen from the writeup.  *(targeted: Best Domain Name from GoDaddy Registry)*
**AI:** none
**Architecture:** Quest 2 Unity app captures audio, Python/C# processing sends values through a FastAPI web server to an ESP microcontroller driving an L298N motor driver, with an accelerometer returning data; MATLAB for analysis.
**Novelty:** Hardware-heavy build combining voice input, a physical vehicle and AR; no ML involved. Microcontroller named as both ESP32 and ESP8266 on the page.
**Scope:** small · working: Demo video and electronics/AR screenshots on page; no repo or measurements. · polish: Custom-fabricated car with gears and axles; Bluetooth-to-WiFi switch indicates iteration.
**Claims:** Louder scream makes the car faster | No measurements reported
**Gaps:** No repo linked; Domain name not mentioned; Video not opened; Page inconsistencies: ESP32 vs ESP8266, driver called DC relay
Sources: https://devpost.com/software/car-hf3moa, https://hackgt-11-circus-of-invention.devpost.com/

---

### Market Melee
*HackGT HackGT 11 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Best DEI Hack sponsored by Fidelity

**What it is:** A Flask web app where users build simulated stock portfolios from S&P 500 stocks using real market data, view performance graphs and metrics with explanatory pop-ups, and compare with friends in leagues.
**Problem / user:** Everyday people intimidated by financial jargon, and would-be traders who cannot afford to trade, wanting to learn and compete without real money.

**Features**
- Simulated portfolios — Users allocate investments across hundreds of stocks and track performance over time using market data from yfinance. *[shown_working]*
- Graphs and stock pages — Matplotlib performance charts and per-stock metric pages. *[shown_working]*
- Metric explainers — Pop-up modals explain daily returns, volatility and Sharpe ratio. *[claimed]*
- Friend leagues — Compare progress against friends; live drafting is future work. *[claimed]*
- Accounts — bcrypt-hashed login with user-scoped data in MongoDB Atlas. *[claimed]*

**Flow:** Sign up or log in → Pick and allocate simulated stocks → View portfolio graphs → Open a stock to read metrics and pop-up explanations → Check league standings

**Prompt:** Best DEI Hack sponsored by Fidelity: build financial technology that expands access to financial opportunities and resources for all communities.
**Fit (implied):** Gamified paper trading lowers the barrier to learning investing without capital; the page frames accessibility for everyday people but does not cite the prize.  *(targeted: Best DEI Hack sponsored by Fidelity)*
**Sponsor tools:** MongoDB Atlas (User data and stock statistics, supporting)
**AI:** none
**Architecture:** Flask backend with Jinja templates and Bootstrap front end, MongoDB Atlas, pandas/NumPy analysis over a bundled data folder of stock files, Matplotlib images.
**Novelty:** Plain gamified paper-trading app built from an investing class; ML only listed as future work. Repo holds hundreds of stock data files.
**Scope:** small · working: ~1.5k LOC plus 487 data files and a demo video; no live host or tests. · polish: Short README mirroring the Devpost text; pop-up explainers noted.
**Claims:** Statistics and visualizations worked seamlessly with frontend | No usage metrics reported
**Gaps:** Real-time data claim vs bundled data files unverified; League functionality described as not yet implemented in next steps
Sources: https://devpost.com/software/market-melee, evidence/hackgt-hackgt-11-market-melee.json, https://hackgt-11-circus-of-invention.devpost.com/

---

### MedEase: AI-Assisted Diagnostic Workflow
*HackGT HackGT 11 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Use of MongoDB Atlas

**What it is:** A web app for doctors: log in, upload patient PDFs, and a retrieval-augmented LLM returns a differential diagnosis and note content formatted for an EHR, with past documents stored in MongoDB.
**Problem / user:** Emergency-room physicians who lose much of a shift to data entry, which the team ties to patient-safety risk.

**Features**
- PDF upload and history — Doctors upload patient PDFs and reopen earlier uploads. *[claimed]*
- RAG differential diagnosis — LlamaIndex pipeline over a vector store returns a differential and relevant medical information. *[claimed]*
- EHR-ready output — Surfaces information that can be entered directly into an electronic health record. *[claimed]*
- Login — Authentication page with user data in MongoDB. *[claimed]*
- MongoDB Atlas storage — Users, vector database and PDFs kept in Atlas. *[claimed]*
- EHR API and medication ordering — Future integration to cut the 15-click prescription process. *[planned]*

**Flow:** Log in → Upload or open a patient PDF → RAG model runs → Read differential and EHR-ready notes

**Prompt:** Best Use of MongoDB Atlas: build a hack using MongoDB Atlas, the cloud database (student credit and free tier available).
**Fit (explicit):** Atlas holds user accounts, the RAG vector database and uploaded PDFs, making it the single data store for the diagnostic pipeline.  *(targeted: Best Use of MongoDB Atlas)*
**Sponsor tools:** MongoDB Atlas (User data, vector search store and PDF storage, core)
**AI:** Retrieval-augmented generation with LlamaIndex over uploaded PDFs; LLM not named on the page.
**Architecture:** Astro/React/TypeScript frontend on Vercel; Python LlamaIndex backend calling an LLM; MongoDB Atlas for users, vectors and files.
**Novelty:** Narrow clinical documentation helper with a vector store in the same database as accounts; accuracy not evaluated and medical-use claims untested.
**Scope:** small · working: Live site and demo video linked; repo could not be read; no accuracy metrics. · polish: Hosted web app with login and document history.
**Claims:** Over 40% of an ER shift is data entry (cited study) | No performance metrics for the tool
**Gaps:** Evidence clone failed; README unreachable via WebFetch and raw; LLM model unnamed; Live site and video not opened
Sources: https://devpost.com/software/medease-ai-assisted-diagnostic-workflow, https://hackgt-11-circus-of-invention.devpost.com/

---

### Noma
*HackGT HackGT 11 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 1st Place [1st]

**What it is:** A surgical telemedicine platform for Mohs surgery. It shows remote surgeons a 3D face reconstruction from a patient scan and builds time-stamped, speaker-labeled transcripts of the operating room using a Neo4j knowledge graph and an LLM.
**Problem / user:** Rural patients and surgeons lacking local Mohs specialists, who need remote experts to guide procedures and documentation.

**Features**
- 3D face reconstruction viewer — Gaussian-splat style reconstruction from an initial face video shown in a Three.js/React viewer; consultants rotate it. *[shown_working]*
- Remote incision guidance — Consultants mark incisions on the 3D model in an incision tool demo. *[shown_working]*
- Speaker-diarized OR transcription — AWS Transcribe separates speakers; video actions transcribed with a vision-language model. *[claimed]*
- Surgical knowledge graph — Neo4j GraphRAG maps tools, procedures and surgeons, updated as transcripts arrive. *[shown_working]*
- LLM documentation with EHR Q&A — Fine-tuned Meditron 7B generates time-stamped notes; module answers questions over a sample EHR PDF. *[claimed]*

**Flow:** Capture initial facial video → Reconstruct 3D model → Consultant views and marks incisions → OR audio/video is transcribed into a knowledge graph → LLM outputs time-stamped documentation

**Prompt:** not public / not found
**Fit (none):** Overall award; healthcare telemedicine with multi-component build.  *(targeted: Best Overall)*
**Sponsor tools:** AWS Transcribe (speaker diarization and transcription of OR audio, supporting)
**AI:** Instant Splat/Gaussian splatting for 3D; AWS Transcribe; LITA for video action text; Meditron 7B plus GraphRAG over Neo4j for documentation; OpenAI key in setup.
**Architecture:** Flask API with streaming, RAG and transcription modules; React/Three.js mesh viewer and incision tool; Neo4j graph; Streamlit presentation demo; RunPod for heavy inference.
**Novelty:** Pairs 3D reconstruction with an auto-built surgical knowledge graph; real-time claim limited because reconstruction takes 45+ minutes so a pre-scan is loaded.
**Scope:** medium · working: Demo video, screenshots and runnable repo; live reconstruction not achieved per challenges section. · polish: Structured README, setup with uv, presentation app; no tests.
**Claims:** Real-time 3D visualization (page admits reconstruction takes 45+ minutes)
**Gaps:** Best Overall criteria not found
Sources: https://devpost.com/software/noma-ug9qxn, evidence/hackgt-hackgt-11-noma.json

---

### OncoAI
*HackGT HackGT 11 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Carnival for a Cause - 1st Place [1st]

**What it is:** A Next.js dashboard concept that ingests blood tests, mammograms, pathology slide images and scRNA-seq data for breast cancer, runs them through models, and has an LLM compile one clinician report with encrypted storage.
**Problem / user:** Clinicians and breast cancer patients facing unequal, slow diagnosis that normally needs pathologists, geneticists, radiologists and hematologists.

**Features**
- Multi-modal patient data upload — Accepts four data types per patient. *[claimed]*
- Model analysis per data type — Transformers and neural nets (PyTorch/TensorFlow) process each input; which model handles what is not stated. *[claimed]*
- LLM report compilation — An LLM merges model outputs into one patient report. *[claimed]*
- Encrypted record storage — Patient records encrypted and kept in PostgreSQL. *[claimed]*
- One-click analysis — Whole pipeline triggered from a single action. *[claimed]*

**Flow:** Upload patient data → System runs models → LLM compiles report → Record encrypted and stored → Clinician reviews report

**Prompt:** not public / not found
**Fit (implied):** Health-equity cause project; page names the track it won, no stated link to track text.  *(targeted: Carnival for a Cause)*
**AI:** LLMs (Gemini, Groq, Llama, Mistral listed) plus unspecified transformer/neural models for the data types; LLM synthesizes the report.
**Architecture:** Next.js frontend on Vercel with Postgres/Vercel Blob/Google Cloud Storage dependencies and bcrypt; Python models; uploads folder present in repo.
**Novelty:** Attempts to combine four unusual data modalities, including scRNA-seq, in one report.
**Scope:** small · working: No demo video or live link; repo is mostly a Next.js scaffold with uploads and pages folders. · polish: Default create-next-app README; no tests.
**Claims:** Cuts a month-long four-doctor process to minutes (self-reported)
**Gaps:** no demo evidence; track text not found
Sources: https://devpost.com/software/oncoai, evidence/hackgt-hackgt-11-oncoai.json

---

### OncoBot
*HackGT HackGT 11 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Emerging - 3rd Place [3rd]

**What it is:** A Discord bot that takes a photo of a skin lesion, runs OpenCV image processing to say melanoma yes or no, and if yes asks for a location and lists the five nearest hospitals via Google Maps.
**Problem / user:** Worried individuals who want a quick check of a suspicious skin mark and a pointer to nearby care.

**Features**
- Lesion photo analysis in Discord — Preprocessing removes noise, locates lesions, then outputs a melanoma yes/no. *[shown_working]*
- Nearest hospitals lookup — User gives an address; Google Maps API returns five closest hospitals. *[shown_working]*

**Flow:** Send lesion image to bot → Bot returns melanoma yes or no → If yes, enter location → Bot lists nearest 5 hospitals

**Prompt:** not public / not found
**Fit (none):** Beginner-friendly category; project is a first-hackathon health bot.  *(targeted: Best Emerging)*
**AI:** Pre-trained OpenCV models and classical preprocessing only; no custom model trained.
**Architecture:** Python main.py runs a Discord bot calling an OpenCV pipeline and the Google Maps API; token and key from env file.
**Novelty:** Delivers screening through a chat bot rather than an app; built by first-time hackers.
**Scope:** tiny · working: Four screenshots on Devpost show yes and no results and hospital list; repo has 4 files. · polish: README with setup steps; no tests.
**Claims:** 82% accurate labeling system (no dataset or method given) | about 200,000 new melanoma cases yearly (cited)
**Gaps:** no video
Sources: https://devpost.com/software/oncobot-qlkv0n, evidence/hackgt-hackgt-11-oncobot.json

---

### prompt+
*HackGT HackGT 11 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 3rd Place [3rd]

**What it is:** A Chrome extension plus Flask backend that adds a prompt+ button to LLM chat boxes, compresses prompts to cut tokens, and produces copyable summaries of past chats to carry context into new chats.
**Problem / user:** Developers, researchers and heavy LLM users who exhaust token allowances and struggle to write efficient prompts.

**Features**
- Prompt compression for text — Stop-word removal, lemmatization and punctuation prioritization via spaCy. *[claimed]*
- Code prompt optimization — Rewrites code with lambdas, ternaries and renamed variables via custom GPT agents. *[claimed]*
- Input type detection — Classifies input as text or code and routes to the matching strategy. *[claimed]*
- Task-specific modes — Templates for creative writing, technical queries, code generation, summarization. *[claimed]*
- Chat context summaries — A contextualization model summarizes a conversation for pasting into a new chat or another assistant. *[claimed]*
- Efficiency metrics — Reports processing time and token usage using tiktoken counts. *[claimed]*
- In-page UI — Button beside send, preview, copy-to-clipboard, double-click to replace prompt. *[shown_working]*

**Flow:** Type prompt in chat box → Click prompt+ → Preview optimized prompt → Double-click to replace it → Copy chat summary into a new chat

**Prompt:** not public / not found
**Fit (none):** Overall award; developer-productivity tool for LLM users.  *(targeted: Best Overall)*
**AI:** OpenAI models with LangChain custom agents for code; spaCy NLP and tiktoken for plain-text compression and counting; classification routes input type.
**Architecture:** Chrome extension (React/JS) talks to a Flask backend; prompts stored in Firebase realtime database and wiped when session ends.
**Novelty:** Targets token budget rather than answer quality, and adds cross-assistant context handoff.
**Scope:** small · working: Demo video and five screenshots; repo has extension and Flask backend. · polish: Figma design, extension UI; no tests.
**Claims:** 47% token reduction for text inputs | 35% token reduction for code inputs (method not described)
**Gaps:** Best Overall criteria not found
Sources: https://devpost.com/software/prompt-sf7drq, evidence/hackgt-hackgt-11-prompt.json

---

### SafeSnap
*HackGT HackGT 11 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Emerging - 2nd Place [2nd]

**What it is:** A Snap Spectacles AR lens built in Lens Studio that guides a user through an earthquake: it scans the room, labels objects, gives audio and visual cues for safe spots, and shows a voice-controlled floating checklist.
**Problem / user:** People in natural disasters, with earthquakes as proof of concept; many wrongly think running to doorways is safest.

**Features**
- Room scan and object labeling — Lens scans the surroundings in 3D and identifies objects. *[claimed]*
- Safe-location cues — Audio and visual signals when the user is in a safe spot. *[claimed]*
- Floating voice-activated checklist — Checklist of earthquake actions follows the user or stays fixed, controlled by a SnapAR voice asset. *[claimed]*
- ML safe-spot detection — Trained model to find secure locations instantly. *[planned]*

**Flow:** Put on Spectacles with the lens → Lens scans room → Receive cues for safe spots → Use voice to run the checklist

**Prompt:** not public / not found
**Fit (none):** Beginner-oriented category; AR disaster guidance prototype.  *(targeted: Best Emerging)*
**Sponsor tools:** Snap Lens Studio / Spectacles (AR lens, scanning, voice recognition asset, core)
**AI:** None in current build; object-identification ML listed as future work, relying on Lens Studio built-in scanning and voice assets.
**Architecture:** Single Lens Studio project in JavaScript with assets, voice recognition and checklist scripts running on Spectacles.
**Novelty:** AR-glasses disaster-preparedness guide; team new to Lens Studio.
**Scope:** small · working: Demo video and five screenshots on Devpost; repo is a Lens Studio project dump (~600 files, mostly cache and assets). · polish: No tests; features unproven beyond demo.
**Claims:** 58% of Americans think doorways are safest in quakes; 34% trained (cited FEMA)
**Gaps:** video content not described
Sources: https://devpost.com/software/safesnap, evidence/hackgt-hackgt-11-safesnap.json

---

### SafeWay
*HackGT HackGT 11 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of Terraform

**What it is:** A Flask and Mapbox route planner that uses scraped government crime, streetlight and road-quality data to propose three routes between two points and rank them by safety, lighting, walkability and efficiency preferences, run via Docker and Terraform.
**Problem / user:** Pedestrians and drivers in unfamiliar areas who get efficient but unsafe, dark or rough routes from mainstream navigation apps.

**Features**
- Safety-related data scraping — Pandas scripts collect public data on high-crime areas, streetlights and road quality. *[claimed]*
- Preference-weighted routing — User sets weights for safety, walkability, lighting and efficiency. *[claimed]*
- Three ranked routes — Algorithm returns three candidates and rates them by data near points along each route. *[shown_working]*
- Mapbox map — Interactive map draws routes; screenshot shows GT to Emory. *[shown_working]*
- Terraform and Docker run — terraform apply starts the containerized app. *[shown_working]*
- Mobile app and more metrics — Future work. *[planned]*

**Flow:** Enter start and destination → Adjust preference weights → App computes three routes → Compare ranked routes on map

**Prompt:** Best Use of Terraform (HashiCorp): use Terraform in your project; community edition is free.
**Fit (explicit):** README and Devpost say Terraform with Docker standardizes running the app: terraform init and apply start it and destroy stops it; the repo contains a .terraform directory.  *(targeted: Best Use of Terraform)*
**Sponsor tools:** Terraform (Provisioning and running the Dockerized app, supporting); MongoDB Atlas (Storing scraped route data, supporting)
**AI:** none
**Architecture:** Python scraping into MongoDB Atlas via PyMongo; Flask API computes route scores; vanilla JS front end with Mapbox; Docker image launched through Terraform.
**Novelty:** Combines civic datasets into multi-criteria route scoring; Terraform used for local app deployment rather than cloud infrastructure.
**Scope:** small · working: ~800 LOC, Dockerfile, data and static folders, screenshot of real routes; no live demo or tests. · polish: README run instructions and emoji sections; modest UI.
**Claims:** Highly functional app with intuitive UI (self-assessment) | No safety outcomes measured
**Gaps:** Data sources not named; Routing algorithm not detailed; Video mentioned but not linked
Sources: https://devpost.com/software/saferoute-2iyzml, evidence/hackgt-hackgt-11-safeway.json, https://hackgt-11-circus-of-invention.devpost.com/

---

### SentinelCV
*HackGT HackGT 11 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Magical Midway - 1st Place [1st]

**What it is:** A bedsore-prevention system that uses existing hospital room RGB cameras with pose estimation to track patients' joints and movement, and raises dashboard alerts when immobility exceeds a threshold.
**Problem / user:** Nurses and hospital staff trying to prevent pressure ulcers, which affect about 2.5 million patients yearly and are rarely monitored.

**Features**
- Patient and joint detection — MediaPipe pose estimation plus YOLO find the patient in bed and key joints from camera video. *[shown_working]*
- Immobility tracking and alerts — Movement classification measures time without moving; web GUI alerts staff to reposition. *[shown_working]*
- Multi-patient dashboard — Flask GUI shows per-patient status, recent movement and alerts, reachable from any device on network. *[shown_working]*
- Per-patient thresholds from EHR — Backend supports individual thresholds; EHR integration planned. *[planned]*

**Flow:** Camera feed processed live → System tracks joints and movement → Immobility passes threshold → Alert appears in dashboard → Staff reposition patient

**Prompt:** not public / not found
**Fit (implied):** Patient-safety monitoring using existing hardware; page names the track won.  *(targeted: Magical Midway)*
**AI:** MediaPipe pose estimation, Ultralytics YOLO and OpenCV with custom logic for position and movement classification; tuned thresholds.
**Architecture:** Python Flask server reads camera streams, runs pose and detection, serves a Bootstrap web GUI with per-patient alerts.
**Novelty:** Reuses existing room cameras, no extra sensors; includes cited clinical statistics.
**Scope:** small · working: Demo video and four GIFs of body detection, joint detection, posture monitoring and UI. · polish: Detailed README with citations; no tests.
**Claims:** Pressure ulcers affect about 2.5M patients yearly (cited) | Tuned thresholds give high accuracy (no metrics)
**Gaps:** Magical Midway text not found
Sources: https://devpost.com/software/project-restease, evidence/hackgt-hackgt-11-sentinelcv.json

---

### SnapSecure
*HackGT HackGT 11 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner SnapAR Skullcandy Grind True Wireless Earbuds

**What it is:** A Snap Spectacles Lens that authenticates users by hand gesture, switches their saved physical-environment presets (such as lamp colors through a Raspberry Pi bridge), and estimates heart rate from head motion and tremor from hand motion.
**Problem / user:** People sharing AR headsets or smart rooms who need quick user switching, plus users who want passive health tracking such as early Parkinson's tremor signs.

**Features**
- Gesture authentication — A decision tree running in Lens Studio recognizes personal gestures such as a finger tap; models trained from three samples per gesture. *[shown_working]*
- Environment presets — On login, a Raspberry Pi bridge changes IoT devices like lamp colors. *[shown_working]*
- Heart rate from head motion — Ballistocardiogram-style signal filtered with Butterworth and FFT. *[claimed]*
- Tremor detection — Derived from hand-tracking motion data. *[claimed]*
- Cross-headset models — Python gesture models exported to ONNX, said to work on Spectacles, Vision Pro and Quest 2. *[claimed]*
- Streamlit model demo — Separate web demo of the models. *[shown_working]*
- Door unlock and stress tracking — Future work. *[planned]*

**Flow:** Wear Spectacles and perform an authentication gesture → System loads the user's presets → Lamps and other devices adjust → Headset records heart rate and tremor data for that user

**Prompt:** SnapAR Skullcandy prize: build a Lens on Spectacles showcasing AI on AR glasses; teams give a live demo to judges.
**Fit (implied):** Lens Studio Lens on Spectacles applies trained gesture models and health signal analysis to identify users and personalize the room; page does not cite the prize text itself.  *(targeted: SnapAR Skullcandy Grind True Wireless Earbuds)*
**Sponsor tools:** Snap Spectacles / Lens Studio (Gesture capture, in-Lens decision tree and motion data, core)
**AI:** Gesture classifiers trained in Python from few samples, exported to ONNX and re-implemented as a decision tree in Lens Studio; classical signal processing (Butterworth, FFT) for heart rate.
**Architecture:** Lens Studio Lens sends HTTP requests via Heroku to Python backend; Raspberry Pi bridges to lamps; SciPy/pandas models and Streamlit demo in a second repo.
**Novelty:** Combines AR biometric-like gesture login, IoT control and passive health sensing in one Lens; rate limits forced moving detection on device.
**Scope:** small · working: Demo video, Streamlit model demo and Lens Studio project in repo; no accuracy results. · polish: Repo is a raw Lens Studio project (2.4k files, cache included) with a one-paragraph README.
**Claims:** Gesture models from only three examples | Works across three headsets | No accuracy metrics
**Gaps:** README is one paragraph; Cross-device claim and health accuracy unverified; Model demo and video not opened
Sources: https://devpost.com/software/snapsecure, evidence/hackgt-hackgt-11-snapsecure.json, https://hackgt-11-circus-of-invention.devpost.com/

---

### SpecTackles
*HackGT HackGT 11 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** SnapAR Soundview Speaker

**What it is:** A Snap Spectacles AR lens that detects an image marker (such as a light switch) and, when the wearer interacts with it, sends a command through Firebase to a Raspberry Pi that physically toggles a real light, then shows the new state in the glasses.
**Problem / user:** Spectacles wearers who want hands-free control of smart-home devices; the page states a goal rather than an explicit problem.

**Features**
- Image-marker detection in AR — Lens Studio image tracking recognises a marker and a JavaScript event fires on interaction. *[claimed]*
- Real light-switch toggle — Event writes the action to Firebase; a Python script on a Raspberry Pi reads it and toggles the physical device. *[claimed]*
- State feedback in AR — Device state (light on/off) read back from Firebase and rendered in the glasses view, with white and blue LED states and on-screen toggle buttons. *[claimed]*
- NextJS web control interface — Browser page talks to the lens logic via TypeScript as an alternative control surface. *[claimed]*
- Gesture, voice and more devices — Listed as next steps: gesture recognition, voice commands, thermostats and door locks. *[planned]*

**Flow:** Look at a marker or light switch through Spectacles → Lens Studio detects it and the wearer triggers it → Action is written to Firebase → Raspberry Pi receives the command and toggles the device → New light state appears in the AR view → Optionally control the same device from the web page

**Prompt:** not public / not found
**Fit (implied):** Built a Lens Studio lens for Snap Spectacles using image tracking to drive a real-world device, i.e. an AR-glasses application. Sponsor prize wording was not found, so fit is inferred from the Spectacles/Lens Studio use.  *(targeted: SnapAR Soundview Speaker)*
**Sponsor tools:** Snap Spectacles (AR glasses as the interaction surface, core); Lens Studio (Image tracking and lens event logic, core)
**AI:** none
**Architecture:** Spectacles lens (Lens Studio, JavaScript) detects markers and writes device actions to Firebase; a Raspberry Pi running Python watches Firebase and switches the hardware; a NextJS page offers browser control.
**Novelty:** Closes an AR-glasses to cloud to physical-hardware loop for a real light switch; repo holds many Lens Studio experiment folders (two-marker tags, API-call buttons, sliders, object detection).
**Scope:** small · working: Page claims an end-to-end prototype; no video or live link, seven captioned screenshots only. · polish: Repo is a large pile of Lens Studio experiment projects with a two-line README; little documentation.
**Claims:** Real-time control of a physical light switch from AR | End-to-end functional prototype
**Gaps:** No demo video; README is a two-line note saying the clickable-button folder is the Lens Studio project; Prize text for SnapAR Soundview Speaker not found; HackGT 11 page not fetched; Thermostat shown only in a screenshot caption
Sources: https://devpost.com/software/spectackles, evidence/hackgt-hackgt-11-spectackles.json

---

### WoundAI
*HackGT HackGT 11 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Emerging - 1st Place [1st]

**What it is:** A mobile app concept where a patient photographs a wound and a TensorFlow CNN returns a wound class with per-class confidence scores, with wound information kept in one place. Repo is a thin React scaffold with a LiveKit assistant folder.
**Problem / user:** Patients managing one or more wounds who want easier tracking and information, also pitched to clinicians.

**Features**
- Wound photo classification — Phone camera image run through a CNN returning class and confidence per class. *[claimed]*
- Severity assessment — Mentioned as part of analysis. *[claimed]*
- Centralized wound records — Stores wound info for patients with multiple wounds. *[claimed]*
- Voice-to-text input — Appears in tagline only; LiveKit assistant folder in repo. *[unclear]*

**Flow:** Capture wound photo → App runs CNN → See predicted class and confidence per class

**Prompt:** not public / not found
**Fit (none):** Healthcare image classification app; page lists the award only.  *(targeted: Best Emerging)*
**AI:** TensorFlow CNN on wound images with OpenCV preprocessing; page build text appears copied from a plant-disease classifier.
**Architecture:** React (create-react-app) frontend with Python backend and a livekit-assistant folder; no evidence of connected deployed model.
**Novelty:** Wound triage via phone photo; page reads partly like a research proposal and has copied-looking build text.
**Scope:** tiny · working: Demo video linked but not described; repo ~25 files, 318 LOC, default CRA README. · polish: Has a test file but no real documentation.
**Claims:** High classification accuracy (no metrics)
**Gaps:** dataset and model not named; challenges section empty
Sources: https://devpost.com/software/woundai, evidence/hackgt-hackgt-11-woundai.json

---

