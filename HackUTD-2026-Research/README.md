# HackUTD 2026 Research

> **Analysis phase (step 5):** start with `00_START_HERE.md`, then `01_ANALYSIS_SPEC.md` and `02_PIPELINE.md`. New analysis work goes in `data/`, `scripts/` and `outputs/`; background is in `reference/`.

Research on past hackathon winners (and a non-winner baseline) to understand what wins at HackUTD and its sponsor tracks. Pipeline: (1) hackathon list, (2) winners compilation, (3) per-project analysis, (4) deeper per-project read (done), (5) pattern analysis and playbook (not started).

Everything is observed fact and short paraphrase. No claims about why anything won yet.

## Start here
| If you want... | Open |
|---|---|
| One searchable list of all 1,152 projects, with links to each project's full profile | `ALL_PROJECTS_INDEX.csv` |
| To read how a specific project works (features, flow, prompt fit, gaps) | `04_deep_dives/profiles/<winners|sponsor|baseline>/<hackathon-edition>.md` |
| To filter and sort everything in a spreadsheet | `04_deep_dives/HackUTD_Deep_Dives.xlsx` |
| Sponsor challenge text collected so far | `04_deep_dives/prompts_cache/` and `03_sponsor_tracks/sponsor_prompt_library.md` |
| Tech stack, commit-timing and other first-pass metrics | `01_winners/HackUTD_Research_project_analysis.xlsx` |

## Folder map
| Folder | Contents | Records |
|---|---|---|
| `01_winners/` | First-pass records, workbook, readable cards, data dictionary for the winners dataset | 911 |
| `02_baseline_non_winners/` | HackUTD 2025 non-winners, kept separate as a comparison sample | 100 |
| `03_sponsor_tracks/` | Sponsor-prize winners (NVIDIA, Capital One, State Farm, CBRE, Nord, Photon and others), prompt library, discovery notes | 141 |
| `04_deep_dives/` | Deep read of every project from the three datasets above (Devpost page, README, prize text), plus collected prompt text | 1,152 |
| `05_master_winner_lists/` | Master list of winners across 60 hackathons (about 2,475 prize rows); the source queue if more projects are added | n/a |
| `99_archive_superseded/` | Old intermediate files; safe to ignore | n/a |

The three datasets stay labeled everywhere: the `dataset` column (winners, sponsor, baseline) and the folder each profile sits in. Winner and non-winner data are never mixed in one file except the combined index and the deep-dive files, where `dataset` and `placement_tier` identify each project.

## Deep-dive coverage (04_deep_dives)
- 871 projects have a Devpost page plus a real README or repo evidence (depth A), 255 have one source (B), 26 are thin or unreachable (C).
- Confidence: 579 high, 529 medium, 44 low.
- 289 projects are flagged as candidates for a second pass; `ALL_PROJECTS_INDEX.csv` has a `needs_second_pass` column and `04_deep_dives/second_pass_queue.txt` lists them.

## Known limits
- Many sponsor briefs are not public (HackUTD 2024/2025 challenges were in a hackerpack; HackMIT 2026 and several sponsor prizes list only a name). Those records say so.
- Devpost pages and READMEs often disagree; deep-dive records keep both and note which one the feature list follows.
- Depth labels are agent-assigned and not perfectly consistent; some depth-A records have boilerplate READMEs.
- Placements are known only where a page or prize name states them; some are contradictory and flagged.
- Two pairs of listings share one Devpost page (ProDuh, MayDay) and are marked `duplicate_of`.
- About 1,340 mostly unranked winners at 42 smaller events are in the master list but have not been analyzed.
- Videos were not watched; live demos mostly not opened.
- Team names, access codes and credentials are not stored. Two Devpost pages (Constructa, Navo) displayed live-looking API keys, and several public HackUTD repos may contain env or credential files; the owners should check and rotate.

## Open items
1. Second pass on the flagged projects.
2. HackUTD 2026 action sheet (what to build and target this weekend). Sponsor briefs for all 17 sponsors are now in 06_hackutd_2026_sponsors/ (start with its README.md).
3. Pattern analysis and playbook across the datasets.
4. ConUHacks IX/X sponsor prize listings are now saved in 04_deep_dives/prompts_cache/ (rewards only; those sponsors publish no problem statements).
