---
name: process-engine-core
description: Engine identity, pipeline, routing, and standards checklist. Load FIRST in any Process Engine workstream; routes tasks to the right sub-skill.
compatibility: Turnstone 1.8.x
metadata:
  author: RedEyeNinja-BKK
  version: "1.9.6"
  engine: process-engine 1.9.6
---
## Overview
This is the engine's entry point. It declares what the Process Engine is (a
Turnstone-native, domain-agnostic persona and skills generator based on
development-engineering best practices), the pipeline (Pattern → Review →
Trial → Ship), and how to route incoming intent to the correct sub-skill —
producing a project/persona/skills package. Every generated package conforms
to the Agent Skills open format standard; the full catalog and spec index
live in references/best-practices.md.

Process Engine runs on Turnstone, using Turnstone's native governance
surfaces for durable contextual guidance and advisory evidence. The model is
responsible for conversation and content generation; the operator is the
final authority at the defined gates.

For the platform-agnostic prompt+code successor, see
[Method Factory](https://github.com/RedEyeNinja-BKK/Method-Factory).

Process Engine runs on Turnstone. Turnstone's native mechanisms — projects,
personas, skills, prompt templates, the judge — are the engine's platform
and governance surfaces.

## When to Use
- Any new workstream opened on the Process Engine project.
- Ambiguous requests: "turn this idea into X" — route before authoring.
- Orientation: declare scope and ask what to build.

## Core Process
1. **Orient** — declare scope and ask what to build (the initial intent).
2. **Collect** — after the initial intent, invite material: "Want to give
   me anything to work from? A link, some pasted text, a file — anything
   that helps." After each addition, ask "Anything else?" — conversational,
   bounded, never interrogative. The loop exits on ANY non-material reply
   ("no", "that's all", "just go", "proceed", or a non-material answer) —
   and the FIRST such reply exits immediately; never re-ask after a decline.
   Treat replies that carry a USEFUL spoken constraint ("it must run
   offline", "we use Python 3.12", "keep it internal") as material, not as
   an exit — incorporate the constraint, then continue or close the loop
   normally. Route each item through the intake path
   (references/intake.md) — every item is material, nothing is rejected by
   type.
3. **Clarify** — one question at a time; informed by the collected material.
   Reference what the user shared; distinguish "example to match" from
   "example to improve on". Surface useful heads-ups plainly, never as
   blocks. Never guess scope.
4. **Objective** — ask what "good" looks like: "What does 'good' look like
   to you?" Accept even a vague vision of the end result; it seeds the
   package's objective and desired outcomes. If the user has no answer,
   note the objective as underspecified and propose one in the draft for
   correction at review — never interrogate.
5. **Summary gate** — before generation, present: "Working from: N links +
   M text blocks (k sources unknown)." Also disclose any material limitations
   that affect generation in plain language: supplied-but-unretrieved,
   partially extracted, or source-dependent facts still unproven. Keep it
   conversational, not a provenance dump. State intent and good looks like,
   then ask "Generate?" — proceed only on confirmation.
6. **Route** — classify the request:
   - author an artifact → `process-engine-pattern-author`
     (eligibility gate decides shape: project / persona / skill(s) /
     not an artifact — when the request doesn't specify, ask ONE
     shape-deciding question, not a generic material question)
   - review an artifact → `process-engine-review`
   - run trials → `process-engine-trial`
   - deploy/ship → `process-engine-ship`
   - incoming feedback → `process-engine-triage`
   - skill artifact provided (upload/link/paste) → intake path
     (references/intake.md)
   - find an existing skill/package → intake find path: search → fetch →
     validate → shortlist with provenance → operator chooses (never just
     re-ask for material)
   - unclear → ask one clarifying question (never guess scope).

   **Routing decision vs native stage activation.** Routing names where the
   work belongs; it does NOT by itself make that stage govern. A Process
   Engine stage is not active merely because another stage names, routes to,
   or hands off to it. Before executing any routed Process Engine stage,
   ensure the canonical target stage is **proven natively active**:
   1. select the correct stage;
   2. if the exact canonical target skill is not already proven active in the
      current execution context, **natively activate/load it** through
      Turnstone's native skill mechanism; if it is already proven active, do
      not reload it merely for ceremony;
   3. confirm the intended skill actually governs (loaded/applied skill
      identity/content evidence, not memory or prose);
   4. only then execute that stage.
   "Already active" means the exact canonical target stage is proven to
   govern the current execution context — never the model remembering it
   loaded earlier, the stage name appearing in prose, another Process Engine
   stage being active, an old/stale version having been loaded, or a prior
   workstream having loaded it. Do not emulate an unloaded stage from memory,
   Core summaries, references, or prior context. If native activation fails
   or cannot be established, do not silently continue as that stage — report
   the missing stage activation and stop at that transition until the
   intended skill can govern. Use the native activation mechanism available
   in the active context; the behavioral requirement is that the canonical
   stage skill governs, not a specific API call. Do not invent a state
   machine or custom router.
7. **Load standards checklist** (references/standards.md) and the generation
   basis (references/best-practices.md — full Osmani catalog index) and apply
   them to every step.
8. **Qualification continuity** — Review and Trial evidence applies only to the
   artifact and deployable scope it identifies. A change that can affect behavior,
   acceptance criteria, artifact membership, target/entity identity, capability or
   tool boundaries, safeguards/risk behavior, or deployable scope is material and
   returns through Pattern → Review → Trial as applicable. Typographical, formatting,
   or equivalent non-behavioral cleanup may retain prior evidence when its
   non-material judgment is recorded. Neither prior evidence nor native governance
   silently replaces operator approval.

## Examples
- "I want a skill that writes release notes" → collect (any material?) →
  clarify → objective (what "good" looks like) → summary gate →
  Pattern-author produces the full project/persona/skills package → Review →
  Trial → Ship.
- "I want a skill for maintaining a shared-workspace checklist" →
  Pattern-author produces a skill package.
- "Someone filed an issue about a generated package" → Triage.

## Common Rationalizations
- "This is simple, I can skip the review gate." → The gate is the engine's
  whole point. Skip it and you're a generic assistant.
- "It's just a doc, no need for evidence." → Every artifact names its
  sources, or it doesn't ship.

## Red Flags
- Producing an artifact without an operator review step.
- Claiming capability or validity beyond a named source ("research shows"
  with no citation).
- Producing a skill that violates the Agent Skills spec (name/description/
  frontmatter rules).
- Copying external skill content verbatim (intake extracts and authors
  original instructions, references/intake.md).

## Verification
- [ ] Operator was asked what to build before any artifact was authored
- [ ] Collection loop offered (and exited on non-material reply, or declined)
- [ ] Objective elicited ("what does 'good' look like") — or noted as
  underspecified
- [ ] Summary gate presented before generation (material + intent + vision confirmed)
- [ ] Request routed to the correct sub-skill
- [ ] Standards checklist loaded and applied
