# CR-DEA-ROL-04: Canonical Admissions — Patient Experience Manager, Population Health Program Manager

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Admit two roles as canonical (E5), both from the newly swept experience &
program cluster: `roles:role-patient-experience-manager` and
`roles:role-population-health-program-manager`.

## 2. Evidence trail (EVIDENCE.md §3)

### Patient Experience Manager

| Stage | Rating | Evidence |
|---|---|---|
| Recurrence | E1 | Health pass 1 (2026-10-27): patient-experience accountability in health delivery |
| Corroboration | E2 | Public-sector pass 1 (2026-10-27): citizen-services experience management, independent industry and source class |
| Enterprise-generality | E3 | Argument: experience management recurs in every enterprise with service populations (patient/citizen/customer/member); telecom and banking slices carry adjacent CX accountabilities inside their service roles, evidencing the pattern's breadth |
| Distinctness | E4 | `docs/distinctness-register.md` experience & program cluster: distinct from Service Designer (operate vs design), Relationship Manager (aggregate experience vs named-account P&L), Citizen Services Operations Manager (how it feels vs whether it runs) |
| Review | E5 | This CR: semantic review (definition, taxonomy fit: functional · experience) and architectural review (single `requires` edge to `skills:skill-experience-management`) |

### Population Health Program Manager

| Stage | Rating | Evidence |
|---|---|---|
| Recurrence | E1 | Health pass 1 (2026-10-27): population-health program accountability |
| Corroboration | E2 | Public-sector pass 1 (2026-10-27): public program management corroborates the program-management core |
| Enterprise-generality | E3 | Argument: program management recurs enterprise-wide (any temporary, outcome-targeted, multi-workstream initiative); four slices each evidence program-shaped work |
| Distinctness | E4 | `docs/distinctness-register.md`: distinct from Process Owner (temporary program vs standing process), model entity CHI (role manages initiatives, is not one), Product Owner (population outcomes vs product value) |
| Review | E5 | This CR: semantic review (definition, taxonomy fit: functional · program) and architectural review (single `requires` edge to `skills:skill-program-management`) |

## 3. Change

| Field | Before | After |
|---|---|---|
| `lifecycle_status` (both instances) | `proposed` | `active` |
| `version` (both instances) | 0.1.0 | 0.2.0 |
| Evidence trail | rating notes in rationale | provenance ladders recorded on the instances |
| `CATALOG.yaml` | canonical: 2 | canonical: 4 |

Both instances gain explicit `evidence_ladder` metadata. The E3 stage on
these admissions is an argued enterprise-generality case (per EVIDENCE.md
E3 definition: recurrence across industries/sectors evidenced), resting on
the four-slice pattern plus the corroborated second industry; the next
industry slice that registers either role directly converts the argument to
direct multi-industry evidence.

## 4. Acceptance recording (GOVERNANCE.md §4)

1. Schema validation green (CI `entities` job).
2. Cross-catalog check green-or-warned: `skills:skill-experience-management` and `skills:skill-program-management` edges warn until `dea-catalog-skills` publishes; admission is on role evidence.
3. Both review outcomes recorded in §2 per role.
4. Post-merge CI must stay green.

## 5. Verification

- `python3 scripts/validate_entities.py` — 34/34 PASS
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures
