# Sponsor prize winners and challenge prompts (HackUTD prep)

Separate from the main winners dataset and from the non-winner baseline. Covers winners of prizes sponsored by NVIDIA, Capital One, State Farm, CBRE, Photon, Clockwork Labs (SpacetimeDB), the Nord family (NordVPN, NordPass, Saily, Incogni) and AT&T, at hackathons from Nov 2024 to Nov 2026.

## What is here
| Path | What it is |
|---|---|
| `Sponsor_prize_winners_analysis.xlsx` | Tab **Projects**: 141 newly analyzed sponsor winners (same columns as the winner workbook plus `sponsors`). Tab **Winner_Index**: all 178 sponsor-prize rows found, including 37 already analyzed in the main winners dataset (`already_analyzed`). Tab **Prompt_Library**: 114 challenge prompts. Other tabs as in the winner workbook |
| `sponsor_prompt_library.md` | The same prompts, grouped by sponsor, readable |
| `data/project_records.jsonl` | The 141 analyzed records |
| `project_cards/` | Readable cards |
| `discovery_notes/` | Per-sponsor notes: approaches tried, events where the sponsor was present but winners were not found, open leads; the 9 winner rows with no project link |

## Counts (winner rows found / of which not yet analyzed before this batch)
NVIDIA 54/42, Capital One 43/40, Photon 24/21, CBRE 17/11, Nord family 15/5, State Farm 13/10, Clockwork Labs 12/12, AT&T 0. "Coveron" looks like a Nord product name and has no prize of its own.

## What to know
- **Ranks:** only 33 of 178 rows have a stated 1st/2nd/3rd. Devpost badges usually say just "Winner <sponsor prize>".
- **Prompts are thin:** most sponsor briefs are sent privately at kickoff (HackUTD uses a hackerpack). Capital One's brief is usually an open fintech theme with the Nessie API optional. Several prompts are only prize tiers.
- **Winning does not require the sponsor tool:** the analysis records `sponsor_fit_note` for each project. Examples: 10 of the Capital One winners in the first batches never named a Capital One API; none of the 9 State Farm winners used a State Farm API (the theme was insurance, safety or financial education); the Nord winners used no Nord product. For NVIDIA, Jetson and Nemotron/NIM winners did use the hardware or model as a core part of the build. All Spacetime winners used SpacetimeDB as the core backend.
- **Medium confidence (15 records):** mostly cases where the prize was a sponsor-bundle reward with no sponsor tool used, 7 HackHarvard 2026 Photon entries whose pages show no prize badge yet (unconfirmed), and a few thin writeups.
- **Dates:** some event end dates are best guesses (flagged per record). `ui_polish` is blank and live demos were not opened.
- **Coverage is partial** (listing APIs stop early, some hackathon sites would not load); see `discovery_notes/` for what is left.
- Project IDs here start with `sponsor-`; match to other datasets by name and edition.
