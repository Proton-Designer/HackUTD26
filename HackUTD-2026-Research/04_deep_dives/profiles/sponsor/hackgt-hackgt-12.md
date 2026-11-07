# HackGT — HackGT 12 (2 projects)

### HR Audit
*HackGT HackGT 12 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Capital One - Best Financial Hack

**What it is:** A voice-first agent platform with two parts. A security co-pilot analyzes fraud, freezes cards and alerts customers by phone, and a voice banking line lets callers run transactions on Nessie data in natural language. A productivity suite automates email, calendar, documents and tasks via Mastra agents.
**Problem / user:** Consumers and businesses: fraud detection has barely changed and many customers still prefer humans on the phone; also staff time lost to routine operations.

**Features**
- AI security co-pilot — Mastra agent on a Cedar-OS dashboard analyzes suspicious activity with OpenAI, freezes cards and alerts customers through Twilio. *[claimed]*
- Phone banking by voice — Callers speak requests over Twilio and Flask executes them against the Nessie API, with custom context storage across calls. *[claimed]*
- Multi-agent ecosystem — Separate agents for alerts, voice calls, account protection and transactions. *[claimed]*
- Email automation — SendGrid sends and tracks enterprise email from agents. *[claimed]*
- Calendar, documents and tasks — Agents schedule events, generate documents and automate tasks; README also mentions a RAG system. *[claimed]*

**Flow:** Co-pilot detects suspicious activity → Agent analyzes, freezes card and alerts customer → Customer calls in and requests banking actions by voice → Context persists through multi-step conversation → Business users trigger email and scheduling agents

**Prompt:** Capital One Best Financial Hack at HackGT 12: build a fintech project that could change how people handle money; judged on creativity, complexity and completeness; Nessie mock banking API offered.
**Fit (implied):** Uses the Nessie API for voice banking and adds AI fraud response, aiming to reimagine financial operations around agent co-pilots.  *(targeted: Capital One - Best Financial Hack)*
**Sponsor tools:** Capital One Nessie API (Account and transaction operations in voice banking, core)
**AI:** Mastra agents orchestrate tasks with OpenAI models for fraud analysis and reasoning; voice handled through Twilio with custom state management; README also lists RAG and name recognition.
**Architecture:** Next.js/React dashboard on Cedar-OS, Mastra agent layer, Flask/FastAPI backend with webhooks (ngrok), Twilio voice and SendGrid email, Nessie for data.
**Novelty:** Broad scope combining fraud response, phone banking and an HR/office productivity suite under one agent framework; the HR framing in the repo name is only loosely tied to the banking pitch.
**Scope:** medium · working: Demo video links (YouTube and Drive); no metrics or live site. · polish: Detailed README with mermaid architecture diagram; tests present; wide feature list with little shown detail.
**Claims:** Serve 1.7B people without smartphones (aspiration) | 70% of customers prefer humans over AI bots (Okta, as cited)
**Gaps:** video not viewed; no metrics; README and Devpost describe somewhat different products
Sources: https://devpost.com/software/the-hr-audit, evidence/sponsor-hackgt-hackgt-12-hr-audit.json

---

### I'd Rather Scroll
*HackGT HackGT 12 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner Capital One - Best Financial Hack

**What it is:** A web app that turns a user's uploaded study notes into short reel-style videos. Gemini reads the file and extracts key points, generates the script, AI voice narrates it, and Pixabay stock footage supplies the background.
**Problem / user:** Students who study from notes and prefer scrolling short videos to reading.

**Features**
- Notes ingestion — User uploads a notes file which Gemini reads. *[claimed]*
- Key point extraction — Gemini pulls the main points from the notes. *[claimed]*
- Reel content generation — Gemini turns key points into short scripted reel content. *[claimed]*
- AI narration — AI voice generation reads the content aloud; provider not named. *[claimed]*
- Video backgrounds — Pixabay stock video is used behind the narration. *[claimed]*

**Flow:** Provide a notes file → Gemini extracts key points and writes reel content → Voice narration and stock video are combined → User scrolls short study reels

**Prompt:** Capital One Best Financial Hack at HackGT 12: build a fintech project that could change how people handle money; judged on creativity, complexity and completeness; Nessie mock banking API offered.
**Fit (none):** Page makes no financial claim and does not mention Nessie or money; no stated connection to the prize.  *(targeted: Capital One - Best Financial Hack)*
**AI:** Google Gemini for reading notes, extracting key points and generating reel content, plus an unnamed AI voice generator.
**Architecture:** React front end calling Gemini, a voice generation service and Pixabay video to assemble reels.
**Novelty:** Study tool styled after short-form video feeds; page is brief and describes a simple pipeline of existing APIs.
**Scope:** tiny · working: Creator says fully working app and links a Vimeo demo; no repo or live site. · polish: Short Devpost text, no screenshots described, no repository.
**Claims:** Got a fully working app up
**Gaps:** no repository; video not viewed; no stated connection to the financial prize
Sources: https://devpost.com/software/i-d-rather-scroll

---

