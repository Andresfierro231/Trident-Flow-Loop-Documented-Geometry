#!/usr/bin/env python3
"""Generate SVG, standalone TikZ/LaTeX and qualified coordinates from VCU_inputs.xlsx.

Python 3.9+; standard library only. Never reads cached formula values as inputs.
"""
import argparse
import hashlib
import html
import json
import math
import posixpath
import sys
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from control_content import build_report, markdown_register, validate as validate_control
from insulation import resolve_regions, export_regions, insulation_diagram
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
REL = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'


def read_workbook(filename):
    """Read the row-5 headers and row-6+ records, including appended rows."""
    with zipfile.ZipFile(filename) as z:
        strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            strings = [''.join(t.itertext()) for t in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        rels = {r.attrib['Id']: r.attrib['Target'] for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        result = {}
        for sh in ET.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet', NS):
            target = rels[sh.attrib[REL]]
            target = target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/' + target)
            rows = {}
            for row in ET.fromstring(z.read(target)).findall('s:sheetData/s:row', NS):
                cells = {}
                for cell in row.findall('s:c', NS):
                    address = cell.attrib['r']
                    col = ''.join(c for c in address if c.isalpha())
                    idx = 0
                    for c in col:
                        idx = idx * 26 + ord(c) - 64
                    if cell.find('s:f', NS) is not None:
                        raise ValueError(f'{sh.attrib["name"]}!{address}: use a measured/input value, not a formula.')
                    typ = cell.attrib.get('t')
                    val = cell.find('s:v', NS)
                    if typ == 'inlineStr':
                        value = ''.join(cell.find('s:is', NS).itertext())
                    elif val is None or val.text is None:
                        value = None
                    elif typ == 's':
                        value = strings[int(val.text)]
                    elif typ in ('str', 'e', 'b'):
                        value = val.text
                    else:
                        value = float(val.text)
                    cells[idx - 1] = value
                rows[int(row.attrib['r'])] = cells
            header = rows.get(5, {})
            if not header:
                raise ValueError(f'{sh.attrib["name"]}: missing headers on row 5.')
            result[sh.attrib['name']] = [{header[i]: cells.get(i) for i in header}
                for n, cells in sorted(rows.items()) if n > 5 and cells.get(0) not in (None, '')]
        return result


def number(value, label, optional=False):
    if value in (None, ''):
        if optional:
            return None
        raise ValueError(f'{label}: a number is required.')
    try:
        n = float(value)
    except (ValueError, TypeError):
        raise ValueError(f'{label}: enter a number without unit text.') from None
    if not math.isfinite(n):
        raise ValueError(f'{label}: number must be finite.')
    return n


def unique(records, key, title):
    keys = [r[key] for r in records]
    if len(set(keys)) != len(keys):
        raise ValueError(f'{title}: duplicate {key}.')


def solve(tables):
    required = ['Start', 'Geometry', 'Sensors', 'Calibration', 'Thermal spans', 'Fluids', 'Materials', 'Model choices']
    for name in required:
        if name not in tables:
            raise ValueError(f'Missing worksheet: {name}')
    unique(tables['Start'], 'Field', 'Start')
    settings = {r['Field']: r['Value'] for r in tables['Start']}
    if settings.get('Facility') != 'VCU' or any(r.get('Facility') != 'VCU' for r in tables['Fluids']):
        raise ValueError('This prototype accepts VCU only. Keep ACU in a separate configuration.')
    unique(tables['Geometry'], 'Segment', 'Geometry')
    unique(tables['Sensors'], 'Sensor ID', 'Sensors')
    unique(tables['Calibration'], 'Sensor ID', 'Calibration')
    notes = []
    tolerance = number(settings.get('Closure tolerance mm'), 'Closure tolerance')
    if tolerance <= 0:
        raise ValueError('Closure tolerance must be positive.')
    points = {str(settings['Origin']): (0., 0., 0.)}
    current = str(settings['Origin'])
    segments = {}
    first = current
    for i, row in enumerate(tables['Geometry']):
        name = row['Segment']
        if row['Start'] != current:
            raise ValueError(f'{name}: Start must follow previous End ({current}).')
        a = points[current]
        if row['Kind'] == 'straight':
            length = number(row['Length mm'], name + ' length')
            if length <= 0:
                raise ValueError(f'{name}: length must be positive.')
            phi = number(row['Phi deg'], name + ' phi')
            if not 0 <= phi < 360:
                raise ValueError(f'{name}: phi must be in [0, 360).')
            angle = math.radians(phi)
            dx, dy = length * math.sin(angle), length * math.cos(angle)
            if row.get('Bend dx mm') is not None or row.get('Bend dy mm') is not None:
                raise ValueError(f'{name}: leave bend offsets blank on a straight segment.')
        elif row['Kind'] == 'bend':
            dx = number(row['Bend dx mm'], name + ' bend dx')
            dy = number(row['Bend dy mm'], name + ' bend dy')
            if math.hypot(dx, dy) <= 0:
                raise ValueError(f'{name}: bend endpoints must differ.')
            length = None
            if row.get('Length mm') is not None or row.get('Phi deg') is not None:
                raise ValueError(f'{name}: use offsets for a bend; leave Length and Phi blank.')
        else:
            raise ValueError(f'{name}: Kind must be straight or bend.')
        for key in ('ID mm', 'OD mm', 'Insulation mm'):
            v = number(row.get(key), name + ' ' + key, True)
            if v is not None and (v < 0 or (key != 'Insulation mm' and v == 0)):
                raise ValueError(f'{name}: invalid {key}.')
        if row.get('ID mm') is not None and row.get('OD mm') is not None and float(row['ID mm']) >= float(row['OD mm']):
            raise ValueError(f'{name}: ID must be less than OD.')
        b = (a[0] + dx, a[1] + dy, 0.)
        end = row['End']
        if end in points and not (end == first and i == len(tables['Geometry']) - 1):
            raise ValueError(f'{name}: repeated endpoint {end}.')
        segments[name] = dict(row, start_xyz_mm=a, end_xyz_mm=b, axial_length_mm=length)
        if end != first:
            points[end] = b
        current = end
    if current != first:
        raise ValueError('Final segment must return to the origin endpoint label.')
    gap = math.dist(b, points[first])
    if gap > tolerance:
        raise ValueError(f'Loop does not close: {gap:.3f} mm gap exceeds {tolerance:g} mm. Reconcile lengths, angles and bend offsets; no automatic repair.')
    coords = []
    for row in tables['Sensors']:
        sid = row['Sensor ID']
        if row['Type'] not in ('STC', 'PTC', 'LF'):
            raise ValueError(f'{sid}: Type must be STC, PTC or LF.')
        seg = segments.get(row['Segment'])
        if seg is None or seg['Kind'] != 'straight':
            raise ValueError(f'{sid}: sensor stationing currently requires a named straight segment.')
        d = number(row['Distance mm'], sid + ' distance')
        if row['From endpoint'] not in (seg['Start'], seg['End']):
            raise ValueError(f'{sid}: endpoint does not belong to {row["Segment"]}.')
        length = seg['axial_length_mm']
        if not 0 <= d <= length:
            raise ValueError(f'{sid}: distance {d:g} mm is outside segment length {length:g} mm.')
        station = d if row['From endpoint'] == seg['Start'] else length - d
        a, b = seg['start_xyz_mm'], seg['end_xyz_mm']
        t = tuple((b[k] - a[k]) / length for k in range(3))
        axis = tuple(a[k] + station * t[k] for k in range(3))
        # e0 = up projected onto cross-sectional plane; vertical fallback +x.
        up = (-t[1] * t[0], 1 - t[1] ** 2, 0.)
        mag = math.sqrt(sum(v * v for v in up))
        e0 = tuple(v / mag for v in up) if mag > 1e-8 else (1., 0., 0.)
        e90 = (t[1]*e0[2]-t[2]*e0[1], t[2]*e0[0]-t[0]*e0[2], t[0]*e0[1]-t[1]*e0[0])
        angle = number(row['Circumference deg'], sid + ' circumference', True)
        radius = number(row['Radius mm'], sid + ' radius', True)
        if angle is not None and not 0 <= angle < 360:
            raise ValueError(f'{sid}: circumference angle must be in [0, 360).')
        if radius is not None and radius < 0:
            raise ValueError(f'{sid}: radius cannot be negative.')
        xyz = None
        if angle is not None and radius is not None:
            ang = math.radians(angle)
            xyz = tuple(axis[k] + radius * (math.cos(ang)*e0[k] + math.sin(ang)*e90[k]) for k in range(3))
        coords.append(dict(row, station_from_start_mm=station, axis_xyz_mm=axis,
            sensor_xyz_mm=xyz, zero_direction=e0, positive_90_direction=e90,
            zero_reference='Projected upward vertical' if mag > 1e-8 else 'Drawing +x (vertical pipe)',
            one_d_mapping=next((r['1-D mapping'] for r in tables['Calibration'] if r['Sensor ID']==sid),None),
            cfd_mapping=next((r['CFD mapping'] for r in tables['Calibration'] if r['Sensor ID']==sid),None)))
    spans=[]
    for row in tables['Thermal spans']:
        seg=segments.get(row['Segment'])
        if seg is None or seg['Kind']!='straight':
            raise ValueError(f'{row["Feature"]}: thermal span requires a straight segment.')
        if row['From endpoint'] not in (seg['Start'],seg['End']):
            raise ValueError(f'{row["Feature"]}: invalid endpoint.')
        if row['Role'] not in ('Jacket envelope','Active heating','Active cooling'):
            raise ValueError(f'{row["Feature"]}: unsupported thermal role.')
        d0=number(row['Start mm'],row['Feature']+' start',True)
        d1=number(row['End mm'],row['Feature']+' end',True)
        if d0 is None and d1 is None:
            notes.append(f'{row["Feature"]}: boundaries unknown; not drawn.')
            continue
        if d0 is None or d1 is None or not 0<=d0<d1<=seg['axial_length_mm']:
            raise ValueError(f'{row["Feature"]}: start/end must define a positive span inside the segment.')
        length=seg['axial_length_mm']
        ss=[d0,d1] if row['From endpoint']==seg['Start'] else [length-d0,length-d1]
        aa,bb=seg['start_xyz_mm'],seg['end_xyz_mm']
        ends=[tuple(aa[k]+q/length*(bb[k]-aa[k]) for k in range(3)) for q in ss]
        spans.append(dict(row,ends_xyz_mm=ends))
    for r in tables['Fluids']:
        lo=number(r['Minimum C'],r['Fluid ID']+' minimum',True)
        hi=number(r['Maximum C'],r['Fluid ID']+' maximum',True)
        if lo is not None and hi is not None and lo>=hi:
            raise ValueError(f'{r["Fluid ID"]}: temperature range is reversed or empty.')
    notes += ['CAD references are not verified sensing junctions or acquisition-channel names.',
              'Bends are schematic connectors. No continuous hydraulic length is inferred.',
              'JTC-A/B, branch pipes, tank and coolant plumbing are retained as outstanding scope, not drawn.',
              'Model input draft only: missing bore, property selections, calibrations and approved boundary conditions.']
    insulation = resolve_regions(tables, segments, notes)
    return dict(settings=settings,segments=segments,points=points,sensors=coords,thermal_spans=spans,insulation_regions=insulation,
                closure_gap_mm=gap,model_ready=False,notes=notes)


class Drawing:
    """A small shared vector scene emitted to SVG and TikZ without external assets."""
    def __init__(self, title, subtitle, width=1400, height=1500):
        self.width,self.height=width,height
        self.items=[]
        self.text(70,65,title,30,bold=True)
        self.text(70,102,subtitle,17,color='#576976')
        self.line((70,125),(width-70,125),'#CFD9DF',2)
    def line(self,a,b,color='#263D4B',width=2,dash=False,opacity=1):
        self.items.append(('line',a,b,color,width,dash,opacity))
    def text(self,x,y,value,size=18,color='#263D4B',anchor='start',bold=False):
        self.items.append(('text',x,y,str(value),size,color,anchor,bold))
    def circle(self,x,y,r=7,color='#263D4B'):
        self.items.append(('circle',x,y,r,color))
    def svg(self):
        out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}"><rect width="100%" height="100%" fill="white"/>']
        for item in self.items:
            if item[0]=='line':
                _,a,b,c,w,dash,opacity=item
                out.append(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" stroke="{c}" stroke-width="{w}"'+(' stroke-dasharray="6 5"' if dash else '')+(f' stroke-opacity="{opacity}"' if opacity!=1 else '')+'/>')
            elif item[0]=='circle':
                _,x,y,r,c=item
                out.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{r}" fill="white" stroke="{c}" stroke-width="2"/>')
            else:
                _,x,y,v,s,c,a,b=item
                out.append(f'<text x="{x:.3f}" y="{y:.3f}" font-family="Arial, sans-serif" font-size="{s}" fill="{c}" text-anchor="{a}"'+(' font-weight="bold"' if b else '')+'>'+html.escape(v)+'</text>')
        return '\n'.join(out+['</svg>'])
    def tikz(self):
        out=[r'\begin{tikzpicture}[x=0.01cm,y=-0.01cm]',f'\\path[use as bounding box] (0,0) rectangle ({self.width},{self.height});']
        colors={i[3] if i[0]=='line' else i[4] if i[0]=='circle' else i[5] for i in self.items}
        out.extend(f'\\definecolor{{c{c[1:]}}}{{HTML}}{{{c[1:]}}}' for c in sorted(colors))
        for i in self.items:
            if i[0]=='line':
                _,a,b,c,w,dash,opacity=i
                out.append(f'\\draw[draw=c{c[1:]},line width={w*.26:.3f}pt'+(',dashed' if dash else '')+(f',draw opacity={opacity}' if opacity!=1 else '')+f'] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});')
            elif i[0]=='circle':
                _,x,y,r,c=i
                out.append(f'\\draw[fill=white,draw=c{c[1:]},line width=0.5pt] ({x:.3f},{y:.3f}) circle ({r});')
            else:
                _,x,y,v,s,c,a,b=i
                anchor={'start':'base west','middle':'base','end':'base east'}[a]
                out.append(f'\\node[anchor={anchor},inner sep=0pt,text=c{c[1:]},font=\\sffamily\\fontsize{{{s*.28:.2f}}}{{{s*.34:.2f}}}\\selectfont'+('\\bfseries' if b else '')+f'] at ({x:.3f},{y:.3f}) {{{tex(v)}}};')
        return '\n'.join(out+[r'\end{tikzpicture}'])


def tex(value):
    if value is None or value=='':
        return r'\textit{Unknown}'
    if isinstance(value,float):
        value=f'{value:.3f}'
    trans={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
    return ''.join(trans.get(c,c) for c in str(value))


def diagrams(model):
    segments=model['segments']; points=model['points']
    xmin=min(p[0] for p in points.values()); xmax=max(p[0] for p in points.values())
    ymin=min(p[1] for p in points.values()); ymax=max(p[1] for p in points.values())
    scale=min(660/(xmax-xmin),760/(ymax-ymin))
    def screen(p): return (370+(p[0]-xmin)*scale,390+(ymax-p[1])*scale)
    figs=[]
    for sensors in (False,True):
        fig=Drawing('VCU / '+('SENSOR LOCATIONS' if sensors else 'GEOMETRY AND THERMAL COVERAGE'),
                    model['settings']['Configuration ID']+' | generated from the editable workbook')
        for seg in segments.values():
            fig.line(screen(seg['start_xyz_mm']),screen(seg['end_xyz_mm']),width=5,dash=seg['Kind']=='bend')
        for span in model['thermal_spans']:
            col={'Jacket envelope':'#5D9DC3','Active heating':'#C44536','Active cooling':'#007A8A'}[span['Role']]
            fig.line(*[screen(p) for p in span['ends_xyz_mm']],color=col,width=14)
        for tag,p in points.items():
            x,y=screen(p); fig.text(x-15,y-14,tag,20,bold=True)
        fig.text(700,770,'VCU',54,'#A3B0B9','middle')
        if sensors:
            groups={name:[] for name in ('upcomer','cooler','downcomer','heater')}
            for s in model['sensors']:
                groups.setdefault(s['Segment'],[]).append(s)
            for leg,ss in groups.items():
                ss.sort(key=lambda s:s['axis_xyz_mm'][1] if leg in ('upcomer','downcomer') else s['axis_xyz_mm'][0],reverse=leg in ('upcomer','downcomer'))
                for j,s in enumerate(ss):
                    xy=screen(s['axis_xyz_mm']); col={'STC':'#263D4B','PTC':'#388452','LF':'#286AA6'}[s['Type']]
                    fig.circle(*xy,color=col)
                    if leg in ('upcomer','downcomer'):
                        lx=75 if leg=='upcomer' else 1110
                        ly=470+j*105
                        elbow=(320 if leg=='upcomer' else 1065,ly)
                        fig.line(xy,elbow,'#8B9AA5',1)
                        fig.line(elbow,(lx+190 if leg=='upcomer' else lx-8,ly),'#8B9AA5',1)
                        anchor='start'
                    else:
                        lx=150+j*(1100/max(len(ss)-1,1))
                        ly=205 if leg=='cooler' else 1245
                        fig.line(xy,(lx,ly+55 if leg=='cooler' else ly-25),'#8B9AA5',1)
                        anchor='middle'
                    fig.text(lx,ly,s['Sensor ID'],20,col,anchor,True)
                    fig.text(lx,ly+25,f'{s["From endpoint"]} + {s["Distance mm"]:.1f} mm',16,anchor=anchor)
                    if s['Circumference deg'] is not None:
                        fig.text(lx,ly+47,f'angle {s["Circumference deg"]:g} deg',15,col,anchor)
            fig.text(70,1370,'Markers show axial stations; circumferential positions are recorded separately.',17)
            fig.text(70,1400,'STC = wall reference | PTC = penetrating TC reference | LF = fiber reference',17)
        else:
            placements={'upcomer':(80,700),'cooler':(700,265),'downcomer':(1100,800),'heater':(700,1250)}
            for name,(x,y) in placements.items():
                if name not in segments: continue
                seg=segments[name]; anchor='middle' if name in ('cooler','heater') else 'start'
                fig.text(x,y,name.upper(),22,anchor=anchor,bold=True)
                fig.text(x,y+30,f'{seg["axial_length_mm"]:.3f} mm',20,anchor=anchor)
                fig.text(x,y+57,f'phi = {seg["Phi deg"]:.3f} deg',17,anchor=anchor)
            fig.text(70,180,'Blue: jacket envelope. Red appears only for entered active heater spans.',18)
            fig.text(70,1370,'Lengths are axis-end spans. Heater span is projected; it is not an exact joined path.',17)
            fig.text(70,1400,'Dashed corners are schematic endpoint connectors, not hydraulic arc geometry.',17)
        fig.text(70,1445,'VCU Rev9 CAD candidate | installed geometry and sensing locations require confirmation',16,'#576976')
        figs.append(fig)
    guide=Drawing('SENSOR POSITION / ANGLE CONVENTION','Circumferential angle is separate from segment inclination.',1400,950)
    cx,cy,r=320,430,180
    guide.circle(cx,cy,r)
    guide.line((cx,cy),(cx,cy-r),'#263D4B',2)
    guide.line((cx,cy),(cx+r,cy),'#263D4B',2)
    guide.text(cx,cy-r-20,'0 deg: top / e0',21,anchor='middle')
    guide.text(cx+r+20,cy,'90 deg / e90',21)
    guide.text(cx,cy+r+40,'180 deg',21,anchor='middle')
    guide.text(cx-r-20,cy,'270 deg',21,anchor='end')
    guide.circle(cx+r*math.sin(math.pi/4),cy-r*math.cos(math.pi/4),9,'#286AA6')
    guide.text(650,280,'HOW TO RECORD A SENSOR',24,bold=True)
    for j,t in enumerate(['1. Pick a segment and one of its endpoints.','2. Measure distance along that segment.','3. Enter angle around the pipe, if known.','4. Enter radius from the axis for a 3-D point.','5. Identify mount, contact or sensing junction.']):
        guide.text(650,330+j*45,t,20)
    guide.text(70,740,'Positive rotation is right-hand about the directed segment (+s). e90 = tangent x e0.',20)
    guide.text(70,780,'For vertical pipes, e0 is drawing +x. For other pipes, e0 is projected upward vertical.',20)
    guide.text(70,820,'The 45-degree dot is illustrative. No VCU sensor angle has been assumed.',20)
    guide.text(70,860,'A blank angle or radius leaves the exported 3-D sensor point unresolved.',20)
    figs.append(guide)
    # Optional angle cards populated only from actual entered angles.
    angled=[s for s in model['sensors'] if s['Circumference deg'] is not None]
    for start in range(0,len(angled),6):
        card=Drawing('ENTERED SENSOR ANGLES','Local cross sections | the same e0/e90 convention applies to every card.',1400,1100)
        for j,s in enumerate(angled[start:start+6]):
            x,y=270+(j%3)*430,360+(j//3)*440
            card.circle(x,y,100);card.line((x,y),(x,y-100),'#98A7B1')
            a=math.radians(s['Circumference deg']);card.circle(x+100*math.sin(a),y-100*math.cos(a),8,'#286AA6')
            card.text(x,y-150,s['Sensor ID'],24,anchor='middle',bold=True)
            card.text(x,y+145,f'{s["Circumference deg"]:g} deg | {s["From endpoint"]}+{s["Distance mm"]:.1f} mm',18,anchor='middle')
            card.text(x,y+178,'Zero: '+s['zero_reference'],15,anchor='middle')
        figs.append(card)
    return figs


def latex_table(rows, headers, keys, widths):
    spec=''.join(r'>{\raggedright\arraybackslash}' + f'p{{{w}\\textwidth}}' for w in widths)
    out=[r'\small\setlength{\tabcolsep}{4pt}',r'\begin{longtable}{'+spec+'}',r'\toprule',
         ' & '.join(r'\textbf{'+tex(h)+'}' for h in headers)+r' \\\midrule\endhead']
    for row in rows:
        out.append(' & '.join(tex(row.get(k)) for k in keys)+r' \\[3pt]')
    return '\n'.join(out+[r'\bottomrule\end{longtable}\normalsize'])


def report(tables, model, figs, digest):
    return build_report(tables, model, figs, digest, tex, latex_table, insulation_diagram(model, Drawing))


def generate(filename, outdir):
    tables=read_workbook(filename)
    validate_control(tables)
    model=solve(tables)
    initial=ROOT/'reference/initial_tables.json'
    if initial.exists():
        seed={d['name']: {r[0]:dict(zip(d['headers'],r)) for r in d['rows']} for d in json.loads(initial.read_text())}
        for name in ('Geometry','Sensors','Thermal spans'):
            for row in tables[name]:
                key=next(iter(row)); old=seed[name].get(row[key])
                if old and row.get('Status')=='CAD-derived' and any(row.get(k)!=old.get(k) for k in row if k!='Notes'):
                    model['notes'].append(f'{name} / {row[key]}: edited input still marked CAD-derived; update its evidence/status.')
    digest=hashlib.sha256(Path(filename).read_bytes()).hexdigest()
    model['input_sha256']=digest
    figs=diagrams(model)
    out=Path(outdir);out.mkdir(parents=True,exist_ok=True)
    names=['geometry','sensors','angle_convention']+[f'sensor_angles_{i+1}' for i in range(max(0,len(figs)-3))]
    for name,fig in zip(names,figs):
        (out/(name+'.svg')).write_text(fig.svg())
    (out/'insulation.svg').write_text(insulation_diagram(model, Drawing).svg())
    (out/'insulation_regions.json').write_text(json.dumps(export_regions(tables,model,digest),indent=2,ensure_ascii=False))
    for old in out.glob('sensor_angles_*.svg'):
        if old.stem not in names: old.unlink()
    (out/'VCU_control_package.tex').write_text(report(tables,model,figs,digest))
    (out/'requirements_and_evidence.md').write_text(markdown_register(tables))
    (out/'resolved_inputs.json').write_text(json.dumps(tables,indent=2,ensure_ascii=False))
    (out/'geometry_and_sensors.json').write_text(json.dumps(model,indent=2,ensure_ascii=False))
    (out/'validation.json').write_text(json.dumps(dict(input_sha256=digest,geometry_valid=True,closure_gap_mm=model['closure_gap_mm'],model_ready=False,notes=model['notes']),indent=2))
    return model


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=ROOT.parent/'VCU_inputs.xlsx')
    parser.add_argument('--out',type=Path,default=ROOT/'generated')
    args=parser.parse_args()
    try:
        model=generate(args.input,args.out)
    except (ValueError,KeyError,zipfile.BadZipFile) as error:
        # Never let an earlier valid output silently appear to match invalid edits.
        args.out.mkdir(parents=True,exist_ok=True)
        (args.out/'validation.json').write_text(json.dumps({'geometry_valid':False,'error':str(error),'previous_outputs':'May be stale; not regenerated.'},indent=2))
        parser.exit(2,f'Input error: {error}\nPrevious figures, if present, are stale.\n')
    print(f'Generated {len(model["sensors"])} main-loop sensor references; closure gap {model["closure_gap_mm"]:.6g} mm.')
    print('Draft outputs: '+str(args.out))


if __name__=='__main__':
    main()
