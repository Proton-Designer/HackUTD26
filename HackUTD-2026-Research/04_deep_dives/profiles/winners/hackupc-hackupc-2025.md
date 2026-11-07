# HackUPC — HackUPC 2025 (20 projects)

### CARmen
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [2nd] Seat - Know Your Cupra [2nd]

**What it is:** A web platform for prospective Cupra Tavascan buyers: a manual-grounded RAG chatbot, an image upload and region-select flow that explains car parts, object detection with labels, and an interactive 3D interior in a Cupra-styled interface.
**Problem / user:** Prospective and new Cupra Tavascan owners who want to know the car before it is theirs; answers drawn from the official manual rather than free generation.

**Features**
- Manual chatbot — Query expansion, page retrieval from Gemini-embedded manual chunks, chunk re-ranking and nearby images, then an LLM answers grounded text with page images. *[claimed]*
- Image and region queries — User selects an area of an uploaded photo; Gemini describes it, retrieval and image-similarity re-ranking find matching manual content. *[claimed]*
- Object detection — Automatically detects and labels car parts in uploaded images. *[claimed]*
- 3D interior simulation — Interactive 3D view of the Tavascan interior in the browser. *[claimed]*
- Manual preprocessing — PDF manual split into pages and chunks with section titles, page numbers and images, then indexed. *[claimed]*
- Brand-aligned UI — Clean responsive interface imitating Cupra visual identity. *[claimed]*

**Flow:** Open the web app → Ask a natural-language question in the chatbot or upload a car photo → Select a region of the image → Receive grounded answer with manual pages and images → Explore the interior in the 3D view

**Prompt:** Seat 'Know Your Cupra': help customers learn the vehicle's features between ordering and delivery, ideally by gamifying the user manual in a friendly way.
**Fit (explicit):** README says it was built for the SEAT challenge; uses RAG over the manual plus image Q&A and 3D interior to teach the car; no gamification described.  *(targeted: Seat - Know Your Cupra (2nd))*
**AI:** Gemini embeddings and vision for a multimodal RAG over the manual with query expansion and re-ranking; LLM generates grounded answers; object detection labels parts.
**Architecture:** Web frontend with Canvas region cropping sends base64 images to a Python backend that does retrieval over a vector store of manual text and images and calls the LLM.
**Novelty:** Multimodal retrieval that accepts a cropped image region and returns matching manual pages and images; 3D interior alongside chat.
**Scope:** medium · working: Repo about 17.8k LOC with tests and README describing pipeline; Devpost shows four screenshots; no video or live link. · polish: Branded UI screenshots; no Docker or CI.
**Claims:** Answers grounded in retrieved manual content rather than free generation
**Gaps:** Devpost does not name LLM, vector DB or 3D engine; README says Gemini embeddings; README setup not read beyond 2500 chars in my pass; Devpost lists no gamification
Sources: https://devpost.com/software/carmen, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-carmen.json

---

### CUPRA-App
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [1st] Seat - Know Your Cupra [1st]

**What it is:** A React Native (Expo) mobile and web app that gamifies learning the Cupra Tavascan with missions, levels, points, daily tasks, interest points, a glossary and a searchable pocket manual, backed by Express and MongoDB.
**Problem / user:** New or prospective Cupra Tavascan owners waiting for delivery who need to learn the car's features and want one place for its information.

**Features**
- Missions and levels — Users complete tasks tied to car features to earn points and keep a daily engagement streak. *[claimed]*
- Learning games and rewards — Gamified lessons derived from the user manual with reward incentives. *[claimed]*
- Interactive points of interest — Explore vehicle interest points to see specs and features. *[claimed]*
- Pocket manual search — Advanced search across features, glossary terms and notices. *[claimed]*
- Glossary — Complete list of technical terms. *[claimed]*
- Profile and progress — Shows stats and progress; JWT-authenticated backend stores users. *[claimed]*
- Themed UI — Light and dark themes styled to look like the CUPRA brand. *[claimed]*

**Flow:** Open the app on mobile or web → Pick up daily tasks and missions → Complete learning games to earn points → Explore points of interest on the car → Search the pocket manual or glossary → Check profile progress

**Prompt:** Seat 'Know Your Cupra': help customers learn their vehicle's features between ordering and delivery, ideally by gamifying the user manual in a friendly way.
**Fit (explicit):** README quotes the challenge and answers with missions, levels, points, daily features and a manual search, directly gamifying the manual.  *(targeted: Seat - Know Your Cupra (1st))*
**AI:** none
**Architecture:** Expo Router React Native client talks to a Node/Express API using JWT auth, MongoDB via Mongoose, with Redis rate limiting and Winston logging in backend dependencies.
**Novelty:** Direct gamification of the manual with streaks and levels; no AI, unlike the other Cupra entries.
**Scope:** medium · working: About 10.8k LOC repo with tests; README gives install steps; Devpost has no screenshots described or video. · polish: Theme support and brand styling; backend hardening deps (rate limit, validation).
**Claims:** Customer knows the car inside and out before driving it
**Gaps:** README (Spanish) says built during HackUPC 2024 while Devpost and challenge show 2025; Devpost spells model Tabascan and Tavascan; Screenshots not counted
Sources: https://devpost.com/software/cupra-app, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-cupra-app.json

---

### DataCenter-DeCoder
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [2nd] Siemens Energy - Data Center Designer [2nd]

**What it is:** An interactive data center planner with drag-and-drop module placement on a ReactFlow canvas, live constraint checks, and Python backend optimization that selects and distributes modules from CSV-defined equipment and data center types.
**Problem / user:** Engineers designing data centers who juggle power, cooling, space and cost with disconnected tools and manual calculation.

**Features**
- Drag-and-drop placement — Users drag modules like transformers, water supplies and processors onto a canvas (dnd-kit, ReactFlow). *[shown_working]*
- Real-time constraint validation — Resource inputs, outputs, space and price are checked as the layout changes and violations shown visually. *[claimed]*
- Resource flow modeling — Modules declare resource inputs and outputs in Modules.csv so flows between components are modeled. *[claimed]*
- Constraint-based optimization — Backend algorithms choose and distribute modules to meet a data center type's limits and minimize or maximize objectives. *[claimed]*
- Multiple data center types — Server Square, Dense Storage and Supercomputer specs loaded from Data_Center_Spec.csv. *[claimed]*
- Trade-off visualization — Shows design trade-offs between cost, power and space. *[claimed]*
- 3D view, thermal model, ML suggestions — Listed as future work with vendor catalog integration. *[planned]*

**Flow:** Choose a data center type → Drag modules onto the canvas → See constraint status update → Run the optimizer to auto-select modules → Review trade-offs

**Prompt:** Siemens Energy 'Data Center Designer': build a tool for designing made-to-order data centers where users explore equipment and services for networking, cooling, power, processing and storage.
**Fit (explicit):** Builds the requested designer with module catalog, constraint checking and optimization; README says developed with Siemens Energy.  *(targeted: Siemens Energy - Data Center Designer (2nd))*
**Sponsor tools:** Siemens Energy module and spec CSV data (Defines module resources, costs and data center type constraints, core)
**AI:** none
**Architecture:** React/TypeScript/Vite frontend with Material-UI and ReactFlow; FastAPI backend with optimization algorithms and MongoDB storage of module and constraint data.
**Novelty:** Combines a visual builder with a constraint solver over the sponsor's resource-flow data model.
**Scope:** medium · working: About 12.5k LOC repo; Devpost has three screenshots; no video or live demo. · polish: README has data format docs and install; no tests, Docker or CI.
**Claims:** Optimizes resources and maximizes performance of designs
**Gaps:** Optimizer algorithm not described beyond constraint-based; Working status of validation inferred from README and Devpost
Sources: https://devpost.com/software/datacenter-decoder, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-datacenter-decoder.json

---

### ECHOLOOK
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [1st] InditexTech - Visual Search [1st]

**What it is:** A mobile-first virtual fitting room: photograph yourself, segment garments with U2-Net, tap a garment for Inditex Visual Search matches or speak a request, then try suggestions on your photo with Fashn.ai and keep a personal history.
**Problem / user:** Online fashion shoppers, especially of Inditex brands, who miss the closeness of trying clothes on in a store.

**Features**
- Clothing segmentation — U2-Net mini model finds garments in the photo and marks centroids to tap. *[shown_working]*
- Visual search by tap — Clicking a centroid queries the Inditex Visual Search API for similar garments, improved by segmentation. *[shown_working]*
- Voice search — Whisper transcribes speech in any language; Gemini turns it into a structured query for Inditex Product Search. *[shown_working]*
- Virtual try-on — One tap sends suggested garments plus user photo to Fashn.ai to blend. *[shown_working]*
- Accounts and history — JWT sign-up/login; photos, masks and suggestions saved in MongoDB and S3. *[claimed]*
- Favorites and recommendations — Planned with fine-tuned speech-to-query models. *[planned]*

**Flow:** Sign up or log in → Capture or upload a photo → Segmentation shows garments and centroids → Tap one or record a voice query → Review Inditex suggestions → Tap to try on virtually → History saves everything

**Prompt:** InditexTech 'Visual Search': web or mobile app using Inditex's Visual Search API to identify and locate similar catalog clothing from real-time photos or screenshots, focusing on item identification.
**Fit (explicit):** Segmentation plus tap-to-search uses the Visual Search API on photos; adds voice product search and try-on beyond the brief.  *(targeted: InditexTech - Visual Search (1st))*
**Sponsor tools:** Inditex Visual Search API (Tap a garment to find similar catalog items, core); Inditex Product Search API (Structured voice query results, core)
**AI:** U2-Net mini segmentation in a FastAPI microservice; Whisper-small plus Gemini Pro parse voice into structured queries; Fashn.ai generates virtual try-on.
**Architecture:** Quasar/Vue client, Node/Express server with MongoDB and S3, Dockerized Python AI microservices for segmentation and whisper parsing, external Inditex and Fashn.ai APIs.
**Novelty:** Chains segmentation, two Inditex APIs, multilingual voice and generative try-on into one flow; AI services modular as independent APIs.
**Scope:** small · working: README gives install and env keys; first end-to-end demo claimed; about 4.5k LOC; Cypress deps; no video. · polish: Logo, README tables, i18n in client; no CI.
**Claims:** Segmentation boosts precision of Visual Search (no metric) | First end-to-end photo/audio to fitting-room demo
**Gaps:** Screenshot count taken from listed gallery screens; Evidence flags no tests though Cypress listed as dep
Sources: https://devpost.com/software/echolook, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-echolook.json

---

### Feel the CUPRA
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [3rd] Seat - Know Your Cupra [3rd]

**What it is:** A Unity digital twin of the Cupra Tavascan with a welcome animation, six guided feature tours, a voice assistant that answers from the manual via RAG, a physics acceleration/braking simulator, and an EEG headband mode that drives the simulated car by focus.
**Problem / user:** Prospective and new Tavascan buyers who want to learn the car's features before delivery without reading the manual.

**Features**
- 3D digital twin with tours — Real-time animated car welcome, a Know more button and a Learn about menu with six visual and voice-guided tours. *[shown_working]*
- Voice manual assistant — Press a button, speak; audio goes to Gemini 2.0 Flash with RAG over manual embeddings and returns audio plus text. *[shown_working]*
- Physics driving simulator — Acceleration and braking modeled with kinematic equations from real power, torque, curves and mass values. *[shown_working]*
- EEG mind-controlled driving — Muse headband signals, FFT-cleaned, classified focused vs relaxed by a Random Forest via Flask and sent to Unity to control speed. *[shown_working]*
- Docker for assistant — Containerized assistant to fix Linux-to-Windows library incompatibilities. *[shown_working]*

**Flow:** Launch the app and watch the Tavascan welcome animation → Press Know more to enter the feature scene → Pick one of six guided tours → Try acceleration and braking in the simulator → Press the assistant button and ask by voice → Optionally wear the Muse headband to control the car by focus

**Prompt:** Seat 'Know Your Cupra': help customers learn their vehicle's features between ordering and delivery, ideally by gamifying the user manual in a friendly way.
**Fit (explicit):** README says it implements the challenge: a digital twin teaching features through tours and a voice assistant over the manual, plus an EEG driving demo as a showpiece.  *(targeted: Seat - Know Your Cupra (3rd))*
**AI:** Gemini 2.0 Flash voice assistant with embeddings RAG over the official manual; separate Random Forest classifier trained on hand-labeled Muse EEG samples for focused vs relaxed.
**Architecture:** Unity/C# app; Flask voice assistant (Docker) calling Gemini; FastAPI/Flask layer relays Muse EEG classifications from Python to Unity.
**Novelty:** Adds a brain-signal driving simulator and physics-based vehicle model to a manual-learning brief; hardware EEG headband used in a car-manual challenge.
**Scope:** small · working: README has demo and screenshots at end; Devpost has nine screenshots and a video; repo about 1k LOC excluding Unity assets. · polish: Logos, authors, tech table and Docker version; no tests or CI.
**Claims:** Customers learn features without reading the manual | Describes simulator as unprecedented and realistic (no metrics)
**Gaps:** Which EEG state maps to accelerate or brake is unspecified; No classifier accuracy; README truncated at 2800 chars in my pass; Unity assets excluded from LOC
Sources: https://devpost.com/software/feel-the-cupra, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-feel-the-cupra.json

---

### FlowCore
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [1st] Siemens Energy - Data Center Designer [1st]

**What it is:** A drag-and-drop data center designer on a React Flow canvas with an AI auto-complete button, a SAT-solver layout optimizer, an isometric failure simulator and a live dashboard, communicating over MQTT and WebSockets.
**Problem / user:** Engineers and energy managers designing sustainable data centers, where design is costly, complex and disconnected from real-time environmental factors.

**Features**
- Modular workflow builder — Drag racks, power units, cooling, UPS and networking blocks; resource needs adjust with budget, geolocation and target capacity. *[shown_working]*
- AI Magic Button — Analyzes a partial design and adds missing components to balance power, cooling, redundancy, compliance and budget. *[claimed]*
- SAT-solver optimization — Python SAT solver finds a spatial layout considering noise, solar capacity, cooling efficiency and space use. *[shown_working]*
- Isometric failure simulator — Simulates overheating, breakdowns and blackouts while the autonomous system reacts in real time. *[shown_working]*
- Real-time dashboard — Shows energy, cooling demand, uptime and SLA, renewable ratio and failure probability, fed by MQTT. *[shown_working]*
- Live data sync — MQTT (Mosquitto), WebSockets and REST keep subsystems consistent; MongoDB stores data. *[claimed]*

**Flow:** Create a data center and place blocks in the workflow builder → Press Magic Button to auto-complete → Run the optimization engine for a layout → Run the isometric simulation and inject failures → Watch metrics on the dashboard

**Prompt:** Siemens Energy 'Data Center Designer': build a tool for designing made-to-order data centers where users explore equipment and services for networking, cooling, power, processing and storage.
**Fit (explicit):** Page is titled for the Datacenter Designer challenge; delivers a designer with auto-completion, optimization and simulation beyond the basic placement brief.  *(targeted: Siemens Energy - Data Center Designer (1st))*
**Sponsor tools:** Siemens Energy challenge data (Not stated on page, unclear)
**AI:** A Gemini-tagged assistant adds missing components to a design; a PySAT solver (not ML) optimizes layouts. Details of the model use are not described.
**Architecture:** Next.js/React Flow frontend; FastAPI backend with MongoDB; Mosquitto MQTT and WebSocket real-time channel; PySAT solver; Docker Compose.
**Novelty:** Adds SAT-based layout, failure simulation and live telemetry to a designer brief, with an LP model screenshot.
**Scope:** medium · working: Devpost shows six screenshots (dashboard, workflow, simulation, LP model, MQTT); backend repo about 3.3k LOC, frontend repo not inspected. · polish: Docker Compose and multi-protocol backend; backend README is empty; no video.
**Claims:** Built in 36 hours | Working end-to-end simulation and optimization system
**Gaps:** Backend README is just a title; frontend repo LleidaHackers/frontend not read; How Gemini is used is not described; No performance numbers
Sources: https://devpost.com/software/flowcore, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-flowcore.json (backend repo, README empty)

---

### Graf-Anna
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [1st] Grafana - Green Grafana [1st]

**What it is:** A public Grafana dashboard telling a story about industrial-era CO2, temperature rise, natural disasters, deforestation and life expectancy, with country comparisons, geomaps, stat panels and explanatory text, tied to SDGs 9, 12 and 13.
**Problem / user:** General audience for climate education wanting the historical context and drivers of climate change; no specific user named.

**Features**
- Historical trend panels — Time series since about 1850 for global CO2 emissions, temperature rise and natural disaster counts. *[shown_working]*
- National comparison — CO2 per capita and life expectancy trends for the US, China, Canada and Spain. *[shown_working]*
- Deforestation emissions — CO2 from deforestation broken down by commodity such as beef, oilseeds and cereals for key nations. *[shown_working]*
- Global footprint maps — Geomap panels of emission hotspots and land use (industry vs agriculture). *[shown_working]*
- Key metric stats and SDG imagery — Stat panels such as temperature anomaly and disaster counts, plus text, Polystat/image panels and SDG logos. *[shown_working]*
- Custom app plugin, LLM insights, dynamic images — Planned plugin built with Scenes was abandoned for time; LLM insights not implemented. *[planned]*

**Flow:** Open the public Grafana dashboard → Scroll rows from historical trends to national comparisons → Review deforestation breakdowns → Explore global maps and read explanatory text

**Prompt:** Grafana 'Green Grafana': use Grafana to visualize open data on UN SDGs, focus on environmental goals; dashboards, an app plugin, or both; suggested sources UN SDG Data, World Bank, Our World in Data.
**Fit (explicit):** Dashboard built from Our World in Data and similar open data on SDG-linked climate topics, using Infinity plugin; dropped the custom plugin option.  *(targeted: Grafana - Green Grafana (1st))*
**Sponsor tools:** Grafana (dashboards, Infinity plugin) (All visualization, CSV and API ingestion, core)
**AI:** none
**Architecture:** Grafana dashboard using the Infinity data source to load CSV and API data from Our World in Data and OpenAQ, arranged in rows of time series, bar, geomap, stat and text panels.
**Novelty:** Narrative-driven storytelling dashboard linking emissions, consumption, disasters and life expectancy rather than a single metric view.
**Scope:** small · working: Public Grafana dashboard linked on Devpost; no repo, so contents not inspected. · polish: Structured rows, SDG imagery and text panels; no video.
**Claims:** Shows interconnection of industry, consumption, climate and health
**Gaps:** No repository linked; Dashboard itself not opened; Page says live data used but also lists live data as next step; Exact deforestation data source uncertain per page
Sources: https://devpost.com/software/graf-anna, https://hackupc-2025.devpost.com/

---

### IndiSearch
*HackUPC HackUPC 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** HackUPC 2nd place [2nd]

**What it is:** A Chrome extension that finds people and clothing in whatever video or page you watch, lets you hover or click an item to search the Inditex catalog for similar garments with purchase links, and offers a diffusion-based virtual try-on.
**Problem / user:** Shoppers who see an outfit on Netflix, X, YouTube or an ad and cannot find where to buy it.

**Features**
- On-screen clothing detection — YOLO detects people and draws bounding boxes over captured screenshots; Mediapipe and ultralytics appear in backend dependencies. *[shown_working]*
- Inditex similar-item search — Hover or click a highlighted item; backend queries the Inditex API with a public screenshot URL and lists matches. *[shown_working]*
- Purchase links and product images — IndiTech API gives names, IDs and links; SerpApi scraping fetches product images. *[shown_working]*
- Temporary public image URLs — Custom method hosts screenshots briefly because the Inditex API needs public URLs. *[claimed]*
- Virtual try-on — Try-On Diffusion endpoint on RapidAPI renders the person wearing the chosen garment, with a loading state. *[shown_working]*
- Mobile support, basket integration — Planned improvements. *[planned]*

**Flow:** Browse a site like Netflix, X or YouTube → Extension detects people and clothing → Hover or click a highlighted item → See similar Inditex items with buy links → Optionally run virtual try-on and see before and after

**Prompt:** InditexTech 'Visual Search': web or mobile app using Inditex's Visual Search API to identify and locate similar catalog clothing from real-time photos or screenshots, focusing on item identification.
**Fit (implied):** Overall prize, but the build is an Inditex visual search from screenshots, matching the sponsor challenge, with a try-on extra.  *(targeted: HackUPC 2nd place)*
**Sponsor tools:** Inditex API (IndiTech) (Similar-item search and purchase links, core)
**AI:** YOLO person detection; Inditex visual similarity search; hosted Try-On Diffusion API for garment rendering.
**Architecture:** Chrome extension (JavaScript) captures screens and calls a FastAPI backend that runs YOLO, calls Inditex and SerpApi, and hosts temporary image URLs.
**Novelty:** Brings shopping into video watching via a browser extension, with detection overlay and try-on.
**Scope:** small · working: Four screenshots show detection, search and try-on; repo about 1.2k LOC; no video. · polish: Repo README is a generic screenshot-extension stub; no tests or CI.
**Claims:** All planned features completed within 36 hours
**Gaps:** README describes a generic screenshot-capture extension and server that saves uploads; Devpost describes full detection and search; both recorded; Prize is general 2nd place not the sponsor track; track fit inferred
Sources: https://devpost.com/software/indisearch-nc7k59, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-indisearch.json

---

### Inditex clothe detector
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [3rd] InditexTech - Visual Search [3rd]

**What it is:** A Chrome extension: capture a screenshot of a garment on any shop page, send it through a small Python server to the Inditex visual search API, and see similar Inditex products with name, price and buy link.
**Problem / user:** Online shoppers who see a garment on one site and want similar Zara, Massimo Dutti or Pull&Bear items without repeated searching.

**Features**
- Screenshot capture — Extension lets the user select a product region on the page and grabs the image. *[shown_working]*
- Similar product search — Python Flask server forwards the image to the Inditex-provided API and returns similar items. *[shown_working]*
- Result display — Shows product name, price and purchase link in the extension UI built with React and Vite. *[claimed]*
- API error handling — Handles failures of external API responses; described as a lesson. *[claimed]*
- Mobile version and filters — Planned color, fabric and type filters and mobile capture. *[planned]*

**Flow:** Install extension in Chrome and start the Python server → Open a page showing a garment → Capture a screenshot with the extension → Server queries Inditex API → See similar Inditex garments with links

**Prompt:** InditexTech 'Visual Search': web or mobile app using Inditex's Visual Search API to identify and locate similar catalog clothing from real-time photos or screenshots, focusing on item identification.
**Fit (explicit):** README says it was built for the Inditex challenge: screenshot a product and show similar Inditex items.  *(targeted: InditexTech - Visual Search (3rd))*
**Sponsor tools:** Inditex Visual Search API (Finding similar products from a screenshot, core)
**AI:** No model of its own; relies on Inditex's visual similarity API.
**Architecture:** Chrome extension frontend posts images to a Flask server that calls the Inditex API and relays results.
**Novelty:** Minimal and direct implementation of the sponsor brief; screenshot-based extension.
**Scope:** tiny · working: README gives install and run steps; about 1.2k LOC; no screenshots or video on Devpost. · polish: README in Spanish says it tied for 2nd/3rd; minimal UI; some tests present.
**Claims:** README says 3rd place tied with 2nd in the Inditex challenge
**Gaps:** File count inflated by committed node_modules; Devpost says Flask backend; README says python server.py; No metrics
Sources: https://devpost.com/software/inditex-clothe-detector, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-inditex-clothe-detector.json

---

### Inditex Visual Search
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [2nd] InditexTech - Visual Search [2nd]

**What it is:** A Next.js web app, deployed on Vercel, that finds similar Inditex clothing from an uploaded image, a drag-and-drop file, a live camera capture or an image URL, with server-side calls to the Inditex visual search API.
**Problem / user:** Shoppers who want items similar to a photo of clothing; team also wanted to experiment with image preprocessing to improve accuracy.

**Features**
- Multiple image inputs — File picker or drag-and-drop, camera capture in a video-call-style view, or pasting an image URL, with a preview before searching. *[shown_working]*
- Visual search results — Image is sent through server-side calls to Inditex's visual search; similar items are listed as suggestions. *[shown_working]*
- Product image scraping — Cheerio (and Puppeteer locally) scrape product images; Zara's anti-bot protection blocked this in production. *[claimed]*
- Token refresh and secure calls — Automatic OAuth token refresh and server rendering keep API credentials off the client. *[claimed]*
- Info screen and user guide — Landing, about page and in-app guide styled like Inditex platforms. *[claimed]*
- Try-on, item selection, store availability, accounts — Listed as next steps. *[planned]*

**Flow:** Land on the main screen → Upload, drag in, capture or paste a link to a photo → Preview the image → Run the search → Browse similar Inditex suggestions

**Prompt:** InditexTech 'Visual Search': web or mobile app using Inditex's Visual Search API to identify and locate similar catalog clothing from real-time photos or screenshots, focusing on item identification.
**Fit (explicit):** Directly implements the brief: photo or camera input to Inditex Visual Search, returning similar catalog items.  *(targeted: InditexTech - Visual Search (2nd))*
**Sponsor tools:** Inditex Visual Search API (Core similar-item lookup with OAuth, core)
**AI:** No own model; relies on the Inditex visual search model through API. Team's own experiments centered on image preprocessing ideas.
**Architecture:** Next.js 15 app with server-side API routes handling Inditex OAuth and search, cheerio scraping for images, Tailwind/Radix UI; originally React plus FastAPI before migration.
**Novelty:** Straightforward implementation of the brief with three input modes and a live deployment; notable for documented migration and production scraping limits.
**Scope:** small · working: Live Vercel link on Devpost; README with setup and usage; about 2.4k LOC. · polish: Responsive UI, guide screens; README claims tests though none flagged; no video.
**Claims:** Functional MVP with polished UI built under time constraints
**Gaps:** README is Spanish and mentions a test command, but evidence shows no tests; Screenshot count not captured; Production scraping blocked by Zara per Devpost
Sources: https://devpost.com/software/inditex-visual-search, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-inditex-visual-search.json

---

### MMG
*HackUPC HackUPC 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** HackUPC 1st place [1st]

**What it is:** A blackout-resilient flight information system: Raspberry Pi clusters host their own Wi-Fi access points and a server, Android phones bridge subnets over Bluetooth and Wi-Fi, and passengers keep getting flight updates without mains power or internet. Includes an admin portal.
**Problem / user:** Airport passengers who lose flight delay and change information during a power or internet outage, inspired by the 2025 Iberian blackout.

**Features**
- Offline flight updates — Phones receive delay and change data from local cluster servers with no external internet. *[shown_working]*
- Self-hosted access points — Raspberry Pis configure their own Wi-Fi access point (hostapd, systemd) so devices connect without outside infrastructure. *[shown_working]*
- Multi-subnet bridging — Smartphones use Bluetooth and Wi-Fi at once to link several subnets, routing traffic between clusters and reaching the main server. *[shown_working]*
- Energy-efficient design — Optimized to keep battery use low during emergencies. *[claimed]*
- Android app — Kotlin app using Room for local storage shows flight data. *[shown_working]*
- Admin dashboard — React portal over a Node/Express and SQLite backend to manage flight data, shown in screenshots. *[shown_working]*
- Failure resilience — Internal communication continues when parts of the network drop. *[claimed]*

**Flow:** Passenger's phone joins a nearby Raspberry Pi access point → App syncs flight updates stored locally → Phones bridging two clusters pass data across subnets → Admin updates flight info through the portal → Updates reach devices even during blackout

**Prompt:** Vueling 'Watch out, Blackout!': minimal app for travelers about to fly sharing critical flight info during a blackout over an ad hoc network, prioritizing critical data, low battery, bonus for gamification.
**Fit (explicit):** README credits the Vueling challenge: ad hoc Pi and phone mesh delivering flight info offline with low battery use; no gamification mentioned.  *(targeted: HackUPC 1st place, Vueling challenge)*
**AI:** none
**Architecture:** Raspberry Pi clusters act as access points and local servers; Android phones bridge subnets via Bluetooth and Wi-Fi; main Node/Express server with SQLite and a React admin portal.
**Novelty:** Real networking hardware (Pi clusters, hostapd, phone bridging) rather than a simulated app; overall winner with an infrastructure focus.
**Scope:** medium · working: Demo video and screenshots of Pi hardware and APK; repo about 6.9k LOC with tests; very large file count suggests committed artifacts. · polish: Branded README, logo and admin portal; no CI or Docker.
**Claims:** Network convergence, routing and server access achieved | Works through power outages and connectivity loss
**Gaps:** Devpost lists ChatGPT and Copilot as tools without saying how; No quantified battery or range data; Hardware count and cluster size not stated
Sources: https://devpost.com/software/mmg, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-mmg.json

---

### Peaceful Protest Tracker: Headlines vs Reality
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [2nd] Grafana - Green Grafana [2nd]

**What it is:** A public Grafana dashboard fed by a scrape-analyze-store pipeline: Serbian independent and pro-government news is scraped, Gemini extracts protest location and sentiment, and Grafana shows a protest map, sentiment, keyword comparisons and a schedule.
**Problem / user:** People trying to understand Serbian student protests after the Novi Sad canopy collapse, when media outlets told conflicting stories.

**Features**
- Live protest map — Geomap panel of reported protest locations extracted from articles, updated every couple of hours. *[shown_working]*
- Sentiment analysis — Gemini 2.5 Flash returns article sentiment on how students and protesters are portrayed. *[shown_working]*
- Keyword comparison — Compares terms like justice against propaganda language across media spheres. *[shown_working]*
- Headlines vs reality charts — Time series, stat and table panels contrast narratives and show a protest schedule. *[shown_working]*
- Automated scraping pipeline — Python BeautifulSoup scrapers run via cron through a Spring Boot coordinator that stores cleaned JSON in MongoDB Atlas. *[shown_working]*
- Structured Gemini extraction — Custom prompts return JSON: whether the article covers a protest, where, who is mentioned and sentiment. *[shown_working]*

**Flow:** Open the public Grafana dashboard → View protest locations on the map → Compare sentiment and keywords across outlets → Read the headlines vs reality panels and schedule table

**Prompt:** Grafana 'Green Grafana': use Grafana to visualize open data on UN SDGs, focus on environmental goals; dashboards, an app plugin, or both; suggested sources UN SDG Data, World Bank, Our World in Data.
**Fit (explicit):** Grafana dashboard framed on UN SDG 16 (peaceful societies) rather than an environmental goal; data is scraped news, not the suggested open datasets.  *(targeted: Grafana - Green Grafana (2nd))*
**Sponsor tools:** Grafana (Public dashboard with geomap, time series, stat and table panels, core)
**AI:** Gemini 2.5 Flash with custom prompts converts article text to structured JSON (protest flag, location, people, sentiment) via a Python script called by Spring Boot.
**Architecture:** Python scrapers to Gemini to Spring Boot backend (cron, REST) to MongoDB Atlas to Grafana dashboard.
**Novelty:** Uses an LLM-driven news pipeline as Grafana data source and compares state-aligned and independent media coverage of a live political event.
**Scope:** small · working: Public Grafana dashboard link and YouTube preview; repo about 3.3k LOC with tests. · polish: Detailed README with architecture and setup; no Docker or CI.
**Claims:** Largely self-maintaining as long as source site formats remain unchanged
**Gaps:** Devpost lists no video while README links a YouTube preview; No article counts or sentiment accuracy; Devpost did not show screenshot count
Sources: https://devpost.com/software/peaceful-protest-tracker-headlines-vs-reality, https://hackupc-2025.devpost.com/, evidence/hackupc-hackupc-2025-peaceful-protest-tracker-headlines-vs-reality.json

---

### Rack Attack
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence low*
**Prizes:** [3rd] Siemens Energy - Data Center Designer [3rd]

**What it is:** A web tool for designing data centers from a set of supplied parts, showing the build in 3D and tracking requirements live while giving recommendations for desirable qualities. Built for the Siemens Energy data center challenge.
**Problem / user:** Customers or sales engineers who need a data center configured to custom requests that template solutions do not fit; the Devpost page does not state the problem explicitly.

**Features**
- Assemble data center infrastructure from provided parts — User composes a design from the challenge's component set in a dynamic interface for custom requests. *[claimed]*
- Live view of all requirements — Requirement status is shown continuously as the design changes. *[claimed]*
- Recommendations toward desirable qualities — Suggests changes based on target qualities; Gemini is listed in the stack, role not described. *[claimed]*
- 3D rendering of the design — Three.js scene rendered in the browser from the chosen configuration. *[claimed]*

**Flow:** Open the web app → Pick parts to assemble the data center → Watch requirement tracker and 3D view update → Act on recommendations to reach desired qualities

**Prompt:** Build a designer for a made-to-order data center where clients explore equipment and service options across networking, cooling, power and processing against external loads.
**Fit (explicit):** Page says it was built from a Siemens challenge that allowed flexible app design; it lets a user configure a data center from provided parts with live requirement tracking.  *(targeted: Siemens Energy - Data Center Designer)*
**AI:** Gemini is listed as a built-with tool; the page does not say whether it drives recommendations or something else.
**Architecture:** Next.js/React/TypeScript frontend with Three.js 3D view; Python FastAPI backend; MongoDB storage; Gemini for AI features.
**Novelty:** Combines a parts-based configurator with live requirement tracking and a 3D view; page is very brief and gives little detail on rules or recommendation logic.
**Scope:** small · working: A demo video exists but its content could not be read; no live demo link. · polish: Short Devpost text; repo README and tree not readable.
**Claims:** Winner of 3rd place in the Siemens Energy Data Center Designer challenge | Aims to be intuitive and fun to use
**Gaps:** Repo clone failed and README fetch failed, so no repo details; Video content not viewable; Siemens challenge text not found; Devpost page lists no problem, challenges or next steps
Sources: https://devpost.com/software/rack-attack, https://hackupc-2025.devpost.com/

---

### Referlut
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [1st] Revolut - AI in Financial Applications [1st]

**What it is:** A student-focused web app that surfaces refer-a-friend and pooling deals, uses LLM agents to scrape and validate them, matches users who can benefit together, and adds LLM personal-finance insights from linked bank transactions.
**Problem / user:** Students managing money who miss refer-a-friend or pooled-purchase offers and struggle to find peers to refer.

**Features**
- Deal discovery by scraping and LLM validation — Scraper navigates the web; Gemini with Google Search validates deals and fills in missing or biased details. *[claimed]*
- Marketplace page of referral and pooling offers — React page lists deals so users can browse and advertise their own. *[claimed]*
- Matching users to share deals — Pairs users who can jointly benefit from a referral or pooling offer. *[claimed]*
- Bank account linking — Open Banking API (GoCardless/Nordigen client in requirements) fetches transactions, cached locally and refreshed in real time. *[claimed]*
- LLM personal finance insights and dashboard — GPT-4.1 does denser financial analysis; GPT-3.5 Turbo summarises convoluted deals; shown on a user dashboard. *[claimed]*
- Parallel fetching with buffered rendering — Responses are fetched in parallel and rendered progressively to hide LLM and scrape latency. *[claimed]*
- Social side and other pooling types — Collaborative features and car-pooling or student renting. *[planned]*

**Flow:** Sign in → Link a bank account via Open Banking → Browse the marketplace of validated referral and pooling deals → Get matched with another user for a deal → View LLM-generated finance insights on the dashboard

**Prompt:** Build a working AI-powered finance tool (LLMs or deep learning), beyond a plain chatbot, judged on innovation, impact and creativity; Revolut supplies no APIs.
**Fit (implied):** Uses LLM agents to find and verify student deals and to generate spending insights from bank data, aiming past a plain chatbot.  *(targeted: Revolut - AI in Financial Applications)*
**AI:** Agentic workflow: Gemini with Google Search validates scraped deals; GPT-3.5 Turbo condenses deal text; GPT-4.1 produces financial analytics; Responses API and MCP mentioned.
**Architecture:** React/Tailwind frontend; FastAPI Python API with BeautifulSoup scraping and OpenAI/Gemini calls; Supabase backend and auth; Open Banking transactions cached and fed to LLM insights.
**Novelty:** Targets referral and pooling offers as a deal category, with LLM verification of scraped deals and peer matching, rather than generic budgeting.
**Scope:** medium · working: Repo has about 14k LOC across frontend and API; Devpost reports little lag under heavy LLM and scraping load; no demo link. · polish: Four screenshots; repo README is a one-line title only; no tests.
**Claims:** Handled heavy LLM and scraping load with little no lag | 1st place in Revolut AI in Financial Applications
**Gaps:** Repo README holds only a title; features come from Devpost and file tree; No video or user-flow description; Matching logic details not described
Sources: https://devpost.com/software/referlut, evidence/hackupc-hackupc-2025-referlut.json, https://hackupc-2025.devpost.com/

---

### RevPoints+
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [3rd] Revolut - AI in Financial Applications [3rd]

**What it is:** Two-sided prototype for Revolut Points: consumers get personalised places to spend points from their transaction history, and small vendors upload a brochure so an AI agent drafts a marketing campaign. Includes a recruiter agent that enriches vendor leads and drafts outreach.
**Problem / user:** Revolut customers rarely redeem points because they miss relevant offers; small partner vendors lack an automated way to reach interested users.

**Features**
- Personalised Explore Feed of redemption options — Sentence-Transformer embeddings with recency-weighted transaction scoring rank vendors; README describes a k-NN content recommender over mock CSVs. *[shown_working]*
- Real-time feed refresh — Redis Streams pub/sub updates recommendations when new transactions arrive. *[claimed]*
- User profiling agent — Gemini builds a JSON profile of top categories, frequent merchants, spend frequency and timing. *[claimed]*
- Vendor Campaigner agent — Vendor uploads a catalogue or brochure; Gemini 2.5 Pro drafts a campaign, vendor edits and confirms, saved in Redis. *[shown_working]*
- Recruiter agent — Uses Perplexity to enrich vendor name, email and description, produce a JSON profile and draft outreach emails. *[claimed]*
- Consumer and vendor dashboards — Points balance, spend by category and merchant charts for users; offer performance and engagement for vendors. *[claimed]*
- Campaign notifications — Interested users are notified on launch, timed to their activity patterns. *[claimed]*
- Variants, dynamic tiers, bundles, mobile apps, open API — Listed future work. *[planned]*

**Flow:** Consumer opens app and sees a Spend Points feed built from mock transactions → Browses vendor offers payable in points and dashboards → Vendor registers and uploads a brochure → AI drafts a campaign; vendor reviews, edits and confirms → Campaign goes live and interested users are notified

**Prompt:** Build a working AI-powered finance tool (LLMs or deep learning), beyond a plain chatbot, judged on innovation, impact and creativity; Revolut supplies no APIs.
**Fit (implied):** Applies LLM agents and embeddings to Revolut's points programme, connecting customers and vendors; framed around low points redemption.  *(targeted: Revolut - AI in Financial Applications)*
**AI:** Gemini 2.5 Pro with function-calling schemas and Pydantic for brochure-to-campaign extraction; Gemini for user profiles; Sentence-Transformers for recommendations; Perplexity API for vendor enrichment; LangGraph orchestration.
**Architecture:** Separate consumer and vendor apps (Streamlit per Devpost, with React/v0 front ends in repo); Python modules; Redis cache and Streams; LangGraph/LangChain agents; mock CSV transactions and partners.
**Novelty:** Addresses both sides of a loyalty market with consumer recommender, vendor campaign generator and vendor recruitment agent, plus a human-in-the-loop review step.
**Scope:** medium · working: Two live demo URLs listed (Devpost Streamlit, README Vercel); repo about 18k LOC with consumer and vendor apps. · polish: Revolut-style card UI; README short and describes a simpler Streamlit k-NN loop than the Devpost; no tests.
**Claims:** Brochure to live campaign in under 2 minutes | Explore Feed latency under 200 ms after transactions | Parsing errors cut by 80% with function calling, Pydantic and retries
**Gaps:** Devpost and README disagree on UI stack: Devpost says Streamlit with Redis agents, README describes a simple Streamlit k-NN demo while repo also holds React vendor and consumer apps; demo URLs differ between the two; Claims not verified; No video
Sources: https://devpost.com/software/revpoints, evidence/hackupc-hackupc-2025-revpoints.json, https://hackupc-2025.devpost.com/

---

### TopRack Studio
*HackUPC HackUPC 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** HackUPC 3rd place [3rd]

**What it is:** A data center planning platform: a web editor where sales staff drag modules into a room layout scanned in VR, with constraint checking, and a Unity VR view so clients can walk the layout in first person.
**Problem / user:** Sales teams and clients who struggle to communicate and validate made-to-order data center layouts.

**Features**
- 2D drag-and-drop layout editor — Web app on a Leaflet grid where modules from a library are dragged into the room. *[shown_working]*
- Room scan to grid — Room coordinates from a VR scan are converted into a sandbox-style grid. *[claimed]*
- VR first-person client view — Unity app with Meta XR SDK shows the layout in a headset; README also mentions WebXR. *[claimed]*
- CSV-driven rules and module libraries — Uploading CSVs defines modules and constraints for networking, cooling, power and processing without code changes. *[claimed]*
- Spec checker and real-time feedback — Design is validated against rulesets and violations are shown instantly. *[claimed]*
- Project setup and cloud storage — Setup wizard with units and advanced options; Django REST API stores designs. *[claimed]*
- Live web-to-VR sync, multi-user, better visuals — Devpost lists real-time sync as next step while also describing live updates. *[planned]*

**Flow:** Create a project and choose modules and rulesets → Scan the room in VR → Drag modules into the 2D layout and watch constraints → Client in headset views the 3D layout → Iterate and save to the cloud

**Prompt:** Build a designer for a made-to-order data center where clients explore equipment and service options across networking, cooling, power and processing against external loads.
**Fit (explicit):** Page says it was built for the Siemens challenge; adds constraint rulesets for networking, cooling and power plus a VR client view.  *(targeted: Siemens Energy - Data Center Designer, HackUPC 3rd place)*
**AI:** none
**Architecture:** Vue 3/React web front end with Leaflet; Django REST API with SQLite; Unity/Meta XR VR app; CSV rule engine; deployed demo site.
**Novelty:** Uses VR for both room scanning and client presentation, tying a headset scene to a web editor; hardware brought to the event.
**Scope:** medium · working: Live demo site and video linked; repo about 8k LOC across web, backend and VR folders. · polish: Rich README with screenshots and setup wizard shots; no tests or CI.
**Claims:** Functional VR experience built in under 36 hours | Web interface and Unity scene interaction achieved
**Gaps:** README lists Vue/Jotai/WebXR while Devpost lists React and Unity, so stack is inconsistent; Unity-to-web communication not explained; Prize is overall 3rd place, not a sponsor prize
Sources: https://devpost.com/software/toprack-studio, evidence/hackupc-hackupc-2025-toprack-studio.json, https://hackupc-2025.devpost.com/

---

### TripMates - Team Trip Planner AI Agent
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [1st] Skyscanner - The Perfect Reunion: Finding the Best Destination for friends around the world [1st]

**What it is:** A voice AI agent that sits in on a group of friends planning a trip, answers when asked, searches flights, hotels and events through APIs, and emails a trip proposal at the end.
**Problem / user:** Groups of friends in different cities who find it hard to agree on a destination together.

**Features**
- Real-time group voice conversation — LiveKit room with Deepgram speech-to-text, gpt-4o-mini agent and Cartesia text-to-speech; listens to chatter and replies when asked. *[shown_working]*
- Preference merging — Collects budget, dates and interests from each member and proposes options resolving conflicts. *[claimed]*
- Flight search — Agent tool calls Skyscanner for options and prices and picks a good one for the group. *[shown_working]*
- Hotels and events — Amadeus for hotels; Ticketmaster and Meetup for activities. *[claimed]*
- Emailed trip proposal — At session end the agent sends a summary via SendGrid. *[claimed]*
- Live transcript and animations — React UI shows the conversation as text with animated feedback. *[shown_working]*
- Calendar sync, voting, editable proposal — Listed as next steps. *[planned]*

**Flow:** Start the agent in the web app → Members speak preferences aloud and talk among themselves → Ask the agent for destinations, flights, hotels, events → Agent proposes a plan → Proposal is emailed to the group

**Prompt:** Design a user-friendly travel planner that helps a group of friends in different places pick a meeting destination, weighing interests, events, cost and sustainability.
**Fit (explicit):** README says it was made for this challenge: one conversational agent collects everyone's preferences and queries Skyscanner flight data for the group.  *(targeted: Skyscanner - The Perfect Reunion)*
**Sponsor tools:** Skyscanner API (Flight options and prices exposed as an agent tool, core)
**AI:** gpt-4o-mini orchestrates tool calls inside LiveKit Agents; Deepgram transcribes and Cartesia speaks (Devpost names OpenAI and Deepgram Nova 3 differently).
**Architecture:** React frontend with LiveKit client; Python LiveKit Agents backend with tool functions calling Skyscanner, Amadeus, Ticketmaster, Meetup and SendGrid.
**Novelty:** Voice-first agent that listens to a live group discussion rather than a form-based planner.
**Scope:** small · working: README has demo video link and setup steps; about 1k LOC. · polish: Clear README with architecture bullets and screenshots section; no tests.
**Claims:** 1st place in Skyscanner track
**Gaps:** Devpost and README disagree on speech stack (OpenAI STT and Deepgram TTS vs Deepgram STT and Cartesia TTS) and Devpost lists no video while README links one; No metrics
Sources: https://devpost.com/software/tripmates-team-trip-planner-ai-agent, evidence/hackupc-hackupc-2025-tripmates-team-trip-planner-ai-agent.json, https://hackupc-2025.devpost.com/

---

### unpackr
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [3rd] Skyscanner - The Perfect Reunion: Finding the Best Destination for friends around the world [3rd]

**What it is:** A vibes-based group trip recommender: members upload luggage photos, a favourite song and a colour palette, and the app suggests a destination, then shows cheapest flights per member, local events and a like/dislike-driven itinerary.
**Problem / user:** Groups of friends planning a trip who want a playful alternative to the usual where-do-you-want-to-go question.

**Features**
- Vibe input — Users give luggage photos, a song and a colour palette; the app analyses aesthetic and mood (model not named; openai dependency in repo). *[claimed]*
- Group creation by code — One member creates a group and shares a code; everyone submits their own inputs. *[claimed]*
- Live flight pricing — Skyscanner API returns cheapest flights from each member's origin to the suggested destination. *[claimed]*
- Destination events — PredictHQ API lists events during the travel dates. *[claimed]*
- Group itinerary — Members like or dislike suggested activities and feedback produces a group plan. *[claimed]*
- Accounts and storage — Supabase handles login, sign-up and database. *[claimed]*

**Flow:** Sign up and create or join a group with a code → Each member uploads photos, palette and song → App suggests a destination → See per-member flight prices and destination events → Vote on activities to get a group itinerary

**Prompt:** Design a user-friendly travel planner that helps a group of friends in different places pick a meeting destination, weighing interests, events, cost and sustainability.
**Fit (explicit):** Shared inputs from every member drive one group destination, with Skyscanner flight prices per origin and event data.  *(targeted: Skyscanner - The Perfect Reunion)*
**Sponsor tools:** Skyscanner API (Cheapest flight prices from each member's location, core)
**AI:** Image, song and palette analysis for mood-based destination matching; model and method not specified on the page.
**Architecture:** Next.js front end with react-three-fiber visuals; Supabase for auth and data; OpenAI, Skyscanner and PredictHQ API calls.
**Novelty:** Chooses destinations from aesthetic inputs such as luggage photos, music and colours rather than stated preferences.
**Scope:** small · working: Repo about 5.6k LOC with feature list in README; no demo link or video. · polish: Branded logo and README feature list; one gallery image; no tests.
**Claims:** 3rd place in Skyscanner challenge
**Gaps:** AI model and how mood is mapped to a destination not described; No video or demo
Sources: https://devpost.com/software/unpackr, evidence/hackupc-hackupc-2025-unpackr.json, https://hackupc-2025.devpost.com/

---

### We Nomad Us
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [2nd] Skyscanner - The Perfect Reunion: Finding the Best Destination for friends around the world [2nd]

**What it is:** A Flutter mobile app where a group creates a 'Tribe', swipes yes/no on travel-preference cards, and receives Gemini- and Skyscanner-based destination, date and activity suggestions, plus NFC-unlocked digital collectibles stored in an in-app wallet.
**Problem / user:** Groups, including non-technical users, who struggle to agree on where to travel together.

**Features**
- Tribes joined by QR, code or NFC — A user creates a virtual room; members join via a unique code, QR or NFC tap, backed by Supabase. *[claimed]*
- Simultaneous swipe quiz — Members swipe right or left on yes/no cards on climate, activities, budget and culture. *[claimed]*
- Gemini-based destination recommendation — Aggregated group answers are weighted by a Gemini-based model (prompt engineering, described fine-tuning) to rank destinations. *[claimed]*
- Flight prices, dates and activities — Skyscanner API gives live prices, best dates and trip duration; results cached in Supabase and combined with Gemini activity ideas. *[claimed]*
- Collectibles with rarity tiers — NFT-like items (Common, Rare, Shiny) earned for destinations, tracked in Supabase without a real blockchain. *[claimed]*
- NFC partner unlocks — Tapping NFC cards at partner sites such as museums or local bars unlocks exclusive collectibles; partnerships were simulated. *[claimed]*
- Offline mode, social sharing, AR collectibles, premium tier — Listed future work. *[planned]*

**Flow:** Create a Tribe → Members join via QR, code or NFC → Everyone swipes through the quiz → App recommends destinations with prices, dates and activities → Collectibles are earned or unlocked by NFC and kept in the wallet

**Prompt:** Design a user-friendly travel planner helping a group of friends in different places pick a meeting destination, weighing interests, events, cost and sustainability.
**Fit (explicit):** Swipe quiz collects every member's preferences simultaneously; Skyscanner data supplies prices and dates for the group's destination.  *(targeted: Skyscanner - The Perfect Reunion)*
**Sponsor tools:** Skyscanner API (Live flight prices, optimal dates, trip durations and activity data, core)
**AI:** Gemini-based recommender over aggregated swipe responses with preference weighting; also generates activity suggestions combined with Skyscanner data.
**Architecture:** Flutter client with NFC plugins; Supabase Postgres, auth and API; Gemini scripts; Skyscanner calls cached in Supabase; web demo hosted on Vercel.
**Novelty:** Adds a physical NFC collectible game with partner locations on top of a group travel quiz, aimed at local tourism.
**Scope:** medium · working: Full Flutter project with Android, iOS, desktop targets, a deployment folder and a test folder; site wenomads.us listed. · polish: One demo image on Devpost; repo README is the default Flutter template; no video.
**Claims:** Users can create a Tribe, join and swipe in minutes | 2nd place in Skyscanner challenge
**Gaps:** README is Flutter boilerplate so repo detail comes from file tree only; evidence tree inflated by a committed .venv; Fine-tuning claim and NFC reliability not verified
Sources: https://devpost.com/software/we-nomad-us, evidence/hackupc-hackupc-2025-we-nomad-us.json, https://hackupc-2025.devpost.com/

---

### Wise Wallet
*HackUPC HackUPC 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [2nd] Revolut - AI in Financial Applications [2nd]

**What it is:** A personal-finance assistant with a React dashboard and an Alexa skill. Random Forest models classify spending as needs or wants and predict month-end totals; Gemini answers spoken questions about recent spending.
**Problem / user:** Individuals who only see raw expense numbers and want early, understandable feedback on spending before the month ends.

**Features**
- Needs vs wants classification — Random Forest classifier, trained on simulated transactions, labels each expense; shown as a semi-circular chart beside an expense list. *[claimed]*
- Month-end expense prediction — Random Forest regressor estimates the month's total from partial data and plots it in a graph. *[claimed]*
- Alexa voice assistant — Skill Lambda fetches the user's expenses and passes the spoken query to Gemini, answering questions like what was spent on food last week. *[claimed]*
- Serverless ML inference — Docker-image Lambdas load models from S3 and serve classify-expenses and predict-expenses endpoints behind API Gateway. *[claimed]*
- Latency reduction for voice — Caching common intents and reducing cold starts cut about 5 s responses. *[claimed]*
- Bank sync, mobile app, daily voice digest — Plaid or open banking, React Native, morning summary; later domain-tuned LLM. *[planned]*

**Flow:** Open the web dashboard with listed bank movements → See predicted month-end spend and needs/wants breakdown → Ask Alexa a spending question → Gemini answers using the latest expense data

**Prompt:** Build a working AI-powered finance tool (LLMs or deep learning), beyond a plain chatbot, judged on innovation, impact and creativity; Revolut supplies no APIs.
**Fit (implied):** Combines custom-trained ML models with an LLM voice interface, going beyond a text chatbot; README labels it the 2nd place Revolut prize.  *(targeted: Revolut - AI in Financial Applications)*
**AI:** scikit-learn Random Forest classifier and regressor trained on simulated expense data; Gemini with tuned system and query prompts for Alexa answers.
**Architecture:** React/TypeScript dashboard; AWS API Gateway, Lambda (Docker images via ECR) and S3 model storage; separate Alexa skill Lambda calling Gemini.
**Novelty:** Pairs trained classical ML for classification and forecasting with an LLM voice layer on a smart speaker.
**Scope:** small · working: Devpost says deployed with real ML inference; repo about 2.4k LOC with Lambda, models and frontend; no demo link. · polish: Detailed README with deployment steps; two screenshots; no tests or CI.
**Claims:** Cut Alexa response from about 5 s via caching and fewer cold starts | Real ML inference rather than hardcoded logic
**Gaps:** Devpost page read via Chrome after WebFetch returned empty; Training data was simulated; accuracy not reported; No video or live demo
Sources: https://devpost.com/software/spendly-nx3hb0, evidence/hackupc-hackupc-2025-wise-wallet.json, https://hackupc-2025.devpost.com/

---

