# Gemini Research Intake 001

This note distills the first Gemini deep-research brief into:

- high-confidence additions worth keeping
- claims that still need verification
- concrete follow-up tasks for this workspace

Source brief:

- `docs/external-research/gemini-deep-research-001.md`

## High-confidence keep

These points fit the current workspace model and are worth retaining immediately.

### General SNES workflow

- `Asar` remains the default assembler reference for modern SNES patch workflows.
- `BPS` and `Flips` are worth keeping beside IPS because they are safer for modern patch distribution.
- `LoROM`, `HiROM`, and `FastROM` should stay first-class concepts in the graph and docs.

### Zelda 3

- Zelda randomizer logic is correctly framed as graph-based reachability and item-state reasoning.
- Entrance and door randomizers are correctly understood as pointer/topology rewrites, not just item shuffles.
- The Zelda lane still benefits from deeper RAM/SRAM/state docs and from a stronger vanilla progression note.

### Super Metroid

- PLMs and room/state headers are central reverse-engineering surfaces.
- The community’s logic terminology remains tightly tied to movement, topology, and reachability.
- Metroid Construction is still a core external knowledge source for the Metroid lane.

### SMW

- The report correctly reinforces the editor-centric nature of SMW hacking.
- `callisto` is correctly treated as a build-system/orchestration layer rather than a disassembly or editor.
- A reproducible SMW workflow should eventually connect clean ROM, source/disassembly, editor outputs, and patch tooling.

### Cross-game design

- The brief’s three-part framing is compatible with the workspace:
  - Zelda 3: adventure / logic / state
  - Super Metroid: movement / topology / reachability
  - SMW: editor-centric authored platforming

## Claims to verify before treating as canonical

The Gemini report is useful, but several specific references should be verified against primary sources before we absorb them into canonical docs or the graph.

### Tooling and debugger references

- `bsnes-plus` and `Mesen-S` as the current "gold standards" for SNES debugging
- exact role and current relevance of `ZScream`

### Zelda references

- `MathOnNapkins` as the best historical disassembly reference
- `JaredBrian` Asar-compatible disassembly lineage
- the exact identity and current usefulness of the "Zelda 3 Compendium"
- `alttp.run` as the definitive RAM/SRAM map source

### Super Metroid references

- `P.JBoy` disassembly as the standard relocatable reference
- exact repo identity and current activity of `sm_disassembly`
- `Kejardon` documents as a still-foundational source

### SMW references

- exact repo identity and current recommendation status of `smw-project-template`
- whether the proposed build flow ordering is still the best current representation of mature SMW projects

### Video and channel references

- `Displaced Gamers` specific relevant episodes
- `Danofmosttrades` Lunar Magic series as the right starter video lane
- which TASBot / live-hardware exploit talks are most relevant to this workspace versus merely interesting

## Concrete tasks extracted from the brief

These are the most useful follow-ups that came out of the report.

### Add to shared SNES research

- verify and, if valid, ingest the strongest debugger/video/community references named in the report
- evaluate `Archipelago` / multiworld protocol as a future crossover-research lane
- build a short note on BPS versus IPS versus Asar in practical workflow terms

### Add to Zelda lane

- deepen the vanilla progression note around game states, key logic, and world-state flags
- compare JP and US Zelda 3 source/disassembly expectations where that impacts hacking workflows

### Add to Metroid lane

- document the PLM execution model more explicitly
- inspect existing `sm-json-data` logic definitions already present in local repos before adding outside copies

### Add to SMW lane

- verify whether a modern `smw-project-template` belongs in the lane
- turn the staged SMW ROM plus `SMWDisX` into the first real vanilla deep-dive note
- eventually connect the editor/tool/build-system layers into one concrete SMW workflow note

## Immediate workspace interpretation

The Gemini brief did not fundamentally change the workspace direction.

What it did do:

- confirm the major lane structure is sound
- add a few promising external references
- suggest a few higher-level future research tracks:
  - debugger/tool verification
  - multiworld protocol research
  - SMW project-template/build-pipeline study

That means this brief is best treated as:

- a useful secondary-source intake
- not yet a canonical source on its own
