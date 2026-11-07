# WEHack: project cards (5 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## WEHack 2025

### Bread Bot  (WEHack 2025)

- **Prizes:** Winner Capital One Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Investor-protection platform combining a CNN-LSTM stock/REIT direction predictor with sentiment analysis, a Solidity peer-to-peer crypto loan marketplace and an investing-mistakes quiz.
- **Problem / user:** New investors face misinformation and risk and hesitate to start with limited capital. / first-time retail investors
- **Domain / idea type:** fintech_finance + education / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; llm_chat
- **Stack:** langs Python; JavaScript; Solidity; frontend HTML; CSS; Web3.js; backend Flask; TensorFlow; Hardhat; db ; hosting 
- **Tech/APIs:** TensorFlow CNN-LSTM (ai_model, core); Solidity smart contracts / Hardhat (other, core); Yahoo Finance data (data_source, core); PRAW (Reddit) + VADER sentiment (data_source, supporting); Gemini (ai_model, unclear); Web3.js / MetaMask (other, supporting)
- **Sponsor APIs:**  | fit: Targeted the Capital One Challenge with an investment risk and financial-literacy platform; the page names no Capital One API or dataset.
- **Repo:** public, commits 20 (before/in/after event: None/None/None), README thin
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims True (Claims 80%+ class accuracy for the price-direction model.)
- **Notes:** Three-part build: custom CNN-LSTM model on Yahoo Finance data (claims 80%+ class accuracy), Reddit/news sentiment, and a smart-contract loan marketplace stated to run on Ethereum mainnet via MetaMask.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/money-makerz) | [GitHub](https://github.com/aasthasharrma/WeHack25/)

### Kairos  (WEHack 2025)

- **Prizes:** Winner Capital One Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** AI fraud-defense platform that flags forged documents (pay stubs, tax returns, IDs) via OCR and Gemini and analyzes live calls for scam signals with Deepgram.
- **Problem / user:** Mid-sized banks and local telecoms are vulnerable to document forgery and scam calls but lack accessible AI fraud tooling. / mid-sized financial institutions and local telecom providers
- **Domain / idea type:** safety_security + fintech_finance / automation_or_agent
- **Platforms / hardware / AI:** mobile_cross; web / False / llm_chat; vision; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend React; Expo; backend Flask; Node.js; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, core); Deepgram (ai_model, core); Tesseract OCR (ai_model, core); Pillow / pdf2image / Poppler (framework, supporting); Expo (framework, supporting); Flask (framework, supporting)
- **Sponsor APIs:**  | fit: Targeted the Capital One Challenge with fraud and loan-document forgery detection aimed at banks; the page names no Capital One API or dataset.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 3, writeup short, impact claims False
- **Notes:** Two detection channels (document forgery via Tesseract/Pillow/pdf2image and real-time call scam detection via Deepgram transcription); Expo mobile frontend; no video or live link listed.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots; event_start; event_end; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/kairos-fnab7r) | [GitHub](https://github.com/charuy2/wehack25)

### Personal Finance / Smart Investment App  (WEHack 2025)

- **Prizes:** Winner CBRE Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Web app for planning monthly budgets and short and long term savings and investments, using past market data and Gemini guidance.
- **Problem / user:** People lack a single tool joining budgeting with investment planning informed by past market performance. / individual savers and beginner investors
- **Domain / idea type:** fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend Python; db MongoDB; hosting 
- **Tech/APIs:** Google Gemini (ai_model, supporting); Yahoo Finance data (data_source, core); MongoDB (database, supporting); Python (framework, core)
- **Sponsor APIs:**  | fit: Finance planning app entered in the CBRE challenge; the page names no CBRE data or API and ties it to the challenge only by the prize.
- **Repo:** public, commits 71 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Canva slide deck linked instead of a demo; no screenshots uploaded; Python models over Yahoo Finance data with MongoDB-stored user profiles.
- **Team size:** 3 | **Confidence:** high | unverified: sponsor_fit_note; event_start; event_end; event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/money-app-z4w7r5) | [GitHub](https://github.com/SarahMendoza/investment-planning-app.git)

### Stock Lock  (WEHack 2025)

- **Prizes:** Winner CBRE Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Streamlit stock tool offering LSTM price prediction, DCA and SWP planning pages and a Gemini chatbot over live Yahoo Finance data.
- **Problem / user:** Retail investors need accessible predictions and systematic investing guidance without market expertise. / retail investors
- **Domain / idea type:** fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs Python; frontend Streamlit; backend Python; db ; hosting Hugging Face Spaces
- **Tech/APIs:** TensorFlow LSTM (framework, core); Yahoo Finance API (data_source, core); Google Gemini API (ai_model, supporting); LangChain (framework, supporting); Streamlit (framework, core)
- **Sponsor APIs:**  | fit: Finance prediction and planning tool entered in the CBRE challenge; the page does not describe use of any CBRE resource.
- **Repo:** public, commits 7 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 22, writeup medium, impact claims False
- **Notes:** Combines a TensorFlow LSTM forecaster with systematic-investment calculators and an LLM chatbot; hosted as a Hugging Face Space.
- **Team size:** 2 | **Confidence:** high | unverified: sponsor_fit_note; event_start; event_end; event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/investai) | [GitHub](https://github.com/gayu2216/StockLock)

### TrendPulse  (WEHack 2025)

- **Prizes:** Winner CBRE Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Dashboard that scans social media for keywords tied to chosen stocks and crypto, runs NLP sentiment analysis and aggregates signals in real time.
- **Problem / user:** Investors cannot track social sentiment across platforms quickly enough to use it. / stock and crypto investors
- **Domain / idea type:** fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; backend Node.js; Python; db MongoDB; hosting 
- **Tech/APIs:** Twitter and Reddit APIs (data_source, core); Apache Kafka (framework, supporting); NLP sentiment models (ai_model, core); MongoDB (database, supporting); React (framework, supporting)
- **Sponsor APIs:**  | fit: Social-sentiment finance tool entered in the CBRE challenge; no CBRE resource used per the page.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** Streams Twitter and Reddit data through Apache Kafka into NLP sentiment models, with a React front end and MongoDB.
- **Team size:** 2 | **Confidence:** high | unverified: sponsor_fit_note; event_start; event_end; event_start; event_end; ui_polish; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/trendpulse) | [GitHub](https://github.com/Ajiyiba/TrendPulse/tree/main)
