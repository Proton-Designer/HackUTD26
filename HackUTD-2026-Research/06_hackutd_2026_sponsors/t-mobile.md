# T-Mobile (Title sponsor, HackUTD 2026)

## 1. Who they are
US wireless carrier headquartered in Bellevue, WA, with a very large Frisco/Plano, TX presence (unverified detail from general knowledge). Sells mobile, home internet and business connectivity; also exposes carrier "Network APIs" via DevEdge. [verified: t-mobile.com/wholesale/network-apis lists the four API families below]

## 2. HackUTD 2026 prize/challenge
- T-Mobile is listed as **Title sponsor** on zeroday.hackutd.co. [verified]
- Site states: "This year's challenge tracks will be announced once hacking starts." Teams can enter up to two tracks. [verified]
- Challenge text: **not public** (revealed at hacking start, Sat Nov 7, ~12:00 CT). Prize list: **not public**.
- Schedule item: T-Mobile Fireside Chat, Sat 1:30-2:20pm, ECSW 1.315. [verified]
- Last year's T-Mobile prizes (2025): 1st iPhone 17, 2nd iPad Air, 3rd Beats Studio Pro. [verified, hackutd-2025.devpost.com]

## 3. Products/APIs usable in 36 hours
DevEdge (https://devedge.t-mobile.com). Docs:
- Network Fraud Signals: https://devedge.t-mobile.com/network-fraud-signals
- SIM-based Network Authentication / number verification: https://devedge.t-mobile.com/network-authentication
- Call Protection (Brand Call Protect, Inbound Call Verify): https://devedge.t-mobile.com/call-protection
- Quality on Demand: https://devedge.t-mobile.com/qod
Access: the pages show "Get Started"/"Talk to an expert"/contact form; no public sandbox, SDK or self-serve key was visible. [verified that none was mentioned; real availability unverified]. Assume you will NOT get live carrier APIs unless the sponsor hands out hackathon access; ask at the booth.
Practical fallback: public data (see 2025 winners used Reddit, Downdetector, Twilio, Groq, Gemini, Auth0).

## 4. Prior hackathon sponsorships
- HackUTD 2025 (theme "Lost in the Pages"): T-Mobile track with prizes above. The official challenge statement was NOT on the Devpost page (said to be in hackerpack once hacking starts) [verified]. Prompt inferred from winners: build a tool for T-Mobile product managers to understand customer sentiment/pain points in real time [inferred].
  Winners (labelled Winner; T-Mobile-themed):
  - InsighT https://devpost.com/software/t-insights : PM dashboard, aggregates Reddit/outage trackers/forums/news/support logs, Customer Happiness Index, Leaflet heatmap, Gemini 2.0 Flash for prioritized actions. Stack Next.js, Supabase. [verified]
  - Beacon https://devpost.com/software/na-504rkg : 0-100 Happiness Score by region/service, live PII-scrubbed call transcripts (Twilio, Presidio), social triage, Groq-hosted LLaMA, MongoDB, Auth0. [verified]
  - HarmoniQ https://devpost.com/software/x-yiqm81 : PM command center for sentiment, outage prediction, resource allocation. [verified from gallery blurb only]
  Which of these took 1st/2nd/3rd: unknown. Gallery: https://hackutd-2025.devpost.com/project-gallery (24 of 367 seen; other T-Mobile winners may exist).
- Other winners in the same gallery were for other sponsors' tracks (ProdigyPM etc.), not mapped to T-Mobile.
- T-Mobile Hacktober 2019 (XR, Metro brand): AR to cut online phone returns; a UTD freshman team won 2nd with an AR app sizing a phone against a dollar bill. https://cs.utdallas.edu/student-hackathon-experience-supratik-pochampally-and-his-team-win-2nd-place-at-t-mobile-hacktober-hackathon [verified]
- T Challenge (T-Mobile + Deutsche Telekom startup program, AI for telecom) is a separate program, not a hackathon [verified by search titles only].

## 5. Likely judging values (inference)
Evidence: 2025 winners were polished, data-integrating, product-manager-facing dashboards with LLM insights and a clear T-Mobile customer story [verified pattern, inference on cause]. Expect: tie to real customer/business problem, working demo, AI used meaningfully, clear persona, polish, use of T-Mobile brand/data themes.
Project directions (inference):
1. Customer-experience signal engine: ingest public sentiment/outage data, produce ranked issues with LLM root-cause and suggested actions (but differentiate from 2025 winners).
2. Fraud/trust demo around SIM swap / number verification flow (mock the Network API behind an interface; swap in real API if provided).
3. Home internet / Quality-on-Demand scenario app (e.g. gaming/telehealth session that requests a bandwidth boost), simulated if no API access.

## 6. Questions for the booth
- Do we get sandbox/credentials for any DevEdge API? How to request, and by when?
- Is the track a PM/customer-experience prompt again or something new? What data is provided?
- Rubric weights (impact, technical depth, demo, business viability)? Is there a Devpost-only or live judging?
- Can we enter two tracks with one project?
- Which T-Mobile team will judge (product, network, engineering)?

## Sources
- https://zeroday.hackutd.co [verified]
- https://hackutd-2025.devpost.com and /project-gallery [verified]
- https://devpost.com/software/t-insights ; https://devpost.com/software/na-504rkg [verified]
- https://www.t-mobile.com/wholesale/network-apis ; https://devedge.t-mobile.com [verified]
- https://cs.utdallas.edu/student-hackathon-experience-supratik-pochampally-and-his-team-win-2nd-place-at-t-mobile-hacktober-hackathon [verified]
