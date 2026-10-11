# Ten-Minute GCP Architecture Review

[← Advanced drills](scenario-drills.md) · [Next: Rapid fire →](rapid-fire.md)

## 0:00–1:00 — Context

State users, journeys, scale, data, regulation, SLOs, RTO/RPO, constraints, and assumptions.

## 1:00–2:30 — Foundation

Explain organization, folders, projects, billing, ownership, Organization Policy,
identity federation, Shared VPC, and project vending.

## 2:30–5:00 — Workload design

Walk ingress and DNS, runtime, authoritative data, integration, analytics, and operator
paths. Name service scope and why each choice beats one credible alternative.

## 5:00–7:00 — Failure and recovery

Inject zone loss, region loss, identity/key failure, quota, downstream saturation, and
data corruption. State degradation, RTO/RPO, restore, reconciliation, and evidence.

## 7:00–8:30 — Security and operations

Cover least privilege, federation, secrets/keys, perimeter, supply chain, telemetry,
SLOs, incident access, runbooks, and ownership.

## 8:30–10:00 — Economics and decisions

Give demand/cost drivers, failure headroom, quotas, unit metric, top risks, assumptions,
validation plan, and exit triggers. Close with the decision—not another service list.
