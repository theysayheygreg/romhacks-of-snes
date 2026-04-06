# Changelog

All notable changes to the SNES workspace should be recorded here.

This changelog is for the workspace itself:

- structure
- tooling
- research assets
- analysis artifacts
- milestone ROM-generation capability

It is not a full session transcript.

## 2026-03-31

### Added

- Second standalone SMW ROM artifact note for a visible gameplay patch.
- `apply_smw_starting_lives_09.sh` helper for producing a checksum-fixed SMW gameplay test ROM.
- `smw-starting-lives-09.asm` as the first visible gameplay patch in the SMW lane.
- App-path-aware `snes9x` launcher and DualSense setup helpers so staged release builds and source-built test apps can share the same harness.
- `docs/tas-harnesses-01.md` as the first shared note on TAS and TAS-adjacent automation lanes for the three anchor games.
- `docs/tas-harness-sketches-01.md` plus machine-readable harness manifests under `data/tas-harnesses/`.
- `tools/validate_tas_harnesses.py` for checking harness-manifest structure.
- `lanes/metroid/tas-harness-01.md`, `harness/scenarios/super-metroid-known-door-transition.json`, and `tools/run_tas_harness.py` as the first concrete Metroid harness slice.
- `analysis/validation/super-metroid-known-door-transition-preflight.json` as the first generated Metroid harness result artifact.
- `lanes/metroid/practice-hack-01.md` as the first classification note for `sm_practice_hack` as a Metroid testing/instrumentation asset.
- Host-resolution support in `tools/run_tas_harness.py` so harness artifacts can record whether they are in real automation or manual-assist fallback mode on this Mac.
- `tools/run_tas_manual_assist.py` as the first operator-facing launcher for the current Metroid `Snes9x` manual-assist lane.
- `tools/complete_tas_manual_assist.py` as the first completion tool for turning a pending manual-assist artifact into a pass/fail result.
- `analysis/validation/super-metroid-known-door-transition-manual-assist.json` as the first generated manual-assist harness artifact.
- `lanes/smw/tas-harness-01.md` and `harness/scenarios/smw-starting-lives-09.json` as the first concrete SMW manual-assist harness lane.
- `analysis/validation/smw-starting-lives-09-preflight.json` and `analysis/validation/smw-starting-lives-09-manual-assist.json` as the first generated SMW harness artifacts.
- `lanes/zelda/tas-harness-01.md` and `harness/scenarios/zelda3-fresh-file-boot.json` as the first concrete Zelda manual-assist harness lane.
- `analysis/validation/zelda3-fresh-file-boot-preflight.json` and `analysis/validation/zelda3-fresh-file-boot-manual-assist.json` as the first generated Zelda harness artifacts.

### Changed

- Standardized the practical macOS emulator lane on `snes9x` while parking `bsnes` as renderer/debug R&D.
- Extended the SMW lane from header-only artifact generation to a real gameplay-state patch workflow.
- Added a reusable DualSense setup path for the staged `snes9x` app on this Mac.
- Added a separate `snes9x` controller-test app with a stronger analog-stick dead zone for local drift comparison.
- Added the first explicit backlog slice for TAS-style deterministic smoke testing across the shared SNES lane plus Zelda, Metroid, and SMW.

### Verified

- SMW U start-lives patch at `00:9E24` changes the initialization immediate from `#$04` to the internal value `#$08`, which displays as 9 lives in-game.
- `smw-starting-lives-09.sfc` boots correctly in `snes9x` with the expected 9 starting lives behavior.
- The staged `snes9x` app now accepts the connected DualSense as Player 1 through the workspace setup helper.
- A source-built universal `Snes9x.app` with a `0.5` stick dead zone launches correctly on this Mac as a separate test lane.
- The first Metroid harness slice can now launch through the local `Snes9x` app and emit a machine-readable manual-assist checklist artifact for operator verification.
- The first Metroid harness slice now has a concrete path from pending checklist artifact to final pass/fail result without needing full emulator automation yet.
- The first SMW harness slice now uses the same preflight plus manual-assist plus completion flow against the visible start-lives patch ROM.
- The first SMW harness slice is now recorded as a real `pass` result.
- The first Zelda harness slice now uses the same preflight plus manual-assist flow against the exact-match JP base ROM.

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
- Follow-up `bsnes` Metal render-loop refinement on macOS, keeping the patched vendored lane clean on `codex/metal-macos`.
