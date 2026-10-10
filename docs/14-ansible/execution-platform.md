# Execution Platforms and Operations

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

A laptop can prove content; it is not a production automation platform. Shared
automation needs reproducible runtimes, controlled credentials, authorization,
capacity, scheduling, evidence, and recovery.

## Execution environments

An execution environment packages `ansible-core`, Python, collections, system
libraries, and tooling into a versioned container image. Build it through a
reviewed supply chain, scan and sign it, pin dependencies, test it with content,
and promote the immutable digest. Do not install dependencies during a production
job from an untrusted network.

## CLI, AWX, and Automation Controller

- **CLI** is appropriate for development and tightly controlled break-glass use.
- **AWX** is the upstream controller project and a useful community platform.
- **Automation Controller** is the supported Red Hat product capability within
  Ansible Automation Platform.

A controller adds projects, inventories, credentials, job templates, schedules,
workflows, surveys, RBAC, logs, notifications, and APIs. It does not make unsafe
content safe; guardrails remain part of the content and operating model.

## Job contract

A production job should pin:

- source revision and execution-environment digest;
- inventory source and synchronized snapshot;
- validated parameters and host limit;
- credential references and privilege boundary;
- forks, strategy, timeout, batch, and stop conditions;
- approval, maintenance window, notifications, and evidence retention.

## Workflow design

Use workflows for explicit dependencies such as inventory sync, preflight,
change, verification, and recovery. Distinguish success, failure, and always-run
paths. Keep workflows understandable; a large visual graph can hide coupling as
easily as a large playbook.

## Capacity and isolation

Place execution near targets without flattening trust zones. Separate production
from lower-trust workloads, prevent concurrent conflicting jobs, set resource
limits, and monitor queue time, runner saturation, inventory latency, and target
connection load. Horizontal capacity does not remove downstream API limits.

## Operational measures

Track change success rate, unreachable rate, unexpected changed count,
convergence on second run, mean recovery time, stale inventory failures,
credential failures, queue time, manual intervention, and policy exceptions.
Tie these to service outcomes rather than celebrating task volume.

## Break-glass automation

Prepare diagnostic and containment workflows before incidents. Require a ticket,
short-lived authorization, narrow target limit, immutable content, captured
output, peer review when possible, and post-incident reconciliation. A controller
must not become an unaudited root shell with a web interface.

Return to the [module overview](index.md) when ready to continue.
