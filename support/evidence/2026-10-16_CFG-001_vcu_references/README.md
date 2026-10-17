# CFG-001: VCU source copies for sharing

Imported 2026-10-16 from the modeling-owned VCU references; original locations
and SHA-256 identities are recorded in `origins.json`. These copies preserve
the original bytes, including historical wording and links relative to their
original repository. Use `origins.json` to locate those external link targets.
They are evidence copies, not new approvals or independent validation.

- `VMAT`: `vcu_candidate_materials_v3.yaml` contains the nine solid-property functions.
- `V5C`: `ADR-0033-vcu-solid-properties-5c.md` permits working extrapolation to 5 C.
- `VSEL`: `2026-10-14_GEO-008_rev9_working_selection.md` is the later Rev9 decision.
- `VINS`: `insulation.yaml` retains the October 7 regional estimates/contact assumption.
- The two Rev9 CSVs are exact members of the already supplied original ZIP.

Read VSEL before using older insulation descriptions. The material library's
older provenance says fiberglass is beneath the cooler; the later regional
configuration and VSEL say the top leg is bare. Historical statements are
retained, not silently rewritten. Installed thicknesses, product identities,
contact, exact sensing junctions and electrical footprint remain unverified.

`VCU_inputs_before_CFG-001.xlsx` preserves the preceding DRAFT-003 workbook.
`workbook_changes.json` is the exact row/cell patch from that hash. To reproduce
DRAFT-004 from the repository root (Python standard library only):

```sh
python3 support/scripts/import_vcu_references.py --output /tmp/VCU_CFG-001_reproduced.xlsx
```

The importer refuses other baseline bytes. It is a one-time migration record,
not a way to merge future team edits. Do not replace a later edited workbook
with this historical migration output. Numerical checks and limitations are in
`reports/configuration/2026/10/16/2026-10-16_CFG-001_vcu_reference_sync/`.
