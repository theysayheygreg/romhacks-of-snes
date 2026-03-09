# Build Outputs

This directory is for generated ROMs and other local build outputs.

Policy:

- Generated binaries stay out of git by default.
- Keep filenames descriptive and stable enough for manual testing.
- When an output matters, record it in `WORKLOG.md` and summarize the milestone in `CHANGELOG.md`.

Suggested naming:

- `zelda-working-YYYYMMDD.sfc`
- `super-metroid-test-YYYYMMDD.sfc`
- `smw-test-YYYYMMDD.sfc`
- `smz3-seed-<seed>.sfc`

When a build artifact is important, note:

- base ROM used
- patch or tool used
- date
- expected behavior
- whether it was emulator-tested or hardware-tested
