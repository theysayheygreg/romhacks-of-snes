# SMW Standalone ROM 01

This is the first standalone SMW ROM artifact produced directly inside the workspace.

Base ROM:

- `../../roms/base/Super Mario World (USA).sfc`

Patch input:

- `../../patches/smw/smw-workspace-header-test.asm`

Helper script:

- `../../tools/apply_smw_workspace_header_test.sh`

Output ROM:

- `../../build/smw-workspace-test-20260309.sfc`

Probe artifact:

- `../../analysis/smw-workspace-test-20260309-rom.json`

## Scope

This is intentionally a low-risk pipeline-validation patch.

It changes:

- the internal ROM title at `00:FFC0`

It does not yet change gameplay.

That is deliberate.
The goal of this first artifact is to prove:

- base ROM copy
- local patch application
- checksum repair
- generated output inspection

all work cleanly in the SMW lane.

## Result

The generated ROM is a distinct output image derived from the staged local base ROM.

Observed properties from the local probe:

- still `LoROM`
- still `SlowROM`
- same ROM size as the base image
- different hash from the base ROM
- internal ROM title now reads `SMW WORKSPACE TEST`

Current verification level:

- patch application verified locally
- probe output generated locally
- emulator test not yet run in this pass
- hardware test not yet run

## Why this artifact matters

The workspace now has a real SMW output path, even before standing up:

- a full Lunar Magic round-trip
- a full Callisto template build
- a more invasive gameplay patch

That is enough to support the next step, which is now captured in:

- `standalone-rom-02.md`
