import asyncio
import httpx
import pytest
from detection.engines import local


def _client(handler):
    return httpx.AsyncClient(transport=httpx.MockTransport(handler))


def test_parse_json_variants():
    assert local.parse_json('{"s": 0.9}') == {"s": 0.9}
    assert local.parse_json('<think>hm {x}</think>```json\n{"s": 0.1, "asks": []}\n```')["s"] == 0.1
    with pytest.raises(ValueError):
        local.parse_json("no json here")


def test_score_posts_ollama_chat(monkeypatch):
    monkeypatch.setenv("LOCAL_LLM_URL", "http://x:1/")
    monkeypatch.setenv("LOCAL_MODEL", "m1")
    seen = {}

    def handler(req):
        seen["url"] = str(req.url)
        import json
        seen["body"] = json.loads(req.content)
        return httpx.Response(200, json={"choices": [{"message": {"content": '{"s": 0.9, "asks": ["otp"]}'}}]})

    async def go():
        async with _client(handler) as c:
            return await local.score("read me the code", {"a": 1}, client=c)

    out = asyncio.run(go())
    assert out == {"s": 0.9, "asks": ["otp"]}
    assert seen["url"] == "http://x:1/v1/chat/completions"
    b = seen["body"]
    assert b["model"] == "m1" and b["temperature"] == 0 and b["response_format"] == {"type": "json_object"}
    assert "<caller_transcript>" in b["messages"][1]["content"]


def test_score_raises_on_http_error_and_garbage():
    async def go(resp):
        async with _client(lambda r: resp) as c:
            return await local.score("x", {}, client=c)
    with pytest.raises(httpx.HTTPStatusError):
        asyncio.run(go(httpx.Response(500)))
    with pytest.raises(ValueError):
        asyncio.run(go(httpx.Response(200, json={"choices": [{"message": {"content": "sorry"}}]})))
