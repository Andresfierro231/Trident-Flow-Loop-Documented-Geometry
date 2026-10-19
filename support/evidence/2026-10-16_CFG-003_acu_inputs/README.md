# CFG-003 portable ACU source bundle

Purpose: create ACU_inputs.xlsx without inheriting any prior facility data. Owner: configuration-control repository; original geometry and research evidence remain with the modeling/site repositories. Date: 2026-10-16. All snapshots are immutable evidence for this revision.

`inputs.json` records 31 source snapshots, original exact paths, revisions/context, source qualifications, sizes and SHA-256. Geometry is the reviewed ACU Rev B text derivative, cross-checked against the reviewed selection's hashes. Original CAD identities are preserved in `GSRC_sources.csv`; no CAD file was opened. `SITEXLSX_ACU-STNCL-sensors.xlsx` is the unmodified site sensor-list workbook at commit b7e1714d25200f289061ab1430695f455a82cae1. It has priority over its copied CSV/TOML transcription. Source workbook cells are also transcribed into Site source rows.

`template_schema.json` records the original template path/hash and generic headers only. No physical values are copied from that template. Styles, package metadata, all rows and all strings in ACU_inputs.xlsx are written afresh. `tables.json` is the literal ACU seed plus cell-provenance ledger, authored by `support/scripts/prepare_acu_inputs.py`. It is a reproducibility reference; the root XLSX is the editable master.

Shared source snapshots such as STATUS and ADR22 retain their original mixed-facility context. Only explicitly identified ACU paragraphs are evidence for this workbook. They do not authorize cross-facility physical values. Every scientific value in the ACU workbook is independently sourced to ACU records.

Reproduce from the repository root:

```sh
python3.11 support/scripts/acu_workbook.py build --workbook /tmp/ACU_inputs_reproduced.xlsx
python3.11 support/scripts/acu_workbook.py validate --workbook /tmp/ACU_inputs_reproduced.xlsx --output-dir /tmp/acu_checks
```

Inputs: tables.json and source snapshots; outputs: literal XLSX and isolated structured validation/exports. Source hashes, unknown preservation, geometry/property/channel transcription and foreign-data checks must pass. ACU operating-data processing remains paused; this bundle contains no raw acquisition processing or physical release approval.
