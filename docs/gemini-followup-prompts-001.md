# Gemini Follow-up Prompts 001

Use these after the first Gemini report.

Each prompt is narrower and verification-oriented.
The goal is to turn the broad first-pass into sources we can trust and distill.

## Prompt 1: Verify External References

```text
I’m working in a local SNES reverse-engineering workspace.

Please format your output as a single Markdown document intended to live at:
/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/docs/external-research/gemini-reference-verification-001.md

If you cannot write files directly, return the full contents of that Markdown document in your response.

I previously produced a broad research brief, but now I need a verification pass.

Please verify the following claimed references against primary or highly credible sources:

- bsnes-plus
- Mesen-S
- ZScream
- MathOnNapkins Zelda 3 disassembly reference
- JaredBrian Zelda 3 disassembly lineage
- Zelda 3 Compendium
- alttp.run RAM/SRAM references
- P.JBoy Super Metroid disassembly
- sm_disassembly for Super Metroid
- Kejardon Super Metroid technical docs
- smw-project-template
- Displaced Gamers videos relevant to SNES reverse engineering
- Danofmosttrades Lunar Magic / SMW hacking videos

For each item, determine:
- what it actually is
- whether it is current, historical, deprecated, or ambiguous
- whether it is worth adding to a canonical SNES romhacking workspace
- the best primary link or archive link
- what category it belongs to:
  - source/disassembly
  - editor/tool
  - debugger/emulator
  - community docs
  - video/teaching
  - randomizer logic

Output structure:
- Executive Summary
- Verified Keep
- Historical But Useful
- Ambiguous / Needs More Caution
- Not Recommended
- Direct Links Table
- Suggested Workspace Updates

Important:
- Prefer primary sources over summaries.
- If you cannot confidently verify something, say so explicitly.
- Distinguish clearly between “important historically” and “recommended today”.
- Keep the result focused on what should enter a serious research workspace.
```

## Prompt 2: Metroid PLM and Logic Deep Dive

```text
I’m building a Super Metroid reverse-engineering lane inside a larger SNES research workspace.

Please format your output as a single Markdown document intended to live at:
/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/docs/external-research/gemini-metroid-plm-deep-dive-001.md

If you cannot write files directly, return the full contents of that Markdown document in your response.

I want a focused research brief on:
- PLMs in Super Metroid
- room state headers
- Bank $84 / Bank $8F style documentation and community conventions
- how randomizer logic data maps onto these low-level engine structures

Please search across:
- Metroid Construction
- GitHub repos
- technical docs
- forum posts or archived docs if foundational
- videos only if they are genuinely technical and useful

What I need:

1. PLM understanding
- what PLMs are
- how they are loaded and updated
- what kinds of game objects they cover
- why they matter for items, doors, crumble blocks, and interactivity

2. Room and state structure
- how room headers and state headers work
- how event-dependent room variations are represented
- where the community usually documents these structures

3. Randomizer relationship
- how item randomizers and map randomizers interact with PLMs, room data, and door data
- whether the logic layer and the ROM-structure layer tend to live in separate repos or files

4. Output format
- concise technical summary
- best references with links
- terms and concepts glossary
- “best next local tasks” section for a workspace already containing:
  - strager/supermetroid
  - RandomMetroidSolver
  - MapRandomizer

Important:
- prioritize technical sources over broad overviews
- clearly separate verified low-level facts from community terminology or conventions
- if multiple disassemblies or docs disagree, call that out
```

## Prompt 3: SMW Build Pipeline and Template Verification

```text
I’m building a Super Mario World hacking lane inside a larger SNES research workspace.

Please format your output as a single Markdown document intended to live at:
/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/docs/external-research/gemini-smw-pipeline-verification-001.md

If you cannot write files directly, return the full contents of that Markdown document in your response.

I need a focused verification pass on the modern SMW project pipeline.

Current local anchors in the workspace:
- SMWDisX
- Lunar Magic
- callisto
- a clean Super Mario World (USA) ROM

Please research and verify:

1. Modern project-template / build-template references
- whether `smw-project-template` is the right current reference
- what repo is actually most recommended today for a source-first SMW project
- whether `callisto` is the central orchestration tool in that workflow

2. Pipeline structure
- how mature SMW hacks currently combine:
  - clean ROM
  - Lunar Magic
  - Asar
  - PIXI
  - GPS
  - AddmusicK
  - Callisto or similar tooling
- which parts are still editor-driven versus source-first

3. Version expectations
- which base ROM revisions are most commonly expected today
- where SMW U 1.00 fits
- whether there are major caveats for Japanese or other revisions

4. Output format
- Executive Summary
- Verified Modern Pipeline
- Tool Roles
- Recommended Template Repos
- Version / Base ROM Notes
- Suggested Workspace Updates

Important:
- prioritize primary repo docs and major community references
- distinguish “common in the community” from “best-engineered today”
- call out if the ecosystem is fragmented rather than pretending it is unified
```

## Prompt 4: Multiworld / Archipelago Relevance

```text
I’m researching whether multiworld synchronization ideas are relevant to a SNES romhacking workspace focused on Zelda 3, Super Metroid, SMW, and crossover ideas like SMZ3.

Please format your output as a single Markdown document intended to live at:
/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/docs/external-research/gemini-multiworld-archipelago-001.md

If you cannot write files directly, return the full contents of that Markdown document in your response.

I want a technical/product-oriented research brief on:
- Archipelago and similar multiworld systems
- how they synchronize state across games
- how much of that is relevant to future crossover or randomizer ideas versus being a separate domain

What I need:

1. System overview
- what Archipelago is
- how multiworld state is represented
- how item/location synchronization usually works

2. SNES-specific relevance
- which SNES games and randomizers commonly integrate with it
- whether ALTTP / Super Metroid / SMZ3 style projects are already represented
- whether support tends to be patch-based, emulator-based, or external-client based

3. Design relevance
- what parts are actually useful for future design work:
  - shared progression graphs
  - item/location abstraction
  - networked progression
  - cross-game rule translation

4. Output format
- Executive Summary
- Technical Model
- SNES Relevance
- Useful Ideas for This Workspace
- Probably Out of Scope
- Suggested Next Tasks

Important:
- focus on architectural relevance, not just player-facing descriptions
- include links to primary docs or repos when possible
- be honest if the result is “interesting but not immediately useful”
```
