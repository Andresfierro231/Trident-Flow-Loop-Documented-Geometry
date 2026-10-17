---
title: Current VCU insulation coverage
status: provisional
last_updated: 2026-10-16
tags: [project/trident, doc/living_truth, domain/geometry, domain/materials, facility/vcu]
---

# Current VCU insulation coverage

Tags: #project/trident #doc/living_truth #domain/geometry #domain/materials #facility/vcu

The user's 2026-10-16 reaffirmation that upcomer and heater are insulated
agrees with the existing regional model. Missing surveys were incorrectly
represented as Unknown whole-region coverage in the shareable workbook.
Reported coverage must remain visible independently of product validation.

| Regions | Coverage | Workbook material | Approximate radial thickness |
|---|---|---|---|
| Upcomer, downcomer, all four corners | Insulated | MAIN-INS: fiberglass | 50.8 mm (2 in) |
| Straight heater H-A | Insulated | HEATER-INS: calcium-aluminum-silicate ceramic-fiber strip only | 6.35 mm (1/4 in) |
| Pre-cooler, jacket region, post-cooler (straight D-E) | Bare | None | Not applicable |

There is no additional 2-in fiberglass layer on the heater. LF-01 remains
covered per the user's corrected GEO-009 statement. STC local bare contacts
do not imply that their entire parent segments are uninsulated. Bare pipe
under the jacket still exchanges with coolant, not automatically room air.

Coverage and thickness entries are Reported; thicknesses are approximate user
estimates. Product numbers 5556K73 and 4057K14 are reported candidates, not
purchase/certificate confirmation. Original product fit data, thickness
uncertainty, local contacts and exact transition surveys remain unresolved.
None of those gaps justifies reverting the documented regional coverage to
Unknown. No new property functions or measured uncertainties are invented.

Source precedence: ADR-0025 records two regional material/thickness estimates;
ADR-0026's old full-loop assumption is superseded for straight cooler D-E by
the October 6/14 bare-cooler decisions; GEO-009 covers both upper corners and
LF-01. Current regional v7 preserves v6's numerical assignments and adds
explicit evidence scope; Rev9 working selection v3 carries the complete
workbook crosswalk. DRAFT-006 now contains seven insulated and three bare
regions. V6/v2/v1 snapshots and earlier reports remain unchanged.

These are current model-input and documentation records. Historical solver
cases/results remain tied to their original versions. This task does not
activate Rev9 solver migration, new simulations or operating-data processing.

Sources: [ADR-0025](../../../docs/decisions/ADR-0025-vcu-regional-insulation-and-nominal-bore.md), [ADR-0026](../../../docs/decisions/ADR-0026-vcu-full-loop-insulation-contact-and-fiberglass-range.md), [GEO-009](../../../docs/decisions/2026-10-16_GEO-009_covered_top_corners.md), [GEO-010](../../../docs/decisions/2026-10-16_GEO-010_regional_insulation_sync.md), [regional YAML](insulation.yaml), [working selection v3](rev9_working_selection_v3.json).
