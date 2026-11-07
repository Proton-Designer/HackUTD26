# DubHacks: project cards (38 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## DubHacks '26

### Brawlmegle  (DubHacks '26)

- **Prizes:** Chef's Kitchen: 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Webcam fighting game that scans you into a rigged 3D fighter and lets you box peer-to-peer using body-motion intent detection.
- **Problem / user:** Motion boxing games lack the impact and feel of classic arcade fighters; the team wanted that effect from a camera. / casual gamers with a webcam
- **Domain / idea type:** entertainment_games + creative_media / entertainment_or_game
- **Platforms / hardware / AI:** web / False / vision; generative_media; speech_or_voice; llm_chat
- **Stack:** langs TypeScript; frontend React; Three.js; MediaPipe; backend WebRTC relay on EC2; db ; hosting AWS EC2; AWS GPU
- **Tech/APIs:** MediaPipe (ai_model, core); TRELLIS.2 (ai_model, core); GPT (ai_model, supporting); ElevenLabs (ai_model, supporting); Three.js (framework, core); WebRTC (framework, core); AWS EC2/GPU (cloud, core); Blender (other, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 14, writeup medium, impact claims False
- **Notes:** Own GPU server runs TRELLIS.2 to make a 3D fighter from a scan in about 40 seconds with a custom Blender auto-rigger; Omegle-style WebRTC matchmaking; ElevenLabs live commentary.
- **Team size:** 4 | **Confidence:** high | unverified: sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/brawlmegle)

### Codegraph  (DubHacks '26)

- **Prizes:** Cook Smarter: 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** VS Code extension that graphs a C/C++ codebase, explains nodes with AI, and scores the risk of changing each node.
- **Problem / user:** With more AI-written code, developers lose understanding of large codebases that are hard to navigate, especially beginners. / C/C++ developers and beginners
- **Domain / idea type:** dev_tools + education / dev_tool
- **Platforms / hardware / AI:** other / False / llm_chat; rag_or_search
- **Stack:** langs TypeScript; JavaScript; C; C++; frontend Cytoscape.js; cytoscape-elk; HTML; CSS; backend VS Code extension host; db ; hosting 
- **Tech/APIs:** Cytoscape.js (framework, core); VS Code Language Model API (ai_model, core); GPT-4o / GitHub Copilot Chat (ai_model, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 80 (before/in/after event: 0/80/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Calls VS Code Language Model API (Copilot Chat or GPT-4o); Ask AI panel highlights and traces affected nodes; change-risk score per node; limited to C/C++ so far.
- **Team size:** 2 | **Confidence:** high | unverified: platforms
- **Links:** [Devpost](https://devpost.com/software/codegraph-1nj2ku) | [GitHub](https://github.com/kx1100/Dubhacks-26)

### Delta  (DubHacks '26)

- **Prizes:** 2nd Place Perceptron: Perception [2nd]  (tier: sponsor_winner)
- **Pitch:** Git-style version control for hardware: an overhead camera logs each bench change as a commit with before/after images and an AI description.
- **Problem / user:** Hardware prototyping has no change history; people lose working states and rely on phone photos and chat messages. / hardware engineers, robotics teams and EE students
- **Domain / idea type:** dev_tools + education / dev_tool
- **Platforms / hardware / AI:** web; hardware / True / vision; llm_chat; rag_or_search
- **Stack:** langs Python; TypeScript; frontend React 19; Vite; Tailwind; shadcn/ui; TanStack Query; backend Python; Supabase Realtime; db Supabase Postgres; Supabase Storage; hosting NVIDIA Jetson Orin Nano
- **Tech/APIs:** Perceptron Mk1.5 (ai_model, core, sponsor); OpenCV (framework, core); NVIDIA Jetson Orin Nano (hardware_part, core); Supabase (database, core); USB webcam (hardware_part, core)
- **Sponsor APIs:** Perceptron | fit: Used Perceptron Mk1.5 with strict JSON schema, low reasoning effort and prior-frame context to identify components and bounding boxes in crops.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims False
- **Notes:** OpenCV pixel pipeline decides if something changed; Perceptron Mk1.5 only names parts; runs on Jetson Orin Nano in a printed enclosure; 61 backend and 12 frontend tests; zero false positives on 100 frames.
- **Team size:** 4 | **Confidence:** high | unverified: repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/delta-o91du3) | [GitHub](https://github.com/Aditya9246/dh26/tree/final)

### Drone Perceptron Relief System  (DubHacks '26)

- **Prizes:** Winner Community Kitchen: 1st Place [1st]  (tier: track_winner)
- **Pitch:** Semi-automatic disaster-relief drone system: Perceptron model finds people and distance, data lands in TigerData, and an optimizer picks the next drone move.
- **Problem / user:** Disaster drone relief is manual, error-prone under stress and hard to standardize, giving poor emergency response. / disaster response teams
- **Domain / idea type:** safety_security + civic_legal / data_or_analytics
- **Platforms / hardware / AI:** web; other / True / vision; predictive_ml
- **Stack:** langs Python; SQL; HTML; frontend HTML; backend Python; db TigerData; hosting 
- **Tech/APIs:** Perceptron model (ai_model, core, sponsor); TigerData (database, core, sponsor); Drones (telemetry and footage) (hardware_part, core)
- **Sponsor APIs:** Perceptron; TigerData | fit: Used Perceptron's vision model to detect people and distance, and TigerData as the time-series store, in a disaster-response loop.
- **Repo:** public, commits 38 (before/in/after event: 0/37/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 0, writeup short, impact claims True (Says optimization is about 8x faster median response than brute force on benchmarks.)
- **Notes:** Closed loop from drone telemetry to people-detection to 2D map to optimizer; claims about 8x faster median response than brute force on benchmarks; demo video sped up and author asks 0.75x viewing.
- **Team size:** 4 | **Confidence:** high | unverified: has_hardware; platforms; stack_frontend; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/drone-perceptron-relief-system) | [GitHub](https://github.com/ashwin-builds/optimized-drone-search)

### dump  (DubHacks '26)

- **Prizes:** VEYZL: First Place [1st]  (tier: sponsor_winner)
- **Pitch:** Event photo-sharing rooms with no app or account: scan a QR, upload, find yourself by face, search by content, and everything auto-deletes after 24-72 hours.
- **Problem / user:** Collecting everyone's event photos is messy across group chats, AirDrop and shared drives, and finding photos of yourself in hundreds of shots is tedious. / friend groups and event attendees
- **Domain / idea type:** social_community + creative_media / twist_on_known_app
- **Platforms / hardware / AI:** web; bot_or_chat / False / vision; speech_or_voice; rag_or_search; llm_chat; agent_or_tool_use; generative_media
- **Stack:** langs ; frontend Next.js; Tailwind CSS; PWA; backend background worker; Docker Compose; Caddy; db MongoDB; TigerData; Cloudflare R2; hosting Vultr; Cloudflare
- **Tech/APIs:** Perceptron (ai_model, core, sponsor); Photon 2.0 iMessage (telecom, core, sponsor); VEYZL (other, supporting, sponsor); Backboard (ai_model, core, sponsor); InsightFace (ai_model, core); faster-whisper (ai_model, supporting); BiRefNet (ai_model, supporting); MongoDB (database, core, sponsor); TigerData (database, supporting, sponsor); Vultr (cloud, core, sponsor); Cloudflare R2 (cloud, core); Next.js (framework, core)
- **Sponsor APIs:** Perceptron; Photon; VEYZL; Backboard; MongoDB; TigerData; Vultr | fit: Pointed VEYZL audits at its public vision endpoint and reworked refusals, redaction and answer checking based on the findings.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup long, impact claims False
- **Notes:** Rooms can be created over iMessage via Photon; VEYZL safety audits were run on the vision endpoint and fed back into fixes; page also lists an MLH Vultr win not in the queue.
- **Team size:** 5 | **Confidence:** high | unverified: n_screenshots; team_size
- **Links:** [Devpost](https://devpost.com/software/dump-imwsvx)

### Formly - the secure, fast form filler  (DubHacks '26)

- **Prizes:** T-Mobile: 1st Place [1st]  (tier: sponsor_winner)
- **Pitch:** A drop-in 'Fill with Formly' button that builds a private data profile from the user's files and accounts and fills any form with per-field source and approval.
- **Problem / user:** Forms repeatedly ask for the same personal details, and browser autofill misses sensitive or document-based fields like SSNs, IDs and VINs. / people filling long forms and businesses hosting them
- **Domain / idea type:** productivity_workplace + safety_security / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; vision; agent_or_tool_use
- **Stack:** langs TypeScript; JavaScript; frontend Next.js; React; Tailwind CSS; backend Node.js; Next.js API; db SQLite; hosting Docker
- **Tech/APIs:** Gemini API (ai_model, core); Next.js (framework, core); SQLite (database, supporting); Nemotron-Personas-USA (data_source, supporting); T-Mobile synthetic data (data_source, supporting, sponsor); Claude (fallback) (ai_model, token)
- **Sponsor APIs:**  | fit: T-Mobile signup form is one of four demo forms and T-Mobile synthetic data was used for testing; no T-Mobile API used.
- **Repo:** public, commits 114 (before/in/after event: 0/114/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims True (Reports 107 of 108 field checks correct on its synthetic test set.)
- **Notes:** Short written answers must quote facts that code verifies against the profile; blank fields preferred over guesses; four demo forms styled after T-Mobile, SpaceXAI, Chase and DMV; test set from synthetic personas.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/formly-the-secure-fast-form-filler) | [GitHub](https://github.com/salvobonsma/DubHacks2026)

### Husky Dormers  (DubHacks '26)

- **Prizes:** CloudForce: Raffle [unknown]  (tier: sponsor_winner)
- **Pitch:** Website for UW students to plan dorm cooking events and delegate cooking tasks among people gathering for a shared purpose.
- **Problem / user:** Students find campus dining unsatisfactory and want an easy way to organize shared meals in dorms. / UW dorm residents
- **Domain / idea type:** housing_real_estate + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; SQL; HTML; CSS; frontend React; backend ; db SQL; hosting 
- **Tech/APIs:** React (framework, core); TypeScript (framework, supporting)
- **Sponsor APIs:**  | fit: Prize is a CloudForce raffle, not a challenge; no CloudForce product use appears on the page.
- **Repo:** public, commits 47 (before/in/after event: 0/47/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup medium, impact claims False
- **Notes:** First-time hackers' React and TypeScript site; won a CloudForce raffle prize rather than a judged award.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; prizes.placement
- **Links:** [Devpost](https://devpost.com/software/husky-dormers) | [GitHub](https://github.com/agent965/dormplanner)

### Kill-Switch  (DubHacks '26)

- **Prizes:** T-Mobile: 3rd Place [3rd]  (tier: sponsor_winner)
- **Pitch:** ESP32 breadboard device that flags risky websites with LEDs and a buzzer using an AI screen check and URL risk score, with a button that texts a caregiver.
- **Problem / user:** Screen-based fraud warnings fail users with cognitive, visual or motor impairments, leaving them exposed to scams. / older or disabled users and their caregivers
- **Domain / idea type:** safety_security + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision; llm_chat
- **Stack:** langs C; Python; frontend ; backend FreeRTOS; Python; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Gemini API (ai_model, core); APIVoid (data_source, core); Twilio (telecom, supporting); FreeRTOS (framework, supporting)
- **Sponsor APIs:**  | fit: Page does not name T-Mobile; uses Twilio for the caregiver text alert.
- **Repo:** public, commits 2 (before/in/after event: 0/2/0), README none
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims True (Cites $7.7 billion lost to internet fraud by Americans 60+ in 2025.)
- **Notes:** Runs FreeRTOS tasks on an ESP32 that calls APIs over Wi-Fi; Python and C talk over a COM port; built from parts left from university hardware classes; breadboard only.
- **Team size:** 2 | **Confidence:** high | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/kill-switch-sb82du) | [GitHub](https://github.com/turboz23/killSwitch)

### KO.rbit  (DubHacks '26)

- **Prizes:** SpaceXAI: 1st Place [1st]  (tier: sponsor_winner)
- **Pitch:** Full-body lightsaber duel using laptop pose tracking and a phone gyro as the blade, plus a 3D explorer of 31,266 real space objects and an AI voice guide.
- **Problem / user:** Wanted a physical living-room saber duel on real planetary terrain with space data that is real, built quickly with AI tools. / gamers and space enthusiasts
- **Domain / idea type:** entertainment_games + education / entertainment_or_game
- **Platforms / hardware / AI:** web; mobile_ios / False / speech_or_voice; vision; generative_media; agent_or_tool_use
- **Stack:** langs TypeScript; JavaScript; Python; frontend React; Vite; React Three Fiber; Three.js; MediaPipe; backend Node.js; Socket.IO; db ; hosting 
- **Tech/APIs:** Grok Voice (ai_model, core, sponsor); Grok Imagine (ai_model, supporting, sponsor); Grok text-to-speech (ai_model, supporting, sponsor); Perceptron Mk1.5 (ai_model, core, sponsor); MediaPipe Pose (ai_model, core); Three.js (framework, core); NASA/JPL/CelesTrak/HYG data (data_source, core); Cursor (other, supporting)
- **Sponsor APIs:** Grok Voice; Grok Imagine; Grok TTS; Perceptron | fit: Used Grok Voice for the live LYRA guide, Grok Imagine for her look, and Grok agents for research and design; Perceptron also powers replays.
- **Repo:** public, commits 175 (before/in/after event: 0/164/11), README detailed
- **Demo/writeup:** video True, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Server is authoritative for hits and stamina; Mars arena uses NASA MOLA heightmap; opt-in Perceptron KO replay recut; writeup details an AI agent crew used for research, sound and audits.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; team_size
- **Links:** [Devpost](https://devpost.com/software/space-battles-aei3wz) | [GitHub](https://github.com/alnnguyen/Dubhacks26)

### Lapse  (DubHacks '26)

- **Prizes:** Visa: Reimagine Shopping [n/a]; SideShift: 3rd Place [3rd]  (tier: sponsor_winner)
- **Pitch:** Browser extension that collects rewards from a dedicated inbox and uses a constraint solver to stack coupons, memberships and card cashback at checkout.
- **Problem / user:** Shoppers collect loyalty rewards and coupons but forget or misuse them, losing savings. / online shoppers and merchants running loyalty programs
- **Domain / idea type:** retail_consumer + fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** browser_extension; web / False / predictive_ml; recommendation; rag_or_search
- **Stack:** langs Python; TypeScript; frontend React; WXT; Chrome extension; backend FastAPI; Pydantic; Postmark; db PostgreSQL; pgvector; pgcrypto; hosting Docker
- **Tech/APIs:** Google OR-Tools CP-SAT (framework, core); SetFit (ai_model, core); GLiNER (ai_model, supporting); Presidio (framework, supporting); pgvector (database, supporting); Postmark (other, supporting)
- **Sponsor APIs:**  | fit: Framed around Visa's loyalty-rewards statistics and card-benefit stacking for the shopping track; no Visa API listed.
- **Repo:** public, commits 54 (before/in/after event: 0/53/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims True (Cites Visa figures of 17.4 memberships held vs 8.8 used and up to $10 billion missed annually; labels benefits as potential, not measured.)
- **Notes:** OR-Tools CP-SAT stacking with 200ms budget and greedy fallback; locally trained SetFit email classifier plus JSON-LD, regex and GLiNER extraction; encrypted reward codes; claims no outside service calls.
- **Team size:** 4 | **Confidence:** high | unverified: sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/vouch-ld4voh) | [GitHub](https://github.com/asyaafv/DubHacks26)

### Make a Drink!  (DubHacks '26)

- **Prizes:** Best Freshman Beginner Project [unknown]  (tier: track_winner)
- **Pitch:** Browser 3D virtual bar where players learn cocktail recipes, practice pouring and serve AI-generated customers.
- **Problem / user:** Bartending practice is hard to access; the author wanted a playable bartender simulator. / casual players and cocktail learners
- **Domain / idea type:** entertainment_games + education / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat; generative_media
- **Stack:** langs TypeScript; frontend Next.js; React; Three.js; react-three-fiber; Tailwind CSS; backend Node.js; db ; hosting Vercel
- **Tech/APIs:** Gemini (ai_model, core); Three.js / react-three-fiber (framework, core); Rapier (framework, supporting); Claude (ai_model, token); Backboard (other, unclear)
- **Sponsor APIs:**  | fit: Event-run Best Freshman Beginner Project award; no sponsor tool targeted.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup short, impact claims False
- **Notes:** Solo freshman build with Three.js scene, Rapier ice physics and Gemini-written customer orders.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; prizes.placement; ai_types
- **Links:** [Devpost](https://devpost.com/software/make-a-drink-3ful2k)

### Noxen  (DubHacks '26)

- **Prizes:** SideShift: 2nd Place [2nd]; DubHacks Next: 1st Place [1st]  (tier: sponsor_winner)
- **Pitch:** Autonomous nightly facility inspection: LiDAR scans diffed against a baseline, a vision-language model triages changes, and a camera-only drone is dispatched by text.
- **Problem / user:** Facility and construction inspections are manual, costly and infrequent, so small defects go unnoticed between visits. / facility operators and construction managers
- **Domain / idea type:** safety_security + productivity_workplace / hardware_gadget
- **Platforms / hardware / AI:** web; hardware; bot_or_chat / True / vision; agent_or_tool_use; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; Vite; backend FastAPI; ROS 2; WebSockets; db SQLite; hosting Raspberry Pi
- **Tech/APIs:** Perceptron vision-language model (ai_model, core, sponsor); Photon messaging agent (telecom, core, sponsor); Unitree L2 LiDAR (hardware_part, core); Open3D (framework, core); Depth Anything V2 (ai_model, core); YOLO (ai_model, supporting); ROS 2 (framework, core); OpenAI (ai_model, unclear)
- **Sponsor APIs:** Perceptron; Photon | fit: Used Perceptron's vision-language model to triage before/after changes and a Photon agent to text alerts and dispatch the drone; page also ties itself to the Cook Smarter theme.
- **Repo:** public, commits 1 (before/in/after event: 0/1/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup long, impact claims False (States customer calls with construction directors and a planned paid pilot, no numeric market claims.)
- **Notes:** Scout drone localizes in a LiDAR-built map using only its camera; monocular depth scaled via the map; hot-swap battery mechanism; change detection tuned to measured 2 cm sensor noise; SMS dispatch via Photon.
- **Team size:** 2 | **Confidence:** high | unverified: team_size
- **Links:** [Devpost](https://devpost.com/software/noxen) | [GitHub](https://github.com/RonRastorguev/noxendh)

### Octaby  (DubHacks '26)

- **Prizes:** SideShift: 1st Place [1st]  (tier: sponsor_winner)
- **Pitch:** Fabric wristband with four haptic motors that cues blind and low-vision users which direction to move their hand to reach an object.
- **Problem / user:** Assistive tools focus on navigation, with few helping blind users locate and reach small objects such as items on a table. / blind and low-vision users
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_ios / True / vision; speech_or_voice; agent_or_tool_use
- **Stack:** langs Swift; Python; frontend iOS app; ARKit; backend Uvicorn; db ; hosting 
- **Tech/APIs:** Perceptron (ai_model, core, sponsor); ARKit / LiDAR (hardware_part, core); OpenAI (ai_model, unclear); Haptic vibration motors with Arduino (hardware_part, core)
- **Sponsor APIs:** Perceptron | fit: No explicit SideShift tie; the page describes a working assistive-wearable prototype built end to end in a day.
- **Repo:** public, commits 120 (before/in/after event: 14/106/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 9, writeup medium, impact claims False
- **Notes:** Pivoted a few hours in from a 3D-printed servo bracelet to a sewn fabric band with conductive thread and Arduino; audio goes to Perceptron to produce guidance; ARKit/LiDAR iOS side; stores remembered objects.
- **Team size:** 4 | **Confidence:** high | unverified: tech_items.is_sponsor; sponsor_fit_note; stack_backend
- **Links:** [Devpost](https://devpost.com/software/octaby) | [GitHub](https://github.com/Eddwal/haptic-reach-demo)

### OpenCanopy  (DubHacks '26)

- **Prizes:** DubHacks Next: 2nd Place [2nd]; 1st Place Perceptron: Perception [1st]  (tier: sponsor_winner)
- **Pitch:** One-click satellite check of a land plot for post-2020 deforestation, combining loss maps with a vision model and producing a printable case file.
- **Problem / user:** EU deforestation rules need per-plot verification, but checking requires GIS expertise and multiple datasets, so approvals rely on self-declared claims. / EU regulators, importers and forest-adjacent communities
- **Domain / idea type:** sustainability_climate + civic_legal / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend MapLibre GL; HTML/CSS/JS; backend Python server; rasterio; shapely; NumPy; db ; hosting Slurm (UW Hyak)
- **Tech/APIs:** Perceptron Mk1.5 (ai_model, core, sponsor); Sentinel-2 via Microsoft Planetary Computer (data_source, core); Hansen Global Forest Change (data_source, core); JRC Global Forest Cover 2020 (data_source, core); MapLibre GL (maps_geo, supporting); Cursor (other, token)
- **Sponsor APIs:** Perceptron | fit: Used Perceptron Mk1.5 on before/after Sentinel-2 pairs and year-by-year video to box converted regions, then cross-checked them against loss pixels.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup long, impact claims True (Cites EUR 126 billion annual covered imports, 6.7 million hectares tropical primary forest lost in 2024, and 880 ha cleared on the sample plot.)
- **Notes:** Region confirmed only if at least 25% shows post-2020 loss, else inconclusive; global sweep of clearings run on a university cluster; reported 100% precision and 67% recall on a 48-chip test.
- **Team size:** 3 | **Confidence:** high | unverified: stack_database
- **Links:** [Devpost](https://devpost.com/software/clearcut-p5hmfx)

### PathWise  (DubHacks '26)

- **Prizes:** CloudForce: Most Creative [unknown]  (tier: sponsor_winner)
- **Pitch:** Walking-route app for the UW campus area that finds safer routes by penalizing poorly lit or awkward segments within a capped time budget.
- **Problem / user:** Conventional maps pick the shortest path and ignore how safe or comfortable a walk home feels. / students walking around campus
- **Domain / idea type:** safety_security + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / False
- **Stack:** langs Python; TypeScript; frontend React Native; Expo; backend FastAPI; Uvicorn; Pydantic; SQLAlchemy; JWT; db PostgreSQL; hosting 
- **Tech/APIs:** FastAPI (framework, core); Expo / React Native (framework, core); PostgreSQL (database, supporting); Walking graph routing (data_source, core)
- **Sponsor APIs:**  | fit: Won CloudForce 'Most Creative' prize; page text names no CloudForce or Salesforce tools, so sponsor tool use is not shown.
- **Repo:** public, commits 32 (before/in/after event: 0/32/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 25, writeup long, impact claims False
- **Notes:** Safety modeled as edge penalties and weights on a walking graph with a 30% extra-time cap; Expo React Native client with FastAPI server; two different video links listed.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; n_screenshots; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/pathwise-zm305y) | [GitHub](https://github.com/Ethant06/PathWise)

### Pollensight  (DubHacks '26)

- **Prizes:** Winner Community Kitchen: 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Turns fixed-camera video into per-flower insect visit records, forecasts insect paths and plans a pollinator robot route, with an RL bee simulation.
- **Problem / user:** Pollinators are declining and crops depend on them; growers lack actionable data on which flowers get visited and how a robot could help. / growers and agricultural robotics researchers
- **Domain / idea type:** sustainability_climate + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; predictive_ml; rag_or_search; other
- **Stack:** langs Python; TypeScript; frontend React 19; Vite; three.js; Canvas 2D; SVG; backend Node.js; Python; db ; hosting 
- **Tech/APIs:** Perceptron Mk1.5 (ai_model, core, sponsor); OpenCV (framework, core); scikit-learn (framework, supporting); Stable-Baselines3 / Gymnasium (framework, core); MuJoCo (Crazyflie 2 model) (framework, supporting); Monash insect datasets (data_source, core); three.js (framework, supporting)
- **Sponsor APIs:** Perceptron | fit: Used Perceptron Mk1.5 for box detection, JSON-schema output and Files API to verify insects and locate flowers in video.
- **Repo:** public, commits 66 (before/in/after event: 0/66/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims True (Cites a third of food depending on pollinators and reports accuracy figures such as 90% tracking coverage and 79% top-3 next-flower accuracy.)
- **Notes:** Cheap OpenCV tracker confirmed by Perceptron Mk1.5 crops (visit precision 64% to 90%); cached API client replays offline; RL bee replayed in MuJoCo with Crazyflie model; 48 clips from public datasets.
- **Team size:** 4 | **Confidence:** high | unverified: stack_database; stack_hosting; domain_secondary
- **Links:** [Devpost](https://devpost.com/software/beebot-zbaxvy) | [GitHub](https://github.com/b-ananya/pollensight)

### ReMind  (DubHacks '26)

- **Prizes:** 2nd Place Perceptron: Robotics [2nd]; [MLH] Best Use of Backboard [unknown]  (tier: sponsor_winner)
- **Pitch:** Voice memory-game companion for dementia care that starts a robot-arm keychain shuffle game and texts caregivers if the resident says something worrying.
- **Problem / user:** Nursing home residents with dementia lack staff-led cognitive activities, and existing digital tools are hard for older adults to use. / dementia residents and caregivers
- **Domain / idea type:** mental_health + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / speech_or_voice; llm_chat; agent_or_tool_use; vision; predictive_ml
- **Stack:** langs Python; TypeScript; frontend Next.js; backend FastAPI; Node service; db ; hosting 
- **Tech/APIs:** Gemini Live API (ai_model, core, sponsor); Backboard (other, core, sponsor); Photon (iMessage SDK) (telecom, supporting, sponsor); Perceptron cloud training (ai_model, supporting, sponsor); SO-101 arm with LeRobot (hardware_part, core)
- **Sponsor APIs:** Gemini; Backboard; Photon; Perceptron | fit: Used Backboard for long-term voice memory and Perceptron's cloud to train arm policies, though the page says the learned policy could not reliably grasp.
- **Repo:** public, commits 188 (before/in/after event: 0/188/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims True (Says nearly half of nursing home residents live with dementia; reports honest robot results such as 5 of 7 re-picks working.)
- **Notes:** AI can only call a short allowlisted tool set enforced by server and robot code; SO-101 arm trained from 60 demos but demo runs taught positions with camera verification; Photon iMessage alerts.
- **Team size:** 4 | **Confidence:** high | unverified: stack_database; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/remind-y8kg9s) | [GitHub](https://github.com/remind-dubhacks/dubhacks-2026)

### Robo-view  (DubHacks '26)

- **Prizes:** 1st Place Perceptron: Robotics [1st]  (tier: sponsor_winner)
- **Pitch:** Voice- or text-commanded SO-101 robot arm with a camera that films products from dynamic cinematic angles using a trained movement policy.
- **Problem / user:** Dynamic-angle product videos are laborious to shoot; the team wanted algorithmic robot cinematography that is smooth and efficient. / product marketers and video creators
- **Domain / idea type:** creative_media + retail_consumer / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_cross / True / vision; speech_or_voice; agent_or_tool_use; predictive_ml
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** SO-101 robotic arm (hardware_part, core); Isaac 0.5 model (ai_model, core, sponsor); Perceptron Mk1.5 API (ai_model, supporting, sponsor)
- **Sponsor APIs:** Perceptron | fit: Trained a robot arm policy on Perceptron's Isaac model and used the Perceptron API to relabel bounding boxes, matching the Robotics track.
- **Repo:** public, commits 54 (before/in/after event: 0/53/1), README solid
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** About 75 teleoperated demonstrations (25 per movement) used to train with Isaac 0.5; Perceptron used to relabel data with bounding boxes; app returns recorded video to the user.
- **Team size:** 4 | **Confidence:** high | unverified: platforms; stack_frontend; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/robo-view) | [GitHub](https://github.com/kaleturner/dubhacks_2026/tree/main)

### Saykind  (DubHacks '26)

- **Prizes:** CloudForce: Most Viral [unknown]  (tier: sponsor_winner)
- **Pitch:** Calm browser-based practice space for adults with aphasia to rehearse everyday words and then use them in a supported conversation.
- **Problem / user:** People with aphasia after stroke struggle to retrieve words and lack gentle, low-pressure practice tools. / adults with aphasia
- **Domain / idea type:** accessibility + health_wellness / social_good
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice
- **Stack:** langs TypeScript; frontend Next.js; React; React Native Web; Tailwind CSS; Framer Motion; GSAP; backend Node.js; Zod; db ; hosting Vercel
- **Tech/APIs:** Claude (Anthropic) (ai_model, core); OpenAI (ai_model, supporting); ElevenLabs (ai_model, core); Perceptron (ai_model, unclear); axe-core (framework, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:**  | fit: Won CloudForce 'Most Viral' prize; page text shows no CloudForce or Salesforce tool use, so the fit is not stated.
- **Repo:** public, commits 35 (before/in/after event: 0/35/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 49, writeup long, impact claims False
- **Notes:** Phone-app-style UI delivered in the browser via React Native Web; combines Anthropic Claude, OpenAI, ElevenLabs voice and Perceptron; accessibility testing with axe-core; larger gallery.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; n_screenshots; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/saykind) | [GitHub](https://github.com/pranay-ratan/saykind)

### SonoRocky  (DubHacks '26)

- **Prizes:** 3rd Place Perceptron: Perception [3rd]  (tier: sponsor_winner)
- **Pitch:** Phone-camera scene narration plus an ultrasonic cane attachment that turns obstacle distance into beeps, helping visually impaired people navigate.
- **Problem / user:** Mobility canes give limited information, and visually impaired people suffer frequent injuries from hazards and head-level obstacles. / blind and low-vision pedestrians
- **Domain / idea type:** accessibility + safety_security / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision; speech_or_voice; llm_chat
- **Stack:** langs Python; JavaScript; C; frontend HTML5; JavaScript; backend Python server; db ; hosting 
- **Tech/APIs:** Perceptron mk1.5 (ai_model, core, sponsor); ElevenLabs TTS (ai_model, core, sponsor); ESP8266 with ultrasonic sensor (hardware_part, core); Fusion 360 / Prusa MK4 printed housing (hardware_part, supporting)
- **Sponsor APIs:** Perceptron; ElevenLabs | fit: Used Perceptron's vision model for live frame descriptions and hazard alerts in an accessibility assistant.
- **Repo:** public, commits 17 (before/in/after event: 0/17/0), README thin
- **Demo/writeup:** video True, live none, screenshots 9, writeup long, impact claims True (Cites a study: 7% of respondents had non-superficial injuries monthly and 13% head-level injuries; claims hardware under $15.)
- **Notes:** Perceptron mk1.5 describes camera frames with under 2s latency, ElevenLabs streams speech; ESP8266 ultrasonic sensor on a 3D-printed cane clamp posts distances over WiFi; hardware under $15.
- **Team size:** 4 | **Confidence:** high | unverified: stack_database; stack_hosting; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/walk-safer) | [GitHub](https://github.com/tsengjohn44-lgtm/dh26-project)

### Starward  (DubHacks '26)

- **Prizes:** T-Mobile: 2nd Place [2nd]  (tier: sponsor_winner)
- **Pitch:** Hiking planner that estimates where satellite messaging will work along a trail, recommends check-in spots, and texts trip plans to an emergency contact.
- **Problem / user:** Hikers lose cell service in remote areas and do not know where satellite messaging would work or whether they need paid satellite service. / hikers and their emergency contacts
- **Domain / idea type:** safety_security + telecom_networking / data_or_analytics
- **Platforms / hardware / AI:** web; bot_or_chat / False / False
- **Stack:** langs Python; JavaScript; HTML; frontend HTML; JavaScript; Folium; backend Flask; Node.js; db ; hosting Render
- **Tech/APIs:** CelesTrak (data_source, core); Skyfield/SGP4 (other, core); OpenStreetMap (maps_geo, core); Folium (maps_geo, core); Photon Spectrum (telecom, supporting, sponsor); T-Mobile T-Satellite (telecom, supporting, sponsor); Cursor (other, token); Claude Code (other, token)
- **Sponsor APIs:** Photon | fit: Recommendation engine compares phone, carrier and satellite plans including T-Mobile T-Satellite; Photon carries trip sharing and check-ins.
- **Repo:** public, commits 16 (before/in/after event: 0/16/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup long, impact claims False
- **Notes:** Coverage is an estimate from orbit calculations plus terrain; recommendation engine can advise buying nothing; Photon check-in bridge built in Node alongside a Flask app.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ai_used
- **Links:** [Devpost](https://devpost.com/software/starward) | [GitHub](https://github.com/eva032/Starward)

### Tenant  (DubHacks '26)

- **Prizes:** Photon: Track Winner [unknown]  (tier: sponsor_winner)
- **Pitch:** Scan a QR in a room to get a ten-minute chat-controlled lease on nearby devices (phone flashlight, laptop music and voice), via web or iMessage.
- **Problem / user:** Shared spaces like hospital rooms and hotels have controllable devices that guests are not allowed to operate, forcing awkward workarounds. / guests and hosts in shared rooms (hospital, hotel)
- **Domain / idea type:** ai_agents_infra + accessibility / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / True / llm_chat; agent_or_tool_use
- **Stack:** langs Python; JavaScript; AppleScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend FastAPI; WebSockets; db ; hosting 
- **Tech/APIs:** Photon 2.0 iMessage (telecom, core, sponsor); OpenAI Codex (ai_model, core); FastAPI (framework, core); WebSockets (framework, core); AppleScript (other, supporting)
- **Sponsor APIs:** Photon | fit: Used Photon 2.0 to give the room a real phone number and carry iMessage conversations to the agent.
- **Repo:** public, commits 52 (before/in/after event: 0/51/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Access is a time-limited lease checked at each command with version stamps so stale commands are refused; host reset rotates the room code; devices are plain web pages plus AppleScript.
- **Team size:** 2 | **Confidence:** high | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/tenant-lpy96k) | [GitHub](https://github.com/owen-tsao/tenant)

### tensormew  (DubHacks '26)

- **Prizes:** Winner Chef's Kitchen: 1st Place [1st]  (tier: track_winner)
- **Pitch:** Reinforcement-learning agent plays Pokemon Crystal to the first gym badge, calling an LLM only for stuck or hard moments.
- **Problem / user:** Calling an LLM on every game frame is slow and costly; most steps are mechanical and need no language reasoning. / AI/RL researchers and game-agent builders
- **Domain / idea type:** ai_agents_infra + entertainment_games / automation_or_agent
- **Platforms / hardware / AI:** desktop; cli / False / agent_or_tool_use; vision; llm_chat; predictive_ml
- **Stack:** langs Python; frontend Streamlit; backend PyBoy; Gymnasium; Pydantic; db SQLite; hosting 
- **Tech/APIs:** PyBoy (framework, core); PyTorch (framework, core); PPO (NumPy/PyTorch) (framework, core); Gemini tool calling (ai_model, core); Gymnasium (framework, supporting); Streamlit (framework, supporting); SQLite (database, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 134 (before/in/after event: 0/130/4), README solid
- **Demo/writeup:** video True, live none, screenshots 15, writeup long, impact claims False
- **Notes:** 13.2M-parameter vision plus RAM GRU policy in PyBoy; Gemini tool calls only on triggers with logged reasons and dollar cost; reward shaped on story event flags; 34 test modules.
- **Team size:** 4 | **Confidence:** high | unverified: sponsor_apis_used; is_sponsor_flags; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/tensor-mew) | [GitHub](https://github.com/AvinashD24/tensormew)

### Tool Distill  (DubHacks '26)

- **Prizes:** Winner Cook Smarter: 1st Place [1st]  (tier: track_winner)
- **Pitch:** Python library and Claude Code plugin that records agent tool calls and turns expensive successful runs into verified single-call tools.
- **Problem / user:** Agents rediscover the same long tool-call sequences every run, wasting tokens and time, and generated tools are hard to trust. / developers running AI agents in production
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** cli; other / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; frontend ; backend Typer; MCP SDK; db SQLite; hosting PyPI
- **Tech/APIs:** Anthropic SDK / Claude (ai_model, core); Claude Code plugin and hooks (framework, core); MCP SDK (framework, core); SQLite (WAL) (database, supporting); pytest (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 34 (before/in/after event: 0/34/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 0, writeup long, impact claims True (Demo claim of a 20-30 call discovery run reduced to one distilled call with four inside; business-model reasoning without market numbers.)
- **Notes:** Published to PyPI (0.1.0) and installable as Claude Code plugin; proposals pass AST static, replay and efficiency checks with a draft-to-deprecated lifecycle; 338 offline tests.
- **Team size:** 2 | **Confidence:** high | unverified: sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/tool-distill) | [GitHub](https://github.com/irtaza-kashif/tool-distill/tree/main)


## DubHacks 2025

### Artemis  (DubHacks 2025)

- **Prizes:** GROW - The Advocate [unknown]  (tier: sponsor_winner)
- **Pitch:** Focus system that tracks gaze and cognitive state and automatically tunes the workspace, including Chrome tabs, music and smart lighting.
- **Problem / user:** People with ADHD and focus problems get pulled into distraction when coding or studying. / people with ADHD and focus difficulty
- **Domain / idea type:** health_wellness + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** desktop; hardware / True / vision; llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; Python; JavaScript; frontend Electron; React; backend Node.js; Express.js; db ; hosting 
- **Tech/APIs:** MediaPipe (ai_model, core); Gemini (ai_model, supporting); Spotify API (other, supporting); Wiz local control API (hardware_part, supporting); Raspberry Pi (hardware_part, supporting); Chrome DevTools Protocol (other, core)
- **Sponsor APIs:**  | fit: Won the GROW Advocate prize; the project targets an ADHD focus-support advocacy theme, and the exact prize criteria are not shown on the page.
- **Repo:** public, commits 40 (before/in/after event: 0/37/3), README detailed
- **Demo/writeup:** video True, live none, screenshots 25, writeup long, impact claims False
- **Notes:** Eye tracking via MediaPipe with Python-to-Node JSON-RPC bridge, Chrome DevTools Protocol tab control, Spotify and Wiz smart-light control, and a Raspberry Pi component.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; prizes.placement; sponsor_fit_note criteria
- **Links:** [Devpost](https://devpost.com/software/artemis-kxd36i) | [GitHub](https://github.com/tgondil/artemis)

### BloomSync AI; CRISPR Apples; Mango  (DubHacks 2025)

- **Prizes:** Okanagan - Hack the Farm of the Future [unknown]  (tier: sponsor_winner)
- **Pitch:** BloomSync AI pipeline aggregates apple genomic data and uses reinforcement learning to propose edits to flowering genes so apples fruit on new wood.
- **Problem / user:** Apple trees fruit on old wood, which makes uniform fruiting and robotic harvesting difficult. / orchard growers and plant breeders
- **Domain / idea type:** sustainability_climate + food_nutrition / data_or_analytics
- **Platforms / hardware / AI:** other / False / predictive_ml
- **Stack:** langs Python; frontend ; backend ; db ; hosting AWS
- **Tech/APIs:** AWS (cloud, supporting); NCBI/UniProt/GDR genomic data (data_source, core); Reinforcement learning (ai_model, core)
- **Sponsor APIs:**  | fit: Targeted the Okanagan Hack the Farm of the Future challenge by using bioinformatics and RL to redesign apple flowering for robotic harvesting.
- **Repo:** public, commits 18 (before/in/after event: 0/15/3), README solid
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Queue entry merges three team projects (BloomSync AI, CRISPR Apples, Mango) sharing one prize; only BloomSync AI page was read. Uses NCBI, UniProt and GDR genomic data.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; prizes.placement; merged_entry_only_first_project_read; writeup_sections; writeup_length
- **Links:** [Devpost](https://devpost.com/software/bloomsync-ai ; https://devpost.com/software/crispr-apples ; https://devpost.com/software/mango-1u6a7x) | [GitHub](https://github.com/ericyuxuanye/dubhacks25)

### CareLens; Roam  (DubHacks 2025)

- **Prizes:** T-Mobile: 5G Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Offline multi-agent fall detection on a Raspberry Pi that watches via camera and alerts without requiring the user to press a button.
- **Problem / user:** Wearable-button fall detectors fail when elderly users are unconscious during an emergency. / elderly people living alone and caregivers
- **Domain / idea type:** health_wellness + telecom_networking / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision; agent_or_tool_use
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Raspberry Pi (hardware_part, core); OpenCV (framework, core)
- **Sponsor APIs:**  | fit: Entered for the T-Mobile 5G Challenge; the CareLens page runs offline and mentions no T-Mobile or 5G tooling, so the fit of Roam is unread.
- **Repo:** public, commits 3 (before/in/after event: 0/3/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 7, writeup short, impact claims False
- **Notes:** Queue entry merges CareLens and Roam under one T-Mobile 5G Challenge prize; only CareLens page was read. Runs fully offline on edge hardware with OpenCV.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; prizes.placement; merged_entry_only_first_project_read; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/carelens-edy2b8 ; https://devpost.com/software/roam-7h8vbm) | [GitHub](https://github.com/jeanchoe/hackaques)

### Chameleon  (DubHacks 2025)

- **Prizes:** DubHacks NEXT [unknown]  (tier: track_winner)
- **Pitch:** Chrome extension that detects signs of limited motor control or reading difficulty and adapts web pages, such as enlarging buttons, using Gemini.
- **Problem / user:** Users with ADHD, dyslexia or motor-control limits find standard web interfaces hard to use. / web users with ADHD, dyslexia or motor-control difficulties
- **Domain / idea type:** accessibility + education / social_good
- **Platforms / hardware / AI:** browser_extension / False / llm_chat
- **Stack:** langs JavaScript; TypeScript; Python; frontend React; Chrome Extension; backend Python; db ; hosting 
- **Tech/APIs:** Gemini 2.5 Flash API (ai_model, core); Statsig (other, unclear, sponsor); React (framework, supporting); Chrome extension APIs (framework, core)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Detects repeated missed clicks to enlarge interactive elements; Gemini 2.5 Flash adapts the UI; Statsig is listed among built-with tools.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots; placement_tier; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/robyn-6i4v2u) | [GitHub](https://github.com/AjitMallav/bridgeui-hub)

### ClearVision  (DubHacks 2025)

- **Prizes:** Best Freshman Beginner's Project [unknown]  (tier: track_winner)
- **Pitch:** Haptic wristband that helps visually impaired users navigate by feeding depth-camera and AI vision output into vibration cues.
- **Problem / user:** Visually impaired people need intuitive, safe navigation help beyond canes and audio-only guidance. / visually impaired individuals
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision
- **Stack:** langs Python; frontend ; backend Ubuntu; db ; hosting 
- **Tech/APIs:** Intel RealSense (hardware_part, core); Gemini (ai_model, core); Haptic wristband (hardware_part, core); Python (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 17 (before/in/after event: 0/16/1), README thin
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Combines an Intel RealSense depth camera, Gemini vision, and a wearable haptic wristband; runs on Ubuntu; hardware and software built by subteams.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; placement_tier
- **Links:** [Devpost](https://devpost.com/software/clearvision) | [GitHub](https://github.com/aditya0shah/clearVision)

### CodeGraph  (DubHacks 2025)

- **Prizes:** Atlassian: Best Use of Forge Agents [unknown]  (tier: sponsor_winner)
- **Pitch:** Forge app that uses LLMs to turn a codebase into an interactive directed-acyclic-graph map of structure, dependencies and impact.
- **Problem / user:** Student developers inheriting unfamiliar codebases spend hours finding files and understanding logic when onboarding. / student developers and teams inheriting codebases
- **Domain / idea type:** dev_tools + education / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs JavaScript; frontend React; backend Node.js; Forge; db ; hosting Atlassian Forge
- **Tech/APIs:** Atlassian Forge (framework, core, sponsor); Gemini API (ai_model, core); GitHub API (data_source, core); React (framework, supporting)
- **Sponsor APIs:** Atlassian Forge | fit: Built the codebase-mapping tool as a Forge app, targeting the Atlassian Best Use of Forge Agents prize; the page does not describe agent use in detail.
- **Repo:** public, commits 19 (before/in/after event: 0/19/0), README thin
- **Demo/writeup:** video False, live none, screenshots 10, writeup medium, impact claims False
- **Notes:** Runs on Atlassian Forge with Gemini API and GitHub API; page has a pitch story but no standard headed sections; Loom demo and Jira app link listed; queue url was truncated.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; edition_blob_queue_split; writeup_sections; writeup_length; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/directedacycliccodebase) | [GitHub](https://github.com/CosmicOdyssey/DubHacks-2025/)

### DubOps; Wellify.AI; Bond - Find Your Own Community  (DubHacks 2025)

- **Prizes:** Best Use of AI by AWS [unknown]  (tier: sponsor_winner)
- **Pitch:** DubOps analyzes a codebase with LLMs, then generates and runs the steps to deploy the app automatically.
- **Problem / user:** Writing apps is easier with generative AI, but deploying them is still hard for programmers. / developers deploying web apps
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend Next.js; backend Flask; db ; hosting AWS
- **Tech/APIs:** AWS Bedrock (ai_model, core, sponsor); AWS (cloud, supporting, sponsor); Flask (framework, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** AWS Bedrock | fit: DubOps used AWS Bedrock as its gateway to large language models, matching the Best Use of AI by AWS prize.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims False
- **Notes:** Queue entry merges DubOps, Wellify.AI and Bond under one AWS prize; only DubOps page was read. Three-step analyze, plan, deploy flow using AWS Bedrock as the LLM gateway.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; prizes.placement; merged_entry_only_first_project_read; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/dubops ; https://devpost.com/software/wellify-ai ; https://devpost.com/software/bond-xuhodw) | [GitHub](https://github.com/Hudica/DubOps)

### glimpse  (DubHacks 2025)

- **Prizes:** Statsig Hackathon Challenge: AI That Learns What Works [unknown]  (tier: sponsor_winner)
- **Pitch:** Agentic photo editor that adds predictive AI suggestions on top of a simple editing tool, helping photographers learn what edits work.
- **Problem / user:** Beginner photographers find it hard to know which edits improve an image. / amateur photographers
- **Domain / idea type:** creative_media + education / creative_tool
- **Platforms / hardware / AI:** web / False / vision; agent_or_tool_use; llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; backend FastAPI; Ollama; db ; hosting 
- **Tech/APIs:** Statsig (other, unclear, sponsor); Gemini (ai_model, core); Gemma 2 via Ollama (ai_model, core); Next.js (framework, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** Statsig | fit: Targeted Statsig's 'AI That Learns What Works' challenge with predictive AI editing suggestions; Statsig is listed in built-with but its use is not described in the visible text.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 10, writeup medium, impact claims False
- **Notes:** Uses local Gemma2 via Ollama alongside Gemini; Statsig listed in built-with; FastAPI backend with Next.js frontend; repo name says DUBHACKS-2026.
- **Team size:** 2 | **Confidence:** medium | unverified: ui_polish; n_screenshots; sponsor_fit_note; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/glimpse-sd9p2y) | [GitHub](https://github.com/chetan-cloud/DUBHACKS-2026)

### Math Sandbox  (DubHacks 2025)

- **Prizes:** INVENT - The Innovator [unknown]  (tier: track_winner)
- **Pitch:** Projector-and-camera table where handwritten equations on paper are read by Gemini and graphed live onto the surface.
- **Problem / user:** Exploring math functions is usually screen-bound; the team wanted a physical, Dynamicland-style interface. / students and math learners
- **Domain / idea type:** education + creative_media / hardware_gadget
- **Platforms / hardware / AI:** hardware; desktop / True / vision
- **Stack:** langs Python; frontend ; backend OpenCV; SymPy; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, core); OpenCV (framework, core); SymPy (framework, core); Projector and camera (hardware_part, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 124 (before/in/after event: 0/123/1), README thin
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** OpenCV aligns projector output with camera input; Gemini parses handwriting; SymPy evaluates the functions; physical projector setup in the demo.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; placement_tier
- **Links:** [Devpost](https://devpost.com/software/interactive-grapher-thingy) | [GitHub](https://github.com/lukasmwerner/desmos-in-the-world)

### Minty: Digital Tooth Fairy  (DubHacks 2025)

- **Prizes:** VISA - Play, Pay, Repeat: Reinventing Childhood Joy... [unknown]  (tier: sponsor_winner)
- **Pitch:** Gamified toothbrushing app where camera-verified brushing raises the virtual value of a child's teeth, tied to payment-style rewards.
- **Problem / user:** Parents struggle to motivate kids to brush, and tooth-fairy rewards do not encourage daily habits. / children and parents
- **Domain / idea type:** health_wellness + fintech_finance / entertainment_or_game
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs TypeScript; frontend Next.js; Tailwind; backend Prisma; db PostgreSQL; hosting Vercel
- **Tech/APIs:** Gemini (ai_model, core); Stripe (payments, supporting); Prisma + PostgreSQL (database, core); Figma (other, supporting); Next.js (framework, core)
- **Sponsor APIs:**  | fit: Targeted Visa's 'Play, Pay, Repeat' childhood-joy challenge with a rewards-based brushing game; the page lists Stripe, not Visa products.
- **Repo:** public, commits 33 (before/in/after event: 0/33/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 19, writeup medium, impact claims False
- **Notes:** Real-time AI verification of brushing via camera using Gemini; custom assets made with AI generation and digital art; Stripe in stack; Visa challenge framing.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/minty-4vcu9m) | [GitHub](https://github.com/owenkrause/tfp)

### NeuroMapping: Low-Cost Cognitive Safety System  (DubHacks 2025)

- **Prizes:** Prizes in Kind [unknown]  (tier: sponsor_winner)
- **Pitch:** Software-only system that turns simulated EEG signals into cognitive-risk heatmaps using a CNN and Transformer ensemble, with a community awareness dashboard.
- **Problem / user:** Cognitive risk assessment and mental health awareness are hard to access cheaply worldwide. / general public and mental health awareness groups
- **Domain / idea type:** mental_health + health_wellness / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; frontend Streamlit; Dash; Plotly; backend PyTorch; TensorFlow; db Firebase; PostgreSQL; SQLite; hosting Google Cloud
- **Tech/APIs:** PyTorch (framework, core); TensorFlow (framework, supporting); OpenAI (ai_model, unclear); Streamlit (framework, supporting); Firebase (database, supporting); Google Cloud (cloud, unclear)
- **Sponsor APIs:**  | fit: Prize was Prizes in Kind (no specific sponsor challenge); the page names no sponsor tool.
- **Repo:** public, commits 31 (before/in/after event: 25/6/0), README none
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup long, impact claims False
- **Notes:** Works on simulated EEG data only; page links Figma, Netlify and Canva sites alongside the repo and runs a very long, emoji-heavy writeup.
- **Team size:** 1 | **Confidence:** medium | unverified: ui_polish; prizes.placement; writeup_sections; has_impact_claims
- **Links:** [Devpost](https://devpost.com/software/neuromapping-low-cost-cognitive-safety-system) | [GitHub](https://github.com/senushidinara/NeuroMapping)

### Optivise  (DubHacks 2025)

- **Prizes:** DubHacks NEXT [unknown]  (tier: track_winner)
- **Pitch:** Experimentation tool that makes A/B testing scalable for small teams, using Statsig and Gemini.
- **Problem / user:** Most companies barely run experiments compared with Google-scale testing, so teams miss learning from user behavior. / small product teams
- **Domain / idea type:** dev_tools + productivity_workplace / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs TypeScript; CSS; frontend Next.js; React; Tailwind CSS; backend ; db ; hosting 
- **Tech/APIs:** Statsig (other, core); Gemini (ai_model, supporting); Next.js (framework, supporting)
- **Sponsor APIs:**  | fit: Won DubHacks NEXT, an event-run award; page does not describe a sponsor challenge.
- **Repo:** public, commits 45 (before/in/after event: 0/45/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup short, impact claims False
- **Notes:** Very short writeup (inspiration only plus Built With); Statsig feature-flag and experiment platform paired with Gemini.
- **Team size:** 2 | **Confidence:** medium | unverified: ui_polish; prizes.placement; placement_tier; what_it_does
- **Links:** [Devpost](https://devpost.com/software/optivise-6ag1nm) | [GitHub](https://github.com/williamdinhh/Optivise)

### Spendify  (DubHacks 2025)

- **Prizes:** Atlassian: Best Use of Forge Agents [unknown]  (tier: sponsor_winner)
- **Pitch:** Student expense-tracking app built as a Forge app on Atlassian Jira, with a custom dashboard and Rovo AI help.
- **Problem / user:** College freshmen suddenly manage their own money without a clear picture of where it goes. / college students
- **Domain / idea type:** fintech_finance + education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / agent_or_tool_use
- **Stack:** langs JavaScript; frontend HTML; CSS; JSX; backend Forge; db ; hosting Atlassian Forge
- **Tech/APIs:** Atlassian Forge (framework, core, sponsor); Jira (other, core, sponsor); Rovo (ai_model, supporting, sponsor)
- **Sponsor APIs:** Atlassian Forge; Jira; Rovo | fit: Built the whole app as a Forge app on Jira with Rovo, targeting the Atlassian Best Use of Forge Agents prize.
- **Repo:** public, commits 8 (before/in/after event: 0/8/0), README solid
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Runs inside Jira via Atlassian Forge with a custom UI; Rovo listed; second demo link on Loom; bundled queue entry (split from three projects).
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; ai_types
- **Links:** [Devpost](https://devpost.com/software/spendify) | [GitHub](https://github.com/s-prshah/spendify-atlassian)

### TaskFlow  (DubHacks 2025)

- **Prizes:** Atlassian: Best Use of Forge Agents [unknown]  (tier: sponsor_winner)
- **Pitch:** Chrome extension that screenshots Canvas assignment pages and uses Rovo agents via a Forge backend to create labeled Jira tasks automatically.
- **Problem / user:** Manually copying assignments into task managers is tedious for students. / college students
- **Domain / idea type:** productivity_workplace + education / automation_or_agent
- **Platforms / hardware / AI:** browser_extension; web / False / agent_or_tool_use; vision
- **Stack:** langs JavaScript; frontend Chrome extension; backend Forge; db ; hosting Atlassian Forge
- **Tech/APIs:** Atlassian Forge (framework, core, sponsor); Rovo agents (ai_model, core, sponsor); Jira (other, core, sponsor); Chrome extension (framework, core)
- **Sponsor APIs:** Atlassian Forge; Rovo; Jira | fit: Used Rovo agents on a Forge backend to read Canvas screenshots and create Jira tasks, targeting the Atlassian Forge Agents prize.
- **Repo:** public, commits 1 (before/in/after event: 0/1/0), README none
- **Demo/writeup:** video True, live none, screenshots 1, writeup short, impact claims False
- **Notes:** Four repos linked (Forge agent, Chrome extension, image-processing server, Jira task adder); Rovo agents parse screenshots; bundled queue entry (split from three projects).
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split
- **Links:** [Devpost](https://devpost.com/software/taskflow-qv6z7m) | [GitHub](https://github.com/Achintya72/task-flow-agent)
