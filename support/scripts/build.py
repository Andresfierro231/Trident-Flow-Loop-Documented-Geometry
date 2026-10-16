#!/usr/bin/env python3
"""Regenerate the workbook outputs and compile the repository PDF entry point."""
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
    common = ['-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
              '-jobname=VCU_control_package', f'-output-directory={output}', 'main.tex']
    if shutil.which('latexmk'):
        subprocess.run(['latexmk', '-pdf', *common], cwd=ROOT, check=True)
    elif shutil.which('pdflatex'):
        for _ in range(3):
            subprocess.run(['pdflatex', *common], cwd=ROOT, check=True)
    else:
        raise RuntimeError('PDF compiler missing. Install TeX Live or MacTeX with '
                           'latexmk/pdflatex, or compile main.tex in Overleaf. '
                           'Workbook outputs have been generated successfully.')
    pdf = output / 'VCU_control_package.pdf'
    # A checkpoint must verify that its PDF belongs to these exact inputs.
    identity = {name: sha256(ROOT / name) for name in (
        'VCU_inputs.xlsx', 'support/generated/VCU_control_package.tex',
        'support/output/pdf/VCU_control_package.pdf')}
    (output / 'build_manifest.json').write_text(json.dumps(identity, indent=2) + '\n')
    print(f'PDF: {pdf}')


if __name__ == '__main__':
    try:
        main()
    except (subprocess.CalledProcessError, RuntimeError) as error:
        print(f'Build failed: {error}', file=sys.stderr)
        sys.exit(1)
