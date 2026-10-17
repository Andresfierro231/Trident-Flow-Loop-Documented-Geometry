---
title: Bind cooler parameters and training data to one facility geometry
status: review
last_updated: 2026-09-21
tags: [project/trident, doc/decision, domain/thermal_network, domain/identifiability, facility/shared, status/provisional]
---

# ADR-0022: bind cooler parameters and training data to one facility geometry

Tags: #project/trident #doc/decision #domain/thermal_network #domain/identifiability #facility/shared #status/provisional

## Decision

Add a separate `facility_secondary_jacket_boundary_v1` model form using the
`facility_secondary_pipe_shell_ntu_eliminated_v1` algorithm. Keep ACU and VCU
as distinct solver geometries. Every resolved facility cooler and every fitted
parameter set must carry exact `facility_id` and `geometry_id` values. Training
provenance must repeat those values as `training_facility_id` and
`training_geometry_id`. Every training dataset binding must also repeat its
dataset, facility, and geometry IDs; any mismatch fails before network assembly.

ACU requires air contacting bare pipe within the jacket, no insulation mass or
pipe-to-insulation conductance over the covered fraction, and an explicit
positive shell-to-secondary/room path. VCU requires water, but its insulation
and shell construction must be declared by its own resolved geometry rather
than copied from ACU. Parameter sets are never implicitly portable between the
two loops.

## Why

Cooler conductances depend on loop geometry, jacket construction, coolant,
measurement planes, and operating conditions. A numerically plausible UA
trained on one loop is not evidence for the other. Exact facility/geometry
binding makes the most consequential training-data mistake a configuration
error instead of a silent calibration result.

The facility form also separates pipe heat removal from heat exchanged between
the room-exposed jacket shell and the secondary stream. This preserves a
secondary energy ledger while applying only the pipe term to the primary
thermal network.

## Consequences and limits

- ACU and VCU policy files live in separate facility folders and name air and
  water, respectively.
- `parameter_set_id`, parameter status, and dataset/facility/geometry bindings
  are reported with each solve. A trained candidate requires at least one
  fully bound training dataset.
- Partial bare-pipe coverage scales away the insulation volume and radial
  conductance on the covered fraction; full coverage omits that insulation
  state and room boundary.
- Current values are synthetic interface tests. Predictive training still
  requires verified per-run flow, temperatures and planes, coolant properties,
  jacket geometry, accepted loop geometry, uncertainty, and held-out data.
- The algebraically eliminated steady secondary path is not a transient shell
  model or a full conjugate exchanger.

Evidence: [PHY-009 tests](../../tests/cooler/test_phy_009.py),
[equation contract](../theory/STEADY_COOLER_MODEL_FORMS.md), and the separate
[ACU](../../config/facilities/acu_provisional/cooler_model.yaml) and
[VCU](../../config/facilities/vcu_provisional/cooler_model.yaml) policy files.
