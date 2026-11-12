# CR-DEA-ROL-24: Shard Layout Migration and Cross-Catalog Checker Update

| Field | Value |
|---|---|
| CR id | CR-DEA-ROL-24 |
| Owner | Emmanuel A. Otchere |
| Author | Emmanuel A. Otchere |
| Status | Proposed |
| Date | 2026-11-12 |
| Scope | dea-catalog-roles (entities/v1-alpha layout, CATALOG.yaml paths, scripts/) |
| Metamodel | dea-metamodel v0.3.0 |
| Related | CR-MET-024 (entity storage layout), CR-DEA-SKL-01 (skills catalog), CR-ROL-RICH-000, CR-DEA-ROL-05 |

## Objective

Bring dea-catalog-roles into the org-wide CR-MET-024 shard layout and make
`scripts/check_cross_catalog_refs.py` able to resolve partner catalogs that
publish in that layout.

## Background

1. **The flat layout is past the shard trigger.** entities/v1-alpha holds
   1,252 record files. GitHub truncates directory listings at 1,000 entries
   and CST-017 fails at 800+ tracked entries
   (dea-metaframework/docs/entity-storage-layout.md v1.2.0, ratified
   2026-11-10). The remedy, ratified as CR-MET-024 and already implemented in
   dea-catalog-metrics, is sharding on the first character of the record
   slug with a `0-9` fallback for digit-leading slugs.
2. **The cross-catalog checker cannot see sharded partners.** `collect_ids`
   in scripts/check_cross_catalog_refs.py walks exactly two levels
   (entities/<dir>/<file>.yaml). A partner catalog publishing in the shard
   form (entities/v1-alpha/<shard>/<id>/<id>.yaml) yields zero ids, so every
   role-side `skills:` reference would warn "no published entities" forever
   once dea-catalog-skills publishes (CR-DEA-SKL-01).

## Deliverables

| Artifact | Path | Notes |
|---|---|---|
| Migration tool | `scripts/migrate_to_shard_layout.py` | Moves 1,252 records to `entities/v1-alpha/<shard>/<id>/<id>.yaml`; record file names become the full record id (metrics reference form); per-record and per-shard READMEs (S2.3); CATALOG.yaml `path:` values rewritten in place, all other bytes preserved; re-runnable; `--dry-run` |
| Checker update | `scripts/check_cross_catalog_refs.py` | Partner ids collected from the partner's CATALOG.yaml when present (authoritative, one API call); otherwise a depth-bounded entities/ walk that handles both the legacy flat layout and the CR-MET-024 shard form (record directories whose names contain `:` are record ids); API paths percent-encoded |
| Materializer update | `scripts/materialize_roles.py` | New admissions write the shard form directly with per-record READMEs; a record still at its legacy flat path counts as existing (existing wins); a `--dry-run` migration is the prerequisite for any new admission |
| This CR | `change-requests/CR-DEA-ROL-24.md` | |

## Layout rule (CR-MET-024)

```
entities/v1-alpha/<shard>/<id>/<id>.yaml
e.g. entities/v1-alpha/e/roles:role-enterprise-architect/roles:role-enterprise-architect.yaml
```

Shard = first character of the record slug (`roles:role-` prefix removed);
`0-9` fallback for digit-leading slugs. The record path stays derivable
from the id alone (entity-storage-layout.md S5); record ids are
byte-identical before and after the move (git detects the renames).

## Gate semantics

The migration is safe by construction:

- id/file-name consistency: every moved record's `id` field must match the
  catalog id (hard error otherwise);
- collision refusal: a flat record and a shard record both existing for one
  id is a hard error;
- re-runnable: already-migrated records are skipped;
- census: the migration prints the worst shard against the 800 trigger.

## Verification

```
python scripts/migrate_to_shard_layout.py --dry-run   # 1252 to move
python scripts/migrate_to_shard_layout.py             # moves + READMEs + CATALOG paths
python scripts/validate_entities.py                   # unchanged gates pass
python scripts/check_cross_catalog_refs.py             # resolves sharded partners
```

Expected post-migration census: 26 letter shards + `0-9`; worst shard well
under the 800-entry trigger.

## Rollout

Single PR moving the records, rewriting CATALOG.yaml paths, and replacing
the two scripts; CI re-runs validate_entities.py over the moved tree
(rglob-based, shard-safe). No role ids, names, or relationship instances
change; the diff is moves plus READMEs plus path values.

## References

- dea-metaframework `docs/entity-storage-layout.md` v1.2.0 (CR-MET-024)
- dea-catalog-metrics `scripts/_catalog.py` (reference shard implementation)
- technehub-labs/dea-catalog-skills CR-DEA-SKL-01 (sharded skills baseline)
