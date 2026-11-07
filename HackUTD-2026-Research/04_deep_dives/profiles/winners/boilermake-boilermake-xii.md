# BoilerMake — BoilerMake XII (3 projects)

### Fluention
*BoilerMake BoilerMake XII · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 3rd Place Prize: JBL Speaker [3rd]

**What it is:** Speech-therapy web platform with two modules: an assistant that trains lip and tongue positions (MediaPipe Face Mesh and color-based tongue tracking), image description, vocabulary game and voice conversation; and a translator that turns impaired speech into clear synthesized speech via Whisper, GPT-4 and Google TTS.
**Problem / user:** People with speech or language impairments (autism, dysarthria, aphasia, apraxia) for whom traditional therapy is costly and hard to reach.

**Features**
- Lip shape training — Face Mesh lip height-to-width ratio detects 'oooo' and 'eeeee' shapes held 2 s, three reps *[claimed]*
- Tongue position training — HSV filtering and contour detection classify left, right and down positions *[claimed]*
- Image description feedback — Speech-to-text then grammar, pronunciation and sentence structure analysis *[claimed]*
- Vocabulary game — AI synonym and alternative-word suggestions in gamified mode *[claimed]*
- Voice conversation partner — Voice API assistant gives real-time pronunciation and fluency corrections *[claimed]*
- Language-disorder translator — Whisper transcript, GPT-4 normalization, Google Cloud TTS audio output *[shown_working]*
- ML-based lip and tongue analysis — Stated next step replacing ratio heuristics *[planned]*

**Flow:** Open the web app → Choose speech-pathology exercises or translator → For translator: press Start Recording and speak → Backend transcribes, normalizes and synthesizes speech → Hear the cleaned output

**Prompt:** BoilerMake XII (open-ended): 1st iPad, 2nd Sony WH-1000XM4, 3rd JBL Charge 5 per teammate; College of Engineering Most Consequential Project; Cartesia Best Use of Sonic ($1,000 plus API credits); Caterpillar Best Cloud Implementation. Judged on execution, challenge and creativity.
**Fit (none):** Open-ended event; project is an accessibility health tool judged on execution, challenge and creativity; no sponsor track targeted.  *(targeted: 3rd Place Prize)*
**AI:** Whisper STT, GPT-4 text normalization, Google TTS; MediaPipe landmarks and OpenCV color/contour heuristics for mouth analysis; Groq and TensorFlow listed.
**Architecture:** Next.js frontend and FastAPI backend; browser records audio and video; backend calls speech and LLM services and returns audio and feedback.
**Novelty:** Pairs computer-vision oral-motor exercises with a speech-normalization translator in one therapy aid.
**Scope:** medium · working: YouTube demo and nine screenshots; repo large (about 193k estimated lines, likely includes dependencies) with tests. · polish: Structured README with sections; no accuracy or user-testing data.
**Claims:** Built in under 36 hours | About five APIs integrated
**Gaps:** Video not watched; LOC estimate inflated by bundled files
Sources: https://devpost.com/software/fluention, https://github.com/jihwimin/fluention (evidence file README), https://boilermake-xii.devpost.com/

---

### MockMade
*BoilerMake BoilerMake XII · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** 2nd Place Prize: Sony Headphone [2nd]; Cartesia: Best Use of Sonic; Caterpillar: Best Cloud Implementation

**What it is:** AI mock-interview site: pick a company and behavioral or technical mode. Behavioral mode phones the user via Retell AI and grades the call across categories; technical mode is a LeetCode-style editor with a voice AI interviewer giving hints. Lip-synced video replay is generated with Sync.
**Problem / user:** Job seekers, especially CS students, facing a tough internship market who want realistic interview practice.

**Features**
- Behavioral phone-screen interview — Retell AI calls the user's number and asks job-related questions *[claimed]*
- Graded post-interview report — Multiple OpenAI prompts grade transcript and audio by category *[claimed]*
- Video simulation of the interview — Sync lip-sync over videos hosted on Cloudinary *[claimed]*
- Technical coding interview — LeetCode-like platform; Whisper transcribes speech, GPT-4o reads code and transcript, Cartesia Sonic speaks *[claimed]*
- Company selection and question bank — MongoDB stores LeetCode-style questions *[claimed]*
- Login and sign-up — Auth0 *[claimed]*

**Flow:** Sign in with Auth0 → Choose company and interview type → Behavioral: answer the phone call; Technical: code and ask the AI for hints → Receive graded analysis → Watch video simulation

**Prompt:** Cartesia Best Use of Sonic: $1,000 cash plus $1,000 API credits; Caterpillar Best Cloud Implementation: gear prize pack. BoilerMake XII (open-ended): 1st iPad, 2nd Sony WH-1000XM4, 3rd JBL Charge 5 per teammate; College of Engineering Most Consequential Project; Cartesia Best Use of Sonic ($1,000 plus API credits); Caterpillar Best Cloud Implementation. Judged on execution, challenge and creativity.
**Fit (explicit):** Uses Cartesia Sonic TTS in the technical interviewer voice; deploys on Render and Vercel for the cloud prize. Devpost lists the awards as won.  *(targeted: 2nd Place, Cartesia: Best Use of Sonic, Caterpillar: Best Cloud Implementation)*
**Sponsor tools:** Cartesia Sonic (Text-to-speech for the technical interviewer, core); Retell AI (Real-time voice phone interview, core); Sync (Lip-sync video simulation, supporting)
**AI:** Retell voice agent for calls; OpenAI multi-prompt grading and GPT-4o for technical hints; Whisper STT; Cartesia TTS; Sync lip sync.
**Architecture:** Next.js/React frontend on Vercel; backend on Render with MongoDB, Auth0, Retell webhooks, OpenAI grading, Cloudinary and Sync for video.
**Novelty:** Real outbound phone interview plus lip-synced video replay, in addition to a coding interview with voice.
**Scope:** medium · working: Demo site and YouTube video listed; three repos (backend, demo, frontend); backend repo unreadable. · polish: Separate demo domain and hosted stack; no metrics.
**Claims:** Post-interview grading across categories | Technical hints until all test cases pass
**Gaps:** Repo clone failed and GitHub not fetchable; README unread; Video not watched
Sources: https://devpost.com/software/mockmate, https://boilermake-xii.devpost.com/

---

### REMI
*BoilerMake BoilerMake XII · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 1st Place Prize: iPad [1st]; College of Engineering: Most Consequential Project

**What it is:** Peer-to-peer campus bike rental: a 3D-printed smart lock with an Arduino Nano, NFC reader and servo, unlocked over BLE/NFC keys from a Flutter app. Owners list bikes, renters find nearby ones on Google Maps, with Firebase auth and database.
**Problem / user:** Purdue students who find rideshare and scooters expensive, and bike owners with idle bikes who could earn money lending.

**Features**
- Smart lock with encrypted NFC keys — Arduino Nano plus NFC reader and servo, BLE central/peripheral link, I2C *[claimed]*
- Owner bike listings — Mobile app lets owners list bikes for lending *[claimed]*
- Renter map discovery — Google Maps and geolocation show nearby bikes *[claimed]*
- Unlock via NFC from the app — App communicates with lock over BLE/NFC *[claimed]*
- Accounts and live data — Firebase auth and database for users and transactions *[claimed]*
- Return-responsibility enforcement — Stated without a described mechanism *[unclear]*

**Flow:** Owner lists a bike → Renter opens app and finds a bike on the map → Renter unlocks it by NFC → Rides and returns it → Owner earns money

**Prompt:** BoilerMake XII (open-ended): 1st iPad, 2nd Sony WH-1000XM4, 3rd JBL Charge 5 per teammate; College of Engineering Most Consequential Project; Cartesia Best Use of Sonic ($1,000 plus API credits); Caterpillar Best Cloud Implementation. Judged on execution, challenge and creativity. College of Engineering Most Consequential Project awards certificates and swag.
**Fit (implied):** Campus-mobility product solving a local cost problem with working hardware; Devpost lists both awards as won.  *(targeted: 1st Place Prize: iPad, College of Engineering: Most Consequential Project)*
**AI:** none
**Architecture:** Flutter/Dart app (Google Maps, geolocator) with Firebase; BLE/NFC link to Arduino Nano lock with servo; 3D-printed housing.
**Novelty:** Pairs custom lock hardware with a two-sided rental marketplace built by a team new to hardware.
**Scope:** medium · working: Page says working prototype integrating NFC and app; video linked; repo about 5.7k lines mostly Flutter scaffolding. · polish: Canva deck, diagrams and 3D-printed lock images; README copies Devpost text; no security details.
**Claims:** Working prototype far surpassed initial expectations
**Gaps:** Video not watched; Encryption scheme undescribed
Sources: https://devpost.com/software/remi-hbkrzs, https://github.com/mihir-chauhan/REMI (evidence file README), https://boilermake-xii.devpost.com/

---

