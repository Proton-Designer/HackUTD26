# ShellHacks — ShellHacks 2024 (4 projects)

### FiveHacks
*ShellHacks ShellHacks 2024 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner Statefarm

**What it is:** A static HTML/CSS educational website, adapted from a Neocities template, that explains insurance basics and why to choose State Farm, aimed at college students, with an embedded quiz.
**Problem / user:** College students who lack the initiative to open their own insurance accounts.

**Features**
- Insurance explainer pages — Condensed company and 'why choose State Farm' content in short readable sections with custom icons *[shown_working]*
- Embedded quiz — A quiz placed on the site; the team calls it the hardest element to add to the template *[claimed]*

**Flow:** Open the Neocities site → Read the insurance and State Farm pages → Take the embedded quiz

**Prompt:** State Farm 'Making Insurance Easy': build a hack that makes insurance simpler and more helpful for students, e.g. streamlined claims or safety tips.
**Fit (explicit):** Provides plain-language insurance education for students and promotes State Farm; the page frames it as a State Farm submission.  *(targeted: State Farm challenge (Making Insurance Easy))*
**AI:** none
**Architecture:** Static HTML and CSS pages hosted on Neocities, modified from a third-party theme; no backend.
**Novelty:** Very low-tech static site; content-driven rather than interactive.
**Scope:** tiny · working: Live Neocities site linked; page lists no other features. · polish: Custom icons and graphics over a template; no video or repo.
**Gaps:** no repo; live site not opened
Sources: https://devpost.com/software/fivehacks

---

### Lease Saving Plan
*ShellHacks ShellHacks 2024 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Capital One

**What it is:** A Python desktop app for people considering a car lease: it computes monthly lease payments, estimates insurance cost, and tracks savings toward a down payment, with English and Spanish interfaces.
**Problem / user:** Car-lease shoppers, including Spanish speakers, confused by lease payments, insurance and budgeting.

**Features**
- Lease payment calculator — Computes monthly payment from car choice, down payment and term *[shown_working]*
- Insurance estimator — Estimates monthly premium from age, driving history and location *[claimed]*
- Savings tracker — Tracks progress toward the down-payment goal *[claimed]*
- English/Spanish toggle — Switches all UI text between languages *[claimed]*
- Pie-chart breakdowns — Matplotlib charts of cost components *[claimed]*
- Car model database — SQLite store of car models used by calculators *[claimed]*

**Flow:** Pick a car and enter down payment and lease term → Enter age, driving history, location → View lease and insurance estimates and charts → Update savings progress → Toggle language

**Prompt:** Capital One ShellHacks 2024 challenge: design a better mobile experience for financial-services customers using generative AI, data analytics and software engineering.
**Fit (implied):** A personal-finance calculator for leasing and savings; uses no generative AI or mobile UI, so alignment with the stated challenge is loose.  *(targeted: Capital One)*
**AI:** none
**Architecture:** CustomTkinter GUI over Python calculators with an SQLite database of cars and Matplotlib charts, run locally.
**Novelty:** Bilingual desktop calculator combining lease and insurance estimates; solo build.
**Scope:** small · working: README and Devpost describe working calculators; one screenshot; no video or demo link. · polish: Language toggle and charts; repo includes a committed virtualenv which inflates size figures.
**Gaps:** no demo video; loc_estimate inflated by .venv
Sources: https://devpost.com/software/lease-saving-plan, https://github.com/Jackal-HQ/Lease-Saving-Guide (evidence README), sponsor_prompts_*.jsonl (ShellHacks 2024)

---

### SmartCards
*ShellHacks ShellHacks 2024 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Capital One

**What it is:** A web add-on for budgeting apps: the user uploads a receipt photo and the app itemizes the purchases, categorizes them with OpenAI and a local classifier, and shows investing and cashback suggestions.
**Problem / user:** Budgeting-app users who find split transactions awkward and are unsure about investing.

**Features**
- Receipt upload and itemization — Photo is parsed into line items and organized as transactions *[claimed]*
- Item categorization — OpenAI API plus a Flask-served local model trained on a 42k-product Kaggle set (stated 83% accuracy) *[claimed]*
- Investing insights — Personalized investment opportunities and spending recommendations from purchases *[claimed]*
- Cashback and credit card hints — Reminders of cashback options per purchase *[claimed]*
- Charts and OAuth2 login — Chart.js visuals; OAuth2 sign-in *[claimed]*

**Flow:** Land on the site and log in → Upload a receipt photo → Open Items to see categorized purchases → Open Insights for investing and spending suggestions

**Prompt:** Capital One ShellHacks 2024 challenge: better mobile experience for financial-services customers using generative AI, data analytics and software engineering.
**Fit (implied):** Uses GenAI and data analytics to turn receipts into categorized finance data and investing prompts; web rather than mobile.  *(targeted: Capital One)*
**AI:** OpenAI API categorizes transactions and writes investment insights; a separate local classifier on Flask, trained on a Kaggle product dataset, handles item classification.
**Architecture:** React/Vite/Tailwind frontend; Node/Express server plus a Python Flask server for the classifier; OAuth2 login; database for transactions still in progress.
**Novelty:** Pairs receipt itemization with investing nudges inside a budgeting context; runs two backend servers.
**Scope:** small · working: README walkthrough and six Devpost screenshots; frontend and both servers said to be connected; no live link. · polish: Branded landing page and charts; no tests.
**Claims:** Local classifier reaches 83% accuracy on 42,000-product dataset
**Gaps:** no video or live demo
Sources: https://devpost.com/software/smartcards-qxdusb, https://github.com/mavreyn/smart-cards (evidence README), sponsor_prompts_*.jsonl (ShellHacks 2024)

---

### Treasure Keepers
*ShellHacks ShellHacks 2024 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Statefarm

**What it is:** A fantasy-themed Streamlit site that teaches personal finance to low-income, first-generation and immigrant students through quizzes that award coins, a budget builder with charts, and OpenAI-powered advisor characters.
**Problem / user:** First-generation, low-income students and immigrants with limited financial literacy.

**Features**
- Intake form — First page collects user information *[shown_working]*
- Coin-reward quiz — Quiz page tests finance knowledge and awards coins at the end *[shown_working]*
- Budget builder with visuals — Users create a custom budget and see visualizations *[shown_working]*
- Character advisors — OpenAI API replies in distinct fantasy character personalities *[shown_working]*
- Hand-drawn fantasy theme — Krita sprites and backgrounds applied by heavy custom CSS, with music *[shown_working]*

**Flow:** Enter personal info on first page → Take the quiz and earn coins → Build a budget and view charts → Visit advisor page for AI guidance

**Prompt:** State Farm 'Making Insurance Easy': simplify and make insurance useful for students; the project instead teaches general financial literacy.
**Fit (implied):** Teaches student financial literacy in a gamified way; page does not mention insurance or the prompt.  *(targeted: State Farm challenge)*
**AI:** OpenAI chat API prompted with per-character personas to give tailored finance advice; advisor chat not yet interactive.
**Architecture:** Multi-page Streamlit app (Python) with custom CSS/HTML; OpenAI API calls for advice; deployed on Streamlit Cloud.
**Novelty:** Strong visual theming (custom art) on top of Streamlit; persona-driven advisors.
**Scope:** small · working: Live Streamlit app linked on Devpost; multipage flow described. · polish: Custom art, music and navbar; README minimal; repo includes committed venv.
**Gaps:** no video; loc_estimate inflated by venv
Sources: https://devpost.com/software/treasure-keepers, https://github.com/Juuicee/ShellHacks-2024 (evidence README), sponsor_prompts_*.jsonl (ShellHacks 2024)

---

