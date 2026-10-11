# Migration Strategies and Target State

[← Discovery and portfolio](discovery-portfolio.md) · [Next: Landing-zone readiness →](landing-zone-readiness.md)

## Use dispositions as decisions, not slogans

Common portfolio dispositions are **rehost, replatform, refactor/re-architect,
repurchase, relocate, retire, and retain**. Definitions vary across frameworks, so
state what each means in the program. Select at workload or meaningful component
boundary and document why, risk, economics, prerequisites, and future trigger.

| Disposition | Best fit | Principal caution |
| --- | --- | --- |
| Rehost | Deadline-led move with acceptable architecture | Moves operational debt and may worsen cost |
| Relocate | Compatible virtualization estate with minimal application change | Preserves platform constraints and licensing questions |
| Replatform | Bounded managed-service or runtime change | Compatibility and operating behavior still require proof |
| Refactor/re-architect | Material value requires architecture change | Highest delivery, regression, and organization risk |
| Repurchase | Commodity capability is better served by SaaS/product | Data exit, integration, identity, process, and vendor risk |
| Retire | Capability is unused, duplicated, or replaced | Usage and records obligations must be proven |
| Retain | Constraint or value makes movement unjustified now | Needs an owner, support plan, review date, and integration path |

## Define the target state before tool selection

Specify service boundaries, runtime, data authority, integrations, identity, network,
resilience, observability, delivery, security, governance, support, capacity, cost, and
exit posture. Distinguish minimum viable landing state from later optimization. Avoid
both permanent lift-and-shift and a program-blocking “modernize everything” mandate.

## Test target assumptions early

Use proofs for compatibility, performance, latency, quotas, licensing, data movement,
control evidence, operability, and team skills. A successful installation is not a
production proof. Define representative load and failure conditions plus explicit
acceptance thresholds.

## Preserve optionality deliberately

Portability has cost. Apply it where exit, regulatory, bargaining, acquisition, or
deployment requirements justify it. Prefer portable interfaces, data formats,
automation, and observability where practical; accept provider differentiation when
its value exceeds switching risk.
