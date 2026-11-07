# HooHacks — HooHacks 2025 (3 projects)

### Dr. Andy - The Deployable Surgeon
*HooHacks HooHacks 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 1st Place [1st]

**What it is:** A tele-surgery prototype: a surgeon wearing a Meta Quest 3 controls a pair of custom-built robotic arms through hand tracking, with stereo cameras for vision at the remote site, linked over WebSockets and ROS; the demo tied a suture.
**Problem / user:** Patients in war zones, disaster areas and remote regions lacking surgeons; the operator is a skilled surgeon controlling remotely.

**Features**
- VR hand-tracking control — Quest 3 hand tracking in Unity captures finger movement and sends it over WebSockets, mapped to arm commands. *[shown_working]*
- Custom robotic arms — Team-built arms with Arduino firmware move via inverse kinematics from ROS commands. *[shown_working]*
- Stereo vision — Dual cameras give the surgeon an immersive 3D view in a mixed-reality UI. *[shown_working]*
- Low-latency link — Page and README state sub-50 ms control latency. *[claimed]*
- Stabilization — ML-based stabilization claimed for precision; AI-assisted version is future work. *[claimed]*
- OpenXR support — Designed to work with any OpenXR headset. *[claimed]*

**Flow:** Put on Quest 3 headset → Hand movements are tracked → Commands flow via Unity and ROS to arms → Arms mirror movement while stereo video returns → Demo ties a suture

**Prompt:** Best Overall: no theme; all projects considered, judged on UI/UX, creativity, feasibility, functionality and impact.
**Fit (none):** Working hardware demo with high impact framing; no explicit prize targeting, as Best Overall has no stated theme.  *(targeted: Best Overall - 1st Place)*
**AI:** Mentions ML-based stabilization for precision, with no model detail; mostly kinematics and control rather than ML.
**Architecture:** Unity on Quest 3 tracks hands, sends over WebSockets to a ROS node that computes inverse kinematics and drives Arduino-controlled arms; stereo cameras stream back to a mixed-reality UI.
**Novelty:** Full custom-built physical robot with VR teleoperation within a hackathon, delivering a physical task (suturing).
**Scope:** large · working: Demo GIFs in README and hardware prototype performing a suture; repo around 28k LOC. · polish: Structured README with technology sections, photos and gifs; no tests.
**Claims:** Sub-50 ms control latency | Precision exceeded expectations, unquantified
**Gaps:** no video link; latency not independently shown
Sources: https://devpost.com/software/y-u9oxsk, https://github.com/paris-phan/and-e, https://hoohacks-2025.devpost.com/

---

### Show Me A Sign
*HooHacks HooHacks 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 2nd Place [2nd]

**What it is:** A Duolingo-style web app for learning American Sign Language fingerspelling. The learner signs letters to their webcam; video frames stream to a Flask backend where a CNN and a geometry-based finger check jointly judge the sign.
**Problem / user:** Mainstream language apps ignore ASL; targets beginners and intermediate learners who want instant feedback on their hand signs.

**Features**
- Real-time sign recognition from webcam — Frames stream over WebSockets to a Flask server; hand tracking feeds a CNN trained on about 25,000 wireframe-style hand images. *[shown_working]*
- Hybrid prediction (CNN plus geometry) — OpenCV finger-geometry analysis is combined with CNN top-K confidence; README screenshots show agree, medium and high-confidence cases. *[shown_working]*
- Letter flashcard lessons — A lesson shows one letter at a time and advances once the user signs it correctly. *[claimed]*
- Lesson pathways by difficulty — Content organized from alphabet to numbers and phrases across beginner, intermediate, advanced levels. *[claimed]*
- Progress tracking with XP and achievements — Supabase stores accounts, profiles, XP, accuracy metrics; a progress tracker page displays them. *[shown_working]*
- Frame-rate control — Client throttles frames sent to the server to keep latency low under load. *[claimed]*

**Flow:** Sign up or log in → Open a lesson from the pathway → See a letter flashcard → Sign the letter to the webcam → Backend scores the sign with CNN plus geometry → Advance to next letter and view progress and XP

**Prompt:** Best Overall at HooHacks 2025 has no stated theme; any project is considered, scored on UI/UX, creativity, feasibility, functionality and impact (out of 5 each). Event tags: beginner friendly, education, social good.
**Fit (implied):** Education-flavored accessibility project with working ML feedback loop and gamified UI; no prize is explicitly targeted on the page.  *(targeted: Best Overall - 2nd Place)*
**AI:** Custom CNN trained on roughly 25k ASL hand-sign images in wireframe form, fused with a rule-based finger geometry check; MediaPipe/OpenCV hand tracking supplies landmarks.
**Architecture:** React/TypeScript/Vite frontend with shadcn UI captures webcam; socket-based stream to Flask backend running OpenCV and TensorFlow models; Supabase handles auth and progress.
**Novelty:** Fuses a learned classifier with explicit geometric checks and trains on wireframe hands to reduce skin-tone and hand-size bias; most ASL demos use a single model.
**Scope:** medium · working: Repo of about 134 files and 12k LOC with separate frontend and Python server; README screenshots of live model outputs. · polish: Animated responsive UI, auth, lessons, XP and progress pages; no tests or live link.
**Claims:** CNN trained on about 25,000 ASL images | Pipeline optimized for 30fps with minimal latency | Wireframe training reduces skin color and hand size bias
**Gaps:** no demo video; no accuracy figures; only letters shown working; phrases are aspirational
Sources: https://devpost.com/software/show-me-a-sign, https://github.com/itskevinshi/lingo-sign-explorer, https://hoohacks-2025.devpost.com/

---

### wearit
*HooHacks HooHacks 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Best Overall - 3rd Place [3rd]

**What it is:** A React Native (Expo) mobile app that takes a photo of a clothing item and produces weather-aware outfit inspiration, an optional avatar try-on and shopping links by chaining several third-party APIs.
**Problem / user:** Everyday people who own clothes but struggle to style them; wants quick, wearable outfit ideas suited to weather and personal style.

**Features**
- Wardrobe photo analysis — Uploaded image goes to Google Cloud Vision for labels and color palette to identify garment type and vibe. *[claimed]*
- LLM-written fashion prompt — Together AI Mistral-7B turns vision output into a short fashion description and search query, with fallback parsing for malformed output. *[claimed]*
- Weather- and location-aware queries — Open-Meteo supplies local weather that tailors the outfit search query. *[claimed]*
- Outfit inspiration images — Tailored query sent to Pexels API; curated outfit photos are displayed. *[claimed]*
- Avatar virtual try-on — ReadyPlayerMe avatar resembling the user previews outfits. *[claimed]*
- Shopping recommendations — SerpAPI Google Shopping returns purchasable items matching the tried-on look. *[claimed]*
- Wardrobe image storage — Camera-roll images are converted and uploaded to AWS S3 across iOS and Android. *[claimed]*

**Flow:** Upload a photo of a wardrobe item → App analyzes image with Vision and LLM → App fetches location weather → Pexels outfit images are shown → Optionally create avatar and preview outfits → View shopping results for the look

**Prompt:** Best Overall at HooHacks 2025 has no stated theme; any project is considered, scored on UI/UX, creativity, feasibility, functionality and impact (out of 5 each).
**Fit (none):** General consumer mobile app showing a long multi-API pipeline; no prize is explicitly targeted.  *(targeted: Best Overall - 3rd Place)*
**AI:** Google Cloud Vision labels and colors feed prompt-engineered Mistral-7B-Instruct (via Together AI) to produce short search queries; no training or retrieval.
**Architecture:** Expo React Native client orchestrates chained and parallel promise-based calls to Vision, Together AI, Open-Meteo, Pexels, ReadyPlayerMe, SerpAPI and S3, then aggregates results into screens.
**Novelty:** Combines vision tagging, LLM prompt generation, weather, avatar try-on and shopping search in one mobile pipeline; mostly API orchestration.
**Scope:** small · working: Repo about 28 files and 2.5k LOC; README only notes API keys are needed; no demo video or live link. · polish: Multiple Expo screens described; no screenshots, tests or setup docs in README.
**Claims:** Full-stack AI app built in under 24 hours | Integrates five or more external APIs
**Gaps:** no demo video; README nearly empty; features not verified working
Sources: https://devpost.com/software/wearit-a5nw62, https://github.com/athiraponneth/HooHacks25, https://hoohacks-2025.devpost.com/

---

