# GEO-010 regional insulation source crosswalk

Owner: VCU configuration / Codex, 2026-10-16. `origins.json` records exact
original source paths and hashes. The copies retain original historical text;
relative links within them refer to their owning model repository. Read
INSULATION_CURRENT.md for current interpretation, not superseded full-coverage
statements in the older ADR-0026. USER_CONFIRMATION.md records the user's latest
upcomer/heater reaffirmation; GEO-009 retains covered corners and LF-01.

Inputs: immutable DRAFT-005 workbook, region_assignments.json, current model
regional YAML v7 / Rev9 working v3, ADR-0025/0026 and GEO-009. All numeric
thicknesses are reported approximate estimates, not new installed measurements.
Original material product/curve validation and exact transition surveys remain
separate from known reported regional coverage.

Reproduce with Python's standard library from the configuration repository root:

```sh
python3 -B support/scripts/sync_regional_insulation.py --output /tmp/VCU_GEO-010.xlsx
python3 -B support/scripts/sync_regional_insulation.py --check --summary /tmp/GEO-010-checks.json
```

Expected output: DRAFT-006, seven Insulated regions (six MAIN-INS at approximately
50.8 mm, heater HEATER-INS at approximately 6.35 mm), three Bare top partitions,
no Unknown regional coverage. No additional fiberglass over the heater strip.
The updater guards the saved input hash; do not overwrite later team edits
with this historical migration output. The checker reads the live workbook,
source identities and generated exports. No new dependencies or macros.
