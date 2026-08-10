---
name: process-engine-triage
description: Feedback sensor — collect public feedback (GitHub issues/discussions/stars/forks) and convert it into engine improvements (meta-improvement loop).
compatibility: Turnstone 1.8.x
metadata:
  author: RedEyeNinja-BKK
  version: "1.9.6"
  engine: process-engine 1.9.6
---
## Overview
The engine improves its own process. Feedback is the sensor: issues and
discussions from real users surface what works and what doesn't. Triage
categorizes feedback, proposes process revisions, and gates them through review.

## When to Use
- New GitHub issue/discussion on the public repo.
- Periodic review of stars/forks/discussion themes.
- Any feedback about a generated package or the engine's own process.
- Periodic quality stocktake of deployed skills (adapted from ECC
  skill-stocktake): audit the engine's own skills for quality.
- External skill artifacts shared or discovered follow the intake path
  (references/intake.md) — a sibling of feedback triage, same gate discipline.

## Core Process
1. **Collect** — watch issues/discussions (via monitor/API); note new signals.
   Run periodic stocktake: audit deployed skills for quality (spec
   compliance, trigger accuracy, red-flag substance) and treat findings as
   signals routed like BUG/DESIGN.
2. **Categorize** (with severity + reproduction):
   - BUG (artifact performs wrong or violates the Agent Skills spec) → route
     to pattern-author (fix) + trial (regression)
   - DESIGN (experience flaw) → draft a process/artifact revision → review
   - IDEA (new capability) → log to roadmap; propose to operator
   - SAFETY (risk/scope/safety-adjacent report) → highest priority; review immediately
   Routing names where the work belongs; it does not make the target stage
   active. Before any routed Process Engine stage executes (pattern-author
   fix, review, trial regression), **natively activate/load the canonical
   target stage skill** through Turnstone's native skill mechanism and
   confirm it governs — do not emulate the stage from this skill or prior
   context. If activation cannot be established, stop at the transition and
   report the missing stage activation.
   Each report gets: severity (blocker / major / minor / nit), reproduction
   status (reproduced / not-reproduced / unknown), and deduplication (link to
   an existing report if it is the same defect). Stars/forks are **adoption
   signals**, not quality feedback — do not treat a star as a defect report;
   only substantive issues/discussions enter the categorize step.
3. **Meta-improvement**: if the flaw is in the PROCESS itself, draft a revision
   to the relevant skill/reference → review → trial → ship.
4. **Traceability link**: when a defect concerns a generated package, link it
   to the package/project identity, version/revision, deployed-object
   evidence, and relevant trial evidence when available — traceability from
   feedback to the shipped artifact, using existing Turnstone/GitHub
   evidence (no separate manifest is required).
5. **Report** — plain-language digest to operator; recommend action; wait for
   operator call. Never auto-respond publicly without operator sign-off.

## Examples
- Issue: "generated package X behaves wrong in scenario Y" → BUG → fix
  via pattern-author → regression trial.
- Issue: "generated package X ignored its declared scope boundary in scenario Y"
  → SAFETY → review immediately, tune the per-package safeguard trigger.

## Common Rationalizations
- "It's one user, ignore it." → One real report is signal; triage it properly.
- "We can respond directly on GitHub." → Public replies need operator sign-off.

## Red Flags
- Risk/scope-related feedback deprioritized.
- Responding publicly without operator approval.
- Feedback collected but never converted into action.

## Verification
- [ ] Feedback categorized and logged
- [ ] Stocktake findings (if run) categorized and routed
- [ ] Operator informed with recommendation
- [ ] Action routed (or explicitly deferred by operator)
