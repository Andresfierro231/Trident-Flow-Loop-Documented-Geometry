---
title: Permit VCU solid-property extrapolation down to 5 C
status: accepted
last_updated: 2026-10-07
tags: [project/trident, doc/decision, domain/materials, facility/vcu, status/provisional]
---

# ADR-0033: VCU solid working ranges down to 5 °C

Tags: #project/trident #doc/decision #domain/materials #facility/vcu #status/provisional

## Decision and authority

On October 7 the user explicitly directed the 316L pipe, fiberglass and heater
strip density, specific heat and conductivity functions to be applicable down
to **278.15 K (5 °C)**. The user reports checking the pipe against another
extrapolation. The comparison table/source was not supplied or independently
reviewed. This authorizes a working extrapolation, not product validation.

New library [v3](../../config/materials/vcu_candidate_materials_v3.yaml) preserves
all functions, coefficients, units, upper bounds and out-of-range error policies.
Material identifiers remain the same; the library revision identifies the range
change. [v2](../../config/materials/vcu_candidate_materials_v2.yaml) is unchanged.
The current VCU insulation selection advances to v5 with the same v4 coverage
and thicknesses, selecting library v3. The old selection is preserved in
[v4 snapshot](../../config/facilities/vcu_provisional/insulation_v4_bare_cooler_2026-10-06.yaml).

The engineering reconstruction and property-range tests cover the new endpoint.
Earlier report copies and their numerical results remain historical v2 results;
their six property-range exclusions have not been recomputed. To reproduce
those results use v2 materials, the preserved v4 insulation snapshot and the
solver write-up copied into the original report. Future 5 °C studies use v3
materials explicitly and a fresh output bundle. No fluid properties change.

## Evidence and limits

The [change and run-triage bundle](../../reports/data/2026/10/07/2026-10-07_CAL-003_vcu_5c_properties_and_run_triage/README.md)
pins before/after files, tests and July acquisition metadata. Installed grade,
insulation products, source fits and calibration eligibility remain provisional.
