"""Insulation coverage must remain independent from geometry and thermal boundaries."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('generate', ROOT / 'scripts/generate.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
from insulation import default_rows, HEADERS, insulation_diagram


class InsulationTests(unittest.TestCase):
    def setUp(self):
        self.tables = g.read_workbook(ROOT / 'tests/fixtures/VCU_inputs.xlsx')
        self.tables['Insulation regions'] = default_rows()

    def test_old_workbook_remains_unknown_without_inference(self):
        del self.tables['Insulation regions']
        self.tables['Geometry'][0]['Insulation mm'] = 50
        model = g.solve(self.tables)
        self.assertEqual(len(model['insulation_regions']), 10)
        self.assertTrue(all(r['coverage'] == 'Unknown' and r['thickness_mm'] is None for r in model['insulation_regions']))
        self.assertTrue(any('worksheet absent' in n for n in model['notes']))

    def test_top_regions_partition_parent_segment(self):
        model = g.solve(self.tables)
        pre, cooler, post = model['insulation_regions'][2:5]
        length = model['segments']['cooler']['axial_length_mm']
        self.assertEqual(pre['start_station_mm'], 0)
        self.assertEqual(pre['end_station_mm'], cooler['start_station_mm'])
        self.assertEqual(cooler['end_station_mm'], post['start_station_mm'])
        self.assertAlmostEqual(post['end_station_mm'], length)
        self.assertAlmostEqual(sum(r['length_mm'] for r in (pre, cooler, post)), length)
        self.assertEqual(pre['end_xyz_mm'], cooler['start_xyz_mm'])
        self.assertEqual(cooler['end_xyz_mm'], post['start_xyz_mm'])

    def test_jacket_reference_can_use_other_endpoint(self):
        before = g.solve(self.tables)
        length = before['segments']['cooler']['axial_length_mm']
        row = self.tables['Thermal spans'][0]
        start, end = row['Start mm'], row['End mm']
        row.update({'From endpoint': 'E', 'Start mm': length - end, 'End mm': length - start})
        after = g.solve(self.tables)
        for a, b in zip(before['insulation_regions'][2:5], after['insulation_regions'][2:5]):
            self.assertAlmostEqual(a['start_station_mm'], b['start_station_mm'])
            self.assertAlmostEqual(a['end_station_mm'], b['end_station_mm'])

    def test_missing_jacket_leaves_top_extents_unresolved(self):
        self.tables['Thermal spans'] = self.tables['Thermal spans'][1:]
        model = g.solve(self.tables)
        for row in model['insulation_regions'][2:5]:
            self.assertFalse(row['extent_resolved'])
            self.assertIsNone(row['length_mm'])
            self.assertIsNone(row['start_xyz_mm'])
        self.assertIn('extent unresolved', insulation_diagram(model, g.Drawing).svg())

    def test_reversed_or_ambiguous_jacket_is_rejected(self):
        row = self.tables['Thermal spans'][0]
        row['Start mm'], row['End mm'] = row['End mm'], row['Start mm']
        with self.assertRaisesRegex(ValueError, 'positive span'):
            g.solve(self.tables)
        row['Start mm'], row['End mm'] = row['End mm'], row['Start mm']
        self.tables['Thermal spans'].append(copy.deepcopy(row))
        with self.assertRaisesRegex(ValueError, 'ambiguous'):
            g.solve(self.tables)

    def test_independent_states_preserve_physical_geometry(self):
        before = g.solve(self.tables)
        self.tables['Insulation regions'][0].update({'Coverage': 'Insulated', 'Material ID': 'MAIN-INS', 'Thickness mm': 50})
        self.tables['Insulation regions'][1]['Coverage'] = 'Bare'
        after = g.solve(self.tables)
        for key in ('points', 'segments', 'sensors', 'thermal_spans'):
            self.assertEqual(before[key], after[key])
        self.assertEqual([r['coverage'] for r in after['insulation_regions'][:3]], ['Insulated', 'Bare', 'Unknown'])
        scene = insulation_diagram(after, g.Drawing)
        svg = ET.fromstring(scene.svg())
        bands = [e for e in svg if e.tag.endswith('line') and e.get('stroke-width') == '36']
        self.assertEqual(len(bands), 1)
        self.assertEqual(bands[0].get('stroke-opacity'), '0.28')
        self.assertIn('draw opacity=0.28', scene.tikz())
        self.assertTrue(any('without complete supporting evidence' in n for n in after['notes']))

    def test_corner_lengths_are_not_inferred(self):
        corners = [r for r in g.solve(self.tables)['insulation_regions'] if r['geometry_kind'] == 'schematic_corner']
        self.assertEqual(len(corners), 4)
        self.assertTrue(all(r['length_mm'] is None and r['start_station_mm'] is None for r in corners))
        self.assertTrue(all(r['extent_resolved'] for r in corners))

    def test_invalid_state_material_thickness_and_ids_are_rejected(self):
        baseline = copy.deepcopy(self.tables)
        for patch, message in [({'Coverage': ''}, 'Coverage must'),
                               ({'Coverage': 'Yes'}, 'Coverage must'),
                               ({'Material ID': 'MISSING'}, 'not in Materials'),
                               ({'Thickness mm': -1}, 'nonnegative'),
                               ({'Thickness mm': float('nan')}, 'nonnegative'),
                               ({'Coverage': 'Insulated', 'Thickness mm': 0}, 'must be positive'),
                               ({'Coverage': 'Bare', 'Thickness mm': 10}, 'contradicts'),
                               ({'Coverage': 'Bare', 'Material ID': 'MAIN-INS'}, 'clear insulation'),
                               ({'Evidence type': 'Approved'}, 'Evidence type')]:
            with self.subTest(patch=patch):
                self.tables = copy.deepcopy(baseline)
                self.tables['Insulation regions'][0].update(patch)
                with self.assertRaisesRegex(ValueError, message):
                    g.solve(self.tables)
        self.tables = copy.deepcopy(baseline)
        self.tables['Insulation regions'].append(copy.deepcopy(self.tables['Insulation regions'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            g.solve(self.tables)
        self.tables = copy.deepcopy(baseline)
        self.tables['Insulation regions'].pop()
        with self.assertRaisesRegex(ValueError, 'all ten'):
            g.solve(self.tables)

    def test_regional_thickness_wins_over_legacy_and_is_flagged(self):
        self.tables['Geometry'][0]['Insulation mm'] = 25
        self.tables['Insulation regions'][0].update({'Coverage': 'Insulated', 'Thickness mm': 50})
        model = g.solve(self.tables)
        self.assertEqual(model['insulation_regions'][0]['thickness_mm'], 50)
        self.assertTrue(any('conflicts with legacy' in n for n in model['notes']))

    def test_all_insulated_bare_and_unknown_have_different_overlays(self):
        for state, expected in [('Insulated', 10), ('Bare', 0), ('Unknown', 0)]:
            with self.subTest(state=state):
                for row in self.tables['Insulation regions']:
                    row['Coverage'] = state
                model = g.solve(self.tables)
                svg = ET.fromstring(insulation_diagram(model, g.Drawing).svg())
                bands = [e for e in svg if e.tag.endswith('line') and e.get('stroke-width') == '36']
                self.assertEqual(len(bands), expected)

    def write_workbook(self, path):
        """Append a small literal-values sheet to the old fixture, without spreadsheet dependencies."""
        ns = g.NS['s']
        sheet = ET.Element('{'+ns+'}worksheet')
        data = ET.SubElement(sheet, '{'+ns+'}sheetData')
        for number, values in [(5, HEADERS)] + [(i+6, [row[key] for key in HEADERS]) for i, row in enumerate(self.tables['Insulation regions'])]:
            row = ET.SubElement(data, '{'+ns+'}row', {'r':str(number)})
            for i, value in enumerate(values):
                if value is None:
                    continue
                cell = ET.SubElement(row, '{'+ns+'}c', {'r':chr(65+i)+str(number), 't':'inlineStr'})
                ET.SubElement(ET.SubElement(cell, '{'+ns+'}is'), '{'+ns+'}t').text = str(value)
        with zipfile.ZipFile(ROOT/'tests/fixtures/VCU_inputs.xlsx') as src, zipfile.ZipFile(path, 'w') as dst:
            for item in src.infolist():
                payload = src.read(item.filename)
                if item.filename == 'xl/workbook.xml':
                    xml = ET.fromstring(payload)
                    ET.SubElement(xml.find('s:sheets',g.NS),'{'+ns+'}sheet', {'name':'Insulation regions','sheetId':'999',g.REL:'rId999'})
                    payload = ET.tostring(xml)
                elif item.filename == 'xl/_rels/workbook.xml.rels':
                    xml = ET.fromstring(payload)
                    ET.SubElement(xml,'{http://schemas.openxmlformats.org/package/2006/relationships}Relationship', {'Id':'rId999','Type':'http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet','Target':'worksheets/insulation.xml'})
                    payload = ET.tostring(xml)
                elif item.filename == '[Content_Types].xml':
                    xml = ET.fromstring(payload)
                    ET.SubElement(xml,'{http://schemas.openxmlformats.org/package/2006/content-types}Override', {'PartName':'/xl/worksheets/insulation.xml','ContentType':'application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml'})
                    payload = ET.tostring(xml)
                dst.writestr(item,payload)
            dst.writestr('xl/worksheets/insulation.xml',ET.tostring(sheet))

    def test_workbook_edit_reaches_json_svg_pdf_source_and_checkpoint(self):
        from checkpoint import create_checkpoint, sha256
        self.tables['Insulation regions'][0].update({'Coverage':'Insulated', 'Material ID':'MAIN-INS', 'Thickness mm':50,
            'Evidence type':'Installed measurement', 'Evidence file / location':'test-photo / frame 2'})
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            workbook = root/'VCU_inputs.xlsx'
            self.write_workbook(workbook)
            out = root/'support/generated'
            model = g.generate(workbook,out)
            exported = json.loads((out/'insulation_regions.json').read_text())
            self.assertTrue(exported['coverage_record_present'])
            self.assertEqual(exported['input_sha256'], model['input_sha256'])
            self.assertEqual(exported['regions'][0]['thickness_mm'], 50)
            self.assertIn('stroke-opacity="0.28"', (out/'insulation.svg').read_text())
            report = (out/'VCU_control_package.tex').read_text()
            self.assertLess(report.index(r'\label{insulation-main}'), report.index(r'\appendix'))
            self.assertIn('test-photo / frame 2', report)
            # Supply a test build identity to exercise the checkpoint copy, not a compiler.
            pdf = root/'support/output/pdf'
            pdf.mkdir(parents=True)
            (pdf/'VCU_control_package.pdf').write_bytes(b'Test PDF fixture')
            (pdf/'VCU_detailed_audit.pdf').write_bytes(b'Test audit PDF fixture')
            identity = {name:sha256(root/name) for name in (
                'VCU_inputs.xlsx','support/generated/VCU_control_package.tex','support/output/pdf/VCU_control_package.pdf',
                'support/generated/VCU_detailed_audit.tex','support/output/pdf/VCU_detailed_audit.pdf')}
            (pdf/'build_manifest.json').write_text(json.dumps(identity))
            saved = create_checkpoint(root,'test-user','source-test-commit')
            self.assertEqual((saved/'generated/insulation_regions.json').read_bytes(),(out/'insulation_regions.json').read_bytes())
            self.assertEqual((saved/'generated/insulation.svg').read_bytes(),(out/'insulation.svg').read_bytes())


if __name__ == '__main__':
    unittest.main()
