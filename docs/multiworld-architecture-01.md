# Multiworld Architecture 01

This note captures the first shared workspace pass on Archipelago-style multiworld synchronization.

It is based on:

- the workspace’s current crossover and progression-grammar notes
- secondary-source intake from `docs/external-research/gemini-multiworld-archipelago-001.md`

The goal is not to turn Archipelago into a new primary project immediately.
The goal is to decide what parts of its architecture are genuinely relevant to this workspace.

## Core relevance

The strongest reason multiworld matters here is not multiplayer novelty.

It is this:

- multiworld systems force progression to become a formal cross-game protocol

That is highly relevant to a workspace already interested in:

- randomizer logic
- crossover progression
- shared item/location abstractions
- multi-game ROM or state architectures

## Most useful architectural ideas

### 1. Unified item/location abstraction

A multiworld system needs to express many different games in a shared language of:

- locations
- items
- access rules
- progression dependencies

That is directly relevant to this workspace because we already treat:

- Zelda randomizers
- Metroid randomizers
- `SMZ3`
- broader crossover ideas

as progression-graph problems.

### 2. Cross-game dependency modeling

Multiworld makes one important idea explicit:

- an unlock in game A can satisfy a requirement in game B

That is the same family of problem that makes `SMZ3` and `multirando-asm` interesting.

So even if we never build a networked system, Archipelago-style models are still useful as:

- crossover progression design references

### 3. External state bridge concept

The report highlights a useful architectural split:

- game/client state
- external coordination layer

Whether the implementation uses:

- SNI
- WebSockets
- emulator bridges

or something else, the design lesson is still relevant:

- cross-game synchronization does not have to live entirely inside one ROM

That matters for future ideas because some crossover designs may be cleaner as:

- external-state systems

rather than:

- single-image cartridge merges

## What seems most relevant to this workspace

The most reusable parts are:

- item/location ID abstraction
- cross-game progression-graph translation
- explicit synchronization/state-handshake thinking
- formal “received item” and “granted unlock” models

Those are design and systems ideas we can reuse even without adopting Archipelago itself.

## What is probably out of scope for now

These look interesting, but not worth making central yet:

- building a custom multiworld server
- emulator/client compatibility engineering as a primary project
- network-stack implementation details before we finish the core single-ROM crossover work

That means Archipelago should currently be treated as:

- architecture inspiration
- protocol/reference research
- not a near-term implementation target

## Relationship to current workspace lanes

### Shared SNES lane

Multiworld is relevant as:

- a formal model for item/location abstraction
- a way to reason about external synchronization

### SMZ3 lane

Multiworld is relevant as:

- a comparison point for cross-game progression logic
- a possible future alternative to “everything inside one ROM”

### Future crossover work

If we move beyond two-game and four-game crossover concepts, multiworld may become more attractive because it can avoid some of the cartridge-layout constraints that composite ROMs introduce.

## Best next tasks

1. Verify the exact relevance of `ArchipelagoMW/Archipelago` to the SNES games already in this workspace.
2. Verify `SNI` as the actual bridge layer that matters for SNES-side experimentation.
3. Add one short comparison note later:
   - single composite ROM crossover
   - external multiworld synchronization
4. Decide whether multiworld belongs as:
   - a shared architecture topic
   - a crossover-lane subtopic
   - or only a future-ideas reference
