# VTHacks — VTHacks 13 (1 projects)

### CrediWise - Use the right card, every time.
*VTHacks VTHacks 13 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner [Capital One] $250 Amazon Gift Card

**What it is:** Chrome extension plus web dashboard and Flask backend that detects a checkout page, reads the merchant domain and total, and tells the shopper which of their credit cards earns the most rewards. A dashboard tracks savings and shows spending insights.
**Problem / user:** Credit card holders who lose rewards by picking the wrong card at checkout and do not want manual lookups.

**Features**
- Checkout detection — MV3 content script identifies checkout pages (Amazon, Spotify, Delta cited) and extracts domain and total. *[claimed]*
- Best-card recommendation — Compares user's cards using base rates and scraped public offers; shows banner and popup. *[claimed]*
- Offer scraping and parsing — Bright Data MCP scrapes issuer offers; an LLM parses terms into rules; refreshed every few hours via GitHub Actions. *[claimed]*
- Savings dashboard — React dashboard shows lifetime savings, what other cards would have earned, category breakdowns and charts. *[claimed]*
- AI spending insights — LLM suggests cards based on spending patterns. *[claimed]*
- Card setup — User lists cards they own; only issuer/reward profiles stored, not sensitive card data. *[claimed]*

**Flow:** Install the extension → List the cards you own → Shop and reach a checkout page → Banner/popup recommends the best card → Review savings in the dashboard

**Prompt:** Capital One Best Financial Hack at VTHacks 13: prize for the best finance-themed hack; the listing gives no further brief.
**Fit (implied):** A consumer-finance tool optimizing credit card rewards at purchase time; fits the generic finance brief. No Capital One API is used and no prize is named on the page.  *(targeted: Capital One Best Financial Hack)*
**AI:** An LLM (page says Llama in text, Gemini in tags) parses unstructured card-offer terms into merchant/min-spend/expiry rules and writes spending insights; recommendation logic is rule-based on those rules.
**Architecture:** MV3 extension (content+background scripts) calls a Flask API backed by Supabase Postgres and Upstash Redis cache; scrapers run on a GitHub Actions schedule; React/Tailwind dashboard on Vercel.
**Novelty:** Spans three surfaces (extension, dashboard, scraping pipeline) in one hackathon build; live scraping of offers plus LLM rule extraction is more than a static rewards table.
**Scope:** medium · working: Live Vercel dashboard link, demo video, ~2.4k LOC across extension, frontend, backend with run instructions; no tests. · polish: Five screenshots, folder guide in README, setup flow.
**Claims:** Privacy-first: no sensitive card data stored
**Gaps:** Video not watched; Page inconsistent on Llama vs Gemini; Extension not tried
Sources: https://devpost.com/software/crediwise-use-the-right-card-every-time, evidence/sponsor-vthacks-vthacks-13-crediwise-use-the-right-card-every-time.json, sponsor_prompts_CapitalOne_StateFarm_CBRE.jsonl

---

