#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
import sys

from run_tas_harness import load_json, resolve_host, sha256_file


SNES9X_OPEN = Path("/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/open_in_snes9x.sh")


def main() -> int:
    parser = argparse.ArgumentParser(description="Launch a TAS harness scenario in manual-assist mode.")
    parser.add_argument("scenario", help="Absolute path to a harness scenario manifest JSON file.")
    args = parser.parse_args()

    scenario_path = Path(args.scenario)
    if not scenario_path.is_file():
        print(f"missing scenario manifest: {scenario_path}", file=sys.stderr)
        return 1

    scenario = load_json(scenario_path)
    host_resolution = resolve_host(scenario)
    if host_resolution["mode"] != "manual_assist":
        print(json.dumps({
            "scenario_id": scenario["id"],
            "status": "blocked",
            "reason": f"scenario is not in manual-assist mode: {host_resolution}"
        }, indent=2))
        return 1

    if host_resolution["selected_host"] != "Snes9x":
        print(json.dumps({
            "scenario_id": scenario["id"],
            "status": "blocked",
            "reason": f"unsupported manual-assist host: {host_resolution['selected_host']}"
        }, indent=2))
        return 1

    snes9x_paths = scenario["host_candidates"].get("Snes9x", [])
    app_path = next((p for p in snes9x_paths if Path(p).exists()), None)
    if app_path is None:
        print(json.dumps({
            "scenario_id": scenario["id"],
            "status": "blocked",
            "reason": "no Snes9x app path found"
        }, indent=2))
        return 1

    rom_path = Path(scenario["rom"]["path"])
    result_path = Path(scenario["result"]["manual_assist_artifact"])
    checklist = scenario["scenario"].get("manual_assist_checklist", [])

    subprocess.run(
        [str(SNES9X_OPEN), str(rom_path)],
        check=True,
        env={**os.environ, "APP": app_path},
    )

    result = {
        "scenario_id": scenario["id"],
        "status": "pending_operator",
        "mode": "manual_assist",
        "selected_host": host_resolution["selected_host"],
        "app_path": app_path,
        "rom_path": str(rom_path),
        "rom_sha256": sha256_file(rom_path),
        "candidate_transition": scenario["scenario"].get("candidate_transition"),
        "checklist": checklist,
    }

    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
