# HackNYU — 2025 (2 projects)

### Dristhi
*HackNYU 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Track: Security and Privacy (sponsored by Nord Security)

**What it is:** Hardware prototype smart bag for visually impaired users that combines a webcam, ultrasonic sensors, posture and temperature sensing, and an emergency button, feeding a web app that gives spoken guidance.
**Problem / user:** Visually impaired people (page cites ~245 million) needing safer navigation, obstacle avoidance and a way to call for help.

**Features**
- Emergency alert — One button tap sends an alert to a designated contact. *[claimed]*
- Obstacle detection — Webcam plus HC-SR04 ultrasonic sensors detect obstacles; ultrasonic readings validate camera distance. *[claimed]*
- Object and people detection and tracking — OpenCV and MediaPipe detect faces/objects with tracking. *[claimed]*
- Posture and temperature sensing — Bag measures posture and environmental/body temperature. *[claimed]*
- Spoken guidance web app — Web app delivers real-time audio guidance (pyttsx3 listed). *[claimed]*

**Flow:** User carries the bag → Sensors and webcam capture surroundings → Web app converts detections to spoken guidance → User taps button to alert contact in emergencies

**Prompt:** HackNYU Security and Privacy track (Nord Security): build a tool that strengthens user security or privacy and protects sensitive data or the wider digital ecosystem; judged on creativity, usability and real-world impact.
**Fit (implied):** Frames the bag as personal safety for visually impaired users, with unspecified 'security features'; the link to digital privacy is weak and not stated on the page.  *(targeted: Track: Security and Privacy (Nord Security))*
**AI:** Classical computer vision (OpenCV, MediaPipe) for detection and tracking; no trained models named; AI scene description is future work.
**Architecture:** Sensors and webcam on a bag feed Python/C++ code (OpenCV, MediaPipe, threading) that serves a web app producing text-to-speech audio.
**Novelty:** Physical sensor-integrated wearable rather than a pure software submission; combines distance cross-validation from camera and ultrasonic.
**Scope:** small · working: Page claims a working integrated prototype but lists no repo, video or demo; ultrasonic sensor reportedly unreliable. · polish: Only Devpost text and screenshots; no further assets found.
**Claims:** Integrates diverse sensors into one system that works in real-world conditions
**Gaps:** No repo; No video or demo; Screenshot count unknown
Sources: https://devpost.com/software/dristhi, sponsor_prompts_Nord_Saily_Incogni.jsonl

---

### FirstWave
*HackNYU 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Track: Security and Privacy (sponsored by Nord Security)

**What it is:** Spear-phishing simulation platform where GPT-4o agents build fake LinkedIn personas from public data, engage target employees, and report vulnerabilities in a dashboard so organizations can train staff.
**Problem / user:** Organizations whose security training does not mimic modern social-engineering tactics.

**Features**
- Campaign setup — Define target profiles and the types of sensitive information to test. *[claimed]*
- AI persona generation — Agents create fake LinkedIn profiles from public data. *[claimed]*
- AI engagement — Agents converse with targets to mimic phishing, using Puppeteer for browser automation. *[claimed]*
- Live feed and dashboard — Real-time view of campaign activity and metrics. *[shown_working]*
- Post-campaign analysis report — Report on target engagement, vulnerabilities and recommended actions. *[shown_working]*

**Flow:** Create a campaign with target profile → Agents build persona and engage → Watch live feed and dashboard → Read analysis report → Plan follow-up training

**Prompt:** HackNYU Security and Privacy track (Nord Security): build a tool strengthening user security or privacy, judged on creativity, usability and real-world impact against cybersecurity problems.
**Fit (implied):** Offensive-security training tool that tests employees' resistance to social engineering; the page says it won the track but does not draw the link.  *(targeted: Track: Security and Privacy (Nord Security))*
**AI:** GPT-4o generates personas and conversation flows; Puppeteer drives LinkedIn interaction; analysis report summarizes target behavior.
**Architecture:** Next.js/React app with Node backend and MongoDB; AI agents (GPT-4o) plus Puppeteer automation; dashboard and live feed show campaign state.
**Novelty:** Uses agents to run full social-engineering campaigns including persona creation, rather than templated phishing emails; raises ethics and consent issues the team mentions.
**Scope:** small · working: Five screenshots (dashboard, live feed, LinkedIn, report) and ~6k LOC repo with tests; no video or live demo; README is a placeholder. · polish: Landing page and dashboard UI shown; no documentation.
**Claims:** Creates hyper-realistic social engineering interactions
**Gaps:** README placeholder only; No video; Real-world operation unverified
Sources: https://devpost.com/software/firstwave-5wbld1, evidence/sponsor-hacknyu-2025-firstwave.json, sponsor_prompts_Nord_Saily_Incogni.jsonl

---

