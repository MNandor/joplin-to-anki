#!/bin/python3

from readconfig import config
from joplinToMarkdown import *
import re

j2h = config['j2h']

print(j2h)

for label, jnote, _, filename in j2h:

	jtitle, jlines = joplinToMarkdown(jnote)

	text = '\n'.join(jlines)


	pattern = re.compile(r'(# .*)\n*\1', re.MULTILINE)

	text = re.sub(pattern, r'\1\n', text)

	with open(f'hugo/{filename}', 'wt') as ifs:
		ifs.write(text)

