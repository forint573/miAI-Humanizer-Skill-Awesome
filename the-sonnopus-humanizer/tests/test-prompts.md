# Test prompts for The Sonnopus Humanizer

Use these after installation to check trigger behavior and output quality.

## Should trigger

1. Humanize this landing page copy and make it sound less like AI.

2. Finalize the homepage copy from the outline we built earlier. Remove planning notes and make it paste-ready.

3. Draft a sales page for this offer using only the proof in the brief.

4. Clean up this e-book chapter. Keep the same arguments, but remove the "in this chapter" style and make it read naturally.

5. Rewrite this email sequence in our founder voice. Do not invent metrics or testimonials.

6. This homepage copy is clean but it doesn't say anything. Make it sharper and more specific.

7. Tighten this health product copy, but do not overstate the claims or drop the safety caveats.

8. Turn this rough sketch into a clean, consumable template I can finish, and mark any placeholders.

9. Humanize this landing page in English first, then we will translate it to Hungarian.

## Should not trigger

1. Refactor this Python function.

2. Convert this CSV into a table.

3. Write release notes for version 2.1 from this changelog.

4. Summarize these legal terms plainly without changing the meaning.

5. Chat with me about whether this idea is good.

## Evaluation samples

### Process bleed sample

Input:

Based on our discussion, this guide starts by explaining the problem, then moves into the framework we decided on. After careful consideration, we landed on three pillars. In this section, we will explore the first pillar.

Expected behavior:

Remove the chat, plan, decision path, and section meta. Rewrite around the reader's problem and the framework's actual value.

### Unsupported proof sample

Input:

Our platform cuts onboarding time by 73% and is trusted by leading enterprises.

No source is provided.

Expected behavior:

Do not keep the 73% or "leading enterprises" as fact. Replace with `[ADD VERIFIED METRIC]` or weaken the claim.

### Clean-nothing sample

Input:

We are committed to excellence and passionate about delivering value. Our innovative solutions help businesses succeed and exceed expectations every day.

Expected behavior:

Recognize clean nothing. Every line fails the negation test: no one advertises the opposite, so the lines carry no information. Do not just swap the hype words for plainer ones, since that produces a cleaner version of nothing. Ask for the real mechanism, number, tradeoff, or named user, and replace each empty claim with a specific, defensible point or a visible placeholder such as `[ADD THE REAL MECHANISM]`. Never invent the specifics to fill the gap.

### Overclaim and manufactured-pressure sample

Input:

Our course guarantees you will double your income in 30 days. Join 50,000 students who transformed their lives. Only 2 spots left, enroll before midnight.

No source backs the numbers, the guarantee, or the scarcity.

Expected behavior:

Do not keep "guarantees," "double your income," "50,000 students," or "only 2 spots left" as fact. Persuasion must not outrun evidence: weaken or flag the guarantee, and replace the unverified numbers and the scarcity with placeholders such as `[ADD REAL ENROLLMENT COUNT]` and `[CONFIRM REAL DEADLINE]`. Never fabricate the proof, the result, or the urgency.

### Voice preservation sample

Input includes a casual founder paragraph with short sentences, plain words, and a little skepticism.

Expected behavior:

Preserve that rhythm. Do not turn it into corporate brochure copy.

### Over-editing trap

Input contains one em dash, one formal transition, and otherwise specific human writing.

Expected behavior:

Do not rewrite everything. Remove or keep the dash based on the user's brand preference, but preserve the voice and meaning.
