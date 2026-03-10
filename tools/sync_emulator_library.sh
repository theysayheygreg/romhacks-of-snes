#!/usr/bin/env bash
set -euo pipefail

repo_root="/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes"
documents_root="$HOME/Documents/SNES"
base_roms="$repo_root/roms/base"
build_roms="$repo_root/build"
ready_dir="$documents_root/emulator-ready"
data_dir="$documents_root/emulator-data"

mkdir -p "$documents_root"
mkdir -p "$ready_dir"
mkdir -p "$data_dir/bsnes/saves" "$data_dir/bsnes/states" "$data_dir/bsnes/screenshots" "$data_dir/bsnes/cheats" "$data_dir/bsnes/patches"

ln -sfn "$base_roms" "$documents_root/base-roms"
ln -sfn "$build_roms" "$documents_root/build-roms"

# Rebuild the curated ready-to-test directory as symlinks.
find "$ready_dir" -maxdepth 1 -type l -delete

find "$base_roms" -maxdepth 1 -type f \( -iname '*.sfc' -o -iname '*.smc' \) | while IFS= read -r rom; do
  ln -sfn "$rom" "$ready_dir/$(basename "$rom")"
done

find "$build_roms" -maxdepth 1 -type f \( -iname '*.sfc' -o -iname '*.smc' \) | while IFS= read -r rom; do
  ln -sfn "$rom" "$ready_dir/$(basename "$rom")"
done

printf 'Documents root: %s\n' "$documents_root"
printf 'Ready-to-test: %s\n' "$ready_dir"
