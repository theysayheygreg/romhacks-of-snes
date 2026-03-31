# SNES Reverse Engineering Workspace

This subfolder is the working area for building a reusable SNES knowledge base:

- how the hardware works
- how commercial ROMs are structured
- how current tools analyze and modify them
- how to get from source or patch data to an emulator and real hardware

## Current sources

- `repos/snes9x`: broad, portable emulator implementation
- `repos/bsnes`: accuracy-focused emulator with strong cartridge modeling
- `repos/DiztinGUIsh`: collaborative disassembly and tracelog tooling
- `repos/snestistics`: trace-guided disassembly focused on LoROM workflows
- `repos/sd2snes`: flash cartridge firmware and FPGA logic
- `repos/SMZ3`: example project that merges Super Metroid and Zelda 3 into one ROM
- `repos/supermetroid`: exact-match Super Metroid NTSC disassembly/rebuild source lane
- `repos/jpdasm`: ALTTP JP1.0 full disassembly and annotations
- `repos/z3randomizer`: assembly-heavy ALTTP randomizer patch base
- `repos/alttp_vt_randomizer`: ALTTP randomizer application and patch-generation stack
- `repos/ALttPDoorRandomizer`: Python-heavy ALTTP door-randomizer generation stack
- `repos/RandomMetroidSolver`: VARIA randomizer/solver/tracker/plandomizer stack
- `repos/MapRandomizer`: Super Metroid map/room-connectivity randomizer stack
- `repos/SMWDisX`: multi-version Super Mario World disassembly/rebuild source lane
- `repos/callisto`: Super Mario World project build-system and orchestration lane
- `repos/smw-project-template`: Super Mario World starter/template lane built around Callisto
- `repos/multirando-asm`: four-game crossover randomizer / architecture repo for SM, ALTTP, Zelda 1, and Metroid 1

## Layout

- `docs/`: human-readable notes and workflows
- `analysis/`: generated outputs and ROM-specific facts
- `build/`: generated ROMs and other local build artifacts
- `roms/`: staged clean base ROMs for workspace-local use
- `data/`: machine-readable graph and metadata
- `tools/`: local helper tools for inspection
- `repos/`: ingested upstream source trees
- `lanes/`: project swim lanes under the shared SNES workspace
- `BACKLOG.md`: durable task list for this workspace
- `WORKLOG.md`: execution-oriented tracking between planning and milestone outputs
- `CHANGELOG.md`: durable milestone log for the workspace itself
- `ROADMAP.md`: phased execution plan for the workspace
- `docs/macos-toolchain.md`: verified macOS setup, interop notes, and build commands
- `docs/randomizer-architecture.md`: conceptual model for seed/logic/spoiler-driven randomizers
- `docs/zelda-randomizer-progression.md`: Zelda-focused note on logic, spheres, and spoiler/playthrough structure
- `docs/metroid-randomizer-progression.md`: Metroid-focused note on logic, presets, solver paths, and reachability
- `docs/smz3-lineage-concepts.md`: concept-level note on what `SMZ3` inherits from Zelda, Metroid, and crossover-specific design work
- `docs/progression-grammar.md`: high-level model of how Zelda, Metroid, topology randomizers, and crossovers structure progression
- `docs/research-resource-index.md`: curated external resource list for general SNES hacking and the three anchor games
- `docs/game-design-three-anchors.md`: comparative design and mechanics note for Zelda 3, Super Metroid, and SMW
- `docs/gemini-deep-research-prompt.md`: reusable prompt for broader Gemini research across videos and community materials
- `docs/gemini-followup-prompts-001.md`: focused Gemini prompts for verification and game-specific follow-up research
- `docs/gemini-research-intake-001.md`: distilled intake note from the first Gemini deep-research brief
- `docs/gemini-reference-verification-intake-001.md`: distilled intake note from the first Gemini reference-verification brief
- `docs/multiworld-architecture-01.md`: first shared note on Archipelago-style multiworld relevance for the workspace
- `docs/emulator-testing-layout.md`: local testing-folder layout and emulator path conventions
- `docs/bsnes-macos-rendering-01.md`: investigation note for the current Apple Silicon `bsnes` black-video issue
- `docs/snes9x-macos-01.md`: current practical macOS `snes9x` app lane and expected config/data paths
- `docs/external-research/`: landing zone for externally generated research briefs before distillation
- `WORKSPACE-STRUCTURE.md`: how shared SNES knowledge and per-project swim lanes are organized
- `lanes/zelda/vanilla-deep-dive-01.md`: first practical vanilla Zelda 3 reverse-engineering note
- `lanes/metroid/vanilla-deep-dive-01.md`: first practical vanilla Super Metroid reverse-engineering note
- `lanes/metroid/plm-room-state-01.md`: first structural note on PLMs and room-state data in Super Metroid
- `lanes/smw/INTAKE.md`: intake checklist for standing up the SMW lane with a base ROM and repos
- `lanes/smw/lunar-magic-01.md`: local Lunar Magic tooling classification and supported-ROM notes
- `lanes/smw/callisto-01.md`: Callisto build-system classification and workflow notes
- `lanes/smw/workflow-model-01.md`: first canonical workflow model note for the SMW lane
- `lanes/smw/vanilla-deep-dive-01.md`: first practical vanilla SMW reverse-engineering note
- `lanes/smw/smw-project-template-01.md`: first classification note for the modern SMW template/starter lane
- `lanes/smw/standalone-rom-01.md`: first standalone SMW ROM artifact note
- `lanes/smz3/multirando-asm-01.md`: crossover note on the four-game `multirando-asm` architecture repo

## Notes

- The example ROMs are analyzed with `tools/rom_probe.py`.
- Clean base ROMs are now staged under `roms/base/` and should be used instead of the iCloud originals.
- Generated local outputs live under `build/`, with conventions documented in `build/README.md`.
- The macOS toolchain is now documented in `docs/macos-toolchain.md`.
- The current `bsnes` Apple Silicon rendering issue and workaround lane are captured in `docs/bsnes-macos-rendering-01.md`.
- The current practical `snes9x` release-app lane is captured in `docs/snes9x-macos-01.md`.
- The current external resource pass is curated in `docs/research-resource-index.md`.
- The current comparative design note for the three anchor games lives in `docs/game-design-three-anchors.md`.
- The first Gemini brief has been distilled into `docs/gemini-research-intake-001.md`.
- The first Gemini reference-verification brief has been distilled into `docs/gemini-reference-verification-intake-001.md`.
- The current multiworld relevance note lives in `docs/multiworld-architecture-01.md`.
- `snes/` is now a standalone git repository for the workspace itself.
- Verified locally on this Mac:
  - `bsnes` source build
  - staged official `snes9x` macOS release app
  - `SMZ3` CLI build and help output
  - `MapRandomizer` Rust workspace check after submodule hydration
  - `z3randomizer` patch-first ROM generation
- The current Metroid anchor note lives in `lanes/metroid/vanilla-deep-dive-01.md`.
- The current Metroid PLM/state companion note lives in `lanes/metroid/plm-room-state-01.md`.
- The current Zelda anchor note lives in `lanes/zelda/vanilla-deep-dive-01.md`.
- The current SMW anchor note lives in `lanes/smw/vanilla-deep-dive-01.md`.
- The SMW lane now has its first standalone ROM artifact and starter-template classification.
- `repos/supermetroid` exactly matches the local Super Metroid ROM by SHA-1 and is now the canonical Metroid source-reference lane.
- `repos/jpdasm` exactly matches the local Zelda JP ROM by SHA-1/MD5 and is the canonical Zelda source-reference lane.
- This workspace is SNES-only. Non-SNES reverse-engineering work should live in a separate workspace.
