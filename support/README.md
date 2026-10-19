# Supporting files

For contributing evidence, use the [contributor guide](docs/START_HERE.md).
For reviewing submissions, use the [maintainer guide](docs/MAINTAINER_START.md).
Detailed conventions are in the [technical reference](docs/TECHNICAL_REFERENCE.md).

Contributors can use [GitHub Actions and dated checkpoints](docs/DATED_CHECKPOINTS.md)
without running commands. The commands below are the local maintainer alternative.

Run these commands from the repository root:

```sh
make             # Regenerate and compile the PDF
make generate    # Regenerate without a LaTeX compiler
make test        # Run the behavior checks
```

Without Make, use `python3 support/scripts/build.py`,
`python3 support/scripts/generate.py`, or
`python3 -m unittest discover -s support/tests -v`.

Generation needs Python 3.9+ and no extra Python packages. PDF compilation
also needs MacTeX or TeX Live with `latexmk` or `pdflatex`, TikZ, lmodern,
booktabs, longtable and hyperref. The PDF is written to
`support/output/pdf/VCU_control_package.pdf`.

The root `main.tex` includes the concise `support/generated/VCU_control_package.tex`.
`audit.tex` includes the complete `support/generated/VCU_detailed_audit.tex`.
`make` generates and compiles both PDFs into `support/output/pdf/`; `make generate`
refreshes both LaTeX files and all data exports. The concise PDF omits empty
prototype forms and the full evidence register. Submitted form responses and
entered calibration dates/uncertainties remain visible. Complete records,
equations, source qualifications and per-channel limits remain in the workbook,
exports and detailed audit.
For Overleaf, select `main.tex` and pull the generated files after GitHub Actions
finishes. See the [Overleaf instructions](docs/DATED_CHECKPOINTS.md#use-overleaf-without-running-commands).

Check `support/generated/validation.json` before using outputs. A failed
generation marks previous outputs stale and stops the PDF build.
The record remains a draft pending evidence and review.

| Folder | Contents |
|---|---|
| `docs/` | Contributor, modeling and maintainer guides |
| `reference/` | Source evidence, manifests and original snapshots |
| `generated/` | Generated LaTeX, drawings and data exports |
| `scripts/`, `tests/` | Build tools and behavior checks |
| `archive/` | Original drafts and preview |
| `evidence/` | Photos, certificates and measurements for the working configuration |
| `checkpoints/` | Permanent dated copies of the workbook, PDF, exports and evidence |
| `output/`, `tmp/` | Local build files and layout previews; ignored by Git |

The [CFG-001 source-import bundle](evidence/2026-10-16_CFG-001_vcu_references/README.md)
records exact inputs, patch parameters, expected outputs and the one-command
migration invocation. `scripts/import_vcu_references.py` preserves XLSX
formatting and dropdowns; `scripts/check_vcu_reference_import.py` checks
transcription and preservation (optional PyYAML dependency).

The later [GEO-009 evidence bundle](evidence/2026-10-16_GEO-009_covered_top_corners/README.md) documents the corrected covered-corner/LF-01 records. Use `scripts/check_covered_top_corners.py` for the historical DRAFT-005 workbook; CFG-001 checks describe the earlier historical import.

For the current DRAFT-006 workbook, [GEO-010 source crosswalk](evidence/2026-10-16_GEO-010_regional_insulation_sync/README.md) gives exact inputs/parameters, expected outputs and migration invocation. Use `python3 -B support/scripts/sync_regional_insulation.py --check` for current consistency checks.
