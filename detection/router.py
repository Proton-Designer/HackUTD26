from __future__ import annotations
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from detection.detect import detect
from detection.auth import require_token

router = APIRouter()


class DetectIn(BaseModel):
    call_id: str = Field(default="c_unknown", pattern=r"^[A-Za-z0-9_-]{1,64}$")
    window_text: str = ""
    metadata: dict = Field(default_factory=dict)
    engine: str = "cloud"


@router.post("/detect", dependencies=[Depends(require_token)])
async def post_detect(body: DetectIn) -> dict:
    return await detect(body.call_id, body.window_text, body.metadata, body.engine)
