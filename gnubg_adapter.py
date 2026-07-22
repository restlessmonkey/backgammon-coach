from __future__ import annotations

"""
GNU Backgammon adapter boundary for Backgammon Coach v2.0.1.

This file intentionally refuses to fabricate rankings. The precise Windows GNUbg
automation method must be validated against the installed build before analysis
is enabled. See docs/setup/LIVE_GNUBG_VALIDATION_CHECKLIST.md.

Expected behavior after implementation:
1. Read the PWA request JSON.
2. Convert the board to a GNUbg-supported position representation.
3. Evaluate every supplied complete legal candidate with GNUbg.
4. Return rankings and equities in the API contract format.
5. Record the GNUbg executable/version and raw evidence used for the result.
"""

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gnubg", required=True)
    parser.add_argument("--request", required=True)
    parser.add_argument("--response", required=True)
    args = parser.parse_args()

    request_path = Path(args.request)
    if not request_path.is_file():
        print(f"Request file not found: {request_path}", file=sys.stderr)
        return 2

    # Refuse to claim engine strength until the installed GNUbg interface has
    # been validated and this adapter has been completed.
    print(
        "GNU Backgammon adapter is not yet certified. "
        "Complete LIVE_GNUBG_VALIDATION_CHECKLIST.md before enabling analysis.",
        file=sys.stderr,
    )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
