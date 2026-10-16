# VCU geometry and sensors: a handoff for Codex on HPC

Prepared 2026-10-15. **Working draft, not an approved installed configuration.**

## Start here

The goal is to resolve what the **Rev9 CAD actually supports**, then give the experimental team a short list of measurements and records that CAD cannot supply. Support both the 1-D system model and CFD/conjugate heat-transfer model. Keep the same definitions in both.

1. Transfer this repository folder to HPC. Keep its directory structure.
2. Unzip `reference/VCU_Rev9_CAD_Model_Package.zip` into a separate working directory. The archive contains the supplied package unchanged, including its source STEP, tables, scripts and qualifications. Its Rev8 comparison files are historical context only.
3. Give Codex this document and the prompt below. Tell it where the extracted Rev9 package and template folder are located.
4. Ask it to return a CAD findings report and the remaining experimental questions. Review those before changing the workbook or baseline.

**You do not need to ask the experimental team to recover coordinates already available from CAD. You do need them to identify the installed hardware, sensing locations and acquisition channels.**

For the complete requirements register, use `generated/requirements_and_evidence.md`. The friendly intake forms are in `inputs/VCU_inputs.xlsx`; the generated LaTeX is `generated/VCU_control_package.tex`.

## Prompt to give Codex on HPC

```text
Read docs/HPC_GEOMETRY_SENSOR_HANDOFF.md in the VCU control-template repository.
I will provide the path to the extracted VCU_Rev9_CAD_Model_Package.

Work through tasks G01-G08 and S01-S06 below. First inspect the supplied
structured data and its qualifications; use the exact hashed Rev9 STEP for
independent checks when useful. Preserve all source files. Put new analysis,
scripts, geometry variants and reports in a separate work/output directory.

Keep five kinds of information separate: CAD-derived geometry, installed
measurements, reported information, modeling assumptions and approved choices.
No CAD result is an installed measurement or an approval. Preserve unknowns
as null. Do not import ACU values, Rev8 dimensions or inferred DAQ mappings.

The user means position around the pipe circumference by sensor inclination.
Keep that angle separate from pipe inclination and probe-axis direction.
Preserve reference points, projected stations and actual sensing points as
different entities. Do not relabel mounting centroids as sensing junctions.

Produce the six deliverables and acceptance checks specified below. Resolve
what the evidence permits. For each remaining item, explain what cannot be
determined and give the experimental team one concrete information request.
Record proposed repairs or modeling choices separately with their effects.
Do not silently modify the source package, workbook baseline or approvals.
Do not run experiments or send messages to the experimental team.
```

## What is authoritative for this analysis?

The **candidate CAD baseline** is the supplied Rev9 structured package, issue 2026-10-08, drawing VCU-R9-E01. Its source is:

`source/_STEPFILE_UTDTloopWithOpticsAndHXRev9_9_18_26.step`

Expected STEP SHA-256:

```text
78c6ae52bf39084fbd9b1306d28dcbe2c1c4d5fccd334b0e68c861022a1bfbcf
```

The source describes native millimetres, SolidWorks 2026/AP214, export 2026-10-06T16:40:01. Verify the hash before using revision-specific face references. Face numbers belong to this import and extraction environment; they are not persistent identifiers for arbitrary reimports or revised CAD.

| Source inside the Rev9 package | Use it for | Qualification to preserve |
|---|---|---|
| `README.txt`; `MANIFEST.json` | Definitions, scope, provenance and limitations | Read these before extracting values |
| `data/VCU_Rev9_Engineering_Data.json`; `VCU_Rev9_Data_Dictionary.json` | Combined model and field meanings | Preserve nested evidence, statuses and nulls |
| `data/VCU_Rev9_Dimensions.csv` | 199 quantities with units, basis and source | Precision is not measurement uncertainty |
| `data/VCU_Rev9_Segments.csv`; `VCU_Rev9_Pipe_Axes.csv`; `VCU_Rev9_Coordinates.csv` | Eight main-loop segments, component axes and 57 reference points | Axis bounds, chords, projected spans and hydraulic lengths differ |
| `data/VCU_Rev9_Diameters.csv`; `VCU_Rev9_All_Cylindrical_Faces.csv` | Diameter evidence and detailed face inventory | Local spool IDs cannot establish the main-loop bore |
| `data/VCU_Rev9_Sensor_Stations.csv`; `VCU_Rev9_Contact_Solutions.csv`; `VCU_Rev9_Probe_Shafts.csv` | Reference stations, all returned contacts and seven external sheaths | These do not define junctions or acquisition identities |
| `data/VCU_Rev9_Heater_Clamps.csv`; `VCU_Rev9_Branch_Connections.csv` | Mechanical clamps and extended-axis crossings | Neither active heating boundaries nor physical tee planes are established |
| `data/geometry.json`; `data/reconstructed_bends.json`; `raw/` | Derived geometry and the supporting extraction | Reconstructed surfaces need qualification |
| `scripts/`; `scripts/environment_versions.json` | Reproduction and independent checks | Revision-specific paths/face selections; inspect before executing |
| `VCU_Rev9_CAD_Engineering_Drawings.pdf`, sheets 1-8 | Human review of the same package | Drawings are not an installed survey |

The template's `reference/rev9_extraction.json` is a convenient subset, not a substitute for all the source data above. `reference/source_manifest.json` locates the other supplied notes and Phase 0-4 drafts and records their hashes. `reference/REV9_ARCHIVE.md` documents the portable archive.

Do not use the supplied Rev8-based VCU overview PNGs as dimensional evidence. Do not use ACU drawings, ANEC labels or ACU channel names as VCU evidence. Rev8 comparison files in the unmodified Rev9 archive must remain comparison-only.

## Known CAD facts and open qualifications

These are reference checks, not newly measured values. The full precision remains in the source tables.

| Item | Supported CAD information | What remains open |
|---|---|---|
| Main-loop order | B-C upcomer; C-D upper-left bend; D-E cooler; E-F upper-right bend; F-G downcomer; G-H lower-right bend; H-A heater; A-B lower-left bend | Confirm this geometry represents the installed revision |
| Straight axes | B-C 1219.200 mm; D-E 1352.550 mm; F-G 1228.668560 mm; inclined axes 10.800 degrees | Installed dimensions, tolerances and gravity alignment |
| H-A heater leg | Projected span 1346.496215 mm; two unique pieces total 1353.698560 mm; projected overlap 7.202345 mm; transverse offset 0.151551 mm | Exact joined hydraulic centerline is **null**, not the sum or projected span |
| Three torus bends | R57.15 mm; A-B and E-F 79.2 degrees / 78.998489 mm; C-D 100.8 degrees / 100.543531 mm | Installed radii, bore and manufacturing deviations |
| G-H lower-right bend | Chord 86.619443 mm; recovered supporting-surface spine 98.265651 mm; G/H endpoint residuals 0.168531 / 0.145883 mm | Exact continuous hydraulic centerline unresolved; recovered spine is qualified |
| Main pipe and local spools | Main OD 33.401 mm; local exit ID 26.924 mm, LF/combined spool ID 26.6446 mm, PTC/JTC mounting spool ID 25.4 mm | Main swept-body bore absent; no loop-wide ID or wall thickness may be inferred |
| Cooling jacket | Shell length 1017.5875 mm; with end plates 1030.2875 mm; shell OD/ID 88.9 / 77.9272 mm; each plate 6.35 mm | Active heat-transfer limits, flow routing, contacts and actual control/measurement boundaries |
| Heater clamps | Four 50.8 mm-wide clamps; centers from H at 109.941860, 478.241860, 859.241860, 1214.841860 mm; outer mechanical span 1155.7 mm | Active heater locations/lengths are **null**; clamp edges are not energized edges |
| Exit branches/tank | TLEP and BREP tube lengths 469.9 mm; tank outer-axis length 311.15 mm; TLEP-OUT and TANK-IN coincide geometrically | Actual internal connectivity, fill level, valve/vent states and model boundaries |
| Branch crossings | TLEP crosses at D+50.800 mm; BREP at H+19.769579 mm; branch IN planes are 4.0005 mm outward from these crossings | Extended-axis intersections are not physical weld or tee locations |
| Hoses and drain | Each hose modeled centerline 544.189360 mm; simplified drain geometry supplied | Hose bore, actual valve passage/connectivity and loss coefficient unknown |
| Sensor references | 12 STC + 4 LF + 5 PTC (including PTC-X) + 2 JTC = 23 logical references; 21 on main loop | Installed count, actual sensor identity, junctions, optical active extent and channels |
| STC contacts | 21 returned closest-point solutions for 12 bodies; STC-01 gap 1.0455 mm; STC-01/06/07/12 have multiple solutions | No certified sensing junction or sensing footprint is defined |

The jacket annulus hydraulic diameter 44.5262 mm assumes a concentric, unobstructed annulus. It is **not** the main-pipe hydraulic diameter. A closed endpoint traversal does not prove a watertight fluid domain or an exact physical flow path.

Reported notes mention nominal 1.049-inch main ID, 316L Schedule 40 pipe, about 2-inch fiberglass insulation and 1/4-inch heater insulation. Keep these as **reported information requiring confirmation**, separate from CAD and installed measurements. Do not use them to fill missing CAD bore or insulation fields automatically. See source IDs MAT and HEAT in `reference/source_manifest.json`.

## Coordinate and angle rules

The supplied CAD-to-local transform is:

```text
B_CAD = [580.490685642161, -2830.921838891466, 1990.8865097103596] mm
x = B_CAD_Z - CAD_Z
y = CAD_Y - B_CAD_Y
n = CAD_X - B_CAD_X
```

This is a right-handed drawing frame. Its y direction is drawing-up; the installed relationship to gravity needs confirmation. Preserve out-of-plane n coordinates for branches, ports, sensors, hoses and valve.

A-H are straight-cylinder axis bounds. Use separate, clearly named virtual sharp corners if needed. A tape measurement from a fitting edge is not automatically a distance from A-H: record the measured datum and its offset to the chosen axis endpoint.

For a straight segment, define its unit tangent **t from the named start toward the named end**. Compute axial station by projecting the point minus the start onto t. Retain distance from both ends and any out-of-range flag. Do not replace axis distance with drawing horizontal distance.

**Proposed circumferential convention, requiring team adoption:** project an explicit up vector perpendicular to t and normalize it to obtain e0. Define e90 = t cross e0. For a vertical segment this projection degenerates: explicitly use projected drawing +x as the fallback and record that choice. Record the near-parallel threshold used by software. Derive theta with atan2(r dot e90, r dot e0), where r is the point's radial displacement from its projected axis point. Wrap theta into [0,360) degrees. A zero or unresolved radial displacement has an **undefined angle**, not zero.

The prototype uses drawing +y as up and +x for vertical segments. The HPC pass must reconcile this with the installed gravity vector before calling the result a physical top-relative angle. Positive angle is right-hand rotation about t; show t and the viewing direction on each cross-section.

For curved segments, define a qualified local tangent and continuous frame first. Do not apply a straight-leg projection across a bend. Keep these as separate fields:

- `pipe_inclination`: axis orientation relative to a stated gravity/up reference.
- `circumferential_angle`: where the point sits around that axis; this is the user's requested angle.
- `probe_axis_direction`: a separate vector/orientation, if needed for insertion geometry.

## Geometry tasks for HPC

All G tasks are owned initially by the computational/CAD team. A computed result remains CAD-derived; a proposed simplification remains a modeling assumption until reviewed. Every task applies to the Rev9 candidate only.

| ID | Task and purpose | Source/locator | Return and stopping rule |
|---|---|---|---|
| G01 | Verify source, frame, units and endpoint definitions so both models share one geometry | STEP hash; README Coordinate Frame; Coordinates rows A-H; Segments | Reproduce transform, segment signs, station bases and main-loop traversal. Flag differences; never silently relabel corners |
| G02 | Recheck H-A overlap/offset and G-H reconstruction before defining hydraulic lengths | Segments heater/lower-right bend; Pipe Axes; geometry/reconstructed_bends; source faces | Classify which limits are exact, projected or reconstructed. If CAD cannot establish a continuous path, preserve null and give separately named repair options with length/displacement effects |
| G03 | Establish which components really contain an internal passage | Diameters; All Cylindrical Faces; source solids | Map each ID to its own component/axial extent and evidence. Distinguish outer cylinders, cavities and solid placeholder bodies. Report absent bores; do not invent them |
| G04 | Build the branch/tank/jacket/port/hose/drain topology needed for model boundaries | Branch Connections; Pipe Axes; Coordinates; Engineering Data | Connection graph with source faces, coincidence residuals and confidence. Separate geometric coincidence from verified fluid connectivity. Flag terminal planes needing experimental disposition |
| G05 | Separate mechanical, heated, cooled and insulated spans | Heater Clamps; jacket dimensions/planes; supplied notes MAT/HEAT | Mechanical span map plus explicit null active spans. Identify available coordinates for future heater/insulation entries; CAD alone cannot determine energized coverage |
| G06 | Generate a qualified 1-D geometry view | G01-G05; existing template Geometry inputs | Segment/branch lengths, elevation changes, areas/perimeters where supported, and missing parameters. No exact total loop length or fluid volume from unresolved path/bore |
| G07 | Assess CFD/CHT geometry readiness | Original solid inventory plus G02-G05 | List gaps, overlaps, missing bores and proposed solids/fluid regions. Any repaired/idealized CAD is a separate variant with parameters, volume/area changes and source-to-model traceability |
| G08 | Extend input-driven diagrams without changing evidence status | Template scripts/generate.py; generated geometry/sensors JSON; Rev9 coordinates | Dimensioned overview, branch/port view and sensor cross-sections generated from one data set. State CAD versus measured overlay and schematic versus geometric curves. Do not let rendering offsets alter coordinates |

Do not attempt to recover insulation composition, roughness, contact resistance, physical supports or operating states from an unlabeled CAD shape. Search for explicit evidence, then leave unresolved items for the team.

## Sensor tasks for HPC

All S tasks are owned initially by the computational/instrumentation analysis team; actual hardware/channel verification belongs to the experimental instrumentation team.

| ID | Task and purpose | Source/locator | Return and stopping rule |
|---|---|---|---|
| S01 | Audit all 23 logical references so none are lost or double-counted as independent hardware | Sensor Stations, keyed by sensor_id; source assembly/reference paths | Stable drawing-reference inventory. Preserve shared LF/PTC mounts, PTC-X and the two jacket-port JTCs; do not infer unique physical-sensor count or DAQ names |
| S02 | Recompute stations and circumferential reference-point angles | Sensor Stations actual/projected XYZ; Contact Solutions; local frame | Axial/radial/angle coordinates with datum, basis and qualification. STC-02 check: B+116.68608092269051 mm; selected local point [-5.796806986985757,116.68608092269051,15.39538011145487] mm. This is a CAD reference, not a measured junction |
| S03 | Preserve contact ambiguity instead of selecting a convenient point | All 21 Contact Solutions; STC-01/06/07/12; STC-01 gap | All pipe-side/body-side solution pairs and derived station/angle alternatives. Do not interpret returned solution ranges as physical sensing footprints or statistical uncertainty |
| S04 | Identify what external sheath geometry can establish | Probe Shafts, seven rows; LF/PTC/JTC mounting centroids | Reference mount and external sheath endpoints/axis/OD, with source paths. Leave insertion depth, junction and optical active length unknown unless explicit evidence encodes them |
| S05 | Design measurement-to-model mapping for both approaches | S01-S04; template Sensors/Calibration; register C21-C33 and M04/M21 | Map each observation to wall/fluid/coolant domain and a spatial/temporal sampling definition. Keep proposed mapping separate from verified junction/channel identity; distributed fiber needs chainage and active sampling grid |
| S06 | Produce a short physical verification sheet | Remaining S findings; SNOTE PTC-X conflict; P0-02/P1-02 requests | One row per required installation/channel/calibration confirmation, with picture/datum and exact evidence requested. Do not discard PTC-X merely because the notes call it a fluke |

Use names such as `reference_point_xyz`, `projected_axis_xyz` and `sensing_point_xyz` rather than a single ambiguous `sensor_position`. Keep `sensing_point_xyz = null` when it is not established. A mounting centroid on the axis has no circumferential location without a second, physically meaningful point.

## What the experimental team will still need to supply

Send this list after HPC has removed questions already answered by qualified CAD evidence. A labeled photo, marked drawing or certificate is often more useful than a prose answer.

| ID / owner | Please provide | Why it matters / applicability | Current evidence and question |
|---|---|---|---|
| E01 Facility/geometry lead | Installed revision/date, overall photos, change list, datum locations and gravity/tilt survey | Establishes which CAD applies; both models | Rev9 is a candidate only. Does installed VCU match it? |
| E02 Geometry lead | Main bore/OD by section; bend dimensions; local restrictions; measurement method and uncertainty | Flow area, wall storage, pressure loss; both models | Main bore absent from CAD. Which nominal pipe information is actually installed? |
| E03 Experimental thermal lead | Insulation product/layer, thickness and coverage endpoints by section; gaps, seams, supports and contacts | Heat loss and CHT solid domains | Notes report insulation, but no verified section-by-section survey is supplied |
| E04 Electrical/experimental lead | Each heater's active start/end, element identity, wiring/supply, measured real power, control sensor and electrical schematic | Heat input distribution, storage and net-fluid-duty accounting | CAD clamps are mechanical only. Which lengths are energized and how is power measured? |
| E05 Coolant/experimental lead | Flow routing/direction, working fluid, active contact limits, sensor/meter planes, measured flow, setpoints and feedback sketch | Cooler boundary conditions and calorimetry | Geometric port labels do not establish flow order or operating boundary conditions |
| E06 Facility lead | TLEP/BREP/tank/valve connectivity and states, fill level, vent/pressure reference and terminal boundary photos | Exit-pipe/tank boundaries; both models | CAD axes/coincidences do not establish physical or thermal boundary conditions |
| E07 Instrumentation lead | Installed sensor count/type/serial, drawing-ID-to-cable-to-DAQ crosswalk, channel units and data-file column | Observation identity and reproducibility | CAD labels are not encoded acquisition labels. Resolve PTC-X and shared mounts explicitly |
| E08 Instrumentation/geometry lead | Actual datum-to-junction station, circumferential position, insertion/radial location, mounting/contact method and uncertainty | Wall/fluid distinction and CFD/1-D observation locations | CAD references are not verified junctions. Include how a measured corner relates to A-H |
| E09 Optical instrumentation lead | Fiber route, active start/end, chainage direction/origin, spatial grid/gauge length, readout channel and TC pairing offsets | Distributed measurement mapping | Mounting location alone does not locate optical measurement samples |
| E10 Instrumentation lead | Last calibration date, certificate, range, correction, uncertainty with coverage factor/confidence, response characteristics and next-due status | Measurement uncertainty and transient comparison | No CAD-derived calibration; distinguish vendor specification from calibration uncertainty |
| E11 DAQ/analysis leads | Sampling rates, filters, clock offsets, time stamps, synchronization event and channel exclusions | Phase baseline, relaxation and transition interpretation | Physical co-location and synchronized samples must be demonstrated |

For each reply record: configuration ID; item ID; value and units; measured/observed date; method; uncertainty basis; evidence filename and exact locator; contributor; reviewer; and unresolved limitations. A reported value may be useful while remaining unverified. Blank means unknown, not zero.

## Connection to the draft STNCL Phases 0-4

The original plans remain **draft requirements**, not confirmed Nick Luciano approvals or authorization to operate. The existing workbook's **Phase requests** tab has 17 detailed requests; **Review issues** has nine conflicts/gaps. Geometry/sensor priorities are:

- **Phase 0:** E01-E11 configuration, geometry, channel tracing, calibration, environmental measurements and synchronized checkout. Electrical VCU heating requires its own measured-power/control-volume definition, replacing heater secondary-fluid calorimetry where the draft uses it.
- **Phase 1:** establish actual TC/fiber pairs and their spatial offsets, baseline quality and channel exclusions. The draft requests co-located comparisons while Phase 0 notes not all sensors are co-located; the usable-pair rule needs resolution.
- **Phase 2:** confirm sensor-to-zone mapping, initial temperature map, branch/valve inventory and residual heat exchange. Reconcile the Method's in-loop recirculation with Required Outputs' tank-uniformity-before-each-fill wording. Electrical input being off does not eliminate stored heater energy.
- **Phase 3:** preserve accepted-state sensor windows and electrical/coolant measurement boundaries. Freeze model/geometry/property versions before blind comparisons; recalibration consumes a validation case.
- **Phase 4:** preserve sensor/flow inference geometry, usable exchanger temperature differences, transition clocks and actual achieved conditions. The matrix is five unique states plus a repeat. Define the electrical versus net thermal heater-duty coordinate consistently before using it for inference.

The campaign drafts focus on Prop-30. The user also permits VCU air and water experiments; fluid/circuit/run applicability and acceptance limits must be stated separately. ACU HITEC/water information is outside this VCU baseline.

## Required HPC returns

1. **`CAD_FINDINGS.md`** — readable findings for G01-G08/S01-S06, what was resolved, what remains unknown, and links to evidence.
2. **`geometry_sensor_evidence.csv` or JSON** — one row per assertion: stable field/record ID, purpose, component/sensor ID, value, unit, responsible team, applicability/configuration/revision, evidence kind, evidence status, review status, source file/hash/locator, method, uncertainty or qualification, unresolved question, and disposition. Keep actual measurements and approved choices in separate records from CAD derivations.
3. **`sensor_reference_coordinates.csv` plus full JSON** — original reference XYZ, projected XYZ, segment/datum, station from both ends, radial position, circumferential angle/frame, solution index and reference basis. Include sensing-point/DAQ fields as null unless supported; retain nested alternatives in JSON.
4. **`MODEL_GEOMETRY_CHOICES.md`** — candidate 1-D and CFD/CHT representations, required assumptions/repairs, affected lengths/areas/volumes, and decision owner. Do not mark a proposal approved.
5. **`EXPERIMENTAL_INFORMATION_REQUEST.md`** — the remaining E questions, prioritized by what blocks the intended model/test, each with a concrete return format. Separate measurements from records/identity confirmations.
6. **Reproducible analysis and labeled vector diagrams** — scripts, environment versions, exact input hashes and a short run guide; geometry overview, branch view, sensor reference map and angle convention. Add a compact validation result and include failures/limitations.

## Acceptance checks before handing results back

- Confirm the source hash, mm/degree units, right-handed frame and forward/inverse coordinate transformation.
- Reproduce supplied axis stations, endpoint sums and jacket dimension chain within explicitly stated numerical tolerances. Tolerances for computation are not fabrication tolerances.
- Retain the 23 logical reference inventory, 21 main-loop references and two port references. Check shared mounts without inventing acquisition mappings.
- Preserve all STC contact alternatives and the STC-01 gap. A diagram's displaced label/marker must not change stored XYZ.
- Check circumferential-angle round trips, vertical/near-vertical fallback and undefined radial cases. State axis direction and sign on diagrams.
- Keep main bore, active heater span, unverified sensing positions and unresolved exact hydraulic lengths null. No automatic nominal fill, silent healing or extrapolated channel labels.
- Demonstrate that measured inputs change diagram labels/positions from the same data source. Keep CAD, reported and measured overlays distinguishable, including diagram captions.
- For 1-D and CFD/CHT, list what blocks a defensible model separately from what permits an explicitly provisional model. No generated geometry is automatically an approved choice.

## Returning results to the local LaTeX package

Return the reports and supporting files first. The package maintainer reviews each claim, adds accepted evidence to the relevant form/register, and records a separate model choice where needed. The workbook is the editable input; LaTeX and diagrams are generated outputs. Follow `MAINTAINER_START.md` for regeneration.

Do not overwrite the workbook with CAD output or silently replace the open LaTeX document. Preserve the existing candidate baseline and its qualifications until a reviewed change is recorded. No GitHub push or baseline approval is implied by this handoff.
