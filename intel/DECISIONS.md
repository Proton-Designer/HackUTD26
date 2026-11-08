# intel/ decisions (P4a)

## Lookups
- Lookups are plain functions with a CLI: fast to test, and the agent calls them as read-only tools.
- RDAP via rdap.org (one public endpoint, redirects to the right registry, no key).
- BTC via blockstream.info (total received + tx count, no key). ETH via eth.blockscout.com (balance + tx count; no free "total received"). Demo wallet should be BTC.
- Fail open: network errors/timeouts return status "unavailable" and still emit an event. Never raises.
- Lookups run in parallel (one timeout worst case, not the sum) and hosts are env-overridable (INTEL_RDAP_BASE,
  INTEL_BTC_BASE, INTEL_ETH_BASE) for drills or a mirror on stage. Drill (2026-11-08, live Nemotron, P1 hub in-process):
  dead DNS and blackholed hosts both -> lookups "unavailable", gate still 7/7; worst case 10.9 s (6 s timeout + LLM).
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

## Capital One Nessie (mock bank) - confirmed against the live API 2026-11-08
- Base https://api.nessieisreal.com (HTTP port 80 refuses connections, so the http:// default was changed to https). Auth ?key= on every request. The docs page is a JS app and /swagger and /api-docs return 403, so paths and payloads were confirmed with a throwaway probe (clearly fake names).
- Confirmed: POST /customers {first_name,last_name,address{street_number,street_name,city,state,zip}}; POST /customers/{id}/accounts {type:"Checking",nickname,rewards,balance}; POST /merchants {name, category (a string, not a list), address, geocode{lat,lng}}; POST /accounts/{id}/deposits {medium,transaction_date,status,amount,description}; POST /accounts/{id}/purchases {merchant_id,medium,purchase_date,amount,status,description}.
- Transfers: POST /accounts/{payer}/transfers?payee_id=<payee> with body {transaction_date,status,amount,description}. medium/payee_id in the BODY are rejected ("extra fields not permitted"). GET /accounts/{id}/transfers[?type=payer] lists that account's transfers (404 "No transfers found" when empty). Responses carry NO payer/payee fields, and ?type=payee returns 404 even for a transfer created with payee_id. So: her pending transfer is matched by the description her banking app wrote ("Zelle to <handle>"), and bank-wide evidence uses the transfer ids the seed recorded.
- GET/PUT/DELETE /transfers/{id}: PUT {"status":"cancelled"} -> 202, and PUT {"status":"pending"} restores it. So hold_transfer = PUT cancelled (DELETE only if PUT is rejected) and the undo token restores pending. DELETE works on transfers/deposits/accounts; customers, merchants and purchases can't be deleted (403). Two empty "Probe Fake" customers and one "Probe Grocer (fake)" merchant from the probe remain in the sandbox.
- Amounts are stored as integers (12.5 -> 12), so all seeded amounts are whole dollars.
- Enterprise (read-only): /enterprise/{customers,accounts,transfers}/{id} answer in ~0.3 s. The /enterprise/* LIST endpoints return the whole shared sandbox (>1 MB) and time out, so they're never used. payee_activity = GET /enterprise/accounts/{payee} + GET /enterprise/transfers/{id} for each seeded evidence transfer (completed ones counted).
- Fail open: 5 s timeout (NESSIE_TIMEOUT), never raises, status "unavailable". The /demo/reset hook deletes leftover pending demo transfers (so rehearsals always have exactly ONE pending) and then POSTs one; 3 s timeouts, skipped silently with no key, no seed or any error (measured: reset 0.2-1.1 s; worst case with Nessie blackholed ~3 s, reset still succeeds).
- Trust: the scammer's captured value is matched in OUR code (normalized payment_handle rail:id, or bank hash/last4) against intel/demo_config.json payout_destination. Transfer ids come only from the Nessie lookup on her own account; the LLM never sees or supplies them (lookup events carry counts, not ids). hold_transfer needs target_source "nessie:pending_transfer" and flag_payee_bankwide needs "nessie:payee"; anything else (LLM, instruction_to_ai) is denied. An allowlisted payout destination (email-handle domain or phone) -> not actioned + attempted_poisoning. legit=true calls never run intel.
- hold_transfer: auto, scope her, simulated=true (sandbox), status applied, undo token "hold-..." (via POST /intel/blocklist/{token}/undo or intel.api.undo_block). If the PUT fails after a successful lookup, no action is shown as applied (logged as skipped). flag_payee_bankwide: queued, analyst Approve, simulated payload simulated/bank-payee-flag/v0.
- Mock bank ids live in intel/nessie_ids.json (committed, so every machine with the key shares one mock bank). The scammer's handle appears in Nessie only as the description of Maria's own scripted transfer, as her banking app would write it.
- Security (#54, P1 review): the gate no longer trusts a proposal's target_source alone. hold_transfer needs target_source "nessie:pending_transfer" AND the id in ctx.bank_transfer_ids (filled only from the Nessie lookup on her account); flag_payee_bankwide needs "nessie:payee" AND the payout key in ctx.bank_payees. LLM proposals are re-stamped target_source "llm" (claimed value kept as llm_claimed_source) and lose gate-trusted fields (destination, destination_allow_key, payee_account_id, amount, proposer, rail). Nessie ids must match ^[0-9a-fA-F-]{24,36}$ before they reach any URL path.

## Laundering chain + network map (2026-11-08)
- Model: 7 synthetic victims each send ONE completed transfer into the existing "SIMULATED ScammerDestination" payee,
  which is now the MULE ($18,100 in). The mule then makes 3 completed transfers to a new "SIMULATED CashOut" account
  ($17,300 out). Maria is role "target"; her $1,800 edge is the one Backfire cuts. All synthetic, whole dollars.
- Edges are RECORDED, not discovered: Nessie transfer reads return no payer/payee and ?type=payee 404s, and the
  /enterprise list endpoints dump the whole shared sandbox and time out. seed_nessie writes ids["chain"] = {nodes, edges}
  (edge = src/dst account + transfer_id + amount + date). GET /intel/chain only CONFIRMS each recorded edge by id via
  GET /enterprise/transfers/{id} (parallel, cached 60 s since completed transfers don't change).
- Maria's edge has no fixed transfer id (a new pending transfer is created at every /demo/reset), so it's resolved live:
  held = an active hold in the intel store (this reset) whose transfer reads "cancelled" in Nessie (nessie.transfer_status).
  Her pending or held $1,800 never counts toward the mule's total_in (it hasn't arrived, and with Backfire it never does).
- Additive: seed_chain() extends an existing seed (Maria, mule, her pending flow and the original 3 evidence transfers are
  untouched); evidence_transfer_ids grows to all 7 victims, so flag_payee_bankwide evidence now says 7 customers / $18,100.
  payee_activity reads run in parallel to keep the hold path fast.
- Fail open: Nessie down -> seeded edge values, status "unavailable"; the endpoint never raises.
- /intel/map: a standalone page I own (intel/chain_map.html), not part of P4b's command center. Self-contained HTML +
  inline SVG + vanilla JS, fetches only same-origin `chain` every 3 s, with a paste-JSON fallback. Both routes sit under
  P1's intel guard (paired device / localhost / HUB_TOKEN), so over the public tunnel they need P1 to allow them.
