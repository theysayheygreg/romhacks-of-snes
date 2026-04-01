# TAS Harness Sketches 01

This note turns the TAS research pass into concrete harness sketches for the three anchor games.

These are not full implementations yet. They are workspace-ready starting points that define:

- the preferred emulator lane
- the first useful smoke tests
- what should be asserted
- what kind of artifact should be produced

The goal is to stop relying only on "open emulator and look at it" as soon as possible.

## Shared model

Each game gets the same three harness shapes:

1. `movie_replay`
2. `ram_assert`
3. `level_or_room_smoke`

The first practical implementation does not need all three for every game. It just needs one deterministic test that is worth keeping.

Machine-readable manifests live in:

- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/data/tas-harnesses/smw.json`
- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/data/tas-harnesses/super-metroid.json`
- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/data/tas-harnesses/zelda3.json`

## Super Mario World

Best first harness:

- `movie_replay`

Reason:

- SMW has a simple early-game boot flow.
- We already have a working patched ROM and a known visible state.
- A short deterministic sequence is enough to detect a surprising amount of breakage.

First useful smoke tests:

- `boot_to_yoshis_house`
  - boot ROM
  - enter a fresh save
  - start 1-player game
  - confirm the overworld loads and Mario can enter Yoshi's House
- `starting_lives_patch_check`
  - boot the `smw-starting-lives-09.sfc` artifact
  - verify the displayed life count matches the expected patch behavior

Best first assertion style:

- RAM assertion if the exact lives address is easy to poll
- otherwise screenshot/manual-visible state at first, then RAM later

Best first host candidate:

- `BizHawk`

Why:

- It is more likely than `snes9x` release builds to support the kind of scripting and replay control we want for automation.

## Super Metroid

Best first harness:

- `level_or_room_smoke`

Reason:

- Super Metroid already has the richest script ecosystem.
- Room loading, door transitions, and player state are exactly the kinds of things hacks break.

First useful smoke tests:

- `crateria_spawn_boot`
  - boot ROM
  - confirm Samus spawns into a stable playable state
- `known_door_transition`
  - execute a short deterministic movement sequence through one stable room transition
  - confirm the next room loads and control continues
- `item_or_plm_probe`
  - enter a known item room
  - verify the PLM/item object is present and interactable

Best first assertion style:

- RAM assertion plus script-visible room/door state

Best first host candidate:

- `BizHawk` for scripting convenience
- keep `lsnes` as the likely long-term deterministic replay lane

Why:

- `PJBoy/lua` gives us the strongest immediate leverage here.

## Zelda 3 / ALTTP

Best first harness:

- `ram_assert`

Reason:

- ALTTP's strongest immediate automation lane is state/interface-oriented, not obviously a mature public TAS-script stack like Super Metroid.
- We can still get real value by checking deterministic state transitions.

First useful smoke tests:

- `fresh_file_boot`
  - boot ROM
  - verify new game path reaches stable controllable state
- `basic_world_state_check`
  - confirm a handful of key WRAM/SRAM flags are sane on a fresh file
- `safe_room_entry`
  - verify entering one known early room does not hang or corrupt state

Best first assertion style:

- RAM/state assertions first
- movie replay later if we adopt a stronger ALTTP emulator-script lane

Best first host candidate:

- `SNI` plus compatible emulator/device interfaces for state observation
- `BizHawk` only if we later find a worthwhile ALTTP Lua/TAS stack to standardize on

## Recommended implementation order

1. Super Metroid room/door smoke test
2. SMW boot-to-overworld smoke test
3. ALTTP fresh-file RAM/state smoke test

That order gets us the most leverage fastest.

## Output shape

Every harness should eventually produce:

- a small manifest entry describing the test
- a launcher or runner script
- one result file under `analysis/validation/`
- a pass/fail summary that does not require opening the emulator manually

The harness does not need to be fully autonomous on day one. A hybrid script-plus-emulator workflow is acceptable if it gives us deterministic checkpoints and a clean result artifact.
