#!/bin/sh
set -eu

APP="${APP:-/Users/theysayheygreg/Documents/SNES/emulators/Snes9x-1.63.app}"
DB="$APP/Contents/Frameworks/snes9x_framework.framework/Versions/A/Resources/gamecontrollerdb.txt"
PREF_PLIST="$HOME/Library/Preferences/com.snes9x.macos.snes9x.plist"
PREF_DOMAIN="com.snes9x.macos.snes9x"
DEVICE_KEY="1356:3302:0"
PLAYER_KEY="0"
MAPPING_LINE="030000004c050000e60c000000010000,PS5 Controller,a:b1,b:b2,back:b8,dpdown:h0.4,dpleft:h0.8,dpright:h0.2,dpup:h0.1,guide:b12,leftshoulder:b4,leftstick:b10,lefttrigger:a3,leftx:a0,lefty:a1,misc1:b14,rightshoulder:b5,rightstick:b11,righttrigger:a4,rightx:a2,righty:a5,start:b9,x:b0,y:b3,platform:Mac OS X,"

if [ ! -d "$APP" ]; then
  echo "missing Snes9x app: $APP" >&2
  exit 1
fi

if [ ! -f "$DB" ]; then
  echo "missing Snes9x controller database: $DB" >&2
  exit 1
fi

if pgrep -x Snes9x >/dev/null 2>&1; then
  echo "quit Snes9x before running this setup script" >&2
  exit 1
fi

python3 - <<'PY' "$DB" "$MAPPING_LINE"
import pathlib
import sys

db_path = pathlib.Path(sys.argv[1])
mapping_line = sys.argv[2]

text = db_path.read_text()
lines = text.splitlines()
needle = "030000004c050000e60c000000010000,PS5 Controller,"

if any(line == mapping_line for line in lines):
    raise SystemExit(0)

updated = False
for index, line in enumerate(lines):
    if line.startswith(needle):
        lines[index] = mapping_line
        updated = True
        break

if not updated:
    insert_at = len(lines)
    for index, line in enumerate(lines):
        if line.startswith("030000004c050000f20d000000010000,PS5 Controller,"):
            insert_at = index
            break
    lines.insert(insert_at, mapping_line)

db_path.write_text("\n".join(lines) + "\n")
PY

mkdir -p "$(dirname "$PREF_PLIST")"

if [ ! -f "$PREF_PLIST" ]; then
  defaults write "$PREF_DOMAIN" ShowFPS -bool false >/dev/null
fi

TMP_PLIST="$(mktemp /tmp/snes9x-dualsense.XXXXXX.plist)"

python3 - <<'PY' "$PREF_PLIST" "$TMP_PLIST" "$DEVICE_KEY" "$PLAYER_KEY"
import plistlib
import sys
from pathlib import Path

plist_path = Path(sys.argv[1])
tmp_path = Path(sys.argv[2])
device_key = sys.argv[3]
player_key = sys.argv[4]

mapping = {
    "0": "69:0",
    "1": "69:255",
    "2": "68:0",
    "3": "68:255",
    "4": "52:0",
    "5": "53:0",
    "6": "55:0",
    "7": "54:0",
    "8": "56:0",
    "9": "57:0",
    "10": "61:0",
    "11": "60:0",
}

with plist_path.open("rb") as handle:
    data = plistlib.load(handle)

joypad_inputs = data.setdefault("JoypadInputs", {})
joypad_inputs.pop("1356", None)
joypad_inputs[device_key] = mapping

joypad_players = data.setdefault("JoypadPlayers", {})
joypad_players[player_key] = device_key

with plist_path.open("wb") as handle:
    plistlib.dump(data, handle)

with tmp_path.open("wb") as handle:
    plistlib.dump(data, handle)
PY

defaults import "$PREF_DOMAIN" "$TMP_PLIST"
rm -f "$TMP_PLIST"

echo "DualSense mapping prepared for Snes9x."
echo "Player 1 is assigned to $DEVICE_KEY."
