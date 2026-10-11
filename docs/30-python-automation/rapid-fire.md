# Rapid-Fire Revision

[← Module overview](index.md) · [Flashcards](flashcards.md)

1. **Automation chain?** Outcome, authority, state, plan, bounded change, verify, evidence, reconcile.
2. **Why not Python for everything?** Declarative/workflow systems may own state, durability, and recovery better.
3. **Pure core?** Decision logic without network, file, clock, randomness, or cloud side effects.
4. **Adapter?** Boundary translating owned models to an external API or system.
5. **Type hint value?** Earlier interface feedback, not runtime input validation.
6. **Dataclass fit?** Explicit lightweight records with generated behavior.
7. **Iterator value?** Processes data lazily without retaining the full collection.
8. **Exception rule?** Catch only to handle, translate, enrich, compensate, or retry knowingly.
9. **Partial success?** Some items completed; result must preserve item-level outcome.
10. **Uncertain outcome?** Remote effect may have occurred despite missing response.
11. **CLI stdout/stderr?** Results to stdout; diagnostics to stderr.
12. **Stable CLI automation output?** Versioned JSON schema plus documented exit codes.
13. **Configuration precedence?** Explicit documented order with observable non-secret effective values.
14. **Safe target selection?** Owned inventory, explicit scope, preview, limits, and revalidation.
15. **Dry-run fidelity?** Same selection/planning path, no mutation, limitations disclosed.
16. **Why not secret CLI arguments?** Process listings and shell history can expose them.
17. **Boto3 session?** Credential, Region, profile/config context for clients/resources.
18. **Paginator?** SDK abstraction over service continuation tokens and pages.
19. **Waiter?** Polling state machine with defined success/failure/delay, not universal readiness.
20. **Control-plane acknowledgement?** Request accepted, not necessarily usable resource state.
21. **Retry candidates?** Known transient, rate, or service failures on safely repeatable work.
22. **Retry budget?** Bound attempts and elapsed time, with exponential backoff and jitter.
23. **Jitter value?** Prevents synchronized clients from retrying together.
24. **Idempotency?** Repeating same logical operation does not create unintended additional effect.
25. **Idempotency key contract?** Operation, target, input fingerprint, principal, retention, conflict.
26. **Checkpoint?** Durable progress/outcome data enabling validated resume and reconciliation.
27. **Rollback limit?** Prior state or external side effects may not be safely reversible.
28. **Compensation?** New business/technical action that counteracts an earlier effect.
29. **Thread fit?** Blocking I/O with bounded workers and thread-safe dependencies.
30. **Process fit?** CPU-bound work that tolerates serialization and process overhead.
31. **Async fit?** Many compatible I/O operations with explicit cancellation/backpressure.
32. **Backpressure?** Constrain producers when consumers or dependencies cannot keep up.
33. **Concurrency danger?** Higher quota pressure, memory, race, and blast radius.
34. **Graceful shutdown?** Stop intake, checkpoint/finish atomic work, release, flush, report.
35. **Unit-test focus?** Selection, validation, planning, classification, and formatting.
36. **Integration-test focus?** Real identity, permissions, SDK/service semantics, and cleanup.
37. **Mocking risk?** Tests may prove behavior against an invented provider.
38. **Destructive-path tests?** Empty/broad scope, protected target, drift, absent approval, stop limit.
39. **Coverage limitation?** Executed lines do not prove assertions, scenarios, or safety.
40. **Reproducible application?** Controlled build plus locked, reviewed dependencies and artifact identity.
41. **Wheel?** Standard Python distribution artifact for library or application installation.
42. **Container benefit?** Controlled runtime/dependencies; still needs patching, identity, and lifecycle.
43. **Lambda concern?** Timeout, retry semantics, cold start, package size, concurrency, idempotency.
44. **Credential default?** Short-lived runtime role/managed identity, not embedded cloud keys.
45. **Structured event?** Named fields for run, target, action, attempt, outcome, reason, request ID.
46. **Kill switch?** Stops new work safely without pretending completed effects vanished.
47. **Reconciliation?** Independent compare of intended and actual state followed by owned repair.
48. **Useful automation SLO?** Correct durable outcome within time, not process exit zero.
49. **Multi-cloud abstraction rule?** Standardize intent/results while preserving native semantics in adapters.
50. **Strong closing test?** Safety, authority, state, failure, proof, owner, cost, residual risk.
