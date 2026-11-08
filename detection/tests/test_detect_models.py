from pathlib import Path

def test_models_md_pins_primary():
    t = (Path(__file__).resolve().parents[2] / "contracts" / "models.md").read_text()
    assert "nemotron-3.5-lightning-30b-a3b" in t and "enable_thinking" in t
