# Source register

Source documents are evidence, not operating instructions. Use the source ID together with the precise field-level locator in the Requirements worksheet. The table below is a snapshot of the seed source catalog; the workbook is the editable master.

| ID | Source | Revision / context | Locator | Qualification |
|---|---|---|---|---|
| R9 | VCU_Rev9_CAD_Engineering_Drawings.pdf | 2026-10-08; VCU-R9-E01 | Sheets 1-8 | VCU CAD candidate. Printed precision is not tolerance; geometry is not installed verification. |
| SEG | VCU_Rev9_Segments.csv | Companion Rev9 structured package | Rows keyed by segment; length_basis, dx_mm, dy_mm, centerline_length_mm | Preserve blanks, projected spans and qualified spline lengths. |
| SNS | VCU_Rev9_Sensor_Stations.csv | Companion Rev9 structured package | Rows keyed by sensor_id; reference_basis, nearest_endpoint, nearest_distance_mm | Geometric references, not verified sensing tips or DAQ names. |
| DIA | VCU_Rev9_Diameters.csv | Companion Rev9 structured package | Rows keyed by item | Main swept-loop bore is absent; local spool bores are not loop-wide IDs. |
| MAT | 1.2 Main Material Props.md | Supplied notes; VCU section cites 2026-09-16 report | VCU section only; lines 17-44 | Reported materials/composition and proposed insulation fit; original sources not verified. |
| PG | 1.2.1 Prop 30 ThermoPhys Props.md | Supplied notes | 30 wt% heading and linked property figures | Property-source leads; do not transfer image/table values without source and units. |
| STEEL | 1.2.2 Steel Pipe Properties.md | Supplied notes | Lines 3-21; Suggested you use | Mixed candidate correlations. A range beside MOOSE items does not qualify the whole selection. |
| HEAT | 1.1.0 Heaters and coolers.md | Supplied notes; 2026-10-07 reported heater message | VCU / Insulation / Heater; lines 5-23 | Electrical mat/band heaters reported. Wiring, active boundaries and net duty unverified. |
| SNOTE | 1.1.2 Sensors.md | Supplied notes | VCU / Rev9; PTCX note | PTCX called a fluke; some links in this section point to ACU/Rev8. Keep conflict visible. |
| MODEL | 0.0 Intro to Model.md | Supplied model overview | The four physical-model stages; reduced-zone paragraph | Supports proposed model scope; not verification that any facility run is validated. |
| P0 | STNCL_Phase0_System_Checkout.tex | Revision 0.1; 2026-08-17; draft | Section 2 Technical Basis; Section 3 Method / Required Outputs | Draft requirements for facility-specific completion; approval not supplied. |
| P1 | STNCL_Phase1_Ambient_Equilibrium_Baseline.tex | Revision 0.1; draft | Section 2 Data Acceptance and Uncertainty; Section 3 Method / Required Outputs | Prop-30 plan; thresholds and noise examples are not universal operating limits. |
| P2 | STNCL_Phase2_Thermal_Relaxation_Tests.tex | Revision 0.1; draft | Section 2 Thermal Model and Heat Loss; Section 3 Method / Required Outputs | Prop-30 plan; conditioning and tank qualification wording need reconciliation. |
| P3 | STNCL_Phase3_Low_Duty_Steady_Heat_Loss_Tests.tex | Revision 0.1; draft | Section 2 Blind validation; Section 3 Method / Required Outputs / Disposition | Heater-side duty definition requires electrical adaptation for VCU. |
| P4 | STNCL_Phase4_Initial_Test_Matrix_and_Transition_Characterization.tex | Revision 0.1; draft | Section 2 Primary-flow inference; Section 3 Method / Required Outputs | Five unique states plus repeat; applicability and uncertainty gates are draft requirements. |
| USER | User decisions in this chat | 2026-10-15 | Editable forms; VCU fluid scope; both models; circumferential sensor position | VCU Prop-30/air/water; circuit and run assignment still required. ACU excluded. |
| DESIGN | Proposed package design | 2026-10-15 | This requirements register and coordinate convention | Assistant-proposed documentation field/convention, not an approved physical fact. |

## File identity

Exact local paths and hashes of the reviewed source files are in `source_manifest.json`. Those hashes identify the source bytes, not their correctness or approval. Original source files stay at the supplied locations.

The Rev9 package reports the STEP source `_STEPFILE_UTDTloopWithOpticsAndHXRev9_9_18_26.step` with SHA-256 `78c6ae52bf39084fbd9b1306d28dcbe2c1c4d5fccd334b0e68c861022a1bfbcf`. This is the package-reported STEP hash.

## Context excluded from baseline values

ACU arrangement PDFs, ANEC-000126 sensor labels, ACU naming notes and images are ACU evidence only. Supplied VCU overview PNG captions identify Rev8, so they are visual-format references only. Mixed archives and notes linking other revisions are not imported wholesale.

## Preserved snapshots

`rev9_extraction.json` retains the imported raw segment/sensor rows, including blanks and qualifications. `initial_tables.json` retains the initial numerical workbook inputs. `initial_control_tables.json` retains the initial requirements, source records, phase requests, review issues and example forms. None is an alternate editing master.
