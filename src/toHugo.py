#!/bin/python3

from readconfig import config
from joplinToMarkdown import *
import re

from deformatter import deformatToHugo

j2h = config['j2h']

print(j2h)

for label, jnote, _, filename in j2h:

	jtitle, jlines = joplinToMarkdown(jnote)

	text = '\n'.join(jlines)

	text = deformatToHugo(text)

	with open(f'hugo/{filename}', 'wt') as ifs:
		ifs.write(text)

