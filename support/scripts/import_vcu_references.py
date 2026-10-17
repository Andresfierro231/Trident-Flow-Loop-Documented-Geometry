#!/usr/bin/env python3
"""Reproduce CFG-001 from its hashed baseline, using only the standard library.

Untouched XLSX ZIP members, dropdowns and styles are preserved. A different
input hash is refused, preventing accidental replacement of later team edits.
"""
import argparse, copy, hashlib, json, posixpath, sys, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/'support/evidence/2026-10-16_CFG-001_vcu_references'
S='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
P='http://schemas.openxmlformats.org/package/2006/relationships'
C='http://schemas.openxmlformats.org/package/2006/content-types'
ET.register_namespace('x',S);ET.register_namespace('r',R)
def tag(n): return '{'+S+'}'+n
def col(n):
    result=''
    while n:
        n,r=divmod(n-1,26);result=chr(65+r)+result
    return result

def write_row(sheet,number,headers,fields):
    body=sheet.find(tag('sheetData'))
    row=next((r for r in body if int(r.get('r'))==number),None)
    if row is None:
        template=body[-1]
        row=ET.SubElement(body,tag('row'),{'r':str(number)})
    else: template=row
    for key,data in fields.items():
        address=col(headers.index(key)+1)+str(number)
        cell=next((c for c in row if c.get('r')==address),None)
        if cell is None:
            cell=ET.SubElement(row,tag('c'),{'r':address})
            old=next((c for c in template if ''.join(filter(str.isalpha,c.get('r')))==col(headers.index(key)+1)),None)
            if old is not None and old.get('s'):cell.set('s',old.get('s'))
        for child in list(cell):cell.remove(child)
        cell.attrib.pop('t',None)
        if data is None:continue
        if isinstance(data,(int,float)):ET.SubElement(cell,tag('v')).text=str(data)
        else:
            cell.set('t','inlineStr');ET.SubElement(ET.SubElement(cell,tag('is')),tag('t')).text=str(data)
    row[:]=sorted(row,key=lambda c:(len(''.join(filter(str.isalpha,c.get('r')))),''.join(filter(str.isalpha,c.get('r')))))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=BUNDLE/'VCU_inputs_before_CFG-001.xlsx')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();payload=json.loads((BUNDLE/'workbook_changes.json').read_text())
    if hashlib.sha256(args.input.read_bytes()).hexdigest()!=payload['input_sha256']:raise SystemExit('Different baseline; refusing to overwrite later edits.')
    with zipfile.ZipFile(args.input) as z:
        infos=z.infolist();data={i.filename:z.read(i.filename) for i in infos}
    workbook=ET.fromstring(data['xl/workbook.xml']);rels=ET.fromstring(data['xl/_rels/workbook.xml.rels'])
    targets={r.get('Id'):r.get('Target') for r in rels}
    paths={s.get('name'):(targets[s.get('{'+R+'}id')].lstrip('/') if targets[s.get('{'+R+'}id')].startswith('/') else posixpath.normpath('xl/'+targets[s.get('{'+R+'}id')])) for s in workbook.find(tag('sheets'))}
    sheets={n:ET.fromstring(data[p]) for n,p in paths.items()}
    sys.path.insert(0,str(ROOT/'support/scripts'))
    from generate import read_workbook
    original=read_workbook(args.input);modified=set();counts={n:len(rows[0]) for n,rows in original.items()}
    for patch in payload['changes']:
        name=patch['sheet']
        if patch.get('new'):
            source=copy.deepcopy(sheets['Sources']);body=source.find(tag('sheetData'))
            for row in list(body):
                if int(row.get('r'))>5:body.remove(row)
            for kind in ['dataValidations','autoFilter','conditionalFormatting']:
                for element in source.findall(tag(kind)):source.remove(element)
            write_row(source,1,['Title'],{'Title':'VCU Rev9 component reference dimensions'})
            write_row(source,2,['Scope'],{'Scope':'CAD-derived local dimensions; not installed measurements. Main bore unknown.'})
            write_row(source,5,patch['headers'],dict(zip(patch['headers'],patch['headers'])))
            for i,row in enumerate(patch['rows'],6):
                write_row(source,i,patch['headers'],row)
                added=source.find(tag('sheetData'))[-1]
                added.set('ht','110');added.set('customHeight','1')
                for cell in added:cell.set('s','17')
            for column,width in zip(source.find(tag('cols')),[15,36,86,12,112]):column.set('width',str(width))
            write_row(source,3,['Guide'],{'Guide':'Use local bores only for the identified component. Portable source: support/evidence/2026-10-16_CFG-001_vcu_references/VCU_Rev9_Diameters.csv'})
            paths[name]='xl/worksheets/cfg001_dimensions.xml';sheets[name]=source;counts[name]=len(patch['headers'])
            rid='rIdCFG001Dimensions'
            sid=str(max(int(s.get('sheetId')) for s in workbook.find(tag('sheets')))+1)
            ET.SubElement(workbook.find(tag('sheets')),tag('sheet'),{'name':name,'sheetId':sid,'{'+R+'}id':rid})
            ET.SubElement(rels,'{'+P+'}Relationship',{'Id':rid,'Type':R+'/worksheet','Target':'worksheets/cfg001_dimensions.xml'})
            ct=ET.fromstring(data['[Content_Types].xml'])
            ET.SubElement(ct,'{'+C+'}Override',{'PartName':'/'+paths[name],'ContentType':'application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml'})
            data['[Content_Types].xml']=ET.tostring(ct,encoding='utf-8',xml_declaration=True)
        else:
            headers=list(original[name][0]);sheet=sheets[name]
            if 'append' in patch:
                number=max(int(r.get('r')) for r in sheet.find(tag('sheetData')))+1
                write_row(sheet,number,headers,patch['append'])
                filt=sheet.find(tag('autoFilter'))
                if filt is not None:filt.set('ref','A5:'+col(len(headers))+str(number))
            else:
                if original[name][patch['row']-6]!=patch['expect']:raise SystemExit('Source row differs: '+name)
                write_row(sheet,patch['row'],headers,patch['fields'])
        modified.add(name)
    for name in modified:
        dimension=sheets[name].find(tag('dimension'))
        if dimension is not None:dimension.set('ref','A1:'+col(counts[name])+str(max(int(r.get('r')) for r in sheets[name].find(tag('sheetData')))))
        data[paths[name]]=ET.tostring(sheets[name],encoding='utf-8',xml_declaration=True)
    data['xl/workbook.xml']=ET.tostring(workbook,encoding='utf-8',xml_declaration=True)
    data['xl/_rels/workbook.xml.rels']=ET.tostring(rels,encoding='utf-8',xml_declaration=True)
    args.output.parent.mkdir(parents=True,exist_ok=True);temporary=args.output.with_suffix('.tmp.xlsx')
    with zipfile.ZipFile(temporary,'w',zipfile.ZIP_DEFLATED) as z:
        for info in infos:z.writestr(info,data.pop(info.filename))
        for path,content in data.items():z.writestr(path,content)
    temporary.replace(args.output)
    print(f'CFG-001: updated {len(modified)} sheets; added 14 local CAD component records.')
if __name__=='__main__':main()
