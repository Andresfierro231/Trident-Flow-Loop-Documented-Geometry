"""Behavioral checks for the editable geometry workflow; no third-party packages."""
import copy
import importlib.util
import math
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('generate', ROOT/'scripts/generate.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)


class GeometryTests(unittest.TestCase):
    def setUp(self):
        self.t=g.read_workbook(ROOT.parent/'VCU_inputs.xlsx')

    def test_baseline_closes_and_preserves_unknowns(self):
        m=g.solve(self.t)
        self.assertLess(m['closure_gap_mm'],.001)
        self.assertEqual(len(m['sensors']),21)
        self.assertTrue(all(s['sensor_xyz_mm'] is None for s in m['sensors']))
        self.assertFalse(m['model_ready'])

    def test_end_referenced_distance(self):
        s=self.t['Sensors'][0]
        s['From endpoint']='C';s['Distance mm']=100
        m=g.solve(self.t)
        out=m['sensors'][0]
        self.assertAlmostEqual(out['axis_xyz_mm'][1],1219.2-100,5)

    def test_circumference_rotation_and_vertical_reference(self):
        s=self.t['Sensors'][0];s['Circumference deg']=0;s['Radius mm']=10
        out=g.solve(self.t)['sensors'][0]
        self.assertAlmostEqual(out['sensor_xyz_mm'][0],10,5)
        s['Circumference deg']=90
        out=g.solve(self.t)['sensors'][0]
        self.assertAlmostEqual(out['sensor_xyz_mm'][2],-10,5)
        self.assertAlmostEqual(math.dist(out['axis_xyz_mm'],out['sensor_xyz_mm']),10)

    def test_length_edits_move_geometry_and_labels(self):
        before=g.solve(self.t)
        self.t['Geometry'][0]['Length mm']+=100
        self.t['Geometry'][4]['Length mm']+=100
        after=g.solve(self.t)
        self.assertAlmostEqual(after['points']['C'][1]-before['points']['C'][1],100)
        self.assertIn('1319.200 mm',g.diagrams(after)[0].svg())

    def test_out_of_range_sensor_rejected(self):
        self.t['Sensors'][0]['Distance mm']=9999
        with self.assertRaisesRegex(ValueError,'outside segment'):
            g.solve(self.t)

    def test_inconsistent_loop_rejected(self):
        self.t['Geometry'][0]['Length mm']+=100
        with self.assertRaisesRegex(ValueError,'does not close'):
            g.solve(self.t)

    def test_acu_rejected(self):
        self.t['Start'][0]['Value']='ACU'
        with self.assertRaisesRegex(ValueError,'VCU only'):
            g.solve(self.t)

    def test_duplicate_sensor_rejected(self):
        self.t['Sensors'].append(copy.deepcopy(self.t['Sensors'][0]))
        with self.assertRaisesRegex(ValueError,'duplicate'):
            g.solve(self.t)

    def test_blank_is_not_zero(self):
        s=self.t['Sensors'][0];s['Distance mm']=0
        self.assertAlmostEqual(g.solve(self.t)['sensors'][0]['station_from_start_mm'],0)
        s['Distance mm']=None
        with self.assertRaisesRegex(ValueError,'number is required'):
            g.solve(self.t)

    def test_actual_workbook_edit_regenerates_all_outputs(self):
        # Modify a disposable XLSX value at the XML level to test the whole reader/export chain.
        with tempfile.TemporaryDirectory() as temp:
            fn=Path(temp)/'edited.xlsx'
            with zipfile.ZipFile(ROOT.parent/'VCU_inputs.xlsx') as src,zipfile.ZipFile(fn,'w') as dst:
                for item in src.infolist():
                    data=src.read(item.filename)
                    if item.filename=='xl/worksheets/sheet3.xml':
                        xml=ET.fromstring(data)
                        for cell in xml.findall('.//s:c',g.NS):
                            if cell.attrib['r']=='E6':
                                cell.find('s:v',g.NS).text='200'
                        data=ET.tostring(xml)
                    dst.writestr(item,data)
            m=g.generate(fn,Path(temp)/'out')
            self.assertAlmostEqual(m['sensors'][0]['axis_xyz_mm'][1],200,5)
            self.assertIn('B + 200.0 mm',(Path(temp)/'out/sensors.svg').read_text())
            self.assertIn('200.000',(Path(temp)/'out/VCU_control_package.tex').read_text())
            self.assertTrue(any('edited input' in n for n in m['notes']))


if __name__=='__main__':
    unittest.main()
