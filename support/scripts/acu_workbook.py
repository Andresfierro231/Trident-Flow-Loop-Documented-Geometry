#!/usr/bin/env python3
"""Build and validate the ACU workbook using literal OOXML cells only.

Python 3.11. build uses standard library; validate also requires PyYAML for
independent checks against the preserved ACU material source. No PDF renderer,
image viewer, CAD reader, network or raw-data adapter is invoked.
"""
from pathlib import Path
import argparse,csv,hashlib,json,math,posixpath,re,tomllib,zipfile
import xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/'support/evidence/2026-10-16_CFG-003_acu_inputs'
NS='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG='http://schemas.openxmlformats.org/package/2006/relationships'
N={'s':NS}
E.register_namespace('',NS);E.register_namespace('r',R)
def tag(n):return '{'+NS+'}'+n
def col(n):
 s=''
 while n:n,r=divmod(n-1,26);s=chr(65+r)+s
 return s

def read_cells(path):
 result={}
 with zipfile.ZipFile(path) as z:
  strings=[''.join(n.itertext()) for n in E.fromstring(z.read('xl/sharedStrings.xml'))] if 'xl/sharedStrings.xml' in z.namelist() else []
  rels={r.get('Id'):r.get('Target') for r in E.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
  for sh in E.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet',N):
   target=rels[sh.get('{'+R+'}id')];target=target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/'+target)
   rows={}
   for row in E.fromstring(z.read(target)).findall('s:sheetData/s:row',N):
    cells={}
    for c in row.findall('s:c',N):
     if c.find('s:f',N) is not None:raise ValueError('Formula input is not allowed: '+sh.get('name')+'!'+c.get('r'))
     address=c.get('r');k=re.sub(r'\d','',address);v=c.find('s:v',N)
     if c.get('t')=='inlineStr':value=''.join(c.find('s:is',N).itertext())
     elif v is None or v.text is None:value=None
     elif c.get('t')=='s':value=strings[int(v.text)]
     elif c.get('t') in ['str','e','b']:value=v.text
     else:value=float(v.text)
     cells[k]=value
    rows[int(row.get('r'))]=cells
   result[sh.get('name')]=rows
 return result

def read_tables(path):
 tables={}
 for name,rows in read_cells(path).items():
  headers=rows[5];tables[name]=[{key:row.get(c) for c,key in headers.items()} for i,row in sorted(rows.items()) if i>=6 and row.get('A') not in (None,'')]
 return tables

def build(output):
 tables=json.loads((BUNDLE/'tables.json').read_text());data={}
 workbook=E.Element(tag('workbook'));E.SubElement(E.SubElement(workbook,tag('bookViews')),tag('workbookView'));sheets=E.SubElement(workbook,tag('sheets'))
 rels=E.Element('{'+PKG+'}Relationships');content=E.Element('{http://schemas.openxmlformats.org/package/2006/content-types}Types')
 CT='{http://schemas.openxmlformats.org/package/2006/content-types}'
 for ext,ctype in [('rels','application/vnd.openxmlformats-package.relationships+xml'),('xml','application/xml')]:E.SubElement(content,CT+'Default',{'Extension':ext,'ContentType':ctype})
 E.SubElement(content,CT+'Override',{'PartName':'/xl/workbook.xml','ContentType':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml'})
 E.SubElement(content,CT+'Override',{'PartName':'/xl/styles.xml','ContentType':'application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml'})
 for index,(name,t) in enumerate(tables.items(),1):
  E.SubElement(sheets,tag('sheet'),{'name':name,'sheetId':str(index),'{'+R+'}id':'rId'+str(index)})
  E.SubElement(rels,'{'+PKG+'}Relationship',{'Id':'rId'+str(index),'Type':R+'/worksheet','Target':f'worksheets/sheet{index}.xml'})
  E.SubElement(content,CT+'Override',{'PartName':f'/xl/worksheets/sheet{index}.xml','ContentType':'application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml'})
  ws=E.Element(tag('worksheet'));E.SubElement(ws,tag('dimension'),{'ref':'A1:'+col(len(t['headers']))+str(len(t['rows'])+5)})
  view=E.SubElement(E.SubElement(ws,tag('sheetViews')),tag('sheetView'),{'workbookViewId':'0','showGridLines':'0'})
  E.SubElement(view,tag('pane'),{'ySplit':'5','topLeftCell':'A6','activePane':'bottomLeft','state':'frozen'})
  columns=E.SubElement(ws,tag('cols'))
  for j,h in enumerate(t['headers'],1):
   numeric=any(word in h for word in [' mm',' K',' deg',' X ',' Y ',' Z '])
   width=22 if numeric else 28 if j==1 else 60 if any(word in h.lower() for word in ['source','notes','qualification','evidence','understanding','locator','specification','question','equation']) else 38
   E.SubElement(columns,tag('col'),{'min':str(j),'max':str(j),'width':str(width),'customWidth':'1'})
  body=E.SubElement(ws,tag('sheetData'))
  def row(number,values,style,height=None):
   rr=E.SubElement(body,tag('row'),{'r':str(number),**({'ht':str(height),'customHeight':'1'} if height else {})})
   for j,val in enumerate(values,1):
    if val is None or val=='':continue
    address=col(j)+str(number);cell=E.SubElement(rr,tag('c'),{'r':address,'s':str(style)})
    if isinstance(val,(int,float)) and not isinstance(val,bool):
     if not math.isfinite(val):raise ValueError('Nonfinite '+name+'!'+address)
     E.SubElement(cell,tag('v')).text=str(val)
    else:
     cell.set('t','inlineStr');E.SubElement(E.SubElement(cell,tag('is')),tag('t'),{'{http://www.w3.org/XML/1998/namespace}space':'preserve'}).text=str(val)
  row(1,['ACU | '+name],1,28)
  row(2,['ACU-REVB-DRAFT-001 | 2026-10-16 | Draft; installation and scientific review pending.'],2,32)
  row(3,['Blank = unknown. Cite Sources and exact locator. CAD, reported and assumed values are distinct. See Provenance for cell-level evidence.'],2,42)
  row(4,['ACU operating-data processing remains on hold. This workbook records existing documents only.'],2,32)
  row(5,t['headers'],3,42)
  for i,record in enumerate(t['rows'],6):
   # Rows can be expanded by the contributor; set enough height for wrapped text.
   lengths=[len(str(record.get(h) or '')) for h in t['headers']]
   height=min(260,max(60,15*(1+max(lengths,default=0)//48)))
   row(i,[record.get(h) for h in t['headers']],5 if name.startswith('Form ') else 4,height)
  E.SubElement(ws,tag('autoFilter'),{'ref':'A5:'+col(len(t['headers']))+str(len(t['rows'])+5)})
  merge=E.SubElement(ws,tag('mergeCells'),{'count':'4'})
  for n in range(1,5):E.SubElement(merge,tag('mergeCell'),{'ref':'A'+str(n)+':'+col(len(t['headers']))+str(n)})
  if name=='Insulation regions':
   key=t['headers'].index('Coverage')+1;valids=E.SubElement(ws,tag('dataValidations'),{'count':'1'})
   v=E.SubElement(valids,tag('dataValidation'),{'type':'list','allowBlank':'0','showErrorMessage':'1','sqref':col(key)+'6:'+col(key)+str(5+len(t['rows']))})
   E.SubElement(v,tag('formula1')).text='"Unknown,Insulated,Bare"'
  data[f'xl/worksheets/sheet{index}.xml']=E.tostring(ws,encoding='utf-8',xml_declaration=True)
 E.SubElement(rels,'{'+PKG+'}Relationship',{'Id':'rIdStyles','Type':R+'/styles','Target':'styles.xml'})
 data['xl/workbook.xml']=E.tostring(workbook,encoding='utf-8',xml_declaration=True);data['xl/_rels/workbook.xml.rels']=E.tostring(rels,encoding='utf-8',xml_declaration=True)
 data['[Content_Types].xml']=E.tostring(content,encoding='utf-8',xml_declaration=True)
 data['_rels/.rels']=f'<Relationships xmlns="{PKG}"><Relationship Id="rId1" Type="{R}/officeDocument" Target="xl/workbook.xml"/></Relationships>'.encode()
 data['xl/styles.xml']=f'''<styleSheet xmlns="{NS}"><fonts count="3"><font><sz val="11"/><name val="Calibri"/></font><font><b/><color rgb="FFFFFFFF"/><sz val="16"/><name val="Calibri"/></font><font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Calibri"/></font></fonts><fills count="5"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF16374A"/><bgColor indexed="64"/></patternFill></fill><fill><patternFill patternType="solid"><fgColor rgb="FFF2F5F6"/><bgColor indexed="64"/></patternFill></fill><fill><patternFill patternType="solid"><fgColor rgb="FFFFF2CC"/><bgColor indexed="64"/></patternFill></fill></fills><borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders><cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs><cellXfs count="6"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="center"/></xf><xf numFmtId="0" fontId="0" fillId="3" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf><xf numFmtId="0" fontId="2" fillId="2" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf><xf numFmtId="0" fontId="0" fillId="4" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf></cellXfs><cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles></styleSheet>'''.encode()
 output.parent.mkdir(parents=True,exist_ok=True);temp=output.with_suffix('.tmp.xlsx')
 with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as z:
  for path,content in data.items():
   info=zipfile.ZipInfo(path,date_time=(2026,10,16,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,content)
 temp.replace(output)
 print(json.dumps({'status':'built','output':str(output),'sheets':len(tables),'bytes':output.stat().st_size}))

def validate(path,outdir):
 import yaml
 checks=[]
 def ck(name,condition):checks.append({'check':name,'pass':bool(condition)})
 tables=read_tables(path);sources=json.loads((BUNDLE/'inputs.json').read_text());paths={r['Source ID']:ROOT/r['File / record'] for r in sources}
 def raw(sid):return list(csv.DictReader(paths[sid].open(newline='')))
 for r in sources:ck('source hash '+r['Source ID'],hashlib.sha256(paths[r['Source ID']].read_bytes()).hexdigest()==r['SHA-256'])
 reviewed=yaml.safe_load(paths['GSELECT'].read_text())
 for key,sid in [('pipe_segments','GSEG'),('comparisons','GCMP'),('bends','GBEND'),('thermal_zones','GZONE'),('components','GCOMP'),('exits','GEXIT'),('sensors','GSENS')]:
  ck('reviewed geometry authority hash '+key,hashlib.sha256(paths[sid].read_bytes()).hexdigest()==reviewed['source_tables'][key]['sha256'])
 for b in raw('GBEND'):
  ck('torus arc '+b['bend_id'],math.isclose(float(b['radius_mm'])*float(b['sweep_rad']),float(b['arc_length_mm']),abs_tol=1e-8))
 settings={r['Field']:r['Value'] for r in tables['Start']};ck('facility ACU',settings['Facility']=='ACU');ck('draft configuration',settings['Configuration ID']=='ACU-REVB-DRAFT-001' and settings['Status']=='Draft')
 for s,n in [('Geometry',8),('Sensors',15),('Sensor points',26),('Native channels',119),('Instruments',48),('Instrument classes',20),('Requirements',78)]:ck('inventory '+s,len(tables[s])==n)
 seed=json.loads((BUNDLE/'tables.json').read_text())
 for name,t in seed.items():ck('seed transcription '+name,tables[name]==t['rows'])
 geom={r['Segment']:r for r in tables['Geometry']};segments=raw('GSEG');comp={r['component_id']:r for r in raw('GCOMP')};total=0
 for r in segments:
  g=geom[r['segment_id']];straight=r['geometry']=='straight_tangent_span'
  ck('centerline '+r['segment_id'],math.isclose(g['Length mm'] if straight else g['Arc length mm'],float(r['centerline_length_mm']),abs_tol=1e-10));total+=g['Length mm'] if straight else g['Arc length mm']
  ck('main bore/OD '+r['segment_id'],g['ID mm']==float(comp['MAIN_PIPE']['id_mm']) and g['OD mm']==float(comp['MAIN_PIPE']['od_mm']))
  ck('no blanket thickness '+r['segment_id'],g['Insulation mm'] is None)
  for end in ['start','end']:
   for axis in 'xyz':ck('XYZ '+r['segment_id']+' '+end+axis,g[end.title()+' '+axis.upper()+' mm']==float(r[end+'_'+axis+'_mm']))
  if straight:
   phi=math.radians(g['Phi deg']);length=g['Length mm'];ck('direction '+r['segment_id'],math.isclose(length*math.sin(phi),float(r['delta_x_mm']),abs_tol=1e-8) and math.isclose(length*math.cos(phi),float(r['delta_y_mm']),abs_tol=1e-8))
 ck('total physical centerline',math.isclose(total,5687.535910181431,abs_tol=1e-9))
 for i,r in enumerate(segments):
  nxt=segments[(i+1)%len(segments)];ck('endpoint continuity '+r['segment_id'],all(math.isclose(float(r['end_'+ax+'_mm']),float(nxt['start_'+ax+'_mm']),abs_tol=1e-8) for ax in 'xyz'))
 sm={r['sensor_id']:r for r in raw('GSENS')}
 for r in tables['Sensors']:
  s=sm[r['Sensor ID']];ck('sensor station '+r['Sensor ID'],r['Segment']==s['leg_id'] and r['Distance mm']==float(s['offset_from_flat_start_mm']))
  ck('no invented sensor operator '+r['Sensor ID'],all(r[k] is None for k in ['DAQ channel','Circumference deg','Radius mm']))
  for axis in 'xyz':ck('saved sensor XYZ '+r['Sensor ID']+' '+axis,r['Reference '+axis.upper()+' mm']==float(s['global_'+axis+'_mm']))
 for r,s in zip(tables['Sensor points'],raw('GPOINT')):
  ck('saved point '+s['point_id'],r['Point ID']==s['point_id'] and all(r[ax.upper()+' mm']==float(s['global_'+ax+'_mm']) for ax in 'xyz') and r['Attachment check']==s['verification_status'])
 for r in tables['Calibration']:ck('unknown calibration '+r['Sensor ID'],all(r[k] is None for k in ['Model / serial','Last calibration','Certificate','Range','Correction','Uncertainty','Coverage factor','Acquisition / lag']))
 zones={r['zone_id']:r for r in raw('GZONE')}
 for feature,zid in [('Heating tape hardware','HEATING_TAPE'),('Cooling jacket hardware','COOLING_JACKET')]:
  r=next(r for r in tables['Thermal spans'] if r['Feature']==feature);z=zones[zid];ck('hardware span '+feature,r['Start mm']==float(z['start_offset_mm']) and r['End mm']==float(z['end_offset_mm']))
 for r in tables['Thermal spans']:
  if r['Feature'].startswith('Active'):ck('unknown measured active span '+r['Feature'],r['Start mm'] is None and r['End mm'] is None)
 declared=tomllib.loads(paths['SITECH'].read_text())['channel'];declinst=tomllib.loads(paths['SITEINST'].read_text())
 for r in tables['Native channels']:
  pv=r['Native channel'];d=declared[pv];matches=[i['id'] for i in declinst['instrument'] if pv in i.get('channels',[])];ck('exact site channel '+pv,r['Declared unit']==d.get('unit') and r['Declared description']==d.get('description') and r['Candidate instrument IDs']==('; '.join(matches) or None) and r['Run applicability'] is None)
 pwm=[r for r in tables['Native channels'] if re.search(r'HE-[^:]+:Time$',r['Native channel'])];ck('13 PWM widths in ms',len(pwm)==13 and all(r['Declared unit']=='ms' for r in pwm))
 for r in tables['Instrument classes']:
  original=declinst['instrument_class'][r['Class ID']];extra={k:v for k,v in original.items() if k not in ['maker','model','kind']};ck('exact class '+r['Class ID'],json.loads(r['Declared specifications'])==extra)
 for r in tables['Instruments']:
  original=next(i for i in declinst['instrument'] if i['id']==r['Instrument ID']);ck('exact instrument '+r['Instrument ID'],r['Class ID']==original['class'] and r['Placement']==original.get('placement') and r['Native channels']==('; '.join(original.get('channels',[])) or None))
 original_xlsx=read_cells(paths['SITEXLSX'])
 for r in tables['Site source rows']:
  cells=original_xlsx[r['Original sheet']][int(r['Original row'])]
  mapping={'Name':'A','Model':'B','Location / description':'C','EPICS prefix':'D','Column E':'E','DAQ notes':'F','URL':'G'}
  ck('original sensor workbook row '+r['Source row'],all(r[k]==cells.get(c) for k,c in mapping.items()))
 materials=yaml.safe_load(paths['AMAT'].read_text())['materials']
 for r in tables['Property branches']:
  f=materials[r['Material ID']]['properties'][r['Property']];ck('property definition '+r['Material ID']+'/'+r['Property'],r['Model']==f['model'] and r['Output units']==f['units'] and r['Working minimum K']==f['valid_temperature_K'][0] and r['Working maximum K']==f['valid_temperature_K'][1] and r['Out-of-range policy']=='error' and r['Calibration eligible']=='false')
  if f['model']=='constant':ck('constant '+r['Material ID']+'/'+r['Property'],float(r['Exact equation / table'])==f['value'])
  elif f['model']=='polynomial':
   values=[float(v) for v in re.findall(r'\(([-+\d.eE]+)\)',r['Exact equation / table'])];ck('polynomial coefficients '+r['Material ID']+'/'+r['Property'],values==f['coefficients'])
  elif f['model']=='exponential_inverse_temperature':
   eq=r['Exact equation / table'];values=[float(eq.split(' * exp(')[0])]+[float(v) for v in re.findall(r'\(([-+\d.eE]+)\)/T_K',eq)];ck('exponential coefficients '+r['Material ID'],values==f['coefficients'])
 for r,s in zip(tables['Fluid table'],raw('MTABLE')):ck('legacy fluid table T='+str(s['temperature_K']),all(r[k]==float(v) for k,v in s.items()))
 for r in tables['Fluids']:ck('no invented operating limits '+r['Fluid ID'],r['Minimum C'] is None and r['Maximum C'] is None and r['Concentration'] is None)
 for name in ['Form pipe','Form sensor','Form material']:
  ck('blank intake '+name,all(all(r[k] is None for k in ['Your entry','Your evidence file / location','Reviewer / date']) for r in tables[name]))
 ck('no physical approval invented',all(r['Selected choice'] is None and r['Reviewer / date'] is None and r['Review state'] in ['Needs information','Needs review'] for r in tables['Requirements']))
 ids={r['Source ID'] for r in tables['Sources']};ledger={r['Cell']:r for r in tables['Provenance']}
 ck('unique source IDs',len(ids)==len(tables['Sources']));ck('unique cell provenance',len(ledger)==len(tables['Provenance']))
 for s,rows in tables.items():
  if s=='Provenance':continue
  headers=list(rows[0])
  missing=[];bad=[]
  for i,r in enumerate(rows,6):
   for j,k in enumerate(headers,1):
    if r[k] in (None,''):continue
    address=s+'!'+col(j)+str(i);p=ledger.get(address)
    if p is None:missing.append(address)
    elif any(ref.strip() not in ids for ref in p['Source IDs'].split(';')):bad.append(address)
  ck('all populated cells have provenance '+s,not missing);ck('valid provenance sources '+s,not bad)
 # Check all OOXML text, including banners, for foreign-facility leftovers.
 with zipfile.ZipFile(path) as z:
  ck('ZIP CRC',z.testzip() is None);ck('no hidden sheets or shared-string leftovers','xl/sharedStrings.xml' not in z.namelist())
  text='\n'.join(z.read(n).decode() for n in z.namelist() if n.endswith('.xml'))
  banned=['VCU','Prop-30','PROP30','JTC-A','JTC-B','PTC-X','STC-','942.186081','1346.496214','5556K73','4057K14']
  for word in banned:ck('no foreign value '+word,word not in text)
  ck('no macros/embedded drawings',not any(n.endswith('.bin') or '/drawings/' in n or '/media/' in n for n in z.namelist()))
 result={'status':'pass' if all(c['pass'] for c in checks) else 'fail','task_id':'CFG-003','configuration':settings['Configuration ID'],'checks':len(checks),'passed':sum(c['pass'] for c in checks),'workbook_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'physical_centerline_mm':total,'model_ready':False,'operating_data_processed':False,'visual_inspection':False,'counts':{s:len(r) for s,r in tables.items()},'details':checks}
 outdir.mkdir(parents=True,exist_ok=True);(outdir/'checks.json').write_text(json.dumps(result,indent=2)+'\n');(outdir/'resolved_inputs.json').write_text(json.dumps(tables,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ['details','counts']}))
 for c in checks:
  if not c['pass']:print('FAIL: '+c['check'])
 return result['status']=='pass'

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('action',choices=['build','validate']);p.add_argument('--workbook',type=Path,default=ROOT/'ACU_inputs.xlsx');p.add_argument('--output-dir',type=Path,default=ROOT/'support/generated/acu');a=p.parse_args()
 if a.action=='build':build(a.workbook)
 else:raise SystemExit(0 if validate(a.workbook,a.output_dir) else 1)
if __name__=='__main__':main()
