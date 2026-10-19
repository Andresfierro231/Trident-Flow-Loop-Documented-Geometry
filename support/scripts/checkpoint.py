#!/usr/bin/env python3
"""Freeze a dated configuration after a successful workbook-to-PDF build."""
import argparse
from datetime import date, datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from generate import read_workbook

ROOT = Path(__file__).resolve().parents[2]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def create_checkpoint(root, actor, source_commit):
    settings = {r['Field']: r['Value'] for r in read_workbook(root / 'VCU_inputs.xlsx')['Start']}
    config = str(settings.get('Configuration ID') or '')
    effective = str(settings.get('Effective date') or '')
    summary = str(settings.get('Change summary') or '').strip()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,79}', config):
        raise ValueError('Start: Configuration ID must use letters, numbers, dots, underscores or hyphens.')
    if date.fromisoformat(effective).isoformat() != effective:
        raise ValueError('Start: Effective date must be YYYY-MM-DD text.')
    if not summary:
        raise ValueError('Start: Change summary is required for a dated checkpoint.')
    if not actor.strip():
        raise ValueError('Identify who is saving the checkpoint.')

    generated = root / 'support/generated'
    validation = json.loads((generated / 'validation.json').read_text())
    if not validation.get('geometry_valid') or validation.get('input_sha256') != sha256(root / 'VCU_inputs.xlsx'):
        raise ValueError('Regenerate successfully before creating a checkpoint; validation is stale or invalid.')
    build = json.loads((root / 'support/output/pdf/build_manifest.json').read_text())
    required = ('VCU_inputs.xlsx', 'support/generated/VCU_control_package.tex',
                'support/output/pdf/VCU_control_package.pdf')
    if any(build.get(name) != sha256(root / name) for name in required):
        raise ValueError('The PDF or workbook has changed since the last successful build. Rebuild first.')
    # Legacy checkpoints have only the configuration PDF. New builds must bind
    # the detailed audit source and PDF to the same build manifest as well.
    audit = ('support/generated/VCU_detailed_audit.tex', 'support/output/pdf/VCU_detailed_audit.pdf')
    has_audit = any((root / name).exists() or name in build for name in audit)
    if has_audit and any(not (root / name).is_file() or build.get(name) != sha256(root / name) for name in audit):
        raise ValueError('The detailed audit has changed or is missing. Rebuild first.')
    resolved = json.loads((generated / 'resolved_inputs.json').read_text())
    if resolved != read_workbook(root / 'VCU_inputs.xlsx'):
        raise ValueError('Generated data does not match the saved workbook. Rebuild first.')

    parent = root / 'support/checkpoints'
    destination = parent / f'{effective}_{config}'
    if destination.exists():
        raise FileExistsError(f'Checkpoint already exists: {destination.name}. Use a new configuration ID; do not overwrite it.')
    evidence = root / 'support/evidence'
    if evidence.exists() and any(p.is_symlink() for p in evidence.rglob('*')):
        raise ValueError('Evidence must be stored as files, not symbolic links.')
    parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=parent, prefix='.checkpoint-') as temp:
        staged = Path(temp) / 'record'
        staged.mkdir()
        shutil.copy2(root / 'VCU_inputs.xlsx', staged / 'VCU_inputs.xlsx')
        shutil.copy2(root / required[2], staged / 'VCU_control_package.pdf')
        if has_audit:
            shutil.copy2(root / audit[1], staged / 'VCU_detailed_audit.pdf')
        shutil.copytree(generated, staged / 'generated')
        if evidence.exists():
            shutil.copytree(evidence, staged / 'evidence')
        if sha256(staged / 'VCU_inputs.xlsx') != validation['input_sha256']:
            raise ValueError('Workbook changed while saving the checkpoint. Rebuild and retry.')
        hashes = {p.relative_to(staged).as_posix(): sha256(p)
                  for p in sorted(staged.rglob('*')) if p.is_file()}
        manifest = dict(configuration_id=config, effective_date=effective,
                        status=settings.get('Status'), change_summary=summary,
                        prepared_by=settings.get('Prepared by'), checked_by=settings.get('Checked by'),
                        checkpoint_saved_by=actor, source_commit=source_commit,
                        created_utc=datetime.now(timezone.utc).isoformat(),
                        input_sha256=validation['input_sha256'], files=hashes)
        (staged / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        (staged / 'README.md').write_text(
            f'# {config}\n\nEffective date: {effective}\n\n{summary}\n\n'
            'This is a saved configuration record. Keep it unchanged; make later edits in the root workbook '
            'and save a new checkpoint. Open VCU_control_package.pdf to read it. '
            'Evidence files and generated exports are included; manifest.json records file hashes, '
            'the source commit and who saved it. Saving a checkpoint does not change its review status.\n')
        staged.rename(destination)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--actor', default=os.environ.get('GITHUB_ACTOR', ''))
    args = parser.parse_args()
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    destination = create_checkpoint(ROOT, args.actor, commit)
    print(f'Saved checkpoint: {destination.relative_to(ROOT)}')
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as handle:
            handle.write(f'path={destination.relative_to(ROOT).as_posix()}\n')


if __name__ == '__main__':
    main()
