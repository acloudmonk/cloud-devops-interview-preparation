# Advanced Platform Engineering Drills

[← Scenario questions](scenarios.md) · [Next: Ten-minute platform review →](presentation-template.md)

For each drill, state containment, evidence, failure classes, durable correction,
validation, communication, and residual risk.

## Drill 1 — Compromised template dependency

Pause affected scaffolding and releases, identify generated repositories and built
artifacts from provenance, revoke compromised credentials, and preserve evidence.
Patch the source, rebuild trusted artifacts, and assess deployed workloads. Add
pinned verified dependencies, template SBOM/provenance, isolated generation, release
gates, consumer inventory, and an emergency notification/upgrade path.

## Drill 2 — GitOps controller deletes healthy workloads

Disable reconciliation safely, protect workload state, and preserve desired-state,
policy, identity, and controller logs. Determine whether bad Git state, scope,
pruning, race, or privilege caused the deletion. Restore from an approved revision,
verify data, partition controller authority, add destructive-change previews and
approval, canary reconciliation, and tested recovery from timeout or partial apply.

## Drill 3 — Platform API latency blocks all deployments

Declare impact by journey and provide status plus an approved degraded path. Inspect
queues, downstream quotas, locks, database, dependency timeouts, and recent change.
Apply admission control and priority, restore or roll back, then separate synchronous
validation from long-running work, expose operation status, define SLOs, and test
backlog recovery without retry amplification.

## Drill 4 — Cross-team secrets appear in build logs

Restrict logs, stop the leaking workflow, rotate affected secrets, identify viewers
and artifacts, and follow incident obligations. Remove static secrets through
ephemeral workload identity, mask but do not rely on masking alone, isolate runners,
limit log retention/access, and add secret canaries and tests that prove one team's
job cannot read another team's credentials.

## Drill 5 — Policy rollout blocks emergency fixes

Pause or narrowly revert the failing policy while preserving essential security
controls. Establish an audited, time-bound break-glass path with accountable approval.
Inspect false-positive scope and policy version. Add test fixtures from representative
workloads, dry-run/shadow evaluation, canary enforcement, owner and remediation text,
exception expiry, and a policy rollback contract.

## Drill 6 — Catalog ownership data is mostly stale

Do not use unreliable metadata for paging or compliance claims. Identify authoritative
sources and lifecycle events, mark confidence/freshness, and ask teams to correct
high-risk services first. Automate reconciliation from repositories, identity, and
runtime where appropriate; require ownership on creation and transfer; alert before
expiry; and measure unknown or unresponsive ownership as operational risk.

## Drill 7 — A cloud quota causes mass provisioning failures

Throttle new requests, prioritize critical operations, show accurate status, and
avoid blind retries. Reconcile partial resources and release unused capacity. Add
quota inventory, demand forecasting, preflight checks, reservations where justified,
bounded retries, regional/account cells, and a failure mode that does not strand
costly resources or falsely report success.

## Drill 8 — Teams fork the platform modules

Inventory forks and understand whether latency, missing features, trust, or version
breakage caused them. Secure high-risk copies and establish support boundaries.
Provide versioned composable modules, extension points, automated upgrades, release
notes, compatibility tests, and contribution paths. Retire forks through value and
migration evidence, not repository policing alone.

## Drill 9 — Platform on-call becomes unsustainable

Stabilize staffing and reduce noisy paging, then classify incidents by platform
defect, dependency, consumer misuse, and support request. Define journey SLOs and
service tiers, improve runbooks and automation, distribute component ownership,
reserve reliability capacity, and adjust scope. A platform cannot scale by turning
every consumer question into a page for one central team.

## Drill 10 — Executive mandates 100% adoption by quarter end

Translate the mandate into business outcomes and risk. Segment consumers, identify
unsupported workloads, and propose staged targets for eligible paths, successful
migrations, supported versions, and retired risk. Show why nominal enrollment can
hide bypass and parallel systems. Escalate capacity and trade-offs, keep governed
exceptions, and make outcome evidence the exit criterion.
