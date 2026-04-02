# Metroid TAS Harness Note 01

This note captures the first concrete TAS-harness lane for Super Metroid.

## Source lane ingested

- `../../repos/PJBoy-lua`
  - local path: `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/PJBoy-lua`
  - current local commit: `466d417`

Most relevant files in that repo for this lane:

- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/PJBoy-lua/Super Metroid.lua`
- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/PJBoy-lua/Super Hitbox.lua`
- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/PJBoy-lua/Super Hitbox + TAS.lua`
- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/PJBoy-lua/Super Camhack.lua`
- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/PJBoy-lua/cross emu.lua`

Complementary instrumentation asset:

- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/sm_practice_hack`
- classification note:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/lanes/metroid/practice-hack-01.md`

## Why this is the first real harness lane

This repo already gives us:

- emulator abstraction through `cross emu.lua`
- direct WRAM readers for room, door, game-state, Samus position, and many other fields
- a TAS-oriented overlay layer
- support for `BizHawk`, `lsnes`, and older rerecording emulator workflows

That makes it the strongest immediate way to stop relying only on manual launch-and-look verification.

## First scenario choice

The first concrete scenario for this lane is:

- `super-metroid-known-door-transition`

Its job is not to prove an entire run works. Its job is to prove one short stable slice works:

- ROM boots
- Samus reaches controllable state
- one known room/door transition setup is available as the first smoke-test target

Current concrete candidate slice:

- source room:
  - `Landing Site`
  - room pointer `0x91F8`
- destination room:
  - `Parlor and Alcatraz`
  - room pointer `0x92FD`

This is intentionally an early-game Crateria slice because it should be easier to reproduce and less fragile than something later in the route.

## Current implementation status

This workspace now has:

- a machine-readable scenario manifest at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/harness/scenarios/super-metroid-known-door-transition.json`
- a generic harness preflight runner at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/run_tas_harness.py`
- a manual-assist launcher for the current macOS host reality at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/run_tas_manual_assist.py`
- a generated preflight artifact at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/analysis/validation/super-metroid-known-door-transition-preflight.json`
- a generated manual-assist artifact at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/analysis/validation/super-metroid-known-door-transition-manual-assist.json`

Right now the runner does preflight validation only:

- verifies the ROM exists
- verifies the referenced Lua harness files exist
- records the ROM hash
- records the intended host and assertion set
- resolves which host is actually available on this Mac

That is deliberately small. It gives us a real scenario object and result artifact now, without pretending we already have BizHawk automation wired on this Mac.

Current host reality on this Mac:

- preferred automation host remains `BizHawk`
- but the official current BizHawk project does not provide a real Apple Silicon macOS lane
- `lsnes` is not currently installed and is not available as a simple Homebrew formula here
- so the runner now records a host-resolution result and can fall back to `Snes9x` as a manual-assist lane

## What to do next

The next implementation step is:

1. bind the first real assertions
   - `game_state`
   - `room_pointer`
   - `door_transition_function`
   - Samus control-ready state
   - source room pointer `0x91F8`
   - destination room pointer `0x92FD`
2. replace manual assist with true host automation once a TAS-capable host is available
3. emit pass/fail results into the same `analysis/validation/` path family

## Practical recommendation

Do not overbuild this.

The first finished Metroid harness should be:

- one host
- one scenario
- 3 to 5 assertions
- one JSON result

That is enough to become genuinely useful for hack smoke testing.
