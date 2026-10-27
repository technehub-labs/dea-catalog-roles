# Distinctness Register (E4 Sweep)

Per EVIDENCE.md §3, E4 requires a distinctness argument: a candidate is not
a duplicate or near-duplicate of another cataloged role. This register records
the sweep outcome per cluster. Review outcome recorded per GOVERNANCE.md §4.

## Cluster: compliance & assurance (swept 2026-10-27)

| Role | Accountability (one line) | Distinct from | Distinctness argument |
|---|---|---|---|
| Regulatory Compliance Manager | Enterprise conformance to sector regulation | Financial Crime Compliance Manager | Sector regulation generally (privacy, safety, prudential, market conduct) vs program-level AML/sanctions. Different evidence base, different control set; overlap only at regulatory-change intake. |
| Regulatory Compliance Manager | — | Data Protection Officer | All-of-regulation conformance vs personal-data protection specifically. DPO has statutory independence and data-subject-facing duties; RCM has none. |
| Regulatory Compliance Manager | — | Internal Auditor | Owning the compliance control environment (first/second line) vs independent assurance over all controls (third line). Different reporting lines by design. |
| Financial Crime Compliance Manager | AML/sanctions program | Data Protection Officer | Financial-crime detection and reporting vs personal-data protection; control sets are disjoint. |
| Internal Auditor | Independent assurance to the board | Data Protection Officer | Enterprise-wide control assurance vs data-protection advice and oversight; DPO independence is regulatory, auditor independence is governance-structural. |
| Clinical Governance Lead | Clinical quality & safety standards | Regulatory Compliance Manager | Clinical practice standards (peer/professional basis) vs sector regulation (legal basis). Corroborated only in health; both accountabilities exist separately in every health system. |

**Sweep outcome:** Regulatory Compliance Manager is distinct from all five
adjacent roles. No merges required. Sweep re-runs if a new role lands in the
cluster.

## Cluster: finance (swept 2026-10-27)

| Role | Accountability (one line) | Distinct from | Distinctness argument |
|---|---|---|---|
| Treasury Manager | Balance-sheet liquidity & funding | Public Finance Manager | Corporate treasury (funding, IR/FX exposure within limits) vs public budget cycle (appropriation, in-year control, legislative reporting). Different fiduciary basis; overlap only in cash management mechanics. |

**Sweep outcome:** distinct; no merge.

## Cluster: data & information (swept 2026-10-27)

| Role | Accountability (one line) | Distinct from | Distinctness argument |
|---|---|---|---|
| Data Architect | Enterprise data architecture | Health Information Manager | Data models, ownership boundaries, governance rules for data assets vs records governance (privacy, consent, coding integrity, release of information). HIM is accountable for records, DA for architecture. |

**Sweep outcome:** distinct; no merge.

## Cluster: experience & program (swept 2026-10-27)

| Role | Accountability (one line) | Distinct from | Distinctness argument |
|---|---|---|---|
| Patient Experience Manager | Patient/citizen feedback, service recovery, experience improvement | Service Designer | Operating and improving live services (feedback loops, complaint resolution) vs designing new or redesigned services (journeys, blueprints, prototypes). Different lifecycle stage of the same service. |
| Patient Experience Manager | — | Relationship Manager | Experience of a service population (aggregate measures, service recovery) vs commercial ownership of a named-account portfolio (P&L accountability). Different success criteria. |
| Patient Experience Manager | — | Citizen Services Operations Manager | Experience outcomes (satisfaction, service recovery) vs service delivery operations (queues, SLAs, caseload). PEM is accountable for how service feels; CSOM for whether it runs. |
| Population Health Program Manager | Health-outcome programs for a defined population | Process Owner | Program = temporary, outcome-targeted, multi-workstream change initiative vs process = standing, repeatable operational flow. Different object and horizon. |
| Population Health Program Manager | — | Change Initiative (model entity CHI) | Role vs initiative: the role persists across the programs it manages; an initiative is one instance. The ROL manages CHIs; it is not one. |
| Population Health Program Manager | — | Product Owner | Program portfolio accountability (epidemiological targets, population outcomes) vs single-product value maximization (backlog, increments). Different value measure. |

**Sweep outcome:** both candidates distinct from all adjacent roles; no merges. Service Designer vs Citizen Services Operations Manager boundary (design vs run) also clarified via the PEM/CSOM row. Sweep re-runs if a new role lands in the cluster.

## Pending clusters

- operations (Service Assurance, Claims Operations, Payments Operations,
  Citizen Services Operations, NOC, Service Provisioning): sweep at next
  admission from that cluster
- commercial (Relationship Manager, Procurement Manager): same
- design (Service Designer, Clinical Informaticist): same
