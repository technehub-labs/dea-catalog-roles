# CR-DEA-ROL-09: Tranche Admission — Legal & Regulatory Governance Tier (60 roles)

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Materialize the legal-regulatory slice's governance tier (30 domain
Auditors + 30 domain Compliance Officers) and extend the cross-slice
corroboration: both function families now recur across three independent
industries (technology, audit, legal & regulatory).

## 2. Corroboration analysis

| Function family | Technology | Audit | Legal & Regulatory | Corroboration |
|---|---|---|---|---|
| domain Auditor | 30 | 30 | 30 | Three independent industries — E3-track at family level |
| domain Compliance Officer | 30 | 30 | 30 | Three independent industries — E3-track at family level |

Per EVIDENCE.md, ratings attach per instance (all remain E1,
proposed/unverified). The three-industry family recurrence recorded here
is the evidence base for future systematic per-role admissions, and the
first family-level E3-track (enterprise-generality) argument in the batch.

Domain sets are disjoint across slices (technology domains, assurance
domains, legal/regulatory domains); 0 id collisions (verified).

## 3. Change

- 60 entity files under `entities/v1-alpha/` (legal-regulatory governance)
- `CATALOG.yaml`: 187 → 247 entities
- `ingestion/manifest.yaml`: collision count 160 → 220, rationale
  recorded (gate-enforced)

## 4. Verification

- `python3 scripts/validate_ingestion.py` — OK
- `python3 scripts/validate_entities.py` — 247/247 PASS
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures

## 5. Distinctness note

Legal-regulatory domains are statute-specific (Administrative Justice,
Competition Law, Consumer Protection, …); no overlap with technology or
assurance domains. Enterprise-level Internal Auditor / Regulatory
Compliance Manager boundaries per CR-DEA-ROL-07 §5 apply unchanged.
