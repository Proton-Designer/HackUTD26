"""Unit tests never call the live Nessie sandbox (test_nessie.py injects a mock transport instead)."""
import os

os.environ.setdefault("NESSIE_OFFLINE", "1")
