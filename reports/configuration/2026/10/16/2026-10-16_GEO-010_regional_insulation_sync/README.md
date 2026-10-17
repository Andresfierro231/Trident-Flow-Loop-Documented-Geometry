# GEO-010: regional insulation synchronization

Date: 2026-10-16. Owner: geometry / agent-root-insulation-sync-20261016.
Status: checked reported-coverage reconciliation, pending outside review.

The earlier workbook was too conservative: missing product validation and
installed surveys were represented as Unknown regional coverage despite known
user reports/model assignments. This task restores the reported data.

| Region group | Coverage | Insulation | Approximate thickness |
|---|---|---|---|
| Upcomer, downcomer, all four corners | Insulated | Fiberglass MAIN-INS | 50.8 mm (2 in) |
| Straight heater | Insulated | Calcium-aluminum-silicate ceramic-fiber HEATER-INS strip only | 6.35 mm (1/4 in) |
| Straight D-E pre-cooler, jacket and post-cooler | Bare | None | Not applicable |

LF-01 remains covered. No extra 50.8 mm fiberglass goes over the heater strip.
All coverage evidence is Reported; thickness values are approximate estimates,
not measurements or validated installed-product data. Exact local STC contacts,
transition positions, product/certificate/fit validation and uncertainty remain
open independently. Those open details do not erase known reported coverage.

Reviewed source chain: VCU-007/ADR-0025 regional materials/thicknesses;
VCU-008/ADR-0026 historical full-loop assumption; Oct6/14 bare straight cooler
amendments; GEO-009 corrected covered upper corners/LF-01; current user confirms
upcomer/heater. Current guide INSULATION_CURRENT.md reconciles the hierarchy.

Workbook DRAFT-006 now has all ten regions populated, with source crosswalk,
material links and reference form/requirement updates. Material equations,
geometry, sensors, fluid/calibration/thermal boundaries and contributor/approval
fields remain unchanged. Model regional v7 and Rev9 selection v3 add explicit
coverage evidence/crosswalk without changing v6's numerical model assignments.
V6/v2/v1 and historical reports/checkpoints are preserved.

Verification: 35 workbook/source/preservation checks; 30 repository behavior
tests; 13 focused model/material tests pass. PDF compiled to 76 pages, final
compiler log has no warnings/overfull boxes; pdfTeX 1.40.24 / TeX Live 2022
from TACC module texlive/2023. No visual inspection. Numeric closure is unchanged.

No historical solver results or operating data are recomputed. Current input
records agree; regional YAML is not automatically wired through the general
solver loader. This is not a full Rev9 solver migration or facility validation.

Exact inputs/hashes and the reproducible migration are documented under
`support/evidence/2026-10-16_GEO-010_regional_insulation_sync/` from repository
root. Commands: `python3 -B support/scripts/sync_regional_insulation.py --check
--summary /tmp/GEO-010-checks.json` (on one line), `python3 -B -m unittest discover
-s support/tests -v`, then `module load texlive/2023` and `python3 -B support/scripts/build.py`.
Full logs and structured checks are retained alongside this report.
