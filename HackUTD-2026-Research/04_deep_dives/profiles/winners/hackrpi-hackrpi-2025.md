# HackRPI — HackRPI - 2025 (1 projects)

### Brain Invaders
*HackRPI HackRPI - 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best First-Time Hack

**What it is:** A Space Invaders-style browser game built to exercise impulse control and response inhibition, with timing windows, stacking power-ups and debuffs, adaptive difficulty and an end-of-round analytics dashboard.
**Problem / user:** People with ADHD, ASD or other regulation difficulties who struggle with impulse control and timing-based decisions.

**Features**
- Impulse-control gameplay — Space Invaders loop with timing windows that reward waiting and penalize premature actions *[claimed]*
- Behavior tracking — Records reaction times, premature actions, missed windows, accuracy and score, stored via Express/MongoDB backend *[claimed]*
- Adaptive difficulty — Difficulty adjusts to player behavior *[claimed]*
- Power-ups and debuffs — Stackable modifiers that change play *[claimed]*
- Round summary dashboard — Charts and insights on reaction times, accuracy, impulse counts and difficulty progression *[claimed]*
- Accessible UI — Readable text with background contrast, neurodivergent-friendly design *[claimed]*
- Profiles and long-term progress — Per-user tracking over time *[planned]*

**Flow:** Start a timed Space Invaders-style round → Respond within timing windows while using power-ups/debuffs → Round ends → View summary charts and insights

**Prompt:** Best First-Time Hack: for teams in which more than half are hacking for the first time; judged on practicality, creativity, technical difficulty and effort.
**Fit (none):** Page does not mention first-time status; the project is a self-contained game with analytics and an accessibility purpose.  *(targeted: Best First-Time Hack)*
**AI:** none
**Architecture:** Phaser.js game inside a React frontend, Node/Express backend logging player behavior to MongoDB, dashboard computed from stored round data.
**Novelty:** Applies a classic arcade format to a clinical-style response-inhibition training idea with analytics; no AI.
**Scope:** small · working: Repo of about 2.3k lines with frontend and backend; demo video embedded on Devpost, not viewed. · polish: Retro styling and dashboard claimed; README is a single descriptive paragraph.
**Claims:** Adaptive difficulty working | Clean analytics dashboard | No clinical validation reported
**Gaps:** README has no real content; video not viewable; feature working status unverified
Sources: https://devpost.com/software/space-invaders-impulse-control-trainer, evidence/hackrpi-hackrpi-2025-brain-invaders.json (one-paragraph README), https://hackrpi-2025.devpost.com/

---

