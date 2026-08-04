# Changelog

All notable changes to Process Engine are recorded here.

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
