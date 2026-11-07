# McHacks — McHacks 13 (3 projects)

### Bloomscroll
*McHacks McHacks 13 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Third Place [3rd]; Best AI project that uses the Gumloop API

**What it is:** A SvelteKit study app that turns course uploads into short 'reels' and makes scrolling the way through learning: theory reels teach, test reels quiz, and correct answers advance a progress bar.
**Problem / user:** Students like doomscrolling but find studying rigid; the app channels the scroll habit into a structured learning flow.

**Features**
- Scroll-driven learning flow — Vertical scroll moves the student through ordered study content *[claimed]*
- Theory reels — Gumloop-generated teaching cards from uploaded course content *[shown_working]*
- Test reels — Quiz reels where a correct answer raises the progress bar; wrong answers also shown *[shown_working]*
- Content upload and generation — User uploads course material and Gumloop AI turns it into reels *[claimed]*
- Dashboard and course progress list — Topic list with progress tracking *[shown_working]*
- Progress persistence — MongoDB Atlas stores progress, state and interactions *[claimed]*

**Flow:** Open dashboard → Upload course content → App generates reels → View topic progress list → Scroll through theory and test reels → Answers update progress bar

**Prompt:** not public / not found
**Fit (explicit):** Gumloop AI processes uploaded content and generates the reels; the team notes struggling with Gumloop's logic model. Official prize text for McHacks 13 could not be fetched.  *(targeted: Best AI project that uses the Gumloop API, Third Place)*
**Sponsor tools:** Gumloop (processing uploaded content and generating theory and test reels, core)
**AI:** Gumloop workflows generate learning materials and quiz items from uploaded course content; underlying model not named.
**Architecture:** SvelteKit and Tailwind frontend with MongoDB Atlas for progress; Gumloop for content processing.
**Novelty:** Reuses the short-video scroll pattern as the study interface itself rather than blocking scrolling.
**Scope:** small · working: Demo video and screenshots of dashboard, theory and test reels; repo unreadable. · polish: Short Devpost; no next steps listed; team cites time pressure.
**Claims:** No metrics reported
**Gaps:** evidence status clone_failed and raw README not found; McHacks 13 page unreachable so prize text missing; video not watched
Sources: https://devpost.com/software/brain-rejuvenate

---

### McGill Go
*McHacks McHacks 13 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** First Place [1st]

**What it is:** Full-stack web app that helps McGill students planning an exchange semester find host-university courses that match their own degree requirements, using scraped catalog, equivalency and prerequisite data.
**Problem / user:** Second-year McGill students planning exchange face fragmented information across databases and PDFs when checking which foreign courses count toward their degree.

**Features**
- Equivalent-course matching — Finds courses at chosen partner universities that line up with the student's McGill program requirements, using scraped equivalency and curriculum data. *[claimed]*
- Degree-fit exploration — Students browse host courses and see how they slot into their degree in one place instead of searching several sites. *[claimed]*
- Prerequisite integration — Merges open-source prerequisite data from the mcgill.courses project into the match results. *[claimed]*
- Curriculum digitization and transcript extraction — Structures program requirements so courses can be compared programmatically. *[claimed]*
- Partner institution data collection — Selenium scrapers pull course catalogs and equivalency tables from JavaScript-heavy university sites. *[claimed]*
- Course eligibility logic — Backend logic decides whether a course is eligible against a student's requirements. *[unclear]*

**Flow:** Student opens the web app → Selects host universities → Sees courses that match their McGill requirements → Reviews how each course fits the degree and its prerequisites

**Prompt:** McHacks 13 top three prizes: first place paid $2,000 cash; all projects auto-entered and judged on execution, technical complexity, impact and creativity.
**Fit (none):** No stated prize targeting; entered in the general top-3 pool, where it addresses a concrete student problem with a working scraped-data pipeline.  *(targeted: First Place [1st])*
**AI:** Built-with tags list Claude, Gemini and Cursor, but the page does not say how models are used inside the product (vibe-coding is mentioned for development).
**Architecture:** Next.js/React frontend calls a FastAPI backend backed by MongoDB; Selenium scrapers collect catalog, equivalency and curriculum data, supplemented by open prerequisite data.
**Novelty:** Targets a niche but real student workflow (exchange credit transfer) with scraped real university data rather than a generic chatbot.
**Scope:** small · working: Devpost says a fully functional full-stack app was built and a demo video exists; repo clone failed so nothing verified. · polish: Demo video and five screenshots; no live link or README read.
**Claims:** Team says it built a fully functional full-stack application in a short time | No accuracy or user metrics reported
**Gaps:** Repo clone failed and README not retrievable via raw or GitHub fetch; Video content not seen; Sizes of repo unknown; Matching accuracy unquantified
Sources: https://devpost.com/software/exchange-v1hmq8, https://mchacks13.devpost.com/

---

### WaterYouDoin
*McHacks McHacks 13 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Second Place [2nd]

**What it is:** Chrome extension (Manifest V3) that classifies prompts locally before they reach an AI assistant, sending factual lookups to a search engine, blocking low-value ones and nudging users to think first on reasoning-heavy ones, with a water-saved counter.
**Problem / user:** Developers who use AI assistants for trivial lookups and repetitive prompts, and the resource use that causes.

**Features**
- Local prompt classification — Heuristic classifier sorts prompts into factual, low-value or reasoning-heavy, with an ML fallback for ambiguous ones; runs in the browser. *[shown_working]*
- Factual redirect — Factual prompts are redirected to a non-AI search engine instead of being sent to the assistant. *[claimed]*
- Low-value blocking and think-first nudge — Low-value prompts are blocked; reasoning-heavy prompts get a gentle nudge with a mascot and suggested next step. *[claimed]*
- Water-saved stats — Local token estimate via gpt-tokenizer turns avoided prompts into estimated water saved, shown daily and lifetime in a popup. *[shown_working]*
- Edge-case handling — Handles short but meaningful prompts and duplicate submissions. *[claimed]*
- Privacy by design — No backend or network calls; storage stays in Chrome storage. *[shown_working]*

**Flow:** User installs the unpacked extension → Types a prompt in an AI assistant → Extension classifies it before submission → Redirect, block or nudge depending on class → Popup shows avoided usage and water saved

**Prompt:** McHacks 13 top three prizes (second place was Meta Ray-Ban glasses); every project auto-entered; judged on execution, technical complexity, impact and creativity.
**Fit (none):** No stated prize targeting; entered in the general pool, with a sustainability angle (reducing unnecessary AI calls) and a fully local build.  *(targeted: Second Place [2nd])*
**AI:** No hosted model: heuristic NLP classifier plus a small local scikit-learn-derived ML fallback; gpt-tokenizer for token counts.
**Architecture:** MV3 extension with background script, content script intercepting prompts, popup/options/nudge pages and local storage; separate Python ml/ folder for dataset evaluation, Vite build.
**Novelty:** Inverts the usual AI tool: it discourages AI use, quantifies it as water saved, and does so with no cloud inference.
**Scope:** small · working: README gives build and load instructions plus Vitest suite; Devpost claims over 180 unit tests; repo has tests. · polish: Mascot, popup/options UI, README screenshots, demo video.
**Claims:** Over 180 unit tests on real developer prompts | Zero backend, fully local classification
**Gaps:** No water-savings figures; Video not seen
Sources: https://devpost.com/software/wateryourdoin, https://github.com/memoud0/WaterYouDoin, evidence/mchacks-mchacks-13-wateryoudoin.json, https://mchacks13.devpost.com/

---

