# HackRPI — 2025 (1 projects)

### ByteBite
*HackRPI 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best Data Science Hack (+ Nord bundle: 1yr NordVPN/NordPass/NordProtect/Incogni, 1GB Saily, 3-month nexos.ai with 200 EUR credit)

**What it is:** Web app for RPI students that scrapes campus dining-hall menus and uses a ranking engine plus Gemini to score dishes against each student's allergies, diet and goals, with warnings and special health modes.
**Problem / user:** Students with allergies, athletes and people with chronic conditions who struggle to find safe or healthy dining-hall food.

**Features**
- Menu scraping — Automatically pulls current dining-hall menus. *[claimed]*
- Personalized meal scoring — Ranking engine scores items against allergies, diet and goals and returns warnings. *[claimed]*
- Allergy alerts and filters — Flags unsafe items in real time. *[claimed]*
- Health modes — Diabetic, low-sodium and high-protein modes. *[claimed]*
- Text-to-speech and custom UI — Accessibility features listed in the README. *[claimed]*
- Mood tracking and health avatar — Gamified avatar and mood tracking. *[claimed]*

**Flow:** Onboard with allergies, diet and goals → App fetches the current menu → Ranking engine scores items → Browse main screen and menu page with warnings

**Prompt:** not public / not found
**Fit (implied):** Analyzes scraped menu data with a custom scoring engine; no official prize description was found, and the Nord add-on has no brief.  *(targeted: Best Data Science Hack)*
**AI:** Gemini analyzes menu items for nutrition/allergen content; a custom ranking engine combines that with the user's profile for scores.
**Architecture:** React frontend and Flask backend with a scraper feeding menu data into Gemini analysis and the ranking engine; deployed on Render at a custom domain.
**Novelty:** Tailored to one campus's dining halls with health-condition modes; otherwise a standard menu-plus-LLM nutrition assistant.
**Scope:** small · working: Custom-domain site named in README and ~4.6k LOC of code; no video; repo has CI and tests. · polish: Two screenshots, accessibility TTS, theming options.
**Claims:** Fully working nutrition assistant built in under 24 hours
**Gaps:** No official prize text for Best Data Science Hack; Site not opened
Sources: https://devpost.com/software/bytebite-5ohg82, evidence/sponsor-hackrpi-2025-bytebite.json, sponsor_prompts_Nord_Saily_Incogni.jsonl

---

