# Terraform and Ansible Boundaries

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Terraform/OpenTofu and Ansible can complement each other, but sequential tools
do not automatically create clean ownership. The boundary must identify the
authoritative system for every resource and mutable field.

## Default responsibility split

| Concern | Primary owner |
| --- | --- |
| VPC, subnet, IAM role, instance, load balancer | Terraform/OpenTofu |
| Base image artifact | Image pipeline |
| First-boot identity and minimal bootstrap | Image/cloud-init/managed bootstrap |
| Host package, file, service, and configuration | Ansible when mutable configuration is justified |
| Secret value | Secret manager; Ansible may retrieve and place it temporarily |
| Application release | Deployment platform or pipeline |
| Continuous compliance | Policy/configuration service with explicit remediation owner |

This is a starting point, not a law. The invariant is single ownership with a
documented interface.

## Safer hand-offs

Prefer stable discovery contracts over generated static inventory. Terraform can
create instances and governed tags; an inventory plugin discovers those tags.
For explicit outputs, publish only non-secret identifiers through a versioned,
access-controlled interface. Do not parse Terraform state broadly from Ansible.

Separate provisioning from configuration jobs. A Terraform provisioner that
runs Ansible couples retries, state, connectivity, and failure recovery. Use a
workflow or event to start configuration after infrastructure readiness, with
independent status and rerun semantics.

## Avoid overlapping mutation

Common conflicts include security-group rules, IAM policies, instance tags,
cloud-init files, service configuration, and autoscaling properties. If Ansible
changes a field Terraform owns, the next plan reports drift or reverses it. Move
ownership deliberately and prove a no-surprise transition.

## Failure choreography

Define what happens when infrastructure succeeds but configuration fails:

1. mark the instance or environment unready;
2. keep it out of production traffic;
3. preserve both tools' evidence;
4. retry only idempotent configuration with the same content version;
5. replace the node if its state is uncertain;
6. reconcile inventory and infrastructure after recovery.

Do not destroy healthy infrastructure automatically merely because a transient
configuration dependency failed.

## Interview decision statement

"Terraform owns durable cloud-resource lifecycle and Ansible owns approved
mutable host configuration. They exchange stable identifiers and readiness
events, use separate credentials and evidence, and never manage the same field."

Return to the [module overview](index.md) when ready to continue.
