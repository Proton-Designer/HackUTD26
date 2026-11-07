# HackPrinceton — Spring 2025 (1 projects)

### SixthSense
*HackPrinceton Spring 2025 · dataset: sponsor · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall Hack (Meta Quest + NordVPN products 1yr + 1GB data per member)

**What it is:** SixthSense is an assistive wearable for blind users: Meta glasses see the scene, YOLOv8 names objects, and a glove buzzes a distinct vibration pattern per object while a servo gauntlet pushes the hand toward its location.
**Problem / user:** Visually impaired people who want environmental awareness without overloading hearing.

**Features**
- Object detection from glasses camera — YOLOv8 labels objects with bounding boxes from Meta glasses footage. *[shown_working]*
- Embedding-to-vibration tactile signatures — Object-name embeddings become vibration waveforms via inverse Fourier transform, so similar objects feel similar. *[shown_working]*
- Directional guidance gauntlet — Servo motors steer the hand toward object coordinates. *[shown_working]*
- Multi-object harmonic blending — Several signatures are layered and normalized to avoid overload. *[claimed]*
- Separate what and where controllers — Two Arduinos handle identity and direction. *[shown_working]*

**Flow:** Wear glasses, glove and gauntlet → Glasses capture the scene → Objects are detected and embedded → Glove vibrates each signature → Gauntlet guides hand to object

**Prompt:** HackPrinceton Spring 2025 top overall prize (Meta Quest plus a year of Nord products and 1GB data per member); no challenge brief.
**Fit (none):** General overall award; the project is a hardware and AI accessibility prototype.  *(targeted: Best Overall Hack)*
**AI:** YOLOv8 detection plus a semantic embedding of class names, mapped to vibration patterns by inverse Fourier transform.
**Architecture:** Meta glasses feed a processing unit running detection and embeddings; Arduino controllers drive glove vibration and gauntlet servos; Next.js dashboard.
**Novelty:** Haptic language derived from embeddings so semantic similarity maps to tactile similarity, with split what/where channels and no audio.
**Scope:** medium · working: Page and README describe a built prototype and a first user test; repo has tests. · polish: Landing/dashboard, architecture screenshots, Canva deck; no video.
**Claims:** 71.68% correlation between similar objects vs 10.23% for different ones | First test user identified objects by vibration alone | Latency cut from seconds to milliseconds
**Gaps:** Measurement method unstated
Sources: https://devpost.com/software/sixthsense-xuw41r, https://github.com/k-kochhar/SixthSense

---

