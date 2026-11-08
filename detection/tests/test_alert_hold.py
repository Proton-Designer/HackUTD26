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
    r = Rig([("ok", R(0.95)), ("fail", R(0.3)), ("fail", R(0.3)), ("ok", R(0.96))])
    r.say(); r.user("continue"); r.say(); r.say(); r.say()
    assert r.ss() == [0.95, 0.95, 0.95, 0.96] and r.alerts() == ["first"]


def test_real_low_llm_score_still_restores():
    r = Rig([("ok", R(0.95)), ("ok", R(0.1))])
    r.say(); r.say()
    assert r.ss() == [0.95, 0.1]


def test_four_failed_windows_decay():
    r = Rig([("ok", R(0.95))] + [("fail", R(0.3))] * 4)
    for _ in range(5): r.say(dt=1)
    assert r.ss() == [0.95, 0.95, 0.95, 0.95, 0.3]


def test_hold_expires_after_ten_seconds():
    r = Rig([("ok", R(0.95)), ("fail", R(0.0))])
    r.say(); r.say(dt=11)
    assert r.ss() == [0.95, 0.0]


def test_failed_window_without_prior_llm_passes_through():
    r = Rig([("fail", R(0.3))])
    r.say()
    assert r.ss() == [0.3]


def test_rules_clean_failed_windows_hold_only_the_first():
    # normal talk after the scam while both engines fail: first window held, then s restores
    r = Rig([("ok", R(0.95))] + [("fail", R(0.0))] * 3)
    for _ in range(4): r.say(dt=1)
    assert r.ss() == [0.95, 0.95, 0.0, 0.0]


def test_continue_clears_window_so_benign_talk_restores():
    texts = []
    r = Rig([("ok", R(0.95)), ("ok", R(0.0))])
    orig = r.m.detect
    async def spy(cid, text, meta):
        texts.append(text); return await orig(cid, text, meta)
    r.m.detect = spy
    r.say(); r.user("continue"); r.say()
    assert len(texts) == 2 and texts[1].count("\n") == 0 and r.ss() == [0.95, 0.0]


def test_failed_flag_bounded_without_clear():
    D.ENGINE_FAILED.clear()
    for i in range(2100): D._set_failed(f"c{i}", True)
    assert len(D.ENGINE_FAILED) == 2000 and "c2099" in D.ENGINE_FAILED and "c0" not in D.ENGINE_FAILED


def test_continue_mid_flight_drops_stale_result():
    r = Rig([("ok", R(0.95, asks=["gift_cards"])), ("ok", R(0.95, asks=["gift_cards", "otp"]))])
    async def go():
        t = asyncio.create_task(r.m.on_final("c1", {"text": "x"}))
        await asyncio.sleep(0)
        return t
    asyncio.run(r.m.on_final("c1", {"text": "x"}))
    n_before = len(r.ev)
    orig = r.m.detect
    async def slow(cid, text, meta):
        await asyncio.sleep(0.05); return await orig(cid, text, meta)
    r.m.detect = slow
    async def scenario():
        t = asyncio.create_task(r.m.on_final("c1", {"text": "y"}))
        await asyncio.sleep(0.01)
        await r.m.on_event({"type": "user.action", "call_id": "c1", "data": {"action": "continue"}})
        await t
    asyncio.run(scenario())
    assert len(r.ev) == n_before


def test_late_final_of_pre_continue_audio_is_dropped():
    r = Rig([("ok", R(0.95, asks=["gift_cards"])), ("ok", R(0.95, asks=["gift_cards", "otp"]))])
    r.say()
    n = len(r.ev); r.t += 1; t_audio = r.t
    r.user("continue"); r.t += 6                      # STT lagged: the pre-Continue utterance finalizes 6 s later
    asyncio.run(r.m.on_final("c1", {"text": "pay with gift cards", "_t_end": t_audio - 0.5}))
    assert len(r.ev) == n and not r.m.calls["c1"].utts
    asyncio.run(r.m.on_final("c1", {"text": "new line", "_t_end": r.t}))   # audio after Continue still counts
    assert len(r.ev) > n


def _ask_partial(r, t_snap=None):
    u = {"text": "read me the six digit code from your text message", "is_final": False}
    if t_snap is not None:
        u["_t_end"] = t_snap
    n = len(r.ev); asyncio.run(r.m.on_partial("c1", u)); return len(r.ev) - n


def test_late_partial_of_pre_continue_audio_ignored_new_one_fast_paths():
    r = Rig([("ok", R(0.95, asks=["gift_cards"]))])
    r.say()
    t_snap = r.t; r.t += 1
    r.user("continue"); r.t += 6
    lt = r.m.calls["c1"].llm_t
    assert _ask_partial(r, t_snap) == 0 and r.m.calls["c1"].llm_t == lt   # no alert, no anchor update
    assert _ask_partial(r, r.t) > 0                    # NEW hard ask after Continue re-alerts on the fast path


def test_untagged_partial_control_would_realert():
    r = Rig([("ok", R(0.95, asks=["gift_cards"]))])
    r.say(); r.t += 1; r.user("continue"); r.t += 6
    assert _ask_partial(r) > 0                          # positive control: without the tag the same partial fires
