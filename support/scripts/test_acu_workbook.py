"""Failure checks for the ACU evidence workbook; no source/master mutations."""
from pathlib import Path
from tempfile import TemporaryDirectory
import contextlib,io,unittest,zipfile
import xml.etree.ElementTree as E
from acu_workbook import ROOT,BUNDLE,NS,build,read_cells,validate

class ACUWorkbookChecks(unittest.TestCase):
 def mutate(self,folder,cell,new_value=None,formula=False,member="xl/worksheets/sheet1.xml"):
  base=ROOT/'ACU_inputs.xlsx';output=folder/'mutated.xlsx'
  with zipfile.ZipFile(base) as src,zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as dst:
   for info in src.infolist():
    data=src.read(info.filename)
    if info.filename==member:
     root=E.fromstring(data);c=next((c for c in root.iter('{'+NS+'}c') if c.get('r')==cell),None)
     if c is None:
      row=next(r for r in root.iter('{'+NS+'}row') if r.get('r')==''.join(ch for ch in cell if ch.isdigit()))
      c=E.SubElement(row,'{'+NS+'}c',{'r':cell})
     for node in list(c):c.remove(node)
     if formula:
      c.attrib.pop('t',None);E.SubElement(c,'{'+NS+'}f').text='1+1';E.SubElement(c,'{'+NS+'}v').text='2'
     else:
      c.set('t','inlineStr');E.SubElement(E.SubElement(c,'{'+NS+'}is'),'{'+NS+'}t').text=new_value
     data=E.tostring(root,encoding='utf-8',xml_declaration=True)
    dst.writestr(info,data)
  return output
 def test_reproducible_build(self):
  with TemporaryDirectory() as d,contextlib.redirect_stdout(io.StringIO()):
   output=Path(d)/'copy.xlsx';build(output)
   self.assertEqual(output.read_bytes(),(ROOT/'ACU_inputs.xlsx').read_bytes())
 def test_formula_is_rejected_even_with_cached_value(self):
  with TemporaryDirectory() as d:
   output=self.mutate(Path(d),'B6',formula=True)
   with self.assertRaisesRegex(ValueError,'Formula input'):read_cells(output)
 def test_other_facility_tag_fails(self):
  with TemporaryDirectory() as d,contextlib.redirect_stdout(io.StringIO()):
   output=self.mutate(Path(d),'B6','VCU')
   self.assertFalse(validate(output,Path(d)/'qa'))
 def test_inferred_sensor_native_binding_is_rejected(self):
  with TemporaryDirectory() as d,contextlib.redirect_stdout(io.StringIO()):
   # A plausible native name still cannot establish a physical CAD sensor join.
   output=self.mutate(Path(d),'H6','NCDT1:HEAT:TC-HP1_1',member='xl/worksheets/sheet3.xml')
   self.assertFalse(validate(output,Path(d)/'qa'))

if __name__=='__main__':unittest.main()
