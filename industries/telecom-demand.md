# Telecom Slice — Skills Demand List

Per [INDUSTRIES.md](../INDUSTRIES.md). This is the consolidated demand signal
to `dea-catalog-skills` from the telecom discovery pass 1: the skill ids this
slice's role instances require published for their `SKL → ROL` edges to
resolve.

## New skill demand from this slice

| Skill (proposed name) | id | Required by role |
|---|---|---|
| Network Operations | `skills:skill-network-operations` | `roles:role-network-operations-center-engineer` |
| Service Assurance | `skills:skill-service-assurance` | `roles:role-service-assurance-manager` |
| Interconnect Management | `skills:skill-interconnect-management` | `roles:role-interconnect-and-wholesale-manager` |
| Regulatory Compliance | `skills:skill-regulatory-compliance` | `roles:role-regulatory-compliance-manager` |
| Service Provisioning | `skills:skill-service-provisioning` | `roles:role-service-provisioning-manager` |
| Network Planning | `skills:skill-network-planning` | `roles:role-network-planning-engineer` |

## Prior demand (cross-industry, from catalog seed + PR #3)

| Skill | id | Required by role |
|---|---|---|
| Enterprise Architecture | `skills:skill-enterprise-architecture` | `roles:role-enterprise-architect` |
| Solution Architecture | `skills:skill-solution-architecture` | `roles:role-solution-architect` |
| Platform Engineering | `skills:skill-platform-engineering` | `roles:role-platform-engineer` |
| Domain Leadership | `skills:skill-domain-leadership` | `roles:role-domain-owner` |
| Product Management | `skills:skill-product-management` | `roles:role-product-owner` |
| Facilitation | `skills:skill-facilitation` | `roles:role-community-lead` |
| Data Architecture | `skills:skill-data-architecture` | `roles:role-data-architect` |
| Security Architecture | `skills:skill-security-architecture` | `roles:role-security-architect` |
| Architecture Review | `skills:skill-architecture-review` | `roles:role-architecture-board-member` |
| Process Management | `skills:skill-process-management` | `roles:role-process-owner` |

## Notes

- All telecom candidates are E1 (single industry pass) except Regulatory
  Compliance Manager, which recurs across regulated industries and is
  tracked toward E2 in the next pass.
- eTOM/SID are process/data frameworks: they evidence recurring telco work;
  role names are inferred, not transcribed (EVIDENCE.md §1).
