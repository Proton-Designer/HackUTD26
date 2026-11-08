"""Laptop-side test peer for the demo VoIP app.

Speaks the same signaling protocol as the app, sends a 440 Hz tone as its "voice",
and records whatever audio the phone sends to a WAV file.

  answer mode: wait for a call, answer after --ring seconds
  call mode:   call --target, then talk
Either way it hangs up after --talk seconds (or when the phone hangs up).
"""
import argparse
import asyncio
import fractions
import json
import math
import time
import uuid
import wave

import av
import numpy as np
import websockets
from aiortc import MediaStreamTrack, RTCPeerConnection, RTCSessionDescription
from aiortc.sdp import candidate_from_sdp

RATE = 48000
FRAME = 960  # 20 ms


class ToneTrack(MediaStreamTrack):
    kind = "audio"

    def __init__(self, freq=440.0):
        super().__init__()
        self.freq = freq
        self.pts = 0
        self.start = None

    async def recv(self):
        if self.start is None:
            self.start = time.monotonic()
        target = self.start + self.pts / RATE
        delay = target - time.monotonic()
        if delay > 0:
            await asyncio.sleep(delay)
        t = (np.arange(FRAME) + self.pts) / RATE
        samples = (0.3 * 32767 * np.sin(2 * math.pi * self.freq * t)).astype(np.int16)
        frame = av.AudioFrame.from_ndarray(samples.reshape(1, -1), format="s16", layout="mono")
        frame.sample_rate = RATE
        frame.pts = self.pts
        frame.time_base = fractions.Fraction(1, RATE)
        self.pts += FRAME
        return frame


class Peer:
    def __init__(self, args):
        self.args = args
        self.ws = None
        self.pc = None
        self.call_id = None
        self.peer = None
        self.remote_set = False
        self.pending = []
        self.frames = []
        self.done = asyncio.Event()
        self.connected_at = None

    def log(self, *a):
        print(f"[{time.strftime('%H:%M:%S')}] [{self.args.name}]", *a, flush=True)

    async def send(self, msg):
        await self.ws.send(json.dumps(msg))

    def new_pc(self):
        pc = RTCPeerConnection()
        pc.addTrack(ToneTrack())

        @pc.on("connectionstatechange")
        async def _():
            self.log("connection:", pc.connectionState)
            if pc.connectionState == "connected" and self.connected_at is None:
                self.connected_at = time.monotonic()
                asyncio.create_task(self.talk_then_hangup())
            if pc.connectionState in ("failed", "closed"):
                self.done.set()

        @pc.on("track")
        def on_track(track):
            self.log("receiving", track.kind)
            asyncio.create_task(self.record(track))

        return pc

    async def record(self, track):
        while True:
            try:
                frame = await track.recv()
            except Exception:
                return
            arr = frame.to_ndarray()
            # aiortc gives s16 interleaved; keep the first channel
            ch = len(frame.layout.channels)
            mono = arr.reshape(-1, ch)[:, 0] if arr.ndim == 2 and arr.shape[0] == 1 else arr[0]
            self.frames.append((frame.sample_rate, mono.astype(np.int16)))

    async def talk_then_hangup(self):
        await asyncio.sleep(self.args.talk)
        if not self.done.is_set():
            self.log("hanging up")
            await self.send({"type": "bye", "to": self.peer, "callId": self.call_id, "reason": "remote_hangup"})
            self.done.set()

    async def add_candidate(self, msg):
        c = candidate_from_sdp(msg["candidate"].split(":", 1)[1])
        c.sdpMid = msg.get("sdpMid")
        c.sdpMLineIndex = msg.get("sdpMLineIndex")
        await self.pc.addIceCandidate(c)

    async def on_remote_description(self):
        self.remote_set = True
        for m in self.pending:
            await self.add_candidate(m)
        self.pending.clear()

    async def handle(self, msg):
        t = msg.get("type")
        if t == "users":
            self.log("online:", msg["ids"])
            if self.args.mode == "call" and self.call_id is None and self.args.target in msg["ids"]:
                await self.place_call()
        elif t == "offer" and self.args.mode == "answer" and self.call_id is None:
            self.call_id, self.peer = msg["callId"], msg["from"]
            self.log(f"incoming call from {self.peer}; answering in {self.args.ring}s")
            if self.args.decline:
                await asyncio.sleep(self.args.ring)
                await self.send({"type": "reject", "to": self.peer, "callId": self.call_id})
                self.log("declined")
                self.done.set()
                return
            self.pc = self.new_pc()
            await self.pc.setRemoteDescription(RTCSessionDescription(msg["sdp"], "offer"))
            await self.on_remote_description()
            await asyncio.sleep(self.args.ring)
            await self.pc.setLocalDescription(await self.pc.createAnswer())
            await self.send({"type": "answer", "to": self.peer, "callId": self.call_id, "sdp": self.pc.localDescription.sdp})
            self.log("answered")
        elif t == "answer" and msg.get("callId") == self.call_id:
            self.log("call answered by", msg["from"])
            await self.pc.setRemoteDescription(RTCSessionDescription(msg["sdp"], "answer"))
            await self.on_remote_description()
        elif t == "ice" and msg.get("callId") == self.call_id and self.pc:
            if self.remote_set:
                await self.add_candidate(msg)
            else:
                self.pending.append(msg)
        elif t in ("bye", "reject") and msg.get("callId") == self.call_id:
            self.log(f"remote {t}", msg.get("reason", ""))
            self.done.set()

    async def place_call(self):
        self.call_id, self.peer = str(uuid.uuid4()), self.args.target
        self.log("calling", self.peer)
        self.pc = self.new_pc()
        await self.pc.setLocalDescription(await self.pc.createOffer())  # aiortc gathers all candidates into the SDP
        await self.send({"type": "offer", "to": self.peer, "callId": self.call_id, "sdp": self.pc.localDescription.sdp})
        if self.args.cancel:
            async def give_up():
                await asyncio.sleep(self.args.cancel)
                if self.connected_at is None and not self.done.is_set():
                    self.log("giving up (caller hung up while ringing)")
                    await self.send({"type": "bye", "to": self.peer, "callId": self.call_id, "reason": "remote_hangup"})
                    self.done.set()
            asyncio.create_task(give_up())

    async def run(self):
        async with websockets.connect(self.args.server) as ws:
            self.ws = ws
            await self.send({"type": "register", "id": self.args.name})

            async def reader():
                async for raw in ws:
                    await self.handle(json.loads(raw))

            task = asyncio.create_task(reader())
            try:
                await asyncio.wait_for(self.done.wait(), timeout=self.args.timeout)
            except asyncio.TimeoutError:
                self.log("timed out")
            task.cancel()
            if self.pc:
                await self.pc.close()
        self.report()

    def report(self):
        if not self.frames:
            self.log("RESULT: received no audio")
            return
        rate = self.frames[0][0]
        pcm = np.concatenate([f for _, f in self.frames])
        with wave.open(self.args.out, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(rate)
            w.writeframes(pcm.tobytes())
        rms = float(np.sqrt(np.mean(pcm.astype(np.float64) ** 2)))
        self.log(f"RESULT: received {len(pcm) / rate:.1f}s of audio @ {rate} Hz, rms={rms:.1f} -> {self.args.out}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--server", default="ws://127.0.0.1:8080")
    p.add_argument("--name", default="laptop-bot")
    p.add_argument("--mode", choices=["answer", "call"], default="answer")
    p.add_argument("--target", help="who to call in call mode")
    p.add_argument("--ring", type=float, default=2.0)
    p.add_argument("--talk", type=float, default=8.0)
    p.add_argument("--decline", action="store_true")
    p.add_argument("--cancel", type=float, default=0, help="call mode: hang up after N s if not answered")
    p.add_argument("--timeout", type=float, default=120)
    p.add_argument("--out", default="bot_received.wav")
    asyncio.run(Peer(p.parse_args()).run())


if __name__ == "__main__":
    main()
