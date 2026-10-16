"""Protect the distinction between submitted evidence and selected baseline inputs."""
import importlib.util
import json
import re
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('generate', ROOT/'scripts/generate.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


class ControlRecordsTests(unittest.TestCase):
    def setUp(self):
        self.tables = g.read_workbook(ROOT/'tests/fixtures/VCU_inputs.xlsx')

    def test_seed_evidence_is_complete_but_not_approved(self):
        g.validate_control(self.tables)
        self.assertEqual(len(self.tables['Requirements']), 78)
        self.assertEqual({int(r['Phase']) for r in self.tables['Phase requests']}, set(range(5)))
        self.assertTrue(all(not r['Selected choice'] for r in self.tables['Requirements']))
        self.assertTrue(all(r['Review state'] != 'Approved for stated use' for r in self.tables['Requirements']))
        self.assertTrue(all(not r['Your entry'] for name in ('Form pipe','Form sensor','Form material') for r in self.tables[name]))

    def test_approval_needs_a_scoped_decision(self):
        row = self.tables['Requirements'][0]
        row['Review state'] = 'Approved for stated use'
        with self.assertRaisesRegex(ValueError, 'needed to record this review decision'):
            g.validate_control(self.tables)
        row.update({'Selected choice':'VCU-test','Decision scope / rationale':'Test-only scope',
                    'Reviewer / date':'Test reviewer / 2026-10-15','Effective configuration':'Test-only configuration'})
        g.validate_control(self.tables)
        self.assertEqual(row['Evidence type'], 'Reported')

    def test_broken_evidence_reference_is_rejected(self):
        self.tables['Requirements'][0]['Evidence source'] = 'MISSING-SOURCE'
        with self.assertRaisesRegex(ValueError, 'not in Sources'):
            g.validate_control(self.tables)

    def test_configuration_precedes_forms_and_all_navigation_targets_exist(self):
        model = g.solve(self.tables)
        report = g.report(self.tables, model, g.diagrams(model), 'test-workbook')
        appendix = report.index(r'\appendix')
        for target in ('overview', 'geometry-main', 'instruments-main',
                       'thermal-main', 'materials-main', 'uncertainty-main'):
            self.assertLess(report.index(r'\label{' + target + '}'), appendix)
        for target in ('administration', 'form-pipe', 'form-sensor',
                       'form-material', 'requirements', 'sources-detail'):
            self.assertGreater(report.index(r'\label{' + target + '}'), appendix)
        labels = re.findall(r'\\label\{([^}]+)\}', report)
        self.assertEqual(len(labels), len(set(labels)))
        targets = re.findall(r'\\hyperref\[([^]]+)\]', report)
        self.assertTrue(targets)
        self.assertTrue(set(targets).issubset(labels))

    def test_form_response_reaches_document_without_changing_geometry(self):
        before = g.solve(self.tables)
        with tempfile.TemporaryDirectory() as temp:
            edited = Path(temp)/'submitted.xlsx'
            with zipfile.ZipFile(ROOT/'tests/fixtures/VCU_inputs.xlsx') as src, zipfile.ZipFile(edited,'w') as dst:
                for item in src.infolist():
                    data = src.read(item.filename)
                    if item.filename == 'xl/worksheets/sheet9.xml':
                        xml = ET.fromstring(data)
                        row = xml.find('.//s:row[@r="7"]', g.NS)
                        for address, value in {'F7':'1717 mm (test response only)', 'G7':'test-photo / frame 2',
                                               'H7':'Installed measurement', 'I7':'Test submitter / 2026-10-15'}.items():
                            cell = row.find(f's:c[@r="{address}"]', g.NS)
                            if cell is None:
                                cell = ET.SubElement(row, '{'+g.NS['s']+'}c', {'r':address})
                            for child in list(cell):
                                cell.remove(child)
                            cell.set('t','inlineStr')
                            text = ET.SubElement(ET.SubElement(cell, '{'+g.NS['s']+'}is'), '{'+g.NS['s']+'}t')
                            text.text = value
                        data = ET.tostring(xml)
                    dst.writestr(item,data)
            after = g.generate(edited,Path(temp)/'out')
            report = (Path(temp)/'out/VCU_control_package.tex').read_text()
            self.assertIn('1717 mm (test response only)', report)
            self.assertIn('test-photo / frame 2', report)
            self.assertEqual(before['points'],after['points'])
            self.assertEqual(before['segments'],after['segments'])
            records = json.loads((Path(temp)/'out/resolved_inputs.json').read_text())
            self.assertEqual(records['Form pipe'][1]['Reference only'], '1219.200 mm')


if __name__=='__main__':
    unittest.main()
