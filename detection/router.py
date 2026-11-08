from __future__ import annotations
from fastapi import APIRouter
from pydantic import BaseModel, Field
from detection.detect import detect

router = APIRouter()


class DetectIn(BaseModel):
    call_id: str = ""
    window_text: str = ""
    metadata: dict = Field(default_factory=dict)
    engine: str = "cloud"


@router.post("/detect")
async def post_detect(body: DetectIn) -> dict:
    return await detect(body.call_id, body.window_text, body.metadata, body.engine)
