"""Voice enrollment for onboarding (contract: contracts/interfaces.md, 00_SHARED_RULES.md).
POST /voice/enroll  JSON {recording: <base64 audio>, mime, consent_version} -> {voice_id}
DELETE /voice/{voice_id} -> {ok: true}
Both need a paired device / direct loopback / x-hub-token (device.require_device).
P3 connected (env P3_VOICE_URL, else P3_BASE): proxy to P3 and relay its voice_id; emit voice.enrolled / voice.deleted.
Not connected, or P3 unreachable: the audio is DROPPED (never stored, never logged) and the answer is
{voice_id: null, fallback: "synthetic", reason: ...}; nothing is emitted. Audio and base64 never appear in logs or error text."""
import base64, binascii, json, logging, os, re
from urllib.parse import quote
import httpx
from fastapi import APIRouter, Depends, HTTPException, Request
from . import bus, device

log = logging.getLogger("hub.voice")
router = APIRouter()
MAX_AUDIO = 5 * 1024 * 1024                    # decoded audio bytes
MAX_BODY = (MAX_AUDIO * 4) // 3 + 4096         # base64 + JSON envelope
MIMES = {"audio/webm": "webm", "audio/ogg": "ogg", "audio/wav": "wav", "audio/x-wav": "wav", "audio/wave": "wav"}
VID_RE = re.compile(r"[A-Za-z0-9_.-]{1,80}")
CONSENT_RE = re.compile(r"[A-Za-z0-9._-]{1,32}")

def _base():
    b = (os.environ.get("P3_VOICE_URL") or os.environ.get("P3_BASE") or "").strip().rstrip("/")
    if b.startswith("ws"):
        b = b.replace("ws", "http", 1)
    return b or None

def _hdrs():
    t = os.environ.get("PIPELINE_TOKEN")
    return {"x-pipeline-token": t} if t else {}

def _magic_ok(kind: str, b: bytes) -> bool:
    return (kind == "webm" and b[:4] == b"\x1a\x45\xdf\xa3") or (kind == "ogg" and b[:4] == b"OggS") or (kind == "wav" and b[:4] == b"RIFF" and b[8:12] == b"WAVE")

async def _read_body(request: Request) -> bytes:
    cl = request.headers.get("content-length")
    if cl and cl.isdigit() and int(cl) > MAX_BODY:
        raise HTTPException(413, "recording too large (max 5 MB)")
    buf = bytearray()
    async for chunk in request.stream():
        buf += chunk
        if len(buf) > MAX_BODY:
            raise HTTPException(413, "recording too large (max 5 MB)")
    return bytes(buf)

@router.post("/voice/enroll", dependencies=[Depends(device.require_device)])
async def enroll(request: Request):
    raw = await _read_body(request)
    try:
        body = json.loads(raw)
        rec, mime, consent = body["recording"], str(body.get("mime") or "audio/webm").split(";")[0].strip().lower(), body["consent_version"]
        if not isinstance(rec, str) or not isinstance(consent, str):
            raise ValueError
    except Exception:                                   # never echo the body back
        raise HTTPException(400, "expected JSON {recording: base64, mime, consent_version}")
    del raw
    if not CONSENT_RE.fullmatch(consent):
        raise HTTPException(400, "bad consent_version")
    kind = MIMES.get(mime)
    if not kind:
        raise HTTPException(415, "accepted formats: webm, ogg, wav")
    try:
        audio = base64.b64decode(rec, validate=True)
    except (binascii.Error, ValueError):
        raise HTTPException(400, "recording is not valid base64")
    del rec, body
    if len(audio) > MAX_AUDIO:
        raise HTTPException(413, "recording too large (max 5 MB)")
    if len(audio) < 1000 or not _magic_ok(kind, audio):
        raise HTTPException(415, f"not a valid {kind} recording")
    base = _base()
    if not base:
        del audio                                        # not kept anywhere
        return {"voice_id": None, "fallback": "synthetic", "reason": "voice service not connected"}
    try:
        async with httpx.AsyncClient(timeout=30) as c:
            r = await c.post(base + "/voice/enroll", headers=_hdrs(),
                             json={"recording": base64.b64encode(audio).decode(), "mime": mime, "consent_version": consent})
        r.raise_for_status()
        vid = r.json().get("voice_id")
        if not isinstance(vid, str) or not VID_RE.fullmatch(vid):
            raise ValueError("bad voice_id")
    except Exception as e:                               # fail open: onboarding continues with the labelled synthetic voice
        log.warning("voice enroll via P3 failed (%s); falling back to synthetic", type(e).__name__)
        return {"voice_id": None, "fallback": "synthetic", "reason": "voice service unreachable"}
    finally:
        del audio
    bus.publish("voice.enrolled", "c_onboard", {"voice_id": vid, "consent_version": consent})
    return {"voice_id": vid}

@router.delete("/voice/{voice_id}", dependencies=[Depends(device.require_device)])
async def delete_voice(voice_id: str):
    """Idempotent: always {ok: true}, even for unknown ids or when P3 is down. Proxies to P3 when connected."""
    base = _base()
    if base and VID_RE.fullmatch(voice_id):
        try:
            async with httpx.AsyncClient(timeout=10) as c:
                r = await c.delete(f"{base}/voice/{quote(voice_id, safe='')}", headers=_hdrs())
            if r.status_code < 500:                      # 2xx or 404 (already gone) both mean deleted
                bus.publish("voice.deleted", "c_onboard", {"voice_id": voice_id})
        except Exception as e:
            log.warning("voice delete via P3 failed (%s); local delete reported ok", type(e).__name__)
    return {"ok": True}
