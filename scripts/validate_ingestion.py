#!/usr/bin/env python3
"""Validate the bulk ingestion source against schema and catalog invariants.

Gates (CR-ROL-RICH-000 pipeline):
  1. Manifest integrity — CSV sha256 matches the manifest.
  2. Row schema — every row satisfies role.schema.json constraints
     (id pattern, type const, name/description lengths, semver,
     lifecycle enum) and relationship-instance constraints
     (relationship_type in vocabulary, target id patterns).
  3. Internal uniqueness — no duplicate ids, no duplicate
     relationship ids.
  4. Slice shape — 12 slices, 500 rows each, industry ids match the
     registered slice list.
  5. Collision policy — ids already materialized in entities/ are
     counted and reported; existing instances win, bulk rows for them
     are skipped at materialization (never overwritten).
  6. Taxonomy — role_class in the five TAXONOMY.md primary classes.
"""

import csv
import hashlib
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
INGEST = ROOT / "ingestion"

ID_PAT = re.compile(r"^[a-z][a-z0-9-]*:[a-z0-9-]+$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
SKILL_PAT = re.compile(r"^skills:skill-[a-z0-9-]+$")
CLASSES = {"leadership", "governance", "functional", "technical", "enablement"}
EXPECTED_SLICES = {
    "technology", "entertainment", "media", "finance", "mining",
    "transport", "manufacturing", "healthcare", "audit",
    "legal-regulatory", "consulting", "telecom",
}
REL_TYPES_ALLOWED = {"requires"}


def fail(msg: str, failures: list):
    failures.append(msg)
    print(f"FAIL {msg}")


def main() -> int:
    failures: list = []

    manifest_path = INGEST / "manifest.yaml"
    csv_path = INGEST / "bulk-6000-roles.csv"
    if not manifest_path.is_file() or not csv_path.is_file():
        sys.exit("ingestion source or manifest missing")

    manifest = yaml.safe_load(manifest_path.read_text())

    # 1. manifest integrity
    digest = hashlib.sha256(csv_path.read_bytes()).hexdigest()
    if digest != manifest.get("sha256"):
        fail(f"sha256 mismatch: manifest={manifest.get('sha256')} actual={digest}", failures)

    # existing entity ids (collision policy)
    existing_ids = set()
    for f in (ROOT / "entities").rglob("*.yaml"):
        data = yaml.safe_load(f.read_text())
        if isinstance(data, dict) and data.get("id"):
            existing_ids.add(data["id"])

    # 2-6. row validation
    seen_ids = {}
    seen_rel_ids = {}
    slice_counts = {}
    collisions = []
    n = 0
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            n += 1
            rid = row["id"]
            if not ID_PAT.match(rid):
                fail(f"row {n}: bad id {rid!r}", failures)
            if rid in seen_ids:
                fail(f"row {n}: duplicate id {rid} (first at row {seen_ids[rid]})", failures)
            seen_ids[rid] = n
            if row["type"] != "Role":
                fail(f"row {n} [{rid}]: type must be 'Role'", failures)
            if not (1 <= len(row["name"]) <= 200):
                fail(f"row {n} [{rid}]: name length out of range", failures)
            if len(row["description"] or "") > 2000:
                fail(f"row {n} [{rid}]: description > 2000 chars", failures)
            if not SEMVER.match(row["version"]):
                fail(f"row {n} [{rid}]: bad semver {row['version']!r}", failures)
            if row["lifecycle_status"] != "proposed":
                fail(f"row {n} [{rid}]: bulk rows must be proposed", failures)
            if row["role_class"] not in CLASSES:
                fail(f"row {n} [{rid}]: unknown role_class {row['role_class']!r}", failures)
            if row["industries"] not in EXPECTED_SLICES:
                fail(f"row {n} [{rid}]: unregistered slice {row['industries']!r}", failures)
            slice_counts[row["industries"]] = slice_counts.get(row["industries"], 0) + 1
            relid = row["relationship_id"]
            if not ID_PAT.match(relid):
                fail(f"row {n} [{rid}]: bad relationship id {relid!r}", failures)
            if relid in seen_rel_ids:
                fail(f"row {n} [{rid}]: duplicate relationship id {relid}", failures)
            seen_rel_ids[relid] = n
            if row["relationship_type"] not in REL_TYPES_ALLOWED:
                fail(f"row {n} [{rid}]: relationship_type {row['relationship_type']!r} not allowed", failures)
            if not SKILL_PAT.match(row["relationship_target_id"]):
                fail(f"row {n} [{rid}]: bad primary skill id {row['relationship_target_id']!r}", failures)
            if row["secondary_skill_id"] and not SKILL_PAT.match(row["secondary_skill_id"]):
                fail(f"row {n} [{rid}]: bad secondary skill id {row['secondary_skill_id']!r}", failures)
            if rid in existing_ids:
                collisions.append(rid)

    if n != manifest.get("rows"):
        fail(f"row count {n} != manifest rows {manifest.get('rows')}", failures)

    # 4. slice shape
    for sl in EXPECTED_SLICES:
        c = slice_counts.get(sl, 0)
        if c != 500:
            fail(f"slice {sl}: expected 500 rows, found {c}", failures)
    extra = set(slice_counts) - EXPECTED_SLICES
    for sl in extra:
        fail(f"unexpected slice {sl}", failures)

    if len(collisions) != manifest.get("collisions_with_existing", len(collisions)):
        fail(
            f"collision count changed: manifest={manifest.get('collisions_with_existing')} actual={len(collisions)}",
            failures,
        )

    print(f"rows: {n}; slices: {len(slice_counts)}; unique ids: {len(seen_ids)}")
    print(f"collisions with existing entities: {len(collisions)} (existing win; skipped at materialization)")
    for c in sorted(collisions):
        print(f"  skip: {c}")

    if failures:
        sys.exit(f"{len(failures)} ingestion validation failure(s)")
    print("ingestion validation OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
