---
title: VCU diagnostics findings and next analyses
status: provisional
last_updated: 2026-10-08
tags: [project/trident, doc/report, domain/data, domain/uncertainty, facility/vcu, status/provisional]
---

# VCU diagnostics findings and next analyses

Tags: #project/trident #doc/report #domain/data #domain/uncertainty #facility/vcu #status/provisional

Owner: CAL-003 / agent-root-vcu-catalog-20261008.

[Experiment index](../../../../VCU_EXPERIMENT_INDEX.md), [completed campaign](../2026-10-08_CAL-003_vcu_experiment_diagnostics_retry/README.md), [original methods](../2026-10-08_CAL-003_vcu_experiment_diagnostics_retry/METHODOLOGY.md), [numeric summary](summary.json), [source hashes](inputs.json), [producer snapshot](producer.py), [receipt](receipt.json).

## What the campaign found

The native inventory has **23 sources, 22 readable**. Across readable acquisitions, the conservative shape classifier gives two ambient, two heater-step, one cooling and 17 mixed/unclassified. July 29 is the failed source. The 19 CSV exports remain supplementary; they are not 19 more independent experiments and have unverified clock/unit/equivalence. The two step patterns are June 24 and the long July 15 run; August 31 is cooling. Shapes do not establish heater commands or working fluid. Many mixed files contain multiple phases, family disagreements, missing room references or abrupt changes; they are not automatically unusable experiments.

June 17/23 retain the requested jolt warnings. A phase transition can also trigger the generic jolt screen; manual interval review must separate intended switching from unexplained anomalies.

## Ambient repeatability, correlation and averaging

September 2/4 are the strongest current ambient baseline candidates. These are descriptive installed-system diagnostics. They do not identify intrinsic electronics noise or absolute sensor accuracy.

The following medians use all 16 main channels (STC1–12/PTC1–4). Whole-record rows summarize one metric per channel; short-window rows summarize all channel/windows. Linearly detrending a shorter interval removes a different component of temperature evolution, so these measures must not be interchanged.

| Metric, °C unless specified | September 2 | September 4 |
|---|---:|---:|
| Whole-record raw SD | 0.150082 | 0.174662 |
| Whole-record linearly detrended SD | 0.0996881 | 0.0738711 |
| One-minute detrended SD | 0.0061664 | 0.00616364 |
| 30-minute detrended SD | 0.0153539 | 0.0153167 |
| Adjacent native difference proxy | 0.00125078 | 0.00125502 |
| Native lag-one correlation | 0.999833 | 0.999653 |

[All baseline metrics](baseline_metrics.csv), [averaging metrics](averaging_metrics.csv).

The adjacent-difference proxy is about 0.00125 °C. It is SD(diff(T))/sqrt(2), which has a white-noise interpretation only under uncorrelated-noise assumptions. It is not an accuracy specification or a complete noise floor.

On the six-hour detrended records, increasing averaging from one second to five minutes barely changes the median variation of an averaged reading: September 2 goes from 0.09961 to 0.09968 °C; September 4 from 0.07374 to 0.07270 °C. The slower correlated component dominates this measure. Thirty-minute averages reduce it to 0.09028/0.05847 °C, but only 12 complete blocks remain; 9/16 and 2/16 channels still fail the exploratory block-correlation screen. No optimal averaging interval is established.

All 16 whole-record channels, and all 30/60-minute channel windows, flag correlation for the compact ten-second-block uncertainty display. Its tiny conditional uncertainties must not be promoted to validated uncertainty bars. The current bootstrap resamples block means assuming independent blocks; it preserves simultaneous channel covariance, but does not preserve remaining serial dependence across those blocks. The next uncertainty analysis must address that dependence and changing conditions. A one-minute compact field that is blank is unavailable, not zero.

We have evidence of slow correlated variation, not a demonstrated distinction between room physics, common DAQ behavior and sensor-specific drift. Native sampling is approximately 30 Hz in these two runs; native PSD cannot directly resolve a 60 Hz component. The listed native dominant spectral bin alone is not evidence of a physical period; segment resolution and slower one-second-mean spectra must be inspected numerically.

## A concrete quality issue that must precede fitting

June 12 STC6, PTC2 and PTC3 have recorded Celsius minima near **−55,973 °C**, below absolute zero. PTC2/3 also exceed 548 °C. The original catalog's plateau minimum **−12,654 °C is contaminated**, and cannot be a physical loop temperature. The present hard screen flags all Celsius channels with a native minimum below −273.15 °C. This is deliberately narrow: it is not a complete engineering operating-range or failure-code check. Only these three native channels were flagged by this particular screen.

[Exact affected channels](hard_invalid_channels.csv). Preserve raw values. Exclude affected channel/interval data from physical fitting pending DAQ status/scaling/open-circuit review; do not discard the whole run automatically or silently replace values. Existing hashed campaign statistics remain unchanged. A subsequent curated catalog must propagate validity masks into classification, plateau bounds and uncertainty summaries.

## New chiller information and its modeling meaning

[Operator update](operator_update.json): on October 8 the user reports that oscillations at heated plateaus arise in part from chiller on/off control toward a setpoint, and clarifies that this applies to the runs where high temperatures are allowed to oscillate. Exact file intervals, controller sensor and switching timestamps remain unknown. This explains a reported contributor; this summary has not independently attributed each oscillation.

Analyze such plateaus as **cyclic operation**: mean level, cycle amplitude and cycle period may settle while instantaneous temperatures continue changing. Report cycle mean and phase-resolved range separately from residual scatter. Stable average behavior is a different experimental target from instantaneous equilibrium.

Use PTC5/6 and Tank where recorded to characterize cooler forcing, then check propagation through cooler STC6/7 and main-loop PTC/STC channels. Determine matched timing, lag, coherence and amplitude attenuation on intervals with approximately fixed operating inputs. Shared spectral structure and a plausible thermal lag support a common cooler response; they do not prove causality or exclude switching-related electrical effects. Setpoint/schedule changes and spills must be separated from sustained cycling. Do not assign the chiller explanation to the documented chiller-off ambient runs.

The physical network should use the measured jacket-inlet history as a prescribed boundary when the inlet channel/medium/plane/clock is qualified. A constant setpoint alone is insufficient for predicting the observed oscillation. If inlet history is unavailable, a specified periodic-boundary sensitivity is conditional; fit an empirical forcing only with an explicit training/test split. Predicting controller behavior itself requires controller logic, deadband, timing and flow information.

For each node the existing network still follows C*dT/dt = sum(G*(T_neighbor−T)) + Q. A time-varying cooler boundary changes the driving terms. Start with unchanged material-derived G and C and report mean error, oscillation amplitude error, phase lag and time-series RMSE separately. Do not tune conductivity to absorb a missing cooler input. July 15's below-boundary wall discrepancy remains unresolved unless a qualified colder path/local boundary can account for it.

## How to use the results now

- Select comparison intervals with declared phase, input history, valid sensors and coverage. Use September 2/4 for baseline drift and common-mode studies; use July 15 as the existing conditional powered/relaxation case. June 24 is another shape-screened candidate, with operating inputs still needing qualification. Keep August 27 excluded and July 22 deferred for physical fitting.
- Use the curves to choose and justify averaging windows. Preserve incomplete tails and covariance when averaging sensor-minus-ambient differences. Do not turn a conditional standard uncertainty into absolute accuracy.
- Use valid sensor/phase uncertainty to weight residuals, while reporting systematic bias, room gradients, installation effects and unknown calibration separately. Observation variability and forward-model input uncertainty require separate budgets.
- Compare cyclical heated operation by complete-cycle averages and amplitude/phase; compare physical transient trajectories on unused intervals, without state reinitialization.

## Next analysis, in execution order

1. **Curate validity and phases.** Investigate the three June 12 channels, define flagged native intervals, propagate masks into a new catalog version; review June 17/23 jolts and provisional mixed categories. Add an oscillating-plateau tag to phase-level records, retaining whole-run shape and command provenance.
2. **Finish the ambient uncertainty budget.** For September 2/4, quantify common-mode versus sensor-specific changes, sensor-minus-Amb covariance, lag/transfer and calibration-offset sensitivity using separate-day holdouts. Use contiguous-block resampling or a justified correlation estimator; verify uncertainty stability across block durations. Run July 14's separate 90-second bursts as a short-term repeatability comparison, not a long-period drift baseline. Absolute Type B stays unknown until calibration/reference evidence exists.
3. **Characterize heated cycling.** Start July 15; July 24 is a second candidate because both files contain PTC5, PTC6, Tank and Amb with matched counts/increments. [Reference-channel coverage and metadata hashes](cycle_candidate_coverage.json) document availability, not an established cycling interval. June 24/25 have Tank but lack the PTC5/6/Amb quartet, making direct cooler-boundary comparisons less complete. Estimate repeated-cycle timing, drift of cycle means, peak-to-peak amplitude, coherence and lag; show phase overlays grouped by sensor kind. Declare sufficient cycle/record counts and frequency resolution; return unqualified when too few cycles or switching signals are absent.
4. **Perform a cooler-driven forward comparison.** Apply qualified measured cooler histories to the physical network with material-derived properties, then examine mean/amplitude/phase errors on unused intervals. Retain fluid/flow/power and historical sensor-map qualification gates. A forced boundary-response test is distinct from predicting the cooler/controller itself.
5. **Only then revisit parameter estimation.** Evaluate sensitivity and identifiability before fitting grouped conductance/contact/film parameters. Relaxation/cycle phase can constrain time scales or ratios; absolute resistance and heat capacity still require a fixed property/power anchor. Keep material predictions, effective fitted parameters and held-out errors separately reportable.

Steps 2 and 3 can run concurrently across days, channels and independently selected intervals, using existing caches and scheduler resources. Preserve source masks and phase selections in resolved inputs. This interpretation step schedules no new long job and makes no new fitted-property or forward-validation claim.

## Reproduce the summary

Producer algorithm vcu_diagnostics_interpretation_v1 reads only the completed campaign catalog and native per-group CSVs, takes the documented medians, and screens recorded Celsius minima against −273.15 °C. Four independent summary workers are bounded by CPU affinity; a representative serial/process result matches exactly. 29 native groups summarized in 2.43 s. Text interpretation and the operator update are curated separately from computed data.

From the repository root:

    python3.11 -B tools/summarize_vcu_experiment_diagnostics.py --campaign reports/data/2026/10/08/2026-10-08_CAL-003_vcu_experiment_diagnostics_retry --output reports/data/2026/10/08/2026-10-08_CAL-003_vcu_diagnostics_findings --workers 4
