# SMW Project Template 01

This note classifies `Underrout/smw-project-template` inside the SMW lane.

Local repo:

- `../../repos/smw-project-template`

Observed local commit:

- `6ab7d7d`

## Why it matters

This repo is the clearest current example in the workspace of an SMW project being treated as:

- a tracked source tree
- a tool-orchestrated build
- a generated ROM output

not just:

- a manually edited binary

## What it contains

From the local README and TOML config:

- `callisto` as the primary orchestration layer
- `Lunar Magic`
- `FLIPS`
- `AddmusicK`
- `GPS`
- `PIXI`
- `UberASMTool`

The default project output is:

- `build/{project_name}.smc`

The default initial patch is:

- `resources/initial_patch_sa1.bps`

with an explicit FastROM alternative noted in `callisto/resources.toml`.

## What it confirms for this workspace

This repo strongly confirms the model already emerging in the SMW lane:

- clean base ROM as compatibility anchor
- editor-driven asset and level authoring
- tracked resources and patches outside the ROM
- orchestration layer that rebuilds the ROM from scratch

It also strengthens two earlier conclusions:

- modern SMW work is often pipeline-oriented
- SA-1 is a common default in modern starter workflows, even if not universal

## Relationship to the existing SMW lane

Best classification:

- `SMWDisX`
  - source/reference lane
- Lunar Magic
  - editor lane
- `callisto`
  - orchestration/build-system lane
- `smw-project-template`
  - template/starter-project lane built around the orchestration model

So `smw-project-template` does not replace `SMWDisX`.
It sits above it in the stack as a practical project skeleton.

## Important caveat

The local template is still strongly Windows-shaped:

- setup instructions center on `callisto.exe`
- Lunar Magic integration is part of the expected happy path

So for this Mac-based workspace, the repo is currently:

- a validated reference lane
- not yet a fully verified local execution lane

That distinction matters.
It is useful now as a workflow model and file-layout reference, even before we make it run end to end on macOS.

## Current verdict

`smw-project-template` belongs in the SMW lane.

Recommended role:

- first modern template/starter lane

Confidence level:

- medium-high for architecture and workflow classification
- low for local macOS execution until we deliberately test or adapt it

## Next steps

1. Keep using this repo as the file-layout and build-pipeline reference lane.
2. Compare its project shape directly against our current `snes/` lane layout.
3. Later, decide whether to:
   - adapt the template for a Mac-friendly helper lane
   - or keep it as a reference while using narrower local scripts for standalone ROM generation
