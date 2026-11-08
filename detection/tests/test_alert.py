import asyncio
from detection import alert, schema

def R(s, asks=(), chips=("c",)):
    return {"s": s, "band": schema.band(s), "asks": list(asks), "scam_type": "x", "stage": "pressure", "impersonates": None,
            "addresses_ai_system": False, "why_chips": list(chips) * 1, "engine": "cloud"}

class Rig:
    def __init__(self, scores):
        self.t, self.events, self.scores = 1000.0, [], list(scores)
        self.calls = 0
        async def emit(t, c, d): self.events.append((t, d))
        async def det(cid, text, meta, engine):
            self.calls += 1
            v = self.scores.pop(0)
            if isinstance(v, Exception): raise v
            return v
        self.m = alert.AlertMachine(emit=emit, detect=det, clock=lambda: self.t)
    def say(self, text="x", dt=5):
        self.t += dt; asyncio.run(self.m.on_final("c1", {"text": text}))
    def ev(self, type_, **d): asyncio.run(self.m.on_event({"type": type_, "call_id": "c1", "data": d}))
    def alerts(self): return [d["level"] for t, d in self.events if t == "alert.fired"]

def test_legit_stays_silent():
    r = Rig([R(0.05), R(0.1), R(0.2), R(0.15)])
    for _ in range(4): r.say()
    assert r.alerts() == [] and len([1 for t, _ in r.events if t == "risk.update"]) == 4

def test_scam_exactly_one_first():
    r = Rig([R(0.3), R(0.85), R(0.9), R(0.97)])
    for _ in range(4): r.say()
    assert r.alerts() == ["first"]

def test_hard_ask_with_moderate_s_fires():
    r = Rig([R(0.65, ["gift_card"])]); r.say()
    assert r.alerts() == ["first"]
    r = Rig([R(0.65, ["secrecy"])]); r.say()
    assert r.alerts() == []

def test_chips_max_four():
    r = Rig([R(0.9, chips=list("abcdef"))]); r.say()
    assert len(r.events[-1][1]["why_chips"]) == 4

def test_continue_flat_high_no_realert():
    r = Rig([R(0.85), R(0.86), R(0.9), R(0.9)])
    r.say(); r.ev("user.action", action="continue")
    for _ in range(3): r.say()
    assert r.alerts() == ["first"]

def test_continue_then_critical_one_realert_then_rearm():
    r = Rig([R(0.85), R(0.97), R(0.98), R(0.5), R(0.99)])
    r.say(); r.ev("user.action", action="continue")
    r.say(); r.say()
    assert r.alerts() == ["first", "realert"]
    r.say(); r.say()          # dropped below 0.8, rises to critical again
    assert r.alerts() == ["first", "realert", "realert"]

def test_new_hard_ask_realerts_once():
    r = Rig([R(0.85, ["gift_card"]), R(0.88, ["gift_card", "otp"]), R(0.9, ["gift_card", "otp", "wire"])])
    r.say(); r.ev("user.action", action="continue"); r.say(); r.say()
    assert r.alerts() == ["first", "realert"]

def test_no_realert_without_continue():
    r = Rig([R(0.85), R(0.99)]); r.say(); r.say()
    assert r.alerts() == ["first"]

def test_exception_and_garbage_no_crash():
    r = Rig([RuntimeError("x"), "garbage", {"s": "bad"}, R(0.1)])
    for _ in range(4): r.say()
    assert [t for t, _ in r.events] == ["risk.update"]
    asyncio.run(r.m.on_event({"type": None})); asyncio.run(r.m.on_event({}))

def test_quiet_switch_off_and_not_when_fired():
    r = Rig([R(0.05)] * 3 + [R(0.05)] * 5)
    r.say(dt=1); r.say(dt=100); r.say(dt=100)   # 200 s of normal
    n = r.calls
    r.say(dt=5); assert r.calls == n          # muted: no more /detect
    r2 = Rig([R(0.85), R(0.1), R(0.1), R(0.1)])
    r2.say(); r2.say(dt=100); r2.say(dt=100); r2.say(dt=100)
    assert r2.calls == 4

def test_decoy_scores_but_no_alerts_and_restore_resets():
    r = Rig([R(0.3), R(0.95), R(0.2), R(0.9)])
    r.say(); r.ev("handoff.started"); r.say(); assert r.alerts() == []
    r.say(); r.ev("handoff.restored"); r.say(); assert r.alerts() == ["first"]

def test_call_ended_cleans_up():
    r = Rig([R(0.1)]); r.say(); r.ev("call.ended")
    assert "c1" not in r.m.calls

def test_coalesce_one_in_flight():
    gate = asyncio.Event(); n = {"i": 0, "max": 0, "cur": 0}
    async def det(cid, text, meta, engine):
        n["cur"] += 1; n["max"] = max(n["max"], n["cur"]); n["i"] += 1
        await asyncio.sleep(0.05); n["cur"] -= 1; return R(0.1)
    async def emit(*a): pass
    m = alert.AlertMachine(emit=emit, detect=det)
    async def go():
        await asyncio.gather(*[m.on_final("c", {"text": str(i)}) for i in range(5)])
    asyncio.run(go())
    assert n["max"] == 1 and n["i"] <= 2

def test_fast_path_alerts_before_llm_returns():
    import time
    t0 = {}
    async def emit(t, c, d):
        if t == "alert.fired": t0["alert"] = time.time()
    async def slow(cid, text, meta, engine):
        await asyncio.sleep(0.4); t0["llm"] = time.time(); return R(0.3)
    m = alert.AlertMachine(emit=emit, detect=slow)
    asyncio.run(m.on_final("c", {"text": "You must pay today with gift cards and tell no one"}))
    assert t0["alert"] < t0["llm"] - 0.3          # fired from rule floor, not after the LLM
    # same-window floor: LLM saying 0.3 does not lower the emitted s; the next window scores fresh
    ev = []
    async def emit2(t, c, d): ev.append((t, d))
    m = alert.AlertMachine(emit=emit2, detect=slow)
    asyncio.run(m.on_final("c", {"text": "hello how are you"}))
    assert [d["s"] for t, d in ev if t == "risk.update"] == [0.3]
    assert [d["level"] for t, d in ev if t == "alert.fired"] == []

def test_s_can_fall_after_fast_path():
    r = Rig([R(0.2), R(0.1)])
    r.say("pay with gift cards now")             # fast path fires, llm 0.2 floored to quick s
    r.say("goodbye", dt=100)
    s_vals = [d["s"] for t, d in r.events if t == "risk.update"]
    assert s_vals[-1] == 0.1 and max(s_vals) >= 0.8

def test_partial_fast_path_fires_once_and_final_does_not_double():
    r = Rig([R(0.3)])
    asyncio.run(r.m.on_partial("c1", {"text": "you must pay with gift cards"}))
    assert r.alerts() == ["first"] and r.calls == 0
    r.say("you must pay with gift cards")
    assert r.alerts() == ["first"]

def test_partial_never_raises():
    r = Rig([]); asyncio.run(r.m.on_partial("c1", {})); asyncio.run(r.m.on_partial("c1", {"text": None}))

def test_alert_retried_when_hub_down_then_delivered(monkeypatch):
    """TASK-055 drill 3b: hub POST fails (returns False) around alert.fired -> retried until delivered, exactly one delivered."""
    monkeypatch.setattr(alert, "ALERT_RETRY_EVERY_S", 0.05)
    got, fails = [], [3]
    async def emit(t, c, d):
        if t == "alert.fired":
            if fails[0] > 0: fails[0] -= 1; return False
            got.append(d["level"])
        return True
    async def det(cid, text, meta, engine): return R(0.9)
    async def go():
        m = alert.AlertMachine(emit=emit, detect=det)
        await m.on_final("c1", {"text": "x"}); await asyncio.sleep(0.5)
        return m
    asyncio.run(go())
    assert got == ["first"]

def test_alert_retry_stops_after_call_ended(monkeypatch):
    monkeypatch.setattr(alert, "ALERT_RETRY_EVERY_S", 0.05)
    got = []
    async def emit(t, c, d):
        if t == "alert.fired": got.append(1); return False
        return True
    async def det(cid, text, meta, engine): return R(0.9)
    async def go():
        m = alert.AlertMachine(emit=emit, detect=det)
        await m.on_final("c1", {"text": "x"}); await asyncio.sleep(0.12)
        await m.on_event({"type": "call.ended", "call_id": "c1", "data": {}}); n = len(got); await asyncio.sleep(0.3)
        return n, len(got)
    a, b = asyncio.run(go())
    assert a == b

def test_alert_retry_stops_after_continue(monkeypatch):
    monkeypatch.setattr(alert, "ALERT_RETRY_EVERY_S", 0.05)
    got = []
    async def emit(t, c, d):
        if t == "alert.fired": got.append(1); return False
        return True
    async def det(cid, text, meta, engine): return R(0.9)
    async def go():
        m = alert.AlertMachine(emit=emit, detect=det)
        await m.on_final("c1", {"text": "x"}); await asyncio.sleep(0.12)
        await m.on_event({"type": "user.action", "call_id": "c1", "data": {"action": "continue"}}); n = len(got); await asyncio.sleep(0.3)
        return n, len(got)
    a, b = asyncio.run(go())
    assert a == b and a >= 1
