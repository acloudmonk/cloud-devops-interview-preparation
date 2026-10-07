# Capacity, SLO, RTO, and RPO Worked Example

Last reviewed: **2026-10-07**

This is an interview calculation exercise, not a production forecast. Its value
is the reasoning chain: declare assumptions, show simple arithmetic, identify
the sensitive variables, and explain how testing will replace estimates.

## Starting scenario

- One million users may arrive around the weekly ticket release.
- The business wants most legitimate users admitted within 15 minutes.
- An admitted journey performs six browse requests, one reservation attempt,
  and—when successful—one payment attempt.
- Eight percent of arrivals attempt a reservation.
- Sixty percent of reservation attempts reach payment.
- Traffic can be 2.5 times the average during the busiest minute.
- Maintain 30% tested capacity headroom.

## Step 1: estimate arrival and request rates

Average arrival rate:

```text
1,000,000 users / 900 seconds = 1,111 users/second
```

The waiting room should admit users based on downstream capacity, not merely
the number waiting. If all users were admitted evenly, the estimated rates are:

| Journey | Average calculation | Average rate | Busiest-minute estimate |
| --- | ---: | ---: | ---: |
| Browse | 1,111 × 6 | 6,666 requests/s | 16,665 requests/s |
| Reserve | 1,111 × 0.08 | 89 requests/s | 223 requests/s |
| Payment | 89 × 0.60 | 53 requests/s | 133 requests/s |

Add 30% headroom only after identifying the bottleneck:

| Journey | Peak estimate | With 30% headroom |
| --- | ---: | ---: |
| Browse | 16,665 requests/s | 21,665 requests/s |
| Reserve | 223 requests/s | 290 requests/s |
| Payment | 133 requests/s | 173 requests/s |

Do not present these as facts. Conversion rate, burst shape, bot traffic, cache
hit rate, and admission window could each materially change the result.

## Step 2: estimate concurrency

Use Little's Law as a first approximation:

```text
concurrency = arrival rate × average time in the system
```

If browse processing averages 200 ms at 21,665 requests/s:

```text
21,665 × 0.2 = 4,333 concurrent browse requests
```

If reservation processing averages 500 ms at 290 requests/s:

```text
290 × 0.5 = 145 concurrent reservation requests
```

The estimate informs connection pools, task concurrency, thread/event-loop
limits, and dependency budgets. It does not replace a load test because latency
often increases non-linearly near saturation.

## Step 3: estimate queue recovery

Suppose a worker outage creates 120,000 queued payment tasks. After recovery:

- workers can process 400 messages/s;
- new work continues at 150 messages/s;
- effective drain rate is 250 messages/s.

```text
drain time = backlog / (processing rate - new arrival rate)
drain time = 120,000 / (400 - 150) = 480 seconds = 8 minutes
```

If processing rate is less than or equal to arrival rate, the queue never
recovers. Scaling on CPU alone may miss this; message age and backlog per worker
are better signals.

## Step 4: state correctness separately from availability

The purchase journey can fail while the inventory invariant still holds:

```text
One seat can belong to at most one confirmed order.
```

Interview answers should separate:

- availability: can the customer complete the journey?
- durability: is an accepted order retained?
- correctness: can the same seat or payment be applied twice?
- timeliness: how long until the final state is known?

A `409 Conflict` for an already-held seat is a correct business outcome, not a
platform availability failure.

## Step 5: define SLIs and SLOs

| Journey | SLI | Example SLO |
| --- | --- | --- |
| Admission | Valid tokens issued / eligible requests | 99.9% per release window |
| Browse | Successful non-excluded responses / valid requests | 99.9% monthly |
| Reserve | Correct completed outcomes / valid attempts | 99.95% per release window |
| Purchase latency | Time from accepted reservation to known outcome | p95 under 2 seconds |
| Queue recovery | Age of oldest processable message | Under 10 minutes |
| Reconciliation | Age of unknown payment outcomes | 99% resolved within 15 minutes |

Define exclusions narrowly. Do not hide overload, dependency failures, or
server errors by classifying them as invalid requests.

## Step 6: calculate an error budget

A 99.95% monthly availability objective over a 30-day month permits:

```text
30 × 24 × 60 = 43,200 minutes
43,200 × 0.0005 = 21.6 minutes
```

The weekly release is a short, business-critical window, so a monthly average
can hide a severe Friday outage. Use both a monthly objective and a release-window
objective. Fast burn alerts should detect rapid budget consumption during the event.

## Step 7: distinguish RTO and RPO

| Capability | Example RTO | Example RPO | Reasoning |
| --- | ---: | ---: | --- |
| Browse catalogue | 30 minutes | 24 hours | Rebuildable and cacheable data |
| Reservation | 5 minutes | Near zero | Inventory correctness and revenue |
| Confirmed order | 15 minutes | Near zero | Customer entitlement and payment |
| Analytics | 24 hours | 4 hours | Delayed reporting is acceptable |

RTO is the maximum acceptable restoration time. RPO is the maximum acceptable
data loss measured in time. Neither is proven by a diagram; restore and failover
tests must produce measured results.

## Step 8: identify AWS validation evidence

An AWS-oriented answer could validate assumptions using:

- CloudFront and AWS WAF request/admission metrics;
- Application Load Balancer request, error, and target-latency metrics;
- ECS desired/running task counts and saturation;
- DynamoDB consumed capacity, latency, throttling, and conditional failures;
- SQS message age, depth, receive count, and DLQ depth;
- application metrics for reservation correctness and payment reconciliation.

Name the evidence after explaining the SLI. A dashboard is not useful merely
because it contains many service metrics.

## Interview follow-ups

1. Which assumption most affects cost?
2. What happens if 30% rather than 8% attempt a reservation?
3. How do bots change admission calculations?
4. What if payment capacity is fixed at 80 requests/s?
5. Which work can be queued and which must remain synchronous?
6. How would you prove the 30% headroom is real?
7. How does a cache hit-rate drop affect origin capacity?
8. When would you pre-scale instead of relying on reactive autoscaling?

## Strong answer pattern

> I would not design directly for one million simultaneous backend requests.
> I would model arrival shape and journey mix, constrain admission to the tested
> capacity of the reservation and payment path, protect the seat invariant with
> an atomic write, and validate the model through release-shaped load tests.
> I would track customer success, latency, queue recovery, and reconciliation—not
> only CPU—and revise the model using observed conversion and cache-hit rates.
