# Industry Discovery Program

Per GOVERNANCE.md and EVIDENCE.md, industry sources **evidence specialization
boundaries, never first-order membership**. This document defines how the
catalog runs bounded, industry-managed discovery so that:

1. role instances stay enterprise-general in identity (a role exists because
   the responsibility recurs, not because one industry names it);
2. each industry slice produces a concrete demand signal for the partner
   catalogs (skills, later actors), which is what closes cross-catalog edges;
3. the process is repeatable per industry without re-inventing method.

## Method per industry slice

| Step | Deliverable |
|---|---|
| 1. Register the industry | `industries/<industry>.yaml` (scope, sources, status) |
| 2. Recurrence sweep | candidate roles inferred from recurring responsibilities in the industry's operating model, rated per EVIDENCE.md |
| 3. Demand list | `industries/<industry>-demand.md`: skills ids the slice requires published, one row per role-to-skill edge |
| 4. Coordination | post the demand list to `dea-catalog-skills` (issue per slice) |
| 5. Reconciliation | enterprise-general candidates land in `entities/` with `industries:` facet; industry-specific-only candidates stay in the slice register until E2+ |

## Industry facet convention

Role instances may carry `metadata.industries: [<industry-id>]` listing the
industries whose operating models evidence the role's recurrence. Absence
means general recurrence was argued without industry slicing. The facet is
evidence provenance, not membership: it never restricts a role's scope.

## Slices

| Industry | id | Status | Demand list |
|---|---|---|---|
| Telecommunications | `telecom` | discovery-complete (E1 candidates registered) | [industries/telecom-demand.md](industries/telecom-demand.md) |
| Banking | `banking` | discovery-complete (6 candidates; 1 E2 promotion) | [industries/banking-demand.md](industries/banking-demand.md) |
| Health | `health` | discovery-complete (6 candidates; 1 E2, 1 E3-track promotion) | [industries/health-demand.md](industries/health-demand.md) |
| Public Sector | `public-sector` | discovery-complete (6 candidates; 1 E3 confirm, 2 E2 promotions) | [industries/public-sector-demand.md](industries/public-sector-demand.md) |
