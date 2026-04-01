#!/bin/sh
set -eu

APP="/Users/theysayheygreg/Documents/SNES/emulators/Snes9x-1.63.app"

if [ "$#" -ne 1 ]; then
  echo "usage: $0 /absolute/path/to/rom.sfc" >&2
  exit 1
fi

ROM="$1"

if [ ! -d "$APP" ]; then
  echo "missing Snes9x app: $APP" >&2
  exit 1
fi

if [ ! -f "$ROM" ]; then
  echo "missing ROM: $ROM" >&2
  exit 1
fi

open -ga "$APP"
sleep 1
open -a "$APP" "$ROM"
