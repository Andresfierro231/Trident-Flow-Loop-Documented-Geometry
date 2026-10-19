---
title: ACU geometry and instrumentation revision B
status: provisional
last_updated: 2026-09-08
tags: [project/trident, doc/report, facility/acu, domain/geometry, status/provisional]
---

# ACU geometry and instrumentation — Revision B

Tags: #project/trident #doc/report #facility/acu #domain/geometry #status/provisional

CAD-primary schema 2.0. Source: **Annotated_ACU(2).FCStd — CAD extraction / saved annotations**. CAD geometry supersedes conflicting values in ExtractedMeasurements.txt, ACU_Detailed_General_Arrangement.pdf and ACU_Detailed_General_Arrangement 2.pdf. Sources includes document hashes; each primary row gives the filename, evidence kind and exact CAD object/face/datum locator.

## Read coordinates

```python
from load_acu import load_acu
tables, metadata = load_acu()
sensor_xyz = tables['sensor_points'][['sensor_id', 'point_role', 'global_x_mm', 'global_y_mm', 'global_z_mm']]
pipe_xyz = tables['pipe_segments'][['segment_id', 'start_x_mm', 'start_y_mm', 'start_z_mm', 'end_x_mm', 'end_y_mm', 'end_z_mm']]
exit_xyz = tables['exits']  # TLEP and BREP main-pipe axis limits
```

Or use `pandas.read_csv('sensor_points.csv')` and `pandas.read_csv('pipe_segments.csv')`. The loader needs pandas; `validate_acu.py` uses only the Python standard library. JSON top-level arrays correspond one-for-one to CSV files. No pandas-specific binary format is required.

## Frames and definitions

- All processed lengths and XYZ values are millimetres. Native CAD X is right, Y up/elevation, Z out of the front-elevation plane. Data is not plot-rotated. Tiny out-of-plane residuals are retained, not forced to zero.
- For a translated local frame, subtract the `HEATER_IN` XYZ row in `named_locations` from each global point. Keep all three components.
- `sensor_points`: 26 saved physical annotation points across 15 sensors. `point_role` differentiates start/end; four fibers have start only. CAD labels do not establish the active sensing junction or DAQ channel.
- `sensors`: one row per sensor; global XYZ is its saved Start_Point. Separate `centerline_*` values are its orthogonal projection onto that leg's straight axis. `offset_from_flat_start_mm` is the dot-product distance from the upstream tangent; `s_cad_mm` adds the leg's straight-start loop station.
- Station s=0 is the DOWN_BOTTOM bend midpoint. Positive order is Heater → Upcomer → Cooler → Downcomer.
- `pipe_segments`: 8 full flow-ordered loop segments. Start/end are tangent points. Straight `centerline_length_mm` is endpoint distance; curved length is measured torus radius times its actual trimmed sweep in radians. Signed `delta_*` equals end minus start.
- `exits`: TLEP/BREP cylinder-axis endpoints at analytical face limits, loop-side to remote-side. These are NOT automatically the junction intersection or expansion-tank port.
- `solid_face_segments`: individual analytical straight-face boundaries, in CAD surface-parameter direction rather than necessarily flow direction.
- `named_locations`: 20 tangent, thermal-zone, join, exit and station-origin points. `thermal_zones` gives hardware axial extents, not certified active heat-transfer spans.
- `cad_annotations`, `cad_inventory` and `annotation_checks` retain broad CAD context and attachment verification evidence. Bounding boxes are geometric bounds, not centerline coordinates.
- JSON null / CSV blank means undefined, never zero. Printed 0.001 mm precision is not a fabrication tolerance.

## Resolved differences and remaining caveats

The full heater tangent span is 1312.943118 mm; cooler is 1313.722983 mm. Each includes a 57.15 mm short section omitted from the PDFs' stated full-leg lengths. Heater also includes an approximately 0.433138 mm axial model gap. This gap is retained explicitly in the span and station length, not repaired; the closed centerline does not prove a watertight solid.

CAD torus sweeps replace the prior text-code angle convention. Main exit pipes have OD 42.164 mm and ID 32.4612 mm; smaller PDF exit-related diameters are not used for those main pipes. Original values remain in `comparisons` and `legacy_*`; legacy tables are **SUPERSEDED_REFERENCE_ONLY**, not an alternative default geometry.

47 of 49 datum-circle checks match the serialized support edge directly. Saved PTC_2/3 End_Point locations instead match Edge29 circle centers of the same components, while the saved support fields say Edge38 in extracted BRep order. Both references are preserved and flagged; no remote relocation or source recomputation was performed. All checked saved points match a circle center within 1e-9 mm.

The FCStd archive was read as saved Document.xml plus OpenCascade BRep geometry; no source macros were executed and the file was not recomputed or modified. All 221 Part::Feature placements and the parent Part placement were checked as identity for global BRep extraction.

Run `python validate_acu.py` to validate the exported data. This package is an engineering geometry reference, not a fabrication release or survey certification.
