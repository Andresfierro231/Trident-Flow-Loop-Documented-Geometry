"""A saved checkpoint must retain its inputs and reject stale or reused builds."""
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

SUPPORT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SUPPORT / 'scripts'))
spec = importlib.util.spec_from_file_location('checkpoint', SUPPORT / 'scripts/checkpoint.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


class CheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copy2(SUPPORT / 'tests/fixtures/VCU_inputs.xlsx', self.root / 'VCU_inputs.xlsx')
        generated = self.root / 'support/generated'
        generated.mkdir(parents=True)
        tables = c.read_workbook(self.root / 'VCU_inputs.xlsx')
        (generated / 'resolved_inputs.json').write_text(json.dumps(tables))
        (generated / 'validation.json').write_text(json.dumps({
            'geometry_valid': True, 'input_sha256': c.sha256(self.root / 'VCU_inputs.xlsx')}))
        (generated / 'VCU_control_package.tex').write_text('Test report source')
        output = self.root / 'support/output/pdf'
        output.mkdir(parents=True)
        (output / 'VCU_control_package.pdf').write_bytes(b'Test PDF fixture')
        identity = {name: c.sha256(self.root / name) for name in (
            'VCU_inputs.xlsx', 'support/generated/VCU_control_package.tex',
            'support/output/pdf/VCU_control_package.pdf')}
        (output / 'build_manifest.json').write_text(json.dumps(identity))
        evidence = self.root / 'support/evidence'
        evidence.mkdir()
        (evidence / 'measurement.txt').write_text('Test evidence')

    def test_checkpoint_retains_evidence_and_file_hashes(self):
        saved = c.create_checkpoint(self.root, 'test-user', 'source-test-commit')
        manifest = json.loads((saved / 'manifest.json').read_text())
        self.assertEqual(manifest['source_commit'], 'source-test-commit')
        self.assertEqual(manifest['checkpoint_saved_by'], 'test-user')
        self.assertEqual(manifest['status'], 'Draft')
        self.assertEqual((saved / 'evidence/measurement.txt').read_text(), 'Test evidence')
        self.assertEqual(manifest['input_sha256'], c.sha256(saved / 'VCU_inputs.xlsx'))
        for name, digest in manifest['files'].items():
            self.assertEqual(c.sha256(saved / name), digest)

    def test_existing_checkpoint_is_never_overwritten(self):
        saved = c.create_checkpoint(self.root, 'test-user', 'source-test-commit')
        original = (saved / 'manifest.json').read_bytes()
        with self.assertRaises(FileExistsError):
            c.create_checkpoint(self.root, 'another-user', 'other-commit')
        self.assertEqual(original, (saved / 'manifest.json').read_bytes())

    def test_changed_pdf_is_rejected(self):
        (self.root / 'support/output/pdf/VCU_control_package.pdf').write_bytes(b'Stale PDF')
        with self.assertRaisesRegex(ValueError, 'Rebuild first'):
            c.create_checkpoint(self.root, 'test-user', 'source-test-commit')

    def test_changed_workbook_is_rejected(self):
        with open(self.root / 'VCU_inputs.xlsx', 'ab') as handle:
            handle.write(b'changed-input')
        with self.assertRaisesRegex(ValueError, 'stale or invalid'):
            c.create_checkpoint(self.root, 'test-user', 'source-test-commit')

    def add_audit(self):
        names = ('support/generated/VCU_detailed_audit.tex', 'support/output/pdf/VCU_detailed_audit.pdf')
        for name in names:
            (self.root / name).write_bytes(b'Audit fixture')
        path = self.root / 'support/output/pdf/build_manifest.json'
        build = json.loads(path.read_text())
        build.update({name: c.sha256(self.root / name) for name in names})
        path.write_text(json.dumps(build))

    def test_checkpoint_retains_matching_detailed_audit(self):
        self.add_audit()
        saved = c.create_checkpoint(self.root, 'test-user', 'source-test-commit')
        manifest = json.loads((saved / 'manifest.json').read_text())
        self.assertEqual((saved / 'VCU_detailed_audit.pdf').read_bytes(), b'Audit fixture')
        self.assertEqual(manifest['files']['VCU_detailed_audit.pdf'], c.sha256(saved / 'VCU_detailed_audit.pdf'))

    def test_stale_or_missing_detailed_audit_is_rejected(self):
        self.add_audit()
        path = self.root / 'support/output/pdf/VCU_detailed_audit.pdf'
        path.write_bytes(b'Changed audit fixture')
        with self.assertRaisesRegex(ValueError, 'detailed audit'):
            c.create_checkpoint(self.root, 'test-user', 'source-test-commit')
        path.unlink()
        with self.assertRaisesRegex(ValueError, 'detailed audit'):
            c.create_checkpoint(self.root, 'test-user', 'source-test-commit')


if __name__ == '__main__':
    unittest.main()
