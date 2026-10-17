---
title: VCU full-loop insulation, perfect contact, and fiberglass lower bound
status: provisional
last_updated: 2026-10-05
tags: [project/trident, doc/decision, facility/vcu, domain/geometry, domain/materials, status/provisional]
---

# ADR-0026: VCU insulation completion assumptions

Tags: #project/trident #doc/decision #facility/vcu #domain/geometry #domain/materials #status/provisional

## Context

The [VCU-007 candidate](../../reports/geometry/2026/09/26/2026-09-26_VCU-007_bore_insulation/README.md)
assigned 2-in fiberglass to ordinary main pipe and only a 1/4-in ceramic
strip to the heater leg. Its fiberglass fit was limited to the originally
claimed 297–533 K range. Coverage at bends and beneath the cooling jacket,
and thermal contact, were left unspecified.

## Decision

Per the user's 2026-09-26 departure handoff, use fiberglass from 283.15 K
(10 °C) to 533 K as a **working extrapolation** below the original 297 K
lower fit bound. Continue to error outside this range. Assume insulation
covers all eight main-loop segments and the full circumference without gaps.
The straight H–A heater segment has only the ceramic strip; all other seven
segments have fiberglass, including the D–E cooler leg beneath the water
jacket. Set interfacial thermal contact resistance to zero for insulation
interfaces with underlying pipe or heater surfaces.

The [VCU-008 bundle](../../reports/geometry/2026/09/26/2026-09-26_VCU-008_full_loop_insulation/README.md)
checks coverage, range behavior, source hashes, and the preserved v1/v2
history. These choices do not certify the installed wrap or validate
the property law.

## Consequences

Including fiberglass beneath the water jacket creates a substantial radial
resistance between primary pipe and coolant in a physical model. Its effect
must remain visible in resolved configurations and sensitivity runs; it must
not be hidden in a fitted cooler parameter without a declared model form.
Later facility evidence should confirm cooler-region wrap, heater/strip
layer order, contact gaps, cladding, and product-specific properties.

## User clarification — 2026-10-05

The user explicitly confirmed that VCU top pipe outside the water jacket is
insulated like other ordinary pipe segments and that the cooling pipe is
insulated beneath the jacket. This strengthens the coverage choice above as
the intended VCU model topology. The nominal fiberglass thickness, actual
installed resistance and contact, and whether a single cooler UA can be
identified remain separate evidence and calibration questions. The
`0.297722983459119 m` uncovered TOP length in VNV-007 is an ACU-shaped
synthetic example, not a VCU geometry measurement.
