# Pipeline, Identity, and Build Security

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

The build system converts source into trusted artifacts with powerful credentials.
If it is compromised, downstream scanning of the resulting artifact may not reveal
malicious behavior inserted during the build.

## Trust boundaries

Separate untrusted pull-request evaluation from protected release builds. Review
repository permissions, workflow definitions, actions/plugins, runner images,
caches, dependencies, secrets, artifact stores, signing identities, network
egress, logs, and deployment credentials.

## Identity design

- federate workloads to short-lived cloud roles using verifiable job claims;
- bind repository, branch/tag, workflow, environment, and audience where supported;
- separate build, publish, sign, deploy, and administrative authority;
- issue credentials only after policy and approval gates that require them;
- prevent untrusted code from reaching production secrets or persistent runners.

## Runner isolation

Prefer ephemeral clean runners for sensitive builds. Destroy compute and workspace
after the job; constrain network egress; isolate tenants and trust levels; patch
base images; and prevent privileged container or host-socket exposure unless a
reviewed design requires it. Treat caches as untrusted inputs keyed by identity
and immutable content.

## Reproducibility and hermeticity

Pin toolchains and inputs, record digests, minimize network dependency, and make
build steps deterministic where practical. Reproducible builds help comparison;
hermetic builds constrain undeclared inputs. Neither alone proves source review,
builder integrity, or authorization.

## Build incident response

Stop releases, isolate runners, revoke credentials and signing identities,
preserve workflow logs/images/caches, identify artifacts produced in the exposure
window, quarantine or block them, rebuild on a trusted platform, verify consumers,
and communicate downstream impact. Recovery includes restoring the root of trust,
not merely rerunning the job.

Return to the [module overview](index.md) when ready to continue.
