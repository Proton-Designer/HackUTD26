# HP & NVIDIA Developer Challenge — 2025 (10 projects)

### AffectLink
*HP & NVIDIA Developer Challenge 2025 · dataset: sponsor · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner First Place [1st]

**What it is:** Local-first telehealth dashboard that watches a patient's webcam and microphone, estimates emotion from face, vocal tone and transcribed words, and computes an Emotional Consistency Index that flags when words and non-verbal cues disagree. All inference runs on an HP workstation.
**Problem / user:** Clinicians running virtual sessions who lose non-verbal emotional cues and may miss a patient's real state.

**Features**
- Facial emotion analysis — DeepFace runs locally on webcam frames. *[shown_working]*
- Speech emotion and transcription — Whisper ASR transcribes speech and a Hugging Face SER model reads vocal tone, deployed via HP AI Studio's local Swagger API. *[shown_working]*
- Text emotion classification — Classifier on the transcript produces a text-emotion signal. *[shown_working]*
- Emotional Consistency Index — Aggregates face, voice and text emotion and flags mismatches; formula not published. *[claimed]*
- Streamlit clinician dashboard — Reads result JSON and latest frame to display live metrics. *[shown_working]*
- MLflow tracking — Experiments, model registration and versioning in HP AI Studio. *[shown_working]*

**Flow:** Capture webcam and mic → Pipeline splits video and audio paths → Models return face, audio and text emotions → ECI computed and written to local files → Streamlit UI shows live frames and metrics

**Prompt:** Build an AI web app using HP AI Studio tools that solves a real problem in one industry (automotive manufacturing, healthcare, finance, retail or technology); judged equally on AI innovation, demo and documentation, industry impact, and originality.
**Fit (explicit):** Healthcare use case built on HP AI Studio (MLflow, local Swagger deployment) on an HP workstation with on-device inference; the README states this integration explicitly.  *(targeted: First Place [1st], Healthcare industry)*
**Sponsor tools:** HP AI Studio (Local deployment of Whisper/SER/text models via Swagger API and MLflow tracking, core); HP workstation (Local on-device inference, supporting)
**AI:** Three modalities: DeepFace (face), Whisper plus Hugging Face SER (voice), Hugging Face text emotion classifier; fused rule-based into an ECI. All inference local; DeepFace runs outside AI Studio.
**Architecture:** main_processor orchestrates webcam/mic capture, sends frames to DeepFace and audio to AI Studio-served models, aggregates ECI, writes JSON/JPG files that the Streamlit UI reads.
**Novelty:** Cross-modal inconsistency score aimed at telehealth rather than single-emotion labels; deliberately local to avoid sending patient data to the cloud.
**Scope:** medium · working: Solo project with ~4.9k LOC pipeline and screenshots of dashboard, MLflow and Swagger; no tests; demo video said to exist but no link. · polish: README with thumbnail, architecture, MIT license, built-with list.
**Claims:** Patient data never leaves the device | ECI highlights unexpressed emotion, fatigue or stress
**Gaps:** No accuracy or latency figures; Video link absent; ECI formula undocumented
Sources: https://devpost.com/software/affectlink, evidence/sponsor-hp-nvidia-developer-challenge-2025-affectlink.json, sponsor_prompts_NVIDIA.jsonl

---

### Codence
*HP & NVIDIA Developer Challenge 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Bonus Best in Enterprise Data Analysis

**What it is:** Platform that extracts decisions from uploaded meeting notes with GPT models, proposes Jira ticket updates that a human approves before syncing, and checks GitLab pull requests via webhook against the agreed rules, explaining violations.
**Problem / user:** PMs, tech leads and engineers whose meeting decisions drift from tickets and code.

**Features**
- Meeting decision extraction — GPT-based model pulls rules and decisions from unstructured notes uploaded in a minimal web UI. *[claimed]*
- Approval-gated Jira sync — Suggested ticket updates pushed via Jira REST only after human approval. *[claimed]*
- GitLab PR checks — Webhook on pull requests validates code changes against extracted rules. *[claimed]*
- Violation explanations — AI describes in plain language why a PR breaks a rule. *[claimed]*

**Flow:** Upload meeting notes → AI extracts decisions → Human approves suggestions → Jira tickets update → PR opens and webhook checks it → Violations explained

**Prompt:** Build an AI web app using HP AI Studio tools that solves a real problem in one industry (automotive manufacturing, healthcare, finance, retail or technology); judged equally on AI innovation, demo and documentation, industry impact, and originality.
**Fit (implied):** Enterprise workflow tool for product teams; page tags mention HP AI Studio but do not explain its role.  *(targeted: Bonus Best in Enterprise Data Analysis)*
**Sponsor tools:** HP AI Studio (Only appears as a tag; role not described, unclear)
**AI:** GPT-based models extract rules from notes and generate explanations for rule violations; no retrieval or fine-tuning described.
**Architecture:** Web UI uploads notes to a FastAPI backend (tags say Flask) that calls GPT, Jira REST and receives GitLab webhooks; Docker listed.
**Novelty:** Closes the loop from meeting notes to tickets to PR enforcement; the repo contains a full PRD with measurable goals.
**Scope:** small · working: ~2.6k LOC repo with tests and four screenshots; no video or live demo. · polish: PRD-style README with personas and user stories.
**Claims:** PRD targets 90%+ rules parsed and 80% violations caught within 24 hours (goals, not results)
**Gaps:** No measured results; HP AI Studio role unclear
Sources: https://devpost.com/software/codence, evidence/sponsor-hp-nvidia-developer-challenge-2025-codence.json, sponsor_prompts_NVIDIA.jsonl

---

### Document Analysis Toolset
*HP & NVIDIA Developer Challenge 2025 · dataset: sponsor · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Second Place [2nd]

**What it is:** Streamlit document-forensics suite: detects and crops signatures in PDFs with a custom YOLO model, classifies signature forgeries with a fine-tuned ViT, and flags tampered regions using Error Level Analysis plus PDF version-history inspection.
**Problem / user:** Reviewers of contracts and financial or legal documents who need fast, objective checks for forged signatures and altered PDFs.

**Features**
- Signature detection and extraction — YOLO model (ONNX) finds signatures on every PDF page and offers crop downloads. *[shown_working]*
- Signature verification — ViT classifier compares two signatures and returns authenticity with confidence, side by side. *[shown_working]*
- Manipulation detection — Error Level Analysis highlights suspicious regions, including pasted-in signatures. *[shown_working]*
- PDF version history — Shows version changes in a document. *[shown_working]*
- Hosted multi-page app — Separate Streamlit pages per analysis type. *[shown_working]*

**Flow:** Upload a PDF → Detect and download signature crops → Compare two signatures for authenticity score → Run ELA and version-change views

**Prompt:** Build an AI web app using HP AI Studio tools that solves a real problem in one industry (automotive manufacturing, healthcare, finance, retail or technology); judged equally on AI innovation, demo and documentation, industry impact, and originality.
**Fit (explicit):** Trains custom models in HP AI Studio with MLflow tracking for a finance/legal document-fraud use case; README gives AI Studio install steps.  *(targeted: Second Place [2nd])*
**Sponsor tools:** HP AI Studio (Training, experimentation, MLflow model registry, core); NVIDIA GPU (RTX 4070 Ti Super) (Model training, supporting)
**AI:** Two custom-trained models: YOLOv11 signature detector exported to ONNX and a fine-tuned ViT forgery classifier; ELA is classical image analysis.
**Architecture:** Streamlit multi-page app calling ONNX YOLO and ViT (Hugging Face hosted) with PDF2Image preprocessing; training notebooks and MLflow registration in AI Studio.
**Novelty:** Combines model-based signature checks with classical forensic methods and version history in one non-technical tool; ships pretrained weights and a hosted app.
**Scope:** medium · working: Hosted Streamlit app, YouTube video, sample documents and pretrained models in repo. · polish: Detailed README with install and training sections, custom CSS, three screenshots.
**Claims:** Signature detection precision above 95% | Forgery classification accuracy above 90% | Multi-page documents processed in seconds
**Gaps:** Accuracy figures lack dataset or method; App not opened
Sources: https://devpost.com/software/document-analysis-toolset, evidence/sponsor-hp-nvidia-developer-challenge-2025-document-analysis-toolset.json, sponsor_prompts_NVIDIA.jsonl

---

### Medical Report Analyzer / Healthy Habits Recommender
*HP & NVIDIA Developer Challenge 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Bonus Honorable Mention: Healthcare

**What it is:** Flask web app where a user uploads a medical report (PDF or image), OCR extracts the text, and GPT produces a summary plus health-habit and food suggestions, packaged as an MLflow model for HP AI Studio.
**Problem / user:** People who receive annual checkup reports, forget the findings, and do not act on values needing improvement.

**Features**
- Report upload and OCR — Tesseract and PyMuPDF extract text from PDFs, scans and images. *[claimed]*
- Summaries — GPT summarizes findings, doctor notes and prescriptions. *[claimed]*
- Habit and food suggestions — Model proposes a few healthy habits and nutrition tips. *[claimed]*
- History-aware profile — Stores data per user and bases advice on all prior reports. *[claimed]*
- Duplicate detection — Avoids reprocessing the same upload. *[claimed]*
- AI Studio packaging — MLflow pyfunc model with Swagger UI and custom web app deployment. *[claimed]*

**Flow:** Upload report on web page → OCR extracts text → GPT prompt built → Receive summary, habit and food suggestions

**Prompt:** Build an AI web app using HP AI Studio tools that solves a real problem in one industry (automotive manufacturing, healthcare, finance, retail or technology); judged equally on AI innovation, demo and documentation, industry impact, and originality.
**Fit (explicit):** Healthcare use case orchestrated through HP AI Studio features (MLflow registry, Swagger, custom web app); the README lists the AI Studio features used.  *(targeted: Bonus Honorable Mention: Healthcare)*
**Sponsor tools:** HP AI Studio (MLflow registry, Swagger and web-app deployment, core)
**AI:** OCR then OpenAI GPT-4 prompts produce summaries and suggestions; a Llama registration script exists and the page also mentions local Llama 2.
**Architecture:** Static HTML demo frontend posts to a Flask backend that runs pytesseract/PyMuPDF OCR, calls OpenAI, and is wrapped as an MLflow pyfunc for AI Studio.
**Novelty:** Simple OCR-plus-LLM pipeline notable mainly for its end-to-end AI Studio packaging; no clinical validation.
**Scope:** tiny · working: YouTube demo and two screenshots; repo ~570 LOC in 9 files. · polish: README with structure, judging and setup sections; plain HTML UI.
**Claims:** Fully functional end-to-end upload-to-insight system
**Gaps:** Per-user history/duplicate features not seen in a small repo; No accuracy evidence
Sources: https://devpost.com/software/medical-report-analyzer-healthy-habits-recommender, evidence/sponsor-hp-nvidia-developer-challenge-2025-medical-report-analyzer-healthy-habits-recommender.json, sponsor_prompts_NVIDIA.jsonl

---

### Mira3D
*HP & NVIDIA Developer Challenge 2025 · dataset: sponsor · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Third Place [3rd]

**What it is:** Local pipeline that turns a short 2D video into an interactive 3D Gaussian-splat model: Birefnet removes backgrounds, COLMAP with CUDA reconstructs the scene, Brush renders splats, and a React Three Fiber web editor views and exports the result, run inside HP AI Studio.
**Problem / user:** Creators wanting realistic 3D models from phone-style video, locally and privately, for uses like retail, heritage, AEC and manufacturing.

**Features**
- Background removal — Birefnet ONNX model segments each frame. *[shown_working]*
- Photogrammetry reconstruction — CUDA-enabled COLMAP runs SfM and MVS on extracted frames. *[shown_working]*
- Gaussian splat rendering — Brush engine (Vulkan) trains and renders splats. *[shown_working]*
- In-browser viewer/editor — React Three Fiber interface to view and export models. *[shown_working]*
- MLflow artifact tracking — Exported binaries tracked in AI Studio. *[claimed]*
- Interactive splat editing — Advanced editing and refinement. *[planned]*

**Flow:** Provide a short video → Frames get backgrounds removed → COLMAP reconstructs → Brush renders splats → View and export in web editor

**Prompt:** Build an AI web app using HP AI Studio tools that solves a real problem in one industry (automotive manufacturing, healthcare, finance, retail or technology); judged equally on AI innovation, demo and documentation, industry impact, and originality.
**Fit (explicit):** Uses AI Studio containers, MLflow and Swagger with NVIDIA GPUs for on-prem 3D reconstruction aimed at retail, AEC and manufacturing; the README names these industries and AI Studio.  *(targeted: Third Place [3rd])*
**Sponsor tools:** HP AI Studio (Containerized deployment, MLflow tracking, Swagger, core); NVIDIA GPU/CUDA (COLMAP acceleration and splat training, core)
**AI:** Birefnet (ONNX) segmentation for preprocessing; Gaussian splatting for rendering; the rest is classical photogrammetry.
**Architecture:** Setup script installs COLMAP, FFmpeg, ImageMagick and Brush; notebooks drive the pipeline in AI Studio; React frontend with Three Fiber displays outputs.
**Novelty:** Fully local video-to-splat stack wrapped for a managed ML workstation; documents GPU/Vulkan container hurdles including Blackwell issues.
**Scope:** medium · working: YouTube demo and three screenshots; repo has ~1.7k LOC with frontend, notebooks and setup script. · polish: README with use cases and install steps; web editor.
**Gaps:** No performance numbers; Video not watched
Sources: https://devpost.com/software/mirai-5d98z3, evidence/sponsor-hp-nvidia-developer-challenge-2025-mira3d.json, sponsor_prompts_NVIDIA.jsonl

---

### OpenMed
*HP & NVIDIA Developer Challenge 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Bonus Best in Enterprise Computer Vision

**What it is:** A medical imaging web app where a user uploads a chest X-ray or brain MRI, per-disease ResNet50 classifiers return a diagnosis with confidence and Grad-CAM heatmap, and an OpenAI-backed chat explains results.
**Problem / user:** Clinicians, ER and rural/telemedicine providers short on radiology expertise who distrust black-box AI and need fast, explainable reads.

**Features**
- Pneumonia, TB and brain-tumor classification — Separate ResNet50 per condition with automatic routing; tumor model has three classes. *[claimed]*
- Grad-CAM heatmaps — Overlays highlight image regions that drove each prediction; example brain MRI shown in README. *[shown_working]*
- Confidence scoring — Numeric confidence with low/medium/high stratification. *[claimed]*
- Conversational agent — OpenAI GPT interprets intent, tracks multi-turn context and explains results in plain language. *[claimed]*
- OpenWebUI front end with FastAPI backend — Image upload and chat via OpenAI-compatible endpoints and microservices. *[shown_working]*
- MLflow tracking and HP AI Studio training — Models trained on AI Studio GPUs with experiment logging; checkpoints on Hugging Face. *[claimed]*
- Audit trail, HIPAA, FDA alignment — Stated without documentation. *[unclear]*

**Flow:** Download pretrained checkpoints → Open the OpenWebUI interface → Upload X-ray or MRI → System routes to matching model and returns diagnosis with confidence → View Grad-CAM overlay → Ask follow-up questions in chat

**Prompt:** Build an AI web app with HP AI Studio tools that solves a real problem in one industry (healthcare among them), judged on AI innovation, documentation, industry impact and originality.
**Fit (explicit):** Healthcare imaging app trained and deployed on HP AI Studio with MLflow; computer vision classifiers plus explainability for clinicians.  *(targeted: Bonus Best in Enterprise Computer Vision)*
**Sponsor tools:** HP AI Studio (GPU training, MLflow tracking, terminal-based deployment of services, core)
**AI:** Transfer-learned ResNet50 classifiers on three Kaggle datasets, Grad-CAM for explanation, OpenAI GPT as the chat/intent layer.
**Architecture:** OpenWebUI front end calls FastAPI with an OpenAI-compatible interface; services route images to per-disease PyTorch models, produce Grad-CAM, and the LLM composes explanations; MLflow tracks training.
**Novelty:** Pairs three imaging models with explainability and a chat agent inside an existing chat UI; heavy emphasis on trust and interpretability writing.
**Scope:** medium · working: About 11k lines, 69 Grad-CAM result files, Hugging Face checkpoints and reported test accuracies; no video or live demo. · polish: Long README and docs folder with screenshots; no tests or Docker file.
**Claims:** Test accuracy 96.5% pneumonia, 98.7% TB, 97.2% brain tumor | Under 3 seconds per image | HIPAA and FDA-aligned design
**Gaps:** no video; no external validation
Sources: https://devpost.com/software/openmed-gtp792, https://github.com/sriharshapy/openMed, https://hpaistudio.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

### Orpheus Engine
*HP & NVIDIA Developer Challenge 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Bonus Honorable Mention: Technology

**What it is:** A digital audio workstation that runs in Electron and the browser, paired with an AI agent meant to analyze recordings, transcribe speech and slice clips on search. Author admits many intended features exist only as mockups.
**Problem / user:** Audio professionals who want AI-assisted restoration, analysis and export of recordings across devices, with plugins. No explicit problem statement on the page.

**Features**
- DAW workspace — Editing, analysis and export of audio in Electron, later adapted to run in a browser; screenshot of the Electron app. *[shown_working]*
- Agent analysis of recordings — RAG-style agent identifies useful clips or suggests edits. *[claimed]*
- Transcription and search-based slicing — Speech is transcribed and sections are cut based on a user search. *[claimed]*
- Bluetooth/nRF recording input — Record from Bluetooth devices straight into the DAW; not fully tested. *[claimed]*
- Plugin system and store — Supports VST, Python, TypeScript and dApp plugins; author says untested. *[unclear]*
- Web3 export, minting, IP protection via Story — Decentralized audio export route. *[planned]*

**Flow:** Open the DAW (Electron or browser) → Record audio from a Bluetooth device → Agent analyzes the recording → Transcribe speech and slice by search → Export audio with metadata or the transcript

**Prompt:** Build an AI web app with HP AI Studio tools that solves a real problem in one industry (automotive, healthcare, finance, retail or technology), judged on AI innovation, documentation, impact and originality.
**Fit (implied):** Technology-industry tool; says a Hugging Face model was later run on HP AI Studio, and MLflow/Jupyter demos informed design. GPU use for heavy plugins is claimed.  *(targeted: Bonus Honorable Mention: Technology)*
**Sponsor tools:** HP AI Studio (hosting the model, CPU/GPU for plugins, MLflow and Jupyter patterns from its demos, supporting)
**AI:** Hugging Face model (later moved to HP AI Studio) powering an agent with retrieval over audio data and speech transcription; author notes heavy use of AI to write the code.
**Architecture:** TypeScript/React client (82 files) in Electron or browser, a Python/GraphQL server for the agent and model, plus a plugin layer.
**Novelty:** An entire DAW rather than a single-purpose AI tool, with ambitions for plugin store and Web3 export; largely aspirational.
**Scope:** medium · working: About 16k lines in client and server directories and an Electron screenshot; no video or demo link. · polish: Author states features are mockups; no tests detected in the evidence scan; README empty in evidence.
**Claims:** Supports VST, Python, TypeScript and dApp plugins | Records directly from Bluetooth and MADI devices
**Gaps:** README text empty in evidence; no video
Sources: https://devpost.com/software/orpheus-engine, evidence/orpheus-engine.json, https://hpaistudio.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

### QuantumFinance AI
*HP & NVIDIA Developer Challenge 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Bonus Honorable Mention: Finance

**What it is:** A web stock-research platform whose FastAPI backend routes requests to Perplexity models for sector dashboards, news summaries, sentiment, risk, deep-research reports and time-boxed trading strategies, plus a finance Q&A assistant. React front end deployed on Vercel.
**Problem / user:** Everyday investors who find financial analysis tools too complex or expensive.

**Features**
- Market dashboard — Shows dominant narratives per sector, momentum companies and market mood. *[shown_working]*
- AI stock research report — Perplexity deep-research pipeline writes a narrative report with projections. *[claimed]*
- Trading strategies — Reasoning model uses Alpha Vantage price history for intraday, weekly or monthly ideas. *[claimed]*
- News, sentiment and risk — Per-stock endpoints summarize 30 days of news, sentiment drivers and top risks. *[claimed]*
- Stock Assist chat — General finance Q&A, e.g. summarizing an earnings report. *[claimed]*
- MLflow prompt logging — Prompt versions and outputs logged and model deployed from HP AI Studio. *[claimed]*

**Flow:** Open dashboard for sector topics and mood → Search a ticker → View research, strategy, sentiment and risk tabs → Read news summaries → Ask Stock Assist a question

**Prompt:** Build an AI web app with HP AI Studio tools that solves a real problem in one industry (automotive, healthcare, finance, retail or technology), judged on AI innovation, documentation, impact and originality.
**Fit (explicit):** Finance-industry app; backend developed in HP AI Studio containers and logged/deployed via its MLflow, README gives steps for deploying through the studio.  *(targeted: Bonus Honorable Mention: Finance)*
**Sponsor tools:** HP AI Studio (containerized dev workspace, MLflow prompt/model logging and deployment, supporting); NVIDIA GPU libraries (cited generally as preinstalled, token)
**AI:** Hosted Perplexity LLMs with live web search (standard, deep research, reasoning) orchestrated by a central router; hundreds of prompt variations tuned; no actual fine-tuning shown despite writeup mentioning it.
**Architecture:** React frontend calls a FastAPI service (main.py, strategy.py) that dispatches to Perplexity endpoints and Alpha Vantage, wrapped as an MLflow model in HP AI Studio.
**Novelty:** Thin orchestration over third-party LLM APIs; distinguishing choice is separating research, sentiment, risk and strategy into dedicated prompts and models.
**Scope:** small · working: Live Vercel demo link, deployable FastAPI backend and React frontend, about 5k lines. · polish: README with judging steps and two screenshots; no tests or video.
**Claims:** Gives every investor a strategic advantage
**Gaps:** no video; no metrics
Sources: https://devpost.com/software/quantumfinance-ai, https://github.com/Husky-AI9/QuantumFinanceAI (evidence README), https://hpaistudio.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

### Sophia
*HP & NVIDIA Developer Challenge 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Bonus Best in Gen AI

**What it is:** A crypto intelligence web platform: chat with a LoRA-fine-tuned Phi-3-Mini finance model, get news-RAG answers, sentiment over 100+ coins, paper-trade a portfolio and receive auto-generated daily podcast summaries.
**Problem / user:** Novice and experienced crypto retail traders overwhelmed by the pace of news, sentiment and market data.

**Features**
- Finance chat model — Phi-3-Mini-128k fine-tuned with LoRA (8-bit) on Finance-Instruct-500k, served via an OpenAI-compatible Flask wrapper; Deep Research and Agent modes. *[claimed]*
- News RAG — RSS articles from four crypto outlets embedded in Milvus for context-aware answers. *[claimed]*
- Sentiment across 100+ coins — VADER and TextBlob scored over 11,000+ scraped articles. *[claimed]*
- Paper trading portfolio — Track holdings and trade with live CoinGecko prices, no real money. *[claimed]*
- Daily podcast generation — Automated daily market summaries turned into podcasts. *[claimed]*
- Auth and rate limiting — Google OAuth, SQLite user store, per-user limits. *[claimed]*
- Alerts, wallet and exchange links, real trading — Rebalancing, alerts, MetaMask/Binance connections. *[planned]*

**Flow:** Land on site and sign in with Google → Open chat and ask market questions → Check sentiment tools → Build a paper portfolio and trade → Listen to daily podcast

**Prompt:** Build an AI web app with HP AI Studio tools solving a real problem in one industry (finance among them), judged on AI innovation, documentation, impact and originality.
**Fit (explicit):** Fine-tunes and serves a language model on HP AI Studio with MLflow, adding RAG and agents for a finance (crypto) audience.  *(targeted: Bonus Best in Gen AI)*
**Sponsor tools:** HP AI Studio (GPU fine-tuning, MLflow model serving, inference API wrapped by Flask, core)
**AI:** LoRA-fine-tuned Phi-3-Mini, LangChain agents, Milvus vector RAG over scraped news, lexicon sentiment (VADER/TextBlob), generated podcast scripts.
**Architecture:** React/TypeScript front end, Node/Express backend with SQLite, Flask OpenAI-compatible wrapper to the AI Studio model, Milvus and MLflow in Docker, RSS scrapers and CoinGecko feeds.
**Novelty:** Combines fine-tuned model, RAG, sentiment, paper trading and podcasts in one product with a live domain; broad scope for a challenge entry.
**Scope:** large · working: Live site and repo link per Devpost; screenshots of landing, chat and portfolio views. · polish: Auth, rate limiting and multi-page UI described; repo not readable here so unverified.
**Claims:** 11,000+ articles analyzed across 100+ cryptocurrencies | Describes itself as production-ready
**Gaps:** repo clone failed and raw README fetch failed; no video
Sources: https://devpost.com/software/sophia-76ueiq, https://hpaistudio.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

### TryOn
*HP & NVIDIA Developer Challenge 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Bonus Honorable Mention: Retail

**What it is:** A local virtual clothing try-on demo: a Flask page where the user uploads a photo and a garment, and a CatVTON diffusion model served as an MLflow-compatible model composites the garment onto the person.
**Problem / user:** Online shoppers unsure how clothes will look who also do not want to upload personal photos to the cloud.

**Features**
- Virtual try-on — Body segmentation plus diffusion inpainting blends a chosen garment into the user photo. *[shown_working]*
- Local, offline inference — Pipeline runs on the user machine so images never leave it. *[claimed]*
- Web demo UI — Drag-and-drop upload, preview, adjustable inference steps (10-50) and clothing type (upper, lower, full). *[shown_working]*
- Model registration on AI Studio — register_model.py registers and tests the model with versioning. *[claimed]*
- Text-to-image garment search — Find clothes by description. *[planned]*

**Flow:** Register model and start backend → Launch demo app on port 7860 → Upload a person photo → Pick garment, type and steps → Preview generated try-on

**Prompt:** Build an AI web app with HP AI Studio tools that solves a real problem in one industry (automotive, healthcare, finance, retail or technology), judged on AI innovation, documentation, impact and originality.
**Fit (explicit):** Retail use case; model registered, versioned and served via HP AI Studio with MLflow-compatible backend; README recommends AI Studio setup on a GPU.  *(targeted: Bonus Honorable Mention: Retail)*
**Sponsor tools:** HP AI Studio (model registration, versioning, GPU project and deployment, core)
**AI:** Pretrained CatVTON virtual try-on diffusion model with segmentation, wrapped for inference; no training described.
**Architecture:** Flask demo app posts images to an MLflow-compatible model server loaded with CatVTON components; results stored in a results folder.
**Novelty:** Emphasizes privacy-preserving on-device try-on; largely repackages an existing open model, repo contains many notebook files.
**Scope:** small · working: Runnable demo and backend scripts with sample images; large repo (950 files, mostly notebook assets); no live link or video. · polish: Clear setup README and responsive UI description; one screenshot on Devpost.
**Claims:** Images never leave the device | High realism while lightweight
**Gaps:** no video; no quantitative results
Sources: https://devpost.com/software/tryon-woi0bh, https://github.com/krishnaadithya/tryon (evidence README), https://hpaistudio.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

