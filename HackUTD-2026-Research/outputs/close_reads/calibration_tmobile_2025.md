# Q21 Calibration case: HackUTD 2025 T-Mobile track

Close read, 2026-11-06. Subjects:
- **InsighT**: https://devpost.com/software/t-insights. Badge "Winner T-Mobile"; placement unknown, treated as "placed above HarmoniQ".
- **Beacon**: https://devpost.com/software/na-504rkg. Badge "Winner T-Mobile"; placement unknown, treated as "placed above HarmoniQ".
- **HarmoniQ**: https://devpost.com/software/x-yiqm81. Badges "Winner T-Mobile" and "Winner Best Use of Auth0". The team says it placed 3rd; Devpost does not show this.

I treat HarmoniQ as an ordinary data point. The lessons below are about project features. They say nothing about the people.

**Sources read.** The three Devpost pages (fetched 2026-11-06) and the three linked GitHub repos. The InsighT README is detailed, the Beacon README is a title only (14 bytes), and the HarmoniQ README is empty: it was cleared on 2025-11-11, after the event. Because two READMEs were empty, I also read the source files that carry each project's core claims. Other sources: the rows in `04_deep_dives/data/deepdive_all.jsonl` and `01_winners/data/project_records.jsonl`, and the profiles in `04_deep_dives/profiles/winners/hackutd-hackutd-2025.md`.

**Baseline.** The baseline is the 16 non-winning T-Mobile-targeting entries from `data/tables/Q19_hackutd2025_track_targeting.csv`: 8 `demo_ready` and 8 `random`. Counts come from `scripts/q21_tmobile_calibration.py`, which writes `data/tables/Q21_tmobile2025_entries.csv` and `data/tables/Q21_tmobile2025_counts.csv`.

**Limits.**
- I did not watch any videos. All three pages embed a YouTube demo.
- The official T-Mobile challenge text was never public. The 3 winners and 12 of 16 (75%) baseline entries build a "Customer Happiness Index" (CHI), so the prompt probably asked for one. That is an `inference`.
- n = 3 winners, and placement is known only for HarmoniQ.

**Data corrections found.**
- `deepdive_all` says HarmoniQ has `has_video: false` and "no demo or video". The Devpost page embeds a YouTube video (id `rJU3_Fffqnc`). `project_records` has `has_demo_video: true` but `demo_video_url: null`. The correct value is **has_video = true**.
- `deepdive_all` lists HarmoniQ's live sentiment, outage prediction and CHI as `claimed`. The repo shows these are static or hardcoded in the demo dashboard (see §1.3). That is weaker than `claimed`.

---

## 1. Per-project fields (spec §2.3) and ratings (spec §2.4)

All quotes come from the Devpost page unless marked `[repo]`. Ratings are analyst judgments, not judge scores (rule 5).

### 1.1 InsighT

| field | value | evidence (≤25 words) |
|---|---|---|
| tagline | "Unified dashboard for T-Mobile PMs to track real-time customer sentiment, performance, and operational data, driving smarter, data-driven decisions and improved customer satisfaction." | verbatim |
| one_sentence | T-Mobile PMs see scraped complaints and outages as a happiness index, heatmap and AI-prioritized opportunities. | — |
| pattern | data_to_decision | "turns raw noise into prioritized, location‑aware, actionable intelligence" |
| named_user | true | "We set out to give PMs the power to see, understand, and act." |
| cost_of_problem_stated | asserted | "Feedback is scattered across social media, outage trackers, forums, and support logs." |
| ai_role | single_call_wrapper | "Google Gemini 2.0 Flash for insights on emerging issues via secure server‑side API routes." Sentiment and topic detection are in the pipeline. |
| has_hardware | no | web only |
| live_data | yes | "Scrapers for Reddit, News, DownDetector, IsTheServiceDown, Outage.Report, plus customer feedback". `[repo]` The Reddit scraper fetches `reddit.com/r/{sub}.json` live. |
| n_user_flows | 2 (monitor dashboard; opportunity → PRD/stories) | "Generates AI‑powered, actionable opportunities with priority/urgency, root cause analysis, recommended actions, impact, and stakeholders". The README lists "PRD Generation", "User Stories Generation". |
| mocked_parts_disclosed | no | Nothing is admitted on the page. `[repo]` The repo has `downdetector-data.json`, `community-sample.json` and an "insert sample data" button. |
| n_external_deps | 10 | Reddit, Google News, DownDetector, IsTheServiceDown, Outage.Report, Supabase, Gemini, OpenStreetMap, Nominatim, Vercel |
| sponsor_features_used | 0 (T-Mobile) | No T-Mobile API or product is named. T-Mobile is the problem owner. |
| sponsor_removable | n/a (no T-Mobile tech) | — |
| prompt_literalness | 2 (vs inferred CHI prompt) | "Computes a Customer Happiness Index (CHI) and trends by product area (Network, Mobile App, Billing, Home Internet)." |
| prompt_words_in_title | 0 | "InsighT" (capital T is a brand nod, not prompt wording) |
| problem_owner | sponsor_internal_or_b2b | "for T-Mobile PMs" |
| novelty_source | execution_of_familiar_idea | The twist is going from signal to opportunity to PRD and user stories. |
| technical_centerpiece | Seven-source scraper ingestion with dedup, topic detection and intensity weighting, feeding a geo heatmap and Gemini opportunities. | "Sentiment scoring, topic detection, deduplication/merging, and intensity weighting." |
| centerpiece_visible | in_demo_output | "Visualizes geographic clusters via a Leaflet heatmap and overlays live outage markers." Live site and 15 screenshots. |
| has_video | true | YouTube 4c7uRVxoJfc (not watched) |
| has_arch_diagram | false | none on page |
| n_images | 15 | uncaptioned screenshots |
| wow_moment | A live heatmap with outage markers next to AI opportunity cards giving root cause, priority and stakeholders. | — |

Other evidence: the page links a live site, insight-tmobile.us. It returned HTTP 200 on 2026-11-06 and redirects to /login. The page claims "production‑ready experience".

| dimension | rating | justification |
|---|---|---|
| innovation | 3 | Familiar CHI dashboard. The one real twist is turning signals into PRDs, user stories and RICE-scored opportunities. |
| technical_complexity | 4 | Seven scrapers, cron-secured ingestion, dedup and topic detection, Postgres, geo pipeline and Gemini routes, all present in the repo. |
| completeness | 4 | Deployed live site, video and 15 screenshots. PRD generation is only claimed. |
| design | 4 | "clean, on‑brand dashboard" and many distinct views shown. I can't confirm polish beyond the screenshots. |
| impact | 3 | Plausible benefit for named PMs. No stats or user evidence. |
| presentation | 4 | The tagline names the user and value, and the README is detailed. The tagline is long, so the value is not obvious at a glance. |

### 1.2 Beacon

| field | value | evidence (≤25 words) |
|---|---|---|
| tagline | "A real-time, cross-domain Customer Happiness Index that detects, tracks, and helps act on customer sentiment for T-Mobile." | verbatim |
| one_sentence | T-Mobile call agents and PR teams see live, PII-scrubbed call sentiment and social triage on a happiness map. | — |
| pattern | data_to_decision | "connects those signals to personalized recommendations, automated triage, and actionable insights" |
| named_user | false (first two sentences name a mascot and T-Mobile; agents and PR teams appear later) | "Meet Telly, your friendly companion turning customer data into delight." |
| cost_of_problem_stated | asserted | "After calling T-Mobile ourselves, we imagined a world where every customer interaction leaves behind a digital heartbeat" |
| ai_role | multimodal_pipeline | "Cleaned transcripts are analyzed for sentiment and issue classification using an LLaMA model hosted on the Groq API." |
| has_hardware | no | phone calls via Twilio, no team hardware |
| live_data | yes | "Twilio captures live customer calls and streams them to a Flask server via ngrok." `[repo]` `answer_phone.py` imports Twilio and Presidio. |
| n_user_flows | 3 (central map, call-agent dashboard, PR/campaign dashboard) | Gallery captions: "Central Dashboard", "Call Center Agent Dashboard", "Social Campaigns Dashboard" |
| mocked_parts_disclosed | no | Nothing is admitted on the page. `[repo]` The repo has `generate_fake_data.py` ("Generate fake call data with random locations") and static `reddit.json` and `twitter.json`. |
| n_external_deps | 8 | Twilio, ngrok, Presidio, Groq/LLaMA, MongoDB Atlas, ForumScout, Downdetector, Auth0 |
| sponsor_features_used | 0 (T-Mobile) | The page uses T-Mobile brand values and the T-Mobile Tuesday offer concept, but no T-Mobile tech. |
| sponsor_removable | n/a | — |
| prompt_literalness | 2 (vs inferred CHI prompt) | "Aggregates sentiment, feedback, and network data to produce a live 0–100 'Happiness Score' by region, service, and location." |
| prompt_words_in_title | 0 | "Beacon" |
| problem_owner | sponsor_internal_or_b2b | "Provides T-Mobile service agents with a real-time, branded view of customer issues" |
| novelty_source | new_data_or_context | Live call audio is the third data domain, alongside social and outage data. |
| technical_centerpiece | Live Twilio call → Presidio PII scrub → Groq LLaMA sentiment/issue → MongoDB → agent dashboard. | "Presidio ensures no sensitive data reaches AI models" |
| centerpiece_visible | in_demo_output (per screenshot caption; video not watched) | "Live, PII-Scrubbed Transcriptions: Calls captured via Twilio and scrubbed in our Flask backend are streamed in real time" |
| has_video | true | YouTube VelZ-2xXLAw (not watched) |
| has_arch_diagram | false (a "Tech Stack" image, not a flow diagram; not verified visually) | caption "Tech Stack" |
| n_images | 5 | Login, Central Dashboard, Call Center Agent Dashboard, Social Campaigns Dashboard, Tech Stack |
| wow_moment | Phoning in and watching a PII-scrubbed transcript with sentiment appear on the agent dashboard during the call. | — |

| dimension | rating | justification |
|---|---|---|
| innovation | 4 | The live-call domain plus privacy-first PII scrubbing plus PR campaign and offer planning goes beyond the standard CHI dashboard. |
| technical_complexity | 4 | A real telephony → PII → LLM → database pipeline exists in the repo. Social and outage data are partly static. |
| completeness | 3 | Three dashboards shown, but the call pipeline is only claimed on the page. The repo seeds fake call data and has no README. |
| design | 4 | Three persona-specific dashboards, a branded mascot, and on-brand tone throughout. |
| impact | 3 | Named agent and PR users with a plausible benefit. No evidence. |
| presentation | 4 | The tagline states the product in one line and the mascot is memorable. The README is empty. |

### 1.3 HarmoniQ (3rd, + Best Use of Auth0)

| field | value | evidence (≤25 words) |
|---|---|---|
| tagline | "A command-center for T-Mobile product managers to anticipate customer needs. See sentiment in real time, predict outages, and allocate resources—all to strengthen every customer connection." | verbatim |
| one_sentence | T-Mobile PMs and network engineers see sentiment, predicted regional outages and Gemini-suggested actions in one dashboard. | — |
| pattern | data_to_decision | "visualizing hotspots, predicting outages, generating insights, allocating resources and automatically assigning tasks for resolution" |
| named_user | false in the description's first two sentences (users are named in sentence 4 and in the tagline) | "helps product managers and network engineers in detecting early issues" |
| cost_of_problem_stated | asserted | "Telecommunications companies often struggle to bridge the gap between technical performance data and customer satisfaction metrics." It mentions a literature review but cites no statistic. |
| ai_role | custom_or_finetuned_model (+ Gemini chat) | "Using trained Random Forest and Gradient Boosting models, HarmoniQ predicts the likelihood of service outages across different regions." |
| has_hardware | no | — |
| live_data | unknown: the page claims yes, the repo contradicts it | Page: "continuously tracks live sentiment from online forums like Reddit & X". `[repo]` The dashboard loads a static `Assets/social_media_feedback.json` with pre-labelled sentiment. |
| n_user_flows | 1 (land → Auth0 login → workspace dashboard) | Gallery captions: "Landing Page", "Login Page", "Dashboard" |
| mocked_parts_disclosed | yes | "augmented with simulated regional outage data"; "We overcame this by synthesizing realistic outage events" |
| n_external_deps | 5 | Reddit, X, Kaggle datasets, Gemini, Auth0 |
| sponsor_features_used | T-Mobile 0. Auth0: 3 (Universal Login, Google and Microsoft social connections, user profile/session) | `[repo]` `loginWithRedirect({ authorizationParams: { connection: "google-oauth2" } })` |
| sponsor_removable | T-Mobile n/a. Auth0 yes (login gate only) | — |
| prompt_literalness | 2 (vs inferred CHI prompt) | "The platform computes a Customer Happiness Index (CHI) that reflects the overall satisfaction level in real time." |
| prompt_words_in_title | 0 | "HarmoniQ" |
| problem_owner | sponsor_internal_or_b2b | "command-center for T-Mobile product managers" |
| novelty_source | combination | Network-performance data joined with social sentiment, plus outage prediction. |
| technical_centerpiece | Offline Random Forest and Gradient Boosting outage classifiers on Kaggle network data plus synthetic outages. | "Both were trained on custom-curated datasets based on publicly available Kaggle samples and augmented with simulated regional outage data." |
| centerpiece_visible | described_only | `[repo]` The model lives in a notebook. The dashboard's outage map uses three hardcoded points (Dallas 0.35, Houston 0.72, Austin 0.28), and the "Predict" button calls `/predict/outage`, which neither Flask app in the repo defines. |
| has_video | true | YouTube rJU3_Fffqnc (not watched); corrects `deepdive_all` |
| has_arch_diagram | unknown | Captions "brainstorming", "main features" were not inspected visually. |
| n_images | 6 | logo, Landing Page, Login Page, Dashboard, brainstorming, main features |
| wow_moment | A Gemini assistant explaining "latency spikes correlate with negative keyword surges" and proposing triage actions. | `[repo]` The `/ai/triage` and `/ai/chat` Gemini endpoints exist and are real calls. |

Other repo facts, for HarmoniQ only. These are code facts; I am not implying anything about what the team intended.
- The CHI trend line and the competitor chart on the dashboard are hardcoded arrays.
- The repo also contains a separate React "Network Optimizer" app built on a Kaggle Bihar (India) 3G/4G dataset (`PROJECT_SUMMARY.md`). That app is not wired to the Auth0 dashboard.
- The repo contains unrelated pages ("Reading Practice", "Fox Mode").
- A Gemini API key is committed in plaintext in `server/main.py`. I did not record the value.

| dimension | rating | justification |
|---|---|---|
| innovation | 3 | Joining network performance with sentiment for outage prediction is a real twist on the CHI dashboard. 1 of 8 `demo_ready` (Sync) and 1 of 8 `random` (T-Mobile Happy Assessment Dashboard) also pitched sentiment + network data. |
| technical_complexity | 2 | The page reads like a 3. Visible code shows a working Gemini proxy and an offline notebook model, but the dashboard data is static or hardcoded and the predict path is not wired. |
| completeness | 2 | Login and the dashboard shell work. The core prediction and live-sentiment journey is not end-to-end in the repo at HEAD. |
| design | 3 | Clean landing, login and workspace pages. 3 of 6 gallery images are logo, brainstorming and features rather than the product. |
| impact | 3 | Named PMs and network engineers with a plausible benefit. "Strong accuracy" is claimed with no number. |
| presentation | 3 | The tagline is clear but long. The page is readable, the README is empty, and only one product screenshot is captioned "Dashboard". |

---

## 2. Gap table: HarmoniQ vs the two placed above it

| dimension | InsighT | Beacon | HarmoniQ | gap (HarmoniQ − mean of the two above) | visible difference |
|---|---|---|---|---|---|
| innovation | 3 | 4 | 3 | −0.5 | Beacon added a whole new data domain (live calls with PII scrubbing). HarmoniQ's twist (network + sentiment) stayed mostly in prose. |
| technical_complexity | 4 | 4 | 2 | −2.0 | Both higher placers have a real ingestion pipeline in code (scrapers; Twilio → Presidio → LLM). HarmoniQ's headline ML is offline and not wired to the dashboard. |
| completeness | 4 | 3 | 2 | −1.5 | InsighT shipped a deployed live site and Beacon three working persona dashboards. HarmoniQ shows one flow, login → dashboard, on static data. |
| design | 4 | 4 | 3 | −1.0 | The higher placers show 15 and 4 product screenshots. HarmoniQ shows 1 product screenshot plus landing and login pages. |
| impact | 3 | 3 | 3 | 0 | No difference: all three assert the problem without evidence and target internal T-Mobile staff. |
| presentation | 4 | 4 | 3 | −1.0 | The higher placers have one-line, CHI-first taglines (and InsighT a detailed README). HarmoniQ has a long tagline and an empty README. |

The largest gaps are technical_complexity and completeness. Both are about whether the core data path actually runs, not about the idea. Impact shows no gap. (Analyst ratings, n = 3, `inference`.)

---

## 3. Auth0 integration depth (HarmoniQ), or what a cheap API side prize cost

What it did, from repo files `login-auth.js`, `profile-auth.js`, `login.html` and `profile.html`:
- Loads `auth0-spa-js` 2.0 from the Auth0 CDN, with `domain` and `clientId` read from `auth_config.json`.
- The login page sends email/password, "Forgot password" and "Sign up" (`screen_hint: "signup"`) to Auth0 Universal Login with `loginWithRedirect()`.
- It offers Google (`google-oauth2`) and Microsoft (`windowslive`) social connections.
- The workspace page completes the callback with `handleRedirectCallback()` and guards itself with `isAuthenticated()`, redirecting to login if needed.
- It shows the user's name, avatar and email from `getUser()`, and has a logout button.

What it did not do:
- No roles or RBAC.
- No access tokens sent to the backend. The Flask API at `127.0.0.1:5001` has no auth checks (0 auth/token references in `server/main.py`).
- No MFA, Actions or Organizations.
- Redirect URIs are hardcoded to `127.0.0.1:8000`, so it was demoed locally.

The page says only: "integrating secure authentication with Auth0". Auth0 does not appear in the Built With list.

**Effort: small (scope, not a duration estimate).** It is about 100 lines of JS plus Auth0 dashboard setup for an app and two social connections, following the Auth0 SPA quickstart.

**Comparison.**
- Beacon used Auth0 at about the same depth: `Auth0Provider`, `useAuth0`, a `Protected` route component and logout. Its page's "role-based access" claim has no role code visible in `AuthContext.tsx` or `Protected.tsx`. Beacon did not win the Auth0 prize. Whether it entered that track is unknown.
- In the baseline, 1 of 8 `random` (lisTen.AI) and 0 of 8 `demo_ready` T-Mobile entries mention Auth0.
- So login-only Auth0 was enough to win this side prize once. Why HarmoniQ was picked over Beacon is not explained by available evidence.

---

## 4. Table stakes vs differentiators in the 2025 T-Mobile track

Counts come from keyword flags over the existing record and deep-dive text (`data/tables/Q21_tmobile2025_counts.csv`). They mean "mentioned", not "verified working". The winner cells are low n (3). The baseline groups are never pooled.

| feature | winners (3) | demo_ready (8) | random (8) | read |
|---|---|---|---|---|
| Customer Happiness Index / happiness score | 3 of 3 (100%) | 7 of 8 (88%) | 5 of 8 (62%) | **table stakes**. Almost certainly the prompt (inference). |
| Map / heatmap | 2 of 3 (67%) by flag. 3 of 3 by close read: HarmoniQ has a Leaflet outage map | 6 of 8 (75%) | 6 of 8 (75%) | **table stakes** |
| LLM-generated actions/insights | 3 of 3 (100%) | 7 of 8 (88%) | 3 of 8 (38%) | table stakes vs `demo_ready` |
| Synthetic/mock data | 1 of 3 (33%) disclosed on page. 3 of 3 in repos by close read | 5 of 8 (62%) | 4 of 8 (50%) | universal. Real data was hard to get for everyone. |
| Outage/network data fused with sentiment | 3 of 3 (100%) | 2 of 8 (25%) | 3 of 8 (38%) | **the clearest winner-vs-baseline association** |
| Median named tech items | 6 | 4 | 3 | winners integrated more sources |
| Live deployed demo | 1 of 3 (33%) | 1 of 8 (12%) | 0 of 8 (0%) | rare everywhere |
| Call/voice data | 1 of 3 (33%) | 1 of 8 (12%) | 2 of 8 (25%) | a differentiator for Beacon only |

**Shared by all three winners.** Fact, from the pages:
- CHI-named output.
- A T-Mobile-internal user (PMs, agents, PR).
- At least three data source types, including outage or network data.
- An LLM layer that writes recommended actions.
- A web dashboard with a map.
- A YouTube demo.
- Prose that uses T-Mobile brand language. All three use "T-Mobile" in the tagline.
- No T-Mobile API, because none was publicly available.

**What distinguished the two above HarmoniQ** (association, n = 3):
1. A data path that visibly runs end to end, from a live source to an on-screen number. InsighT has live scrapers and a deployed site. Beacon has live phone calls through a PII scrubber.
2. Several distinct product screens and personas shown: 15 screenshots for InsighT, 3 persona dashboards for Beacon. HarmoniQ showed 1 product screenshot.
3. An action artifact past the chart: generated PRDs, user stories and RICE-scored opportunities (InsighT); agent resolution suggestions and campaign/offer plans (Beacon). HarmoniQ's equivalent, task assignment and Slack/Jira alerts, is described or "planned".

**Counterexample to "more sources plus Gemini wins".** Read the Room (`demo_ready`, https://devpost.com/software/cool-project-w4h7ob) did not win. It pulls Reddit, X, Trustpilot and DownDetector, scores call transcripts with Gemini, has about 20k LOC, 19 screenshots, a video and a detailed README. It is on paper as broad as InsighT. What separated it is not explained by available evidence: no live site is recorded, but placement drivers are not visible on the page.

---

## 5. Findings

```
FINDING: In the 2025 T-Mobile track a CHI-style sentiment dashboard with a map and LLM recommendations was table stakes, not a differentiator: present in all 3 winners and most non-winners.
SUPPORT: happiness index 3 of 3 winners (100%, low n), 7 of 8 demo_ready (88%), 5 of 8 random (62%); map 6 of 8 (75%) in each baseline group; LLM actions 7 of 8 demo_ready (88%). Unweighted. Examples: InsighT https://devpost.com/software/t-insights, Beacon https://devpost.com/software/na-504rkg, HarmoniQ https://devpost.com/software/x-yiqm81; non-winners SentimentRadar https://devpost.com/software/sentimentradar, T-Pulse https://devpost.com/software/t-pulse. Table: data/tables/Q21_tmobile2025_counts.csv
COUNTEREXAMPLES: none found among T-Mobile winners
CONFIDENCE: medium (baseline is the only valid winner-vs-non-winner set and the pattern is lopsided, but winner n = 3 and flags are keyword-derived)
TYPE: association
IMPLICATION FOR US: If 2026 T-Mobile repeats a sentiment/CX prompt, treat "score + map + AI suggestions" as the floor; budget build time for what comes after it, not for the dashboard itself.
```

```
FINDING: The 3rd-place entry's largest visible gap to the two placers above it was whether the core data path visibly ran end to end, not idea or impact.
SUPPORT: analyst ratings: technical_complexity gap −2.0, completeness −1.5, impact 0 (n = 3). InsighT has live scrapers plus a deployed site; Beacon has a Twilio→Presidio→LLM pipeline in code; HarmoniQ's dashboard uses a static social JSON, hardcoded outage points and CHI series, and a predict endpoint not defined in the repo. Links above.
COUNTEREXAMPLES: Read the Room (non-winner, https://devpost.com/software/cool-project-w4h7ob) shows a broad, apparently working pipeline yet did not place
CONFIDENCE: low (n = 3; ratings are analyst judgments; the live demo at judging may have differed from repo HEAD; videos not watched)
TYPE: inference
IMPLICATION FOR US: Make at least one input → number path genuinely live and demonstrable at the station (e.g. post/call in → score changes on screen) before adding any modelled or predicted feature.
```

```
FINDING: Every 2025 T-Mobile winner fused outage or network data with customer sentiment, which only a minority of non-winning T-Mobile entries did.
SUPPORT: 3 of 3 winners (100%, low n) vs 2 of 8 demo_ready (25%) and 3 of 8 random (38%); median named tech items 6 vs 4 vs 3. Examples: InsighT (DownDetector, IsTheServiceDown, Outage.Report), Beacon (Downdetector), HarmoniQ (Kaggle network data).
COUNTEREXAMPLES: Read the Room and MagentaMonitor (demo_ready) also used outage data and did not win; Sync (demo_ready) fused sentiment with network health and did not win
CONFIDENCE: low (n = 3 winners; keyword flags over existing records)
TYPE: association
IMPLICATION FOR US: In a telecom CX prompt, join customer-voice data to an operational signal (outages, coverage, network) rather than reporting sentiment alone.
```

```
FINDING: The Best Use of Auth0 prize was won with a login-only integration (Universal Login, Google/Microsoft social login, route guard, profile display, logout) estimated at low effort.
SUPPORT: 1 of 1 Auth0 winner in this set (HarmoniQ, https://devpost.com/software/x-yiqm81); repo shows ~100 lines of auth0-spa-js, no roles, no backend token checks. Effort: small in scope (login only). Beacon used Auth0 at similar depth and did not win the Auth0 prize (entry status unknown).
COUNTEREXAMPLES: Beacon (similar depth, no Auth0 prize)
CONFIDENCE: low (n = 1; MLH judging criteria and entrant count not visible)
TYPE: fact (integration depth) / inference (that depth sufficed)
IMPLICATION FOR US: If an MLH Auth0 prize exists, add Auth0 Universal Login with one social connection early, as a small-scope add-on; say so explicitly on the Devpost (HarmoniQ named it in one sentence and not in Built With).
```

```
FINDING: Mocked or synthetic data was used by all three winners, but only the 3rd-place entry disclosed it on its page, so disclosure did not visibly change outcomes.
SUPPORT: disclosed on page 1 of 3 (HarmoniQ: "augmented with simulated regional outage data"); in repos 3 of 3 (InsighT sample JSON + insert-sample-data button; Beacon generate_fake_data.py, static reddit.json/twitter.json; HarmoniQ static social JSON). Baseline mock mentions 5 of 8 demo_ready (62%), 4 of 8 random (50%).
COUNTEREXAMPLES: none found
CONFIDENCE: low (n = 3; repo state may differ from what was demoed)
TYPE: fact (presence) / inference (no visible effect)
IMPLICATION FOR US: Seeded/sample data is acceptable in this track; pair it with one real live source and label which is which when judges ask.
```

```
FINDING: The two placers above 3rd each showed more distinct product screens or personas on the Devpost than HarmoniQ did.
SUPPORT: product screenshots InsighT 15, Beacon 4 of 5 (three persona dashboards + login), HarmoniQ 1 of 6 ("Dashboard"; others logo, landing, login, brainstorming, features). n = 3.
COUNTEREXAMPLES: Read the Room (19 screenshots) and Satisfaction Visual Analytics (19) did not win
CONFIDENCE: low (n = 3; non-winners with many screenshots break any simple rule)
TYPE: association
IMPLICATION FOR US: Fill the Devpost gallery with captioned product screens (one per persona/flow), not logos or brainstorm boards.
```
