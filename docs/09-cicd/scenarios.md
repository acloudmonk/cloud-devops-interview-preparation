# CI/CD and Progressive-Delivery Scenarios

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer aloud before reading the model answer. Establish artifact identity, trust
boundary, target state, customer impact, recovery choice, and verification.

## 1. Pipeline is green but production has the wrong image

**Model answer:** Stop promotion, compare deployed digest—not tag—with the approved
run and registry evidence, and restore the last known-good digest if safe. Trace
tag mutation, target selection, and concurrent runs. Enforce build-once promotion,
digest deployment, environment binding, and post-deploy identity verification.

## 2. Canary metrics pass but customers report failures

**Model answer:** Pause exposure and segment reports by cohort, route, tenant,
device, and business outcome. The canary may be unrepresentative or telemetry may
miss correctness. Restore/disable exposure, preserve evidence, fix cohort and
success criteria, and include customer and business signals in future analysis.

## 3. GitHub Actions cannot assume its AWS role

**Model answer:** Keep static keys out. Inspect token issuance, workflow permissions,
audience, issuer, subject/environment claims, AWS trust policy, clock, and CloudTrail
denials. Correct the narrow mismatch and test from the intended protected context;
do not broaden trust to every branch or repository as a quick fix.

## 4. A secret appears in job logs

**Model answer:** Cancel exposure where possible, revoke/rotate immediately, restrict
logs and artifacts, and determine every downstream use. Preserve audit evidence
without spreading the value. Fix the command/input path, permissions, redaction,
and secret design; masking alone is not remediation.

## 5. An older run deploys after a newer run

**Model answer:** Stop or reverse the stale deployment using verified digests and
target state. Add environment-scoped concurrency, cancel/obsolescence checks, and a
monotonic release/version guard. Make cancellation and deploy steps idempotent so
partial state is reconciled before retry.

## 6. Database change makes application rollback fail

**Model answer:** Protect traffic and roll forward or disable exposure if the old
binary is no longer schema-compatible. Assess written data before any reversal.
Replace destructive single-release migration with expand–migrate–contract,
compatibility tests, bounded backfill, and an explicit irreversible boundary.

## 7. Required test passes only after reruns

**Model answer:** Treat the original failure as evidence, classify product versus
test/infrastructure causes, and measure reproducibility. Do not normalize rerun-
until-green. Assign ownership; fix or time-bound quarantine visibly; preserve a
small trustworthy blocking suite while broader evidence runs in parallel.

## 8. Shared cache may contain attacker-controlled output

**Model answer:** Stop privileged consumers, invalidate the cache, and rebuild on a
clean trusted runner. Check fork/event, key scope, write permissions, and whether
cached output was published. Partition cache by trust boundary and immutable inputs;
never treat cache as provenance or a promoted artifact.

## 9. Persistent self-hosted runner is compromised

**Model answer:** Quarantine the runner/pool, revoke reachable credentials, block
publication/deployment, and investigate jobs, network, caches, and artifacts since
the earliest credible compromise. Rebuild runners from known images, verify outputs,
and move to isolated ephemeral capacity with constrained network and roles.

## 10. Artifact registry is unavailable during release

**Model answer:** Stop unsafe promotion and determine whether targets already have
the verified digest. Use only tested, integrity-verified continuity paths—not an
untrusted rebuild. Respect dependency objectives, communicate release impact, and
later test replica/retention/offline recovery appropriate to the business need.

## 11. Manual production approval becomes a bottleneck

**Model answer:** Measure wait by risk class and ask what judgment the approval adds.
Automate objective evidence, pre-authorize low-risk changes within policy, and keep
human review for material risk with artifact/health context and an expiry. Audit
bypass without making routine delivery depend on chat availability.

## 12. One AWS region deploys and the second fails

**Model answer:** Pause global promotion, establish actual digest/config/schema per
region and customer-routing impact, and avoid blind retry. Choose complete, restore,
or temporarily route based on compatibility and capacity. Make regional steps
idempotent, expose partial state, and define sequencing and reconciliation.

## 13. A forked pull request needs tests

**Model answer:** Run untrusted code on isolated ephemeral infrastructure with no
production secrets, write token, shared privileged cache, or internal network.
Publish only non-sensitive results. Require trusted review before any privileged
workflow, and prevent base-context workflows from executing fork-controlled code.

## 14. Emergency fix needs a policy bypass

**Model answer:** State customer harm and why the normal path cannot meet recovery
time. Use a time-bound, least-privilege, multi-party break-glass route; retain source,
artifact, approver, target, and command evidence; verify recovery; then reconcile
the change through normal controls and review the bypass cause.

## 15. CI cost doubles while delivery slows

**Model answer:** Segment queue/execution and spend by workflow, stage, runner, and
change type. Remove duplicate builds, unsafe broad matrices, oversized checkout and
artifacts, and serial dependencies; tune cache and capacity after correctness.
Measure lead time and reliability alongside cost so savings do not create delay.
