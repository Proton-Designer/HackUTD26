"""Thin async Telnyx REST client. Never logs the API key."""
import os, httpx
from urllib.parse import quote
API = "https://api.telnyx.com/v2"

class TelnyxError(Exception): pass

async def _post(path: str, body: dict | None = None, text: bool = False):
    key = os.environ.get("TELNYX_API_KEY")
    if not key: raise TelnyxError("TELNYX_API_KEY not set")
    async with httpx.AsyncClient(timeout=8) as c:
        r = await c.post(API + path, json=body or {}, headers={"Authorization": f"Bearer {key}"})
    if r.status_code >= 400: raise TelnyxError(f"{path} -> {r.status_code} {r.text[:200]}")
    return r.text if text else r.json()

async def get_call(ccid):
    """GET /calls/{ccid}: exists only for a real, live call on OUR account (compensating control when webhooks are unsigned)."""
    key = os.environ.get("TELNYX_API_KEY")
    if not key: raise TelnyxError("TELNYX_API_KEY not set")
    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.get(f"{API}/calls/{quote(ccid, safe='')}", headers={"Authorization": f"Bearer {key}"})
    if r.status_code >= 400: raise TelnyxError(f"get_call -> {r.status_code}")
    return r.json()

def _id(x: str) -> str: return quote(x, safe="")

async def answer(ccid, body=None): return await _post(f"/calls/{_id(ccid)}/actions/answer", body)
async def reject(ccid, cause="CALL_REJECTED"): return await _post(f"/calls/{_id(ccid)}/actions/reject", {"cause": cause})
async def hangup(ccid): return await _post(f"/calls/{_id(ccid)}/actions/hangup")
def dial_allowed(to) -> bool:
    """HARD GUARD: POST /v2/calls may only dial our own Maria SIP URI (sip:<TELNYX_SIP_USER>@sip.telnyx.com). Any PSTN number is refused unless
    BACKFIRE_ALLOW_PSTN_OUTBOUND=1 (outbound PSTN self-dials with scam audio got an account blocked)."""
    if os.environ.get("BACKFIRE_ALLOW_PSTN_OUTBOUND") == "1": return True
    u = os.environ.get("TELNYX_SIP_USER")
    return bool(u) and str(to or "").strip().lower() == f"sip:{u}@sip.telnyx.com".lower()

async def dial(body):
    if not dial_allowed((body or {}).get("to")):
        raise TelnyxError("dial refused: only sip:<our SIP user> may be dialed; PSTN outbound needs BACKFIRE_ALLOW_PSTN_OUTBOUND=1")
    return await _post("/calls", body)
async def create_conference(ccid, name): return await _post("/conferences", {"call_control_id": ccid, "name": name, "beep_enabled": "never"})
async def join_conference(conf_id, ccid, **kw): return await _post(f"/conferences/{_id(conf_id)}/actions/join", {"call_control_id": ccid, **kw})
async def leave_conference(conf_id, ccid): return await _post(f"/conferences/{_id(conf_id)}/actions/leave", {"call_control_id": ccid})
async def webrtc_token(credential_id): return await _post(f"/telephony_credentials/{_id(credential_id)}/token", text=True)
