import asyncio
from detection import alert, detect as D
from detection.tests.test_alert import R


class Rig:
    def __init__(self, scores):
        self.t, self.ev, self.scores = 1000.0, [], list(scores)
        async def emit(t, c, d): self.ev.append((t, d))
        async def det(cid, text, meta, engine):
            kind, r = self.scores.pop(0)
            D.ENGINE_FAILED[cid] = kind == "fail"
            return r
        self.m = alert.AlertMachine(emit=emit, detect=det, clock=lambda: self.t)
    def say(self, dt=3):
        self.t += dt; asyncio.run(self.m.on_final("c1", {"text": "x"}))
    def user(self, a): asyncio.run(self.m.on_event({"type": "user.action", "call_id": "c1", "data": {"action": a}}))
    def alerts(self): return [d["level"] for t, d in self.ev if t == "alert.fired"]
    def ss(self): return [d["s"] for t, d in self.ev if t == "risk.update"]


def test_failed_window_after_critical_no_dip_no_realert():
    r = Rig([("ok", R(0.95)), ("fail", R(0.0)), ("fail", R(0.0)), ("ok", R(0.96))])
    r.say(); r.user("continue"); r.say(); r.say(); r.say()
    assert r.ss() == [0.95, 0.95, 0.95, 0.96] and r.alerts() == ["first"]


def test_real_low_llm_score_still_restores():
    r = Rig([("ok", R(0.95)), ("ok", R(0.1))])
    r.say(); r.say()
    assert r.ss() == [0.95, 0.1]


def test_four_failed_windows_decay():
    r = Rig([("ok", R(0.95))] + [("fail", R(0.0))] * 4)
    for _ in range(5): r.say(dt=1)
    assert r.ss() == [0.95, 0.95, 0.95, 0.95, 0.0]


def test_hold_expires_after_ten_seconds():
    r = Rig([("ok", R(0.95)), ("fail", R(0.0))])
    r.say(); r.say(dt=11)
    assert r.ss() == [0.95, 0.0]


def test_failed_window_without_prior_llm_passes_through():
    r = Rig([("fail", R(0.3))])
    r.say()
    assert r.ss() == [0.3]
