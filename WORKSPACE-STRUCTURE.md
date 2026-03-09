# SNES Workspace Structure

The top-level goal of this workspace is still:

- reverse engineer SNES games
- understand how SNES ROMs are built and modified
- learn how patching, randomizers, and reconstruction-heavy hacks work
- produce valid ROM outputs that can run in emulators and on real hardware

The workspace is now organized with **platform-level shared knowledge** at the top and **project swim lanes** underneath.

## Top-level shared layer

These paths stay shared across all SNES work:

- `repos/`
  - upstream source trees and reference repos
- `docs/`
  - shared conceptual and technical notes
- `analysis/`
  - generated ROM facts and shared outputs
- `build/`
  - generated ROMs and local build artifacts worth keeping inside the workspace
- `WORKLOG.md`
  - execution-oriented record of work performed from backlog/roadmap items
- `CHANGELOG.md`
  - durable milestone and workspace-change log
- `roms/`
  - staged clean base ROMs for workspace-local use
- `data/`
  - machine-readable metadata and graph data
- `tools/`
  - local helper scripts
- `BACKLOG.md`
  - workspace-wide backlog
- `ROADMAP.md`
  - workspace-wide roadmap

Use the shared layer for:

- hardware notes
- emulator/tooling notes
- randomizer concepts
- cross-project patterns
- shared research artifacts
- work tracking and milestone logging

## Swim lanes

Each swim lane is a project/output lane inside the SNES umbrella.

Current lanes:

- `lanes/zelda/`
- `lanes/metroid/`
- `lanes/smz3/`
- `lanes/smw/`

Use a swim lane for:

- project-specific notes
- curated repo references for that lane
- findings and hypotheses specific to that game/ecosystem
- lane-specific TODOs once they become substantial

Lane-local backlog files:

- `lanes/zelda/BACKLOG.md`
- `lanes/metroid/BACKLOG.md`
- `lanes/smz3/BACKLOG.md`
- `lanes/smw/BACKLOG.md`

## Intended relationship

Think of the structure like this:

- `snes/` = platform workspace
- `lanes/zelda/` = Zelda-specific output lane
- `lanes/metroid/` = Super Metroid-specific output lane
- `lanes/smz3/` = crossover output lane
- `lanes/smw/` = Super Mario World-specific lane for editor-driven and assembly-heavy hacking workflows

This keeps the workspace from collapsing into either:

- one giant undifferentiated SNES dump
- or many totally disconnected mini-projects with no shared platform layer

## Scope boundary

Non-SNES reverse engineering should live in a different workspace.

This workspace is explicitly for SNES-only work, even if some concepts later generalize.
