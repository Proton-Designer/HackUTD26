# Sponsor discovery notes (Capital One, State Farm, CBRE)

## Approaches that worked
- Devpost search (/software/search) is blocked by Cloudflare (429/JS challenge); abandoned after the first CBRE query (which surfaced the first CBRE winners).
- Reliable route: WebFetch of a hackathon home page (prizes/sponsors), then in Chrome fetch /project-gallery pages, keep entries with a winner badge, fetch each project page, regex the prize badges for the sponsor. Works for any hackathon whose slug is known.
- Slug discovery: WebSearch restricted to devpost.com with sponsor phrases ("Best Financial Hack", "Making Insurance Easy", "CBRE challenge").
- Mined already-analyzed all_records.jsonl prize lists.

## Caveats
- Placement is "unknown" nearly everywhere (badges say only "Winner <sponsor>"); only UXperience 2025 CBRE lists 1st/2nd/3rd.
- Some event dates null (WEHack 2025, ShellHacks 2025, HackNC 2025 end etc. not stated on pages).
- Prompts file includes a few pre-window reference rows (HackSMU V 2023, HackUTA 2023, Formula Hacks 2024, Bitcamp 2024, WildHacks 2024) and CBRE-sponsored items before Nov 2024 are flagged in edition text. CBRE winners at TAMUhack 2023 / WEHack 2023 exist but are out of window (not in winners file).
- Most challenge pages give no brief (hackerpack at kickoff); Capital One briefs are formulaic (fintech open-ended, Nessie API).

## Present but winners NOT retrieved (browser dropped before finish or pages inaccessible)
- Scans queued but unfinished when Chrome disconnected: HackNC 2024 (Capital One, Nov 2-3 2024), MadHacks Fall 2024 (Capital One), HackRice 15 (Capital One, Sep 2025), Technica 2025 (Capital One, Nov 2025), Technica 2024 (Capital One, Oct 2024); gallery winners lists were collected, only part of bitcamp2025/wichacks-26 scanned before this.
- Winners lists scanned with no sponsor hit though sponsor present: HackNYU 2025 (Capital One), MHacks 2026, BigRed//Hacks 2026 (Capital One), TAMUhack 2025 beyond 1; HackHarvard 2026 gallery empty (winners not posted), HackGT 12 got 2.
- Slugs returning client_error/403 (not accessible): hackutd-2024, tamuhack2026, hacktx-2025/hacktx25, hackgt-11/13, hackprinceton-spring-2026, hacknyu-2026, bigredhacks2025, hackuta20xx, hackdfw, hacksmu-2025.

## Leads left
- Finish scans above; also HackTX 2025, HackGT 11/13, HackNYU Fall 2025, Hack the North 2025, YHack, Cal Hacks, HackRU, BoilerMake, HackKU/HackUIowa (Midwest State Farm), HackUTA 2024/2025 (State Farm), UXperience 2026, TAMUhack 2024/2026 CBRE logo, HackAI/UTD events, WEHack 2025 dates.
- Real-estate CBRE: only the internal CBRE "Innovate 2026" employee hackathon (cbre.com blog) found; not open to students.
- Non-Devpost recaps (LinkedIn/X/MLH/university news) searched via WebSearch with no usable results.

## Follow-up pass (2026-11-02)
- Faster method: from a Devpost tab, in-page fetch() of `<slug>.devpost.com/project-gallery?winners=true&page=N` (parse `a.block-wrapper-link`), then fetch each project page and read JSON-LD `award` + `.winner` badges; ~1 s/project. Cross-subdomain fetch works with credentials included.
- Fully scanned this pass (all winner-gallery projects, badge check): HackNC 2024 (94), HackRice 15 (86), HackRice 16 (Sep 11-13, 2026), Technica 2025 (127), Technica 2024 (113), MadHacks Fall 2024 (slug `madhacks`, 55), Bitcamp 2025 (231; no new beyond the 2 already recorded), WiCHacks 2026 (49; only Income Firewall, already recorded), TAMUhack 2026 (slug `th26`, 171; one Capital One winner), HackTX 2025 (slug `hacktx2025`, 226), HackNYU Fall 2025 (`hacknyu-fall-2025`, 65, no sponsors on page, 0 hits), HackPrinceton Spring 2026 (`hackprinceton-spring-26`, Apr 17-19 2026, 131 winners-flagged, 0 sponsor hits and no sponsor text on home page), HackGT 13 (`hackgt13`, Sep 25-27 2026; no Capital One/State Farm/CBRE on home page; scan stopped at roughly 175 of 268 winners with 0 hits when the tab was closed).
- Real slugs confirmed: hacktx2025, hackgt-11-circus-of-invention (home page has no target sponsors), hacknyu-2025, hacknyu-fall-2025, hackutd-ripple, yhack-2024 / yhack (Fall 2024), hackthenorth2025, hackru-fall-2024, hackru-fall-2025, boilermake-xii, hackku-2025, hacksmu-vi, hacksmu-vii, hackrice-16.
- Home pages checked with NO Capital One / State Farm / CBRE prize text: Hack the North 2025, YHack (2024 fall), HackRU Fall 2024 and Fall 2025, BoilerMake XII, HackKU 2025, HackSMU VI and VII, HackNYU Fall 2025, HackGT 11, HackGT 13. (YHack 2024 spring page only lists a Capital One person as judge.) HackDFW/HackUIowa slugs are 2015/2017 events (out of window).
- Slug probes that returned nothing: bigredhacks2025/bigredhacks-2025, hackuta-2024/2025 variants, hackunt-2025/2026, hackrice-14, hacknyu2026, hacktx25.
- Non-Devpost recaps: UTD CS news (cs.utdallas.edu tag pages) only has pre-2023 HackUTD/State Farm items; no sponsor recap naming placements/briefs for HackUTD 2024/2025 found. HackFSU 6 State Farm "100forGood" challenge is from 2019 (out of window).
- State Farm SunHacks 2025: prize "Best Hack for Safety" (1 winner, car safety kit + State Farm swag), no brief text; judging is generic Design/Originality/Functionality/Complexity.

## Remaining leads
- BigRed//Hacks 2025, HackUTA 2024/2025, HackUNT 2025, HackNYU 2026, Cal Hacks, other Texas schools (Rice done; UTSA, Texas State, Baylor, Texas Tech slugs not found), UXperience 2026, HackTX 2025 State Farm/CBRE (none on page).
- Still no real State Farm or CBRE briefs beyond the generic ones already in the prompts file.
