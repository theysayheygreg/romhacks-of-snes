# bsnes macOS Rendering Note 01

This note captures the current `bsnes` video failure on the Apple Silicon Mac used for this workspace.

## Symptom

- ROMs load
- audio plays
- the window stays black

This reproduces with:

- the locally built `arm64` app from `repos/bsnes`
- the current official nightly macOS app

## Local source findings

The macOS build in this codebase only exposes one real video backend:

- `OpenGL 3.2`

Relevant local sources:

- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/bsnes/ruby/video/video.cpp`
- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/bsnes/ruby/video/cgl.cpp`
- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/bsnes/bsnes/target-bsnes/program/video.cpp`

Important details:

- `Video::hasDrivers()` on macOS resolves to `OpenGL 3.2` plus `None`
- `VideoCGL` is the macOS implementation path
- there is no Metal renderer in the current `bsnes` macOS path here
- the UI code already contains comments noting that `video.clear()` is not working on `macOS/OpenGL 3.2`

## Upstream issue match

The strongest upstream match is:

- [bsnes issue #320](https://github.com/bsnes-emu/bsnes/issues/320): `OpenGL driver logs error and produces no video output on MacOS M3`

The issue body describes the same shape:

- native Apple Silicon build
- audio works
- no video output
- OpenGL driver warning on macOS

One later comment reports it still happening on an M1 MacBook Air on Sequoia.

## Architecture finding

Current local/source-nightly observations:

- locally built workspace app is `arm64`
- the current official nightly macOS asset also unpacks to an `arm64` binary

That means the current nightly is not a useful architecture control, because it reproduces the same native Apple Silicon path.

## Practical workaround hypothesis

The best current workaround hypothesis is:

- use an `x86_64` macOS build under Rosetta

Why:

- the matching upstream issue explicitly said an older `x86_64` nightly still rendered while native Apple Silicon builds failed
- this workspace successfully produced a clean `x86_64` app bundle for testing at:
  - `/Users/theysayheygreg/Documents/SNES/emulators/bsnes-x86_64-20260309.app`

## Current recommendation

For this Mac:

- keep `bsnes` source as a reference/debugging codebase
- treat native `arm64` `bsnes` GUI builds as currently unreliable for runtime video testing
- test the `x86_64` Rosetta build next
- if that still fails, prefer `snes9x` as the pragmatic emulator lane and real hardware via `sd2snes` as final truth
