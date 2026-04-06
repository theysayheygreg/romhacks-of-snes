# Zelda TAS Harness Note 01

This note captures the first concrete TAS-adjacent harness lane for Zelda 3 / ALTTP.

## Why this is the first Zelda harness slice

Zelda does not currently have the same obvious public emulator-script stack in this workspace that Super Metroid does.

So the right first move is not a replay movie. It is a small fresh-file smoke test that can later evolve into stronger RAM-state observation.

This keeps the Zelda lane honest:

- the base ROM is exact-match and already fingerprinted
- the current practical host on this Mac is still `Snes9x`
- the first useful question is whether a fresh file reaches stable controllable state without corruption or hang

## First scenario choice

The first concrete scenario for this lane is:

- `zelda3-fresh-file-boot`

Its job is to prove one short stable slice works:

- ROM boots
- a fresh save can start
- the game reaches an early controllable state
- visible HUD and world state look sane

The second concrete scenario for this lane is:

- `zelda3-basic-world-state`

Its job is to keep the same short fresh-file slice, but tie it back to trusted Zelda state anchors:

- `MODE = $7E0010`
- `SUBMODE = $7E0011`
- `INDOORS = $7E001B`
- `ROOM_FLAGS_WRAM_START = $7EF000`
- `OverworldEventDataWRAM = $7EF280`
- `ProgressIndicator = $7EF3C5`
- `CurrentWorld = $7EF3CA`
- `FollowerIndicator = $7EF3CC`

## Current implementation status

This workspace now has:

- a machine-readable scenario manifest at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/harness/scenarios/zelda3-fresh-file-boot.json`
- the shared preflight runner at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/run_tas_harness.py`
- the shared manual-assist launcher at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/run_tas_manual_assist.py`
- the shared manual-assist completion tool at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/complete_tas_manual_assist.py`
- a generated preflight artifact at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/analysis/validation/zelda3-fresh-file-boot-preflight.json`
- a generated manual-assist artifact at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/analysis/validation/zelda3-fresh-file-boot-manual-assist.json`
- a second world-state preflight artifact at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/analysis/validation/zelda3-basic-world-state-preflight.json`
- a second world-state manual-assist artifact at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/analysis/validation/zelda3-basic-world-state-manual-assist.json`

Current host reality on this Mac:

- preferred host remains `SNI`
- practical current host remains `Snes9x`
- so this first Zelda slice is manual-assist, not true automation

## What to do next

1. run and complete the first Zelda manual-assist result
2. run and complete the world-state manual-assist result
3. add one richer state-oriented Zelda slice after that
   - early room entry
   - stronger room-flag observation
4. replace manual assist with better RAM-observation or interface automation when a worthwhile host exists locally

## Practical recommendation

Do not overbuild this.

The first finished Zelda harness should be:

- one base ROM
- one fresh-file boot check
- one JSON result

That is enough to make the Zelda lane safer for later patch work.
