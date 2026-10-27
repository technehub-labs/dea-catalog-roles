# Role Taxonomy

Classification axis for Role instances in this catalog. MECE at the top level;
subclasses may overlap deliberately (a role may be both `technical` and
`governance` via tags, but carries exactly one primary class).

## Primary classes

| Class | Definition | Typical examples |
|---|---|---|
| `leadership` | Sets direction and is accountable for outcomes of a domain | CTO, Head of Architecture, Domain Owner |
| `governance` | Constrains or reviews the shape of other entities | Architecture Board Member, Guardrail Owner |
| `functional` | Delivers a business capability end-to-end | Product Owner, Process Owner, Service Manager |
| `technical` | Realizes technology and data artifacts | Enterprise Architect, Solution Architect, Platform Engineer |
| `enablement` | Supports others in performing their roles | Coach, Trainer, Community Lead |

## Conventions

- One `role_class` per role instance; additional facets via `tags`.
- New classes require a change request under `change-requests/`.
- The taxonomy anticipates a future `completeness_contract` (OpenDEAM main,
  post-v0.3.0): every role instance must classify by exactly one class to
  count toward catalog completeness.
