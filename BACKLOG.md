# SNES Workspace Backlog

This is the durable task list for shared SNES workspace work.

Lane-specific work lives in:

- `lanes/zelda/BACKLOG.md`
- `lanes/metroid/BACKLOG.md`
- `lanes/smz3/BACKLOG.md`
- `lanes/smw/BACKLOG.md`

## Now

- [ ] Establish a real macOS build/run lane
  - [x] Install and verify `dotnet`, `cmake`, `asar`, `wget`, `rustup`, `php`, and `composer`.
  - [x] Verify one primary emulator build target with `bsnes`.
  - [x] Confirm that `SMZ3` builds locally and runs on this Mac with `DOTNET_ROLL_FORWARD=Major`.
  - [x] Confirm that `MapRandomizer` is Mac-viable once submodules are hydrated.
  - [x] Produce one end-to-end documented path from patch input to a runnable ROM with `z3randomizer`.
  - [ ] Produce one real standalone Zelda ROM artifact intended for eventual cartridge testing.
  - [ ] Produce one real standalone Super Metroid ROM artifact intended for eventual cartridge testing.
  - [ ] Decide whether to keep using runtime roll-forward for `SMZ3` or add a dedicated `.NET 7` runtime lane.

- [ ] Start filling the swim lanes with lane-specific artifacts
  - `lanes/zelda`: vanilla grammar, disassembly, and randomizer notes
  - `lanes/metroid`: vanilla grammar, solver logic, and patch targets
  - `lanes/smz3`: crossover graph, ROM layout, and shared-rule notes
  - `lanes/smw`: intake, ROM fingerprinting, `SMWDisX`, editor ecosystem, and low-level notes

- [ ] Map randomizer concepts explicitly across games
  - Seed generation
  - Logic / reachability rules
  - Spoiler logs and progression spheres
  - ROM emission and patch artifacts
  - Distinguish item randomizers from world-structure randomizers

- [ ] Expand the knowledge graph from curated notes into source-linked structure
  - Add file-level and subsystem-level nodes for emulators, tools, and hardware workflows.
  - Link example ROM facts to concrete source files and build steps.
  - Decide on a graph format that stays easy to diff and extend.

- [ ] Build a curated external research lane
  - Add foundational SNES hardware and patching resources to the knowledge graph.
  - Add Zelda / Metroid / SMW community guide links that are worth keeping long-term.
  - Keep a short distinction between source/disassembly, editor/tooling, randomizer, and design-analysis resources.

- [ ] Build deeper design notes for the three anchor games
  - Zelda 3 as item/state progression grammar
  - Super Metroid as movement/topology progression grammar
  - SMW as authored challenge and exit-graph grammar
  - Pull out specific design levers that are reusable for future projects

- [ ] Run a second-pass research sweep with Gemini
  - Use the workspace prompt in `docs/gemini-deep-research-prompt.md`.
  - Focus on YouTube videos, talks, archived threads, and long-form community posts.
  - Distill the results back into durable notes rather than keeping them as a raw dump.
  - [x] Distill the first Gemini brief into `docs/gemini-research-intake-001.md`.
  - [x] Distill the first Gemini reference-verification brief into `docs/gemini-reference-verification-intake-001.md`.

## Next

- [ ] Define a standard per-game intake template
  - Required artifacts
  - ROM fingerprinting
  - Mapper/header facts
  - Initial questions for gameplay and engine analysis

- [ ] Add a patching workflow note
  - IPS/BPS/asar roles
  - Base ROM handling
  - Validation steps in emulator and on `sd2snes`
  - Distinguish patch-first randomizer workflows from full source-reconstruction workflows

- [ ] Build a base-ROM and tool compatibility matrix
  - Which ROM revisions each tool or editor expects
  - Which tools are exact-match source lanes versus multi-version lanes
  - Which workflows are Mac-native, Windows-assisted, or emulator-specific

- [ ] Verify Gemini-surfaced external references before promoting them to canonical docs
  - debugger lanes like `bsnes-plus` and `Mesen-S`
  - historical Zelda and Metroid disassembly references
  - SMW project-template and other build-pipeline references
  - compare `Mesen 2`, `bsnes-plus`, and `bsnes`
  - evaluate `JaredBrian/AsarUSALTTPDisassembly`, `alttp.run`, and `yaze`
  - evaluate `InsaneFirebat/sm_disassembly`
  - evaluate `smw-project-template`

- [ ] Document emulator working-directory and path behavior
  - capture `bsnes` app-level config/support paths and per-game path behavior
  - inspect the local `snes9x` build for equivalent config/save/state paths
  - decide whether the workspace wants launcher/helper scripts for consistent ROM testing
  - validate whether the `x86_64` Rosetta `bsnes` build is a stable workaround for the Apple Silicon black-video issue
  - [x] Stage a practical `snes9x` macOS app lane and capture its expected config/data paths
  - [ ] Manually verify the native Metal-enabled `bsnes` build against clean and modified ROMs

- [ ] Research multiworld / Archipelago-style crossover synchronization
  - understand protocol shape and state sync assumptions
  - decide whether this is relevant to future crossover ideas or only adjacent inspiration
  - [x] Produce one first-pass shared note on multiworld relevance.

- [ ] Build a “safe first mods” cookbook
  - One low-risk patch example for Zelda
  - One low-risk patch example for Super Metroid
  - [x] One low-risk patch or editor-driven modification for SMW

- [ ] Add a hardware deployment note for `sd2snes`
  - Feature support boundaries
  - Special-chip caveats
  - Real-console verification checklist
  - Keep this scoped as deployment/validation context, not the main day-to-day reverse-engineering focus.

## Research Gaps

- [ ] Pull deeper low-level material from `SMW Central`
  - RAM maps
  - assembly docs
  - patch/tool conventions
  - blocked currently by Cloudflare from simple terminal fetches

- [ ] Inspect whether DiztinGUIsh has a viable non-Windows analysis lane
  - CLI-only export path
  - file-format interoperability
  - whether Windows-only capture unlocks enough value to justify an auxiliary lane at all
