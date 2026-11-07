# HackUTD 2026 — Winner-Dataset Analysis Spec (for AI agents)

Version: final, 2026-11-06. Audience: LLM agents analyzing the team's research folder: 1,152 deeply-read projects (911 winners, 141 sponsor-prize winners, 100 HackUTD 2025 non-winners), drawn from a master list of 2,475 prize rows across 59 hackathons. Read `00_START_HERE.md` first, then this whole file. Pipeline/roles: `02_PIPELINE.md`.

## 0. Mission and constraints

- Team: 4 students. Event: HackUTD 2026, 24-hour, in-person, UT Dallas, starts 2026-11-07. Tracks/challenges are announced only when hacking starts.
- Goal: 1st place general track AND 1st place in a sponsor track, plus any side prize obtainable with the same build.
- The analysis must end in DECISIONS usable the moment tracks are announced, not in interesting statistics.
- Prior-work rule: HackUTD has historically disqualified code written before hacking starts. Never recommend pre-writing submission code. Safe prep = docs reading, accounts, API keys, throwaway practice code that is not submitted.

### 0.1 Confirmed event facts (user-confirmed or from official HackUTD pages)

- Schedule (zeroday.hackutd.co): hacking starts Sat 2026-11-07 12:00 CT; initial Devpost submission required Sat ~23:00 CT; final submissions due Sun 2026-11-08 12:00 CT; judging Sun 13:00–16:00 CT (ECSW/ECSS); closing 17:00 CT.
- Tracks: every project is automatically in the General track. Each team may submit to up to 2 SPONSOR tracks and unlimited side tracks. In 2024 and 2025, [MLH]-prefixed tracks did not count toward the sponsor limit.
- Judging format: expo-style. Team sets up a station (laptop/monitor) in a lecture hall/room. Groups of judges come to the team, several groups over the session. Each visit ≈ 5 min demo/pitch + 2–3 min questions (2024 page said 3–5 min demos). Some judges are sponsor reps (sponsor tracks), others professors/hackathon veterans. Judging software historically "Jury".
- Submission video: demo-only, max 2 minutes (2024 and 2025 rules).
- Rubric: identical six criteria on the 2024 and 2025 HackUTD Devposts, no published weights: Innovation & Creativity, Technical Complexity, Completeness, Design, Impact, Presentation. Assume unchanged for 2026 unless the 2026 Devpost says otherwise.
- 2025 prize structure (for reference): General 3 places; most sponsor tracks 3 places (Capital One 1, EOG 2); side tracks Best Startup, Best Hardware, Best Design, Best Beginner, plus MLH/API prizes (e.g. Auth0, Gemini, ElevenLabs).
- IMPORTANT data caveat: HackUTD Devpost badges show WHICH track a project won but NOT its 1st/2nd/3rd placement (2024 and 2025), except Pinata 2024. So HackUTD rows support same-track peer comparison, not 1st-vs-2nd comparison. Placement-paired analysis (Q1, Q3, Q10, Q15, Q23) must use the other events where placement is published (see 2.0).

### 0.2 HackUTD 2026 sponsors (user-confirmed) → sponsor_industry mapping

| sponsor | sponsor_industry | note |
|---|---|---|
| T-Mobile | telecom | likely headline sponsor; team has prior T-Mobile 3rd |
| AT&T | telecom | sponsor research found no AT&T prize yet; may be a non-track sponsor |
| PNC Bank | finance_banking | |
| Goldman Sachs | finance_banking | |
| Capital One | finance_banking | |
| Toyota Financial Services | finance_banking (+ auto_mobility) | |
| State Farm | insurance | |
| CBRE | real_estate | |
| EOG Resources | energy | |
| NVIDIA | ai_compute | 2025 track was very crowded (reported 100+ entries; unverified) |
| NMC2 | ai_compute / cloud_devtools | assumed = NorthMark Compute & Cloud (2025 sponsor); verify |
| 8090 AI | ai_compute | verify what the challenge asks |
| Niantic Spatial | geospatial_ar | |
| Spacetime | cloud_devtools | likely SpacetimeDB (Clockwork Labs) — all 12 'Best Use of Spacetime' winners found used SpacetimeDB as core backend (`03_sponsor_tracks`); 2026 identity unconfirmed |
| Axxess | health | Dallas home-healthcare software |
| Winstead PC | legal | Dallas law firm |
| Photon | other | identity unclear; verify at opening |

Full per-sponsor briefs (tier, workshops, tools, past winners, [V]/[U] claims): `06_hackutd_2026_sponsors/`. Add `legal` to the sponsor_industry enum. For Q11/Q13, only build sponsor cards and matrix rows for these industries; other industries are context only.

### 0.3 What expo judging implies for the analysis

- Every project is judged by several judge groups, each for ~5 + 2–3 minutes, at the team's own station. So: (a) the pitch must be a repeatable ~4.5-minute script with the working result shown early; (b) the station itself (monitor, visible output, cover screen) is seen before the team speaks — Q15 matters more; (c) Q&A is ~35% of each visit — prepare answers, not just the demo.
- Live Q&A is not in the dataset. Use Q6 (technical centerpiece) and Q21 (calibration) to predict likely questions; see section 5.

## 1. Hard rules for every agent

1. The dataset is winners-only EXCEPT HackUTD 2025, which has a 100-project non-winner baseline (`02_baseline_non_winners/`: 50 `demo_ready`, 50 `random`). Winner-vs-non-winner comparisons are valid ONLY for HackUTD 2025; use `demo_ready` as the fair comparison and `random` as the typical entry, and never pool them. Everywhere else, do NOT compute or report "win rate", "lift", "saturation", or "X increases the chance of winning". Allowed: prevalence among winners, the HackUTD 2025 baseline comparison, and the comparisons in rule 2.
2. Valid comparisons: (a) 1st vs 2nd/3rd/HM within the SAME event and SAME track; (b) multi-award vs single-award projects; (c) general-track vs sponsor-track winners; (d) HackUTD vs other events; (e) recent (2025-06 onward) vs older; (f) repeat-winner teams vs others.
3. Always report counts with percentages: "4 of 7 (57%)". Flag any cell with n < 5 as "low n".
4. Every tagged value needs an evidence quote (≤ 25 words) from the page, or the value `unknown`. Never infer a feature is present because it is plausible. Absence on the page = `unknown`, not `no`, unless the field definition says otherwise.
5. Your 1–5 ratings are analyst judgments, not judge scores. Never correlate them with placement as if they were official scores; use them only for within-event rank comparisons and minimum/spread analysis.
6. Devpost videos are edited submissions, not the live judging pitch. Label any video-derived finding "video".
7. Separate fact from inference. Any claim about why judges chose something is `inference` unless a judge, organizer, or press quote says it.
8. If a pattern cannot be explained by visible evidence, write "not explained by available evidence". Do not invent reasons.

## 2. Phase 0 — Data setup (do first)

### 2.0 What already exists (start here, do not redo it)

Data collection is largely complete. Build on these files; do not re-collect them.

| Source | Records | Key contents |
|---|---|---|
| `04_deep_dives/data/deepdive_all.jsonl` | 1,152 (all three datasets) | what_it_is, problem_and_user, core_features (with working status), user_flow, prompt_text_found, prompt_summary, prompt_fit, sponsor_tool_use (with depth core/supporting/token), ai_approach, architecture, novelty_notes, scope_and_completeness, claims, presentation_assets, evidence depth A/B/C, confidence, placement_tier, prizes, sponsors, duplicate_of, second_pass_flag |
| `01_winners/data/project_records.jsonl` | 911 winners | first-pass schema (`01_winners/DATA_DICTIONARY.md`): one_line_pitch, problem_statement, target_user, domain_primary/secondary, idea_type, platforms, has_hardware, ai_used, ai_types, stack_*, tech_items (with depth), sponsor_apis_used, sponsor_fit_note, has_demo_video, has_live_demo, n_screenshots, ui_polish, commit counts before/in/after event window, readme_quality, writeup_sections, writeup_length, has_impact_claims, team_size, prizes with placement, event dates |
| `02_baseline_non_winners/data/project_records.jsonl` | 100 HackUTD 2025 non-winners | same schema + `sample_group` (`demo_ready` / `random`) |
| `03_sponsor_tracks/data/project_records.jsonl` | 141 sponsor-prize winners | same schema + `sponsors`; `Sponsor_prize_winners_analysis.xlsx` also has Winner_Index (178 rows) and Prompt_Library (114 prompts) |
| `ALL_PROJECTS_INDEX.csv` | 1,152 | one row per project: dataset, placement_tier, prizes, evidence_depth, confidence, duplicate_of, needs_second_pass, profile path, URLs |
| `04_deep_dives/profiles/<dataset>/<hackathon-edition>.md` | 1,152 | readable profile cards |
| `04_deep_dives/prompts_cache/`, `03_sponsor_tracks/sponsor_prompt_library.md` | | collected sponsor challenge text |
| `06_hackutd_2026_sponsors/*.md` | 17 | brief per 2026 sponsor, claims marked [V]erified/[U]nverified |
| `05_master_winner_lists/HackUTD_winners_master_v2.csv/.md` | 2,475 prize rows | source queue; ~1,340 mostly-unranked winners at 42 smaller events are NOT yet analyzed |

Join rules:
- Join on `project_id` where prefixes match; otherwise match on normalized name + edition (baseline IDs use `hackutd-hackutd-2025-`, winners use `hackutd-2025-`, sponsor set uses `sponsor-`).
- Respect `duplicate_of` (ProDuh, MayDay share one page): count once.
- Placement lives in `prizes[].placement` (1st/2nd/3rd/unknown) and `placement_tier` (`overall_top3`, `overall_other`, `track_winner`, `sponsor_winner`, `honorable_or_finalist`, `baseline_non_winner`). Most HackUTD placements are `unknown` (HarmoniQ's T-Mobile 3rd is from the team).
- Respect `evidence.depth` (A/B/C) and `confidence`; report findings with and without depth C / low-confidence records when they could change the result.
- Existing free text is the earlier agents' paraphrase. Treat it as evidence, not ground truth; where a field matters for a P1 question and the record is depth B/C, go back to the Devpost page.

Known limits already documented (read before analysis): root `README.md`, `01_winners/README.md`, `02_baseline_non_winners/README.md`, `03_sponsor_tracks/README.md`, `04_deep_dives/README.md`. Videos were not watched; live demos mostly not opened; `ui_polish` is mostly blank.

### 2.0.1 Mapping existing fields → this spec's fields
Derive from existing data first; tag with an LLM only what cannot be derived.

| spec field (§2.3/§2.4) | derive from existing | still needs tagging? |
|---|---|---|
| has_hardware, has_video, n_images, has_arch_diagram | `has_hardware`, `presentation_assets`, `n_screenshots` | no |
| ai_role | `ai_used`, `ai_types`, `ai_approach` | map to enum; tag only ambiguous cases |
| n_external_deps | count of `tech_items` / `sponsor_tool_use` | no (script) |
| sponsor_features_used, sponsor_removable | `sponsor_tool_use[].depth` (core = not removable), `sponsor_fit_note` | map; tag only `unclear` |
| prompt_literalness, prompt_words_in_title | `prompt_fit`, `prompt_summary`, `prompt_text_found` | yes (only where prompt text was found) |
| named_user | `target_user`, `problem_and_user` | yes (yes/no against the definition) |
| cost_of_problem_stated | `has_impact_claims`, `impact_claims_note`, `claims` | yes (enum) |
| pattern, novelty_source, problem_owner | `what_it_is`, `idea_type`, `novelty_notes`, `domain_*` | yes |
| technical_centerpiece, centerpiece_visible | `architecture`, `ai_approach`, `core_features` | yes |
| n_user_flows, mocked_parts_disclosed | `user_flow`, `core_features[].working_status`, `scope_and_completeness`, `claims`, `evidence.gaps` | yes |
| live_data | `architecture`, `core_features` | yes |
| wow_moment | `core_features`, `presentation_assets` | yes |
| tagline, cover test inputs | not stored verbatim | fetch title + tagline + first image from Devpost |
| rubric ratings (§2.4) | all of the above + profile card | yes (deep rating) |
| event_type, weight, recent | `hackathon`, `edition`, `event_start/end` | script + small manual map |
| prize_kind, sponsor_industry | `prizes`, `sponsors` | script + manual review of unmatched labels |

### 2.1 Row structure
- One row per PROJECT. Awards in a child list (one project may hold several awards). Never double-count a multi-award project in prevalence stats.

### 2.2 Event-context fields (all rows, mostly from page metadata)

| field | type | values / rule |
|---|---|---|
| project_id | str | stable id |
| event_name | str | |
| event_date | date | |
| event_type | enum | `hackutd`, `student_24h_inperson`, `student_36_48h`, `virtual`, `corporate_or_mlh_online`, `other` |
| weight | float | hackutd=3, student_24h_inperson=2, student_36_48h=1, others=0.5. Use weighted and unweighted views. |
| recent | bool | event_date ≥ 2025-06-01 |
| awards | list | each: {prize_name, placement: `1`/`2`/`3`/`HM`/`unranked`, prize_kind, sponsor, sponsor_industry} |
| prize_kind | enum | `general`, `sponsor_domain` (solve sponsor's business/problem prompt), `sponsor_api_depth` ("best use of X"), `sponsor_open`, `side_design`, `side_hardware`, `side_social_impact`, `side_beginner`, `mlh`, `peoples_choice`, `other` |
| sponsor_industry | enum | `telecom`, `finance_banking`, `insurance`, `real_estate`, `energy`, `auto_mobility`, `geospatial_ar`, `ai_compute`, `security_privacy`, `identity_auth`, `cloud_devtools`, `retail`, `health`, `legal`, `other`, `none` |
| n_awards | int | count of awards |
| team_size | int/unknown | |

### 2.3 Project-content fields (all rows; LLM-tagged from Devpost text)

| field | type | definition |
|---|---|---|
| tagline | str | verbatim Devpost tagline |
| one_sentence | str | your ≤ 20-word plain-English statement: user + what it does + outcome |
| pattern | enum | primary transformation: `docs_to_action`, `sensor_to_alert_or_action`, `vision_to_assist`, `voice_to_action`, `data_to_decision`, `risk_detect_and_respond`, `translate_between_people_or_systems`, `workflow_automation_agent`, `realtime_coordination`, `education_feedback`, `game_or_social`, `spatial_ar`, `devtool`, `other` |
| named_user | bool | a specific user type (e.g. "ER nurses", "first-gen applicants") appears in the first 2 sentences of description |
| cost_of_problem_stated | enum | `none`, `asserted`, `cited_stat`, `user_quote_or_interview`, `measured_by_team` |
| ai_role | enum | `none`, `single_call_wrapper`, `rag_or_chat`, `agentic_multistep`, `multimodal_pipeline`, `custom_or_finetuned_model`, `on_device` |
| has_hardware | yes/no/unknown | physical device used in demo per page |
| live_data | yes/no/unknown | ingests live external data/sensors/streams during demo |
| n_user_flows | int/unknown | distinct end-to-end user flows the page or video shows working |
| mocked_parts_disclosed | yes/no/unknown | page admits mocks, hardcoded data, or unfinished parts |
| n_external_deps | int | count of named external APIs/services/devices |
| sponsor_features_used | int/unknown | count of distinct features of the awarding sponsor's product used |
| sponsor_removable | yes/no/unknown | would the core demo still work if the sponsor's tech were removed? |
| prompt_literalness | 0/1/2 | sponsor-track only: 0 = loose reinterpretation, 1 = fits theme, 2 = directly answers stated prompt |
| prompt_words_in_title | 0/1/2 | 0 none, 1 domain words, 2 sponsor prompt wording mirrored |
| problem_owner | enum | sponsor-track only: `consumer`, `sponsor_internal_or_b2b`, `sponsor_customers` |
| novelty_source | enum | `new_user_group`, `new_interaction`, `new_data_or_context`, `technical_method`, `combination`, `execution_of_familiar_idea` |
| technical_centerpiece | str | ≤ 20 words: the hardest thing built beyond standard API calls; `none_visible` if none |
| centerpiece_visible | enum | `in_demo_output`, `shown_via_diagram_or_logs`, `described_only`, `none` |
| has_video | bool | |
| has_arch_diagram | bool | |
| n_images | int | screenshots/GIFs |
| wow_moment | str | ≤ 20 words; the most impressive visible result |
| evidence_tags | dict | per field: short quote |

### 2.4 Deep-rating fields

Deep-rate every project. If work is staged, these strata must be complete first because the key comparisons depend on them: all HackUTD winners; all multi-award projects; every event+track where a published 1st and a 2nd/3rd both exist (paired sets); all general/overall 1sts from `student_24h_inperson` events.

Rate 1–5 on the six HackUTD rubric dimensions (same on the 2024 and 2025 official Devposts; replace only if the 2026 Devpost differs):

| dimension | 1 | 3 | 5 |
|---|---|---|---|
| innovation | common idea, no twist | familiar idea, one real twist | approach judges likely haven't seen |
| technical_complexity | template/CRUD/one API call | meaningful integration or pipeline | hard engineering visibly solved |
| completeness | slides/mockups | core flow works with gaps | full core journey works end to end |
| design | default UI, confusing | clean, usable | polished, one obvious flow |
| impact | vague benefit | plausible benefit for named user | consequential, evidenced benefit |
| presentation | value unclear from page | understandable after reading | value obvious in 10 seconds |

Also on the subset:
- `cover_test_score` (0–3): give a SEPARATE blind agent only title + tagline + first image. It answers "what does it do / for whom / why it matters". Score 1 point per correct part vs the full page. Placement must be hidden from this agent.
- Video-only (if video exists): `secs_to_first_working_result`, `opens_with` = `problem` | `product` | `team` | `other`.

### 2.5 Tagger pilot (mandatory before tagging all rows)
- Tag 30 projects twice (two independent agent passes, or agent + teammate).
- Compute per-field agreement. Drop or redefine any field below 70% agreement.
- Report the dropped fields in the final output.

### 2.6 Non-winner baseline (exists for HackUTD 2025)
`02_baseline_non_winners/`: 100 HackUTD 2025 non-winners from a 325-project pool (50 `demo_ready` = most-engaged with repo + video; 50 `random`, seeded). Tag them exactly like winners. Compare HackUTD 2025 winners vs `demo_ready` (fair) and vs `random` (typical) separately; label differences as association, not cause. Extending the baseline to HackUTD 2024 is optional and would strengthen these comparisons.

## 3. Analysis questions (final list, prioritized)

Priority: P1 = core questions the final decisions depend on; P2 = supporting; P3 = exploratory. Answer all of them; priority sets order and emphasis. Each question: method → required output → decision it feeds.

### A. What earns 1st overall

**Q0 [P1] What separates HackUTD 2025 winners from strong non-winners?**
Method: HackUTD 2025 winners vs baseline `demo_ready`, then vs `random`, on every §2.3/§2.4 field and the existing first-pass fields (scope, AI use, sponsor tool depth, presentation assets, writeup, impact claims, commit share in window). Report counts per group.
Output: ranked list of differences with counts. Decision: the clearest evidence of what HackUTD judges reward over a complete-but-losing project.

**Q1 [P1] What differs between 1st and 2nd/3rd in the same event and track?**
Method: paired sets only (published placements; HackUTD rows mostly excluded, see 0.1). For every field in 2.3/2.4, compute the share in 1st vs 2nd/3rd; list fields with a gap ≥ 20 points AND ≥ 5 pairs. Read 10 pairs manually and write one sentence per pair on the visible difference.
Output: ranked differentiator list with counts and counterexamples. Decision: where to be exceptional, not merely competent.

**Q2 [P1] Which rubric dimensions are floors and which separate 1st?**
Method: per dimension, share of all subset winners scoring ≥ 4 (floor if ≥ 80%) and median 1st minus median 2nd/3rd in paired sets.
Output: table of floor vs differentiator dimensions. Decision: how to split 24 hours between build, design, and pitch.

**Q3 [P2] Do 1sts win by being balanced or by one spike?**
Method: compare the MINIMUM dimension score and the max–min spread for 1st vs 2nd/3rd.
Output: "balanced" / "spiky" / "no difference" with counts. Decision: guard every weak spot vs invest in one standout.

**Q4 [P1] What are the 3–5 recurring profiles of general 1st-place projects?**
Method: cluster general 1sts (weighted toward hackutd/student_24h) by pattern + ai_role + has_hardware + live_data + novelty_source. Describe each cluster with 3 example projects and 1 exception.
Output: archetype cards. Decision: the project shape to pursue.

**Q5 [P1] What is the minimum winning build?**
Method: distribution of n_user_flows, n_external_deps, completeness score, mocked_parts_disclosed among general 1sts vs 2nd/3rd.
Output: spec like "1st typically shows N flows, ≤ M dependencies, core journey complete". Decision: scope cap and feature-freeze criteria.

**Q6 [P1] Where is the technical centerpiece and how is it made visible?**
Method: ai_role distribution (recent vs older), technical_centerpiece text, centerpiece_visible; compare 1st vs 2nd/3rd.
Output: list of centerpiece types that appear in 1sts + how each was shown. Share of 1sts that are `single_call_wrapper`. Decision: where engineering hours go and how to show them.

**Q7 [P2] Where does novelty come from?**
Method: novelty_source distribution in general 1sts vs sponsor 1sts.
Output: ranked novelty mechanisms with examples. Decision: how to differentiate from look-alike AI projects.

**Q8 [P2] How specific is the problem framing?**
Method: named_user, cost_of_problem_stated, one_sentence clarity; 1st vs 2nd/3rd.
Output: counts. Decision: how narrowly to define the user and what proof to gather during the event.

### B. Sponsor tracks and prize stacking

**Q9 [P1] How do multi-award projects stack prizes?**
Method: distribution of n_awards; list every prize_kind pair among multi-award projects; "x of y general 1sts also won a sponsor prize"; top-10% share of all awards.
Output: pairing table. Decision: how to use the two track slots (e.g. one `sponsor_domain` + one `sponsor_api_depth`).

**Q10 [P1] What separates sponsor 1st from sponsor 2nd/3rd?**
Method: paired sponsor sets; compare sponsor centrality (sponsor_removable, sponsor_features_used), prompt_literalness, problem_owner, completeness.
Output: rule list such as "sponsor 1sts are non-removable in X of Y". Decision: integration depth and literal-vs-creative fit.

**Q11 [P1] Pattern × sponsor-industry lookup matrix (track-announcement tool).**
Method: crosstab of pattern by sponsor_industry for all sponsor-prize winners, with counts and 1–2 example project names per cell; mark cells where the same project also placed in general.
Output: matrix table. Decision: when tracks are announced, pick pre-researched frames immediately instead of brainstorming from scratch.

**Q12 [P2] What is the minimum viable integration for API-depth and side prizes?**
Method: for `sponsor_api_depth` and `side_*` winners: sponsor_features_used, whether shown live, estimated extra effort (`low`/`med`/`high` from writeup; label as estimate).
Output: list of side-prize types winnable with low extra effort. Decision: which add-on prizes to chase and which to skip.

**Q13 [P2] Sponsor playbook cards.**
Method: for each sponsor confirmed at HackUTD 2026 that also appears in the dataset: past winners' pattern, problem_owner, prompt_literalness, centrality.
Output: one card per sponsor. Decision: track choice and pitch angle per sponsor.

**Q14 [P2] Do sponsor 1sts mirror the prompt's language?**
Method: prompt_words_in_title, 1st vs 2nd/3rd.
Output: counts. Decision: whether to echo sponsor wording in Devpost and table pitch.

### C. Judging and presentation

**Q15 [P1] Can a stranger understand the project from the cover?**
Method: cover_test_score, 1st vs 2nd/3rd (paired sets).
Output: score gap with counts and 3 best/worst taglines. Decision: time spent on name, tagline, first image, first 10 seconds at the table.

**Q16 [P2, strong P1 candidate] When does the working result appear in the video, and what is the wow moment?** (HackUTD requires a ≤2-minute demo-only video, so winners' videos are a direct template.)
Method: secs_to_first_working_result, opens_with, wow_moment catalog (video-tagged subset only).
Output: median timing + catalog of wow moments by type. Decision: demo order and the central demo moment.

**Q17 [P2] How do winners make impact believable?**
Method: cost_of_problem_stated distribution; 1st vs 2nd/3rd.
Output: counts by evidence type. Decision: what evidence to produce during the 24 hours (e.g. a timed before/after test).

**Q18 [P2] What does a winning Devpost page contain?**
Method: has_video, has_arch_diagram, n_images, presence of challenges/what's-next sections; general 1sts vs sponsor 1sts.
Output: checklist with prevalence. Decision: Devpost template written at the event.

### D. Transfer to HackUTD and to this team

**Q19 [P1] What do HackUTD winners specifically share?**
Method: full manual read of every `hackutd` row (expected small n). Compare against `student_24h_inperson` patterns from Q1–Q11; list where HackUTD differs.
Output: HackUTD-specific findings with every project named. Decision: overrides general patterns when they conflict.

**Q20 [P2] What changed recently?**
Method: share per ai_role, has_hardware, live_data, pattern for recent vs older (counts).
Output: "now table stakes" vs "still distinctive" list. Decision: which features no longer differentiate.

**Q21 [P1] Calibration case: last year's HackUTD T-Mobile 3rd + Auth0 winner vs that year's T-Mobile 1st and 2nd.**
Data: HarmoniQ (https://devpost.com/software/x-yiqm81, record `hackutd-2025-*harmoniq*`) won T-Mobile 3rd + Best Use of Auth0 at HackUTD 2025 (placement per the team; not on Devpost). `06_hackutd_2026_sponsors/t-mobile.md` describes all three 2025 T-Mobile winners as sentiment dashboards. The other 2025 T-Mobile winners in the dataset are InsighT (https://devpost.com/software/t-insights) and Beacon (https://devpost.com/software/na-504rkg); their 1st/2nd order is not published — ask the team, otherwise treat both as 'placed above HarmoniQ'.
Method: tag all three with 2.3 + 2.4; write the gap per dimension; record how deep the Auth0 integration was.
Output: one-page gap analysis. Decision: what separated 3rd from 1st for a team like ours, and what a cheap API prize cost. (Note: this year's team is different; lessons are about the project, not the people.)

**Q22 [P3] What do repeat-winning teams do every time?**
Method: match member profile links across events in the dataset (undercounted). Compare their projects' fields.
Output: consistent behaviors. Decision: process habits.

**Q23 [P2] What project types place but rarely take 1st?**
Method: within winners: patterns/ai_roles common in 2nd/3rd/HM but rare in 1st (paired sets). Label as association.
Output: avoid list. Decision: ideas to reject quickly when choosing.

## 4. Questions deliberately CUT (out of scope)

| cut item | reason |
|---|---|
| Win rate / lift / saturation by domain or tech | invalid without non-winners (unless 2.6 sample exists) |
| Submissions per track, prize EV per track | not in a winners-only scrape; ask at event instead |
| Build time / hours-to-MVP inferred from commits | commit counts and in-window share exist for many repos (`01_winners`), but squashed/late pushes make build-time inference unreliable; use commit data only descriptively (e.g. prior-work norms), never as a winning factor |
| Live pitch time split, speaker handoffs, judge Q&A | live pitch not recorded; videos are not the pitch |
| Judge psychology / "unspoken criteria" | not observable; inference only |
| "Learning" criterion scoring | unobservable; rubric claim unverified |
| Team role mix, team size optimum | rarely stated; small effect on decisions |
| TAM / revenue model / logo-branding | likely noise at a student expo |
| UI library / stack frequency | describes popularity, not winning |
| Word-count ratios, problem-to-code ratio | cheap but no decision value |

## 5. Track-announcement decision procedure (run when tracks are announced)

1. Verify (see section 6). Paste official rubric, track list, and limits into context.
2. For each track: map to sponsor_industry and prize_kind; read its Q13 card and Q11 matrix row.
3. Generate 3–5 candidate (problem, primary track, secondary track/side prize) tuples using Q4 archetypes and Q11 cells.
4. Gates (fail any = fix or drop): eligible under rules; exact demo action + visible result can be stated in one sentence; a 4-person team can name a credible path to a working core flow within the event.
5. Score survivors 1–5, weighted: general-track strength 25, demo memorability 20, sponsor fit (non-removable, literal) 15, feasibility 15, problem/user value 10, distinctiveness 10, extra prize fit 5. Total = Σ(score×weight)/5. Treat as discussion tool. Do not let a high total hide a 1 or 2 in any row.
6. Commit to one candidate. Then: required initial Devpost entry; build; feature freeze well before the submission deadline; test, record the ≤2-min demo video, finish Devpost, rehearse the ~4.5-min station pitch and the most likely judge questions; submit.
7. Station prep: a cover screen that passes the Q15 cover test, seeded demo data, a one-click reset, and the backup video loaded locally.

## 6. Still to verify at opening ceremony

Resolved (see 0.1, 0.2): sponsor list, track limits, judging format, rubric (high confidence), schedule.

Still open:
- Whether a project can win General AND sponsor prizes at the same time (2025 allowed multi-award in practice; confirm).
- Whether MLH/side prizes are again outside the 2-sponsor limit.
- What NMC2, 8090 AI, Spacetime, and Photon challenges actually ask.
- Prior-work and boilerplate rules; whether the repo must be public.
- Number of judge groups per station and how finalists/winners are selected (starred projects? second round?).
- Exact per-visit timing at each room.

## 7. Required final outputs

Produce exactly these, each in the finding format below:
0. HackUTD 2025 winners vs non-winners comparison (Q0).
1. 3–5 general 1st-place archetype cards (Q4).
2. Ranked 1st-vs-2nd differentiators + floor/differentiator rubric table (Q1, Q2, Q3).
3. Minimum winning build spec (Q5, Q6).
4. Prize-stacking playbook + pattern × sponsor matrix + sponsor cards (Q9–Q14).
5. Cover/demo/Devpost template (Q15–Q18).
6. HackUTD-specific overrides + calibration-case gaps (Q19, Q21).
7. Avoid list (Q23) + "table stakes now" list (Q20).
8. Data-quality note: fields dropped in pilot, low-n cells, unknown rates.

Finding format (mandatory):
```
FINDING: <one sentence>
SUPPORT: <n of N, weighted/unweighted>, examples: <project names + links>
COUNTEREXAMPLES: <names or "none found">
CONFIDENCE: high | medium | low  (+ why)
TYPE: fact | association | inference
IMPLICATION FOR US: <one concrete action or rule>
```

## 8. Recommended execution order (dependency order, not a scope cut)

Join + derive (2.0, 2.0.1) → pilot (2.5) → tag remaining fields (2.3) → deep rating (2.4) + cover test → Q19 and Q21 (close reads) → Q0 → Q1–Q3 → Q9–Q11 → Q4–Q8 → Q12–Q18 → Q20, Q22, Q23 → section 7 outputs → independent red-team review of every finding.
