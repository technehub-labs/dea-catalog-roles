# CR-DEA-ROL-18: Tranche Admission — Manufacturing Governance Tier (60 roles)

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (stacked PR)

## 1. Objective

Materialize the manufacturing slice's governance tier as candidate entities (60
roles, function families: Auditor + Compliance Officer). Bounded batch via the CR-DEA-ROL-05
pipeline; per-role canonical admission still requires evidence per
GOVERNANCE.md §4.

## 2. Change

- 60 entity files under `entities/v1-alpha/`
- `CATALOG.yaml`: cumulative entity count
- `ingestion/manifest.yaml`: collision count updated with rationale
  (gate-enforced)

## 3. Verification

- `python3 scripts/validate_ingestion.py` — OK
- `python3 scripts/validate_entities.py` — PASS
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures

## 4. Distinctness

Per-domain roles; enterprise-level boundaries per prior cluster sweeps
(compliance/assurance, operations) apply unchanged. Intra-batch
uniqueness enforced by the ingestion gate.
