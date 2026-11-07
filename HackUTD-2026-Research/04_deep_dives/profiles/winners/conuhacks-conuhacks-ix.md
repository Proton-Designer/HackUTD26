# ConUHacks — ConUHacks IX (17 projects)

### 404 Lost & Found
*ConUHacks ConUHacks IX · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 3rd Place - 4x MSI MAG 27” QHD Gaming monitor and MLH Winner Pins [3rd]

**What it is:** An AI lost-and-found web app: users report or search for items, YOLO detects objects in uploaded photos and ResNet embeddings score visual similarity between lost and found items. Images sit in Azure Blob Storage, metadata in MongoDB, with Google Maps directions to the item.
**Problem / user:** People who lose valuables; manual text descriptions and memory make matching lost and found items slow and frustrating.

**Features**
- Report and search lost items — Users post items with images; search works with nearby locations. *[claimed]*
- Object detection — YOLO localizes items such as laptops, backpacks and keys in uploads. *[claimed]*
- Visual similarity matching — ResNet-50 embeddings compare lost and found images. *[claimed]*
- Caption generation — Azure AI Vision generates captions. *[claimed]*
- Maps navigation — Google Maps API guides user to the item. *[claimed]*
- Cloud deployment pipeline — Docker images pushed to ACR by GitHub Actions; Terraform provisions Azure App Service. *[shown_working]*

**Flow:** Report or search for an item with a photo → YOLO detects the object → ResNet finds close matches → View match and get directions → Claim the item

**Prompt:** 3rd place overall: prize is gaming monitors and MLH pins; no track brief.
**Fit (none):** General placement prize, no brief; project is a full-stack AI app with cloud deployment.  *(targeted: 3rd Place)*
**AI:** YOLO object detection plus fine-tuned ResNet-50 embeddings for similarity scoring; Azure AI Vision for captions.
**Architecture:** Streamlit frontend and FastAPI backend; images in Azure Blob Storage, metadata in MongoDB; Terraform and GitHub Actions deploy to Azure.
**Novelty:** Pairs vision matching with production-style infrastructure (IaC, CI/CD) for a weekend build.
**Scope:** small · working: Repo ~1.3k LOC with Docker and CI; demo video link in README; no live URL. · polish: Emoji-styled README; infra automation; YOLO version inconsistent (v5 vs v8).
**Gaps:** video not watched; YOLOv5/v8 inconsistent
Sources: https://devpost.com/software/404-lost-found, evidence/conuhacks-conuhacks-ix-404-lost-found.json (README), https://conuhacks-ix.devpost.com/

---

### ASL-Bridge
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [DRUIDE] Best Use of Language

**What it is:** A prototype ASL-to-speech translator. An LSTM trained on body, hand and face keypoints recognizes signed words from video, GPT-4 rewrites the literal gloss into fluent English, and ElevenLabs speaks it.
**Problem / user:** Signers and the people who want to talk with them; translation apps neglect sign language.

**Features**
- Keypoint extraction — Extracts hand, arm, body and head keypoints from a video stream with a ML pose model. *[shown_working]*
- LSTM sign recognition — Trained on self-collected data (60 samples per word); only 10 words learned. *[shown_working]*
- Gloss-to-English via GPT-4 — Turns "NICE MEET YOU" into "Nice to meet you". *[claimed]*
- Voice output with ElevenLabs — Speaks the decoded sentence. *[claimed]*
- Data collection script — Records samples for each word. *[shown_working]*

**Flow:** Record signed sentence on camera → Keypoints extracted → LSTM predicts word sequence → GPT-4 smooths into English → ElevenLabs speaks it

**Prompt:** [DRUIDE] Best Use of Language: no challenge text published beyond the title; prize is goodies.
**Fit (implied):** Translates sign language into spoken English, using language models to fix grammar and generate speech.  *(targeted: [DRUIDE] Best Use of Language)*
**Sponsor tools:** ElevenLabs (Speech output, supporting)
**AI:** Custom LSTM over pose keypoints for word detection; GPT-4 converts ASL gloss grammar to English; ElevenLabs TTS.
**Architecture:** Python/OpenCV capture, keypoint extractor, LSTM classifier, GPT-4 text pass, ElevenLabs voice.
**Novelty:** Sequence model on motion keypoints rather than static handshapes, though vocabulary limited to 10 words.
**Scope:** tiny · working: Small repo (~500 LOC) and screenshots of training and tracking; no demo video. · polish: README with slides link; proof-of-concept only.
**Claims:** Handles movement, enabling a potentially full dictionary
**Gaps:** no video
Sources: https://devpost.com/software/asl-bridge, evidence/conuhacks-conuhacks-ix-asl-bridge.json (README), https://conuhacks-ix.devpost.com/

---

### Better Call Saul AI
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence C · confidence low*
**Prizes:** [MLH] Best Domain Name from GoDaddy Registry

**What it is:** A React/Vite web app named Better Call Saul AI, deployed on Vercel. Its purpose is not documented; dependencies (Deepgram, Google Cloud Speech, annyang, Supabase) suggest a voice-driven legal-help assistant, but this is inferred.
**Problem / user:** Unknown; not stated in any readable source.

**Features**
- Voice input — Dependencies for Deepgram, Google speech-to-text and annyang imply speech capture. *[unclear]*
- Supabase data layer — Supabase client dependency implies stored user or case data. *[unclear]*

**Prompt:** MLH prize: register a domain with GoDaddy Registry; the page lists no specific rules beyond that.
**Fit (none):** Not determinable; no description or domain seen.  *(targeted: [MLH] Best Domain Name from GoDaddy Registry)*
**AI:** none
**Architecture:** Vite/TypeScript frontend with Tailwind and shadcn/ui plus a small Express backend using Google Cloud Speech; hosted on Vercel/Netlify.
**Novelty:** Cannot assess; no description available.
**Scope:** small · working: Repo ~5k LOC and 33 commits; Vercel page loads with title only. · polish: Template-style UI scaffolding (many Radix components); no docs.
**Gaps:** Devpost page not found at tried URLs; no README; purpose inferred from dependencies only
Sources: https://github.com/Stoplossking1/BetterCallSaulAI, https://better-call-saul-ai.vercel.app, evidence/conuhacks-conuhacks-ix-better-call-saul-ai.json, https://conuhacks-ix.devpost.com/

---

### Beyond Budgeting
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [TAILE'D] Best Use of Lovable

**What it is:** A web personal-finance companion built on Lovable that pulls simulated open-banking account data into a dashboard and offers AI budgeting plus investment and Sun Life product suggestions.
**Problem / user:** Retail banking/insurance customers wanting spending insight and advice; page frames Sun Life as the beneficiary, claiming it would save the company money.

**Features**
- Simulated OpenBanking integration — API endpoints expose mock real-time account and transaction data to the app *[claimed]*
- Financial summary dashboard — Shows accounts and spending profile overview *[shown_working]*
- AI budgeting and expense tracking — Analyzes spending patterns to suggest savings; model unnamed *[claimed]*
- Investment and Sun Life product recommendations — Tailors strategies and company products to the user profile *[shown_working]*
- Financial literacy hub — Educational resources, FAQs and links *[planned]*
- Chatbot financial advisor — Real-time AI guidance *[planned]*

**Flow:** Open the hosted Lovable app → View dashboard of accounts and spending → Review AI budgeting insights → Open investment recommendations page

**Prompt:** TAILE'D prize for showcasing the best use of Lovable; teams build on Lovable, post about it tagging Lovable on X; winner offered an interview for a Lovable customer-success role.
**Fit (implied):** The whole app was generated and iterated on the Lovable platform (repo is a Lovable export with Vite/React/shadcn/Supabase folders), so platform use is complete but not otherwise described.  *(targeted: [TAILE'D] Best Use of Lovable)*
**Sponsor tools:** Lovable (Generating and hosting the entire React/TypeScript app, core)
**AI:** Unspecified AI for budgeting analysis and recommendations; no model or prompting detail given.
**Architecture:** Lovable-generated Vite/React/TypeScript/shadcn front end with Tailwind, a small Supabase directory, and mock open-banking endpoints feeding dashboard and recommendation views.
**Novelty:** Framed around a specific insurer (Sun Life) with product cross-sell; built entirely through a prompt-to-app platform rather than hand-coded.
**Scope:** small · working: Live lovable.app demo link and two screenshots; repo about 8k LOC of generated code. · polish: Generic Lovable README; dashboard and recommendation screens shown; literacy hub and chatbot unfinished.
**Claims:** Would save Sun Life over $650,000 per year (no method given)
**Gaps:** No AI model detail; No walkthrough; Demo site not opened
Sources: https://devpost.com/software/beyond-budgeting, https://conuhacks-ix.devpost.com/, evidence file

---

### CrisisConnect
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Gen AI

**What it is:** A Streamlit app matching disaster victims' free-text requests to donor offers. A fine-tuned BERT model predicts the need type, then embeddings, distance and capacity checks rank donors, with an LLM summary and a news page.
**Problem / user:** People affected by disasters needing shelter, food or medical help, and donors offering aid; hard to connect them quickly.

**Features**
- Intent classification — Fine-tuned BERT sorts requests into six needs (shelter, food, medical, transport, financial, supplies) using ChatGPT-generated training data *[claimed]*
- Donor ranking — Sentence-transformer cosine similarity plus distance penalty, intent and keyword boosts, capacity check, normalized 0-1 *[claimed]*
- LLM summary of donor offers — Llama3-8B-Instruct summarizes top donor matches for the victim *[claimed]*
- News and updates page — spaCy extracts disaster and place, news API fetches articles, ranked by embedding similarity, BART summarizes top 5 *[claimed]*
- Donor registration page — Donors submit details and offers so victims can reach them *[claimed]*
- Interactive donor map — Built in React but could not be ported to Streamlit *[unclear]*

**Flow:** Victim types a description of their situation → App detects location and predicts need type → Ranked donor matches with LLM summaries appear → Victim opens News and Updates for relevant disaster articles → Donors separately register offers

**Prompt:** MLH Best Use of Gen AI: build a functional application using publicly available generative AI APIs such as OpenAI, Anthropic, Hugging Face, Llama, Watson or Gemini.
**Fit (implied):** Uses a fine-tuned language model, Llama3-8B-Instruct for summaries, BART and ChatGPT-generated training data in a working matching app; page lists the prize as won.  *(targeted: [MLH] Best Use of Gen AI)*
**AI:** Fine-tuned BERT classifier on synthetic data (reports 100 percent accuracy, admitted overfitting); Sentence Transformers embeddings for matching; Llama3-8B-Instruct and BART for summaries.
**Architecture:** Python backend and Streamlit front end; classifier then embedding/scoring pipeline over a mock donor database; separate news pipeline with spaCy, news API and summarizer.
**Novelty:** Combines classification, semantic ranking with geographic and capacity logic, and news retrieval in one relief dashboard; transparent about synthetic data.
**Scope:** small · working: Repo with backend, mock_db and Streamlit pages (~2.5k LOC); no demo link or video. · polish: README is the Devpost text; admits overfitting and dropped map; no tests.
**Claims:** Intent classifier reached 100% accuracy, acknowledged as overfitting
**Gaps:** No demo; Screenshot count unknown
Sources: https://devpost.com/software/crisisconnect-8zm143, https://conuhacks-ix.devpost.com/, evidence file

---

### CyberOxide
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of MongoDB Atlas

**What it is:** A local network security monitor: a Rust backend captures packet metadata, stores events in MongoDB, an LLM assesses threats from anonymized data, and a Streamlit dashboard shows results live.
**Problem / user:** Individuals who want to watch their own network traffic for threats without exposing packet contents to third parties.

**Features**
- Metadata-only packet capture — Rust sniffer records headers/metadata, never payloads, non-promiscuous by default with optional toggle *[claimed]*
- Threat pattern detection — Rules and pattern recognition on captured events *[claimed]*
- LLM threat insights — Anonymized event summaries sent to Together.ai LLM for analysis *[claimed]*
- Event storage — Local MongoDB with async operations and configurable retention *[claimed]*
- Real-time dashboard — Streamlit page reading MongoDB asynchronously *[shown_working]*
- Cross-platform support — Handles Linux, macOS, Windows capture differences *[claimed]*

**Flow:** Start mongod → Run the Rust backend with cargo run → Launch streamlit dashboard → Watch traffic events and LLM threat insights update

**Prompt:** MLH Best Use of MongoDB Atlas: build a hack using MongoDB Atlas; promotes free tier and student credit.
**Fit (implied):** MongoDB stores all network events behind the dashboard with async access, but the README describes a local mongod rather than Atlas.  *(targeted: [MLH] Best Use of MongoDB Atlas)*
**Sponsor tools:** MongoDB (Event storage for the dashboard (local instance per README), core)
**AI:** Together.ai hosted LLM analyzes anonymized traffic metadata for threat insights; no training.
**Architecture:** Rust packet capture and Actix server writes events to MongoDB; Python/Streamlit dashboard queries it asynchronously and calls the LLM API.
**Novelty:** Rust packet capture paired with a privacy-preserving LLM step; team states they learned Rust during the event.
**Scope:** small · working: Repo with Rust and Python code (~1.3k LOC), tests folder, CI workflow, dashboard screenshot. · polish: Polished README with diagrams folder, legal/privacy notes and contributing docs; no video or live demo.
**Claims:** Analyzes metadata only, never packet contents
**Gaps:** No demo video
Sources: https://devpost.com/software/cyberoxide, https://conuhacks-ix.devpost.com/, evidence file

---

### FinHealth
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [MLH] Best Use of Streamlit

**What it is:** A Streamlit investing assistant for beginners combining stock recommendations, sentiment-labelled news, a context-aware GPT chatbot, tailored plans and portfolio-screenshot analysis.
**Problem / user:** People new to investing who find managing finances and picking investments intimidating.

**Features**
- Stock recommendations dashboard — Yahoo Finance data with buy/hold/sell suggestions from a random-forest-style classifier *[shown_working]*
- News sentiment labels — Marks market news positive, neutral or negative *[shown_working]*
- Context-aware chatbot — GPT-4o-mini answers using tracked stocks and recent news *[shown_working]*
- Tailored investment plan — Form of finances, goals and risk tolerance produces a custom plan *[shown_working]*
- Portfolio screenshot analysis — Parses an uploaded portfolio image for advice *[claimed]*

**Flow:** Open home dashboard of recommended stocks → Read news with sentiment → Ask the chatbot questions → Fill the tailored plan form and read results → Upload a portfolio screenshot for analysis

**Prompt:** MLH Best Use of Streamlit: hack with Streamlit, the free-to-deploy Python framework, for an Arduino Tiny ML Kit per member.
**Fit (implied):** Entire app is a Streamlit multi-screen dashboard with custom HTML/CSS components and plotly charts; team says it was their first Streamlit project.  *(targeted: [MLH] Best Use of Streamlit)*
**Sponsor tools:** Streamlit (Whole front end and app framework, core)
**AI:** GPT-4o-mini chatbot with news and stock context; sentiment analysis of headlines; scikit-learn classifier for buy/hold/sell, claimed 79 percent average accuracy.
**Architecture:** Python Streamlit app pulling yfinance quotes and news, running sklearn and nltk models locally, calling OpenAI for chat and plans, plotly visuals.
**Novelty:** Bundles prediction, sentiment, chat and screenshot-based portfolio review in one beginner-focused tool.
**Scope:** small · working: Repo and six screenshots on the page; no live demo or video. · polish: Custom styled UI; accuracy metric undefined; repo name differs between links.
**Claims:** Average prediction accuracy of 79% reached within 24 hours
**Gaps:** README not inspected in detail
Sources: https://devpost.com/software/budget-buddy-b42oin, https://conuhacks-ix.devpost.com/, evidence file

---

### Finsurance
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Sun Life - 4x 100$ Amazon gift cards

**What it is:** A budgeting website with a dolphin mascot chatbot, Fin, built in a Botpress agent trained on Sun Life information. It adds an interactive budget planner, a financial-literacy quiz, site navigation help and login-backed account data.
**Problem / user:** People wanting approachable financial guidance and Sun Life information; page defines no narrower user.

**Features**
- Fin chatbot companion — Botpress agent with workflows and custom tools, trained on Sun Life data and budgeting help. *[claimed]*
- Interactive budgeting tool — Lets users plan future finances on the site. *[claimed]*
- Financial literacy quiz — Quiz section on the website. *[claimed]*
- Navigation guidance — Fin helps users move between the site's topics. *[claimed]*
- Authentication and stored account data — FastAPI backend with PostgreSQL for login and secure retrieval of each user's data. *[claimed]*

**Flow:** Visit the site and log in → Use the budgeting tool → Ask Fin questions about budgeting or Sun Life → Take the literacy quiz

**Prompt:** Sun Life prize on the ConUHacks IX listing shows only 4x $100 Amazon gift cards; the Devpost page says the challenge was an AI companion.
**Fit (explicit):** Fin is an AI mascot companion with Sun Life knowledge and budgeting help, matching the stated AI-companion challenge.  *(targeted: Sun Life - 4x 100$ Amazon gift cards)*
**AI:** Botpress-hosted conversational agent using built-in workflows plus custom tools; underlying LLM not specified.
**Architecture:** React/TypeScript frontend (separate repo), Python FastAPI backend with PostgreSQL for auth and user data, Botpress agent embedded as chatbot.
**Novelty:** Mascot-driven companion that combines a chatbot, quiz and budget planner; backend repo is tiny so most logic lives in Botpress.
**Scope:** small · working: Screenshots of workflow, backend stack and a sample bot conversation; backend repo only ~560 LOC and 9 files; no demo link. · polish: Claims a polished front end; six slides in the gallery.
**Claims:** Fin has extensive Sun Life and budgeting knowledge | Won Sun Life prize
**Gaps:** Backend repo has no README; frontend repo README is Create React App boilerplate; Quiz and budget internals not seen
Sources: https://devpost.com/software/finsurance, evidence/conuhacks-conuhacks-ix-finsurance.json (backend repo, no README), https://raw.githubusercontent.com/SophiaClifton/hashbrown-app/HEAD/README.md

---

### FireWatch
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SAP - Lunch Tour with hiring managers

**What it is:** Wildfire dashboard for Quebec that allocates firefighting units to reported fires to limit cost and missed high-severity responses, and uses scikit-learn models to predict 2025 fire-prone areas, shown on a Mapbox map.
**Problem / user:** Emergency services need to deploy limited firefighting units well and anticipate future fires to cut response times and damage costs.

**Features**
- Resource allocation optimizer — Reads current wildfire CSV and assigns units by severity, speed, availability and deployment time, minimizing operating and missed-fire damage cost. *[claimed]*
- Efficiency report — Generates a summary of firefighting efficiency and costs from the allocation. *[claimed]*
- Fire prediction model — sklearn models trained on 2020-2023 fire and environmental data predict fire-prone areas, severity and location for 2025. *[claimed]*
- Mapbox prediction map — Interactive map of predicted fire locations over Quebec. *[shown_working]*
- Multi-view dashboard — File upload, list view, list-plus-map view, prediction view and map view. *[shown_working]*

**Flow:** Upload the wildfire CSV → View incidents as a list → View list alongside the map → Open the predictions view and map

**Prompt:** SAP challenge (text from team README): optimize firefighting resource deployment to minimize cost and high-severity missed responses, then predict future fires with ML and map them. Official prize listing is only a tour and lunch with iXp hiring managers.
**Fit (explicit):** Implements both parts: cost-minimizing allocation and ML fire prediction with a map visualization.  *(targeted: SAP - Lunch Tour with hiring managers)*
**AI:** scikit-learn models trained on historical environmental and wildfire data predict severity and location of 2025 fires; allocation uses optimization algorithms (unnamed).
**Architecture:** React/shadcn Vite frontend with Mapbox, Flask backend (Python) for optimization and prediction, CSV inputs.
**Novelty:** Covers both halves of the SAP brief in one deployed dashboard; no accuracy numbers given.
**Scope:** medium · working: Live demo at firewatch.bentostudio.io listed; README with setup; ~4k LOC across frontend and backend. · polish: Five dashboard views; no tests or CI.
**Claims:** Reduces response times and wildfire damage costs (no figures)
**Gaps:** Optimization algorithm unnamed; No metrics
Sources: https://devpost.com/software/firewatch-qn4yap, evidence/conuhacks-conuhacks-ix-firewatch.json (jammy312/Hackaton2025 README)

---

### GeoAir
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** DRW - 4x JBL Speakers for 1st Place

**What it is:** A web dashboard that pulls open Montreal CSV data for air quality and EV charging stations, analyzes them in a Flask backend and serves results to a Next.js front end to explore whether charging stations relate to air quality.
**Problem / user:** Asks whether EV charging sites correlate with urban air quality; no specific user named.

**Features**
- Dynamic open-data retrieval — Backend fetches CSV files from Donnees Montreal with updates. *[claimed]*
- Data analysis — pandas, numpy and geopandas filter and analyze five CSVs of roughly 200-700 rows each. *[claimed]*
- API endpoints to frontend — Flask serves analyzed data to a Next.js/Tailwind site. *[claimed]*
- 3D interactive map — Planned map to view analyzed data by region. *[planned]*

**Flow:** Open the website → View air quality and charging-station analysis fed by the API

**Prompt:** DRW prize listing: 4x JBL speakers for 1st place; no challenge text. Devpost frames it as a large-dataset challenge.
**Fit (implied):** Combines multiple open city datasets into one analysis and web view; page does not state its findings.  *(targeted: DRW - 4x JBL Speakers for 1st Place)*
**AI:** none
**Architecture:** Flask Python server with pandas/geopandas reads Montreal CSVs and exposes API endpoints consumed by a Next.js frontend.
**Novelty:** Cross-links two municipal datasets to test a hypothesis, but results are not stated.
**Scope:** small · working: Single screenshot; repo has a flask_server folder and dashboard; no demo or video. · polish: Next.js README is boilerplate; planned 3D map not built.
**Claims:** Analyzed five CSV files of 200-700 records
**Gaps:** README is Next.js boilerplate; No findings reported; Repo name conuhacksIV; edition ConUHacks IX per queue
Sources: https://devpost.com/software/geoair, evidence/conuhacks-conuhacks-ix-geoair.json

---

### GUN WEST
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** BEENOX - 4X PRIZES FOR WINNERS

**What it is:** A Wild West 1v1 arena shooter written in Java with Swing and sockets, no game engine. Two clients connect peer-to-peer and fight in rounds with pistol, shotgun and sniper plus speed-boost star pickups.
**Problem / user:** Not framed as a problem; a fun cowboy-themed multiplayer game for casual players, inspired by Call of Duty and Hotline Miami.

**Features**
- 1v1 peer-to-peer multiplayer — Two clients connect over Java sockets and sync player state. *[claimed]*
- Three switchable weapons — Pistol, shotgun and sniper. *[claimed]*
- Star speed-boost pickups — Temporary speed boost item in the arena. *[claimed]*
- Round-based matches with win screen — Rounds, win image, menu, instructions, controls and username screens. *[shown_working]*
- Custom engine pieces — Tile renderer, asset loader, collision and networking written from scratch. *[claimed]*
- Original art and audio — Assets drawn in paint.net, with music and weapon sound effects. *[claimed]*

**Flow:** Home screen → Instructions → Pick a username → Controls screen → Fight rounds switching guns → Win screen

**Prompt:** BEENOX prize listing: 4 headsets, mice, keyboards and Call of Duty Black Ops 6 games for the winners; no challenge text.
**Fit (none):** A from-scratch game, consistent with a games sponsor, but page states no link to the prize.  *(targeted: BEENOX - 4X PRIZES FOR WINNERS)*
**AI:** none
**Architecture:** Single Java Swing app with custom tile renderer, collision and asset loader; sockets give a two-client peer-to-peer link.
**Novelty:** Entire game stack hand-built in 24 hours without an engine; art and sound all in-house.
**Scope:** small · working: Screens listed in gallery; ~2.4k LOC Java; no video or README. · polish: Menu, instruction and win screens, music; sync latency listed as future work.
**Claims:** Everything built in 24 hours | All assets made in-house
**Gaps:** Repo has no README; Screenshot count approximated from captions
Sources: https://devpost.com/software/gun-west, evidence/conuhacks-conuhacks-ix-gun-west.json

---

### LeetWrite
*ConUHacks ConUHacks IX · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 2nd Place - 4x Meta Quest 3S 128GB VR Headset with Touch Plus Controllers & Batman: Arkham Shadow and MLH Winner Pins [2nd]

**What it is:** A solo-built 'reverse LeetCode' game: AI produces code in clean, messy or unreadable style and players write a description of what it does; an LLM scores them, with real-time PvP lobbies and ELO ratings.
**Problem / user:** Software engineers and students who practice writing code but rarely practice reading and documenting others' code.

**Features**
- AI-generated code puzzles — OpenAI generates a solution to a bank question in clean, messy or unreadable style *[shown_working]*
- LLM judging of descriptions — Scores player explanations on correctness, creativity and clarity *[shown_working]*
- Real-time PvP lobbies — Socket.IO lobbies and custom matchmaking queue for head-to-head rounds *[shown_working]*
- ELO ranking — Custom ELO math with ratings stored in MongoDB *[shown_working]*
- Authentication — Developer-built login *[claimed]*
- Leagues and auto-queue — Competitive league tiers and automatic matchmaking *[planned]*

**Flow:** Sign in → Create or join a lobby → Receive generated code from a question → Write a description of what it does → LLM scores answers and ELO updates

**Prompt:** General 2nd place at ConUHacks IX (prize: Meta Quest headsets); no thematic challenge text, judged overall.
**Fit (none):** General placement prize with no theme; project is a complete multiplayer game MVP with AI generation and judging.  *(targeted: 2nd Place general)*
**AI:** OpenAI API both generates code samples at varied cleanliness and grades player descriptions against rubric prompts tuned by the developer.
**Architecture:** Next.js front end, Express plus Socket.IO backend for lobbies, MongoDB for users and ratings, OpenAI for generation and scoring; API tunneled from a laptop via Cloudflare.
**Novelty:** Inverts the LeetCode format to train code reading; combines LLM-as-judge with competitive ELO matchmaking, built by one person.
**Scope:** medium · working: README embeds a demo video; ~3k LOC with separate frontend and backend; live API now inactive. · polish: Clear README, auth, matchmaking and ELO implemented; no tests; Devpost has no video.
**Claims:** Placed 2nd among 800+ participants and 180+ projects, solo in 24 hours
**Gaps:** Live demo down; Question bank source unnamed
Sources: https://devpost.com/software/leetwrite, https://conuhacks-ix.devpost.com/, evidence file

---

### PrezPal
*ConUHacks ConUHacks IX · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 1st Place - 4x PS5 and MLH Winner Pins [1st]

**What it is:** A voice-controlled AI presentation builder: say a topic, get a generated slide deck, then edit and style slides by speaking, with commands mapped to editing functions through OpenAI function calling.
**Problem / user:** Anyone who wants to make slide decks quickly without manual layout work; user not specified.

**Features**
- Deck generation by topic — OpenAI generates slides for a chosen topic *[claimed]*
- Voice commands — Moonshine speech recognition transcribes spoken edit requests *[claimed]*
- Natural language to function calls — OpenAI function calling converts requests into PowerPoint-style edit operations *[claimed]*
- Custom slide editing engine — Applies edits and styling to slides dynamically *[claimed]*
- Image fetching — Pulls pictures from Unsplash *[claimed]*
- Multi-deck, templates, LaTeX layout — Future extensions *[planned]*

**Flow:** Pick a topic and generate a deck → Speak an edit request → Request transcribed and mapped to an edit function → Slides update in the React client via polling

**Prompt:** General 1st place at ConUHacks IX (4x PS5 and MLH pins); overall prize without a theme.
**Fit (none):** General top prize with no theme; project delivers a voice plus LLM presentation editor.  *(targeted: 1st Place general)*
**AI:** Moonshine ASR for speech to text; OpenAI function calling turns commands into structured slide edit calls; generative text for slide content.
**Architecture:** React client polls a Python server; server runs ASR, OpenAI calls and an editing engine over slide state; Unsplash for images. WebSockets were abandoned for polling.
**Novelty:** Treats presentation editing as a tool-calling problem with speech input and a custom editing engine.
**Scope:** medium · working: Client and server code ~3k LOC; Devpost lists no demo link or video; README only a title (jsonderulo). · polish: Minimal docs; no tests; polish unclear.
**Gaps:** No demo or screenshots seen; Features unverified
Sources: https://devpost.com/software/prezpal-36079w, https://conuhacks-ix.devpost.com/, evidence file

---

### Quebec FireFighters
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SAP - Lunch Tour with hiring managers

**What it is:** Bilingual SwiftUI app for iOS, iPadOS and Mac that sends wildfire data to a Flask backend, returns an optimal allocation of firefighting units, and shows ML-predicted future fire hotspots on a map with GPS coordinates.
**Problem / user:** Firefighters and units need to manage and anticipate Quebec wildfires; team wants to pitch it to firefighters.

**Features**
- Resource deployment optimization — Load wildfire data by CSV or link; backend allocates units to minimize damage and operational cost. *[shown_working]*
- Wildfire prediction — Model trained on historical environmental and fire data forecasts future occurrences. *[shown_working]*
- Prediction map and hotspot list — SwiftUI map view and GPS coordinate listing of predicted hotspots. *[shown_working]*
- Bilingual interface — App supports two languages (not specified). *[claimed]*
- Deployed REST backend — Flask server hosted on Render. *[claimed]*

**Flow:** Load a wildfire CSV or link in the app → View deployment report → Request wildfire predictions → Inspect hotspots on the map

**Prompt:** SAP challenge (from FireWatch README, same prize): optimize firefighting deployment for cost and missed severe fires, then predict fires with ML and visualize on a map. Official listing: tour and lunch with iXp hiring managers.
**Fit (implied):** Covers deployment optimization plus ML prediction with map visualization in a native iOS app.  *(targeted: SAP - Lunch Tour with hiring managers)*
**AI:** Prediction model on historical environmental and wildfire data, reported about 90% accuracy and 88% F1; model type unspecified.
**Architecture:** SwiftUI iOS client calls a Flask REST API deployed on Render for optimization and predictions.
**Novelty:** Native Apple client rather than web dashboard for the SAP brief; Z3-based optimal deployment listed as future work.
**Scope:** small · working: README links a YouTube Shorts demo; ~1.8k LOC SwiftUI; four screenshots. · polish: Bilingual UI and deployed backend claimed; no tests.
**Claims:** About 90% accuracy and 88% F1 on historical data | Met all goals set at start
**Gaps:** Backend repo (aliraeisdanaei/CONUHack2025) not read; Model details unspecified
Sources: https://devpost.com/software/quebec-firefighters, evidence/conuhacks-conuhacks-ix-quebec-firefighters.json

---

### RememberThroughMe
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [MLH] Best Use of AI powered by Reach Capital

**What it is:** An assistive tool for people with memory loss that recognizes faces and places AI voice calls, with an OpenAI agent keeping each person's past interactions in MongoDB so the assistant can recall them in conversation.
**Problem / user:** People with memory loss and their loved ones, aiming to reduce isolation by helping recall past interactions.

**Features**
- Face recognition and recall — FaceNet embeddings with OpenCV cascades, indexed in Faiss, retrieve a person's stored history *[claimed]*
- Voice-to-voice AI calls — Twilio calls with speech diarization; assistant converses using remembered dialogue *[claimed]*
- Agent-managed memory logs — OpenAI agent edits and retrieves MongoDB records in real time during conversation *[claimed]*
- Smart-glasses wearable — Memory assistance on glasses *[planned]*
- Healthcare integration and therapy — AI cognitive support *[planned]*

**Flow:** Camera recognizes a person → Stored history for that person is retrieved → Voice call starts with the AI → Agent updates memory log as conversation continues

**Prompt:** MLH Best Use of AI powered by Reach Capital: projects should impact learning, health or work; prize includes webcam and a chance to talk with Reach Capital investors.
**Fit (explicit):** Targets health (memory loss) with face recognition, voice calls and a GPT agent over MongoDB; README states it won this prize.  *(targeted: [MLH] Best Use of AI powered by Reach Capital)*
**Sponsor tools:** MongoDB (Memory log storage edited by the OpenAI agent, core)
**AI:** FaceNet face embeddings with Faiss similarity search; OpenAI GPT agent reads and writes MongoDB memory records; Twilio speech with diarization.
**Architecture:** Python video_service for face matching and a call-service for Twilio voice; GPT agent and MongoDB hold memory; Swift component listed unexplained.
**Novelty:** Combines face recognition with a phone-call voice agent that edits a persistent memory store, aimed at dementia-style care.
**Scope:** medium · working: Repo ~3k LOC split into video and call services; demo video and slides linked. · polish: README only points to Devpost; no tests; screenshots uncaptioned.
**Claims:** Data managed securely with no external storage
**Gaps:** Video not watched; Swift role unknown
Sources: https://devpost.com/software/rememberthroughme, https://conuhacks-ix.devpost.com/, evidence file

---

### RestoPort
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [TAILE'D] Best Social Media Post

**What it is:** A Streamlit dashboard for airport restaurants and shops that pulls Montreal airport flight data and visualizes it to anticipate busy periods, with a beta sales-prediction metric.
**Problem / user:** Restaurants and retail stores at YUL airport that struggle to predict peaks, schedule staff and limit waste.

**Features**
- Flight data collection — Cloudscraper requests to the airport site's non-REST endpoint with live updates *[shown_working]*
- Flight data visualization — Pandas and Streamlit charts tied to store location *[shown_working]*
- Sales prediction metric — Beta heuristic estimating sales from flights; no trained model *[claimed]*
- Supervised sales model and flight database — Pipeline and ML model from flight parameters *[planned]*

**Flow:** Open the hosted Streamlit app → Choose location or store → View incoming flight data and charts → Read the beta sales indicator

**Prompt:** TAILE'D Best Social Media Post: write a LinkedIn post about the hackathon experience, project and takeaways, tagging Tail'ed and ConUHacks with team name; winners get hoodies.
**Fit (implied):** Prize judged on a LinkedIn post, not the software; the Devpost page notes the award but the post was not seen.  *(targeted: [TAILE'D] Best Social Media Post)*
**Sponsor tools:** Streamlit (Whole app and hosting, core)
**AI:** No trained model shipped; predictive analytics is a beta metric, supervised ML listed as future work.
**Architecture:** Single Streamlit app: Cloudscraper and requests fetch airport flights, pandas shapes data, Streamlit renders and hosts it; devcontainer config included.
**Novelty:** Niche use case: connects airport flight schedules to concession planning using scraped data.
**Scope:** tiny · working: Hosted streamlit.app link; repo about 550 LOC across 11 files. · polish: Clean UI claimed; no screenshots or video; README absent from evidence.
**Gaps:** Devpost 'what it does' empty; LinkedIn post not found
Sources: https://devpost.com/software/restoport, https://conuhacks-ix.devpost.com/, evidence file

---

### UrbanCanvas
*ConUHacks ConUHacks IX · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** DRW - 4x JBL Speakers for 1st Place

**What it is:** React web app that plots Montreal murals, public art and cultural landmarks on a Google Map, with filters and a fastest-route custom tour generator, backed by Node.js and MongoDB loaded from city open datasets.
**Problem / user:** Tourists and residents who want to find and explore Montreal's public art and heritage sites.

**Features**
- Map of murals, art and landmarks — Pins for all three datasets on Google Maps. *[shown_working]*
- Category sorting — Switch between murals, public art and significant landmarks. *[shown_working]*
- Filters — Filter by artist, year, borough (19) and type. *[claimed]*
- Pin details — Click a pin to see information about the work or site. *[claimed]*
- Fastest custom tour route — Generates the quickest route through chosen stops. *[claimed]*

**Flow:** Open the map → Choose a category and filters → Click pins for details → Build a custom tour and get the fastest route

**Prompt:** DRW prize listing: 4x JBL speakers for 1st place; team describes the challenge as using large datasets.
**Fit (explicit):** Merges three City of Montreal open datasets (a fourth dropped) into one map experience; also motivated by MLH's MongoDB prize.  *(targeted: DRW - 4x JBL Speakers for 1st Place)*
**Sponsor tools:** MongoDB (database for the city art datasets, core)
**AI:** none
**Architecture:** MongoDB loaded with city open data, Node.js API, React frontend using Google Maps API.
**Novelty:** Combines three municipal art and culture datasets into route-planning tour; team notes Leaflet would have been cheaper than Google Maps.
**Scope:** small · working: Screenshots of map, tour and filters; ~1.6k LOC plus a large backend data folder; tests present. · polish: Logo and legend panel; lists data inconsistency and caching issues.
**Claims:** No merge conflicts, smooth integration
**Gaps:** README says four datasets but names three; No demo link
Sources: https://devpost.com/software/urbancanvas, evidence/conuhacks-conuhacks-ix-urbancanvas.json

---

