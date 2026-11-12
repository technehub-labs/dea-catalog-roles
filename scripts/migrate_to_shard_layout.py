#!/usr/bin/env python3
"""Migrate flat entity records to the CR-MET-024 shard layout (CR-DEA-ROL-24).

GitHub truncates directory listings at 1,000 entries and the org-wide shard
trigger is 800 tracked entries (CST-017; dea-metaframework
docs/entity-storage-layout.md v1.2.0). dea-catalog-roles currently keeps
1,252 records flat in entities/v1-alpha/, past the trigger.

This tool moves every record from

    entities/v1-alpha/<slug>.yaml

to the shard form used by dea-catalog-metrics (the reference
implementation):

    entities/v1-alpha/<shard>/<id>/<id>.yaml

shard = first character of the record slug (`roles:role-` prefix removed;
`0-9` fallback for digit-leading slugs). The record file name becomes the
FULL record id (byte-identical to the record's id field), matching the
metrics layout. Per S2.3 (README-per-folder) each record directory gains a
README.md and each shard directory gains a census README.md.

CATALOG.yaml entity paths are rewritten in place; only the `path:` values
change, the rest of the file is preserved byte-for-byte.

Safe to re-run: already-migrated records are skipped; a flat record and a
shard record both existing for one id is a hard error.

Usage:
    python scripts/migrate_to_shard_layout.py --dry-run
    python scripts/migrate_to_shard_layout.py
"""

import argparse
import collections
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTITIES = ROOT / "entities" / "v1-alpha"
CATALOG = ROOT / "CATALOG.yaml"
SHARD_TRIGGER = 800

ID_LINE = re.compile(r"^( *)- id: (\S+)$")
PATH_LINE = re.compile(r"^( *)path: (\S+)$")


def slug_for(rid: str) -> str:
    return rid.split(":", 1)[1].replace("role-", "", 1)


def shard_for(rid: str) -> str:
    """CR-MET-024 shard directory for a role id."""
    ch = slug_for(rid)[:1]
    return ch if ch.isalpha() and ch.isascii() and ch.islower() else "0-9"


def record_relpath(rid: str) -> str:
    """Id-derived repository-relative path of a record file."""
    return f"entities/v1-alpha/{shard_for(rid)}/{rid}/{rid}.yaml"


def plan():
    """One (id, old_path, new_path, state) tuple per catalog entity."""
    catalog = yaml.safe_load(CATALOG.read_text())
    entities = (catalog.get("catalog") or {}).get("entities") or []
    moves = []
    for e in entities:
        rid, old = e["id"], e["path"]
        new = record_relpath(rid)
        if old == new:
            state = "already-sharded"
        elif (ROOT / old).is_file():
            if (ROOT / new).is_file():
                raise SystemExit(f"collision for {rid}: both {old} and {new} exist")
            state = "move"
        elif (ROOT / new).is_file():
            state = "already-migrated"
        else:
            raise SystemExit(f"missing record for {rid}: neither {old} nor {new}")
        moves.append((rid, old, new, state))
    return moves


def record_readme(rec: dict, relpath: str) -> str:
    return (
        f"# {rec['name']}\n\n"
        f"**Record id:** `{rec['id']}`\n"
        f"**Type:** {rec['type']} | **Lifecycle:** {rec.get('lifecycle_status')} "
        f"(v{rec.get('version')})\n"
        f"**Path:** `{relpath}` (derived from the id; entity-storage-layout.md S5)\n\n"
        f"{rec.get('description', '')}\n\n"
        f"*Moved to the CR-MET-024 shard layout by "
        f"`scripts/migrate_to_shard_layout.py` (CR-DEA-ROL-24). "
        f"Do not edit manually.*\n"
    )


def rewrite_catalog(moves):
    """Rewrite only the path: lines; preserve every other byte."""
    by_id = {rid: new for rid, old, new, state in moves
             if state in ("move", "already-migrated")}
    lines = CATALOG.read_text().splitlines(keepends=True)
    current_id = None
    for i, line in enumerate(lines):
        stripped = line.rstrip("\n")
        m = ID_LINE.match(stripped)
        if m:
            current_id = m.group(2)
            continue
        p = PATH_LINE.match(stripped)
        if p and current_id in by_id:
            lines[i] = f"{p.group(1)}path: {by_id[current_id]}\n"
    CATALOG.write_text("".join(lines))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="print the migration plan without moving anything")
    args = ap.parse_args()

    moves = plan()
    to_move = [m for m in moves if m[3] == "move"]
    n_migrated = sum(1 for m in moves if m[3] == "already-migrated")
    n_sharded = sum(1 for m in moves if m[3] == "already-sharded")
    print(f"{len(moves)} records: {len(to_move)} to move, "
          f"{n_migrated} already migrated, {n_sharded} already sharded")
    if args.dry_run:
        for rid, old, new, state in moves[:10]:
            print(f"  {state}: {old} -> {new}")
        print("  ... (dry run; nothing moved)")
        return 0

    by_shard = collections.defaultdict(list)
    for rid, old, new, state in to_move:
        new_path = ROOT / new
        new_path.parent.mkdir(parents=True, exist_ok=True)
        (ROOT / old).rename(new_path)
        rec = yaml.safe_load(new_path.read_text())
        if rec.get("id") != rid:
            raise SystemExit(
                f"id mismatch: {new} holds {rec.get('id')}, catalog says {rid}")
        (new_path.parent / "README.md").write_text(record_readme(rec, new))
        by_shard[shard_for(rid)].append(rid)

    # per-shard census READMEs (over all records, not just this run's moves)
    shard_counts = collections.Counter(shard_for(rid) for rid, *_ in moves)
    for shard in sorted(shard_counts):
        sdir = ENTITIES / shard
        sdir.mkdir(parents=True, exist_ok=True)
        n = shard_counts[shard]
        (sdir / "README.md").write_text(
            f"# Shard `{shard}`\n\n"
            f"**Records:** {n} (directory entries: {n + 1} incl. this README; "
            f"CST-017 trigger: 800)\n\n"
            f"Roles `{shard}*` per the CR-MET-024 shard rule "
            "(dea-metaframework/docs/entity-storage-layout.md S4).\n\n"
            "*Generated by `scripts/migrate_to_shard_layout.py` "
            "(CR-DEA-ROL-24).*\n")

    rewrite_catalog(moves)
    worst = max(shard_counts.items(), key=lambda kv: kv[1])
    print(f"migration complete; {len(to_move)} records moved; worst shard "
          f"`{worst[0]}` = {worst[1]} records ({worst[1] + 1} entries < "
          f"{SHARD_TRIGGER} trigger)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
