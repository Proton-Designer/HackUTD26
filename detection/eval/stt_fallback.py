"""TASK-049: Riva-failure -> Whisper acceptance, in process, real WhisperSTT + the real stt.RivaSTT.transcribe / FallbackSTT code (only Riva's network call is faked).
  python -m detection.eval.stt_fallback failure [--wav W] [--n 6] [--out table.md]     failure modes: resource_exhausted (429), unavailable, hang
  python -m detection.eval.stt_fallback cards  [--variants p28] [--cards ...]            pstn_cards.py with STT=whisper on private ports (hub 8290, P2 8294)
No transcript text is printed or saved by `failure`."""
import argparse, asyncio, os, sys, time, wave
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

def utterances(wav, n):
    from detection.stream import Segmenter
    w = wave.open(wav); pcm = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2"); seg, out = Segmenter(), []
    for i in range(0, len(pcm) - 159, 160): out += seg.feed(pcm[i:i + 160])
    out += seg.flush()
    return out[:n]

def fake_riva(mode):
    from detection import stt
    class Fake(stt.RivaSTT):
        def __init__(self): pass
        def _run(self, pcm):
            if mode == "hang": time.sleep(60); return ""          # thread stays stuck after wait_for gives up (the real failure shape)
            raise RuntimeError({"resource_exhausted": "<_InactiveRpcError StatusCode.RESOURCE_EXHAUSTED 429 rate limit exceeded>",
                                "unavailable": "<_InactiveRpcError StatusCode.UNAVAILABLE failed to connect>"}[mode])
    return Fake()

async def failure(a):
    from detection import stt
    utts = utterances(a.wav, a.n); assert utts, "no utterances in wav"
    rows = []
    wh = stt.WhisperSTT(); t = time.perf_counter(); await wh.transcribe(utts[0]); base = time.perf_counter() - t   # warm
    ts = []
    for u in utts:
        t = time.perf_counter(); await wh.transcribe(u); ts.append(time.perf_counter() - t)
    for mode in ("resource_exhausted", "unavailable", "hang"):
        for warm in (True, False):
            os.environ["P2_STT_TIMEOUT"] = "6"
            fb = stt.FallbackSTT(fake_riva(mode), preload=False, whisper_factory=(lambda: wh) if warm else stt.WhisperSTT)
            if warm: fb._fb = wh
            res = []
            for i, u in enumerate(utts):
                t = time.perf_counter(); txt = await fb.transcribe(u); dt = time.perf_counter() - t
                res.append((i + 1, round(dt, 2), bool(txt.strip()), fb.fails, fb.bypassing))
            rows.append((mode, "warm" if warm else "cold", res))
    lines = ["| failure | whisper | per-utterance seconds (u1..uN) | text returned | fails after | bypass engaged after u2 |", "|---|---|---|---|---|---|"]
    for mode, w, res in rows:
        lines.append(f"| {mode} | {w} | {' / '.join(str(r[1]) for r in res)} | {sum(r[2] for r in res)}/{len(res)} | {res[-1][3]} | {res[1][4]} |")
    lines.append(f"\nWhisper base.en alone on this CPU: p50 {sorted(ts)[len(ts)//2]:.2f} s, max {max(ts):.2f} s per utterance ({len(ts)} utterances, first warm call {base:.2f} s).")
    out = "\n".join(lines); print(out)
    if a.out: Path(a.out).write_text(out + "\n")

def cards(a):
    from detection.scripts import acceptance, pstn_cards
    acceptance.HUB, acceptance.P2 = 8290, 8294          # private ports: eng2 runs the same harness on 8190/8191
    ns = argparse.Namespace(variants=a.variants, cards=a.cards, stt="whisper", resume=a.resume, json=a.json)
    asyncio.run(pstn_cards.main(ns))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("failure"); f.add_argument("--wav", default=str(ROOT / "detection/testdata/pstn/s1_p28.wav")); f.add_argument("--n", type=int, default=6); f.add_argument("--out")
    c = sub.add_parser("cards"); c.add_argument("--variants", default="p28"); c.add_argument("--cards", default=""); c.add_argument("--resume", action="store_true"); c.add_argument("--json", default="stt_whisper_rows.json")
    a = ap.parse_args()
    asyncio.run(failure(a)) if a.cmd == "failure" else cards(a)
