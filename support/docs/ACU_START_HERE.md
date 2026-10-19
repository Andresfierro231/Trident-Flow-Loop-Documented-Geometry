# ACU inputs: start here

Open [ACU_inputs.xlsx](../../ACU_inputs.xlsx). This is **ACU-REVB-DRAFT-001**, a separate ACU documentation master. All populated data rows were rebuilt from ACU evidence; the prior workbook supplied generic field/header structure only.

1. Read **Start** and **Current knowledge** for scope, coordinate/station conventions and remaining questions.
2. Use **Geometry**, **Sensors**, **Sensor points**, **Thermal spans** and **Insulation regions** for qualified CAD or reported facts. Angles, effective sensing radii, native joins, instrument calibration and measured active thermal spans remain unknown where unsupported. A saved CAD annotation is not a measured junction.
3. Use **Native channels**, **Instruments**, **Instrument classes** and **Site source rows** for the pinned site's candidate declarations. The original sensor-list workbook has priority over its TOML transcription. Native names, `SetPoint`/`Setpoint` spelling, missing units and unresolved aliases remain literal. The 119-channel site declaration and the separately documented 145-identity run registry are different inventories.
4. **Materials**, **Property branches** and **Fluid table** preserve candidate correlations, units, working domains, original implementation provenance and alternatives. All candidates are calibration-ineligible. The 400–605 K working interval is not an approved operating envelope or primary-source validation.
5. Complete the amber **Form pipe**, **Form sensor** or **Form material** rows with a dated item/run-specific source. Blank means unknown. Forms are initially blank; their reference cells contain ACU evidence only. Selections and reviewer fields remain pending.
6. **Sources** gives source IDs, portable paths, original locations, revision/context, SHA-256 and qualifications. **Provenance** gives one record for every populated data cell, with its address, source IDs and locator. Follow the cited source row, exact source locator and file hash.

**Requirements** contains 78 reauthored ACU records. **Phase requests** contains ten documentation gates, not an approved experimental sequence. **Review issues** preserves both resolved historical geometry qualifications and open evidence gaps. Exact bend, exit and named-location tables have their own tabs.

The ACU operating-data processing hold of 2026-09-29 remains active. This documentation task did not open raw acquisitions, process events, select steady windows, fit parameters, run simulations, inspect CAD or visually view images/PDFs.

## Validate or reproduce

From the repository root, Python 3.11 and PyYAML are available on the verified HPC environment:

```sh
python3.11 support/scripts/acu_workbook.py validate
```

Inputs: `ACU_inputs.xlsx`, preserved CFG-003 source snapshots and the original ACU table seed. Outputs: `support/generated/acu/checks.json` and `resolved_inputs.json`; nonzero exit on failed evidence/structure checks. The initial transcription has 697 passing checks. Intentional later scientific edits need a dated evidence/provenance revision; this seed audit will flag differences.

Reproduce the initial draft to a separate file, preserving the editable master:

```sh
python3.11 support/scripts/acu_workbook.py build --workbook /tmp/ACU_inputs_reproduced.xlsx
python3.11 support/scripts/acu_workbook.py validate --workbook /tmp/ACU_inputs_reproduced.xlsx --output-dir /tmp/acu_reproduction_checks
```

The builder uses only the Python standard library and writes literal XLSX cells without formulas, macros, images, cached inputs or shared-string remnants. It freezes the row-5 headers and adds filters, wrapping and a regional coverage dropdown. The seed authoring script is `support/scripts/prepare_acu_inputs.py`; its inputs are only the portable snapshots and generic header schema.

The default LaTeX workflow still builds the existing VCU document. ACU has its own workbook and isolated JSON exports; an ACU LaTeX generator has not been created by this workbook task.

[Audit, evidence and checks](../../reports/configuration/2026/10/16/2026-10-16_CFG-003_acu_inputs/README.md).
