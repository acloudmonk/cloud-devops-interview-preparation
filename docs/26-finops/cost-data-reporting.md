# Cost Data, Visibility, and Reporting

[← Module overview](index.md) · [Allocation and unit economics](allocation-unit-economics.md)

Cost reports are trustworthy only when their scope, cost basis, data latency,
currency, adjustments, and allocation rules are explicit. Different questions
legitimately require different views.

## Cost-basis decisions

- **Unblended cost** reflects charges associated with usage line items before
  some account-level sharing effects.
- **Amortized cost** spreads upfront commitment fees across the benefit period.
- **Net cost** incorporates applicable discounts, credits, or adjustments where available.
- **Effective cost** attributes commitment economics to covered usage.
- **Invoice view** reconciles what is payable; it may differ from management views.

Definitions and availability vary by provider and billing construct. Never compare
dashboards until scope, basis, timing, taxes, credits, support, marketplace, and
currency treatment match.

## AWS data architecture

- Use Cost Explorer for interactive trends, filters, forecasts, and investigation.
- Use AWS Data Exports with CUR 2.0 for detailed governed analytics; consider FOCUS exports where interoperability is required.
- Store exports in a controlled S3 data product with catalog, quality checks, schema handling, and restricted access.
- Use Athena, a warehouse, or another governed engine for repeatable analysis; publish persona-specific dashboards.
- Use Cost Categories, account hierarchy, and allocation tags consistently across reporting and alerts.

Billing data can contain sensitive commercial and organizational information.
Apply least privilege, encryption, retention, audit, and row- or view-level controls.
Separate data-platform administration from unrestricted visibility of all rates.

## Data-quality controls

Track arrival freshness, record completeness, schema changes, duplicate ingestion,
currency, account coverage, allocation percentage, late provider adjustments,
marketplace charges, credits, refunds, and reconciliation with invoices. Preserve
raw immutable inputs and version transformation logic.

## Reporting by persona

- Engineering needs actionable daily drivers, resources, efficiency, and owners.
- Product needs unit cost, margin/value, demand, quality, and scenario choices.
- Finance needs forecast, accrual, invoice reconciliation, and variance explanation.
- Procurement needs demand coverage, rate, term, renewal, and concentration.
- Leadership needs value, material risk, trend, decisions, and accountable outcomes.

A dashboard is not an operating model. Every material view needs a review cadence,
decision threshold, action owner, due date, and measurement of realized outcome.

Return to the [module overview](index.md) when ready to continue.
