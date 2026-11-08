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


@pytest.fixture(autouse=True)
def _no_real_nvidia_keys(tmp_path, monkeypatch):
    """Tests never read the repo .env for NVIDIA keys and start with no failover keys / no remembered healthy key."""
    from server import nvidia_keys
    monkeypatch.setattr(nvidia_keys, "ENV_FILE", tmp_path / "no.env")
    for k in ("NVIDIA_API_KEY_2", "NVIDIA_API_KEY_3", "INTEL_NVIDIA_API_KEY"): monkeypatch.delenv(k, raising=False)
    nvidia_keys.reset()
