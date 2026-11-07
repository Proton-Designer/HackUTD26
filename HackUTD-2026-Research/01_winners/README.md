# 01_winners: first-pass project records (winners)

Data-collection step only. Each project gets one structured record of observed facts and short paraphrases. Cross-project patterns are a later step.

> Non-winners are in `../02_baseline_non_winners/`; sponsor-prize winners and the prompt library are in `../03_sponsor_tracks/`; the deeper read of every project is in `../04_deep_dives/`. See `../README.md` for the map.

## What is here
| Path | What it is |
|---|---|
| `HackUTD_Research_project_analysis.xlsx` | The workbook. Tabs: Projects (one row per project), Prizes, Tech_APIs, Project_Notes, Sources, Data_Dictionary |
| `data/project_records.jsonl` | The same 911 records, one JSON object per line, for scripting |
| `../05_master_winner_lists/HackUTD_winners_master_v2.md` / `.csv` | Master list of winners across 60 hackathons (2,475 prize rows). It is the source queue for any further projects |
| `project_cards/` | Readable one-card-per-project files, one file per hackathon |
| `DATA_DICTIONARY.md` | Every field, allowed values and rules |
| `../99_archive_superseded/` | The earlier HackUTD-only files, now included in the files above |

## Coverage: 911 projects, 47 hackathons, 92 editions
- **HackUTD 2024 and 2025:** all 72 winning projects (the 73rd queue entry was a duplicate listing).
- **The 15 other large events** (Cal Hacks, TreeHacks, HackMIT, LA Hacks, HackGT, Hack the North, DubHacks, Bitcamp, ConUHacks, UC Berkeley AI Hackathon, HackUMass, StormHacks, UNIHACK, Junction, HackEurope): 305 projects, namely the overall placements, track winners and finalists.
- **Wave 3, placed winners at 31 smaller events:** 264 projects whose prize text names a 1st, 2nd or 3rd place or a placed sponsor prize (HackUPC, TAMUhack, Hacklytics, HackNC, HackIllinois, VTHacks, YHack, PennApps and others).
- **Waves 4-5, big-event sponsor/track winners (all remaining):** 270 records covering the unranked sponsor-prize and track winners at the 11 big events (Bitcamp, HackGT, Cal Hacks, HackUMass, StormHacks, LA Hacks, TreeHacks, DubHacks, ConUHacks, Berkeley AI, UNIHACK). Bundled queue entries were split into one record per project where read.
- **Not yet analyzed:** about 1,340 mostly unranked winners at 42 smaller events. All are in the master winners list.

## Data quality
- Confidence: 628 high, 263 medium, 20 low (later waves are mostly medium or high but read from short extracts, so tech depth and AI types are partly inferred).
- GitHub: 783 projects link a repo, 724 had their commit history read by cloning (commit counts, first/last commit, languages, README size, and commits before, during and after the event window where dates are known). 36 list no repo and 23 repos were private or missing.
- 4,788 technology/API entries are recorded with how deeply each was used (core, supporting or token).
- Event dates are filled for 450 projects; most wave-3 editions have no dates yet, so their commit-window fields are blank. Some came from memory or news articles and are flagged unverified.

## Known limits
- **Wave 3 rank handling:** "1st Runner Up" is recorded as 2nd and "Second Runner-Up" as 3rd (flagged in unverified_fields). Placements stay "unknown" where a prize name lists the whole 1st/2nd/3rd scale. Two HackIllinois records carry an `edition_mismatch` flag because the winner badges on their pages belong to other hackathons.
- **Six records with no project page** (3 hackCBS, 3 HackOut teams, plus a few others) are low confidence and built from official reports or queue data.
- **Placements:** 1st/2nd/3rd is recorded only where a page or prize name states it. Devpost usually shows the track, not the rank. HarmoniQ's 3rd in the HackUTD 2025 T-Mobile track is from the team.
- **UI polish** is blank for most projects (it needs a look at screenshots), and **live demos** were not opened.
- **Sponsor flags** (`is_sponsor`) are often inferred, because sponsor lists were not always on the event page.
- **Team size** is counted from names shown on the page and can be off by one. No names are stored.
- **HackMIT** moved off Devpost, so its records come from plume.hackmit.org. HackMIT 2024 has no findable project page.
- **Domain, idea type and tech depth** are one reader's reading of each project, not organizer categories.
- Several public HackUTD repos appear to contain env or credential files. Their contents were not opened, but the owners may want to check for leaked keys.

- **Wave 4 notes:** a few queue entries bundled several projects under one ID. One (10 Fetch.ai winners at Berkeley AI 2026) was split into 10 records; three DubHacks 2025 and two LA Hacks 2025 bundles were only partly read and are flagged `bundled_projects_not_read`. Every placement in wave 4 is "unknown" because no prize name states a rank. Better Call Saul AI (ConUHacks IX) is a queue-only record because its page 404s.

- **Date corrections:** ConUHacks IX is 2025-02-01 to 02 (earlier records wrongly carried ConUHacks X's 2026 dates); Cal Hacks 13 and LA Hacks 2026 dates were filled in. Their commit-timing fields were recomputed.
