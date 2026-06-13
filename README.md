<div align="center">

# The Sonnopus Humanizer ✸☽

**Humanize AI-written marketing and long-form copy in Claude. It removes AI tells and process bleed, keeps your facts and your voice, and pushes past clean-but-empty writing to the specific, true point worth reading.**

[![CI](https://github.com/forint573/miAI-Humanizer-Skill-Awesome/actions/workflows/ci.yml/badge.svg)](https://github.com/forint573/miAI-Humanizer-Skill-Awesome/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-d97757.svg)](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
[![Made for Sonnet & Opus](https://img.shields.io/badge/Made_for-Sonnet_%26_Opus-8a63d2.svg)](#)

</div>

---

## TL;DR

The Sonnopus Humanizer drafts and de-slops marketing and long-form copy: landing pages, e-books, reports, case studies, sales pages, product copy, and founder notes. It keeps the writing about the reader and the product, it refuses to invent facts, and it preserves a real voice instead of flattening it into house style. It also does the part most humanizers skip: it makes the copy say something. Clean but empty is a failure here, not a finish line.

It is built for copywriters, marketers, and founders who draft with AI and want copy that does not read like AI. It is not an AI-detector bypass. It makes weak copy read like a person actually wrote it, and worth the reader's time once they did.

Install it in one line, then ask Claude to humanize your copy.

```bash
git clone https://github.com/forint573/miAI-Humanizer-Skill-Awesome.git && \
  cp -r miAI-Humanizer-Skill-Awesome/the-sonnopus-humanizer ~/.claude/skills/
```

Then open Claude and say *"humanize this landing page"* or *"finalize this draft and strip the planning notes."* That is the whole setup.

---

## What it is

The Sonnopus Humanizer is an [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for marketing and long-form copy. It fixes two failures at once.

The first is process bleed: the finished piece starts narrating the hidden work behind it. The copy points at the chat, the outline, the roadmap, an earlier draft, or a leftover scaffold instead of speaking to the reader about the product, the offer, the proof, the objection, and the next step.

The second is clean nothing: the copy comes out tidy and de-slopped and still says nothing only this writer could say. Most humanizers stop at the first failure and ship the second. This one treats both as failures. The standard it holds copy to is not "reads like a human wrote it" but "a sharp human would be glad they wrote it, and a busy reader is glad they read it."

It also avoids the two ways humanizing usually backfires:

- It never invents numbers, names, testimonials, results, awards, or claims. Missing proof becomes a visible placeholder, not a fabrication. The substance it adds always comes from your material, never from a confident guess.
- It never flattens good human writing into one generic voice. A provided writing sample beats the skill's default taste every time.

## The two tests

Every sentence in the output should pass two questions. The first catches process bleed:

> Would this sentence make sense to a reader who never saw the project, chat, plan, outline, prompt, or drafting process?

If not, cut it, or rewrite it around the reader, product, offer, proof, objection, or next step.

The second catches clean nothing:

> Could this exact sentence appear on a competitor's page, or about a different product?

If yes, it carries no information. Replace it with the specific, true thing only this writer could say, drawn from the real material.

## See it in action

The first row carries two problems at once: it narrates the chat and the plan, and it ships an unverified number as fact. The second row is clean but empty. The right cells are what the skill returns.

| Before | After |
| --- | --- |
| *"Based on our discussion, this guide starts with the problem, then moves into the framework we landed on. Our platform cuts onboarding time by 73% and is trusted by leading enterprises."* | *"Onboarding breaks down in three predictable places. Here is where, and how to fix each one. `[ADD VERIFIED METRIC]` `[ADD NAMED CUSTOMER]`"* |
| *"We're committed to excellence and deliver world-class solutions that help businesses succeed."* | *"Your reps stop copying leads between four tabs. The CRM writes call notes back to the deal on its own, so follow-up happens the same day instead of next week. `[CONFIRM SUPPORTED INTEGRATIONS]`"* |

In the first row, the chat reference and the roadmap narration are gone and the copy opens on the reader's problem. The unsupported `73%` and the vague "leading enterprises" are flagged for a human to verify, not shipped as proof. The second row shows the other half of the job: the committed-to-excellence line passes every grammar check and still says nothing, so the skill replaces it with the specific mechanism a competitor could not claim, and flags the one detail it cannot verify.

## Install

Three ways, fastest first.

**1. One line, Claude Code.** Installs a personal skill that is available in every project:

```bash
git clone https://github.com/forint573/miAI-Humanizer-Skill-Awesome.git && \
  cp -r miAI-Humanizer-Skill-Awesome/the-sonnopus-humanizer ~/.claude/skills/
```

For a project skill that travels with one repo, copy the folder into that repo's `.claude/skills/` instead.

**2. Installer script.** From a clone, run `./install.sh` for user scope, or `SCOPE=project ./install.sh` to install into the current repo. To install without cloning first:

```bash
curl -fsSL https://raw.githubusercontent.com/forint573/miAI-Humanizer-Skill-Awesome/main/install.sh | bash
```

**3. Packaged `.skill` file.** Download it from the [Releases](https://github.com/forint573/miAI-Humanizer-Skill-Awesome/releases) page, or build it yourself:

```bash
make build   # writes dist/the-sonnopus-humanizer.skill
```

Upload that file anywhere custom Claude skills are accepted. The archive keeps the skill folder at its root.

## Use it

Once installed, Claude reaches for the skill on its own when you ask for things like:

- "Humanize this landing page and make it sound less like AI."
- "Finalize the homepage copy from the outline. Remove planning notes and make it paste-ready."
- "Draft a sales page for this offer using only the proof in the brief."
- "Clean up this e-book chapter. Keep the arguments, but lose the self-announcing intros."
- "This copy is clean but it says nothing. Make it specific and sharp without inventing anything."

It stays out of the way for code, raw data, tables, changelogs, release notes, legal terms, technical reference docs, and casual chat. There, factual structure matters more than this posture.

## Optional scanner

For long drafts, a heuristic scanner flags leftover process bleed, wrapper text, hype clusters, empty claims, vague authority, and em or en dashes:

```bash
python the-sonnopus-humanizer/scripts/copy_scan.py draft.txt
# or
cat draft.txt | python the-sonnopus-humanizer/scripts/copy_scan.py
```

It produces false positives on purpose. Treat each result as a reason to look, not a verdict. Human judgment always wins.

> This README was written with the skill's own rules: no em dashes, no hype clusters, no process bleed, no invented facts, nothing that fails the swap test. The only places the rules are broken on purpose are the *Before* cells above, which exist to show the patterns the skill removes.

## What's inside

```text
the-sonnopus-humanizer/
├── SKILL.md                      # the active instruction layer
├── README.md                     # the skill's own package notes
├── references/
│   ├── process-bleed.md          # the seven leaks, examples, fast-scan phrases
│   ├── substance.md              # the intelligence layer: how to say something worth reading
│   ├── ai-tells.md               # diagnostic catalog of generic AI prose
│   ├── qa-scorecard.md           # 9-category, 0 to 2 readiness score
│   └── voice-calibration.md      # matching a sample or brand voice
├── scripts/
│   └── copy_scan.py              # optional heuristic scanner
└── tests/
    └── test-prompts.md           # trigger / no-trigger checks and samples
```

## Design notes

- **Lean active layer.** `SKILL.md` holds only what the model needs in context to act. The deeper catalogs live in `references/` and load on demand, which keeps the instruction layer clear for both Sonnet and Opus.
- **Clean is not the finish line.** De-slopping removes what should not be there. `substance.md` supplies what should: the specific, defensible point only this writer could make. The skill treats clean-but-empty copy as a failure and draws the substance from your material, never from an invented fact.
- **Diagnose on clusters, not words.** `ai-tells.md` names why something reads as machine written. One formal word, one transition, or one dash is not proof of AI writing.
- **Lightest effective edit.** Drafting, finalization, and cleanup are separate modes. The skill picks the smallest one that solves the task instead of rewriting good prose for its own sake.

## FAQ

**Who is this for?**
Copywriters, marketers, founders, and anyone who drafts marketing or long-form copy with AI and wants it to read like a person wrote it.

**Does it bypass AI detectors?**
No. This is not an AI-detection bypass tool. It improves real copy: it removes AI tells and process bleed, flags unverified claims, and keeps your voice. The goal is honest, publishable writing, not gaming a detector.

**Which models does it work with?**
It is written for Claude and tuned for both Sonnet and Opus. It works anywhere Claude reads skills, including Claude Code, the desktop and web apps, and any setup that accepts custom skills.

**Will it invent facts to fill a gap?**
No. Missing proof becomes a visible placeholder such as `[ADD VERIFIED METRIC]`, never a fabricated number, name, or testimonial.

**Does it just remove AI words, or does it actually improve the writing?**
Both, and the second part is the point. Removing tells leaves a gap, and a gap filled with a cleaner version of nothing is still nothing. The skill fills it with a specific, defensible claim drawn from your material, the kind a competitor could not also make. If the substance genuinely is not there, it flags the gap instead of inventing one.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md). Changes to behavior should keep [`tests/test-prompts.md`](the-sonnopus-humanizer/tests/test-prompts.md) honest and pass the automated checks (`make check`).

## License

Apache License 2.0. Copyright 2026 Virág Làzár Csaba ✸☽. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

> "Claude", "Sonnet", and "Opus" are model names from Anthropic. This is an independent community skill. It is not affiliated with or endorsed by Anthropic.
