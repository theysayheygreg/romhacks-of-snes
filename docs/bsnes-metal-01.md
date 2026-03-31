# bsnes Metal Note 01

This note captures the first real macOS Metal backend implementation for the vendored `bsnes` source tree in this workspace.

## Goal

Fix the Apple Silicon macOS black-video issue in native `bsnes` by adding a native Metal video driver instead of relying only on the existing Cocoa OpenGL path.

## Source branch

The implementation currently lives in the vendored `bsnes` repo here:

- repo: `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/bsnes`
- branch: `codex/metal-macos`
- commit: `afc9e74`

## Built app

Two useful app paths now exist:

- repo build output:
  - `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/bsnes/bsnes/out/bsnes.app`
- staged test app:
  - `/Users/theysayheygreg/Documents/SNES/emulators/bsnes-metal-20260331.app`

## Implementation shape

The new driver is:

- `ruby/video/mtl.cpp`

Related source changes:

- `ruby/GNUmakefile`
- `ruby/video/video.cpp`
- `bsnes/target-bsnes/settings/settings.cpp`

Current behavior:

- adds a native `Metal` driver beside the legacy `OpenGL 3.2` macOS path
- prefers `Metal` on this Mac by migrating existing saved `OpenGL 3.2` driver selections to `Metal`
- keeps the existing Cocoa/window integration model
- uses a Metal texture upload plus textured-quad render path
- supports the existing `None` vs `Blur` shader setting as nearest vs linear sampling
- preserves the current `bsnes` viewport sizing contract by honoring the requested output rectangle inside the drawable

Current limitation:

- this is not a full port of the OpenGL shader stack to Metal
- the current Metal driver is a pragmatic rendering backend focused on getting native Apple Silicon output working
- custom OpenGL multi-pass shader folders are not implemented in the Metal path yet

## Verification state

Verified:

- Metal-enabled app builds cleanly on this Mac
- live `bsnes` settings currently resolve to `Driver: Metal`

Still pending:

- manual visual verification that ROM output renders correctly in the Metal build
- comparison against the `snes9x` reference lane using the same ROMs

## Why this was the chosen fix

- the existing macOS path in `bsnes` is hard-wired to Cocoa + `NSOpenGLView`
- upstream issue `#320` matches the Apple Silicon symptom exactly
- `bsnes` already vendors Metal code in the imported SameBoy Game Boy frontend, which made a native macOS Metal path a reasonable direction
- adding a new driver is much less invasive than trying to repair Apple Silicon behavior inside deprecated macOS OpenGL
