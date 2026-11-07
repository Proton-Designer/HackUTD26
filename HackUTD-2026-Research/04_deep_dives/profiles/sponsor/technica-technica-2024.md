# Technica — Technica 2024 (1 projects)

### Pennywise
*Technica Technica 2024 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Capital One: Best Financial Hack

**What it is:** An event-budgeting web app: users enter event type, date and expected costs, then get budget allocation, an AI financial-advice chatbot and spending analytics, with options to set pronouns and accommodations.
**Problem / user:** People planning events who struggle to stay within budget.

**Features**
- Event budget form — Collects event type, date and expected expense *[shown_working]*
- Budget allocation — Splits budget by event type and size *[claimed]*
- AI advisor chatbot — Gemini-based chat for personalized budget advice *[claimed]*
- Spending analytics — Visual charts of spending patterns *[claimed]*
- Profile and accommodations — Update name, pronouns and accessibility needs *[shown_working]*

**Flow:** Fill in event form → See budget allocation → Chat with AI advisor → Review analytics → Edit settings

**Prompt:** Capital One Technica 2024 Best Financial Hack: build a tool for any finance-related need using creativity and technical skill.
**Fit (implied):** Personal budgeting tool with AI advice; page lists the prize win without quoting the prompt.  *(targeted: Capital One: Best Financial Hack)*
**AI:** Gemini listed as the advisor model; page gives no integration detail.
**Architecture:** React/Ant Design frontend deployed on Vercel with a Flask backend.
**Novelty:** Includes pronoun and accommodation settings in a budgeting app; otherwise a typical budgeting chatbot.
**Scope:** small · working: Live Vercel demo and video linked; four screenshots. · polish: Ant Design UI; team new to React and backend.
**Gaps:** backend stack conflict (Flask vs Node); video not watchable
Sources: https://devpost.com/software/pennywise-84p1il, https://github.com/Yashaswe/pennywise (evidence README), sponsor_prompts_*.jsonl (Technica 2024)

---

