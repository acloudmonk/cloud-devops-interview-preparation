# Evidence

Store only sanitized Markdown summaries in Git. Do not commit raw exports that
may contain account IDs, endpoints, tokens, customer data, trace attributes, or
cost details tied to an account.

Each experiment report should include:

- date, owner role, source commit, and tool versions;
- purpose and hypothesis;
- sanitized environment description;
- traffic or fault profile;
- steady-state and stop conditions;
- observed result and dashboard/trace reference;
- limitations, decision, and follow-up;
- teardown verification where resources were created.

Suggested files are `assumptions.md`, `load-test.md`, `fault-test.md`,
`recovery.md`, `cost.md`, and `teardown.md`.
