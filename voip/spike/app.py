"""TASK-002 spike: answer Telnyx call, ONE bidirectional caller-leg stream, log frames, optional tone inject.
Run: voip/.venv/bin/uvicorn voip.spike.app:app --port 8787
Env: TELNYX_API_KEY, PUBLIC_WS (wss://<tunnel host>), TARGET_LEGS=self|opposite|both, INJECT_TONE=1
Fail open: a stream failure never hangs up the call. Raw caller audio saved to the run logs dir only (never commit)."""
import os, json, base64, math, asyncio, time, pathlib, re, secrets, httpx
from urllib.parse import quote
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect

API = "https://api.telnyx.com/v2"
LOGDIR = pathlib.Path(os.environ.get("SPIKE_LOGDIR", "/Users/aymanmohammed/Documents/HackUTD26/.claude/overnight/run-20261107-2330/logs"))
app = FastAPI()
STATS: dict = {}
TOKENS: dict = {}  # call_session_id -> token, registered only from webhooks
CCID_RE = re.compile(r'^[A-Za-z0-9_:.=-]{8,200}$')
MAX_BYTES = 8000 * 60 * 10  # 10 min of PCMU per stream
# TODO(TASK-005): verify Telnyx Ed25519 webhook signature (telnyx-signature-ed25519 / telnyx-timestamp) before acting

def lin2ulaw(s: int) -> int:
    s = max(-32635, min(32635, s)); sign = 0x80 if s < 0 else 0
    s = abs(s) + 132; e = s.bit_length() - 8; m = (s >> (e + 3)) & 0x0F
    return ~(sign | (e << 4) | m) & 0xFF

def tone_frames(hz=1000, secs=2.0, rate=8000, chunk=160):
    pcm = [int(8000 * math.sin(2 * math.pi * hz * i / rate)) for i in range(int(rate * secs))]
    u = bytes(lin2ulaw(x) for x in pcm)
    return [u[i:i + chunk] for i in range(0, len(u), chunk)]

def save_evidence(name: str, obj):
    LOGDIR.mkdir(parents=True, exist_ok=True)
    with open(LOGDIR / name, "a") as f: f.write(json.dumps(obj) + "\n")

async def cmd(ccid: str, action: str, body: dict):
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.post(f"{API}/calls/{quote(ccid, safe='')}/actions/{action}", json=body,
                         headers={"Authorization": f"Bearer {os.environ['TELNYX_API_KEY']}"})
        save_evidence("eng2-cmd.jsonl", {"action": action, "status": r.status_code, "resp": r.text[:300]})
        return r

@app.post("/telnyx/webhook")
async def webhook(req: Request):
    ev = (await req.json())["data"]; et = ev["event_type"]; p = ev["payload"]
    save_evidence("eng2-webhooks.jsonl", ev)  # full payload incl. attestation fields (no secrets in payload)
    ccid = p.get("call_control_id")
    if et == "call.initiated" and p.get("direction") == "incoming":
        if not (ccid and CCID_RE.match(ccid) and CCID_RE.match(p.get('call_session_id', ''))): return {"ok": False}
        tok = TOKENS.setdefault(p['call_session_id'], secrets.token_urlsafe(16))
        body = {"stream_url": f"{os.environ['PUBLIC_WS']}/media/{p['call_session_id']}?t={tok}",
                "stream_track": "inbound_track", "stream_codec": "PCMU",
                "stream_bidirectional_mode": "rtp", "stream_bidirectional_codec": "PCMU",
                "stream_bidirectional_target_legs": os.environ.get("TARGET_LEGS", "self")}
        r = await cmd(ccid, "answer", body)
        if r.status_code >= 400:  # fail open: answer plain
            await cmd(ccid, "answer", {})
    return {"ok": True}

@app.websocket("/media/{call_id}")
async def media(ws: WebSocket, call_id: str, t: str = ""):
    if not (TOKENS.get(call_id) and secrets.compare_digest(TOKENS[call_id], t)):
        await ws.close(code=1008); return
    await ws.accept()
    st = STATS[call_id] = {"connected": 0, "start": 0, "media": 0, "stop": 0, "other": 0, "tracks": set()}
    raw = open(LOGDIR / f"eng2-caller-{call_id}.ulaw", "wb")
    stream_id = None; written = 0
    try:
        while True:
            m = json.loads(await ws.receive_text()); ev = m.get("event")
            if ev == "media":
                st["media"] += 1; st["tracks"].add(m["media"].get("track"))
                if written < MAX_BYTES:
                    b = base64.b64decode(m["media"]["payload"]); raw.write(b); written += len(b)
                if st["media"] == 1: save_evidence("eng2-frames.jsonl", m)
                if st["media"] == 150 and os.environ.get("INJECT_TONE"):
                    asyncio.create_task(inject(ws, stream_id))
            else:
                st[ev if ev in st else "other"] += 1; save_evidence("eng2-frames.jsonl", m)
                if ev == "start": stream_id = m.get("stream_id") or m["start"].get("stream_id", None)
    except (WebSocketDisconnect, RuntimeError):
        pass
    finally:
        raw.close(); st["tracks"] = sorted(map(str, st["tracks"])); save_evidence("eng2-summary.jsonl", {call_id: st})

async def inject(ws, stream_id):
    for f in tone_frames():
        await ws.send_text(json.dumps({"event": "media", "media": {"payload": base64.b64encode(f).decode()}}))
        await asyncio.sleep(0.02)

@app.get("/health")
def health(): return {"ok": True}
