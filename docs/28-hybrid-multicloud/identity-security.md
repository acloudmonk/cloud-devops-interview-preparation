# Identity, Security, and Trust

[← Module overview](index.md) · [Connectivity and DNS](connectivity-dns.md)

Federate identities and policy intent where useful, but preserve provider-native
authorization and independent recovery. Network reachability is not authorization.

## Identity layers

- Workforce identity: central IdP, federation, phishing-resistant authentication,
  conditional access, lifecycle, privileged access, and break-glass recovery.
- Workload identity: short-lived federation, service identities, audience/scope,
  rotation, attestation, and no shared long-lived keys.
- Customer identity: consistent user journey with data, residency, and failover rules.
- Machine/edge identity: device enrollment, hardware roots where justified, offline
  policy, revocation, and fleet lifecycle.

Map identities to AWS IAM, Microsoft Entra/Azure RBAC, Google Cloud IAM, Kubernetes,
SaaS, and on-premises directories without assuming roles are semantically equivalent.
Keep authorization least-privileged in each target environment.

## Trust boundaries

Document federation issuers, token paths, certificate authorities, secrets, key
management, administrative planes, CI/CD, artifact trust, and logging. Separate
production, security, backup, and platform administration where correlated
credentials would defeat resilience.

## Security operations

Normalize high-value events into a common incident process while retaining raw
provider context. Align classification, vulnerability handling, threat modeling,
network policy intent, encryption, key ownership, and evidence retention. Do not
force one lowest-common-denominator control when providers offer stronger mechanisms.

## Compromise and recovery

Test IdP loss, federation misconfiguration, certificate expiry, revoked connectivity,
cloud-admin compromise, and CI/CD compromise. Maintain constrained, monitored,
time-limited emergency access in each environment and rehearse recovery without
making the central identity plane an unrecoverable single point.

Return to the [module overview](index.md) when ready to continue.
