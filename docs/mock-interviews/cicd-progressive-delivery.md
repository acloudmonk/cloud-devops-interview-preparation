# Mock Interview: CI/CD and Progressive Delivery

[← CI/CD module overview](../09-cicd/index.md) ·
[Master competency map](../master-competency-map.md)

Use this 50-minute interview after completing Module 09. Reveal follow-ups only
when their section begins.

## Candidate brief

A 250-engineer company uses GitHub Actions to deploy 55 services into development,
staging, and multi-region production AWS accounts. Builds use mutable tags, AWS keys
live in repository secrets, forks share persistent runners, tests are flaky, and
database migrations run at startup. A stale workflow recently replaced a good
production version. Design a trustworthy and progressive delivery system.

## Schedule

| Time | Candidate task | Interviewer observes |
| --- | --- | --- |
| 0–5 min | Clarify product, traffic, compliance, recovery, and team constraints | Discovery before tool choice |
| 5–13 min | Draw control/execution planes and artifact/evidence flow | Delivery mental model |
| 13–22 min | Design test portfolio, immutable promotion, and gates | Signal, traceability, and speed |
| 22–31 min | Design runner trust, GitHub OIDC, and AWS role boundaries | Security and identity reasoning |
| 31–39 min | Choose deployment, exposure, and verification strategy | Progressive-delivery trade-offs |
| 39–45 min | Handle data change, stale run, and regional partial failure | Compatibility and recovery |
| 45–50 min | Give migration and executive recommendation | Adoption, metrics, and clarity |

## Required follow-ups

1. The canary is healthy but customer-support reports checkout failures. What now?
2. Provenance validates, but the authorized builder was compromised. What did it prove?
3. A cloud API timed out after partial success. Is a pipeline rerun safe?
4. A destructive schema migration finished. How does that change rollback?
5. GitHub is unavailable during an urgent security release. What continuity is allowed?

## Decision follow-ups

| Candidate choice | Ask |
| --- | --- |
| Use blue/green | How are database compatibility, cost, traffic switch, and fallback tested? |
| Use canary | Why is the cohort representative and which signal stops promotion? |
| Keep manual approval | What judgment does it add and what evidence/expiry does the approver see? |
| Use self-hosted runners | How are trust levels, lifecycle, network, image, and credentials isolated? |
| Adopt GitOps | How does emergency change avoid a reconciliation fight and return to source of truth? |
| Rebuild per environment | Why is that preferable to promoting a verified immutable digest? |

## Scorecard

Score each dimension from 0 to 4.

| Dimension | 0–1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Discovery | Starts with YAML/tool | Basic delivery questions | Product, data, trust, recovery, scale | Finds constraints that change strategy |
| Mental model | Linear job list | Stages and environments | Control/execution and evidence flow | Predicts cross-boundary failure |
| Quality | “Run all tests” | Test levels named | Portfolio, signal, ownership, flake policy | Risk-based selection and measurable trust |
| Supply chain | Tags and scans | Digest/SBOM mentioned | Build once, provenance, retention, policy | Explains trust root and compromise response |
| Security | Stored secrets | Least privilege | OIDC, events, runners, environments | End-to-end attacker-path reasoning |
| Delivery | Generic canary | Plausible rollout | Cohort, signals, thresholds, recovery | Compatibility and business outcomes integrated |
| Operations | Rerun/rollback | Some monitoring | Partial state, idempotency, concurrency, SLOs | Tested continuity and evidence-led incident command |
| Leadership | Tool dump | Understandable | Migration, measures, decision | Concise trade-off and organizational adoption |

Maximum score: **32**. A score of 25 or more with no dimension below 2 is a
strong senior-level practice result.

## Reflection

Record one missed trust boundary, one weak signal, one unsafe recovery assumption,
one compatibility gap, and one answer to shorten. Repeat within seven days.
