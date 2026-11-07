# TASK-101 spot-check (eng1 re-tags 10 of eng2 rows, blind)

Seed 101 (random.seed(101); random.sample over all rows of the 38 eng2 S3 shards). Rows: Pb682a06cc3 (shard_pri_27), Peabd80a57a (shard_rest_34), P423203f610 (shard_rest_10), Pa9978f0b08 (shard_rest_24), P2f5a0215f6 (shard_pri_07), Pcf8dc34ed0 (shard_rest_30), Pc5c08dea22 (shard_pri_29), Pcf60c00c66 (shard_pri_31), P040efb950d (shard_rest_00), Pc2d341f78f (shard_rest_28)

Each of the 10 rows was tagged by me from the input record only before opening eng2 output. Table lists only DISAGREEMENTS (all other cells agree).

| blind_id | field | yours | theirs | agree | note |
|---|---|---|---|---|---|
| Pb682a06cc3 | ai_role | single_call_wrapper | agentic_multistep | n | |
| Pb682a06cc3 | novelty_source | new_interaction | execution_of_familiar_idea | n | |
| Pb682a06cc3 | design | 3 | 2 | n | |
| Peabd80a57a | n_user_flows | 0 | 2 | n | |
| P423203f610 | innovation | 5 | 4 | n | |
| P423203f610 | completeness | 4 | 3 | n | |
| P423203f610 | design | 3 | unknown | n | |
| P423203f610 | presentation | 4 | 3 | n | |
| Pa9978f0b08 | n_user_flows | 0 | 1 | n | |
| Pa9978f0b08 | presentation | 3 | 4 | n | |
| P2f5a0215f6 | pattern | translate_between_people_or_systems | vision_to_assist | n | |
| P2f5a0215f6 | presentation | 4 | 5 | n | |
| Pc5c08dea22 | named_user | False | True | n | |
| Pc5c08dea22 | n_user_flows | 0 | 1 | n | |
| Pc5c08dea22 | novelty_source | execution_of_familiar_idea | combination | n | |
| Pc5c08dea22 | innovation | 2 | 3 | n | |
| Pc5c08dea22 | impact | 2 | 3 | n | |
| Pc5c08dea22 | presentation | 3 | 4 | n | |
| Pcf60c00c66 | n_user_flows | 0 | 1 | n | |
| P040efb950d | named_user | False | True | n | |
| P040efb950d | presentation | 4 | 3 | n | |
| Pc2d341f78f | novelty_source | execution_of_familiar_idea | new_interaction | n | |
| Pc2d341f78f | design | 4 | 3 | n | |
| Pc2d341f78f | impact | 2 | 1 | n | |

## Per-field agreement (n of 10)

- pattern: 9/10
- ai_role: 9/10
- named_user: 8/10
- n_user_flows: 6/10
- live_data: 10/10
- novelty_source: 7/10
- innovation: 8/10
- technical_complexity: 10/10
- completeness: 9/10
- design: 7/10
- impact: 8/10
- presentation: 5/10
- sponsor_tracks: 10/10
- sponsor_removable: 10/10
- prompt_literalness: 10/10

Overall: 126/150 = 84%

## Systematic differences
(Note: has_hardware is not an output field of the S3 schema, so it was not compared.)
- innovation: mean (theirs - mine) = +0.00 over 10 rows
- technical_complexity: mean (theirs - mine) = +0.00 over 10 rows
- completeness: mean (theirs - mine) = -0.10 over 10 rows
- design: mean (theirs - mine) = -0.22 over 9 rows
- impact: mean (theirs - mine) = +0.00 over 10 rows
- presentation: mean (theirs - mine) = +0.10 over 10 rows
- n_user_flows (6/10, lowest structural gap): eng2 gives 1-2 flows to projects whose features are all `claimed` (Peabd80a57a, Pa9978f0b08, Pc5c08dea22, Pcf60c00c66); I gave 0 following "claimed-only flows don't count". Likely a one-directional offset (eng2 higher); the rule wording is ambiguous when a demo video/screenshots exist.
- presentation (5/10, lowest rating field): disagreements are +/-1 in both directions (4 of 5 off by one step, eng2 higher in 3 of 5); no consistent bias, just a noisy dimension.
- novelty_source: 3 disagreements, all involving execution_of_familiar_idea vs combination/new_interaction; boundary is fuzzy.
- named_user: eng2 more generous (Vestique "wardrobe" shoppers, BreakingPoint car-repair sufferers = True; I said False as generic).
- Organizer-vs-company track calls: all 10 agree (organizer-only lists -> []; company tracks included).
- Ratings show no rating offset overall (mean diffs within +/-0.25); design `unknown` used by eng2 for TORQ where I rated 3.
