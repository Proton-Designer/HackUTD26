"""TASK-011: do two simultaneous calls degrade each other? Streams the cached synthetic IRS call (detection/testdata/acc/irs.wav)
alone, then twice at once (different call_ids) against a local P2 (:8191), and prints per-utterance final-transcript latency
(end of speech -> transcript.caller final) and end-of-speech -> risk.update, solo vs concurrent. Real NVIDIA STT/LLM calls."""
import asyncio, statistics, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from detection.scripts.acceptance import Loop, ensure_wavs, utt_ends

def lat(L, cid, t0, ends):
    fin = [e["_t"] for e in L.ev(cid, "transcript.caller") if e["data"].get("is_final", True)]
    ru = [e["_t"] for e in L.ev(cid, "risk.update")]
    f = [fin[i] - (t0 + ends[i]) for i in range(min(len(fin), len(ends)))]
    r = []
    for i in range(min(len(fin), len(ends))):
        nxt = [t for t in ru if t >= fin[i]]
        if nxt: r.append(nxt[0] - (t0 + ends[i]))
    return f, r

async def main():
    wav = ensure_wavs()["irs"]; ends = utt_ends(wav)
    ids = ["cc_solo", "cc_a", "cc_b"]
    L = Loop("cloud", ids); await L.start()
    try:
        t_solo = await L.run_call("cc_solo", wav)
        ta, tb = await asyncio.gather(L.run_call("cc_a", wav), L.run_call("cc_b", wav))
    finally:
        await L.stop()
    rows = [("solo", *lat(L, "cc_solo", t_solo, ends)), ("A (2 concurrent)", *lat(L, "cc_a", ta, ends)), ("B (2 concurrent)", *lat(L, "cc_b", tb, ends))]
    print(f"{'call':18} {'final latency per utt (s)':32} {'risk.update latency per utt (s)'}")
    for n, f, r in rows: print(f"{n:18} {' '.join(f'{x:5.2f}' for x in f):32} {' '.join(f'{x:5.2f}' for x in r)}")
    solo_f, conc_f = statistics.mean(rows[0][1] or [0]), statistics.mean([x for _, f, _ in rows[1:] for x in f] or [0])
    print(f"mean final latency solo {solo_f:.2f}s vs concurrent {conc_f:.2f}s (delta {conc_f - solo_f:+.2f}s)")
    print("FAIL: a concurrent call got no transcripts" if not (rows[1][1] and rows[2][1]) else "OK: both concurrent calls produced finals")
    sys.exit(0 if rows[1][1] and rows[2][1] else 1)
asyncio.run(main())
