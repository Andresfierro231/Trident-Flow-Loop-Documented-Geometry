# Start here: help complete the VCU record

You can contribute without editing LaTeX or running a program. Start with one item you know, add what you can verify, and leave the rest open.

**Open [VCU_inputs.xlsx](../../VCU_inputs.xlsx).** Choose one of these tabs:

| I want to document… | Open this tab | Example already supplied |
|---|---|---|
| A pipe and its insulation | **Form pipe** | VCU upcomer, B–C |
| A sensor, its channel and calibration | **Form sensor** | Drawing reference STC-02 |
| A material-property choice | **Form material** | Reported fiberglass insulation conductivity |

## Five small steps

1. **Check the item.** Make sure the example refers to the hardware or material you are documenting. Put the configuration ID, item, date and your name in your response.
2. **Read the gray cells.** They contain reference information and its source. “CAD-derived” or “Reported” does not mean the installed item has been checked.
3. **Fill the amber cells in columns F–I.** Add your entry, its evidence file and exact location, its evidence type, and your name/date. Use the units shown in the question. Keep dates as text in `YYYY-MM-DD` form.
4. **Leave uncertainty visible.** A blank means unknown. If you cannot check something, leave the value blank and write what is missing in the evidence cell. Use “Not applicable” with a reason when appropriate. Do not enter zero to mean “not known.”
5. **Save and return the workbook with the evidence.** A reviewer records the accepted choice and scope; the package maintainer updates the baseline and regenerates the document.

You are done with a first return when someone else can tell **what you checked, which item it belongs to, and where your evidence is**. You do not have to resolve every row at once.

## Choose your short guide

- **Experimental team:** [Complete a form and return useful evidence](EXPERIMENTAL_START.md).
- **Computational team:** [Select model inputs and shared properties](MODELING_START.md).
- **Package maintainer:** [Review changes and refresh the document](MAINTAINER_START.md).
- **Codex on HPC:** [Resolve geometry/sensor evidence, then prepare the remaining experimental questions](HPC_GEOMETRY_SENSOR_HANDOFF.md). The original Rev9 package is included as a portable archive under `support/reference/`.

For a different segment, sensor or material, save a separate response copy. Ask the maintainer to replace the example reference cells with evidence for that item, or clear those references and leave them unknown. Do not carry the upcomer’s reference information into another segment. Keep tab names and the row-5 headers unchanged so the document generator can read them.

## Where to find more detail

**Phase requests** lists 17 specific returns requested by the draft STNCL plans. **Requirements** contains 78 field records; filter by responsible team or package. **Review issues** lists nine unresolved conflicts or qualification gaps. **Sources** explains the short source IDs, such as SEG, MAT and P0.

The PDF opens with six pages describing the configuration. Contributor guides, forms and administrative records are in linked appendices. Form responses appear when the maintainer regenerates it. They **do not automatically change geometry, channel mappings or selected properties**.

This is a VCU draft. Rev9 supplies the candidate CAD geometry. Installed measurements, modeling assumptions and approved choices remain separate. ACU documents and the Rev8 overview images do not supply VCU baseline values. The STNCL requests are documentation requests; the supplied drafts do not establish permission to operate or Nick Luciano’s approval.
