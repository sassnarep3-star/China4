# COORDINATION.md — Shared Task Board

This is the shared task board for all agent sessions working on this repo.
Claim a task by writing your session ID, status, and file scope, then commit and push immediately.
Do not edit files in another session's claimed scope.

## Session Note (arena-6eb49625)

Session `arena-6eb49625` runs on Arena-managed branch `arena/6eb49625-china4`.
Per Arena platform policy this session **cannot create or switch to other branches**,
so all session work (including integration) is committed on `arena/6eb49625-china4`
and the final PR is opened from `arena/6eb49625-china4` → `main`.
This substitutes for the `session-<id>/<task>` branch convention.
The user authorized autonomous operation for the full session (no review pauses).
As of claim time no other session has files in this repo; if another session appears,
it should claim tasks below that are still `unclaimed` and avoid files listed as
owned by `arena-6eb49625`.

## Task Board

| # | Task | Status | Owner session | Date (UTC) | File scope |
|---|------|--------|---------------|------------|------------|
| 1 | Repo review (line-by-line, flag irregularities) | completed | arena-6eb49625 | 2026-11-07 | README.md, full repo inventory |
| 2 | Research: China-side FX rules (SAFE/PBOC, official sources) | completed | arena-6eb49625 | 2026-11-07 | research/china-rules.md |
| 3 | Research: US-side tax & reporting (IRS/FinCEN, official sources) | completed | arena-6eb49625 | 2026-11-07 | research/us-tax.md |
| 4 | Research: conversion channels + penalty/fee breakdown | completed | arena-6eb49625 | 2026-11-07 | research/methods.md |
| 5 | Data tables (verified rows only, source link per row) | completed | arena-6eb49625 | 2026-11-07 | site/data/*.js |
| 6 | Site build (dashboard UI, landing + subpages) | completed | arena-6eb49625 | 2026-11-07 | index.html, site/**, assets/** |
| 7 | Verification pass (line-by-line vs official sources, link check, build check) | completed | arena-6eb49625 | 2026-11-07 | all of the above |
| 8 | Integration: PR to main, merge, GitHub Pages deploy, record result | claimed | arena-6eb49625 | 2026-11-07 | merge + COORDINATION.md updates |

## Handoff / Request Log

(none yet)

## Completed-Task Records (sources, verification, irregularities)

- Tasks 1–7: original repository contained only the README heading; no substantive pre-existing claims to review. Added research, dashboard, data, flagged issues and verification notes. Primary evidence linked in site records (SAFE, tax authorities, IRS, FinCEN, CBP and govinfo); provider-specific statements attributed to provider. Unverified fees, penalties and availability are on the Flagged page. Local reference/source checker, JavaScript syntax and HTTP smoke tests passed; these do not establish legal correctness or remote source availability.
- Task 8: PR opened, merge and deployment pending.

## PR / Merge Record

PR: https://github.com/sassnarep3-star/China4/pull/5 — merge and deployment pending.
