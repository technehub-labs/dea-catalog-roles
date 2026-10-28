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
| Telecommunications | `telecom` | discovery-complete (E1) — extended to 500 via bulk batch | [industries/telecom-demand.md](industries/telecom-demand.md) |
| Finance & Banking | `finance` | registered — supersedes `banking` slice, extended via bulk batch | [industries/finance-demand.md](industries/finance-demand.md) |
| Healthcare | `healthcare` | registered — extends `health` slice via bulk batch | [industries/healthcare-demand.md](industries/healthcare-demand.md) |
| Public Sector | `public-sector` | discovery-complete (6 candidates; 1 E3 confirm, 2 E2 promotions) | [industries/public-sector-demand.md](industries/public-sector-demand.md) |
| Technology | `technology` | registered — discovery pass 2 (absorbs ICT/SaaS/cloud) | [industries/technology-demand.md](industries/technology-demand.md) |
| Entertainment | `entertainment` | registered — discovery pass 2 | [industries/entertainment-demand.md](industries/entertainment-demand.md) |
| Media | `media` | discovery-complete (E1) — extended to 500 | [industries/media-demand.md](industries/media-demand.md) |
| Mining & Resources | `mining` | registered — discovery pass 2 | [industries/mining-demand.md](industries/mining-demand.md) |
| Transport & Logistics | `transport` | registered — discovery pass 2 | [industries/transport-demand.md](industries/transport-demand.md) |
| Manufacturing | `manufacturing` | registered — discovery pass 2 | [industries/manufacturing-demand.md](industries/manufacturing-demand.md) |
| Audit & Assurance | `audit` | registered — discovery pass 2 | [industries/audit-demand.md](industries/audit-demand.md) |
| Legal & Regulatory | `legal-regulatory` | registered — discovery pass 2 | [industries/legal-regulatory-demand.md](industries/legal-regulatory-demand.md) |
| Consulting | `consulting` | registered — discovery pass 2 | [industries/consulting-demand.md](industries/consulting-demand.md) |

Bulk-batch demand (6000 roles, 12 slices × 500, 30 domains each):
[industries/bulk-6000-demand.md](industries/bulk-6000-demand.md) — 359 primary + 359 secondary skill ids.

Legacy superseded registers remain for provenance: `banking`, `health`.
