# Platforms, Portability, and Delivery

[← Module overview](index.md) · [Data and integration](data-integration.md)

Portability is a spectrum and a business capability, not a binary property. Define
what must move, between which targets, within what time, with which acceptable
redesign, and why.

## Portability layers

| Layer | Typical mechanism | Remaining coupling |
| --- | --- | --- |
| Source and build | Git, open formats, reproducible builds | CI identity, runners, policies |
| Artifact | OCI images, signed packages, SBOM/provenance | registry, architecture, runtime assumptions |
| Infrastructure | Terraform/OpenTofu, provider modules | provider resource semantics and state |
| Workload | Kubernetes or common runtime contracts | storage, ingress, IAM, operators, add-ons |
| Data | open schemas/export and migration tools | consistency, scale, managed features |
| Operations | common SLOs, OpenTelemetry, runbook model | provider APIs, events, incident tooling |

Do not hide provider differences behind a universal abstraction that prevents teams
from using valuable capabilities. Standardize interfaces and governance; allow
provider-specific implementation behind owned platform products.

## Delivery model

Use a common source-of-truth and policy intent with environment-specific pipelines,
credentials, tests, and rollout. Sign and replicate artifacts; make configuration,
secrets, feature flags, schemas, and dependencies explicit. Test provider quotas,
API differences, rollback, and partial cross-environment release.

## Kubernetes reality

Kubernetes improves workload API consistency but not identity, network, load
balancing, storage, database, observability, upgrades, node supply, or support parity.
Operate multiple clusters only with fleet lifecycle, policy, version, add-on,
capacity, and incident ownership.

## Portability evidence

Run build-from-source, restore, deployment, data migration, traffic, rollback, and
operator exercises in the target environment. Measure elapsed time, manual work,
feature loss, data loss, performance, cost, and skill gaps. Documentation alone is
not portability.

Return to the [module overview](index.md) when ready to continue.
