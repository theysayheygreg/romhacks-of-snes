# SMW Standalone ROM 02

This is the first visible gameplay patch in the SMW lane.

Base ROM:

- `../../roms/base/Super Mario World (USA).sfc`

Patch input:

- `../../patches/smw/smw-starting-lives-09.asm`

Helper script:

- `../../tools/apply_smw_starting_lives_09.sh`

Output ROM:

- `../../build/smw-starting-lives-09.sfc`

Probe artifact:

- `../../analysis/smw-starting-lives-09-rom.json`

## Scope

This patch changes the vanilla new-save initialization path from 4 starting lives to 9.

For the U ROM matched by this workspace, the immediate value lives at:

- `LoadSaveAndFadeToOW`
- `SMW_U.sym` address `00009E17`
- patched instruction at `00:9E26`

It also changes the internal ROM title so the output image is easy to identify in tooling.

## Why this patch

This is still a low-risk patch, but unlike the header-only test it changes visible gameplay state.

That makes it a better checkpoint for the SMW lane because it proves:

- ROM patching works
- the patched ROM can be distinguished from the base image
- we can alter real gameplay behavior without touching level data or editor workflows yet
