# references/evidence-library.md — Engine basis sources

This file holds the engine's OWN basis sources. Per-package evidence libraries
are generated with each package (named sources relevant to that domain).

- **Skill anatomy / engineering discipline:** Addy Osmani, agent-skills (MIT),
  github.com/addyosmani/agent-skills — process-not-prose, anti-rationalization,
  verification non-negotiable, progressive disclosure, evals pattern. Full
  catalog index: references/best-practices.md.
- **Agent Skills open format standard:** agentskills/agentskills (code
  Apache-2.0, docs CC-BY-4.0), github.com/agentskills/agentskills — SKILL.md
  specification (frontmatter rules, progressive disclosure), trigger-optimized
  description doctrine, eval methodology (trigger sets, with/without baseline),
  skills-ref reference implementation. The engine's generated skills comply
  with this standard.
- **Evidence-naming rule:** any technique referenced by a generated package must
  name its real source; never "research shows" without a citation.
- **Security/risk basis (proportional):** OWASP Cheat Sheet Series
  (github.com/OWASP/CheatSheetSeries) — AI Agent Security, LLM Prompt
  Injection Prevention, and MCP Security cheat sheets provide proportional
  security/risk guidance when a generated package's intent, material, tools,
  or domain make security relevant. This is a named, proportional basis, not
  universal security boilerplate: generated packages are not claimed to be
  "OWASP-compliant," and OWASP recommendations are not applied universally.

The engine's universal generation basis is intentionally limited to
development-engineering practice (Osmani workflow discipline + Agent Skills
format/authoring guidance); OWASP is the named proportional cross-cutting
security/risk basis, applied when a package's intent/material/tools/domain
make security relevant. Domain references (medicine, finance, law, and
similar) are supplied per-package at generation time — never preset here.
