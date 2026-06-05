#!/usr/bin/env python3
"""
copy_scan.py

A lightweight, heuristic scanner for reader-facing copy. It flags likely process
bleed, assistant wrapper text, clusters of generic AI-style prose, vague
authority, and em/en dash usage.

It does NOT judge quality. It is a coarse net for long final deliverables, meant
to catch things a quick read skims past (a leftover dash, a wrapper sentence, a
hype cluster). It produces false positives by design, so treat every result as a
warning to look at, not a verdict. Human judgment always wins, and the skill's
"do more good than harm" rules override anything here.

Usage:
  python scripts/copy_scan.py draft.txt
  cat draft.txt | python scripts/copy_scan.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PATTERNS = {
    # Process bleed: the production journey showing through.
    "process_bleed": [
        r"\bin this (article|guide|section|chapter|report|document|post)\b",
        r"\b(as requested|per your request|based on (our|the) (discussion|conversation|previous conversation|chat)|as you mentioned|you asked me to|as we (discussed|established) earlier)\b",
        r"\b(we decided|we landed on|we considered|after careful consideration|what emerged was|the chosen approach)\b",
        r"\b(we started by|first we|next we|moving into the next phase|finally we arrive|building on (this|that))\b",
        r"\b(through extensive research|carefully crafted|countless hours|our commitment to)\b",
    ],
    # Assistant wrapper: correspondence pasted into the deliverable.
    # Tightened so a real sentence like "Here is a verified interpreter" does NOT match;
    # a wrapper noun (copy/draft/version/etc.) or an assistant phrase is required.
    "assistant_wrapper": [
        r"\b(here(?:'s| is)|below (?:is|you'?ll find)) (?:the |your |a |an )?(?:rewritten|revised|humani[sz]ed|finalized|updated|cleaned[- ]?up|polished|final)?\s*(?:copy|draft|version|text|rewrite|content|piece)\b",
        r"\bhere(?:'s| is) (?:the |your )?(?:rewritten|revised|humani[sz]ed|finalized|polished) (?:version|text)\b",
        r"\b(hope (?:this|that) helps|let me know if|feel free to let me know|i hope this finds you)\b",
    ],
    "generic_hype": [
        r"\b(world-class|cutting-edge|next-gen(?:eration)?|game-changing|best-in-class|future-proof|revolutionary|groundbreaking)\b",
        r"\b(seamless|robust|holistic|comprehensive|pivotal|crucial|vital|transformative)\b",
        r"\b(unlock|empower|leverage|utilize|streamline|foster|facilitate|harness|cultivate|elevate)\b",
        r"\b(actionable insights|value-add|move the needle|digital transformation|paradigm shift)\b",
    ],
    "vague_authority": [
        r"\b(experts say|industry leaders agree|research shows|studies suggest|many believe|some argue|it is widely (?:known|believed))\b",
    ],
    "formulaic_structure": [
        r"\bnot just\b[^.]{0,60}\bbut also\b",
        r"\bit'?s not (only|just)\b[^.]{0,60}\bit'?s\b",
        r"\blet'?s (dive in|explore|break this down|unpack)\b",
        r"\bhere'?s what you need to know\b",
    ],
    "dash_usage": [
        r"[\u2014\u2013]",     # em dash, en dash
        r"\s--\s",             # spaced double hyphen used as a dash
    ],
    # Informational only: presence of placeholders is good, not a problem.
    "visible_placeholders": [
        r"\[[A-Z0-9 _./-]{5,}\]",
    ],
}

# Groups that are real problems when present (or, for hype, when clustered).
PROBLEM_GROUPS = {"process_bleed", "assistant_wrapper", "dash_usage", "vague_authority", "generic_hype", "formulaic_structure"}


def read_text() -> str:
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).read_text(encoding="utf-8")
    return sys.stdin.read()


def context_line(text: str, start: int) -> str:
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", start)
    if line_end == -1:
        line_end = len(text)
    return text[line_start:line_end].strip()


def scan(text: str) -> dict:
    findings = []
    for group, patterns in PATTERNS.items():
        for pattern in patterns:
            for m in re.finditer(pattern, text, flags=re.IGNORECASE):
                findings.append({
                    "group": group,
                    "match": text[m.start():m.end()].strip(),
                    "line": context_line(text, m.start())[:240],
                })

    counts: dict[str, int] = {}
    for item in findings:
        counts[item["group"]] = counts.get(item["group"], 0) + 1

    warnings = []
    if counts.get("process_bleed", 0):
        warnings.append("Process bleed: the copy refers to the project, plan, chat, or decisions. Rewrite around the reader, product, offer, proof, or next step.")
    if counts.get("assistant_wrapper", 0):
        warnings.append("Assistant wrapper text in the deliverable. Delete it; the copy should start with the copy.")
    if counts.get("dash_usage", 0):
        warnings.append("Em/en dash usage. Remove unless it is an exact quote, explicit user preference, or established brand voice.")
    if counts.get("vague_authority", 0):
        warnings.append("Vague authority. Name the source, cite it, weaken the claim, or cut it.")
    if counts.get("generic_hype", 0) >= 3:
        warnings.append("Generic hype cluster. Replace mood words with proof, mechanics, or concrete tradeoffs.")
    if counts.get("formulaic_structure", 0):
        warnings.append("Formulaic AI structure (false contrast, signposting). Rewrite as direct, positive statements.")

    return {
        "summary": counts,
        "warnings": warnings,
        "note": "Heuristic only. Expect false positives. A single hype word or one flagged phrase is usually fine; act on clusters and on clear wrapper/dash/process hits. Human judgment overrides this output.",
        "findings": findings,
    }


def main() -> None:
    result = scan(read_text())
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
