# SpawnSet Dupe Detector

> **Portfolio showcase — production source is private and this repository is intentionally non-runnable.**

Advanced DayZ SpawnSet abuse detector with confidence scoring, case management and recovery monitoring.

## What it demonstrates

- VPP Player Activity parsing
- Suspicious death-cycle analysis
- Confidence scoring
- Case management
- Relationship analysis
- Watchlist/whitelist/ignore states
- Recovery and backfill scans
- Automated tests in private edition

## Technology

Python • discord.py • SQLite • Regex parsing • Heuristic scoring • Async workers

## High-level workflow

1. Ingest player activity batch
2. Build normalized player timeline
3. Evaluate suspicious relationships and cycles
4. Calculate private confidence model
5. Open/update moderation case

## Public interface preview

The public skeleton exposes only the architectural surface:

- `ingest_activity_batch(...)`
- `build_timeline(...)`
- `evaluate_case(...)`
- `calculate_confidence(...)`
- `update_case_state(...)`

The production implementations behind these methods are withheld. See [`NOTICE.md`](NOTICE.md).

## Repository contents

- `src/public_interface.py` — non-runnable interface skeleton;
- `docs/ARCHITECTURE.md` — high-level design;
- `examples/config.example.jsonc` — sanitized configuration shape;
- `LICENSE` — explicit all-rights-reserved notice.

## Status

Production-tested private project / portfolio edition.
