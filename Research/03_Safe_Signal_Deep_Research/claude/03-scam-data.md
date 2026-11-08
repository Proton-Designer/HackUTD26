# 03 - Scam landscape data (Safe Signal / HackUTD 2026)

Compiled 2026-11-07. Every figure has a year and a source. UNVERIFIED = not confirmed in a primary or credible source.

## TL;DR
1. US consumers reported losing **$15.9B to fraud in 2025** (about 3M reports, up from $12.5B in 2024). Text was the **#1 contact method by number of reports**. Social media was #1 by dollars ($2.1B). Source: FTC, 2026.
2. FBI IC3 2025: **$20.9B lost, 1,008,597 complaints**. People 60+ lost **$7.7B** (201,266 complaints). AI-related complaints: 22,364, with **$893M** lost.
3. Top 5 FTC text scams (2024 data, latest spotlight): fake package delivery, fake job/task, fake bank/Amazon fraud alert, unpaid toll, "wrong number". Together they made up about **half** of all text fraud reports. Text-scam losses were **$470M in 2024**, and FTC says text losses rose **61% in 2025**.
4. AI voice cloning is now in official guidance: FCC 2024 ruling, FBI PSAs (Dec 2024, May 2025), FTC 2023 alert. Hard loss numbers are thin outside the IC3 AI figure ($893M).
5. Seed data: UCI SMS Spam (CC BY 4.0) and Mishra & Soni smishing (CC BY 4.0, 638 smishing messages) are both safe for a hackathon. Nazario phishing corpus is CC BY 4.0. PhishTank works best with a free key and has a Cisco EULA.

**Important caveat:** I could not find a published *Consumer Sentinel Network Data Book 2025* PDF. ftc.gov/data still links only the 2024 edition, and the expected 2025 PDF URL returned an error. The 2025 headline numbers below come from FTC testimony (Mar 25, 2026), an FTC Data Spotlight (Apr 2026), an FTC press release (Jun 2026), and the FTC older-adults report (Oct 2026). For the full category, contact, payment and age tables I give the **2024 Data Book** as the latest full edition.

---

## 1. FTC Consumer Sentinel

### 1a. 2025 headline figures (calendar 2025)
| Metric | Value | Source |
|---|---|---|
| Total reported fraud losses | $15.9B (2025), up from $12.5B (2024) | FTC JEC testimony, Mar 25 2026: https://www.ftc.gov/system/files/ftc_gov/pdf/ftc-testimony-jec-hearing-on-the-rising-scam-economy.pdf |
| Fraud reports | ~3.0M (2025), up from 2.6M (2024) | same |
| Growth since 2020 | ~430% rise in reported losses; six straight years of increases, driven by $100K+ loss reports | same |
| Estimated true cost (incl. unreported) | up to $195.9B (2024 estimate) | same |
| Investment scams | >$7.9B (2025), about half of all losses; average loss >$10K | same |
| Imposter scams | >1M reports, >$3.5B (2025); most reported category since 2020; about 1 in 3 fraud reports | same; FTC press release Jun 2026: https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-data-show-people-reported-losing-3-point-5-billion-imposter-scams-2025 (figures via BleepingComputer write-up: https://bleepingcomputer.com/news/security/ftc-warns-of-record-35-billion-losses-to-imposter-scams-in-2025) |
| Business impersonators | ~$1B (2025); bank impersonation was the costliest | FTC Jun 2026 release (via BleepingComputer, above) |
| Government impersonators | ~$920M (2025) | same |
| Top contact method by # reports | Text message (2025) | FTC JEC testimony 2026 |
| Top contact method by $ lost | Social media, $2.1B (2025), about 8x the $261M in 2020 | FTC Data Spotlight Apr 2026: https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2026/04/reported-losses-scams-social-media-eight-times-higher-2020 |
| Payment methods | Bank payments = highest $ losses, crypto #2; credit card = most often reported | FTC JEC testimony 2026 |
| Bank transfer + crypto combined | >$4B (2025) | AARP summary, Apr 2026: https://www.aarp.org/money/scams-fraud/fbi-ftc-report-2025-losses.html |
| Credit cards + payment apps | $736.9M (2025) | AARP summary, Apr 2026 (same URL) |
| Losses, age 50+ vs younger | $4.3B (50+) vs $2.3B (younger) (2025) | AARP summary, Apr 2026 (same URL). Not checked against FTC |

**Social-media spotlight details (2025, FTC Apr 2026 spotlight URL above):**
- Investment scams that started on social media: $1.1B. Romance scams from social media: $298M; nearly 60% of romance losers said it started there.
- Shopping is the most reported social-media scam. Over 40% of those who lost money said it began with an ad.
- About 1 in 3 job-scam losers said it started on social media.
- Facebook had the most losses, then WhatsApp, then Instagram.
- Share of loss reports by contact method, as extracted: social media ~28-30%, website/app 31%, phone 11%, email 10%, text 7%. Website/app at 31% being above social media looks odd given that social is called the top method. Check the spotlight chart before using the ranking (partly UNVERIFIED).
- Share of each age group's loss reports that started on social media: 18-29 40%, 30-39 32%, 40-49 32%, 50-59 32%, 60-69 29%, 70-79 23%, 80+ 14%.

### 1b. Older adults (60+), calendar 2025
Source: FTC, *Protecting Older Consumers 2025-2026*, Oct 19 2026: https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf
- 60+ reported losses: **>$3B in 2025** (about $2.4B in 2024). Estimated true losses: $13.3B to $119.5B.
- About 123K of the ~470K age-stated reports from people 60+ showed a loss. Median loss for 60+ was about $900. **Median loss for 80+ was $2,000**, up 21% from 2024.
- **Losses of $100K or more were 6% of older adults' loss reports but 70% of their dollars.**
- Government impersonation was the #2 loss category for 60+. Older adults made up 92% of FTC-impersonation losses, 85% of SSA-impersonation losses and 75% of FBI-impersonation losses. All-ages losses, via a secondary write-up: FTC impersonation $161M, SSA $144M, FBI $28M (https://www.recordinglaw.com/news/ftc-older-adults-fraud-report-2026/; dollar figures UNVERIFIED against the PDF).
- Tech support: older adults were 324% more likely to report losing money (secondary write-up, same URL).
- Payment: bank transfers and crypto lost the most dollars. Gift cards were the top method for tech support, romance, family impersonation and prize scams.
- **Median loss when the scam started by phone: $3,000. When it started on social media: $599.** Aggregate text-scam losses rose 61% vs 2024.
- No mention of AI or voice cloning in this report.

### 1c. 2024 Data Book (latest full edition), calendar 2024
Source: https://www.ftc.gov/system/files/ftc_gov/pdf/csn-annual-data-book-2024.pdf and press release Mar 10 2025: https://www.ftc.gov/news-events/news/press-releases/2025/03/new-ftc-data-show-big-jump-reported-losses-fraud-125-billion-2024
- 2,600,678 fraud reports. $12.54B lost. 38% reported losing money (27% in 2023). Median loss $497.
- Contact methods by # reports: email #1, phone #2, text #3. Email: 25% of reports, $502M lost, $600 median.
- Bank transfer $2.09B and crypto $1.42B lost the most. Together they exceeded all other methods combined. Credit card was the most frequently reported method.
- Government imposters: $789M (2024). Job and employment agency scams: $501M (2024), up from $90M in 2020.

| Rank | Category (2024) | Reports | % lost $ | Total loss | Median |
|---|---|---|---|---|---|
| 1 | Imposter scams | 845,806 | 22% | $2.95B | $800 |
| 2 | Online shopping | 383,441 | 76% | $432M | $130 |
| 3 | Business & job opportunities | 126,217 | 36% | $751M | $2,250 |
| 4 | Investment | 118,960 | 79% | $5.70B | $9,196 |
| 5 | Internet services | 118,261 | 28% | $164M | $300 |
| 6 | Prizes/sweepstakes | 97,350 | 22% | $351M | $1,000 |
| 7 | Telephone & mobile services | 92,520 | 39% | $56M | $240 |

The age and contact-method tables in the 2024 PDF did not extract cleanly. Read pages directly or use https://www.ftc.gov/exploredata if you need age breakdowns.

### 1d. FTC Data Spotlight: Top text scams (2024 data, published Apr 14 2025)
https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2025/04 (PDF: https://www.ftc.gov/system/files/ftc_gov/pdf/spotlight-top-text-scams.pdf)
- $470M lost to text scams in 2024, more than 5x 2020. 11% of text-scam reports showed a loss (5% in 2020).
- Top 5 by reports, together about 50% of text fraud reports. **The FTC does not publish an individual share for each.**
  1. Fake package delivery problem (USPS lookalike, small "redelivery fee")
  2. Fake job offers / task scams
  3. Fake fraud alerts (bank or Amazon; reply YES/NO or call; "move your money to keep it safe")
  4. Unpaid toll notices
  5. "Wrong number" texts leading to friendship or romance, then a fake investment platform
- I found no newer text-scam spotlight covering 2025 data. The 61% rise for 2025 comes from the Oct 2026 older-adults report.

---

## 2. FBI IC3 2025 Internet Crime Report
Source: https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf (released Apr 2026, per press coverage)
- **1,008,597 complaints, $20.877B lost** (+26% vs 2024, per AARP, URL above).
- **60+: 201,266 complaints, $7.748B lost** (about +60% vs 2024 per AARP). The 2025 report folds in the elder figures. I did not find a separate 2025 Elder Fraud Report PDF (UNVERIFIED whether one exists).
- Crypto-related: 181,565 complaints, $11.366B lost.
- **AI-related: 22,364 complaints, $893.3M lost.** AARP says $352M of that came from older adults.

| Crime type (2025) | Complaints | Losses |
|---|---|---|
| Phishing/spoofing | 191,561 | $215.8M |
| Extortion | 89,129 | $122.5M |
| Investment | 72,984 | $8.649B |
| Non-payment/non-delivery | 56,478 | $503.4M |
| Tech/customer support | 47,794 | $2.135B |
| Government impersonation | 32,424 | $797.9M |
| BEC | 24,768 | $3.047B |
| Employment | 24,688 | $362.9M |
| Confidence/romance | 23,159 | $929.3M |

Related: in 2024 the IC3 Recovery Asset Team froze $469M of $651.5M reported in Financial Fraud Kill Chain cases (FTC JEC testimony 2026). This is a useful talking point for intervening early.

---

## 3. International
- **GASA + Feedzai, Global State of Scams 2025** (Oct 7 2025; 46,000 adults, 42 markets): 57% met a scam in the past year, 23% lost money, about **$442B lost globally**. Victims by type: shopping 54%, investment 48%, unexpected money 48%. https://gasa.org/knowledge-base/blog/global-scams-on-the-rise-over-half-of-adults-worldwide-report-scam-encounters ; $442B figure: https://www.feedzai.com/blog/gasa-global-state-of-scams-report/
- **UK Finance Annual Fraud Report 2026** (covers 2025): £1.28B total (+4%). APP fraud: 248,070 cases, £576.4M (+19%). Investment APP: £221.5M (+40%). Purchase scams: 71% of APP cases, £118.1M. Romance: £39.2M. **66% of APP cases started online and 17% through telecoms. Telecoms made up 28% of APP losses.** Banks reimbursed 61% of APP losses. PDF: https://www.ukfinance.org.uk/system/files/2026-06/UK%20Finance%20Fraud%20Report%202026.pdf (figures via https://www.neopay.co.uk/uk-finance-fraud-report-2026-payment-fraud-losses-reach-1-28-billion/)
- **BBB Scam Tracker Risk Report 2025:** investment/crypto and employment were the two riskiest scam types. More than 77% of people targeted by investment/crypto scams lost money. Employment scams went from 14.4% to 15.8% of reports. https://bbbmarketplacetrust.org/riskreport/
- Ofcom / ACMA Scamwatch: not researched (time).

---

## 4. Voice-clone and AI-enabled scams, 2024-2026
- **FCC Declaratory Ruling (FCC 24-17, Feb 8 2024):** AI-generated voices count as "artificial" under the TCPA, so AI-voice robocalls need prior consent and state AGs can sue. https://cooley.com/news/insight/2024/2024-02-15-fcc-ai-generated-robocalls-illegal-under-the-tcpa
- **FBI PSA I-120324-PSA (Dec 3 2024):** criminals use generative AI for text, images, cloned voices of relatives asking for emergency money, and live deepfake video of executives. The FBI recommends a family secret word. https://www.ic3.gov/PSA/2024/PSA241203
- **FBI PSA I-051525-PSA (May 15 2025):** since Apr 2025, smishing plus AI-voice vishing campaigns have impersonated senior US officials. Attackers build rapport, move the target to another app, then steal credentials and reuse the accounts against the target's contacts. https://www.ic3.gov/PSA/2025/PSA250515
- **FTC consumer alert (Mar 20 2023):** scammers clone a relative's voice from a short online clip and ask for wire, crypto or gift-card PINs. FTC advice: hang up and call the person back. https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes
- **IC3 2025:** $893M in AI-related losses (see section 2). This is the best hard number.
- Industry figures on deepfake call growth (Pindrop, vendor blogs) are vendor marketing and I did not check them. Treat them as UNVERIFIED and avoid them in the pitch.

---

## 5. Script patterns for 12 scam types (openers are original examples for synthetic data)

| # | Type | Representative opener (synthetic) | Escalation | Payment demanded | Red flags | Source |
|---|---|---|---|---|---|---|
| 1 | Package delivery | "USPS: Your parcel is on hold, address incomplete. Update within 12h: usps-redeliver[.]top" | Lookalike site asks for a $1-3 "redelivery fee", then card number, SSN | Card entered on phishing site | Unexpected text, odd domain, tiny fee, deadline | FTC text spotlight 2025 (above) |
| 2 | Unpaid toll | "NTTA notice: unpaid toll balance $6.89. Pay by today to avoid a $50 late fee: ntta-pay[.]info" | Site captures card number, then follow-up texts | Card on phishing site | Mimics state toll name, sender number changes, late-fee threat | FBI PSA I-041224-PSA: https://www.ic3.gov/PSA/2024/PSA240412 ; FTC spotlight |
| 3 | Fake bank fraud alert | "Chase Alert: Did you try a $1,249.00 purchase at Best Buy? Reply YES or NO" | Reply triggers a call from the "fraud dept", then an OTP request, then "move funds to a safe account" | Bank transfer/wire, Zelle, sometimes crypto ATM or cash courier | Asks for OTP, tells you to move money, caller ID spoofed | FTC spotlight; FTC imposter release Jun 2026 |
| 4 | Wrong number / pig butchering | "Hi Jenny, still on for coffee Thursday?" ... "Oh sorry, wrong number! Where are you based?" | Small talk for weeks, move to WhatsApp, photos of a lavish life, "my uncle's trading app", small win paid out, then large deposits, then "tax/fee" to withdraw | Crypto (USDT) to the fake platform, bank wire | Stranger who stays chatty, moves apps, guaranteed returns, withdrawal fees | FTC spotlight; https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams |
| 5 | Job / task | "Hi, I'm Ava from a recruiting firm. Remote part-time role, $300-$800/day rating apps. Interested?" | Training on a platform, tasks earn "commission", account goes negative, you must deposit to unlock "combo tasks", withdrawal blocked | Crypto deposits, sometimes payment apps | Unsolicited offer, pay to work, vague tasks, WhatsApp/Telegram | FTC spotlight; https://consumer.ftc.gov/articles/job-scams (URL UNVERIFIED) |
| 6 | Government impersonation | "This is Officer Grant, SSA Office of Inspector General. Your SSN is linked to a money laundering case." | Badge number, then threat of arrest or frozen benefits, transfer to a "federal agent", then "protect your assets" | Gift cards, wire, crypto ATM, cash or gold handed to a courier | Agency calling to ask for money, secrecy, spoofed caller ID | https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam |
| 7 | Tech support | Pop-up: "Windows Defender: Your PC is infected. Call Microsoft Support at 1-8xx-xxx-xxxx now" | Remote-access tool, fake virus scan, "fix" fee or fake refund overpayment, handoff to a fake bank or government agent | Gift cards, wire, crypto, payment apps | Pop-up with a phone number, remote access request, overpaid "refund" | https://consumer.ftc.gov/articles/how-spot-avoid-and-report-tech-support-scams |
| 8 | Romance | "Your smile in your profile made my day. I'm an engineer on an offshore rig, rarely online." | Daily messages, moves off the app, avoids video calls, emergency (customs, medical, ticket) or crypto pitch | Wire, gift-card PINs, payment apps, crypto | Never meets, moves platforms fast, asks for money | https://consumer.ftc.gov/articles/what-know-about-romance-scams |
| 9 | Grandparent / voice clone | Call in the grandchild's cloned voice: "Grandma, it's me, I crashed the car and I'm in jail. Please don't tell Mom." | A "lawyer" or "officer" takes over, bail amount, gag order, courier pickup or second demand | Cash courier, gift cards, wire, crypto | Urgency plus secrecy, voice slightly off, refuses callback | FTC alert Mar 2023; FBI PSA Dec 2024 (above) |
| 10 | Marketplace overpayment | "Is the couch still available? I'll pay $200 over asking for movers. Sending a cashier's check." | Check arrives for more than the price, buyer asks you to refund the difference before the check bounces. Variant: fake "Zelle business upgrade" email | Seller refunds by Zelle, gift card, money order, wire | Overpayment, refund request, buyer won't meet | https://consumer.ftc.gov/articles/how-spot-avoid-and-report-fake-check-scams |
| 11 | Crypto investment | Social-media ad or DM: "Our AI trading bot made members 4.2% daily. Free signal group, limited seats." | Signal group, fake dashboard showing gains, larger deposits, withdrawal "fee/tax", then a "recovery service" scam | Crypto (often via Bitcoin ATM), wire | Guaranteed returns, celebrity endorsement, fee to withdraw | FTC crypto article (above); FTC social spotlight 2026 |
| 12 | QR / quishing | Sticker on a parking meter: "Scan to pay - ParkFast". Or email: "Package failed, scan to reschedule" | QR opens a lookalike payment or login page, captures card or credentials, sometimes malware | Card or credentials on the fake page | QR sticker on top of another, unsolicited QR, misspelled URL | https://consumer.ftc.gov/consumer-alerts/2023/12/scammers-hide-harmful-links-qr-codes-steal-your-information |

Cross-cutting signals for a detector:
- Urgency or a deadline
- Secrecy ("don't tell anyone")
- Moving to another app
- Requests for an OTP or remote access
- "Move money to protect it"
- Payment by gift card, crypto, crypto ATM, wire or courier
- Lookalike domains (.top, .info, hyphenated brand names)
- Caller ID claiming a government agency or bank

---

## 6. Seed datasets
| Dataset | Size | License | Link | Restrictions |
|---|---|---|---|---|
| UCI SMS Spam Collection (Almeida & Hidalgo, 2011) | 5,574 SMS (about 4,827 ham, 747 spam) | CC BY 4.0 | https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip (DOI 10.24432/C5CC84) | Attribution only. Old (2011-12) and UK/Singapore-heavy |
| Mishra & Soni SMS Phishing Dataset (Mendeley, 2022) | 5,971 SMS: 4,844 ham, 489 spam, 638 smishing; flags for URL, email, phone | CC BY 4.0 | https://data.mendeley.com/datasets/f45bkkt8pr/1 (DOI 10.17632/f45bkkt8pr.1) | Attribution only |
| Smishing Dataset I (Timko & Rahman, smishtank.com, 2024) | 1,090 smishing samples | Paper is CC BY-NC-SA 4.0; dataset license not stated (UNVERIFIED) | https://arxiv.org/abs/2402.18430 | Treat as non-commercial. Most current US smishing |
| Kaggle mirror of UCI SMS Spam (uciml) | ~5,572 rows, spam.csv (UNVERIFIED) | Not confirmed (UNVERIFIED) | https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset | Kaggle login required. Use the UCI original instead |
| Nazario phishing corpus | mbox files from 2005-07 plus yearly folders 2015-2025 | CC BY 4.0 (LICENSE.txt) | https://monkey.org/~jose/phishing/ | Attribution. Email only, not SMS |
| PhishTank | Live verified phishing URLs, updated hourly; CSV/JSON/XML | Cisco terms of use; commercial use not confirmed (UNVERIFIED) | https://data.phishtank.com/data/online-valid.json (with free key: /data/&lt;key&gt;/online-valid.json.bz2); register: https://phishtank.org/api_register.php | A few downloads per day without a key. Set a descriptive User-Agent |

Hackathon suggestion: train on UCI + Mishra & Soni. Use Nemotron to generate 2024-26 style US variants of the 12 script patterns above (toll, USPS, task, wrong number). Use PhishTank URLs as realistic link payloads, defanged.

---

## UNVERIFIED / gaps
- No 2025 Consumer Sentinel Data Book PDF found. The full 2025 category, contact, payment and age tables are unconfirmed.
- No FTC per-type share for the top 5 text scams. Only "about half combined".
- The FTC 2025 dollar loss for text messages is not published in what I found. Only the +61% change is.
- AARP's $4.3B (50+) and $736.9M (cards/apps) are not checked against FTC primary data.
- All-ages FTC, SSA and FBI impersonation dollar figures come from a secondary write-up.
- No separate IC3 2025 Elder Fraud Report found.
- Kaggle license, PhishTank commercial terms and the smishtank dataset license are unconfirmed.
- Ofcom and ACMA were not covered.
