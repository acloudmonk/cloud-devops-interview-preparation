# AWS Ticketing Architecture Lab Workspace

This workspace supports the pilot module's
[AWS implementation guide](../../../docs/01-cloud-architecture/implementation-guide.md).
The local slice implements the reservation, durable dispatch, payment, and
reconciliation paths using the same data and messaging semantics planned for
AWS. It is a learning system, not production software.

## Working agreement

- Use a dedicated sandbox AWS account and short-lived federation.
- Set an AWS Budget before deployment.
- Tag resources with `Project=ticketing-lab` and `Environment=lab`.
- Do not commit credentials, account IDs, state, plans, `.env`, or raw telemetry.
- Open a feature-branch PR and require manual approval for milestone changes.
- Run load and failure tests only against an endpoint you are authorized to test.

## What the local slice proves

- A DynamoDB transaction prevents two orders from holding the same seat.
- An idempotency key is bound to one request and stored order.
- A committed reservation remains dispatchable when SQS is temporarily unavailable.
- SQS duplicate delivery cannot duplicate a confirmed order or payment.
- Declined payments release only the reservation they own.
- An ambiguous payment result enters reconciliation rather than being charged again.
- Invalid messages are retried and then moved to a DLQ.

The API intentionally returns `202 Accepted`: reservation is durable, but
payment confirmation completes asynchronously.

## Prerequisites

- Docker with the Compose plugin
- Python 3.12 or later for tests and the smoke script
- Ports 8000, 8080, 8081, and 4566 available locally

No AWS account or cloud credentials are required. The Compose-only `local`
credential values are placeholders accepted by the emulators and have no
permissions outside the local network.

## Run the unit tests

From this directory:

```bash
ruff check app scripts tests
ruff format --check app scripts tests
python -m unittest discover -s tests -v
```

Ruff is a developer prerequisite for the first two commands and is pinned in
`requirements-test.txt`. Install `requirements-app.txt` and
`requirements-test.txt` to run the API and worker contract tests. The core
invariant tests require no containers.

## Start the complete local environment

```bash
docker compose config --quiet
docker compose up --build -d
docker compose ps
docker compose logs init
python scripts/smoke.py
```

Expected results:

- `init` exits with code 0 after creating three tables, SQS, the DLQ, and 20 seats;
- `api`, `worker`, and `payment-stub` are running;
- `GET http://localhost:8080/ready` returns `{"status":"ready"}`;
- the smoke test reserves a seat, safely replays the request, and observes a
  single confirmed order.

OpenAPI documentation is available locally at
`http://localhost:8080/docs` and `http://localhost:8081/docs`.

## Exercise payment outcomes

Submit a unique seat and key for each case:

```bash
curl -X POST http://localhost:8080/reservations \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: practice-decline-001" \
  -d '{"eventId":"event-001","seatId":"seat-002","paymentMode":"decline"}'
```

Valid `paymentMode` values are `success`, `decline`, `timeout`, and `unknown`.
They exist only to make failure behavior reproducible:

| Mode | Expected order behavior |
| --- | --- |
| `success` | Worker confirms payment and seat |
| `decline` | Worker declines order and releases the owned hold |
| `unknown` | Stub records charge, returns 504, and reconciliation confirms it |
| `timeout` | Worker marks reconciliation; provider reports no known result |

Retrieve the order using the returned `orderId`:

```bash
curl http://localhost:8080/orders/ORDER_ID
```

## Exercise dispatch recovery

```bash
docker compose stop localstack
```

Create a reservation. The API keeps `dispatchStatus` as `PENDING` because the
reservation transaction already committed but SQS is unavailable. Then recover:

```bash
docker compose start localstack
docker compose restart worker
docker compose logs -f worker
```

The worker scans pending reservations, republishes them, and marks dispatch as
sent. Duplicate publication remains safe because order and payment processing
are idempotent.

## Troubleshooting

| Symptom | Check | Safe action |
| --- | --- | --- |
| API never becomes healthy | `docker compose logs init api` | Confirm ports and emulator health, then recreate |
| Order remains `RESERVED` | `docker compose logs worker localstack` | Restore SQS/worker and observe pending dispatch |
| Order remains `RECONCILIATION` | Payment mode and stub lookup | Decide whether a retry is safe; never retry a charge blindly |
| Message reaches DLQ | Message shape and receive count | Diagnose before replay; do not purge evidence |
| Smoke test conflicts | Existing in-memory state | Use the same key or tear down and recreate |

## Teardown

```bash
docker compose down --volumes --remove-orphans
docker compose ps --all
```

The second command should show no lab containers. The emulators use ephemeral
storage, so teardown removes all local ticket, order, queue, and payment data.

## Intentional limitations

- Authentication and customer identity are excluded from this local correctness slice.
- Pending dispatch and reconciliation use DynamoDB scans suitable only for the
  tiny lab data set. The AWS milestone must use a durable outbox/indexed access
  pattern rather than a growing table scan.
- The payment provider is an in-memory test double and loses state on restart.
- DynamoDB Local and LocalStack approximate AWS APIs but do not reproduce every
  quota, latency, IAM, networking, failure, or consistency characteristic.
- Idempotency-record expiry, inventory import, refunds, and operator replay
  controls remain future exercises.
- Local HTTP is acceptable only inside this isolated lab; cloud deployment must
  use TLS, workload identity, least privilege, and secret management.

## Workspace

```text
01-cloud-architecture-ticketing/
├── .env.example
├── compose.yaml
├── Dockerfile
├── requirements-app.txt
├── requirements-test.txt
├── pyproject.toml
├── app/ticketing/
│   ├── api.py
│   ├── adapters.py
│   ├── bootstrap.py
│   ├── domain.py
│   ├── payment_stub.py
│   └── worker.py
├── architecture/
│   ├── decisions/0001-compute-platform.md
│   └── threat-model.md
├── evidence/README.md
├── infra/terraform/
│   ├── bootstrap/README.md
│   └── workload/README.md
├── load/k6/ticket-release.js
├── observability/README.md
├── runbooks/order-processing.md
├── scripts/smoke.py
└── tests/
    ├── README.md
    ├── test_api.py
    ├── test_domain.py
    └── test_worker.py
```

The local slice deliberately keeps its domain model independent from FastAPI,
DynamoDB, and SQS so invariant tests remain fast. Cloud infrastructure should
be added only after its matching decision record and acceptance tests are reviewed.

## Milestones

1. Complete assumptions, SLOs, threat model, and ADRs. **Scaffolded**
2. Prove seat, idempotency, dispatch, and payment invariants locally. **Implemented**
3. Deploy the two-AZ AWS core using Terraform. **Next milestone**
4. Add edge admission, security, telemetry, and delivery controls.
5. Run load, failure, and restore tests.
6. Record cost, measured RTO/RPO, limitations, and teardown.

## Definition of done

- All four business invariants in the lab are covered by automated tests.
- `terraform fmt -check -recursive` and `terraform validate` pass.
- No static cloud credential exists in source, image, configuration, or logs.
- The deployment can roll back to the prior known-good task definition.
- SLO, queue, payment-reconciliation, and DLQ behavior are observable.
- Load and fault reports state hypothesis, environment, result, and limitations.
- Destroy is followed by service/tag and cost verification.
