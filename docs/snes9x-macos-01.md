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

## Workspace role

For this Mac, `snes9x` should be treated as:

- the practical GUI emulator lane for quick ROM testing
- a fallback runtime lane when `bsnes` is blocked by the current Apple Silicon rendering issue

`bsnes` still remains useful as:

- a reference codebase
- an accuracy-oriented research lane
- a future debugger/reference lane if the macOS rendering issue is resolved
