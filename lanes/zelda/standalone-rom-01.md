# Zelda Standalone ROM 01

This is the first standalone Zelda ROM artifact in the workspace.

Base ROM:

- `../../roms/base/Zelda no Densetsu - Kamigami no Triforce (Japan).sfc`

Patch input:

- `../../repos/z3randomizer/LTTP_RND_GeneralBugfixes.asm`

Helper script:

- `../../tools/apply_z3_general_bugfixes.sh`

Output ROM:

- `../../build/zelda-general-bugfixes.sfc`

Probe artifact:

- `../../analysis/zelda-general-bugfixes-rom.json`

## Scope

This artifact promotes the already-verified general bugfix patch path into a stable workspace output with a durable name.

It is not a custom gameplay redesign yet. It is the first cartridge-test-intended Zelda patch-first artifact because it proves:

- the exact local JP base ROM can be patched reproducibly
- the resulting ROM remains checksum-valid
- the workspace has a stable Zelda output image worth carrying forward into later emulator and hardware checks

## Why this artifact

For Zelda, the lowest-risk useful artifact was already present in the randomizer ecosystem:

- a small established patch payload
- a proven local helper path
- a final ROM shape that the workspace can reproduce on demand

That makes it a better first milestone than inventing a custom ASM edit before the Zelda patch-target sheet is fully documented.
