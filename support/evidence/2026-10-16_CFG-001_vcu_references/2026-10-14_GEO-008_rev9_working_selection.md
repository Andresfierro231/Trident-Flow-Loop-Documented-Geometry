---
title: VCU Rev9 working geometry and installation selection
status: provisional
last_updated: 2026-10-14
tags: [project/trident, doc/decision, domain/geometry, facility/vcu]
---

# VCU Rev9 working selection — 14 October 2026

Tags: #project/trident #doc/decision #domain/geometry #facility/vcu

Owner: geometry / agent-root-rev9-plots-20261014; task GEO-008.
This is the current working decision, based on the user's October 14 answers.
It supersedes the October 8 blanket rejection of Rev9 working sensor joins
and the earlier under-insulation interpretation of STC contact. Earlier
reports, native data and configurations remain historical evidence.

## User direction and interpretation

Rev9 is the best available geometry; work with it until better evidence is
given. Use corresponding Rev9 STC1–12 and PTC1–4 references as the working
numbered map. The user explicitly says STC5 changed location and directs use
of its Rev9 coordinates, and confirms PTC4's location. Change dates/run ranges
were not supplied; this decision does not relocate sensors in old runs.

| Reference | Working native channel / role | Decision |
|---|---|---|
| STC-05 | STC5, upcomer | Use station 942.186081 mm from B |
| PTC-04 | PTC4, lower H–A leg | Retain station 63.716137 mm from H |
| JTC-B | PTC5, jacket inlet | Explicit user-confirmed pairing |
| JTC-A | PTC6, jacket outlet | Explicit user-confirmed pairing |
| PTC-X | No channel | Exclude as suspected artifact; preserve original source row |
| LF-01–04 | Geometric mount references | No optical/native binding inferred |

The provider's jacket field named `flow_direction` is a geometric axis
direction, not evidence overriding the user's inlet/outlet pairing. The
working JSON preserves it as `source_geometric_axis_direction`; detailed
internal jacket routing remains unverified.

The user says all STCs should be on bare pipe. This defines local contact
conditions; it does not establish that entire vertical legs are bare.
The whole top D–E leg is uninsulated, explicitly including STC6/7 and PTC1/3.
The water jacket is still present; uninsulated does not mean exposed to room
air everywhere. Other insulation transition endpoints remain unknown.

Assume the entire lower straight H–A leg heated, from H-based station 0 to
1346.496215 mm, using the Rev9 projected union span. This is the user's
modeling assumption, not a measured electrical footprint or clamp envelope.
The package's active heater start/end/length fields remain null. Main pipe
nominal ID remains 26.64 mm, OD 33.401 mm.

Continue the Rev9 local frame: B is origin; x = B_CAD_Z − CAD_Z;
y = CAD_Y − B_CAD_Y; n = CAD_X − B_CAD_X. Plot drawing Y upward and retain
local gravity (0, −1, 0) as the previous working convention. The user directs
inclination to come from geometry; no independent installed gravity survey
was supplied. Geometry yields approximately 10.8° for the lower and upper
inclined legs. An old source called CAD-Z elevation; this is a historical
frame-label conflict, not a reason to rotate the current plot.

## Why H–A has a qualification

The extraction has two heater-leg cylindrical-axis pieces. Their length sum
is 1353.698560 mm, but the projected intervals overlap by 7.202345 mm.
Subtracting the overlap yields the 1346.496215 mm union span. The axes are
transversely offset by 0.151551 mm. Therefore the union is a useful working
span, but the extraction does not establish one exact connected hydraulic
centerline. This is unrelated to overlapping electrical heaters. G–H remains
a qualified reconstructed spline. Plot bends as dashed endpoint chords and
retain source length qualifications rather than silently healing geometry.

## Implementation and limits

The portable [working selection](../../config/facilities/vcu_provisional/rev9_working_selection_v1.json)
contains coordinates, station and length bases, user-selected bindings,
exclusions, thermal assumptions, source hashes and unresolved fields.
The [comparison bundle](../../reports/geometry/2026/10/14/2026-10-14_GEO-008_rev9_comparisons/README.md)
owns plots and reproduction. Existing solver cases are still Rev8; this
plotting task does not activate a solver migration or reprocess operating data.
Physical sensing tips, historical run applicability, electrical power split,
remaining insulation limits and exact connected centerlines still need evidence.
No CAD or images were opened. This choice replaces indefinite blocking with
explicit provisional inputs; it does not certify fabrication or calibration.
