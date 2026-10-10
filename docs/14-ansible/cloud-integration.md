# AWS and Multi-Cloud Integration

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Cloud integration has two distinct paths: modules call cloud control-plane APIs,
while connection plugins execute against hosts. Keep their identities,
networking, evidence, and ownership separate.

## AWS reference pattern

Use an `amazon.aws.aws_ec2` inventory source filtered by approved accounts,
regions, running state, and managed tags. Construct groups from normalized tags,
but govern the tags that grant targeting. Assume a short-lived role for discovery
and a separately scoped role for cloud mutations.

For host execution, compare:

- **SSH through a controlled path** — familiar and efficient, but requires key,
  bastion, security-group, host-key, and rotation management;
- **AWS Systems Manager connection** — avoids inbound SSH, but depends on SSM
  Agent, instance role, controller IAM, Session Manager plugin, network endpoints,
  and—for the Ansible plugin—an S3 transfer path.

Use VPC endpoints where isolation requires them. Log CloudTrail, controller jobs,
SSM sessions where applicable, and target-side privilege events.

## Elastic-fleet concerns

Inventory changes during a run. Pin or record the resolved snapshot, identify
hosts by stable cloud identifiers, tolerate legitimate termination, and avoid
reusing hostnames as durable identity. Design autoscaling images and bootstrap so
new instances do not depend on a slow fleet-wide configuration run.

## Azure translation

Translate AWS accounts and tags to subscriptions/resource groups and tags. Use
the `azure.azcollection` inventory and modules, workload or managed identity,
and appropriate SSH/WinRM or managed connectivity. Separate Azure control-plane
permissions from guest operating-system authority.

## Google Cloud translation

Translate to organizations, folders, projects, zones, labels, and the
`google.cloud` collection. Prefer service-account impersonation and OS Login or
IAP-aligned access rather than exported long-lived keys. Bound discovery and
mutation to approved projects.

## Cloud API automation

Ansible modules can create cloud resources, but decide ownership before doing so.
Use Ansible for orchestrated API actions when sequencing and operational context
matter; use Terraform/OpenTofu for durable infrastructure lifecycle. Never let
both tools continuously manage the same mutable field.

## Selection questions

Ask whether the target is a VM at all, whether a managed patch/configuration
service meets the requirement, how private connectivity works, which identity
performs discovery versus mutation, how throttling is handled, and what happens
when a region or control-plane API is unavailable.

Return to the [module overview](index.md) when ready to continue.
