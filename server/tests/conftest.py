import pytest

@pytest.fixture(autouse=True)
def _isolated_latency_log(tmp_path, monkeypatch):
    """Tests must never write to the real logs/latency.jsonl."""
    from server import ops
    monkeypatch.setattr(ops, "LATENCY_LOG", tmp_path / "latency.jsonl")
    ops.reset()
