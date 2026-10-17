# GEO-009: corrected insulation coverage evidence

Owner: VCU configuration package / Codex, 2026-10-16. USER_CLARIFICATION.md
retains the user's corrected statement: both entire top corners and LF-01
are covered. Earlier bare-corner staging was never applied or pushed.

Inputs: preserved DRAFT-004 workbook, corrected direct user report, and exact
copies of the modeling owner's current v6 insulation.yaml and Rev9 working
selection v2. The model owner is `/scratch/09748/andresfierro231/projects_scratch/Trident/andrew_WorkSpace/trident_modeling_initiative`.
The 50.8 mm fiberglass model estimate is provisional; installed product and
thickness remain unknown and are blank in the workbook corner records.

From the configuration repository root, reproduce the historical migration:

```sh
python3 -B support/scripts/update_covered_top_corners.py --output /tmp/VCU_GEO-009.xlsx
python3 -B support/scripts/check_covered_top_corners.py --output /tmp/GEO-009-checks.json
```

Python standard library only. Expected output is DRAFT-005 with INS-02/06
Insulated and LF-01 explicitly covered locally, unchanged numerical geometry,
other regional coverage and approval cells. The updater verifies the saved
input hash. Do not use this migration output to replace later team edits.
