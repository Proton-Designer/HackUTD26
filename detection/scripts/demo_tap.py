"""Auto-tap for the local demo: on alert.fired, POST /user/action scammer_get_scammed (what Maria's button does). Loopback only, synthetic call."""
import asyncio, json, sys, urllib.request
import websockets

HUB = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8200"
DELAY = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0

async def main():
    async with websockets.connect(HUB.replace("http", "ws", 1) + "/events") as ws:
        async for m in ws:
            e = json.loads(m)
            if e.get("type") == "alert.fired":
                await asyncio.sleep(DELAY)
                r = urllib.request.Request(HUB + "/user/action", json.dumps({"call_id": e["call_id"], "action": "scammer_get_scammed"}).encode(),
                                           {"content-type": "application/json"})
                try: print("auto-tap scammer_get_scammed:", urllib.request.urlopen(r, timeout=5).status, flush=True)
                except Exception as ex: print("auto-tap failed:", ex, flush=True)
                return
asyncio.run(main())
