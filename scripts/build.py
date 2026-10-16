#!/usr/bin/env python3
"""Regenerate the workbook outputs and compile the repository PDF entry point."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    # The CLI also marks previous outputs stale when validation fails.
    subprocess.run([sys.executable, str(ROOT / 'scripts/generate.py')],
                   cwd=ROOT, check=True)
    output = ROOT / 'output/pdf'
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
    print(f'PDF: {output / "VCU_control_package.pdf"}')


if __name__ == '__main__':
    try:
        main()
    except (subprocess.CalledProcessError, RuntimeError) as error:
        print(f'Build failed: {error}', file=sys.stderr)
        sys.exit(1)
