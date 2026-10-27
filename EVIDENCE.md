# Evidence: Method, Source Stances, Provenance

Normative for how role evidence is gathered, rated, and recorded. Admission decisions cite this document.

---

## 1. Principle: research, not copy

Established role taxonomies are **evidence sources, never templates**. Roles are inferred from recurring enterprise responsibilities; they are not transcribed from any framework. A source can prove that a responsibility recurs across enterprises; it cannot prove that its naming or grouping is right for this catalog. Names are decided by TAXONOMY.md; admission by this document.

## 2. Source classes and stances

| Class | Examples | Stance |
|---|---|---|
| enterprise-architecture | TOGAF role/skill guidance; ArchiMate actor/role modeling | Corroborates role identity and the ROL→AC realization pattern. Names never copied. |
| team-topologies | Platform team patterns | Corroborates the platform-engineer class of roles and team-shape distinctions. |
| job-architecture | Job-architecture and competency frameworks | Evidences market recurrence of role definitions; naming-discipline caution. |
| organizational-design | Span-of-control and accountability literature | Corroborates the leadership/governance class boundaries. |
| internal-baseline | Adopting-enterprise HR and operating-model structures | Reality check; never sufficient alone. |

## 3. Evidence ratings

Candidate roles carry an ordinal rating, E0–E5:

| Rating | Meaning |
|---|---|
| E0 | Invented or single-source; not admissible |
| E1 | Named in one source class; registered as candidate only |
| E2 | Recurring across two independent source classes |
| E3 | Enterprise-generality argued: recurrence across industries/sectors |
| E4 | Distinctness argued: not a duplicate of another cataloged role |
| E5 | Reviewed and admitted canonical |

The four seed instances (Enterprise Architect, Solution Architect, Platform Engineer, Domain Owner) and the Phase-4 additions are currently **E1 candidates**: seeded from enterprise-architecture and team-topologies recurrence, pending corroborated → reviewed promotion per GOVERNANCE.md §3.

## 4. Provenance

Every role instance carries a `provenance` block on its relationships (`type: manual|discovery|inference…`, `asserted_by`, `verification_status: unverified`) per the metamodel's relationship-instance schema. Asserted-by values naming the seed effort are recorded in the CR chain; published artifacts carry no agent names (cardinal rule R1).

## 5. Cross-catalog evidence

- A `skills:` reference is evidenced by the partner catalog's published entity list; until `dea-catalog-skills` publishes, references stay `unverified` warnings.
- A future `actors:` reference (ROL→AC) will be evidenced the same way once `dea-catalog-actors` publishes; the 1:0..N cardinality means roles precede assignments.

## 6. References

- Method: [`GOVERNANCE.md`](GOVERNANCE.md)
- Classification: [`TAXONOMY.md`](TAXONOMY.md)
- Coordination: [dea-catalog-skills#1](https://github.com/technehub-labs/dea-catalog-skills/issues/1)
