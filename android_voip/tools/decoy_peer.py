"""Backfire decoy peer: joins Demo VoIP calls as `decoy` after Scammer Get Scammed.

The signaling server (BACKFIRE_HUB set) moves the scammer's call here. This peer bridges the WebRTC audio to the hub's
WS /android/decoy/{call_id}, which runs it through server/relay.py into P3's WSS /decoy/{call_id} (Telnyx protocol), or
into the hub's built-in echo decoy when P3_DECOY_URL is unset. So the decoy engine is the same one the Telnyx path uses.

  scammer phone --WebRTC/Opus--> this peer --PCM16 8 kHz--> hub /android/decoy --mu-law frames--> P3 /decoy
  scammer phone <--WebRTC/Opus-- this peer <--mu-law media/clear-- hub <------------------------- P3

Run from the repo root (hub and signaling server on this laptop):
  .venv-hub/bin/python android_voip/tools/decoy_peer.py --server ws://127.0.0.1:8090 --hub http://127.0.0.1:8000
"""
import argparse
import asyncio
import base64
import fractions
import json
import os
import sys
import time

import av
import websockets
from aiortc import MediaStreamTrack, RTCConfiguration, RTCIceServer, RTCPeerConnection, RTCSessionDescription
from aiortc.sdp import candidate_from_sdp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from bridge import ulaw  # noqa: E402

RATE = 8000
FRAME = 160                 # 20 ms at 8 kHz
FRAME_BYTES = FRAME * 2


def log(*a):
    print(f"[{time.strftime('%H:%M:%S')}] [decoy]", *a, flush=True)


class DecoyVoice(MediaStreamTrack):
    """Plays whatever the decoy engine sends; silence otherwise. aiortc resamples 8 kHz to Opus's 48 kHz."""
    kind = "audio"

    def __init__(self):
        super().__init__()
        self.buf = bytearray()
        self.pts = 0
        self.start = None

    def play(self, pcm: bytes):
        self.buf += pcm
        if len(self.buf) > RATE * 2 * 30:          # never queue more than 30 s
            del self.buf[: len(self.buf) - RATE * 2 * 30]

    def clear(self):
        self.buf.clear()                           # barge-in: the scammer started talking

    async def recv(self):
        if self.start is None:
            self.start = time.monotonic()
        delay = self.start + self.pts / RATE - time.monotonic()
        if delay > 0:
            await asyncio.sleep(delay)
        chunk = bytes(self.buf[:FRAME_BYTES])
        del self.buf[:FRAME_BYTES]
        chunk += b"\0" * (FRAME_BYTES - len(chunk))
        frame = av.AudioFrame(format="s16", layout="mono", samples=FRAME)
        frame.planes[0].update(chunk)
        frame.sample_rate = RATE
        frame.pts = self.pts
        frame.time_base = fractions.Fraction(1, RATE)
        self.pts += FRAME
        return frame


class Session:
    def __init__(self, app, call_id, peer):
        self.app, self.call_id, self.peer = app, call_id, peer
        # aiortc gathers every candidate before answering; skipping STUN on a LAN cuts the handoff gap from ~5 s to <1 s.
        ice = [RTCIceServer(app.args.stun)] if app.args.stun else []
        self.pc = RTCPeerConnection(RTCConfiguration(iceServers=ice))
        self.voice = DecoyVoice()
        self.pc.addTrack(self.voice)
        self.hub = None
        self.remote_set = False
        self.pending = []
        self.closed = False
        self.tasks = []

        @self.pc.on("track")
        def on_track(track):
            log(self.call_id[:8], "hearing the scammer")
            self.tasks.append(asyncio.create_task(self.uplink(track)))

        @self.pc.on("connectionstatechange")
        async def on_state():
            log(self.call_id[:8], "connection:", self.pc.connectionState)
            if self.pc.connectionState == "failed":
                await self.end("failed")

    async def answer(self, sdp):
        await self.pc.setRemoteDescription(RTCSessionDescription(sdp, "offer"))
        self.remote_set = True
        for m in self.pending:
            await self.add_candidate(m)
        self.pending.clear()
        await self.connect_hub()
        await self.pc.setLocalDescription(await self.pc.createAnswer())
        await self.app.send({"type": "answer", "to": self.peer, "callId": self.call_id, "sdp": self.pc.localDescription.sdp})
        log(self.call_id[:8], f"answered {self.peer}")
        self.tasks.append(asyncio.create_task(self.cap()))

    async def connect_hub(self):
        url = self.app.args.hub.replace("http", "ws", 1).rstrip("/") + f"/android/decoy/{self.call_id}"
        if self.app.args.hub_token:
            url += "?t=" + self.app.args.hub_token
        try:
            self.hub = await asyncio.wait_for(websockets.connect(url, max_size=None), 3)
            self.tasks.append(asyncio.create_task(self.downlink()))
        except Exception as e:
            log(self.call_id[:8], f"hub unreachable ({type(e).__name__}); the scammer will hear silence")

    async def uplink(self, track):
        """Scammer audio -> hub, as PCM16 8 kHz mono."""
        rs = av.AudioResampler(format="s16", layout="mono", rate=RATE)
        while not self.closed:
            try:
                frame = await track.recv()
            except Exception:
                return
            if self.hub is None:
                continue
            for f in rs.resample(frame):
                try:
                    await self.hub.send(bytes(f.planes[0])[: f.samples * 2])
                except Exception:
                    self.hub = None
                    return

    async def downlink(self):
        """Decoy engine -> scammer."""
        try:
            async for raw in self.hub:
                if not isinstance(raw, str):
                    continue
                m = json.loads(raw)
                ev = m.get("event")
                if ev == "media":
                    self.voice.play(ulaw.decode(base64.b64decode(m["media"]["payload"])))
                elif ev == "clear":
                    self.voice.clear()
                elif ev == "backfire":
                    log(self.call_id[:8], "decoy engine:", m.get("decoy"))
        except Exception as e:
            log(self.call_id[:8], f"hub link lost ({type(e).__name__})")
        if not self.closed:
            await self.end("decoy_done")

    async def cap(self):
        await asyncio.sleep(self.app.args.max_minutes * 60)
        log(self.call_id[:8], "time cap reached")
        await self.end("decoy_cap")

    async def add_candidate(self, msg):
        c = candidate_from_sdp(msg["candidate"].split(":", 1)[1])
        c.sdpMid = msg.get("sdpMid")
        c.sdpMLineIndex = msg.get("sdpMLineIndex")
        await self.pc.addIceCandidate(c)

    async def ice(self, msg):
        if self.remote_set:
            await self.add_candidate(msg)
        else:
            self.pending.append(msg)

    async def end(self, reason, notify=True):
        if self.closed:
            return
        self.closed = True
        if notify:
            await self.app.send({"type": "bye", "to": self.peer, "callId": self.call_id, "reason": "remote_hangup"})
        log(self.call_id[:8], "ended:", reason)
        for t in self.tasks:
            if t is not asyncio.current_task():
                t.cancel()
        if self.hub is not None:
            try:
                await self.hub.close()
            except Exception:
                pass
        await self.pc.close()
        self.app.sessions.pop(self.call_id, None)


class App:
    def __init__(self, args):
        self.args = args
        self.ws = None
        self.sessions: dict[str, Session] = {}

    async def send(self, msg):
        try:
            await self.ws.send(json.dumps(msg))
        except Exception:
            pass

    async def handle(self, msg):
        t, cid = msg.get("type"), msg.get("callId")
        s = self.sessions.get(cid)
        if t == "registered":
            log(f"online as {msg.get('id')} on {self.args.server}; waiting for handoffs")
        elif t == "error":
            log("server error:", msg.get("message"))
        elif t == "offer" and cid and s is None:
            s = self.sessions[cid] = Session(self, cid, msg["from"])
            await s.answer(msg["sdp"])
        elif t == "ice" and s is not None:
            await s.ice(msg)
        elif t in ("bye", "reject") and s is not None:
            await s.end("scammer hung up", notify=False)

    async def run(self):
        while True:
            try:
                async with websockets.connect(self.args.server) as ws:
                    self.ws = ws
                    reg = {"type": "register", "id": self.args.name}
                    if self.args.secret:
                        reg["secret"] = self.args.secret
                    await self.send(reg)
                    async for raw in ws:
                        await self.handle(json.loads(raw))
            except Exception as e:
                log(f"signaling lost ({type(e).__name__}); retrying in 2 s")
            await asyncio.sleep(2)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--server", default="ws://127.0.0.1:8090", help="Demo VoIP signaling server")
    p.add_argument("--hub", default=os.environ.get("BACKFIRE_HUB", "http://127.0.0.1:8000"), help="Backfire hub base URL")
    p.add_argument("--hub-token", default=os.environ.get("HUB_TOKEN", ""), help="HUB_TOKEN, if the hub uses one")
    p.add_argument("--name", default=os.environ.get("DECOY_ID", "decoy"))
    p.add_argument("--secret", default=os.environ.get("DECOY_SECRET", ""))
    p.add_argument("--max-minutes", type=float, default=20)
    p.add_argument("--stun", default="", help="STUN URL (e.g. stun:stun.l.google.com:19302) if phones are not on this LAN")
    asyncio.run(App(p.parse_args()).run())


if __name__ == "__main__":
    main()
