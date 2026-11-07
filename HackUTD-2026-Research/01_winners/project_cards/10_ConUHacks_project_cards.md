# ConUHacks: project cards (48 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## ConUHacks IX

### 404 Lost & Found  (ConUHacks IX)

- **Prizes:** 3rd Place - 4x MSI MAG 27” QHD Gaming monitor and MLH Winner Pins [3rd]  (tier: overall_top3)
- **Pitch:** Lost-and-found app that matches reported items to found-item images using YOLOv8 detection and ResNet similarity, then gives map directions to the item.
- **Problem / user:** Traditional lost-and-found relies on manual descriptions and memory, making matching slow and imprecise. / people who lost belongings; venues running lost and found
- **Domain / idea type:** retail_consumer + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs Python; frontend Streamlit; backend FastAPI; db MongoDB; Azure Blob Storage; hosting Azure; Docker; Terraform; GitHub Actions
- **Tech/APIs:** YOLOv8 (ai_model, core); ResNet (ai_model, core); OpenCV (framework, supporting); Azure AI Vision (ai_model, unclear); Microsoft Azure (cloud, core); MongoDB (database, supporting, sponsor); Google Maps API (maps_geo, supporting); Terraform (other, supporting); Docker (other, supporting)
- **Sponsor APIs:** MongoDB
- **Repo:** public, commits 140 (before/in/after event: 0/138/2), README detailed
- **Demo/writeup:** video False, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Full cloud deployment with Docker, Terraform on Azure and GitHub Actions CI/CD; Streamlit UI and FastAPI backend; Google Maps used for navigation to item.
- **Team size:** 4 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; MongoDB is_sponsor; Azure AI Vision depth
- **Links:** [Devpost](https://devpost.com/software/404-lost-found) | [GitHub](https://github.com/nic5694/404_Lost_And_Found)

### ASL-Bridge  (ConUHacks IX)

- **Prizes:** [DRUIDE] Best Use of Language [unknown]  (tier: sponsor_winner)
- **Pitch:** Prototype that recognizes ASL signs through computer vision and an ML model, converts them to grammatical English and speaks them aloud.
- **Problem / user:** Few people understand ASL and translation apps neglect sign language, limiting communication for signers. / ASL users and the people they talk with
- **Domain / idea type:** accessibility + education / social_good
- **Platforms / hardware / AI:** desktop / False / vision; llm_chat; speech_or_voice
- **Stack:** langs Python; frontend ; backend OpenCV; Jupyter; db ; hosting 
- **Tech/APIs:** OpenCV (framework, core); custom ML sign model (ai_model, core); OpenAI (ai_model, core); ElevenLabs (ai_model, supporting)
- **Sponsor APIs:**  | fit: Entry for Druide's Best Use of Language prize, translating sign language into grammatically correct spoken English.
- **Repo:** public, commits 39 (before/in/after event: 0/39/0), README solid
- **Demo/writeup:** video False, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Custom word-detection ML model with hand/face tracking; OpenAI used to decode ASL grammar into English and ElevenLabs for voice output; prototype is not real-time yet.
- **Team size:** 4 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; platforms; team_size; OpenAI role
- **Links:** [Devpost](https://devpost.com/software/asl-bridge) | [GitHub](https://github.com/MaximBacar/asl-bridge)

### Better Call Saul AI  (ConUHacks IX)

- **Prizes:** [MLH] Best Domain Name from GoDaddy Registry [unknown]  (tier: sponsor_winner)
- **Pitch:** Unknown: Devpost page returned 'page does not exist'; the name and old domain tag suggest a legal or fintech AI assistant.
- **Problem / user:** None / None
- **Domain / idea type:** civic_legal + fintech_finance / other
- **Platforms / hardware / AI:**  / None / None
- **Stack:** langs TypeScript; JavaScript; HTML; CSS; frontend ; backend ; db ; hosting 
- **Sponsor APIs:** GoDaddy Registry | fit: Prize was the MLH GoDaddy Registry best domain name award; how the project used the domain is not visible.
- **Repo:** public, commits 33 (before/in/after event: 0/27/6), README none
- **Demo/writeup:** video None, live none, screenshots None, writeup None, impact claims None
- **Notes:** Queue-only record: the Devpost URL is a 404 now and a title search found several similarly named projects with no way to confirm which is this one.
- **Team size:** None | **Confidence:** low | unverified: page_404; one_line_pitch; problem_statement; target_user; domain_primary; idea_type; platforms; has_hardware; ai_used; ai_types; tech_items; sponsor_fit_note; team_size; n_screenshots; writeup_sections; writeup_length; has_impact_claims; demo_video_url
- **Links:** [Devpost](https://devpost.com/software/better-call-saul-ai) | [GitHub](https://github.com/Stoplossking1/BetterCallSaulAI)

### Beyond Budgeting  (ConUHacks IX)

- **Prizes:** [TAILE'D] Best Use of Lovable [unknown]  (tier: sponsor_winner)
- **Pitch:** Lovable-built personal finance companion with simulated open-banking data, spending dashboard, AI budgeting, investment and Sun Life product recommendations.
- **Problem / user:** Individuals lack accessible, personalized help understanding spending and choosing savings or investment products. / everyday consumers managing money
- **Domain / idea type:** fintech_finance + education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / recommendation
- **Stack:** langs TypeScript; SQL; frontend Lovable; backend ; db SQL; hosting Lovable
- **Tech/APIs:** Lovable (other, core, sponsor); Sun Life products (other, token, sponsor); Simulated open banking API (data_source, supporting)
- **Sponsor APIs:** Lovable | fit: Prize for best use of Lovable; the app was built on that platform.
- **Repo:** public, commits 55 (before/in/after event: 0/55/0), README solid
- **Demo/writeup:** video False, live not_checked, screenshots 2, writeup short, impact claims False
- **Notes:** Built with Lovable; open banking is simulated through API endpoints; chatbot advisor listed as upcoming and literacy hub as in development.
- **Team size:** 4 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; ai_types; Sun Life sponsor flag
- **Links:** [Devpost](https://devpost.com/software/beyond-budgeting) | [GitHub](https://github.com/pankajdeep/beyond-budgeting)

### CrisisConnect  (ConUHacks IX)

- **Prizes:** [MLH] Best Use of Gen AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Streamlit app that classifies free-text disaster requests into need types with a fine-tuned BERT model and ranks donor offers by relevance, location and capacity.
- **Problem / user:** Disaster victims struggle to find shelter, food and medical help, and donors lack a way to be matched to specific needs quickly. / disaster victims and donors
- **Domain / idea type:** social_community + civic_legal / social_good
- **Platforms / hardware / AI:** web / False / recommendation; rag_or_search; llm_chat
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend Streamlit; backend Python; PyTorch; db ; hosting 
- **Tech/APIs:** BERT (fine-tuned) (ai_model, core); Hugging Face (ai_model, supporting); Llama 3 (ai_model, unclear); PyTorch (framework, supporting); Streamlit (framework, supporting)
- **Sponsor APIs:**  | fit: Targeted MLH's Best Use of Gen AI with NLP intent classification and semantic matching of relief requests to donor offers.
- **Repo:** public, commits 30 (before/in/after event: 0/30/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Combines a fine-tuned BERT intent classifier with semantic matching over donor offers; Llama 3 and Hugging Face appear in the built-with list.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/crisisconnect-8zm143) | [GitHub](https://github.com/gsinchan135/AIdmatch)

### CyberOxide  (ConUHacks IX)

- **Prizes:** [MLH] Best Use of MongoDB Atlas [unknown]  (tier: sponsor_winner)
- **Pitch:** Privacy-first local network monitor with a Rust packet-capture backend, metadata-only analysis, LLM threat insights and a Streamlit and MongoDB dashboard.
- **Problem / user:** People lack a private way to spot threats in their own network traffic without exposing packet contents. / home and individual network users
- **Domain / idea type:** safety_security + dev_tools / dev_tool
- **Platforms / hardware / AI:** desktop; web / False / llm_chat
- **Stack:** langs Rust; Python; frontend Streamlit; backend Rust; db MongoDB; hosting 
- **Tech/APIs:** MongoDB (database, core, sponsor); Rust packet capture (framework, core); Streamlit (framework, core); LLM threat analysis (provider not named) (ai_model, supporting)
- **Sponsor APIs:** MongoDB | fit: Used local MongoDB with async operations to store network events behind the dashboard; page does not mention Atlas specifically.
- **Repo:** public, commits 69 (before/in/after event: 0/66/3), README detailed
- **Demo/writeup:** video False, live none, screenshots 1, writeup long, impact claims False
- **Notes:** Writeup is largely a README; analyzes only traffic metadata, sends anonymized queries to an LLM, and integrates async MongoDB into Streamlit; team learned Rust during the event.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/cyberoxide) | [GitHub](https://github.com/nichoc0/ConUHacks2025)

### FinHealth  (ConUHacks IX)

- **Prizes:** [MLH] Best Use of Streamlit [unknown]  (tier: sponsor_winner)
- **Pitch:** Streamlit finance dashboard with stock picks, sentiment-tagged news, a context-aware chatbot, tailored investment plans and portfolio analysis from a screenshot.
- **Problem / user:** Managing money and understanding investments is intimidating for beginners. / beginner investors
- **Domain / idea type:** fintech_finance + education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; vision; recommendation
- **Stack:** langs Python; HTML; CSS; frontend Streamlit; backend Python; db ; hosting 
- **Tech/APIs:** Streamlit (framework, core, sponsor); OpenAI (ai_model, core)
- **Sponsor APIs:** Streamlit | fit: Built the whole front end as a multi-page Streamlit app (dashboard, chatbot, plan form, portfolio analysis).
- **Repo:** public, commits 79 (before/in/after event: 0/73/6), README detailed
- **Demo/writeup:** video False, live none, screenshots 25, writeup medium, impact claims False
- **Notes:** Parses a user's portfolio screenshot with a vision-capable model and ties chatbot answers to tracked stocks and recent news sentiment.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/budget-buddy-b42oin) | [GitHub](https://github.com/AndyChhuon/FinHealth)

### Finsurance  (ConUHacks IX)

- **Prizes:** Sun Life - 4x 100$ Amazon gift cards [unknown]  (tier: sponsor_winner)
- **Pitch:** Web financial toolkit with a budgeting planner, a literacy quiz and Fin, a dolphin AI companion built in Botpress and trained on Sun Life material.
- **Problem / user:** People need accessible financial guidance and education; the team answered Sun Life's challenge to build an AI companion. / people seeking financial guidance
- **Domain / idea type:** fintech_finance + education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; Python; JavaScript; frontend React; backend FastAPI; Flask; db PostgreSQL; hosting 
- **Tech/APIs:** Botpress (ai_model, core); Sun Life data (data_source, supporting, sponsor); FastAPI (framework, supporting); PostgreSQL (database, supporting); React (framework, supporting)
- **Sponsor APIs:** Sun Life challenge data | fit: Answered Sun Life's challenge by building an AI financial-companion chatbot trained on Sun Life data, alongside a budgeting tool and quiz.
- **Repo:** public, commits 43 (before/in/after event: 0/43/0), README none
- **Demo/writeup:** video False, live none, screenshots 31, writeup medium, impact claims False
- **Notes:** Companion chatbot built with Botpress workflows and custom tools; page links two GitHub repos (backend and an app repo) and notes infrastructure hosting of Postgres and FastAPI was the main hurdle.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; domain_secondary
- **Links:** [Devpost](https://devpost.com/software/finsurance) | [GitHub](https://github.com/TempestSt3rm/conuhack_backend)

### FireWatch  (ConUHacks IX)

- **Prizes:** SAP - Lunch Tour with hiring managers [unknown]  (tier: sponsor_winner)
- **Pitch:** Quebec wildfire dashboard that optimizes firefighting resource deployment from fire reports and predicts 2025 fire-prone areas with a scikit-learn model on a Mapbox map.
- **Problem / user:** Quebec wildfires threaten communities, and emergency services need smarter resource allocation and advance prediction of fire locations. / emergency and wildfire response services in Quebec
- **Domain / idea type:** safety_security + sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; shadcn/ui; Mapbox; backend Flask; scikit-learn; db ; hosting 
- **Tech/APIs:** scikit-learn (framework, core); Mapbox (maps_geo, core); Flask (framework, supporting); React (framework, supporting)
- **Sponsor APIs:**  | fit: Won SAP's lunch tour with hiring managers, a recruiting prize; page does not show any SAP tool used.
- **Repo:** public, commits 87 (before/in/after event: 0/86/1), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup medium, impact claims False
- **Notes:** Two parts: allocation optimizer weighing severity, deployment time and cost of missed responses, plus ML prediction trained on 2020-2023 history; CSV upload dashboard with map and list views.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/firewatch-qn4yap) | [GitHub](https://github.com/jammy312/Hackaton2025)

### GeoAir  (ConUHacks IX)

- **Prizes:** DRW - 4x JBL Speakers for 1st Place [unknown]  (tier: sponsor_winner)
- **Pitch:** Dashboard combining Montreal real-time air quality and EV charging station open data to explore whether EV adoption links to cleaner air.
- **Problem / user:** Unclear whether electric vehicle uptake correlates with better urban air quality. / city residents and analysts curious about EVs and pollution
- **Domain / idea type:** sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; JavaScript; frontend Next.js; Tailwind CSS; backend Flask; pandas; numpy; geopandas; db ; hosting 
- **Tech/APIs:** Donnees Montreal open data (data_source, core); Flask (framework, core); pandas (framework, core); Next.js (framework, supporting); ChatGPT (coding help) (ai_model, token)
- **Sponsor APIs:**  | fit: Addressed the DRW open-data challenge by analyzing Montreal air-quality and EV charging datasets.
- **Repo:** public, commits 6 (before/in/after event: 0/6/0), README none
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Flask backend pulls five CSV datasets from the Montreal open data portal with live updates; team's first time using open data.
- **Team size:** 4 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/geoair) | [GitHub](https://github.com/mylinhtang/conuhacksIV)

### GUN WEST  (ConUHacks IX)

- **Prizes:** BEENOX - 4X PRIZES FOR WINNERS [unknown]  (tier: sponsor_winner)
- **Pitch:** Engine-free Java 1v1 multiplayer gunfight game with pistol, shotgun and sniper switching and speed-boost stars, themed on the event's Wild West.
- **Problem / user:** Not stated; built as a game inspired by Call of Duty, Hotline Miami and the event's cowboy theme. / casual gamers
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / False / False
- **Stack:** langs Java; frontend Swing; backend Java Sockets; db ; hosting 
- **Tech/APIs:** Java Swing (framework, core); Java Sockets (framework, core); Eclipse (other, supporting); Paint.NET (other, supporting)
- **Sponsor APIs:**  | fit: Won a Beenox sponsor prize ('4X prizes for winners'); page does not mention any Beenox tool, so the fit is not shown.
- **Repo:** public, commits 95 (before/in/after event: 0/95/0), README none
- **Demo/writeup:** video True, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Written from scratch with Java Sockets and Swing, no game engine; peer-to-peer client sync; all art and sound made in-house within 24 hours.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; problem_statement; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/gun-west) | [GitHub](https://github.com/TheBester14/GunWest.git)

### LeetWrite  (ConUHacks IX)

- **Prizes:** 2nd Place - 4x Meta Quest 3S 128GB VR Headset with Touch Plus Controllers & Batman: Arkham Shadow and MLH Winner Pins [2nd]  (tier: overall_top3)
- **Pitch:** Reverse-LeetCode game: an LLM generates messy code, players write explanations, and the LLM judges them in ELO-ranked multiplayer lobbies.
- **Problem / user:** Developers practice writing code but rarely practice reading and documenting code written by others. / students and software engineers practicing code comprehension
- **Domain / idea type:** education + entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs JavaScript; frontend Next.js; backend Express; Socket.IO; db MongoDB; hosting 
- **Tech/APIs:** OpenAI API (ai_model, core); Socket.IO (framework, core); MongoDB (database, supporting, sponsor); Next.js (framework, supporting); Express (framework, supporting)
- **Sponsor APIs:** MongoDB
- **Repo:** public, commits 29 (before/in/after event: 0/21/8), README solid
- **Demo/writeup:** video False, live not_checked, screenshots 9, writeup medium, impact claims False
- **Notes:** Solo-built in 24 hours; OpenAI both generates the code puzzles and scores answers on correctness, creativity and clarity; Socket.IO lobbies with ELO ratings.
- **Team size:** 1 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; MongoDB is_sponsor; team_size inferred from single listed creator
- **Links:** [Devpost](https://devpost.com/software/leetwrite) | [GitHub](https://github.com/Jxl-s/ConUHacksIX)

### PrezPal  (ConUHacks IX)

- **Prizes:** 1st Place - 4x PS5 and MLH Winner Pins [1st]  (tier: overall_top3)
- **Pitch:** Voice-controlled generative slide editor that builds and restyles presentations on a topic using OpenAI function calling and Moonshine speech recognition.
- **Problem / user:** Making and editing slide decks is slow; the team wanted a faster hands-free generative presentation tool. / presenters, students, office workers
- **Domain / idea type:** productivity_workplace + creative_media / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs JavaScript; Python; frontend React; CSS; backend Python; db ; hosting 
- **Tech/APIs:** OpenAI API (ai_model, core); Moonshine (ai_model, core); Unsplash (data_source, supporting); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 97 (before/in/after event: 0/97/0), README thin
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Natural-language/voice commands are turned into function calls on a custom slide-editing engine; polling used after WebSocket setup failed; Unsplash supplies images.
- **Team size:** 4 | **Confidence:** medium | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/prezpal-36079w) | [GitHub](https://github.com/CarciDev/PrezPal)

### Quebec FireFighters  (ConUHacks IX)

- **Prizes:** SAP - Lunch Tour with hiring managers [unknown]  (tier: sponsor_winner)
- **Pitch:** SwiftUI iOS app that allocates firefighting units from wildfire data (CSV or link) to cut damage and cost, and predicts future wildfires with a model trained on historical data.
- **Problem / user:** Rising wildfires since 2020 call for better allocation of firefighting resources and prediction of where fires will occur. / fire management agencies in Quebec
- **Domain / idea type:** sustainability_climate + safety_security / data_or_analytics
- **Platforms / hardware / AI:** mobile_ios; desktop / False / predictive_ml
- **Stack:** langs Swift; Python; frontend SwiftUI; Xcode; backend Flask; REST API; db ; hosting 
- **Tech/APIs:** SwiftUI (framework, core); Flask (framework, supporting); Wildfire prediction model (ai_model, core)
- **Sponsor APIs:**  | fit: Entered the SAP challenge with a wildfire resource-allocation and prediction app; page does not name an SAP product.
- **Repo:** public, commits 17 (before/in/after event: 0/17/0), README solid
- **Demo/writeup:** video True, live none, screenshots 16, writeup short, impact claims False
- **Notes:** Native SwiftUI client for iPhone and Mac backed by a Flask API; page shows two GitHub repos (iOS app and a second CONUHack2025 repo).
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; ai_types; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/quebec-firefighters) | [GitHub](https://github.com/alireza12t/ConUHack2025-Quebec-Firefighters-iOS-App)

### RememberThroughMe  (ConUHacks IX)

- **Prizes:** [MLH] Best Use of AI powered by Reach Capital [unknown]  (tier: sponsor_winner)
- **Pitch:** Memory-assistance system for people with memory loss: recognizes faces, recalls past interactions from MongoDB, and holds voice-to-voice AI phone calls.
- **Problem / user:** Memory loss isolates people from loved ones, who need real-time help recalling past interactions. / people with memory loss and their families
- **Domain / idea type:** health_wellness + accessibility / social_good
- **Platforms / hardware / AI:** mobile_ios; bot_or_chat / False / llm_chat; agent_or_tool_use; vision; speech_or_voice; rag_or_search
- **Stack:** langs Python; Swift; frontend Swift; backend Python; db MongoDB; hosting 
- **Tech/APIs:** OpenAI GPT agent (ai_model, core); MongoDB (database, core, sponsor); FaceNet + OpenCV (ai_model, core); Faiss (framework, supporting); Twilio (telecom, core)
- **Sponsor APIs:** MongoDB | fit: Targeted the Reach Capital AI prize with an AI memory companion; also uses MongoDB as the agent's editable memory store.
- **Repo:** public, commits 42 (before/in/after event: 0/40/2), README thin
- **Demo/writeup:** video True, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** OpenAI agent edits and retrieves MongoDB records directly; FaceNet embeddings indexed with Faiss for fast recall; Twilio voice calls with speech diarization; Swift in the stack.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; platforms; problem_statement
- **Links:** [Devpost](https://devpost.com/software/rememberthroughme) | [GitHub](https://github.com/ayush27316/rtMe)

### RestoPort  (ConUHacks IX)

- **Prizes:** [TAILE'D] Best Social Media Post [unknown]  (tier: sponsor_winner)
- **Pitch:** Streamlit dashboard using airport flight data to help airport restaurants and shops anticipate peak periods, staffing and waste, with beta sales prediction.
- **Problem / user:** Airport businesses struggle to predict busy periods, plan staffing and minimize waste. / airport restaurants and retail stores
- **Domain / idea type:** retail_consumer / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; frontend Streamlit; backend pandas; numpy; Cloudscraper; db ; hosting Streamlit Cloud
- **Tech/APIs:** Streamlit (framework, core, sponsor); pandas (framework, core); Cloudscraper (other, supporting); Airport flight data (data_source, core)
- **Sponsor APIs:** Streamlit
- **Repo:** public, commits 64 (before/in/after event: 0/10/54), README none
- **Demo/writeup:** video False, live not_checked, screenshots 0, writeup short, impact claims False
- **Notes:** Scrapes an airport website's unconventional API with Cloudscraper; sales-prediction metric marked beta; hosted on Streamlit Cloud. Prize was for best social media post.
- **Team size:** 4 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; "What it does" section empty on page
- **Links:** [Devpost](https://devpost.com/software/restoport) | [GitHub](https://github.com/andrewchababi/streamlitFlights)

### UrbanCanvas  (ConUHacks IX)

- **Prizes:** DRW - 4x JBL Speakers for 1st Place [unknown]  (tier: sponsor_winner)
- **Pitch:** Map web app plotting Montreal murals, public art and cultural sites from open data, with filters and a fastest-route custom tour.
- **Problem / user:** Montreal's cultural open datasets are hard for citizens and tourists to explore as a coherent picture of the city. / Montreal citizens and tourists
- **Domain / idea type:** civic_legal + creative_media / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs JavaScript; frontend React; backend Node.js; db MongoDB; hosting 
- **Tech/APIs:** Google Maps API (maps_geo, core); MongoDB (database, core, sponsor); Montreal open data (data_source, core); ChatGPT (coding help) (ai_model, token)
- **Sponsor APIs:** MongoDB | fit: Used large Montreal public datasets as the DRW challenge asked, stored in MongoDB and visualized on a map.
- **Repo:** public, commits 43 (before/in/after event: 0/41/2), README solid
- **Demo/writeup:** video False, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Built on three Montreal open datasets for the DRW large-data challenge; filters by artist, year and borough; caches Google Maps calls to limit cost.
- **Team size:** 3 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; MongoDB is_sponsor
- **Links:** [Devpost](https://devpost.com/software/urbancanvas) | [GitHub](https://github.com/DobDub/UrbanCanvas)


## ConUHacks X

### AeroGuard.tech  (ConUHacks X)

- **Prizes:** [MLH] Best Use of Snowflake API [unknown]  (tier: sponsor_winner)
- **Pitch:** SOC-style real-time incident triage platform (A.E.G.I.S. Garden) using Gemini for explainable priority scores, Snowflake for forecasting, MongoDB for state and Solana for controlled funds.
- **Problem / user:** Cyber and disaster response teams face alert noise, opaque prioritization, slow coordination and low trust when money and identity are involved. / security operations and disaster-response teams
- **Domain / idea type:** safety_security + civic_legal / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; vision; predictive_ml; speech_or_voice; rag_or_search
- **Stack:** langs Python; TypeScript; JavaScript; frontend React; Vite; backend FastAPI; WebSockets; db MongoDB Atlas; Snowflake; hosting 
- **Tech/APIs:** Snowflake (Snowpipe Streaming, Cortex) (database, core, sponsor); Google Gemini (ai_model, core); OpenRouter (ai_model, supporting); MongoDB Atlas (database, supporting, sponsor); Solana (other, supporting); ElevenLabs (ai_model, supporting); FastAPI (framework, core); React (framework, supporting)
- **Sponsor APIs:** Snowflake; MongoDB Atlas | fit: Page says Snowpipe Streaming ingests incidents and Snowflake Cortex handles impact prediction, priority ranking and demand forecasting.
- **Repo:** public, commits 8 (before/in/after event: 0/6/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Monorepo with FastAPI API, React/Vite dashboard and Solana demo package; combines Gemini, OpenRouter routing, Snowflake Cortex, MongoDB Atlas, Solana and ElevenLabs voice alerts.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/aeroguard-tech) | [GitHub](https://github.com/GautamTalksDev/aeroguard-tech)

### Banq Pirate  (ConUHacks X)

- **Prizes:** Desjardins - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Android banking app that adapts to surroundings: night mode, jungle mode when moving, hand-gesture control and ElevenLabs voice for visually impaired users.
- **Problem / user:** Desjardins challenge to make a banking interface that feels alive and adapts to environment while staying accessible. / mobile banking users incl. visually impaired
- **Domain / idea type:** fintech_finance + accessibility / twist_on_known_app
- **Platforms / hardware / AI:** mobile_android / False / vision; speech_or_voice
- **Stack:** langs Java; XML; frontend Android Studio; backend ; db SQLite; hosting 
- **Tech/APIs:** ElevenLabs (ai_model, supporting); Google AI Edge gesture recognition (ai_model, supporting); SQLite (database, supporting); Android camera sensors (hardware_part, supporting)
- **Sponsor APIs:**  | fit: Built an adaptive, environment-reactive banking app in answer to the Desjardins challenge.
- **Repo:** public, commits 70 (before/in/after event: 0/69/1), README solid
- **Demo/writeup:** video False, live none, screenshots 3, writeup short, impact claims False
- **Notes:** Java/XML Android app using device camera sensors, Google hand-gesture recognition and ElevenLabs voice; team's first hackathon; ESP32 hardware planned next.
- **Team size:** 4 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/banq-pirate) | [GitHub](https://github.com/keatonnguyen/Pirate-Informatique)

### BooBoo Buddy  (ConUHacks X)

- **Prizes:** Dialogue - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** AI health agent that triages symptoms, finds nearby clinics via Google Places, phones them through Twilio, and books a chosen time slot for the user.
- **Problem / user:** Being sick makes it hard to call around for a clinic that can see you today. / patients needing a same-day clinic appointment
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs TypeScript; frontend Next.js 14; React; Tailwind CSS; backend Next.js; db Prisma; SQLite; hosting Vercel
- **Tech/APIs:** OpenRouter (GPT-4o-mini) (ai_model, core); Twilio (telecom, core); Google Places API (maps_geo, core); Web Speech API (other, supporting); Prisma + SQLite (database, supporting)
- **Sponsor APIs:**  | fit: Agent that connects symptom triage to real clinic bookings, aligned with the Dialogue virtual-care challenge; writeup lists Dialogue API integration as future work only.
- **Repo:** public, commits 46 (before/in/after event: 0/32/14), README detailed
- **Demo/writeup:** video None, live none, screenshots 4, writeup long, impact claims False
- **Notes:** LLM decides when to trigger tool calls; parses clinic replies into clickable 30-minute slots and handles walk-in versus appointment responses; includes a GenAI disclosure image.
- **Team size:** 3 | **Confidence:** medium | unverified: has_demo_video
- **Links:** [Devpost](https://devpost.com/software/booboo-buddy) | [GitHub](https://github.com/mchoi-cs/BooBooBuddy)

### Buildo  (ConUHacks X)

- **Prizes:** [MLH] Best Use of Gemini API [unknown]  (tier: sponsor_winner)
- **Pitch:** Turns a plain-language hardware idea into a visualization, AliExpress parts cart, starter firmware and illustrated assembly steps with a demo video.
- **Problem / user:** Hardware ideas are slow to realize because specs, parts and planning are unclear and hard to visualize before building. / hobbyists and students building hardware projects
- **Domain / idea type:** dev_tools + creative_media / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; generative_media; rag_or_search
- **Stack:** langs Python; JavaScript; frontend Next.js; React; NES.css; backend Flask; Flask-CORS; BeautifulSoup; db MongoDB; hosting Railway
- **Tech/APIs:** Google Gemini 2.5 Flash (text and image) (ai_model, core, sponsor); Snowflake Cortex (ai_model, core, sponsor); Veo 3.1 (ai_model, supporting); MongoDB Atlas (database, supporting, sponsor); Flask (framework, core); Next.js (framework, core); .tech domain (other, token, sponsor)
- **Sponsor APIs:** Google Gemini API; Snowflake Cortex; MongoDB Atlas | fit: Gemini 2.5 Flash selects parts from natural language and generates the assembled-product and instruction images, alongside Snowflake Cortex for instructions and firmware.
- **Repo:** public, commits 126 (before/in/after event: 0/126/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 12, writeup long, impact claims True (Reports cutting token counts and cost/latency about 70% and user wait from about 4 minutes to about 30 seconds.)
- **Notes:** Scraped 36k+ AliExpress parts into a 7k+ catalog; parallelizes Gemini (parts, images) with Snowflake Cortex (instructions, firmware); Veo-based assembly video; retro NES.css UI.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/product-creator-temp-name-conu-x) | [GitHub](https://github.com/chantalzhang/conuhacks26)

### CodeMafia  (ConUHacks X)

- **Prizes:** Druide – Best Use of Language (Presentation) [unknown]  (tier: sponsor_winner)
- **Pitch:** Among Us-style multiplayer game where 3-5 players fix broken Python code together while a hidden impostor sabotages it; tests run in-browser via Pyodide.
- **Problem / user:** Debugging practice is a chore; the team wanted to make it social and competitive as a deduction game. / programmers and students who enjoy coding games
- **Domain / idea type:** entertainment_games + education / entertainment_or_game
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; Python; frontend React; Vite; Zustand; Framer Motion; Monaco Editor; backend Partykit; db ; hosting Vercel
- **Tech/APIs:** Partykit (framework, core); Pyodide (framework, core); Monaco Editor (framework, core); Zustand (framework, supporting); Framer Motion (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 13, writeup long, impact claims False
- **Notes:** Partykit WebSockets sync lobby state; Monaco editor with collaborative editing; Pyodide (WebAssembly) runs Python tests client-side with no backend; emergency meetings and voting.
- **Team size:** 5 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; team_size inferred from bios; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/codemafia) | [GitHub](https://github.com/rayyankhan47/codemafia)

### D3CISION  (ConUHacks X)

- **Prizes:** D3 Security - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** SOC alert triage platform that correlates events into attack stories, scores them with XGBoost plus SHAP explanations, and offers a Gemini advisor that can act.
- **Problem / user:** Security analysts face thousands of alerts and cannot tell which to investigate first without context. / security operations center analysts
- **Domain / idea type:** safety_security + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind; Framer Motion; backend Python; db MongoDB Atlas; hosting 
- **Tech/APIs:** XGBoost (ai_model, core); SHAP (ai_model, core); Google Gemini 3 Flash (ai_model, core); ElevenLabs (ai_model, supporting); MongoDB Atlas (database, supporting); NetworkX (framework, core); scikit-learn (framework, supporting)
- **Sponsor APIs:**  | fit: Trained a triage model on D3 Security's challenge data and benchmarked it against the D3 rule-based logic.
- **Repo:** public, commits 69 (before/in/after event: 0/69/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 9, writeup long, impact claims True (Self-reported model metrics (AUC 0.989, F1 0.963) and a 142% improvement over the sponsor baseline.)
- **Notes:** Reports 98.9% AUC and +142% over D3's rule baseline; Gemini agent can isolate hosts or block traffic on request; ElevenLabs voice briefings; uncertainty flagging.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video
- **Links:** [Devpost](https://devpost.com/software/d3cision) | [GitHub](https://github.com/SohaibDM/ConuHacks-X-D3-Challenge)

### Desjardins ConUHacks Adventure Banking App  (ConUHacks X)

- **Prizes:** Desjardins - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Banking app with deposit/withdraw/invest that camouflages its colors from the camera, doubles as a compass, supports voice, and hides details when a second face appears.
- **Problem / user:** Desjardins Chameleon's Eye challenge: banking software that adapts to adventurous environments while staying secure. / mobile banking users on the move
- **Domain / idea type:** fintech_finance + safety_security / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / vision; speech_or_voice
- **Stack:** langs JavaScript; frontend HTML; CSS; Expo; backend ; db ; hosting 
- **Tech/APIs:** Expo (framework, core); Machine learning (unspecified) (ai_model, unclear)
- **Sponsor APIs:**  | fit: Addressed the Desjardins Chameleon's Eye challenge with camera-adaptive theme and onlooker privacy mode.
- **Repo:** public, commits 96 (before/in/after event: 4/92/0), README thin
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Planned a Raspberry Pi sensor setup, abandoned for lack of a display and pivoted to phone sensors; ML-based onlooker detection hides user details.
- **Team size:** 4 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; platforms; ML model unnamed
- **Links:** [Devpost](https://devpost.com/software/desjardins-conuhacks-adventure-banking-app) | [GitHub](https://github.com/MatthewBuzzetti/ConuHacks2026)

### Desjungles  (ConUHacks X)

- **Prizes:** Desjardins - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** React Native banking app that goes into secret text-to-speech mode when several faces watch, themes by ambient light, and shows a jungle scene while moving.
- **Problem / user:** Desjardins-themed challenge for a secure, inclusive, accessible banking app that adapts to the user's environment. / mobile banking users
- **Domain / idea type:** fintech_finance + accessibility / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / vision; speech_or_voice
- **Stack:** langs TypeScript; frontend React Native; Expo Go; backend Node.js; db MongoDB; hosting 
- **Tech/APIs:** BlazeFace (ai_model, core); Whisper (ai_model, supporting); MongoDB (database, supporting); Expo (framework, supporting); React Native (framework, core)
- **Sponsor APIs:**  | fit: Built an environment-adaptive banking app matching the Desjardins challenge theme.
- **Repo:** public, commits 66 (before/in/after event: 0/66/0), README solid
- **Demo/writeup:** video False, live none, screenshots 10, writeup medium, impact claims False
- **Notes:** Uses BlazeFace face detection for multi-viewer privacy mode, Whisper for voice, and device light and motion sensors; light/dark themes; transfers and send money flows.
- **Team size:** 5 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; MongoDB sponsor flag; team_size inferred from bios
- **Links:** [Devpost](https://devpost.com/software/desjungles) | [GitHub](https://github.com/cristina-trofimov/desjungles)

### Donair  (ConUHacks X)

- **Prizes:** Talsom - Sponsor Challenge [unknown]; Front Row Ventures - Investor Pitch Award [unknown]  (tier: sponsor_winner)
- **Pitch:** Agentic fundraising platform: Gemini finds likely donors from 110k+ historical gifts via vector search, runs a lead Kanban, and takes live Solana Pay donations at events.
- **Problem / user:** Event fundraising depends on slow manual donor research and big-ticket sponsors. / event organizers and fundraisers
- **Domain / idea type:** fintech_finance + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / rag_or_search; agent_or_tool_use; llm_chat; recommendation
- **Stack:** langs TypeScript; frontend Next.js 16; React 19; Tailwind CSS 4; Recharts; backend Express.js; Next.js API routes; db Supabase PostgreSQL with pgvector; hosting Vercel; Supabase
- **Tech/APIs:** Google Gemini 2.5 Flash (ai_model, core); Gemini text-embedding-004 (ai_model, core); Supabase pgvector (database, core); Solana Pay (payments, core); @solana/web3.js (payments, core); CharityCAN / Indiana University donation data (data_source, core); Recharts (framework, supporting)
- **Sponsor APIs:**  | fit: Won Talsom challenge and Front Row Ventures Investor Pitch Award; page does not describe the briefs or name sponsor products.
- **Repo:** public, commits 53 (before/in/after event: 0/53/0), README solid
- **Demo/writeup:** video None, live not_checked, screenshots 6, writeup long, impact claims True (States a dataset of over 110,000 historical donations and a donor scoring formula; no outcome numbers.)
- **Notes:** RAG over a CharityCAN/Indiana University donation dataset in Supabase pgvector, agent tool-calling with web search, ethics flags on leads, and Solana mainnet transaction monitoring with QR codes.
- **Team size:** 3 | **Confidence:** medium | unverified: team_size; has_demo_video; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/flowstate-7ihg10) | [GitHub](https://github.com/forkiron/donair)

### Dr.Bob  (ConUHacks X)

- **Prizes:** Dialogue - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Chat-based AI medical triage assistant with a saved medical profile, trusted-clinic whitelist, geolocated clinic finding and a glassmorphic light/dark UI.
- **Problem / user:** Healthcare portals and clinic phone queues are tedious when sick; people want a calm, frictionless triage tool. / patients seeking symptom guidance and nearby clinics
- **Domain / idea type:** health_wellness / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; JavaScript; frontend HTML5; CSS3; Vanilla JavaScript; backend Flask; db ; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); Flask (framework, core); Browser Geolocation API (maps_geo, supporting)
- **Sponsor APIs:**  | fit: Triage chat that connects users to nearby clinics, fitting the Dialogue virtual-care theme; no Dialogue API use is stated.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Vanilla JS front end styled as a mobile app frame with an animated theme engine; booking is not integrated and listed as future work.
- **Team size:** 4 | **Confidence:** medium | unverified: stack_database; has_demo_video; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/dr-bob) | [GitHub](https://github.com/theganders/Dr.Bob)

### Drop'edthe.tech  (ConUHacks X)

- **Prizes:** Deck - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** A very fast bot that calls backend APIs to drop university courses instantly, packaged as an Electron app plus a download site.
- **Problem / user:** Dropping/adding courses on a registration site is slow and rate-limited; the team targeted the Deck challenge with a speed bot. / university students
- **Domain / idea type:** education + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** desktop; web / False / False
- **Stack:** langs JavaScript; frontend React; HTML; CSS; backend ; db ; hosting 
- **Tech/APIs:** Puppeteer (framework, core); Electron (framework, core); React (framework, supporting)
- **Sponsor APIs:**  | fit: Built a browser/web automation bot for the Deck challenge, which is related to automation of web tasks (challenge details not on page).
- **Repo:** public, commits 39 (before/in/after event: 0/37/2), README detailed
- **Demo/writeup:** video None, live not_checked, screenshots 5, writeup medium, impact claims False
- **Notes:** Works against a demo registration site, not the real one; uses Puppeteer to show results and tackles captchas and rate limits.
- **Team size:** 6 | **Confidence:** medium | unverified: team_size; has_demo_video; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/drop-edthe-tech) | [GitHub](https://github.com/spilledthoughts/ConUHacks)

### FOMO  (ConUHacks X)

- **Prizes:** [HackConcordia] Best Beginner (All team members must be first-time hackers) [unknown]  (tier: track_winner)
- **Pitch:** iOS map app showing busy hotspots, letting shy users read local chatter and ask location-tied questions before joining in.
- **Problem / user:** People stay isolated and don't know where gatherings happen or how to step in. / isolated or shy young adults
- **Domain / idea type:** social_community + mobility_transport / new_category
- **Platforms / hardware / AI:** mobile_ios / False / False
- **Stack:** langs Swift; frontend Xcode; Swift; backend Firebase; db Firestore; hosting Firebase
- **Tech/APIs:** Firebase (cloud, core); Firestore (database, core); Swift (framework, core); ChatGPT (coding help) (ai_model, token); Map API (maps_geo, core)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Native Swift iOS app on Firebase/Firestore with live location and user-flow tracking; team of first-time hackers, some without Macs.
- **Team size:** 3 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; map API unnamed; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/fomo-91dnsu) | [GitHub](https://github.com/yansvassi/FOMO)

### HealthMe  (ConUHacks X)

- **Prizes:** MentorMates - Sponsor Challenge [unknown]; Dialogue - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Voice-first health assistant that chats with context, maps nearby clinics, and phones a clinic via an AI agent to book an appointment with a live transcript.
- **Problem / user:** Sick people must navigate clinic portals and phone queues to find care and book appointments. / patients seeking clinic appointments
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs TypeScript; Python; JavaScript; frontend React; Tailwind CSS; backend Flask; Express.js; Node.js; Socket.io; db Firebase Firestore; hosting GCP
- **Tech/APIs:** ElevenLabs (ai_model, core); Google Gemini (ai_model, core); Twilio (telecom, core); Mapbox (maps_geo, supporting); Firebase/Firestore (database, supporting); Socket.io (framework, supporting)
- **Sponsor APIs:**  | fit: Virtual-care style assistant that finds clinics and books appointments, matching the Dialogue (virtual health) and MentorMates challenges at a thematic level; page does not name sponsor products.
- **Repo:** public, commits 122 (before/in/after event: 0/107/15), README none
- **Demo/writeup:** video None, live none, screenshots None, writeup long, impact claims False
- **Notes:** Places real outbound phone calls through an ElevenLabs voice agent and shows the live call transcript via Socket.io; includes an emergency calling feature.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots; has_demo_video; sponsor_fit_note; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/healthme-cshbay) | [GitHub](https://github.com/thomasballarddev/ConUHacksX)

### I LOST IT  (ConUHacks X)

- **Prizes:** SAP - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Multimodal AI lost-and-found: users search found items by text or photo, and Gemini generates ownership-verification questions to block false claims.
- **Problem / user:** Manual lost-and-found bins and descriptions make it hard for owners to find items and for staff to verify claims. / campus/venue lost-and-found staff and owners
- **Domain / idea type:** retail_consumer + ai_agents_infra / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; rag_or_search; llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind; shadcn/ui; Framer Motion; backend FastAPI; db Milvus; Supabase; hosting Vercel
- **Tech/APIs:** DINOv2 (ai_model, core); CLIP (ai_model, core); Sentence Transformers (ai_model, core); Gemini 2.0 Flash (ai_model, core); Milvus (database, core); Supabase (database, supporting); FastAPI (framework, core); Next.js (framework, supporting)
- **Sponsor APIs:**  | fit: Built an AI-assisted lost-and-found matching platform for the SAP challenge (challenge brief not on page); SAP products are not mentioned.
- **Repo:** public, commits 25 (before/in/after event: 0/25/0), README solid
- **Demo/writeup:** video None, live not_checked, screenshots 4, writeup long, impact claims False
- **Notes:** Fuses four embedding approaches (DINOv2, CLIP image, CLIP caption, sentence text) across four Milvus collections with weighted scoring; staff portal with collections by location.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/i-lost-it) | [GitHub](https://github.com/ayoubm85/ilostit)

### JungleBank  (ConUHacks X)

- **Prizes:** 3rd Place - General [3rd]; Desjardins - Sponsor Challenge [unknown]  (tier: overall_top3)
- **Pitch:** Jungle-themed banking game teaching kids finance through expense tracking, interest, stock investing and Godot mini-games, with voice control and a Gemini AI banker.
- **Problem / user:** Children and young teens need an engaging way to learn about money, expenses, interest and investing. / children and young teens
- **Domain / idea type:** education + fintech_finance / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice
- **Stack:** langs JavaScript; GDScript; frontend React; Godot; HTML; CSS; backend Express; db ; hosting Render
- **Tech/APIs:** Gemini (ai_model, supporting); ElevenLabs (ai_model, supporting); Godot (framework, core); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 158 (before/in/after event: 0/155/3), README solid
- **Demo/writeup:** video False, live not_checked, screenshots 6, writeup medium, impact claims False
- **Notes:** Combines a React/Express banking UI with Godot games; scenes shift day/night with real time; voice activation via ElevenLabs/Gemini for accessibility. Prize list also includes Desjardins challenge, not shown as badge.
- **Team size:** 4 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; second prize (Desjardins) not shown as badge on page; Gemini/ElevenLabs depth; voice activation tech
- **Links:** [Devpost](https://devpost.com/software/junglebank) | [GitHub](https://github.com/afsans1/JungleBank)

### llm in chrome  (ConUHacks X)

- **Prizes:** Deck - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** A Chrome-based tool for using an LLM in the browser; the Devpost text is only a note about repeated submission problems.
- **Problem / user:** Not stated on the page. / browser users (inferred)
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** browser_extension / False / llm_chat
- **Stack:** langs JavaScript; frontend HTML; CSS; backend ; db ; hosting 
- **Sponsor APIs:**  | fit: Won the Deck sponsor challenge; page gives no explanation.
- **Repo:** public, commits 314 (before/in/after event: 0/20/294), README detailed
- **Demo/writeup:** video None, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Devpost writeup contains no project description, only a note that the account was repeatedly banned on submitting the text; details are likely in the repo.
- **Team size:** 1 | **Confidence:** low | unverified: one_line_pitch; problem_statement; target_user; domain_primary; idea_type; platforms; ai_used; ai_types; sponsor_fit_note; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/test-mszpgt) | [GitHub](https://github.com/hanzili/llm-in-chrome)

### Love At First Bite  (ConUHacks X)

- **Prizes:** [MLH] Best .Tech Domain Name [unknown]  (tier: sponsor_winner)
- **Pitch:** Restaurant finder where an LLM turns a plain-English request into Yelp searches and users swipe poster-style cards, ranked by a weighted score.
- **Problem / user:** Groups suffer decision fatigue picking dinner, and Yelp or Google Maps give too much information to decide quickly. / groups and couples choosing where to eat
- **Domain / idea type:** food_nutrition + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; recommendation
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind CSS; Framer Motion; backend Next.js API routes; Zod; db ; hosting Vercel
- **Tech/APIs:** OpenAI GPT-4o-mini via OpenRouter (ai_model, core); Yelp Fusion API (data_source, core); Framer Motion (framework, supporting); Next.js (framework, core); Zod (framework, supporting); .tech domain (loveatfirstbite.tech) (other, core, sponsor)
- **Sponsor APIs:** .Tech Domains | fit: Targeted the MLH .Tech domain prize by hosting the app at loveatfirstbite.tech; the page does not discuss the domain beyond the live link.
- **Repo:** public, commits 67 (before/in/after event: 9/58/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims False
- **Notes:** GPT-4o-mini via OpenRouter maps vibe words to Yelp categories as a validated JSON SearchSpec; Framer Motion swipe physics; custom ranking weighting rating, distance and price.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/love-at-first-bite-kt3zca) | [GitHub](https://github.com/Miro-vk/concordia-hackathon.git)

### Nova Legends  (ConUHacks X)

- **Prizes:** Druide – Best Use of Language (Presentation) [unknown]  (tier: sponsor_winner)
- **Pitch:** Multiplayer 2D top-down knight shooter on a 100% custom Java engine with server-authoritative networking on Vultr, spatial audio, chat and map generator.
- **Problem / user:** Wanted to show a custom-built engine can give tighter competitive gameplay than a generic one. / competitive multiplayer gamers
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / False / False
- **Stack:** langs Java; frontend ; backend Java sockets; db ; hosting Vultr
- **Tech/APIs:** Vultr (cloud, core, sponsor); Java sockets (framework, core); Custom game engine (framework, core)
- **Sponsor APIs:** Vultr | fit: Prize for use of language; project is an engine and game written from scratch, hosted on Vultr servers.
- **Repo:** public, commits 3 (before/in/after event: 0/3/0), README none
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Custom physics, animation, camera, audio and UI services written from scratch in Java; authoritative server on Vultr cloud; custom procedural map generator.
- **Team size:** 2 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; Vultr sponsor flag; Druide prize link to project unclear
- **Links:** [Devpost](https://devpost.com/software/nova-legends) | [GitHub](https://github.com/tahakhalfi/EHC-NOVA_LEGENDS)

### Nursie  (ConUHacks X)

- **Prizes:** [MLH] Best Use of ElevenLabs [unknown]  (tier: sponsor_winner)
- **Pitch:** On-premises AI nurse assistant for long-term care that detects falls with mmWave radar and a floor vibration mat, tracks vitals and presence, and offers a voice interface.
- **Problem / user:** Unwitnessed falls and staff shortages in Quebec long-term care homes cause long delays before help arrives and serious complications. / long-term care staff and residents
- **Domain / idea type:** health_wellness + accessibility / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / speech_or_voice; agent_or_tool_use; predictive_ml
- **Stack:** langs Python; C++; JavaScript; frontend React; backend FastAPI; Flask; ROS2; db MongoDB; hosting 
- **Tech/APIs:** ElevenLabs (ai_model, core, sponsor); mmWave radar (hardware_part, core); Floor vibration mat (hardware_part, core); ROS2 (framework, supporting); MongoDB (database, supporting); FastAPI (framework, supporting); React (framework, supporting)
- **Sponsor APIs:** ElevenLabs | fit: Used ElevenLabs to give the fall-detection assistant a voice interface for residents and caregivers.
- **Repo:** public, commits 48 (before/in/after event: 0/48/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims True (Quotes Canadian fall statistics: 47% rise in older-adult fall hospitalizations 2008-2019 and 5,581 fall deaths in 2019.)
- **Notes:** Sensor-fusion system with mmWave radar, vibration mat, door and presence sensors and smartwatch vitals on a local network using ROS2; the writeup contains unresolved citation placeholder text.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/nursie) | [GitHub](https://github.com/rappphg/Nursie)

### One-Man-Crew  (ConUHacks X)

- **Prizes:** SAP - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Human-in-the-loop lost-and-found tool that ranks the top five matches from image and text embeddings for admins to review and confirm.
- **Problem / user:** Students struggle to recover lost items even when found; automation alone risks false matches and fraud. / university lost-and-found admins and students
- **Domain / idea type:** retail_consumer + education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; rag_or_search
- **Stack:** langs Python; JavaScript; frontend React; HTML; CSS; backend Flask; db JSON files; hosting 
- **Tech/APIs:** Gemini API (ai_model, supporting); Image/text embeddings with cosine similarity (ai_model, core); Flask (framework, core); pandas (framework, supporting); SMTP (other, supporting)
- **Sponsor APIs:**  | fit: Built an AI-assisted lost-and-found matcher for the SAP challenge (brief not on page); SAP products are not mentioned.
- **Repo:** public, commits 25 (before/in/after event: 0/23/2), README solid
- **Demo/writeup:** video None, live none, screenshots 3, writeup medium, impact claims False (Impact section is qualitative only, no numbers.)
- **Notes:** Solo build that deliberately keeps admins in control of clarification questions and ownership confirmation; sends emails via SMTP.
- **Team size:** 1 | **Confidence:** medium | unverified: stack_database; has_demo_video; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/one-man-crew) | [GitHub](https://github.com/NawarTurk/HACK_human-in-loop-lostfound)

### PETER the ProtectoBot  (ConUHacks X)

- **Prizes:** [HackConcordia] Best Hardware [unknown]  (tier: track_winner)
- **Pitch:** Two-wheeled sentry robot with ESP32-S3 camera, custom-soldered speaker amp and ResNet model that predicts one second ahead to offset video lag; teleop, gesture-follow and autonomous modes.
- **Problem / user:** Wi-Fi video lag makes real-time robot control hard; team wanted a full-stack robotics proof of concept for home sentry use. / homeowners wanting a security robot
- **Domain / idea type:** safety_security + ai_agents_infra / hardware_gadget
- **Platforms / hardware / AI:** hardware; desktop / True / vision; predictive_ml
- **Stack:** langs Python; C++; frontend ; backend PyTorch; CUDA; db ; hosting 
- **Tech/APIs:** ESP32-S3 Sense (hardware_part, core); ResNet (PyTorch) (ai_model, core); Fusion 360 (other, supporting); Op-amp speaker circuit (hardware_part, supporting); UDP video streaming (other, supporting)
- **Sponsor APIs:**  | fit: Awarded the HackConcordia hardware prize for a fully custom robot with CAD chassis, soldered audio and on-robot ML integration.
- **Repo:** public, commits 44 (before/in/after event: 0/43/1), README thin
- **Demo/writeup:** video False, live none, screenshots 12, writeup long, impact claims False
- **Notes:** CAD-designed 3D-printed chassis, hand-built op-amp speaker circuit that accidentally sounds like a diesel idle, imitation-learning ResNet trained on maze data collected during event.
- **Team size:** 5 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; team_size inferred from bios
- **Links:** [Devpost](https://devpost.com/software/peter-the-protecto-bot) | [GitHub](https://github.com/aburiz/Conuhacks2026)

### Pinscher  (ConUHacks X)

- **Prizes:** 2nd Place - General Challenge [2nd]  (tier: overall_top3)
- **Pitch:** Hands-free Mac controller using camera hand gestures and offline voice commands, plus Gemini features that turn recorded sessions into slide decks and summaries.
- **Problem / user:** Repetitive manual clicking and typing makes computing tedious and inaccessible for users with limited mobility. / Mac users, including those with limited mobility
- **Domain / idea type:** accessibility + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** desktop / False / vision; speech_or_voice; llm_chat; agent_or_tool_use
- **Stack:** langs Python; JavaScript; frontend Electron; React; backend Python; OpenCV; Vosk; db ; hosting 
- **Tech/APIs:** Gemini 2.0 Flash (ai_model, core); OpenCV (framework, core); Vosk (ai_model, core); Electron (framework, supporting); Marp CLI (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 125 (before/in/after event: 0/125/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Pinch-to-click via OpenCV hand tracking, Vosk offline speech, Gemini 2.0 Flash intent parsing and video summarization to Marp slides; Electron dashboard; macOS-only.
- **Team size:** 4 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; Gemini sponsor flag
- **Links:** [Devpost](https://devpost.com/software/pinscher) | [GitHub](https://github.com/katkes/ConUHacksX)

### retro secrets  (ConUHacks X)

- **Prizes:** [MLH] Best Use of Solana [unknown]  (tier: sponsor_winner)
- **Pitch:** Social platform for AI-generated ASCII art NFTs that hide encrypted messages in character colors, with art and ownership recorded on Solana.
- **Problem / user:** Team wanted a more playful kind of NFT: art that doubles as a steganographic message carrier shared among friends. / social media users and NFT hobbyists
- **Domain / idea type:** creative_media + social_community / creative_tool
- **Platforms / hardware / AI:** web / False / generative_media; llm_chat
- **Stack:** langs TypeScript; frontend Next.js; backend ; db MongoDB; hosting 
- **Tech/APIs:** Solana (other, core, sponsor); Phantom wallet (auth, supporting); Google Gemini (ai_model, core); AES encryption (other, core); MongoDB (database, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** Solana | fit: Stored each ASCII artwork on the Solana blockchain to prove creation time and ownership, with Phantom wallet verification.
- **Repo:** public, commits 65 (before/in/after event: 0/65/0), README solid
- **Demo/writeup:** video True, live none, screenshots 28, writeup short, impact claims False
- **Notes:** Hides messages by LSB-encoding into ASCII character colors with custom AES encryption; verifies authenticity by re-hashing the ASCII; Phantom wallet integration and Gemini-generated source art.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/retro-secrets) | [GitHub](https://github.com/deltag0/ConUHacks)

### Scale Or Fail  (ConUHacks X)

- **Prizes:** [MLH] Best Use of Vultr [unknown]  (tier: sponsor_winner)
- **Pitch:** Voice-first system design interview practice: users explain solutions aloud, transcription feeds Snowflake-hosted grading agents with RAG, hosted on Vultr.
- **Problem / user:** System design interviews are rising but few resources simulate high-pressure verbal practice. / software engineers preparing for system design interviews
- **Domain / idea type:** education + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search; speech_or_voice
- **Stack:** langs C#; Python; TypeScript; frontend Angular; TypeScript; backend .NET 10; Python runner; db Snowflake; MongoDB; hosting Vultr; Docker; GitHub Actions
- **Tech/APIs:** Vultr (compute, container registry, object storage, serverless inference) (cloud, core, sponsor); Snowflake (agent procedures, RAG) (ai_model, core, sponsor); Auth0 (auth, supporting, sponsor); Azure Speech to Text (ai_model, supporting); ElevenLabs (ai_model, supporting); Angular (framework, supporting); .NET 10 (framework, core)
- **Sponsor APIs:** Vultr; Snowflake; Auth0 | fit: Hosted all services on Vultr (VM, container registry, object storage, serverless GPU inference for text-to-speech) with Docker CI/CD and Watchtower.
- **Repo:** public, commits 141 (before/in/after event: 0/141/0), README none
- **Demo/writeup:** video False, live not_checked, screenshots 4, writeup long, impact claims True (Cites a HackerRank-sourced claim that system design interview invitations rose over 100 percent since 2024.)
- **Notes:** Six Snowflake agent procedures plus RAG over system-design PDFs stored in Vultr Object Storage; C# .NET 10 API; two TTS providers raced for speed; Watchtower auto-deploys Docker images.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/system-design-90lx1y) | [GitHub](https://github.com/nic5694/ScaleOrFail)

### Schooless  (ConUHacks X)

- **Prizes:** Deck - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** An education platform with an Angular front end and Python/MongoDB back end that tracks learner progress; the page gives little detail.
- **Problem / user:** Not stated on the page; the writeup only describes a generic usable, scalable learning app. / students/learners (inferred)
- **Domain / idea type:** education / other
- **Platforms / hardware / AI:** web / False / None
- **Stack:** langs Python; TypeScript; frontend AngularJS; backend Python; db MongoDB; hosting Amazon EC2
- **Tech/APIs:** AngularJS (framework, core); MongoDB (database, core); Amazon EC2 (cloud, supporting); CLIP (ai_model, unclear)
- **Sponsor APIs:**  | fit: Won the Deck sponsor challenge; page does not explain how the project relates to Deck.
- **Repo:** public, commits 73 (before/in/after event: 0/73/0), README solid
- **Demo/writeup:** video None, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Devpost writeup is a single how-built paragraph; CLIP is listed in Built With but its use is not explained. Sponsor challenge is Deck.
- **Team size:** 3 | **Confidence:** low | unverified: one_line_pitch; problem_statement; target_user; domain_primary; idea_type; ai_used; sponsor_fit_note; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/schooless) | [GitHub](https://github.com/Luchiga19/conuhacks2026)

### SherLostHolmes  (ConUHacks X)

- **Prizes:** SAP - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Gamified lost-and-found: semantic AI matching, blurred 'suspect' lineup with a decoy, AI interrogation questions, and ESP32 smart lockers for pickup.
- **Problem / user:** Reclaiming lost items is bureaucratic and open to false claims; the team wanted a more engaging, fraud-resistant process. / university students and lost-and-found admins
- **Domain / idea type:** retail_consumer + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; TypeScript; frontend Next.js 14; Tailwind CSS; Framer Motion; backend FastAPI; LangChain; OpenRouter; db MongoDB Atlas; hosting 
- **Tech/APIs:** LangChain (framework, core); OpenRouter (ai_model, core); MongoDB Atlas (database, core); Cloudinary (other, supporting); Clerk (auth, supporting); XIAO ESP32-S3 (hardware_part, core); Servo motor (hardware_part, core)
- **Sponsor APIs:**  | fit: Built an AI lost-and-found system with hardware lockers for the SAP challenge (brief not on page); SAP products are not mentioned.
- **Repo:** public, commits 49 (before/in/after event: 0/25/24), README none
- **Demo/writeup:** video None, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Includes a physical smart locker prototype (XIAO ESP32-S3, servo lock, I2C keyboard for one-time codes), a decoy-item fraud check, and a slot-machine game for unclaimed items.
- **Team size:** 4 | **Confidence:** medium | unverified: team_size; has_demo_video; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/sherlostholmes) | [GitHub](https://github.com/AndrewKaranu/SherLostHolmes)

### Socratic  (ConUHacks X)

- **Prizes:** [MLH] Best Use of MongoDB Atlas [unknown]  (tier: sponsor_winner)
- **Pitch:** VS Code extension that mentors by guiding questions instead of giving answers, with adjustable help levels, AI teachers with voices, skill tracking and RAG context.
- **Problem / user:** Coding assistants hand over answers, which can hinder real learning and problem-solving skill. / students and junior developers
- **Domain / idea type:** education + dev_tools / dev_tool
- **Platforms / hardware / AI:** desktop / False / llm_chat; rag_or_search; speech_or_voice
- **Stack:** langs TypeScript; JavaScript; frontend VS Code Webview API; backend ; db MongoDB Atlas; hosting 
- **Tech/APIs:** MongoDB Atlas (database, core, sponsor); Google Gemini (ai_model, core); ElevenLabs (ai_model, supporting, sponsor); VS Code extension API (framework, core)
- **Sponsor APIs:** MongoDB Atlas; ElevenLabs | fit: Used MongoDB cloud storage to sync user skill progress and mentor settings across devices.
- **Repo:** public, commits 102 (before/in/after event: 0/101/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 19, writeup short, impact claims False
- **Notes:** Sidebar webview extension with a marketplace-style set of mentor personalities and ElevenLabs voices, plus MongoDB-synced progress and sponsor skill packages.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/socratic-xu768i) | [GitHub](https://github.com/GitExcited/Socratic)

### TheGardens  (ConUHacks X)

- **Prizes:** Desjardins - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Four-part system: ESP32 IMU haptic glove controlling a desktop treasure game, a Flutter banking app reacting to in-game weather, voice commands, and a relay server.
- **Problem / user:** Gesture and voice control for people who cannot easily use keyboards and mice, framed by the Desjardins challenge. / users unable to use standard keyboards and mice
- **Domain / idea type:** accessibility + fintech_finance / hardware_gadget
- **Platforms / hardware / AI:** hardware; desktop; mobile_cross / True / None
- **Stack:** langs C++; Dart; Python; TypeScript; JavaScript; frontend Flutter; HTML5; CSS3; backend Python; db SQLite; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); IMU sensors (hardware_part, core); Flutter (framework, core); SQLite (database, supporting)
- **Sponsor APIs:**  | fit: Pivoted from a Jarvis-style idea to a weather-reactive banking app and game for the Desjardins challenge.
- **Repo:** public, commits 40 (before/in/after event: 0/35/5), README detailed
- **Demo/writeup:** video False, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Glove IMU math projects 3D acceleration to 2D cursor motion; DIY flex sensors failed; Bluetooth/Wi-Fi link to a shared server relaying between game and Flutter app.
- **Team size:** 5 | **Confidence:** high | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video; ai_used (voice commands mentioned, no AI stack listed); team_size inferred from bios
- **Links:** [Devpost](https://devpost.com/software/thegardens) | [GitHub](https://github.com/MinhVo2005/ConuHack)

### Thornmail  (ConUHacks X)

- **Prizes:** D3 Security - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Security log triage that groups activity into explainable attack stories, scores risk with rules, and uses a local Llama model to highlight key details; analyst decides.
- **Problem / user:** Real threats are buried under thousands of noisy alerts, and analysts lack connected context. / security operations analysts
- **Domain / idea type:** safety_security + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; backend FastAPI; Uvicorn; db ; hosting 
- **Tech/APIs:** Ollama + Llama 3 (ai_model, supporting); FastAPI (framework, core); Next.js (framework, core); pandas (framework, supporting); NumPy (framework, supporting)
- **Sponsor APIs:**  | fit: Built an alert-correlation and risk-scoring pipeline for the D3 Security challenge; page does not name D3 products used.
- **Repo:** public, commits 18 (before/in/after event: 0/16/2), README detailed
- **Demo/writeup:** video None, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Uses a locally run Llama 3 via Ollama as a support tool only; risk scoring is rule-based and conservative, aimed at auditability.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/sentinel-2sjz9f) | [GitHub](https://github.com/meuhcow/Thornmail)

### ViniClip  (ConUHacks X)

- **Prizes:** 1st Place - General Challenge [1st]  (tier: overall_top3)
- **Pitch:** Browser recorder that edits video live while you speak, trimming pauses and bad takes via speech-to-text plus an OpenAI tool-calling agent and ffmpeg, with optional Reels posting.
- **Problem / user:** Recording clean video means re-takes and long manual editing to cut mistakes and pauses. / short-form video creators
- **Domain / idea type:** creative_media + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs TypeScript; Python; frontend React; Vite; backend FastAPI; ffmpeg; db ; hosting 
- **Tech/APIs:** OpenAI Responses API (ai_model, core); Moonshine (ai_model, core); ffmpeg (other, core); FastAPI (framework, supporting); React (framework, supporting); Instagram Reels posting (other, token)
- **Sponsor APIs:** 
- **Repo:** public, commits 96 (before/in/after event: 0/96/0), README none
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Streams browser audio/video over WebSocket to FastAPI; Moonshine transcribes, an LLM picks cuts through function calls, ffmpeg stitches segments in near real time.
- **Team size:** 4 | **Confidence:** medium | unverified: event dates not found; sponsor flags; n_screenshots; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/viniclip) | [GitHub](https://github.com/mahutt/ViniClip)

### Vulkan Tank Online  (ConUHacks X)

- **Prizes:** Beenox - Sponsor Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** A top-down multiplayer tank game written in C++ on raw Vulkan, with LAN/internet play via Valve's GameNetworkingSockets.
- **Problem / user:** No problem stated; a technical exercise in building a game without an engine. / gamers / graphics programming enthusiasts
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / False / False
- **Stack:** langs C++; C; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Vulkan (framework, core); GameNetworkingSockets (framework, core); Assimp (framework, supporting); CMake (other, supporting); ZeroTier (other, supporting)
- **Sponsor APIs:**  | fit: Real-time 3D multiplayer game built in C++ for the Beenox (game studio) challenge; page does not describe the brief.
- **Repo:** public, commits 25 (before/in/after event: 0/24/1), README solid
- **Demo/writeup:** video None, live none, screenshots 3, writeup medium, impact claims False
- **Notes:** Avoids a game engine; Vulkan renderer with shadow mapping and Assimp model loading, cross-platform Windows/macOS multiplayer, ZeroTier used to get around hackathon Wi-Fi client isolation.
- **Team size:** 2 | **Confidence:** medium | unverified: has_demo_video; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/topdown-tank-online) | [GitHub](https://github.com/benyoon1/conuhacksX)
