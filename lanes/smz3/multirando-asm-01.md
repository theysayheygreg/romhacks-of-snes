# multirando-asm 01

This note classifies `multirando-asm` inside the crossover lane.

## Local repo

Local path:

- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/multirando-asm`

## What it is

From the repo README:

- "ASM code repo for the Super Metroid, A Link to the Past, Zelda 1 and Metroid 1 randomizer."

That makes it materially different from `SMZ3`.

`SMZ3` is the current two-game anchor in this workspace.
`multirando-asm` broadens the idea into:

- four games
- one SNES ROM
- mixed SNES-native and NES-origin game substrates

## Why it matters

This is one of the most important crossover examples we have so far because it pushes past:

- merged progression across two SNES games

into:

- multi-game architecture across four games
- SNES-hosted adaptation of NES-origin games
- larger cartridge/banking and runtime switching concerns

So it is not just "another randomizer repo."
It is a crossover-architecture repo.

## High-value repo signals

The repo structure already tells us a lot.

### Game-specific source areas

There are distinct source areas for:

- `src/m3/`
- `src/z3/`
- `src/z1/`
- `src/m1/`

The naming strongly suggests:

- `m3` = Super Metroid
- `z3` = A Link to the Past
- `z1` = Zelda 1
- `m1` = Metroid 1

### NES-on-SNES adaptation work

The repo is not merely bundling NES games.
It contains explicit SNES port/adaptation work for the NES-origin games.

Examples surfaced from the local source:

- `src/m1/init.asm`
- `src/m1/snes.asm`
- `src/m1/hooks.asm`

These contain comments about:

- custom boot routines for Metroid 1 on SNES
- converting NES OAM/PPU behavior to SNES-side behavior
- simulating NES banking using SNES banks

That means this repo is also relevant as:

- an example of cross-platform adaptation inside a single cartridge/runtime concept

### Explicit crossover architecture notes

The repo’s `ideas.md` is especially valuable.

It describes:

- SA-1-driven banking ideas
- ROM slot allocation across multiple games
- SRAM/BW-RAM handling across game contexts
- a possible shared helper/"Mother Brain" supervisory layer
- multiworld functionality as an explicit design target

That is exactly the kind of architecture thinking we want in this workspace.

## Relationship to SMZ3

`multirando-asm` appears best understood as:

- adjacent to `SMZ3`
- building on similar crossover instincts
- broader in scope
- more architecture-heavy

The local repo even references:

- "Added a subset of patches from SMZ3"

So the clean mental model is:

- `SMZ3` = two-game crossover anchor
- `multirando-asm` = four-game crossover / mixed-runtime architecture lead

## Best reasons to keep it in the workspace

It gives us a second major crossover example for:

- multi-game item/reward translation
- runtime switching between very different game substrates
- SA-1/banking strategy for large composite ROMs
- shared SRAM and state management
- crossover build architecture beyond a simple two-game merger

## Best next tasks

1. Compare `multirando-asm`'s banking model against the current `SMZ3` ROM-layout understanding.
2. Extract the repo’s implied runtime-switching model:
   - what changes when entering SM vs ALTTP vs Z1 vs M1
3. Decide whether the crossover lane should explicitly track:
   - two-game crossovers
   - multi-game crossovers
   - multiworld protocols
4. Determine whether Zelda 1 and Metroid 1 need lightweight reference nodes in the SNES knowledge graph as crossover guest games.
