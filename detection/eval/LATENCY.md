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

