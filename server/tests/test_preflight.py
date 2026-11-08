import http.server, json, os, pathlib, subprocess, sys, threading

ROOT = pathlib.Path(__file__).resolve().parents[2]


def _stub(remote):
    body = json.dumps({"flags": {"SIM_MODE": False}, "pipelines": {"P2 /detect": {"mounted": False, "remote": remote}}}).encode()
    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(s):
            ok = s.path.startswith("/demo/status")
            s.send_response(200 if ok else 404); s.send_header("content-type", "application/json"); s.end_headers(); s.wfile.write(body if ok else b"{}")
        def log_message(*a): pass
    srv = http.server.HTTPServer(("127.0.0.1", 0), H); threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def _run(remote, tmp_path):
    srv = _stub(remote)
    try:
        env = dict(os.environ, HUB_URL=f"http://127.0.0.1:{srv.server_port}", P2_STT_URL="ws://tok:sekret@p2.example.org:8100/stt?x=1", LOGDIR=str(tmp_path))
        env.pop("P2_BASE", None); env.pop("HUB_TOKEN", None)
        return subprocess.run([sys.executable, str(ROOT / "scripts" / "preflight"), "--live", "--no-tunnel"], env=env, capture_output=True, text=True, timeout=60)
    finally:
        srv.shutdown()


def test_preflight_p2_down_is_hard_fail_with_host_only(tmp_path):
    r = _run("unreachable", tmp_path)
    line = next(l for l in r.stdout.splitlines() if "P2 reachable" in l)
    assert line.startswith("FAIL") and "host=p2.example.org:8100" in line and "unreachable" in line
    assert "sekret" not in r.stdout + r.stderr and "tok:" not in line and "/stt" not in line
    assert r.returncode == 1


def test_preflight_p2_up_passes_that_check(tmp_path):
    r = _run("up", tmp_path)
    assert next(l for l in r.stdout.splitlines() if "P2 reachable" in l).startswith("PASS")


def test_f9_preflight_checks_p2_tunnel_url_file(tmp_path):
    (tmp_path / "p2_tunnel_url.txt").write_text("https://p2-dead.invalid\n")
    r = _run("up", tmp_path)
    line = next(l for l in r.stdout.splitlines() if "p2_tunnel_url.txt" in l and "reachable" in l)
    assert line.startswith("FAIL") and "host=p2-dead.invalid" in line and "stale" in line
    assert "host=p2-dead.invalid (logs/p2_tunnel_url.txt)" in next(l for l in r.stdout.splitlines() if "P2 reachable" in l)
    (tmp_path / "p2_tunnel_url.txt").unlink()
    assert not any("p2_tunnel_url" in l for l in _run("up", tmp_path).stdout.splitlines())


def test_ready_check_summarizes_and_fails_on_live_call_without_leaking_env(tmp_path):
    body = json.dumps({"flags": {"SIM_MODE": False, "active_calls": 2, "MARIA_LEG": "sip", "telnyx_ok": True}, "pipelines": {}}).encode()
    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(s):
            ok = s.path.startswith("/demo/status")
            s.send_response(200 if ok else 404); s.send_header("content-type", "application/json"); s.end_headers(); s.wfile.write(body if ok else b"{}")
        def log_message(*a): pass
    srv = http.server.HTTPServer(("127.0.0.1", 0), H); threading.Thread(target=srv.serve_forever, daemon=True).start()
    try:
        env = dict(os.environ, LOGDIR=str(tmp_path), P2_STT_URL="ws://127.0.0.1:1/stt", P3_BASE="http://127.0.0.1:1", TELNYX_API_KEY="SEKRET-VALUE-123", NVIDIA_API_KEY="NV-SEKRET-456")
        env.pop("HUB_TOKEN", None); env.pop("P2_BASE", None)
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "ready_check"), "--local", f"http://127.0.0.1:{srv.server_port}", "--no-tunnel"],
                           env=env, capture_output=True, text=True, timeout=120)
    finally:
        srv.shutdown()
    out = r.stdout
    assert r.returncode == 1 and "NOT READY" in out
    assert any(l.startswith("FAIL") and "active_calls == 0" in l and "active_calls=2" in l for l in out.splitlines())
    assert any(l.startswith("FAIL") and "decoy (P3)" in l and "host=127.0.0.1:1" in l for l in out.splitlines())
    assert any(l.startswith("FAIL") and l.split("  ")[1].startswith("P2 /healthz") for l in out.splitlines())
    assert any(l.startswith("PASS") and "telnyx_ok" in l for l in out.splitlines())
    assert "SEKRET" not in out + r.stderr


def test_ready_check_fails_on_non_seed_trusted_numbers(tmp_path):
    def run(trusted):
        status = json.dumps({"flags": {"active_calls": 0, "MARIA_LEG": "sip", "telnyx_ok": True}, "pipelines": {}}).encode()
        tr = json.dumps({"trusted": trusted}).encode()
        class H(http.server.BaseHTTPRequestHandler):
            def do_GET(s):
                b = status if s.path.startswith("/demo/status") else tr if s.path == "/trusted" else b"{}"
                s.send_response(200); s.send_header("content-type", "application/json"); s.end_headers(); s.wfile.write(b)
            def log_message(*a): pass
        srv = http.server.HTTPServer(("127.0.0.1", 0), H); threading.Thread(target=srv.serve_forever, daemon=True).start()
        try:
            env = dict(os.environ, LOGDIR=str(tmp_path)); env.pop("HUB_TOKEN", None)
            return subprocess.run([sys.executable, str(ROOT / "scripts" / "ready_check"), "--local", f"http://127.0.0.1:{srv.server_port}", "--no-tunnel"], env=env, capture_output=True, text=True, timeout=120).stdout
        finally:
            srv.shutdown()
    line = lambda o: next(l for l in o.splitlines() if "trusted list holds only" in l)
    assert line(run([{"number": "+15555550188", "label": "Her bank (synthetic)"}])).startswith("PASS")
    bad = line(run([{"number": "+15555550188", "label": "x"}, {"number": "+14695551234", "label": "mom"}]))
    assert bad.startswith("FAIL") and "1 extra" in bad and "+1469***34" in bad and "4695551234" not in bad
