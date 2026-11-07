# HackNC — HackNC 2025 (6 projects)

### Carolina Capital: OS Game About Youth Finance Management
*HackNC HackNC 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** HackNC Beginner - 1st Place [1st]

**What it is:** Browser game styled as a 90s desktop OS where a first-generation UNC student runs weekly life: banking, jobs, housing, courses, loans, a three-stock simulator and scam emails, with an advisor mascot. Win by reaching savings, credit and degree goals; lose by bankruptcy or zero happiness.
**Problem / user:** Incoming students making complex money decisions with no safe place to practice.

**Features**
- Retro desktop with apps — Icons open windows: browser with tabs, balance widget, calendar, degree tracker, goals *[shown_working]*
- Weekly simulation loop — Next Week applies salary, interest, rent, bills, loan drafts, market ticks and random events *[shown_working]*
- Credit and loans — Score moves with payments (+7 on time, -18 missed); APR tied to score; amortized loans *[shown_working]*
- Stock simulator — Three assets with order books and candlestick charts via Chart.js *[shown_working]*
- Jobs, housing and courses with prerequisites — Hiring requires housing and coursework *[shown_working]*
- Random events and scam emails — Inbox events change balances; clicking scams costs 25% of checking *[shown_working]*
- Advisor mascot and well-being meter — Tips every 10 s; happiness 0-150 drives losing *[shown_working]*
- Gemini use — Tag only; role unspecified *[unclear]*

**Flow:** Start with $10,000 and 600 credit score → Open apps to pick housing, job, courses → Press Next Week → Handle bills, events and scams → Reach savings, credit and degree goals or lose

**Prompt:** HackNC Beginner track 1st place (AirPods, retro keyboard or Polaroid bundle choice); judged on application/impact, functionality, creativity, technical complexity, presentation.
**Fit (implied):** Beginner-track entry built from vanilla HTML/CSS/JS with a finance literacy theme; page states the beginner placement.  *(targeted: HackNC Beginner - 1st Place)*
**AI:** Google Gemini is tagged on Devpost but neither page nor README describes its use; the README describes a scripted simulation.
**Architecture:** Single-page vanilla JS app: one gameState object (~1.5k lines), modular render functions per window, Chart.js and Luxon.
**Novelty:** Faithful desktop-OS metaphor with a rich economy model (credit, amortization, order books) built without frameworks.
**Scope:** small · working: README details mechanics; YouTube video; 2.6k lines in three code files; no hosted link. · polish: Draggable windows, ARIA roles, pixel art pass; no tests.
**Claims:** Built Win98-style desktop and state engine in one weekend
**Gaps:** Video not watched; Gemini role unknown
Sources: https://devpost.com/software/carolina-capital-os-game-about-youth-finance-management, https://github.com/j3ffreyl1u/HackNC-2025 (evidence file README), https://hacknc-2025.devpost.com/

---

### CuratePlate
*HackNC HackNC 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** HackNC Beginner - 3rd Place [3rd]

**What it is:** An iOS app where a diner photographs a restaurant menu, and it parses each dish, estimates nutrition and gives a 0-100 meal-value score tied to the user's body metrics and dietary restrictions. A bunny mascot voice explains nutrients aloud.
**Problem / user:** Budget-conscious college students eating out who want filling, relatively healthy and affordable choices and cannot easily judge nutrition per dollar from a menu.

**Features**
- Menu photo scanning — Camera capture with VisionKit text recognition; Gemini cleans and structures item names, descriptions and prices *[claimed]*
- Nutrition estimates — Gemini plus Nutritionix data estimate calories, protein, carbs, fat, fiber and sugar per dish *[claimed]*
- Meal Value score — 0-100 score weighing nutrient density against price, penalising excess sugar or unhealthy fat *[claimed]*
- Personalised profile — User enters height, weight, age, sex to estimate daily needs and sets dietary restrictions *[claimed]*
- Dietary flag detection — Marks vegetarian, vegan and gluten-free dishes from menu text *[claimed]*
- Tete nutrient voice assistant — Tapping a nutrient plays an ElevenLabs-voiced explanation of its benefits *[claimed]*

**Flow:** Create account and enter body metrics and restrictions → Open camera and photograph a menu → Backend parses items and estimates nutrition → Browse dishes ranked with personalised scores → Open a dish to see meal-value and nutrients → Ask the mascot about a nutrient and hear it

**Prompt:** HackNC Beginner track: teams self-select Beginner at submission and compete for 1st-3rd hardware prizes; the page gives no theme or judging criteria.
**Fit (explicit):** Team describes it as their first app and first API integration; open-ended track, so fit is simply a beginner-level working app.  *(targeted: HackNC Beginner)*
**Sponsor tools:** Gemini API (Menu parsing and nutrition estimation, core); ElevenLabs (Voice of the Tete mascot explaining nutrients, supporting)
**AI:** Gemini 2.5 Flash extracts structured menu items from images and estimates nutrition and a value score; Nutritionix supplies food data; ElevenLabs Multilingual v2 does streamed speech.
**Architecture:** SwiftUI iOS app captures images and calls a local FastAPI Python backend, which queries Gemini and Nutritionix and an ElevenLabs endpoint; JSON results return to the app.
**Novelty:** Combines per-dollar nutrition scoring with personal profile and a talking mascot; otherwise a standard vision-LLM-plus-nutrition-API stack.
**Scope:** small · working: Repo has iOS and FastAPI code (~2k LOC) and README usage; no demo video or live link. · polish: Custom font, hand-drawn graphics and mascot; no tests.
**Claims:** Meal Value score rates nutrition per dollar from 0 to 100 | Handles 50+ nutrients with spoken explanations
**Gaps:** No demo video; Dietary restriction list is limited per page
Sources: https://devpost.com/software/curateplate, evidence/hacknc-hacknc-2025-curateplate.json (README), https://hacknc-2025.devpost.com/

---

### EyeCode: Speak With Your Eyes!
*HackNC HackNC 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** HackNC Beginner - 2nd Place [2nd]

**What it is:** A webcam application that tracks eye blinks, treating short blinks as Morse dots and long ones as dashes, decodes them live into text and optionally speaks the text with ElevenLabs. It runs from a CLI or a Flask browser dashboard.
**Problem / user:** People with ALS, paralysis or stroke who cannot speak or type; the page says dedicated AAC devices cost thousands of dollars.

**Features**
- Blink detection — MediaPipe Face Mesh landmarks give an eye aspect ratio; dropping under a threshold counts as a blink, smoothed over frames *[shown_working]*
- Morse classification — Blink duration separates dots from dashes; pauses delimit letters and words *[shown_working]*
- Live decoding overlay — Camera feed shows EAR, current Morse sequence and decoded text *[shown_working]*
- Text-to-speech — After a pause of about two seconds the transcript is voiced through ElevenLabs *[claimed]*
- Web dashboard — Flask server streams MJPEG video with signal stats, clear button and browser audio playback *[shown_working]*
- Tunable parameters — CLI flags for EAR threshold, dot and dash durations, cooldowns, voice id, disabling TTS *[shown_working]*

**Flow:** Start the app in web or CLI mode → Face the webcam → Blink short or long to spell Morse symbols → Watch decoded text appear on the dashboard → Pause and hear the text spoken → Clear the buffer and continue

**Prompt:** HackNC Beginner track: self-selected beginner category with 1st-3rd hardware prizes; no theme or criteria given.
**Fit (implied):** Open beginner track; project is a small working accessibility tool built from off-the-shelf vision and speech components.  *(targeted: HackNC Beginner)*
**Sponsor tools:** ElevenLabs (Speaks decoded text aloud, supporting)
**AI:** MediaPipe Face Mesh landmark model feeds a rule-based EAR blink detector; ElevenLabs provides speech. No LLM.
**Architecture:** Python with OpenCV and MediaPipe in a multithreaded loop; Flask serves MJPEG stream, polled decoded text and TTS audio to an HTML/JS page.
**Novelty:** Zero-hardware Morse-by-blink AAC idea; README credits an earlier hackathon blink-to-text project as inspiration.
**Scope:** tiny · working: Small Python repo (~1.2k LOC) with CLI and Flask modes and an embedded demo video on Devpost. · polish: Detailed README flags and troubleshooting hints; no tests.
**Claims:** 90%+ blink detection accuracy at 30 FPS (no method given) | Replaces AAC devices costing $7,000-$15,000 at zero cost | 12+ tunable parameters
**Gaps:** Video not watched; Accuracy claim unverified
Sources: https://devpost.com/software/eyecode-speak-with-your-eyes, evidence/hacknc-hacknc-2025-eyecode-speak-with-your-eyes.json (README)

---

### InterviewArcade
*HackNC HackNC 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** HackNC General - 1st Place [1st]

**What it is:** A retro-arcade-styled mock technical interview site: the student picks a company or problem type, talks through an approach while coding in an editor, and Gemini grades both audio and code. Feedback comes as scores, written strengths and weaknesses, and an ElevenLabs voiceover.
**Problem / user:** Students preparing for internship technical interviews who need practice and feedback on both communication and coding.

**Features**
- Company or category selection — User chooses a company or question type from a stored question list *[claimed]*
- Interview session with code editor — Monaco-based editor plus microphone recording during the problem *[shown_working]*
- Chunked audio streaming — Audio is sent to the backend in chunks while the user speaks and merged at the end *[claimed]*
- Gemini evaluation — Audio, code and question go to Gemini, which returns JSON scores and feedback transcript *[claimed]*
- Case-by-case feedback page — Strengths and areas to improve for communication and coding, shown in columns *[claimed]*
- Spoken feedback — Feedback text turned into an MP3 by ElevenLabs and played back *[claimed]*
- Retro game theming — Pac-Man, Space Invaders and Breakout inspired UI and loading screen *[shown_working]*

**Flow:** Pick a company or question category → Start the interview → Talk through approach while writing code → Submit for evaluation → Read scored feedback → Listen to AI voiceover of feedback

**Prompt:** HackNC General track: open category, 1st-3rd hardware prizes plus MLH pins; no theme text.
**Fit (none):** Open-ended general track; entry is an education tool. Also uses Gemini and ElevenLabs, MLH sponsor tools, though no stated targeting.  *(targeted: HackNC General)*
**Sponsor tools:** Gemini API (Multimodal grading of audio and code, core); ElevenLabs (Voiceover of feedback, supporting)
**AI:** Gemini receives the combined audio, code and question and returns structured JSON scores and narrative feedback; ElevenLabs converts it to speech.
**Architecture:** React frontend (Monaco editor, GSAP) calls a FastAPI backend that stores audio chunks, queries Gemini and ElevenLabs, and serves question files.
**Novelty:** Grades spoken explanation alongside code rather than code only; arcade visual theme. Live AI conversation was dropped for time.
**Scope:** small · working: Frontend and backend repo (~2.8k LOC); README describes the full flow, but no video or live link on Devpost. · polish: Detailed retro UI with several themed screens; no tests.
**Gaps:** No demo video; Whether feedback worked end to end is not shown
Sources: https://devpost.com/software/interview-arcade, evidence/hacknc-hacknc-2025-interviewarcade.json (README)

---

### Localized
*HackNC HackNC 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** HackNC General - 2nd Place [2nd]; Capital One Best Personal Finance Hack

**What it is:** An iOS app for UNC students that surfaces a weekly rotating lineup of deals from Franklin Street businesses. Students claim one free coupon per week, unlock another by sharing, and redeem via dynamic QR codes; businesses publish offers and track redemptions.
**Problem / user:** Chapel Hill students on a budget and independent local businesses losing foot traffic, with delivery apps taking large cuts and rewards programs favouring chains.

**Features**
- Weekly rotating Lineup — Users browse a changing set of deals from restaurants, shops and studios *[shown_working]*
- Coupon claiming with share unlock — One free coupon per week, a second after sharing the app *[claimed]*
- QR redemption — App generates dynamic QR codes that the business scans and the backend verifies *[shown_working]*
- Business dashboard — Businesses create and manage offers and see redemptions in real time *[shown_working]*
- Map view — MapKit pins with expandable business info *[shown_working]*
- Auth and 17-route API — FastAPI with JWT login, separate user and business flows, S3 image storage *[shown_working]*

**Flow:** Sign up as student or business → Student browses weekly Lineup or map → Claims a coupon, shares for a second → Shows QR code in store → Business scans to redeem → Business views redemption data

**Prompt:** General track is open-ended with 1st-3rd prizes. Capital One Best Personal Finance Hack: $250 per member for the best personal-finance project; the page gives no further brief.
**Fit (implied):** Student savings angle (free weekly coupons for budget-limited students) is the only finance link; no Capital One API is mentioned.  *(targeted: HackNC General, Capital One Best Personal Finance Hack)*
**AI:** none
**Architecture:** SwiftUI MVVM iOS app talks to FastAPI+SQLModel on Vercel, with PostgreSQL on AWS RDS, JWT auth and S3 file storage; QR codes are generated and verified server side.
**Novelty:** Two-sided marketplace (student and business personas) with real deployed backend and AWS infrastructure, unusually full-stack for a hackathon; no AI.
**Scope:** medium · working: Deployed API docs, ~3.5k LOC iOS and backend, simulator screenshots in README, demo video on Devpost. · polish: Liquid-glass icons and custom branding; no tests.
**Claims:** 17 API routes across six service categories | Plans a pilot with 10-15 Franklin Street businesses
**Gaps:** Backend code in separate repo not read; No usage metrics
Sources: https://devpost.com/software/localized, evidence/hacknc-hacknc-2025-localized.json (README), https://hacknc-2025.devpost.com/

---

### SentiFrame
*HackNC HackNC 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** HackNC General - 3rd Place [3rd]

**What it is:** A pipeline that streams video and audio from Ray-Ban Meta glasses to a Python backend, scores facial emotion and transcribes speech in real time, then uses Gemini to summarise and ElevenLabs to read coaching feedback aloud. A React dashboard shows the results.
**Problem / user:** Communicators in healthcare, education or customer service who lack awareness of audience emotional tone; no specific user persona is named.

**Features**
- Glasses video capture workaround — Phone mirrored to desktop, screen-captured and exposed as a virtual webcam since Meta offers no live API *[claimed]*
- Facial emotion scoring — OpenCV frames sent to a RunPod-hosted expression model giving seven emotion scores from 0 to 1 *[claimed]*
- Live transcription — PyAudio mic stream to Deepgram WebSocket for sub-second speech-to-text *[claimed]*
- Session logging — Transcript and emotion data stored in Firebase Firestore *[claimed]*
- Gemini summaries and coaching — Gemini 2.5 Flash extracts key moments, tone and end-of-session coaching *[claimed]*
- Emotion-matched spoken summary — ElevenLabs voice profile chosen by emotional tone reads the summary *[claimed]*
- Dashboard — React/Recharts UI with engagement peaks and emotional consistency metrics *[claimed]*

**Flow:** Wear glasses and start a live session → Video and audio stream to backend → Emotions and transcript logged live → Dashboard displays sentiment trends → End session to receive coaching summary → Hear it read in a tone-matched voice

**Prompt:** HackNC General track: open-ended, with 1st-3rd hardware prizes and MLH pins; no theme.
**Fit (none):** Open track; the entry is a multi-sensor wearable AI pipeline.  *(targeted: HackNC General)*
**Sponsor tools:** Gemini API (Summaries and tonality inference, core); ElevenLabs (Tone-selected spoken summaries, supporting)
**AI:** Custom facial expression model on RunPod for emotion vectors, Deepgram for speech-to-text, Gemini 2.5 Flash for summarisation, ElevenLabs for voice.
**Architecture:** Multithreaded async Python backend ingests virtual-camera frames and mic audio, calls RunPod and Deepgram, logs to Firestore, calls Gemini and ElevenLabs; React/TypeScript dashboard reads logs.
**Novelty:** Uses smart glasses as sensor despite no developer API, via screen-capture virtual camera; combines vision, audio and LLM coaching.
**Scope:** medium · working: Page describes a working end-to-end pipeline and embeds a demo video; no repo or measurements. · polish: Dashboard stack listed; no repo to check.
**Claims:** Sub-second transcription | Targets end-to-end lag under about 2 seconds
**Gaps:** No repository linked; Video not watched; No performance numbers
Sources: https://devpost.com/software/smartframe-m4695z, https://hacknc-2025.devpost.com/

---

