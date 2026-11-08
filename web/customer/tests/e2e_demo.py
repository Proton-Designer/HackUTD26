#!/usr/bin/env python3
"""No-phone end-to-end rehearsal of the P1 demo path (TASK-015). Everything is SIMULATED: simulated caller, no Telnyx, no real audio.
Run:  web/customer/tests/run_e2e.sh      (see README.md). Exit 0 only if every step passes. Gaps are reported as GAP, not hidden."""
import asyncio, base64, importlib.util, json, os, pathlib, re, subprocess, sys, tempfile, threading, time, urllib.request, urllib.error, glob
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[3]
PORT = os.environ.get("E2E_PORT", "8011"); BASE = f"http://127.0.0.1:{PORT}"
SHOTS = ROOT / "logs" / "e2e"; SHOTS.mkdir(parents=True, exist_ok=True)
PIN = os.environ.get("DEVICE_PIN", "424242")
SCAMMER = "+15555550199"          # synthetic 555 number, unlisted
results = []

def check(step, name, ok, detail="", gap=None):
    tag = "PASS" if ok else ("GAP" if gap else "FAIL")
    results.append((step, name, tag, detail, gap)); print(f"[{tag}] {step} {name}" + (f" - {detail}" if detail and not ok else "") + (f"  (owner: {gap})" if tag == "GAP" else ""), flush=True)
    return ok

def http(method, path, body=None, headers=None):
    req = urllib.request.Request(BASE + path, None if body is None else json.dumps(body).encode(), {"content-type": "application/json", **(headers or {})}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=5) as r: raw = r.read().decode(); return r.status, (json.loads(raw) if raw[:1] in "{[" else raw)
    except urllib.error.HTTPError as e: return e.code, {}
    except Exception as e: return None, {"error": str(e)}

# ---- reuse the simulator's own webhook builders (scripts/sim_call.py) ----
spec = importlib.util.spec_from_file_location("sim_call", ROOT / "scripts" / "sim_call.py"); sim = importlib.util.module_from_spec(spec); spec.loader.exec_module(sim)

# ---- hub event listener (a second WS /events client, like the command center) ----
events = []
def listen():
    import websockets
    async def run():
        async with websockets.connect(f"ws://127.0.0.1:{PORT}/events") as ws:
            async for m in ws: events.append(json.loads(m))
    try: asyncio.run(run())
    except Exception: pass
def has(t, **kw): return next((e for e in events if e["type"] == t and all(e["data"].get(k) == v for k, v in kw.items())), None)
def wait_for(fn, secs=6):
    end = time.time() + secs
    while time.time() < end:
        r = fn()
        if r: return r
        time.sleep(0.1)
    return None

# ---- one held-open simulated call (initiated, answered, streaming, media WS kept alive until hangup) ----
class SimCall:
    def __init__(self, frm):
        self.sid = "11111111-0000-4000-8000-" + os.urandom(6).hex(); self.ccid = "v3:sim_" + os.urandom(12).hex(); self.frm = frm; self.stop = False
        self.base = {"call_control_id": self.ccid, "call_session_id": self.sid, "call_leg_id": self.sid, "from": frm, "to": "+15555550100", "connection_id": "sim", "client_state": None}
    def hook(self, et, p): return sim.post(BASE + "/telnyx/webhook", sim.webhook(et, p))
    def start(self):
        st, resp = self.hook("call.initiated", dict(self.base, direction="incoming", state="parked", start_time=sim.now()))
        self.url = resp.get("stream_url"); return st
    def answer(self):
        self.hook("call.answered", dict(self.base, direction="incoming", state="answered")); self.hook("streaming.started", dict(self.base, stream_type="websocket"))
        self.frames_in = 0; self.decoy_audio = 0
        threading.Thread(target=lambda: asyncio.run(self._media()), daemon=True).start()
    async def _media(self):
        import websockets
        if not self.url: return
        audio = sim.pcmu_tone(secs=1.0); frames = [audio[i:i+160] for i in range(0, len(audio), 160)]
        try:
            async with websockets.connect(self.url) as ws:
                sj = lambda o: ws.send(json.dumps(o))
                await sj({"event": "connected", "protocol": "Call", "version": "1.0.0"})
                await sj({"event": "start", "sequence_number": "1", "stream_id": "sim-stream", "start": {"call_control_id": self.ccid, "call_session_id": self.sid, "stream_id": "sim-stream", "tracks": ["inbound"], "media_format": {"encoding": "audio/x-mulaw", "sample_rate": 8000, "channels": 1}}})
                async def reader():
                    async for m in ws:
                        try:
                            if json.loads(m).get("event") == "media": self.decoy_audio += 1   # audio the hub sends back to the caller leg = decoy speaking
                        except ValueError: pass
                rt = asyncio.create_task(reader()); i = 0
                while not self.stop:
                    await sj({"event": "media", "sequence_number": str(i + 2), "stream_id": "sim-stream", "media": {"track": "inbound", "chunk": str(i + 1), "timestamp": str(i * 20), "payload": base64.b64encode(frames[i % len(frames)]).decode()}})
                    i += 1; self.frames_in = i; await asyncio.sleep(0.02)
                await sj({"event": "stop", "sequence_number": str(i + 2), "stream_id": "sim-stream", "stop": {"call_control_id": self.ccid}}); rt.cancel()
        except Exception as e: print("  (media ws ended:", type(e).__name__, ")")
    def hangup(self):
        self.stop = True; time.sleep(0.2); self.hook("call.hangup", dict(self.base, direction="incoming", state="hangup", hangup_cause="normal_clearing", hangup_source="caller"))

def chromium_path():
    for p in sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium-*/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing")), reverse=True): return p
    return None

def main():
    env = dict(os.environ, NO_TUNNEL="1", SIM_MODE="1", VOIP_OPEN_TOKEN="1", HUB_PORT=PORT, DEVICE_PIN=PIN, HUB_DB=tempfile.mkdtemp() + "/e2e.db", INTEL_DB=tempfile.mkdtemp() + "/intel.db")
    # voip's on_answered reads these with os.environ[...] (KeyError -> no call.answered in SIM_MODE if unset); dummies are harmless, sim never calls Telnyx
    env.setdefault("TELNYX_CRED_CONNECTION_ID", "sim"); env.setdefault("TELNYX_SIP_USER", "sim"); env.setdefault("INTEL_EXTRACT_GRACE", "1")  # intel blocks the caller this long after a decoy call ends (default 20s)
    for k in ("HUB_TOKEN", "PUBLIC_WS"): env.pop(k, None)
    hub = subprocess.Popen([str(ROOT / "scripts" / "run_hub")], cwd=ROOT, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    try:
        if not check("1", "hub up (run_hub, NO_TUNNEL SIM_MODE VOIP_OPEN_TOKEN)", wait_for(lambda: http("GET", "/healthz")[0] == 200, 20)): return
        st, status = http("GET", "/demo/status?format=json"); check("1", "voip mounted in the hub (/demo/status)", st == 200 and "voip" in json.dumps(status).lower(), json.dumps(status)[:120])
        check("1", "Maria's app served at /app/", http("GET", "/app/")[0] == 200)
        threading.Thread(target=listen, daemon=True).start(); time.sleep(0.5)
        with sync_playwright() as pw:
            try: br = pw.chromium.launch()
            except Exception: br = pw.chromium.launch(executable_path=chromium_path())
            ctx = br.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2); pg = ctx.new_page()
            pg.add_init_script("""window.__rings = 0; document.addEventListener("DOMContentLoaded", () => new MutationObserver(() => { if (document.getElementById("phone").dataset.state === "ringing") window.__rings++; }).observe(document.getElementById("phone"), {attributes: true, attributeFilter: ["data-state"]})); window.__osc = 0; const o = AudioContext.prototype.createOscillator; AudioContext.prototype.createOscillator = function(){ window.__osc++; return o.apply(this, arguments); };""")
            shot = lambda n: pg.screenshot(path=str(SHOTS / f"{n}.png"))
            pg.goto(BASE + "/app/?skipsetup&novoip"); pg.wait_for_selector("#phone"); time.sleep(0.8)
            # 2. pairing (TASK-014 hub side). Localhost is exempt on the hub, so the screen normally does not show here.
            if not pg.locator("#pairView").is_hidden():
                pg.fill("#pairPin", PIN); pg.click("#pairBtn"); pg.wait_for_load_state(); time.sleep(0.8)
                check("2", "paired with the hub PIN, app works after", pg.locator("#pairView").is_hidden() and bool(pg.evaluate("localStorage.getItem('bf.device')")))
            else:
                code, _ = http("POST", "/pair", {"pin": PIN})
                if code == 404: check("2", "pairing (hub /pair)", False, "POST /pair is 404", gap="eng1 (TASK-014 hub side not landed)")
                else: check("2", "pairing screen not needed on localhost (dev exemption); /pair answers", code in (200, 401), f"/pair -> {code}")
            shot("02-idle")
            # 3. unlisted number calls in
            call = SimCall(SCAMMER); call.start()
            routed = wait_for(lambda: has("call.routed"))
            check("3", "call.routed LIVE_GUARD for an unlisted caller", bool(routed) and routed["data"]["decision"] == "LIVE_GUARD", json.dumps(routed))
            check("3", "app rings (data-state=ringing)", bool(wait_for(lambda: pg.evaluate("BF.ui()") == "ringing")), pg.evaluate("BF.ui()"))
            check("3", "ring screen shows the number + Scam Likely", SCAMMER in pg.inner_text("#callerNumber") and pg.locator("#scamLabel").is_visible(), pg.inner_text("#callerNumber"))
            check("3", "badge says Live Guard on", "Live Guard on" in pg.inner_text("#guard"), pg.inner_text("#guard"))
            shot("03-ringing")
            pg.click("#answerBtn"); call.answer()
            check("3", "answered: app goes active", bool(wait_for(lambda: pg.evaluate("BF.ui()") == "active")), pg.evaluate("BF.ui()"))
            check("3", "hub emits call.answered (by maria)", bool(wait_for(lambda: has("call.answered"))), json.dumps([e["type"] for e in events if e["call_id"] == call.sid]))
            check("3", "caller audio reaches the hub relay (frames flowing)", bool(wait_for(lambda: getattr(call, "frames_in", 0) > 10)), str(getattr(call, "frames_in", None)))
            shot("03b-active")
            # 4. fake P2: risk.update + alert.fired
            http("POST", "/events", {"type": "risk.update", "call_id": call.sid, "data": {"s": 0.92, "band": "high", "asks": ["gift_card", "secrecy"], "scam_type": "irs", "stage": "payment", "impersonates": "IRS", "addresses_ai_system": False, "why_chips": ["Asks for gift cards", "Claims to be IRS", "Secrecy"], "engine": "local"}})
            http("POST", "/events", {"type": "alert.fired", "call_id": call.sid, "data": {"level": "first", "why_chips": ["Asks for gift cards", "Claims to be IRS", "Secrecy"]}})
            check("4", "alert box shown", bool(wait_for(lambda: pg.locator("#alertBox").is_visible())))
            check("4", "3 why-chips", pg.locator("#chips li").count() == 3, str(pg.locator("#chips li").count()))
            check("4", "3 big buttons (Continue / Scammer Get Scammed / Hang up)", all(pg.locator(s).is_visible() for s in ("#btnContinue", "#btnGets", "#btnHang")))
            check("4", "two beeps fired (oscillators created)", wait_for(lambda: pg.evaluate("window.__osc") >= 2) is not None and pg.evaluate("window.__osc") >= 2, str(pg.evaluate("window.__osc")))
            check("4", "badge = Possible scam", "Possible scam" in pg.inner_text("#guard"), pg.inner_text("#guard"))
            shot("04-alert")
            # 5. Scammer Get Scammed
            pg.click("#btnGets")
            ua = wait_for(lambda: has("user.action", action="scammer_get_scammed"))
            check("5", "user.action scammer_get_scammed reached the hub (WS /events)", bool(ua))
            ho = wait_for(lambda: has("handoff.started"), 4)
            check("5", "handoff.started emitted after user.action", bool(ho), "no handoff.started within 4s", gap="eng1/eng2: nothing turns user.action=scammer_get_scammed into handoff.started + relay.start_decoy (grep: only ops.py reads handoff.started)")
            time.sleep(1.5)
            check("5", "app shows the handed-off state", "We've got it" in pg.inner_text("#handoffMsg") and "Handled" in pg.inner_text("#guard"), pg.inner_text("#guard"))
            code, stats = http("GET", "/demo/status?format=json")
            check("5", "echo decoy started and answering the caller leg", getattr(call, "decoy_audio", 0) > 0, f"decoy frames back to caller: {getattr(call, 'decoy_audio', 0)}", gap="eng1/eng2: relay.start_decoy never called (same gap)")
            shot("05-handoff")
            # 6. end call -> blocklist -> second call rejected pre-ring
            call.hangup()
            check("6", "call.ended", bool(wait_for(lambda: has("call.ended"))))
            bl = wait_for(lambda: next((e for e in events if e["type"] == "blocklist.updated" and str(e["data"].get("number", "")).replace("+", "")[-10:] == SCAMMER[-10:]), None), 12)
            check("6", "blocklist.updated for the scammer", bool(bl), "seen: " + json.dumps([e["data"] for e in events if e["type"] == "blocklist.updated"])[:200], gap="follows from the handoff gap above" if not ho else None)
            time.sleep(0.5); pg.evaluate("BF.view('protView')"); time.sleep(0.6); shot("06-protection")
            n_inc = len([e for e in events if e["type"] == "call.incoming"]); before = len(events)
            out = subprocess.run([sys.executable, str(ROOT / "scripts" / "sim_call.py"), "--from", SCAMMER, "--hub", BASE, "--fast"], capture_output=True, text=True, timeout=40, env=dict(os.environ))
            time.sleep(1)
            r2 = [e for e in events[before:] if e["type"] == "call.routed"]
            check("6", "second call from the same number: call.routed BLOCKED_BACKFIRE", bool(r2) and r2[-1]["data"]["decision"] == "BLOCKED_BACKFIRE", json.dumps(r2[-1:] ) , gap="follows from the handoff gap" if not bl else None)
            check("6", "app never rang for the blocked call (rings still 1)", pg.evaluate("window.__rings") == 1, f"rings={pg.evaluate('window.__rings')}", gap="follows from the handoff gap" if not r2 or r2[-1]["data"]["decision"] != "BLOCKED_BACKFIRE" else None)
            shot("06b-blocked")
            br.close()
    finally:
        try: os.killpg(hub.pid, 15)
        except Exception: pass
    bad = [r for r in results if r[2] != "PASS"]
    print("\n=== E2E SUMMARY:", len(results) - len(bad), "pass,", len([r for r in bad if r[2] == "GAP"]), "gap,", len([r for r in bad if r[2] == "FAIL"]), "fail ===")
    for s, n, t, d, g in bad: print(f"  {t} step {s}: {n}" + (f" -> {g}" if g else ""))
    print("screenshots:", SHOTS); return 0 if not bad else 1

if __name__ == "__main__":
    sys.exit(main() or 0)
