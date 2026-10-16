# Record insulation coverage

Open **Insulation regions** in `VCU_inputs.xlsx`. Change the amber cells;
keep the gray region IDs, names and boundary references unchanged.

1. Set **Coverage** to **Insulated**, **Bare**, or **Unknown** for each whole region.
   An unanswered physical question stays **Unknown**, rather than Bare.
2. For insulated regions, optionally enter a **Material ID** from the Materials
   tab and the measured **Thickness mm**. Do not enter zero for an unknown thickness.
   Clear insulation material and positive thickness when selecting Bare.
3. Add the evidence type, file/page/photo location and relevant notes. Identify
   the surface covered, particularly whether cooler insulation is outside the
   jacket. Record partial coverage or layers in Notes; this version's dropdown
   describes the whole region and does not draw partial patches or individual layers.
4. Update the configuration ID, date and change summary on **Start**, then save
   and upload the workbook to GitHub. Actions regenerates the PDF and exports.

The ten regions follow the drawing traversal:

| ID | Region | Extent |
|---|---|---|
| INS-01 | Upcomer | B–C |
| INS-02 | Top-left corner | C–D |
| INS-03 | Pre-cooler | D to jacket start |
| INS-04 | Cooler | Jacket start to jacket end |
| INS-05 | Post-cooler | Jacket end to E |
| INS-06 | Top-right corner | E–F |
| INS-07 | Downcomer | F–G |
| INS-08 | Bottom-right corner | G–H |
| INS-09 | Heater | H–A |
| INS-10 | Bottom-left corner | A–B |

The top partition uses **Complete jacket** on **Thermal spans**. Those provisional
mechanical boundaries do not establish active cooling or measured insulation
edges. Distances may be recorded from either end of the cooler; the export
normalizes them from its Start endpoint. Pre/post names describe drawing
traversal, not verified flow direction. If jacket boundaries are unknown,
the three top extents are marked unresolved and receive no coverage band.

The PDF's **Insulation** page shows a translucent blue band for Insulated,
a bare centerline with a Bare label for Bare, and gray dashed markings with
question marks for Unknown. Band width is illustrative and does not represent
physical thickness. Corner connectors remain schematic, without inferred arc
lengths. Detailed evidence is linked in the insulation appendix.

## Computational exports

The **VCU-insulation-data** artifact in each successful Actions run contains:

- `insulation.svg`: the same diagram used in the PDF.
- `insulation_regions.json`: configuration ID/date, workbook hash, coordinate
  frame, stable region IDs, coverage, material/thickness, evidence, boundary
  basis, resolved endpoints and straight-segment stations/lengths in mm.

The JSON has schema version 1. A null length or coordinate is unknown, not zero.
Corner path lengths are always null; straight spans follow the existing
axis-end geometry, including the heater's projected-span qualification.
There are no resistance factors, resistance calculations, automatic boundary
conditions or interactive what-if controls in this version.

Regional coverage/thickness is authoritative. The older **Geometry → Insulation mm**
field remains for compatibility, but does not fill regional coverage or thickness;
conflicting values appear in validation notes. Older workbooks without the new
tab still build with all coverage Unknown. Existing dated checkpoints remain
unchanged; new checkpoints automatically include the diagram and JSON.
