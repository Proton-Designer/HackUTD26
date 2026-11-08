"""TASK-043: judge script cards (data/script-cards.md) over PHONE-QUALITY audio. SYNTHETIC voice (Magpie TTS) + synthetic degradation.
Renders each card line with TTS (cached), degrades like PSTN (300-3400 Hz band-pass, light noise, speech level in dBFS, optional 1.2x fast talker;
mu-law 8 kHz happens in stream_wav), streams each through a local hub+P2 (real STT, P2_ENGINE=local by default) one call at a time and prints a table.
Usage: pstn_cards.py [--variants p20,p28,fast] [--cards 1,2,b1] [--stt riva|whisper] [--out table.md]   (P2_STT=whisper also via --stt)
Cache dir: PSTN_CACHE (default detection/testdata/pstn, git-ignored by size: do not commit)."""
import argparse, asyncio, hashlib, json, os, re, sys, time, wave
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
CACHE = Path(os.environ.get("PSTN_CACHE", ROOT / "detection/testdata/pstn"))
SIL = 1.2
BENIGN = {
    "b1": ("Legit bank notice", ["Hi, this is the fraud department at your bank. We saw a charge at a grocery store and want to confirm it was you.",
                                 "If it was you, there is nothing to do. We will never ask for your codes or passwords.",
                                 "If you are unsure, hang up and call the number on the back of your card. Have a good day."]),
    "b2": ("Pharmacy pickup", ["Hello, this is the pharmacy at the corner. Your prescription is ready for pickup.",
                               "We are open until nine tonight. Bring your insurance card when you come in.", "Thanks, and have a nice evening."]),
    "b3": ("Friend chat", ["Hey, it's Sam. Are we still on for dinner on Saturday?", "I was thinking the Italian place by the park, around seven.",
                           "Let me know if that works, and bring your sister if she wants to come."]),
}

def parse_cards(md):
    cards = {}
    for block in re.split(r"(?m)^# Card ", md)[1:]:
        n, title = re.match(r"(\d+): (.*)", block).groups()
        lines = [m.group(1) for m in re.finditer(r'(?m)^\d\. \*\*"(.*)"\*\*', block)]
        for h in ("### Payment step", "### Zelle step"):
            m = re.search(re.escape(h) + r'[^\n]*\n\*\*"(.*)"\*\*', block)
            if m: lines.append(m.group(1))
        cards[n] = (title.strip(), [re.sub(r"\s+([.,])", r"\1", l) for l in lines])
    return cards

def synth_line(text):
    f = CACHE / "tts" / (hashlib.sha1(text.encode()).hexdigest()[:16] + ".npy")
    if f.exists(): return np.load(f)
    import riva.client
    from dotenv import dotenv_values
    key = os.environ.get("NVIDIA_API_KEY") or dotenv_values(ROOT / ".env").get("NVIDIA_API_KEY")
    auth = riva.client.Auth(None, True, "grpc.nvcf.nvidia.com:443", [["function-id", "877104f7-e885-42b9-8de8-f6e4c6303969"], ["authorization", "Bearer " + key]])
    # wallets/URLs/phone numbers are read as written by the judge; spell the dotted forms the way a person would say them
    spoken = text.replace("refunds.dept@backfire-demo.example", "refunds dot dept at backfire dash demo dot example").replace("backfire-demo.example", "backfire dash demo dot example")
    svc = riva.client.SpeechSynthesisService(auth)
    for attempt in range(8):
        try:
            pcm = np.frombuffer(svc.synthesize(spoken, language_code="en-US", sample_rate_hz=8000, voice_name="Magpie-Multilingual.EN-US.Mia").audio, dtype="<i2"); break
        except Exception as e:   # shared team key: back off on rate limit, keep what is cached
            if "exceeded rate limit" not in str(e) or attempt == 7: raise
            print("TTS rate limited, waiting 25 s", flush=True); time.sleep(25)
    f.parent.mkdir(parents=True, exist_ok=True); np.save(f, pcm); time.sleep(3.0)   # shared rate limit
    return pcm

def bandpass(x, lo=300.0, hi=3400.0, rate=8000):
    X = np.fft.rfft(x); fr = np.fft.rfftfreq(len(x), 1 / rate)
    g = np.clip((fr - lo * 0.8) / (lo * 0.4), 0, 1) * np.clip((hi * 1.1 - fr) / (hi * 0.2), 0, 1)   # soft skirts around the corners
    return np.fft.irfft(X * g, len(x))

def speech_rms(x, frame=160):
    f = x[: len(x) // frame * frame].reshape(-1, frame); r = np.sqrt((f ** 2).mean(1)); loud = r[r > 0.3 * np.percentile(r, 95)]
    return float(np.sqrt((loud ** 2).mean())) if len(loud) else float(r.mean())

def degrade(pcm, level_dbfs=-28.0, speed=1.0, snr_db=25.0, seed=7):
    """PSTN-like: speed -> band-pass 300-3400 -> set ACTIVE-speech RMS to level_dbfs -> add band-limited noise at snr_db below speech. Returns int16 (mu-law applied by the streamer)."""
    x = pcm.astype(np.float64)
    if speed != 1.0:
        x = np.interp(np.arange(0, len(x), speed), np.arange(len(x)), x)       # crude resample: also raises pitch ~ a fast, higher talker
    x = bandpass(x)
    x *= (10 ** (level_dbfs / 20) * 32768) / max(speech_rms(x), 1e-9)
    noise = bandpass(np.random.default_rng(seed).standard_normal(len(x))); noise *= speech_rms(x) * 10 ** (-snr_db / 20) / max(noise.std(), 1e-9)
    return np.clip(x + noise, -32768, 32767).astype("<i2")

def build(lines, level, speed):
    """-> (int16 pcm 8 kHz, [(start_s, end_s) per line])."""
    parts, spans, t = [np.zeros(8000, "<i2")], [], 1.0
    for l in lines:
        d = degrade(synth_line(l), level, speed); gap = np.zeros(int(8000 * SIL), "<i2")
        spans.append((t, t + len(d) / 8000)); parts += [d, gap]; t += (len(d) + len(gap)) / 8000
    return np.concatenate(parts), spans

def words(s): return re.findall(r"[a-z0-9']+", s.lower())
def matched(ref, hyp):
    from collections import Counter
    r, h = Counter(words(ref)), Counter(words(hyp)); return sum(min(v, h[k]) for k, v in r.items()) / max(1, sum(r.values()))

VARIANTS = {"p20": (-20.0, 1.0), "p28": (-28.0, 1.0), "q38": (-38.0, 1.0), "fast": (-28.0, 1.2)}

LIVE = os.environ.get("PSTN_LIVE_URL", "http://localhost:8100")


def wait_idle(max_wait_s=1800):
    """RULES-CARD guard: never run llama-using batches while the LIVE service has a call (active_stt_sockets>0). Fails open if :8100 is unreachable."""
    import urllib.request
    t0 = time.time()
    while time.time() - t0 < max_wait_s:
        try:
            n = json.load(urllib.request.urlopen(LIVE + "/healthz", timeout=3)).get("active_stt_sockets", 0)
        except Exception:
            return
        if not n: return
        print(f"live call active ({n} sockets): paused", flush=True); time.sleep(10)


async def main(a):
    from detection import detect as D
    from detection.scripts.acceptance import Loop, fmt
    md = (ROOT / "data/script-cards.md").read_text()
    cards = {f"s{n}": v for n, v in parse_cards(md).items()}; cards.update(BENIGN)
    want = a.cards.split(",") if a.cards else list(cards)
    want = [("s" + w if w.isdigit() else w) for w in want]
    jobs = [(c, v) for c in want for v in a.variants.split(",")]
    wavs = {}
    for c, v in jobs:
        title, lines = cards[c]; pcm, spans = build(lines, *VARIANTS[v])
        p = CACHE / f"{c}_{v}.wav"; p.parent.mkdir(parents=True, exist_ok=True)
        w = wave.open(str(p), "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(8000); w.writeframes(pcm.tobytes()); w.close(); wavs[(c, v)] = (str(p), spans)
    if a.stt == "whisper": os.environ["P2_STT"] = "whisper"
    ids = {j: f"pc_{j[0]}_{j[1]}_{a.stt}" for j in jobs}
    L = Loop(os.environ.get("ACC_ENGINE", "local"), list(ids.values())); await L.start()
    rows = json.loads(Path(a.json).read_text()) if Path(a.json).exists() and a.resume else []
    done = {(r["card"], r["variant"]) for r in rows}
    try:
        for (c, v) in jobs:
            if (c, v) in done: continue
            wait_idle()
            cid = ids[(c, v)]; title, lines = cards[c]; wav, spans = wavs[(c, v)]
            t0 = await L.run_call(cid, wav)
            fin = [e for e in L.ev(cid, "transcript.caller") if e["data"].get("is_final", True)]
            hyp = " ".join(e["data"].get("text", "") for e in fin)
            ref_main = " ".join(lines[:5] if c.startswith("s") else lines)
            al = L.ev(cid, "alert.fired"); ru = L.ev(cid, "risk.update")
            ask_i = next((i for i, l in enumerate(lines) if D.rule_scan(l)["asks"]), None)
            first = (al[0]["_t"] - t0) if al else None
            ask_end = spans[ask_i][1] if ask_i is not None else None
            # final latency
            lat = []   # per line: first final arriving at/after the line's end (a mid-line endpoint split must not count as latency)
            for sp in spans:
                nxt = [e["_t"] - t0 for e in fin if e["_t"] - t0 >= sp[1] - 0.05]
                if nxt: lat.append(min(nxt) - sp[1])
            rows.append(dict(card=c, title=title, variant=v, stt=a.stt, words=matched(ref_main, hyp), finals=len(fin), lines=len(lines),
                             smax=max([e["data"]["s"] for e in ru] or [0]), alert=(first - ask_end) if (first is not None and ask_end is not None) else None,
                             alert_abs=first, fired=bool(al), ask_line=None if ask_i is None else ask_i + 1, lat=(sum(lat) / len(lat) if lat else None),
                             hyp=hyp[:400]))
            Path(a.json).write_text(json.dumps(rows, indent=1))      # incremental: a stopped run keeps its rows (--resume continues)
            r = rows[-1]; print(f"{c:4} {v:5} words={r['words']:.0%} finals={r['finals']}/{r['lines']} s={r['smax']:.2f} alert={'NO' if not r['fired'] else fmt(r['alert'])} lat={fmt(r['lat'])}", flush=True)
    finally:
        await L.stop()
    Path(a.json).write_text(json.dumps(rows, indent=1))
    print("wrote", a.json)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--variants", default="p20,p28,fast"); ap.add_argument("--cards", default="")
    ap.add_argument("--stt", default="riva"); ap.add_argument("--resume", action="store_true"); ap.add_argument("--json", default="pstn_rows.json")
    asyncio.run(main(ap.parse_args()))
