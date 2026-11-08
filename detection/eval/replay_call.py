"""Replay a call WAV (8 kHz mono, e.g. a logs/audio dump or a script-card wav) through WS /stt/{call} of a P2 service in real time,
then read that service's log to print per-utterance endpoint->final and endpoint->risk.update latency. No transcript text is printed or saved.

  python -m detection.eval.replay_call WAV --url ws://127.0.0.1:8104 --log /path/to/service.log [--label before] [--json out.json]

Guards: refuses to start while the LIVE service (LIVE_HEALTH_URL, default :8100) has active_stt_sockets>0 (use --wait to pause until idle),
and requires the target's /healthz to answer. The replay uses a fresh call id and the target's own log; run the target with HUB_URL pointing nowhere.
Latency source: 'stt final <call>-uN: X s after endpoint' (endpoint time = log time - X) and 'risk.update call=<call> ...' lines."""
import argparse, asyncio, base64, datetime as dt, json, os, re, statistics as st, sys, time, urllib.request, uuid, wave
import numpy as np, websockets

LIVE_HEALTH = os.environ.get("LIVE_HEALTH_URL", "http://127.0.0.1:8100/healthz")
TS = re.compile(r"^(\d\d):(\d\d):(\d\d)\.(\d{3}) ")

def mulaw_encode(pcm):
    x = np.clip(pcm.astype(np.int32), -32635, 32635); s = (x < 0); x = np.abs(x) + 0x84
    e = np.clip(np.floor(np.log2(np.maximum(x, 1))).astype(int) - 7, 0, 7)
    m = (x >> (e + 3)) & 0x0F
    return (~(((s.astype(int) << 7) | (e << 4) | m)) & 0xFF).astype(np.uint8).tobytes()

def _get(url, timeout=3):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return json.loads(r.read())

def live_sockets():
    try:
        return int(_get(LIVE_HEALTH).get("active_stt_sockets", 0))
    except Exception:
        return 0            # unreachable live service counts as idle (same rule as run_eval)

def log_epoch(line, day0):
    m = TS.match(line)
    if not m: return None
    h, mi, s, ms = map(int, m.groups())
    return day0 + h * 3600 + mi * 60 + s + ms / 1000

def parse_log(lines, call, day0):
    finals, risks, alerts = [], [], []
    for ln in lines:
        if call not in ln: continue
        t = log_epoch(ln, day0)
        if t is None: continue
        m = re.search(r"stt final \S+-u(\d+): ([\d.]+)s after endpoint", ln)
        if m: finals.append({"u": int(m[1]), "t_final": t, "lag": float(m[2]), "t_end": t - float(m[2])}); continue
        m = re.search(r"risk\.update call=\S+ s=([\d.]+) band=(\S+) engine=(\S+) src=(\S+)", ln)
        if m: risks.append({"t": t, "s": float(m[1]), "band": m[2], "engine": m[3], "src": m[4]}); continue
        m = re.search(r"alert\.fired call=\S+ level=(\S+) src=(\S+) s=([\d.]+)", ln)
        if m: alerts.append({"t": t, "level": m[1], "src": m[2], "s": float(m[3])})
    return finals, risks, alerts

def summarize(finals, risks, alerts, t_start):
    rows, used = [], {}
    for f in sorted(finals, key=lambda x: x["u"]):
        r = next((x for x in risks if x["t"] >= f["t_final"]), None)
        row = {"u": f["u"], "endpoint_s": round(f["t_end"] - t_start, 2), "end_to_final_s": round(f["lag"], 2),
               "end_to_risk_s": None if r is None else round(r["t"] - f["t_end"], 2),
               "engine": None if r is None else r["engine"], "s": None if r is None else r["s"]}
        if r is not None:
            used[id(r)] = used.get(id(r), 0) + 1
            row["shared_risk"] = used[id(r)] > 1      # this window was coalesced with the previous one
        rows.append(row)
    lf = [r["end_to_final_s"] for r in rows]
    lr = [r["end_to_risk_s"] for r in rows if r["end_to_risk_s"] is not None]
    q = lambda v, p: None if not v else round(sorted(v)[min(len(v) - 1, int(p * len(v)))], 2)
    first_alert = None if not alerts else round(min(a["t"] for a in alerts) - t_start, 2)
    return {"utterances": len(rows), "finals_p50": None if not lf else round(st.median(lf), 2), "finals_max": None if not lf else max(lf),
            "risk_p50": None if not lr else round(st.median(lr), 2), "risk_p90": q(lr, 0.9), "risk_max": None if not lr else max(lr),
            "risk_updates": len(risks), "alerts": len(alerts), "first_alert_s": first_alert, "rows": rows}

async def stream(wav, url, call, speed):
    w = wave.open(wav); assert w.getframerate() == 8000 and w.getnchannels() == 1, "need 8 kHz mono WAV"
    pcm = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2")
    async with websockets.connect(f"{url}/stt/{call}") as ws:
        await ws.send(json.dumps({"event": "connected"}))
        await ws.send(json.dumps({"event": "start", "start": {"media_format": {"encoding": "PCMU", "sample_rate": 8000, "channels": 1}}}))
        t0 = time.time()
        for i in range(0, len(pcm) - 159, 160):
            await ws.send(json.dumps({"event": "media", "media": {"track": "inbound", "payload": base64.b64encode(mulaw_encode(pcm[i:i + 160])).decode()}}))
            await asyncio.sleep(max(0, t0 + (i + 160) / 8000 / speed - time.time()))
        await ws.send(json.dumps({"event": "stop"}))
        try: await asyncio.wait_for(ws.wait_closed(), 20)
        except Exception: pass
    return t0, len(pcm) / 8000

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("wav"); ap.add_argument("--url", default="ws://127.0.0.1:8104"); ap.add_argument("--log", required=True)
    ap.add_argument("--label", default="run"); ap.add_argument("--json"); ap.add_argument("--wait", action="store_true")
    ap.add_argument("--settle", type=float, default=15.0, help="seconds to wait after the stream ends for late finals/risk lines")
    ap.add_argument("--speed", type=float, default=1.0)
    a = ap.parse_args(argv)
    http = a.url.replace("ws://", "http://").replace("wss://", "https://")
    try: _get(http + "/healthz")
    except Exception as e: print(f"target {http} not answering: {type(e).__name__}"); return 2
    while live_sockets() > 0:
        if not a.wait: print("LIVE CALL in progress (active_stt_sockets>0); not starting"); return 3
        time.sleep(2)
    call = "replay-" + uuid.uuid4().hex[:8]
    day0 = dt.datetime.combine(dt.date.today(), dt.time()).timestamp()
    t_start, dur = asyncio.run(stream(a.wav, a.url, call, a.speed))
    time.sleep(a.settle)
    with open(a.log, errors="replace") as f: lines = f.readlines()
    out = summarize(*parse_log(lines, call, day0), t_start)
    out.update({"label": a.label, "audio_s": round(dur, 1), "call": call})
    print(f"[{a.label}] {dur:.1f}s audio, {out['utterances']} finals: endpoint->final p50 {out['finals_p50']} max {out['finals_max']} s; "
          f"endpoint->risk p50 {out['risk_p50']} p90 {out['risk_p90']} max {out['risk_max']} s; risk updates {out['risk_updates']}, alerts {out['alerts']}")
    for r in out["rows"]:
        print(f"  u{r['u']:<2} end@{r['endpoint_s']:>6}s  final +{r['end_to_final_s']}s  risk +{r['end_to_risk_s']}s  engine={r['engine']} s={r['s']}{' (shared)' if r.get('shared_risk') else ''}")
    if a.json:
        with open(a.json, "w") as f: json.dump(out, f, indent=1)
    return 0

if __name__ == "__main__":
    sys.exit(main())
