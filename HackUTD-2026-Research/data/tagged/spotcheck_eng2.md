# Spot-check eng2 on eng1 rows (TASK-102)

Seed 102; random.sample over all eng1 S3 rows (39 shards, 578 rows). Blind: my values written before opening eng1 output. has_hardware not in output schema so not compared (mine vs record agree by inspection).

| blind_id | field | yours | theirs | agree | note |
|---|---|---|---|---|---|
| P7f055cae41 | pattern | docs_to_action | translate_between_people_or_systems | n |  |
| P7f055cae41 | ai_role | single_call_wrapper | single_call_wrapper | y |  |
| P7f055cae41 | named_user | True | True | y |  |
| P7f055cae41 | n_user_flows | 2 | 1 | n |  |
| P7f055cae41 | live_data | no | no | y |  |
| P7f055cae41 | novelty_source | combination | combination | y |  |
| P7f055cae41 | rating_innovation | 3 | 3 | y | |
| P7f055cae41 | rating_technical_complexity | 3 | 3 | y | |
| P7f055cae41 | rating_completeness | 3 | 4 | n | |
| P7f055cae41 | rating_design | 3 | 3 | y | |
| P7f055cae41 | rating_impact | 3 | 3 | y | |
| P7f055cae41 | rating_presentation | 3 | 4 | n | |
| P7f055cae41 | sponsor_fit_tracklist | ['Impiricus'] | ['Impiricus: Build the next HCP Engagement Tool'] | n |  |
| P3d74ce689d | pattern | risk_detect_and_respond | data_to_decision | n |  |
| P3d74ce689d | ai_role | multimodal_pipeline | multimodal_pipeline | y |  |
| P3d74ce689d | named_user | True | True | y |  |
| P3d74ce689d | n_user_flows | 1 | 1 | y |  |
| P3d74ce689d | live_data | no | yes | n |  |
| P3d74ce689d | novelty_source | combination | combination | y |  |
| P3d74ce689d | rating_innovation | 4 | 4 | y | |
| P3d74ce689d | rating_technical_complexity | 4 | 4 | y | |
| P3d74ce689d | rating_completeness | 3 | 3 | y | |
| P3d74ce689d | rating_design | 3 | 3 | y | |
| P3d74ce689d | rating_impact | 4 | 4 | y | |
| P3d74ce689d | rating_presentation | 3 | 3 | y | |
| P3d74ce689d | sponsor_fit_tracklist | ['Tiger Data'] | ['MLH Best Use of Tiger Data'] | n |  |
| P90e0ad34df | pattern | realtime_coordination | realtime_coordination | y |  |
| P90e0ad34df | ai_role | none | none | y |  |
| P90e0ad34df | named_user | True | True | y |  |
| P90e0ad34df | n_user_flows | 1 | 1 | y |  |
| P90e0ad34df | live_data | yes | yes | y |  |
| P90e0ad34df | novelty_source | combination | new_user_group | n |  |
| P90e0ad34df | rating_innovation | 3 | 3 | y | |
| P90e0ad34df | rating_technical_complexity | 3 | 4 | n | |
| P90e0ad34df | rating_completeness | 3 | 3 | y | |
| P90e0ad34df | rating_design | 3 | 3 | y | |
| P90e0ad34df | rating_impact | 3 | 3 | y | |
| P90e0ad34df | rating_presentation | 3 | 4 | n | |
| P90e0ad34df | sponsor_fit_tracklist | [] | [] | y |  |
| Pfa38d84ce9 | pattern | education_feedback | education_feedback | y |  |
| Pfa38d84ce9 | ai_role | single_call_wrapper | multimodal_pipeline | n |  |
| Pfa38d84ce9 | named_user | True | True | y |  |
| Pfa38d84ce9 | n_user_flows | 3 | 2 | n |  |
| Pfa38d84ce9 | live_data | no | no | y |  |
| Pfa38d84ce9 | novelty_source | combination | combination | y |  |
| Pfa38d84ce9 | rating_innovation | 4 | 4 | y | |
| Pfa38d84ce9 | rating_technical_complexity | 3 | 4 | n | |
| Pfa38d84ce9 | rating_completeness | 4 | 4 | y | |
| Pfa38d84ce9 | rating_design | 3 | 4 | n | |
| Pfa38d84ce9 | rating_impact | 3 | 3 | y | |
| Pfa38d84ce9 | rating_presentation | 4 | 4 | y | |
| Pfa38d84ce9 | sponsor_fit_tracklist | ['Cognition', 'Deepgram', 'OpenAI'] | ['Cognition: Best Use of Devin', 'Deepgram: Build Something Worth Talking To', 'OpenAI: The Fifth Teammate'] | n |  |
| P9eb85ca873 | pattern | risk_detect_and_respond | risk_detect_and_respond | y |  |
| P9eb85ca873 | ai_role | none | none | y |  |
| P9eb85ca873 | named_user | False | False | y |  |
| P9eb85ca873 | n_user_flows | 1 | 2 | n |  |
| P9eb85ca873 | live_data | no | no | y |  |
| P9eb85ca873 | novelty_source | technical_method | technical_method | y |  |
| P9eb85ca873 | rating_innovation | 3 | 3 | y | |
| P9eb85ca873 | rating_technical_complexity | 3 | 4 | n | |
| P9eb85ca873 | rating_completeness | 4 | 4 | y | |
| P9eb85ca873 | rating_design | 3 | 4 | n | |
| P9eb85ca873 | rating_impact | 3 | 3 | y | |
| P9eb85ca873 | rating_presentation | 3 | 4 | n | |
| P9eb85ca873 | sponsor_fit_tracklist | [] | [] | y |  |
| P57919ee9a0 | pattern | game_or_social | vision_to_assist | n |  |
| P57919ee9a0 | ai_role | single_call_wrapper | single_call_wrapper | y |  |
| P57919ee9a0 | named_user | True | False | n |  |
| P57919ee9a0 | n_user_flows | 1 | 1 | y |  |
| P57919ee9a0 | live_data | no | no | y |  |
| P57919ee9a0 | novelty_source | combination | execution_of_familiar_idea | n |  |
| P57919ee9a0 | rating_innovation | 3 | 3 | y | |
| P57919ee9a0 | rating_technical_complexity | 2 | 2 | y | |
| P57919ee9a0 | rating_completeness | 3 | 4 | n | |
| P57919ee9a0 | rating_design | 3 | 4 | n | |
| P57919ee9a0 | rating_impact | 2 | 2 | y | |
| P57919ee9a0 | rating_presentation | 3 | 4 | n | |
| P57919ee9a0 | sponsor_fit_tracklist | [] | [] | y |  |
| P0690b4d91a | pattern | sensor_to_alert_or_action | sensor_to_alert_or_action | y |  |
| P0690b4d91a | ai_role | on_device | multimodal_pipeline | n |  |
| P0690b4d91a | named_user | True | True | y |  |
| P0690b4d91a | n_user_flows | 3 | 3 | y |  |
| P0690b4d91a | live_data | yes | yes | y |  |
| P0690b4d91a | novelty_source | technical_method | new_interaction | n |  |
| P0690b4d91a | rating_innovation | 5 | 4 | n | |
| P0690b4d91a | rating_technical_complexity | 4 | 5 | n | |
| P0690b4d91a | rating_completeness | 4 | 4 | y | |
| P0690b4d91a | rating_design | 3 | 3 | y | |
| P0690b4d91a | rating_impact | 4 | 4 | y | |
| P0690b4d91a | rating_presentation | 4 | 4 | y | |
| P0690b4d91a | sponsor_fit_tracklist | [] | ['Espressif', 'Cognition: Best Use of Devin', 'Long Lake', 'Meta: Bringing People Closer Together With AI', 'Voloridge: Signal in the Noise'] | n |  |
| P7dedca78ff | pattern | sensor_to_alert_or_action | sensor_to_alert_or_action | y |  |
| P7dedca78ff | ai_role | on_device | on_device | y |  |
| P7dedca78ff | named_user | True | True | y |  |
| P7dedca78ff | n_user_flows | 1 | 1 | y |  |
| P7dedca78ff | live_data | yes | yes | y |  |
| P7dedca78ff | novelty_source | combination | combination | y |  |
| P7dedca78ff | rating_innovation | 3 | 4 | n | |
| P7dedca78ff | rating_technical_complexity | 4 | 5 | n | |
| P7dedca78ff | rating_completeness | 3 | 3 | y | |
| P7dedca78ff | rating_design | 3 | 3 | y | |
| P7dedca78ff | rating_impact | 4 | 4 | y | |
| P7dedca78ff | rating_presentation | 3 | 4 | n | |
| P7dedca78ff | sponsor_fit_tracklist | ['State Farm', 'Waymo'] | ['State Farm', 'Waymo'] | y |  |
| P21958759c3 | pattern | game_or_social | game_or_social | y |  |
| P21958759c3 | ai_role | custom_or_finetuned_model | custom_or_finetuned_model | y |  |
| P21958759c3 | named_user | True | True | y |  |
| P21958759c3 | n_user_flows | 1 | 0 | n |  |
| P21958759c3 | live_data | yes | yes | y |  |
| P21958759c3 | novelty_source | combination | combination | y |  |
| P21958759c3 | rating_innovation | 2 | 3 | n | |
| P21958759c3 | rating_technical_complexity | 2 | 3 | n | |
| P21958759c3 | rating_completeness | 3 | 2 | n | |
| P21958759c3 | rating_design | 3 | 3 | y | |
| P21958759c3 | rating_impact | 1 | 1 | y | |
| P21958759c3 | rating_presentation | 2 | 3 | n | |
| P21958759c3 | sponsor_fit_tracklist | [] | [] | y |  |
| Pe25a7c62ec | pattern | realtime_coordination | realtime_coordination | y |  |
| Pe25a7c62ec | ai_role | single_call_wrapper | agentic_multistep | n |  |
| Pe25a7c62ec | named_user | True | True | y |  |
| Pe25a7c62ec | n_user_flows | 1 | 2 | n |  |
| Pe25a7c62ec | live_data | no | no | y |  |
| Pe25a7c62ec | novelty_source | combination | new_interaction | n |  |
| Pe25a7c62ec | rating_innovation | 3 | 4 | n | |
| Pe25a7c62ec | rating_technical_complexity | 3 | 4 | n | |
| Pe25a7c62ec | rating_completeness | 4 | 4 | y | |
| Pe25a7c62ec | rating_design | 3 | 4 | n | |
| Pe25a7c62ec | rating_impact | 3 | 3 | y | |
| Pe25a7c62ec | rating_presentation | 4 | 5 | n | |
| Pe25a7c62ec | sponsor_fit_tracklist | ['Photon'] | ['Photon iMessage', 'Visa The Future of Shopping'] | n |  |

## Agreement per field (n of 10)
- pattern: 7/10
- ai_role: 7/10
- named_user: 9/10
- n_user_flows: 5/10
- live_data: 9/10
- novelty_source: 6/10
- rating_innovation: 6/10
- rating_technical_complexity: 3/10
- rating_completeness: 7/10
- rating_impact: 10/10
- rating_presentation: 3/10
- sponsor_fit_tracklist: 8/10

Overall exact agreement: 80/120 = 67%

## Rating offsets (theirs minus mine, mean)
- innovation: +0.2 (n=10)
- technical_complexity: +0.7 (n=10)
- completeness: +0.1 (n=10)
- design: +0.4 (n=10)
- impact: +0.0 (n=10)
- presentation: +0.7 (n=10)

## Notes and systematic differences
- sponsor_fit_tracklist: "agree" = same NUMBER of company tracks (my names are short forms; eng1 uses full track names). 8/10 agree. The two misses: P0690b4d91a (my view was truncated before sponsor_tracks_considered, so I listed none; eng1 listed 5 company tracks: my error, not theirs) and Pe25a7c62ec (eng1 also counted a Visa product track I skipped; their call is reasonable under the "include when unsure" rule).
- Ratings: eng1 is about +0.7 higher than me on technical_complexity and presentation, +0.4 on design. Impact is identical (10/10). Innovation and completeness are within +0.2. Looks like a mild upward offset on 3 of 6 dimensions, not a bias of more than one point on any row.
- n_user_flows (5/10) is the weakest of the tagging fields: I count a journey only when features are shown_working (so claimed-only records give me 1, and a 0 for none); eng1 sometimes counts 2 on the same evidence (P9eb85ca873, Pe25a7c62ec, P90e0ad34df-type claimed records) and sometimes fewer (P7f055cae41, Pfa38d84ce9). Definition ambiguity rather than error.
- pattern/ai_role differences are borderline-class cases (translate vs docs_to_action; on_device vs multimodal_pipeline; agentic vs single_call). novelty_source differences are mostly combination vs a single dominant source.
- named_user: one disagreement (LureLore, "anglers"; I said true, eng1 false). live_data: one (FloodBeacon).
- Lowest fields: technical_complexity rating (3/10) and presentation rating (3/10) by exact match, n_user_flows (5/10) among categorical tags. Differences are mostly 1 point.
- Caveat: n=10, one rater each, so agreement estimates are rough. has_hardware is not an output field and was not compared.
