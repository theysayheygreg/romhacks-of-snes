#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path("/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes")
HARNESS_DIR = ROOT / "data" / "tas-harnesses"


def validate_manifest(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text())

    required_top = [
        "id",
        "game",
        "rom",
        "lane",
        "status",
        "primary_host_candidate",
        "harnesses",
    ]
    for key in required_top:
        if key not in data:
            errors.append(f"{path.name}: missing top-level key '{key}'")

    harnesses = data.get("harnesses", [])
    if not isinstance(harnesses, list) or not harnesses:
        errors.append(f"{path.name}: 'harnesses' must be a non-empty list")
        return errors

    required_harness = ["id", "type", "priority", "goal", "assertions", "expected_artifact"]
    for harness in harnesses:
        for key in required_harness:
            if key not in harness:
                errors.append(f"{path.name}: harness missing key '{key}'")
        if not isinstance(harness.get("assertions", []), list) or not harness.get("assertions"):
            errors.append(f"{path.name}: harness '{harness.get('id', '<unknown>')}' needs non-empty assertions")

    return errors


def main() -> int:
    manifests = sorted(HARNESS_DIR.glob("*.json"))
    if not manifests:
        print("no manifests found", file=sys.stderr)
        return 1

    errors: list[str] = []
    for manifest in manifests:
        errors.extend(validate_manifest(manifest))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    for manifest in manifests:
        data = json.loads(manifest.read_text())
        print(f"{manifest.name}: {data['game']} ({len(data['harnesses'])} harness sketches)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
