"""TASK-053: compare Whisper replays of real call dumps with the live Riva finals for the same call. AGGREGATES ONLY: no transcript text is printed or saved.
  python -m detection.eval.stt_compare --riva-log logs/p2.log --whisper-log svc.log --pair RIVA_CALL_ID=REPLAY_CALL_ID[,..] [--audio-dir logs/audio]
Per call: finals count, word agreement (Riva transcript as the proxy reference, multiset overlap / Riva words, and the reverse), Whisper finals with no Riva
final within +-2 s of the same audio time ('extra'), Whisper finals that are on the common hallucination list, Riva finals Whisper missed."""
import argparse, re, sys
from collections import Counter
from detection.eval.replay_call import log_epoch
import datetime as dt

HALLU = {"thank you", "thanks for watching", "you", "bye", "okay", "thank you for watching", "so", "oh", "uh", "um", "mm", "hmm"}
FIN = re.compile(r"stt final (\S+)-u(\d+): ([\d.]+)s after endpoint: '(.*)'")

def words(s): return re.findall(r"[a-z0-9']+", s.lower())

def finals(lines, cid, day0):
    t0, out = None, []
    for ln in lines:
        if cid not in ln: continue
        t = log_epoch(ln, day0)
        if t is None: continue
        if t0 is None and "first frame" in ln: t0 = t
        m = FIN.search(ln)
        if m and m[1] == cid: out.append({"u": int(m[2]), "end": t - float(m[3]) - (t0 or 0), "lag": float(m[3]), "text": m[4]})
    return out

def agree(a, b):
    ca, cb = Counter(words(a)), Counter(words(b))
    return sum(min(v, cb[k]) for k, v in ca.items()) / max(1, sum(ca.values()))

def compare(rf, wf):
    rt, wt = " ".join(f["text"] for f in rf), " ".join(f["text"] for f in wf)
    extra = [f for f in wf if not any(abs(f["end"] - r["end"]) <= 2.0 for r in rf)]
    missed = [r for r in rf if not any(abs(f["end"] - r["end"]) <= 2.0 for f in wf)]
    lag = sorted(f["lag"] for f in wf)
    return {"riva_finals": len(rf), "whisper_finals": len(wf), "riva_words": len(words(rt)), "whisper_words": len(words(wt)),
            "agree_vs_riva": round(agree(rt, wt), 3), "riva_vs_whisper": round(agree(wt, rt), 3), "extra": len(extra), "missed": len(missed),
            "hallu": sum(1 for f in wf if re.sub(r"[^a-z ]", "", f["text"].lower()).strip() in HALLU),
            "hallu_riva": sum(1 for f in rf if re.sub(r"[^a-z ]", "", f["text"].lower()).strip() in HALLU),
            "lag_p50": round(lag[len(lag) // 2], 2) if lag else None, "lag_max": lag[-1] if lag else None}

def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("--riva-log", required=True); ap.add_argument("--whisper-log", required=True); ap.add_argument("--pair", required=True)
    a = ap.parse_args(argv)
    day0 = dt.datetime.combine(dt.date.today(), dt.time()).timestamp()
    rl = open(a.riva_log, errors="replace").readlines(); wl = open(a.whisper_log, errors="replace").readlines()
    for p in a.pair.split(","):
        rc, wc = p.split("=")
        rcid = next((m[1] for ln in rl for m in [re.search(r"stt final (" + re.escape(rc) + r"\S*)-u\d+:", ln)] if m), rc)
        r = compare(finals(rl, rcid, day0), finals(wl, wc, day0))
        print(rc[:8], r)
if __name__ == "__main__":
    sys.exit(main())
