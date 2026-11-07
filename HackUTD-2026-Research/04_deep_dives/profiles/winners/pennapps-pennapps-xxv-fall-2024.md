# PennApps — PennApps XXV (Fall 2024) (3 projects)

### Rally AI
*PennApps PennApps XXV (Fall 2024) · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall 2nd [2nd]; Best Design; The Wolfram Award

**What it is:** A web app that lets a politician's campaign generate a personalized video ad for a voter's town: it researches local issues and the candidate's policies, writes a speech, clones the voice, lip-syncs existing footage and overlays B-roll.
**Problem / user:** Campaign and ad teams wanting voters to see how a candidate's policies affect their locality; team cites interviews with 70+ campaigns and 40+ ad teams.

**Features**
- Local issue and policy research — Firecrawl and Perplexity gather local news, economic data and the candidate's positions; insights stored in Supabase. *[shown_working]*
- Policy-to-voter matching — LLM chain correlates the candidate's policies with issues in the voter's area. *[claimed]*
- Speech writing — GPT writes an ad script in the politician's style, refined by validator agents. *[shown_working]*
- Voice cloning — Cartesia Sonic synthesizes narration from short clips of the politician's voice. *[shown_working]*
- Lip-synced video — SyncLabs re-times existing candidate footage to the generated audio. *[shown_working]*
- B-roll planning and overlay — LLM picks timestamps and topics, Pexels footage fetched, FFmpeg overlays it. *[shown_working]*
- State compliance checks — LLM chain grounded in NCSL and OpenFEC sources plus validators to avoid negativity and misinformation; includes a bills database. *[claimed]*

**Flow:** Choose candidate policies and a voter location → System scrapes local data and matches issues → Script generated and checked → Voice, lip-sync and B-roll assembled → Download finished ad in minutes

**Prompt:** PennApps XXV pages give no description for Best Overall or Best Design; the Wolfram Award goes to the top three teams overall, each receiving a year of Wolfram|One Professional.
**Fit (none):** Polished multi-agent product with end-to-end demo; Wolfram award is placement-based, so no separate targeting.  *(targeted: Best Overall 2nd, Best Design, The Wolfram Award)*
**AI:** Chain of GPT-4o-mini agents for parsing, scripting and B-roll planning, with validator agents; Perplexity research, Cartesia voice cloning, SyncLabs lip-sync models.
**Architecture:** Next.js app on Vercel orchestrates an 8-layer agent pipeline: data aggregation, voter profile, policy matching, script, assets, video, post-processing, deployment, with Supabase storage and FFmpeg.
**Novelty:** End-to-end composition of research, cloned voice, lip-sync and compliance-aware validation into one personalized political-ad generator; subject is politically sensitive.
**Scope:** medium · working: Repo 101 files, about 6.5k LOC, live Vercel demo and YouTube video linked. · polish: Compliance and detailed README sections; Best Design prize; no tests.
**Claims:** Ad produced in under 4 minutes | 70+ campaigns and 40+ ad teams interviewed | Legal for candidates to create AI personas of themselves
**Gaps:** video not viewed; no quality metrics; compliance accuracy unmeasured
Sources: https://devpost.com/software/rally-8sxi2t, https://github.com/pr28416/rally, https://pennapps-xxv.devpost.com/

---

### SoundSheild
*PennApps PennApps XXV (Fall 2024) · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Best Overall 1st [1st]; The Wolfram Award

**What it is:** A wearable headphone-plus-camera prototype built on a Raspberry Pi Zero that monitors ambient noise, filters and masks overwhelming sound with calming audio, and warns the wearer when a person is detected behind them during loud conditions.
**Problem / user:** People with sound hypersensitivity (cited as 50-70 percent of autistic people, also others) who need relief from noise without losing awareness of surroundings.

**Features**
- Continuous ambient sound monitoring — Python audio pipeline measures noise amplitude and frequency content in real time. *[claimed]*
- Real-time noise reduction — Spectral subtraction and dynamic range compression filter loud sound while quiet sounds such as speech pass through. *[claimed]*
- Calming audio on overload — Soothing music plays only when noise rises above a threshold, adjusting to changing levels. *[claimed]*
- Person-behind alert — Camera with OpenCV detects someone behind the wearer; alert fires when sound amplitude is high. *[claimed]*
- Heart-rate stress trigger — A heart rate sensor would raise filtering automatically when stress is detected. *[planned]*

**Flow:** Wear headphone with camera and Pi Zero → Device monitors ambient sound → Quiet sound and speech pass through → Overwhelming noise triggers filtering and calming music → Camera sees person behind while loud: user is alerted

**Prompt:** PennApps XXV pages give no description for Best Overall; the Wolfram Award goes to the top three teams overall, each receiving a year of Wolfram|One Professional.
**Fit (none):** Accessibility-focused hardware prototype; neither prize is explicitly targeted, Wolfram award tied to placement.  *(targeted: Best Overall 1st, The Wolfram Award)*
**AI:** No named ML model; classical DSP (librosa, SciPy spectral subtraction, compression) and OpenCV computer vision for person detection.
**Architecture:** Raspberry Pi Zero runs Python audio processing and camera person detection, driving headphone output with filtered sound, calming music and alerts.
**Novelty:** Pairs selective noise suppression with a rear-facing camera for situational awareness, aimed at sensory sensitivity on very low-power hardware.
**Scope:** small · working: Devpost describes a functional prototype with eight screenshots; repo could not be cloned or fetched, no video. · polish: No metrics, demo video or live link found.
**Claims:** Functional prototype integrating CV, audio and hardware | Speech and low-level sounds are left unfiltered
**Gaps:** repo clone and fetch failed; no video; no performance or user-test data
Sources: https://devpost.com/software/soundsheild, https://pennapps-xxv.devpost.com/

---

### SurgeVue
*PennApps PennApps XXV (Fall 2024) · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Best Overall 3rd [3rd]; Best AR/VR Hack

**What it is:** A neurosurgery assistant prototype combining an iOS AR app that overlays tumor outlines, a PyTorch classifier for tumors and foreign objects, an Arduino gyroscope and sweat sensor for hand tracking, and face plus RFID access control for patient data.
**Problem / user:** Neurosurgeons and medical students needing precision and safety in brain surgery; page asserts high mortality risk without a source.

**Features**
- AR tumor overlay — Swift/SceneKit iOS app draws tumor outlines and patient data over the surgical field. *[claimed]*
- Tumor classification and foreign object detection — PyTorch models plus OpenCV image processing served via Flask; repo includes a brain tumor image dataset folder. *[claimed]*
- Instrument and hand tracking — Arduino gyroscope streams motion data; app shows hand movement trends. *[claimed]*
- Sweat sensor monitoring — Arduino sensor data shown in mobile app alongside movement trends. *[claimed]*
- Authorized access to patient records — Facial recognition and RFID gate data, with PropelAuth for authentication. *[claimed]*
- 3D brain model — Interactive 3D model listed as future work; repo has a modeling_3d folder. *[planned]*

**Flow:** Surgeon authenticates by face and RFID → AR view shows tumor outline and classification → Gyroscope and sweat data stream to the app → Surgeon reviews hand movement trends

**Prompt:** PennApps XXV pages give no description for Best Overall or Best AR/VR Hack; only prize lines (Best AR/VR: mini projector per winner).
**Fit (implied):** AR surgical overlay on iOS fits the AR/VR category; no explicit statement of prize targeting.  *(targeted: Best Overall 3rd, Best AR/VR Hack)*
**Sponsor tools:** PropelAuth (authentication and access control for patient data, supporting)
**AI:** PyTorch classifier for brain tumors and foreign objects with OpenCV preprocessing and Flask API; dataset source and accuracy not stated.
**Architecture:** iOS Swift/SceneKit AR client calls Flask backend with ML models; Arduino sensors (gyroscope, sweat, RFID) feed data to the app; Google Cloud used for training.
**Novelty:** Bundles AR imagery, ML, wearable sensing and biometric access in one surgical concept; hardware integration is the unusual part.
**Scope:** small · working: Repo 529 files but about 500 are image data; about 1.5k LOC; demo video links exist, not viewed. · polish: Emoji-styled README; no tests; no metrics and no clinical validation.
**Claims:** Real-time AR overlays | Model accurately classifies tumors and detects foreign objects | Non-elective neurosurgery mortality rises 15-fold
**Gaps:** video not viewed; no accuracy numbers; unclear which parts run end-to-end
Sources: https://devpost.com/software/surgikalai, https://github.com/jeet-dekivadia/SurgeVue, https://pennapps-xxv.devpost.com/

---

