"""TASK-010: latency log + integration-readiness status. Never raises into the call path (fail open)."""
import html, json, logging, os, pathlib, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from . import bus, db

log = logging.getLogger("hub.ops")
LATENCY_LOG = pathlib.Path(os.environ.get("HUB_LATENCY_LOG") or pathlib.Path(__file__).resolve().parent.parent / "logs" / "latency.jsonl")
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
    _t.clear(); stats.clear()

def latency_summary():
    out = {}
    for m, v in stats.items():
        sv = sorted(v)
        out[m] = {"n": len(v), "last_ms": v[-1], "p50_ms": sv[len(sv) // 2], "max_ms": sv[-1]}
    return {"metrics": out, "log": str(LATENCY_LOG)}

# name -> (path prefix that proves the router is mounted, env var for remote base URL)
EXPECTED = {
    "voip":   ("/telnyx", "VOIP_BASE"),
    "P2 /detect": ("/detect", "P2_BASE"),
    "P3 /decoy":  ("/decoy", "P3_BASE"),
    "P4 /intel":  ("/intel/actions", "P4_BASE"),
}

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

def status(app):
    paths = [getattr(r, "path", "") for r in app.routes]
    names = {}
    with ThreadPoolExecutor(4) as ex:
        futs = {n: ex.submit(_probe, os.environ.get(env)) for n, (_, env) in EXPECTED.items()}
        for n, (prefix, env) in EXPECTED.items():
            names[n] = {"mounted": any(p.startswith(prefix) for p in paths), "remote": futs[n].result()}
    try:
        counts = {"confirmed_scammers": len(db.list_confirmed()), "calls": len(db.list_calls())}
        for tbl in ("campaign_numbers", "trusted"):
            counts[tbl] = db.q(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
    except Exception:
        counts = {"error": "db unavailable"}
    return {"hub": "up", "pipelines": names,
            "flags": {"DEMO_MODE": os.environ.get("DEMO_MODE") == "1", "HUB_TOKEN_set": bool(os.environ.get("HUB_TOKEN"))},
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
