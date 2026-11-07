# HackUPC: project cards (41 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackUPC 2025

### CARmen  (HackUPC 2025)

- **Prizes:** [2nd] Seat - Know Your Cupra [2nd]  (tier: sponsor_winner)
- **Pitch:** Web platform where prospective Cupra Tavascan buyers chat, upload photos and tour a 3D interior, answered from the car manual.
- **Problem / user:** Owners and buyers struggle to learn car features from a long PDF manual. / prospective car buyers
- **Domain / idea type:** retail_consumer + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; vision
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend Python; db vector database; hosting 
- **Tech/APIs:** Vector database embeddings (database, core); LLM (unspecified) (ai_model, core); Canvas API (framework, supporting)
- **Sponsor APIs:**  | fit: Built an assistant around the Cupra Tavascan manual for the SEAT/Cupra challenge.
- **Repo:** public, commits 70 (before/in/after event: 0/61/9), README detailed
- **Demo/writeup:** video False, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Manual text and images embedded in a vector DB; users select a region of an uploaded photo (Canvas crop sent as base64) to ask about that part.
- **Team size:** 4 | **Confidence:** high | unverified: tech_items
- **Links:** [Devpost](https://devpost.com/software/carmen) | [GitHub](https://github.com/WeihaoLin0830/HackUPC_2025)

### CUPRA-App  (HackUPC 2025)

- **Prizes:** [1st] Seat - Know Your Cupra [1st]  (tier: sponsor_winner)
- **Pitch:** Gamified mobile app that teaches new Cupra Tabascan owners their car step by step and doubles as a searchable pocket manual.
- **Problem / user:** New car owners find it hard to learn their vehicle's features from a conventional manual. / new Cupra Tabascan owners
- **Domain / idea type:** mobility_transport + education / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / False
- **Stack:** langs TypeScript; frontend React Native; Expo; backend Express; db MongoDB; hosting 
- **Tech/APIs:** React Native (framework, core); Expo (framework, supporting); MongoDB (database, supporting)
- **Sponsor APIs:**  | fit: Built a gamified onboarding and manual app for the Cupra Tabascan, matching SEAT's Know Your Cupra challenge.
- **Repo:** public, commits 59 (before/in/after event: 0/57/2), README detailed
- **Demo/writeup:** video False, live none, screenshots None, writeup short, impact claims False
- **Notes:** Very short writeup; React Native/Expo app with Express and MongoDB for the SEAT Know Your Cupra challenge.
- **Team size:** 4 | **Confidence:** medium | unverified: ai_used; n_screenshots; tech_items
- **Links:** [Devpost](https://devpost.com/software/cupra-app) | [GitHub](https://github.com/d1mo22/HackUPC)

### DataCenter-DeCoder  (HackUPC 2025)

- **Prizes:** [2nd] Siemens Energy - Data Center Designer [2nd]  (tier: sponsor_winner)
- **Pitch:** Drag-and-drop data center module planner with real-time constraint checking and custom placement optimization.
- **Problem / user:** Engineers juggle power, cooling, space and cost with disconnected tools and manual math. / data center engineers
- **Domain / idea type:** energy_utilities + dev_tools / dev_tool
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; Python; frontend React; TypeScript; Material-UI; backend FastAPI; db ; hosting 
- **Tech/APIs:** React Flow (framework, core); Material-UI (framework, supporting); FastAPI (framework, core)
- **Sponsor APIs:**  | fit: Visual data center design and constraint tool for the Siemens Energy challenge.
- **Repo:** public, commits 129 (before/in/after event: 0/127/2), README detailed
- **Demo/writeup:** video False, live none, screenshots 3, writeup short, impact claims False
- **Notes:** Short writeup; visualizes resource flow and trade-offs between modules, backed by custom FastAPI optimization algorithms.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/datacenter-decoder) | [GitHub](https://github.com/guimCC/DataCenter-DeCoder)

### ECHOLOOK  (HackUPC 2025)

- **Prizes:** [1st] InditexTech - Visual Search [1st]  (tier: sponsor_winner)
- **Pitch:** Mobile-first fitting-room app: segment clothes in a photo, search Inditex garments by tap or voice, and virtually try them on.
- **Problem / user:** Online fashion shopping lacks the spontaneity of trying clothes in a store. / online fashion shoppers
- **Domain / idea type:** retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web; mobile_cross / False / vision; speech_or_voice; llm_chat; generative_media
- **Stack:** langs JavaScript; Python; frontend Vue; Quasar; backend Node.js; Express; FastAPI; db MongoDB; S3; hosting Docker
- **Tech/APIs:** Inditex Visual Search API (data_source, core, sponsor); Inditex Product Search API (data_source, core, sponsor); U2-Net (ai_model, core); Whisper (ai_model, core); Gemini Pro (ai_model, supporting); Fashn.ai (ai_model, core); MongoDB (database, supporting); Docker (other, supporting)
- **Sponsor APIs:** Inditex Visual Search API; Inditex Product Search API | fit: Used Inditex visual and product search APIs, boosted by segmentation, plus try-on.
- **Repo:** public, commits 13 (before/in/after event: 0/12/1), README detailed
- **Demo/writeup:** video False, live none, screenshots 8, writeup long, impact claims False
- **Notes:** Chains U2-Net clothing segmentation to improve visual search, Whisper plus Gemini voice-to-query, and Fashn.ai virtual try-on; each AI service runs as its own FastAPI container.
- **Team size:** 3 | **Confidence:** high | unverified: platforms
- **Links:** [Devpost](https://devpost.com/software/echolook) | [GitHub](https://github.com/EchoLook/echolook)

### Feel the CUPRA  (HackUPC 2025)

- **Prizes:** [3rd] Seat - Know Your Cupra [3rd]  (tier: sponsor_winner)
- **Pitch:** Unity digital twin of the Cupra Tavascan with guided tours, a voice assistant over the manual, and an EEG headband-controlled driving demo.
- **Problem / user:** Buyers want to learn car features without reading a manual. / prospective car buyers
- **Domain / idea type:** retail_consumer + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** desktop; hardware / True / llm_chat; rag_or_search; speech_or_voice; predictive_ml
- **Stack:** langs C#; Python; frontend Unity3D; backend Flask; db ; hosting Docker
- **Tech/APIs:** Unity3D (framework, core); Gemini 2.0 Flash (ai_model, core); Muse headband (hardware_part, core); Flask (framework, supporting); Docker (other, supporting); Random Forest classifier (ai_model, core)
- **Sponsor APIs:**  | fit: Digital twin of the Tavascan with RAG voice assistant for the SEAT/Cupra challenge.
- **Repo:** public, commits 21 (before/in/after event: 0/21/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 10, writeup long, impact claims False
- **Notes:** Muse EEG headband signals filtered with FFT and classified by a Random Forest (focused vs relaxed) to accelerate or brake a Unity car simulation via a Flask API.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/feel-the-cupra) | [GitHub](https://github.com/ArnauCS03/feel-the-cupra-hackupc-2025)

### FlowCore  (HackUPC 2025)

- **Prizes:** [1st] Siemens Energy - Data Center Designer [1st]  (tier: sponsor_winner)
- **Pitch:** Drag-and-drop data center designer with AI auto-complete, SAT-solver layout optimization, failure simulation and live dashboard.
- **Problem / user:** Designing sustainable data centers is costly, complex and disconnected from regional conditions. / data center engineers and energy managers
- **Domain / idea type:** energy_utilities + dev_tools / data_or_analytics
- **Platforms / hardware / AI:** web / False / agent_or_tool_use
- **Stack:** langs Python; JavaScript; frontend Next.js; React Flow; TailwindCSS; backend FastAPI; MQTT; WebSockets; db MongoDB; hosting Docker Compose
- **Tech/APIs:** Gemini (ai_model, supporting); Next.js (framework, core); React Flow (framework, core); FastAPI (framework, core); MongoDB (database, core); MQTT (Mosquitto) (other, core); SAT solver (framework, core); Docker (other, supporting)
- **Sponsor APIs:**  | fit: Built a data center designer with optimization and simulation for the Siemens Energy challenge.
- **Repo:** public, commits 118 (before/in/after event: 0/117/1), README thin
- **Demo/writeup:** video False, live none, screenshots 6, writeup long, impact claims False
- **Notes:** MQTT plus WebSockets feed a live isometric failure simulator; Python SAT solver does spatial layout; AI 'magic button' fills missing components.
- **Team size:** 4 | **Confidence:** high | unverified: ai_types
- **Links:** [Devpost](https://devpost.com/software/flowcore) | [GitHub](https://github.com/LleidaHackers/backend)

### Graf-Anna  (HackUPC 2025)

- **Prizes:** [1st] Grafana - Green Grafana [1st]  (tier: sponsor_winner)
- **Pitch:** Grafana dashboard linking industrial-era CO2 emissions, temperature, disasters, deforestation and life expectancy to UN SDGs.
- **Problem / user:** Climate-driver data is scattered and hard to see as one story. / general public and students
- **Domain / idea type:** sustainability_climate + education / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs ; frontend ; backend ; db ; hosting Grafana Cloud
- **Tech/APIs:** Grafana (other, core, sponsor); Infinity plugin (other, supporting, sponsor); Our World in Data (data_source, core); OpenAQ API (data_source, supporting)
- **Sponsor APIs:** Grafana | fit: Dashboard built in Grafana using the Infinity plugin and geomap panels.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 3, writeup long, impact claims False
- **Notes:** No custom code: built from Grafana panels and the Infinity plugin on public datasets after dropping a planned custom app plugin; hosted on grafana.net.
- **Team size:** 5 | **Confidence:** high | unverified: has_live_demo
- **Links:** [Devpost](https://devpost.com/software/graf-anna)

### IndiSearch  (HackUPC 2025)

- **Prizes:** HackUPC 2nd place [2nd]  (tier: overall_top3)
- **Pitch:** Chrome extension that detects clothing in videos on sites like Netflix or YouTube and lets you find and buy matching items.
- **Problem / user:** Spotting an outfit on screen and tracking down where to buy it online is slow and frustrating. / online shoppers watching video content
- **Domain / idea type:** retail_consumer + creative_media / twist_on_known_app
- **Platforms / hardware / AI:** browser_extension / False / vision; recommendation
- **Stack:** langs JavaScript; Python; frontend Chrome extension; backend FastAPI; db ; hosting 
- **Tech/APIs:** YOLO (ai_model, core); FastAPI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 44 (before/in/after event: 0/44/0), README solid
- **Demo/writeup:** video False, live none, screenshots 9, writeup medium, impact claims False
- **Notes:** YOLO detects people on screen then clothing is identified and searched for products; JavaScript extension with FastAPI backend combining several APIs.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots; tech_items; writeup_length
- **Links:** [Devpost](https://devpost.com/software/indisearch-nc7k59) | [GitHub](https://github.com/joanbros5/HackatonUPC2025/tree/main)

### Inditex clothe detector  (HackUPC 2025)

- **Prizes:** [3rd] InditexTech - Visual Search [3rd]  (tier: sponsor_winner)
- **Pitch:** Screenshot-based tool that sends a garment image to the Inditex API and lists similar products with price and purchase link.
- **Problem / user:** Finding similar clothes from a webpage image needs multiple manual searches. / online fashion shoppers
- **Domain / idea type:** retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs JavaScript; Python; frontend React; Vite; backend Flask; db ; hosting 
- **Tech/APIs:** Inditex Visual Search API (data_source, core, sponsor); Flask (framework, supporting); React (framework, supporting)
- **Sponsor APIs:** Inditex Visual Search API | fit: Passes screenshots to the Inditex API for similar-product results.
- **Repo:** public, commits 29 (before/in/after event: 0/26/3), README solid
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Short writeup; React/Vite interface for taking screenshots with a Flask server forwarding images to the Inditex API.
- **Team size:** 3 | **Confidence:** medium | unverified: team_size; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/inditex-clothe-detector) | [GitHub](https://github.com/jmnu4245/hackupc25)

### Inditex Visual Search  (HackUPC 2025)

- **Prizes:** [2nd] InditexTech - Visual Search [2nd]  (tier: sponsor_winner)
- **Pitch:** Next.js web app that finds similar Inditex clothing from an uploaded or camera-captured photo, deployed on Vercel.
- **Problem / user:** Shoppers want to find similar garments from a photo quickly. / online fashion shoppers
- **Domain / idea type:** retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs TypeScript; frontend Next.js; Tailwind; backend Next.js SSR; db ; hosting Vercel
- **Tech/APIs:** Inditex Visual Search API (data_source, core, sponsor); Next.js (framework, core); Vercel (cloud, supporting); Cheerio (framework, supporting)
- **Sponsor APIs:** Inditex Visual Search API | fit: Wraps Inditex visual search API in a camera/upload UI.
- **Repo:** public, commits 44 (before/in/after event: 0/44/0), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 8, writeup long, impact claims False
- **Notes:** Server-side rendering keeps API credentials hidden, with token auto-refresh; product image scraping broke on Vercel and Zara anti-bot protection in production.
- **Team size:** 3 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/inditex-visual-search) | [GitHub](https://github.com/aolle99/HackUPC2025)

### MMG  (HackUPC 2025)

- **Prizes:** HackUPC 1st place [1st]  (tier: overall_top3)
- **Pitch:** Raspberry Pi clusters and a companion Android app that keep passengers getting flight updates during power and connectivity outages.
- **Problem / user:** During blackouts, travelers lose connectivity and battery and miss flight delay information. / airline passengers
- **Domain / idea type:** mobility_transport + telecom_networking / hardware_gadget
- **Platforms / hardware / AI:** mobile_android; hardware; web / True / None
- **Stack:** langs Kotlin; Java; JavaScript; Bash; HTML; CSS; frontend React; backend Node.js; Express; db SQLite; Room; hosting 
- **Tech/APIs:** Raspberry Pi (hardware_part, core); hostapd WiFi AP (other, core); Android (Kotlin) (framework, core); Bluetooth (other, supporting); SQLite (database, supporting); ChatGPT (ai_model, token)
- **Sponsor APIs:**  | fit: Entered for the Vueling challenge; project targets flight-update delivery during outages.
- **Repo:** public, commits 88 (before/in/after event: 0/83/5), README detailed
- **Demo/writeup:** video True, live none, screenshots 15, writeup medium, impact claims False
- **Notes:** Raspberry Pi nodes act as local WiFi access points (hostapd) with TCP/UDP and Bluetooth links, resilient to connectivity loss; built for the Vueling challenge.
- **Team size:** 5 | **Confidence:** medium | unverified: ai_used; n_screenshots; writeup_length; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/mmg) | [GitHub](https://github.com/Fez248/HACKUPC-2025)

### Peaceful Protest Tracker: Headlines vs Reality  (HackUPC 2025)

- **Prizes:** [2nd] Grafana - Green Grafana [2nd]  (tier: sponsor_winner)
- **Pitch:** Grafana dashboard that scrapes Serbian news, uses Gemini to extract protest locations and sentiment, and contrasts independent versus government-aligned coverage.
- **Problem / user:** Conflicting media accounts of the Serbian student protests make events hard to understand. / citizens and observers following Serbian protests
- **Domain / idea type:** civic_legal + social_community / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; Java; frontend ; backend Spring Boot; Python; db MongoDB Atlas; hosting Grafana Cloud
- **Tech/APIs:** Gemini 2.5 Flash (ai_model, core); Grafana (other, core, sponsor); MongoDB Atlas (database, core); Spring Boot (framework, core); BeautifulSoup (framework, supporting)
- **Sponsor APIs:** Grafana | fit: Dashboard built on Grafana panels fed from MongoDB Atlas.
- **Repo:** public, commits 20 (before/in/after event: 0/15/5), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 2, writeup long, impact claims False
- **Notes:** Scheduled pipeline: BeautifulSoup scraping, Gemini 2.5 Flash JSON extraction, Spring Boot cron coordinator, MongoDB Atlas, Grafana geomap and trend panels.
- **Team size:** 4 | **Confidence:** high | unverified: has_live_demo
- **Links:** [Devpost](https://devpost.com/software/peaceful-protest-tracker-headlines-vs-reality) | [GitHub](https://github.com/mrsladoje/hackupc2025)

### Rack Attack  (HackUPC 2025)

- **Prizes:** [3rd] Siemens Energy - Data Center Designer [3rd]  (tier: sponsor_winner)
- **Pitch:** Web platform to assemble data center infrastructure from provided parts with 3D view, live requirement tracking and recommendations.
- **Problem / user:** Customers need flexible, intuitive way to configure data centers beyond fixed templates. / data center customers
- **Domain / idea type:** energy_utilities + dev_tools / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; React; three.js; backend FastAPI; db MongoDB; hosting 
- **Tech/APIs:** Next.js (framework, core); FastAPI (framework, core); Gemini (ai_model, unclear); MongoDB (database, supporting); three.js (framework, supporting)
- **Sponsor APIs:**  | fit: Data center configurator for the Siemens Energy challenge.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 2, writeup short, impact claims False
- **Notes:** Very short writeup; includes 3D rendering (three.js) and an LLM component, details not described.
- **Team size:** 3 | **Confidence:** high | unverified: team_size; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/rack-attack) | [GitHub](https://github.com/hiatus770/hackupc2025)

### Referlut  (HackUPC 2025)

- **Prizes:** [1st] Revolut - AI in Financial Applications [1st]  (tier: sponsor_winner)
- **Pitch:** Student-finance web app that finds refer-a-friend and pooled deals via LLM-validated scraping and matches users to share them.
- **Problem / user:** Student-friendly referral and pooling offers are hard to find and hard to find peers for. / students
- **Domain / idea type:** fintech_finance + social_community / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs JavaScript; frontend React; Tailwind; backend Supabase; BeautifulSoup; db Supabase; hosting 
- **Tech/APIs:** Gemini (ai_model, core); GPT-4.1 (ai_model, core); GPT-3.5 turbo (ai_model, supporting); Supabase (database, core); Open Banking API (data_source, supporting); BeautifulSoup (framework, supporting)
- **Sponsor APIs:**  | fit: Fintech app using LLM agents and bank-transaction linking for the Revolut AI-in-finance challenge.
- **Repo:** public, commits 46 (before/in/after event: 0/45/1), README thin
- **Demo/writeup:** video False, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Open Banking link for real-time transactions; several LLMs split by task (Gemini with search for fact-checking, GPT-3.5 for summaries, GPT-4.1 for analytics).
- **Team size:** 4 | **Confidence:** high | unverified: team_size
- **Links:** [Devpost](https://devpost.com/software/referlut) | [GitHub](https://github.com/ron0studios/Referlut)

### RevPoints+  (HackUPC 2025)

- **Prizes:** [3rd] Revolut - AI in Financial Applications [3rd]  (tier: sponsor_winner)
- **Pitch:** Streamlit prototype recommending where Revolut Points can be spent and letting vendors generate AI marketing campaigns from brochures.
- **Problem / user:** Revolut points go unredeemed because users miss relevant vendors and small vendors lack reach. / Revolut users and partner vendors
- **Domain / idea type:** fintech_finance + retail_consumer / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; vision; recommendation
- **Stack:** langs Python; frontend Streamlit; backend LangGraph; LangChain; Pydantic; db Redis; hosting Streamlit Cloud
- **Tech/APIs:** Gemini 2.5 Pro (ai_model, core); LangGraph (framework, core); Redis (database, core); Perplexity API (data_source, supporting); Sentence-Transformers (ai_model, supporting); Streamlit (framework, core)
- **Sponsor APIs:**  | fit: Points-redemption recommender and vendor campaign tool for the Revolut AI-in-finance challenge.
- **Repo:** public, commits 61 (before/in/after event: 0/53/8), README solid
- **Demo/writeup:** video False, live not_checked, screenshots 2, writeup long, impact claims True (Reports 80% fewer parsing errors, sub-200ms feed latency and campaign creation in under two minutes.)
- **Notes:** Multiple LangGraph agents (campaigner, profiler, recruiter) with Redis Streams pub/sub feed; separate consumer and vendor Streamlit apps deployed. Writeup cites 80% fewer parsing errors and under 200ms feed latency.
- **Team size:** 4 | **Confidence:** high | unverified: live_demo_url
- **Links:** [Devpost](https://devpost.com/software/revpoints) | [GitHub](https://github.com/simoncoessens/Revpoints-Plus)

### TopRack Studio  (HackUPC 2025)

- **Prizes:** HackUPC 3rd place [3rd]  (tier: overall_top3)
- **Pitch:** Data center planning tool: drag-and-drop 2D layout editor in a scanned room, mirrored live into a VR headset for clients.
- **Problem / user:** Sales teams need to plan and show data center module layouts to clients in the real room context. / data center sales teams and clients
- **Domain / idea type:** productivity_workplace + creative_media / creative_tool
- **Platforms / hardware / AI:** web; other / True / False
- **Stack:** langs Python; TypeScript; frontend React; Leaflet; Tailwind; Unity; backend Django; db SQLite; hosting 
- **Tech/APIs:** Unity (framework, core); Meta XR SDK (hardware_part, core); Leaflet.js (maps_geo, core); Django (framework, supporting); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 152 (before/in/after event: 0/152/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 11, writeup medium, impact claims False
- **Notes:** Team brought a VR setup to the event; room coordinates from a VR scan become a grid in a Leaflet web editor synced with a Unity/Meta XR scene; Siemens challenge.
- **Team size:** 4 | **Confidence:** medium | unverified: ai_used; n_screenshots; writeup_length; platforms
- **Links:** [Devpost](https://devpost.com/software/toprack-studio) | [GitHub](https://github.com/false-positive/toprack-studio)

### TripMates - Team Trip Planner AI Agent  (HackUPC 2025)

- **Prizes:** [1st] Skyscanner - The Perfect Reunion: Finding the Best Destination for friends around the world [1st]  (tier: sponsor_winner)
- **Pitch:** Voice AI agent that listens to a group of friends, proposes destinations, finds real flights and hotels, and emails a trip proposal.
- **Problem / user:** Friends in different cities struggle to agree on a destination. / groups of friends planning trips
- **Domain / idea type:** mobility_transport + social_community / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend React; LiveKit; backend Python; LiveKit Agents; Pydantic; db ; hosting 
- **Tech/APIs:** Skyscanner API (data_source, core, sponsor); LiveKit Agents (framework, core); OpenAI (ai_model, core); Deepgram Nova 3 (ai_model, supporting); Amadeus (data_source, supporting); Ticketmaster (data_source, supporting); Meetup (data_source, token)
- **Sponsor APIs:** Skyscanner API | fit: Agent queries the Skyscanner API for flights as part of group trip proposals.
- **Repo:** public, commits 109 (before/in/after event: 0/109/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 3, writeup long, impact claims False
- **Notes:** Agent joins a live group conversation via LiveKit and calls multiple travel APIs (Skyscanner, Amadeus, HotelAPI, Ticketmaster, Meetup) during the session.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/tripmates-team-trip-planner-ai-agent) | [GitHub](https://github.com/adriablancafort/tripmates-hackupc2025)

### unpackr  (HackUPC 2025)

- **Prizes:** [3rd] Skyscanner - The Perfect Reunion: Finding the Best Destination for friends around the world [3rd]  (tier: sponsor_winner)
- **Pitch:** Group trip recommender that suggests destinations from photos of your luggage, a favorite song and a color palette, with flight prices and events.
- **Problem / user:** Typical 'where do you want to go' prompts ignore travelers' vibe. / groups of friends planning trips
- **Domain / idea type:** mobility_transport + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; recommendation
- **Stack:** langs JavaScript; frontend Next.js; backend Supabase; db Supabase; hosting 
- **Tech/APIs:** Skyscanner API (data_source, core, sponsor); PredictHQ API (data_source, supporting); Supabase (database, core); Next.js (framework, core)
- **Sponsor APIs:** Skyscanner API | fit: Fetches cheapest flights per group member via Skyscanner API.
- **Repo:** public, commits 110 (before/in/after event: 0/110/0), README solid
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Inverts trip planning: users upload suitcase photos and music to get a destination; combines Skyscanner flights, PredictHQ events and per-activity group voting.
- **Team size:** 4 | **Confidence:** medium | unverified: ai_used; ai_types; n_screenshots; team_size
- **Links:** [Devpost](https://devpost.com/software/unpackr) | [GitHub](https://github.com/bielupc/hackupc25)

### We Nomad Us  (HackUPC 2025)

- **Prizes:** [2nd] Skyscanner - The Perfect Reunion: Finding the Best Destination for friends around the world [2nd]  (tier: sponsor_winner)
- **Pitch:** Flutter app where groups swipe yes/no travel quizzes, get Gemini and Skyscanner-based destination picks, and earn NFC-unlocked collectibles.
- **Problem / user:** Groups find choosing a shared travel destination hard. / groups of travelers
- **Domain / idea type:** mobility_transport + social_community / new_category
- **Platforms / hardware / AI:** mobile_cross / True / llm_chat; recommendation
- **Stack:** langs Dart; SQL; frontend Flutter; backend Supabase; db PostgreSQL; hosting Vercel
- **Tech/APIs:** Skyscanner API (data_source, core, sponsor); Gemini (ai_model, core); Supabase (database, core); Flutter (framework, core); NFC (hardware_part, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:** Skyscanner API | fit: Uses Skyscanner flight prices and dates to inform group destination recommendations.
- **Repo:** public, commits 79 (before/in/after event: 0/79/0), README solid
- **Demo/writeup:** video False, live not_checked, screenshots 2, writeup long, impact claims False
- **Notes:** Gamified collectibles (Common/Rare/Shiny) unlocked by NFC cards at partner locations, managed without a blockchain; Tribe rooms joined by QR code.
- **Team size:** 4 | **Confidence:** high | unverified: has_hardware
- **Links:** [Devpost](https://devpost.com/software/we-nomad-us) | [GitHub](https://github.com/meulencv/wenomadus)

### Wise Wallet  (HackUPC 2025)

- **Prizes:** [2nd] Revolut - AI in Financial Applications [2nd]  (tier: sponsor_winner)
- **Pitch:** React dashboard plus Alexa skill that predicts month-end spending and classifies needs versus wants, answering questions via Gemini.
- **Problem / user:** Expense trackers dump numbers without helping people understand or control spending early. / individuals managing personal spending
- **Domain / idea type:** fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web; bot_or_chat / False / llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs TypeScript; Python; Node.js; frontend React; Vite; TailwindCSS; backend AWS Lambda; API Gateway; Alexa Skills; db S3; hosting AWS; Docker
- **Tech/APIs:** Gemini (ai_model, core); Amazon Alexa (other, core); AWS Lambda (cloud, core); scikit-learn (framework, core); Docker (other, supporting)
- **Sponsor APIs:**  | fit: Personal-finance prediction and voice assistant built for the Revolut AI-in-finance challenge.
- **Repo:** public, commits 50 (before/in/after event: 0/48/2), README detailed
- **Demo/writeup:** video False, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Two scikit-learn Random Forest models (regressor for monthly total, classifier for needs/wants) trained on simulated data, served from AWS Lambda; Alexa latency cut from ~5s via caching.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/spendly-nx3hb0) | [GitHub](https://github.com/juandiazx/wise-wallet)


## HackUPC 2026

### ARC React  (HackUPC 2026)

- **Prizes:** [Jetbrains] 1st place [1st]  (tier: sponsor_winner)
- **Pitch:** iPhone AR IDE that floats code panels in 3D space with hand gestures and voice, syncing to MongoDB and a JetBrains plugin.
- **Problem / user:** No go-to mobile IDE exists and phone screens limit viewing a codebase. / mobile developers
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** mobile_ios / False / speech_or_voice; llm_chat; vision
- **Stack:** langs Swift; Kotlin; Python; frontend SwiftUI; ARKit; RealityKit; backend FastAPI; db MongoDB Atlas; hosting Vercel
- **Tech/APIs:** ARKit/RealityKit (framework, core); MediaPipe (framework, core); ElevenLabs (ai_model, supporting, sponsor); OpenAI API (ai_model, supporting); MongoDB Atlas (database, supporting); JetBrains IntelliJ plugin (other, supporting, sponsor); FastAPI (framework, supporting)
- **Sponsor APIs:** JetBrains (IntelliJ plugin, Junie); ElevenLabs | fit: Mobile AR IDE with a JetBrains IntelliJ plugin and Junie-styled chat panel.
- **Repo:** public, commits 50 (before/in/after event: 0/50/0), README solid
- **Demo/writeup:** video False, live none, screenshots 3, writeup long, impact claims False
- **Notes:** ARKit/RealityKit panels rendered as textures, MediaPipe hand-gesture interpretation, ElevenLabs voice replies, FastAPI backend plus Kotlin IntelliJ plugin reading a MongoDB vector store.
- **Team size:** 3 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/arc-react) | [GitHub](https://github.com/elilourens/HackUPC-MobileIDE)

### B2Travel  (HackUPC 2026)

- **Prizes:** [Skyscanner] 2nd place [2nd]; [MLH] Best Use of ElevenLabs [unknown]  (tier: sponsor_winner)
- **Pitch:** Chrome extension saves travel images to a CLIP-clustered 3D WebVR memory universe navigable by an ElevenLabs voice agent.
- **Problem / user:** Travel inspiration gets lost in camera rolls and bookmarks. / travel dreamers
- **Domain / idea type:** mobility_transport + creative_media / new_category
- **Platforms / hardware / AI:** browser_extension; web / False / vision; speech_or_voice; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; JavaScript; frontend A-Frame; Chrome extension; backend FastAPI; PyTorch; db MongoDB Atlas; hosting 
- **Tech/APIs:** ElevenLabs Conversational AI (ai_model, core, sponsor); CLIP (ai_model, core); UMAP (framework, core); A-Frame (framework, core); FastAPI (framework, supporting); MongoDB Atlas (database, supporting); ngrok (other, token)
- **Sponsor APIs:** ElevenLabs | fit: ElevenLabs voice agent drives navigation and recommendations inside the VR scene.
- **Repo:** public, commits 56 (before/in/after event: 0/55/1), README detailed
- **Demo/writeup:** video False, live none, screenshots 2, writeup long, impact claims False
- **Notes:** CLIP embeddings projected to 3D via UMAP and rendered in A-Frame VR; a voice agent triggers events the VR frontend polls to fly to a 'vibe'.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/b2travel) | [GitHub](https://github.com/laiamp/HackUPC-2026)

### Baymaxxing  (HackUPC 2026)

- **Prizes:** [Mecalux] 2nd place [2nd]  (tier: sponsor_winner)
- **Pitch:** Python warehouse layout optimizer packing storage bays around columns and uneven ceilings using Shapely geometry and parallel exploration.
- **Problem / user:** Maximizing storage capacity at minimum cost under physical constraints is a hard puzzle. / warehouse managers
- **Domain / idea type:** productivity_workplace / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; frontend Streamlit; Plotly; backend Python multiprocessing; db ; hosting 
- **Tech/APIs:** Shapely (framework, core); Streamlit (framework, supporting); Plotly (framework, supporting)
- **Sponsor APIs:**  | fit: Optimization algorithm for the Mecalux warehouse layout challenge.
- **Repo:** public, commits 46 (before/in/after event: 0/45/1), README detailed
- **Demo/writeup:** video False, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Active-node packing via priority queue and multiprocessing explorers cut off at 27s of a 30s limit; Streamlit/Plotly visualizer for manual edits.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/baymaxxing-qglxnc) | [GitHub](https://github.com/P-Santin/HACK2026)

### Bender Blender  (HackUPC 2026)

- **Prizes:** [Jetbrains] 3rd place [3rd]; [MLH] Best Domain Name from GoDaddy Registry [unknown]  (tier: sponsor_winner)
- **Pitch:** Turns a local repository into a voice-navigable dependency graph, with local Gemma summaries and a Ledger USB privilege badge.
- **Problem / user:** Newcomers to a codebase face a file tree with no mental map. / developers onboarding to unfamiliar repos
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** web / True / llm_chat; speech_or_voice
- **Stack:** langs TypeScript; frontend Next.js; Tailwind; backend Next.js API routes; db ; hosting 
- **Tech/APIs:** Qwen3 32B via Groq (ai_model, core); Ollama Gemma (ai_model, core); ElevenLabs TTS (ai_model, supporting, sponsor); Ledger USB device (hardware_part, supporting); react-force-graph-2d (framework, core); Next.js (framework, core)
- **Sponsor APIs:** ElevenLabs; GoDaddy Registry domain (benderblender.cooking) | fit: Third at JetBrains track; also won MLH best domain name prize.
- **Repo:** public, commits 23 (before/in/after event: 0/23/0), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 2, writeup long, impact claims False
- **Notes:** Falls back from Groq-hosted Qwen3 to local Ollama Gemma; polls USB for a Ledger device to show a hardware privilege badge; regex import resolvers across languages.
- **Team size:** 3 | **Confidence:** high | unverified: has_hardware
- **Links:** [Devpost](https://devpost.com/software/bender-blender) | [GitHub](https://github.com/meulencv/spoon-map)

### BioMeshP2P  (HackUPC 2026)

- **Prizes:** [Pears] 1st place [1st]  (tier: sponsor_winner)
- **Pitch:** Peer-to-peer network of Arduino Uno Q-style nodes that classify heat risk locally and jointly trigger cooling actions, shown on a React dashboard.
- **Problem / user:** Heatwaves harm people and heat-prevention responses are not automated. / city environmental managers
- **Domain / idea type:** sustainability_climate + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / False / predictive_ml
- **Stack:** langs JavaScript; frontend React; Vite; backend Node.js; Pear; db ; hosting 
- **Tech/APIs:** Pear runtime (framework, core, sponsor); TensorFlow.js MLP (ai_model, core); Arduino UNO Q (emulated) (hardware_part, supporting, sponsor); React/Vite dashboard (framework, supporting)
- **Sponsor APIs:** Pears | fit: Serverless P2P sensor network on the Pear runtime.
- **Repo:** public, commits 30 (before/in/after event: 0/30/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Nodes are emulated under the Pear runtime with mock sensor data and a TensorFlow.js MLP; consensus among peers triggers actions; NAT hole-punching troubles on eduroam.
- **Team size:** 4 | **Confidence:** high | unverified: has_hardware
- **Links:** [Devpost](https://devpost.com/software/biomeshp2p) | [GitHub](https://github.com/Salipoke/hackUPC_2026)

### Carbassot climbing  (HackUPC 2026)

- **Prizes:** [Mecalux] 1st place [1st]  (tier: sponsor_winner)
- **Pitch:** Automatic warehouse layout solver placing storage bays in irregular spaces using geometric checks, local search and simulated annealing, with 2D/3D visualization.
- **Problem / user:** Placing elements in an irregular space with ceiling limits by hand is tedious. / warehouse planners
- **Domain / idea type:** productivity_workplace / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs C++; TypeScript; frontend React; backend Node.js; C++; db ; hosting 
- **Tech/APIs:** C++ solver (framework, core); React (framework, supporting); Node.js (framework, supporting)
- **Sponsor APIs:**  | fit: Layout optimization for the Mecalux warehouse challenge.
- **Repo:** public, commits 89 (before/in/after event: 0/88/1), README detailed
- **Demo/writeup:** video False, live none, screenshots 2, writeup short, impact claims False
- **Notes:** Catalan-language writeup; C++ solver with restarts and simulated annealing, TypeScript/React visualizer; no mention of AI.
- **Team size:** 4 | **Confidence:** high | unverified: domain_primary
- **Links:** [Devpost](https://devpost.com/software/el-carbasot-sml) | [GitHub](https://github.com/d1mo22/HackUPC26)

### convertfs  (HackUPC 2026)

- **Prizes:** [HackUPC] 1st place [1st]  (tier: overall_top3)
- **Pitch:** FUSE filesystem that converts files on the fly: drop a file into a mounted directory and read out the converted version.
- **Problem / user:** File format conversion normally needs separate tools and manual steps. / developers and command-line users
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** cli; desktop / False / False
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** FUSE (framework, core); FFmpeg (other, core); libvips (other, core); markitdown (framework, supporting); Nix (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 34 (before/in/after event: 0/34/0), README solid
- **Demo/writeup:** video False, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Writeup is README-style; supports video remux/H.264 compression with hardware encoder selection, image formats via libvips, and PDF/Office to markdown via markitdown.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/convertfs) | [GitHub](https://github.com/ThatOtherAndrew/convertfs)

### Djubrino  (HackUPC 2026)

- **Prizes:** [Qualcomm] 1st place [1st]  (tier: sponsor_winner)
- **Pitch:** Smart underground waste containers on Arduino Uno Q with edge AI detecting litter, fill level, fire and odor, feeding a city dashboard.
- **Problem / user:** Full containers and litter in Barcelona create pollution and odors. / city waste-management services
- **Domain / idea type:** sustainability_climate + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision
- **Stack:** langs C; Python; TypeScript; frontend Next.js; shadcn; backend FastAPI; db MongoDB Atlas; hosting 
- **Tech/APIs:** Arduino Uno Q (hardware_part, core, sponsor); Edge Impulse (ai_model, core); MongoDB Atlas (database, supporting); FastAPI (framework, supporting); Next.js (framework, supporting); Ultrasound distance sensor (hardware_part, core)
- **Sponsor APIs:** Qualcomm Arduino Uno Q | fit: Ran edge inference and sensor reading on Arduino Uno Q hardware.
- **Repo:** public, commits 6 (before/in/after event: 0/6/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 12, writeup long, impact claims False
- **Notes:** Uses both chips of Arduino Uno Q (STM32 sensors, Qualcomm processor); Edge Impulse litter-detection model; fixed inter-chip messaging by downgrading the RTOS; three repos.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor
- **Links:** [Devpost](https://devpost.com/software/djubrino) | [GitHub](https://github.com/ColG-02/backend_hackupc)

### FestiCleaner  (HackUPC 2026)

- **Prizes:** [Qualcomm] 2nd place [2nd]  (tier: sponsor_winner)
- **Pitch:** Autonomous trash-collecting robot built from recycled materials on Arduino Uno Q with onboard vision and a live control dashboard.
- **Problem / user:** Festival venues in Barcelona are left littered and cleanup needs heavy manual work. / venue operators and city cleaning crews
- **Domain / idea type:** sustainability_climate / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision
- **Stack:** langs C; Python; JavaScript; frontend React; Bun; backend FastAPI; db ; hosting 
- **Tech/APIs:** Arduino Uno Q (hardware_part, core, sponsor); Edge Impulse (ai_model, core); YOLOv8 (ai_model, unclear); FastAPI (framework, supporting); React (framework, supporting); Bun (framework, supporting)
- **Sponsor APIs:** Qualcomm Arduino Uno Q | fit: Autonomous robot with onboard edge inference on Arduino Uno Q.
- **Repo:** public, commits 29 (before/in/after event: 0/29/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Cardboard and jar-lid chassis; trash detection by Edge Impulse/YOLOv8 model run on the board with no external compute; motors too weak so power bank is lifted by hand.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor
- **Links:** [Devpost](https://devpost.com/software/festicleaner) | [GitHub](https://github.com/iRobo1/FestiCleaner)

### guAIta  (HackUPC 2026)

- **Prizes:** [Qualcomm] 3rd place [3rd]  (tier: sponsor_winner)
- **Pitch:** Edge stations on Arduino Uno Q detect wild boars, score risk on a map dashboard and place ElevenLabs voice calls to authorities.
- **Problem / user:** Wild boar spread in Catalonia raises African swine fever containment costs. / Catalan authorities and field teams
- **Domain / idea type:** safety_security + sustainability_climate / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision; speech_or_voice
- **Stack:** langs TypeScript; frontend React; Vite; MapLibre; Tailwind; backend Node.js; Fastify; Zod; db SQLite; hosting 
- **Tech/APIs:** Arduino Uno Q (hardware_part, core, sponsor); Edge Impulse FOMO (ai_model, core); ElevenLabs (ai_model, core, sponsor); Fastify (framework, supporting); Socket.IO (framework, supporting); MapLibre GL JS (maps_geo, supporting); SQLite (database, supporting)
- **Sponsor APIs:** Qualcomm Arduino Uno Q; ElevenLabs | fit: Edge detection on Arduino Uno Q with local inference.
- **Repo:** public, commits 86 (before/in/after event: 0/85/1), README detailed
- **Demo/writeup:** video False, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Edge Impulse FOMO model with 20-frame rolling confidence filter (threshold 0.7); events flow to Fastify/Socket.IO server and MapLibre dashboard; automated voice escalation.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor
- **Links:** [Devpost](https://devpost.com/software/guaita) | [GitHub](https://github.com/guimCC/guAIta)

### hpcp  (HackUPC 2026)

- **Prizes:** [HP] 2nd place [2nd]  (tier: sponsor_winner)
- **Pitch:** Physics-based simulator of Metal Jet S100 components with true versus sensor-observed state and a tool-using chat copilot that must cite run, tick and component.
- **Problem / user:** Printer components age, sensors drift, and an assistant must never invent numbers. / printer operators and maintenance engineers
- **Domain / idea type:** energy_utilities + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; TypeScript; frontend SvelteKit; backend FastAPI; Convex; db SQLite; hosting Docker
- **Tech/APIs:** Gemma 4 via OpenRouter (ai_model, core); Convex agent (framework, core); FastAPI (framework, supporting); SQLite (database, core); SvelteKit (framework, core); Streamlit (framework, supporting); Docker (other, supporting)
- **Sponsor APIs:**  | fit: Simulator and grounded co-pilot for the HP Metal Jet S100 challenge.
- **Repo:** public, commits 141 (before/in/after event: 0/140/1), README detailed
- **Demo/writeup:** video False, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Deterministic seeded simulation with coupled wear laws (Archard, Coffin-Manson, Arrhenius); maintenance agent sees only observed state; Convex agent with nine tools over a SQLite historian.
- **Team size:** 5 | **Confidence:** high | unverified: domain_primary
- **Links:** [Devpost](https://devpost.com/software/metalmind) | [GitHub](https://github.com/stickerdaniel/hackUPC)

### JetSense: AI agents for printers.  (HackUPC 2026)

- **Prizes:** [HP] 1st place [1st]  (tier: sponsor_winner)
- **Pitch:** Predictive-maintenance dashboard for HP Metal Jet S100 printers with stochastic degradation model, PPO repair scheduler and voice-enabled AI assistant.
- **Problem / user:** Industrial metal 3D printers fail unpredictably; fixed-schedule or reactive repairs are wasteful or costly. / printer operators and maintenance teams
- **Domain / idea type:** energy_utilities + dev_tools / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs Python; JavaScript; frontend Next.js; React; backend Flask; db Supabase; hosting Vercel; Hugging Face
- **Tech/APIs:** PyTorch (framework, core); PPO reinforcement learning (ai_model, core); Next.js (framework, core); Flask (framework, supporting); Supabase (database, supporting); Hugging Face (cloud, supporting); Vercel (cloud, supporting); Blender (other, supporting)
- **Sponsor APIs:**  | fit: Predictive maintenance model for the HP Metal Jet S100 challenge.
- **Repo:** public, commits 100 (before/in/after event: 0/94/6), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 2, writeup long, impact claims False
- **Notes:** Models part health with differential equations and L1-regularized rates; PPO agent picks among 512 joint replacement combinations under a budget; 3D printer model in dashboard; email alerts.
- **Team size:** 2 | **Confidence:** high | unverified: mislabeled_domain
- **Links:** [Devpost](https://devpost.com/software/jetsense-ai-agents-for-printers) | [GitHub](https://github.com/Litusiano/hackupc-2026)

### OpenPlanner  (HackUPC 2026)

- **Prizes:** [Jetbrains] 2nd place [2nd]  (tier: sponsor_winner)
- **Pitch:** Cursor/VS Code sidebar extension that keeps AI-agent work as a JSON tree of plans, phases and tasks and runs phases through an agent CLI.
- **Problem / user:** Plans for AI-assisted coding get scattered across chat, and context is lost between sessions. / developers using AI coding agents
- **Domain / idea type:** dev_tools + productivity_workplace / dev_tool
- **Platforms / hardware / AI:** desktop / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; frontend ; backend Node.js; db MongoDB Atlas (optional); hosting 
- **Tech/APIs:** Cursor CLI (other, core); VS Code extension API (framework, core); JetBrains Junie (other, token, sponsor); MongoDB Atlas (database, supporting)
- **Sponsor APIs:**  | fit: Developer tool for planning and handing off agent work in editors.
- **Repo:** public, commits 101 (before/in/after event: 0/101/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 3, writeup long, impact claims False
- **Notes:** Plans stored as plain JSON on disk (source of truth); webview streaming buffered with replay and truncation; optional last-write-wins MongoDB Atlas sync.
- **Team size:** 4 | **Confidence:** high | unverified: sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/openplanner) | [GitHub](https://github.com/NatanSisoev/OpenPlanner)

### PearPost  (HackUPC 2026)

- **Prizes:** [Skyscanner] 1st place [1st]  (tier: sponsor_winner)
- **Pitch:** Peer-to-peer inbox protocol letting personal AI agents discover each other, exchange encrypted typed messages and call tools, with a graph desktop UI.
- **Problem / user:** AI agents live in isolated apps and cannot coordinate directly without a central server. / people running personal AI agents
- **Domain / idea type:** ai_agents_infra + dev_tools / dev_tool
- **Platforms / hardware / AI:** desktop; cli / False / agent_or_tool_use
- **Stack:** langs JavaScript; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Pears runtime (framework, core, sponsor); Hyperswarm (framework, core, sponsor); Hypercore (framework, core, sponsor); Hyperbee (framework, core, sponsor); Autobase (framework, supporting, sponsor); Hyperdrive (framework, supporting, sponsor); sodium-native (framework, supporting); Hermes agent (other, supporting); OpenClaw (other, supporting)
- **Sponsor APIs:** Pears | fit: Serverless P2P agent messaging on Pears/Hypercore; writeup also argues fit to other sponsor tracks.
- **Repo:** public, commits 32 (before/in/after event: 0/32/0), README solid
- **Demo/writeup:** video False, live none, screenshots 0, writeup long, impact claims False
- **Notes:** Agent addresses (pear+agent://), Hypercore outboxes, Hyperbee inboxes, integrations for Hermes and OpenClaw agents, CLI and live agent-graph UI; writeup maps fit to four sponsor tracks.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/bot-com) | [GitHub](https://github.com/EternalRecursion121/post)

### PearUp  (HackUPC 2026)

- **Prizes:** [HackUPC] 2nd place [2nd]  (tier: overall_top3)
- **Pitch:** Fully peer-to-peer dating app where each device trains a local model on swipes and only shares weight updates via federated averaging.
- **Problem / user:** Dating apps centralize sensitive swipe data on servers. / dating app users
- **Domain / idea type:** social_community / new_category
- **Platforms / hardware / AI:** desktop / False / predictive_ml; recommendation
- **Stack:** langs JavaScript; frontend Electron; Chart.js; backend Pear; Bare runtime; db ; hosting 
- **Tech/APIs:** Pear (Holepunch) (framework, core, sponsor); Hyperswarm (framework, core, sponsor); Hypercore (framework, core, sponsor); Autobase (framework, supporting, sponsor); TensorFlow.js (framework, supporting); Electron (framework, supporting); Chart.js (framework, supporting)
- **Sponsor APIs:** Pear (Holepunch)
- **Repo:** public, commits 40 (before/in/after event: 0/40/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 1, writeup long, impact claims False
- **Notes:** Built on Pear/Holepunch stack (Hyperswarm, Hypercore, Autobase) with a from-scratch pure-JS neural network for the Bare runtime and a live convergence dashboard.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor flags
- **Links:** [Devpost](https://devpost.com/software/pearup-fpg8sy) | [GitHub](https://github.com/mserra0/dfl-pears)

### Roam  (HackUPC 2026)

- **Prizes:** [Skyscanner] 3rd place [3rd]  (tier: sponsor_winner)
- **Pitch:** Chrome extension that watches Instagram and TikTok scrolling behavior to score travel destinations by hidden intent, showing live Skyscanner flight prices.
- **Problem / user:** People's real travel desire shows in scrolling behavior, not in what they search. / social media users planning travel
- **Domain / idea type:** mobility_transport / new_category
- **Platforms / hardware / AI:** browser_extension / False / llm_chat
- **Stack:** langs TypeScript; frontend ; backend Express.js; db MongoDB Atlas; hosting Railway
- **Tech/APIs:** Skyscanner API (data_source, core, sponsor); Gemma 4 via Gemini API (ai_model, supporting); MongoDB Atlas (database, supporting); Express.js (framework, supporting); Railway (cloud, supporting)
- **Sponsor APIs:** Skyscanner API | fit: Shows cheapest live Skyscanner flights with booking deeplinks for each detected destination.
- **Repo:** public, commits 25 (before/in/after event: 0/25/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Eleven engagement signals with non-linear dwell weighting and 7-day half-life decay feed a plain-math score; Gemma 4 only detects destinations and writes summaries; built solo.
- **Team size:** 1 | **Confidence:** high | unverified: team_size
- **Links:** [Devpost](https://devpost.com/software/roam-yxus4c) | [GitHub](https://github.com/expires/skyscanner-upc)

### Slap  (HackUPC 2026)

- **Prizes:** [Bending Spoons] 1st place [1st]  (tier: sponsor_winner)
- **Pitch:** Slack bot that uses Gemini to turn non-technical issue reports into structured pending GitHub issues, with notification and a tracking dashboard.
- **Problem / user:** Non-technical staff lose time relaying small website errors to developers. / non-technical teams and developers
- **Domain / idea type:** productivity_workplace + dev_tools / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / llm_chat; agent_or_tool_use
- **Stack:** langs JavaScript; frontend Next.js; React; Vite; backend Express.js; db ; hosting 
- **Tech/APIs:** Gemini API (ai_model, core); Slack API (other, core); GitHub API (Octokit) (other, core); Express.js (framework, supporting); Next.js (framework, supporting)
- **Sponsor APIs:**  | fit: Workflow bot for the Bending Spoons track turning messages into GitHub issues.
- **Repo:** public, commits 52 (before/in/after event: 0/48/4), README detailed
- **Demo/writeup:** video False, live none, screenshots 0, writeup long, impact claims False
- **Notes:** Writeup is README-style and still contains template text ('adjust this section'); developers approve issues before action.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots; tech_items depth
- **Links:** [Devpost](https://devpost.com/software/slap-f6nxiq) | [GitHub](https://github.com/mogonlac/hackupc2026)

### Smadex Creative Copilot  (HackUPC 2026)

- **Prizes:** [HackUPC] 3rd place [3rd]  (tier: overall_top3)
- **Pitch:** Self-contained ML dashboard for ad creatives with SHAP explanations, clusters and a Gemini chatbot with function calling over the dataset.
- **Problem / user:** Advertisers need to understand why a creative wins or fatigues. / advertisers and marketers
- **Domain / idea type:** retail_consumer / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; predictive_ml
- **Stack:** langs Python; JavaScript; frontend Chart.js; HTML; backend Python pipeline; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, core); scikit-learn (framework, core); SHAP (framework, core); XGBoost (framework, supporting); Chart.js (framework, supporting); Pillow (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 7 (before/in/after event: 0/7/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 0, writeup long, impact claims False
- **Notes:** Team new to ML; KMeans personas written by Gemini from SHAP profiles; portfolio optimizer using PCA cosine distance; single HTML file with injected API key; credits Claude as coding aid.
- **Team size:** 2 | **Confidence:** medium | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/smadex-creative-copilot) | [GitHub](https://github.com/lalig777/Smadex-Challenge)

### Smadex Creative Lab  (HackUPC 2026)

- **Prizes:** [Smadex] 1st place [1st]  (tier: sponsor_winner)
- **Pitch:** Ad-tech dashboard that scores creative survivability, forecasts fatigue with hazard models and explains results with SHAP and Gemma 4 insights.
- **Problem / user:** Advertisers only discover creative fatigue after money is lost. / advertisers and marketers
- **Domain / idea type:** retail_consumer / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; Vite; Tailwind; backend FastAPI; Node.js; db PostgreSQL; hosting Docker
- **Tech/APIs:** Gemma 4 (ai_model, core); SHAP (framework, supporting); FastAPI (framework, supporting); PostgreSQL (database, supporting); React (framework, supporting)
- **Sponsor APIs:**  | fit: Dashboard for Smadex ad creative performance data.
- **Repo:** public, commits 87 (before/in/after event: 0/87/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Gemma 4 runs in a separate Node.js agent streaming via SSE; hazard models and PCA portfolio map; Survivability Lab health scores.
- **Team size:** 3 | **Confidence:** medium | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/smadex-creative-lab) | [GitHub](https://github.com/jowelhub/HACK_UPC_SMADEX)

### SmadexAd Courtroom  (HackUPC 2026)

- **Prizes:** [Smadex] 2nd place [2nd]  (tier: sponsor_winner)
- **Pitch:** Five specialized AI agents debate an ad creative over three rounds and deliver a weighted verdict (scale, pause, pivot, test next) with a readable transcript.
- **Problem / user:** Marketers see what happened in dashboards but not why a creative performs. / advertisers and marketers
- **Domain / idea type:** retail_consumer + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; vision
- **Stack:** langs Python; frontend Streamlit; backend FastAPI; Pydantic; db DuckDB; SQLite; hosting Render
- **Tech/APIs:** Gemma via Ollama (ai_model, core); FastAPI (framework, core); DuckDB (database, supporting); Streamlit (framework, core); Pydantic (framework, supporting)
- **Sponsor APIs:**  | fit: Multi-agent analysis of Smadex ad creative data.
- **Repo:** public, commits 57 (before/in/after event: 0/57/0), README solid
- **Demo/writeup:** video False, live not_checked, screenshots 11, writeup long, impact claims False
- **Notes:** Custom A2A protocol with each agent a FastAPI microservice using Pydantic messages, no agent framework; fatigue from 7-day CTR slope; Streamlit transcript UI deployed on Render.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/ad-courtroom) | [GitHub](https://github.com/GuillermoCalet/HACKUPC-2-26)

### Warehouse Yasolizer  (HackUPC 2026)

- **Prizes:** [Mecalux] 3rd place [3rd]  (tier: sponsor_winner)
- **Pitch:** Warehouse bay-placement optimizer maximizing used area at minimum cost, built with GPU parallelism in C++/OpenGL.
- **Problem / user:** Placing storage bays to maximize area and minimize cost. / warehouse planners
- **Domain / idea type:** productivity_workplace / data_or_analytics
- **Platforms / hardware / AI:** desktop / False / llm_chat
- **Stack:** langs C++; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Claude (ai_model, supporting); Gemini (ai_model, token); OpenGL (framework, core); Antigravity (other, unclear)
- **Sponsor APIs:**  | fit: Optimization for the Mecalux warehouse layout challenge.
- **Repo:** public, commits 12 (before/in/after event: 0/11/1), README detailed
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Very thin writeup; says a Gemini-made prompt was handed to Claude to scaffold the project; GPU pipelining mentioned as a challenge.
- **Team size:** 4 | **Confidence:** medium | unverified: ai_used; ai_types; n_screenshots; team_size
- **Links:** [Devpost](https://devpost.com/software/warehouse-yasolizer) | [GitHub](https://github.com/Carlos-Prlt/HackUPC_2026)
