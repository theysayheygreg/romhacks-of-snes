# SMW TAS Harness Note 01

This note captures the first concrete TAS-harness lane for Super Mario World.

## Why this is the first SMW harness slice

The first practical SMW harness should not start with a long replay.

The workspace already has:

- a verified visible gameplay patch ROM at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/build/smw-starting-lives-09.sfc`
- a matching probe artifact at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/analysis/smw-starting-lives-09-rom.json`
- a working local `Snes9x` lane on this Mac

That makes the start-lives patch check a better first executable harness than a longer boot-to-Yoshi's-House flow.

## First scenario choice

The first concrete scenario for this lane is:

- `smw-starting-lives-09`

Its job is to prove one short visible gameplay slice works:

- the patched ROM boots
- a fresh save can start
- the overworld becomes controllable
- the displayed lives value is visibly `9`

This keeps the first SMW harness aligned with the already-verified visible patch rather than inventing a more ambitious replay lane too early.

## Current implementation status

This workspace now has:

- a machine-readable scenario manifest at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/harness/scenarios/smw-starting-lives-09.json`
- the shared preflight runner at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/run_tas_harness.py`
- the shared manual-assist launcher at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/run_tas_manual_assist.py`
- the shared manual-assist completion tool at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/tools/complete_tas_manual_assist.py`
- a generated preflight artifact at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/analysis/validation/smw-starting-lives-09-preflight.json`
- a generated manual-assist artifact at:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/analysis/validation/smw-starting-lives-09-manual-assist.json`

Current host reality on this Mac:

- preferred automation host remains `BizHawk`
- practical current host remains `Snes9x`
- so this first SMW slice is manual-assist, just like the current Metroid slice

## What to do next

1. run and complete the first manual-assist SMW result
2. add one richer SMW slice after this settles
   - boot to stable overworld
   - enter Yoshi's House
3. replace manual assist with better host automation when a worthwhile replay-capable host exists locally

## Practical recommendation

Do not overbuild this.

The first finished SMW harness should be:

- one patched ROM
- one short visible check
- one JSON result

That is enough to make the SMW lane safer for future ROM edits.
