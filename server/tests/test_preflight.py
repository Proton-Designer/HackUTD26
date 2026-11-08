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
