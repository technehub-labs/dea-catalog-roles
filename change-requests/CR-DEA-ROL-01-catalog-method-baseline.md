# CR-DEA-ROL-01: Catalog Method and Governance Baseline

**Owner:** Emmanuel A. Otchere
**Author:** Emmanuel A. Otchere
**Status:** Proposed (this PR)

## 1. Objective

Establish the governance document set for the Role catalog: `GOVERNANCE.md` (change control, review roles, acceptance recording), `EVIDENCE.md` (source classes, ratings E0–E5, provenance), and the CR-DEA-ROL series conventions.

## 2. Deliverables

| # | Deliverable |
|---|---|
| 1 | `GOVERNANCE.md` — normative change-control and acceptance rules |
| 2 | `EVIDENCE.md` — evidence classes, ratings, provenance conventions |
| 3 | `change-requests/README.md` — series index |
| 4 | Seed-role evidence rating recorded (all instances: E1 candidate) |

## 3. Rationale

The catalog passed bare allocation (PR #1: envelope, schemas, CI gates) and the entity is queued for lifecycle promotion (dea-architecture-framework#22, proposed → planned). Method documents must exist before admission decisions are made, so that the first canonical promotion cites a landed method rather than retrofitting one.

## 4. Non-goals

- No METHODOLOGY.md yet: the full evidence-ladder procedure lands with the first canonical-admission CR, when it has a real decision to record.
- No instance changes: all existing instances remain E1 candidates under the new ratings.

## 5. Verification

- `python3 scripts/validate_entities.py` — unaffected, PASS (4 instances)
- `python3 scripts/check_cross_catalog_refs.py` — unaffected, 0 failures
- Documents follow the `dea-catalog-business-capabilities` governance document set (CR-DEA-BC-01 precedent), scoped to this catalog.
