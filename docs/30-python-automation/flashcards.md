# Python Automation Flashcards

[← Module overview](index.md) · [Rapid-fire revision](rapid-fire.md)

1. **Decision model?** Outcome → authority → state → plan → bounded change → verify → evidence → reconcile.
2. **Mechanism test?** Use the system best owning state, durability, recovery, and operator experience.
3. **Automation contract?** Inputs, targets, identity, idempotency, failure, dry run, verify, evidence, owner.
4. **Code structure?** Pure domain decisions plus injected external adapters and thin orchestration.
5. **Data validation?** Schema, type, range, identifier, time, encoding, duplicate, unknown field.
6. **Result states?** Changed, unchanged, skipped, failed, uncertain, reconciled.
7. **CLI contract?** Arguments, config precedence, output schema, stderr, exit codes, compatibility.
8. **Destructive guardrails?** Explicit scope, preview, plan, revalidation, max changes, canary, approval.
9. **SDK rule?** Expect pagination, throttling, eventual consistency, async completion, quotas.
10. **Ambiguous timeout?** Query state before repeating; retain unknown if proof is unavailable.
11. **Safe retry?** Classified transient + repeatable operation + bounded backoff/jitter.
12. **Idempotency proof?** Same logical request and input produces one intended durable effect.
13. **Checkpoint content?** Item, plan/version, attempt, known state, outcome, verification.
14. **Resume rule?** Revalidate current state, input, authority, and plan before continuing.
15. **Concurrency rule?** Start sequential, measure, bound workers/rate/queue/memory, add backpressure.
16. **Thread/process/async?** Blocking I/O / CPU / compatible high-concurrency I/O.
17. **Test pyramid?** Pure unit, adapter contract, isolated integration, failure, safety/canary.
18. **Mock boundary?** Mock owned adapter; verify provider behavior with isolated integration tests.
19. **Dry-run test?** Same selector/planner as apply and no side effect across every adapter.
20. **Artifact contract?** Versioned code, dependencies, config/schema, provenance, immutable identity.
21. **Workload identity?** Short-lived platform credential scoped to runtime and task.
22. **Logging boundary?** Allowlisted structured evidence; never credentials or sensitive payloads.
23. **Incident sequence?** Stop, revoke, preserve, enumerate, stabilize, reconcile, restore, improve.
24. **Automation success?** Verified intended state and transparent partial/unknown outcomes.
25. **Architect answer?** Outcome/invariant → mechanism/state → safety/failure → proof/owner/trade-off.

Review missed cards after one day, three days, and seven days.
