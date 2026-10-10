# Deployment and Progressive-Delivery Strategies

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Deployment changes running software. Release makes a capability available.
Exposure decides which users receive it. Keeping these separate makes risk easier
to control: deploy dark, verify, expose gradually, and remove safely.

## Strategy comparison

| Strategy | Capacity and speed | Risk shape | Best fit |
| --- | --- | --- | --- |
| Recreate | Brief interruption; simple | All users change together | Non-critical or stateful single-instance workloads |
| Rolling | Modest extra capacity | Old/new versions coexist | Backward-compatible services and routine releases |
| Blue/green | Near-double capacity | Fast traffic switch and fallback | High-value releases needing environment-level isolation |
| Canary | Small initial exposure | Requires reliable segmentation and signals | Frequent service releases with representative traffic |
| Feature flag | Independent exposure | Code/config combinations and flag debt | User or capability-level experiments and risk control |

GitOps-style reconciliation is an operating model rather than a traffic strategy.
A controller continuously reconciles declared desired state; rolling, blue/green,
or canary behavior may occur underneath it.

## AWS anchor

- **Amazon ECS:** rolling replacement is common; blue/green can use CodeDeploy
  with target groups and traffic-shifting deployment configurations.
- **EC2/Auto Scaling:** replace instances in controlled batches, verify health,
  and protect required capacity; CodeDeploy supports in-place and blue/green flows.
- **AWS Lambda:** publish immutable versions, move an alias by weighted traffic,
  monitor alarms, and shift or restore the alias.
- **Amazon EKS:** Kubernetes Deployments provide rolling behavior; a progressive
  delivery controller can add canary analysis and promotion.

Azure App Service deployment slots, Azure Container Apps revisions, Google Cloud
Run revisions, managed instance groups, and Kubernetes controllers express similar
ideas. Translate by invariant: immutable version, traffic control, health evidence,
promotion decision, and recovery path.

## Choosing the strategy

Evaluate:

- acceptable error budget consumption and blast radius;
- startup time, connection draining, and session behavior;
- spare capacity and cost;
- compatibility between clients, services, schemas, and messages;
- whether traffic is representative and segmentable;
- quality and speed of telemetry;
- rollback feasibility and data consequences;
- regulatory approval or evidence needs.

Do not call a rollout “canary” merely because it starts small. A useful canary has
an explicit cohort, hypothesis, comparison baseline, observation window, automated
or owned decision, and promotion/abort criteria.

## Verification sequence

1. Confirm the intended artifact digest, target, configuration, and approval.
2. Run pre-deployment compatibility and capacity checks.
3. Deploy to the first bounded cohort.
4. Verify technical health and business outcomes against a baseline.
5. Promote in controlled stages or abort.
6. Confirm steady state, remove temporary capacity, and record evidence.

Use service-level and customer signals—availability, latency, correctness,
saturation, conversion, job completion—not only CPU and container health.

## Rollback, roll-forward, and stop

Rollback is appropriate when the previous artifact and data contract remain valid
and restoration is faster and safer. Roll forward when state has changed
irreversibly, the previous version is incompatible, or a small correction is safer.
Sometimes the correct action is to stop exposure with a flag while diagnosing.

Define decision authority, maximum observation time, and trigger thresholds before
production. Test recovery paths. A theoretical rollback button is not a recovery
capability until timing, permissions, dependencies, and schema compatibility have
been exercised.
