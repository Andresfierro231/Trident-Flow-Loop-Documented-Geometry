#!/usr/bin/env python3
"""Apply the CFG-002 literal-input patch to its saved, source-hashed DRAFT-006.

Run from the owner repository:
python3 support/scripts/sync_vcu_current_understanding.py --output /tmp/VCU_CFG002.xlsx
Preserves untouched ZIP members, styles and validations; refuses other baselines.
"""
import argparse
import copy
import hashlib
import json
import posixpath
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
from generate import read_workbook
from import_vcu_references import tag, col, write_row, S, R, P, C
ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/'support/evidence/2026-10-16_CFG-002_vcu_current_understanding'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=BUNDLE/'VCU_inputs_before_CFG-002.xlsx')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    plan=json.loads((BUNDLE/'workbook_changes.json').read_text())
    if hashlib.sha256(args.input.read_bytes()).hexdigest()!=plan['input_sha256']:
        raise SystemExit('Different baseline; refusing to replace later edits.')
    with zipfile.ZipFile(args.input) as z:
        infos=z.infolist();data={i.filename:z.read(i.filename) for i in infos}
    workbook=ET.fromstring(data['xl/workbook.xml'])
    rels=ET.fromstring(data['xl/_rels/workbook.xml.rels'])
    targets={r.get('Id'):r.get('Target') for r in rels}
    paths={s.get('name'):(targets[s.get('{'+R+'}id')].lstrip('/') if targets[s.get('{'+R+'}id')].startswith('/') else posixpath.normpath('xl/'+targets[s.get('{'+R+'}id')])) for s in workbook.find(tag('sheets'))}
    sheets={n:ET.fromstring(data[p]) for n,p in paths.items()}
    original=read_workbook(args.input)
    counts={n:len(rows[0]) for n,rows in original.items()}
    modified=set()
    for patch in plan['changes']:
        name=patch['sheet']
        if patch.get('new'):
            sheet=copy.deepcopy(sheets['Sources']);body=sheet.find(tag('sheetData'))
            for row in list(body):
                if int(row.get('r'))>5:body.remove(row)
            for kind in ['dataValidations','autoFilter','conditionalFormatting']:
                for element in sheet.findall(tag(kind)):sheet.remove(element)
            for n,text in [(1,patch['title']),(2,patch['scope']),(3,'Sources and limitations remain explicit. Blank measured values mean unknown; no package approval implied.')]:
                write_row(sheet,n,['Text'],{'Text':text})
            write_row(sheet,5,patch['headers'],dict(zip(patch['headers'],patch['headers'])))
            for i,row in enumerate(patch['rows'],6):
                write_row(sheet,i,patch['headers'],row)
                added=sheet.find(tag('sheetData'))[-1];added.set('ht','145');added.set('customHeight','1')
                for cell in added:cell.set('s','17')
            for column,width in zip(sheet.find(tag('cols')),[20,35,95,50,100]):column.set('width',str(width))
            index=len(paths)+1;path=f'xl/worksheets/cfg002_{index}.xml';rid=f'rIdCFG002_{index}'
            paths[name]=path;sheets[name]=sheet;counts[name]=len(patch['headers'])
            sid=str(max(int(s.get('sheetId')) for s in workbook.find(tag('sheets')))+1)
            ET.SubElement(workbook.find(tag('sheets')),tag('sheet'),{'name':name,'sheetId':sid,'{'+R+'}id':rid})
            ET.SubElement(rels,'{'+P+'}Relationship',{'Id':rid,'Type':R+'/worksheet','Target':path.removeprefix('xl/')})
            ct=ET.fromstring(data['[Content_Types].xml'])
            ET.SubElement(ct,'{'+C+'}Override',{'PartName':'/'+path,'ContentType':'application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml'})
            data['[Content_Types].xml']=ET.tostring(ct,encoding='utf-8',xml_declaration=True)
        else:
            headers=list(original[name][0]);sheet=sheets[name]
            if 'append' in patch:
                number=max(int(r.get('r')) for r in sheet.find(tag('sheetData')))+1
                write_row(sheet,number,headers,patch['append'])
            else:
                if patch['expect'] not in original[name]:raise SystemExit('Source row differs: '+name)
                write_row(sheet,patch['row'],headers,patch['fields'])
        modified.add(name)
    for name in modified:
        sheet=sheets[name];last=max(int(r.get('r')) for r in sheet.find(tag('sheetData')))
        dim=sheet.find(tag('dimension'))
        if dim is not None:dim.set('ref','A1:'+col(counts[name])+str(last))
        filt=sheet.find(tag('autoFilter'))
        if filt is not None:filt.set('ref','A5:'+col(counts[name])+str(last))
        data[paths[name]]=ET.tostring(sheet,encoding='utf-8',xml_declaration=True)
    data['xl/workbook.xml']=ET.tostring(workbook,encoding='utf-8',xml_declaration=True)
    data['xl/_rels/workbook.xml.rels']=ET.tostring(rels,encoding='utf-8',xml_declaration=True)
    args.output.parent.mkdir(parents=True,exist_ok=True);tmp=args.output.with_suffix('.tmp.xlsx')
    with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as z:
        for info in infos:z.writestr(info,data.pop(info.filename))
        for path,content in data.items():z.writestr(path,content)
    tmp.replace(args.output)
    print(json.dumps({'status':'ok','patch_records':len(plan['changes']),'output':str(args.output)}))
if __name__=='__main__':main()
