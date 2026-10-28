# CR-DEA-ROL-12: Canonical Admissions — Data Protection Officer, NOC Engineer, Relationship Manager

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Admit three curated roles as canonical (E5), each with genuine
second-industry batch corroboration under the family-recurrence register
usage rules. Excluded from this round despite tempting evidence:
Treasury Manager, Public Finance Manager, Claims Operations Manager,
Clinical Informaticist — their batch domains sit in slices that
*supersede or extend* their original industry (finance extends banking,
healthcare extends health), so the batch rows are not independent
corroboration. Recorded here to keep the exclusion honest and auditable.

## 2. Evidence trails

### Data Protection Officer (`roles:role-data-protection-officer`)

| Stage | Rating | Evidence |
|---|---|---|
| Recurrence | E1 | Public-sector pass 1: data-protection accountability in citizen-services operating model |
| Corroboration | E2 | Legal-regulatory slice carries the `Data Protection & Privacy` operating-model domain (17 roles anchored on it) — an independent industry evidencing the same responsibility |
| Enterprise-generality | E3 | Personal-data processing at scale recurs across all 12 slices' operating models; the two registering industries (public-sector, legal-regulatory) are the most data-regulation-intensive forms |
| Distinctness | E4 | Compliance/assurance cluster (prior sweep): distinct from Regulatory Compliance Manager (personal-data vs all-of-regulation; statutory independence) and Internal Auditor |
| Review | E5 | This CR: semantic (governance · compliance) + architectural (requires edge to `skills:skill-data-protection`) |

### Network Operations Center Engineer (`roles:role-network-operations-center-engineer`)

| Stage | Rating | Evidence |
|---|---|---|
| Recurrence | E1 | Telecom pass 1: NOC accountability in the telco operating model |
| Corroboration | E2 | Technology slice carries the `Network Operations Centre` domain — network operations as a responsibility recurs outside telecom |
| Enterprise-generality | E3 | Network operations recurs wherever production networks exist (technology, telecom slices; implied by data-center-dependent operating models across all slices) |
| Distinctness | E4 | Operations cluster sweep (this PR): distinct from Service Assurance Manager, Service Provisioning Manager, Platform Engineer |
| Review | E5 | This CR: semantic (technical · operations) + architectural (requires edge to `skills:skill-network-operations`) |

### Relationship Manager (`roles:role-relationship-manager`)

| Stage | Rating | Evidence |
|---|---|---|
| Recurrence | E1 | Banking pass 1: named-account portfolio ownership |
| Corroboration | E2 | Consulting slice carries the `Client Relationship Management` domain — relationship ownership recurs in a services-industry form |
| Enterprise-generality | E3 | Named-account relationship management recurs wherever revenue depends on managed portfolios (banking, consulting slices; commercial domain cluster across the batch) |
| Distinctness | E4 | Operations sweep appended row + commercial & sourcing boundary set: distinct from Interconnect & Wholesale Manager (customer vs carrier counterparties), Procurement Manager (revenue vs buy-side) |
| Review | E5 | This CR: semantic (functional · commercial) + architectural (requires edge to `skills:skill-relationship-management`) |

## 3. Change

| Instance | lifecycle_status | version |
|---|---|---|
| `roles:role-data-protection-officer` | proposed → active | 0.1.0 → 0.2.0 |
| `roles:role-network-operations-center-engineer` | proposed → active | 0.1.0 → 0.2.0 |
| `roles:role-relationship-manager` | proposed → active | 0.1.0 → 0.2.0 |

Evidence ladders recorded on instances; industries facet extended with
the corroborating slice; `CATALOG.yaml` canonical 7 → 10. Operations
cluster swept in the distinctness register.

## 4. Verification

- `python3 scripts/validate_entities.py` — 307/307 PASS
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures
- Post-merge CI green (standing checks)
