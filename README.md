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

## License

Apache 2.0 — see [LICENSE](./LICENSE) and [NOTICE](./NOTICE).
