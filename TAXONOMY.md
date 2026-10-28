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

## Instance counts (bulk batch, CR-ROL-RICH-000)

| Class | Definition | Instances in batch |
|---|---|---|
| `leadership` | Sets direction and is accountable for outcomes of a domain | 718 |
| `governance` | Constrains or reviews the shape of other entities | 718 |
| `functional` | Delivers a business capability end-to-end | 2051 |
| `technical` | Realizes technology and data artifacts | 1795 |
| `enablement` | Supports others in performing their roles | 718 |

## Seniority vocabulary (tag facet)

Derived from the role function; carried as a tag `seniority:<band>:<level>`:

| Band | Level | Definition | Instances in batch |
|---|---|---|---|
| Associate | 1 | Executes defined tasks under supervision; learning the domain playbook | 359 |
| Professional | 2 | Delivers independently within standard practice | 1436 |
| Senior | 3 | Handles complex, ambiguous work; reviews others' output | 1436 |
| Lead | 4 | Directs a team or practice area; owns team outcomes | 1442 |
| Principal | 5 | Sets standards and direction across a domain; deep expert authority | 968 |
| Executive | 6 | Owns domain strategy, investment, and organisational design | 359 |

## Conventions

- One `role_class` per role instance; additional facets via `tags`.
- New classes require a change request under `change-requests/`.
- The taxonomy anticipates a future `completeness_contract` (OpenDEAM main,
  post-v0.3.0): every role instance must classify by exactly one class to
  count toward catalog completeness.
