# Cloud SDK and API Engineering

[← CLI and configuration](cli-configuration.md) · [Next: Reliability →](reliability-idempotency.md)

SDKs simplify request construction; they do not remove distributed-systems behavior.

## AWS anchor

Use Boto3 sessions and clients with explicit Region/account assumptions. Prefer the
default credential provider chain and IAM roles over embedded keys. Configure connect
and read timeouts plus an appropriate retry mode; record request IDs. Use paginators
for every list API, waiters only when their success/failure states and delay fit the
objective, and service-specific idempotency tokens where supported.

## API correctness

- Distinguish control-plane acknowledgement from resource readiness.
- Expect throttling, eventual consistency, quotas, partial pages, and asynchronous jobs.
- Retry only transient and safely repeatable operations with exponential backoff and jitter.
- Bound attempts and elapsed time; honor server retry guidance where trustworthy.
- Validate account, Region, partition, resource ownership, and tags before mutation.
- Preserve an uncertain outcome after timeout; query state before repeating.

## Multi-cloud translation

Azure SDK clients commonly use `azure-identity` credentials; Google Cloud client
libraries use Application Default Credentials. Both have distinct paging, long-running
operation, retry, endpoint, project/subscription, and error models. Standardize your
automation result and evidence contract, not a leaky “universal SDK” abstraction.

## Inventory at scale

Stream pages, checkpoint continuation safely, bound parallel calls, centralize quota
budgets, and deduplicate stable resource identifiers. Record inventory time and
completeness; a changing estate is not a transactionally consistent snapshot.
