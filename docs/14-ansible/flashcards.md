# Ansible Active-Recall Flashcards

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Cover the answer column and explain each prompt with one failure mode.

| Prompt | Answer cue |
| --- | --- |
| Six-part model | intent → targets → data → content → execution → verified outcome |
| Agentless caveat | no resident Ansible agent; controller, transport, runtime, identity, and evidence still exist |
| Idempotency | repeated execution produces no unintended change when intent is already satisfied |
| Convergence | supported starting states move toward one declared outcome |
| Inventory boundary | discovery plus grouping plus authorized resolved target set |
| Tag risk | a tag used for privileged targeting must have governed writers and independent constraints |
| Variable discipline | one owner, namespaced inputs, safe defaults, validated overrides, explainable precedence |
| Fact-cache rule | explicit need, TTL, sensitivity, invalidation; never stale authorization evidence |
| Command guard | discover state, constrain execution, define changed/failed, validate, recover |
| Handler invariant | notified only by relevant change; dependent service outcome must be verified |
| Rolling safety | preflight → drain → bounded change → readiness → outcome → observe → continue |
| Error taxonomy | unreachable is transport; failed is task; rescued/ignored may hide final risk |
| Role contract | inputs, defaults, validation, platforms, outcomes, owner, version, tests, deprecation |
| Collection trust | pinned executable dependency with source, maintainer, integrity, and upgrade evidence |
| Execution environment | immutable, tested runtime for core, Python, collections, and system dependencies |
| Controller value | RBAC, templates, schedules, workflows, credentials, evidence, API; not automatic safety |
| Credential boundary | separate discovery, mutation, connection, and escalation with short-lived identity |
| Vault limitation | file encryption at rest; key custody, runtime exposure, logging, and rotation remain |
| Check-mode limitation | forecast quality depends on module support and observed external state |
| Convergence evidence | representative apply followed by a second run with zero unintended change |
| AWS inventory | account/region/state/tag filters plus governed groups, snapshot, count, and limit |
| SSM trade-off | no inbound SSH, but IAM/agent/plugin/endpoints/S3 transfer and audit dependencies |
| Terraform boundary | one system owns each mutable field; stable discovery/readiness hand-off |
| Partial-run recovery | stop expansion, preserve evidence, classify hosts, restore or converge, verify outcome |
| Executive recommendation | bounded ownership, targets, trust, runtime, rollout, recovery, adoption, and measures |

Review missed cards after one day, three days, and seven days.

Return to the [module overview](index.md) when ready to continue.
