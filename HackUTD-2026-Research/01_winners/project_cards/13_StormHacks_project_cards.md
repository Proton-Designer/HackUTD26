# StormHacks: project cards (55 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## StormHacks 2025

### Air Command  (StormHacks 2025)

- **Prizes:** [MLH] Best Use of Snowflake API [unknown]  (tier: sponsor_winner)
- **Pitch:** Sip-and-puff breath sensor on a BeagleBone that acts as a Bluetooth keyboard and mouse, with optional voice commands mapped by Snowflake Cortex.
- **Problem / user:** People with limited mobility need accessible computer input without hands. / people with limited mobility
- **Domain / idea type:** accessibility + dev_tools / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / speech_or_voice; llm_chat
- **Stack:** langs Python; C; frontend ; backend BlueZ; db ; hosting 
- **Tech/APIs:** Snowflake Cortex LLM (ai_model, supporting, sponsor); BeagleBone AI / ZenHat (hardware_part, core); MPXV7002DP pressure sensor (hardware_part, core); BlueZ HID over GATT (other, core)
- **Sponsor APIs:** Snowflake Cortex | fit: Added an optional layer where Snowflake Cortex LLM maps natural-language voice commands into HID key sequences.
- **Repo:** public, commits 15 (before/in/after event: 0/15/0), README thin
- **Demo/writeup:** video False, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Differential air pressure sensor into a BeagleBone ADC, sip/puff classified by a state machine, emulated as BLE HID over GATT; Cortex LLM turns spoken commands into key sequences.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/air-command-smu9t0) | [GitHub](https://github.com/bsbhakti/stormhacks)

### ASL Express – Touchless AI Food Ordering Assistant  (StormHacks 2025)

- **Prizes:** Best Hardware [unknown]  (tier: track_winner)
- **Pitch:** Touchless drive-thru style ordering that reads sign-language gestures from a laptop camera, speaks the order, and shows status on an ESP32 device.
- **Problem / user:** Deaf and mute customers find drive-thru and counter ordering stressful or inaccessible. / deaf and mute customers and food vendors
- **Domain / idea type:** accessibility + food_nutrition / hardware_gadget
- **Platforms / hardware / AI:** desktop; hardware / True / vision; speech_or_voice; llm_chat
- **Stack:** langs Python; C++; frontend ; backend Python; PySerial; db ; hosting 
- **Tech/APIs:** Google Gemini API (ai_model, core, sponsor); MediaPipe (ai_model, core); OpenCV (framework, supporting); ElevenLabs (ai_model, supporting, sponsor); ESP32 (hardware_part, core); LCD, LEDs, buzzer, ultrasonic sensor (hardware_part, supporting)
- **Sponsor APIs:** Google Gemini API; ElevenLabs | fit: Won Best Hardware with an ESP32-based ordering kiosk prototype paired with camera gesture recognition.
- **Repo:** public, commits 1 (before/in/after event: 0/1/0), README none
- **Demo/writeup:** video False, live none, screenshots 31, writeup long, impact claims False
- **Notes:** MediaPipe hand tracking with Gemini for gesture intent, ElevenLabs speech, and an ESP32 with LCD, LEDs, buzzer and ultrasonic sensor over serial; three repos (main, backend, hardware).
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; demo_video_url
- **Links:** [Devpost](https://devpost.com/software/sign2order-touchless-ai-food-ordering-assistant) | [GitHub](https://github.com/KashfiRashid/ASL_Express)

### Carrie - AI Therapy In Your Pocket  (StormHacks 2025)

- **Prizes:** [MLH] Best Use of ElevenLabs [unknown]  (tier: sponsor_winner)
- **Pitch:** Emotion-aware AI therapy companion that holds live video calls, detecting facial emotion and replying with a voice.
- **Problem / user:** Burnout is rising while traditional therapy is costly and hard to access around the clock. / burned-out professionals and healthcare workers
- **Domain / idea type:** mental_health + health_wellness / new_category
- **Platforms / hardware / AI:** web / False / vision; speech_or_voice; llm_chat
- **Stack:** langs TypeScript; Python; JavaScript; frontend React; backend Node.js; Express; Flask; db MongoDB; hosting 
- **Tech/APIs:** ElevenLabs (ai_model, core, sponsor); LiveKit (other, core); Hugging Face Transformers (ViT emotion model) (ai_model, core); PyTorch (framework, supporting); MongoDB (database, supporting)
- **Sponsor APIs:** ElevenLabs | fit: Won Best Use of ElevenLabs; ElevenLabs provides the companion's voice in live video therapy sessions.
- **Repo:** public, commits 65 (before/in/after event: 0/65/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 19, writeup long, impact claims False
- **Notes:** Microservices: React/TypeScript front end, Node/Express API with MongoDB, Flask service running a ViT emotion model; LiveKit for video and ElevenLabs for voice; a Canva deck is linked.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; demo_video_url; impact_claims
- **Links:** [Devpost](https://devpost.com/software/carrie-ai-therapy-in-your-pocket) | [GitHub](https://github.com/TimSeah/StormHacks_LumberLoons)

### ConnectSFU  (StormHacks 2025)

- **Prizes:** Software Systems Prize [unknown]  (tier: track_winner)
- **Pitch:** Central web hub for SFU club events with a club-admin view, buddy finding and Gemini-powered AI search.
- **Problem / user:** Club event information at SFU is scattered across channels, making events hard to discover. / SFU students and club organizers
- **Domain / idea type:** social_community + education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs TypeScript; frontend React; Tailwind CSS; DaisyUI; backend ; db Supabase; hosting Vercel
- **Tech/APIs:** Gemini API (ai_model, supporting, sponsor); Supabase (database, core); React (framework, core); Vercel (cloud, supporting)
- **Sponsor APIs:** Gemini API | fit: Won the Software Systems Prize, an event prize, for a multi-view event platform with a database backend and AI search.
- **Repo:** public, commits 66 (before/in/after event: 0/66/0), README solid
- **Demo/writeup:** video False, live not_checked, screenshots 7, writeup long, impact claims False
- **Notes:** Separate user and club-administrator views; Gemini API powers natural-language event search; Supabase backend; design done in Figma and Procreate; deployment trouble late in the build.
- **Team size:** 5 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/connectsfu) | [GitHub](https://github.com/avkap007/stormhacks-connectsfu)

### EcoDepot  (StormHacks 2025)

- **Prizes:** SEE Sustainable Engineering Track [unknown]; Surge Choice Award [unknown]  (tier: sponsor_winner)
- **Pitch:** A smart recycling bin that identifies items with computer vision, rotates to the right compartment, and credits bottle-deposit money to a student-ID login.
- **Problem / user:** People misplace recyclables in bins and lack incentive to recycle. / University students and campus recycling programs
- **Domain / idea type:** sustainability_climate + retail_consumer / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision; predictive_ml
- **Stack:** langs Python; C++; frontend React; Next.js; backend Next.js; db Supabase; hosting Netlify
- **Tech/APIs:** TensorFlow (ai_model, core); Arduino (hardware_part, core); Supabase (database, supporting); Fusion 360 (other, supporting); Netlify (cloud, supporting)
- **Sponsor APIs:**  | fit: Sustainable engineering track: hardware recycling sorter tied to UN SDGs 9 and 12; Surge Choice basis not stated.
- **Repo:** public, commits 90 (before/in/after event: 0/89/1), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 4, writeup long, impact claims False
- **Notes:** 3D-printed rotating bin driven by a microcontroller; student ID barcode read by vision serves as login since the magnetic stripe was inaccessible; Fusion 360 link listed.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/ecodepot) | [GitHub](https://github.com/iancdev/recycle-sorter)

### EcoTag  (StormHacks 2025)

- **Prizes:** United Nations Sustainable Development Goals Enactus Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** A phone-based QR laser tag game that also has players scan litter, classify it with a vision model, and score points for sorting it correctly.
- **Problem / user:** Laser tag is tied to expensive arenas and post-gathering cleanup is a chore that people skip or sort wrongly. / Groups and schools playing casually outdoors or indoors
- **Domain / idea type:** sustainability_climate + entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs TypeScript; frontend React; Vite; ZXing-WASM; backend Node.js; Express; WebSockets; db Firebase; hosting Vercel
- **Tech/APIs:** OpenAI Vision API (ai_model, core); ZXing-WASM (framework, core); WebSockets (framework, core); Firebase (database, supporting); Vercel Edge Functions (cloud, supporting)
- **Sponsor APIs:**  | fit: UN SDG track: gamified litter sorting with CO2 savings estimates, mapped to several SDGs.
- **Repo:** public, commits 41 (before/in/after event: 0/40/1), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 9, writeup long, impact claims True (Reports QR accuracy of 95 percent, sub-100ms latency, and says it was chosen among 778 participants.)
- **Notes:** Browser QR detection with ZXing-WASM over a WebSocket event bus; page reports latency and accuracy figures; two repos linked on the page, backend one recorded.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; github_url (two repos listed); sections mapping
- **Links:** [Devpost](https://devpost.com/software/taqr) | [GitHub](https://github.com/fesenjuniors/backend)

### EduFind  (StormHacks 2025)

- **Prizes:** Best Use of SFU Courses API [unknown]  (tier: sponsor_winner)
- **Pitch:** A course-selection site recommending SFU courses by metrics, with a course builder and a social space to discuss courses.
- **Problem / user:** Selecting courses is clunky; students want easier choosing plus peer interaction around courses. / SFU students choosing courses
- **Domain / idea type:** education + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / recommendation; llm_chat
- **Stack:** langs JavaScript; TypeScript; CSS; HTML; SQL; frontend React; Tailwind CSS; backend Express.js; db Supabase; hosting 
- **Tech/APIs:** SFU Courses API (data_source, core, sponsor); DeepSeek API (ai_model, supporting); Supabase (database, core); Figma (other, token)
- **Sponsor APIs:** SFU Courses API | fit: Course builder and recommendations built on the SFU course API data.
- **Repo:** public, commits 124 (before/in/after event: 0/85/39), README solid
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Combines the course API with a DeepSeek API for recommendations and a community page; the writeup admits scope creep cut planned features.
- **Team size:** 4 | **Confidence:** medium | unverified: ai_used; ai_types; n_screenshots; team_size; SFU Courses API is_sponsor
- **Links:** [Devpost](https://devpost.com/software/edufind-aveu6k) | [GitHub](https://github.com/StormHacks-2025/ProjectCourseBuilder)

### Encore  (StormHacks 2025)

- **Prizes:** Most Likely to Become a Startup [unknown]  (tier: track_winner)
- **Pitch:** Mobile app showing which friends are attending nearby concerts, with an optional shared seat number to find them in the venue.
- **Problem / user:** Concerts are social but people rarely know which friends are going or how to find them once inside. / concert-goers
- **Domain / idea type:** social_community + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / False
- **Stack:** langs TypeScript; frontend Expo; TailwindCSS; backend Vercel; db Firestore; hosting Vercel
- **Tech/APIs:** Expo (framework, core); Firebase Auth / Firestore (database, core); Ticketmaster API (data_source, core); TailwindCSS (framework, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:**  | fit: Won the startup-potential award; the page makes no market-size claims and lists a Canva deck link.
- **Repo:** public, commits 5 (before/in/after event: 0/5/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Event feed pulled from Ticketmaster API via a Vercel backend; a Canva link is listed alongside the repo (likely a pitch deck).
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; team_size; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/encore-vzilag) | [GitHub](https://github.com/zhaojzn/encore-demo-app)

### FretNot  (StormHacks 2025)

- **Prizes:** IEEE SFU Prize Track [unknown]  (tier: sponsor_winner)
- **Pitch:** A clip-on guitar attachment with laser diodes that light chord finger positions, driven by a web app that parses song chords over Bluetooth.
- **Problem / user:** Beginners struggle to learn chord finger positions on the fretboard. / Beginner guitar learners
- **Domain / idea type:** education + creative_media / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / None
- **Stack:** langs TypeScript; C++; frontend React; backend ; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Laser diodes (hardware_part, core); Bluetooth Low Energy (other, core); Tesseract OCR (other, supporting); OnShape (other, supporting)
- **Sponsor APIs:**  | fit: IEEE track: an electronics project with microcontroller, lasers and custom enclosure.
- **Repo:** public, commits 8 (before/in/after event: 0/4/4), README solid
- **Demo/writeup:** video False, live none, screenshots 2, writeup long, impact claims False
- **Notes:** ESP32 with laser diodes in a custom 3D-printed enclosure; OCR (Tesseract) parses chord sheets, but only four chords were supported due to limited pins.
- **Team size:** 4 | **Confidence:** high | unverified: ai_used; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/fretnot) | [GitHub](https://github.com/doruphin/fretnot)

### GANPI  (StormHacks 2025)

- **Prizes:** Safe Software Best Modern C++ [unknown]  (tier: sponsor_winner)
- **Pitch:** Web AI assistant powered by Gemini that generates code, explains concepts and solves problems, with a C++ command-line component.
- **Problem / user:** The team wanted a natural, fast, clean interface for interacting with Gemini's API. / developers and general users
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web; cli / False / llm_chat
- **Stack:** langs C++; JavaScript; frontend Next.js; backend Node.js; db ; hosting Vercel
- **Tech/APIs:** Gemini API (ai_model, core); C++ (framework, unclear, sponsor); CMake (other, unclear); Next.js (framework, core); Vercel (cloud, supporting)
- **Sponsor APIs:**  | fit: Prize is for modern C++ from Safe Software; the page lists C++ and CMake and a second repo, but the writeup does not describe the C++ work.
- **Repo:** public, commits 9 (before/in/after event: 0/9/0), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 0, writeup short, impact claims False
- **Notes:** Two repos listed (GANPI and GANPI-LOCUS); built-with includes C++ and CMake alongside Next.js, consistent with the modern-C++ prize, though the writeup describes only the web app.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; team_size; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/ganpi) | [GitHub](https://github.com/chdrPE/GANPI)

### GemiDice  (StormHacks 2025)

- **Prizes:** [MLH] Best Use of .Tech [unknown]  (tier: sponsor_winner)
- **Pitch:** Dungeons-and-Dragons-style text adventure where Gemini narrates the story and dice rolls decide outcomes.
- **Problem / user:** Players want a freeform, replayable adventure game without needing a human dungeon master. / casual tabletop and text-game players
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat; generative_media
- **Stack:** langs Python; JavaScript; frontend HTML5; CSS; backend Flask; db ; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core, sponsor); ElevenLabs (ai_model, unclear, sponsor); .tech domain (other, supporting, sponsor); Flask (framework, core)
- **Sponsor APIs:** Gemini; .Tech Domains; ElevenLabs | fit: Won Best Use of .Tech and hosts its site at a gemidice.tech address, alongside Gemini-driven storytelling.
- **Repo:** public, commits 31 (before/in/after event: 0/27/4), README solid
- **Demo/writeup:** video False, live not_checked, screenshots 13, writeup medium, impact claims False
- **Notes:** Gemini is prompted with a story setup and mood/layout changes; ElevenLabs listed; the team of first-timers says it ran a .tech domain; links page is a hub-style site.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; demo_video_url
- **Links:** [Devpost](https://devpost.com/software/anything-pxw2f5) | [GitHub](https://github.com/roilee1101/stormhacks2025)

### GuardianEye  (StormHacks 2025)

- **Prizes:** BluePrint Social Good Track [unknown]  (tier: sponsor_winner)
- **Pitch:** A dashboard that analyzes live camera feeds with computer vision to detect falls, smoke or inactivity for elderly people and texts caregivers.
- **Problem / user:** Falls are a leading cause of injury deaths among seniors and help often arrives too late. / Family caregivers and elder-care staff
- **Domain / idea type:** health_wellness + safety_security / social_good
- **Platforms / hardware / AI:** web / False / vision; agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; Python; frontend React; CSS; backend FastAPI; db ; hosting 
- **Tech/APIs:** YOLOv8 (ai_model, core); MediaPipe (framework, supporting); OpenCV (framework, supporting); Gemini (ai_model, supporting); Strands Agents (framework, supporting); Model Context Protocol (framework, supporting); Twilio (telecom, core)
- **Sponsor APIs:**  | fit: Social good track: elderly fall and hazard monitoring with real-time caregiver alerts.
- **Repo:** public, commits 85 (before/in/after event: 0/82/3), README solid
- **Demo/writeup:** video False, live none, screenshots 3, writeup long, impact claims True (Cites that falls are the top cause of unintentional injury deaths in the elderly and one in four seniors falls yearly.)
- **Notes:** Pairs YOLOv8, OpenCV and MediaPipe detection with Gemini agent analysis through Strands Agents and MCP, and Twilio SMS alerts.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/guardianeye) | [GitHub](https://github.com/ryanraen/GuardianEye)

### Hello World Rube Goldberg (The StormHacks Experience)  (StormHacks 2025)

- **Prizes:** CSSS Rube Goldberg Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** A joke Rube Goldberg machine of cans and electronics that needlessly elaborately ends up printing hello world.
- **Problem / user:** None stated; a playful challenge entry to overcomplicate printing hello world. / Hackathon participants and organizers (humor)
- **Domain / idea type:** entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / False
- **Stack:** langs C++; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Arduino (hardware_part, core)
- **Sponsor APIs:**  | fit: Built as an entry to the CSSS Rube Goldberg Challenge using Arduino hardware.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Physical chain-reaction build using Arduino, tape and cans; page links a Google Drive file, no repo listed.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; n_screenshots; demo_video_url
- **Links:** [Devpost](https://devpost.com/software/hello-world-rube-goldberg-the-stormhacks-experience)

### Hooray-For-Huawei  (StormHacks 2025)

- **Prizes:** Huawei Custom Challenge #2: Automatic Decision for Re-computation [unknown]  (tier: sponsor_winner)
- **Pitch:** A C++ heuristic algorithm that returns a near-optimal ordering of nodes to minimize time for Huawei's re-computation challenge.
- **Problem / user:** Decide an efficient order of computation nodes to cut total time, per Huawei's challenge. / Huawei challenge judges
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** cli / False / False
- **Stack:** langs C++; frontend ; backend ; db ; hosting 
- **Tech/APIs:** C++ (framework, core)
- **Sponsor APIs:**  | fit: Direct solution to Huawei challenge 2 on automatic decisions for re-computation.
- **Repo:** public, commits 36 (before/in/after event: 0/36/0), README solid
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Very brief writeup; algorithmic entry in C++ with no UI, and the stated challenge was long runtime to reach a valid solution.
- **Team size:** 4 | **Confidence:** medium | unverified: platforms; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/hooray-for-huawei) | [GitHub](https://github.com/Arnice123/Stormhacks-Hooray-For-Huawei)

### IntervU  (StormHacks 2025)

- **Prizes:** Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** AI mock interview app: upload resume and job post, get tailored behavioral and coding questions, hints, runnable code tests, feedback and a final score.
- **Problem / user:** Mock interview practice is costly or limited, and friends are not always available. / students applying for software co-op and engineering jobs
- **Domain / idea type:** education + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice
- **Stack:** langs Go; TypeScript; frontend Next.js; React; backend Go; db MongoDB; hosting Render; Vercel
- **Tech/APIs:** Google Gemini API (ai_model, core); Go-Piston (other, core); MongoDB (database, core); ElevenLabs (ai_model, supporting); OpenAI (ai_model, token)
- **Sponsor APIs:** 
- **Repo:** public, commits 84 (before/in/after event: 0/84/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 5, writeup long, impact claims False
- **Notes:** Go backend with Piston for sandboxed Python/JS execution against test cases; separate frontend and backend repos (queue records frontend only); ElevenLabs voice mentioned in built-with.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/intervu-852wre) | [GitHub](https://github.com/PaulP1406/IntervU_frontend)

### LockedIn  (StormHacks 2025)

- **Prizes:** Charles Chang Institute of Entrepreneurship Prize Track [unknown]  (tier: sponsor_winner)
- **Pitch:** An Electron desktop focus app where Gemini checks screenshots against your stated goal and the webcam flags looking away, then alerts you.
- **Problem / user:** Timers and to-do lists do not know when attention has drifted, which is especially hard for people with ADHD. / Students and people with attention difficulties
- **Domain / idea type:** productivity_workplace + mental_health / automation_or_agent
- **Platforms / hardware / AI:** desktop / False / vision; llm_chat
- **Stack:** langs JavaScript; TypeScript; frontend Electron; React; Vite; backend Streamlit; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, core); Electron (framework, core); Streamlit (framework, unclear)
- **Sponsor APIs:**  | fit: Entrepreneurship track: positioned as a consumer focus product with a dashboard and session summaries.
- **Repo:** public, commits 89 (before/in/after event: 0/89/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Combines periodic desktop screenshots sent to Gemini with webcam gaze tracking in an Electron app, plus a session analytics dashboard.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/lockedin-09v51s) | [GitHub](https://github.com/yood2/lockedin)

### M.I.R.A  (StormHacks 2025)

- **Prizes:** [MLH] Best Use of Gemini API [unknown]  (tier: sponsor_winner)
- **Pitch:** Local-first desktop work companion that logs app usage into a semantic timeline and offers a voice and text AI assistant with screen context.
- **Problem / user:** Time-blocking tools do not reflect reality, leaving people unclear what they actually accomplished during screen time. / knowledge workers
- **Domain / idea type:** productivity_workplace + ai_agents_infra / twist_on_known_app
- **Platforms / hardware / AI:** desktop / False / speech_or_voice; llm_chat; vision
- **Stack:** langs C++; Python; TypeScript; frontend React; Electron; shadcn/ui; backend Django; db ; hosting 
- **Tech/APIs:** Gemini API (ai_model, core, sponsor); ElevenLabs (ai_model, core, sponsor); Electron (framework, core); React (framework, supporting); Django (framework, supporting); C++ logging agent (other, core)
- **Sponsor APIs:** Gemini API; ElevenLabs | fit: Uses Gemini (listed in built-with) for screen-context reasoning in its companion, plus ElevenLabs for speech mode; the page does not detail the Gemini calls.
- **Repo:** public, commits 54 (before/in/after event: 1/47/6), README solid
- **Demo/writeup:** video False, live none, screenshots 5, writeup long, impact claims False
- **Notes:** C++ native agent logs window and idle data every second, Python captures screenshots, Electron dashboard, global shortcut toggles ElevenLabs speech mode; data stays local.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/m-i-r-a) | [GitHub](https://github.com/irvincardoza/stormhacks2025)

### Mapd  (StormHacks 2025)

- **Prizes:** Winner Finalists; Winner United Nations Sustainable Development Goals Enactus Challenge; Winner Best Design [unknown]; Finalists [unknown]; Best Design [unknown]; United Nations Sustainable Development Goals Enactus Challenge [unknown]  (tier: track_winner)
- **Pitch:** A map platform that pulls public permit, zoning and transit data for a development address and summarizes its likely community impact in plain language.
- **Problem / user:** Residents cannot easily see how a nearby construction project will affect traffic, noise and amenities because open data is fragmented. / Residents and neighbourhood groups near urban developments
- **Domain / idea type:** civic_legal + housing_real_estate / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; JavaScript; frontend Vite; React; Tailwind CSS; Mapbox GL; backend FastAPI; Cloudflare Workers; db MongoDB; hosting Vercel; DigitalOcean; Docker
- **Tech/APIs:** OpenAI (ai_model, core); Mapbox GL (maps_geo, core); MongoDB (database, core); DigitalOcean (cloud, supporting); Cloudflare Workers (cloud, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:**  | fit: UN SDG track: framed as an urban-development transparency tool for communities; Best Design cited for minimal map UI is not stated on the page.
- **Repo:** public, commits 117 (before/in/after event: 0/105/12), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 7, writeup long, impact claims False
- **Notes:** Uses a geocoding and fuzzy-match reconciliation layer plus cached, batched OpenAI summaries over cleaned records; deployed across Vercel, DigitalOcean and Cloudflare Workers.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; tech_items.is_sponsor; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/mapd-urban-development-intelligence) | [GitHub](https://github.com/LMSAIH/StormHacks2025)

### Music March  (StormHacks 2025)

- **Prizes:** Huawei Custom Challenge #1: Interactive Landscape Graphics [unknown]  (tier: sponsor_winner)
- **Pitch:** A real-time 3D audio visualizer where bass, mid and treble drive the height of ray-marched fractal terrain you can fly through.
- **Problem / user:** Extends Huawei's ray marching challenge into an interactive music visualization, after speeding the base renderer up. / Electronic music fans and DJs
- **Domain / idea type:** creative_media + entertainment_games / creative_tool
- **Platforms / hardware / AI:** desktop / False / False
- **Stack:** langs C++; GLSL; frontend SDL3; backend ; db ; hosting 
- **Tech/APIs:** SDL3 (framework, core); GLSL (framework, core); FFT (other, core)
- **Sponsor APIs:**  | fit: Built on Huawei's challenge 1 ray marching shader, optimized and extended with audio-reactive terrain.
- **Repo:** public, commits 78 (before/in/after event: 0/78/0), README thin
- **Demo/writeup:** video False, live none, screenshots 2, writeup medium, impact claims True (Claims at least 20x frame rate improvement, from 3 fps to 60 fps.)
- **Notes:** SDL3 engine with FFT band splitting feeding a GLSL fragment shader; reports frame rate going from about 3 fps to 60 fps.
- **Team size:** 3 | **Confidence:** high | unverified: team_size
- **Links:** [Devpost](https://devpost.com/software/the-ray-marching-band) | [GitHub](https://github.com/ErykHalicki/ray_marcher)

### Optimized Ray-marching algorithm  (StormHacks 2025)

- **Prizes:** Huawei Custom Challenge #1: Interactive Landscape Graphics [unknown]  (tier: sponsor_winner)
- **Pitch:** A solo GLSL optimization of Huawei's heightfield ray marcher using distance-based detail, Lipschitz-bounded stepping and the Illinois method.
- **Problem / user:** Rendering procedurally generated landscape heightfields by ray marching is slow, especially at grazing angles. / Graphics programmers (Huawei challenge)
- **Domain / idea type:** creative_media + dev_tools / creative_tool
- **Platforms / hardware / AI:** desktop / False / False
- **Stack:** langs GLSL; frontend ; backend ; db ; hosting 
- **Tech/APIs:** GLSL (framework, core)
- **Sponsor APIs:**  | fit: Improves Huawei's supplied basic ray marching algorithm for the landscape graphics challenge.
- **Repo:** public, commits 9 (before/in/after event: 0/8/1), README solid
- **Demo/writeup:** video False, live none, screenshots 0, writeup long, impact claims True (States a 37.8 percent reduction in ray marching step count.)
- **Notes:** Solo entry; claims a 37.8 percent cut in step count via K-Lipschitz bound and Illinois root-finding window skipping.
- **Team size:** 1 | **Confidence:** high | unverified: n_screenshots; platforms
- **Links:** [Devpost](https://devpost.com/software/optimized-procedural-heightfield-rendering) | [GitHub](https://github.com/markharmon868/SphericalTrace)

### Punchly  (StormHacks 2025)

- **Prizes:** ColorStack Most Portable Project [unknown]  (tier: sponsor_winner)
- **Pitch:** NFC-based digital loyalty punch card: customers tap a tag at the counter to log a visit and earn a stamp, with a merchant web dashboard.
- **Problem / user:** Paper punch cards get lost and QR-code scanning is slow and has security drawbacks for small businesses. / small shops and their customers
- **Domain / idea type:** retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross; web / True / False
- **Stack:** langs Python; JavaScript; frontend React Native; Expo; backend Flask; db SQLite; Supabase; hosting 
- **Tech/APIs:** NFC tags (hardware_part, core); React Native / Expo (framework, core); Flask (framework, core); SQLite (database, core); Supabase (database, token)
- **Sponsor APIs:**  | fit: Won the ColorStack Most Portable Project prize, matching a cross-platform Expo app plus web dashboard built around a portable NFC tag.
- **Repo:** public, commits 35 (before/in/after event: 0/34/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 19, writeup medium, impact claims False
- **Notes:** Expo React Native app with NFC deep links, Flask API on SQLite after Supabase RLS and auth issues slowed the team; a web dashboard was also finished.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/punchly) | [GitHub](https://github.com/Aneel-Badesha/stormhacks2025)

### Qount  (StormHacks 2025)

- **Prizes:** Best Solo Project [unknown]  (tier: track_winner)
- **Pitch:** iOS counting game that flashes a random number of cubes briefly, then asks the player to guess how many there were.
- **Problem / user:** Solo builder wanted to recreate a brain-training mini-game from Nintendo Switch footage. / casual mobile gamers
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** mobile_ios / False / False
- **Stack:** langs Swift; frontend SwiftUI; backend ; db ; hosting 
- **Tech/APIs:** SwiftUI (framework, core); AVFoundation (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 24 (before/in/after event: 0/24/0), README none
- **Demo/writeup:** video True, live none, screenshots 7, writeup short, impact claims False
- **Notes:** Solo project in Swift and SwiftUI; hit an App Store-style limit when overriding volume buttons; works mainly on iPhone, less reliably on iPad.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/qount) | [GitHub](https://github.com/nevadoj/boxgame)

### Racoon Works Hua Wei CC 2  (StormHacks 2025)

- **Prizes:** Huawei Custom Challenge #2: Automatic Decision for Re-computation [unknown]  (tier: sponsor_winner)
- **Pitch:** A C++ scheduler for AI model computation that compares naive, greedy, heuristic, beam search and branch-and-bound strategies with recomputation to limit memory peak.
- **Problem / user:** Scheduling AI model computation under memory limits needs decisions on when to recompute intermediate results. / Huawei challenge judges / AI compiler engineers
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** cli / False / False
- **Stack:** langs C++; frontend ; backend ; db ; hosting 
- **Tech/APIs:** C++ (framework, core)
- **Sponsor APIs:**  | fit: Direct solution to Huawei challenge 2 using multiple scheduling algorithms with memory-aware recomputation.
- **Repo:** public, commits 26 (before/in/after event: 0/26/0), README thin
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Research-driven entry implementing several recent recomputation papers; the team notes memory peak hit the ceiling while chasing optimal time.
- **Team size:** 4 | **Confidence:** medium | unverified: platforms; n_screenshots; team_size
- **Links:** [Devpost](https://devpost.com/software/racoon-works-hua-wei-cc-2) | [GitHub](https://github.com/notwinston/Racoon_Works_Storm_Hacks2025)

### Rehabit  (StormHacks 2025)

- **Prizes:** Most Likely to Become a Startup [unknown]  (tier: track_winner)
- **Pitch:** Browser-based home rehab coach that uses a webcam and pose tracking to score symmetry and range of motion, then writes a Gemini report.
- **Problem / user:** Post-stroke or injury rehab is hard to access and hard to measure objectively at home. / rehab patients and clinicians
- **Domain / idea type:** health_wellness / new_category
- **Platforms / hardware / AI:** web / False / vision; llm_chat; predictive_ml
- **Stack:** langs Python; JavaScript; frontend HTML; CSS; JavaScript; backend Flask; Flask-SocketIO; db ; hosting 
- **Tech/APIs:** MediaPipe Pose (ai_model, core); OpenCV (framework, core); Gemini API (ai_model, core); ElevenLabs API (ai_model, unclear); Flask-SocketIO (framework, supporting); NumPy (framework, supporting)
- **Sponsor APIs:**  | fit: Won the startup-potential award; the page cites a planned clinic pilot and reimbursement alignment but no quantified market figures.
- **Repo:** public, commits 30 (before/in/after event: 0/30/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** MediaPipe Pose and OpenCV compute joint angles with smoothing; Flask-SocketIO streams results; plans a clinic pilot, FHIR export and HIPAA/PIPEDA alignment.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; ai_types
- **Links:** [Devpost](https://devpost.com/software/rehabit-c093se) | [GitHub](https://github.com/KR13H/Rehabit.git)

### SFU Grad Map  (StormHacks 2025)

- **Prizes:** Best Use of SFU Courses API [unknown]  (tier: sponsor_winner)
- **Pitch:** A web app where searching an SFU course shows an interactive graph of its prerequisites and equivalent courses, extracted with Gemini.
- **Problem / user:** Finding SFU course prerequisites means clicking through many outline pages on an unintuitive official system. / SFU students planning their degree
- **Domain / idea type:** education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs JavaScript; frontend Next.js; D3.js; shadcn; Aceternity; backend ; db ; hosting Vercel
- **Tech/APIs:** SFU Courses API (data_source, core, sponsor); Gemini Flash (ai_model, core); D3.js (framework, core); Next.js (framework, supporting)
- **Sponsor APIs:** SFU Courses API | fit: Uses SFU course data as the source, with Gemini parsing prerequisites into a visual graph.
- **Repo:** public, commits 63 (before/in/after event: 0/55/8), README solid
- **Demo/writeup:** video False, live not_checked, screenshots 3, writeup long, impact claims False
- **Notes:** Gemini turns free-text prerequisite descriptions into JSON, rendered with D3; team tried a manual parser but found the text too inconsistent.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; SFU Courses API is_sponsor (inferred from prize name)
- **Links:** [Devpost](https://devpost.com/software/sfu-grad-map) | [GitHub](https://github.com/alexchen817/stormhacks2025-sfu-course-map)

### SurvivalChess  (StormHacks 2025)

- **Prizes:** Finalists [unknown]; Best Game [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Timed puzzle game where you move chess-style pieces, including custom Stag and Trident pieces, off tiles marked for destruction each round.
- **Problem / user:** Not a problem-driven project; a game concept built from a teammate's chess arrangement puzzle. / casual puzzle game players
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; frontend PixiJS; Vite; backend Node.js; db ; hosting Vercel
- **Tech/APIs:** PixiJS (framework, core); Vite (framework, supporting); Node.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 24 (before/in/after event: 0/16/8), README thin
- **Demo/writeup:** video False, live not_checked, screenshots 2, writeup medium, impact claims False
- **Notes:** Page lists StormHacks 2025 (queue entry placed under edition 2025). Also won Best Game. Browser game with endless rounds and two invented pieces.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/survivalchess) | [GitHub](https://github.com/jpg157/SurvivalChess_Stormhacks_2025)

### Track2Give  (StormHacks 2025)

- **Prizes:** Best Beginner [unknown]; Most Likely to Become a Startup [unknown]; United Nations Sustainable Development Goals Enactus Challenge [unknown]  (tier: track_winner)
- **Pitch:** A web app for tracking pantry items and expiry dates, alerting users and suggesting donation of food about to expire.
- **Problem / user:** Households forget what food they have until it spoils, adding to food waste. / Households wanting to cut food waste
- **Domain / idea type:** sustainability_climate + food_nutrition / social_good
- **Platforms / hardware / AI:** web / False / None
- **Stack:** langs JavaScript; frontend HTML; CSS; EJS; backend Node.js; Express.js; Passport.js; db MongoDB; Mongoose; hosting Render
- **Tech/APIs:** MongoDB (database, core); Passport.js (auth, supporting); Gemini (ai_model, unclear); Cloudinary (other, unclear)
- **Sponsor APIs:**  | fit: UN SDG track: food-waste reduction and donation suggestions.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 12, writeup long, impact claims False
- **Notes:** Server-rendered EJS app with Passport auth; receipt scanning and AI expiry prediction are listed as future work, though Gemini and Cloudinary appear in the Built With list.
- **Team size:** 4 | **Confidence:** high | unverified: ai_used; n_screenshots; team_size; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/track2give) | [GitHub](https://github.com/abdullahmohammed1234/StormHacks2025)


## StormHacks 2026

### Apex FSD  (StormHacks 2026)

- **Prizes:** SSSS - Seb's Software Systems Python Track [unknown]  (tier: sponsor_winner)
- **Pitch:** A PilotNet-style CNN drives Forza from screen pixels and speed, physically turning a real force-feedback steering wheel with human takeover.
- **Problem / user:** Most AI driving demos stop at a function call; team wanted end-to-end pixels-to-steering that moves a real wheel. / racing-sim and ML hobbyists
- **Domain / idea type:** mobility_transport + ai_agents_infra / hardware_gadget
- **Platforms / hardware / AI:** desktop; hardware / True / vision; predictive_ml
- **Stack:** langs Python; frontend ; backend PyTorch; OpenCV; PySDL2; db ; hosting Google Colab
- **Tech/APIs:** PyTorch (framework, core); PilotNet-style CNN (ai_model, core); Forza Data Out telemetry (data_source, core); vJoy (other, core); HidHide (other, core); Thrustmaster TMX wheel (hardware_part, core); DXcam (other, supporting); OpenCV (framework, supporting)
- **Sponsor APIs:**  | fit: Python-based ML and control pipeline (PyTorch, OpenCV, PySDL2) fits a Python systems track.
- **Repo:** public, commits 186 (before/in/after event: 0/186/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Two PCs over Ethernet; vJoy plus HidHide to feed a virtual wheel; DAgger corrections loop; measured 66 ms screen lag versus telemetry; about 3 hours of training data on one map.
- **Team size:** 4 | **Confidence:** high | unverified: tech_items.is_sponsor; demo video is a drive.google.com link; exact URL not captured; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/apex-fsd) | [GitHub](https://github.com/iancdev/stormhacks)

### Chess without Borders  (StormHacks 2026)

- **Prizes:** Huawei Custom Challenge #1 - Beyond Euclid [unknown]  (tier: sponsor_winner)
- **Pitch:** A multiplayer 3D chess game where players warp the board between Euclidean and hyperbolic geometry so piece moves follow geodesics.
- **Problem / user:** Non-Euclidean geometry is hard to grasp abstractly; a familiar game lets players experience curved space. / Chess players and math-curious gamers
- **Domain / idea type:** entertainment_games + education / entertainment_or_game
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; frontend HTML; CSS; Three.js; Vite; backend Node.js; ws WebSockets; db ; hosting 
- **Tech/APIs:** Three.js (framework, core); WebSockets (ws) (framework, core); Vite (framework, supporting)
- **Sponsor APIs:**  | fit: Answers Huawei challenge Beyond Euclid with a game built on non-Euclidean board geometry.
- **Repo:** public, commits 15 (before/in/after event: 0/15/0), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 3, writeup long, impact claims False
- **Notes:** Geometry is a core mechanic, with a shared TypeScript engine for browser and server, Three.js rendering and WebSocket multiplayer; Google Drive link also listed.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/chess-2-watsne) | [GitHub](https://github.com/geoff-jiang/Chess2)

### Common Ground  (StormHacks 2026)

- **Prizes:** SFU Satellite - ALEASAT - Earth Observation Track [unknown]  (tier: sponsor_winner)
- **Pitch:** 3D park design tool built on real Vancouver lidar and city data where residents design, vote and comment, and planners get heatmaps and exports.
- **Problem / user:** Park planning feedback comes from whoever attends meetings; planners lack precise, broad resident input. / city green-space planners and residents
- **Domain / idea type:** civic_legal + sustainability_climate / new_category
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs TypeScript; frontend React; React Three Fiber; three.js; backend Hono; db Postgres; Drizzle; pglite; hosting 
- **Tech/APIs:** Gemini (ai_model, supporting); NRCan HRDEM lidar (data_source, core); Vancouver Open Data (data_source, core); TransLink GTFS (data_source, supporting); OpenStreetMap (data_source, supporting); React Three Fiber (framework, core); Hono (framework, supporting); Postgres (database, supporting)
- **Sponsor APIs:**  | fit: Uses earth-observation style elevation (lidar) and municipal geodata as its base layer; page does not mention the satellite sponsor.
- **Repo:** public, commits 2 (before/in/after event: 0/2/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 9, writeup medium, impact claims False
- **Notes:** Demo site uses 1 m NRCan lidar terrain, city tree inventory, TransLink GTFS and OSM; Gemini turns text into layouts; offline fallback; budget and slope rules update live.
- **Team size:** 1 | **Confidence:** high | unverified: tech_items.is_sponsor; sponsor_fit_note; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/project-thing-cg94vo) | [GitHub](https://github.com/zach1502/commonground)

### CrimePath  (StormHacks 2026)

- **Prizes:** [MLH] Best Use of Gemini API [unknown]  (tier: sponsor_winner)
- **Pitch:** AI investigation workspace that turns unstructured evidence into a structured chronological timeline for investigators.
- **Problem / user:** Investigators struggle to organize and make sense of scattered evidence in time order. / law enforcement investigators
- **Domain / idea type:** civic_legal + safety_security / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; JavaScript; frontend React; Tailwind CSS; backend Node.js; Express; db PostgreSQL; TigerData; hosting 
- **Tech/APIs:** Gemini API (ai_model, core, sponsor); TigerData (PostgreSQL) (database, supporting); .tech domain (other, supporting, sponsor); React (framework, supporting)
- **Sponsor APIs:** Gemini API; .Tech Domains | fit: Won Best Use of Gemini API; Gemini turns raw evidence into structured timeline data.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 22, writeup long, impact claims False
- **Notes:** Idea came from a teammate's law-enforcement experience; Gemini converts evidence into structured data stored in PostgreSQL via TigerData; writeup flags consistency of AI output as the main challenge.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/crimepath)

### Cubic  (StormHacks 2026)

- **Prizes:** IATSU - Best Design Track [unknown]  (tier: sponsor_winner)
- **Pitch:** Two-player co-op puzzle game on a shared cube: one player outside, one trapped inside in a mirrored dark world, talking to solve six faces.
- **Problem / user:** Wanted a co-op game where communication between friends is the whole point; solo players get an AI partner. / friends playing co-op browser games
- **Domain / idea type:** entertainment_games + social_community / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice
- **Stack:** langs TypeScript; frontend Phaser 4; Vite; backend Node.js; Socket.io; db ; hosting Vercel; Render
- **Tech/APIs:** Phaser (framework, core); Socket.io (framework, core); WebRTC (other, core); Gemini (ai_model, supporting); ElevenLabs (ai_model, supporting); Vercel (cloud, supporting); Render (cloud, supporting)
- **Sponsor APIs:**  | fit: Prize is a design track; page does not describe design process, only pixel-art UI and cross-device input.
- **Repo:** public, commits 281 (before/in/after event: 0/279/2), README detailed
- **Demo/writeup:** video None, live not_checked, screenshots 8, writeup medium, impact claims False
- **Notes:** WebRTC proximity voice chat that gets quieter with distance on the cube; Gemini plus ElevenLabs AI partner for solo play; pixel-art Phaser 4 client with desktop, gamepad and touch.
- **Team size:** 4 | **Confidence:** high | unverified: tech_items.is_sponsor; sponsor_fit_note; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/cubic-wu2s5i) | [GitHub](https://github.com/ltanafranca1004/Cubic)

### Deceipt  (StormHacks 2026)

- **Prizes:** Enactus SFU - United Nations Sustainability Development Goals (UNSDG) Track [unknown]  (tier: sponsor_winner)
- **Pitch:** A paperless-receipt site that opens with an arcade game about receipt waste, then shows an interactive demo of searchable digital receipts and warranty tracking.
- **Problem / user:** Paper receipts are mostly thrown away, wasting resources, and are lost when needed for returns or warranties. / Shoppers and consumers
- **Domain / idea type:** sustainability_climate + retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; frontend React; Vite; Figma Make; backend ; db ; hosting GitHub Pages; Cloudflare DNS
- **Tech/APIs:** Figma Make (other, core); GitHub Pages (cloud, supporting); Cloudflare (cloud, supporting)
- **Sponsor APIs:**  | fit: UNSDG track: paperless receipts framed around tree and water savings with sourced environmental figures.
- **Repo:** public, commits 44 (before/in/after event: 0/44/0), README none
- **Demo/writeup:** video False, live not_checked, screenshots 3, writeup long, impact claims True (Cites 300 billion receipts yearly and about 3.3 million US trees lost per year.)
- **Notes:** Static front-end only, made with Figma Make; a canvas mini-game personalizes the paper-waste reveal; team fixed a mobile rendering bug on demo morning.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/deceipt) | [GitHub](https://github.com/parsa-rawr/deceipt)

### Doggin' Around  (StormHacks 2026)

- **Prizes:** Huawei Custom Challenge #2 - Fetching Reality [unknown]  (tier: sponsor_winner)
- **Pitch:** Upload a comic page, step into a panel as a 3D world with a rigged dog companion, and the later panels redraw with a new ending.
- **Problem / user:** Readers cannot change a comic's ending; the team also had to turn a single dog photo into an animatable 3D character. / comic readers and game players
- **Domain / idea type:** creative_media + entertainment_games / creative_tool
- **Platforms / hardware / AI:** web / False / generative_media; vision; speech_or_voice; other
- **Stack:** langs TypeScript; Python; frontend Three.js; Spark; Vite; backend PyTorch; PyTorch3D; gsplat; db ; hosting RunPod
- **Tech/APIs:** AniGen (ai_model, core); TripoSplat (ai_model, core); TRELLIS (ai_model, supporting); BITE / D-SMAL (ai_model, core); World Labs Marble (ai_model, core); Gemini (ai_model, core); ElevenLabs (ai_model, supporting); Rapier (framework, supporting); Spark (framework, core); Three.js (framework, core); RunPod (cloud, supporting); Blender (other, supporting)
- **Sponsor APIs:**  | fit: Used the two dog photographs supplied by Huawei as the basis for rigged, animated 3D dog characters.
- **Repo:** public, commits 11 (before/in/after event: 11/0/0), README detailed
- **Demo/writeup:** video None, live not_checked, screenshots 7, writeup long, impact claims False
- **Notes:** Two separate image-to-3D dog pipelines (AniGen rig plus Gaussian splats; SMAL-pets-style fit); 29 dog actions; voice commands; panel-to-world via World Labs Marble; 60 FPS claimed.
- **Team size:** 4 | **Confidence:** high | unverified: github_url (queue value points to the upstream AniGen research repo, not the team's own code); tech_items.is_sponsor; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/doggin-around) | [GitHub](https://github.com/VAST-AI-Research/AniGen)

### DoubleTake  (StormHacks 2026)

- **Prizes:** TiDB x AI Open Build [unknown]  (tier: sponsor_winner)
- **Pitch:** Dating platform where two best friends pair up as a duo and match with another duo, using TiDB vector search for vibe-based discovery.
- **Problem / user:** Solo dating apps feel like interviews and are intimidating, so the team wanted a safer, more social, lower-pressure way to meet people. / young adults dating with a friend
- **Domain / idea type:** social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / rag_or_search; recommendation
- **Stack:** langs Java; JavaScript; frontend React; Tailwind; Vite; backend Spring Boot; db TiDB; Supabase; hosting Render
- **Tech/APIs:** TiDB Cloud (vector search) (database, core, sponsor); Spring Boot (framework, core); React (framework, core); Tailwind (framework, supporting); Supabase (database, unclear); Claude Code (other, supporting); Render (cloud, supporting)
- **Sponsor APIs:** TiDB | fit: Stores app data in cloud TiDB and runs vector search over AI embeddings of plain-English descriptions for semantic vibe matching.
- **Repo:** public, commits 86 (before/in/after event: 0/84/2), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 9, writeup long, impact claims False
- **Notes:** Java Spring Boot backend on TiDB with an embedding service that turns plain-text vibe descriptions into vector queries; React frontend uses a mock API toggle; Claude Code used for ideation and debugging.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/doubletake-pnxuv8) | [GitHub](https://github.com/JDeni1/DoubleTake)

### Etika  (StormHacks 2026)

- **Prizes:** Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Compliance navigator for new Vancouver sole proprietors: three agents check confirmed facts against cited official sources and produce a Now/Next/Later plan.
- **Problem / user:** Business compliance rules are scattered across government sites and thresholds shift, so owners cannot tell what applies to them. / new sole proprietors in Vancouver
- **Domain / idea type:** civic_legal + fintech_finance / automation_or_agent
- **Platforms / hardware / AI:** web / False / rag_or_search; agent_or_tool_use; llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; backend FastAPI; Pydantic; db TiDB Cloud; hosting 
- **Tech/APIs:** Gemini Flash (ai_model, core, sponsor); gemini-embedding-001 (ai_model, core, sponsor); TiDB Cloud (database, core, sponsor); FastAPI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 103 (before/in/after event: 0/94/9), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** Deterministic rules engine decides status and score; Gemini only explains; hand-built RAG over official BC and CRA sources with citation validation; cut Gemini calls to 3 per assessment. Queue had no GitHub, page links one.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/etika) | [GitHub](https://github.com/gaida123/etika)

### FloodBeacon  (StormHacks 2026)

- **Prizes:** [MLH] Best Use of Tiger Data [unknown]  (tier: sponsor_winner)
- **Pitch:** Responder dashboard combining before/after satellite bridge-damage comparisons with an SMS intake that Gemini turns into structured flood help requests.
- **Problem / user:** During floods, satellite imagery and victims' messages sit in separate places, making it hard for responders to assess who needs help and which access routes are cut. / disaster responders
- **Domain / idea type:** safety_security + civic_legal / data_or_analytics
- **Platforms / hardware / AI:** web; bot_or_chat / False / llm_chat; vision
- **Stack:** langs Python; TypeScript; frontend React; Vite; backend FastAPI; Pydantic; db PostgreSQL; hosting 
- **Tech/APIs:** Twilio SMS (telecom, core); Gemini (ai_model, core); PostgreSQL (database, core); Rasterio (framework, core); FastAPI (framework, core); React (framework, supporting)
- **Sponsor APIs:**  | fit: Tiger Data is Postgres-based; the page lists PostgreSQL for observation metadata and incident records but never names Tiger Data, so the fit is not shown on the page.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Twilio SMS webhook with signature validation and background Gemini extraction, audit history, and Rasterio-aligned Maxar, Vantor and Planet imagery for Germany, Libya and Nepal; AI findings kept separate from agency data.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; n_screenshots; sponsor_fit_note; sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/floodbeacon)

### HyperSpace  (StormHacks 2026)

- **Prizes:** TiDB x AI Open Build [unknown]  (tier: sponsor_winner)
- **Pitch:** Explorable hyperbolic map of 2,475 Wikipedia AI topics, with TiDB vector and full-text search and Gemini-assisted exploration.
- **Problem / user:** Large knowledge collections are hard to explore; lists hide connections and mind maps become tangled hairballs. / learners and researchers exploring a topic area
- **Domain / idea type:** education + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / rag_or_search; llm_chat
- **Stack:** langs TypeScript; JavaScript; frontend Next.js; React; Tailwind CSS; d3-hypertree; backend Node.js; db TiDB Cloud; MySQL; hosting 
- **Tech/APIs:** TiDB Cloud (vector + full-text search) (database, core, sponsor); Gemini API (ai_model, supporting, sponsor); d3-hypertree (framework, core); Wikipedia/MediaWiki API (data_source, core); .tech domain (other, supporting, sponsor)
- **Sponsor APIs:** TiDB Cloud; Gemini API; .Tech Domains | fit: Won TiDB x AI Open Build; TiDB Cloud stores the topic graph and serves vector and full-text search over it.
- **Repo:** public, commits 34 (before/in/after event: 0/34/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Crawls Wikipedia's category graph from the AI category and renders it on a Poincare disk with d3-hypertree; side-by-side comparison of search modes; one Devpost screenshot.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/hyperspace) | [GitHub](https://github.com/nav175/HyperSpace)

### Ink Habitat  (StormHacks 2026)

- **Prizes:** TiDB x AI Open Build [unknown]  (tier: sponsor_winner)
- **Pitch:** Creature-farm game where players draw their own creatures, name them, give them speech and behaviors, and battle.
- **Problem / user:** Farm games rarely let players create their own creatures, so the authors built one that does. / casual game players
- **Domain / idea type:** entertainment_games + creative_media / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; generative_media
- **Stack:** langs Python; frontend ; backend Python; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, core, sponsor); ElevenLabs (ai_model, core, sponsor)
- **Sponsor APIs:** Gemini; ElevenLabs | fit: Won TiDB x AI Open Build, but the page's tech list shows only Gemini, ElevenLabs and Python and does not mention TiDB.
- **Repo:** public, commits 36 (before/in/after event: 0/36/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 25, writeup long, impact claims False
- **Notes:** Two first-time game makers; players draw creatures and Gemini plus ElevenLabs give them speech; battle mechanics were the hardest design problem; 25 screenshots.
- **Team size:** 2 | **Confidence:** medium | unverified: ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/ink-habitat) | [GitHub](https://github.com/anny282/Ink-Habitat)

### Onus.  (StormHacks 2026)

- **Prizes:** [MLH] Best Use of ElevenLabs [unknown]  (tier: sponsor_winner)
- **Pitch:** Live map grading all 26 BC public post-secondary sexual violence policies with AI against 17 criteria, alongside anonymous student ratings.
- **Problem / user:** Schools must have sexual violence policies, but nobody publicly checks whether they meet student-advocacy minimum standards or are followed in practice. / BC post-secondary students
- **Domain / idea type:** civic_legal + safety_security / social_good
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; speech_or_voice
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind; shadcn/ui; MapLibre GL; backend Supabase; db PostgreSQL; pgvector; hosting 
- **Tech/APIs:** ElevenLabs STT/TTS (ai_model, core, sponsor); Google Gemini (ai_model, core); Supabase (Postgres, Realtime, Auth, pgvector) (database, core); MapLibre GL JS (maps_geo, core); OSRM (maps_geo, supporting); PDF.js (framework, supporting); Next.js (framework, core)
- **Sponsor APIs:** ElevenLabs | fit: Uses ElevenLabs speech-to-text and text-to-speech, including Farsi and Punjabi, so users can ask about a school's policy by voice.
- **Repo:** public, commits 182 (before/in/after event: 0/182/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 2, writeup long, impact claims True (Covers all 26 BC public institutions graded on 17 criteria; claims most policies guarantee little protection on paper.)
- **Notes:** Every graded point must be a quote verified against the source PDF; includes voice Q&A in many languages answered only from the school's policy, pgvector search and OSRM-precomputed routes to support services.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/onus-hx2fua) | [GitHub](https://github.com/TheRoryQueen/OnusBC)

### Otter Nonsense  (StormHacks 2026)

- **Prizes:** Surge Choice Award [unknown]  (tier: sponsor_winner)
- **Pitch:** Relaxed multiplayer 3D otter game: dive for clams and trinkets, chat, buy hats and unwind by a campfire.
- **Problem / user:** Wanted a chill social game in the spirit of WEBFISHING and Sledding Game. / casual multiplayer gamers
- **Domain / idea type:** entertainment_games + social_community / entertainment_or_game
- **Platforms / hardware / AI:** web / False / None
- **Stack:** langs JavaScript; Python; frontend three.js; backend Python; db ; hosting GitHub Actions
- **Tech/APIs:** three.js (framework, core); Python multiplayer server (framework, core); Blender (other, supporting); GitHub Actions (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 146 (before/in/after event: 0/146/0), README none
- **Demo/writeup:** video None, live not_checked, screenshots 9, writeup medium, impact claims False
- **Notes:** No-account multiplayer, trinket collection and hat shop; GitHub Actions auto-deploy; team notes difficulty managing a fast-changing codebase with AI help.
- **Team size:** 4 | **Confidence:** high | unverified: ai_used; team_size (member list ambiguous, writeup says 4); tech_items.is_sponsor; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/otter-nonsense) | [GitHub](https://github.com/ashermemon/stormhacks)

### Phase Escape  (StormHacks 2026)

- **Prizes:** Huawei Custom Challenge #1 - Beyond Euclid [unknown]  (tier: sponsor_winner)
- **Pitch:** Chase game in a hyperbolic maze where a real tilt controller steers and curved space shifts you between colour layers in a 4D-style world.
- **Problem / user:** Curved-space games treat curvature as visuals; the author wanted holonomy to be the mechanic, felt physically through a hand controller. / players curious about non-Euclidean geometry
- **Domain / idea type:** entertainment_games + education / entertainment_or_game
- **Platforms / hardware / AI:** web; desktop; hardware / True / other
- **Stack:** langs TypeScript; C++; frontend Three.js; Electron; backend ; db ; hosting 
- **Tech/APIs:** Three.js (framework, core); Electron (framework, supporting); ESP32 (hardware_part, core); BNO055 IMU (hardware_part, core); Bluetooth Low Energy (other, core); Claude Code (ai_model, supporting)
- **Sponsor APIs:**  | fit: Built around the Huawei challenge theme of non-Euclidean space: a game on the hyperbolic plane with a 4D rotation view.
- **Repo:** public, commits 25 (before/in/after event: 0/25/0), README detailed
- **Demo/writeup:** video None, live not_checked, screenshots 7, writeup long, impact claims False
- **Notes:** Custom ESP32 + BNO055 wireless controller over BLE; exact hyperboloid geometry; 9 levels; solver and autopilot prove levels beatable; 143 automated tests; built with Claude Code.
- **Team size:** 1 | **Confidence:** high | unverified: ai_types; tech_items.is_sponsor; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/phase-escape) | [GitHub](https://github.com/Dan007b/phase-escape)

### Pixel Cat Arena  (StormHacks 2026)

- **Prizes:** Best Game [unknown]  (tier: track_winner)
- **Pitch:** Browser cat battler where players build and gear a cat, fight PvE and other players, and claim items as Solana devnet tokens.
- **Problem / user:** The author wanted in-game item ownership to be more meaningful than a database row. / casual browser gamers
- **Domain / idea type:** entertainment_games + fintech_finance / entertainment_or_game
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; frontend ; backend FastAPI; db ; hosting 
- **Tech/APIs:** Solana (devnet) (other, core, sponsor); FastAPI (framework, core)
- **Sponsor APIs:** Solana | fit: Won the event-run Best Game category; Solana devnet minting backs the item ownership claim.
- **Repo:** public, commits 26 (before/in/after event: 0/26/0), README solid
- **Demo/writeup:** video True, live none, screenshots 19, writeup medium, impact claims False
- **Notes:** Solo build with a FastAPI backend and a real Solana devnet mint plus wallet-signature claim; the author notes the difficulty of keeping truth split between database and chain.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/pixel-cat-arena) | [GitHub](https://github.com/kirill-stepanishin/pixel-cat-arena)

### PunchCode  (StormHacks 2026)

- **Prizes:** CSSS - SFU CS Legacy Track [unknown]  (tier: sponsor_winner)
- **Pitch:** A web simulator of the IBM 029 card-punch where users punch Fortran programs onto cards, with a tutorial and LeetCode-style levels.
- **Problem / user:** Few people know how programmers coded with punch cards; the project lets them experience it. / Students and history-curious programmers
- **Domain / idea type:** education + entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; Python; JavaScript; frontend Next.js; CSS; backend FastAPI; db ; hosting 
- **Tech/APIs:** Next.js (framework, supporting); FastAPI (framework, core); Fortran (framework, core)
- **Sponsor APIs:**  | fit: Built for the CSSS legacy track by recreating SFU's historical IBM card-punch coding experience.
- **Repo:** public, commits 21 (before/in/after event: 0/21/0), README thin
- **Demo/writeup:** video False, live not_checked, screenshots 4, writeup medium, impact claims False
- **Notes:** Faithful card-punch simulation with sound design; a Python FastAPI backend actually compiles and runs the user's Fortran.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/punchcode) | [GitHub](https://github.com/ImJulien/PunchCode)

### Rapid Triage  (StormHacks 2026)

- **Prizes:** Best Hardware [unknown]  (tier: track_winner)
- **Pitch:** ESP32 wearable that streams patient vitals to a time-series backend, scores triage priority, and guides responders via dashboard and iOS app.
- **Problem / user:** In mass-casualty incidents, patients can deteriorate unseen while too few responders are available to keep reassessing everyone. / emergency responders and incident commanders
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web; mobile_ios / True / False
- **Stack:** langs Python; C++; JavaScript; frontend Next.js; backend Flask; db Tiger Data (PostgreSQL); hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Tiger Data (database, core, sponsor); Flask (framework, core); Next.js (framework, core); BLE RSSI proximity (hardware_part, supporting); Arduino (framework, supporting)
- **Sponsor APIs:** Tiger Data | fit: Entered Best Hardware track with an ESP32 multi-sensor wearable; page also describes Tiger Data as its core time-series store for vitals.
- **Repo:** public, commits 3 (before/in/after event: 0/3/0), README thin
- **Demo/writeup:** video False, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Wearable with heart rate, SpO2, temperature and ECG sends data over a local Wi-Fi network (no internet needed); iOS app uses BLE signal strength to locate the assigned patient; a second firmware repo is listed.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/rapid-triage) | [GitHub](https://github.com/bsbhakti/stormhacks26)

### ReliefPool  (StormHacks 2026)

- **Prizes:** [MLH] Best Use of Solana [unknown]  (tier: sponsor_winner)
- **Pitch:** Solana relief pool that automatically pays NGOs when an ML classifier rates an earthquake's tsunami risk above a threshold.
- **Problem / user:** Disaster relief funds can take days or weeks to arrive, far slower than the disaster itself. / disaster-relief NGOs and donors
- **Domain / idea type:** fintech_finance + sustainability_climate / automation_or_agent
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Rust; Python; TypeScript; frontend Vite; backend Node.js; FastAPI; db ; hosting Solana devnet
- **Tech/APIs:** Solana (Anchor, devnet) (other, core, sponsor); scikit-learn logistic regression (ai_model, core); USGS earthquake feed (data_source, core); NOAA tsunami dataset (data_source, core); Phantom / Solflare wallets (auth, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** Solana | fit: Built an Anchor smart contract on Solana devnet that holds donated funds and releases payouts to NGO wallets when the oracle triggers.
- **Repo:** public, commits 51 (before/in/after event: 0/51/0), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Anchor (Rust) program on devnet triggered by an oracle that reads USGS quakes; logistic regression trained on USGS and NOAA data reports 87% accuracy and 0.97 ROC-AUC; duplicate-payout and fail-safe checks.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/reliefpool) | [GitHub](https://github.com/manandrew-dev/ReliefPool.git)

### ReTrace  (StormHacks 2026)

- **Prizes:** Best Solo [unknown]  (tier: track_winner)
- **Pitch:** Turns existing city traffic cameras into a searchable index of vehicles, using detection, tracking and attribute classification without faces or plates.
- **Problem / user:** Canada lacks modern traffic surveillance search tools; the author wanted vehicle-level retrieval that avoids identifying people. / traffic and public-safety analysts
- **Domain / idea type:** safety_security + mobility_transport / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; rag_or_search; speech_or_voice; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Vite; Framer Motion; backend FastAPI; PyTorch; db ; hosting Cloudflare tunnel; GitHub Pages
- **Tech/APIs:** YOLO (ai_model, core); CLIP (ai_model, core); Whisper (ai_model, supporting); Qwen (ai_model, supporting); PyTorch (framework, core); FastAPI (framework, core); Hugging Face (ai_model, supporting); Cloudflare (cloud, supporting)
- **Sponsor APIs:**  | fit: Won the event-run Best Solo prize; the project was built by a single author.
- **Repo:** public, commits 38 (before/in/after event: 0/38/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 49, writeup long, impact claims False
- **Notes:** Solo build: YOLOv12n fine-tuned on 43,654 vehicle images, CLIP/EfficientNet-style classifiers, Whisper and Qwen for queries, run on an RTX 3090 and tunneled via Cloudflare; 49 screenshots.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/retrace-p3i7kl) | [GitHub](https://github.com/radmirkaz/ReTrace/tree/main)

### SI Storage  (StormHacks 2026)

- **Prizes:** Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** 3D warehouse dashboard linking inventory records in Neon Postgres with OCR of shelf photos, shown as pending observations until a human edits stock.
- **Problem / user:** Small warehouse teams count stock by hand and photos alone miss hidden boxes or sealed contents. / small warehouse operations teams
- **Domain / idea type:** productivity_workplace + retail_consumer / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; llm_chat
- **Stack:** langs TypeScript; Python; JavaScript; frontend React; Three.js; React Three Fiber; Vite; backend FastAPI; db PostgreSQL (Neon); hosting 
- **Tech/APIs:** Three.js / React Three Fiber (framework, core); Neon PostgreSQL (database, core); Firebase Authentication (auth, supporting); Cloudinary (cloud, supporting); OCR pipeline (other, supporting); OpenCV (framework, unclear); Gemini (ai_model, supporting)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 0, writeup long, impact claims False
- **Notes:** Adapted an existing WareTwin 3D scene; keeps OCR results as pending observations separate from verified stock and labels demo data as generated samples; no video or images listed.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/si-storage) | [GitHub](https://github.com/Tommy-Ren/SI-Storage)

### Soft Step  (StormHacks 2026)

- **Prizes:** Best Sports Analytics [unknown]  (tier: track_winner)
- **Pitch:** Leg-worn ESP32 and two-IMU sensor that measures knee angle and landing impact on hikes, with a web app and Snowflake Cortex chatbot to review technique.
- **Problem / user:** Downhill hiking causes knee pain, and hikers lack objective data on how hard they land and how much they bend their knees. / hikers
- **Domain / idea type:** health_wellness + entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; rag_or_search
- **Stack:** langs JavaScript; C++; frontend HTML; CSS; JavaScript; Chart.js; backend Node.js; db Supabase; IndexedDB; hosting Netlify
- **Tech/APIs:** ESP32 + 2 IMUs (hardware_part, core); Snowflake Cortex (ai_model, supporting, sponsor); Supabase (database, core); Chart.js (framework, supporting); Bluetooth (hardware_part, supporting)
- **Sponsor APIs:** Snowflake Cortex | fit: Won an event sports-analytics prize; page also shows a Snowflake Cortex chatbot over hike data, not tied to that prize.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots None, writeup long, impact claims False
- **Notes:** Complementary filter fuses thigh and shin IMU data; step logs saved in IndexedDB, gzip-compressed into Supabase; Cortex chatbot answers questions over hike records via the backend.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/hiking-sensor)

### SoftWear  (StormHacks 2026)

- **Prizes:** Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Smart jacket with an IMU and LEDs plus a room camera that detects falls and shows paramedics a body map of likely impact points.
- **Problem / user:** Older adults fall often; responders lack quick information on where the body hit. / older adults and paramedics
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / None
- **Stack:** langs C; Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); IMU (hardware_part, core); Room camera (hardware_part, core); LED matrix (hardware_part, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 3, writeup medium, impact claims True (Cites about 1 in 4 adults over 65 falling yearly and 78,000 Canadian fall hospitalizations in 2022.)
- **Notes:** Shows 'likely contact' and 'not measured' instead of claiming injuries; ESP32 jacket with LED matrix and camera-confirmed posture; no repo link on page.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/safe-landing)

### SURGE  (StormHacks 2026)

- **Prizes:** [MLH] Best Use of Snowflake API [unknown]  (tier: sponsor_winner)
- **Pitch:** Two-way flood emergency system pairing a government dashboard with a resident voice agent so alerts and ground reports flow both directions.
- **Problem / user:** Flash floods change fast and one-way alerts do not capture what residents are seeing or needing. / emergency officials and residents in flood zones
- **Domain / idea type:** safety_security + civic_legal / automation_or_agent
- **Platforms / hardware / AI:** web / False / speech_or_voice; agent_or_tool_use; llm_chat
- **Stack:** langs JavaScript; Python; frontend Next.js; React; backend Python; db Snowflake; hosting Render
- **Tech/APIs:** Snowflake (database, core, sponsor); ElevenLabs (ai_model, core, sponsor); Gemini (ai_model, supporting, sponsor); Next.js (framework, core); Render (cloud, supporting)
- **Sponsor APIs:** Snowflake; ElevenLabs; Gemini | fit: Won Best Use of Snowflake API; Snowflake is listed in the stack for the emergency data, though the writeup excerpt gives limited detail on its role.
- **Repo:** public, commits 72 (before/in/after event: 0/71/1), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 13, writeup long, impact claims False
- **Notes:** Inspired by flash flooding in Nepal; officials publish alerts and residents report via an ElevenLabs voice agent; Snowflake used for data; the writeup stresses a real-time two-way loop.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/surge-u2vh86) | [GitHub](https://github.com/awang1809/surge-stormhacks)

### ToughCrowd  (StormHacks 2026)

- **Prizes:** Best Beginner [unknown]; Best Highschool Hack [unknown]  (tier: track_winner)
- **Pitch:** Pitch practice tool where an AI judge panel hears your spoken pitch over uploaded slides, interrupts, asks tough questions and scores measured delivery.
- **Problem / user:** Hackathon teams are underprepared for hard judge questions like who pays for the product. / hackathon and startup pitchers
- **Domain / idea type:** education + productivity_workplace / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; agent_or_tool_use
- **Stack:** langs JavaScript; frontend HTML5; pdf.js; backend Node.js; db ; hosting Vercel
- **Tech/APIs:** ElevenLabs (ai_model, core, sponsor); OpenRouter (ai_model, core); pdf.js (framework, supporting); Vercel (cloud, supporting); .tech domain (other, supporting, sponsor)
- **Sponsor APIs:** ElevenLabs; .Tech Domains | fit: Won the event-run Best Beginner and Best Highschool Hack prizes; the page does not state the team's school status beyond the prize.
- **Repo:** public, commits 68 (before/in/after event: 0/68/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 28, writeup long, impact claims False
- **Notes:** Plain HTML/JS with no framework; pdf.js renders slides; speech-to-text keeps filler words so delivery stats are counted from timestamps; models chosen through OpenRouter after testing.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/toughcrowd) | [GitHub](https://github.com/eric-30/stormhacks-app)

### WeCare  (StormHacks 2026)

- **Prizes:** Best MedTech [unknown]; WiCS - WiCS Cosmos Track [unknown]  (tier: track_winner)
- **Pitch:** A Raspberry Pi puppy-shaped pill reminder that speaks to seniors, confirms doses by touch, scans bottles with Gemini, and logs to a caregiver app.
- **Problem / user:** Seniors on many medications make dosing mistakes and families cannot tell whether pills were taken. / Seniors and their family caregivers
- **Domain / idea type:** health_wellness + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_cross / True / vision; speech_or_voice; llm_chat
- **Stack:** langs Python; TypeScript; frontend Expo; React Native; Next.js; backend Python; APScheduler; db Firebase; hosting 
- **Tech/APIs:** Raspberry Pi (hardware_part, core); Google Gemini vision (ai_model, core); ElevenLabs (ai_model, core); Firebase (database, supporting); Expo / React Native (framework, supporting); OpenCV (framework, supporting); Capacitive touch sensor (hardware_part, supporting)
- **Sponsor APIs:**  | fit: MedTech and WiCS track: device plus caregiver app addressing medication adherence for seniors.
- **Repo:** public, commits 19 (before/in/after event: 0/19/0), README solid
- **Demo/writeup:** video False, live none, screenshots 3, writeup long, impact claims True (Cites Canadian statistics on seniors taking 10+ medications and medication nonadherence driving hospital and nursing home admissions.)
- **Notes:** 3D-printed puppy enclosure with touch sensor, speaker and webcam; bottle scan declines to answer when unsure; caregiver app was not yet live-connected to the device.
- **Team size:** 4 | **Confidence:** high | unverified: has_demo_video; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/carebot-q8x3t6) | [GitHub](https://github.com/sefu06/StormHacks-26)

### WhatDaDogDoing  (StormHacks 2026)

- **Prizes:** Huawei Custom Challenge #2 - Fetching Reality [unknown]  (tier: sponsor_winner)
- **Pitch:** Photograph a dog and about 40 seconds later a furry rigged 3D copy wanders around your room in phone AR, fetching and sniffing.
- **Problem / user:** Challenge asked for a lifelike 3D dog from one photo living in the real room; author had no GPU and needed it realistic. / dog owners and AR users
- **Domain / idea type:** entertainment_games + creative_media / entertainment_or_game
- **Platforms / hardware / AI:** web; mobile_cross / False / vision; generative_media
- **Stack:** langs Python; TypeScript; frontend three.js; React; backend Python server; WebSockets; db ; hosting Vercel; Cloudflare tunnel
- **Tech/APIs:** DINOv2 (ai_model, core); Stable Diffusion / VAE (ai_model, unclear); three.js (framework, core); Vercel (cloud, supporting); Cloudflare Tunnel (cloud, supporting); WebXR AR (framework, core)
- **Sponsor APIs:**  | fit: Directly implements the Huawei challenge brief of a single-photo 3D dog that lives in the user's real room.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots None, writeup medium, impact claims False
- **Notes:** Solo build running ML on a laptop CPU; motion matching over 41 minutes of dog mocap; 156K fur strands; AR on Android, gyro view on iPhone; multi-guest rooms.
- **Team size:** 1 | **Confidence:** high | unverified: n_screenshots; Stable Diffusion role; tech_items.is_sponsor; demo_video_url; has_demo_video; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/whatdadogdoing) | [GitHub](https://github.com/quannguyen2306-ctrl/stormhacks2026)

### Why Did We Choose This Tech?  (StormHacks 2026)

- **Prizes:** [MLH] Best .Tech Domain Name [unknown]  (tier: sponsor_winner)
- **Pitch:** Workspace where teams plan with an AI assistant by text or voice, publish architecture decision records, and have a GitHub bot check pull requests against them.
- **Problem / user:** Reasoning behind architecture decisions is scattered, and AI agents or contributors can drift from or invent scope without it. / software teams
- **Domain / idea type:** dev_tools + productivity_workplace / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; agent_or_tool_use
- **Stack:** langs TypeScript; frontend React; vinext; backend Cloudflare Workers; Drizzle; db PostgreSQL; PlanetScale; hosting Cloudflare
- **Tech/APIs:** .Tech domain (other, core, sponsor); Gemini via OpenRouter (ai_model, core); ElevenLabs (ai_model, supporting, sponsor); WorkOS (auth, supporting); GitHub review bot (other, core); MCP (other, supporting); Cloudflare Workers (cloud, core); PlanetScale / PostgreSQL (database, core); Linear / Slack (other, supporting)
- **Sponsor APIs:** .Tech Domains | fit: Product is served at whydidwechoosethis.tech and wdwct.tech, the .tech domains for the MLH domain prize.
- **Repo:** public, commits 136 (before/in/after event: 0/134/2), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 9, writeup long, impact claims False
- **Notes:** Exposes decisions to coding agents via MCP, adds Linear and Slack integrations, tracks provenance from conversation to published version; runs on Cloudflare Workers; the .tech domain is wdwct.tech and whydidwechoosethis.tech.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/why-did-we-choose-this-tech) | [GitHub](https://github.com/rockydotsystems/stormhacks2026)
