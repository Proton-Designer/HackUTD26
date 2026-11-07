# Hacklytics: project cards (25 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## Hacklytics - 2025: Jurassic Age

### Banana Search  (Hacklytics - 2025: Jurassic Age)

- **Prizes:** Second in Finance [2nd]  (tier: track_winner)
- **Pitch:** Meal-planning app that generates a recipe, finds missing ingredients from a fridge photo, and compares grocery store prices for the shopping list.
- **Problem / user:** Rising food prices make it hard to cook desired meals on budget without overspending or wasting food. / budget-conscious home cooks
- **Domain / idea type:** food_nutrition + fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; vision; agent_or_tool_use
- **Stack:** langs TypeScript; Python; Node.js; frontend Next.js; React; backend Node.js; Python; LangChain; Langflow; db Supabase; hosting AWS
- **Tech/APIs:** LangChain (framework, core); Langflow (framework, core); Supabase (auth, supporting); Grocery price APIs (unnamed) (data_source, core); Amazon Web Services (cloud, unclear); Yahoo Finance (data_source, unclear)
- **Sponsor APIs:**  | fit: Finance-track entry focused on grocery budgeting and price comparison.
- **Repo:** public, commits 82 (before/in/after event: 82/0/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims False
- **Notes:** Combines LLM recipe generation, fridge-image ingredient detection and external grocery price APIs; built with LangChain/Langflow agents and Supabase auth with Google and GitHub login.
- **Team size:** 4 | **Confidence:** high | unverified: sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/banana-search-ueb89p) | [GitHub](https://github.com/SarveshGade/banana_search)

### Basketball Positioning Neural Network and Kmean Cluster  (Hacklytics - 2025: Jurassic Age)

- **Prizes:** Third in Sports [3rd]  (tier: track_winner)
- **Pitch:** Basketball analytics notebook using KMeans to classify player positions and regression to study player-versus-defender matchup statistics.
- **Problem / user:** Matchup-based stats (how a player does against a specific defender) are underrepresented in NBA analysis. / basketball fans and analysts
- **Domain / idea type:** entertainment_games / data_or_analytics
- **Platforms / hardware / AI:** other / False / predictive_ml
- **Stack:** langs Python; frontend ; backend ; db ; hosting Google Colab
- **Tech/APIs:** KMeans clustering (ai_model, core); Linear regression (ai_model, core); Google Colab (cloud, supporting); Hackathon-provided basketball CSV (data_source, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 3 (before/in/after event: 3/0/0), README thin
- **Demo/writeup:** video True, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Solo-style learning project in Colab using the CSV provided by the hackathon; KMeans and linear regression despite 'neural network' in the title; no how-we-built section filled in.
- **Team size:** 2 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/basketball-positioning-neural-network-and-kmean-cluster) | [GitHub](https://github.com/jsohn0824/Hacklytics-submission.git)

### Cipher AI  (Hacklytics - 2025: Jurassic Age)

- **Prizes:** Third in Cybersecurity [3rd]  (tier: track_winner)
- **Pitch:** Steganography tool that hides a secret message inside natural-sounding generated text, returning a password-protected key file.
- **Problem / user:** Obvious encryption like RSA gets users flagged under censorship; covert messages that look like normal speech avoid detection. / activists and people under surveillance
- **Domain / idea type:** safety_security / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; generative_media
- **Stack:** langs Python; JavaScript; frontend React; backend Flask; NLTK; Pandas; NumPy; db ; hosting 
- **Tech/APIs:** OpenAI GPT-4o (ai_model, core); Sentiment140 dataset (data_source, core); NLTK (framework, supporting); Flask (framework, supporting); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 57 (before/in/after event: 57/0/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Key words picked by frequency from a Sentiment140 tweet subset, then GPT-4o builds the dictionary and encoded cover text; decryption key delivered as a password-protected JSON.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/cipher-ai) | [GitHub](https://github.com/vprahalad/Hacklytics2025)

### Deqo  (Hacklytics - 2025: Jurassic Age)

- **Prizes:** Second in Cybersecurity [2nd]  (tier: track_winner)
- **Pitch:** Decentralized marketplace where people rent out idle computing power; buyers upload Docker jobs, lenders run them via a CLI, with blockchain-style verification.
- **Problem / user:** Cloud compute is expensive while personal and institutional machines sit idle. / AI researchers and small teams needing compute; owners of idle machines
- **Domain / idea type:** dev_tools + ai_agents_infra / new_category
- **Platforms / hardware / AI:** web; cli / False / recommendation
- **Stack:** langs TypeScript; Python; SQL; frontend Next.js; Tailwind CSS; backend FastAPI; Uvicorn; Docker; db Supabase; hosting AWS EC2; Netlify
- **Tech/APIs:** AWS ECR (cloud, core); AWS S3 (cloud, core); Supabase (database, core); Docker (other, core); AES-GCM encryption (other, supporting); Blockchain verification (other, unclear)
- **Sponsor APIs:**  | fit: Entered under the cybersecurity track; writeup stresses encrypted transfer, Docker isolation and verified computation.
- **Repo:** public, commits 118 (before/in/after event: 118/0/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims False
- **Notes:** Docker images moved through AWS ECR and S3 with AES-GCM encryption; CLI auto-runs jobs on a lender's schedule; verification layer described as blockchain-based.
- **Team size:** 4 | **Confidence:** high | unverified: sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/deqo) | [GitHub](https://github.com/vid277/hacklytics25)

### MedX  (Hacklytics - 2025: Jurassic Age)

- **Prizes:** Second in Healthcare [2nd]  (tier: track_winner)
- **Pitch:** Mobile medication tracker with barcode logging, Gemini drug-interaction checks, a health chatbot, journaling and shareable AI-generated medication reports.
- **Problem / user:** People struggle to track medications, spot drug interactions and get reliable health guidance quickly. / patients managing multiple medications
- **Domain / idea type:** health_wellness + ai_agents_infra / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / llm_chat; vision
- **Stack:** langs TypeScript; JavaScript; frontend React Native; Expo; backend Firebase; db Firebase; hosting 
- **Tech/APIs:** Gemini API (ai_model, core, sponsor); OpenFDA API (data_source, core); Firebase (cloud, supporting); Expo / React Native (framework, core); Barcode scanning (other, supporting)
- **Sponsor APIs:** Gemini API | fit: Healthcare-track entry using Gemini for interaction analysis and OpenFDA for drug data.
- **Repo:** public, commits 292 (before/in/after event: 292/0/0), README solid
- **Demo/writeup:** video True, live none, screenshots 8, writeup long, impact claims False
- **Notes:** Barcode scan queries OpenFDA to identify drugs; Gemini rates interactions on severity tiers; Expo React Native app with Firebase.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags
- **Links:** [Devpost](https://devpost.com/software/medx-d7tle6) | [GitHub](https://github.com/hxxtsxxh/MedX)

### MIR.AI - AI Driven, Efficient MRI Super-Resolution  (Hacklytics - 2025: Jurassic Age)

- **Prizes:** Third in Healthcare [3rd]  (tier: track_winner)
- **Pitch:** Unpaired image-translation model that upscales lower-field MRI scans toward higher-quality resolution, with a React frontend.
- **Problem / user:** High-quality 3T MRI is costly, limiting access in resource-limited regions. / hospitals and clinics with limited imaging hardware
- **Domain / idea type:** health_wellness / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; generative_media
- **Stack:** langs Python; TypeScript; frontend React; TypeScript; backend PyTorch Lightning; Python; db ; hosting Google Colab
- **Tech/APIs:** PyTorch Lightning (framework, core); Contrastive Unpaired Translation (ai_model, core); Google Colab (cloud, supporting); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 79 (before/in/after event: 79/0/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Uses Contrastive Unpaired Translation in PyTorch Lightning because no paired low/high-res scans were available for validation; trained in Colab.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/ai-driven-efficient-mri-super-resolution) | [GitHub](https://github.com/venkat1596/Hacklytics_Hackathon)

### PerfectPunch  (Hacklytics - 2025: Jurassic Age)

- **Prizes:** Second in Sports [2nd]  (tier: track_winner)
- **Pitch:** Sensor-free boxing trainer: webcam pose tracking and a custom punch classifier give form, speed and injury-risk feedback, plus a Gemini coaching chatbot.
- **Problem / user:** Boxing coaching is subjective and the sport carries high concussion and brain-injury risk. / amateur and professional boxers
- **Domain / idea type:** health_wellness + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; predictive_ml; llm_chat
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; Taipy; backend Django; OpenCV; MediaPipe; PyTorch; NumPy; Pandas; db ; hosting 
- **Tech/APIs:** MediaPipe (ai_model, core); OpenCV (framework, core); PyTorch custom punch model (ai_model, core); Gemini API (ai_model, supporting, sponsor); Taipy (framework, core); Django (framework, supporting)
- **Sponsor APIs:** Gemini API | fit: Sports-track entry: pose-based punch analytics and injury risk.
- **Repo:** public, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims True (Cites 87% of pro boxers with chronic brain injury and $800 to $30,000 concussion treatment costs as motivation.)
- **Notes:** Custom PyTorch punch-type model on wrist/elbow pose estimates; Taipy dashboard of reaction time, accuracy and stance; Gemini API for coaching text; no wearables required.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags; sponsor_fit_note; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/perfectpunch) | [GitHub](https://github.com/Archerman1/PerfectPunch)

### Sympli  (Hacklytics - 2025: Jurassic Age)

- **Prizes:** Third in Generative AI [3rd]  (tier: track_winner)
- **Pitch:** Web app where patients log chronic-illness symptoms through a Gemini chatbot and see symptom-frequency charts that physicians can review.
- **Problem / user:** Symptom reporting for chronic conditions is fragmented and delayed, limiting timely diagnosis and treatment. / chronic-illness patients and their physicians
- **Domain / idea type:** health_wellness + ai_agents_infra / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs TypeScript; JavaScript; frontend React; React Router; Tailwind CSS; shadcn/ui; Recharts; backend Firebase; db Firestore; hosting Firebase Hosting
- **Tech/APIs:** Gemini 2.0 (ai_model, core, sponsor); Firebase Auth (auth, core); Firestore (database, core); Recharts (framework, supporting); Google Cloud (cloud, supporting)
- **Sponsor APIs:** Gemini | fit: Entered in the Healthcare and GenAI tracks; Gemini 2.0 chatbot collects symptom data conversationally.
- **Repo:** public, commits 71 (before/in/after event: 71/0/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup long, impact claims True (Cites 60% of Americans with a chronic condition and $4.1 trillion annual healthcare spending.)
- **Notes:** SMS chat was dropped due to phone verification hurdles, so Firebase auth on the web is used; monthly line graph shows each symptom's frequency; separate patient and physician logins.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags
- **Links:** [Devpost](https://devpost.com/software/sympli) | [GitHub](https://github.com/B-Ricey763/sympli-health)

### TaxDaddy  (Hacklytics - 2025: Jurassic Age)

- **Prizes:** 3rd Place Hack [3rd]  (tier: overall_top3)
- **Pitch:** Voice-based tax assistant: call a Twilio number, talk to a real-time AI agent that reads uploaded documents, fills tax forms, and flags anomalies and fraud.
- **Problem / user:** Filing taxes and understanding tax documents is tedious and confusing. / individual taxpayers
- **Domain / idea type:** fintech_finance + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / llm_chat; agent_or_tool_use; rag_or_search; speech_or_voice
- **Stack:** langs Python; frontend ; backend WebSockets; PyPDF form filler; OCR; db MongoDB; hosting 
- **Tech/APIs:** OpenAI Realtime API (ai_model, core); Twilio (telecom, core); MongoDB (database, supporting); OCR (other, supporting); WebSockets (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 53 (before/in/after event: 53/0/0), README none
- **Demo/writeup:** video True, live none, screenshots 6, writeup medium, impact claims False
- **Notes:** Twilio phone call bridged by WebSocket to the OpenAI real-time API; RAG plus form-filling tools; Benford's Law risk score for fraud detection on uploaded documents.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/taxdaddy) | [GitHub](https://github.com/NSP909/taxerino)

### thera_pixel  (Hacklytics - 2025: Jurassic Age)

- **Prizes:** 2nd Place Hack [2nd]  (tier: overall_top3)
- **Pitch:** Gamified physical therapy: webcam pose tracking turns rehab exercises into a pixel-art pizza game and a form-feedback practice studio.
- **Problem / user:** Patients struggle to stay consistent with prescribed home physical therapy exercises. / physical therapy patients, younger and older
- **Domain / idea type:** health_wellness + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend Flask; OpenCV; MediaPipe; NumPy; SciPy; db ; hosting 
- **Tech/APIs:** MediaPipe 3D pose (ai_model, core); OpenCV (framework, core); IntelliRehabDS (data_source, core); Flask (framework, supporting); SciPy/NumPy (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 49 (before/in/after event: 49/0/0), README thin
- **Demo/writeup:** video True, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Ground-truth movement curves built from the small IntelliRehabDS dataset via cleaning and temporal interpolation; pacing timer compares live arm angle to expected angle.
- **Team size:** 2 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/rehab-fv6j1l) | [GitHub](https://github.com/vehnil/PTplay.git)


## Hacklytics - 2026: Golden Byte

### A Spark in the Dark  (Hacklytics - 2026: Golden Byte)

- **Prizes:** First in Entertainment [1st]  (tier: track_winner)
- **Pitch:** Hollow Knight-inspired browser platformer controlled by hand gestures via webcam, with an AI voice narrator telling the story.
- **Problem / user:** Wanted a more interactive, story-driven indie game experience than keyboard controls give. / casual gamers
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web / False / speech_or_voice; llm_chat; vision
- **Stack:** langs JavaScript; frontend HTML; CSS; MediaPipe; backend ; db ; hosting Vercel
- **Tech/APIs:** MediaPipe hand tracking (framework, core); Gemini API (ai_model, core, sponsor); ElevenLabs API (ai_model, core, sponsor); Vercel (cloud, supporting)
- **Sponsor APIs:** Gemini; ElevenLabs
- **Repo:** public, commits 42 (before/in/after event: 0/42/0), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup medium, impact claims False
- **Notes:** Player moves a platform with MediaPipe hand tracking to carry a sprite; all art hand-drawn; Gemini and ElevenLabs combined for narration; team's first time using APIs.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor_flags
- **Links:** [Devpost](https://devpost.com/software/a-spark-in-the-dark) | [GitHub](https://github.com/sadie2488/Hacklytics-SSL.git)

### Alleaf  (Hacklytics - 2026: Golden Byte)

- **Prizes:** Best Overall Hack - 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Wearable stress detector: an ESP32 heart-rate sensor and ML model trigger haptic bilateral stimulation and RAG-based meditation guidance.
- **Problem / user:** Rising depression and anxiety linked to stress and low mindfulness need real-time, automated support. / people managing stress and anxiety
- **Domain / idea type:** mental_health + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / predictive_ml; rag_or_search; llm_chat; agent_or_tool_use
- **Stack:** langs Python; JavaScript; frontend Next.js; backend Flask; LangChain; scikit-learn; Pandas; NumPy; db Actian VectorDB; Firebase; hosting 
- **Tech/APIs:** ESP32 + heart-rate sensor (hardware_part, core); WESAD dataset stress model (ai_model, core); Gemini (ai_model, supporting); Actian VectorDB (database, core, sponsor); LangChain (framework, supporting); Firebase (cloud, supporting)
- **Sponsor APIs:** Actian VectorDB
- **Repo:** public, commits 207 (before/in/after event: 0/205/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Custom ESP32 device reads RR intervals with a red LED sensor and drives haptic bilateral stimulation; stress classifier trained on WESAD served via Flask; RAG agents use Actian vector DB.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags; sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/alleaf) | [GitHub](https://github.com/Gustavo-Galvao-e-Silva/Alleaf)

### BlindSpot  (Hacklytics - 2026: Golden Byte)

- **Prizes:** Second in Finance [2nd]  (tier: track_winner)
- **Pitch:** Humanitarian capital-allocation dashboard: scores country crisis severity from UN data, optimizes budget splits, and answers questions via Gemini and a vector-search brief generator.
- **Problem / user:** Humanitarian funding follows headlines rather than measured severity, leaving some severe crises underfunded. / aid donors, journalists and UN coordinators
- **Domain / idea type:** civic_legal + fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; llm_chat; rag_or_search
- **Stack:** langs Python; frontend Streamlit; Plotly; backend PySpark; scikit-learn; XGBoost; SciPy; db Databricks; Actian VectorAI; hosting Streamlit Community Cloud; Docker
- **Tech/APIs:** Databricks (cloud, core, sponsor); Actian VectorAI (database, core, sponsor); Gemini 2.5 Flash (ai_model, core, sponsor); XGBoost (ai_model, supporting); scikit-learn PCA (framework, core); SciPy SLSQP optimizer (framework, core); UN datasets (FTS, UCDP GED, IDMC, IPC, ReliefWeb) (data_source, core); Streamlit (framework, core)
- **Sponsor APIs:** Databricks; Actian VectorAI; Gemini | fit: Finance-track entry framing humanitarian aid as capital allocation using UN data, optimization and ML.
- **Repo:** public, commits 28 (before/in/after event: 0/27/1), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 8, writeup long, impact claims True (Dashboard headline estimates lives lost annually to funding misallocation; reports 2,388 documents embedded.)
- **Notes:** PCA severity score, XGBoost forecasts and SciPy SLSQP allocation over five UN datasets in Databricks; RAG over 2,388 UN docs in Actian VectorAI using TF-IDF instead of neural embeddings; three persona-specific briefs.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags; sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/blindspot-azf0i1) | [GitHub](https://github.com/Hidhayath-Nisha/blindspot)

### BraceML  (Hacklytics - 2026: Golden Byte)

- **Prizes:** First in Sports; Figma Make Most Creative Data Visualization [1st]  (tier: track_winner)
- **Pitch:** Real-time camera-based biomechanics platform scoring injury risk and fatigue for individuals and whole teams, with concussion detection plus iOS and Quest VR clients.
- **Problem / user:** Preventive movement assessment needs expensive labs, and coaches substitute tired players by guesswork rather than objective data. / athletes and coaches
- **Domain / idea type:** health_wellness + other / new_category
- **Platforms / hardware / AI:** web; mobile_ios; other / True / vision; llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs Python; TypeScript; Swift; C#; frontend Next.js 15; React 19; Three.js; SwiftUI; Unity; backend FastAPI; WebSocket; Caddy; db Actian VectorAI DB; MongoDB; hosting Docker Compose; Tailscale
- **Tech/APIs:** Actian VectorAI DB (database, core, sponsor); Gemini 2.0 Flash (ai_model, core, sponsor); Figma Make (other, supporting, sponsor); ElevenLabs TTS (ai_model, supporting, sponsor); YOLO11-pose (ai_model, core); RTMW3D / HybrIK / BoT-SORT (ai_model, supporting); CLIP-ReID (ai_model, supporting); Meta Quest 3 (Unity) (hardware_part, supporting); MongoDB (database, supporting); TensorRT (framework, supporting)
- **Sponsor APIs:** Actian VectorAI DB; Gemini; Figma Make; ElevenLabs | fit: Sports-track winner that also took the Figma Make visualization prize; used Figma Make for dashboard design, Actian for movement embeddings and Gemini for intake and jersey reading.
- **Repo:** public, commits 101 (before/in/after event: 0/101/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup long, impact claims True (Cites 200,000 US ACL tears yearly, 3.5 million youth injuries, $300 assessments, and a 35% earlier squat warning.)
- **Notes:** Same binary WebSocket protocol serves web, native iOS (240fps concussion capture) and Unity Meta Quest 3 clients; 28-dim pose features with spectral clustering; Gemini Vision reads jersey numbers; claims 626 tests.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags; n_screenshots; domain_secondary; platforms
- **Links:** [Devpost](https://devpost.com/software/braceml) | [GitHub](https://github.com/jiekaitao/BRACE)

### Conduit  (Hacklytics - 2026: Golden Byte)

- **Prizes:** Second in Healthcare [2nd]  (tier: track_winner)
- **Pitch:** Accessibility layer turning voice, EEG, eye tracking and ASL hand signs into standard computer input events for users who cannot use conventional controls.
- **Problem / user:** Computer interfaces assume hand use, clear speech or sight, excluding many people with disabilities. / people with motor, speech or vision disabilities
- **Domain / idea type:** accessibility + health_wellness / new_category
- **Platforms / hardware / AI:** desktop; hardware / True / speech_or_voice; vision; predictive_ml; llm_chat
- **Stack:** langs Python; TypeScript; frontend Electron; backend FastAPI; OpenCV; db ; hosting 
- **Tech/APIs:** ElevenLabs STT (ai_model, core, sponsor); Gemini (ai_model, core, sponsor); Muse EEG headset (hardware_part, core); MobileNetV2 ASL classifier (ai_model, core); OpenCV face/iris landmarks (framework, core); Electron (framework, supporting)
- **Sponsor APIs:** ElevenLabs; Gemini
- **Repo:** public, commits 56 (before/in/after event: 0/55/1), README thin
- **Demo/writeup:** video True, live none, screenshots 11, writeup long, impact claims True (Cites 1.3 billion people with disability and over 30% unable to use conventional computer controls.)
- **Notes:** Four independent input modalities share one canonical event schema: Muse EEG intent, iris-based gaze cursor, custom MobileNetV2 ASL letter classifier, and ElevenLabs plus Gemini voice commands.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags
- **Links:** [Devpost](https://devpost.com/software/conduit-y8gqoj) | [GitHub](https://github.com/kwaiidev/conduit)

### Crisis Averted  (Hacklytics - 2026: Golden Byte)

- **Prizes:** 3rd Overall Hack [3rd]  (tier: overall_top3)
- **Pitch:** Voice-commanded 3D globe that visualizes humanitarian funding gaps, with an AI agent that flies to regions and delivers spoken briefings.
- **Problem / user:** Humanitarian aid is allocated reactively by media visibility instead of measured need. / aid funders and humanitarian responders
- **Domain / idea type:** civic_legal + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; speech_or_voice; rag_or_search; llm_chat
- **Stack:** langs Python; JavaScript; TypeScript; frontend Next.js; react-globe.gl; Three.js; Tailwind CSS; Framer Motion; Recharts; backend FastAPI; Apache Kafka; Node.js; WebRTC; WebSockets; db Actian Vector DB; Databricks Delta Lake; SQLite; hosting Vultr
- **Tech/APIs:** Gemini 3.0 Pro/Flash (ai_model, core, sponsor); ElevenLabs (ai_model, core, sponsor); Databricks Genie (cloud, core, sponsor); Actian Vector DB (database, core, sponsor); Vultr 192-core VM (cloud, core, sponsor); Apache Kafka (framework, core); UN OCHA HDX HAPI (data_source, core); sentence-transformers all-mpnet-base-v2 (ai_model, supporting); react-globe.gl / Three.js (framework, core)
- **Sponsor APIs:** Databricks; Actian Vector DB; Vultr; ElevenLabs; Gemini
- **Repo:** public, commits 160 (before/in/after event: 0/160/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Multi-stage pipeline: ElevenLabs voice isolation, Gemini function calling, Kafka command bus, Databricks Genie SQL, Actian vector search on a self-hosted 192-core Vultr VM, and a Three.js globe deformed by funding gaps.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags; sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/crisis-averted) | [GitHub](https://github.com/GodlyDonuts/Hacklytics-GoldenByte)

### DarkHorse  (Hacklytics - 2026: Golden Byte)

- **Prizes:** Third in Sports [3rd]  (tier: track_winner)
- **Pitch:** World Cup match tool that combines Elo, matchup features and player impact into a single DarkScore flagging upset risk before kickoff.
- **Problem / user:** Favorites usually win, but fans lack a readable signal for when a match is quietly unstable. / soccer fans and World Cup bettors/analysts
- **Domain / idea type:** entertainment_games / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; Vite; backend Python; db ; hosting Vercel
- **Tech/APIs:** XGBoost (ai_model, core); Elo ratings (data_source, core); Vercel (cloud, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 47 (before/in/after event: 0/47/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup short, impact claims False
- **Notes:** XGBoost model trained on a custom scraped dataset; readable tiers and named player contributors explain each score.
- **Team size:** 3 | **Confidence:** medium | unverified: stack_frontend; stack_backend
- **Links:** [Devpost](https://devpost.com/software/darkhorse) | [GitHub](https://github.com/WorldCup-UnderDog/DarkHorse_WorldCup)

### DataFables  (Hacklytics - 2026: Golden Byte)

- **Prizes:** Third in Entertainment [3rd]  (tier: track_winner)
- **Pitch:** Pixel-art educational story game for children: AI-generated branching stories grounded in Snowflake facts, narrated in 10 languages with pronunciation practice.
- **Problem / user:** Many children's digital games entertain without building creativity, vocabulary or literacy. / young children and their parents
- **Domain / idea type:** education + entertainment_games / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; generative_media; speech_or_voice
- **Stack:** langs TypeScript; Python; SQL; JavaScript; frontend Next.js; React; backend Python; Snowflake REST API; db Snowflake; VectorAI DB; hosting 
- **Tech/APIs:** Snowflake (database, core, sponsor); Actian VectorAI DB (database, core, sponsor); Gemini (ai_model, core, sponsor); ElevenLabs (ai_model, core, sponsor); SafetyKit (other, supporting, sponsor); Next.js (framework, core)
- **Sponsor APIs:** Snowflake; Actian VectorAI DB; Gemini; ElevenLabs; SafetyKit
- **Repo:** public, commits 33 (before/in/after event: 0/33/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 3, writeup long, impact claims False
- **Notes:** Retrieval chain of Snowflake REST facts, VectorAI semantic recall of mispronounced words, Gemini story and images, ElevenLabs narration and SafetyKit child-safety check; XP, coin shop and character designer.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags
- **Links:** [Devpost](https://devpost.com/software/hacklytics-2026) | [GitHub](https://github.com/jaimeb18/datafables)

### HeartScape  (Hacklytics - 2026: Golden Byte)

- **Prizes:** Third in Healthcare [3rd]  (tier: track_winner)
- **Pitch:** Browser 3D viewer that builds explorable healthy and congenital heart models from cardiac MRI, with patient-similarity search and an AI region explainer.
- **Problem / user:** Understanding congenital heart anatomy from stacks of 2D MRI slices is slow and unintuitive. / medical students, researchers and clinicians
- **Domain / idea type:** health_wellness + education / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; JavaScript; frontend Three.js; HTML; backend Flask; PyVista; db Actian VectorAI; hosting Docker
- **Tech/APIs:** Actian VectorAI (database, core, sponsor); Sphinx.AI (other, supporting, sponsor); Gemini 2.5 (ai_model, supporting, sponsor); Three.js (framework, core); PyVista (framework, core); HVSMR-2.0 dataset (data_source, core)
- **Sponsor APIs:** Actian VectorAI; Sphinx.AI; Gemini
- **Repo:** public, commits 67 (before/in/after event: 0/67/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Meshes built from the public HVSMR-2.0 CMR dataset; Actian VectorAI stores volumetric-measurement vectors (not learned embeddings) in six collections using Euclidean distance; Sphinx.AI notebooks make deviation heatmaps.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags
- **Links:** [Devpost](https://devpost.com/software/heartscape) | [GitHub](https://github.com/SohamAg/hacklytics2026)

### Lumos AI  (Hacklytics - 2026: Golden Byte)

- **Prizes:** 2nd Overall Hack [2nd]  (tier: overall_top3)
- **Pitch:** Location safety platform that scores any place 0-100 from FBI crime data and live feeds with an XGBoost model, route comparison, and an AI voice agent that can call 911.
- **Problem / user:** Existing safety tools give vague crime labels without time-specific risk or help when someone cannot speak in an emergency. / travelers, students and solo walkers or joggers
- **Domain / idea type:** safety_security + civic_legal / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; llm_chat; speech_or_voice; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend React; Vite; Tailwind CSS; shadcn/ui; Mapbox GL JS; Framer Motion; backend FastAPI; XGBoost; Firebase Cloud Functions; db Firebase Realtime Database; Firestore; hosting Vultr; Netlify
- **Tech/APIs:** XGBoost safety model (ai_model, core); FBI NIBRS data (data_source, core); Gemini 2.5 Flash (ai_model, core, sponsor); VAPI (telecom, core); ElevenLabs (ai_model, supporting, sponsor); Vultr Cloud Compute (cloud, core, sponsor); Mapbox GL (maps_geo, core); Google Routes API (maps_geo, supporting); Citizen API (data_source, supporting); Firebase (cloud, core); Socrata open data portals (data_source, supporting); Twilio (telecom, unclear)
- **Sponsor APIs:** Vultr; Gemini; ElevenLabs
- **Repo:** public, commits 37 (before/in/after event: 0/34/3), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 10, writeup long, impact claims True (Reports 48 GB of data, about 59 million incidents, 136,626 cities covered, and sub-2-second scoring.)
- **Notes:** Processed about 48 GB of FBI NIBRS data into agency profiles, fused 11+ live APIs, and built a VAPI/Gemini/ElevenLabs voice agent with live GPS streaming via Firebase RTDB. Writeup is very long with many numbers.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags; sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/lumos-ai) | [GitHub](https://github.com/hxxtsxxh/lumos.ai)

### MomentumShift  (Hacklytics - 2026: Golden Byte)

- **Prizes:** Second in Sports [2nd]  (tier: track_winner)
- **Pitch:** NBA analytics tool that visualizes game momentum in real time, predicts scoring runs with ML and matches historical patterns.
- **Problem / user:** Traditional box-score stats miss momentum swings that decide basketball games. / basketball fans and analysts
- **Domain / idea type:** entertainment_games / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; backend FastAPI; Node.js proxy; scikit-learn; db Supabase; hosting 
- **Tech/APIs:** scikit-learn (framework, core); Supabase (database, supporting); NBA API (data_source, core); FastAPI (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 6 (before/in/after event: 0/6/0), README solid
- **Demo/writeup:** video True, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Proprietary momentum algorithm; the team hit NBA API deprecation during the build; writeup is terse bullet fragments.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/momentumshift) | [GitHub](https://github.com/rishyendra333/hacklytics-2026)

### Nexus  (Hacklytics - 2026: Golden Byte)

- **Prizes:** Third in Finance [3rd]  (tier: track_winner)
- **Pitch:** Platform mapping how global news events ripple as financial shocks across countries, sectors and S&P 100 stocks, with a 3D globe, forecasts and what-if simulation.
- **Problem / user:** Connecting geopolitical and supply-chain events to market impact normally requires costly institutional terminals unavailable to ordinary people. / retail investors and finance learners
- **Domain / idea type:** fintech_finance + education / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; llm_chat; rag_or_search
- **Stack:** langs Python; TypeScript; frontend React; Vite; Tailwind; Mapbox GL; Recharts; backend NestJS; FastAPI; Socket.io; db Actian VectorAI DB; hosting AWS ECS Fargate; CloudFront
- **Tech/APIs:** Actian VectorAI DB (database, core, sponsor); LSTM per-ticker models (TensorFlow/Keras) (ai_model, core); BART-large-MNLI (ai_model, core); all-MiniLM-L6-v2 (ai_model, core); OpenAI (ai_model, supporting); Mapbox GL (maps_geo, core); AWS ECS Fargate/CloudFront (cloud, supporting); NewsAPI, Polygon, Finnhub, GDELT, ACLED (data_source, core)
- **Sponsor APIs:** Actian VectorAI DB | fit: Finance-track entry using Actian VectorAI DB for historical event similarity search.
- **Repo:** public, commits 59 (before/in/after event: 0/59/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 5, writeup long, impact claims True (Cites a literature review on financial literacy tools and a $32B geopolitical risk intelligence market; claims sub-100ms inference.)
- **Notes:** Self-trained models: 117 per-ticker LSTMs trained on Georgia Tech Phoenix cluster, BART zero-shot event classifier, sub-100ms custom model server with fallback to OpenAI then stubs; backend lists two GitHub repos.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags; sponsor_apis_used; domain_secondary
- **Links:** [Devpost](https://devpost.com/software/nexus-6tr249) | [GitHub](https://github.com/UpStackLabs/nexus-frontend)

### Tempr  (Hacklytics - 2026: Golden Byte)

- **Prizes:** Second in Entertainment [2nd]  (tier: track_winner)
- **Pitch:** Mobile app that turns a text mood, photo or calendar event into a Spotify queue drawn from the user's liked songs using Gemini and audio-feature matching.
- **Problem / user:** Large liked-song libraries cause choice paralysis when someone wants music that fits a specific vibe or moment. / Spotify listeners
- **Domain / idea type:** entertainment_games + creative_media / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / llm_chat; vision; recommendation
- **Stack:** langs TypeScript; frontend Expo; React Native; expo-router; backend Supabase Auth; db AsyncStorage; hosting 
- **Tech/APIs:** Gemini API (ai_model, core, sponsor); Spotify Web API (data_source, core); Supabase Auth (auth, supporting); Apple Calendar (other, supporting); YouTube Data API (data_source, supporting); Expo / React Native (framework, core)
- **Sponsor APIs:** Gemini
- **Repo:** public, commits 34 (before/in/after event: 0/34/0), README solid
- **Demo/writeup:** video True, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Gemini converts prompt or image to a target vibe vector matched by cosine similarity against Spotify audio-feature vectors; calendar-triggered playlists with 10-minute notifications; swipe Discover with YouTube previews.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor_flags
- **Links:** [Devpost](https://devpost.com/software/tempr) | [GitHub](https://github.com/aidenerard/tempr.git)

### Veritais  (Hacklytics - 2026: Golden Byte)

- **Prizes:** First in Finance [1st]  (tier: track_winner)
- **Pitch:** Scores executive truthfulness by fusing facial action units, vocal features and verified-claim outcomes from public videos into a per-company Truth Index and CEO leaderboard.
- **Problem / user:** Corporate deception signals in speech and expression go unmeasured, so investors lack an accessible accountability tool. / retail investors, analysts and journalists
- **Domain / idea type:** fintech_finance + ai_agents_infra / new_category
- **Platforms / hardware / AI:** web / False / vision; speech_or_voice; agent_or_tool_use; rag_or_search; predictive_ml; llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; Bun; backend FastAPI; scikit-learn; SciPy; librosa; Praat; Py-Feat; db vector database (unnamed); hosting 
- **Tech/APIs:** Whisper V3 (ai_model, core); Py-Feat (framework, core); librosa / Praat (framework, core); LLM/VLM verification agent (model unnamed) (ai_model, core); YouTube (data_source, core); Next.js (framework, supporting)
- **Sponsor APIs:**  | fit: Finance-track entry applying multimodal ML to executive statements and truthfulness scoring.
- **Repo:** public, commits 128 (before/in/after event: 0/128/0), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims True (Cites academic studies on vocal affect and facial expressions; mentions about 4000 hours of recordings.)
- **Notes:** Learns from statements later verified true or false by an agentic LLM loop; within-person baseline normalization of facial and prosodic features; Whisper transcription and speaker fingerprint vector DB.
- **Team size:** 3 | **Confidence:** high | unverified: sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/veritais) | [GitHub](https://github.com/8pxl/veritas)

### Vigil  (Hacklytics - 2026: Golden Byte)

- **Prizes:** First in Healthcare [1st]  (tier: track_winner)
- **Pitch:** Event safety system pairing a Wear OS watch with camera-based posture analysis to detect fainting or dizziness in at-risk attendees and alert medical staff.
- **Problem / user:** People with conditions like POTS risk fainting in long event queues, and response to medical distress in crowds is slow. / event attendees with chronic conditions and event medical staff
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** mobile_android; hardware; other / True / vision; predictive_ml; llm_chat
- **Stack:** langs Python; Kotlin; Dart; frontend Flutter; Wear OS; backend FastAPI; OpenCV; PyTorch; db ; hosting 
- **Tech/APIs:** Gemini API (ai_model, supporting, sponsor); YOLOv8 Nano (ai_model, core); PyTorch LSTM (ai_model, core); Samsung Galaxy Watch 4 (hardware_part, core); Raspberry Pi (hardware_part, core); Bluetooth LE (hardware_part, core); Flutter (framework, supporting)
- **Sponsor APIs:** Gemini
- **Repo:** public, commits 34 (before/in/after event: 0/34/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Fuses Galaxy Watch 4 signals, BLE/RSSI localization via Raspberry Pi units and a YOLOv8n plus custom LSTM vision pipeline; Gemini writes incident summaries for staff.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor_flags
- **Links:** [Devpost](https://devpost.com/software/vigil-b8uatr) | [GitHub](https://github.com/aishanibal/hacklytics2026)
