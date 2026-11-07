# HackGT: project cards (74 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackGT 11

### 90°  (HackGT 11)

- **Prizes:** Winner Best Use of MATLAB [unknown]  (tier: sponsor_winner)
- **Pitch:** Mobile app that learns a user's favorite photo angles from uploaded examples and guides a friend taking their photo toward those angles.
- **Problem / user:** Handing a phone to someone for a photo yields many unusable shots and explaining preferred angles is awkward. / people who want better photos taken by others
- **Domain / idea type:** creative_media + retail_consumer / creative_tool
- **Platforms / hardware / AI:** mobile_cross / False / vision; predictive_ml
- **Stack:** langs JavaScript; Python; MATLAB; frontend React Native; Expo; backend Node.js; Mongoose; Terraform; db MongoDB; hosting AWS EC2; AWS S3; Terraform
- **Tech/APIs:** MATLAB deep learning (ai_model, core, sponsor); PyTorch / TensorFlow / Keras (framework, supporting); OpenCV (framework, supporting); MongoDB Atlas (database, core); AWS EC2/S3 (cloud, supporting); Terraform (cloud, supporting); React Native / Expo (framework, core)
- **Sponsor APIs:** MATLAB | fit: Targeted Best Use of MATLAB by training the good-versus-bad photo model in MATLAB and arguing it trained far faster than PyTorch or TensorFlow, with a MATLAB runtime in the deployment.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 16, writeup long, impact claims True (Claims MATLAB training took about 1 minute versus 35 minutes with PyTorch or TensorFlow.)
- **Notes:** Photo-quality model trained in MATLAB and compared with PyTorch/TensorFlow (writeup claims 1 minute versus 35 minutes); Terraform deploys AWS EC2/S3 and MongoDB Atlas with a MATLAB runtime; Figma prototype linked.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; platforms
- **Links:** [Devpost](https://devpost.com/software/90)

### AerLock  (HackGT 11)

- **Prizes:** Analytics Arcade - 1st Place [1st]  (tier: track_winner)
- **Pitch:** One-button Android app that remotely cuts Wi-Fi, Bluetooth, cellular and ports on all a user's devices through MQTT endpoints.
- **Problem / user:** Consumer cyber defense tools are costly and complicated, with no easy way to airgap many devices at once. / everyday users and travelers worried about attacks
- **Domain / idea type:** safety_security + telecom_networking / dev_tool
- **Platforms / hardware / AI:** mobile_android; desktop / False / False
- **Stack:** langs Kotlin; Java; Python; C; frontend Android (XML); backend MQTT; db ; hosting HiveMQ Cloud; AWS
- **Tech/APIs:** HiveMQ MQTT cloud (cloud, core); MQTT over TLS 1.2 (other, core); Kotlin/Java Android (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 21 (before/in/after event: 0/17/4), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup medium, impact claims False
- **Notes:** Android controller plus Windows and Linux endpoint agents listening on HiveMQ cloud MQTT over TLS 1.2; users can bring their own broker; endpoints offered for download.
- **Team size:** 3 | **Confidence:** medium | unverified: n_screenshots; event_start; event_end; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/aerlock) | [GitHub](https://github.com/JackWachter/AerLock)

### Clarity  (HackGT 11)

- **Prizes:** PHRI Challenge - 1st Place [1st]  (tier: track_winner)
- **Pitch:** Multimodal fatigue detector for doctors using face video and voice audio, with explainable saliency maps.
- **Problem / user:** Fatigued doctors make diagnostic errors and burn out, yet few systems exist to detect and support them. / physicians and hospital staff
- **Domain / idea type:** health_wellness + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; speech_or_voice; predictive_ml
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend Python; PyTorch; OpenCV; WebRTC; db ; hosting 
- **Tech/APIs:** PyTorch (framework, core); WebRTC (framework, core); OpenCV (framework, core); Vision transformer (FEF fine-tune) (ai_model, core); HuBERT-base (ai_model, core); Whisper-tiny (ai_model, supporting); Matplotlib (framework, supporting); Hugging Face (other, supporting)
- **Sponsor APIs:**  | fit: Detects clinician fatigue to reduce misdiagnosis, fitting a health-focused challenge; PHRI sponsor products not stated.
- **Repo:** public, commits 32 (before/in/after event: 3/23/6), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims True (Cites a malpractice payout and a physician suicide-rate statistic; reports ~92% model accuracy on unseen data.)
- **Notes:** Fine-tuned vision transformer on a fatigue-face dataset plus HuBERT audio emotion model; inference ran on a remote RTX 4090 machine streamed over WebRTC.
- **Team size:** 3 | **Confidence:** high | unverified: sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/clarity-kuv9xn) | [GitHub](https://github.com/shayaf84/clarity/tree/main)

### EVA  (HackGT 11)

- **Prizes:** AI Funhouse - 1st Place [1st]  (tier: track_winner)
- **Pitch:** AI conversation tutor for language learners that gives instant grammar corrections and a language-independent pronunciation check.
- **Problem / user:** Language apps lack natural conversation with native-like feedback, and waiting for corrections slows learning. / language learners
- **Domain / idea type:** education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice
- **Stack:** langs Python; frontend Tailwind CSS; backend Flask; db MySQL; hosting 
- **Tech/APIs:** GPT-4o (ai_model, core); Hugging Face phoneme recognition model (ai_model, core); Flask (framework, core); MySQL (database, supporting); Snap Spectacles / Lens Studio (hardware_part, unclear, sponsor)
- **Sponsor APIs:** 
- **Repo:** public, commits 1 (before/in/after event: 0/1/0), README none
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Started on Snap Spectacles with Lens Studio but pivoted to a Flask web app after text-to-speech bugs; uses zero-shot cross-lingual phoneme recognition paper for pronunciation.
- **Team size:** 3 | **Confidence:** high | unverified: team_size; n_screenshots; event_start; event_end; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/eva-jmb5et) | [GitHub](https://github.com/Jinash-Rouniyar/EVA_Voice_Companion)

### Fight and Furious  (HackGT 11)

- **Prizes:** Best Overall - 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Web app that teaches Krav Maga self-defense moves and scores the user live via webcam pose comparison.
- **Problem / user:** Gender-based violence is widespread and many people lack accessible self-defense instruction. / women and young people wanting self-defense training
- **Domain / idea type:** safety_security + education / social_good
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend React; backend FastAPI; Streamlit; Uvicorn; db ; hosting 
- **Tech/APIs:** MediaPipe (ai_model, core); OpenCV (framework, core); Streamlit (framework, supporting); React (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 5 (before/in/after event: 0/4/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims True (Cites 736 million women having experienced gender violence and about 26% aged 15 to 24.)
- **Notes:** Accuracy computed as mean squared error of angles between limb vectors from MediaPipe pose; live video via Streamlit embedded as iframe in React page; beginners on the team.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/fight-and-furious) | [GitHub](https://github.com/maechen/HackGTFinal2024)

### FirefightAR  (HackGT 11)

- **Prizes:** SnapAR Elexa Power Bank (20000mAH) [unknown]  (tier: sponsor_winner)
- **Pitch:** Snap Spectacles AR app that overlays hazards, detected people and the shortest path to them or the exit to help firefighters search burning buildings.
- **Problem / user:** Firefighters search smoke-filled buildings by slow, brute-force crawling, raising risk of injury and disorientation. / firefighters
- **Domain / idea type:** safety_security / hardware_gadget
- **Platforms / hardware / AI:** other; hardware / True / vision
- **Stack:** langs JavaScript; TypeScript; Python; frontend Lens Studio; backend Firebase; db Firebase; hosting 
- **Tech/APIs:** Snap Spectacles / Lens Studio (hardware_part, core, sponsor); Spectacles Interaction Kit (framework, supporting, sponsor); YOLOv5 (ai_model, core); Firebase (database, supporting)
- **Sponsor APIs:** Snap Spectacles; Lens Studio | fit: Targeted the SnapAR prize by building a Spectacles AR rescue-navigation app in Lens Studio with Snap team support.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Uses a pre-trained YOLOv5 on fire-related data rather than a custom model; built on a Spectacles toolkit released a week earlier; Firebase shares state among team members.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/firefightar) | [GitHub](https://github.com/thanh12273203/FirefightAR)

### Lightning McScream  (HackGT 11)

- **Prizes:** Best Domain Name from GoDaddy Registry [unknown]  (tier: sponsor_winner)
- **Pitch:** Laser-cut ESP32 car that speeds up the louder you scream, raced on a Unity AR track viewed on a Quest 2 headset.
- **Problem / user:** Not a problem-driven project; it is a carnival-style game linking voice volume to physical speed. / game and carnival players
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** hardware; other / True / False
- **Stack:** langs Python; C#; C++; MATLAB; frontend Unity; backend FastAPI; db ; hosting 
- **Tech/APIs:** ESP32 microcontroller (hardware_part, core); Meta Quest 2 + Unity (hardware_part, core); FastAPI (framework, supporting); MATLAB / Simulink (framework, supporting); Accelerometer, DC motor, L298N driver (hardware_part, core)
- **Sponsor APIs:**  | fit: Won the MLH GoDaddy Registry domain-name prize; the page does not mention a domain name or any GoDaddy product.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Voice volume and pitch computed in Python/C# are relayed via FastAPI to an ESP32 driving a custom 12V-powered, laser-cut car with custom gears; accelerometer data gives top speed; MATLAB/Simulink used for design.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; sponsor_fit_note; is_sponsor
- **Links:** [Devpost](https://devpost.com/software/car-hf3moa)

### Market Melee  (HackGT 11)

- **Prizes:** Winner Best DEI Hack sponsored by Fidelity [unknown]  (tier: sponsor_winner)
- **Pitch:** Web app for simulated S&P 500 stock portfolios using real market data, with graphs, metrics and friend leagues to make investing less intimidating.
- **Problem / user:** Financial jargon, calculations and visualizations intimidate everyday people trying to learn about investing. / beginner investors and students
- **Domain / idea type:** fintech_finance + education / entertainment_or_game
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; JavaScript; frontend HTML; CSS; Bootstrap; Jinja; backend Flask; pandas; NumPy; Matplotlib; db MongoDB Atlas; hosting 
- **Tech/APIs:** yfinance (data_source, core); MongoDB Atlas (database, core); Flask (framework, core); pandas / NumPy / Matplotlib (framework, supporting); bcrypt (auth, supporting)
- **Sponsor APIs:**  | fit: Entered Fidelity's Best DEI Hack prize with a financial-literacy simulator aimed at making investing approachable; the page does not mention Fidelity's tools.
- **Repo:** public, commits 72 (before/in/after event: 5/60/7), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Built by a pair from a computational investing class; simulated portfolios on S&P 500 data via yfinance with league-based comparison against friends; Flask with MongoDB Atlas.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/market-melee) | [GitHub](https://github.com/vennreddy490/Market-Melee)

### MedEase: AI-Assisted Diagnostic Workflow  (HackGT 11)

- **Prizes:** Best Use of MongoDB Atlas [unknown]  (tier: sponsor_winner)
- **Pitch:** Web app where doctors upload patient PDFs and a RAG pipeline returns a differential diagnosis and notes ready for EHR entry, with login and saved documents.
- **Problem / user:** Emergency doctors spend a large share of shifts on data entry instead of monitoring patients. / doctors and clinicians
- **Domain / idea type:** health_wellness + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; TypeScript; frontend Astro; React; backend Python; LlamaIndex; db MongoDB Atlas; hosting Vercel
- **Tech/APIs:** MongoDB Atlas (users, PDFs, vector search) (database, core, sponsor); LlamaIndex RAG (framework, core); Astro (framework, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:** MongoDB Atlas | fit: Used MongoDB Atlas for user data, PDF storage and the RAG vector database in its diagnostic workflow.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup medium, impact claims True (Cites a study that over 40% of a 10-hour ER shift goes to data entry and 4,000 clicks.)
- **Notes:** MongoDB Atlas holds user records, PDF storage and the vector index for RAG built with LlamaIndex; frontend in Astro by relatively inexperienced members; next step is EHR API integration.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; llm_model; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/medease-ai-assisted-diagnostic-workflow) | [GitHub](https://github.com/1129Chengyuan/EMR-Automatic)

### Noma  (HackGT 11)

- **Prizes:** Best Overall - 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Telemedicine tool for Mohs surgery that gives remote surgeons a 3D face reconstruction and auto-generated time-stamped transcripts from the operating room.
- **Problem / user:** Rural patients lack access to Mohs-surgery specialists, raising delays and error risk. / remote consulting surgeons and rural dermatology patients
- **Domain / idea type:** health_wellness + ai_agents_infra / new_category
- **Platforms / hardware / AI:** web / False / vision; speech_or_voice; rag_or_search; llm_chat; generative_media
- **Stack:** langs Python; JavaScript; frontend React; Three.js; Streamlit; backend Flask; Node.js; db Neo4j; hosting AWS; RunPod
- **Tech/APIs:** Instant Splat (ai_model, core); AWS Transcribe (cloud, core); LITA (ai_model, core); Neo4j GraphRAG (database, core); Meditron 7B (ai_model, core); RunPod (cloud, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 23 (before/in/after event: 0/18/5), README detailed
- **Demo/writeup:** video True, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Uses Instant Splat for 3D face; AWS Transcribe diarization, LITA video actions, Neo4j GraphRAG into Meditron 7B; 3D reconstruction takes 45+ minutes so only initial scan shown, not live.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots; event_start; event_end; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/noma-ug9qxn) | [GitHub](https://github.com/Shrey1306/mona)

### OncoAI  (HackGT 11)

- **Prizes:** Carnival for a Cause - 1st Place [1st]  (tier: track_winner)
- **Pitch:** Aggregates blood tests, mammograms, slide images and scRNA-seq data through AI models and an LLM into one breast cancer report.
- **Problem / user:** Breast cancer diagnosis needs several specialists over weeks, and access gaps hit minority and low-income patients hardest. / oncology care teams and clinicians
- **Domain / idea type:** health_wellness / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; vision; llm_chat
- **Stack:** langs Python; JavaScript; frontend Next.js; backend PyTorch; TensorFlow; db PostgreSQL; hosting Vercel
- **Tech/APIs:** Gemini (ai_model, unclear); Groq (ai_model, unclear); Llama (ai_model, unclear); Mistral (ai_model, unclear); PyTorch (framework, core); TensorFlow (framework, unclear); PostgreSQL (database, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 21 (before/in/after event: 0/21/0), README solid
- **Demo/writeup:** video True, live none, screenshots None, writeup medium, impact claims True (Says a month-long four-doctor process becomes a couple of minutes; no measurements given.)
- **Notes:** Multimodal inputs (four data types) fed to separate models then LLM-compiled; encrypted patient records in Postgres aiming at HIPAA compliance; page lists many LLM providers.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots; event_start; event_end; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/oncoai) | [GitHub](https://github.com/kevinw93/hackgt12)

### OncoBot  (HackGT 11)

- **Prizes:** Best Emerging - 3rd Place [3rd]  (tier: track_winner)
- **Pitch:** Discord bot that checks uploaded skin photos for melanoma with OpenCV image processing and lists the five nearest hospitals via Google Maps.
- **Problem / user:** People worried about skin cancer often find out late and lack a quick way to screen and find care. / worried individuals checking skin lesions
- **Domain / idea type:** health_wellness / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat / False / vision
- **Stack:** langs Python; frontend Discord; backend OpenCV; Discord API; db ; hosting 
- **Tech/APIs:** OpenCV (framework, core); Discord API (other, core); Google Maps API (maps_geo, core); Kaggle dataset (data_source, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 11 (before/in/after event: 1/10/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup long, impact claims True (States about 200,000 melanoma diagnoses yearly and 82% cumulative labeling accuracy of its own bot.)
- **Notes:** First-hackathon team; relies on pre-trained OpenCV models rather than training, reporting 82% labeling accuracy; Kaggle dataset; delivered entirely as a Discord bot in Python.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; event_start; event_end; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/oncobot-qlkv0n) | [GitHub](https://github.com/AAsteriskz7/onco-bot)

### prompt+  (HackGT 11)

- **Prizes:** Best Overall - 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Chrome extension that compresses LLM chat prompts to save tokens and summarizes conversation context for reuse in new chats.
- **Problem / user:** Users waste token limits on poorly crafted prompts and lose context when restarting chats. / LLM chat users and developers
- **Domain / idea type:** dev_tools + productivity_workplace / dev_tool
- **Platforms / hardware / AI:** browser_extension / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend React; Chrome extension; backend Flask; LangChain; spaCy; tiktoken; db Firebase Realtime Database; hosting 
- **Tech/APIs:** OpenAI API (ai_model, core); spaCy (framework, core); LangChain (framework, supporting); Firebase (database, supporting); tiktoken (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 31 (before/in/after event: 7/24/0), README solid
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims True (Claims 47% token reduction for plain text and 35% for code inputs; method not shown.)
- **Notes:** Routes plain text through spaCy stop-word/lemma trimming and code through a LangChain GPT agent; Firebase stores prompt pairs wiped at session end; button placed beside chat send button.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/prompt-sf7drq) | [GitHub](https://github.com/promptplusGT/promptplus)

### SafeSnap  (HackGT 11)

- **Prizes:** Best Emerging - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Snap AR lens that scans a room, labels objects, and signals safe locations with audio and visual cues plus a voice-activated floating checklist.
- **Problem / user:** Writeup gives no problem beyond wanting a useful Snap AR idea; implied need is guiding users to safe spots. / AR glasses users needing safety guidance
- **Domain / idea type:** safety_security / new_category
- **Platforms / hardware / AI:** other / False / False
- **Stack:** langs JavaScript; frontend Lens Studio; backend ; db ; hosting 
- **Tech/APIs:** Snap Lens Studio / Snap AR (framework, core, sponsor); Lens Studio voice recognition asset (other, supporting, sponsor)
- **Sponsor APIs:** Snap Lens Studio
- **Repo:** public, commits 19 (before/in/after event: 0/19/0), README solid
- **Demo/writeup:** video True, live none, screenshots 5, writeup short, impact claims False
- **Notes:** Built in Lens Studio for Snap AR with voice recognition asset; checklist can follow the user or stay fixed; very short writeup; no ML yet.
- **Team size:** 4 | **Confidence:** medium | unverified: team_size; platforms; problem_statement; tech_items.is_sponsor; n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/safesnap) | [GitHub](https://github.com/yashalluri/SAFESNAP)

### SafeWay  (HackGT 11)

- **Prizes:** Best Use of Terraform [unknown]  (tier: sponsor_winner)
- **Pitch:** Route planner that uses scraped crime, streetlight and road-quality data to return three walking or driving routes ranked by safety, lighting, walkability and efficiency.
- **Problem / user:** Standard navigation apps pick efficient routes that may pass through unsafe, dark or poorly maintained areas. / pedestrians in unfamiliar areas
- **Domain / idea type:** mobility_transport + safety_security / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; JavaScript; frontend HTML; CSS; JavaScript; backend Flask; PyMongo; pandas; db MongoDB Atlas; hosting Docker
- **Tech/APIs:** Terraform (cloud, supporting, sponsor); Docker (framework, supporting); Mapbox API (maps_geo, core); MongoDB Atlas (database, core, sponsor); Flask (framework, supporting)
- **Sponsor APIs:** Terraform; MongoDB Atlas | fit: Targeted the Terraform prize by using Terraform with Docker to standardize how the web app is run.
- **Repo:** public, commits 126 (before/in/after event: 20/102/4), README detailed
- **Demo/writeup:** video True, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Government open data scraped with pandas; route waypoints scored by nearby crime, lights and road condition; MongoDB Atlas backend; Docker and Terraform used to standardize the dev environment.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; terraform_depth
- **Links:** [Devpost](https://devpost.com/software/saferoute-2iyzml) | [GitHub](https://github.com/CalebBunch/hackGT11)

### SentinelCV  (HackGT 11)

- **Prizes:** Magical Midway - 1st Place [1st]  (tier: track_winner)
- **Pitch:** Uses existing hospital room cameras and pose detection to track patient movement and alert nurses to risky immobility that causes pressure ulcers.
- **Problem / user:** Bedsores are common and preventable but rely on manual repositioning checks by hospital staff. / hospital nurses and caregivers
- **Domain / idea type:** health_wellness + safety_security / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend Bootstrap; JavaScript; backend Flask; OpenCV; Ultralytics YOLO; MediaPipe; db ; hosting 
- **Tech/APIs:** MediaPipe (ai_model, core); Ultralytics YOLO (ai_model, core); OpenCV (framework, core); Flask (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 5 (before/in/after event: 0/5/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims True (Cites 2.5 million patients per year, 9.1% vs 1.8% mortality, and $26.8 billion annual US cost of pressure injuries.)
- **Notes:** No extra sensors; MediaPipe and YOLO pose on RGB feeds for multiple patients; per-patient immobility thresholds in backend; Flask dashboard with GIF updates; cites mortality and cost statistics.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; event_start; event_end; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/project-restease) | [GitHub](https://github.com/Invincible-Rummy/SentinelCV)

### SnapSecure  (HackGT 11)

- **Prizes:** Winner SnapAR Skullcandy Grind True Wireless Earbuds [unknown]  (tier: sponsor_winner)
- **Pitch:** Gesture-based user authentication on Snap Spectacles that adjusts the environment to the user and tracks heart rate and tremors for health monitoring.
- **Problem / user:** Shared AR headsets need seamless user switching, and passive health signals like tremor could help early disease detection. / AR headset users in shared environments
- **Domain / idea type:** safety_security + health_wellness / new_category
- **Platforms / hardware / AI:** other; hardware / True / predictive_ml
- **Stack:** langs Python; TypeScript; JavaScript; frontend Lens Studio; Streamlit; backend Python; ONNX; SciPy; pandas; db ; hosting Heroku; Streamlit Cloud
- **Tech/APIs:** Snap Spectacles / Lens Studio (hardware_part, core, sponsor); ONNX (framework, supporting); SciPy / pandas (framework, supporting); Raspberry Pi (hardware_part, supporting); Streamlit (framework, supporting); Heroku (cloud, supporting)
- **Sponsor APIs:** Snap Spectacles; Lens Studio | fit: Targeted the SnapAR prize by building gesture authentication and health tracking on Snap Spectacles with Lens Studio.
- **Repo:** public, commits 18 (before/in/after event: 3/15/0), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 13, writeup medium, impact claims False
- **Notes:** Gesture models trained on just 3 samples per person; heart rate from a ballistocardiogram-style signal pipeline; models also run across headsets including Apple devices; second repo SnapSecureModelDemo linked.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; platforms
- **Links:** [Devpost](https://devpost.com/software/snapsecure) | [GitHub](https://github.com/ryan-gerhart/HackGT24_SnapSecure)

### SpecTackles  (HackGT 11)

- **Prizes:** SnapAR Soundview Speaker [unknown]  (tier: sponsor_winner)
- **Pitch:** Snap Spectacles AR lens that lets wearers toggle a real light switch by interacting with a tracked virtual marker, relayed through Firebase to a Raspberry Pi.
- **Problem / user:** Controlling physical devices usually requires phones or switches; the team wanted hands-free AR control of real-world objects. / smart-home users and AR wearers
- **Domain / idea type:** other + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / False
- **Stack:** langs JavaScript; TypeScript; Python; frontend Next.js; Lens Studio; backend Firebase; db Firebase; hosting 
- **Tech/APIs:** Snap Spectacles / Lens Studio (hardware_part, core, sponsor); Firebase (database, core); Raspberry Pi (hardware_part, core); Next.js (framework, supporting); Python (framework, supporting)
- **Sponsor APIs:** Snap Spectacles; Lens Studio | fit: Built a Lens Studio lens for Snap Spectacles using image tracking to trigger real-world device control.
- **Repo:** public, commits 23 (before/in/after event: 0/21/2), README thin
- **Demo/writeup:** video True, live none, screenshots 25, writeup medium, impact claims False
- **Notes:** End-to-end chain from Lens Studio image tracking to Firebase to a Raspberry Pi actuating a physical light switch; demo video listed.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; domain_primary
- **Links:** [Devpost](https://devpost.com/software/spectackles) | [GitHub](https://github.com/ktarafder/spectacles-frontend)

### WoundAI  (HackGT 11)

- **Prizes:** Best Emerging - 1st Place [1st]  (tier: track_winner)
- **Pitch:** Mobile app concept that classifies wound photos with a CNN, shows confidence scores, and helps patients track healing.
- **Problem / user:** Patients managing wounds lack an easy way to monitor healing and get a quick classification of wound type. / wound-care patients and clinicians
- **Domain / idea type:** health_wellness / data_or_analytics
- **Platforms / hardware / AI:** mobile_cross; web / False / vision
- **Stack:** langs Python; frontend React; backend OpenCV; TensorFlow; db ; hosting 
- **Tech/APIs:** Convolutional neural network (ai_model, core); OpenCV (framework, supporting); TensorFlow (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 5 (before/in/after event: 0/5/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Writeup is generic and partly inconsistent (How built mentions plant disease classification); one teammate notes an AI segmentation feature; stack listed as just Python and React.
- **Team size:** 3 | **Confidence:** medium | unverified: platforms; team_size; n_screenshots; event_start; event_end; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/woundai) | [GitHub](https://github.com/ankit06ch/WoundAI)


## HackGT 12

### Atlas  (HackGT 12)

- **Prizes:** Cedar - Best Use of CedarOS [unknown]; Ergo - Best Use of Mastra Agent Framework for Productivity [unknown]  (tier: sponsor_winner)
- **Pitch:** Desktop overlay that indexes codebases into a shared AI memory, with 3D call-graph visualization, so people and AI tools keep the same context.
- **Problem / user:** Developers lose context across AI prompts, huge codebases and onboarding; rebuilding context is slow and costly. / software engineers and AI-assisted dev teams
- **Domain / idea type:** dev_tools + productivity_workplace / dev_tool
- **Platforms / hardware / AI:** desktop / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs TypeScript; frontend React; Tailwind CSS; Three.js; backend Express.js; Node.js; Electron; db ; hosting 
- **Tech/APIs:** Mastra (framework, core, sponsor); CedarOS (framework, core, sponsor); Vercel AI SDK (framework, supporting); OpenAI (ai_model, supporting); Gemini (ai_model, supporting); Composio (other, supporting); Better Auth (auth, supporting); Electron (framework, core); Three.js (framework, supporting)
- **Sponsor APIs:** CedarOS; Mastra | fit: Built the agent layer on Mastra and the CedarOS framework, both listed in Built With, targeting the CedarOS and Mastra productivity-agent prizes.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims True (Cites that onboarding a new engineer in an enterprise can take 6 to 8 months.)
- **Notes:** Electron app styled after the macOS emoji picker; repo indexing with per-file summaries and Three.js 3D call graphs; built on Mastra agents and the CedarOS framework.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; prizes.placement
- **Links:** [Devpost](https://devpost.com/software/atlas-tlfpkz)

### BikeBuddy  (HackGT 12)

- **Prizes:** The Gadget Gallery - 1st Place [1st]  (tier: track_winner)
- **Pitch:** Bike add-on with handlebar turn-signal controller, rear LCD signal and brake display, camera feed, and phone app for speed and maps.
- **Problem / user:** Cyclists on campus feel unsafe at intersections because hand signaling is awkward and unclear to others. / student cyclists
- **Domain / idea type:** mobility_transport + safety_security / hardware_gadget
- **Platforms / hardware / AI:** mobile_cross; hardware / True / False
- **Stack:** langs TypeScript; C++; frontend React Native; Expo; backend ESP32 firmware; PlatformIO; Arduino framework; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); ESP32 camera (hardware_part, core); LCD display (hardware_part, core); React Native / Expo (framework, core); Apple Maps (maps_geo, supporting); PlatformIO (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 29 (before/in/after event: 8/21/0), README thin
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims False
- **Notes:** ESP32 rear box acts as Wi-Fi access point and web server streaming MJPEG to the app; brake detection fuses GPS, accelerometer, gyroscope and magnetometer; laser-cut acrylic housing.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/bikebuddy) | [GitHub](https://github.com/tsar-boomba/BikeBuddy)

### Caladrius  (HackGT 12)

- **Prizes:** The Curator's Cause - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Privacy-first triage assistant: patient-held medical passport shared by short-lived QR code, with an LLM agent asking follow-ups and ranking patients.
- **Problem / user:** Triage errors are common and stem from missing patient history and inefficient triage processes in emergency departments. / triage nurses, emergency providers and patients
- **Domain / idea type:** health_wellness + safety_security / automation_or_agent
- **Platforms / hardware / AI:** mobile_cross; web / False / llm_chat; agent_or_tool_use; predictive_ml
- **Stack:** langs Python; TypeScript; JavaScript; frontend React Native; Next.js; React; Tailwind CSS; backend FastAPI; Express.js; LangGraph; db MongoDB; hosting AWS S3
- **Tech/APIs:** OpenAI GPT-5 (ai_model, core); LangGraph (framework, core); AWS S3 (cloud, core); MongoDB (database, supporting); Amazon Transcribe Medical (cloud, token); Vertex AI MedGemma (ai_model, token)
- **Sponsor APIs:** 
- **Repo:** public, commits 71 (before/in/after event: 7/64/0), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims True (Cites 150M annual US ED visits and a study finding about a third of triage decisions are erroneous.)
- **Notes:** Rotating 60-second session ID points to temporary S3 bucket (AES-GCM planned but dropped); LangGraph agents with user-interrupt; pivoted from NFC after a sponsor engineer conversation; GPT-5 used instead of local model.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots; platforms; is_sponsor flags
- **Links:** [Devpost](https://devpost.com/software/caladrius) | [GitHub](http://github.com/midcha/Caladrius)

### CanDraw  (HackGT 12)

- **Prizes:** Ergo - Best Use of Mastra Agent Framework for Productivity [unknown]  (tier: sponsor_winner)
- **Pitch:** AI copilot for diagramming that turns text descriptions into system-design and UML diagrams, built on Mastra agents and the Cedar-OS UI library.
- **Problem / user:** Engineers sketch architecture diagrams by hand, which is slow when mapping components and dependencies. / engineers and developers
- **Domain / idea type:** productivity_workplace + dev_tools / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; JavaScript; SQL; frontend Next.js; React; Cedar-OS; backend Node.js; Mastra; db SQL; hosting 
- **Tech/APIs:** Mastra (framework, core, sponsor); Cedar-OS (framework, core); OpenAI (ai_model, core); Next.js (framework, supporting); SQL (database, supporting)
- **Sponsor APIs:** Mastra | fit: Used the Mastra agent framework to power the diagram-generation agent, targeting the Mastra productivity prize.
- **Repo:** public, commits 41 (before/in/after event: 4/36/1), README solid
- **Demo/writeup:** video True, live none, screenshots 22, writeup long, impact claims False
- **Notes:** Next.js front end uses Cedar-OS component library with a Mastra backend agent layer; diagrams generated from natural language.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/s-hrncfi) | [GitHub](https://github.com/V-prajit/CanDraw)

### CommitSense  (HackGT 12)

- **Prizes:** MLH - Best Domain Name from GoDaddy Registry [unknown]  (tier: sponsor_winner)
- **Pitch:** Developer tool that stores a company's code, commits and tickets in Snowflake and uses retrieval-augmented generation to explain legacy code as a narrative.
- **Problem / user:** Undocumented legacy code with cryptic variables and fixes takes weeks to decode. / developers working on legacy codebases
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs TypeScript; frontend React; Vite; Tailwind CSS; shadcn/ui; backend ; db Snowflake; hosting 
- **Tech/APIs:** Snowflake Cortex (ai_model, core, sponsor); Snowflake (database, core, sponsor); Gemini (ai_model, supporting, sponsor); React (framework, supporting)
- **Sponsor APIs:** Snowflake Cortex; Gemini | fit: Prize was MLH Best Domain Name from GoDaddy Registry; the page does not mention a GoDaddy domain, so the domain claim is not verified (project is built on Snowflake Cortex).
- **Repo:** public, commits 3 (before/in/after event: 0/2/1), README none
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** Combines commit history, ticket data and code comments into one story per explanation; Snowflake Cortex and Gemini for retrieval and generation.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; prizes.placement; sponsor_fit_note domain-name use not shown on page
- **Links:** [Devpost](https://devpost.com/software/commitsense-da5h6s) | [GitHub](https://github.com/Downbeatfoil/HackGT-CommitSense)

### Dispatch  (HackGT 12)

- **Prizes:** Winner Hall of Illusions - 1st Place [1st]  (tier: track_winner)
- **Pitch:** VR firefighter training in a burning maze where walking in place with a body-worn IMU tracker drives locomotion.
- **Problem / user:** First responders need realistic, affordable VR training, but treadmills and forward-only movement limit realism. / firefighters, EMTs and rescue teams
- **Domain / idea type:** safety_security + education / hardware_gadget
- **Platforms / hardware / AI:** desktop; hardware / True / False
- **Stack:** langs C#; C++; Python; frontend Unity; backend SteamVR/OpenVR driver; PlatformIO firmware; db ; hosting 
- **Tech/APIs:** Unity (framework, core); SteamVR/OpenVR (framework, core); PlatformIO (framework, supporting); IMU tracker (3D-printed) (hardware_part, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 44 (before/in/after event: 5/37/2), README thin
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Custom IMU chest tracker with microcontroller with PlatformIO firmware feeding a C++ SteamVR/OpenVR driver; fire spreads over time; three trackers built but only chest one used.
- **Team size:** 4 | **Confidence:** high | unverified: none
- **Links:** [Devpost](https://devpost.com/software/dispatch-u7fwrv) | [GitHub](https://github.com/RealityBenders/BoundlessVR)

### Doc McQuery  (HackGT 12)

- **Prizes:** Impiricus [unknown]  (tier: sponsor_winner)
- **Pitch:** Semantic search over hospital patient records: clinicians pick a patient and ask a query, and embeddings plus an LLM surface relevant record content.
- **Problem / user:** Clinicians struggle to find relevant details buried in long electronic medical records. / clinicians and hospital staff
- **Domain / idea type:** health_wellness + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / rag_or_search; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Vite; Tailwind CSS; backend Flask; Docker; db PostgreSQL; pgvector; hosting 
- **Tech/APIs:** PostgreSQL + pgvector (database, core); sentence-transformers (ai_model, core); OpenAI API (ai_model, core); NIH API (data_source, supporting); Synthea (data_source, supporting); Flask (framework, core); React (framework, supporting)
- **Sponsor APIs:**  | fit: Sponsor prize from Impiricus (healthcare tech); page does not describe any Impiricus-specific tool, so fit appears to be the healthcare-records problem domain.
- **Repo:** public, commits 66 (before/in/after event: 8/58/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 22, writeup long, impact claims False
- **Notes:** Tested on 1000 synthetic patient records generated with Synthea; Postgres with pgvector embeddings, plus an NIH API; page has only Backend and Frontend sections.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; n_screenshots; sponsor_fit_note; is_sponsor
- **Links:** [Devpost](https://devpost.com/software/dr-mcquery) | [GitHub](https://github.com/hhsiao24/Doc-McQuery)

### Dose  (HackGT 12)

- **Prizes:** Winner Best Overall - 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Sensor-equipped smart pill bottle that streams pill-count data to a web dashboard showing adherence scores and anomalies.
- **Problem / user:** Many chronic patients skip prescribed doses, costing the healthcare system heavily and muddying clinical trial data. / clinicians, caregivers and trial researchers
- **Domain / idea type:** health_wellness / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / False
- **Stack:** langs JavaScript; TypeScript; Python; Arduino C++; CSS; frontend Next.js; React; RadixUI; backend ; db Supabase; hosting 
- **Tech/APIs:** Xiao ESP32-C3 (hardware_part, core); TAL220 load cell (hardware_part, core); HX711 ADC (hardware_part, core); Supabase (database, core); Next.js (framework, core); RadixUI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 20 (before/in/after event: 0/20/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 4, writeup medium, impact claims True (Cites 30-50% non-adherence rate and $100-300B annual US cost.)
- **Notes:** 3D-printed bottle with ESP32-C3 and load cell detecting pill weight changes; firmware posts to a backend that computes stats into Supabase.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/dose-ebmo9z) | [GitHub](https://github.com/dawsonp2003/HackGT12-Dose)

### Dotify  (HackGT 12)

- **Prizes:** The Gadget Gallery - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Portable device that photographs an object, gets a Gemini description, and embosses a short Braille label with servo-driven pins.
- **Problem / user:** Most everyday packaged goods have no Braille, leaving visually impaired people dependent on workarounds to identify items. / visually impaired people
- **Domain / idea type:** accessibility / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision; llm_chat
- **Stack:** langs TypeScript; Python; C++; JavaScript; frontend HTML; CSS; JavaScript; TypeScript; backend Python; Arduino C++; db ; hosting 
- **Tech/APIs:** Google Gemini API (ai_model, core); Arduino UNO R4 (hardware_part, core); Micro servos x6 (hardware_part, core); DC motor and driver (hardware_part, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 1 (before/in/after event: 0/0/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Six micro servos press Braille dots into paper while a DC motor advances it; Arduino UNO R4 receives text over serial from a laptop web app; 3D-printed housing.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/dotify) | [GitHub](https://github.com/benmorrissey06/dotify)

### graphaura  (HackGT 12)

- **Prizes:** Crypt of Data - 1st Place [1st]  (tier: track_winner)
- **Pitch:** Turns photos and documents into an interactive 3D knowledge graph of people, places and moments, searchable with hybrid RAG.
- **Problem / user:** Personal memories spread across photos and documents are hard to explore and connect. / individuals organizing personal memories
- **Domain / idea type:** creative_media + ai_agents_infra / creative_tool
- **Platforms / hardware / AI:** web / False / rag_or_search; vision
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; react-force-graph-3d; backend FastAPI; structlog; R2R; db Neo4j; PostgreSQL; pgvector; Redis; Supabase; hosting 
- **Tech/APIs:** R2R (framework, core); Neo4j (database, core); pgvector (database, core); Redis (database, supporting); react-force-graph-3d (framework, core); Supabase (database, unclear)
- **Sponsor APIs:** 
- **Repo:** public, commits 11 (before/in/after event: 0/11/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup short, impact claims False
- **Notes:** Writeup is a short repo-style tech summary; pairs Neo4j graph with pgvector via external R2R service for ingestion, NER and RAG; 3D force-graph front end.
- **Team size:** 3 | **Confidence:** medium | unverified: ai_types; writeup_length
- **Links:** [Devpost](https://devpost.com/software/graphaura) | [GitHub](https://github.com/liamellison02/graphaura)

### Grindstone  (HackGT 12)

- **Prizes:** MLH - Best AI Application Built with Cloudflare [unknown]  (tier: sponsor_winner)
- **Pitch:** Goal-setting app where Mastra agents turn a rough goal into a dated SMART goal with milestones, with a SwiftUI client and Cloudflare backend.
- **Problem / user:** Habit trackers lack real milestones and customizable smart goals, and are not engaging to use. / people setting personal goals
- **Domain / idea type:** productivity_workplace + health_wellness / automation_or_agent
- **Platforms / hardware / AI:** mobile_ios; web / False / agent_or_tool_use; llm_chat
- **Stack:** langs Swift; TypeScript; frontend SwiftUI; backend Next.js; Mastra; Cloudflare Workers; AI SDK; db Cloudflare D1; hosting Cloudflare
- **Tech/APIs:** Cloudflare Workers (cloud, core, sponsor); Cloudflare D1 (database, core, sponsor); Mastra (framework, core); Gemini (ai_model, core); OpenAI (ai_model, supporting); SwiftUI (framework, core); Next.js (framework, supporting)
- **Sponsor APIs:** Cloudflare Workers; Cloudflare D1 | fit: Hosted the backend and database on Cloudflare (Workers, D1) with AI agents, targeting the MLH Best AI Application Built with Cloudflare prize.
- **Repo:** public, commits 13 (before/in/after event: 2/7/4), README solid
- **Demo/writeup:** video True, live none, screenshots 1, writeup short, impact claims False
- **Notes:** Two repos linked (site and iOS app); backend and database hosted on Cloudflare Workers with D1; Mastra agents call Gemini and OpenAI models.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/grindstone) | [GitHub](https://github.com/ScorelineSocial/site)

### Hall of Us  (HackGT 12)

- **Prizes:** Hall of Illusions - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Web uploader with AI tagging that turns hackathon photos into spatially anchored mixed-reality museum exhibits on Quest 3.
- **Problem / user:** Hackathon memories get lost as photos on phones rather than shared, explorable experiences. / hackathon attendees and event organizers
- **Domain / idea type:** creative_media + social_community / creative_tool
- **Platforms / hardware / AI:** web; other / True / llm_chat; vision; rag_or_search
- **Stack:** langs Python; C#; JavaScript; frontend React; Next.js; Unity; backend FastAPI; Pydantic; LangChain; db PostgreSQL; Amazon S3; hosting VPS; Coolify
- **Tech/APIs:** Meta Quest 3 / Meta XR SDK (hardware_part, core); Unity (framework, core); Cedar (framework, supporting); OpenAI (ai_model, core); LangChain (framework, supporting); Amazon S3 (cloud, supporting); PostgreSQL (database, supporting)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup medium, impact claims False
- **Notes:** Quest 3 app places exhibits via spatial anchors around the actual venue, with occlusion shaders; Cedar spells and natural-language filtering; self-hosted VPS with Coolify.
- **Team size:** 4 | **Confidence:** high | unverified: platforms (Quest 3 listed as other); ai_types; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/hall-of-us) | [GitHub](https://github.com/reeyank/hall-of-us)

### InfraBlocks  (HackGT 12)

- **Prizes:** Warp - Best Developer Tool [unknown]  (tier: sponsor_winner)
- **Pitch:** Drag-and-drop web editor where users diagram cloud infrastructure as blocks and get deployable Terraform code, with an AI assistant.
- **Problem / user:** Managing cloud infrastructure and Terraform syntax is complex for developers acting as part-time sysadmins. / developers managing cloud infrastructure
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind CSS; Radix UI; XYFlow; backend ; db ; hosting 
- **Tech/APIs:** Warp (other, supporting, sponsor); Cedar-OS (framework, supporting, sponsor); OpenAI (ai_model, supporting); XYFlow (framework, core); Terraform (other, core); Next.js (framework, supporting)
- **Sponsor APIs:** Warp; Cedar-OS | fit: Writeup says the team used Warp as its main development environment while building this developer tool, matching the Warp Best Developer Tool prize.
- **Repo:** public, commits 77 (before/in/after event: 4/72/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 10, writeup long, impact claims False
- **Notes:** Visual block diagram compiled into Terraform; team used the Warp terminal as primary dev environment and Cedar-OS for the AI assistant.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; prizes.placement
- **Links:** [Devpost](https://devpost.com/software/infrablocks) | [GitHub](https://github.com/Carbinski/InfraBlocks)

### Medicus  (HackGT 12)

- **Prizes:** Impiricus [unknown]  (tier: sponsor_winner)
- **Pitch:** Platform where medical device reps upload product and clinical data and doctors use AI search to find relevant devices, replacing in-person sales visits.
- **Problem / user:** Doctors are swamped by irrelevant information while device sales reps spend time and money traveling to hospitals. / healthcare providers and medical device sales reps
- **Domain / idea type:** health_wellness + retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web / False / rag_or_search; agent_or_tool_use; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Cedar; backend Mastra; Zod; React Email; db PostgreSQL; hosting Docker
- **Tech/APIs:** Mastra (framework, core); OpenAI (ai_model, core); Perplexity (ai_model, supporting); PostgreSQL (database, core); Cedar (framework, supporting); React Email (framework, supporting)
- **Sponsor APIs:**  | fit: Sponsor prize from Impiricus; the writeup frames the project around improving healthcare-provider engagement, which matches the sponsor's domain, but names no Impiricus tool.
- **Repo:** public, commits 20 (before/in/after event: 0/7/13), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** Targets healthcare-provider engagement; uses Mastra agents with Perplexity and OpenAI, Cedar UI, and React Email for outreach.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; sponsor_fit_note; is_sponsor
- **Links:** [Devpost](https://devpost.com/software/medicous) | [GitHub](https://github.com/Tjust032/gt-hackathon-2025)

### Ming Management Training, a personalized AI-native L&D coach  (HackGT 12)

- **Prizes:** MLH - Best Use of Gemini API [unknown]  (tier: sponsor_winner)
- **Pitch:** Multi-agent LLM coach that lets engineers moving into management practice realistic workplace scenarios and get personalized feedback.
- **Problem / user:** AI automation is displacing workers, and engineers stepping into management lack practice with real workplace situations. / engineers becoming managers
- **Domain / idea type:** education + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; frontend Next.js; React; shadcn; Tailwind CSS; Cedar-OS; backend Mastra; MCP; Cloudflare Workers; db ; hosting Cloudflare Workers
- **Tech/APIs:** Gemini API (ai_model, core, sponsor); Google Natural Language API (ai_model, supporting); Mastra (framework, core); Cedar-OS (framework, supporting); MCP (framework, supporting); Cloudflare Workers (cloud, supporting, sponsor); Next.js (framework, supporting)
- **Sponsor APIs:** Gemini API; Cloudflare Workers | fit: Used Gemini models (with Mastra multi-agent orchestration) to power the coaching scenarios, targeting the MLH Best Use of Gemini API prize.
- **Repo:** public, commits 353 (before/in/after event: 62/241/50), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 19, writeup medium, impact claims False
- **Notes:** Deployed on Cloudflare Workers; multi-agent design built with Mastra and Cedar-OS, plus Gemini and Google Natural Language API; MCP listed in stack.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/ming-management-training-a-personalized-ai-native-l-d-coach) | [GitHub](https://github.com/m3ru/HackGTProject)

### Orion  (HackGT 12)

- **Prizes:** Winner Best Emerging - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Onboarding assistant that ingests GitHub, Slack, docs and terminal commands, answering questions with cited sources and a reference timeline.
- **Problem / user:** New engineers lose weeks piecing together context scattered across Slack, PRs, docs and CI history. / new and existing software engineers
- **Domain / idea type:** dev_tools + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; JavaScript; Bash; frontend React; CSS; backend Flask; LangChain; scikit-learn; db PostgreSQL; ChromaDB; Supabase; hosting 
- **Tech/APIs:** ChromaDB (database, core); nomic-embed-text (ai_model, core); Gemini (ai_model, core); PostgreSQL (database, core); Supabase (database, unclear); GitHub API (data_source, core); Slack API (data_source, core); LangChain (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 112 (before/in/after event: 36/73/3), README solid
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims False
- **Notes:** Hybrid dense (nomic-embed-text) and TF-IDF sparse retrieval in ChromaDB; polls GitHub and Slack every second for incremental re-indexing; timeline UI shows cited sources.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/orion-owa3ry) | [GitHub](https://github.com/josephp1005/orion)

### RefNet  (HackGT 12)

- **Prizes:** Winner Best Overall - 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Citation-network explorer for research papers with an AI assistant that can manipulate the graph, plus notes and exports.
- **Problem / user:** Literature reviews are slow, requiring manual tracking of citations, trends and reference-manager entries. / student and academic researchers
- **Domain / idea type:** education + ai_agents_infra / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; JavaScript; frontend React; D3.js; Tailwind CSS; Cedar OS; backend Flask; NetworkX; Node.js; Mastra; db ; hosting AWS EC2; Vercel
- **Tech/APIs:** GPT-4o (ai_model, core); Cedar OS (framework, core); Mastra (framework, core); OpenAlex API (data_source, core); D3.js (framework, core); NetworkX (framework, supporting); AWS EC2 (cloud, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 71 (before/in/after event: 4/64/3), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 5, writeup long, impact claims False
- **Notes:** Cedar OS floating assistant acts on the frontend (highlights nodes, adds papers) via a Mastra/GPT-4o backend; exports JSON, BibTeX, PNG and PDF review.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/refnet-c04g9n) | [GitHub](https://github.com/Shreyas765/RefNet)

### Sideline  (HackGT 12)

- **Prizes:** PrizePicks - The Second Screen Experience [unknown]  (tier: sponsor_winner)
- **Pitch:** Second-screen app for live NFL games with sponsor-funded community micro bets, private team leaderboards and an AI explainer chatbot.
- **Problem / user:** Watching sports is passive, and beginners and communities lack engaging shared ways to follow games. / sports fans, including beginners
- **Domain / idea type:** entertainment_games + social_community / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / llm_chat; rag_or_search
- **Stack:** langs TypeScript; frontend React Native; Expo; backend Node.js; Express.js; ws; db Firebase; Firestore; hosting 
- **Tech/APIs:** Sportradar NFL API (data_source, core); OpenAI GPT (ai_model, core); Firebase (auth, core); Firestore (database, core); WebSockets (ws) (framework, core)
- **Sponsor APIs:**  | fit: Built a second-screen live-sports experience with in-game micro bets, matching the PrizePicks second-screen prize theme.
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 8, writeup medium, impact claims False
- **Notes:** Custom WebSocket wrapper over Sportradar NFL feed simulates live events; GPT generates micro-bet prompts; sponsor-backed bets convert community accuracy into charity donations.
- **Team size:** 4 | **Confidence:** medium | unverified: github_url (links to the HackGT12 organization page, not a project repo); is_sponsor flags; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/sideline)

### The Kick is Good  (HackGT 12)

- **Prizes:** PrizePicks - Signal from the Noise [unknown]  (tier: sponsor_winner)
- **Pitch:** Semi-automatic computer-vision system that measures field goal kick distance from video using user-provided field calibration and OpenCV tracking.
- **Problem / user:** Broadcasters do not publish how far field goals are kicked from; getting distance from video needs tracking. / football fans and analysts
- **Domain / idea type:** entertainment_games + other / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs Python; frontend React; backend OpenCV; NumPy; SciPy; Matplotlib; db ; hosting 
- **Tech/APIs:** OpenCV (framework, core); NumPy/SciPy (framework, supporting); React (framework, supporting)
- **Sponsor APIs:**  | fit: Targeted PrizePicks' Signal from the Noise challenge by extracting a new sports statistic (kick distance) from game video; no PrizePicks API shown.
- **Repo:** public, commits 9 (before/in/after event: 0/6/3), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup long, impact claims False
- **Notes:** Phased pipeline starting with manual field calibration, then OpenCV tracking, built by a two-person team with little prior CV experience.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; prizes.placement; domain_secondary
- **Links:** [Devpost](https://devpost.com/software/the-kick-is-good) | [GitHub](https://github.com/ColinVu/FGtracking)

### Tradegist  (HackGT 12)

- **Prizes:** Crypt of Data - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Analyzes uploaded trade history for behavioral biases like revenge trading using heuristics, logistic regression, an LLM classifier and an AI coach.
- **Problem / user:** Existing trading tools focus on markets, not on the psychological patterns that drive traders to lose money. / retail and active traders
- **Domain / idea type:** fintech_finance + mental_health / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; backend FastAPI; LangChain; db Supabase; Postgres; hosting 
- **Tech/APIs:** LLaMA (ai_model, core); Claude (ai_model, supporting); OpenAI (ai_model, supporting); Supabase (database, core); LangChain (framework, supporting); Logistic regression (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 60 (before/in/after event: 3/52/5), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Solo build; three-layer behavior pipeline (rules, logistic regression, LLaMA sequence classifier) plus RAG coaching via Claude and OpenAI; demo video has no audio.
- **Team size:** 1 | **Confidence:** medium | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/tradegist) | [GitHub](https://github.com/SohamAg/tradegist-ai)

### Vertex A11y  (HackGT 12)

- **Prizes:** Winner Best Emerging - 1st Place [1st]  (tier: track_winner)
- **Pitch:** Chrome extension that scans pages for WCAG/ADA problems, highlights them in place, and uses OpenAI to suggest fixes.
- **Problem / user:** Most websites fail accessibility guidelines because developers treat accessibility as an afterthought. / web developers
- **Domain / idea type:** accessibility + dev_tools / dev_tool
- **Platforms / hardware / AI:** browser_extension / False / llm_chat
- **Stack:** langs JavaScript; HTML; CSS; frontend Vanilla JavaScript; Motion.js; backend Node.js; db ; hosting 
- **Tech/APIs:** OpenAI API (ai_model, supporting); Chrome Extension (Manifest V3) (framework, core); Motion.js (framework, supporting); esbuild (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 27 (before/in/after event: 0/27/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims True (Cites 216 million visually impaired people and a WebAIM finding that over 96% of top sites fail guidelines.)
- **Notes:** Seven-category rule-based scanner in vanilla JS with Motion.js animations, esbuild bundling for Manifest V3, and OpenAI explanations; scoring A/AA/AAA tiers.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/vertex-a11y) | [GitHub](https://github.com/karandeol-26/vertex_A11y)

### vibesB2B  (HackGT 12)

- **Prizes:** Winner Best Overall - 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Meeting coach that aligns transcripts with audience emotion analysis and sends coaching feedback into Slack, Docs and Attio.
- **Problem / user:** Presenters leave meetings unsure how their message landed and lack concrete feedback on delivery. / presenters, sales and business professionals
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** desktop; web / False / llm_chat; vision; speech_or_voice; agent_or_tool_use
- **Stack:** langs Python; TypeScript; Node.js; frontend Electron; backend Flask; Mastra; Node.js; db SQLite; hosting Vercel; ngrok
- **Tech/APIs:** Mastra (framework, core, sponsor); Recall.ai Desktop SDK (other, core); AssemblyAI (ai_model, core); Gemini API (ai_model, core); MediaPipe Face Mesh (framework, core); OpenCV (framework, supporting); Keras/TensorFlow (framework, core); Attio CRM (other, supporting, sponsor); Slack (other, supporting); Electron (framework, core)
- **Sponsor APIs:** Mastra; Attio
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Electron app records meetings via Recall.ai; ResNet50+LSTM emotion model plus custom brow-furrow confusion metric merged by timestamp with AssemblyAI transcript; Mastra delivers output.
- **Team size:** 4 | **Confidence:** medium | unverified: team_size; is_sponsor flags for Mastra/Attio; sponsor_apis_used; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/vibesb2b) | [GitHub](https://github.com/atoniolo76/vibeb2b)

### VisionNav  (HackGT 12)

- **Prizes:** The Curator's Cause - 1st Place [1st]  (tier: track_winner)
- **Pitch:** iPhone camera and LiDAR app that guides visually impaired users around obstacles and to objects using spatial audio in AirPods.
- **Problem / user:** Visually impaired people lack affordable, accessible tools for navigating everyday surroundings independently. / visually impaired people
- **Domain / idea type:** accessibility / social_good
- **Platforms / hardware / AI:** mobile_ios / True / vision; speech_or_voice; llm_chat
- **Stack:** langs Swift; Python; frontend Swift; Xcode; backend Python; OpenCV; NumPy; db ; hosting 
- **Tech/APIs:** Ultralytics YOLO (ai_model, core); Gemini (ai_model, supporting); MediaPipe (framework, supporting); OpenCV (framework, supporting); iPhone LiDAR (hardware_part, core); AirPods spatial audio (hardware_part, core); Google speech-to-text (ai_model, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 31 (before/in/after event: 3/28/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup long, impact claims True (Cites 7.3M visually impaired US adults, 1M fully blind, 70% unemployed; claims over 20 fps processing.)
- **Notes:** Swift app streams MJPEG and LiDAR packets over WebSockets to a Python server running YOLO; hand-guidance mode uses hand tracking and pitch/tempo audio cues at over 20 fps.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/vision-app) | [GitHub](https://github.com/jaeheonshim/VisionNav)

### Vital  (HackGT 12)

- **Prizes:** Impiricus [unknown]  (tier: sponsor_winner)
- **Pitch:** Agentic workflow platform for clinicians with a real-time research stream of new guidelines and patient cards that an AI helper can sort.
- **Problem / user:** Physicians struggle to keep up with constant new medical literature and drug approvals while managing patients. / physicians and clinicians
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind CSS; shadcn/ui; backend ; db Supabase; hosting 
- **Tech/APIs:** Impiricus data feed (data_source, core, sponsor); Cedar-OS (framework, core, sponsor); OpenAI (ai_model, core); Supabase (database, supporting)
- **Sponsor APIs:** Impiricus data feed; Cedar-OS | fit: Integrated the sponsor Impiricus' data feed into a real-time guideline research stream for clinicians.
- **Repo:** public, commits 30 (before/in/after event: 1/27/2), README none
- **Demo/writeup:** video True, live none, screenshots 25, writeup medium, impact claims False
- **Notes:** Research Stream integrates Impiricus' own data feed; promptable helper agent reorders patient cards using Cedar-OS.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; prizes.placement
- **Links:** [Devpost](https://devpost.com/software/vital-1qsh6u) | [GitHub](https://github.com/IndianaJonesR/vital)

### Waste2Taste  (HackGT 12)

- **Prizes:** MLH - Best Use of Snowflake API [unknown]  (tier: sponsor_winner)
- **Pitch:** Camera system over dining hall conveyor belts measures leftover food per plate with vision models and sends data to Snowflake for chef insights.
- **Problem / user:** Dining halls throw away large amounts of food without data to tell chefs what goes uneaten. / dining hall chefs and food-service managers
- **Domain / idea type:** sustainability_climate + food_nutrition / data_or_analytics
- **Platforms / hardware / AI:** web; hardware / True / vision; predictive_ml
- **Stack:** langs Python; TypeScript; JavaScript; frontend ; backend ; db Snowflake; Supabase; hosting 
- **Tech/APIs:** Snowflake (database, core, sponsor); Snowflake Cortex (ai_model, core, sponsor); OWL-ViT (ai_model, core); Segment Anything (ai_model, core); GroundingDINO (ai_model, supporting); Depth Anything (ai_model, supporting); Raspberry Pi (hardware_part, core); Supabase (database, supporting)
- **Sponsor APIs:** Snowflake; Snowflake Cortex | fit: Pipes plate-waste measurements into Snowflake and uses Snowflake Cortex to produce insights for chefs, targeting the MLH Best Use of Snowflake API prize.
- **Repo:** public, commits 6 (before/in/after event: 0/5/1), README solid
- **Demo/writeup:** video True, live none, screenshots 22, writeup long, impact claims False
- **Notes:** Raspberry Pi capture feeds OWL-ViT/GroundingDINO detection, Segment Anything and Depth Anything to estimate waste volume; analytics in Snowflake Cortex dashboard.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; prizes.placement
- **Links:** [Devpost](https://devpost.com/software/waste2taste-etwp34) | [GitHub](https://github.com/gab-conde/hackgt-25)


## HackGT 13

### Athena  (HackGT 13)

- **Prizes:** NSA: Hearsay: The Audio Authentication Challenge - 2nd Place [2nd]  (tier: sponsor_winner)
- **Pitch:** Desktop agent for Google Meet that detects AI-cloned voices, masks keystroke sounds against acoustic attacks, and redacts spoken secrets.
- **Problem / user:** Voice-cloned callers and microphone-based keystroke eavesdropping can leak passwords and codes during video calls. / people on video calls handling sensitive information
- **Domain / idea type:** safety_security + ai_agents_infra / new_category
- **Platforms / hardware / AI:** desktop; web / False / llm_chat; agent_or_tool_use; speech_or_voice; predictive_ml
- **Stack:** langs Python; JavaScript; frontend pywebview; backend FastAPI; WebSocket; db ; hosting 
- **Tech/APIs:** XLS-R (Hugging Face Transformers) (ai_model, core); LightGBM (framework, supporting); PyTorch (framework, core); Google Gemini 2.5 Flash (ai_model, core); Backboard (other, supporting, sponsor); Vosk (ai_model, core); Google Meet (other, core); librosa (framework, supporting)
- **Sponsor APIs:** Backboard | fit: Trained fused XLS-R and gradient-boosted real-vs-synthetic voice detector on the NSA Hearsay challenge and reported organizer scores.
- **Repo:** public, commits 1 (before/in/after event: 0/1/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 10, writeup long, impact claims True (Reports measured results: EER 2.5%, 80% per-key typing read, attacker driven to 2.8% chance level, STOI 0.98.)
- **Notes:** Injects audio bridge into Chrome Meet session via DevTools; self-built keystroke attacker versus LLM-driven adversarial shield; reports organizer metrics minDCF 0.058, EER 2.5%; 90 mock-driver tests.
- **Team size:** 4 | **Confidence:** high | unverified: tech_items.is_sponsor; stack_database
- **Links:** [Devpost](https://devpost.com/software/callguard) | [GitHub](https://github.com/georgia-mellon/athena ; https://github.com/danmano411/hearsay)

### ATP - Accessible to Prescription  (HackGT 13)

- **Prizes:** Impiricus: Build the next HCP Engagement Tool - 1st Place [1st]; Notability: Trust the Process [unknown]  (tier: sponsor_winner)
- **Pitch:** Voice AI agent phones insurers for prior authorization and hands the live call to the doctor when clinical input is needed, then resumes.
- **Problem / user:** Doctors spend many hours weekly on insurer calls for prior authorization, time taken from patient visits. / doctors and medical practice staff
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; frontend React; backend FastAPI; db ; hosting 
- **Tech/APIs:** ElevenLabs Agents (ai_model, core, sponsor); ElevenLabs voice cloning (ai_model, core, sponsor); LiveKit (other, core); Plivo (telecom, core); OpenAI (ai_model, core); Slack (other, supporting); Notability (other, supporting, sponsor)
- **Sponsor APIs:** ElevenLabs; Notability | fit: Built an agent that handles insurer prior-authorization calls and escalates to the physician, addressing the Impiricus HCP engagement brief; Notability used for whiteboarding flows.
- **Repo:** public, commits 2 (before/in/after event: 0/2/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims True (Cites a medical director spending about 10 hours weekly on insurers and estimating 25-30 more patients weekly.)
- **Notes:** Insurer stays on the line while doctor's phone rings; doctor presses # to hand back; ElevenLabs voice clone of doctor; facts link to supporting transcript turns; Slack briefing.
- **Team size:** 2 | **Confidence:** high | unverified: tech_items.is_sponsor; stack_database
- **Links:** [Devpost](https://devpost.com/software/atp) | [GitHub](https://github.com/notvasub/ATP-Access-to-Prescription)

### Bear With Me  (HackGT 13)

- **Prizes:** MLH: Best Domain from .tech [unknown]  (tier: sponsor_winner)
- **Pitch:** Kid-first pediatric intake system: a child tablet companion character gathers information during the exam-room wait for parents and clinicians.
- **Problem / user:** Children and parents face anxiety and paperwork in waiting rooms with little explanation of what is happening. / pediatric patients, parents and clinics
- **Domain / idea type:** health_wellness + mental_health / new_category
- **Platforms / hardware / AI:** web / False / speech_or_voice; llm_chat; vision
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind CSS; Web Audio API; backend Node.js; Supabase Realtime; Zod; db PostgreSQL; Supabase; hosting Vercel
- **Tech/APIs:** .TECH domain (other, supporting, sponsor); Grok / xAI voice and TTS (ai_model, core); Silero VAD (ONNX Runtime Web) (ai_model, supporting); OpenCV (framework, supporting); Supabase (database, core); Vercel (cloud, supporting); Next.js (framework, core)
- **Sponsor APIs:** .TECH domain | fit: Deployed the app at a .tech domain (bearwithme.tech), matching the MLH Best Domain from .tech prize.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 31, writeup long, impact claims False
- **Notes:** Three connected experiences (child tablet, parent, clinician); voice interaction with Grok TTS/voice, on-device Silero VAD via ONNX Runtime Web, Supabase realtime; deployed on a .tech domain.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/bear-with-me-8ijcef)

### Bump  (HackGT 13)

- **Prizes:** Oracle of the Deep - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** iPhone app where two nearby people tap phones together and get specific shared-interest conversation starters from a user-approved voice-built profile.
- **Problem / user:** People near each other want to talk but lack context for a first conversation, and loneliness is widespread. / students and people at events or classes
- **Domain / idea type:** social_community + mental_health / new_category
- **Platforms / hardware / AI:** mobile_ios; web / False / llm_chat; speech_or_voice; recommendation
- **Stack:** langs Swift; Node.js; frontend SwiftUI; ActivityKit; WidgetKit; backend Node.js 20; db Supabase Realtime; hosting Render; Vercel
- **Tech/APIs:** Grok (xAI) voice, STT, TTS (ai_model, core, sponsor); Nearby Interaction (UWB) (framework, core); MultipeerConnectivity (framework, core); Core Motion (framework, core); Supabase Realtime (database, supporting); Render (cloud, supporting); Apple Foundation Models (ai_model, supporting); Cursor (other, token)
- **Sponsor APIs:** Grok (xAI)
- **Repo:** public, commits 86 (before/in/after event: 0/86/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims True (Cites WHO estimate of about 1 in 6 people experiencing loneliness and published studies on fear of talking to strangers.)
- **Notes:** Bump detected via Core Motion plus UWB ranging and MultipeerConnectivity, refusing ambiguous pairings; matching done on-device before Grok phrases talking points, with Apple Foundation Models fallback.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor flags
- **Links:** [Devpost](https://devpost.com/software/bump-it1fjy) | [GitHub](https://github.com/bump-hackgt/bump)

### Campfire  (HackGT 13)

- **Prizes:** MLH: Best Use of backboard.io [unknown]  (tier: sponsor_winner)
- **Pitch:** WhatsApp bot that joins a travel group chat, captures messages, photos and voice notes, and turns the trip into a memory timeline.
- **Problem / user:** The best moments of group trips stay buried in chat threads and never make it into shareable memories. / friend groups on trips
- **Domain / idea type:** social_community + creative_media / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / llm_chat; rag_or_search; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend React; Vite; D3.js; React Router; backend Flask; Node.js; Baileys; Celery; Gunicorn; SQLAlchemy; db PostgreSQL; pgvector; Redis; hosting Vultr; Docker; Caddy
- **Tech/APIs:** Backboard.io (ai_model, core, sponsor); Vultr (cloud, supporting, sponsor); OpenAI (ai_model, core); ElevenLabs (ai_model, supporting); Muse Spark (ai_model, supporting); WhatsApp via Baileys (other, core); pgvector (database, supporting); Celery + Redis (framework, supporting)
- **Sponsor APIs:** Backboard.io; Vultr | fit: Used Backboard as long-term memory for the OpenAI agent to carry context across days of a group's trip.
- **Repo:** public, commits 57 (before/in/after event: 0/57/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 16, writeup long, impact claims False
- **Notes:** Node.js Baileys service bridges WhatsApp to a Flask/Celery backend with pgvector memory; D3/TopoJSON map visualization; hosted on Vultr behind Caddy.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/campfire-3jo6wc) | [GitHub](https://github.com/Suhas0723/Campfire)

### ClearPath  (HackGT 13)

- **Prizes:** Impiricus: Build the next HCP Engagement Tool - 3rd Place [3rd]  (tier: sponsor_winner)
- **Pitch:** Prior-authorization engine built from a real insurance policy plus a shared care-team workspace and an AI patient assistant named Ava.
- **Problem / user:** Prior authorization is opaque to doctors and patients, and care teams lack shared context about next steps and ownership. / doctors, reviewers and patients
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; rag_or_search; agent_or_tool_use
- **Stack:** langs Python; TypeScript; SQL; frontend Next.js; React; Tailwind CSS; backend FastAPI; Pydantic; Uvicorn; db ; hosting Vercel
- **Tech/APIs:** Google Gemini (ai_model, supporting, sponsor); Meta Muse Spark (ai_model, supporting, sponsor); Muse Voice (ai_model, supporting, sponsor); OpenAI (ai_model, supporting); ElevenLabs (ai_model, supporting, sponsor); Grok (ai_model, supporting); openFDA (data_source, supporting); NIH RxNav (data_source, supporting); FHIR (framework, supporting)
- **Sponsor APIs:** Google Gemini; Meta Muse Spark; ElevenLabs | fit: Pitched PA workflow plus shared chart as an HCP engagement workspace for Impiricus; also targeted Meta, AI/ML and Gemini/ElevenLabs tracks.
- **Repo:** public, commits 41 (before/in/after event: 0/41/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup long, impact claims True (States counts from the processed policy: 253-page document, 90 categories (41 required, 41 not required, 8 conditional).)
- **Notes:** Insurance PDF structured into 90 benefit categories with page references; FHIR-shaped resources; second-model validation; the shared-care app and PA engine are separate workstreams, not yet connected.
- **Team size:** 3 | **Confidence:** high | unverified: stack_database; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/clearpath-chvrpy) | [GitHub](https://github.com/hariomsah01/HackGT-13 ; https://github.com/sumanshah7/ClearPath.git)

### Degrees  (HackGT 13)

- **Prizes:** MLH: Best Use of Gemini API [unknown]  (tier: sponsor_winner)
- **Pitch:** Mobile app that builds a social graph from in-person meetings (QR or room codes) and uses Gemini to form small groups and plan a real outing.
- **Problem / user:** College students meet many people but few acquaintances turn into lasting connections. / college students
- **Domain / idea type:** social_community / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / False / recommendation; llm_chat; rag_or_search
- **Stack:** langs TypeScript; frontend React Native; Expo; NativeWind; Zustand; TanStack Query; backend Hono; Node.js; Zod; db PostgreSQL; pgvector; Supabase; hosting Netlify
- **Tech/APIs:** Gemini (embeddings + Maps grounding) (ai_model, core, sponsor); Google Maps / Places (maps_geo, core); Supabase (database, core); pgvector (database, supporting); Ticketmaster API (data_source, supporting); React Native / Expo (framework, core)
- **Sponsor APIs:** Gemini API | fit: Used Gemini embeddings to rank similar-interest connections, Gemini to compose groups with explanations, and Gemini with Maps grounding to pick venues.
- **Repo:** public, commits 111 (before/in/after event: 0/109/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** Gemini embeddings rank candidates on the connection graph, Gemini with Google Maps grounding picks venues, and Places fills details; Ticketmaster API also listed.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/degrees-gdibjk) | [GitHub](https://github.com/prbhagam/degrees)

### DocSpot  (HackGT 13)

- **Prizes:** Impiricus: Build the next HCP Engagement Tool - 2nd Place [2nd]  (tier: sponsor_winner)
- **Pitch:** Physician network map that recommends specialists for referrals, drafts a privacy-checked e-fax, and invites non-members to connect on Impiricus.
- **Problem / user:** Physicians struggle to reach specialists and colleagues, especially as practices are acquired and in rural areas, which hampers referrals. / physicians and referring clinics
- **Domain / idea type:** health_wellness + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; recommendation
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; SVG; backend FastAPI; Pydantic; Uvicorn; db ; hosting Render
- **Tech/APIs:** OpenAI gpt-4.1-mini (ai_model, supporting); NPI Registry data (data_source, core); Resend Email API (other, supporting); FastAPI (framework, core); Impiricus network concept (other, unclear, sponsor)
- **Sponsor APIs:**  | fit: Framed around Impiricus's opted-in HCP network to bring non-members into it via referral interactions; no sponsor API listed.
- **Repo:** public, commits 31 (before/in/after event: 0/31/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup long, impact claims True (Cites survey and report stats, e.g. 82% of US physicians employed by hospitals or corporations and 76.4% trusting other physicians.)
- **Notes:** Demo uses 253 cleaned NPI Registry clinician records; SVG specialty-grouped network map; patient consent form signed via emailed link before details are shared; QR codes on fax previews.
- **Team size:** 3 | **Confidence:** high | unverified: stack_database
- **Links:** [Devpost](https://devpost.com/software/docspot) | [GitHub](https://github.com/tvisha-t/docSpot)

### DopaMarine  (HackGT 13)

- **Prizes:** Aramco: A Marina's Mission - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Turns uploaded lecture material into a sea-creature study game with Pokemon-style AR duels, XP progression and a practice-exam boss.
- **Problem / user:** Students procrastinate and lose focus while studying, so they need motivating, learning-style-adapted study tools. / students
- **Domain / idea type:** education + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; generative_media
- **Stack:** langs JavaScript; HTML; CSS; frontend React; Vite; Tailwind CSS; Leaflet; backend Node.js; Express; WebSockets; db MongoDB Atlas; hosting 
- **Tech/APIs:** Google Gemini API (ai_model, core); MongoDB Atlas (database, core); Leaflet / OpenStreetMap (maps_geo, supporting); WebSockets (framework, supporting); Figma (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 26 (before/in/after event: 0/26/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 0, writeup long, impact claims False
- **Notes:** Browser-only AR with device motion and on-device face detection mini-games; Gemini output validated server-side with retries and fallback models; MongoDB with local JSON fallback.
- **Team size:** 3 | **Confidence:** high | unverified: sponsor_apis_used; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/dopamarine) | [GitHub](https://github.com/Srihansi-Sagi/dopamarine)

### FlyBy  (HackGT 13)

- **Prizes:** Best Overall - 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Simulated search-and-rescue system pairing a fly-vision-inspired drone reflex with AI ground control that ranks sightings for human-approved dispatch.
- **Problem / user:** After disasters, rescuers lose time sorting fragmented drone footage and detector flags before reaching trapped survivors. / search-and-rescue responders
- **Domain / idea type:** safety_security + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; vision; predictive_ml
- **Stack:** langs Python; TypeScript; frontend Three.js; Vite; TypeScript; backend FastAPI; WebSockets; db MongoDB Atlas; hosting 
- **Tech/APIs:** flyvis (ai_model, core); Laya (ai_model, core); Grok (xAI API) (ai_model, core); MongoDB Atlas (database, supporting); Three.js (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 83 (before/in/after event: 0/80/3), README detailed
- **Demo/writeup:** video True, live none, screenshots 3, writeup long, impact claims True (Cites a review that 85-95% of rubble survivors in three earthquakes were rescued within 24 hours.)
- **Notes:** Uses pretrained flyvis fly-brain model with a fitted readout for obstacle braking, a fine-tuned Laya model for triage scoring, Grok for field reports, and a 3D neuron activity viewer; all in simulation.
- **Team size:** 3 | **Confidence:** high | unverified: sponsor flags on Grok, MongoDB Atlas, Laya
- **Links:** [Devpost](https://devpost.com/software/flyby-fdxcua) | [GitHub](https://github.com/monishramj/flyby)

### Fourteenth Floor  (HackGT 13)

- **Prizes:** The Lighthouse Laboratory - 1st Place [1st]  (tier: track_winner)
- **Pitch:** Turns a project folder into a 3D office where a manager agent and specialist Codex agents work visibly, with evidence required to close tasks.
- **Problem / user:** Running several AI agents means watching scrolling logs, and agents can claim work is done without proof. / developers running multiple AI coding agents
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web; desktop / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; JavaScript; Python; frontend Three.js; Vite; WebXR; backend Node.js; Codex app server; MCP; db ; hosting 
- **Tech/APIs:** Codex app server (ai_model, core); Three.js (framework, core); Blender MCP (framework, supporting); MCP (framework, core); WebXR (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 3 (before/in/after event: 0/3/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Agents run as sandboxed Codex sessions via its app server; evidence gate requires diffs or observed passing tests; office built with Blender MCP; Three.js scene with WebXR mode untested on hardware.
- **Team size:** 4 | **Confidence:** high | unverified: sponsor flags on Codex
- **Links:** [Devpost](https://devpost.com/software/fourteenth) | [GitHub](https://github.com/Pudging/fourteenth-floor)

### HeirLoom  (HackGT 13)

- **Prizes:** Meta: Bringing People Closer Together with AI - Winner [unknown]  (tier: sponsor_winner)
- **Pitch:** iOS app where a voice AI companion named Loomie interviews family members to turn memories into a shared living family archive.
- **Problem / user:** Families scattered by distance and generations lose shared stories and a sense of connection. / families across generations
- **Domain / idea type:** social_community + creative_media / new_category
- **Platforms / hardware / AI:** mobile_ios / False / llm_chat; speech_or_voice
- **Stack:** langs Swift; frontend SwiftUI; backend ; db MongoDB; hosting 
- **Tech/APIs:** Grok (ai_model, core); Backboard.io (other, supporting); MongoDB (database, supporting); Swift/SwiftUI (framework, core)
- **Sponsor APIs:**  | fit: Targeted Meta's Bringing People Closer Together with AI theme with a voice AI companion for family memories; Built With does not list a Meta model.
- **Repo:** public, commits 40 (before/in/after event: 0/39/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 25, writeup long, impact claims False
- **Notes:** Native Swift/SwiftUI app with full-duplex low-latency voice streaming and a hand-designed parchment and Polaroid aesthetic with no AI-generated assets.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; prizes.placement; writeup_sections beyond accomplishments
- **Links:** [Devpost](https://devpost.com/software/heirloom-3q2bn9) | [GitHub](https://github.com/Adalo-Gusa/SPIRE_GT_Hacks)

### Hey Buddy  (HackGT 13)

- **Prizes:** MLH: Best Use of ElevenLabs [unknown]  (tier: sponsor_winner)
- **Pitch:** Real-time phone interpreter you add to an ordinary call by dialing a number, translating speech between languages with no app.
- **Problem / user:** People who understand English but freeze on calls with pharmacies, clinics or utilities need live interpretation. / non-native English speakers and their families
- **Domain / idea type:** accessibility + telecom_networking / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / speech_or_voice; llm_chat
- **Stack:** langs TypeScript; frontend React; Vite; Tailwind CSS; backend Node.js; Express.js; Socket.IO; WebSockets; db ; hosting Railway
- **Tech/APIs:** ElevenLabs (ai_model, core, sponsor); Twilio (telecom, core); Meta Muse Spark (ai_model, supporting); Grok (xAI) (ai_model, supporting); WhatsApp (telecom, supporting); Railway (cloud, supporting)
- **Sponsor APIs:** ElevenLabs | fit: Uses ElevenLabs for speech in the live interpreter pipeline, matching the MLH Best Use of ElevenLabs prize.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Twilio Media Streams pipeline of speech-to-text, translation and ElevenLabs speech back into the same call; verified on real calls in Turkish and tested in other languages.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; prizes.placement; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/hey-buddy-3e4utl) | [GitHub](https://github.com/eymen160/hey-buddy)

### Inkling  (HackGT 13)

- **Prizes:** Notability: Trust the Process [unknown]  (tier: sponsor_winner)
- **Pitch:** Note-taking canvas that keeps erased handwriting as ghost ink, pairs corrections with lecture timestamps and turns mistakes into a study plan.
- **Problem / user:** Note apps delete mistakes, discarding the signal about what a student misunderstood. / students taking handwritten notes
- **Domain / idea type:** education / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind CSS; backend Node.js; db PostgreSQL; TimescaleDB; SQLite; hosting Railway
- **Tech/APIs:** Notability (other, supporting, sponsor); Gemini (ai_model, supporting); Groq (ai_model, supporting); ElevenLabs (ai_model, supporting, sponsor); TimescaleDB (Tiger Data) (database, supporting, sponsor); Playwright (framework, supporting)
- **Sponsor APIs:** Notability; ElevenLabs; Tiger Data | fit: Has a dedicated section on using Notability Pro Smart Notes for research and design, aimed at the Notability Trust the Process prize.
- **Repo:** public, commits 7 (before/in/after event: 0/7/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 43, writeup long, impact claims False
- **Notes:** Every stroke is stamped with lecture time, speed and pressure; solo build that used Notability Pro for its own research notes and quizzes.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; prizes.placement
- **Links:** [Devpost](https://devpost.com/software/inkling-ud1re3) | [GitHub](https://github.com/PranavNagothu/Inkling)

### Lullabuy  (HackGT 13)

- **Prizes:** VISA: Reimagine Shopping - Winner [unknown]  (tier: sponsor_winner)
- **Pitch:** Payment-hold checkout for used baby gear that reads an item's label and checks recall databases before funds move, reversing the Visa hold if recalled.
- **Problem / user:** Parents buy secondhand strollers and cribs from strangers with no easy way to know whether they were recalled. / parents buying secondhand baby gear
- **Domain / idea type:** safety_security + fintech_finance / new_category
- **Platforms / hardware / AI:** web; mobile_cross / False / vision; llm_chat; rag_or_search
- **Stack:** langs TypeScript; Python; frontend Next.js; React Native; Expo; MapLibre; backend MCP; db MongoDB Atlas; hosting Vercel
- **Tech/APIs:** Visa Acceptance / Microform / Token Management (payments, core, sponsor); Visa Trusted Agent Protocol (payments, supporting, sponsor); Gemini / Vertex AI (ai_model, core); CPSC recall API (data_source, core); MongoDB Atlas Vector Search (database, supporting); ElevenLabs (ai_model, supporting); Solana (other, token); Notability (other, supporting, sponsor)
- **Sponsor APIs:** Visa Acceptance; Visa Microform; Visa Token Management Service; Visa Trusted Agent Protocol | fit: Holds a Visa-backed payment until a recall check passes, built on Visa Acceptance, Microform and Token Management for the Reimagine Shopping prize.
- **Repo:** public, commits 83 (before/in/after event: 0/83/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 13, writeup long, impact claims True (Cites roughly 100 infant deaths linked to a recalled Fisher-Price sleeper.)
- **Notes:** Camera label reading is checked against CPSC, NHTSA and federal resale bans; page also documents using Notability for architecture notes and quiz prep.
- **Team size:** 2 | **Confidence:** medium | unverified: ui_polish; prizes.placement; writeup_sections beyond inspiration
- **Links:** [Devpost](https://devpost.com/software/lullabuy) | [GitHub](https://github.com/StephenSook/secondhand-safe)

### MiiHab: Get Back in the Game  (HackGT 13)

- **Prizes:** The Lighthouse Laboratory - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Wii-style VR physical therapy using Meta Quest and AirPods motion sensing, with a voice AI coach and a live clinician portal.
- **Problem / user:** Patients get about an hour a week with a therapist and do repetitive rehab alone, unmotivated and unmonitored between visits. / physical therapy patients and their clinicians
- **Domain / idea type:** health_wellness + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** other; web / True / llm_chat; agent_or_tool_use; speech_or_voice; recommendation
- **Stack:** langs C#; Swift; JavaScript; TypeScript; Python; frontend Unity; React; backend Node.js; db Supabase; hosting Vercel; Tailscale
- **Tech/APIs:** Meta Quest (hardware_part, core); AirPods CoreMotion (hardware_part, core); Unity (framework, core); Meta Muse Spark (ai_model, core, sponsor); ElevenLabs Conversational AI (ai_model, core, sponsor); Tailscale (other, supporting); Supabase (database, supporting); Claude (ai_model, unclear)
- **Sponsor APIs:** Meta Muse Spark; ElevenLabs | fit: Built a health-focused rehab system around Meta Quest and Muse Spark with a clinician EHR loop.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Two Macs each stream one AirPods pair over Tailscale to a relay because macOS allows one pair at a time; headset head tracking measures trunk lean; adapter reshapes ElevenLabs requests for Muse.
- **Team size:** 4 | **Confidence:** high | unverified: tech_items.is_sponsor; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/rehabmii-get-back-in-the-game) | [GitHub](https://github.com/hackgt13/rehabmii)

### Nudge  (HackGT 13)

- **Prizes:** Meta: Bringing People Closer Together with AI - Winner [unknown]  (tier: sponsor_winner)
- **Pitch:** iOS app that lowers friction to calling close friends by suggesting when to call and surfacing photos tied to things you mentioned, built on AWS AI services.
- **Problem / user:** People call the friends and family they love most the least, because starting a call has friction and uncertainty. / people keeping in touch with close friends and family
- **Domain / idea type:** social_community / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / False / llm_chat; recommendation; vision; speech_or_voice; rag_or_search
- **Stack:** langs Swift; TypeScript; frontend SwiftUI; backend AWS Lambda; API Gateway; Amazon SQS; AWS CDK; Node.js; db DynamoDB; S3 Vectors; hosting AWS
- **Tech/APIs:** Amazon Bedrock (Nova, Titan) (ai_model, core); Amazon Rekognition (ai_model, core); Amazon Transcribe (ai_model, supporting); Amazon Chime SDK (other, core); AWS Lambda / API Gateway / DynamoDB / SQS (cloud, core); S3 Vectors (database, supporting); Apple Push Notifications (other, supporting); Claude Code (other, supporting)
- **Sponsor APIs:**  | fit: Targeted Meta's 'Bringing People Closer Together with AI' challenge by building an AI app that nudges people to call friends; page text names no Meta tools (AWS stack).
- **Repo:** public, commits 97 (before/in/after event: 0/97/0), README solid
- **Demo/writeup:** video True, live none, screenshots 28, writeup long, impact claims False
- **Notes:** Built almost entirely on AWS (Bedrock Nova and Titan, Rekognition, Transcribe, Chime SDK, Lambda, S3 Vectors) and written with Claude Code; long writeup with tooling section.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots; writeup_sections
- **Links:** [Devpost](https://devpost.com/software/nudge-hcvxfq) | [GitHub](https://github.com/AlanRoybal/hackgt)

### PledgeCheck  (HackGT 13)

- **Prizes:** MLH: Best use of Vultr [unknown]  (tier: sponsor_winner)
- **Pitch:** Turns an at-home pregnancy test into a fraud-resistant, auditable record a dermatologist can approve in one tap, for isotretinoin patients.
- **Problem / user:** Isotretinoin risks birth defects and compliance checks are easy to cheat or burdensome, so a verifiable test record is needed. / dermatologists and isotretinoin patients
- **Domain / idea type:** health_wellness + safety_security / new_category
- **Platforms / hardware / AI:** web / False / vision; llm_chat; speech_or_voice
- **Stack:** langs TypeScript; Python; frontend Next.js; React; Tailwind CSS; shadcn/ui; backend Python; OpenCV; db PostgreSQL; Supabase; TimescaleDB; hosting Vercel; Vultr
- **Tech/APIs:** Vultr (cloud, core, sponsor); Grok / xAI (ai_model, core); ElevenLabs (ai_model, supporting); OpenCV (framework, core); Solana (other, supporting); Stripe (payments, supporting); Supabase (database, core); Tiger Data / TimescaleDB (database, supporting)
- **Sponsor APIs:** Vultr | fit: Ran the image-fingerprinting and non-AI test-line verification service on Vultr, targeting the MLH Best use of Vultr prize.
- **Repo:** public, commits 96 (before/in/after event: 0/96/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 28, writeup long, impact claims False
- **Notes:** Anti-fraud design with one-time links, photo fingerprinting on a Vultr image service, OpenCV cross-check of test lines, and on-chain hash anchoring (Solana) with no patient data.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/pledgecheck-qrusc1) | [GitHub](https://github.com/adrit-ganeriwala-05/PledgeCheck)

### Pose  (HackGT 13)

- **Prizes:** MLH: Best Use of Tiger Data [unknown]  (tier: sponsor_winner)
- **Pitch:** ESP32 and BNO055 wearable that detects sustained slouching against a calibrated baseline and sends it over Bluetooth to a web dashboard with a leaderboard.
- **Problem / user:** Long study and coding sessions make people forget their posture. / students and desk workers
- **Domain / idea type:** health_wellness + social_community / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / False
- **Stack:** langs Ruby; Assembly; frontend ; backend Ruby on Rails; db TigerData; hosting 
- **Tech/APIs:** TigerData (database, core, sponsor); ESP32 (hardware_part, core); BNO055 (hardware_part, core); Bluetooth LE (other, core); Ruby on Rails (framework, supporting); Claude (ai_model, token); Codex (ai_model, token)
- **Sponsor APIs:** Tiger Data | fit: Stores posture episodes in TigerData (listed under Built With) behind authenticated storage for the dashboard, targeting MLH Best Use of Tiger Data.
- **Repo:** public, commits 56 (before/in/after event: 0/56/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Classification and episode timing run on-device; the browser connects via Web Bluetooth and stores data in TigerData with a friendly social leaderboard.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; prizes.placement
- **Links:** [Devpost](https://devpost.com/software/posture-pal-ul3hfa) | [GitHub](https://github.com/Keipydesu/buzzbuzzlovers)

### ReelFriends  (HackGT 13)

- **Prizes:** Notability: Trust the Process [unknown]  (tier: sponsor_winner)
- **Pitch:** NFC-tap web app that voice-onboards users, matches them with nearby strangers on interests, and suggests an activity to do together.
- **Problem / user:** People skip events and food stalls because it feels awkward to go alone or ask someone. / students at events who want company
- **Domain / idea type:** social_community / new_category
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; speech_or_voice; recommendation
- **Stack:** langs TypeScript; frontend Next.js; backend ; db MongoDB; hosting 
- **Tech/APIs:** Meta Muse Spark (ai_model, core, sponsor); ElevenLabs (ai_model, core, sponsor); NFC tags (hardware_part, core); Arduino (hardware_part, supporting); MongoDB (database, supporting); Notability (other, supporting, sponsor)
- **Sponsor APIs:** Notability; Meta Muse Spark; ElevenLabs | fit: Contains a Notability section describing its use in the build, matching the Notability Trust the Process prize.
- **Repo:** public, commits 19 (before/in/after event: 0/18/1), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 55, writeup long, impact claims False
- **Notes:** NFC tags hold plain URLs so no install is needed; Meta Muse Spark creates profiles and recommendations and ElevenLabs voices onboarding; includes a Notability section.
- **Team size:** 5 | **Confidence:** high | unverified: ui_polish; prizes.placement
- **Links:** [Devpost](https://devpost.com/software/reelfriends) | [GitHub](https://github.com/deadly-nightshade/hackatgt26)

### Rescu  (HackGT 13)

- **Prizes:** MLH: Best Use of Solana [unknown]  (tier: sponsor_winner)
- **Pitch:** Disaster relief market on Solana where a storm-impact model triggers instant aid airdrops to affected households redeemable at local stores.
- **Problem / user:** Disaster food aid after Hurricane Helene took nearly a month to open and required in-person applications. / disaster-affected households and local merchants
- **Domain / idea type:** civic_legal + fintech_finance / social_good
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs TypeScript; Rust; Python; frontend Next.js; React; Tailwind CSS; deck.gl; MapLibre; backend Fastify; Node.js; WebSockets; db PostgreSQL; PostGIS; TimescaleDB; hosting Vultr
- **Tech/APIs:** Solana (other, core, sponsor); Token-2022 (other, core, sponsor); Anchor (framework, core); TigerData / TimescaleDB (database, supporting, sponsor); Grok (xAI) (ai_model, supporting); Vultr (cloud, supporting); NOAA/PRISM/USGS data (data_source, core)
- **Sponsor APIs:** Solana; Tiger Data | fit: Implements the relief market on Solana with Token-2022 and an Anchor program, targeting the MLH Best Use of Solana prize.
- **Repo:** public, commits 28 (before/in/after event: 0/28/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 25, writeup long, impact claims True (Reports simulated 20,000 households and about 20 million dollars in aid delivered with zero failed purchases.)
- **Notes:** Model trained on 23 US hurricanes and graded against FEMA payouts; simulation reports about 20M dollars delivered to 20,000 households in a median under one second.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; prizes.placement
- **Links:** [Devpost](https://devpost.com/software/rescu-qfuz8e) | [GitHub](https://github.com/NikhileshThiru/rescu)

### Ripple  (HackGT 13)

- **Prizes:** SpaceXAI: Make it Legendary [unknown]  (tier: sponsor_winner)
- **Pitch:** Interactive Atlanta map modeling how MARTA transit disruptions ripple to nearby people and places, with natural-language scenarios turned into forecasted impacts.
- **Problem / user:** Transit failures in Atlanta have uneven effects on residents and key services, and planners lack a view of who is affected. / transit planners and Atlanta residents
- **Domain / idea type:** mobility_transport + civic_legal / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Vite; Tailwind; deck.gl; MapLibre; backend FastAPI; Uvicorn; psycopg; db PostgreSQL; PostGIS; TimescaleDB; hosting 
- **Tech/APIs:** deck.gl (framework, core); MapLibre (maps_geo, core); PostGIS (database, core); TimescaleDB (database, supporting); FastAPI (framework, core); MARTA transit data (data_source, core)
- **Sponsor APIs:**  | fit: Won SpaceXAI 'Make it Legendary' prize; page text names no xAI tools, so how it targeted the sponsor challenge is not shown.
- **Repo:** public, commits 85 (before/in/after event: 0/85/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 19, writeup long, impact claims False
- **Notes:** Geospatial stack of PostGIS, deck.gl and MapLibre; neural network converts event descriptions to forecasted station impacts; deployed on a .tech domain.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; n_screenshots; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/ripple-vepi8b) | [GitHub](https://github.com/MannanB/HackGT13)

### SideQuests  (HackGT 13)

- **Prizes:** MLH: Best Use of MongoDB Atlas [unknown]  (tier: sponsor_winner)
- **Pitch:** Travel social network that matches travelers to places and to each other using taste onboarding, ML recommendations and a crawler for local events.
- **Problem / user:** Travelers struggle to find activities and companions that fit their tastes, pace and budget in unfamiliar places. / travelers
- **Domain / idea type:** social_community + retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios; web / False / recommendation; llm_chat; agent_or_tool_use
- **Stack:** langs Swift; Go; Python; frontend SwiftUI; backend Go; NGINX; Python ML service; Cloudflare; db MongoDB; hosting Cloudflare; Vultr; Google Cloud
- **Tech/APIs:** MongoDB (database, core, sponsor); Gemini (ai_model, supporting, sponsor); Vultr (cloud, supporting, sponsor); Cloudflare (cloud, supporting, sponsor); Muse Spark (ai_model, supporting); Hugging Face transformers (ai_model, core); Stripe (payments, token); Visa (payments, unclear); Claude (ai_model, supporting)
- **Sponsor APIs:** MongoDB; Gemini API; Vultr; Cloudflare | fit: Used MongoDB as the app's database behind a Go API, targeting the MLH Best Use of MongoDB Atlas prize (Atlas by name not confirmed in page text).
- **Repo:** public, commits 318 (before/in/after event: 0/317/1), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 19, writeup long, impact claims False
- **Notes:** Very long writeup includes a research-style abstract and ablation sections; SwiftUI app, Go API behind NGINX, Python ML service and a Muse Spark crawler; several .tech subdomains.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; n_screenshots; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/sidequestz) | [GitHub](https://github.com/karthiksing05/HackGT-13-Proj)

### SideQuests-HearsaySubmission  (HackGT 13)

- **Prizes:** NSA: Hearsay: The Audio Authentication Challenge - 1st Place [1st]  (tier: sponsor_winner)
- **Pitch:** Entry for the NSA audio authentication challenge; the Devpost page has empty section headings, so the approach is not described.
- **Problem / user:** Presumably telling real audio from fake per the challenge name; the page gives no description. / None
- **Domain / idea type:** safety_security / other
- **Platforms / hardware / AI:** other / None / predictive_ml
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Python (framework, unclear); ML/AI (unspecified) (ai_model, unclear)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Devpost writeup is blank apart from headings; only built-with tags are ai, ml, python; no links, images or video listed.
- **Team size:** 4 | **Confidence:** low | unverified: problem_statement; target_user; domain_primary; platforms; has_hardware; ai_types; idea_type; one_line_pitch
- **Links:** [Devpost](https://devpost.com/software/sidequests-hearsaysubmission)

### Sky-C2  (HackGT 13)

- **Prizes:** Best Overall - 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Phone-in-Cardboard heads-up display that labels aircraft by real bearing using live ADS-B data, with a hands-free Grok voice assistant.
- **Problem / user:** Air traffic controllers manually match aircraft seen through the window with radar and paper strips, costing attention. / air traffic controllers
- **Domain / idea type:** mobility_transport + ai_agents_infra / new_category
- **Platforms / hardware / AI:** web; mobile_cross / True / llm_chat; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend Vite; TypeScript; Canvas; backend FastAPI; Python; db ; hosting 
- **Tech/APIs:** adsb.lol (data_source, core); Grok (xAI) (ai_model, core); Grok text-to-speech (ai_model, supporting); WebRTC (framework, supporting); Google Cardboard (hardware_part, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 31 (before/in/after event: 0/29/2), README none
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims False
- **Notes:** No computer vision: GPS, compass and gyroscope plus adsb.lol feed and bearing geometry place icons; stereo canvas HUD in Google Cardboard; Grok answers by voice; WebRTC live view to laptop.
- **Team size:** 3 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/sky-c2) | [GitHub](https://github.com/jaiden-lee/ar-plane-identifier)

### Strider  (HackGT 13)

- **Prizes:** The Shipyard - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Wearable leg exoskeleton that uses IMUs to detect gait phase and drives two brushless motors to assist walking, adjustable assist level.
- **Problem / user:** Muscle loss with age makes walking and stairs hard for many elderly people, reducing independence. / elderly people with mobility difficulty
- **Domain / idea type:** health_wellness + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / False
- **Stack:** langs C++; frontend ; backend Arduino firmware; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); MPU6050 IMU (hardware_part, core); REV ION brushless motors (hardware_part, core); SPARK MAX motor controllers (hardware_part, core); 3S LiPo battery (hardware_part, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 3 (before/in/after event: 0/3/0), README none
- **Demo/writeup:** video True, live none, screenshots 4, writeup medium, impact claims True (States 25% of elderly have trouble with daily activities and up to 50% muscle loss by 80s; claims up to 40 lbs force assist.)
- **Notes:** Two REV brushless motors through 36:1 gearboxes, waterjet-cut and 3D-printed parts; assist can go negative for progressive overload; CAN control failed so PWM used.
- **Team size:** 2 | **Confidence:** high | unverified: stack_languages (C++ inferred from Arduino tag)
- **Links:** [Devpost](https://devpost.com/software/djdj-t21vgp) | [GitHub](https://github.com/aaaronqu/strider)

### Synesthesia  (HackGT 13)

- **Prizes:** The Shipyard - 1st Place [1st]  (tier: track_winner)
- **Pitch:** Wearable prototype that shows Deaf and hard-of-hearing users sound type and direction as AR-style visual cues on their phone.
- **Problem / user:** Deaf and hard-of-hearing people miss nearby sounds such as sirens, knocks and being called by name. / Deaf and hard-of-hearing people
- **Domain / idea type:** accessibility / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / speech_or_voice; predictive_ml
- **Stack:** langs JavaScript; MicroPython; frontend HTML5; CSS3; Canvas API; Web Bluetooth API; Web Audio API; backend ; db ; hosting 
- **Tech/APIs:** YAMNet (ai_model, core); MediaPipe (framework, supporting); Raspberry Pi Pico (hardware_part, core); ESP32 (hardware_part, core); Web Bluetooth API (framework, core); Web Speech API (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 14 (before/in/after event: 0/14/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 3, writeup long, impact claims False
- **Notes:** Pico compares three mic levels for rough direction, UART to ESP32, BLE to phone web app running on-device YAMNet; timing fusion refuses to show direction when ambiguous; audio never leaves the phone.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/synesthesia-b1p9r3) | [GitHub](https://github.com/RishabhK12/Synesthesia)

### TapChart  (HackGT 13)

- **Prizes:** Aramco: A Marina's Mission - 1st Place [1st]  (tier: track_winner)
- **Pitch:** Camera-based finger-tapping test builds a personal motor baseline for Parkinson's patients, reachable by NFC tag for EMTs and doctors in a possible stroke.
- **Problem / user:** Clinicians seeing a Parkinson's patient in an emergency lack a record of normal motor function, making stroke assessment harder. / Parkinson's patients, EMTs and clinicians
- **Domain / idea type:** health_wellness + accessibility / new_category
- **Platforms / hardware / AI:** web / True / vision; predictive_ml
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend Python; db PostgreSQL; Supabase; hosting Vercel
- **Tech/APIs:** MediaPipe (ai_model, core); OpenCV (framework, supporting); NFC (hardware_part, core); Supabase (database, supporting); scikit-learn (framework, supporting); Claude (ai_model, unclear)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 13, writeup long, impact claims False
- **Notes:** Stores derived tapping measurements instead of video; NFC tag gives licensed providers access; page states it gives context only and does not diagnose stroke.
- **Team size:** 2 | **Confidence:** high | unverified: sponsor_apis_used; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/tapchart) | [GitHub](https://github.com/alana170/TapChart)

### TedTime  (HackGT 13)

- **Prizes:** Meta: Bringing People Closer Together with AI - Winner [unknown]  (tier: sponsor_winner)
- **Pitch:** Smart teddy bear with an ESP32 and companion app that preserves relatives' voices and stories so families stay connected across distance.
- **Problem / user:** Families with relatives abroad want a more personal way to keep voices and stories than phone calls or recordings. / families with distant grandparents
- **Domain / idea type:** social_community / hardware_gadget
- **Platforms / hardware / AI:** mobile_cross; hardware / True / llm_chat; speech_or_voice
- **Stack:** langs Python; frontend React Native; Expo; backend FastAPI; db Supabase; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Meta Muse Spark (ai_model, supporting, sponsor); Grok (ai_model, supporting); FastAPI (framework, supporting); Supabase (database, supporting); React Native / Expo (framework, supporting)
- **Sponsor APIs:** Meta Muse Spark | fit: Targets Meta's Bringing People Closer Together with AI theme with a voice-preserving bear for distant family; Muse Spark appears in Built With.
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 31, writeup medium, impact claims False
- **Notes:** Plush hardware with a 3D-printed endoskeleton (Onshape CAD linked), read-along feature and community stories explore page; GitHub link points to an organization, not a repo.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; prizes.placement; writeup_sections; ai_types; how Muse Spark is used
- **Links:** [Devpost](https://devpost.com/software/teddy-42km8n)

### VIGIL: Assistive Eyewear with an Autonomous Aerial Scout  (HackGT 13)

- **Prizes:** Best Overall - 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Sensor-equipped glasses plus voice control send a DJI Tello drone to find an item or person, then guide a blind user there with speech and haptics.
- **Problem / user:** Blind people who lose objects must search hazardous rooms by touch or wait for help. / blind and visually impaired people
- **Domain / idea type:** accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware; desktop / True / vision; speech_or_voice; agent_or_tool_use; predictive_ml
- **Stack:** langs Python; frontend ; backend Python; djitellopy; OpenCV; FFmpeg; db ; hosting Modal
- **Tech/APIs:** DJI Tello (hardware_part, core); ESP32-CAM (hardware_part, core); VL53L0X ToF sensors (hardware_part, supporting); YOLO11 / YOLO-World (ai_model, core); Whisper (ai_model, core); Fruit-fly connectome (MaleCNS) (data_source, core); CMA-ES on Modal (cloud, supporting); AirPods Pro (hardware_part, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 37 (before/in/after event: 0/33/4), README detailed
- **Demo/writeup:** video True, live none, screenshots 9, writeup medium, impact claims True (Reports steering error of 6.6 degrees vs 11.0 with random wiring across 500+ automated tests.)
- **Notes:** Drone steering uses a fruit-fly connectome circuit (1,446 neurons) with a 34-parameter adapter tuned via CMA-ES on Modal; reports 6.6 vs 11.0 degree steering error; ESP32-CAM glasses with ToF sensors and servo pads.
- **Team size:** 4 | **Confidence:** high | unverified: stack_languages (only Python listed)
- **Links:** [Devpost](https://devpost.com/software/vigil-assistive-eeywear-with-an-autonomous-aerial-scout) | [GitHub](https://github.com/parthm667/vigil)
