# Architecture

Process Engine is a Turnstone-native agent-skill framework: a persona, six skills,
seven references, and six session templates that drive a gated authoring pipeline.
Turnstone's native governance mechanisms (prompt policy, advisory judge) enforce
the gates mechanically — the model generates packages; Turnstone owns the guardrails.

For the platform-agnostic prompt+code successor, see
[Method Factory](https://github.com/RedEyeNinja-BKK/Method-Factory).

## Components

```
Process Engine (project)
├── persona: process-engine        # identity, standards, working style
├── skills/ (6)
│   ├── process-engine-core        # entry + routing
│   ├── process-engine-pattern-author
│   ├── process-engine-review
│   ├── process-engine-trial
│   ├── process-engine-ship
│   └── process-engine-triage
├── references/ (7, on core)       # loaded on demand
│   ├── standards.md               # standards checklist
│   ├── safety.md                  # heads-up practice
│   ├── evidence-library.md        # named basis sources
│   ├── skill-anatomy.md           # SKILL.md anatomy
│   ├── best-practices.md          # catalog + spec index
│   ├── intake.md                  # input-agnostic intake
│   └── governance.md              # Turnstone governance objects
└── templates/ (6)                 # session initial prompts
```

## The pipeline

```mermaid
flowchart TB
    A[Intent] --> B[Orient]
    B --> C[Collect]
    C --> D[Clarify]
    D --> E[Objective]
    E --> F[Summary Gate]
    F -- operator confirms --> G[Pattern]
    F -- material or intent unclear --> C
    G --> H[Review]
    H -- REVISE --> G
    H -- operator sign-off --> I[Trial]
    I -- FAIL --> G
    I -- all PASS --> J[Ship]
    J --> K[Deployed package]
    J -- verify read-back --> L[Evidence recorded]
    L --> M[Feedback to Triage]
    M -- BUG or design --> G
```

**Pipeline gates** (v1.9.5): every stage has an operator gate. Turnstone's native
prompt policy and advisory judge enforce these mechanically.

- **Orient** — declare scope and ask what to build.
- **Collect** — the engine invites material (links, text, files, docs) and
  routes each item through intake (input-agnostic, extract-author-original).
  Exits on any non-material reply.
- **Clarify** — one question at a time, informed by the collected material.
- **Objective** — the engine asks what "good" looks like; the vision seeds
  the package's objective and outcomes.
- **Summary Gate** — summary of material + intent + vision; operator confirms.
- **Pattern** — eligibility gate decides the shape; pattern-author designs
  the package to standard, names evidence, builds per-package safeguards
  for risk-relevant intents, writes acceptance criteria. Output: DRAFT.
- **Review** — standards checklist, spec-compliance check, anatomy check,
  coverage check, adversarial pass. Verdict with evidence; operator sign-off
  is the gate.
- **Trial** — case set from acceptance criteria + scope surface (happy path,
  gray zone, escalation, boundary, trigger set), actual vs expected
  recorded. Depth scales with the package's domain.
- **Ship** — confirm gates, define rollback, deploy via Turnstone's native
  API, verify by read-back, record evidence.

## Release integrity

`process-engine.toml` is the canonical release manifest (version, lineage,
artifact counts). `tools/validate.py` + the GitHub Actions release gate
enforce structural integrity: version consistency, link resolution,
frontmatter validity. The evaluator-era steps have been retired.
Evaluator evidence is preserved at
[Method Factory](https://github.com/RedEyeNinja-BKK/Method-Factory).

## Native mechanisms used

| Artifact | Native mechanism |
|---|---|
| Project | `POST /v1/api/projects` |
| Persona | `POST/PATCH /v1/api/admin/personas` |
| Skills + templates | skills API (`prompt_templates` store): `POST/PUT /v1/api/admin/skills` |
| References | skill resources: `POST /v1/api/admin/skills/{id}/resources` |
| Governance enforcement | Prompt policy (content-only, no tool_gate) + advisory judge rules |
| Session start | prompt templates (orientation + starters) |

## Store format vs repository format

Turnstone's native store keeps skill metadata in API fields (name, description,
content), with frontmatter shown as a `yaml` code block inside content. The
Agent Skills open format standard uses real YAML frontmatter at the top of
`SKILL.md`. The repository keeps the spec-valid form; the native store keeps
its native form. Content is otherwise identical.
