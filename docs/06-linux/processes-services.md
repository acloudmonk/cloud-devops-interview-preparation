# Processes, Services, and Logs

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**

## Process lifecycle

A process is created, loads code and configuration, opens resources, performs
work, and exits with a status. Its parent is responsible for collecting the exit
result. Long-running service reliability depends on more than keeping a PID
alive: readiness, dependency health, safe termination, and bounded restart
behavior matter.

### Signals and graceful termination

| Signal concept | Appropriate reasoning |
| --- | --- |
| Graceful termination | Stop admission, finish or hand off bounded work, flush durable state, then exit before the deadline |
| Reload | Apply explicitly reload-safe configuration without replacing the process |
| Forced termination | Last resort after the graceful deadline; may leave partial work requiring reconciliation |
| Child notification | Parent must collect child status and account for worker failure |

Do not assume every application handles a signal safely. Confirm its contract,
termination grace period, and behavior when forced termination occurs.

## systemd mental model

systemd manages units and their relationships. A service can be ordered after
another unit without actually requiring it, and it can require a unit without
waiting for application-level readiness. Explain dependency and ordering
separately.

Important unit behaviors include:

- `After=` and `Before=`: ordering, not health;
- `Requires=` and `Wants=`: dependency strength;
- restart policy and rate limiting;
- startup, stop, and watchdog timeouts;
- environment and credential sources;
- resource limits and cgroup placement;
- declared user, group, capabilities, and filesystem protections.

A restart loop can amplify an outage by repeatedly consuming CPU, opening
connections, or replaying work. Bound retries and make the failure observable.

## “Active” is not “ready”

A service manager reports lifecycle state. Customer readiness may additionally
require configuration load, migrations, dependency connections, cache warmup,
leader election, and successful handling of representative requests.

Use separate signals for:

- process liveness;
- local readiness;
- dependency readiness;
- end-to-end customer success.

## Logs as evidence

Logs answer discrete-event questions: what happened, to which entity, at what
time, with what outcome? They do not replace metrics or traces.

Good operational logs include:

- UTC timestamp and stable event name;
- severity with a defined meaning;
- service version and instance identity;
- correlation or request identifier;
- outcome and safe error classification;
- no credentials, tokens, unnecessary identity data, or payload secrets.

### journald and persistence

The journal can combine service stdout/stderr, kernel messages, unit metadata,
and structured fields. Retention and persistence depend on configuration and
available storage. A logging failure must not silently consume the root
filesystem or block the critical application path.

## Evidence-oriented command map

Commands are examples of questions, not a script to execute blindly.

| Question | Common read-only evidence |
| --- | --- |
| What process owns this work? | `ps`, `/proc/<pid>`, service-manager status |
| Why did it exit? | Unit status, journal for the unit, exit code, coredump metadata |
| Is it restarting? | Unit state transitions, restart counter, start-limit events |
| What is it waiting on? | Process state, wait channel, stack or trace evidence when authorized |
| Which descriptors are open? | `/proc/<pid>/fd`, descriptor counts and types |
| What changed? | Package, configuration, deployment, and audit history |
| Did the kernel intervene? | Kernel journal, OOM and device events |

Preserve timestamps, time zone, host identity, and command context. A copied
line without these can be misleading.

## Safe service incident sequence

1. Confirm customer impact and affected service instances.
2. Record recent changes and current process/unit state.
3. Capture bounded logs and resource evidence.
4. Determine whether failure is local, dependency-driven, or fleet-wide.
5. Choose a reversible mitigation: remove one instance, reduce admission,
   rollback, or replace.
6. Restart only when its consequence and recovery path are understood.
7. Verify the customer journey and reconcile unfinished work.
8. Fix lifecycle, readiness, dependency, or alerting design—not only the symptom.
