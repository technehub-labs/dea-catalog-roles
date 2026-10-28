# CR-DEA-ROL-07: Batch Admission — Technology Governance Tier (60 roles)

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Materialize the technology slice's governance tier as candidate entities:
60 roles — 30 domain Auditors and 30 domain Compliance Officers across the
30 operating-model domains. Second bounded batch through the CR-DEA-ROL-05
pipeline, completing the technology slice's leadership + governance
accountability layers (90 of 500 technology candidates materialized).

## 2. Selection rationale

Same bounded shape as CR-DEA-ROL-06: one slice, one class (`governance`),
two function families (`Auditor`, `Compliance Officer`) — the tier that
constrains and reviews the technology domains whose leadership landed in
ROL-06. Materialization at `proposed`/E1; per-role canonical admission
still requires evidence per GOVERNANCE.md §4.

## 3. Change

- 60 entity files under `entities/v1-alpha/` (`*-auditor.yaml`,
  `*-compliance-officer.yaml`)
- `CATALOG.yaml`: 67 → 127 entities
- `ingestion/manifest.yaml`: collision count 40 → 100, rationale recorded
  (gate-enforced)

## 4. Verification

- `python3 scripts/validate_ingestion.py` — OK
- `python3 scripts/validate_entities.py` — 127/127 PASS
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures expected

## 5. Distinctness note

Domain Auditor and domain Compliance Officer instances are per-domain
second-line roles; they do not collide with the enterprise-level Internal
Auditor (third-line, independent assurance) or Regulatory Compliance
Manager (sector regulation) already admitted — different scope and line of
defense. Boundary recorded for the next distinctness sweep of the
governance cluster.
