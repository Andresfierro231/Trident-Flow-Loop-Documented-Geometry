# Save a dated configuration

The root workbook is the current working record. A dated checkpoint is a saved
copy of the configuration and its evidence for a particular date. Later changes
get a new ID and checkpoint; previous folders stay unchanged.

## 1. Update and save the workbook

Download the current `VCU_inputs.xlsx` from GitHub before editing.

| Where | What to update |
|---|---|
| **Start** | New Configuration ID, Effective date as `YYYY-MM-DD` text, Prepared by and Change summary. Keep Status and Checked by consistent with actual review. |
| Affected baseline tabs | Geometry/insulation, Sensors, Calibration, Thermal spans, Fluids, Materials or Model choices, as applicable. Sensor removal affects both Sensors and Calibration. |
| **Requirements** | Supporting file/page/photo locators, evidence type, open questions, and actual review decisions. C02 records change history. |
| **Review issues / Phase requests** | Update questions affected by the change. Retain the reason for a removal or other disposition. |

Only change the records affected by the new configuration. Leave unknown values
blank. Form tabs collect proposed evidence; their responses do not automatically
update the baseline drawing tables. Do not enter an approval or reviewer unless
that review occurred.

Save and close Excel. In GitHub, use **Add file → Upload files** at the repository
root to replace `VCU_inputs.xlsx`, then commit the upload. Upload supporting files
inside `support/evidence/`; cite those locations in the workbook. Large datasets
can stay in a stable external archive if the workbook records the location,
revision and checksum. External files are not downloaded automatically.

## 2. Get the PDF

Open [Actions → Build document](https://github.com/Andresfierro231/Trident-Flow-Loop-Documented-Geometry/actions/workflows/document.yml).
The workbook upload starts a build. Open the successful run and download
**VCU-control-document** under **Artifacts** (GitHub sign-in is required).
It contains the PDF and its build identity. Check the date, configuration ID,
drawings and affected tables before sharing it. If the build fails, open the
failed step for its error; a failed build is not a new usable document.

## 3. Freeze the dated copy

On the same Actions page, choose **Run workflow**, select **main**, check
**Save a dated checkpoint from the workbook's Start fields**, then run it.
The workflow builds the workbook again and saves:

```text
support/checkpoints/YYYY-MM-DD_Configuration-ID/
    VCU_inputs.xlsx
    VCU_control_package.pdf
    generated/
    evidence/
    manifest.json
    README.md
```

The date and ID come from **Start**. The manifest records the change summary,
review status, file hashes, source commit and the GitHub account that saved it.
The workflow commits the folder to GitHub and also offers a downloadable
**VCU-dated-checkpoint** artifact. Artifacts expire after 90 days; the committed
folder is the permanent record. An existing date/ID is never overwritten.

Saving a checkpoint does not approve its contents. Draft records remain draft.
For another change on the same date, use a new Configuration ID.

## Use Overleaf without running commands

Overleaf compiles the generated LaTeX; GitHub Actions reads the Excel workbook
and generates that LaTeX. The build saves refreshed files back to GitHub.

For a linked project, pull the latest GitHub changes in Overleaf, select
`main.tex` as the main document, and click **Recompile**. To send an updated
workbook through Overleaf instead, upload it there, push the Overleaf changes
to GitHub, wait for Actions to finish, then pull the generated changes back and
recompile. Recompile alone does not read a changed workbook.

Overleaf GitHub synchronization requires premium/Commons access and an initial
link by the project owner. Import this repository as a new Overleaf project if
it is not already linked. Sync is manual. See
[Overleaf's GitHub synchronization guide](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization).

Without GitHub sync, use the PDF from Actions, or upload the repository's latest
source ZIP as an Overleaf project. Edit configuration values in the workbook;
manual changes to generated `.tex` files are replaced by the next build.

## Maintainer setup and local alternative

The workflow is `.github/workflows/document.yml`. GitHub Actions must be enabled;
the workflow needs permission to commit generated files and checkpoints to main.
If branch rules reject the automated push, the PDF artifact still contains the
build result; a maintainer must integrate the generated changes and checkpoint
through the repository's required review process.

For local maintenance only, `make` builds the PDF and `make test` runs checks.
After a successful build, `python3 support/scripts/checkpoint.py --actor NAME`
saves the same dated folder. It verifies the workbook, generated inputs and PDF
hashes before saving.
