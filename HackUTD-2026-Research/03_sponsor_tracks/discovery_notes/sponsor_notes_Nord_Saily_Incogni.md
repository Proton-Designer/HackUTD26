# Nord / Saily / Incogni sponsor discovery notes (partial)

## Approaches tried
- WebSearch (many phrasings: "Best Use of NordVPN", Saily Best Travel Hack, Incogni Best Privacy, site:devpost.com): almost no useful hits (only bug-bounty / PR pages). Not productive.
- Devpost project search JSON (/software/search?query=...): noisy; prize badges not indexed. Only found keyword noise (e.g. Aegis-LEO mentions Nord tech, not a prize).
- Best route: open each hackathon's Devpost page (guessed slug, <slug>.devpost.com), regex the page text for nord|saily|incogni, then read the winners gallery and check each project's Winner badges via same-origin fetch from devpost.com.
- ~75 slugs checked (many guesses 404 as "Devpost" title).

## Findings
- Nord sponsorship appears almost entirely as a prize add-on/bundle (1-year NordVPN, NordPass, Incogni, Saily 1GB, later NordProtect + nexos.ai credit), usually attached to overall 1st/2nd place or an AI/Best Overall prize, not as a Nord-authored challenge with API/tools.
- Only a true Nord-sponsored track found: HackNYU 2025 "Security and Privacy" (2 winners: FirstWave, Dristhi).
- No Saily-only prize (e.g. "Best Travel Hack") and no Incogni-only prize ("Best Privacy Hack") found on any page scanned. Saily/Incogni always appear inside the Nord bundle. Hence all rows are sponsor "NordVPN/NordPass"; bundle text lists Saily and Incogni.
- HackUTD 2025: "Guided Track" prize = NordVPN 1-year subscription (beginner track, 1 winner). Winner not identified (not on winners gallery page 1; 367 winners across 16 pages). HackUTD 2024 Guided Track winner DuckTalk is in all_records (prize detail for 2024 unverified). HackUTD 2024 page slug hackutd-2024 returned 404 for me.
- HackRPI 2025: Nord/Saily/nexos.ai add-on text sits at the end of the Best Data Science Hack entry; unclear whether it is a separate prize. Winner not identified.

## Present but winners not found / not fully resolved
- HackNYU 2025 (second page of winners only partly checked; both Security & Privacy winners found).
- HackRPI 2025 (Nord add-on; winner unknown).
- HackUTD 2025 Guided Track winner.
- HackUMass XII, QHacks 2025, DeltaHacks XI, McHacks 12: winners listed (from all_records), though QHacks 2025 / DeltaHacks / McHacks dates are null.
- McHacks 12 first place bundle includes NordVPN/NordPass/Incogni.

## Checked, no Nord/Saily/Incogni text
treehacks 2025/2026, tamuhack 2025, hack-western-12, conuhacks ix/x, nwhacks 2025/2026, hackdavis 2025/2026, boilermake-xii, cal-hacks-12-0, la-hacks-2025, hackutd-2025 (except Guided Track), hackumass-xiii, qhacks-2026, deltahacks-12, uofthacks-13, hackillinois 2025/2026, swamphacks-xi, hack-the-valley-11, hoohacks-2026, hackpsu fall/spring 2025, hacknc-2025, vthacks 13/14, bitcamp2025, hackrpi-2026, hacknyu-fall-2025, hackprinceton-fall-2025, hackharvard2026, hackumbc-2025.

## Leads left
- Slug-404 (unchecked): hackutd-2024, mchacks-13, uofthacks-12, tamuhack2026, hackgt 11/12, hackharvard2025, hack-western-11, hacklytics-2025 (removed), uottahack, sbhacks, hackncstate-2025, bitcamp2026, hackprinceton-spring-2026, yhack, hackrice, hacktx, boilermake-xiii. Find correct slugs (Devpost hackathon links on project pages) and scan.
- MLH season lists (mlh.com/seasons/2025|2026/events; only 24 events rendered per page) for more events with Nord partner prizes; Global Hack Week.
- Many smaller Devpost hackathons Nov 2024 - Nov 2026 (api list gave ~540 mostly 2026 small events; not scanned).
- Nord Security / MLH social posts and recap blogs not searched beyond WebSearch.

## Follow-up pass (2026-11-02)
- HackUTD 2024 real slug hackutd-ripple: Guided Track prize = 1-year NordVPN + NordPass (1 winner); DuckTalk row updated. HackUTD 2025 Guided Track winner NOT identifiable: crawled all 366 gallery projects, JSON-LD "award" field shows no Guided Track badge (330 have no badge); ChemQuick (devpost.com/software/chem-numbers) says it was built "as part of the guided track" but has no award badge, so not recorded as winner.
- HackRPI 2025 (Nov 15-16, 2025): Nord bundle belongs to Best Data Science Hack; winner ByteBite (badge verified). Row added.
- HackNYU 2025: crawled 154 gallery projects; exactly 2 Security and Privacy badges (FirstWave, Dristi), verified.
- Real slugs found via project-page JSON-LD subjectOf and scanned, no Nord/Saily/Incogni text: McHacks 13 (mchacks13), UofTHacks 11 (uofthacks-11) and 13, TAMUhack 2026 (th26), HackGT 11 (hackgt-11-circus-of-invention), 12, 13 (hackgt13), HackHarvard 2024/2025, Hack Western 12, Bitcamp 2026 (bitcamp-2026), YHack 2024 (yhack-2024), yhack, yhack-2026, HackPrinceton Spring 2026 (hackprinceton-spring-26), BoilerMake XI, HackNC 2026 and ~20 others from all_records editions (HackDartmouth, HackNJIT, Hacklytics, Hack@Brown, StormHacks, UNIHACK, PennApps, SwampHacks XII, HackNC 2025, HackSheffield, HackUPC, HackNotts). Only known Nord events re-hit: HackUTD 2024, DeltaHacks XI, QHacks 2025, HackUMass XII.
- Tip: project page JSON-LD has "award" array and "subjectOf" event url; devpost subdomains allow same-browser fetch from other devpost hosts.
## Remaining
- Leads 5 (other MLH events, scanning HackUTD master v2 hackathons not already scanned) and 6 (social/recap posts) not done. HackUTD 2025 Guided Track winner unresolved (try HackUTD recap/Instagram/Discord).
