# ConUHacks — ConUHacks X (31 projects)

### AeroGuard.tech
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [MLH] Best Use of Snowflake API

**What it is:** An incident-response decision-support dashboard (also called A.E.G.I.S. Garden on the page) that triages alerts with Gemini, streams updates over WebSockets, voices critical alerts, stores incidents in MongoDB and records audit proof on Solana.
**Problem / user:** Disaster-response and cybersecurity teams facing noisy alerts, slow coordination and trust problems around aid funds.

**Features**
- Explainable AI triage — Gemini or OpenRouter LLM scores priority and confidence with a readable rationale, plus self-validation *[shown_working]*
- Real-time incident stream — FastAPI WebSocket pushes MongoDB change updates to the React dashboard *[shown_working]*
- Snowflake analytics — Snowpipe streaming, Cortex impact prediction and ranking, forecasting *[claimed]*
- Vector and geo search — MongoDB Atlas vector search matches incidents to responders; Ottawa-bounded map queries *[shown_working]*
- Voice alerts — ElevenLabs speaks high and critical incidents with opt-in and rate limiting *[claimed]*
- Solana audit and aid controls — On-chain verification, transfer hooks, time-locked funds, compressed NFT responder identity, Blinks *[claimed]*
- Demo/real mode switch with mocks — MODE flag and mock Gemini, Mongo and ElevenLabs for development *[shown_working]*

**Flow:** Run API and dashboard (demo mode available) → Incidents appear on Ottawa map and list → AI triage assigns priority and rationale → Critical incidents trigger audio alert → Analyst checks proof and audit trail

**Prompt:** MLH Best Use of Snowflake API: use Snowflake's REST APIs to access LLMs, for example RAG chatbots; Arduino Tiny ML kit prize.
**Fit (implied):** Page describes Snowflake streaming ingestion, Cortex prediction and ranking and External Functions as part of the pipeline, though the repo README stresses Gemini and MongoDB.  *(targeted: [MLH] Best Use of Snowflake API)*
**Sponsor tools:** Snowflake (Streaming ingestion, Cortex impact prediction, forecasting, supporting); MongoDB Atlas (Incident storage, change streams, vector and geo search, core); ElevenLabs (Spoken alerts for critical incidents, supporting); Solana (Audit verification and fund controls, supporting); Gemini (Triage reasoning and function calling, core)
**AI:** Gemini triage with confidence, function calling and self-validation; OpenRouter routes models by cost and latency; embeddings power vector search; Cortex for forecasting.
**Architecture:** Monorepo: FastAPI API, React/Vite dashboard, Solana demo package. MongoDB change streams feed WebSocket UI; Snowflake handles analytics; scripts switch demo and production modes.
**Novelty:** Very broad integration of many sponsor stacks in one monorepo with proof tooling and tests; large codebase for a hackathon.
**Scope:** large · working: About 500 files and 75k LOC, tests present, .env.example, demo mode; video linked, no live demo. · polish: Detailed README, proof system, mode scripts; Devpost text mixes names and skips challenges.
**Claims:** Edge nodes detect disasters offline (tagline only, no detail)
**Gaps:** Many claimed features unverified; Video not watched; Edge hardware unexplained
Sources: https://devpost.com/software/aeroguard-tech, https://conuhacks-x.devpost.com/, evidence file

---

### Banq Pirate
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Desjardins - Sponsor Challenge

**What it is:** Android banking app that adapts to its surroundings: a dark stealth mode in low light and a jungle mode that uses the camera to read hand signs for hands-free transactions, with ElevenLabs voice output.
**Problem / user:** Banking interfaces are static; helps people in dark places, those unable to touch the screen, and users with sight difficulties.

**Features**
- Low-light stealth mode — Phone detects low luminosity and switches to a dark interface. *[claimed]*
- Jungle mode hand gestures — Camera activates and Google AI Edge gesture recognition accepts up to 5 hand signals for transactions. *[claimed]*
- AI voice output — ElevenLabs reads responses aloud for accessibility. *[claimed]*
- Core banking screens — Login, dashboard and money transfer screens with SQLite storage. *[shown_working]*

**Flow:** Log in → See dashboard → Phone senses light or touch availability and changes mode → Use gestures or voice to transfer money

**Prompt:** Desjardins sponsor challenge: prepaid-card prizes for 5 winners; page gives no problem text. README says team placed 4th.
**Fit (explicit):** Banking app that reacts to its environment, matching the challenge theme the page cites.  *(targeted: Desjardins - Sponsor Challenge)*
**Sponsor tools:** ElevenLabs (AI voice output, supporting)
**AI:** Google AI Edge hand gesture recognition from the camera; ElevenLabs text-to-speech.
**Architecture:** Native Android (Java/XML) app with camera sensing, SQLite local storage, ElevenLabs API calls; ESP32 hardware planned.
**Novelty:** Gesture and ambient-light driven banking UI aimed at accessibility; hardware plan dropped.
**Scope:** small · working: README lists features; ~1.9k LOC Android with tests; three screenshots. · polish: Claims to run without crashing; no demo video.
**Claims:** Placed 4th in the Desjardins challenge (README)
**Gaps:** Devpost says 'going rogue' and 'jungle' modes; README covers both with slightly different wording
Sources: https://devpost.com/software/banq-pirate, evidence/conuhacks-conuhacks-x-banq-pirate.json

---

### BooBoo Buddy
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Dialogue - Sponsor Challenge

**What it is:** Agentic health assistant: chats to triage symptoms, advises 911 for emergencies, finds nearby clinics via Google Places, and places real Twilio calls to check walk-in availability or appointment slots and then book the chosen time.
**Problem / user:** Sick people who waste hours phoning clinics for same-day care.

**Features**
- Symptom triage chat — GPT-4o-mini via OpenRouter assesses severity and asks follow-ups; voice input via Web Speech API. *[shown_working]*
- Emergency detection — Advises calling 911 when severity warrants. *[claimed]*
- Clinic search — Google Places finds nearby clinics from user location. *[shown_working]*
- Automated inquiry calls — Twilio calls clinic, records, transcribes and an LLM reads walk-in vs appointment answers. *[shown_working]*
- Time-slot picker — Converts phrases like openings between 2 and 5 into 30-minute slots. *[shown_working]*
- Booking and confirmation call — Second call books the chosen slot and confirms. *[shown_working]*
- Health profile personalization — Prisma/SQLite profiles pass context to the LLM. *[claimed]*

**Flow:** Sign in and open chat → Describe symptoms by text or voice → Get severity assessment or 911 advice → Pick a nearby clinic and click call → Choose a slot → Receive booking confirmation

**Prompt:** Dialogue sponsor challenge: prize is Cursor Pro for a year, swag and office visit; no challenge text. Team README frames it as agentic healthcare beyond a chatbot.
**Fit (explicit):** End-to-end virtual-to-physical care handoff: triage, finding clinics, calling and booking; page lists Dialogue integration as next step.  *(targeted: Dialogue - Sponsor Challenge)*
**AI:** GPT-4o-mini via OpenRouter does conversation, symptom extraction, escalation decisions and transcript interpretation; LLM chooses when to call tools.
**Architecture:** Next.js 14 app with workflow state machine, OpenRouter LLM, Twilio telephony with polling for transcripts, Google Places, Prisma+SQLite, deployed on Vercel.
**Novelty:** Makes real outbound phone calls and interprets live human replies rather than simulating; mermaid sequence diagram in README.
**Scope:** medium · working: Live Vercel demo link in README; ~7.7k LOC; tests present; sequence diagram. · polish: GenAI disclosure page, sign-in, slot grid; no quantitative results.
**Claims:** Real calls to real numbers, not simulated | End-to-end automation to confirmed appointment
**Gaps:** Call reliability not measured
Sources: https://devpost.com/software/booboo-buddy, evidence/conuhacks-conuhacks-x-booboo-buddy.json

---

### Buildo
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Gemini API

**What it is:** A web app where a user describes a hardware gadget in plain English and gets a visualization, a priced parts cart, starter firmware, step-by-step illustrated assembly instructions and a demo video.
**Problem / user:** Makers, students and hobbyists who have a device idea but struggle with parts selection, specs and build planning.

**Features**
- Idea to project generation — Prompt hits /generate; Gemini 2.5 Flash selects parts from a scraped catalog and returns structured JSON *[shown_working]*
- Parts cart and checkout — Catalog of 7k+ scraped AliExpress parts ranked by keyword, rating and price *[shown_working]*
- Starter firmware — Snowflake Cortex generates skeleton code to copy *[shown_working]*
- Illustrated assembly steps — Separate Flask microservice generates images in background with Gemini; downloadable *[shown_working]*
- Assembly video demo — Video generation of assembly, credited to Veo *[claimed]*
- Project dashboard and extras — Tabs for inventory, code, assembly, blueprints; profile and arcade section *[shown_working]*

**Flow:** Type a hardware idea → Wait about 30 seconds on loading screen → See visualization, parts cart, code and instructions → Images finish loading in background → Check out parts, copy code, download instructions

**Prompt:** MLH Best Use of Gemini API: push the boundaries of what's possible with AI using Google Gemini; prize Google swag kits.
**Fit (implied):** Gemini 2.5 Flash does parts selection and assembly image generation, the core of the product; Snowflake Cortex also used for instructions.  *(targeted: [MLH] Best Use of Gemini API, [MLH] Best .Tech Domain Name (hosted on a .tech domain))*
**Sponsor tools:** Gemini API (Parts selection and assembly image generation, core); Snowflake Cortex (Assembly instructions and firmware text, core); MongoDB Atlas (Optional sync of scraped catalog, token)
**AI:** Gemini 2.5 Flash with structured JSON prompts for parts and images; Snowflake Cortex for instructions and code; token use cut about 70% by sending only part names; Veo credited for video.
**Architecture:** Next.js frontend on Railway; Flask main API on 5000 plus assembly-image microservice on 5001; BeautifulSoup-scraped parts_catalog.json; responses cached by description hash.
**Novelty:** End-to-end idea-to-build kit including real purchasable parts, firmware, images and video, using a self-scraped catalog of tens of thousands of products.
**Scope:** medium · working: Live .tech site, 12k LOC repo across frontend, backend, image service; YouTube demo. · polish: Retro NES styling, progressive loading, caching, docs folder; no tests; README short.
**Claims:** Scraped ~36-37k products, 7k+ curated | Cut token counts about 70% | Cut user wait from about 4 minutes to about 30 seconds
**Gaps:** Live site not opened; Veo use only from bio
Sources: https://devpost.com/software/product-creator-temp-name-conu-x, https://conuhacks-x.devpost.com/, evidence file

---

### CodeMafia
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Druide – Best Use of Language (Presentation)

**What it is:** Browser multiplayer social-deduction game for 3-5 players where civilians collaboratively fix broken Python code in a shared editor while a hidden impostor sabotages it; emergency meetings let players vote someone out.
**Problem / user:** Makes debugging the gameplay; for developers and fans of Among Us-style games.

**Features**
- Lobby and category voting — 3-5 players join and vote on a problem category. *[shown_working]*
- Hidden impostor role — One player secretly sabotages code; roles shown at start. *[shown_working]*
- Collaborative code editing — Monaco editor with real-time sync over Partykit. *[shown_working]*
- In-browser Python tests — Pyodide runs tests client-side; passing all tests wins for civilians. *[shown_working]*
- Sabotage verification — Checks that impostor changes break code in specific ways. *[claimed]*
- Emergency meetings and voting — Discussion phase ends with vote to eject. *[shown_working]*
- Animated menu — Wandering animals, birds and rain. *[shown_working]*

**Flow:** Open main menu → Join lobby → Vote category → See role → Edit code and run tests → Call emergency meeting and vote → Game ends on win condition

**Prompt:** Druide Best Use of Language (Presentation): prize is Antidote+ Personal per member; no description text found.
**Fit (implied):** Uses programming language (Python) as the game's core mechanic; page does not state the connection.  *(targeted: Druide – Best Use of Language (Presentation))*
**AI:** none
**Architecture:** React/TypeScript/Vite client with Zustand and Framer Motion; Partykit WebSocket rooms sync state; Monaco editor; Pyodide WebAssembly for Python execution, deployed on Vercel.
**Novelty:** Fuses social deduction with live coding and runs validation entirely in the browser with no backend.
**Scope:** medium · working: Live demo at codemafia.vercel.app; 25 Devpost likes; team claims dozens of playtests. · polish: Animated menu and fixes for cursor jumping and flicker.
**Claims:** Python tests run surprisingly fast in browser | Dozens of test playthroughs
**Gaps:** Clone failed; repo README unreachable via raw and github.com WebFetch; Language count and sabotage rules unseen
Sources: https://devpost.com/software/codemafia

---

### D3CISION
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** D3 Security - Sponsor Challenge

**What it is:** Security-operations triage dashboard that groups raw alerts into 'attack stories', scores them with XGBoost, explains scores with SHAP, ranks them in a 3D Gravity Stack, and lets analysts or a Gemini agent isolate hosts or block traffic.
**Problem / user:** SOC analysts face more alerts than they can investigate and lack context.

**Features**
- Story correlation — Entity affinity, temporal clustering and NetworkX graphs group events into stories. *[shown_working]*
- XGBoost threat scoring — 50+ engineered features such as bursts and external IPs score each event. *[shown_working]*
- SHAP explanations — Shows which features drove each score. *[shown_working]*
- Gravity Stack — Animated 3D view where critical stories rise. *[shown_working]*
- Gemini tactical advisor — Remediation plans, Q&A and investigation paths per story. *[claimed]*
- Response actions — Isolate host and block traffic buttons; natural-language bulk actions logged in MongoDB Atlas. *[claimed]*
- Voice briefings — ElevenLabs narration, toggled by hotkey. *[claimed]*
- Uncertainty flags — Marks low-signal stories for manual review. *[claimed]*

**Flow:** Run pipeline: clean, train, score, correlate, finalize → Open dashboard and see ranked stories → Open story for SHAP and plan → Listen to briefing or ask the agent → Isolate host or block traffic

**Prompt:** D3 Security sponsor challenge: official listing offers an interview with D3 Security and an RSA Conference pass for first place; challenge dataset and rule-based baseline referenced by the team.
**Fit (explicit):** Beats the D3 rule-based baseline (severity, confidence, external IP) with ML scoring and story correlation on the challenge datasets.  *(targeted: D3 Security - Sponsor Challenge)*
**Sponsor tools:** ElevenLabs (voice briefings, supporting); MongoDB Atlas (storing AI plans and actions, supporting); Gemini API (advisor and tactical actions, core)
**AI:** XGBoost scores events; SHAP explains; Gemini generates remediation, Q&A and executes natural-language actions; ElevenLabs narrates.
**Architecture:** Python pipeline (XGBoost, SHAP, scikit-learn, NetworkX) outputs scored events and stories to a Next.js 15 dashboard that calls Gemini, ElevenLabs and MongoDB Atlas.
**Novelty:** Pairs correlation, explainability and an action-taking agent with a cinematic 3D UI; response actions only operate within the app.
**Scope:** large · working: Reported evaluation table and results folder; ~5k LOC; 8 screenshots. · polish: Hotkeys, global entity pivoting, extensive README with architecture.
**Claims:** AUC-ROC 0.9886, F1 0.9627 | 142.5% improvement over baseline | Hundreds of events in under 1 second | 100 alerts to 5 campaigns
**Gaps:** Metric measurement method unspecified; README says Gemini 1.5/2.0 vs page Gemini 3 Flash
Sources: https://devpost.com/software/d3cision, evidence/conuhacks-conuhacks-x-d3cision.json

---

### Desjardins ConUHacks Adventure Banking App
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence low*
**Prizes:** Desjardins - Sponsor Challenge

**What it is:** Treasure-hunt themed banking app for Desjardins: normal withdraw, deposit and invest actions plus camouflage that blends the display with camera colors, a compass for a second device, hands-free voice control, and ML detection of a second viewer to hide details.
**Problem / user:** Page states none; framed around Desjardins' chameleon challenge, protecting users in risky or adventurous situations.

**Features**
- Core banking — Withdraw, deposit and invest. *[claimed]*
- Camouflage display — Blends app colors with those the camera sees. *[claimed]*
- Compass — Acts as a compass for a second device. *[claimed]*
- Voice control — Hands-free commands in sticky situations. *[claimed]*
- Shoulder-surfing privacy — ML detects another person and hides user details. *[claimed]*

**Flow:** Page gives none; general behavior only

**Prompt:** Desjardins sponsor challenge (called 'Chameleon's Eye' on the page): prepaid-card prizes; no official problem text found.
**Fit (explicit):** Adapts the banking UI to the environment and hides data from onlookers.  *(targeted: Desjardins - Sponsor Challenge)*
**AI:** Unnamed machine-learning software for second-person detection and adventuring functions; Expo used for some features.
**Architecture:** Web front end (HTML/CSS/JS) with Expo-based components; Raspberry Pi sensor plan abandoned. Repo shows treasure-compass, TreasureBankMainWindow and Brightness folders.
**Novelty:** Treasure-hunt metaphor with camouflage and compass beyond normal banking; hardware pivot.
**Scope:** small · working: No demo, video or screenshots described; repo ~2.9k LOC with Docker devcontainer. · polish: README is a placeholder.
**Claims:** Delivered a finished project the team was satisfied with
**Gaps:** README placeholder; Implementation of features not verified; Stack ambiguous between page and repo
Sources: https://devpost.com/software/desjardins-conuhacks-adventure-banking-app, evidence/conuhacks-conuhacks-x-desjardins-conuhacks-adventure-banking-app.json

---

### Desjungles
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Desjardins - Sponsor Challenge

**What it is:** Expo React Native banking app with a jungle theme: transfer between own accounts or to others, Spy Mode that switches to spoken banking when multiple people look at the screen, ambient-light theming, and motion-triggered jungle scene.
**Problem / user:** Banking safely in varied environments; inspired by Desjardins values of security, inclusivity and accessibility.

**Features**
- Money transfers — Between own accounts and to another person. *[shown_working]*
- Spy Mode — BlazeFace detects more than one viewer and switches to text-to-speech banking. *[claimed]*
- Ambient-light theme — Light level sets light or dark mode. *[claimed]*
- Motion jungle mode — Moving user sees jungle environment and locked Home screen. *[claimed]*
- Per-screen light and dark — Login, home, accounts and transactions in both themes. *[shown_working]*

**Flow:** Log in → Home and account views → Send or transfer money → Spy or motion mode activates automatically

**Prompt:** Desjardins sponsor challenge: prepaid cards; no problem text found.
**Fit (explicit):** Environment-aware banking UI with privacy and accessibility angles.  *(targeted: Desjardins - Sponsor Challenge)*
**AI:** BlazeFace face detection for multiple viewers; Whisper listed in stack, use unclear.
**Architecture:** React Native/Expo TypeScript app, Node.js backend with MongoDB.
**Novelty:** Sensors drive the UI theme and privacy behavior; gamified jungle.
**Scope:** medium · working: 10 screenshots; ~4.2k LOC app/backend; tests present; no demo video. · polish: Light/dark per screen; platform differences noted.
**Gaps:** README is Expo boilerplate; Whisper use unclear
Sources: https://devpost.com/software/desjungles, evidence/conuhacks-conuhacks-x-desjungles.json

---

### Donair
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Talsom - Sponsor Challenge; Front Row Ventures - Investor Pitch Award

**What it is:** Agentic fundraising platform for events: discovers donors via semantic search over 110,000+ past donations and web search, scores leads, tracks them in a kanban pipeline, and runs live Solana Pay QR donations with incentive trackers.
**Problem / user:** Event fundraisers who manually research donors and chase big sponsors.

**Features**
- Donor discovery — Gemini embeddings and pgvector match the event to historical recipients plus web search. *[shown_working]*
- Agent chat — Gemini 2.5 Flash with tools find_similar_recipients, search_web, get_event_leads and save_lead. *[claimed]*
- Lead scoring — Capacity, affinity and timeliness 0-100 combined to a relevance score. *[claimed]*
- Kanban pipeline — Discovered, Contacted, Negotiating, Confirmed with ethics flags. *[claimed]*
- Solana Pay donations — QR codes, live transaction monitoring, multi-currency to SOL. *[claimed]*
- Live feed and incentive trackers — Realtime updates via Supabase. *[claimed]*
- News monitoring and analytics — Tracks awards, appointments, grants; post-event analytics. *[claimed]*

**Flow:** Create event → Discover donors → Go live for donations → Track progress → Manage leads → Review analytics

**Prompt:** Talsom sponsor challenge ($100 prepaid per member, no text); Front Row Ventures Investor Pitch Award: 30-minute pitch meeting with the investment team.
**Fit (implied):** Pitched as a business product with donor-discovery agent and payments; Solana Pay also fits the MLH Solana prize.  *(targeted: Talsom - Sponsor Challenge, Front Row Ventures - Investor Pitch Award)*
**Sponsor tools:** Solana Pay / web3.js (live donations and tx monitoring, core); Gemini API (matching, agent, core)
**AI:** Gemini 2.0/2.5 Flash for matching, SQL generation and tool-calling agent; text-embedding-004 vectors in pgvector.
**Architecture:** Next.js 16 frontend and API routes plus Express; Supabase Postgres with pgvector, RLS and Realtime; Solana mainnet; deployed on Vercel.
**Novelty:** Combines donor research agent, vector search over charity data, and crypto payments in one event workflow.
**Scope:** large · working: Live demo donair.tech and YouTube video; ~14.6k LOC; embedded README video. · polish: Offline fallback, demo mode for WebSocket failures, README.
**Claims:** Indexed 110,000+ donations | Cosine threshold 0.3
**Gaps:** Devpost URL slug 'flowstate' differs from name Donair
Sources: https://devpost.com/software/flowstate-7ihg10, evidence/conuhacks-conuhacks-x-donair.json

---

### Dr.Bob
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Dialogue - Sponsor Challenge

**What it is:** Mobile-style web chat for symptom triage with Gemini, location-aware nearby clinic finding, a saved medical profile that can be shared with clinics, a trusted clinic list, and a polished light/dark UI.
**Problem / user:** Sick people who want guidance without navigating healthcare portals or phone holds.

**Features**
- Symptom triage chat — LLM chat gives immediate guidance. *[claimed]*
- Nearby clinics — Browser Geolocation finds clinics. *[claimed]*
- Medical profile — Pop-up stores conditions and shares them in appointment requests. *[claimed]*
- Trusted clinics whitelist — Faster prioritization. *[claimed]*
- Auth and relational storage — Flask backend with sessions, conversations and conditions. *[claimed]*
- Theme engine and animations — CSS variables, glass panels, blurred sidebar. *[shown_working]*
- Direct booking — Booking via clinic APIs is listed as future work. *[planned]*

**Flow:** Open app → Describe symptoms → Allow location → Save trusted clinics → Update profile → Request appointment

**Prompt:** Dialogue sponsor challenge: Cursor Pro, swag, office visit; no challenge text.
**Fit (implied):** AI health navigation with clinic discovery and profile sharing; booking not yet built.  *(targeted: Dialogue - Sponsor Challenge)*
**AI:** LLM chat engine (Gemini tag) for medical reasoning.
**Architecture:** Vanilla HTML/CSS/JS frontend, Flask backend with relational DB, Geolocation API.
**Novelty:** Emphasis on UI craft; page text inconsistent on automatic scheduling.
**Scope:** small · working: Two screenshots only; no demo. · polish: Detailed theme and animation work.
**Claims:** Highly reactive theme engine
**Gaps:** Repo clone failed, README unreachable; Page mentions Maps/Mixpanel keys unexplained
Sources: https://devpost.com/software/dr-bob

---

### Drop'edthe.tech
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Deck - Sponsor Challenge

**What it is:** Automation suite for the Concordia Deckathon challenge portal: a pure-API script that registers, logs in, drops classes, pays fees and finalizes dropout by defeating the portal's verification puzzles, plus an Electron app and landing page.
**Problem / user:** Concordia students who want to drop courses quickly; targets a mock challenge portal, not the real university site.

**Features**
- Pure-API dropout script — Registers, logs in, drops classes, pays and finishes dropout. *[shown_working]*
- Anti-bot module solving — Handles 12 verification modules via API or DOM. *[shown_working]*
- CAPTCHA strategies — sharp pixel analysis, Gemini vision, parallel brute force of 512 combinations. *[shown_working]*
- Electron app — Desktop wrapper packaged as exe. *[shown_working]*
- Puppeteer result view — Shows completed message. *[shown_working]*
- Landing site — React site hosts download. *[shown_working]*
- Add classes — Planned. *[planned]*

**Flow:** Download from site → Run Electron app or script → Script walks portal → Browser shows completion

**Prompt:** Deck sponsor challenge: first place $1,500 USD plus skateboard deck for a solo participant; no challenge text.
**Fit (explicit):** Solves Deckathon portal puzzle gauntlet end to end; explicit via README Deckathon framing.  *(targeted: Deck - Sponsor Challenge)*
**AI:** Gemini Flash vision to identify crowds; no other AI.
**Architecture:** Node script plus Puppeteer, Electron/React frontend, landing site.
**Novelty:** Races a gamified bot-detection obstacle course; targeted at a purpose-built demo portal.
**Scope:** medium · working: Demo video and site; README table of modules; ~6.8k LOC. · polish: Packaged executable and site.
**Claims:** Solves over 12 verification modules
**Gaps:** Devpost says demo site not real Concordia
Sources: https://devpost.com/software/drop-edthe-tech, evidence/conuhacks-conuhacks-x-drop-edthe-tech.json

---

### FOMO
*ConUHacks ConUHacks X · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** [HackConcordia] Best Beginner (All team members must be first-time hackers)

**What it is:** A beginner-built iOS app (Swift, Firebase) that opens on a map of busy gathering spots, lets you tap a hotspot to see what people there are discussing, and ask the crowd a location-tied question.
**Problem / user:** People who feel isolated and do not know where gatherings are happening or how to join; businesses are a later audience.

**Features**
- Hotspot map — Map shows high-energy areas using live location data *[claimed]*
- Hotspot conversation view — Tapping a hotspot shows what people there discuss *[claimed]*
- Passive browsing — Watch and listen without joining *[claimed]*
- Location-tied questions — Ask the crowd at a hotspot, stored in Firestore *[claimed]*
- User tracking and location permissions — Permission flow and flow tracking *[claimed]*
- Profiles, friends, roles, business locations — Future extensions *[planned]*

**Flow:** Open app to the map → Tap a hotspot → Read what people are discussing → Optionally ask a question tied to the place

**Prompt:** HackConcordia Best Beginner: all team members must be first-time hackers; misrepresentation leads to disqualification.
**Fit (explicit):** Page states all members were first-time hackers and finished a working multi-feature iOS app despite limited Macs and Git conflicts.  *(targeted: [HackConcordia] Best Beginner)*
**AI:** ChatGPT listed in built-with but no stated role.
**Architecture:** Swift iOS client in Xcode talking to Firebase/Firestore for live location and discussion data, with a map API.
**Novelty:** Frames social discovery around live crowd conversation rather than event listings; built by a first-time team on mobile.
**Scope:** small · working: Repo exists but clone failed so unseen; team says features and full flow tested in Xcode simulator. · polish: No video, demo or screenshots described; unclear.
**Gaps:** Repo clone failed; No demo or video
Sources: https://devpost.com/software/fomo-91dnsu, https://conuhacks-x.devpost.com/

---

### HealthMe
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** MentorMates - Sponsor Challenge; Dialogue - Sponsor Challenge

**What it is:** Voice-first health assistant: spoken symptom chat with Gemini using health history, a clinic map, and an ElevenLabs agent that phones a clinic to book while user watches a live transcript; also has emergency calling.
**Problem / user:** People who need nearby care and want it booked hands-free.

**Features**
- Context-aware chat — Gemini uses history, vitals, symptoms. *[claimed]*
- Clinic map — Mapbox shows nearby care. *[claimed]*
- AI phone calls — Agent calls clinic and books. *[claimed]*
- Live transcript — Socket.io streams the call. *[claimed]*
- Emergency calling — For urgent situations. *[claimed]*
- Voice interaction — Speech in and TTS out. *[claimed]*
- Firestore storage — Chat history and profiles. *[claimed]*

**Flow:** Speak symptoms → Hear reply → See clinics on map → Start AI call → Watch transcript until booked

**Prompt:** Dialogue: Cursor Pro, swag, office visit; MentorMates: $25 Amazon cards; no challenge text.
**Fit (implied):** AI health navigation with real booking calls.  *(targeted: MentorMates - Sponsor Challenge, Dialogue - Sponsor Challenge)*
**Sponsor tools:** ElevenLabs (voice and phone agent, core)
**AI:** Gemini chat plus ElevenLabs conversational phone agent.
**Architecture:** React frontend, Flask/Express backend, Socket.io, Twilio, Firestore, GCP.
**Novelty:** Combines voice chat, map and live-transcribed call.
**Scope:** medium · working: ~10.5k LOC; no demo video. · polish: README is AI Studio boilerplate.
**Claims:** Makes real calls, not mockups
**Gaps:** Backend stack inconsistent on page
Sources: https://devpost.com/software/healthme-cshbay, evidence/conuhacks-conuhacks-x-healthme.json

---

### I LOST IT
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SAP - Sponsor Challenge

**What it is:** A multimodal lost-and-found web app where owners search found items by text, photo or both, and staff manage inventory. Four embedding collections are fused into ranked matches, and Gemini produces captions, OCR and ownership-verification questions to deter false claims.
**Problem / user:** People who lost items and staff at campuses, gyms and workplaces who manually match vague descriptions against cluttered bins of unclaimed items.

**Features**
- Multimodal search by text, image or both — Query runs against four Milvus vector collections (DINOv2 image, CLIP image, CLIP caption, sentence-embedding text) at once *[claimed]*
- Weighted score fusion — Scores from the four matching paths are combined with tuned weights into one ranked result list, filterable by collection and location *[claimed]*
- Gemini captioning, OCR and follow-up questions — Gemini 2.0 Flash with structured Pydantic output describes found-item photos and asks clarifying questions *[claimed]*
- Ownership-verification questions — Questions only the true owner could answer are generated to block fraudulent claims *[claimed]*
- Staff assistant portal — Staff organize items into location collections, review matches and manage inquiries *[claimed]*
- Inquiry tracking and match notifications — Real-time status of a lost-item inquiry for the owner *[claimed]*
- Mobile-first UI — Next.js, Tailwind, shadcn/ui and Framer Motion front end with Supabase auth and image hosting *[shown_working]*

**Flow:** User snaps a photo and/or types a description of the lost item → System searches the four vector collections and fuses scores → Gemini asks follow-up questions to refine → Verification questions are generated for the owner to answer → Ranked candidate matches are returned and the inquiry is tracked → Staff review matches and manage collections in their portal

**Prompt:** SAP sponsor challenge at ConUHacks X: CAD 400 total across 3 winners; 1st gets $100 Amazon gift cards plus lunch with SAP Montreal executives and hiring managers, 2nd/3rd lunch only. The Devpost page gives no problem statement.
**Fit (implied):** Page says it won the SAP challenge; it is an AI-assisted lost-and-found matcher, but the brief is not public and SAP products are not used.  *(targeted: SAP - Sponsor Challenge)*
**AI:** DINOv2, CLIP and Sentence-Transformers embeddings in Milvus for cross-modal retrieval with weighted fusion; Gemini 2.0 Flash for captions, OCR, follow-up and verification questions via structured output.
**Architecture:** Next.js frontend on Vercel with Supabase auth/storage; FastAPI backend (PyTorch) embeds images and text, queries four Milvus collections, merges scores, and calls Gemini.
**Novelty:** Fuses four separate embedding spaces (image-image, image-caption, text-image, text-text) instead of one, and adds owner-verification question generation.
**Scope:** medium · working: Live Vercel demo link and ~8.8k LOC repo with frontend plus FastAPI server; no video. · polish: Mobile-first animated UI; repo README is the default create-next-app text; no tests.
**Claims:** Combines four matching approaches in one multimodal search | Verification questions help prevent fraudulent claims | No quantitative accuracy metrics reported
**Gaps:** SAP challenge brief text not found; No video; README is boilerplate; Planned: notifications, native apps, QR claim pickup
Sources: https://devpost.com/software/i-lost-it, evidence/conuhacks-conuhacks-x-i-lost-it.json, https://conuhacks-x.devpost.com/

---

### JungleBank
*ConUHacks ConUHacks X · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 3rd Place - General [3rd]; Desjardins - Sponsor Challenge

**What it is:** A gamified banking app that teaches kids and young teens finance: track expenses, buy items to survive, learn about interest, trade stocks, talk to a Gemini AI banker and play Godot mini-games to earn coins.
**Problem / user:** Children and young teens who need financial literacy; built for the Desjardins sponsor challenge.

**Features**
- Expense tracking and store — Users manage spending and buy items to stay alive or get bonuses *[shown_working]*
- Interest and stock investing — Invest page and Stock Market screen *[shown_working]*
- Godot mini-games — Collect coins and find treasure chests to earn money, written in GDScript *[shown_working]*
- Gemini AI Banker — Chat assistant answers finance questions *[shown_working]*
- Voice navigation — Accessibility mode to use the app by speech *[claimed]*
- Light/dark by time of day — Scene changes with device time *[claimed]*
- Coin transfer — Transfer screen *[shown_working]*

**Flow:** Open home page → Check expenses and buy items → Play coin-collecting game → Invest in stocks or transfer coins → Ask the AI banker

**Prompt:** Desjardins sponsor challenge listed with prepaid-card prizes only; no problem statement published. Also entered General Challenge, where it placed 3rd.
**Fit (explicit):** Page says it was built for the Desjardins challenge, teaching youth about expenses, interest and investing; the official challenge text was not found.  *(targeted: 3rd Place General, Desjardins - Sponsor Challenge)*
**Sponsor tools:** Gemini API (AI Banker assistant, supporting); ElevenLabs (Voice features listed in built-with, unclear)
**AI:** Gemini powers an in-app AI banker; voice activation via speech tooling; no details of prompting.
**Architecture:** React client with Express server, plus Godot game exported and embedded; deployed on Render.
**Novelty:** Wraps a banking sim in a survival-game theme with real Godot mini-games and speech-only navigation.
**Scope:** medium · working: Live Render demo, 8k LOC repo with client, server and game folders, README screenshots. · polish: Screenshots of six screens; no tests or video; Godot learned on the fly.
**Claims:** Won 3rd place general at ConUHacks 2026
**Gaps:** Desjardins challenge text not found
Sources: https://devpost.com/software/junglebank, https://conuhacks-x.devpost.com/, evidence file

---

### llm in chrome
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence low*
**Prizes:** Deck - Sponsor Challenge

**What it is:** An open-source Chrome extension project positioned as a Claude-in-Chrome alternative that works with any LLM. The Devpost page has only a tagline and a complaint about submission problems; the repo README now describes a later product, Hanzi Browse.
**Problem / user:** Implied: people who want a browser-driving AI assistant but with a model of their choice. The Devpost page states no problem.

**Features**
- Browser agent in Chrome usable with any LLM — Tagline claims an open-source Claude-in-Chrome style assistant that is model-agnostic; providers not named *[claimed]*
- Later README: 24 site playbooks — Per current README, per-site hints (X, LinkedIn, Gmail) auto-load by URL to help the agent finish tasks; belongs to later Hanzi Browse version *[unclear]*
- Later README: MCP sub-agent for coding agents — One setup command wires the browser into Claude Code, Cursor, Codex and others; agent loop reads page, plans, acts, repeats *[unclear]*
- Later README: REST API and SDK — Backend can call runTask in plain English and the user own Chrome executes it *[unclear]*

**Flow:** Install the Chrome extension from the repo → Give the agent a plain-English browser task → Agent loop reads the page, plans, clicks/types/scrolls and returns an answer (per later README)

**Prompt:** Deck sponsor challenge: CAD ~4,079 across 3 winners; 1st (solo) USD 1,500 plus a Deck skateboard and scraper, 2nd USD 1,000, 3rd USD 500. No problem text on the page.
**Fit (none):** No stated connection; the page only shows the winner label and the challenge text is not public.  *(targeted: Deck - Sponsor Challenge)*
**AI:** Tagline says any LLM drives the browser; later README describes an LLM agent loop (read page, plan, act, observe) with managed or bring-your-own-model modes.
**Architecture:** Chrome extension plus (later versions) a native host, server, SDK and landing site; the README describes MCP wiring into coding agents. Hackathon-era structure unclear.
**Novelty:** Open-source, model-agnostic take on a browser-agent extension; repo has since grown into a larger product.
**Scope:** large · working: Repo has ~75k LOC, tests, Docker, npm package and Chrome Web Store link in the current README; hackathon-time state unknown. · polish: Current README is polished with install flow and pricing; Devpost page itself is nearly empty.
**Claims:** Open source and works with any LLM (tagline) | Current README: 24 site playbooks; 20 free tasks/month then $0.05/task
**Gaps:** Devpost page is a tagline plus a rant; README describes a later product so features follow README but are marked unclear for the hackathon version; Deck challenge text not public
Sources: https://devpost.com/software/test-mszpgt, evidence/conuhacks-conuhacks-x-llm-in-chrome.json, https://conuhacks-x.devpost.com/

---

### Love At First Bite
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best .Tech Domain Name

**What it is:** A 'Tinder for restaurants' web app: describe what you crave in plain English, an LLM converts it into Yelp search filters, then you swipe through full-screen restaurant cards to find a match.
**Problem / user:** Groups and individuals suffering decision fatigue over where to eat; Yelp and Maps are information-dense but slow for deciding.

**Features**
- Natural-language search — GPT-4o-mini via OpenRouter outputs a Zod-validated SearchSpec mapping vibes and budget to Yelp categories *[shown_working]*
- Swipe cards — Framer Motion physics swipes on poster-style cards showing name, rating, photo *[shown_working]*
- Yelp Fusion retrieval — Parallel Yelp requests built from parsed spec *[shown_working]*
- Weighted ranking — Score weighted by rating, distance, price fit and other factors; best match shown on result page *[shown_working]*
- Multiplayer consensus and booking — Shared swiping, taste learning, reservation APIs *[planned]*

**Flow:** Describe the meal in plain English → LLM parses into search spec → Yelp results load as cards → Swipe right or left → See best-match result page

**Prompt:** MLH Best .Tech Domain Name: register a .Tech domain for the project; prize a desktop microphone and free .Tech domain for years.
**Fit (implied):** Deployed at loveatfirstbite.tech; page and README do not describe domain use beyond the link.  *(targeted: [MLH] Best .Tech Domain Name)*
**Sponsor tools:** .Tech Domain (Hosting the demo at loveatfirstbite.tech, token)
**AI:** GPT-4o-mini through OpenRouter with strict JSON system prompts converts free text into structured Yelp parameters; Zod validates output.
**Architecture:** Next.js 16 App Router on Vercel; LLM parse then parallel Yelp Fusion calls then scoring in lib/ranking; Tailwind and Framer Motion UI.
**Novelty:** Swipe mechanic applied to restaurant choice with an LLM layer translating subjective vibes into API filters.
**Scope:** small · working: Live .tech site, YouTube video, 3k LOC with tests and docs folder. · polish: Detailed README, screenshots of three pages, error validation; no CI.
**Claims:** Parallel requests can cut response time in half (general claim)
**Gaps:** Site not opened
Sources: https://devpost.com/software/love-at-first-bite-kt3zca, https://conuhacks-x.devpost.com/, evidence file

---

### Nova Legends
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Druide – Best Use of Language (Presentation)

**What it is:** A multiplayer 2D top-down knight shooter with sword and ranged combat, built on a fully custom Java engine. Server-authoritative game state runs on Vultr cloud servers with custom physics, animation, camera, spatial audio, chat and a map generator.
**Problem / user:** Competitive multiplayer gamers who want skill-and-positioning combat; the team also wanted to show a custom engine can beat a generic one for a niche game.

**Features**
- Multiplayer knight arena — Players fight to become the ultimate knight with ranged attacks and sword slashes *[claimed]*
- Server-authoritative networking — Clients send inputs and render; the server computes physics and game state over Java sockets on Vultr *[claimed]*
- Custom 2D physics engine — Collision and movement for top-down gameplay written from scratch *[claimed]*
- Dual-mode camera — Focus Mode for precision combat and Unfocused Mode for map awareness *[claimed]*
- Spatialized audio — Directional sound cues in-game *[claimed]*
- Chat service, scoreboard and map generator — Native chat, live scoreboard and procedurally generated maps *[claimed]*
- Custom animation service and UI framework — Character-state animation and a hand-built UI layer *[claimed]*

**Flow:** Connect a client to the Vultr-hosted server → Spawn into a generated map → Fight other knights with sword and ranged attacks → Use chat and see the scoreboard

**Prompt:** Druide Best Use of Language (Presentation): 2 winners, each team member gets an Antidote+ Personal licence; the page gives no judging description beyond the title.
**Fit (none):** No stated link to the language prize; the page presents a game and engine. Vultr hosting matches the MLH Vultr track but only the Druide prize is listed.  *(targeted: Druide - Best Use of Language (Presentation))*
**Sponsor tools:** Vultr (Hosts the authoritative game server, supporting)
**AI:** none
**Architecture:** Java client renders and sends inputs over sockets to an authoritative Java server on Vultr that runs physics and game state; custom services for animation, camera, audio, chat and map generation.
**Novelty:** Entire engine (physics, networking, animation, audio, UI) written from scratch in Java rather than using an existing game framework.
**Scope:** medium · working: Repo with ~4.5k LOC in Java/Gradle; page claims scoreboard, chat and physics work on a live Vultr server; no demo or video. · polish: One screenshot; empty README; no tests.
**Claims:** 100% custom-made engine | Chat, scoreboard and physics work together on a live Vultr server
**Gaps:** README empty; Prompt text for Druide only a title; Planned: biomes, fire-arrows, battle royale
Sources: https://devpost.com/software/nova-legends, evidence/conuhacks-conuhacks-x-nova-legends.json, https://conuhacks-x.devpost.com/

---

### Nursie
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of ElevenLabs

**What it is:** A privacy-minded elder-care monitoring prototype for Quebec long-term care homes: mmWave radar, floor vibration mat, door and presence sensors and a watch detect falls, while an iPad voice assistant triages resident requests with Gemini.
**Problem / user:** Residents of long-term care (CHSLD) and nursing staff; falls go unwitnessed at night and staffing shortages delay help.

**Features**
- Multi-sensor fall detection — mmWave radar plus vibration mat, with ESP32 nodes publishing to ROS 2 and fused for fall checks *[claimed]*
- Staff alerts — Phone call and prioritized dashboard alert on emergency *[claimed]*
- Resident behavior profile — MongoDB profile with anomaly flags such as night departures *[claimed]*
- Voice assistant — ElevenLabs iPad module for questions, reminders; webhooks send transcripts to backend *[claimed]*
- Gemini triage — Classifies transcripts into priority, intent and summary and escalates critical ones *[claimed]*
- Vital signs and live telemetry — TI mmWave viewer reads breath and heart rate; ROS-to-WebSocket bridge streams to React dashboard *[shown_working]*
- Local privacy design — On-premises LAN via OpenWRT router, no camera, edge processing *[claimed]*

**Flow:** Sensors on ESP32 nodes publish events → System fuses signals and detects falls or anomalies → Staff get phone call and dashboard alert → Resident speaks to iPad voice module → Gemini triages transcript and critical items escalate

**Prompt:** MLH Best Use of ElevenLabs: add realistic AI voice and audio to an app; prize wireless earbuds.
**Fit (implied):** ElevenLabs powers the resident-facing voice interface, with transcripts sent via webhooks to Gemini triage and escalation.  *(targeted: [MLH] Best Use of ElevenLabs)*
**Sponsor tools:** ElevenLabs (Resident voice interface with webhook transcripts, core); Gemini (Transcript triage and escalation, core); MongoDB (Resident profiles and events, supporting)
**AI:** Gemini triages voice transcripts into priority, intent and summary; ElevenLabs conversational voice; local AI claimed to separate soft landings from critical falls.
**Architecture:** ESP32 sensor nodes to ROS 2 to backend WebSocket bridge; FastAPI/Flask with MongoDB; React/Vite dashboard; iPad voice module with ElevenLabs webhooks; WatchApp; private OpenWRT LAN.
**Novelty:** Real multi-sensor hardware stack (mmWave, vibration mat, ROS 2, firmware) plus voice agent, with explicit privacy architecture for Quebec Law 25.
**Scope:** large · working: Repo of 1.3k files and 32k LOC with firmware, tracking, backend, frontend and watch app; demo video linked; Docker included. · polish: Run-all scripts and ROS bridge docs; no tests; no detection accuracy figures.
**Claims:** Compliant by design with Quebec privacy law (Law 25) | Cited fall-hospitalization rise of 47% from 2008 to 2019
**Gaps:** No performance metrics; Video not watched
Sources: https://devpost.com/software/nursie, https://conuhacks-x.devpost.com/, evidence file

---

### One-Man-Crew
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SAP - Sponsor Challenge

**What it is:** A human-in-the-loop lost-and-found system. Students submit an inquiry with photo and description, admins log found items, and image plus text embeddings rank the top five matches for the admin to review, clarify and confirm.
**Problem / user:** Students who cannot get items back even after they are found, and admins who run the lost-and-found process.

**Features**
- Embedding-based matching — Separate image and text embedding services plus Gemini embeddings; cosine similarity with configurable weights ranks inventory *[shown_working]*
- Top-five ranked matches for admin review — Admin clicks Process and sees five best matches by combined text+image score *[shown_working]*
- Clarification questions — Admins can ask the student follow-ups before matching *[claimed]*
- Manual ownership confirmation — Admin selects the best match; nothing auto-resolves *[claimed]*
- Email notification on match — SMTP email sent when inquiry status becomes matched *[claimed]*
- Submission rate limit and linked resolution — 20-second cooldown; resolving an inquiry also resolves the matched inventory item *[claimed]*
- Role logins — Admin and student accounts with an admin inventory page *[claimed]*

**Flow:** Student submits photo and description → Admin adds found items to inventory → Admin presses Process; embeddings are compared → Top five matches shown ranked → Admin picks match; student is emailed → Student claims item; both records resolved

**Prompt:** SAP sponsor challenge at ConUHacks X: CAD 400 total across 3 winners; 1st gets $100 Amazon gift cards plus lunch with SAP Montreal executives and hiring managers, 2nd/3rd lunch only. The Devpost page gives no problem statement.
**Fit (implied):** Won the SAP challenge; builds an AI matcher with admin oversight. Brief not public and SAP tools not used.  *(targeted: SAP - Sponsor Challenge)*
**AI:** Gemini embeddings and image/text embedding microservices compared by cosine similarity with tunable weights; AI only ranks, a human decides.
**Architecture:** React frontend; Flask gateway (port 8029) with JSON storage; separate image-embedding and text-embedding Python services; SMTP email.
**Novelty:** Four-terminal microservice split and deliberate human-in-the-loop design rather than autonomous resolution; built by one developer in about 30 hours.
**Scope:** small · working: Repo of ~4k LOC with working run instructions for four services; no live demo or video. · polish: Clear README with config knobs; no tests; sample credentials appear in README.
**Claims:** Reduces false matches and fraud via human review (not measured)
**Gaps:** SAP brief not public; Page lists SMTP and Gemini without usage detail; no next steps
Sources: https://devpost.com/software/one-man-crew, evidence/conuhacks-conuhacks-x-one-man-crew.json, https://conuhacks-x.devpost.com/

---

### PETER the ProtectoBot
*ConUHacks ConUHacks X · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** [HackConcordia] Best Hardware

**What it is:** A 3D-printed two-wheeled sentry robot with an ESP32-S3 camera that can be driven by hand, follow a pointing finger, or patrol autonomously using a ResNet model trained on maze runs, with a custom op-amp speaker imitating an idling diesel.
**Problem / user:** Homeowners wanting a robot to watch the house while away; also a full-stack robotics proof of concept.

**Features**
- Teleoperation with data recording — Python app drives robot over UDP while logging inputs and video for training *[shown_working]*
- Gesture following — Computer vision tracks the user's index finger and robot follows *[claimed]*
- Autonomous sentry mode — Fine-tuned ResNet imitation-learning policy drives navigation *[shown_working]*
- Latency compensation — Model predicts environment up to 1 second ahead *[claimed]*
- Custom speaker audio — Soldered op-amp circuit plays idling-diesel sound *[shown_working]*
- Custom CAD chassis — Designed in Fusion 360 and 3D printed *[shown_working]*

**Flow:** Choose mode in Python app → Drive manually while recording maze runs → Train the ResNet on collected data → Switch to sentry mode for autonomous maze navigation

**Prompt:** HackConcordia Best Hardware prize (Raspberry Pi 5 AI kit and cash); no separate description on the hackathon page.
**Fit (implied):** A fully custom hardware build: printed chassis, soldered audio circuit, ESP32 firmware and an onboard-camera-driven learned policy.  *(targeted: [HackConcordia] Best Hardware)*
**AI:** Imitation learning: ResNet with pretrained weights fine-tuned on self-collected maze driving data (PyTorch/CUDA), plus finger-gesture vision and short-horizon prediction for lag.
**Architecture:** ESP32-S3-Sense streams camera over UDP to a Python desktop app that runs models and sends control; separate base-controller firmware; training scripts with wandb logging.
**Novelty:** Hardware-heavy: custom CAD, hand-built analog audio and a self-collected imitation dataset all within a day.
**Scope:** medium · working: Repo with firmware, ResNet training, Python app and a 20k-file dataset; Devpost photos of builds and maze runs; no video. · polish: README is a one-line pointer; no tests; photos of poster and final builds.
**Claims:** Won Best Hardware (README also says 1st place)
**Gaps:** No demo video; Model accuracy not given
Sources: https://devpost.com/software/peter-the-protecto-bot, https://conuhacks-x.devpost.com/, evidence file

---

### Pinscher
*ConUHacks ConUHacks X · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 2nd Place - General Challenge [2nd]

**What it is:** A hands-free Mac control app: webcam hand gestures (pinch, swipe, scroll) and natural-language voice commands drive the OS, and a Gemini presenter assistant turns recorded sessions into transcripts, notes and slide decks.
**Problem / user:** People who find computer work manual and tedious, presenters, and users with limited mobility via accessibility modes.

**Features**
- Gesture control — OpenCV hand tracking maps pinch to click or drag, ring-finger swipe to tab switch, scroll and app switching *[shown_working]*
- Voice intents — Vosk offline speech-to-text then Gemini 2.0 Flash parses commands into actions *[shown_working]*
- Presenter assistant — Gemini summarizes recorded video and creates Marp slide decks and speaker notes *[shown_working]*
- One-command demo to PDF — Records demo, muxes it and outputs formatted PDF deck in under 60 seconds *[claimed]*
- Accessibility modes — Dwell-click and sticky keys *[claimed]*
- Electron dashboard — React UI to tune gestures, detector and camera *[shown_working]*

**Flow:** Configure camera and gestures in dashboard → Control slides and apps with hand gestures → Say a command like summarize this meeting → Receive transcript, notes and PDF deck

**Prompt:** General Challenge 2nd place at ConUHacks X (CAD 3,220 and a Steam Deck per member); no theme text.
**Fit (none):** General placement prize without a theme; project is a multimodal gesture and voice computer controller.  *(targeted: 2nd Place General Challenge)*
**Sponsor tools:** Gemini API (Intent parsing and video summarization for slides, supporting)
**AI:** Gemini 2.0 Flash parses natural-language intents into structured action plans and summarizes multimodal video; Vosk handles offline speech; OpenCV for hand tracking.
**Architecture:** Multi-process Python core (Poetry) with a custom bridge issuing macOS mouse and keyboard events; Electron/React dashboard; Marp CLI for decks; gesture_model folder.
**Novelty:** Combines gesture OS control, voice intent parsing and automatic deck generation, including playing Wordle without touching the keyboard.
**Scope:** medium · working: 7k LOC repo with gesture_model, frontend and OS link; screenshots on Devpost; no video. · polish: Long feature list in README exceeds what is demonstrated; Mac only; no tests.
**Claims:** Demo recorded and turned into PDF deck in under 60 seconds
**Gaps:** README feature list partly aspirational; No video
Sources: https://devpost.com/software/pinscher, https://conuhacks-x.devpost.com/, evidence file

---

### retro secrets
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Solana

**What it is:** A social platform where users generate AI ASCII art with Gemini, hide an AES-encrypted message in the character colours via LSB steganography, mint it on Solana for proof of creation, and set countdowns before the secret reveals.
**Problem / user:** Friends, followers and creators who want playful hidden messages such as teasers or postcards; no formal problem stated.

**Features**
- AI ASCII art generation — Gemini 2.5 Flash Image with prompt augmentation, converted by ascii-magic *[shown_working]*
- Hidden message encoding — AES-encrypted text embedded in character colours with LSB encoding; reveal reverses it *[shown_working]*
- Solana storage and verification — Art hash stored on chain for creation time and ownership; re-hash to verify *[shown_working]*
- Social feed — Browse friends' and public creations with comments *[shown_working]*
- Interest recommendations — Clustering algorithm suggests art *[claimed]*
- Countdown reveals — Timer hides secret until unlock; users subscribe to countdowns *[shown_working]*
- Phantom wallet login — Connect wallet *[shown_working]*

**Flow:** Connect Phantom wallet → Prompt Gemini for art → Convert to ASCII and embed secret → Store on Solana and post to feed → Set countdown; others reveal after it ends

**Prompt:** MLH Best Use of Solana: use Solana's fast execution and low transaction costs for apps such as games, DEXs or payment prototypes; prize a Ledger Nano S Plus.
**Fit (implied):** Art is stored on Solana for verifiable timestamps and ownership, with wallet connect and hash verification; the chain underpins the NFT concept.  *(targeted: [MLH] Best Use of Solana)*
**Sponsor tools:** Solana (On-chain art storage, timestamp and ownership proof, core); Gemini API (Image generation, core)
**AI:** Gemini 2.5 Flash Image generates art from prompts, augmented for ASCII-friendly output; clustering algorithm for recommendations.
**Architecture:** Next.js/TypeScript frontend, FastAPI and MongoDB backend, Gemini image generation, ascii-magic conversion, LSB plus AES steganography, Solana program with Phantom wallet.
**Novelty:** Unusual mix of ASCII art, colour-channel steganography, time-locked reveal and NFT social feed.
**Scope:** medium · working: 6k LOC repo with backend, app, test-ledger; demo video; screenshots show generate, social and verify pages. · polish: Next.js template README plus feature list; no tests; no live demo.
**Gaps:** Video not watched
Sources: https://devpost.com/software/retro-secrets, https://conuhacks-x.devpost.com/, evidence file

---

### Scale Or Fail
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Vultr

**What it is:** A voice-first system design interview trainer: the user explains an architecture aloud, speech is transcribed, Snowflake agent procedures with RAG grade it and ask follow-ups, ending in a scaled or failed verdict.
**Problem / user:** Engineers preparing for system design interviews who lack spoken, high-pressure practice beyond static reading.

**Features**
- Spoken practice session — User gets a prompt and talks; Azure STT via Python runner transcribes in real time *[shown_working]*
- Snowflake grading agents — Six SQL/Python procedures evaluate transcript, check bottlenecks and decide scaled or failed *[claimed]*
- RAG critique — System design PDFs from Vultr storage loaded into a Snowflake knowledge base, retrieved by cosine similarity *[claimed]*
- Follow-up questions with voice — Spoken via the faster of ElevenLabs or a Vultr GPU TTS deployment *[claimed]*
- Dashboard and history — Auth0 login with persistent session feedback *[shown_working]*
- CI/CD to Vultr — GitHub Action builds three Docker images and Watchtower redeploys *[shown_working]*

**Flow:** Sign in via Auth0 → See dashboard → Start session with architecture problem → Explain design aloud → Answer follow-up questions → Get graded result and saved feedback

**Prompt:** MLH Best Use of Vultr: use Vultr cloud infrastructure including one-click deployment and GPU instances; prize portable screens.
**Fit (explicit):** Runs on Vultr compute instances and VM, uses Vultr Object Storage, Container Registry and a GPU serverless inference TTS deployment.  *(targeted: [MLH] Best Use of Vultr)*
**Sponsor tools:** Vultr (Compute VM, object storage, container registry, GPU TTS inference, core); Snowflake (Agent procedures and RAG knowledge base, core); ElevenLabs (Text-to-speech option, supporting); MongoDB (Listed; role unclear, unclear)
**AI:** LLM agents inside Snowflake grade transcripts against rubrics with RAG over system design PDFs; Azure speech-to-text; dual TTS providers; Whisper planned.
**Architecture:** Angular frontend, .NET 10 API with Auth0, Python STT runner, Snowflake stored procedures, Docker containers on Vultr with Watchtower pulling from Vultr registry, .tech domain SSL.
**Novelty:** Uses Snowflake as the agent runtime and races two TTS providers for latency; production-style CI/CD and tests for a hackathon.
**Scope:** medium · working: 9k LOC repo with tests, Docker, CI and env example; demo link; four screenshots. · polish: Auth, history, deploy pipeline; README is Angular boilerplate; no video.
**Claims:** System design interview invitations up over 100% since 2024 (cites HackerRank)
**Gaps:** Live demo not opened; STT provider description inconsistent
Sources: https://devpost.com/software/system-design-90lx1y, https://conuhacks-x.devpost.com/, evidence file

---

### Schooless
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence low*
**Prizes:** Deck - Sponsor Challenge

**What it is:** A repo with an Angular front end (folder named dropout-simulator), a Python server and a Playwright-Python folder. The Devpost page is nearly empty, giving only the tagline 'Devtools Network AI' and a tech list.
**Problem / user:** Not stated on the page.

**Features**
- Angular client — Front end handles user interaction and content presentation; app served locally on port 4200 *[unclear]*
- Python backend — Handles data, progress tracking and logic per the page; server started with server.py *[unclear]*
- Playwright-Python scripts — Folder present in repo; purpose not documented *[unclear]*

**Flow:** Start the Python server → Start the Angular client and open localhost:4200

**Prompt:** Deck sponsor challenge: CAD ~4,079 across 3 winners; 1st (solo) USD 1,500 plus Deck skateboard and scraper, 2nd USD 1,000, 3rd USD 500. No problem text on the page.
**Fit (none):** Repo description says 'Deck sponsor challenge'; no description of how the project addresses it.  *(targeted: Deck - Sponsor Challenge)*
**AI:** Only the 'Network AI' tagline and a 'clip' tag; no AI details.
**Architecture:** Angular client talking to a Python server (MongoDB and Amazon EC2 listed in built-with); Playwright-Python folder.
**Novelty:** Insufficient description to judge; folder name suggests a dropout simulator.
**Scope:** small · working: ~2k LOC repo with client, server and tests flag true; no demo or video. · polish: Only setup README; Devpost page minimal.
**Gaps:** No feature description anywhere; What the app does is unknown; Deck challenge text not public
Sources: https://devpost.com/software/schooless, evidence/conuhacks-conuhacks-x-schooless.json, https://github.com/Luchiga19/conuhacks2026

---

### SherLostHolmes
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SAP - Sponsor Challenge

**What it is:** A gamified, detective-themed lost-and-found system. AI semantically matches a description to found items, shows matches as blurred 'suspects' with a hidden decoy, an AI persona interrogates the claimant, and ESP32 servo lockers release items with one-time codes.
**Problem / user:** Students who lose items and face awkward, vague lost-and-found office visits; also admins managing found inventory.

**Features**
- AI semantic matching — LangChain with embeddings matches a description (blue water bottle) to differently worded found items *[claimed]*
- Blind lineup — Matches appear as anonymous suspects with Cloudinary-blurred images and personas *[shown_working]*
- Interrogation room — An AI persona asks ownership-verification questions without revealing answers, using forbidden-phrase and validation layers *[claimed]*
- Decoy fraud detection — A random cross-category decoy is hidden in each lineup; picking it flags a fraud attempt *[claimed]*
- ESP32 smart lockers — XIAO ESP32-S3, servo lock and CardKB keypad fetch the code from the backend, verify, unlock and auto-lock after 10 s *[shown_working]*
- Lucky Find slot machine — Items unclaimed for 6+ months can be won by pulling a slot machine *[shown_working]*
- Admin dashboard and auth — Registration, sign-in, filing a lost item, evidence page and admin dashboard shown in screenshots *[shown_working]*

**Flow:** Register and sign in → File a lost item → Describe item on the Evidence page → View blurred suspect lineup → Answer interrogation questions → Receive one-time code → Enter code on locker keypad to collect

**Prompt:** SAP sponsor challenge at ConUHacks X: CAD 400 total across 3 winners; 1st gets $100 Amazon gift cards plus lunch with SAP Montreal executives and hiring managers, 2nd/3rd lunch only. The Devpost page gives no problem statement.
**Fit (implied):** Won SAP challenge; AI lost-and-found with verification and physical lockers. Brief not public; SAP products unused.  *(targeted: SAP - Sponsor Challenge)*
**AI:** LangChain orchestration via OpenRouter, custom vector embeddings for semantic search, and a guarded LLM persona for interrogation questions; structured workflows chosen over free agents.
**Architecture:** Next.js 14 frontend with Clerk auth; FastAPI backend with MongoDB Atlas, LangChain/OpenRouter and Cloudinary; ESP32 lockers poll REST endpoints for status, password verify and unlock reports.
**Novelty:** Combines game theming, decoy-based fraud detection and a physical locker with keypad; slot-machine redemption of old items.
**Scope:** medium · working: Screenshots of full app flow, locker firmware with API contract and wiring; ~12.6k LOC; no live demo. · polish: Themed UI, nine screenshots; locker README with troubleshooting; no tests.
**Claims:** Decoy item flags fraudulent claims | 24/7 pickup via smart lockers with one-time passwords
**Gaps:** Evidence README is the ESP32 locker README only; SAP brief not public
Sources: https://devpost.com/software/sherlostholmes (Chrome), evidence/conuhacks-conuhacks-x-sherlostholmes.json, https://conuhacks-x.devpost.com/

---

### Socratic
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of MongoDB Atlas

**What it is:** VS Code extension that coaches learners with guiding questions and hints rather than finished answers. Users pick an AI teacher persona with its own voice and a help level from nudge to full solution, and a radar chart tracks skill progress.
**Problem / user:** Students and early-career coders who copy AI-generated code without learning; wants mentorship that builds understanding.

**Features**
- Real-time code analysis with popups — Watches code as you type and shows hints with Explain, Debug, Improve and Stuck buttons *[shown_working]*
- Five adaptive help levels — From slight nudge to full hands-on solution, chosen by the learner *[shown_working]*
- AI teacher marketplace — Personas (Socrates, Ninja, Army General etc.) with distinct prompts, ElevenLabs voices and catchphrases *[shown_working]*
- Skill Atlas radar chart — Tracks proficiency per skill category; skill packs can be unlocked or downloaded *[shown_working]*
- Voice in and out — ElevenLabs TTS encouragement every ~10 lines and STT via mic for questions *[shown_working]*
- RAG over uploaded files — Dropped files are chunked, embedded with Gemini and retrieved via MongoDB Atlas Vector Search *[shown_working]*
- Cloud-synced profiles — MongoDB stores profile, skill data and teacher configs, with local JSON fallback *[shown_working]*

**Flow:** Install VSIX in VS Code → Pick a teacher and help level → Write code and receive contextual popups → Ask questions in chat by text or voice → Attach files for context → Watch skill radar update

**Prompt:** not public / not found
**Fit (explicit):** README title banner names the MongoDB Atlas prize and details Atlas use: user profiles, nested $set/$inc updates, shareable teacher configs, and $vectorSearch for document retrieval.  *(targeted: [MLH] Best Use of MongoDB Atlas)*
**Sponsor tools:** MongoDB Atlas (Profiles, skill tracking, marketplace teachers, vector search RAG, core); ElevenLabs (Teacher voices TTS and speech-to-text, supporting)
**AI:** Google Gemini generates Socratic guidance in teacher personas; Gemini text-embedding-004 embeds uploaded documents for semantic retrieval from Atlas.
**Architecture:** TypeScript extension with webview sidebar; service layer for Gemini chat, ElevenLabs voice, RAG and a hybrid MongoDB/local DataService; data stored as JSON teacher profiles and Atlas collections.
**Novelty:** Inverts the usual coding-assistant goal by withholding answers; persona voices, skill radar and downloadable sponsor skill packs make it a mini learning platform inside the editor.
**Scope:** medium · working: Detailed README with screenshots, ~21k LOC, packaged VSIX flow and demo video. · polish: Landing page in docs/, teacher marketplace UI, README screenshots.
**Claims:** Dynamic encouragement every ten lines of code | Atlas Vector Search used for document RAG
**Gaps:** No MongoDB challenge text on ConUHacks X page
Sources: https://devpost.com/software/socratic-xu768i, https://github.com/GitExcited/Socratic

---

### TheGardens
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Desjardins - Sponsor Challenge

**What it is:** A four-part hands-free system: an ESP32 plus IMU glove acting as a gesture mouse and voice input, a desktop treasure-hunt game with changing weather, a Flutter banking app that reacts to the game's weather, and a relay server linking game and app.
**Problem / user:** People who cannot easily use keyboards or mice because of work conditions or physical disabilities; the glove is described as a future goal rather than a validated user group.

**Features**
- Gesture glove — ESP32 with MPU-9250 IMU turns hand motion into cursor control, projecting 3D acceleration into 2D movement, sent over Bluetooth HID *[shown_working]*
- Voice commands — Glove or phone microphone streams speech to a backend using ElevenLabs speech-to-text and Gemini for actions and app navigation *[claimed]*
- Treasure-hunt desktop game — Character collects treasure and travels through environments with varied weather *[shown_working]*
- Weather-reactive banking app — Flutter iOS app with balances, payees, contacts and transactions that changes theme with the game weather and real-time weather data *[shown_working]*
- Invisibility Mode — Banking privacy view that hides financial data from onlookers *[claimed]*
- Relay server — Shared server (SQLite) passes state between game and banking app via an agreed API contract *[shown_working]*

**Flow:** Flash firmware and pair the glove by Bluetooth → Run the desktop client and open the dashboard → Move the hand to steer the game character → Weather in the game appears in the mobile banking app → Use voice commands to navigate the app

**Prompt:** Desjardins sponsor challenge: 5 winners with prepaid cards (CAD 2,300 total, 1st $200 per member down to 5th $50). The Devpost page gives no problem text.
**Fit (explicit):** Page says the Desjardins challenge made the team pivot from a Jarvis-style idea to a banking app tied to the game's weather, with a glove for accessible input.  *(targeted: Desjardins - Sponsor Challenge)*
**Sponsor tools:** ElevenLabs (Speech-to-text for voice commands, supporting); Gemini API (Turning transcribed voice into actions, supporting)
**AI:** ElevenLabs speech-to-text then Gemini maps speech to app actions (per README); no other models.
**Architecture:** ESP32 glove (IMU, mic) to desktop client over BLE HID; separate game; backend relay with SQLite between game and Flutter iOS banking app; banking and weather data feeds.
**Novelty:** Combines custom wearable hardware, a game and a banking app in one demo; argues IMU sensing over camera tracking for occlusion, lighting and privacy.
**Scope:** medium · working: Demo video, ~13k LOC repo with Flutter, server and game folders, plus app screenshots; DIY flex sensors failed so IMU used. · polish: README with hardware tables, architecture diagram and comparison; some tests; integration across teams was rough.
**Claims:** Hardware sensors beat camera tracking on occlusion, lighting, latency and privacy (README)
**Gaps:** Video not watched; README calls the project G-Lovers/GestureFlow, page TheGardens; Planned: two-glove mode, flex sensors, on-device gesture ML
Sources: https://devpost.com/software/thegardens, evidence/conuhacks-conuhacks-x-thegardens.json, https://conuhacks-x.devpost.com/

---

### Thornmail
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** D3 Security - Sponsor Challenge

**What it is:** A local-first defensive security triage dashboard. It ingests SOC log CSVs, clusters related events into explainable cases, scores risk by transparent rules, and uses an on-device Llama 3 model to summarize key details and suggest next steps. The analyst decides.
**Problem / user:** Security analysts buried under noisy alerts where each log looks like a separate issue.

**Features**
- Case clustering from CSV logs — Groups related events into connected cases using transparent clustering *[shown_working]*
- Rule-based risk scoring — Clear, auditable scoring logic ranks cases *[shown_working]*
- Local LLM explanations — Ollama Llama 3 summarizes cases, highlights relationships and recommends next steps; data stays on the machine *[shown_working]*
- Dual views — User-friendly and analyst-focused dashboards *[claimed]*
- Live event stream and API — FastAPI endpoints for stats, cases and an SSE stream with demo preloading of CSV events *[shown_working]*

**Flow:** Start FastAPI backend and Next.js frontend (one command) → Backend preloads sample CSV events → Open dashboard to see clustered, scored cases → Request an AI summary for a case → Analyst makes the final call

**Prompt:** D3 Security sponsor challenge: 2 winners; 1st gets Amazon gift cards, a D3 interview and an RSA Conference pass per member. The Devpost page gives no problem text.
**Fit (implied):** Won the D3 challenge; it is a SOC-style alert triage tool that reduces noise, explains cases and keeps the analyst in control. Brief not public.  *(targeted: D3 Security - Sponsor Challenge)*
**AI:** Local Llama 3 via Ollama explains and summarizes pre-clustered, rule-scored cases; AI supports rather than decides.
**Architecture:** Next.js frontend (port 3001) calls a FastAPI backend (port 8000) that ingests CSVs with pandas, clusters and scores, streams via SSE, and queries Ollama.
**Novelty:** Emphasizes conservative, auditable rules with AI only as a local explainer; no cloud data transfer.
**Scope:** large · working: Demo video and repo with backend, frontend, sample test cases and data; file count inflated by data (~1.3M LOC estimate). · polish: README with setup, verification commands and one-command dev; tests present; no metrics.
**Claims:** Local-only processing; no data leaves the machine | Reduces alert noise (no numbers)
**Gaps:** Video not watched; page title is Sentinel, repo Thornmail; No quantitative results; Defensive tool; sample data origin not stated
Sources: https://devpost.com/software/sentinel-2sjz9f, evidence/conuhacks-conuhacks-x-thornmail.json, https://conuhacks-x.devpost.com/

---

### ViniClip
*ConUHacks ConUHacks X · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 1st Place - General Challenge [1st]

**What it is:** Browser recorder that edits itself while you talk. Audio streams to a backend that transcribes it, an OpenAI tool-calling agent decides which segments to cut, and ffmpeg trims and stitches the clip; it can also post to Instagram Reels.
**Problem / user:** Short-form video creators who lose time re-recording or cutting pauses and flubbed takes after the fact.

**Features**
- Live in-browser recording — MediaRecorder captures video and AudioWorklet streams audio over WebSocket to FastAPI *[claimed]*
- Streaming speech-to-text — Moonshine transcribes audio on the server with voice activity detection *[claimed]*
- Agent-driven cutting — OpenAI Responses API with function calling returns which pieces to drop (pauses, repeated takes, mistakes) *[claimed]*
- ffmpeg trim and stitch — Edits applied while recording so the output is nearly ready at stop *[claimed]*
- Post to Instagram Reels — A tool call uploads via S3 and the Instagram API on command *[claimed]*
- Stutter removal, subtitles, overlays — Listed as future work *[planned]*

**Flow:** Press record → Browser streams audio/video to server → Server transcribes and the agent flags cuts → ffmpeg removes flagged parts live → Stop and get near-final video → Optionally command a Reels upload

**Prompt:** ConUHacks X General Challenge: overall hackathon prize with no separate descriptive prompt; ranked 1st to 3rd.
**Fit (none):** Open general category; the project is a self-contained real-time media tool with no specific prompt to answer.  *(targeted: 1st Place - General Challenge)*
**AI:** Moonshine ONNX speech-to-text with Silero VAD; OpenAI Responses API tool calls decide cut segments and trigger Reels posting.
**Architecture:** React/Vite frontend captures media over WebSocket to a FastAPI backend; async queues and frame buffers feed Moonshine and the OpenAI agent; ffmpeg edits; boto3/S3 and Instagram Graph for posting.
**Novelty:** Edits during capture rather than post-production, using an LLM agent as the editor instead of a fixed silence trimmer.
**Scope:** small · working: Repo with front and back (~2.4k LOC) but README only covers setup; no demo video or live link. · polish: Minimal README and no screenshots.
**Claims:** Editing happens almost instantly during recording
**Gaps:** No video or demo link; Working status unverified
Sources: https://devpost.com/software/viniclip, https://github.com/mahutt/ViniClip, https://conuhacks-x.devpost.com/

---

### Vulkan Tank Online
*ConUHacks ConUHacks X · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Beenox - Sponsor Challenge

**What it is:** A top-down multiplayer tank game in C++ on raw Vulkan, with shadow mapping, Phong shading and Assimp OBJ models. Players host or join over LAN or the internet using Valve's GameNetworkingSockets.
**Problem / user:** No problem stated; the builders wanted to make a PvP shooter without a game engine and learn Vulkan.

**Features**
- Vulkan renderer — Shadow mapping, Phong shading, tank animation and OBJ loading via Assimp, built from the vkguide.dev template *[shown_working]*
- Multiplayer over LAN or internet — Host/join with GameNetworkingSockets; unreliable messages sync NetPlayer state every few frames *[shown_working]*
- Tank controls and shooting — WASD movement, J/K turret rotation, space to fire projectiles, P moves the light *[shown_working]*
- Cross-platform build — CMake; played across Windows and macOS *[shown_working]*

**Flow:** Build with CMake → Host a game or join by address → Drive tank and aim turret → Fire projectiles and see remote tanks update

**Prompt:** Beenox sponsor challenge: one winning team gets a gaming keyboard, headset and Call of Duty: Black Ops 7 per member. The Devpost page gives no problem text.
**Fit (none):** No stated link; a from-scratch networked 3D game by a games-industry sponsor's challenge, inferred only.  *(targeted: Beenox - Sponsor Challenge)*
**AI:** none
**Architecture:** C++ Vulkan client based on vkguide.dev renderer; client/server over GameNetworkingSockets with ZeroTier used to bypass hackathon WiFi isolation; Assimp for models.
**Novelty:** Raw Vulkan with no game engine plus real networking inside a hackathon; challenges were firewalls and client isolation.
**Scope:** medium · working: README controls and features, two screenshots, cross-OS multiplayer claimed; repo includes large third_party tree. · polish: Documented build and controls; no video or demo; tests flagged present.
**Claims:** Real-time multiplayer in a Vulkan demo within the hackathon | Synchronized play across Windows and macOS
**Gaps:** Beenox brief not public; No next steps
Sources: https://devpost.com/software/topdown-tank-online, evidence/conuhacks-conuhacks-x-vulkan-tank-online.json, https://conuhacks-x.devpost.com/

---

