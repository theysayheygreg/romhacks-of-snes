# Snes9x macOS Note 01

This note captures the current practical `snes9x` lane for the SNES workspace on macOS.

## Current status

The simplest working macOS path is the official app release, not a local source build.

Staged app:

- `/Users/theysayheygreg/Documents/SNES/emulators/Snes9x-1.63.app`

Source archive used:

- `https://github.com/snes9xgit/snes9x/releases/download/1.63/snes9x-1.63-Mac.zip`

Verified app facts:

- version `1.63`
- universal binary
- contains both `x86_64` and `arm64`
- bundle identifier `com.snes9x.macos.snes9x`

Verified runtime facts on this Mac:

- the app opens cleanly on Apple Silicon
- ROM loading works through the app's native Cocoa `open` path
- stock `Super Mario World (USA).sfc` loads with a visible gameplay surface
- the reliable scripted launcher is:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/open_in_snes9x.sh`

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

- `open -a Snes9x <rom>` was not a reliable ROM handoff here
- using AppleScript `tell application "Snes9x" to open POSIX file ...` is reliable

## Workspace role

For this Mac, `snes9x` should be treated as:

- the practical GUI emulator lane for quick ROM testing
- the default runtime lane while `bsnes` remains in R&D
- the emulator we should keep using while the workspace returns to actual ROMhacking work

`bsnes` still remains useful as:

- a reference codebase
- an accuracy-oriented research lane
- a future debugger/reference lane if the macOS rendering issue is resolved

Current `bsnes` note:

- the Metal branch now proves visible native window output on Apple Silicon
- the remaining bug is the real-frame upload path, not macOS window creation
- that is useful progress, but not enough to justify blocking ROM work on further `bsnes` effort right now
