import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "engine_server"))
from engine_server import validate_payload

valid = {
    "protocol": "backgammon-coach-engine-v1",
    "game": {"points": [0] * 24, "dice": [3, 1]},
    "candidates": [{"index": 0, "moves": [{"from": 13, "to": 10, "die": 3}]}],
}
ok, message = validate_payload(valid)
assert ok, message

invalid = dict(valid)
invalid["game"] = {"points": [0] * 23, "dice": [3, 1]}
ok, _ = validate_payload(invalid)
assert not ok

print("PASS — payload validation")
