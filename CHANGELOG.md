# Changelog

All notable changes to The Sonnopus Humanizer are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-05

First public release.

### Added
- `SKILL.md` — the active instruction layer: scope, modes, the one sentence
  test, the seven process-bleed leaks, human-prose rules, dash default, fact
  safety, voice safety, the workflow, and the pre-ship checklist.
- `references/process-bleed.md` — expanded leak examples and fast-scan phrases.
- `references/ai-tells.md` — diagnostic catalog of generic AI prose patterns,
  meant to be applied to clusters rather than isolated words.
- `references/qa-scorecard.md` — an 8-category, 0–2 scorecard for judging
  whether finished copy is production-ready.
- `references/voice-calibration.md` — quick guide for matching a provided
  writing sample or brand voice.
- `scripts/copy_scan.py` — optional heuristic scanner that flags process
  bleed, assistant wrapper text, hype clusters, vague authority, and dashes.
- `tests/test-prompts.md` — trigger / no-trigger prompts and evaluation
  samples for checking behavior after install.
- `install.sh` — one-command installer (user or project scope, curl-pipeable)
  so the skill drops into a Claude skills folder in a single step.
- README with a `TL;DR`, one-line install, a before/after example, an FAQ, and
  the skill's own rules applied to its copy (no em or en dashes, no hype
  clusters, no process bleed, no invented facts).
- Repository scaffolding: Apache-2.0 LICENSE, NOTICE, CONTRIBUTING,
  CODE_OF_CONDUCT, build script, automated checks, and CI.

[1.0.0]: https://github.com/forint573/miAI-Humanizer-Skill-Awesome/releases/tag/v1.0.0
