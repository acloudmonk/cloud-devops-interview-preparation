# Kubernetes Ecosystem Active-Recall Flashcards

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use each prompt without viewing the cue. Explain the ownership boundary, failure mode,
and one condition that changes the choice.

| Prompt | Answer cue |
| --- | --- |
| Ecosystem decision | unmet outcome → options → controllers/data/identity → lifecycle/cost/exit → pilot evidence |
| Controller ownership | one authoritative writer per field/outcome; status and emergency paths explicit |
| Helm strength/risk | versioned package/release versus template/value/hook/dependency complexity |
| Kustomize strength/risk | visible YAML composition versus overlay/patch coupling and drift |
| Rendered evidence | source + package/base + inputs + renderer + manifest digest + policy + target |
| GitOps boundary | desired-state reconciliation and drift, not complete runtime/customer truth |
| GitOps emergency | bounded pause/source change, evidence, customer verify, commit, resume/converge |
| CNI decision | IPAM/routing/service/policy/encryption/observability/kernel/support/migration |
| eBPF boundary | powerful kernel mechanism with node-wide/version/resource/debug implications |
| Gateway API | role-oriented classes/gateways/routes/attachment with implementation conformance |
| Mesh decision | identity/mTLS/traffic/telemetry value versus proxy/control-plane/cert/upgrade cost |
| Retry budget | one end-to-end deadline, bounded idempotent retries, backoff, downstream safeguards |
| Scaling chain | demand → metric/event → replicas/resources → pending → nodes/cloud → ready work |
| Autoscaler conflict | assign replicas/requests/nodes/fields to compatible authoritative controllers |
| Admission contract | objective, scope, audit/enforce, timeout/failure, HA, exception, test, rollback |
| Secret model | Git ciphertext, synced Secret, CSI mount, or direct retrieval by exposure/availability needs |
| Certificate proof | inspect served chain/key/reload/client trust, not only controller status |
| Operator value | continuous domain reconciliation worth CRD/controller/privilege/lifecycle dependency |
| CRD lifecycle | schema/default/version/conversion/storage/migration/backup/finalizer/deletion |
| Managed add-on limit | provider packages/supports some layers; customer owns config, rollout, impact |
| Upgrade graph | API/CRD/webhook/controller/data plane/consumer order plus skew and irreversibility |
| Reconciliation incident | source/object/owner/controller/dependency/external state/customer evidence |
| Safe uninstall | migrate consumers/data, reconcile cleanup, remove dependencies, then APIs/identity/cloud |
| Platform contract | supported interface/versions/SLO/owner/escalation/cost/exception/deprecation |
| Executive recommendation | minimum justified stack, consolidation, lifecycle risk, adoption, evidence, decision |

Review missed cards after one day, three days, and seven days.
