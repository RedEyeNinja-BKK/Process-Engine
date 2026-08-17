---
name: process-engine-trial
description: Trial harness — scripted cases and trigger sets that prove an artifact performs correctly before it ships.
compatibility: Turnstone 1.8.x
metadata:
  author: RedEyeNinja-BKK
  version: "1.9.6"
  engine: process-engine 1.9.6
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
- When a package is revised after Review or Trial and prior evidence might be reused.
- Regression: re-run cases after a change that affects behavior or scope.
- When the deployable scope changes materially after Trial evidence — previous
  case results may be retained as historical evidence, but cannot qualify the
  changed scope automatically; return through Pattern → Review → Trial as
  applicable.

## Core Process
0. **Determine continuity and applicable categories before running.** If prior
   Review or Trial evidence might be reused, record a concise `material` or
   `non-material` judgment and the reason. A change is material when it can
   affect behavior, acceptance criteria, artifact membership, target/entity
   identity, capability/tool boundaries, safeguards/risk behavior, or
   deployable scope. Editorial, typographical, or equivalent non-behavioral
   cleanup may retain prior evidence when judged non-material. For a material
   revision, record what changed, which applicable categories/cases must run
   again, which prior evidence remains directly valid, and any newly applicable
   category; a sentence or bullets is sufficient, not a formal matrix.

   Then identify which trial categories apply to this package and record the
   set: acceptance-criteria / happy-path cases; gray-zone / boundary /
   escalation cases; identity case when target identity is material;
   trigger/activation set when the package is activation-dependent;
   safeguard-specific drills when risk-relevant. A concise trial-evidence
   summary is sufficient — no persisted state manifest.

0a. **Capability preflight.** Before behavioral cases that depend on runtime
   capabilities, verify the required capability path is actually available in
   the target Trial runtime. If package declarations are internally wrong,
   that should have been caught at Review (REVISE). If the package declaration
   is correct but the runtime capability is unavailable/stale, classify the
   overall Trial as INCOMPLETE — do not score the behavioral case FAIL — and
   report the responsible runtime/tool layer if known.

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
   - identity case (when identity/target selection is material to behavior):
     include at least one contradiction / alias / near-match case — e.g., two
     similar names or IDs, a supplied-vs-live source conflict, or a near-miss
     alias that looks like the target but is not. Record whether the package
     preserved the distinction (or required disambiguation) instead of
     collapsing the entities.
2. **Define fixtures** — setup stubs: model config, persona, skill, scenario
   input. Emit case sets in a structured format (id, prompt, expected_output).
3. **Run** each case with clean context; record actual vs expected result.
4. **Score** per case: PASS / FAIL; document failures precisely. Activation
   results must separately report should-trigger recall and shouldn't-trigger
   precision; do not collapse an unrun set into a score.
5. **Overall Trial verdict** — exactly one of:
   - **PASS**: every applicable required category has direct evidence and all
     required executed cases pass for the qualification scope identified by
     Review and Trial.
   - **INCOMPLETE**: one or more required categories are unrun, blocked,
     unavailable, missing direct evidence, preflight-unavailable, or otherwise
     unproven. INCOMPLETE does not advance to Ship. A later narrowing or other
     material scope change does not convert the prior INCOMPLETE into PASS;
     the changed scope must obtain its own applicable Review and Trial evidence.
   - **FAIL**: a required executed case demonstrates behavior that violates
     the package's acceptance criteria/scope. FAIL returns through
     revision/review.
   Preserve granular case-level PASS/FAIL — the point is to distinguish
   "10/10 executed behavioral cases PASS" from "overall Trial PASS" when
   another required category remains unrun.
6. **Hand back**: only overall PASS may hand off to Ship. INCOMPLETE remains
   in Trial until evidence is complete. FAIL routes to pattern-author
   (revisions) or review (re-verify).

**Native stage activation on transitions.** Naming the next stage does not
make it active. For FAIL requiring package revision, ensure the appropriate
canonical stage skill is **proven natively active** (`process-engine-pattern-author`
for rewrites or `process-engine-review` for re-verification) before that
stage executes; if not already proven active, **natively activate/load it**.
For PASS, do not execute Ship merely because Ship is named: present/retain
the operator Ship gate, and only once Ship is separately authorized should
`process-engine-ship` be **proven natively active** (activated/loaded if not
already) for deployment work. "Already active" means the exact canonical
target stage is proven to govern the current execution context — not memory,
stage-name prose, another PE stage, a stale version, or a prior workstream.
Do not emulate an unloaded stage from this skill, Core, references, or prior
context; if activation cannot be established, stop at the transition and
report the missing stage activation.

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
- No contradiction/alias/near-match case for a package whose behavior
  depends on distinguishing entities (names, IDs, roles, endpoints, aliases).

## Verification
- [ ] Cases defined for all acceptance criteria + scope surface
- [ ] Applicable trial categories determined before running (behavioral, boundary/adversarial, identity where material, trigger/activation where activation-dependent, safeguard where risk-relevant)
- [ ] Capability preflight performed for runtime-dependent cases (unavailable → overall INCOMPLETE, not behavioral FAIL)
- [ ] Identity/alias/near-match case included where identity is material to behavior
- [ ] Trigger set run (where package has activation-dependent skills)
- [ ] Every case run, actual vs expected recorded
- [ ] Overall Trial verdict recorded: PASS (all applicable categories evidenced) / INCOMPLETE (category unrun/unproven) / FAIL (required case violates acceptance criteria)
- [ ] Only overall PASS handed to Ship
- [ ] Trial evidence recorded in the project
