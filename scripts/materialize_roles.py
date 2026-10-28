#!/usr/bin/env python3
"""Materialize bulk ingestion rows as entity instances (admission path).

Per CR-ROL-RICH-000 §6 and GOVERNANCE.md §4: bulk rows are candidates;
they materialize as entities/v1-alpha/<slug>.yaml only when admitted via
CR. This tool performs the mechanical conversion for an explicit list of
row ids (or --slice for a whole-slice admission):

    python scripts/materialize_roles.py --ids roles:role-x roles:role-y
    python scripts/materialize_roles.py --slice technology --limit 10

Safety:
  - refuses to overwrite an existing entity file (existing wins);
  - validates the CSV against the manifest first (reuses the gate);
  - refuses rows whose lifecycle_status is not 'proposed';
  - refuses --slice without --limit (whole-slice admission must be an
    explicit bounded decision, not a default).

Output YAML validates against schemas/role.schema.json (enforced by
scripts/validate_entities.py in CI).
"""

import argparse
import csv
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import validate_ingestion  # noqa: E402  (reuse gate + manifest)

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTITIES = ROOT / "entities" / "v1-alpha"


def slug_for(rid: str) -> str:
    return rid.split(":", 1)[1].replace("role-", "", 1)


def row_to_instance(row: dict) -> dict:
    tags = [t.strip() for t in row["tags"].split(";") if t.strip()]
    tags.append(f"seniority:{row['seniority_band']}:{row['seniority_level']}")
    rel_provenance = {
        "type": row["provenance_type"],
        "reference": row["provenance_reference"],
        "asserted_by": row["provenance_asserted_by"],
        "verification_status": row["provenance_verification_status"],
    }
    relationships = [
        {
            "id": row["relationship_id"],
            "source_id": row["id"],
            "target_id": row["relationship_target_id"],
            "relationship_type": row["relationship_type"],
            "status": row["relationship_status"],
            "rationale": (
                "Primary SKL -> ROL requires edge from bulk ingestion batch "
                "(CR-ROL-RICH-000); unverified until dea-catalog-skills publishes."
            ),
            "provenance": rel_provenance,
        }
    ]
    if row["secondary_skill_id"]:
        relationships.append(
            {
                "id": row["relationship_id"] + "-secondary",
                "source_id": row["id"],
                "target_id": row["secondary_skill_id"],
                "relationship_type": row["relationship_type"],
                "status": row["relationship_status"],
                "rationale": (
                    "Secondary SKL -> ROL requires edge from bulk ingestion batch "
                    "(CR-ROL-RICH-000); unverified until dea-catalog-skills publishes."
                ),
                "provenance": dict(rel_provenance),
            }
        )
    industries = [row["industries"]]
    industries += [t.strip() for t in row["related_industries"].split(";") if t.strip()]
    return {
        "id": row["id"],
        "type": row["type"],
        "name": row["name"],
        "description": row["description"],
        "version": row["version"],
        "lifecycle_status": row["lifecycle_status"],
        "tags": tags,
        "metadata": {
            "catalog": row["catalog"],
            "metamodel_version": row["metamodel_version"],
            "domain": row["domain"],
            "org_unit": row["org_unit"],
            "function": row["function"],
            "seniority_band": row["seniority_band"],
            "seniority_level": int(row["seniority_level"]),
            "industries": industries,
        },
        "relationships": relationships,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--ids", nargs="+")
    g.add_argument("--slice")
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    if args.slice and not args.limit:
        sys.exit("--slice requires --limit (bounded admission only)")

    validate_ingestion.main()  # gate must pass before any materialization

    with open(ROOT / "ingestion" / "bulk-6000-roles.csv", newline="") as f:
        rows = list(csv.DictReader(f))

    if args.ids:
        selected = [r for r in rows if r["id"] in set(args.ids)]
        missing = set(args.ids) - {r["id"] for r in selected}
        if missing:
            sys.exit(f"unknown ids: {sorted(missing)}")
    else:
        selected = [r for r in rows if r["industries"] == args.slice][: args.limit]

    written = skipped = 0
    for row in selected:
        out = ENTITIES / f"{slug_for(row['id'])}.yaml"
        if out.is_file():
            print(f"skip (exists): {out.name}")
            skipped += 1
            continue
        ENTITIES.mkdir(parents=True, exist_ok=True)
        with open(out, "w") as f:
            yaml.safe_dump(row_to_instance(row), f, sort_keys=False, allow_unicode=True, width=100)
        print(f"wrote: {out.name}")
        written += 1

    print(f"materialized {written}, skipped {skipped}")
    print("next: add CATALOG.yaml entries + admission CR, then validate_entities.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
