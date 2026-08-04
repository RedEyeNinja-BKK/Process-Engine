---
name: process-engine-trial
description: Trial harness — scripted cases and trigger sets that prove an artifact performs correctly before it ships.
compatibility: Turnstone 1.8.x
metadata:
  author: RedEyeNinja-BKK
  version: "1.9.5"
  engine: process-engine 1.9.5
---
## Overview
Trials are the engine's proof. Every package is trialed before shipping.
Trial depth is proportionate to the package's domain: simple skills get
focused cases; risk-relevant packages get adversarial coverage and trigger
sets. The operator decides what's sufficient.

Risk-relevant packages additionally get safeguard-specific drills per their
per-package spec.

## When to Use
- After review PASS, before ship.
- When an artifact is revised in ways that change its performance or scope.
- Regression: re-run cases after any change.

## Core Process
1. **Define cases** from the artifact's acceptance criteria and scope surface:
   - happy path (e.g. normal use of the package)
   - gray zone (e.g. input near the scope boundary — must be handled per
     package scope, not guessed)
   - escalation (e.g. input beyond the declared scope — must engage the
     package's own handling path)
   - boundary (e.g. input that clearly exceeds scope → decline/route per
     package scope)
   - trigger set (should-trigger queries + shouldn't-trigger near-misses):
     varied phrasing, explicitness, detail, complexity — exercises the
     package's descriptions, which carry the activation burden.
   Scale case depth to the package: a simple standup-notes skill needs
   2-3 deterministic cases from the acceptance criteria. A risk-relevant
   package needs the full case suite.
2. **Define fixtures** — setup stubs: model config, persona, skill, scenario
   input. Emit case sets in a structured format (id, prompt, expected_output).
3. **Run** each case with clean context; record actual vs expected result.
4. **Score**: PASS / FAIL per case; document failures precisely. Activation
   results must separately report should-trigger recall and shouldn't-trigger
   precision; do not collapse an unrun set into a score.
5. **Hand back**: trial evidence → pattern-author (revisions) or review
   (re-verify) or ship (all pass).

## Examples
- Case: out-of-scope request → input outside the package's declared domain →
  expected: decline and route, never guess. Actual recorded.
- Trigger case: near-miss query sharing keywords with the package's domain
  but needing something else → expected: no activation. Actual recorded.

## Common Rationalizations
- "I know it works, I tried it once." → One informal try is not a trial.
- "Real users are the trial." → For risk-relevant packages, real users are the
  LAST step, after adversarial cases pass.
- "The description will activate fine; I wrote it well." → Trigger sets exist
  because activation is the failure mode. Prove it.

## Red Flags
- Shipping an artifact with no trial evidence.
- Trials that only test the happy path.
- No trigger set for a package with activation-dependent skills.
- Ignoring a FAIL case ("edge case, won't happen").

## Verification
- [ ] Cases defined for all acceptance criteria + scope surface
- [ ] Trigger set run (where package has activation-dependent skills)
- [ ] Every case run, actual vs expected recorded
- [ ] All PASS (or failures routed back to author/review)
- [ ] Trial evidence recorded in the project
