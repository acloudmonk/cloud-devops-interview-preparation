# Enterprise Platform and Shared Services

[← Organizations and governance](multi-account-governance.md) · [Next: Identity and security →](identity-security.md)

## Treat the AWS platform as a product

The platform should provide safe, supported paths for account creation, identity,
networking, DNS, certificates, keys, logs, security findings, backup, delivery,
observability, cost allocation, quota requests, and incident access. Define consumers,
owners, service levels, versions, support, adoption, feedback, and retirement. A landing
zone without an operating platform becomes a one-time installation that drifts.

## Automate account lifecycle

Use Control Tower Account Factory, Account Factory for Terraform, or governed custom
automation as organizational needs justify. Intake should capture owner, environment,
data classification, network, Region, cost center, controls, and lifecycle. Apply
baselines idempotently, test policy changes in staging, detect drift, and define safe
update, quarantine, suspension, and closure paths.

## Deploy organization-wide capabilities

CloudFormation StackSets can deploy stacks across accounts and Regions; delegated
administration reduces management-account use. CloudFormation and CDK are AWS-native
infrastructure options, while other IaC tools may remain appropriate. Protect execution
roles, pin and review artifacts, stage broad changes, bound concurrency and failure
tolerance, and retain a recovery path when the central pipeline is unavailable.

## Share only what should be shared

AWS Resource Access Manager can share supported resources across accounts; Service
Catalog can publish governed products. Common services may include DNS, transit,
inspection, directories, artifact repositories, observability, security, and backup.
For each shared service define tenancy, authorization, routing, quota, cost allocation,
change compatibility, SLO, degraded behavior, recovery, and consumer escape path.

## Choose centralization deliberately

Centralize capabilities whose consistency, risk, or economics benefit the enterprise;
federate workload decisions that product teams can safely own. Excessive centralization
creates queues and large blast radii, while uncontrolled duplication creates drift.
Use interfaces and policy boundaries so central teams provide enablement rather than
manual tickets.

## Integrate delivery and operations

Separate build, deployment, and runtime identities; promote immutable artifacts rather
than rebuilding them per account. Provide standard telemetry, runbooks, backup, patch,
vulnerability, change, and incident integrations. Measure account/product lead time,
platform availability, adoption, exceptions, failed changes, consumer satisfaction,
and toil—not resource counts alone.
