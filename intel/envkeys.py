"""Read an API key: process env first, else the repo-root .env (P1's hub doesn't load it). Values are never logged."""
from __future__ import annotations

import os
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent / ".env"


def env_secret(name: str) -> str | None:
    if os.getenv(name):
        return os.getenv(name)
    try:
        for line in ENV_FILE.read_text().splitlines():
            k, _, v = line.strip().partition("=")
            if k.removeprefix("export ").strip() == name and v.strip():
                return v.strip().strip('"').strip("'")
    except OSError:
        pass
    return None
