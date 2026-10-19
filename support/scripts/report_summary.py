"""Concise configuration PDF; full evidence remains in the workbook and audit."""
from collections import Counter, defaultdict
from pathlib import Path
import re
from urllib.parse import quote

from report_front import build_front

REPO = 'https://github.com/Andresfierro231/Trident-Flow-Loop-Documented-Geometry/blob/main/'
ROOT = Path(__file__).resolve().parents[2]


def build_summary(tables, model, figs, digest, tex, latex_table, insulation_figure):
    def esc(value):
        return tex(value).replace(r'\_', r'\_\allowbreak{}')

    def line(label, value):
        return r'\textbf{' + esc(label) + ':} ' + esc(value) + r'\par'

    def section(title, label):
        return r'\clearpage\section{' + esc(title) + r'}\label{' + label + '}'

    def file_link(path, title):
        return r'\href{' + REPO + quote(path, safe='/') + '}{' + esc(title) + '}'

    def cell(value):
        return value[0] if isinstance(value, tuple) else esc(value).replace('\n', r'\par ')

    def table(headers, rows, widths):
        spec = ''.join(r'>{\raggedright\arraybackslash}p{' + str(w) + r'\textwidth}' for w in widths)
        result = [r'\begingroup\small\setlength{\tabcolsep}{4pt}',
                  r'\begin{longtable}{' + spec + '}', r'\toprule',
                  ' & '.join(r'\textbf{' + esc(h) + '}' for h in headers) + r'\\\midrule\endhead']
        result += [' & '.join(cell(v) for v in row) + r'\\[4pt]' for row in rows]
        return '\n'.join(result + [r'\bottomrule\end{longtable}\endgroup'])

    def joined(values):
        return ' / '.join(dict.fromkeys(str(v) for v in values if v not in (None, ''))) or 'Unknown'

    out = [build_front(tables, model, figs, esc, line, section, latex_table,
                       insulation_figure, compact=True),
           r'\appendix\phantomsection\label{appendices}',
           section('Geometry reference', 'geometry-detail'), r'\label{baseline-tables}',
           r'CAD candidate dimensions. Installed measurements and nominal model values remain separate. Sources: R9, SEG, SNS; current selection: VSEL, WORK.',
           table(['Segment', 'Endpoints', 'Length mm', 'Phi deg', 'Basis'],
                 [(r['Segment'], r['Start'] + ' to ' + r['End'], r['Length mm'], r['Phi deg'], r['Status'])
                  for r in tables['Geometry']], [.23, .13, .17, .12, .25]),
           r'\textbf{Frame and stationing.} Origin B; $x$ right, $y$ up, $n$ out of the drawing. '
           r'Straight-leg $\phi$ is clockwise from upward vertical: $\Delta x=L\sin\phi$, $\Delta y=L\cos\phi$. '
           r'Sensor distances are measured from the named endpoint along the segment. A distance from the end gives $s=L-d$.',
           r'\textbf{Qualification.} Bend offsets close the drawing; they are not physical arc lengths. '
           r'Heater pieces overlap by about 7.202 mm and their axes differ by about 0.152 mm. '
           r'The heater length is a projected span. The G--H spline bend has fit qualifications. '
           r'Full source rows and coordinate definitions are retained in the workbook and detailed audit.',
           r'\textbf{Sensor coordinates.} Circumferential angle and sensing radius are separate from leg inclination. '
           r'Both are needed for a full sensing point. Blank inputs remain unknown; printed precision is not uncertainty.']
    if model['notes']:
        out += [r'\textbf{Generator qualifications}\begin{itemize}',
                *[r'\item ' + esc(n) for n in model['notes']], r'\end{itemize}']

    out += [section('Regional insulation', 'insulation-detail'),
            r'Coverage applies to the whole named region. Thickness is an approximate reported estimate. '
            r'Local STC contacts and transition details are separate. Sources: VREG, VTOP, CURRENT.',
            table(['Region', 'Boundary', 'Coverage', 'Material', 'mm'],
                  [(r['name'], r['boundary_reference'], r['coverage'], r['material_id'], r['thickness_mm'])
                   for r in model['insulation_regions']], [.23, .27, .14, .17, .08]),
            r'Unknown coverage differs from confirmed bare pipe. Material identity, installed thickness, contact, '
            r'supports and cladding require evidence. Jacket partitions describe mechanical extents; they do not '
            r'establish active cooling boundaries. Per-region notes, station limits and evidence locators remain '
            r'in Insulation regions and the detailed audit.']
    evidence_groups = defaultdict(list)
    for row in model['insulation_regions']:
        evidence_groups[(row['evidence_type'], row['evidence_file_location'])].append(row['region_id'])
    for (basis, locator), regions in evidence_groups.items():
        scope = 'All regions' if len(regions) == len(model['insulation_regions']) else ', '.join(regions)
        out += [line(scope + ' [' + basis + ']', locator)]

    out += [section('Channels and calibration', 'calibration-detail'),
            r'Working bindings and observation roles are reproduced below. They do not establish the installed '
            r'sensing junction, calibrated accuracy or applicability to an earlier run. STC roles describe the '
            r'outside pipe surface; PTC1--4 centerline observation is a model assumption.',
            table(['Native channel', 'Drawing reference / domain', 'Working role', 'Source'],
                  [(r['Native channel'], r['Reference / domain'], r['Working role / operator'], r['Basis / source'])
                   for r in tables.get('Native channels', [])], [.14, .26, .39, .11])]
    # Older/partial workbooks may have no native-channel sheet. Preserve entered
    # calibration mappings without printing identical 1-D and CFD text twice.
    if not tables.get('Native channels'):
        out += [table(['Sensor', 'Model observation mapping'],
                      [(r['Sensor ID'], joined([r.get('1-D mapping'), r.get('CFD mapping')]))
                       for r in tables['Calibration']], [.18, .72])]
    unbound = [r for r in tables['Sensors'] if not r.get('DAQ channel')]
    if unbound:
        out += [line('References with no entered DAQ binding', ', '.join(r['Sensor ID'] for r in unbound))]
    out += [r'\subsection*{Calibration evidence}']
    for key in ('Last calibration', 'Uncertainty'):
        missing = sum(r.get(key) in (None, '') for r in tables['Calibration'])
        out += [line(key + ' not recorded', str(missing) + ' of ' + str(len(tables['Calibration'])) + ' sensor records')]
    entered = [r for r in tables['Calibration']
               if any(r.get(k) not in (None, '') for k in ('Last calibration', 'Uncertainty'))]
    if entered:
        out += [table(['Sensor', 'Last calibration', 'Uncertainty'],
                      [(r['Sensor ID'], r.get('Last calibration'), r.get('Uncertainty')) for r in entered], [.18, .30, .42])]
    out += [r'Certificates, corrections, response, acquisition settings and run-specific validity remain '
            r'in Calibration. PTC5/JTC-B inlet and PTC6/JTC-A outlet are working jacket-port bindings; '
            r'the port reference is not a confirmed wetted measurement plane. Amb and Tank placements '
            r'also require confirmation. See VSEL, WORK, XWALK and the channel-specific limits in the detailed audit.']

    out += [section('Model and property summary', 'model-records'),
            r'These are documented working choices and proposals. Observed hardware, model assumptions and '
            r'approval remain separate. Full equations, input/output units, rationale and uncertainties are in '
            r'Model choices and Materials in the workbook and detailed audit.',
            table(['Topic / status', '1-D proposal', 'CFD / CHT proposal'],
                  [(r['Interface / topic'] + ' [' + str(r['Status']) + ']',
                    r.get('1-D choice'), r.get('CFD / CHT choice'))
                   for r in tables['Model choices']], [.20, .35, .35]),
            r'Per-topic evidence, observed state and sensitivity qualifications are retained in Model choices '
            r'and the detailed audit. Current working sources include VSEL, WORK, VREG and CURRENT.',
            r'\clearpage\subsection*{Property applicability}',
            table(['Record', 'Recorded domain'],
                  [(r['Material ID'], r['Valid domain']) for r in tables['Materials']], [.18, .72]),
            r'Property fit/working domains are not facility operating limits. Installed products and '
            r'property uncertainties need confirmation. Earlier Rev8 results retain their original geometry '
            r'and insulation assumptions. This document does not migrate historical results to Rev9.']

    states = Counter(r['Review state'] for r in tables['Requirements'])
    out += [section('Open decisions and evidence', 'issues-detail'), r'\label{requirements}',
            line('Requirement review states', '; '.join(f'{state}: {count}' for state, count in sorted(states.items()))),
            r'The following issue register identifies decisions to resolve. Field IDs refer to the ' +
            esc(str(len(tables['Requirements']))) + r'-record Requirements sheet; the full register, including evidence type, selection, reviewer '
            r'and decision scope, is retained in the workbook and detailed audit. Suggested owners are not assignments.',
            table(['Issue / affected fields', 'Next decision'],
                  [(r['Issue ID'] + ' | ' + r['Kind'] + '\n' + r['Affected fields'], r['Resolution needed'])
                   for r in tables['Review issues']], [.31, .59]),
            r'\textbf{Before comparison.} Record prediction targets, applicable configuration/run, comparison '
            r'interval, metric, numerical acceptance limit and uncertainty coverage. The template supplies '
            r'no approved numerical acceptance criteria. Draft Phase 0--4 requests remain in Phase requests '
            r'and the detailed audit; they do not authorize a test.']

    # Actual submitted responses must remain visible even when blank prototype
    # forms are omitted from the short PDF. Responses never select a baseline.
    submitted = [(name, r) for name in ('Form pipe', 'Form sensor', 'Form material')
                 for r in tables[name] if any(r.get(k) not in (None, '')
                                             for k in ('Your entry', 'Your evidence file / location', 'Reviewer / date'))]
    if submitted:
        out += [r'\subsection*{Submitted evidence awaiting review}',
                r'Form responses below are submissions for review and do not automatically update the baseline.',
                table(['Form / field', 'Submitted response', 'Evidence / type / reviewer'],
                      [(name + ' / ' + r['Field ID'], r.get('Your entry'),
                        joined([r.get('Your evidence file / location'), r.get('Entry evidence type'), r.get('Reviewer / date')]))
                       for name, r in submitted], [.20, .33, .37])]

    out += [section('Sources', 'sources-detail'),
            r'Use each source ID with its exact row/page/section locator in the workbook or detailed audit. '
            r'Linked titles open repository copies where available. Full paths, source qualifications and '
            r'hashes remain in the supporting records.',
            r'\textbf{Scope.} R9/SEG/SNS describe a CAD candidate. VSEL/WORK and VREG/CURRENT record later '
            r'working selections. XWALK and historical diagnostics retain their dated Rev8 applicability. '
            r'P0--P4 are draft plans. ACU material and Rev8 overview images supply no VCU Rev9 values.']
    titles = {
        'VSEL': 'Rev9 working selection', 'VINS': 'Earlier insulation assignments',
        'VTOP': 'Upper-corner coverage clarification', 'VREG': 'Regional insulation update',
        'WORK': 'Rev9 working selection v3', 'XWALK': 'Historical sensor crosswalk',
        'DIAG': 'Initial system diagnostics', 'FOLLOW': 'Diagnostics follow-up',
        'DAQISS': 'Experimental-team clarification draft', 'OPCYCLE': 'Operator report on chiller cycling',
        'TRIAGE': 'Historical run-identity triage', 'FLUIDCFG': 'Provisional fluid identity',
        'ASSUME': 'Model assumptions snapshot', 'CURRENT': 'Current insulation record',
        'VMAT': 'Candidate material properties', 'V5C': 'Solid-property working domains',
    }
    rows = []
    for r in tables['Sources']:
        path = r['File / record']
        title = titles.get(r['Source ID'], Path(path).name.replace('_', ' '))
        title = re.sub(r'\.(pdf|csv|tex|md|yaml|json)$', '', title)
        rendered = file_link(path, title) if (ROOT / path).is_file() else esc(title)
        rows.append((r['Source ID'], (rendered,), r['Revision / context']))
    out += [table(['ID', 'Reference', 'Revision / context'], rows, [.10, .47, .33])]

    # Let this brief guide fill the end of the references instead of reserving
    # another mostly empty final page.
    out += [r'\section{Contributing and full records}\label{administration}',
            r'\label{form-pipe}\label{form-sensor}\label{form-material}\label{phase-requests}',
            r'Edit the workbook and attach file/page/photo locators. Forms collect proposed evidence; '
            r'the maintainer updates the accepted baseline deliberately after review. Unknown values stay blank. '
            r'Review decisions require a named reviewer, date, scope and effective configuration.',
            table(['Need', 'Where to find it'], [
                ('Submit a pipe, sensor or property record', 'Form pipe / Form sensor / Form material tabs'),
                ('Complete requirements and review decisions', 'Requirements; Review issues'),
                ('Draft campaign evidence requests', 'Phase requests (P0--P4)'),
                ('Current understanding and its limits', 'Current knowledge; Native channels'),
                ('Equations, units and applicability', 'Materials; Model choices'),
            ], [.42, .48]),
            r'\textbf{Contributor guide:} ' + file_link('support/docs/START_HERE.md', 'Start here') + r'. '
            r'\textbf{Coordinate definitions and conventions:} ' + file_link('support/docs/TECHNICAL_REFERENCE.md', 'Technical reference') + '.',
            r'\par',
            r'\textbf{Detailed PDF:} VCU\_detailed\_audit.pdf is generated alongside this document. '
            r'It retains the full forms, phase requests, evidence register, channel-specific qualifications and source catalog.\par',
            r'\textbf{Complete data:} ' + file_link('VCU_inputs.xlsx', 'VCU workbook') + '; ' +
            file_link('support/generated/resolved_inputs.json', 'resolved inputs') + '; ' +
            file_link('support/generated/requirements_and_evidence.md', 'readable evidence register') + r'.\par',
            line('Configuration', model['settings']['Configuration ID']),
            line('Effective date', model['settings'].get('Effective date')),
            line('Status', model['settings'].get('Status')),
            line('Prepared by', model['settings'].get('Prepared by')),
            line('Checked by', model['settings'].get('Checked by')),
            line('Workbook SHA-256', ' '.join(digest[i:i+16] for i in range(0, len(digest), 16))),
            r'\end{document}']
    return '\n'.join(out)
