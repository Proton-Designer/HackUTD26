#!/usr/bin/env python3
"""No-phone end-to-end rehearsal of the P1 demo path (TASK-015). Everything is SIMULATED: simulated caller, no Telnyx, no real audio.
Run:  web/customer/tests/run_e2e.sh      (see README.md). Exit 0 only if every step passes. Gaps are reported as GAP, not hidden."""
import asyncio, base64, importlib.util, json, os, pathlib, re, subprocess, sys, tempfile, threading, time, urllib.request, urllib.error, glob
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[3]
PORT = os.environ.get("E2E_PORT", "8011"); BASE = f"http://127.0.0.1:{PORT}"
SHOTS = pathlib.Path(os.environ.get("E2E_SHOTS") or tempfile.mkdtemp(prefix="backfire-e2e-shots-")); SHOTS.mkdir(parents=True, exist_ok=True)   # temp dir by default; never the live logs/
PIN = os.environ.get("DEVICE_PIN", "424242")
SCAMMER = "+15555550199"          # synthetic 555 number, unlisted
results = []

def check(step, name, ok, detail="", gap=None):
    tag = "PASS" if ok else ("GAP" if gap else "FAIL")
    results.append((step, name, tag, detail, gap)); print(f"[{tag}] {step} {name}" + (f" - {detail}" if detail and not ok else "") + (f"  (owner: {gap})" if tag == "GAP" else ""), flush=True)
    return ok

def _env_token(name):   # the hub (run_hub) loads .env after the shell, so POST /events needs the same PIPELINE_TOKEN; read it quietly, never print it
    v = os.environ.get(name)
    if v: return v
    try:
        for ln in (ROOT / ".env").read_text().splitlines():
            if ln.startswith(name + "="): return ln.split("=", 1)[1].strip().strip("\"'")
    except Exception: pass
    return None
PIPE = _env_token("PIPELINE_TOKEN")
def http(method, path, body=None, headers=None):
    if PIPE and path == "/events" and method == "POST": headers = {"x-pipeline-token": PIPE, **(headers or {})}
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
    env = dict(os.environ, NO_TUNNEL="1", SIM_MODE="1", VOIP_OPEN_TOKEN="1", HUB_PORT=PORT, DEVICE_PIN=PIN, HUB_DB=tempfile.mkdtemp() + "/e2e.db", INTEL_DB=tempfile.mkdtemp() + "/intel.db", LOGDIR=tempfile.mkdtemp(prefix="backfire-e2e-logs-"), HUB_NO_PIN_FILE="1")
    # voip's on_answered reads these with os.environ[...] (KeyError -> no call.answered in SIM_MODE if unset); dummies are harmless, sim never calls Telnyx
    env.setdefault("TELNYX_CRED_CONNECTION_ID", "sim"); env.setdefault("TELNYX_SIP_USER", "sim"); env.setdefault("INTEL_EXTRACT_GRACE", "1")  # intel blocks the caller this long after a decoy call ends (default 20s)
    for k in ("HUB_TOKEN", "PUBLIC_WS"): env.pop(k, None)
    env.update(P3_DECOY_URL="", P3_BASE="", P3_VOICE_URL="", DECOY_STANDIN="echo")   # isolated: never the real decoy from .env; run_hub keeps these explicit values; hub echo stand-in answers the caller leg
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
            # 2b. pairing link /app/?pair=XXXXXX (fresh phone): pairs by itself, the code is stripped from the URL before the reload
            c2 = br.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2); p2 = c2.new_page(); navs = []
            p2.on("request", lambda r: navs.append(r.url) if r.is_navigation_request() else None)
            p2.goto(BASE + "/app/?pair=" + PIN + "&skipsetup&novoip"); p2.wait_for_selector("#phone")
            tok = wait_for(lambda: p2.evaluate("localStorage.getItem('bf.device')"), 8); time.sleep(1.0)
            check("2b", "pairing link pairs automatically (device token stored)", bool(tok))
            check("2b", "pairing link: the code is stripped from the URL (and was gone before the reload)", "pair=" not in p2.url and len(navs) >= 2 and all("pair=" not in u for u in navs[1:]), f"navigations={len(navs)} code_in_url={'pair=' in p2.url}")
            check("2b", "pairing link: app is usable after the reload (no pairing screen)", p2.locator("#pairView").is_hidden() and p2.locator("#callView").is_visible())
            c2.close()
            # 2c. a bad link never leaves the code in the URL and falls back (localhost needs no pairing, so the app carries on)
            c3 = br.new_context(viewport={"width": 375, "height": 667}, device_scale_factor=2); p3 = c3.new_page()
            p3.goto(BASE + "/app/?pair=000000&skipsetup&novoip"); p3.wait_for_selector("#phone"); time.sleep(1.5)
            check("2c", "bad pairing link: code stripped, no token, back to the app", "pair=" not in p3.url and not p3.evaluate("localStorage.getItem('bf.device')") and p3.locator("#callView").is_visible() and p3.locator("#pairView").is_hidden())
            p3.evaluate("BF.onUnauthorized()"); time.sleep(0.3)   # the fallback code box, as a 401 would show it
            fits = p3.evaluate("(() => { const h = document.getElementById('pairTitle'); return h.getBoundingClientRect().height < 1.6 * parseFloat(getComputedStyle(h).lineHeight); })()")
            check("2c", "pairing screen: 'Connect your phone' fits one line at 375 px, Connect waits for 6 digits", fits and p3.inner_text("#pairTitle") == "Connect your phone" and p3.locator("#pairBtn").is_disabled() and p3.locator("#a2hs").is_hidden())
            p3.screenshot(path=str(SHOTS / "02c-pairing-375.png")); c3.close()
            # 3. unlisted number calls in
            call = SimCall(SCAMMER); call.start()
            routed = wait_for(lambda: has("call.routed"))
            check("3", "call.routed LIVE_GUARD for an unlisted caller", bool(routed) and routed["data"]["decision"] == "LIVE_GUARD", json.dumps(routed))
            check("3", "app rings (data-state=ringing)", bool(wait_for(lambda: pg.evaluate("BF.ui()") == "ringing")), pg.evaluate("BF.ui()"))
            check("3", "ring screen shows the number + Scam Likely", re.sub(r"\D","",SCAMMER) in re.sub(r"\D","",pg.inner_text("#callerNumber")) and pg.locator("#scamLabel").is_visible(), pg.inner_text("#callerNumber"))
            check("3", "badge says Live Guard on", "Live Guard on" in pg.inner_text("#guard"), pg.inner_text("#guard"))
            check("3", "ringtone playing while ringing (audio element or Web Audio)", bool(wait_for(lambda: pg.evaluate("!!(BF.ringEl && !BF.ringEl.paused)"), 3)), str(pg.evaluate("BF.ringEl ? BF.ringEl.paused : 'no ringEl'")))
            shot("03-ringing")
            pg.click("#answerBtn"); call.answer()
            check("3", "ringtone stops on answer", bool(wait_for(lambda: pg.evaluate("!BF.ringEl || BF.ringEl.paused"), 3)))
            check("3", "answered: app goes active", bool(wait_for(lambda: pg.evaluate("BF.ui()") == "active")), pg.evaluate("BF.ui()"))
            check("3", "hub emits call.answered (by maria)", bool(wait_for(lambda: has("call.answered"))), json.dumps([e["type"] for e in events if e["call_id"] == call.sid]))
            check("3", "caller audio reaches the hub relay (frames flowing)", bool(wait_for(lambda: getattr(call, "frames_in", 0) > 10)), str(getattr(call, "frames_in", None)))
            shot("03b-active")
            # 4. fake P2: risk.update + alert.fired
            http("POST", "/events", {"type": "risk.update", "call_id": call.sid, "data": {"s": 0.92, "band": "high", "asks": ["gift_card", "secrecy"], "scam_type": "irs", "stage": "payment", "impersonates": "IRS", "addresses_ai_system": False, "why_chips": ["Asks for gift cards", "Claims to be IRS", "Secrecy"], "engine": "local"}})
            http("POST", "/events", {"type": "alert.fired", "call_id": call.sid, "data": {"level": "first", "why_chips": ["Asks for gift cards", "Claims to be IRS", "Secrecy"]}})
            check("4", "alert box shown", bool(wait_for(lambda: pg.locator("#alertBox").is_visible())))
            check("4", "3 why-chips", pg.locator("#chips li").count() == 3, str(pg.locator("#chips li").count()))
            check("4", "3 big buttons (Continue / Fire Back / Hang up)", all(pg.locator(s).is_visible() for s in ("#btnContinue", "#btnGets", "#btnHang")))
            check("4", "two beeps fired (oscillators created)", wait_for(lambda: pg.evaluate("window.__osc") >= 2) is not None and pg.evaluate("window.__osc") >= 2, str(pg.evaluate("window.__osc")))
            check("4", "badge = Scam Likely", "Scam Likely" in pg.inner_text("#guard"), pg.inner_text("#guard"))
            shot("04-alert")
            # 5. Fire Back
            pg.click("#btnGets")
            ua = wait_for(lambda: has("user.action", action="scammer_get_scammed"))
            check("5", "user.action scammer_get_scammed reached the hub (WS /events)", bool(ua))
            ho = wait_for(lambda: has("handoff.started"), 4)
            check("5", "handoff.started emitted after user.action", bool(ho), "no handoff.started within 4s", gap="eng1/eng2: nothing turns user.action=scammer_get_scammed into handoff.started + relay.start_decoy (grep: only ops.py reads handoff.started)")
            time.sleep(1.5)
            check("5", "app shows the handed-off state", "put the phone down" in pg.inner_text("#handoffMsg") and "Handled" in pg.inner_text("#guard"), pg.inner_text("#guard"))
            code, stats = http("GET", "/demo/status?format=json")
            check("5", "echo decoy started and answering the caller leg", getattr(call, "decoy_audio", 0) > 0, f"decoy frames back to caller: {getattr(call, 'decoy_audio', 0)}", gap="eng1/eng2: relay.start_decoy never called (same gap)")
            shot("05-handoff")
            # 6. end call -> blocklist -> second call rejected pre-ring
            call.hangup()
            check("6", "call.ended", bool(wait_for(lambda: has("call.ended"))))
            bl = wait_for(lambda: next((e for e in events if e["type"] == "blocklist.updated" and str(e["data"].get("number", "")).replace("+", "")[-10:] == SCAMMER[-10:]), None), 12)
            check("6", "blocklist.updated for the scammer", bool(bl), "seen: " + json.dumps([e["data"] for e in events if e["type"] == "blocklist.updated"])[:200], gap="follows from the handoff gap above" if not ho else None)
            time.sleep(1.0); shot("06a-ended-summary")
            check("6", "ended screen shows a call summary (duration + Backfire row)", pg.locator("#summary").is_visible() and "Backfire" in pg.inner_text("#summary"), pg.inner_text("#summary") if pg.locator("#summary").count() else "no #summary")
            check("6", "summary says synthetic voice when no voice is enrolled", "synthetic voice" in pg.inner_text("#summary") and "your voice" not in pg.inner_text("#summary"), pg.inner_text("#summary"))
            num = wait_for(lambda: (lambda t: t if t and "Checking" not in t else None)(pg.evaluate("(document.getElementById('sumBlocked')||{}).textContent || ''")), 8)
            check("6", "summary 'Number: Checking...' resolves (Blocked for you / Reported) within ~5 s", num in ("Blocked for you", "Reported"), str(num))
            check("6", "badge reset to Live Guard on after the call", "Live Guard on" in pg.inner_text("#guard"), pg.inner_text("#guard"))
            time.sleep(0.5); pg.evaluate("BF.view('protView')"); time.sleep(0.6); shot("06-protection")
            n_inc = len([e for e in events if e["type"] == "call.incoming"]); before = len(events)
            out = subprocess.run([sys.executable, str(ROOT / "scripts" / "sim_call.py"), "--from", SCAMMER, "--hub", BASE, "--fast"], capture_output=True, text=True, timeout=40, env=dict(os.environ))
            time.sleep(1)
            r2 = [e for e in events[before:] if e["type"] == "call.routed"]
            check("6", "second call from the same number: call.routed BLOCKED_BACKFIRE", bool(r2) and r2[-1]["data"]["decision"] == "BLOCKED_BACKFIRE", json.dumps(r2[-1:] ) , gap="follows from the handoff gap" if not bl else None)
            check("6", "app never rang for the blocked call (rings still 1)", pg.evaluate("window.__rings") == 1, f"rings={pg.evaluate('window.__rings')}", gap="follows from the handoff gap" if not r2 or r2[-1]["data"]["decision"] != "BLOCKED_BACKFIRE" else None)
            shot("06b-blocked")
            # 7. regression (07:45 live bug): a NEW call after a handed-off call must start on the normal call screen, not "Backfire has the call"
            call3 = SimCall("+12145550177"); call3.start()
            check("7", "next call (other number) rings", bool(wait_for(lambda: pg.evaluate("BF.ui()") == "ringing")), pg.evaluate("BF.ui()"))
            pg.click("#answerBtn"); call3.answer()
            wait_for(lambda: pg.evaluate("BF.ui()") == "active"); time.sleep(1.0)
            view = pg.evaluate("document.getElementById('active').dataset.view")
            check("7", "next call does NOT show the previous call's handoff screen", view == "call" and not pg.locator("#handoffMsg").is_visible(), f"view={view} handoffVisible={pg.locator('#handoffMsg').is_visible()}")
            shot("07-next-call")
            call3.hangup()
            wait_for(lambda: pg.evaluate("BF.ui()") == "ended")
            # 8. summary 'Checking...' never sticks: a handed-off call whose block never arrives says 'Reported' after ~5 s (fake events through the app's own handler)
            fake = "e2e-noblock-" + os.urandom(3).hex()
            pg.evaluate("""id => { const t = new Date().toISOString(); for (const [type, data] of [["call.incoming", {from: "+15555550123"}], ["call.routed", {decision: "LIVE_GUARD"}], ["alert.fired", {level: "first", why_chips: ["Asks for gift cards"]}], ["handoff.started", {}], ["call.ended", {ended_by: "caller"}]]) BF.deliver({type, call_id: id, ts: t, data}); }""", fake)
            check("8", "summary shows 'Checking...' right after a call with no block yet", "Checking" in pg.evaluate("(document.getElementById('sumBlocked')||{}).textContent || ''"))
            num2 = wait_for(lambda: (lambda t: t if "Checking" not in t else None)(pg.evaluate("(document.getElementById('sumBlocked')||{}).textContent || ''")), 8)
            check("8", "no blocklist.updated: 'Checking...' falls back to 'Reported' after ~5 s", num2 == "Reported", str(num2))
            shot("08-summary-reported")
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
