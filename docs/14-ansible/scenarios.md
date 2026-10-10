# Scenario Questions and Model Answers

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Answer each question aloud before reading the model answer. State assumptions,
failure radius, trade-offs, verification, and recovery.

## 1. A playbook always reports changed

**Model answer:** Identify the first noisy task and compare pre/post state. Common
causes are commands, timestamps, templates with unstable ordering, and inaccurate
`changed_when`. Replace commands with stateful modules or add guarded discovery
and explicit change semantics. Test a clean run, a mutation run, and a second run;
do not simply suppress `changed` because handlers and reporting depend on it.

## 2. Dynamic inventory selects production unexpectedly

**Model answer:** Stop the run, preserve the resolved inventory and source
filters, and confirm whether any mutation occurred. Treat targeting tags as
governed data, separate discovery from authorization, require account/environment
filters plus a production limit, and alert on host-count changes. Reconcile
affected hosts and correct the source contract before retrying.

## 3. Thousands of hosts need a package update

**Model answer:** Segment by service, failure domain, OS, and criticality. Pin the
package and repository, preflight capacity and recovery, canary representative
hosts, then use bounded `serial` batches with health checks and stop criteria.
Do not maximize forks blindly; protect repositories, controllers, networks, and
downstream services. Verify behavior and second-run convergence.

## 4. The team stores secrets in Ansible Vault

**Model answer:** Vault is valid encryption at rest, but assess key custody,
rotation, access, plaintext exposure, logs, and deployment. For centrally managed
dynamic secrets, prefer runtime lookup from a secret manager with short-lived
identity. Keep `no_log`, diff, callback, artifact, and failure paths safe, then
test revocation and leakage scenarios.

## 5. A handler fails after configuration changed

**Model answer:** Stop expansion and identify hosts with changed files, notified
handlers, and failed service state. Restore the known-good version or fix forward
on the smallest batch, then verify service outcome. Improve pre-validation,
template validation, handler observability, rescue logic, and canary gates; a file
change is not complete until the dependent service is healthy.

## 6. Terraform should run Ansible through a provisioner

**Model answer:** Avoid tight coupling. Terraform provisioners mix stateful
infrastructure reconciliation with remote connectivity and configuration retries.
Let Terraform publish stable identifiers/readiness; a separate workflow resolves
inventory and starts a versioned, rerunnable Ansible job. Define ownership,
credentials, evidence, failure status, and reconciliation independently.

## 7. Developers request arbitrary extra variables in production

**Model answer:** Extra variables have strong precedence and can bypass safe
defaults. Expose a small validated survey or API schema, authorize values by job
template, protect target and privilege variables, and log the approved inputs.
Use separate templates for materially different authority rather than one
universal playbook controlled by free-form input.

## 8. SSH access is prohibited in AWS

**Model answer:** Evaluate the `amazon.aws.aws_ssm` connection. Confirm SSM Agent,
instance profile, controller role, Session Manager plugin, regional endpoints,
S3-transfer requirements, encryption, and logging. Test failure and throttling.
The design removes inbound SSH but does not remove credentials, dependencies, or
target-side privilege controls.

## 9. Check mode is clean, but production changes fail

**Model answer:** Check mode is not a transactional plan. Identify unsupported or
skipped modules, missing registered results, external dependencies, and drift
between preview and run. Add representative integration tests, preflight asserts,
saved content/runtime versions, a canary, outcome checks, and explicit recovery.

## 10. One global automation credential is proposed

**Model answer:** Reject the unbounded blast radius. Separate inventory-read,
cloud-mutation, target-connect, and escalation identities by environment and
service. Use short-lived federation, controller RBAC, approved templates, and
runner isolation. Design rapid revocation and correlate controller, cloud, and
target audit trails.

## 11. Variable precedence produces the wrong port

**Model answer:** Trace every definition for the affected host across role
defaults/vars, inventory sources, group/host variables, play data, surveys, and
extra variables. Inspect group and inventory load order. Remove duplicate
authority and publish the intended override contract instead of adding another
higher-precedence value.

## 12. A third-party collection must be upgraded

**Model answer:** Treat it as an executable dependency change. Review release and
security notes, pin the candidate with `ansible-core` and execution-environment
dependencies, test representative targets and negative paths, canary, then roll
out in waves. Retain the previous signed environment and define rollback and
credential-containment actions.

## 13. Ansible and Terraform both update EC2 tags

**Model answer:** Establish field-level ownership. Stop one writer, inventory the
desired and actual values, move the tag declaration to the authoritative system,
and verify both a no-surprise Terraform plan and an unchanged Ansible run. Use
read-only discovery across the boundary; never normalize the conflict with
reciprocal ignores.

## 14. Facts are slow across the fleet

**Model answer:** Measure which facts are used, gather a subset or disable global
gathering, and cache only with an explicit TTL and invalidation model. Do not use
stale facts for authorization or critical decisions. Partition runs, tune forks
against downstream capacity, and keep outcome verification independent of fact
collection.

## 15. A brownfield estate has hundreds of laptop playbooks

**Model answer:** Inventory content, credentials, targets, owners, frequency, and
risk. Freeze the most dangerous patterns, establish controller and execution
environment foundations, then migrate one service through linting, idempotency,
tests, scoped identity, and evidence. Expand by risk and adoption metrics; keep a
time-bound exception path and retire shared keys and local production execution.

Return to the [module overview](index.md) when ready to continue.
