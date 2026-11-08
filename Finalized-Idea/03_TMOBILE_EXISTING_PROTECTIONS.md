# T-Mobile's Existing Scam, Spam and Fraud Protections: Inventory for HackUTD 2026 "Safe Signal"

Prepared Nov 7, 2026. Every claim has a source URL. **UNVERIFIED** marks anything not confirmed on a primary or reputable source. **CONTRADICTION** marks places where T-Mobile pages disagree with each other.

---

## TL;DR: top 8 findings

1. **All of T-Mobile's call protection works on metadata and number reputation. None of it uses call content.** In its own Nov 2026 report, T-Mobile says it identifies scam calls "by analyzing activity and calling patterns in real time." Scam ID, Scam Block, Potential Spam and Callback Protection all check the number and its behaviour, not what is said. We found no T-Mobile product that listens to, transcribes or scores the audio of a call for scam detection. [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf)
2. **T-Mobile already has an in-network AI voice agent, but it only translates.** Live Translation (dial `*87*` during a call; beta opened spring 2026) runs agentic AI inside the network. T-Mobile told The Register that "AI isn't listening in on calls that aren't being translated" and "We do not save call recordings or transcripts." The CTO said, "We don't listen to customers' calls." This shows the platform can handle real-time in-call AI. It also shows T-Mobile has publicly committed to not listening, which our product would need to address. [The Register](https://www.theregister.com/2026/02/11/tmobile_network_ai_translate_live_calls), [CNET](https://www.cnet.com/tech/mobile/t-mobile-opens-beta-for-network-based-live-language-translation/)
3. **Free Scam Shield covers the "before" stage well.** It includes Scam ID ("Scam Likely", on by default), Scam Block (opt-in, `#662#`), Potential Spam tagging (on by default), Caller ID (opt-in, `#436#`), Caller Verified (STIR/SHAKEN), Scam Callback Protection (on by default), network SMS/MMS spam blocking and Safe Web Browsing (DNS-level). Scam Shield Premium costs **$4 per line per month on T-Mobile** and **$2 per line per month on Metro**. [T-Mobile](https://www.t-mobile.com/benefits/scam-shield), [Metro FAQ](https://www.metrobyt-mobile.com/benefits/scam-shield/faq)
4. **Headline figures from the Nov 2, 2026 report:**
   - more than 160B unwanted calls identified or blocked since March 2017
   - about 29B inbound calls tagged as scam or spam in 2025
   - 428M+ "Potential Spam" tags in 2025 from new AI/ML systems, a tenfold increase over 2024
   - more than 800 scam calls identified or blocked every second
   - about 3B spam or scam SMS/MMS blocked in 2025, with about 50% more scam and spam messages than in 2024
   - 67M+ Scam Callback Protection warnings played
   - about 99% of Scam Block users never turn it off
   - 99% fewer successful SIM swaps since 2022
   - 100B+ malicious DNS requests blocked
   Also: **Scam Callback Protection is the only "during" intervention.** Before an outbound call to a number on the Scam Likely list connects, it plays an audible warning. It is a list lookup, not content analysis.
5. **First Orion is T-Mobile's analytics vendor.** In October 2026 First Orion described itself as "T-Mobile's analytics engine." It also runs T-Mobile for Business branded calling (INFORM, Mobile Originated Branded Calling, Business Number ID). Hiya historically powered the older Name ID app. [First Orion PR](http://firstorion.com/press-releases/first-orion-spam-watchlist-launch)
6. **Account protections are strong but opt-in, and the pages contradict each other on who is eligible.** SIM Protection, Port Out Protection, biometric verification, digital ID scan and a T-Life security pop-up all exist. One support page says SIM Protection is "Not available to T-Mobile for Business, T-Mobile Prepaid, or Metro." Other pages give Prepaid and Business setup steps, and Metro advertises its own "SIM Change Protection."
7. **Competitors have moved further on AI.** AT&T has been testing a network-based agentic **AI "digital receptionist"** since September 2025. It answers unknown callers, asks who they are and why they are calling, shows a live transcript, and disconnects calls that look like fraud. We found no comparable AI screening or answering product at Verizon or T-Mobile. Network AI that answers scam calls is therefore not new to the industry, but T-Mobile has nothing like it. Turning that conversation into scammer intelligence (a decoy) appears to be unclaimed by any carrier.
8. **DevEdge network APIs exist but are gated.** These include Network Fraud Signals (18+ signals, including SIM swap), SIM Swap (CAMARA), SIM-based Network Authentication, and Call Protection (Brand Call Protect and Inbound Call Verify). Access requires a lead form, a business review and an **NDA**. DevEdge says it "is not fully self-service at initial entry," so a hackathon team cannot simply sign up and call these APIs. [DevEdge FAQ](https://devedge.t-mobile.com/support/faq)

---

## Master feature table

Abbreviations: "Before / During / After" is when the feature acts relative to a threat. PP = postpaid, PrP = T-Mobile Prepaid, TFB = T-Mobile for Business.

| Feature | What it does | B / D / A | Default or opt-in | Who's eligible | Price | Source |
|---|---|---|---|---|---|---|
| Scam ID ("Scam Likely") | Network labels suspected scam calls before they connect, using threat databases and behavioural algorithms; catches spoofing | Before | **Default on**; "No action is required" | All T-Mobile customers; Metro; Mint (as "Scam Screener") | Free | [benefits](https://www.t-mobile.com/benefits/scam-shield), [glossary](https://www.t-mobile.com/news/understanding-t-mobiles-cybersecurity-definitions), [Mint](https://www.mintmobile.com/help/what-is-scam-screener/) |
| Scam Block | Network ends Scam Likely calls before the phone rings. On: `#662#`. Off: `#632#`. Status check: `#787#` | Before | **Opt-in** | T-Mobile PP and PrP (PrP by dial code, store or 611); Metro; DIGITS via 611 | Free | [scamshield](https://www.t-mobile.com/scamshield), [2017 PR](https://www.t-mobile.com/news/press/scam-block), [FCC guide](https://www.fcc.gov/sites/default/files/robocall_protection_guide_tmobile.pdf) |
| Potential Spam and category labels | Labels such as "Potential Spam", "Telemarketing" and "Political" applied in the network; new AI/ML models tagged 428M+ calls in 2025 | Before | **Default on** | All T-Mobile customers | Free | [customers/scam-shield](https://www.t-mobile.com/customers/scam-shield), [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud) |
| Send Potential Spam to voicemail | Routes Potential Spam calls straight to voicemail | Before | Opt-in in T-Life | PP (T-Life) | Free | [customers/scam-shield](https://www.t-mobile.com/customers/scam-shield) |
| Caller ID (formerly Name ID) | Shows caller name for numbers not in contacts; some details come from WhitePages profiles | Before | **Opt-in** (`#436#`, T-Life, store, 611) | All T-Mobile customers with a capable device; Metro; TFB with 12 or fewer lines | Free | [scamshield](https://www.t-mobile.com/scamshield), [business](https://www.t-mobile.com/business/solutions/call-protection) |
| Caller Verified (STIR/SHAKEN) | Shows that the calling number is authenticated; launched in 2019 and works across carriers | Before | Default on capable devices | All customers with a capable device | Free | [2019 PR](https://www.t-mobile.com/news/press/caller-verified-note9), [2020 PR](https://www.t-mobile.com/news/un-carrier/scam-shield-protects-customers-from-scams-robocalls) |
| Neighborhood-spoofing protection | Network stops calls spoofing your area code and prefix | Before | Default | All customers | Free | [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud) |
| Scam Callback Protection | Checks **outbound** calls against the Scam Likely list and plays an audio warning before the call connects; 67M+ warnings played | **During** (outbound) | **Default on**; "No action is required" | T-Mobile; Mint (confirmed); Metro **UNVERIFIED** | Free | [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf), [customers/scam-shield](https://www.t-mobile.com/customers/scam-shield), [Mint](https://www.mintmobile.com/help/what-is-scam-screener/) |
| Personal block list and Allow list | Block or allow specific numbers in T-Life | Before | Opt-in | PP | Free per benefits page; Premium per support page (**CONTRADICTION**) | [benefits](https://www.t-mobile.com/benefits/scam-shield), [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud) |
| Network SMS/MMS spam filter | Checks each message against spam "fingerprints and signatures" and blocks matches; about 3B blocked in 2025 | Before | Default | All customers; Metro | Free | [scamshield](https://www.t-mobile.com/scamshield), [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf) |
| Safe Web Browsing | DNS-layer blocking of phishing and malware domains, with a T-Life "Dangerous site blocked!" alert; launched 2025; 100B+ requests blocked | Before / During | Default at network level; "Availability can depend on your settings" | All customers on supported devices | Free | [benefits](https://www.t-mobile.com/benefits/scam-shield), [glossary](https://www.t-mobile.com/news/understanding-t-mobiles-cybersecurity-definitions) |
| Scam Counter and Activity log | Shows blocked and received scam calls; report from the log | After | T-Life | PP | Free | [scamshield](https://www.t-mobile.com/scamshield) |
| Scam Shield Premium | Sends whole call categories (telemarketer, political, charity, survey) to voicemail; reverse number lookup; network-stored block lists that follow you to new devices; "Send to voicemail" list; voicemail-to-text | Before / After | Paid add-on | PP (T-Life); Metro | **$4 per line per month** (T-Mobile); **$2 per line per month** (Metro); included on Experience More and Beyond, and on Experience for Business plans | [benefits](https://www.t-mobile.com/benefits/scam-shield), [Metro FAQ](https://www.metrobyt-mobile.com/benefits/scam-shield/faq), [Cape review](https://www.cape.co/blog/t-mobile-scam-shield-review), [TFB plans](https://www.t-mobile.com/business/experience-business-plans) |
| Call reporting | Report calls in T-Life or at callreporting.t-mobile.com; "Corrections are made within 48 hours of a verified request" | After | User-initiated | PP (app); anyone (web) | Free | [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud) |
| 7726 text reporting | Forward spam to 7726; T-Mobile replies with a confirmation and passes the message to a vendor-run "Security Center" | After | User-initiated | All | Free; does not count toward the plan | [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud) |
| Account PIN/Passcode | 6 to 15 non-sequential digits; changes require being on the T-Mobile network with Wi-Fi off; only the Primary Account Holder can change it | Before | Recommended (T-Mobile); required (Metro) | All | Free | [account fraud](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud), [Metro ATO](https://www.metrobyt-mobile.com/support/security/how-to-avoid-account-takeover-fraud) |
| SIM Protection | Blocks SIM or eSIM changes until it is turned off; **does not cover iPhone eSIM transfers** | Before | **Opt-in** | PP (all pages agree); PrP, TFB and Metro (**CONTRADICTION**, see section 4) | Free | [sim-protection](https://www.t-mobile.com/support/plans-features/sim-protection), [account fraud](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud) |
| Port Out Protection | Blocks porting the number to another carrier; must be added line by line; only the Primary Account Holder can remove it | Before | **Opt-in** | PP, TFB, PrP, Metro | Free | [account fraud](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud) |
| Biometric verification (T-Life) | Face or fingerprint check in T-Life when contacting customer care | Before | Opt-in (set up via care) | PP; iOS 16+ or Android 11+ | Free | [account fraud](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud) |
| Digital ID scan | Government ID plus selfie as an alternative to a one-time PIN | Before / After | Opt-in | Postpaid consumer accounts with voice lines | Free | [account fraud](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud) |
| T-Life security pop-up | Warns before sensitive actions such as a SIM change: "T-Mobile will never contact you to initiate a SIM transfer…" | During | Default (in T-Life) | T-Life users | Free | [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf) |
| SIM box / SIM farm detection | Machine-learning detection of SIM farms using network and behavioural attributes | Before (network-wide) | Internal | n/a | n/a | [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf) |
| Honeypot network | Controlled environment that attracts attackers so T-Mobile can study their techniques and feed its AI defences (network and cyber, **not** voice decoys) | n/a | Internal | n/a | n/a | [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf) |
| Live Translation (context, not anti-scam) | In-network AI agent triggered by `*87*`; translates in the caller's own cloned voice; T-Mobile says it does not record or store calls | During | Opt-in per call; beta | PP beta participants | Free during beta | [Newsroom](https://www.t-mobile.com/news/network/live-translation-beta-registration), [The Register](https://www.theregister.com/2026/02/11/tmobile_network_ai_translate_live_calls) |
| PROXY by DIGITS | Free second number for privacy. **Discontinued for new users Apr 9, 2025**; existing lines kept | Before | n/a | Legacy only | n/a | [PhoneArena](https://www.phonearena.com/news/t-mobile-discontinues-proxy-by-digits_id170235) |
| Branded calling / Verified Business Call | Verified business name, logo and call reason, via First Orion (INFORM, MOBC, BNID) | Before | Business enrolls; consumer can toggle | TFB and enterprises | Paid (First Orion) | [support](https://www.t-mobile.com/support/plans-features/consumer-versus-branded-calling), [First Orion](https://firstorion.com/solutions/t-mobile-for-business) |
| Brand Call Protect / Inbound Call Verify | Blocks spoofed outbound calls using an enterprise's numbers; verifies inbound calls to enterprise toll-free lines (30-second live and 30-minute lookback) | Before / During | Enterprise contract | Enterprises via DevEdge (NDA) | Contact sales | [DevEdge](https://devedge.t-mobile.com/call-protection) |
| Network Fraud Signals / SIM Swap / Network Authentication APIs | 18+ fraud signals including SIM swap and device binding; CAMARA SIM Swap; SIM-based verification to replace SMS one-time codes | Before | Enterprise contract | Enterprises via DevEdge (NDA) | Contact sales | [Fraud Signals](https://devedge.t-mobile.com/network-fraud-signals), [SIM Swap](https://devedge.t-mobile.com/Sim-swap), [Auth](https://devedge.t-mobile.com/network-authentication) |
| Threat Protect (SmartVPN) | Business app: blocks malicious sites and encrypts traffic when needed | Before | Opt-in | TFB; iOS 14+ or Android 7.1+ | $1.99 per user per month, or included on some plans | [Threat Protect](https://www.t-mobile.com/business/solutions/security/threat-protect) |
| T-SIMsecure / SASE / Secure SIM Authentication | SIM-based protection of the device-to-platform connection; uses the SIM as an authentication factor | Before | Opt-in | TFB | Contact sales | [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf), [security](https://www.t-mobile.com/business/solutions/security) |

---

## 1. Scam Shield (free)

- **How it works.** T-Mobile describes the system this way: "Our supercharged network analyzes every call and text using A.I., machine learning, and patented technologies… Our defenses update every six minutes." [scamshield](https://www.t-mobile.com/scamshield) The 2017 launch release described the original mechanism as matching "against an advanced global database of tens of thousands of known scammer numbers… kept up-to-date… with behavioral heuristics and intelligent scam pattern detection." [2017 PR](https://www.t-mobile.com/news/press/scam-block)
- **Scam ID ("Scam Likely").** "Enabled by default for all T-Mobile customers. No action is required." [scamshield](https://www.t-mobile.com/scamshield) The glossary adds that identification "happens in real time before the call connects." [glossary](https://www.t-mobile.com/news/understanding-t-mobiles-cybersecurity-definitions)
- **Scam Block.** Ways to turn it on:
  - toggle in T-Life
  - dial `#662#`
  - My T-Mobile
  - for DIGITS numbers, dial 611
  - prepaid customers: `#662#`, a store or 611

  Turn it off with `#632#` and check its status with `#787#` ([FCC guide](https://www.fcc.gov/sites/default/files/robocall_protection_guide_tmobile.pdf), [2017 PR](https://www.t-mobile.com/news/press/scam-block)). What it blocks: "all 'Scam Likely' calls." Potential Spam calls are not blocked unless sent to voicemail, and Scam Block "does not work on outbound calls." [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud), [customers/scam-shield](https://www.t-mobile.com/customers/scam-shield)
- **Anonymous callers.** "T-Mobile can't block anonymous calls or override the privacy choice of the caller" because of FCC rules. [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud)
- **Caller ID / Name ID.** Free and opt-in (`#436#`). Caller details partly come from WhitePages profiles. Name ID was historically powered by Hiya (2020). [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud), [Hiya blog](https://blog.hiya.com/consumer-reports-spam-findings-rank-hiya-powered-t-mobile-name-id-as-1/). Who supplies caller names today is **UNVERIFIED**.
- **Caller Verified (STIR/SHAKEN).** First launched January 2019 on the Galaxy Note9. It then went cross-network with Comcast and later AT&T and Inteliquent. [2019 PR](https://www.t-mobile.com/news/press/caller-verified-note9), [Comcast PR](https://www.t-mobile.com/news/press/inter-carrier-stir-shaken-launch)
- **Scam Callback Protection.**
  - What it does: "checks outbound calls against a database of known scam numbers and alerts customers with an audible warning before the call connects."
  - What the customer hears: "The number you are calling has been identified as likely a scam. It is recommended you hang up now."
  - Results: "Since we deployed the feature, it has played more than 67 million warnings, and most alerted customers have chosen to hang up before the call connects." [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf)
  - It is on by default. [customers/scam-shield](https://www.t-mobile.com/customers/scam-shield)
  - It was live on Mint by around 2024 (the Mint help page is dated May 2024). The exact launch date on T-Mobile is **UNVERIFIED**. [Mint](https://www.mintmobile.com/help/what-is-scam-screener/)
  - Mint tells users who hear a wrong warning to call care. [Mint](https://www.mintmobile.com/help/what-is-scam-screener/)
- **Safe Web Browsing.** Network DNS-layer blocking of "known phishing sites, malware distributors, and other malicious sources." It launched in 2025 and has blocked more than 100B malicious DNS requests. [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf), [glossary](https://www.t-mobile.com/news/understanding-t-mobiles-cybersecurity-definitions)
- **Spam text filtering.**
  - The network has done this "since 2014" and checks every message against "spam message fingerprints and signatures." [scamshield](https://www.t-mobile.com/scamshield)
  - "T-Mobile cannot block scam or spam messages on iMessage or other third-party messaging apps because the encrypted messages are not sent through the T-Mobile network." [customers/scam-shield](https://www.t-mobile.com/customers/scam-shield)
  - **CONTRADICTION:** an older FAQ says SMS, MMS **and RCS** are covered ([scamshield](https://www.t-mobile.com/scamshield), cached 2025), while the current benefits page says "*SMS and MMS only." [benefits](https://www.t-mobile.com/benefits/scam-shield)
- **Proxy number.** PROXY by DIGITS closed to new users on Apr 9, 2025. Existing lines were kept, and paid DIGITS plans remain. [PhoneArena](https://www.phonearena.com/news/t-mobile-discontinues-proxy-by-digits_id170235), [TmoNews](https://www.tmonews.com/2025/05/proxy-by-digits-quietly-phased-out-by-t-mobile)
- **2025–2026 additions:**
  - Safe Web Browsing (2025)
  - new AI/ML Potential Spam models (428M tags in 2025; expected to reach 25M a day "once fully optimized")
  - T-Life "Dangerous site blocked!" alerts
  - Scam Shield moved into T-Life; the standalone Scam Shield app is now Metro-only (March 2025) ([PhoneArena](https://www.phonearena.com/news/t-mobile-user-has-a-tip-for-customers-who-dont-want-to-lose-another-trusty-app_id168943))
  - a page rebrand to "ScamShield"
  - First Orion's "Watchlist," which lets businesses see Potential Spam tags on the T-Mobile network (Oct 2026)

## 2. Scam Shield Premium

| | T-Mobile | Metro |
|---|---|---|
| Price | $4 per line per month ([benefits](https://www.t-mobile.com/benefits/scam-shield)) | $2 per line per month ([Metro FAQ](https://www.metrobyt-mobile.com/benefits/scam-shield/faq), [Metro add-ons](https://www.metrobyt-mobile.com/shop/services/protection)); also in the $3 "Storage and Security Bundle" with Google One |
| Features | Category blocking to voicemail (telemarketers, political, charity, surveys); reverse number lookup; network-stored "Always Block" lists that survive app deletion and new devices; "Send to voicemail" list; voicemail-to-text (SMS, email or Visual Voicemail) | Same list; Metro describes it as "call and text controls" |
| Included on | Experience More and Experience Beyond ([Cape](https://www.cape.co/blog/t-mobile-scam-shield-review)); Experience for Business plans ([TFB](https://www.t-mobile.com/business/experience-business-plans)). T-Mix plans list only "Scam Shield Basic" ([plans](https://www.t-mobile.com/cell-phone-plans)). Whether T-Mix More or Loaded include Premium is **UNVERIFIED** | Not included by default |
| Prepaid | "The T-Life app does not support Scam Shield with Prepaid accounts"; prepaid customers get Scam Block and Caller ID by dial code only ([support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud)) | Metro uses the legacy Scam Shield app |

Note on voicemail-to-text: it is transcription only. We found no evidence that T-Mobile scans voicemail content for scams.

## 3. Content-based or AI analysis of calls and texts (critical)

**Conclusion: we found no evidence that any T-Mobile, Metro or Mint product listens to, transcribes or scores call audio for scam detection.**

How we checked:
- **Nov 2026 report (T-Mobile's most complete and current statement).** The report describes call protection as AI/ML "analyzing activity and calling patterns in real time." It names Scam ID, Scam Block, Potential Spam and Callback Protection. It mentions no audio, transcript or voice analysis of customer calls. Its forward-looking items are about AI-enabled fraud, non-human identities, adversarial AI testing and a honeypot program, not content screening. [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf)
- **Glossary.** The cybersecurity glossary defines Scam ID as using "threat intelligence databases and behavioral algorithms," and Scam Shield as integrating "AI-driven analysis, network-level monitoring and threat intelligence." Neither definition mentions content. [glossary](https://www.t-mobile.com/news/understanding-t-mobiles-cybersecurity-definitions)
- **Live Translation (the only in-call network AI).** It is activated per call with `*87*`. T-Mobile's statements:
  - "We do not save call recordings or transcripts."
  - "AI isn't listening in on calls that aren't being translated."
  - "We don't listen to customers' calls, and [the AI models] are not trained on customers' data" (CTO John Saw).

  [The Register](https://www.theregister.com/2026/02/11/tmobile_network_ai_translate_live_calls), [CNET](https://www.cnet.com/tech/mobile/t-mobile-opens-beta-for-network-based-live-language-translation/). The CEO said it is "the first AI-powered network-level feature," and T-Mobile declined to name what comes next. [The Register](https://www.theregister.com/on-prem/2026/02/11/t-mobiles-new-network-based-ai-will-translate-live-calls/5161068)
- **Partner searches.** We searched for T-Mobile together with each of: AI call screening, AI receptionist, Microsoft Azure Operator Call Protection, Hiya, TNS and Google. We found no current T-Mobile deployment of content-based screening.
  - Microsoft's Azure Operator Call Protection, which transcribes and analyses calls, was trialled by BT in the UK, not T-Mobile. [MSPowerUser](https://mspoweruser.com/microsofts-azure-operator-call-protection-uses-ai-to-detect-scam-calls)
  - Hiya now sells deepfake detection and real-time call analysis to operators. It lists T-Mobile as a logo partner, but we found no T-Mobile deployment of those features. [Hiya](https://www.hiya.com/solutions/technology-partners). **UNVERIFIED** whether T-Mobile uses any Hiya product today.
- **Text messages.** Filtering uses message "fingerprints and signatures," a form of content pattern matching. We found no evidence of LLM-based semantic analysis of texts.
- **Analytics vendor.** First Orion: "As T-Mobile's analytics engine, First Orion provides insight into the behaviors observed on the network that are associated with spam labeling." [First Orion PR, Oct 13 2026](http://firstorion.com/press-releases/first-orion-spam-watchlist-launch). First Orion also sells SENTRY blocking and PROTECT+ "risk detection" to carriers and enterprises. [First Orion](http://firstorion.com/products)
- **Device-side layers, not T-Mobile's.** Apple added call screening in iOS 26 and Google offers Call Screen on Pixel; both run on the phone, not in the network. [Mobile World Live](https://www.mobileworldlive.com/att/att-trials-agentic-ai-phone-receptionist)

## 4. Account protections

- **PIN/Passcode.**
  - Must be 6 to 15 digits. It cannot be sequential or repeating, the start or end of the mobile number, any number on the account, the Billing Account Number, a tax ID, an SSN or a date of birth.
  - Only the Primary Account Holder can change it, and only while on the T-Mobile network with **Wi-Fi off**.
  - Metro: a 6 to 15 digit PIN is mandatory, plus security questions. A one-time PIN is required for SIM changes, port-out PIN generation, PIN changes, address changes and "Add/Remove of Account Takeover Protection features."

  [account fraud](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud), [Metro ATO](https://www.metrobyt-mobile.com/support/security/how-to-avoid-account-takeover-fraud)
- **SIM Protection.**
  - Free and opt-in. It can be set per line or for the whole account.
  - An Authorized User can add it; only the Primary Account Holder can remove it.
  - "Does not cover eSIM transfers on Apple iPhones." [account fraud](https://www.t-mobile.com/support/account/set-up-your-customer-pinpasscode)
- **Port Out Protection.**
  - Free and opt-in, added line by line.
  - Eligible: Postpaid, TFB, Prepaid and Metro.
  - Porting out then requires turning it off and generating a Temporary Port Out PIN. [transfer](https://www.t-mobile.com/support/account/transfer-your-phone-number)
- **Biometric ID verification.**
  - T-Life face or fingerprint check used when contacting care. Postpaid; iOS 16+ or Android 11+.
  - Digital ID scan (ID plus selfie in place of a one-time PIN) is available to postpaid consumer voice accounts. [account fraud](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud)
- **T-Life security pop-up.** Shown before a SIM change: "T-Mobile will never contact you to initiate a SIM transfer unless you first initiate it. If you received an unsolicited request, do not respond." [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf). Launch date **UNVERIFIED**.
- **Result.** "Layered authentication measures have reduced successful SIM swap attacks by 99% since 2022." The press release says "more than 99%." [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf), [press release](https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile)
- **eSIM transfer limits.** Beyond the iPhone exclusion, we found no specific T-Mobile eSIM transfer rate limits. **UNVERIFIED**.
- **Mint.** We found no Mint pages on SIM protection or port-out protection. **UNVERIFIED**.

**CONTRADICTION: SIM Protection eligibility**

| Page | What it says |
|---|---|
| [/support/plans-features/sim-protection](https://www.t-mobile.com/support/plans-features/sim-protection) | "Available to all T-Mobile Postpaid… **Not available to T-Mobile for Business, T-Mobile Prepaid, or Metro by T-Mobile.**" |
| [/support/plans-features/help-with-t-mobile-account-fraud](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud) | Says "offered to all T-Mobile Postpaid," but includes "T-Mobile Prepaid accounts" toggle steps and "T-Mobile for Business accounts: Visit your self-service portal." |
| [Metro ATO page](https://www.metrobyt-mobile.com/support/security/how-to-avoid-account-takeover-fraud) | "SIM Change Protection is a free feature offered to all Metro by T-Mobile customers." |

## 5. Reporting

- **Calls.**
  - In T-Life: Manage/Account > Scam Shield > Recent activity > Report Caller, then choose a category. Premium users can also add the number to their block list.
  - On the web: [callreporting.t-mobile.com](https://callreporting.t-mobile.com/). "Corrections are made within 48 hours of a verified request." [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud)
- **Texts.**
  - Forward to **7726**. It is free and does not count against the plan.
  - T-Mobile replies with a confirmation SMS and forwards the message to "the Security Center… a global system, run by a vendor on our behalf… linked to a global database… may be shared with government agencies." The vendor is not named (**UNVERIFIED**).
  - Native reporting also works: iOS 16+ "Report Junk" and Google Messages "Report Spam." [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud)
- **What happens after a report.** "Reports are used to update network policies" ([FCC guide](https://www.fcc.gov/sites/default/files/robocall_protection_guide_tmobile.pdf)). The report adds: "Each report gives us valuable signals… By combining customer reports with AI and ML, we can adapt our defenses." ([Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf)). We found no per-report status or outcome sent back to the customer.
- **Account fraud.**
  - Current customers: "contact us as soon as possible" (611, or the general contact page).
  - Identity-theft debt disputes: [online form](https://customerhelp.t-mobile.com/fraud/fraud_dispute), investigated within 30 business days (10 for California).
  - FACTA records requests are supported.
  - Scam Shield app issues: CallProtectionOps@T-Mobile.com.

  [account fraud](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud), [App Store](https://apps.apple.com/us/app/t-mobile-scam-shield/id1367276365)
- **Business numbers that are wrongly labelled.** Businesses can register for free at Call Transparency or Free Caller Registry. **CONTRADICTION:** T-Mobile pages cite different URLs, [calltransparency.com](https://www.t-mobile.com/customers/scam-shield) and [freecallerregistry.com](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud). First Orion's Watchlist shows Potential Spam tags from the last 24 hours. [First Orion](http://firstorion.com/press-releases/first-orion-spam-watchlist-launch)

## 6. Business

- **T-SIMsecure / SASE.** "Helps protect the connection between a user's device and T-Mobile's security platforms." Secure SIM Authentication uses the SIM or eSIM "as an authentication factor." T-SIMsecure Essentials is aimed at 5 to 24 users. [Report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf), [security](https://www.t-mobile.com/business/solutions/security)
- **SmartVPN / Threat Protect.** Blocks malicious sites and encrypts traffic only when needed. $1.99 per user per month or included on some plans. TFB only. [Threat Protect](https://www.t-mobile.com/business/solutions/security/threat-protect)
- **Mobile Threat Defense.** Named in the report as covering "malicious apps, unsafe links, phishing, device vulnerabilities." Product name, vendor and price are **UNVERIFIED**.
- **Brand Call Protect and Inbound Call Verify.**
  - Brand Call Protect blocks spoofed calls that use an enterprise's numbers.
  - Inbound Call Verify authenticates callers to enterprise toll-free lines, with a 30-second live lookback and a 30-minute recent-call lookback.
  - Available via DevEdge sales. [DevEdge](https://devedge.t-mobile.com/call-protection)
- **Enterprise branded calling (First Orion).**
  - INFORM with Authentication, INFORM with Logo, Mobile Originated Branded Calling (launched Jul 21, 2026, "industry-first wireless provider deployment") and Business Number ID.
  - Shown to consumers as "T Verified Business Call."

  [First Orion MOBC](https://firstorion.com/press-releases/first-orion-mobc-t-mobile-2026), [support](https://www.t-mobile.com/support/plans-features/consumer-versus-branded-calling)
- **DevEdge APIs.** Network Fraud Signals (18+ signals: SIM swap, subscriber tenure, device binding, device lost or stolen status; CAMARA-compatible), SIM Swap (CAMARA 1.0; pilot terms), SIM-based Network Authentication, Quality on Demand, Device Status and Location Verification.
  - **Not public or self-serve.** The process is "submit interest… review… NDA… then access."
  - Pricing is "contact us."

  [FAQ](https://devedge.t-mobile.com/support/faq), [Fraud Signals](https://devedge.t-mobile.com/network-fraud-signals), [SIM Swap](https://devedge.t-mobile.com/Sim-swap), [Wholesale](https://www.t-mobile.com/wholesale/network-apis)

## 7. Nov 2, 2026 "Advancing Cybersecurity at T-Mobile" and other 2025–2026 statements (exact quotes)

All from the [report PDF](https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf) and the [press release](https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile) unless noted.

- **On AI-enabled scams:**
  - "Cybercriminals are using artificial intelligence (AI) to generate phishing campaigns and deepfake voice scams on an industrial scale."
  - "Bad actors deploy increasingly sophisticated, AI-generated campaigns to target consumers and businesses."
- **How T-Mobile detects scam calls:** "We use continuously improving AI and machine learning (ML) models to identify and stop scam calls by analyzing activity and calling patterns in real time."
- **Scale:**
  - "Today, 100% of our customers receive core network-level protection."
  - "Since launching Scam ID and Scam Block in March 2017, we've protected customers from more than 160 billion unwanted calls. Today, we identify or block an average of over 800 scam calls every second."
- **2025 call figures:** "In 2025 alone, we tagged nearly 29 billion inbound calls as likely scams and spam. That includes more than 428 million 'Potential Spam' calls detected and tagged by our new AI and ML systems—a tenfold increase compared to 2024… once fully optimized, these systems are expected to identify over 25 million unwanted spam calls each day."
- **Scam Block usage:** "Nearly 99% of customers who turn on Scam Block never turn it off."
- **Messaging:**
  - "In 2025, our network-level protections blocked nearly 3 billion spam and scam SMS and MMS messages."
  - "In 2025, we saw nearly 50% more scam and spam messages than the previous year, and we're continuing to identify hundreds of millions of scam and spam calls every week" (Jeff Simon, EVP and CIO).
- **Callback Protection:** "more than 67 million warnings."
- **Forward-looking:**
  - "Emerging risks such as AI-enabled fraud and non-human identity compromise…"
  - "Non-human identities—including AI agents, bots, and automated services—represent a growing attack surface."
  - "Our honeypot network… provides real-world insight into emerging threats. Those insights feed into our AI-driven defenses."
- **Overall threat trend:** a 37% increase in attempted intrusions and a 35% decrease in credential-based attempts year over year.
- **Other 2026 announcements:**
  - Live Translation network AI: Feb 11 announcement; beta launched around May 21. [Newsroom](https://www.t-mobile.com/news/network/live-translation-beta-registration), [PCMag](https://www.pcmag.com/news/tmobile-debuts-ai-backed-live-language-translation-beta-no-app-needed)
  - The CTO blog calls Live Translation "only the tip of the iceberg" of network-native agentic AI. [blog](https://www.t-mobile.com/news/network/t-mobile-live-translation-and-the-rise-of-intelligent-connectivity)
  - "Understanding T-Mobile's Cybersecurity Definitions" glossary (Nov 2026). [glossary](https://www.t-mobile.com/news/understanding-t-mobiles-cybersecurity-definitions)

## 8. Defaults, platform limits and complaints

- **On by default:** Scam ID, Potential Spam tagging, Callback Protection, text spam filtering, Safe Web Browsing (network side), STIR/SHAKEN display, neighborhood-spoofing protection.
- **Opt-in:** Scam Block, Caller ID, sending Potential Spam to voicemail, block and allow lists, Premium, SIM Protection, Port Out Protection, biometrics, digital ID scan, Live Translation.
- **T-Life requirements:**
  - T-Life is needed for full controls (reporting, lists, Premium, web alerts) and requires a **postpaid** account. Prepaid customers get dial codes only.
  - Metro still uses the standalone Scam Shield app.
  - Network features work on "any phone," including flip phones, with "Capable device req'd."

  [support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud), [PhoneArena](https://www.phonearena.com/news/t-mobile-user-has-a-tip-for-customers-who-dont-want-to-lose-another-trusty-app_id168943)
- **iOS vs Android:**
  - SIM Protection does not cover iPhone eSIM transfers.
  - Biometrics need iOS 16+ or Android 11+.
  - Native junk reporting needs iOS 16+, or Google Messages on Android.
  - Branded-call logos and reasons appear only on "supported Android and iOS devices."
  - iMessage and other over-the-top messaging cannot be filtered.
- **Complaints from credible reviews:**
  - Mixed effectiveness and false positives that block legitimate calls. [SlashGear, Jun 2026](https://www.slashgear.com/2200747/tmobile-report-spam-feature-effectiveness)
  - The T-Life integration made the app "slower" and "unintuitive." [Cape, Apr 2026](https://www.cape.co/blog/t-mobile-scam-shield-review). Note that Cape is a competing carrier, so this source is biased.
  - App store reviewers report that blocked numbers still ring through, spam is only visible after the fact in the missed-call log, and rotating-number campaigns get past blocking. [App Store](https://apps.apple.com/us/app/t-mobile-scam-shield/id1367276365), [Google Play](https://play.google.com/store/apps/details?hl=en_IN&id=com.tmobile.services.nameid)
  - T-Mobile's own FAQ admits that "scammers sometimes still find a way around these network protections." [scamshield](https://www.t-mobile.com/scamshield)
  - Freshly provisioned VoIP numbers evade reputation-based systems. This is a general limitation of all carriers' approaches. [Callro](https://getcallro.com/blog/does-phone-builtin-spam-protection-work)

### Other contradictions and inconsistencies

- **Personal number blocking:** listed as free on the [benefits page](https://www.t-mobile.com/benefits/scam-shield), but "Block calls and texts from specific numbers" is listed as Premium on the [support page](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud).
- **RCS spam coverage:** included in the older FAQ, "SMS and MMS only" in the current one (see section 1).
- **Mint Scam Screener:** Mint says it "can't be toggled on or off" ([Mint](https://www.mintmobile.com/help/what-is-scam-screener/)); BestMVNO says it "can be turned on or off" ([BestMVNO](https://bestmvno.com/mint-mobile/mint-mobile-adds-3gb-canada-roaming)). Whether Mint offers Scam Block is **UNVERIFIED**.
- **Callback warning wording:** the report uses "The number you are calling has been identified as likely a scam"; the FAQ uses "We've identified the number you are calling is likely a scam."
- **Branding:** the current benefits page says "ScamShield"; the report and support pages say "Scam Shield."
- **Business call registration:** calltransparency.com vs freecallerregistry.com.
- **SIM swap reduction:** the report says "99%"; the press release says "more than 99%."

---

## Gaps: what T-Mobile does NOT do today

**How we checked:** the Nov 2026 report and glossary; all Scam Shield consumer and support pages; Metro and Mint pages; DevEdge; the newsroom (Live Translation and 2025–26 coverage); press (The Register, CNET, PCMag, SlashGear); and vendor sites (First Orion, Hiya, Microsoft). An absence is never fully provable, but every item below was searched for and not found.

1. **No in-call content analysis for scam detection.** T-Mobile does not listen to, transcribe or semantically analyse live call audio to detect scams. Detection is by number reputation, calling patterns and STIR/SHAKEN only. The company's public position is "we don't listen to customers' calls," and its in-network AI listens only when a user dials `*87*` for translation.
2. **No AI call screener, receptionist or assistant that answers suspicious calls.** AT&T has been testing exactly this since September 2025. T-Mobile's only options for a suspect call are label, block or send to voicemail.
3. **No mid-call warning on inbound calls.** If a scam call gets through (new or rotating numbers, spoofing that passes checks), nothing warns the customer during the conversation. Callback Protection only warns on **outbound** calls, before they connect, and only for listed numbers.
4. **No deepfake or voice-clone detection product for consumers,** even though the report names "deepfake voice scams on an industrial scale" as a threat.
5. **No scammer engagement, decoy or intelligence extraction.** T-Mobile's honeypot program studies network and cyber attacker techniques; we found nothing that engages scam callers to harvest callback numbers, payment rails, URLs or scripts. The only feedback loop is customer reports.
6. **No scam analysis of voicemail.** Voicemail-to-text (Premium, $4 per month) is plain transcription with no scam scoring.
7. **No coverage of encrypted or over-the-top channels.** T-Mobile states it cannot filter iMessage or third-party messaging apps. Whether RCS is covered is contradictory across pages.
8. **No closed loop on reports.** Customers get a confirmation text but no outcome, no "this number has now been blocked for X people," and no outreach to others who were contacted by the same scammer.
9. **No "after" recovery workflow for scam victims** beyond "contact us," identity-theft dispute forms, and links to the FTC and credit bureaus. We found no guided path such as "I just got scammed: lock account, flag bank, report."
10. **No caregiver or trusted-contact scam alerts.** Family Allowances is parental controls on usage, not scam alerting. **UNVERIFIED** absence.
11. **Several protections are off by default.** Scam Block, SIM Protection and Port Out Protection are all opt-in (SIM and Port Out also line by line). Prepaid customers have no T-Life Scam Shield, and SIM Protection eligibility is contradictory across pages.
12. **The network APIs are not self-serve.** DevEdge fraud and call APIs require an NDA and a business review, which limits third-party innovation and hackathon use.

**Positioning implication for the team:** build on top of Scam ID and Scam Block, which already provide the "is this number suspect" signal. Add the missing pieces: the **during** stage (content-aware screening by an AI answerer, before the customer is connected) and the **after** stage (turning scam conversations into infrastructure intelligence that feeds back into Scam ID and Callback Protection lists). Address T-Mobile's "we don't listen" stance directly. Two options: make screening consent-based and opt-in, like `*87*`, and/or only analyse calls the network has *already* flagged as Scam Likely, where a scammer, not a customer, is the one on the line. Frame the decoy as a voice extension of T-Mobile's existing honeypot program.

---

## Competitor parity

| Capability | T-Mobile Scam Shield | AT&T ActiveArmor | Verizon Call Filter |
|---|---|---|---|
| Free network labelling and blocking | Yes. Scam ID on by default; Scam Block opt-in | Yes. "Fraud calls are automatically set to Block"; spam is labelled ([AT&T](https://www.att.com/support/article/wireless/KM1147710/)) | Yes. Free tier auto-blocks high-risk calls to voicemail ([Verizon](https://www.verizon.com/solutions-and-services/add-ons/protection-and-security/call-filter)) |
| Category controls | Premium ($4) | Free in app (telemarketers, political, surveys and others) | Call Filter (category controls) |
| Caller name ID | Free (opt-in) | Advanced ($7 per month) | Plus ($3.99 per line, or $10.99 for 3+ lines) |
| Outbound scam-number warning | **Yes (Callback Protection, 67M+ warnings)** | Not found | Not found |
| Network DNS safe browsing | Free, network-wide | Advanced (paid) | Verizon Digital Secure (paid or perk) **UNVERIFIED** details |
| AI agent that answers or screens calls | **No** | **Testing: network "digital receptionist,"** agentic voice-to-voice AI with live transcript that disconnects fraud (Sep 2025; GA status **UNVERIFIED**) ([AT&T blog](https://about.att.com/blogs/2025/ai-digital-receptionist.html), [Verge](http://www.theverge.com/news/778518/att-ai-call-screening-digital-receptionist)) | **None found** in 2025–26 (the Oct 2026 perks release lists Call Filter only; app moving into "Verizon Protect") ([Verizon](https://www.verizon.com/about/news/verizon-delivers-free-safety-family-ai-perks)) |
| In-network AI on live calls (any use) | Live Translation (`*87*`, beta) | Digital receptionist (test) | Not found |
| Account lock | SIM Protection and Port Out Protection | Wireless Account Lock ([AT&T](https://www.attconnects.com/stories/fighting-fraud-atts-commitment-to-protecting-americans/)) | Number Lock / SIM Protection **UNVERIFIED** |

---

## Sources

**T-Mobile**
- https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile
- https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf
- https://investor.t-mobile.com/news-releases/news-release-details/t-mobile-opens-its-cybersecurity-transformation-new-report
- https://www.t-mobile.com/news/understanding-t-mobiles-cybersecurity-definitions
- https://www.t-mobile.com/benefits/scam-shield
- https://www.t-mobile.com/customers/scam-shield
- https://www.t-mobile.com/scamshield
- https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud
- https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud
- https://www.t-mobile.com/support/plans-features/sim-protection
- https://www.t-mobile.com/support/account/set-up-your-customer-pinpasscode
- https://www.t-mobile.com/support/account/transfer-your-phone-number
- https://www.t-mobile.com/support/plans-features/block-unwanted-calls
- https://www.t-mobile.com/support/plans-features/consumer-versus-branded-calling
- https://www.t-mobile.com/business/solutions/call-protection
- https://www.t-mobile.com/business/solutions/security
- https://www.t-mobile.com/business/solutions/security/threat-protect
- https://www.t-mobile.com/business/experience-business-plans
- https://www.t-mobile.com/cell-phone-plans
- https://www.t-mobile.com/wholesale/network-apis
- https://www.t-mobile.com/news/press/scam-block
- https://www.t-mobile.com/news/press/caller-verified-note9
- https://www.t-mobile.com/news/press/inter-carrier-stir-shaken-launch
- https://www.t-mobile.com/news/un-carrier/scam-shield-protects-customers-from-scams-robocalls
- https://www.t-mobile.com/news/network/live-translation-beta-registration
- https://www.t-mobile.com/news/network/t-mobile-live-translation-and-the-rise-of-intelligent-connectivity
- https://www.fcc.gov/sites/default/files/robocall_protection_guide_tmobile.pdf

**DevEdge**
- https://devedge.t-mobile.com/support/faq
- https://devedge.t-mobile.com/network-fraud-signals
- https://devedge.t-mobile.com/Sim-swap
- https://devedge.t-mobile.com/network-authentication
- https://devedge.t-mobile.com/call-protection

**Metro and Mint**
- https://www.metrobyt-mobile.com/benefits/scam-shield/faq
- https://www.metrobyt-mobile.com/shop/services/protection
- https://www.metrobyt-mobile.com/support/security/how-to-avoid-account-takeover-fraud
- https://www.mintmobile.com/help/what-is-scam-screener/
- https://bestmvno.com/mint-mobile/mint-mobile-adds-3gb-canada-roaming

**Vendors**
- http://firstorion.com/press-releases/first-orion-spam-watchlist-launch
- https://firstorion.com/press-releases/first-orion-mobc-t-mobile-2026
- https://firstorion.com/solutions/t-mobile-for-business
- https://blog.hiya.com/consumer-reports-spam-findings-rank-hiya-powered-t-mobile-name-id-as-1/
- https://www.hiya.com/solutions/technology-partners
- https://mspoweruser.com/microsofts-azure-operator-call-protection-uses-ai-to-detect-scam-calls

**Press and reviews**
- https://www.theregister.com/2026/02/11/tmobile_network_ai_translate_live_calls
- https://www.cnet.com/tech/mobile/t-mobile-opens-beta-for-network-based-live-language-translation/
- https://www.pcmag.com/news/tmobile-debuts-ai-backed-live-language-translation-beta-no-app-needed
- https://www.slashgear.com/2200747/tmobile-report-spam-feature-effectiveness
- https://www.cape.co/blog/t-mobile-scam-shield-review
- https://www.phonearena.com/news/t-mobile-user-has-a-tip-for-customers-who-dont-want-to-lose-another-trusty-app_id168943
- https://www.phonearena.com/news/t-mobile-discontinues-proxy-by-digits_id170235
- https://apps.apple.com/us/app/t-mobile-scam-shield/id1367276365
- https://getcallro.com/blog/does-phone-builtin-spam-protection-work

**Competitors**
- https://about.att.com/blogs/2025/ai-digital-receptionist.html
- http://www.theverge.com/news/778518/att-ai-call-screening-digital-receptionist
- https://www.mobileworldlive.com/att/att-trials-agentic-ai-phone-receptionist
- https://www.att.com/support/article/wireless/KM1147710/
- https://www.att.com/support/article/my-account/KM1252916/
- https://www.attconnects.com/stories/fighting-fraud-atts-commitment-to-protecting-americans/
- https://www.verizon.com/solutions-and-services/add-ons/protection-and-security/call-filter
- https://www.verizon.com/about/news/verizon-delivers-free-safety-family-ai-perks
