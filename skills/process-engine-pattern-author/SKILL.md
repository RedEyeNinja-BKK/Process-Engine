---
name: process-engine-pattern-author
description: Generate the project/persona/skills package for an intent — to the engine's standard (spec-valid SKILL.md, Osmani anatomy, evidence-named, scope-honest, safeguard-aware, acceptance-criteria'd).
compatibility: Turnstone 1.8.x
metadata:
  author: RedEyeNinja-BKK
  version: "1.9.6"
  engine: process-engine 1.9.6
---
## Overview
Turns an operator intent into the engine's final product shape — a
**project / persona / skills package** (a project, a persona, a single skill,
multiple skills, or not an artifact at all, per the eligibility gate). The
artifact SHAPE is decided up front by the eligibility gate. The package is
generated from the development-engineering best-practices basis
(references/best-practices.md —
full Osmani catalog + Agent Skills spec index): personas as system prompts,
skills as spec-valid SKILL.md following the engine's anatomy
(references/skill-anatomy.md), session
templates, and the project scaffolding. Output is a DRAFT package — always
handed to review.

## When to Use
- New artifact requested (persona, skill, template, doc, repo content).
- Revisions after a review or trial found issues.

## Core Process
1. **Eligibility gate** — decide the artifact shape deliberately: is this a
   project, a persona, a single skill, or multiple skills — or not an
   artifact at all (decline or route elsewhere)? If the shape is unclear,
   ask ONE shape-deciding question (project / persona / skill(s) / not an
   artifact) — never a generic material question; never assume. The shape
   drives everything downstream. When declining (out of scope), decline
   cleanly: state the boundary and route, and do NOT offer to do the
   off-scope work yourself — the engine generates packages, not the domain
   content.
2. **Interpret intent** — use the clarified intent, the collected-input
   summary, and the user's vision of what "good" looks like (the objective
   seed) from core. One clarifying question at a time if still ambiguous;
   never guess scope.
3. **Design the package** — determine the package shape from the intent and the
   best-practices basis (references/best-practices.md):
   - Project scaffolding (name, visibility, owner)
   - Persona → system-prompt shape (identity, scope, standards, style, boundaries)
   - Skills → SKILL.md: spec-valid frontmatter (name ≤64 chars, lowercase
     letters/digits/hyphens, matches the directory name; description ≤1024
     chars, what + when; imperative/user-intent phrasing is PE authoring
     guidance; optional license,
     compatibility, metadata incl. provenance — source URL/date when known)
     + Osmani anatomy body: Overview · When to Use · Core Process · Examples ·
     Common Rationalizations · Red Flags · Verification
   - Design rules: add what the agent lacks, omit what it knows; coherent
     units; moderate detail; progressive disclosure (SKILL.md is the entry
     point, references load on demand)
   - Session templates (initial prompts)
   - Governance artifacts (Turnstone-native): a prompt policy (the package's
     operating stance, content-only, no tool_gate) and advisory judge rules
     (the package's risk posture, on its own tool family). These are native
     governance helpers — advisory, operator-visible, reversible — that
     provide durable contextual guidance and review/trial evidence; they
     never silently replace operator approval. See
     references/governance.md.
   - Objective + desired outcomes — formed from the user's vision of "good":
     the problem being solved and why it matters (objective), and 2–4
     observable end states from the user's perspective (outcomes). If the
     vision was vague or absent, propose a concrete objective in the draft
     for correction at review.
4. **Synthesize from collected material** — extract techniques, domain
   specifics, and intent from ALL user-provided material (any form: skill
   links, text blocks, files, store links, docs — per references/intake.md);
   combine into a best-of-all-worlds design; author ORIGINAL instructions —
   never copy input content verbatim.

   **Preserve identity-critical facts.** When the intent or collected
   material contains identity-critical relationships — an entity paired with
   its roles and its identifiers/endpoints/interfaces/aliases (machines,
   accounts, people, products, records, services) — preserve them in the
   package wherever they affect decisions or tool targets:
   - Record the entity ↔ role ↔ identifier mapping explicitly; never flatten
     distinct identifiers into one, and never infer equivalence the operator
     did not assert.
   - Mutable operational/contextual identity facts (addresses, endpoints,
     interfaces, contact identifiers, account associations, record IDs —
     anything that can change or varies by context) belong in a package
     reference/resource by default; genuinely stable, behavior-defining
     identity (who the agent is, which fixed entities it protects) may live
     in the persona. Do not bloat the persona with mutable operational
     facts.
   - When supplied or live sources disagree on an identity-critical fact,
     preserve the disagreement, name the sources, and require disambiguating
     evidence — never silently select one.
   - If the operator asserts an equivalence (two names are the same entity),
     record it as an operator-supplied fact; otherwise the generated package
     must treat identity equivalence as something to prove or leave open.
5. **Name the evidence** — every technique cites its real source; add to the
   package's evidence library (generated per-package) if new. Bake
   provenance (source URL/date) into each generated SKILL.md metadata when
   the source is known.
6. **Safeguard pass** — if the intent touches a risk-relevant domain (domains
   involving people, regulated activities, or safety-critical systems) or the
   operator designates one, flag it and build per-package safeguards and scope
   limits from the package's own named evidence library and operator direction.
   The engine presets none (references/safety.md). Heads-up, never block.
7. **Acceptance criteria** — write explicit exit criteria into each artifact,
   derived from the objective: the vision of "good" becomes observable exit
   criteria.

   **Executable capability path.** When generated procedures depend on tools
   or runtime capabilities, identify the intended executable capability path
   and keep package declarations internally consistent with it. Conceptually:
   procedure → required capability → declared/expected runtime tool path.
   The path must be coherent with the persona/tool declarations and **any
   skill-level `allowed-tools` constraints when present** (Agent Skills
   treats `allowed-tools` as optional/experimental — do not require every
   generated skill to add it; the reasoning must also work when a skill
   legitimately omits that field). This is package-design reasoning, not a
   separate manifest/artifact. Do not prescribe specific tools or mechanisms
   (shell, MCP, wrappers, reloads) — require coherence, not implementation
   doctrine.

   **Destination-skill preflight (generated Turnstone skills).** Once a
   generated skill's canonical Agent Skills `name` is selected and the
   intended destination is Turnstone, perform a destination-state preflight
   **when an authoritative native read-only skill-catalog capability is
   available in the active generator context** — do not run it before the
   proposed identity exists, and do not make it another pipeline stage.
   Record exactly one of:
   - **PROVEN PRESENT** — authoritative Turnstone catalog evidence shows an
     existing destination skill whose identity materially collides with the
     proposed generated skill. Preserve the proposed canonical name, the
     existing skill identity/name, returned object identity where available,
     and the evidence source.
   - **PROVEN ABSENT** — use only when the authoritative Turnstone lookup
     semantics genuinely support proving absence for the queried skill
     identity. A generic search returning zero results is NOT automatically
     PROVEN ABSENT.
   - **UNPROVEN** — generator lacks the authoritative read surface; the
     lookup cannot establish absence; the result is ambiguous; returned
     identity cannot be resolved confidently; or the lookup fails. Never
     guess.
   Do not invent a fuzzy-matching or normalization engine: use the generated
   Agent Skills canonical `name`, authoritative Turnstone skill identity/name
   fields, and native matching semantics where provided. When returned
   evidence reveals casing/display-name/identity ambiguity, preserve it — do
   not silently collapse distinct identities without evidence about their
   object identities. Broader semantic overlap may be surfaced as a heads-up
   when materially useful, but is NOT a mandatory catalog-wide ritual.
   If PROVEN PRESENT, you may propose possible dispositions for later
   operator consideration (rename the new skill; retain/coexist
   intentionally; later supersede the old skill; revise/update where
   supported). You must NOT choose one automatically, and must NOT create,
   update, enable, disable, delete, or supersede anything. Destination-state
   evidence informs the draft; it does not grant mutation authority. This
   scope is generated **skills** only — do not extend to personas, projects,
   policies, templates, or every Turnstone artifact without evidence.

   **Identity-bound evidence.** The recorded destination-skill evidence is
   valid only for the **same canonical skill identity it queried**. Keep the
   queried/proposed canonical Agent Skills `name`, returned destination
   identity/object evidence where applicable, the PRESENT/ABSENT/UNPROVEN
   state, and the evidence source together as one reviewable unit (no new
   manifest or persisted schema). If a collision disposition changes the
   generated skill's canonical `name` (e.g. `openclaw-management` →
   `openclaw-remote-maintenance`), that is a **revision**, not merely a
   future deployment instruction: update the draft identity, **re-run the
   destination-skill preflight for the new canonical name**, record fresh
   PRESENT/ABSENT/UNPROVEN evidence, and return to Review. The old receipt
   must not carry forward as evidence for the new identity. No re-run is
   required when the disposition leaves the generated canonical `name`
   unchanged (intentional coexistence using the same proposed identity;
   later operator-gated supersession of an existing skill; another
   disposition that does not change the canonical name).

   **Point-in-time semantics.** PROVEN PRESENT / PROVEN ABSENT means proven
   by the named authoritative catalog evidence **at the time of the
   preflight**. It is destination-state evidence for author/review, not a
   transactional guarantee that catalog state cannot change before Ship.
   Do not create locks, reservations, state leases, transactional catalog
   logic, or a new Ship preflight on this evidence.
8. **Assemble the package** — project/persona/skills/templates/governance as
   one bundle; skill folders mirror the spec layout (SKILL.md + references/ +
   optional scripts/ and assets/) when shipped as repo content.
9. **Hand off** — mark DRAFT and hand the package to `process-engine-review`.
   Naming Review does not make it active: before Review executes, **natively
   activate/load `process-engine-review`** through Turnstone's native skill
   mechanism and confirm the canonical Review skill governs. Do not emulate
   Review from this skill, Core, references, or prior context. If the native
   activation cannot be established, stop at the handoff and report the
   missing stage activation — do not proceed as if Review ran.

## Examples
- "I want a skill that writes release notes" → package: project + persona
  (system-prompt shape) + skills (release-notes skill, spec-valid SKILL.md,
  Osmani anatomy) + templates.
- "I want a package for a database-backup operator skill" → package: skill
  (spec-valid frontmatter, Osmani anatomy, examples, verification), template,
  reference additions.

## Common Rationalizations
- "I'll add sources later." → Sources are part of the draft, not a retrofit.
- "This intent is too small to need safeguards." → If the intent touches
  people or regulated domains, safeguards are part of the package, sized to
  the domain.
- "The description can be vague; the body explains it." → The description
  carries the whole triggering burden. Write it imperative and explicit about
  scope (PE authoring guidance) — or the skill never activates.

## Red Flags
- An artifact with no evidence naming, no safeguard pass (risk-relevant
  intents), or no acceptance criteria.
- A SKILL.md whose frontmatter violates the spec (name rules, description
  limits, unknown fields).
- Draft presented as "done" instead of "draft for review".
- A generated package that could act on, describe, or gate the WRONG entity
  because identity-critical facts were dropped, flattened, or silently
  resolved (e.g., two names/IDs/endpoints collapsed as if equivalent).

## Verification
- [ ] Eligibility gate passed — shape decided (project / persona / skill(s) / not an artifact)
- [ ] Correct anatomy chosen and complete
- [ ] Objective formed from the user's vision ("good") — or proposed in draft when underspecified
- [ ] Skill frontmatter spec-valid (name rules, description ≤1024, allowed fields)
- [ ] Provenance metadata included where source known
- [ ] Package folder layout follows the spec (SKILL.md + references/ + optional scripts/assets)
- [ ] Evidence named for every technique
- [ ] Safeguard pass done for risk-relevant intents (per-package, sourced)
- [ ] Identity-critical relationships preserved (entity ↔ role ↔ identifiers) where they affect decisions or tool targets; conflicts kept visible until disambiguated; no silent equivalence inference
- [ ] Governance artifacts: prompt policy + advisory judge rules (Turnstone-native)
- [ ] Acceptance criteria written
- [ ] Executable capability path identified where procedures depend on tools/capabilities; package declarations internally consistent with it (no prescribed tool/mechanism doctrine)
- [ ] Destination-skill preflight recorded for generated Turnstone skills when authoritative native catalog read is available (PROVEN PRESENT / PROVEN ABSENT / UNPROVEN); no mutation; no automatic disposition
- [ ] Marked DRAFT, handed to review
