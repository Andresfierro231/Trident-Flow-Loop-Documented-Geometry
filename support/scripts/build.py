#!/usr/bin/env python3
"""Regenerate and compile the concise configuration and full audit PDFs."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    # The CLI also marks previous outputs stale when validation fails.
    subprocess.run([sys.executable, str(ROOT / 'support/scripts/generate.py')],
                   cwd=ROOT, check=True)
    output = ROOT / 'support/output/pdf'
    output.mkdir(parents=True, exist_ok=True)
    compiler = shutil.which('latexmk') or shutil.which('pdflatex')
    if not compiler:
        raise RuntimeError('PDF compiler missing. Install TeX Live or MacTeX with '
                           'latexmk/pdflatex, or compile main.tex in Overleaf. '
                           'Workbook outputs have been generated successfully.')
    for source, jobname in [('main.tex', 'VCU_control_package'), ('audit.tex', 'VCU_detailed_audit')]:
        common = ['-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
                  f'-jobname={jobname}', f'-output-directory={output}', source]
        if Path(compiler).name == 'latexmk':
            subprocess.run([compiler, '-pdf', *common], cwd=ROOT, check=True)
        else:
            for _ in range(3):
                subprocess.run([compiler, *common], cwd=ROOT, check=True)
    # A checkpoint must verify that its PDF belongs to these exact inputs.
    identity = {name: sha256(ROOT / name) for name in (
        'VCU_inputs.xlsx', 'support/generated/VCU_control_package.tex',
        'support/output/pdf/VCU_control_package.pdf',
        'support/generated/VCU_detailed_audit.tex',
        'support/output/pdf/VCU_detailed_audit.pdf')}
    (output / 'build_manifest.json').write_text(json.dumps(identity, indent=2) + '\n')
    print(f'Configuration PDF: {output / "VCU_control_package.pdf"}')
    print(f'Detailed audit PDF: {output / "VCU_detailed_audit.pdf"}')


if __name__ == '__main__':
    try:
        main()
    except (subprocess.CalledProcessError, RuntimeError) as error:
        print(f'Build failed: {error}', file=sys.stderr)
        sys.exit(1)
