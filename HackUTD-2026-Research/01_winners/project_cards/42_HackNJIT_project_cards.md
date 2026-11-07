# HackNJIT: project cards (8 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackNJIT - 2023

### Coralations  (HackNJIT - 2023)

- **Prizes:** Best First-Year Hack [1st]  (tier: track_winner)
- **Pitch:** Website with a chatbot and interactive Caribbean maps linking coral bleaching severity to nearby countries' CO2 emissions.
- **Problem / user:** Coral bleaching in the Caribbean is tied to rising CO2 and warming, but the link is hard to see in raw data. / general public and students curious about coral bleaching
- **Domain / idea type:** sustainability_climate + education / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; frontend GoDaddy website builder; Folium HTML maps; backend Pandas; db ; hosting GoDaddy
- **Tech/APIs:** Folium (framework, core); Pandas (framework, core); GoDaddy (cloud, core); Kommunicate.io (other, supporting); Zenodo coral dataset (data_source, core); Kaggle CO2 dataset (data_source, core)
- **Sponsor APIs:** GoDaddy
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 0, writeup medium, impact claims False
- **Notes:** Built mostly with the GoDaddy site builder; maps made in Folium from merged Zenodo and Kaggle datasets; chatbot from a no-code builder. Prize is a first-year category.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots; is_sponsor_flags; github_url
- **Links:** [Devpost](https://devpost.com/software/name-po5230)

### SeaSOS  (HackNJIT - 2023)

- **Prizes:** 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Maritime operations app for cruise ships covering crew onboarding, staff management and emergency protocols, with an AR-capable iOS component.
- **Problem / user:** Ships need organized onboarding, staffing and emergency response processes. / Cruise and ship operators and crew
- **Domain / idea type:** safety_security + productivity_workplace / other
- **Platforms / hardware / AI:** web; mobile_ios / False / False
- **Stack:** langs Python; frontend Streamlit; backend ; db Redis; hosting AWS
- **Tech/APIs:** ARKit (framework, unclear); Redis (database, supporting); AWS (cloud, supporting); Streamlit (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 5 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 1, writeup short, impact claims False
- **Notes:** Built in 25 hours with Streamlit, Redis, AWS and ARKit for iOS; short writeup with one screenshot.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end; problem_statement; ai_used
- **Links:** [Devpost](https://devpost.com/software/seasos) | [GitHub](https://github.com/sarvagyad37/SeaSOS)

### Treasure Snap!  (HackNJIT - 2023)

- **Prizes:** 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Streamlit game where players try to find where a user-uploaded photo was taken and upload their own shot, which is scored against it by image comparison.
- **Problem / user:** Geocaching-style photo hunts need an automatic way to verify that a player reached the right spot. / Casual players and explorers
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs Python; frontend Streamlit; backend ; db MongoDB; hosting AWS
- **Tech/APIs:** CNN image comparison (ai_model, core); MongoDB (database, supporting); AWS (cloud, supporting); Streamlit (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 86 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video False, live none, screenshots 22, writeup long, impact claims False
- **Notes:** Attempts are validated against the target photo with two image-comparison methods including a CNN; Streamlit app with MongoDB on AWS.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; problem_statement
- **Links:** [Devpost](https://devpost.com/software/treasure-snap) | [GitHub](https://github.com/dustinlaa/HackNJIT2023)

### Wager Whales  (HackNJIT - 2023)

- **Prizes:** 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Fake-money betting site where users wager on events in live aquarium streams by drawing on the stream, with YOLOv8 detection checking outcomes.
- **Problem / user:** Entertainment-focused novelty of gambling-style play without real money, built around live animal streams. / Casual users who enjoy novelty games
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs Python; JavaScript; frontend Vue.js; backend Python; db ; hosting 
- **Tech/APIs:** YOLOv8 (ai_model, core); OpenCV (framework, supporting); Vue.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 7, writeup medium, impact claims False
- **Notes:** Bets are placed by drawing regions on live aquarium streams and resolved using YOLOv8 object detection; page links a live site but no repo.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; target_user; problem_statement
- **Links:** [Devpost](https://devpost.com/software/wager-whales)


## HackNJIT - 2024

### Gamify.work()  (HackNJIT - 2024)

- **Prizes:** Second Place [2nd]  (tier: overall_top3)
- **Pitch:** Workers play a remote apple-catching game while a factory robotic hand mirrors their hand movements to do real pick-and-place tasks.
- **Problem / user:** Repetitive industrial work is costly and causes burnout and turnover; the idea is to make it feel like play. / factory/warehouse workers and employers
- **Domain / idea type:** productivity_workplace / hardware_gadget
- **Platforms / hardware / AI:** desktop; web; hardware / True / vision
- **Stack:** langs Python; C++; JavaScript; frontend React; Tailwind CSS; Vite; Pygame; Tkinter; backend Python; PySerial; Sockets; db ; hosting Vercel
- **Tech/APIs:** MediaPipe (ai_model, core); OpenCV (framework, core); TensorFlow (framework, supporting); Arduino (hardware_part, core); Bluetooth module / PySerial (hardware_part, core); Pygame (framework, core); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 1 (before/in/after event: None/None/None), README none
- **Demo/writeup:** video False, live not_checked, screenshots None, writeup long, impact claims False
- **Notes:** Webcam hand tracking drives a Pygame game and sends commands over Bluetooth serial to an Arduino robotic hand; one Arduino failed mid-build.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/gamify-work-swhulb) | [GitHub](https://github.com/AnishPandey1944/HACK_NJIT_REPO)

### Medify  (HackNJIT - 2024)

- **Prizes:** Third Place [3rd]  (tier: overall_top3)
- **Pitch:** Web app for soldiers and field medics: AI wound identification, privacy image censoring, GPT-generated treatment steps read aloud, with blockchain record keeping.
- **Problem / user:** Medics and soldiers in remote, high-stress settings need fast, reliable wound assessment and treatment guidance. / field medics and soldiers
- **Domain / idea type:** health_wellness + safety_security / automation_or_agent
- **Platforms / hardware / AI:** web / True / vision; llm_chat; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend Next.js; React; Tailwind CSS; backend FastAPI; Flask; PyTorch; db ; hosting Cloudflare
- **Tech/APIs:** PyTorch wound classifier (ai_model, core); GPT wrapper (ai_model, supporting); Midnight (other, token, sponsor); Raspberry Pi + fswebcam (hardware_part, unclear); FastAPI (framework, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** Midnight
- **Repo:** public, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup medium, impact claims False
- **Notes:** Two models (wound classifier and image censor) plus GPT wrapper and text-to-speech; Raspberry Pi/fswebcam listed; Midnight protocol was only planned for encrypting records.
- **Team size:** 4 | **Confidence:** medium | unverified: has_hardware; has_demo_video; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/medify-khoaid) | [GitHub](https://github.com/SitaaronKL/Medify)

### SteamPunch  (HackNJIT - 2024)

- **Prizes:** Best First-Year Hack [1st]  (tier: track_winner)
- **Pitch:** Steampunk-styled Arduino controller with ultrasonic sensor and joystick that plays a custom Pygame 2D fighting game.
- **Problem / user:** Team wanted to merge Arduino skills and game development into a custom physical game controller. / casual gamers / hackathon demo audience
- **Domain / idea type:** entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** desktop; hardware / True / False
- **Stack:** langs Python; C++; frontend Pygame; backend ; db ; hosting 
- **Tech/APIs:** Arduino (hardware_part, core); Ultrasonic sensor and joystick (hardware_part, core); Pygame (framework, core); PySerial (framework, core); PlatformIO (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 42 (before/in/after event: None/None/None), README thin
- **Demo/writeup:** video True, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Controller auto-detects the Arduino serial port by vendor/product ID; shell made from recycled cups and paper; switched from Unity to Pygame after serial integration trouble.
- **Team size:** 3 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/steampunch) | [GitHub](https://github.com/MaKe-MaX/MaKeMaX_HackNJIT2024)

### TheBackPak  (HackNJIT - 2024)

- **Prizes:** First Place [1st]  (tier: overall_top3)
- **Pitch:** Wearable posture tracker: two motion sensors on clothing feed a regression model and a Flask web app alerts on bad posture.
- **Problem / user:** Poor daily posture causes chronic pain and lower productivity, and people lack real-time feedback. / people with desk or daily posture problems
- **Domain / idea type:** health_wellness / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / predictive_ml
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend Flask; db ; hosting 
- **Tech/APIs:** Flask (framework, core); Linear regression model (ai_model, core); I2C motion sensors (hardware_part, core); Microcomputer (unspecified) (hardware_part, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 36 (before/in/after event: None/None/None), README thin
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Two sensors given separate I2C addresses on a microcomputer; linear regression classifies good vs bad posture; everything runs on the device with a Flask UI.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/thebackpak) | [GitHub](https://github.com/Binimal101/theBackPak)
