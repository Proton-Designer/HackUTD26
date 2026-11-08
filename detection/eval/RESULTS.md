# P2 detection evaluation: cloud vs local vs rules-only

**All data is synthetic** (hand-written scam scripts, legit look-alikes, adversarial rows). Small n: read every cell with its interval (Wilson 95%). Thresholds were tuned on split=dev only and frozen before scoring split=test (`FROZEN.json`, git `20ca58a`).

Setup: caller lines replayed one at a time, window = last 5 lines, alert when s >= threshold. 'Rules' = a plain keyword baseline (`rules_score` in run_eval.py), not an LLM. Seconds assume ~3 s of speech per line.

## split = test  (the headline numbers)

| metric | rules (thr 0.85) | local (thr 0.95) |
|---|---|---|
| rows scored / not scored (429 or model failure) | 60 / 0 | 60 / 0 |
| scam recall (all alert-worthy) | 85% (28/33) [69-93] | 100% (33/33) [90-100] |
| adversarial recall | 69% (9/13) [42-87] | 100% (13/13) [77-100] |
| injection-only recall | 86% (6/7) [49-97] | 100% (7/7) [65-100] |
| false alarm, all legit | 19% (5/27) [8-37] | 7% (2/27) [2-23] |
| false alarm, plain legit | 5% (1/20) [1-24] | 0% (0/20) [0-16] |
| false alarm, keyword-bait legit | 57% (4/7) [25-84] | 29% (2/7) [8-64] |
| asks precision | 82% (47/57) [71-90] | 65% (50/77) [54-75] |
| asks recall | 80% (47/59) [68-88] | 85% (50/59) [73-92] |
| lines from first hard ask to alert (mean) | +0.00 (n=28) | -0.54 (n=28) |
| approx seconds late (lines*3s + p50 latency) | +0.0 | -0.0 |
| addresses_ai flag: false positives (scripts that never address the AI) | 0% (0/55) [0-7] | 2% (1/55) [0-10] |
| addresses_ai flag: detected (scripts that do) | 0% (0/5) [0-43] | 100% (5/5) [57-100] |
| windows where the model failed (fell back to rules) | 0/252 | 0/252 |
| /detect latency p50 / p95 / mean (ms) | 0 / 0 / 0 | 1606 / 1896 / 1666 |

Recall by scam type (n per cell; cells with n<5 are anecdotes):

| scam_type | rules | local |
|---|---|---|
| bank_fraud_department | 6/7 | 7/7 |
| charity_donation | 1/1 | 1/1 |
| crypto_investment | 2/2 | 2/2 |
| grandparent_emergency | 1/3 | 3/3 |
| irs_gov_impersonation | 2/3 | 3/3 |
| job_offer | 1/1 | 1/1 |
| lottery_prize | 1/1 | 1/1 |
| medicare_impersonation | 2/2 | 2/2 |
| package_delivery | 2/2 | 2/2 |
| romance_crypto | 2/2 | 2/2 |
| sheriff_warrant | 1/1 | 1/1 |
| tech_support | 4/5 | 5/5 |
| utility_shutoff | 3/3 | 3/3 |

## split = dev  (used for tuning, optimistic)

| metric | rules (thr 0.85) | cloud (thr 0.85) | local (thr 0.95) |
|---|---|---|---|
| rows scored / not scored (429 or model failure) | 60 / 0 | 51 / 9 | 58 / 2 |
| scam recall (all alert-worthy) | 91% (30/33) [76-97] | 93% (28/30) [79-98] | 100% (31/31) [89-100] |
| adversarial recall | 85% (11/13) [58-96] | 100% (10/10) [72-100] | 100% (11/11) [74-100] |
| injection-only recall | 100% (7/7) [65-100] | 100% (7/7) [65-100] | 100% (6/6) [61-100] |
| false alarm, all legit | 26% (7/27) [13-45] | 5% (1/21) [1-23] | 30% (8/27) [16-48] |
| false alarm, plain legit | 15% (3/20) [5-36] | 5% (1/20) [1-24] | 15% (3/20) [5-36] |
| false alarm, keyword-bait legit | 57% (4/7) [25-84] | 0% (0/1) [0-79] | 71% (5/7) [36-92] |
| asks precision | 85% (47/55) [74-92] | 70% (49/70) [58-79] | 33% (50/152) [26-41] |
| asks recall | 87% (47/54) [76-94] | 100% (49/49) [93-100] | 100% (50/50) [93-100] |
| lines from first hard ask to alert (mean) | +0.00 (n=30) | -1.04 (n=25) | -0.89 (n=28) |
| approx seconds late (lines*3s + p50 latency) | +0.0 | -2.2 | -1.0 |
| addresses_ai flag: false positives (scripts that never address the AI) | 0% (0/56) [0-6] | 4% (2/47) [1-14] | 60% (33/55) [47-72] |
| addresses_ai flag: detected (scripts that do) | 0% (0/4) [0-49] | 100% (4/4) [51-100] | 100% (3/3) [44-100] |
| windows where the model failed (fell back to rules) | 0/252 | 0/216 | 0/244 |
| /detect latency p50 / p95 / mean (ms) | 0 / 0 / 0 | 912 / 1588 / 992 | 1700 / 3541 / 2066 |

Recall by scam type (n per cell; cells with n<5 are anecdotes):

| scam_type | rules | cloud | local |
|---|---|---|---|
| bank_fraud_department | 5/5 | 5/5 | 5/5 |
| charity_donation | 1/1 | 1/1 | 1/1 |
| crypto_investment | 1/2 | 2/2 | 2/2 |
| grandparent_emergency | 4/5 | 4/4 | 4/4 |
| irs_gov_impersonation | 3/4 | 4/4 | 4/4 |
| job_offer | 2/2 | 2/2 | 2/2 |
| lottery_prize | 1/1 | 1/1 | 1/1 |
| medicare_impersonation | 3/3 | 2/3 | 3/3 |
| package_delivery | 2/2 | 1/2 | 2/2 |
| romance_crypto | 2/2 | 1/1 | 2/2 |
| sheriff_warrant | 1/1 | 1/1 | 1/1 |
| tech_support | 4/4 | 3/3 | 3/3 |
| utility_shutoff | 1/1 | 1/1 | 1/1 |

## Before vs after TASK-022/023 (split = test, thresholds unchanged)

BEFORE = results/before/ (scored on code at `20ca58a`, prior to AI-address gating, clause negation, request-verb gate, few-shots). AFTER = current trunk `1972d5d`. No retuning; thresholds tuned on dev only. The rules row is the standalone keyword baseline in run_eval.py, so it is identical by construction.

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

**Not scored (no results yet, e.g. NVIDIA key 429):** cloud/test

## Honest caveats

- Scripts are short (4-5 lines) and written by the team, so models see cleaner text than a real STT stream.
- Test n is small; intervals are wide. A 5-point gap between engines is not a finding.
- 'First hard ask' is located by the rules baseline, so delay is relative to that reference, not human labels.
- No audio, no real callers, no real PII anywhere.
- Cloud test is not scored (NVIDIA 429); rows with any model-failure window are excluded and counted as not scored.
