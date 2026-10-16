# Supporting files

For contributing evidence, use the [contributor guide](docs/START_HERE.md).
For reviewing submissions, use the [maintainer guide](docs/MAINTAINER_START.md).
Detailed conventions are in the [technical reference](docs/TECHNICAL_REFERENCE.md).

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

The root `main.tex` includes `support/generated/VCU_control_package.tex`.
For Overleaf, select `main.tex` and upload/sync generated files after workbook
changes; Overleaf does not run the workbook generator.

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
| `output/`, `tmp/` | Local build files and layout previews; ignored by Git |
