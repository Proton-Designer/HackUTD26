# HackDartmouth — HackDartmouth - X (2 projects)

### FormFix
*HackDartmouth HackDartmouth - X · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Third Place - Airpods [3rd]

**What it is:** Exercise form coach: user uploads a video or uses a webcam, MediaPipe finds body keypoints, the app isolates one repetition, compares joint angles and timing against reference angles from a professional, and Gemini writes improvement advice shown as text or spoken aloud.
**Problem / user:** People who exercise without a trainer cannot tell if their form is wrong; the tool gives automatic corrective feedback.

**Features**
- Video upload or live webcam — Flask web app accepts a file or live camera stream for analysis. *[shown_working]*
- Rep isolation — Custom algorithm segments footage into a single repetition before analysis. *[shown_working]*
- Angle comparison to reference — Joint angles between key points are compared with golden angles taken from a professional video; angles chosen over displacement to reduce body-size and camera effects. *[shown_working]*
- Gemini feedback summary — Angle and rep-timing data go to Gemini, which writes what to improve. *[shown_working]*
- Transcript and speech — Upload mode shows on-screen text; live mode reads feedback aloud with pyttsx3. *[shown_working]*

**Flow:** Upload a clip or start webcam → App segments one rep → Angles and timing compared to reference → Gemini generates summary → Read transcript or hear it spoken

**Prompt:** HackDartmouth X Third Place overall prize (AirPods gen 4 for the team); the prize page gives no theme or description.
**Fit (none):** No stated prize targeting; general overall placement. Devpost lists Healthcare and Education tracks without explaining them.  *(targeted: Third Place overall)*
**Sponsor tools:** Gemini API (turn angle and timing data into coaching text, core); Novita AI (listed in built-with tags; role not stated, unclear)
**AI:** MediaPipe pose landmarks drive rule-based angle comparison to reference; Gemini only phrases the coaching summary.
**Architecture:** Flask backend with OpenCV, MediaPipe and rerun-sdk, HTML/JS templates, Gemini call, pyttsx3 for speech.
**Novelty:** Uses joint-angle comparison against a single professional reference and rep segmentation instead of a trained exercise classifier.
**Scope:** small · working: Devpost links a demo video; no live site; README absent. · polish: About 1.5k LOC in 25 files, no tests or README; covers few exercises per the team.
**Claims:** Rep-isolation algorithm has good performance (no metrics)
**Gaps:** repo has no README; no accuracy data
Sources: https://devpost.com/software/formfix, evidence/hackdartmouth-hackdartmouth-x-formfix.json (no README, manifest only), https://hackdartmouth-x.devpost.com/

---

### Neurolytics
*HackDartmouth HackDartmouth - X · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Second Place - Beats [2nd]

**What it is:** Medical imaging assistant: Devpost describes DICOM CT/MRI loading, 3D volume rendering and Gemini-based analytics over scans stored in S3, while the repo README presents a simpler web app where a user uploads an MRI slice, gets a Gemini Vision summary and chats about the scan.
**Problem / user:** Radiologists face complex 3D scans and neuroradiologists are scarce; the tool targets clinicians and trainees who want quick AI-assisted reading.

**Features**
- MRI upload and AI analysis — Next.js page posts a T1/T2 image to a Flask endpoint where Gemini Vision returns JSON findings (tumor type, abnormalities). *[claimed]*
- Context-grounded chat — Follow-up questions use the stored JSON analysis keyed by timestamp. *[claimed]*
- History tab — Each run saved to AWS S3 with thumbnail and summary. *[claimed]*
- DICOM to 3D volume — Sorts slices by InstanceNumber and builds volumes; MIP and translucent rendering via Napari. *[claimed]*
- MRI library and analytics views — Screens render S3 contents with analytics and 3D tumor GIFs on Devpost. *[shown_working]*
- Tumor location hint on CT — Gemini identifies a possible tumor location. *[claimed]*

**Flow:** Upload a scan → Receive AI summary → Ask follow-up questions in chat → Browse past scans in library or history → Open 3D rendering

**Prompt:** HackDartmouth X Second Place overall prize (Beats Solo 4); no theme or description given on the prize page.
**Fit (none):** No stated prize targeting; general placement. Healthcare imaging build with Gemini, which is also an MLH track.  *(targeted: Second Place overall)*
**Sponsor tools:** Gemini API (MLH track) (vision analysis and chat, core)
**AI:** Gemini Vision produces structured JSON analysis of the image; later chat answers are grounded by feeding that JSON back as context.
**Architecture:** Next.js 14 front end, Flask API calling Gemini and boto3, AWS S3 for images and JSON, plus Napari-based DICOM 3D rendering per Devpost.
**Novelty:** Pairs LLM scan summaries with 3D DICOM volume rendering; README and Devpost differ in scope, suggesting layered work.
**Scope:** medium · working: Video and three GIF captions on Devpost; README documents endpoints; no live demo. · polish: Repo is huge (7.8k files, 67k LOC, likely vendored libraries); landing and chat screenshots; no tests.
**Claims:** More than 50 million people need MRI interpretation yearly (README) | Expert-level insights in seconds (README)
**Gaps:** Devpost and README scopes do not match (MRI vs CT/DICOM 3D); no accuracy validation
Sources: https://devpost.com/software/neurolytics, evidence/hackdartmouth-hackdartmouth-x-neurolytics.json (README), https://hackdartmouth-x.devpost.com/

---

