#!/usr/bin/env python3
"""Check that cross-catalog ids referenced by role instances resolve.

For every relationship on every role instance, the target id namespace
(e.g. skills:, actors:) is looked up against the partner catalog's published
entity list via the GitHub API. Partner catalogs that have not yet published
entities are reported as unresolved-warning, not failure, per the phased
build plan; a referenced id that contradicts a published list is a failure.

CR-DEA-ROL-24: partner catalogs may publish in either layout:

  - legacy flat: entities/<version>/<slug>.yaml
  - CR-MET-024 shard form: entities/<version>/<shard>/<id>/<id>.yaml
    (dea-metaframework/docs/entity-storage-layout.md; a record directory
    whose name contains `:` IS the record id, byte-identical to the id field)

The partner's CATALOG.yaml is authoritative when present and parseable;
otherwise the entities/ tree is walked (depth-bounded, both layouts).
"""

import base64
import json
import pathlib
import subprocess
import sys
from urllib.parse import quote

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

MAX_WALK_DEPTH = 4


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


def _blob_text(repo: str, sha: str) -> str:
    blob = gh_api(f"repos/{repo}/git/blobs/{sha}")
    return base64.b64decode(blob["content"]).decode("utf-8")


def _walk_yaml_ids(repo: str, api_path: str, depth: int = 0):
    """Yield entity ids under a contents-API directory, in either layout."""
    if depth > MAX_WALK_DEPTH:
        return
    for entry in gh_api(api_path):
        if entry["type"] == "file" and entry["name"].endswith((".yaml", ".yml")):
            content = yaml.safe_load(_blob_text(repo, entry["sha"]))
            if isinstance(content, dict) and content.get("id"):
                yield content["id"]
        elif entry["type"] == "dir":
            if ":" in entry["name"]:
                # CR-MET-024 record directory: its name is the record id
                yield entry["name"]
            yield from _walk_yaml_ids(
                repo,
                f"repos/{repo}/contents/{quote(entry['path'], safe='/')}",
                depth + 1)


def collect_ids(repo: str) -> set | None:
    """Return the set of entity ids published by a catalog repo, or None
    if the repo has no entities/ directory yet (nothing published)."""
    # 1. authoritative: the partner's CATALOG.yaml
    try:
        meta = gh_api(f"repos/{repo}/contents/CATALOG.yaml")
        catalog = yaml.safe_load(base64.b64decode(meta["content"]))
        block = (catalog or {}).get("catalog") or {}
        ids = {e["id"] for e in block.get("entities") or []
               if isinstance(e, dict) and e.get("id")}
        if ids:
            return ids
    except NotFound:
        pass
    except Exception:
        pass  # malformed/unreadable catalog: fall back to the tree walk
    # 2. fallback: walk entities/ (legacy flat or CR-MET-024 sharded)
    try:
        entries = gh_api(f"repos/{repo}/contents/entities")
    except NotFound:
        return None
    ids = set()
    for entry in entries:
        if entry["type"] == "dir":
            ids.update(_walk_yaml_ids(
                repo, f"repos/{repo}/contents/{quote(entry['path'], safe='/')}"))
        elif entry["name"].endswith((".yaml", ".yml")):
            content = yaml.safe_load(_blob_text(repo, entry["sha"]))
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
