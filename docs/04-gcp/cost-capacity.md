# Cost, Capacity, Quotas, and Sustainability

[← Reliability and operations](reliability-operations.md) · [Next: Well-Architected →](well-architected.md)

Map billing account → project → service/SKU → label/tag → workload/team → business
unit, and export detailed billing data. A budget normally alerts; it is not a guaranteed
spending cap.

Model steady state, peak, failure headroom, storage/operations, telemetry, support,
licenses, egress, backup, and engineering effort. Track cost per business transaction.

## Optimization order

1. Remove waste and correct allocation.
2. Right-size architecture and demand.
3. Schedule or autoscale elastic work safely.
4. Tune storage lifecycle and data movement.
5. Buy committed use discounts after stable-demand evidence.
6. Use Spot VMs only for interruption-tolerant work.

Quotas are reliability controls. Inventory project, regional, zonal, API, IP, CPU,
accelerator, database, and connection limits. Forecast failover demand, request changes
early, alarm on consumption/rejections, and test degradation when increases are denied.

For sustainability, reduce idle capacity and needless replicas/transfers, improve
utilization, and lifecycle data while balancing carbon, sovereignty, latency, and SLOs.
