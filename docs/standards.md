# Process Engine standards

This document summarizes the release-facing standards checklist. The canonical
skill reference is [`../references/standards.md`](../references/standards.md).

## Inputs and gates

Every input is assessed and accounted for; it is incorporated or excluded with
a recorded reason. Nothing is rejected by type.

The actual operator gates are:

1. summary confirmation;
2. review approval;
3. trial acceptance; and
4. ship approval.

Nothing ships without operator approval, and trials with evidence precede ship.
A REVISE result returns through diagnose, rewrite, audit, and re-review.

Turnstone's native prompt policy and advisory judge enforce these gates
mechanically. The model generates packages; Turnstone owns the guardrails.

## Evidence

Claims must name their sources. Generated artifacts preserve provenance when
known, use original instructions rather than copied text, and remain subject
to scope limits, review, trial evidence, and operator approval.

## Turnstone-native

Process Engine runs on Turnstone. Every generated package includes Turnstone
governance objects — prompt policy and advisory judge rules — that enforce
the engine's operating stance. The governance layer is the enforcement
mechanism, not an add-on. See [Governance usage](governance-usage.md).
