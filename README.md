# Trident configuration and modeling control

Use the workbook to record the VCU configuration, supporting evidence,
calibration and model choices. Generate the LaTeX/PDF from that saved record.

**Contributors:** follow [START_HERE.md](START_HERE.md), then edit
[inputs/VCU_inputs.xlsx](inputs/VCU_inputs.xlsx). A blank means unknown;
form responses go to review before they change the baseline.

**Maintainers:** from this repository, run:

```sh
python3 scripts/build.py
```

This regenerates and validates the workbook outputs, then compiles
`output/pdf/VCU_control_package.pdf`, including its contents and cross-references.
It needs Python 3.9+ and a LaTeX installation with `latexmk` or `pdflatex`
(MacTeX or TeX Live, with TikZ, lmodern, booktabs, longtable and hyperref).
No third-party Python packages are required.

To regenerate without a LaTeX installation:

```sh
python3 scripts/generate.py
```

Open `main.tex` in your LaTeX editor or select it as the Overleaf main document.
It includes the generated standalone document. Overleaf compiles the committed
outputs; regenerate locally and upload/sync them after workbook changes.
Read `generated/validation.json` before using the outputs. A failed generator
marks earlier outputs stale and stops the PDF build.

## Document format

The PDF starts with contributor instructions and a configuration record checklist,
then evidence forms, phase requests, open issues, geometry and sensor drawings,
and candidate input tables. Appendices retain the complete requirements register,
model/material records, calibration summary and source catalog. The checklist
keeps configuration identity, photographs, property evidence, calibration,
uncertainty and acceptance criteria visible together.

## Where things belong

| Location | Purpose |
|---|---|
| `inputs/` | Editable workbook: the master record |
| `docs/` | Experimental, modeling and maintainer guides; technical conventions |
| `reference/` | Evidence manifests, Rev9 archive and initial snapshots |
| `scripts/` | Workbook validation, geometry and document generation, PDF build |
| `generated/` | Reproducible LaTeX, SVGs, JSON and evidence register; do not edit by hand |
| `output/pdf/` | Compiled PDF and build files; ignored by Git |
| `tests/` | Geometry and evidence/review behavior checks |
| `archive/initial-drafts/` | Original outline, ethos notes and preview, preserved for context |

Run `make` to build, `make generate` to refresh outputs, or `make test` for checks.
The equivalent test command is `python3 -m unittest discover -s tests -v`.

See the [maintainer guide](docs/MAINTAINER_START.md) for review and refresh steps,
and the [technical reference](docs/TECHNICAL_REFERENCE.md) for workbook fields,
coordinate conventions and output qualifications.

This remains a draft VCU record. Building the document checks input structure
and drawing consistency; it does not approve the installed configuration or
establish model readiness. ACU configurations need a separate package.
