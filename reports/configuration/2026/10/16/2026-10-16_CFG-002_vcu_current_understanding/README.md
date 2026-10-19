# CFG-002: current VCU understanding reconciled into the master workbook

Status: verified documentation update, DRAFT-007; physical release and scientific review remain pending. Owner: agent-root-cfg002 under Andres Fierro's explicit 2026-10-16 request. This task supersedes the earlier completed CFG-001/GEO-009/GEO-010 edit scopes for this package. Modeling-owned sources were read only.

## Results

- Populated 16 Rev9 main-loop native bindings and 18 TC working observation mappings. Added **Native channels** with 20 core channels, including PTC5/JTC-B inlet, PTC6/JTC-A outlet, Amb and Tank. Four LF references remain unbound; PTC-X stays excluded.
- Added **Current knowledge**: 26 topics covering geometry, nominal versus CAD bore, gravity, local bare STC contacts, insulation, heater/cooler, topology, fluids, properties, calibration, run identity, data validity, covariance and validation limits.
- Updated 27 of 78 requirements and added three explicit review issues. Twelve issues now preserve historical applicability, DAQ validity and cooler-control gaps. Sources distinguish superseded Rev8 statements from current working selections.
- Clarified reported circuit roles without selecting one primary fill for every experiment. Updated model choices with current documented assumptions and unresolved experimental boundaries.
- Geometry, all material equations, regional insulation assignments, CAD dimensions and phase requests are unchanged. Main CAD bore, physical angles/radii, instrument calibration values, measured active heating/cooling spans and operating limits stay blank.

## Evidence and reproduction

Inputs, source hashes, original paths, saved DRAFT-006 and expected-row patch plan: [portable evidence](../../../../../../support/evidence/2026-10-16_CFG-002_vcu_current_understanding/README.md). The original modeling owner is `/scratch/09748/andresfierro231/projects_scratch/Trident/andrew_WorkSpace/trident_modeling_initiative`. Its current working v3 and insulation v7 decisions control; historical analysis snapshots retain their own Rev8/v5 provenance.

From the repository root:

```sh
python3 support/scripts/sync_vcu_current_understanding.py --output /tmp/VCU_CFG002.xlsx
python3 support/scripts/generate.py
python3 support/scripts/check_vcu_current_understanding.py --output /tmp/CFG002_checks.json
python3 -m unittest discover -s support/tests -v
module load texlive/2023
python3 support/scripts/build.py
```

The patch tool refuses a different baseline. It preserves styles/dropdowns and untouched ZIP members, and addresses physical row numbers including gaps left by the prior PTC-X removal. The checker compares the exact intended rows, all 20 main-loop stations to working v3, source hashes, exports, null preservation and package readiness. The extra worksheets are also included in generated LaTeX and the readable register.

## Validation and limits

232/232 checks and 30/30 behavior tests pass. The package compiles with pdfTeX 1.40.24 / TeX Live 2022 through module texlive/2023. Final PDF log has no warnings, undefined references or overfull boxes. No image/PDF pages or CAD archives were visually inspected. See `checks.json`, `summary.json` and full logs.

This is the best documented provisional understanding, not installed-hardware certification, an approved experiment plan, calibrated accuracy, or a validated facility model. Historical run applicability and scientific acceptance remain open. No experiments, simulations or raw-data reprocessing were performed. No external messages were sent.
