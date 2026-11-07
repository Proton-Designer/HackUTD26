# HackUTD: project cards (72 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackUTD 2024

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
- **Repo:** public, commits 5 (before/in/after event: 0/5/0), README solid
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
- **Repo:** public, commits 19 (before/in/after event: 0/19/0), README solid
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
- **Repo:** public, commits 25 (before/in/after event: 0/23/2), README none
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
- **Repo:** public, commits 8 (before/in/after event: 0/4/4), README solid
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
- **Repo:** public, commits 6 (before/in/after event: 0/5/1), README solid
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


## HackUTD 2025

### Alchemetrics  (HackUTD 2025)

- **Prizes:** Nvidia [unknown]  (tier: sponsor_winner)
- **Pitch:** Dashboard where an NVIDIA Nemotron planner coordinates agents that detect potion drains, match transport tickets, flag discrepancies, forecast overflow and plan routes.
- **Problem / user:** A fictional potion factory had cauldron logs that did not match collections, so missing or misreported potion went unnoticed. / operators of the challenge scenario potion factory
- **Domain / idea type:** ai_agents_infra + productivity_workplace / data_or_analytics
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; predictive_ml
- **Stack:** langs Python; TypeScript; frontend Next.js; Tailwind; backend FastAPI; NumPy; Pandas; OR-Tools; SQLAlchemy; db PostgreSQL; SQLite; hosting 
- **Tech/APIs:** NVIDIA Nemotron (ai_model, core, sponsor); OR-Tools (other, supporting); FastAPI (framework, core); Next.js (framework, supporting); Postgres (database, supporting)
- **Sponsor APIs:** NVIDIA Nemotron | fit: Used Nemotron as the planner that decides which agent or tool runs next and logs its reasoning for the Nvidia challenge.
- **Repo:** public, commits 32 (before/in/after event: 0/18/14), README solid
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims False
- **Notes:** Built around a whimsical sponsor challenge scenario; planner logs visible reasoning traces; routing uses OR-Tools; writeup admits early mock responses before full Nemotron integration.
- **Team size:** 3 | **Confidence:** medium | unverified: first_commit; last_commit; commits_in_event_window; placement; domain_secondary; Nemotron depth (writeup mentions mock responses)
- **Links:** [Devpost](https://devpost.com/software/abc-xapnio) | [GitHub](https://github.com/Lanisha20/JIA.ai)

### AutoBoard  (HackUTD 2025)

- **Prizes:** Goldman Sachs [unknown]  (tier: sponsor_winner)
- **Pitch:** AWS serverless platform that automates financial vendor onboarding with document extraction, a compliance questionnaire, risk scoring and one-click approvals.
- **Problem / user:** Vendor onboarding at large financial firms depends on manual document review that takes weeks. / compliance teams and vendors at financial institutions
- **Domain / idea type:** fintech_finance + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs Python; frontend React; Vite; Tailwind CSS; backend AWS Lambda; API Gateway; db Amazon RDS; hosting AWS
- **Tech/APIs:** AWS Textract (cloud, core); AWS Lambda (cloud, core); API Gateway (cloud, core); Amazon RDS (database, core); Gemini (ai_model, unclear)
- **Sponsor APIs:**  | fit: Targets Goldman Sachs-style vendor onboarding and KY3P compliance workflows described in the writeup.
- **Repo:** public, commits 24 (before/in/after event: 0/24/0), README solid
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims True (Claims compliance timelines drop from weeks to hours; no measured data shown.)
- **Notes:** Fully AWS serverless with seven Python Lambda functions defined as infrastructure as code; includes separate vendor and bank-side views and an audit trail. Devpost text appeared cut off after the backend heading.
- **Team size:** 4 | **Confidence:** medium | unverified: first_commit; last_commit; commits_in_event_window; ui_polish; placement; gemini_depth; writeup_sections_truncated
- **Links:** [Devpost](https://devpost.com/software/404-not-found-us43mg) | [GitHub](https://github.com/Rabib001/HackUTD_2025)

### AutoPM  (HackUTD 2025)

- **Prizes:** Winner PNC Bank [unknown]  (tier: sponsor_winner)
- **Pitch:** Product-management copilot of eight Gemini-driven agents covering ideas, stories, research, RICE scoring, OKRs, wireframes, email and Jira tickets.
- **Problem / user:** PMs juggle ideation, prioritization, stakeholder emails and Jira under time pressure and want repetitive work offloaded. / product managers
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search; generative_media
- **Stack:** langs TypeScript; HTML; frontend Next.js 14; React; Tailwind; backend Next.js API routes; Node.js; LangGraph; LangChain; Zod; db MongoDB; hosting 
- **Tech/APIs:** Google Gemini 2.0 Flash (ai_model, core); LangGraph (framework, core); Jira Cloud (other, core); Tavily (data_source, supporting); Gmail API (other, supporting); Auth0 (auth, supporting, sponsor); MongoDB (database, supporting)
- **Sponsor APIs:** Auth0 | fit: Entered for the PNC Bank track with a PM-workflow tool; the writeup does not mention banking or PNC-specific APIs.
- **Repo:** public, commits 27 (before/in/after event: 0/24/3), README detailed
- **Demo/writeup:** video True, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Writeup stresses that all 8 agents run on Gemini; avoids black-box sentiment scores. Repo README (not Devpost) claims 2nd place in the PNC track.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; Auth0 usage depth
- **Links:** [Devpost](https://devpost.com/software/autopm-2tjzu8) | [GitHub](https://github.com/hrishinave/HackUTD2)

### Beacon  (HackUTD 2025)

- **Prizes:** T-Mobile [unknown]  (tier: sponsor_winner)
- **Pitch:** Real-time customer happiness index for T-Mobile combining live call transcripts, social posts and outage data, with PII scrubbing, agent dashboard and campaign suggestions.
- **Problem / user:** T-Mobile teams lack a live, unified view of customer sentiment across calls, social media and network outages. / telecom call-center agents and PR/marketing teams
- **Domain / idea type:** telecom_networking + productivity_workplace / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs Python; JavaScript; frontend Next.js; TailwindCSS; backend Flask; ngrok; db MongoDB Atlas; hosting 
- **Tech/APIs:** Twilio (telecom, core); LLaMA via Groq API (ai_model, core); Microsoft Presidio (other, core); MongoDB Atlas (database, core, sponsor); Auth0 (auth, supporting, sponsor); ForumScout API (data_source, supporting); Downdetector (data_source, supporting); Next.js (framework, core)
- **Sponsor APIs:** Auth0; MongoDB Atlas | fit: Customer-sentiment platform framed around T-Mobile Un-carrier values, mascot and T-Mobile Tuesday offers, using call, social and outage signals.
- **Repo:** public, commits 19 (before/in/after event: 0/19/0), README none
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Mascot-branded (Telly the dog). Live Twilio call audio goes through a Presidio PII scrubber before LLaMA on Groq classifies sentiment; separate agent and campaign dashboards.
- **Team size:** 4 | **Confidence:** medium | unverified: first_commit; last_commit; commits_in_event_window; ui_polish; placement; MongoDB_sponsor_status
- **Links:** [Devpost](https://devpost.com/software/na-504rkg) | [GitHub](https://github.com/iampritisee/hackutd)

### bevinAI  (HackUTD 2025)

- **Prizes:** Best Use of DigitalOcean Gradient AI by MLH [unknown]  (tier: sponsor_winner)
- **Pitch:** AI project manager that turns an idea into a planned Jira board, links meetings to tickets, validates PRs against requirements and anchors audit hashes on Solana.
- **Problem / user:** Friction between development, project management and business goals slows work in regulated enterprises. / Enterprise project managers and dev teams (framed around PNC)
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; JavaScript; frontend React; backend Django; FastAPI; Node.js/Express; db MySQL; hosting AWS Amplify
- **Tech/APIs:** Nvidia NIM Nemotron-70B (ai_model, core, sponsor); MCP (framework, core); Jira API (other, core); GitHub API (other, supporting); Slack (other, supporting); Confluence (other, supporting); Solana (other, supporting); AWS Amplify (cloud, supporting); DigitalOcean Gradient AI (ai_model, unclear, sponsor)
- **Sponsor APIs:** Nvidia NIM | fit: Writeup names no DigitalOcean Gradient AI usage; it centers on Nvidia NIM/Nemotron and PNC framing, so the MLH prize fit is unclear.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 2, writeup long, impact claims True (Claims a one-sentence idea becomes a planned Jira project in under 10 minutes and could cut time-to-market by weeks.)
- **Notes:** Chained Nemotron-70B prompts produce structured Jira JSON; PR validator compares diffs with acceptance criteria; optional Solana ledger hashes workflow events; MCP server handles async tasks.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; sponsor_fit_note; n_screenshots; ui_polish; team_size
- **Links:** [Devpost](https://devpost.com/software/bevinai)

### Cura  (HackUTD 2025)

- **Prizes:** CBRE [unknown]  (tier: sponsor_winner)
- **Pitch:** Commercial real estate intelligence platform with agent-driven navigation, forecasting, property comparison, pros/cons analysis and market sentiment.
- **Problem / user:** Most people lack knowledge and access to commercial real estate because few agents work in that segment. / Commercial real estate investors and first-time buyers
- **Domain / idea type:** housing_real_estate + fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; rag_or_search; predictive_ml
- **Stack:** langs Python; TypeScript; frontend Next.js; backend FastAPI; CrewAI; db MongoDB; hosting 
- **Tech/APIs:** CrewAI (framework, core); Nvidia Nemo models (ai_model, unclear, sponsor); Ollama (ai_model, supporting); MongoDB MCP (database, supporting); FastAPI (framework, core); Next.js (framework, core)
- **Sponsor APIs:**  | fit: Commercial real estate analytics platform aimed at the CBRE challenge.
- **Repo:** public, commits 78 (before/in/after event: 0/73/5), README solid
- **Demo/writeup:** video None, live none, screenshots 2, writeup medium, impact claims True (Cites a figure that only 21% of US real estate agents work with commercial properties.)
- **Notes:** Reasoning agents adapt the dashboard layout to context; relies on web scraping; README says Llama 3.1 via Ollama/vLLM with Gemini fallback and MongoDB Atlas.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; repo_commits; first_commit; last_commit; commits_in_event_window; ui_polish; team_size; stack_hosting; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/tbd-58ftpr) | [GitHub](https://github.com/armaanamatya/HackUTD2025)

### DataDriver  (HackUTD 2025)

- **Prizes:** Winner Northmark Compute & Cloud [unknown]; Winner Nvidia [unknown]  (tier: sponsor_winner)
- **Pitch:** Agentic copilot for data center technicians that builds maintenance workflows, checks inventory and re-plans when problems appear.
- **Problem / user:** Data center maintenance still relies on clipboards and hunting through old docs when something unexpected happens. / data center technicians
- **Domain / idea type:** ai_agents_infra + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; JavaScript; frontend React; Vite; TailwindCSS; backend Flask; db MongoDB; hosting 
- **Tech/APIs:** NVIDIA Nemotron nano 9b v2 (ai_model, core, sponsor); NeMo toolkit (framework, supporting, sponsor); LangChain (framework, core); MongoDB (database, core); Flask (framework, core)
- **Sponsor APIs:** NVIDIA Nemotron; NeMo | fit: Core agent runs on an Nvidia Nemotron model; the Northmark prize fit is not explained in the writeup.
- **Repo:** public, commits 74 (before/in/after event: 0/73/1), README detailed
- **Demo/writeup:** video None, live none, screenshots 2, writeup long, impact claims False
- **Notes:** ReAct-style agent on nemotron-nano-9b-v2 with LangChain; team had never built agents before. Repo continued receiving commits into January 2026.
- **Team size:** 4 | **Confidence:** high | unverified: has_demo_video; ui_polish; sponsor_fit_note (Northmark)
- **Links:** [Devpost](https://devpost.com/software/datadriver) | [GitHub](https://github.com/Jeanpascal-Gauthier/hackutd25)

### DCDaddy  (HackUTD 2025)

- **Prizes:** Northmark Compute & Cloud [unknown]  (tier: sponsor_winner)
- **Pitch:** Operations command center for data-center technicians covering AI ticket parsing from email and Slack, health-aware routing on floor plans, predictive inventory and a device assistant.
- **Problem / user:** Data-center technicians use fragmented tools and manual processes, causing human error and inefficiency in large compute facilities. / data center technicians and admins
- **Domain / idea type:** productivity_workplace + safety_security / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; predictive_ml
- **Stack:** langs TypeScript; JavaScript; frontend Next.js; React; Tailwind CSS; backend Next.js API routes; db MongoDB Atlas; hosting AWS
- **Tech/APIs:** Gemini 2.0 Flash (ai_model, core); MongoDB Atlas (database, core, sponsor); Gmail API (other, supporting); Slack ingestion (other, supporting); AWS (cloud, unclear); Next.js (framework, core)
- **Sponsor APIs:** MongoDB Atlas | fit: Addresses the Northmark data-center operations challenge areas: work orders, communications, routing, inventory and error prevention.
- **Repo:** public, commits 17 (before/in/after event: 0/17/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims True (Cites a $2.8B, 400MW facility scale and claims of cost savings and uptime gains without measurements.)
- **Notes:** Combines a five-constraint routing algorithm that factors technician health conditions, floor elevation and hot/cold zones with a 3D rack viewer and deterministic inventory depletion formulas. Repo description self-labels 3rd place (unverified).
- **Team size:** 4 | **Confidence:** medium | unverified: first_commit; last_commit; commits_in_event_window; ui_polish; placement; AWS_depth
- **Links:** [Devpost](https://devpost.com/software/fun-dashboard) | [GitHub](https://github.com/anishalle/hackutd2025)

### Enchantress  (HackUTD 2025)

- **Prizes:** EOG Resources [unknown]  (tier: sponsor_winner)
- **Pitch:** Gamified potion-cauldron dashboard with a map, time-series graphs and detection of transport-ticket mismatches, plus overflow forecasting and pickup scheduling.
- **Problem / user:** Transport tickets only give daily totals, making it hard to match them to real drain events and spot unlogged or misreported volumes. / operators monitoring fluid or supply-chain flows (framed as a potion factory)
- **Domain / idea type:** other + productivity_workplace / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; JavaScript; HTML; CSS; frontend React; Vite; backend TypeScript; db ; hosting 
- **Tech/APIs:** React (framework, core); Vite (framework, supporting)
- **Sponsor APIs:**  | fit: Matched the EOG Resources challenge (tracking potion flow and discrepancies) with a visual dashboard and discrepancy algorithm, framed as oil-tracking analogy.
- **Repo:** public, commits 62 (before/in/after event: 0/62/0), README none
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Fantasy reskin of an oil-tracking style problem; 12 animated cauldrons and a week of minute-level data; no AI used, forecasting and ML listed only as future work.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; domain_primary; readme_quality (default Vite template, treated as none)
- **Links:** [Devpost](https://devpost.com/software/enchantress-w2li90) | [GitHub](https://github.com/LegendaryPenguin/Enchantress/tree/master)

### HarmoniQ  (HackUTD 2025)

- **Prizes:** Winner T-Mobile [3rd]; Winner Best Use of Auth0 [unknown]  (tier: track_winner)
- **Pitch:** AI dashboard for telecom teams that pairs network performance data with social sentiment to predict outages and suggest actions.
- **Problem / user:** Network performance data and customer sentiment are analysed separately, so telecom teams spot service problems and frustration late. / Telecom product managers and network engineers
- **Domain / idea type:** telecom_networking + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; Vite; TailwindCSS; backend FastAPI; Flask; db ; hosting 
- **Tech/APIs:** Gemini API (ai_model, core); scikit-learn (framework, core); Auth0 (auth, supporting, sponsor); Kaggle datasets (data_source, core); Reddit and X APIs (data_source, supporting); React (framework, core)
- **Sponsor APIs:** Auth0 | fit: Telecom-focused sentiment and outage dashboard for the T-Mobile track; Auth0 used for login per the writeup.
- **Repo:** public, commits 12 (before/in/after event: 0/11/1), README thin
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Blends Kaggle network data (plus simulated outages) with Reddit/X sentiment into a Customer Happiness Index; outage models trained offline with random forest and gradient boosting.
- **Team size:** 4 | **Confidence:** medium | unverified: demo_video_url; repo_commits; first_commit; last_commit; commits_in_event_window; readme_quality; ui_polish; stack_database; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/x-yiqm81) | [GitHub](https://github.com/Siriapps/HarmoniQ)

### HealthSense  (HackUTD 2025)

- **Prizes:** Best Use of Vultr [unknown]  (tier: sponsor_winner)
- **Pitch:** Wearable sensor kit where an Arduino and Raspberry Pi stream data to Redis on Vultr and a Nemotron agent alerts the wearer via vibration.
- **Problem / user:** Detecting concerning health or safety readings for workers from live sensor data and alerting them. / workers wearing sensors
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / agent_or_tool_use; predictive_ml
- **Stack:** langs C++; Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend Python; db Redis; hosting Vultr
- **Tech/APIs:** Vultr (cloud, core, sponsor); NVIDIA Nemotron (ai_model, core, sponsor); Redis (database, core); Arduino Uno (hardware_part, core); Raspberry Pi 5 (hardware_part, core)
- **Sponsor APIs:** Vultr; NVIDIA Nemotron | fit: Vultr hosts both the Redis database and the Nemotron agent that decides when to alert.
- **Repo:** public, commits 79 (before/in/after event: 0/77/2), README solid
- **Demo/writeup:** video None, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Accelerometer, heart rate and temperature sensors on Arduino Uno feeding a Pi 5; button silences vibration alert; mentions anomaly detection with encoder-decoder. Repo includes compiled objects and model weights.
- **Team size:** 4 | **Confidence:** high | unverified: has_demo_video; ui_polish; stack_backend
- **Links:** [Devpost](https://devpost.com/software/healthsense-0qxrs4) | [GitHub](https://github.com/delster1/utdproj)

### Hingine  (HackUTD 2025)

- **Prizes:** Toyota Financial Services [unknown]  (tier: sponsor_winner)
- **Pitch:** Swipe-based car discovery app for students that connects to Toyota Financial data and unlocks APR rewards through short finance lessons.
- **Problem / user:** Young adults with thin credit find car leasing and financing confusing and intimidating. / college students and young first-time car buyers
- **Domain / idea type:** fintech_finance + education / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross; mobile_ios; mobile_android / False / False
- **Stack:** langs TypeScript; frontend React Native; Expo; React Navigation; backend ; db ; hosting 
- **Tech/APIs:** Toyota Financial Services data (data_source, core, sponsor); Expo (framework, core); React Native (framework, core)
- **Sponsor APIs:** Toyota Financial Services | fit: Uses Toyota Financial Services car and finance data behind a swipe interface with lesson-based APR incentives.
- **Repo:** public, commits 3 (before/in/after event: 0/3/0), README thin
- **Demo/writeup:** video None, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Mixes dating-app swipe UX with Duolingo-style lessons; completed lessons unlock simulated incentives such as APR reductions. Repo has only three commits.
- **Team size:** 3 | **Confidence:** high | unverified: has_demo_video; ui_polish; ai_used (not mentioned, assumed none)
- **Links:** [Devpost](https://devpost.com/software/hingine) | [GitHub](https://github.com/Pancakemix31/Hingine)

### hyperlynx  (HackUTD 2025)

- **Prizes:** Best Domain Name from GoDaddy Registry [unknown]  (tier: sponsor_winner)
- **Pitch:** Ticketing layer on top of a custom Jira-like system that gives data-center technicians context and helps managers track work orders.
- **Problem / user:** Ticket-to-response workflows in data centers are slow and tedious, hurting technicians, managers and compliance. / data center technicians and managers
- **Domain / idea type:** productivity_workplace + telecom_networking / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend React; Bootstrap; backend Django; db ; hosting Vultr
- **Tech/APIs:** Django (framework, core); Vultr (cloud, supporting, sponsor); Auth0 (auth, supporting, sponsor); GoDaddy domain (hyperlynx.us) (other, supporting, sponsor); Gemini (ai_model, unclear); Jira API (other, unclear)
- **Sponsor APIs:** Vultr; Auth0; GoDaddy Registry | fit: Registered the project domain hyperlynx.us through the GoDaddy Registry offer and listed it as the live site.
- **Repo:** public, commits 6 (before/in/after event: 0/6/0), README none
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup medium, impact claims True (Cites a $500M cost to AWS from a recent data-center gap and an underserved emergency-dispatch market, unsourced.)
- **Notes:** Built its own Jira-like ticket simulator to mimic data center work orders; claims adjacent market in emergency dispatch; includes custom branding with hand-drawn font; slide deck linked.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; live_demo_status (site fetch blocked); ai_types; ai_used (Gemini listed in Built With only); is_sponsor flags
- **Links:** [Devpost](https://devpost.com/software/hyperlynx) | [GitHub](http://github.com/zekestephens/hyperlynx)

### InsighT  (HackUTD 2025)

- **Prizes:** Winner T-Mobile [unknown]  (tier: sponsor_winner)
- **Pitch:** Dashboard for T-Mobile product managers that aggregates customer complaints and outage signals, maps hotspots, and uses Gemini to suggest prioritized opportunities.
- **Problem / user:** Customer feedback is scattered across social media, outage trackers and forums, so PMs cannot see where customers are hurting. / telecom product managers
- **Domain / idea type:** telecom_networking + productivity_workplace / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind; Radix UI; Recharts; Leaflet; backend Node.js; Next.js API routes; Cheerio; db Supabase Postgres; hosting Vercel
- **Tech/APIs:** Google Gemini 2.0 Flash (ai_model, core); Supabase (database, core); Reddit API (data_source, core); DownDetector / outage trackers (scraped) (data_source, core); Leaflet + OpenStreetMap + Nominatim (maps_geo, core); Vercel (cloud, supporting)
- **Sponsor APIs:**  | fit: Built as a customer-intelligence dashboard aimed at T-Mobile product managers, covering network, app, billing and home internet areas.
- **Repo:** public, commits 34 (before/in/after event: 0/34/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 16, writeup long, impact claims False
- **Notes:** Scrapes Reddit, DownDetector-style outage sites and news into a Customer Happiness Index, with a Leaflet heatmap and live outage overlays built on free mapping services.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement
- **Links:** [Devpost](https://devpost.com/software/t-insights) | [GitHub](https://github.com/AbdullahMoghal/t-insight-hack2025)

### Kachow  (HackUTD 2025)

- **Prizes:** Toyota Financial Services [unknown]  (tier: sponsor_winner)
- **Pitch:** Car-buying assistant with a chatbot that pulls pricing, insurance, gas, maintenance and APR information and uses mock bank data to guide financing decisions.
- **Problem / user:** Buying a car requires dozens of hours researching prices, costs and financing, leading to buyer regret. / car buyers
- **Domain / idea type:** fintech_finance + retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs JavaScript; Python; frontend React; backend Node.js; db MongoDB; hosting 
- **Tech/APIs:** Nemotron (ai_model, core); OpenAI-based agent (ai_model, core); MongoDB (database, supporting, sponsor); React (framework, core); Node.js (framework, core)
- **Sponsor APIs:**  | fit: Car-purchase and financing (APR) advisor aligned with an auto-finance sponsor; uses mock bank data rather than real account integration.
- **Repo:** public, commits 6 (before/in/after event: 0/5/1), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 5, writeup long, impact claims True (Cites a statistic that 46% of Americans have car buyer remorse; no source shown.)
- **Notes:** Chatbot named KaBot is an OpenAI-based agent on a Node backend; bank connection is mock data. Writeup is humorous and skips middleware details. Claims no AI hallucinations without evidence.
- **Team size:** 4 | **Confidence:** medium | unverified: first_commit; last_commit; commits_in_event_window; ui_polish; placement; Nemotron_is_sponsor
- **Links:** [Devpost](https://devpost.com/software/car-thing-1dsxyk) | [GitHub](https://github.com/adamFabsa/Kachow)

### Kori  (HackUTD 2025)

- **Prizes:** Best Use of Gemini API by MLH [unknown]  (tier: sponsor_winner)
- **Pitch:** Raspberry Pi touchscreen desk companion cat that senses room conditions and mood, rewards focus time, and syncs with a mobile app with Gemini insights.
- **Problem / user:** Long study or work sessions feel isolating, and people want gentle support without productivity tracking pressure. / students and remote workers who study or work long hours
- **Domain / idea type:** mental_health + productivity_workplace / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_cross; desktop / True / vision; llm_chat
- **Stack:** langs JavaScript; TypeScript; frontend Electron; React Native; Expo; backend Express; db ; hosting 
- **Tech/APIs:** Google Gemini API (ai_model, supporting, sponsor); Raspberry Pi 5 (hardware_part, core); BME280 sensor (hardware_part, core); Camera mood recognition (other, supporting); Electron (framework, core); React Native (framework, core)
- **Sponsor APIs:** Google Gemini API | fit: Gemini processes session and environment data in the mobile app to generate insights for the user.
- **Repo:** public, commits 28 (before/in/after event: 0/27/1), README solid
- **Demo/writeup:** video None, live not_checked, screenshots 4, writeup long, impact claims False
- **Notes:** Custom 3D-printed case, BME280 plus air-quality sensors, mic loudness and camera mood cues; hourly non-judgmental check-in. Electron UI, Express on the Pi, React Native app. Has a live site.
- **Team size:** 5 | **Confidence:** high | unverified: has_demo_video; ui_polish; live_demo_status; stack_languages (from Built With list)
- **Links:** [Devpost](https://devpost.com/software/kori) | [GitHub](https://github.com/DuckyDaBucky/HackUTD2025)

### MirrorAPI  (HackUTD 2025)

- **Prizes:** StateFarm [unknown]  (tier: sponsor_winner)
- **Pitch:** Web tool that sends the same request to two API versions, diffs the JSON, and uses an NVIDIA Nemotron RAG agent to write a change report.
- **Problem / user:** Developers struggle to track and document API changes between versions and assess migration impact. / developers and employees maintaining API-dependent codebases
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; agent_or_tool_use
- **Stack:** langs TypeScript; Python; frontend Next.js 14; React; Tailwind; shadcn/ui; backend FastAPI; db ; hosting 
- **Tech/APIs:** NVIDIA Nemotron (ai_model, core, sponsor); FastAPI (framework, supporting); OAuth (employee sign-in) (auth, supporting); Next.js (framework, core)
- **Sponsor APIs:** NVIDIA Nemotron | fit: Built for the State Farm API-versioning challenge and also used NVIDIA Nemotron for the RAG-generated change reports.
- **Repo:** public, commits 39 (before/in/after event: 0/35/4), README solid
- **Demo/writeup:** video True, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Client-side JSON diffing feeds a FastAPI backend calling Nemotron; README additionally mentions a 0-100 migration risk score and Markdown export. Writeup says team gathered feedback from sponsor reps.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement
- **Links:** [Devpost](https://devpost.com/software/mirror-api) | [GitHub](https://github.com/ParsaBazrpash/MirrorAPI)

### NLB (Nothing Left Behind)  (HackUTD 2025)

- **Prizes:** Winner General Track [unknown]  (tier: track_winner)
- **Pitch:** iOS app that reminds group members of shared shopping-list items when near a relevant store and splits receipts via AI scanning.
- **Problem / user:** People forget small errands and waste time manually splitting grocery bills among roommates or family. / roommates and families sharing groceries
- **Domain / idea type:** retail_consumer + fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / False / vision; llm_chat
- **Stack:** langs Swift; frontend SwiftUI; backend Firebase; db Firestore; hosting 
- **Tech/APIs:** Google Gemini API (ai_model, core, sponsor); Apple Vision (OCR) (framework, core); CoreLocation (maps_geo, core); Firebase Auth (auth, supporting); Firestore (database, core)
- **Sponsor APIs:** Google Gemini API
- **Repo:** public, commits 2 (before/in/after event: 0/2/0), README none
- **Demo/writeup:** video False, live none, screenshots 11, writeup medium, impact claims False
- **Notes:** Combines geofenced reminders with OCR plus Gemini receipt parsing; Gemini was added after Vision OCR alone could not produce clean item lists. Repo is a single Xcode project.
- **Team size:** 2 | **Confidence:** high | unverified: has_demo_video; ui_polish
- **Links:** [Devpost](https://devpost.com/software/tbd-app) | [GitHub](https://github.com/yeshasn/hackutd-nlb)

### Pact  (HackUTD 2025)

- **Prizes:** Winner CBRE [unknown]; Winner Best Use of Solana [unknown]  (tier: sponsor_winner)
- **Pitch:** Contract management platform with AI-assisted drafting, multi-party approvals, escrowed milestone payments and Solana-anchored document hashes.
- **Problem / user:** Slow, opaque partnership agreements leave clients unsure what they pay for and delay projects. / businesses and their clients/vendors negotiating contracts
- **Domain / idea type:** civic_legal + fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs Rust; TypeScript; frontend Next.js; React; backend Node.js; Anchor; db IPFS; hosting 
- **Tech/APIs:** Solana (other, core, sponsor); Anchor (framework, core); Google Gemini API (ai_model, supporting, sponsor); IPFS (database, supporting)
- **Sponsor APIs:** Solana; Google Gemini API | fit: Contract hashes, deal state, reputation and escrow are implemented as Solana programs; CBRE fit is not stated beyond B2B deal management.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Three Solana programs in Rust/Anchor (deals, reputation, escrow); IPFS for documents; Gemini extracts requirements and scores fraud risk. Writeup lists several phases as future work.
- **Team size:** 3 | **Confidence:** medium | unverified: has_demo_video; ui_polish; repo (linked but clone failed, private or deleted); sponsor_fit_note; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/autotract) | [GitHub](https://github.com/lakshkumar06/pact)

### PoyoLabs  (HackUTD 2025)

- **Prizes:** EOG Resources [unknown]  (tier: sponsor_winner)
- **Pitch:** Pixel-art gamified dashboard that shows data points as potion cauldrons, with a Nemotron-powered chatbot, network map and route optimization.
- **Problem / user:** Wanted to make data and network analysis visually engaging rather than plain charts. / analysts monitoring network or asset data
- **Domain / idea type:** telecom_networking + entertainment_games / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend Flask; db ; hosting GoDaddy
- **Tech/APIs:** NVIDIA Nemotron (ai_model, supporting, sponsor); Auth0 (auth, unclear, sponsor); Flask (framework, core); GoDaddy (other, supporting, sponsor)
- **Sponsor APIs:** NVIDIA Nemotron; Auth0; GoDaddy | fit: Dashboard tracks cauldron data points with an AI chatbot; the EOG-specific challenge link is not explained in the writeup.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 5, writeup long, impact claims False
- **Notes:** Hand-made pixel art and animations on a Flask backend; deployed to a custom domain. Includes historical playback and optimal route map.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ui_polish; live_demo_status (site unreachable from sandbox proxy); sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/poyolabs-47n0fz)

### PoyoPop  (HackUTD 2025)

- **Prizes:** Best Startup [unknown]  (tier: track_winner)
- **Pitch:** Mobile-style app that maps nearby food and drink pop-ups for consumers and lets vendors post events and track visit counts instead of ratings.
- **Problem / user:** Small pop-up food vendors without a social following struggle to reach customers, and food fans struggle to find pop-ups. / food lovers and small pop-up vendors
- **Domain / idea type:** food_nutrition + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web; mobile_cross / False / False
- **Stack:** langs JavaScript; frontend Figma; Vite; backend ; db ; hosting 
- **Tech/APIs:** Figma / Figma Make (other, core); Interactive map API (unspecified) (maps_geo, unclear)
- **Sponsor APIs:** 
- **Repo:** public, commits 4 (before/in/after event: 0/4/0), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 11, writeup long, impact claims False
- **Notes:** Mostly a Figma prototype (Figma Make export) with a Vite code bundle; team included first-time hackers from non-CS majors. Chose visit counts over ratings by design. Business/go-to-market plan featured in writeup.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; platforms; ai_used
- **Links:** [Devpost](https://devpost.com/software/poyopop) | [GitHub](https://github.com/reina8zhou-blip/HackUTD-2025---PoyoPop.git)

### ProdigyPM  (HackUTD 2025)

- **Prizes:** Winner General Track [unknown]  (tier: track_winner)
- **Pitch:** AI console that turns a product PDF or chat-built PRD into department subprojects with estimates and pushes them to Jira with a live dashboard.
- **Problem / user:** Product managers manually break product documents into tasks, estimates and Jira tickets, which takes hours. / product managers
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; TypeScript; JavaScript; frontend Next.js; React; Tailwind; backend FastAPI; pydantic; uvicorn; pdfplumber; db ; hosting S3 (optional)
- **Tech/APIs:** OpenAI GPT-4 Turbo (ai_model, core); Jira Cloud API (other, core); FastAPI (framework, core); Next.js (framework, core); pdfplumber (other, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Three named GPT-4 Turbo agents (PDF, decomposition, PRD consultant); dashboard polls Jira every 2 seconds; storage can be local or S3.
- **Team size:** 2 | **Confidence:** medium | unverified: ui_polish; team_size; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/prodigypm-kaqe09)

### ProdPlex  (HackUTD 2025)

- **Prizes:** Winner PNC Bank [unknown]  (tier: sponsor_winner)
- **Pitch:** Multi-agent product-management copilot where several Nemotron models handle research, strategy, design and PRD generation.
- **Problem / user:** Product managers lose time on documentation, research and coordination instead of strategy. / product managers
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs JavaScript; Python; TypeScript; frontend React; backend FastAPI; db ; hosting 
- **Tech/APIs:** NVIDIA Nemotron (ai_model, core, sponsor); React (framework, core); Figma (other, supporting); LangGraph (framework, supporting)
- **Sponsor APIs:** NVIDIA Nemotron | fit: Built directly on the PNC challenge about reimagining the product manager role with GenAI, using Nemotron models for each agent.
- **Repo:** public, commits 10 (before/in/after event: 0/10/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Claims no central orchestrator among agents; RAG added to a Nemotron model; Figma used for design output. Repo README lists seven agents and many status markdown files. Repo named ProdigyPM in README.
- **Team size:** 4 | **Confidence:** high | unverified: has_demo_video; ui_polish; stack_backend (from repo README, not writeup)
- **Links:** [Devpost](https://devpost.com/software/prodify-94vbpk) | [GitHub](https://github.com/Ka2507/hackutd2025)

### ProDuh!  (HackUTD 2025)

- **Prizes:** Winner PNC Bank [unknown]  (tier: sponsor_winner)
- **Pitch:** Multi-agent LLM command center that links product-management tools and turns strategy and KPIs into Jira/ADO-ready stories.
- **Problem / user:** PMs waste time on copy-paste glue across Jira, Confluence and chats, and strategy rarely flows into backlog stories. / Product managers
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; frontend React; backend Node/Express; db PostgreSQL; hosting Google Cloud
- **Tech/APIs:** Gemini (ai_model, core); Google ADK (framework, core); OpenAI (ai_model, unclear); Jira/ADO/Confluence adapters (other, core); PostgreSQL (database, supporting)
- **Sponsor APIs:**  | fit: PNC track fit appears to be a workplace productivity tool; no PNC-specific API is named on the page.
- **Repo:** public, commits 24 (before/in/after event: 0/24/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 9, writeup medium, impact claims False
- **Notes:** Adapter layer gives Jira and Azure DevOps parity; agent loops capped at three to limit drift; demo uses mock analytics CSV rather than live data.
- **Team size:** 2 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; repo_commits; first_commit; last_commit; commits_in_event_window; ui_polish; team_size; sponsor_fit_note; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/produh) | [GitHub](https://github.com/christinaduthie/produh)

### ProDuh! - The "duh" way to ship smarter  (HackUTD 2025)

- **Prizes:** PNC Bank [unknown]  (tier: sponsor_winner)
- **Pitch:** Multi-agent AI command center covering the product lifecycle, turning goals into Jira or Azure DevOps ready stories and keeping docs linked.
- **Problem / user:** Product managers waste hours copying between Jira, Confluence and chats, and strategy drifts from sprint work. / product managers
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; frontend React; backend Node.js; Express; db PostgreSQL; hosting Google Cloud
- **Tech/APIs:** Google Gemini (ai_model, core, sponsor); Google ADK (framework, supporting); OpenAI (ai_model, unclear); Jira (other, core); Confluence (other, supporting); PostgreSQL (database, supporting); Google Cloud (cloud, unclear)
- **Sponsor APIs:** Google Gemini | fit: Targets the PNC product-manager lifecycle challenge with an LLM agent layer over Jira/ADO and Confluence.
- **Repo:** public, commits 24 (before/in/after event: 0/24/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 9, writeup long, impact claims False
- **Notes:** App-agnostic adapter layer for Jira and Azure DevOps plus Confluence, Graph, ServiceNow and GitHub drivers; agent loops capped at three; mock analytics CSV stands in for real data. Pitched as a 2-minute demo.
- **Team size:** 2 | **Confidence:** high | unverified: has_demo_video; ui_polish; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/produh) | [GitHub](https://github.com/christinaduthie/produh)

### qAPIbara  (HackUTD 2025)

- **Prizes:** StateFarm [unknown]  (tier: sponsor_winner)
- **Pitch:** AI-assisted API regression tool that diffs two API versions, auto-generates tests and explains breaking changes with visual health dashboards.
- **Problem / user:** Debugging breaking changes between API versions is slow and manual for QA and backend teams. / QA engineers and DevOps/backend teams
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; JavaScript; frontend React; Framer Motion; backend FastAPI; db Firestore; hosting Vultr
- **Tech/APIs:** NVIDIA Nemotron (ai_model, core, sponsor); Google Gemini API (ai_model, core, sponsor); Auth0 (auth, supporting, sponsor); Vultr (cloud, supporting, sponsor); Firestore (database, supporting); FastAPI (framework, core)
- **Sponsor APIs:** NVIDIA Nemotron; Google Gemini API; Auth0; Vultr | fit: Applies API version regression testing to the State Farm challenge area, using LLMs to generate tests and explain failures.
- **Repo:** public, commits 24 (before/in/after event: 0/23/1), README detailed
- **Demo/writeup:** video None, live none, screenshots 4, writeup long, impact claims True (States target user counts (tens of thousands of engineers) and up to 80 percent faster diagnosis, no sourcing.)
- **Notes:** Uses Nemotron to plan test workflows and Gemini to explain regressions; includes regression heatmap and service health score. Repo had 23 commits during the event and one in December 2025.
- **Team size:** 1 | **Confidence:** high | unverified: has_demo_video; ui_polish; sponsor_fit_note (State Farm challenge text not seen)
- **Links:** [Devpost](https://devpost.com/software/in-progress-2awbie) | [GitHub](https://github.com/nathanhanxp/qAPIbara)

### Relay  (HackUTD 2025)

- **Prizes:** Best Use of ElevenLabs by MLH [unknown]  (tier: sponsor_winner)
- **Pitch:** Agentic assistant for data center technicians that plans and runs SSH-based verification checks, with a Jira chat companion and an AR camera overlay.
- **Problem / user:** Data center technicians need help running checks and working through maintenance tasks; Devpost writeup itself is missing so the exact stated problem is unknown. / data center technicians
- **Domain / idea type:** ai_agents_infra + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web; other / None / agent_or_tool_use; llm_chat; vision
- **Stack:** langs Python; frontend ; backend Flask; SQLAlchemy; LangGraph; LangChain; asyncssh; db PostgreSQL (Neon); hosting 
- **Tech/APIs:** LangGraph deepagents (framework, core); asyncssh verifier (other, core); PostgreSQL / Neon (database, core); Anthropic Claude (Jira agent) (ai_model, supporting); NVIDIA hosted Llama (ai_model, supporting); Atlassian Jira (other, supporting); Tavily (data_source, token); OpenCV + AprilTags (other, supporting); ElevenLabs (ai_model, unclear, sponsor)
- **Sponsor APIs:** ElevenLabs (claimed by prize only; not seen in README) | fit: Prize is MLH Best Use of ElevenLabs, but README names no voice or ElevenLabs usage; usage not verified.
- **Repo:** public, commits 6 (before/in/after event: 0/5/1), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup short, impact claims False
- **Notes:** Devpost description failed to save; the page only has updates pointing to the README. Repo has LangGraph deep agent, SSH verifier, Jira agent and an OpenCV AprilTag AR overlay (data feed not wired).
- **Team size:** None | **Confidence:** low | unverified: team_size; ElevenLabs_use; n_screenshots; ui_polish; first_commit; last_commit; commits_in_event_window; placement; platforms; has_hardware; writeup_sections; writeup_length
- **Links:** [Devpost](https://devpost.com/software/tbd-v8pqbk) | [GitHub](https://github.com/Squidtoon99/hackutd-legend)

### SpendingWithSpendy  (HackUTD 2025)

- **Prizes:** Capital One [unknown]; Best Design [unknown]  (tier: sponsor_winner)
- **Pitch:** Kid-oriented banking app where an NFC Spendy card authorises in-game currency purchases and parents review spending and reload funds.
- **Problem / user:** Digital payments make money intangible, so children struggle to visualise spending and manage their own money. / Children and their parents
- **Domain / idea type:** fintech_finance + education / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / True / False
- **Stack:** langs TypeScript; frontend React Native; Expo; Tailwind; backend ; db ; hosting 
- **Tech/APIs:** Expo (framework, core); React (framework, core); NFC card (hardware_part, core); Tailwind (framework, supporting)
- **Sponsor APIs:**  | fit: Financial-literacy app for kids targeting the Capital One track; no Capital One API named.
- **Repo:** public, commits 36 (before/in/after event: 0/35/1), README solid
- **Demo/writeup:** video None, live none, screenshots 6, writeup short, impact claims False
- **Notes:** Mascot-driven UI shows each dollar as a Spendy character; NFC card tap confirms purchases of Robux or Valorant Points; Figma link listed alongside the repo.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; repo_commits; first_commit; last_commit; commits_in_event_window; readme_quality; ui_polish; stack_languages
- **Links:** [Devpost](https://devpost.com/software/spendingwithspendy) | [GitHub](https://github.com/brendanshen24/SpendWithSpendy)

### Stamped  (HackUTD 2025)

- **Prizes:** Goldman Sachs [unknown]  (tier: sponsor_winner)
- **Pitch:** Onboarding platform for banks that manages clients from lead prospecting through full onboarding with role-based dashboards.
- **Problem / user:** Financial institutions lose efficiency to manual client onboarding processes. / Bank staff, clients and vendors
- **Domain / idea type:** fintech_finance + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; frontend Next.js 14; React; backend ; db Supabase; hosting Netlify
- **Tech/APIs:** Supabase (database, core); Supabase Auth (auth, core); Next.js (framework, core)
- **Sponsor APIs:**  | fit: Banking onboarding workflow tool fitted to the Goldman Sachs track; no Goldman API named.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 7, writeup short, impact claims False
- **Notes:** Multi-role system (clients, vendors, employees) with sales pipeline, client list and risk assessment screens; no AI mentioned in the writeup.
- **Team size:** 2 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; live_demo_status; ui_polish; team_size; stack_hosting; ai_used
- **Links:** [Devpost](https://devpost.com/software/stamped-6hnl4w)

### TaskFlow  (HackUTD 2025)

- **Prizes:** Northmark Compute & Cloud [unknown]  (tier: sponsor_winner)
- **Pitch:** Datacenter technician coordination: mobile web app with tickets, checklists, chat and path planning, an engineer dashboard, and an iOS AR pointer app.
- **Problem / user:** Datacenter tickets suffer delays and poor visibility into where technicians are and how work is progressing. / datacenter technicians and engineers
- **Domain / idea type:** productivity_workplace + telecom_networking / twist_on_known_app
- **Platforms / hardware / AI:** web; mobile_ios / False / False
- **Stack:** langs TypeScript; JavaScript; Python; Swift; frontend Next.js; React; SwiftUI; RealityKit; backend Supabase; Python; db Supabase; hosting Vercel (per repo About link)
- **Tech/APIs:** Supabase (database, core); RealityKit (framework, core); Next.js (framework, core); SwiftUI (framework, core); USDZ (other, supporting)
- **Sponsor APIs:**  | fit: Datacenter-operations tool entered for Northmark Compute & Cloud; no Northmark-specific API named in the writeup.
- **Repo:** public, commits 36 (before/in/after event: 0/32/0), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 10, writeup short, impact claims False
- **Notes:** Two repos: a Next.js/Supabase web app (with Python folder) and a separate iOS RealityKit AR app letting a remote user point at a server item. Jira board shown in screenshots.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; repo_commits (32 web + 4 iOS); ai_used (not mentioned in writeup); live demo (repo About lists a Vercel link that could not be fetched)
- **Links:** [Devpost](https://devpost.com/software/d-68uye4) | [GitHub](https://github.com/NEjim2001/hackutd-2025)

### Toyotron  (HackUTD 2025)

- **Prizes:** Toyota Financial Services [unknown]; Nvidia [unknown]  (tier: sponsor_winner)
- **Pitch:** AI car-buying concierge that surveys shoppers, recommends Toyotas, chats or simulates phone calls, and books test drives and emails quotes.
- **Problem / user:** Car shoppers lack confidence, time and knowledge to take the first step toward buying. / Prospective Toyota car buyers
- **Domain / idea type:** retail_consumer + mobility_transport / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; speech_or_voice; recommendation
- **Stack:** langs TypeScript; CSS; frontend Next.js; Tailwind; backend Next.js API routes; db Supabase; hosting Vercel
- **Tech/APIs:** Nvidia Nemotron (ai_model, core, sponsor); OpenRouter (ai_model, core); Retell (ai_model, supporting); Resend (other, supporting); Google Calendar (other, supporting); Supabase (database, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:** Nvidia Nemotron | fit: Built explicitly for the Toyota and Nvidia tracks: Nemotron powers agent reasoning for a Toyota shopping assistant.
- **Repo:** public, commits 96 (before/in/after event: 0/93/3), README detailed
- **Demo/writeup:** video None, live not_checked, screenshots 8, writeup long, impact claims False
- **Notes:** Named from Toyota plus Nemotron to target two sponsor tracks; multi-agent orchestration with tool layer for email, calendar and trade-in estimates; phone-style voice agent via Retell.
- **Team size:** 5 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; live_demo_status; repo_commits; first_commit; last_commit; commits_in_event_window; ui_polish; team_size
- **Links:** [Devpost](https://devpost.com/software/toyotron) | [GitHub](https://github.com/anbguye/hackutd-Toyota-Toyotron)

### TrustEstate AI  (HackUTD 2025)

- **Prizes:** CBRE [unknown]  (tier: sponsor_winner)
- **Pitch:** Real estate browsing app with a Google Maps interface where a Gemini assistant fact-checks property data against Google Search and assigns each listing a trust score.
- **Problem / user:** Consumers cannot tell whether online property listing information is reliable or current. / home buyers and property researchers
- **Domain / idea type:** housing_real_estate + ai_agents_infra / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs TypeScript; frontend React; Vite; Tailwind; shadcn; Recharts; backend ; db browser localStorage; properties.json (mock); hosting 
- **Tech/APIs:** Gemini (ai_model, core); Google Search tool-calling (data_source, core); Google Maps API (maps_geo, core); CBRE property data (simulated) (data_source, supporting, sponsor); Recharts (framework, supporting)
- **Sponsor APIs:**  | fit: Framed around CBRE commercial property data, though the demo uses self-made mock property profiles because CBRE data is private.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 8, writeup long, impact claims False
- **Notes:** Property data is a mock properties.json imitating CBRE data; saved items persist in browser localStorage. Gemini uses tool-calling with Google Search to verify facts and produce confidence meters.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; placement; repo_commits; first_commit; last_commit
- **Links:** [Devpost](https://devpost.com/software/cbre-project)

### TrustIssues.AI  (HackUTD 2025)

- **Prizes:** Goldman Sachs [unknown]  (tier: sponsor_winner)
- **Pitch:** Multi-agent system that extracts vendor PDF data, screens against sanctions lists, scores risk by rules, and requires human sign-off before granting access.
- **Problem / user:** Onboarding vendors and clients is slow, inconsistent and risky because teams manually review documents and databases. / compliance and vendor-onboarding teams at enterprises
- **Domain / idea type:** fintech_finance + safety_security / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; frontend Streamlit; backend Python; PyPDF2; FuzzyWuzzy; OpenAI SDK; db ; hosting 
- **Tech/APIs:** NVIDIA Nemotron-49B-Instruct (ai_model, core, sponsor); Streamlit (framework, supporting); PyPDF2 (other, supporting); FuzzyWuzzy sanctions check (data_source, supporting)
- **Sponsor APIs:** NVIDIA Nemotron | fit: Targeted at Goldman Sachs with a compliance-style vendor risk workflow using human-in-the-loop approval and audit logging; also uses NVIDIA Nemotron for explanations.
- **Repo:** public, commits 9 (before/in/after event: 0/9/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 8, writeup long, impact claims True (States onboarding can take up to six months; no measured results from the tool.)
- **Notes:** ReAct-style Coordinator, Extractor, Verifier and Risk Analyst agents; risk score is deterministic rules code, LLM only explains; verification uses mock APIs; every step logged to JSON audit trail.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement
- **Links:** [Devpost](https://devpost.com/software/coffee-overflow) | [GitHub](https://github.com/ybavgito/TrustIssues.AI)

### UpGuardian  (HackUTD 2025)

- **Prizes:** StateFarm [unknown]  (tier: sponsor_winner)
- **Pitch:** Developer service that detects breaking changes when upgrading API versions, using deterministic diffing guided by an agentic LLM.
- **Problem / user:** Migrating to a new API version means tediously testing endpoints and hunting subtle response differences by hand. / Application developers consuming third-party APIs
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web; desktop / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; Dart; frontend Flutter; backend FastAPI; db SQLite; hosting 
- **Tech/APIs:** Nvidia Nemotron (ai_model, core, sponsor); FastAPI (framework, core); Flutter (framework, core); SQLite (database, supporting)
- **Sponsor APIs:** Nvidia Nemotron | fit: Writeup does not mention State Farm specifically; it is a developer tool using Nvidia's Nemotron model.
- **Repo:** public, commits 50 (before/in/after event: 0/50/0), README none
- **Demo/writeup:** video None, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Dashboard proxies API calls to protect tokens; uploaded request logs feed tests; deterministic diff engine is paired with Nemotron agent; multi-tenant auth only groundwork, not implemented.
- **Team size:** 5 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; platforms; repo_commits; first_commit; last_commit; commits_in_event_window; readme_quality; ui_polish; team_size; stack_hosting; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/upguard) | [GitHub](https://github.com/Arian04/UpGuardian)

### VisionScout  (HackUTD 2025)

- **Prizes:** Best Hardware [unknown]  (tier: sponsor_winner)
- **Pitch:** Smart-glasses video is analyzed by a YOLO model to auto-build car and property listings with condition scores, plus an AI chat that recommends matching listings.
- **Problem / user:** Online car and property listings rely on subjective descriptions, so buyers cannot easily judge real condition. / car and home buyers and listing creators
- **Domain / idea type:** retail_consumer + housing_real_estate / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision; llm_chat; agent_or_tool_use; recommendation
- **Stack:** langs Python; TypeScript; frontend React; Tailwind; backend Flask; LangGraph; Selenium; BeautifulSoup4; db ; hosting 
- **Tech/APIs:** YOLO (locally trained) (ai_model, core); Voxel smart glasses and SDK (hardware_part, core, sponsor); Gemini 2.5 Pro (ai_model, core); LangGraph (framework, supporting); Zillow API (data_source, supporting); Cars.com scraping (data_source, supporting)
- **Sponsor APIs:** Voxel smart glasses | fit: Built the hardware-track entry on the event-provided smart glasses, running a custom vision model against their SDK to capture defects.
- **Repo:** public, commits 27 (before/in/after event: 0/26/1), README thin
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Used event-provided Voxel smart glasses; team patched a buggy SDK and trained a local YOLO detector because the default API was slow; car data scraped from Cars.com.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; first_commit; last_commit; commits_in_event_window; placement; Voxel glasses sponsor status
- **Links:** [Devpost](https://devpost.com/software/coolproject69) | [GitHub](https://github.com/ClosetCoderSad/VisionScout)

### WiSPR - Wireless Safety Pulse Relay  (HackUTD 2025)

- **Prizes:** Best Beginner [unknown]  (tier: track_winner)
- **Pitch:** Wearable Arduino badge that senses heat and humidity hazards and lets teammates exchange silent vibration/LED alerts, with a React ticket dashboard.
- **Problem / user:** Technicians in loud, hazardous workplaces cannot reliably hear or see danger or communicate with teammates. / Industrial technicians working in noisy environments
- **Domain / idea type:** safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / False
- **Stack:** langs C++; JavaScript; CSS; frontend React; CSS; backend ; db ; hosting 
- **Tech/APIs:** Arduino (hardware_part, core); DHT11 sensor (hardware_part, core); React (framework, core); Figma (other, supporting); AutoCAD (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 5 (before/in/after event: 0/5/0), README thin
- **Demo/writeup:** video None, live none, screenshots 3, writeup long, impact claims False
- **Notes:** Breadboard prototype with DHT11 sensor, LCD, LEDs, buzzer and two Arduinos exchanging serial alerts; also an AutoCAD badge model, Figma design and React dashboard on simulated data.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; demo_video_url; repo_commits; first_commit; last_commit; commits_in_event_window; ui_polish
- **Links:** [Devpost](https://devpost.com/software/wispr-wireless-safety-pulse-relay) | [GitHub](https://github.com/ParisUNgo/HackUTD-WiSPR)

### Working Memory  (HackUTD 2025)

- **Prizes:** Winner General Track [unknown]  (tier: track_winner)
- **Pitch:** Agentic dev tool that watches coding sessions in VS Code and generates searchable summaries so developers can regain context after switching projects.
- **Problem / user:** Students switching between coding projects lose the reasoning, pending tasks and mental model behind their code. / student and hobbyist developers juggling several projects
- **Domain / idea type:** dev_tools + productivity_workplace / dev_tool
- **Platforms / hardware / AI:** web; desktop / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs TypeScript; Python; JavaScript; HTML; frontend React; Tailwind CSS; backend FastAPI; Uvicorn; GitPython; db ; hosting 
- **Tech/APIs:** GPT-4.1-mini (ai_model, core); OpenAI Agents SDK (framework, supporting); OpenRouter (ai_model, supporting); Model Context Protocol / VS Code extension (framework, core); FastAPI (framework, core); React + Tailwind (framework, core); GitPython (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 35 (before/in/after event: 0/29/6), README solid
- **Demo/writeup:** video True, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Three-part system: React dashboard, VS Code extension exposing an MCP-style HTTP endpoint, and FastAPI agent that sends git changelogs to GPT-4.1-mini. README claims a 1st place grand prize (unverified).
- **Team size:** 3 | **Confidence:** medium | unverified: n_screenshots; first_commit; last_commit; commits_in_event_window; ui_polish; placement; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/working-memory) | [GitHub](https://github.com/Mihirz/HackUTDProject)
