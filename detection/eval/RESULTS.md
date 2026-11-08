# P2 detection evaluation: cloud vs local vs rules-only

**All data is synthetic** (hand-written scam scripts, legit look-alikes, adversarial rows). Small n: read every cell with its interval (Wilson 95%). Thresholds were tuned on split=dev only and frozen before scoring split=test (`FROZEN.json`, git `20ca58a`).

Setup: caller lines replayed one at a time, window = last 5 lines, alert when s >= threshold. 'Rules' = a plain keyword baseline (`rules_score` in run_eval.py), not an LLM; 'prodrules' = the production rule path (`detect.quick`: rule_scan + merge, what runs live when the LLM fails). Seconds assume ~3 s of speech per line.

## split = test  (the headline numbers)

| metric | rules (thr 0.85) | prodrules (thr 0.8) | local (thr 0.95) |
|---|---|---|---|
| rows scored / not scored (429 or model failure) | 60 / 0 | 60 / 0 | 60 / 0 |
| scam recall (all alert-worthy) | 85% (28/33) [69-93] | 73% (24/33) [56-85] | 100% (33/33) [90-100] |
| adversarial recall | 69% (9/13) [42-87] | 62% (8/13) [36-82] | 100% (13/13) [77-100] |
| injection-only recall | 86% (6/7) [49-97] | 86% (6/7) [49-97] | 100% (7/7) [65-100] |
| false alarm, all legit | 19% (5/27) [8-37] | 4% (1/27) [1-18] | 7% (2/27) [2-23] |
| false alarm, plain legit | 5% (1/20) [1-24] | 0% (0/20) [0-16] | 0% (0/20) [0-16] |
| false alarm, keyword-bait legit | 57% (4/7) [25-84] | 14% (1/7) [3-51] | 29% (2/7) [8-64] |
| asks precision | 82% (47/57) [71-90] | 76% (28/37) [60-87] | 65% (50/77) [54-75] |
| asks recall | 80% (47/59) [68-88] | 47% (28/59) [35-60] | 85% (50/59) [73-92] |
| lines from first hard ask to alert (mean) | +0.00 (n=28) | -0.08 (n=24) | -0.54 (n=28) |
| approx seconds late (lines*3s + p50 latency) | +0.0 | -0.2 | -0.0 |
| addresses_ai flag: false positives (scripts that never address the AI) | 0% (0/55) [0-7] | 0% (0/55) [0-7] | 2% (1/55) [0-10] |
| addresses_ai flag: detected (scripts that do) | 0% (0/5) [0-43] | 0% (0/5) [0-43] | 100% (5/5) [57-100] |
| windows where the model failed (fell back to rules) | 0/252 | 0/252 | 0/252 |
| /detect latency p50 / p95 / mean (ms) | 0 / 0 / 0 | 1 / 20 / 4 | 1606 / 1896 / 1666 |

Recall by scam type (n per cell; cells with n<5 are anecdotes):

| scam_type | rules | prodrules | local |
|---|---|---|---|
| bank_fraud_department | 6/7 | 5/7 | 7/7 |
| charity_donation | 1/1 | 1/1 | 1/1 |
| crypto_investment | 2/2 | 1/2 | 2/2 |
| grandparent_emergency | 1/3 | 1/3 | 3/3 |
| irs_gov_impersonation | 2/3 | 2/3 | 3/3 |
| job_offer | 1/1 | 1/1 | 1/1 |
| lottery_prize | 1/1 | 1/1 | 1/1 |
| medicare_impersonation | 2/2 | 2/2 | 2/2 |
| package_delivery | 2/2 | 2/2 | 2/2 |
| romance_crypto | 2/2 | 2/2 | 2/2 |
| sheriff_warrant | 1/1 | 1/1 | 1/1 |
| tech_support | 4/5 | 4/5 | 5/5 |
| utility_shutoff | 3/3 | 1/3 | 3/3 |

## split = dev  (used for tuning, optimistic)

| metric | rules (thr 0.85) | prodrules (thr 0.8) | cloud (thr 0.85) | local (thr 0.95) |
|---|---|---|---|---|
| rows scored / not scored (429 or model failure) | 60 / 0 | 60 / 0 | 51 / 9 | 58 / 2 |
| scam recall (all alert-worthy) | 91% (30/33) [76-97] | 79% (26/33) [62-89] | 93% (28/30) [79-98] | 100% (31/31) [89-100] |
| adversarial recall | 85% (11/13) [58-96] | 77% (10/13) [50-92] | 100% (10/10) [72-100] | 100% (11/11) [74-100] |
| injection-only recall | 100% (7/7) [65-100] | 86% (6/7) [49-97] | 100% (7/7) [65-100] | 100% (6/6) [61-100] |
| false alarm, all legit | 26% (7/27) [13-45] | 0% (0/27) [0-12] | 5% (1/21) [1-23] | 30% (8/27) [16-48] |
| false alarm, plain legit | 15% (3/20) [5-36] | 0% (0/20) [0-16] | 5% (1/20) [1-24] | 15% (3/20) [5-36] |
| false alarm, keyword-bait legit | 57% (4/7) [25-84] | 0% (0/7) [0-35] | 0% (0/1) [0-79] | 71% (5/7) [36-92] |
| asks precision | 85% (47/55) [74-92] | 90% (37/41) [77-96] | 70% (49/70) [58-79] | 33% (50/152) [26-41] |
| asks recall | 87% (47/54) [76-94] | 69% (37/54) [55-79] | 100% (49/49) [93-100] | 100% (50/50) [93-100] |
| lines from first hard ask to alert (mean) | +0.00 (n=30) | +0.04 (n=26) | -1.04 (n=25) | -0.89 (n=28) |
| approx seconds late (lines*3s + p50 latency) | +0.0 | +0.1 | -2.2 | -1.0 |
| addresses_ai flag: false positives (scripts that never address the AI) | 0% (0/56) [0-6] | 0% (0/56) [0-6] | 4% (2/47) [1-14] | 60% (33/55) [47-72] |
| addresses_ai flag: detected (scripts that do) | 0% (0/4) [0-49] | 0% (0/4) [0-49] | 100% (4/4) [51-100] | 100% (3/3) [44-100] |
| windows where the model failed (fell back to rules) | 0/252 | 0/252 | 0/216 | 0/244 |
| /detect latency p50 / p95 / mean (ms) | 0 / 0 / 0 | 0 / 5 / 1 | 912 / 1588 / 992 | 1700 / 3541 / 2066 |

Recall by scam type (n per cell; cells with n<5 are anecdotes):

| scam_type | rules | prodrules | cloud | local |
|---|---|---|---|---|
| bank_fraud_department | 5/5 | 5/5 | 5/5 | 5/5 |
| charity_donation | 1/1 | 0/1 | 1/1 | 1/1 |
| crypto_investment | 1/2 | 1/2 | 2/2 | 2/2 |
| grandparent_emergency | 4/5 | 4/5 | 4/4 | 4/4 |
| irs_gov_impersonation | 3/4 | 3/4 | 4/4 | 4/4 |
| job_offer | 2/2 | 2/2 | 2/2 | 2/2 |
| lottery_prize | 1/1 | 1/1 | 1/1 | 1/1 |
| medicare_impersonation | 3/3 | 3/3 | 2/3 | 3/3 |
| package_delivery | 2/2 | 0/2 | 1/2 | 2/2 |
| romance_crypto | 2/2 | 1/2 | 1/1 | 2/2 |
| sheriff_warrant | 1/1 | 1/1 | 1/1 | 1/1 |
| tech_support | 4/4 | 4/4 | 3/3 | 3/3 |
| utility_shutoff | 1/1 | 1/1 | 1/1 | 1/1 |

## Before vs after TASK-022/023 (split = test, thresholds unchanged)

BEFORE = results/before/ (scored on code at `20ca58a`, prior to AI-address gating, clause negation, request-verb gate, few-shots). AFTER = trunk `1972d5d` (local+rules runs). No retuning; thresholds tuned on dev only. The rules row is the standalone keyword baseline in run_eval.py, so it is identical by construction.

**local** (thr 0.95); rows scored before 60 (not scored 0), after 60 (not scored 0)

| metric | before | after |
|---|---|---|
| scam recall | 100% (33/33) [90-100] | 100% (33/33) [90-100] |
| adversarial recall | 100% (13/13) [77-100] | 100% (13/13) [77-100] |
| false alarm, all legit | 7% (2/27) [2-23] | 7% (2/27) [2-23] |
| false alarm, keyword-bait legit | 29% (2/7) [8-64] | 29% (2/7) [8-64] |
| addresses_ai false positives | 49% (27/55) [36-62] | 2% (1/55) [0-10] |
| asks precision | 36% (56/155) [29-44] | 65% (50/77) [54-75] |
| asks recall | 95% (56/59) [86-98] | 85% (50/59) [73-92] |
| /detect latency p50 (ms) | 2736 | 1606 |

**rules** (thr 0.85); rows scored before 60 (not scored 0), after 60 (not scored 0)

| metric | before | after |
|---|---|---|
| scam recall | 85% (28/33) [69-93] | 85% (28/33) [69-93] |
| adversarial recall | 69% (9/13) [42-87] | 69% (9/13) [42-87] |
| false alarm, all legit | 19% (5/27) [8-37] | 19% (5/27) [8-37] |
| false alarm, keyword-bait legit | 57% (4/7) [25-84] | 57% (4/7) [25-84] |
| addresses_ai false positives | 0% (0/55) [0-7] | 0% (0/55) [0-7] |
| asks precision | 82% (47/57) [71-90] | 82% (47/57) [71-90] |
| asks recall | 80% (47/59) [68-88] | 80% (47/59) [68-88] |
| /detect latency p50 (ms) | 0 | 0 |

## Held-out v2 (40 fresh synthetic rows, scored ONCE, thresholds frozen on dev, no tuning)

File `heldout_v2.jsonl` (written before the engines saw it; not in the default row files). Scored on trunk `ebabe10`. 20 scams (8 no-classic-keywords, 4 Spanish/Spanglish, 4 AI-directed injection, 4 slow-build) + 20 legit (10 keyword-bait, 10 ordinary). n is tiny: read every interval.

| metric | rules (thr 0.85) | prodrules (thr 0.8) | local (thr 0.95) |
|---|---|---|---|
| rows scored / not scored | 40 / 0 | 40 / 0 | 40 / 0 |
| scam recall | 40% (8/20) [22-61] | 45% (9/20) [26-66] | 100% (20/20) [84-100] |
| adversarial recall (injection + Spanish) | 50% (4/8) [22-78] | 62% (5/8) [31-86] | 100% (8/8) [68-100] |
| false alarm, all legit | 30% (6/20) [15-52] | 10% (2/20) [3-30] | 10% (2/20) [3-30] |
| false alarm, keyword-bait legit | 60% (6/10) [31-83] | 20% (2/10) [6-51] | 20% (2/10) [6-51] |
| false alarm, plain legit | 0% (0/10) [0-28] | 0% (0/10) [0-28] | 0% (0/10) [0-28] |
| asks precision | 59% (10/17) [36-78] | 71% (10/14) [45-88] | 59% (22/37) [43-74] |
| asks recall | 36% (10/28) [21-54] | 36% (10/28) [21-54] | 79% (22/28) [60-90] |
| addresses_ai false positives | 0% (0/36) [0-10] | 0% (0/36) [0-10] | 3% (1/36) [0-14] |
| windows fallen back to rules | 0/163 | 0/163 | 0/163 |
| /detect latency p50 (ms) | 0 | 5 | 1620 |

Scam recall by v2 style (alerted / n):

| style | rules | prodrules | local |
|---|---|---|---|
| no_keywords | 0/8 | 1/8 | 8/8 |
| spanish | 0/4 | 1/4 | 4/4 |
| injection | 4/4 | 4/4 | 4/4 |
| slow_build | 4/4 | 3/4 | 4/4 |

**Not scored (no results yet, e.g. NVIDIA key 429):** cloud/test

## Honest caveats

- Scripts are short (4-5 lines) and written by the team, so models see cleaner text than a real STT stream.
- Test n is small; intervals are wide. A 5-point gap between engines is not a finding.
- 'First hard ask' is located by the rules baseline, so delay is relative to that reference, not human labels.
- No audio, no real callers, no real PII anywhere.
- Cloud test is not scored (NVIDIA 429); rows with any model-failure window are excluded and counted as not scored.

## Latency benchmark (no NVIDIA calls; `bench_latency.py`)

P2 on test port 8104, `LOCAL_LLM_URL` -> Windows llama.cpp b12199 CUDA-12.4, Nemotron-3-Nano-4B Q4_K_M, RTX 3050 Ti 4 GB (`-np 1`, one GPU slot). 40 real test-split windows per level, unique ref prefix so the LRU cache is bypassed. "not real-model" counts replies that fell back to another engine (0 everywhere). Rules is the in-process `detect.quick` (the live fallback), 1000 calls; `rules` is not a `/detect` engine.

| path | concurrency | n | p50 ms | p95 ms | mean ms | req/s | not real-model |
|---|---|---|---|---|---|---|---|
| rules (detect.quick, in-process) | 1 | 1000 | 1.92 | 22.49 | 5.94 | n/a | 0 |
| local /detect (Nemotron 4B Q4_K_M, RTX 3050 Ti) | 1 | 40 | 1660 | 1820 | 1663 | 0.60 | 0 |
| local /detect (Nemotron 4B Q4_K_M, RTX 3050 Ti) | 2 | 40 | 3218 | 4037 | 3340 | 0.59 | 0 |
| local /detect (Nemotron 4B Q4_K_M, RTX 3050 Ti) | 4 | 40 | 4022 | 4082 | 3947 | 0.99 | 0 |

Reading: local is serial on one GPU slot, so p50 scales with concurrency (about 1.7 s alone, 3.2 s at 2, 4.0 s at 4; p95 at 4 is right at detect's 4 s timeout). Throughput stays about 0.6 to 1 request/s, so two simultaneous live calls degrade each other when local is the active engine.

End-to-end 'caller endpoint -> risk.update', read from `logs/p2.log` with `call_report.py` (only 3 usable utterances; these were live, unscripted tests, anecdotes not a benchmark):

| path | endpoint -> risk.update |
|---|---|
| cloud answered | 1.9 s |
| cloud 429, failover to local | 3.4 s and 2.2 s |

Also in those logs: STT final transcript arrives 0.25 to 0.71 s after the endpoint. A held-out cloud probe through `/detect` took 0.9 s (one call, 200).

