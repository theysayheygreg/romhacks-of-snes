# SMW Workflow Model 01

This note captures the first canonical workflow model for the SMW lane.

It is based on:

- local tooling notes for Lunar Magic and `callisto`
- local source/disassembly context from `SMWDisX`
- the staged local SMW U 1.00 base ROM
- secondary-source intake from `../../docs/external-research/gemini-smw-pipeline-verification-001.md`

The goal is to keep the structural model that is strongly compatible with the local workspace, while treating more opinionated ecosystem claims as follow-up validation tasks.

## Core model

The cleanest current model for SMW hacking in this workspace is:

- clean base ROM as compatibility anchor
- editor-driven spatial authoring
- source-first patch and tool orchestration
- generated ROM as build output, not primary source of truth

That is the main distinction between the mature SMW ecosystem and many older ROMhacking workflows.

## The main layers

### 1. Base ROM layer

Current workspace anchor:

- `../../roms/base/Super Mario World (USA).sfc`
- `../../analysis/super-mario-world-usa-rom.json`

Current practical interpretation:

- SMW U 1.00 is the default working base for this workspace unless a repo or tool proves otherwise

This is already supported by:

- the staged ROM facts
- Lunar Magic’s documented support
- the broader direction of the external verification brief

### 2. Editor-driven spatial layer

Current local anchor:

- `./lunar-magic-01.md`

Lunar Magic remains the clearest representation of the editor-driven side of SMW work:

- level editing
- overworld editing
- graphics and palette editing
- text editing
- external level import/export
- targeted ASM-assisted engine extension

This layer is still the practical home of:

- spatial content
- obstacle layout
- world-map layout
- many of the authored-feel decisions

### 3. Source/disassembly reference layer

Current local anchor:

- `../../repos/SMWDisX`

`SMWDisX` is best treated as:

- source/reference lane
- banked code and memory-map understanding lane
- engine-level modification reference

The local workspace should not assume that every normal SMW project uses `SMWDisX` as its literal build base.

Instead, the safer current interpretation is:

- `SMWDisX` is a powerful source/reference substrate
- mature day-to-day hacking workflows may still center on a clean ROM plus tools rather than on building directly from a disassembly

### 4. Build-system/orchestration layer

Current local anchor:

- `./callisto-01.md`

`callisto` is the strongest local example of a source-first orchestration workflow:

- clean ROM as input
- patches and modules as tracked sources
- exports and resources managed outside the ROM
- generated ROM as final output

This means the SMW lane is already best understood as a four-part system:

- clean ROM
- editor outputs
- source patches/modules/resources
- orchestration into a generated ROM

## Practical tool-role model

The current best workspace model is:

- `Lunar Magic`
  - editor-driven spatial authoring
- `SMWDisX`
  - source/reference and engine-understanding lane
- `callisto`
  - orchestration/build lane
- `Asar`
  - assembly patch application lane
- other inserters such as `PIXI`, `GPS`, `AddmusicK`, `UberASM`
  - probable ecosystem-standard specialized resource insertion lanes

Important caveat:

- the exact recommended modern versions and ordering of those inserter tools still need primary-source verification for this workspace

So those should currently be treated as:

- highly plausible workflow components
- not yet a fully verified local standard

## What this means for source of truth

The most important design/workflow shift is:

- the ROM is no longer the only meaningful project artifact

A mature SMW project likely wants these outside the ROM:

- patches
- modules
- configuration
- level exports
- graphics/resources
- build metadata

That is why `callisto` matters so much conceptually.
It turns ROM hacking into something closer to:

- a reproducible build pipeline

than:

- manual binary mutation

## Where the local workspace stands

The SMW lane now has enough structure to support this workflow model conceptually:

- base ROM is staged and fingerprinted
- Lunar Magic is documented as the editor lane
- `SMWDisX` is documented as the source/reference lane
- `callisto` is documented as the build/orchestration lane

What is still missing is a concrete end-to-end local example.

That means the next high-value step is not more abstraction.
It is one real SMW workflow pass, even if small.

## What still needs verification

These claims from the external brief are useful but should remain provisional until we confirm them ourselves:

- `smw-project-template` as the best current starter template
- the exact modern tool stack ordering
- the exact degree to which `SMWDisX` is used as an active base versus a reference lane
- whether SA-1-first is a sensible default assumption for this workspace
- exact tool version expectations

## Best next tasks

1. Ingest and evaluate `smw-project-template` if it holds up.
2. Produce the first vanilla SMW deep-dive note from the staged U 1.00 base ROM plus `SMWDisX`.
3. Write one concrete “minimal SMW build pipeline” note for this workspace:
   - base ROM
   - editor/tool roles
   - expected outputs
4. Decide whether the first SMW artifact should be:
   - a tiny editor-like content change
   - a tiny Asar patch
   - or a template/project-structure reproduction experiment
