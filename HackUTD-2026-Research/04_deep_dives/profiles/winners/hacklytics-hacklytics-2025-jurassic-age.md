# Hacklytics — Hacklytics - 2025: Jurassic Age (10 projects)

### Banana Search
*Hacklytics Hacklytics - 2025: Jurassic Age · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Second in Finance [2nd]

**What it is:** Next.js meal-planning web app: type a dish, get a generated recipe, upload a fridge photo to find missing ingredients, then pick local grocery stores and see store-specific prices and a total for an editable shopping list.
**Problem / user:** Home cooks facing high food prices who overspend or waste food when deciding what to cook and buy.

**Features**
- Recipe generation — User enters a dish; LLM-style endpoint returns ingredient list and steps. *[claimed]*
- Fridge photo missing-ingredient detection — Uploaded fridge image is compared with recipe ingredients to find what is missing. *[claimed]*
- Store price comparison — Custom API endpoints and curl-derived store requests fetch location-specific grocery prices and totals. *[claimed]*
- Editable shopping list — Quantities and totals recalculate per selected store. *[shown_working]*
- Auth with email, Google, GitHub — Supabase sign-up and login. *[shown_working]*
- Session persistence — React state plus localStorage keep list and missing items. *[shown_working]*

**Flow:** Sign up or log in → Enter a dish and get a recipe → Upload fridge photo → Select grocery stores → Compare prices and total → Edit shopping list

**Prompt:** Finance track (sponsored by Capital One): build a creative solution using financial data and technology to improve financial services and simplify user experiences.
**Fit (implied):** Frames the app as budgeting help: grocery price comparison and shopping-list totals to cut food spending, rather than market or fintech data.  *(targeted: Second in Finance)*
**AI:** Recipe generation and fridge-image ingredient recognition via unnamed models; Devpost tags LangChain and Langflow but page does not confirm model use.
**Architecture:** Next.js/React/TypeScript front end with Supabase auth; Python backend folder with API endpoints calling grocery store APIs; results normalized and cached in localStorage.
**Novelty:** Chains recipe generation, fridge vision and live grocery price scraping in one budgeting flow; reverse-engineered store requests by store ID.
**Scope:** small · working: Embedded demo video and screenshots; repo about 3,100 LOC across app and backend. · polish: Auth, responsive UI, editable lists; README is detailed but has no setup steps.
**Claims:** Could save users time and money by optimizing shopping lists
**Gaps:** model used for recipes and vision not named; grocery APIs unnamed; video not watched
Sources: https://devpost.com/software/banana-search-ueb89p, evidence/hacklytics-hacklytics-2025-jurassic-age-banana-search.json, https://hacklytics2025.devpost.com/

---

### Basketball Positioning Neural Network and Kmean Cluster
*Hacklytics Hacklytics - 2025: Jurassic Age · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Third in Sports [3rd]

**What it is:** A Google Colab data-science notebook on a supplied basketball CSV: KMeans groups players into positions from in-game stats, and linear regression studies how a player performs against specific defenders, with matchup visualizations.
**Problem / user:** Analysts and teams wanting matchup-level insight; author says matchup statistics are overlooked versus shooting efficiency.

**Features**
- KMeans position clustering — Clusters players by in-game statistics after standardization and feature engineering. *[claimed]*
- Linear regression on matchups — Predicts player outcomes against particular defenders. *[claimed]*
- Matchup visualizations — Charts of specific player-versus-defender statistics. *[claimed]*
- Strategy questions — Offensive approach against a defender; best defender for an opponent; shooting tendencies. *[claimed]*

**Flow:** Load the Hacklytics-provided CSV in Colab → Standardize and engineer features → Run KMeans and regression → View matchup plots

**Prompt:** Sports track: apply data science and machine learning to sports analytics such as historical data, scorekeeping and player statistics.
**Fit (implied):** Applies clustering and regression to supplied player and defender data to explore matchup strategy.  *(targeted: Third in Sports)*
**AI:** Classical ML: KMeans clustering and linear regression; despite the title no neural network is described.
**Architecture:** Single Python notebook in Colab reading the provided CSV, preprocessing, fitting KMeans and regression, plotting results.
**Novelty:** Focuses on player-versus-defender matchup statistics; author frames it as a first self-taught ML project with a one-night scope.
**Scope:** tiny · working: Devpost describes results qualitatively; repo contains only a title README and no code files seen. · polish: No metrics, video or screenshots reported.
**Gaps:** repo holds no code, README is one line; no metrics; how-we-built-it section empty
Sources: https://devpost.com/software/basketball-positioning-neural-network-and-kmean-cluster, evidence/hacklytics-hacklytics-2025-jurassic-age-basketball-positioning-neural-network-and-kmean-cluster.json, https://hacklytics2025.devpost.com/

---

### Cipher AI
*Hacklytics Hacklytics - 2025: Jurassic Age · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Third in Cybersecurity [3rd]

**What it is:** Web tool for linguistic steganography: a user types a secret message and receives natural-sounding cover text containing it, plus a password-protected JSON key file for decoding. GPT-4o builds the keyword dictionary and encoded text.
**Problem / user:** Activists and people under censorship who need messages that do not look encrypted, unlike RSA ciphertext which flags the sender.

**Features**
- Secret message to cover text — Backend picks keywords by tweet word frequency and has GPT-4o weave them into natural text. *[claimed]*
- Password-protected key file — Returns a JSON file holding the decryption key. *[claimed]*
- Keyword selection from tweet data — Sentiment140 subset used to rank candidate words and tune key generation. *[claimed]*
- React interface with Flask backend — Message entry page calling a Python API. *[shown_working]*

**Flow:** Type secret message in the React page → Backend selects keywords and generates cover text → Receive cover text and password-protected key file → Share text on ordinary platforms

**Prompt:** Cybersecurity track: tackle data-driven cybersecurity problems by protecting sensitive information, detecting threats and keeping systems intact.
**Fit (implied):** Protects sensitive messages by hiding them in plausible speech instead of visible encryption, to avoid detection.  *(targeted: Third in Cybersecurity)*
**AI:** GPT-4o prompted to create a keyword dictionary and the encoded message; NLTK/pandas used on Sentiment140 tweets for word frequency.
**Architecture:** React frontend posts message to Flask backend; backend ranks keywords from tweet data, calls OpenAI API, returns cover text and encrypted key JSON.
**Novelty:** Steganography via LLM-generated natural text rather than image or file hiding; team says undetectability is unverified.
**Scope:** small · working: Two screenshots and an end-to-end React/Flask build; repo has some tests, about 650 LOC. · polish: Detailed README mirrors Devpost; no video or live demo.
**Claims:** Tackles an open research problem in linguistic steganography | Few existing tools offer simple covert codes for everyday platforms
**Gaps:** no detectability measurements; decoding flow not described in detail
Sources: https://devpost.com/software/cipher-ai, evidence/hacklytics-hacklytics-2025-jurassic-age-cipher-ai.json, https://hacklytics2025.devpost.com/

---

### Deqo
*Hacklytics Hacklytics - 2025: Jurassic Age · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Second in Cybersecurity [2nd]

**What it is:** Marketplace for idle compute: buyers upload Docker images as jobs, lenders run them through a web portal or Python CLI, and outputs return through S3. Claims blockchain-style verification, AES-GCM encryption and an autorun scheduling mode.
**Problem / user:** AI researchers and small businesses needing cheaper compute than AWS or GCP; lenders with idle machines who want income.

**Features**
- Docker job upload and execution — Buyer uploads image; lender container run isolated; output files downloadable. *[shown_working]*
- Lender CLI — Runs a job from its ID with Supabase RLS authentication. *[claimed]*
- Autorun scheduling — CLI picks and runs jobs at lender-preset times, offline-capable. *[claimed]*
- Hardware-based job matching — AI matches jobs to lender specs and verifies requirements. *[claimed]*
- Encrypted transfer and verification — AES-GCM with asymmetric authentication, S3 transfer and blockchain-style integrity proof. *[claimed]*
- Dashboard — Job monitoring, earnings, availability settings, payments. *[shown_working]*

**Flow:** Buyer uploads Docker image in portal → Lender browses jobs matching hardware or enters job ID in CLI → Container runs in isolation → Output returned via S3 → Buyer downloads results

**Prompt:** Cybersecurity track: tackle data-driven cybersecurity problems by protecting sensitive information, detecting threats and keeping systems intact.
**Fit (implied):** Emphasizes secure execution of untrusted code: container isolation, encryption and verification of computation results, framed as security of a decentralized marketplace.  *(targeted: Second in Cybersecurity)*
**AI:** Page says AI handles job-hardware matching, scheduling and requirement checks; models not named.
**Architecture:** Next.js frontend on Netlify; FastAPI on EC2 with ECR for images, S3 for data, Supabase for state/auth; Python CLI on lender side; verification layer.
**Novelty:** End-to-end compute marketplace with a lender CLI and autorun mode; large frontend plus 24k LOC repo built in a weekend.
**Scope:** medium · working: Live Netlify site, embedded video, six screenshots; repo has frontend, backend, cli and example jobs. · polish: Dashboard, scheduling UI and README with feature list; no tests.
**Claims:** Built a production-ready platform in 36 hours | Blockchain ensures all computations are verified
**Gaps:** chain not named; distributed task splitting is future work; video not watched
Sources: https://devpost.com/software/deqo, evidence/hacklytics-hacklytics-2025-jurassic-age-deqo.json, https://hacklytics2025.devpost.com/

---

### MedX
*Hacklytics Hacklytics - 2025: Jurassic Age · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Second in Healthcare [2nd]

**What it is:** React Native/Expo medication tracker: log prescriptions by barcode scan or manually, check drug interactions with Gemini and OpenFDA data, chat with a health assistant, journal symptoms, and export AI-generated medication reports.
**Problem / user:** Individuals managing multiple medications who lack quick access to professionals for interaction questions.

**Features**
- Barcode and manual medication logging — Scanned codes are reformatted and looked up in OpenFDA. *[claimed]*
- AI drug-interaction checker — Gemini analyzes the log and sorts interactions by severity thresholds. *[claimed]*
- Health chatbot — Gemini-based assistant answers medical queries and FAQs. *[claimed]*
- Journal — Entries for symptoms and progress. *[claimed]*
- Shareable medication report — Generative AI builds a downloadable report. *[claimed]*
- Firebase auth, profile, dashboard — Login and personalization screens appear in screenshots. *[shown_working]*

**Flow:** Sign up or log in → Add a medication by scan or manual entry → Review interaction risk → Ask the chatbot → Generate and share report

**Prompt:** Healthcare track: analyze large healthcare datasets with health informatics and computational modeling for public-health or biomedical problems.
**Fit (implied):** Uses public drug data (OpenFDA) and generative AI to support personal medication safety and decisions.  *(targeted: Second in Healthcare, Best Use of Gemini (MLH, possible))*
**Sponsor tools:** Google Gemini API (chatbot, interaction analysis and report generation, core)
**AI:** Gemini API powers the chat assistant, severity-tiered interaction analysis and report text; README also mentions OCR of drug labels.
**Architecture:** Expo React Native app with Firebase auth and storage; barcode data queries OpenFDA; Gemini API called for analysis, chat and reports.
**Novelty:** Combines barcode lookup, severity-tiered interaction output and shareable AI reports in a mobile app.
**Scope:** medium · working: Embedded demo video and screenshots; repo about 8,300 LOC with 34 app files. · polish: README lists features, setup and APIs; animations noted; no tests.
**Gaps:** no accuracy checks of interactions; video not watched
Sources: https://devpost.com/software/medx-d7tle6, evidence/hacklytics-hacklytics-2025-jurassic-age-medx.json, https://hacklytics2025.devpost.com/

---

### MIR.AI - AI Driven, Efficient MRI Super-Resolution
*Hacklytics Hacklytics - 2025: Jurassic Age · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Third in Healthcare [3rd]

**What it is:** Unpaired image-to-image model aiming to turn 1.5T MRI scans into 3T-quality images, using Contrastive Unpaired Translation in PyTorch Lightning, with a backend for image handling and a React/TypeScript frontend.
**Problem / user:** Patients and providers in resource-limited regions where 3T scanners are too costly.

**Features**
- 1.5T to 3T style super-resolution — CUT-based unpaired translation model trained on unpaired scans. *[claimed]*
- Image processing backend — Dedicated service handles upload and inference. *[claimed]*
- React/TypeScript UI — Frontend integrated with the backend. *[shown_working]*
- Parameter testing — Hyperparameter experiments to tune the model. *[claimed]*

**Flow:** Upload a lower-field MRI image in the web UI → Backend runs the translation model → View enhanced output

**Prompt:** Healthcare track: analyze large healthcare datasets with health informatics and computational modeling for public-health or biomedical problems.
**Fit (implied):** Uses imaging data and ML to widen access to diagnostic-quality MRI in underserved settings.  *(targeted: Third in Healthcare)*
**AI:** Contrastive Unpaired Translation GAN-style model in PyTorch Lightning; no paired ground truth for validation.
**Architecture:** Colab-trained model in a model folder; Python backend for image handling; React/TypeScript web frontend.
**Novelty:** Applies unpaired image translation to field-strength upgrading; team states lack of paired data blocked validation.
**Scope:** medium · working: Demo video embedded; repo has web, model, backend and test directories. · polish: README with overview and team roles; no quantitative metrics reported.
**Claims:** Transforms 1.5T images to 3T quality
**Gaps:** no image-quality metrics; training data source unnamed; file count inflated by committed node_modules
Sources: https://devpost.com/software/ai-driven-efficient-mri-super-resolution, evidence/hacklytics-hacklytics-2025-jurassic-age-mir-ai-ai-driven-efficient-mri-super-resolution.json, https://hacklytics2025.devpost.com/

---

### PerfectPunch
*Hacklytics Hacklytics - 2025: Jurassic Age · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Second in Sports [2nd]

**What it is:** Sensor-free boxing trainer using a webcam: MediaPipe/OpenCV track the body, a custom PyTorch model classifies punches, a Taipy dashboard shows speed, accuracy and risk metrics, and a Gemini chatbot gives coaching and workout plans.
**Problem / user:** Boxers from amateur to pro who get only subjective coaching and face concussion risk.

**Features**
- Real-time pose tracking — OpenCV and MediaPipe analyze punch form and biomechanics. *[claimed]*
- Punch type classification — Custom PyTorch model uses wrist and elbow motion points. *[claimed]*
- Injury and concussion risk metrics — Assesses defensive stance, form weaknesses and high-risk impact zones. *[claimed]*
- Taipy dashboard — Reaction time, per-category accuracy, dodging, stance and leg analysis. *[claimed]*
- Gemini coaching feedback and chatbot — Personalized recommendations, workout plans and recovery tips. *[claimed]*

**Flow:** Throw punches in front of a webcam → System tracks and classifies punches → Dashboard shows metrics and risk → Gemini feedback and chatbot give advice

**Prompt:** Sports track: apply data science and machine learning to sports analytics such as historical data, scorekeeping and player statistics.
**Fit (implied):** Applies computer vision and ML to athlete performance data with an injury-prevention angle.  *(targeted: Second in Sports)*
**Sponsor tools:** Google Gemini API (LLM coaching feedback and chatbot, supporting)
**AI:** MediaPipe pose estimation feeds a custom PyTorch punch classifier; Gemini gives text coaching and injury alerts.
**Architecture:** Django backend with OpenCV/MediaPipe pipeline and PyTorch model, Taipy dashboard, Matplotlib charts, Gemini API; HTML/CSS/JS frontend.
**Novelty:** Hardware-free punch classification plus injury-risk framing; cites boxing brain-injury statistics.
**Scope:** small · working: Seven screenshots on Devpost; repo unreadable so build size unknown. · polish: No video; metrics are not reported.
**Claims:** 87% of pro boxers have chronic brain injury (cited background) | No sensors or external hardware required
**Gaps:** repo clone and raw README fetch failed; no video; classifier accuracy unknown
Sources: https://devpost.com/software/perfectpunch, https://hacklytics2025.devpost.com/

---

### Sympli
*Hacklytics Hacklytics - 2025: Jurassic Age · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Third in Generative AI [3rd]

**What it is:** Web platform where chronic-illness patients log symptoms by chatting with a Gemini 2.0 assistant, and both patients and physicians see Recharts line graphs of symptom frequency by month. Separate patient and physician logins via Firebase.
**Problem / user:** Patients with chronic conditions and physicians who lack timely, structured symptom histories.

**Features**
- Gemini symptom-intake chatbot — Asks tailored follow-ups and records answers. *[shown_working]*
- Symptom parsing and storage — Responses cleaned and written to Firestore in real time. *[claimed]*
- Symptom frequency charts — Month vs frequency lines, one per symptom, plus cluster views. *[shown_working]*
- Patient and physician roles — Firebase Authentication with protected routes. *[shown_working]*
- HIPAA, record documentation, environment correlation — Listed as next steps. *[planned]*

**Flow:** Sign in as patient or physician → Chat with Gemini about symptoms → Data stored in Firestore → View symptom trend graphs → Physician reviews charts

**Prompt:** Generative AI track: explore generative AI from creative work to AI solutions for complex real-world problems.
**Fit (explicit):** Uses a generative chatbot to turn conversation into structured symptom data for clinicians, a real-world health application of generative AI.  *(targeted: Third in Generative AI, Healthcare (also entered))*
**Sponsor tools:** Google Gemini API (conversational symptom intake, core)
**AI:** Gemini 2.0 prompted to ask follow-up questions and extract symptoms from chat text.
**Architecture:** React/TypeScript frontend (shadcn/ui, Recharts) on Firebase Hosting; Cloud Run/Node backend with Gemini; Firestore and Firebase Auth.
**Novelty:** Conversational data capture feeding clinician-facing trend graphs; SMS delivery was dropped due to number verification.
**Scope:** small · working: Live Firebase site, demo video, README quickstart; about 2,900 LOC. · polish: Typed React UI, env example files, dual roles.
**Claims:** 60% of Americans have a chronic condition (background) | Comprehensive automated testing (no tests seen in repo)
**Gaps:** no clinical validation; video not watched
Sources: https://devpost.com/software/sympli, evidence/hacklytics-hacklytics-2025-jurassic-age-sympli.json, https://hacklytics2025.devpost.com/

---

### TaxDaddy
*Hacklytics Hacklytics - 2025: Jurassic Age · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 3rd Place Hack [3rd]

**What it is:** Voice tax assistant: users upload tax documents, then phone a Twilio number and talk to a real-time OpenAI voice agent that answers questions from the documents, fills tax forms, flags anomalies and fraud risk, and emails the finished forms.
**Problem / user:** Individuals who find filing taxes tedious and want an accountant-like helper.

**Features**
- Document upload with OCR — Extracts and summarizes fields from arbitrary files into MongoDB. *[claimed]*
- Phone voice agent — Twilio audio streams over WebSockets to the OpenAI real-time API. *[shown_working]*
- RAG over documents — Voice agent answers questions about uploaded files. *[claimed]*
- Auto form filling — Identifies needed forms, fills fields via PyPDF filler, emails for signing. *[claimed]*
- Anomaly detection — Compares similar extracted fields for inconsistencies. *[claimed]*
- Benford fraud scoring — Compares digit distributions to Benford to give risk score. *[claimed]*
- Analytics and visualizations — Fine-tuned model produces insights and charts. *[claimed]*

**Flow:** Upload tax documents → OCR extracts data → Call the Twilio number → Ask questions and request analytics → Agent fills forms and flags risks → Forms emailed to user

**Prompt:** Finance track (sponsored by Capital One): build a creative solution using financial data and technology to improve financial services and simplify user experiences.
**Fit (implied):** Page does not name a track; it applies financial documents, voice AI and fraud analytics to simplify tax filing.  *(targeted: 3rd Place Hack, Finance track (likely))*
**AI:** OpenAI real-time voice agent with tools and RAG over OCRed documents; a fine-tuned model for insights; statistical Benford checks.
**Architecture:** Twilio call audio via WebSocket to OpenAI real-time API; Python backend with MongoDB store, OCR, PyPDF filling; React/Vite frontend for uploads.
**Novelty:** Phone-call interface to a document-aware agent with Benford-law fraud scoring and autonomous PDF form filling.
**Scope:** medium · working: Demo video and six screenshots; repo about 10k LOC with backend and frontend. · polish: README is the Vite template; no live demo.
**Gaps:** no accuracy metrics; video not watched; prize title not tied to a track
Sources: https://devpost.com/software/taxdaddy, evidence/hacklytics-hacklytics-2025-jurassic-age-taxdaddy.json, https://hacklytics2025.devpost.com/

---

### thera_pixel
*Hacklytics Hacklytics - 2025: Jurassic Age · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 2nd Place Hack [2nd]

**What it is:** Webcam physical-therapy app: MediaPipe 3D pose tracks the patient. Pizza Pursuit turns arm exercises into pixel-art pizza making, while Practice Studio times each motion and gives pacing and form feedback against ground-truth movements built from a rehab dataset.
**Problem / user:** Physical therapy patients who struggle to keep up prescribed home exercises.

**Features**
- Pizza Pursuit game — Arm movements advance pizza-making scenes in pixel art. *[claimed]*
- Practice Studio — Timer cues each motion and compares user arm angle to expected angle. *[claimed]*
- Real-time pose tracking — OpenCV and MediaPipe 3D pose give joint angles from live video. *[claimed]*
- Pace feedback — Tells user to speed up or slow down repetitions. *[claimed]*
- Ground truth from IntelliRehabDS — Dataset cleaned and temporally interpolated into reference progressions. *[claimed]*

**Flow:** Open web app → Choose Pizza Pursuit or Practice Studio → Camera tracks exercise → Receive game progress or pacing feedback

**Prompt:** Healthcare track: analyze large healthcare datasets with health informatics and computational modeling for public-health or biomedical problems.
**Fit (implied):** Uses a motion dataset and pose estimation to make rehab exercises engaging and checkable at home.  *(targeted: 2nd Place Hack)*
**AI:** MediaPipe pose estimation; learned models for ground truth were tried and abandoned for timer-based reference comparison.
**Architecture:** Flask web app with HTML/JS, OpenCV/MediaPipe processing, and NumPy/SciPy ground-truth data derived from IntelliRehabDS.
**Novelty:** Gamifies rehab with pixel-art game plus separate form studio; built reference trajectories from a small dataset.
**Scope:** small · working: Nine screenshots and embedded video; repo includes Flask templates and static assets. · polish: README is two lines; repo holds large dataset files.
**Gaps:** no accuracy metrics; prize title does not name a track; LOC inflated by dataset
Sources: https://devpost.com/software/rehab-fv6j1l, evidence/hacklytics-hacklytics-2025-jurassic-age-thera-pixel.json, https://hacklytics2025.devpost.com/

---

