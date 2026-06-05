# The Sonnopus Humanizer

A Claude Agent Skill for drafting, finalizing, and humanizing reader-facing marketing and long-form copy.

It exists to stop one common failure: the finished deliverable starts narrating the hidden production process behind it. The copy mentions the chat, outline, roadmap, prior draft, internal decision, or scaffold instead of speaking directly to the reader about the product, offer, proof, objection, and next step.

## What this version optimizes

The package is built around six choices:

- Short invocation metadata, so the model can trigger the skill reliably.
- Lean `SKILL.md`, so the active instruction layer is clear for both Sonnet and Opus.
- Deeper references, so the model can inspect examples and diagnostics only when useful.
- Strong fact safety, so the skill never invents metrics, testimonials, proof, awards, or claims.
- Voice preservation, so it improves copy without flattening it into one house style.
- Optional scanner, so long deliverables can be checked for leftover process bleed and wrapper text.

## Core principle

Every sentence should pass this test:

> Would this sentence make sense to a reader who never saw the project, chat, plan, outline, prompt, or drafting process?

If not, it is process bleed. Cut it or rewrite it around the reader, product, offer, proof, objection, or next step.

## Installation

Upload the package where custom Claude skills are supported. The archive keeps the skill folder at the root.

## Testing

Use `tests/test-prompts.md`. The most important checks:

1. It triggers for landing pages, e-books, reports, product copy, and humanizing requests.
2. It does not trigger for code, raw data, legal terms, changelogs, or casual chat.
3. It replaces missing proof with visible placeholders instead of inventing facts.
4. It removes process bleed without deleting real meaning.
5. It preserves a provided voice sample rather than forcing a generic style.

## Optional scanner

Run:

```bash
python scripts/copy_scan.py draft.txt
```

The script flags likely process bleed, wrapper text, dash usage, vague authority, and hype clusters. It is intentionally heuristic. Treat its output as warnings, not verdicts.
