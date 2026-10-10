# Testing, Policy, and Security

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

No single check proves an infrastructure change safe. Layer fast author feedback,
configuration tests, plan-aware policy, controlled integration evidence, and runtime
verification.

## Assurance layers

| Layer | Finds | Does not prove |
| --- | --- | --- |
| Format and validate | syntax, internal consistency | provider/API outcome |
| Static analysis | known insecure or inconsistent patterns | final evaluated plan |
| Module tests | contract and selected behavior | production account behavior |
| Plan review | target-specific actions and replacements | successful or healthy runtime |
| Policy evaluation | codified organizational constraints | all context or business intent |
| Integration test | real provider/module interaction | every scale/failure condition |
| Post-apply verification | deployed control and service outcome | future drift or resilience |

## Test strategy

- Unit-test expressions, validations, outputs, and module behavior with mocks where useful.
- Run integration tests in isolated accounts/projects with bounded cost and cleanup.
- Test upgrades from supported module/provider versions and imported brownfield state.
- Include negative tests: invalid inputs, denied policy, unavailable dependencies, and
  deletion protection.
- Test architecture outcomes using cloud-native queries, not only Terraform outputs.

## Policy as code

Evaluate the plan representation when decisions depend on resolved resource actions.
Use static configuration policy for rules that do not require a plan. Start new controls
in advisory mode, measure violations, remediate the paved path, then enforce by risk tier.

Every rule needs an owner, rationale, tests, severity, remediation, exception mechanism,
expiry, and version. Fail-open/fail-closed behavior must be explicit for policy service
outages. Policy cannot replace IAM, service control policies, Azure Policy, organization
policy, or resource-native safeguards.

## Secret handling

- Never commit credentials or secret variable files.
- Fetch secrets at execution time through workload identity and an approved manager.
- Understand that secret inputs and generated values can persist in state and plan files.
- Restrict plan/state artifacts, logs, crash files, caches, and support bundles.
- Prefer references or service integrations that avoid returning plaintext where possible.
- Rotate after suspected exposure and investigate historical artifacts and replicas.

## Supply-chain controls

Pin tool, provider, module, action, and policy versions. Verify checksums/signatures where
supported, review lock-file changes, restrict module sources, scan artifacts, inventory
dependencies, and define emergency upgrade procedures. A trusted provider can execute
with the full authority of the pipeline role.

## Destructive-change controls

Combine plan visibility, explicit deletion/replacement thresholds, additional approval
for protected resources, cloud deletion protection, backups, maintenance windows, and
post-change verification. Do not parse colored console text as the only policy input.

## Exceptions

An exception records scope, justification, compensating control, approver, owner, and
expiry. Store it as reviewable configuration and report active/expired exceptions. A
permanent ignore rule is undocumented policy abandonment.

## Security review questions

1. Can untrusted code obtain backend or apply credentials?
2. Can a reviewer approve one plan while another plan is applied?
3. Which secrets are stored in state, plans, logs, and caches?
4. Can a compromised provider/module affect other roots or accounts?
5. Which controls still hold if the IaC runner or policy service is unavailable?
