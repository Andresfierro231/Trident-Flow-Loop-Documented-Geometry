# Trident configuration record

Record the flow-loop setup, measurements and supporting evidence in
[VCU_inputs.xlsx](VCU_inputs.xlsx).

New here? Follow the [contributor guide](support/docs/START_HERE.md).
Start with one item you can verify; leave unknown values blank.

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

[Step-by-step checkpoint and Overleaf instructions](support/docs/DATED_CHECKPOINTS.md).

Build instructions, references and tools live in [support/](support/README.md).
