# CR-DEA-ROL-05: Bulk Ingestion Pipeline (6000 candidate roles, 12 slices)

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)
**Source spec:** CR-ROL-RICH-000 (uploaded ingestion batch)

## 1. Objective

Land the 6000-role bulk ingestion batch as a **governed pipeline**, not a
bulk dump: a canonical checked-in source, integrity gates in CI, a
materialization tool bound to the admission path, and doc extensions per
the source spec.

## 2. Deliverables

| # | Deliverable | Path |
|---|---|---|
| 1 | Canonical ingestion source (6000 rows, Roles sheet of the workbook) | `ingestion/bulk-6000-roles.csv` |
| 2 | Integrity manifest (sha256, counts, collision policy) | `ingestion/manifest.yaml` |
| 3 | Validation gate: manifest integrity, row schema, uniqueness, slice shape, taxonomy, collision policy | `scripts/validate_ingestion.py` + `.github/workflows/validate-ingestion.yml` |
| 4 | Materializer bound to the admission path (CR-ROL-RICH-000 §6; existing instances win; bounded slices only) | `scripts/materialize_roles.py` |
| 5 | Pilot admission: 3 technology-slice roles materialized | `entities/v1-alpha/{api-management,application-portfolio,automation-rpa}-administrator.yaml` |
| 6 | Demand list: full batch skill demand (359 primary + 359 secondary) | `industries/bulk-6000-demand.md` |
| 7 | Doc extensions: catalog scale, 12-slice register, taxonomy counts, seniority vocabulary, rich facets | `README.md` / `INDUSTRIES.md` / `TAXONOMY.md` |
| 8 | Slice registers: 12 `industries/<id>.yaml` (incl. `finance` superseding note re `banking`) | `industries/` |

## 3. Gate semantics (robustness)

- **Manifest integrity:** CSV sha256 must match the manifest; any silent
  edit to the source fails CI. Verified by tamper test.
- **Row schema:** id pattern, type const, name/description limits, semver,
  proposed-only lifecycle, registered slice ids, allowed relationship
  types, skill id patterns — per the workbook's own Schema Guide sheet.
  All 6000 rows pass with zero defects.
- **Uniqueness:** 6000 unique ids, 6000 unique relationship ids.
- **Slice shape:** 12 slices × exactly 500.
- **Collision policy:** 7 bulk ids collide with materialized instances
  (credit-risk-manager, clinical-governance-lead, financial-crime-compliance-manager,
  network-planning-engineer, patient-experience-manager, procurement-manager,
  service-assurance-manager). Existing instances win — they carry richer
  evidence trails; the materializer refuses to overwrite and the gate
  verifies the collision count.
- **Bounded admission:** `--slice` requires `--limit`; whole-slice
  admission must never be a default.

## 4. Admission path (unchanged governance)

Bulk rows remain candidates (proposed, unverified, catalog-seed). Admission
proceeds per GOVERNANCE.md/EVIDENCE.md by CR with evidence; on admission,
rows materialize via the tool and skill references must resolve against the
published `dea-catalog-skills` list. Nothing in this CR admits the batch.

## 5. Verification

- `python3 scripts/validate_ingestion.py` — 6000 rows OK, 7 collisions as
  manifest-declared, tamper test FAILs correctly
- `python3 scripts/validate_entities.py` — 37/37 PASS (34 + 3 pilots)
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures, 40 warnings
  (skills catalog unpublished)
- CI: new `validate-ingestion.yml` runs the gate on every push/PR
