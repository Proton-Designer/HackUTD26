# 04_deep_dives: deep-dive pass

1152 projects, each read beyond its short brief: Devpost page in full, GitHub README and repo evidence where available, prize/track text where public. Nothing here speculates about *why* something won; that is the next step.

## Counts
- Dataset: winners 911, sponsor-track 141, baseline non-winners 100 (labels preserved from the earlier passes)
- Evidence depth: A (Devpost + real README/evidence) 871, B (one source only) 255, C (thin/unreachable) 26
- Confidence: high 579, medium 529, low 44
- Projects with public prize/track text found: 748 of 1152
- Flagged for a possible second pass (depth B/C or low confidence): 289 (see second_pass_queue.txt)

## What is where
- `profiles/<dataset>/<hackathon-edition>.md`: readable profile cards (what it is, features with working status, flow, prompt fit, AI, architecture, scope, claims, gaps)
- `HackUTD_Deep_Dives.xlsx`: same data, filterable
- `data/deepdive_all.jsonl`: full structured records
- `prompts_cache/`: prize/challenge text collected per hackathon (DubHacks 2026 notes were merged into one file)
- `second_pass_queue.txt`

## Known limits (read before drawing conclusions)
- Many sponsor prompts are not public (HackUTD 2024/2025 challenges lived in a hackerpack; HackMIT 2026, several MLH/sponsor prizes list a name only). Those records say `prompt_text_found: false`; do not treat a paraphrase as the official brief.
- Depth labels were set by each agent and are not perfectly consistent: some depth-A records have boilerplate/empty READMEs and are effectively B. Counts above are recomputed from the files.
- Devpost pages and READMEs often disagree (stack, models, numbers, placement). Records keep both and say which the feature list follows; check `gaps`.
- Three evidence repos pointed at the wrong/third-party repo and were corrected by the agents (Orbis Engine, ai-companion, Doggin' Around); the latter's match is inferred.
- Two pairs share one Devpost page and carry identical content (marked `duplicate_of`): ProDuh, MayDay.
- Placement labels are unreliable for some entries (e.g. a README claiming a different place than Devpost; Recycle Tracker's "2nd place" belongs to another event; Clarify shows both Winner and Runner Up).
- Several records are stubs because no public source exists (hackCBS 7.0 teams, Vibe Coders, BREAKDANCE, Get Away, EyeCraft, Roomie). minutemesh was kept deliberately high-level.
- Team names, access codes, test logins and leaked API keys were left out of the records. Two Devpost pages (Constructa, Navo) showed live-looking keys; those teams should rotate them.
- Videos were not watched; only their descriptions/links were read.
