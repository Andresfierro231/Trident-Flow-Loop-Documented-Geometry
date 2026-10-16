# VCU configuration and modeling control template

An editable workbook generates labeled vector drawings, a standalone LaTeX document, and qualified coordinates for 1-D and CFD workflows. This is a working geometry and form prototype, not a released facility description or a complete CFD/system-model input deck.

## Start here

Read **[START_HERE.md](START_HERE.md)** for the five-step form workflow. Experimental contributors fill the three Form tabs and return evidence; they do not need to run software. The [maintainer guide](MAINTAINER_START.md) explains review and regeneration. The [modeling guide](MODELING_START.md) covers shared properties, boundaries and validation.

This increment adds **78 field requirements**, **17 phase information requests**, **nine review issues**, and **17 source records**. The three sample forms separate reference evidence, new responses and review. All physical/model choices remain draft.

From the repository folder, run `python3 support/scripts/build.py` to regenerate and compile the PDF, or `python3 support/scripts/generate.py` to regenerate outputs only. The root `main.tex` includes the generated standalone document. Review `support/generated/validation.json` before using any output. A failed build leaves prior figures in place and marks them stale. A successful build records the workbook hash. This prototype always marks modeling readiness false.

The generator needs Python 3.9+ and no third-party Python packages. The LaTeX document uses common packages including TikZ, longtable and booktabs. XLSX inputs must be literal values; formulas are rejected rather than relying on possibly stale cached values. The workbook itself has no macros and does not refresh drawings until the generator runs.

## Which sheet to edit

| Sheet | What the experimental or computational team enters |
|---|---|
| Start | Configuration identity, origin, editing conventions and review status |
| Form pipe / Form sensor / Form material | Three evidence-intake prototypes, with reference cells and separate responses; responses do not overwrite baseline tables |
| Requirements | Field purpose, proposed owner, applicability, requirement/evidence locators, evidence type, unresolved question, and separate selection/review fields |
| Phase requests | Concrete information returns from draft STNCL Phases 0–4, including electrical-heater adaptations |
| Review issues | Open conflicts, proposed owner, affected fields and needed resolution |
| Sources | Source IDs, revision/context, locator guidance and qualifications |
| Insulation regions | Ten whole-region coverage dropdowns, material/thickness and evidence; see [insulation guide](INSULATION.md) |
| Geometry | Segment lengths/directions, bend offsets, pipe bore/OD and insulation thickness |
| Sensors | Sensor type, segment, endpoint, distance along the pipe, circumferential angle, radius, DAQ identity and point meaning |
| Calibration | Instrument identity, calibration date/certificate, corrections, uncertainty, acquisition behavior and 1-D/CFD mapping |
| Thermal spans | Actual heater element boundaries, active cooling boundaries and mechanical jacket envelope |
| Fluids | VCU fluid choices, concentration basis, circuit assignment, operating range and property source |
| Materials | Selected property equations/tables, units, applicability, uncertainty and justification |
| Model choices | Physical branch/boundary states and the corresponding choices for each model |

Blank means unknown. Zero is an entered value. Printed decimal places do not establish measurement precision. Enter units only in the units specified by the column header. Calibration fields are free text so a date, certificate reference, quantity and units can be explicit; use ISO `YYYY-MM-DD` text for dates in this prototype.

## Geometry conventions

- Local origin B; x rightward, y upward, n out of the drawing.
- Traversal: B-C-D-E-F-G-H-A-B.
- A straight segment uses its axis-end length L and direction phi measured clockwise from +y: dx = L sin(phi), dy = L cos(phi). Up is 0 degrees, right 90, down 180, left 270.
- A bend uses signed endpoint offsets dx/dy. The rendered dashed connection is schematic. It is **not** the elbow arc or a CFD-ready surface.
- The imported heater direction is derived from its endpoint chord. Because the original CAD has overlapping offset heater pieces, this differs slightly from its 10.800-degree cylindrical-axis inclination. No continuous hydraulic centerline is claimed.
- The chain must close. Changing just one leg may require corresponding measured updates elsewhere. The program flags an inconsistent chain instead of changing other measurements to make it fit.
- The 0.1 mm closure threshold is a configurable numerical drawing tolerance, not a construction tolerance or an uncertainty estimate.

For example, `STC-04 / upcomer / C / 492.914 mm` means measure 492.914 mm back from endpoint C along the upcomer. The generator converts that to a station from B and draws the point. It does not measure a horizontal or vertical projected distance in place of along-pipe distance.

## Circumferential position

Circumferential angle alpha is separate from the pipe direction phi. It describes position around the pipe, not the direction a probe points.

For a nonvertical segment, zero is the uppermost radial direction: upward vertical projected onto the plane perpendicular to the pipe. For a vertical segment, zero is drawing +x because “top of the circumference” is undefined. Positive rotation is right-hand about the start-to-end segment direction. The angle guide is viewed along that direction (+s into the page).

The generator exports the explicit local basis vectors. A full point is computed only when radius and angle are both entered:

`point = axis_point + radius * (cos(alpha) * e0 + sin(alpha) * (tangent cross e0))`

Radius is the distance from the pipe axis to the particular reference being recorded; it is not automatically inferred from OD or assumed to be an insertion depth. Identify whether the point is a mount, pipe reference, sensing junction or sensing-extent reference. A point does not fully describe a distributed fiber sensing extent; that is future schema work.

The full-loop diagram shows axial stations. Entered angles also create per-sensor cross-section cards in the LaTeX and `sensor_angles_*.svg` files. The baseline intentionally has no entered angles or radii. All 3-D sensor points therefore remain null even though their axial locations are available.

## Evidence and facility separation

The starting geometry and sensor stationing come from the supplied VCU Rev9 CAD extraction, drawing issue 2026-10-08. Original imported segment/sensor rows are preserved in `support/reference/rev9_extraction.json`; initial workbook values are preserved in `support/reference/initial_tables.json`, with the added control records in `support/reference/initial_control_tables.json`. They are audit references, not alternate editable inputs. See `support/reference/SOURCES.md` and `support/reference/source_manifest.json` for source identity, exact supplied paths and read-time file hashes.

CAD sensor IDs are not confirmed DAQ names. The model contains PTC-X, while a supplied note calls it a fluke. The record remains visible with that conflict until the installed hardware is checked. JTC-A/B remain on the Calibration sheet; coolant-port geometry is not included in this main-loop drawing version.

The main-loop bore and insulation fields are blank pending installed/specification evidence. Heater clamp extents are not energized heater boundaries. Only the complete jacket envelope is prefilled. Enter one thermal-span row per heater element when the active boundaries are known.

VCU fluid choices are Prop-30, air and water. Prop-30 is reported as 30% propylene glycol by mass; product/formulation and original property source require confirmation. Circuit assignments and experimental temperature limits remain unknown. ACU HITEC/water configurations belong in a separate facility package. The generator explicitly rejects an ACU facility tag.

Material entries are reported candidates. No correlations have been independently qualified here. The supplied STNCL plans remain draft requirements until their approval status is confirmed. In particular, their secondary-fluid heater energy accounting needs adaptation to VCU's reported electrical heaters.

## Generated outputs

- `insulation.svg`: regional coverage diagram, with schematic bands and a three-state legend.
- `insulation_regions.json`: versioned computational export of coverage, boundaries, geometry qualifications and evidence.
- `geometry.svg`: dimensions and entered thermal spans.
- `sensors.svg`: automatic sensor labels and leader lines.
- `angle_convention.svg`: coordinate guide.
- `sensor_angles_*.svg`: added when circumferential angles are supplied.
- `VCU_control_package.tex`: standalone configuration record with seven technical pages, internal navigation, embedded TikZ figures, and linked appendices containing contributor guides, forms, review issues, requirements, model/material records and sources.
- `requirements_and_evidence.md`: searchable, readable export of the full requirements, phase requests, issues and source catalog.
- `resolved_inputs.json`: every input row in readable form for review and version comparison.
- `geometry_and_sensors.json`: endpoint coordinates, axial sensor stations, optional 3-D points, mapping fields and qualifications.
- `validation.json`: workbook hash, closure result, errors or qualifications.

The document summarizes selected calibration and geometry fields; the workbook and resolved-input export retain all fields. Form responses appear in the document but do not change selected baseline inputs automatically. Do not edit generated outputs as the master record. SVG text is escaped, and LaTeX input is escaped as text rather than executed as commands.

## Verification

```sh
python3 -m unittest discover -s support/tests -v
```

All 30 behavior checks pass. Behavior tests use the saved workbook under `support/tests/fixtures/` so contributors can change the working workbook without invalidating seed-specific checks; the build validates the actual working workbook separately. They cover loop closure, endpoint reversal, coordinate/angle transforms, unknown versus zero, geometry changes, impossible distances, duplicate IDs, VCU/ACU separation, full workbook regeneration, source references, complete review decisions, form responses reaching the document without changing baseline geometry, and configuration-first ordering with valid navigation targets. The seven original data sheets were also compared with the pre-edit workbook and remain unchanged.

The repository PDF build compiles the root entry point with repeated passes for contents and cross-references. The reorganized document has been rendered for page-layout review. These checks do not verify installed hardware or simulation validity; there are no spreadsheet formulas or macros.

## Next development increment

See `docs/NEXT_STEPS.md`. Extend the input schema and generator together; preserve source identity and unknown values. Avoid manually redrawing figures after measurement changes.
