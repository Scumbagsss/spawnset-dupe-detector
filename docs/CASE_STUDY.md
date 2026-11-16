# Engineering case study — investigating suspicious activity

## Problem

Staff reviewing DayZ activity logs face two competing problems: too many individual events to inspect manually, and too little context to make a fair decision based on a single message.

The engineering challenge is to transform raw, imperfect logs into **reviewable cases** while preserving context and uncertainty.

## Design approach

**Normalize first.** Event sources are converted into a common representation with time, subject, operation and source-reference fields.

**Analyze sequences, not isolated lines.** Ordering, time windows and relationships can provide useful investigation context. No actual private detection signatures or thresholds are published.

**Persist review state.** Case records allow updates, reopening, dismissal or continued investigation without duplicating notifications each time the same batch is processed.

**Keep a human in the loop.** An alert supports an investigation; it is not a finding of misconduct.

## Synthetic illustration

| Time (invented) | Subject | Event | Review relevance |
|---|---|---|---|
| 10:00:00 | player-A | item-related event | Starting context |
| 10:00:08 | player-A | item-related event | Requires contextual examination |
| 10:00:14 | player-B | related event | May or may not be connected |

This table is **fictional** and does not reveal or reproduce real server logs or production detection logic.

## Engineering questions

- How is source evidence preserved when input arrives out of order?
- What happens after a log batch is retried?
- When is a case updated rather than duplicated?
- How are false positives and incomplete evidence represented?
- How are moderator permissions and audit history enforced?

These are the design questions this project addresses. The public interface does not demonstrate their full implementation.

## Verification boundary

In a reviewed private source snapshot dated **16 November 2026**, the related investigation subsystem had **27 locally passing tests**. The entire live service was not tested as part of that review, and no measurable false-positive rate or runtime reliability metric was provided.

## What remains private

Detector implementation, data schema, actual thresholds, live player identifiers, raw logs, credentials and deployment information.
