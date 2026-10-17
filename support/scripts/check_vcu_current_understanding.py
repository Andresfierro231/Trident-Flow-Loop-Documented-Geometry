#!/usr/bin/env python3
"""Check CFG-002 source fidelity, preserved unknowns and generated exports.

Inputs: current master, saved DRAFT-006, patch plan, source snapshots and exports.
Output: concise JSON plus --output JSON receipt; exit nonzero on any failed check.
Run: python3 support/scripts/check_vcu_current_understanding.py --output /tmp/cfg002_checks.json
"""
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import zipfile
from generate import read_workbook
ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/'support/evidence/2026-10-16_CFG-002_vcu_current_understanding'

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    checks=[]
    def check(name,condition):checks.append({'check':name,'pass':bool(condition)})
    master=ROOT/'VCU_inputs.xlsx';base=BUNDLE/'VCU_inputs_before_CFG-002.xlsx'
    original=read_workbook(base);actual=read_workbook(master)
    plan=json.loads((BUNDLE/'workbook_changes.json').read_text())
    check('baseline hash',hashlib.sha256(base.read_bytes()).hexdigest()==plan['input_sha256'])
    expected=copy.deepcopy(original)
    for patch in plan['changes']:
        s=patch['sheet']
        if patch.get('new'):expected[s]=patch['rows']
        elif 'append' in patch:
            expected[s].append({k:patch['append'].get(k) for k in original[s][0]})
        else:
            key=next(iter(patch['expect']))
            index=next(i for i,r in enumerate(expected[s]) if r[key]==patch['expect'][key])
            check(f'{s} baseline row {patch["row"]}',expected[s][index]==patch['expect'])
            expected[s][index].update(patch['fields'])
    for s in expected:check('exact intended sheet values: '+s,expected[s]==actual[s])
    for src in json.loads((BUNDLE/'inputs.json').read_text()):
        check('portable source hash '+src['source_id'],hashlib.sha256((ROOT/src['portable_path']).read_bytes()).hexdigest()==src['sha256'])
    w=json.loads((BUNDLE/'WORK_rev9_working_selection_v3.json').read_text());wm={r['source_id']:r for r in w['sensors']}
    geometry={r['Segment']:r for r in actual['Geometry']}
    for s in ['Geometry','Materials','Insulation regions','CAD dimensions','Phase requests','Form pipe','Form material']:
        check('fully preserved '+s,actual[s]==original[s])
    for r in actual['Sensors']:
        sid=r['Sensor ID'];ref=wm[sid];g=geometry[r['Segment']]
        station=r['Distance mm'] if r['From endpoint']==g['Start'] else g['Length mm']-r['Distance mm']
        check('Rev9 station '+sid,math.isclose(station,ref['station_from_start_mm'],abs_tol=1e-5))
        check('working channel '+sid,r['DAQ channel']==ref['channel'])
        check('no invented radius/angle '+sid,r['Radius mm'] is None and r['Circumference deg'] is None)
    check('16 main bindings',sum(bool(r['DAQ channel']) for r in actual['Sensors'])==16)
    channels={r['Native channel']:r for r in actual['Native channels']}
    check('20 native channels',len(channels)==20)
    for native,sid,role in [('PTC5','JTC-B','inlet'),('PTC6','JTC-A','outlet')]:
        check('jacket role '+native,channels[native]['Reference / domain'].startswith(sid) and role in channels[native]['Working role / operator'])
    for r in actual['Calibration']:
        check('no invented calibration '+r['Sensor ID'],all(r[k] is None for k in ['Model / serial','Last calibration','Certificate','Range','Correction','Uncertainty','Coverage factor','Acquisition / lag']))
    for r in actual['Thermal spans']:
        if r['Feature'].startswith('Active'):check('measured thermal extent remains unknown '+r['Feature'],r['Start mm'] is None and r['End mm'] is None)
    check('main bore null',all(r['ID mm'] is None for r in actual['Geometry']))
    check('excluded PTC-X absent',not any(r['Sensor ID']=='PTC-X' for r in actual['Sensors']+actual['Calibration']))
    check('26 current knowledge topics',len(actual['Current knowledge'])==26)
    req=actual['Requirements'];check('78 requirements preserved',len(req)==78)
    check('no release approval invented',not any(r['Review state']=='Approved for stated use' for r in req))
    for r in actual['Fluids']:check('no operating limits invented '+r['Fluid ID'],r['Minimum C'] is None and r['Maximum C'] is None)
    with zipfile.ZipFile(base) as z0,zipfile.ZipFile(master) as z1:
        for n in z0.namelist():
            if n.startswith('xl/worksheets/') or n in ['xl/workbook.xml','xl/_rels/workbook.xml.rels','[Content_Types].xml']:continue
            check('untouched XLSX member '+n,z0.read(n)==z1.read(n))
    resolved=json.loads((ROOT/'support/generated/resolved_inputs.json').read_text());check('generated resolved input equality',resolved==actual)
    validation=json.loads((ROOT/'support/generated/validation.json').read_text());digest=hashlib.sha256(master.read_bytes()).hexdigest()
    check('generated workbook hash',validation['input_sha256']==digest)
    check('geometry closure',validation['geometry_valid'] and validation['closure_gap_mm']<0.1)
    check('model readiness remains false',validation['model_ready'] is False)
    tex=(ROOT/'support/generated/VCU_control_package.tex').read_text()
    register=(ROOT/'support/generated/requirements_and_evidence.md').read_text()
    for phrase in ['Native channels','Current knowledge','June12','PTC5','VCU-REV9-DRAFT-007']:
        check('LaTeX exports '+phrase,phrase in tex)
    for phrase in ['Native channels','Current knowledge','June12','PTC5']:
        check('readable register exports '+phrase,phrase in register)
    result={'status':'pass' if all(c['pass'] for c in checks) else 'fail','checks':len(checks),'passed':sum(c['pass'] for c in checks),'workbook_sha256':digest,'details':checks}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='details'}))
    for c in checks:
        if not c['pass']:print('FAIL: '+c['check'])
    raise SystemExit(0 if result['status']=='pass' else 1)
if __name__=='__main__':main()
