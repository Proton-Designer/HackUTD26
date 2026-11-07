# HackUTD 2026 — Findings (S7 synthesis, v2 after S8 red team)

Spec: `01_ANALYSIS_SPEC.md` §7. Every number comes from a table in `data/tables/` (named in each SUPPORT line; index `data/tables/INDEX.md`), produced by `scripts/s6_tagged.py`, `scripts/s6_q09_stacking.py`, `scripts/q04_archetype_counts.py`, `scripts/s7_sponsor_cards.py` and the S5 close reads. Red-team review: `outputs/redteam_review.md` (findings) and `outputs/redteam_kit_review.md` (kit, archetypes); the change log is at the end.

How to read this:
- Ratings (1–5) are **analyst judgments** by blind Sonnet taggers, not judge scores (spec rule 5). Cover scores (0–3) come from a separate blind cover test.
- Winner-vs-non-winner comparisons exist **only for HackUTD 2025** (36 tagged winners vs 50 `demo_ready` and 50 `random` non-winners, a sample of 100 non-winners; never pooled). Elsewhere: 1st vs 2nd/3rd in the same event and track ("paired": 127 tracks, 129 1sts vs 224 2nd/3rd), general vs sponsor 1sts, or prevalence among winners.
- "all" = every tagged row; "excl_weak" drops thin records. Findings are stated only where both views agree in direction.
- n < 5 = **low n**. Noise yardstick: a gap of fewer than about 3 projects, or a track sign count like 54 vs 36, is not distinguishable from chance.
- TYPE: fact (directly counted) / association (a difference between groups, not proof of cause) / inference (our reading of why).
- Companion files: `outputs/archetypes.md` (Q4), `outputs/sponsor_cards.md` (Q13), `outputs/close_reads/*` (Q19, Q21), `outputs/TRACK_DAY_KIT.md` (decisions).

---

## 0. HackUTD 2025 winners vs non-winners (Q0)

Source: `Q00_hackutd2025_vs_baseline_all.csv`, `..._excl_weak.csv`, `Q00_hackutd2025_ordinal_all.csv`, `Q19_hackutd2025_group_counts.csv`; per-project notes in `outputs/close_reads/hackutd_2025_winners.md`. W = winners (all tracks), D = `demo_ready`, R = `random`.

FINDING 0.1: Winners more often show working features, and more of them; one working flow alone does not separate winners from strong non-winners.
SUPPORT: exactly 2 flows shown working: W 8 of 35 (23%), D 0 of 47 (0%), R 1 of 42 (2%); 1 flow: W 25 of 35 (71%), D 36 of 47 (77%); 0 flows: W 1 of 35 (3%), D 9 of 47 (19%), R 11 of 42 (26%) (excl_weak: 2 flows 24% / 0% / 3%). Independent close read: ≥1 feature shown working W 27 of 36 (75%), D 21 of 50 (42%), R 17 of 50 (34%); ≥3 shown working W 12 of 36 (33%), D 8 of 50 (16%), R 7 of 50 (14%) (`Q19_hackutd2025_group_counts.csv`).
COUNTEREXAMPLES: 25 of 35 winners showed exactly one flow.
CONFIDENCE: medium — two independent measures agree; small n; flows are counted from page text (a documentation measure), and the field had 5–6 of 10 spot-check agreement.
TYPE: association
IMPLICATION FOR US: Get one core flow fully working first; add a second working flow on top; never present an unbuilt feature.

FINDING 0.2: Winners more often use a multi-step agent design; projects with no AI or only RAG/chat are more common among non-winners.
SUPPORT: agentic_multistep W 17 of 36 (47%), D 14 of 50 (28%), R 8 of 50 (16%); excl_weak 49% / 28% / 18%. Single-call wrapper or no AI (combined): W 13 of 36 (36%), D 22 of 50 (44%), R 28 of 50 (56%). Single-call wrapper alone shows no gap (W 6 of 36, 17%; D 10 of 50, 20%).
COUNTEREXAMPLES: 15 of 65 general 1sts across all events (23%) use no AI (`Q04_general_1sts_ai_role.csv`).
CONFIDENCE: medium (about 7 projects difference vs D)
TYPE: association
IMPLICATION FOR US: If the idea uses AI, make it do visible multi-step work (tool calls, actions, chained steps).

FINDING 0.3: Data-in/dashboard-out is the most common shape among strong non-winners and about half as common among winners; it is also rare among general 1sts at other events, though common among sponsor 1sts.
SUPPORT: pattern data_to_decision W 8 of 36 (22%), D 24 of 50 (48%), R 20 of 50 (40%); excl_weak 23% / 50% / 46%. General 1sts 4 of 65 (6%) vs sponsor 1sts 14 of 54 (26%) (`Q07_novelty_general1_vs_sponsor1.csv`).
COUNTEREXAMPLES: the 2025 T-Mobile winners were sentiment dashboards (close read).
CONFIDENCE: medium
TYPE: association
IMPLICATION FOR US: For a General-track contender, do not make a plain dashboard the core; if a sponsor track asks for insight, add an action or interaction on top.

FINDING 0.4: Winners are more often rated ≥4 on completeness and presentation (small counts); innovation and impact show no winner advantage.
SUPPORT: rated ≥4: completeness W 8 of 36 (22%) vs D 3 of 50 (6%); presentation W 11 of 36 (31%) vs D 7 of 50 (14%); technical complexity 12 of 36 (33%) vs 14 of 50 (28%); innovation 1 of 36 (3%, low n) vs 3 of 50 (6%, low n). Medians are equal (3 vs 3) for completeness and presentation; impact 2.5 vs 3 (`Q00_hackutd2025_ordinal_all.csv`). Same direction in excl_weak.
COUNTEREXAMPLES: 28 of 36 winners are not rated ≥4 on completeness.
CONFIDENCE: low–medium (gaps of 4–5 projects; presentation had the weakest spot-check agreement)
TYPE: association
IMPLICATION FOR US: Inference: finishing the core flow and presenting it clearly is a better use of effort than adding ideas.

FINDING 0.5: Winners more often make the technical centerpiece visible than strong non-winners; this does not carry over to 1st vs 2nd/3rd at other events.
SUPPORT: visible (diagram/logs or demo output): W 18 of 36 (50%), D 14 of 50 (28%), R 4 of 50 (8%); described only: W 10 of 36 (28%), D 21 of 50 (42%), R 13 of 50 (26%). Within paired general tracks: shown in demo output 30 of 61 (49%) 1sts vs 67 of 117 (57%) 2nd/3rd (`Q01_paired_general.csv`).
COUNTEREXAMPLES: 10 winners only described the centerpiece; the within-track comparison runs the other way.
CONFIDENCE: low–medium
TYPE: association
IMPLICATION FOR US: Show the hard part on screen (logs, agent trace, architecture view next to the demo) — it helps reach the winner group at HackUTD; it is not evidence for beating the other top projects.

FINDING 0.6: No 2025 winner page with a known image count had zero images, while 40% of typical entries did; a clear cover does not separate winners from strong non-winners.
SUPPORT: 0 images W 0 of 34 (2 unknown), D 9 of 50 (18%), R 20 of 50 (40%) (excl_weak R 10 of 39, 26%). Cover 3/3: W 30 of 36 (83%), D 43 of 49 (88%), R 33 of 49 (67%) (`Q15_cover_hackutd2025.csv`). Across all events, 0 images: general 1sts 5 of 58 (9%), sponsor 1sts 12 of 46 (26%) (`Q18_page_contents.csv`).
COUNTEREXAMPLES: those 1sts with no images.
CONFIDENCE: medium (cover scores have a ceiling: 835 of 1,068 scored 3/3, `Q15_cover_distribution_all.csv`)
TYPE: association
IMPLICATION FOR US: Images and a clear cover separate us from weak entries, not from strong ones. Do them well, then move on.

FINDING 0.7: Hardware is more common among winners (low n on the non-winner side).
SUPPORT: has_hardware W 5 of 35 (14%), D 1 of 49 (2%, low n), R 3 of 44 (7%, low n).
COUNTEREXAMPLES: 30 of 35 winners had no hardware.
CONFIDENCE: low
TYPE: association
IMPLICATION FOR US: Hardware is an option, not a requirement. (The external-dependency gap, W 22% vs D 6% with 5–7 listed services, is not used: the count tracks how fully a page lists its stack, and winners write longer pages.)

FINDING 0.8: Using a sponsor's product does not separate HackUTD 2025 winners from strong non-winners.
SUPPORT: any sponsor tool core to the build: W 14 of 36 (39%), D 26 of 50 (52%), R 17 of 50 (34%) (`Q19_hackutd2025_group_counts.csv`). 22 of 24 company-problem awards went to projects using no sponsor product (`Q19_hackutd2025_award_integration_counts.csv`).
COUNTEREXAMPLES: API-depth prizes (NVIDIA, Solana) required real tool use.
CONFIDENCE: medium
TYPE: association
IMPLICATION FOR US: For problem-style tracks, spend effort on the problem, not on forcing sponsor tech in.

FINDING 0.9: "Execution of a familiar idea" is less common among winners.
SUPPORT: novelty_source execution_of_familiar_idea W 14 of 36 (39%), D 26 of 50 (52%), R 30 of 50 (60%).
COUNTEREXAMPLES: 14 winners.
CONFIDENCE: low–medium (about 5 projects vs D)
TYPE: association
IMPLICATION FOR US: Prefer a combination or a new interaction over a cleaner version of a common idea.

Smaller gaps (named user 86% / 76% / 64%; live data 61% / 53% / 42%) are in the tables.

---

## 1. General 1st-place archetypes and general vs sponsor 1sts (Q4, Q7)

Full cards: `outputs/archetypes.md` (assignment `Q04_archetype_assignment.csv`, counts `Q04_archetype_counts.csv`). HackUTD does not publish placement, so the 65 general 1sts are from other events.

FINDING 1.1: The most common general-1st patterns are sensor-to-action, vision-to-assist and game/social; dashboards and chat are rare.
SUPPORT: sensor_to_alert_or_action 10 of 65 (15%), vision_to_assist 10 of 65 (15%), game_or_social 8 of 65 (12%); data_to_decision 4 of 65 (6%); rag_or_chat 1 of 65 (2%, low n). ai_role multimodal 21 of 65 (32%), none 15 (23%), agentic 10 (15%), custom/fine-tuned 7 (11%), single-call 6 (9%). Hardware 23 of 65 (35%); live data 40 of 65 (62%); novelty combination 25 (38%), new interaction 15 (23%) (`Q04_general_1sts_*.csv`). Archetypes: A hardware sense-and-act 22, B multimodal human-need pipeline 16, C agent/dev-tool automation 11, D playful new interaction 9, E data-to-decision utility 4 (low n), unassigned 3. Examples: Duet (Cal Hacks 11.0), Pyrosense (Hack the Valley 11), SeeForMe (McHacks 12), Scrub+ (HackNC 2026).
COUNTEREXAMPLES: 14 patterns appear; the top three cover 28 of 65 (43%).
CONFIDENCE: medium (prevalence among winners only)
TYPE: fact
IMPLICATION FOR US: Seed candidates from archetypes B and C first; A (hardware) only with a hardware loop the team can already make work — 15 of 22 A examples come from 36–48h events and 0 of 6 HackUTD general winners were hardware (archetypes.md).

FINDING 1.2: General 1sts and sponsor 1sts differ in shape: general 1sts are more often games/new interactions, sponsor 1sts more often dashboards, document tools and familiar ideas well executed.
SUPPORT: general 1sts vs sponsor 1sts: game_or_social 8 of 65 (12%) vs 1 of 54 (2%, low n); new_interaction 15 of 65 (23%) vs 8 of 54 (15%); data_to_decision 4 of 65 (6%) vs 14 of 54 (26%); docs_to_action 2 of 65 (3%, low n) vs 6 of 54 (11%); execution_of_familiar_idea 6 of 65 (9%) vs 13 of 54 (24%) (`Q07_novelty_general1_vs_sponsor1.csv`).
COUNTEREXAMPLES: combination novelty is equal (38% vs 37%).
CONFIDENCE: medium
TYPE: association (spec rule 2c)
IMPLICATION FOR US: A General + sponsor double needs a sponsor-fit problem delivered with a general-style interaction (new interaction or combination), not a sponsor-style dashboard.

---

## 2. 1st vs 2nd/3rd differentiators and rubric floors (Q1, Q2, Q3)

Source: `Q01_paired_all_tracks.csv`, `Q01_paired_general.csv`, `Q01_paired_sponsor.csv`, `Q01_paired_theme_other.csv`, `Q02_floor_vs_differentiator.csv`, `Q10_sponsor_fit_by_placement.csv`.

FINDING 2.1: In the all-track, general and sponsor paired tables, no tagged field reaches the spec's bar (gap ≥ 20 points with ≥ 5 pairs). Two smaller sets do: theme tracks and sponsor prompt literalness.
SUPPORT: largest all-track gap: impact backed by a cited statistic 29 of 129 (22%) vs 28 of 224 (12%). Largest general-track gaps: cited statistic 18 of 61 (30%) vs 16 of 117 (14%); accomplishments section 39 of 54 (72%) vs 87 of 105 (83%); sensor_to_alert 10 of 61 (16%) vs 6 of 117 (5%); education_feedback 2 of 61 (3%, low n) vs 16 of 117 (14%). Exceptions meeting the bar: theme/other tracks design ≥4 10 of 17 (59%) vs 8 of 31 (26%) over 15 pairs, and exactly 1 flow 20 of 24 (83%) vs 21 of 34 (62%) over 24 pairs (`Q01_paired_theme_other.csv`); sponsor-domain prompt literalness = 2, 14 of 16 (88%) vs 18 of 27 (67%) paired (`Q10`, see 4.2).
COUNTEREXAMPLES: n/a
CONFIDENCE: medium. Tagger agreement on these fields was 67–84%, which shrinks real differences: "not detected" is not "no difference".
TYPE: fact
IMPLICATION FOR US: The visible features that get a project into the top 3 do not explain who takes 1st; that is not explained by available evidence. Inference: the live demo and Q&A may matter, so rehearse both.

FINDING 2.2: No rubric dimension is a floor among winners, and no dimension separates 1st from 2nd/3rd.
SUPPORT: share of winners rated ≥4: technical complexity 580 of 1,048 (55%), presentation 445 of 1,048 (42%), innovation 407 of 1,048 (39%), completeness 304 of 1,048 (29%), design 242 of 881 (27%), impact 101 of 1,048 (10%) — none reach 80%. Paired median gap 0.0 on all six. Track signs (1st rated higher / equal / lower): technical complexity 54 / 37 / 36, presentation 52 / 37 / 38 (within noise), innovation 36 / 56 / 35, impact 38 / 45 / 44.
COUNTEREXAMPLES: n/a
CONFIDENCE: medium (analyst ratings; within-track only)
TYPE: fact
IMPLICATION FOR US: Treat every rubric dimension as a gate to pass; no single dimension is shown to win 1st.

FINDING 2.3: 1sts are not spikier than 2nd/3rd; their whole rating profile is at most slightly higher.
SUPPORT: rating minimum, tracks 1st higher / equal / lower: 47 / 46 / 34 (general 21 / 24 / 15); rating spread 42 / 42 / 43.
COUNTEREXAMPLES: 34 tracks where the 1st had the lower minimum.
CONFIDENCE: low
TYPE: association
IMPLICATION FOR US: Do not bet on one standout dimension while leaving another weak.

---

## 3. Minimum winning build (Q5, Q6)

Source: `Q01_paired_general.csv`, `Q04_general_1sts_ai_role.csv`, `Q04_general_1sts.csv`, `Q06_general_1st_centerpieces.csv`.

FINDING 3.1: The typical general 1st shows one working user flow and lists 0–4 external services.
SUPPORT: general 1sts: 1 flow 42 of 58 (72%), 2 flows 10 of 58 (17%), 0 flows 5 of 58 (9%) vs 2nd/3rd 71% / 10% / 14%; external services 0–2 23 of 61 (38%), 3–4 27 of 61 (44%), 5–7 9 of 61 (15%), >7 2 of 61 (3%, low n). At HackUTD 2025, more working features is what separated winners (Finding 0.1).
COUNTEREXAMPLES: 5 general 1sts with 0 flows shown on the page.
CONFIDENCE: medium (page-text measure)
TYPE: fact
IMPLICATION FOR US: Scope = one end-to-end flow, then a second if the first is stable; keep external services to ones that will each work at the table; say plainly what is simulated (judgment — mocked_parts_disclosed is unknown for 46% of rows and cannot be compared).

FINDING 3.2: 58% of general 1sts have a multimodal pipeline or hardware at their core; single-call wrappers are 9%.
SUPPORT: multimodal pipeline or hardware 38 of 65 (58%); ai_role multimodal 21 (32%), none 15 (23%; 7 of these 15 have hardware), agentic 10 (15%), custom/fine-tuned 7 (11%), single_call_wrapper 6 (9%), on-device 5 (8%). Paired general: single-call 5 of 61 (8%) 1sts vs 16 of 117 (14%) 2nd/3rd (small gap). Centerpiece texts: `Q06_general_1st_centerpieces.csv`.
COUNTEREXAMPLES: 6 single-call 1sts.
CONFIDENCE: medium
TYPE: fact
IMPLICATION FOR US: Put engineering into one non-trivial pipeline (multi-input, multi-step or hardware) that the demo exercises.

---

## 4. Prize stacking, sponsor tracks, matrix and cards (Q9–Q14)

Source: `Q09_*.csv`, `Q10_sponsor_fit_by_placement.csv`, `Q11_pattern_x_industry.csv`, `Q13_sponsor_card_rows.csv`, `Q13_sponsor_card_stats.csv`; cards in `outputs/sponsor_cards.md`.

FINDING 4.1: Most winners win one award; winning General plus a sponsor prize happens in a minority of cases.
SUPPORT: one award: 900 of 1,048 winners (86%); HackUTD 57 of 69 (83%), so 12 of 69 (17%) won 2+ (`Q09_n_awards_dist.csv`). General 1sts also winning a sponsor prize: 10 of 65 (15%); student 24h in-person 4 of 23 (17%); HackUTD general winners (any place) 2 of 6 (33%, low n — Lumo and TalkTuahBank also won the Goldman Sachs track) (`Q09_general_1st_also_sponsor.csv`). Most common pairs among 148 multi-award projects: general + sponsor API-depth 18 (12%), general + open sponsor prize 16 (11%), general + sponsor-domain 13 (9%) (`Q09_kind_pairs.csv`).
COUNTEREXAMPLES: 55 of 65 general 1sts won no sponsor prize.
CONFIDENCE: medium (dataset sampled winners per track: stacking is a lower bound)
TYPE: fact
IMPLICATION FOR US: Inference: pick the sponsor track whose problem fits the General idea, then add one MLH/side prize the build already uses.

FINDING 4.2: Sponsor-domain 1sts more often build what the challenge literally asked for; how much sponsor tech they use does not differ.
SUPPORT: prompt_literalness = 2: 1sts 15 of 17 (88%) vs 2nd/3rd 18 of 27 (67%) — literalness unknown for 17 of 34 1sts and 29 of 56 lower placers. Sponsor tech removable 24 of 34 (71%) vs 36 of 55 (65%); zero sponsor features 18 of 34 (53%) vs 29 of 55 (53%); prompt words in title (2 words) 10 of 24 (42%) vs 15 of 42 (36%) (`Q10_sponsor_fit_by_placement.csv`).
COUNTEREXAMPLES: 2 of 17 sponsor-domain 1sts were loose interpretations; 9 of 27 lower placers were too.
CONFIDENCE: low (small counts, half unknown; not significant)
TYPE: association
IMPLICATION FOR US: For problem-style tracks, solve exactly the stated problem for the stated user; sponsor tech is optional.

FINDING 4.3: Almost all API-depth prize winners made the sponsor's tool non-removable; most used exactly one feature.
SUPPORT: sponsor_api_depth winners (any place): tool not removable 117 of 138 (85%); exactly 1 feature 77 of 141 (55%), 3+ features 37 of 141 (26%). 1st vs 2nd/3rd: low n (3 vs 5–6) (`Q10`).
COUNTEREXAMPLES: 21 of 138 (15%) API-depth winners where the tool was removable.
CONFIDENCE: medium for the any-place share (partly by definition of the prize); no evidence on which depth places higher
TYPE: fact
IMPLICATION FOR US: For a tool prize, make at least one feature of the tool load-bearing in the core flow and show it working.

FINDING 4.4: The pattern × industry matrix and sponsor cards are lookup tools for track announcement.
SUPPORT: `Q11_pattern_x_industry.csv`; `Q13_sponsor_card_rows.csv` award rows per 2026 sponsor: Capital One 42, NVIDIA 21, CBRE 17, Photon 17, State Farm 13, Spacetime 12, T-Mobile 7, Goldman Sachs 6, NMC2 6, PNC 6, Toyota FS 6, EOG 4 (award rows, not projects); `outputs/sponsor_cards.md`.
COUNTEREXAMPLES: Axxess, AT&T, Winstead PC, 8090 AI, Niantic Spatial have no dataset winners (brief-only cards).
CONFIDENCE: n/a (reference)
TYPE: fact
IMPLICATION FOR US: At announcement, read each candidate track's card before brainstorming (TRACK_DAY_KIT §2).

---

## 5. Cover, demo and Devpost template (Q15–Q18)

Source: `Q15_cover_hackutd2025.csv`, `Q15_cover_examples_1sts.csv`, `Q15_cover_distribution_all.csv`, `Q16_wow_moments_1sts.csv`, `Q18_page_contents.csv`, `Q01_paired_*`.

FINDING 5.1: Most 1sts pass the cover test, but so do their lower-placed peers; 15–19% of 1sts do not score 3/3.
SUPPORT: cover 3/3: general 1sts 43 of 53 (81%), all 1sts 94 of 111 (85%); paired general tracks, 1st higher / equal / lower: 12 / 33 / 8; all tracks 24 / 72 / 13. HackUTD 2025 random entries scoring 0: 10 of 49 (20%) vs winners 0 of 36. Whole dataset: 835 of 1,068 (78%) scored 3/3. Low-scoring 1sts: "Kitkat — Redefining mobile computing." (1), "Identity Matrix — ." (0); high: "FaceTimeOS: AI Mac Agent — FaceTime to talk, see, and control your Macbook with AI Agents" (3) (`Q15_cover_examples_1sts.csv`).
COUNTEREXAMPLES: those low-cover 1sts.
CONFIDENCE: medium (ceiling effect)
TYPE: association
IMPLICATION FOR US: Name + tagline say who it is for and what it does in one line; test on a stranger; then move on.

FINDING 5.2: Typical general-1st Devpost pages have a video and the standard sections; they are typical, not universal, and architecture diagrams are uncommon.
SUPPORT: general 1sts: video 47 of 56 (84%), challenges section 50 of 56 (89%), what's-next 45 of 56 (80%), accomplishments 41 of 56 (73%), 4+ images 38 of 58 (66%), 0 images 5 of 58 (9%), architecture diagram 13 of 59 (22%). Sponsor 1sts: video 30 of 43 (70%), what's-next 28 of 43 (65%), 0 images 12 of 46 (26%). HackUTD 2025: video embedded W 35 of 36 (97%), D 50 of 50, R 48 of 50 — video does not separate (`Q18_page_contents.csv`; page-embed definition, which differs from the first-pass has_video in `Q19_hackutd2025_group_counts.csv`).
COUNTEREXAMPLES: 9 general 1sts without a video embed.
CONFIDENCE: high (fact)
TYPE: fact
IMPLICATION FOR US: Devpost template = embedded video + several images (product working first) + all standard sections; an architecture image is optional (judgment).

FINDING 5.3: Wow moments in general-1st write-ups are often a physical or cross-device action happening live.
SUPPORT: examples from `Q16_wow_moments_1sts.csv` (page text; videos not watched; not classified across all rows): "Phone unlocks the 3D-printed bike lock over NFC" (REMI); "Brain waves change tempo and intensity of live generated music" (Duet); "Calling the Mac over FaceTime, the agent answers by voice, runs the task and texts back a screenshot" (FaceTimeOS).
COUNTEREXAMPLES: software-only wow moments in the same catalog.
CONFIDENCE: low (hand-picked examples, no denominator)
TYPE: inference
IMPLICATION FOR US: Design one moment where the judge sees the system act on the real world or on their own input.

FINDING 5.4: A minority of 1sts back impact with evidence; a cited statistic is the most common form.
SUPPORT: evidence beyond assertion: 40 of 129 (31%) of all paired 1sts, 19 of 61 (31%) of general 1sts. Cited statistic: general 1sts 18 of 61 (30%) vs 2nd/3rd 16 of 117 (14%) (below the 20-point bar). No evidence stated 21 of 61 (34%), asserted only 21 of 61 (34%) (`Q01_paired_general.csv`).
COUNTEREXAMPLES: 42 of 61 general 1sts give no evidence beyond assertion.
CONFIDENCE: low–medium
TYPE: association
IMPLICATION FOR US: Put one cited number about the problem into the pitch and page; a measured before/after during the event would be unusual.

---

## 6. HackUTD-specific overrides (Q19; Q21 is in the close read)

Full detail: `outputs/close_reads/hackutd_2025_winners.md`, `hackutd_2024_winners.md`, `calibration_tmobile_2025.md`; tables `Q19_*`, `Q21_tmobile2025_counts.csv`.

FINDING 6.1: At HackUTD 2025, company-problem awards went to projects that solved the sponsor's business problem without its product; in 2024, sponsor data was central for about a third of company-track winners.
SUPPORT: 2025: 22 of 24 company-problem awards problem-only, 2 used sponsor data (`Q19_hackutd2025_award_integration_counts.csv`); sponsor tool core W 14 of 36 (39%) vs D 26 of 50 (52%) (Finding 0.8). 2024: problem-only 11 of 19 (58%); sponsor data as the core 7 of 19 (37%); unknown 1 (`Q19_hackutd2024_counts.txt`).
COUNTEREXAMPLES: API-depth tracks (NVIDIA, Solana 2025) required real tool use; 2024 data-core winners.
CONFIDENCE: high for 2025 (every winner read); medium for 2024
TYPE: fact
IMPLICATION FOR US: For problem-style tracks at HackUTD, the problem comes first; use a sponsor's data or API when the challenge provides it.

FINDING 6.2: Of 100 sampled HackUTD 2025 non-winners, none targeted State Farm or Goldman Sachs, each of which awarded 3 prizes.
SUPPORT: `Q19_hackutd2025_track_targeting.csv`: State Farm W 3, D 0, R 0; Goldman Sachs W 3, D 0, R 0; Toyota D 10 + R 6; T-Mobile D 8 + R 8; NVIDIA D 17 + R 9.
COUNTEREXAMPLES: Capital One drew 3 of 100 sampled entries and had 1 winner.
CONFIDENCE: low (a sample, not all entries)
TYPE: fact (sample counts) / inference (that some tracks are less crowded)
IMPLICATION FOR US: When two tracks fit equally, ask organizers or watch the room for crowding; lean toward the business-problem track fewer teams seem to pick.

(Dropped in v2: the 2024 General-winner theme claim and the T-Mobile calibration finding — see change log. The calibration case remains as a single-case anecdote in `outputs/close_reads/calibration_tmobile_2025.md`.)

---

## 7. Watch list (Q23) and what is common now (Q20)

Source: `Q23_place_not_first.csv`, `Q20_recent_vs_older.csv`.

FINDING 7.1: A few types are over-represented among 2nd/3rd/HM relative to 1st, and a few the other way; all gaps are small.
SUPPORT: share in 2nd/3rd/HM vs 1st (paired): new_data_or_context novelty 24 of 227 (11%) vs 6 of 129 (5%); education_feedback 23 of 227 (10%) vs 6 of 129 (5%); single_call_wrapper 34 of 227 (15%) vs 13 of 129 (10%); data_to_decision 35 of 227 (15%) vs 15 of 129 (12%). General tracks: education_feedback 16 of 117 (14%) vs 2 of 61 (3%, low n). Over-represented among 1sts: sensor_to_alert 16 of 129 (12%) vs 13 of 224 (6%) (`Q01_paired_all_tracks.csv`).
COUNTEREXAMPLES: every type has 1sts.
CONFIDENCE: low (gaps 3–6 points, picked from about 30 rows)
TYPE: association
IMPLICATION FOR US: Watch list, not a ban: a study/quiz feedback app, a one-prompt wrapper, or a dashboard as the whole product needs a strong reason (e.g. the sponsor asked for it — State Farm's most common past-winner pattern is education_feedback).

FINDING 7.2: Agentic AI and live data have become more common among winners; neither is required.
SUPPORT: winners since 2025-06 vs older: agentic_multistep 187 of 715 (26%) vs 31 of 330 (9%) (weighted 27% vs 7%); single_call_wrapper 12% vs 19%; no AI 121 of 715 (17%) vs 26%; live data 444 of 681 (65%) vs 169 of 301 (56%); hardware 24% vs 21%.
COUNTEREXAMPLES: 237 of 681 recent winners (35%) without live data; 17% without AI.
CONFIDENCE: medium (event mix also changed; weighted columns agree)
TYPE: fact
IMPLICATION FOR US: Agentic AI and live data are common, not distinctive by themselves; HackUTD 2025 still showed an agentic gap (Finding 0.2), so if AI is used, make it multi-step and visible.

---

## 8. Data-quality note

- Coverage: 1,148 counted projects tagged and validated (`data/tagged/content_all.jsonl`; `scripts/s3_validate_merge.py`: 1,148 of 1,148 valid). One tagger model (Sonnet) for every shard; pilot agreement ≥70% on every field (`data/tagged/pilot/agreement*.md`); Opus rated presentation +0.37 above Sonnet in the pilot, so absolute ratings are model-dependent (relative comparisons only).
- Cross spot-check (10 random rows each way; `data/tagged/spotcheck_eng1.md`, `spotcheck_eng2.md`): exact agreement 84% (126 of 150 cells) and 67% (80 of 120). Weakest: presentation rating (5 of 10; 3 of 10), technical complexity rating (3 of 10, one tagger about +0.7 higher), n_user_flows (6 of 10; 5 of 10 — whether claimed-but-not-shown flows count). Sponsor track calls 10 of 10 and 8 of 10. Shards were assigned in blind_id order (random with respect to group and placement), so tagger offsets add noise rather than bias; rating and flow findings are capped at medium confidence.
- Unknown rates (`Q99_unknown_rates.csv`): mocked_parts_disclosed 530 of 1,148 (46%) — not used for comparisons; design rating 195 of 1,148 (17%); live_data 7%; cover score 80 of 1,148 (7%, incl. 16 image-only glance answers excluded).
- Cover test ceiling: 835 of 1,068 scored 3/3 (`Q15_cover_distribution_all.csv`); it detects bad covers, not great ones.
- Empty or bundled records: a few rows were empty placeholders (minimum ratings) or bundled 2–3 projects (tagged on the first); excl_weak drops thin records.
- sponsor_fit track labels varied between taggers (organizer vs company track). Q10/Q13 use only the sponsor_fit entry matched to the awarding sponsor by name; unmatched awards count as unknown.
- prompt_literalness is unknown (challenge text unavailable) for about half of sponsor-domain awards; unknowns may be selective.
- n_external_deps is a count of listed tech items, so it tracks page detail as much as build breadth.
- Videos were not watched: Q16 timing (secs_to_first_working_result, opens_with) is not measured; wow moments are page text.
- HackUTD does not publish 1st/2nd/3rd, so HackUTD rows are not in paired sets; 0 HackUTD general 1sts in Q4.
- Prize stacking is a lower bound (dataset sampled winners per track).
- Three general 1sts (Nomi, GDELT Open Intelligence Agent, AffectLink) carry a truncated event label ("2025") in `Q04_general_1sts.csv`; their event type is correct.
- Low-n cells are flagged `low_n` in the tables. Q22 (repeat teams) was not computed (member links not reliably available).

---

## Change log (v1 → v2, from `outputs/redteam_review.md`)

- Fixed numbers: HackUTD multi-award 12 of 69 (was "15 of 71"); ai_role none is 7 of 15 hardware (was "mostly hardware"); 0.6 image counts (2 unknown; counterexamples added); 0.5 "non-winners describe only" restricted to demo_ready; "almost all 1sts pass the cover" → 81–85%; cover ceiling now from a table (835 of 1,068); 2.1 gap list reordered; 6.1 2024 count replaced by the table's problem-only 11 of 19 / data-core 7 of 19.
- Weakened wording/confidence: 0.4, 0.5, 0.7 (dependency claim removed), 1.1, 2.1 (scope + exceptions), 2.2 (no separating dimension), 2.3, 3.1 (no service cap), 3.2, 4.1 (implication labelled inference), 4.2 (confidence low), 4.3 (no "one deep use beats many"), 5.1–5.4, 6.1, 6.2, 7.1 (watch list, both directions), 7.2 (common, not table stakes).
- Added: 0.8 (sponsor product use does not separate), 0.9 (familiar-idea novelty), 1.2 (general vs sponsor 1sts), close-read ≥3-working support in 0.1, theme-track and literalness exceptions in 2.1.
- Dropped: 6.3 (2024 General theme: n = 3, confounded with the Goldman prompt, "new interaction" not in any table); 6.4 (T-Mobile calibration: single case, placement assumed, ratings not in a table; kept as anecdote in the close read).
- Removed time estimates from `outputs/close_reads/calibration_tmobile_2025.md` and `hackutd_2025_winners.md`.
