#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: $0 BASE_ROM OUTPUT_ROM" >&2
  exit 1
fi

base_rom="$1"
output_rom="$2"
asar_bin="/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/z3randomizer/bin/macos/asar"
patch_file="/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/patches/metroid/sm-starting-energy-199.asm"

if [[ "$base_rom" == "$output_rom" ]]; then
  echo "output ROM must differ from base ROM" >&2
  exit 1
fi

cp "$base_rom" "$output_rom"
"$asar_bin" --fix-checksum=on "$patch_file" "$output_rom"
