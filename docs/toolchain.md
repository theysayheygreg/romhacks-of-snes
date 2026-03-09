# Toolchain and Workflow

## Emulators

### bsnes

`bsnes` is the best local source here for understanding high-fidelity cartridge modeling and subsystem boundaries.

What it is especially good for:

- cartridge manifests and board-aware loading
- subsystem separation by hardware block
- special-chip coverage
- patch-friendly runtime features like IPS/BPS soft-patching

Relevant local paths:

- `../repos/bsnes/bsnes/sfc/cartridge/cartridge.cpp`
- `../repos/bsnes/bsnes/sfc/cartridge/load.cpp`
- `../repos/bsnes/bsnes/sfc/cpu/`
- `../repos/bsnes/bsnes/sfc/ppu/`
- `../repos/bsnes/bsnes/sfc/coprocessor/`

Recommended role in this workspace:

- primary accuracy/reference emulator
- useful when we need to understand what hardware-faithful behavior should look like
- not the sole success criterion, because real hardware via `sd2snes` is the final target

### snes9x

`snes9x` is the pragmatic counterweight: widely used, portable, and easier to mine for mapping heuristics and compatibility-oriented behavior.

What it is especially good for:

- ROM type scoring (`LoROM` vs `HiROM`)
- explicit memory map construction
- broad emulator compatibility knowledge

Relevant local paths:

- `../repos/snes9x/memmap.cpp`
- `../repos/snes9x/snapshot.cpp`
- `../repos/snes9x/apu/`

Recommended role in this workspace:

- secondary compatibility/reference emulator
- useful for understanding long-lived emulator conventions and broad compatibility behavior
- valuable as source code, even when the final pass is on real hardware

## Reverse-engineering tools

### jpdasm

`jpdasm` is a highly relevant Zelda-specific source artifact: a full disassembly of the Japanese 1.0 version of A Link to the Past that aims to reassemble exactly back to the original ROM.

High-value traits:

- bank-split assembly source across the game
- explicit labels and annotations
- ROM extraction tooling via `binextract.py`
- build scaffolding via `Makefile` and `_build.bat`
- WRAM, SRAM, and APU symbol files

Important constraint:

- it requires binary assets extracted from a local `alttp.sfc` into a `bin/` directory before full reassembly
- the repo ships a Windows-specific `asarmon.exe`, but also includes a `Makefile` and Python extraction path, so it is not purely Windows-locked

Relevant local paths:

- `../repos/jpdasm/README.md`
- `../repos/jpdasm/Makefile`
- `../repos/jpdasm/binextract.py`
- `../repos/jpdasm/main.asm`
- `../repos/jpdasm/symbols_wram.asm`
- `../repos/jpdasm/symbols_sram.asm`

### z3randomizer

`z3randomizer` looks like the low-level ALTTP randomizer patch layer: lots of focused `.asm` modules, Asar-based build scripts, ROM header edits, and direct hook/data patching.

High-value traits:

- patch-first and assembly-centric
- platform-specific build helpers under `bin/`
- direct ROM changes like FastROM flags, hooks, HUD, items, events, and randomizer-specific systems

Relevant local paths:

- `../repos/z3randomizer/build.sh`
- `../repos/z3randomizer/LTTP_RND_GeneralBugfixes.asm`
- `../repos/z3randomizer/hooks.asm`
- `../repos/z3randomizer/zelda.asm`
- `../repos/z3randomizer/ram.asm`

### alttp_vt_randomizer

`alttp_vt_randomizer` sits higher in the stack: it is an application-level randomizer with CLI/web flows that takes a base ROM, generates patch/build state, and writes out randomized results.

High-value traits:

- explicit base-ROM workflow
- command-line generation path
- web application and API layer
- built-in use of patching tools like `asar` and `flips`
- useful for understanding the "randomizer service/application" side rather than only the patch payload side

Relevant local paths:

- `../repos/alttp_vt_randomizer/readme.md`
- `../repos/alttp_vt_randomizer/app/Randomizer.php`
- `../repos/alttp_vt_randomizer/app/Rom.php`
- `../repos/alttp_vt_randomizer/routes/console.php`
- `../repos/alttp_vt_randomizer/bin/`

### ALttPDoorRandomizer

`ALttPDoorRandomizer` looks like a distinct Python-heavy randomizer line focused on deeper dungeon/door topology changes, with its own CLI/GUI, modeling code, and ROM-writing layer.

High-value traits:

- strong logic/modeling layer for doors, dungeons, keys, overworld shuffle, and mystery/plando modes
- explicit CLI and GUI entry points
- ROM-writing layer in Python
- BPS patch artifact in `data/base2current.bps`

Relevant local paths:

- `../repos/ALttPDoorRandomizer/README.md`
- `../repos/ALttPDoorRandomizer/DungeonRandomizer.py`
- `../repos/ALttPDoorRandomizer/DoorShuffle.py`
- `../repos/ALttPDoorRandomizer/Rom.py`
- `../repos/ALttPDoorRandomizer/data/base2current.bps`

### RandomMetroidSolver

`RandomMetroidSolver` is the `VARIA` stack: a Super Metroid randomizer plus solver, tracker, plandomizer, and customization tooling.

High-value traits:

- explicit split between randomizer and solver
- skill presets and randomizer presets
- progression-speed and progression-difficulty tuning
- spoiler-path generation through the solver
- patch/customization tooling around generated ROMs

Relevant local paths:

- `../repos/RandomMetroidSolver/README.md`
- `../repos/RandomMetroidSolver/randomizer.py`
- `../repos/RandomMetroidSolver/solver.py`
- `../repos/RandomMetroidSolver/logic/`
- `../repos/RandomMetroidSolver/rando/`
- `../repos/RandomMetroidSolver/patches/`

### supermetroid

`supermetroid` is the strongest current vanilla/source lane for Super Metroid in this workspace: a bank-split disassembly that rebuilds the NTSC ROM and explicitly states the target SHA-1.

High-value traits:

- exact target-ROM statement in the README
- bank-split source files from `bank80.asm` through `bankb6.asm`
- dedicated `ram.asm` and `sram.asm`
- reproducible source build on macOS via `make`
- bundled `wla-dx` toolchain vendor tree

Critical result:

- the repo README states SHA-1 `da957f0d63d14cb441d215462904c4fa8519c613`
- the local example ROM hashes to that same SHA-1
- so this repo is a revision-matched source reference for the exact local Super Metroid ROM, not just a related disassembly

Relevant local paths:

- `../repos/supermetroid/README.md`
- `../repos/supermetroid/Makefile`
- `../repos/supermetroid/src/main.asm`
- `../repos/supermetroid/src/bank8f.asm`
- `../repos/supermetroid/src/ram.asm`
- `../repos/supermetroid/src/sram.asm`

### MapRandomizer

`MapRandomizer` is a Super Metroid randomizer line focused on room connectivity and map topology, with substantial logic and reachability infrastructure.

High-value traits:

- room-connection and map-pool driven seed generation
- explicit reachability engine
- Rust, Python, and C++ components
- web and CLI generation paths
- patch sources and ROM-output tooling

Relevant local paths:

- `../repos/MapRandomizer/README.md`
- `../repos/MapRandomizer/rust/maprando-web/`
- `../repos/MapRandomizer/rust/maprando-logic/`
- `../repos/MapRandomizer/rust/maprando-game/`
- `../repos/MapRandomizer/cpp/reachability.cpp`
- `../repos/MapRandomizer/patches/`

### DiztinGUIsh

`DiztinGUIsh` is less "automatic decompiler" and more "human-guided disassembly workspace".

High-value traits:

- imports BSNES/BizHawk execution data
- supports live trace capture from a special BSNES+ build over a socket
- exports assembly intended to round-trip through `asar`
- supports plain-text `.dizraw` project files for Git-friendly collaboration

Relevant local paths:

- `../repos/DiztinGUIsh/README.md`
- `../repos/DiztinGUIsh/TRACE CAPTURE INSTRUCTIONS.md`
- `../repos/DiztinGUIsh/Diz.Import/src/bsnes/tracelog/`
- `../repos/DiztinGUIsh/Diz.Core/serialization/`

### snestistics

`snestistics` is trace-driven and report-oriented. It is narrower than Diz, but useful.

Strengths:

- generates assembler source from trace-backed knowledge
- emits data, DMA, branch, and rewind-style reports
- keeps annotations separate so you can iteratively refine output

Important limitation:

- current project docs explicitly say the usable emulator side is Windows-only
- current docs also say it only supports `LoROM` games

Relevant local paths:

- `../repos/snestistics/docs/index.md`
- `../repos/snestistics/source/trace.h`
- `../repos/snestistics/source/snestistics.cpp`

## Hardware deployment

### sd2snes

`sd2snes` is the bridge from "ROM file on disk" to "ROM running on a real SNES".

Why it matters:

- it contains both firmware and FPGA mapping logic
- it shows what real hardware deployment must support for flash loading, special chips, MSU1, USB-driven workflows, and some savestate features
- it is a concrete reference for which board behaviors are realistically deployable

Recommended role in this workspace:

- final deployment and validation path
- usually not the first thing to inspect during routine ROM analysis
- important whenever we need to answer "does this still behave like a valid SNES cartridge on real hardware?"

Relevant local paths:

- `../repos/sd2snes/src/`
- `../repos/sd2snes/verilog/`
- `../repos/sd2snes/src/usbinterface.c`
- `../repos/sd2snes/src/msu1.c`
- `../repos/sd2snes/src/snes.h`

## Recommended workflow in this workspace

1. Fingerprint the ROM.
2. Run it in an emulator that matches the question.
3. Capture execution or usage data.
4. Build annotations and labels.
5. Export or author patches/assembly.
6. Validate in emulator again.
7. Validate on `sd2snes`-class hardware if the change depends on real hardware behavior.

Current local helper:

- `../tools/rom_probe.py`

## Patch-first vs source-reconstruction workflows

A useful distinction for this workspace:

- `source-reconstruction` workflows try to recover enough labeled assembly or structure to rebuild the original ROM exactly or near-exactly
- `patch-first` workflows assume a known-good base ROM and emit targeted binary or assembly patches on top of it

For modern SNES randomizers and many active romhacking communities, the dominant workflow is usually patch-first:

- start from a canonical base ROM
- inject or replace specific routines
- rewrite data tables, item locations, and game logic
- emit a new playable ROM by applying generated patches to the base

That means we should treat these as separate but related lanes:

- `jpdasm` is a source-reconstruction style artifact for Zelda 3
- `z3randomizer` is a low-level patch/randomizer codebase for Zelda 3
- `alttp_vt_randomizer` is a higher-level randomizer application that still targets a canonical base ROM
- `ALttPDoorRandomizer` is a Python-heavy randomizer/modeling codebase with deeper dungeon-door manipulation
- `RandomMetroidSolver` is a Super Metroid seed-generation + solver + tracker stack
- `MapRandomizer` is a Super Metroid map-topology randomizer with explicit reachability modeling
- `SMZ3` is primarily a patch-generation/build pipeline over base ROM inputs
- many future hacks we ingest will likely look more like `SMZ3` than like a full disassembly

Practically, this means "understanding how to make SNES hacks" does not require full source recovery for every game. Often the real task is:

- identify the correct base ROM revision
- understand enough code/data structure to patch safely
- maintain deterministic patch application and validation

There is also an important middle-to-far end of the spectrum:

- some ecosystems, especially `Super Mario World`, evolved into reconstruction-heavy, assembly-first workflows
- they may still use the original ROM as a compatibility anchor, but large portions of game behavior, assets, and structure are effectively replaced or rewritten
- tools like `Lunar Magic` sit on top of deep format knowledge plus targeted ASM modifications and can support projects that feel much closer to "authoring a new game on the original engine substrate" than to "patching a few routines"

So the actual continuum looks more like:

- small patch over canonical base ROM
- randomizer-style generated patch pipeline
- deep assembly hack with major engine rewrites
- editor-assisted reconstruction-heavy project that still emits a valid SNES ROM

Most of these communities still stay assembly-centric at the final authored layer. Even when tooling gets sophisticated, the output is usually still:

- assembly patches
- binary assets
- pointer/data table updates

rather than a fully high-level game codebase compiled through an abstract runtime.

## Current Mac status

The current macOS lane is operational enough for active work:

- `cmake`, `wget`, `php`, `composer`, `rustup`, `dotnet@8`, `dotnet@9`, and `asar` are installed
- `bsnes` builds locally from source as a native arm64 app bundle
- `SMZ3` builds locally with the `.NET 9` SDK and runs when `DOTNET_ROLL_FORWARD=Major` is set
- `MapRandomizer` builds through `cargo check` once its submodules are initialized
- `z3randomizer` can emit a patched ALTTP ROM from the example Zelda base ROM

Interop notes:

- `SMZ3` targets `net7.0`, so the current Mac lane uses SDK/runtime roll-forward rather than a dedicated `.NET 7` runtime
- `MapRandomizer` must be cloned with submodules or repaired with `git submodule update --init --recursive`
- `z3randomizer` should be invoked from its repository root so its relative data-file includes resolve correctly
- `jpdasm` still depends on `asarmon`, not stock `asar`
- `alttp_vt_randomizer` now has its PHP/composer prerequisites installed, but its app/database workflow is not yet verified here
- `DiztinGUIsh` and the most useful `snestistics` capture flows remain Windows-assisted rather than Mac-native

See `docs/macos-toolchain.md` for the exact commands and verified outputs.

Windows note:

- Windows-only tooling is not a project goal by itself.
- If `DiztinGUIsh` or `snestistics` provide uniquely valuable capture/disassembly workflows, we can treat Windows as an auxiliary lane rather than a primary platform requirement.
