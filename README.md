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

## License

Apache 2.0 — see [LICENSE](./LICENSE) and [NOTICE](./NOTICE).
