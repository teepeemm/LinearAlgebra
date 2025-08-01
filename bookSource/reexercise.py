#!/usr/local/bin/python3

import re
from glob import glob

for exfilename in glob('**/*.tex'):
    with open(exfilename) as exfile:
        lines = exfile.read()
#    if r'$$' not in lines:
#        continue
#    print(exfilename)
    if re.search(r'\n\n\\\[', lines, re.MULTILINE):
        print(exfilename)
#        breakpoint()
#    quit()
#    lines = re.sub(r'\$\$(.*?)\$\$', r'\\[\1\\]', lines, flags=re.DOTALL)
##    lines = re.sub(r'\\pdftooltip{\\begin{tikzpicture}\[(.*?)\\end{tikzpicture}}{(.*?)}',
##                    r'\\begin{tikzpicture}[alt={\2},\1\\end{tikzpicture}',
##                    lines, flags=re.DOTALL)
##    lines = re.sub(r'\\pdftooltip{\\begin{tikzpicture}(.*?)\\end{tikzpicture}}{(.*?)}',
##                    r'\\begin{tikzpicture}[alt={\2}]\1\\end{tikzpicture}',
##                    lines, flags=re.DOTALL)
##    lines = re.sub(r'(?<!\\pdftooltip{)\\begin{tikzpicture}(.*?)\\end{tikzpicture}',
##                    r'\\pdftooltip{\\begin{tikzpicture}\1\\end{tikzpicture}}{ALT-' 'TEXT-TO-BE-DETERMINED}',
##                    lines, flags=re.DOTALL)
#    with open(exfilename, 'w') as exfile:
#        exfile.write(lines)
