#!/usr/bin/env python3
"""Reproduce GEO-009's reported whole-corner and local LF-01 exposure correction."""
import argparse,hashlib,json,os,zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
from generate import read_workbook,NS,REL
from import_vcu_references import write_row,tag
ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/'support/evidence/2026-10-16_GEO-009_covered_top_corners'
EVIDENCE='support/evidence/2026-10-16_GEO-009_covered_top_corners/USER_CLARIFICATION.md'
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    source=BUNDLE/'VCU_inputs_before_GEO-009.xlsx'
    if hashlib.sha256(source.read_bytes()).hexdigest()!=json.loads((BUNDLE/'input_identity.json').read_text())['sha256']:raise SystemExit('Baseline identity differs')
    original=read_workbook(source)
    with zipfile.ZipFile(source) as z:infos=z.infolist();data={i.filename:z.read(i.filename) for i in infos}
    rels={r.get('Id'):r.get('Target') for r in ET.fromstring(data['xl/_rels/workbook.xml.rels'])}
    paths={s.get('name'):(rels[s.get(REL)].lstrip('/') if rels[s.get(REL)].startswith('/') else 'xl/'+rels[s.get(REL)]) for s in ET.fromstring(data['xl/workbook.xml']).findall('s:sheets/s:sheet',NS)}
    sheets={n:ET.fromstring(data[path]) for n,path in paths.items()};modified=set()
    def update(name,key,match,fields):
        i=next(i for i,r in enumerate(original[name]) if r[key]==match)
        write_row(sheets[name],i+6,list(original[name][0]),fields);modified.add(name)
    for id in ['INS-02','INS-06']:
        update('Insulation regions','Region ID',id,{'Coverage':'Insulated','Material ID':None,'Thickness mm':None,'Evidence type':'Reported','Evidence file / location':EVIDENCE+' / entire covered top-left C-D and top-right E-F corners','Notes':'Entire corner insulated per corrected Andres Fierro statement 2026-10-16. Installed product and thickness unmeasured; model fiberglass estimate remains provisional.'})
    lf=next(r for r in original['Sensors'] if r['Sensor ID']=='LF-01')
    update('Sensors','Sensor ID','LF-01',{'Notes':lf['Notes']+' User report 2026-10-16 (VTOP): LF-01 is covered locally. CAD mount reference lies on upcomer 61.113919 mm below C; covered extent, optical extent and DAQ mapping remain unknown.'})
    update('Start','Field','Configuration ID',{'Value':'VCU-REV9-DRAFT-005'})
    update('Start','Field','Change summary',{'Value':'GEO-009: entire covered top-left C-D and top-right E-F corners Insulated; LF-01 locally covered, per Andres Fierro 2026-10-16. Model regional insulation v6 and Rev9 working selection v2 agree. Other coverage, numerical geometry and historical evidence unchanged.'})
    update('Requirements','Field ID','C15',{'Current evidence':'User 2026-10-16: entire C-D/E-F upper corners insulated; LF-01 locally covered. Top D-E remains bare. Remaining vertical cutbacks and LF-01 coverage extent unknown.','Evidence type':'Reported','Evidence source':'VSEL; VTOP','Evidence locator':'VTOP direct user clarification; Insulation regions INS-02/06; Sensors LF-01; regional model v6','Review state':'Needs review'})
    headers=list(original['Sources'][0]);row={'Source ID':'VTOP','File / record':EVIDENCE,'Revision / context':'Direct user clarification 2026-10-16; model regional v6 / Rev9 working v2','Locator guide':'Whole C-D / E-F corners; LF-01 local exposure','Qualification':'Reported by user; no independent survey, optical extent, covered extent or historical run dates supplied.'}
    write_row(sheets['Sources'],len(original['Sources'])+6,headers,row);modified.add('Sources')
    for name in modified:
        dim=sheets[name].find(tag('dimension'))
        if dim is not None and name=='Sources':dim.set('ref','A1:E'+str(len(original['Sources'])+6))
        data[paths[name]]=ET.tostring(sheets[name],encoding='utf-8',xml_declaration=True)
    args.output.parent.mkdir(parents=True,exist_ok=True);tmp=args.output.with_suffix('.tmp.xlsx')
    with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as z:
        for i in infos:z.writestr(i,data[i.filename])
    os.replace(tmp,args.output)
    print('DRAFT-005: both whole upper corners Insulated; LF-01 explicitly covered locally.')
if __name__=='__main__':main()
