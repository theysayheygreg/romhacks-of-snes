#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def main() -> int:
    parser = argparse.ArgumentParser(description="Run TAS-harness preflight validation for a scenario manifest.")
    parser.add_argument("scenario", help="Absolute path to a harness scenario manifest JSON file.")
    args = parser.parse_args()

    scenario_path = Path(args.scenario)
    if not scenario_path.is_file():
        print(f"missing scenario manifest: {scenario_path}", file=sys.stderr)
        return 1

    scenario = load_json(scenario_path)
    rom_path = Path(scenario["rom"]["path"])
    analysis_path = Path(scenario["rom"]["analysis"])
    result_path = Path(scenario["result"]["preflight_artifact"])
    script_paths = [Path(p) for p in scenario["source_harness"]["entry_scripts"]]

    errors: list[str] = []
    if not rom_path.is_file():
        errors.append(f"missing rom: {rom_path}")
    if not analysis_path.is_file():
        errors.append(f"missing rom analysis: {analysis_path}")
    for script_path in script_paths:
        if not script_path.is_file():
            errors.append(f"missing source harness file: {script_path}")

    result = {
        "scenario_id": scenario["id"],
        "status": "pass" if not errors else "fail",
        "mode": "preflight_only",
        "runtime": scenario["runtime"]["preferred_host"],
        "rom_path": str(rom_path),
        "rom_sha256": sha256_file(rom_path) if rom_path.is_file() else None,
        "analysis_path": str(analysis_path),
        "entry_scripts": [str(p) for p in script_paths],
        "candidate_transition": scenario["scenario"].get("candidate_transition"),
        "assertions": scenario["assertions"],
        "errors": errors
    }

    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(json.dumps(result, indent=2) + "\n")

    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
