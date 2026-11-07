# Red-team review: TRACK_DAY_KIT.md + archetypes.md (TASK-106, eng1)

Reviewer: eng1, who wrote neither file. Neither reviewed file was edited. I checked every number I could against `data/tables/` (Q00, Q01, Q04, Q07, Q09, Q10, Q11, Q18, Q19, Q20, Q23) and read both files against `outputs/findings.md`, spec §0, §1, §5, §7, and `outputs/sponsor_cards.md`. Line numbers refer to the reviewed files as read at this time.

## Verdict
- **Numbers are clean.** I found 0 numeric mismatches in either file. Every count I traced matches its table (list in "What I verified").
- The problems are in the reasoning: causal or over-strong wording, evidence labels dropped on the way from findings to rules, and three actionable contradictions (NMC2 depth rule, the hardware-first candidate rule, "table stakes").
- Totals: **4 high, 16 medium, 7 low.**

---

## HIGH

**H1 · TRACK_DAY_KIT.md:162 (also :39) · NMC2 classed as tool-style, but its winners did not need NMC tech.**
§7 says NVIDIA / NMC2 / Spacetime / 8090 AI "(tool-style): one sponsor feature load-bearing and shown working". Q13 rows for NMC2: sponsor_removable = yes 6 of 6, sponsor_features_used = 0 for 6 of 6. Q19 award integration marks the HackUTD 2025 NMC winners DataDriver and DCDaddy as `problem_only` (22 of 24 sponsor-domain awards, `Q19_hackutd2025_award_integration_counts.csv`). `sponsor_cards.md` already says problem-fit for NMC2. A team following the kit would spend effort forcing NMC tech in.
Fix: move NMC2 to the problem-style bucket (rule 7), with "datacenter/AI-ops problem, confirm identity at the workshop". For 8090 AI, say "no dataset evidence; ask at the booth" instead of tool-style.

**H2 · TRACK_DAY_KIT.md:25 and :108 · "table stakes" is not supported by the numbers it cites.**
Rule 5 says "Agentic + live data are now table stakes". 5c says "Table stakes: live data, a real AI pipeline". Q20 (`Q20_recent_vs_older.csv`): agentic_multistep 187 of 715 (26%) of recent winners, live_data 444 of 681 (65%). So 74% of recent winners are not agentic and 35% have no live data. F7.2 says "common", not "table stakes", and the sibling findings (F0.2, F1.1) say 15 of 65 general 1sts have no AI at all. As worded, the kit tells the team an agent is mandatory.
Fix: "Common among recent winners (agentic 26%, live data 65%); not required. If AI is used, make it multi-step."

**H3 · TRACK_DAY_KIT.md:42 (plus :178) · Candidate seeding pushes the hardware archetype, which `archetypes.md` rates a weak HackUTD fit, and never mentions the 24-hour limit.**
Step 3: "Aim for at least one candidate from A or B and one from C." `archetypes.md:42`: A "HackUTD fit: weak to uncertain" (0 of 6 HackUTD general winners are hardware). `archetypes.md` also rates C "strong", B "medium to strong", D weak, E medium. A's evidence base is 15 of 22 (68%) from 36–48h events, 5 of 22 (23%) from 24h in-person (`Q04_archetype_counts.csv`); HackUTD 2026 is 24 hours (`06_hackutd_2026_sponsors/README.md`). The kit's own event-facts line (:178) omits the duration. Hardware has the highest feasibility risk for a 24h build.
Fix: seed from B and C first, A only if the team already has a working hardware loop; add "24-hour event; archetype A evidence is mostly 36–48h events" and put the duration in the event-facts line.

**H4 · TRACK_DAY_KIT.md:22 · Rule 2 states an inference as a conclusion.**
"No tagged field separates 1st from 2nd/3rd; so the table demo and Q&A decide it." F2.1 says the cause "is not explained by available evidence (likely the live pitch and judge Q&A, which are not in the data)". Spec §1 rules 7 and 8 and §4 (cut: judge Q&A / psychology) forbid asserting this. The same sentence turns "no visible difference" into "the demo decides".
Fix: "Nothing visible on Devpost separates 1st from 2nd/3rd; why is not explained by available evidence. Inference: the live demo and Q&A may matter, so rehearse both."

---

## MEDIUM

**M1 · TRACK_DAY_KIT.md:21 · Rule 1 is comparative and causal beyond F0.1.**
"beats many claimed" was not tested. "two connected working flows is what separated 2025 winners from strong non-winners (23% vs 0%)" gives no n (8 of 35 vs 0 of 47) and "connected" is not a tagged field. 77% of winners did NOT show two flows, and F0.1's own counterexample says one complete flow is enough. "strong non-winners often show none working" is 9 of 47 (19%) with zero flows. This also sits awkwardly with 5a (second flow optional).
Fix: "Winners more often showed two working flows (8 of 35, 23% vs 0 of 47 demo-ready); 25 of 35 (71%) showed one. Association, HackUTD 2025 only."

**M2 · TRACK_DAY_KIT.md:23 · Rule 3 outruns its findings.**
F2.2 paired median gap is 0.0 on all six dimensions. F2.3 is confidence "low–medium" (min rating: 47 higher / 46 equal / 34 lower). Rule 3 turns this into "no dimension may be weak" and says 1sts "edge out peers most on technical complexity and presentation" without the sign counts (54/37/36 and 52/37/38).
Fix: add the counts and confidence ("slightly more often, low–medium"), keep it as a gate, not a finding.

**M3 · TRACK_DAY_KIT.md:24 · Rule 4 ignores the contrary within-track result.**
It cites F0.5 (HackUTD 2025 winners vs non-winners) and F3.2. F3.2 shows the centerpiece shown in demo output in 30 of 61 (49%) of paired general 1sts vs 67 of 117 (57%) of 2nd/3rd: no 1st advantage. The rule is HackUTD-2025-only evidence and should say so.
Fix: "HackUTD 2025: winners showed the centerpiece more often than non-winners. Across other events 1sts show it no more often than 2nd/3rd."

**M4 · TRACK_DAY_KIT.md:27 and :161 · Rule 7 wording and missing caveats.**
- "reward" is causal. F4.2 is TYPE association.
- 88% vs 67% (15 of 17 vs 18 of 27) is literalness known for only 17 1sts and 27 lower placers; 17 of 34 and 29 of 56 are unknown (`Q10_sponsor_fit_by_placement.csv`). The kit drops this.
- F4.2 evidence covers "banks, insurance, real estate, energy"; :161 extends it to health and legal. Axxess and Winstead have 0 dataset winners (cards are brief-only), so that extension has no data.
Fix: add n and the unknown share, say "association", drop health/legal or label them "[brief only, no evidence]".

**M5 · TRACK_DAY_KIT.md:57–68 and :161 · Matrix and rule 7 do not cover Capital One's API-depth awards or Photon.**
Capital One is listed under banks (problem-style). Q13: 9 of 42 Capital One awards are sponsor_api_depth and 12 of 42 (29%) are non-removable (`sponsor_cards.md` Capital One card). Photon is industry `other` in the spec and has no row; Q11 has an `other` industry (N=106) the kit omits, and Photon has 17 dataset winners, 13 of 17 non-removable. Photon is only mentioned in §8 as "unknown".
Fix: add a Photon/`other` row or note, and flag Capital One as "mostly problem-style; API-depth prize possible, see card".

**M6 · TRACK_DAY_KIT.md:28 · Rule 8 reads placement into an any-place finding.**
F4.3 is any-place only (1st vs lower: low n, 3 vs 5–6; confidence "low" for that comparison). "reward one load-bearing feature" and its source line "one deep use beats many shallow ones" are not supported. 55% used exactly one feature, so 45% used 2+; Spacetime (median 2) and NVIDIA (median 2) cards show more than one.
Fix: "Most API-depth winners (85%) made the tool non-removable; 55% used one feature, 45% two or more. No evidence on which depth places higher."

**M7 · TRACK_DAY_KIT.md:95 · "≤ 4 external services" is presented as a rule, not a finding.**
F3.1 reports 0–2 deps 38%, 3–4 44%, 5–7 15% of general 1sts; F0.7 says 5–7 dependencies are more common in HackUTD 2025 winners (8 of 36, 22% vs 3 of 50, 6% demo-ready) and "more integrations are fine if they all work". The cap contradicts F0.7.
Fix: reword as "typical general 1st uses 0–4 (82%); more is fine if each works at the table".

**M8 · TRACK_DAY_KIT.md:118–119 and :127 · Demo-timing advice has no data behind it.**
"Show the working result immediately … before architecture or slides" and "Open on the working result, not a title card" are not in any table: videos were not watched and `secs_to_first_working_result` / `opens_with` were not measured (`findings.md` data-quality note). F5.3 is inference, confidence low–medium. The kit presents these as template rules without the label.
Fix: tag 5e step 2 and 5f first bullet "[inference; Q16 opening not measured]".

**M9 · TRACK_DAY_KIT.md:145–154 · The judge-question table is unlabeled inference.**
Spec §4 cuts "judge Q&A" and "judge psychology" as unobservable; §0.3 allows predicted questions only via Q6/Q21. The "why they ask" column is judge-intent inference, and "static data cost points last year" rests on one case (n=3, F6.4).
Fix: header "Predicted questions (inference; not observed)" and cite the single calibration case as such.

**M10 · TRACK_DAY_KIT.md:70 · "Competition is uneven" generalises from a 100-entry baseline sample.**
`Q19_hackutd2025_track_targeting.csv`: State Farm 0 of 50 demo_ready, 0 of 50 random; Goldman Sachs 0 and 0 (the "3 prizes each" is right, 3 of 36 winners each). F6.2 itself says the baseline is a sample of 100 of 367 entries. Absence in a sample is not "nobody entered", and spec §4 cuts submissions-per-track.
Fix: "Of 100 sampled non-winners, none targeted State Farm or Goldman (sample, not all entries); ask organizers for entry counts."

**M11 · TRACK_DAY_KIT.md:163 · T-Mobile calibration is over-stated.**
"3rd-place gap was technical complexity and completeness, not idea". The close read has innovation −0.5 (Beacon 4, HarmoniQ 3), so idea is not gap-free. It is n = 3 analyst ratings (`calibration_tmobile_2025.md`), and the 1st/2nd/3rd order is team-reported, not on Devpost (spec Q21 note). The kit drops all of that.
Fix: "(n=3, analyst ratings, placement team-reported): largest gaps were technical complexity and completeness; innovation −0.5".

**M12 · TRACK_DAY_KIT.md:100–105 · Avoid list drops F7.1's confidence.**
F7.1 is confidence "low" with gaps 3–6 points overall (education_feedback 23 of 227 (10%) vs 6 of 129 (5%)). The kit says "reject fast". It also conflicts with the data for State Farm: education_feedback is the top insurance pattern (Q11, 5 of 14) and 4 of 13 State Farm card rows. The kit's "unless the track literally asks" does not cover a sponsor track that historically rewards it.
Fix: "low-confidence signal; a sponsor track that rewarded it (State Farm) is an exception".

**M13 · TRACK_DAY_KIT.md:29 and :134 · "floors" overstates what Q18 shows.**
Rule 9 calls images, video and full Devpost sections floors. Q18 for general 1sts: video 47 of 56 (84%), what's-next 45 of 56 (80%), accomplishments 41 of 56 (73%), 0 images 5 of 58 (9%). A floor means near-universal; the table shows 11–27% of 1sts lack these. "≥ 4 images" appears in no table (≥4 images = 4–6 plus >6 = 38 of 58, 66% of general 1sts; 73% of HackUTD 2025 winners).
Fix: "typical, not universal (e.g. 84% embedded video)"; say the "≥ 4 images" threshold is a judgment.

**M14 · TRACK_DAY_KIT.md:111–115 · Cover-test template shows only bad examples.**
Spec §7 output 5 and Q15 ask for best and worst tagline examples. `Q15_cover_examples_1sts.csv` has them. The kit shows three bad covers and no good one, so the "one line" format has no real exemplar.
Fix: add 2–3 best-scoring real 1st-place covers from Q15.

**M15 · archetypes.md:188–194 (Finding 3) · Archetype E is not the data_to_decision set the finding claims.**
"My archetype E (n=4) is the small hand-grouped version of this." Of the 4 general 1sts with pattern = data_to_decision (WhaleBeing, McGill Go, Post Surgery Pillow, GDELT Open Intelligence Agent), only 2 are in E; Post Surgery Pillow is in A and GDELT is in C. E also holds a `docs_to_action` row and a `realtime_coordination` row (Search and Rescue is listed as an example, but its pattern is realtime_coordination). The "COUNTEREXAMPLES: none found among the 4" line is therefore wrong: the other two data_to_decision 1sts are in other archetypes (a hardware pillow, an agent).
Fix: drop the E equivalence; list all four data_to_decision 1sts and where they were assigned.

**M16 · archetypes.md:38, :67, :125, :127, :175 · Causal "why they won" statements and one self-contradicting implication.**
Spec §1 rule 7: why judges chose something is inference unless a judge or press says it. Lines: Kitkat "It won as a finished craft build" (:38); Vril "It won on the depth of the editing tool" (:67); Growth Garden "Its draw is polish" (:125); "The wow is judges playing it themselves" (:127). Line 175: "Hardware is a valid general-track route, but only when the loop is live and visible" is contradicted by the same file's exception (:38: Kitkat won with no live data, no AI) and by 3 of 22 hardware rows with live data no/unknown (:172).
Fix: prefix with "inference:" and change :175 to "most hardware 1sts (19 of 22) ran a live loop".

---

## LOW

**L1 · TRACK_DAY_KIT.md:117 · Duration estimate in the pitch skeleton.**
"expo: ~5 min demo/pitch + 2–3 min questions per judge group". This is observed from the 2024/25 Devpost pages (spec §0.1: "2024 page said 3–5 min demos"), not confirmed for 2026, and §8:175 correctly lists per-visit timing as unconfirmed. Spec §5 step 6 uses "~4.5-min station pitch", which the kit omits. Fix: mark "(observed 2024/25; confirm at opening)" and use one consistent figure.

**L2 · Time/duration scan (check 4) · no other estimates.**
Searched both files for hour, minute, day, night, morning, overnight, "by <time>". Only L1 plus official facts: video ≤ 2 min (:126, :178, spec rule). "within the event" (:44) and "once flow 1 is demo-stable" (:48) are conditions, not durations. archetypes.md "setup time" (:46) is a risk, not an estimate. No schedule ("by Saturday night") language found.

**L3 · TRACK_DAY_KIT.md:42 · Archetype counts sum to 62, not 65.**
A 22 + B 16 + C 11 + D 9 + E 4 = 62; the other 3 (5%) are "unassigned" in `Q04_archetype_counts.csv` and `archetypes.md:17`. The kit says "n of 65" without the 3. Fix: add "· unassigned 3 (5%)".

**L4 · TRACK_DAY_KIT.md:45 · Gate example is hardware-biased.**
"Judge says X into the mic → the arm does Y" nudges toward A, which H3 shows is a weak HackUTD fit. Fix: a software example too.

**L5 · TRACK_DAY_KIT.md:25 · "more common in 2nd/3rd" overstates a small gap.**
single_call_wrapper 14% vs 8% in general paired tracks (`Q01_paired_general.csv`: 16 of 117 vs 5 of 61); F3.2 calls it a "small gap". Fix: "slightly more common".

**L6 · archetypes.md:75, :133 · Unsourced risk statements.**
"Live demos depend on lighting, noise and wifi" and "the most fragile on the 'so what' question" are not in any table. The A card (:46) states "That is not in the data"; B and D do not. Fix: label as inference.

**L7 · archetypes.md:184 · Vague HackUTD-fit claim.**
"HackUTD's own 2024-25 general winners … sit in these two shapes or in text-app territory" covers every outcome, so it cannot be wrong. Fix: name which of the six map to B or C (the file already does so for TalkTuahBank → B, Working Memory and ProdigyPM → C) and say the other three are unassigned.

---

## What I verified (no mismatch found)
- Kit rule numbers: 23% vs 0% (8 of 35 vs 0 of 47, Q00); single-call 9% (6 of 65, Q04 ai_role); data_to_decision 6% (4 of 65) and 48% (24 of 50 demo_ready, Q00); 22 of 24 and 88% vs 67% (Q19, Q10); 85% (117 of 138) and 55% (77 of 141) (Q10); 30% vs 14% and 3% vs 14% (18 of 61 vs 16 of 117; 2 of 61 vs 16 of 117, Q01); 10 of 65 (15%) stacking (Q09).
- Kit §3 matrix: all 9 populated rows match Q11 for N and every top-pattern count (finance 85 / 36·10·7·6; insurance 14; telecom 12; real_estate 17; energy 9; ai_compute 123; health 17; cloud_devtools 102; auto_mobility 21); all example names appear in the Q11 examples column. Scoring weights sum to 100 and match spec §5 step 5.
- Kit §8 matches spec §6; all F-numbers cited by the kit exist in `findings.md`.
- Archetypes: sizes 22/16/11/9/4 + 3 unassigned = 65 (`Q04_archetype_counts.csv`, `Q04_archetype_assignment.csv`); I recomputed every count and weighted percent quoted in the A–E "Defining fields" lists I sampled (14 of 14 cells match, including weighted shares); hardware 23 of 65 (35%, weighted 33%); Q07 (game 8 of 65 vs 1 of 54; data_to_decision 4 of 65 vs 14 of 54); Q20 (169 of 707, 187 of 715, data_to_decision 20% → 14%). All 15 listed example projects exist in `Q04_general_1sts.csv` with matching event, one_sentence, archetype and link (event labels abbreviated: "VTHacks 13" vs "VTHacks - 13", "HackNJIT 2023" vs "HackNJIT - 2023", "Cal Hacks 12.0, 2025" vs "Cal Hacks 12.0 (2025)"; Preflight-ai has no link in the table, as noted in the file).
- No "increases the chance", "win rate", "lift" or "saturation" wording in either file. The causal-word problems are the softer "reward / beats / separated / decide / won on" forms listed above.

## Not done
- I did not re-run the S6 scripts or re-check tag quality, only table-to-document consistency.
- I did not verify finding text against close-read files beyond the T-Mobile calibration (M11) and the 22 of 24 sponsor-domain count.
- The kit's numbered F-references were checked for existence, not for each finding's full support line.
