# StormHacks — StormHacks 2025 (27 projects)

### Air Command
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [MLH] Best Use of Snowflake API

**What it is:** A sip-and-puff breath controller built on a BeagleBone with a differential pressure sensor. It shows up over Bluetooth as an ordinary keyboard and mouse, so a person with limited mobility can drive a computer by breathing. An optional voice layer uses an LLM to turn spoken commands into key sequences.
**Problem / user:** People with limited mobility who cannot use a standard keyboard and mouse and need an alternative input device.

**Features**
- Breath-driven input device — Pressure sensor feeds the BeagleBone ADC; readings are converted to kPa, filtered and classified into gestures *[claimed]*
- Gesture classification — State machines and timing thresholds separate short sip, long puff and continuous actions *[claimed]*
- Bluetooth HID keyboard and mouse — Composite HID over GATT (BLE) via BlueZ presents mouse movement, clicks and shortcuts to any host *[claimed]*
- Voice-to-keystroke mapping — Snowflake Cortex LLM maps natural-language commands such as opening a browser to HID key sequences *[claimed]*
- Typo-tolerant command resolution — Misspelled commands still resolve to the intended shortcut, with HID byte array generated *[claimed]*
- Linux input emulation — Uses /dev/uinput for local device emulation alongside BlueZ *[claimed]*

**Flow:** User sips or puffs into the pressure sensor → BeagleBone reads, filters and classifies the signal into a gesture → Gesture becomes an HID report sent over BLE to the paired computer → Optionally the user speaks a command that the LLM converts to a key sequence

**Prompt:** MLH prize for using Snowflake's REST API to access LLMs on a single account; student 120-day Snowflake trial offered, Arduino TinyML kit as prize.
**Fit (explicit):** Adds Snowflake Cortex as an optional natural-language layer converting voice commands into HID key sequences; the core device works without it.  *(targeted: [MLH] Best Use of Snowflake API)*
**Sponsor tools:** Snowflake Cortex LLM (Mapping natural-language voice commands to HID key sequences, supporting)
**AI:** Snowflake Cortex LLM interprets spoken or typed commands and outputs key sequences; the voice recognition engine is not named. Gesture classification is rule-based, not ML.
**Architecture:** MPXV7002DP sensor via resistor divider into BeagleBone ZenHat ADC, Python/C gesture classifier, BlueZ HID-over-GATT BLE peripheral and uinput; Cortex call for command mapping.
**Novelty:** Hardware assistive-input build with custom BLE HID descriptor work, pairing a physical sip-puff sensor with an LLM command layer.
**Scope:** small · working: Repo of about 900 lines in hal/ and app/; Devpost describes solved BLE and ADC issues but shows no demo. · polish: Minimal README, one screenshot, no video.
**Claims:** Appears to any computer as a standard keyboard and mouse | Tagline says the device learns, unexplained
**Gaps:** README is only a title; no video; voice engine unnamed
Sources: https://devpost.com/software/air-command-smu9t0, https://github.com/bsbhakti/stormhacks, https://stormhacks2025.devpost.com/

---

### ASL Express - Touchless AI Food Ordering Assistant
*StormHacks StormHacks 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Hardware

**What it is:** A drive-thru style ordering kiosk prototype where a person signs letters to a laptop camera. MediaPipe hand tracking and Gemini interpret the sign, and the confirmed order goes over serial to an ESP32 that shows it on an LCD with LEDs and a buzzer.
**Problem / user:** Deaf and mute customers who find speech-based ordering at drive-thrus and kiosks frustrating or impossible; also public venues like hospitals and airports.

**Features**
- Sign-to-menu recognition — MediaPipe hand landmarks plus Gemini classify signs A, B, C as burger, fries, drink. *[claimed]*
- Quantity by repetition — Repeating a sign 1 to 3 times sets the quantity. *[claimed]*
- Thumbs-up to finalize — A thumbs-up (called Done) confirms the order. *[claimed]*
- ESP32 order handoff — Python sends the confirmed order via pyserial over USB/UART to an ESP32 running C++ firmware. *[claimed]*
- Physical feedback — LCD shows the order; LEDs and a buzzer confirm recognition; an ultrasonic sensor is attached but its role is unstated. *[claimed]*

**Flow:** Stand in front of laptop camera → Sign A, B or C, repeating for quantity → Give a thumbs-up to finish → Order sent to ESP32 → LCD, LEDs and buzzer confirm

**Prompt:** Best Hardware: "Awarded to the best hardware hack!" Prize: air fryer per team member.
**Fit (implied):** Joins an AI vision pipeline to an ESP32 board with LCD, LEDs, buzzer and an ultrasonic sensor; page says it bridges AI vision and embedded hardware. Prize link is stated by results, not the text.  *(targeted: Best Hardware)*
**Sponsor tools:** Google Gemini API (Gesture analysis and intent mapping alongside MediaPipe landmarks, supporting); ElevenLabs (Planned voice feedback; listed as a tag only, token)
**AI:** MediaPipe extracts hand landmarks via OpenCV; Gemini API classifies the gesture and maps intent. No training data or accuracy numbers given.
**Architecture:** Laptop Python app (OpenCV, MediaPipe, Gemini) sends orders by pyserial to an ESP32 (Arduino IDE C++) driving LCD, LEDs, buzzer and ultrasonic sensor. Three repos (frontend, backend, hardware).
**Novelty:** Accessibility use case translating sign language into a physical ordering device; limited to three letters plus a done gesture.
**Scope:** medium · working: Ten screenshots and claimed full prototype; linked front-end repo is about 9,200 LOC of v0-generated Next.js with Supabase deps and no README. · polish: No video, demo link or README; hardware and backend repos could not be opened.
**Claims:** Fully functional prototype bridging AI vision and embedded hardware. | Reliable recognition of gestures with high accuracy (no metrics).
**Gaps:** Evidence repo has no README and looks like a web front end; backend and hardware repos unreadable; Page inconsistent on gesture count (three signs vs four plus Done); Frontend deps (Supabase) not explained on page
Sources: https://devpost.com/software/sign2order-touchless-ai-food-ordering-assistant, evidence file for KashfiRashid/ASL_Express (no README), https://stormhacks2025.devpost.com/

---

### Carrie - AI Therapy In Your Pocket
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of ElevenLabs

**What it is:** A web app where a user holds a live video call with an AI therapist voiced through ElevenLabs. Webcam frames are classified for facial emotion every couple of seconds and that emotion is injected into the conversation so the agent adjusts its tone. Chats are stored for later review.
**Problem / user:** People who find therapy costly, slow to book or stigmatized, including burnt-out professionals and healthcare workers, wanting an always-available judgment-free listener.

**Features**
- Real-time facial emotion detection — Webcam frame every 2s, OpenCV Haar face detection then a ViT classifier for 7 emotions with confidence *[shown_working]*
- Emotion-aware replies — Agent Manager prepends detected emotion to the user message so the ElevenLabs agent shifts tone (gentle if sad, calm if angry) *[claimed]*
- Live video sessions — LiveKit WebRTC rooms with tokens issued by the Node backend *[claimed]*
- Voice conversation — ElevenLabs Conversational AI handles speech in and synthesized empathetic voice out *[claimed]*
- Conversation history — MongoDB stores sessions; history page lets users review past chats *[claimed]*
- Anonymous accounts and auth — JWT sessions with bcrypt-hashed passwords and protected routes *[claimed]*
- Emotion webhook and SocketIO updates — Flask AI service exposes process_frame, emotion and webhook endpoints plus socket push *[claimed]*
- Containerized AWS deployment — Docker Compose, ECS Fargate, ECR, Secrets Manager, CloudWatch documented *[claimed]*

**Flow:** User signs up or logs in → Starts a video session with Carrie → Frontend sends compressed webcam frames every 2s to backend → AI service returns the detected emotion → Emotion is attached to the user message going to ElevenLabs → Carrie answers by voice in the call → Session is logged and appears in history

**Prompt:** MLH prize for deploying natural, human-sounding audio with ElevenLabs; encourages voice-enabled or narrated experiences. Prize: ElevenLabs earbuds/AirPods.
**Fit (implied):** ElevenLabs Conversational AI is the therapist's voice and dialogue engine, with prompt variables carrying emotion context to shape tone.  *(targeted: [MLH] Best Use of ElevenLabs)*
**Sponsor tools:** ElevenLabs Conversational AI / TTS (Voice agent persona and spoken replies with dynamic emotion variables, core)
**AI:** Hugging Face Vision Transformer classifies 7 facial emotions from webcam frames; ElevenLabs conversational agent generates voiced replies, with emotion context injected through prompt/dynamic variables.
**Architecture:** React/LiveKit frontend captures frames; Node/Express backend (auth, LiveKit tokens, agent manager, MongoDB) proxies to a Flask PyTorch emotion service; ElevenLabs agent returns voice.
**Novelty:** Couples computer-vision emotion detection with a voice agent so the therapist reacts to facial affect, plus full AWS deployment config.
**Scope:** medium · working: About 6,700 LOC across frontend, Node backend and Python AI service; screenshots of chat and emotion view. · polish: Long README with architecture diagram and API docs, Dockerized, mobile and desktop layouts; no tests.
**Claims:** Sub-2-second capture to response latency, no method given | Described as production-ready | Therapy cost cited as $100-300 per hour
**Gaps:** no demo video; Canva slides not read; crisis detection only planned
Sources: https://devpost.com/software/carrie-ai-therapy-in-your-pocket, https://github.com/TimSeah/StormHacks_LumberLoons, https://stormhacks2025.devpost.com/

---

### ConnectSFU
*StormHacks StormHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Software Systems Prize

**What it is:** A web portal for SFU students to find campus events and clubs, RSVP, and request an event buddy, with Gemini-powered natural-language search. Includes a mock club-admin view. Next.js with Supabase auth limited to SFU emails.
**Problem / user:** SFU students who miss events scattered over Instagram, Discord and email, especially those who hesitate to attend alone; clubs struggling to reach audiences.

**Features**
- Unified event browsing — Home page with search, featured events, trending categories, new clubs; events page filters by campus, category, dates, popularity. *[shown_working]*
- AI natural-language search — Gemini API matches a free-text description to events or clubs. *[claimed]*
- RSVP and calendar link — Event detail page has an RSVP form and a Google Calendar link. *[claimed]*
- Find a Buddy — User sets comfort and vibe preferences tied to an event; Demo Mode pairs the first compatible request into a match record; Gemini scoring planned. *[claimed]*
- Match notifications and messages — Matched users are notified and a view shows the latest message per buddy. *[claimed]*
- Club admin dashboard — Create events and see attendance and sign-up stats; described as a mockup. *[planned]*
- SFU-email login — Supabase Auth restricts sign-in to SFU addresses. *[claimed]*

**Flow:** Log in with SFU email → Search or filter events → Open an event and RSVP or add to Google Calendar → Click Find a Buddy and submit preferences → Get matched and message

**Prompt:** Software Systems Prize: "Awarded to the best project from a team consisting of at least 2 Software Systems Students." Prize: JBL speakers.
**Fit (none):** A multi-table full-stack web system with auth, database, AI search and deployment; the prize rule concerns team composition, which the page does not discuss.  *(targeted: Software Systems Prize)*
**Sponsor tools:** Gemini API (Natural-language event/club search and planned buddy-pair scoring, supporting)
**AI:** Gemini API powers natural-language event search; planned production mode scores buddy pairs from bios, interests, vibe and event details above a match threshold. Demo Mode pairs without AI.
**Architecture:** Next.js 14 and TypeScript front end with Tailwind/DaisyUI and Framer Motion; Supabase Postgres, auth, buddy_requests and buddy_matches tables; Gemini API; Resend dependency; Vercel deploy.
**Novelty:** Buddy-matching angle for solo attendees on top of an event board; README is a stale early-status list that contradicts the finished Devpost scope.
**Scope:** medium · working: Live Vercel demo link and about 6,000 LOC; Devpost walkthrough describes login, filters, RSVP and buddy flow. · polish: Figma design system and animated assets; README still lists core features as next steps; no tests or video.
**Gaps:** README (early status) and Devpost describe different completeness; feature list follows Devpost; Demo not opened; page lists test login credentials which were not recorded
Sources: https://devpost.com/software/connectsfu, https://github.com/avkap007/stormhacks-connectsfu (evidence file README), https://stormhacks2025.devpost.com/

---

### EcoDepot
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SEE Sustainable Engineering Track; Surge Choice Award

**What it is:** A smart recycling and trash bin prototype: a camera identifies an item thrown on a chute, the bin rotates to the right compartment, and refundable bottles credit money to a student account that is opened by scanning the ID barcode.
**Problem / user:** People who misjudge what is recyclable and have little incentive to sort; page cites low bottle recycling rates and BC deposit refunds; first target is university students.

**Features**
- Camera-based item sorting — TensorFlow model plus a hybrid AI check identifies trash or recyclable type. *[claimed]*
- Rotating bin compartments — Microcontroller (Arduino, C++) turns motors to position the correct compartment, then deposits. *[claimed]*
- Student ID barcode login — Camera reads the ID barcode, used as a UUID, to start a session in seconds. *[claimed]*
- Deposit refund credit — Refundable cans and bottles deposited in a session add money to the account. *[claimed]*
- User dashboard — Next.js and Supabase app shows account info and bottle transaction history. *[claimed]*

**Flow:** Hold student ID to the camera to log in → Drop an item on the chute → Bin classifies it and rotates to the right slot → Refundable items credit the account → View balance and history in the dashboard

**Prompt:** SEE Sustainable Engineering Track: apply engineering principles for lasting environmental and social impact. Surge Choice Award: most creative and inspiring project, picked by SFU Surge organizers.
**Fit (explicit):** README ties it to UN SDGs 9 and 12 and recycling incentives via engineering hardware plus ML. Creative and inspiring angle is judged by Surge, no stated tie.  *(targeted: SEE Sustainable Engineering Track, Surge Choice Award)*
**AI:** TensorFlow model trained to recognize recyclables from camera images, with an AI-based verification step; separate vision step reads the ID barcode. Dataset not named.
**Architecture:** Python vision/ML detects items and barcodes; microcontroller drives motors rotating the bin; Next.js/React front end with Supabase (and edge functions) on Netlify; parts 3D printed from Fusion 360 designs.
**Novelty:** Pairs sorting hardware with a deposit-refund economic incentive and barcode-based login workaround for ID cards.
**Scope:** medium · working: About 5,000 LOC in frontend, supabase and docs; Netlify demo link; team calls it a proof of concept. · polish: Detailed README mirroring the Devpost writeup; no video; dropped one motor due to supplies.
**Claims:** Page cites that only 16% of bottles were recycled in 2022. | Aims to recycle thousands of bottles at one university.
**Gaps:** No accuracy or throughput numbers; Demo not opened; ML code location in repo not confirmed
Sources: https://devpost.com/software/ecodepot, https://github.com/iancdev/recycle-sorter (evidence file README), https://stormhacks2025.devpost.com/

---

### EcoTag
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** United Nations Sustainable Development Goals Enactus Challenge

**What it is:** A phone-camera laser tag game where players wear QR codes and tag each other in the browser, combined with a clean-up mode where they scan litter, have vision AI classify it, and earn points for choosing the right bin. A shared leaderboard merges both.
**Problem / user:** Groups wanting laser tag without arenas or gear, and the cleanup chore after gatherings; players of all ages at parks, schools, offices and homes.

**Features**
- QR-code laser tag — Each player wears a QR code; tap-to-shoot captures a camera frame and ZXing-WASM decodes the target code to score. *[shown_working]*
- Litter scanning and classification — Camera scan of an item is classified by OpenAI vision into Organic, Paper, Recyclable or Landfill. *[claimed]*
- Bin check and CO2 savings — Points for correct bin, plastic multipliers, penalties for wrong bins, and a CO2-equivalent estimate. *[claimed]*
- Live leaderboard — Combines tagging and tidying points across players. *[claimed]*
- Real-time multiplayer sync — WebSocket event bus with 15+ event types, reconnection, optimistic updates, differential state sync. *[claimed]*
- Adaptive QR detection — Resolution scales with zoom; capture only on tap; frames compressed to about 200KB; zoom/pan coordinate mapping. *[claimed]*
- Haptic and sound feedback — Vibration and effects on actions. *[claimed]*

**Flow:** Join a game on a phone browser → Scan opponent QR tags to score → Scan litter and match it to the right bin → Watch leaderboard of combined points

**Prompt:** UN SDG Enactus Challenge: design innovative, scalable solutions for one or more of the UN 17 SDGs; judged on front end, back end, design, originality and fit to the chosen goal.
**Fit (explicit):** README says it won the SDG challenge; gameplay encourages sorting waste and shows CO2 savings, promoting responsible consumption through a social game.  *(targeted: United Nations Sustainable Development Goals Enactus Challenge)*
**AI:** OpenAI Vision API classifies photographed litter into four categories and feeds CO2 estimates and game analytics; README also lists Google Cloud Vision as a dependency. QR decoding is non-AI.
**Architecture:** React/TypeScript/Vite phone client with ZXing-WASM and a WebSocket game client; Node/Express backend with Firebase, ws, OpenAI and Vision APIs; Vercel deployment.
**Novelty:** Merges a camera-only laser tag mechanic with an environmental sorting game and CO2 scoring; unusually heavy engineering detail on latency.
**Scope:** large · working: Backend about 8,100 LOC with tests; separate frontend repo, Vercel demo link, embedded demo video and labeled screenshots. · polish: Extensive README with latency numbers; five captioned screenshots; self-described world first claim.
**Claims:** QR accuracy 95% at 20 FPS, detection under 100 ms. | WebSocket round trip under 15 ms; end-to-end under 50-100 ms. | Adaptive processing cuts overhead 40%. | Picked among top projects of 778 participants (README).
**Gaps:** Evidence repo is backend only; frontend repo qr-tag-arena README could not be fetched; Latency figures are self-reported; Video content not viewed
Sources: https://devpost.com/software/taqr, https://github.com/fesenjuniors/backend (evidence file README), https://stormhacks2025.devpost.com/

---

### EduFind
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best Use of SFU Courses API

**What it is:** A web app for SFU students that recommends courses from an uploaded transcript using the DeepSeek API, shows success ratings, and offers a drag-and-drop course planner fed by the SFU Courses API, plus a social/community page.
**Problem / user:** SFU students choosing courses; wanting course selection as easy as modern page builders.

**Features**
- Transcript-based course recommendations — README: DeepSeek API recommends courses from parsed transcripts and academic performance. *[claimed]*
- Student success ratings — Parsed grades generate ratings to guide course choice. *[claimed]*
- Drag-and-drop course planner — Dnd-kit planner with live course data from the SFU Courses API. *[claimed]*
- Course community / socials — Users interact socially about courses; backend has Socket.io and Mongo/Postgres deps. *[claimed]*
- Dashboard — One teammate built the dashboard; page says clean interactive UI works with both APIs. *[claimed]*

**Flow:** Sign in and upload a transcript → View recommendations and ratings → Drag courses into a plan using live SFU data → Discuss courses on the socials page

**Prompt:** Best Use of SFU Courses API: "Best usage of API from https://api.sfucourses.com" (no further description).
**Fit (explicit):** Its course builder pulls course data from the SFU Courses API for drag-and-drop planning; README says it earned this award for that.  *(targeted: Best Use of SFU Courses API)*
**Sponsor tools:** SFU Courses API (Real-time course information in the drag-and-drop planner, core); DeepSeek API (Transcript-based course recommendations, supporting)
**AI:** DeepSeek API generates personalized course recommendations from parsed transcript data; PDF parsing via pdf-parse. Prompting details not given.
**Architecture:** React and Tailwind front end with dnd-kit; Express backend with Supabase/Postgres, auth and rate limiting; calls SFU Courses API and DeepSeek.
**Novelty:** Combines transcript parsing with AI recommendations and a visual planner; Devpost text is brief and README states more than the page.
**Scope:** medium · working: README says full-stack MVP built in 24 hours; about 8,200 LOC (backend tree inflated by 4,700 files); tests and Docker present. · polish: No screenshots counted, video or live link; pricing and likes features unbuilt; admits scope creep.
**Claims:** Full-stack MVP built in 24 hours (README).
**Gaps:** Devpost page short; transcript and success-rating features come only from README; Backend deps (Mongo, Socket.io) suggest community features of unclear maturity
Sources: https://devpost.com/software/edufind-aveu6k (via Chrome), https://github.com/StormHacks-2025/ProjectCourseBuilder (evidence file README), https://stormhacks2025.devpost.com/

---

### Encore
*StormHacks StormHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Most Likely to Become a Startup

**What it is:** An Expo React Native concert companion that lists local upcoming shows from Ticketmaster, lets users add friends, mark Attending or Interested, and optionally share seat numbers to find friends at the venue.
**Problem / user:** Concert-goers who do not know which friends are at the same shows and cannot easily meet up at the venue.

**Features**
- Local concert feed — Ticketmaster Discovery API results fetched through Vercel serverless functions, browsed by location. *[claimed]*
- Friends and overlapping concerts — Add friends and see which shows they plan to attend. *[claimed]*
- Attending / Interested status — Users mark each show so friends can see their plans. *[claimed]*
- Optional seat sharing — Share seat number to locate friends inside the venue. *[claimed]*
- Auth and storage — Firebase Auth and Firestore hold accounts and social data. *[claimed]*

**Flow:** Sign in → Add friends → Browse local concerts → Mark Attending or Interested → Optionally share seat info

**Prompt:** Most Likely to Become a Startup: projects with the strongest potential to grow beyond the hackathon; judged on market need, scalability, viable business path.
**Fit (implied):** Consumer social app with a clear audience and expansion roadmap (venue partners, Spotify/Apple Music integration, groups, reviews); the page does not discuss business model.  *(targeted: Most Likely to Become a Startup)*
**AI:** none
**Architecture:** Expo (React Native) TypeScript app styled with NativeWind; Firebase Auth/Firestore; Vercel serverless functions proxy the Ticketmaster API.
**Novelty:** Social layer over existing ticketing data with seat sharing; standard stack and scope.
**Scope:** small · working: About 4,800 LOC with login, home and friends screens; embedded demo video and four screenshots. · polish: Canva design deck; README notes the public repo is a copy because the main repo had exposed keys.
**Gaps:** Video not viewed; Seat-sharing implementation not confirmed in code; Whether the Devpost-listed prize text applies beyond the generic rubric is unknown
Sources: https://devpost.com/software/encore-vzilag, https://github.com/zhaojzn/encore-demo-app (evidence file README), https://stormhacks2025.devpost.com/

---

### FretNot
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** IEEE SFU Prize Track

**What it is:** A clip-on guitar attachment with laser diodes driven by an ESP32 that lights the fret and string positions of a chord, controlled over Bluetooth from a React web app. The app can read a song sheet with OCR and step through lyrics showing each chord.
**Problem / user:** Beginner guitar learners who need help memorizing chord fingerings; the device acts as training wheels.

**Features**
- Laser chord projection — ESP32 maps each chord to a matrix of laser diode GPIOs and lights them when the chord is received. *[shown_working]*
- Bluetooth control — Browser Web Bluetooth writes chord names to a BLE characteristic on the ESP32. *[shown_working]*
- Lyrics and chord performance mode — Web app steps through song lyrics, sending the matching chord with each line. *[claimed]*
- OCR song parsing — Tesseract reads an uploaded image/PDF of lyrics with chords; README admits it is fitted to one song and format. *[claimed]*
- Custom 3D-printed mount — Enclosure designed in Onshape to clip onto the guitar. *[shown_working]*
- Chord set — Only C, E, F and Fm supported due to ESP32 pin limits. *[shown_working]*

**Flow:** Clip device to guitar and power the ESP32 → Open the web app and connect via Bluetooth → Pick a chord or upload a song sheet → Lasers show the chord as lyrics advance

**Prompt:** IEEE SFU Prize Track: "Awarded to the project that best applies electrical, electronic, or computing principles to solve a real-world problem." Prize: Raspberry Pi kit.
**Fit (explicit):** Electronics and BLE firmware solve a learning problem; README states it won the IEEE award. Uses ESP32, laser diodes and custom enclosure.  *(targeted: IEEE SFU Prize Track)*
**AI:** No ML; Tesseract OCR reads song sheets (team chose OCR over machine learning). ML proposed for varied formats later.
**Architecture:** React/Vite/TypeScript web app with OCR; Web Bluetooth to an ESP32 Arduino sketch exposing a chord characteristic; laser diodes wired to GPIO; 3D-printed enclosure.
**Novelty:** Physical laser guide on the fretboard linked to song lyrics, rather than an on-screen chord chart.
**Scope:** small · working: README embeds a video demo; about 580 LOC; four chords working for one preview song. · polish: Hardware printed enclosure; documented ESP32 pin matrix; no tests; OCR limited.
**Claims:** Complete product built in 24 hours; first hackathon for three members.
**Gaps:** Video not viewed; Devpost lists chords C, E, F, Fm; README does not list them
Sources: https://devpost.com/software/fretnot, https://github.com/doruphin/fretnot (evidence file README), https://stormhacks2025.devpost.com/

---

### GANPI
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Safe Software Best Modern C++

**What it is:** A C++17 command-line tool that sends plain-English requests to the Gemini API and turns them into shell commands, with preview, confirmation prompts and an interactive mode. A Next.js web interface also exists on Vercel.
**Problem / user:** Terminal beginners and people tired of switching between a terminal and an AI assistant.

**Features**
- Natural language to shell command — Gemini converts English requests into shell commands via libcurl and nlohmann/json. *[claimed]*
- Command preview and confirmation — Shows the command before running and asks before risky operations. *[claimed]*
- Dangerous-command filtering — README: sanitization and detection of harmful commands, conservative defaults. *[claimed]*
- Interactive chat mode — --interactive flag for ongoing conversation with the terminal. *[claimed]*
- Config via API key file — Prompts for Gemini key on first run, saved in a home config file. *[claimed]*
- Web interface — Next.js site deployed at Vercel; page lists code generation and explanations. *[claimed]*

**Flow:** Build with CMake and set a Gemini key → Run ganpi with a request or --interactive → Review the generated command → Confirm to execute

**Prompt:** Safe Software Best Modern C++: rewards clean, modern, efficient C++ on real problems; judged on interface design, correctness and safety (RAII, no raw pointers), performance.
**Fit (explicit):** Core CLI is C++17 with CMake and tests; README stresses C++ speed and safety checks. Page says it won the Best Modern C++ category; adherence to RAII not verified.  *(targeted: Safe Software Best Modern C++)*
**Sponsor tools:** Google Gemini API (Translating natural language requests into shell commands, core)
**AI:** Gemini (gemini-pro per README config) prompted to return shell commands for plain-English requests; no retrieval or agents described.
**Architecture:** C++17 CLI (src, include, test) calling Gemini over libcurl; separate Next.js web UI on Vercel; second repo GANPI-LOCUS listed.
**Novelty:** Natural-language shell helper written in C++ instead of Python or JS, targeting the C++ prize.
**Scope:** small · working: About 1,400 LOC with tests and a build script; Vercel demo link; README has many usage examples. · polish: Polished README with templated sections (placeholder clone URL); no video.
**Claims:** Calls itself a revolutionary CLI tool (README).
**Gaps:** Devpost describes a code-generation assistant more broadly than the README CLI; Second repo GANPI-LOCUS not read; Web interface not opened
Sources: https://devpost.com/software/ganpi, https://github.com/chdrPE/GANPI (evidence file README), https://stormhacks2025.devpost.com/

---

### GemiDice
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of .Tech

**What it is:** A solo Dungeons-and-Dragons-style text adventure where Gemini plays dungeon master. The player types any action, Gemini asks for a dice roll, outcomes affect a health bar, and replies can be read aloud with ElevenLabs. Themed backgrounds change with the scene; game state can be saved and loaded.
**Problem / user:** Solo players who want a free-form story game; the page states no explicit problem, only a Zork-meets-D&D idea.

**Features**
- Free-text story actions — Player types any idea; Gemini responds as dungeon master within the story world *[shown_working]*
- Dice-roll mechanic — Gemini asks for a specific number roll per attempted action; bad rolls cost health *[shown_working]*
- Health bar — Tracks damage from unlucky rolls *[claimed]*
- Voice narration — Speaker icon plays Gemini output via ElevenLabs text-to-speech *[shown_working]*
- Themed scenes — Prompt-driven mood and layout changes with four backdrops: Desert, Forest Temple, Ale house, Cave *[shown_working]*
- Save and load state — Save button stores the current game, load returns to last save *[claimed]*

**Flow:** Open the hosted site → Read the opening scenario from Gemini → Type what you want to do → Roll the dice number requested → Read or listen to the outcome via speaker icon → Save progress and load later

**Prompt:** MLH prize: win a .Tech domain name (for life) to showcase and expand a project, with Blue Snowball mics for the team.
**Fit (explicit):** Hosted at a gemidice.tech domain (links.gemidice.tech) and the README declares the .Tech award.  *(targeted: [MLH] Best Use of .Tech)*
**Sponsor tools:** .Tech domain (Public hosting address for the game, supporting); ElevenLabs (TTS narration, supporting); Gemini API (Dungeon master LLM, core)
**AI:** Gemini acts as dungeon master via an initial story prompt and prompt-driven theming; ElevenLabs reads responses aloud.
**Architecture:** Flask backend calling Gemini and ElevenLabs, HTML/CSS/JS front end with static theme images; deployed on gunicorn.
**Novelty:** Zork-style open-ended input with real dice mechanics enforced through LLM prompting; team's first hackathon.
**Scope:** small · working: About 700 LOC Flask app; README says it is now unusable because the API subscription ended. · polish: Four themed backgrounds and screenshots; short README.
**Claims:** Winner of Best use of .Tech
**Gaps:** no video; live site no longer functional
Sources: https://devpost.com/software/anything-pxw2f5, https://github.com/roilee1101/stormhacks2025, https://stormhacks2025.devpost.com/

---

### GuardianEye
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** BluePrint Social Good Track

**What it is:** A home-safety monitoring prototype: a React dashboard shows camera feeds while a FastAPI backend uses vision models and a Gemini agent to flag falls, smoke or distress and send SMS alerts through Twilio to caregivers. Described as a prototype for elderly care.
**Problem / user:** Elderly people living alone and their caregivers or family; page cites falls as a leading cause of injury among seniors.

**Features**
- Live camera dashboard — React/TypeScript view of room feeds with hazard indicators and status. *[shown_working]*
- Incident analysis — Gemini 2.5 Flash via Strands returns JSON with incident, emergency level, summary and suggestion for frames. *[claimed]*
- Hazard detection — MediaPipe, YOLOv8 and OpenCV used for falls, smoke and unusual motion or inactivity. *[claimed]*
- SMS alerts — Twilio texts caregivers when an emergency is detected. *[claimed]*
- Camera status monitoring — Backend tracks feed health. *[claimed]*

**Flow:** Caregiver opens dashboard → Views camera for a room → System analyzes frames → Alert details appear and SMS is sent for high-level incidents

**Prompt:** BluePrint Social Good Track: "Awarded to the project that best demonstrates how technology can be used as a tool for positive change"; focus on equity, accessibility, community well-being.
**Fit (implied):** Aimed at elder safety and faster caregiver response; page frames fall statistics and family motivation. Link inferred from the topic.  *(targeted: BluePrint Social Good Track)*
**Sponsor tools:** Twilio (SMS emergency alerts, supporting); Google Gemini (Strands Agents / MCP) (Agentic incident reasoning on camera frames, core)
**AI:** Frames from webcam via MediaPipe go to Gemini 2.5 Flash through Strands Agents with a structured-JSON prompt; YOLOv8 and OpenCV add detection. Accuracy not measured.
**Architecture:** React/TypeScript/Tailwind client; FastAPI backend with Strands, google-genai, mediapipe, ultralytics, twilio; env-configured API keys.
**Novelty:** Uses an LLM agent for ambiguous-incident reasoning plus classic CV and SMS in one monitoring pipeline.
**Scope:** medium · working: About 3,800 LOC split frontend and backend, three screenshots; no demo or video. · polish: Clear README setup and sample output; no tests.
**Claims:** Working prototype showing real-time event tracking (no metrics).
**Gaps:** Camera-monitoring system: no consent, privacy or data-retention safeguards stated on page or README; No accuracy or false-alarm data
Sources: https://devpost.com/software/guardianeye, https://github.com/ryanraen/GuardianEye (evidence file README), https://stormhacks2025.devpost.com/

---

### Hello World Rube Goldberg (The StormHacks Experience)
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** CSSS Rube Goldberg Challenge

**What it is:** A deliberately over-complicated physical Rube Goldberg machine, built from cans, tape and Arduino electronics, whose only purpose is to end up printing "hello world". Submitted with a video; the team frames it as a tribute to StormHacks culture beyond software.
**Problem / user:** No real problem; a joke build for the hackathon community and the CSSS challenge judges, deliberately turning a trivial task into an absurdly elaborate chain.

**Features**
- Chain-reaction machine that ends in printing "hello world" — Physical contraption of cans and electronics driven by Arduino (C++); the page says it overcomplicates printing the phrase. *[claimed]*
- Hackathon-culture theme — Built to reference the whole StormHacks experience including electronics, not only programming; a video disclaimer notes the can props were empty. *[claimed]*

**Flow:** Watch the demo video / Google Drive link → Machine chain runs and finally prints "hello world"

**Prompt:** CSSS Rube Goldberg Challenge: award for the project that makes a simple task absurdly complex, an over-engineered build that still works.
**Fit (implied):** Turns the trivial task of printing "hello world" into a multi-stage physical chain using cans, tape and Arduino; the page names the prize as the one it won.  *(targeted: CSSS Rube Goldberg Challenge)*
**AI:** none
**Architecture:** Physical chain of mechanical stages (cans, tape) ending at an Arduino-controlled output that prints "hello world"; no software stack described beyond Arduino C++.
**Novelty:** Pure hardware joke project with no software product; a rare non-software entry that fits a humor-driven prize.
**Scope:** tiny · working: Devpost shows a video/Drive demo link; page text offers no technical description of the stages. · polish: Minimal writeup; humorous tone; no repo.
**Gaps:** No repo; Drive demo video not viewable; Number and type of machine stages not described
Sources: https://devpost.com/software/hello-world-rube-goldberg-the-stormhacks-experience (via Chrome page text), https://stormhacks2025.devpost.com/

---

### Hooray-For-Huawei
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Huawei Custom Challenge #2: Automatic Decision for Re-computation

**What it is:** A C++ heuristic algorithm for Huawei Challenge 2: given a computation graph, it returns an ordered list of nodes that minimizes execution time while staying under a peak-memory limit, choosing what to recompute.
**Problem / user:** Huawei challenge judges; the problem is deciding which operators to recompute in a DAG so peak memory stays within a target at lowest total time.

**Features**
- Near-optimal node ordering — Returns a vector of nodes ordered to minimize time while meeting the maximum peak-memory constraint. *[claimed]*
- Heuristic search algorithm — Described as an advanced heuristic in C++; README gives no algorithmic detail; repo has src/include/data dirs with sample inputs. *[unclear]*
- Validity-preserving solution — Team says the hard part was runtime needed to produce a still-valid schedule. *[claimed]*

**Flow:** Build the C++ program → Feed it a challenge graph input file from data/ → Read the output ordered node list

**Prompt:** Huawei Challenge 2: design an algorithm ordering operator execution in an AI model under a memory limit, with optional recomputation, to minimize total computation time; judged on efficiency, creativity and rigor.
**Fit (explicit):** Directly implements the challenge: outputs a node order minimizing time under the peak-memory ceiling using a C++ heuristic.  *(targeted: Huawei Custom Challenge #2: Automatic Decision for Re-computation)*
**Sponsor tools:** Huawei re-computation challenge problem/data (Problem definition and input graphs the algorithm solves, core)
**AI:** none
**Architecture:** Single C++ program (src + include) reading challenge graph files from a data folder and emitting a node order; no services.
**Novelty:** Algorithmic submission with no UI; competes on solution quality rather than product features.
**Scope:** small · working: Repo has about 955 LOC of C++ and sample data; no benchmarks or results reported. · polish: README is the Devpost template text only; no usage instructions.
**Claims:** Returns a good solution to the problem (no numbers given)
**Gaps:** No benchmark numbers; Algorithm internals not documented; Full Huawei brief is an external doc, not read
Sources: https://devpost.com/software/hooray-for-huawei, https://github.com/Arnice123/Stormhacks-Hooray-For-Huawei (evidence README), https://stormhacks2025.devpost.com/

---

### IntervU
*StormHacks StormHacks 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Finalists

**What it is:** An AI mock-interview web app: the user uploads a resume and pastes a job description, then practices tailored behavioural questions and coding problems with a raccoon-mascot voice interviewer, getting hints, instant feedback and a final hireability report.
**Problem / user:** Software-engineering co-op and job seekers who cannot get enough mock interviews from friends or coaches and find paid mock-interview tools costly or limited.

**Features**
- Resume and job-description tailoring — Gemini reads the uploaded resume and job post; stored behavioural questions are customised by role, seniority and background. *[shown_working]*
- Voice interview — Browser mic input transcribed by OpenAI Whisper; interviewer replies spoken via ElevenLabs text-to-speech; camera/mic waiting room step. *[shown_working]*
- In-browser coding challenges — Monaco editor; Go backend runs Python or JavaScript remotely through a Piston service and checks output against test cases. *[shown_working]*
- Adaptive hints — Gemini gives progress-aware hints without revealing the answer. *[claimed]*
- Per-question feedback — Instant AI feedback on behavioural and technical answers. *[shown_working]*
- Final report — Hireability score with breakdown and improvement suggestions on a results page. *[shown_working]*
- Topic selection — User picks up to three interview categories (behavioural, technical, leadership) before starting. *[shown_working]*

**Flow:** Upload PDF resume and paste job description → Choose up to 3 topics → Set up camera and mic in waiting room → Read instructions → Interview with Ryan the Raccoon (voice + code editor) → Review scored results and tips

**Prompt:** Finalists: the StormHacks 2025 top-finalist prize; the page gives only the heading "The Finalists of StormHacks 2025!" with no criteria.
**Fit (none):** No stated prize target; Devpost shows Finalists/Winner labels without detail. General category entry.  *(targeted: Finalists)*
**Sponsor tools:** Google Gemini API (Question customisation, hints and feedback, core); ElevenLabs API (Spoken interviewer voice, core)
**AI:** Gemini customises questions, gives hints and scores answers (JSON outputs cleaned of markdown fences); OpenAI Whisper does speech-to-text; ElevenLabs does text-to-speech. Code correctness is checked by actual execution against tests.
**Architecture:** Next.js 15/React frontend (Vercel) with API routes for transcription and TTS; separate Go REST backend (handler, service, repository layers) on Render with MongoDB; Piston executes submitted code.
**Novelty:** Combines resume-aware questions, voice interviewer and real code execution in one flow; separate Go backend plus Next frontend is more than typical for a weekend.
**Scope:** medium · working: Live site and hosted backend API listed, demo video, about 5.4k LOC frontend plus separate Go repo. · polish: Custom raccoon mascot art, mobile-first Tailwind layout, multi-step flow, README with setup.
**Claims:** First production Go API built by the team | Final report gives a hireability score
**Gaps:** Backend repo README not read; Frontend README names OpenAI/Whisper while Devpost credits Gemini for question logic; both recorded; Auth/accounts not implemented (next steps)
Sources: https://devpost.com/software/intervu-852wre, https://github.com/PaulP1406/IntervU_frontend (evidence README), https://stormhacks2025.devpost.com/

---

### LockedIn
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Charles Chang Institute of Entrepreneurship Prize Track

**What it is:** A cross-platform Electron desktop focus assistant: the user states a goal, then Gemini checks periodic screenshots against that goal while a webcam check flags looking away, firing gentle alerts and ending with a dashboard and motivational summary.
**Problem / user:** People, especially those with ADHD, who get pulled to distractions like short-video feeds and find timers or to-do lists lack real-time accountability.

**Features**
- Intention setting — User enters what they will work on and a session length (up to 60 minutes). *[shown_working]*
- Screenshot goal check — Periodic desktop screenshots go to Gemini 2.5 Flash, which judges whether activity matches the stated goal. *[shown_working]*
- Webcam attention tracking — Webcam frames analysed by AI to detect looking away, phone use or distraction. *[shown_working]*
- Drift alerts — Gentle notification or motivational message when focus is lost; window can be minimized while monitoring continues. *[shown_working]*
- Session tracking and dashboard — Tracks focused time; Streamlit dashboard over session logs for analytics and post-session summaries. *[claimed]*
- Planned: Pomodoro, ambient audio, study plans — Listed as next steps: focus/break cycles, lo-fi sounds, milestone study plans. *[planned]*

**Flow:** Open app and set session intention and duration → App starts webcam and screenshot monitoring → Receive alert if off-task or looking away → End session → View focused time, dashboard and motivational summary

**Prompt:** Charles Chang Institute of Entrepreneurship track: rewards clear market potential, sustainable business model and ability to scale beyond the hackathon, plus creativity, feasibility and impact.
**Fit (implied):** Packaged as a consumer productivity product with target segment (ADHD users), dashboard and planned premium-style features; no explicit business model on the page.  *(targeted: Charles Chang Institute of Entrepreneurship Prize Track)*
**Sponsor tools:** Google Gemini 2.5 Flash (Multimodal analysis of screenshots and webcam frames, core)
**AI:** Gemini 2.5 Flash multimodal calls on screenshots and webcam images, comparing activity to the user-stated goal and attention state to decide when to alert.
**Architecture:** Electron app (React 19, Vite, TypeScript) with main-process IPC capturing screens and webcam, calling Gemini; Electron Store persistence; session JSON logs read by a separate Streamlit dashboard.
**Novelty:** Combines goal-aware screen understanding with webcam gaze checks in one desktop agent; monitors the user themself, with README stating images are not saved permanently.
**Scope:** medium · working: Devpost claims a working MVP with no mock data; repo has about 4.4k LOC, build scripts for three OSes, demo video. · polish: Framer Motion UI, README with setup and privacy notes, dashboard.
**Claims:** Working MVP with no mock data | Screenshots processed in real time and not saved (README)
**Gaps:** No live demo; video not viewable; Webcam model detail beyond Gemini unconfirmed; Business model not stated
Sources: https://devpost.com/software/lockedin-09v51s, https://github.com/yood2/lockedin (evidence README), https://stormhacks2025.devpost.com/

---

### M.I.R.A
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Gemini API

**What it is:** A desktop time-tracking assistant that logs active app, window title and idle time with a native C++ agent, analyzes periodic screenshots with Gemini, and shows a dashboard. A global shortcut opens a voice or text companion that answers questions about your workday.
**Problem / user:** Computer workers who finish long screen sessions unsure what they accomplished and find to-do lists and time-blocking inaccurate.

**Features**
- Native activity logger — C++ tracker writes app, window title, timestamp and idle seconds to a JSONL file; Windows and macOS builds *[claimed]*
- Screenshot analysis — Python script posts periodic screenshots to Django endpoint that calls Gemini for semantic context *[claimed]*
- Dashboard — Electron+React app with charts, daily timeline, per-app usage and session stats from Django dashboard endpoint *[shown_working]*
- Voice companion — ElevenLabs speech-to-speech mode answers what you worked on or helps when stuck *[claimed]*
- Text companion — Reads current screen and gives context tips such as debugging hints *[claimed]*
- Global shortcut toggle — Switches assistant between voice and text modes *[claimed]*
- Local-first data — Activity data kept in local files rather than cloud storage *[claimed]*

**Flow:** Run C++ tracker and Django backend → Mira logs activity quietly → Press global shortcut to talk or type to the companion → Ask about past work or focus time → Open dashboard for timelines and app usage

**Prompt:** MLH prize encouraging AI-powered apps built on the Gemini API, such as advice chatbots, summarizers and creative generators; prize mechanical keyboards.
**Fit (implied):** Gemini analyzes screenshots to extract semantic work context feeding the timeline and assistant.  *(targeted: [MLH] Best Use of Gemini API)*
**Sponsor tools:** Gemini API (Screenshot analysis endpoint, core); ElevenLabs (Voice companion, supporting)
**AI:** Gemini interprets periodic screenshots to extract what the user is doing; ElevenLabs provides speech interaction with local context. Exact prompts not shown.
**Architecture:** C++ tracker to JSONL, Django backend with analytics and Gemini screenshot endpoint, Electron/React dashboard polling the dashboard API, ElevenLabs module in Python.
**Novelty:** Three-language stack with native OS tracker plus screenshot-aware voice assistant, built in under 24 hours.
**Scope:** large · working: About 13,700 LOC, 195 files, runbook and integration docs; dashboard merges live data over mock data. · polish: Radix/shadcn UI, five screenshots, runbook docs, some tests.
**Claims:** Functional prototype in under 24 hours | Data stays local
**Gaps:** no video; local-first claim vs cloud AI unexplained
Sources: https://devpost.com/software/m-i-r-a, https://github.com/irvincardoza/stormhacks2025, https://stormhacks2025.devpost.com/

---

### Mapd
*StormHacks StormHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Finalists; Winner United Nations Sustainable Development Goals Enactus Challenge; Winner Best Design; Finalists; Best Design; United Nations Sustainable Development Goals Enactus Challenge

**What it is:** A Vancouver map platform that overlays City of Vancouver development permits with nearby amenities (schools, parks, transit, libraries and more) and uses OpenAI to write plain-language, scored impact analyses for each development.
**Problem / user:** Residents, planners and developers who see new construction and cannot easily tell how it affects the surrounding community, because the public data is fragmented.

**Features**
- Interactive permit map — Mapbox GL map with permit markers/clusters, popups, amenity markers and Vancouver neighbourhood boundary overlays. *[shown_working]*
- Address or pin start — User drops a pin or pastes a permit address to begin an analysis (Devpost). *[claimed]*
- AI impact reports — GPT-4 scores each permit from -10 to +10 across 9 infrastructure categories with estimates such as enrollment change. *[shown_working]*
- Amenity enrichment — Scripts add nearby amenities to permits by Haversine distance within a configurable radius. *[shown_working]*
- Filtering and search — Permits filtered by coordinates, distance, project value and property use with pagination. *[shown_working]*
- Hypothetical report endpoint — POST endpoint generates an impact report for custom, non-permit data. *[shown_working]*
- Edge caching — Cloudflare Worker proxies GET requests with a 5-minute cache. *[shown_working]*
- Missing-data explanations — UI states why a dataset is missing rather than failing silently. *[claimed]*

**Flow:** Open mapd.tech landing page → Browse permits on the map or paste an address → Click a development to see details and nearby amenities → Open the AI impact brief with scores and cited data → Filter by value or property use

**Prompt:** UN SDG Enactus Challenge: scalable solutions for one or more of the 17 UN Sustainable Development Goals, judged on front end, back end, design, originality and fit to the chosen goal. Best Design: UX, visual appeal, accessibility.
**Fit (implied):** Frames urban-development transparency for communities (sustainable cities); minimal map UI served Best Design. Page does not name the specific SDG.  *(targeted: United Nations Sustainable Development Goals Enactus Challenge, Best Design, Finalists)*
**AI:** OpenAI GPT-4 generates per-permit impact analysis and numeric scores from structured permit and amenity fields; results are precomputed by script and cached; Devpost also mentions embeddings and fuzzy matching for entity linking.
**Architecture:** React/Vite/Mapbox frontend on Vercel, Cloudflare Worker cache, FastAPI backend with MongoDB (Docker, DigitalOcean); batch scripts ingest Vancouver open data, enrich with amenities and generate reports.
**Novelty:** Precomputes LLM impact reports over real municipal open data with numeric per-category scoring, rather than a live chat over a map.
**Scope:** large · working: Live site mapd.tech, Vimeo video, about 15.8k LOC across frontend, backend and edge worker, CI workflow, Docker. · polish: shadcn/ui and Tailwind design, logo, detailed README with API table and architecture diagram.
**Claims:** Impact brief appears in seconds | Tracks 9 infrastructure categories | Scores range -10 to +10
**Gaps:** Placement conflict: README says Overall Winner, Best Design and 2nd place UN SDG Enactus; Devpost shows ambiguous Winner/Finalists labels. Queue lists Finalists, Best Design, UN SDG Enactus; Devpost describes address paste and Vancouver-wide fuzzy matching; README documents permit-centric map; feature list merges both; Specific SDG not named
Sources: https://devpost.com/software/mapd-urban-development-intelligence, https://github.com/LMSAIH/StormHacks2025 (evidence README), https://stormhacks2025.devpost.com/

---

### Music March
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Huawei Custom Challenge #1: Interactive Landscape Graphics

**What it is:** A real-time 3D audio visualizer: system audio goes through an FFT, split into bass, mid and treble, and those values raise the heights of procedurally generated, ray-marched fractal terrain the viewer can fly around in.
**Problem / user:** Electronic music fans and DJs wanting vivid background visuals; the team says it came from interest in graphics and electronic music rather than a stated problem.

**Features**
- Audio-reactive terrain — FFT output aggregated into bass, mid and treble coefficients passed to the shader to amplify hill heights. *[shown_working]*
- Procedural infinite terrain — Fractal Brownian motion height field generated in a GLSL fragment shader, extended endlessly. *[shown_working]*
- Ray marching renderer — Fragment shader ray marches the scene in real time with optimizations. *[shown_working]*
- Free navigation — User moves through the world, viewing terrain up close or far away. *[claimed]*
- Rule-based colouring — Terrain coloured by rules on height. *[claimed]*
- Performance gain — Frame rate raised from about 3 fps to about 60 fps on laptops versus the Huawei baseline (team claim). *[claimed]*

**Flow:** Play music on the computer → Launch the C++/SDL3 app → Watch terrain heights respond to bass, mid and treble → Fly through the landscape

**Prompt:** Huawei Challenge 1: build a real-time interactive app rendering infinite procedural terrain, pushing ray-marching limits, exploring new math and optimizing performance.
**Fit (explicit):** Started from Huawei ray-marching shader template, rewrote and optimized it, and added audio-driven procedural terrain.  *(targeted: Huawei Custom Challenge #1: Interactive Landscape Graphics)*
**Sponsor tools:** Huawei ray-marching terrain template (Starting shader/SDL3 implementation that was optimized and extended, core)
**AI:** none
**Architecture:** C++ with SDL3 for window, render pipeline and audio capture; FFTW3 for frequency analysis; band values uploaded to GPU buffer; GLSL fragment shader ray marches fBm terrain.
**Novelty:** Ties spectrum bands directly to a ray-marched height field instead of the typical 2D visualizer; pairs the challenge template with audio input.
**Scope:** small · working: Repo with about 2.3k LOC and a screenshot of the running visualizer; no video. · polish: README is two sentences and an image; no setup steps.
**Claims:** At least 20x frame-rate improvement, about 3 to 60 fps
**Gaps:** No demo video; Devpost slug "the ray marching band" differs from queue name Music March; Huawei brief doc not read
Sources: https://devpost.com/software/the-ray-marching-band, https://github.com/ErykHalicki/ray_marcher (evidence README), https://stormhacks2025.devpost.com/

---

### Optimized Ray-marching algorithm (SphericalTrace)
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Huawei Custom Challenge #1: Interactive Landscape Graphics

**What it is:** A solo set of GLSL shader optimizations for Huawei's heightfield terrain ray marcher: distance-based detail, K-Lipschitz-bounded sphere tracing, an early height cutoff and the Illinois root-finding method, with scripts that measure step-count savings.
**Problem / user:** Huawei challenge judges and graphics readers: render procedural fBm terrain faster in real time without losing visual quality.

**Features**
- Distance-based level of detail — Mesh/noise octaves reduced with camera distance so fine high-frequency noise is skipped far away. *[shown_working]*
- K-Lipschitz sphere tracing — Distance bound derived from the fBm parameters lets rays take adaptive larger steps. *[shown_working]*
- Height cutoff — Rays end once above the maximum possible terrain height, speeding sky pixels. *[shown_working]*
- Illinois method hit refinement — Root finding reduces small steps near the surface; windows without a hit are skipped. *[shown_working]*
- Grazing-angle handling — Sign-change search over a larger window inspired by bisection. *[claimed]*
- Performance analysis scripts — Python scripts count ray-marching steps and compare baseline versus optimized renders. *[shown_working]*

**Flow:** Load the GLSL shaders into a graphics host (Huawei template) → Tune terrain parameters in support_functions.glsl → Run the Python script to compare step counts and images

**Prompt:** Huawei Challenge 1: build a real-time interactive app rendering infinite procedural terrain, pushing ray-marching limits, with new math and performance work.
**Fit (explicit):** README states it is the solo winning submission; improves the provided template with sphere tracing, LOD and root finding, and reports reduced steps.  *(targeted: Huawei Custom Challenge #1: Interactive Landscape Graphics)*
**Sponsor tools:** Huawei ray-marching terrain template (Baseline shaders improved by the project, core)
**AI:** none
**Architecture:** GLSL shaders (main sphere-traced ray march plus support-function include) layered over Huawei template, with Python analysis and image-compare utilities and saved baseline/optimized renders.
**Novelty:** Math-driven optimization (Lipschitz bound, Illinois method) by one person rather than a new app; comparison images and step-count scripts back the claims.
**Scope:** tiny · working: Repo has before/after render folders and analysis scripts; about 49 LOC of own code beyond the template. · polish: Short README with results list; no video.
**Claims:** Total step count reduced 37.8% | FPS from 10 to 17 on author machine (README) | Frame time 100 ms to 60 ms | Memory 7.5 to 6 MB
**Gaps:** No video; LOC estimate counts only a few non-template files
Sources: https://devpost.com/software/optimized-procedural-heightfield-rendering, https://github.com/markharmon868/SphericalTrace (evidence README), https://stormhacks2025.devpost.com/

---

### Punchly
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** ColorStack Most Portable Project

**What it is:** A digital punch-card loyalty system for small shops: customers tap an NFC tag at the counter, which opens a React Native app and adds a stamp, while merchants use a Flask web dashboard to see stats, search customers and manage stamps and redemptions.
**Problem / user:** Small merchants whose paper punch cards get lost and give no analytics, and customers who dislike slow or insecure QR-code loyalty flows.

**Features**
- NFC tap check-in — Tag deep link opens the app and POST /api/mobile/scan validates a signature, upserts the reward record and returns progress. *[shown_working]*
- Customer wallet — Expo app with Supabase email login, list of cards, card detail and merchants to add; progress bars. *[shown_working]*
- Merchant dashboard — Flask web UI with KPIs, customer search, manual stamping, redemption tracking and analytics; bcrypt login with session cookies. *[shown_working]*
- Tag replay protection — Signature hash of program, points and timestamp with 24-hour expiry (hackathon version; production HMAC planned). *[claimed]*
- Stats API — GET /api/stats returns user, scan and near-reward counts. *[claimed]*
- Planned hardening — Port SQLite to Supabase, reward and tag CRUD, audit logs, stronger NFC security. *[planned]*

**Flow:** Customer signs up in the mobile app → Taps NFC tag at the counter → App opens and stamp is added with progress shown → Merchant logs into dashboard to review analytics and redeem rewards

**Prompt:** ColorStack Most Portable Project: the project best suited for on-the-go use such as phone apps, wearables or AR/VR.
**Fit (implied):** Mobile-first tap-to-stamp app using phone NFC and deep links, replacing physical cards; page names the award it won.  *(targeted: ColorStack Most Portable Project)*
**Sponsor tools:** Supabase (Customer email authentication in mobile app, supporting)
**AI:** none
**Architecture:** Expo/React Native app with Supabase auth and deep links from NFC tags to a Flask REST API backed by SQLite (users, companies, rewards); Flask server-rendered merchant dashboard.
**Novelty:** Hardware-adjacent tap flow with signed expiring tags plus both customer and merchant sides built in one weekend.
**Scope:** medium · working: Devpost says dashboard and functional mobile app done in 24 hours; repo about 6.8k LOC across mobile and server; no video. · polish: Banner image, README with problem, features and components; env example present.
**Claims:** Dashboard and mobile app completed in a 24-hour hackathon
**Gaps:** README claims offline sync, QR fallback and points programs not confirmed by Devpost; Devpost says SQLite not yet in Supabase; No demo or video
Sources: https://devpost.com/software/punchly, https://github.com/Aneel-Badesha/stormhacks2025 (evidence README), https://stormhacks2025.devpost.com/

---

### Qount
*StormHacks StormHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Solo Project

**What it is:** A pick-up-and-play iPhone memory game in SwiftUI: each round shows a random number of cubes briefly, hides them, and asks the player to guess how many there were. Inspired by a brain-training mini-game on Switch; built solo.
**Problem / user:** Casual players wanting a quick counting-memory game; no problem statement beyond recreating a game the author could not play.

**Features**
- Random cube rounds — Each round generates a random number of cubes on screen. *[shown_working]*
- Timed reveal then hide — Cubes are shown a few seconds then hidden before the guess. *[shown_working]*
- Count guess input — Player guesses the count, reportedly using hardware volume buttons for input (overriding them). *[claimed]*
- Planned: stats, local multiplayer, sound, harder puzzles — Listed as not yet built. *[planned]*

**Flow:** Start a round → Watch cubes appear then vanish → Enter the count guess → See result and play again

**Prompt:** Best Solo Project: most impressive project by one person; judges look for creativity, technical execution and a complete polished result built without a team.
**Fit (implied):** Built by one person; the page lists the award but does not tie features to it.  *(targeted: Best Solo Project)*
**AI:** none
**Architecture:** Native Swift/SwiftUI iOS app (Xcode project boxgame) with animation, state management and some AVFoundation; no backend.
**Novelty:** Small native game clone of a console mini-game; unusual in being a single-person iOS app with hardware-button input.
**Scope:** tiny · working: Author says it works mostly on iPhone and not reliably on iPad; repo about 1.2k LOC; no video. · polish: Six screenshots; no README.
**Claims:** Works majority of the time on iPhone, iPad support unreliable
**Gaps:** Repo has no README; feature list from Devpost only; Screenshot contents not described
Sources: https://devpost.com/software/qount, https://github.com/nevadoj/boxgame (evidence tree; no README), https://stormhacks2025.devpost.com/

---

### Racoon Works (Huawei CC 2)
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Huawei Custom Challenge #2: Automatic Decision for Re-computation

**What it is:** A C++ set of scheduling algorithms for Huawei Challenge 2 that choose execution order and which intermediate results to drop and recompute, to keep peak memory under the limit; approaches include greedy, heuristic, beam search and branch-and-bound.
**Problem / user:** Huawei challenge judges; ordering operators of an AI-model graph under memory limits with optional recomputation to minimize total time.

**Features**
- Naive topological scheduler — Baseline ordering following graph topology. *[claimed]*
- Greedy and heuristic schedulers — Heuristic variant implemented from recent recomputation research. *[claimed]*
- Beam search — Keeps several candidate schedules while exploring. *[claimed]*
- Branch-and-bound scheduling — Bounded branching to prune the search for optimal time. *[claimed]*
- Aggressive memory management — Drops intermediate results when memory is tight and recomputes nodes to lower the peak. *[claimed]*

**Flow:** Build with CMake → Run on input graphs in input/ → Read the scheduled order

**Prompt:** Huawei Challenge 2: algorithm ordering operator execution under memory limits with optional recomputation to minimize total computation time; judged on efficiency, creativity, rigor.
**Fit (explicit):** Implements several recomputation scheduling algorithms drawn from recent papers; page names the challenge as the one it won.  *(targeted: Huawei Custom Challenge #2: Automatic Decision for Re-computation)*
**Sponsor tools:** Huawei re-computation challenge problem/data (Problem definition and input graphs, core)
**AI:** none
**Architecture:** CMake C++ project (src, include, input graphs, docs folder with presentation material) offering multiple scheduler strategies.
**Novelty:** Compares several algorithm families grounded in recent papers rather than a single heuristic.
**Scope:** small · working: About 1.8k LOC C++ and sample inputs; team admits memory peak hit the ceiling and no metrics are reported. · polish: README only lists the challenge and contacts; docs dir exists.
**Claims:** Implements several recent research papers on recomputation
**Gaps:** MILP mentioned in meta description but not in body; No benchmark results; docs folder contents not read
Sources: https://devpost.com/software/racoon-works-hua-wei-cc-2, https://github.com/notwinston/Racoon_Works_Storm_Hacks2025 (evidence README), https://stormhacks2025.devpost.com/

---

### Rehabit
*StormHacks StormHacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Most Likely to Become a Startup

**What it is:** A browser-based home-rehab coach for stroke and injury recovery: the webcam tracks body keypoints during guided exercises, computes joint angles, range of motion and left/right symmetry, counts and grades reps, and has Gemini write a plain-English report (ElevenLabs for voice).
**Problem / user:** People doing physiotherapy at home after stroke or injury who lack objective feedback, and clinicians who want measurable progress data.

**Features**
- Pose tracking — MediaPipe Pose (33 landmarks) with OpenCV on webcam frames streamed to a Flask-SocketIO backend; live overlay and timers. *[shown_working]*
- Guided drills — Arms up, elbow flex/extend and sit-to-stand (README adds march in place) with exercise animations. *[shown_working]*
- Symmetry and ROM scores — Left versus right comparison and range-of-motion percent, with handling for a weaker side. *[shown_working]*
- Rep segmentation and quality — Max/min angle per rep; speed, control, trunk lean; Savitzky-Golay smoothing and outlier clipping. *[claimed]*
- Gemini session report — Structured session JSON sent to Gemini, which returns a readable progress note to share with a clinician. *[claimed]*
- Voice coaching — ElevenLabs converts AI feedback to spoken guidance (README). *[claimed]*
- CSV/JSON export — Session data exportable. *[claimed]*
- Planned: clinician dashboard, FHIR export, privacy features — Cohort views, PDF exports, gap alerts, on-device processing, consent logs, goniometer validation. *[planned]*

**Flow:** Open app in browser and allow webcam → Pick a guided drill → Follow along with live overlays and timers while reps are tracked → Review symmetry, ROM and rep quality → Get Gemini report to share with clinician

**Prompt:** Most Likely to Become a Startup: strongest potential to grow beyond the hackathon, with a clear market need, scalability and path to a viable business.
**Fit (implied):** Page lists clinician dashboard, commercial clinic pilot, HIPAA/PIPEDA alignment and reimbursement as next steps, positioning it as a health-tech product; no explicit link to the prize text.  *(targeted: Most Likely to Become a Startup)*
**Sponsor tools:** Google Gemini API (Turning session metrics into readable feedback report, core); ElevenLabs API (Voice coaching output, supporting)
**AI:** MediaPipe pose estimation for keypoints and geometric analysis for angles and symmetry; Gemini receives structured session JSON and writes the report; ElevenLabs speaks feedback.
**Architecture:** Browser JS captures webcam and streams frames over Socket.IO to a Flask backend running MediaPipe/OpenCV trackers and analytics; Gemini and ElevenLabs services produce report and audio; JSON/CSV export.
**Novelty:** Gives quantitative symmetry and ROM metrics from a plain webcam in the browser with no wearables, with an explicit one-side-weaker case.
**Scope:** medium · working: Repo with trackers, services, tests folder and about 2.5k LOC; Devpost screenshots; no clinical validation or video. · polish: README with architecture, exercise table and quickstart; five screenshots.
**Claims:** End-to-end flow from drills to generated report | No clinical validation yet; goniometer comparison planned
**Gaps:** Devpost lists three drills, README four (adds march in place); list merges both; No demo video or live link
Sources: https://devpost.com/software/rehabit-c093se, https://github.com/KR13H/Rehabit.git (evidence README), https://stormhacks2025.devpost.com/

---

### SFU Grad Map
*StormHacks StormHacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best Use of SFU Courses API

**What it is:** A web app that shows SFU course prerequisites as an interactive D3 dependency graph. Searching a course shows its description, prerequisites and equivalents, and Gemini converts messy prerequisite text from SFU course data into structured JSON.
**Problem / user:** SFU students who find the official goSFU course info unintuitive and must open many course outline pages to trace prerequisites, especially for upper-division courses.

**Features**
- Course search — Search shows description, prerequisites and equivalent courses. *[shown_working]*
- Dependency graph — D3.js graph with animated transitions; nodes expandable by searching a prerequisite from the current view. *[shown_working]*
- Hover details — Hovering a course node shows its description and prerequisites. *[shown_working]*
- AI prerequisite extraction — Gemini (flash) turns unstructured prerequisite text into organised JSON after a manual parser was abandoned. *[claimed]*
- Equivalency handling — Substitutable courses represented since equivalence depends on program. *[claimed]*
- Planned: accounts and degree tracking — Authentication, personalised progress, course-load recommendations, transcript integration. *[planned]*

**Flow:** Search a course on the site → See it and its prerequisites as a graph → Hover nodes for descriptions → Search a prerequisite to expand the graph

**Prompt:** Best Use of SFU Courses API: best usage of the API at api.sfucourses.com (only a one-line description on the prize page).
**Fit (implied):** Course search and prerequisite data drive the graph; page names SFU course outline data but does not detail the API calls.  *(targeted: Best Use of SFU Courses API)*
**Sponsor tools:** SFU Courses API (api.sfucourses.com) (Course descriptions and prerequisite text feeding the graph, core); Google Gemini API (Parsing prerequisite text to JSON, core)
**AI:** Gemini flash extracts structured prerequisite and equivalency data from free-text course descriptions; rate limits slowed multi-course processing.
**Architecture:** Next.js (JavaScript) app on Vercel using shadcn/aceternity UI, fetching SFU course data, calling Gemini via @google/genai, rendering relationships with D3.
**Novelty:** Turns scattered prerequisite prose into a navigable graph using LLM parsing, solving a real campus pain point.
**Scope:** small · working: Live Vercel demo link and about 1.9k LOC; Devpost calls it a functional prototype. · polish: Responsive UI with animations; README is the default create-next-app text; no video.
**Claims:** Fully functional prototype integrating Gemini and visual course relationships
**Gaps:** README is boilerplate so API use is inferred from Devpost and prize name; No video
Sources: https://devpost.com/software/sfu-grad-map, https://github.com/alexchen817/stormhacks2025-sfu-course-map (evidence README), https://stormhacks2025.devpost.com/

---

### SurvivalChess
*StormHacks StormHacks 2025 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Finalists; Best Game

**What it is:** A browser game mixing chess movement rules with timed survival: each round tiles holding pieces are marked for destruction and the player must move those pieces to safety before the timer ends, with endless rounds and two custom pieces (Stag and Trident).
**Problem / user:** Game players looking for a fast puzzle-survival twist on chess; no problem statement given.

**Features**
- Chess movement on small board — Pieces follow traditional chess move rules on a reduced board. *[shown_working]*
- Danger-marked tiles — At round start specific tiles are marked for destruction; pieces on them are lost unless moved in time. *[shown_working]*
- Timed endless rounds — Time limit per round; unlimited number of rounds. *[shown_working]*
- Custom Stag and Trident pieces — New pieces with their own movement options. *[claimed]*
- Planned extras — Larger danger areas, scoring database, power-ups, drag-and-drop, themes, sound. *[planned]*

**Flow:** Open the game on Vercel → Round begins and tiles get marked → Move endangered pieces off before time runs out → Next round continues

**Prompt:** Best Game: awarded to the most engaging, creative and well-designed game. Finalists: heading only, no criteria.
**Fit (implied):** A playable, original genre mix (chess plus survival) with custom pieces; README and page state the Best Game and winner labels.  *(targeted: Best Game, Finalists)*
**AI:** none
**Architecture:** TypeScript object-oriented game on PixiJS rendering, bundled with Vite, deployed to Vercel; client-only.
**Novelty:** Fuses turn-based chess rules with real-time pressure; custom Stag and Trident pieces extend the ruleset.
**Scope:** small · working: Live Vercel demo, MVP of core loop, about 1.6k LOC. · polish: Two screenshots and GIF; README just awards and team (names not recorded); no video.
**Claims:** MVP captured most of core game in the time limit
**Gaps:** Devpost labels Winner Best Game and Winner Finalists ambiguously; Stag/Trident move rules not described
Sources: https://devpost.com/software/survivalchess, https://github.com/jpg157/SurvivalChess_Stormhacks_2025 (evidence README), https://stormhacks2025.devpost.com/

---

### Track2Give
*StormHacks StormHacks 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Beginner; Most Likely to Become a Startup; United Nations Sustainable Development Goals Enactus Challenge

**What it is:** A web food-inventory tracker where users log items with expiry dates, see time remaining, get automatic expiry alerts and donation suggestions for soon-to-expire food. Screenshots also show a scan page, AI chat and a maps prototype.
**Problem / user:** Household users who forget what is in the fridge or pantry until it expires, causing food waste.

**Features**
- Inventory with expiry tracking — Add, edit, delete items with expiry dates; remaining shelf life computed by date arithmetic. *[shown_working]*
- Expiry alerts — Scheduled background tasks check dates and send notifications with real-time updates without refresh. *[claimed]*
- Donation suggestions — Suggests donation options for soon-to-expire items; one teammate built the donation logic. *[claimed]*
- User accounts — Passport.js login and sessions; each user linked to own inventory in MongoDB. *[shown_working]*
- Scan and AI chat pages — Screenshots show a scan page and AI chat (Gemini and Cloudinary listed); function not described. *[unclear]*
- Maps page — Shown only as a prototype sketch. *[planned]*
- Planned: OCR receipts, food-bank integration, mobile barcodes, donor leaderboard — Listed next steps. *[planned]*

**Flow:** Sign up or log in → View dashboard and food list with time to expiry → Add items (manual or scan page) → Receive expiry alerts and donation suggestions

**Prompt:** UN SDG Enactus: scalable solutions for the UN goals; Most Likely to Become a Startup: market need, scalability; Best Beginner: at least half the team first-time hackers.
**Fit (implied):** Targets food waste and donation (sustainability angle); page says it promotes donation and sustainability awareness. No explicit goal number or business model.  *(targeted: Best Beginner, Most Likely to Become a Startup, United Nations Sustainable Development Goals Enactus Challenge)*
**AI:** Gemini listed with an AI chat page screenshot; role not explained on the page. OCR expiry prediction is a future item.
**Architecture:** Node/Express app with EJS templates, MongoDB via Mongoose, Passport.js auth, scheduled jobs for expiry checks, Cloudinary and Gemini integrations; deployed on Render.
**Novelty:** Combines expiry tracking with donation redirection; several pages (scan, AI chat, maps) appear to be partial or prototype.
**Scope:** small · working: Live Render demo link; page calls it a fully functional inventory tracker; repo could not be read. · polish: Seven screenshots listed; no video.
**Claims:** Fully functional data-driven inventory tracker (team claim)
**Gaps:** Repo clone failed and GitHub/raw README unreachable (404); Gemini/scan/AI chat role unverified; Awards labelled Winner for three prizes without placement
Sources: https://devpost.com/software/track2give, https://stormhacks2025.devpost.com/

---

