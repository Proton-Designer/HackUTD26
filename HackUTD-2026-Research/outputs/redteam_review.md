# S8 Red-team review of `outputs/findings.md` (TASK-104, eng2)

Reviewer did not write findings.md. Every claim below cites a table row in `data/tables/`. Checks per finding: (1) recompute numbers, (2) spec §1 rules, (3) robustness (excl_weak, noise, omitted counterexamples), (4) implication vs support, no time/duration estimates.

Scope note: `archetypes.md` and `sponsor_cards.md` got a lighter pass (section 5).

**Tally (27 findings): HOLDS 3 · WEAKEN 22 · DROP 2. Numeric/citation errors: 11 (section 3).**

Noise yardstick used throughout: a gap of fewer than ~3 projects, or whose two cell sizes are about 17 vs 27, is within noise. Sign-test margin on 54 vs 36 non-tied tracks is z≈1.9 (p≈0.06); 52 vs 38 is z≈1.5 (p≈0.14).

---

## 1. Verdict per finding

### 0. HackUTD 2025 winners vs non-winners

**0.1 HOLDS (small reword).**
- Numbers match `Q00_hackutd2025_vs_baseline_all.csv` (n_user_flows: 2 flows W 8/35 (23%), D 0/47, R 1/42 (2%); 0 flows W 1/35, D 9/47 (19%), R 11/42 (26%)). excl_weak: 8/34 (24%), D 0/45, R 1/37 (3%) ✓. Close read ✓: `Q19_hackutd2025_group_counts.csv` shown_working_ge_1 W 27/36 (75%), D 21/50 (42%), R 17/50 (34%), median shown working W 2 vs D 0 vs R 0.
- Reword: ">2 flows" is not zero for D (2 of 47, 4%; R 2 of 42), so say "two flows: W 8 of 35 vs D 0 of 47", not "almost never show two or more".
- Extra support available: shown_working_ge_3 W 12/36 (33%) vs D 8/50 (16%); depth-A-only W 12/29 (41%) vs D 8/30 (27%).
- Also state the one-flow row: W 25/35 (71%) vs D 36/47 (77%), so "one flow" does not separate.

**0.2 HOLDS.**
- Numbers match `Q00_..._all` ai_role: agentic W 17/36 (47%), D 14/50 (28%), R 8/50 (16%); single-call-or-none W 13/36, D 22/50, R 28/50 ✓ (6+7, 10+12, 11+17). excl_weak 17/35 (49%), 13/46 (28%), 7/39 (18%) ✓.
- Caveat to add: `single_call_wrapper` alone shows no gap (W 6/36 17%, D 10/50 20%, R 11/50 22%). The gap is carried by `none` and `rag_or_chat` (W 2/36 vs D 7/50). Say "single-call or no-AI" only as the combined row.
- Gap is 19 points on 36 vs 50 (about 7 projects); medium confidence is fair.
- Conflicts with 7.2 (see 7.2).

**0.3 WEAKEN (implication overreaches).**
- Numbers ✓: data_to_decision W 8/36 (22%), D 24/50 (48%), R 20/50 (40%); excl_weak 23%/50%/46%.
- The W group is winners of ALL tracks (sponsor and General) and cannot isolate "General track". The implication ("For the General track, avoid a plain analytics dashboard") is better supported by `Q07_novelty_general1_vs_sponsor1.csv`: data_to_decision general 1sts 4/65 (6%) vs sponsor 1sts 14/54 (26%). Cite that for the General advice; the Q00 row only shows winners are rarer than strong non-winners in this shape.
- "Half as common" ✓ (22% vs 48%). The counterexample (T-Mobile dashboards win a sponsor track) is correct and should sit in the SUPPORT line: pattern wins sponsor tracks (14/54).

**0.4 WEAKEN.**
- Numbers ✓ (completeness ≥4 W 8/36, D 3/50; presentation 11/36, 7/50; technical 12/36 vs 14/50; innovation 1/36 vs 3/50; impact median 2.5 vs 3).
- Gap is 5 projects (completeness) and 4 projects (presentation) on 36 vs 50, from the two weakest-agreement fields (spot-check: presentation 5/10 and 3/10; `findings.md` §8). Medians are identical (3 vs 3) for completeness and presentation (`Q00_hackutd2025_ordinal_all.csv`).
- Reword "rated higher" to "more often rated ≥4 (8 vs 3 projects; 11 vs 7)". Downgrade to low–medium confidence. The implication ("put effort into a finished core flow and clear presentation") is a reasonable inference but should say so.
- excl_weak holds in direction: completeness 8/35 vs 3/46, presentation 11/35 vs 7/46.

**0.5 WEAKEN (one claim false).**
- Numbers ✓: diagram/logs W 7/36 (19%), D 3/50 (6%), R 1/50 (2%); demo output W 11/36 (31%), D 11/50 (22%), R 3/50 (6%); described-only W 10/36 (28%), D 21/50 (42%).
- "Non-winners more often only describe it" is false against `random`: described-only R 13/50 (26%) < W 10/36 (28%) (R is mostly `none`: 33/50, 66%). It is true only against `demo_ready`. Reword to "strong non-winners (demo_ready) more often only describe it".
- Cleaner stat: visible (diagram/logs + demo output) W 18/36 (50%), D 14/50 (28%), R 4/50 (8%).
- Tension to disclose: within tracks the pattern reverses. General 1sts show it in demo output 30/61 (49%) vs 2nd/3rd 67/117 (57%); described-only 19/61 (31%) vs 25/117 (21%) (`Q01_paired_general.csv`; excl_weak 51% vs 60%, 32% vs 22%). Winner-vs-non-winner and 1st-vs-lower are different questions and 0.5/3.2 should say so.

**0.6 WEAKEN.**
- Numbers ✓ (0 images W 0/34, D 9/50 (18%), R 20/50 (40%); cover 3/3 W 30/36 (83%), D 43/49 (88%), R 33/49 (67%)).
- "Every 2025 winner page had images" overstates: 2 of 36 winners have unknown image count (`Q18_page_contents.csv`, hackutd2025_winners_unknown = 2). Say "none of the 34 with a known count had 0 images".
- "COUNTEREXAMPLES: none for images" is wrong. `Q18_page_contents.csv` n_images = 0: general 1sts 5/58 (9%), sponsor 1sts 12/46 (26%). Add these.
- The floor claim is also weak against D: 41/50 (82%) of demo_ready have images, so images separate winners from `random` only (R 40% with none), not from the fair comparison group.
- excl_weak: R none drops to 10/39 (26%) (`Q00_..._excl_weak.csv`), so the W-vs-R image gap is smaller than the headline.

**0.7 WEAKEN (keep hardware as low n; drop or demote the dependency claim).**
- Numbers ✓: hardware W 5/35 (14%), D 1/49 (2%), R 3/44 (7%); deps 5–7: W 8/36 (22%), D 3/50 (6%), R 3/50 (6%).
- D hardware n=1 and R n=3 are low n (<5). The finding says low confidence but must also write "low n" next to the cells (spec rule 3).
- `n_external_deps` is a script count of listed tech items (spec §2.0.1), so it tracks how thoroughly a page lists its stack. W also have longer write-ups (`Q19`: writeup_long W 20/36 (56%), D 22/50 (44%); writeup_ge_6_sections W 32/36 (89%) vs D 37/50 (74%)). Confound: deps may reflect page detail, not build breadth.
- Contradicts 3.1: 0.7 says "more integrations are fine" while 3.1 caps at ≤4 services. Reconcile or drop one.

### 1. Archetypes

**1.1 WEAKEN (reword "cluster").**
- Numbers ✓ (`Q04_general_1sts_pattern.csv`, `_ai_role.csv`, `_has_hardware.csv`, `_live_data.csv`, `_novelty_source.csv`): sensor 10/65, vision 10/65, game 8/65, data_to_decision 4/65, rag_or_chat 1/65, multimodal 21/65, none 15/65, agentic 10/65, single_call 6/65, hardware 23/65 (35%), live 40/65 (62%), combination 25/65 (38%), new_interaction 15/65 (23%). Examples exist in `Q04_general_1sts.csv` (Duet, Pyrosense, SeeForMe, Scrub+, Quota).
- The pattern table has 14 values; the top three are 28/65 (43%). "Cluster around physical-world input" is supported only if sensor+vision+voice+spatial are pooled: 26/65 (40%). Say "the three most common patterns are sensor (15%), vision (15%), game/social (12%)". There is no non-winner comparator, so "not dashboards or chatbots" is a statement about prevalence only (the TYPE line already says so).
- Better comparative support exists (spec rule 2c): general vs sponsor 1sts in `Q07` (see section 4).

### 2. 1st vs 2nd/3rd

**2.1 WEAKEN.**
- Cited numbers ✓ (`Q01_paired_all_tracks.csv`: cited_stat 29/129 (22%) vs 28/224 (12%), 10 pts, 127 tracks; general 18/61 (30%) vs 16/117 (14%); sensor 10/61 (16%) vs 6/117 (5%); education_feedback 2/61 (3%) vs 16/117 (14%)). No row in the three cited Q01 files has `flag_gap20_pairs5 = True` ✓.
- But "No tagged field separates 1st from 2nd/3rd" is broader than the evidence:
  - `Q01_paired_theme_other.csv` has 5 rows flagged: rating_design_ge4 10/17 (59%) vs 8/31 (26%) (gap 33, 15 pairs, all and excl_weak) and n_user_flows=1 20/24 (83%) vs 21/34 (62%) (gap 21, 24 pairs).
  - `Q10_sponsor_fit_by_placement.csv` sponsor_domain prompt_literalness=2: paired_1st 14/16 (88%) vs paired_2nd_3rd 18/27 (67%): a 21-point gap, which meets the spec threshold if ≥5 pairs, and it is Finding 4.2's own number. 2.1 and 4.2 contradict each other.
  - Scope the claim to "in the all-track, general and sponsor paired tables (Q01)".
- "Largest general-track gaps" is mis-ordered: page_has_accomplishments_section True 39/54 (72%) vs 87/104 (84%) is a 12-point gap, larger than sensor/education (11).
- The sentence "(likely the live pitch and judge Q&A…)" is a guess about why judges chose; spec rule 8 says write "not explained by available evidence" only. Delete "likely…".
- Confidence "high" is not warranted: tagger agreement on categorical fields is 67–84%, so noisy tags shrink real differences. "Not detected" ≠ "not different".

**2.2 WEAKEN.**
- Numbers ✓ (`Q02_floor_vs_differentiator.csv`; tracks higher/equal/lower technical 54/37/36, presentation 52/37/38, completeness 47/42/38, impact 38/45/44; general presentation 26/20/14, median 4 vs 3).
- "1sts lead slightly on technical complexity and presentation" is within noise: 54 vs 36 (z≈1.9) and 52 vs 38 (z≈1.5). In excl_weak presentation is 48/38/37 (11 apart) and technical 52/36/35 (`Q01_paired_all_tracks.csv`). Innovation (36/56/35) and impact (38/45/44) show it is the same noise level.
- Rating the 1st higher is not "where 1sts edge out 2nd/3rd" in a usable sense; the paired median gap is 0.0 on all six (as the same finding says). The implication contradicts 2.1 ("nothing separates"). Reword: "no dimension separates; technical and presentation lean toward 1st but within noise".

**2.3 WEAKEN.**
- Numbers ✓ (rating_min 47/46/34 all, 21/24/15 general, medians 3 vs 2; spread 42/42/43).
- "More balanced, not spikier" does not follow. If minimum is higher and spread (max−min) is the same (42/42/43), the whole profile is shifted up, not more balanced. 47 vs 34 non-tied tracks is not distinguishable from zero (z≈1.4).
- The implication ("guard every dimension") is generic advice; remove the "balanced" claim. Rating min/spread are allowed within-event analyses (spec rule 5), but state it as low confidence.

### 3. Minimum build

**3.1 WEAKEN.**
- Numbers ✓ (general 1sts 1 flow 42/58 (72%), 2 flows 10/58 (17%), 0 flows 5/58 (9%) vs lower 71%/10%/14%; deps 0–2 23/61, 3–4 27/61, 5–7 9/61).
- "Mocked parts disclosed where stated: 35 of 35" is close to tautological. By the field definition (absence = unknown, rule 4) a `yes` can only be written when the page states the mock. Lower placers are 61/63 (97%) (`Q01_paired_general.csv`), so there is no contrast either. Remove it as evidence for "say what is simulated".
- Implication "≤ 4 external services" as a cap: 1sts with 5+ deps are 9/61 (15%) general and 30/129 (23%) all tracks (24 at 5–7, 6 at >7), and HackUTD 2025 winners with 5–7 are 8/36 (22%) vs D 3/50 (6%). A prevalence cap is not a rule; phrase as "most (82%) used ≤4".
- The 5 general 1sts with 0 flows are acknowledged; add that n_user_flows is page-text-only for every row, so "flows shown" is a documentation measure.

**3.2 WEAKEN (one false parenthetical).**
- Numbers ✓ (21, 15, 10, 7, 6, 5 of 65; paired 30/61 (49%) vs 67/117 (57%); described only 31% vs 21%).
- "none 15 of 65 (23%, mostly hardware/systems)": only 7 of the 15 ai_role=none rows have has_hardware=True (47%) (`Q04_general_1sts.csv`). "Mostly" is wrong.
- Headline "usually a multimodal pipeline or custom hardware": the union of multimodal OR hardware is 38/65 (58%); multimodal alone is 32%. Write "58% (38 of 65) have either".
- TYPE "fact" is fine for counts, but the paired centerpiece rows run against 0.5: general 1sts are slightly less often "shown in demo output" than lower placers. State the tension.

### 4. Stacking and sponsors

**4.1 WEAKEN (numeric error).**
- Verified: 10/65 (15%), 4/23 (17%), 2/6 (33%); pairs 18/16/13 of 148 (12%/11%/9%) (`Q09_general_1st_also_sponsor.csv`, `Q09_kind_pairs.csv`).
- Wrong: "HackUTD: 15 of 71 winners won 2+ awards". `Q09_n_awards_dist.csv` (scope hackutd) says 11 with 2 awards + 1 with 3 = 12 of 69 (17%). Also `Q19_hackutd2025_award_integration_counts.csv` has 41 awards over 36 projects (at most 5 projects with extras) and `Q19_hackutd2024_counts.txt` 7 of 33 multi-prize, so 15 cannot be reached from either table.
- HackUTD "general + sponsor" cases (Lumo, TalkTuahBank) overlap because the General winners also won the Goldman track: that is track structure, not a free stacking choice.
- Implication ("choose the sponsor track whose problem fits … then add one cheap API/MLH prize") is inference; label it so. The data show co-occurrence in multi-award projects only (rule 2b) and is a lower bound (`Q09_award_concentration.csv` note).

**4.2 WEAKEN.**
- Numbers ✓ (`Q10`: literalness=2 15/17 (88%) vs 18/27 (67%); removable 24/34 (71%) vs 36/55 (65%); features=0 18/34 (53%) vs 29/55 (53%); words-in-title 2: 10/24 (42%) vs 15/42 (36%)).
- The 21-point literalness gap rests on 17 vs 27 awards, and half of the awards have unknown literalness (unk 17 of 34; 29 of 56), with unknown most likely when the challenge text could not be found, so selection is possible. A 15/17 vs 18/27 gap is not significant (Fisher p≈0.15). Confidence should be low, not medium.
- The 2nd–3rd literalness=0/1 rows (1/27 and 8/27) show non-literal winners exist at 33% of lower placers. The implication "solve exactly the stated problem" is fair advice, but "builds what the challenge literally asked" should not be stated as a separator of 1st.

**4.3 WEAKEN (implication breaks spec rule 1).**
- Numbers ✓ (117/138 (85%) not removable; 77/141 (55%) one feature; 3+ features 27+5+3+1+1 = 37/141 (26%); 21/138 (15%) removable).
- It is nearly tautological: an API-depth prize is by definition awarded for using the API, so not-removable is built in.
- "One deep use beats many shallow ones" is a win-comparison claim with no comparator (1st vs lower is 3 vs 5–6, low n); rule 1 forbids claims of this form. Replace with "most (55%) API-depth winners used exactly one feature; 26% used 3+".

**4.4 HOLDS.**
- Counts match `Q13_sponsor_card_rows.csv` (Capital One 42, NVIDIA 21, CBRE 17, Photon 17, State Farm 13, Spacetime 12, T-Mobile 7, Goldman 6, NMC2 6, PNC 6, Toyota FS 6, EOG 4). Brief-only list (no rows for Axxess, AT&T, Winstead PC, 8090 AI, Niantic Spatial) ✓. They are award rows, not projects; say so.

### 5. Cover, demo, Devpost

**5.1 WEAKEN.**
- Numbers ✓ (general cover 1st higher/equal/lower 12/33/8; all 24/72/13; W/D/R 83/88/67; R cover 0 10/49 (20%) `Q15_cover_hackutd2025.csv`; low-cover 1sts exist `Q15_cover_examples_1sts.csv`).
- "Almost all 1sts pass" overstates: 3/3 is 43/53 (81%) of general 1sts and 94/111 (85%) of all 1sts (`Q01_paired_*`, cover_test_3of3); 15–19% of 1sts do not score 3/3.
- The R figure is written "0/3" which reads as "0 of 3"; write "score 0".
- "838 of 1,071" is true (counted from `data/tagged/cover_test.jsonl`: 3→838, 2→133, 1→58, 0→42) but is not in any `data/tables/` file (violates "every number from a table"), and `Q99_unknown_rates.csv` implies 1,148 − 80 = 1,068 scored. Reconcile 1,071 vs 1,068 (spec §0 data note and STATUS.md say 16 image-only rows are excluded).

**5.2 WEAKEN.**
- Numbers ✓ (`Q18_page_contents.csv`: video 47/56, >6 images 23/58, 0 images 5/58, challenges 50/56, what's-next 45/56, accomplishments 41/56, arch 13/59; HackUTD winners video 35/36 (97%)).
- Video does not separate at HackUTD 2025: demo_ready 50/50 (100%), random 48/50 (96%) in the same Q18 row. 97% is the floor for everyone.
- Direct inconsistency across tables: `Q19_hackutd2025_group_counts.csv` has_video W 18/36 (50%), D 50/50 (100%), R 47/50 (94%) (different definition), so a reader of Q19 would conclude winners have FEWER videos. Add a note on which definition is used.
- Implication "video + ≥4 images (including one architecture/flow image)": ≤3 images 20/58 (34%) of general 1sts (1–3: 15, 0: 5); architecture diagram 13/59 (22%), and HackUTD W 5/36 (14%) vs D 5/50 (10%). Nothing in the tables supports ≥4 images or an architecture image as a requirement. Also sponsor 1sts have 0 images in 12/46 (26%).

**5.3 WEAKEN.**
- Rule 3 breach: the SUPPORT is three hand-picked examples (REMI, Duet, FaceTimeOS from `Q16_wow_moments_1sts.csv`), with no n of N for "physical or cross-device vs chart". "Not a chart" has no denominator.
- Fix: classify every row in Q16 (n = 129 1sts) as physical/cross-device/software-only by manual read and report the share. As written the finding is inference (TYPE says so) and should be labelled low confidence.

**5.4 WEAKEN.**
- Numbers ✓ (`Q01_paired_general.csv` cited_stat 18/61 (30%) vs 16/117 (14%); `Q00` cost_evidence_beyond_assertion 3/36 (8%), 3/50 (6%), 3/50 (6%)).
- The three HackUTD cells are n=3 each (low n), so 8% vs 6% vs 6% must not be reported as a comparison. Remove or flag.
- "Rare" conflicts with data: beyond-assertion evidence is 19/61 (31%) of general 1sts and 40/129 (31%) of all 1sts. Say "a minority (31%)".
- The 16-point general gap is below the 20-point threshold and also leans on one tag value; keep as low confidence. "assert impact without evidence 69%" merges `none` (21/61, 34%) with `asserted` (21/61, 34%) (`Q01_paired_general.csv` cost_of_problem_stated); say "state no evidence".

### 6. HackUTD-specific

**6.1 WEAKEN.**
- 2025 ✓: 22 of 24 sponsor_domain awards problem_only, 2 sponsor_data (`Q19_hackutd2025_award_integration_counts.csv`). 2024 partly ✓: `Q19_hackutd2024_counts.txt` problem_only 11 of 19 (58%); core_data 4 + core_data* 3 = 7 of 19 (37%) used sponsor data as the core; unknown 1.
- "18 of 19 solved the sponsor's business problem" is not in any table or counts file.
- "No sponsor tool" ≠ `problem_only`/`core_data`; 2024 sponsors' data were central for 37% of company-track winners, so "problem not product" is too strong for 2024. Also `Q19_hackutd2025_group_counts.csv` any_sponsor_tool_core: winners 14/36 (39%) vs demo_ready 26/50 (52%): that supports 6.1 better (product use does not separate) and should replace the unverifiable count.
- Confidence "high" is only fair for 2025 (full read of every winner); 2024 is N=33 of 35 (2 excluded).

**6.2 WEAKEN.**
- Table ✓ (`Q19_hackutd2025_track_targeting.csv`: State Farm W 3, D 0, R 0; Goldman Sachs W 3, D 0, R 0; Toyota D 10 + R 6; T-Mobile D 8 + R 8; NVIDIA D 17 + R 9).
- The baseline is a sample of 100 (50 demo_ready picked for demo readiness, 50 random) from an unknown entry total. Zero in a sample of 100 does not mean "drew no entries". The correct statement: "none of 100 sampled non-winners targeted State Farm or Goldman Sachs".
- The implication ("prefer finance/insurance B2B problems that fewer teams will pick") is inference and ignores Capital One, a finance track that drew 3 of the 100 (R) with 1 winner (same table). Keep as low-confidence inference.

**6.3 DROP (as an actionable finding).**
- "with a new interaction" is not in any cited table (`Q19_hackutd2024_close_read_tags.csv` has no novelty column; `Q19_hackutd2024_counts.txt` has none).
- Confound: two of the three General winners (Lumo, TalkTuahBank) also won Goldman Sachs, and all Goldman winners (Lumo, TalkTuahBank, AllBank) have the unbanked focus (`Q19_hackutd2024_counts.txt`: "Goldman winners with unbanked focus: 3 of 3"). The theme may come from the Goldman prompt, not from the General track.
- n=3 low n, 2025 General winners differ (NLB, ProdigyPM, Working Memory per `Q19_hackutd2025_award_integration_counts.csv`), and the implication ("consistent with HackUTD General winners") conflicts with the finding's own counterexample. Keep as a one-line note in the close read.

**6.4 DROP (keep as anecdote in the close read only).**
- Single case; per the calibration file, "InsighT and Beacon placement unknown, treated as 'placed above HarmoniQ'" (`outputs/close_reads/calibration_tmobile_2025.md` lines 4–6). The finding's "higher T-Mobile winners" is an assumption, not data. 3rd place is the team's statement, not Devpost's.
- "−2 technical complexity, −1.5 completeness" are analyst ratings (n=3, labelled inference in the close read) but typed `fact (gap)` in findings.md, and they are not in the cited table (`Q21_tmobile2025_counts.csv` has feature counts only).
- Time-estimate violation in the source: `calibration_tmobile_2025.md:182` ("about 1–3 person-hours") and `:260` ("in the first hours"). findings.md avoids the number but states "the Auth0 prize cost little", which rests on that estimate. Remove the estimate from the close read and from this finding.
- Per standing instruction HarmoniQ is an ordinary data point; a one-project "calibration" with a directive implication gives it exactly the special weight to avoid.

### 7. Avoid list and table stakes

**7.1 WEAKEN (drop the "reject quickly" implication).**
- Numbers ✓ (`Q23_place_not_first.csv`: new_data 24/227 (11%) vs 6/129 (5%); education_feedback 23/227 (10%) vs 6/129 (5%); single_call 34/227 (15%) vs 13/129 (10%); data_to_decision 35/227 (15%) vs 15/129 (12%); general education 16/117 (14%) vs 2/61 (3%)).
- Gaps are 3–6 points, picked as the top of ~30 rows (multiple comparisons). Title wording "take 1st less often" is win-rate language (rule 1); say "are over-represented among 2nd/3rd/HM relative to 1st (association)".
- "A dashboard over a public dataset" is not a tagged field; data_to_decision is a pattern (12% of 1sts) and is 14/54 (26%) of sponsor 1sts. The implication should not tell a team to reject these; downgrade to a watch-list.
- The same table shows 1st-over-represented types (sensor 12% vs 6%, vision 16% vs 12%) which the finding omits; either list both or neither.

**7.2 WEAKEN.**
- Numbers ✓ (`Q20_recent_vs_older.csv`: agentic 187/715 (26%) vs 31/330 (9%); single_call 12% vs 19%; none 17% vs 26%; live 444/681 (65%) vs 169/301 (56%); hardware 24% vs 21%).
- "They no longer distinguish a project by themselves" is a winner-vs-non-winner statement; Q20 compares winners only (rule 2e) and cannot test it. And it conflicts with 0.2 (agentic W 47% vs D 28% in HackUTD 2025, which is a recent event).
- "Table stakes: live data and a real AI pipeline" overreaches: 35% of recent winners have no live data (237/681), and 17% (121/715) have no AI. Say "common (65%, 26%), not required".
- Recent vs older also differs in event mix; the weighted columns (27% vs 7% agentic) agree, which supports the direction.

---

## 2. Cross-finding contradictions to resolve

1. 0.2 (agentic helps at HackUTD 2025) vs 7.2 (agentic is table stakes).
2. 0.5 (visible centerpiece separates W from D) vs 3.2 (general 1sts show centerpiece less often than lower placers).
3. 0.7 (5–7 deps more common among winners, "more integrations fine") vs 3.1 (cap at ≤4).
4. 2.1 (no separator by the spec threshold) vs 4.2 (21-pt literalness gap) vs `Q01_paired_theme_other.csv` flagged rows.
5. 2.2 (technical/presentation edge) vs 2.1 (nothing separates).
6. 5.2 (HackUTD W video 97%, from Q18) vs `Q19_hackutd2025_group_counts.csv` has_video W 50%.
7. 0.6 (images are a floor, "no counterexample") vs `Q18_page_contents.csv` (sponsor 1sts with 0 images 12/46, 26%).
8. 6.1 ("problem, not product" high confidence) vs 2024 core_data 7 of 19 (37%).

## 3. Numeric and citation errors

| # | Where | Claimed | Table says |
|---|---|---|---|
| 1 | 4.1 | HackUTD "15 of 71 winners won 2+ awards" | `Q09_n_awards_dist.csv` hackutd: 11 (2 awards) + 1 (3 awards) = 12 of 69 (17%) |
| 2 | 3.2 | ai_role none 15/65 "mostly hardware/systems" | `Q04_general_1sts.csv`: 7 of the 15 have has_hardware=True (47%) |
| 3 | 0.6 | "Every 2025 winner page had images" | `Q18`: 0 images 0 of 34; 2 of 36 unknown |
| 4 | 0.6 | COUNTEREXAMPLES "none for images" | `Q18`: general 1sts 0 images 5/58 (9%); sponsor 1sts 12/46 (26%) |
| 5 | 0.5 | "non-winners more often only describe" | `Q00`: random described-only 13/50 (26%) < winners 10/36 (28%) |
| 6 | 6.1 | "18 of 19 solved the sponsor's business problem" | not in any table or counts file (problem_only 11 of 19) |
| 7 | 6.3 | "with a new interaction" | not in any `data/tables/` file |
| 8 | 6.4 | tech −2, completeness −1.5, cited to `Q21_tmobile2025_counts.csv` | table has feature counts only; ratings are from the close read (n=3, inference) |
| 9 | 5.1/§8 | "838 of 1,071" | true in `data/tagged/cover_test.jsonl`, not in a `data/tables/` file; `Q99_unknown_rates.csv` implies 1,068 scored |
| 10 | 2.1 | "largest general-track gaps" list omits larger | `Q01_paired_general.csv` page_has_accomplishments_section 72% vs 84% (12 pts) > 11 |
| 11 | 5.1 | "almost all 1sts pass" | cover_test_3of3 general 43/53 (81%), all 94/111 (85%) |

## 4. Missing findings the tables clearly support

1. **General vs sponsor 1sts (spec rule 2c)**, `Q07_novelty_general1_vs_sponsor1.csv`: data_to_decision 4/65 (6%) vs 14/54 (26%); execution_of_familiar_idea 6/65 (9%) vs 13/54 (24%); game_or_social 8/65 (12%) vs 1/54 (2%); docs_to_action 2/65 (3%) vs 6/54 (11%); new_interaction 15/65 (23%) vs 8/54 (15%). Only data_to_decision is cited, in a counterexample. These are the clearest General-vs-sponsor splits in the data.
2. **Devpost page differences by track kind**, `Q18_page_contents.csv`: 0 images sponsor 1sts 12/46 (26%) vs general 5/58 (9%); what's-next section 28/43 (65%) vs 45/56 (80%); video 30/43 (70%) vs 47/56 (84%).
3. **Sponsor product use does not separate at HackUTD 2025**, `Q19_hackutd2025_group_counts.csv`: any_sponsor_tool_core W 14/36 (39%), D 26/50 (52%), R 17/50 (34%).
4. **Novelty source at HackUTD 2025**, `Q00` novelty_source: execution_of_familiar_idea W 14/36 (39%), D 26/50 (52%), R 30/50 (60%) (gap −13 vs D, about 5 projects; medium–low).
5. **Breadth of working flows**, `Q19_hackutd2025_group_counts.csv`: shown_working_ge_3 W 12/36 (33%), D 8/50 (16%), R 7/50 (14%); depth-A-only W 12/29 (41%), D 8/30 (27%). This is the strongest independent support for 0.1 and is not cited.
6. **Theme/other tracks** (`Q01_paired_theme_other.csv`): design ≥4 10/17 (59%) vs 8/31 (26%), 15 pairs, plus n_user_flows=1 20/24 (83%) vs 21/34 (62%). Report with low-n/small-sample caveat, or explain why excluded (they contradict 2.1's headline).
7. **Concentration**, `Q09_n_awards_dist.csv`: 900 of 1,048 winners (86%) won exactly one award; HackUTD 57 of 69 (83%).

## 5. Lighter pass: archetypes.md and sponsor_cards.md

- `archetypes.md` counts match `Q04_archetype_counts.csv` / `Q04_archetype_assignment.csv` (A 22, B 16, C 11, D 9, E 4, unassigned 3 = 65). The archetype E cell is flagged low n ✓.
- Data bug: `Q04_archetype_assignment.csv` and `Q04_general_1sts.csv` have `event` = "2025" for Nomi, GDELT Open Intelligence Agent and AffectLink (truncated event names, 3 of 65 rows). Fix the upstream event label before these go in a table of examples.
- `archetypes.md` §D says "games win general tracks at other events more than sponsor tracks". That phrasing is win-rate language; use "game_or_social is 8/65 of general 1sts vs 1/54 of sponsor 1sts".
- `archetypes.md` "HackUTD fit" lines are labelled inference and say HackUTD 1sts are not in the table ✓.
- `sponsor_cards.md` states counts are "not a win rate" ✓ and flags LOW N ✓. The T-Mobile card line 39 (winners 3 of 36 (8%), baseline 8/50 each) matches `Q19_hackutd2025_track_targeting.csv` ✓. No duration estimates found by grep in findings.md, archetypes.md, sponsor_cards.md; the only ones in the project outputs are in `close_reads/calibration_tmobile_2025.md` (lines 182, 260), which must be edited.
- Grep for win-rate/lift/odds language in findings.md: only 4.3 ("beats") and 7.1 ("take 1st less often") breach rule 1 wording.

## 6. Not done

- Did not re-run `scripts/s6_tagged.py` from the raw jsonl; recomputed from the CSVs in `data/tables/` plus `Q04_general_1sts.csv`, `cover_test.jsonl`.
- Did not read the Devpost pages or the underlying records; ratings and tags were treated as given.
- Did not verify the 2024/2025 close-read narrative beyond what the Q19/Q21 tables and the counts txt contain.
- Significance figures (z, Fisher) are quick hand calculations for orientation only, not part of the project tables.
