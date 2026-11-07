# HackUTD 2025 BASELINE: NON-WINNING projects

**These are NOT winners.** They are a comparison sample for the winner dataset in `../01_winners/`. Every record has `is_winner = false`, `placement_tier = baseline_non_winner` and no prizes.

## What is here
| Path | What it is |
|---|---|
| `HackUTD2025_BASELINE_non_winners.xlsx` | Same tabs and columns as the winner workbook, plus a `sample_group` column |
| `data/project_records.jsonl` | The 100 records, one per line |
| `project_cards/` | Readable cards |
| `DATA_DICTIONARY.md` | Same schema as the winner dataset |

## How the 100 were chosen
- Gallery: 366 HackUTD 2025 submissions on Devpost. All 36 winner-flagged projects were removed, plus 2 duplicate entries, 1 name collision (inSIGHT vs the winner InsighT) and 2 junk names, leaving a pool of 325.
- **demo_ready (50):** the most-engaged pool projects (likes plus comments) that list both a GitHub repo and a video.
- **random (50):** a seeded random draw (`random.seed(2025)`) from the other 275, so it includes weak and empty entries on purpose. It is the honest picture of an average submission.
- To compare winners with the baseline, use `demo_ready` as the fair comparison (complete projects that did not place) and `random` as the typical entry. Keep them apart.

## Data quality
- Confidence: 38 high, 51 medium, 11 low. About 10 low records are empty templates or placeholder pages (e.g. "Placeholder", "idk", "Team Registration"); the notes say what each page really is.
- Slice 2 (20 projects) was read more thinly than the others (only a short extract per page), so its writeup sections, AI types and tech depth are partly guessed and flagged in `unverified_fields`.
- 75 of 100 list a GitHub repo; 70 had commit history read. Event window is 2025-11-08 to 2025-11-09. `ui_polish` is blank and live demos were not opened, as in the winner set.
- Sponsor flags are judgment calls (Gemini, Auth0, ElevenLabs, NVIDIA Nemotron and similar were treated as sponsor/MLH tools) and are listed in `unverified_fields`.
- Note: baseline `project_id`s use the prefix `hackutd-hackutd-2025-`, while the older winner records use `hackutd-2025-`. Match on name and edition, not ID.
