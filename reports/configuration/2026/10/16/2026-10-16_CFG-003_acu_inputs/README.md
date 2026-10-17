# CFG-003: source-qualified ACU configuration workbook

Owner: Implementer agent-root-cfg003, assigned by coordinator root under Andres Fierro's explicit request. Date: 2026-10-16. Status: REVIEW; documentation draft, not physical release. Output: root **ACU_inputs.xlsx**, **ACU-REVB-DRAFT-001**.

## Result and evidence

The workbook reuses generic table concepts but recreates all rows and OOXML strings from ACU evidence. It has 29 sheets and 6,114 per-cell provenance entries. Thirty-one source snapshots retain exact paths, revisions, hashes and qualifications; Sources also identifies the assistant-authored documentation design. No old facility data, macros, shared strings, media or hidden-sheet contents are carried into the XLSX.

The controlling geometry is reviewed ACU Rev B: eight tangent/arc segments totaling 5687.535910181431 mm, CAD main ID/OD 26.6446/33.401 mm, 1238.25 mm wrap hardware, 1016 mm jacket hardware, 15 sensor references and 26 saved annotation points. Full CAD coordinates, torus centers/radii/sweeps, branches and named locations are retained. The 0.4331381515232535 mm modeled heater gap and PTC2/3 support-edge qualifications stay explicit. CAD precision is not fabrication tolerance; hardware extents are not certified active thermal footprints.

ACU-specific candidate materials include the Jin working primary-fluid default, Kirst and original-table alternatives, legacy SS316L/ceramic candidates and fiberglass alternative. Twenty-five property definitions and 42 legacy table rows retain exact units, implementation ranges, out-of-range policy and original provenance. No installed-product or primary-source validation is asserted. General insulation remains an estimated 25.4–50.8 mm range; upper pipe outside the air jacket is reported about 50.8 mm; no insulation is assigned beneath the jacket. Other coverage/product/contact details stay unresolved.

The site declaration is pinned at b7e1714d25200f289061ab1430695f455a82cae1: 119 native-channel declarations, 48 instruments and 20 classes. Fifty-eight original sensor-workbook rows are transcribed verbatim beside the candidate interpretation. Missing units, literal PV spelling and unresolved aliases remain intact. Declared class specifications do not become calibration certificates. No native channel is guessed for a CAD sensor; no sensing radius/angle/layer or run applicability is invented. The site map and the separately documented 145-identity run registry are distinct.

The 78 requirements are reauthored for ACU. Blank intake responses and pending selection/reviewer fields preserve the difference between available evidence and accepted decisions. Ten information-return gates are documentation requests rather than an approved experiment plan.

## Validation

**697/697 checks pass**, including all source hashes, matching reviewed geometry hashes, arc arithmetic and endpoint closure, coordinates, stationing, property definitions/table values, literal channel names/units, original source-workbook rows, unknown preservation, provenance coverage and absence of known foreign-facility strings throughout XLSX XML. The four tests cover byte-identical reproduction, cached-formula rejection, foreign-facility rejection and rejection of an invented sensor/native join. See `checks.json`, `summary.json` and `tests.log`.

The package was checked numerically and as XML/ZIP; it was not opened in a spreadsheet GUI or visually inspected. No CAD, image/PDF pixels or raw operating acquisition was opened. No ACU operating-data processing, event interpretation, simulations, fits or steady-window acceptance occurred. The existing September 29 hold remains active.

## Reproduce and edit

[ACU guide](../../../../../../support/docs/ACU_START_HERE.md) describes the workbook, provenance, unknowns and editing procedure. [Portable inputs](../../../../../../support/evidence/2026-10-16_CFG-003_acu_inputs/README.md) records original ownership and hashes. Producing scripts: `support/scripts/prepare_acu_inputs.py` and `support/scripts/acu_workbook.py`.

```sh
python3.11 support/scripts/acu_workbook.py build --workbook /tmp/ACU_inputs_reproduced.xlsx
python3.11 support/scripts/acu_workbook.py validate --workbook /tmp/ACU_inputs_reproduced.xlsx --output-dir /tmp/acu_checks
python3.11 -m unittest discover -s support/scripts -p test_acu_workbook.py -v
```

Python 3.11; builder is standard-library-only, preparation/validation use PyYAML already present on HPC. Inputs are source snapshots and literal seed; outputs are the XLSX and isolated ACU JSON records. Reproduce to a separate path so later edits to the master are preserved. Intentional later changes require new dated evidence/provenance and a new transcription audit.

The existing default LaTeX document pipeline is facility-specific to VCU. This task adds an independent ACU workbook and JSON exports; it does not create an ACU PDF generator or certify a solver deck. Existing VCU workbook and generated outputs are preserved byte-for-byte.
