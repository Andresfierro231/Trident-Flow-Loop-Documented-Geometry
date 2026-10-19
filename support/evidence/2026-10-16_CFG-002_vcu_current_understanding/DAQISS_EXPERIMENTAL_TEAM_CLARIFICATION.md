---
title: Draft VCU DAQ and abrupt-transition clarification
status: provisional
last_updated: 2026-10-08
tags: [project/trident, doc/report, domain/data, facility/vcu, status/provisional]
---

# Draft VCU DAQ and abrupt-transition clarification

Tags: #project/trident #doc/report #domain/data #facility/vcu #status/provisional

Please confirm the native Celsius conversion/status behavior for June 12.
These values are nonphysical; we preserve raw files and quarantine the affected
channels. Could these be DAQ sentinels, open-circuit/compensation or conversion
errors? Can you provide status/error metadata and an independent original/export?
Please explain the first affected intervals and whether otherwise plausible
values on these same channels are trustworthy. We are retaining other channels.

| Native channel | Raw min/max °C | Impossible count | Range suspect count | Source SHA-256 |
|---|---|---:|---:|---|
| STC6 | -55973.60501709323 / 84.47552011619635 | 3397 | 0 | 11c7dc8540039bd50655fc590456fd49586bd7bcf220bcc78edbfec9cd0135a7 |
| PTC2 | -55973.55631072198 / 548.7658547478215 | 697 | 204 | 11c7dc8540039bd50655fc590456fd49586bd7bcf220bcc78edbfec9cd0135a7 |
| PTC3 | -55973.55631072198 / 552.949611624688 | 9061 | 357 | 11c7dc8540039bd50655fc590456fd49586bd7bcf220bcc78edbfec9cd0135a7 |

June 17/23: please distinguish heater/cooler/flow/operator events from DAQ disturbances.
Times below are native elapsed times, not assumed local wall clocks.

- June17 core-STC trend changes occur near 50 and 53 minutes. Auxiliary
  MatHeater temperatures use a separate provisional range screen; their
  236–274 °C values are not declared invalid by the loop's 150 °C ceiling.
- June23 core events occur near 184.17, 202.25 and 205.50 minutes. The last
  two widespread STC/PTC steps are approximately 9.51 and 9.06 °C per five seconds.
- Do these match heater power, cooling water, primary flow, handling, or a reset?
  [Corrected native phase/validity records](curation_updates.json) retain details.

For July15/24, please confirm PTC5/PTC6/Tank media, inlet/outlet positions,
jacket circulation/flow and controller sensor. Switching/setpoint logs would
help interpret approximately 8.8/8.5-minute associations; they are not proof of
controller cycling. Please reconcile historical STC/PTC station bindings with
Rev9, especially STC5 and PTC-X, and provide calibration/error-code records.

This is a draft for the user to send. No message has been sent to the team.
