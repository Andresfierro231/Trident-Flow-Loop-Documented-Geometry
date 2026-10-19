---
title: CAL-004 follow-up: cooler associations, unused intervals and corrected phase curation
status: provisional
last_updated: 2026-10-08
tags: [project/trident, doc/report, domain/data, facility/vcu, status/provisional]
---

# CAL-004 follow-up: cooler associations, unused intervals and corrected phase curation

Tags: #project/trident #doc/report #domain/data #facility/vcu #status/provisional

## Read first

The numerical results of the [initial complete campaign](../2026-10-08_CAL-004_vcu_boundary_study/README.md) remain unchanged:
job 3497757 completed 313 native channel cases, 46 joint temporal block cases
and 278 unfit material scenarios on 256 CPUs. Its strict raw-PTC5 cycle screen
was unqualified in both runs. This follow-up addresses the concrete reason:
slow curved baselines can hide small oscillations and dominate raw peak finding.
It does **not** turn an inconclusive screen into proven chiller cycling.

[Full original methodology](../2026-10-08_CAL-004_vcu_boundary_study/METHODOLOGY.md), [refinement addendum](METHODOLOGY.md),
[input/code dependencies](inputs.json), [mean/amplitude/phase/trajectory errors](forward_errors.csv),
[unused empirical transfer](cooler_transfer_holdout.csv) and [receipt](receipt.json).

## Native validity and phase corrections

June 12: report the nonphysical data to the team; quarantine STC6/PTC2/PTC3
from physical inference rather than deleting the dataset. The first campaign
found 13,155 below-absolute-zero/nonfinite samples plus 561 range suspects,
while unaffected retained values span 18.554–44.305 °C.
[Updated source-linked clarification draft](EXPERIMENTAL_TEAM_CLARIFICATION.md).

June 17 auxiliary MatHeater1/2/3 temperatures are separately screened at
−20 to 800 °C; the previous generic 150 °C ceiling was too restrictive for
these heater-mounted channels. They are not loop-fluid/STC comparison targets.
Native values are preserved; new masks and counts are separately versioned.
Auxiliary heater jumps no longer define core-loop phase guards. A supplementary
one-minute median-STC derivative-contrast screen catches slower loop jolts.
Both screens mark candidate phase changes, not automatic physical invalidity.
[Corrected June17/23 phase records](curation_updates.json).

## Ambient results and what subtraction can accomplish

STC first-common-mode fractions are 0.971 (Aug 31), 0.923 (Sep 2), 0.914
(Sep 4); corresponding correlations with detrended Amb are 0.956, 0.606,
0.181. Shared variation is strong on every day; Amb does not explain it equally.
Subtracting Amb is therefore a hypothesis that needs unused-interval checks,
not a universally justified noise removal. Covariance and bootstrap difference
uncertainty are preserved. Type B calibration uncertainty remains unknown.

[Temporal-block uncertainty](../2026-10-08_CAL-004_vcu_boundary_study/correlated_uncertainty.csv),
[block sensitivity/correlation](../2026-10-08_CAL-004_vcu_boundary_study/uncertainty_block_stability.csv),
and [ambient transfer checks](../2026-10-08_CAL-004_vcu_boundary_study/ambient).

![Ambient uncertainty with temporal correlation](../2026-10-08_CAL-004_vcu_boundary_study/figures/2026_08_31_c861813120_g0_averaging_uncertainty.png)

![Ambient uncertainty with temporal correlation](../2026-10-08_CAL-004_vcu_boundary_study/figures/2026_09_02_f3a3ad51b5_g0_averaging_uncertainty.png)

![Ambient uncertainty with temporal correlation](../2026-10-08_CAL-004_vcu_boundary_study/figures/2026_09_04_791594aa47_g0_averaging_uncertainty.png)

## Heated oscillation associations: three references, trend sensitivity

The longest earliest pre-change hot window ending no later than 90 native
minutes is selected from the initial input-based candidates. Compare PTC5,
PTC6 and Tank under 15/30/45-minute local quadratic trend removal, retaining
the unfiltered measured temperatures for amplitude/mean/coherence/error metrics.
Filter-sensitive and band-edge periods remain unqualified. No switching logs
or controller sensor identity were supplied; do not assert chiller causality.

| Group | Reference | Trend window min | Period s | Matched cycles | Period CV | Provisional repeating signal |
|---|---|---:|---:|---:|---:|---|
| 2026_07_15_5db23b6be8_g0 | PTC5 | 15.0 | 528.52 | 7 | 0.214 | False |
| 2026_07_15_5db23b6be8_g0 | PTC5 | 30.0 | 885.62 | 3 | 0.131 | False |
| 2026_07_15_5db23b6be8_g0 | PTC5 | 45.0 | 885.62 | 2 | 0.138 | False |
| 2026_07_15_5db23b6be8_g0 | PTC6 | 15.0 | 528.52 | 7 | 0.228 | True |
| 2026_07_15_5db23b6be8_g0 | PTC6 | 30.0 | 528.52 | 7 | 0.177 | True |
| 2026_07_15_5db23b6be8_g0 | PTC6 | 45.0 | 528.52 | 7 | 0.178 | True |
| 2026_07_15_5db23b6be8_g0 | Tank | 15.0 | 520.13 | 7 | 0.178 | False |
| 2026_07_15_5db23b6be8_g0 | Tank | 30.0 | 885.62 | 5 | 0.277 | False |
| 2026_07_15_5db23b6be8_g0 | Tank | 45.0 | 885.62 | 5 | 0.249 | False |
| 2026_07_24_37701ee905_g0 | PTC5 | 15.0 | 474.90 | 6 | 0.227 | True |
| 2026_07_24_37701ee905_g0 | PTC5 | 30.0 | 697.19 | 4 | 0.124 | True |
| 2026_07_24_37701ee905_g0 | PTC5 | 45.0 | 712.35 | 4 | 0.112 | True |
| 2026_07_24_37701ee905_g0 | PTC6 | 15.0 | 321.25 | 10 | 0.195 | True |
| 2026_07_24_37701ee905_g0 | PTC6 | 30.0 | 762.05 | 3 | 0.161 | False |
| 2026_07_24_37701ee905_g0 | PTC6 | 45.0 | 780.19 | 3 | 0.207 | False |
| 2026_07_24_37701ee905_g0 | Tank | 15.0 | 512.00 | 7 | 0.135 | True |
| 2026_07_24_37701ee905_g0 | Tank | 30.0 | 512.00 | 7 | 0.159 | True |
| 2026_07_24_37701ee905_g0 | Tank | 45.0 | 520.13 | 7 | 0.198 | True |

All reference-mode [channel mean/amplitude/coherence/lag metrics](association_metrics.csv) and per-mode individual-cycle means/ranges are saved. The selected mode below is an exploratory reference frequency, not a qualified controller period.

### 2026_07_15_5db23b6be8_g0

Hot interval 30.0–90.0 min; exploratory reference PTC6, period 528.52 s. Trend sensitivity period ratio 1.000; station/jacket roles still unconfirmed.

| Channel | Harmonic amplitude °C | Coherence | Wrapped lag s | Residual SD °C |
|---|---:|---:|---:|---:|
| STC1 | 0.0837 | 0.457 | -84.00 | 0.2806 |
| STC2 | 0.0624 | 0.205 | -82.92 | 0.2210 |
| STC3 | 0.0419 | 0.021 | -37.53 | 0.3180 |
| STC4 | 0.0597 | 0.047 | -51.64 | 0.2330 |
| STC5 | 0.0596 | 0.024 | -45.97 | 0.2507 |
| STC6 | 0.0758 | 0.080 | -66.75 | 0.2830 |
| STC7 | 0.0217 | 0.071 | -48.52 | 0.2372 |
| STC8 | 0.0478 | 0.073 | -1.52 | 0.2902 |
| STC9 | 0.0597 | 0.025 | -47.82 | 0.2631 |
| STC10 | 0.0639 | 0.025 | -43.69 | 0.2703 |
| STC11 | 0.0639 | 0.021 | -43.97 | 0.2843 |
| STC12 | 0.0370 | 0.080 | -110.05 | 0.3292 |
| Tank | 0.0202 | 0.662 | -170.41 | 0.0966 |
| Amb | 0.0309 | 0.822 | -235.42 | 0.1320 |
| PTC1 | 0.0226 | 0.059 | -65.05 | 0.2786 |
| PTC2 | 0.1422 | 0.404 | 72.27 | 0.4699 |
| PTC3 | 0.0673 | 0.093 | -50.32 | 0.2956 |
| PTC4 | 0.0666 | 0.149 | -3.65 | 0.3856 |
| PTC5 | 0.0195 | 0.626 | unidentifiable | 0.1019 |
| PTC6 | 0.0548 | 1.000 | -0.00 | 0.1005 |

![2026_07_15_5db23b6be8_g0 grouped trends or residuals](figures/2026_07_15_5db23b6be8_g0_trends.png)

![2026_07_15_5db23b6be8_g0 grouped trends or residuals](figures/2026_07_15_5db23b6be8_g0_transfer.png)
### 2026_07_24_37701ee905_g0

Hot interval 30.0–90.0 min; exploratory reference Tank, period 512.00 s. Trend sensitivity period ratio 1.016; station/jacket roles still unconfirmed.

| Channel | Harmonic amplitude °C | Coherence | Wrapped lag s | Residual SD °C |
|---|---:|---:|---:|---:|
| STC1 | 0.0543 | 0.071 | -202.59 | 0.2095 |
| STC2 | 0.0391 | 0.079 | -253.88 | 0.1390 |
| STC3 | 0.0078 | 0.327 | unidentifiable | 0.1809 |
| STC4 | 0.0200 | 0.447 | unidentifiable | 0.1015 |
| STC5 | 0.0212 | 0.448 | 196.90 | 0.1113 |
| STC6 | 0.0446 | 0.035 | 234.61 | 0.1956 |
| STC7 | 0.0235 | 0.138 | -73.67 | 0.1200 |
| STC8 | 0.0588 | 0.200 | 161.89 | 0.1825 |
| STC9 | 0.0361 | 0.256 | 186.54 | 0.1278 |
| STC10 | 0.0345 | 0.189 | 193.14 | 0.1165 |
| STC11 | 0.0352 | 0.135 | 205.30 | 0.1184 |
| STC12 | 0.0690 | 0.143 | -204.97 | 0.2985 |
| Tank | 0.0755 | 1.000 | -0.00 | 0.1961 |
| Amb | 0.0190 | 0.026 | unidentifiable | 0.1237 |
| PTC1 | 0.0253 | 0.269 | 198.50 | 0.1134 |
| PTC2 | 0.1253 | 0.105 | 85.04 | 0.4924 |
| PTC3 | 0.0341 | 0.262 | 181.26 | 0.2189 |
| PTC4 | 0.0330 | 0.333 | 188.45 | 0.1327 |
| PTC5 | 0.0241 | 0.545 | 24.53 | 0.1863 |
| PTC6 | 0.0313 | 0.237 | 17.51 | 0.2825 |

![2026_07_24_37701ee905_g0 grouped trends or residuals](figures/2026_07_24_37701ee905_g0_trends.png)

![2026_07_24_37701ee905_g0 grouped trends or residuals](figures/2026_07_24_37701ee905_g0_transfer.png)

## Measured-boundary subtraction and prediction checks

Four-input empirical transfer uses PTC5/PTC6/Tank/Amb, training-only lag/ridge
selection and the untouched final half. Reported residual SD is unexplained
variability after an empirical boundary correction, not intrinsic noise.
Residual uncertainty preserves temporal blocks; insufficient one/two-period
records remain unavailable. Multicollinearity prevents physical interpretation
of gains. Phase wraps and tiny harmonic amplitudes are explicitly flagged.

The 278 prior material trajectories are reused **without fitting or re-solving**,
then scored on the same fixed interval and reference frequency. Full-trajectory
mean/RMSE errors remain in the original report. This separates mean, harmonic
amplitude and phase/time error; it does not certify the guessed local forcing.

| Group / family / channel | Unused mean error °C | Amplitude error °C | Phase-time error s | RMSE °C |
|---|---:|---:|---:|---:|
| 2026_07_15_5db23b6be8_g0 / connection / STC6 | 4.640 | -0.004 | unidentifiable | 4.647 |
| 2026_07_15_5db23b6be8_g0 / connection / STC7 | 16.671 | -0.040 | unidentifiable | 16.673 |
| 2026_07_15_5db23b6be8_g0 / insulated / STC2 | 9.496 | 0.035 | -251.44 | 9.503 |
| 2026_07_15_5db23b6be8_g0 / insulated / STC3 | 28.480 | 0.046 | 226.69 | 28.481 |
| 2026_07_15_5db23b6be8_g0 / insulated / STC4 | 5.525 | 0.003 | 170.59 | 5.532 |
| 2026_07_15_5db23b6be8_g0 / insulated / STC8 | 10.153 | 0.000 | unidentifiable | 10.156 |
| 2026_07_15_5db23b6be8_g0 / insulated / STC9 | 8.865 | -0.005 | 164.13 | 8.868 |
| 2026_07_15_5db23b6be8_g0 / insulated / STC10 | 6.999 | 0.002 | 158.30 | 7.005 |
| 2026_07_15_5db23b6be8_g0 / insulated / STC11 | 5.501 | 0.018 | 158.97 | 5.511 |
| 2026_07_15_5db23b6be8_g0 / cooler / STC6 | -29.070 | 0.006 | unidentifiable | 29.072 |
| 2026_07_15_5db23b6be8_g0 / cooler / STC7 | -16.323 | -0.030 | -95.12 | 16.325 |
| 2026_07_24_37701ee905_g0 / insulated / STC2 | 4.879 | 0.092 | -111.20 | 4.894 |
| 2026_07_24_37701ee905_g0 / insulated / STC3 | 30.626 | 0.079 | unidentifiable | 30.626 |
| 2026_07_24_37701ee905_g0 / insulated / STC4 | 1.732 | 0.050 | unidentifiable | 1.735 |
| 2026_07_24_37701ee905_g0 / insulated / STC8 | 4.829 | -0.025 | 44.07 | 4.830 |
| 2026_07_24_37701ee905_g0 / insulated / STC9 | 3.910 | 0.003 | -46.62 | 3.910 |
| 2026_07_24_37701ee905_g0 / insulated / STC10 | 2.215 | 0.002 | unidentifiable | 2.215 |
| 2026_07_24_37701ee905_g0 / insulated / STC11 | 0.959 | 0.003 | unidentifiable | 0.959 |
| 2026_07_24_37701ee905_g0 / cooler / STC6 | -25.362 | -0.027 | unidentifiable | 25.363 |
| 2026_07_24_37701ee905_g0 / cooler / STC7 | -11.872 | -0.023 | unidentifiable | 11.873 |
| 2026_07_24_37701ee905_g0 / connection / STC6 | 0.362 | -0.023 | -51.70 | 0.414 |
| 2026_07_24_37701ee905_g0 / connection / STC7 | 13.305 | -0.018 | -244.53 | 13.306 |

![Unfit material trajectories, candidate map](../2026-10-08_CAL-004_vcu_boundary_study/figures/2026_07_15_5db23b6be8_g0_connection_material_forward.png)

![Unfit material trajectories, candidate map](../2026-10-08_CAL-004_vcu_boundary_study/figures/2026_07_15_5db23b6be8_g0_cooler_material_forward.png)

![Unfit material trajectories, candidate map](../2026-10-08_CAL-004_vcu_boundary_study/figures/2026_07_15_5db23b6be8_g0_insulated_material_forward.png)

![Unfit material trajectories, candidate map](../2026-10-08_CAL-004_vcu_boundary_study/figures/2026_07_24_37701ee905_g0_connection_material_forward.png)

![Unfit material trajectories, candidate map](../2026-10-08_CAL-004_vcu_boundary_study/figures/2026_07_24_37701ee905_g0_cooler_material_forward.png)

![Unfit material trajectories, candidate map](../2026-10-08_CAL-004_vcu_boundary_study/figures/2026_07_24_37701ee905_g0_insulated_material_forward.png)

## Fitting gate and next evidence

Actual sensor station/run identities, wetted jacket probes/planes/flow,
controller switching history and calibration Type B remain unresolved.
Physical resistance fitting is deferred rather than tuning material properties
to absorb unknown forcing or cold paths. Fixed material capacity is an anchor
only for a correctly specified model. Empirical transfer is not installed R.
Hot second halves are internal checks already inspected in this campaign.
Future fitting requires a declared training set and fresh qualified prediction
checks; the holdout status below distinguishes inspected from reserved data.

Ask the experimental team about June 12 conversion/error codes and June17/23
events; confirm July15/24 PTC5/PTC6/Tank media and water circulation, controller
sensor/logs, and historical channel-to-station bindings. The low/high reference
temperatures alone do not establish flow or justify changing the recorded labels.

## Incremental value beyond temperature drift

The boundary models contain a time trend. Improving on a constant-temperature
baseline therefore does not establish that ambient or cooler predictors remove
noise. A separate linear time-only model was fitted on exactly the same first
half and tested on the same final-half samples. No holdout coefficients were fit.
[Per-channel paired errors](boundary_incremental_value.csv), [summary](baseline_summary.json),
and [reproducible producer](BASELINE_PRODUCER.py) retain this comparison.

| Run | Median paired boundary-model / time-only RMSE ratio across STCs |
|---|---:|
| August 31 | 0.431 |
| September 2 | 1.075 |
| September 4 | 1.202 |
| July 15 | 1.052 |
| July 24 | 2.528 |

Below one means lower held-out error with the measured-boundary predictors.
Only August 31 shows a consistent median improvement. The ratio is the median
of paired channel ratios, not the ratio of separate median errors. July 15's
apparent improvement over a constant baseline is largely drift extrapolation;
July 24's cooler correction is substantially worse than the time-only benchmark.
These exploratory checks do not establish causal thermal or electrical noise.

At the longest approximately 30-minute uncertainty blocks, median conditional
STC mean uncertainty on September 4 increases from 0.0192 to 0.0337 °C when Amb
is subtracted. No STC on the three long ambient days passes the provisional
block-stability screen. Report the block sensitivity rather than a certified
intrinsic-noise or absolute accuracy value; unknown calibration Type B remains open.

## Overnight work incorporated

The [overnight completion matrix](../2026-10-08_CAL-004_vcu_boundary_study/OVERNIGHT_CLOSEOUT.md)
links all four priorities: native August31/September2/September4 noise, joint
covariance/periodic behavior, recovered July14 screening, and July15 conditional
heating/cooling response. Slurm 3496245 finished in 148.14 s; the local response
analysis finished in 18.44 s. July14 contains five separate 90-second bursts,
not a joined long ambient baseline; its operating-condition match remains open.
This study incorporates those source-hashed native caches and response limits.

## Holdout status and next fitting decision

The 30–60 minute hot halves train empirical transfers; the 60–90 minute halves
are checks and have now been inspected. They must not be presented as fresh
independent validation for future model selection. Existing material trajectories
were unfit, but their errors have likewise been inspected. The [holdout registry](holdout_registry.json)
reserves the June25 native acquisition from resistance fitting/model selection
in this campaign; its diagnostic-only history, unknown secondary boundary and
anomaly require condition/validity qualification before use. An additional
controlled run with known boundaries is preferable for external prediction checking.
No resistance fitting is launched while the stated boundary/map/uncertainty gates
remain unmet.

## Execution and verification

One-node/256-CPU jobs 3497757 and 3497777 completed in 72.46 and 11.93 s.
The first failed import attempt 3497756 is preserved separately. The follow-up
plots ran in parallel; the maintained original publisher now also dispatches
independent plots in parallel, checked on a bounded serial/process PNG case.
No scaling speedup is claimed. Python 3.11 is required by this environment's
plotting installation; default Python3 selects an incompatible old Matplotlib.
Full tests: 385 passed, 5 skipped because foreground nptdms is unavailable.
Existing source-hashed native caches were used; new TDMS readability was not claimed.
Strict documentation findings and final hash/header/energy checks are recorded
in [verification](verification.json). No images or CAD were visually inspected.
