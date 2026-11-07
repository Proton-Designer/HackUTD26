# HackGT — HackGT 13 (30 projects)

### Athena
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** NSA: Hearsay: The Audio Authentication Challenge - 2nd Place [2nd]

**What it is:** Desktop agent that wraps Google Meet to defend against AI voice-clone callers and keyboard-sound eavesdropping. It scores the other party's voice as real or synthetic, perturbs keystroke audio so an attacker model reads a decoy, and tones out spoken secrets like codes. A dashboard shows a combined threat level.
**Problem / user:** People on video calls exposed to deepfake colleagues, acoustic keystroke side channels and accidentally spoken passwords or reset codes.

**Features**
- Voice authenticity scoring — Scores each 4-second window of caller audio real vs synthetic with fused XLS-R models plus a LightGBM spectral model. *[shown_working]*
- Keystroke attacker (Ares) — CNN + BiGRU with CTC reads typed keys from audio; team's own build used to measure leakage. *[shown_working]*
- Adversarial keystroke shield (Athena) — Optimizes an inaudible perturbation so the attacker reads a decoy while speech stays intact. *[shown_working]*
- Secret Shield — Vosk spots digit runs, passwords, card numbers in outgoing speech and tones them out via a 500 ms delay. *[shown_working]*
- Unified threat score — Combines voice risk, keystroke leakage and speech timing into 0-100 with SAFE to CRITICAL levels. *[shown_working]*
- Meet integration — Launches Chrome with an injected audio bridge so Meet publishes the shielded mic. *[shown_working]*
- Ares vs Athena panel — Dashboard shows attacker and defender rounds on each typing burst. *[shown_working]*

**Flow:** Launch Athena desktop app → It opens Google Meet in its own Chrome window with the audio bridge → Voice risk updates as the caller speaks → User types; attacker guesses vs real keys appear → Spoken secrets are muted before the other side hears them → Threat level updates on the dashboard

**Prompt:** NSA Hearsay challenge (2nd place) has no official description on the Devpost listing; per the team's README it concerns detecting real versus AI-synthetic voices, scored with minDCF and EER.
**Fit (explicit):** The voice-authenticity pillar runs the team's Hearsay challenge model (reported minDCF 0.058, EER 2.5%); keystroke and secret-shield pillars extend it into a call-security product.  *(targeted: NSA: Hearsay: The Audio Authentication Challenge - 2nd)*
**Sponsor tools:** Gemini 2.5 Flash (LLM agents for attacker/defender and decoy choice, supporting); Backboard (memory across rounds, supporting)
**AI:** Fine-tuned XLS-R and LightGBM fusion for deepfake voice detection; CNN+BiGRU CTC keystroke transcriber; Gemini plans decoys and sensitive spans; adversarial perturbation optimization; Vosk ASR.
**Architecture:** Python 3.12 desktop app (pywebview, FastAPI/WebSocket dashboard) with an event bus; model drivers run off the audio thread; Chrome DevTools injection wraps getUserMedia for Meet.
**Novelty:** Combines three audio threats in one live agent and built its own acoustic keystroke attacker to test the defense; reports adversarial re-solving and cross-keyboard failure openly.
**Scope:** large · working: 183-file repo, 90 tests, separate hearsay repo, video, and reported measurements from a live Meet test room. · polish: Offline fallback without API keys, dashboard, docs folder; compute-heavy full matches take minutes.
**Claims:** Voice detector minDCF 0.058, EER 2.5%; 10 of 10 held-out voices in Meet test | Keystroke attacker about 80% per key on real free typing | Shield held attacker at chance (2.8%) per round | Spoken 6-digit code blocked with about 1 s leaked
**Gaps:** official Hearsay challenge text not public
Sources: https://devpost.com/software/callguard, https://github.com/georgia-mellon/athena, https://hackgt13.devpost.com/

---

### ATP - Accessible to Prescription
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Impiricus: Build the next HCP Engagement Tool - 1st Place [1st]; Notability: Trust the Process

**What it is:** Voice AI agent that phones an insurer to pursue a prescription prior authorization, then bridges the doctor into the same live call when clinical judgment is needed and resumes after the doctor presses # to hand back. Includes an operator and presentation view and Slack briefings.
**Problem / user:** Prescribers and practice staff who lose hours each week on prior-authorization calls with insurers.

**Features**
- Outbound insurer call — Python service dials via Plivo SIP into a LiveKit room; agent introduces the request using supplied case info. *[shown_working]*
- Live doctor handoff — On escalation the agent pauses, calls the doctor, posts a Slack briefing; doctor presses 1 to join the same call. *[shown_working]*
- Hand-back to AI — Doctor presses # or taps Return to AI; agent resumes with the new context and can re-escalate later. *[shown_working]*
- Voicemail and no-answer handling — Press-1 confirmations and timeouts keep voicemail out of the conversation; insurer told doctor is unavailable. *[shown_working]*
- Facts and outcome capture — Records decision, reference number, requirements; approval reported only on explicit insurer confirmation. *[shown_working]*
- Operator and presentation views — Web UI for call setup, live transcript and facts, history and JSON export. *[shown_working]*

**Flow:** Save insurer and doctor phone numbers in the operator screen → Start insurer call; recipient presses 1 → Agent explains the request and answers questions → When clinical input is needed it calls the doctor and posts a Slack briefing → Doctor presses 1, speaks with insurer, presses # to return → Agent finishes and outcome is logged

**Prompt:** Impiricus: build technology-enabled healthcare provider engagement tools that deliver the right information at the right time (HackGT 12 wording; HackGT 13 page lists the prize without text). Notability 'Trust the Process' has no public description.
**Fit (explicit):** Engages physicians by pulling them into insurer calls only when needed and briefing them in Slack; Devpost lists both tracks and mentions Notability diagrams for call-flow design.  *(targeted: Impiricus: Build the next HCP Engagement Tool - 1st, Notability: Trust the Process)*
**Sponsor tools:** ElevenLabs Agents (real-time speech, voice generation, voice cloning, core); Notability (whiteboarding call flows (per Devpost), token)
**AI:** OpenAI reasons over case info and decides when to escalate; ElevenLabs handles speech-to-text and voice; optional cloned doctor-like voice for smoother transitions.
**Architecture:** Local FastAPI coordinator manages case and call state, joins LiveKit room and Plivo SIP legs, calls OpenAI and ElevenLabs, posts to Slack; React web view.
**Novelty:** Single continuous call where AI and human alternate, with repeat escalations and phone-key controls; handles real telephony edge cases like voicemail.
**Scope:** medium · working: Rehearsed live call with insurer and doctor phones described; repo has tests and a make demo launcher. · polish: Detailed operator README, Slack status states; no demo video listed; no metrics.
**Claims:** Doctor estimate of 10 hours a week on prior auth (cited, not measured)
**Gaps:** no video; exact Notability prompt unknown
Sources: https://devpost.com/software/atp, https://github.com/notvasub/ATP-Access-to-Prescription, https://hackgt13.devpost.com/

---

### Bear With Me
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** MLH: Best Domain from .tech

**What it is:** A pediatric intake system: at check-in a child gets a tablet with a talking bear that asks 7 to 9 adaptive questions by voice, picture cards or pointing at a body, while the parent answers reworded questions on their phone and staff see a one-page side-by-side brief.
**Problem / user:** Children in pediatric visits, who account for only about 4 to 14 percent of the talk per a cited study; also parents, doctors and front-desk staff.

**Features**
- Bear Companion tablet — NFC-matched tablet; Grok-powered bear asks short adaptive questions starting from the parent's stated reason, with voice interruption via on-device voice detection. *[shown_working]*
- Multiple child answer modes — Speak, tap picture cards, or point to where it hurts; a mounted camera locates the pointing on a body model. *[claimed]*
- Range-of-motion check — Same body kinematic model assesses whether joints move through full range. *[claimed]*
- Bear's Helper parent chat — Phone link from booking; Grok reword follow-up questions and a validator ensures wording cannot leak the child's answer. *[claimed]*
- Doctor Brief staff portal — Live dashboard of active tablets, safety alerts, child and parent answers side by side with disagreements flagged, pain body map and family questions. *[claimed]*
- Safety detection — Flags statements like trouble breathing or being hurt by someone and alerts staff. *[claimed]*
- Engagement tools — Bear Run mini-game unlocks after three questions; Get a grown-up button. *[claimed]*
- NFC check-in — Card with only an ID tapped on a USB reader; staff login required for lookups; syncs to the tablet. *[claimed]*

**Flow:** Parent books and receives a Bear's Helper link → Family taps NFC card at front desk → Child answers the bear by voice, cards or pointing → Parent answers real-time follow-ups on phone → Staff watch the Doctor Brief fill live with safety alerts → Doctor reads a one-page summary of both views

**Prompt:** not public / not found
**Fit (explicit):** Deployed publicly on a .tech domain (bearwithme.tech) with a guided demo at /demo. MLH prize text itself was not fetched.  *(targeted: MLH: Best Domain from .tech)*
**Sponsor tools:** .TECH domain (Hosting the live app at bearwithme.tech, supporting)
**AI:** xAI Grok for speech-to-text, structured-output answer mapping, text-to-speech, parent question rewording and summaries; Silero VAD voice detection; OpenCV kinematic body model for pointing.
**Architecture:** Next.js on Vercel with Node backend; Supabase Postgres (18 tables) and Realtime for sync across tablet, camera, parent phone and staff dashboard; USB NFC reader and mounted camera.
**Novelty:** Brings a child-first intake with a leak-proof parent question validator and camera-based body pointing into the waiting room, spanning four synced devices.
**Scope:** large · working: Live site with guided demo; claims four devices sync in about one second. · polish: Public domain, 18-table schema, Vitest tests mentioned; no repo or video linked.
**Claims:** Four devices sync within about one second | Bear response time cut from about five seconds to under one second | Children make up 4 to 14 percent of talk in their own visits (cited study)
**Gaps:** No GitHub repo linked; No video linked; bearwithme.tech/demo not opened; No user testing or clinical validation
Sources: https://devpost.com/software/bear-with-me-8ijcef

---

### Bump
*HackGT HackGT 13 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Oracle of the Deep - 2nd Place [2nd]

**What it is:** Native iPhone app where two nearby people tap phones, confirm the bump, and see specific shared interests plus AI-written conversation starters drawn only from approved profile facts. Profiles are built by speaking a short intro to a Grok voice interviewer.
**Problem / user:** Students and event attendees standing near each other who do not know what to say to start a conversation.

**Features**
- Voice-built profile — Short spoken or typed intro; Grok asks up to three follow-ups aloud and drafts a profile the user edits and approves. *[shown_working]*
- Phone-tap bump — MultipeerConnectivity, UWB ranging and accelerometer spike combine; both users confirm; ambiguous bumps rejected. *[shown_working]*
- Grounded overlap matching — On-device matching ranks specific shared and complementary interests above broad categories. *[shown_working]*
- Conversation starters — Grok phrases only the computed overlaps; falls back to Apple Foundation Models or templates, labeled. *[shown_working]*
- Private check-in — After the chat, log topics and whether to reconnect; data stays on the phone. *[shown_working]*
- Live Activity and bump rooms — Status in Live Activity; Supabase Realtime rooms vanish after the bump. *[shown_working]*

**Flow:** Create profile by speaking → Review and approve profile lines → Tap phones with a nearby person and both confirm → View shared interests and talking points → Check in privately afterward

**Prompt:** Oracle of the Deep (2nd) has no public description on the listing. Devpost also names Meta's 'Bringing People Closer Together with AI' and SpaceXAI 'Make it Legendary' as intended prizes.
**Fit (explicit):** Devpost argues the unstructured-speech-to-grounded-match pipeline fits the ML track, in-person connection fits Meta's theme, and Grok does speech and reasoning.  *(targeted: Oracle of the Deep - 2nd, ML/AI/Data track, Meta: Bringing People Closer Together with AI, SpaceXAI: Make it Legendary)*
**Sponsor tools:** xAI Grok (speech-to-text/TTS interviews, profile drafting, tagging, talking points, core)
**AI:** Grok for voice interview, interest tagging and starter phrasing with validation; matching done deterministically on-device first so AI cannot invent overlaps; Apple on-device model fallback.
**Architecture:** SwiftUI iOS 17 app with MultipeerConnectivity, Nearby Interaction, Core Motion; Node bump-api on Render keeps the xAI key; Supabase Realtime for encrypted bump messages; ActivityKit.
**Novelty:** Builds a phone-touch gesture on iOS without phone-to-phone NFC; grounds LLM output on precomputed overlaps; no match score or feed by design.
**Scope:** large · working: Native iOS app, web beta link, backend, tests; about 26k LOC across ios, web and backend. · polish: Research-cited README, TOC, roadmap, mockups; no video listed.
**Claims:** No measured outcomes; effect on conversations listed as future work
**Gaps:** no video; prize text absent
Sources: https://devpost.com/software/bump-it1fjy, https://github.com/bump-hackgt/bump, https://hackgt13.devpost.com/

---

### Campfire
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** MLH: Best Use of backboard.io

**What it is:** A bot that joins a friend group's WhatsApp trip chat, captures messages, photos, voice notes and locations between start and end commands, posts a narrated recap each night, and afterwards offers a story player that steps through the trip on an illustrated map.
**Problem / user:** Groups of friends travelling together whose voice notes, jokes and photos get buried in a group chat.

**Features**
- WhatsApp capture with commands — Baileys service streams chat events via Redis; /campfire start and end bound capture, off/on the record pause it, forget deletes a message. *[claimed]*
- Nightly narrated recap — OpenAI builds ordered story segments and ElevenLabs narrates; sent to the chat each night. *[claimed]*
- Voice-note transcription — ElevenLabs transcribes shared voice memos. *[claimed]*
- Around the Campfire story player — React app moves through trip locations with narration, captions, real voice memos on an illustrated d3 map. *[shown_working]*
- Long-term trip memory — Backboard gives the OpenAI agent memory across days. *[claimed]*
- Local suggestions and next-trip ideas — Muse Spark suggests food and activities after the recap; README says next-trip suggestions are still stubs. *[unclear]*
- Side Quests, anniversary callbacks — Listed as future work; stubs in README. *[planned]*

**Flow:** Type /campfire start in the WhatsApp group → Chat normally while Campfire captures content → Use off the record or forget for privacy → Receive a narrated recap each night → Type /campfire end → Open Around the Campfire to play back the trip

**Prompt:** not public / not found
**Fit (explicit):** Backboard supplies long-term memory for the OpenAI trip agent so context persists across days of a trip. MLH prize text was not fetched.  *(targeted: MLH: Best Use of backboard.io)*
**Sponsor tools:** Backboard.io (Long-term memory for the trip agent, core); Vultr (VPS keeping the WhatsApp bot online, supporting); ElevenLabs (Transcription and narration, supporting)
**AI:** OpenAI orders captured content into story segments, ElevenLabs transcribes and narrates, Backboard adds persistent memory, Muse Spark gives local suggestions.
**Architecture:** Node Baileys WhatsApp service to Redis streams; Flask, Celery and Postgres/pgvector backend; React/Vite playback app; Docker Compose with Caddy on a Vultr VPS.
**Novelty:** Meets users in their existing chat with an explicit on/off-the-record capture window, producing a narrated story rather than a feed.
**Scope:** medium · working: Live login site, Docker Compose setup and sample-trip seed script; README says some features are stubs. · polish: 13.7k LOC with tests, Docker, deploy guide and docs folder.
**Claims:** Working capture, story pipeline and post-trip group features
**Gaps:** README is a later version that includes a Visa Intelligent Commerce payments section not on the Devpost; feature list follows Devpost, README used for status; No demo video; Next-trip suggestions status conflicts (Devpost claims, README says stub)
Sources: https://devpost.com/software/campfire-3jo6wc, evidence/hackgt-hackgt-13-campfire.json

---

### ClearPath
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Impiricus: Build the next HCP Engagement Tool - 3rd Place [3rd]

**What it is:** Healthcare prototype combining a prior-authorization engine built from a real 253-page insurance plan document with a shared care-team workspace and a patient voice assistant named Ava. Insurer review is simulated and all data is demo data.
**Problem / user:** Patients waiting on prior authorization and doctors across specialties who cannot see what is missing or who owns the next step.

**Features**
- Policy library from real plan PDF — Extracts 90 benefit categories (41 required, 41 not, 8 conditional) with source pages and review workflow. *[shown_working]*
- Prior-auth check and questionnaire — Doctor picks patient, plan, treatment; rules engine says required/not/conditional and guides documentation (FHIR-shaped). *[shown_working]*
- Reviewer queue and history — Simulated reviewers approve, deny or request info; append-only history feeds a patient status page. *[shown_working]*
- Shared care workspace — Per-patient conditions, meds, notes, AI team briefings with next-step owners, relationship graph. *[shown_working]*
- Ava patient assistant — Speech or text intake, follow-ups, patient reviews a summary and sends it to one or all doctors. *[shown_working]*
- Medication panel — openFDA labels, adverse events and RxNav lookup; AI drafts a patient-friendly explanation. *[shown_working]*
- Ask ClearPath assistant — Gemini assistant using platform data and screen context. *[shown_working]*

**Flow:** Doctor selects patient, plan and treatment → App reports whether authorization is needed with sources → Doctor completes questionnaire and submits → Simulated reviewer decides; patient tracks status → Patient talks to Ava; summary goes to doctors → Doctors review meds and reply

**Prompt:** Impiricus track: build technology-enabled tools for engaging healthcare providers with the right information at the right time (HackGT 12 wording); no HackGT 13 text found.
**Fit (explicit):** Gives clinicians policy answers, briefings and patient messages in one workflow; Devpost names Impiricus, Meta and AI/ML tracks.  *(targeted: Impiricus: Build the next HCP Engagement Tool - 3rd, Meta: Bringing People Closer Together with AI, AI/ML: Oracle of the Deep)*
**Sponsor tools:** Gemini (Ask ClearPath assistant, supporting); ElevenLabs (Ava spoken replies, supporting); Meta Muse Spark/Voice (care-team briefings and transcription, supporting)
**AI:** PDF text structured into rules then second-model review (Grok) for human inspection; OpenAI powers Ava; Gemini and Muse Spark for assistant and briefings; BM25 search.
**Architecture:** Next.js/TypeScript frontend on Vercel; FastAPI backend with rules engine, FHIR-shaped resources, in-memory data; openFDA and RxNav medication APIs.
**Novelty:** Grounds prior-auth logic in an actual insurer document with page citations and keeps three questions (required, complete, approved) separate; two merged repos.
**Scope:** large · working: Two Vercel demos, three videos, 12k LOC repo; reviewer side simulated. · polish: Long README; in-memory storage, no tests; unintegrated branches acknowledged.
**Claims:** 253-page plan converted to 90 structured categories
**Gaps:** second repo not read
Sources: https://devpost.com/software/clearpath-chvrpy, https://github.com/hariomsah01/HackGT-13, https://hackgt13.devpost.com/

---

### Degrees
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** MLH: Best Use of Gemini API

**What it is:** An iOS app, pitched as a dating app for friend groups, that records in-person meetings as edges in a social graph (QR scan or room code), then uses Gemini to form small hangout groups from friends-of-friends, plan a real venue, and learn from post-hangout feedback.
**Problem / user:** College students, starting with Georgia Tech, who meet many people but rarely turn them into friends; feed-driven social apps do not push people offline.

**Features**
- In-person connections — Scan a QR code or join an event by room code and mark who you talked to; ending a hosted meetup connects attendees. *[claimed]*
- AI group formation — Recursive SQL walks the graph by chosen degree, pgvector ranks by Gemini embedding similarity, Gemini assembles a small group with an explanation including a friend-of-a-friend. *[shown_working]*
- Server-enforced anonymity — Unmet people stay anonymous until all accept; explanations written per viewer and replies naming unmet people rejected. *[claimed]*
- Grounded activity planning — Gemini with Google Maps grounding picks a venue, Places API adds address and price, Ticketmaster events as fallback; resumable job to fit serverless limits. *[claimed]*
- Group chat, icebreakers, photo album — Supabase Realtime chat, Gemini icebreakers, shared photos closing 24 hours after the hangout. *[claimed]*
- Feedback loop — Ratings and per-person labels, Gemini extracts interest tags, profile re-embedded; mutual 'great' allows phone-number exchange. *[claimed]*
- Your Circle — View of met people with a Play mode to bump into connections. *[claimed]*

**Flow:** Sign up and set reach, group size, budget, distance and frequency → Meet someone and scan QR or join by room code → Receive an anonymous AI-formed group with an explanation → Accept, chat and generate a venue plan → Attend, then rate the hangout and label each person → Browse Your Circle

**Prompt:** not public / not found
**Fit (explicit):** README says it was built for the Meta challenge of a social app with AI throughout, and Gemini handles embeddings, group formation, grounded planning and feedback analysis. Won the MLH Gemini prize; prize text not fetched.  *(targeted: MLH: Best Use of Gemini API, Meta: Bringing People Closer Together with AI)*
**Sponsor tools:** Gemini API (768-dim embeddings, group formation, icebreakers, feedback analysis, Maps-grounded planning, core); Google Maps grounding / Places API (Real venue selection and details, supporting)
**AI:** Gemini embeddings plus pgvector for similarity, Gemini Flash (Flash-Lite fallback) for group composition, icebreakers and feedback tagging, Gemini with Maps grounding for plans; deterministic fallbacks when quotas fail.
**Architecture:** Expo React Native iOS app; Hono API on Netlify Functions owning all AI calls and writes; Supabase Postgres with pgvector, Auth, Realtime and Storage under row-level security; shared Zod contract package.
**Novelty:** Treats friendship formation as graph traversal with degree-limited reach and viewer-specific anonymity, and feeds ratings back into embeddings.
**Scope:** large · working: Deployed API, mock mode for local run, seeded demo data, one test showing a score move from 0.83 to 0.97; no video. · polish: 205 files, 17.9k LOC, tests, PRD, architecture and API docs, demo script.
**Claims:** 'Would meet again' rating raised a match score from 0.83 to 0.97 on demo data | Every seeded user got a group including a friend-of-a-friend | AI steps have fallbacks so the demo never fully fails
**Gaps:** No demo video; Devpost lists Expo SDK 57 and the README says group votes on a time; minor differences not reconciled; MLH and Meta prize texts not fetched
Sources: https://devpost.com/software/degrees-gdibjk, evidence/hackgt-hackgt-13-degrees.json

---

### DocSpot
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Impiricus: Build the next HCP Engagement Tool - 2nd Place [2nd]

**What it is:** Web prototype where a physician finds a suitable specialist on a map of physicians, gets an AI-drafted, privacy-checked e-fax referral, and tracks the reply. Specialists not on Impiricus can respond without an account and later connect. Patient consent runs through an emailed signing link.
**Problem / user:** Referring physicians who cannot reach specialists, especially 'digitally dark' ones reachable mainly by fax, e.g. in rural or acquired practices.

**Features**
- Network map and list — SVG map of clinicians grouped by specialty plus a list view; demo uses 253 NPI-based records. *[shown_working]*
- Specialist ranking — Ranks by specialty, distance and relationship, including physicians outside Impiricus. *[shown_working]*
- AI e-fax draft — gpt-4.1-mini drafts an editable fax with minimal patient details and a privacy check before sending. *[shown_working]*
- Reply without account — Recipient can respond to a referral and optionally connect on Impiricus later. *[shown_working]*
- Patient consent flow — Emailed signing link via Resend, date-of-birth check and signature before more detail is shared. *[shown_working]*
- Colleague, telehealth and trial finder — Searches for colleagues, telehealth and trial options. *[claimed]*

**Flow:** Search specialist or open network map → Review ranked recommendations → Generate and edit e-fax draft with privacy check → Send and track response → If accepted, patient signs consent via email link → Specialist may connect on Impiricus

**Prompt:** Impiricus track: build technology-enabled tools that engage healthcare providers with the right information at the right time (HackGT 12 wording; HackGT 13 page lists no text).
**Fit (explicit):** README states it was built for the Impiricus challenge; reaches physicians outside the network through fax and invites them onto the platform.  *(targeted: Impiricus: Build the next HCP Engagement Tool - 2nd)*
**Sponsor tools:** Impiricus network concept (invitation path for non-members, unclear)
**AI:** OpenAI gpt-4.1-mini receives limited structured details to draft the fax and assist privacy review.
**Architecture:** Plain HTML/JS/SVG frontend; FastAPI backend with Pydantic; NPI registry data cleaned in a notebook; Resend for consent emails; hosted on Render.
**Novelty:** Uses fax as the engagement channel for physicians who ignore digital outreach, plus consent-gated disclosure; team's first hackathon.
**Scope:** small · working: Live Render demo link; 7.7k LOC repo with 21 files. · polish: No tests or video; fax sending is mocked (real e-fax integration listed as next step).
**Claims:** Demo covers 253 clinician records
**Gaps:** no video; whether fax is actually sent unclear
Sources: https://devpost.com/software/docspot, https://github.com/tvisha-t/docSpot, https://hackgt13.devpost.com/

---

### DopaMarine
*HackGT HackGT 13 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Aramco: A Marina's Mission - 2nd Place [2nd]

**What it is:** Browser study game where uploaded lecture slides or notes become a question deck, then a sea-creature world: finish levels for pearls (XP), beat a practice-exam shark boss, and fight Pokemon-style AR duels by answering questions. Weak concepts spawn as stronger Storm variants.
**Problem / user:** Students who get distracted by phones and find studying unmotivating.

**Features**
- Deck generation — Gemini turns PDFs, slides and notes into questions, field guides and hints, validated server-side. *[shown_working]*
- Sea-creature buddy and levels — Choose a buddy matching learning style; gameplay mechanics vary by style; pearls unlock levels. *[shown_working]*
- Practice-exam boss — Boss shark level acts as a practice exam. *[shown_working]*
- AR duels — Phone camera AR battles solo, with friends or nearby players; correct answers throw balls at the opponent. *[shown_working]*
- Map and spawns — Leaflet/OpenStreetMap map where concept creatures spawn nearby; weak concepts spawn stronger. *[shown_working]*
- Real-time duels and raids — WebSockets for presence, duels and raids. *[claimed]*
- Offline fallbacks — Local JSON if MongoDB is down; retries and fallback Gemini models. *[shown_working]*

**Flow:** Sign up and upload notes → AI generates deck and levels → Pick a sea-creature buddy → Complete levels, earn pearls, beat boss → Open AR and battle by answering questions → Grow from krill to bigger fish

**Prompt:** Aramco: A Marina's Mission (2nd) has no public description on the listing; the name hints at a marine theme.
**Fit (implied):** Sea-creature theme throughout; Devpost lists the track as its result but does not explain the fit.  *(targeted: Aramco: A Marina's Mission - 2nd)*
**AI:** Google Gemini generates decks and content with retries, fallback models and validation of inconsistent JSON.
**Architecture:** React/Vite/Tailwind frontend; Node/Express backend with WebSockets; MongoDB Atlas with local JSON fallback; Leaflet map; camera and motion sensors.
**Novelty:** Fuses a study-deck generator with a location-based creature-catching and AR duel loop, tying creature strength to weak concepts.
**Scope:** medium · working: 82-file repo with video; AR and map features described with fallbacks. · polish: Custom artwork, no tests; no live URL.
**Gaps:** prize text absent
Sources: https://devpost.com/software/dopamarine, https://github.com/Srihansi-Sagi/dopamarine, https://hackgt13.devpost.com/

---

### FlyBy
*HackGT HackGT 13 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 2nd Place [2nd]

**What it is:** Simulated search-and-rescue system for a flooded neighborhood. A drone flags possible people among debris and animals, a ground-control dashboard ranks the flags and recommends actions for human approval, and a separate fly-vision-based reflex handles obstacle avoidance in a carport simulation.
**Problem / user:** Rescue teams who can find people but lose time triaging drone detections and field reports.

**Features**
- Ranked sighting queue — Ground control orders flags and updates with new field reports and hazards. *[shown_working]*
- Recommended actions — Fine-tuned local model suggests re-check, close inspection, dispatch or deprioritize; uncertain leads stay visible. *[shown_working]*
- Human approval and crew brief — Commander approves or overrides; Grok drafts a crew brief. *[shown_working]*
- Field report ingestion — Grok turns messy reports into an updated incident picture. *[shown_working]*
- Fly-vision reflex — Pretrained flyvis model plus custom readout produces brake/turn commands in a 3D carport sim. *[shown_working]*
- Neuron visualization — Adapted fly-brain viewer maps activity onto neurons. *[shown_working]*
- Mission log — Events stored in MongoDB Atlas. *[claimed]*

**Flow:** Simulated drone sweeps the flooded area → Flags appear in a ranked queue → Reports reorder the queue → Drone returns for close inspection of uncertain leads → Commander approves dispatch and a brief is drafted

**Prompt:** Best Overall at HackGT 13 is a prize listing with no description; build anything.
**Fit (none):** No specific sponsor prompt; open-brief entry.  *(targeted: Best Overall - 2nd)*
**Sponsor tools:** xAI Grok (field-report parsing and crew briefs, supporting); MongoDB Atlas (mission event logs, supporting)
**AI:** Fine-tuned local Laya model ranks leads; Grok summarizes reports; pretrained flyvis fly-visual-system model with a custom motion readout drives the reflex.
**Architecture:** Python/FastAPI simulator streams sightings by WebSocket to a TypeScript/Three.js dashboard; separate reflex service processes camera frames; MongoDB logging.
**Novelty:** Pairs a biologically inspired fly-vision reflex with LLM-assisted triage; fully simulated and explicit that no quantitative results exist yet.
**Scope:** large · working: 264-file repo with tests; working simulated loop per Devpost; no video. · polish: Restricted SharePoint deck; no quantitative evaluation.
**Claims:** Mapped flyvis activity onto tens of thousands of neurons in a 3D viewer
**Gaps:** no video; demo link restricted
Sources: https://devpost.com/software/flyby-fdxcua, https://github.com/monishramj/flyby, https://hackgt13.devpost.com/

---

### Fourteenth Floor
*HackGT HackGT 13 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** The Lighthouse Laboratory - 1st Place [1st]

**What it is:** Developer tool that turns a project folder into a 3D office where a manager agent and specialist Codex agents sit at desks. The manager writes code, specialists do read-only work, and tasks close only with evidence such as a diff or an observed passing test.
**Problem / user:** Developers running several coding agents who must read scrolling terminal logs to see who is working or blocked.

**Features**
- 3D office generation — Three.js office built from any project folder; inspect desks or walk the floor. *[shown_working]*
- Manager and read-only specialists — Only the manager writes code; specialists research, plan tests, check risks. *[shown_working]*
- Messaging and file scopes — Tracked agent-to-agent messages; declared scopes and meetings serialize edits to the same file. *[shown_working]*
- Evidence gate — Tasks close only with diff, observed passing test run, or existing screenshot. *[shown_working]*
- Stalled-agent replacement — Eject an agent; replacement resumes from a saved handoff. *[shown_working]*
- Accessibility and VR — Reduced motion, keyboard alternatives; WebXR mode built but untested on a headset. *[claimed]*

**Flow:** Point tool at a project folder → 3D office appears with agents at desks → Agents work via Codex sessions → Watch, inspect desks, or walk the floor → Tasks go to review and close with evidence

**Prompt:** The Lighthouse Laboratory (1st) has no public description on the listing.
**Fit (none):** No stated link; developer-tooling and agent-orchestration entry.  *(targeted: The Lighthouse Laboratory - 1st)*
**Sponsor tools:** Codex app server (runs each agent in sandboxed sessions, core); Blender MCP (AI-driven office modeling, supporting)
**AI:** Codex agents with code-enforced tools for delegation, status, messaging and acknowledgment rather than prompt-only rules; manager/specialist roles.
**Architecture:** Local Node server for persistence, replay and Git checkpoints; Vite/Three.js client; Codex app server sessions on isolated profiles; Python Blender pipeline.
**Novelty:** Makes agent coordination spatially visible and enforces closure rules in code; reports reliability gains from roles and review rather than prompts.
**Scope:** medium · working: Repo with 124 files and tests; run instructions need Codex CLI; no video or live URL. · polish: Accessibility options; ~2.8k LOC counted; no quantitative claims.
**Claims:** Agents cannot close tasks without evidence
**Gaps:** no video
Sources: https://devpost.com/software/fourteenth, https://github.com/Pudging/fourteenth-floor, https://hackgt13.devpost.com/

---

### HeirLoom
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Meta: Bringing People Closer Together with AI - Winner

**What it is:** A native iOS app where a voice AI companion, Loomie, talks aloud with older relatives about their memories and an analysis backend turns the stories into a shared family archive: a corkboard family tree, cross-generation 'Sparks' and a 3D globe.
**Problem / user:** Spread-out families whose elders' oral histories and life lessons vanish unrecorded, and younger relatives who want to hear and keep them.

**Features**
- Loomie voice companion — Full-duplex xAI real-time voice over WebSockets from AVAudioEngine at 24 kHz; sensory-detail prompts and tuned voice-activity detection so pauses do not cut speakers off. *[claimed]*
- Corkboard family tree — SwiftUI board with pinned Polaroid cards and red twine, custom layout for pushpins, tilts and Bezier strings. *[claimed]*
- Post-session analysis — FastAPI service with Grok 4.3 extracts relatives, enriches profiles and updates the tree without forms. *[claimed]*
- Sparks — New stories compared to the family archive to link shared passions and trades across generations. *[claimed]*
- 3D heritage globe — MapKit globe plotting hometowns, migrations and story locations. *[claimed]*
- iOS share extension — Send photos and voice memos from the camera roll or Instagram into the family feed. *[claimed]*
- Dialogue memory — Backboard.io state machine tracks dialogue history, relationships and facts so Loomie avoids repeating itself. *[claimed]*
- Picture books, keepsake export, spatial gallery — Listed as next steps (Grok Imagine, print export, Vision Pro and Meta XR). *[planned]*

**Flow:** Storyteller opens the iOS app and speaks with Loomie → Loomie asks about sensory details and guides the story → Memories pin onto the family corkboard → Backend analyses the session and updates relatives and the tree → Sparks and the globe surface connections → Family members add photos via the share extension

**Prompt:** not public / not found
**Fit (implied):** Uses AI voice to connect generations and preserve family history; README states it won the Meta track. Meta challenge text was not found, and no Meta model is listed in the stack.  *(targeted: Meta: Bringing People Closer Together with AI - Winner)*
**Sponsor tools:** Backboard.io (Dialogue state and long-term memory, core); xAI Grok (Real-time voice and post-session analysis, core); MongoDB Atlas (Stores members, stories and relationships, supporting)
**AI:** xAI real-time voice for conversation, Grok 4.3 for entity extraction, summarisation and kinship resolution, Backboard state machine for grounding across sessions.
**Architecture:** SwiftUI iOS client streaming audio to the xAI Realtime API and calling a FastAPI backend (motor, MongoDB Atlas) that also calls Backboard.io; share extension target in the same Xcode project.
**Novelty:** Hand-built corkboard and twine layout and a custom voice-activity setup for slow elderly speech; fully native audio pipeline instead of a web voice widget.
**Scope:** medium · working: README with architecture diagram, iOS and FastAPI code about 20k LOC; no video or live link, tests not flagged. · polish: Custom artwork and layouts described, README detailed; no tests or CI.
**Claims:** All artwork custom, no AI-generated or stock assets | Full-duplex low-latency voice (no figures) | Won the Meta track
**Gaps:** No demo video or live link; README setup section not read in full; Meta challenge text not found; Devpost says Instagram-only share, README says any app
Sources: https://devpost.com/software/heirloom-3q2bn9, evidence/hackgt-hackgt-13-heirloom.json

---

### Hey Buddy
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** MLH: Best Use of ElevenLabs

**What it is:** A phone interpreter you add to any live call by dialing Buddy's number and merging: it translates turn by turn between English and the user's language, warns in that language about scam tactics, and logs calls to a portal; businesses get tracking numbers that turn interpreted calls into CRM records.
**Problem / user:** Older immigrants who freeze or get scammed on English phone calls, their families, and businesses or safety hotlines that miss details from callers with limited English.

**Features**
- Three-way live interpretation — Twilio Media Streams audio is transcribed by ElevenLabs Scribe, translated by Grok and voiced by ElevenLabs; detected language decides who spoke. *[shown_working]*
- Six languages — English, Turkish, Spanish, Arabic, Hindi (beta) and Mandarin (beta) with a native voice each. *[claimed]*
- Scam warnings — Grok checks the other party's turns for six manipulation cues, warns in the user's language and via WhatsApp, quoting exact words and never declaring a call safe. *[claimed]*
- User portal — Phone number plus PIN login; each call as a thread with original and interpreted text, per-turn audio and a short summary written by Muse Spark. *[claimed]*
- Business tracking numbers and CRM — A unique number per line; each call becomes a record with source, intent, outcome and bilingual transcript; urgent safety calls marked escalated; dashboard by line, language, intent. *[claimed]*
- Localised web app — Web app and CRM in six languages with right-to-left layout for Arabic. *[claimed]*
- Hardening — Caller speech treated as data, login rate limits, per-key data isolation. *[claimed]*

**Flow:** During any call tap Add call, dial Buddy and Merge → Buddy greets both sides then interprets each turn → If cues of a scam appear, user hears a warning and gets a WhatsApp message → After the call review transcript, audio and summary in the portal → Businesses see the call logged in the CRM

**Prompt:** not public / not found
**Fit (implied):** ElevenLabs Scribe v2 does speech-to-text with language detection and Flash v2.5 does native-voice text-to-speech in the live call pipeline. MLH prize text not fetched.  *(targeted: MLH: Best Use of ElevenLabs)*
**Sponsor tools:** ElevenLabs (Scribe v2 transcription and Flash v2.5 voices in six languages, core); Twilio (Phone number and Media Streams call audio, core); xAI Grok (Per-turn translation and scam-cue analysis, core); Meta Muse Spark (Post-call summaries, supporting)
**AI:** Pipeline of STT, Grok translation with a scam-term glossary, parallel Grok cue analysis, and TTS; Muse Spark moved to summaries after exceeding the 8 second live budget.
**Architecture:** Twilio webhook opens a Media Streams WebSocket to a Node/Express/Socket.IO server that segments utterances and streams voice back; React/Vite/Tailwind app served from one Railway process with a persistent volume at hey-buddy.tech.
**Novelty:** Needs no app: joins a standard merged call as a third party and pairs interpretation with live scam-cue warnings, plus a business-side CRM view.
**Scope:** large · working: Live site, demo video, and reported timings from real merged calls including Turkish; other languages tested on phone-quality audio. · polish: Six-language web app and CRM, security audit, WhatsApp fallback; repo not readable.
**Claims:** Grok translation about 0.6 to 0.8 s versus earlier 3 to 13 s spikes | Full turn time 1.1 to 1.4 s on a real merged call | Median end-of-speech to Buddy speaking 1.4 to 1.8 s | Verified on real Turkish calls
**Gaps:** Evidence clone failed and README not retrievable on raw.githubusercontent.com (404 on HEAD/main/master); repo may be private or removed; Video and live site not opened; ElevenLabs prize text not fetched
Sources: https://devpost.com/software/hey-buddy-3e4utl

---

### Inkling
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Notability: Trust the Process

**What it is:** A lecture note-taking canvas for iPad and Apple Pencil that keeps erased handwriting as faint 'ghost ink', timestamps strokes to the lecture, and builds a review timeline of corrected misconceptions, unresolved gaps and breakthroughs with AI re-explanations.
**Problem / user:** Students whose final notes hide where they got stuck; also teachers who want an anonymous view of where a class slowed down.

**Features**
- Ghost ink — Erased strokes remain as dashed teal ink, toggleable, each stroke stored with lecture second, speed and pressure. *[shown_working]*
- Signal Lab stuck-moment detection — Every 10 seconds scores pauses during lecture speech, slowdown versus the student's own baseline, extra erasing and pen pressure; each flag lists which signals fired. *[shown_working]*
- Misconception pairing and gaps — Matches an erase to a nearby rewrite by overlap as a corrected misconception; unrewritten erasures become gaps carried into later sessions. *[shown_working]*
- AI re-teaching with check question — Gemini reads before/after handwriting; Groq writes a short re-explanation and question, graded server-side; a right answer becomes a breakthrough. *[shown_working]*
- Replay 20s and multilingual spoken help — Replays the missed 20 seconds of lecture; explanations offered in 10 languages and read aloud via ElevenLabs. *[shown_working]*
- Notability comparison and PDF export — Overlay slider compares a clean Notability export with the hidden erased ink; ghost ink and moments export as PDF. *[shown_working]*
- Teacher class heatmap — TimescaleDB continuous aggregate finds class-wide slowdowns; anonymous, groups under three suppressed. *[shown_working]*
- Live lecture transcription — Transcribes the professor in the browser so detection works without a recording; disabled in public demo. *[claimed]*

**Flow:** Open a seeded recorded lecture (or start live) and write notes → Ink is timestamped; pace meter shows steady, slowing or stuck → Open session review to see a learning timeline of ghost ink → Open the 01:40 correction to see before/after crops and AI reading → Answer the check question to earn a breakthrough → Open the 04:10 gap and press Replay 20s → Compare with Notability export, then view Progress and class hotspots

**Prompt:** not public / not found
**Fit (explicit):** Page has a section on using Notability Pro to import the lecture and for research/design, plus an in-app compare view and PDF export aimed at Notability; the process of mistakes is the product.  *(targeted: Notability: Trust the Process)*
**Sponsor tools:** Notability (Lecture import for research/design, comparison of clean export against ghost ink, PDF export, supporting); ElevenLabs (Spoken explanations, supporting); Tiger Data (TimescaleDB) (Pen-sample hypertable and class hotspot aggregate, supporting)
**AI:** Gemini interprets erase-versus-rewrite handwriting crops; Groq gpt-oss produces explanations, check questions and translations under strict JSON schemas; detection itself is a deterministic TypeScript engine; provider-agnostic AI layer with offline fixtures for demo.
**Architecture:** Next.js 16 app with pointer-event ink canvas; Signal Lab TypeScript engine; SQLite or Postgres/TimescaleDB store; AI provider layer (Gemini, Groq, ElevenLabs); pdf-lib export; Dockerised on Railway with DEMO_MODE fixtures.
**Novelty:** Treats erased handwriting as the data signal and uses per-student baselines rather than class averages; solo build with large test suite and an offline, seeded demo mode.
**Scope:** large · working: Live site, seeded demo, 850+ unit and 100+ Playwright tests claimed, 45k LOC repo, 3-minute demo video. · polish: Marketing page, About page, Railway deploy docs, self-hosted fonts, offline demo path, privacy design.
**Claims:** Full erase-flag-re-teach-breakthrough loop works live in under a minute | 850+ unit/integration and 100+ Playwright end-to-end tests | Built solo in one weekend | No formal detection accuracy measured yet
**Gaps:** Notability prize text not published; Video not watched
Sources: https://devpost.com/software/inkling-ud1re3, https://github.com/PranavNagothu/Inkling (evidence README)

---

### Lullabuy
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** VISA: Reimagine Shopping - Winner

**What it is:** A checkout for used baby gear that authorizes the buyer's Visa payment without capturing, then at pickup reads the product label from a photo and checks CPSC and NHTSA recalls and banned product types; clean items capture the hold, recalled or banned ones reverse it.
**Problem / user:** Parents buying used cribs, bassinets or car seats from strangers, where recalled or banned items slip through peer-to-peer handoffs; also marketplace trust-and-safety teams.

**Features**
- Visa payment hold, capture or reversal — Card typed into Visa Microform, authorization with capture off; pickup result decides capture, reversal, or keep-held when uncertain. *[shown_working]*
- Label scan and recall matching — Barcode, Gemini label-text reading and in-browser CLIP classifier feed a matcher over 1,136 CPSC and 71 NHTSA recalls with batch-specific rules. *[shown_working]*
- Banned-type photo classifier — CLIP ViT-B/32 embedding plus trained head via transformers.js; reports macro-F1 0.72 on unseen products versus 0.56 zero-shot. *[shown_working]*
- Voice and typed shopping agent — Gemini/ElevenLabs agent filters 1,662 pre-scanned eBay and Craigslist listings; red listings cannot be bought. *[shown_working]*
- Trusted Agent Protocol and MCP tool — AI-agent checkouts signed per RFC 9421 and verified; recall check exposed as an MCP tool and public API. *[shown_working]*
- Recall phone call and recall watch — Vonage/ElevenLabs call on reversal; daily job rechecks captured sales and sends web push if later recalled. *[shown_working]*
- Solana item passport — SHA-256 of the pickup record written to a devnet Memo transaction and a Metaplex Core asset; passport page re-verifies it. *[shown_working]*
- Deal board, kiosk and mobile app — Atlas change streams update a live deal view; USB-scanner kiosk for swap meets; Expo app with Android APK. *[shown_working]*

**Flow:** Say or type what you need; agent returns pre-screened listings → Agree on price and enter card in Visa Microform to place a hold → Meet seller and photograph the product label → App reads barcode and label and runs recall and banned-type checks → Hold is captured on no match, reversed on recall or ban, kept if uncertain → Buyer gets a call naming the recall on reversal; captured sale gets an on-chain passport

**Prompt:** not public / not found
**Fit (explicit):** Rebuilds the used-goods checkout around a Visa authorize-then-capture hold gated by a safety check, using Microform, Token Management, card-linked offers and Trusted Agent Protocol for agent purchases.  *(targeted: VISA: Reimagine Shopping - Winner)*
**Sponsor tools:** Visa Acceptance (authorize/capture/reverse) (Payment hold, capture and reversal in sandbox, core); Visa Microform (Hosted card entry, core); Visa Token Management Service (Saved cards and card-linked offers, supporting); Visa Trusted Agent Protocol (Signed AI-agent checkouts, supporting); MongoDB Atlas (Deals, change streams, vector search, core); ElevenLabs (Voice shopping agent and recall call, supporting); Notability (Notes and practice quiz for rehearsal, token)
**AI:** Gemini 3.5 Flash turns requests into filters and reads label photos but never decides allow/deny; Gemini also extracted model/batch/UPC from recalls with verbatim checks; custom CLIP head classifies banned types; Atlas vector search matches recall photos.
**Architecture:** Next.js 16 on Vercel with MongoDB Atlas state, Visa sandbox APIs, recall index built from CPSC/NHTSA, in-browser classifier, MCP endpoint, Solana devnet writes, Vonage calls, and an Expo mobile client.
**Novelty:** Uses a payment hold as the safety enforcement point, with trained and evaluated models, held-out splits, hand-checked recall extraction and an honest status endpoint; unusually broad integration surface for a weekend.
**Scope:** large · working: Live site, public check API, tested end-to-end Visa auth/capture/reversal, Android APK release, measured model results in docs/FACTS.json. · polish: CI with e2e and secret scanning, judge page, trust console, motion design, documented hand checks.
**Claims:** Banned-type model macro-F1 0.7243 vs 0.558 zero-shot CLIP | 2 of 107 ordinary items wrongly flagged vs 38 for zero-shot | 1,662 real listings scanned; flags fell from 39 to 9 | 820 recalls matchable after Gemini extraction (from 449) | Photo search ranked correct recall first in 60 of 144
**Gaps:** No demo video on Devpost; Visa Direct payout written but not enabled; Prize text not published
Sources: https://devpost.com/software/lullabuy, https://github.com/StephenSook/secondhand-safe (evidence README)

---

### MiiHab: Get Back in the Game
*HackGT HackGT 13 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** The Lighthouse Laboratory - 2nd Place [2nd]

**What it is:** Wii-style VR physical therapy: patients wearing a Meta Quest and AirPods play golf, bowling and guided exercises measured from their own motion, coached by a voice AI named Alex, while a clinician portal shows live rep-by-rep data and pushes signed plan updates.
**Problem / user:** Rehab patients who get roughly one therapist hour a week and little feedback between visits, plus the physicians monitoring them.

**Features**
- Motion-measured VR games — Unity golf and bowling driven by AirPod CoreMotion and Quest head tracking. *[shown_working]*
- Movement studio — Guided shoulder raises and curls counted rep by rep. *[shown_working]*
- Alex voice coach — ElevenLabs voice with Meta Muse Spark; coaches from measured values, follows the care plan, stops at pain 7 or higher. *[shown_working]*
- Clinician EHR portal — Live rep updates, pain and quality tracking, replay, signed plan updates pushed to headset. *[shown_working]*
- Social features — Friends, messaging, group sessions, Muse-suggested intros and streak cards. *[claimed]*

**Flow:** Patient wears Quest and AirPods → Alex greets and coaches during play → Movements are measured; session stops at pain 7+ → Clinician watches live and signs plan updates → Alex explains the changes next session

**Prompt:** The Lighthouse Laboratory (2nd) has no public description on the listing.
**Fit (none):** No stated link; devpost lists only the result. Uses Meta Quest/Muse and ElevenLabs.  *(targeted: The Lighthouse Laboratory - 2nd)*
**Sponsor tools:** ElevenLabs Conversational AI (Alex voice and listening, core); Meta Muse Spark (language model and social suggestions, core)
**AI:** Muse Spark LLM with tool calls to read care plan and measurements, log pain, request plan review; ElevenLabs for speech; custom adapter keeps key local.
**Architecture:** Unity Quest app over USB to a Mac; Swift CoreMotion AirPod streams from two Macs merged by a Tailscale relay; Node coordinator; React clinician portal.
**Novelty:** Uses AirPods as body-motion sensors for VR rehab, with two-Mac relay for two AirPod pairs and camera-free tracking.
**Scope:** large · working: Demo video and detailed Devpost hardware setup; repo could not be cloned for inspection. · polish: Multiple components; no clinical validation.
**Claims:** Coach stops sessions at pain 7+ | Works without camera, even in the dark
**Gaps:** repo clone failed, README unread
Sources: https://devpost.com/software/rehabmii-get-back-in-the-game, https://hackgt13.devpost.com/

---

### Nudge
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Meta: Bringing People Closer Together with AI - Winner

**What it is:** An iOS app with an AWS backend that sends both friends a nudge when their calendars show free time, runs a 1:1 video call, shows photos from the speaker's camera roll when they mention an event, and summarizes the call for follow-ups.
**Problem / user:** Pairs of friends or family who mean to call each other but default to texting because of uncertainty about timing.

**Features**
- Mutual free/busy nudges — Only free/busy blocks plus focus, driving and awake signals leave the device; when both are free both phones get a nudge, with Skip reason. *[claimed]*
- 1:1 video call — Amazon Chime SDK for iOS with data messages for photo offers; accept from lock screen via VoIP push. *[claimed]*
- Photo surfacing during calls — Transcribe streams speech; Nova Lite detects a photo reference; Titan embeddings search indexed photos; speaker sees an Ask first card before sharing. *[shown_working]*
- Photo safety gate — Rekognition moderation, OCR for IDs/documents/screenshots and a Nova sensitivity check before indexing; photos kept 30 days and deletable. *[shown_working]*
- Post-call summaries and follow-up topics — Nova Lite summarizes the call and extracts open items that seed a later nudge; both can view and delete. *[claimed]*
- Adaptive timing and auto-replies — Rule-based scheduler tunes nudges from response history; Nova Lite drafts replies like in a meeting. *[claimed]*
- Tap-to-add friends — Two iPhones held together use UWB Nearby Interaction, knock detection fallback, and MultipeerConnectivity. *[planned]*

**Flow:** Two people add each other by tapping phones → Both get a nudge when both are free → One accepts and a video call begins (or skips) → Mentioning a past event surfaces a matching photo under Ask first → Speaker taps Show to share it → Summary is generated; follow-up topics seed a later nudge

**Prompt:** not public / not found
**Fit (explicit):** Uses AI to lower the friction of reconnecting with close friends: timing nudges, in-call photo recall and follow-up memory, on a single-friendship model.  *(targeted: Meta: Bringing People Closer Together with AI - Winner)*
**AI:** Amazon Bedrock Nova Lite handles photo-reference detection, queries, captions, summaries, follow-ups, auto-replies and sensitivity checks; Titan Multimodal Embeddings for photo search in S3 Vectors; Rekognition and Transcribe.
**Architecture:** SwiftUI iOS app with NudgeKit package; AWS CDK stack with API Gateway HTTP/WebSocket, Lambda, DynamoDB, S3 Vectors, SQS, Cognito, Chime and Bedrock; headless peer-bot for testing.
**Novelty:** Spec-driven build with decision log, eval harnesses for detector, retrieval and safety, and a scripted peer bot for two-party tests; privacy-first free/busy only design.
**Scope:** large · working: Deployed dev stage with integration and simulator E2E tests; APNs/VoIP and UWB not verified on real devices. · polish: 212 deterministic screenshots, WCAG AA colors, docs for spec, decisions and milestones.
**Claims:** Detector precision 1.000, recall 0.896 on 140 windows | Retrieval top-1 1.000 on 60 photos | About 1.0 s p50 transcript to suggestion | 93 unit, 31 integration, 62 XCTest tests
**Gaps:** No demo video; Real-device push and UWB unverified; Meta prize text not published; No Meta tools named
Sources: https://devpost.com/software/nudge-hcvxfq, https://github.com/AlanRoybal/hackgt (evidence README)

---

### PledgeCheck
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** MLH: Best use of Vultr

**What it is:** A web workflow for isotretinoin clinics to verify at-home pregnancy tests: a one-time link opens a live-camera capture with a hidden handwritten challenge code, fraud checks and two readers run, and a dermatologist approves in one tap. A hash-chained audit log is anchored to Solana.
**Problem / user:** Dermatology clinics that must prevent faked or misread at-home iPLEDGE pregnancy tests, plus patients avoiding monthly clinic trips and drug makers wanting anonymous aggregates.

**Features**
- One-time link and timed session — Clinic approval emails a single-use link (24h expiry); tapping Start opens a 40-minute session and reveals a 4-character code to write on the test. *[shown_working]*
- Live-camera-only capture — No gallery uploads; server timestamps the photo; English and Spanish voice guidance from pre-generated ElevenLabs clips. *[claimed]*
- Photo fingerprint reuse blocking — Perceptual hash on a Vultr OpenCV service rejects reused photos across clinics when under 8 of 64 bits differ. *[shown_working]*
- Dual readers with rules engine — Grok vision reads result and code; non-AI OpenCV measures test lines; disagreement or confidence below 85% routes to a doctor. *[shown_working]*
- One-tap dermatologist review — Review card shows photo, both readings, fraud warnings and timeline; approval opens a 7-day pickup window; software never approves alone. *[shown_working]*
- Tamper-evident audit log with Solana anchor — SHA-256 hash chain; head fingerprint written to Solana devnet every 10 events; Verify screen recomputes and compares. *[shown_working]*
- Drug-maker analytics — De-identified weekly totals in Tiger Data with small counts hidden; failures designed not to block approvals. *[claimed]*

**Flow:** Patient requests a refill from the dashboard → Clinic approves and an emailed one-time link is sent → Patient taps Start and sees the 4-character code → Patient writes the code on the test and photographs it live → Fraud checks and both readers run → Dermatologist approves or rejects in one tap → Approval opens pickup window; all actions logged and anchored

**Prompt:** not public / not found
**Fit (explicit):** Runs the Python/OpenCV image-fingerprinting and non-AI line-reading service on a Vultr server at its own domain, serving as the second independent reader.  *(targeted: MLH: Best use of Vultr)*
**Sponsor tools:** Vultr (Hosts OpenCV image service for hashing and line measurement, core); Tiger Data (De-identified analytics warehouse, supporting); ElevenLabs (Pre-recorded voice guidance, supporting); Solana (Anchoring audit-log hash, supporting); Stripe (Listed in built-with, undescribed, unclear)
**AI:** Grok vision reads test result and handwritten code; OpenCV provides an independent non-AI reading; a deterministic rules engine, not an LLM, decides routing; a doctor makes the final call.
**Architecture:** Next.js on Vercel with Supabase (Postgres, RLS, auth) calls Grok and a Vultr OpenCV service, applies rules engine, queues for dermatologist review, writes audit chain to Supabase, Solana, and de-identified events to Tiger Data.
**Novelty:** Targets a concrete upcoming FDA rule change with layered fraud controls and candid limitations; separates AI and non-AI readers and anchors audit hash on-chain.
**Scope:** large · working: 450+ web tests and 78 database checks claimed; approvals work locally; README admits nothing deployed at writing, Devpost lists a demo domain. · polish: Honest status table, audit docs, role-based login, QR link issuing; OpenCV reader uncalibrated.
**Claims:** 450+ automated web tests and 78 database checks | Grok read all six real test photos correctly (small sample) | OpenCV misread 4 of 6 real photos, openly reported | Hash match threshold under 8 of 64 bits
**Gaps:** README says nothing deployed while Devpost lists a demo domain; feature list follows Devpost; Vultr prize text not published; Video not watched
Sources: https://devpost.com/software/pledgecheck-qrusc1, https://github.com/adrit-ganeriwala-05/PledgeCheck (evidence README)

---

### Pose
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** MLH: Best Use of Tiger Data

**What it is:** A small ESP32 + BNO055 wearable that calibrates an upright baseline, detects sustained slouching and sends episodes over browser Bluetooth to a Rails web dashboard with accounts, friend groups and weekly slouch-share rankings.
**Problem / user:** Students and desk workers who forget their posture during long study or coding sessions.

**Features**
- On-device calibration and slouch detection — Firmware stores an upright baseline, classifies posture and times episodes, separating brief movement from sustained slouching. *[claimed]*
- Browser BLE pairing and live readings — Web page pairs over Bluetooth Low Energy, shows live state, queues uploads, flags stale or disconnected data. *[claimed]*
- Duplicate-upload protection — Upload handling avoids double-counting repeated snapshots; tests cover timing and upload logic. *[claimed]*
- Accounts and history — Username/password accounts store snapshots in a Tiger Cloud TimescaleDB hypertable; Day/Week/Month charts. *[shown_working]*
- Friend groups and rankings — Invite codes form groups; weekly ranking by percent of tracked time slouching; separate most-improved highlight. *[claimed]*
- Muse conversational coach — Planned workspace guidance via Muse; /coach exists dev-only and no live response verified. *[planned]*

**Flow:** Calibrate wearable upright → Wear while studying → Wearable times slouch episodes → Browser receives data over BLE and uploads to Rails app → View live posture, today card and charts → Join friend group and check weekly rankings

**Prompt:** not public / not found
**Fit (implied):** Stores posture snapshots in a Tiger Cloud TimescaleDB hypertable verified against a real instance, behind authenticated storage feeding the history charts and group rankings.  *(targeted: MLH: Best Use of Tiger Data)*
**Sponsor tools:** Tiger Data (TimescaleDB) (posture_snapshots hypertable and history, core); Meta Muse (Planned coach, dev-only, token)
**AI:** No ML in sensing; posture is threshold logic on IMU data. Muse is planned as a conversational coach; AI coding assistants helped build it.
**Architecture:** ESP32 firmware reads BNO055 and advertises over BLE; browser Web Bluetooth relays snapshots to a Rails app persisting into Tiger Cloud TimescaleDB; dashboard shows rankings.
**Novelty:** Physical wearable plus social competition layer; repo has extensive numbered decision records and a grader note file.
**Scope:** medium · working: Rails persistence verified against Tiger Cloud; README says physical wearable verification pending and deployment deferred. · polish: Mobile-first dashboard, themes, decision docs; no demo video or link.
**Claims:** Physical end-to-end verification still a next step
**Gaps:** Devpost title is Posture Pal while repo calls it pose; README opens with an instruction aimed at AI graders, ignored; Prize text not published; No video or demo
Sources: https://devpost.com/software/posture-pal-ul3hfa, https://github.com/Keipydesu/buzzbuzzlovers (evidence README, partial)

---

### ReelFriends
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Notability: Trust the Process

**What it is:** A mobile web game where each person is a fish; voice onboarding builds an interest profile, tapping a friend's NFC tag plays a cutscene of shared interests, and met friends populate a personal beach, with an Arduino badge showing name and fish.
**Problem / user:** People who rarely meet new people in person and find approaching strangers awkward, such as classmates sharing a space.

**Features**
- Voice onboarding to profile — Spoken answers transcribed with ElevenLabs Scribe; Muse Spark extracts interests with quote evidence; user edits before saving. *[shown_working]*
- Fish avatar customization — Hand-drawn accessory overlays aligned on the same canvas as the base fish. *[shown_working]*
- NFC tap cutscene — Tag holds a URL; tap opens browser app and plays cutscene of shared interests, or fish may clam up with retry later. *[claimed]*
- Personal beach and hangouts — Met people appear on your beach with speech bubbles; repeat meets unlock hangout scenes at higher levels. *[shown_working]*
- Opt-in fish recommendations — Shared-interest people swim around your island, cached with a 30-minute refresh; tapping their tag in person brings them ashore. *[claimed]*
- Hardware badge — Arduino Uno drives an LCD with name and scrolling interests and a TFT showing the fish. *[claimed]*
- Dev tooling and mock mode — Scripts to seed fish, simulate meets and unfriend; mock AI mode runs with zero calls. *[shown_working]*

**Flow:** Answer voice onboarding prompts → Review and edit the extracted profile and customize fish → Tap a friend's NFC tag with phone → Watch the friendship cutscene or clam-up → See the friend on your beach → Meet again to unlock hangouts

**Prompt:** not public / not found
**Fit (explicit):** Page has a Notability section: all art and UI drawn in Notability, with accessories drawn at matching canvas size so overlays align in code.  *(targeted: Notability: Trust the Process)*
**Sponsor tools:** Notability (Drawing all art and UI assets, supporting); Meta Muse Spark (Meta Model API) (Profile extraction, overlap analysis, dialogue, recommendations, core); ElevenLabs (Voice prompts and Scribe transcription, core); MongoDB Atlas (Profiles, pairs, cutscenes, cached AI, supporting)
**AI:** Muse Spark returns structured JSON validated by Zod for profile extraction, semantic overlap, dialogue and recommendations; prompts tuned to avoid vague labels and date-like tone; caching and mock mode control credit use.
**Architecture:** Next.js/TypeScript mobile web app on Vercel; ElevenLabs voice in and out; Muse Spark via API; MongoDB Atlas or JSON file storage; custom canvas beach loop; NFC tags as URLs; Arduino badge.
**Novelty:** Uses physical NFC taps and a hardware badge to push online matching into in-person meetups, with an evidence-quoted profile and consent-first appearance.
**Scope:** medium · working: Live demo domain, mock/live AI modes, tests and many CLI tools in README; NFC and badge not shown on video. · polish: Custom hand-drawn art, scenes, dev impersonation tools; no video.
**Claims:** Built in 36 hours | Caching made replays and re-taps free within a 50-dollar AI credit budget
**Gaps:** No video; Prize text not published
Sources: https://devpost.com/software/reelfriends, https://github.com/deadly-nightshade/hackatgt26 (evidence README)

---

### Rescu
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** MLH: Best Use of Solana

**What it is:** A simulated disaster-relief system on Solana: a multi-hazard model scores census tracts at hurricane landfall, relief tokens are airdropped to household wallets, spendable only at registered local stores under on-chain rules, with a Grok shopping agent and an anomaly oracle that suspends price gougers.
**Problem / user:** Hurricane survivors who wait weeks for restricted aid or receive fast but misusable cash; implied users are residents, merchants and disaster officials.

**Features**
- Need-scoring model — Scores 83,241 census tracts on wind, rain, surge, housing and vulnerability; payouts clamped 250 to 2,000 dollars; matched FEMA county split 0.64 vs 0.38 on 23 hurricanes. *[shown_working]*
- Landfall airdrop of Relief Dollars — Official declares disaster and funds it; aid lands in household wallets as the storm moves, median 0.93 s in a 20,000-household run. *[shown_working]*
- On-chain spending rules — Token-2022 transfer hook enforces registered stores, disaster zone, 200 dollar order cap, 300 dollar daily cap, no peer transfers. *[shown_working]*
- Grok shopping agent — Builds baskets from live store shelves, waits for user confirm, bounded by on-chain cap. *[shown_working]*
- Fraud oracle — Anomaly detection flags price gouging; Grok writes case summary; one click suspends a store on-chain. *[shown_working]*
- Day-30 expiry — Unspent aid returns to treasury while stores keep earnings. *[shown_working]*
- Command Center and apps — 3D hurricane map, treasury and feed, 13-attack break-it panel, resident app with QR claim, merchant terminal, time-travel dashboard. *[shown_working]*

**Flow:** Official declares and funds a disaster → Aid airdrops neighborhood by neighborhood → Resident scans QR to receive aid → Resident asks Grok to shop and confirms the basket → On-chain rules accept or reject payments → Oracle flags a gouging store and official suspends it → Day 30 returns unspent aid

**Prompt:** not public / not found
**Fit (explicit):** Core logic lives in a Rust Anchor program on devnet with a Token-2022 transfer hook enforcing spending rules, sub-second airdrops and on-chain store suspension.  *(targeted: MLH: Best Use of Solana)*
**Sponsor tools:** Solana (Anchor, Token-2022 transfer hook) (Registry, treasury, spending rules, suspension, core); Vultr (Hosts Solana validator and simulation, supporting); Tiger Data (TimescaleDB) (Streaming payments and live dashboard aggregates, supporting); Grok (xAI) (Shopping agent and case summaries, supporting)
**AI:** Hazard-based need model trained against FEMA outcomes; Grok shopping agent checks live shelves before proposing baskets; anomaly oracle flags price gougers with Grok-written summaries.
**Architecture:** Anchor program on Solana devnet; Fastify simulator of 20,000 households and 500 stores on a Vultr validator; Postgres/PostGIS/TimescaleDB; Python model; Next.js with deck.gl and WebSockets.
**Novelty:** Combines a validated disaster-need model with programmable restricted money and a fraud oracle, load-tested at 20,000 households; built solo.
**Scope:** large · working: Live site, devnet program, full benchmark run with reported figures, video. · polish: Four interfaces, 3D hurricane map, time-travel dashboard, stated limitations; stores and identity mocked.
**Claims:** Median 0.93 s storm-to-wallet across 20,000 households | 19,997,202.94 dollars delivered, 0 failed; 423 bad payments blocked | Oracle precision 0.99, recall 0.87, caught 10 of 10 gougers | Beat wind-only rule on 22 of 23 storms | Built solo in 36 hours, about 30 cents of AI credits
**Gaps:** Prize text not published; Video not watched
Sources: https://devpost.com/software/rescu-qfuz8e, https://github.com/NikhileshThiru/rescu (evidence README)

---

### Ripple
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SpaceXAI: Make it Legendary

**What it is:** An interactive Atlanta map of MARTA rail access that simulates station or destination closures, disasters described in plain language, and planned new facilities, showing added travel time to hospitals, groceries and schools by community.
**Problem / user:** Transit-dependent and lower-income Atlanta residents who lose access to essentials when stations close; planners and policymakers as implied users.

**Features**
- Disrupt tab — Put a station on maintenance or shut a station or destination; communities shaded by added travel time with a panel of who is affected and where visitors shift. *[shown_working]*
- Intelligence tab — Plain-language event (e.g. earthquake near Midtown) interpreted by Gemini, falling back to Grok then ChatGPT; closes stations, destroys destinations, triggers evacuation and fills hospitals. *[shown_working]*
- Plan tab — Place a new destination or build a budgeted site set; areas saving 15+ minutes turn green; optimal siting for lowest average distance or lower-income benefit. *[shown_working]*
- Report tab — Add or remove stations and destinations in the shared database, permanently. *[claimed]*
- Access simulation — Runs in browser; displaced households reroute to next-best reachable destination; single-destination services like schools do not reroute. *[shown_working]*
- Equity insights — Census and CMS data show lower-income regions up to 3x more affected by closures. *[claimed]*

**Flow:** Open Atlanta map with stations and destinations → Close a station and view shaded travel-time impact → Click a hospital to see most damaging stations → Describe a disaster in the Intelligence chat → Use Plan to add or suggest a facility → Submit a report to correct data

**Prompt:** not public / not found
**Fit (implied):** Uses Grok (xAI) as one of three language models interpreting disaster scenarios and summarizing impact; the track is only known by name, so fit is inferred.  *(targeted: SpaceXAI: Make it Legendary)*
**Sponsor tools:** Grok (xAI) (Second-choice scenario interpretation and summaries, supporting); Tiger Data (TimescaleDB) (Postgres/PostGIS store for network and destinations, supporting)
**AI:** Gemini, then Grok, then ChatGPT in fallback order turn natural-language events into closures, destroyed destinations and evacuation zones; a statistical model estimates daily destination visits.
**Architecture:** React/Vite/MapLibre/deck.gl frontend running access simulation in browser; FastAPI backend with LLM Intelligence endpoints; Postgres with PostGIS and TimescaleDB; loaders for GTFS, Census, OSM, CMS.
**Novelty:** Combines transit-access simulation with an LLM disaster scenario layer and equity-targeted facility siting on real Atlanta data.
**Scope:** medium · working: Live demo domain and four working tabs per README; video link on Devpost. · polish: Colour-coded tabs, shared state between chat and Disrupt, design doc; few quantitative validations.
**Claims:** Lower-income regions up to 3x more affected by closures | Optimal new-site placement for distance and equity overlaps strongly
**Gaps:** Prize text not published; Devpost calls model a neural network while saying statistical; unclear
Sources: https://devpost.com/software/ripple-vepi8b, https://github.com/MannanB/HackGT13 (evidence README)

---

### SideQuests
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** MLH: Best Use of MongoDB Atlas

**What it is:** An iPhone app that turns free time into a timed, personalised plan of nearby events and places with transit legs, which can be private, shared or posted to a forum, with group chat, shared album and expense splitting. The Devpost page also bundles a separate synthetic-speech detector for another track.
**Problem / user:** Travellers and students with unplanned free time who juggle maps, calendar, chat and payment apps to find and organise things to do.

**Features**
- Timed plan generation — User sets window, range and mood; planner retrieves candidates by geo/time and solves a DAG itinerary, returning three plans in under a second. *[shown_working]*
- Taste model — Qwen3 embeddings of likes, dislikes and events feed a trained compatibility classifier; NDCG@10 0.897 vs 0.849 cosine baseline. *[shown_working]*
- Plan editing and sharing — Drag to reorder with auto re-timing, swap stops, keep private, share with friends or post to Forum with cap and lock time. *[shown_working]*
- Group tools — Per-group WebSocket chat, shared photo album and equal-split expense tab. *[claimed]*
- Agentic ticket checkout — Agent finds tickets on official sites, fills details and books after approval or under a user limit. *[claimed]*
- Catalog ingestion — Ticketmaster, Google Places, OSM and Resident Advisor crawls fill MongoDB with deduplication; 9,000+ Atlanta activities embedded. *[shown_working]*
- Facebook import and rating loop — Likes become suggested ratings; post-outing ratings update the profile. *[claimed]*
- HEARSAY detector (separate entry) — Three-model speech ensemble gives calibrated synthetic probability with concept-tree explanations; reports EER 1.44% on official NSA test. *[claimed]*

**Flow:** Onboard with ratings, company, pace, spend → Set window and mood by typing or dictation → Receive three timed plans → Reorder or swap stops → Book tickets via agent → Share or post to Forum, join group chat and split costs → Rate stops to refine profile

**Prompt:** not public / not found
**Fit (implied):** MongoDB is the activity catalog with geospatial and TTL indexes behind retrieval for planning; page text does not tie it to the prize beyond listing it.  *(targeted: MLH: Best Use of MongoDB Atlas)*
**Sponsor tools:** MongoDB (Activity catalog with 2dsphere and TTL indexes, app data, core); Vultr (Production VPS, supporting); Meta Muse Spark (Researching and enriching activity data, supporting); Visa and Stripe (Listed in tags, not detailed, unclear)
**AI:** Qwen3-Embedding text embeddings plus trained 1.85M-parameter compatibility classifier on synthetic LLM-judged data, Jev LLM reranking, parity-gated embedding providers; Muse Spark and Gemini enrich catalog.
**Architecture:** SwiftUI app to Cloudflare, nginx, Go API with MongoDB and WebSocket hub, calling a FastAPI ML service; offline ingestion crawlers and GPU training jobs.
**Novelty:** Very large scope: iOS app, Go backend, trained ranking model, data pipeline and a second ML project on one page; self-correcting DAG planner.
**Scope:** large · working: Deployed API on a VPS with seeded demo world and real city data; about 145k LOC and 147 test files claimed; video. · polish: API contract docs, architecture diagram, model and dataset published on Hugging Face.
**Claims:** NDCG@10 0.897 vs 0.849 baseline | Three plans in 0.2 to 0.6 s | 9,000+ Atlanta activities embedded in about 3 GPU-minutes | HEARSAY EER 1.44% on official NSA test
**Gaps:** Devpost page covers both SideQuests and a HEARSAY submission; features follow SideQuests with HEARSAY listed once; Prize text not published
Sources: https://devpost.com/software/sidequestz, https://github.com/karthiksing05/HackGT-13-Proj (evidence README)

---

### SideQuests-HearsaySubmission
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence C · confidence low*
**Prizes:** NSA: Hearsay: The Audio Authentication Challenge - 1st Place [1st]

**What it is:** Placeholder Devpost page for an NSA Hearsay audio-authentication challenge entry (1st place). All description sections are empty; tags only say ai, ml and Python.
**Problem / user:** Not stated; the challenge concerns telling real voices from AI-synthetic ones.

**Prompt:** NSA Hearsay (1st) has no listing text; another team's README describes it as detecting real versus synthetic voice, scored by minDCF.
**Fit (none):** Content not described.  *(targeted: NSA: Hearsay: The Audio Authentication Challenge - 1st)*
**AI:** none
**Architecture:** Not described; tags indicate Python ML.
**Novelty:** Nothing recorded; winning entry has an empty writeup.
**Scope:** tiny · working: None on the page; no repo link. · polish: Empty sections.
**Gaps:** empty page; no repo; evidence file belongs to a different SideQuests project
Sources: https://devpost.com/software/sidequests-hearsaysubmission, https://hackgt13.devpost.com/

---

### Sky-C2
*HackGT HackGT 13 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 1st Place [1st]

**What it is:** Phone-in-Cardboard heads-up display that labels nearby aircraft at their true compass bearings using live ADS-B data, with no computer vision. Looking at a plane brings up an info card, and a 'Hey Grok' voice assistant answers questions about it. A supervisor can watch the wearer's view by WebRTC.
**Problem / user:** Airport tower controllers who juggle binoculars, radar, paper strips and lookup tables to identify aircraft; plane spotters are secondary.

**Features**
- Bearing-accurate labels — Icons placed using GPS, compass and great-circle math with pinhole projection. *[shown_working]*
- Aircraft card — Shows callsign, airline, type, route, altitude, climb rate, speed, distance for the centered aircraft. *[shown_working]*
- Color coding — Red blinking for squawk 7500/7600/7700, purple medical, green military, grey on ground. *[shown_working]*
- Heading-up radar mini-map — Rotates as the wearer turns. *[shown_working]*
- Hey Grok voice queries — Wake word then Grok answers using data on the focused aircraft; about 0.9 s per answer. *[shown_working]*
- Live stream and recording — WebRTC view to a laptop with one-click recording. *[shown_working]*
- Calibration and demo mode — In-headset lens, tilt and FOV calibration; indoor demo and API fallbacks. *[shown_working]*

**Flow:** Put phone in Cardboard headset → App reads GPS and compass → Aircraft appear at their bearings → Look at one to center it and see its card → Say Hey Grok and ask a question → Supervisor watches the stream

**Prompt:** Best Overall at HackGT 13 is a prize listing with no description; build anything.
**Fit (none):** No sponsor prompt; open-brief entry that uses xAI Grok.  *(targeted: Best Overall - 1st)*
**Sponsor tools:** xAI Grok (voice assistant answers and TTS, supporting)
**AI:** Grok (no reasoning mode) answers spoken questions grounded on live focused-aircraft data; browser wake-word and speech recognition; geometry rather than vision for placement.
**Architecture:** Vite/TypeScript web app (stereo camera, HUD canvas); FastAPI flight service polling adsb.lol each second; FastAPI voice service with Grok; ngrok to phone.
**Novelty:** $10 Cardboard plus sensor math and public ADS-B data as a cheap AR tower aid; explicit that it is not certified.
**Scope:** medium · working: 138-file repo with tests; Devpost gives measured timings and sensor-fix details; no video or live link. · polish: Calibration tool, rate-limit handling, fallbacks.
**Claims:** Flight data refreshes every 1 s | Grok answers in about 0.9 s | 15 degree in-focus cone
**Gaps:** repo README is a web subfolder note only; no video
Sources: https://devpost.com/software/sky-c2, https://github.com/jaiden-lee/ar-plane-identifier, https://hackgt13.devpost.com/

---

### Strider
*HackGT HackGT 13 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** The Shipyard - 2nd Place [2nd]

**What it is:** Wearable leg exoskeleton prototype. IMUs on the legs detect gait phase and an ESP32 drives two brushless motors through a 36:1 gearbox to add assist during walking, with an adjustable level that can go negative for resistance training.
**Problem / user:** Older adults who struggle with stairs and everyday movement as muscle mass declines.

**Features**
- Gait phase detection — MPU6050 IMUs compare angles and angular velocity to detect steps. *[shown_working]*
- Motor assist — ESP32 sends PWM to SPARK MAX controllers for two REV brushless motors; claims up to 40 lbs offloaded. *[shown_working]*
- Adjustable assist level — Setting can be negative to add resistance for progressive overload. *[shown_working]*

**Flow:** Wear the device → Walk; IMUs detect steps → Motors assist at the chosen level

**Prompt:** The Shipyard (2nd) has no public description on the listing (appears to be the hardware track).
**Fit (implied):** Hardware build; the track name suggests physical builds but no text confirms.  *(targeted: The Shipyard - 2nd)*
**AI:** none
**Architecture:** IMUs to ESP32 gait detection, PWM to motor controllers, brushless motors with 36:1 gearbox, 3S LiPo and BEC; waterjet and 3D-printed frame.
**Novelty:** Physical hardware exoskeleton with progressive-overload mode; built by non-CS students using PWM because CAN failed.
**Scope:** small · working: Creators say it works and reduces load; repo has only 3 files; video linked but not viewed. · polish: Rough prototype; tuning described as tedious.
**Claims:** Offloads up to 40 lbs in total | 36:1 gearbox, motors 150 RPM max
**Gaps:** repo has no README; video not watched
Sources: https://devpost.com/software/djdj-t21vgp, https://hackgt13.devpost.com/

---

### Synesthesia
*HackGT HackGT 13 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** The Shipyard - 1st Place [1st]

**What it is:** Wearable prototype that shows Deaf and hard-of-hearing users what sounds are around them and roughly where they come from. A Pico with three microphones estimates direction by loudness, an ESP32 sends it over BLE, and a phone web app classifies the sound with YAMNet and draws AR-style cues.
**Problem / user:** Deaf and hard-of-hearing people who miss alarms, knocks, or someone calling their name.

**Features**
- Direction cues — Pico estimates bearing from relative mic loudness; phone shows sirens left/right and knocks as a front pulse. *[shown_working]*
- On-device sound classification — YAMNet via TFLite/WASM labels alarms, sirens, horns, knocks, speech, dogs, doorbells. *[shown_working]*
- Timing-based fusion — Pairs a classified sound with a nearby direction event; shows no bearing if ambiguous. *[shown_working]*
- Personal name alerts — Saved names trigger visual notification and vibration via speech recognition. *[claimed]*
- Rear warning and calibration — Rear-facing warnings, ambient calibration, thresholds, clipping detection. *[shown_working]*

**Flow:** Wear sensor unit and open phone web app → Mics detect sound; direction sent over BLE → Phone classifies sound → Cue appears over live camera view → Saved name triggers an alert

**Prompt:** The Shipyard (1st) has no public description on the listing (appears to be the hardware track).
**Fit (explicit):** Hardware sensor plus phone prototype; Devpost states it was submitted to The Shipyard.  *(targeted: The Shipyard - 1st)*
**AI:** YAMNet on-device audio classification, MediaPipe, Web Speech API for names; no cloud audio upload.
**Architecture:** Raspberry Pi Pico (MicroPython) with 3 analog mics -> UART -> ESP32 BLE bridge -> Chrome Android web app with Web Audio, Web Bluetooth and canvas overlay.
**Novelty:** Combines cheap loudness-based direction hardware with on-device classification; clear about its limits versus true triangulation; privacy-first packets.
**Scope:** medium · working: Repo with tests and CI, demo video; no accuracy measurements. · polish: Honest prototype caveats in README; no quantified results.
**Claims:** Audio never leaves the phone; only direction packets are sent
**Gaps:** no measured accuracy
Sources: https://devpost.com/software/synesthesia-b1p9r3, https://github.com/RishabhK12/Synesthesia, https://hackgt13.devpost.com/

---

### TapChart
*HackGT HackGT 13 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Aramco: A Marina's Mission - 1st Place [1st]

**What it is:** A web app where Parkinson's patients run a short camera-based finger-tapping test to build a personal motor baseline and trend charts. An NFC tag links to the profile so licensed clinicians or EMTs can compare current movement with history during a possible stroke.
**Problem / user:** Clinicians seeing a Parkinson's patient with possible stroke symptoms lack a record of that person's usual motor function; targets patients, EMTs and doctors.

**Features**
- Camera finger-tapping test — MediaPipe hand tracking extracts tapping measurements from a short recording; only derived measurements are stored, not video. *[claimed]*
- Personal baseline and charts — Test results over time are turned into a baseline and trend charts for care teams. *[claimed]*
- NFC-linked patient profile — A tap on the patient's tag opens the clinical view of their baseline; limited to licensed healthcare providers. *[claimed]*
- Clinician portal — HCP login and verification, patient list, patient data access and log screens appear in the design images. *[claimed]*
- Medical band management — Patients add or edit their NFC band; screens shown in gallery. *[claimed]*

**Flow:** Patient signs in to the patient portal → Patient records a short finger-tapping test on camera → App shows results, analysis and test history → Clinician or EMT taps the patient's NFC tag → Verified provider opens the baseline and compares recent measurements

**Prompt:** not public / not found
**Fit (none):** Track description not found publicly; the project is a health-access tool framed around emergency stroke assessment for Parkinson's patients, so the link to the track is inferred only.  *(targeted: Aramco: A Marina's Mission - 1st Place)*
**AI:** MediaPipe vision tracking plus numpy/scipy/scikit-learn analysis of tapping signals; Claude is listed in built-with but its role is not described. No diagnosis is claimed.
**Architecture:** Web front end on Vercel, Python movement-analysis pipeline (MediaPipe, OpenCV), Supabase/Postgres storing measurements per patient ID, NFC tag pointing to a clinician view.
**Novelty:** Pairs a longitudinal personal motor baseline with NFC emergency access; explicitly stores derived metrics instead of video and states it does not diagnose stroke.
**Scope:** small · working: Live Vercel link listed; 14 screen images; repo could not be cloned for evidence. · polish: Designed screens for patient and clinician roles; privacy and disclaimer thinking in the writeup.
**Claims:** Stores no patient video; NFC access limited to licensed providers
**Gaps:** repo clone failed so README not read; Aramco track description not published; no video link seen
Sources: https://devpost.com/software/tapchart, https://hackgt13.devpost.com/

---

### TedTime
*HackGT HackGT 13 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Meta: Bringing People Closer Together with AI - Winner

**What it is:** TedTime is a React Native story-sharing app paired with a Bluetooth teddy bear. Relatives upload voice recordings; a backend transcribes them, adds timed sound effects chosen by an LLM and a cover image, and the bear moves its arms to the audio while it plays.
**Problem / user:** Families with relatives far away, especially children whose grandparents live abroad, who want a more personal way to keep loved ones' voices and stories than a call or plain audio.

**Features**
- Story recording, upload and sharing — Expo React Native app with Supabase auth and storage; stories shared with family and an Explore page of community stories. *[shown_working]*
- Automatic sound effects — Deepgram gives word timestamps; Muse Spark matches transcript to a 100+ Freesound catalog and returns effect times; backend mixes a processed MP3. *[claimed]*
- Story metadata and cover image — Second FastAPI endpoint returns description, hashtags and a Grok Imagine cover image. *[claimed]*
- Animated teddy bear — ESP32 receives audio over Bluetooth, runs an FFT for dominant frequency and drives quiet brushless-motor arms on a 3D-printed skeleton. *[claimed]*
- Read-along — Story playback screen shown in screenshots. *[unclear]*
- Haptic feedback — Bear described as giving haptics; not explained. *[planned]*

**Flow:** Record or upload a story in the app → Backend transcribes with word timestamps → LLM picks sound-effect timestamps from the catalog → Receive processed MP3 plus metadata and cover image → Save and share with family or browse Explore → Bear moves arms to the audio over Bluetooth

**Prompt:** not public / not found
**Fit (implied):** Uses Muse Spark to enrich family voice stories so distant relatives feel present, delivered through an app and a physical bear; page does not name the prize explicitly beyond the recognition note.  *(targeted: Meta: Bringing People Closer Together with AI - Winner)*
**Sponsor tools:** Meta Muse Spark (Choosing sound-effect timestamps from transcript and catalog, core); Grok Imagine (Story cover images, supporting)
**AI:** Deepgram transcription with word timestamps, then Muse Spark reads the transcript plus an effects catalog and outputs when each effect plays; Grok Imagine generates covers; bear uses FFT signal processing, not ML.
**Architecture:** Expo React Native app with Supabase; FastAPI backend with Deepgram, Muse Spark, Freesound catalog in a separate Supabase and mixing; ESP32 with motor driver receives audio over Bluetooth.
**Novelty:** Pairs an AI audio-enrichment pipeline with a custom animated plush toy using CAD-designed internals; hardware reacts to the audio frequency spectrum.
**Scope:** medium · working: Page describes app screens and backend endpoints; no video or live demo and no measured results. · polish: Screenshots of several app screens and a public CAD design; repo link points only to an organisation.
**Claims:** 100+ background sounds in catalog
**Gaps:** No evidence file or single repo, only a GitHub org link; No video; Prize text not published; Devpost title TedTime, queue name Tedtime
Sources: https://devpost.com/software/teddy-42km8n

---

### VIGIL: Assistive Eyewear with an Autonomous Aerial Scout
*HackGT HackGT 13 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall - 3rd Place [3rd]

**What it is:** Sunglasses with an ESP32-CAM, two time-of-flight sensors and two servo pads, paired with a laptop-controlled DJI Tello drone. The user asks by voice for an item or person, the drone finds it and returns, and the glasses guide the user there with speech and haptic pads.
**Problem / user:** Blind or low-vision people who lose objects in a room and must search by touch or wait for help.

**Features**
- Voice request — AirPods stem press starts push-to-talk; local Whisper transcribes and a constrained parser maps requests like find my water bottle to detectable classes. *[shown_working]*
- Drone object search — Tello hovers behind the wearer, drops to search height, scans, scores and hops until YOLO-World finds the target (bottle detected 95-100% at 1.3-4 m on team photos). *[shown_working]*
- Find a named person — Face ID against one photo per teammate lets the drone look for people by name. *[claimed]*
- Relative localization — Computes the object's position relative to where the wearer stood and faced, using monocular depth and pose. *[shown_working]*
- Guidance with speech and haptics — Spoken directions via TTS in AirPods plus two servo pads on the glasses indicate direction; ToF sensors on glasses. *[shown_working]*
- Fruit-fly connectome steering — Drone steering uses a 1,446-neuron subgraph from a fly connectome with a 34-parameter adapter trained by CMA-ES on Modal. *[shown_working]*

**Flow:** Wearer presses AirPod stem and asks for an item or person → Whisper transcribes; request parsed to a target class → Tello drops down, explores and finds the target → Drone returns to wearer and reports the relative position → Glasses give spoken directions and servo pad cues until arrival

**Prompt:** Best Overall: general top-three prize for the best project of the event; no further text published.
**Fit (implied):** Open overall prize; project is a full hardware-software accessibility stack (glasses, drone, voice, simulation-trained controller) with README stating 3rd overall of 268.  *(targeted: Best Overall - 3rd Place)*
**Sponsor tools:** Modal (Cloud training of the fly-connectome adapter with CMA-ES, supporting)
**AI:** Local Whisper STT, YOLO-World open-vocabulary and YOLO11 detection, face ID, Depth-Anything monocular depth, and a fly-connectome spiking-network controller tuned by CMA-ES; LLM query parser optional.
**Architecture:** Laptop runs perception, search planner and voice app; Tello over Wi-Fi; glasses Arduino Nano ESP32 on a second Wi-Fi with camera, ToF sensors and servos; UDP links between flight and voice apps.
**Novelty:** Uses a real fly-brain connectome circuit for drone pursuit steering and combines a drone scout with wearable haptics; unusually large codebase with about 200 tests and simulation.
**Scope:** large · working: Two real-world drone-following test images and README detailing hardware setup, calibration and measured detection rates. · polish: CAD renders, product photos, 376 files, setup and safety procedures, voice self-test tool.
**Claims:** 6.6 degree steering error vs 11.0 with randomly wired neurons | Bottle found 95-100% of views at 1.3-4 m, no false detections | 500+ automated tests | 3rd overall of 268 (README)
**Gaps:** demo video not viewable; track text not published
Sources: https://devpost.com/software/vigil-assistive-eeywear-with-an-autonomous-aerial-scout, evidence file README (parthm667/vigil), https://hackgt13.devpost.com/

---

