# Ansible Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Answer each in 20–40 seconds. Add one trade-off or failure mode.

## Foundations

1. **What makes Ansible agentless?** The controller normally uses existing transports and temporary modules rather than a resident Ansible agent.
2. **What is convergence?** Moving supported starting states toward one declared outcome.
3. **Idempotency versus convergence?** Idempotency means repeat causes no unintended change; convergence also covers reaching intent from varied starts.
4. **When should Ansible not own a resource?** When another system already owns its durable lifecycle or a managed/immutable option is safer.
5. **Module versus command?** A module exposes state semantics; a command needs explicit discovery, change, failure, and recovery logic.
6. **Push-model benefit?** Central scheduling, policy, and evidence.
7. **Push-model risk?** Reachability, controller capacity, and concentrated credentials.
8. **Why is YAML validity insufficient?** It proves syntax, not target safety, convergence, recovery, or outcome.
9. **What is a play?** A mapping of targets to ordered tasks, roles, variables, and execution controls.
10. **What is a handler?** A notified task that performs a dependent action only when relevant change occurs.

## Inventory and data

1. **Why is inventory a security boundary?** It determines where privileged code can execute.
2. **Static versus dynamic inventory?** Curated stable list versus API-discovered elastic targets.
3. **Why govern targeting tags?** Tag writers could otherwise grant machines access to privileged automation.
4. **What should a target preview show?** Source, filters, snapshot time, groups, count, exclusions, and sample identities.
5. **Why avoid arbitrary extra variables?** Their high precedence can bypass safe configuration and authority boundaries.
6. **What are facts?** Observed target data gathered or supplied to a run.
7. **Fact-cache risk?** Stale or sensitive data may drive incorrect decisions or leak.
8. **How do you debug precedence?** List every source and load order for the affected host, then remove duplicate ownership.
9. **Why namespace role variables?** To reduce collisions and make ownership explicit.
10. **Why prefer stable cloud IDs?** Hostnames and instances can be replaced or reused in elastic fleets.

## Execution and reuse

1. **Role contract essentials?** Purpose, inputs, defaults, validation, platforms, outcomes, owner, version, tests, and migration.
2. **What is a collection?** A namespaced package for roles, modules, plugins, playbooks, and documentation.
3. **Why use fully qualified collection names?** To make implementation origin explicit and avoid name collisions.
4. **What is an execution environment?** A versioned image containing Ansible and its runtime dependencies.
5. **AWX versus Automation Controller?** AWX is upstream; Automation Controller is the supported Red Hat product capability.
6. **What does a job template bind?** Content, inventory, credentials, runtime, parameters, limits, and execution policy.
7. **Why isolate runners?** To contain credentials, network reach, dependency risk, and resource contention.
8. **How does `serial` help?** It limits each batch and therefore the immediate failure radius.
9. **Why can high forks be harmful?** They can overload controller, network, repositories, APIs, or targets.
10. **Why avoid deep includes?** They hide order, inputs, and failure behavior.

## Security and assurance

1. **What does Ansible Vault protect?** Encrypted data at rest, subject to vault-key security.
2. **What does `no_log` not protect?** Target files, process memory, external systems, or every indirect callback/artifact path.
3. **Why avoid global admin credentials?** A controller or content compromise becomes fleet-wide compromise.
4. **How should jobs authenticate to AWS?** With short-lived, scoped role credentials rather than stored access keys.
5. **SSH host-key checking value?** It helps authenticate the target and resist machine impersonation.
6. **What does SSM connectivity trade?** Inbound SSH for IAM, agent, plugin, endpoint, session, and transfer dependencies.
7. **What does check mode prove?** Only the supported modules' forecast under current observations.
8. **What is a convergence test?** A second run that reports no unintended changes.
9. **Why test negative paths?** Safe stopping and recovery matter when dependencies or inputs fail.
10. **Why pin collections?** To make behavior reproducible and upgrades reviewable.

## Architecture and operations

1. **Terraform/Ansible default boundary?** Terraform owns cloud-resource lifecycle; Ansible owns justified mutable host configuration.
2. **Why avoid Terraform provisioners for Ansible?** They couple state reconciliation to remote execution and retries.
3. **Safer hand-off?** Stable identifiers or governed tags plus an independent readiness-triggered job.
4. **Can both tools manage tags?** Not the same mutable tag; establish field-level single ownership.
5. **How should rolling change be verified?** Readiness, application transaction, security state, telemetry, and observation window.
6. **First response to wrong targets?** Stop new batches, preserve snapshot/evidence, and determine completed mutations.
7. **What is an unreachable host?** Connection failed before normal task execution; it differs from a task failure.
8. **Why can a green run be unsafe?** Rescued/ignored failures or missing outcome checks may hide broken service.
9. **Key platform measures?** Success, unreachable, convergence, recovery, queue, inventory anomaly, manual effort, and impact.
10. **Architect's closing recommendation?** Bound ownership, targets, identity, runtime, rollout, recovery, and measurable outcomes.

Return to the [module overview](index.md) when ready to continue.
