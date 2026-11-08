import asyncio, base64, json
import websockets
from fastapi.testclient import TestClient
from server import relay
from server.main import app

def fr(i, track="inbound"):
    return {"event": "media", "media": {"track": track, "chunk": str(i), "timestamp": str(i * 20), "payload": base64.b64encode(bytes([i % 256]) * 160).decode()}}

async def _server(handler):
    srv = await websockets.serve(handler, "127.0.0.1", 0)
    return srv, srv.sockets[0].getsockname()[1]

def run(coro):
    return asyncio.run(coro)

def test_p2_always_p3_after_handoff_and_echo_back(monkeypatch):
    async def go():
        p2, p3 = [], []
        async def h2(ws):
            async for m in ws: p2.append(json.loads(m))
        async def h3(ws):
            async for m in ws:
                d = json.loads(m); p3.append(d)
                if d["event"] == "media":
                    await ws.send(json.dumps({"event": "media", "media": {"payload": d["media"]["payload"]}}))
                    await ws.send(json.dumps({"event": "mark", "mark": {"name": "m"}}))
        s2, port2 = await _server(h2); s3, port3 = await _server(h3)
        monkeypatch.setenv("P2_STT_URL", f"ws://127.0.0.1:{port2}"); monkeypatch.setenv("P3_DECOY_URL", f"ws://127.0.0.1:{port3}")
        back = []
        async def to_caller(f): back.append(f)
        await relay.open("c1", to_caller)
        await relay.caller_frame("c1", {"event": "connected"})
        await relay.caller_frame("c1", {"event": "start", "stream_id": "S1", "start": {}})
        for i in range(1, 6): await relay.caller_frame("c1", fr(i))
        await asyncio.sleep(0.2)
        assert [m["event"] for m in p2] == ["connected", "start"] + ["media"] * 5 and p3 == []   # P2 always, P3 not yet
        await relay.caller_frame("c1", fr(99, track="outbound"))  # never enters
        assert await relay.start_decoy("c1")
        for i in range(6, 9): await relay.caller_frame("c1", fr(i))
        await asyncio.sleep(0.3)
        assert [m["event"] for m in p3][:2] == ["connected", "start"] and p3[1]["stream_id"] == "S1"
        assert [m["event"] for m in p3[2:]] == ["media"] * 3          # only caller media after handoff
        assert [b["event"] for b in back].count("media") == 3 and any(b["event"] == "mark" for b in back)
        assert len([m for m in p2 if m["event"] == "media"]) == 8      # still fanned to P2 (outbound dropped)
        await relay.close("c1"); s2.close(); s3.close()
    run(go())

def test_p3_crash_and_p2_down_fail_open(monkeypatch):
    async def go():
        lost = []
        async def h3(ws):
            await ws.recv(); await ws.recv(); await ws.close()   # crash right after handshake
        s3, port3 = await _server(h3)
        monkeypatch.setenv("P3_DECOY_URL", f"ws://127.0.0.1:{port3}"); monkeypatch.setenv("P2_STT_URL", "ws://127.0.0.1:1")  # P2 unreachable
        async def to_caller(f): pass
        await relay.open("c2", to_caller, on_decoy_lost=lambda cid: lost.append(cid))
        assert await relay.start_decoy("c2")
        for i in range(30):
            await relay.caller_frame("c2", fr(i)); await asyncio.sleep(0.01)   # must never raise
        await asyncio.sleep(0.3)
        assert lost == ["c2"] and relay.stats("c2")["decoy_active"] is False
        await relay.close("c2"); s3.close()
        monkeypatch.setenv("P3_DECOY_URL", "ws://127.0.0.1:1"); monkeypatch.setenv("HUB_PORT", "1")   # P3 AND the stand-in fallback unreachable
        await relay.open("c3", to_caller); assert await relay.start_decoy("c3") is False; await relay.close("c3")
        await relay.caller_frame("nope", fr(1))  # unknown call: no raise
    run(go())

def test_builtin_echo_decoy():
    c = TestClient(app)
    with c.websocket_connect("/decoy-echo/x") as ws:
        ws.send_text(json.dumps(fr(1)))
        assert json.loads(ws.receive_text())["media"]["payload"] == fr(1)["media"]["payload"]


def test_p2_gets_pipeline_token_header_only_when_set(monkeypatch):
    async def go(tok):
        seen = []
        async def h2(ws):
            seen.append(ws.request.headers.get("x-pipeline-token"))
            async for m in ws: pass
        s2, port2 = await _server(h2)
        monkeypatch.setenv("P2_STT_URL", f"ws://127.0.0.1:{port2}")
        if tok: monkeypatch.setenv("PIPELINE_TOKEN", tok)
        else: monkeypatch.delenv("PIPELINE_TOKEN", raising=False)
        async def to_caller(f): pass
        await relay.open("ct", to_caller)
        await relay.caller_frame("ct", {"event": "connected"})
        await relay.caller_frame("ct", {"event": "start", "stream_id": "S", "start": {}})
        await relay.caller_frame("ct", fr(1))
        await asyncio.sleep(0.2)
        await relay.close("ct"); s2.close()
        return seen
    assert run(go("s3cret")) == ["s3cret"]
    assert run(go(None)) == [None]

def test_p2_token_never_in_url_or_plaintext_remote(monkeypatch):
    async def go():
        monkeypatch.setenv("PIPELINE_TOKEN", "tok")
        for url in ("ws://203.0.113.5:9/stt/x",):
            try: await relay._connect_p2(url); return "connected"
            except ConnectionError as e: assert "tok" not in str(e) and "wss" in str(e)
        def nohdr(url): return None          # signature without a headers kwarg
        monkeypatch.setattr(websockets, "connect", nohdr)
        try: await relay._connect_p2("wss://p2.example.com/stt/x"); return "connected"
        except ConnectionError as e: assert "URL" in str(e) and "tok" not in str(e)
        return "refused"
    assert run(go()) == "refused"


def test_p2_connect_and_close_logged_with_frames_sent(monkeypatch, caplog):
    import logging
    async def go(url):
        async def h2(ws):
            async for m in ws: pass
        s2, port2 = await _server(h2)
        monkeypatch.setenv("P2_STT_URL", url.format(port=port2))
        monkeypatch.delenv("PIPELINE_TOKEN", raising=False)
        async def to_caller(f): pass
        await relay.open("c9abcdefgh", to_caller)
        await relay.caller_frame("c9abcdefgh", {"event": "connected"})
        await relay.caller_frame("c9abcdefgh", {"event": "start", "stream_id": "S", "start": {}})
        for i in range(1, 4): await relay.caller_frame("c9abcdefgh", fr(i))
        await asyncio.sleep(0.2)
        await relay.close("c9abcdefgh"); s2.close()
    with caplog.at_level(logging.WARNING, logger="hub.relay"):
        run(go("ws://127.0.0.1:{port}"))
    msgs = [r.getMessage() for r in caplog.records]
    assert "P2 connected call=c9abcdef" in msgs
    assert any(m.startswith("P2 closed call=c9abcdef frames_sent=5 connected=True") for m in msgs)
    caplog.clear()
    with caplog.at_level(logging.WARNING, logger="hub.relay"):
        run(go("ws://127.0.0.1:1"))      # never connects
    assert any("frames_sent=0 connected=False" in r.getMessage() for r in caplog.records)


def lw(c, path, headers=None, **kw):
    """Loopback WS client as a browser/tool on the hub machine sees it (TestClient always sends Host: testserver, so set it)."""
    return c.websocket_connect(path, headers={"host": "127.0.0.1:8000", **(headers or {})}, **kw)

def test_listen_fans_out_caller_and_decoy_tagged_and_is_gated(monkeypatch):
    from server import device
    c = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    remote = TestClient(app)
    from server import bus
    bus.publish("call.incoming", "L1", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})   # call known to the hub
    async def go_decoy():
        async def h3(ws):
            async for m in ws:
                d = json.loads(m)
                if d["event"] == "media":
                    await ws.send(json.dumps({"event": "media", "media": {"payload": "REVDT1k="}}))
        s3, port3 = await _server(h3)
        monkeypatch.setenv("P3_DECOY_URL", f"ws://127.0.0.1:{port3}"); monkeypatch.delenv("P2_STT_URL", raising=False)
        async def back(f): pass
        await relay.open("L1", back)
        await relay.caller_frame("L1", {"event": "start", "stream_id": "S", "start": {}})
        await relay.start_decoy("L1")
        await relay.caller_frame("L1", fr(1))
        await asyncio.sleep(0.3)
        await relay.close("L1"); s3.close()
    # remote without a token: refused; with a bad token: refused
    import pytest
    for kw in ({}, {"headers": {"x-device-token": "nope"}}):
        with pytest.raises(Exception):
            with remote.websocket_connect("/listen/L1", **kw): pass
    # fan-out: use the loop that runs the TestClient portal
    with lw(c, "/listen/L1") as ws:
        relay._fan("L1", "caller", fr(7)); relay._fan("L1", "decoy", {"event": "media", "media": {"payload": "REVDT1k="}})
        relay._fan("L1", "caller", {"event": "media", "media": {}})          # no payload: ignored
        a, b = json.loads(ws.receive_text()), json.loads(ws.receive_text())
        assert a == {"track": "caller", "payload": fr(7)["media"]["payload"]}   # exactly {track, payload}: nothing else leaves the hub
        assert b == {"track": "decoy", "payload": "REVDT1k="}
    assert relay.listener_count() == 0                                        # cleaned up on disconnect
    # paired device via subprotocol (browser path)
    tok = remote.post("/pair", json={"pin": device.PIN}).json()["device_token"]
    # cross-site hijack: loopback client but a foreign page Origin (or rebinding Host) is refused; same-origin page and no-Origin tools are fine
    for hdr in ({"origin": "https://evil.example"}, {"origin": "http://127.0.0.1:9999"}):
        with pytest.raises(Exception):
            with lw(c, "/listen/L1", headers=hdr): pass
    with lw(c, "/listen/L1", headers={"origin": "http://127.0.0.1:8000"}): pass
    rebind = TestClient(app, base_url="http://evil.example:8000", client=("127.0.0.1", 5000))
    with pytest.raises(Exception):
        with rebind.websocket_connect("/listen/L1", headers={"host": "evil.example:8000", "origin": "http://evil.example:8000"}): pass
    with pytest.raises(Exception):                                            # unknown call id: refused (no slot squatting)
        with lw(c, "/listen/never-seen-call"): pass
    with remote.websocket_connect("/listen/L1", subprotocols=["bf-device", tok]) as ws:
        assert ws.accepted_subprotocol == "bf-device"                         # token itself is never echoed
        relay._fan("L1", "caller", fr(2)); assert json.loads(ws.receive_text())["track"] == "caller"
    with pytest.raises(Exception):                                            # token without the bf-device marker, or a wrong token
        with remote.websocket_connect("/listen/L1", subprotocols=[tok]): pass
    with pytest.raises(Exception):
        with remote.websocket_connect("/listen/L1", subprotocols=["bf-device", "wrong"]): pass
    lq = asyncio.Queue(50); relay._LQ["L1"] = {lq}                              # real relay path: caller frame in, decoy frame back
    run(go_decoy()); relay._LQ.pop("L1")
    got = []
    while not lq.empty():
        m = lq.get_nowait()
        if m is not None: got.append(json.loads(m))     # None = end-of-call sentinel from relay.close
    assert {"track": "caller", "payload": fr(1)["media"]["payload"]} in got and {"track": "decoy", "payload": "REVDT1k="} in got

def test_listen_max_three_and_slow_drop(monkeypatch):
    c = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    from server import bus
    bus.publish("call.incoming", "L2", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    from contextlib import ExitStack
    with ExitStack() as st:
        for _ in range(3): st.enter_context(lw(c, "/listen/L2"))
        assert relay.listener_count() == 3
        import pytest
        with pytest.raises(Exception):
            with lw(c, "/listen/L2"): pass                      # 4th refused
    assert relay.listener_count() == 0
    # a full per-listener queue drops frames instead of blocking the relay
    q = asyncio.Queue(2); relay._LQ["L3"] = {q}
    for i in range(10): relay._fan("L3", "caller", fr(i))
    assert q.qsize() == 2
    relay._LQ.pop("L3")


def test_listener_released_when_session_closes():
    c = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    async def go():
        async def back(f): pass
        await relay.open("L9", back)
        with lw(c, "/listen/L9"):
            assert relay.listener_count() == 1
            await relay.close("L9")
            await asyncio.sleep(0.8)                  # listener loop sees the end-of-call sentinel and exits
            assert relay.listener_count() == 0
    run(go())


def test_listen_live_call_paired_device_from_call_incoming_on():
    """A live (non-sim) call: a paired remote device may attach as soon as call.incoming is on the bus, before any media stream opens."""
    import pytest
    from server import bus, device
    remote = TestClient(app)
    tok = remote.post("/pair", json={"pin": device.PIN}).json()["device_token"]
    with pytest.raises(Exception):                                            # nothing on the bus yet: unknown call refused
        with remote.websocket_connect("/listen/LIVE1", subprotocols=["bf-device", tok]): pass
    bus.publish("call.incoming", "LIVE1", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    assert "LIVE1" not in relay._S                                            # no relay session / media yet
    with remote.websocket_connect("/listen/LIVE1", subprotocols=["bf-device", tok]) as ws:
        assert ws.accepted_subprotocol == "bf-device"
        assert relay.listener_count() == 1
    assert relay.listener_count() == 0


def _talk_setup(monkeypatch, enabled=True):
    from voip import router as V
    got = []
    async def inject(cid, b64):
        got.append((cid, b64)); return True
    monkeypatch.setattr(V, "talk_enabled", lambda cid: enabled, raising=False)
    monkeypatch.setattr(V, "inject_maria", inject, raising=False)
    from server import bus
    bus.publish("call.incoming", "T1", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    relay._TALKERS.clear()
    return got


def test_talk_auth_one_talker_and_frames_reach_voip(monkeypatch):
    import base64, json, pytest
    from server import device
    got = _talk_setup(monkeypatch)
    f = base64.b64encode(b"\xff" * 160).decode()
    remote = TestClient(app)
    with pytest.raises(Exception):
        with remote.websocket_connect("/talk/T1"): pass                                  # no token
    tok = remote.post("/pair", json={"pin": device.PIN}).json()["device_token"]
    c = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    with remote.websocket_connect("/talk/T1", subprotocols=["bf-device", tok]) as ws:
        assert ws.accepted_subprotocol == "bf-device"
        tok2 = remote.post("/pair", json={"pin": device.PIN}).json()["device_token"]       # a DIFFERENT device
        with pytest.raises(Exception):                                                    # second talker (other device) refused
            with remote.websocket_connect("/talk/T1", subprotocols=["bf-device", tok2]): pass
        ws.send_text(json.dumps({"payload": f}))
        ws.send_bytes(b"\xff" * 160)                                                      # binary 20 ms frame
        ws.send_text(json.dumps({"payload": base64.b64encode(b"\xff" * 960).decode()}))   # 6 frames in one message
        ws.send_text(json.dumps({"payload": base64.b64encode(b"\xff" * 100).decode()}))   # not a 20 ms multiple: dropped
        ws.send_text("not json"); ws.send_text(json.dumps({"payload": "!!"}))
    import time; time.sleep(0.2)
    assert [g[0] for g in got] == ["T1"] * 3 and got[0][1] == f
    assert "T1" not in relay._TALKERS
    with pytest.raises(Exception):
        with lw(c, "/talk/never-seen"): pass                                              # unknown call


def test_talk_refused_when_voip_says_not_enabled_and_rate_limited(monkeypatch):
    import base64, json, pytest, time
    got = _talk_setup(monkeypatch, enabled=False)
    c = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    with pytest.raises(Exception):
        with lw(c, "/talk/T1"): pass
    got2 = _talk_setup(monkeypatch, enabled=True)
    f = json.dumps({"payload": base64.b64encode(b"\xff" * 160).decode()})
    with lw(c, "/talk/T1") as ws:
        for _ in range(200): ws.send_text(f)                                              # burst far above 60 frames/s
    time.sleep(0.3)
    assert 55 <= len(got2) <= 80, len(got2)


def test_talk_frames_dropped_while_decoy_active(monkeypatch):
    import base64, json, time
    from server import bus
    got = _talk_setup(monkeypatch)
    bus.publish("handoff.started", "T1", {})
    c = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    f = json.dumps({"payload": base64.b64encode(b"\xff" * 160).decode()})
    with lw(c, "/talk/T1") as ws:
        for _ in range(5): ws.send_text(f)
    time.sleep(0.2)
    assert got == []
    bus.publish("handoff.restored", "T1", {})
    with lw(c, "/talk/T1") as ws:
        ws.send_text(f)
    time.sleep(0.2)
    assert len(got) == 1


def test_talk_reconnect_from_same_device_replaces_old_socket(monkeypatch):
    import base64, json, time
    from server import device
    got = _talk_setup(monkeypatch)
    f = json.dumps({"payload": base64.b64encode(b"\xff" * 160).decode()})
    remote = TestClient(app)
    tok = remote.post("/pair", json={"pin": device.PIN}).json()["device_token"]
    with remote.websocket_connect("/talk/T1", subprotocols=["bf-device", tok]) as old:
        old.send_text(f)
        with remote.websocket_connect("/talk/T1", subprotocols=["bf-device", tok]) as new:   # same device: replaces, not refused
            time.sleep(0.2)
            new.send_text(f); new.send_text(f)
            time.sleep(0.3)
            msg = old.receive()
            assert msg["type"] == "websocket.close" and msg["code"] == 1000                  # old socket closed with 1000
    time.sleep(0.2)
    assert len(got) == 3 and not relay._TALKERS


def test_listen_reconnect_from_same_device_replaces_and_frees_slot(monkeypatch):
    import time, pytest
    from server import bus, device
    remote = TestClient(app)
    tok = remote.post("/pair", json={"pin": device.PIN}).json()["device_token"]
    bus.publish("call.incoming", "L7", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    from contextlib import ExitStack
    c = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    with ExitStack() as st:
        a = st.enter_context(remote.websocket_connect("/listen/L7", subprotocols=["bf-device", tok]))
        st.enter_context(lw(c, "/listen/L7")); st.enter_context(lw(c, "/listen/L7"))      # local console holds two more: cap reached
        assert relay.listener_count() == 3
        with remote.websocket_connect("/listen/L7", subprotocols=["bf-device", tok]) as b:   # reconnect at the cap: replaces, not 403/1013
            time.sleep(0.2)
            assert a.receive()["type"] == "websocket.close"
            assert relay.listener_count() == 3
            tok2 = remote.post("/pair", json={"pin": device.PIN}).json()["device_token"]
            with pytest.raises(Exception):                                                # a different device at the cap is still refused
                with remote.websocket_connect("/listen/L7", subprotocols=["bf-device", tok2]): pass


def test_p2_down_at_call_start_retries_during_call_then_connects(monkeypatch, caplog):
    import logging
    monkeypatch.setattr(relay, "P2_RETRY_S", 0.3); monkeypatch.setattr(relay, "P2_FAST_TRIES", 2); monkeypatch.setattr(relay, "P2_SLOW_S", 0.3)
    got = []
    async def h2(ws):
        async for m in ws: got.append(json.loads(m))
    async def go():
        s, port = await _server(h2); s.close(); await s.wait_closed()          # P2 DOWN: nothing listens on this port
        monkeypatch.setenv("P2_STT_URL", f"ws://127.0.0.1:{port}"); monkeypatch.delenv("PIPELINE_TOKEN", raising=False)
        async def to_caller(f): pass
        await relay.open("cdownretry1", to_caller)
        await relay.caller_frame("cdownretry1", {"event": "connected"})
        await relay.caller_frame("cdownretry1", {"event": "start", "stream_id": "S", "start": {}})
        for i in range(1, 25): await relay.caller_frame("cdownretry1", fr(i)); await asyncio.sleep(0.05)   # ~1.2 s: several failed attempts
        assert not got
        s2 = await websockets.serve(h2, "127.0.0.1", port)                      # P2 comes back mid-call
        for i in range(25, 70): await relay.caller_frame("cdownretry1", fr(i)); await asyncio.sleep(0.03)
        await asyncio.sleep(0.3); await relay.close("cdownretry1"); s2.close()
    with caplog.at_level(logging.WARNING, logger="hub.relay"):
        run(go())
    msgs = [r.getMessage() for r in caplog.records]
    assert any("P2 connect failed" in m and "attempt=1" in m and "retry in" in m for m in msgs) and any("attempt=3" in m for m in msgs)
    assert any(m.startswith("P2 connected call=cdownret") and "failed attempt" in m for m in msgs)
    assert [m["event"] for m in got[:2]] == ["connected", "start"]                  # header replayed on the late connect
    assert sum(1 for m in got if m["event"] == "media") >= 10                         # media flows again after P2 returns


def test_f19_reconnect_replaces_session_and_stale_close_cannot_kill_new(monkeypatch):
    monkeypatch.delenv("P2_STT_URL", raising=False); monkeypatch.delenv("P2_BASE", raising=False)
    c = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    from server import bus
    bus.publish("call.incoming", "F19", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    async def go():
        got = []
        async def back(f): pass
        old = await relay.open("F19", back)
        new = await relay.open("F19", back)                    # media WS reconnect
        assert old is not new and relay._S["F19"] is new
        await relay.close("F19", old)                          # the OLD socket's late cleanup
        assert relay._S.get("F19") is new                      # the new session survives
        await relay.caller_frame("F19", fr(1)); assert relay._S["F19"].dropped == 0
        await relay.close("F19", new)                          # the owner closes: gone
        assert "F19" not in relay._S
        await relay.close("F19", new)                          # idempotent
        # legacy close(call_id) with no session still closes whatever is current
        s3 = await relay.open("F19", back); await relay.close("F19"); assert "F19" not in relay._S
    run(go())


def test_f19_listener_survives_media_reconnect():
    import time
    from server import bus
    bus.publish("call.incoming", "F19L", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    c = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    async def go():
        async def back(f): pass
        await relay.open("F19L", back)
        with lw(c, "/listen/F19L"):
            assert relay.listener_count() == 1
            await relay.open("F19L", back)                     # reconnect: listener must stay attached
            await asyncio.sleep(0.8)
            assert relay.listener_count() == 1
            await relay.close("F19L")                          # real end of call releases it
            await asyncio.sleep(0.8)
            assert relay.listener_count() == 0
    run(go())


def test_f9_p2_tunnel_url_file_overrides_env_per_call(monkeypatch, tmp_path):
    monkeypatch.setenv("LOGDIR", str(tmp_path)); monkeypatch.setenv("P2_STT_URL", "ws://127.0.0.1:1"); monkeypatch.delenv("P2_BASE", raising=False)
    assert relay._url("P2_STT_URL", "/stt/x") == "ws://127.0.0.1:1/stt/x"                    # no file: env
    f = tmp_path / "p2_tunnel_url.txt"
    f.write_text("https://abc.trycloudflare.com\n"); assert relay._url("P2_STT_URL", "/stt/x") == "wss://abc.trycloudflare.com/stt/x"
    f.write_text("https://def.trycloudflare.com/ignored/path?x=1\n"); assert relay._url("P2_STT_URL", "/stt/x") == "wss://def.trycloudflare.com/stt/x"   # re-read, origin only
    for bad in ("file:///etc/passwd", "https://user:pw@h.example", "garbage", ""):
        f.write_text(bad); assert relay._url("P2_STT_URL", "/stt/x") == "ws://127.0.0.1:1/stt/x", bad                                     # invalid: ignored, env wins
    from server import ops
    f.write_text("https://ghi.trycloudflare.com"); assert ops._remote_base("P2_BASE") == "https://ghi.trycloudflare.com/healthz"


def test_f3_start_decoy_falls_back_to_standin_when_p3_unreachable(monkeypatch):
    async def go():
        seen = []
        async def hs(ws):
            seen.append(ws.request.path if hasattr(ws, "request") else "?")
            async for m in ws: pass
        s, port = await _server(hs)
        monkeypatch.setenv("P3_DECOY_URL", "ws://127.0.0.1:1"); monkeypatch.setenv("HUB_PORT", str(port)); monkeypatch.delenv("DECOY_STANDIN", raising=False)
        async def back(f): pass
        await relay.open("F3c", back)
        assert await relay.start_decoy("F3c") is True                      # P3 dead -> built-in persona stand-in took it
        assert relay.stats("F3c")["decoy_active"] is True and any("/decoy-standin/F3c" in p for p in seen)
        await relay.close("F3c"); s.close()
    run(go())


def test_f7_normal_routed_call_skips_p2_but_still_fans_to_listeners(monkeypatch):
    from server import bus
    bus.publish("call.incoming", "F7n", {"from": "+15555550188", "to": "+15555550100", "attestation": "A", "scam_id_score": 0.1})
    bus.publish("call.incoming", "F7f", {"from": "+15555550199", "to": "+15555550100", "attestation": "none", "scam_id_score": 0.1})
    bus.publish("call.routed", "F7f", {"decision": "NORMAL", "reason": "Hub error, fail open"})     # fail-open NORMAL is NOT trusted: keeps scoring
    bus.publish("call.routed", "F7n", {"decision": "NORMAL", "reason": "Trusted contact, caller ID verified"})
    bus.publish("call.incoming", "F7g", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    bus.publish("call.routed", "F7g", {"decision": "LIVE_GUARD", "reason": "x"})
    c = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    async def go():
        p2 = []; hooked = []
        async def h2(ws):
            async for m in ws: p2.append(json.loads(m))
        s2, port2 = await _server(h2)
        monkeypatch.setenv("P2_STT_URL", f"ws://127.0.0.1:{port2}"); monkeypatch.delenv("PIPELINE_TOKEN", raising=False)
        monkeypatch.setattr(relay, "feed_audio_hook", lambda cid, fr_: hooked.append(cid))
        async def back(f): pass
        for cid in ("F7n", "F7g", "F7f"):
            await relay.open(cid, back)
        q = asyncio.Queue(100); relay._LQ.setdefault("F7n", set()).add(q)
        for i in range(1, 6):
            await relay.caller_frame("F7n", fr(i)); await relay.caller_frame("F7g", fr(i)); await relay.caller_frame("F7f", fr(i))
        await asyncio.sleep(0.3)
        assert q.qsize() == 5                                              # NORMAL call still reaches /listen
        assert set(hooked) == {"F7g", "F7f"}                                      # fallback detector hook only for the guarded call
        for cid in ("F7n", "F7g", "F7f"): await relay.close(cid)
        s2.close()
        return p2
    p2 = run(go())
    assert sum(1 for m in p2 if m.get("event") == "media") == 10         # P2 saw LIVE_GUARD + fail-open calls, never the trusted one
