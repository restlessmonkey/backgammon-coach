from __future__ import annotations

import json
import logging
import os
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, request
from flask_cors import CORS

ROOT = Path(__file__).resolve().parent
CONFIG_PATH = Path(os.environ.get("BACKGAMMON_ENGINE_CONFIG", ROOT / "configuration" / "engine_config.json"))
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "engine_server.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
LOG = logging.getLogger("backgammon-coach-engine")


@dataclass(frozen=True)
class Config:
    host: str
    port: int
    allowed_origins: list[str]
    gnubg_executable: str
    adapter_command: list[str]
    request_timeout_seconds: int
    analysis_enabled: bool


def load_config() -> Config:
    raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return Config(
        host=str(raw.get("host", "127.0.0.1")),
        port=int(raw.get("port", 8765)),
        allowed_origins=list(raw.get("allowed_origins", ["http://localhost", "https://localhost"])),
        gnubg_executable=str(raw.get("gnubg_executable", "")),
        adapter_command=list(raw.get("adapter_command", [])),
        request_timeout_seconds=int(raw.get("request_timeout_seconds", 120)),
        analysis_enabled=bool(raw.get("analysis_enabled", False)),
    )


def executable_status(path_value: str) -> dict[str, Any]:
    if not path_value:
        return {"configured": False, "exists": False, "path": ""}
    path = Path(path_value)
    return {"configured": True, "exists": path.is_file(), "path": str(path)}


def validate_payload(payload: Any) -> tuple[bool, str]:
    if not isinstance(payload, dict):
        return False, "Request body must be a JSON object."
    if payload.get("protocol") != "backgammon-coach-engine-v1":
        return False, "Unsupported or missing protocol."
    game = payload.get("game")
    if not isinstance(game, dict):
        return False, "Missing game object."
    points = game.get("points")
    if not isinstance(points, list) or len(points) != 24:
        return False, "game.points must contain exactly 24 points."
    dice = game.get("dice")
    if not isinstance(dice, list) or not dice or any(not isinstance(v, int) or v < 1 or v > 6 for v in dice):
        return False, "game.dice must contain valid die values."
    candidates = payload.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        return False, "At least one legal candidate is required."
    for i, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            return False, f"Candidate {i} must be an object."
        if not isinstance(candidate.get("index"), int):
            return False, f"Candidate {i} is missing an integer index."
        moves = candidate.get("moves")
        if not isinstance(moves, list) or not moves:
            return False, f"Candidate {i} contains no checker moves."
    return True, ""


def run_adapter(config: Config, payload_path: Path, response_path: Path) -> dict[str, Any]:
    if not config.analysis_enabled:
        raise RuntimeError(
            "Analysis is intentionally disabled until the GNU Backgammon adapter "
            "has passed live validation. Set analysis_enabled=true only after completing "
            "LIVE_GNUBG_VALIDATION_CHECKLIST.md."
        )
    if not config.adapter_command:
        raise RuntimeError("No adapter_command is configured.")

    command = [
        token.replace("{payload}", str(payload_path))
             .replace("{response}", str(response_path))
             .replace("{gnubg}", config.gnubg_executable)
        for token in config.adapter_command
    ]
    LOG.info("Launching adapter command: %s", command)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=config.request_timeout_seconds,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"Adapter failed with exit code {completed.returncode}. "
            f"STDERR: {completed.stderr[-2000:]}"
        )
    if not response_path.exists():
        raise RuntimeError("Adapter returned success but did not create a response file.")
    result = json.loads(response_path.read_text(encoding="utf-8"))
    if result.get("engine") != "GNU Backgammon":
        raise RuntimeError("Adapter response did not identify the engine as GNU Backgammon.")
    if not isinstance(result.get("rankings"), list) or not result["rankings"]:
        raise RuntimeError("Adapter response contains no rankings.")
    result["adapter_stdout"] = completed.stdout[-2000:]
    return result


CONFIG = load_config()
app = Flask(__name__)
CORS(app, origins=CONFIG.allowed_origins)


@app.get("/health")
def health():
    status = executable_status(CONFIG.gnubg_executable)
    ready = bool(CONFIG.analysis_enabled and status["exists"] and CONFIG.adapter_command)
    return jsonify({
        "status": "ok" if ready else "setup-required",
        "service": "Backgammon Coach Grandmaster Engine Server",
        "serviceVersion": "2.0.1",
        "engine": "GNU Backgammon" if ready else "GNU Backgammon adapter not certified",
        "analysisReady": ready,
        "analysisEnabled": CONFIG.analysis_enabled,
        "gnubg": status,
        "adapterConfigured": bool(CONFIG.adapter_command),
        "configPath": str(CONFIG_PATH),
    }), 200


@app.post("/analyze")
def analyze():
    request_id = uuid.uuid4().hex
    payload = request.get_json(silent=True)
    valid, error = validate_payload(payload)
    if not valid:
        return jsonify({"error": error, "requestId": request_id}), 400

    request_dir = ROOT / "runtime" / request_id
    request_dir.mkdir(parents=True, exist_ok=False)
    payload_path = request_dir / "request.json"
    response_path = request_dir / "response.json"
    payload_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    started = time.time()
    try:
        result = run_adapter(CONFIG, payload_path, response_path)
        result["requestId"] = request_id
        result["elapsedMilliseconds"] = round((time.time() - started) * 1000)
        (request_dir / "final_response.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        return jsonify(result), 200
    except Exception as exc:
        LOG.exception("Analysis request %s failed", request_id)
        failure = {
            "error": str(exc),
            "requestId": request_id,
            "engine": "NOT VERIFIED",
            "analysisReady": False,
        }
        (request_dir / "failure.json").write_text(json.dumps(failure, indent=2), encoding="utf-8")
        return jsonify(failure), 503


if __name__ == "__main__":
    LOG.info("Starting service on %s:%s using %s", CONFIG.host, CONFIG.port, CONFIG_PATH)
    app.run(host=CONFIG.host, port=CONFIG.port, debug=False)
