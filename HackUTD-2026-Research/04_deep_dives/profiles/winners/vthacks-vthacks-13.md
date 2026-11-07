# VTHacks — VTHacks - 13 (4 projects)

### Cognita
*VTHacks VTHacks - 13 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** VTHacks - 2nd Place Prize [2nd]

**What it is:** An onboarding platform for interns: a company uploads PDFs, manuals and policies, and an intern asks a question to get a short multi-section lesson with interactive pieces such as multiple choice and drag-and-drop. Interaction logs feed follow-up lessons for weak spots.
**Problem / user:** Interns and new hires facing hundreds of pages of documents, and the HR teams who must onboard them without much time.

**Features**
- Document ingestion — PyMuPDF extracts PDF text, chunks it, and Gemini embeddings go into ChromaDB *[claimed]*
- Question-to-lesson generation — RAG retrieval plus Gemini 2.5 Pro produces structured JSON lessons with multiple sections *[claimed]*
- Interactive lesson components — Frontend renders multiple choice, fill-in-the-blank, code examples, drag-and-drop and diagrams *[shown_working]*
- Progress tracking — Attempts, time spent and completion per component visible to interns and companies *[claimed]*
- Adaptive follow-ups — Interaction logs detect knowledge gaps and trigger targeted lessons; a reviser agent edits lessons *[claimed]*
- Auth and org storage — Flask cookie-JWT auth and MongoDB helpers for users, orgs and lessons *[shown_working]*

**Flow:** Company uploads training documents → Text is chunked and embedded → Intern asks about a role or process → System retrieves context and generates a lesson → Intern completes interactive components → Analytics trigger a follow-up lesson

**Prompt:** VTHacks 13 main 2nd place prize: general overall placement, Nintendo Switch 2 per member; the page gives no theme or criteria.
**Fit (none):** General overall prize with no brief; project is an AI education/HR tool, and it also uses Gemini (an MLH sponsor prize) without stating that it targets it.  *(targeted: VTHacks 2nd Place)*
**Sponsor tools:** Gemini API (Embeddings and lesson generation, core)
**AI:** RAG: Gemini embeddings in ChromaDB retrieve document chunks, Gemini 2.5 Pro writes structured JSON lessons from engineered prompts; a second agent revises lessons.
**Architecture:** Next.js 15 frontend with shadcn UI over a Flask backend with JWT cookies, MongoDB helpers, and ChromaDB plus Gemini scripts (LessonGen, LessonReviser).
**Novelty:** Generates interactive lesson components rather than text answers, and plans to close the loop with gap-based follow-ups.
**Scope:** small · working: Repo ~4.9k LOC; README calls LessonGen experimental and the chat endpoint a placeholder, so the pipeline is only partly wired. Demo video exists. · polish: Branding assets, animated dashboards and lesson reader built on shadcn; no tests.
**Gaps:** Video not watched; Adaptive follow-up logic not evidenced in README
Sources: https://devpost.com/software/cognito-at5gu8, evidence/vthacks-vthacks-13-cognita.json (README), https://vthacks-13.devpost.com/

---

### Fire Guard
*VTHacks VTHacks - 13 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** VTHacks - 3rd Place Prize [3rd]

**What it is:** A hardware prototype of a firefighter helmet that fuses LiDAR, 24 GHz radar, IMU, camera and microphone. It builds SLAM maps meant to work through smoke, labels rooms from detected objects, transcribes radio speech, recognizes hand gestures and shows everything on a HUD and a command-center dashboard.
**Problem / user:** Firefighters (and incident commanders) dealing with low visibility, disorientation and unreliable noisy radio communication inside burning buildings.

**Features**
- LiDAR plus radar SLAM — Fuses 2D LiDAR, radar heatmaps and BNO055 IMU to map and correct drift, tested in simulated smoke *[shown_working]*
- Object detection and room labels — YOLOv5 finds objects; DistilGPT-2 turns them into room labels such as kitchen *[shown_working]*
- Speech to text chat — Whisper transcribes radio speech into a shared team chat *[shown_working]*
- Gesture recognition — MediaPipe Hands reads stop, help and OK signals *[claimed]*
- Obstacle and inactivity alerts — Radar levels SAFE to EMERGENCY; IMU inactivity pings last known location *[claimed]*
- HUD and command dashboard — Web HUD on the helmet laptop and Next.js dashboard for monitoring several firefighters *[claimed]*
- Custom ad-hoc networking — Serial and WebSocket pipelines route sensor streams; mesh planned *[claimed]*

**Flow:** Helmet sensors stream data → Laptop runs detection, SLAM, speech and gesture models → Firefighter sees map, alerts and chat on HUD → Pings and transcripts reach shared chat → Commander watches status on dashboard

**Prompt:** VTHacks 13 main 3rd place prize: general overall placement, Sony headphones per member; the page gives no theme or criteria.
**Fit (none):** General overall prize with no brief; project is a multi-sensor safety hardware build.  *(targeted: VTHacks 3rd Place)*
**AI:** YOLOv5 object detection, Whisper speech-to-text, MediaPipe Hands gestures and DistilGPT-2 for room labelling; fusion and SLAM are classical sensor processing.
**Architecture:** Helmet sensors feed a laptop (Jetson TX2 abandoned) via ESP32/serial and an ad-hoc router; FastAPI WebSockets ingest and fuse data for a Next.js HUD and dashboard.
**Novelty:** Adds penetrating radar to LiDAR SLAM and a helmet comms layer; heavy custom hardware work for a hackathon (radar boards, ad-hoc networking).
**Scope:** medium · working: ~12k LOC across mapping, detection, transcription and radar folders; Devpost says SLAM worked only in simulated smoke and with a single helmet. · polish: Detailed README and hardware notes; limited screenshots, no video, no tests.
**Claims:** Radar setup required studying 300+ pages of documentation | Fused SLAM demonstrated in simulated smoke
**Gaps:** Slideshow not read; No quantitative results; README and Devpost differ on LiDAR model/radar spec counts
Sources: https://devpost.com/software/fire-guard, evidence/vthacks-vthacks-13-fire-guard.json (README), https://vthacks-13.devpost.com/

---

### SpeakEasy
*VTHacks VTHacks - 13 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** VTHacks - Best First Time Hack

**What it is:** A web app where users upload (or record) a speech video and get a transcript, a battery of scores, reference talks to compare against, and an AI coach report with strengths and practice tasks.
**Problem / user:** Public speakers, especially non-native English speakers and neurodivergent people, who find coaching expensive and generic tools unaware of their needs.

**Features**
- Video upload and transcription — Flask backend extracts audio with ffmpeg and transcribes with Whisper *[shown_working]*
- Transcript grading — Gemini scores clarity, relevance, flow, vocabulary, grammar, filler words and rhetoric, and infers speech context *[shown_working]*
- Reference talk comparison — Gemini makes search keywords, YouTube Data API finds talks, yt_dlp fetches audio, Gemini compares delivery to them *[claimed]*
- Multimodal coach report — Uploads video+audio to Gemini for strengths, improvements and 1-3 practice tasks plus overall score *[shown_working]*
- Speaking metrics — Word count, words per minute, duration and length score *[shown_working]*
- Live practice mode and metric info button — Webcam practice screen and explanations of each metric *[claimed]*
- Text-only fallback — Falls back to transcript-only analysis when audio is noisy or quiet *[claimed]*
- Progress history and accounts — Log in and compare past speeches *[planned]*

**Flow:** Upload a talk video or open live practice → Backend extracts audio and Whisper transcribes → Gemini grades transcript and retrieves examples → Reference talks fetched and compared → Multimodal Gemini writes coach report → Results page shows scores, context, examples and feedback

**Prompt:** not public / not found
**Fit (none):** Prize page gives only the name; the page does not state team eligibility details. Project inclusive framing (non-native, neurodivergent speakers) is its own pitch.  *(targeted: VTHacks - Best First Time Hack)*
**Sponsor tools:** Google Gemini API (Transcript grading, audio comparison and multimodal coach report (about six calls per analysis), core)
**AI:** Whisper for transcription; Gemini with strict JSON-schema prompts for transcript scoring, keyword generation, audio-vs-reference grading and a final multimodal coaching pass over video and audio.
**Architecture:** React/Tailwind frontend posts video to a Flask /api/analyze; Python modules (TextEncoder, AudioEncoder, Coach) call Whisper, Gemini, YouTube API and yt_dlp; JSON returned; uploads deleted afterward.
**Novelty:** Combines reference-talk retrieval from YouTube with multimodal grading, and targets non-native and neurodivergent speakers specifically.
**Scope:** small · working: Backend and React frontend of about 2.4k lines with tests mocking Gemini; Devpost screenshots show results pages. · polish: Detailed README, metric info screen, many scoring dimensions; no demo video or live link.
**Claims:** Complete multimodal pipeline of video, audio and transcript | JSON-first prompts stabilize LLM output | About 6 Gemini calls per analysis
**Gaps:** no description of Best First Time Hack criteria; README lists Gemini only while Devpost also lists YouTube/yt_dlp steps
Sources: https://devpost.com/software/speakeasy-49nuf1, evidence/vthacks-vthacks-13-speakeasy.json (README), prompts_cache/vthacks-13.md

---

### StoryVue
*VTHacks VTHacks - 13 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** VTHacks - 1st Place Prize [1st]

**What it is:** A hands-free reading assistant for visually impaired children: a camera detects a printed book, Tesseract.js reads the page text, and an OpenAI model can read, explain or summarise it aloud while the child controls everything by voice. A voice chat mode with settings is also in the repo.
**Problem / user:** Visually impaired children who want to read independently; the page cites statistics on childhood vision impairment and the benefit of being read to.

**Features**
- Book detection — TensorFlow model checks for a book in the camera frame and shows confidence before OCR *[claimed]*
- Live OCR — Tesseract.js extracts text from video frames, which is cleaned before use *[claimed]*
- AI explanation and summaries — OpenAI GPT-3.5 explains hard content and summarises pages conversationally *[shown_working]*
- Voice control — Web Speech API speech recognition and spoken replies with adjustable voice, rate and pitch *[shown_working]*
- Conversation memory — Chat keeps context across messages *[shown_working]*
- LiveKit audio streaming — Real-time audio processing hooks; collaborative reading is future *[planned]*

**Flow:** Point camera at a printed book → App detects book and runs OCR → Text sent to the backend and GPT → Response is spoken aloud → Child asks follow-ups by voice

**Prompt:** VTHacks 13 main 1st place prize: overall top project, MacBook Air per member; the page gives no theme or criteria. Accessibility had a separate prize it did not list.
**Fit (none):** Overall prize with no brief; the project is an accessibility education tool, though Devpost does not name the separate Best Accessibility prize.  *(targeted: VTHacks 1st Place)*
**Sponsor tools:** LiveKit (Audio streaming scaffold and planned collaboration, supporting)
**AI:** OpenAI GPT-3.5-turbo gives conversational explanations; Tesseract.js does OCR and a TensorFlow.js model detects books; browser Web Speech API handles speech.
**Architecture:** Browser app (Web Speech, Tesseract.js, TensorFlow.js) talks to a Node/Express backend that calls OpenAI, with Google OAuth and optional LiveKit server.
**Novelty:** Combines book detection, OCR and LLM explanation in a fully voice-driven flow aimed at blind children; collaborative reading is only planned.
**Scope:** small · working: ~6k LOC repo (includes model files), README setup steps and demo video; README features centre on voice chat, not OCR. · polish: Figma slides and demo video; no tests; README is generic.
**Claims:** Cites 7 million US people with vision impairment as motivation
**Gaps:** OCR/book-detection not described in README; Video not watched
Sources: https://devpost.com/software/storyvue, evidence/vthacks-vthacks-13-storyvue.json (README), https://vthacks-13.devpost.com/

---

