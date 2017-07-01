import sys
import os
import shutil
import subprocess

DIRNAME = 'tex'

FMT = r'''\documentclass[tikz, margin=3mm]{standalone}

\begin{document}
\begin{tikzpicture}[scale=5.0]
%s
\end{tikzpicture}
\end{document}
'''

s = sys.stdin.read()

tex = FMT % s


if os.path.exists(DIRNAME):
    shutil.rmtree(DIRNAME)

os.mkdir(DIRNAME)
fname = 'main.tex'
fpath = os.path.join(DIRNAME, fname)
open(fpath, 'w').write(tex)
os.chdir(DIRNAME)

print subprocess.check_call(['pdflatex' ,fname])
print subprocess.check_call(['evince', 'main.pdf'])
