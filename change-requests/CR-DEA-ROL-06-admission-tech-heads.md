# CR-DEA-ROL-06: Batch Admission — Technology Head-of Leadership (30 roles)

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Materialize the technology slice's Head-of leadership tier as candidate
entities: 30 roles, one per operating-model domain (API Management through
Technology Risk), all `seniority:Executive:6`, class `leadership`. First
bounded batch admission exercising the CR-DEA-ROL-05 pipeline end to end.

## 2. Selection rationale

- **Bounded:** one slice, one function family (`Head of`), one class —
  exactly the shape the materializer's bounded-admission rule exists for.
- **Consistent:** a uniform tier (domain leadership), so the batch reads as
  a coherent governance unit rather than a grab-bag.
- **Candidates, not canonical:** these materialize at `lifecycle_status:
  proposed`, E1, unverified — per CR-ROL-RICH-000 §6 admission path.
  Canonical admission (E5) still requires per-role evidence and review;
  this batch is the *materialization* step, not canonical admission.

## 3. Change

- 30 entity files under `entities/v1-alpha/head-of-*.yaml`
- `CATALOG.yaml`: 37 → 67 entities
- `ingestion/manifest.yaml`: collision count 10 → 40, with rationale
  (the integrity gate requires the count to be explained)

## 4. Verification

- `python3 scripts/validate_ingestion.py` — OK (gate re-verified after
  manifest update)
- `python3 scripts/validate_entities.py` — 67/67 PASS
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures expected
  (skills warn until `dea-catalog-skills` publishes)

## 5. Distinctness note

Head-of roles are per-domain leadership; the pending clusters in
`docs/distinctness-register.md` (design, operations, commercial) do not
cover intra-domain leadership duplication — intra-batch uniqueness is
enforced by the ingestion gate (30 unique domains, verified), and
Domain Owner (already admitted) is cross-domain; per-domain Head-of
roles do not collide with it.
