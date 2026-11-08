"""Replay mock/events.json caller lines (transcript.caller) through the alert machine and print the s curve + alerts.
  python -m detection.scripts.replay_mock [--real]   (default: rule-only detect, no network; --real uses P2_ENGINE via detect())"""
import asyncio, json, sys
from pathlib import Path
from detection import alert

async def main(real):
    d = json.load(open(Path(__file__).resolve().parents[2] / "mock" / "events.json"))
    for call in d["calls"]:
        out, t = [], [0.0]
        async def emit(ty, cid, data): out.append((ty, data))
        det = None
        if not real:
            from detection import detect as D, schema
            async def det(cid, text, meta, engine): return schema.normalize({**{"s": 0}, **D.rule_scan(text)}, "fallback") if False else D.merge({}, D.rule_scan(text), "fallback")
        m = alert.AlertMachine(emit=emit, detect=det, clock=lambda: t[0])
        print(f"== {call['call_id']}: {call['title']}")
        for ev in call["events"]:
            if ev["type"] == "transcript.caller" and ev["data"].get("is_final", True):
                t[0] += 6; n = len(out)
                await m.on_final(call["call_id"], ev["data"])
                for ty, dd in out[n:]:
                    print(f"  {ty:12s}", f"s={dd['s']:.2f} {dd['band']:8s} asks={dd['asks']}" if ty == "risk.update" else dd)
            elif ev["type"] in ("user.action", "handoff.started", "handoff.restored", "call.ended"):
                await m.on_event({**ev, "call_id": call["call_id"]})
if __name__ == "__main__":
    asyncio.run(main("--real" in sys.argv))
