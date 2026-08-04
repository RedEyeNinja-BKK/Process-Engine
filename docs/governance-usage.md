# Governance Usage — Process Engine × Turnstone's Governance Surface

> **Status:** DEPLOYED (2026-08-01). Live: prompt policy `process-engine-context`
> (content-only, priority 1) + heuristic rule `process-engine-authoring`
> (advisory, review, low risk). Operator is the only gate — every governance
> artifact is advisory, never blocking, always reversible.
>
> **Context:** Process Engine runs on Turnstone, using Turnstone's native
> governance surface to enforce the engine's core philosophy mechanically:
> collect before creating, operator-gated shipping, nothing ships untried,
> heads-up not police.

---

## 1. Why Turnstone

Turnstone's Governance surface is the engine's enforcement layer — a
first-class, self-hosted mechanism over how agents operate:

| Harness | Governance surface |
|---|---|
| **Turnstone** | Full — projects, personas, roles, policies, prompts, judge, audit |
| Hermes | Agent runtime (skills, toolsets, tasks) — no governance objects |
| OpenClaw | Agent + channels (Discord/LINE) — emission-focused |
| Claude | Commercial harness — no governance layer |

Process Engine's "operator is the gate" philosophy maps directly to Turnstone's
approval surfaces. The governance layer is not an add-on — it's the engine's
native enforcement mechanism. The model generates packages; Turnstone owns
the guardrails.

---

## 2. Governance as capability, not guardrail

Process Engine uses Turnstone's Prompts and Judge surfaces as Turnstone
capabilities — not as guardrails. Every use is advisory, never blocking:

- **Prompt policy** — anchors the engine's operating stance persistently
  across sessions (collect-first, operator-gated, heads-up posture).
- **Advisory judge** — produces intent verdicts as auditable evidence
  during trials and reviews, always informing the operator, never
  replacing their approval.

Tool policies remain off the table. The operator is the only gate.

---

## 3. Deployed governance artifacts

### Prompt policy: `process-engine-context`

A content-only, priority-1 prompt policy stating the engine's durable
operating stance. Every session on the Process Engine project starts
aligned even before the core skill loads:

```
Process Engine context (applies to sessions on the Process Engine project):
- Collect before creating: invite the user's material (links, text, files,
  docs); nothing is rejected by type.
- Ask what "good" looks like; form the objective and desired outcomes from
  the vision.
- Operator is the only gate: nothing ships without operator sign-off.
- Nothing ships untried: trials with evidence precede every ship.
- Adapt, never copy: extract techniques, author original instructions,
  attribute sources.
- Heads-up, not police: surface useful considerations, never obstruct.
```

**Policy ID:** `f0991b6598ad4623a410b45cc7aabf28`

### Advisory judge rule: `process-engine-authoring`

A heuristic rule on the skills tool family (tool=skills, arg=process-engine,
risk=low, recommendation=review, advisory). Produces per-call intent
verdicts as machine-consistent evidence that each gate action matched
the operator's intent. Always advisory — the operator decides.

**Rule ID:** `64b985f99743463a9ddf1a78ded01466`

---

## 4. Judge surface — verified

The judge admin API is live and verified:

- **14** settings (enabled, model, smart_approvals, confidence_threshold, output_guard)
- **36** heuristic rules
- **19** output-guard patterns

Judge model: `deepseek-deepseek-v4-flash`. Smart approvals at confidence
threshold 0.95. Output guard active.

### How Judge serves Process Engine

1. **Trial grading** — verdicts provide machine-consistent evidence per case.
2. **Review-gate evidence** — intent summaries and risk assessments join the
   review checklist as auditable, non-blocking records.
3. **Objective-fidelity check** — the LLM tier scores whether actions serve
   the operator's stated "good" — the intent-alignment test.

All verdicts are advisory. The operator remains the only gate.

---

## 5. Design principles (current)

- **Advisory, never blocking** — judge verdicts inform, never replace operator approval.
- **Reversible** — every governance artifact can be disabled or deleted.
- **Content-only** — the prompt policy carries the engine's stance; it never restricts tools.
