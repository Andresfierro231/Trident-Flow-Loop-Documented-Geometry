---
title: VCU upper corners and LF-01 covered
status: provisional
last_updated: 2026-10-16
tags: [project/trident, doc/decision, domain/geometry, facility/vcu]
---

# GEO-009: upper corners and LF-01 covered

Tags: #project/trident #doc/decision #domain/geometry #facility/vcu

The user's final 2026-10-16 correction states both upper corners and LF-01 are
covered. This supersedes their earlier same-session uncovered statement. That
bare-corner workbook was only staged and never applied or pushed.

Current regional insulation v6 keeps upper_left_bend C-D and upper_right_bend
E-F entirely in the insulated main-pipe region, removes the partial flags and
bare-parent-corner list, and retains only straight cooler D-E as bare. The
50.8 mm fiberglass thickness and identity remain provisional model estimates;
coverage confirmation does not establish installed product or thickness.

Rev9 working selection v2 records the same distinction and LF-01 locally
covered at its upcomer CAD mount reference 61.11391907730831 mm from C. Optical
extent, sensing junctions, DAQ binding and historical run dates are not supplied.
Workbook DRAFT-005 sets INS-02/INS-06 Insulated, leaves their installed material
and thickness blank, and adds LF-01's covered note with reported evidence.

V5 regional config and v1 selection are preserved. Existing solver results and
Rev8 cases are unchanged; regional YAML is not automatically wired through the
general solver loader. This is a current input-record correction, not completion
of a Rev9 solver migration or an experiment reprocessing campaign.
