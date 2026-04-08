# Super Metroid Standalone ROM 01

This is the first standalone Super Metroid ROM artifact in the workspace.

Base ROM:

- `../../roms/base/Super Metroid (Japan, USA) (En,Ja).sfc`

Patch input:

- `../../patches/metroid/sm-starting-energy-199.asm`

Helper script:

- `../../tools/apply_sm_starting_energy_199.sh`

Output ROM:

- `../../build/super-metroid-starting-energy-199.sfc`

Probe artifact:

- `../../analysis/super-metroid-starting-energy-199-rom.json`

## Scope

This patch changes vanilla new-file current and max health from `99` to `199`.

For the exact ROM matched by this workspace, the initialization instruction lives at:

- `81:B2CD`
- `LDA #$0063`

The patch changes that immediate to `#$00C7`, then lets the next two vanilla stores write the new max and current health values.

## Why this patch

This is a low-risk visible patch:

- it touches one immediate value in a clearly identified new-file init path
- it changes gameplay state in an obvious way
- it stays close to the first patch-target notes already documented in the Metroid lane

That makes it a better first standalone Metroid artifact than a header-only marker or a free-space-heavy startup rewrite.
