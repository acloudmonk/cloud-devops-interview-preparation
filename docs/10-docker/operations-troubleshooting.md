# Container Operations and Troubleshooting

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Troubleshoot from the observed lifecycle state and preserve evidence before repeated
restarts replace it. Container status, application health, and customer health are
different signals.

## Lifecycle failure map

| Stage | Typical failure evidence |
| --- | --- |
| Resolve/pull | Name, auth token, manifest, platform, digest, registry/network error |
| Unpack/create | Disk/inode pressure, corrupt layer, snapshotter, mount, runtime policy |
| Start | Entrypoint/command, working directory, user, architecture, library, permission |
| Run | Exit code, signal, OOM, CPU throttle, health check, dependency, application logs |
| Stop | Signal forwarding, drain duration, grace timeout, stuck I/O, forced kill |
| Remove/reclaim | Mount references, leaked snapshot, log/cache/image garbage collection |

## First evidence set

Capture immutable image digest and platform; runtime configuration; exit code and
signal; start/stop timestamps; restart/health history; stdout/stderr and application
telemetry; resource counters/limits; mount/network/DNS details; host/task/node events;
deployment cohort; and recent configuration/secret/dependency changes.

## Common exit patterns

- Exit `0`: process completed successfully, but a service may have the wrong command.
- Exit `1` or application-specific: inspect application/configuration evidence.
- Exit `126`: command found but not executable/allowed.
- Exit `127`: command or interpreter not found.
- Exit `137`: often SIGKILL; investigate OOM and forced termination rather than assume.
- Exit `143`: often SIGTERM handled/defaulted; determine why the platform stopped it.

Shells encode signals as `128 + signal`, but platform status and kernel events are
stronger evidence than memorized arithmetic.

## Resource diagnosis

For memory, compare cgroup current/peak/events, host pressure, page cache, native
allocation, application heap, and OOM records. For CPU, distinguish application
work from quota throttling, run queue, steal time, and node contention. Inspect PID,
file-descriptor, inode, byte, and log limits. Percentages without their cgroup and
host denominators can mislead.

## Health-check design

- **Startup:** allow initialization without premature liveness failure.
- **Readiness:** can this instance accept its intended traffic now?
- **Liveness:** is restart likely to restore this instance?
- **Deep dependency checks:** useful for diagnostics but can create correlated
  restarts if used as liveness.

Keep checks bounded, representative, inexpensive, and observable. A health command
may run in the container namespace with different tools, environment, user, or DNS
than an external load balancer.

## Debugging minimal images

Do not permanently install a shell and network tools solely for emergencies. Use
platform-supported debug containers, namespace entry from an authorized host, a
diagnostic image with controlled provenance, packet/flow telemetry, and external
probes. Record who attached and what changed; prefer read-only observation.

## Operating model

Track pull/start latency, restart and OOM rate, throttle time, health failure,
resource saturation, image age/vulnerability exposure, registry latency/error,
ephemeral-storage growth, and workload cost. Segment by digest, architecture,
runtime/node image, zone, launch type, and deployment cohort.

Capacity includes image download/unpack, startup surge, steady resources, shutdown
overlap, and failure replacement—not only average application utilization. Reserve
headroom for rollouts and incidents, then right-size using percentiles and service
objectives rather than arbitrary universal limits.
