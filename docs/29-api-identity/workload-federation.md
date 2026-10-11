# Workload Identity and Federation

[← Authorization](authorization-policy.md) · [Next: Security →](security-threats.md)

Workloads need identity without copying long-lived secrets into source, pipelines,
images, hosts, or multiple clouds.

## Preferred chain

1. Platform authenticates workload from controlled runtime attributes.
2. Workload receives a short-lived, audience-bound assertion or credential.
3. Target trusts exact issuer, subject, audience, and approved context.
4. Authorization grants only required actions and resources.
5. Issue, exchange, decision, use, and denial create correlated evidence.

On AWS use IAM roles for compute, EKS service-account federation, Roles Anywhere
where certificates are appropriate, and scoped cross-account trust. Azure managed
identities/workload federation and Google Workload Identity Federation provide
analogous flows with different claims and policy semantics.

## Trust design

Never trust an entire repository, cluster, account, or tenant when a narrower subject
is available. Bind repository/workflow/environment, Kubernetes namespace/service
account, account/project, audience, and deployment authority as supported. Avoid
wildcard subjects, reusable CI credentials, and one role shared across stages.

## Rotation and revocation reality

Short lifetime limits exposure but does not replace containment. Stop the issuer or
subject, revoke trust, block downstream use, rotate signing material, enumerate
actions, and rebuild affected workloads. Plan key overlap, discovery cache, clock
skew, JSON Web Key Set failure, and emergency access.

## SPIFFE and service identity

SPIFFE/SPIRE can issue portable workload identities, but introduces trust-domain,
attestation, server/agent, federation, and recovery operations. Service meshes can
automate mutual TLS; they do not decide business authorization or secure all egress.

## Proof

Demonstrate that a credential cannot be replayed from another workload, environment,
audience, or tenant, and that identity-plane loss has an explicit safe mode.
