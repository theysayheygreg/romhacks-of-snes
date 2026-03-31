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
- First-pass canonical SMW workflow model note.
- First-pass canonical vanilla SMW deep-dive note and key-symbol map.
- First SMW template/starter-lane classification note for `smw-project-template`.
- First standalone SMW ROM artifact note and helper patch script.
- Emulator testing layout note and a sync script for a Documents-based shared load folder.
- `bsnes` macOS rendering investigation note and an `x86_64` Rosetta workaround lane.
- `bsnes` Metal backend implementation note and staged native test app.
- `snes9x` macOS practical-lane note and staged release app path.
- Local `bsnes` Metal-backend patch lane and staged patched app path.
- First-pass canonical Metroid PLM and room-state note.
- `multirando-asm` crossover note and knowledge-graph expansion for four-game composite-ROM architecture.
- First shared note on multiworld / Archipelago-style architectural relevance.
- Research resource index, comparative game-design note, and Gemini deep-research prompt.
- Gemini research intake note capturing verified leads versus claims still requiring primary-source confirmation.
- Gemini reference-verification intake note with promoted follow-up leads for debugger, Zelda, Metroid, and SMW lanes.
- Nested git repository for `snes/`.

### Changed

- Standardized the workspace on staged local base ROM copies under `roms/base/`.
- Updated docs and notes to reference staged local ROM copies rather than iCloud source paths.
- Promoted the SMW lane from intake-only status into a concrete analysis and output lane.

### Verified

- `bsnes` source build on macOS.
- `SMZ3` CLI build and help output on macOS with runtime roll-forward.
- `MapRandomizer` Rust workspace check on macOS after submodule hydration.
- `z3randomizer` patch-first ROM generation path.
- `smw-project-template` repo identity and workflow shape against the current SMW lane model.
- Standalone SMW patch-first ROM generation via bundled Asar with checksum repair.
- `bsnes` path layout against a unified `~/Documents/SNES/` testing directory.
- The current upstream `bsnes` nightly macOS asset architecture and the locally built `x86_64` Rosetta test app shape for the Apple Silicon rendering issue.
- The vendored `bsnes` source lane now has a native Metal backend branch and a clean Metal-enabled macOS app build.
- The official `snes9x` macOS release app source URL, architecture shape, and expected app data/config roots.
- Clean local `bsnes` Metal-backend build on macOS and automatic migration from `OpenGL 3.2` settings to `Metal`.
