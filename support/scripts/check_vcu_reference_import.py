#!/usr/bin/env python3
"""Check CFG-001 transcription, source identities and workbook preservation.

Requires PyYAML to read the owning model's unchanged property library.
Does not inspect images or claim physical validation.
"""
import argparse, csv, hashlib, json, math, re, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
import yaml
from generate import read_workbook
ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/'support/evidence/2026-10-16_CFG-001_vcu_references'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=ROOT/'VCU_inputs.xlsx')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();before=read_workbook(BUNDLE/'VCU_inputs_before_CFG-001.xlsx');after=read_workbook(args.input)
    checks=[]
    def check(name,result):
        checks.append({'check':name,'passed':bool(result)})
    for item in json.loads((BUNDLE/'origins.json').read_text()):
        check('Source hash: '+item['copy'],hashlib.sha256((BUNDLE/item['copy']).read_bytes()).hexdigest()==item['sha256'])
    for name in ['Sensors','Calibration','Thermal spans','Fluids','Phase requests','Review issues']:
        check('Preserved '+name,after[name]==before[name])
    for key in ['Your entry','Your evidence file / location','Entry evidence type','Reviewer / date']:
        for name in ['Form material','Form pipe','Form sensor']:
            check('Contributor cells '+name+' / '+key,[r[key] for r in after[name]]==[r[key] for r in before[name]])
    decision_keys=['Selected choice','Decision scope / rationale','Reviewer / date','Effective configuration']
    check('Approval fields unchanged',all([r[k] for k in decision_keys]==[b[k] for k in decision_keys] for r,b in zip(after['Requirements'],before['Requirements'])))
    check('Geometry inputs unchanged',all({k:v for k,v in r.items() if k!='Notes'}=={k:v for k,v in b.items() if k!='Notes'} for r,b in zip(after['Geometry'],before['Geometry'])))
    check('CAD main bores remain null',all(r['ID mm'] is None for r in after['Geometry']))
    for name in ['Form pipe','Form sensor']:
        check(name+' unchanged',after[name]==before[name])
    ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(BUNDLE/'VCU_inputs_before_CFG-001.xlsx') as a,zipfile.ZipFile(args.input) as b:
        check('ZIP integrity',b.testzip() is None)
        check('Original ZIP members retained',set(a.namelist())<=set(b.namelist()))
        check('Styles unchanged',a.read('xl/styles.xml')==b.read('xl/styles.xml'))
        check('Dropdowns unchanged',all([ET.tostring(e) for e in ET.fromstring(a.read(n)).findall('s:dataValidations',ns)]==[ET.tostring(e) for e in ET.fromstring(b.read(n)).findall('s:dataValidations',ns)] for n in a.namelist() if n.startswith('xl/worksheets/') and n.endswith('.xml')))
    dims=list(csv.DictReader((BUNDLE/'VCU_Rev9_Diameters.csv').open()))
    check('14 component records',len(after['CAD dimensions'])==len(dims)==14)
    check('CAD dimension values and local qualifications',all(r['Component']==d['item'] and r['Reference values']=='; '.join(f'{k}={v}' for k,v in d.items() if v and k in ['outer_diameter_mm','inner_diameter_mm','wall_thickness_mm','radial_width_mm','axial_thickness_mm']) and d['note'] in r['Evidence / limitations'] for r,d in zip(after['CAD dimensions'],dims)))
    lib=yaml.safe_load((BUNDLE/'vcu_candidate_materials_v3.yaml').read_text())
    values=[]
    for row,key in zip(after['Materials'][:3],lib['materials']):
        props=lib['materials'][key]['properties'];equations=row['Equation / table'].split('; ')
        for expression,(name,p) in zip(equations,props.items()):
            raw=expression.split(' = ')[1]
            got=[float(x) for x in re.findall(r'\(([-+\d.eE]+)\)',raw)] if p['model']=='polynomial' else [float(raw)]
            expected=p['coefficients'] if p['model']=='polynomial' else [p['value']]
            check(row['Material ID']+' '+name+' exact coefficients',got==expected)
            low,high=p['valid_temperature_K'];check(row['Material ID']+' '+name+' domain',f'{low:g}-{high:g} K' in row['Valid domain'])
            for temp in [low,293.15,high]:
                value=sum(c*temp**i for i,c in enumerate(got))
                check(row['Material ID']+' '+name+f' positive at {temp} K',math.isfinite(value) and value>0)
                values.append({'material':row['Material ID'],'property':name,'temperature_K':temp,'value':value,'units':p['units']})
        check(row['Material ID']+' provisional qualification','calibration_eligible=false' in row['Rationale'] and row['Status']=='Reported')
    summary={'task':'CFG-001','status':'passed' if all(c['passed'] for c in checks) else 'failed','input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),'checks':checks,'property_transcription_values':values,'limitations':'Numerical transcription and file checks only; no product/source-fit/installation validation or visual review.'}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(summary,indent=2)+'\n')
    print(f"{summary['status']}: {sum(c['passed'] for c in checks)}/{len(checks)} checks; 9 property functions; 27 scalar check values.")
    if summary['status']!='passed':raise SystemExit(1)
if __name__=='__main__':main()
