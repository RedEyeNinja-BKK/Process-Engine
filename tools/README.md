# tools/ — Repository maintenance utilities

These are **maintenance tools used by CI and maintainers only**. They are not
part of the Process Engine runtime — the engine itself is **prompts only**.
Nothing in this directory executes when the engine runs; Turnstone provides
the native governance surfaces (prompt policy as durable contextual guidance,
advisory judge as evidence/recommendation; operator approval remains
authoritative).

| Tool | Purpose |
|---|---|
| `validate.py` | Structural repository validation (CI + local): release/version metadata consistency, skill/reference/template counts, frontmatter validity, root ↔ embedded-reference equality, local Markdown link resolution, stale-version sweep. |

`validate.py` reads `process-engine.toml` as repository release metadata and
is wired into `.github/workflows/release-gate.yml` (display name
`structural-validation`). A successful run means only that the committed
repository structure is internally consistent — it is NOT behavioral proof,
trial PASS, or release/deployment approval.
