---
title: Selectable cooler and controlled counter-current jacket boundary
status: review
last_updated: 2026-09-15
tags: [project/trident, doc/decision, domain/thermal_network, domain/flow, facility/acu, status/provisional]
---

# ADR-0015: selectable cooler and controlled counter-current jacket

Tags: #project/trident #doc/decision #domain/thermal_network #domain/flow #facility/acu #status/provisional

## Decision

Add five selectable synthetic steady cooler forms to the shared M1/M2/M3
network. Make the controlled, counter-current secondary stream the main
predictive ACU candidate: eliminate its steady plug-flow temperatures
analytically against the solved pipe-wall cells and predict coolant outlet
temperature and total removed heat. Retain signed prescribed duty/flux as
diagnostics, fixed-sink UA and ambient convection/radiation as explicit
sensitivity forms. Do not infer duty from the unknown primary flow.

## Why and boundaries

This keeps heat removal coupled to trial wall temperatures and conserves
primary/secondary energy without adding a secondary Newton state or dividing
by primary flow at reversal. The user confirmed controlled counter-current
flow, commonly ambient inlet, and measured outlet data on 2026-09-15; exact
numerical coolant conditions and jacket UA were not supplied. Each form and
its source/pipe application layer is explicit. Predictive forms apply at
pipe wall; a signed imposed fluid source is only a SAM-form diagnostic.

The selected secondary path is a wall-side NTU approximation, not a full
two-stream effectiveness/exchanger or a facility-qualified cooler. Exact
cooler axial boundaries, heat-transfer area and property laws, secondary
internals, and outside verification remain gates. The
[equation note](../theory/STEADY_COOLER_MODEL_FORMS.md) and
[tests](../../tests/cooler/test_cooler.py) carry its implemented contract.

## SAM comparison consequence

The supplied detailed/simple SAM inputs put a positive-valued volumetric
`heat_source` inside the primary fluid on different cooler footprints;
they do not implement this predictive jacket-wall sink. Compare declared
equivalent source-form cases first and leave the heat-source sign unresolved
until an actual SAM export/run is inspected. The
[benchmark plan](../workflows/PYTHON_SAM_FORWARD_BENCHMARK_PLAN.md) and
[SAM-001](../../coordination/tasks/SAM-001.md) make this a future-agent
priority without promoting SAM agreement above conservation or facility
evidence.
