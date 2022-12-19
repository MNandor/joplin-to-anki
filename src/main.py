#!/bin/python3

from joplinToMarkdown import *
from fileToMarkdown import *
from markdownToMap import *
from mapToList import *
from ankiToMap import *
from compareTwoMaps import *

joplinnotes = config['joplinnotes'][::-1]
ankidecks = config['ankidecks'][::-1]

for i in range(len(joplinnotes)):
	jnote = joplinnotes[i]
	adeck = ankidecks[i]

	# Test file
	# tfile = 'test.md'
	# ftitle, flines = fileToMarkdown(tfile)
	# print(ftitle, flines)

	jtitle, jlines = joplinToMarkdown(jnote)
	print(jtitle)

	jheads, jmap = markdownToMap(jlines, jtitle, None)

	akeys, amap = ankiToMap(adeck)


	compareTwoMaps(jmap, amap)
	print('\n'*5)

