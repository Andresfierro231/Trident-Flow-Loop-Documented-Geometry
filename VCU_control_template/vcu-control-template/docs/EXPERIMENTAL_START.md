# Experimental team: complete one useful record

Open the workbook and start with the item you can most easily identify. The three Form tabs are the response forms; the other input tables are maintained after review.

## 1. Identify the item

Use the configuration ID, date and a photo or hardware label. The pipe example is **upcomer B–C**. The sensor example is **drawing reference STC-02**, whose real hardware ID and data channel still need confirmation.

For another item, use a separate response copy. Clear unrelated reference values or ask the maintainer to replace them with properly sourced references. Preserve the original example workbook as a starting point.

## 2. Fill the four amber response columns

| Column | What to enter |
|---|---|
| **Your entry** | The value or description you actually established, with units and date where needed. |
| **Your evidence file / location** | A file name plus page, photo, row, certificate or log interval. Add an open question here if you cannot yet answer the field. |
| **Entry evidence type** | Choose Installed measurement, Reported, CAD-derived, Modeling assumption or Unknown. |
| **Reviewer / date** | Your name/date when submitting; the reviewer later adds their review identity. This alone is not an approval. |

Keep the gray source information intact when it still describes this item. If your measurement disagrees with it, record both. The reviewer needs to see the disagreement.

**Unknown is a useful answer.** Leave the value blank, keep the type Unknown, and say what would be needed to answer it. Use text dates, for example `2026-10-15`, rather than spreadsheet date formulas.

## 3. Use the right measurement reference

For the pipe, identify B and C on a photo before recording the axis-end length. Record actual bore, outside diameter, material evidence, insulation layers, thickness, coverage and gaps separately. The reported nominal bore and approximate insulation thickness have not been verified for this segment.

For a sensor, record the segment, endpoint and distance along the segment. Say whether you measured a mount, pipe contact, probe junction or fiber extent. Trace the real sensor to the real channel; a matching label is not proof of the connection.

The angle field describes **position around the pipe circumference**. It does not describe where a probe points. On a nonvertical pipe, zero is the proposed top radial direction. On a vertical pipe, “top” is ambiguous, so the proposed zero is drawing +x. Confirm the convention before recording angles; a full 3-D point also needs the radius to the particular point being measured.

Include the calibration certificate, calibration date and range, corrections, uncertainty with units and coverage factor, and the next check or recalibration trigger. A prior bath-calibration statement without a device-specific certificate does not establish current calibration.

## 4. Return a small, traceable bundle

Return the saved workbook, the cited evidence files, and unresolved questions. Use the configuration/item/date in the file or folder names. In the last review row, leave the release decision pending unless the authorized reviewer has actually made it.

The maintainer will keep the evidence, record any accepted changes, and refresh the drawings and document. You do not need to run the generator.

## What else the draft phases request

| Phase | Evidence to gather or agree on |
|---|---|
| **0: Checkout** | Configuration photos, channel/calibration map, electrical and coolant/control sketches, circuit fluids, branch states, limits and synchronized checkout logs. |
| **1: Ambient baseline** | Qualified passive baseline and room history; actual TC/Luna pairing; noise, drift and covariance inputs; criteria the measurements can resolve. |
| **2: Relaxation** | Agreed conditioning/fill procedure; full warm/cold histories; residual power and stored-heat evidence; initial-state information for the model team. |
| **3: Low-duty checks** | Heater-only/cooler-only records, inactive-system evidence and accepted intervals for a blind comparison with the frozen model. |
| **4: Initial matrix** | Target bands, five states plus the repeat, transition/event histories, failed attempts and evidence supporting flow inference and applicability. |

Open **Phase requests** for the exact return and source locator. These requests do not authorize executing the draft tests. The heater-side energy accounting must be adapted to electrical VCU heating, and the Phase 2 conditioning wording needs reconciliation.
