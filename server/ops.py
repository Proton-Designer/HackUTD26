"""TASK-010: latency log + integration-readiness status. Never raises into the call path (fail open)."""
import html, json, logging, os, pathlib, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from . import bus, db

log = logging.getLogger("hub.ops")
LATENCY_LOG = pathlib.Path(os.environ.get("HUB_LATENCY_LOG") or (pathlib.Path(os.environ.get("LOGDIR") or pathlib.Path(__file__).resolve().parent.parent / "logs") / "latency.jsonl"))
_t: dict = {}        # call_id -> {"incoming": t, "action": t, "alert": bool}
stats: dict = {}     # metric -> list[ms] (last 200)

def _rec(metric, call_id, ms):
    ms = round(ms, 1)
    stats.setdefault(metric, []).append(ms)
    del stats[metric][:-200]
    try:
        LATENCY_LOG.parent.mkdir(parents=True, exist_ok=True)
        with LATENCY_LOG.open("a") as f:
            f.write(json.dumps({"ts": time.time(), "call_id": call_id, "metric": metric, "ms": ms}) + "\n")
    except Exception:
        log.warning("latency log write failed", exc_info=True)

def observe(ev):
    t, cid, now = ev["type"], ev["call_id"], time.time()
    s = _t.setdefault(cid, {})
    if len(_t) > 500:
        _t.pop(next(iter(_t)), None)
    if t == "call.incoming":
        s.clear(); s["incoming"] = now
    elif t == "call.routed" and "incoming" in s:
        _rec("route_ms", cid, (now - s["incoming"]) * 1000)
    elif t == "alert.fired" and "incoming" in s and not s.get("alert"):
        s["alert"] = True
        _rec("alert_ms", cid, (now - s["incoming"]) * 1000)
    elif t == "user.action":
        s["action"] = now
    elif t == "handoff.started" and "action" in s:
        _rec("handoff_ms", cid, (now - s.pop("action")) * 1000)

bus.add_observer(observe)

def reset():
    _t.clear(); stats.clear()   # telnyx_state is account health, not demo state: reset leaves it

def latency_summary():
    out = {}
    for m, v in stats.items():
        sv = sorted(v)
        out[m] = {"n": len(v), "last_ms": v[-1], "p50_ms": sv[len(sv) // 2], "max_ms": sv[-1]}
    return {"metrics": out, "log": str(LATENCY_LOG)}

# Telnyx REST health, reported by voip (in-process: `from server import ops; ops.telnyx_result(ok, detail)`). Never raises; never stores bodies/keys.
telnyx_state: dict = {"ok": None, "kind": None, "ts": None}

def telnyx_result(ok: bool, detail: str = "") -> None:
    """Record the outcome of the latest Telnyx REST call. ok=True -> telnyx_ok true. On failure `detail` is the error text (e.g.
    'POST /calls -> 401 {...10009 user marked as blocked}'): 401/403/10009 -> telnyx_ok false (kind 'auth'); network/5xx/other -> telnyx_ok
    unchanged-but-flagged (kind 'unreachable'/'error') so one blip doesn't claim the account is blocked."""
    try:
        d = str(detail or "")
        if ok:
            telnyx_state.update(ok=True, kind=None)
        elif "10009" in d or " 401" in d or " 403" in d or "-> 401" in d or "-> 403" in d:
            telnyx_state.update(ok=False, kind="auth")
        else:
            telnyx_state.update(kind="unreachable" if any(w in d.lower() for w in ("connect", "timeout", "timed out", "unreachable", "dns")) else "error")
        telnyx_state["ts"] = time.time()
    except Exception:
        pass

# name -> (path prefix that proves the router is mounted, env var for remote base URL)
EXPECTED = {
    "voip":   ("/telnyx", "VOIP_BASE"),
    "P2 /detect": ("/detect", "P2_BASE"),
    "P3 /decoy":  ("/decoy/", "P3_BASE"),
    "P4 /intel":  ("/intel/actions", "P4_BASE"),
}

def _remote_base(env):
    """Remote pipeline base URL for the probe: <env> if set, else derive the http(s) host from the relay's ws URL
    (P2_STT_URL / P3_DECOY_URL, ws->http, path dropped) and probe /healthz there."""
    if env == "P2_BASE":
        try:
            from . import relay
            o = relay.p2_tunnel_origin()   # F9: logs/p2_tunnel_url.txt (current P2 tunnel) beats the env
            if o: return o + "/healthz"
        except Exception:
            pass
    b = os.environ.get(env)
    if b:
        return b
    ws_env = {"P2_BASE": "P2_STT_URL", "P3_BASE": "P3_DECOY_URL"}.get(env)
    u = os.environ.get(ws_env or "")
    if not u:
        return None
    from urllib.parse import urlsplit
    sp = urlsplit(u)
    return f"{'https' if sp.scheme == 'wss' else 'http'}://{sp.netloc}/healthz" if sp.netloc else None

def _probe(base):
    if not base:
        return "not configured"
    try:
        urllib.request.urlopen(base, timeout=1).close()
        return "up"
    except urllib.error.HTTPError:
        return "up"  # any HTTP answer = reachable
    except Exception:
        return "unreachable"

def _paths(routes, prefix=""):
    out = []
    for r in routes:
        if hasattr(r, "original_router"):  # newer FastAPI wraps include_router results
            out += _paths(r.original_router.routes, prefix + (getattr(r, "prefix", "") or ""))  # route.path already carries the router's own prefix
        elif hasattr(r, "path"):
            out.append(prefix + r.path)
    return out

def _nvidia_key_set():
    """True/False only, never the value. Same lookup intel uses (env, else repo .env)."""
    try:
        from intel import agent
        return bool(agent._api_key())
    except Exception:
        return bool(os.environ.get("NVIDIA_API_KEY"))

def _intel_engine():
    """What intel will use for its next investigation: nemotron model id (key present), template (no key / LLM off), or None if intel isn't mounted."""
    try:
        from intel import api, agent
    except Exception:
        return None
    if not api._cfg.get("use_llm", True) or not _nvidia_key_set():
        return "template"
    return "nemotron:" + str(agent.MODEL)

def customer_name() -> str:
    """Display name of the protected customer (env CUSTOMER_NAME, default "Maria"; set it empty for no name). Cosmetic only: enum values like by:"maria" never change."""
    n = os.environ.get("CUSTOMER_NAME")
    n = "Maria" if n is None else n
    return "".join(ch for ch in n if ch.isprintable() and ch not in "<>&\"'`\\").strip()[:40]

def status(app):
    paths = _paths(app.routes)
    names = {}
    with ThreadPoolExecutor(4) as ex:
        futs = {n: ex.submit(_probe, _remote_base(env)) for n, (_, env) in EXPECTED.items()}
        for n, (prefix, env) in EXPECTED.items():
            names[n] = {"mounted": any(p.startswith(prefix) for p in paths), "remote": futs[n].result()}
            if n == "P3 /decoy" and names[n]["mounted"] and not os.environ.get("P3_DECOY_URL") and any(p.startswith("/decoy-standin/") for p in paths):
                names[n]["stand_in"] = True   # /decoy/{id} is voip's stand-in persona alias, not the real P3
    try:
        counts = {"confirmed_scammers": len(db.list_confirmed()), "calls": len(db.list_calls())}
        for tbl in ("campaign_numbers", "trusted"):
            counts[tbl] = db.q(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
    except Exception:
        counts = {"error": "db unavailable"}
    try:
        from . import relay
        _ids, _last = relay.active_calls()
    except Exception:
        _ids, _last = [], None
    return {"hub": "up", "pipelines": names, "active_call_ids": [i[:8] for i in _ids],
            "flags": {"DEMO_MODE": os.environ.get("DEMO_MODE") == "1", "FALLBACK": os.environ.get("FALLBACK") == "1", "SIM_MODE": os.environ.get("SIM_MODE") == "1", "FALLBACK_DETECT": os.environ.get("FALLBACK_DETECT") == "1", "NVIDIA_API_KEY_set": _nvidia_key_set(), "telnyx_ok": telnyx_state["ok"], "telnyx_last_error": telnyx_state["kind"], "intel_engine": _intel_engine(), "HUB_TOKEN_set": bool(os.environ.get("HUB_TOKEN")), "MARIA_LEG": os.environ.get("MARIA_LEG") or "sip", "CUSTOMER_NAME": customer_name(), "active_calls": len(_ids), "last_call_activity_ts": _last},
            "db": counts, "latency": latency_summary()["metrics"]}

def status_html(s):
    rows = "".join(
        f"<tr><td>{html.escape(n)}</td><td>{'mounted' if v['mounted'] else 'not mounted'}</td><td>{html.escape(v['remote'])}</td></tr>"
        for n, v in s["pipelines"].items())
    return ("<!doctype html><meta charset=utf-8><title>Backfire hub status</title>"
            "<style>body{font:15px system-ui;margin:2rem}td,th{padding:.3rem .8rem;border-bottom:1px solid #ccc;text-align:left}</style>"
            "<h1>Backfire hub status <small>(simulated carrier network)</small></h1>"
            f"<p>hub: <b>up</b> · DEMO_MODE: {s['flags']['DEMO_MODE']} · HUB_TOKEN set: {'yes' if s['flags']['HUB_TOKEN_set'] else 'no'}</p>"
            f"<table><tr><th>pipeline</th><th>router</th><th>remote base</th></tr>{rows}</table>"
            f"<p>db: {html.escape(json.dumps(s['db']))}</p><p>latency: {html.escape(json.dumps(s['latency']))}</p>")
