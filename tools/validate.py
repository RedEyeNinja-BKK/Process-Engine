#!/usr/bin/env python3
"""Process Engine structural repository validation.

Validates the checked-in repository structure against its release metadata
(process-engine.toml) and the Agent Skills spec. Fails on any of:

    - version / lineage mismatch across surfaces
    - missing / extra references, templates, skills
    - embedded core references differing from root references
    - invalid or unsupported frontmatter
    - broken Markdown links
    - documentation component counts
    - stale version references

This is a repository maintenance utility used by CI and maintainers. It is
NOT part of the Process Engine runtime — the engine is prompts only; nothing
in this repository executes when the engine runs.

A successful result means only: the committed repository structure is
internally consistent. It is NOT evidence of behavioral quality, trial
PASS, release approval, or deployment approval. Turnstone provides
runtime/governance; behavioral trials establish product behavior; the
operator approves merge/release/deployment.

Usage:
    python3 tools/validate.py [--repo DIR]

Exit 0 = structural validation PASS. Non-zero = structural validation failed.
"""

import argparse
import glob
import os
import re
import sys

FAILURES = []


def fail(msg):
    FAILURES.append(msg)
    print(f"  FAIL  {msg}")


def ok(msg):
    print(f"  ok    {msg}")


def note(msg):
    print(f"  note  {msg}")


def load_manifest(repo):
    cfg = {}
    with open(os.path.join(repo, "process-engine.toml")) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                cfg[k.strip()] = v.strip().strip('"')
    return cfg


def walk_md_links(text, base_dir):
    """Return (target, anchor) pairs from markdown links, relative to base_dir."""
    out = []
    for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = m.group(1)
        if target.startswith("http") or target.startswith("#"):
            continue
        parts = target.split("#", 1)
        path, anchor = parts[0], (parts[1] if len(parts) > 1 else "")
        out.append((path, anchor))
    return out


def check_evidence_links(repo):
    """Every markdown link inside the repo must resolve to an existing file."""
    bad = []
    for path in glob.glob(os.path.join(repo, "**/*.md"), recursive=True):
        rel = os.path.relpath(path, repo)
        text = open(path).read()
        base = os.path.dirname(path)
        for target, anchor in walk_md_links(text, base):
            resolved = os.path.normpath(os.path.join(base, target))
            if not os.path.exists(resolved):
                bad.append(f"{rel} -> {target} (missing)")
            elif anchor:
                # check anchor exists in target (heading anchors only)
                ttext = open(resolved).read()
                # GitHub-style anchors: lowercase, spaces->-, strip punctuation
                want = anchor.lower().replace(" ", "-")
                heading_match = False
                for hm in re.finditer(r"^#{1,6}\s+(.+)$", ttext, re.M):
                    slug = hm.group(1).lower().strip()
                    slug = re.sub(r"[^\w\- ]", "", slug).replace(" ", "-")
                    if slug == want:
                        heading_match = True
                        break
                if not heading_match:
                    bad.append(f"{rel} -> {target}#{anchor} (no anchor)")
    for b in bad:
        fail(f"broken link: {b}")
    if not bad:
        ok("all markdown links resolve")


def check_frontmatter(repo):
    """Skill frontmatter: allowed fields, required fields, name rules."""
    allowed = {"name", "description", "compatibility", "metadata", "license", "allowed-tools", "version"}
    try:
        import yaml
    except Exception:
        fail("PyYAML required")
        return
    for skill_dir in glob.glob(os.path.join(repo, "skills/*/")):
        smd = os.path.join(skill_dir, "SKILL.md")
        if not os.path.isfile(smd):
            fail(f"missing SKILL.md in {os.path.basename(skill_dir)}")
            continue
        name = os.path.basename(skill_dir.rstrip("/"))
        text = open(smd).read()
        if not text.startswith("---"):
            fail(f"{name}: missing frontmatter")
            continue
        try:
            fm = yaml.safe_load(text.split("---", 2)[1])
        except Exception as e:
            fail(f"{name}: frontmatter parse error: {e}")
            continue
        for k in fm:
            if k not in allowed:
                fail(f"{name}: unsupported frontmatter field {k!r}")
        if fm.get("name") != name:
            fail(f"{name}: frontmatter name {fm.get('name')!r} != dir name")
        if not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", name):
            fail(f"{name}: name fails lowercase-hyphen rule")
        desc = fm.get("description", "")
        if not desc:
            fail(f"{name}: missing description")
        elif len(desc) > 1024:
            fail(f"{name}: description > 1024")
        # Required body sections
        for sec in ["## Overview", "## When to Use", "## Core Process", "## Common Rationalizations", "## Red Flags", "## Verification"]:
            if sec not in text:
                fail(f"{name}: missing required section {sec}")
    ok("skill frontmatter + required sections valid")


def check_embedded_refs(repo, refs):
    """Core's embedded references must byte-match root references."""
    for r in refs:
        root = os.path.join(repo, "references", f"{r}.md")
        emb = os.path.join(repo, "skills", "process-engine-core", "references", f"{r}.md")
        if not os.path.isfile(root):
            fail(f"reference {r}: root missing")
            continue
        if not os.path.isfile(emb):
            fail(f"reference {r}: embedded copy missing in core")
            continue
        if open(root).read() != open(emb).read():
            fail(f"reference {r}: embedded copy differs from root")
    ok("embedded core references == root references")


def check_counts(repo, manifest):
    skills = [d for d in os.listdir(os.path.join(repo, "skills")) if os.path.isdir(os.path.join(repo, "skills", d))]
    refs = [f[:-3] for f in os.listdir(os.path.join(repo, "references")) if f.endswith(".md")]
    tmpls = [f[:-3] for f in os.listdir(os.path.join(repo, "templates")) if f.endswith(".md")]

    sk = int(manifest.get("skill_count", 0))
    rf = int(manifest.get("reference_count", 0))
    tm = int(manifest.get("template_count", 0))

    if len(skills) != sk:
        fail(f"skill count {len(skills)} != manifest {sk}")
    if len(refs) != rf:
        fail(f"reference count {len(refs)} != manifest {rf}")
    if len(tmpls) != tm:
        fail(f"template count {len(tmpls)} != manifest {tm}")
    ok(f"counts match: {sk} skills / {rf} refs / {tm} templates")


def check_doc_counts(repo, manifest):
    """docs/architecture.md component counts match manifest."""
    arch = open(os.path.join(repo, "docs", "architecture.md")).read()
    if str(manifest.get("skill_count")) not in re.findall(r"six skills", arch):
        # architecture says 'six skills'; if counts differ, flag
        if "six skills" in arch and manifest.get("skill_count") != "6":
            fail("architecture.md still says 'six skills'")
        else:
            ok("architecture.md component wording present")
    if "seven references" in arch and manifest.get("reference_count") != "7":
        fail("architecture.md still says 'seven references'")
    ok("docs/architecture.md component counts consistent")


def check_version_sweep(repo, manifest):
    version = manifest.get("version")
    lineage = manifest.get("lineage")
    # Generic semantic version: flag any 1.x/2.x version that differs from the
    # canonical manifest outside historical changelog contexts.
    ver_re = re.compile(r"\bv?\d+\.\d+\.\d+\b")
    bad = []
    for path in glob.glob(os.path.join(repo, "**/*"), recursive=True):
        if not os.path.isfile(path) or "/runs/" in path or "/.git/" in path:
            continue
        rel = os.path.relpath(path, repo)
        if rel.startswith("tools/") or rel == "process-engine.toml":
            continue
        if rel in {"README.md", "CHANGELOG.md"}:
            continue  # prose docs; README links to the successor, CHANGELOG records release history
        ext = os.path.splitext(rel)[1]
        if ext not in (".md", ".json", ".toml", ".yaml"):
            continue
        text = open(path).read()
        for m in ver_re.finditer(text):
            cand = m.group(0).lstrip("v")
            # Ignore compatibility strings that name OTHER versions legitimately
            # (e.g. "Turnstone 1.8.x" is fine; only flag a bare semver mismatch)
            if cand == version:
                continue
            # A prior-version token is valid when it names preserved historical
            # evidence or a concrete historical release-bundle path.
            line_start = text.rfind("\n", 0, m.start()) + 1
            line_end = text.find("\n", m.end())
            line = text[line_start:None if line_end < 0 else line_end].lower()
            if "historical" in line or "historic" in line or "release-v1.8.0" in line:
                continue
            bad.append(f"{rel}: version {m.group(0)} != canonical {version}")
    for b in bad:
        fail(b)
    if not bad:
        ok(f"no stale version references (canonical {version})")
    ok(f"lineage {lineage} set in manifest")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=None)
    args = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.abspath(args.repo) if args.repo else os.path.dirname(here)
    manifest = load_manifest(repo)

    print(f"Process Engine structural repository validation — v{manifest.get('version')} (lineage {manifest.get('lineage')})")
    print(f"repo: {repo}\n")

    check_counts(repo, manifest)
    check_doc_counts(repo, manifest)
    check_frontmatter(repo)
    check_embedded_refs(repo, ["standards", "safety", "evidence-library", "skill-anatomy", "best-practices", "intake", "governance"])
    check_evidence_links(repo)
    check_version_sweep(repo, manifest)

    if FAILURES:
        print(f"\nSTRUCTURAL VALIDATION FAILED: {len(FAILURES)} problem(s)")
        sys.exit(1)
    print("\nSTRUCTURAL VALIDATION PASS — committed repository structure is internally consistent.")


if __name__ == "__main__":
    main()
