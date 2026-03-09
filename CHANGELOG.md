# Changelog

All notable changes to the SNES workspace should be recorded here.

This changelog is for the workspace itself:

- structure
- tooling
- research assets
- analysis artifacts
- milestone ROM-generation capability

It is not a full session transcript.

## 2026-03-09

### Added

- Shared SNES workspace structure with swim lanes for Zelda, Metroid, SMZ3, and SMW.
- macOS toolchain notes and helper scripts.
- ROM probe tooling and analysis artifacts for Zelda, Super Metroid, and SMW.
- First-pass deep-dive notes for Zelda and Super Metroid.
- SMW intake, Lunar Magic notes, and `callisto` build-system notes.
- Research resource index, comparative game-design note, and Gemini deep-research prompt.
- Nested git repository for `snes/`.

### Changed

- Standardized the workspace on staged local base ROM copies under `roms/base/`.
- Updated docs and notes to reference staged local ROM copies rather than iCloud source paths.

### Verified

- `bsnes` source build on macOS.
- `SMZ3` CLI build and help output on macOS with runtime roll-forward.
- `MapRandomizer` Rust workspace check on macOS after submodule hydration.
- `z3randomizer` patch-first ROM generation path.
