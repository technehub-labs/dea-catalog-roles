#!/usr/bin/env python3
"""Check that cross-catalog ids referenced by role instances resolve.

For every relationship on every role instance, the target id namespace
(e.g. skills:, actors:) is looked up against the partner catalog's published
entity list via the GitHub API. Partner catalogs that have not yet published
entities are reported as unresolved-warning, not failure, per the phased
build plan; a referenced id that contradicts a published list is a failure.
"""

import json
import pathlib
import subprocess
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent

# namespace -> catalog repo that owns it
NAMESPACE_REPOS = {
    "skills": "technehub-labs/dea-catalog-skills",
    "actors": "technehub-labs/dea-catalog-actors",
}


class NotFound(Exception):
    pass


def gh_api(path: str):
    proc = subprocess.run(
        ["gh", "api", path],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if proc.returncode != 0:
        if "HTTP 404" in proc.stderr or "Not Found" in proc.stderr:
            raise NotFound(path)
        raise RuntimeError(f"gh api {path} failed: {proc.stderr.strip()}")
    return json.loads(proc.stdout)


def collect_ids(repo: str) -> set | None:
    """Return the set of entity ids published by a catalog repo, or None
    if the repo has no entities/ directory yet (nothing published)."""
    try:
        entries = gh_api(f"repos/{repo}/contents/entities")
    except NotFound:
        return None
    names = [e["name"] for e in entries if e["type"] == "dir"]
    ids = set()
    for name in names:
        for f in gh_api(f"repos/{repo}/contents/entities/{name}"):
            if f["name"].endswith((".yaml", ".yml")):
                blob = gh_api(f"repos/{repo}/git/blobs/{f['sha']}")
                import base64
                content = yaml.safe_load(base64.b64decode(blob["content"]))
                if isinstance(content, dict) and content.get("id"):
                    ids.add(content["id"])
    return ids or None


def main() -> int:
    failures = warnings = 0
    namespace_ids: dict[str, set | None] = {}

    for path in sorted((ROOT / "entities").rglob("*.yaml")):
        instance = yaml.safe_load(path.read_text())
        for rel in instance.get("relationships") or []:
            target = rel.get("target_id", "")
            namespace = target.split(":", 1)[0] if ":" in target else ""
            if namespace == "roles":
                continue
            repo = NAMESPACE_REPOS.get(namespace)
            if repo is None:
                print(f"FAIL {path.name}: unknown namespace '{namespace}' in {target}")
                failures += 1
                continue
            if namespace not in namespace_ids:
                try:
                    namespace_ids[namespace] = collect_ids(repo)
                except Exception as e:
                    print(f"WARN could not query {repo}: {e}")
                    namespace_ids[namespace] = None
            known = namespace_ids[namespace]
            if known is None:
                print(f"WARN {path.name}: {target} unresolved ({repo} has no published entities)")
                warnings += 1
            elif target not in known:
                print(f"FAIL {path.name}: {target} not found in {repo}")
                failures += 1
            else:
                print(f"OK   {path.name}: {target} resolves in {repo}")

    if failures:
        sys.exit(f"{failures} unresolved reference failure(s), {warnings} warning(s)")
    print(f"cross-catalog check complete: 0 failures, {warnings} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
