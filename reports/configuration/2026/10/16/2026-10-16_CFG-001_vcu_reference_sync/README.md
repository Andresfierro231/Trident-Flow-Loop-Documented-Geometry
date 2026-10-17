# CFG-001: VCU reference synchronization

Date: 2026-10-16. Owner: configuration package / Codex, at Andres Fierro's request.
Status: prepared and checked; DRAFT-004 remains subject to team review.

The editable master is the root `VCU_inputs.xlsx`. Geometry, material and model
records feed the generator; the intake forms collect separate evidence and do
not automatically replace baseline inputs. Row 5 is the machine-read header;
rows 6 onward are records. Unknowns remain empty and approval fields are separate.

## Changes

- Added **CAD dimensions**, 14 local component records: main outer envelope,
  TLEP/BREP, jacket shell/endplates/ports, hoses, valve, instrument spools,
  sheath/guide/capillary tubing and expansion tank. Each retains its Rev9
  source locator and qualification. Main bore is still absent in CAD; local
  spool IDs must not be used as a loop-wide bore.
- Enriched Geometry notes with the analytical bend radii/angles/arcs and the
  qualified spline/heater details. Numeric geometry inputs are unchanged.
- Added nine reported solid rho/cp/k functions on Materials, with T in K,
  SI output units, original-source limitations and working domains: pipe
  278.15-813 K; fiberglass 278.15-533 K; heater strip 278.15-1089 K. The
  5 C extension is user-authorized extrapolation, not product validation.
  All candidates remain calibration-ineligible; uncertainties remain unknown.
- Added portable source copies and Sources IDs VMAT, V5C, VSEL and VINS.
  The copied library's historical under-jacket insulation wording is superseded
  by the later Rev9 selection; the disagreement is explicitly retained.
- Recorded the nominal 26.64 mm main bore and full H-A heated-span assumption
  in Model choices / Requirements. CAD ID and installed active heater/cooler
  boundaries remain null. Geometry source status remains CAD-derived.
- Set only the three top D-E insulation regions Bare, with Reported evidence
  from the October 14 decision. Jacket hardware remains present. Other whole
  regions remain Unknown; approximate 50.8 mm fiberglass / 6.35 mm heater-strip
  thicknesses are recorded as reference estimates, not installed measurements.
- Updated Start to VCU-REV9-DRAFT-004 and retained all contributor entry and
  approval cells. Sensors, calibration, fluids, thermal spans, phases, review
  issues, source snapshots and dated checkpoints are unchanged.

## Inputs and reproduction

The input workbook, exact patch, source copies, original locations and hashes
are retained in [the evidence bundle](../../../../../../support/evidence/2026-10-16_CFG-001_vcu_references/README.md).
From the repository root:

```sh
python3 support/scripts/import_vcu_references.py --output /tmp/VCU_CFG-001_reproduced.xlsx
python3 support/scripts/check_vcu_reference_import.py --output /tmp/VCU_CFG-001_checks.json
python3 -m unittest discover -s support/tests -v
module load texlive/2023
python3 support/scripts/build.py
```

The importer requires only Python's standard library. The optional numerical
checker uses PyYAML to read the unchanged owning-model property library. Build
and ordinary generation have no new dependencies. Preserve later workbook
edits: the importer reproduces only the hashed DRAFT-003 input.

## Verification and limits

84/84 source/transcription/preservation checks passed, including exact
coefficients for nine property functions, 27 positive finite endpoint/reference
values, ZIP integrity, original dropdowns/styles, null CAD IDs and unchanged
approval fields. All 30 repository behavior tests passed. The document compiled
with pdfTeX 1.40.24 / TeX Live 2022 (TACC module `texlive/2023`) to 76 pages;
no compiler warnings or overfull boxes were reported. Loop closure residual:
8.528702653865114e-06 mm against the existing 0.1 mm numerical tolerance.
`model_ready` remains false.

Checks are in `checks.json`; full test/build logs are retained alongside this
report. These checks do not verify installation, original property fits,
uncertainty or experimental validity. No images or PDF pages were visually
inspected. The new CAD dimensions tab is present in the workbook and resolved
input export; it is not a new diagram or separate PDF component catalog.
No operating data were processed; ACU remains outside this VCU task.
No checkpoint was overwritten, and no commit, push or team message was sent.
