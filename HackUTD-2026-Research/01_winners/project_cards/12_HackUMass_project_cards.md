# HackUMass: project cards (51 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackUMass XII

### 2D fun game!!!  (HackUMass XII)

- **Prizes:** Best UI/UX [unknown]  (tier: track_winner)
- **Pitch:** Simple 2D pixel-art platformer, SuburbanRunner, with double jumps and speed bursts meant to relieve stress after work or school.
- **Problem / user:** People want a relaxing way to unwind, and the team wanted to show 2D games can feel rich rather than flat. / casual players
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / False / False
- **Stack:** langs ; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Godot (framework, core)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Built in Godot with sprites and scenes sourced from the internet; the only link is a Google Drive folder, no repo or video.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; platforms; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/2d-fun-game)

### Ai-Companion  (HackUMass XII)

- **Prizes:** Wolfram Award [unknown]  (tier: sponsor_winner)
- **Pitch:** Unity desktop pet companion using Whisper, GPT and ElevenLabs voice, with a JSON memory profile and desktop assistant actions.
- **Problem / user:** People feel isolated and overloaded by screens and want a personalised companion that adapts over time. / desktop users wanting a companion
- **Domain / idea type:** ai_agents_infra + mental_health / new_category
- **Platforms / hardware / AI:** desktop / False / llm_chat; speech_or_voice; agent_or_tool_use
- **Stack:** langs C#; Python; frontend Unity; backend ; db ; hosting 
- **Tech/APIs:** OpenAI GPT-4o-mini (ai_model, core); Whisper (ai_model, core); ElevenLabs (ai_model, core); Unity (framework, core); OpenWeatherMap (data_source, supporting); NewsAPI (data_source, supporting); Figma (other, token)
- **Sponsor APIs:** 
- **Repo:** public, commits 97 (before/in/after event: 94/0/3), README detailed
- **Demo/writeup:** video False, live none, screenshots 10, writeup long, impact claims False
- **Notes:** Two-layer GPT calls maintain a locally stored profile/memory JSON; keyword-triggered news and weather injection; Windows DLL actions like calendar; GitHub link is a third-party Unity package, not the project repo.
- **Team size:** 2 | **Confidence:** medium | unverified: github_url_is_dependency_not_project_repo
- **Links:** [Devpost](https://devpost.com/software/ai-companion-d3681a) | [GitHub](https://github.com/srcnalt/OpenAI-Unity)

### Braille Assist  (HackUMass XII)

- **Prizes:** Wolfram Award [unknown]  (tier: sponsor_winner)
- **Pitch:** Arduino-driven motor device that converts typed English text into physical braille output.
- **Problem / user:** Translating text into braille is more useful when delivered on a physical device rather than a screen. / braille readers
- **Domain / idea type:** accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / False
- **Stack:** langs Python; C++; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Arduino (hardware_part, core); Motors (hardware_part, core); 3D printing (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 1 (before/in/after event: 0/1/0), README none
- **Demo/writeup:** video False, live none, screenshots 14, writeup short, impact claims False
- **Notes:** Team had no prior hardware experience; used motors and a 3D-printed box; Python and C++ code; photos of wiring and backend code.
- **Team size:** 5 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/braille-assist-1683ru) | [GitHub](https://github.com/ImaMinh/HackUMass-2024)

### Dice Aid  (HackUMass XII)

- **Prizes:** Best Mechanical Hack [unknown]  (tier: track_winner)
- **Pitch:** Raspberry Pi dice roller with a 3D-printed shell and stepper motors that launches dice at the press of a button, sweeps them up, recognizes the faces by camera and shows the total.
- **Problem / user:** Traditional dice rolling is hard for people with limited dexterity; the team wanted accessible, unbiased rolling for any game. / tabletop gamers with limited dexterity
- **Domain / idea type:** accessibility + entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Raspberry Pi 4B (hardware_part, core); Stepper motors (hardware_part, core); Camera dice recognition (ai_model, core); 3D-printed shell (hardware_part, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** Mechanical build split across ME (CAD shell), EE (Pi 4B to stepper motors) and CompE (UI and dice recognition) roles; getting a camera working on the Pi was the main challenge.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/dice-aid)

### FoundU  (HackUMass XII)

- **Prizes:** Wolfram Award [unknown]  (tier: sponsor_winner)
- **Pitch:** Mobile app that reads a found UMass UCard via OCR, looks up the owner's email and automatically emails them.
- **Problem / user:** Lost UCards rarely reach owners because finders cannot easily identify or contact them. / UMass students
- **Domain / idea type:** social_community + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** mobile_cross / False / vision
- **Stack:** langs TypeScript; JavaScript; frontend React Native; Expo; backend Node.js; Express; db ; hosting 
- **Tech/APIs:** Google Cloud Vision API (ai_model, core); Puppeteer (framework, core); Nodemailer (other, core); Expo (framework, supporting); Multer (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Chains OCR name extraction, Puppeteer scraping of the campus people directory behind a session cookie, and automated email; writeup states a $1,700 Wolfram award; only link is a LinkedIn post.
- **Team size:** 2 | **Confidence:** high | unverified: github_url_absent_on_page
- **Links:** [Devpost](https://devpost.com/software/foundu)

### Infraflow  (HackUMass XII)

- **Prizes:** [MLH] Best Use of Terraform [unknown]; [HACKUMASS] Best Security Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** Drag-and-drop cloud diagram editor that instantly generates Terraform code for AWS, Azure or GCP resources.
- **Problem / user:** Cloud infrastructure and infrastructure-as-code are intimidating for beginners and students without hands-on DevOps access. / students and DevOps beginners
- **Domain / idea type:** dev_tools + education / dev_tool
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; frontend Next.js; backend Bun; Express; db ; hosting Vercel
- **Tech/APIs:** Terraform (other, core, sponsor); AWS (cloud, supporting); Azure (cloud, supporting); GCP (cloud, supporting); Express (framework, core); Next.js (framework, core); Bun (framework, supporting)
- **Sponsor APIs:** Terraform | fit: Core product converts visual diagrams into Terraform configuration files for several cloud providers, matching the MLH Terraform challenge.
- **Repo:** public, commits 19 (before/in/after event: 0/19/0), README none
- **Demo/writeup:** video False, live not_checked, screenshots 5, writeup medium, impact claims False
- **Notes:** Writeup left a template placeholder in the frontend bullet; supports multiple cloud providers; backend uses Bun with Express.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/infraflow) | [GitHub](https://github.com/weebao/infraflow)

### Is my house on fire?  (HackUMass XII)

- **Prizes:** Best Smart Home Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** Raspberry Pi camera watches an oven and uses cloud computer vision to detect if it is on, showing status on a website.
- **Problem / user:** Renters in old apartments worry about leaving the stove or oven on and want remote reassurance. / apartment dwellers worried about leaving appliances on
- **Domain / idea type:** safety_security + sustainability_climate / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision
- **Stack:** langs Python; JavaScript; frontend React; CSS; backend Python; db MongoDB Atlas; hosting Google Cloud; Terraform
- **Tech/APIs:** OpenCV (framework, core); Raspberry Pi + webcam (hardware_part, core); MongoDB Atlas (time series) (database, supporting, sponsor); Google Cloud (cloud, supporting); Terraform (other, supporting); .tech domain (other, supporting, sponsor); React (framework, supporting)
- **Sponsor APIs:** MongoDB Atlas; .Tech Domains | fit: Won Best Smart Home Hack with a Raspberry Pi camera oven monitor, which fits the smart-home theme directly.
- **Repo:** public, commits 27 (before/in/after event: 0/27/0), README none
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup medium, impact claims False
- **Notes:** Detects oven indicator lights and displayed temperatures with OpenCV; history stored in MongoDB Atlas time series; infrastructure on GCP via Terraform; a DNS change cost two hours.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/is-my-house-on-fire) | [GitHub](https://github.com/listsarah/HackUMass24)

### Loop  (HackUMass XII)

- **Prizes:** Best Android/IOS [unknown]  (tier: track_winner)
- **Pitch:** Mobile app where you create Interests that get daily AI-summarized newsletters and push alerts about new releases or breaking news.
- **Problem / user:** People who quit social media lose track of current events and new releases without paying for many subscriptions. / people avoiding social media
- **Domain / idea type:** productivity_workplace + social_community / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / llm_chat
- **Stack:** langs JavaScript; frontend React Native; backend ; db ; hosting 
- **Tech/APIs:** React Native (framework, core); Unnamed AI API (summarize/scrape) (ai_model, supporting)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Solo project; first completed app for the builder; AI API used only for summarizing and scraping web data; no account required.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; n_screenshots; ai_types; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/loop-5p83qv) | [GitHub](https://github.com/jamespineiro/loop)

### Loopwise  (HackUMass XII)

- **Prizes:** Best Use of ML/AI [unknown]  (tier: track_winner)
- **Pitch:** Recommends driving loops to rideshare drivers using DBSCAN clustering and LSTM demand forecasts over historical ride data.
- **Problem / user:** Rideshare drivers waste time and fuel idling or searching for passengers. / rideshare drivers
- **Domain / idea type:** mobility_transport + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; recommendation
- **Stack:** langs Python; JavaScript; frontend React; Next.js; backend Flask; FastAPI; db ; hosting 
- **Tech/APIs:** LSTM (PyTorch/TensorFlow) (ai_model, core); DBSCAN (scikit-learn) (ai_model, core); Folium/Leaflet (maps_geo, supporting); Pandas/NumPy (framework, supporting)
- **Sponsor APIs:**  | fit: Trained demand-forecasting and clustering models are the core of the product.
- **Repo:** public, commits 12 (before/in/after event: 0/12/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 26, writeup long, impact claims False
- **Notes:** Many charts and maps of ride data in gallery (26 images); writeup claims real-time GPS but describes historical datasets; open-source routing builds the loop.
- **Team size:** 2 | **Confidence:** high | unverified: real_time_claim
- **Links:** [Devpost](https://devpost.com/software/loopwise) | [GitHub](https://github.com/devger04/Loopwise)

### magic algorithms  (HackUMass XII)

- **Prizes:** Wolfram Award [unknown]  (tier: sponsor_winner)
- **Pitch:** Interactive web visualizer for Dijkstra, minimum spanning tree and network flow algorithms on user-built graphs.
- **Problem / user:** Graph algorithms taught in CS courses are hard to grasp without seeing them step by step. / CS students
- **Domain / idea type:** education / creative_tool
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; JavaScript; frontend Vue; HTML Canvas; backend ; db ; hosting Netlify
- **Tech/APIs:** Vue (framework, core); HTML Canvas (framework, core)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup short, impact claims False
- **Notes:** Course-tied (UMass CS311) teaching tool on Netlify; short writeup; no repo link listed.
- **Team size:** 3 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/magic-w453qf)

### Maple.ai  (HackUMass XII)

- **Prizes:** [MLH] Best AI Project with Databricks Open Source [unknown]  (tier: sponsor_winner)
- **Pitch:** AI chemistry tutor that detects student emotion from voice with Hume EVI and answers from a Databricks-based RAG knowledge base.
- **Problem / user:** Tutoring tools hand out answers but ignore how students feel while learning, and LLMs can hallucinate on technical content. / chemistry students
- **Domain / idea type:** education + mental_health / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; speech_or_voice
- **Stack:** langs Python; TypeScript; JavaScript; frontend Next.js; React; Tailwind; backend Flask; LangChain; db LanceDB; hosting 
- **Tech/APIs:** Databricks (DBRX, chat UI library) (ai_model, core, sponsor); LanceDB (database, supporting); LlamaIndex (framework, supporting); Hume EVI (ai_model, core); Midnight blockchain (other, supporting); OpenAI (ai_model, unclear); LangChain (framework, supporting); Flask (framework, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** Databricks DBRX | fit: Built an open-source RAG knowledge base with DBRX, LanceDB and LlamaIndex over Wolfram MathWorld and used Databricks' chat UI library for the tutoring chat.
- **Repo:** public, commits 23 (before/in/after event: 0/21/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 6, writeup medium, impact claims False
- **Notes:** Combines Hume voice emotion detection with a mood gauge, RAG over Wolfram MathWorld using DBRX and LanceDB, and a Midnight blockchain DApp for private records.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/maple-ai) | [GitHub](https://github.com/lonexreb/Maple)

### NekoPix  (HackUMass XII)

- **Prizes:** Wolfram Award [unknown]  (tier: sponsor_winner)
- **Pitch:** Web tool where users sketch a level layout and give a theme; DALL-E 3 generates textures for a playable game.
- **Problem / user:** Game development is hard to start because it needs many tools and CS knowledge. / beginners in game development
- **Domain / idea type:** creative_media + education / creative_tool
- **Platforms / hardware / AI:** web / False / generative_media
- **Stack:** langs JavaScript; frontend Next.js; React; backend ; db ; hosting 
- **Tech/APIs:** DALL-E 3 (ai_model, core); Next.js (framework, core); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 46 (before/in/after event: 0/46/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup medium, impact claims False
- **Notes:** Drawing pad feeds a prebuilt game engine; texture generation runs async on a separately hosted backend so play continues while images load.
- **Team size:** 5 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/gameify) | [GitHub](https://github.com/waiwasabi/game2024)

### onedef  (HackUMass XII)

- **Prizes:** [MLH] Best .Tech Domain Name [unknown]  (tier: sponsor_winner)
- **Pitch:** Library that lets Python and JavaScript call each other's functions as if imported, using sockets and generated glue code.
- **Problem / user:** Using functions across language boundaries normally needs heavy bindings; the team wanted import-like simplicity. / developers mixing Python and JavaScript
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** cli; other / False / False
- **Stack:** langs Python; JavaScript; C; frontend ; backend Node.js; Python; db ; hosting AWS; Terraform
- **Tech/APIs:** .tech domain (other, token, sponsor); Sockets (UNIX domain) (other, core); Node.js (framework, core); Terraform (other, supporting); AWS (cloud, supporting)
- **Sponsor APIs:** .Tech Domains | fit: Won Best .Tech Domain Name and listed onedef.tech as its site; the project itself is a language-interop library.
- **Repo:** public, commits 125 (before/in/after event: 0/124/1), README thin
- **Demo/writeup:** video False, live not_checked, screenshots 0, writeup long, impact claims False
- **Notes:** Built from scratch on raw sockets in plain Node and Python, after abandoning a Rust-based plan; either language can act as client or server; testing was hard until everything existed.
- **Team size:** 5 | **Confidence:** high | unverified: ui_polish; demo_video_url
- **Links:** [Devpost](https://devpost.com/software/unicall) | [GitHub](https://github.com/PianoPanda/HackUMASSXII)

### Piano Rotation Analyzer  (HackUMass XII)

- **Prizes:** Best Novel Hack [unknown]  (tier: track_winner)
- **Pitch:** Python script that reads fingered Music XML sheet music and reports biomechanical hand-rotation information for piano passages.
- **Problem / user:** Pianists need to know how their hand and forearm must rotate between keys, not just which keys to play. / pianists and piano teachers
- **Domain / idea type:** creative_media + education / creative_tool
- **Platforms / hardware / AI:** cli / False / False
- **Stack:** langs Python; frontend ; backend music21; db ; hosting 
- **Tech/APIs:** music21 (framework, core); Music XML (data_source, core)
- **Sponsor APIs:**  | fit: Won the event-run Best Novel Hack category; no sponsor technology used.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Uses music21 to parse Music XML with fingering annotations; a web upload interface was only a stretch goal; single-person project with no screenshots or video.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/piano-technique-analyzer)

### qSound  (HackUMass XII)

- **Prizes:** Nord Security Add-On [unknown]  (tier: sponsor_winner)
- **Pitch:** Live music audio drives a 12-qubit quantum simulation rendered as waves and particles, with a small neural net scoring intensity.
- **Problem / user:** Experimental project with no practical problem; merges quantum mechanics and neural networks to visualize sound. / music and quantum-computing enthusiasts
- **Domain / idea type:** creative_media + entertainment_games / creative_tool
- **Platforms / hardware / AI:** desktop / False / predictive_ml
- **Stack:** langs Python; frontend OpenGL; backend ; db ; hosting 
- **Tech/APIs:** Qiskit (framework, core); PyTorch (framework, core); OpenGL (framework, core)
- **Sponsor APIs:**  | fit: Entered for the Nord Security add-on prize; the writeup does not tie the project to security.
- **Repo:** public, commits 81 (before/in/after event: 0/81/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 3, writeup medium, impact claims False
- **Notes:** Maps amplitude, frequency and phase to qubit rotations; custom 60-song dataset for intensity model; custom FFT feature extraction; OpenGL particles.
- **Team size:** 4 | **Confidence:** high | unverified: sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/q-sound) | [GitHub](https://github.com/odepoint/qSound)

### RealityPaint  (HackUMass XII)

- **Prizes:** Third Prize [3rd]  (tier: overall_top3)
- **Pitch:** Projector plus Kinect depth camera that maps generated art onto physical surfaces and masks out objects in front of them.
- **Problem / user:** Blending digital art with real spaces needs reliable object masking under projection, which webcams struggled to provide. / artists, presenters, people decorating spaces
- **Domain / idea type:** creative_media / creative_tool
- **Platforms / hardware / AI:** desktop; hardware / True / generative_media; vision
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Microsoft Kinect (hardware_part, core); OpenCV (framework, core); DALL-E 3 (ai_model, supporting); Projector (hardware_part, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 97 (before/in/after event: 0/96/1), README solid
- **Demo/writeup:** video False, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Switched from webcam to Kinect overnight after a projection feedback loop; patched unfinished Python Kinect wrappers; team says it did not fully work.
- **Team size:** 3 | **Confidence:** high | unverified: ai_types
- **Links:** [Devpost](https://devpost.com/software/realitypaint) | [GitHub](https://github.com/beaverbois/RealityPaint)

### SafeSteps  (HackUMass XII)

- **Prizes:** Best UMass-Related Hack [unknown]  (tier: track_winner)
- **Pitch:** Flutter campus-safety app mapping UMass HELP phones with directions, live location sharing, a one-tap emergency call and safer route suggestions.
- **Problem / user:** Students walking alone at night cannot quickly find HELP phones or share their location with trusted people. / UMass Amherst students
- **Domain / idea type:** safety_security + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / False
- **Stack:** langs Dart; frontend Flutter; backend Firebase; db Firebase; hosting Firebase
- **Tech/APIs:** Flutter (framework, core); Google Maps API (maps_geo, core); Google Directions / Places (maps_geo, supporting); Firebase (cloud, core)
- **Sponsor APIs:**  | fit: Targeted the UMass-related hack category with a map of campus HELP phones and escort features tied to UMass Security.
- **Repo:** public, commits 58 (before/in/after event: 0/56/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Maps all UMass HELP phone locations and routes through well-lit paths near them; inspired by a real late-night incident involving a friend.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/safesteps-62k5zb) | [GitHub](https://github.com/adhirajj/safesteps)

### SpeedPUB  (HackUMass XII)

- **Prizes:** Grand Prize [1st]  (tier: overall_top3)
- **Pitch:** Python tool that converts EPUBs into syntax-highlighted versions, colouring words by part of speech (English and Chinese) and optionally bolding for speed reading, with a Tkinter GUI.
- **Problem / user:** Reading is time-consuming for avid readers and language learners; highlighting word function could speed reading and aid comprehension. / avid readers and language learners
- **Domain / idea type:** education + productivity_workplace / creative_tool
- **Platforms / hardware / AI:** desktop / False / other
- **Stack:** langs Python; frontend Tkinter; backend ; db ; hosting 
- **Tech/APIs:** NLTK (framework, core); HanLP (ai_model, core); EbookLib (framework, core); BeautifulSoup (framework, supporting); Tkinter (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 37 (before/in/after event: 0/37/0), README solid
- **Demo/writeup:** video None, live none, screenshots 6, writeup medium, impact claims False
- **Notes:** Pipeline uses EbookLib and BeautifulSoup to rewrite EPUB XHTML, NLTK for English and HanLP for Chinese part-of-speech tagging; team plans to keep using it themselves.
- **Team size:** 2 | **Confidence:** medium | unverified: has_demo_video; placement_tier
- **Links:** [Devpost](https://devpost.com/software/untitled-project-03byqsepgkdf) | [GitHub](https://github.com/theokrueger/speedpub)

### StoryBytes  (HackUMass XII)

- **Prizes:** Best Use of GenAI [unknown]  (tier: track_winner)
- **Pitch:** Kids' story generator producing text, illustrations and spoken narration from a description, with poem mode and clickable vocabulary.
- **Problem / user:** Children want to turn their ideas into stories, at suitable reading levels and in various languages. / children, parents, language learners
- **Domain / idea type:** education + creative_media / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; generative_media; speech_or_voice
- **Stack:** langs TypeScript; JavaScript; frontend React; backend Node.js; Express; db ; hosting 
- **Tech/APIs:** OpenAI GPT-4o (ai_model, core); getimg.ai (ai_model, core); Black Forest Labs (ai_model, supporting); ElevenLabs (ai_model, core); Free Dictionary API (data_source, supporting)
- **Sponsor APIs:**  | fit: Multi-step generative pipeline covering text, images and audio fits the GenAI category.
- **Repo:** public, commits 142 (before/in/after event: 0/139/3), README solid
- **Demo/writeup:** video False, live none, screenshots 16, writeup long, impact claims False
- **Notes:** Chains GPT-4o, getimg.ai/Black Forest Labs images and ElevenLabs TTS; DALL-E access failed so image model was swapped; backend caches files to cut latency.
- **Team size:** 6 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/storybytes) | [GitHub](https://github.com/Citrus216/storybytes)

### The Miraculous Bits and Bytes Fuzzer  (HackUMass XII)

- **Prizes:** Nord Security Add-On [unknown]  (tier: sponsor_winner)
- **Pitch:** A Go fuzzer that mutates bytes of an input file, feeds it to a target program and logs the crashing byte and error.
- **Problem / user:** Developers lack an easy, efficient way to find vulnerabilities in their programs. / software developers
- **Domain / idea type:** safety_security + dev_tools / dev_tool
- **Platforms / hardware / AI:** cli / False / False
- **Stack:** langs Go; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Go (framework, core); VS Code (other, token)
- **Sponsor APIs:**  | fit: Security-themed byte-mutation fuzzer submitted for the Nord Security add-on prize; no Nord product is named.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Team was new to Go and fuzzing; tested against public GitHub projects; page has no screenshots; GitHub link points to a branch.
- **Team size:** 4 | **Confidence:** high | unverified: sponsor_fit_note; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/a-miraculous-fuzzer) | [GitHub](https://github.com/azb0222/Fuzzer/tree/final)

### The Wave  (HackUMass XII)

- **Prizes:** [MLH] Best Use of MongoDB Atlas [unknown]  (tier: sponsor_winner)
- **Pitch:** Native iOS app that maps local social events and gatherings on a live map using geolocation.
- **Problem / user:** People miss nearby social events because discovery is scattered; the app surfaces gatherings around them. / people looking for local social events
- **Domain / idea type:** social_community / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / False / False
- **Stack:** langs Swift; Python; frontend SwiftUI; backend Flask; db MongoDB; hosting Terraform
- **Tech/APIs:** MongoDB (database, core, sponsor); Flask (framework, core); SwiftUI (framework, core); Terraform (other, supporting); .tech domain (other, supporting, sponsor)
- **Sponsor APIs:** MongoDB Atlas | fit: Won Best Use of MongoDB Atlas; MongoDB stores the app's user and event data behind a Flask API.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 13, writeup medium, impact claims False
- **Notes:** Switched from React Native to SwiftUI mid-hackathon; Flask API backed by MongoDB; Terraform listed; the writeup claims a working real-time event map prototype.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; github_url; demo_video_url
- **Links:** [Devpost](https://devpost.com/software/the-wave-v21rau)

### Tomo  (HackUMass XII)

- **Prizes:** Second Prize [2nd]  (tier: overall_top3)
- **Pitch:** Space Invaders-style Python game where OpenAI generates per-round twists such as bosses, portals and black holes, controllable with a Leap Motion hand tracker.
- **Problem / user:** No problem stated; aims to bring AI into a favourite hobby, retro gaming. / gamers
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / True / llm_chat; generative_media
- **Stack:** langs Python; C++; frontend pygame; backend ; db ; hosting 
- **Tech/APIs:** OpenAI API (ai_model, core); Leap Motion controller (hardware_part, core, sponsor); pygame (framework, core)
- **Sponsor APIs:** Leap Motion (hardware provided by HackUMass)
- **Repo:** public, commits 74 (before/in/after event: 0/70/4), README solid
- **Demo/writeup:** video None, live none, screenshots 3, writeup medium, impact claims False
- **Notes:** LLM responses are converted into executable Python that alters gameplay; Leap Motion input comes from a C++ script piped in as keyboard events; hardware loaned by the hackathon.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ai_types
- **Links:** [Devpost](https://devpost.com/software/tomo-dmajc3) | [GitHub](https://github.com/Ben-Santana/AI-Space-Invaders)

### VR Breadboard  (HackUMass XII)

- **Prizes:** Best AR/VR Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** Unity VR virtual breadboard where users place components and wire circuits to learn electronics hands-on.
- **Problem / user:** Learning circuit design needs physical parts and lab access; a VR breadboard makes practice accessible and safe. / electronics students and educators
- **Domain / idea type:** education / creative_tool
- **Platforms / hardware / AI:** other / True / None
- **Stack:** langs C#; Python; frontend Unity; backend ; db ; hosting 
- **Tech/APIs:** Unity (framework, core); Meta VR/XR (hardware_part, core); OpenAI (ai_model, unclear); Pygame (framework, unclear)
- **Sponsor APIs:**  | fit: Won Best AR/VR Hack with a Unity-based VR circuit-building simulator, matching the AR/VR category.
- **Repo:** public, commits 7 (before/in/after event: 0/7/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 10, writeup long, impact claims False
- **Notes:** Built in Unity with C# for Meta headsets; tags also list OpenAI, RAG and vision though the visible writeup excerpt centers on component simulation; main challenge was accurate component behavior.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; ai_used; has_hardware; ai_types
- **Links:** [Devpost](https://devpost.com/software/circuit-simulator) | [GitHub](https://github.com/Parth12358/Circuit-Simulator-Kit)

### WorldWide Rover  (HackUMass XII)

- **Prizes:** Best Embedded System [unknown]  (tier: track_winner)
- **Pitch:** Raspberry Pi and Arduino rover with maze and obstacle avoidance that anyone can drive in real time from a web interface.
- **Problem / user:** Remote control of robots is hard to access for learning; the team wanted NASA-style rover operation from any browser. / robotics learners and remote operators
- **Domain / idea type:** education + other / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / False
- **Stack:** langs Python; C++; JavaScript; frontend React; backend Flask; db ; hosting AWS; ngrok
- **Tech/APIs:** Raspberry Pi (hardware_part, core); Arduino (hardware_part, core); Flask (framework, core); React (framework, supporting); ngrok (other, supporting); AWS (cloud, supporting); RPi.GPIO (framework, supporting)
- **Sponsor APIs:**  | fit: Targeted the embedded-system track with a Raspberry Pi and Arduino rover linked by UART and driven over the web.
- **Repo:** public, commits 32 (before/in/after event: 0/32/0), README solid
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Pi sends commands over UART to an Arduino that drives the motors; Flask server hit from a React page via AWS and ngrok; 12V battery power was a challenge.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; domain_secondary
- **Links:** [Devpost](https://devpost.com/software/worldwide-rover) | [GitHub](https://github.com/Manujake/HackUMass2024)


## HackUMass XIII

### $HackProof  (HackUMass XIII)

- **Prizes:** [MLH] Best Use of Solana [unknown]  (tier: sponsor_winner)
- **Pitch:** On-chain hackathon voting on Solana: soulbound NFT badges for participants, $HACK vote tokens, project NFTs and a live leaderboard.
- **Problem / user:** Hackathon scoring is decided by a few judges in a centralized process with little community recognition. / hackathon participants and organizers
- **Domain / idea type:** civic_legal + social_community / new_category
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; Rust; frontend Next.js; Tailwind; backend Solana programs; db IPFS; hosting Vercel
- **Tech/APIs:** Solana (devnet, SPL tokens) (other, core, sponsor); Rust (framework, core); Phantom wallet (auth, supporting); NFT.Storage / IPFS (other, supporting); Next.js (framework, core); Vercel (cloud, supporting)
- **Sponsor APIs:** Solana | fit: Built the voting, registration and soulbound NFT logic as Solana programs in Rust on devnet with SPL tokens.
- **Repo:** public, commits 79 (before/in/after event: 0/76/3), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup long, impact claims False
- **Notes:** Rust Solana programs on devnet, Phantom wallet login, IPFS metadata via NFT.Storage, and QR-code mobile voting for live demos; 100 tokens issued per participant.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/hackproof-r9v24j) | [GitHub](https://github.com/namerror/HackProof-prototype)

### 3D Printing Kiosk  (HackUMass XIII)

- **Prizes:** Winner Second Prize [2nd]  (tier: overall_top3)
- **Pitch:** Makerspace kiosk where students scan an ID on a custom ESP32 RFID reader to authorize and start a sliced 3D print.
- **Problem / user:** Makerspace 3D printing had no checks on print length, printer count, training status or ownership of failed prints. / makerspace staff and CICS students
- **Domain / idea type:** productivity_workplace + education / hardware_gadget
- **Platforms / hardware / AI:** desktop; hardware / True / False
- **Stack:** langs C++; QML; frontend Qt Quick; backend ; db SQL (database software switched during build); hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); PN5180 RFID module (hardware_part, core); Qt Quick (framework, core); OrcaSlicer (other, core); PlatformIO (other, supporting); Fusion (CAD) (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 123 (before/in/after event: 0/11/112), README thin
- **Demo/writeup:** video True, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Solo build: custom PN5180 RFID reader with 3D-printed case, Qt/QML kiosk app, OrcaSlicer integration by mimicking OctoPrint API, derives stable ID from encrypted campus cards. Second repo: card-reader-firmware.
- **Team size:** 1 | **Confidence:** high | unverified: stack_database
- **Links:** [Devpost](https://devpost.com/software/pcm-3d-printing-kiosk) | [GitHub](https://github.com/Atyrnal/PCMakerspace3DPKiosk ; https://github.com/Atyrnal/card-reader-firmware)

### Amby  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Hardware] Best Circuit Hack [unknown]  (tier: track_winner)
- **Pitch:** ESP32 noise-level monitor with LED indicators and a dashboard showing quiet spots over time.
- **Problem / user:** People want quiet places to hang out and ways to avoid noise complaints without costly decibel meters. / students, gamers, partygoers
- **Domain / idea type:** social_community / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / False
- **Stack:** langs Python; C++; HTML; frontend Jinja; HTML; backend FastAPI; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Microphone (hardware_part, core); FastAPI (framework, supporting); Plotly (framework, supporting); Pandas (framework, supporting)
- **Sponsor APIs:**  | fit: Circuit built around an ESP32 microphone input and LEDs.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 11, writeup medium, impact claims False
- **Notes:** LED colors indicate threshold states; dashboard charts are static Plotly/Matplotlib; multi-location WiFi data collection listed as future work.
- **Team size:** 2 | **Confidence:** high | unverified: repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/amby) | [GitHub](https://github.com/HumanAri/Amby)

### AR Cube Cannon  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Hardware] Best Hardware Hack [unknown]  (tier: track_winner)
- **Pitch:** Handheld device with a transparent OLED showing a virtual grid where cubes can be placed or removed, like a block tool gun.
- **Problem / user:** Playful take on placing blocks in real life; no practical problem stated. / makers and gamers
- **Domain / idea type:** entertainment_games + creative_media / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / False
- **Stack:** langs C++; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Arduino (hardware_part, core); Transparent OLED display (hardware_part, core); IMU (hardware_part, core)
- **Sponsor APIs:**  | fit: Physical device with custom body, display and sensors.
- **Repo:** public, commits 2 (before/in/after event: 0/2/0), README none
- **Demo/writeup:** video False, live none, screenshots 12, writeup short, impact claims False
- **Notes:** Built from scrap makerspace parts; IMU position drift forced a pivot to button-based position with orientation; custom 3D cube rendering pipeline.
- **Team size:** 4 | **Confidence:** high | unverified: tech_items_details
- **Links:** [Devpost](https://devpost.com/software/ar-cube-cannon) | [GitHub](https://github.com/Magirush/AR-Cube-Cannon)

### Atlas  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Software] Best Web Hack [unknown]  (tier: track_winner)
- **Pitch:** Upload images, embed with CLIP, project to 3D with PCA, cluster with k-means and explore the result in an interactive 3D map.
- **Problem / user:** Seeing how images relate semantically is hard in a flat gallery. / people exploring image collections
- **Domain / idea type:** creative_media + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; predictive_ml; rag_or_search
- **Stack:** langs Python; JavaScript; frontend React; Vite; React Three Fiber; Tailwind CSS; Zustand; backend FastAPI; db Supabase PostgreSQL; hosting 
- **Tech/APIs:** OpenAI CLIP (ai_model, core); scikit-learn (framework, core); React Three Fiber (framework, core); Supabase (database, supporting); Gemini (ai_model, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:**  | fit: Full-stack web app with a Python backend and 3D React frontend.
- **Repo:** public, commits 32 (before/in/after event: 0/22/10), README solid
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Combines kNN graph with an MST for connectivity; chose PCA over UMAP for speed; Gemini mentioned for image descriptions; JWT auth through Supabase.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/atlas-5pzm69) | [GitHub](https://github.com/c-aly/Atlas)

### Birders' Cuckoo Clock  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Hardware] Best Beginner Hardware [unknown]  (tier: track_winner)
- **Pitch:** Raspberry Pi Pico digital cuckoo clock that plays a random bird call each hour and shows the bird's name on an LCD.
- **Problem / user:** A first-time hacker wanted a fun way to learn to identify bird calls like her birding family. / casual birders and families
- **Domain / idea type:** entertainment_games + education / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / False
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Raspberry Pi Pico (hardware_part, core); 16x2 LCD display (hardware_part, core); LM386 amplifier + speaker (hardware_part, core)
- **Sponsor APIs:**  | fit: Won the event-run Best Beginner Hardware prize with a solo first-hackathon Pico build.
- **Repo:** public, commits 16 (before/in/after event: 0/13/3), README thin
- **Demo/writeup:** video False, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Solo first-hackathon build on a breadboard with Pico, 16x2 LCD wired in 8-pin mode, LM386 amplifier and speaker; hardware parts were limited.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/birders-cuckoo-clock) | [GitHub](https://github.com/sharayujosh/hackathon25)

### Clause  (HackUMass XIII)

- **Prizes:** [MLH] Best Use of AI powered by Reach Capital [unknown]  (tier: sponsor_winner)
- **Pitch:** AI platform that scans leases, medical bills and contracts for rights violations, computes dollar impact and drafts enforcement letters, with a Chrome extension.
- **Problem / user:** Ordinary people lack the legal knowledge to spot tenant, billing or contract violations that cost them money. / tenants, patients and consumers
- **Domain / idea type:** civic_legal + fintech_finance / automation_or_agent
- **Platforms / hardware / AI:** web; browser_extension / False / llm_chat; rag_or_search; speech_or_voice; agent_or_tool_use
- **Stack:** langs Python; TypeScript; JavaScript; frontend Next.js; React; backend FastAPI; db Snowflake; hosting Vultr; Cloudflare
- **Tech/APIs:** Gemini (ai_model, core, sponsor); Snowflake Cortex (database, core, sponsor); ElevenLabs (ai_model, supporting, sponsor); Solana (other, unclear, sponsor); Vultr (cloud, supporting, sponsor); Cloudflare (cloud, supporting); MCP (other, unclear); FastAPI (framework, core); spaCy (framework, supporting)
- **Sponsor APIs:** Gemini; Snowflake; ElevenLabs; Solana; Vultr | fit: Won Best Use of AI powered by Reach Capital; the project applies Gemini with Snowflake Cortex RAG to help ordinary people enforce legal rights.
- **Repo:** public, commits 10 (before/in/after event: 0/10/0), README solid
- **Demo/writeup:** video True, live none, screenshots 25, writeup long, impact claims True (Opens with claims about billions of dollars lost to unenforced tenant, medical-bill and consumer rights; also asserts zero hallucinations.)
- **Notes:** RAG grounded on retrieved statutes via Snowflake Cortex to curb Gemini hallucinations, PII redaction before LLM calls, React web app plus Chrome extension, ElevenLabs voice and Solana listed; three repos.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/clause-bu9l74) | [GitHub](https://github.com/sh1v-ansh/clause-backend)

### Data Security Hub  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Cybersecurity] Best Beginner Cybersecurity Hack [unknown]  (tier: track_winner)
- **Pitch:** Beginner tool that encrypts and decrypts data on the fly and uses Gemini to generate strong themed passwords.
- **Problem / user:** Everyday users need an easy way to secure their own data and create strong but memorable passwords. / general users new to security
- **Domain / idea type:** safety_security / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs HTML; frontend HTML; backend ; db ; hosting 
- **Tech/APIs:** Google Gemini API (ai_model, core); HTML (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 4 (before/in/after event: 0/4/0), README thin
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Team says most code was produced with Google Gemini plus a little of their own; first time using AI in a project.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; platforms
- **Links:** [Devpost](https://devpost.com/software/data-security-hub) | [GitHub](https://github.com/LordBraveNick/DataSecHub)

### DataVault  (HackUMass XIII)

- **Prizes:** [MLH] Best Use of Vultr [unknown]  (tier: sponsor_winner)
- **Pitch:** Pipeline that anonymizes and AES-encrypts sensitive records, then lets users query them with Gemini via a privacy-preserving RAG flow hosted on Vultr.
- **Problem / user:** Organizations want AI insights from sensitive data like health or finance records without exposing raw personal information. / organizations with sensitive data
- **Domain / idea type:** safety_security + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web / False / rag_or_search; llm_chat
- **Stack:** langs Python; JavaScript; frontend HTML; CSS; JavaScript; backend FastAPI; gRPC; db PostgreSQL; ChromaDB; hosting Vultr; Docker
- **Tech/APIs:** Vultr (cloud, core, sponsor); Google Gemini (ai_model, core); ChromaDB (database, core); PostgreSQL (database, core); FastAPI (framework, supporting); gRPC (framework, supporting); Docker (other, supporting); Hugging Face embeddings (ai_model, supporting)
- **Sponsor APIs:** Vultr | fit: Hosts the whole pipeline in a Vultr cloud environment, which the writeup states as the cloud host.
- **Repo:** public, commits 21 (before/in/after event: 0/21/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 3, writeup long, impact claims False
- **Notes:** PII swapped for synthetic data before AES-256-CBC storage as blobs in PostgreSQL; embeddings built from anonymized data in ChromaDB; gRPC ingest with FastAPI RAG API; docker-compose deployment.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/datavault-cqajxi) | [GitHub](https://github.com/P-Bhanu-Sohan/DataVault)

### HALO  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [PIT] Best Accessibility Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** A Chrome extension that pauses videos on detecting seizure-risk flashing and offers Gemini summaries with ElevenLabs read-aloud for hard-to-read pages.
- **Problem / user:** Flashing video can trigger photosensitive seizures and dense web text is hard for people with ADHD or dyslexia. / People with photosensitive epilepsy, ADHD, dyslexia or visual impairments
- **Domain / idea type:** accessibility + health_wellness / social_good
- **Platforms / hardware / AI:** browser_extension / False / llm_chat; speech_or_voice
- **Stack:** langs JavaScript; HTML; CSS; frontend Vanilla JS; Manifest V3; backend ; db Chrome storage; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); ElevenLabs (ai_model, core); Chrome extension API (framework, core); WCAG 2.1 luminance (other, core)
- **Sponsor APIs:**  | fit: Accessibility prize: flash-seizure protection and reading/TTS assistance in one extension.
- **Repo:** public, commits 67 (before/in/after event: 0/60/7), README detailed
- **Demo/writeup:** video False, live none, screenshots 8, writeup long, impact claims True (Cites about 3% of people having photosensitive epilepsy and 12-48x performance gains.)
- **Notes:** Implements WCAG luminance flash detection locally on several video sites, plus a four-strategy text extractor; vanilla JS with no dependencies.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/halo-u73r9j) | [GitHub](https://github.com/athulya-anil/Halo)

### healthNET  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Ethical AI] Most Impactful AI Hack [unknown]  (tier: track_winner)
- **Pitch:** Federated-learning platform letting hospitals train shared models via Flower without sharing raw patient data.
- **Problem / user:** Privacy rules stop hospitals pooling data, leaving models biased and less accurate. / hospitals and medical institutions
- **Domain / idea type:** health_wellness + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; backend FastAPI; db ; hosting Vultr
- **Tech/APIs:** Flower (framework, core); Vultr (cloud, core, sponsor); FastAPI (framework, supporting); React (framework, supporting)
- **Sponsor APIs:** Vultr | fit: Used Vultr cloud credits to host the aggregator and train models.
- **Repo:** public, commits 54 (before/in/after event: 0/53/1), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 11, writeup long, impact claims True (Cites an estimate that about 30% of world data volume comes from healthcare.)
- **Notes:** Node servers plus aggregator using FedAvg; dashboards for client training/inference and aggregator; hosted on Vultr credits; cites a market-share statistic.
- **Team size:** 5 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/healthnet-h5o0dx) | [GitHub](https://github.com/HenryLiu714/healthnet)

### Interdict.  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Software] Best Software Hack [unknown]  (tier: track_winner)
- **Pitch:** SOCKS5 proxy that silently throttles connections to blocklisted sites the longer you use them, to discourage doomscrolling.
- **Problem / user:** Screen-time blockers are visible and easy to dodge; covert slowdowns could build frustration that reduces use. / people trying to cut screen time
- **Domain / idea type:** mental_health + productivity_workplace / new_category
- **Platforms / hardware / AI:** web; other / False / False
- **Stack:** langs Python; frontend Tailwind CSS; backend Flask; db ; hosting 
- **Tech/APIs:** SOCKS5 proxy (other, core); Flask (framework, supporting); Tailwind CSS (framework, supporting)
- **Sponsor APIs:**  | fit: Pure software networking tool, fits the Software track.
- **Repo:** public, commits 52 (before/in/after event: 0/52/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Uses aversive conditioning idea with a configurable throttle formula; only inspects destination, not content; hosted externally so iPhones can connect; pivoted from HTTP/S proxy to SOCKS5.
- **Team size:** 5 | **Confidence:** high | unverified: platforms
- **Links:** [Devpost](https://devpost.com/software/interdict) | [GitHub](https://github.com/theokrueger/interdict)

### minutemesh  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Cybersecurity] Most Impactful Cybersecurity Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** A pentest tool built on MeshTNC firmware that crafts Meshtastic packets impersonating any sender in channels where the key is known.
- **Problem / user:** Meshtastic channel messages are not signed, so sender identity rests on a spoofable MAC address, enabling undetectable impersonation. / Security researchers and pentesters of Meshtastic mesh radios
- **Domain / idea type:** safety_security + telecom_networking / dev_tool
- **Platforms / hardware / AI:** cli; hardware / True / False
- **Stack:** langs C; C++; JavaScript; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Meshtastic (other, core); MeshTNC firmware (hardware_part, core); LoRa radio (hardware_part, core); AES (other, supporting); Protobuf (framework, supporting); PlatformIO (framework, supporting)
- **Sponsor APIs:**  | fit: Targets the cybersecurity track by demonstrating a working impersonation attack on a mesh radio protocol.
- **Repo:** public, commits 1389 (before/in/after event: 1349/37/3), README detailed
- **Demo/writeup:** video False, live none, screenshots 3, writeup medium, impact claims False
- **Notes:** Integrates a previously published mesh-poisoning cryptography into radio firmware with a CLI; had to preserve protobuf structure when forging packets.
- **Team size:** 2 | **Confidence:** high | unverified: n_screenshots; team_size
- **Links:** [Devpost](https://devpost.com/software/minutemesh) | [GitHub](https://github.com/jordaeday/minutemesh)

### Obscurafy  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Cybersecurity] Best Data Protection [unknown]  (tier: sponsor_winner)
- **Pitch:** An iOS app that scans your photo library on-device for IDs and cards, letting you swipe to keep, blur or delete each flagged image.
- **Problem / user:** People share or keep photos exposing personal documents without noticing, risking data leaks. / iPhone users with sensitive photos in their library
- **Domain / idea type:** safety_security / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / False / vision; llm_chat
- **Stack:** langs Swift; Python; frontend SwiftUI; backend Swift server layer; db ; hosting 
- **Tech/APIs:** YOLOv11 (ai_model, core); CoreML (framework, core); PyTorch (framework, supporting); Gemini API (ai_model, supporting); Apple Photos API (other, core); VisionKit (framework, supporting)
- **Sponsor APIs:**  | fit: Fits the data protection prize via fully on-device detection and redaction before any cloud call.
- **Repo:** public, commits 48 (before/in/after event: 0/47/1), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 7, writeup long, impact claims False
- **Notes:** Custom YOLOv11 detector trained from eight merged open datasets and converted to CoreML; Tinder-style swipe review; redacts before sending to Gemini for explanations.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; live_demo_url classification (site link, also a Canva link listed)
- **Links:** [Devpost](https://devpost.com/software/vaulteye) | [GitHub](https://github.com/AlexanderMcGreevy/Obscurafy)

### OceanEye  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [PIT] Best Sustainability Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** A dashboard that detects floating ocean trash with YOLOv8, maps it with satellite data, and plans smoothed cleanup boat routes with Gemini insights.
- **Problem / user:** Ocean plastic cleanup is manual and inefficient, lacking detection, mapping and route planning. / Marine cleanup organizations and researchers
- **Domain / idea type:** sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; rag_or_search; llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; Three.js; backend Flask; db vector store; hosting Netlify; Vultr
- **Tech/APIs:** YOLOv8 (ai_model, core); Google Gemini (ai_model, core); Google Earth Engine (data_source, core); Sentinel-2 (data_source, supporting); OpenCV (framework, supporting); Vultr (cloud, supporting); Netlify (cloud, supporting)
- **Sponsor APIs:**  | fit: Sustainability prize: detection and route planning aimed at reducing cleanup fuel use.
- **Repo:** public, commits 26 (before/in/after event: 0/19/7), README detailed
- **Demo/writeup:** video False, live none, screenshots 5, writeup long, impact claims True (Cites millions of tons of plastic and over 100,000 marine animals harmed yearly as motivation.)
- **Notes:** Combines YOLOv8 segmentation, Earth Engine satellite data, a Gemini RAG pipeline and 2-opt plus Catmull-Rom route optimisation in one dashboard.
- **Team size:** 5 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/oceanhub) | [GitHub](https://github.com/Tirth2116/OceanEye)

### OnePen  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Ethical AI] Most Novel Use of AI [unknown]  (tier: track_winner)
- **Pitch:** Handwriting note-taking web app where a TensorFlow.js gesture model turns underlines, boxes and circles into formatting and tool actions.
- **Problem / user:** Switching to toolbars interrupts note-taking flow. / students and heavy note-takers
- **Domain / idea type:** productivity_workplace + education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs JavaScript; Python; frontend HTML Canvas; TensorFlow.js; backend Flask; db IndexedDB; hosting GitHub Pages
- **Tech/APIs:** TensorFlow.js (ai_model, core); Keras (framework, core); Pix2Text (ai_model, supporting); Google Drive API (other, supporting); Flask (framework, supporting)
- **Sponsor APIs:**  | fit: Custom-trained gesture recognition model drives the interface.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Team hand-wrote about 4,000 gesture samples, augmented to 36,000+; includes Pix2Text math recognition, Google Drive sync, IndexedDB autosave; no repo listed.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/onepen)

### Pacific  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Ethical AI] Best Theory and Plan [unknown]  (tier: track_winner)
- **Pitch:** Real-time 2D global-illumination renderer implementing radiance cascades with wgpu compute shaders on a Rust engine.
- **Problem / user:** Real-time ray tracing is noisy and costly; radiance cascades aim for sharp global illumination. / graphics programmers
- **Domain / idea type:** dev_tools + creative_media / other
- **Platforms / hardware / AI:** desktop / False / False
- **Stack:** langs Rust; WGSL; frontend ; backend ; db ; hosting 
- **Tech/APIs:** wgpu (framework, core); V4-Engine (framework, core); WGSL shaders (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 35 (before/in/after event: 0/34/1), README thin
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Implements a recent rendering technique from sparse technical papers; built on a teammate's V4-Engine; currently 2D with 3D in progress; no screenshots on page.
- **Team size:** 3 | **Confidence:** high | unverified: domain_primary
- **Links:** [Devpost](https://devpost.com/software/pacific) | [GitHub](https://github.com/gabefork/pacific)

### PixelParty  (HackUMass XIII)

- **Prizes:** Winner Third Prize [3rd]  (tier: overall_top3)
- **Pitch:** 64x64 LED matrix on a Raspberry Pi that mirrors a shared web drawing canvas in real time.
- **Problem / user:** Online interaction with friends feels remote; a physical shared display makes it feel present. / friends sharing a room display
- **Domain / idea type:** creative_media + social_community / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / False
- **Stack:** langs Python; JavaScript; C++; frontend HTML; CSS; JavaScript; backend Flask; db ; hosting 
- **Tech/APIs:** Raspberry Pi 3 B+ (hardware_part, core); Adafruit 64x64 LED matrix (hardware_part, core); rpi-led-matrix (framework, core); Flask (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 8 (before/in/after event: 0/8/0), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 5, writeup medium, impact claims False
- **Notes:** Drives the Adafruit panel without the usual HAT via rpi-led-matrix; Flask server spawns a separate panel process linked by a pipe; first hackathon for team.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/pixelparty) | [GitHub](https://github.com/AshwinSarma21/PixelParty)

### Plotholes  (HackUMass XIII)

- **Prizes:** [MLH] Best Use of Snowflake API [unknown]  (tier: sponsor_winner)
- **Pitch:** Geospatial platform that combines NYC 311 street-issue data, crowd reports and AI-analyzed photos into an interactive road-damage map.
- **Problem / user:** Road damage reports are scattered and hard to aggregate, so cities and drivers lack a clear view of problem areas. / drivers, city planners and local residents
- **Domain / idea type:** civic_legal + mobility_transport / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Leaflet; backend Flask; db PostgreSQL; Supabase; Snowflake; hosting 
- **Tech/APIs:** Snowflake Cortex (database, supporting, sponsor); YOLOv8 (ai_model, core); Hugging Face (ai_model, supporting); OpenStreetMap (maps_geo, supporting); NYC 311 open data (data_source, core); Supabase (database, supporting); Shapely (framework, supporting); .tech domain (other, supporting, sponsor)
- **Sponsor APIs:** Snowflake; Supabase; .Tech Domains | fit: Won Best Use of Snowflake API; the writeup names Snowflake Cortex among new tools used in its geospatial analytics pipeline, with limited detail on the exact role.
- **Repo:** public, commits 78 (before/in/after event: 0/77/1), README thin
- **Demo/writeup:** video False, live not_checked, screenshots 0, writeup long, impact claims False
- **Notes:** Original plan to cover Amherst or Boston was dropped for lack of data, so NYC 311 data was used; YOLOv8 and Hugging Face analyze images; Snowflake Cortex and Supabase added.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; demo_video_url; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/plothole) | [GitHub](https://github.com/GraceW03/Plotholes)

### Racing Sim Pedal Set  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Hardware] Best Mechanical Hack [unknown]  (tier: track_winner)
- **Pitch:** Custom machined racing-sim pedals with hall-effect sensors and load-cell brake feeding a Pico microcontroller.
- **Problem / user:** Makers wanted self-built racing pedals that work as game input. / sim racers
- **Domain / idea type:** entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / False
- **Stack:** langs C; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Raspberry Pi Pico (hardware_part, core); Hall effect sensors (hardware_part, core); Load cells (hardware_part, core)
- **Sponsor APIs:**  | fit: Machined mechanical pedal assembly.
- **Repo:** public, commits 3 (before/in/after event: 0/2/1), README solid
- **Demo/writeup:** video False, live none, screenshots 2, writeup short, impact claims False
- **Notes:** Aluminum and steel parts machined by the team at an ECE makerspace; 20kg load cells noted as too small; finished set works in racing games.
- **Team size:** 2 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/racing-sim-pedal-set) | [GitHub](https://github.com/audtheshaud/racing-sim-pedals)

### Reddit's Mood  (HackUMass XIII)

- **Prizes:** [MLH] Best .Tech Domain Name [unknown]  (tier: sponsor_winner)
- **Pitch:** 3D globe website that pulls Reddit posts and uses Gemini to score their emotion and intensity by location.
- **Problem / user:** The team wanted a way to see what mood the world is expressing at a glance. / curious general web users
- **Domain / idea type:** social_community + entertainment_games / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; JavaScript; frontend Framer; Spline; Three.js; HTML5; backend Django; db ; hosting Vultr
- **Tech/APIs:** .tech domain (other, supporting, sponsor); Gemini (ai_model, core, sponsor); Vultr (cloud, supporting, sponsor); Reddit API (data_source, core); Three.js (framework, supporting); Spline (other, supporting); Django (framework, core)
- **Sponsor APIs:** .Tech Domains; Gemini; Vultr | fit: Won Best .Tech Domain Name and runs on redditsmood.tech, alongside Gemini and Vultr use.
- **Repo:** public, commits 23 (before/in/after event: 0/19/4), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup short, impact claims False
- **Notes:** Django backend on Vultr with Gemini sentiment scoring; front end made with Framer, Spline and Three.js; team notes the globe finally rendering emotions at 7 am.
- **Team size:** 5 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/reddit-s-mood) | [GitHub](https://github.com/aamir-azeez/redditsmood)

### Resi  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Ethical AI] Best Beginner AI Hack [unknown]  (tier: track_winner)
- **Pitch:** Voice-driven dorm maintenance assistant that transcribes spoken issues, classifies them with GPT, and routes tickets to maintenance or RAs on a live dashboard.
- **Problem / user:** UMass students find dorm maintenance reporting slow, relying on paper forms, calls and emails that get lost. / UMass students, RAs and maintenance staff
- **Domain / idea type:** productivity_workplace + housing_real_estate / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross; web / False / speech_or_voice; llm_chat
- **Stack:** langs JavaScript; frontend Expo; React Native; backend Node.js; Express; db Firebase Realtime Database; hosting Render
- **Tech/APIs:** OpenAI Whisper (ai_model, core); GPT-4-Turbo (ai_model, core); Firebase (Auth, Realtime DB) (database, core); Expo / React Native (framework, core); Render (cloud, supporting); Cursor (other, token)
- **Sponsor APIs:**  | fit: Entered the Ethical AI beginner track with a voice-to-ticket assistant using Whisper and GPT-4-Turbo; the page does not discuss ethics.
- **Repo:** public, commits 56 (before/in/after event: 0/49/7), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup medium, impact claims False
- **Notes:** Asks clarifying questions before creating a ticket, auto-assigns queue positions synced every 5 seconds, and restricts sign-in to UMass accounts.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/resi) | [GitHub](https://github.com/RavjeetChahal/MoveMate/)

### SlideScribe  (HackUMass XIII)

- **Prizes:** [MLH] Best Use of ElevenLabs [unknown]  (tier: sponsor_winner)
- **Pitch:** Phone app that detects classroom slides through the camera and answers blind students' questions about slide content by audio.
- **Problem / user:** Blind and visually impaired students cannot see slide images, charts or text, so they struggle to follow lectures. / blind and visually impaired students
- **Domain / idea type:** accessibility + education / social_good
- **Platforms / hardware / AI:** mobile_cross / False / vision; speech_or_voice; llm_chat
- **Stack:** langs Dart; Python; frontend Flutter; backend Python; db ; hosting 
- **Tech/APIs:** ElevenLabs (ai_model, core, sponsor); Gemini API (ai_model, core); OpenCV (framework, core); EasyOCR (framework, core); Flutter (framework, core)
- **Sponsor APIs:** ElevenLabs | fit: Uses ElevenLabs text-to-speech to speak slide descriptions and answers to students through earbuds.
- **Repo:** public, commits 28 (before/in/after event: 0/27/1), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Combines OpenCV slide segmentation, EasyOCR and vision-language models, with spoken answers through earbuds so they do not clash with the teacher.
- **Team size:** 5 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/and_then_there_was_light) | [GitHub](https://github.com/SuyashManiyar/HackUMass_codebase)

### Soundbrush  (HackUMass XIII)

- **Prizes:** Winner Grand Prize [1st]  (tier: overall_top3)
- **Pitch:** Drawing web app that plays a synth note and shows a color name for the selected hue, aimed at visually impaired artists.
- **Problem / user:** People with visual impairments cannot easily identify the color they are drawing with. / visually impaired artists
- **Domain / idea type:** accessibility + creative_media / creative_tool
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs JavaScript; CSS; frontend Next.js; React; p5.js; Tone.js; backend ; db ; hosting 
- **Tech/APIs:** p5.js (framework, core); Tone.js (framework, core); Next.js (framework, supporting); Figma (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 23 (before/in/after event: 0/23/0), README solid
- **Demo/writeup:** video False, live none, screenshots 8, writeup medium, impact claims False
- **Notes:** Eight synth notes mapped to hue; undo/redo and save/load of sketches; Figma prototype by one member, implemented by the other. Placement 1st inferred from Grand Prize name.
- **Team size:** 2 | **Confidence:** high | unverified: placement
- **Links:** [Devpost](https://devpost.com/software/sound-art-app) | [GitHub](https://github.com/maxdopp/SoundBrush)

### TabSense  (HackUMass XIII)

- **Prizes:** [MLH] Best Use of Gemini API [unknown]  (tier: sponsor_winner)
- **Pitch:** Chrome extension that uses the Gemini API to classify open tabs by content and intent and group them automatically.
- **Problem / user:** Manually grouping browser tabs is tedious, so many open tabs stay disorganized. / heavy browser tab users
- **Domain / idea type:** productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** browser_extension / False / llm_chat
- **Stack:** langs JavaScript; HTML; CSS; frontend Chrome extension; backend ; db ; hosting 
- **Tech/APIs:** Gemini API (ai_model, core, sponsor); Chrome Extension APIs (framework, core)
- **Sponsor APIs:** Gemini API | fit: Won Best Use of Gemini API; Gemini classifies each open tab to decide its group.
- **Repo:** public, commits 30 (before/in/after event: 0/30/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 10, writeup medium, impact claims False
- **Notes:** Extension popup UI built in plain JavaScript, HTML and CSS; Gemini calls go through a backend, and the team struggled with auth and async handling.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/tabsense-7dh05r) | [GitHub](https://github.com/anshuanjna/TabSense)

### Tandem  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Software] Best Beginner Software [unknown]  (tier: track_winner)
- **Pitch:** Web app that matches UMass students with study partners in the moment, using real class listings.
- **Problem / user:** The university's study-buddy tool is barely used, so students struggle to find partners on the spot. / UMass students
- **Domain / idea type:** education + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; JavaScript; frontend HTML5; JavaScript; backend FastAPI; db SQLAlchemy; hosting Render
- **Tech/APIs:** FastAPI (framework, core); SQLAlchemy (database, core); Render (cloud, supporting); .tech domain (other, supporting, sponsor)
- **Sponsor APIs:** .Tech Domains | fit: Won the event-run Best Beginner Software prize; team was all first-timers.
- **Repo:** public, commits 25 (before/in/after event: 0/24/1), README thin
- **Demo/writeup:** video False, live not_checked, screenshots 1, writeup medium, impact claims False
- **Notes:** Class data pulled from the UMass directory into a SQLAlchemy database; FastAPI backend deployed on Render; all team members were first-time hackers.
- **Team size:** 5 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/tandem-t0zvo4) | [GitHub](https://github.com/paperfour/tandem)

### Vault  (HackUMass XIII)

- **Prizes:** [HACKUMASS] [Software] Best Mobile Hack [unknown]  (tier: track_winner)
- **Pitch:** iOS app that blocks chosen apps based on geofenced locations like gyms and dining halls.
- **Problem / user:** People stay glued to their phones in public places. / phone users wanting fewer distractions
- **Domain / idea type:** mental_health + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / False / False
- **Stack:** langs Swift; frontend ; backend ; db SQLite; hosting 
- **Tech/APIs:** MapKit (maps_geo, core); SQLite (database, supporting)
- **Sponsor APIs:**  | fit: Native iOS app.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 7, writeup short, impact claims False
- **Notes:** Very short writeup of a few lines; native Swift with MapKit geofencing and SQLite; solo entry.
- **Team size:** 1 | **Confidence:** high | unverified: repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/vault-mk1l65) | [GitHub](https://github.com/BraedenTurner22/Vault)
