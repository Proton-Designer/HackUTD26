# data/tables index

Every number in outputs/ must trace to one of these tables.

| table | question | script | contents |
|---|---|---|---|
| `Q00_hackutd2025_ordinal_all.csv` | Q0 | `scripts/s6_tagged.py` | HackUTD 2025 winners vs baseline groups: medians/means of ratings and cover score (all). |
| `Q00_hackutd2025_ordinal_excl_weak.csv` | Q0 | `scripts/s6_tagged.py` | HackUTD 2025 winners vs baseline groups: medians/means of ratings and cover score (excl_weak). |
| `Q00_hackutd2025_vs_baseline_all.csv` | Q0 | `scripts/s6_tagged.py` | HackUTD 2025 winners vs demo_ready vs random non-winners, every tagged field (all). |
| `Q00_hackutd2025_vs_baseline_excl_weak.csv` | Q0 | `scripts/s6_tagged.py` | HackUTD 2025 winners vs demo_ready vs random non-winners, every tagged field (excl_weak). |
| `Q01_paired_all_tracks.csv` | Q1/Q2/Q3/Q5/Q6/Q8/Q14/Q15/Q17 | `scripts/s6_tagged.py` | 1st vs 2nd/3rd in the same event+track (all_tracks); categorical shares with gap + track-pair count; ordinal medians + per-track sign counts. |
| `Q01_paired_general.csv` | Q1/Q2/Q3/Q5/Q6/Q8/Q14/Q15/Q17 | `scripts/s6_tagged.py` | 1st vs 2nd/3rd in the same event+track (general); categorical shares with gap + track-pair count; ordinal medians + per-track sign counts. |
| `Q01_paired_sponsor.csv` | Q1/Q2/Q3/Q5/Q6/Q8/Q14/Q15/Q17 | `scripts/s6_tagged.py` | 1st vs 2nd/3rd in the same event+track (sponsor); categorical shares with gap + track-pair count; ordinal medians + per-track sign counts. |
| `Q01_paired_theme_other.csv` | Q1/Q2/Q3/Q5/Q6/Q8/Q14/Q15/Q17 | `scripts/s6_tagged.py` | 1st vs 2nd/3rd in the same event+track (theme_other); categorical shares with gap + track-pair count; ordinal medians + per-track sign counts. |
| `Q01_paired_tracks.csv` | Q1 | `scripts/s6_tagged.py` | Every paired track (published 1st + 2nd/3rd) and its projects. |
| `Q02_floor_vs_differentiator.csv` | Q2 | `scripts/s6_tagged.py` | Per rubric dimension: share of winners rated >=4 (floor if >=80%), paired 1st-minus-lower medians and per-track signs, HackUTD 2025 winners vs demo_ready medians. |
| `Q04_archetype_assignment.csv` | Q4 | TASK-105 manual assignment | general 1st -> archetype |
| `Q04_archetype_counts.csv` | Q4 | `scripts/q04_archetype_counts.py` | Per-archetype field counts (n, N, pct, weighted pct). |
| `Q04_general_1sts.csv` | Q4 | `scripts/s6_tagged.py` | Every general/overall 1st with clustering fields (pattern, ai_role, hardware, live data, novelty), centerpiece and wow moment. |
| `Q04_general_1sts_ai_role.csv` | Q4 | `scripts/s6_tagged.py` | General 1sts: distribution of ai_role (unweighted + weighted). |
| `Q04_general_1sts_has_hardware.csv` | Q4 | `scripts/s6_tagged.py` | General 1sts: distribution of has_hardware (unweighted + weighted). |
| `Q04_general_1sts_live_data.csv` | Q4 | `scripts/s6_tagged.py` | General 1sts: distribution of live_data (unweighted + weighted). |
| `Q04_general_1sts_novelty_source.csv` | Q4 | `scripts/s6_tagged.py` | General 1sts: distribution of novelty_source (unweighted + weighted). |
| `Q04_general_1sts_pattern.csv` | Q4 | `scripts/s6_tagged.py` | General 1sts: distribution of pattern (unweighted + weighted). |
| `Q04_general_1sts_pattern_x_ai.csv` | Q4 | `scripts/s6_tagged.py` | General 1sts: pattern x ai_role counts (unweighted and event-type weighted). |
| `Q06_general_1st_centerpieces.csv` | Q6 | `scripts/s6_tagged.py` | Technical centerpiece text and visibility for every general 1st. |
| `Q07_novelty_general1_vs_sponsor1.csv` | Q7 | `scripts/s6_tagged.py` | Novelty source (and pattern, ai_role) among general 1sts vs sponsor 1sts. |
| `Q09_award_concentration.csv` | Q9 | `scripts/s6_q09_stacking.py` | Share of all awards held by the top 10% of projects. |
| `Q09_general_1st_also_sponsor.csv` | Q9 | `scripts/s6_q09_stacking.py` | Share of general-track winners (1st / any place) that also won a sponsor, MLH or side prize. |
| `Q09_kind_pairs.csv` | Q9 | `scripts/s6_q09_stacking.py` | Prize-kind pairs held by the same project (multi-award projects only). |
| `Q09_n_awards_dist.csv` | Q9 | `scripts/s6_q09_stacking.py` | Distribution of awards per winning project, by event type (projects, not awards). |
| `Q09_two_sponsor_combos.csv` | Q9 | `scripts/s6_q09_stacking.py` | Among projects with 2+ sponsor prizes: which sponsor prize kinds they combined. |
| `Q10_sponsor_fit_by_placement.csv` | Q10/Q12/Q14 | `scripts/s6_tagged.py` | Awarding-sponsor fit (removable, features used, prompt literalness, prompt words in title, problem owner, completeness) by sponsor prize kind and placement. Sponsor_fit matched to award for 530 of 541 sponsor awards. |
| `Q11_pattern_x_industry.csv` | Q11 | `scripts/s6_tagged.py` | Pattern x sponsor_industry for all sponsor-prize winners (projects), with examples and how many also won general. |
| `Q13_sponsor_card_rows.csv` | Q13 | `scripts/s6_tagged.py` | One row per past award from a HackUTD 2026 sponsor: project, placement, pattern, problem owner, literalness, centrality, completeness. |
| `Q13_sponsor_card_stats.csv` | Q13 | `scripts/s7_sponsor_cards.py` | Per-sponsor counts (pattern, problem_owner, literalness, removable, features used) for sponsor_cards.md. |
| `Q15_cover_distribution_all.csv` | Q15 | `scripts/s6_tagged.py` | Cover-test score distribution over every tagged project with a valid cover score (ceiling check). |
| `Q15_cover_examples_1sts.csv` | Q15 | `scripts/s6_tagged.py` | Cover-test score with exact title + tagline for every tagged 1st (best/worst tagline examples). |
| `Q15_cover_hackutd2025.csv` | Q15 | `scripts/s6_tagged.py` | Cover-test score distribution: HackUTD 2025 winners vs baseline groups. |
| `Q16_wow_moments_1sts.csv` | Q16 | `scripts/s6_tagged.py` | Wow moment (from page text, not video) for every 1st; videos were not watched. |
| `Q18_page_contents.csv` | Q18 | `scripts/s6_tagged.py` | Devpost page checklist prevalence: general 1sts, sponsor 1sts, HackUTD 2025 winners vs baseline. |
| `Q19_hackutd2025_award_integration_counts.csv` | Q19 | `scripts/q19_hackutd2025_group_counts.py` | Sponsor integration depth per award; from manual close-read judgments. |
| `Q19_hackutd2025_domain_track_prompt_fit.csv` | Q19/Q0 | `scripts/q19_hackutd2025_group_counts.py` | Prompt-fit level, company-problem tracks only. |
| `Q19_hackutd2025_group_counts.csv` | Q19/Q0 | `scripts/q19_hackutd2025_group_counts.py` | n of N per group per metric with names; depth-A-only sensitivity rows. |
| `Q19_hackutd2025_named_user_counts.csv` | Q19/Q0 | `scripts/q19_hackutd2025_group_counts.py` | Named-user judgment, winners vs demo_ready. |
| `Q19_hackutd2025_per_project.csv` | Q19/Q0 | `scripts/q19_hackutd2025_group_counts.py` | HackUTD 2025 winners vs demo_ready vs random, per project. |
| `Q19_hackutd2025_track_targeting.csv` | Q19/Q0 | `scripts/q19_hackutd2025_group_counts.py` | Track targeted per group; winners = track won. |
| `Q20_recent_vs_older.csv` | Q20 | `scripts/s6_tagged.py` | Winners since 2025-06 vs older: ai_role, hardware, live data, pattern (unweighted + event-type weighted). |
| `Q23_place_not_first.csv` | Q23 | `scripts/s6_tagged.py` | In tracks with a published 1st: patterns/ai_roles over-represented among 2nd/3rd/HM vs 1st (association). |
| `Q99_unknown_rates.csv` | data quality | `scripts/s6_tagged.py` | Unknown/na rate per field across all tagged projects. |
