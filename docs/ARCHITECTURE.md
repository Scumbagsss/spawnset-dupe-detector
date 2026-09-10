# Architecture

## Purpose

Advanced DayZ SpawnSet abuse detector with confidence scoring, case management and recovery monitoring.

## Boundary

The public repository documents only the system boundary. The production edition contains private implementation details, persistence schemas, operational thresholds, adapters, credentials and deployment configuration.

## Components

- **Discord interaction layer** — buttons, forms, commands and/or event listeners.
- **Domain service layer** — validates state and executes the project-specific workflow.
- **Persistence/integration layer** — private production storage and external adapters.
- **Observability layer** — staff logs, error handling and operational feedback.

## Workflow

1. Ingest player activity batch
2. Build normalized player timeline
3. Evaluate suspicious relationships and cycles
4. Calculate private confidence model
5. Open/update moderation case

## Why the implementation is private

The production code is a commercial/private implementation. The portfolio edition intentionally prevents direct deployment while still documenting the engineering scope.
