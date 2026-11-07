# PennApps — PennApps XXVI (2 projects)

### SproutAI
*PennApps PennApps XXVI · dataset: sponsor · tier: sponsor_winner · evidence B · confidence low*
**Prizes:** Winner CATEGORY - Finance (Capital One)

**What it is:** A demand-forecasting dashboard for grocery stores that aims to reduce food waste by matching stock to predicted demand and showing sustainability scores. The page names Cerebras, Exa and Gemini as the AI stack but gives little concrete detail.
**Problem / user:** Grocery stores, warehouses and small businesses that lose sales and create waste because they cannot predict demand.

**Features**
- ML demand forecasting — TensorFlow models trained on retail and environmental datasets predict demand. *[claimed]*
- Inventory flow dashboard — React dashboard shows inventory flows in real time. *[claimed]*
- Waste reduction impact view — Dashboard shows waste avoided across stores. *[claimed]*
- Sustainability scoring — Scores tied to operational efficiency and carbon impact. *[claimed]*
- Actionable recommendations — Suggests stocking adjustments from forecasts. *[claimed]*

**Flow:** Business loads retail data → Models forecast demand → Dashboard shows inventory and waste impact → User follows stocking recommendations

**Prompt:** Finance category sponsored by Capital One, chosen at Devpost submission; no further brief.
**Fit (none):** Connection to finance is indirect: cost savings and waste reduction for retailers via forecasting. Page does not state the link to the Finance category.  *(targeted: CATEGORY - Finance (Capital One))*
**AI:** Demand forecasting models in Python and TensorFlow; Cerebras for training/inference scale, Exa and Gemini named but roles unspecified.
**Architecture:** React dashboard over Python/TensorFlow forecasting models; data sources unnamed.
**Novelty:** Pairs retail demand forecasting with sustainability metrics; description is high level.
**Scope:** small · working: Page claims a working prototype; no repo, demo or video. · polish: Four screenshots with no captions; otherwise unverified.
**Claims:** Working prototype predicts demand and highlights waste savings
**Gaps:** No repo; No demo or video; Data sources and model details absent; Connection to Finance category unstated
Sources: https://devpost.com/software/sproutai-9vil8w

---

### Subsave
*PennApps PennApps XXVI · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner CATEGORY - Finance (Capital One)

**What it is:** A mobile subscription manager that has users prepay a year of subscriptions into a DeFi yield vault so the yield offsets costs, while keeping monthly cancellation. Blockchain details are hidden behind a plain dashboard; yield is simulated in the demo.
**Problem / user:** Individuals paying many monthly subscriptions that return nothing, with trackers that only monitor and cancellation that requires chasing each merchant.

**Features**
- Prepaid subscription vault — User deposits about a year of subscription cost into a vault that is designed to earn DeFi yield. *[claimed]*
- Simulated yield accrual — Demo models yield over time to show lower effective cost. *[shown_working]*
- Mobile dashboard — Expo/React Native Paper screens for adding subscriptions, balances, upcoming charges, vault detail and notifications. *[shown_working]*
- Monthly cancel with withdrawal logic — Vault withdrawals and policy rules return funds when a subscription is cancelled. *[claimed]*
- Gemini plan advice — Fetches subscription info, recommends tier and prepay horizon. *[claimed]*
- Grid SDK automated payments — Programmable accounts with spending caps pay merchants automatically. *[planned]*

**Flow:** Log in with Auth0 → Add subscriptions → Prepay into a vault → See balances and upcoming charges → Cancel monthly and withdraw remainder

**Prompt:** Finance category sponsored by Capital One, chosen at Devpost submission; no further brief.
**Fit (implied):** Consumer finance product that reduces recurring costs through yield; no Capital One API is used.  *(targeted: CATEGORY - Finance (Capital One))*
**AI:** Google Gemini API fetches subscription data for any service, recommends plan tier and optimizes the prepay horizon; role is only lightly described on Devpost.
**Architecture:** Expo React Native client with Auth0 login and MongoDB Atlas storage; service layer wraps blockchain calls designed for Squads Grid SDK vaults; Gemini for recommendations.
**Novelty:** Uses DeFi yield to subsidize ordinary subscriptions without merchant cooperation, with crypto abstracted away.
**Scope:** small · working: About 7.8k LOC in the app excluding dependencies, has tests; yield is simulated and Grid integration unfinished. · polish: Detailed README; no demo or video links.
**Claims:** Subscriptions become cheaper without merchants changing anything
**Gaps:** No demo or video; Real DeFi integration absent
Sources: https://devpost.com/software/subsave, https://github.com/adlonymous/subsave

---

