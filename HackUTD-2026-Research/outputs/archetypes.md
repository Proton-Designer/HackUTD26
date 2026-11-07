# Q4 — General 1st-place archetypes (TASK-105, eng2)

**What this is.** The 65 general 1st-place projects in `data/tables/Q04_general_1sts.csv`, sorted by hand into 5 recurring profiles. I read each row's pattern, ai_role, has_hardware, live_data, novelty_source, centerpiece, wow and one_sentence, then decided the group. The assignment is in `data/tables/Q04_archetype_assignment.csv`. A script (`scripts/q04_archetype_counts.py`) only counted rows afterwards and wrote `data/tables/Q04_archetype_counts.csv`.

**How to read the numbers.**
- "n of N (pct%)" is unweighted. "weighted" uses the table's `weight` column: hackutd and student_24h rows count 2, student_36_48h rows count 1, corporate/online rows count 0.5. The `weight` column was set earlier in the pipeline and I did not change it.
- All 65 rows are **video-or-page-derived tags** from Devpost submissions, not live judging. HackUTD's own 1sts are not in this table (see "HackUTD fit"). Labels: **fact** = counted from the table; **inference** = my reading.
- Group boundaries are my judgment. The hardware group is clean because it is defined by `has_hardware = True` (22 of the 23 hardware rows; the 23rd, Chronomancer, went to Playful). The other groups overlap at the edges (for example Orca could be Playful), so treat the counts as approximate to ±2 rows.

| Archetype | n of 65 | pct | weighted |
|---|---|---|---|
| A. Hardware sense-and-act loop | 22 | 34% | 31% |
| B. Multimodal human-need pipeline | 16 | 25% | 27% |
| C. Agent / dev-tool automation | 11 | 17% | 16% |
| D. Playful new interaction | 9 | 14% | 14% |
| E. Data-to-decision utility (low n) | 4 | 6% | 8% |
| Unassigned / other | 3 | 5% | 4% |

---

## A. Hardware sense-and-act loop (22 of 65, 34%; weighted 31%)

**Shape:** A physical device senses something, a model or rule decides, and something visible happens in the real world or on a live dashboard.

**Defining fields** (`Q04_archetype_counts.csv`):
- has_hardware = True: 22 of 22 (100%).
- live_data = yes: 19 of 22 (86%; weighted 85%).
- pattern sensor_to_alert_or_action: 10 of 22 (45%; weighted 43%). Next: realtime_coordination 3 (14%) and vision_to_assist 3 (14%).
- ai_role: none 7 (32%), multimodal_pipeline 5 (23%), custom_or_finetuned_model 4 (18%), on_device 3 (14%), agentic_multistep 2 (9%). So AI is not required.
- novelty_source: combination 10 (45%), new_interaction 6 (27%).
- event_type: student_36_48h 15 (68%; weighted 57%), student_24h_inperson 5 (23%; weighted 38%).

**Examples**
- **REMI** (BoilerMake XII): "Purdue students rent nearby owner-listed bikes, unlocked by phone through a custom NFC smart lock." https://devpost.com/software/remi-hbkrzs
- **Pyrosense** (Hack the Valley 11): "Firefighters wear a helmet unit that maps buildings and gas; incident commanders see a live 3D hazard heat map." https://devpost.com/software/pyrosafe
- **Shepherd** (TreeHacks 2026): "Blind and low-vision pedestrians get a roughly $50 motorized cane that steers them around obstacles using iPhone LiDAR." https://devpost.com/software/raising-cane

**Exception:** **Kitkat** (HackNotts '26) has hardware but no AI, no live data and no user problem. It is a 3D-printed ESP32 flip phone with a custom OS (https://devpost.com/software/kitkat). Inference: it won as a finished craft build, so "hardware" alone is not the pattern. A live loop is.

**Typical centerpiece and wow:** a self-built sensor-to-actuator or sensor-to-map chain (NFC lock, LiDAR SLAM plus gas readings, steering cane). The wow is the physical or on-screen result happening on cue: the phone unlocks the lock, the heat map paints the floor, the cane nudges left.

**HackUTD fit: weak to uncertain (inference).** None of the six HackUTD general winners in the close reads (`outputs/close_reads/hackutd_2024_winners.md`, `hackutd_2025_winners.md`) is described as hardware: TalkTuahBank, Lumo, Ripple Banking (2024); NLB, ProdigyPM, Working Memory (2025). The 2024 close read excludes one "General and Hardware Track" winner (Roomie) for thin evidence. Hardware is common among general 1sts overall, but HackUTD general winners look software-first. Hardware also costs the most to set up at a table.

**What a 4-person team must show at the table:** the device working live with one visible trigger-and-response right at the start of the demo, a backup video of the same loop, and one sentence naming the real user. Bring spares for the single point of failure (power, radio, sensor).

**Risks:** a wiring or radio failure at the table, setup time, and judges who cannot see the loop from a distance. Nothing in this table shows how often hardware loops failed at the table. That is not in the data.

---

## B. Multimodal human-need pipeline (16 of 65, 25%; weighted 27%)

**Shape:** Camera, voice or document input goes through a multimodal model to give a specific group of people something they could not do before: sight, reading, coaching, surgery guidance.

**Defining fields:**
- ai_role = multimodal_pipeline: 15 of 16 (94%; weighted 91%).
- has_hardware = False: 16 of 16 (100%).
- pattern vision_to_assist: 7 (44%; weighted 40%). Next: voice_to_action 2 and education_feedback 2 (12% each).
- live_data = yes: 9 (56%), no: 7 (44%).
- novelty_source: combination 8 (50%; weighted 55%), new_interaction 3 (19%), new_user_group 3 (19%).
- event_type: student_24h_inperson 8 (50%; weighted 68%), student_36_48h 7 (44%).

**Examples**
- **StoryVue** (VTHacks 13): "Visually impaired children point a camera at a printed book and hear it read, explained or summarised by voice." https://devpost.com/software/storyvue
- **SeeForMe** (McHacks 12): "Visually or mobility impaired people hear nearby objects announced and get spoken turn-by-turn directions by voice command." https://devpost.com/software/seeforme
- **Scrub+** (HackNC 2026): "Scrubbed-in surgeons navigate 3D CT scans by gesture and voice, measure margins and compare cutting plans without touching a computer." https://devpost.com/software/scrub-d67fm5

**Exception:** **Vril** (Hack Western 12) is multimodal but has no live data and no disability or health user. A non-designer types a prompt and gets an editable 3D product with dielines. Inference: it won on the depth of the editing tool (https://devpost.com/software/vril).

**Typical centerpiece and wow:** a stitched pipeline (detector or OCR, then an LLM, then speech or a 3D view). The wow is a person pointing a camera or speaking and getting an answer back at once.

**HackUTD fit: medium to strong (inference).** TalkTuahBank (2024) is a voice agent that runs banking actions by phone call for people with no smartphone. It is the closest HackUTD general winner to this shape. The other five HackUTD general winners are text and screen apps. Q20 (`data/tables/Q20_recent_vs_older.csv`) shows multimodal_pipeline is 27% of recent winners vs 24% of older ones (all winners, not only 1sts), so the shape is not fading.

**What a 4-person team must show at the table:** the live input working on the judge's own object or voice (a book, a hand, a spoken question), the named user group, and one number or outcome from a real or realistic input.

**Risks:** many entries look alike (vision_to_assist alone is 10 of 65, 15%), so novelty must come from the user group or the combination. Inference (not in the data): live demos depend on lighting, noise and wifi.

---

## C. Agent / dev-tool automation (11 of 65, 17%; weighted 16%)

**Shape:** Software that takes a developer or office task off a person's hands: agents triage a bug, block a bad dependency, run a Mac by voice.

**Defining fields:**
- has_hardware = False: 11 of 11 (100%).
- ai_role agentic_multistep: 7 (64%; weighted 63%); none 2 (18%).
- pattern: devtool 4 (36%), workflow_automation_agent 3 (27%), risk_detect_and_respond 2 (18%).
- novelty_source technical_method: 6 (55%; weighted 48%), combination 3 (27%).
- live_data = yes 6 (55%), no 4 (36%).
- event_type: student_36_48h 7 (64%), student_24h_inperson 3 (27%; weighted 44%).

**Examples**
- **Alto** (LA Hacks 2025): "Mobile developers get a multi-agent pipeline that ingests bug reports, pulls repo code, hypothesizes root causes and posts to Slack." https://devpost.com/software/alto
- **Preflight-ai** (NMIT HACKS 2026): "Developers get pull requests blocked or flagged when npm dependency upgrades look malicious, using scans plus a Gemini verdict." (no Devpost link in the table)
- **FaceTimeOS: AI Mac Agent** (Cal Hacks 12.0, 2025): "Remote workers FaceTime or iMessage their Mac and an AI agent runs tasks, talks back and texts a screenshot." https://devpost.com/software/facetime-macos-ai-agent

**Exception:** **convertfs** (HackUPC 2026) has no AI. It is a FUSE filesystem that converts files as you drop them in (https://devpost.com/software/convertfs). Its novelty is purely technical method.

**Typical centerpiece and wow:** a multi-step chain with a clear before/after (bug report in, root-cause hypothesis in Slack; PR opened, BLOCK comment appears). The wow is the result landing in a tool the judge already uses.

**HackUTD fit: strong (inference).** Working Memory (VS Code extension plus MCP, 2025) and ProdigyPM (agents pushing to Jira, 2025) are both this shape. That is 2 of the 6 HackUTD general winners in the close reads. Q20 shows agentic_multistep at 26% of recent winners vs 9% of older (all winners; weighted 27% vs 7%), the largest shift in that table. This archetype is rising.

**What a 4-person team must show at the table:** one end-to-end run on a real input from the judge's world (a real repo, a real PR), the tool the result lands in, and what it checks before acting. ProdigyPM's close read says the available evidence did not explain its win, so do not rely on a thin demo.

**Risks:** crowded space (agentic projects are 187 of 715 recent winners in Q20, 26%), and judges may see a wrapper over an API unless the checks or the multi-step logic are visible.

---

## D. Playful new interaction (9 of 65, 14%; weighted 14%)

**Shape:** A game, toy or creative tool whose fun comes from a new way to play: a webcam as controller, betting on a live fish tank, an AI stand-in that lives on after you log off.

**Defining fields:**
- pattern game_or_social: 7 of 9 (78%; weighted 83%); the other 2 are translate_between_people_or_systems.
- has_hardware = False: 8 (89%).
- novelty_source: new_interaction 4 (44%), combination 3 (33%).
- ai_role is spread out: single_call_wrapper 3 (33%), custom_or_finetuned_model 2 (22%), and one each of multimodal, none, on_device, agentic.
- live_data: no 5 (56%), yes 4 (44%; weighted 58%).
- event_type: student_36_48h 6 (67%), student_24h_inperson 3 (33%).

**Examples**
- **kinemo** (PennApps XXVI): "Two players use a laptop webcam and body pose to play three motion-controlled games with a gesture menu." https://devpost.com/software/kinemo
- **Wager Whales** (HackNJIT 2023): "Casual players bet play-money coins that a fish will enter a region they draw on a live aquarium stream." https://devpost.com/software/wager-whales
- **Identity Matrix** (UofTHacks 13): "Players curious about social simulation join a shared pixel world where an AI agent of them keeps socializing after logoff." https://devpost.com/software/temp-sqyptg

**Exception:** **Growth Garden** (UNIHACK 2025) is a calming habit tracker, not a competitive or novel-input game, and it uses one LLM call. Inference: its draw is polish: surface snapping on a 3D planet plus ambient audio (https://devpost.com/software/growth-garden).

**Typical centerpiece and wow:** an input method nobody expects (body pose, a drawn box on a live feed) or a world that keeps running without you. Inference: the wow is judges playing it themselves.

**HackUTD fit: weak to uncertain (inference).** None of the six HackUTD general winners is a game. The overall table (Q07, `data/tables/Q07_novelty_general1_vs_sponsor1.csv`) shows game_or_social at 8 of 65 general 1sts (12%) vs 1 of 54 sponsor 1sts (2%), so game_or_social is 8 of 65 general 1sts vs 1 of 54 sponsor 1sts. Two of the three 2024 HackUTD general winners (TalkTuahBank, Lumo) also won the Goldman Sachs prize, so sponsor-themed framing may matter there. That is inference from the close reads.

**What a 4-person team must show at the table:** a judge able to play immediately on arriving, with no setup or sign-up.

**Risks (inference, not in the data):** this group may be the most fragile on the "so what" question. Judges can enjoy it and still ask what problem it solves.

---

## E. Data-to-decision utility (4 of 65, 6%; weighted 8%; low n)

**Shape:** An ordinary dashboard or planner that turns real data into a decision for a defined user: whale-strike risk for ship routes, courses that count toward a degree, rescue routes.

**Defining fields (n=4, treat as descriptive only):**
- pattern data_to_decision 2 of 4 (50%); ai_role none 2 (50%); has_hardware False 3 (75%).
- novelty_source new_user_group 2 (50%).
- event_type student_24h_inperson 3 (75%; weighted 86%).

**Examples**
- **WhaleBeing** (DeltaHacks XI): "Shipping operators and conservationists see daily blue whale habitat and the strike risk of a chosen ship route." https://devpost.com/software/whalebeing-27sj0w
- **McGill Go** (McHacks 13): "McGill students planning exchange find host-university courses that count toward their degree using scraped catalog data." https://devpost.com/software/exchange-v1hmq8
- **Search and Rescue** (HooHacks 2026): "Emergency planners design multi-floor buildings in 2D/3D and simulate routed rescues with hazards." https://devpost.com/software/search-and-rescue-2pwlkf

**Exception:** **BravoDispatch** (Hack Western 11) has no visible centerpiece in the table and is a single LLM call (docs_to_action). It stays here by pattern only, so it is the weakest fit in the group.

**HackUTD fit: medium (inference).** NLB (2025) and Lumo (2024) are everyday-utility apps with a clear user. The overall table shows data_to_decision is 4 of 65 general 1sts (6%) vs 14 of 54 sponsor 1sts (26%) (Q07), so this shape is 14 of 54 sponsor 1sts vs 4 of 65 general 1sts. Q20 shows data_to_decision falling from 20% of older winners to 14% of recent ones.

**What a 4-person team must show at the table:** one real dataset, one decision the user can make from it, and a screen that shows the answer without explanation.

**Risks:** with 4 rows nothing here is solid. It may be a sponsor-track shape that happened to win general at small events.

---

## Unassigned / other (3 of 65, 5%)

Team Zenith Hacks (hackCBS 7.0), Placement-ke-Pyaase (HackOut'25) and One Million Notes (UofTHacks 12). All three have pattern = other, ai_role = none, novelty_source = execution_of_familiar_idea, and unknown hardware and live_data. The table has no centerpiece or wow for any of them (all `none_visible`), so I could not place them. They do not change any share above by more than 5 points.

---

## Findings

```
FINDING: About a third of general 1sts are hardware sense-and-act loops, and 86% of those run on live data.
SUPPORT: 22 of 65 (34%; weighted 31%) are archetype A; within A, live_data = yes is 19 of 22 (86%). Q04 has_hardware = True is 23 of 65 (35%; weighted 33%), against 169 of 707 (24%) for all recent winners in Q20. Examples: REMI https://devpost.com/software/remi-hbkrzs, Pyrosense https://devpost.com/software/pyrosafe, Shepherd https://devpost.com/software/raising-cane
COUNTEREXAMPLES: Kitkat (hardware, no live data, no AI) and 3 of 22 hardware rows with live_data no or unknown. The six HackUTD general winners in the close reads are software.
CONFIDENCE: medium (counts are exact; the hardware-vs-all-winners gap compares 1sts to a different population)
TYPE: association
IMPLICATION FOR US: Most hardware 1sts (19 of 22) ran a live loop. Do not add hardware for novelty if the team cannot make one loop work on stage.
```

```
FINDING: Software archetypes B and C together make up 42% of general 1sts, and both are built on multimodal or agentic AI.
SUPPORT: 27 of 65 (42%; weighted 43%): B 16 (multimodal_pipeline 15 of 16, 94%) and C 11 (agentic_multistep 7 of 11, 64%). Examples: StoryVue https://devpost.com/software/storyvue, Alto https://devpost.com/software/alto, FaceTimeOS https://devpost.com/software/facetime-macos-ai-agent
COUNTEREXAMPLES: convertfs (no AI), Vril (no live data, no user problem beyond design). 2 of 11 C rows have ai_role = none.
CONFIDENCE: medium (hand-grouped; boundaries overlap by about 2 rows)
TYPE: association
IMPLICATION FOR US: If we go software, pick B or C and name the exact user and the exact input. Of the six HackUTD 2024-25 general winners, TalkTuahBank maps to B and Working Memory and ProdigyPM map to C; the other three are unassigned (not tagged in the 65-row table).
```

```
FINDING: Data-to-decision is 4 of 65 general 1sts (6%) but 14 of 54 sponsor 1sts (26%).
SUPPORT: general 1st 4 of 65 (6%) vs sponsor 1st 14 of 54 (26%) for pattern data_to_decision, from `Q07_novelty_general1_vs_sponsor1.csv`. Archetype E is not the same set. The four general 1sts with pattern data_to_decision are WhaleBeing (E), McGill Go (E), Post Surgery Pillow (A) and GDELT Open Intelligence Agent (C); E also holds BravoDispatch (docs_to_action) and Search and Rescue (realtime_coordination). Examples: WhaleBeing https://devpost.com/software/whalebeing-27sj0w, McGill Go https://devpost.com/software/exchange-v1hmq8
COUNTEREXAMPLES: none among the 4 contradict the count, but only 2 of the 4 sit in archetype E (the other two are in a hardware and an agent archetype); the 14 sponsor-track 1sts are not listed here.
CONFIDENCE: medium (Q07 counts are exact; both groups are small)
TYPE: association
IMPLICATION FOR US: Use a data-to-decision build as the sponsor-track or side-prize layer of a plan, not as the general-track centerpiece.
```

## Not done / caveats
- HackUTD 2024 and 2025 general winners are not in the 65-row table, so "HackUTD fit" is my reading of the two close-read files, not counted tags.
- No weighted share for the six HackUTD winners. I did not tag them.
- Group boundaries (B vs D for Orca, A vs D for Chronomancer, C vs B for Percival and TalkTuahAirline) are judgment calls. Chronomancer is in D despite hardware = True, which is why A has 22 rows and not 23.
- No team member names appear. Preflight-ai has no Devpost link in the source table.

## Revisions after red team (TASK-107)
- M15: Finding 3 no longer equates archetype E with data_to_decision; the four data_to_decision 1sts and their archetypes are listed, and E's non-matching rows are named.
- M16: "why they won" statements for Kitkat, Vril, Growth Garden and the Playful wow now start with "Inference:"; the hardware implication now reads "19 of 22 ran a live loop" instead of "only when".
- L6: risk lines for B and D are labelled inference, not in the data.
- L7: HackUTD-fit line in Finding 2 names the mapping (TalkTuahBank to B, Working Memory and ProdigyPM to C) and says the other three are unassigned.
- Red-team §5: win-rate phrasing in D and E replaced by counts (8 of 65 vs 1 of 54; 14 of 54 vs 4 of 65).
- Truncated event label "2025" (Nomi, GDELT Open Intelligence Agent, AffectLink) in the Q04 tables: none of the three is used as an example here, but GDELT is cited above by pattern; the upstream label is still to be fixed in `Q04_general_1sts.csv` and `Q04_archetype_assignment.csv`.
