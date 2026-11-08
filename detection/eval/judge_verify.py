"""#147 judge-bucket verification driver (eval tool, not runtime). Phone-quality synthetic TTS (pstn_cards.build, -28 dBFS, band-pass, noise),
streamed one call at a time through a scratch hub+P2 (acceptance.Loop: temp hub DB, P2_ENGINE=local, never the live hub). Socket guard on :8100.
Usage: ACC_HUB_PORT=8190 ACC_P2_PORT=8102 python -m detection.eval.judge_verify OUT.json MODE [cards] [voices]
  MODE demo     : the trimmed Judge/demo card, full call
  MODE greeting : first line only (then silence) for each card
  MODE full     : the full card (lines + payment step)
  MODE para     : paraphrase pass = the card minus its key cue line (index given as card:idx, e.g. 3:2)
"""
import asyncio, json, os, sys, time
from pathlib import Path
from detection.scripts import pstn_cards as P
from detection.scripts.acceptance import Loop
ROOT = P.ROOT
DEMO = ["Hi, this is the fraud team at your bank. Someone's draining your account right now. To protect your savings, you need to move them to a safe account. And don't tell anyone at the branch.",
        "Our secure line is 1-888-555-0123, and the transfer portal is backfire-demo dot example.",
        "Open your banking app and send the $1,800 by Zelle to refunds dot dept at backfire dash demo dot example. That's the safe account."]
def load_cards():
    md = (ROOT / "data/script-cards-v3-bank.md").read_text()
    return {k: v for k, v in P.parse_cards(md).items()}
async def main():
    out, mode = sys.argv[1], sys.argv[2]
    cards = load_cards(); cards["demo"] = ("Judge demo card (trimmed)", DEMO)
    sel = sys.argv[3].split(",") if len(sys.argv) > 3 and sys.argv[3] else (["demo"] if mode == "demo" else [str(i) for i in (1, 2, 4, 5, 6, 7, 8, 10)] + ["demo"])
    voices = sys.argv[4].split(",") if len(sys.argv) > 4 else ["Mia", "Jason"]
    jobs = []
    for v in voices:
        for c in sel:
            key, _, idx = c.partition(":")
            title, lines = cards[key]
            if mode == "greeting": L1 = lines[:1]
            elif mode == "para": L1 = [l for i, l in enumerate(lines) if i != int(idx)]
            else: L1 = lines
            jobs.append((key + (":" + idx if idx else ""), v, title, L1, lines))
    L = Loop("local", [f"jv{i}" + "r" * k for i in range(len(jobs)) for k in range(3)]); await L.start()
    rows = []
    try:
        for i, (key, voice, title, L1, full) in enumerate(jobs):
            P.VOICE = voice; P.wait_idle()
            pcm, spans = P.build(L1, -28.0, 1.0)
            p = Path(os.environ.get("JV_TMP", "/tmp")) / f"jv_{mode}_{key.replace(':','_')}_{voice}.wav"
            import wave
            w = wave.open(str(p), "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(8000); w.writeframes(pcm.tobytes()); w.close()
            cid = f"jv{i}"; P.wait_idle()
            t0, paused = await P.guarded_call(L, cid, str(p))
            # events are read from the scratch P2's own log (exact alert/risk/final times), not from the hub websocket
            import re, datetime
            day = datetime.date.fromtimestamp(t0); txt = L.log.name; L.log.flush()
            def ts(h): return datetime.datetime.combine(day, datetime.time.fromisoformat(h)).timestamp() - t0
            lines_ = [l for l in open(txt, errors="replace") if re.search(rf"(call=|\s){cid}(\s|-u)", l)]
            al = [ts(l.split()[0]) for l in lines_ if "alert.fired" in l]
            ru = [{"data": {"s": float(re.search(r"s=([0-9.]+)", l).group(1))}} for l in lines_ if "p2.alert risk.update" in l]
            fin = [{"data": {"text": re.search(r"u\d+: [0-9.]+s after endpoint: .(.*)", l).group(1)}} for l in lines_ if "p2.stream stt final" in l]
            first = al[0] if al else None
            def which(t):
                for j, (a, b) in enumerate(spans):
                    if t <= b + P.SIL: return j + 1
                return len(spans)
            r = dict(card=key, voice=voice, mode=mode, lines=len(L1), alert=bool(al), alert_s=first, alert_line=which(first) if first else None,
                     from_first_word=(first - spans[0][0]) if first else None, smax=max([e["data"]["s"] for e in ru] or [0]),
                     payment_start=spans[-1][0], margin=(spans[-1][0] - first) if first else None, spans=[(round(a, 1), round(b, 1)) for a, b in spans],
                     finals=[e["data"].get("text", "")[:70] for e in fin][:8], paused=paused)
            rows.append(r); Path(out).write_text(json.dumps(rows, indent=1)); os.remove(p)
            print(f"{key:7} {voice:5} {mode} alert={'NO' if not al else f'{first:.1f}s (line {r['alert_line']}, {r['from_first_word']:.1f}s from first word, margin {r['margin']:+.1f}s)'} smax={r['smax']:.2f}", flush=True)
    finally:
        await L.stop()
asyncio.run(main())
