# PSTN-quality judge script cards (TASK-043)
All audio is SYNTHETIC (Magpie TTS "Mia", fictional scripts from data/script-cards.md; the 3 benign scripts b1-b3 are ours). Measured 2026-11-08 ~03:50-04:45 CT, P2 on :8102, `P2_ENGINE=local` (live config, llama on :8101), real Riva Parakeet STT, post-TASK-047 code (on_final off the STT worker). One call at a time, no live call open (socket guard).

## How the audio was degraded (`detection/scripts/pstn_cards.py`, unit tests in tests/test_pstn_degrade.py)
300-3400 Hz band-pass (FFT, soft skirts) -> active-speech RMS set to the level -> band-limited noise at 25 dB SNR -> 8 kHz mu-law (done by the streamer). Variants: **p20** = -20 dBFS speech RMS, **p28** = -28 dBFS, **fast** = 1.2x speed (crude resample, so pitch rises too) at -28 dBFS. Each card = lines 1-5 + payment step (card 2 also the Zelle step), 1.2 s gaps, as a judge would read it.
Columns: *words matched* = share of the card's reference words (lines 1-5) found in the concatenated Riva finals (not a true WER; numbers/wallet strings are the usual misses). *alert* = `alert.fired` time minus the end of the first line whose text trips the rule scan (negative = fired before the judge finished that line). *final latency* = first final arriving after each line ends, averaged per call. *finals/lines* above 1.0 = Riva endpoint split a line at a pause (harmless).

## Result
- **Scam cards: 28 of 28 rows alerted** (cards 1-10; p20/p28/fast for 1-7, p20 for 8, p28/fast for 8-10), max s 1.00. Every alert fired **before** the first ask line ended (latest: -0.22 s, card 2 where the first ask is the OTP request in line 3; most fire 1-14 s earlier, from the threat/impersonation lines).
- **Benign: 9 of 9 rows no alert** (b1 legit bank notice, b2 pharmacy, b3 friend chat; p20/p28/fast). Highest score 0.55 (b1 at -20 dBFS: bank script mentioning codes/"call back"), under the 0.80 alert threshold.
- **Transcription:** words matched median 97%, min 93% (card 1 and card 9 fast). The fast variant costs 0-4 points.
- **Final latency: median 0.97 s, max 2.3 s** after the line ends (one slow row, card 2 fast). Compare eng3's Whisper-fallback measurement on the same cards: p50 1.6 s (STT_FALLBACK.md). Riva is ~0.6 s faster here, mostly because TASK-047 stopped the STT worker waiting for detect().
- No fixes were needed: no VAD endpointing failure on phone audio and no rules miss from STT mishearings in this set (so no changes to rules or thresholds; thresholds untouched).

## Not done / caveats
- Whisper pass (P2_STT=whisper) NOT run (eng3's STT_FALLBACK.md covers the fallback on these cards). The -38 dBFS stress variant (q38) is implemented but NOT run. Cards 9 and 10 have no p20 row, card 8 has no p28/fast overlap issues but only p20+p28+fast across two files; rows missing: s9 p20, s10 p20 (total 37 of 39 planned).
- Synthetic TTS voice with a synthetic channel, not a real handset/PSTN leg; the one real PSTN call measured earlier (a99a2060) was only 2 words. Real judge accents, echo and cross-talk are untested.
- Rules-on-mishearing ("Irs", "6th digit") were not stress-tested separately because every card alerted anyway.

## Rows
| card | stt | variant | words matched | finals/lines | max s | alert vs first-ask line end (s) | final latency (s) | ask line |
|---|---|---|---|---|---|---|---|---|
| s1 IRS Gift Card | riva | p20 | 96% | 7/6 | 1.00 | -13.02 | 1.23 | 4 |
| s1 IRS Gift Card | riva | p28 | 96% | 7/6 | 1.00 | -13.99 | 1.09 | 4 |
| s1 IRS Gift Card | riva | fast | 93% | 6/6 | 1.00 | -13.15 | 1.02 | 4 |
| s2 Bank Fraud Department | riva | p20 | 96% | 8/7 | 1.00 | -0.34 | 0.95 | 3 |
| s2 Bank Fraud Department | riva | p28 | 96% | 8/7 | 1.00 | -0.22 | 0.92 | 3 |
| s2 Bank Fraud Department | riva | fast | 96% | 7/7 | 1.00 | -0.41 | 2.31 | 3 |
| s3 Crypto Investment | riva | p20 | 96% | 7/6 | 1.00 | -5.55 | 0.93 | 5 |
| s3 Crypto Investment | riva | p28 | 96% | 7/6 | 1.00 | -8.21 | 1.04 | 5 |
| s3 Crypto Investment | riva | fast | 96% | 6/6 | 1.00 | -7.20 | 1.02 | 5 |
| s4 Tech Support | riva | p20 | 97% | 7/6 | 1.00 | -2.75 | 0.89 | 3 |
| s4 Tech Support | riva | p28 | 97% | 7/6 | 1.00 | -5.14 | 0.88 | 3 |
| s4 Tech Support | riva | fast | 97% | 6/6 | 1.00 | -4.25 | 0.94 | 3 |
| s5 Grandchild Emergency | riva | p20 | 97% | 7/6 | 1.00 | -3.55 | 0.99 | 5 |
| s5 Grandchild Emergency | riva | p28 | 97% | 7/6 | 1.00 | -5.54 | 0.90 | 5 |
| s5 Grandchild Emergency | riva | fast | 97% | 6/6 | 1.00 | -4.63 | 0.92 | 5 |
| s6 Utility Shutoff | riva | p20 | 97% | 7/6 | 1.00 | -2.24 | 0.99 | 4 |
| s6 Utility Shutoff | riva | p28 | 97% | 7/6 | 1.00 | -5.04 | 0.99 | 4 |
| s6 Utility Shutoff | riva | fast | 95% | 6/6 | 1.00 | -4.30 | 0.98 | 4 |
| s7 Medicare | riva | p20 | 99% | 7/6 | 1.00 | -0.98 | 0.97 | 3 |
| s7 Medicare | riva | p28 | 99% | 7/6 | 1.00 | -1.02 | 0.96 | 3 |
| s7 Medicare | riva | fast | 100% | 6/6 | 1.00 | -0.42 | 0.94 | 3 |
| s8 Package Delivery | riva | p20 | 99% | 7/6 | 1.00 | -1.63 | 1.02 | 3 |
| s8 Package Delivery | riva | p28 | 99% | 7/6 | 1.00 | -1.64 | 0.92 | 3 |
| s8 Package Delivery | riva | fast | 99% | 6/6 | 1.00 | -1.14 | 1.21 | 3 |
| s9 Job Offer | riva | p28 | 94% | 7/6 | 1.00 | -9.18 | 0.89 | 5 |
| s9 Job Offer | riva | fast | 93% | 6/6 | 1.00 | -7.35 | 1.13 | 5 |
| s10 Romance Crypto | riva | p28 | 97% | 7/6 | 1.00 | -1.50 | 0.85 | 5 |
| s10 Romance Crypto | riva | fast | 96% | 6/6 | 1.00 | -0.89 | 0.88 | 5 |
| b1 Legit bank notice | riva | p20 | 98% | 3/3 | 0.55 | NO ALERT | 1.08 | - |
| b1 Legit bank notice | riva | p28 | 100% | 3/3 | 0.05 | NO ALERT | 0.95 | - |
| b1 Legit bank notice | riva | fast | 100% | 3/3 | 0.05 | NO ALERT | 1.01 | - |
| b2 Pharmacy pickup | riva | p20 | 100% | 3/3 | 0.05 | NO ALERT | 0.98 | - |
| b2 Pharmacy pickup | riva | p28 | 100% | 3/3 | 0.05 | NO ALERT | 0.90 | - |
| b2 Pharmacy pickup | riva | fast | 100% | 3/3 | 0.05 | NO ALERT | 0.88 | - |
| b3 Friend chat | riva | p20 | 100% | 3/3 | 0.05 | NO ALERT | 1.01 | - |
| b3 Friend chat | riva | p28 | 100% | 3/3 | 0.05 | NO ALERT | 1.00 | - |
| b3 Friend chat | riva | fast | 100% | 3/3 | 0.05 | NO ALERT | 0.96 | - |

scam rows: 28, alerted: 28; benign rows: 9, false alarms: 0 (max s 0.55)
