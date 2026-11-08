"""DEMO_MODE: replay mock/events.json through the bus (shown on WS /events)."""
import asyncio, json, pathlib
from . import bus
MOCK = pathlib.Path(__file__).resolve().parent.parent / "mock" / "events.json"

async def run(only_call=None, speed=1.0, loop=False):
    doc = json.loads(MOCK.read_text())
    while True:
        calls = [c for c in doc["calls"] if only_call in (None, c["call_id"])]
        await asyncio.gather(*[_play(c, speed) for c in calls])
        if not loop:
            return
        await asyncio.sleep(5)

async def _play(call, speed):
    prev = 0.0
    for ev in sorted(call["events"], key=lambda e: e["ts"]):
        if ev["ts"] > prev:
            await asyncio.sleep((ev["ts"] - prev) / max(speed, 0.01)); prev = ev["ts"]
        bus.publish(ev["type"], ev["call_id"], ev["data"])
