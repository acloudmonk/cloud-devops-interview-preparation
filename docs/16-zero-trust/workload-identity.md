# Workload Identity and Service Access

[← Module overview](index.md) · [Module 15: DevSecOps](../15-devsecops/index.md)

Workloads need attributable, scoped, short-lived identity independent of host IP,
shared secret, or developer account. The identity must bind the running workload
to claims that the destination can verify and authorize.

## Identity lifecycle

1. Establish workload identity from a trusted platform or orchestrator.
2. Bind identity to immutable context such as account, namespace, service account,
   deployment environment, repository, or attested workload properties.
3. Exchange or mint audience-bound, short-lived credentials at runtime.
4. Authorize the action at the destination and record subject plus workload context.
5. Rotate trust roots, revoke compromised issuers, and remove identity with workload.

Examples include EC2 instance profiles, ECS task roles, EKS Pod Identity or IRSA,
Azure managed identities and workload identity federation, Google service accounts
with Workload Identity Federation, and SPIFFE identities in heterogeneous estates.

## Common failures

- node or instance identity is unintentionally shared by many workloads;
- tokens have broad audiences, excessive lifetime, or unsafe filesystem exposure;
- any repository, branch, namespace, or service account can assume a sensitive role;
- service identity exists, but the destination grants wildcard actions;
- issuer or signing-key compromise has no rehearsed revocation path;
- sidecars or meshes are treated as proof that application authorization is correct.

## mTLS and service meshes

mTLS can protect transport and authenticate certificate possession. It does not
prove that a workload image is safe, that its current request is authorized, or
that tenant and business rules were enforced. A mesh can standardize certificate
rotation and coarse service policy; applications or gateways still enforce
resource- and action-level authorization.

## Egress and dependency trust

Authorize outbound destinations, DNS behavior, protocols, and sensitive data
movement. Validate server identity; use private endpoints where they improve
exposure and policy, but do not equate "private" with authorized. Inventory
service dependencies so a compromised workload cannot freely discover and call
the environment.

## Interview test

Trace one call: which runtime receives which credential, from which issuer, with
which audience and lifetime, over which path, evaluated by which policy, logged
where, and revoked how? Product names without that chain are not an architecture.

Return to the [module overview](index.md) when ready to continue.
