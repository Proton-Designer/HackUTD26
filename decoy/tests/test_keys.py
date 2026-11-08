"""#123: NVIDIA key failover order (no network)."""
import sys
sys.path.insert(0, ".")
import decoy.core as C


def test_rotation(monkeypatch):
    monkeypatch.setenv("NVIDIA_API_KEY", "k1"); monkeypatch.setenv("NVIDIA_API_KEY_2", "k2"); monkeypatch.setenv("NVIDIA_API_KEY_3", "k3")
    monkeypatch.setattr(C, "_key_start", 0)
    assert C.keys_in_order() == ["k1", "k2", "k3"]
    C.key_failed("k1", "429")
    assert C.keys_in_order() == ["k2", "k3", "k1"]
    C.key_failed("k1", "429")          # stale failure of a key that is no longer current: no double advance
    assert C.keys_in_order() == ["k2", "k3", "k1"]
    C.key_failed("k2", "429"); C.key_failed("k3", "429")
    assert C.keys_in_order() == ["k1", "k2", "k3"]


def test_single_and_missing(monkeypatch):
    monkeypatch.setenv("NVIDIA_API_KEY", "k1"); monkeypatch.delenv("NVIDIA_API_KEY_2", raising=False); monkeypatch.setenv("NVIDIA_API_KEY_3", "k1")
    monkeypatch.setattr(C, "_key_start", 0)
    assert C.nvidia_keys() == ["k1"]   # duplicates and blanks dropped
    C.key_failed("k1", "429")
    assert C.keys_in_order() == ["k1"]


def test_is_key_error():
    class E(Exception):
        def __init__(self, n): self.n = n
        def code(self):
            return type("C", (), {"name": self.n})()
    assert C.is_key_error(E("RESOURCE_EXHAUSTED")) and C.is_key_error(E("UNAUTHENTICATED"))
    assert not C.is_key_error(E("DEADLINE_EXCEEDED")) and not C.is_key_error(ValueError())
