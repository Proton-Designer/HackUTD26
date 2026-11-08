"""Local engine: Nemotron Nano 4B on this machine's GPU via Ollama. Stands in for on-device detection.

Same contract as cloud.py: `async score(window_text, metadata) -> raw dict` (or raises). detect.py
normalizes + merges with the rule backstop and fails open on any exception/timeout.
Env: LOCAL_LLM_URL (default http://127.0.0.1:11434), LOCAL_MODEL (default backfire-nemotron-nano-4b).
The prompt is detection/prompt.py, shared with the cloud engine so the comparison is fair.
"""
from __future__ import annotations

import json
import os
import re

import httpx

from detection.prompt import build_messages

DEFAULT_URL = "http://127.0.0.1:11434"
DEFAULT_MODEL = "backfire-nemotron-nano-4b"
TIMEOUT_S = float(os.environ.get("LOCAL_TIMEOUT_S", "20"))


def _url() -> str:
    return os.environ.get("LOCAL_LLM_URL", DEFAULT_URL).rstrip("/")


def _model() -> str:
    return os.environ.get("LOCAL_MODEL", DEFAULT_MODEL)


def parse_json(text: str) -> dict:
    """Pull the first JSON object out of model text (tolerates <think> blocks / code fences)."""
    text = re.sub(r"<think>.*?</think>", "", text or "", flags=re.S)
    start = text.find("{")
    if start < 0:
        raise ValueError("no JSON object in local model output")
    obj, _ = json.JSONDecoder().raw_decode(text[start:])
    if not isinstance(obj, dict):
        raise ValueError("local model output is not a JSON object")
    return obj


async def score(window_text: str, metadata: dict | None = None, *, client: httpx.AsyncClient | None = None) -> dict:
    body = {
        "model": _model(),
        "messages": build_messages(window_text, metadata or {}),
        "stream": False,
        "think": False,
        "format": "json",
        "options": {"temperature": 0, "num_predict": 220, "num_ctx": 2048},
        "keep_alive": "30m",
    }
    own = client is None
    c = client or httpx.AsyncClient(timeout=TIMEOUT_S)
    try:
        r = await c.post(f"{_url()}/api/chat", json=body)
        r.raise_for_status()
        return parse_json(r.json().get("message", {}).get("content", ""))
    finally:
        if own:
            await c.aclose()
