---
title: Assess ACU site channel and instrument declarations against experimental needs
status: todo
last_updated: 2026-09-29
tags: [project/trident, doc/specification, domain/data, facility/acu]
---

# DAQ-006: ACU site-map evidence audit

Tags: #project/trident #doc/specification #domain/data #facility/acu

Owner: unassigned. Read-only evidence audit; no ACU operating-data processing while the 2026-09-29 user hold applies.

## Input and scope

Assess `acu-flowloop-site` remote branch `origin/feat/own-channel-map` at commit `b7e1714d25200f289061ab1430695f455a82cae1`: `site/channel-maps/acu_flowloop.toml`, `site/instruments/instruments.toml`, their README files, and the source CSV/workbook provenance. Reconcile exact native channel IDs against DAQ-001's bounded registry and DAQ-005's label questions when the user resumes that work. Do not infer a physical junction from a description alone or equate the branch with the 2026-09-15 installation without a dated facility sign-off.

## Permitted output and acceptance

A source-pinned candidate crosswalk and gap table under `docs/data/` or `reports/data/`, with one row per intended observation or boundary channel: native ID, instrument ID, facility/geometry revision, physical station and layer, source and run applicability, original/acquired unit, calibration/uncertainty, status, and confidence. Missing fields stay unknown. Link questions to [DAQ-004](DAQ-004.md) and [DAQ-005](DAQ-005.md). No real-data comparison or fit.
