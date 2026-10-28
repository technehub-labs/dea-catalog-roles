# CR-DEA-ROL-10: Tranche Admission — Consulting Governance Tier (60 roles) + Family Recurrence Register

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Two deliverables:

1. Materialize the consulting slice's governance tier (30 domain
   Auditors + 30 domain Compliance Officers) — a fourth industry for both
   governance families.
2. Add `docs/family-recurrence-register.md`: the citable evidence base
   for per-role admissions, recording an honest finding about the batch.

## 2. The honest finding (recorded in the register)

Analysis of the full batch shows domains, primary skill ids, and role
names are **industry-disjoint by construction**: zero instance-level
cross-industry recurrence exists in batch data. Therefore:

- Per-instance E2 **cannot** be claimed from batch data alone; it requires
  a second slice registering the same domain role, or an external source
  (EVIDENCE.md §2).
- What the batch genuinely evidences is **family recurrence**: 17
  function families (class × function) recur across all 12 slices. The
  register records these as E3-track at family level, with usage rules
  for admission CRs (family row + the role's own domain evidence, and an
  explicit industry-generality argument where the domain is generic).

This keeps the evidence method honest (EVIDENCE.md §1: research, not
copy) while still letting the batch power admissions correctly.

## 3. Change

- 60 consulting governance entity files (`entities/v1-alpha/`)
- `docs/family-recurrence-register.md` (new)
- `CATALOG.yaml`: 247 → 307 entities
- `ingestion/manifest.yaml`: collision count 220 → 280, rationale
  recorded (gate-enforced)

## 4. Verification

- `python3 scripts/validate_ingestion.py` — OK
- `python3 scripts/validate_entities.py` — 307/307 PASS
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures expected

## 5. Materialization state after this tranche

| Family | Materialized | Industries |
|---|---|---|
| leadership / Head of | 30 | technology |
| governance / Auditor | 120 | technology, audit, legal-regulatory, consulting |
| governance / Compliance Officer | 120 | technology, audit, legal-regulatory, consulting |
| **Total batch materialized** | **270 of 6000** | 4 slices |
