# Change Requests

This directory tracks formal change requests (CRs) for `technehub-labs/dea-catalog-roles`, per the `CR-DEA-ROL` series defined in [`GOVERNANCE.md`](../GOVERNANCE.md) §2.

| CR | Title | Status | Notes |
|---|---|---|---|
| [CR-DEA-ROL-01](CR-DEA-ROL-01-catalog-method-baseline.md) | Catalog Method and Governance Baseline | Merged (PR #2) | Establishes GOVERNANCE.md (change control, review roles, acceptance) and EVIDENCE.md (source classes, E0–E5 ratings, provenance), and the CR-DEA-ROL series conventions. Precedent: dea-catalog-business-capabilities CR-DEA-BC-01. |
| [CR-DEA-ROL-02](CR-DEA-ROL-02-first-canonical-admission.md) | First Canonical Admission — Regulatory Compliance Manager | Proposed (this PR) | Admits `roles:role-regulatory-compliance-manager` as the catalog's first canonical role (E5): lifecycle proposed → active, version 0.1.0 → 0.2.0, evidence ladder recorded on the instance. Adds `docs/distinctness-register.md` (E4 sweep: compliance/assurance, finance, data clusters). Four-industry recurrence (telecom, banking, health, public-sector); distinct from Financial Crime Compliance Manager, Data Protection Officer, Internal Auditor, Clinical Governance Lead. Verification: 34/34 schema-valid; cross-catalog 0 failures (skills edge warns pending publication, tracked in dea-catalog-skills#1). |
