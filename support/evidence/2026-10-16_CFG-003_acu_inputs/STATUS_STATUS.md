---
title: Project status
status: active
last_updated: 2026-10-14
tags: [project/trident, doc/living_truth, facility/shared]
---

# Project status

Tags: #project/trident #doc/living_truth #facility/shared

**GEO-010 insulation reconciliation:** [Current coverage and two material types](config/facilities/vcu_provisional/INSULATION_CURRENT.md) records ordinary piping/corners insulated with approximately 50.8 mm fiberglass, heater with approximately 6.35 mm ceramic strip only, and straight cooler bare. Workbook DRAFT-006 now uses reported coverage instead of Unknown; estimates remain labeled.

**October 16 VCU correction:** [GEO-009](docs/decisions/2026-10-16_GEO-009_covered_top_corners.md) records both entire top corners C-D/E-F insulated and LF-01 locally covered. GEO-009 established regional v6 and working selection v2; GEO-010 now carries current v7/v3; LF-01 window extents and historical applicability remain unknown. Existing solver results are unchanged.


**October 14 VCU geometry:** [GEO-008 plots and portable working selection](reports/geometry/2026/10/14/2026-10-14_GEO-008_rev9_comparisons/README.md)
compare Rev9 with ACU Rev B and actual Rev7. User selects Rev9 STC/PTC
references for working use: STC5 changed location, PTC4 retained, PTC-X excluded
as suspected artifact, JTC-B = PTC5 inlet and JTC-A = PTC6 outlet. All STCs
contact bare pipe; whole top leg uninsulated; full projected lower-leg heating
assumed. Numeric closure/layout/header checks pass; no visual inspection.
Historical run applicability and remaining insulation/centerline details are
open. Older October 8 blanket unconfirmed-map statements below are historical;
existing solver runs remain Rev8 and were not rerun.

**October 14 proposal framing:** [DOC-029](reports/proposal/2026/10/14/2026-10-14_DOC-029_rom_framework/README.md) preserves author approval of the CFD–experiment order-reduction framework as the contribution and physics-based ROM as its result. RO-004/005 and the compiled proposal are aligned; learning physical parameters from experiments is core. This changes research planning, not implementation or facility validation. ACU processing remains held.

**October 13 preservation:** [Verified recovery package](reports/operations/2026/10/13/2026-10-13_OPS-002_scratch_recovery/README.md) preserves 37.47 GB in 3.285 GB of Work/Box archives, with 137,842 files hash-checked during clean restoration. New Git preservation branch is pushed; live main/index unchanged. Recovered June12 curation and cooler solver checks pass. Final commit/bundle receipt is in the external control folder. Scientific review and nine unrelated documentation findings remain.

**October 9 session handoff:** [Recent-results closeout](reports/data/2026/10/09/2026-10-09_DOC-023_vcu_session_closeout/README.md) lists user/team checks and a saved Monday October 12 PowerPoint checklist. No new analysis or presentation changes; no timed notification scheduled.

**September 4 presentation clarification:** [Markdown slide copy](reports/solver/2026/10/07/2026-10-07_DOC-019_expanded_solver_experiments/draft_02_extension_slides.md)
has 26 core/eight appendix slides with conclusions and takeaways.
[Actual-Amb replacement figures](reports/data/2026/10/09/2026-10-09_CAL-006_vcu_ambient_benchmark_explained/README.md)
clarify that the old ambient-change reference copies Amb by adding an initial
wall-room gap; its apparent spike is not a simulated or observed wall spike.

**September 4 slide-28 deep dive:** [CAL-005 report](reports/data/2026/10/09/2026-10-09_CAL-005_vcu_sep04_deep_dive/README.md)
adds seven fluid/wall/ambient plots and exact historical replay. STC5 warms
0.9394 °C experimentally but cools 0.6465 °C in the solid-only model; STC12
initially cools then reheats. The model supplies measured Amb and has no fluid
state; PTC benchmarks are explicitly empirical. Local boundary/initial state,
map and calibration questions remain open (OQ-DATA-010). In review.

**CAL-004 boundary/uncertainty analysis complete, in review:** [Current report](reports/data/2026/10/08/2026-10-08_CAL-004_vcu_boundary_followup/README.md)
incorporates overnight work and source-pinned curation, joint temporal uncertainty,
heated associations and 278 unfit material scenarios. Jobs 3497757/3497777 used
one node/256 CPUs and finished in 72.46/11.93 s. June12 STC6/PTC2/PTC3 are
quarantined; other channels retained. June17/23 transitions are guarded, not
automatically DAQ faults. Shared ambient variation does not imply room causation;
Amb subtraction increases September4 conditional uncertainty. Time-only holdout
benchmarks show boundary predictors help August31, but not consistently September2/4
or July15/24. Exploratory 8.8/8.5-minute reference modes are not controller proof.
Rev9 native bindings, jacket media/planes/flow and Type B remain open; physical
resistance fitting is deferred. CAL-003 broader qualification remains active.


**Last updated:** 2026-10-08

**VCU Rev9 geometry intake:** [GEO-007 review](reports/geometry/2026/10/08/2026-10-08_GEO-007_vcu_rev9_text_review/README.md)
passes 73 numeric text-table checks. User selects Rev9 as best pipe geometry
documentation; main ID stays 26.64 mm. Four straight reference lengths change
by approximately 12–15%; exact heater/G–H centerlines and powered heater extent
remain qualified/undefined. The user questions STC5 and suspects a PTC-X
mislabel: all Rev9/native bindings are unconfirmed.
[Team review sheet](docs/data/2026-10-08_VCU_REV9_SENSOR_LABEL_REVIEW.md)
and heater/port/installation questions precede solver/map migration. Previous
Rev8 studies remain conditional historical evidence. No CAD was opened.

**VCU all-acquisition diagnostics complete:** One-node / 256-CPU computation published 123,185 signal/window cases, 3,412 joint bootstrap cases and 1,006 plots across 48 groups from 23 TDMS plus 19 supplementary CSV payloads. [Experiment index](reports/data/VCU_EXPERIMENT_INDEX.md), [methodology](docs/data/VCU_EXPERIMENT_DIAGNOSTICS_METHOD.md), and [verified execution receipt](runs/2026-10-08_CAL-003_vcu_experiment_diagnostics_retry/README.md). Every working acquisition has linked uncertainty/ reports. July 29 is the sole unreadable source; September 2/4 are provisional ambient baseline candidates. Tiny (<20 min) is a warning; classifications/plateaus are provisional and Type B accuracy is unknown. After published calculations, serial verification was handed from 3496297 to [parallel finalizer 3496597](runs/2026-10-08_CAL-003_vcu_diagnostics_finalize/README.md), which completed in 179.57 s, exit 0: 128,374 unique artifacts, 141 Markdown documents, all 1,006 PNG headers and both reference anomalies checked. This bounded campaign is complete; broader CAL-003 physical qualification and scientific review remain open.

**VCU findings/next analysis:** [Numerical interpretation](reports/data/2026/10/08/2026-10-08_CAL-003_vcu_diagnostics_findings/README.md) shows median adjacent-difference proxies ~0.00125 °C versus six-hour detrended SD 0.100/0.074 °C for September 2/4; averaging to five minutes barely reduces the slow component, and compact ten-second uncertainty blocks remain correlated. June 12 STC6/PTC2/PTC3 contain physically invalid Celsius values; original plateau minimum is contaminated. User reports chiller cycling contributes to oscillating hot plateaus (OQ-DATA-006); next priorities are validity masks, correlation-aware ambient uncertainty, matched cooler-cycle/lag analysis, and measured-cooler-input forward tests before material fitting. OQ-DATA-007 tracks invalid readings.

**Solver/Clarno presentation:** The [VCU thermal-node figure](reports/solver/2026/10/08/2026-10-08_DOC-020_vcu_thermal_nodes/README.md)
provides source-proportioned geometry with representative fluid/pipe/insulation
nodes for slide 4; scientific and visual review remain open.
[Expanded Draft 2](reports/solver/2026/10/07/2026-10-07_DOC-019_expanded_solver_experiments/README.md)
explains the network, matrix assembly, nonlinear/flow algorithms, experimental
inventory and candidate runs before a proposed timeline: 36 slides, five
appendices, 17 images, and an independently code-checked synthetic matrix.
It includes the completed July 15 conditional wall study and its boundary
discrepancy. The [first 20-minute draft](reports/solver/2026/10/07/2026-10-07_DOC-018_solver_clarno_presentation/README.md)
remains available. DOC-018/019 await scientific and visual review. The LaTeX
repository retains its report-extension plan; its copied presentation area
was removed.

**Documentation review:** DOC-012 completed the overdue map and documentation
review on 2026-10-07. Both workspace maps have 20 resolving relative links;
the workspace map now names the current nested dated-report layout. The
[review receipt](reports/operations/2026/10/07/2026-10-07_DOC-012_documentation_review/README.md)
records two remaining strict-audit coordination findings assigned to the
active EXP-005 owner. The next documentation check is due 2026-10-14 and
repository-map review 2026-10-21.

**Report layout:** Dated report bundles now sit under
`reports/<category>/YYYY/MM/DD/<dated-bundle>/`. The [DOC-017 migration](reports/operations/2026/10/07/2026-10-07_DOC-017_report_layout/README.md)
moved 54 bundles, refreshed day indexes, and retargeted the VCU working plot
links. The documentation audit enforces the layout for future reports.

**VCU July 14 and grouped plots:** [VIS-013](reports/data/2026/10/07/2026-10-07_VIS-013_vcu_july14_and_grouped/README.md)
pulled the four-file July 14 TC test from Box with matching SHA-1 values and
added its five-group TDMS to the dated working run view. Across 22 readable
acquisitions, 58 combined STC/ambient and PTC views are linked beside the run
data; July 14 also has 100 individual native plots. Twelve older native groups
lack ambient and are labeled accordingly. All source/plot hash and PNG checks
pass, with ten serial/parallel July 14 PNGs matching. July 29 remains unreadable.
The plots are diagnostic and await outside review.

**Next VCU experiment handoff:** [2026-09-30 warm start](docs/workflows/2026-09-30_WORK_PLAN.md).

**October 8 VCU noise campaign complete:** [Run snapshot and receipts](runs/2026-10-08_CAL-003_vcu_noise_campaign/README.md)
record successful job 3496245 on NuclearEnergy: one node, 256 CPUs, 148.1 s.
Native August 31/September 2/September 4 diagnostics and five separate July 14
90-second bursts feed covariance and 2,000-replicate block bootstraps.
[Local response report](reports/data/2026/10/08/2026-10-08_CAL-003_vcu_noise_response/RESPONSE_REPORT.md)
completes fourteen effective heating/cooling fits. Five tests pass and the
bounded real July 14 serial/process outputs agree. The native report has 520 signal cases and 256 block-bootstrap cases; conditional Type A does not certify intrinsic noise
or unknown Type B accuracy. No automatic conversation wake-up is configured.

**July 15 conditional wall study complete:** [Results, solver and PPT handoff](reports/data/2026/10/07/2026-10-07_CAL-003_vcu_wall_response/README.md)
contain 243 parallel sensitivity cases, nine grouped fits and 21 conductivity
profiles. Unfit material transfer RMSE is 8.15 °C; ±2 °C leg offsets yield
6.11 °C and separate wide-offset diagnostics 1.88 °C. Conductivity profiles
are nearly flat and material scales hit bounds: no unique installed-property
recovery is supported. Every scored STC falls below the minimum supplied
room/fluid boundary in the late interval, conflicting with the passive radial
model class. OQ-DATA-005 tracks historical sensor/local-fluid/cold-path checks.
The complete study remains conditional; broader CAL-003 scientific review and
qualified prediction/report acceptance remain open.

**July 15 reconstruction completed:** [Report and slide handoff](reports/data/2026/10/07/2026-10-07_CAL-003_vcu_july15_reconstruction/README.md)
includes 5,100 native one-minute rows and nine grouped plots for both files.
The liquid file has a strong cooling interval near 118.5–148.5 native minutes:
STC1 drops 39.0 °C and PTC1 drops 32.2 °C. Native UTC / note UTC−4 places the
recorded voltage/chiller reduction 1.58 min before the cooling marker. The user
selects UTC−4 as the working report assumption, rejects UTC−5 and defers the
short file as likely startup. Clear PTC2/STC1 rises appear about 8–10 min after
the heating command; actual switching versus thermal lag remains unknown.
The [next comparison plan](reports/data/2026/10/07/2026-10-07_CAL-003_vcu_july15_reconstruction/WORKING_DECISION.md)
proposes a measured-PTC-boundary wall-response study before coupled validation. Pretransition STC1 slope is +2.13 °C/h,
so no steady initial equilibrium is claimed. Unknown continuing heater watts,
fluid/flow/jacket properties and historical sensor applicability still prevent
qualified liquid prediction error. Two focused tests pass; new means reproduce
960 prior five-minute means within 2.85e-14 °C and 255 short means exactly.

**Latest VCU user decisions:** [5 °C properties and July run triage](reports/data/2026/10/07/2026-10-07_CAL-003_vcu_5c_properties_and_run_triage/README.md)
extends all nine solid-property lower bounds to 278.15 K with unchanged functions
and upper bounds, preserving v2 materials and v4 insulation. July 22 is deferred
from physical fitting. The short July 15 file may belong to the liquid experiment;
its operating join is unresolved and it must not be assumed air-only. Native
start times differ by 76 minutes; the related liquid note has 100→15 V, not
explicit shutoff. Current local July 29 still matches the damaged DAQ-013 hash;
an independent original/backup is needed. User will ask about July 14 and a
new experiment. 24 focused tests and 336 full-suite tests pass (four skips);
`make check` stops at unrelated documentation/EXP-005 gates.

**October 7 VCU diagnosis:** [Ambient tracking and slide handoff](reports/data/2026/10/07/2026-10-07_CAL-003_vcu_ambient_tracking/README.md)
separates overall drift from adjacent changes. August 31/September 2 generally
track ambient increments; September 4 has nine negative increment correlations
among ten scored STCs. Training-only empirical offsets give 0.314/0.174/0.207 °C
held-out-day RMSE; this is not evidence of certified sensor calibration bias.
Background job 3493557 completed: 120 valid sensitivity cases, six property-range
exclusions, readable short July 15/22 screens, and August 28 phase diagnostics.
The best September 4 material case improves RMSE to 0.508 °C but matches only
2/10 whole-run directions; initial insulation sensitivity does not resolve the
trend failure. August 28 remains conditional.
Finer windows deferred; CAL-003 remains in progress.

**VCU calibration and Friday error report:** CAL-001 assigns working
`calibration` role to all 22 unique staged VCU TDMS payloads, without
qualifying them for fitting or reserving a validation set. The October 9
[earlier report preparation](reports/data/2026/10/05/2026-10-05_CAL-001_vcu_friday_error_prep/FRIDAY_REPORT_DRAFT.md)
gives in-sample ambient-reference diagnostics for three 0 W days: STC RMSE
1.293 °C (August 31), 1.160 °C (September 2), and 1.005 °C (September 4).
Every window remains unqualified, and only September 4 has an executed
zero-power forward solve. Day reports are staged under each copied run's
`plots/` folder without Box sync. The historical [Clarno challenge checkpoint](reports/data/2026/10/05/2026-10-05_CAL-002_vcu_clarno_checkpoint/CLARNO_CHALLENGE_REPORT_DRAFT.md)
adds August 27 native powered-transient evidence. The user now judges its
heater timing unknown and likely unknowable, so [ADR-0032](docs/decisions/ADR-0032-defer-aug27-powered-comparison.md)
excludes that run from the active prediction and Friday report. No powered
prediction error has been scored. CAL-002 is a bounded
[feasibility closeout](reports/data/2026/10/05/2026-10-05_CAL-002_aug27_closeout/README.md)
in review; CAL-003 owns alternate-run selection and the Friday report.

**VCU working sensor map:** On 2026-10-05 the user confirmed the numbered
`STC1`–`STC12` and `PTC1`–`PTC4` station join for planned comparisons, with
no known moved or disconnected probes. The [working crosswalk](docs/data/2026-10-05_VCU_WORKING_SENSOR_CROSSWALK.md)
uses the revised Rev 8 coordinates; all 16 rounded triples match source.
The user accepted PTC1–4 at pipe centerline and STC1–12 at the outside pipe
surface under insulation as working operators; VCU-002 is done. Physical
junction depths and calibration remain under DAQ-007 and the open questions.

**Geometry lengths under reconciliation:** The user's October 6 ACU schematic
reading of 1.2554 m is its long inclined face, while Rev B gives a 1.312943 m
full bottom tangent span including the short continuation; the 1.4686 m
lower horizontal width agrees with Rev B within 0.2 mm. The user's VCU
“1.1.2 geometry pics” readings (49.750 in inclined face, 58.525 in lower
width, 50 in upcomer, and approximate 3.4825 in vertical offsets) conflict
with Rev 8/full-system values by about 140–269 mm depending on definition.
[GEO-006](reports/geometry/2026/10/06/2026-10-06_GEO-006_schematic_length_reconciliation/README.md)
holds the separate candidate, comparison, and replot; VCU reference selection
remains open pending schematic revision and corner/end-point definitions.

**August 28 conditional cooldown:** The user recalls heater likely off and
Prop-30 likely present; cooler state remains unknown. CAL-003 produced a
source-pinned solid-only radial comparison using the 72 native five-minute
windows and measured ambient. Ten noncooler STCs have 0.736 °C baseline RMSE
after initialization, with 1.246 °C RMSE through the ambient minimum. The
[report](reports/data/2026/10/05/2026-10-05_CAL-003_aug28_radial_cooldown/README.md)
and plot are staged in the working August 28 `plots/` folder without Box
sync. Fluid/cooler dynamics and full-loop Friday prediction remain open.
The user has no August 28 operator parameters or matched DOCX and now directs
the active first comparison to the documented zero-power ambient runs.
[CAL-003's three-day solid-only report](reports/data/2026/10/06/2026-10-06_CAL-003_vcu_ambient_solid_only/README.md)
scores ten noncooler STCs over eleven post-initial half-hour windows per day:
ambient-initialized h=10 RMSE is 0.538 °C (August 31), 0.728 °C (September 2),
and 1.016 °C (September 4). These are unfit, conditional same-run model
discrepancies with measured ambient as input, not independent validation.
Each day's output is staged in its archived copied-Box run `plots/` folder;
no Box sync was performed.
The expanded [air-filled conduction study](reports/data/2026/10/06/2026-10-06_CAL-003_vcu_air_conduction_study/STUDY.md)
adds inline observation/model plots, a three-day pooled fit, individual-day
fits, leave-one-day-out transfer scores, and fitted-versus-material insulation
resistance comparisons. The pooled heater resistance multiplier hits its lower
bound; no final window passes the steady diagnostic. These are conditional
effective calibrations, not installed-resistance measurements or full-loop
validation. The VCU cooler and short connections are now provisionally bare
per the user's correction; vertical legs remain insulated.

**July 29 native source:** EXP-003's other exports are uploaded, but its
42,271,578-byte July 29 TDMS has 42,250,880 trailing zero bytes in matching
Box landing, working, and archived copies. The edge CSV cannot be produced
from that payload. EXP-003 is blocked pending a separate readable original.
The [DAQ-013 forensic report](reports/data/2026/10/05/2026-10-05_DAQ-013_jul29_tdms_forensics/README.md)
locates the absent second TDMS/index segment at byte 24,576 and confirms that
the surviving prefix contains channel metadata but zero waveform samples.

EXP-006 completed its 15-case VCU native diagnostic array: fourteen cases
produced 12,812 five-minute candidate channel-window rows; one roughly
ten-second June 17 acquisition had no full window. Sources and outputs
passed hash checks. These windows are unqualified, and EXP-006 awaits
[outside review](reports/data/2026/10/05/2026-10-05_EXP-006_vcu_native_batch/README.md).

**VCU Box staging workflow:** DAQ-011 Slurm job 3490104 completed the
pull-only VCU deposit transfer: all 523 Box files matched landing and 195
selected paths backed by 162 copied payloads entered
`working/vcu/current`. DAQ-012 moved nine older dated/view directories to
`data/archive/box_legacy_2026-10-05/`, removed their old-name links, and left
only `landing/` and `working/` inside Box staging. EXP-007 added a 35-row
DOCX-sourced heater/chiller/working-fluid/notes CSV, with explicit unknown
states and the disputed August 27 heater timing flagged. See the
[workflow](docs/data/VCU_BOX_LANDING_WORKFLOW.md),
[cleanup](reports/data/2026/10/05/2026-10-05_DAQ-012_box_staging_cleanup/README.md), and
[condition table](reports/data/2026/10/05/2026-10-05_EXP-007_vcu_operational_summary/README.md).

**VCU plot location:** VIS-011 built 20 working run folders across 18 dates
under `data/staging/box/working/vcu/runs/`. Each has `data/` and named
collections under `plots/` side by side, including the May 28 shakedown run. The 425 main PNGs
remain physically in dated reports; redundant working copies were removed.
The August 28 run also links the active CAL-003 radial-cooldown report; that
separate task still has one staged working PNG.
The [stable index](reports/data/VCU_PLOT_INDEX.md) and working `catalog.csv`
map dates to case directories and the original reports. The separate
`working/vcu/objects/` directory holds 162 unique selected Box source
payloads named by SHA-256; readable source names are in `current/source/`.
Earlier pilot and parallel benchmark plots remain linked from the index.

**VCU trend diagnostic:** VIS-007 produced 20 native temperature overlays and
240 original-sample candidate window values from the September 4 ambient run.
Source and output hashes pass; every window remains unqualified, and plot
appearance awaits outside review. See the [dated bundle](reports/data/2026/10/05/2026-10-05_VIS-007_vcu_native_trends/README.md).

**VCU local report placement and radial prior:** VIS-008 copied generated
September 4 plots/reports into the local copied Box run's `plots/` folder;
Box synchronization is pending. IDN-002 calculated provisional per-length
pipe-plus-insulation conduction resistances of 6.69014 K·m/W for ordinary
pipe and 0.73190 K·m/W for the heater leg at the final ambient candidate
window temperature. They are material priors, not empirical facility fits.
See the [staging receipt](reports/data/2026/10/05/2026-10-05_VIS-008_vcu_plot_staging/README.md)
and [resistance report](reports/data/2026/10/05/2026-10-05_IDN-002_vcu_radial_prior/README.md).

**VCU run staging and expanded plots:** DAQ-009 provides a hash-verified
per-date local link view of 26 TDMS paths and 26 candidate operator notes,
without moving raw files. VIS-009 submitted a 20-case, 18-date native trend
array as Slurm job 3489771; all 20 cases completed and 425 plot outputs and
their local staged copies passed hash checks. The source and plot tree now
resides in the DAQ-012 archive; VIS-009 awaits outside review. See the [staging index](reports/data/2026/10/05/2026-10-05_DAQ-009_vcu_staging_index/README.md)
and [plot campaign](reports/data/2026/10/05/2026-10-05_VIS-009_vcu_all_native_trends/README.md).
VIS-010 has a separate channel-parallel pilot with synthetic output equivalence
checked; paired job 3489950 completed with identical 20 PNG hashes and a
3.973× one-to-four-worker end-to-end speedup on the August 28 case. It awaits
outside review. See its
[pilot bundle](reports/data/2026/10/05/2026-10-05_VIS-010_vcu_parallel_pilot/README.md).

**VCU forward pilot:** FWD-001 completed an eight-cell M2 zero-flow ambient
baseline and a separate synthetic 10 W sensitivity. Both converge and close
their heat ledgers; the baseline returns the ambient input. These diagnostic
outputs are not calibrated or validated facility predictions. See the
[run bundle](runs/2026-10-05_FWD-001_vcu_ambient_forward/README.md). Its
[concise report](reports/data/2026/10/05/2026-10-05_FWD-001_vcu_forward_summary/README.md)
is staged in the copied September 4 run's `plots/` folder; Box is not synced.

**Current checkpoint:** reviewed software foundations and provisional ACU/VCU
evidence; VNV-007's synthetic cooler bookkeeping and M3 root-reporting
corrections received the user's bounded acceptance on 2026-10-05. Other
synthetic M0/M1/M2/M3 and cooler reviews remain. Separate M3 equation checks
pass, but branch count is mesh-sensitive and facility prediction is open.


**CI maintenance, 2026-10-14:** OPS-003 replaces sibling-repository test inputs
with source-pinned ACU/VCU snapshots and upgrades the checkout/Python actions
to Node 24. All 275 committed-source tests passed. This maintenance update
preserves provisional evidence gates and does not reassess scientific results.
See [OPS-003](coordination/tasks/OPS-003.md).

## Established

- The repository scaffold, strict documentation audit, immutable-reference
  checks, package check, task/open-question boards, and pull-only Box workflow
  are operational.
- NET-001 and CFG-001 passed separate adversarial reviews. NET-002 now rejects
  malformed control volumes and boolean geometric values; CFG-002 confines
  nested property-table paths and requires literal sensor booleans.
- GEO-002 and GEO-003 reviewed the supplied machine-readable geometry without
  opening CAD or images. Future agents must ask for explicit confirmation
  before opening externally created CAD or relying on image-only dimensions.
- ACU Rev B is the best current provisional ACU geometry evidence and outranks
  approximate SAM dimensions. Its reviewed physical arc centerline is
  5687.535910 mm; the chord representation is 53.300964 mm shorter.
- The ACU bottom stainless pipe carries the external heater wrap: 42.943118 mm
  inlet clearance, 1238.250000 mm tape span, and 31.750000 mm outlet clearance.
  The top pipe is enclosed by a 1016.000000 mm cooling jacket beginning
  215.172983 mm from its inlet; secondary-flow internals and measurement planes
  remain unknown.
- The user's 2026-09-26 revised VCU Rev 8 text package is now the best known
  geometric sensor-reference source. It supplies 22 references (20 main-loop,
  two jacket-port), an explicit frame, OD, jacket span, and qualified bend
  lengths. All 18 older CSV coordinates recur exactly, so this is improved
  identification and context rather than independent relocation. No physical
  junction or native DAQ channel is certified. The user's 2026-09-26 working
  selections use a rounded nominal 26.64 mm ID in v2 and assign
  heat over the entire straight H–A bottom leg; the measured bore, installed
  heater boundaries, and exact spline lengths remain unknown. See VCU-005/006/007.
- For VCU observations, the user says Luna fiber traverses the entire pipe
  diameter and labeled surface TCs measure on the outside pipe surface under
  insulation; penetrating TCs may provisionally be
  modeled at centerline, subject to testing (ASM-023). Optical position
  registration and junction depths remain unresolved.
- VCU-004 now provides a source-pinned, user-directed Rev C page/model frame:
  the heater is the inclined bottom leg, the cooler is above it, UP/DN are
  vertical in model X/Y, and model gravity is negative Y. All source pipe,
  named-location, and diagnostic sensor coordinates have an invertible rigid
  transform. The new extraction labels source Y as height, supporting the
  chosen frame, and the user now says Y is probably physical elevation,
  parallel to the upcomer. Older metadata labels source Z physical elevation;
  the Y choice is provisional until that contradiction is resolved for an
  accepted buoyancy claim (OQ-GEO-009).
- On 2026-09-14 the user said floating VCU sensor references may be ignored.
  Workbook `off_loop_candidate` and `unassigned` entries are therefore excluded
  from the main-loop sensor set, while retained as source evidence. This does
  not validate the remaining on-loop positions or sensing junctions.
- The new `VCU_Rev7_Rev8_CAD_Comparison.xlsx` is checked as a distinct cached-cell
  comparison source against the Rev 8 CSV package. Its 20 matched revision
  references and 18 prior Rev 8 sensor coordinates reconcile numerically;
  five unmatched references and off-loop exclusions remain explicit. This is
  source consistency, not physical sensor-position confirmation.
- ACU/VCU `leg()` construction adds half-bends around a middle value that
  already includes them. The resulting overstatement is 524.243479 mm for ACU
  and 434.919195 mm for VCU. Facility review selected `middle_is_flat` for both
  loops; the literal builder result remains discrepancy evidence.
- INT-001 is implemented and accepted. It provides a
  dependency-free system-object adapter, four explicitly named portable
  candidates spanning both `leg()` interpretations, and hash-pinned external
  overrides. `middle_is_flat` is the preferred system-object interpretation,
  but no provisional candidate is automatically promoted to runtime geometry.
- ARCH-001 records TAMU/Ethan modeling-choice families: corner/centerline
  representation, mesh refinement, heater/cooler placement, radial and axial
  coupling, hydraulics/friction, solver strategy, data roles, and 3-D coupling.
- Material definitions are externally selectable. The Jin HITEC branch is the
  user-selected provisional ACU diagnostic default; Kirst and the original
  TAMU table remain alternatives. Exact composition, primary evidence,
  uncertainties, pipe grade, and installed insulation remain unknown, so all
  candidates are calibration-ineligible.
- VCU's provisional primary-fluid identity is Prop-30 glycol, based on Nick's
  plan and the user's 2026-09-14 clarification. Earlier mineral-oil wording is
  superseded; product, concentration, and accepted properties remain unknown.
- The user identifies VCU piping as nominal 1-inch Schedule 40 316L and now
  selects the rounded 26.64 mm nominal ID for provisional main piping. Their
  316L, fiberglass, and heater-strip property curves are loadable but
  calibration-ineligible candidates. Catalog comparisons support nominal
  dimensions and selected property anchors, not the installed products or
  complete fits. Both insulation candidates now have user-approved working
  extrapolation down to 10 °C; the original fiberglass fit started at 297 K.
  See VCU-007/008.
- Every resolved model configuration must now provide categorized assumptions
  for geometry, mesh, heater/cooler, radial/axial transfer, hydraulics, solver,
  materials, and data use. Reporting infrastructure copies those assumptions,
  resolved inputs, hashes, diagnostics, and results into a run bundle.
- The current ACU baseline omits the bottom exit entirely while preserving its
  source geometry for possible future variants. The retained top exit is a
  flow-capable, experiment-specific temperature/pressure pin. The present
  thermal diagnostic still imposes no global circulation.
- Cooler closure is experiment-selected; the earlier 90 W duty is retained only
  as a named diagnostic fallback, not as an accepted experimental boundary.
- VCU ordinary main piping provisionally has about 2 in (0.0508 m) fiberglass
  insulation. The heater leg has only about 1/4 in (0.00635 m) of a distinct
  calcium–aluminum–silicate ceramic-fiber strip outside the pipe, per user
  clarification. The user now directs full-loop coverage and perfect thermal
  contact for the provisional model: fiberglass covers all non-heater
  segments, including beneath the water jacket. Installed products, cooler
  construction, coverage, and contact remain unverified. See VCU-008.
- The original ACU Box root export has a staged 120-identity channel registry;
  only an 8 KiB prefix of its approximately 991 MB sample file was streamed,
  and the full source remains remote. DAQ-002 later mapped both ACU and VCU
  deposits and staged bounded dated-run examples. See the
  [deposit guide](docs/data/BOX_DATA_DEPOSITS_GUIDE_2026-09-16.md) for exact
  paths, provenance, and limits; units, calibration, and sensor mapping remain
  unresolved.
- The unpacked Nick Luciano experiment-plan package is registered as VCU
  Prop-30 glycol experiment intent. It is not controlling geometry or DAQ
  evidence, and its text contains symbolic rather than numerical heater duties.
- The user lifted the earlier PHY-001 pause on 2026-09-14. A synthetic,
  no-fluid M0 steady solver now supports radial transfers, swappable ambient
  closures, exact fixed-temperature constraints, heat-ledger diagnostics, and
  reproducible run bundles. PHY-001 and the separately derived VNV-001 checks
  await outside review. M0 is not a loop-flow or validated facility solver.
- On user direction, a synthetic steady M1 candidate adds periodic fluid,
  pipe, and optional insulation cells. With zero mass flow, neighboring fluid
  cells conduct heat axially; pipe walls now conduct axially by default when
  explicit positive wall area/conductivity are supplied. The earlier pipe-off
  case remains an explicit regression variant; insulation axial
  conduction and advection remain absent. PHY-002/003/004 and VNV-002/003 await
  outside review. M1 is not transient and cannot yet represent Phase 2
  relaxation or facility prediction.
- Implementation-linked M0 and M1 drafts now record the steady signed
  residuals, nonlinear solve, and M1's full 15-state periodic matrix.
  The M1 draft now leads with layer-major ordering and an edge-based
  explanation of its periodic axial operator, then gives the full
  default-on 15-by-15 scalar matrix, compact layer/cell blocks, explicit
  pipe-off reduction, symbol glossary, and solve iteration hierarchy.
  A companion six-cell, layer-ordered 18-state note clarifies the shared
  ambient input. MATH-002/003/004/005 await outside review; advection, momentum, and transient
  mathematics remain deferred until those models exist.
- VNV-003's separately assembled unequal three/five-cell pipe-on/off
  matrices, pipe-edge nonlinear direction, bounded refinement, and
  heat-closure checks passed on 2026-09-15. This is synthetic
  agent-performed verification, not independent-person review or accepted
  pipe geometry/material. The stale axial-pipe docstring was corrected without
  changing M1 equations.
- M2 now adds conservative, prescribed signed mass-flow enthalpy transfer to
  the periodic M1 fluid network. Exactly zero flow returns the M1 residual
  and solution; positive, negative, near-zero, and high-Peclet synthetic
  checks, nonlinear enthalpy, fixed-temperature reactions, and three-level
  refinement passed. Face-flux, cell-Peclet, numerical-diffusion, and energy
  diagnostics are reported. PHY-005 and VNV-004 are in the separate review
  queue pending outside acceptance. No momentum/pressure-drop equation or
  facility flow/property validation is claimed.
- The lightweight active task board now contains only todo, in-progress,
  and blocked work. Review and completed rows are held in separate registries;
  stable task packet/evidence paths preserve historical traceability.
- M1/M2 state and residual vectors now use fluid-first, pipe-second,
  insulation-last ordering, matching the primary mathematics. Run bundles
  identify this order and the actual selected numerical algorithm. The
  supported steady network now uses interaction-declared structural coloring,
  sparse CSC finite-difference Jacobian assembly, and a nonsymmetric SciPy
  sparse direct solve for at least 12 free nodes in auto mode. Dense NumPy
  FD/LU remains available and is the named safety fallback for small or
  undeclared-interaction networks. Synthetic derivative, reaction, reversal,
  energy, and paired 5/20/40-cell timing checks passed; SOL-002 awaits
  outside review, not facility validation.
- A synthetic nested M3 candidate now couples the complete M2 thermal solve
  to an auditable signed integral momentum residual. The loss law is finite
  and linear near zero, and the signed scan reports absent/multiple roots
  instead of picking a branch. The diagnostic uses provisional ACU Rev B
  lengths/pipe ID, user-confirmed +CAD-Y-up, and user-directed top-exit-off-
  loop topology, but synthetic hydraulic/thermal closures and constant
  property approximations. PHY-006 awaits outside review; VNV-005's
  separately assembled same-agent synthetic checks now pass but await outside
  review. Accepted facility inputs remain a separate gate. Its three scan roots do not imply
  physical multistability or measured agreement.
- VNV-005 independently assembled velocity-coordinate head/loss rows and a
  constant-property coupled thermal matrix/bisection oracle. Seven synthetic
  checks pass. At 5/10/20 cells, the separate equations confirm M3's
  candidate roots and show that two additional negative roots appear under
  refinement; branch count is not yet mesh-converged. This is same-agent
  equation verification, not outside-person review or facility validation.
- PHY-007 adds five explicit steady cooler forms: signed total duty, signed
  heat flux, fixed external temperature/UA, ambient convection/radiation, and
  controlled counter-current secondary plug flow with local wall-side UA.
  The last form predicts coolant outlet temperature and closes its heat
  ledger without adding Newton states. Pipe-wall cooling replaces room ambient
  only where explicitly configured; diagnostic duty can instead be placed in
  primary fluid. The 8-cell ACU Rev B matrix is synthetic, and its root count
  and outlet predictions vary by closure. Fifteen focused cooler/SAM-interface
  checks pass; PHY-007 awaits outside review.
- A source-hashed cooler matrix runner and strict normalized SAM-export
  wrapper are available. SAM-001 now has a bounded `+90/-90 W` one-step
  diagnostic from the installed SAM executable and the SHA-pinned detailed
  input. The positive primary-fluid `heat_source` yields a warmer primary
  cooler outlet than the negative case, consistent with **heating** rather
  than the source comment's “removal.” Seven unused declarations include
  `T_amb` and `h_amb`. Both actual scalar CSVs and their hashes are preserved.
  No reviewed like-for-like Python–SAM result or facility agreement exists;
  source layer, geometry, topology, properties, boundaries, and steady
  interpretation require an alignment crosswalk.
- VNV-006 phase one now resolves physical heater/jacket boundaries on actual
  10/20/40/80-cell synthetic ACU meshes, preserves total heater/jacket spans,
  source volumes and bend K, and surveys 12 cooler/mesh cases plus seven
  40-cell hydraulic perturbations. The original imposed-duty `±0.02 kg/s`
  scan reported one root on aligned meshes, but range expansion to `±0.04`
  reveals three conditional candidates: the apparent disappearance was
  range censoring. All three tested cooler forms had three candidate roots
  on each tested mesh after expansion; an 81-point 80-cell repeat retained
  the count. The reported branch flows are not fully mesh-converged, no
  dynamic stability or physical selection is established, and VNV-006
  remains in progress. The weekly documentation review was renewed on
  2026-09-16 after a zero-finding strict audit.
- VNV-006 phase two adds a source-hashed one-at-a-time steady candidate
  continuation over heater duty, coolant flow/inlet, and jacket UA. Thirty
  resolved 20/40/80-cell points gave three conditional roots each, zero
  failed trials or count changes, and a 90-row portable CSV with per-root
  energy/momentum/cooler outputs. Rank-only links do not identify stable
  physical branches or prove the absence of folds outside the tested ranges.
  The 12-case aligned phase-one matrix was rerun after M3 root-acceptance v2;
  all candidate flows and counts matched its earlier ledger exactly.
- SAM-001 now also has an actual strictly checked, settled synthetic
  straight-pipe fluid-source run with a SHA-pinned scalar export. Its
  `-90 W` primary source gives `496.83871124183 K` at 240 s versus
  `496.8387110371135 K` from the common Python M2 specific-enthalpy
  balance, an outlet difference of `2.05e-7 K` and energy discrepancy
  `5.83e-6 W`. This is a **component integrated-energy pilot**, not a
  full periodic M2/M3 Python–SAM loop match, jacket comparison, or
  facility validation. Its stationarity/regression thresholds were set
  after pilot inspection and need preregistration for an independent run.
- SAM-001's source-pinned full-loop *field inventory* now covers fourteen
  required Python M3 versus read-only detailed SAM form fields. Twelve differ
  and two remain unresolved, so there is no alignment ID or full-loop
  numerical delta. A checked crosswalk, not matching ID text alone, is now
  required by the comparison interface before a diagnostic delta can be
  issued. A new matched SAM fixture and settled export remain outstanding;
  code-to-code agreement would test only the declared forms.
- SAM-002 has a bounded ACU three-model diagnostic: Trident M3 and an isolated,
  hash-pinned TAMU 1D ACU extension produced steady candidates; a new closed
  SAM loop passed input checking and one transient step. The three-model
  crosswalk still has twelve different and two unresolved form fields, and
  SAM has no settled export, so no like-for-like flow or temperature delta is
  issued. The [phase-one report](reports/benchmarks/THREE_MODEL_ACU_PHASE1.md)
  ranks the SAM/Trident physics and station-map work; optional TAMU closures
  remain subject to PHY-008's later evidence gate.
- VNV-007's separate-agent technical review corrected partial-cell cooler
  ambient ownership and M3 root acceptance. Cooler form v2 retains room
  exchange on unjacketed cell length; M3 outer algorithm v2 lists only
  numerical-zero scan points or pressure-tolerance-qualified bracket roots.
  Fixed secondary ports now report their direction relative to signed primary
  flow. The 12-case aligned and seven-case hydraulic root surveys retain
  their reported counts and flows to nine decimals; the eight-cell partial-
  coverage cooler matrix changes. The user accepted the synthetic correction
  on 2026-10-05 with ACU/VCU insulation separated; physical branch selection
  and facility agreement remain open. VNV-007 and VNV-009 are done.
- VNV-008 independently audited the synthetic aligned-mesh arithmetic and
  signed-root searches without editing solver or SAM builder code. Heater,
  jacket, room conductance, volumes, elevations and one-time bend K conserve
  through 160 cells. A 40-cell 161-point scan retained the three conditional
  roots found on a 41-point grid. Retaining all original hydraulic segment
  vertices in a separate 20/40/80/160-cell mesh also retained three tested
  roots but shifted candidate flows and near-zero cooler duty. Value
  convergence and exhaustive enumeration remain open. The user's bounded
  VNV-007 review is recorded; experimental-team evidence questions remain.
  Physical inputs, capacities and inertia are
  unavailable at present, so dynamic stability and facility claims remain
  pending. Global `git diff --check` now passes after the minor IDN-001
  whitespace cleanup.
- VNV-006's frozen 1280-cell source-vertex refinement completed successfully
  as Slurm job `3454733`. All six source hashes match both frozen snapshots;
  three signed candidates persisted across 56 completed trials with no grid
  failures; and geometry, source totals, volumes, and bend K remained
  conserved. Every 640→1280 preregistered provisional flow/duty target passes,
  so this and 320→640 form two successive passing refinement steps. This
  closes the bounded numerical handoff only: the finite search is not an
  exhaustive-root proof, the targets lack a benchmark-derived error budget,
  and dynamic stability, outside review, physical inputs, and measured
  discrimination remain open. See the [dated closeout](reports/verification/2026/09/21/2026-09-21_VNV-006_n1280_source_vertex/README.md).
- PHY-009 adds a synthetically tested, facility-bound cooler form with separate
  primary-pipe and jacket-shell/room heat ledgers. ACU requires air contacting
  bare pipe and removes insulation mass/conductance only over jacket coverage;
  VCU requires water and an independently declared construction. Solver,
  parameter set, and every training dataset must carry the same exact facility
  and geometry IDs or assembly fails. No parameters have been trained and no
  facility prediction is claimed; run-specific evidence and outside review
  remain gates. See the [implementation checks](reports/verification/2026/09/21/2026-09-21_PHY-009_facility_cooler/README.md).
- EXP-001 has a first-stage, synthetically tested Box-native-to-canonical
  streaming bridge and explicit temperature observation/comparison ledger.
  It retains raw row/time/status identities, requires revisioned channel
  unit/sensor maps and node operators, preserves unknown uncertainties,
  and rejects declared calibration/validation dataset leakage. Six focused
  tests include a synthetic M3-to-observation comparison. At the EXP-001
  handoff, only the small channel registry and sample prefix had been staged;
  DAQ-002 has since staged a dated ACU sample file and a bounded VCU example.
  No verified run window, engineering-unit/calibration crosswalk, or real-data
  agreement exists. EXP-001 remains in progress.
- DAQ-002's 2026-09-16 metadata snapshot lists six ACU and 479 VCU Box
  files. A compressed dated ACU run and a VCU derived CSV/operator note were
  staged in ignored scratch with source hashes; the large root ACU export and
  most VCU source files remain on Box. The ACU operator's roughly 11:30–12:30
  local stable-period note is a candidate window only. The
  [guide](docs/data/BOX_DATA_DEPOSITS_GUIDE_2026-09-16.md),
  [inventory](docs/data/BOX_DATA_DEPOSITS_FILE_INVENTORY_2026-09-16.csv), and
  [selected-source manifest](docs/data/BOX_DATA_DEPOSITS_SELECTED_SOURCE_MANIFEST_2026-09-16.yaml)
  provide the future-agent intake handoff; DAQ-002 awaits outside review.
- VIS-001 now exports a provisional SAM-derived ACU centerline/heater/jacket
  schematic as SVG/PNG with machine-readable coordinates and virtual-sensor
  labels. It preserves the known 1.2 mm geometry gap and does not represent
  verified Rev B Cartesian geometry or installed instruments. IDN-001 adds an
  auxiliary four-to-six-region effective-temperature model; six synthetic
  checks demonstrate passive common-scale ambiguity, a known-input anchor,
  directed energy conservation, and a remaining parallel-path ambiguity.
  Both tasks await outside review.
- VIS-004 adds reproducible 2-D ACU Rev B and VCU Rev 8 source-table geometry
  and sensor plots, plus a common-origin overlay and plotted-coordinate JSON.
  The 15 ACU drawing references remain unverified as installed junctions;
  the 18 VCU positions remain questioned. The figures are diagnostic-only,
  not accepted observation maps or fit inputs.
- DOC-001 assembled a provisional C1 geometry/configuration/M0 checkpoint
  with a reproducible synthetic 72 W M0 run and source/config/environment
  hashes. Focused C1 checks passed, but PHY-001/VNV-001 outside review remains
  pending. This checkout has no Git metadata or environment lock, so C1 is
  not accepted as a revision-complete checkpoint.

## Current blockers and unknowns

- On 2026-09-29 the user paused ACU operating-data processing. DAQ-001,
  DAQ-004, and EXP-002-ACU are on hold; [DAQ-004](coordination/tasks/DAQ-004.md)
  records the questions needed to resume. Read-only ACU site-map assessment is
  separate. New facility-specific [ACU](coordination/tasks/DAQ-006.md) and
  [VCU](coordination/tasks/DAQ-007.md) map audits, a VCU native intake task,
  and separate [ACU](coordination/tasks/EXP-002-ACU.md) and
  [VCU](coordination/tasks/EXP-002-VCU.md) per-run metadata tasks are on the
  board. Evidence from one loop cannot close the other loop's gate.
- The new site branches contain candidate channel/instrument declarations:
  ACU at `b7e1714d25200f289061ab1430695f455a82cae1` and force-updated VCU
  at `ba13857bcd6b67936c406f1d087f73af40640962`. The
  [bounded assessment](coordination/tasks/DOC-013.md) records what they add and
  their unresolved run-installation, geometry, unit, and operating-condition
  links. Neither branch alone makes experimental data fit-ready.
- The user selected **newest-to-oldest** VCU run processing. The bounded
  current Box listing starts with September 4, 3, and 2 ambient TC folders,
  then August 31; the dated inventory lists August 28 as the latest Prop-30
  folder. September 4 native TDMS and its separately stored DOCX are now
  source-hashed in ignored staging. The [DAQ-008 schema](reports/data/2026/09/29/2026-09-29_DAQ-008_vcu_0904_native_intake/README.md)
  identifies 20 channels, 648,071 samples each, native `Deg C` and a
  0.033333325 s waveform increment. The pinned
  [VCU site-map comparison](reports/data/2026/09/29/2026-09-29_DAQ-007_vcu_0904_channel_name_crosswalk/README.md)
  matches all 20 native channel names but does not establish physical junctions.
  [Native plots](reports/data/2026/09/29/2026-09-29_VIS-006_vcu_0904_native_ambient/README.md)
  and [text-only DOCX extraction](reports/data/2026/09/29/2026-09-29_EXP-002-VCU_0904_ambient_metadata/README.md)
  are diagnostic. The note says no fluid, 0 W heaters, and chiller off; its
  10:25 start and TDMS timezone-naive 16:05:49 start are unreconciled.
  Sensor installation, calibration, quality, and geometry links remain open;
  the [VCU question sheet](docs/data/VCU_EXPERIMENT_CLARIFICATIONS_2026-09-29.md)
  lists exact requests. The earlier July 15 derived CSV remains a plotting
  pilot, not the first run in the new analysis order.
- The user identifies VCU PTC5/PTC6 as jacket-water inlet/outlet probes,
  provisionally until corrected; inner air is the ambient-run working medium.
  September 4 DOCX and TDMS may share an arbitrary elapsed origin for
  exploratory steady work, while absolute clock alignment remains open.
  The [VCU Box handoff](reports/data/2026/09/29/2026-09-29_EXP-003_vcu_box_handoff/README.md)
  converts native TDMS first/last records and summarizes explicit heater
  power and working-fluid notes by date and run path. July 29 native TDMS is
  unreadable and most notes lack total watts, so those cells remain open.
  The generated VCU handoff was uploaded to Box
  `VCU Data Deposit/Codex_Exports/2026-09-29_EXP-003_vcu_box_handoff/`;
  30 uploaded files matched in a remote hash check. The task stays active
  for the corrected July 29 source and condition gaps.
- The user requested matching central STNCL operator DOCX notes beside
  their dated VCU uploads. The [EXP-004 placement receipt](reports/data/2026/09/29/2026-09-29_EXP-004_vcu_note_placement/README.md)
  records 12 new copies verified on Box, 2 already identical, and 10 omitted
  for no exact compatible folder or template status. Four same-name,
  different-content notes were retained with source-hash suffixes.

- Native ACU DAQ names and nominal sampling periods are now known, but units,
  coordinates/depths, calibration records, status-code meanings, run identity,
  and the physical sensor crosswalk remain unresolved.
- The first ACU Box comparison has no verified stable operating window.
  The user elected to build the native-to-physical channel crosswalk together;
  no TC wiring-code legend or engineering-unit evidence is yet known, so
  no Box TC °C-to-K conversion is entered. DAQ-001 remains the owner of that
  crosswalk and full source intake.
- The 15 ACU Rev B FIB/WT/PT drawing references have mixed or uncertain
  installed-junction status per the user; none is yet a verified observation
  operator or native Box channel match.
- The user says ACU jacket flow is controlled and counter-current, with
  ambient-inlet air contacting bare pipe; outside the jacket the upper pipe
  has approximately 2 inches of insulation, and the jacket shell is exposed
  to room air. VCU cooling uses water. Exact per-run secondary flows,
  inlet/outlet temperatures and planes, air/water properties, UA, routing,
  and jacket-shell room exchange remain unverified. The current synthetic
  jacket example uses `c_p=4180 J/(kg K)` and omits shell-to-room exchange;
  it is not a physical ACU air-jacket prediction.
- For ACU exploratory work only, the user suggested 37 L/min jacket-air flow
  and about 20 C counter-current inlet. Air-flow reference conditions and
  actual values remain unverified. The user expects flow rate in metadata and
  operating conditions in experimental runs, some on Box; qualify each run
  before using its values for prediction or comparison.
- VCU exact spline-corner hydraulic lengths, confirmed main-loop ID and heater extent, exact Prop-30
  product/concentration, property model, and material construction are unknown.
- The revised 2026-09-26 VCU package supplies the user's best known geometric
  sensor positions and reproduces the old 18 coordinates exactly. Do not use
  the old `sensors.csv` as a certified observation map; resolve physical
  junctions, optical position registration, native channels, and the PTC
  centerline assumption before calibration or validation.
- Installed VCU insulation products and regional thickness confirmation, exact
  ACU salt composition, VCU pipe dimensions/grade evidence and axial wall area,
  property uncertainty, and authoritative citations need facility confirmation.
- Experiment-specific ambient conditions, top-exit temperature/pressure,
  cooler closure and measurements, pressure datum/tank states, and numerical
  heater duties must be supplied per run.
- Nick's plan inventory, VCU Rev 8 candidates, and pinned-code candidates remain
  separate evidence streams; none silently supersedes another.
- The original `VCU_Loop_Coordinates_Rev8.xlsx` is retained in this worktree.
  GEO-004 checks the separate Rev7/Rev8 comparison workbook by its own name
  and schema; the original Rev 8 CSV files were not modified.

## Immediate objective

The [C2 pre-fit checkpoint](reports/checkpoints/C2_PRE_FIT_2026-09-21/README.md)
is the reproducibility baseline for the next reporting cycle. Continue the
shared geometry-revision-addressable observation contract and work backward
from the September 4 VCU diagnostic through the separate VCU metadata and
native-source gates. The September 3 ambient folder is next; a flowing-loop
Prop-30 case needs its own run-specific heater/water conditions. ACU operating
data remain on user hold. When the user resumes ACU data work, follow the
[2026-09-22 handoff](docs/workflows/2026-09-22_WORK_PLAN.md): qualify a bounded
run, preregister the learning protocol, and run a fixed-parameter diagnostic
before optimization. ACU and VCU solver geometries, datasets, parameter sets,
channel maps, and run metadata require separate evidence. The active and
review boards retain current work.

Continue VNV-006 from its bounded continuation checkpoint: retain the user's
all-source-vertex mesh rule, review search completeness and a defensible
numerical error budget, and add coupled dynamic stability only with defensible
capacities/inertia. Do not call steady root count physical stability.
[VNV-009](coordination/tasks/VNV-009.md) awaits the user's dated
verdict on the prepared VNV-007 synthetic-correction packet.
Use SAM-001's strictly checked component pilot as a narrow energy-balance
regression and its completed **mismatch inventory** to design a genuinely
matched full-loop fixture and settled SAM run before claiming M3 agreement.
The TAMU developing-flow profile evaluation is tracked as PHY-008 for after
this forward gate. Obtain
second-person review of PHY-007 and the passing VNV-001/002 and VNV-003 evidence
before scientific use.
Collect the user's MATH-007 conductance-write-up review. Review the M2
candidate and VNV-004 evidence before scientific use; independently verify
the passing VNV-005 M3 equation evidence with an outside person before any
facility hydraulic claim. A TAMU
developing-flow loss case remains a later gate. Review SOL-002's sparse
derivative/factorization and paired accuracy/timing evidence before wider
scientific use. Continue DAQ-001 from the exact ACU deposit
using bounded, checksum-first operations;
recover experiment/run metadata and a physical crosswalk before scientific use.
Review GEO-004 independently and obtain confirmed VCU sensor junction positions
before using that geometry in calibration or validation. Review the MATH-002/003
equation-to-code drafts against VNV findings before treating them as verified.

## Current review documents

- [ACU/VCU reconciliation](docs/geometry/reviews/2026-09-09_ACU_VCU_RECONCILIATION.md)
- [TAMU architecture review](docs/reference_reviews/TAMU_MODEL_ARCHITECTURE.md)
- [TAMU materials review](docs/reference_reviews/TAMU_MODEL_MATERIALS.md)
- [REV-001 acceptance](coordination/status/2026/09/2026-09-09_REV-001.md)
- [Facility decisions](coordination/status/2026/09/2026-09-10_CFG-003.md)
- [ACU data-deposit inventory](docs/data/ACU_BOX_DATA_DEPOSIT_INVENTORY_2026-09-10.md)
- [Open-question board](coordination/questions/BOARD.md)
- [Task review queue](coordination/REVIEW_BOARD.md)
- [Completed task archive](coordination/archive/BOARD_DONE.md)
- [M0 control-volume mathematics](docs/theory/M0_CONTROL_VOLUME_AND_SOLVER.md)
- [M1 steady no-flow mathematics](docs/theory/M1_STEADY_NO_FLOW_CONTROL_VOLUME_AND_MATRIX.md)
- [M1 six-cell layer-ordered matrix](docs/theory/M1_LAYER_ORDERED_SIX_CELL_MATRIX.md)
- [M2 signed-flow equations](docs/theory/M2_PRESCRIBED_FLOW_ENERGY.md)
- [M2 independent synthetic verification](reports/verification/M2_VERIFICATION.md)
- [Versioned solver numerics and state order](docs/theory/SOLVER_NUMERICS_AND_STATE_ORDER.md)
- [Sparse solver verification](reports/verification/SPARSE_SOLVER_VERIFICATION.md)
- Provisional M0--M3 LaTeX draft in the paper workspace at
  /scratch/09748/andresfierro231/projects_scratch/Papers/UTexas_Research/initial_solver_writeup/main.tex;
  the original detailed M1 derivation remains as appendices. The current
  13-page PDF is kept local and ignored by Git; the 42-file source inventory
  records exact input hashes. Independent physics and facility review remain open.
- [2026-09-15 work plan](docs/workflows/2026-09-15_WORK_PLAN.md)
- [M1 no-flow and VCU fluid decision](docs/decisions/ADR-0009-m1-stagnant-fluid-conduction-and-vcu-fluid-identity.md)
- [M1 optional pipe-wall mechanism](docs/decisions/ADR-0010-m1-optional-axial-pipe-wall-conduction.md)
- [M1 default-on pipe-wall decision](docs/decisions/ADR-0011-m1-default-on-pipe-conduction.md)
- [M0 verification](reports/verification/M0_VERIFICATION.md)
- [M1 verification](reports/verification/M1_VERIFICATION.md)
- [M1 pipe-on verification](reports/verification/M1_PIPE_AXIAL_VERIFICATION.md)
