"""TASK-034 B: /detect latency benchmark (no NVIDIA calls). Run a P2 on a test port first:
  LOCAL_LLM_URL=http://172.21.192.1:8101 .venv/bin/uvicorn detection.app:app --port 8104
  .venv/bin/python -m detection.eval.bench_latency --port 8104 --n 40
Windows come from the eval rows (last 5 lines at each step); a unique ref prefix defeats detect's LRU cache so every request is a real call.
Prints a markdown table. engine=rules is not a /detect engine, so rules = in-process detect.quick (the live fallback path)."""
import argparse
import asyncio
import statistics
import time

import httpx

from .run_eval import WINDOW_LINES, load_rows


def windows(n: int) -> list[str]:
    out = []
    for r in load_rows(split="test"):
        L = r["caller_lines"]
        for k in range(1, len(L) + 1):
            out.append("\n".join(L[max(0, k - WINDOW_LINES):k]))
    return out[:n]


def q(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(round(p * (len(xs) - 1))))]


async def run_level(url: str, engine: str, conc: int, wins: list[str], tag: str) -> dict:
    lat, bad = [], 0
    it = iter(enumerate(wins))
    async with httpx.AsyncClient(timeout=15) as c:
        async def worker():
            nonlocal bad
            for i, w in it:
                t0 = time.perf_counter()
                try:
                    r = await c.post(url, json={"call_id": f"bench_{tag}", "window_text": f"[ref {tag}-{conc}-{i}] {w}", "metadata": {}, "engine": engine})
                    d = r.json()
                    if r.status_code != 200 or d.get("engine") != engine:
                        bad += 1   # fell back to another engine = not a real model answer
                except Exception:
                    bad += 1
                lat.append((time.perf_counter() - t0) * 1000)
        t0 = time.perf_counter()
        await asyncio.gather(*[worker() for _ in range(conc)])
        wall = time.perf_counter() - t0
    return {"conc": conc, "n": len(lat), "p50": statistics.median(lat), "p95": q(lat, 0.95), "mean": statistics.mean(lat),
            "bad": bad, "rps": len(lat) / wall}


async def main(a):
    wins = windows(a.n)
    url = f"http://127.0.0.1:{a.port}/detect"
    tag = str(int(time.time()) % 100000)
    from detection.detect import quick
    ts = []
    for w in wins * 25:
        t0 = time.perf_counter(); quick(w, "cloud"); ts.append((time.perf_counter() - t0) * 1000)
    print("| path | concurrency | n | p50 ms | p95 ms | mean ms | req/s | not real-model |")
    print("|---|---|---|---|---|---|---|---|")
    print(f"| rules (detect.quick, in-process) | 1 | {len(ts)} | {statistics.median(ts):.2f} | {q(ts, .95):.2f} | {statistics.mean(ts):.2f} | n/a | 0 |")
    for conc in (1, 2, 4):
        m = await run_level(url, "local", conc, wins, tag)
        print(f"| local /detect (Nemotron 4B Q4_K_M, RTX 3050 Ti) | {conc} | {m['n']} | {m['p50']:.0f} | {m['p95']:.0f} | {m['mean']:.0f} | {m['rps']:.2f} | {m['bad']} |")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8104)
    ap.add_argument("--n", type=int, default=40)
    asyncio.run(main(ap.parse_args()))
