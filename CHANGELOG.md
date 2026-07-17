# Changelog

All notable changes to this repository are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
Versions map to git tags (`vX.Y.Z`) and to the plugin version in
`.claude-plugin/marketplace.json`, so plugin users receive an update only when a
new version is released.

## [1.0.0] - 2026-07-17

### Added

- Claude Code plugin marketplace: install every skill with
  `/plugin marketplace add easyzoom/aix-skills` and
  `/plugin install aix-skills@aix-skills`.
- Four new integration skills: `cellular-at-modem-integration`,
  `gnss-gps-integration`, `battery-charger-fuel-gauge-integration`, and
  `tflite-micro-integration`.
- README-to-`skills/` sync validation (missing/extra rows, duplicates, and the
  `skills-N` badge count) in `scripts/validate-skills.py`.
- Release tooling: `scripts/release.py` and a tag-triggered GitHub Release
  workflow.

### Changed

- `scripts/validate-skills.py` now parses frontmatter with a real YAML parser,
  so valid multi-line descriptions are no longer rejected.
- Aligned `template/skill-template` and `docs/skill-authoring.md` with the
  section conventions used by the existing skills.
- Grounded five previously thin skills (`plooc-integration`,
  `heatshrink-integration`, `micro-ecc-integration`, `cortex-r5-debug`,
  `openocd-jlink-stlink-debug`) with real APIs, registers, and commands.

### Removed

- The unused `awesome/` placeholder directory and its issue template.
