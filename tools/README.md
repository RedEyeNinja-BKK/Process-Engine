# tools/ — Repository maintenance utilities

These are **maintenance tools used by CI and maintainers only**. They are not
part of the Process Engine runtime — the engine itself is **prompts only**.
Nothing in this directory executes when the engine runs; Turnstone's native
governance (prompt policy, advisory judge) is the enforcement layer.

| Tool | Purpose |
|---|---|
| `validate.py` | Structural release gate (CI + local): manifest version/lineage, skill/reference/template counts, frontmatter validity, link resolution, stale-version sweep, regeneration drift. |
| `convert.py` | Content sync: regenerates `skills/`, `references/`, `templates/`, `persona.md` from the authoring drafts directory (the same source deployed to the Turnstone store). |

Both tools read `process-engine.toml` as the canonical release manifest and
are wired into `.github/workflows/release-gate.yml`. They are intentionally
small and structural — Process Engine generates packages; it does not ship
code.
