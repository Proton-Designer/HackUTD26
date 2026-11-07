# TreeHacks: project cards (26 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## TreeHacks 2025

### BAS Climate Action Matcher  (TreeHacks 2025)

- **Prizes:** Winner Sustainability Prize: Best prototyping process ($800 Cash) [unknown]; Winner Intersystems: Best Use of GenAI using InterSystems IRIS Vector Search ($2k 1st / $1.5k 2nd / $1k 3rd) [unknown]  (tier: track_winner)
- **Pitch:** Agentic tool that matches a company to relevant climate initiatives and peer actions using RAG over sustainability reports, UN cooperative initiatives and scraped trackers.
- **Problem / user:** Companies struggle to find concrete actions and partnerships to reduce their carbon footprint. / corporate sustainability teams
- **Domain / idea type:** sustainability_climate + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; rag_or_search; llm_chat
- **Stack:** langs JavaScript; TypeScript; Python; HTML; Jupyter; frontend ; backend LangChain; DAIN Butterfly; db InterSystems IRIS; hosting 
- **Tech/APIs:** InterSystems IRIS Vector Search (database, core, sponsor); DAIN Butterfly (framework, core, sponsor); Gemini (ai_model, supporting); NVIDIA Llama (ai_model, supporting, sponsor); LangChain (framework, supporting)
- **Sponsor APIs:** InterSystems IRIS Vector Search; DAIN | fit: Targeted the InterSystems GenAI prize by using IRIS vector search for RAG over a custom database of company sustainability reports.
- **Repo:** public, commits 32 (before/in/after event: 0/27/5), README detailed
- **Demo/writeup:** video True, live none, screenshots 19, writeup long, impact claims False
- **Notes:** Orchestrated by a DAIN Butterfly agent workflow with custom tools; vector search in InterSystems IRIS over hundreds of sustainability reports; scrapes Zero Tracker and NZDPU; also lists Gemini and NVIDIA Llama.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; stack_languages; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/bas-climate-action-matcher) | [GitHub](https://github.com/Suzehva/bas_labs)

### BlinkAI  (TreeHacks 2025)

- **Prizes:** Winner Best Beginner Hack (Keychron K8 Pro keyboard per team member) [unknown]  (tier: track_winner)
- **Pitch:** Webcam system that reads intentional blinks as Morse code, converts them to text and sends it to an AI assistant for a reply.
- **Problem / user:** People with Parkinson's, ALS or other mobility limits find voice or typing interfaces to assistants hard to use. / people with mobility impairments
- **Domain / idea type:** accessibility + health_wellness / new_category
- **Platforms / hardware / AI:** web / False / vision; llm_chat
- **Stack:** langs Python; HTML; CSS; frontend React; backend Flask; db ; hosting 
- **Tech/APIs:** MediaPipe (framework, core); OpenCV (framework, core); Flask (framework, supporting); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 14 (before/in/after event: 0/11/3), README thin
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Blink-duration filtering separates deliberate blinks from natural ones using MediaPipe and OpenCV; Morse decoded to text and forwarded to an LLM assistant; only one screenshot.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/blinkai) | [GitHub](https://github.com/FuzionEcho/BlinkAI)

### BrailleBot: Make Every Document Accessible!  (TreeHacks 2025)

- **Prizes:** Winner Best Hardware Hack [unknown]  (tier: track_winner)
- **Pitch:** Braille printer made by adding a sub-$15 spring-loaded embossing head to a cheap 3D printer, with AI turning documents and image descriptions into braille G-code.
- **Problem / user:** Braille printers cost around $1500 and most web content lacks image descriptions, leaving visually impaired people with scarce accessible materials. / visually impaired students and teachers
- **Domain / idea type:** accessibility + education / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; vision
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Chakra UI; backend Flask; db ; hosting Vercel
- **Tech/APIs:** Groq (Llama 3 8B / 11B Vision) (ai_model, core); Zoom API (other, supporting); 3D printer with Marlin firmware (hardware_part, core); Custom 3D-printed embossing mechanism (hardware_part, core); Flask (framework, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 153 (before/in/after event: 0/149/4), README solid
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims True (Claims about 100x cheaper than existing braille printers, embosser under $15 versus $1500, and 3% of the internet being accessible.)
- **Notes:** Snap-action punch driven by the printer's extruder motor, tuned with adjustable spring and cork backing; Flask converts text to braille G-code for Marlin over USB serial; live canvas preview.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; is_sponsor
- **Links:** [Devpost](https://devpost.com/software/readable-ai-braille-printer) | [GitHub](https://github.com/cathyzbn/braille-printer)

### ECGo  (TreeHacks 2025)

- **Prizes:** Winner Web3 Prize: Most Crazy Idea ($7k Cash + 7k EIGEN) [unknown]  (tier: sponsor_winner)
- **Pitch:** Portable low-cost ECG device that records a three-second heartbeat sample, uploads it, and gets an AI arrhythmia diagnosis viewable by sample ID in a web app.
- **Problem / user:** Portable ECG machines are scarce in developing regions and crisis zones. / clinicians and patients in under-resourced regions
- **Domain / idea type:** health_wellness + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / predictive_ml
- **Stack:** langs C; Python; frontend Streamlit; backend Python; PyTorch; db InfluxDB; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); AD8232 ECG IC (hardware_part, core); PyTorch (framework, core); InfluxDB (database, supporting); Opacity (other, unclear, sponsor); Streamlit (framework, supporting)
- **Sponsor APIs:** Opacity | fit: Entered for the Web3 Prize (Most Crazy Idea); the page lists Opacity in the stack but the excerpt read does not show how it was used.
- **Repo:** public, commits 29 (before/in/after event: 2/26/1), README solid
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** ESP32 reads an AD8232 ECG front end, shows the waveform on two I2C OLEDs with a joystick pan/zoom, runs on AA batteries; PyTorch model; Opacity and InfluxDB listed in stack.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; sponsor_apis_used; sponsor_fit_note; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/ecgo) | [GitHub](https://github.com/fightingj305/ecgo)

### Edith  (TreeHacks 2025)

- **Prizes:** Winner Most Technically Complex Hack [unknown]  (tier: track_winner)
- **Pitch:** Raspberry Pi smart glasses that stream camera video to GPU servers for depth and 3D segmentation, then guide blind users to objects with Gemini and haptic feedback.
- **Problem / user:** Visually impaired people need real-time spatial awareness and object location that standard vision models and handheld devices do not give. / blind and visually impaired people
- **Domain / idea type:** accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Tailwind CSS; backend PyTorch; NumPy; db ; hosting NVIDIA A100 server
- **Tech/APIs:** Raspberry Pi Zero 2W (hardware_part, core); Gemini multimodal live API (ai_model, core); PyTorch depth/segmentation models on 4x A100 (ai_model, core); IMU and haptic vibration motors (hardware_part, core); Adafruit parts (hardware_part, supporting); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 1, writeup long, impact claims False
- **Notes:** Inference parallelized across four NVIDIA A100s for depth maps, segmentation and point clouds; Gemini multimodal API locates objects; IMU-driven vibration motors with decaying amplitude; fall detection; custom perfboard circuits and brass-reinforced 3D-printed frame.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; is_sponsor; n_screenshots; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/edith-bvh014) | [GitHub](https://github.com/jotalis/Edith)

### ERWIN: Enhanced Rock Weathering Impact Navigator  (TreeHacks 2025)

- **Prizes:** Sustainability Prize: Best solves the user's pain point of a provided challenge ($800 Cash) [unknown]  (tier: track_winner)
- **Pitch:** Map-based web tool that forecasts CO2 removal from enhanced rock weathering by fetching soil and climate data, running a geochemical model and charting uncertainty, plus quarry suggestions.
- **Problem / user:** Forecasting carbon removal for rock-weathering projects needs PhD-level knowledge and poorly documented Fortran-based models, leaving investors and planners with very uncertain estimates. / carbon credit investors and ERW researchers
- **Domain / idea type:** sustainability_climate + fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; JavaScript; frontend JavaScript; Mapbox; backend Flask; Docker; Qiskit; CrunchFlow; db ; hosting Docker
- **Tech/APIs:** CrunchFlow (framework, core); Qiskit / IBM Quantum Cloud (cloud, supporting); SoilGrids API (data_source, core); Open-Meteo API (data_source, core); Mapbox API (maps_geo, supporting); Selenium + BeautifulSoup (framework, supporting); Docker (framework, supporting)
- **Sponsor APIs:**  | fit: Targeted the Carbon Removal Assessment challenge by building a user-friendly forecasting interface around an ERW geochemistry model, informed by a Stanford professor's input.
- **Repo:** public, commits 73 (before/in/after event: 0/67/6), README none
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Wraps the CrunchFlow geochemistry model behind a Basic/Advanced UI; Qiskit sampling that can run on IBM Quantum Cloud; quarry data scraped from the National Mine Map Repository; Dockerized; built by a first-hackathon team.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; is_sponsor; placement_tier
- **Links:** [Devpost](https://devpost.com/software/erwin-enhanced-rock-weathering-impact-navigator) | [GitHub](https://github.com/Jackal-Studios/rock-thing)

### HawkWatch  (TreeHacks 2025)

- **Prizes:** Winner TreeHacks Grand Prize | 1st Place ($11k Cash) [1st]  (tier: overall_top3)
- **Pitch:** Browser-based surveillance platform that sends video, audio and body-pose data to Gemini to flag crime or medical emergencies and email alerts with timelines.
- **Problem / user:** Security cameras record everywhere but staff cannot watch many feeds, so incidents like fainting or shoplifting are missed. / security staff at stores, hospitals and malls
- **Domain / idea type:** safety_security + health_wellness / automation_or_agent
- **Platforms / hardware / AI:** web / False / vision; llm_chat; speech_or_voice
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind CSS; TensorFlow.js; Canvas API; backend Supabase; Resend; db Supabase; hosting 
- **Tech/APIs:** Google Gemini VLM (ai_model, core); TensorFlow.js (framework, core); OpenAI (ai_model, supporting); Supabase (database, supporting); Resend (other, supporting)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Combines TensorFlow.js pose data with Gemini VLM live analysis in the browser; includes MP4 upload analysis, incident timelines, CSV export and an OpenAI chat assistant fed event context.
- **Team size:** 5 | **Confidence:** medium | unverified: github_url; has_demo_video; ui_polish; n_screenshots; event dates from memory
- **Links:** [Devpost](security / computer vision)

### Hearti  (TreeHacks 2025)

- **Prizes:** Winner Most Impactful Hack (JBL Partybox 110 per team member) [unknown]  (tier: track_winner)
- **Pitch:** Turns cardiac MRI scans into an interactive 3D heart model and classifies congenital heart disease type and severity with a confidence score.
- **Problem / user:** Congenital heart disease patients need lifelong monitoring, and flat 2D scans are hard for patients and doctors to interpret. / cardiologists and congenital heart disease patients
- **Domain / idea type:** health_wellness + other / new_category
- **Platforms / hardware / AI:** web; other / False / vision; predictive_ml; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind; Plotly; backend FastAPI; PyTorch; NumPy; db Vespa; hosting Vercel
- **Tech/APIs:** PyTorch (framework, core); NVIDIA (cloud, unclear, sponsor); ElevenLabs (ai_model, supporting, sponsor); Luma AI (ai_model, unclear, sponsor); Vespa (database, unclear, sponsor); Meta Quest (hardware_part, supporting); Next.js (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 60 (before/in/after event: 0/60/0), README none
- **Demo/writeup:** video True, live not_checked, screenshots 19, writeup long, impact claims False
- **Notes:** Custom volume-shading algorithm maps MRI intensity onto segmented heart models; PyTorch classifier outputs category, severity and confidence; Meta Quest viewing and ElevenLabs voice listed in stack.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; platforms; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/hearti) | [GitHub](https://github.com/ethan-tam33/heartAI)

### HiveMind  (TreeHacks 2025)

- **Prizes:** Education Grand Prize [unknown]  (tier: track_winner)
- **Pitch:** Classifies students' understanding with AI quizzes, groups them into four-person learning hubs and matches stronger students with weaker ones, with a 3D brain progress view.
- **Problem / user:** Standardized teaching leaves students at different comprehension levels behind, and no structured way connects those who understand with those who struggle. / students and instructors in online courses
- **Domain / idea type:** education + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; predictive_ml; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend Next.js; Three.js; Streamlit; backend Flask; Python; db InterSystems IRIS Vector; ChromaDB; Supabase; Vespa; hosting 
- **Tech/APIs:** Perplexity Sonar API (ai_model, core, sponsor); InterSystems IRIS Vector database (database, core, sponsor); Google Gemini (ai_model, unclear); Zoom (other, supporting); Three.js (framework, supporting); ChromaDB (database, unclear); Vespa (database, unclear); Supabase (database, unclear)
- **Sponsor APIs:** Perplexity Sonar; InterSystems IRIS
- **Repo:** public, commits 14 (before/in/after event: 0/10/4), README detailed
- **Demo/writeup:** video None, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Four learning hubs of four students each via custom matching, vector embeddings for assessment, Zoom session monitored by an AI agent, Three.js 3D brain dashboard; team restarted the repo late after merge conflicts.
- **Team size:** 5 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; team_size; event dates from memory; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/hivemind-18cula) | [GitHub](https://github.com/rajashekarcs2023/HiveMind)

### Iris  (TreeHacks 2025)

- **Prizes:** Winner Edge AI Prize: Most Creative On-Device AI Deployment ($10k Cash) [unknown]  (tier: track_winner)
- **Pitch:** 3D-printed headset holding an iPhone camera that runs on-device vision models to detect hazards for blind users and gives haptic buzzes plus spoken directions.
- **Problem / user:** Blind and visually impaired people face hazards such as head-height obstacles, potholes and street crossings. / blind and visually impaired people
- **Domain / idea type:** accessibility + safety_security / hardware_gadget
- **Platforms / hardware / AI:** mobile_ios; hardware / True / vision; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; frontend Expo; backend PyTorch; CUDA; db ; hosting 
- **Tech/APIs:** PyTorch (framework, core); CUDA / NVIDIA (hardware_part, supporting, sponsor); Groq (ai_model, supporting, sponsor); Expo (framework, core); 3D-printed headset (hardware_part, core)
- **Sponsor APIs:**  | fit: Targeted the Edge AI Prize by running hazard-detection vision models on-device with sub-100 ms claimed latency; sponsor product use not detailed beyond NVIDIA and Groq tags.
- **Repo:** public, commits 30 (before/in/after event: 0/29/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 10, writeup long, impact claims True (Cites a survey that about 40% of 300 blind people have a head-height collision at least yearly; claims under 100 ms detection.)
- **Notes:** Runs captioning, classification, segmentation and depth-estimation models as agent specialists, claims hazard detection in under 100 ms; Expo mobile app, CUDA/PyTorch, Groq and NVIDIA in stack.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; platforms; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/iris-vlnzp0) | [GitHub](https://github.com/RoyceAroc/iris)

### Lemon  (TreeHacks 2025)

- **Prizes:** Sustainability Prize: Best incorporation of broader context to enhance venture viability ($800 Cash) [unknown]  (tier: track_winner)
- **Pitch:** Mobile marketplace where farmers list surplus or imperfect produce at a discount for consumers and businesses, with bulk requests and local advertising.
- **Problem / user:** Large amounts of edible produce are discarded for looking imperfect while consumers and businesses want cheaper, sustainable food. / farmers, shoppers and local businesses
- **Domain / idea type:** sustainability_climate + food_nutrition / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross; web / False / False
- **Stack:** langs Dart; frontend Flutter; FlutterFlow; backend Supabase; db Supabase PostgreSQL; hosting FlutterFlow
- **Tech/APIs:** FlutterFlow (framework, core); Supabase (database, core); Flutter (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 8 (before/in/after event: 0/8/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims True (Cites 60 million tons of US produce wasted yearly, over 50% discarded, and 1.2 billion tonnes discarded globally.)
- **Notes:** Built in FlutterFlow with Supabase/PostgreSQL by a first-hackathon pair using sponsored FlutterFlow access; page is explicitly mobile-view only; writeup covers market, regulation and stakeholder incentives.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; is_sponsor
- **Links:** [Devpost](https://devpost.com/software/lemon-7gn5hq) | [GitHub](https://github.com/twosodium/lemon)

### MediLedger  (TreeHacks 2025)

- **Prizes:** Winner Web3 Prize: Best AI Agents ($8k Cash + 8k EIGEN [1st] & $7k Cash + 7k EIGEN [2nd]) [unknown]  (tier: sponsor_winner)
- **Pitch:** Hospitals publish Merkle roots of their drug inventory to EigenDA so an agent can verify a neighbor has a drug in stock without revealing full inventories.
- **Problem / user:** Hospital drug stockouts persist because hospitals will not share full inventories with competitors and checking stock means manual phone calls. / hospital pharmacy and supply staff
- **Domain / idea type:** health_wellness + ai_agents_infra / new_category
- **Platforms / hardware / AI:** web / False / agent_or_tool_use
- **Stack:** langs TypeScript; frontend FlutterFlow; Next.js; backend Express.js; Node.js; SHA256; Merkle trees; db ; hosting 
- **Tech/APIs:** EigenDA (other, core, sponsor); EigenLayer agent framework (framework, supporting, sponsor); Merkle trees and proofs (other, core); FlutterFlow (framework, supporting); Express.js (framework, supporting)
- **Sponsor APIs:** EigenDA; EigenLayer | fit: Committed hospital inventory Merkle roots to EigenDA and used EigenLayer's agent framework for verifiable AI and data availability logging.
- **Repo:** public, commits 14 (before/in/after event: 0/13/1), README solid
- **Demo/writeup:** video None, live not_checked, screenshots 2, writeup long, impact claims False
- **Notes:** Inventory stored as Merkle tree with only the root committed to EigenDA; proof verification runs off-chain in the backend; UI built in FlutterFlow with a Next.js proof of concept. Mostly first-time hackers.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ui_polish; live_demo_url; is_sponsor flags; event dates from memory; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/mediledger) | [GitHub](https://github.com/shayaansultan/treehacks-final)

### OmNom  (TreeHacks 2025)

- **Prizes:** Winner Most Creative Hack (Pioneer DJ DDJ-FLX4 Pack per team member) [unknown]  (tier: track_winner)
- **Pitch:** Custom-built delivery robot with a lift that holds food on a rope the recipient must cut, ordered through a web app with routing and vision.
- **Problem / user:** The page does not state a problem; it focuses on building a from-scratch robot for food delivery with a playful hand-off. / people ordering food delivery
- **Domain / idea type:** food_nutrition + mobility_transport / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision
- **Stack:** langs Python; TypeScript; C++; frontend Next.js; React; Vite; Tailwind; backend FastAPI; OpenCV; WebSockets; db ; hosting Vercel
- **Tech/APIs:** NVIDIA Jetson Nano (hardware_part, core); Arduino (hardware_part, supporting); RoboClaw (hardware_part, core); OpenCV (framework, supporting); OpenAI API (ai_model, unclear); Google Maps Places API (maps_geo, supporting); OpenRouteService (maps_geo, supporting); DPT / ViT / CLIP (ai_model, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 70 (before/in/after event: 0/70/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 34, writeup long, impact claims False
- **Notes:** Robot built entirely from scratch: 22 laser-cut sheet-metal parts, 6 inch wheels, custom drivers instead of ROS, Jetson Nano, RoboClaw motor controllers; food hangs from a rope the user cuts.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; problem_statement; target_user; platforms
- **Links:** [Devpost](https://devpost.com/software/omnom-hg16v3) | [GitHub](https://github.com/NilsIrl/ActuallyAHuman/tree/main)

### PUSHPA  (TreeHacks 2025)

- **Prizes:** Winner Edge AI Prize: Operator Optimization Champion ($5k Cash) [unknown]  (tier: track_winner)
- **Pitch:** Firefighter support system pairing an autonomous drone, Meta glasses and an on-phone vision model with a LangChain agent, all designed to work without cloud connectivity.
- **Problem / user:** Firefighters in disaster zones often lack Wi-Fi or cellular service, so cloud AI is unavailable when they need hazard awareness. / firefighters and first responders
- **Domain / idea type:** safety_security + ai_agents_infra / hardware_gadget
- **Platforms / hardware / AI:** hardware; web; mobile_android / True / vision; agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; Python; C++; frontend Next.js; Socket.IO; backend Node.js; LangChain; PyTorch; llama.cpp; ExecuTorch; db ; hosting Vercel
- **Tech/APIs:** Custom PyTorch Winograd convolution kernel (framework, core); llama.cpp / ExecuTorch on-device VLM (ai_model, core); LangChain (framework, core); Gemini (synthetic data) (ai_model, supporting); Meta glasses and drone (MAVLink) (hardware_part, core); Vercel (cloud, supporting)
- **Sponsor APIs:**  | fit: Targeted the Edge AI track operator-optimization prize with a custom optimized convolution kernel and on-phone vision model running without cloud access.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims True (Cites US residential fire and wildfire statistics and claims a 20x inference speedup.)
- **Notes:** Custom hybrid direct/Winograd convolution kernel claimed to give 20x on-device speedup; MobileVLM on a Samsung Galaxy via llama.cpp; drone and glasses hacked without official SDKs; commands via WhatsApp or glasses.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; is_sponsor; placement_tier; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/pushpa-pyro-uav-system-for-high-risk-patrol-and-alerting) | [GitHub](https://github.com/chandrasuda/nextgen-firewatcher)

### SurviveX  (TreeHacks 2025)

- **Prizes:** Winner Edge AI Prize: Most Creative On-Device AI Deployment ($10k Cash) [unknown]  (tier: track_winner)
- **Pitch:** Offline survival assistant: a fine-tuned Llama 3.2 1B running on Apple Vision Pro via ExecuTorch gives hands-free spoken guidance, adapting to simulated vitals.
- **Problem / user:** People lost or injured in the wilderness or disasters have no internet to call for help or look up survival knowledge. / hikers, soldiers and disaster responders
- **Domain / idea type:** safety_security + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** other; mobile_ios / True / llm_chat; speech_or_voice
- **Stack:** langs Swift; Python; frontend SwiftUI; visionOS; backend ExecuTorch; PyTorch; torchtune; db ; hosting on-device
- **Tech/APIs:** ExecuTorch (framework, core); Llama-3.2-1B-Instruct (ai_model, core); torchtune LoRA (framework, core); NVIDIA Brev H100 (cloud, supporting); Terra API (data_source, supporting); Apple Vision Pro / SwiftUI (hardware_part, core); GPT-4 (data prep) (ai_model, supporting)
- **Sponsor APIs:**  | fit: Targeted the Edge AI track's on-device deployment prize by running a fine-tuned Llama 1B through ExecuTorch on Vision Pro, iPhone and iPad without internet.
- **Repo:** public, commits 23 (before/in/after event: 0/23/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims True (Opens with a statistic that 30% of people lost in the wilderness never find their way back.)
- **Notes:** Llama-3.2-1B LoRA fine-tuned with torchtune on a Brev H100 using GPT-4-prepared dialogues; ExecuTorch .pte binaries linked into SwiftUI visionOS app; vitals simulated through Terra API.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; is_sponsor; placement_tier
- **Links:** [Devpost](https://devpost.com/software/survivex) | [GitHub](https://github.com/rockuutree/SurviveX-Treehacks/tree/main)

### Therms - Thermoregulation Wearables with AI-powered Insights  (TreeHacks 2025)

- **Prizes:** Healthcare Grand Prize [unknown]; Scrapybara: Capy Prize [unknown]  (tier: track_winner)
- **Pitch:** Shoe-sole wearable using Peltier modules to heat or cool the feet, with a web app that blends wearable data, GPT insights and automated appointment booking.
- **Problem / user:** Existing palm or foot cooling setups need bulky liquid pumps; people with thermoregulation problems and athletes need a portable heating and cooling solution. / people with diabetes or spinal injuries, athletes, soldiers, elderly users
- **Domain / idea type:** health_wellness + productivity_workplace / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / llm_chat; agent_or_tool_use; predictive_ml
- **Stack:** langs JavaScript; frontend Next.js; Tailwind CSS; backend Node.js; Firebase; db Firebase; hosting 
- **Tech/APIs:** Peltier thermoelectric modules with motor controller and IMU (hardware_part, core); OpenAI ChatGPT (ai_model, core); Scrapybara (other, core, sponsor); Terra API (data_source, supporting, sponsor); Firebase (database, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** Scrapybara; Terra API; OpenAI | fit: Scrapybara computer-use agent automates booking appointments and managing prescriptions from detected health trends.
- **Repo:** public, commits 27 (before/in/after event: 0/26/1), README solid
- **Demo/writeup:** video None, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Pump-free Peltier sole with reversed-polarity switching, copper heat spreading and 3D-printed modular frame; software chain Terra data to OpenAI insights to Scrapybara agent that books appointments.
- **Team size:** 3 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; placement within healthcare track; event dates from memory
- **Links:** [Devpost](https://devpost.com/software/therms-thermoregulation-wearables-with-ai-powered-insights) | [GitHub](https://github.com/arnavnc/therms-platform)

### VisionGuard: smart vision for smarter driving  (TreeHacks 2025)

- **Prizes:** Autonomy Grand Prize [unknown]; Tesla: Excellence Prize [unknown]  (tier: track_winner)
- **Pitch:** Applies vision-language models with ensembling and prompting tricks to in-car video to flag distracted driving, reckless maneuvers and hazardous road conditions.
- **Problem / user:** Driver distraction, reckless driving and icy or low-visibility conditions cause crashes; drivers and fleets lack explainable safety feedback. / drivers, fleet managers, insurers
- **Domain / idea type:** mobility_transport + safety_security / data_or_analytics
- **Platforms / hardware / AI:** other / False / vision; llm_chat; predictive_ml
- **Stack:** langs Python; frontend ; backend Hugging Face TRL; DeepSpeed; PyTorch; ONNX Runtime; TensorRT; OpenCV; db ; hosting Colab; 4x A100 GPUs
- **Tech/APIs:** Google Gemini (ai_model, core); Pixtral 13B (ai_model, core); OpenAI GPT-4 (ai_model, supporting); Qwen VL-2B with GRPO (ai_model, supporting); NuScenes-QA dataset (data_source, supporting); Hugging Face TRL (framework, supporting); OpenCV (framework, supporting)
- **Sponsor APIs:**  | fit: Won Autonomy grand prize and a Tesla prize; the writeup does not describe sponsor product use beyond a driving-scene benchmark dataset.
- **Repo:** public, commits 18 (before/in/after event: 0/18/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 0, writeup long, impact claims False
- **Notes:** Research-style build: majority-vote ensembles of Gemini and Pixtral with chain-of-thought, plus a GRPO fine-tune of Qwen VL-2B on 4 A100s that did not beat API models; real-time inference not achieved.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; platforms; is_sponsor flags; event dates from memory
- **Links:** [Devpost](https://devpost.com/software/visionguard-smart-vision-for-smarter-driving) | [GitHub](https://github.com/JayYeung/tesla_kaggle)


## TreeHacks 2026

### ChromaChord  (TreeHacks 2026)

- **Prizes:** Winner Treehacks Grand Prize (3rd) [3rd]; Winner [Suno] Best Musical Hack [unknown]  (tier: overall_top3)
- **Pitch:** Real-time jazz assistant that turns live MIDI into chroma vectors, maps chord transitions on a graph, suggests next chords and generates backing tracks.
- **Problem / user:** Learning jazz harmony and improvisation lacks interpretable tools; opaque LLM suggestions do not explain which chords work together. / jazz learners and improvising musicians
- **Domain / idea type:** creative_media + education / creative_tool
- **Platforms / hardware / AI:** web / None / llm_chat; agent_or_tool_use; rag_or_search; generative_media
- **Stack:** langs Python; TypeScript; frontend Next.js; backend Python; Claude Agent SDK; db ; hosting Vercel
- **Tech/APIs:** Perplexity Sonar API (ai_model, supporting, sponsor); Claude Agent SDK (ai_model, supporting, sponsor); Chroma vectors and harmonic graph model (other, core); MIDI input (hardware_part, core); Suno (ai_model, unclear, sponsor); Next.js (framework, supporting); Vercel (cloud, token)
- **Sponsor APIs:** Perplexity Sonar; Claude Agent SDK | fit: Suno Best Musical Hack prize listed; the writeup does not mention Suno and says backing tracks are generated dynamically.
- **Repo:** public, commits 62 (before/in/after event: 0/61/1), README solid
- **Demo/writeup:** video None, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Deterministic physics and graph-theory harmony engine ranks about 4000 chords by dissonance; AI is a decision layer on top. Uses direct MIDI input after noisy audio proved hard.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; has_hardware; ui_polish; is_sponsor flags; event dates from memory
- **Links:** [Devpost](https://devpost.com/software/chromachord) | [GitHub](https://github.com/J4Joshua/JASS-APP)

### diffuji  (TreeHacks 2026)

- **Prizes:** Most Creative [unknown]; [Neo] Most Likely to Become a Product [unknown]  (tier: sponsor_winner)
- **Pitch:** Raspberry Pi instant camera that runs photos through image-to-image diffusion filters and prints the result on a thermal sticker printer, plus a price-lookup mode.
- **Problem / user:** Instant cameras are fun, and the team wanted to make physical keepsakes of moments that are part real and part dreamed. / casual consumers and event attendees
- **Domain / idea type:** creative_media + entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / generative_media; vision; rag_or_search
- **Stack:** langs Python; frontend ; backend Python; Railway API server; db ; hosting Railway; Modal
- **Tech/APIs:** Raspberry Pi Zero 2 W + thermal printer (hardware_part, core); Gemini 2.5 Flash Image (ai_model, core); OpenAI gpt-image-1.5 (ai_model, supporting); FLUX.1-Kontext on Modal (ai_model, supporting); Perplexity search (ai_model, supporting); Railway (cloud, supporting)
- **Sponsor APIs:**  | fit: Entered the Neo most-likely-to-become-a-product prize with a consumer instant-camera device and project site; the page does not mention any Neo product use.
- **Repo:** public, commits 25 (before/in/after event: 0/22/3), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 9, writeup long, impact claims False
- **Notes:** Custom Railway API routes modes to Gemini 2.5 Flash Image, gpt-image-1.5 or self-hosted FLUX.1-Kontext on a Modal H100; ordered Bayer dithering for thermal prints; Perplexity-based thrift price stickers; case printed at the makerspace.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; is_sponsor; placement_tier
- **Links:** [Devpost](https://devpost.com/software/diffuji) | [GitHub](http://github.com/alexkranias/dispo)

### Freak in the Sheets  (TreeHacks 2026)

- **Prizes:** Winner Most Technically Complex [unknown]; Winner [Human Capital] Human Capital Fellowship Prize ($50k equity-free per team member, up to $200k) [unknown]  (tier: sponsor_winner)
- **Pitch:** An LLVM compiler backend and custom instruction set that runs compiled C or Rust programs inside Google Sheets via iterative-calculation formulas.
- **Problem / user:** Not a problem-driven project; it demonstrates that arbitrary software can be executed within a spreadsheet's formula limits. / programmers and compiler enthusiasts
- **Domain / idea type:** dev_tools + entertainment_games / dev_tool
- **Platforms / hardware / AI:** web; cli / False / False
- **Stack:** langs C; C++; JavaScript; frontend Google Sheets; backend LLVM; db ; hosting Google Sheets
- **Tech/APIs:** LLVM (framework, core); Google Sheets (other, core); Custom ISA and assembler (framework, core)
- **Sponsor APIs:**  | fit: Won the Human Capital Fellowship prize with a compiler-to-spreadsheet project; the page shows no use of a Human Capital product.
- **Repo:** public, commits 28 (before/in/after event: 0/28/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup medium, impact claims False
- **Notes:** Invented ISA with 2D memory and assembler; uses Sheets iterative calculation and a backend validation exploit to loop without input; packs 16,666 32-bit ints per cell via Unicode glyphs.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; is_sponsor; problem_statement; placement_tier
- **Links:** [Devpost](https://devpost.com/software/freak-in-the-sheets-7jl542) | [GitHub](https://github.com/kognise/freak-in-the-sheets/)

### HeartStart  (TreeHacks 2026)

- **Prizes:** Winner Best Beginner Hack [unknown]  (tier: track_winner)
- **Pitch:** Autonomous mobile robot that monitors a wearable heart-rate sensor, alerts emergency services via Twilio on cardiac arrest, drives to the patient and performs CPR compressions.
- **Problem / user:** Over 350,000 out-of-hospital cardiac arrests occur yearly in the US and CPR must be continuous in the minutes before help arrives. / cardiac arrest patients and bystanders at home
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision
- **Stack:** langs Python; C; JavaScript; frontend HTML; CSS; backend ROS2; OpenCV; db ; hosting 
- **Tech/APIs:** ROS2 (framework, core); OpenCV (framework, core); Arduino (hardware_part, core); Twilio (telecom, supporting); Arducam cameras (hardware_part, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 15 (before/in/after event: 0/15/0), README none
- **Demo/writeup:** video True, live none, screenshots 10, writeup long, impact claims True (Cites over 350,000 US out-of-hospital cardiac arrests per year as motivation.)
- **Notes:** Mechanical CPR mechanism uses a crank shaft with 3D-printed parts; ROS2 depth-based vision with Arducam cameras for approach and positioning; Twilio emergency call routed to a friend in the demo.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/heartstart) | [GitHub](https://github.com/nicolewongbiz/cpr-robot.git)

### Mira  (TreeHacks 2026)

- **Prizes:** Winner Most Impactful [unknown]; Winner [OpenAI] Artificial Intelligence Track [unknown]  (tier: track_winner)
- **Pitch:** Voice assistant on Ray-Ban Meta glasses for dementia patients that finds objects in a 3D reconstruction of the home, answers medication questions and alerts caregivers.
- **Problem / user:** Dementia patients repeatedly lose items and forget medications, and family caregivers cannot be present around the clock. / dementia patients and family caregivers
- **Domain / idea type:** health_wellness + accessibility / automation_or_agent
- **Platforms / hardware / AI:** web; mobile_android; hardware / True / agent_or_tool_use; vision; speech_or_voice; rag_or_search; llm_chat
- **Stack:** langs Python; TypeScript; Kotlin; frontend Next.js; React; Tailwind CSS; ONNX Runtime Web; backend FastAPI; Modal; MediaMTX; Tailscale; Twilio; db Supabase Postgres; hosting Modal A100 GPUs; Google Cloud
- **Tech/APIs:** OpenAI (GPT-5 mini, Whisper, TTS) (ai_model, core, sponsor); Perplexity Sonar (ai_model, core, sponsor); OpenEvidence / FHIR patient info (data_source, supporting, sponsor); Modal A100 GPUs (cloud, core); Grounding DINO and DPVO/HLoc (ai_model, core); Ray-Ban Meta glasses (hardware_part, core); Supabase Realtime (database, core); Gemini (ai_model, supporting); ElevenLabs (ai_model, unclear); Twilio (telecom, unclear); Tailscale (other, supporting)
- **Sponsor APIs:** OpenAI; Perplexity Sonar; OpenEvidence | fit: OpenAI Whisper, GPT-5 mini and TTS power the voice agent with function-calling tools for spatial search, medication lookup and escalation.
- **Repo:** public, commits 107 (before/in/after event: 0/103/4), README detailed
- **Demo/writeup:** video None, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Chains specialist models: SfM point cloud on Modal GPUs, Grounding DINO object graph, DPVO pose tracking with HLoc re-localization, Gemini orientation check; de-identified FHIR records; long hop chain from glasses to laptop.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; event dates from memory; n_screenshots; OpenAI track tier
- **Links:** [Devpost](https://devpost.com/software/mira-w65b0a) | [GitHub](https://github.com/nathanjzhao/treehacks2026)

### Robosurge  (TreeHacks 2026)

- **Prizes:** Winner Treehacks Grand Prize (2nd) [2nd]  (tier: overall_top3)
- **Pitch:** Four-arm magnetically controlled robot surgery station steered by natural-language commands and a Quest 3 head-tracked camera, with Lean-verified trajectory safety.
- **Problem / user:** Surgical specialist shortages and costly operating rooms; current surgical robots add precision but do not automate tasks or reduce staffing. / surgeons and hospitals
- **Domain / idea type:** health_wellness + ai_agents_infra / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision; agent_or_tool_use; llm_chat
- **Stack:** langs Python; Lean; frontend TanStack; WebRTC; backend FastAPI; WebSocket; Nix; db ; hosting ASUS Ascent GX10; edge
- **Tech/APIs:** Four robot arms with custom inverse kinematics (hardware_part, core); Intel RealSense depth camera and ArUco tags (hardware_part, core); Meta Quest 3 (hardware_part, core); GPT-5.2 (ai_model, core); Gemini Robotics-ER 1.5 (ai_model, core); Segment Anything and YOLOv11 (ai_model, supporting); Lean theorem prover (other, supporting); Nix (other, supporting); ASUS Ascent GX10 (hardware_part, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 81 (before/in/after event: 0/81/0), README thin
- **Demo/writeup:** video None, live none, screenshots 4, writeup long, impact claims True (Cites projected shortage of nearly 20,000 surgical specialists by 2036, about $2,200 per hour per surgeon, and staffing cut from 10 to 1.)
- **Notes:** Custom inverse kinematics, RealSense plus ArUco affine mapping across four arms, GPT-5.2 and Gemini Robotics fusion, Nix reproducible builds, and Lean proofs of safe trajectories written without AI.
- **Team size:** 5 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; event dates from memory; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/we-use-nix) | [GitHub](https://github.com/quantum9Innovation/treehacks2026)

### Sentinel  (TreeHacks 2026)

- **Prizes:** Winner Best Hardware Hack [unknown]  (tier: track_winner)
- **Pitch:** Multi-agent coding system built on the Claude Agent SDK that takes a GitHub repo and a task and writes bare-metal embedded code, tested on a Raspberry Pi Zero W OS.
- **Problem / user:** Bare-metal embedded programming is notoriously hard for AI coding tools. / embedded systems developers
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web; hardware / True / agent_or_tool_use; llm_chat
- **Stack:** langs C; ARM assembly; Python; TypeScript; frontend Next.js; React; Tailwind; backend FastAPI; Uvicorn; Claude Agent SDK; db ; hosting 
- **Tech/APIs:** Claude Agent SDK (framework, core); Claude Opus (ai_model, core); Raspberry Pi Zero W (hardware_part, core); arm-none-eabi-gcc (framework, supporting); Next.js (framework, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** Orchestrator, research and parallel worker agents fork the repo and read datasheets; team co-developed Sentinel OS on an RPi Zero W in ARM assembly and C to test the agents.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; platforms; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/sentinel-c8ki50) | [GitHub](https://github.com/apple-314/treehacks26)

### Shepherd  (TreeHacks 2026)

- **Prizes:** Winner Treehacks Grand Prize (1st) [1st]; Winner [OpenEvidence] Healthcare Track Grand Prize [unknown]; Winner [OpenEvidence] Best Use of Clinical Information (4x Apple Watches) [unknown]  (tier: overall_top3)
- **Pitch:** Motorized white cane that uses iPhone LiDAR to sense obstacles and nudges the user toward clear paths, plus GPS wheelchair-accessible voice navigation.
- **Problem / user:** Plain canes only signal obstacles, and smart steering canes are too expensive for most blind and low-vision users. / blind and low-vision pedestrians
- **Domain / idea type:** accessibility + mobility_transport / hardware_gadget
- **Platforms / hardware / AI:** mobile_ios; hardware / True / vision; speech_or_voice
- **Stack:** langs Swift; C++; frontend SwiftUI; ARKit; backend CoreBluetooth; FreeRTOS; NimBLE; db ; hosting GCP
- **Tech/APIs:** iPhone LiDAR / ARKit (hardware_part, core); Seeed XIAO ESP32-S3 with DC motor (hardware_part, core); OpenRouteService (maps_geo, supporting); Google Geocoding API (maps_geo, supporting); Overpass API (maps_geo, supporting); Vapi (ai_model, supporting); Apple Vision framework (ai_model, supporting); DeepLabV3 / CoreML (ai_model, unclear)
- **Sponsor APIs:**  | fit: OpenEvidence track prizes listed, but the writeup does not mention OpenEvidence or clinical information use.
- **Repo:** public, commits 36 (before/in/after event: 0/36/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 24, writeup long, impact claims True (Cites 1.7 million legally blind Americans; reports sub-50ms detection-to-motor latency and 60fps depth pipeline.)
- **Notes:** 60fps LiDAR gap-seeking steering sent by BLE to an ESP32 motor on the cane, under 50ms claimed latency; grass avoidance uses plain HSV color analysis with no ML; dual watchdogs zero the motor.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; event dates from memory
- **Links:** [Devpost](https://devpost.com/software/raising-cane) | [GitHub](https://github.com/tonywangs/shepherd)

### VisionOS  (TreeHacks 2026)

- **Prizes:** Winner [OpenAI] Artificial Intelligence Track [unknown]  (tier: track_winner)
- **Pitch:** Voice-driven agentic operating layer for blind users that controls the browser and desktop apps by conversation instead of linear screen reading.
- **Problem / user:** Screen readers read pages linearly, break on inaccessible sites and need many shortcuts, unlike how sighted users scan. / blind and visually impaired computer users
- **Domain / idea type:** accessibility + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** desktop / False / agent_or_tool_use; speech_or_voice; vision; rag_or_search; llm_chat
- **Stack:** langs TypeScript; frontend Electron; backend LangGraph; Agentverse; db Elasticsearch; hosting 
- **Tech/APIs:** OpenAI GPT-4.1 mini (ai_model, core, sponsor); Cartesia TTS (ai_model, core, sponsor); LangGraph (framework, core); Stagehand by Browserbase (other, core, sponsor); Agent-S by Simular AI (other, core, sponsor); Perplexity Sonar API (ai_model, supporting, sponsor); Elasticsearch with Jina embeddings (database, supporting, sponsor); Fetch.ai Agentverse (other, unclear, sponsor)
- **Sponsor APIs:** OpenAI; Cartesia; Stagehand; Agent-S; Perplexity Sonar; Elasticsearch; Jina; Agentverse | fit: OpenAI GPT-4.1 mini is the conversational brain and routing classifier behind the multi-agent workflow.
- **Repo:** public, commits 50 (before/in/after event: 0/50/0), README thin
- **Demo/writeup:** video None, live none, screenshots 0, writeup long, impact claims True (States visual-impairment accessibility gaps cost companies $7 billion a year.)
- **Notes:** LangGraph supervisor with dedicated GPT-4.1-mini routing step; Stagehand drives the browser and Agent-S drives the desktop; Elasticsearch with Jina embeddings gives cross-session memory; Electron overlay UI.
- **Team size:** 3 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; event dates from memory; OpenAI track tier; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/visionos-5euxo7) | [GitHub](https://github.com/ledaniel0/treehacks2026)
