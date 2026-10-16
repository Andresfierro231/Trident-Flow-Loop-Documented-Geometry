"""Readable control-package content, generated from the editable workbook.

Forms collect evidence; they never silently overwrite geometry or approval state.
"""
import re

FORM_NAMES = ('Form pipe', 'Form sensor', 'Form material')
REQUIRED_SHEETS = FORM_NAMES + ('Requirements', 'Phase requests', 'Review issues', 'Sources')
EVIDENCE_TYPES = {'Unknown', 'CAD-derived', 'Installed measurement', 'Reported', 'Modeling assumption'}


def validate(tables):
    for name in REQUIRED_SHEETS:
        if name not in tables:
            raise ValueError(f'Missing worksheet: {name}')
    records = tables['Requirements']
    ids = [r['Field ID'] for r in records]
    if len(set(ids)) != len(ids):
        raise ValueError('Requirements: duplicate Field ID.')
    sources = {r['Source ID'] for r in tables['Sources']}
    if len(sources) != len(tables['Sources']):
        raise ValueError('Sources: duplicate Source ID.')
    for row in records:
        for key in ('Field ID', 'Package', 'Field', 'Purpose', 'Responsible team', 'Applicability',
                    'Requirement source', 'Requirement locator', 'Current evidence', 'Evidence type',
                    'Evidence source', 'Evidence locator', 'Review state', 'Unresolved question'):
            if row.get(key) in (None, ''):
                raise ValueError(f'Requirements / {row.get("Field ID")}: {key} is required. Use Unknown when unresolved.')
        if row['Evidence type'] not in EVIDENCE_TYPES:
            raise ValueError(f'{row["Field ID"]}: approval belongs in Review state, not Evidence type.')
        if row['Review state'] not in {'Needs information','Needs review','Approved for stated use','Not applicable'}:
            raise ValueError(f'{row["Field ID"]}: choose a listed review state.')
        if row['Review state'] in {'Approved for stated use','Not applicable'}:
            keys = ('Decision scope / rationale','Reviewer / date','Effective configuration')
            if row['Review state']=='Approved for stated use':
                keys += ('Selected choice',)
            for key in keys:
                if not row.get(key):
                    raise ValueError(f'{row["Field ID"]}: {key} is needed to record this review decision.')
        for key in ('Requirement source', 'Evidence source'):
            for ref in row[key].split(';'):
                ref = ref.strip().split(' / ')[0]
                if ref != 'None supplied' and ref not in sources:
                    raise ValueError(f'{row["Field ID"]}: source ID {ref} is not in Sources.')
    for name in FORM_NAMES:
        for row in tables[name]:
            if row['Field ID'] not in ids:
                raise ValueError(f'{name}: unknown Field ID {row["Field ID"]}.')
            if row['Entry evidence type'] not in EVIDENCE_TYPES:
                raise ValueError(f'{name}: choose a listed evidence type; approval is a separate decision.')
    request_ids = [r['Request ID'] for r in tables['Phase requests']]
    if len(request_ids) != len(set(request_ids)):
        raise ValueError('Phase requests: duplicate Request ID.')


def build_report(tables, model, figs, digest, tex, latex_table):
    """Keep the front easy to use; put the complete traceable register in appendices."""
    def esc(value):
        if isinstance(value, str):
            # Long identifiers/filenames need natural line-break opportunities.
            value = re.sub(r'\b([0-9a-f]{64})\b', lambda m: ' '.join(m[1][i:i+16] for i in range(0,64,16)), value)
        return tex(value).replace(r'\_', r'\_\allowbreak{}')

    def line(label, value):
        return r'\textbf{' + esc(label) + ':} ' + esc(value) + r'\par'

    def section(title, label=None):
        return r'\clearpage\section{' + esc(title) + '}' + (r'\label{'+label+'}' if label else '')

    out = [r'''\documentclass[11pt]{article}
\usepackage[letterpaper,margin=0.7in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,booktabs,longtable,array,graphicx,tikz,xcolor,hyperref}
\usetikzlibrary{arrows.meta}
\definecolor{navy}{HTML}{16374A}
\definecolor{pale}{HTML}{EEF3F6}
\definecolor{amber}{HTML}{FFF4D6}
\definecolor{muted}{HTML}{576976}
\hypersetup{colorlinks=true,linkcolor=navy,urlcolor=navy,pdftitle={VCU Configuration and Modeling Control}}
\renewcommand{\familydefault}{\sfdefault}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\setlength{\emergencystretch}{3em}
\setcounter{tocdepth}{1}
\raggedbottom
\newcommand{\notebox}[1]{\par\noindent\colorbox{amber}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{#1}}\par}
\begin{document}
{\color{navy}\LARGE\bfseries VCU Configuration and\\[4pt] Modeling Control}\par
{\large Start here, evidence register and three sample forms}\par
''', line('Configuration', model['settings']['Configuration ID']),
        r'\notebox{\textbf{Draft for team completion.} The Rev9 geometry is a CAD candidate. Installed measurements and release approvals still need evidence.}',
        r'\section*{Start with one record}',
        r'You do not need to learn LaTeX to contribute. Open \textbf{inputs/VCU\_inputs.xlsx}, choose a Form tab, and fill the amber response cells. The package maintainer turns the saved workbook into this document and the labeled drawings.',
        r'\begin{enumerate}',
        r'\item \textbf{Choose one item.} Start with the upcomer pipe, the STC-02 sensor reference, or the insulation conductivity example.',
        r'\item \textbf{Read the reference.} Gray cells show what the supplied evidence says and where to find it. They are not confirmed answers.',
        r'\item \textbf{Enter what you know.} Add units, measurement date and the point or component you checked. Leave unknown values blank; add the open question in the evidence cell.',
        r'\item \textbf{Attach proof.} Name the file and the exact photo, page, row or certificate. Choose the evidence type and add your name/date.',
        r'\item \textbf{Return it for review.} The reviewer records the decision and its scope. Form entries do not automatically replace the baseline.',
        r'\end{enumerate}',
        r'\textbf{A useful first return:} one completed form, its evidence files, and a short list of anything you could not confirm. A partial, honest record is useful.',
        r'\textbf{Keep the example attached to its item.} To work on a different segment, sensor or material, save a separate response copy. Clear the old example references or have the maintainer replace them with evidence for the new item.',
        r'\textbf{Find your page:} pipe form p.~\pageref{form-pipe}; sensor form p.~\pageref{form-sensor}; property form p.~\pageref{form-material}; phase requests p.~\pageref{phase-requests}; complete requirements p.~\pageref{requirements}.',
        r'\textbf{Need help?} The repository file \textbf{START\_HERE.md} has separate paths for the experimental team, computational team and package maintainer.',
        section('Who fills in what?'),
        r'\textbf{Experimental team.} Record the installed hardware, fluids, sensor/channel mapping, calibration evidence, electrical wiring, coolant routing and raw logs. Use the phase requests to see what evidence is needed next.',
        r'\textbf{Computational team.} Propose model domains, boundary conditions, material correlations, uncertainty methods and validation checks. Explain the intended use and why each choice is suitable.',
        r'\textbf{Package reviewer.} Resolve conflicting evidence and record the approved choice, scope, date and effective configuration. The listed teams are suggested owners; named owners and release authority still need confirmation.',
        r'\textbf{Package maintainer.} Preserve the submitted evidence, update accepted input records deliberately, regenerate, and check that the document and diagrams match the saved workbook.',
        r'\subsection*{Two labels answer two different questions}',
        latex_table([
            {'a':'CAD-derived','b':'A result from the identified Rev9 model; installation not verified.'},
            {'a':'Installed measurement','b':'A measured physical item with date, method and evidence.'},
            {'a':'Reported','b':'A statement in notes or a communication; original evidence may still be needed.'},
            {'a':'Modeling assumption','b':'A proposed idealization or convention requiring rationale.'},
            {'a':'Unknown','b':'No supported value is available yet.'}], ['Evidence type','What it means'],['a','b'],[.24,.68]),
        r'\textbf{Review state is separate:} Needs information, Needs review, Approved for stated use, or Not applicable with a reason. Approval must name the selected value, reviewer, date and scope. A CAD-derived value stays CAD-derived after review. This package establishes no approved physical or modeling choices.',
        r'\subsection*{What belongs in each package?}',
        r'\textbf{Configuration Control} describes the physical setup and measurement chain: geometry, insulation, fluids, instruments, calibration, heating/cooling, branch states and run identity.',
        r'\textbf{Modeling Control} describes how that setup is represented: 1-D and CFD/CHT domains, boundary/initial conditions, shared properties, closures, numerical checks, uncertainty and independent validation.',
        r'\textbf{Shared records} connect the two: evidence, approvals, sensor-to-model mapping, measured power, property selection and validation applicability.',
        r'\notebox{The STNCL documents are draft evidence sources. The requests in this package do not authorize running a test or establish that Nick Luciano has approved the draft requirements.}',
        r'\clearpage\tableofcontents']

    out += [section('Configuration record and acceptance basis', 'configuration-record'),
        r'\begingroup\small',
        r'The configuration record supplies the measured inputs and uncertainties needed to compare an experiment with a model. Record what changed, which evidence applies, and what error is acceptable for the stated comparison. Do not replace an unknown with a nominal value to complete the document.',
        r'\subsection*{Record identity}',
        *[line(key, model['settings'].get(key)) for key in
          ('Facility', 'Configuration ID', 'Status', 'Scope', 'Geometry source',
           'Prepared by', 'Checked by', 'Plan approval')],
        r'\subsection*{Complete a dated package}',
        latex_table([
            {'item':'Identity and changes', 'record':'Start; Requirements C01--C04',
             'evidence':'Effective date, configuration ID, change history, reviewer and approved use.'},
            {'item':'Geometry and insulation', 'record':'Geometry; Form pipe; C05--C16',
             'evidence':'Lengths, diameters, sensor datum, layer coverage, material certificates and measurement uncertainty.'},
            {'item':'Photographs', 'record':'Requirements C17',
             'evidence':'Dated overview and detail files linked to the configuration, component and viewpoint.'},
            {'item':'Fluids and properties', 'record':'Fluids; Materials; Form material; C18--C20; M12--M19',
             'evidence':'Product/composition, circuit, property source, equation, units, applicability and uncertainty.'},
            {'item':'Instrumentation and calibration', 'record':'Sensors; Calibration; Form sensor; C21--C33',
             'evidence':'All instruments including fiber sensors: position, channel, certificate, correction, validity and uncertainty.'},
            {'item':'Heater and cooler', 'record':'Thermal spans; C34--C41',
             'evidence':'Active boundaries, circuits, measured power/flow, calibration, feedback and setpoint history.'},
            {'item':'Run and boundary state', 'record':'Model choices; C42--C46',
             'evidence':'Branches, tank/valve states, ambient conditions, operating limits, run ID and raw files.'},
            {'item':'Model and acceptable error', 'record':'Model choices; Requirements M01--M32',
             'evidence':'Model revision, prediction targets, uncertainty method, conservation/convergence checks and quantitative acceptance limits.'}
        ], ['Package item', 'Workbook record', 'Evidence to retain'],
           ['item', 'record', 'evidence'], [.21, .28, .43]),
        r'\subsection*{Define what is good enough before comparison}',
        r'For each prediction target, record the quantity and units, applicable run/configuration, comparison interval, error metric, quantitative acceptance limit and uncertainty coverage. Explain how measurement and model uncertainty enter the decision. Use Requirements M01, M17 and M22--M32 for the selected choices and review scope; no numerical acceptance limits are supplied by this template.',
        r'\textbf{Where to enter evidence:} keep file/page/photo locators in the corresponding Requirements evidence fields. Use the selected choice, decision scope, reviewer/date and effective configuration fields for review decisions. The checklist above is a navigation aid, not a second editable record.',
        r'\par\endgroup']

    details = {
        'Form pipe': ('Pipe and insulation segment', 'form-pipe',
            'Example: VCU upcomer B-C. Confirm the actual section before using the reported pipe or insulation details.'),
        'Form sensor': ('Sensor, channel and calibration', 'form-sensor',
            'Example: drawing reference STC-02. Identify the actual hardware and channel independently; a drawing label is not a DAQ mapping.'),
        'Form material': ('Material-property selection appendix', 'form-material',
            'Example: thermal conductivity of reported main-pipe fiberglass insulation. The equation is a candidate from notes, not a selected correlation.')}
    for name in FORM_NAMES:
        title, label, intro = details[name]
        out += [section(title, label), esc(intro),
            r'\par\textbf{Workbook tab:} '+esc(name)+r'. Fill columns F--I. Every unanswered line below remains \textbf{TO CONFIRM}.',
            r'\textbf{Record context:} configuration / item / date / completed by: \hrulefill\par']
        records = tables[name]
        for i, row in enumerate(records):
            if i and i % 5 == 0:
                out += [r'\clearpage', r'{\large\bfseries '+esc(title)+r' --- continued}\par',
                        r'\textbf{Record context:} configuration / item / date: \hrulefill\par']
            entry = row.get('Your entry')
            out += [r'\par\noindent\begin{minipage}{\textwidth}\small',
                r'{\color{navy}\bfseries '+esc(row['What to record'])+r'}\hfill '+esc(row['Field ID'])+r'\par',
                r'\colorbox{pale}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{',
                r'\textbf{Reference only ('+esc(row['Reference basis'])+'):} '+esc(row['Reference only'])+r'\par',
                r'{\footnotesize Source: '+esc(row['Reference source'])+r'}}}\par',
                r'\textbf{Your entry:} '+(esc(entry) if entry not in (None, '') else r'{\color{muted}TO CONFIRM}\enspace\hrulefill')+r'\par',
                r'{\footnotesize\textbf{Evidence:} '+(esc(row.get('Your evidence file / location')) if row.get('Your evidence file / location') else r'file + page/photo/row: \hrulefill')+r'\par',
                line('Entry type / reviewer and date',str(row['Entry evidence type'])+' / '+str(row.get('Reviewer / date') or 'Pending')),
                r'}\end{minipage}\par\vspace{5pt}']
        if name == 'Form material':
            out += [r'\notebox{\textbf{Before selection:} verify the original data, temperature convention, units and property-specific domain. The reported 297--533 K interval is a fit domain, not a VCU operating limit. Repeat this form for every required property and material.}']

    out += [section('What the draft phases ask the team to return', 'phase-requests'),
        r'These are concrete information requests extracted from draft STNCL Phases 0--4. Values and test conditions in those plans remain draft. The electrical-heater cautions below must be resolved for VCU.',
        r'\textbf{How to use:} pick a request, gather the listed files, and return them with the configuration/run ID. The computational team supplies the analysis where indicated. Mark completion only after the review partner has assessed the evidence.']
    for i, row in enumerate(tables['Phase requests']):
        out += [r'\par\noindent\begin{minipage}{\textwidth}\small\setlength{\parskip}{2pt}',
            r'\subsection*{'+esc(row['Request ID'])+' | '+esc(row['Request'])+'}',
            line('Please do', row['Experimental-team action']),
            line('Return', row['Return this evidence']),
            line('VCU adaptation / caution', row['VCU adaptation / caution']),
            line('Review partner', row['Review partner']),
            line('Traceability', row['Field IDs']+'; '+row['Source locator']),
            line('Done when', row['Completion check']),r'\end{minipage}\par\vspace{8pt}']

    out += [section('Issues to resolve together'),
        r'All issues below are open. The suggested owners help route a question; they do not imply an assigned or approved responsibility.']
    for i, row in enumerate(tables['Review issues']):
        out += [r'\par\noindent\begin{minipage}{\textwidth}\small\setlength{\parskip}{2pt}',
            r'\subsection*{'+esc(row['Issue ID'])+' | '+esc(row['Kind'])+'}',
            line('Finding', row['What conflicts / is missing']),
            line('Next decision', row['Resolution needed']),
            line('Suggested owner', row['Suggested owner']),
            line('Source / locator', row['Source and locator']),
            line('Affected fields', row['Affected fields']),r'\end{minipage}\par\vspace{8pt}']

    out += [section('Rev9 geometry and drawing conventions'),
        r'Only the qualified Rev9 structured geometry seeds the CAD candidate. Original source rows are retained in reference/rev9\_extraction.json. Installed measurements, reported nominal sizes and selected model geometry remain separate records.',
        r'\begin{itemize}',
        r'\item Main-loop bore remains unknown in the CAD baseline. Local spool bores cannot supply the missing loop-wide value.',
        r'\item Heater pieces overlap by about 7.202 mm and their axes differ by about 0.152 mm. The displayed heater length is a projected span, not an exact continuous hydraulic length.',
        r'\item The G--H bend is reconstructed from spline geometry with qualified fit residuals. Dashed overview connectors are schematic; they do not define hydraulic arc lengths.',
        r'\item Jacket shell and full envelope differ. Neither establishes the active cooling span; clamps do not establish active electrical heating spans.',
        r'\item Sensor markers show geometric references. Physical junctions, fiber extents, channels and circumferential positions require evidence.',
        r'\end{itemize}',
        r'\textbf{Measured distances:} choose the segment and the labeled endpoint. Measure along its axis. Record which physical point you measured. For a bent section, ask the maintainer for a qualified path convention before entering an arc distance.',
        r'\textbf{Circumferential position:} this is the location around the pipe, separate from the leg inclination. For a vertical leg, ``top of the pipe'' is ambiguous; the proposed zero is drawing +x. The convention needs team agreement.',
        r'\subsection*{Coordinate definitions for the maintainer}',
        r'Origin B; $x$ rightward, $y$ upward, $n$ out of the drawing. Straight-leg direction $\phi$ is clockwise from upward vertical. Thus $\Delta x=L\sin\phi$ and $\Delta y=L\cos\phi$. Circumferential angle $\alpha$ is a separate input.',
        r'For distance $d$ from the start, $s=d$; from the end, $s=L-d$. Then $\mathbf{p}_{a}=\mathbf{p}_0+s\mathbf{t}$. Define $\mathbf{e}_0$ as projected upward vertical perpendicular to $\mathbf{t}$, normalized; for vertical pipes use drawing $+x$. Let $\mathbf{e}_{90}=\mathbf{t}\times\mathbf{e}_0$. The point is $\mathbf{p}=\mathbf{p}_{a}+r(\cos\alpha\,\mathbf{e}_0+\sin\alpha\,\mathbf{e}_{90})$.',
        r'Both radius and angle are required for a full point. A blank is unknown, not zero. Printed precision is not measurement uncertainty.',
        r'\subsection*{Current generator qualifications}',r'\begin{itemize}']
    out.extend(r'\item '+esc(n) for n in model['notes'])
    out.append(r'\end{itemize}')
    for fig in figs:
        out += [r'\clearpage\thispagestyle{empty}',r'\begin{center}\resizebox{\textwidth}{!}{%', fig.tikz(),r'}\end{center}']
    out += [section('Current candidate input tables'),
        r'\subsection*{Main-loop geometry}',
        latex_table([dict(r,endpoints=f'{r["Start"]} to {r["End"]}') for r in tables['Geometry']],
            ['Segment','Endpoints','Length mm','Phi deg','Evidence'],
            ['Segment','endpoints','Length mm','Phi deg','Status'],[.23,.12,.16,.14,.22]),
        r'Bends use offsets, not straight-length inputs. See the editable Geometry sheet and source length basis. The example forms do not populate these baseline cells.',
        r'\subsection*{Main-loop geometric sensor references}',
        latex_table(model['sensors'], ['Sensor','Segment','From','Distance mm','Angle deg'],
            ['Sensor ID','Segment','From endpoint','Distance mm','Circumference deg'],[.17,.25,.10,.17,.17]),
        r'JTC-A/B are retained in Calibration, but jacket-port positions are not yet drawn. DAQ mappings, calibration and model mappings remain unknown unless separately entered with evidence.',
        r'\subsection*{VCU fluid choices}',
        r'Prop-30, air and water are permitted candidate options from the user. A circuit/run assignment is still required. The supplied draft phase campaign is Prop-30-specific.',
        latex_table([dict(r,range=f'{r["Minimum C"]} to {r["Maximum C"]}' if r['Minimum C'] is not None and r['Maximum C'] is not None else None) for r in tables['Fluids']],
            ['Fluid','Product','Circuit','Range C'],['Fluid ID','Product','Circuit','range'],[.15,.30,.22,.20])]

    out += [r'\appendix', section('Complete requirements and evidence register', 'requirements'),
        r'The Requirements workbook tab is the editable master. Each record states why the field is needed, who should supply it, where the requirement and evidence came from, what uses it supports, and what remains unresolved. Requirement provenance is distinct from evidence for a value.',
        r'\textbf{Review rule:} the records below describe candidate evidence. Approved choices require a recorded decision, scope and effective configuration; none has been established in this seed package.']
    for i, row in enumerate(tables['Requirements']):
        out += [r'\par\noindent\begin{minipage}{\textwidth}\small\setlength{\parskip}{2pt}',
            r'\subsection*{'+esc(row['Field ID'])+' | '+esc(row['Field'])+'}',
            line('Purpose', row['Purpose']),
            line('Package / responsible team', row['Package']+' / '+row['Responsible team']),
            line('Applies to', row['Applicability']),
            line('Requirement source / locator', row['Requirement source']+'; '+row['Requirement locator']),
            line('Current evidence ['+row['Evidence type']+']', row['Current evidence']),
            line('Evidence source / locator', row['Evidence source']+'; '+row['Evidence locator']),
            line('Review state', row['Review state']),
            line('Selected choice', row.get('Selected choice') or 'None selected'),
            line('Decision scope / rationale', row.get('Decision scope / rationale')),
            line('Reviewer / date; effective configuration', str(row.get('Reviewer / date') or 'Pending')+'; '+str(row.get('Effective configuration') or 'Unknown')),
            line('To resolve', row['Unresolved question']),r'\end{minipage}\par\vspace{5pt}']

    out += [section('Current model and material input records'),
        r'These records reproduce the existing Model choices and Materials worksheets. Unknown inputs remain visible. New answers in the three prototype forms are evidence for review; they do not automatically populate these records.']
    for name, key in [('Model choices','Interface / topic'),('Materials','Material ID')]:
        out += [(r'\clearpage' if name=='Materials' else '')+r'\subsection{'+esc(name)+'}']
        for i,row in enumerate(tables[name]):
            out += [r'\par\noindent\begin{minipage}{\textwidth}\small\setlength{\parskip}{2pt}',r'\subsection*{'+esc(row[key])+'}']
            out.extend(line(k,v) for k,v in row.items() if k!=key)
            out += [r'\end{minipage}\par\vspace{5pt}']
    out += [r'\clearpage\subsection{Calibration summary}',
        r'Complete certificates, corrections and acquisition details remain on Calibration and in the resolved input export.',
        latex_table([dict(r,mapping=' / '.join(str(r[k]) for k in ('1-D mapping','CFD mapping') if r.get(k)) or None) for r in tables['Calibration']],
            ['Sensor','Last calibration','Uncertainty','Model mapping'],['Sensor ID','Last calibration','Uncertainty','mapping'],[.15,.22,.24,.26])]

    out += [section('Source catalog and limits of use'),
        r'Use the source ID with the row/page/section locator. Source files are not operating instructions. Exact local paths and read-time file hashes are recorded in reference/source\_manifest.json. Files remain at their supplied locations; they are not all duplicated into this repository.']
    for i, row in enumerate(tables['Sources']):
        if i and i % 4 == 0:
            out += [r'\clearpage{\large\bfseries Source catalog --- continued}\par']
        out += [r'\par\noindent\begin{minipage}{\textwidth}\small',
            r'\subsection*{'+esc(row['Source ID'])+' | '+esc(row['File / record'])+'}',
            line('Revision / context', row['Revision / context']),
            line('Find it', row['Locator guide']),
            line('Qualification', row['Qualification']),r'\end{minipage}\par\vspace{5pt}']
    out += [r'\subsection*{Context retained outside the VCU baseline}',
        r'ACU general-arrangement drawings, ANEC-000126 sensor labels, ACU sensor naming notes and ACU images belong to ACU. They supply no VCU values or channel mappings here. The supplied VCU overview PNGs identify Rev8 as their source and are visual-format references only. Mixed geometry archives and note links require member-level facility/revision checks; their contents are not imported wholesale.',
        r'\subsection*{Generated record identity}',
        line('Workbook SHA-256 (spaces only for wrapping)', digest),
        r'All form answers, source rows and requirement fields are exported to generated/resolved\_inputs.json. The readable register is also available in generated/requirements\_and\_evidence.md. A successful build verifies the input structure and drawing geometry, not experimental or modeling readiness.',
        r'\end{document}']
    return '\n'.join(out)


def markdown_register(tables):
    out = ['# VCU requirements and evidence register',
           'Generated from `inputs/VCU_inputs.xlsx`. Edit the workbook and regenerate. Draft; no release approval is implied.',
           'Evidence type and review state are independent. All proposed owners require team confirmation.']
    for name, key in [('Requirements','Field ID'), ('Phase requests','Request ID'), ('Review issues','Issue ID'), ('Sources','Source ID')]:
        out.append('## '+name)
        for row in tables[name]:
            out.append('### '+str(row[key]))
            out.extend(f'**{k}:** {v if v not in (None, "") else "Unknown"}\n' for k,v in row.items() if k!=key)
    return '\n\n'.join(out)+'\n'
