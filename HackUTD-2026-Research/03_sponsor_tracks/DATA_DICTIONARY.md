# Project analysis record: data dictionary (v1)

One JSON object per project, one line per project in a .jsonl file. This step is DATA COLLECTION ONLY: record observed facts and short paraphrases. Do NOT speculate about why a project won and do NOT write cross-project themes. That happens in a later step.

## Rules
- `null` = could not find / not applicable. `false` = looked and it is not there. Never use `false` for "didn't check".
- Never invent a link, stack item, number or claim. If a field is a guess, list its name in `unverified_fields`.
- Free text must be YOUR OWN short paraphrase (max ~30 words per field). Never copy sentences from Devpost, READMEs or articles.
- Do not record names of team members. Only `team_size`.
- Controlled-vocabulary fields must use exactly the allowed values below. If nothing fits use `other` and explain in `distinctive_notes`.
- Every record needs at least one URL in `sources`.

## Fields

### Identity and outcome
| field | type | notes |
|---|---|---|
| project_id | string | `<hackathon_slug>-<edition>-<project_slug>`, lowercase, hyphens |
| project_name | string | as shown on Devpost |
| hackathon | string | e.g. "HackUTD" |
| hackathon_no | int | number from the master list |
| edition | string | e.g. "HackUTD 2025" |
| event_start / event_end | string or null | ISO dates `YYYY-MM-DD` |
| is_winner | bool | false only for baseline (non-winner) projects |
| prizes | list of objects | `{prize, category_as_awarded, placement}`; placement is "1st"/"2nd"/"3rd"/"unknown"/null |
| placement_tier | enum | `overall_top3`, `overall_other`, `track_winner`, `sponsor_winner`, `honorable_or_finalist`, `baseline_non_winner` |
| n_prizes | int | count of prizes in `prizes` |

### Links
| field | type |
|---|---|
| devpost_url, github_url, demo_video_url, live_demo_url | string or null |
| repo_status | enum: `public`, `private_or_missing`, `dead_link`, `none_listed` |

### Idea
| field | type | notes |
|---|---|---|
| one_line_pitch | string | your paraphrase, <=25 words |
| problem_statement | string | your paraphrase, <=30 words |
| target_user | string | short phrase |
| domain_primary | enum | see Domain list |
| domain_secondary | enum or null | same list |
| idea_type | enum | `new_category`, `twist_on_known_app`, `dev_tool`, `automation_or_agent`, `social_good`, `entertainment_or_game`, `hardware_gadget`, `data_or_analytics`, `creative_tool`, `other` |
| distinctive_notes | string or null | factual, <=40 words, what is unusual about the build or demo |

### Product and tech
| field | type | notes |
|---|---|---|
| platforms | list of enum | `web`, `mobile_ios`, `mobile_android`, `mobile_cross`, `desktop`, `browser_extension`, `cli`, `hardware`, `bot_or_chat`, `other` |
| has_hardware | bool or null | physical device built or used as part of the demo |
| ai_used | bool or null | |
| ai_types | list of enum | `llm_chat`, `agent_or_tool_use`, `rag_or_search`, `vision`, `speech_or_voice`, `recommendation`, `predictive_ml`, `generative_media`, `other` |
| stack_languages, stack_frontend, stack_backend, stack_database, stack_hosting | list of string | as stated in the writeup/repo |
| tech_items | list of objects | one per notable technology/API: `{name, kind, is_sponsor, depth}`. kind: `ai_model`, `cloud`, `database`, `payments`, `maps_geo`, `data_source`, `auth`, `telecom`, `hardware_part`, `framework`, `other`. depth: `core` (product breaks without it), `supporting`, `token` (name-drop / thin use), `unclear` |
| sponsor_apis_used | list of string | sponsor/MLH products used, by name |
| sponsor_fit_note | string or null | for sponsor-track wins: one factual sentence on how the project used what the sponsor offered |

### Execution and demo
| field | type | notes |
|---|---|---|
| has_demo_video | bool or null | |
| has_live_demo | bool or null | a hosted working link was listed |
| live_demo_status | enum | `working`, `broken`, `not_checked`, `none` |
| n_screenshots | int or null | images on the Devpost page |
| ui_polish | enum or null | `low`, `medium`, `high`; judge from screenshots/live demo only, else null |
| repo_commits | int or null | commits seen (300 = history truncated at 300) |
| commits_before_event / commits_in_window / commits_after_event | int or null | counts relative to the event window (event start 00:00 to end 23:59 + 12h, US Central); computed from commit timestamps |
| share_commits_in_window | float or null | commits_in_window / commits seen |
| first_commit, last_commit | string or null | ISO datetime |
| commits_in_event_window | bool or null | true if at least half of the commits seen fall inside the event window; null if unknown |
| readme_quality | enum or null | `none`, `thin`, `solid`, `detailed` |

### Writeup and team
| field | type | notes |
|---|---|---|
| writeup_sections | list of enum | which of: `inspiration`, `what_it_does`, `how_built`, `challenges`, `accomplishments`, `learned`, `next_steps`, `other` |
| writeup_length | enum or null | `short` (<150 words), `medium`, `long` (>500 words) |
| has_impact_claims | bool or null | quantified impact/market numbers stated |
| impact_claims_note | string or null | paraphrase the kind of claim, <=25 words |
| team_size | int or null | |

### Provenance
| field | type | notes |
|---|---|---|
| confidence | enum | `high`, `medium`, `low` |
| unverified_fields | list of string | |
| sources | list of string | URLs actually opened |
| analyzed_at | string | ISO date |

## Domain list (domain_primary / domain_secondary)
`health_wellness`, `mental_health`, `fintech_finance`, `education`, `sustainability_climate`, `accessibility`, `safety_security`, `productivity_workplace`, `dev_tools`, `social_community`, `entertainment_games`, `creative_media`, `retail_consumer`, `food_nutrition`, `mobility_transport`, `telecom_networking`, `housing_real_estate`, `energy_utilities`, `civic_legal`, `ai_agents_infra`, `other`

## Output tabs built later from these records
Projects (one row per project, scalar fields), Prizes (one row per project-prize), Tech_APIs (one row per `tech_items` entry), Project_Notes (free-text fields), Data_Dictionary (this file), Sources (url + confidence per project).


## Version notes
- v1.1: added `energy_utilities` domain; replaced the strict commit-window boolean with before/in/after counts and a share; repo fields are filled by a script that clones each repo, not by agents.
