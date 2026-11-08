"""Engine contract (cloud.py by eng1, local.py by eng3):

    async def score(window_text: str, metadata: dict) -> dict

Returns the RAW model JSON (keys per detection/prompt.py: s, asks, scam_type, stage,
impersonates, addresses_ai_system, why_chips) or raises. Do NOT normalize or merge rules there:
detection.detect.detect() calls detection.schema.normalize() and applies the rule backstop.
Messages come from detection.prompt.build_messages(window_text, metadata).
"""
