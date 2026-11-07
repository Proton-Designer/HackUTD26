# HackNJIT — HackNJIT - 2024 (4 projects)

### Gamify.work()
*HackNJIT HackNJIT - 2024 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Second Place [2nd]

**What it is:** Remote work game that controls a physical robot hand: the player moves their own hand to catch virtual apples, MediaPipe and a TensorFlow gesture model turn the movements into commands sent over Bluetooth, and the robotic hand in a factory repeats them.
**Problem / user:** Repetitive industrial tasks cause burnout and turnover; the idea lets workers do them remotely as a game.

**Features**
- Apple-catching game — Playable remotely; hand movement guides a virtual hand to catch apples and drop them in a basket. *[claimed]*
- Hand tracking and gestures — MediaPipe landmarks with OpenCV and a TensorFlow gesture classifier. *[claimed]*
- Robotic hand mirroring — Arduino-driven hand copies the player moves in real time over Bluetooth with PySerial. *[claimed]*
- Data compression — Messages between components are compressed and encoded. *[claimed]*
- Web front end — React, Tailwind and Vite UI; Devpost also mentions Pygame and tkinter. *[unclear]*
- Multiplayer and other games — Future collaboration or competition modes. *[planned]*

**Flow:** Open game from home → Move hand in front of camera → Virtual hand catches apples → Gestures sent to robot hand → Factory hand performs pick and place

**Prompt:** HackNJIT 2024 Second Place (2nd Place Runner Up, $1,000 split); event theme was Steampunk with a themed-hack prize.
**Fit (none):** No stated prize targeting; page does not tie to the steampunk theme.  *(targeted: 2nd Place Runner Up)*
**AI:** MediaPipe hand landmarks plus TensorFlow gesture recognition map hand poses to robot commands.
**Architecture:** Webcam to Python (MediaPipe, OpenCV, TensorFlow) to game and serial/Bluetooth link to Arduino robot hand; React site on Vercel. Exact link method inconsistent on page.
**Novelty:** Gamifies physical remote manipulation with a hardware robot hand, a hardware build beyond typical web demos.
**Scope:** small · working: Two demo site links and repos listed; no video; one Arduino failed and troubleshooting dominated time. · polish: About 870 LOC in 12 root files, no README or tests.
**Claims:** Seamless connection between gameplay and robotic function | Data compression without losing essential details
**Gaps:** repo has no README; hardware demo not evidenced
Sources: https://devpost.com/software/gamify-work-swhulb, evidence/hacknjit-hacknjit-2024-gamify-work.json (no README, tree only), prompts_cache/hacknjit-2024.md

---

### Medify
*HackNJIT HackNJIT - 2024 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Third Place [3rd]

**What it is:** Web app for soldiers and field medics: the user photographs a wound, a PyTorch model identifies it, a censoring model protects privacy, and a GPT wrapper produces step-by-step treatment instructions read aloud.
**Problem / user:** Soldiers and field medics treating injuries in remote, high-stress settings where fast, correct treatment matters.

**Features**
- Wound photo capture and identification — PyTorch classification model trained with data augmentation; images captured via a Raspberry Pi with fswebcam or device camera. *[claimed]*
- Image censorship model — Second PyTorch model masks sensitive content in wound images for privacy. *[claimed]*
- GPT-generated treatment steps — A GPT wrapper turns the identified wound into detailed step-by-step instructions. *[claimed]*
- Text-to-speech instructions — Treatment steps are read aloud so hands stay free. *[claimed]*
- Blockchain record keeping — Immutable storage of sensitive records; kept lightweight for low connectivity. *[claimed]*
- MedKit Manager page — Page for tracking medkit contents, shown in screenshots. *[unclear]*
- Midnight encryption of soldier ID, inventory, injury location — Planned privacy layer; page says they were planning to integrate it. *[planned]*

**Flow:** Open the web app → Snap a photo of the wound → Models identify the wound and censor the image → GPT wrapper writes treatment instructions → Instructions are spoken via text-to-speech → Record is stored on blockchain layer

**Prompt:** HackNJIT 2024 overall places (First/Second/Third) rewarded the best overall hacks; the MLH Midnight prize asked teams to build a DApp using Midnight.
**Fit (implied):** Placed third overall; Midnight encryption was listed as a planned integration for sensitive medical data, so the sponsor link is partial.  *(targeted: Third Place, MLH Best Use of Midnight (likely))*
**Sponsor tools:** Midnight (planned encryption of soldier ID, medkit inventory and injury data, unclear)
**AI:** Two PyTorch models (wound identification and image censoring) plus a GPT wrapper that generates treatment text; no accuracy figures given.
**Architecture:** React/Next.js frontend with Flask/FastAPI Python backend; PyTorch models; GPT wrapper; text-to-speech; blockchain ledger; Raspberry Pi camera capture; served through Cloudflared.
**Novelty:** Combines wound CV, privacy censoring, LLM first-aid guidance and an immutable ledger for a military field-medic scenario; includes a Raspberry Pi camera path.
**Scope:** small · working: Live site medify.tech and screenshots listed; no metrics or video, and repo README unreadable. · polish: Landing page and MedKit Manager screenshots; Midnight integration unfinished.
**Claims:** Works across environments and lighting conditions for wound ID | Quick treatment can decide life or death (framing)
**Gaps:** repo clone failed and GitHub/raw README not fetchable; no demo video; screenshot count approximate
Sources: https://devpost.com/software/medify-khoaid, https://hacknjit-2024.devpost.com/

---

### SteamPunch
*HackNJIT HackNJIT - 2024 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best First-Year Hack [1st]

**What it is:** A 2D platformer-fighter written in Pygame and played with a handmade steampunk-styled Arduino controller. An ultrasonic sensor reads hand pull-back to charge attacks and a joystick dodges. Story: a factory robot turns on a polluting industry.
**Problem / user:** No stated problem; a game for players who want a physical, motion-based controller experience.

**Features**
- Custom Arduino controller — Arduino Uno with ultrasonic sensor and joystick, housed in recycled materials styled steampunk. *[shown_working]*
- Serial input to PC with auto port detection — Python pyserial finds the Arduino by vendor and product ID, no manual port config. *[shown_working]*
- Motion-based attack charge — Pulling a hand back from the ultrasonic sensor charges an attack. *[claimed]*
- Joystick dodging — Swinging the joystick dodges enemies. *[claimed]*
- Pygame 2D fighting game — Game logic written from scratch with non-copyrighted assets. *[shown_working]*
- Multiple levels and narrative — Levels 1 to 3 in screenshots; robot-versus-former-comrades story. *[shown_working]*

**Flow:** Plug in the Arduino controller → Run the Pygame game; port is auto-detected → Swing joystick to dodge enemies → Pull hand back to charge and punch → Progress through levels

**Prompt:** Best First-Year Hack: best hack from teams with more than 50% freshmen. Event theme was Steampunk.
**Fit (implied):** Page says team is early-career and improved since a prior hackathon; controller is steampunk-styled and the game has an industrial-robot story.  *(targeted: Best First-Year Hack, Best Themed Hack (steampunk))*
**AI:** none
**Architecture:** Arduino Uno (C++ via PlatformIO) reads ultrasonic and joystick values and writes them over serial; a Python pyserial layer feeds a Pygame game loop.
**Novelty:** Physical hardware controller with distance-based punch charging for a self-written game; team first tried Unity then switched to Pygame.
**Scope:** small · working: Three level screenshots and controller photos; repo contains game source and PlatformIO project. · polish: Themed enclosure from recycled materials; no video or live link.
**Claims:** First time getting Arduino to communicate with external software
**Gaps:** no video; README two lines; LOC inflated by PlatformIO libs
Sources: https://devpost.com/software/steampunch, evidence/hacknjit-hacknjit-2024-steampunch.json, https://hacknjit-2024.devpost.com/

---

### TheBackPak
*HackNJIT HackNJIT - 2024 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** First Place [1st]

**What it is:** A wearable posture tracker: two orientation sensors on clothing are read by a microcomputer, a linear regression model labels posture good or bad, and a Flask web app shows live feedback and alerts.
**Problem / user:** People with poor daily posture who risk chronic pain and productivity loss.

**Features**
- Two-sensor back angle tracking — Two BNO055-class sensors on separate I2C addresses give x,y,z orientation in real time. *[claimed]*
- Posture classification — Linear regression model trained to label posture good or bad, run on the microcomputer. *[claimed]*
- Live web feedback — Flask app updates in real time with posture state. *[claimed]*
- Posture alerts — Notifies the wearer when to adjust posture. *[claimed]*
- Long-term tracking, suggestions, mobile app — Listed as future work. *[planned]*

**Flow:** Attach sensors to clothing → Python scripts read sensor orientation → Model classifies posture → Flask web app shows live feedback and alerts

**Prompt:** First Place: "Best in Show" overall hack at HackNJIT 2024.
**Fit (none):** Overall prize with no specific challenge; submission is a working hardware plus ML prototype.  *(targeted: First Place)*
**AI:** Simple linear regression on sensor x,y,z readings classifies good versus bad posture; model file included in repo.
**Architecture:** Two I2C orientation sensors to a microcomputer running Python scripts and the regression model, exposing results through a Flask backend to an HTML/CSS/JS front end.
**Novelty:** Garment-mounted dual-sensor posture sensing with an on-device model; Adafruit BNO055 dependencies and a Gemini client library appear in requirements.
**Scope:** tiny · working: Devpost claims working prototype with end-to-end feedback; repo is about 430 lines with a model folder. · polish: README is only a title; no video or screenshots mentioned.
**Claims:** Working prototype tracks posture with real-time feedback
**Gaps:** no accuracy numbers; hardware models unnamed on page; no video
Sources: https://devpost.com/software/thebackpak, evidence/hacknjit-hacknjit-2024-thebackpak.json, https://hacknjit-2024.devpost.com/

---

