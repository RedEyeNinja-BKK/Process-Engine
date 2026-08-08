---
name: process-engine-ship
description: Deploy an approved, trialed package via Turnstone's native mechanisms, verify it, and record evidence.
compatibility: Turnstone 1.8.x
metadata:
  author: RedEyeNinja-BKK
  version: "1.9.6"
  engine: process-engine 1.9.6
---
## Overview
Ships only what has PASSED review AND trial — the generated package (project /
persona / skills / templates / governance) as a whole. Deployment is via
Turnstone's native API mechanisms; verification is by read-back. Rollback is
defined before ship.

## When to Use
- Artifact passed review and trial, operator approved ship.

## Core Process
1. **Confirm gates** — review PASS + trial PASS + operator approval. All three
   required before touching anything. Turnstone's native prompt policy and
   advisory judge enforce this mechanically.
2. **Define rollback** — how to undo this deployment (delete the created
   objects / revert content) before deploying.
3. **Deploy the package** via Turnstone's native API:
   - project → POST /v1/api/projects
   - persona → POST /v1/api/admin/personas
   - skills/templates → skills API (prompt_templates store)
   - prompt policy → POST /v1/api/admin/prompt-policies (content-only,
     priority 1, no tool_gate — the package's operating stance)
   - judge rules → POST /v1/api/admin/judge/heuristic-rules (advisory,
     risk=low, recommendation=review — the package's risk posture)
   Governance artifacts are deployed as helper objects: advisory, never
   silent blockers, operator-visible, reversible (disable/delete).
   See references/governance.md.
4. **Verify** — GET each created object back; confirm identity + content.
5. **Record evidence** — what shipped, mechanism, verification result,
   rollback path.

## Examples
- Ship generated package to Turnstone: POST project → POST persona → POST
  skills/templates → POST prompt policy → POST judge rule → GET each back →
  record → done.

## Common Rationalizations
- "It passed review, just create it." → Trial is required too. No trial, no ship.
- "Rollback is easy, skip defining it." → Define it BEFORE the deploy, not after.

## Red Flags
- Shipping without review PASS + trial PASS + operator approval.
- No verification read-back.
- No rollback path.

## Verification
- [ ] Review PASS + trial PASS + operator approval all recorded
- [ ] Rollback path defined before deploy
- [ ] Native objects deployed and read back
- [ ] Governance objects verified (prompt policy + judge rules, advisory, no tool_gate)
- [ ] Evidence recorded (deployment objects, rollback path)
