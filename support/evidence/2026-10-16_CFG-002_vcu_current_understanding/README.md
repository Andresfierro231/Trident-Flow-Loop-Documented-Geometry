# CFG-002 portable VCU evidence

Source snapshots and hashes are in `inputs.json`. Originals remain with the modeling repository; do not edit these snapshots. WORK/CURRENT and VSEL control current choices; older XWALK/ASSUME/FOLLOW records retain their original revisions and must not override later decisions.

The before-workbook and expected-row patch plan make this reconciliation reproducible. No CAD archive, images or raw experimental data were opened. Run from the repository root:

```sh
python3 support/scripts/sync_vcu_current_understanding.py --output /tmp/VCU_CFG002_reproduced.xlsx
```

Inputs: saved DRAFT-006, `workbook_changes.json`, and hashed source snapshots. Output: DRAFT-007 workbook; generator exports and report provide validation.
