import os, tempfile
_T = tempfile.mkdtemp(prefix="backfire-test-")
os.environ["LOGDIR"] = _T                      # tests never write the live hub's logs/ (pin file, latency, tunnel url)
os.environ["HUB_NO_PIN_FILE"] = "1"
os.environ.setdefault("INTEL_DB", os.path.join(_T, "intel.db"))
os.environ.setdefault("HUB_DB", os.path.join(_T, "hub.db"))
import pytest

@pytest.fixture(autouse=True)
def _isolated_latency_log(tmp_path, monkeypatch):
    from server import ops
    monkeypatch.setattr(ops, "LATENCY_LOG", tmp_path / "latency.jsonl")
    ops.reset()
