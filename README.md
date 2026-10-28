# dea-catalog-roles

> DEA catalog for **Role** — OpenDEAM v0.3.0 (ADR-0003).

## Role (`ROL`)

- **Entity id:** `dea:entity-role`
- **Allocation:** L3 · L3-people-skills-culture
- **Status:** proposed

A defined set of required Skills and responsibilities that an Actor fulfills within an Organizational Unit.

## Relationships (from the OpenDEAM model)

- **ROL → AC** — fulfilled by (realization, 1:0..N)
- **SKL → ROL** — required by (dependency, 0..N:0..N)

## Allocation contract

This repo's `metamodel-pointer.yaml` is validated in CI against the pinned
OpenDEAM root model (`v0.3.0`) via the reusable
`validate-against-model.yml` workflow. Drift fails CI.

Content (entity instances) lands when the entity promotes from
`proposed` to `planned`/`scaffold` per the model lifecycle.

## Catalog structure

- `CATALOG.yaml` — catalog envelope and entity index
- `entities/v1-alpha/` — Role instances (validate against `schemas/role.schema.json`)
- `schemas/` — vendored OpenDEAM schemas pinned to the metamodel
- `dependencies.yaml` — cross-catalog edges (SKL → ROL, ROL → AC)
- `TAXONOMY.md` — role classification axis
- `change-requests/`, `contributions/` — governance queues
- `scripts/validate_entities.py` — schema validation, run in CI
  (`validate-entities.yml`) alongside pointer validation
- `scripts/check_cross_catalog_refs.py` — verifies `skills:`/`actors:`
  references resolve against partner catalogs (warning until they publish
  entities; failure on unknown namespaces or contradicting a published list)
- `GOVERNANCE.md` / `EVIDENCE.md` — change control and evidence method
  (CR-DEA-ROL series)
- `INDUSTRIES.md` + `industries/` — industry discovery program and per-industry
  registers/demand lists (first slice: telecom)
- `change-requests/` — CR-DEA-ROL index and documents
- `ingestion/` — bulk ingestion source + integrity manifest
  (CR-ROL-RICH-000 batch: 6000 candidate roles, 12 industry slices × 500,
  30 domains each); gated in CI by `validate-ingestion.yml`
- `scripts/materialize_roles.py` — materializes admitted bulk rows as
  entities (bounded by CR admission; existing instances win on collision)

## Catalog scale

| Metric | Value |
|---|---|
| Candidate Role entities in bulk batch | 6000 |
| Industry slices | 12 (500 roles each, 30 domains per slice) |
| Role functions (naming families) | 18 |
| Taxonomy primary classes covered | 5 of 5 |
| Seniority bands | 6 |
| Primary SKL → ROL edges asserted | 6000 (+6000 secondary, unverified) |
| Source schema | `schemas/role.schema.json` (OpenDEAM v0.3.0, ADR-0003) |

## Rich role facets

Bulk ingestion rows carry these facets beyond the base schema. Facets never
widen identity or membership; they are provenance and classification only.

| Facet | Schema home | Convention |
|---|---|---|
| `domain` | `metadata.domain` / `tags` | Operating-model domain the role is anchored in |
| `function` | `metadata.function` / `tags` | Naming family (Engineer, Manager, Auditor, …) |
| `org_unit` | `metadata.org_unit` | Organizational Unit alignment (`<Domain> Unit`) |
| `seniority_band` / `seniority_level` | `tags seniority:<band>:<level>` | See TAXONOMY.md |
| `industries` | `metadata.industries[]` | Primary evidence slice (provenance, not membership) |
| `related_industries` | `metadata.industries[]` (additional) | Cross-industry recurrence evidence |
| `secondary_skill_id` | second `relationships[]` edge | Secondary SKL → ROL requires edge, unverified |

## License

Apache 2.0 — see [LICENSE](./LICENSE) and [NOTICE](./NOTICE).
