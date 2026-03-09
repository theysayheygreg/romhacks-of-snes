#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: $0 BASE_ROM OUTPUT_ROM" >&2
  exit 1
fi

base_rom="$1"
output_rom="$2"
repo_root="/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/z3randomizer"

cp "$base_rom" "$output_rom"

cd "$repo_root"
./bin/macos/asar LTTP_RND_GeneralBugfixes.asm "$output_rom"
