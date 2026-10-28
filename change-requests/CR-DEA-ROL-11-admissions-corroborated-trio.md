# CR-DEA-ROL-11: Canonical Admissions — Procurement Manager, Service Designer, Security Architect

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Admit three curated roles as canonical (E5). These are the first
admissions to cite **bulk-batch corroboration** under the
family-recurrence register's usage rules: each role's own domain recurs
across multiple industries in the batch, which — combined with its curated
slice evidence — satisfies E2/E3 without overstating (batch names/ids are
industry-disjoint; the recurrence argued here is at domain level, which is
the honest claim the register permits).

## 2. Evidence trails (EVIDENCE.md §3; family register usage rules)

### Procurement Manager (`roles:role-procurement-manager`)

| Stage | Rating | Evidence |
|---|---|---|
| Recurrence | E1 | Public-sector pass 1: procurement law/policy accountability in citizen-services operating model |
| Corroboration | E2 | Manufacturing slice batch row `roles:role-procurement-manager` (Procurement domain): same role identity, independent industry — the collision we recorded at ingestion is exactly this corroboration |
| Enterprise-generality | E3 | Procurement/sourcing/vendor/supply domains recur across **8 of 12 slices** (mining, manufacturing, technology, media, healthcare, transport, audit, consulting) — the most-recurred non-governance domain cluster in the batch |
| Distinctness | E4 | Commercial & sourcing cluster sweep: distinct from Relationship Manager, Interconnect & Wholesale Manager, Public Finance Manager |
| Review | E5 | This CR: semantic (functional · commercial) + architectural (single requires edge to `skills:skill-procurement-management`) |

### Service Designer (`roles:role-service-designer`)

| Stage | Rating | Evidence |
|---|---|---|
| Recurrence | E1 | Public-sector pass 1: digital-government service design |
| Corroboration | E2 | Batch Designer-family experience-domain roles across independent industries: Developer Experience (technology), Immersive Experiences (entertainment), Patient Experience (healthcare), Customer Experience Design (consulting) |
| Enterprise-generality | E3 | Service-design/experience domains recur across **4 of 12 slices**; experience design as a recurring enterprise responsibility, not a government specialism |
| Distinctness | E4 | Design cluster sweep: distinct from Patient Experience Manager, Clinical Informaticist, Architect family |
| Review | E5 | This CR: semantic (functional · design) + architectural (requires edge to `skills:skill-service-design`) |

### Security Architect (`roles:role-security-architect`)

| Stage | Rating | Evidence |
|---|---|---|
| Recurrence | E1 | Curated seed (PR #3): security architecture in the enterprise technology model |
| Corroboration | E2 | Batch Architect-family security-domain roles across independent industries: Cybersecurity Operations + Product Security (technology), Transport Security (transport), Network Security (telecom) |
| Enterprise-generality | E3 | Security/cyber domains recur across **3 of 12 slices** including two curated industries (telecom seed set); security architecture recurs wherever technology is operationally deployed |
| Distinctness | E4 | Technical-architecture cluster sweep: distinct from Enterprise Architect, Solution Architect, Data Architect |
| Review | E5 | This CR: semantic (governance + technical) + architectural (requires edge to `skills:skill-security-architecture`) |

## 3. Change

| Instance | lifecycle_status | version |
|---|---|---|
| `roles:role-procurement-manager` | proposed → active | 0.1.0 → 0.2.0 |
| `roles:role-service-designer` | proposed → active | 0.1.0 → 0.2.0 |
| `roles:role-security-architect` | proposed → active | 0.1.0 → 0.2.0 |

Evidence ladders recorded on instances; `CATALOG.yaml` canonical 4 → 7.
Distinctness register gains three swept clusters (commercial & sourcing,
design, technical architecture).

## 4. Verification

- `python3 scripts/validate_entities.py` — 307/307 PASS
- `python3 scripts/check_cross_catalog_refs.py` — 0 failures
- Post-merge CI green (standing checks)
