# HackNC — HackNC 2024 (1 projects)

### AI-powered Investment Portfolio Creator
*HackNC HackNC 2024 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Capital One - Best Financial Hack

**What it is:** Full-stack web app for beginner stock investors: they answer a short series of chat-style prompts and get a personalized stock portfolio. Stock picks are filtered by risk statistics computed from Yahoo Finance history, with Gemini integrated for responses.
**Problem / user:** Beginner investors who find starting to invest intimidating and want a quick, easy personalized portfolio.

**Features**
- Preference questionnaire in text-bubble UI — User answers a few prompts shown as chat bubbles; answers drive portfolio selection. *[claimed]*
- Risk-based stock selection — Backend screens stocks on max drawdown, historical volatility and beta calculated from yfinance data with pandas/NumPy. *[shown_working]*
- Portfolio optimization model — A quantitative backend builds the portfolio from the screened stocks (per team bios; README lists the criteria). *[claimed]*
- Gemini LLM integration — Gemini API (frontend package present) generates insights and responses. *[claimed]*
- Ticker logos — Third-party logo lookup shows company logos next to holdings. *[claimed]*

**Flow:** Open the web app → Answer the investor-profile prompts → Backend pulls market data and scores stocks → Receive a tailored portfolio with logos and Gemini-written explanations

**Prompt:** Capital One Best Financial Hack at HackNC 2024: a fintech build such as innovative payments, smarter consumer shopping, accessible financing or financial literacy, scored on creativity, complexity and completeness.
**Fit (implied):** Fits the open financial-hack brief as an investing-education/portfolio tool for novices; no Capital One API is used and the page does not name the prize it targets.  *(targeted: Capital One - Best Financial Hack)*
**AI:** Gemini LLM integrated for insights/responses; portfolio construction itself is classical quant (drawdown, volatility, beta, optimization) rather than LLM-driven.
**Architecture:** React/TypeScript/Tailwind frontend calls a Flask backend; backend pulls yfinance market data, computes risk metrics with pandas/NumPy, optimizes, and calls Gemini and logo APIs.
**Novelty:** Combines classical risk metrics with an LLM chat layer for novices; otherwise a conventional hackathon robo-advisor with no bank or sponsor API.
**Scope:** small · working: Demo video on Vimeo and a ~860-line repo; no live link; deployment was reported as a struggle. · polish: Chat-bubble UI, Tailwind components, logos; no tests in repo despite page mentioning tests.
**Claims:** Integrated an LLM into the app | Won Capital One Best Financial Hack at HackNC 2024
**Gaps:** Video not watched; Exact optimization method not documented; Screenshot count unknown
Sources: https://devpost.com/software/ai-powered-investment-portfolio-creator, evidence/sponsor-hacknc-hacknc-2024-ai-powered-investment-portfolio-creator.json, sponsor_prompts_CapitalOne_StateFarm_CBRE.jsonl

---

