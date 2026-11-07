# HackNYU — HackNYU - 2025 (1 projects)

### SkinGuard - AI Dermatologist
*HackNYU HackNYU - 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best First Time Hack

**What it is:** A MERN web app where users upload skin photos for a predicted condition from an EfficientNetB3 model, chat with an OpenAI-backed assistant about the result, and track skin changes over time.
**Problem / user:** People who cannot easily afford or reach a dermatologist and want an instant preliminary skin assessment.

**Features**
- Skin image analysis — Uploaded photo goes to a Python/Flask-served EfficientNetB3 model that predicts possible conditions *[claimed]*
- AI chatbot — OpenAI API explains results, suggests solutions and answers questions *[claimed]*
- Skin tracker — Users log conditions and compare changes; README adds stored health records and images *[claimed]*
- Accounts — Backend uses JWT and Nodemailer per README *[claimed]*
- Skincare routine recommender — Suggestions based on user history *[planned]*
- Mobile app and dermatologist validation — Planned partnerships to verify diagnoses *[planned]*

**Flow:** Sign in → Upload a skin photo → Receive predicted condition → Ask the chatbot for explanation or advice → Log the entry in the tracker

**Prompt:** Best First Time Hack: one team, up to $25 per participant; the whole team of three or more must be beginners and college students are not eligible.
**Fit (explicit):** Devpost says it was the team's first hackathon and claims a functional MVP; README also labels it the prize winner.  *(targeted: Best First Time Hack)*
**Sponsor tools:** OpenAI API (Chatbot that explains diagnoses, supporting)
**AI:** EfficientNetB3 image classifier (TensorFlow/Keras) trained by a teammate predicts skin condition; OpenAI model powers the explanation chatbot. Training dataset not named.
**Architecture:** React client, Node/Express server with MongoDB, JWT auth, Flask microservice hosting the model, OpenAI API for chat.
**Novelty:** Pairs a custom-trained classifier with an LLM explainer and persistent history; health-adjacent scope, no validation reported.
**Scope:** small · working: About 2.8k lines across client and server; Devpost claims a functional MVP with a demo video. · polish: Figma designs, short README with setup steps; no live link.
**Claims:** Fully functional MVP | Preliminary assessment instead of costly dermatology access | No accuracy metrics reported
**Gaps:** no accuracy numbers or dataset name; video not viewable
Sources: https://devpost.com/software/skinguard-ai-dermatologist, evidence/hacknyu-hacknyu-2025-skinguard-ai-dermatologist.json (README), https://hacknyu-2025.devpost.com/

---

