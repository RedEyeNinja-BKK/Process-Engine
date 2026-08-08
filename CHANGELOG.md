# Changelog

All notable changes to Process Engine are recorded here.

## 1.9.6 — 2026-08-08

**Prompts-only, Turnstone-native — bounded identity-preservation + repository hygiene** (engine v8.0):

### Changed

- **Identity-critical fact preservation:** intake now preserves material entity ↔ role ↔ identifier/alias relationships, explicitly distinct entities remain distinct, source-attributed identity conflicts remain unresolved until evidence disambiguates them, and genuine ambiguity is preserved.
- **Pattern placement:** mutable operational/contextual identity facts default to package references/resources while stable behavior-defining identity may remain in personas.
- **Review:** wrong-entity/ambiguity checking now produces REVISE when ambiguity could change the target.
- **Trial:** identity-sensitive packages include contradiction/alias/near-match cases.
- **Repository hygiene:** removed obsolete drafts→converter generated-source architecture; GitHub committed content is canonical.
- **Structural validation:** retained small repository structural validation and made GitHub CI genuinely fail closed; structural PASS is explicitly separated from behavioral/release approval.

### Validated

- Canonical repository and live `process-engine-generator` runtime were reconciled and read back before product trials.
- Two live late-invocation trials on the canonical Turnstone runtime passed across materially different domains:
  - technical backup-appliance context;
  - customer/order-record context.
- Across the tested cases, Process Engine successfully reused relevant accumulated workstream context without repeated questions, preserved provenance/corrections/ambiguity, excluded irrelevant chatter, and maintained Summary Gate discipline.
- These trials support the observed behavior in the tested scenarios; they do **not** claim a universal transcript-ingestion guarantee.

### Evidence qualification

The old GitHub workflow previously ran the structural validator with `|| true`, so a green check alone was not proof the validator passed; the tooling-hygiene change corrected this to fail-closed. Historical local structural PASS observations remain valid.

## 1.9.5 — 2026-08-04 (clean slate)

**Prompts-only, Turnstone-native — the engine as a methodology factory** (engine v8.0):

- **Clean slate:** repository history rebuilt as a single root commit on
  2026-08-04. All pre-v1.9.5 tags and GitHub releases were removed. The
  evaluator era (v1.7.0–v1.9.1) is not preserved in this repository; its
  content and evidence remain available in
  [Method Factory](https://github.com/RedEyeNinja-BKK/Method-Factory), the
  prompt+code successor, and in local archives.
- **Prompts only:** the engine runtime is entirely prompts — 6 skills, 7
  references, 6 templates, persona. Nothing in the repository executes when
  the engine runs. `tools/` holds maintenance utilities used by CI and
  maintainers only; Turnstone's native governance (prompt policy, advisory
  judge) is the enforcement layer.
- **Core skill:** rebuilt from the original v1.6.0 essence — pipeline,
  routing, gates. No tier system, no manifest mechanics, no governance canon,
  no first-response discipline section.
- **Sub-skills:** all six reoptimized. Trial is proportionate, not tiered.
  Ship is Turnstone-native deployment only.
- **Artifacts removed:** evaluator scripts, eval-run evidence files, the
  34-case evaluator bundle, portability-testing infrastructure, retired
  schema docs. Only the case study remains
  (`case-study/case-study-first-run.md`).
- **CI:** structural release gate only (`tools/validate.py` + GitHub
  Actions) — version counts, links, frontmatter, regeneration drift.

The engine is a methodology factory again — not an evaluator platform.
Prompts generate packages. Turnstone enforces gates.
