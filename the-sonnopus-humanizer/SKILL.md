---
name: the-sonnopus-humanizer
description: "Write, finalize, and clean up reader-facing marketing and long-form copy (landing pages, e-books, reports, case studies, sales and product copy, founder notes) so it reads like a specific human or brand wrote it, stays about the reader and product, and never exposes the planning process. Apply it proactively when finalizing a deliverable at the end of a long build session, where roadmaps, outlines, internal decisions, scaffold files, or chat history leak into the output. Also use when asked to humanize, de-slop, make something sound less like AI, rewrite naturally, tighten, polish, or clean up prose. It preserves facts, never inventing numbers, names, or results, and edits lightly without flattening real voice. Not for code, data, changelogs, release notes, legal terms, or casual chat."
---

# The Sonnopus Humanizer

Use this skill to draft, finalize, or clean up reader-facing copy so it sounds like a specific human or brand wrote it, stays truthful, and never exposes the planning process that produced it.

The core job is simple: keep the finished piece about the reader, the product, the offer, the proof, the objection, and the next step. Remove anything about the chat, outline, roadmap, internal decisions, drafts, prompts, files, or production process unless the user explicitly asked for a retrospective, changelog, or process document.

## Scope

Use this for finished or near-finished copy: landing pages, websites, sales pages, e-books, reports, case studies, product copy, email copy, founder notes, brand copy, and editorial marketing copy.

Also use it when the user asks to humanize, finalize, polish, clean up, rewrite naturally, make less AI-sounding, de-slop, or turn planning work into a reader-facing deliverable.

Do not use it for code, raw data, tables, changelogs, release notes, legal terms, technical reference docs, or casual chat. In those cases, clarity and factual structure matter more than this copy posture.

## Choose the mode

Drafting: write new copy from the brief. Do not invent facts the brief did not give you.

Finalization: turn a planned or half-built artifact into publishable copy. This is the highest-value use. Strip scaffolding, planning residue, assistant wrapper text, and outline language.

Cleanup: improve an existing draft. Preserve the meaning, claims, caveats, sections, and proportions unless the user asks for a deeper rewrite.

Use the lightest mode that solves the task. Do not perform a full rescue rewrite when a clean polish is enough.

## The one test

Apply this question to every sentence:

> Would this sentence make sense to a reader who never saw the project, chat, plan, outline, prompt, or drafting process?

If not, it is process bleed. Cut it or rewrite it around the reader, product, offer, proof, objection, or next step.

The production journey is not the reader's journey. The reader arrives with uncertainty and needs a reason to understand, trust, choose, buy, reply, or act. That journey is the spine.

## Process bleed to remove

Look for these seven leaks:

1. Roadmap narration: describing the order the content was built or will be presented.
2. Artifact meta: saying "in this guide," "this section explores," or announcing the content instead of delivering it.
3. Conversation residue: "as discussed," "as requested," "based on our chat," or any wrapper meant for the requester.
4. Decision disclosure: "we decided," "we landed on," "we considered," or internal strategy talk.
5. Effort padding: "after extensive research," "carefully crafted," or effort used as a substitute for value.
6. Scaffold residue: phases, TODOs, placeholders, outline labels, bracket notes, or template headers left in the copy.
7. Self-praise: calling the piece comprehensive, definitive, carefully crafted, best-in-class, or similar.

Three of the most common, with the move (describe the thing, not the making):

- Roadmap. Before: "In this guide, we will start with the fundamentals, then move to advanced tactics." After: "Most teams get the fundamentals wrong in the same three places. Fix those first."
- Wrapper or conversation. Before: "Great question. Here is the landing-page copy you asked for. Let me know if you want changes." After: delete it and ship only the copy.
- Scaffold. Before: "Phase 1: Awareness. Phase 2: Consideration. [add stats later]." After: "A buyer arrives with one question: will this work for someone like me? [ADD REAL PROOF]"

For the full set and the fast scan phrases, use `references/process-bleed.md`.

## Human prose rule

Be specific, vary rhythm, prefer plain constructions, and never fabricate.

Specific beats generic. Use real names, numbers, mechanics, tradeoffs, and examples when the source provides them. If the source does not provide them, leave a visible placeholder.

Rhythm should vary. Mix short sentences with longer ones. Avoid a uniform mid-length cadence.

Plain beats inflated. Prefer is, has, does, gives, costs, saves, shows, and works over serves as, boasts, showcases, leverages, facilitates, underscores, or represents.

Point of view is allowed when the format supports it. Do not inject personality into legal, technical, compliance, or reference material.

## Dash default

Default to no em dashes or en dashes in final marketing copy. Replace them with a period, comma, colon, parentheses, or a restructured sentence.

Keep a dash only when it is part of an exact quotation, an explicit user preference, or an established brand voice. Do not misquote a source to satisfy this rule.

## Fact safety

Never invent or strengthen specifics. This includes numbers, names, dates, quotes, testimonials, case-study results, awards, certifications, customer logos, integrations, pricing, guarantees, legal claims, compliance claims, and performance claims.

When a useful detail is missing, use a visible placeholder such as `[ADD VERIFIED METRIC]`, `[ADD REAL CUSTOMER EXAMPLE]`, `[ADD SOURCE]`, or `[VERIFY CLAIM]`.

If a claim is plausible but unsupported, weaken it, mark it for verification, or cut it. Do not make the copy sound more certain than the source allows.

## Voice safety

If the user provides a writing sample, brand voice, or style guide, follow that over this skill's default taste. Match sentence length, vocabulary, formality, directness, humor level, opening style, and closing style.

With no sample, default to grounded, concrete, direct, and mildly opinionated only where the format allows. Do not stamp one edgy persona onto every project.

Do not over-edit good human writing. A single formal word, transition, salutation, or dash is not proof of AI writing. Act on clear process bleed, factual risk, or clusters of generic prose.

## Workflow

For drafting or finalization:
1. Identify the reader, product, offer, proof, main objection, and next step from the provided material.
2. Write the deliverable only. Do not put planning notes, rationale, or assistant wrapper inside the copy.
3. Apply the sentence test, fact safety, voice safety, and dash default.
4. Deliver clean copy. Put any editorial note outside the deliverable, and only if useful.

For cleanup:
1. Scan for process bleed first.
2. Scan for unsupported specifics and overclaims.
3. Scan for clusters of AI-flavored prose using `references/ai-tells.md` only as a diagnostic lookup.
4. Rewrite with the smallest effective edit.
5. Preserve substance. If you remove or restructure something for strategy reasons, say so outside the rewritten copy.

## Before shipping

Check these in order:

- No sentence refers to the chat, request, prompt, project plan, outline, file system, internal decisions, or drafting process.
- Every paragraph serves the reader's situation, product behavior, offer, proof, objection, or next step.
- Every specific is supplied by the input or marked with a visible placeholder.
- The voice matches the provided sample or the format.
- Em and en dashes are removed unless an exception applies.
- No assistant wrapper remains: no "here is the copy," "below is," "hope this helps," or "let me know."
- The output is the deliverable the user asked for, not a commentary about making it.

For long deliverables, you may run `scripts/copy_scan.py` as a warning net. Treat the script as a scanner, not a judge.

## References

- `references/process-bleed.md`: expanded examples and fast scan phrases.
- `references/ai-tells.md`: diagnostic catalog for generic AI prose. Use it on clusters, not isolated words.
- `references/qa-scorecard.md`: score finished copy before shipping or when testing the skill.
- `references/voice-calibration.md`: quick voice matching guide.
- `scripts/copy_scan.py`: optional heuristic scanner for long drafts.
