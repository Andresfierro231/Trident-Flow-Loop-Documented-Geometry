#!/usr/bin/env python3
"""Verify GEO-009 exposure records, exported evidence and preservation."""
import argparse,hashlib,json,zipfile
from pathlib import Path
from generate import read_workbook
ROOT=Path(__file__).resolve().parents[2]
E=ROOT/'support/evidence/2026-10-16_GEO-009_covered_top_corners'
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    old=read_workbook(E/'VCU_inputs_before_GEO-009.xlsx');new=read_workbook(ROOT/'VCU_inputs.xlsx');checks=[]
    def check(name,result):checks.append({'check':name,'passed':bool(result)})
    for s in old:
        if s not in ['Start','Sensors','Requirements','Sources','Insulation regions']:check('Unchanged '+s,new[s]==old[s])
    for id in ['INS-02','INS-06']:
        row=next(r for r in new['Insulation regions'] if r['Region ID']==id)
        check(id+' entirely insulated',row['Coverage']=='Insulated' and row['Material ID'] is None and row['Thickness mm'] is None and row['Evidence type']=='Reported' and 'GEO-009' in row['Evidence file / location'])
    check('Other coverage unchanged',all(r==b for r,b in zip(new['Insulation regions'],old['Insulation regions']) if r['Region ID'] not in ['INS-02','INS-06']))
    check('LF01 note only; no DAQ/coordinate invention',all({k:v for k,v in r.items() if k!='Notes'}=={k:v for k,v in b.items() if k!='Notes'} for r,b in zip(new['Sensors'],old['Sensors'])))
    lf=next(r for r in new['Sensors'] if r['Sensor ID']=='LF-01');check('LF01 local covered statement','covered locally' in lf['Notes'] and lf['DAQ channel'] is None and lf['From endpoint']=='C')
    check('Other sensor notes unchanged',all(r==b for r,b in zip(new['Sensors'],old['Sensors']) if r['Sensor ID']!='LF-01'))
    keys=['Selected choice','Decision scope / rationale','Reviewer / date','Effective configuration'];check('Approval fields unchanged',all(all(r[k]==b[k] for k in keys) for r,b in zip(new['Requirements'],old['Requirements'])))
    export=json.loads((ROOT/'support/generated/insulation_regions.json').read_text())
    # Locate the row list without relying on presentation order.
    rows=export.get('regions',export.get('insulation_regions',[]))
    for id in ['INS-02','INS-06']:
        row=next(r for r in rows if r.get('region_id',r.get('Region ID'))==id)
        check(id+' generated Insulated',row.get('coverage')=='Insulated')
    digest=hashlib.sha256((ROOT/'VCU_inputs.xlsx').read_bytes()).hexdigest()
    check('Resolved export matches workbook',json.loads((ROOT/'support/generated/resolved_inputs.json').read_text())==new)
    val=json.loads((ROOT/'support/generated/validation.json').read_text());check('Generator validity/hash',val['geometry_valid'] and val['input_sha256']==digest and not val['model_ready'])
    v=json.loads((E/'rev9_working_selection_v2.json').read_text());check('Model full insulated corners',set(v['insulation']['entire_insulated_upper_corners'])=={'upper_left_bend','upper_right_bend'} and v['insulation']['entire_bare_segments']==['cooler'])
    check('Model LF01 covered locally',next(s for s in v['sensors'] if s['source_id']=='LF-01')['local_insulation_coverage']=='covered')
    with zipfile.ZipFile(ROOT/'VCU_inputs.xlsx') as z:check('XLSX ZIP integrity',z.testzip() is None)
    out={'task':'GEO-009','status':'passed' if all(c['passed'] for c in checks) else 'failed','workbook_sha256':digest,'checks':checks,'limitations':'Reported installation clarification; no visual inspection, optical extent inference or historical simulation rerun.'};a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2)+'\n');print(out['status'],f"{sum(c['passed'] for c in checks)}/{len(checks)} checks")
    if out['status']!='passed':raise SystemExit(1)
if __name__=='__main__':main()
