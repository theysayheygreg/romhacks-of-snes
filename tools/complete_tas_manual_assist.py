#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Complete a pending manual-assist TAS harness artifact with pass/fail results."
    )
    parser.add_argument("artifact", help="Absolute path to an existing manual-assist artifact JSON file.")
    parser.add_argument("--pass-all", action="store_true", dest="pass_all", help="Mark every checklist item as pass.")
    parser.add_argument(
        "--fail-index",
        action="append",
        default=[],
        metavar="N",
        help="1-based checklist index to mark as fail. Can be repeated.",
    )
    parser.add_argument(
        "--note",
        action="append",
        default=[],
        metavar="N=TEXT",
        help="Attach a note to a checklist item using 1-based index, e.g. --note 3=door hung on fadeout",
    )
    parser.add_argument("--operator-notes", default=None, help="Freeform operator notes for the overall result.")
    parser.add_argument(
        "--status",
        choices=["pass", "fail"],
        default=None,
        help="Override the inferred overall status.",
    )
    args = parser.parse_args()

    artifact_path = Path(args.artifact)
    if not artifact_path.is_file():
        print(f"missing artifact: {artifact_path}", file=sys.stderr)
        return 1

    artifact = load_json(artifact_path)
    if artifact.get("mode") != "manual_assist":
        print(f"artifact is not manual_assist: {artifact_path}", file=sys.stderr)
        return 1

    checklist_results = artifact.get("checklist_results")
    if not checklist_results:
        checklist_results = [
            {"item": item, "status": "pending", "notes": None}
            for item in artifact.get("checklist", [])
        ]

    fail_indexes: set[int] = set()
    for raw_index in args.fail_index:
        try:
            index = int(raw_index)
        except ValueError:
            print(f"invalid --fail-index value: {raw_index}", file=sys.stderr)
            return 1
        if index < 1 or index > len(checklist_results):
            print(f"--fail-index out of range: {index}", file=sys.stderr)
            return 1
        fail_indexes.add(index - 1)

    notes_by_index: dict[int, str | None] = {}
    for raw_note in args.note:
        if "=" not in raw_note:
            print(f"invalid --note value (expected N=TEXT): {raw_note}", file=sys.stderr)
            return 1
        raw_index, text = raw_note.split("=", 1)
        try:
            index = int(raw_index)
        except ValueError:
            print(f"invalid --note index: {raw_index}", file=sys.stderr)
            return 1
        if index < 1 or index > len(checklist_results):
            print(f"--note index out of range: {index}", file=sys.stderr)
            return 1
        notes_by_index[index - 1] = text.strip() or None

    if args.pass_all:
        for entry in checklist_results:
            entry["status"] = "pass"

    for index in fail_indexes:
        checklist_results[index]["status"] = "fail"

    for index, text in notes_by_index.items():
        checklist_results[index]["notes"] = text

    if not args.pass_all and not fail_indexes:
        print("refusing to complete artifact without --pass-all or at least one --fail-index", file=sys.stderr)
        return 1

    if any(entry["status"] == "pending" for entry in checklist_results):
        print("refusing to complete artifact while checklist items remain pending", file=sys.stderr)
        return 1

    inferred_status = "fail" if any(entry["status"] == "fail" for entry in checklist_results) else "pass"
    artifact["checklist_results"] = checklist_results
    artifact["status"] = args.status or inferred_status
    artifact["completed_at"] = datetime.now(timezone.utc).isoformat()
    artifact["operator_notes"] = args.operator_notes

    artifact_path.write_text(json.dumps(artifact, indent=2) + "\n")
    print(json.dumps(artifact, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
