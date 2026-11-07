# UNIHACK — UNIHACK 2025 (4 projects)

### Crevo
*UNIHACK UNIHACK 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** First Timers' Prize

**What it is:** Crevo (Devpost title Ocuvid) is a web video editor that finds the active speaker, frames the video on them, and adds captions and translation. It works on live recordings and on uploaded footage, outputting a single MP4 and an .srt.
**Problem / user:** Creators, podcasters, educators and businesses who spend hours manually cutting multi-speaker video, aligning subtitles and smoothing transitions.

**Features**
- Live active-speaker framing — MediaPipe face and mouth-movement detection plus face position keeps the camera framed on whoever is talking. *[claimed]*
- Live transcription and translation — Vosk/Kaldi recognizer produces on-screen captions in real time and translates them to another language. *[claimed]*
- Upload mode auto-cut — Voice and face analysis labels speakers (pyannote) and crops/cuts the footage at the right moments into one MP4. *[claimed]*
- Download outputs — After live recording the user can download the edited video and a subtitle (.srt) file. *[claimed]*
- Multi-language subtitles — Captions and subtitles generated in multiple languages. *[claimed]*

**Flow:** Choose live recording or file upload → Live: record while the system frames the speaker and shows captions and translation → Upload: submit a file; speakers are detected by voice and face → System crops and assembles one MP4 → Download video and .srt

**Prompt:** UNIHACK 2025 (Imagination Hackathon, open-ended). The First Timer's Prize is listed by name only with no description; it is for first-time participants.
**Fit (none):** No stated targeting; a working ML video tool built by first-timers is the only link to the prize.  *(targeted: First Timers' Prize)*
**AI:** MediaPipe face/mouth landmarks for speaker detection, pyannote voice recognition for speaker labeling in upload mode, Vosk/Kaldi for speech-to-text; the team also says AI helped write some code.
**Architecture:** Flask backend with MoviePy and ML models exposed via ngrok; multiple Next.js frontends (live demo, live processing, upload) call it.
**Novelty:** Combines face, mouth and voice cues to pick the speaker, with different pipelines for live and uploaded video, rather than a simple caption tool.
**Scope:** small · working: Devpost claims working auto-frame and live captions; README is generic and shows no output. · polish: Figma design and screenshots; README is thin and generic.
**Claims:** Real-time captions and translation in multiple languages | Working auto-frame feature | No accuracy or latency metrics given
**Gaps:** Queue github_url null; repo found on Devpost page; README does not describe the product beyond a generic feature list; No official First Timer's prize text
Sources: https://devpost.com/software/ocuvid, https://raw.githubusercontent.com/fruitiecutiepie/unihack2025/HEAD/README.md, prompts_cache/unihack-2025.md

---

### Growth Garden
*UNIHACK UNIHACK 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** First place [1st]

**What it is:** A habit-building web app where an AI assistant named Bruce turns a user's goal into step-by-step tasks, and each completed task earns plants, mushrooms and items to decorate a calming 3D garden planet.
**Problem / user:** People trying to build better habits, where existing tools are domain-specific, only block apps or are overly prescriptive.

**Features**
- Bruce goal-to-routine assistant — User describes a habit or goal and the Langflow-hosted AI builds a routine of tasks, revisable any time *[shown_working]*
- Garden rewards — Completing tasks earns small plants, mushrooms and decor to place in the garden *[shown_working]*
- 3D garden world — Three.js planet with terrain generation and placement math written by the team *[shown_working]*
- Surface snapping — Objects orient and snap to the planet surface with tunable behavior *[shown_working]*
- Dynamic ambient audio and effects — Different ambient clips are selected, with custom sounds for task completion and mushroom placement *[claimed]*
- Calming visual design — Custom palette, shaders and assets chosen to relax *[claimed]*
- Fallback tasks — Preset tasks used when the AI service is down *[shown_working]*
- Desktop and mobile web access — Responsive Next.js site *[claimed]*

**Flow:** Tell Bruce your goal → Receive a task list → Complete tasks → Earn plants, mushrooms and items → Place and decorate the 3D garden

**Prompt:** Open-ended 'Imagination Hackathon' sponsored by Logitech; placement prizes (1st $5,000, 2nd $2,400, 3rd $1,200) with no per-prize rubric published.
**Fit (none):** Open-ended theme; project is a gamified habit tracker with a hand-built 3D reward world. No stated targeting. DataStax Langflow used, though Best Use of Datastax API prize is not listed as won.  *(targeted: First place)*
**Sponsor tools:** DataStax Langflow (Hosted AI flow generating tasks; went down after the event, fallback tasks used, core)
**AI:** Langflow-hosted LLM flow (underlying model not named) generates tailored habit tasks from the user's goal; preset fallback when unavailable.
**Architecture:** Next.js/React/TypeScript front end with Three.js 3D rendering and physics math; Langflow API calls for AI; Jenkins CI/CD with pnpm; assets from Poly Pizza, Freesound, Sketchfab.
**Novelty:** Pairs an AI coach with a custom 3D world with hand-written surface snapping and collision-style placement; half the team were first-timers.
**Scope:** medium · working: Live demo at growthgarden.anga.dev and 175-commit repo; Devpost update says Langflow service went down, leaving fallback tasks. · polish: Embedded video, 3D art, sound design; repo README is only the Next.js template.
**Claims:** Surface-snapping and ambient audio systems built from scratch
**Gaps:** README is Next.js template; evidence file missing; video not watched
Sources: https://devpost.com/software/growth-garden, https://github.com/AngaBlue/unihack-2025, https://unihack2025.devpost.com/

---

### Shuffl
*UNIHACK UNIHACK 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Second place [2nd]

**What it is:** An accessible hybrid card-game platform that connects a physical table, where cards are read by an Arduino NFC reader, with online players over WebSockets. It adds screen-reader support, voice input and a GPT-4o-mini advisor that coaches players, starting with poker.
**Problem / user:** In-person and remote players, newcomers and visually impaired players who are excluded from card games; braille cards are seen as dull.

**Features**
- Hybrid table play — Arduino Uno with PN532 NFC modules maps each card UID and posts to a Spring Boot REST endpoint so physical cards join online game *[shown_working]*
- Real-time multiplayer — STOMP over SockJS WebSockets with in-memory game state *[shown_working]*
- AI coach — 4o mini gives real-time game advice; first version told players to fold every hand until prompts were refined *[shown_working]*
- Voice input — Azure custom speech recognition replaced browser speech API that failed in Edge and Safari *[claimed]*
- Poker hand evaluation — Algorithm identifies winning hands *[claimed]*
- Accessibility — Screen reader support and claimed WCAG 3:1 contrast, tested with a visually impaired friend *[claimed]*
- LED status display — Screen and LEDs on hardware for debugging and monitoring *[claimed]*
- CI/CD and cloud deploy — Docker, GitHub Actions, Azure Container Apps with auto-scaling *[claimed]*

**Flow:** Join a game from the web app → Deal physical cards scanned by NFC readers → Online players see and act in the same game → Speak commands or read via screen reader → Ask the AI advisor for advice

**Prompt:** Open-ended 'Imagination Hackathon' sponsored by Logitech; placement prizes (1st $5,000, 2nd $2,400, 3rd $1,200) with no per-prize rubric published.
**Fit (none):** Open-ended event; project blends physical hardware, accessibility and AI coaching in a card game. No stated target prize.  *(targeted: Second place)*
**AI:** GPT-4o mini advisor tuned with prompts around game theory to suggest plays; Azure Speech SDK with custom-trained model for voice-to-text.
**Architecture:** Next.js 14 TypeScript client with stomp.js; Spring Boot Java server with in-memory state and REST endpoint; Arduino with PN532 NFC and LEDs; Azure Container Apps, Docker, GitHub Actions.
**Novelty:** Physical NFC cards bridged into an online game with accessibility focus; team did first soldering for hardware.
**Scope:** medium · working: Live site shuffl.monashcoding.com, video and hardware photos; poker evaluator claimed working. · polish: Player and dealer views, CI/CD and containerization; 108 Devpost likes; repo not readable.
**Claims:** Meets 3:1 WCAG contrast | Validated with a visually impaired tester
**Gaps:** repo fetch failed; video not watched
Sources: https://devpost.com/software/shuffl-4rzu3c, https://unihack2025.devpost.com/

---

### Weave
*UNIHACK UNIHACK 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Third place [3rd]

**What it is:** A virtual wardrobe app where users upload clothing photos, have backgrounds removed, drag items onto a mannequin or their own photo, and get an AI-generated try-on preview. Outfits can be saved to a lookbook and shared.
**Problem / user:** People who find trying clothes on tedious, such as those with injuries or mobility challenges, and anyone facing outfit decision fatigue.

**Features**
- Digital closet — Upload wardrobe photos stored on S3 with automatic background removal via AWS Lambda neural network *[shown_working]*
- Mannequin mix-and-match — Drag-and-drop clothes on a custom mannequin with proportion handling *[shown_working]*
- AI try-on preview — FashnAI API called once per garment, chaining outputs to layer several items on user's photo *[shown_working]*
- Lookbook and sharing — Save outfits, track past ones, share with friends for feedback *[claimed]*
- Shopping integration — Browse brand clothing and pair with closet items; Devpost lists it both as a feature and as coming soon *[planned]*
- Responsive UI — Works on mobile and desktop *[claimed]*

**Flow:** Upload clothing photos → Backgrounds removed and items added to closet → Drag items onto mannequin or upload own photo → AI renders preview layering garments → Save to lookbook and share

**Prompt:** Open-ended 'Imagination Hackathon' sponsored by Logitech; placement prizes (1st $5,000, 2nd $2,400, 3rd $1,200) with no per-prize rubric published.
**Fit (none):** Open-ended event; project is a practical AI try-on tool. No stated target prize.  *(targeted: Third place)*
**AI:** FashnAI virtual try-on API handles one clothing item per call, so the app chains calls iteratively; separate neural background removal on AWS Lambda.
**Architecture:** Next.js/React/Tailwind frontend, Go backend calling FashnAI, Lambda background removal, S3 image storage, Docker with Coolify deployment and CloudFormation.
**Novelty:** Works around the single-item API limit by sequential layering to dress a user photo with a full outfit.
**Scope:** medium · working: Live demo at unihack.jasondev.me; described as working end to end, no video. · polish: Responsive UI and cloud infrastructure; repo not readable here.
**Claims:** Minimal latency previews, no numbers | Faster rendering via preprocessing
**Gaps:** repo fetch failed; no video
Sources: https://devpost.com/software/weave-vn2xdk, https://unihack2025.devpost.com/

---

