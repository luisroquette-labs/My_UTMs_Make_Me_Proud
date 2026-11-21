# Dashboard export contract

## Context

The dashboard consumes a storage-layer export with links, daily aggregates, events, and conversions. Aggregates and events may refer to slugs not present among the exported links. A missing daily aggregate is different from an explicit row with zero clicks. Event UTM values are snapshots of the click, while link UTMs can change later.

## Decision

Reject unknown slugs as export corruption. Build origins from event snapshots, not current link fields. Render missing days as `—` and measured zeros as `0`. Derive 7/30/90-day totals from the same aggregates used for each link. Produce a deterministic, offline, single-file HTML report without JavaScript.

## Consequences

The exporter must preserve referential integrity and event UTM snapshots. Tests must keep the missing-day, zero, window and origin distinctions. A malformed expiry currently escapes validation and is tracked in issue #5; this ADR does not endorse that behavior.
