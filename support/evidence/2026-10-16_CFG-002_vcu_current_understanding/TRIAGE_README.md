---
title: VCU 5 C material extension and revised July run interpretation
status: provisional
last_updated: 2026-10-07
tags: [project/trident, doc/report, domain/data, domain/materials, facility/vcu, status/provisional]
---

# CAL-003: Solid-property range change and July run triage

Tags: #project/trident #doc/report #domain/data #domain/materials #facility/vcu #status/provisional

Owner: VCU calibration/report / agent-root-vcu-ambient-diagnostics-20261007.

## Material decision

The user authorized all nine pipe/fiberglass/heater-strip property functions
down to 5 °C and reports checking the pipe extrapolation independently.
[ADR-0033](../../../../../../docs/decisions/ADR-0033-vcu-solid-properties-5c.md)
records authority, evidence limits and historical reproduction.

| Material | Previous lower bound | New allowed range |
|---|---:|---|
| 316L pipe | 19.85 °C | 5–539.85 °C |
| Main fiberglass | 10 °C | 5–259.85 °C |
| Heater CAS strip | 10 °C | 5–815.85 °C |

Each row applies to density, specific heat and conductivity. All functions,
units, coefficients and upper limits are unchanged. Values below 5 °C still
raise errors. Low-temperature use is labeled user-approved extrapolation,
not installed-product validation. Exact comparison evidence was not supplied.

Active materials: [v3](../../../../../../config/materials/vcu_candidate_materials_v3.yaml).
Preserved prior materials: [v2](../../../../../../config/materials/vcu_candidate_materials_v2.yaml).
Active regional selection: [insulation.yaml](../../../../../../config/facilities/vcu_provisional/insulation.yaml),
now v5 selecting v3 materials. Old v4 coverage/selection is preserved in
[the snapshot](../../../../../../config/facilities/vcu_provisional/insulation_v4_bare_cooler_2026-10-06.yaml).
The maintained [engineering solver note](../../../../../../docs/theory/VCU_AIR_RADIAL_SOLVER.md)
and executable reconstruction use the new range. Historical report copies
retain the former range; previous six exclusions are not automatically removed.

Focused checks: nine properties accepted at 278.15 K and rejected below;
unchanged coefficients/upper limits and overlapping-range values; active
selection; engineering reconstruction at 5 °C and existing scenarios.
24 focused tests passed. `receipt.json` records the broader gate result.
`make check` ran 336 passing tests and four optional-dependency skips; it then
stopped on an unrelated historical August 28 link and two EXP-005 coordination
findings. The new bundle had no documentation errors in that check.

```bash
PYTHONPATH=src python3.11 -m pytest tests/materials/test_vcu_5c_extension.py \
  tests/calibration/test_radial_solver_writeup.py tests/calibration/test_radial_cooldown.py \
  tests/config/test_facility_decisions.py -q
PYTHONPATH=data/staging/vcu_window_deps:src python3.11 -B tools/check_vcu_5c_extension.py
# Example FUTURE rerun inside an appropriate compute allocation, fresh output:
PYTHONPATH=data/staging/vcu_window_deps:src OPENBLAS_NUM_THREADS=1 \
  python3.11 -B tools/study_vcu_ambient_tracking.py background --workers 4 \
  --materials config/materials/vcu_candidate_materials_v3.yaml \
  --insulation config/facilities/vcu_provisional/insulation.yaml \
  --output reports/data/2026/10/07/2026-10-07_CAL-003_vcu_5c_sensitivity
```

No new sensitivity campaign has been submitted by this change.

## July 22: defer physical interpretation

The user is concerned about STC warming while PTCs cool and missing conditions.
Defer this run from physical comparison/fitting. Preserve its raw source and
prior numerical screen as diagnostic evidence. Do not infer electrical noise,
fluid identity, or external heat from opposed trends alone.

## July 15: possibly the same liquid experiment

The user believes the file called ambient may belong to the July 15 liquid
experiment and finds its cooling promising. This supersedes an inference that
different files necessarily represent different experiments. They are distinct
byte acquisitions; their experiment relationship remains unresolved.

Native STC1 stored start timestamps read from metadata:

| File | Stored wf_start_time |
|---|---|
| `Ambient_TC_Reading_07152026/Ambient_TC_Reading_07152026.tdms` | 2026-07-15T14:31:47.480372 |
| `30propTest07_15_2026/30propTest07_15_2026.tdms` | 2026-07-15T15:48:04.709400 |

The start times differ by 76 min 17.229 s. Native increment is 0.033333325 s;
both STC1 channels declare °C. Clock correctness/time-zone alignment with the
operator note remains unverified; no local event time is inferred here.
Metadata alone does not establish whether both acquisitions shared fluid,
heater/cooler state or installation. No operating note is silently reassigned.

In the fifteen one-minute means of the short file, STC1 falls 22.602→21.977 °C,
but PTC1 rises 27.310→28.462 °C and Amb rises 24.357→25.274 °C. Thus not every
probe undergoes a common cooldown, and an initially steady hot state is not
yet established. Keep the user's hypothesis and screen the appropriate
acquisition/interval rather than declaring a qualified passive decay.

The related liquid note records **100 V at 11:45 AM → 15 V at 1:45 PM**,
not an explicit heater-off event; heater watts are missing. If that history
applies, cooling with continuing heat input requires its power uncertainty to
be modeled. If a genuinely heater-off segment is confirmed, measured prior
heater power may be unnecessary after observation-based initialization, but
fluid storage, unobserved insulation state and jacket boundary still matter.
Prop-30 remains a hypothesis for the short file, not an accepted assignment.

Next July 15 work: clock/experiment join, all-channel observations and event
markers, explicit heated versus passive interval selection, then declared
fluid/solid model and uncertainty. Do not fit the short file as air-only based
on its folder name. User will ask about July 14 ambient and another experiment.

## July 29 recovery

The current local Box landing TDMS remains 42,271,578 bytes with SHA-256
`83d17c15bfc29eea4a60836202db46df5c4ad58e8877fb86e8f0a7b956c8bd5c`,
identical to the source in [DAQ-013](../../05/2026-10-05_DAQ-013_jul29_tdms_forensics/README.md).
That assessment found only metadata and zero-filled missing waveform segments.
This check does not establish whether the remote Box source has changed since
the last transfer; no remote transfer was performed here.

Ask for the original acquisition-machine July 29 TDMS and matching index,
or an independent backup/export with actual channel samples. Ask them to
verify it opens and contains nonzero-length temperature waveforms before
uploading. Reuploading the same damaged payload will not recover data. The
index cannot recreate missing waveform bytes. Preserve hashes and confirm a
replacement by an actual read and channel sample counts.

## Handoff

For report/PPT agents, this note supersedes July 22's candidate priority and
any assumption that the short July 15 file is an independent air experiment.
The [prior study](../2026-10-07_CAL-003_vcu_ambient_tracking/README.md) remains
historical diagnostic evidence. CAL-003 stays in progress; August 27 excluded,
ACU processing paused. Exact source/config/test hashes are in `manifest.json`.
