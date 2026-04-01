#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
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


def resolve_host(scenario: dict) -> dict:
    preferred = scenario["runtime"]["preferred_host"]
    alternates = scenario["runtime"].get("alternate_hosts", [])
    fallback = scenario["runtime"].get("manual_assist_fallback")
    host_candidates = scenario.get("host_candidates", {})

    resolution = {
        "preferred_host": preferred,
        "available_hosts": [],
        "selected_host": None,
        "mode": "blocked",
        "blocked_reason": None,
    }

    def candidate_exists(path_str: str) -> bool:
        p = Path(path_str)
        return p.exists()

    ordered = [preferred] + [h for h in alternates if h != preferred]
    for host in ordered:
        paths = host_candidates.get(host, [])
        present_paths = [p for p in paths if candidate_exists(p)]
        if present_paths or shutil.which(host):
            resolution["available_hosts"].append({
                "host": host,
                "paths": present_paths,
                "which": shutil.which(host),
            })

    for host_info in resolution["available_hosts"]:
        if host_info["host"] == preferred:
            resolution["selected_host"] = preferred
            resolution["mode"] = "automated_candidate"
            return resolution

    if fallback:
        for host_info in resolution["available_hosts"]:
            if host_info["host"] == fallback:
                resolution["selected_host"] = fallback
                resolution["mode"] = "manual_assist"
                resolution["blocked_reason"] = f"preferred host '{preferred}' not available on this machine"
                return resolution

    resolution["blocked_reason"] = f"no candidate host found for preferred host '{preferred}' or fallback '{fallback}'"
    return resolution


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
    host_resolution = resolve_host(scenario)

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
        "host_resolution": host_resolution,
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
