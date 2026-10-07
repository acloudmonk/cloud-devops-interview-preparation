# Cloud VM Operations

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**

## Layered failure model

Cloud VM troubleshooting must separate control-plane state from data-plane and
guest behavior.

| Layer | Examples | Evidence owner |
| --- | --- | --- |
| Customer journey | Failed request, latency, incorrect response | Application telemetry and synthetic checks |
| Application/runtime | Deadlock, pool exhaustion, bad release | Service logs, traces, runtime and process evidence |
| Guest OS | OOM, full filesystem, failed service, bad route | Kernel, systemd, filesystem, socket and host metrics |
| Virtual devices | Block or network device errors | Guest kernel plus provider device/volume metrics |
| Compute host/platform | Host impairment, maintenance, hypervisor issue | Provider health/status signals and support evidence |
| Cloud control plane | API, IAM, quota, orchestration failure | Audit events, API errors, service health and quotas |

A VM can be “running” in the control plane while the guest is unbootable or the
application is unavailable.

## AWS reference operating model

For an autoscaled, stateless Linux service on AWS:

- build and scan a versioned machine image;
- launch with an instance profile and no static cloud credentials;
- distribute across Availability Zones behind health-based traffic routing;
- collect customer, application, guest, and EC2/EBS signals;
- manage routine access through Systems Manager where suitable;
- replace unhealthy instances rather than accumulating undocumented repairs;
- preserve state in managed or explicitly replicated durable services;
- retain a tested serial-console or offline-volume recovery path for exceptional cases.

### AWS evidence boundaries

| Signal | What it can indicate | What it does not prove |
| --- | --- | --- |
| EC2 system status check | Underlying host/platform reachability issue | Application correctness |
| EC2 instance status check | Guest networking or OS responsiveness issue | Which process or dependency failed |
| Attached EBS status/metrics | Volume availability, latency, queue, throughput behavior | Filesystem and application consistency |
| CloudWatch host/application metrics | Trends and alarms when collected correctly | Complete root cause without guest context |
| Serial console/output | Early boot and emergency guest evidence | Normal application path health |
| Systems Manager inventory/session | Managed access and fleet information | Availability when agent, IAM, network, or service dependencies fail |

## Repair or replace?

Prefer replacement when the host is stateless, image-driven, and the fleet has
capacity. Repair may be necessary when evidence, unique state, boot recovery,
or a migration constraint requires it.

| Prefer replacement | Consider controlled repair |
| --- | --- |
| Known-good image exists | Unique state or forensic evidence is present |
| Capacity and dependencies can absorb drain | Replacement would violate RTO or data safety |
| Configuration is automated | Recovery procedure is documented and reversible |
| Failure is isolated to one instance | Fleet-wide image/configuration defect would recreate failure |

Replacement without diagnosis can reproduce a systemic defect. Repair without
configuration reconciliation creates drift. Choose deliberately.

## Patch and image rollout

1. Define exposure, urgency, and compensating controls.
2. Build a new image from trusted sources.
3. Validate boot, service readiness, telemetry, and rollback behavior.
4. Canary on representative traffic and failure domains.
5. Expand progressively with SLO and resource gates.
6. Drain and remove the old version.
7. Verify inventory, vulnerability state, and fleet consistency.

## Multi-cloud translation

| Capability | AWS | Azure | Google Cloud | Important distinction |
| --- | --- | --- | --- | --- |
| VM health and lifecycle | EC2 status checks and Auto Scaling | Resource Health, boot diagnostics, VM Scale Sets | VM health checks, managed instance groups | Health signal semantics and automatic action differ |
| Managed guest access | Systems Manager Session Manager | Azure Bastion/Run Command/Entra login options | IAP TCP forwarding and OS Login | Agent, IAM, network, and audit dependencies differ |
| Boot recovery | EC2 Serial Console, console output, offline EBS repair | Serial Console and VM repair | Interactive serial console and disk repair workflow | Availability, permissions, and image support differ |
| Guest telemetry | CloudWatch Agent and application telemetry | Azure Monitor Agent | Ops Agent | Collection schema, identity, cost, and failure behavior differ |
| Image-based fleet | AMIs and launch templates | Managed Images/Compute Gallery | Images and instance templates | Rollout and version management models differ |

Do not memorize product equivalence. Explain the access path, identity,
dependency, audit, and recovery semantics required by the operating model.

## Cost and reliability decisions

- More spare fleet capacity reduces replacement risk but increases steady cost.
- Detailed high-cardinality telemetry improves diagnosis but can increase cost and data exposure.
- Long log retention supports investigations but needs classification and lifecycle policy.
- In-place patching can reduce replacement churn but increases drift and rollback complexity.
- Multi-zone placement helps host/AZ failures but not a shared image, configuration, or dependency defect.
