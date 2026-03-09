# SNES Workspace Roadmap

This roadmap turns the backlog into a sequence that gets us to useful outcomes quickly:

- a repeatable local toolchain
- one deeply understood anchor game
- a reusable knowledge base for future hacks

## Working assumptions

- Real hardware via `sd2snes` is the final runtime oracle.
- `bsnes` and `snes9x` are primarily research and debugging references, not the sole definition of success.
- `bsnes` is the preferred accuracy reference.
- `snes9x` is useful as a long-lived compatibility reference and for understanding practical emulator behavior.
- Windows compatibility is not a goal by itself. We should only introduce a Windows-assisted lane if a specific reverse-engineering capability justifies it.
- The workspace needs to support both:
  - patch-first workflows over canonical base ROMs
  - reconstruction-heavy, assembly-first workflows like the SMW/Lunar Magic ecosystem

## Phase 1: Make the workspace operational

Goal:

- produce a working local lane from source material to runnable ROM output, with final validation on real hardware

Why this goes first:

- without a verified build and validation lane, the rest of the research stays theoretical
- it also tells us which parts of the current stack are Mac-native and which should be treated as Windows-assisted

Tasks:

- install and verify `dotnet`
- install and verify `cmake`
- install and verify `asar`
- pick one primary emulator target for daily work
- define the emulator role split:
  - `bsnes` as accuracy/reference
  - `snes9x` as compatibility/reference
- document one end-to-end ROM build/test path
- verify whether `SMZ3` can generate a final ROM locally on macOS
- produce one standalone Zelda ROM artifact for later cartridge testing
- produce one standalone Super Metroid ROM artifact for later cartridge testing
- keep `sd2snes` as deployment context, but not as a blocking firmware research thread

Current status:

- `bsnes` source build is verified on macOS arm64.
- `SMZ3` CLI builds under the `.NET 9` SDK and runs here with `DOTNET_ROLL_FORWARD=Major`.
- `MapRandomizer` compiles through `cargo check` on macOS once submodules are initialized.
- `z3randomizer` provides the current simplest documented patch-first ROM lane.
- Real cartridge loading is intentionally deferred until we have stronger standalone Zelda and Metroid ROM artifacts.

Exit criteria:

- one documented command path that produces a ROM or patch artifact locally
- one standalone Zelda ROM artifact ready for future cartridge testing
- one standalone Super Metroid ROM artifact ready for future cartridge testing
- one note that clearly separates:
  - Mac-native tooling
  - optional Windows-assisted tooling
  - deployment-on-hardware context

Dependencies:

- none

Priority:

- `P0`

## Phase 2: Establish the first anchor game

Goal:

- build a serious technical profile of Super Metroid

Why Super Metroid first:

- strong existing reverse-engineering ecosystem
- already one of the two reference ROMs in the workspace
- directly relevant to `SMZ3`
- dense enough to teach us a lot about rooms, state, item logic, and engine patching

Tasks:

- map major banks and code/data regions
- identify reset vectors, startup flow, and dispatch patterns
- document room structure and room-state variation
- document save RAM usage and progression state
- identify compression/decompression touchpoints
- identify 3-5 low-risk first patch targets
- relate Super Metroid randomizer lineage (`RandomMetroidSolver`, `MapRandomizer`) to the base-game analysis

Exit criteria:

- one document that explains where the major systems live
- one short list of patchable targets with likely addresses/banks or search strategies
- enough confidence to try a first small code or data mod
- one note explaining how Super Metroid randomizer logic and solver terminology maps onto the base game

Dependencies:

- benefits from Phase 1 but can partially proceed in parallel

Priority:

- `P0`

## Phase 2b: Establish the Zelda 3 source lane

Goal:

- connect the existing Zelda JP example ROM to a concrete, banked source disassembly

Why this now matters more:

- `jpdasm` gives us a revision-matched ALTTP JP1.0 source base
- that sharply reduces ambiguity when we start mapping Zelda systems or comparing against `SMZ3`

Tasks:

- verify the example ROM against `jpdasm`'s stated checksums/revision
- map the repository structure and major bank files
- identify symbol files for WRAM/SRAM/APU work
- document the asset-extraction and reassembly path
- map how the patch/randomizer lineage (`z3randomizer`, `alttp_vt_randomizer`, `ALttPDoorRandomizer`) sits beside the disassembly lane

Exit criteria:

- one note that explains how to use `jpdasm` as the Zelda reference source
- one verified statement on whether our local Zelda ROM matches the expected target revision closely enough for direct use
- one note describing the split between Zelda disassembly, low-level patch code, and randomizer application logic

Dependencies:

- benefits from Phase 1

Priority:

- `P1`

## Phase 3: Turn notes into a reusable framework

Goal:

- make the knowledge base scale beyond one game

Why this matters:

- otherwise every new game becomes a fresh research sprint with no structure

Tasks:

- expand the knowledge graph from hand-curated nodes to source-linked nodes
- add subsystem/file references for emulators, tools, ROMs, and hardware paths
- add curated external research resources and community hubs into the graph
- distill external assistant research briefs from `docs/external-research/` into canonical workspace docs and graph updates
- define a per-game intake template
- define a patch validation template
- define a hardware deployment checklist for `sd2snes`

Exit criteria:

- one consistent schema for adding a new game
- graph entries linked to local files and generated analysis artifacts
- future game intake reduced to a repeatable checklist

Dependencies:

- informed by Phases 1 and 2

Priority:

- `P1`

## Phase 4: Validate the crossover pipeline

Goal:

- use `SMZ3` as the first proof that we can understand and reproduce a sophisticated SNES ROM build workflow

Why this matters:

- it is close to the kind of future work you want: merged games, custom mechanics, nontrivial patch generation

Tasks:

- verify exact base ROM expectations
- verify required IPS and other resource inputs
- generate at least one final ROM locally
- map where crossover mechanics are emitted in patch data
- document how the combined ROM layout is constructed
- verify that the final ROM is acceptable to the real-hardware path, not just emulators

Exit criteria:

- one reproducible `SMZ3` build recipe in this workspace
- one document describing where its major binary transformations happen

Dependencies:

- strongly depends on Phase 1
- benefits from Phase 2

Priority:

- `P1`

## Phase 5: Broaden the ecosystem view

Goal:

- stand up the SMW lane enough to study mature editor-driven hacking practices without losing the shared SNES structure

Tasks:

- activate the SMW swim lane with its own backlog and intake checklist
- identify the first base SMW ROM and fingerprint it
- classify `SMWDisX` as the first source/reference lane and decide which revision to anchor on
- ingest the first wave of SMW-specific repos and tools
- extract low-level reference material from `SMW Central`
- document how Lunar Magic-style tooling combines format knowledge with targeted ASM patches
- compare those patterns to Super Metroid and Zelda workflows
- build a comparative design note across Zelda, Metroid, and SMW that is explicit about progression grammar and modifiable levers
- turn the staged SMW base ROM into a first deep-dive and compatibility anchor for `SMWDisX`, Lunar Magic, and `callisto`

Exit criteria:

- one doc connecting community workflow patterns to this workspace's tooling strategy
- enough material to decide whether we should build editor-like helpers later

Dependencies:

- none, but still lower leverage than the earlier phases right now

Priority:

- `P2`

## Suggested order

1. Phase 1
2. Phase 2
3. Phase 2b
4. Phase 4
5. Phase 3
6. Phase 5

Rationale:

- `Phase 1` gets us out of pure research mode.
- `Phase 1` also makes sure we are validating against the real target machine instead of treating emulators as the end goal.
- `Phase 2` gives us deep understanding in one real target.
- `Phase 2b` gives Zelda 3 a source-grounded lane instead of leaving it as only a ROM artifact.
- `Phase 4` converts that into a nontrivial applied build workflow.
- `Phase 3` then turns what we learned into durable process.
- `Phase 5` broadens the ecosystem once the core lane is already working.

## Open decisions

- Which reverse-engineering features actually justify a Windows helper lane for Diz/snestistics?
- Should the first actual mod target be Super Metroid alone, or should we push directly toward an `SMZ3`-style reproduction lane?
