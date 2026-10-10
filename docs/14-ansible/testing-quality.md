# Testing and Quality Gates

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Testing should answer progressively harder questions: does content parse, follow
standards, behave correctly, converge, remain compatible, and produce the
required service outcome?

## Assurance layers

| Layer | Question | Example evidence |
| --- | --- | --- |
| Static | Is content structurally valid and maintainable? | YAML checks, syntax check, ansible-lint |
| Contract | Are inputs valid and dependencies pinned? | argument assertions, requirement lock review |
| Unit/plugin | Does custom logic behave correctly? | focused Python and `ansible-test` tests |
| Integration | Does the role configure a representative target? | ephemeral test instance or container |
| Convergence | Is a second run unexpectedly unchanged? | zero unintended changes |
| Negative | Do unsafe inputs and failed dependencies stop safely? | deliberate failure cases |
| Outcome | Does the service work for users? | health, transaction, security, and telemetry checks |

## Check mode is one layer

Check mode can reveal prospective changes and drift, but module support varies,
registered data may not exist, commands may be skipped, and external systems can
change after the forecast. Maintain a documented exception list and do not call
check mode a guaranteed plan.

## Representative test matrix

Select operating-system versions, architectures, Python versions, init systems,
cloud images, dependency versions, clean hosts, already-converged hosts, and
supported upgrade states. Risk and usage should determine the matrix; exhaustive
combinations are rarely economical.

## Safe promotion flow

1. lint and syntax-check the pinned content;
2. test role contracts and custom plugins;
3. run integration and second-run convergence tests;
4. build and scan the execution environment;
5. run check/diff against a non-production target;
6. canary one production failure domain;
7. verify application and security outcomes;
8. expand in bounded batches with automated stop criteria.

## Test common failure paths

Exercise unreachable targets, expired identity, missing secret, stale inventory,
package-repository outage, handler failure, partial batch, bad template,
controller restart, and rollback. A recovery procedure that has never been run is
only a hypothesis.

## Quality policy

Start new standards as advisory, remove platform friction, then enforce the
high-value controls. Every exception needs an owner, reason, scope, expiry, and
compensating control. Measure false positives and escape defects.

Return to the [module overview](index.md) when ready to continue.
