# Linux & OS Fundamentals

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**
Level: **Senior / Architect**

Linux knowledge in senior cloud interviews is not command memorization. It is
the ability to explain how work moves through processes, memory, storage,
network sockets, and services; distinguish guest failures from cloud-platform
failures; and recover safely using evidence.

!!! tip "Where to start"
    Start with **1. Operating-system mental model** and follow the numbered path.
    The module uses AWS EC2 as its cloud anchor, with Azure and Google Cloud
    differences where they affect diagnosis or recovery. No server or cloud
    account is required.

## Learning objectives

By the end of this module, you should be able to:

- explain process, thread, scheduling, memory, filesystem, and I/O behavior;
- reason about systemd units, dependencies, startup, shutdown, and journald;
- distinguish utilization from saturation and identify the constrained resource;
- investigate CPU, memory, disk, filesystem, and process symptoms safely;
- explain permissions, capabilities, privilege boundaries, SSH, and audit evidence;
- separate application, guest OS, virtual device, host, and cloud control-plane failures;
- design monitoring, patching, recovery, and immutable replacement strategies;
- lead a Linux incident using hypotheses, reversible mitigations, and verification;
- communicate commands as evidence-gathering tools rather than as a random checklist.

## Recommended module path

### Phase 1 — Learn the system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Operating-system mental model](concepts.md) | Understand kernel/user space, processes, resources, and failure boundaries |
| 2 | [Processes, services, and logs](processes-services.md) | Explain lifecycle, signals, systemd, dependencies, and journald |
| 3 | [CPU and memory reasoning](cpu-memory-performance.md) | Interpret load, scheduling, reclaim, swap, OOM, and pressure |
| 4 | [Storage and filesystems](storage-filesystems.md) | Reason about capacity, inodes, mounts, durability, and I/O latency |
| 5 | [Identity, permissions, and secure access](security-access.md) | Apply least privilege across users, files, capabilities, sudo, and SSH |
| 6 | [Cloud VM operations](cloud-vm-operations.md) | Separate guest, host, storage, network, and provider failure domains |
| 7 | [Troubleshooting playbook](troubleshooting-playbook.md) | Diagnose from customer symptom to evidence, mitigation, and prevention |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 8 | [Linux production design exercise](design-exercise.md) | Design an operable fleet without deploying infrastructure |
| 9 | [Scenario questions and model answers](scenarios.md) | Practise 15 core Linux interview scenarios |
| 10 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous cross-layer failures |
| 11 | [Ten-minute operations review](presentation-template.md) | Present risk, evidence, recovery, and improvement decisions |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 12 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 13 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 14 | [Timed Linux operations mock interview](../mock-interviews/linux-operations.md) | Complete a scored 50-minute assessment |
| 15 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

This module covers Linux reasoning and operating-system troubleshooting. Detailed
DNS, routing, TLS, load balancing, and packet analysis belong to
[Module 07 — Networking & DNS](../07-networking/index.md). Container isolation
is introduced through namespaces and cgroups; image construction and container
runtimes belong to [Module 10 — Docker](../10-docker/index.md).

## Completion checklist

- [ ] I can explain the system from an incoming request to process, memory, and storage.
- [ ] I can distinguish high utilization from harmful saturation.
- [ ] I can diagnose a failed service without starting with a restart.
- [ ] I can explain a safe full-disk, OOM, and failed-boot recovery approach.
- [ ] I answered all 25 scenarios aloud and recorded weak areas.
- [ ] I completed the design exercise before reading scenario answers.
- [ ] I completed the mock interview and recorded evidence for each score.
