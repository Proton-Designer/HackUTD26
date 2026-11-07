# TAMUhack — TAMUhack 2025 (18 projects)

### Aviateur
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Second Place for American Airlines Challenge [2nd]

**What it is:** Two-sided tool for airline maintenance: iPhone/iPad app guides crew through 3D scans of aircraft problems, uploads them, and a web platform lets engineers view the models, see fleet history and request further scans.
**Problem / user:** Faults like broken lights or exterior damage need specialist engineers to travel on-site; remote review of 3D scans by maintenance engineers could avoid that. Built around American Airlines.

**Features**
- 3D scanning iOS app — Swift and RealityKit app with step-by-step scan instructions for minor and major issues *[shown_working]*
- Automatic upload — scans sent to a central Express server *[claimed]*
- Engineer web viewer — Next.js site renders 3D models (USDZ viewer) for remote inspection *[claimed]*
- Feedback and re-scan requests — engineers comment and ask staff for additional scans *[claimed]*
- Fleet history and past scans — database of aircraft history and maintenance comments *[claimed]*
- Live AA flight data with caching — backend pulls flight data from several vendor APIs and caches to respect rate limits *[claimed]*
- Generative-AI scan pre-analysis and photo/video capture — AI summary of scans for engineers *[planned]*

**Flow:** Crew opens app and scans issue per instructions → Scan uploads to server → Engineer opens web platform and views 3D model and fleet history → Engineer leaves feedback or requests another scan

**Prompt:** Create a solution for the airline industry covering passenger experience, employee experience or operational efficiency (1st 75k AAdvantage miles).
**Fit (implied):** Targets employee experience and operational efficiency by letting engineers diagnose issues remotely from crew 3D scans, integrated with AA flight data.  *(targeted: Second Place, American Airlines Challenge)*
**Sponsor tools:** American Airlines flight data API (Flight Engine) (live flight data and aircraft/flight context, supporting)
**AI:** none
**Architecture:** Swift/RealityKit iOS scanner -> Express backend (uploads, cached AA vendor API calls, libsql DB) -> Next.js web app with Three.js/USDZ viewer; Clerk auth in the web package.
**Novelty:** Uses native iOS LiDAR-style 3D capture rather than photos for an airline maintenance workflow; team learned Swift on the spot.
**Scope:** medium · working: Live site aviateur.tech and 12 screenshots; team says it was 'almost working'. · polish: Multi-package monorepo with tests present; no video.
**Claims:** Placed second in AA challenge | Team states project was almost working
**Gaps:** README empty
Sources: https://devpost.com/software/aviateur, evidence/tamuhack-tamuhack-2025-aviateur.json, https://tamuhack-2025.devpost.com/

---

### Coinvo
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Second Place for PIMCO Challenge [2nd]

**What it is:** Beginner-built finance website combining a stock ticker, an OpenAI-powered chatbot that answers investing questions, and a saved watchlist of stocks.
**Problem / user:** People are overwhelmed by financial tools and lack clear actionable insights; aimed at casual investors and enthusiasts.

**Features**
- Real-time stock ticker — displays live market data from unnamed APIs *[claimed]*
- AI helper bot — OpenAI-based chatbot answers financial questions and gives context *[claimed]*
- Stock performance and strategy help — user asks the bot to analyze performance or suggest strategies *[claimed]*
- Watchlist — save selected stocks via local storage or a database (unspecified) *[claimed]*
- Web interface — Flask-served HTML/CSS/JS pages *[claimed]*

**Flow:** View market data in ticker → Ask the AI assistant about stocks or strategy → Save stocks to the watchlist

**Prompt:** Develop a hack that promotes good financial behavior, focused on specific financial goals.
**Fit (implied):** Gives users market data and AI guidance to support investing decisions; no explicit financial-goal feature is described.  *(targeted: Second Place, PIMCO Challenge)*
**AI:** OpenAI chat model contextualized on financial topics; page claims fine-tuning but gives no detail.
**Architecture:** Flask backend with HTML/CSS/JS frontend, stock data APIs and OpenAI API; Streamlit listed in tags.
**Novelty:** Standard stock-plus-chatbot combination; notable as each member's first full website.
**Scope:** small · working: No repo, demo or video linked; only a written description. · polish: None observable.
**Claims:** Second place in PIMCO challenge | AI fine-tuned for context-aware financial advice (unverified)
**Gaps:** no repo found, no demo
Sources: https://devpost.com/software/coinvo, https://tamuhack-2025.devpost.com/

---

### DJ Bestie
*TAMUhack TAMUhack 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Third Overall Software Hack [3rd]

**What it is:** AI virtual DJ companion: a Unity WebGL animated character talks with the user by voice, reads facial expression and body language through a camera, and plays Spotify-based songs matched to mood and energy.
**Problem / user:** Listeners want a music buddy who shares taste and reacts to mood and conversation, whether relaxing, working out or partying.

**Features**
- Voice conversation — hands-free speech recognition in the browser drives chat with the DJ *[claimed]*
- Emotion and body-language vision — deepface and MediaPipe analyze face and motion in real time *[shown_working]*
- Mood-based recommendations — Python RAG backend with GPT and Spotify endpoints picks songs by mood and energy *[claimed]*
- Animated DJ character — Unity WebGL avatar with custom animations and lighting *[shown_working]*
- Personalized DJ page — Next.js page per user; MongoDB storage *[shown_working]*
- Similar song and artist suggestions — DJ introduces related tracks *[claimed]*
- Fitness mode, offline mode, social sharing — listed future work *[planned]*

**Flow:** Open the DJ page → Talk to the character by voice → Camera reads expression and body language → DJ recommends and plays matching music

**Prompt:** not public / not found
**Fit (none):** General overall prize with no description; project is a multimodal AI entertainment app.  *(targeted: Third Overall Software Hack)*
**AI:** OpenAI GPT for conversation and recommendations (rapidfuzz matching), PyTorch/TensorFlow models for face emotion, MediaPipe/deepface for body and face tracking.
**Architecture:** Next.js/React frontend embedding Unity WebGL; WebSocket backend with MongoDB; Python services for vision, speech analysis and recommendations; Spotify API.
**Novelty:** Combines animated 3D avatar, speech, computer vision and music API in one multimodal loop.
**Scope:** medium · working: Repo with separate vision, speech, recommendations and Unity components; two screenshots; no demo or video. · polish: Unity-based animated avatar; no tests or README detail.
**Claims:** Third overall software hack | Real-time emotion analysis (unmeasured)
**Gaps:** README is one line; no demo
Sources: https://devpost.com/software/dj-bestie, evidence/tamuhack-tamuhack-2025-dj-bestie.json

---

### DreamDrive
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Second Place for Toyota Challenge [2nd]

**What it is:** Quiz-driven Toyota recommender: a two-minute questionnaire on budget, efficiency, seating and tech yields tailored model suggestions with detail pages.
**Problem / user:** Picking among Toyota's many models is hard; aimed at enthusiasts and first-time buyers.

**Features**
- Preference quiz — short questionnaire on budget, fuel economy, seating, tech *[shown_working]*
- Matching algorithm — filters a vehicle dataset by quiz answers; details not described *[claimed]*
- Recommendations and results summary views — personalized list and recap *[shown_working]*
- Vehicle details page — model specs view *[shown_working]*
- Hand-collected dataset in PostgreSQL — web-researched specs loaded by migration scripts via Drizzle *[claimed]*
- Dealership inventory and financing integration — real-time pricing *[planned]*

**Flow:** Take the quiz → View results summary → Browse recommendations → Open a vehicle detail page

**Prompt:** Build a web or mobile solution helping people shop for Toyota vehicles: search, compare, match preferences including financing and leasing costs.
**Fit (implied):** Matches vehicles to buyer preferences via a quiz; financing and leasing are listed only as next steps.  *(targeted: Second Place, Toyota Challenge)*
**Sponsor tools:** AWS (deployment hosting (sst/PostgreSQL), supporting)
**AI:** none
**Architecture:** Next.js app with Drizzle ORM over PostgreSQL, deployed on AWS via SST; openai/ai packages in manifest though writeup mentions no AI.
**Novelty:** Simple recommender; manifest suggests an AI SDK was installed but no AI feature is described.
**Scope:** small · working: Live site dreamdrive.app, repo and YouTube video listed. · polish: Clean UI claimed; around 9.5k LOC with a large component set.
**Claims:** Quiz finishes in about two minutes | Early testers reported high satisfaction (no numbers)
**Gaps:** README minimal
Sources: https://devpost.com/software/dreamdrive, evidence/tamuhack-tamuhack-2025-dreamdrive.json, https://tamuhack-2025.devpost.com/

---

### DrumRoller
*TAMUhack TAMUhack 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Third Overall Hardware Hack [3rd]

**What it is:** Hardware dice tower: servo-driven drum dispenses a chosen number of dice (1-6) from a keypad, and a lifting tray returns them to the cup, with extra modes for rolling many dice.
**Problem / user:** Rolling many dice by hand slows tabletop games and is hard for people with limited hand use.

**Features**
- Dice count dispense — keypad keys 1-6 spin a continuous-servo drum until that many dice drop, detected by IR line sensor *[shown_working]*
- Return to cup — key 0 raises then lowers the tray; * and # raise and lower manually *[shown_working]*
- Demo mode — dispenses then immediately returns dice *[shown_working]*
- Timed Return mode — same with 7.5 second delay *[shown_working]*
- Empty to Table mode — tray raised and drum spun to roll many dice onto the table *[shown_working]*
- Expandable controller — spare pins for more sensors *[claimed]*
- OpenCV dice reading, Discord/voice control, multiple dice types — vision counting and remote play *[planned]*

**Flow:** Power on → Press a number key to roll → Dice drop into tray → Press 0 to return to cup, or choose a special mode

**Prompt:** not public / not found
**Fit (none):** General hardware prize with no description; working electromechanical prototype.  *(targeted: Third Overall Hardware Hack)*
**AI:** none
**Architecture:** Atmega 2560 (Arduino C++, VarSpeedServo) reads a 3x4 keypad and IR line sensor, drives SG90 servos; 3D-printed enclosure from SolidWorks.
**Novelty:** Full mechanical device with four sensor types tried; shows hardware iteration and failure notes (broken servo, power draw).
**Scope:** small · working: README gives full key operation and wiring notes; author reports reliable portable operation; promo video mentioned. · polish: 3D-printed enclosure and documented modes.
**Claims:** Reliable dice detection and dispensing in a portable form | Third overall hardware hack
**Gaps:** video not watched
Sources: https://devpost.com/software/drumroller, evidence/tamuhack-tamuhack-2025-drumroller.json

---

### EcoFy
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** First Place for Amazon Web Services Challenge [1st]

**What it is:** Sustainability app that tracks a user's purchases through uploaded receipts, scores companies on ESG, and offers 2% cash back on buying from qualifying companies.
**Problem / user:** Greenwashing makes it hard for consumers to know whether purchases are really sustainable.

**Features**
- Receipt-based ESG tracker — user uploads receipts; Rekognition and S3 are used but role not stated *[claimed]*
- Sustainability insights — actionable habit suggestions from OpenAI and Open Food Facts data *[claimed]*
- Cash-back rewards — 2% back at companies meeting sustainability standards *[claimed]*
- Learn and plan resources — educational content on sustainability *[claimed]*

**Flow:** Upload a receipt → ESG tracker evaluates it → See insights and cash back

**Prompt:** Use AI/ML for a real-world challenge in healthcare, sustainability or education; bonus for AWS services such as Bedrock, Rekognition, Polly, IoT.
**Fit (implied):** Sustainability use case using Rekognition and S3; team tried Bedrock but hit access issues.  *(targeted: First Place, AWS Challenge)*
**Sponsor tools:** AWS Rekognition and S3 (receipt image handling (role unspecified), supporting); AWS Bedrock (attempted, access blocked, token)
**AI:** OpenAI API and Open Food Facts lookup for product sustainability; AWS Rekognition for image analysis.
**Architecture:** Next.js/React frontend; AWS S3 and Rekognition; OpenAI and Open Food Facts APIs. Repo is a small Next.js scaffold of about 1.5k LOC.
**Novelty:** Rewards-linked ESG receipt scoring concept; implementation appears thin relative to the pitch.
**Scope:** small · working: Repo is mostly a create-next-app scaffold; no demo or video. · polish: Not evident.
**Claims:** 2% cash back for sustainable purchases | First place AWS challenge
**Gaps:** README is boilerplate; flows undemonstrated
Sources: https://devpost.com/software/ecofy-5oalq2, evidence/tamuhack-tamuhack-2025-ecofy.json, https://tamuhack-2025.devpost.com/

---

### Ember
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Second Place for Arm Challenge [2nd]

**What it is:** Web dashboard educating the public about natural disasters, centered on LA fires: per-region property damage and drought data, Plotly charts, a fires education page and a map with Gemini-generated insights.
**Problem / user:** Public awareness and damage assessment after disasters like California wildfires; for affected, at-risk and curious people.

**Features**
- Damage and drought visualizations — Plotly charts from REST APIs for property damage and drought *[shown_working]*
- Interactive map — API data placed at matching locations *[shown_working]*
- Gemini insights — LLM summarizes retrieved data per region *[claimed]*
- Fires education page — researched hazard information *[shown_working]*
- Boundary-select region map — click region to update info *[planned]*

**Flow:** Open dashboard → View regional charts and map → Read generated insights → Visit education page

**Prompt:** Develop a solution to improve disaster preparedness, response or post-event analysis.
**Fit (implied):** Post-event damage analysis and education; ran REST API on an ARM-based server (MacBook M2).  *(targeted: Second Place, Arm Challenge)*
**Sponsor tools:** Arm (ARM-based server hosting the graph API, token)
**AI:** Gemini LLM API turns cleaned data into written insights.
**Architecture:** Flask graph-data REST API on ARM hardware -> React (MUI) frontend with Plotly charts and map.
**Novelty:** Narrow data-viz scope; boundary map not delivered.
**Scope:** small · working: Repo with tests and small codebase (~700 LOC); no demo link. · polish: Basic.
**Claims:** Second place Arm challenge
**Gaps:** no demo
Sources: https://devpost.com/software/ember-guqk6r, evidence/tamuhack-tamuhack-2025-ember.json, https://tamuhack-2025.devpost.com/

---

### FindAir
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** First Place for American Airlines Challenge [1st]; Best Use of Gen AI

**What it is:** Lost-and-found system for airlines: cleaning crews verify a flight, photograph a found item and speak the seat number; an LLM describes the item, the system finds the passenger and emails retrieval or shipping options, and booth staff scan a QR code to close the claim.
**Problem / user:** Items lost on flights are rarely recovered because the process lacks tracking and communication; users are cleaning crews, lost-and-found staff and passengers of American Airlines.

**Features**
- Flight verification — employee enters flight number checked against the American Airlines API *[claimed]*
- Camera item capture with voice seat entry — phone photo plus spoken seat number with mic toggle; image stored on Cloudinary *[claimed]*
- AI item descriptions — LLaMA 3.3 via Groq writes a description that employees can edit on an ingestion page *[claimed]*
- Passenger lookup and email — seat and flight mapped to contact; email with item, QR code, collect or ship options *[claimed]*
- Shipping payment and label — passenger pays for delivery; label generated *[claimed]*
- QR / confirmation-code claim and receipt — booth staff scan QR or enter code, mark item claimed, print receipt *[claimed]*
- Item gallery — browse logged items *[claimed]*
- Role-based access and data minimization — only necessary passenger data handled *[claimed]*

**Flow:** Employee enters flight number → Scans item and speaks seat → Image uploaded and described by AI → Employee reviews descriptions → Passenger emailed with QR and options → Passenger pays shipping or collects at booth → Staff scan QR to mark claimed

**Prompt:** Create a solution for the airline industry covering passenger experience, employee experience or operational efficiency (1st 75k AAdvantage miles).
**Fit (implied):** Streamlines crew lost-item intake with multimodal AI and passenger notification, using the AA flight API; improves employee and passenger experience.  *(targeted: First Place, American Airlines Challenge, Best Use of Gen AI)*
**Sponsor tools:** American Airlines flight API (flight verification and details, supporting); Groq (LLaMA 3.3) (item description generation, core)
**AI:** LLaMA 3.3 via Groq generates item descriptions from photos; voice used for seat input.
**Architecture:** Next.js/Tailwind on Vercel; Node backend calling AA API; Cloudinary image hosting; seat-to-passenger database; email and QR claim flow.
**Novelty:** Full end-to-end lifecycle from found item to receipt, with twelve distinct screens shown.
**Scope:** medium · working: Page shows screenshots of each stage including architecture diagram; no live demo or video. · polish: Complete multi-screen flow; ~6k LOC.
**Claims:** Recovery rates could exceed 30-40% airport benchmark (unmeasured) | First place AA challenge and Best Use of Gen AI
**Gaps:** README is boilerplate
Sources: https://devpost.com/software/afinda, evidence/tamuhack-tamuhack-2025-findair.json, https://tamuhack-2025.devpost.com/

---

### FinSim
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** First Place for PIMCO Challenge [1st]

**What it is:** Interactive financial education simulator where players build a virtual stock portfolio and watch it evolve over time. Later README version adds a BitLife-style 2008-2025 game with investor profiles, random life events and Gemini-generated scenarios.
**Problem / user:** Financial education is dull and abstract; learners practice markets and see how events affect portfolios.

**Features**
- Virtual portfolio — buy stocks and track value *[shown_working]*
- Live price simulation — prices update in real time; scraped data per Devpost *[claimed]*
- Historical 2008-2025 mode — month/year time advance over curated split-adjusted stock data *[claimed]*
- Investor profiles — five personality types with different perks *[claimed]*
- AI life events and yearly recaps — Gemini generates scenarios and robo-advisor summaries; rule-based fallback *[claimed]*
- Win/lose conditions — reach $1M by 2025, partial credit at $250k, bankruptcy below $1,000 *[claimed]*
- Asset purchases like cars and houses — spend portfolio on life decisions *[planned]*

**Flow:** Pick a profile → Build portfolio from index funds and megacaps → Advance time → React to events → Review recap and outcome

**Prompt:** Develop a hack that promotes good financial behavior, focused on specific financial goals.
**Fit (implied):** Teaches investing behavior through simulation with a concrete goal in later README ($10k to $1M); Devpost version shows live portfolio simulation.  *(targeted: First Place, PIMCO Challenge)*
**AI:** Later README: Gemini via Google GenAI SDK generates scenarios and recaps; Devpost mentions none.
**Architecture:** React SPA with Tailwind and SVG sparklines; Express server proxying Gemini; deterministic historical price interpolator; Devpost version used Flask and scraped data.
**Novelty:** Life-sim framing of investing; README appears to have been rewritten after the hackathon, so features may exceed what was shown then.
**Scope:** small · working: Devpost video and repo; README detailed but possibly postdates the event. · polish: Detailed README, ~2.5k LOC.
**Claims:** First place PIMCO challenge | Players can reach $1M by end of 2025 (README premise)
**Gaps:** README version differs from Devpost writeup
Sources: https://devpost.com/software/finsim-d2j8be, evidence/tamuhack-tamuhack-2025-finsim.json, https://tamuhack-2025.devpost.com/

---

### FireGrid.ai
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** First Place for Arm Challenge [1st]

**What it is:** Hardware wildfire early-warning prototype: an Arduino with temperature, humidity and soil moisture sensors feeds a Raspberry Pi that uploads to MongoDB, shown on a Next.js dashboard with live graphs, an OpenAI chatbot over the readings and push alerts on high temperature.
**Problem / user:** California wildfires cause large losses and insurers pull back; goal is monitoring conditions to spot trends and prepare. Aimed at wildfire-prone communities.

**Features**
- Sensor collection — Arduino reads temperature, humidity, soil moisture *[claimed]*
- Pi uplink — Raspberry Pi forwards data to MongoDB *[claimed]*
- Live dashboard — Next.js app updates graphs as new data arrives *[claimed]*
- LLM chatbot — OpenAI answers questions using sensor metrics *[claimed]*
- Temperature push alert — notification to a designated phone above threshold *[claimed]*
- Weatherproofing and manufacturing optimization — outdoor hardening *[planned]*

**Flow:** Sensors record data → Pi uploads to MongoDB → Dashboard shows live graphs → User asks chatbot → Alert fires on high temperature

**Prompt:** Develop a solution to improve disaster preparedness, response or post-event analysis.
**Fit (implied):** Environmental monitoring for wildfire preparedness running on Raspberry Pi (Arm hardware).  *(targeted: First Place, Arm Challenge)*
**Sponsor tools:** Arm (Raspberry Pi) (edge device relaying sensor data, supporting)
**AI:** OpenAI API chatbot grounded in latest sensor readings.
**Architecture:** Arduino -> Raspberry Pi -> MongoDB -> Next.js app with OpenAI chatbot; Cloudflare Workers tried then dropped.
**Novelty:** End-to-end sensor to LLM chat prototype; team admits far from production.
**Scope:** small · working: Described prototype only; no repo, demo or video found. · polish: Unknown.
**Claims:** First place Arm challenge | Prototype addresses wildfire impacts (self-described far from adoption)
**Gaps:** no repo or demo
Sources: https://devpost.com/software/firegrid-ai, https://tamuhack-2025.devpost.com/

---

### flock
*TAMUhack TAMUhack 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Second Overall Software Hack [2nd]

**What it is:** Web app that helps American Airlines travelers after a delay or cancellation: dashboard of flights, then options to generate a one-day itinerary, get hotel vouchers redeemable with points, or find nearby rental cars.
**Problem / user:** About 20% of US flights are delayed or cancelled and compensation takes much back-and-forth; targets disrupted AA customers.

**Features**
- Flight dashboard — shows user flights and rewards from the AA Flight Engine API *[shown_working]*
- Itinerary generation — OpenAI builds a one-day plan using Google Places near the disrupted location *[claimed]*
- Hotel vouchers — overnight stay redeemable with AA points *[claimed]*
- Car rental options — scraped Turo listings with pagination *[claimed]*
- Google sign-in and saved itineraries — NextAuth, Prisma on AWS RDS PostgreSQL *[shown_working]*

**Flow:** Sign in with Google → See flights on dashboard → On a delay or cancellation choose itinerary, hotel or car → Review results → Save itinerary

**Prompt:** Create a solution for the airline industry covering passenger experience, employee experience or operational efficiency.
**Fit (implied):** Improves passenger experience during disruptions, built on AA Flight Engine API; overall prize has no stated text.  *(targeted: Second Overall Software Hack)*
**Sponsor tools:** American Airlines Flight Engine API (flight and rewards data, core)
**AI:** OpenAI API for itinerary content.
**Architecture:** T3 stack: Next.js, TypeScript, Prisma, PostgreSQL on AWS RDS; API routes call AA, Google Places/Maps, OpenAI and Turo scraping.
**Novelty:** Turns disruptions into trip suggestions; scraped Turo for rental data.
**Scope:** medium · working: Live site flockingawesome.tech, repo README, screenshots. · polish: Figma designs, auth and database; no video.
**Claims:** Second overall software hack | Built almost all planned features
**Gaps:** no video
Sources: https://devpost.com/software/flock-ayxf75, evidence/tamuhack-tamuhack-2025-flock.json

---

### Garage
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Third Place for Toyota Challenge [3rd]

**What it is:** Toyota car shopping and VR experience: a web configurator with 3D models for customizing color and interior, then sending the configured car to a Meta headset to walk around at full scale and test drive.
**Problem / user:** Online configurators don't convey the true feel of a car; buyers can be disappointed later. For online car shoppers.

**Features**
- 3D web configurator — React, TypeScript and Three.js show models with color and interior options *[shown_working]*
- Send to VR — configured model pushed to a Meta headset *[claimed]*
- Full-scale VR inspection — walk around and view interior in Unity *[shown_working]*
- VR test drive — custom driving physics in Unity *[claimed]*
- Toyota database use — model, costs and options *[claimed]*
- Cost comparison — side-by-side financial view *[claimed]*

**Flow:** Open Toyota-style page → Customize car → Send to headset → Walk around the car → Take a test drive

**Prompt:** Build a web or mobile solution for shopping Toyota vehicles with search, compare and cost-based matching.
**Fit (implied):** Immersive configurator plus comparison for Toyota shoppers, extending online browse into VR.  *(targeted: Third Place, Toyota Challenge)*
**AI:** none
**Architecture:** React/Three.js web app plus Unity 6 (Meta XR SDK, C#) VR app; Blender-optimized models.
**Novelty:** VR test drive and full-scale car in a hackathon shopping challenge; one headset shared by team.
**Scope:** small · working: YouTube demo and screenshots; repo ~750 LOC (Unity assets excluded). · polish: Optimized models; web/VR state sync unfinished.
**Claims:** Fully functional VR interface for Toyota
**Gaps:** VR not verified
Sources: https://devpost.com/software/garage-8vlb9e, evidence/tamuhack-tamuhack-2025-garage.json

---

### Hi-5
*TAMUhack TAMUhack 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** First Overall Hardware Hack [1st]

**What it is:** Voice-controlled assistive glove: spoken or typed commands in a React app are normalized by NLP, stored in Firebase, and a Raspberry Pi 5 relays them to an Arduino Uno that drives servos pulling elastic strings sewn on the glove to move fingers.
**Problem / user:** People with limited hand mobility from stroke, neurological disorders, arthritis or paralysis; helps rehabilitation and independence.

**Features**
- Voice and text commands — React UI takes spoken or typed commands *[claimed]*
- NLP mapping — normalizes commands to specific finger movements *[claimed]*
- Cloud sync — Firebase Realtime Database stores commands *[claimed]*
- Finger actuation — Pi 5 sends serial to Arduino Uno driving servos tendon-style *[claimed]*
- Feedback sensors, other limbs — planned extensions *[planned]*

**Flow:** Speak or type a command → NLP maps to fingers → Command saved to Firebase → Pi detects change → Arduino and servos move fingers

**Prompt:** not public / not found
**Fit (none):** General hardware prize with no stated text; an assistive device addressing rehabilitation (a medical-hardware theme).  *(targeted: First Overall Hardware Hack)*
**AI:** NLP library normalizes commands to finger actions; no ML model described.
**Architecture:** React web app -> Firebase Realtime DB -> Raspberry Pi 5 (Python) -> USB serial -> Arduino Uno -> servo driver -> servos and glove strings.
**Novelty:** Solo hardware build; soft-tendon glove with voice front end.
**Scope:** small · working: Author states functional prototype and links cometpro.xyz demo site; no repo or video. · polish: Unknown.
**Claims:** First overall hardware hack | Functional prototype from a solo first hackathon
**Gaps:** no repo or video; demo site not opened
Sources: https://devpost.com/software/hi-5-lng2ha

---

### Kaizen
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** First Place for Toyota Challenge [1st]

**What it is:** A Toyota shopping assistant that pulls specs, images and reviews from several sites, ranks models with a weighted score the shopper tunes, and offers an LLM review summary plus a chat over the collected documents.
**Problem / user:** Car shoppers facing 100+ features per model across a big Toyota catalog who want to match a vehicle to their own priorities such as power, speed or reliability.

**Features**
- Weighted-sum vehicle ranking — Scores each Toyota from quantitative specs; shopper sets weights per metric, e.g. horsepower over MPG, and rankings update. *[shown_working]*
- Aggregated specs and reviews — Scrapes cars.com specs, toyota.com images and Edmunds reviews with Selenium/BeautifulSoup into a single dataset. *[shown_working]*
- LLM review summarization — OpenAI model condenses user reviews into themes and overall sentiment. *[shown_working]*
- Conversational chat over documents — LangChain chain with memory and vector-store retrieval answers questions about the vehicle dataset. *[claimed]*
- Compare and Explore views — Next.js frontend with About, Landing, Compare and Explore pages fed by Flask endpoints. *[shown_working]*
- Tracing and evaluation — Arize Phoenix traces LLM/retrieval steps; custom hallucination and correctness evals plus a Guardrails validator. *[claimed]*

**Flow:** Open landing page → Browse or explore Toyota models → Adjust metric weights → See re-ranked vehicles → Compare selected cars side by side → Read LLM review summary or ask the chat

**Prompt:** Toyota challenge: build a web or mobile tool that helps people shop for Toyota vehicles, letting them search, compare and find cars by preference, including financing and leasing costs.
**Fit (implied):** Provides a comparison and ranking experience over Toyota models driven by user-set weights, with review summaries. No financing or leasing component is mentioned.  *(targeted: Toyota Challenge)*
**Sponsor tools:** Arize Phoenix (Tracing LLM and retrieval steps and running evaluations, supporting)
**AI:** OpenAI API via LangChain: review summarization and a memory-backed retrieval chat over a vector store; Arize Phoenix tracing, custom hallucination/correctness evals and Guardrails output validation.
**Architecture:** Selenium scrapers store data in a pickle and Postgres (Docker); Flask API serves a Next.js/Tailwind frontend; LangChain/OpenAI layer handles summaries and chat, traced by Phoenix.
**Novelty:** Pairs a user-weighted numeric ranking with LLM sentiment summaries and includes an LLM evaluation/guardrail layer, unusual for a shopping hack.
**Scope:** medium · working: Demo video embedded; four frontend views; about 4k LOC across frontend, backend and arize folders. · polish: Authors call it relatively polished; Figma mockups used; repo README is nearly empty.
**Claims:** Writeup calls the product relatively polished and low on bugs | Evaluation code for hallucination and correctness is published in the repo
**Gaps:** README empty; no financing/leasing detail; video not watched
Sources: https://devpost.com/software/kaizen-ri9yp2, evidence/tamuhack-tamuhack-2025-kaizen.json, https://tamuhack-2025.devpost.com/

---

### NimbusNews: AI-Powered Weather Storytelling
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Second Place for Amazon Web Services Challenge [2nd]

**What it is:** A pipeline that takes a meteorological chart, has a vision LLM read it, writes a plain-language summary, voices it with TTS and lip-syncs an AI anchor to produce a TV-style weather video shown in a Streamlit dashboard.
**Problem / user:** Meteorologists and researchers spend hours interpreting charts, and public weather communication is slow and manual; the public gets easier-to-consume forecasts.

**Features**
- Chart analysis with vision LLM — Llama 3.2 Vision (90B or 11B) via Bedrock or Cloudflare WorkersAI reads charts like 500 hPa maps and detects patterns. *[shown_working]*
- Report summarization — Llama 3.1 70B turns the chart analysis into a plain-language summary. *[shown_working]*
- Narration audio — Deepgram text-to-speech generates the spoken report. *[shown_working]*
- Lip-synced AI anchor — Modified Wav2Lip fork (Python 3.10, batch processing, Apple MPS) syncs audio to an anchor video, run via a separate Flask server. *[shown_working]*
- Backend switch — User can pick Cloudflare WorkersAI or AWS Bedrock as inference backend; custom retry logic for latency. *[shown_working]*
- Streamlit dashboard with S3 — Upload or select charts from S3; analysis, audio/video report and architecture views; outputs stored back in S3. *[shown_working]*
- Expansion to news aggregation — Planned scraping of AP News, SEC filings and arXiv, topic clustering, multi-anchor studio and a 24/7 live newsroom. *[planned]*

**Flow:** Submit weather chart in Streamlit or pick from S3 → Vision model analyzes chart → LLM writes summary → Deepgram generates audio → Wav2Lip produces anchor video → View and stream report in dashboard

**Prompt:** AWS challenge: build an innovative AI/ML solution for a real-world problem in healthcare, sustainability or education, with bonus points for AWS services such as Bedrock, Rekognition, Polly or IoT.
**Fit (implied):** Uses Bedrock-hosted Llama models and S3 for a weather-reporting pipeline, framed around climate and weather communication.  *(targeted: Amazon Web Services Challenge)*
**Sponsor tools:** AWS Bedrock (Hosting Llama 3.2 Vision for chart analysis (alternative to Cloudflare), core); AWS S3 (Storing input charts and generated audio/video outputs, core)
**AI:** Chained models: Llama 3.2 Vision for charts, Llama 3.1 70B for summaries, Deepgram Aura TTS, Wav2Lip for lip-sync; agentic orchestration inspired by LangChain with model-size selection by complexity.
**Architecture:** Streamlit app calls Bedrock/WorkersAI for vision and text, Deepgram for audio, a separate Flask Wav2Lip server for video, with S3 for storage and playback.
**Novelty:** Chains four AI stages into a synthetic anchor broadcast and revived/modernized the Wav2Lip codebase; pitched as a general data-to-newsroom tool.
**Scope:** small · working: README with setup and pipeline diagram; two repos including a Wav2Lip fork; screenshots of reports; about 660 LOC in main repo. · polish: Architecture diagram and sample input in README; no demo video.
**Claims:** Processes NOAA 500 hPa charts 150x faster than manual analysis (self-reported) | First weather-specific AI video pipeline using open-source models (claimed) | Rewrote about 20% of Wav2Lip codebase
**Gaps:** no demo video; Wav2LipModern repo not read
Sources: https://devpost.com/software/nimbusnews-ai-powered-weather-storytelling, evidence/tamuhack-tamuhack-2025-nimbusnews-ai-powered-weather-storytelling.json, https://tamuhack-2025.devpost.com/

---

### Smart Plant Pot
*TAMUhack TAMUhack 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Second Overall Hardware Hack [2nd]

**What it is:** A purely analog circuit that senses soil moisture and, when soil is dry, lights an LED and drives a motor standing in for a water pump, with no Arduino or code.
**Problem / user:** Botanists and small self-sufficient farmers who need soil moisture kept steady without manual watering or complex electronics.

**Features**
- Soil moisture sensing — Analog sensing circuit with op-amps and transistors detects falling moisture; adjustable setpoint via potentiometer. *[claimed]*
- LED feedback — LED lights when soil gets dry. *[claimed]*
- Automatic watering — Triggers a motor (gear motor substituting for a pump) to release water until moisture recovers. *[claimed]*
- Empty-reservoir cutoff — Pump stops when the water source runs out. *[claimed]*
- Overcurrent protection — Safety circuitry protects against excess current. *[claimed]*
- Battery-powered, code-free design — Built from breadboard, ICs, resistors, capacitors; also lists an A/C adaptor. *[claimed]*

**Flow:** Moisture falls → Circuit detects drop → LED turns on → Motor releases water → Pump stops when source empty

**Prompt:** Overall Hardware Hack prizes (1st to 3rd) for top hardware projects; no further criteria published.
**Fit (none):** Fully analog hardware build with no microcontroller; page does not state a target prize.  *(targeted: Overall Hardware Hack)*
**AI:** none
**Architecture:** Analog loop: moisture sensor into op-amp comparator with potentiometer setpoint, driving LED and transistor-switched motor, with current and empty-source protection.
**Novelty:** Deliberately avoids microcontrollers and code, using discrete analog parts and scrap cans.
**Scope:** tiny · working: Gallery image only; no video or measurements; prototype uses gear motor as pump. · polish: Breadboard prototype; PCB listed as future work.
**Claims:** Built without any Arduino or code | Uses scrap soda cans and readily available parts
**Gaps:** no repo; no schematic or video
Sources: https://devpost.com/software/smart-plant-pot-1ykih9, https://tamuhack-2025.devpost.com/

---

### TalkTuahAirline
*TAMUhack TAMUhack 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** First Overall Software Hack [1st]; Third Place for American Airlines Challenge [3rd]

**What it is:** A phone-call voice assistant for airline passengers that gives airport directions, flight status and TSA tips, and can phone another passenger to negotiate a seat swap, speaking English or Spanish.
**Problem / user:** Airline passengers, especially first-timers, stressed by airports, long lines and awkward seat-swap requests.

**Features**
- Seat swapping by phone — Assistant calls the current seat holder, negotiates the switch and reports the outcome to the requester; backend uses Retell SDK plus puppeteer/selenium. *[shown_working]*
- Airport navigation — Answers location questions about gates, restrooms, restaurants and lounges from preloaded maps. *[claimed]*
- Flight information — Flight status, gate changes, boarding times and how full a flight is, tied to a real upcoming AA flight. *[claimed]*
- TSA guidance — Packing and checkpoint advice, backed by mock APIs. *[claimed]*
- Real-time alerts — Notifies of delays or gate changes with suggested actions. *[claimed]*
- Multilingual voice — English and Spanish via Eleven Labs voices through Twilio calls. *[claimed]*
- Web dashboard — React/Tailwind UI with call log and flight dashboard screenshots. *[shown_working]*

**Flow:** Passenger calls the assistant → Asks navigation, flight or TSA question → Requests a seat swap → Assistant phones other passenger and negotiates → Requester is notified of result → Can see calls in dashboard

**Prompt:** American Airlines challenge: create a solution for the airline industry covering passenger experience, employee experience or operational efficiency; 1st-3rd win AAdvantage miles. Overall Software Hack is a general top prize.
**Fit (implied):** Passenger-experience tool that handles airport navigation, flight status, TSA questions and seat swapping through phone calls.  *(targeted: American Airlines Challenge, Overall Software Hack)*
**AI:** Retell AI wraps a GPT model for dialogue and task handling, with Twilio telephony and Eleven Labs voice synthesis for English and Spanish.
**Architecture:** Node/Express backend orchestrates Retell calls (GPT, Twilio, Eleven Labs) and seat-swap logic; React/Tailwind frontend shows call logs and flight dashboard.
**Novelty:** Agent places outbound calls to a second passenger to carry out a task, rather than only answering questions.
**Scope:** small · working: Repo with backend and frontend (~1.5k LOC); screenshots of call log and dashboard; no video. · polish: Detailed README; humorous branding; mock data for TSA.
**Claims:** Available 24/7 by ordinary phone call with no app or internet | Handles English and Spanish voice calls
**Gaps:** no demo video; seat-swap reliability unverified
Sources: https://devpost.com/software/talktuahairline, evidence/tamuhack-tamuhack-2025-talktuahairline.json, https://tamuhack-2025.devpost.com/

---

### Vision Learning
*TAMUhack TAMUhack 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Third Place for Amazon Web Services Challenge [3rd]

**What it is:** An AI interview-practice web app that talks to the user with synthesized voice and scores confidence, knowledge and eye contact using face analysis, giving personalized feedback.
**Problem / user:** Students and early-career professionals who find professional-development resources too generic for interview preparation.

**Features**
- Interview practice with AI — User solves problems in real time and converses with an OpenAI-driven interviewer. *[claimed]*
- Voice synthesis — AWS Polly speaks the AI interviewer responses. *[claimed]*
- Eye-contact and face analysis — AWS Rekognition and OpenCV evaluate facial cues such as eye contact. *[claimed]*
- Personalized feedback — Reports strengths and improvement areas on confidence, knowledge and eye contact. *[claimed]*
- Planned speech transcription — Add AWS Transcribe for more natural interaction. *[planned]*

**Flow:** Open web app → Start interview practice → Answer problems with camera on → Interact with AI voice → Receive feedback on confidence, knowledge, eye contact

**Prompt:** AWS challenge: AI/ML solution for a real-world problem in healthcare, sustainability or education, with bonus for Bedrock, Rekognition, Polly or IoT.
**Fit (implied):** Education/career-prep tool using Rekognition for face analysis and Polly for voice.  *(targeted: Amazon Web Services Challenge)*
**Sponsor tools:** AWS Rekognition (Facial recognition/eye-contact evaluation, core); AWS Polly (Voice synthesis for AI interviewer, core)
**AI:** OpenAI model for conversation and feedback, AWS Rekognition and OpenCV for vision, AWS Polly for speech.
**Architecture:** HTML/CSS/JS frontend served with Flask/Express backend that calls OpenAI, Polly and Rekognition.
**Novelty:** Combines voice interviewer with computer-vision body-language scoring in one practice loop.
**Scope:** small · working: Repo with templates and static files (~2.5k LOC); no demo link or video. · polish: README is only a title line; page offers no metrics.
**Claims:** Delivers a personalized, human-like learning experience (no metrics)
**Gaps:** no video; feature behavior unverified
Sources: https://devpost.com/software/vision-learning, evidence/tamuhack-tamuhack-2025-vision-learning.json, https://tamuhack-2025.devpost.com/

---

