# SNES System Model

## Core hardware model

The practical reverse-engineering target is not just "the SNES", but a layered system:

- `5A22` main CPU: a 65c816-derived CPU with DMA/HDMA and memory-mapped I/O
- `PPU1/PPU2`: tile/sprite/background hardware with access mediated through registers
- `SPC700 + DSP`: separate audio CPU and sound DSP
- `WRAM`: 128 KiB of main work RAM, conventionally in banks `7E-7F`
- `Cartridge space`: ROM, SRAM, and optional enhancement chips mapped into the CPU address space

For emulator-backed study, the most relevant truth sources in this workspace are:

- `../repos/snes9x/memmap.cpp`
- `../repos/snes9x/apu/`
- `../repos/bsnes/bsnes/sfc/cpu/`
- `../repos/bsnes/bsnes/sfc/ppu/`
- `../repos/bsnes/bsnes/sfc/smp/`
- `../repos/bsnes/bsnes/sfc/cartridge/`

## Memory map patterns that matter for hacks

The parts you touch most when modifying games are:

- CPU-visible WRAM:
  - banks `7E-7F`
  - used for runtime state, decompressed buffers, entity state, temporary work areas
- Hardware registers:
  - mirrored across low banks
  - PPU registers live in the `0x2000-0x3FFF` region
  - CPU/DMA/control registers live in the `0x4000-0x5FFF` region
- Cartridge ROM/RAM:
  - mapped differently depending on `LoROM`, `HiROM`, and special-chip boards

`snes9x` is a good map-centric reference here. In `memmap.cpp`, `ScoreLoROM` / `ScoreHiROM` identify probable mappings, and the `map_*` functions show how ROM, SRAM, WRAM, DSP, SA-1, SuperFX, and other board types are wired into CPU-visible banks.

## LoROM vs HiROM in practice

For current hacking work, the two common mental models are:

- `LoROM`
  - ROM appears in 32 KiB windows, usually at `8000-FFFF` in many banks
  - common for many first-party and fan-hack targets
  - both example ROMs in this workspace currently score as LoROM
- `HiROM`
  - larger contiguous 64 KiB windows
  - changes bank math and pointer conventions

`bsnes` models this one level higher than `snes9x`: it loads a cartridge manifest and board description rather than only inferring mapping from header bytes. That is useful when a hack grows beyond "plain LoROM/HiROM with no extras" into unusual boards or enhancement chips.

## Enhancement chips and edge cases

Any serious SNES knowledge base has to treat "special chips" as first-class:

- `SA-1`
- `SuperFX`
- `DSP1/2/4`
- `Cx4`
- `SPC7110`
- `SDD1`
- `MSU1` as a modern extension used by hacks and patches

These are not cosmetic details. They change:

- address decoding
- timing assumptions
- what must be emulated accurately
- what a flashcart must support
- how a patch can safely allocate or stream data

`snes9x` exposes this in the many specialized `Map_*` functions. `bsnes` exposes it through `bsnes/sfc/coprocessor/`, `bsnes/sfc/cartridge/`, and board manifests.

## What a ROM hack usually changes

At the binary level, most SNES modifications fall into a few buckets:

- code patches:
  - inject or replace 65c816 routines
- data edits:
  - item tables, room tables, scripts, object layouts, pointers
- asset edits:
  - graphics, palettes, tilemaps, music/sample data
- map/layout edits:
  - rooms, exits, event flags, portals, progression logic
- mapper-aware expansion:
  - moving code/data to new free banks and repointing callers
- hardware-extension integration:
  - MSU1, SA-1, or flashcart-assisted workflows

The key constraint is always the same: every change has to remain consistent with the original game's bank layout, pointer format, and runtime assumptions.
