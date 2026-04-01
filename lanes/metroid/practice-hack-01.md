# Metroid Practice Hack Note 01

This note classifies `sm_practice_hack` inside the Metroid lane.

## Repo

- local path:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/sm_practice_hack`
- local commit:
  - `db2244e`

## What it is

`sm_practice_hack` is best treated as a testing and instrumentation asset, not just a player convenience tool.

The README is explicit about that:

- it is intended for contributors and people adapting it for Super Metroid romhacks
- it supports multiple patch outputs for different runtime targets
- one of its major purposes is controlled practice/debug visibility through InfoHUD and related features

## Why it matters to this workspace

For the SNES workspace, this project is useful because it already embodies a lot of what we want from a lightweight harness-support layer:

- controlled debugging surfaces
- runtime state visibility
- patchable instrumentation for hacked ROMs
- a known path toward FX Pak / SD2SNES-compatible use

That makes it adjacent to TAS tooling in a productive way:

- `PJBoy-lua` gives us emulator-side script visibility
- `sm_practice_hack` gives us ROM-side instrumentation patterns

Together, those are a better testing stack than either alone.

## Practical role

Treat `sm_practice_hack` as:

- a testing/instrumentation repo
- a source of patterns for ROM-side observability
- a future enhancement lane for making hacked Metroid ROMs easier to verify

Do not treat it as the first harness host by itself.

The first harness host should still be an emulator/script lane.
The practice hack is better used as a complementary instrumentation layer once the first deterministic scenario is running.
