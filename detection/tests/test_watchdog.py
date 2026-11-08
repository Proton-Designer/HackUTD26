"""watchdog.sh against a throwaway tmux session, a stdlib fake service and a fake tunnel (no network, no live windows)."""
import os, shutil, socket, subprocess, sys, textwrap, uuid
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pytestmark = pytest.mark.skipif(not shutil.which("tmux"), reason="needs tmux")


def _free():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p


def test_restarts_missing_service_window_and_reports_new_tunnel_url(tmp_path):
    sess, port = f"wdt{uuid.uuid4().hex[:6]}", _free()
    (tmp_path / "svc.py").write_text(textwrap.dedent(f"""
        import http.server
        class H(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                b=b'{{"ok":true,"active_stt_sockets":0}}'; self.send_response(200); self.end_headers(); self.wfile.write(b)
            def log_message(self,*a): pass
        http.server.HTTPServer(("127.0.0.1",{port}),H).serve_forever()"""))
    (tmp_path / "tun.sh").write_text("echo 'x https://fake-new-one.trycloudflare.com y' >> " + str(tmp_path / "tun.log") + "; sleep 120\n")
    env = dict(os.environ, WD_SESSION=sess, WD_PORT=str(port), WD_TICK_S="1", WD_TUN_EVERY="2", WD_FAILS="3", WD_MAX_TICKS="14",
               WD_LOG=str(tmp_path / "wd.log"), WD_URL_FILE=str(tmp_path / "url.txt"), WD_TUN_LOG=str(tmp_path / "tun.log"),
               WD_SVC_CMD=f"{sys.executable} {tmp_path/'svc.py'}", WD_TUN_CMD=f"bash {tmp_path/'tun.sh'}",
               WD_TUNNEL_URL="http://127.0.0.1:1")          # dead tunnel
    subprocess.run(["tmux", "new-session", "-d", "-s", sess, "-n", "other", "sleep 60"], check=True)
    try:
        subprocess.run(["bash", os.path.join(ROOT, "detection/scripts/watchdog.sh")], env=env, cwd=ROOT, timeout=90,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        log = (tmp_path / "wd.log").read_text()
        assert "SVC RESTART" in log                                             # window was missing -> recreated
        assert "TUNNEL URL CHANGED" in log and "fake-new-one" in log
        assert (tmp_path / "url.txt").read_text().strip() == "https://fake-new-one.trycloudflare.com"
    finally:
        subprocess.run(["tmux", "kill-session", "-t", sess], capture_output=True)   # kills the fake service too
