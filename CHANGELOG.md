# Changelog

All notable changes to The Sonnopus Humanizer are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-06-13

The intelligence and integrity release. Version 1.0 made copy clean: no AI
tells, no process bleed, no invented facts, no flattened voice. This release
adds two things the first half made necessary. First, the substance to make
copy worth reading, not just clean. Second, the safety layer the substance
demands: a humanizer is a persuasion amplifier, and the better it works, the
more it can harm when the claims are not sound. So the same release that adds
persuasive force adds the firewall. Persuasion never outruns evidence,
load-bearing caveats survive every edit, and the skill humanizes honest copy
but refuses to manufacture proof, scarcity, urgency, or a real person's words.
The value always comes from the true material. Nothing is invented to add it.

This release also states the skill's honest scope plainly across the files: it
turns a quick sketch into a consumable template that a human finishes into final
prose, not publish-ready copy, and it chains with the Hungarian translation
skill for interpretive, native Hungarian rather than a literal calque.

### Added
- `references/substance.md`: the intelligence layer. Defines the "clean nothing"
  failure and the moves that catch it (the swap test, the negation test, earning
  a claim by showing the mechanism, the so-what ladder, the real question), the
  keep-the-tension rule, the cliché-to-truth move, mode-specific guidance, a
  voice guard, and worked examples, all under one hard boundary: insight is
  compression of true material, never invention. Earning a claim by showing why
  it is true, rather than asserting it, is the move that turns persuasion into
  something the reader actually learns.
- `references/integrity.md`: the do-more-good-than-harm layer the scanner
  always referenced but the skill never spelled out. Persuasion never outruns
  evidence, load-bearing caveats (safety, legal, financial, uncertainty)
  survive every edit, authenticity is never manufactured (no fabricated
  reviews, social proof, scarcity, urgency, or putting words in a real person's
  mouth), the substance moves are bounded by all of it, and humanizing is named
  as the wrong tool for disguising authorship where disclosure is expected.
- `SKILL.md`: a "Make it worth reading" section carrying the four core substance
  tests and the insight-not-invention rule, a "Do more good than harm" section
  carrying the integrity rules, a reframed mission that names the subtractive
  and additive jobs as co-equal and binds both to the harm rule, a substance
  pass and a harm check in the workflows, and clean-nothing plus harm lines in
  the pre-ship checklist.
- `references/qa-scorecard.md`: new "Substance (worth reading)" and "Integrity
  (do more good than harm)" categories, so the new dimensions are scored, not
  just described. A 0 in Truthfulness, Substance, or Integrity caps the result
  whatever the total.
- `references/ai-tells.md`: a capstone entry, "Clean nothing (the de-slop
  trap)," and a framing note that cutting a tell is only half the job.
- `scripts/copy_scan.py`: an `empty_claim` detector for phrases that fail the
  negation test, a `risky_claim` detector for high-liability claims (guarantees,
  absolutes, medical, financial, or regulated, #1 or world's-best), and a
  `manufactured_pressure` detector for fabricated scarcity, urgency, and social
  proof. Heuristic, like the rest of the scanner.
- `references/translation-handoff.md`: how to chain with
  `translating-english-to-hungarian`. Humanize in English first, translate last
  and interpretively, pass the formal or informal register (`ön` or `te`) with
  the voice, keep placeholders untranslated, carry the integrity rules across
  the language line, and let Hungarian typography win in the Hungarian output.
- `tests/`: a clean-nothing sample, an overclaim and manufactured-pressure
  sample, trigger prompts for substance and integrity work, plus automated
  checks for the new reference files and the empty-claim, risky-claim, and
  manufactured-pressure detectors.

### Changed
- The skill description now names the additive job (says something worth
  reading: specific, defensible, non-obvious, not clean but empty) alongside the
  humanizing job, without weakening the existing triggers.
- The scorecard is now ten categories out of twenty, with rescaled thresholds
  and Integrity as a gating category. "Substance preservation" was renamed
  "Meaning preservation" to free the word "substance" for the new value category.
- Root and skill READMEs reframed around two failures, two tests, and the
  do-more-good-than-harm standard.
- Positioning made explicit across the files: the skill turns quick sketches
  into consumable templates that humans finish into final prose, not
  publish-ready copy. Finalization mode, the workflows, and both READMEs now
  say so.

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
