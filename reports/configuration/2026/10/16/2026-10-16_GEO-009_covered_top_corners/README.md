# GEO-009: corrected covered upper corners and LF-01

Date: 2026-10-16. Owner: geometry / agent-root-covered-corners-20261016.
Status: checked current input-record correction, pending outside review.

The user's final clarification is controlling: both entire upper corners C-D
and E-F are insulated, and LF-01 is covered. It supersedes the earlier bare
statement. The bare intermediate workbook was staged only, never applied/pushed.

DRAFT-005 sets INS-02/INS-06 to Insulated with Reported evidence. Installed
material/thickness remain blank. LF-01 Notes explicitly record covered locally;
its CAD reference remains on the upcomer 61.11391907730831 mm from C. No DAQ,
optical extent or historical run dates are inferred. Other coverage, geometry,
properties, calibration and approval cells are unchanged. Straight top cooler
D-E remains bare under the previous dated selection.

The model's current regional v6 places both entire upper bends in the insulated
main-pipe region, removes their partial-coverage and bare-parent flags, retains
only cooler in the bare region, and records LF-01 covered locally. Material
functions and candidate 50.8 mm fiberglass estimate are unchanged. V5 and
Rev9 selection v1 are preserved; current Rev9 working selection advances to v2.

Verification: 12 focused model/material tests; 30 workbook behavior tests;
26 workbook/export/preservation checks. The document compiles to 76 pages with
pdfTeX 1.40.24 / TeX Live 2022 (TACC module texlive/2023), with no warnings/overfull boxes in the final compiler log. No images/PDF pages were visually inspected.

These are current model input records. Regional YAML is not automatically wired
through the general solver loader; historical Rev8 solver cases/results are
unchanged. This task does not activate a full Rev9 solver migration or run
simulations/operating-data processing. Product/thickness, remaining transition
boundaries, sensing junctions and historical run applicability remain open.

Inputs/hashes are in `support/evidence/2026-10-16_GEO-009_covered_top_corners/`
from repository root; see that bundle README for the reproducible updater.
Check the live workbook/export with `python3 -B support/scripts/check_covered_top_corners.py --output /tmp/GEO-009-checks.json`.
Regenerate/build using `module load texlive/2023` then
`python3 -B support/scripts/build.py`. Run behavior checks with
`python3 -B -m unittest discover -s support/tests -v`.
Full logs and structured results are retained alongside this report.
