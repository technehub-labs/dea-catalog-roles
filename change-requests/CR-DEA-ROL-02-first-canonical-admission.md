# CR-DEA-ROL-02: First Canonical Admission — Regulatory Compliance Manager

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Admit `roles:role-regulatory-compliance-manager` as the catalog's first
canonical role (E5), per EVIDENCE.md ratings and GOVERNANCE.md §4 acceptance
recording.

## 2. Evidence trail (EVIDENCE.md §3)

| Stage | Rating | Evidence |
|---|---|---|
| Recurrence | E1 | Telecom pass 1 (2026-10-27): sector-regulation accountability in telco operating model |
| Corroboration | E2 | Banking pass 1 (2026-10-27): prudential/conduct regulation, independent jurisdiction and source class |
| Enterprise-generality | E3 | Health + public-sector passes (2026-10-27): four industries; regulation corroborated from both the regulated and the regulator side |
| Distinctness | E4 | [`docs/distinctness-register.md`](../docs/distinctness-register.md): distinct from Financial Crime Compliance Manager, Data Protection Officer, Internal Auditor, Clinical Governance Lead |
| Review | E5 | This CR: semantic review (definition, taxonomy fit: governance · compliance) and architectural review (relationship correctness: single `requires` edge to `skills:skill-regulatory-compliance`) |

## 3. Change

| Field | Before | After |
|---|---|---|
| `lifecycle_status` (instance) | `proposed` | `active` |
| `version` (instance) | 0.1.0 | 0.2.0 |
| Evidence trail | rating notes in rationale | provenance ladder recorded on the instance |
| `CATALOG.yaml` | lifecycle_status: proposed | active |

No schema, taxonomy, or governance change. Distinctness register added at
`docs/distinctness-register.md` (compliance/assurance, finance, data
clusters swept; pending clusters recorded).

## 4. Acceptance recording (GOVERNANCE.md §4)

1. Schema validation green (CI `entities` job).
2. Cross-catalog check green-or-warned: the `skills:skill-regulatory-compliance` edge remains a warning until `dea-catalog-skills` publishes (tracked in its issue #1); admission is on role evidence, not edge resolution.
3. Both review outcomes recorded in §2 of this CR.
4. Post-merge CI must stay green.

## 5. Verification

- `python3 scripts/validate_entities.py` — 34/34 PASS (with this PR's instance change)
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures
- Distinctness register reviewed as part of this CR
