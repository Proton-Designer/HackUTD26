# Technica — Technica 2025 (2 projects)

### Personal Cart Roaster
*Technica Technica 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner [Capital One] Best Financial Hack

**What it is:** A Chrome extension that sends a shopper's cached personal info and cart to Gemini to generate a personalized roast, then reads it aloud with an ElevenLabs voice to discourage impulse buying. Currently Amazon only.
**Problem / user:** Online shoppers, including the creator, who impulse buy.

**Features**
- Cart roast — Gemini generates a roast from the cart and stored personal info *[claimed]*
- Voice playback — ElevenLabs reads the roast through a click-to-play audio player (MV3 autoplay limits) *[claimed]*
- Personal info cache — User enters details stored locally *[claimed]*

**Flow:** Install extension → Enter personal info → Shop on Amazon → Click play to hear roast

**Prompt:** Capital One Technica 2025 Best Financial Hack: bold fintech project for payments, smarter shopping, accessible financing or financial literacy; judged on creativity, complexity, completeness.
**Fit (implied):** Uses humor to curb impulse spending, a smarter-shopping angle; page lists the win.  *(targeted: [Capital One] Best Financial Hack)*
**AI:** Gemini writes the roast from cart and user info; ElevenLabs text-to-speech voices it.
**Architecture:** Manifest V3 Chrome extension (TypeScript, React/Vite) calling Gemini and ElevenLabs APIs.
**Novelty:** Shame-by-voice deterrent rather than a budgeting tool; solo build in under 24 hours.
**Scope:** tiny · working: Creator says Gemini and ElevenLabs calls work; two screenshots; no repo or video. · polish: Creator calls audio workaround unpolished.
**Claims:** Built solo in under 24 hours
**Gaps:** no repo; no video
Sources: https://devpost.com/software/personal-cart-roaster, sponsor_prompts_*.jsonl (Technica 2025)

---

### Resale Radar
*Technica Technica 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner [Capital One] Best Financial Hack

**What it is:** A Java desktop app that scrapes sold-item data from Poshmark with Playwright, drops statistical outliers, computes a recommended listing price for an item, and charts the underlying data in a JavaFX/FXML GUI.
**Problem / user:** Online resellers on sites like Poshmark who need to list items at prices that actually sell, rather than relying on the site's suggestions or original prices.

**Features**
- Scrape Poshmark category/sold data — Playwright pulls sale data for item categories from Poshmark listings *[claimed]*
- Outlier exclusion — Statistical analysis removes extreme prices before computing the estimate *[claimed]*
- Recommended listing price — Java methods compute an effective price from sale history, demand and historical value *[claimed]*
- Graphing of scraped data — Results and data distribution are plotted in the GUI *[claimed]*
- JavaFX GUI — Layout built in SceneBuilder with FXML for viewing results *[claimed]*
- Support for Depop and eBay — Extend scraping to other resale sites *[planned]*

**Flow:** Open the desktop app → Enter or choose an item/category → App scrapes Poshmark sold data → Outliers are filtered out → Recommended price and graphs are shown

**Prompt:** not public / not found
**Fit (implied):** A pricing tool that helps sellers maximize sale revenue, which is a finance-adjacent consumer tool; the page does not state the link to the prize or use any Capital One resource.  *(targeted: Capital One Best Financial Hack)*
**AI:** none
**Architecture:** Playwright scraper feeds a Java backend that filters outliers and computes the price; a JavaFX (FXML/SceneBuilder) front end displays the recommendation and graphs.
**Novelty:** Uses real sold-listing data from a resale marketplace as the pricing basis rather than a generic finance API; plain statistics, no ML.
**Scope:** small · working: Page lists scraping, outlier removal and graphing as accomplished; no demo, video or repo link. · polish: Basic GUI only; the page has an unfilled What is next heading.
**Gaps:** no repo link; no demo or video; no user flow described; no Technica-specific Capital One prompt text
Sources: https://devpost.com/software/resale-radar

---

