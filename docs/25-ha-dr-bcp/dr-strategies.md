# Disaster-Recovery Strategies

[← Module overview](index.md) · [HA and failure domains](ha-failure-domains.md)

Choose a recovery strategy per business service and failure scenario. The labels
describe broad patterns; measured end-to-end recovery determines whether the
design meets its objectives.

## AWS recovery continuum

| Strategy | Recovery state | Strength | Principal risk |
| --- | --- | --- | --- |
| Backup and restore | Protected data plus rebuild assets | Lowest steady-state cost | Provisioning and restore duration or missing dependencies |
| Pilot light | Core data and minimal critical components running | Faster than full rebuild | Scale-up, deployment, and integration remain on recovery path |
| Warm standby | Complete but scaled-down environment | Faster, regularly exercisable recovery | Capacity, drift, and promotion orchestration |
| Multi-site active-active | Multiple sites serve production | Lowest potential interruption | Data conflicts, correlated failure, operational and cost complexity |

Do not attach fixed RTO/RPO values to a label. Data size, replication, quotas,
automation, people, validation, and downstream systems determine the result.

## Selection questions

- Which disruption and blast radius are covered?
- Does the business need continuity, recovery, or both?
- Can data be asynchronously replicated, and what loss is acceptable?
- Can the application run with stale, partial, or read-only data?
- Are artifacts, secrets, certificates, keys, configuration, and IaC independent?
- Is recovery capacity pre-provisioned or guaranteed by quota and reservation?
- Which data-plane operations work if a provider control plane is impaired?
- How are external integrations, allowlists, DNS, and human access switched?
- Can the organization operate and test the added complexity?

## Recovery dependency chain

Recover foundations before consumers: governance and emergency access; network
and DNS; keys, secrets, certificates, and identity; data; platforms; applications;
integrations; observability; then business validation. A dependency graph and
wave plan are more credible than a flat application priority list.

## Control-plane caution

Pre-create resources and permissions needed during recovery when practical.
Depending on emergency creation, quota increases, new trust relationships, or
untested console access extends RTO and may fail during a broad event.

## Exit and failback

Define activation thresholds, decision authority, minimum success criteria,
maximum acceptable time in recovery mode, data reconciliation, failback method,
and conditions for declaring normal operations. DR is incomplete without a safe
way to preserve writes made after failover.

Return to the [module overview](index.md) when ready to continue.
