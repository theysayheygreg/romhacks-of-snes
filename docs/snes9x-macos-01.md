# Snes9x macOS Note 01

This note captures the current practical `snes9x` lane for the SNES workspace on macOS.

## Current status

The simplest working macOS path is the official app release, not a local source build.

Staged app:

- `/Users/theysayheygreg/Documents/SNES/emulators/Snes9x-1.63.app`

Current custom controller-test app:

- `/Users/theysayheygreg/Documents/SNES/emulators/Snes9x-1.63-deadzone-05.app`

Current local harness/debug app:

- `/Users/theysayheygreg/Documents/SNES/emulators/Snes9x-1.63-no-rominfo.app`

Source archive used:

- `https://github.com/snes9xgit/snes9x/releases/download/1.63/snes9x-1.63-Mac.zip`

Verified app facts:

- version `1.63`
- universal binary
- contains both `x86_64` and `arm64`
- bundle identifier `com.snes9x.macos.snes9x`

Verified runtime facts on this Mac:

- the app opens cleanly on Apple Silicon
- ROM loading works through a normal `open -a Snes9x <rom>` handoff
- stock `Super Mario World (USA).sfc` loads with a visible gameplay surface
- the connected PS5 DualSense is detected by `Snes9x` as vendor `0x054c`, product `0x0ce6`
- the staged release app needed an updated `gamecontrollerdb.txt` entry because the bundled DB lacked the upstream macOS PS5 mapping
- the most reliable local fix is to write the DualSense HID cookie bindings directly into `Snes9x` prefs for this machine
- the current workspace mapping uses the DualSense left stick for SNES directions
- the reliable scripted launcher is:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/open_in_snes9x.sh`
- the reliable DualSense setup helper is:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/setup_snes9x_dualsense.sh`
- both helpers now accept `APP=/absolute/path/to/Snes9x.app` so the stable lane and custom test builds can share the same workflow

## Why this is the current practical lane

- the local `snes9x` source repo includes a real macOS Cocoa/Xcode app lane under `repos/snes9x/macosx`
- this Mac's current `xcodebuild` environment is broken before project load due an Xcode plug-in initialization failure
- `xcodebuild -runFirstLaunch` reports that authorization is required to repair/install the missing packages
- the official release app avoids that local Xcode blocker entirely

## Expected app data paths

The Homebrew cask metadata for `snes9x` identifies these macOS paths:

- `~/Library/Application Support/Snes9x`
- `~/Library/Preferences/com.snes9x.macos.snes9x.plist`
- `~/Library/Saved Application State/com.snes9x.macos.snes9x.savedState`

These should be treated as the likely app-level config and data roots for the current release app.

Observed note:

- the simplest working launcher in this workspace is now a plain `open -a` helper script
- the simplest controller fix is to patch the staged app bundle's SDL controller database with the upstream PS5 macOS mapping and then install a direct DualSense binding set for `1356:3302:0`
- `Snes9x` persists only one input per SNES direction in prefs, so this local setup uses the left stick rather than duplicating both stick and D-pad
- a custom source-built app now exists with a firmer `0.5` left-stick dead zone for drift testing on this older DualSense
- a second custom source-built app now exists for harness/debug use with the startup ROM-info overlay disabled and viewport mouse clicks ignored
- that local harness build was used to confirm that clean Zelda can boot and start a real save file via keyboard without the earlier click-triggered hang

## Workspace role

For this Mac, `snes9x` should be treated as:

- the practical GUI emulator lane for quick ROM testing
- the default runtime lane while `bsnes` remains in R&D
- the emulator we should keep using while the workspace returns to actual ROMhacking work

Current status:

- the stable release app remains the default day-to-day lane
- the custom `deadzone-05` app is a side-by-side controller experiment lane
- the custom `no-rominfo` app is the local harness/debug lane for isolating macOS focus/input issues
- the DualSense is working as Player 1 in the stable harness
- the first visible SMW gameplay patch boots and plays correctly through this setup

`bsnes` still remains useful as:

- a reference codebase
- an accuracy-oriented research lane
- a future debugger/reference lane if the macOS rendering issue is resolved

Current `bsnes` note:

- the Metal branch now proves visible native window output on Apple Silicon
- the remaining bug is the real-frame upload path, not macOS window creation
- that is useful progress, but not enough to justify blocking ROM work on further `bsnes` effort right now
