# Trident configuration record

## ACU configuration workbook

[ACU_inputs.xlsx](ACU_inputs.xlsx) is the independent **ACU-REVB-DRAFT-001** master, populated from reviewed Rev B text geometry and source-qualified ACU material/instrument records. Start with **Current knowledge** and **Provenance**. See the [ACU guide](support/docs/ACU_START_HERE.md) and [dated evidence audit](reports/configuration/2026/10/16/2026-10-16_CFG-003_acu_inputs/README.md). The default PDF workflow below builds the VCU document; ACU uses its own validation/export command.


Current workbook: **DRAFT-007**. [Current-understanding audit](reports/configuration/2026/10/16/2026-10-16_CFG-002_vcu_current_understanding/README.md) reconciles working channel bindings, observation operators, boundaries and historical data limits. Open **Current knowledge** and **Native channels** for the qualified summary. [All regional coverage and both insulation types](reports/configuration/2026/10/16/2026-10-16_GEO-010_regional_insulation_sync/README.md) are now populated from reported VCU assignments; thicknesses are labeled approximate estimates.

Record the flow-loop setup, measurements and supporting evidence in
[VCU_inputs.xlsx](VCU_inputs.xlsx).

New here? Follow the [contributor guide](support/docs/START_HERE.md).
Start with one item you can verify; leave unknown values blank.

For insulation coverage, use the workbook's **Insulation regions** dropdowns.
See the [short insulation guide](support/docs/INSULATION.md).

For each dated configuration:

1. On **Start**, set a new **Configuration ID**, **Effective date**, your name
   under **Prepared by**, and a short **Change summary**. Update the affected
   hardware, calibration and property records; cite the evidence.
2. Save and upload `VCU_inputs.xlsx` to GitHub, replacing the root workbook.
   Upload photos and certificates under `support/evidence/`.
3. [Actions → Build document](https://github.com/Andresfierro231/Trident-Flow-Loop-Documented-Geometry/actions/workflows/document.yml)
   builds the PDF automatically. To freeze a dated copy, choose **Run workflow**,
   check the dated-checkpoint option, and run it on **main**.

The checkpoint saves the workbook, PDF, generated records, evidence and file
hashes together in `support/checkpoints/YYYY-MM-DD_Configuration-ID/`.
Keep old checkpoints unchanged. No terminal or `make` command is needed.

The default **VCU_control_package.pdf** is the concise configuration record:
diagrams, technical summaries, open decisions and compact references.
**VCU_detailed_audit.pdf** is built alongside it and retains the complete forms,
phase requests, requirements/evidence register and source qualifications.
Both are included in the **VCU-control-document** download. The workbook and
complete data exports retain all records. In Overleaf, use `main.tex` for the
concise document or `audit.tex` for the detailed record.

[Step-by-step checkpoint and Overleaf instructions](support/docs/DATED_CHECKPOINTS.md).

Build instructions, references and tools live in [support/](support/README.md).

VCU reference update (2026-10-16, DRAFT-004): **CAD dimensions** contains local
Rev9 component sizes; **Materials** contains the nine reported solid-property
functions and their qualified working domains. See the [change record and
checks](reports/configuration/2026/10/16/2026-10-16_CFG-001_vcu_reference_sync/README.md)
and [portable source bundle](support/evidence/2026-10-16_CFG-001_vcu_references/README.md).

Earlier correction (DRAFT-005, 2026-10-16): both entire upper corners are **Insulated** and LF-01 is covered locally. See [GEO-009](reports/configuration/2026/10/16/2026-10-16_GEO-009_covered_top_corners/README.md).
