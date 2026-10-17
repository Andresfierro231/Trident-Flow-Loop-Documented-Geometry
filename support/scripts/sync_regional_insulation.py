#!/usr/bin/env python3
"""Migrate/check GEO-010 reported insulation regions using the Python standard library."""
import argparse,hashlib,json,zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
from generate import read_workbook,NS,REL
from import_vcu_references import write_row,tag
ROOT=Path(__file__).resolve().parents[2]
B=ROOT/'support/evidence/2026-10-16_GEO-010_regional_insulation_sync'
SOURCE='support/evidence/2026-10-16_GEO-010_regional_insulation_sync/'
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');p.add_argument('--summary',type=Path);a=p.parse_args()
 assignments=json.loads((B/'region_assignments.json').read_text());baseline=B/'VCU_inputs_before_GEO-010.xlsx';old=read_workbook(baseline)
 if hashlib.sha256(baseline.read_bytes()).hexdigest()!=json.loads((B/'input_identity.json').read_text())['sha256']:raise SystemExit('Baseline identity differs')
 if not a.check:
  if a.output is None:p.error('--output required')
  with zipfile.ZipFile(baseline) as z:infos=z.infolist();data={i.filename:z.read(i.filename) for i in infos}
  rels={r.get('Id'):r.get('Target') for r in ET.fromstring(data['xl/_rels/workbook.xml.rels'])};paths={s.get('name'):(rels[s.get(REL)].lstrip('/') if rels[s.get(REL)].startswith('/') else 'xl/'+rels[s.get(REL)]) for s in ET.fromstring(data['xl/workbook.xml']).findall('s:sheets/s:sheet',NS)};sheets={n:ET.fromstring(data[path]) for n,path in paths.items()};modified=set()
  def update(name,key,match,fields):
   i=next(i for i,r in enumerate(old[name]) if r[key]==match);write_row(sheets[name],i+6,list(old[name][0]),fields);modified.add(name)
  for r in assignments:update('Insulation regions','Region ID',r['region_id'],{'Coverage':r['coverage'],'Material ID':r['material_id'],'Thickness mm':r['thickness_mm'],'Evidence type':'Reported','Evidence file / location':SOURCE+'insulation.yaml / regions; VREG; VCU-007/008 and GEO-009','Notes':r['basis']})
  update('Start','Field','Configuration ID',{'Value':'VCU-REV9-DRAFT-006'})
  update('Start','Field','Change summary',{'Value':'GEO-010: all ten insulation regions synchronized: six ordinary-pipe fiberglass regions about 50.8 mm; heater ceramic strip only about 6.35 mm; three top D-E partitions Bare. Coverage Reported; thicknesses approximate estimates. LF-01 remains covered.'})
  for id,text in [('C13','Ordinary main piping (upcomer/downcomer and four corners): fiberglass MAIN-INS; heater: calcium-aluminum-silicate HEATER-INS strip only, no additional fiberglass.'),('C14','Reported estimates: ordinary insulated regions 50.8 mm (2 in); heater strip 6.35 mm (1/4 in). Not installed thickness measurements.'),('C15','Reported coverage known for all ten regions: upcomer/downcomer, four corners and heater insulated; pre-cooler/jacket/post-cooler D-E bare. LF-01 covered. Exact local contacts and transitions remain open.')]:update('Requirements','Field ID',id,{'Current evidence':text,'Evidence type':'Reported','Evidence source':'VREG; VTOP','Evidence locator':'VREG regional YAML and ADR-0025/0026; VTOP corner/LF-01 correction; user reaffirmation 2026-10-16','Review state':'Needs review'})
  for question,ref in [('Insulation product and layer order','Reported fiberglass MAIN-INS on upcomer; heater uses distinct ceramic strip only.'),('Thickness of each layer (mm)','Upcomer: reported approximate 50.8 mm fiberglass; estimate, not measurement.'),('Coverage, gaps and condition','Upcomer insulated per documented assignment and user reaffirmation; exact gaps/condition unmeasured.')]:update('Form pipe','What to record',question,{'Reference only':ref,'Reference basis':'Reported','Reference source':'VREG; user reaffirmation 2026-10-16'})
  for mid,note in [('MAIN-INS','Assigned to upcomer, downcomer and all four corners; approximately 50.8 mm fiberglass.'),('HEATER-INS','Assigned to straight heater only; approximately 6.35 mm ceramic strip; no extra fiberglass.')]:
   row=next(r for r in old['Materials'] if r['Material ID']==mid);update('Materials','Material ID',mid,{'Rationale':row['Rationale']+' '+note+' Reported assignment; exact product and thickness remain unverified.','Source':row['Source']+'; VREG'})
  fields={'Source ID':'VREG','File / record':SOURCE+'README.md','Revision / context':'GEO-010 2026-10-16; regional v7 / working v3','Locator guide':'region_assignments.json; insulation.yaml; ADR-0025/0026; USER_CONFIRMATION.md','Qualification':'Reported coverage and approximate thickness estimates; product/fit validation, installed surveys and historical applicability remain separate.'}
  write_row(sheets['Sources'],len(old['Sources'])+6,list(old['Sources'][0]),fields);modified.add('Sources')
  for name in modified:
   dim=sheets[name].find(tag('dimension'))
   if name=='Sources' and dim is not None:dim.set('ref','A1:E'+str(len(old['Sources'])+6))
   data[paths[name]]=ET.tostring(sheets[name],encoding='utf-8',xml_declaration=True)
  tmp=a.output.with_suffix('.tmp.xlsx');a.output.parent.mkdir(parents=True,exist_ok=True)
  with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as z:
   for i in infos:z.writestr(i,data[i.filename])
  tmp.replace(a.output);print('DRAFT-006: 7 insulated / 3 bare regions; two insulation assignments.');return
 new=read_workbook(ROOT/'VCU_inputs.xlsx');checks=[]
 def check(n,ok):checks.append({'check':n,'passed':bool(ok)})
 for r in assignments:
  row=next(x for x in new['Insulation regions'] if x['Region ID']==r['region_id']);check(r['region_id'],row['Coverage']==r['coverage'] and row['Material ID']==r['material_id'] and row['Thickness mm']==r['thickness_mm'] and row['Evidence type']=='Reported')
 for name in ['Geometry','Sensors','Calibration','Thermal spans','Fluids','Model choices','Form sensor','Form material','Phase requests','Review issues','CAD dimensions']:check('Preserved '+name,new[name]==old[name])
 for k in ['Your entry','Your evidence file / location','Entry evidence type','Reviewer / date']:check('Form contributor '+k,[r[k] for r in new['Form pipe']]==[r[k] for r in old['Form pipe']])
 keys=['Selected choice','Decision scope / rationale','Reviewer / date','Effective configuration'];check('Approvals preserved',all(all(r[k]==b[k] for k in keys) for r,b in zip(new['Requirements'],old['Requirements'])))
 check('Material functions preserved',all(all(r[k]==b[k] for k in ['Equation / table','Input units','Output units','Valid domain']) for r,b in zip(new['Materials'],old['Materials'])))
 v=json.loads((ROOT/'support/generated/validation.json').read_text());check('Generated validity/hash',v['geometry_valid'] and v['input_sha256']==hashlib.sha256((ROOT/'VCU_inputs.xlsx').read_bytes()).hexdigest() and not v['model_ready']);check('Resolved input equality',json.loads((ROOT/'support/generated/resolved_inputs.json').read_text())==new)
 for r in json.loads((B/'origins.json').read_text()):check('Source '+r['copy'],hashlib.sha256((B/r['copy']).read_bytes()).hexdigest()==r['sha256'])
 result={'task':'GEO-010','status':'passed' if all(c['passed'] for c in checks) else 'failed','checks':checks,'assignments':assignments};print(result['status'],f"{sum(c['passed'] for c in checks)}/{len(checks)} checks")
 if a.summary:a.summary.write_text(json.dumps(result,indent=2)+'\n')
 if result['status']!='passed':raise SystemExit(1)
if __name__=='__main__':main()
