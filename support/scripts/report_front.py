"""A short configuration record, with links into the supporting appendices."""


def build_front(tables, model, figs, esc, line, section, table, insulation_figure):
    settings = model['settings']
    requirements = {r['Field ID']: r for r in tables['Requirements']}

    def link(label, title):
        return r'\hyperref[' + label + ']{' + title + r'}'

    def decision(field):
        row = requirements[field]
        return row.get('Selected choice') or 'Not selected'

    def figure(fig):
        return '\n'.join([r'\begin{center}\resizebox{0.93\textwidth}{!}{%',
                          fig.tikz(), r'}\end{center}'])

    out = [r'''\documentclass[11pt]{article}
\usepackage[letterpaper,margin=0.75in,headheight=15pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,booktabs,longtable,array,graphicx,tikz,xcolor,hyperref,fancyhdr}
\usetikzlibrary{arrows.meta}
\definecolor{navy}{HTML}{16374A}
\definecolor{pale}{HTML}{F2F5F6}
\definecolor{amber}{HTML}{F2F5F6}
\definecolor{muted}{HTML}{576976}
\hypersetup{colorlinks=true,linkcolor=navy,urlcolor=navy,pdftitle={VCU Configuration Record},bookmarksopen=false}
\renewcommand{\familydefault}{\sfdefault}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\setlength{\emergencystretch}{3em}
\setcounter{tocdepth}{1}
\raggedbottom
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\footnotesize\color{muted}TRIDENT / VCU}
\fancyhead[R]{\footnotesize\hyperref[overview]{Overview}\quad\hyperref[appendices]{Appendices}}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\newcommand{\notebox}[1]{\par\noindent\colorbox{pale}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{#1}}\par}
''', r'\fancyfoot[L]{\footnotesize\color{muted}' + esc(settings['Configuration ID']) + ' / ' + esc(settings.get('Status')) + '}',
        r'\fancyfoot[R]{\footnotesize\thepage}', r'\begin{document}',
        r'{\color{navy}\LARGE\bfseries VCU configuration record}\par',
        r'\refstepcounter{section}\label{overview}\addcontentsline{toc}{section}{\protect\numberline{1}Configuration overview}',
        r'{\color{muted}Flow-loop setup, instruments and supporting evidence}\par\vspace{8pt}',
        line('Configuration', settings['Configuration ID']),
        line('Effective date', settings.get('Effective date')),
        line('Status', settings.get('Status')),
        r'\textbf{Basis:} Rev9 CAD candidate. The installed configuration has not yet been verified.\par',
        r'\vspace{8pt}']

    # The overview uses the same solved endpoints as the detailed figures.
    # No photograph is substituted for unverified installed evidence.
    points = model['points']
    xmin = min(p[0] for p in points.values())
    ymin = min(p[1] for p in points.values())
    span = max(max(p[0] for p in points.values()) - xmin,
               max(p[1] for p in points.values()) - ymin)
    scale = 6.0 / span
    out += [r'\begin{center}\begin{tikzpicture}[line cap=round,line join=round]']
    for seg in model['segments'].values():
        a, b = seg['start_xyz_mm'], seg['end_xyz_mm']
        style = 'navy,line width=1.5pt' + (',dashed' if seg['Kind'] == 'bend' else '')
        out.append(f'\\draw[{style}] ({(a[0]-xmin)*scale:.4f},{(a[1]-ymin)*scale:.4f}) -- ({(b[0]-xmin)*scale:.4f},{(b[1]-ymin)*scale:.4f});')
    for name, anchor in [('upcomer', 'left'), ('cooler', 'above'),
                         ('downcomer', 'right'), ('heater', 'below')]:
        seg = model['segments'].get(name)
        if seg is None:
            continue
        a, b = seg['start_xyz_mm'], seg['end_xyz_mm']
        x = ((a[0] + b[0]) / 2 - xmin) * scale
        y = ((a[1] + b[1]) / 2 - ymin) * scale
        out.append(f'\\node[font=\\small,text=muted,{anchor},inner sep=8pt] at ({x:.4f},{y:.4f}) {{{esc(name.capitalize())}}};')
    out += [r'\node[text=muted,font=\small] at (3,3) {Main loop};',
        r'\end{tikzpicture}\par{\footnotesize\color{muted}CAD overview. Dashed corners are schematic.}\end{center}',
        r'\vspace{4pt}{\large\bfseries Read the configuration}\par',
        link('geometry-main', 'Geometry') + r'\quad / \quad' + link('insulation-main', 'Insulation') + r'\quad / \quad' + link('instruments-main', 'Instruments') + r'\par',
        link('thermal-main', 'Heating and cooling') + r'\quad / \quad' + link('materials-main', 'Materials and fluids') + r'\par',
        link('uncertainty-main', 'Uncertainty and limitations') + r'\par',
        r'\vspace{8pt}\textbf{Adding information?} Open \texttt{VCU\_inputs.xlsx} and start with one Form tab. ' + link('administration', 'Contributor instructions') + r' and ' + link('appendices', 'supporting records') + r' are in the appendices.\par',
        r'{\footnotesize\color{muted}Unknown values remain open. This draft records available evidence; it is not a released facility description.}\par',
        section('Geometry', 'geometry-main'),
        r'Axis-end dimensions and the recorded jacket envelope. Bore and insulation measurements remain open.',
        figure(figs[0]),
        r'{\small Details: ' + link('geometry-detail', 'coordinate conventions and CAD qualifications') + r'; ' + link('baseline-tables', 'dimension tables') + r'.}\par',
        section('Insulation', 'insulation-main'),
        r'Use the workbook\textquotesingle s \textbf{Insulation regions} tab. Every coverage dropdown describes the whole named region.',
        figure(insulation_figure),
        r'{\small Details: ' + link('insulation-detail', 'materials, thickness and evidence by region') + r'. No resistance factors or boundary conditions are calculated.}\par',
        section('Instruments', 'instruments-main'),
        r'Geometric sensor references on the main loop. Drawing IDs are not confirmed DAQ channel names.',
        figure(figs[1]),
        r'{\small Details: ' + link('calibration-detail', 'calibration and model mapping') + r'; ' + link('form-sensor', 'sensor evidence form') + r'. Jacket-port sensors JTC-A/B are retained in the calibration record.}\par',
        section('Heating and cooling', 'thermal-main'),
        r'The mechanical jacket envelope and active thermal regions are recorded separately.',
        r'\subsection*{Recorded boundaries}',
        r'\par']
    spans = [dict(row, location=str(row['Segment']) + ' / ' + str(row['From endpoint'])) for row in tables['Thermal spans']]
    out += [table(spans, ['Region','Segment / from','Start mm','End mm','Basis'],
                  ['Feature','location','Start mm','End mm','Status'], [.22,.20,.14,.14,.20]),
        r'Distances are measured along the named segment from the stated endpoint. A jacket envelope does not establish active cooling; clamps do not establish energized heater coverage.\par',
        r'\subsection*{Power and control evidence}',
        table([{'topic': requirements[key]['Field'], 'value': decision(key), 'state': requirements[key]['Review state']}
               for key in ('C35','C36','C37','C39','C40','C41')],
              ['Record','Selected choice','Review'], ['topic','value','state'], [.43,.24,.23]),
        r'\vfill{\small Supporting records: ' + link('model-records','boundary and control choices') + r'; ' + link('requirements','full evidence register') + r'.}\par',
        section('Materials and fluids', 'materials-main'),
        r'Candidate identities are listed below. Circuit assignments and selected property models require their own evidence.',
        r'\subsection*{Fluids}',
        table(tables['Fluids'], ['Fluid','Product','Circuit','Basis'], ['Fluid ID','Product','Circuit','Status'], [.15,.39,.18,.18]),
        r'\subsection*{Material and property records}',
        table(tables['Materials'], ['Record','Identity / product','Basis'], ['Material ID','Identity / product','Status'], [.18,.53,.19]),
        r'\vfill{\small Equations, units, applicability and uncertainty: ' + link('model-records','full material records') + r'. To propose a property choice: ' + link('form-material','material evidence form') + r'.}\par',
        section('Uncertainty and limitations', 'uncertainty-main'),
        r'The record must state how accurately the setup is known and what error is acceptable for each intended comparison.',
        table([{'topic': requirements[key]['Field'], 'value': decision(key), 'state': requirements[key]['Review state']}
               for key in ('C12','C30','M17','M22','M28','M31')],
              ['Basis for comparison','Selected choice','Review'], ['topic','value','state'], [.43,.24,.23]),
        r'\subsection*{Limits of this record}',
        r'\begin{itemize}\item The main-loop geometry is a CAD candidate. Installed dimensions, bore and insulation need supporting measurements.\item Sensor stations are geometric references. Channel identity, calibration, junction positions and fiber sensing extents require evidence.\item Drawn bends are schematic connectors, not qualified hydraulic paths. The heater pieces have overlapping and offset CAD geometry.\item A successful document build checks input structure and drawing closure. It does not establish experimental or modeling readiness.\end{itemize}',
        r'\vfill{\small Follow up: ' + link('issues-detail','open issues') + r'; ' + link('requirements','requirements and decisions') + r'; ' + link('sources-detail','source catalog') + r'.}\par',
        r'\clearpage\phantomsection\label{appendices}\pdfbookmark[0]{Appendices}{appendix-bookmark}',
        r'{\color{navy}\LARGE\bfseries Appendices}\par',
        r'Instructions, evidence and administrative detail. Return to the ' + link('overview','configuration overview') + r' at any time using the page header.\par',
        r'\tableofcontents']
    return '\n'.join(out)
