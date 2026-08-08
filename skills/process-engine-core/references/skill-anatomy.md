# references/skill-anatomy.md — SKILL.md anatomy (Osmani + Agent Skills spec + engine additions)

Every generated skill follows this shape:

1. YAML frontmatter — spec-valid per the Agent Skills open standard:
   name (lowercase letters/digits/hyphens, ≤64 chars, matches the directory
   name), description (≤1024 chars, what + when; imperative phrasing is PE
   authoring guidance), optional
   license, compatibility, metadata (incl. provenance — source URL/date when
   known), allowed-tools.
2. Overview — what the skill does
3. When to Use — triggers and conditions
4. Core Process — step-by-step workflow
5. Examples — concrete patterns
6. Common Rationalizations — excuses and rebuttals (anti-rationalization)
7. Red Flags — signs the skill is being violated
8. Verification — exit criteria checklist (non-negotiable)

Engine additions:

- **Evidence section** — named sources for every technique.
- **Safeguard section** — ONLY when the package's intent touches a risk-relevant
  domain: per-package scope limits and safeguards (references/safety.md).
- **Governance artifacts** — every package carries a prompt policy + judge
  rules (helper, advisory, no tool_gate — references/governance.md).
- **Progressive disclosure** — SKILL.md is the entry point; references load on demand.
- **Identity placement** — stable, behavior-defining identity facts (who the
  agent is, which fixed entities it protects) may live in the persona; mutable
  operational/contextual identity facts (addresses, endpoints, interfaces,
  contact identifiers, account associations, record IDs) go in
  references/resources, not the persona. Identity-critical mappings
  (entity ↔ role ↔ identifiers) are preserved wherever they affect decisions
  or tool targets; conflicts between sources stay visible until disambiguated.
