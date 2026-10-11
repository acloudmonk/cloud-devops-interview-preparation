# Organizations, Landing Zones, and Governance

[← Global infrastructure](global-infrastructure.md) · [Next: Identity and security →](identity-security.md)

## Use accounts as strong boundaries

AWS accounts provide isolation for resources, identities, quotas, billing, and blast
radius. Separate production from nonproduction and distinguish security, log archive,
network, infrastructure, deployment, sandbox, and workload concerns as justified.
Account structure should follow policy and operating needs, not the reporting chart.

## Design the organization

Protect the Organizations management account and keep workloads out of it. Group
accounts into OUs with similar policy needs. Use delegated administrators, centralized
evidence, consolidated billing, and account vending. Test organization-wide policy and
automation changes before production application.

## Understand guardrails

Service control policies set maximum available permissions; they do not grant access.
Combine them with IAM identity policies, resource policies, permissions boundaries,
session policies, and service-specific controls. Preventive controls reduce unsafe
possibility; detective and proactive controls provide evidence and feedback.

## Treat the landing zone as a product

AWS Control Tower can establish and govern a multi-account environment, but teams still
own OU/account design, identity, network, keys, logs, security services, backup,
delivery, tagging, budgets, quotas, exceptions, lifecycle, and support. Provide paved
paths, self-service, versions, service levels, adoption metrics, and feedback.

## Govern exceptions and lifecycle

An exception needs scope, rationale, risk owner, compensating control, evidence,
expiry, and removal plan. Account closure must address data retention, keys, backups,
legal hold, ownership, billing, dependencies, and recovery periods. Governance should
enable safe speed, not create undocumented bypasses.
