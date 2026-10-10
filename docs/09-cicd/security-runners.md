# Pipeline Security and Runner Trust

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

A delivery pipeline is a privileged production system. Treat workflow definitions,
dependencies, runners, credentials, artifacts, and approvals as one trust chain.

## Threat model first

Ask four questions before selecting controls:

1. Who can change executable workflow code?
2. Which events can cause untrusted code to run?
3. What credentials, networks, caches, and artifacts can that run reach?
4. What evidence proves the published artifact came from the reviewed source?

Important boundaries include pull requests from forks, reusable workflows,
third-party actions, container images, package scripts, self-hosted runners, and
deployment environments. A green job proves only that the configured job ran; it
does not prove the configuration or execution environment was trustworthy.

## Identity and cloud access

For AWS, prefer GitHub Actions OpenID Connect (OIDC) federation to stored IAM
access keys. The workflow receives a short-lived identity token, AWS validates its
issuer and claims, and AWS STS returns temporary role credentials.

The role trust policy should constrain repository, organization, branch/tag or
protected environment claims as narrowly as practical. Separate build, test,
staging, and production roles; grant each only the actions and resources required.
CloudTrail should make role assumptions and deployment calls attributable.

Equivalent patterns are workload identity federation on Google Cloud and
federated workload identities/service connections on Azure. The invariant is
short-lived, audience-bound, policy-constrained identity—not a particular vendor.

## Event and permission safety

- Default the workflow token to read-only and grant permissions per job.
- Treat `pull_request_target` and equivalent privileged base-context events as
  dangerous when they check out or execute fork-controlled code.
- Protect workflow files and deployment configuration with ownership and review.
- Bind production credentials to protected environments, not ordinary CI jobs.
- Require approval after immutable artifact creation, before production use.
- Keep secrets out of command arguments, debug output, test fixtures, and artifacts.

Masking is a last line of defence, not proof that a secret did not escape. Rotate
an exposed value and investigate logs, artifacts, caches, and downstream systems.

## Third-party and dependency controls

Pin third-party actions to reviewed immutable commit SHAs and use an update process
that re-reviews changes. Prefer a small approved catalog of reusable workflows.
Verify base images and tools, lock dependencies, scan workflow changes, generate an
SBOM, and preserve provenance. Tags and mutable image labels are convenient names,
not immutable evidence.

## Runner models

| Model | Strength | Principal risk | Suitable use |
| --- | --- | --- | --- |
| Hosted ephemeral | Clean instance and low maintenance | Limited private-network/custom-hardware access | Most untrusted build and test work |
| Ephemeral self-hosted | Custom network/tools with single-job lifecycle | Image hygiene, orchestration, and cloud permissions | Controlled private workloads |
| Persistent self-hosted | Fast warm state and specialist hardware | Cross-job persistence and credential/cache theft | Only with strong isolation and trusted workloads |

Separate trusted and untrusted workloads into different runner groups, accounts,
networks, and roles. Prefer disposable runners; deny inbound administration where
possible; patch the image; restrict egress; and monitor unexpected processes,
network calls, or filesystem persistence.

## Production protection

Use branch/ruleset enforcement, required checks, environment protection,
least-privilege deployment roles, immutable artifacts, and an auditable break-glass
procedure. A human approval is useful only when the approver sees the artifact
identity, evidence, intended target, change risk, and current system health.

## Interview test

A strong answer traces one attacker-controlled input through execution, identity,
artifact publication, and deployment. It distinguishes prevention, detection,
containment, recovery, and evidence rather than saying merely “store secrets safely.”
