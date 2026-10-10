# Linux References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last verified: **2026-10-07**

Prefer kernel, project, distribution, and cloud-provider documentation for
behavior that can change. Read command output and tool manuals for the exact
version on the affected system.

## Linux and systemd primary sources

- [Linux kernel administration guide](https://www.kernel.org/doc/html/latest/admin-guide/index.html)
  — kernel interfaces, cgroups, memory, storage, security, and operational behavior.
- [Linux memory-management documentation](https://www.kernel.org/doc/html/latest/admin-guide/mm/index.html)
  — virtual memory concepts and control interfaces.
- [Control Group v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
  — CPU, memory, I/O, PID, and pressure controls.
- [Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html)
  — CPU, memory, and I/O contention signals.
- [Linux man-pages project](https://www.kernel.org/doc/man-pages/)
  — system-call and Linux interface reference.
- [systemd service units](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
  — service lifecycle, restart, and process behavior.
- [systemd unit relationships](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html)
  — dependency and ordering semantics.
- [systemd resource control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html)
  — cgroup-backed service resource policies.
- [journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html)
  — querying system and service journal evidence.

## Security sources

- [Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html)
  — privilege decomposition and capability semantics.
- [OpenSSH manuals](https://www.openssh.com/manual.html)
  — client, server, keys, certificates, and configuration reference.
- [Red Hat: Using SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/using_selinux/index)
  — mandatory access-control concepts, policy, operation, and troubleshooting.

## AWS anchor references

- [EC2 status-check troubleshooting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstances.html)
  — system, instance, and attached-volume evidence.
- [EC2 Serial Console troubleshooting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-using-serial-console.html)
  — boot and network recovery when normal access is unavailable.
- [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
  — managed instance access, IAM, logging, and prerequisites.
- [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
  — guest metrics and log collection.

## Azure and Google Cloud translation

- [Azure Linux VM troubleshooting](https://learn.microsoft.com/troubleshoot/azure/virtual-machines/linux/welcome-virtual-machines-linux)
  — boot, SSH, agent, disk, and performance problem index.
- [Azure Linux boot errors](https://learn.microsoft.com/troubleshoot/azure/virtual-machines/linux/boot-error-troubleshoot-linux)
  — serial-console and offline-repair decision paths.
- [Google Cloud Linux boot troubleshooting](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-linux-boot-issues)
  — serial output, disk repair, kernel, filesystem, and init failures.
- [Google Cloud SSH troubleshooting](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors)
  — identity, network, guest environment, and serial-console distinctions.

## Videos

### Linux performance methodology

- **Speaker:** Brendan Gregg
- **Type:** Conference tutorial
- **Why:** Demonstrates systematic selection of observability tools rather than
  random command execution. Some tool details are older; retain the methodology
  and verify modern syntax in current manuals.
- [Linux Performance Tools, part 1](https://www.youtube.com/watch?v=FJW8nGV4jxY)

## Video discovery sources

Use official channels to locate current talks, then verify claims against
current project documentation:

- [The Linux Foundation](https://www.youtube.com/@Linuxfoundation)
- [Red Hat](https://www.youtube.com/@redhat)
- [Amazon Web Services](https://www.youtube.com/@amazonwebservices)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)

Recommended search themes: Linux performance methodology, cgroup v2, PSI,
systemd service hardening, eBPF observability, OOM analysis, filesystem recovery,
immutable VM fleets, and secure production access.

## Books

- Brendan Gregg, *Systems Performance*
- Michael Kerrisk, *The Linux Programming Interface*
- Brian Ward, *How Linux Works*
- Julia Evans, *How Linux Works* learning materials and zines

Check publisher edition and supported kernel/tool versions before purchasing.

## Suggested reading order

1. Kernel administration overview and systemd unit/service manuals
2. Memory, cgroup v2, and PSI documentation
3. EC2 status-check and serial-console guidance
4. Security references for capabilities and SSH
5. Azure and Google Cloud boot/access comparisons
6. Performance methodology video and selected book chapters
