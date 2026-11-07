# HackUTD — HackUTD 2024 (35 projects)

### AllBank: Inclusive, Intelligent, Impactful
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Goldman Sachs

**What it is:** A React Native mobile banking app for individuals and small businesses with QR payments, goal-based savings, loan planning, an investment dashboard, doorstep banking appointments and a Gemini financial assistant, backed by Firebase.
**Problem / user:** Unbanked and underbanked individuals and small businesses who need accessible, modern banking tools.

**Features**
- Core banking — Manage savings, send money and apply for loans *[claimed]*
- QR code payments — Pay or transfer by scanning QR codes *[claimed]*
- Goal-based savings — Set goals with milestones and contributions *[claimed]*
- Gemini financial assistant — Conversational AI for insights, suggestions and education *[claimed]*
- Investment dashboard — Monitor and analyze investments *[claimed]*
- Doorstep banking — Schedule in-person service appointments *[claimed]*
- Loan planning — Calculate monthly payments and total loan amount *[claimed]*
- Transaction analytics — Breakdown of spending habits *[claimed]*

**Flow:** Sign in with Firebase auth → View accounts and goals → Pay via QR or send money → Chat with the assistant → Plan a loan or book doorstep banking

**Prompt:** not public / not found
**Fit (implied):** A broad inclusive-banking app; the Goldman challenge statement is not public, so the link is inferred from the finance theme.  *(targeted: Goldman Sachs)*
**AI:** Google Gemini powers a conversational assistant for financial queries and insights.
**Architecture:** Expo React Native app using Firebase Firestore and auth, Gemini API calls and some Node.js integration.
**Novelty:** Wide feature surface for a hackathon, including doorstep banking and QR payments aimed at underbanked users.
**Scope:** medium · working: About 4.5k LOC repo and 11 screenshots; no demo or video. · polish: Screenshots and structured README; no tests.
**Gaps:** Goldman prompt text not public; no demo
Sources: https://devpost.com/software/allbank, evidence/hackutd-2024-allbank-inclusive-intelligent-impactful.json

---

### Backtracc
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Hardware; Winner [MLH] Best AI Application Built with Cloudflare; Winner Samba Nova

**What it is:** An in-car hardware and software system for rideshare: back-seat ultrasonic sensors detect riders leaving, a webcam photographs the cabin, a SambaNova-hosted vision LLM lists forgotten items, and the last rider gets a push notification with the photo.
**Problem / user:** Rideshare riders who leave belongings in cars and drivers who spend time and fuel returning them.

**Features**
- Rider exit detection — Three ultrasonic sensors read by a Pico W signal the Raspberry Pi 4 over USB serial *[shown_working]*
- Cabin photo capture — Pi 4 triggers a webcam and uploads the image to the server *[shown_working]*
- Vision LLM item detection — Llama 3.2 Vision 11B on SambaNova identifies left items from the image *[shown_working]*
- Image and metadata storage — Photos stored on Pinata with key-value data on driver, rider and items *[shown_working]*
- Push notification — Most recent rider notified with detected items and the photo *[shown_working]*
- Infrastructure as code — Terraform deploys frontend and manages Cloudflare DNS; backend dockerized on Render *[shown_working]*
- 3D-printed enclosure — Onshape-designed clamp case for the car hub *[shown_working]*

**Flow:** Rider finishes a trip → Sensors see back seats empty → Camera photographs the cabin → Server asks vision model what is left → Image logged on Pinata → Rider gets a push notification

**Prompt:** Pinata and SambaNova prizes have no public challenge text; the MLH Cloudflare prize asks for an AI application built with Cloudflare services such as Workers AI and storage; the Hardware prize has no description.
**Fit (explicit):** Physical sensor and camera rig; vision model hosted on SambaNova; Cloudflare used for DNS, not Workers AI; Pinata used for image storage.  *(targeted: Hardware, MLH Best AI Application Built with Cloudflare, SambaNova)*
**Sponsor tools:** SambaNova (Llama 3.2 Vision 11B) (Identifying items left in the cabin from webcam photos, core); Pinata (Storing photos with per-item metadata, supporting); Cloudflare (DNS management for the frontend, token); Terraform (Deploying the frontend and DNS, supporting)
**AI:** Prompted vision LLM (Llama 3.2 Vision 11B on SambaNova) reads a cabin photo and returns items left behind; prompt engineering was a major focus.
**Architecture:** Pico W with sensors feeds a Pi 4 car hub with webcam; Python hub posts to an Express server (Render) that calls SambaNova, stores to Pinata and pushes notifications; TypeScript frontend deployed via Terraform and Cloudflare.
**Novelty:** Combines embedded C++, Python hub and web stack with a printed enclosure; three codebases and CI with protected main branch.
**Scope:** medium · working: Live site backtracc.tech, repo with frontend, backend, embedded, car-hub, tests, Docker and CI; no video on page. · polish: 3D model doc, Terraform, CI; README is an unfilled template.
**Gaps:** driver notification path unclear; no video; no accuracy numbers
Sources: https://devpost.com/software/project-cd41lvjbiorw, evidence/hackutd-2024-backtracc.json

---

### Capsule
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Pinata [2nd]

**What it is:** A Next.js web app where users upload files into a capsule and share it by URL, QR code or NFC card, so emergency information such as medical records or pet details is reachable quickly. Pinata stores files with metadata and signed links.
**Problem / user:** Families and individuals who need important documents available instantly in emergencies; the creator was inspired by lost files during a relative's medical visits.

**Features**
- Capsules — Container grouping icons, JSON and document files *[shown_working]*
- Share by URL, QR or NFC — Each capsule gets a unique link usable in a QR code or NFC card *[shown_working]*
- Pinata-only storage — Per-file metadata records owner and grouping; signed URLs control access *[claimed]*
- Editor and viewer pages — Landing, capsule list, editor, share and view pages *[shown_working]*
- Passwords and emergency alerts — Capsule passwords and notification on view *[planned]*

**Flow:** Create a capsule in the editor → Add files → Share as a link, QR code or NFC card → Someone scans it and sees the contents

**Prompt:** not public / not found
**Fit (implied):** Uses Pinata for the entire storage layer, including file metadata and signed URLs; the Pinata challenge statement is not public.  *(targeted: Pinata)*
**Sponsor tools:** Pinata (File storage, per-file metadata for ownership and grouping, signed URLs, core)
**AI:** none
**Architecture:** Next.js app with Tailwind and shadcn UI, QR code generation, and Pinata as file store and metadata layer on Vercel.
**Novelty:** Physical-world sharing via NFC cards and pet-tag QR codes with no separate database.
**Scope:** small · working: Live Vercel demo and five screenshots; no repo listed. · polish: Clean UI pages per screenshots list; no passwords yet.
**Gaps:** no repo; no video; Pinata prompt text not public
Sources: https://devpost.com/software/capsule-lp540f

---

### Cheddarboxd
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Pinata; Winner Best Solo Hack

**What it is:** A Letterboxd-style social website for cheese: users rate cheeses and see what other people are trying. Built solo as a SvelteKit PWA with Pinata handling storage.
**Problem / user:** Cheese enthusiasts who want to log, rate and share tastes; the page frames it mainly as a pun-driven joke project rather than a stated pain.

**Features**
- Cheese rating and sharing — Users rate cheeses and publish their tastes to a shared feed *[claimed]*
- Social feed of what others are trying — Browse other users' cheese activity *[claimed]*
- Installable PWA — Served as a progressive web app on a local network; cookie handling was fixed for this *[claimed]*
- Pinata-backed storage — Pinata used as storage layer; docs fed to Cursor to get it working *[claimed]*

**Flow:** Open the PWA → Rate a cheese → Share it → Browse what others are trying

**Prompt:** not public / not found
**Fit (implied):** Uses Pinata as its storage layer and was built by one person; the write-up discusses Pinata docs at length but gives no challenge text it answers.  *(targeted: Pinata, Best Solo Hack)*
**Sponsor tools:** Pinata (storage layer for the app, core)
**AI:** No AI in the product; Cursor was used as a coding assistant during development.
**Architecture:** SvelteKit frontend styled with Tailwind, deployed as a PWA, with Pinata as the storage backend.
**Novelty:** Deliberately comic concept (cheese social network) built by a single person in a weekend; small but complete-feeling social app.
**Scope:** small · working: Demo video linked on Devpost; around 1.2k lines of SvelteKit code. · polish: Repo README is the unmodified SvelteKit template; page text is brief and joking.
**Claims:** Joking "10m DAU and 100k MRR" projection on the next-steps section
**Gaps:** No feature detail beyond one-line description; what Pinata stores is not stated
Sources: https://devpost.com/software/cheddarboxd, https://hackutd-ripple.devpost.com/, https://github.com/joemmalatesta/CheddarBoxd

---

### Data Pattern Observatory
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** PNC Bank

**What it is:** A data observability system that tracks how data is created, moved and used, detects anomalies and trends with statistical models, and shows current and predicted flows in a Streamlit dashboard.
**Problem / user:** Organizations that cannot see how data moves, risking inefficiency, security and compliance trouble; page says the problem came from the PNC challenge.

**Features**
- Real-time data movement tracking — Python backend with Redis monitoring records data flows across MongoDB, Elasticsearch and TimescaleDB stores *[claimed]*
- Pattern and anomaly detection — Statistical models flag unusual patterns in historical data *[claimed]*
- Prediction of future data movement — Statistical forecast of upcoming flow patterns *[claimed]*
- Interactive Streamlit dashboard — Shows current and predicted patterns with usage analytics *[claimed]*
- CrewAI market-crisis agent — Agent meant to predict a crisis from data patterns; not integrated *[planned]*
- Random Forest flow prediction and ML risk ensemble — Separate work to merge into the main app *[planned]*

**Flow:** Start stack with Docker → Data flows are ingested and monitored → Open the Streamlit dashboard → Review current patterns, anomalies and predictions

**Prompt:** not public / not found
**Fit (explicit):** Devpost says the problem statement came from the PNC challenge: giving organizations visibility into data creation, access, movement and use, with business context.  *(targeted: PNC Bank)*
**AI:** Statistical models for pattern detection and forecasting; Random Forest and a CrewAI agent were separate, unintegrated experiments.
**Architecture:** Python processing layer writes to MongoDB, Elasticsearch and TimescaleDB, Redis for real-time monitoring, Docker containers, Streamlit front end.
**Novelty:** Heavy multi-database infrastructure for a hackathon; the stated fit is to an enterprise governance problem rather than a consumer app.
**Scope:** medium · working: README has detailed Docker and Python setup steps; tests exist in repo; no usable demo video. · polish: Detailed README; the Devpost video embed points to an unrelated link.
**Claims:** Says it built a functioning data observability system from scratch
**Gaps:** No valid demo video; repo includes a committed venv so LOC estimate is inflated; sponsor challenge text not public
Sources: https://devpost.com/software/data-pattern-observatory, https://hackutd-ripple.devpost.com/, https://github.com/siddhu-pikachu/data-observability.git

---

### DHy-n0
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner EOG Resources; Winner [MLH] Best .Tech Domain Name

**What it is:** A pipeline safety monitoring web app for oil and gas lease operators. It takes well data, looks for anomalies that could mean hydrate buildup, and charts the results, with an original mascot and its own .tech domain.
**Problem / user:** Lease operators who need to catch hydrate buildups in wells early.

**Features**
- Well data upload — Users upload well data files to the Flask backend *[claimed]*
- Hydrate anomaly detection — Pandas-based analysis flags anomalies thought to indicate hydrate buildup *[claimed]*
- Operator-oriented charts — React frontend with Recharts views designed around a lease operator workflow *[claimed]*
- Branding and promo video — Original mascot, Canva design and a lighthearted promo video; site at dhy-n0.tech *[shown_working]*

**Flow:** Open the site → Upload well data → Backend analyzes it for anomalies → View charts of results

**Prompt:** not public / not found
**Fit (explicit):** README states it was built for the EOG Resources challenge: detect hydrate buildup in wells from data. Also registered a .tech domain for the MLH prize.  *(targeted: EOG Resources, [MLH] Best .Tech Domain Name)*
**AI:** No stated ML model; anomaly inference done with Pandas analysis in the backend.
**Architecture:** React and Recharts frontend talks to a Flask API that runs Pandas analysis on uploaded well data.
**Novelty:** Domain-specific industrial monitoring use case with strong brand identity (mascot, promo video, custom domain).
**Scope:** small · working: Live site and demo video linked; about 800 lines of code. · polish: Custom domain, mascot, and branding; no tests.
**Gaps:** Detection algorithm unspecified; EOG challenge text not public
Sources: https://devpost.com/software/dhy-n0, https://hackutd-ripple.devpost.com/, https://github.com/wenngle/dhy-n0

---

### DuckTalk
*HackUTD HackUTD 2024 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Guided Track

**What it is:** A solo-built companion web app for hackathon attendees with a rubber-duck mascot named Ducky. It combines a to-do list, an interactive Google Map, a five-day weather forecast and Firebase user accounts.
**Problem / user:** Out-of-state hackathon participants working in an unfamiliar city without friends nearby who want to stay organized.

**Features**
- To-do list — Task tracker with hard-coded tasks for prototyping *[claimed]*
- Interactive Google Map — Embedded map for exploring the surroundings *[claimed]*
- 5-day weather forecast — Fetched from WeatherAPI for the user location *[claimed]*
- User accounts — Register and log-in pages backed by Firebase *[claimed]*
- Chat with Ducky — GPT-based chat box on the home page *[planned]*

**Flow:** Register or log in → See the Ducky home page → Check tasks, map and weather

**Prompt:** not public / not found
**Fit (explicit):** Built by following the hackathon's Hacker Project Guide for base structure and database, then themed as a duck companion; this matches the beginner-oriented Guided Track.  *(targeted: Guided Track)*
**AI:** none
**Architecture:** React and Tailwind frontend using Firebase for accounts/data, WeatherAPI for forecast and Google Maps for the map.
**Novelty:** Beginner template-based project; personality comes from the rubber-duck framing.
**Scope:** tiny · working: Page says APIs and Firebase work; no repo, demo or video linked. · polish: None shown; no screenshots described.
**Gaps:** No repo; no demo; Guided Track description not public
Sources: https://devpost.com/software/ducktalk, https://hackutd-ripple.devpost.com/

---

### Echo
*HackUTD HackUTD 2024 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Best Design

**What it is:** A gamified web app that helps neurodivergent children recognize and mimic emotions. Kids copy a 3D mascot's expressions in front of a webcam and take an emotion-recognition quiz with images from Pinata.
**Problem / user:** Children with autism, ADHD, dyslexia or similar conditions who also have alexithymia and find reading faces hard.

**Features**
- Webcam mirroring exercise — Detects facial landmarks and emotion while the child copies the mascot's expression *[claimed]*
- Emotion quiz — Randomized expression images fetched from Pinata; child picks the emotion *[claimed]*
- Model-generated feedback — SambaNova-hosted models give feedback on answers *[claimed]*
- Interactive 3D mascots — Three.js landing mascot that follows the mouse plus an animated guide mascot made in Blender *[claimed]*

**Flow:** Land on home page with reactive 3D mascot → Open webcam trainer and mimic expressions → Get guide feedback → Take the emotion quiz

**Prompt:** Best Design is judged on UI look and also on how well the design reflects thought about user experience.
**Fit (implied):** Strong visual identity (3D mascots, Figma layout) and an accessibility-minded UX for children; page also integrates Pinata and SambaNova.  *(targeted: Best Design, Pinata, SambaNova)*
**Sponsor tools:** Pinata (stores quiz expression images, supporting); SambaNova (fine-tuned model feedback on quiz, supporting)
**AI:** Computer vision for facial landmark and emotion detection from webcam; SambaNova-hosted models for sentiment-style feedback.
**Architecture:** Next.js/React/Three.js frontend, Flask backend processing webcam frames, Pinata for image storage, SambaNova API for feedback.
**Novelty:** Applies emotion recognition to a therapeutic-education use for children, with mascots modeled and rigged in Blender.
**Scope:** medium · working: Team says webcam and quiz pages were completed; no demo video; around 1.9k lines of code. · polish: Design-focused with 3D assets; repo README is the default Next.js template.
**Claims:** Calls its models "scientifically backed" without evidence | Admits slow recognition with multiple faces
**Gaps:** No demo video; no screenshots captions read
Sources: https://devpost.com/software/hackutd-project-kbhins, https://hackutd-ripple.devpost.com/, https://github.com/chaireko/hackutd24

---

### Eco Fast Track
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** CBRE; Veolia

**What it is:** A DIY smart water gauge (Arduino with Grove temperature sensor, potentiometer and LCD in a 3D-printed case) that streams readings to a Next.js web app. It gives managers and tenants usage graphs, AI saving tips and email alerts.
**Problem / user:** Property managers who lose money to faulty water gauges and rely on tenant reports; tenants who want to cut water use.

**Features**
- Sensor-based water gauge — Arduino reads temperature and flow proxy and sends data to a webpage over serial *[shown_working]*
- Usage graphs — Proof-of-concept charts of aggregated usage *[shown_working]*
- Gemini saving tips — Gemini turns a tenant's aggregated readings into personalized advice *[claimed]*
- Over-average email warning — Automated email to tenants whose usage exceeds average (proof of concept) *[shown_working]*
- Wrapped-style visuals and community sharing — Spotify-Wrapped-like data presentation and optional community comparison *[claimed]*
- Leak and freeze-pressure detection — Detect pressure drops or spikes *[planned]*

**Flow:** Device measures water use → Data goes to the web app → Tenant sees graphs and AI tips → Manager sees inefficiencies; high users get an email

**Prompt:** not public / not found
**Fit (implied):** Sustainability angle (water conservation in buildings) with hardware sensing, matching the property-sustainability theme of the CBRE and Veolia tracks; no challenge text cited.  *(targeted: CBRE, Veolia)*
**Sponsor tools:** Pinata (listed on page, role not described, unclear)
**AI:** Google Gemini generates tenant-specific recommendations from aggregated sensor data.
**Architecture:** Arduino with Grove sensors publishes readings (serial; MQTT folders in repo) to a Next.js web app, with Gemini for advice and email alerts.
**Novelty:** Includes custom hardware with a 3D-printed enclosure, rare in sustainability dashboards; WiFi module failed so serial was used.
**Scope:** medium · working: Hardware photos and proof-of-concept graph/email on Devpost; Figma prototype; repo with web and Arduino code. · polish: Figma prototype and Canva design; WiFi planned but dropped.
**Gaps:** No video
Sources: https://devpost.com/software/apartment-monitoring, https://hackutd-ripple.devpost.com/, https://github.com/Fernando4242/HackUTD24-EcoFastTrack

---

### EcoLens (property evaluator)
*HackUTD HackUTD 2024 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Beginner

**What it is:** A Swift app where a user uploads a video of an office or property. Frames are extracted, Google Vision labels furniture, and Llama analyses condition (rips, stains) and suggests sustainable repairs.
**Problem / user:** Property managers who want to repair rather than replace furniture to cut cost and waste.

**Features**
- Video upload — Swift app takes a room video and extracts frames *[claimed]*
- Furniture detection — Google Cloud Vision labels items in frames *[claimed]*
- Wear and damage flagging — Llama contextual analysis spots rips, stains and condition *[claimed]*
- Repair and eco suggestions — LLM returns sustainable repair and energy-efficiency tips *[claimed]*
- IoT live tracking — Sensors to track furniture condition over time *[planned]*

**Flow:** Upload room video in the Swift app → Frames are stored in Pinata → Vision labels furniture → LLM returns condition report and repair suggestions

**Prompt:** not public / not found
**Fit (implied):** Page states a beginner-team project that learned Pinata, Google Vision and Llama; no stated fit to a specific sponsor challenge.  *(targeted: Best Beginner)*
**Sponsor tools:** Pinata (stores extracted video frames, supporting)
**AI:** Google Cloud Vision for object labeling plus a fine-tuned Llama for text and image-to-text condition analysis.
**Architecture:** Swift client uploads video; Python backend extracts frames, stores them in Pinata, calls Vision then Llama and returns insights.
**Novelty:** Multi-stage vision-plus-LLM pipeline for furniture condition, aimed at repair over replacement.
**Scope:** small · working: Pipeline described; no repo, demo or video linked. · polish: No assets visible.
**Gaps:** No repo or demo; Best Beginner description not public
Sources: https://devpost.com/software/property-evaluator, https://hackutd-ripple.devpost.com/

---

### EcoLens (Sustainable Building Manager)
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Veolia

**What it is:** A building sustainability dashboard with interactive graphs of energy, water and carbon trends, HVAC and occupancy analysis, and simulation sliders to preview changes, plus a map of sustainability scores. Devpost text is nearly empty; README holds the detail.
**Problem / user:** Commercial building managers who need to monitor and cut energy, water and carbon from afar.

**Features**
- Interactive trend graphs — Energy, water and carbon charts plus HVAC use and energy vs occupancy views *[claimed]*
- Simulation sliders — Adjust energy, water and emissions metrics to see simulated impact *[claimed]*
- Sustainability score map — Map view of location scores *[claimed]*

**Flow:** Open dashboard → View usage trends → Move sliders to simulate changes → Check map scores

**Prompt:** not public / not found
**Fit (explicit):** README says it was built for the Veolia and CBRE sustainability challenges for commercial buildings and won the Veolia award.  *(targeted: Veolia, CBRE)*
**AI:** none
**Architecture:** React app (Next-style app dir) with a Flask Python backend in cbre-backend.
**Novelty:** Simulation sliders make it a what-if tool rather than a static dashboard.
**Scope:** small · working: README includes dashboard screenshots; about 1.5k lines of code. · polish: Screenshots in README; Devpost sections left blank.
**Claims:** README: built in 24 hours
**Gaps:** Devpost narrative blank; feature list from README only first ~1100 chars read
Sources: https://devpost.com/software/ecolens-pqk62d, https://hackutd-ripple.devpost.com/, https://github.com/Sami-ul/Sustainable-Building-Manager

---

### EcoVerse
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** CBRE

**What it is:** A Unity VR experience: a virtual replica of an office where property managers see live energy and water data, talk to an AI avatar, and feel changes through bHaptics gloves, with Photon multiplayer for remote technicians.
**Problem / user:** Property managers who want remote, intuitive monitoring of building energy and water, plus technicians who troubleshoot with them.

**Features**
- VR office replica — Unity scene of an office to walk through *[claimed]*
- Live usage charts — Streamlit-generated data (Faker synthetic) streamed to Unity over sockets as bar and line graphs *[claimed]*
- AI assistant avatar — Llama via SambaNova API answers inside VR; lip sync built with Ready Player Me avatars *[claimed]*
- Haptic feedback — bHaptics thermo-tactile gloves let managers feel spikes or savings *[claimed]*
- Multi-user collaboration — Photon networking to invite technicians *[claimed]*
- IoT and AR extensions — Sensors and AR for system interaction *[planned]*

**Flow:** Put on headset in the virtual office → Ask the AI assistant questions → Review graphs → Get recommendations → Invite a technician and feel haptic cues

**Prompt:** not public / not found
**Fit (implied):** Tackles building energy and water efficiency in offices via VR monitoring, matching the CBRE sustainability-property track; uses SambaNova API.  *(targeted: CBRE, SambaNova)*
**Sponsor tools:** SambaNova (Llama API behind the AI assistant, core)
**AI:** Llama served by SambaNova powers a conversational assistant and recommendations; data is synthetic.
**Architecture:** Unity C# VR client with Photon multiplayer, sockets receive data from a Python Streamlit analytics app, SambaNova API for AI, bHaptics SDK.
**Novelty:** VR plus haptics for building analytics is unusual; large Unity project with about 50k LOC (mostly assets/scripts).
**Scope:** large · working: Large Unity repo; Drive file linked but not labeled; page inconsistent on whether remote joining works. · polish: Detailed README and Canva design.
**Gaps:** Demo file not read; LOC may include third-party assets
Sources: https://devpost.com/software/ecoverse-5dczmp, https://hackutd-ripple.devpost.com/, https://github.com/FireboltLegend/HackUTD-2024

---

### FinnAI
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** PNC Bank

**What it is:** A Streamlit personal finance app with an AI budgeting chatbot, automatic expense categorisation, savings goal tracking and dashboards, with Firebase for storage and sync.
**Problem / user:** Everyday people who find budgeting and saving intimidating.

**Features**
- AI budgeting chatbot — Gives tailored advice to stay on budget; model not named *[claimed]*
- Automatic expense categorisation — Real-time categorisation and spending insight *[claimed]*
- Savings goals — Targets with AI encouragement *[claimed]*
- Dashboards — Interactive charts of income, expenses and goal progress *[claimed]*
- Bank integration and mobile app — Linked accounts and phone version *[planned]*

**Flow:** Enter or track expenses → View dashboard → Set savings goals → Ask the chatbot for advice

**Prompt:** not public / not found
**Fit (implied):** A consumer personal-finance tool, aligned with the bank sponsor, but the page does not cite a challenge.  *(targeted: PNC Bank)*
**AI:** Chatbot with unspecified ML models analysing user data for advice.
**Architecture:** Streamlit front end, Python analytics, Firebase backend for storage and sync.
**Novelty:** Fairly standard AI budgeting concept.
**Scope:** small · working: Embedded demo video exists but contents not described; no repo. · polish: Not visible.
**Gaps:** No repo; video not viewable
Sources: https://devpost.com/software/finnai, https://hackutd-ripple.devpost.com/

---

### FrontierMap
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Frontier

**What it is:** An iOS RoomPlan app scans a home in AR; a web app (frontiermap.tech) takes the exported USDZ, flattens it to a 2D floor plan, lets the user mark the router and extender count, and shows a Wi-Fi coverage heatmap with suggested extender spots.
**Problem / user:** Frontier Internet customers with weak Wi-Fi in parts of the home who do not know where to place extenders.

**Features**
- AR home scan — iOS RoomPlan app produces a 3D room model exported as USDZ *[claimed]*
- 3D to 2D floor plan — Flask backend converts the model to a flat plan *[shown_working]*
- Extender placement — Algorithm picks best spots for a user-set number of extenders *[shown_working]*
- Coverage heatmap — Predicted signal coverage shown over the plan *[shown_working]*
- Sample USDZ and live site — Test house file and deployed site for judges *[shown_working]*
- Multi-story and ML signal analysis — Planned extension *[planned]*

**Flow:** Scan home or use sample USDZ → Upload on frontiermap.tech → Place router marker → Press Done → View heatmap and extender recommendations

**Prompt:** not public / not found
**Fit (implied):** Directly helps Frontier internet customers optimize home Wi-Fi coverage with extender placement.  *(targeted: Frontier)*
**Sponsor tools:** Pinata (listed in built-with, role not described, unclear)
**AI:** No ML implemented; geometric placement algorithms. ML signal analysis is future work.
**Architecture:** SwiftUI RoomPlan iOS app, Next.js and Tailwind web front end, Flask Python service converting USDZ to OBJ and computing placements, Docker.
**Novelty:** Combines LiDAR AR scanning with a web geometry pipeline, uncommon for a networking sponsor challenge.
**Scope:** medium · working: Live demo site and backup deployment, sample file, video; about 5k LOC. · polish: Landing page, screenshots and Docker setup.
**Claims:** Claims accurate and useful recommendations; no coverage measurements
**Gaps:** none
Sources: https://devpost.com/software/frontierbeyond, https://hackutd-ripple.devpost.com/, https://github.com/davidgamingvn/extended-frontier

---

### FUELICIENT
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Toyota [1st]

**What it is:** A Streamlit app for exploring Toyota fuel-efficiency data with stats and visualizations. Users log in, edit and save modified datasets to their account, and export CSVs.
**Problem / user:** Anyone analyzing the supplied Toyota fuel data who finds raw figures unintuitive and hard to remember.

**Features**
- Interactive exploration — Streamlit UI with fuel-efficiency calculations and statistics *[claimed]*
- Visualizations — Charts of the dataset *[claimed]*
- Accounts and saved analyses — Firebase auth and per-account settings keep earlier work *[claimed]*
- Dataset editing and CSV export — Create modified datasets and download them *[claimed]*
- Pinata/IPFS storage — Data kept on Pinata *[claimed]*

**Flow:** Log in → Explore the data → Modify and save a dataset → Download as CSV

**Prompt:** MLH Best Use of Streamlit: build a Python web app with Streamlit.
**Fit (implied):** Analysis tool over the Toyota-provided fuel data; Streamlit GUI and Pinata for storage.  *(targeted: Toyota [1st], Pinata, MLH Streamlit)*
**Sponsor tools:** Pinata (IPFS storage of fuel data, core); Streamlit (whole GUI, core)
**AI:** none
**Architecture:** Python/pandas backend with Streamlit UI, Firebase auth and settings, Pinata IPFS storage, with multiple deploy links.
**Novelty:** Persistent user-owned dataset copies are an unusual addition for a data viewer.
**Scope:** small · working: Three live demo links and a video; no repo. · polish: Custom domain.
**Gaps:** No repo
Sources: https://devpost.com/software/fuelicient, https://hackutd-ripple.devpost.com/

---

### GitFile
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [MLH] Best Use of Terraform

**What it is:** A custom C wrapper around Git so flat files (PDF, DOCX, XLSX, JPG) store only their changed parts. A web dashboard shows version history and storage cost, edits PDFs via PDF.js, and has an embedded SSH terminal; history lives in Pinata.
**Problem / user:** Businesses that repeatedly back up near-identical documents and pay for the duplicate storage.

**Features**
- Git wrapper for flat files — C commands extend git add/push to capture diffs of non-code files *[claimed]*
- Dashboard with history — One-screen view of versions and storage cost *[claimed]*
- SSH terminal — Restricted SSH session embedded in the site, bridging to a local git session *[claimed]*
- PDF editing — "edit" command opens PDF.js in the dashboard *[claimed]*
- Pinata history storage — Storage and retrieval APIs hold git history *[claimed]*
- Terraform-provisioned Azure VM — Server infrastructure defined in Terraform *[claimed]*

**Flow:** Open gitfile.tech → Edit a PDF via dashboard or terminal → Run git push → See version history and cost saved

**Prompt:** MLH Best Use of Terraform: use Terraform in the project.
**Fit (explicit):** Azure VM, networks and gateways provisioned with Terraform; Cloudflare DNS for the domain.  *(targeted: [MLH] Best Use of Terraform, Pinata)*
**Sponsor tools:** Terraform (provisioning Azure VM and networking, core); Pinata (git history storage, core)
**AI:** none
**Architecture:** Next.js dashboard, Node/Express server, custom C git wrapper on an Azure VM, SSH bridged into an iframe, Pinata storage.
**Novelty:** Low-level systems work (C git wrapper) rather than a typical web app.
**Scope:** medium · working: Website live at gitfile.tech; about 4k LOC; no video. · polish: Dashboard plus terminal; README is minimal.
**Claims:** Over 500x storage cost reduction in benchmarked business cases
**Gaps:** Benchmark method not given
Sources: https://devpost.com/software/gitfile, https://hackutd-ripple.devpost.com/, https://github.com/ssaniya-dev/GitFile

---

### Greenify
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** CBRE

**What it is:** A sustainability platform for office property managers with an emissions calculator that yields a sustainability score, a GPT-4 advice chatbot, and a map of CBRE locations whose emissions are scored with LLaMA 3 over vectorized CBRE reports in Pinecone.
**Problem / user:** Businesses and property managers who want insight into their emissions and ways to improve.

**Features**
- Emissions calculator — Real-time footprint calculation with a custom sustainability score *[claimed]*
- GPT-4 chatbot — Context-aware advice on cutting emissions *[claimed]*
- Interactive emissions map — Scores for CBRE locations with predictive breakdowns, scored by LLaMA 3 *[claimed]*
- RAG pipeline — CBRE environmental reports parsed with Llama and embedded into Pinecone *[claimed]*

**Flow:** Landing page → View map of CBRE locations → Run carbon calculator → Ask chatbot

**Prompt:** not public / not found
**Fit (explicit):** Devpost says it was built for the CBRE challenge on sustainable office spaces, using CBRE location and report data.  *(targeted: CBRE)*
**AI:** GPT-4 chatbot; LLaMA 3 for analytics and parsing; Pinecone retrieval over CBRE reports.
**Architecture:** Next.js/Tailwind frontend, Flask backend with algorithms, Pinecone vector store, map layer.
**Novelty:** Grounds chatbot in the sponsor's own location data via RAG.
**Scope:** small · working: Video linked; repo README empty feature headings; around 350 LOC in the main repo. · polish: Screenshots of three landing pages, map, calculator, chatbot.
**Gaps:** Page inconsistent on Leaflet vs Google Maps; main repo thin; code in other repos
Sources: https://devpost.com/software/greenwise-y6o4bu, https://hackutd-ripple.devpost.com/, https://github.com/yfshaikh/greenify

---

### Hermes
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** PNC Bank

**What it is:** A crypto wallet and investing app for people outside traditional banking, showing balance and credit score, live prices and news from CoinGecko, zoomable charts, price predictions and risk analysis, with a FastAPI backend.
**Problem / user:** People contributing to the economy but lacking banking, investment access or retirement systems, notably the Hispanic community.

**Features**
- Account view — Balance and credit score display *[claimed]*
- Live crypto prices and charts — CoinGecko data in zoomable Chart.js graphs *[claimed]*
- Crypto news — CryptoNews API feed *[claimed]*
- Price prediction — PyTorch LSTM model, though unclear it drives the shown predictions *[claimed]*
- Risk analysis — Helps users understand risk *[claimed]*
- Pension-style payouts — Monthly payouts from portfolios *[planned]*

**Flow:** View balance and score → Check prices and charts → Buy or sell crypto → Review predictions and risk

**Prompt:** not public / not found
**Fit (implied):** Fintech access angle: banking and investing through a crypto wallet for the unbanked.  *(targeted: PNC Bank)*
**AI:** PyTorch LSTM on historical CoinGecko prices for prediction.
**Architecture:** React frontend with Chart.js, FastAPI backend calling CoinGecko and news APIs, pandas/PyTorch for modeling.
**Novelty:** Unbanked-community framing around crypto.
**Scope:** medium · working: Demo video and backend modules; committed node_modules/venv inflate LOC. · polish: Default CRA README; one screenshot.
**Gaps:** Whether LSTM is wired in
Sources: https://devpost.com/software/hermes-c2onvq, https://hackutd-ripple.devpost.com/, https://github.com/AndrewG4404/HackUTD

---

### Homelander
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Frontier

**What it is:** A data-driven app that recommends home internet products from usage and outage data and gives the company outage predictions and statistics per city, with animated visualizations.
**Problem / user:** Internet customers choosing monthly plans and the provider wanting dataset stats and outage forecasts.

**Features**
- Rule-based plan recommendations — Suggests fiber when wireless connections exceed 25 and upgrades when devices hit 95% bps *[claimed]*
- Outage-risk advice — Battery pack and resilient wifi suggested for flagged cities *[claimed]*
- Preventive add-ons — Security, YouTube TV, identity theft protection for heavy-connection users *[claimed]*
- Company stats and outage prediction — Per-city outage predictions and dataset statistics *[claimed]*
- Predictive issue-resolution model — Help customers fix problems *[planned]*

**Flow:** Open flight.thehomelander.tech → See recommendations from usage data → Company view shows stats and outage predictions

**Prompt:** not public / not found
**Fit (implied):** Uses customer product and outage data to recommend Frontier-style services and predict outages.  *(targeted: Frontier)*
**AI:** Unnamed ML for recommendation and outage prediction; thresholds visible in text.
**Architecture:** React frontend with Python backend and ML models over provided datasets.
**Novelty:** Two-sided view (customer and company) in one app.
**Scope:** small · working: Live link to deployed app; no repo or video. · polish: Not described.
**Gaps:** No repo; demo not opened
Sources: https://devpost.com/software/homelander, https://hackutd-ripple.devpost.com/

---

### InvestIQ
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** First Place [1st]; Infosys

**What it is:** A chat-based investing platform where beginners describe trading strategies in plain language, have them backtested on simulated data and get AI feedback, including chart analysis by a vision model, plus an educational chatbot.
**Problem / user:** Beginners and non-technical investors who understand markets but cannot code strategies.

**Features**
- Natural-language strategy builder — Autogen agents turn a described idea into a runnable strategy *[claimed]*
- Simulated backtesting — Tests strategies on realistic market data *[claimed]*
- Education chatbot — Llama 3.1 8B explains market concepts *[claimed]*
- Graph analysis — Llama 90B Vision reads performance charts *[claimed]*
- Stock insights — Perplexity context for stock views *[claimed]*
- Live trading integration — Execute on real platforms *[planned]*

**Flow:** Landing page → Ask the educational chatbot → Describe a strategy to the generator → View graphs and feedback → Refine

**Prompt:** not public / not found
**Fit (implied):** Page also lists a SambaNova hackathon win; Infosys fit is not described.  *(targeted: Infosys, First Place [1st], SambaNova)*
**Sponsor tools:** SambaNova Cloud (Llama chat and vision models, core)
**AI:** Autogen agents, Llama 3.1 8B and 90B Vision on SambaNova, Cohere embeddings, Perplexity for context.
**Architecture:** Next.js frontend, Flask backend running agents, backtests and model calls.
**Novelty:** Uses a vision model to review its own performance charts.
**Scope:** medium · working: Four screenshots and repo with 3.5k LOC; no video. · polish: Detailed README.
**Claims:** Vision model checks graphs show an upward trend, a questionable design
**Gaps:** Infosys prompt not public
Sources: https://devpost.com/software/investiq-1b0cio, https://hackutd-ripple.devpost.com/, https://github.com/krish-shar/hackutd-ripple-effect

---

### KaizenDrive
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Toyota

**What it is:** A Streamlit dashboard of four years of Toyota car data with competitor comparison, a build-your-own dashboard feature, and a RAG chatbot using OpenAI and sentence-transformers.
**Problem / user:** Engineers who waste time on environment setup and want to analyze car data without writing code.

**Features**
- Summary dashboard — Interactive view of Toyota product suite *[claimed]*
- Competitor comparison — Compares Toyota specifics to rivals *[claimed]*
- Custom dashboard builder — User composes their own analyses *[claimed]*
- RAG chatbot — OpenAI with sentence-transformer retrieval answers dataset questions *[claimed]*
- Predictive driving trends — Planned *[planned]*

**Flow:** Open dashboard → Compare competitors → Build custom views → Ask chatbot

**Prompt:** not public / not found
**Fit (implied):** Analysis tool over Toyota car data aimed at engineers.  *(targeted: Toyota)*
**Sponsor tools:** Pinata (listed, role not stated, unclear)
**AI:** OpenAI-powered RAG; open-source model tried and dropped for cost.
**Architecture:** Streamlit app, SentenceTransformer embeddings, OpenAI API, pandas.
**Novelty:** In-house RAG over tabular car data.
**Scope:** small · working: Video and Drive demo linked; 1.5k LOC. · polish: Minimal README.
**Gaps:** Missing values degrade graphs
Sources: https://devpost.com/software/project-ip7kgx0314sh, https://hackutd-ripple.devpost.com/, https://github.com/srutiswathi/hackUTD_24

---

### Lumo
*HackUTD HackUTD 2024 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** General; Goldman Sachs

**What it is:** Group expense app where each participant's own card is charged their share at the moment of purchase, so nobody fronts cash and waits for repayment. Built as a React front end with Stripe-backed payments and a Node/Mongo backend.
**Problem / user:** Unbanked and underbanked people sharing rent, groceries and utilities, who currently rely on cash pooling or reimbursement apps that depend on timely repayment.

**Features**
- Real-time split at purchase — Charges each member's card on file their share when the purchase happens instead of reimbursing later *[claimed]*
- Monthly pledge — User adjusts a monthly pledge amount toward the group *[claimed]*
- Group and member selection — Pick which group you are paying for and which members cover costs *[claimed]*
- Shared card payment — Pay with a shared credit card; prepaid cards and ACH also supported *[claimed]*
- Itemized receipt splitting (Square POS) — Pull itemized receipts and split pre-approved items, with ML item assignment *[planned]*

**Flow:** Open app past loading screen to home → Adjust monthly pledge → Choose which group members cover costs → Choose which group you are paying for → Pay with the shared card

**Prompt:** not public / not found
**Fit (implied):** Page frames it around unbanked and underbanked users and shared-payment fintech, which matches the Goldman Sachs track by inference; no explicit prize statement.  *(targeted: General, Goldman Sachs)*
**AI:** none
**Architecture:** React/Vite/Tailwind front end with Zustand state calls an Express backend using Mongoose/MongoDB, which talks to Stripe to charge participants.
**Novelty:** Reframes bill splitting as simultaneous multi-card charging rather than peer reimbursement; also uses Stripe for real transactions.
**Scope:** small · working: Page claims a fully functional MVP with real transaction processing; repo has front end and backend, no demo link. · polish: Six screenshots; README is nearly empty; no tests.
**Claims:** Fully functional MVP handling real-time transactions | Apple Pay/Apple Cash support not achieved due to Stripe POS permission delay
**Gaps:** No prize text; No video or demo; README empty
Sources: https://devpost.com/software/pay-your-daddy, https://github.com/danielodicho/lumo (evidence file)

---

### Monch
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Pinata [1st]

**What it is:** Web app that estimates calories, carbs, fats and protein from a photo of a meal using a self-trained image classifier plus a public nutrition dataset, and tracks daily totals against the user's goals. Photos and data are stored in Pinata.
**Problem / user:** People tracking macros who find manual logging tedious and paywalled, especially when foods lack printed nutrition values.

**Features**
- Photo food recognition — Custom-trained neural network classifies the food in an uploaded meal photo *[shown_working]*
- Macro calculation — Looks up calories, carbs, fats, protein for the recognized food from a public dataset *[claimed]*
- Goal import and daily tracking — User brings macro goals at sign-up; daily intake compared with targets *[claimed]*
- Macro graph over days — Charts macro totals across different days *[claimed]*
- Pinata image storage — Stores meal images and data through Pinata and shows them with nutrition info *[claimed]*
- Accounts — Clerk authentication *[claimed]*

**Flow:** Sign up and import macro goals → Photograph a meal → App classifies the food → Image and macros stored and shown → View daily totals and trend graph

**Prompt:** not public / not found
**Fit (explicit):** Uses Pinata to store meal images and associated data; the page names Pinata as the storage layer and the prize won.  *(targeted: Pinata [1st])*
**Sponsor tools:** Pinata (File storage for meal images and associated data, core)
**AI:** Self-trained image classification network (not an LLM API) maps a meal photo to a food class, then a public nutrition table gives macros. Architecture and dataset not stated.
**Architecture:** Next.js/React site with Clerk auth; photo goes to the trained classifier, nutrition lookup returns macros, and images plus data are kept in Pinata; backend repo is separate.
**Novelty:** Trained its own classifier by team that was new to ML, rather than calling a hosted vision model.
**Scope:** small · working: Live site monch.tech and demo video linked; the team says it correctly classified a hotdog photo. · polish: Deployed site with auth and charts; backend repo is tiny with no README.
**Claims:** Classifier correctly identified a hotdog image | Built without ChatGPT-style API calls
**Gaps:** No prize text; Frontend repo not linked; Model details unstated
Sources: https://devpost.com/software/monch-e5k0hv, evidence/hackutd-2024-monch.json

---

### Notable
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Samba Nova

**What it is:** AI note-taking web app that transcribes lectures live, lets users edit notes with natural-language commands, turns descriptions into Mermaid diagrams, and answers questions through a voice assistant. Notes can be shared by link or exported to PDF.
**Problem / user:** Students and developers who struggle to take organized notes during lectures and technical discussions with ordinary note apps.

**Features**
- Live lecture transcription — Real-time speech to text during a lecture *[claimed]*
- Natural-language note editing — Commands to rewrite or enhance note content via LLM *[claimed]*
- Diagram generation — Text descriptions converted to Mermaid diagrams via prompt engineering *[claimed]*
- Voice assistant — Context-aware assistant answers questions about notes and suggests improvements *[claimed]*
- Agentic context enrichment — crewAI agents pull context from websites; ChromaDB/SQLite link related notes *[claimed]*
- Share and export — Unique share links and PDF export *[claimed]*
- Floating selection toolbar — Toolbar appears on text selection for AI actions *[claimed]*

**Flow:** Sign in (Supabase) → Start lecture transcription → Edit and enhance notes with AI or commands → Generate diagrams → Ask the voice assistant → Share link or export PDF

**Prompt:** not public / not found
**Fit (explicit):** Uses SambaNova inference for fast, large-context LLM calls on lecture content; the page credits SambaNova for low latency.  *(targeted: Samba Nova)*
**Sponsor tools:** SambaNova API (Fast LLM inference with large context for note enhancement and diagrams, core)
**AI:** Llama models served via SambaNova for editing, summarization and Mermaid generation; crewAI agents gather web context; ChromaDB stores embeddings for cross-note linking.
**Architecture:** React/Vite front end, FastAPI backend deployed on AWS (S3, SageMaker, Terraform), Supabase for auth/db, ChromaDB plus SQLite for persistence.
**Novelty:** Combines transcription, diagram generation, agent retrieval and voice in one note app, with Terraform-managed AWS deployment.
**Scope:** medium · working: Vercel demo and live FastAPI docs link listed; about 6k LOC. · polish: Dockerfile present; README is a stub; no video; no tests.
**Claims:** Transcription and enhancement with negligible delay | Surprisingly accurate generated diagrams
**Gaps:** No prize text; README stub; Databricks role unclear
Sources: https://devpost.com/software/pipeview, evidence/hackutd-2024-notable.json

---

### PipeBrAIns
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** EOG Resources

**What it is:** Dashboard for pipeline owners that predicts hydrate blockages in oil pipelines with a random-forest model trained on the sponsor's data. It offers trend charts, an alerts page, manual data entry for predictions and email notices.
**Problem / user:** Pipeline owners who need early warning of hydrate formation, which can freeze gas flow during rapid pressure drops and endanger people and the environment.

**Features**
- Hydrate prediction — Scikit-learn random forest on four numeric inputs scores likelihood of hydrate *[claimed]*
- Custom prediction API — Flask API serves model predictions to the web UI *[claimed]*
- Trend charts — Chart API graphs pipe data trends *[claimed]*
- Alerts tab — Shows alerts updating every second from pipe data *[claimed]*
- Manual data entry — Owner types values and sees a prediction *[claimed]*
- Owner login and email alerts — Firebase login; SendGrid dynamic-template emails *[claimed]*

**Flow:** Log in via Firebase → View home and pipes pages → Read trend charts → Check alerts tab → Enter custom data for a prediction

**Prompt:** not public / not found
**Fit (explicit):** Page says it used the EOG challenge datasets, filled missing values and added its own hydrate label, then trained a model to predict hydrates.  *(targeted: EOG Resources)*
**Sponsor tools:** EOG Resources challenge datasets (Training data for the hydrate prediction model, core)
**AI:** Random forest regression on EOG pipe data with a team-added hydrate label; reported R2 around 94 percent. Trained in-house, no LLM.
**Architecture:** Python/Flask API hosts the trained model; HTML/Tailwind/JS front end with Firebase auth; SendGrid for alerts.
**Novelty:** Domain-specific industrial ML on sponsor data rather than a general AI app; team trained its own model.
**Scope:** small · working: Demo video linked; claimed R2 of about 94 percent; about 2k LOC. · polish: Multi-page dashboard; README empty; no tests.
**Claims:** R2 around 94 percent on EOG pipe data | Alerts refresh every second
**Gaps:** No prize text; Video not viewable
Sources: https://devpost.com/software/pipebrains, evidence/hackutd-2024-pipebrains.json

---

### Planet Score
*HackUTD HackUTD 2024 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Best Devpost

**What it is:** Chrome extension that estimates the carbon footprint of a product being browsed. It reads the description, infers materials and origin by keywords, gets per-euro emission factors from OpenLCA/Exiobase, and multiplies by price.
**Problem / user:** Shoppers who want eco-friendly purchases but cannot tell what is truly sustainable amid greenwashing.

**Features**
- Description parsing — Keyword matching extracts materials and likely production location from product text *[claimed]*
- Emission factor lookup — OpenLCA API with Exiobase gives kg CO2 per EUR per material *[claimed]*
- Price-scaled estimate — Footprint = kg CO2/EUR times unit price *[claimed]*
- Browser extension UI — Shows the estimate while browsing *[claimed]*

**Flow:** Browse a product page → Extension reads the description → Materials and origin inferred → OpenLCA returns factors → Price-scaled footprint displayed

**Prompt:** not public / not found
**Fit (none):** No stated link to the prize; the Devpost writeup itself is the entry. Sustainability framing is the project's own.  *(targeted: Best Devpost)*
**AI:** none
**Architecture:** JavaScript Chrome extension front end with Python backend calling OpenLCA API against Exiobase data.
**Novelty:** Uses spend-based life-cycle factors (per euro) instead of ML guesses; notes Ecoinvent licence cost as limit.
**Scope:** tiny · working: Six screenshots only; no demo or video; repo about 390 LOC. · polish: README is a generic template with TODOs.
**Claims:** Reliable, transparent data (no metrics)
**Gaps:** No prize text for Best Devpost; Screenshots uncaptioned
Sources: https://devpost.com/software/planet-score, evidence/hackutd-2024-planet-score.json

---

### poyo.ed
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Poyo's Prize

**What it is:** Lecture companion built around a Poyo plush keychain with a camera hidden inside. It live-transcribes speech, captures slides, and compiles summaries into exportable notes organized by course.
**Problem / user:** Students, especially auditory learners, who cannot keep up with fast lectures and briefly shown slides.

**Features**
- Live transcription — Speech-to-text of lecture audio shown as searchable text *[claimed]*
- Slide capture — Camera in plush or uploaded images add slides to notes *[shown_working]*
- LLM summaries — Condenses transcript and captures into structured notes *[claimed]*
- Export — Notes as text or PDF *[claimed]*
- Course library — Homepage lists courses with saved lectures; Clerk accounts *[claimed]*

**Flow:** Sign in → Open a course and start a lecture → Camera plush captures slides while speech is transcribed → View live study helper → Compiled notes exported

**Prompt:** not public / not found
**Fit (implied):** Poyo is HackUTD's mascot; the project builds its hardware around a Poyo plush and calls itself the Poyo grand prize winner.  *(targeted: Poyo's Prize)*
**Sponsor tools:** SambaNova Cloud API (Transcription/LLM summaries per page, supporting); Pinata File API (Storing and retrieving visual captures, supporting); Groq (Listed in stack, role not described, unclear)
**AI:** Speech transcription plus an LLM that condenses transcript and captured slides into notes; model not named.
**Architecture:** Next.js/TypeScript front end with SQLite storage, Pinata for images, Clerk auth, SambaNova/Groq for AI; hardware camera in plush streams to the web app.
**Novelty:** Pairs software with a modified plush toy as a hidden slide-capturing camera.
**Scope:** medium · working: README has full template and features; webcam view and live transcription screenshots; about 4k LOC. · polish: Detailed README with badges and structure; no video or live link.
**Claims:** Rated above 279 teams and 1,100 participants for the Poyo grand prize
**Gaps:** No prize text; Transcription engine ambiguous
Sources: https://devpost.com/software/poyovision, evidence/hackutd-2024-poyo-ed.json

---

### Promising Products
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Frontier

**What it is:** Recommendation web app for Frontier internet customers that suggests internet, tech and smart-home products using a hybrid memory- and model-based collaborative-filtering model. The README frames it as a Pinata/Frontier challenge entry helping customers pick and use the right products.
**Problem / user:** Frontier customers who cannot tell which product solves their problem or how to use it, and whom documentation alone does not help.

**Features**
- Product recommendations — Hybrid collaborative-filtering model (Python/pandas) suggests products to a user *[claimed]*
- Smart-home and internet suggestions — Recommends internet, tech and smart-home items for common customer problems *[claimed]*
- User authentication — Supabase handles sign-in and API calls that return ML results *[claimed]*
- Social sharing and more categories — Connections, favorite sharing, feedback, niche categories *[planned]*

**Flow:** Sign in → Receive recommended products → Review suggestions for problem at hand

**Prompt:** not public / not found
**Fit (explicit):** README states the project provides solutions to common problems of Frontier Internet customers by identifying the most suitable product; Frontier challenge text itself is not public.  *(targeted: Frontier)*
**Sponsor tools:** Pinata (Mentioned in README header and docs complaint; no integration described, unclear)
**AI:** Collaborative filtering (memory-based plus model-based hybrid) trained on a cleaned pandas dataset; source dataset not named.
**Architecture:** React/TypeScript/Tailwind front end with Supabase backend calling a Python ML recommender; results returned through API calls.
**Novelty:** Uses a classical recommender rather than an LLM, tied to a telecom sponsor's customer support scenario.
**Scope:** small · working: No demo, video or walkthrough; about 700 LOC. · polish: Readme-gen styled README; three brainstorm screenshots only.
**Gaps:** No Frontier prize text; No demo; Dataset unnamed
Sources: https://devpost.com/software/promising-products, evidence/hackutd-2024-promising-products.json

---

### Ripple Banking
*HackUTD HackUTD 2024 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** General

**What it is:** Pop-up micro-banking platform where small business owners borrow from large banks and then serve their community as local banking points. Consumers find them on a map, apply for loans, and dashboards track loans; ML background checks vet users.
**Problem / user:** Unbanked and underbanked people in rural or underserved areas, plus small business owners willing to act as intermediaries.

**Features**
- Microbank map — Google Maps interface for consumers to find and choose nearby microbanks *[shown_working]*
- Customer dashboard — Locate a banker, apply for a loan, view current and paid-off loans *[shown_working]*
- Merchant lender dashboard — Apply for bank loans, view history, applicants and current loanees *[shown_working]*
- ML background check — Model vets borrowers and lenders for trust and compliance *[claimed]*
- Heat map — ML-driven heat map of data *[claimed]*

**Flow:** Land on landing page → Customer: open dashboard and find a banker on the map → Apply for a loan and see confirmation → Merchant: apply for bank loan and view applicants and loanees

**Prompt:** not public / not found
**Fit (none):** General track has no stated prompt; page frames financial inclusion for the unbanked.  *(targeted: General)*
**AI:** Machine learning model for borrower background checks and a heat map; details not given.
**Architecture:** Flask backend in Python with HTML/CSS/JS front end, Google Maps API, a database, and an ML model.
**Novelty:** Two-sided model where merchants become micro-banks funded by large banks, rather than a single-bank app.
**Scope:** medium · working: Screenshots and a GIF of dashboards; about 6k LOC; no live demo. · polish: README stub; no video.
**Claims:** About 5.6 million US households unbanked as of 2023 (cited)
**Gaps:** ML details unstated; Screenshot count not captured
Sources: https://devpost.com/software/tbd-z4uir2, evidence/hackutd-2024-ripple-banking.json

---

### Roomie (unverified on Devpost)
*HackUTD HackUTD 2024 · dataset: winners · tier: track_winner · evidence C · confidence low*
**Prizes:** Winner General and Hardware Track (per ACM UTD site, year unconfirmed)

**What it is:** Study-space finder for college campuses, per a one-line club listing: students use it to find places to study. Other details, such as how class schedules or hardware are used, are not documented anywhere found.
**Problem / user:** College students who constantly look for a place to study.

**Features**
- Free-room finder — Uses class schedules and occupancy to show unoccupied campus rooms (from prior brief; unverified) *[unclear]*

**Prompt:** not public / not found
**Fit (none):** Listed by ACM UTD as winner of the General and Hardware tracks; no description of the hardware role.  *(targeted: General, Hardware Track)*
**AI:** none
**Architecture:** 
**Novelty:** Not enough information; listed as hardware-track winner but no hardware is described.
**Scope:** small · working: None found; no Devpost or repo located. · polish: Unknown.
**Gaps:** No Devpost page; No repo; Year unconfirmed; Hardware role unknown
Sources: https://website-acmutd.vercel.app/hackutd

---

### TalkTuahBank
*HackUTD HackUTD 2024 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** General; Goldman Sachs

**What it is:** Voice banking assistant used over a plain phone call. Callers speak to a multi-agent LLM that checks balances, moves money and pays bills, with an admin dashboard for managing users and transactions.
**Problem / user:** About 1.7 billion unbanked adults who lack internet, smartphones or nearby branches.

**Features**
- Phone-call banking — Caller speaks commands via Retell AI voice agent; no app or internet needed *[shown_working]*
- Balance, transfer, bill pay — OpenAI Swarm agents route requests to backend banking actions *[shown_working]*
- Multilingual interaction — Understands several languages and dialects *[claimed]*
- Admin dashboard — Next.js dashboard to manage users, watch transactions, support users *[shown_working]*
- Pinata data storage — User and transaction records stored on IPFS via Pinata *[claimed]*
- Fraud detection and education — ML fraud checks, financial education modules *[planned]*

**Flow:** User phones the service → Voice agent understands the request → Swarm agents run balance, transfer or bill action → Reply spoken back → Admin watches users and transactions in dashboard

**Prompt:** not public / not found
**Fit (explicit):** Pages label it as a Goldman Sachs track entry and aim it at unbanked users; the sponsor challenge statement is not public.  *(targeted: General, Goldman Sachs)*
**Sponsor tools:** Pinata (IPFS storage of user data and transaction records, supporting)
**AI:** Retell AI handles speech and call handling; OpenAI Swarm coordinates multiple LLM agents that call banking functions.
**Architecture:** Phone call to Retell voice agent, then Swarm agent orchestration to a backend and Pinata storage; Next.js/Tailwind/shadcn admin dashboard.
**Novelty:** Banking over an ordinary phone line with a multi-agent LLM, aimed at people without smartphones.
**Scope:** medium · working: Live site and 2-minute demo video linked; README describes the working prototype; about 9k LOC. · polish: Polished README with badges; landing page and architecture screenshot.
**Claims:** Overall 1st place and Goldman Sachs winner among 1,100+ hackers | Built in 24 hours
**Gaps:** No Goldman prompt text
Sources: https://devpost.com/software/talktuahbank, evidence/hackutd-2024-talktuahbank.json

---

### The Virtual Fitness Assistant
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Next Step; Interview Cake

**What it is:** Smart-gym concept that watches a user exercise through a camera with OpenCV and MediaPipe and corrects posture live. A companion FlutterFlow mobile app is meant to give workout plans and gamified progress.
**Problem / user:** Gym-goers without a personal trainer who risk poor form and injury and lose motivation.

**Features**
- Real-time posture correction — MediaPipe pose tracking with OpenCV flags bad form and prompts correction *[shown_working]*
- Posture-gated rep counter — Rep count rises only when correct posture is achieved *[shown_working]*
- Exercise support — Squats and tadasana implemented *[claimed]*
- Personalized plans — ML on performance to generate workouts in mobile app *[claimed]*
- Gamified milestones — Rewards for hitting fitness goals *[claimed]*
- Gym equipment connection — Link equipment to the app for live data *[planned]*

**Flow:** Exercise in front of the camera → Posture checked in real time → Interactive correction when form is wrong → Rep count increments when correct → Progress in mobile app

**Prompt:** not public / not found
**Fit (none):** Listed award is from Student Hacks, not HackUTD; the page does not tie the project to either prize text. HackUTD entry listed among eight hackathons.  *(targeted: Next Step; Interview Cake)*
**AI:** MediaPipe pose estimation and OpenCV for posture checks; ML to personalize plans claimed, not detailed.
**Architecture:** Python CV pipeline using camera, MediaPipe and OpenCV; Flutter/FlutterFlow mobile app with optional Firebase.
**Novelty:** Posture-gated rep counting; submitted to eight hackathons.
**Scope:** small · working: Video demo linked and two screenshots show correction and counting; about 1.1k LOC. · polish: HTML-style README with features and install steps.
**Claims:** Awards and recognition from industry experts and investors (no details)
**Gaps:** Prize is likely from another hackathon; Mobile app not described in detail
Sources: https://devpost.com/software/the-virtual-fitness-assistant-rvt8qg, evidence/hackutd-2024-the-virtual-fitness-assistant.json

---

### ToyoTrends
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Toyota

**What it is:** React analytics site for Toyota engineers to look up car statistics, compare cars and manufacturers over time on fuel efficiency and emissions, with an AI chatbot and vehicle images.
**Problem / user:** Toyota engineers who need to see and interpret fuel efficiency and carbon emissions across Toyota and competitor vehicles.

**Features**
- Car statistics lookup — Search a vehicle and view its fuel and emission stats *[shown_working]*
- Car comparison over time — Chart.js comparison of multiple cars across years *[shown_working]*
- Manufacturer comparison — Compare makers over time *[shown_working]*
- AI chatbot — SambaNova API chatbot for navigation and information help *[claimed]*
- Vehicle images — CarsXE API supplies photos *[claimed]*
- Predictive emissions analytics — Forecasts from trends *[planned]*

**Flow:** Intro animation and landing page → Look up a car → Compare cars over time → Compare manufacturers → Ask chatbot for help

**Prompt:** not public / not found
**Fit (explicit):** Page says it is designed for Toyota engineers to interpret fuel efficiency and emissions of Toyota and competitor cars; Toyota challenge text not public.  *(targeted: Toyota)*
**Sponsor tools:** SambaNova API (Chatbot for navigation and information, supporting)
**AI:** SambaNova-hosted LLM chatbot; analytics itself is deterministic data processing.
**Architecture:** React front end with Chart.js, local JSON vehicle data under public/data, Python filter scripts, CarsXE for images, SambaNova chatbot.
**Novelty:** Mostly a data-visualization tool for a sponsor persona; AI limited to a chatbot.
**Scope:** small · working: Five screenshots and video embedded; local-run instructions; repo not located. · polish: Intro animation, designed UI.
**Claims:** Built in under 24 hours
**Gaps:** No repo; No prize text; Data source unnamed
Sources: https://devpost.com/software/toyota-car-analytics-app

---

### Vestique
*HackUTD HackUTD 2024 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Samba Nova; [MLH] Best Use of Streamlit

**What it is:** Streamlit wardrobe assistant that classifies clothing from photos using vision LLMs, tracks what you wear, emails you about items left unworn, and can list unwanted pieces for sale.
**Problem / user:** Shoppers who spend heavily on clothes but wear little of them, creating waste.

**Features**
- Clothing recognition — Llama-3.2-11B vision model classifies uploaded clothing photos *[claimed]*
- Wear tracking — Daily fit checks log which items are worn most and least *[claimed]*
- Unworn reminders — Brevo emails alert after set days without wear *[claimed]*
- Auto-listing for sale — Marketplace option for unwanted items *[claimed]*
- Style advice — SambaFit AI agent using Llama 3.1 70B for recommendations *[claimed]*

**Flow:** Upload clothing photos → Items classified into wardrobe → Log daily fit check → Get email about unworn items → Optionally list item for sale

**Prompt:** not public / not found
**Fit (implied):** Uses SambaNova-served Llama models and a Streamlit UI; the MLH Streamlit prize is for building a Python web app with Streamlit.  *(targeted: Samba Nova, [MLH] Best Use of Streamlit)*
**Sponsor tools:** SambaNova (Llama 3.1 70B and 3.2 vision inference, core); Streamlit (Entire UI, core); Brevo (Email notifications, supporting)
**AI:** Llama-3.2-11B-Vision classifies garments from photos; Llama-3.1-70B via SambaNova gives style recommendations.
**Architecture:** Streamlit Python app calling SambaNova APIs for vision and text, Brevo for email, local wear logs.
**Novelty:** Links wear-frequency tracking to resale listing as a waste-reduction loop.
**Scope:** small · working: Nine screenshots; setup README with env keys; about 3.9k LOC. · polish: README with features and install steps; no video or demo.
**Claims:** Users wear 40 percent more and save $1,200 yearly (marketing, no data)
**Gaps:** No demo
Sources: https://devpost.com/software/vestique, evidence/hackutd-2024-vestique.json

---

### What's The Move?
*HackUTD HackUTD 2024 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Most Relatable

**What it is:** Web app that finds a meeting spot for a friend group by computing an inverse-weighted midpoint of everyone's locations, then searching Google Maps for places near it.
**Problem / user:** Friend groups scattered across Dallas-Fort Worth who struggle to pick a fair meeting place without someone driving much farther.

**Features**
- Weighted midpoint — Custom Midpoint API weights locations so drives are roughly proportional *[shown_working]*
- Address geocoding — Google Maps geocoding turns addresses into coordinates *[claimed]*
- Nearby place search — Query for a chosen kind of place near the midpoint *[shown_working]*
- Any group size — Works with arbitrary number of friends *[claimed]*
- Group voting and booking — Voting, personalization, availability *[planned]*

**Flow:** Enter your location and friends' locations → Choose type of place → App computes midpoint → Review list of nearby spots

**Prompt:** not public / not found
**Fit (implied):** Solves a common everyday problem, which fits the relatability theme by inference; no prize text found.  *(targeted: Most Relatable)*
**Sponsor tools:** Pinata (Media upload API; errors noted, role minor, token)
**AI:** none
**Architecture:** React front end hosted on Firebase, Express on Firebase Functions, Midpoint API, Google Maps geocoding and places.
**Novelty:** Uses a weighted formula instead of a plain centroid; includes Figma design link.
**Scope:** small · working: Live Firebase demo URL listed; repo has tests and CI. · polish: README with figma, inspiration, tests present; no screenshots on Devpost.
**Claims:** 69 percent find coordinating plans difficult (cited Eventbrite survey)
**Gaps:** No video; Most Relatable prize text not found
Sources: https://devpost.com/software/what-s-the-move-4z5sih, evidence/hackutd-2024-what-s-the-move.json

---

