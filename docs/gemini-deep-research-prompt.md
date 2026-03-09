# Gemini Deep Research Prompt

Use this prompt when asking Gemini to do a broader deep-research pass, especially across YouTube videos, talks, long-form posts, and community materials that are harder to ingest from the terminal.

```text
I’m building a serious research workspace about SNES romhacking, reverse engineering, randomizers, and editor-driven hack workflows.

Please format your output as a single Markdown document intended to live at:
/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/docs/external-research/gemini-deep-research-001.md

If you cannot write files directly, return the full contents of that Markdown document in your response.

I want a deep research brief focused on three anchor games:
- The Legend of Zelda: A Link to the Past
- Super Metroid
- Super Mario World

I also want general SNES romhacking resources.

Please search broadly across:
- YouTube videos
- conference talks or presentations
- long-form community guides
- official docs and manuals where available
- community wikis
- GitHub repos
- forum posts or archived threads that are considered foundational

What I need:

1. General SNES romhacking ecosystem
- best foundational guides for SNES memory mapping, ROM structure, patching, assemblers, tracing, and emulator debugging
- best explanations of LoROM/HiROM/FastROM in practice
- strong resources for Asar, IPS/BPS/FLIPS, bsnes/snes9x debugging, and SNES reverse engineering workflows

2. Zelda 3 specific
- best resources for ALTTP disassembly, RAM/SRAM/state understanding, room and overworld editing, dungeon logic, and randomizer logic
- guides or videos that explain why ALTTP randomizes so well
- resources on entrance randomizer / door randomizer design
- resources that explain ALttP progression, key logic, and state flags at a low level

3. Super Metroid specific
- best resources for disassembly, RAM/SRAM, room data, PLMs, doors, item placement, map structure, and patching
- guides or videos that explain Super Metroid’s progression logic, movement tech logic, and area randomization
- foundational Super Metroid hacking resources from Metroid Construction or related communities
- anything that clearly explains the relationship between movement skill, world topology, and progression logic

4. Super Mario World specific
- best resources for Lunar Magic, SMWDisX, SMW Central, Callisto, Asar, custom sprites/blocks, Map16, ExGFX, overworld editing, and freespace/insertion conventions
- guides or videos that explain why SMW hacking became so editor-centric
- foundational resources for vanilla hacks, kaizo design, secret-exit graph design, and world-map progression
- anything that explains the relationship between Lunar Magic, ASM patches, and reproducible project build pipelines

5. Game design understanding
For each of the three games, explain:
- the core player loop
- the main verbs
- the progression grammar
- how the world is structured
- what the real design goals are
- what kinds of modifications preserve the original feel
- what kinds of modifications radically transform the game

6. Output format
Please produce:
- a curated resource list grouped by topic and by game
- for each resource: why it matters, what level it targets (beginner/intermediate/advanced), and whether it is more about hacking, gameplay/design, or tooling
- a section for “best YouTube/video resources”
- a section for “foundational community docs”
- a section for “most useful repos/tools”
- a section for “open research questions”
- a final section with 10 concrete next-step research tasks for my workspace

Please structure the Markdown document with these top-level sections:
- Executive Summary
- General SNES Resources
- Zelda 3 Resources
- Super Metroid Resources
- Super Mario World Resources
- Game Design Analysis
- Best Video Resources
- Foundational Community Docs
- Most Useful Repos and Tools
- Open Research Questions
- Next-Step Research Tasks

Important:
- Prefer resources that are still accessible today, but include archived/foundational material if it is historically important.
- Distinguish clearly between source/disassembly resources, editor/tool resources, patch/randomizer resources, and design-analysis resources.
- If there are conflicting tool/version expectations around base ROM revisions, call that out explicitly.
- When possible, include direct links.
- Keep the result high-signal and organized for later distillation into canonical workspace docs.
```
