# Scenario Questions and Model Answers

[← Enterprise design exercise](design-exercise.md) · [Next: Advanced platform drills →](scenario-drills.md)

Answer aloud using customer, problem, contract, control, operation, adoption, and
evidence before reading the model answer.

## 1. Leadership says, “Install Backstage and give us a platform”

**Model answer:** Backstage can provide a useful portal and catalog, but it does not
create the underlying product. I would baseline developer journeys, choose one
repeated problem, define responsibility and success, then expose owned APIs,
workflows, controls, documentation, and support through the appropriate interfaces.

## 2. Developers wait ten days for an environment

**Model answer:** Map wait versus execution time and approval reasons. Define a
small number of environment products with schema, policy, quota, TTL, ownership,
status, and deletion. Use durable idempotent orchestration and short-lived identity;
measure successful request lead time and failure demand, not request count alone.

## 3. Security wants every deployment manually approved

**Model answer:** Classify risk and automate evidence and policy for routine changes.
Retain human approval for exceptional or high-impact operations, with separation of
duties. Improve preventive and detective controls, provenance, progressive rollout,
and audit so review attention is applied where judgment adds value.

## 4. Teams reject the standard golden path

**Model answer:** Determine whether the path misses a persona, adds friction, hides
cost, or lacks reliability. Use task observation and journey data rather than blame.
Improve the path, provide governed extensions and escape hatches, and distinguish
valid specialized needs from unsupported preference. Adoption should follow value.

## 5. A shared control plane needs administrator access everywhere

**Model answer:** Challenge that topology. Partition reconciliation by account,
environment, or cell; issue short-lived scoped identities; separate read and write;
and validate every operation. Keep an emergency disable path and audit. Central
discovery does not require centralized unlimited mutation authority.

## 6. A platform upgrade breaks 30 services

**Model answer:** Stop rollout, preserve evidence, restore a compatible version or
disable the failing feature, and communicate affected contracts. Add consumer
inventory, compatibility tests, representative canaries, overlapping versions,
release notes, migration tooling, and deprecation windows with named owners.

## 7. Product teams expect the platform team to own their incidents

**Model answer:** Clarify the responsibility contract. The platform owns platform
journeys and shared capability failures; product teams own application behavior,
data, SLOs, and on-call, with defined escalation. Provide telemetry and operational
paths that make ownership achievable instead of merely restating it.

## 8. The portal is down during a production incident

**Model answer:** Running workloads and essential diagnostics should not depend
synchronously on the portal. Preserve APIs/CLI, dashboards, runbooks, and break-glass
access. Define portal and control-plane SLOs separately, cache safe read data, and
test operation during interface loss.

## 9. Each cloud team wants a separate platform

**Model answer:** Standardize user outcomes, identity principles, metadata, evidence,
and lifecycle contracts while retaining provider-native implementation where useful.
Compare duplicated product and operations cost with genuine regulatory or capability
differences. One experience can orchestrate multiple bounded cloud control planes.

## 10. A self-service request times out after creating resources

**Model answer:** A client timeout is an unknown result, not proof of failure. Return
an operation ID, persist desired/current state, make retries idempotent, reconcile,
and expose status. Detect and handle orphan resources; never blindly submit a second
mutation that can duplicate cost or data.

## 11. A template produces compliant services on day one

**Model answer:** Scaffolding is insufficient for “stay right.” Record template and
dependency versions, centralize reusable workflows/modules, continuously evaluate
policy and ownership, automate upgrades, and measure drift. Provide migrations
rather than recopying templates into hundreds of repositories.

## 12. Finance challenges platform cost

**Model answer:** Show total platform cost alongside reduced duplicated tooling,
wait time, incidents, audit effort, and time to value. Measure cost per active team
or successful journey and realized outcomes versus the baseline. Retire low-value
capabilities; avoid chargeback that drives teams toward riskier shadow paths.

## 13. Kubernetes is mandated for every workload

**Model answer:** Start from workload needs. Kubernetes may suit long-running or
portable container platforms, but managed serverless, batch, or data services can
reduce cognitive load and operations. Offer supported archetypes with consistent
controls and evidence rather than turning one runtime into organizational policy.

## 14. A team needs an unsupported database

**Model answer:** Discover requirements and assess whether demand is reusable. If
not, use a time-bound exception with risk owner, identity, network, backup,
observability, cost, and support minimums. Define who operates it and a re-entry or
retirement path; do not imply platform support the team does not receive.

## 15. Portal adoption reaches 90%, but delivery outcomes do not improve

**Model answer:** Portal login is a vanity metric. Segment journeys and inspect wait,
rework, change failure, recovery, cognitive load, tickets, and business lead time.
The portal may front manual bottlenecks. Improve or remove the constraint, then
measure successful end-to-end outcomes and qualitative user experience.
