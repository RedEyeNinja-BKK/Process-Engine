---
name: process-engine-review
description: The engine's review gate — spec compliance, standards, scope, evidence, safeguards, and acceptance-criteria check before anything ships. Operator sign-off is mandatory.
compatibility: Turnstone 1.8.x
metadata:
  author: RedEyeNinja-BKK
  version: "1.9.6"
  engine: process-engine 1.9.6
---
## Overview
Reviews a draft against the engine's standards. Produces a verdict (PASS /
REVISE / REJECT) with evidence. NEVER auto-ships — the operator's sign-off is
the gate.

## When to Use
- Any artifact after pattern-author produces a draft.
- Re-review after revisions.

## Core Process
1. **Standards checklist** (references/standards.md): evidence-named? scope
   honest? acceptance criteria present?
2. **Spec compliance check**: validate generated skills against the Agent
   Skills open standard — name lowercase-hyphen ≤64 matching the directory,
   description ≤1024 with triggering language, allowed frontmatter fields only,
   SKILL.md present. Two separate evidence steps:

   **A. Native parse evidence.** For each generated SKILL.md, preserve
   evidence that the native Turnstone parse operation actually ran: skill
   identity, native parse invoked, result/success or failure. Review cannot
   PASS a generated SKILL.md without that recorded receipt.

   **B. Allowed-field comparison.** Separately, compare the generated/authored
   frontmatter keys against the current Agent Skills allowed-field contract
   (`name`, `description`, `license`, `compatibility`, `metadata`,
   `allowed-tools`). If any unexpected/non-spec key exists, REVISE — whether
   or not the native parser accepted/parsed the document. Parse success does
   not by itself prove that every frontmatter key is spec-valid.

   Turnstone-specific deployment metadata: use a supported native Turnstone
   object/API field when one exists; if information legitimately belongs in
   the portable SKILL.md, use a valid Agent Skills field such as `metadata`
   when appropriate; otherwise do not invent a SKILL.md frontmatter field and
   do not hallucinate a Turnstone API field.

   **Capability-path consistency**: do procedures that require tools or
   runtime capabilities have an executable path consistent with the generated
   package's persona/tool declarations (procedure → required capability →
   declared/expected runtime tool path)? If a referenced operation has no
   executable declaration in the package, REVISE. Review checks internal
   package coherence here; it does not prove runtime availability — that is
   Trial's job.

   **Destination-skill evidence (generated Turnstone skills)**: for each
   generated Turnstone skill, check the recorded destination-state evidence
   from Pattern:
   - **PROVEN ABSENT** — collision dimension satisfied; do not manufacture a
     collision concern.
   - **PROVEN PRESENT** — require an explicit, reversible, operator-gated
     disposition (e.g. intentional coexistence; create-new then
     operator-approved disable-old; later operator-gated supersession;
     another supported reversible plan that leaves the generated canonical
     `name` unchanged). Review checks the plan; it does NOT execute it.
     Silent overwrite / accidental duplicate assumptions → REVISE.
     **Identity binding:** confirm the recorded destination-skill evidence
     corresponds to the **current canonical `name` in the draft being
     reviewed**. If the evidence belongs to a different skill identity
     (stale receipt after a rename), REVISE — old evidence cannot satisfy
     the collision check. A mere future "rename before deployment" plan is
     NOT sufficient: if the disposition changes identity, the rename must
     happen in Pattern first and the new identity must receive its own
     preflight evidence before Review can evaluate it. If the draft has
     already been renamed and a fresh receipt exists for that exact new
     canonical name, evaluate the new PRESENT/ABSENT/UNPROVEN result
     normally.
   - **UNPROVEN** — for a generated Turnstone skill intended for deployment,
     REVISE with the missing destination-state evidence identified. Do not
     let UNPROVEN silently become PASS merely because Ship later has an
     operator gate.
   Point-in-time: PROVEN PRESENT/ABSENT reflects the named authoritative
   catalog evidence at preflight time; it is not a transactional guarantee
   that catalog state cannot change before Ship.
   Review performs zero catalog mutation: no create, update, enable, disable,
   delete, or supersede. Ship/operator authority remains unchanged.
3. **Safeguard review** (risk-relevant intents only): per-package safeguards
   present, evidence-named, sized to the domain — no preset doctrine
   (references/safety.md).
4. **Anatomy check**: all sections complete and load-bearing
   (references/skill-anatomy.md).
5. **Coverage check**: does the package cover the phases its intent requires
   (references/best-practices.md catalog)?
6. **Adversarial pass**: try to break it — edge cases, gray zones,
   rationalizations a user/agent would make. Include the wrong-entity check:
   could this package act on, describe, or gate the WRONG entity because
   names, IDs, roles, endpoints, or aliases are ambiguous (machines,
   accounts, people, products, records, services)? Ambiguity that could
   change what the package targets is a REVISE finding: the package must
   preserve the ambiguity and require disambiguating evidence, or be changed
   so the target is unambiguous. Do not wave it through as "users will know
   which one."
7. **Verdict + evidence**: PASS / REVISE (specific) / REJECT (why). A REVISE
   verdict returns the artifact through the formal fix loop below — never
   straight to ship.
8. **Operator gate**: present verdict and the draft; only operator sign-off
   advances to trial/ship. Log the verdict.

**Native stage activation on transitions.** Naming the next stage does not
make it active. Before any stage executes after a transition, ensure the
exact canonical target Process Engine skill is **proven natively active** in
the current execution context; if it is not already proven active,
**natively activate/load it** through Turnstone's native skill mechanism and
confirm it governs. If it is already proven active, do not reload it merely
for ceremony. "Already active" means the exact canonical target stage is
proven to govern the current execution context — not memory, stage-name
prose, another PE stage being active, a stale version, or a prior workstream.
Do not emulate an unloaded stage from this skill, Core, references, or prior
context. If activation cannot be established, stop at the transition and
report the missing stage activation — do not silently continue as the target
stage.

## REVISE loop (formal)

1. **Diagnose** — the verdict names each specific finding (what, where, why).
2. **Rewrite** — before Pattern performs the rewrite, ensure the exact
   canonical `process-engine-pattern-author` skill is **proven natively
   active**; if not already proven active, **natively activate/load it**.
   Only the canonical Pattern skill may revise the artifact against the
   findings, preserving intent.
3. **Audit** — before re-review, ensure the exact canonical
   `process-engine-review` skill is **proven natively active**; if not
   already proven active, **natively activate/load it**. The re-review
   confirms each finding is addressed and the result is materially better
   than before. Regression trial re-runs after any change that affects its
   performance or scope — before that regression runs, ensure the exact
   canonical `process-engine-trial` skill is **proven natively active**; if
   not, **natively activate/load it**.

## Examples
- Generated package review: frontmatter spec-valid? acceptance criteria
  present? evidence named? scope limits explicit? safeguards (if risk-relevant)
  present and sourced? → PASS-with-notes or REVISE.
- Skill review: is the Red Flags section real or decorative?

## Common Rationalizations
- "The operator already saw it informally." → Informal ≠ review. Formal
  verdict + sign-off is the record.
- "It passed the checklist, ship it." → Checklist is necessary, not
  sufficient; the operator gate is the sufficient part.
- "The name is fine even if it doesn't match the folder." → Spec requires the
  match; a Turnstone-native skill must validate on the platform.

## Red Flags
- Shipping without a recorded verdict.
- A verdict that ignores the safeguard pass for risk-relevant intents.
- A spec violation waved through ("clients won't notice").
- "PASS" without evidence.
- Identity/alias ambiguity waved through when it could make the package
  act on, describe, or gate the wrong entity.

## Verification
- [ ] Standards checklist completed
- [ ] Spec compliance checked (frontmatter, name/description rules)
- [ ] Native parse evidence recorded in Review (skill identity, parse invoked, result)
- [ ] Allowed-field comparison performed against Agent Skills contract; no unexpected/non-spec frontmatter keys present (REVISE if present, regardless of parse result)
- [ ] Capability-path consistency checked for procedures requiring tools/capabilities (REVISE if no executable declaration)
- [ ] Destination-skill evidence checked for generated Turnstone skills (bound to current canonical name in reviewed draft; PROVEN ABSENT ok; PROVEN PRESENT requires explicit reversible operator-gated disposition without identity change; stale/future-rename receipt or UNPROVEN → REVISE); zero catalog mutation
- [ ] Safeguard review completed (risk-relevant intents only)
- [ ] Coverage check completed against the catalog
- [ ] Verdict recorded with evidence
- [ ] Wrong-entity/ambiguity question asked wherever names, IDs, roles, endpoints, or aliases are material to behavior
- [ ] REVISE loop followed when verdict is REVISE (diagnose → rewrite → audit)
- [ ] Operator sign-off obtained and logged
