# HackHarvard — HackHarvard 2025 (4 projects)

### Post Surgery Pillow (PSP)
*HackHarvard HackHarvard 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** 1st Best Overall Hack [1st]

**What it is:** Hospital pillow with embedded non-invasive sensors that streams patient vitals, scores each patient 0-100 with a weighted formula, ranks who needs a nurse first, and has Gemini write a clinical summary with interventions, shown on a dashboard of patient cards.
**Problem / user:** Nurses covering several critically ill ICU or post-surgery patients who lose minutes checking each manually and prioritize with incomplete information.

**Features**
- Sensor pillow tracking temperature, pressure, movement, heart rate and oxygen — Arduino-based hardware collects repeated readings for trend analysis; 3D-modeled sensor and head layout *[claimed]*
- Weighted 0-100 satisfaction score with risk levels from Critical to Stable — Multi-stage weighting; any parameter below 30 forces risk to at least High *[shown_working]*
- Priority ranking of patients — Formula (100 minus score) x 0.6 x risk multiplier plus critical penalty; worked ICU example ranks #1 with 300.85 *[shown_working]*
- Hidden-critical edge-case detection — Single failing vital (e.g. oxygen 25 with four normal vitals) is flagged Critical despite a decent average *[shown_working]*
- Gemini clinical summaries — Gemini 2.5 Flash writes diagnosis from vitals, nursing interventions, documentation reminders and an executive shift summary *[shown_working]*
- Dashboard with live patient cards — Cards update priority in real time via Node/Express backend and website *[claimed]*
- Post-quantum encrypted database — PQM4-based encryption layer on stored data *[claimed]*
- Edge inference with FFT features, ML and GNN — ARM Cortex-M4 feature extraction plus ML model and graph neural network *[claimed]*

**Flow:** Pillow sensors collect vitals continuously → Scoring algorithm assigns score, risk level and priority rank with edge-case checks → Gemini produces a clinical summary per patient → Dashboard patient cards show ranked priorities → Nurses use the executive summary for shift briefings

**Prompt:** Best Overall Hack: top hack of HackHarvard 2025 (theme 'Compile the Decade', 10th anniversary), judged on innovation/impact, technical complexity, functionality/usability, collaboration/learning; iPad Pro and Pencil for 1st; Switch 2 bundle for 2nd; Ray-Ban Meta glasses for 3rd.
**Fit (none):** Full-stack hardware plus ML plus LLM healthcare system; page does not mention the decade theme or a prize target.  *(targeted: Best Overall Hack)*
**AI:** Deterministic weighted scoring and priority formula for ranking; Gemini 2.5 Flash for natural-language clinical summaries; an ML model and GNN are listed for the processing layer.
**Architecture:** Sensor pillow (Arduino, Cortex-M4 edge features) sends readings to a Node/Express backend and database with PQM4 encryption; scoring service ranks patients; Gemini adds summaries; web dashboard renders patient cards.
**Novelty:** Pairs physical sensing hardware with a transparent triage formula and LLM summary, plus unusual security (post-quantum) and edge-ML claims for a hackathon healthcare project.
**Scope:** medium · working: Page reports tests on 9 simulated patients, under 2 s per analysis, a worked example; repo could not be cloned or read. · polish: Detailed writeup with formulas and examples; no video or live link; database stated inconsistently (PostgreSQL vs MongoDB).
**Claims:** 100% edge-case detection on a small test set | 9 test patients, 3 critical cases correctly prioritized | Under 2 seconds analysis per patient | Post-quantum encrypted storage
**Gaps:** Repo clone failed and GitHub page was not fetchable; README unread; No demo video link
Sources: https://devpost.com/software/post-surgery-pillow-psp, https://hackharvard-2025.devpost.com/

---

### ResQme
*HackHarvard HackHarvard 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 2nd Best Overall Hack [2nd]

**What it is:** Disaster-communication system: ESP32 devices with GPS, OLED, buzzer and a button form a self-healing mesh with one master node that hosts a Wi-Fi access point, plus an Expo mobile app and a Next.js admin map console backed by Supabase.
**Problem / user:** Residents and rescue teams in disaster zones when cell towers and internet fail, who still need to send SOS messages and status updates.

**Features**
- Offline ESP32 mesh messaging — PainlessMesh nodes relay JSON packets; nodes join, leave and reconnect automatically *[claimed]*
- Master node serving a local Wi-Fi access point and webpage — Users connect to send messages or mark status; master distributes messages and logs over serial for cloud mirroring *[claimed]*
- Physical SOS button controls — Single click sends SOS, long press enters Wi-Fi pairing mode, triple click switches to mesh mode *[claimed]*
- GPS location, OLED feedback, buzzer and LEDs — TinyGPSPlus gives position; OLED and buzzer confirm actions in the field *[claimed]*
- React Native (Expo) user app — SOS screen, chat with responders, device status, profile and Supabase auth *[claimed]*
- Admin web console for responders — Next.js with Leaflet map of users and SOS markers, message center and broadcast, real-time Supabase subscriptions *[claimed]*
- Encryption, auto distress detection, long-range radio, cloud dashboards — Listed as future work *[planned]*

**Flow:** User presses the device button or connects to master Wi-Fi → Sends SOS or status; message relays across mesh nodes → Master node logs data for the backend → Responders see alerts and positions on the admin map → Responders message or broadcast back

**Prompt:** Best Overall Hack: top hack of HackHarvard 2025 (theme 'Compile the Decade', 10th anniversary), judged on innovation/impact, technical complexity, functionality/usability, collaboration/learning; iPad Pro and Pencil for 1st; Switch 2 bundle for 2nd; Ray-Ban Meta glasses for 3rd.
**Fit (none):** Social-good hardware plus software system; page states no prize target or connection to the decade theme.  *(targeted: Best Overall Hack)*
**AI:** none
**Architecture:** ESP32 mesh nodes (PlatformIO C++, PainlessMesh, GPS, OLED) with a master AP node; Expo mobile app and Next.js admin dashboard talk to Supabase; master node mirrors logs toward the backend.
**Novelty:** Combines custom soldered mesh hardware with both a responder map console and a mobile app, with offline operation as the core premise and no AI.
**Scope:** medium · working: Repo has three components (about 8.4k lines, 104 files, some tests); Devpost claims functioning mesh but gives no video or measurements. · polish: Long structured README; one screenshot; no demo link; no range or latency numbers.
**Claims:** Nodes dynamically join, leave and reconnect | Compact and low-cost for field deployment
**Gaps:** No demo video or metrics; README status of integration between mesh master and Supabase not verified
Sources: https://devpost.com/software/resqme-jq52al, https://github.com/lordoftheseas/ResQme (evidence file README), https://hackharvard-2025.devpost.com/

---

### ScrewYouIKEA.com
*HackHarvard HackHarvard 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best First-Time Hack

**What it is:** ScrewYouIkea turns uploaded furniture assembly manuals (PDF or images) into step-by-step Three.js 3D animations: Gemini 2.5 Pro extracts parts and steps, Gemini 2.5 Flash writes scene JSON and code, with voice input and a public library.
**Problem / user:** People confused by flat-pack furniture instructions.

**Features**
- Manual upload and extraction — PDF.js pages to images; Gemini Pro identifies tools, parts, steps. *[claimed]*
- 3D step animations — Three.js renders generated scene JSON with labels. *[claimed]*
- Manual library — Search and public collection of converted manuals. *[claimed]*
- Voice assistant — Web Speech API input and speech output. *[claimed]*
- Blueprint view and fullscreen — Minimal technical visuals. *[claimed]*

**Flow:** Upload manual → Processing extracts steps → Open step viewer → Watch 3D animation → Ask by voice

**Prompt:** not public / not found
**Fit (none):** No stated targeting; theme was Compile the Decade.  *(targeted: Best First-Time Hack)*
**AI:** Gemini 2.5 Pro for vision extraction, Flash for generating runnable scene code in a pseudo-sandbox.
**Architecture:** Next.js frontend with API routes, Express Gemini service, Three.js, Vercel.
**Novelty:** LLM-generated code executed in browser to animate assembly.
**Scope:** medium · working: ~12.6k LOC; screenshots; no video. · polish: Detailed README features, library UI.
**Claims:** Runs end-to-end on real IKEA manuals
**Gaps:** No first-time prize text
Sources: https://devpost.com/software/screwyouikea, evidence/hackharvard-hackharvard-2025-screwyouikea-com.json, prompts_cache/hackharvard-2025.md

---

### Yumi
*HackHarvard HackHarvard 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 3rd Best Overall Hack [3rd]

**What it is:** Social food app where users write casual restaurant reviews that Gemini turns into taste profiles, then ask by text or voice for recommendations; mentioning friends with @ merges everyone's preferences into group suggestions. iOS app, Next.js dashboard and FastAPI backend, seeded with scraped Boston restaurants.
**Problem / user:** Visitors and friend groups who default to chains or spend long chat threads choosing where to eat, wanting authentic local food.

**Features**
- Natural-language reviews turned into taste profiles — Gemini extracts flavors, atmosphere, price sensitivity and cuisines; profile accumulates over time *[shown_working]*
- Typed or spoken restaurant recommendations — Gemini Flash function calling with get_user_preferences and get_nearby_restaurants tools, then ranking *[shown_working]*
- @-mention friends for group picks — React hook queries backend as you type; preferences merged union-style and LLM finds places fitting everyone *[shown_working]*
- Boston restaurant database — Custom Google Places scraper over overlapping grid cells, stored in Supabase PostGIS for spatial queries *[claimed]*
- Food photo uploads with client-side resizing — iOS resizes images before upload; team cites 70% shorter uploads *[claimed]*
- Friend graph for coordination — Used for group matching rather than likes or comments *[claimed]*
- Voice AI reservations, calendar, dietary handling, other cities — Listed as next steps *[planned]*

**Flow:** Write a casual review of a place → Gemini updates your taste profile → Ask for recommendations by typing or speaking → Type @ to add friends to the request → Receive ranked restaurants suited to the group

**Prompt:** Best Overall Hack: top hack of HackHarvard 2025 (theme 'Compile the Decade', 10th anniversary), judged on innovation/impact, technical complexity, functionality/usability, collaboration/learning; iPad Pro and Pencil for 1st; Switch 2 bundle for 2nd; Ray-Ban Meta glasses for 3rd.
**Fit (none):** Full-stack agentic social product with iOS, web and backend; no stated prize targeting.  *(targeted: Best Overall Hack)*
**AI:** Gemini Flash with function calling extracts preferences from reviews and orchestrates retrieval and ranking; cached taste profiles cut latency from 15-20 s; sentence-transformers and ElevenLabs are listed without explained roles.
**Architecture:** SwiftUI iOS app and Next.js dashboard call Python FastAPI on Render; Supabase Postgres/PostGIS and auth store users and restaurants; Gemini tools query preferences and nearby places.
**Novelty:** Treats reviews as free-form text feeding an agent rather than star ratings, and merges multiple users' tastes at request time through @ mentions.
**Scope:** large · working: Demo GIF on Devpost; repo about 44k lines across dashboard and extra aegis module; deployed on Render/Netlify per page. · polish: Native iOS app and web dashboard; README is short; no tests; no video.
**Claims:** Built in 36 hours | Image resizing cut upload time by 70% | Thousands of Boston restaurants scraped
**Gaps:** No video; Role of ElevenLabs/Twilio not explained; Repo contains an aegis folder not described in README
Sources: https://devpost.com/software/yumi, https://github.com/scrappydevs/Yummy (evidence file README), https://hackharvard-2025.devpost.com/

---

