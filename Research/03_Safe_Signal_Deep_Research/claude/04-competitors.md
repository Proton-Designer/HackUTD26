# 04 - Competitive landscape (Safe Signal track)

## TL;DR
1. T-Mobile Scam Shield is strong at the network edge and before contact (Scam Likely labels, call blocking, SMS/MMS blocking, Safe Web Browsing, Callback Protection). It is weak during a live scam conversation and has nothing after a loss except 7726 reporting.
2. The best in-call tools today are on-device and tied to the handset: Google Scam Detection (Pixel, Galaxy S26), Samsung (Korea only), Hiya AI Phone ($9.99/mo app). No US carrier ships in-conversation scam analysis. AT&T's LLM "digital receptionist" was only a North Texas pilot as of Sep 2025.
3. Nobody US-side connects the threat to the payment moment except Google's Android in-call banking warning (30-second pause, Dec 2025 US rollout with Cash App and JPMorganChase). Most recovery help sits in paid bundles: Norton LifeLock Ultimate Plus reimbursement and AT&T Advanced ID insurance. UK banks are the gold standard (Confirmation of Payee plus mandatory reimbursement).
4. Every product works one channel at a time. None follows one scam across text, then callback, then payment, then recovery as a single incident with explanations and next steps.
5. Pitch hook: T-Mobile's Nov 2, 2026 cybersecurity report says it is preparing for AI-enabled fraud and AI agents. Our Nemotron agent can be the customer-facing "during and after" layer on top of Scam Shield's "before."

---

## 1. T-Mobile Scam Shield (free) and Scam Shield Premium

### Current feature list (official)
Source: https://www.t-mobile.com/scamshield and https://www.t-mobile.com/benefits/scam-shield (fetched 2026-11-07)

**Free**
- Scam Likely caller label, plus Scam Block, which auto-blocks Scam Likely calls. The page warns it may block calls you want. https://www.t-mobile.com/scamshield
- Personal number blocking, Potential Spam ID, and spam calls sent to voicemail. https://www.t-mobile.com/scamshield
- Callback Protection: warns you when you dial a number on the Scam Likely list. https://www.t-mobile.com/benefits/scam-shield
- Safe Web Browsing: blocks known scam and phishing sites at the network level. https://www.t-mobile.com/scamshield
- Network spam text blocking for SMS and MMS only, free since 2014. https://www.t-mobile.com/benefits/scam-shield
- Scam Block toggle via T-Life, My T-Mobile, or dial #662#. https://www.t-mobile.com/benefits/scam-shield
- Report spam texts by forwarding to 7726. Data may be shared with government and used to train filters. https://www.slashgear.com/2200747/tmobile-report-spam-feature-effectiveness/ (Jun 28, 2026)
- Caller verification relies mainly on STIR/SHAKEN. https://www.slashgear.com/2200747/tmobile-report-spam-feature-effectiveness/
- Account-side protection: SIM Protection, Port-Out Protection, and biometric ID verification. T-Mobile credits these for a 99%+ drop in successful SIM swaps since 2022. https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile (Nov 2, 2026)

**Premium: $4/mo per line add-on** https://www.t-mobile.com/benefits/scam-shield
- Send categorized call types (for example telemarketers) to voicemail.
- Reverse phone number lookup.
- Voicemail transcribed and texted to you.
- The official FAQ lists personal number blocking under both free and Premium, so the exact split is unclear. https://www.t-mobile.com/benefits/scam-shield
- Which plans bundle Premium at no cost (for example Experience More or Beyond): UNVERIFIED. The official page only describes the add-on, and SlashGear says only "included in some plans."

### Channel coverage
| Channel | Coverage | Source |
|---|---|---|
| Calls | Yes. Label, block, voicemail routing, outbound callback warning | t-mobile.com/scamshield |
| SMS/MMS | Yes. Network blocking of known spam patterns | t-mobile.com/benefits/scam-shield |
| RCS | Partial. A competitor blog says RCS is checked against T-Mobile's spam database. UNVERIFIED by T-Mobile | https://www.cape.co/blog/t-mobile-spam-blocker (Apr 17, 2026, competitor source) |
| iMessage / WhatsApp / OTT | None. End-to-end encrypted, so the network cannot see content (inference) | n/a |
| Email | None | t-mobile.com/scamshield (not mentioned) |
| Web links | Yes. Network blocklist (Safe Web Browsing) | t-mobile.com/scamshield |
| Payments | None | t-mobile.com/scamshield (not mentioned) |
| Identity/account | Yes. SIM swap and port-out protection | t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile |

### 2025-2026 changes
- **Early 2025:** The standalone Scam Shield app was folded into the T-Life app, under "Manage." Users reported protections not being on by default. T-Mobile said a spam spike at the time was unrelated. https://www.phonearena.com/news/t-mobile-quiet-app-change-might-be-why-your-phone-rings-off-the-hook_id169066 (Apr 1, 2025, updated Apr 3)
- **Mar 20, 2026:** T-Mobile Newsroom on X announced two new Scam Shield features, Safe Web Browsing and Scam Callback Protection. Safe Web Browsing checks network traffic against known malicious site lists. https://x.com/tmobilenews/status/2035042472305533024 (the date comes from decoding the post ID. The post body could not be fetched because robots blocked it, so the content is from the search snippet only.)
- **Nov 2, 2026:** The "Advancing Cybersecurity at T-Mobile" report says all customers get real-time network screening of calls, texts and browsing. https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile
- AI features in Scam Shield itself: none named on the product pages (checked 2026-11-07). T-Mobile describes machine learning on network data. https://www.slashgear.com/2200747/tmobile-report-spam-feature-effectiveness/
- Partnerships: none found for 2025-2026 consumer scam protection. The older McAfee Security for T-Mobile app exists (https://magentapulse.t-mobile.com/us/en/customer-support/devices/t-mobile-applications/mcafee-security-for-t-mobile-app). Its current status is UNVERIFIED.

### Gaps and complaints
- **(User complaints, Reddit, via PhoneArena)** Users said T-Life is hard to navigate, worried protection was not on by default, and noted that some calls still get through. https://www.phonearena.com/news/t-mobile-quiet-app-change-might-be-why-your-phone-rings-off-the-hook_id169066
- **(User complaints, T-Mobile Community forum)** Scam Shield broke after the T-Life move: blocking from recent calls spins forever, the Scam Shield link disappears, and support said there were no known issues. https://www.t-mobile.com/community/discussions/website-app/scam-shield/198344 (undated)
- **(Review roundup)** Results are inconsistent. Other complaints: a confusing app, legitimate calls blocked (false positives), and doubts that Premium is worth paying for. https://www.slashgear.com/2200747/tmobile-report-spam-feature-effectiveness/
- **(Competitor critique, Cape, labeled as biased)** Filters depend on known patterns, so new scam texts slip through. 7726 is reactive. Broad SMS blocking can catch OTP and 2FA texts. https://www.cape.co/blog/t-mobile-spam-blocker
- **Structural gaps (our analysis):** It gives a label with no explanation. There is no in-conversation analysis, no payment-moment intervention, and no recovery workflow. It cannot see E2EE channels.

---

## 2. Other carriers

### AT&T ActiveArmor
- **Free:** fraud and spam call blocking, data breach alerts, device security alerts, caller ID and reverse lookup. https://www.att.com/features/security-apps/
- **ActiveArmor Advanced, $7/mo:** identity and dark-web monitoring, safe browsing, public Wi-Fi protection, credit monitoring, up to $1M identity theft insurance, and lost wallet restoration. https://www.att.com/features/security-apps/
- **AI "digital receptionist" (pilot):** an in-network LLM agent answers calls, asks who is calling and why, judges spam and urgency, shows a live transcript, and lets the user take over. North Texas test only, with a wider rollout planned. https://dallasinnovates.com/personal-call-screening-att-is-testing-an-ai-digital-receptionist-with-select-north-texas-customers/ (Sep 16, 2025). Current GA status: UNVERIFIED.
- Spam text specifics are not described on the official page. UNVERIFIED.

### Verizon Call Filter
- **Base (free):** screens and auto-blocks spam calls, and lets you report numbers. https://www.verizon.com/solutions-and-services/add-ons/protection-and-security/call-filter/
- **Call Filter Plus:** caller name ID, personal block lists, spam lookup. https://www.verizon.com/solutions-and-services/add-ons/protection-and-security/call-filter/
- Plus price: not on the official page. Widely reported as about $3.99/mo per line. UNVERIFIED (the PIRG article could not be fetched: https://pirg.org/florida/?p=6867).
- Texts, AI, and payments are not covered on the official page.

---

## 3. OS / handset makers

### Google (Pixel, Android, Google Messages)
- **Call Scam Detection:** on-device, flags scam conversation patterns (for example fake bank reps asking for transfers, gift cards or PINs). It alerts with sound and haptics and offers "End call" or "Not a scam." Call content is not saved. https://9to5google.com/2025/02/26/pixel-scam-detection-messages-phone/ (Feb 26, 2025)
- **Messages Scam Detection:** on-device ML that moves conversational scams (package, job) to Spam & blocked. https://9to5google.com/2025/02/26/pixel-scam-detection-messages-phone/
- **Feb 25, 2026:** call Scam Detection comes to Galaxy S26 (US). Pixel regions are US, AU, CA, IN, IE and UK. Messages now uses on-device Gemini for complex conversational threats (job, pig butchering) on Pixel 10 and S26 in US, CA and UK. Audio is processed ephemerally and is not stored or sent. https://9to5google.com/2026/02/25/google-messages-scam-detection-gemini/
- **In-call financial app protection:** if you open a participating banking app while screen sharing on a call with an unknown number, Android warns you, offers one-tap end call and stop sharing, and forces a 30-second pause. US rollout began Dec 2025 with Cash App and JPMorganChase. UK, Brazil and India pilots are live, and P2P apps are being piloted. https://blog.google/security/android-expands-pilot-in-call-scam-protection-financial-apps/ (Dec 3, 2025)
- Coverage depends on the device and app: latest flagships, Google Phone and Messages apps only.

### Apple iOS 26
- **Call Screening:** builds on Live Voicemail and collects the caller's info before you choose to answer. **Messages:** unknown senders go to a separate silenced folder, where you can mark as known, ask for info, or delete. https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/ (Jun 9, 2025)
- "Ask Reason for Calling" setting: Settings > Apps > Phone > Screen Unknown Callers. Roaming calls are not screened. https://support.apple.com/111106
- This is identity-based screening (known vs unknown). Apple has no announced in-call scam-content analysis and no payment intervention (based on the sources above).

### Samsung
- **One UI 8 "Suspected Voice Phishing Call Alert":** on-device AI with yellow "suspected" and red "warning" in-call alerts, trained on 30,000+ Korean government voice-phishing records. South Korea only (Z Flip7/Fold7) at the time of writing. https://www.sammobile.com/news/samsung-details-voice-phishing-protection-galaxy-phones/ (Aug 21, 2025)
- **US:** Galaxy S26 gets Google's Scam Detection in the Samsung Phone app. https://9to5google.com/2026/02/25/google-messages-scam-detection-gemini/
- Smart Call (Hiya-powered caller ID) details: UNVERIFIED in this pass.

---

## 4. Third-party apps

### Hiya AI Phone
- An AI assistant answers unknown calls and asks for name and purpose. It analyzes call audio in real time for scams, flags AI-generated or deepfake voices, and gives transcripts and summaries. Free download, premium $9.99/mo, iOS and Android. https://businesswire.com/news/home/20250128511230/en/Hiya-Launches-First-AI-Call-Assistant-That-Stops-Live-and-Deepfake-Scams-in-Real-Time (Jan 28, 2025)

### Truecaller
- **AI Call Scanner:** the user taps a button mid-call, the call is bridged to Truecaller's line, and a voice sample is checked for AI cloning. Premium only, Android first, US first. https://inderes.fi/releases/truecaller-ab-truecaller-launches-the-worlds-first-ai-cloned-voice-detection (May 29, 2024)
- **Scam Feed:** a crowdsourced scam reporting feed (Apr 2025, India launch). https://www.indiatvnews.com/technology/news/truecaller-scamfeed-launches-to-fight-digital-frauds-report-and-warn-others-instantly-2025-04-29-987850
- SMS filtering (Android): UNVERIFIED in this pass.

### Robokiller
- Blocks spam calls and texts (claims 99%) using predictive analytics and audio fingerprinting. Answer Bots waste scammers' time. Free trial. Price is not on the homepage. https://www.robokiller.com/

### Norton Genie Scam Protection / Pro
- Safe SMS (AI reads text meaning), Safe Call (block or label), Safe Email (flags before opening), Safe Web, and a Genie AI Scam Assistant for one-tap guidance. Scam Support and Reimbursement comes only with Norton 360 with LifeLock Ultimate Plus (US ex-NY). Launched Feb 19, 2025. https://s25.q4cdn.com/670692841/files/doc_news/Norton-Launches-Enhanced-AI-Powered-Scam-Protection-Across-Cyber-Safety-Lineup-2025.pdf
- This is the closest thing to cross-channel coverage, but it is a paid security suite, has no carrier signals, and does not intervene at the payment moment.

---

## 5. Bank-side interventions (UK model)

- **Confirmation of Payee (CoP):** checks the payee name against the account before you send. It returns Match, Close match (shows the real name), or No match (contact the payee). https://www.ukfinance.org.uk/policy-and-guidance/guidance/confirmation-payee
- **APP fraud mandatory reimbursement, from Oct 7, 2024:** cost is split 50:50 between the sending and receiving firms. The optional excess is up to £100 and is not applied to vulnerable consumers. Banks must prove gross negligence to refuse. The consumer standard of caution includes heeding bank warnings and reporting promptly. https://www.psr.org.uk/news-and-updates/latest-news/news/psr-continues-to-take-bold-action-on-app-fraud-as-it-publishes-final-reimbursement-details-ahead-of-2024-implementation/
- The cap was cut to £85,000 per claim, down from the £415,000 proposed. The PSR estimates 99% of claims are still fully covered. https://www.dlapiper.com/insights/publications/2024/09/psr-confirms-app-fraud-reimbursement-level-to-be-reduced (Sep 27, 2024)
- **Payment delay:** HM Treasury consulted on letting PSPs delay suspicious payments by up to 4 days (consultation closed Oct 4, 2024). https://www.dlapiper.com/insights/publications/2024/09/psr-confirms-app-fraud-reimbursement-level-to-be-reduced. Whether and when it was enacted: UNVERIFIED in this pass.
- **Why it matters for us:** "heed warnings" is now a legal factor in UK reimbursement. Warnings and friction at the payment moment are a proven intervention category, and the US has no equivalent mandate. That is the gap for a carrier plus bank handoff.

---

## 6. Gap table

Legend: Y = covers it, P = partial, N = none. "During" means while the scam interaction is live (on the call, in the chat, or at the payment screen). "After" means reporting, recovery, or reimbursement.

| Product | Before | During | After | Call | SMS | RCS / iMessage | Email | Web | Payment | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| T-Mobile Scam Shield (free + Premium $4) | Y | P (ring-time label only) | P (7726 report) | Y | Y | P / N (RCS UNVERIFIED) | N | Y | N | t-mobile.com/scamshield ; t-mobile.com/benefits/scam-shield |
| AT&T ActiveArmor (+ Advanced $7) | Y | P (LLM receptionist pilot) | P (ID insurance, restoration, paid) | Y | P (UNVERIFIED) | N | N | P (paid) | N | att.com/features/security-apps ; dallasinnovates.com (Sep 2025) |
| Verizon Call Filter / Plus | Y | N | N | Y | N (not on page) | N | N | N | N | verizon.com/.../call-filter |
| Google Pixel / Android Scam Detection | Y | Y (live call analysis; banking app warning + 30s pause) | P (report, block) | Y | Y | Y (Google Messages) / N | N | P (UNVERIFIED, Chrome not checked) | P (in-call bank app warning only) | 9to5google 2025-02-26 ; 9to5google 2026-02-25 ; blog.google 2025-12-03 |
| Apple iOS 26 | Y (screen unknown callers and senders) | N | N | Y | Y (unknown-sender folder) | Y (iMessage, identity-based) | N | N (not checked) | N | apple.com/newsroom 2025-06 ; support.apple.com/111106 |
| Samsung One UI 8 | P | Y (Korea only; US via Google on S26) | N | Y | P (via Google Messages) | P / N | N | N | N | sammobile 2025-08-21 ; 9to5google 2026-02-25 |
| Hiya AI Phone ($9.99) | Y | Y (real-time scam + deepfake) | P (transcripts, summaries) | Y | N | N | N | N | N | businesswire 2025-01-28 |
| Truecaller | Y | P (user-triggered voice-clone check) | P (Scam Feed reporting) | Y | P (UNVERIFIED) | N | N | N | N | inderes.fi 2024-05-29 ; indiatvnews 2025-04-29 |
| Robokiller | Y | P (Answer Bots occupy the scammer) | N | Y | Y | N | N | N | N | robokiller.com |
| Norton Genie Scam Protection / Pro | Y | P (on-demand assistant) | Y (reimbursement, top tier only) | Y | Y | N (UNVERIFIED) | Y | Y | P (after-the-fact only) | Norton press release 2025-02-19 |
| UK banks (CoP + warnings + APP reimbursement) | P (warnings) | Y (CoP, warnings at payment) | Y (mandatory reimbursement, £85k cap) | N | N | N | N | N | Y | ukfinance.org.uk ; psr.org.uk ; dlapiper.com |

**What the table shows**
- "Before" is crowded. Every product blocks or labels.
- "During" exists only on-device (Google, Samsung) or in third-party call apps (Hiya, Truecaller), and only for calls. There is no "during" protection for text-led scams in which the victim is mid-conversation and about to pay.
- "After" is nearly empty in the US outside paid identity bundles. No carrier offers a guided recovery workflow.
- No row covers the scam as one journey across channels (text, then callback, then payment, then recovery).
- No product shows an explanation or confidence for its verdict. All of them output a label.

---

## 7. T-Mobile statements to echo (2025-2026)

| Date | What | URL |
|---|---|---|
| Nov 2, 2026 | "Advancing Cybersecurity at T-Mobile" report. All customers get real-time network screening of calls, texts and browsing. 160B+ unwanted calls blocked since Mar 2017. Nearly 3B scam and spam texts blocked in 2025. Scam and spam messages up nearly 50% in 2025 vs 2024. Hundreds of millions of scam and spam calls flagged weekly. SIM swaps down 99%+ since 2022. Preparing for AI-enabled fraud and non-human identities (AI agents, bots) through adversarial AI testing and a honeypot program. | https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile (also https://investor.t-mobile.com/news-releases/news-release-details/t-mobile-opens-its-cybersecurity-transformation-new-report) |
| Nov 2, 2026 | Mark Clancy (SVP, Information Security Officer) said security ultimately comes down to protecting people, and that the work never has a finish line. One short quote: "cybersecurity is about protecting people." | same as above |
| Nov 2, 2026 | Jeff Simon (EVP & CIO): phishing-driven credential compromise among T-Mobile staff is down 99%+, because attackers never stop moving. | same as above |
| Mar 20, 2026 | T-Mobile Newsroom announced Safe Web Browsing and Scam Callback Protection as new Scam Shield features. | https://x.com/tmobilenews/status/2035042472305533024 |
| Early 2025 | Scam Shield moved into the T-Life app. | https://www.phonearena.com/news/t-mobile-quiet-app-change-might-be-why-your-phone-rings-off-the-hook_id169066 |
| Feb 27, 2024 | Over 19B scam calls blocked in 2023 (older baseline). | https://www.t-mobile.com/news/un-carrier/t-mobile-report-customers-protected-from-over-19-billion-scam-calls-in-2023 |

**How to use these in the pitch:** "T-Mobile already stops billions of threats at the network. Its own Nov 2026 report says scam messages rose about 50% last year and that AI-driven fraud is next. We build the layer for the scams that still get through. It explains, guides and acts during and after the threat, and it plugs into the Scam Shield and T-Life signals T-Mobile already has."

---

## 8. Gaps we can own

1. **One incident, many channels.** Every competitor works one channel at a time. Our agent links a smishing text, the callback number (Callback Protection already exists), the URL, and the payment request into one incident timeline with a single risk score. Grounded in table: no row is Y across SMS, call, web and payment.
2. **"During" for text-led and payment-moment scams in the US.** Only Google's in-call banking warning touches the payment moment, and only for calls plus screen sharing on Android. Our agent adds an opt-in "pause and verify" step. When risk is high, it holds a mock payment (Capital One Nessie), proposes a 30-second cool-off, and pings a trusted contact. This borrows the UK and Google friction model. Grounded in table: the Payment column is N for every US carrier.
3. **"After" as a guided recovery plan.** Carriers stop at 7726, and Norton puts recovery behind its top tier. Our agent generates a step-by-step plan: lock the SIM (T-Mobile SIM Protection exists), prefill a report for ReportFraud.ftc.gov or IdentityTheft.gov, give a bank call script, and list passwords to rotate. It tracks completion. Grounded in table: the After column is mostly P or N.
4. **Explain it, with honest confidence.** All competitors output a bare label ("Scam Likely"). T-Mobile's top complaints are false positives and an opaque app. We show why (the red flags found), how sure we are, and the next step, and let users dispute a verdict. Grounded in complaints: SlashGear, Cape, and PhoneArena (Reddit).
5. **User-initiated check for content the network can't see.** iMessage, WhatsApp and other E2EE channels are invisible to Scam Shield. Advanced on-device detection only runs on the newest Pixel and S26. A "forward or screenshot it to the agent" flow (multimodal Nemotron) works on any phone, iPhone included, with no message content stored. Grounded in table: the RCS/iMessage column is N or P for carriers.

---

## Not verified / open items
- Which T-Mobile plans include Scam Shield Premium at no extra cost.
- Whether T-Mobile filters RCS spam (the only source is a competitor blog). T-Mobile's official page says SMS and MMS only.
- Verizon Call Filter Plus price (about $3.99 is reported but not confirmed on the official page).
- Whether AT&T's digital receptionist reached general availability after the Sep 2025 pilot.
- Whether the UK 4-day suspicious payment delay power was enacted, and when.
- Truecaller and Samsung Smart Call SMS features. Chrome and Safari fraudulent-site warnings were not researched.
- The Mar 20, 2026 T-Mobile X post content comes from the search snippet. The date was decoded from the post ID.
