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
        monkeypatch.setenv("P3_DECOY_URL", "ws://127.0.0.1:1")
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
