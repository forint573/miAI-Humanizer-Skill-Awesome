# Changelog

All notable changes to The Sonnopus Humanizer are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-06-13

The intelligence release. Version 1.0 made copy clean: no AI tells, no process
bleed, no invented facts, no flattened voice. It could still leave copy that was
clean and empty. This release adds the second half of the job, making copy say
something worth reading, while keeping every 1.0 guardrail intact. The value
always comes from the true material. Nothing is invented to add it.

### Added
- `references/substance.md`: the intelligence layer. Defines the "clean nothing"
  failure and the tests that catch it (the swap test, the negation test, the
  so-what ladder, the real question), the keep-the-tension rule, the
  cliché-to-truth move, mode-specific guidance, a voice guard, and worked
  examples, all under one hard boundary: insight is compression of true
  material, never invention.
- `SKILL.md`: a "Make it worth reading" section carrying the four core substance
  tests and the insight-not-invention rule, a reframed mission that names the
  subtractive and additive jobs as co-equal, a substance pass in the drafting
  and cleanup workflows, and a clean-nothing line in the pre-ship checklist.
- `references/qa-scorecard.md`: a new "Substance (worth reading)" category, so
  the new dimension is scored, not just described. A 0 in Truthfulness or
  Substance now caps the result whatever the total.
- `references/ai-tells.md`: a capstone entry, "Clean nothing (the de-slop
  trap)," and a framing note that cutting a tell is only half the job.
- `scripts/copy_scan.py`: an `empty_claim` detector for phrases that fail the
  negation test (committed to excellence, deliver value, help you succeed),
  warned on a cluster. Heuristic, like the rest of the scanner.
- `tests/`: a trigger prompt and a clean-nothing evaluation sample, plus
  automated checks for the new reference file and the empty-claim detector.

### Changed
- The skill description now names the additive job (says something worth
  reading: specific, defensible, non-obvious, not clean but empty) alongside the
  humanizing job, without weakening the existing triggers.
- The scorecard is now nine categories out of eighteen, with rescaled
  thresholds. "Substance preservation" was renamed "Meaning preservation" to
  free the word "substance" for the new value category.
- Root and skill READMEs reframed around two failures and two tests.

### Kept
- Every 1.0 guardrail: fact safety, voice preservation, the lightest effective
  edit, the dash default, and the process-bleed test. The new layer never
  overrides them. When substance is missing, the skill flags a placeholder
  instead of inventing it.

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

[2.0.0]: https://github.com/forint573/miAI-Humanizer-Skill-Awesome/releases/tag/v2.0.0
[1.0.0]: https://github.com/forint573/miAI-Humanizer-Skill-Awesome/releases/tag/v1.0.0
