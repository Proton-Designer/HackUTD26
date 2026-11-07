# HackUTD 2024: project cards (35 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

### AllBank: Inclusive, Intelligent, Impactful  (HackUTD 2024)

- **Prizes:** Goldman Sachs [unknown]  (tier: sponsor_winner)
- **Pitch:** Mobile banking app for individuals and small businesses with QR payments, goal-based savings, loan planning and a Gemini financial assistant.
- **Problem / user:** Banking remains inaccessible for many, and traditional services lag behind modern needs. / Individuals and small businesses
- **Domain / idea type:** fintech_finance + accessibility / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / llm_chat; recommendation
- **Stack:** langs JavaScript; frontend React Native; Expo; backend Firebase; Node.js; db Firebase Firestore; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); Firebase Firestore (database, core); React Native (framework, core); Expo (framework, supporting)
- **Sponsor APIs:**  | fit: Inclusive banking app for the Goldman Sachs track; no Goldman API named.
- **Repo:** public, commits 45 (before/in/after event: 0/45/0), README solid
- **Demo/writeup:** video None, live none, screenshots 12, writeup medium, impact claims False
- **Notes:** Broad feature set (investment dashboard, doorstep banking appointments, loan calculator, analytics) in one React Native app; Gemini assistant with Firestore backend.
- **Team size:** 3 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; repo_commits; first_commit; last_commit; commits_in_event_window; ui_polish; stack_languages; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/allbank) | [GitHub](https://github.com/aprajita27/AllBank)

### Backtracc  (HackUTD 2024)

- **Prizes:** Winner Hardware [unknown]; Winner [MLH] Best AI Application Built with Cloudflare [unknown]; Winner Samba Nova [unknown]  (tier: sponsor_winner)
- **Pitch:** In-car Raspberry Pi system detects when riders leave, photographs the back seat, has a vision LLM spot forgotten items, and notifies rider and driver.
- **Problem / user:** Riders lose belongings in ride-share cars and drivers waste time and fuel returning them. / ride-share riders and drivers
- **Domain / idea type:** mobility_transport + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web; mobile_cross / True / vision; llm_chat
- **Stack:** langs TypeScript; Python; C++; frontend React; Vite; backend Express.js; Python; Docker; db Pinata key-value; hosting Render; Cloudflare
- **Tech/APIs:** SambaNova Llama 3.2 Vision 11B (ai_model, core, sponsor); Pinata (cloud, core, sponsor); Cloudflare (cloud, supporting, sponsor); Terraform (cloud, supporting, sponsor); Raspberry Pi 4 and Pico W with ultrasonic sensors (hardware_part, core); Onshape (other, token)
- **Sponsor APIs:** SambaNova; Pinata; Cloudflare; Terraform | fit: Used SambaNova-hosted Llama 3.2 Vision for item detection, Pinata for image storage and Terraform/Cloudflare for deploy and DNS.
- **Repo:** public, commits 95 (before/in/after event: 0/82/13), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 8, writeup long, impact claims False
- **Notes:** Ultrasonic sensors on a Pico W trigger a Pi 4 webcam; 3D-printed enclosure; Terraform manages Cloudflare DNS and frontend deploy; main branch protected with PRs; three codebases in three languages.
- **Team size:** 5 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; n_screenshots (gallery counter showed 9 items, one may be video); live_demo_status (site fetch blocked); domain_secondary; platforms (mobile push notification mentioned)
- **Links:** [Devpost](https://devpost.com/software/project-cd41lvjbiorw) | [GitHub](https://github.com/phamleduy04/hackutd24)

### Capsule  (HackUTD 2024)

- **Prizes:** Pinata [2nd]  (tier: sponsor_winner)
- **Pitch:** Upload files into a shareable capsule retrievable by URL, QR code or NFC card, for things like medical documents or pet tags.
- **Problem / user:** Family members lose shared documents, such as those for doctor visits, and need a simple secure way to access them. / Families, caregivers and pet owners
- **Domain / idea type:** health_wellness + productivity_workplace / new_category
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs ; frontend Next.js; TailwindCSS; ShadCN; backend Next.js; db Pinata; hosting Vercel
- **Tech/APIs:** Pinata (database, core, sponsor); QRCode library (other, supporting); Next.js (framework, core); NFC (hardware_part, unclear)
- **Sponsor APIs:** Pinata | fit: Uses Pinata file storage with per-file metadata and signed URLs as the entire storage layer.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 6, writeup short, impact claims False
- **Notes:** Built almost entirely on Pinata file metadata for grouping and ownership; signed URLs control access; QR codes or NFC cards act as physical links to a capsule.
- **Team size:** 2 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; live_demo_status; ui_polish; team_size; stack_hosting; prizes.placement; platforms
- **Links:** [Devpost](https://devpost.com/software/capsule-lp540f)

### Cheddarboxd  (HackUTD 2024)

- **Prizes:** Winner Pinata [unknown]; Winner Best Solo Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** Letterboxd-style social site where users rate and share cheeses and see what others are trying.
- **Problem / user:** Joke-driven pun on Letterboxd; no real problem is stated beyond wanting a place to share cheese tastes. / cheese enthusiasts
- **Domain / idea type:** food_nutrition + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; JavaScript; frontend SvelteKit; Tailwind; backend SvelteKit; db ; hosting Vercel (per repo link)
- **Tech/APIs:** Pinata (cloud, core, sponsor); SvelteKit (framework, core); Tailwind (framework, supporting)
- **Sponsor APIs:** Pinata | fit: Used Pinata as the storage layer and wrote about its docs being confusing but helpful when fed to an AI editor.
- **Repo:** public, commits 9 (before/in/after event: 0/8/1), README none
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup short, impact claims True (Joking target of 10M daily users and 100k monthly revenue; not a genuine claim.)
- **Notes:** Solo build with a humorous pitch (jokes about 10M DAU); Pinata file storage; ran as a PWA over local network; author used Pinata docs as Cursor context.
- **Team size:** 1 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; Pinata depth; live demo (repo README links a Vercel site, not fetched)
- **Links:** [Devpost](https://devpost.com/software/cheddarboxd) | [GitHub](https://github.com/joemmalatesta/CheddarBoxd)

### Data Pattern Observatory  (HackUTD 2024)

- **Prizes:** PNC Bank [unknown]  (tier: sponsor_winner)
- **Pitch:** Data observability dashboard that tracks data flows and uses statistical models to detect anomalies and predict future data movement.
- **Problem / user:** Organizations lack visibility into how data is created, accessed, moved and used, creating governance and security risks. / data and platform teams in enterprises
- **Domain / idea type:** dev_tools + fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; agent_or_tool_use
- **Stack:** langs Python; frontend Streamlit; backend Python; db MongoDB; Elasticsearch; TimescaleDB; Redis; hosting Docker
- **Tech/APIs:** Streamlit (framework, core); MongoDB (database, core); Elasticsearch (database, supporting); TimescaleDB (database, supporting); Redis (database, supporting); CrewAI (framework, unclear)
- **Sponsor APIs:**  | fit: Answers the PNC Bank data-observability challenge by tracking data patterns and predicting flows with business context.
- **Repo:** public, commits 5 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video None, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Combines MongoDB, Elasticsearch, TimescaleDB and Redis behind a Streamlit dashboard; a CrewAI market-crisis agent and random forest predictor are described as not yet integrated. Repo commits a vendored virtualenv.
- **Team size:** 3 | **Confidence:** medium | unverified: has_demo_video; ui_polish; n_screenshots (no gallery seen in text)
- **Links:** [Devpost](https://devpost.com/software/data-pattern-observatory) | [GitHub](https://github.com/siddhu-pikachu/data-observability.git)

### DHy-n0  (HackUTD 2024)

- **Prizes:** Winner EOG Resources [unknown]; Winner [MLH] Best .Tech Domain Name [unknown]  (tier: sponsor_winner)
- **Pitch:** Web tool that analyzes oil and gas well data to flag anomalies that may signal hydrate buildup, with mascot branding.
- **Problem / user:** Lease operators need help spotting when hydrates may be forming in wells from sensor data. / oil and gas lease operators
- **Domain / idea type:** energy_utilities + productivity_workplace / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; Recharts; backend Flask; Pandas; db ; hosting 
- **Tech/APIs:** Flask (framework, core); Pandas (framework, core); React (framework, core); Recharts (framework, supporting); .Tech domain (other, supporting, sponsor)
- **Sponsor APIs:** .Tech Domain Name | fit: EOG prize: anomaly detection on well data for hydrate prediction; MLH prize for the dhy-n0.tech domain.
- **Repo:** public, commits 19 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 2, writeup medium, impact claims False
- **Notes:** Team was new to React and Recharts; made a promo video and original mascot. Uses a custom .tech domain. Marketing is emphasised in the writeup. Domain is energy (no allowed value).
- **Team size:** 5 | **Confidence:** medium | unverified: demo_video_url (YouTube link seen as text only); ui_polish; live_demo_status; readme_quality; ai_used (anomaly detection assumed ML)
- **Links:** [Devpost](https://devpost.com/software/dhy-n0) | [GitHub](https://github.com/wenngle/dhy-n0)

### DuckTalk  (HackUTD 2024)

- **Prizes:** Guided Track [unknown]  (tier: track_winner)
- **Pitch:** Solo-built companion web app for hackathon participants with a duck mascot, a to-do list, an interactive Google Map and a five-day weather forecast.
- **Problem / user:** Out-of-state hackathon participants in an unfamiliar city can feel lonely and lack local context. / out-of-town hackathon participants
- **Domain / idea type:** social_community + productivity_workplace / entertainment_or_game
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs JavaScript; HTML; CSS; frontend React; Tailwind CSS; backend ; db Firebase; hosting 
- **Tech/APIs:** Firebase (database, core); Google Maps (maps_geo, supporting); WeatherAPI (data_source, supporting); React + Tailwind (framework, core)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Built by one person by customizing the hackathon Guided Track starter project; to-do list is hard-coded and the planned GPT chat for the duck was not implemented.
- **Team size:** 1 | **Confidence:** medium | unverified: n_screenshots; ui_polish; repo_commits; first_commit; last_commit; commits_in_event_window; readme_quality; placement
- **Links:** [Devpost](https://devpost.com/software/ducktalk)

### Echo  (HackUTD 2024)

- **Prizes:** Best Design [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Gamified web app helping neurodivergent children recognize and mimic emotions using webcam facial tracking, a 3D mascot and an emotion quiz.
- **Problem / user:** Children with autism or alexithymia struggle to read facial expressions, and conventional education rarely supports this. / neurodivergent children and their caregivers
- **Domain / idea type:** accessibility + education / social_good
- **Platforms / hardware / AI:** web / False / vision; llm_chat
- **Stack:** langs Python; JavaScript; frontend React; Next.js; Three.js; Tailwind; backend Flask; db Pinata IPFS; hosting 
- **Tech/APIs:** SambaNova API (ai_model, supporting, sponsor); Pinata API (database, supporting, sponsor); Facial landmark detection (other, core); Three.js (framework, core); Blender (other, supporting); Figma (other, supporting)
- **Sponsor APIs:** SambaNova; Pinata
- **Repo:** public, commits 25 (before/in/after event: None/None/None), README none
- **Demo/writeup:** video None, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Blender-rigged 3D mascots rendered with Three.js/WebGL, themed to HackUTD; quiz images come from Pinata IPFS and SambaNova supplies feedback. Repo has no README and a commit a year later.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ui_polish; sponsor status of Pinata/SambaNova; placement_tier (Best Design is a non-sponsor prize, tier chosen as honorable_or_finalist)
- **Links:** [Devpost](https://devpost.com/software/hackutd-project-kbhins) | [GitHub](https://github.com/chaireko/hackutd24)

### Eco Fast Track  (HackUTD 2024)

- **Prizes:** CBRE [unknown]; Veolia [unknown]  (tier: sponsor_winner)
- **Pitch:** Smart water gauge built from an Arduino and Grove sensors that feeds a web app giving property managers and tenants usage insights, alerts and AI saving tips.
- **Problem / user:** Property managers rely on tenant reports or awkward check-ins to find faulty or wasteful water usage. / property managers and apartment tenants
- **Domain / idea type:** sustainability_climate + housing_real_estate / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; recommendation
- **Stack:** langs Python; C++; JavaScript; frontend Next.js; backend Node.js; Python; db ; hosting 
- **Tech/APIs:** Arduino + Grove IoT kit (hardware_part, core); Gemini (ai_model, core); Pinata (cloud, supporting, sponsor); Next.js (framework, core); HiveMQ MQTT (other, unclear); 3D printed enclosure (hardware_part, supporting)
- **Sponsor APIs:** Pinata | fit: Water-monitoring IoT tool matching property-management and sustainability themes of the CBRE and Veolia prizes.
- **Repo:** public, commits 5 (before/in/after event: 0/4/1), README solid
- **Demo/writeup:** video True, live none, screenshots 9, writeup medium, impact claims False
- **Notes:** Working hardware prototype with a 3D-printed enclosure; planned wifi module was unreliable so data went over serial, and README mentions MQTT via HiveMQ. Spotify-Wrapped-style usage visuals; Figma and Canva decks linked.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; Pinata_depth; HiveMQ_use
- **Links:** [Devpost](https://devpost.com/software/apartment-monitoring) | [GitHub](https://github.com/Fernando4242/HackUTD24-EcoFastTrack)

### EcoLens (property evaluator)  (HackUTD 2024)

- **Prizes:** Best Beginner [unknown]  (tier: track_winner)
- **Pitch:** Swift app that analyzes a video of an office or property, detects furniture, flags wear such as rips and stains, and suggests sustainable repairs.
- **Problem / user:** Properties replace furniture too often; prioritizing repair and maintenance would cut cost and environmental impact. / office and property managers
- **Domain / idea type:** sustainability_climate + housing_real_estate / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / False / vision; llm_chat
- **Stack:** langs Swift; Python; frontend Swift; backend Python; db ; hosting 
- **Tech/APIs:** Google Cloud Vision API (ai_model, core); Llama (text and image) (ai_model, core); Pinata (cloud, supporting, sponsor); Swift (framework, core)
- **Sponsor APIs:** Pinata
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Beginner-track winner combining native Swift frontend with Google Vision labeling of extracted video frames and Llama for condition analysis; frames are stored in Pinata.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots; ui_polish; repo_commits; first_commit; last_commit; commits_in_event_window; readme_quality; placement; platforms_ios_inferred_from_Swift
- **Links:** [Devpost](https://devpost.com/software/property-evaluator)

### EcoLens (Sustainable Building Manager)  (HackUTD 2024)

- **Prizes:** Veolia [unknown]  (tier: sponsor_winner)
- **Pitch:** Dashboard for commercial buildings showing energy, water and carbon trends with sliders to simulate changes and a map of sustainability scores.
- **Problem / user:** Building operators need to see sustainability performance and test what changes would improve scores and costs. / commercial building and facilities managers
- **Domain / idea type:** sustainability_climate + productivity_workplace / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; TypeScript; frontend React; backend Flask; db ; hosting 
- **Tech/APIs:** Flask (framework, core); React (framework, core)
- **Sponsor APIs:**  | fit: Dashboard addresses the Veolia challenge on commercial building sustainability, with simulated scores and recommendations per building.
- **Repo:** public, commits 8 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video None, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Devpost writeup sections are empty apart from a one-line summary; details come from the repo README, which includes screenshots, simulation sliders and recommendations. Built against Veolia and CBRE challenges.
- **Team size:** 3 | **Confidence:** medium | unverified: has_demo_video; ui_polish; n_screenshots; ai_used (not stated)
- **Links:** [Devpost](https://devpost.com/software/ecolens-pqk62d) | [GitHub](https://github.com/Sami-ul/Sustainable-Building-Manager)

### EcoVerse  (HackUTD 2024)

- **Prizes:** CBRE [unknown]  (tier: sponsor_winner)
- **Pitch:** VR platform where property managers explore virtual offices, view live energy and water data, talk to an AI assistant and feel inefficiencies through haptic gloves.
- **Problem / user:** Corporate buildings struggle with energy and water efficiency, raising costs and carbon footprint. / Commercial property managers and remote technicians
- **Domain / idea type:** sustainability_climate + housing_real_estate / new_category
- **Platforms / hardware / AI:** desktop; hardware / True / llm_chat; recommendation
- **Stack:** langs C#; Python; frontend Unity; backend Streamlit; db ; hosting 
- **Tech/APIs:** Unity (framework, core); SambaNova API with Llama (ai_model, core, sponsor); bHaptics SDK and gloves (hardware_part, core); Photon (framework, supporting); Streamlit (framework, supporting); Faker (data_source, supporting); Ready Player Me (other, supporting); Blender (other, supporting)
- **Sponsor APIs:** SambaNova | fit: Office-building sustainability monitoring in VR for the CBRE track; also uses SambaNova's API for the assistant.
- **Repo:** public, commits 66 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video None, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Unity VR with bHaptics thermo-tactile gloves, Photon multiplayer for remote technicians, lip-synced AI avatar, and Streamlit data streamed to Unity over sockets using Faker-generated data.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; repo_commits; first_commit; last_commit; commits_in_event_window; ui_polish; team_size; platforms; stack_languages; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/ecoverse-5dczmp) | [GitHub](https://github.com/FireboltLegend/HackUTD-2024)

### FinnAI  (HackUTD 2024)

- **Prizes:** PNC Bank [unknown]  (tier: sponsor_winner)
- **Pitch:** Personal finance app with an AI budgeting chatbot, automatic expense categorisation, savings goals and analytics dashboards.
- **Problem / user:** Budgeting and saving feel complex and daunting for many people. / Everyday consumers managing personal budgets
- **Domain / idea type:** fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; recommendation
- **Stack:** langs Python; frontend Streamlit; backend Firebase; db Firebase; hosting 
- **Tech/APIs:** Streamlit (framework, core); Firebase (database, core)
- **Sponsor APIs:**  | fit: Personal finance assistant for the PNC Bank track; no PNC API named.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots None, writeup long, impact claims False
- **Notes:** Streamlit front end with Firebase storage; the writeup describes an in-house trained chatbot but names no specific model or API.
- **Team size:** 5 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; n_screenshots; ui_polish; team_size; ai_types
- **Links:** [Devpost](https://devpost.com/software/finnai)

### FrontierMap  (HackUTD 2024)

- **Prizes:** Frontier [unknown]  (tier: sponsor_winner)
- **Pitch:** iOS RoomPlan app scans a home in AR, then a web app flattens the model to a floor plan and recommends Wi-Fi extender spots with a coverage heatmap.
- **Problem / user:** Frontier internet customers have weak Wi-Fi in parts of the home and do not know where to put extenders. / home internet customers (Frontier)
- **Domain / idea type:** telecom_networking + retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios; web / False / False
- **Stack:** langs Swift; Python; TypeScript; frontend Next.js; Tailwind; SwiftUI; UIKit; backend Flask; Python; db ; hosting Vercel; Cloudflare
- **Tech/APIs:** Apple RoomPlan (framework, core); Flask (framework, core); Next.js (framework, core); Pinata (cloud, unclear, sponsor); Cloudflare (cloud, unclear, sponsor)
- **Sponsor APIs:** Pinata; Cloudflare | fit: Targeted the Frontier challenge with a Wi-Fi extender placement tool for home internet users; Pinata and Cloudflare listed in Built With.
- **Repo:** public, commits 33 (before/in/after event: 0/33/0), README thin
- **Demo/writeup:** video True, live working, screenshots 4, writeup long, impact claims False
- **Notes:** Pipeline from Apple RoomPlan USDZ scan through Python 3D-to-2D flattening to a Next.js heatmap; offers sample USDZ file for judges; two hosted URLs listed.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; Pinata and Cloudflare depth; readme_quality; github_url (Devpost repo button was the .usdz file link; repo root derived from it)
- **Links:** [Devpost](https://devpost.com/software/frontierbeyond) | [GitHub](https://github.com/davidgamingvn/extended-frontier)

### FUELICIENT  (HackUTD 2024)

- **Prizes:** Toyota [1st]  (tier: sponsor_winner)
- **Pitch:** Streamlit app for exploring Toyota fuel-efficiency data with per-account saved analyses and CSV export.
- **Problem / user:** Large provided datasets are comprehensive but hard to explore and analyses are not retained between sessions. / people analyzing vehicle fuel-efficiency data
- **Domain / idea type:** mobility_transport + sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; frontend Streamlit; backend Python; db Firebase; Pinata IPFS; hosting Streamlit Cloud; GitHub Pages
- **Tech/APIs:** Toyota fuel-efficiency data (data_source, core, sponsor); Streamlit (framework, core); Pinata (database, supporting, sponsor); Firebase (auth, supporting); Pandas (framework, core)
- **Sponsor APIs:** Toyota data; Pinata | fit: Built an explorer on Toyota's fuel-efficiency datasets with saved per-user analyses.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 2, writeup short, impact claims False
- **Notes:** Page badge states First Place Toyota Track. Stores data on Pinata/IPFS, uses Firebase for login and settings, and has several hosted links including a Streamlit app and .tech domain.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ui_polish; live_demo_status; Pinata sponsor status
- **Links:** [Devpost](https://devpost.com/software/fuelicient)

### GitFile  (HackUTD 2024)

- **Prizes:** [MLH] Best Use of Terraform [unknown]  (tier: sponsor_winner)
- **Pitch:** Git wrapper written in C that stores only differences between versions of flat files like PDFs, shown in a web dashboard with an SSH terminal and cost comparison.
- **Problem / user:** Businesses keep full backup copies of mostly unchanged documents, which multiplies storage, bandwidth and latency costs. / businesses storing document backups
- **Domain / idea type:** dev_tools + productivity_workplace / dev_tool
- **Platforms / hardware / AI:** web; cli / False / False
- **Stack:** langs C; JavaScript; frontend Next.js; PDF.js; backend Node.js; Express.js; Git; SSH; db Pinata (git history storage); hosting Azure; Cloudflare
- **Tech/APIs:** Terraform (cloud, core, sponsor); Azure (cloud, core); Pinata (cloud, core, sponsor); Cloudflare DNS (cloud, supporting, sponsor); Git (C wrapper) (framework, core); PDF.js (framework, supporting)
- **Sponsor APIs:** Terraform; Pinata; Cloudflare | fit: Used Terraform to provision the Azure VM, networking and gateways hosting the demo, which matched the MLH Terraform prize.
- **Repo:** public, commits 20 (before/in/after event: 0/20/0), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup long, impact claims True (Claims over 500x storage cost reduction from its own benchmarks.)
- **Notes:** Proof-of-concept with custom C commands around git, Terraform-provisioned Azure VM, restricted SSH session embedded in an iframe, and PDF.js in-terminal editing; Pinata stores history.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; live_demo_status (site fetch blocked)
- **Links:** [Devpost](https://devpost.com/software/gitfile) | [GitHub](https://github.com/ssaniya-dev/GitFile)

### Greenify  (HackUTD 2024)

- **Prizes:** CBRE [unknown]  (tier: sponsor_winner)
- **Pitch:** Sustainability platform for office property managers with an emissions calculator and score, a GPT-4 advice chatbot, and a Leaflet map of CBRE locations scored with LLaMA 3.
- **Problem / user:** Property managers need practical insight into office emissions and clear steps to make buildings more sustainable. / commercial property managers (CBRE)
- **Domain / idea type:** sustainability_climate + housing_real_estate / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; predictive_ml
- **Stack:** langs TypeScript; Python; frontend Next.js; React; Tailwind; Leaflet; Chart.js; D3.js; Three.js; Framer Motion; backend Flask; db MongoDB; Pinecone; hosting 
- **Tech/APIs:** OpenAI GPT-4 (ai_model, core); LLaMA 3 (ai_model, core); Pinecone (database, core); Leaflet / Google Maps (maps_geo, supporting); CBRE emissions reports (data_source, core, sponsor); MongoDB (database, supporting)
- **Sponsor APIs:** CBRE data | fit: Built for the CBRE challenge using CBRE environmental report data to power the RAG chatbot and nationwide emissions map.
- **Repo:** public, commits 26 (before/in/after event: 0/24/2), README thin
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** RAG pipeline built from CBRE environmental report PDFs parsed with Llama and stored in Pinecone; three repos listed on Devpost; README lists gamification feature.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; repo_commits (main repo only; two more repos listed)
- **Links:** [Devpost](https://devpost.com/software/greenwise-y6o4bu) | [GitHub](https://github.com/yfshaikh/greenify)

### Hermes  (HackUTD 2024)

- **Prizes:** PNC Bank [unknown]  (tier: sponsor_winner)
- **Pitch:** Crypto wallet and investing app for people without traditional banking, showing balance, credit score, live crypto prices, price predictions and risk analysis.
- **Problem / user:** Underserved people lacking traditional banking and social security have little access to financial and retirement tools. / unbanked and underserved people, especially Hispanic communities
- **Domain / idea type:** fintech_finance + social_community / social_good
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; Chart.js; Axios; backend FastAPI; Pandas; PyTorch; scikit-learn; db ; hosting 
- **Tech/APIs:** CoinGecko API (data_source, core); CryptoNews API (data_source, supporting); PyTorch LSTM (ai_model, core); FastAPI (framework, core); Chart.js (framework, supporting)
- **Sponsor APIs:**  | fit: Bank-sponsor prize entry offering banking-style balance and credit score views plus investing for underserved users.
- **Repo:** public, commits 19 (before/in/after event: 0/19/0), README none
- **Demo/writeup:** video True, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Uses an LSTM price-prediction model built in PyTorch plus live CoinGecko data; repo has node_modules, venv and .env committed. Linked branch is a personal branch of the repo.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; repo_commits_branch_only; balance_and_credit_score_real_or_mock
- **Links:** [Devpost](https://devpost.com/software/hermes-c2onvq) | [GitHub](https://github.com/AndrewG4404/HackUTD)

### Homelander  (HackUTD 2024)

- **Prizes:** Frontier [unknown]  (tier: sponsor_winner)
- **Pitch:** Data-driven app recommending home internet products from usage and outage data while giving the company outage prediction and statistics.
- **Problem / user:** Customers need simpler plan and product choices tied to their bandwidth, and providers want insight into datasets and outage risk. / home internet customers and telecom providers
- **Domain / idea type:** telecom_networking + retail_consumer / data_or_analytics
- **Platforms / hardware / AI:** web / False / recommendation; predictive_ml
- **Stack:** langs Python; frontend React; backend ; db ; hosting 
- **Tech/APIs:** React (framework, core); Python (framework, core); Frontier datasets (data_source, core, sponsor)
- **Sponsor APIs:** Frontier data | fit: Uses Frontier-style network and outage datasets to drive plan and add-on recommendations.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 0, writeup medium, impact claims False
- **Notes:** Recommendation logic is described as simple threshold rules on connections and bandwidth plus outage-per-city datasets. Demo hosted on a custom subdomain.
- **Team size:** 3 | **Confidence:** medium | unverified: has_demo_video; ui_polish; n_screenshots; live_demo_status; ai_types
- **Links:** [Devpost](https://devpost.com/software/homelander)

### InvestIQ  (HackUTD 2024)

- **Prizes:** First Place [1st]; Infosys [unknown]  (tier: sponsor_winner)
- **Pitch:** Chat-based investing platform where beginners describe trading strategies in plain language, get them backtested on simulated data, and receive AI feedback including chart analysis.
- **Problem / user:** Beginners and non-coders find investing and algorithmic trading overwhelming and cannot build or test strategies. / beginner and non-technical investors
- **Domain / idea type:** fintech_finance + education / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; vision; rag_or_search
- **Stack:** langs Python; JavaScript; frontend Next.js; backend Flask; db ; hosting 
- **Tech/APIs:** SambaNova Cloud (Llama 3.1 8B, Llama 90B Vision) (ai_model, core, sponsor); Autogen (framework, core); Cohere embeddings (ai_model, supporting); Perplexity (ai_model, supporting); Next.js (framework, core); Flask (framework, core)
- **Sponsor APIs:** SambaNova Cloud | fit: Infosys prize; the writeup does not describe any Infosys-specific product use, only a finance education and strategy-testing tool.
- **Repo:** public, commits 36 (before/in/after event: 0/33/3), README thin
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Multi-agent setup (Autogen) on SambaNova-hosted Llama models, with Llama 90B Vision reading generated performance graphs. Also entered in a separate Lightning Fast AI Hackathon where it holds the First Place badge.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; Infosys_placement; First_Place_event_attribution_check; SambaNova_sponsor_status_for_HackUTD
- **Links:** [Devpost](https://devpost.com/software/investiq-1b0cio) | [GitHub](https://github.com/krish-shar/hackutd-ripple-effect)

### KaizenDrive  (HackUTD 2024)

- **Prizes:** Toyota [unknown]  (tier: sponsor_winner)
- **Pitch:** Streamlit dashboard of four years of Toyota car data with competitor comparison, a custom dashboard builder, and a RAG chatbot that answers data questions.
- **Problem / user:** Engineers waste time on local setup and tooling errors before they can explore automotive data. / automotive engineers and analysts
- **Domain / idea type:** mobility_transport + dev_tools / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; frontend Streamlit; backend Python; Pandas; NumPy; Seaborn; db Pinata (file storage); hosting 
- **Tech/APIs:** OpenAI API (ai_model, core); SentenceTransformers (ai_model, core); Streamlit (framework, core); Pinata (cloud, unclear, sponsor); Toyota vehicle dataset (data_source, core, sponsor)
- **Sponsor APIs:** Toyota dataset; Pinata | fit: Built dashboards and a RAG chatbot over the Toyota-provided car dataset for the Toyota challenge.
- **Repo:** public, commits 57 (before/in/after event: 0/57/0), README none
- **Demo/writeup:** video True, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Team first tried an open-source model for the chatbot but dropped it as too expensive to train in time; Devpost links a Google Drive file instead of a hosted app.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; readme_quality; github_url (from queue; not seen in links on Devpost page); Pinata depth; Google Drive link not opened
- **Links:** [Devpost](https://devpost.com/software/project-ip7kgx0314sh) | [GitHub](https://github.com/srutiswathi/hackUTD_24)

### Lumo  (HackUTD 2024)

- **Prizes:** General [unknown]; Goldman Sachs [unknown]  (tier: track_winner)
- **Pitch:** Group expense splitting app that charges each participant card at the moment of purchase instead of having one person front the money and be reimbursed later.
- **Problem / user:** Unbanked and underbanked people sharing rent and groceries rely on informal pooling or post-payment reimbursement, which is unreliable. / unbanked and underbanked groups, college-age roommates
- **Domain / idea type:** fintech_finance + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; JavaScript; frontend React; Vite; Tailwind CSS; Zustand; backend Node.js; Express; db MongoDB; hosting 
- **Tech/APIs:** Stripe (payments, core); MongoDB / Mongoose (database, core, sponsor); React + Vite (framework, core); Zustand (framework, supporting); Bolt / Cursor (dev aids) (other, token)
- **Sponsor APIs:**  | fit: Goldman Sachs prize entry is a fintech tool for real-time shared payments aimed at unbanked and underbanked users.
- **Repo:** public, commits 4 (before/in/after event: 0/4/0), README thin
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Claims a working MVP processing real card transactions through Stripe; could not get Stripe POS access for Apple Cash in time. Team used AI coding tools Bolt and Cursor.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; readme_quality; Stripe_sponsor_status; platforms
- **Links:** [Devpost](https://devpost.com/software/pay-your-daddy) | [GitHub](https://github.com/danielodicho/lumo)

### Monch  (HackUTD 2024)

- **Prizes:** Pinata [1st]  (tier: sponsor_winner)
- **Pitch:** Website that estimates calories and macros from a photo of a meal using a self-trained food image classifier and a public nutrition dataset, with Pinata file storage.
- **Problem / user:** Manual macro tracking is tedious, many meals lack nutrition labels, and existing trackers paywall features. / people tracking calories and macros
- **Domain / idea type:** food_nutrition + health_wellness / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs Python; JavaScript; frontend Next.js; React; Clerk; backend Flask; db ; hosting Vercel
- **Tech/APIs:** Pinata file storage (cloud, core, sponsor); Custom food image classifier (TFLite) (ai_model, core); Public nutrition dataset (data_source, core); Clerk (auth, supporting); Next.js (framework, core)
- **Sponsor APIs:** Pinata | fit: Used Pinata file storage to hold uploaded meal photos alongside the nutrition data shown on the site.
- **Repo:** public, commits 22 (before/in/after event: 0/22/0), README none
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup medium, impact claims False
- **Notes:** Trains its own neural-network food classifier (Food101-style TFLite model in backend repo) rather than calling a hosted LLM; stores meal images in Pinata. Team says it was their first ML project. Linked repo is a fork of the backend.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; team_size; readme_quality; stack_languages; stack_backend; stack_hosting; placement_from_queue_label_only
- **Links:** [Devpost](https://devpost.com/software/monch-e5k0hv) | [GitHub](https://github.com/PerdoGarcia/monch-backend)

### Notable  (HackUTD 2024)

- **Prizes:** Samba Nova [unknown]  (tier: sponsor_winner)
- **Pitch:** AI note-taking app with real-time lecture transcription, natural-language editing, diagram generation, sharing, PDF export and a voice assistant.
- **Problem / user:** Traditional note apps cannot organise or enhance content intelligently during live lectures and technical talks. / Students and developers taking lecture notes
- **Domain / idea type:** education + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; agent_or_tool_use; rag_or_search; generative_media
- **Stack:** langs Python; TypeScript; frontend React; Vite; TailwindCSS; backend FastAPI; db Supabase; SQLite; ChromaDB; hosting AWS (Terraform); Vercel
- **Tech/APIs:** SambaNova API (Llama) (ai_model, core, sponsor); CrewAI (framework, supporting); ChromaDB (database, supporting); Supabase (auth, supporting); AWS S3 and SageMaker (cloud, supporting); Terraform (other, supporting); Databricks (data_source, unclear)
- **Sponsor APIs:** SambaNova | fit: Argues SambaNova's fast inference made real-time transcription and note enhancement feasible; SambaNova API is central to the backend.
- **Repo:** public, commits 22 (before/in/after event: 0/22/0), README thin
- **Demo/writeup:** video None, live not_checked, screenshots 2, writeup long, impact claims False
- **Notes:** SambaNova inference chosen for low-latency live transcription and editing; CrewAI adds web context; ChromaDB persists context; infrastructure defined in Terraform on AWS with SageMaker.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; live_demo_status; repo_commits; first_commit; last_commit; commits_in_event_window; readme_quality; ui_polish; team_size
- **Links:** [Devpost](https://devpost.com/software/pipeview) | [GitHub](https://github.com/nsiyu/HackUTD25)

### PipeBrAIns  (HackUTD 2024)

- **Prizes:** EOG Resources [unknown]  (tier: sponsor_winner)
- **Pitch:** Random-forest model trained on the sponsor dataset predicts hydrate blockages in oil pipelines, shown on a dashboard with live alerts and email notices.
- **Problem / user:** Hydrate blockages in oil and gas pipelines are dangerous and harmful to the environment and hard to catch early. / pipeline owners and operators
- **Domain / idea type:** safety_security + sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; Tailwind; backend Flask; Node.js (server.js in repo); scikit-learn; NumPy; Pandas; SendGrid; db ; hosting 
- **Tech/APIs:** scikit-learn random forest (ai_model, core); EOG pipeline datasets (data_source, core, sponsor); Firebase Auth (auth, supporting); SendGrid (other, supporting); Flask (framework, supporting)
- **Sponsor APIs:** EOG Resources datasets | fit: Trained a hydrate-prediction model directly on the datasets supplied by EOG Resources for its challenge.
- **Repo:** public, commits 31 (before/in/after event: 0/29/2), README none
- **Demo/writeup:** video True, live none, screenshots 3, writeup long, impact claims True (Reports about 94% R^2 / success rate of its own model on the provided data.)
- **Notes:** Team trained its own scikit-learn model on EOG data instead of calling an LLM; reports R^2 around 94 percent; has alerts tab, manual input form, and SendGrid email alerts.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement
- **Links:** [Devpost](https://devpost.com/software/pipebrains) | [GitHub](https://github.com/lightningbolt7/HackUTD-XI)

### Planet Score  (HackUTD 2024)

- **Prizes:** Best Devpost [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Chrome extension that estimates a product's carbon footprint from its description and price using OpenLCA and Exiobase emission factors.
- **Problem / user:** Shoppers cannot tell which products are truly sustainable and face greenwashing. / eco-conscious online shoppers
- **Domain / idea type:** sustainability_climate + retail_consumer / new_category
- **Platforms / hardware / AI:** browser_extension / False / False
- **Stack:** langs JavaScript; Python; frontend Chrome extension; backend Python; db ; hosting 
- **Tech/APIs:** OpenLCA API (data_source, core); Exiobase (data_source, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 6 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video None, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Uses keyword matching on product text to infer materials, then multiplies kg CO2 per euro by price. Writeup is an explainer with FAQ on life-cycle assessment and notes Ecoinvent licensing cost as a blocker.
- **Team size:** 1 | **Confidence:** high | unverified: has_demo_video; ui_polish; placement_tier (Best Devpost is a non-sponsor prize)
- **Links:** [Devpost](https://devpost.com/software/planet-score) | [GitHub](https://github.com/mxgardner/planet-score)

### poyo.ed  (HackUTD 2024)

- **Prizes:** Poyo's Prize [unknown]  (tier: sponsor_winner)
- **Pitch:** Lecture companion that live-transcribes speech, captures slides via a camera hidden in a Poyo plush keychain, and compiles exportable LLM notes.
- **Problem / user:** Students struggle to capture fast-moving lectures and briefly shown slides, hurting comprehension and retention. / University students
- **Domain / idea type:** education + accessibility / twist_on_known_app
- **Platforms / hardware / AI:** web; hardware / True / speech_or_voice; llm_chat; vision
- **Stack:** langs TypeScript; frontend Next.js; TailwindCSS; Material UI; backend Node.js; db SQLite; Pinata; hosting 
- **Tech/APIs:** SambaNova Cloud API (ai_model, core, sponsor); Pinata File API (database, core, sponsor); Groq API (ai_model, supporting); Clerk (auth, supporting); react-speech-navigation (framework, supporting); Camera in plush toy (hardware_part, core)
- **Sponsor APIs:** SambaNova; Pinata | fit: Poyo's Prize is a mascot-themed award; the project embedded a camera in a Poyo plush and used SambaNova and Pinata APIs.
- **Repo:** public, commits 88 (before/in/after event: 0/79/9), README solid
- **Demo/writeup:** video None, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Team dissected a Poyo plush keychain to embed a camera for slide capture; README, which claims a grand prize, was not checked against Devpost badges (only Poyo's Prize listed).
- **Team size:** 5 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; repo_commits; first_commit; last_commit; commits_in_event_window; readme_quality; ui_polish; team_size; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/poyovision) | [GitHub](https://github.com/david-roh/poyoVision)

### Promising Products  (HackUTD 2024)

- **Prizes:** Frontier [unknown]  (tier: sponsor_winner)
- **Pitch:** Product recommendation app for Frontier internet customers, using a hybrid collaborative-filtering model to suggest suitable products and help with their use.
- **Problem / user:** Customers do not know which telecom or tech product fits their need or how to use it, and documentation alone does not help. / Frontier internet customers and tenants
- **Domain / idea type:** telecom_networking + retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web / False / recommendation; predictive_ml
- **Stack:** langs Python; JavaScript; TypeScript; frontend React; Tailwind CSS; backend Supabase; db Supabase; hosting 
- **Tech/APIs:** Collaborative filtering model (pandas) (ai_model, core); Supabase (database, core); Frontier (sponsor challenge) (other, unclear, sponsor); Pinata (cloud, token, sponsor)
- **Sponsor APIs:** Pinata (mentioned as challenge only) | fit: Recommendation app framed around Frontier internet products and tenant rental experience, with mock or dataset-based recommendations.
- **Repo:** public, commits 73 (before/in/after event: 0/44/29), README thin
- **Demo/writeup:** video True, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Hybrid memory- and model-based collaborative filtering recommender modeled on Amazon-style systems, with a React/TypeScript/Tailwind frontend on Supabase. Writeup contains leftover chatbot filler text in the learned section.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; Pinata_depth; Supabase_use_from_member_bio; stack_backend
- **Links:** [Devpost](https://devpost.com/software/promising-products) | [GitHub](https://github.com/Joshua-Ludolf/Promising-Products)

### Ripple Banking  (HackUTD 2024)

- **Prizes:** General [unknown]  (tier: track_winner)
- **Pitch:** Platform letting small business owners borrow from big banks and act as pop-up micro-banks, with a map to find them and ML background checks.
- **Problem / user:** Unbanked and rural people lack nearby, trusted banking access and fall back on costly alternative financial services. / unbanked/underbanked consumers and small business owners
- **Domain / idea type:** fintech_finance + social_community / social_good
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML/CSS/JS; Google Maps; backend Flask; db CSV files (per repo listing); hosting 
- **Tech/APIs:** Flask (framework, core); Google Maps API (maps_geo, core); ML model (unspecified) (ai_model, unclear)
- **Sponsor APIs:** 
- **Repo:** public, commits 77 (before/in/after event: 0/77/0), README thin
- **Demo/writeup:** video True, live none, screenshots 9, writeup long, impact claims True (Cites 5.6 million unbanked US households and trust in the financial system dropping from 45% to 39% in surveys.)
- **Notes:** Two-sided merchant and customer dashboards with loan application flows; ML model feeds a heat map and background checks; cites US unbanked and public-trust survey figures.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; readme_quality; ML model details
- **Links:** [Devpost](https://devpost.com/software/tbd-z4uir2) | [GitHub](https://github.com/ajay-jayanth/ripple-banking)

### Roomie (unverified on Devpost)  (HackUTD 2024)

- **Prizes:** Winner General and Hardware Track (per ACM UTD site, year unconfirmed) [unknown]  (tier: track_winner)
- **Pitch:** Study-space app that uses class schedules and room occupancy to show which campus rooms are free right now.
- **Problem / user:** Students struggle to find unoccupied rooms to study in. / university students
- **Domain / idea type:** education / twist_on_known_app
- **Platforms / hardware / AI:**  / None / None
- **Stack:** langs ; frontend ; backend ; db ; hosting 
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots None, writeup None, impact claims None
- **Notes:** Described only on the ACM UTD site as a General and Hardware track winner; year not stated there and no Devpost page found, so hardware role unknown.
- **Team size:** 4 | **Confidence:** low | unverified: pitch/problem/target (from one-sentence site description); is_winner; prizes; placement_tier; year of win; team_size; project page not found
- **Links:** [Devpost](None)

### TalkTuahBank  (HackUTD 2024)

- **Prizes:** General [unknown]; Goldman Sachs [unknown]  (tier: track_winner)
- **Pitch:** Voice banking assistant reachable by ordinary phone call, using multi-agent LLMs to check balances, move money and pay bills.
- **Problem / user:** Over a billion adults are unbanked, and many lack internet, digital literacy or branch access. / Unbanked and underserved adults
- **Domain / idea type:** fintech_finance + accessibility / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend Next.js; Tailwind; ShadCN UI; backend FastAPI; db Pinata IPFS; hosting 
- **Tech/APIs:** Retell AI (ai_model, core); OpenAI Swarm (framework, core); Pinata IPFS (database, supporting, sponsor); Aeternity (other, token); Next.js (framework, supporting)
- **Sponsor APIs:** Pinata | fit: Financial-inclusion voice banking aimed at the Goldman Sachs track; the deck was branded with Goldman Sachs.
- **Repo:** public, commits 52 (before/in/after event: 0/40/12), README detailed
- **Demo/writeup:** video None, live not_checked, screenshots 5, writeup long, impact claims True (Cites 1.7 billion unbanked adults worldwide as the motivating market size.)
- **Notes:** Works over plain phone calls via Retell telephony; OpenAI Swarm routes between triage, accounts, payments and applications agents; Pinata/IPFS stores records; deployed site uses a mock backend per README.
- **Team size:** 4 | **Confidence:** medium | unverified: placement_tier; has_demo_video; demo_video_url; live_demo_status; repo_commits; first_commit; last_commit; commits_in_event_window; ui_polish; team_size; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/talktuahbank) | [GitHub](https://github.com/aurelisajuan/hackUTD)

### The Virtual Fitness Assistant  (HackUTD 2024)

- **Prizes:** Next Step; Interview Cake [unknown]  (tier: sponsor_winner)
- **Pitch:** Smart-gym concept using OpenCV and MediaPipe for real-time posture correction, with a mobile app offering workout plans and gamified progress.
- **Problem / user:** Gym-goers lack affordable personal guidance, risk injury from poor form and struggle to stay motivated. / gym-goers and fitness enthusiasts
- **Domain / idea type:** health_wellness / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross; hardware / None / vision; predictive_ml; recommendation
- **Stack:** langs Python; JavaScript; frontend FlutterFlow; HTML5; CSS; backend Python; db ; hosting 
- **Tech/APIs:** MediaPipe (ai_model, core); OpenCV (framework, core); FlutterFlow (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 3 (before/in/after event: 0/1/2), README solid
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims True (States the project won multiple hackathon awards and got recognition from industry experts and investors; no numbers.)
- **Notes:** Project was entered in many hackathons; winner badges for Next Step and Interview Cake sit under Student Hacks on the page, so the HackUTD prize attribution is doubtful. Repo has Python exercise scripts and MP3 guides.
- **Team size:** 3 | **Confidence:** low | unverified: prizes (HackUTD attribution doubtful); placement; first_commit; last_commit; commits_in_event_window; has_hardware (IoT mentioned but not evidenced); platforms; ui_polish
- **Links:** [Devpost](https://devpost.com/software/the-virtual-fitness-assistant-rvt8qg) | [GitHub](https://github.com/Shrunkhal2/Virtual_Fitness_Assistant)

### ToyoTrends  (HackUTD 2024)

- **Prizes:** Toyota [unknown]  (tier: sponsor_winner)
- **Pitch:** Web analytics tool letting Toyota engineers chart and compare fuel efficiency and emissions of Toyota and rival vehicles, with an AI chatbot.
- **Problem / user:** Engineers need an easy way to interpret large fuel-efficiency and emissions datasets against competitors. / Toyota engineers
- **Domain / idea type:** mobility_transport + sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs JavaScript; Python; frontend React; Chart.js; backend ; db ; hosting 
- **Tech/APIs:** SambaNova API (ai_model, supporting, sponsor); CarsXE (data_source, supporting); Chart.js (framework, core); React (framework, core); OpenAI (ai_model, unclear)
- **Sponsor APIs:** SambaNova | fit: Fuel-efficiency and emissions analytics for Toyota engineers using public vehicle datasets.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Devpost page is essentially a README paste; includes animated intro, car and manufacturer comparison over time, CarsXE vehicle images and a SambaNova-powered navigation chatbot.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; ui_polish; team_size; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/toyota-car-analytics-app)

### Vestique  (HackUTD 2024)

- **Prizes:** Samba Nova [unknown]; [MLH] Best Use of Streamlit [unknown]  (tier: sponsor_winner)
- **Pitch:** Wardrobe manager that classifies clothing from photos with vision LLMs, tracks wear patterns, emails reminders about unworn items and helps list them for sale.
- **Problem / user:** People buy lots of clothing but wear little of it, creating waste and fashion landfill. / fashion-conscious consumers wanting to reduce clothing waste
- **Domain / idea type:** sustainability_climate + retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; llm_chat; recommendation; agent_or_tool_use
- **Stack:** langs Python; frontend Streamlit; backend Python; db ; hosting 
- **Tech/APIs:** SambaNova (Llama 3.2 11B Vision, Llama 3.1 70B) (ai_model, core, sponsor); Streamlit (framework, core, sponsor); Brevo (other, supporting); OpenCV (other, supporting)
- **Sponsor APIs:** SambaNova; Streamlit | fit: Streamlit served as the whole UI and SambaNova-hosted Llama models did clothing classification and chat, matching both prizes.
- **Repo:** public, commits 100 (before/in/after event: 0/46/54), README solid
- **Demo/writeup:** video True, live none, screenshots 10, writeup medium, impact claims True (Cites statistics on yearly clothing spend, share of clothes worn and projected fashion emissions growth; sources not shown.)
- **Notes:** Entire UI built in Streamlit; SambaNova-hosted Llama vision and text models drive item recognition plus an agent called SambaFit; Brevo sends unworn-item emails. Repo has about 100 commits.
- **Team size:** 2 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; repo_commits_approx_branch_masternew; sponsor_status_of_SambaNova_Brevo
- **Links:** [Devpost](https://devpost.com/software/vestique) | [GitHub](https://github.com/rChwiecko/Closet.ai)

### What's The Move?  (HackUTD 2024)

- **Prizes:** Most Relatable [unknown]  (tier: track_winner)
- **Pitch:** Finds a fair meeting spot for a friend group by computing an inverse-weighted midpoint of everyone's location and searching nearby places.
- **Problem / user:** Friends scattered across a metro area struggle to pick a meeting place without one person driving far. / Friend groups in the same metro area
- **Domain / idea type:** social_community + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs JavaScript; frontend React; backend Express.js; Firebase Functions; db ; hosting Firebase Hosting
- **Tech/APIs:** Google Maps API (maps_geo, core); Firebase Functions (cloud, core); Pinata (other, token, sponsor); Express.js (framework, supporting); React (framework, core)
- **Sponsor APIs:** Pinata
- **Repo:** public, commits 76 (before/in/after event: 0/63/13), README solid
- **Demo/writeup:** video None, live not_checked, screenshots None, writeup medium, impact claims True (Cites an Eventbrite survey figure that 69% of people find coordinating plans with friends difficult.)
- **Notes:** Custom midpoint API weights each person's travel so drives stay proportional; Google Maps geocoding and Places search; switched from React Native to React mid-hack; cites an Eventbrite survey statistic.
- **Team size:** 5 | **Confidence:** medium | unverified: placement_tier; has_demo_video; demo_video_url; live_demo_status; n_screenshots; repo_commits; first_commit; last_commit; commits_in_event_window; ui_polish; team_size; stack_languages
- **Links:** [Devpost](https://devpost.com/software/what-s-the-move-4z5sih) | [GitHub](https://github.com/farisshaik/hackutd_2024)
