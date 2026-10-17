---
title: ACU DAQ channel, unit, clock, and steady-window confirmation checklist
status: provisional
last_updated: 2026-09-25
tags: [project/trident, doc/specification, domain/data, domain/experiments, facility/acu, status/provisional]
---

# ACU DAQ-003 confirmation checklist

Tags: #project/trident #doc/specification #domain/data #domain/experiments #facility/acu #status/provisional

This is the evidence request for the **2026-09-15 ACU-STNCL** run, not an accepted channel map or steady-state result. The [dated source inventory](BOX_DATA_DEPOSITS_GUIDE_2026-09-16.md#acu-deposit-source-and-dated-run-meaning) records the exact Box IDs and hashes. The staged `2026-09-15_channels.csv` has 145 unique native identities, but blank descriptions and no authoritative unit or installed-junction field. Its names are clues only. The source sample has `smpl_time`, `nanosecs`, `channel_id`, `severity_id`, and `status_id`; the meaning of the last two codes is unknown. [DAQ-001](../../coordination/tasks/DAQ-001.md) owns the native crosswalk and raw intake.

## What to send or confirm

For **each channel intended for a steady case**, provide an as-installed I/O or wiring schedule that links the exact `channel_id` and `name` to a physical tag and junction. Include the document title, revision/date, and the person who can confirm it matched the installation on 2026-09-15. A marked-up table or CSV is fine. A drawing location alone is insufficient: the [ACU Rev B sensor table](../geometry/first_extraction/ACU_loop_draft/ACU_Code_Package_RevB/sensors.csv) leaves `channel_name` blank, and some drawing references may not be installed.

| Channel or sensor family to reconcile | What the staged files establish | Missing physical, unit, calibration, status, and clock evidence | Window evidence needed |
| --- | --- | --- | --- |
| `NCDT1:HEAT:TC-*` thermocouples; ACU Rev B FIB/WT/PT references | Native names/IDs and sample times; Rev B candidate coordinates are separate evidence | One row per installed junction: physical tag, loop station and geometry revision, fluid/wall/insulation/air medium, radial depth and attachment, original value unit, DAQ conversion or raw voltage, thermocouple type, cold-junction method, calibration certificate/date/coefficients/uncertainty; status/severity meanings and acquisition clock | Junction temperature completeness, quality, drift, and sensor-pair agreement where applicable |
| `NCDT1:COOLER:RTD*`, `VELO*`, and `VFD1:stat_SpeedRPM` | Native identities only; RPM label is not a verified blower or flow boundary | RTD/velocity probe location and measurement plane, air path and inlet/outlet assignment, units/reference conditions, calibration, status, clock; identify which channels are command versus measured state | Stable measured inlet conditions, air flow or velocity, outlet state, and blower/control state |
| `NCDT1:GAS:*` pressure, temperature, flow, valve, and setpoint channels | Native identities only | Which gas circuit and physical port each belongs to, gauge versus absolute pressure, volumetric-flow reference conditions, units, instrument range/calibration, command versus readback, status, clock | Pressure/flow/control stability and evidence of no configuration change |
| `NCDT1:FLOW:FT21:*` | Nine related native fields, including `flow`, `pv`, and `t*`/`p*` names | Instrument manual or tag sheet defining each field, physical pipe and direction, original units and correction/reference conditions, calibration, status, clock; determine which field is accepted measured primary flow | Measured flow stability and quality if the selected model case uses prescribed flow |
| `NCDT1:HEAT:HE-MH1:HeaterEffectDuty` and other heater command/readback fields | A duty-like name, not a verified thermal-power measurement | Electrical meter and heater wiring, original units, command versus measured watts, sign, thermal-efficiency or loss basis, calibration, status, clock | Measured duty stability and any heater limit, mode, or setpoint transitions |
| `NCDT1:LEVEL:RADAR0`, ambient and other required state channels | Native identities where present | Tank/fill-state interpretation, ambient station and exposure, original units, calibration, status, clock; identify channels that are irrelevant to this run | Stable inventory and ambient; flag missing mandatory boundary channels |

For all families, the evidence should say whether the source value is raw, instrument-scaled, or already converted, and identify its original unit. Please include the DAQ software/export version and the status/severity codebook, including what marks invalid, disconnected, saturated, stale, or substituted values. If a record is unavailable, mark the field **unknown**; do not infer °C, K, watts, or L/min from a channel name.

## Clock and run identity

1. Confirm the exact run start/end and whether the dated folder and 52-row event CSV describe this same acquisition. Give the DAQ computer timezone on 2026-09-15, its clock source/synchronization or measured offset, what `smpl_time` and `nanosecs` mean, and the timezone used by the event record and operator note. The sample filename contains `-05`, but this alone does not prove event-clock alignment.
2. Identify any DAQ restart, clock correction, buffering, or delayed writes. The dated sample contains out-of-date rows and 46 decreases in successive 2026 timestamp strings; rows must be sorted/filtered by verified time and quality, not file order.
3. Supply the run sheet or operator confirmation of valve positions, heater limits/mode, cooler blower/air path and flow, pressure control, ambient, and any intervention during the candidate interval. Link each statement to a time and source revision.

## Candidate steady window and predeclared tests

The event note calls approximately **11:30–12:30 local on 2026-09-15** “fairly stable” near 237 °C and nominal 1.25 kW. This is the **first candidate interval**, not a certified steady window. If the local clock is confirmed as UTC−05 and aligned, it corresponds to 16:30–17:30 UTC; otherwise its UTC bounds remain unknown. Preserve this interval before comparing model predictions.

Before calculating a pass/fail result, record numeric tolerances and minimum hold duration for heater duty, cooler inlet/flow/state, ambient, primary flow/pressure, temperature drift, missing data, and sensor disagreement in the run's qualification config. Then, on quality-filtered synchronized samples, check: (a) no configuration event or transient inside the interval; (b) required-channel coverage and status codes; (c) slopes with uncertainty, drift and block-to-block consistency; (d) autocorrelation and effective sample count; (e) measured heater/cooler/ambient/flow stability; and (f) repeatability or sensor-pair consistency where available. Report raw count, missing fraction, mean, standard deviation, slope with uncertainty, effective count, and exclusions for every accepted signal, as required by the [data contract](DATA_CONTRACT.md#steady-reduction). A failed or unsupported test leaves the window diagnostic-only; choose and record a new candidate before fitting.

## Handoff sequence

1. User supplies the as-installed channel/wiring schedule, calibration/unit and status records, clock rule, and run sheet for this bounded ACU run; a responsible facility person confirms installation and event timing.
2. DAQ-001 checks IDs against the immutable dated registry and raw rows, records each evidence source/revision, and issues a versioned crosswalk with unknowns explicit.
3. EXP-001 applies the predeclared window tests. DAQ-004 may interpret events as candidate changes; EXP-002 may project only qualified, measured or explicitly assumed steady inputs into a simulation case.

No real-data fit or validation claim follows from this checklist alone. The [open data questions](../../coordination/questions/data/README.md) remain open until the corresponding evidence is reviewed.
