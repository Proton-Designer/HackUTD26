"""TASK-055: judging-day failure drills on a PRIVATE stack (hub :8190 + P2 :ACC_P2_PORT, own procs only, SYNTHETIC audio).
Usage: ACC_P2_PORT=8102 drills.py [1a 1b 2 3a 3b 4]   Results print as lines 'DRILL name | alert | gap | healthz | note' and go to the --out json.
Reuses acceptance.Loop. Drills that reach llama (2) wait for :8100 active_stt_sockets==0 first (RULES-CARD llama guard)."""
import asyncio, json, os, signal, subprocess, sys, time
os.environ.setdefault("ACC_P2_PORT", "8102")
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import acceptance as A
import httpx

WAV = str(A.ACC / "irs.wav")

def guard():
    """llama guard: wait while the live service has an STT socket open."""
    while True:
        try:
            n = httpx.get("http://localhost:8100/healthz", timeout=3).json().get("active_stt_sockets", 0)
        except Exception: n = 0
        if not n: return
        print("live call active, pausing", flush=True); time.sleep(5)

async def hz(l):
    try: return (await l.h.get(f"http://localhost:{A.P2}/healthz")).json()
    except Exception as e: return {"error": type(e).__name__}

def brief(j):
    e, s = j.get("engines", {}), j.get("stt", {})
    return {"local_reachable": e.get("local_reachable"), "failovers": e.get("failovers"), "stt_fail": s.get("primary_failures"),
            "stt_bypassed": s.get("primary_bypassed"), "hub_sub": j.get("hub_subscriber_connected"), "breaker": j.get("cloud_breaker"), "last_error": j.get("last_error")}

def summarize(l, cid, t0, ends):
    ask_end = t0 + ends[1]
    al = [e for e in l.ev(cid, "alert.fired")]
    fin = [e for e in l.ev(cid, "transcript.caller") if e["data"].get("is_final")]
    eng = sorted({e["data"].get("engine") for e in l.ev(cid, "risk.update")} - {None})
    return {"alerts": len(al), "gap_s": round(al[0]["_t"] - ask_end, 2) if al else None, "finals": len(fin), "engines": eng,
            "max_s": A.smax(l.ev(cid, "risk.update"))}

async def drill(name, engine, env=None, mid=None):
    """env: os.environ overrides for the P2 under test. mid(l, cid, t0, ends): async hook run during the call."""
    saved = {k: os.environ.get(k) for k in (env or {})}
    os.environ.update(env or {})
    cid = "drill_" + name
    l = A.Loop(engine, [cid, cid + "_2"]); out = {}
    try:
        await l.start(); ends = A.utt_ends(WAV); t0 = time.time()
        task = asyncio.create_task(l.run_call(cid, WAV))
        extra = await mid(l, cid, t0, ends) if mid else None
        await task
        out = summarize(l, cid, t0, ends); out["healthz_after"] = brief(await hz(l)); out["extra"] = extra
    finally:
        await l.stop()
        for k, v in saved.items():
            if v is None: os.environ.pop(k, None)
            else: os.environ[k] = v
    print("DRILL", name, json.dumps(out), flush=True)
    return out

async def snap(l, delay):
    await asyncio.sleep(delay); return brief(await hz(l))

async def mid_snap(l, cid, t0, ends):
    return {"healthz_mid": await snap(l, ends[0] + 1)}

async def mid_hub_drop(l, cid, t0, ends, down_at, up_at):
    """kill the hub (own pgid), restart on the same port + DB at up_at; re-attach the recorder."""
    await asyncio.sleep(max(0, t0 + down_at - time.time()))
    os.killpg(l.procs[0].pid, signal.SIGKILL); l.procs[0].wait(); l.lt.cancel(); n0 = len(l.events)
    sub_down = await snap(l, 3)
    await asyncio.sleep(max(0, t0 + up_at - time.time()))
    l.procs[0] = subprocess.Popen([A.PY, "-c", A.hub_boot([])], cwd=A.ROOT, env=l.env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    for _ in range(60):
        try:
            if (await l.h.get(f"http://localhost:{A.HUB}/healthz")).status_code == 200: break
        except Exception: pass
        await asyncio.sleep(0.25)
    async def listen():
        import websockets
        async with websockets.connect(f"ws://localhost:{A.HUB}/events") as ws:
            async for m in ws:
                e = json.loads(m); e["_t"] = time.time(); l.events.append(e)
    l.lt = asyncio.create_task(listen()); t_up = time.time()
    await asyncio.sleep(20)
    return {"healthz_hub_down": sub_down, "healthz_20s_after_restart": await snap(l, 0), "hub_down_s": round(up_at - down_at, 1),
            "events_seen_after_restart": len(l.events) - n0}

async def d4(name="4"):
    """P2 killed mid-call (own pgid), call 2 streams to a restarted P2."""
    cid = "drill_4"; l = A.Loop("local", [cid, cid + "_2"]); out = {}
    try:
        await l.start(); ends = A.utt_ends(WAV); t0 = time.time()
        task = asyncio.create_task(l.run_call(cid, WAV))
        await asyncio.sleep(ends[0] + 1.0)
        os.killpg(l.procs[1].pid, signal.SIGKILL); l.procs[1].wait(); tk = time.time()
        hub_ok = (await l.h.get(f"http://localhost:{A.HUB}/healthz")).status_code
        await task
        out = summarize(l, cid, t0, ends); out["hub_healthz_with_p2_dead"] = hub_ok
        t_rs = time.time()
        l.procs[1] = subprocess.Popen([A.PY, "-m", "uvicorn", "detection.app:app", "--port", str(A.P2)], cwd=A.ROOT, env=l.env, stdout=l.log, stderr=subprocess.STDOUT, start_new_session=True)
        for _ in range(120):
            try:
                if (await l.h.get(f"http://localhost:{A.P2}/healthz")).status_code == 200: break
            except Exception: pass
            await asyncio.sleep(0.25)
        out["restart_to_healthz_s"] = round(time.time() - t_rs, 1); await asyncio.sleep(3)
        out["healthz_after_restart"] = brief(await hz(l)); t1 = time.time()
        await l.run_call(cid + "_2", WAV)
        r2 = summarize(l, cid + "_2", t1, ends); out["call2_after_restart"] = r2
    finally:
        await l.stop()
    print("DRILL 4", json.dumps(out), flush=True); return out

async def main():
    want = sys.argv[1:] or ["1a", "1b", "3a", "3b", "4", "2"]
    res = {}
    for w in want:
        if w == "1a": res[w] = await drill("1a", "local", {"LOCAL_LLM_URL": "http://127.0.0.1:9"}, mid_snap)   # llama dead, cloud ok
        elif w == "1b": res[w] = await drill("1b", "local", {"LOCAL_LLM_URL": "http://127.0.0.1:9", "NVIDIA_BASE_URL": "http://127.0.0.1:9/v1"}, mid_snap)  # both dead: rules floor
        elif w == "2": guard(); res[w] = await drill("2", "local", {"RIVA_URI": "127.0.0.1:9", "NVIDIA_BASE_URL": "http://127.0.0.1:9/v1"}, mid_snap)  # Riva+cloud refuse (429 stand-in)
        elif w == "3a": res[w] = await drill("3a", "local", {"LOCAL_LLM_URL": "http://127.0.0.1:9"}, lambda l, c, t, e: mid_hub_drop(l, c, t, e, 1.0, e[0] + 1.5))
        elif w == "3b": res[w] = await drill("3b", "local", {"LOCAL_LLM_URL": "http://127.0.0.1:9"}, lambda l, c, t, e: mid_hub_drop(l, c, t, e, e[1] - 2.5, e[1] + 6.0))
        elif w == "4": res[w] = await d4()
        await asyncio.sleep(60 if w in ("1a", "2") else 10)   # shared-key gap
    Path(os.environ.get("DRILLS_OUT", "/tmp/drills.json")).write_text(json.dumps(res, indent=1))

if __name__ == "__main__":
    asyncio.run(main())
