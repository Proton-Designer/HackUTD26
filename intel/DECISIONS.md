# intel/ decisions (P4a)

## Lookups
- Lookups are plain functions with a CLI: fast to test, and the agent calls them as read-only tools.
- RDAP via rdap.org (one public endpoint, redirects to the right registry, no key).
- BTC via blockstream.info (total received + tx count, no key). ETH via eth.blockscout.com (balance + tx count; no free "total received"). Demo wallet should be BTC.
- Fail open: network errors/timeouts return status "unavailable" and still emit an event. Never raises.
- Allowlist: seeded JSON of published bank/agency numbers and domains, marked seed data.

## Agent
- Fixed chain, not free tool-calling: plan -> lookups -> campaign link -> ONE Nemotron 3 Super call -> gate. Chose this because multi-step free agents compound errors (95%/step over 10 steps is about 60%) and the free endpoint's tool calling is unverified. The trace is still multi-step and visible (intel.plan, intel.lookup, campaign.updated, intel.agent, intel.proposals, intel.action).
- Nemotron sees only typed artifacts + lookup results + the network-provided calling number. Never scammer_transcript, never instruction_to_ai text.
- Coverage floor: after a successful Nemotron call, any baseline action (same kind + target) the model omitted is appended with proposer "baseline rule" and counted in intel.agent.n_baseline_added. Chose this because in live runs Super sometimes skipped network_number_block, which is the demo's Approve moment; the model still plans, ranks and explains, and the gate still decides.
- Strict JSON, one retry on invalid output, then a deterministic fallback with the same action kinds (engine: "fallback") so the demo never breaks.
- Model from INTEL_MODEL, default nvidia/nemotron-3.5-super-vl-120b-a12b. Chose it because nvidia/nemotron-3-super-120b-a12b shows in /v1/models but chat returns 404 "Function not found for account"; 3.5 Super VL is the same Super 120B-A12B class and answers. Thinking disabled via chat_template_kwargs; auto-retries without it if the endpoint rejects the flag. Fallback option: nvidia/nemotron-3-ultra-550b-a55b (also live).

## Gate (pure code)
- AUTO: block the caller for her (target must be the network calling number), link campaign (+ campaign-scope pre-ring blocking of all its calling numbers once confirmed), Callback Protection warning (only once the campaign is confirmed; otherwise "held").
- QUEUED (simulated, CAMARA-style payloads): network number block, DNS block + registrar report, exchange freeze request, FTC/IC3 packet. Only if the target is corroborated (network calling number, or the campaign is confirmed); otherwise denied.
- DENIED: trust-increasing kinds (mark safe, add trusted contact, unblock, allowlist add) requested from untrusted input; unknown kinds; targets not in evidence.
- NOT ACTIONED: any allowlist match -> attempted_poisoning, emitted as injection.denied with attempted_poisoning=true.
- Scammer instructions aimed at the AI travel as an `instruction_to_ai` artifact (from P3's extractor) and are turned into attempted actions so the gate visibly denies them. Needs Evan's extractor to emit {type: instruction_to_ai, text, target}.

## Campaigns
- Link only via shared strong indicator (wallet, callback phone, domain, payment handle, bank hash) or script-tag Jaccard >= 0.8 with the same stage sequence. Calling number alone never merges.
- Confirmed = >= 2 independent sightings. Demo independence = distinct (calling number, carrier, day); production should require different carriers AND different days.
- Allowlisted values are excluded from campaign indicators, so a poisoning attempt is recorded (poisoning_attempt_seen) but cannot link or block anything.

## Store / ownership (agree with Ayman)
- SQLite at INTEL_DB (default intel/intel.db). P1's /routing/lookup should call `intel.store.is_blocked(number)` or GET /intel/blocked?number= rather than read tables. Single demo customer: scope "her" = Maria.
- P1 mounts `intel.api.router` and calls `intel.api.configure(emit=<bus publish fn>)`. /intel/ingest needs `calling_number` added by P1 (optional field today).
