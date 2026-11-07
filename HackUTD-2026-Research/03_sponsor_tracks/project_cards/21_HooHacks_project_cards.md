# HooHacks: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## 2025

### Morpheus  (2025)

- **Prizes:** Best Artificial Intelligence (OpenAI credits + 1yr NordVPN/NordPass/Incogni + 1GB Saily) [unknown]  (tier: sponsor_winner)
- **Pitch:** A personal 'second brain' note app with knowledge graph and RAG that exposes the user's context to AI agents such as Claude through an MCP server.
- **Problem / user:** Users must re-explain themselves to every new AI tool because there is no persistent, portable personal context layer. / heavy AI-tool users and knowledge workers
- **Domain / idea type:** ai_agents_infra + productivity_workplace / dev_tool
- **Platforms / hardware / AI:** web; browser_extension / False / llm_chat; rag_or_search; agent_or_tool_use
- **Stack:** langs TypeScript; JavaScript; frontend Tailwind CSS; Vis.js; backend Node.js; Express; db vector database; hosting 
- **Tech/APIs:** OpenAI GPT-3.5 (ai_model, supporting, sponsor); Embeddings / vector search (RAG) (ai_model, core); MCP server for Claude (other, core); Vis.js (framework, supporting); Node.js (framework, supporting)
- **Sponsor APIs:** OpenAI API | fit: Targeted the Nord-sponsored Best AI prize with an OpenAI GPT-3.5 summarization/tagging step plus embeddings-based RAG; no Nord product is shown in use.
- **Repo:** public, commits 47 (before/in/after event: None/None/None), README none
- **Demo/writeup:** video False, live none, screenshots 19, writeup long, impact claims False
- **Notes:** Includes a custom MCP server, Chrome clipper extension and Vis.js graph; two-person team that says it started about 16 hours before the deadline.
- **Team size:** 2 | **Confidence:** high | unverified: sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/morpheus-nu26ai) | [GitHub](https://github.com/dayumsam/morpheus)


## HooHacks 2026

### foreGASt  (HooHacks 2026)

- **Prizes:** Winner Best Financial Hack - Sponsored by Capital One [unknown]  (tier: sponsor_winner)
- **Pitch:** Forecasting tool that links natural gas and fertilizer price data to farm input costs so farmers can anticipate price shocks and financing needs.
- **Problem / user:** Farm prices are inelastic and farmers have few protections against input-cost swings. / farmers and agricultural lenders
- **Domain / idea type:** fintech_finance + sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; llm_chat
- **Stack:** langs Python; frontend Streamlit; Plotly; backend ; db SQLite; hosting Railway; Docker
- **Tech/APIs:** XGBoost (ai_model, core); World Bank and EIA data (data_source, core); Claude (ai_model, supporting); Streamlit (framework, core)
- **Sponsor APIs:**  | fit: Won Best Financial Hack from Capital One with an agricultural price-forecasting tool; the page shows World Bank and EIA data and no Capital One API.
- **Repo:** public, commits 99 (before/in/after event: 0/99/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup long, impact claims False
- **Notes:** XGBoost forecasts on World Bank and EIA data with a Streamlit and Plotly dashboard on Railway; Claude listed among tools; very long writeup (about 1400 words).
- **Team size:** 4 | **Confidence:** high | unverified: event_end; sponsor_fit_note; ui_polish
- **Links:** [Devpost](https://devpost.com/software/hoohacks-submission) | [GitHub](https://github.com/bob3457/HooHacks26)
