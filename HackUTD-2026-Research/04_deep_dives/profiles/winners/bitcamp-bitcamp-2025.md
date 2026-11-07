# Bitcamp — Bitcamp 2025 (33 projects)

### Airwaves
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Gamification Hack - Bitcamp

**What it is:** A browser rhythm game played hands-free: TensorFlow.js HandPose tracks the player's hand via webcam and turns poses into note hits, clicks, scrolls and menu gestures, with 3D visuals in React Three Fiber.
**Problem / user:** People with limited mobility or in recovery who want accessible ways to interact with technology, and a game framing for hand-mobility exercise that therapists could follow.

**Features**
- Webcam hand-tracking game controls — TensorFlow.js HandPose detects landmarks in real time; hand motions hit beat-timed targets *[shown_working]*
- Hand poses as mouse input — Gestures translated into clicks, scrolls and other actions *[shown_working]*
- Gesture menu and volume control — OpenCV.js handles menu navigation and volume adjustment by hand *[claimed]*
- 3D rhythm gameplay — React Three Fiber and Three.js render the note lane with CSS animations *[shown_working]*
- Clone Hero chart support — Reads Clone Hero mapping files for song charts *[claimed]*
- Therapy-inspired gestures — Motions modeled on physical-therapy hand mobility exercises *[claimed]*
- Custom songs, analytics, accessibility settings — Song upload, therapist analytics, motion sensitivity and tempo options, low-end optimization *[planned]*

**Flow:** Open the hosted site and enable webcam → Navigate menus and volume with hand gestures → Pick a song → Hit beat-timed targets with hand motions → Score as notes are hit

**Prompt:** Best Gamification Hack: a hack that gamifies an everyday task.
**Fit (implied):** Turns hand-mobility exercise and everyday computer interaction into a rhythm game; README labels it a winner of the gamified hack prize.  *(targeted: Best Gamification Hack - Bitcamp)*
**AI:** TensorFlow.js HandPose model for real-time hand landmark detection driving gesture recognition; OpenCV.js for menu/volume gestures.
**Architecture:** React and TypeScript front end with React Three Fiber scene; webcam frames go to TF.js hand-pose model in browser, gestures map to game and UI events; Python/OpenCV directory present in repo.
**Novelty:** Fully browser-based hand-tracked rhythm game that doubles as a gesture mouse; accessibility and therapy framing.
**Scope:** small · working: Live Vercel demo, hosted copy, YouTube demo; about 1.9k LOC repo with run instructions. · polish: 3D visuals and animations; short README; no tests; challenges with lighting and false gestures noted.
**Claims:** Built working prototype in under 36 hours | Could have real therapeutic benefits (no data)
**Gaps:** Video not watched; Devpost tags list Python/OpenCV; README says OpenCV.js; both recorded
Sources: https://devpost.com/software/airwaves-342g1j, evidence/bitcamp-bitcamp-2025-airwaves.json (README), https://bitcamp2025.devpost.com/

---

### Bird Box
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Razzle Dazzle Hack - Bitcamp

**What it is:** A mobile-first web game in the spirit of Pokemon Snap where players pick a local bird on a map, photograph it, and get ML species classification, bird segmentation, and a photo-quality rating, with finds saved to a BirdDex.
**Problem / user:** General users, bird watchers or casual players; makes bird watching feel like a collectible game.

**Features**
- Local bird map — Google Maps view with custom pins and frequency zones showing nearby birds, using eBird sightings *[shown_working]*
- Species classification — YOLOv8-based classifier fine-tuned on about 200 species identifies the photographed bird *[shown_working]*
- Bird segmentation — YOLOv8 segmentation model locates the bird in the frame *[shown_working]*
- Photo quality rating — Simple rules check rule-of-thirds placement, clipping at edges and visual quality *[shown_working]*
- BirdDex collection — New species added to a personal dex when photographed *[shown_working]*
- Photo gallery — Saved photos shown in a gallery component *[shown_working]*
- Wikipedia descriptions — Pulls species descriptions from Wikipedia *[claimed]*
- Nearby, health assessment, education — Nearby sightings, bird-health tool, ecosystem content *[planned]*

**Flow:** Open map of local birds → Pick a bird to photograph → Take photo → Model classifies and segments bird → See rating → Species added to BirdDex and photo to gallery

**Prompt:** Best Razzle Dazzle Hack: most unique project; two awards for projects that best entertain the judges.
**Fit (implied):** Playful photo-collecting game with custom ML models and polished UI is aimed at entertaining judges; page does not name the prize as a target.  *(targeted: Best Razzle Dazzle Hack - Bitcamp)*
**AI:** Classification and segmentation models fine-tuned from YOLOv8 checkpoints (PyTorch) with augmentation and overfitting controls; rule-based photo scoring.
**Architecture:** React mobile-first front end; Flask backend with SQLite for images and birds; ML models served by Flask; external Wikipedia, Google Maps and eBird APIs; demo exposed via ngrok.
**Novelty:** Trains its own bird classifier and segmenter and layers photo-composition scoring over it, rather than calling a hosted vision API.
**Scope:** medium · working: Live ngrok demo, 8 gallery items showing map, ratings, BirdDex and segmentation; no repo linked. · polish: Custom map pins, frequency zones, GIF intro; team reports smooth UI.
**Claims:** Classifies about 200 bird species | Retrained model over many hours
**Gaps:** No repo linked so no README; No accuracy numbers; Demo link not opened
Sources: https://devpost.com/software/bird-box-d2eguh, https://bitcamp2025.devpost.com/

---

### BurnoutBuddy
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Gemini API

**What it is:** A burnout-tracking dashboard for students and coders that fuses Fitbit sleep and steps, GitHub commits and webcam drowsiness detection into one burnout score, and responds with a 3D mascot, lo-fi music, hydration nudges and Gemini-written motivational quotes.
**Problem / user:** Busy students and developers who drift into burnout unnoticed and find clinical mental-health apps too serious.

**Features**
- Burnout score — Flask computes a weighted score from sleep, steps, commits and fatigue readings. *[claimed]*
- Webcam fatigue detection — OpenCV, MediaPipe and dlib track eyes in real time to estimate drowsiness. *[claimed]*
- Fitbit and GitHub data pipelines — Python scripts pull step, sleep and commit data into MongoDB Atlas time series. *[claimed]*
- Gemini motivational quotes — Backend asks Gemini for quotes and parses the response into JSON. *[claimed]*
- Interventions — Hydration reminders and randomized lo-fi Spotify embeds. *[claimed]*
- Journaling and task tracking — Entries stored in MongoDB Atlas alongside metrics. *[claimed]*
- Trend charts and 3D sidekick — Chart.js graphs plus a Spline 3D character with confetti. *[claimed]*

**Flow:** Connect Fitbit and GitHub data → Run webcam fatigue detection → View burnout score and trend graphs → Receive hydration, music and quote interventions → Log journal entries and tasks

**Prompt:** Use the Gemini API to build AI-powered apps (MLH Best Use of Gemini API).
**Fit (implied):** Gemini generates the motivational quotes and its responses are parsed in the Flask backend; MongoDB Atlas also stores the data. Gemini is a supporting feature rather than central.  *(targeted: [MLH] Best Use of Gemini API)*
**Sponsor tools:** Gemini API (Motivational quote generation, supporting); MongoDB Atlas (Fitbit/GitHub time series and journal storage, supporting)
**AI:** Gemini generates quotes; OpenCV/MediaPipe/dlib do classic computer-vision drowsiness detection; burnout score is a hand-weighted formula, not learned.
**Architecture:** React frontend with Chart.js and Spline calls a Flask API; Python scripts ingest Fitbit and GitHub data into MongoDB Atlas; a separate webcam module reports fatigue.
**Novelty:** Mixes wearable, code-activity and webcam signals into one wellbeing score with a playful 3D companion.
**Scope:** medium · working: Repo with backend, frontend and Fitbit automation; team says they connected the APIs; no demo link. · polish: Descriptive README; 3D Spline mascot and charts; no video or live site.
**Gaps:** no demo video; repo very large (3350 files) so README only
Sources: https://devpost.com/software/burnoutbuddy, evidence/bitcamp-bitcamp-2025-burnoutbuddy.json (README), https://bitcamp2025.devpost.com/

---

### Bye Bye Study Blues
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** MOST LIT HACK - Alumni Team

**What it is:** An Arduino hardware Pomodoro timer built from 48 LEDs on six branches that show study and break progress by turning rows off over time and flashing indicator lights at phase ends.
**Problem / user:** A student (the builder) who uses 50 minutes study and 5 minutes break and wants a cute visual timer to keep on task.

**Features**
- LED study countdown — A row of lights turns off every 10 minutes of study (10 seconds in demo) *[shown_working]*
- Study-end alert — A green light at the bottom flashes when study time ends *[shown_working]*
- Break countdown — A row turns off each minute of break (1 second in demo) *[shown_working]*
- Break-end alert and restart — Top row flashes, then the cycle restarts *[shown_working]*
- Six-branch LED circuit — Each branch has 8 LEDs in parallel with a resistor on its own digital pin *[shown_working]*

**Flow:** Power the Arduino → Study phase: rows go dark at intervals → Green light flashes at study end → Break phase: rows go dark faster → Top row flashes and cycle restarts

**Prompt:** MOST LIT HACK (alumni team): most LEDs used in a hack, either individually wired or on a strip; prize an LED matrix Arduino kit.
**Fit (implied):** Wires 48 LEDs across six independently controlled branches into a functional timer, directly addressing the LED count criterion.  *(targeted: MOST LIT HACK - Alumni Team)*
**AI:** none
**Architecture:** Arduino board with six digital output pins, each driving a branch of 8 parallel LEDs with one resistor; sketch written in Arduino IDE.
**Novelty:** Pure hardware, no software stack; the focus is wiring many LEDs and a simple state machine for phases.
**Scope:** tiny · working: Vimeo demo video and two circuit photos; no code repo listed. · polish: Breadboard prototype only; author says it is not soldered or polished.
**Claims:** All LED branches light separately and are programmable
**Gaps:** No repo or code; Video not watched; Google Docs 'Try it out' link not read
Sources: https://devpost.com/software/bye-bye-study-blues, https://bitcamp2025.devpost.com/

---

### CarbonQapture
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Hack Promoting Public Health - Bloomberg

**What it is:** A research pipeline and React dashboard that estimates CO2 binding energies of metal-organic frameworks with a simplified VQE quantum simulation in PennyLane and uses a PyTorch neural network to propose new candidate MOFs.
**Problem / user:** Carbon-capture and materials researchers facing a huge MOF design space; speeds screening of good CO2 adsorbers.

**Features**
- MOF data parsing — Reads CIF structure files from a real MOF dataset *[claimed]*
- VQE ground-state estimation — Builds a simplified 2-qubit Hamiltonian per structure and runs PennyLane VQE for energies *[claimed]*
- Neural network MOF generation — Supervised plus generative model proposes new MOF structures, tested again with VQE *[claimed]*
- Performance metrics — Predicts uptake, CO2/N2 selectivity and heat of adsorption *[claimed]*
- Results export and plots — Energies and properties saved as CSV and plotted *[claimed]*
- React web UI — Interactive graphs and sampled views of more than 8,000 generated points *[shown_working]*

**Flow:** Parse CIF data → Compute Hamiltonian and VQE energy → Train model on outputs → Generate new MOFs and re-test → Browse CSV results and charts in web UI

**Prompt:** Best Hack Promoting Public Health (Bloomberg): innovative technology solutions that improve health outcomes, accessibility, and awareness.
**Fit (implied):** Frames carbon capture as environmental and public-health relevant; the connection is not spelled out on the page.  *(targeted: Best Hack Promoting Public Health - Bloomberg)*
**AI:** PyTorch neural network with supervised and generative elements trained on MOF data and VQE outputs to propose structures; quantum VQE via PennyLane after abandoning Qiskit.
**Architecture:** Python pipeline (CIF parser, Hamiltonian builder, PennyLane VQE, PyTorch generator) writing CSV; React front end on Vercel visualizes results.
**Novelty:** Combines quantum-algorithm simulation with generative ML for materials discovery, unusual scope for a hackathon.
**Scope:** medium · working: Vercel demo, YouTube video and seven screenshots comparing existing and generated MOFs; no repo. · polish: Full React UI built from scratch; accuracy figure lacks method; physical validity needed fixes.
**Claims:** 98.3% accuracy in predicted ground state energy | Over 8,000 generated data points | Generated MOFs predicted to beat existing on CO2/N2 selectivity and uptake
**Gaps:** No repo linked; Dataset unnamed; Accuracy figure unsupported
Sources: https://devpost.com/software/carbonqapture, https://bitcamp2025.devpost.com/

---

### CookHub
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best Web Hack Using React - Peraton

**What it is:** A React Native/Expo recipe app where recipes are stored as CookLang markdown, can be forked and edited like GitHub repos, bookmarked, searched, and added to a shopping cart that estimates grocery cost.
**Problem / user:** People wanting cheap, easy recipes, a place to save and share them, and help budgeting groceries.

**Features**
- CookLang recipe rendering — Recipes kept as CookLang markdown files and formatted automatically for display *[claimed]*
- Recipe forking — Users copy an existing recipe into a personal variation, modeled on GitHub forks *[claimed]*
- In-app recipe editor — Text editor to adjust recipes (repo includes draft-js) *[claimed]*
- Metadata search with filters — Search recipes by metadata *[claimed]*
- Favorites — Bookmark recipes to a favorites page *[claimed]*
- Shopping cart and cost estimate — Grocery list items used to find local deals and compute total cost *[claimed]*
- Post and share recipes — Publish recipes for others *[claimed]*

**Flow:** Browse Home → Open a recipe → Fork or edit it → Add ingredients to shopping cart → See cost estimate and favorites

**Prompt:** Best Web Hack Using React (Peraton): uses React, considers end users' needs in interface design, and delivers an attractive, easy-to-navigate UI.
**Fit (implied):** Built the app with React Native and Expo with Figma-planned screens (Home, Recipe, Shopping, Favorites) aimed at budget-conscious cooks.  *(targeted: Best Web Hack Using React - Peraton)*
**AI:** none
**Architecture:** Expo React Native app with file-based routing; Firebase for backend; CookLang parser for recipes; cheerio and puppeteer listed (likely scraping) in dependencies.
**Novelty:** Applies git-style forking to recipes via the CookLang plain-text format, combined with cost estimation.
**Scope:** small · working: Four app screenshots and about 2.5k LOC repo; no demo link or video; README is unmodified Expo template. · polish: Figma layouts and styled screens; no setup notes beyond template; no tests.
**Gaps:** README gives no project info; feature list follows Devpost; Devpost says React in meta, React Native in body; How cheerio/puppeteer used unknown (no local deal data shown)
Sources: https://devpost.com/software/cookhub, evidence/bitcamp-bitcamp-2025-cookhub.json (README is Expo template), https://bitcamp2025.devpost.com/

---

### Cyber Sentinel
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Hardware Hack - Bitcamp

**What it is:** A Raspberry Pi plus browser-extension web-threat detector: while pages load the Pi samples system stats, scores anomalies against a baseline, runs static code and YARA checks, blocks requests to suspicious sites until approved, and shows a risk dashboard in the extension popup.
**Problem / user:** Less tech-savvy people (parents, grandparents, small offices) who want simple, low-cost, privacy-respecting online safety without subscriptions.

**Features**
- System profiling during page loads — Python script on the Pi records CPU, RAM, network use and computes z-scores versus a baseline to flag anomalies *[claimed]*
- Static code analysis — Semgrep scans JavaScript on visited pages *[claimed]*
- YARA malware rules — Rules applied to website code and downloaded files *[claimed]*
- Block until approved — Network requests to suspicious sites are held until the user allows them *[claimed]*
- Risk dashboard popup — Extension popup shows live risk status *[claimed]*
- Gemini risk assessment — Cloud Gemini produces final risk summary *[claimed]*
- Caching and controls — Cache scanned sites, pause blocking, on-demand deep scan *[planned]*

**Flow:** Install extension and run the Pi monitor → Load a website → Pi collects stats and runs Semgrep and YARA → Suspicious requests are blocked until user approves → Popup shows risk dashboard

**Prompt:** Best Hardware Hack: most creative, technical, and innovative use of circuitry, electronics, or microcontrollers.
**Fit (implied):** Uses a Raspberry Pi as a dedicated always-on monitor paired with a browser extension, making a personal hardware security appliance.  *(targeted: Best Hardware Hack - Bitcamp)*
**AI:** Gemini in the cloud produces the final risk assessment; detection otherwise uses statistics (z-scores), Semgrep and YARA rules.
**Architecture:** Chrome extension (React, Tailwind) talks to an Express/Mongoose backend; MongoDB acts as a task queue to the Raspberry Pi, which runs Python monitoring and Semgrep/YARA scripts and posts results back.
**Novelty:** Offloads detection to a home Pi appliance and uses MongoDB as a queue to bypass SSH script restrictions; combines system-resource anomaly signals with code scanning.
**Scope:** small · working: Repo with extension and backend (about 2.3k LOC) and four screenshots; no video or live demo. · polish: Detailed README and logo; no tests; still dependent on cloud middleware.
**Claims:** Finished product with everyday use for the team
**Gaps:** No demo video; Detection accuracy not measured; README mirrors Devpost text
Sources: https://devpost.com/software/cyber-sentinel, evidence/bitcamp-bitcamp-2025-cyber-sentinel.json (README), https://bitcamp2025.devpost.com/

---

### DMPN: Developer Monitoring & Productivity Nexus
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** People's Choice Hack - Bitcamp

**What it is:** A joke-flavored web app that samples a developer's webcam and screen every few seconds, has GPT-4o vision judge focus and posture, and awards 'aura' points shown live, with an admin timeline and Elo-ranked 'Aura Battles'.
**Problem / user:** Developers who think they are productive but get distracted; offers playful, gamified self-monitoring without micromanagement.

**Features**
- Webcam and screen capture — Dashboard captures images at a set interval (default 5 s) after permission grants *[shown_working]*
- GPT-4o aura scoring — Flask backend sends images with prompt templates to OpenAI vision and returns aura point changes *[shown_working]*
- Live score updates — WebSocket streams scores to the frontend *[shown_working]*
- Admin dashboard — Timeline of captures, aura changes, total score and level, productivity tips *[shown_working]*
- Demo mode toggle — 'Use API' switch swaps dummy data for live backend *[shown_working]*
- Aura Battles — Elo-based matchmaking and ranked battles against other developers *[claimed]*
- Nudges — Gentle prompts to refocus *[claimed]*
- IDE plugins and local mode — Browser extension, IDE plugins, local processing *[planned]*

**Flow:** Open dashboard and grant webcam and screen permission → Set capture interval → Start capturing → Backend scores images with GPT-4o → Aura updates live → Admin view shows timeline and tips

**Prompt:** People's Choice Hack: hackers vote on which projects they liked best.
**Fit (none):** Humor, gamified aura battles and a hosted demo aimed at a crowd; no stated targeting.  *(targeted: People's Choice Hack - Bitcamp)*
**AI:** OpenAI GPT-4o vision with custom prompt templates interprets webcam and screenshot images into aura points; Devpost also mentions a 'fine-tuned model' without details.
**Architecture:** Next.js/Tailwind frontend (landing, dashboard, admin) and Flask backend with WebSocket endpoints calling the OpenAI vision API.
**Novelty:** Parodic 'aura' metric for developer focus built from multimodal screen plus face analysis, with Elo battles.
**Scope:** small · working: Hosted site at myaura.tech, YouTube video, 6 screenshots; about 4.4k LOC and has tests. · polish: Clear README with setup and troubleshooting; demo/API toggle; Cursor config present.
**Claims:** Surprisingly accurate productivity assessments (no metrics)
**Gaps:** README does not mention Aura Battles or nudges; those are Devpost claims; Fine-tuned model claim unverified
Sources: https://devpost.com/software/dmpn-dev-aura-aio, evidence/bitcamp-bitcamp-2025-dmpn-developer-monitoring-productivity-nexus.json (README), https://bitcamp2025.devpost.com/

---

### EchoLens
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Social Good Hack - Bitcamp

**What it is:** A mobile web app that uses the phone camera to describe surroundings aloud, remembering earlier photos so it can point out what changed.
**Problem / user:** Not stated explicitly; narrating the camera feed suggests accessibility for people with low vision, matching the Social Good prize.

**Features**
- Spoken scene description — Phone camera frames sent to backend, OpenAI describes objects, result narrated *[claimed]*
- Change detection — Stores previous pictures and reports differences between captures *[claimed]*
- Automatic interval capture — Camera captures at timed intervals *[claimed]*
- Mobile browser delivery — React TypeScript front end served over HTTPS tunnels so phones allow video *[shown_working]*
- Per-user capture intervals and deployment — Adjust capture rate, full hosting *[planned]*

**Flow:** Open the app on a phone via tunnel URL → Camera starts capturing → App speaks a description of objects → Compare with earlier pictures to report changes

**Prompt:** Best Social Good Hack: solves a social problem or helps empower a marginalized community.
**Fit (implied):** Environment narration is an assistive tool, though the page never states the accessibility audience.  *(targeted: Best Social Good Hack - Bitcamp)*
**AI:** OpenAI model describes camera images; usage not detailed on the page.
**Architecture:** React (Vite) frontend on phone via Localtunnel, Flask backend exposed via ngrok HTTPS; backend calls OpenAI and keeps prior images.
**Novelty:** Change-aware narration (diffs against previous captures) rather than single-shot captioning.
**Scope:** tiny · working: YouTube demo and two screenshots; about 670 LOC; README is just tunnel instructions. · polish: Needs manual ngrok and localtunnel setup; not deployed.
**Claims:** It works and remembers previous pictures and differences
**Gaps:** No stated problem or audience; Which OpenAI model and how speech output works not stated
Sources: https://devpost.com/software/echolens-xf9a5q, evidence/bitcamp-bitcamp-2025-echolens.json (README), https://bitcamp2025.devpost.com/

---

### Forens.tech
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best Digital Forensics Related Hack - Cipher Tech Solutions

**What it is:** A local React front end over a Python/FastAPI backend that runs Volatility3 memory-forensics scans on a chosen memory dump, outputs structured JSON, and has a Gemini agent summarize results in a readable form.
**Problem / user:** Digital-forensics tools are hard for amateurs to use; aimed at law-enforcement and blue-team staff from beginner to expert.

**Features**
- Guided scan selection — User picks a memory dump file and chooses which analyses to run *[claimed]*
- Volatility3 automation — Python script runs Volatility3 plugins and returns consistent JSON *[claimed]*
- Analysis options — Running processes, file scan, OS info, network connections, executed commands *[claimed]*
- AI summarization — Gemini agent turns the JSON into summaries and deeper insight *[claimed]*
- Cleaned data display — UI shows objective data alongside tidied command output *[shown_working]*
- More tools and commands — Advanced Volatility commands, other forensic tools, better logging *[planned]*

**Flow:** Choose memory dump file → Select scan types → Backend runs Volatility3 and emits JSON → Gemini summarizes → Results shown in clean UI

**Prompt:** Best Digital Forensics Related Hack (Cipher Tech): digital forensics topics including data carving, reconstruction and recovery tools.
**Fit (implied):** Wraps a standard memory-forensics framework in a guided UI with AI summaries for non-experts.  *(targeted: Best Digital Forensics Related Hack - Cipher Tech Solutions)*
**AI:** Gemini-powered agent summarizes Volatility JSON output into insights; no prompt details.
**Architecture:** React and CSS UI (Figma-designed); FastAPI serves results of a Python script invoking Volatility3 on local memory dumps; JSON passed to Gemini.
**Novelty:** Strong UX process (FigJam task flow, wireframes, hi-fi prototypes) applied to a normally CLI-driven forensics tool.
**Scope:** small · working: Five screenshots incl. data display; repo exists but evidence shows only the Vite React template README and about 700 LOC of frontend; backend not visible in evidence. · polish: UX design artifacts shown; no demo or video.
**Claims:** Good-looking and good-performing app (no metrics)
**Gaps:** README has no project content; features follow Devpost; Backend code not seen in evidence
Sources: https://devpost.com/software/forens-tech, evidence/bitcamp-bitcamp-2025-forens-tech.json (README is Vite template), https://bitcamp2025.devpost.com/

---

### HealthBridge
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Social Good Hack - Bitcamp

**What it is:** An interactive Leaflet map and dashboard that layers social-determinants-of-health data (hospital access, food deserts, police presence, income) to reveal care gaps and overlapping vulnerabilities, with ZIP lookup for nearest providers.
**Problem / user:** Public health agencies, non-profits and policymakers who need to see where underserved communities lack care.

**Features**
- SDOH data map — Interactive web map showing collected health and social datasets *[shown_working]*
- Gap and overlap exploration — Highlights areas with overlapping vulnerabilities and resource gaps *[claimed]*
- ZIP code provider lookup — Enter ZIP to see closest health providers *[claimed]*
- Dashboard and Facility Impact views — Screens beyond the map summarizing data and facility effects *[shown_working]*
- Geolocation recommendations — Personalized resource suggestions by location *[claimed]*
- Live data, feedback, AI placement — Real-time updates, user reports, AI to suggest resource sites *[planned]*

**Flow:** Open home page → View map of health data → Look up ZIP for nearby providers → Open dashboard → Open Facility Impact view

**Prompt:** Best Social Good Hack: solves a social problem or helps empower a marginalized community.
**Fit (implied):** Targets health disparities in underserved communities by making care gaps visible; the page does not name the prize.  *(targeted: Best Social Good Hack - Bitcamp)*
**AI:** none
**Architecture:** Static HTML/CSS front end with Leaflet.js over OpenStreetMap; open state and federal datasets cleaned with Python/pandas and embedded in the app; no live database.
**Novelty:** Combines several non-clinical determinants (police presence, food access) into one equity map; prototype is data embedded, no backend.
**Scope:** small · working: Four screenshots (Home, Map, Dashboard, Facility Impact); no repo, demo or video. · polish: Multiple coherent views; challenges mention messy public data.
**Gaps:** No repo linked; Dataset names not given; No video or live demo
Sources: https://devpost.com/software/healthbridge-i8ao9x, https://bitcamp2025.devpost.com/

---

### Hiding in Plain Sight
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Cybersecurity Track Hack - Bitcamp

**What it is:** A Flask-backed web tool for image steganalysis: users upload images or a zip, and it analyzes them with statistical checks (chi-square, histograms) and anomaly detection to flag possible hidden data and extract it from LSB- or DCT-style embeddings.
**Problem / user:** Security and digital-forensics users who need to find data concealed inside images.

**Features**
- Hidden-data extraction — Recovers data embedded with least-significant-bit and DCT steganography *[claimed]*
- Statistical detection — Chi-square and histogram analysis plus anomaly detection to flag suspect images *[claimed]*
- Batch processing — Upload many images or a .zip at once *[shown_working]*
- Wide format support — Works across common image file types *[claimed]*
- Metadata view — README describes EXIF, dimensions and file size extraction shown in browser *[unclear]*
- Easter-egg UI — Interactive front page with hidden touches *[claimed]*

**Flow:** Start Flask server and open the page → Upload an image or zip of images → Backend analyzes the images → View results in browser

**Prompt:** Best Cybersecurity Track Hack: demonstrates cybersecurity principles and incorporates cybersecurity workshop content.
**Fit (implied):** Applies steganography and forensic analysis ideas to images; page does not say it used workshop content.  *(targeted: Best Cybersecurity Track Hack - Bitcamp)*
**AI:** none
**Architecture:** Python Flask backend using Pillow, NumPy and SciPy for image analysis; HTML/JS front end; zip upload handling.
**Novelty:** Combines detection and extraction in one browser tool with batch upload, using classical statistics rather than ML.
**Scope:** small · working: YouTube demo, two screenshots, test_images folder; about 2.6k LOC estimate. · polish: README appears to describe a generic metadata extractor, partly out of sync with Devpost.
**Gaps:** README describes a metadata extractor (EXIF, size, CLI); Devpost describes steganography extraction and statistics; feature list follows Devpost, README noted as unclear; Video not watched
Sources: https://devpost.com/software/hiding-in-plain-sight, evidence/bitcamp-bitcamp-2025-hiding-in-plain-sight.json (README), https://bitcamp2025.devpost.com/

---

### Image Steganalysis: Detect Hidden Text with Machine Learning
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** People's Choice Hack - Bitcamp

**What it is:** A Random Forest classifier over a 150-dimension hand-built feature vector (statistical, gradient and LSB features) that scores whether an image carries hidden steganographic content, for single images or directories.
**Problem / user:** Cybersecurity and digital-forensics practitioners who need to screen many images for concealed messages.

**Features**
- Hidden-content detection — Random Forest returns a probability that an image contains steganography *[claimed]*
- Feature extraction pipeline — 150-dimensional vector from pixel statistics, gradients and LSB variations *[claimed]*
- Single and batch analysis — Analyze one image or a whole directory *[claimed]*
- Trained on Alaska2 data — Dataset includes JMiPOD, JUNIWARD and UERD embeddings *[claimed]*
- Validation — Stratified cross-validation and tuned thresholds *[claimed]*

**Flow:** Provide an image or directory → Features extracted → Model scores each image → Output yes/no or probability

**Prompt:** People's Choice Hack: hackers vote for the projects they liked best.
**Fit (none):** No stated targeting; popularity prize. Page has 21 likes and a security-themed ML demo.  *(targeted: People's Choice Hack - Bitcamp)*
**AI:** Classical ML: Random Forest on engineered features, chosen after comparing other models; trained on the Alaska2 steganalysis dataset.
**Architecture:** Python scripts for feature extraction and training, Flask listed in tags; repo has 8 files (about 570 LOC) with a plain-text readme.
**Novelty:** Feature-engineered classical approach rather than a deep CNN, as is common for steganalysis; hackathon scope is a binary detector.
**Scope:** tiny · working: Repo has scripts; readme.txt repeats the marketing claim; no demo or video. · polish: Two images claimed; no setup steps or evaluation details.
**Claims:** 95% accuracy detecting hidden messages | Scans thousands of images in milliseconds
**Gaps:** Accuracy unsupported by split or false-positive data; Devpost tags mention deep learning but model is Random Forest; Flask UI not evidenced
Sources: https://devpost.com/software/image-steganalysis-detect-hidden-text-with-ai, evidence/bitcamp-bitcamp-2025-image-steganalysis-detect-hidden-text-with-machine-learning.json (readme.txt), https://bitcamp2025.devpost.com/

---

### Jesture
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Gemini API

**What it is:** A Python desktop drawing game controlled by hand gestures from a webcam: a closed fist draws, an open hand stops. In single-player the Gemini model guesses the drawing; in multiplayer it judges whose drawing is clearest.
**Problem / user:** Casual players of all ages, and those who struggle with keyboards or mice, who want a gesture-based interface.

**Features**
- Fist-to-draw gesture control — MediaPipe gesture recognizer reads hands via OpenCV; fist draws, open hand lifts. *[shown_working]*
- Drawing modes and tools — Free, line and circle modes, four colors and brush-size keys, rendered with Raylib. *[shown_working]*
- AI guessing in single-player — Pressing G sends the canvas to Google GenAI/Gemini to guess the subject. *[shown_working]*
- Multiplayer drawing duel — Timed rounds (30s default) where AI judges the least confusing drawing. *[claimed]*

**Flow:** Launch main.py with single or multi mode → Make a fist to draw in free, line or circle mode → Change color and brush with keys → Press G for the robot to guess → In multiplayer, press Space to start a battle

**Prompt:** Use the Gemini API to build AI-powered apps (MLH Best Use of Gemini API).
**Fit (explicit):** Gemini vision guesses and judges the drawings, making it the core game mechanic; README title cites the Gemini prize.  *(targeted: [MLH] Best Use of Gemini API)*
**Sponsor tools:** Gemini API (google-genai) (Guessing drawings and judging duels, core)
**AI:** MediaPipe gesture model for hand recognition; Gemini multimodal model interprets the drawn canvas to guess or compare.
**Architecture:** Single Python app: OpenCV webcam to MediaPipe gestures to Raylib canvas; canvas image sent to Google GenAI for guesses.
**Novelty:** Small gesture-drawing game with AI-as-judge multiplayer; accessible interface framing.
**Scope:** tiny · working: Short repo (9 files, ~840 LOC) with run commands and controls; no video. · polish: Playful README with controls list; no demo media.
**Gaps:** Devpost calls multiplayer a future item while README documents it; no video
Sources: https://devpost.com/software/jesture-sa1v02, evidence/bitcamp-bitcamp-2025-jesture.json (README), https://bitcamp2025.devpost.com/

---

### Koalafied
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [MLH] Best Use of .Tech

**What it is:** A MERN-stack job-application tracker that gamifies the search: users log applications, notes and statuses, earn collectible animated koalas for applying, interviewing and getting offers, and compete on a leaderboard.
**Problem / user:** Students applying to internships and jobs who track everything in dull spreadsheets and lose organization.

**Features**
- Account system — Sign-up and login with encrypted credentials and JWT sessions. *[claimed]*
- Application dashboard — Shows application statuses, notes and statistics like applications and interviews. *[shown_working]*
- Add and update applications — Create entries and move them through statuses; stored server-side in MongoDB. *[shown_working]*
- Interview and deadline notepad — Free-form notes for upcoming interviews and deadlines. *[claimed]*
- Koala collection — Koalas are awarded for applying, interviewing and receiving offers. *[shown_working]*
- Interactive animated koalas — Pure-React animated koalas roam the screen bottom and can be played with. *[shown_working]*
- Leaderboard — Ranks users by career progress. *[shown_working]*
- Gemini sprites and auto-tracking — Planned Gemini-made sprites/quests and email or extension tracking. *[planned]*

**Flow:** Sign up or log in → Open dashboard → Add an application → Earn a koala for milestones → Play with koalas → Check leaderboard

**Prompt:** Win a lifetime .Tech domain name to showcase and expand the project (MLH Best Use of .Tech).
**Fit (implied):** Deployed at koalafied.tech, using a .Tech domain as its public address. Prize is judged on domain use, which the page does not elaborate.  *(targeted: [MLH] Best Use of .Tech)*
**Sponsor tools:** .Tech domain (Hosts the demo at koalafied.tech, token)
**AI:** none
**Architecture:** React with Material UI frontend calls a Node/Express API backed by MongoDB for users, applications and koalas; JWT auth.
**Novelty:** Applies collectible-pet gamification to job tracking; koala animations built in plain React without a game engine.
**Scope:** small · working: Live site at koalafied.tech and six screenshots; no repo listed. · polish: Custom Photoshop graphics and animations; no video.
**Gaps:** no repo; no video; live site not opened
Sources: https://devpost.com/software/koalafied, https://bitcamp2025.devpost.com/

---

### Lighthouse
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Machine Learning Track Hack - Bitcamp

**What it is:** A solo project using a pretrained Google DDPM diffusion model to denoise very noisy photos by injecting the real image midway through the reverse process, and to create variations by re-adding noise ('renoising') and denoising again, with a GUI and a small API script.
**Problem / user:** Photographers with grainy low-light or high-ISO shots, or flawed photos they want to creatively rework.

**Features**
- Extreme denoising — Insert noisy photo partway into the diffusion timeline so the model rebuilds detail *[shown_working]*
- Creative renoising — Modify an image, add noise back, rerun diffusion to get realistic or artistic variants *[shown_working]*
- Custom noise scheduler — Mimics training noise process so partial-noise starts behave correctly *[claimed]*
- GUI — gui.py desktop interface demonstrating both modes *[shown_working]*
- Python model API — church.py and api_demo.py allow swapping other DDPM checkpoints *[shown_working]*
- Latent diffusion and LoRA — Stable Diffusion/VAE integration and LoRA fine-tuning *[planned]*

**Flow:** Run gui.py with CUDA GPU → Load a noisy or edited image → Choose denoise or creative mode → Model runs partial diffusion → View restored or varied image

**Prompt:** Best Machine Learning Track Hack: demonstrates machine learning principles and incorporates ML workshop content.
**Fit (implied):** Applies diffusion-model mechanics in a novel inversion of the sampling process; page does not mention workshop content.  *(targeted: Best Machine Learning Track Hack - Bitcamp)*
**AI:** Pretrained DDPM diffusion model (Google) in PyTorch, starting from a partially noised real image with a custom scheduler; no training from scratch.
**Architecture:** Python and PyTorch with CUDA; diffusion model auto-downloaded locally; GUI script plus church.py API with HTML docs.
**Novelty:** Repurposes unconditional diffusion models for denoising and editing by mid-process insertion, run on a single consumer GPU (RTX 2070).
**Scope:** small · working: YouTube demo, demo images, GUI and API scripts; about 460 LOC; requires CUDA GPU. · polish: Detailed README with setup, docs html, two screenshots; no tests or metrics.
**Claims:** Restores detail in unrecognizable images (no benchmarks)
**Gaps:** No quantitative quality metrics; Video not watched
Sources: https://devpost.com/software/lighthouse-p1cb0k, evidence/bitcamp-bitcamp-2025-lighthouse.json (README), https://bitcamp2025.devpost.com/

---

### MedSave
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best Use of GenAI in Business - Cloudforce/Microsoft

**What it is:** A web marketplace where pharmacies list surplus or near-expiry medications at a discount and nonprofits or clinics search for them by drug name and distance. Users sign in with Google and pick a pharmacy or nonprofit role.
**Problem / user:** Pharmacies, hospitals and nursing homes discard usable drugs while many people skip medication for cost; serves pharmacies with surplus stock and nonprofits or clinics serving underserved groups.

**Features**
- Google sign-in and role choice — Google OAuth login, then user picks Pharmacy or Nonprofit at onboarding. *[claimed]*
- Pharmacy listing form with NDC autofill — Pharmacy enters NDC code, name, location, price, expiry; backend fills generic name and manufacturer from the NDC Directory API. *[claimed]*
- Marketplace of listings — Listings saved in SQLite and shown in a marketplace view. *[claimed]*
- Nearest-pharmacy drug search — Nonprofit enters drug name and address; Mapbox address lookup ranks listings by proximity. *[claimed]*

**Flow:** Log in with Google → Choose Pharmacy or Nonprofit → Pharmacy submits NDC, price, expiry and location → Backend autofills drug metadata and stores listing → Nonprofit searches drug plus own address → Sees nearest matching pharmacy listings

**Prompt:** Cloudforce/Microsoft prize: best use of TerpAI to generate a business pitch for the final solution, including a shark-tank style investor pitch and a LinkedIn post tagging the sponsors.
**Fit (none):** Devpost lists a terpai tag but describes no AI, pitch or TerpAI use in the body; the GenAI link to the prize is not shown.  *(targeted: Best Use of GenAI in Business - Cloudforce/Microsoft)*
**Sponsor tools:** TerpAI (Listed as a built-with tag only; role not explained, unclear)
**AI:** none
**Architecture:** React/Tailwind frontend calls a Flask REST backend with SQLite storage; external calls to NDC Directory and openFDA for drug data and Mapbox for addresses; Google OAuth for login.
**Novelty:** Two-sided surplus-medication marketplace with NDC-code autofill and distance ranking; otherwise a conventional CRUD marketplace by a first-time team.
**Scope:** small · working: Deployed full-stack app claimed; repo has about 2.3k LOC and frontend tests; no demo video. · polish: Five gallery screenshots; Tailwind styling; no live link recorded.
**Claims:** Cites a study of over $800M usable hospital drugs wasted yearly (external figure) | Cites 1 in 3 Americans skipping meds due to cost (external figure)
**Gaps:** No explanation of GenAI or TerpAI use; No demo video
Sources: https://devpost.com/software/medsave, evidence/bitcamp-bitcamp-2025-medsave.json, https://bitcamp2025.devpost.com/

---

### NeoVisr
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Moonshot Hack - Bitcamp

**What it is:** A React Native (Expo) chat app backed by a Google ADK agent running Gemini 2.0 Flash that advises UMD computer science students. It answers course and prerequisite questions from advising PDFs and can fetch a degree audit and prepare advisor emails.
**Problem / user:** UMD CS students struggle to find clear degree-requirement and prerequisite info and wait weeks for advisor meetings.

**Features**
- Advisor chat agent — ADK LlmAgent cs_advisor answers course questions from indexed advising PDFs or offers an advisor email template. *[shown_working]*
- PDF extraction and search — pdfplumber text extraction over advising PDFs sorted by course level, searched via tools. *[shown_working]*
- Automated degree audit download — Playwright logs into uAchieve through CAS and Duo 2FA and downloads the audit. *[shown_working]*
- Appointment scheduling via TerpEngage — Playwright tool navigates TerpEngage to book advisor appointments. *[claimed]*
- Prefilled advisor email link — Tool builds a Gmail compose link with a templated message. *[claimed]*
- Profile, dark mode and sidebar — Profile screen for name, major, theme; AsyncStorage caches profiles and chat sessions. *[shown_working]*

**Flow:** Open mobile app and set profile → Ask a question such as a course's prerequisites → Agent searches PDFs or triggers the degree audit tool → Receives answer or advisor email template → Optionally schedule an appointment

**Prompt:** Best Moonshot Hack: the most creative, innovative and well-developed hack that shoots for the moon.
**Fit (implied):** Ambitious multi-tool agent that automates logging into university systems with 2FA plus PDF retrieval in a mobile app; README says it won the Moonshot award.  *(targeted: Best Moonshot Hack - Bitcamp)*
**Sponsor tools:** Google ADK / Gemini 2.0 Flash (Agent framework and model for the advisor, core)
**AI:** Google ADK LlmAgent on Gemini 2.0 Flash with custom tools for PDF search, degree audit, scheduling and email. README additionally claims a custom NLP model and multi-agent orchestration; Devpost describes a single agent.
**Architecture:** Expo React Native chat client sends queries through ADK API to a Python agent; tools use pdfplumber over local PDFs and Playwright against uAchieve and TerpEngage.
**Novelty:** Drives real university portals (CAS, Duo 2FA) headlessly from an LLM agent rather than only answering from documents.
**Scope:** medium · working: Live demo reportedly showed a degree audit download and course Q&A; repo has agent, tools and mobile frontend with tests. · polish: Light/dark theming, sidebar, profile screen; credentials handled in plaintext per next-steps.
**Claims:** Devpost: Playwright completed uAchieve audit including Duo 2FA | README: custom NLP model trained on hundreds of pages of advising documents
**Gaps:** README and Devpost differ on agent structure (multi-agent plus custom NLP vs single ADK agent); feature list follows Devpost; No video
Sources: https://devpost.com/software/adviseai, evidence/bitcamp-bitcamp-2025-neovisr.json, https://bitcamp2025.devpost.com/

---

### NeuroScan.AI
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best First Time Hack - Bitcamp

**What it is:** A Streamlit web app that classifies brain tumor type from an uploaded MRI using a fine-tuned MobileNetV2, then asks Gemini for treatment recommendations and exports a PDF report with a doctor-approval section.
**Problem / user:** Early brain tumor detection affects outcomes but advanced diagnostics are not widely accessible; aimed at medical professionals who review and approve outputs.

**Features**
- MRI tumor classification — MobileNetV2 fine-tuned on a brain MRI dataset gives a tumor class with confidence score; Devpost claims 92% accuracy. *[shown_working]*
- Patient information intake — App collects patient details that feed into the analysis and report. *[claimed]*
- Gemini treatment recommendations — Classification result and patient data are sent to Google Gemini for personalized recommendations. *[claimed]*
- Downloadable PDF report — FPDF2 builds a report with patient info, scan analysis, classification, recommendations and space for doctor notes. *[claimed]*
- Doctor review and approval section — Report includes a validation block for physician sign-off. *[claimed]*

**Flow:** Upload MRI scan → Enter patient information → View classification result with confidence → Read Gemini recommendations → Download PDF report → Doctor reviews and approves

**Prompt:** Best First Time Hack: best hack by a first-time hacker showing the most individual growth; at least half the team must be first-time Bitcamp hackers.
**Fit (implied):** Complete ML plus GenAI pipeline with a hosted demo; README labels it a first-place winner. Devpost does not explicitly discuss first-time status.  *(targeted: Best First Time Hack - Bitcamp)*
**Sponsor tools:** Google Gemini (Generating treatment recommendations, supporting)
**AI:** MobileNetV2 transfer learning in TensorFlow for image classification, plus Gemini text generation for recommendations. Repo script name suggests roughly 70% accuracy versus the 92% on Devpost.
**Architecture:** Streamlit app loads a saved Keras model, preprocesses MRI with OpenCV/Pillow, classifies, calls Gemini, and renders a PDF via FPDF2; deployed on Render with Docker.
**Novelty:** Combines a small CNN classifier with an LLM-written clinical report and approval step; the model/dataset approach is common for hackathons.
**Scope:** small · working: Hosted Render demo link and Dockerfile; repo contains the Brain-Tumor-Classification dataset and training script. · polish: PDF report generation and README with install steps; no tests.
**Claims:** Devpost: 92% tumor classification accuracy (no evaluation method given) | Training script filename references 70% accuracy, inconsistent with 92%
**Gaps:** Accuracy figure conflicts between Devpost (92%) and repo script name (70%); Dataset not named on Devpost; No video
Sources: https://devpost.com/software/neuroscan-ai, evidence/bitcamp-bitcamp-2025-neuroscan-ai.json, https://bitcamp2025.devpost.com/

---

### QAOA for the kidney exchange problem
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Advanced Quantum Track Hack - Bitcamp

**What it is:** A Python research-style project that formulates the kidney exchange problem as a binary integer program, converts it to an Ising model and runs QAOA in simulation, comparing against classical CPLEX/CBC solutions.
**Problem / user:** Incompatible kidney donor-recipient pairs need cycles of exchange; the team explored whether quantum optimization could handle this textbook problem.

**Features**
- BIP to Ising conversion — OpenQAOA converts the exchange integer program into an Ising Hamiltonian, with unbalanced penalization to cut variable count. *[shown_working]*
- QAOA simulation — PennyLane simulates the QAOA circuit on classical hardware, limited to datasets of about 30 pairs or fewer. *[shown_working]*
- Classical baselines — CPLEX bindings, PuLP and CBC compute classical solutions; PuLP also filters quantum output. *[shown_working]*
- Dataset tooling — Modernized dataset parser, custom pruner and custom problem generator produce instances. *[shown_working]*
- Result charts — Matplotlib charts of results. *[claimed]*
- Success probabilities and altruistic donors — Listed as possible future extensions. *[planned]*

**Flow:** Unzip datasets with kepio.unzip_data() → Run main.py → Instances are parsed, pruned and converted → QAOA is simulated and output filtered → Compare with classical solution and charts

**Prompt:** Best Advanced Quantum Track Hack: design a hybrid classical-quantum algorithm that uses quantum techniques to solve the track's challenges.
**Fit (implied):** Hybrid pipeline: classical preprocessing and filtering around a simulated QAOA step, applied to a real optimization problem; it also compares with classical solvers.  *(targeted: Best Advanced Quantum Track Hack - Bitcamp)*
**AI:** none
**Architecture:** Python scripts: parser, pruner and generator build instances, OpenQAOA makes an Ising model, PennyLane simulates QAOA, PuLP/CPLEX/CBC produce and filter classical solutions, Matplotlib plots.
**Novelty:** Applies QAOA to kidney-exchange optimization, a niche application the team says had little prior quantum interest; claims speedup without measurements.
**Scope:** tiny · working: Nine files, about 300 LOC; runnable via main.py per README; scale limited by simulation. · polish: Slide deck linked; no UI, tests or charts shown on page.
**Claims:** Says it achieved exponential speedup in many realistic cases (no figures) | Limited to datasets of 30 or fewer donor-recipient pairs
**Gaps:** Speedup claim unverified; Datasets unnamed; Slides not read
Sources: https://devpost.com/software/kidney-donation-chain-integer-programming-with-qaoa, evidence/bitcamp-bitcamp-2025-qaoa-for-the-kidney-exchange-problem.json, https://bitcamp2025.devpost.com/

---

### Quanta
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Advanced Quantum Track Hack - Bitcamp

**What it is:** Quanta is a web tool that predicts how a thin material sheet or an uploaded .obj model deforms under force, using a stiffness-matrix FEA formulation solved either classically or with a quantum HHL linear solver, then rendering the displaced 3D mesh.
**Problem / user:** Engineers and designers evaluating material behavior under stress, especially nanomaterials that Fusion360 cannot model and slow renders there.

**Features**
- Material property lookup — Queries the Materials Project API for the chosen material's properties. *[claimed]*
- Mesh and stiffness matrix FEA — Builds a flat mesh grid with stiffness matrix K and solves Ku=f for displacements. *[shown_working]*
- Quantum HHL solver — Classiq SDK implements the HHL algorithm for sparse linear systems as a proof of concept; limited to small matrices. *[shown_working]*
- Classical solver — Parallel classical implementation for larger meshes. *[shown_working]*
- .obj import — Applies the material to user-supplied geometry made in Blender. *[claimed]*
- 3D deformation rendering — Three.js renders the model from displacement results. *[shown_working]*
- Easter eggs — Dinosaur-themed T-rex game and casino page. *[claimed]*

**Flow:** Open the hosted site → Pick a material → Optionally supply an .obj mesh → Choose classical or quantum solve → View the rendered displaced 3D model

**Prompt:** Best Advanced Quantum Track Hack: design a hybrid classical-quantum algorithm that uses quantum techniques to solve the track's challenges.
**Fit (implied):** Uses HHL via Classiq inside a hybrid pipeline where classical code builds the mesh and renders results; team calls the quantum path a proof of concept.  *(targeted: Best Advanced Quantum Track Hack - Bitcamp)*
**Sponsor tools:** Classiq Python SDK (Implementing the HHL quantum linear solver, core)
**AI:** none
**Architecture:** React/TypeScript/Three.js frontend with Flask/NumPy backend; backend fetches material data, builds stiffness matrix, solves via classical NumPy or Classiq HHL, returns displacements for rendering.
**Novelty:** Pairs quantum linear-system solving with a finite-element mesh and an interactive 3D viewer rather than an abstract benchmark.
**Scope:** medium · working: Hosted at quantano.tech; repo with Flask backend and React GUI, about 2k LOC, Docker file. · polish: Three.js visuals and playful easter eggs; no tests or benchmarks.
**Claims:** Quantum path limited to small matrices; positioned as proof of concept
**Gaps:** Video referenced but no link; Unclear if quantum ran on simulator or hardware
Sources: https://devpost.com/software/quanta-obvusa, evidence/bitcamp-bitcamp-2025-quanta.json, https://bitcamp2025.devpost.com/

---

### Quaran.Tech
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [MLH] Best AI Application Built with Cloudflare

**What it is:** An HTML5 browser game where the player plays a public health specialist such as a contact tracer making fast, high-pressure decisions in compressed days. Stored storylines live in MongoDB, and Gemini can generate new scenarios on demand.
**Problem / user:** The general public (and gamers wanting fresh stories) who do not understand what public health workers do during outbreaks.

**Features**
- Public health role-play game — Cross-platform HTML5 game with days compressed to seconds and rapid decisions. *[shown_working]*
- Gemini-generated scenarios — Gemini creates new alternate storylines beyond the handwritten ones. *[claimed]*
- Stored scenario library — Existing storylines kept in MongoDB and served by Cloudflare Workers. *[claimed]*
- Voice chat with AI characters — Talk to doctors, patients, officials. *[planned]*

**Flow:** Open quaran.tech intro page → Start gameplay as a public health specialist → Make quick decisions as scenarios play out → Receive stored or Gemini-generated storylines

**Prompt:** Build an AI application using Cloudflare services (MLH Best AI Application Built with Cloudflare).
**Fit (implied):** Frontend hosted on Cloudflare Pages and backend on Cloudflare Workers, with Gemini generating story content.  *(targeted: [MLH] Best AI Application Built with Cloudflare)*
**Sponsor tools:** Cloudflare Pages and Workers (Hosting the game and backend API, core); Gemini API (Generating new scenarios, core); MongoDB (Storing scenarios, supporting); .Tech domain (quaran.tech address, token)
**AI:** Gemini prompts produce new storylines to extend hand-written ones; results parsed into the game format.
**Architecture:** jQuery/HTML5 frontend on Cloudflare Pages; Cloudflare Workers backend fetches scenarios from MongoDB and calls Gemini.
**Novelty:** Educational pandemic-role game built without a game engine, with LLM-extended storylines.
**Scope:** small · working: Live game at quaran.tech with intro and gameplay screenshots; no repo. · polish: Hosted on custom domain; no video; gameplay depth unclear.
**Gaps:** no repo; no video; live site not opened
Sources: https://devpost.com/software/quarantech, https://bitcamp2025.devpost.com/

---

### Recipez
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Moonshot Hack - Bitcamp

**What it is:** A React Native (Expo) cooking app that reads grocery receipts with Google Cloud Vision, turns the items into a fridge inventory, and uses Gemini to suggest recipes from what is on hand.
**Problem / user:** New cooks and college students struggle to decide what to cook from limited ingredients and what is missing at the store.

**Features**
- Receipt scanning — Phone camera image goes to Google Cloud Vision OCR; Gemini and prompt engineering normalize item names, brands, typos and units. *[claimed]*
- Fridge inventory — Detected food items are structured and stored in a Fridge screen. *[claimed]*
- Recipe generation — Gemini generates recipes from the available ingredients on the home screen. *[claimed]*
- Saved recipes and inventory update — Users save recipes; cooking one removes its ingredients from the fridge. *[claimed]*
- Expiration reminders — Shelf-life based reminders listed as future work. *[planned]*
- Accounts and cross-device sync — User accounts to sync fridge, planned. *[planned]*

**Flow:** Scan a grocery receipt → Items are added to Fridge → Generate recipes on Homescreen → Save a recipe → Mark it made to deduct ingredients

**Prompt:** Best Moonshot Hack: the most creative, innovative and well-developed hack that shoots for the moon.
**Fit (none):** Page does not say how it targets the prize; it chains OCR and an LLM into a receipt-to-recipe flow.  *(targeted: Best Moonshot Hack - Bitcamp)*
**Sponsor tools:** Google Cloud Vision API (Receipt OCR, core); Google Gemini (Cleaning parsed items and generating recipes, core)
**AI:** Cloud Vision OCR on receipts, then Gemini with prompt engineering to normalize messy item text and generate recipes.
**Architecture:** Expo React Native TypeScript app with Firebase backend; image to Vision API, text to Gemini, structured results to the app.
**Novelty:** Receipt-driven pantry tracking that closes the loop by deducting ingredients when a recipe is cooked.
**Scope:** small · working: Four screenshots show four screens; no repo, demo or video. · polish: Four-screen mobile UI described; no live link.
**Gaps:** No GitHub repo linked on page; No video or demo link
Sources: https://devpost.com/software/recipez-d2zosy, https://bitcamp2025.devpost.com/

---

### Riffs
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best App Dev Track Hack - Bitcamp

**What it is:** A browser app where a guitarist hums a melody, pitchy detects the notes, and the app maps them to guitar string and fret positions in an editable piano-roll style editor. No backend; deployed on Vercel.
**Problem / user:** Learning guitar feels intimidating and existing tools use robotic MIDI, confusing tabs or studio setups; aimed at guitarists and creators.

**Features**
- Hum-to-notes recording — Browser microphone input is analyzed with the pitchy library to detect pitches and turn them into notes. *[shown_working]*
- Fretboard mapping — Detected notes are mapped automatically to realistic guitar string and fret positions with a fretboard visualizer. *[shown_working]*
- Piano-roll riff editor — Custom editor lets users click, drag and delete notes. *[shown_working]*
- Play the riff view — Playback view in a Guitar Hero-style jam experience; Tone.js is a dependency. *[claimed]*
- Guitar sample playback — Real guitar samples made in FL Studio to replace default MIDI; Devpost says integration was still in progress. *[planned]*
- Export, layers and cloud save — MIDI/tab/Guitar Pro export, multiple tracks, cloud saving and AI chord suggestions. *[planned]*

**Flow:** Open the landing page → Record a hummed melody → App generates a riff mapped to guitar positions → Edit notes in the piano roll → Play the riff

**Prompt:** Best App Dev Track Hack: best hack demonstrating app development principles and incorporating App Dev workshop content.
**Fit (implied):** Polished multi-page Next.js/TypeScript app with state across pages and deployment; page does not mention the workshop or track.  *(targeted: Best App Dev Track Hack - Bitcamp)*
**AI:** none
**Architecture:** Client-only Next.js/React/TypeScript app: Web Audio mic input, pitchy pitch detection, note-to-fret mapping, custom piano-roll and fretboard components, Tone.js for sound; hosted on Vercel.
**Novelty:** Voice-to-guitar-tab pipeline entirely in the browser with a self-built note editor in under 36 hours.
**Scope:** small · working: Live Vercel demo link and about 5k LOC repo with landing, record, edit and play views. · polish: Custom visuals, framer-motion animations, themed UI; README is the default Next.js template; no tests.
**Claims:** Built a custom visual note editor from scratch in under 36 hours | Runs entirely in browser with no plugins
**Gaps:** README is the unedited Next.js template; Playback status uncertain; No video
Sources: https://devpost.com/software/riffs, evidence/bitcamp-bitcamp-2025-riffs.json, https://bitcamp2025.devpost.com/

---

### Rizz Lab
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best UI/UX Hack - Bitcamp

**What it is:** An AI dating-coach chat app built from the Vercel Next.js plus FastAPI streaming template. The backend wraps OpenAI for streamed chat, tool calls that rate a flirting line, simulate a date or create a scenario image, plus speech transcription and text-to-speech.
**Problem / user:** Helps people practice and improve flirting lines; Devpost only says people need help razzing and gives the tagline of AI that helps you rizz.

**Features**
- Streaming chat coach — FastAPI streams OpenAI chat completions to a Next.js useChat interface. *[shown_working]*
- Rizz evaluation tool — Model-callable evaluate_rizz function gives feedback on a user's line. *[claimed]*
- Date simulation — simulate_date tool plays out a date from an opening line. *[claimed]*
- Scenario image generation — generate_rizz_image tool creates an image of a scenario. *[claimed]*
- Voice input and output — Audio upload is transcribed with Whisper; a text-to-speech endpoint offers voices. *[claimed]*

**Flow:** Open chat UI → Type or speak an opener → Model streams coaching feedback or calls a tool → Optionally view a generated image or hear speech

**Prompt:** Best UI/UX Hack: judged on innovation, aesthetics, service to the project, and the process.
**Fit (none):** Devpost has no description of design; repo uses Tailwind, framer-motion and Radix components. Connection to the UI/UX criteria is inferred only.  *(targeted: Best UI/UX Hack - Bitcamp)*
**AI:** OpenAI gpt-3.5-turbo with function calling for rizz evaluation, date simulation and image prompts; Whisper-1 for transcription; OpenAI text-to-speech.
**Architecture:** Next.js frontend with Vercel AI SDK useChat talks to FastAPI endpoints (/api/chat, upload-audio, text-to-speech) that stream OpenAI responses and run Python tools.
**Novelty:** Playful dating-practice framing layered on an off-the-shelf AI SDK streaming template.
**Scope:** small · working: Repo has about 8.6k LOC with multiple components and API routes; no demo link or video. · polish: Animated component library; README is the unmodified template; Devpost mostly empty.
**Gaps:** Devpost sections mostly empty; README is a template; features come from backend source; Frontend not inspected
Sources: https://devpost.com/software/rizz-lab, evidence/bitcamp-bitcamp-2025-rizz-lab.json, https://raw.githubusercontent.com/vasantsaladi/umd_hack/HEAD/api/index.py

---

### Roameo
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence low*
**Prizes:** Best Use of GenAI in Business - Cloudforce/Microsoft

**What it is:** A conversational travel-planning chatbot with a React/Tailwind chat UI, claiming to combine OpenAI and Gemini, browser automation over Google Flights and Hotels, Google Maps and ElevenLabs speech to build itineraries by chatting.
**Problem / user:** Travelers lose hours comparing flights, stays and activities across sites; the site frames planning as chatting with a friend.

**Features**
- Conversational trip planning — Chatbot interprets requests and assembles an itinerary in real time. *[claimed]*
- Flight and hotel search — AI-driven browser automation (Browser Use) queries Google Flights and Hotels. *[claimed]*
- Local recommendations and maps — Google Maps tiles and APIs for activities and locations. *[claimed]*
- Automation backend — FastAPI (or Flask per tags) and n8n workflows connect data sources; MongoDB listed. *[claimed]*
- Speech synthesis — ElevenLabs voice output, apparently removed with plan to reintroduce. *[planned]*
- Profiles, collaborative trips, extra services — Personalization, shared planning, insurance, SIM and currency exchange. *[planned]*

**Flow:** Visit roameo.tech landing page → Open the chatbot → Describe the trip → Bot returns flights, hotels, map and itinerary

**Prompt:** Cloudforce/Microsoft prize: best use of TerpAI to generate a business pitch for the final solution, including a shark-tank style pitch and a LinkedIn post tagging the sponsors.
**Fit (implied):** Uses generative AI chat for a travel-service use case; no TerpAI or pitch material is mentioned on the page.  *(targeted: Best Use of GenAI in Business - Cloudforce/Microsoft)*
**Sponsor tools:** ElevenLabs (Speech synthesis of replies (later removed), supporting)
**AI:** OpenAI ChatGPT and Gemini for conversation, Browser Use agent for web interactions with travel sites; ElevenLabs TTS.
**Architecture:** React/Tailwind chat front end; Python backend plus n8n workflows call LLMs, browser automation and Google travel and maps data; MongoDB storage.
**Novelty:** Uses browser automation of Google Flights and Hotels rather than a booking API.
**Scope:** small · working: roameo.tech demo link; repo is a small React app (~1.2k LOC) with an openai dependency, Bolt-generated, no backend visible. · polish: Landing, About, Features and ChatBot pages shown; typewriter and Cesium dependencies; no tests.
**Claims:** Real-time personalized itinerary creation through conversation | Integration of diverse travel data and automation tools
**Gaps:** Repo has no README and no visible backend; Devpost backend and Browser Use claims unverified; Devpost lists both FastAPI and Flask; No video
Sources: https://devpost.com/software/roameo-dtrzau, evidence/bitcamp-bitcamp-2025-roameo.json, https://bitcamp2025.devpost.com/

---

### Schrodinger's Catch: TROUT of This World!
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Hack That Made You Smile - Alumni Team

**What it is:** A Godot VR fishing game for Meta Quest 2 where the species caught comes from a quantum random number: a Flask service runs a 5-qubit Qiskit circuit and returns 0 to 31 to pick one of 32 fish.
**Problem / user:** No problem stated; a relaxing, whimsical VR game for casual players that doubles as a quantum-randomness demo.

**Features**
- Island fishing in VR — Player explores an island and casts a line using Godot XR Tools on Meta Quest 2. *[claimed]*
- Quantum random bites — Hadamard gates place 5 qubits in superposition; measurement gives a number from 0 to 31. *[claimed]*
- Flask quantum API — Godot calls a Python Flask HTTP endpoint that runs the Qiskit circuit. *[claimed]*
- 32 fish types — Returned number maps to which fish spawns after the cast. *[claimed]*

**Flow:** Start the game on a Quest 2 → Explore the island → Cast the line and wait → Godot requests a number from the Flask API → The matching fish spawns

**Prompt:** Hack That Made You Smile (alumni): funny, silly, creative, whimsical, absurd, a parody.
**Fit (implied):** A whimsical fishing game with a quantum pun title using quantum randomness to choose fish; page does not state the prize intent.  *(targeted: Hack That Made You Smile - Alumni Team)*
**AI:** none
**Architecture:** Godot XR project on Quest 2 sends HTTP requests to a Flask app that runs a Qiskit/Aer 5-qubit circuit and returns an integer for fish selection.
**Novelty:** Quantum random number generation used as the game's loot mechanic in VR.
**Scope:** small · working: Godot project of several hundred files plus a small Qiskit Flask app (gunicorn); no video or build. · polish: Four screenshots; README is a title only; sound effects planned.
**Claims:** Quantum circuit yields truly random numbers
**Gaps:** Devpost meta says game is in space while story says island; README is a title only; No video
Sources: https://devpost.com/software/schrodingers-catch-trout-of-this-world, evidence/bitcamp-bitcamp-2025-schrodinger-s-catch-trout-of-this-world.json, https://bitcamp2025.devpost.com/

---

### SkinForReal
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Use of GenAI in Business - Cloudforce/Microsoft

**What it is:** A Flutter skincare-tracking app concept: users take a daily post-wash selfie that Azure Face API analyzes for skin conditions, log products and mood, and receive TerpAI-generated daily reports, alerts and a Skin School feed.
**Problem / user:** People with breakouts, dryness or irritation waste money on routines that do not work; existing trackers lack real-time, personalized, data-driven insight. Aimed at individuals of any skincare stage, including Gen Z.

**Features**
- Daily selfie scan — Post-wash selfie analyzed with Azure Face API for breakouts, redness, dryness, inflammation and trauma; also skin type and Fitzpatrick tone. *[claimed]*
- Product and mood log — Tracks products used, skin feel and lifestyle data such as weather, sleep and stress. *[claimed]*
- Real-time alerts — Flags products causing irritation or barrier damage and early trauma signs. *[claimed]*
- Personalized daily report — TerpAI generates summaries matched to skin type and tone. *[claimed]*
- Skin School feed — GenAI scrollable feed explaining why skin reacts and what to do next. *[claimed]*
- Pattern recognition — Learns routine and skin behavior over time to evolve recommendations. *[claimed]*
- Dermatologist export, multilingual, Pro tier — Ingredient database, Spanish and Mandarin, secure report export, trends dashboard, community, premium tier. *[planned]*

**Flow:** Take a daily post-wash selfie → App detects conditions, skin type and tone → Log products and mood → Receive personalized daily report and alerts → Browse Skin School content → Recommendations adapt over time

**Prompt:** Cloudforce/Microsoft prize: best use of TerpAI to generate a business pitch for the final solution, including a shark-tank style investor pitch and a LinkedIn post tagging the sponsors.
**Fit (explicit):** Lists TerpAI, Azure and Cloudforce as built-with tools; TerpAI generates daily summaries, alerts and Skin School content. Pitch deliverable and LinkedIn post not shown on page.  *(targeted: Best Use of GenAI in Business - Cloudforce/Microsoft)*
**Sponsor tools:** TerpAI (Daily skin summaries, alerts and Skin School content, core); Microsoft Azure Face API (Selfie-based skin condition detection, core)
**AI:** Azure Face API for image analysis of selfies and TerpAI generative text for reports, alerts and educational feed; no custom model described.
**Architecture:** Flutter mobile app sends selfies to Azure, combines results with logged products and lifestyle inputs, and uses TerpAI to produce reports and content.
**Novelty:** Combines selfie analysis, product logging and a GenAI education feed in one skincare companion with safety-alert framing.
**Scope:** small · working: Devpost claims a working prototype in under 36 hours; demo link is a Canva design, no repo or video. · polish: Canva mockup and detailed roadmap; no running build verified.
**Claims:** Full working prototype in under 36 hours | Strong positive feedback in early testing (no numbers)
**Gaps:** No GitHub repo linked; Demo link is a Canva design, not an app; No video
Sources: https://devpost.com/software/skinforreal, https://bitcamp2025.devpost.com/

---

### Sustainable Earth (Eco-Finance)
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Sustainability Hack - Bitcamp

**What it is:** A web app that scores a user's spending for sustainability from uploaded or Plaid-linked transactions, suggests greener alternatives with Gemini, pays eco-score based cashback rewards, and lets users put rewards into green investments.
**Problem / user:** Bank customers who want to spend more sustainably and invest in eco-friendly companies; inspired by the spare-change investing app Acorn.

**Features**
- Transaction ingestion — Users upload a CSV or connect a bank through Plaid (mock accounts) to load transactions. *[shown_working]*
- Eco-score and dashboard — Calculates sustainability scores, category breakdowns and recommended steps to cut footprint. *[shown_working]*
- Eco product search — Gemini-powered search returns the most sustainable option with an eco-score. *[shown_working]*
- Cashback rewards — Rewards with multiplier based on eco-score, spendable at partner companies. *[claimed]*
- Green investing — Risk questionnaire, green stock options, live prices via yfinance and visualization of active investments. *[claimed]*

**Flow:** Sign up or log in → Upload CSV or connect bank via Plaid → Review sustainability overview and eco-score → Search for greener products → Redeem rewards or invest them after the risk questionnaire

**Prompt:** Best Sustainability Hack: does the hack strive to help the environment or solve a sustainability-related issue.
**Fit (implied):** Ties spending behavior to an eco-score, greener product alternatives and green investments; page states the environmental motivation.  *(targeted: Best Sustainability Hack - Bitcamp)*
**AI:** Google Gemini for eco-product and green-stock search and to parse web-scraped data; README mentions Google Generative AI integration.
**Architecture:** React/TypeScript frontend with Express/Node server (README: Passport auth, in-memory storage); Devpost also lists Flask, PostgreSQL, Plaid, yfinance and Replit hosting.
**Novelty:** Joins spending analysis, rewards and investing in one loop; cashback-to-green-stocks pipeline is the distinctive part.
**Scope:** medium · working: Replit demo link, about 15k LOC repo with client, server, ml and tests directories. · polish: Dashboard charts, shadcn UI, responsive design; friends tested and bugs fixed per page.
**Claims:** Finished each project part on time | Used friends to try to break the product and fixed bugs
**Gaps:** Devpost lists Flask and PostgreSQL while README describes Express and in-memory storage; feature list follows both; No video
Sources: https://devpost.com/software/sustainable-earth-eco-finance, evidence/bitcamp-bitcamp-2025-sustainable-earth-eco-finance.json, https://bitcamp2025.devpost.com/

---

### Tariffix
*Bitcamp Bitcamp 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of MongoDB Atlas

**What it is:** A monorepo with a Next.js site that teaches how import tariffs work and a Chrome extension that reads product pages on stores like Amazon and Walmart, suggests an HTS code and estimates the tariff duty, using Gemini and a MongoDB tariff dataset.
**Problem / user:** Average American shoppers who cannot see the hidden tariff cost in everyday purchases.

**Features**
- Chrome extension tariff overlay — Analyzes product pages, suggests an HTS code and estimates duties on retail sites. *[shown_working]*
- Educational website — Next.js guide, landing and watch pages explaining tariff basics. *[shown_working]*
- HTS code lookup — Queries a MongoDB store of HTS codes and rates built from scraped tariff tables. *[claimed]*
- AI metadata extraction — Shared backend uses Gemini to read category and origin and compute estimates. *[claimed]*
- Fallback pricing — Algorithm still returns an estimate if lookups fail. *[claimed]*
- News, graphs, price comparison — Future real-time trade news and country rules. *[planned]*

**Flow:** Install the built extension in Chromium → Browse a product page → Extension suggests HTS code and duty estimate → Visit website to learn tariff fundamentals and look up codes

**Prompt:** Build a hack using MongoDB Atlas (MLH Best Use of MongoDB Atlas).
**Fit (implied):** MongoDB with Mongoose stores the custom HTS code and tariff-rate dataset that powers lookups and estimates.  *(targeted: [MLH] Best Use of MongoDB Atlas)*
**Sponsor tools:** MongoDB Atlas (Stores HTS codes and tariff rates, core); Gemini API (Extract product metadata and estimate duties, supporting)
**AI:** Gemini scrapes and interprets product metadata (category, origin) to map to HTS codes and tariff estimates.
**Architecture:** pnpm monorepo: Next.js website, Vite Chrome extension and shared AI backend over MongoDB.
**Novelty:** Consumer-facing tariff estimator embedded directly in shopping pages, with a self-built dataset because the official API was outdated.
**Scope:** medium · working: Demo video and 15 screenshots on Devpost; monorepo with ~85 files and install steps. · polish: Logo, landing and guide pages, extension UI; README with setup.
**Gaps:** video not watched
Sources: https://devpost.com/software/tariffix, evidence/bitcamp-bitcamp-2025-tariffix.json (README), https://bitcamp2025.devpost.com/

---

### VisuWorld
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Prettiest Hack - Alumni Team; [MLH] Best Use of Gemini API

**What it is:** A web app where you speak a description and Gemini writes a GLSL shader that renders as a navigable 3D world in the browser, using retrieval over a database of Shadertoy snippets. You can keep speaking to refine the world and publish it to a gallery.
**Problem / user:** Anyone, including people with dexterity limits, wanting to create real-time 3D graphics without writing shader code.

**Features**
- Voice prompting — Chrome Web Speech API converts speech to text in the browser. *[shown_working]*
- Gemini shader generation — Gemini 2.0 Flash and 2.5 Pro write GLSL from the prompt. *[shown_working]*
- RAG over Shadertoy snippets — About 34,000 scraped snippets embedded with OpenAI models in ChromaDB guide generation. *[shown_working]*
- Iterative refinement — Current world code is passed back as context for follow-up edits. *[shown_working]*
- Three.js rendering — Generated shader runs in browser via Three.js and WebGL. *[shown_working]*
- Public gallery — Users publish created worlds. *[claimed]*

**Flow:** Speak a world description → Speech turned into text → Gemini generates GLSL with retrieved snippets → Browser renders 3D landscape → Speak refinements or new worlds → Publish to gallery

**Prompt:** Use the Gemini API to build AI-powered apps (MLH Best Use of Gemini API); also Prettiest Hack: most beautiful hack, may favor form over function.
**Fit (implied):** Gemini is the core generator of visuals; the output is a visual 3D shader world, matching the Prettiest Hack criterion.  *(targeted: Prettiest Hack - Alumni Team, [MLH] Best Use of Gemini API)*
**Sponsor tools:** Gemini API (Natural-language to GLSL shader generation, core)
**AI:** Gemini 2.0 Flash / 2.5 Pro generate GLSL; RAG retrieves similar Shadertoy code via OpenAI embeddings in ChromaDB; the current shader is fed back for iteration.
**Architecture:** React/Next.js client with Web Speech and Three.js; backend calls Gemini and queries ChromaDB vector store; shaders execute client-side.
**Novelty:** Voice-to-shader pipeline grounded in a large scraped shader corpus; heavy compute stays on the client.
**Scope:** medium · working: Live demo at create.visuworld.tech and a gallery feature; no repo. · polish: Custom domain, gallery; no video.
**Claims:** RAG database of 25,000+ (elsewhere ~34,000) shader snippets | Even ~500 samples noticeably improved output
**Gaps:** no repo; no video; snippet count inconsistent on page
Sources: https://devpost.com/software/visuworld, https://bitcamp2025.devpost.com/

---

### World Racing
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Razzle Dazzle Hack - Bitcamp

**What it is:** A browser racing game on real-world 3D Mapbox maps: pick any place, set start, finish and checkpoints, preview with a drone flyover, then drive a custom-physics car, alone or against friends over WebSockets.
**Problem / user:** People who want to explore cities but lack time or money, and those who want to practice navigation or unfamiliar driving routes beforehand.

**Features**
- Course creation anywhere — User chooses a real location and defines start, finish and checkpoints; points are converted to a drivable road path. *[shown_working]*
- Drone flyover — Cinematic preview of the route before racing. *[shown_working]*
- Custom car physics — Self-written physics (angular velocity, acceleration, point-to-segment distance) in Three.js with third-person camera. *[shown_working]*
- Driving HUD and environment — Speedometer, compass, landmark and turn cues, time-of-day changes and rain. *[shown_working]*
- Real-time multiplayer — Rust Axum WebSocket server for racing friends. *[claimed]*
- Saved user maps — PostgreSQL with SeaORM stores courses and user-generated maps. *[claimed]*

**Flow:** Open site in browser → Choose a location on the map → Set start, finish and checkpoints → Watch drone flyover → Race with HUD → Invite friends to race

**Prompt:** Best Razzle Dazzle Hack: most unique project; awarded to two projects that best entertain the judges.
**Fit (implied):** Playful Mario Kart-style racing across real cities with cinematic visuals; the page does not name the prize.  *(targeted: Best Razzle Dazzle Hack - Bitcamp)*
**AI:** none
**Architecture:** React/Vite frontend with Mapbox GL JS and Three.js; Rust Axum REST and WebSocket backend with PostgreSQL via SeaORM; Docker Compose with GitHub CI.
**Novelty:** Turns any real city into a drivable course with a self-built physics engine and Rust backend, a larger systems stack than typical hackathon games.
**Scope:** large · working: Hosted demo and GIF; repo with about 11k LOC, Rust workspace, Docker and CI. · polish: Drone shots, weather and sound effects; 34 likes; collision detection scrapped for lack of map data.
**Claims:** Race any real city in seconds | Targets 60 FPS map performance (stated target, not measured)
**Gaps:** No video; Multiplayer maturity unverified
Sources: https://devpost.com/software/world-racing, evidence/bitcamp-bitcamp-2025-world-racing.json, https://bitcamp2025.devpost.com/

---

### μTeX (MuTeX)
*Bitcamp Bitcamp 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Bitcamp Hack - Bitcamp

**What it is:** A solo-built web app that points a live camera at a blackboard, sends frames to Gemini with a prompt, and returns clean LaTeX for handwritten math, with browser text-to-speech to read it aloud for blind or visually impaired users.
**Problem / user:** Handwritten blackboard math is slow to capture in LaTeX and hard for blind students to access; aimed at math students, blind users and inclusive education.

**Features**
- Live blackboard capture — Browser camera frames are fed to Gemini with a transcription prompt. *[shown_working]*
- Math to LaTeX — Gemini returns LaTeX script for equations, usable in notes or papers. *[shown_working]*
- Text-to-speech — Browser built-in speech reads the LaTeX aloud for accessibility. *[claimed]*
- Planned improvements — Live LaTeX compile for checking, TTS speed and volume control, deployment. *[planned]*

**Flow:** Open the web page and allow camera → Point at blackboard → Gemini transcribes to LaTeX → Copy output or listen via TTS

**Prompt:** Best Bitcamp Hack: hacks that make the judges want to join the winners by the campfire; unearth your potential.
**Fit (none):** Page does not connect to the prize wording; it is a solo accessibility tool built late with limited resources.  *(targeted: Best Bitcamp Hack - Bitcamp)*
**Sponsor tools:** Gemini API (Math OCR to LaTeX from camera frames, core)
**AI:** Multimodal Gemini API with a prompt turns camera frames into LaTeX; no other models.
**Architecture:** Static HTML/CSS/JavaScript page that captures camera frames, calls Gemini directly from client JS, and uses the browser speech API.
**Novelty:** Pairs real-time blackboard OCR with an accessibility angle based on LaTeX being screen-reader friendly.
**Scope:** tiny · working: Screenshots show live transcription; video embedded; repo is five files, about 300 LOC. · polish: Plain old-style design; not deployed because the API key sits in client-side JS.
**Gaps:** Video not watched; No live demo; Accuracy not measured
Sources: https://devpost.com/software/tex-mutex, evidence/bitcamp-bitcamp-2025-tex-mutex.json, https://bitcamp2025.devpost.com/

---

