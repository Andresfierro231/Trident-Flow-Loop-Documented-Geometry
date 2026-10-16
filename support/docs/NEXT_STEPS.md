# Next development increment

The user has chosen editable tables/forms, generated LaTeX, both 1-D and CFD/CHT coverage, and circumferential sensor angles. VCU fluids are Prop-30, air and water; ACU fluids are HITEC and water. Keep facilities explicit and separate.

## Resolve before an installed VCU release

1. Confirm the physical VCU revision and survey the reference endpoints, bore/OD, bend geometry and installed angles.
2. Reconcile PTC-X, drawing IDs, actual channels, sensing junctions and fiber active extents. Add the calibration certificates and uncertainty basis.
3. Measure active spans for every electrical heater, identify each supply/circuit and add power measurement and control schematics. Mechanical clamp geometry does not establish heating coverage.
4. Identify coolant circuits, flow direction, sensor planes, measured flow, feedback and setpoint records.
5. Survey insulation layers and contacts by section; attach dated hardware photographs.
6. Record branch/tank connectivity, fill level, valve states, pressure/vent conditions and thermal boundaries.
7. Select original property sources for each fluid/material and verify units, composition, pressure and temperature applicability. Capture fit residuals, source uncertainty, comparison points and implementation tests.
8. Confirm Nick Luciano's approval status for STNCL Phases 0-4 and adapt heater accounting to actual VCU hardware. Reconcile Phase 2 conditioning versus fill/tank wording.

## Extend the prototype

- Add relative branch geometry for TLEP, BREP, tank, jacket ports and JTC-A/B. Keep out-of-plane coordinates.
- Add sensing-extent endpoints for fibers and insertion/junction geometry for probes. Preserve the distinction between mounts and sensing locations.
- Replace schematic bend connectors with independently qualified curves before producing hydraulic lengths or CFD geometry. Do not silently heal the Rev9 overlap/offset.
- Extend the three evidence-intake prototypes into repeatable multi-item records; add heater circuit and cooler feedback forms/diagrams.
- Add run records tying configuration, fluid/circuit assignments, raw-data files, calibration revisions and model revisions together.
- Have the team disposition the 17 phase requests and nine review issues; record named owners and approved plan revisions.
- Split the generated document into Configuration Control and Modeling Control releases sharing the same definitions and property registry, once the content is agreed.
- Add an easy desktop “regenerate” workflow or managed build pipeline after the team's operating environment is established. The present command is portable and does not require macros.
- Add release-specific input rules, approvals and change history. A validated drawing alone must not imply an approved experiment or model.

## Prompt for the next pass

Review the completed VCU evidence-intake forms against the 78-field requirements register. Preserve reference evidence, new measurements and selected choices separately. Identify conflicts and missing evidence before updating the baseline. Extend the next agreed form or branch/tank geometry feature while keeping the workbook, labeled diagrams and existing LaTeX source synchronized. Preserve Rev9 qualifications and unknown values; do not import ACU values, Rev8 dimensions or inferred channel mappings. Keep the experimental-team instructions short and practical.
