# Family Recurrence Register

Per EVIDENCE.md, ratings attach per role instance. This register records
what the bulk batch actually evidences: **function-family recurrence
across industries**. It is the citable evidence base for per-role
admissions; an admission CR cites the family row plus the role's own
domain evidence.

## How to read this register

- A row shows that a function family (class × function) recurs across N
  industries in the bulk batch (CR-ROL-RICH-000). This is family-level
  corroboration: it evidences that the *kind* of responsibility recurs,
  not that a specific role instance recurs.
- Batch domains, skill ids, and role names are deliberately
  industry-disjoint by construction. **Instance-level cross-industry
  recurrence cannot be claimed from batch data alone**; per-instance E2
  requires either a second slice registering the same domain role or an
  external source (EVIDENCE.md §2).

## Families recurring across all 12 slices (E3-track at family level)

| Class | Function | Instances | Slices |
|---|---|---|---|
| enablement | Coach | 359 | 12/12 |
| enablement | Consultant | 359 | 12/12 |
| functional | Analyst | 359 | 12/12 |
| functional | Manager | 359 | 12/12 |
| functional | Operations Coordinator | 359 | 12/12 |
| functional | Planner | 359 | 12/12 |
| functional | Product Owner | 359 | 12/12 |
| functional | Program Manager | 250 | 12/12 |
| governance | Auditor | 359 | 12/12 |
| governance | Compliance Officer | 359 | 12/12 |
| leadership | Head of | 359 | 12/12 |
| leadership | Lead | 359 | 12/12 |
| technical | Administrator | 359 | 12/12 |
| technical | Architect | 359 | 12/12 |
| technical | Designer | 359 | 12/12 |
| technical | Developer | 359 | 12/12 |
| technical | Engineer | 359 | 12/12 |

## Materialization state per family (2026-10-28)

| Family | Materialized | Source CRs |
|---|---|---|
| leadership / Head of | 30 (technology) | ROL-06 |
| governance / Auditor | 90 (technology, audit, legal-regulatory) | ROL-07, ROL-08, ROL-09 |
| governance / Compliance Officer | 90 (technology, audit, legal-regulatory) | ROL-07, ROL-08, ROL-09 |

## Use in admission CRs

1. Cite the family row (recurrence across N industries).
2. Cite the role's own domain evidence (slice register, domain scope).
3. If the domain itself is industry-specific only, the honest ceiling is
   E2 pending a second industry registering the same domain; if the
   domain is generic across industries (e.g., cybersecurity in
   technology, finance, and consulting slices), argue E3 directly.
4. E4 distinctness per the distinctness register; E5 review per
   GOVERNANCE.md §4.
