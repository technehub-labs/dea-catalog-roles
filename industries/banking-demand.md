# Banking Slice — Skills Demand List

Per [INDUSTRIES.md](../INDUSTRIES.md). Consolidated demand signal to
`dea-catalog-skills` from the banking discovery pass 1.

## New skill demand from this slice

| Skill (proposed name) | id | Required by role |
|---|---|---|
| Credit Risk Management | `skills:skill-credit-risk-management` | `roles:role-credit-risk-manager` |
| Financial Crime Compliance | `skills:skill-financial-crime-compliance` | `roles:role-financial-crime-compliance-manager` |
| Payments Operations | `skills:skill-payments-operations` | `roles:role-payments-operations-manager` |
| Treasury Management | `skills:skill-treasury-management` | `roles:role-treasury-manager` |
| Relationship Management | `skills:skill-relationship-management` | `roles:role-relationship-manager` |
| Internal Audit | `skills:skill-internal-audit` | `roles:role-internal-auditor` |

## Evidence-rating movement from this pass

| Role | Before | After | Reason |
|---|---|---|---|
| Regulatory Compliance Manager | E1 (telecom) | **E2** | Corroborated by banking pass: two independent industries |
| Internal Auditor | E1 (banking) | E1 (tracked toward E2) | Recurs across regulated industries; next regulated-industry pass corroborates |
| Relationship Manager | E1 (banking) | E1 (tracked toward E2) | Named-account portfolios recur outside banking |

## Cumulative demand (16 prior + 6 new = 22)

Prior lists: [telecom](telecom-demand.md) and the cross-industry seed set
(see telecom-demand.md "Prior demand" section).

## Notes

- Financial Crime Compliance Manager is deliberately distinct from
  Regulatory Compliance Manager (program-level AML/sanctions vs sector
  regulation generally); distinctness sweep at E4 will test this boundary.
- Regulatory guidance is a corroborating stance (government-guidance class),
  never the definition source (EVIDENCE.md §2).
