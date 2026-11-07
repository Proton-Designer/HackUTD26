# Goldman Sachs - HackUTD 2026 brief
(V = verified from a fetched page; U = unverified/inferred)

## 1. Who they are
Global investment bank / asset manager. [U: general knowledge] Builds client-facing data and analytics platforms (Marquee, GS Quant, GS DAP) and open-source tools. developer.gs.com lists: Curated Data, Security Master, Data Analytics, PlotTool Pro, Portfolio Analytics, GS Quant, Transaction Banking, GS DAP, Liquidity Investing. [V]

## 2. HackUTD 2026 challenge/prize
- Event: HackUTD 2026 "Zero Day", Nov 7-8, 2026, ECSW, UT Dallas, 24-hour hackathon (not 36). [V, zeroday.hackutd.co]
- Goldman Sachs is a Gold sponsor. Day-1 "Goldman Workshop" at 6:10pm. [V]
- Challenge text: **not public**. Site says "This year's challenge tracks will be announced once hacking starts." [V] Prize amounts: not public.
- Warning: hackutd-redesign.pages.dev lists Goldman as Title sponsor and tracks (AI/ML, Healthcare, Sustainability, Cybersecurity, Education, FinTech), but it conflicts with the official 2026 page (and is likely a placeholder/old redesign). Do not rely on it. [V that it conflicts]

## 3. Products / APIs for 24 hours
- GS Quant: Apache-2.0 Python toolkit, `pip install gs-quant`, Python 3.10+. Its APIs need a client ID/secret "available to institutional clients"; others contact sales. [V, github.com/goldmansachs/gs-quant] Docs: https://developer.gs.com/docs/gsquant/ . Whether any no-credential/sandbox use exists: unknown [V that page doesn't say]. Local-only analytics (timeseries/stat functions) may work without credentials [U].
- developer.gs.com services: institutional only, "Register Interest"/contact team; no free tier or pricing listed. [V] So expect NO API access unless the sponsor hands out credentials at the event [U].
- Practical: use public data (FRED, Yahoo/yfinance, SEC EDGAR) [U] and Goldman open source (github.com/goldmansachs) [V exists].

## 4. Prior hackathons
- HackUTD IX (2022): GS track, 4 winners; prizes AirPods Max / Apple TV / $35 Grubhub (devpost track list, fetched from hackutd-ix.devpost.com) [V]. Challenge: "Build a tool for U.S. investors that factors in macroeconomic conditions." Workshop: digital banking platforms at scale. Winners: 1st Horizon; 3rd Finance Planner; runner-up VolatilityAnalysis. [V, https://cs.utdallas.edu/?p=26350]
- HackMIT: sponsored "Best User Experience" prize [V, goldmansachs.com/careers/blog/posts/hackmit.html].
- GS India Hackathon 2026 exists (internal career program) [U, search result only].
- 2023-2025 HackUTD GS prompts: not found. Devpost mirror pages were blocked, so not checked.

## 5. Likely judging values + project ideas (INFERENCE)
Evidence: 2022 prompt emphasized investor tooling + macro data; HackMIT prize emphasized UX. Inferred: clear finance use case, data rigor, polished UX, explainability/risk awareness.
Ideas (inference):
1. Retail-investor macro-regime dashboard (rates/inflation/volatility) with plain-English explanations and scenario sliders.
2. Portfolio stress-tester: LLM-narrated what-if shocks using public data, with uncertainty shown.
3. Financial-literacy / budgeting copilot for students with explainable recommendations.

## 6. Questions for the booth
- What is the actual challenge and judging rubric? Weighting of tech vs. business value?
- Any API credentials, sandbox, or datasets (GS Quant/Marquee) for hackers?
- Are you scoring on UX, quant rigor, or novelty? Is a live demo required?
- What does the 6:10pm workshop cover? Which teams (eng/quant/Marcus?) are judging?

## Sources
- https://zeroday.hackutd.co [V]
- https://cs.utdallas.edu/?p=26350 [V]
- https://hackutd-ix.devpost.com/ [V]
- https://github.com/goldmansachs/gs-quant [V]
- https://developer.gs.com , https://developer.gs.com/docs/gsquant/ [V]
- https://www.goldmansachs.com/careers/blog/posts/hackmit.html [V]
- https://hackutd-redesign.pages.dev/ [conflicting, low trust]
