"""End-to-end check of the Android VoIP Backfire path, all on this laptop (no phones needed).

Two fake phones speak the app's signaling protocol:
  scammer: calls maria, plays a 440 Hz tone, records what it hears, and obeys {type:"transfer"} like the app does
  maria:   answers, streams the caller's audio to /android/media, waits for alert.fired, taps Scammer Get Scammed
Expects: call routed LIVE_GUARD -> handoff -> scammer hears the decoy (the hub's echo decoy plays its own tone back)
-> scammer hangs up -> number blocked -> second call is rejected before ringing.

Needs running: hub (android_voip.bridge.hub_app), signaling server with BACKFIRE_HUB, decoy_peer.py. See BACKFIRE.md.
  .venv-hub/bin/python android_voip/tools/e2e_backfire.py
"""
import argparse
import asyncio
import json
import sys
import time
import uuid

import httpx
import numpy as np
import websockets
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.sdp import candidate_from_sdp

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from testpeer import ToneTrack  # noqa: E402

import av  # noqa: E402


def log(who, *a):
    print(f"[{time.strftime('%H:%M:%S')}] [{who}]", *a, flush=True)


class Phone:
    def __init__(self, name, server):
        self.name, self.server = name, server
        self.ws = None
        self.pc = None
        self.inbox = asyncio.Queue()
        self.remote_set = False
        self.pending = []
        self.heard = []          # (t, rms) of received audio
        self.on_track = None

    async def connect(self):
        self.ws = await websockets.connect(self.server)
        await self.send({"type": "register", "id": self.name})
        asyncio.create_task(self._read())

    async def _read(self):
        async for raw in self.ws:
            m = json.loads(raw)
            if m.get("type") == "ice" and self.pc:
                if self.remote_set:
                    await self._cand(m)
                else:
                    self.pending.append(m)
                continue
            await self.inbox.put(m)

    async def _cand(self, m):
        c = candidate_from_sdp(m["candidate"].split(":", 1)[1])
        c.sdpMid, c.sdpMLineIndex = m.get("sdpMid"), m.get("sdpMLineIndex")
        await self.pc.addIceCandidate(c)

    async def remote(self, sdp, kind):
        await self.pc.setRemoteDescription(RTCSessionDescription(sdp, kind))
        self.remote_set = True
        for m in self.pending:
            await self._cand(m)
        self.pending.clear()

    async def send(self, m):
        await self.ws.send(json.dumps(m))

    async def expect(self, *types, timeout=10):
        end = time.monotonic() + timeout
        while True:
            m = await asyncio.wait_for(self.inbox.get(), max(0.1, end - time.monotonic()))
            if m.get("type") in types:
                return m

    def new_pc(self, tone):
        if self.pc:
            asyncio.create_task(self.pc.close())
        self.pc, self.remote_set, self.pending = RTCPeerConnection(), False, []
        self.pc.addTrack(ToneTrack(tone))

        @self.pc.on("track")
        def _(track):
            asyncio.create_task(self._record(track))
            if self.on_track:
                self.on_track(track)
        return self.pc

    async def _record(self, track):
        while True:
            try:
                f = await track.recv()
            except Exception:
                return
            a = f.to_ndarray().astype(np.float32)
            self.heard.append((time.monotonic(), float(np.sqrt((a ** 2).mean()))))

    def loudness_since(self, t0):
        v = [r for t, r in self.heard if t >= t0]
        return max(v) if v else 0.0


async def uplink_to_hub(track, url):
    """What Maria's app does: caller audio -> PCM16 8 kHz mono -> /android/media."""
    rs = av.AudioResampler(format="s16", layout="mono", rate=8000)
    async with websockets.connect(url) as ws:
        while True:
            try:
                f = await track.recv()
            except Exception:
                return
            for o in rs.resample(f):
                await ws.send(bytes(o.planes[0])[: o.samples * 2])


async def main(a):
    hub = a.hub.rstrip("/")
    hubws = hub.replace("http", "ws", 1)
    tag = uuid.uuid4().hex[:4]
    scam_id, maria_id = f"+1214555{int(tag, 16) % 10000:04d}", f"maria-{tag}"
    scammer, maria = Phone(scam_id, a.server), Phone(maria_id, a.server)
    await scammer.connect(); await maria.connect()
    await asyncio.sleep(0.3)
    http = httpx.AsyncClient(timeout=5)
    ok = True

    def check(cond, what):
        nonlocal ok
        log("CHECK", ("PASS " if cond else "FAIL ") + what)
        ok &= bool(cond)

    # 1. scammer calls maria
    call_id = str(uuid.uuid4())
    pc = scammer.new_pc(440)
    await pc.setLocalDescription(await pc.createOffer())
    await scammer.send({"type": "offer", "to": maria_id, "callId": call_id, "sdp": pc.localDescription.sdp})
    offer = await maria.expect("offer")
    bf = offer.get("backfire") or {}
    check(bf.get("decision") == "LIVE_GUARD", f"carrier routed the call LIVE_GUARD ({bf})")

    # 2. maria subscribes to her call's events, answers, streams the caller's audio
    events = []
    ev_ws = await websockets.connect(f"{hubws}/android/events/{call_id}")

    async def read_events():
        async for raw in ev_ws:
            events.append(json.loads(raw))
    asyncio.create_task(read_events())
    mpc = maria.new_pc(660)
    maria.on_track = lambda t: asyncio.create_task(uplink_to_hub(t, f"{hubws}/android/media/{call_id}"))
    await maria.remote(offer["sdp"], "offer")
    await mpc.setLocalDescription(await mpc.createAnswer())
    await maria.send({"type": "answer", "to": scam_id, "callId": call_id, "sdp": mpc.localDescription.sdp})
    ans = await scammer.expect("answer")
    await scammer.remote(ans["sdp"], "answer")
    t_talk = time.monotonic()
    await asyncio.sleep(2.5)
    check(scammer.loudness_since(t_talk) > 500, "scammer hears maria (660 Hz) before handoff")

    # 3. a detector (P2 stand-in) fires an alert on the bus; maria's app would beep and show the buttons
    await http.post(f"{hub}/events", json={"type": "alert.fired", "call_id": call_id,
                                           "data": {"level": "first", "why_chips": ["Asks for gift cards", "Claims to be IRS"]}})
    await asyncio.sleep(0.5)
    check(any(e["type"] == "alert.fired" for e in events), "maria's event stream got alert.fired")

    # 4. maria taps Scammer Get Scammed
    r = await http.post(f"{hub}/user/action", json={"call_id": call_id, "action": "scammer_get_scammed"})
    check(r.status_code == 200, f"POST /user/action -> {r.status_code}")
    bye = await maria.expect("bye", "backfire")
    check(bye.get("type") == "bye" and bye.get("reason") == "handoff", f"maria is released from the call ({bye})")
    tr = await scammer.expect("transfer")
    check(tr.get("to") == "decoy", f"scammer's phone told to move the call to the decoy ({tr})")

    # 5. scammer's phone re-offers the same call to the decoy, like CallManager.startTransfer
    pc = scammer.new_pc(440)
    await pc.setLocalDescription(await pc.createOffer())
    await scammer.send({"type": "offer", "to": tr["to"], "callId": call_id, "sdp": pc.localDescription.sdp})
    ans = await scammer.expect("answer")
    await scammer.remote(ans["sdp"], "answer")
    t_decoy = time.monotonic()
    await asyncio.sleep(4)
    check(scammer.loudness_since(t_decoy + 1) > 300, "scammer hears the decoy (echo decoy plays the scammer's tone back)")
    types = [e["type"] for e in events]
    check("handoff.started" in types, "handoff.started on the bus")
    check(any(e["type"] == "call.answered" and e["data"].get("by") == "decoy" for e in events), "call.answered by decoy")

    # 6. scammer hangs up -> call.ended -> blocklist.updated
    await scammer.send({"type": "bye", "to": tr["to"], "callId": call_id, "reason": "remote_hangup"})
    await asyncio.sleep(1)
    check(any(e["type"] == "call.ended" and e["data"].get("ended_by") == "caller" for e in events), "call.ended by caller")
    check(any(e["type"] == "blocklist.updated" for e in events), "scammer's number added to maria's blocklist")

    # 7. scammer calls back -> rejected before ringing
    cb = str(uuid.uuid4())
    pc = scammer.new_pc(440)
    await pc.setLocalDescription(await pc.createOffer())
    await scammer.send({"type": "offer", "to": maria_id, "callId": cb, "sdp": pc.localDescription.sdp})
    rej = await scammer.expect("reject", "answer")
    check(rej.get("type") == "reject" and rej.get("reason") == "blocked", f"callback rejected before ring ({rej})")
    rang = False
    try:
        await maria.expect("offer", timeout=1.5)
        rang = True
    except asyncio.TimeoutError:
        pass
    check(not rang, "maria's phone never rang for the callback")

    # cleanup: unblock so the test can be rerun with the same hub
    log_ = (await http.get(f"{hub}/protection-log")).json()
    for b in log_.get("blocked", []):
        if b["number"].endswith(scam_id[-4:]):
            await http.post(f"{hub}/protection-log/undo", json={"undo_token": b["undo_token"]})
    print("\nRESULT:", "ALL PASS" if ok else "FAILURES (see above)")
    return 0 if ok else 1


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--server", default="ws://127.0.0.1:8090")
    p.add_argument("--hub", default="http://127.0.0.1:8000")
    sys.exit(asyncio.run(main(p.parse_args())))
