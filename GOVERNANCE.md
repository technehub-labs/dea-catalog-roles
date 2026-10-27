# Governance: Change Control, Roles, Acceptance

Normative for how this repository changes. Established by **CR-DEA-ROL-01**.

---

## 1. Change control

| Change | Requirement |
|---|---|
| Catalog method (this document set: GOVERNANCE, EVIDENCE, TAXONOMY) | Change Request (`CR-DEA-ROL-*`) |
| Canonical role admission or removal | Evidence trail + review per EVIDENCE.md |
| Role instance shape (`entities/v1-alpha/`) | Schema-valid against vendored `role.schema.json`; CI blocking |
| Cross-catalog references (`skills:`, `actors:`) | Must resolve per `check_cross_catalog_refs.py`; warning only while the partner catalog has no published entities |
| `metamodel-pointer.yaml` | Regenerated from the OpenDEAM root model fan-out only; never hand-edited |
| Record shape | Owned by `dea-metamodel`; reconciled here via CR, never redefined |
| Vendored schemas (`schemas/`) | Mirror `dea-metamodel` at the pinned version; drift is a CR-level change |

## 2. Change Request conventions

1. **Series tag.** `CR-DEA-ROL` (DEA Role). Numbers sequential.
2. **Land as authored.** An accepted CR ships verbatim to `change-requests/CR-DEA-ROL-NN.md`; status changes are recorded by later PRs, not by editing the landed CR.
3. **Proposal PR shape.** A CR proposal PR ships exactly: the CR document, the `change-requests/README.md` index row, and the README pointer.
4. **One phase per PR.** Each phase ships a visible deliverable; the PR body states deliverables, verification, and evidence.

## 3. Roles

| Role | Responsibility |
|---|---|
| Catalog steward | Owns the method documents, the CR pipeline, and promotion decisions. Currently: eaojnr. |
| Semantic reviewer | Definition quality, taxonomy-class fit, MECE discipline, naming conformance. |
| Architectural reviewer | Relationship correctness against the model (SKL→ROL, ROL→AC), layer boundaries, cross-catalog resolution. |

One person may hold multiple roles; the review recording is mandatory regardless.

## 4. Acceptance recording

1. Every lifecycle transition (`proposed → planned → active …` per the metamodel lifecycle) is recorded on the instance's provenance (`provenance` block or PR trail).
2. Canonical admission requires: schema validation green, cross-catalog check green (or warned with rationale), and both review outcomes recorded.
3. Post-merge CI must be green; `validate-allocation.yml` and `validate-entities.yml` are the standing checks.
4. A shipped CR closes with an objective scorecard: deliverables, verification results, live URLs.

## 5. External authorities

| Authority | Owns | This catalog |
|---|---|---|
| `dea-architecture-framework` (OpenDEAM) | Layer and building-block allocation (L3-people-skills-culture); entity lifecycle status | Consumes via pinned model tag; pointer regenerates from fan-out |
| `dea-metamodel` | Entity and relationship structure; record shape; relationship-type vocabulary | Consumes; reconciles via CR, never redefines |
| `dea-catalog-skills` | `skills:` id namespace (SKL→ROL edge) | References must resolve; coordinated via catalog issue |
| `dea-catalog-actors` | `actors:` id namespace (ROL→AC edge) | Deferred until that catalog publishes entities |

## 6. Writing conventions

All shipped documents use Design Specification tone (declarative, no "we should"). Authorship-bearing fields carry `Emmanuel A. Otchere` per the cardinal rule (CR-BP-118); agent roles are recorded in the CR chain, not in published artifacts.

## 7. References

- Evidence: [`EVIDENCE.md`](EVIDENCE.md)
- Classification: [`TAXONOMY.md`](TAXONOMY.md)
- Dependencies: [`dependencies.yaml`](dependencies.yaml)
- Cardinal rules: `dea-architecture-framework` → `docs/governance/cardinal-rules.md`
