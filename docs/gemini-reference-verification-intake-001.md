# Gemini Reference Verification Intake 001

This note distills the first Gemini reference-verification brief into workspace actions.

Source brief:

- `docs/external-research/gemini-reference-verification-001.md`

## Strong leads to promote

These are the most useful leads from the verification brief.

### Debugger / emulator lane

- `Mesen 2` is a strong candidate for the modern debugger-first reference lane.
- `bsnes-plus` appears worth tracking as a stable surgical-debugging tool even if it is no longer the newest path.

Workspace implication:

- the shared toolchain/docs should eventually compare:
  - `bsnes`
  - `bsnes-plus`
  - `Mesen 2`

### Zelda lane

- `JaredBrian/AsarUSALTTPDisassembly` is a strong lead for a modern Asar-compatible Zelda disassembly lane.
- `alttp.run` is a strong lead for accessible Zelda RAM/SRAM/state documentation.
- `yaze` is a strong lead as a modern ALTTP editor lane.

Workspace implication:

- `jpdasm` remains the exact-match canonical JP source lane we already rely on.
- the new question is not replacement, but whether these should be added as:
  - modern US / Asar-compatible source lane
  - modern editor/tooling lane
  - memory-doc reference lane

### Metroid lane

- `InsaneFirebat/sm_disassembly` is a strong lead for a modern relocatable / Asar-compatible Super Metroid disassembly lane.
- `Kejardon` docs remain a strong historical technical reference lead.

Workspace implication:

- `strager/supermetroid` remains our current exact-match source lane.
- the new question is whether `sm_disassembly` should be added as the “modern patch-authoring disassembly lane” alongside it.

### SMW lane

- `smw-project-template` is a strong lead for a modern Callisto-based template lane.

Workspace implication:

- this fits directly with the existing `callisto` classification work.
- if validated, it should become the first “project template / starter workflow” repo in the SMW lane.

## Keep historical, but separate from current-default recommendations

The report’s distinction between “historical but useful” and “recommended today” is worth preserving.

Examples:

- `MathOnNapkins`
- `P.JBoy`
- `Kejardon`
- Zelda 3 Compendium
- older onboarding video channels

These belong in the workspace, but should be labeled as:

- historical foundation
- terminology source
- archival reference

not necessarily:

- default active implementation lane

## Recommendations to treat cautiously

The report is useful, but I would still avoid treating these as final truth until we inspect primary sources ourselves:

- `Mesen 2` as the definitive debugger standard for this workspace
- `JaredBrian` as the primary active Zelda disassembly lane
- `sm_disassembly` as the primary active Super Metroid disassembly lane
- `smw-project-template` as the gold-standard SMW starting point
- `yaze` as the modern default ALTTP editor

The direction is plausible.
The exact recommendation level still needs a primary-source pass.

## Best concrete follow-up tasks

### Shared

- compare `bsnes`, `bsnes-plus`, and `Mesen 2` in one debugger/tooling note
- add a provisional “modern versus historical reference lanes” distinction to the resource index

### Zelda

- evaluate `JaredBrian/AsarUSALTTPDisassembly`
- evaluate `alttp.run`
- evaluate `yaze`

### Metroid

- evaluate `InsaneFirebat/sm_disassembly`
- evaluate whether it complements or supersedes `strager/supermetroid` for patch-authoring work

### SMW

- ingest and classify `smw-project-template` if it holds up
- compare it directly with `callisto`

## Workspace interpretation

This verification brief did improve the quality of the earlier Gemini pass.

Most useful upgrades:

- `Mesen-S` should no longer be treated as the likely current recommendation; `Mesen 2` is the stronger lead
- `ZScream` should not be treated as a default modern recommendation
- the workspace now has clearer “modern lead” candidates for:
  - Zelda
  - Metroid
  - SMW

But this is still an intake note.
The next step is direct validation against those repos and docs before we fully promote them into the canonical resource index and graph.
