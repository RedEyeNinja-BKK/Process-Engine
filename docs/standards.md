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

Turnstone's native prompt policy provides durable contextual guidance and the
advisory judge provides review/trial evidence; neither silently replaces
operator approval. The model generates packages; the operator is the final
gate at summary, review, trial, and ship.

## Evidence

Claims must name their sources. Generated artifacts preserve provenance when
known, use original instructions rather than copied text, and remain subject
to scope limits, review, trial evidence, and operator approval.

## Turnstone-native

Process Engine is **Turnstone only**. It is built for Turnstone, deployed on
Turnstone, and uses Turnstone's native governance surfaces. Nothing in the
engine — and nothing the engine generates — targets any other harness.
Every generated package includes Turnstone governance objects — prompt
policy and advisory judge rules — that provide persistent context and
advisory evidence. The governance layer is a native mechanism, not an
add-on. See [Governance usage](governance-usage.md).
