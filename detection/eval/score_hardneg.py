"""TASK-051: score hardneg_v3.jsonl ONCE (no tuning) with prodrules (thr 0.80) and local (thr 0.95, run with P2_FAILOVER=0). Writes
results/hardneg-v3-<engine>.jsonl (+ prints misfires with the rule chips). Guard: refuses while the live :8100 has active STT sockets.
  P2_FAILOVER=0 LOCAL_LLM_URL=... LOCAL_MODEL=... .venv/bin/python -m detection.eval.score_hardneg"""
import asyncio, json, sys
import httpx
from detection.eval import run_eval as E
from detection import detect as D
PATH = E.EVAL_DIR / "data" / "hardneg_v3.jsonl"
THR = {"prodrules": 0.80, "local": 0.95}

def live():
    try: return int(httpx.get("http://localhost:8100/healthz", timeout=2).json().get("active_stt_sockets", 0))
    except Exception: return 0

async def main():
    if live(): print("live call active: not running"); return 2
    rows = E.load_rows([PATH], split=None); print(len(rows), "rows")
    for eng in ("prodrules", "local"):
        recs = await E.run_engine(eng, rows)
        (E.RESULTS_DIR / f"hardneg-v3-{eng}.jsonl").write_text("".join(json.dumps(r) + "\n" for r in recs))
        fa = [r for r in recs if E.alert_line(r, THR[eng]) is not None]
        print(f"\n{eng} thr={THR[eng]}: false alarms {len(fa)}/{len(recs)}; max s per row: {' '.join(f'{max(p['s'] for p in r['per_line']):.2f}' for r in recs)}")
        for r in fa:
            k = E.alert_line(r, THR[eng]); row = next(x for x in rows if x["id"] == r["id"])
            text = "\n".join(row["caller_lines"][max(0, k - E.WINDOW_LINES):k])
            q = D.quick(text, "local")
            print(f"  {r['id']} [{row['adversarial_kind']}] first >=thr at line {k}: s={r['per_line'][k-1]['s'] if k else '?'} asks={r['per_line'][k-1]['asks']} quick chips={q.get('why_chips')}")
    return 0
sys.exit(asyncio.run(main()))
