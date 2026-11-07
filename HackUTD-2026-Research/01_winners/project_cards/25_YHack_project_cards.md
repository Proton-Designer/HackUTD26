# YHack: project cards (11 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## YHack 2024

### AlphaBuddy AR  (YHack 2024)

- **Prizes:** 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Mobile AR app that recognizes a scanned book page and overlays a 3D model and AI-generated explanation video.
- **Problem / user:** Static book pages make learning less engaging for children. / children and students using printed books
- **Domain / idea type:** education / new_category
- **Platforms / hardware / AI:** mobile_ios; mobile_android / False / vision; generative_media
- **Stack:** langs C#; Python; frontend Unity; Vuforia; backend Python; db ; hosting 
- **Tech/APIs:** Unity (framework, core); Vuforia (framework, core)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Image recognition via Vuforia identifies the page, then Unity overlays generated video and AR objects; built for iOS and Android.
- **Team size:** 2 | **Confidence:** medium | unverified: n_screenshots; ai_types; is_sponsor flags; ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/alphabuddy-ar-rdfkp9)

### Fivi  (YHack 2024)

- **Prizes:** 1st place, Healthcare Track; plus ActualFood, LLC sponsor award [1st]  (tier: track_winner)
- **Pitch:** AI fitness coach that watches exercises through a camera, gives real-time form feedback and acts as a motivating companion.
- **Problem / user:** Working out effectively and safely is hard without personal coaching. / people exercising on their own
- **Domain / idea type:** health_wellness / automation_or_agent
- **Platforms / hardware / AI:**  / None / vision; speech_or_voice
- **Stack:** langs ; frontend ; backend ; db ; hosting 
- **Tech/APIs:** OpenAI voice API (ai_model, unclear)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots None, writeup None, impact claims None
- **Notes:** Only a university news write-up was read (no Devpost or repo listed in queue); uses computer vision and OpenAI voice API per that article; prize also included a sponsor award.
- **Team size:** 3 | **Confidence:** low | unverified: no_devpost_page; platforms; stack; screenshots; event_start; event_end; sponsor details; domain_secondary
- **Links:** [Devpost](None)

### Tidbits  (YHack 2024)

- **Prizes:** 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Turns uploaded lectures into short scrollable AI-generated videos, stitching narration, imagery and music into TikTok-style study clips.
- **Problem / user:** Students lose most lecture material and struggle to stay engaged with long lectures. / college students
- **Domain / idea type:** education + creative_media / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; generative_media
- **Stack:** langs Python; TypeScript; frontend Next.js; Sass; Figma; backend FastAPI; db Supabase; hosting 
- **Tech/APIs:** Anthropic Claude (ai_model, core); OpenAI Whisper (ai_model, core); DALL-E (ai_model, core); ElevenLabs (ai_model, core); D-ID (ai_model, supporting); Suno AI (ai_model, supporting); Supabase (database, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 144 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 9, writeup long, impact claims True (Cites a figure that about 80% of lecture material is lost, with linked research sources.)
- **Notes:** Pipeline chains many AI services (Whisper, Claude, DALL-E, ElevenLabs, D-ID, Suno) into one edited short; page includes full design process and cited sources.
- **Team size:** 4 | **Confidence:** medium | unverified: is_sponsor flags; ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/tidbits-n9mrxa) | [GitHub](https://github.com/dylanvu/Tidbits)

### YGroove  (YHack 2024)

- **Prizes:** 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Web tool that scores how closely a user's dance or exercise movements match a reference video using pose estimation and dynamic time warping.
- **Problem / user:** People practicing dance or exercise lack objective feedback on how accurate their movements are. / dancers and exercisers practicing from videos
- **Domain / idea type:** health_wellness + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs JavaScript; frontend React; Next.js; backend Node.js; db ; hosting 
- **Tech/APIs:** TensorFlow MoveNet (ai_model, core); Dynamic time warping (other, core); Next.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots None, writeup long, impact claims False
- **Notes:** MoveNet pose keypoints compared to a reference with dynamic time warping; supports uploaded video or live webcam.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots; is_sponsor flags; ui_polish; event_start; event_end; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/ygroove) | [GitHub](https://github.com/alexy201/YGroove)


## YHack Fall 2024

### bellcrve  (YHack Fall 2024)

- **Prizes:** 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Distributed computing cluster that runs Monte Carlo simulations for option pricing across worker VMs, using Wolfram for the math.
- **Problem / user:** Option pricing by Monte Carlo is slow on a single machine; distribution should speed convergence. / quantitative finance practitioners
- **Domain / idea type:** fintech_finance + dev_tools / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; frontend React; backend Flask; Dask; db ; hosting DigitalOcean
- **Tech/APIs:** Wolfram (other, core); Dask (framework, core); DigitalOcean (cloud, core); Flask (framework, supporting); PyPI (other, token)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup medium, impact claims False
- **Notes:** Ten DigitalOcean VMs (eight workers, one master, one scheduler) running Dask with geometric Brownian motion simulations; published as a PyPI package per tags.
- **Team size:** 3 | **Confidence:** medium | unverified: is_sponsor flags; ui_polish; event_start; event_end; github_url is org page not repo
- **Links:** [Devpost](https://devpost.com/software/lambda-labs)

### Percival  (YHack Fall 2024)

- **Prizes:** 1st Place [1st]; Best AI Project with Databricks Open Source [unknown]  (tier: overall_top3)
- **Pitch:** Clinical data-entry assistant that takes text, speech or PDFs, anonymizes patient info, fills medical forms and compares cases against a vector database.
- **Problem / user:** Clinicians spend heavy time on manual medical form entry and lack quick comparison with similar past cases. / clinicians and medical office staff
- **Domain / idea type:** health_wellness + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; rag_or_search; recommendation
- **Stack:** langs Python; JavaScript; frontend Next.js; backend Flask; db Cloudflare D1; vector database; hosting Cloudflare
- **Tech/APIs:** OpenAI API (ai_model, core); OpenAI Whisper (ai_model, core); Databricks Open Source (data_source, supporting, sponsor); Cloudflare D1 (database, supporting); Flask (framework, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** Databricks Open Source | fit: Used Databricks open-source tooling for a K-means clustering model over its vector database of similar patient cases.
- **Repo:** public, commits 77 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video False, live none, screenshots 12, writeup long, impact claims False
- **Notes:** K-means clustering on a vector database using Databricks open source to surface similar patient cases; Whisper transcription; Cloudflare D1 for storage and auth.
- **Team size:** 4 | **Confidence:** medium | unverified: github_url_not_listed_on_page_kept_from_queue; is_sponsor flags; ui_polish; event_start; event_end; placement_tier
- **Links:** [Devpost](https://devpost.com/software/percival-nr46ol) | [GitHub](https://github.com/roshanbellary/Percival)

### The Tales of Detective Toasty  (YHack Fall 2024)

- **Prizes:** 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Visual-novel murder mystery on a boat where a GPT-powered assistant answers the player's questions about four suspects and rooms.
- **Problem / user:** Visual novels offer fixed dialogue; the team wanted adaptive AI conversation to deepen mystery gameplay. / casual game players
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / False / llm_chat
- **Stack:** langs Python; Ren'Py; frontend Ren'Py; backend ; db ; hosting itch.io
- **Tech/APIs:** OpenAI ChatGPT API (ai_model, core); Ren'Py (framework, core); Procreate (other, supporting); Canva (other, token)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 9, writeup medium, impact claims False
- **Notes:** Built in Ren'Py with hand-drawn art (Procreate); ChatGPT API powers an in-game assistant adapting to player questions; game distributed on itch.io (private link with secret token omitted).
- **Team size:** 3 | **Confidence:** medium | unverified: platforms; is_sponsor flags; ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/placeholder-5hgbfe)


## YHack Spring 2026

### Circa  (YHack Spring 2026)

- **Prizes:** First Place Overall [1st]; Societal Impact [unknown]  (tier: overall_top3)
- **Pitch:** Automated irrigation system using ESP32 sensor nodes and a motorized turret that waters targeted spots, controlled from a web dashboard.
- **Problem / user:** Conventional irrigation wastes a large share of water and is hard to control precisely. / farmers and growers
- **Domain / idea type:** sustainability_climate + energy_utilities / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / None
- **Stack:** langs C++; Python; JavaScript; frontend React; backend Node.js; Express; FastAPI; MQTT; Socket.IO; db ; hosting GitHub Pages
- **Tech/APIs:** ESP32 (hardware_part, core); MQTT (other, core); Socket.IO (framework, supporting); FastAPI (framework, supporting); Arduino/PlatformIO (hardware_part, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 11, writeup long, impact claims True (States that roughly 40-50% of irrigation water is wasted.)
- **Notes:** Three ESP32 firmware roles (base, turret, sensor nodes) talking over MQTT to a Node/Express server streaming via Socket.IO; dashboard offers pre-irrigation prediction and custom turret control.
- **Team size:** 4 | **Confidence:** medium | unverified: ai_used; is_sponsor flags; ui_polish; event_start; event_end; live_demo_url is project site
- **Links:** [Devpost](https://devpost.com/software/circa-u1fsx5)

### GaitGuard  (YHack Spring 2026)

- **Prizes:** Third Place Overall [3rd]; Built With Zed [unknown]  (tier: overall_top3)
- **Pitch:** Wearable rehab system with three sensor units that compares a patient's movement to a personalized digital twin and gives real-time haptic feedback.
- **Problem / user:** Rehab patients lack real-time, personalized feedback on whether they are performing movements correctly outside the clinic. / physical therapy patients and therapists
- **Domain / idea type:** health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_cross; desktop / True / predictive_ml
- **Stack:** langs Python; frontend ; backend Raspberry Pi; QNX; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); MPU-6050 IMU (hardware_part, core); Haptic motor (hardware_part, core); Raspberry Pi (hardware_part, supporting); QNX (other, unclear, sponsor); Zed editor (other, unclear, sponsor); Claude (ai_model, unclear)
- **Sponsor APIs:** Zed | fit: Second prize is Built With Zed; page lists Zed in Built With, depth of use not described in what was read.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Custom 3D-printed shin unit with ESP32, IMU, LiPo and haptic motor; therapist demonstration builds a per-patient digital twin; mobile and desktop companion apps; Zed and QNX listed.
- **Team size:** 4 | **Confidence:** medium | unverified: ai_used; ai_types; tech_items depth for QNX/Zed/Claude; is_sponsor flags; ui_polish; event_start; event_end; placement_tier; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/gaitguard) | [GitHub](https://github.com/TMulosmani/GaitGuard)

### HandFlow - Smart Glasses For Productivity  (YHack Spring 2026)

- **Prizes:** Best First Hack [unknown]  (tier: track_winner)
- **Pitch:** Glasses-mounted cheap camera that turns hand gestures and a printed macropad into computer input, using a custom gesture classifier.
- **Problem / user:** Smart-glasses-style gesture control is expensive; the team aimed to make it accessible with a very low-cost camera. / productivity users and makers wanting hands-free input
- **Domain / idea type:** productivity_workplace + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware; desktop / True / vision; predictive_ml; llm_chat
- **Stack:** langs Python; frontend ; backend MediaPipe; OpenCV; TensorFlow Lite; scikit-learn; NumPy; Docker; db ; hosting Akash
- **Tech/APIs:** MediaPipe (framework, core); TCN gesture model (TensorFlow/TFLite) (ai_model, core); OpenCV ArUco (framework, core); Gemini (ai_model, supporting); Akash (cloud, unclear, sponsor); Docker (other, token)
- **Sponsor APIs:** Akash
- **Repo:** public, commits 2 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims True (Highlights an extremely affordable $5 camera as the hardware cost.)
- **Notes:** MediaPipe landmarks expanded to 96 features feeding a TCN with 16 gesture classes (~5ms inference); ArUco markers detect a macropad; cites a $5 camera.
- **Team size:** 4 | **Confidence:** medium | unverified: is_sponsor flags; Akash role; ui_polish; event_start; event_end; placement_tier
- **Links:** [Devpost](https://devpost.com/software/handflow) | [GitHub](https://github.com/AndyHuynh24/HandFlow_YHack)

### LifeSaver  (YHack Spring 2026)

- **Prizes:** Second Place Overall [2nd]; Most Creative Hack [unknown]  (tier: overall_top3)
- **Pitch:** Browser-based 3D operating room where hand tracking via webcam controls surgical instruments and an AI coach explains organs and answers voice questions.
- **Problem / user:** Surgical training relies on watching, and simulators cost over $100,000 per machine. / medical students and surgical trainees
- **Domain / idea type:** education + health_wellness / new_category
- **Platforms / hardware / AI:** web / False / llm_chat; vision; speech_or_voice
- **Stack:** langs TypeScript; frontend React Three Fiber; Three.js; Vite; Framer; WebGL; MediaPipe; backend Node.js; Express.js; db MongoDB; hosting 
- **Tech/APIs:** MediaPipe (framework, core); Google Gemini (ai_model, core); ElevenLabs (ai_model, supporting); React Three Fiber (framework, core); MongoDB (database, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 27 (before/in/after event: None/None/None), README none
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims True (Contrasts with surgical simulators costing over $100,000 per machine.)
- **Notes:** No hardware beyond webcam: MediaPipe hand tracking drives instruments in a React Three Fiber operating room; Gemini coaching with ElevenLabs spoken replies.
- **Team size:** 4 | **Confidence:** medium | unverified: is_sponsor flags; ui_polish; event_start; event_end; placement_tier
- **Links:** [Devpost](https://devpost.com/software/lifesaver-lnm0tz) | [GitHub](https://github.com/akhilm2223/yale)
