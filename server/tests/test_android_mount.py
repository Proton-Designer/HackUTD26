"""android_voip.bridge.router is mounted in the hub, and the hub still imports when android_voip is missing or broken."""
import subprocess, sys, os, pathlib, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]


def _env():
    e = dict(os.environ, HUB_NO_PIN_FILE="1", LOGDIR=tempfile.mkdtemp(), HUB_DB=tempfile.mktemp(), INTEL_DB=tempfile.mktemp())
    e.pop("DEMO_MODE", None)
    return e


def _run(code):
    return subprocess.run([sys.executable, "-c", code], cwd=ROOT, env=_env(), capture_output=True, text=True, timeout=60)


def test_routes_present_when_importable():
    from server.main import app
    from server import ops
    paths = ops._paths(app.routes)
    for p in ("/android/route", "/android/call", "/android/report", "/android/handoff", "/android/events/{call_id}",
              "/android/media/{call_id}", "/android/decoy/{call_id}"):
        assert p in paths, p
    assert "/healthz" in paths and "/telnyx/webhook" in paths     # nothing else displaced


def test_hub_starts_without_android_voip():
    r = _run("import sys; sys.modules['android_voip']=None; sys.modules['android_voip.bridge']=None; sys.modules['android_voip.bridge.router']=None\n"
             "import logging; logging.disable(logging.CRITICAL)\n"
             "from server.main import app; from server import ops\n"
             "p=ops._paths(app.routes); assert '/healthz' in p and '/telnyx/webhook' in p and not any(x.startswith('/android/') for x in p); print('OK')")
    assert r.returncode == 0 and "OK" in r.stdout, r.stderr[-800:]


def test_hub_starts_with_broken_android_voip():
    r = _run("import sys, types\n"
             "class Bad:\n"
             "    def find_spec(self, name, path=None, target=None):\n"
             "        if name == 'android_voip.bridge.router': raise RuntimeError('boom')\n"
             "sys.meta_path.insert(0, Bad())\n"
             "import logging; logging.disable(logging.CRITICAL)\n"
             "from server.main import app; from server import ops\n"
             "p=ops._paths(app.routes); assert '/healthz' in p and not any(x.startswith('/android/') for x in p); print('OK')")
    assert r.returncode == 0 and "OK" in r.stdout, r.stderr[-800:]
