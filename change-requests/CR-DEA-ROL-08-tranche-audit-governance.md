# CR-DEA-ROL-08: Tranche Admission — Audit Governance Tier (60 roles) + Cross-Slice Corroboration

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Materialize the audit slice's governance tier (30 domain Auditors + 30
domain Compliance Officers) and record the cross-slice corroboration this
creates with the technology governance tier (CR-DEA-ROL-07): the domain
Auditor and domain Compliance Officer function families now recur across
two independent industries, evidencing E2-track corroboration at family
level.

## 2. Corroboration analysis

| Function family | Technology slice | Audit slice | Corroboration |
|---|---|---|---|
| domain Auditor | 30 instances | 30 instances | Family recurs across two independent industries (technology, audit & assurance) — E2-track at family level |
| domain Compliance Officer | 30 instances | 30 instances | Same — E2-track at family level |

Per EVIDENCE.md, ratings attach to role instances, not families; each
instance remains E1 until its own recurrence is argued. The family-level
corroboration recorded here is the evidence base future per-role
admissions cite. Domain sets are disjoint (technology domains vs
assurance domains), so no id collisions (verified: 0).

## 3. Change

- 60 entity files under `entities/v1-alpha/` (audit-slice governance tier)
- `CATALOG.yaml`: 127 → 187 entities
- `ingestion/manifest.yaml`: collision count 100 → 160, rationale
  recorded (gate-enforced)

## 4. Verification

- `python3 scripts/validate_ingestion.py` — OK
- `python3 scripts/validate_entities.py` — 187/187 PASS
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures expected

## 5. Distinctness note

Audit-slice domains are assurance-specific (Assurance Analytics, Audit
Methodology, …); no overlap with technology domains. Enterprise-level
Internal Auditor / Regulatory Compliance Manager boundaries per
CR-DEA-ROL-07 §5 apply unchanged.
