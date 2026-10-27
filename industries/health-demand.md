# Health Slice — Skills Demand List

Per [INDUSTRIES.md](../INDUSTRIES.md). Consolidated demand signal to
`dea-catalog-skills` from the health discovery pass 1.

## New skill demand from this slice

| Skill (proposed name) | id | Required by role |
|---|---|---|
| Clinical Governance | `skills:skill-clinical-governance` | `roles:role-clinical-governance-lead` |
| Health Information Management | `skills:skill-health-information-management` | `roles:role-health-information-manager` |
| Claims Management | `skills:skill-claims-management` | `roles:role-claims-operations-manager` |
| Clinical Informatics | `skills:skill-clinical-informatics` | `roles:role-clinical-informaticist` |
| Experience Management | `skills:skill-experience-management` | `roles:role-patient-experience-manager` |
| Program Management | `skills:skill-program-management` | `roles:role-population-health-program-manager` |

## Evidence-rating movement from this pass

| Role | Before | After | Reason |
|---|---|---|---|
| Regulatory Compliance Manager | E2 | **E3 (pending review)** | Three independent regulated industries (telecom, banking, health); enterprise-generality argued for regulated enterprises |
| Internal Auditor | E1 (banking) | **E2** | Corroborated by health pass: two independent industries |
| Patient Experience Manager | E1 (health) | E1 (tracked toward E2) | Generalizes to customer-experience roles; next industry pass corroborates |
| Population Health Program Manager | E1 (health) | E1 (tracked toward E2) | Program management recurs enterprise-wide |
| Claims Operations Manager | E1 (health) | E1 (tracked toward E2) | Claims processing recurs across insurance-adjacent industries |

## Cumulative demand (22 prior + 6 new = 28)

Prior lists: [telecom](telecom-demand.md) · [banking](banking-demand.md).

## Notes

- Health Information Manager is adjacent to Data Architect but accountable
  for records governance (privacy, consent, release-of-information), not
  data architecture; the E4 distinctness sweep tests this boundary.
- Clinical sources evidence recurring health responsibilities; regulatory
  guidance corroborates stance only (EVIDENCE.md §2).
