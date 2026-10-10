# IaC and Cloud Security

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

IaC security combines static intent checks, evaluated-change policy, cloud API
controls, deployed-state observation, and ownership-aware remediation.

## Assurance layers

- **Source scanning** detects risky configuration patterns early.
- **Plan/change analysis** evaluates resolved actions, values, and replacements.
- **Policy as code** expresses organizational decisions and exceptions.
- **Cloud preventive controls** constrain what identities and organizations permit.
- **Post-deployment posture** finds drift, unmanaged assets, and runtime exposure.
- **Threat detection** identifies suspicious behavior after deployment.

No layer is complete. Static checks may not know computed values; cloud posture may
arrive after exposure; preventive policy can block recovery if poorly designed.

## Policy design

Tie rules to threats such as public storage, broad IAM, missing encryption,
unrestricted ingress, weak logging, risky Kubernetes privileges, or unapproved
regions. Test positive, negative, edge, upgrade, and exception cases. Assign an
owner and version the rule with the platform it governs.

## Remediation ownership

Do not let a posture tool mutate Terraform-owned resources without coordination.
For non-urgent findings, change the authoritative source and apply through the
normal workflow. For active exposure, contain through a bounded emergency action,
record ownership and expiry, then reconcile source and state.

## AWS governance

Use Organizations and account boundaries, SCPs as coarse preventive guardrails,
IAM Access Analyzer, Config and Security Hub findings, CloudTrail, GuardDuty,
Inspector, KMS, and service-specific controls. Centralize visibility while keeping
remediation ownership with the accountable workload/platform team.

On Azure, translate to management groups, Azure Policy, Defender for Cloud, and
activity logs. On GCP, use organization/folder/project hierarchy, organization
policy, IAM analysis, Security Command Center, audit logs, and service controls.

## Exception contract

An exception includes rule, resource, owner, business reason, risk, compensating
control, approval, evidence, expiry, and remediation plan. Automatically recheck
expiry; an exception registry that never closes becomes hidden policy.

Return to the [module overview](index.md) when ready to continue.
