# Common Case-Study Scorecard

[← Case-study method](method.md) · [Next: Global commerce surge →](global-commerce.md)

Score every case out of 100. Award points for explicit reasoning and evidence, not
for naming many services.

| Dimension | Points | Strong evidence |
| --- | ---: | --- |
| Context and discovery | 10 | Outcome, stakeholders, current state, unknowns, assumptions |
| Requirements and invariants | 10 | Scale, latency, SLO, RTO/RPO, consistency, compliance |
| Options and trade-offs | 12 | Two credible options, comparison, rejected optimization |
| Architecture and data | 15 | Clear flow, state, boundaries, integration, capacity |
| Security and governance | 12 | Threats, identity, isolation, privacy, audit, responsibility |
| Reliability and recovery | 12 | Failure behavior, overload, backup, failover, verification |
| Delivery and operations | 10 | Migration, progressive change, telemetry, ownership, runbooks |
| Cost and value | 8 | Drivers, unit economics, budgets, commitments, value measure |
| Failure-inject response | 6 | Containment, evidence, recovery, communication, learning |
| Communication and decision | 5 | Recommendation, risks, phases, evidence needed next |
| **Total** | **100** | |

## Interpretation

- **90–100:** principal-level; decisions connect technology, business, and change.
- **80–89:** architect-ready; coherent and operable with minor evidence gaps.
- **70–79:** senior design; viable architecture but incomplete trade-offs or rollout.
- **55–69:** solution outline; product knowledge exceeds systems reasoning.
- **Below 55:** restart with discovery, invariants, options, and failure behavior.

## Score caps

The score cannot exceed 69 if there is only one option, 59 if security or recovery
is absent, or 49 if the answer never establishes business outcome and constraints.
An impossible claim such as guaranteed zero downtime should reduce both reliability
and communication scores unless it is immediately corrected.

## Feedback format

Record three strengths, three missing decisions, the highest-risk assumption, and
one experiment to run before repeating the case. Re-score within seven days using
different failure injects.
