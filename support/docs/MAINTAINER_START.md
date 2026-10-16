# Package maintainer: review, save, refresh

Your job is to turn the team’s evidence into a consistent record. The experimental team can return forms without running software.

## 1. Keep the return

Save the submitted workbook and evidence with their configuration/item/date. Keep the original source files and previous release. For a new physical configuration, assign a distinct configuration ID and effective date before merging measurements.

The prototypes describe one item each. To use a response copy for another item, change its context and replace or clear the example reference cells. Keep the tab names and row-5 headers. The present generator reads one workbook at a time; it does not merge multiple submitted copies automatically.

## 2. Review the evidence and record the decision

Check that the evidence identifies the actual component, reference point, units, date and method. Read the listed source qualification. Route conflicts to the suggested owner in **Review issues**.

In **Requirements**, keep **Current evidence**, its type and source separate from **Selected choice**. Record the decision scope/rationale, reviewer/date and effective configuration. Use one review state:

- **Needs information:** evidence is missing.
- **Needs review:** evidence or a candidate choice is available but not accepted.
- **Approved for stated use:** the reviewer has selected a value/choice for an identified scope and configuration.
- **Not applicable:** record why, for which configuration, and who reviewed it.

Approval does not change the evidence type. If multiple measurements or reports disagree, preserve them in the evidence file and reference the record here. Do not erase earlier evidence to make the table appear consistent.

## 3. Update accepted baseline inputs deliberately

Update Geometry, Sensors, Calibration, Thermal spans, Fluids, Materials or Model choices only after the relevant decision. Cite the supporting record in that table. Preserve the Rev9 source extraction and initial input snapshots under `support/reference/`.

Do not fill CAD nulls using nominal values without labeling the different basis. Do not map channels by similar names. Do not reuse ACU values or Rev8 dimensions. Keep active heater/cooling spans distinct from clamps and jacket envelopes.

The prototype has an overall **Draft** status and always reports modeling readiness as false. A completed decision row does not release the whole package. Formal release rules and authority still need agreement.

## 4. Refresh the document and pictures

Save and close the workbook’s editing session. Open a terminal in the repository folder and run:

```sh
python3 support/scripts/build.py
```

The generator needs Python 3.9 or later, with no extra Python packages. It refreshes the existing LaTeX file, labeled figures, readable evidence register and input exports. Form responses appear in the document, while baseline diagrams use the separate baseline tables.

The command validates and regenerates the inputs, then compiles `support/output/pdf/VCU_control_package.pdf`. It requires `latexmk` or `pdflatex`. To generate without compiling, use `python3 support/scripts/generate.py`. Open the root `main.tex` in your LaTeX editor or choose it as the Overleaf main document; it includes `support/generated/VCU_control_package.tex`. The standalone generated document includes its drawing code. The workbook itself has no macros and does not refresh figures when saved.

## 5. Check the result before sharing

Read `support/generated/validation.json`. Confirm the build succeeded and the expected configuration and changes appear in the document and figures. The input hash ties the outputs to the saved workbook. A successful drawing build does not verify the hardware or validate a simulation.

For generator changes, run the behavior checks:

```sh
python3 -m unittest discover -s support/tests -v
```

Then compile the existing LaTeX source and inspect the pages affected by the change. Record the reviewer and changed fields in the configuration change history before a release.

## If something goes wrong

| Message or symptom | What to do |
|---|---|
| “Use a measured/input value, not a formula” | Replace the formula with a reviewed literal input. Keep calculations in the supporting evidence. |
| A sensor is “outside segment” | Check the segment, chosen endpoint, units and along-pipe distance. Do not move it just to make the picture fit. |
| The loop “does not close” | Review the connected endpoint measurements. The generator does not silently adjust other lengths. |
| A required source or review field is missing | Use the Sources ID, or complete the recorded decision and scope. Keep unresolved rows pending. |
| A changed value is still “CAD-derived” | Check whether it really comes from the same CAD evidence. Update the provenance appropriately. |
| The picture did not change | Save the intended workbook, regenerate and check validation. Form responses do not change baseline geometry automatically. |
| The build fails | Earlier generated pictures may be stale. Fix the named input and regenerate before sharing them. |

The full technical conventions and output inventory are in [technical reference](TECHNICAL_REFERENCE.md). The remaining development work is in [NEXT_STEPS.md](NEXT_STEPS.md).
