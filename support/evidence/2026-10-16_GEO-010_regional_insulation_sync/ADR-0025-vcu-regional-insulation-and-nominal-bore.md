---
title: VCU nominal bore and region-specific insulation candidates
status: provisional
last_updated: 2026-09-26
tags: [project/trident, doc/decision, facility/vcu, domain/geometry, domain/materials, status/provisional]
---

# ADR-0025: VCU nominal bore and regional insulation

Tags: #project/trident #doc/decision #facility/vcu #domain/geometry #domain/materials #status/provisional

## Context

The earlier [VCU-006 geometry candidate](../../reports/geometry/2026/09/26/2026-09-26_VCU-006_working_geometry/README.md)
used an approximate 26.9 mm main-loop ID; the regional insulation config
still used an earlier uniform 3-in estimate. On 2026-09-26 the user supplied
NPS 1 Schedule 40 dimensions, revised region-specific insulation estimates,
and candidate material functions. The user clarified that the heater's
ceramic-fiber strip is the only insulation outside its pipe.

## Decision

Use a **new, explicitly selected provisional VCU candidate** with 26.64 mm
main-loop ID, rounded from the nominal 26.6446 mm Schedule 40 calculation.
Keep local exit and spool bores separate. Assign approximately 2 in of the
user's fiberglass candidate to ordinary main pipe, and approximately 1/4 in
of the user's dense calcium–aluminum–silicate strip to the straight H–A
heater leg, with no second 2-in layer there. Preserve the prior VCU-006
candidate and its 3-in historical assumption as provenance.

Load the user-forwarded 316L, fiberglass, and ceramic functions only as
calibration-ineligible material candidates with explicit SI units, ranges,
and out-of-range errors. Extend the ceramic candidate's lower range from
293 K to 283.15 K by the user's explicit direction; label 283.15–293 K as
extrapolated. Do not extend the fiberglass curve below its stated 297 K.

The [VCU-007 intake](../../reports/geometry/2026/09/26/2026-09-26_VCU-007_bore_insulation/README.md)
records the dimensional arithmetic, catalog comparisons, numerical checks,
and remaining evidence needs.

## Consequences

The rounded bore slightly changes flow area and derived wall thickness.
The heater strip's much smaller thickness requires a distinct radial heat
loss path and explicit heater/strip contact interpretation. Ordinary room
temperatures may fall below the fiberglass fit's 297 K lower bound; current
behavior is to error rather than extrapolate it. Installed pipe grade and
bore, insulation part numbers, regional coverage, primary fit sources,
contact/gaps, and thermal uncertainty remain open. No solver automatically
selects these candidates and no facility validation is claimed.
