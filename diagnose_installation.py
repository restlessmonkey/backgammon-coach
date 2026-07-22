from __future__ import annotations
import json
import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "configuration" / "engine_config.json"
REPORT = ROOT / "validation" / f"installation_diagnostic_{datetime.now():%Y%m%d_%H%M%S}.json"

candidates = [
    shutil.which("gnubg"),
    shutil.which("gnubg.exe"),
    r"C:\Program Files\GNU Backgammon\gnubg.exe",
    r"C:\Program Files (x86)\GNU Backgammon\gnubg.exe",
]
found = next((str(Path(p)) for p in candidates if p and Path(p).is_file()), "")

result = {
    "version": "2.0.1",
    "timestamp": datetime.now().isoformat(),
    "python": os.sys.version,
    "config_exists": CONFIG.is_file(),
    "gnubg_candidates": [p for p in candidates if p],
    "gnubg_found": found,
    "executable_probe": None,
    "analysis_certified": False,
    "next_action": "Install GNU Backgammon or update engine_config.json, then run live validation."
}

if found:
    probes = ([found, "--version"], [found, "-v"])
    for cmd in probes:
        try:
            cp = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
            if cp.stdout or cp.stderr:
                result["executable_probe"] = {
                    "command": cmd,
                    "returncode": cp.returncode,
                    "stdout": cp.stdout[-2000:],
                    "stderr": cp.stderr[-2000:]
                }
                break
        except Exception as exc:
            result["executable_probe"] = {"command": cmd, "error": str(exc)}

REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
print(f"\nReport: {REPORT}")
