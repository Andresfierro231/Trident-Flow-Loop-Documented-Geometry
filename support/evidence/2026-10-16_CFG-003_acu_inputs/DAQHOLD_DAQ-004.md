---
title: Convert ACU event record into traceable candidate operating changes
status: blocked
last_updated: 2026-09-29
tags: [project/trident, doc/specification, domain/data, domain/experiments, facility/acu]
---

# DAQ-004: ACU event-record adapter

Tags: #project/trident #doc/specification #domain/data #domain/experiments #facility/acu

**Priority date:** 2026-09-25, from the user's [verbatim prompt](../../docs/workflows/2026-09-25_WORK_PLAN.md).
Owner: unassigned until claimed on the active board.

**User hold, 2026-09-29:** Pause ACU operating-data analysis and event-to-boundary processing. Retain the source and this packet; resume only on new user direction. Channel/instrument-map review may proceed as a separate read-only evidence task under DAQ-006.

## Questions to answer before an ACU operating case

These are questions for the facility/run owner, not assumptions to fill from channel names or values. The [DAQ-003 checklist](../../docs/data/ACU_DAQ_003_CONFIRMATION_CHECKLIST.md) gives the channel-family detail; [DAQ-005](DAQ-005.md) gives the thermocouple-specific label questions.

1. Did the channel and instrument declarations in `acu-flowloop-site` at `b7e1714d25200f289061ab1430695f455a82cae1` match the **as-installed 2026-09-15 ACU-STNCL run**? Who can confirm additions, moves, disconnections, and the source document revision?
2. For each channel intended for comparison, what installed junction, axial station on the chosen ACU geometry revision, sensing layer/depth, and original engineering unit apply? Does the acquired value already include DAQ scaling? What calibration and uncertainty record applies?
3. What do native severity/status codes mean, and what were the DAQ and event-record timezone, clock synchronization/offset, run bounds, restarts, and delayed-write behavior?
4. Which event entries correspond to measured changes, and which are notes or commands? What are the heater's **measured electrical watts**, efficiency/loss basis, controller mode and state; cooler air flow with actual/standard reference conditions, inlet/outlet measurement planes, fan state, and shell-to-room condition; and ambient, primary-flow, valve, tank, and pressure conditions during the candidate window?
5. Is the operator's approximately 11:30–12:30 local 2026-09-15 interval the intended first steady candidate? Were there interventions within it, and which records establish them? Numeric steady-window tolerances must be declared before accepting it.
6. Where are the immutable run sheet, instrument/wiring schedule, calibration and codebook files, event log, and raw acquisition for this run, and who owns their revision history?

The ACU site map adds candidates, but its own text leaves some units, instrument aliases, and location layers open. No answer from VCU can close an ACU question.

## Scope and dependencies

Read the staged 2026-09-15 ACU event CSV identified by the
[selected-source manifest](../../docs/data/BOX_DATA_DEPOSITS_SELECTED_SOURCE_MANIFEST_2026-09-16.yaml)
and [deposit guide](../../docs/data/BOX_DATA_DEPOSITS_GUIDE_2026-09-16.md).
Coordinate with DAQ-001 on source identity and DAQ-003 on clock, units, and
physical meaning before interpreting values.

## Permitted outputs and checks

Add a streaming or bounded parser in a new `src/trident_thermal/data/` module,
focused tests, a documented event schema, and a compact source-hashed
candidate-event table. Retain source row, literal date/time/action/note,
interpretation status, units, and any applicability interval. Reject ambiguous
timezones and unsupported numeric conversions rather than inventing values.
An event is a candidate change until corroborated by measured DAQ channels;
it is not automatically a simulation boundary condition.
