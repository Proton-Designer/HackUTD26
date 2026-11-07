# WEHack — WEHack 2025 (5 projects)

### Bread Bot
*WEHack WEHack 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner Capital One Challenge

**What it is:** An investor-protection web platform combining a CNN-LSTM model that predicts stock and REIT direction, sentiment analysis of news and Reddit, a Solidity peer-to-peer crypto-collateral loan marketplace, and an investing-mistakes quiz.
**Problem / user:** New and first-time investors with limited capital facing misinformation, opaque risk and high perceived risk in stocks and crypto.

**Features**
- Up/down price prediction — CNN-LSTM in TensorFlow on Yahoo Finance closing prices plus indicators; page claims 80%+ class accuracy *[claimed]*
- Sentiment analysis — VADER scores on financial articles and Reddit posts pulled via PRAW *[claimed]*
- P2P crypto loan marketplace — Solidity contracts verify terms; borrowers list loans against crypto, lenders fund for interest *[claimed]*
- Wallet integration — Web3.js and MetaMask, with crypto holdings view and charts *[claimed]*
- Investing-mistakes quiz — Interactive quiz on what not to do when investing *[claimed]*
- Market simulation — Real-time stock market simulation to test investing readiness *[claimed]*

**Flow:** Explore predictions and sentiment analysis → Take the quiz and simulation → Borrower connects wallet and lists a loan → Lender funds a loan and earns interest

**Prompt:** Open-ended Best Financial Hack: an innovative payment solution, smarter shopping, more accessible financing or financial literacy; Capital One Nessie mock banking API optional.
**Fit (implied):** Investor protection, financial literacy quiz and an alternative lending marketplace fit the open-ended finance brief; no Nessie use is stated.  *(targeted: Capital One Challenge)*
**AI:** CNN-LSTM time-series classifier on price history; VADER lexicon sentiment on articles and Reddit; Gemini listed as a tag with no described role.
**Architecture:** Flask Python backend with TensorFlow model and sentiment pipeline, HTML/JS front end using Web3.js and MetaMask, Solidity contracts deployed with Hardhat.
**Novelty:** Unusual mix of ML prediction, sentiment, education and a blockchain lending marketplace in one hackathon build.
**Scope:** medium · working: Repo with backend and frontend; page claims mainnet loans work; no demo or video. · polish: Dark mode and Figma prototype screenshots; Canva presentation.
**Claims:** 80%+ class accuracy | Blockchain lending operates seamlessly on mainnet
**Gaps:** README empty; repo includes committed virtualenvs; no demo or video; accuracy claim unsupported
Sources: https://devpost.com/software/money-makerz, evidence/sponsor-wehack-wehack-2025-bread-bot.json

---

### Kairos
*WEHack WEHack 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner Capital One Challenge

**What it is:** A fraud-defense prototype for mid-sized companies, banks and local telecoms that flags forged documents such as pay stubs, tax returns and IDs and analyzes ongoing calls for scam signals.
**Problem / user:** Mid-sized companies, banks and local telecom providers exposed to scams and document forgery but overlooked by AI fraud tools.

**Features**
- Document forgery detection — Tesseract OCR and image handling extract text, and Gemini assesses pay stubs, tax returns and IDs submitted with loan applications *[claimed]*
- Live scam call analysis — Deepgram audio analysis with voice tone, sentiment and context to flag scam calls *[claimed]*
- Mobile and web client — React/Expo front end over a Flask backend *[claimed]*

**Flow:** Submit a document for a fraud check → Backend OCRs it and Gemini evaluates it → Monitor a live call for scam signals

**Prompt:** Open-ended Best Financial Hack: an innovative payment solution, smarter shopping, more accessible financing or financial literacy; Capital One Nessie mock banking API optional.
**Fit (implied):** Loan-document fraud detection aimed at banks fits a financial hack; no Nessie use is stated.  *(targeted: Capital One Challenge)*
**AI:** Gemini evaluates documents and call content; Deepgram transcribes and analyzes speech; Tesseract OCR with Pillow and pdf2image preprocessing.
**Architecture:** Expo/React front end calls a Flask backend that runs OCR, Gemini and Deepgram.
**Novelty:** Targets document and voice fraud together for smaller institutions rather than consumers.
**Scope:** small · working: Page describes two detection flows with three uncaptioned screenshots; no metrics, demo or video. · polish: Limited; team cites device integration issues.
**Claims:** Solution banks and telecoms could realistically adopt today
**Gaps:** repo clone failed; no UI walkthrough; no metrics
Sources: https://devpost.com/software/kairos-fnab7r

---

### Personal Finance & Smart Investment App
*WEHack WEHack 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner CBRE Challenge

**What it is:** A web app for planning monthly budgets, goals and a stock portfolio, with per-stock and portfolio return and risk estimates, using a Gemini integration over Yahoo data and an open-source Stock Risk Analyzer that classifies stocks as low, medium or high risk.
**Problem / user:** General users of any experience level who want a combined view of past performance, current budget and future investments.

**Features**
- Monthly budget and spending plan — Configurable budget display and monthly planning *[claimed]*
- Long-term goals — Add and track long-term financial goals *[claimed]*
- Portfolio management — Save, update and delete stocks, with returns and risk metrics per stock and overall *[claimed]*
- Risk classification — Bundled open-source ML Stock Risk Analyzer labels stocks Low, Medium or High from technical indicators *[claimed]*
- Gemini guidance — Gemini API uses Yahoo financial data and personal context *[claimed]*

**Flow:** Set a monthly budget → Add long-term goals → Add stocks to a portfolio → Review estimated returns and risk

**Prompt:** Build a simple web or mobile app, a smart detective that gathers multi-source data, predicts investment risks early and turns complex investment information into clear advice.
**Fit (implied):** Provides portfolio risk and return analytics with AI guidance; the page ties itself to the challenge only through the prize.  *(targeted: CBRE Challenge)*
**AI:** Gemini API receives Yahoo market data and personal context for guidance; a third-party ML classifier rates stock risk from historical data and indicators.
**Architecture:** HTML/CSS/JS front end (pivoted from Flutter) with Python calculations and MongoDB for user data, calling Gemini and Yahoo data.
**Novelty:** Combines budgeting with portfolio risk scoring; relies on an open-source risk analyzer folder; Flutter scaffolding left in repo.
**Scope:** small · working: Repo with risk analyzer and Flutter scaffolds; page says MongoDB outage blocked database work near deadline; no demo. · polish: Canva presentation only.
**Gaps:** no demo; unclear how much of the repo is team-written
Sources: https://devpost.com/software/money-app-z4w7r5, evidence/sponsor-wehack-wehack-2025-personal-finance-smart-investment-app.json

---

### Stock Lock
*WEHack WEHack 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner CBRE Challenge

**What it is:** A Streamlit app where a user enters a stock ticker and gets LSTM-based future price predictions plus RAG-generated insights about the stock and market, built on live Yahoo Finance data and a Gemini chatbot, with DCA and SWP planning pages.
**Problem / user:** Individual investors who want data-driven understanding of market trends rather than just price guesses.

**Features**
- LSTM price prediction — TensorFlow LSTM trained on historical Yahoo Finance series predicts future prices for a ticker *[claimed]*
- RAG market insights — LangChain retrieval with context-tuned LLM to reduce hallucination *[claimed]*
- Gemini chatbot — Chat over live stock data *[claimed]*
- Planning pages — Streamlit pages for DCA and SWP planning (per repo layout) *[claimed]*
- Portfolio extension — Real-time pop-up suggestions during investing *[planned]*

**Flow:** Enter a stock ticker → App pulls live and historical data → LSTM predicts prices → RAG component adds insights → Results shown in Streamlit

**Prompt:** Build a simple web or mobile app, a smart detective that gathers multi-source data, predicts investment risks early and turns complex investment information into clear advice.
**Fit (implied):** Predicts short-term stock movement from historical data with AI insights, matching an example solution; the page does not name the challenge.  *(targeted: CBRE Challenge)*
**AI:** TensorFlow LSTM time-series forecasting; LangChain RAG with Chroma vector store and Gemini for insights.
**Architecture:** Streamlit multi-page app calling Yahoo Finance, an LSTM model and a LangChain RAG pipeline with ChromaDB.
**Novelty:** Pairs price forecasting with retrieval-based explanation; small codebase of about 3k lines.
**Scope:** small · working: Repo with seven code files and Streamlit pages; no demo, video or accuracy numbers. · polish: Basic README with narrative sections.
**Gaps:** no prediction accuracy; no demo
Sources: https://devpost.com/software/investai, evidence/sponsor-wehack-wehack-2025-stock-lock.json

---

### TrendPulse
*WEHack WEHack 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner CBRE Challenge

**What it is:** A dashboard that scans Twitter and Reddit for keywords tied to chosen stocks and crypto, scores sentiment with NLP, and aggregates trend and risk indexes next to market data, with live updates over WebSockets.
**Problem / user:** Stock and crypto traders who find manually tracking social chatter impractical.

**Features**
- Keyword scanning — Pulls posts from Twitter and Reddit APIs matching user-chosen assets, streamed through Kafka *[claimed]*
- Sentiment analysis and classification — NLP scores posts and classifies keywords *[claimed]*
- Trend and risk index — Aggregates sentiment into real-time indexes *[claimed]*
- Dashboard views — React dashboard with Home, Asset detail, Market data and Social data screens *[claimed]*
- Live updates — WebSocket push to the front end *[claimed]*

**Flow:** Pick stocks or crypto to follow → Open asset detail → See market data beside social data and sentiment scores

**Prompt:** Build a simple web or mobile app, a smart detective that gathers multi-source data, predicts investment risks early and turns complex investment information into clear advice.
**Fit (implied):** Uses social sentiment to anticipate market risk, matching one example approach; page does not name the challenge.  *(targeted: CBRE Challenge)*
**AI:** Unspecified NLP sentiment extraction and keyword classification on social posts.
**Architecture:** Twitter/Reddit APIs into Kafka, Python services scoring sentiment into MongoDB, React dashboard with WebSockets.
**Novelty:** Streaming Kafka pipeline for a hackathon; demo admits mock data.
**Scope:** small · working: Four screenshots; backend worked in isolation but front end rendering struggled; demo used mock data. · polish: Not deployed; no video.
**Gaps:** repo clone failed; NLP model unnamed; mock data in demo
Sources: https://devpost.com/software/trendpulse

---

