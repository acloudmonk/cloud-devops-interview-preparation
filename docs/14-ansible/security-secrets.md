# Security, Secrets, and Trust

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Ansible can reach many systems with privileged authority, so compromise of its
content, controller, runner, inventory, or credentials can become a fleet-wide
incident. Security begins with smaller trust and target boundaries.

## Identity and access

- use individual SSO identities for humans and short-lived workload identity for jobs;
- separate source-read, inventory-read, target-connect, cloud-API, and escalation rights;
- scope credentials by environment, account, service, and job purpose;
- require approval for high-risk templates and production host limits;
- prohibit shared static administrator keys wherever a brokered path exists.

On targets, start unprivileged and use narrowly allowed `become` operations.
Avoid passwordless unrestricted sudo for a common automation account.

## Transport trust

Verify SSH host keys, WinRM certificates, controller TLS, proxy boundaries, and
private API endpoints. Disabling host-key checking solves symptoms by accepting
machine impersonation risk. Systems Manager can remove inbound SSH exposure, but
introduces IAM, agent, plugin, S3-transfer, session, and regional dependencies.

## Secrets

Ansible Vault encrypts data at rest in a file; it does not by itself solve secret
distribution, authorization, rotation, plaintext in memory, logs, templates, or
the vault-password lifecycle. Prefer external secret systems and lookup plugins
when runtime retrieval and central policy are required.

Secret controls include:

- encrypted source and artifact storage;
- short-lived retrieval identity and least privilege;
- `no_log` for tasks that may expose values;
- safe diff, callback, fact-cache, and job-output policy;
- rotation and revocation testing;
- redaction tests with failure paths, not only successful output.

`no_log` reduces display; it is not a substitute for safe module design or log
access control.

## Content supply chain

Pin and review collections, roles, execution images, and source revisions. Scan
dependencies, restrict Galaxy or registry sources, sign promoted artifacts where
supported, and rebuild on vulnerability or trust changes. A module executes with
the job's authority; treat it like application code.

## Threat scenarios

Consider a malicious pull request, compromised collection, poisoned execution
image, inventory tag manipulation, stolen controller credential, unsafe survey
input, template injection, leaked job output, and controller-to-target pivot.
For each, define prevention, detection, containment, credential revocation,
evidence preservation, and reconciliation.

Return to the [module overview](index.md) when ready to continue.
