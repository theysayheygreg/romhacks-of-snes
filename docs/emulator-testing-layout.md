# Emulator Testing Layout

This note defines the local testing layout for GUI emulators, with `snes9x` now serving as the practical macOS play-test lane.

## Source-of-truth layout

Keep the workspace itself as the source of truth:

- clean staged base ROMs:
  - `../roms/base/`
- generated local ROM outputs:
  - `../build/`
- tracked patch sources, notes, and helper scripts:
  - `../patches/`
  - `../tools/`
  - lane notes under `../lanes/`

Important distinction:

- the repo tracks the patching/build logic and notes
- generated ROM binaries remain disposable local outputs

## Documents-side testing layout

Use a user-facing testing area at:

- `~/Documents/SNES/`

Within it:

- `base-roms`
  - symlink to `../roms/base/`
- `build-roms`
  - symlink to `../build/`
- `emulator-ready`
  - curated symlink folder for ROMs that should be easy to load in emulators
- `emulator-data/bsnes/`
  - `saves/`
  - `states/`
  - `screenshots/`
  - `cheats/`
  - `patches/`

This gives us:

- one stable location for clean ROMs
- one stable location for generated ROMs
- one simple load folder for GUI emulators
- emulator side-effect files separated from the repo and from the curated load folder

## bsnes configuration

`bsnes` stores settings at:

- `~/Library/Application Support/bsnes/settings.bml`

Recommended path targets:

- `Path/Games`
  - `~/Documents/SNES/emulator-ready`
- `Path/Recent/SuperFamicom`
  - `~/Documents/SNES/emulator-ready`
- `Path/Saves`
  - `~/Documents/SNES/emulator-data/bsnes/saves`
- `Path/States`
  - `~/Documents/SNES/emulator-data/bsnes/states`
- `Path/Screenshots`
  - `~/Documents/SNES/emulator-data/bsnes/screenshots`
- `Path/Cheats`
  - `~/Documents/SNES/emulator-data/bsnes/cheats`
- `Path/Patches`
  - `~/Documents/SNES/emulator-data/bsnes/patches`

## snes9x status

The current practical `snes9x` app lane is:

- `/Users/theysayheygreg/Documents/SNES/emulators/Snes9x-1.63.app`

Expected app-level paths:

- `~/Library/Application Support/Snes9x`
- `~/Library/Preferences/com.snes9x.macos.snes9x.plist`
- `~/Library/Saved Application State/com.snes9x.macos.snes9x.savedState`

The local `snes9x` source tree is still present under `repos/snes9x/`, but the local `xcodebuild` path is currently blocked by the host Xcode installation state.

Important implication:

- the shared `~/Documents/SNES/emulator-ready` folder can be the cross-emulator load target
- and the staged release app is now the default quick-test launcher
- `snes9x` appears to use macOS preferences / `NSUserDefaults`, not a simple text config file like `bsnes`

Reliable launcher:

- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/open_in_snes9x.sh`

DualSense setup helper:

- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/setup_snes9x_dualsense.sh`

Current controller note:

- the connected PS5 DualSense is seen by `Snes9x` as device key `1356:3302:0`
- local `Snes9x 1.63` shipped without the matching macOS PS5 SDL mapping
- the workspace helper patches that app bundle resource and installs a direct Player 1 binding set for the local DualSense HID cookies

Verified load example:

```sh
/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/open_in_snes9x.sh \
  "/Users/theysayheygreg/Documents/SNES/emulator-ready/Super Mario World (USA).sfc"
```

## Current emulator app paths

Practical GUI launchers currently staged for this Mac:

- `bsnes` native Metal test build:
  - `/Users/theysayheygreg/Documents/SNES/emulators/bsnes-metal-20260331.app`
- `bsnes` Rosetta workaround candidate:
  - `/Users/theysayheygreg/Documents/SNES/emulators/bsnes-x86_64-20260309.app`
- `snes9x` release app:
  - `/Users/theysayheygreg/Documents/SNES/emulators/Snes9x-1.63.app`

Current preferred quick-test order:

1. `snes9x` release app
2. real hardware via `sd2snes` when we have stronger standalone ROM artifacts
3. `bsnes` only when we are explicitly doing renderer/debug R&D

Current `bsnes` checkpoint:

- the Metal branch can now present a visible native window surface on Apple Silicon
- the remaining bug is real-frame upload, so `bsnes` stays parked as R&D
- do not spend routine ROM-testing time there unless we deliberately re-open that engineering task

## Refresh workflow

Use:

- `../tools/sync_emulator_library.sh`

to rebuild the `~/Documents/SNES/` symlink layout after new ROM outputs are generated.
