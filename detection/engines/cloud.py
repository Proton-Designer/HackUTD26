"""Cloud engine: NVIDIA-hosted Nemotron (primary per contracts/models.md). Returns RAW model JSON or raises."""
from __future__ import annotations
import json, os, re
from pathlib import Path
import httpx
from detection.prompt import build_messages

MODEL = os.environ.get("P2_CLOUD_MODEL", "nvidia/nemotron-3.5-lightning-30b-a3b")
TIMEOUT_S = float(os.environ.get("P2_CLOUD_TIMEOUT_S", "2.5"))


def _creds() -> tuple[str, str]:
    key, base = os.environ.get("NVIDIA_API_KEY"), os.environ.get("NVIDIA_BASE_URL")
    if not (key and base):
        envf = Path(__file__).resolve().parents[2] / ".env"
        if envf.exists():
            for line in envf.read_text().splitlines():
                if "=" in line and not line.lstrip().startswith("#"):
                    k, v = line.split("=", 1)
                    if k.strip() == "NVIDIA_API_KEY" and not key:
                        key = v.strip().strip('"\'')
                    if k.strip() == "NVIDIA_BASE_URL" and not base:
                        base = v.strip().strip('"\'')
    if not (key and base):
        raise RuntimeError("NVIDIA credentials not configured")
    return key, base.rstrip("/")


def parse_json(text: str) -> dict:
    text = (text or "").strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.M).strip()
    try:
        obj = json.loads(text)
    except ValueError:
        m = re.search(r"\{.*\}", text, re.S)
        if not m:
            raise
        obj = json.loads(m.group(0))
    if not isinstance(obj, dict):
        raise ValueError("model JSON is not an object")
    return obj


async def _call(client: httpx.AsyncClient, key: str, base: str, messages: list[dict]) -> str:
    r = await client.post(
        f"{base}/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": MODEL, "messages": messages, "temperature": 0.1, "max_tokens": 300,
            "response_format": {"type": "json_object"},
            "chat_template_kwargs": {"enable_thinking": False},
        },
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"].get("content") or ""


async def score(window_text: str, metadata: dict) -> dict:
    key, base = _creds()
    messages = build_messages(window_text, metadata)
    async with httpx.AsyncClient(timeout=TIMEOUT_S) as client:
        content = await _call(client, key, base, messages)
        try:
            return parse_json(content)
        except ValueError:  # one retry on bad JSON
            content = await _call(client, key, base, messages)
            return parse_json(content)
