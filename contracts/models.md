# P2 engine order (since 02:42 CT 2026-11-08 every real call ran engine=local)
1. **PRIMARY: local Nemotron 3 Nano 4B on the laptop GPU.** Weights `NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf`, served by llama.cpp `llama-server.exe` (Windows CUDA build via WSL interop, `detection/engines/run_local_llm.sh`: `-ngl 99 -c 2048 -np 1 --reasoning off`, port 8101), OpenAI-compatible; model name sent = `nemotron-nano-4b` (`LOCAL_MODEL`), URL `LOCAL_LLM_URL` (WSL gateway :8101). Live runs `P2_ENGINE=local`.
2. **Failover: cloud** `nvidia/nemotron-3.5-lightning-30b-a3b` (table below) when local misses `P2_LOCAL_FIRST_S` (4 s) or its probe fails, within `P2_LOCAL_TIMEOUT_S` (6 s) total; only if the cloud breaker is closed and a key is present.
3. **Floor: deterministic rules** (`detect.quick`, no I/O) always run and only raise s; if both engines fail the result is rules-only, never an exception into P1.
(The cloud-primary order, cloud 2 s then local, is the `P2_ENGINE=cloud` mode used for comparison and acceptance runs.)

# NVIDIA model pins (P2 owns; checked 2026-11-08 ~01:00 CT, eng1)

Endpoint: `$NVIDIA_BASE_URL` (OpenAI-compatible `/chat/completions`), key in `.env` (never commit). `/models` lists 84 ids, but **listed ≠ servable** (some 404 on call).
Probe: one tiny chat call each, 2 plain samples; latency is wall-clock round trip from the dev laptop, so treat as indicative.

| model id | status | p50 ms | JSON mode | thinking | use |
|---|---|---|---|---|---|
| nvidia/nemotron-3.5-lightning-30b-a3b | OK | ~600 (≈290 with thinking off) | `response_format: json_object` OK | thinks by default and can eat max_tokens leaving empty content; **send `chat_template_kwargs: {"enable_thinking": false}`** | **P2 cloud engine (failover when local is primary)** |
| nvidia/nemotron-3.5-bolt-e4b | OK | ~400 | json_object OK | no reasoning | fallback / cheap second opinion |
| nvidia/nemotron-3.5-super-vl-120b-a12b | OK | ~600 (≈490 off) | json_object OK | thinks by default, same kwarg turns it off | verifier candidate (borderline 0.4-0.8) |
| nvidia/nemotron-3-nano-omni-30b-a3b-reasoning | OK | ~2300 plain (≈500 off) | json_object OK | reasoning model, slow unless off | not used |
| nvidia/llama-3.1-nemotron-safety-guard-8b-v3 | OK | 2.8-6.4 s (≈1 s warm) | returns its own `{"User Safety": ...}` | n/a | safety classifier only; too slow for the live path |
| nvidia/nemotron-3-super-120b-a12b | **404** (function not found, still) | n/a | n/a | n/a | unavailable |
| nvidia/nemotron-nano-3-30b-a3b | **404** | n/a | n/a | n/a | unavailable |
| nvidia/nemotron-3.5-content-safety | **404** | n/a | n/a | n/a | unavailable |

Notes
- `nvext.guided_json` is rejected (400 unknown field) on the nemotron-3.5 models; use `response_format: {"type":"json_object"}` plus a schema in the prompt and validate in code.
- Also listed (untested): nemotron-3-ultra-550b-a55b, llama-3.1-nemotron-ultra-253b-v1, -70b-instruct, -51b-instruct, embed models.
- STT: no ASR model is in the nemotron list; STT is chosen by P2 eng2, see detection/DECISIONS.md.
- Rate limits: no `x-ratelimit-*` headers returned. "~40 rpm shared by the whole team key" is reported, unverified. Throttle eval ≤20 rpm and cache.
- P2 cloud engine (failover behind local): **nvidia/nemotron-3.5-lightning-30b-a3b**, thinking off, json_object, temperature 0.1, timeout ~2.5 s.
