#!/usr/bin/env python3
"""Verify published Tier A tables listed in MANIFEST.json exist on disk."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _bootstrap import PROJECT_ROOT, SCRIPTS_DIR

SHARED = PROJECT_ROOT / "data" / "shared_data_manuscript_2026"
MANIFEST = SHARED / "MANIFEST.json"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any MANIFEST entry is missing.",
    )
    args = parser.parse_args()

    if not MANIFEST.is_file():
        print(f"ERROR: missing MANIFEST: {MANIFEST}", file=sys.stderr)
        return 1

    payload = json.loads(MANIFEST.read_text())
    files = payload.get("files", [])
    missing: list[str] = []
    present = 0
    for rel in files:
        path = SHARED / rel
        if path.is_file():
            present += 1
        else:
            missing.append(rel)

    print(f"Shared data root: {SHARED}")
    print(f"MANIFEST generated_utc: {payload.get('generated_utc', 'unknown')}")
    print(f"Listed files: {len(files)}")
    print(f"Present: {present}")
    print(f"Missing: {len(missing)}")
    for rel in missing[:20]:
        print(f"  - {rel}")
    if len(missing) > 20:
        print(f"  ... and {len(missing) - 20} more")

    if missing and args.strict:
        return 1
    return 0 if not missing else (1 if args.strict else 0)


if __name__ == "__main__":
    # Allow running as `python scripts/verify_shared_data.py`
    sys.path.insert(0, str(SCRIPTS_DIR))
    raise SystemExit(main())
