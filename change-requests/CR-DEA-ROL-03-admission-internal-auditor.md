# CR-DEA-ROL-03: Canonical Admission — Internal Auditor

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Admit `roles:role-internal-auditor` as the catalog's second canonical role
(E5), per EVIDENCE.md ratings and GOVERNANCE.md §4 acceptance recording.

## 2. Evidence trail (EVIDENCE.md §3)

| Stage | Rating | Evidence |
|---|---|---|
| Recurrence | E1 | Banking pass 1 (2026-10-27): board-level independent assurance in the banking operating model |
| Corroboration | E2 | Health pass 1 (2026-10-27): clinical-services audit, independent source class |
| Enterprise-generality | E3 | Public-sector pass 1 (2026-10-27): three industries across regulated and publicly-accountable enterprise forms |
| Distinctness | E4 | [`docs/distinctness-register.md`](../docs/distinctness-register.md) compliance/assurance cluster: distinct from Regulatory Compliance Manager (third-line assurance vs second-line control ownership), Data Protection Officer (governance-structural vs statutory independence), Financial Crime Compliance Manager |
| Review | E5 | This CR: semantic review (definition, taxonomy fit: governance · assurance) and architectural review (single `requires` edge to `skills:skill-internal-audit`) |

## 3. Change

| Field | Before | After |
|---|---|---|
| `lifecycle_status` (instance) | `proposed` | `active` |
| `version` (instance) | 0.1.0 | 0.2.0 |
| Evidence trail | rating notes in rationale | provenance ladder recorded on the instance |
| `CATALOG.yaml` | lifecycle_status: proposed; canonical: 1 | lifecycle_status: active; canonical: 2 |

No schema, taxonomy, or governance change.

## 4. Acceptance recording (GOVERNANCE.md §4)

1. Schema validation green (CI `entities` job).
2. Cross-catalog check green-or-warned: the `skills:skill-internal-audit` edge warns until `dea-catalog-skills` publishes (tracked in its issue #1); admission is on role evidence.
3. Both review outcomes recorded in §2.
4. Post-merge CI must stay green.

## 5. Verification

- `python3 scripts/validate_entities.py` — 34/34 PASS (with this PR's instance change)
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures
