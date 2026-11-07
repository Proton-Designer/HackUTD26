# HackUTD 2026 sponsor playbook cards (Q13)

Draft by eng1 for TASK-103. Source of every count: `data/tables/Q13_sponsor_card_rows.csv` (one row per past award from a HackUTD 2026 sponsor), computed by `scripts/s7_sponsor_cards.py` into `data/tables/Q13_sponsor_card_stats.csv`. Brief facts are from `06_hackutd_2026_sponsors/` and keep its [V] verified / [U] unverified marks. Dataset beats the briefs where they disagree (pnc, toyota, cbre).

Reading rules:
- Counts are 'n of N (pct%)'. Cards with N < 5 are marked LOW N; any single-digit count is an anecdote, not a rule. Winners are unweighted projects-awards, not a win rate (spec rule 1).
- 'placement unranked' = the event does not publish 1st/2nd/3rd for that prize (HackUTD badges never do). Most rows are unranked, so these cards describe WHAT sponsors rewarded, not what beat what.
- `prompt_literalness` 0/1/2 = how closely the winner follows the sponsor prompt; `na` = prompt text unavailable or no prompt. `sponsor_removable` = could the sponsor's tech be removed without breaking the project. Both are analyst tags.
- Many rows come from other hackathons where the same company sponsored; the event is shown on every line. All 2026 challenge texts are NOT public (revealed Sat ~12:00 CT), so every pitch angle is inference.
- Sponsors with 0 dataset winners (8090 AI, AT&T, Axxess, Niantic Spatial, Winstead PC) have [brief only] cards.

## T-Mobile
- Tier: Title
- What the sponsor asked: Challenge text NOT public [V]; revealed at hacking start; up to 2 sponsor tracks [V]. 2025 prompt (inferred from winners, [U]): a tool for T-Mobile product managers to understand customer sentiment/pain points in real time. T-Mobile Fireside Chat Sat 1:30pm [V].
- Prize structure: 2025: 1st iPhone 17, 2nd iPad Air, 3rd Beats Studio Pro [V]. 2026 prizes not public [V].
- Past winners in dataset: 7 awards across 3 events (DubHacks 2026 x3; HackUTD 2025 x3; DubHacks 2025 x1).
  - Formly - the secure, fast form filler — DubHacks 2026, placement 1, docs_to_action, owner=consumer: People filling long forms click a button and get forms filled from their own files with per-field sources and approval. <https://devpost.com/software/formly-the-secure-fast-form-filler>
  - Starward — DubHacks 2026, placement 2, data_to_decision, owner=consumer: Hikers pick a trail and get estimated satellite texting coverage, check-in spots, a buy-or-not recommendation and shareable plan. <https://devpost.com/software/starward>
  - HarmoniQ — HackUTD 2025, placement 3, data_to_decision, owner=sponsor_internal_or_b2b: T-Mobile product managers and network engineers see network metrics, social sentiment and outage risk predictions in one dashboard. <https://devpost.com/software/x-yiqm81>
  - Kill-Switch — DubHacks 2026, placement 3, risk_detect_and_respond, owner=consumer: Older and disabled users get LED, buzzer and LCD fraud warnings from an ESP32, with a button that texts a caregiver. <https://devpost.com/software/kill-switch-sb82du>
  - InsighT — HackUTD 2025, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: T-Mobile product managers see customer sentiment and outages by area and get Gemini-written prioritized opportunities and PRDs. <https://devpost.com/software/t-insights>
  - Beacon — HackUTD 2025, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: T-Mobile call agents and PR teams see a live 0-100 customer happiness score fused from calls, social posts and outages. <https://devpost.com/software/na-504rkg>
  - CareLens; Roam — DubHacks 2025, placement unranked, risk_detect_and_respond, owner=consumer: Elderly people living alone and caregivers get offline camera fall detection on a Raspberry Pi that raises a local alarm. [no link in dataset]
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: data_to_decision: 4 of 7 (57%); risk_detect_and_respond: 2 of 7 (29%); docs_to_action: 1 of 7 (14%)
  - problem_owner: consumer: 4 of 7 (57%); sponsor_internal_or_b2b: 3 of 7 (43%)
  - prompt_literalness: 0: 1 of 7 (14%); na: 6 of 7 (86%)
  - sponsor_removable: yes: 7 of 7 (100%)
  - sponsor_features_used: median 0; 0: 5 of 7 (71%); 1: 2 of 7 (29%)
  - placement: unranked: 3 of 7 (43%); 3: 2 of 7 (29%); 1: 1 of 7 (14%); 2: 1 of 7 (14%); prize_kind: sponsor_domain: 4 of 7 (57%); sponsor_open: 3 of 7 (43%)
- What won:
  - FINDING: The three HackUTD 2025 T-Mobile winners are PM/ops sentiment dashboards, the DubHacks winners are consumer tools, and none needed a T-Mobile product (sponsor_removable yes: 7 of 7 (100%)).
    SUPPORT: 4 of 7 (57%) (unweighted, pattern=data_to_decision); examples: Starward (DubHacks 2026) <https://devpost.com/software/starward>, HarmoniQ (HackUTD 2025) <https://devpost.com/software/x-yiqm81>, InsighT (HackUTD 2025) <https://devpost.com/software/t-insights>
    COUNTEREXAMPLES: Formly - the secure, fast form filler (DubHacks 2026) <https://devpost.com/software/formly-the-secure-fast-form-filler>, Kill-Switch (DubHacks 2026) <https://devpost.com/software/kill-switch-sb82du>, CareLens; Roam (DubHacks 2025) [no link in dataset]
    CONFIDENCE: low (n<10; tags are analyst judgments)
    TYPE: association
    IMPLICATION FOR US: Treat T-Mobile as a problem-fit track: show a named persona and a ranked-actions output; no API is needed.
  - FINDING: In HackUTD 2025 the T-Mobile track was crowded with near-identical sentiment dashboards.
    SUPPORT: entries targeting T-Mobile: winners 3 of 36 (8%), demo_ready baseline 8 of 50 (16%), random baseline 8 of 50 (16%) (table Q19_hackutd2025_track_targeting.csv; counts only, not a win rate); examples: winners Beacon, HarmoniQ, InsighT; baseline MagentaMonitor, PulseWire, SentimentRadar
    COUNTEREXAMPLES: none found
    CONFIDENCE: medium (counts exact; the 'near-identical' reading is from the close read)
    TYPE: fact (counts) / inference (reading)
    IMPLICATION FOR US: if the 2026 prompt is again 'sentiment/insights', differentiation (a different persona, a real action loop, live data) matters more than polish alone.
- Pitch angle (inference): Pitch the T-Mobile customer/business problem first, name the persona, show the ranked action on screen before anything else. Brief directions: customer-experience signal engine (differentiated from 2025), SIM-swap/number-verification fraud demo with a mocked network API, Quality-on-Demand scenario app.
- Integration depth rule (inference): Problem-fit depth is enough (0 sponsor features used: 5 of 7 (71%)). Add a network-API mock behind an interface only if the prompt asks.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv, Q19_hackutd2025_track_targeting.csv.

## AT&T — [brief only] no dataset winners
- Tier: Other (presents Saturday dinner)
- What the sponsor asked: No AT&T challenge or prize listed [V]; AT&T absent from 2022/2023/2025 Devpost prize pages [V]; 2024 unknown. T-Mobile is title sponsor, so a telecom-themed track is likely T-Mobile's [V for title; rest U]. Aduna/CAMARA network APIs (Number Verification, SIM Swap) exist [V]; hackathon sandbox status unknown.
- Past winners in dataset: 0 of 0 (no rows in Q13_sponsor_card_rows.csv). Counts, findings: not available.
- Pitch angle (inference): [inference] Do not plan around an AT&T prize. If one appears, SIM-swap/number-verification fraud defence (mocked behind an interface) or low-signal resilience are the brief's directions.
- Integration depth rule (inference): [inference] Ask at the booth first; do not spend integration effort before a prize is confirmed.
- Source: brief only (`06_hackutd_2026_sponsors/`); Q13_sponsor_card_rows.csv has 0 rows for this sponsor.

## PNC Bank
- Tier: Platinum
- What the sponsor asked: Challenge text NOT public [V]; workshop Sat 2:30pm [V]. 2025 challenge statements came in a hackerpack at hacking start [V]. The brief says it could not identify 2024/25 PNC winners and calls 2024 'unknown'; the dataset has 3 HackUTD 2024 + 3 HackUTD 2025 PNC winners (dataset wins over the brief, STATUS open issue).
- Prize structure: 2025: 1st PlayStation 5 Slim, 2nd Ray-Ban Meta glasses, 3rd Yaber T1 Pro-Mini projector [V]. 2026 not public.
- Past winners in dataset: 6 awards across 2 events (HackUTD 2025 x3; HackUTD 2024 x3).
  - AutoPM — HackUTD 2025, placement unranked, workflow_automation_agent, owner=unknown: Product managers get eight Gemini agents that generate ideas, stories, RICE rankings, wireframes, emails and Jira tickets. <https://devpost.com/software/autopm-2tjzu8>
  - ProdPlex — HackUTD 2025, placement unranked, workflow_automation_agent, owner=sponsor_internal_or_b2b: Product managers combine specialist Nemotron agents to research, strategize and draft a PRD in minutes. <https://devpost.com/software/prodify-94vbpk>
  - Data Pattern Observatory — HackUTD 2024, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Enterprise data and platform teams monitor how data moves across stores and see anomalies and predicted flows in a dashboard. <https://devpost.com/software/data-pattern-observatory>
  - Hermes — HackUTD 2024, placement unranked, data_to_decision, owner=consumer: Unbanked people, especially Hispanic communities, view balance, trade crypto and see price predictions and risk analysis in a wallet app. <https://devpost.com/software/hermes-c2onvq>
  - ProDuh! — HackUTD 2025, placement unranked, docs_to_action, owner=sponsor_internal_or_b2b: Product managers turn goals, KPIs and messy notes into Jira or ADO ready stories via a multi-agent assistant. <https://devpost.com/software/produh>
  - FinnAI — HackUTD 2024, placement unranked, data_to_decision, owner=consumer: Everyday people track spending and savings goals and get budgeting advice from an AI chatbot. <https://devpost.com/software/finnai>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: data_to_decision: 3 of 6 (50%); workflow_automation_agent: 2 of 6 (33%); docs_to_action: 1 of 6 (17%)
  - problem_owner: sponsor_internal_or_b2b: 3 of 6 (50%); consumer: 2 of 6 (33%); unknown: 1 of 6 (17%)
  - prompt_literalness: 2: 2 of 6 (33%); na: 4 of 6 (67%)
  - sponsor_removable: yes: 6 of 6 (100%)
  - sponsor_features_used: median 0; 0: 6 of 6 (100%)
  - placement: unranked: 6 of 6 (100%); prize_kind: sponsor_domain: 6 of 6 (100%)
- What won:
  - FINDING: PNC winners were data-to-decision or workflow-agent tools built around the prompt rather than a PNC API, and prompt text is unavailable for most.
    SUPPORT: 6 of 6 (100%) (unweighted, sponsor_removable=yes); examples: AutoPM (HackUTD 2025) <https://devpost.com/software/autopm-2tjzu8>, ProdPlex (HackUTD 2025) <https://devpost.com/software/prodify-94vbpk>, Data Pattern Observatory (HackUTD 2024) <https://devpost.com/software/data-pattern-observatory>
    COUNTEREXAMPLES: none
    CONFIDENCE: low (n<10; tags are analyst judgments)
    TYPE: association
    IMPLICATION FOR US: Plan problem-fit with a clean fintech/fraud/payments story; mock PNC-style APIs behind an interface.
- Pitch angle (inference): Brief directions: payee/account verification and fraud prevention, instant payout for gig workers, mobile check-deposit assistant. Lead with the payments/fraud problem and a visible agent or analytics output.
- Integration depth rule (inference): Problem-only depth; API use cannot be a requirement because 2026 credentials are unknown.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

## Goldman Sachs
- Tier: Gold
- What the sponsor asked: Challenge text NOT public [V]; workshop Sat 6:10pm [V]. 2022 prompt: 'Build a tool for U.S. investors that factors in macroeconomic conditions' [V]. GS Quant/developer.gs.com need institutional credentials [V]: expect no API access unless handed out [U].
- Prize structure: 2022: AirPods Max / Apple TV / $35 Grubhub, 4 winners [V]. 2026 not public.
- Past winners in dataset: 6 awards across 2 events (HackUTD 2025 x3; HackUTD 2024 x3).
  - TrustIssues.AI — HackUTD 2025, placement unranked, docs_to_action, owner=sponsor_internal_or_b2b: Compliance teams upload vendor PDFs and four agents screen sanctions, score risk by rules and await manager approval. <https://devpost.com/software/coffee-overflow>
  - AutoBoard — HackUTD 2025, placement unranked, docs_to_action, owner=sponsor_internal_or_b2b: Financial compliance teams onboard vendors faster with document extraction, a questionnaire, risk scoring and one-click approval. <https://devpost.com/software/404-not-found-us43mg>
  - Lumo — HackUTD 2024, placement unranked, realtime_coordination, owner=consumer: Unbanked and underbanked roommates split expenses by charging each member's card at purchase, so nobody fronts cash. <https://devpost.com/software/pay-your-daddy>
  - Stamped — HackUTD 2025, placement unranked, other, owner=sponsor_internal_or_b2b: Bank staff, clients and vendors use role-based dashboards to manage client onboarding from lead to completion. <https://devpost.com/software/stamped-6hnl4w>
  - TalkTuahBank — HackUTD 2024, placement unranked, voice_to_action, owner=consumer: Phone-call voice banking assistant for unbanked adults without internet, checking balances, moving money and paying bills via multi-agent LLM. <https://devpost.com/software/talktuahbank>
  - AllBank: Inclusive, Intelligent, Impactful — HackUTD 2024, placement unranked, other, owner=consumer: Mobile banking app for underbanked individuals and small businesses with QR payments, goal savings and a Gemini assistant. <https://devpost.com/software/allbank>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: docs_to_action: 2 of 6 (33%); other: 2 of 6 (33%); realtime_coordination: 1 of 6 (17%); voice_to_action: 1 of 6 (17%)
  - problem_owner: sponsor_internal_or_b2b: 3 of 6 (50%); consumer: 3 of 6 (50%)
  - prompt_literalness: na: 6 of 6 (100%)
  - sponsor_removable: yes: 6 of 6 (100%)
  - sponsor_features_used: median 0; 0: 6 of 6 (100%)
  - placement: unranked: 6 of 6 (100%); prize_kind: sponsor_domain: 6 of 6 (100%)
- What won:
  - FINDING: Goldman winners did not use Goldman tooling (removable: 6 of 6 (100%)) and their prompt text is not in the dataset (prompt_literalness na: 6 of 6 (100%)).
    SUPPORT: 6 of 6 (100%) (unweighted, sponsor_removable=yes); examples: TrustIssues.AI (HackUTD 2025) <https://devpost.com/software/coffee-overflow>, AutoBoard (HackUTD 2025) <https://devpost.com/software/404-not-found-us43mg>, Lumo (HackUTD 2024) <https://devpost.com/software/pay-your-daddy>
    COUNTEREXAMPLES: none
    CONFIDENCE: low (n<10; tags are analyst judgments)
    TYPE: association
    IMPLICATION FOR US: Do not rely on GS Quant (institutional credentials); use public market data (FRED, EDGAR) and show a clear finance story with explainability.
- Pitch angle (inference): Retail-investor macro/risk explainer or portfolio stress-test with plain-English narration and visible uncertainty; polish UX (the HackMIT GS prize was a UX prize [V]).
- Integration depth rule (inference): Problem-fit only; no sponsor feature can be assumed available.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

## Capital One
- Tier: Silver (official page); the unofficial redesign page lists Platinum, low trust
- What the sponsor asked: Challenge text NOT public [V]. Only verified item: 'Switch Competition' Sat 6:45pm ECSW 4.210 (what it is: unverified) [V]. Nessie/DevExchange mock APIs may be retired [U].
- Prize structure: HackUTD IX (2022): 1 winner, 50 Amazon gift cards [V]. 2026 not public.
- Past winners in dataset: 42 awards across 33 events (HackGT 12 x2; Bitcamp 2025 x2; PennApps XXVI (Fall 2025) x2; DivHacks 2026 x2; HackRice 15 x2; ShellHacks 2024 x2; ...).
  - SpendingWithSpendy — HackUTD 2025, placement unranked, other, owner=consumer: Kids tap an NFC Spendy card to buy in-game currency while parents review spending and reload funds. <https://devpost.com/software/spendingwithspendy>
  - Localized — HackNC 2025, placement unranked, realtime_coordination, owner=consumer: UNC students claim weekly free coupons from Franklin Street businesses and redeem by QR code; businesses track redemptions. <https://devpost.com/software/localized>
  - HR Audit — HackGT 12, placement unranked, voice_to_action, owner=consumer: Consumers and businesses get voice-first AI agents that handle fraud response, phone banking and office workflows. <https://devpost.com/software/the-hr-audit>
  - I'd Rather Scroll — HackGT 12, placement unranked, education_feedback, owner=consumer: Students upload study notes and get short reel-style videos narrated by AI over stock footage. <https://devpost.com/software/i-d-rather-scroll>
  - BudgetBuddy — Bitcamp 2025, placement unranked, data_to_decision, owner=consumer: College-age users see a virtual pet react to their spending and chat with it for tone-controlled budgeting feedback. <https://devpost.com/software/budgetbuddy-3qvr78>
  - FinGuard — Bitcamp 2025, placement unranked, data_to_decision, owner=consumer: Online shoppers get a browser extension recommending the best linked credit card, warning of scam sites, plus spending insights. <https://devpost.com/software/finguard-x1akuc>
  - PAWS - Personal Assets and Wise Saving — TAMUhack 2025, placement unranked, data_to_decision, owner=consumer: Young people get a budget and savings plan from their transactions and earn points toward collectible cats. <https://devpost.com/software/cat-finances>
  - Drift — TAMUhack 2026, placement unranked, data_to_decision, owner=consumer: Young adults connect a bank account, state a goal in plain English and see success odds from 100,000 Monte Carlo simulations. <https://devpost.com/software/pff>
  - EcoFin Carbon — HackTX 2025, placement unranked, data_to_decision, owner=consumer: Eco-minded consumers see carbon emissions per bank transaction on a dashboard and get a Gemini coach for greener spending. <https://devpost.com/software/ecofin-carbon>
  - BreakingPoint — HackTX 2026, placement unranked, data_to_decision, owner=consumer: People hit by a surprise car repair see a 30-day cash-flow consequence graph and ranked recovery plans. <https://devpost.com/software/breakingpoint>
  - Velum — HackIllinois 2026, placement unranked, other, owner=sponsor_internal_or_b2b: Businesses harden documents so AI extraction fails, anchor them on Solana, and run Nessie banking workflows. <https://devpost.com/software/velum>
  - foreGASt — HooHacks 2026, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Farmers get 30/60/90-day fertilizer price forecasts with risk ranges and a buy-now-or-wait recommendation. <https://devpost.com/software/hoohacks-submission>
  - Plate-O — PennApps XXV (Fall 2024), placement unranked, data_to_decision, owner=consumer: Budget-conscious takeout customers get restaurant and surprise-meal picks sized to a budget computed from their bank data. <https://devpost.com/software/plate-o>
  - SproutAI — PennApps XXVI (Fall 2025), placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Grocery retailers forecast demand with ML and see sustainability scores to cut food waste. <https://devpost.com/software/sproutai-9vil8w>
  - Subsave — PennApps XXVI (Fall 2025), placement unranked, data_to_decision, owner=consumer: Subscription payers prepay a year into a DeFi yield vault so simulated yield offsets costs, with monthly cancellation. <https://devpost.com/software/subsave>
  - edgecart. — HackPrinceton Fall 2025, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Grocery stores detect produce decay by camera and push targeted discounts to shoppers who buy that item. <https://devpost.com/software/edgecart>
  - Roots — HackPrinceton Spring 2025, placement unranked, data_to_decision, owner=consumer: Young adults learning finance get budgeting sliders, Gemini portfolios, card recommendations and lessons on simulated Nessie accounts. <https://devpost.com/software/roots-xk19te>
  - C2Pay — HackHarvard 2025, placement unranked, risk_detect_and_respond, owner=sponsor_customers: Payment app developers embed an SDK that scores risk and escalates to signed C2PA proofs only for risky payments. <https://devpost.com/software/c2pay>
  - AI-powered Investment Portfolio Creator — HackNC 2024, placement unranked, data_to_decision, owner=consumer: Beginner investors answer a few prompts and get a personalized stock portfolio screened by risk statistics. <https://devpost.com/software/ai-powered-investment-portfolio-creator>
  - RxSolve — HackNC 2026, placement unranked, workflow_automation_agent, owner=sponsor_internal_or_b2b: Independent pharmacies get an agent that detects underpaid prescription claims, files appeals across channels and settles recoveries on a sandbox ledger. <https://devpost.com/software/rxsolve>
  - CrediWise - Use the right card, every time. — VTHacks - 13, placement unranked, data_to_decision, owner=consumer: Online shoppers with several credit cards get a checkout-time recommendation of the card earning most rewards, plus a savings dashboard. <https://devpost.com/software/crediwise-use-the-right-card-every-time>
  - LoadCheck — VTHacks - 14, placement unranked, data_to_decision, owner=consumer: Owner-operator truckers paste a load offer and get true net profit, better multi-load routes and a cash-flow check. <https://devpost.com/software/loadcheck>
  - Pay Pals — SwampHacks - XI, placement unranked, game_or_social, owner=consumer: College students join lobbies where Gemini proposes shared savings goals and friends wager favors and Solana tokens on outcomes. <https://devpost.com/software/project-c1nomzfei7a0>
  - Runway — SwampHacks - XII, placement unranked, data_to_decision, owner=sponsor_customers: Paycheck-to-paycheck bank customers get a 30-day balance forecast and quiet, consented cover from supporters before shortfalls. <https://devpost.com/software/runway-57dpic>
  - PayPark — DivHacks 2025, placement unranked, realtime_coordination, owner=consumer: Drivers pick a mapped parking spot, watch cost accrue live and pay the exact amount in RLUSD on XRPL. <https://devpost.com/software/paypark>
  - RentEscrow — DivHacks 2026, placement unranked, workflow_automation_agent, owner=consumer: NYC tenants and landlords share repair cases with photo evidence, AI summaries and a simulated rent escrow settling on XRPL Testnet. <https://devpost.com/software/rentescrow-nthfwb>
  - unsaid — DivHacks 2026, placement unranked, workflow_automation_agent, owner=consumer: Friend groups in New York plan dinner via private iMessage chats that negotiate budget, diet and venue and send a poll. <https://devpost.com/software/unsaid-zm8w5v>
  - OwlNudge — HackRice 15, placement unranked, education_feedback, owner=consumer: Unbanked and underbanked users chat with three Gemini advisor personas, take a quiz and get a dashboard without linking a bank. <https://devpost.com/software/owlnudge>
  - Swipe Coach — HackRice 15, placement unranked, data_to_decision, owner=consumer: Multi-card holders get a recommendation of which credit card to swipe per purchase, plus spending dashboards and a Gemini coach. <https://devpost.com/software/swipe-coach>
  - Larp City — HackRice 16, placement unranked, education_feedback, owner=consumer: Young adults learn personal finance by living a simulated life from age 22 to retirement, with an AI coach review. <https://devpost.com/software/temp-6yaocn>
  - TaskChain — MadHacks Fall 2024, placement unranked, other, owner=consumer: Students stake ETH on tasks with deadlines; stakes return on completion or go to a chosen charity. <https://devpost.com/software/taskchain>
  - Lease Saving Plan — ShellHacks 2024, placement unranked, data_to_decision, owner=consumer: Car-lease shoppers compute monthly lease and insurance costs and track down-payment savings in an English/Spanish desktop app. <https://devpost.com/software/lease-saving-plan>
  - SmartCards — ShellHacks 2024, placement unranked, docs_to_action, owner=sponsor_customers: Budgeting-app users upload receipt photos and get itemized categories plus investing and cashback suggestions. <https://devpost.com/software/smartcards-qxdusb>
  - Agent Zero — ShellHacks 2025, placement unranked, risk_detect_and_respond, owner=sponsor_internal_or_b2b: Finance and accounts-payable teams get an invoice reliability score from an orchestrator routing to specialist fraud agents. <https://devpost.com/software/agentzero-tnh9p3>
  - Pennywise — Technica 2024, placement unranked, data_to_decision, owner=consumer: Event planners get budget allocation, an AI advice chatbot and spending charts from a simple event-cost form. <https://devpost.com/software/pennywise-84p1il>
  - Personal Cart Roaster — Technica 2025, placement unranked, game_or_social, owner=consumer: Impulse online shoppers get a Gemini-written personalized roast of their Amazon cart, read aloud by ElevenLabs, to curb buying. <https://devpost.com/software/personal-cart-roaster>
  - Resale Radar — Technica 2025, placement unranked, data_to_decision, owner=consumer: Poshmark resellers get a recommended listing price from scraped sold data, outlier removal and graphs in a Java desktop app. <https://devpost.com/software/resale-radar>
  - Atlantis - The Long Night — Technica 2026, placement unranked, game_or_social, owner=consumer: People intimidated by personal finance play a pixel-art year-long game where every money move is a real Nessie record. <https://devpost.com/software/atlantis-the-long-night>
  - Treasure Dive — Technica 2026, placement unranked, data_to_decision, owner=consumer: Consumers connect a bank account and see open class-action settlements they may qualify for in a pixel-art chest. <https://devpost.com/software/treasure-dive>
  - Bread Bot — WEHack 2025, placement unranked, data_to_decision, owner=consumer: First-time investors get stock/REIT direction predictions, sentiment, a crypto-collateral P2P loan marketplace and a mistakes quiz. <https://devpost.com/software/money-makerz>
  - Kairos — WEHack 2025, placement unranked, risk_detect_and_respond, owner=sponsor_customers: Mid-sized banks and telecoms flag forged loan documents and scam calls using OCR, Gemini and Deepgram. <https://devpost.com/software/kairos-fnab7r>
  - Income Firewall — WiCHacks 2026, placement unranked, data_to_decision, owner=consumer: Freelancers and gig workers see their chance of hitting zero balance and get a savings rule backtested on history. <https://devpost.com/software/income-firewall>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: data_to_decision: 23 of 42 (55%); other: 3 of 42 (7%); education_feedback: 3 of 42 (7%); risk_detect_and_respond: 3 of 42 (7%); workflow_automation_agent: 3 of 42 (7%); game_or_social: 3 of 42 (7%); realtime_coordination: 2 of 42 (5%); voice_to_action: 1 of 42 (2%); docs_to_action: 1 of 42 (2%)
  - problem_owner: consumer: 32 of 42 (76%); sponsor_internal_or_b2b: 6 of 42 (14%); sponsor_customers: 4 of 42 (10%)
  - prompt_literalness: 0: 1 of 42 (2%); 1: 14 of 42 (33%); 2: 10 of 42 (24%); na: 17 of 42 (40%)
  - sponsor_removable: yes: 30 of 42 (71%); no: 12 of 42 (29%)
  - sponsor_features_used: median 0; 0: 23 of 42 (55%); 1: 17 of 42 (40%); 6: 1 of 42 (2%); 8: 1 of 42 (2%)
  - placement: unranked: 42 of 42 (100%); prize_kind: sponsor_domain: 32 of 42 (76%); sponsor_api_depth: 9 of 42 (21%); sponsor_open: 1 of 42 (2%)
- What won:
  - FINDING: Capital One winners across other events are mostly consumer-facing data-to-decision tools where Capital One tech was removable.
    SUPPORT: 30 of 42 (71%) (unweighted, sponsor_removable=yes); examples: SpendingWithSpendy (HackUTD 2025) <https://devpost.com/software/spendingwithspendy>, Localized (HackNC 2025) <https://devpost.com/software/localized>, I'd Rather Scroll (HackGT 12) <https://devpost.com/software/i-d-rather-scroll>
    COUNTEREXAMPLES: HR Audit (HackGT 12) <https://devpost.com/software/the-hr-audit>, BudgetBuddy (Bitcamp 2025) <https://devpost.com/software/budgetbuddy-3qvr78>, Drift (TAMUhack 2026) <https://devpost.com/software/pff>
    CONFIDENCE: medium (n>=12, share>=70%; capped at medium: analyst tags, placements mostly unpublished)
    TYPE: association
    IMPLICATION FOR US: Default to a consumer finance story on synthetic transactions; do not budget for a required API integration.
  - FINDING: A minority of Capital One awards (sponsor_api_depth prizes) did need the sponsor's API, and those were not removable.
    SUPPORT: api-depth prizes 9 of 42 (21%); of these, sponsor_removable=no 6 of 9 (67%); median sponsor_features_used among them 1; examples: BreakingPoint (HackTX 2026) <https://devpost.com/software/breakingpoint>, RxSolve (HackNC 2026) <https://devpost.com/software/rxsolve>, LoadCheck (VTHacks - 14) <https://devpost.com/software/loadcheck>
    COUNTEREXAMPLES: Velum (HackIllinois 2026) <https://devpost.com/software/velum>, RentEscrow (DivHacks 2026) <https://devpost.com/software/rentescrow-nthfwb>, unsaid (DivHacks 2026) <https://devpost.com/software/unsaid-zm8w5v>
    CONFIDENCE: low-medium (small subgroup)
    TYPE: association
    IMPLICATION FOR US: if a Capital One API/credit prize is announced, add the integration as a visible, live step; otherwise ignore it.
- Pitch angle (inference): Personal-finance coach, fraud/anomaly explainer or financial-inclusion tool for students, built on synthetic data with LLM explanations. Ask what the Switch Competition is.
- Integration depth rule (inference): Problem-fit by default; core integration only for an explicit API-depth prize.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

## Toyota Financial Services
- Tier: Gold
- What the sponsor asked: Challenge text NOT public [V]; no public API [brief tier table]. The brief calls 2024 'unknown'; the dataset has 3 HackUTD 2024 + 3 HackUTD 2025 winners (dataset wins).
- Prize structure: 2025: 1st $500, 2nd $350, 3rd $150 Amazon gift cards [V]. 2022/2023 Toyota prizes were JBL/SXM gear [V].
- Past winners in dataset: 6 awards across 2 events (HackUTD 2024 x3; HackUTD 2025 x3).
  - FUELICIENT — HackUTD 2024, placement 1, data_to_decision, owner=unknown: People analyzing Toyota fuel-efficiency data explore it in Streamlit and save modified datasets per account. <https://devpost.com/software/fuelicient>
  - KaizenDrive — HackUTD 2024, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Automotive engineers explore four years of Toyota car data through dashboards and a RAG chatbot without writing code. <https://devpost.com/software/project-ip7kgx0314sh>
  - Hingine — HackUTD 2025, placement unranked, education_feedback, owner=sponsor_customers: College students swipe through Toyota cars and complete finance lessons to unlock financing perks in a mobile app. <https://devpost.com/software/hingine>
  - Kachow — HackUTD 2025, placement unranked, data_to_decision, owner=sponsor_customers: Car buyers chat with a bot that shows true ownership costs and uses mock bank data to guide financing. <https://devpost.com/software/car-thing-1dsxyk>
  - Toyotron — HackUTD 2025, placement unranked, workflow_automation_agent, owner=sponsor_customers: Prospective Toyota buyers take a quiz, chat with agents, estimate trade-in and book test drives with emailed confirmations. <https://devpost.com/software/toyotron>
  - ToyoTrends — HackUTD 2024, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Toyota engineers chart and compare fuel efficiency and emissions across Toyota and competitor vehicles with a chatbot. <https://devpost.com/software/toyota-car-analytics-app>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: data_to_decision: 4 of 6 (67%); education_feedback: 1 of 6 (17%); workflow_automation_agent: 1 of 6 (17%)
  - problem_owner: sponsor_customers: 3 of 6 (50%); sponsor_internal_or_b2b: 2 of 6 (33%); unknown: 1 of 6 (17%)
  - prompt_literalness: na: 6 of 6 (100%)
  - sponsor_removable: yes: 4 of 6 (67%); no: 2 of 6 (33%)
  - sponsor_features_used: median 0; 0: 4 of 6 (67%); 1: 2 of 6 (33%)
  - placement: unranked: 5 of 6 (83%); 1: 1 of 6 (17%); prize_kind: sponsor_domain: 6 of 6 (100%)
- What won:
  - FINDING: Toyota winners lean data-to-decision (car-buying / cost-of-ownership) tools, with sponsor customers as the stated problem owner in half of them.
    SUPPORT: 4 of 6 (67%) (unweighted, pattern=data_to_decision); examples: FUELICIENT (HackUTD 2024) <https://devpost.com/software/fuelicient>, KaizenDrive (HackUTD 2024) <https://devpost.com/software/project-ip7kgx0314sh>, Kachow (HackUTD 2025) <https://devpost.com/software/car-thing-1dsxyk>
    COUNTEREXAMPLES: Hingine (HackUTD 2025) <https://devpost.com/software/hingine>, Toyotron (HackUTD 2025) <https://devpost.com/software/toyotron>
    CONFIDENCE: low (n<10; tags are analyst judgments)
    TYPE: association
    IMPLICATION FOR US: Frame a buyer-facing cost-transparency or lease-vs-buy tool; a gamified finance-lesson angle also appeared (Hingine).
- Pitch angle (inference): True cost of ownership with what-if APR, agentic first-time-buyer assistant, or a payment-hardship helper; show a before/after cost number on screen.
- Integration depth rule (inference): Problem-fit (no public Toyota API). Non-removable winners: (2 of 6 (33%)): see their lines before assuming zero integration.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

## State Farm
- Tier: Silver
- What the sponsor asked: Challenge text NOT public [V]. 2022 prompt: 'Use technology to create a creative solution to a problem facing the community' [V]; workshop then was serverless REST APIs on AWS [V].
- Prize structure: 2022: 34-inch LG Ultrawide / iPad / Beats Studio 3 [V]. 2026 not public.
- Past winners in dataset: 13 awards across 7 events (HackUTD 2025 x3; ShellHacks 2025 x3; Innovation Hacks 2.0 x2; ShellHacks 2024 x2; ShellHacks 2026 x1; SunHacks 2024 x1; ...).
  - MirrorAPI — HackUTD 2025, placement unranked, devtool, owner=sponsor_internal_or_b2b: Developers upload two API endpoints and get a field-level JSON diff, risk score and LLM-written migration report. <https://devpost.com/software/mirror-api>
  - qAPIbara — HackUTD 2025, placement unranked, devtool, owner=sponsor_internal_or_b2b: QA engineers diff two API versions, auto-generate tests and get AI explanations of regressions on dashboards. <https://devpost.com/software/in-progress-2awbie>
  - UpGuardian — HackUTD 2025, placement unranked, devtool, owner=unknown: Application developers detect breaking changes when moving to new API versions via deterministic diffs interpreted by a Nemotron agent. <https://devpost.com/software/upguard>
  - Dollar Dash — Innovation Hacks 2.0, placement unranked, game_or_social, owner=sponsor_customers: Students in classrooms trade four fictional stocks on phones as news moves prices, ending in a leaderboard. <https://devpost.com/software/dollar-dash>
  - Redreemer — Innovation Hacks 2.0, placement unranked, workflow_automation_agent, owner=sponsor_customers: Homeless and reentry people text one number to get local resources and a stability ladder, and caseworkers monitor progress. <https://devpost.com/software/redreemer>
  - FiveHacks — ShellHacks 2024, placement unranked, education_feedback, owner=sponsor_customers: College students read a static State Farm-themed insurance explainer website with an embedded quiz. <https://devpost.com/software/fivehacks>
  - Treasure Keepers — ShellHacks 2024, placement unranked, education_feedback, owner=consumer: First-generation and low-income students learn finance through fantasy-themed quizzes, a budget builder and AI character advisors. <https://devpost.com/software/treasure-keepers>
  - GreenLight — ShellHacks 2025, placement unranked, education_feedback, owner=consumer: Drivers upload dashcam footage to get Gemini analysis, a generated Three.js 3D replay of the incident and safety quizzes. <https://devpost.com/software/greenlight-idnv6o>
  - Next Step — ShellHacks 2025, placement unranked, education_feedback, owner=consumer: People learning insurance practice urgent auto, home or health scenarios with a voice agent and get scored 0 to 100. <https://devpost.com/software/next-step-cme06a>
  - The Rat Race — ShellHacks 2025, placement unranked, game_or_social, owner=consumer: Students learn insurance terms by playing a satirical branching office game as a rat intern with six endings. <https://devpost.com/software/the-rat-race>
  - Halo — ShellHacks 2026, placement unranked, sensor_to_alert_or_action, owner=consumer: Cyclists get a smart helmet that tracks vehicles approaching from behind and warns them by display, audio and haptics. <https://devpost.com/software/halo-1q59hf>
  - LockItUp — SunHacks 2024, placement unranked, sensor_to_alert_or_action, owner=consumer: ASU students unlock a QR-code lock built into campus bike stands instead of carrying their own lock. <https://devpost.com/software/lockitup>
  - Crises.ai — SunHacks 2025, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Insurance claims and field teams see live disaster feeds on one map with Gemini claim forecasts and adjuster estimates. <https://devpost.com/software/crises-ai>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: education_feedback: 4 of 13 (31%); devtool: 3 of 13 (23%); game_or_social: 2 of 13 (15%); sensor_to_alert_or_action: 2 of 13 (15%); workflow_automation_agent: 1 of 13 (8%); data_to_decision: 1 of 13 (8%)
  - problem_owner: consumer: 6 of 13 (46%); sponsor_internal_or_b2b: 3 of 13 (23%); sponsor_customers: 3 of 13 (23%); unknown: 1 of 13 (8%)
  - prompt_literalness: 0: 1 of 13 (8%); 1: 3 of 13 (23%); 2: 5 of 13 (38%); na: 4 of 13 (31%)
  - sponsor_removable: yes: 13 of 13 (100%)
  - sponsor_features_used: median 0; 0: 13 of 13 (100%)
  - placement: unranked: 13 of 13 (100%); prize_kind: sponsor_domain: 13 of 13 (100%)
- What won:
  - FINDING: State Farm winners show no dominant pattern and none needed State Farm tech (removable: 13 of 13 (100%)).
    SUPPORT: 13 of 13 (100%) (unweighted, sponsor_removable=yes); examples: MirrorAPI (HackUTD 2025) <https://devpost.com/software/mirror-api>, qAPIbara (HackUTD 2025) <https://devpost.com/software/in-progress-2awbie>, UpGuardian (HackUTD 2025) <https://devpost.com/software/upguard>
    COUNTEREXAMPLES: none
    CONFIDENCE: medium (n>=12, share>=70%; capped at medium: analyst tags, placements mostly unpublished)
    TYPE: association
    IMPLICATION FOR US: Open-ended, community-problem prompts: pick by problem relevance (disaster readiness, driving safety, financial resilience), not by sponsor tooling.
- Pitch angle (inference): Disaster-preparedness / claims-readiness, teen-driver coaching or financial-resilience planner. Make the community problem and a measurable benefit obvious.
- Integration depth rule (inference): Problem-only depth.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

## CBRE
- Tier: Silver
- What the sponsor asked: Challenge text NOT public [V]. Past challenges shipped a PDF statement + sample/quarterly data [V]. 2025 challenge 'Lost in the Pages' (chatbot over contracts/reports) [V]. 2022: AI/ML for customer experience from social media/contact centres/surveys [V]. CBRE's own Innovate 2026 rubric: business impact, technical innovation, scalability, market readiness, execution [V]. The brief cites a 2024 CBRE winner 'EcoManage' that is NOT in the dataset (dataset used).
- Prize structure: 2022: $125/$75/$50 Amazon gift cards [V]. 2026 not public.
- Past winners in dataset: 17 awards across 6 events (UXperience 2025 x3; HackUTD 2024 x3; HackUTD 2025 x3; HackUNT 2024 x3; WEHack 2025 x3; WEHack 2026 x2).
  - Aero — UXperience 2025, placement 1, docs_to_action, owner=sponsor_internal_or_b2b: UX professionals on hybrid teams get one assistant that gathers scattered work items and summarizes threads into next steps. <https://devpost.com/software/aero-h038lg>
  - Integra — UXperience 2025, placement 2, other, owner=sponsor_customers: Managers get wellbeing insights, gamified goals and a virtual workspace in a Figma concept to reduce team burnout. <https://devpost.com/software/workplace-wellbeing>
  - Mosaic — UXperience 2025, placement 3, other, owner=sponsor_internal_or_b2b: Hybrid and remote teams use a Figma prototype where finished tasks and habits tint tiles to reveal a picture. <https://devpost.com/software/mosaic-q402zy>
  - Greenify — HackUTD 2024, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Office property managers use an emissions calculator, GPT-4 advice chatbot and a CBRE location emissions map. <https://devpost.com/software/greenwise-y6o4bu>
  - Pact — HackUTD 2025, placement unranked, docs_to_action, owner=sponsor_internal_or_b2b: Vendors and clients draft contracts with AI help, approve them in multi-party workflows and anchor hashes on Solana. <https://devpost.com/software/autotract>
  - TrustEstate AI — HackUTD 2025, placement unranked, data_to_decision, owner=consumer: Home buyers browse a map of properties where Gemini fact-checks each listing against live search and assigns a trust score. <https://devpost.com/software/cbre-project>
  - Eco Fast Track — HackUTD 2024, placement unranked, sensor_to_alert_or_action, owner=sponsor_internal_or_b2b: Property managers and tenants get usage graphs, AI saving tips and email alerts from a homemade Arduino water gauge. <https://devpost.com/software/apartment-monitoring>
  - Cura — HackUTD 2025, placement unranked, data_to_decision, owner=sponsor_customers: Beginner and investor buyers of commercial property get agent-generated forecasts, pros/cons and comparisons in a dashboard. <https://devpost.com/software/tbd-58ftpr>
  - EcoVerse — HackUTD 2024, placement unranked, spatial_ar, owner=sponsor_internal_or_b2b: Property managers explore a VR office replica, view synthetic energy/water data, chat with an AI avatar and feel changes via haptic gloves. <https://devpost.com/software/ecoverse-5dczmp>
  - Meet+ — HackUNT 2024, placement unranked, docs_to_action, owner=sponsor_internal_or_b2b: Meeting attendees paste a transcript and get a summary, action items and calendar-style event details from Gemini. <https://devpost.com/software/meet-gqybo1>
  - Propertunity — HackUNT 2024, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Property managers and tenants use a portal where a Gemini chatbot files tickets and ML forecasts maintenance cost. <https://devpost.com/software/propertunity>
  - UtiliTrack — HackUNT 2024, placement unranked, sensor_to_alert_or_action, owner=sponsor_internal_or_b2b: Small business owners monitor energy use from sensors and let automation schedule HVAC and maintenance to cut waste. <https://devpost.com/software/utilitrack>
  - Personal Finance & Smart Investment App — WEHack 2025, placement unranked, data_to_decision, owner=consumer: General savers plan monthly budgets, goals and a stock portfolio with return and risk estimates and Gemini guidance. <https://devpost.com/software/money-app-z4w7r5>
  - Stock Lock — WEHack 2025, placement unranked, data_to_decision, owner=consumer: Retail investors enter a ticker and get LSTM price predictions plus RAG-generated market insights in a Streamlit app. <https://devpost.com/software/investai>
  - TrendPulse — WEHack 2025, placement unranked, data_to_decision, owner=consumer: Stock and crypto traders get a dashboard scoring Twitter and Reddit sentiment into trend and risk indexes beside market data. <https://devpost.com/software/trendpulse>
  - Miro — WEHack 2026, placement unranked, docs_to_action, owner=sponsor_internal_or_b2b: Commercial property managers get a daily ranked briefing, risk heatmap and Q&A built from their Gmail, Sheets and notes. <https://devpost.com/software/miro-rzbevu>
  - Temp — WEHack 2026, placement unranked, docs_to_action, owner=sponsor_internal_or_b2b: A local LLM agent for property managers retrieves tenant records using salience scores that decay and prune. <https://devpost.com/software/temp-5aht81>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: data_to_decision: 7 of 17 (41%); docs_to_action: 5 of 17 (29%); other: 2 of 17 (12%); sensor_to_alert_or_action: 2 of 17 (12%); spatial_ar: 1 of 17 (6%)
  - problem_owner: sponsor_internal_or_b2b: 11 of 17 (65%); consumer: 4 of 17 (24%); sponsor_customers: 2 of 17 (12%)
  - prompt_literalness: 0: 1 of 17 (6%); 1: 4 of 17 (24%); 2: 5 of 17 (29%); na: 7 of 17 (41%)
  - sponsor_removable: yes: 16 of 17 (94%); no: 1 of 17 (6%)
  - sponsor_features_used: median 0; 0: 16 of 17 (94%); 1: 1 of 17 (6%)
  - placement: unranked: 14 of 17 (82%); 1: 1 of 17 (6%); 2: 1 of 17 (6%); 3: 1 of 17 (6%); prize_kind: sponsor_domain: 17 of 17 (100%)
- What won:
  - FINDING: CBRE winners are overwhelmingly data-to-decision or docs-to-action tools for sponsor-internal/B2B users, and CBRE tech was never needed.
    SUPPORT: 12 of 17 (71%) (unweighted, pattern=data_to_decision/docs_to_action); examples: Aero (UXperience 2025) <https://devpost.com/software/aero-h038lg>, Greenify (HackUTD 2024) <https://devpost.com/software/greenwise-y6o4bu>, Pact (HackUTD 2025) <https://devpost.com/software/autotract>
    COUNTEREXAMPLES: Integra (UXperience 2025) <https://devpost.com/software/workplace-wellbeing>, Mosaic (UXperience 2025) <https://devpost.com/software/mosaic-q402zy>, Eco Fast Track (HackUTD 2024) <https://devpost.com/software/apartment-monitoring>
    CONFIDENCE: medium (n>=12, share>=70%; capped at medium: analyst tags, placements mostly unpublished)
    TYPE: association
    IMPLICATION FOR US: Prepare a documents/data-to-structured-decision frame (lease Q&A with citations, market briefing, energy copilot) so it is ready when the prompt drops.
  - FINDING: CBRE winners did not use any CBRE-provided feature (0 features used: 16 of 17 (94%)), so depth is problem-fit.
    SUPPORT: 16 of 17 (94%) (unweighted, sponsor_features_used=0); examples: Aero (UXperience 2025) <https://devpost.com/software/aero-h038lg>, Integra (UXperience 2025) <https://devpost.com/software/workplace-wellbeing>, Mosaic (UXperience 2025) <https://devpost.com/software/mosaic-q402zy>
    COUNTEREXAMPLES: Greenify (HackUTD 2024) <https://devpost.com/software/greenwise-y6o4bu>
    CONFIDENCE: medium (n>=12, share>=70%; capped at medium: analyst tags, placements mostly unpublished)
    TYPE: association
    IMPLICATION FOR US: Use the provided dataset/PDF as the input and show cited, confidence-marked output; no integration work.
- Pitch angle (inference): Cited answers with confidence levels, structured extraction tables, and a business-impact line (CBRE's own rubric: business impact, innovation, scalability, market readiness, execution).
- Integration depth rule (inference): Problem-only depth; spend the saved time on correctness and sourcing.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

## EOG Resources — LOW N
- Tier: Gold
- What the sponsor asked: Challenge text NOT public [V]; EOG Workshop Sat 5:15pm [V]. 2022 prompt: web/mobile/analysis app on drilling data to improve speed, cost, efficiency [V]. Expect a sponsor-provided dataset [U].
- Prize structure: 2022: 2 winners (DJI Mini SE / Skullcandy Crusher Evo) [V]. 2026 not public.
- Past winners in dataset: 4 awards across 2 events (HackUTD 2025 x2; HackUTD 2024 x2).
  - Enchantress — HackUTD 2025, placement unranked, risk_detect_and_respond, owner=sponsor_internal_or_b2b: Operators monitoring resource flows see a gamified cauldron map that flags transport tickets that disagree with measured drains. <https://devpost.com/software/enchantress-w2li90>
  - PipeBrAIns — HackUTD 2024, placement unranked, risk_detect_and_respond, owner=sponsor_internal_or_b2b: Pipeline owners get a dashboard predicting hydrate blockages with a random-forest model, live alerts and email notices. <https://devpost.com/software/pipebrains>
  - PoyoLabs — HackUTD 2025, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Gamers and operators explore potion cauldron collection, depletion and theft analytics in a pixel-art dashboard with a chatbot. <https://devpost.com/software/poyolabs-47n0fz>
  - DHy-n0 — HackUTD 2024, placement unranked, risk_detect_and_respond, owner=sponsor_internal_or_b2b: Oil and gas lease operators upload well data and see charts flagging anomalies that may signal hydrate buildup. <https://devpost.com/software/dhy-n0>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: risk_detect_and_respond: 3 of 4 (75%); data_to_decision: 1 of 4 (25%)
  - problem_owner: sponsor_internal_or_b2b: 4 of 4 (100%)
  - prompt_literalness: 2: 1 of 4 (25%); na: 3 of 4 (75%)
  - sponsor_removable: yes: 3 of 4 (75%); no: 1 of 4 (25%)
  - sponsor_features_used: median 0; 0: 3 of 4 (75%); 1: 1 of 4 (25%)
  - placement: unranked: 4 of 4 (100%); prize_kind: sponsor_domain: 4 of 4 (100%)
- What won:
  - FINDING: EOG winners are risk-detect-and-respond tools for sponsor-internal (operations) users; LOW N, treat as an anecdote.
    SUPPORT: 3 of 4 (75%) (unweighted, pattern=risk_detect_and_respond); examples: Enchantress (HackUTD 2025) <https://devpost.com/software/enchantress-w2li90>, PipeBrAIns (HackUTD 2024) <https://devpost.com/software/pipebrains>, DHy-n0 (HackUTD 2024) <https://devpost.com/software/dhy-n0>
    COUNTEREXAMPLES: PoyoLabs (HackUTD 2025) <https://devpost.com/software/poyolabs-47n0fz>
    CONFIDENCE: low (n<10; tags are analyst judgments)
    TYPE: association
    IMPLICATION FOR US: If a drilling/operations dataset is provided, build an anomaly/alert tool with a cost-or-time-saved number; otherwise skip.
- Pitch angle (inference): ROP/anomaly detector with cost-saved estimate, or a mobile field dashboard with alerts (the 'control room in your pocket' framing).
- Integration depth rule (inference): Problem-fit on the provided dataset; low n, so no depth rule is supported by the data.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

## NVIDIA
- Tier: Silver
- What the sponsor asked: No challenge or prize public; no NVIDIA event on the 2026 schedule [V]. Free Nemotron endpoints on build.nvidia.com [V]. Do not assume a prize [brief].
- Prize structure: Unknown for HackUTD 2026 [V absence].
- Past winners in dataset: 21 awards across 8 events (TreeHacks 2026 x4; HackUTD 2025 x3; TreeHacks 2025 x3; 2026 x3; Knight Hacks IX (2025) x3; SteelHacks XIII (2026) x3; ...).
  - Alchemetrics — HackUTD 2025, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Potion factory operators see agents detect drains, match tickets, flag discrepancies and plan collection routes on a dashboard. <https://devpost.com/software/abc-xapnio>
  - DataDriver — HackUTD 2025, placement unranked, workflow_automation_agent, owner=sponsor_internal_or_b2b: Data center technicians get an agent that plans maintenance steps, checks inventory, runs tools and replans on issues. <https://devpost.com/software/datadriver>
  - Toyotron — HackUTD 2025, placement unranked, workflow_automation_agent, owner=unknown: Prospective Toyota buyers take a quiz, chat with agents, estimate trade-in and book test drives with emailed confirmations. <https://devpost.com/software/toyotron>
  - Portable Braille — TreeHacks 2025, placement unranked, translate_between_people_or_systems, owner=consumer: Pocket refreshable Braille device syncing with a phone, plus glasses-to-Jetson facial expression readout for blind and deaf-blind users. <https://devpost.com/software/portable-braille-cdq8v5>
  - Ranger — TreeHacks 2025, placement unranked, sensor_to_alert_or_action, owner=consumer: Deaf and hard-of-hearing wearers see sound direction icons and live captions in a Quest AR view from a mic-array hat. <https://devpost.com/software/ranger-6jkv5s>
  - WiiWork — TreeHacks 2025, placement unranked, workflow_automation_agent, owner=unknown: Web developers wrap React components so a voice-driven multi-model agent can see and operate the page with a virtual cursor. <https://devpost.com/software/wiiwork-8u1x62>
  - CalTrack — TreeHacks 2026, placement unranked, risk_detect_and_respond, owner=consumer: Emergency managers see wildfire risk and population density on a map while agents triage 911 calls into addresses and medical details. <https://devpost.com/software/caltrack-i0pq3n>
  - Detour — TreeHacks 2026, placement unranked, risk_detect_and_respond, owner=sponsor_internal_or_b2b: Satellite operators screen live debris conjunctions and get fuel-constrained avoidance burns from on-board LLM agents. <https://devpost.com/software/detour-64kpds>
  - Sprout — TreeHacks 2026, placement unranked, sensor_to_alert_or_action, owner=consumer: A gantry robot garden uses a Jetson Nano camera to identify plant species and health, then waters each plant precisely. <https://devpost.com/software/greenguardian-microfarm>
  - TORQ — TreeHacks 2026, placement unranked, sensor_to_alert_or_action, owner=consumer: Owners of older cars retrofit them to self-drive, with riders dispatching rides and seeing explanations in an iOS app. <https://devpost.com/software/torq>
  - ClawForge — 2026, placement unranked, workflow_automation_agent, owner=sponsor_customers: Small-business owners describe an agent in plain English and get a visual blueprint with safety gates, run in a sandbox. <https://devpost.com/software/clawforge>
  - FactoryMind — 2026, placement unranked, realtime_coordination, owner=sponsor_internal_or_b2b: Factory operators watch a Nemotron leader dispatch worker robots in a 3D warehouse twin under allow/deny policy checks. <https://devpost.com/software/factorymind>
  - MonkeyClaw — 2026, placement unranked, risk_detect_and_respond, owner=sponsor_customers: Agent-platform security teams run an autonomous red, blue and purple loop that attacks NemoClaw sandboxes and verifies patches and telemetry. <https://devpost.com/software/monkeyclaw>
  - TIDAL WAVE — DataHacks 2026, placement unranked, data_to_decision, owner=consumer: Non-expert would-be policymakers type an environmental policy and watch species agents simulate a coastal ecosystem over years. <https://devpost.com/software/tidal-wave-ump7f9>
  - Farsight — Knight Hacks IX (2025), placement unranked, realtime_coordination, owner=unknown: Search-and-rescue responders drive a Jetson rover from a VR headset, detect people, and review a walkable 3D room map. <https://devpost.com/software/farsight-t4qyli>
  - Fireline — Knight Hacks IX (2025), placement unranked, risk_detect_and_respond, owner=consumer: Wildfire crews get tree-mounted Jetson cameras that detect smoke and send tiny satellite alerts to a map console. <https://devpost.com/software/fireline-764nir>
  - Permanence — Knight Hacks IX (2025), placement unranked, vision_to_assist, owner=unknown: Robotics builders get a Jetson rover with persistent 3D object memory that tracks hidden balls and drives to requested targets. <https://devpost.com/software/permanence>
  - VL-ADK — ShellHacks 2025, placement unranked, workflow_automation_agent, owner=consumer: Students and hobbyists type requests to Google ADK agents that drive a Jetson-powered JetBot using camera detections. <https://devpost.com/software/vl-adk>
  - Heard! — SteelHacks XIII (2026), placement unranked, realtime_coordination, owner=sponsor_internal_or_b2b: Working teams get an ambient meeting agent that sorts ideas onto a live board, researches questions and speaks up when useful. <https://devpost.com/software/heard-puhs0f>
  - SurrealEstate — SteelHacks XIII (2026), placement unranked, data_to_decision, owner=consumer: Remote home buyers paste a Zillow link and get an agent-guided room tour with sourced neighborhood research. <https://devpost.com/software/surrealestate>
  - Weave — SteelHacks XIII (2026), placement unranked, translate_between_people_or_systems, owner=consumer: Older adults and helping relatives co-browse one site, each with a personalized accessible view and an AI guide pointing where to click. <https://devpost.com/software/weave-z8t1i0>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: workflow_automation_agent: 5 of 21 (24%); risk_detect_and_respond: 4 of 21 (19%); data_to_decision: 3 of 21 (14%); sensor_to_alert_or_action: 3 of 21 (14%); realtime_coordination: 3 of 21 (14%); translate_between_people_or_systems: 2 of 21 (10%); vision_to_assist: 1 of 21 (5%)
  - problem_owner: consumer: 10 of 21 (48%); sponsor_internal_or_b2b: 5 of 21 (24%); unknown: 4 of 21 (19%); sponsor_customers: 2 of 21 (10%)
  - prompt_literalness: 0: 2 of 21 (10%); 1: 4 of 21 (19%); 2: 11 of 21 (52%); na: 4 of 21 (19%)
  - sponsor_removable: no: 18 of 21 (86%); yes: 3 of 21 (14%)
  - sponsor_features_used: median 2; 1: 8 of 21 (38%); 2: 8 of 21 (38%); 3: 2 of 21 (10%); 4: 2 of 21 (10%); 5: 1 of 21 (5%)
  - placement: unranked: 21 of 21 (100%); prize_kind: sponsor_open: 11 of 21 (52%); sponsor_api_depth: 7 of 21 (33%); sponsor_domain: 3 of 21 (14%)
- What won:
  - FINDING: NVIDIA-prize winners mostly could not remove NVIDIA tech, and most were multi-step agents.
    SUPPORT: 18 of 21 (86%) (unweighted, sponsor_removable=no); examples: Alchemetrics (HackUTD 2025) <https://devpost.com/software/abc-xapnio>, DataDriver (HackUTD 2025) <https://devpost.com/software/datadriver>, Toyotron (HackUTD 2025) <https://devpost.com/software/toyotron>
    COUNTEREXAMPLES: Portable Braille (TreeHacks 2025) <https://devpost.com/software/portable-braille-cdq8v5>, WiiWork (TreeHacks 2025) <https://devpost.com/software/wiiwork-8u1x62>, TIDAL WAVE (DataHacks 2026) <https://devpost.com/software/tidal-wave-ump7f9>
    CONFIDENCE: medium (n>=12, share>=70%; capped at medium: analyst tags, placements mostly unpublished)
    TYPE: association
    IMPLICATION FOR US: If NVIDIA announces a track, make Nemotron/NIM the working core (not a logo) and show it live.
  - FINDING: NVIDIA-prize winners are mostly agentic_multistep systems.
    SUPPORT: 14 of 21 (67%) (unweighted, ai_role=agentic_multistep); examples: Alchemetrics (HackUTD 2025) <https://devpost.com/software/abc-xapnio>, DataDriver (HackUTD 2025) <https://devpost.com/software/datadriver>, Toyotron (HackUTD 2025) <https://devpost.com/software/toyotron>
    COUNTEREXAMPLES: Portable Braille (TreeHacks 2025) <https://devpost.com/software/portable-braille-cdq8v5>, Ranger (TreeHacks 2025) <https://devpost.com/software/ranger-6jkv5s>, Sprout (TreeHacks 2026) <https://devpost.com/software/greenguardian-microfarm>
    CONFIDENCE: medium-low (moderate n or share; analyst tags)
    TYPE: association
    IMPLICATION FOR US: Build a visible multi-step tool-calling flow; median sponsor_features_used in the dataset is 2.
- Pitch angle (inference): Tool-calling agent on Nemotron with an eval/guardrail story, a vision-language document app, or a model-routing latency/cost tool. Note the 2025 NVIDIA track was reportedly crowded (100+ entries, unverified, spec 0.2).
- Integration depth rule (inference): Core integration, 1-2 NVIDIA features minimum (median 2), shown in the demo.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

## NMC2
- Tier: Gold (identity assumed = NorthMark Compute & Cloud, low confidence)
- What the sponsor asked: Challenge text NOT public [V]; NMC workshop Sat 4:20pm ECSW 1.365 [V]. 2025 challenge statement not public on Devpost [V]. The brief's NMC-to-winner mapping is [U] inference.
- Prize structure: 2025 (Northmark): 1st Nintendo Switch 2, 2nd Sony WH-1000XM5, 3rd DJI Tello [V]. 2026 not public.
- Past winners in dataset: 6 awards across 2 events (TAMUhack 2026 x3; HackUTD 2025 x3).
  - Constellation — TAMUhack 2026, placement 1, workflow_automation_agent, owner=sponsor_customers: Researchers new to HPC describe a goal and an agent builds a visual dataflow graph that runs on AWS Batch. <https://devpost.com/software/constellation-qcb483>
  - Cinder Control — TAMUhack 2026, placement 2, data_to_decision, owner=consumer: First responders and residents type or speak fire conditions to see 96-hour spread, impacted infrastructure and evacuation routes. <https://devpost.com/software/fsim>
  - PocketPlay — TAMUhack 2026, placement 3, data_to_decision, owner=sponsor_internal_or_b2b: Coaches, fans and analysts pick offensive and defensive schemes, simulate plays with an ML model and get AI critique. <https://devpost.com/software/pocketplay>
  - TaskFlow — HackUTD 2025, placement unranked, realtime_coordination, owner=sponsor_internal_or_b2b: Datacenter technicians and engineers get a ticket checklist app, a location dashboard and an AR pointer app to speed up tickets. <https://devpost.com/software/d-68uye4>
  - DataDriver — HackUTD 2025, placement unranked, workflow_automation_agent, owner=sponsor_internal_or_b2b: Data center technicians get an agent that plans maintenance steps, checks inventory, runs tools and replans on issues. <https://devpost.com/software/datadriver>
  - DCDaddy — HackUTD 2025, placement unranked, workflow_automation_agent, owner=sponsor_internal_or_b2b: Data center technicians and admins get auto-ticketing from email/Slack, health-aware floor routing, inventory forecasts and a device assistant. <https://devpost.com/software/fun-dashboard>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: workflow_automation_agent: 3 of 6 (50%); data_to_decision: 2 of 6 (33%); realtime_coordination: 1 of 6 (17%)
  - problem_owner: sponsor_internal_or_b2b: 4 of 6 (67%); sponsor_customers: 1 of 6 (17%); consumer: 1 of 6 (17%)
  - prompt_literalness: 1: 2 of 6 (33%); 2: 2 of 6 (33%); na: 2 of 6 (33%)
  - sponsor_removable: yes: 6 of 6 (100%)
  - sponsor_features_used: median 0; 0: 6 of 6 (100%)
  - placement: unranked: 3 of 6 (50%); 1: 1 of 6 (17%); 2: 1 of 6 (17%); 3: 1 of 6 (17%); prize_kind: sponsor_domain: 6 of 6 (100%)
- What won:
  - FINDING: NMC2-tagged awards are workflow-automation agents or data tools for sponsor-internal users; the dataset has only a handful of rows (TAMUhack 2026 has the only ranked ones), so evidence is thin.
    SUPPORT: 6 of 6 (100%) (unweighted, sponsor_removable=yes); examples: Constellation (TAMUhack 2026) <https://devpost.com/software/constellation-qcb483>, Cinder Control (TAMUhack 2026) <https://devpost.com/software/fsim>, PocketPlay (TAMUhack 2026) <https://devpost.com/software/pocketplay>
    COUNTEREXAMPLES: none
    CONFIDENCE: low (n<10; tags are analyst judgments)
    TYPE: association
    IMPLICATION FOR US: Datacenter/AI-ops framing (technician work orders, GPU/power dashboards) is the evidence-backed lane; confirm identity at the NMC workshop first.
- Pitch angle (inference): Datacenter ops copilot (work-order triage, runbook RAG), GPU workload/power visualiser, or an efficient-inference demo with a benchmark view.
- Integration depth rule (inference): Problem-fit (removable: 6 of 6 (100%)). The brief's mapping of 2025 winners to NMC is itself inferred.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

## 8090 AI — [brief only] no dataset winners
- Tier: Platinum ("8090 Solutions" on the site)
- What the sponsor asked: Challenge text and prizes NOT public [V]; no Devpost page found [V absence]. Company assumed = 8090 Solutions, Inc. (Software Factory: requirements -> blueprints -> work orders -> tests; agents via MCP) [V for identity/site name]. Hackathon access likely needs sponsor-provided seats/credits [U].
- Past winners in dataset: 0 of 0 (no rows in Q13_sponsor_card_rows.csv). Counts, findings: not available.
- Pitch angle (inference): [inference] Show requirements-to-tests traceability for a regulated-industry or legacy-modernisation problem; use their MCP workflow only if the booth confirms credits. Brief ideas: legacy-app modernisation, feedback-to-work-order loop, drift/compliance dashboard.
- Integration depth rule (inference): [inference] No dataset evidence for a depth rule. Default to genuine, demo-visible use of their workflow if (and only if) access is confirmed; otherwise treat as problem-fit only.
- Source: brief only (`06_hackutd_2026_sponsors/`); Q13_sponsor_card_rows.csv has 0 rows for this sponsor.

## Niantic Spatial — [brief only] no dataset winners
- Tier: Bronze
- What the sponsor asked: Challenge text and prizes NOT public; no Devpost/MLH listing found [V absence]. Tools: Niantic Spatial SDK (VPS localisation, anchors; Unity/Swift/Kotlin, no web), Scaniverse [V]. 8th Wall is being shut down: do not build on it [V]. Its own contests judged creativity, innovation, technical excellence [V].
- Past winners in dataset: 0 of 0 (no rows in Q13_sponsor_card_rows.csv). Counts, findings: not available.
- Pitch angle (inference): [inference] A real place scanned with Scaniverse and localised with VPS (e.g. campus wayfinding or facility-inspection anchors), shown live at the station; enterprise/physical-AI framing over a games gimmick.
- Integration depth rule (inference): [inference] If entered, core use of VPS/Scaniverse must be visible in the demo; needs a mobile/Unity build, so check team skills before choosing.
- Source: brief only (`06_hackutd_2026_sponsors/`); Q13_sponsor_card_rows.csv has 0 rows for this sponsor.

## Spacetime
- Tier: Silver
- What the sponsor asked: Challenge text NOT public [V]; hosts a 'Bot Tournament' Sat 10:45pm (format unknown) [V]. Company identity unconfirmed: spec 0.2 assumes SpacetimeDB (Clockwork Labs) [U].
- Prize structure: Unknown; no HackUTD history found [U].
- Past winners in dataset: 12 awards across 2 events (Cal Hacks 13.0 (2026) x9; MHacks 2026 x3).
  - Bandit - The only band you need — Cal Hacks 13.0 (2026), placement unranked, realtime_coordination, owner=consumer: Festival attendees, medics and organizers use ESP32 wristbands for crowd density, fall alerts, insurance claims and post-event recaps. <https://devpost.com/software/bandit-the-only-band-you-need>
  - Ender's Bench — Cal Hacks 13.0 (2026), placement unranked, data_to_decision, owner=unknown: AI evaluators watch models in a live survival world and a finance desk to see if they keep policy under pressure. <https://devpost.com/software/ender-s-bench>
  - GeonosisAI — Cal Hacks 13.0 (2026), placement unranked, workflow_automation_agent, owner=sponsor_internal_or_b2b: Robotics teams file a reliability ticket and agents diagnose failures, buy phone-collected demos, fine-tune a policy and re-evaluate. <https://devpost.com/software/robofactory>
  - Luyten — Cal Hacks 13.0 (2026), placement unranked, workflow_automation_agent, owner=sponsor_internal_or_b2b: Startup CFOs run month-end close with agents that only propose, critiqued by a cross-vendor Red Team, confirmed before posting. <https://devpost.com/software/cafoo>
  - Orkio — Cal Hacks 13.0 (2026), placement unranked, workflow_automation_agent, owner=sponsor_customers: Developers running separate AI coding agents get shared intentions, wip snapshots and automated integration conflict repair. <https://devpost.com/software/gehub>
  - Pacioli — Cal Hacks 13.0 (2026), placement unranked, workflow_automation_agent, owner=sponsor_internal_or_b2b: Small-business owners get a collaborative canvas where a Bookkeeper agent categorizes transactions and asks only about uncertain items. <https://devpost.com/software/pacioli>
  - Rally — Cal Hacks 13.0 (2026), placement unranked, game_or_social, owner=consumer: Casual players use a phone as a racket and a laptop as a 3D court for online badminton refereed by SpacetimeDB. <https://devpost.com/software/locomotion-5i4gzy>
  - skyFall — Cal Hacks 13.0 (2026), placement unranked, data_to_decision, owner=consumer: The public gets a live 3D globe forecasting satellite re-entry times and surviving debris using GPU Monte Carlo physics. <https://devpost.com/software/skyfall-uca4i9>
  - Vouch — Cal Hacks 13.0 (2026), placement unranked, risk_detect_and_respond, owner=sponsor_customers: Online shoppers film damaged items and merchants get an AI-investigated case packet plus a portable trust score. <https://devpost.com/software/vouch-7i3bft>
  - CoClip — MHacks 2026, placement unranked, realtime_coordination, owner=consumer: Video editors and teams co-edit one timeline in real time with each other and a Gemini assistant. <https://devpost.com/software/coclip>
  - scalpal. — MHacks 2026, placement unranked, education_feedback, owner=consumer: Surgical residents practice a full appendectomy case in VR with voice patient and AI coach, while motions train robots. <https://devpost.com/software/scalpal>
  - Traycer: Food-waste Intelligence — MHacks 2026, placement unranked, data_to_decision, owner=sponsor_internal_or_b2b: Cafeteria operators see per-food waste from tray cameras and test menu changes in a simulated cafeteria. <https://devpost.com/software/traycer-ai-food-waste-intelligence>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: workflow_automation_agent: 4 of 12 (33%); data_to_decision: 3 of 12 (25%); realtime_coordination: 2 of 12 (17%); game_or_social: 1 of 12 (8%); risk_detect_and_respond: 1 of 12 (8%); education_feedback: 1 of 12 (8%)
  - problem_owner: consumer: 5 of 12 (42%); sponsor_internal_or_b2b: 4 of 12 (33%); sponsor_customers: 2 of 12 (17%); unknown: 1 of 12 (8%)
  - prompt_literalness: 2: 9 of 12 (75%); na: 3 of 12 (25%)
  - sponsor_removable: no: 12 of 12 (100%)
  - sponsor_features_used: median 2; 1: 6 of 12 (50%); 3: 2 of 12 (17%); 4: 4 of 12 (33%)
  - placement: unranked: 12 of 12 (100%); prize_kind: sponsor_api_depth: 12 of 12 (100%)
- What won:
  - FINDING: Every Spacetime award in the dataset used Spacetime as the core backend (sponsor_removable no: 12 of 12 (100%)).
    SUPPORT: 12 of 12 (100%) (unweighted, sponsor_removable=no); examples: Bandit - The only band you need (Cal Hacks 13.0 (2026)) <https://devpost.com/software/bandit-the-only-band-you-need>, Ender's Bench (Cal Hacks 13.0 (2026)) <https://devpost.com/software/ender-s-bench>, GeonosisAI (Cal Hacks 13.0 (2026)) <https://devpost.com/software/robofactory>
    COUNTEREXAMPLES: none
    CONFIDENCE: medium (n>=12, share>=70%; capped at medium: analyst tags, placements mostly unpublished)
    TYPE: association
    IMPLICATION FOR US: Enter only if the team builds on the sponsor's database/runtime from the start; median sponsor_features_used is 2, and 6 of 12 (50%) used only one feature, so one deep use is the floor.
- Pitch angle (inference): A bot/agent for the tournament game API, a self-play tuning harness, or a spectator/replay dashboard. Get the tournament spec early. Identity of the 2026 sponsor is unconfirmed.
- Integration depth rule (inference): Core integration is required (non-removable: 12 of 12 (100%)); do not enter as an afterthought.
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

## Axxess — [brief only] no dataset winners
- Tier: Bronze (brief assumes "Axess" = Axxess, Dallas home-health software)
- What the sponsor asked: Challenge text and prizes NOT public; no Axxess workshop on the Nov 7 schedule [V]. Axxess ran its own healthcare hackathon at UTD Feb 21-22, 2026 (no prizes/challenge text on the page) [V]. API access is negotiated, no self-serve sandbox [third-party claim, U]: expect synthetic data.
- Past winners in dataset: 0 of 0 (no rows in Q13_sponsor_card_rows.csv). Counts, findings: not available.
- Pitch angle (inference): [inference] Clinician/agency-admin workflow tool on synthetic data (voice-to-visit-note with missing-field flags, natural-language agency analytics, plain-language family summaries), with explicit no-real-PHI handling.
- Integration depth rule (inference): [inference] Problem-fit only (no API likely); safe-handling of PHI and a clinician persona matter more than integration depth.
- Source: brief only (`06_hackutd_2026_sponsors/`); Q13_sponsor_card_rows.csv has 0 rows for this sponsor.

## Winstead PC — [brief only] no dataset winners
- Tier: Gold (assumed Dallas law firm, medium-low)
- What the sponsor asked: Challenge text and prizes NOT public [V]. No past HackUTD/Devpost challenge from Winstead found [V absence]; sponsors startup events (MassChallenge Texas, Texas A&M New Ventures) [V listing only]. Use only synthetic/public documents [brief].
- Past winners in dataset: 0 of 0 (no rows in Q13_sponsor_card_rows.csv). Counts, findings: not available.
- Pitch angle (inference): [inference] Trustworthy lawyer/client tool: lease or loan-agreement abstraction with source-cited quotes, startup legal-onboarding checklist, or data-room triage with an audit trail; accuracy, confidentiality and human-in-the-loop framing.
- Integration depth rule (inference): [inference] Problem-fit only; every claim should link to a source page/clause. Related dataset pattern: docs_to_action (see CBRE/Goldman cards).
- Source: brief only (`06_hackutd_2026_sponsors/`); Q13_sponsor_card_rows.csv has 0 rows for this sponsor.

## Photon
- Tier: Other
- What the sponsor asked: Not public; listed only under 'Other' sponsors, no event [V]. Product pitch: messaging-agent SDK, 'agents in the conversations people already use' [brief]. No past HackUTD sponsorship found (first time, [U]).
- Prize structure: Unknown.
- Past winners in dataset: 17 awards across 6 events (HackPrinceton Fall 2025 x5; DubHacks 2026 x3; LA Hacks AI Hackathon 2026 x3; HackNC 2026 x2; Hacklanta 2026 x2; MHacks 2026 x2).
  - Batman — HackNC 2026, placement 1, risk_detect_and_respond, owner=consumer: People meeting strangers text a plan to an iMessage contact that watches location and alerts a chosen friend if they go silent. <https://devpost.com/software/batman-cjer91>
  - Phish Finder — HackNC 2026, placement 2, risk_detect_and_respond, owner=consumer: People forward a suspicious link by iMessage and get a sandbox screenshot, verdict and plain-English reasons back. <https://devpost.com/software/phish-finder>
  - restock — DubHacks 2026, placement HM, workflow_automation_agent, owner=consumer: Roommates text what they ran out of to an iMessage agent that finds ranked live prices and splits the order bill. <https://devpost.com/software/restock-n5hxgo>
  - Safeword — Hacklanta 2026, placement HM, voice_to_action, owner=consumer: People walking alone at night text or call an agent; a spoken duress phrase silently alerts a human contact with a 911 script. <https://devpost.com/software/safeword-3ef01z>
  - SproutPass — LA Hacks AI Hackathon 2026, placement HM, realtime_coordination, owner=consumer: Parents photograph outgrown baby clothes by app or iMessage and get nearby trades matched to other parents' stated needs. <https://devpost.com/software/sproutpass>
  - Tenant — DubHacks 2026, placement unranked, realtime_coordination, owner=consumer: Guests scan a QR in a room and chat to borrow nearby devices for a ten-minute lease. <https://devpost.com/software/tenant-lpy96k>
  - Fluffy — DubHacks 2026, placement unranked, voice_to_action, owner=consumer: Elderly people and caretakers get a camera-driven assistant that infers needs and triggers tools like lights, music and caretaker texts. <https://devpost.com/software/fluffy-xq8lgp>
  - doeve — HackPrinceton Fall 2025, placement unranked, workflow_automation_agent, owner=consumer: Developers and power users text or voice-note iMessage to have an agent operate their Mac remotely. <https://devpost.com/software/do-eve>
  - Messenger AI — HackPrinceton Fall 2025, placement unranked, docs_to_action, owner=consumer: Friends in iMessage group chats get an agent that reads texts, PDFs and images and answers or summarizes from that context. <https://devpost.com/software/messenger-ai>
  - PiggyBank — HackPrinceton Fall 2025, placement unranked, data_to_decision, owner=consumer: Young spenders get iMessage nudges before habitual purchases, with receipt scanning and chat over their Snowflake spending history. <https://devpost.com/software/tbd-9clz1k>
  - TextFly — HackPrinceton Fall 2025, placement unranked, workflow_automation_agent, owner=consumer: Travelers text an agent number for flight search and weather answers, with delay prediction from social signals claimed. <https://devpost.com/software/textfly>
  - Wings — HackPrinceton Fall 2025, placement unranked, data_to_decision, owner=consumer: Thin-credit users get dynamic credit offers or spending advice from an iMessage coach and a BNPL demo. <https://devpost.com/software/wingpay>
  - Concierge — MHacks 2026, placement unranked, voice_to_action, owner=sponsor_internal_or_b2b: Small-business owners text a problem and AI voice agents call vendors, negotiate and book the best quote. <https://devpost.com/software/concierge-o38bu5>
  - Tab: Groupchat Accountant — MHacks 2026, placement unranked, workflow_automation_agent, owner=consumer: Friend groups log shared expenses in an iMessage group chat; a bot splits costs and settles up with a thumbs-up. <https://devpost.com/software/tab-groupchat-finances>
  - Ingineer — Hacklanta 2026, placement unranked, realtime_coordination, owner=consumer: Friend groups text one iMessage agent that matches calendars, creates events and calls specialist agents to plan outings. <https://devpost.com/software/ingineer>
  - BetterBill — LA Hacks AI Hackathon 2026, placement unranked, docs_to_action, owner=consumer: Patients photograph hospital bills, get sourced flags and assistance screening, and an AI advocate phones billing after approval. <https://devpost.com/software/betterbill>
  - Henomaly — LA Hacks AI Hackathon 2026, placement unranked, risk_detect_and_respond, owner=consumer: Poultry farmers get iMessage alerts with evidence images from an edge camera system that spots flock behaviour anomalies. <https://devpost.com/software/holy-crap>
- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):
  - pattern: workflow_automation_agent: 4 of 17 (24%); risk_detect_and_respond: 3 of 17 (18%); voice_to_action: 3 of 17 (18%); realtime_coordination: 3 of 17 (18%); docs_to_action: 2 of 17 (12%); data_to_decision: 2 of 17 (12%)
  - problem_owner: consumer: 16 of 17 (94%); sponsor_internal_or_b2b: 1 of 17 (6%)
  - prompt_literalness: 0: 1 of 17 (6%); 1: 2 of 17 (12%); 2: 10 of 17 (59%); na: 4 of 17 (24%)
  - sponsor_removable: no: 13 of 17 (76%); yes: 3 of 17 (18%); unknown: 1 of 17 (6%)
  - sponsor_features_used: median 1; 1: 16 of 17 (94%); 3: 1 of 17 (6%)
  - placement: unranked: 12 of 17 (71%); HM: 3 of 17 (18%); 1: 1 of 17 (6%); 2: 1 of 17 (6%); prize_kind: sponsor_open: 9 of 17 (53%); sponsor_api_depth: 8 of 17 (47%)
- What won:
  - FINDING: Photon winners are consumer agents where the Photon messaging layer was core (sponsor_removable no: 13 of 17 (76%)), mostly with one sponsor feature (sponsor_features_used=1: 16 of 17 (94%)).
    SUPPORT: 13 of 17 (76%) (unweighted, sponsor_removable=no); examples: Batman (HackNC 2026) <https://devpost.com/software/batman-cjer91>, Phish Finder (HackNC 2026) <https://devpost.com/software/phish-finder>, restock (DubHacks 2026) <https://devpost.com/software/restock-n5hxgo>
    COUNTEREXAMPLES: Fluffy (DubHacks 2026) <https://devpost.com/software/fluffy-xq8lgp>, Tab: Groupchat Accountant (MHacks 2026) <https://devpost.com/software/tab-groupchat-finances>, BetterBill (LA Hacks AI Hackathon 2026) <https://devpost.com/software/betterbill>
    CONFIDENCE: medium (n>=12, share>=70%; capped at medium: analyst tags, placements mostly unpublished)
    TYPE: association
    IMPLICATION FOR US: If a Photon track appears, the agent must be reachable through the real messaging channel in the live demo.
- Pitch angle (inference): Campus assistant over iMessage, group-chat agent, or an accessibility check-in agent; pair with a model backend (Nemotron is a natural pair, [U]).
- Integration depth rule (inference): Core use of the SDK with a live text exchange at the station; 1 feature is enough per the data (median 1).
- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv.

