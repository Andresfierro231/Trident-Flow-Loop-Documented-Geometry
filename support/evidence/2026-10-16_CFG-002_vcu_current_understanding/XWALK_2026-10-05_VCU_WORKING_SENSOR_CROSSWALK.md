---
title: Working VCU native channel to Rev 8 station crosswalk
status: provisional
last_updated: 2026-10-05
tags: [project/trident, doc/report, domain/data, domain/geometry, facility/vcu, status/provisional]
---

# Working VCU sensor crosswalk

Tags: #project/trident #doc/report #domain/data #domain/geometry #facility/vcu #status/provisional

**Facility:** VCU. **Use:** working location assignment for VCU runs selected
for comparison, subject to any run-specific exception. On 2026-10-05 the
user confirmed that `STC1`–`STC12` and `PTC1`–`PTC4` correspond to the
matching numbered stations in the 2026-09-26 Rev 8 table and reported no
known moved, replaced, or disconnected probes. This is an explicit
user-supplied installation interpretation layered over the source geometry;
the [site-map name check](../../reports/data/2026/09/29/2026-09-29_DAQ-007_vcu_0904_channel_name_crosswalk/README.md)
independently matches all 20 September 4 TDMS names but does not establish
their physical locations.

The coordinate source is
[`VCU_Rev8_Sensor_Stations.csv`](../geometry/first_extraction/better_vcu_extraction/VCU_Rev8_CAD_Model_Package/data/VCU_Rev8_Sensor_Stations.csv),
SHA-256 `71c8dfa3fad0292377171b4b9f9afa0b7c00f513933f757195e6bddd63443afe`.
Its reported local frame has B as datum, `x = B_CAD_Z − CAD_Z`, height
`y = CAD_Y − B_CAD_Y`, and normal `n = CAD_X − B_CAD_X`, all in mm. Values
below are rounded for reading; use the CSV for full precision. The model's
gravity choice and the source's conflicting elevation label remain an
explicit [open question](../../coordination/questions/geometry/README.md#oq-geo-009-vcu-source-elevation-versus-model-gravity).

| Native channel | Rev 8 reference | Region | x, height y, n (mm) | Coordinate meaning |
|---|---|---|---|---|
| STC1 | STC-01 | heater | 84.330, -78.828, 16.700 | pipe-solid surface reference |
| STC2 | STC-02 | upcomer | 0.728, 128.090, 16.685 | pipe-solid surface reference |
| STC3 | STC-03 | upcomer | -4.882, 596.187, 15.971 | pipe-solid surface reference |
| STC4 | STC-04 | upcomer | -2.617, 997.065, 16.237 | pipe-solid surface reference |
| STC5 | STC-05 | upper-left bend | 1.632, 1452.794, 16.663 | pipe-solid surface reference |
| STC6 | STC-06 | cooler | 143.987, 1495.933, 16.698 | pipe-solid surface reference |
| STC7 | STC-07 | cooler | 1533.643, 1250.410, 16.971 | pipe-solid surface reference |
| STC8 | STC-08 | downcomer | 1627.220, 1018.340, 16.904 | pipe-solid surface reference |
| STC9 | STC-09 | downcomer | 1631.075, 605.233, 15.897 | pipe-solid surface reference |
| STC10 | STC-10 | downcomer | 1625.039, 149.456, 16.746 | pipe-solid surface reference |
| STC11 | STC-11 | downcomer | 1629.247, -233.639, 16.441 | pipe-solid surface reference |
| STC12 | STC-12 | heater | 1496.777, -327.794, 16.700 | pipe-solid surface reference |
| PTC1 | PTC-01 | cooler | 208.580, 1484.201, -0.031 | probe mount centroid |
| PTC2 | PTC-02 | heater | 112.235, -83.776, -0.021 | probe mount centroid |
| PTC3 | PTC-03 | cooler | 1456.918, 1264.102, 0.245 | probe mount centroid |
| PTC4 | PTC-04 | heater | 1474.065, -323.924, -0.002 | probe mount centroid |

The site source describes STCs as outside-pipe surface thermocouples and
PTC1–PTC4 as immersed primary-loop probes. On 2026-10-05 the user directs
the working measurement operators to take **PTC1–PTC4 at the pipe
centerline** and **STC1–STC12 at the outside pipe surface**. The earlier
all-under-insulation interpretation is superseded for the cooler: the user's
2026-10-06 correction places STC6/7 provisionally on bare primary pipe
beneath the bare jacket. STC5 is assumed under insulation; the other scored
STCs remain beneath heater strip or fiberglass. This is a stated physical
assumption for model comparison, not a measured
junction-depth survey. Every Rev 8 row still says
`physical_junction_is_defined=False`; STC contact footprints and actual PTC
penetration depths are not measured by this table. The numbered station join
and working radial measurement layers are user-confirmed assumptions, while
calibration uncertainty remains separate.

`PTC5` measures jacket-water inlet temperature and `PTC6` jacket-water
outlet temperature per the user's 2026-09-29 clarification; jacket water
flows counter to the primary path. They are **not** mapped to the main-loop
PTC-01…04 coordinates. The Rev 8 `JTC-A/B` rows are jacket-port mount
references, but their pairing to PTC5/6 and the exact wetted measurement
planes remain unconfirmed. `Tank` and `Amb` have native names and candidate
roles but no accepted coordinates here. LF1–LF4 are not part of the 20
September 4 TDMS channels; their mount points are not optical sensing
positions.

For a scored model comparison, carry this crosswalk revision, run ID,
source hash, measurement layer, and uncertainty into each observation row.
Check the applicability of the site-map revision and any run-specific sensor
changes. A station coordinate does not itself qualify a run, accept a steady
window, or validate the predicted temperature.
