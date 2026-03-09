#!/usr/bin/env python3
"""Inspect SNES ROM headers and emit a compact technical summary."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import string
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DESTINATION_CODES = {
    0x00: "Japan",
    0x01: "North America",
    0x02: "Europe",
    0x03: "Sweden",
    0x04: "Finland",
    0x05: "Denmark",
    0x06: "France",
    0x07: "Netherlands",
    0x08: "Spain",
    0x09: "Germany",
    0x0A: "Italy",
    0x0B: "China",
    0x0C: "Indonesia",
    0x0D: "Korea",
}

MAP_MODE_HINTS = {
    0x20: ("LoROM", "SlowROM"),
    0x21: ("HiROM", "SlowROM"),
    0x22: ("LoROM", "SlowROM"),
    0x23: ("SA-1", "SlowROM"),
    0x25: ("ExHiROM", "SlowROM"),
    0x30: ("LoROM", "FastROM"),
    0x31: ("HiROM", "FastROM"),
    0x32: ("LoROM", "FastROM"),
    0x35: ("ExHiROM", "FastROM"),
}


@dataclass
class HeaderCandidate:
    name: str
    offset: int
    score: int
    data: dict[str, Any]


def printable_ratio(raw: bytes) -> float:
    allowed = set(string.ascii_letters + string.digits + " -_&'!:(),./")
    if not raw:
        return 0.0
    clean = 0
    for byte in raw:
        ch = chr(byte)
        if ch in allowed or byte == 0x20:
            clean += 1
    return clean / len(raw)


def decode_title(raw: bytes) -> str:
    text = raw.decode("ascii", errors="ignore").rstrip("\x00 ").strip()
    return text or "<unlabeled>"


def rom_size_from_code(code: int) -> int | None:
    if not 0 <= code <= 0x1F:
        return None
    return 1024 << code


def parse_candidate(data: bytes, name: str, offset: int) -> HeaderCandidate | None:
    if offset < 0 or offset + 0x40 > len(data):
        return None

    raw = data[offset : offset + 0x40]
    title_bytes = raw[:21]
    map_mode = raw[0x15]
    cartridge_type = raw[0x16]
    rom_size_code = raw[0x17]
    ram_size_code = raw[0x18]
    destination_code = raw[0x19]
    company_code = raw[0x1A]
    version = raw[0x1B]
    complement = int.from_bytes(raw[0x1C:0x1E], "little")
    checksum = int.from_bytes(raw[0x1E:0x20], "little")
    native_reset = int.from_bytes(raw[0x3C:0x3E], "little")
    emulation_reset = int.from_bytes(raw[0x3E:0x40], "little")

    mapping_hint, speed_hint = MAP_MODE_HINTS.get(
        map_mode,
        (name, "FastROM" if map_mode & 0x10 else "SlowROM"),
    )

    score = 0
    title_score = printable_ratio(title_bytes)
    if title_score > 0.85:
        score += 4
    elif title_score > 0.60:
        score += 2

    if (checksum ^ complement) == 0xFFFF:
        score += 8

    if native_reset not in (0x0000, 0xFFFF):
        score += 3
    if emulation_reset not in (0x0000, 0xFFFF):
        score += 3

    if map_mode in MAP_MODE_HINTS:
        score += 2

    parsed = {
        "candidate": name,
        "header_offset": offset,
        "title": decode_title(title_bytes),
        "map_mode": f"0x{map_mode:02X}",
        "detected_mapping": mapping_hint,
        "speed": speed_hint,
        "cartridge_type": f"0x{cartridge_type:02X}",
        "rom_size_code": f"0x{rom_size_code:02X}",
        "declared_rom_size_bytes": rom_size_from_code(rom_size_code),
        "ram_size_code": f"0x{ram_size_code:02X}",
        "declared_ram_size_bytes": rom_size_from_code(ram_size_code),
        "destination_code": f"0x{destination_code:02X}",
        "destination": DESTINATION_CODES.get(destination_code, "Unknown"),
        "company_code": f"0x{company_code:02X}",
        "mask_rom_version": version,
        "checksum": f"0x{checksum:04X}",
        "complement": f"0x{complement:04X}",
        "checksum_pair_valid": (checksum ^ complement) == 0xFFFF,
        "native_reset_vector": f"0x{native_reset:04X}",
        "emulation_reset_vector": f"0x{emulation_reset:04X}",
        "title_printable_ratio": round(title_score, 3),
    }
    return HeaderCandidate(name=name, offset=offset, score=score, data=parsed)


def inspect_rom(path: Path) -> dict[str, Any]:
    payload = path.read_bytes()
    has_copier_header = len(payload) % 1024 == 512
    rom = payload[512:] if has_copier_header else payload

    candidates: list[HeaderCandidate] = []
    for name, offset in (
        ("LoROM", 0x7FC0),
        ("HiROM", 0xFFC0),
        ("ExHiROM", 0x40FFC0),
    ):
        candidate = parse_candidate(rom, name, offset)
        if candidate:
            candidates.append(candidate)

    best = max(candidates, key=lambda c: c.score) if candidates else None
    sha256 = hashlib.sha256(rom).hexdigest()

    result: dict[str, Any] = {
        "path": str(path),
        "file_name": path.name,
        "file_size_bytes": os.path.getsize(path),
        "normalized_rom_size_bytes": len(rom),
        "has_copier_header": has_copier_header,
        "sha256": sha256,
        "header_candidates": [
            {
                "candidate": c.name,
                "score": c.score,
                **c.data,
            }
            for c in candidates
        ],
    }
    if best:
        result["selected_header"] = {
            "candidate": best.name,
            "score": best.score,
            **best.data,
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rom", nargs="+", help="Path(s) to .sfc/.smc ROM files")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output",
    )
    args = parser.parse_args()

    reports = [inspect_rom(Path(item).expanduser()) for item in args.rom]
    if len(reports) == 1:
        output: Any = reports[0]
    else:
        output = reports

    json.dump(output, fp=sys.stdout, indent=2 if args.pretty else None)
    if args.pretty:
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
