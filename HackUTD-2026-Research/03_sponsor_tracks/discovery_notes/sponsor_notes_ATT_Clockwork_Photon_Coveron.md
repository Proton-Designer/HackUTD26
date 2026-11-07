# Sponsor discovery notes (in progress; see end for final status)
## Approaches
- Devpost hackathon pages (prize lists) fetched cross-origin from a devpost.com tab, then each hackathon's project-gallery?winners=true pages scanned and every project page checked for the prize badge (more reliable than the search JSON 'winner' flag).
- Devpost software search JSON (rate-limited, 429s from shared IP).
- Photon weekly updates (photon.codes/weekly-update/*) for list of hackathons Photon sponsored.
- WebSearch was nearly useless for all four sponsors.
## Photon
Hackathons with Photon prizes found: HackPrinceton Fall 2025, MHacks 2026, HackNC 2026, Hacklanta 2026, DubHacks 2026, LA Hacks AI Hackathon 2026, HackHarvard 2026 (winners not badge-confirmed). Also non-hackathon Photon contests (Best iMessage Agent Contest, winners Dibs/Adaam/House Force One/BailMeOut; Muse contest) and events w/o public winners (GMI Cloud hackathon, Total Agent Recall, Matcha & Code, MultiModel, Moonlight Hackathon Night winner 'Six Degrees').

## Clockwork Labs / SpacetimeDB
- Devpost prize name is "[Spacetime] Best Use of Spacetime" (not "SpacetimeDB"/"Clockwork Labs"), so searches for those names miss it.
- Cal Hacks 13.0 (Oct 23-25 2026 per Devpost; Spacetime was a presenting sponsor): 9 winners, all 9 found (Bandit, GeonosisAI, Rally, Orkio, Ender's Bench, Luyten, skyFall, Pacioli, Vouch). Placements (1st $2048/2nd $1024/3rd $512) are not shown on project badges. A separate "Scrabblebot Tournament" prize (1st $1024, 2nd $512, 3rd $256; clockworklabs/scrabblebot repo) had no Devpost badge; winners not found.
- MHacks 2026 (Oct 3-4 2026): "Best Use of Spacetime" 3 winners: scalpal., Traycer, CoClip.
- Devpost search 'SpacetimeDB' is capped at 72 results (all Cal Hacks 13); other hackathons with Spacetime prizes could not be surfaced that way. Probed (no Spacetime text): TreeHacks 2025/2026, HackUTD 2025, HackGT 12, Cal Hacks 11/12, HackIllinois 2026, HackPSU, HackRice 15, HackNC 2026, DubHacks 2026, Hacklanta, LA Hacks AI 2026, HackHarvard 2026.
- No blog/X winner posts found via WebSearch (spacetimedb.com/community page has none). Leads: Clockwork Labs X (@clockwork_labs, @spacetime_db) and Discord; clockworklabs GitHub org; Cal Hacks 13 gallery for Scrabblebot winners; TreeHacks 2026 and HackMIT 2025 sites outside Devpost.

## AT&T
- No AT&T hackathon prize/challenge found on any 2024-2026 Devpost hackathon checked. HackUTD 2025 Devpost sponsor/prize list has no AT&T (sponsors: PNC, T-Mobile, Goldman Sachs, State Farm, Northmark C2, EOG, Toyota Financial, Nvidia, Capital One, CBRE, Scale, Cognizant). HackUTD 2024 Devpost page (hackutd-2024.devpost.com) was not readable (403 for fetch, empty page in browser): LEAD, AT&T may have been there; try hackerpack/Notion or Wayback. Devpost search 'AT&T prize' (60 results) had no AT&T-prize winners. WebSearch only returned old (2012-2018) AT&T-run hackathons. HackUTD sponsors rotate; T-Mobile (not requested) appears at HackUTD 2025 and DubHacks 2026.

## Coveron
- Not conclusively identified. Only evidence: Devpost project TraceTag (https://devpost.com/software/tracetag-42s3hd, The Blueprint Hackathon) lists "NordVPN, NordPass, Incogni, Saily, Coveron" as sponsor products, i.e. Coveron appears to be a Nord Security product/brand tied to a Nord Security challenge (The Blueprint Hackathon prizes list NordVPN/NordPass/NordProtect/Incogni). Searches for Coveo/Convex/Coverflex hackathon prizes found nothing that matches. No Coveron-labelled prize or winners found. Recommend asking the user whether they mean Nord Security (their challenge often appears as "Best Cybersecurity Hack"/Nord) or Convex.

## Photon (details)
- Hackathons with confirmed Photon prizes and badge-verified winners: HackPrinceton Fall 2025 (5 winners), MHacks 2026 (2 found: Tab, Concierge; prize lists 2), HackNC 2026 (2), Hacklanta 2026 (2), DubHacks 2026 (3), LA Hacks AI Hackathon 2026 (3).
- HackHarvard 2026 (Oct 16-18): Photon 2.0 track (winner/runner-up/best voice agent) exists but Devpost winners gallery shows no per-prize badges yet; 7 gallery winners mention Photon (listed as UNCONFIRMED in the winners file). Re-check after organizers publish prizes.
- Photon events with no Devpost winners available: GMI Cloud hackathon (Mar 2026), Total Agent Recall (Apr 2026), MultiModel Hackathon (Apr 18, 'Best Photon Interfaces'), HackPrinceton Spring 2026 (track 'Agents in iMessage'; Devpost slug not found), Matcha & Code (May 2), Moonlight Hackathon Night (winner 'Six Degrees'), Eazo, Seattle AWS hackathon. Non-hackathon Photon contests: Best iMessage Agent Contest (Sept 2026; winners Dibs, Adaam, House Force One, BailMeOut), 'Make Your Own Muse' (due Oct 19).
- Notion guidelines page (somethingreat.notion.site/Hackathon-Guidelines-for-Photon-2-0...) not fetchable (JS-rendered).
## Other tools notes
- Devpost project pages for just-finished hackathons (HackHarvard 2026) may not show prize badges yet.
