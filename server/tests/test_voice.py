import base64, json
import httpx
import pytest
from fastapi.testclient import TestClient
from server import bus, device, voice
from server.main import app

WEBM = b"\x1a\x45\xdf\xa3" + b"\x00" * 2000
OGG = b"OggS" + b"\x00" * 2000
MP4 = b"\x00\x00\x00\x18ftypM4A \x00\x00\x00\x00M4A mp42isom" + b"\x00" * 2000   # real ISO-BMFF header: size, 'ftyp', brand
ADTS = b"\xff\xf1\x50\x80\x02\x1f\xfc" + b"\x00" * 2000
WAV = b"RIFF\x00\x00\x00\x00WAVE" + b"\x00" * 2000
b64 = lambda b: base64.b64encode(b).decode()

@pytest.fixture
def c(monkeypatch):
    for k in ("P3_BASE", "P3_VOICE_URL", "PIPELINE_TOKEN"): monkeypatch.delenv(k, raising=False)
    bus.history.clear()
    return TestClient(app, client=("127.0.0.1", 5000))

def body(rec=WEBM, mime="audio/webm;codecs=opus", consent="v1"):
    return {"recording": b64(rec), "mime": mime, "consent_version": consent}

def vevents(): return [e for e in bus.history if e["type"].startswith("voice.")]

def test_auth_required():
    r = TestClient(app)                                   # remote, unpaired
    assert r.post("/voice/enroll", json=body()).status_code == 401
    assert r.delete("/voice/abc").status_code == 401

def test_no_p3_drops_audio_and_emits_nothing(c, caplog):
    import logging
    with caplog.at_level(logging.DEBUG):
        for rec, mime in ((WEBM, "audio/webm;codecs=opus"), (OGG, "audio/ogg"), (WAV, "audio/wav")):
            r = c.post("/voice/enroll", json=body(rec, mime))
            assert r.status_code == 200 and r.json() == {"voice_id": None, "fallback": "synthetic", "reason": "voice service not connected"}
    assert not vevents()
    assert b64(WEBM)[:40] not in caplog.text                # audio never logged

def test_validation(c):
    assert c.post("/voice/enroll", json=body(mime="audio/mpeg")).status_code == 415
    assert c.post("/voice/enroll", json=body(rec=b"not audio at all" * 200)).status_code == 415   # magic bytes must match
    assert c.post("/voice/enroll", json=body(rec=OGG, mime="audio/webm")).status_code == 415       # mime/content mismatch
    assert c.post("/voice/enroll", json={"recording": "!!notb64!!", "mime": "audio/webm", "consent_version": "v1"}).status_code == 400
    assert c.post("/voice/enroll", json=body(consent="v1; drop")).status_code == 400
    assert c.post("/voice/enroll", json={"recording": 5}).status_code == 400
    r = c.post("/voice/enroll", content=b"{bad", headers={"content-type": "application/json"})
    assert r.status_code == 400 and "bad" not in r.text

def test_size_cap(c):
    big = WEBM + b"\x00" * (5 * 1024 * 1024)
    assert c.post("/voice/enroll", json=body(big)).status_code == 413
    huge = b'{"recording":"' + b"A" * (voice.MAX_BODY + 10) + b'"}'
    assert c.post("/voice/enroll", content=huge, headers={"content-type": "application/json"}).status_code == 413
    ok = WEBM + b"\x00" * (4 * 1024 * 1024)
    assert c.post("/voice/enroll", json=body(ok)).status_code == 200

def test_proxies_to_p3_and_emits(c, monkeypatch):
    monkeypatch.setenv("P3_BASE", "http://p3.test:9"); monkeypatch.setenv("PIPELINE_TOKEN", "pt")
    seen = {}
    def handler(req: httpx.Request):
        seen[(req.method, req.url.path)] = (json.loads(req.content) if req.content else None, req.headers.get("x-pipeline-token"))
        if req.method == "POST": return httpx.Response(200, json={"voice_id": "v_123"})
        return httpx.Response(204)
    real = httpx.AsyncClient
    monkeypatch.setattr(voice.httpx, "AsyncClient", lambda **k: real(transport=httpx.MockTransport(handler), **k))
    r = c.post("/voice/enroll", json=body())
    assert r.json() == {"voice_id": "v_123"}
    sent, tok = seen[("POST", "/voice/enroll")]
    assert base64.b64decode(sent["recording"]) == WEBM and sent["consent_version"] == "v1" and sent["mime"] == "audio/webm" and tok == "pt"
    assert [(e["type"], e["data"]) for e in vevents()] == [("voice.enrolled", {"voice_id": "v_123", "consent_version": "v1"})]
    assert c.delete("/voice/v_123").json() == {"ok": True}
    assert ("DELETE", "/voice/v_123") in seen and vevents()[-1]["type"] == "voice.deleted" and vevents()[-1]["data"] == {"voice_id": "v_123"}

def test_p3_down_falls_back_and_delete_still_ok(c, monkeypatch):
    monkeypatch.setenv("P3_VOICE_URL", "http://p3.test:9")
    def dead(req): raise httpx.ConnectError("down")
    real = httpx.AsyncClient
    monkeypatch.setattr(voice.httpx, "AsyncClient", lambda **k: real(transport=httpx.MockTransport(dead), **k))
    assert c.post("/voice/enroll", json=body()).json() == {"voice_id": None, "fallback": "synthetic", "reason": "voice service unreachable"}
    assert not vevents()
    assert c.delete("/voice/v_1").json() == {"ok": True} and not vevents()

def test_delete_idempotent_without_p3_and_odd_ids(c):
    assert c.delete("/voice/never-existed").json() == {"ok": True}
    assert c.delete("/voice/never-existed").json() == {"ok": True}
    assert c.delete("/voice/..%2Fetc").status_code in (200, 404)           # never proxied: the id regex gates it
    assert not vevents()


def test_ios_safari_mp4_aac_accepted_with_mime_params(c):
    for rec, mime in ((MP4, "audio/mp4"), (MP4, "audio/mp4;codecs=mp4a.40.2"), (MP4, "audio/x-m4a"), (MP4, "audio/m4a"),
                      (MP4, "audio/aac"), (ADTS, "audio/aac")):
        r = c.post("/voice/enroll", json=body(rec=rec, mime=mime))
        assert r.status_code == 200, (mime, r.text)
    assert c.post("/voice/enroll", json=body(rec=WEBM, mime="audio/mp4")).status_code == 415      # mime/content mismatch still refused
    assert c.post("/voice/enroll", json=body(rec=MP4, mime="audio/webm")).status_code == 415
    assert c.post("/voice/enroll", json=body(rec=b"\x00" * 2000, mime="audio/mp4")).status_code == 415
