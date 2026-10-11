# Delivery and Software Supply Chain

[← Self-service and control planes](self-service-control-planes.md) · [Next: Security, tenancy, and governance →](security-tenancy-governance.md)

## Source-to-production path

A platform path should connect source policy, review, isolated build, tests, secret
detection, dependency controls, SBOM and provenance, immutable artifacts, signing,
policy, environment promotion, progressive delivery, verification, and rollback.
Reuse versioned components without creating a universal pipeline that fits nothing.

## Trust boundaries

Pull requests and build code are untrusted. Keep production credentials and signing
authority outside user-controlled steps. Use ephemeral workload identity, isolated
runners, least privilege, protected environments, and artifact promotion rather
than rebuilding. Verify provenance and policy at deployment.

## Platform responsibility

The platform owns safe defaults, reusable workflow contracts, evidence interfaces,
and lifecycle. Product teams own application tests, schema compatibility, rollout
health, and service outcomes. Security owns policy intent with engineering partners;
it should not manually approve every low-risk release.

## Change and compatibility

Version pipelines, modules, schemas, and policies. Test consumers against proposed
platform changes, canary across representative teams, and publish migrations.
Database and event changes require expand/contract or another compatible strategy;
rollback is not credible when old code cannot read new data.

## Developer feedback

Make failures specific and actionable at the earliest practical stage. Link policy
denials to owner, rationale, evidence, and remediation. Track false positives,
retries, wait time, and abandonment; a green platform dashboard does not prove a
usable delivery experience.
