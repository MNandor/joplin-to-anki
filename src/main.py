#!/bin/python3

from joplinToMarkdown import *
from fileToMarkdown import *
from markdownToMap import *
from mapToList import *
from ankiToMap import *
from compareTwoMaps import *

joplinnotes = config['joplinnotes']
ankidecks = config['ankidecks']

for i in range(len(joplinnotes)):
	jnote = joplinnotes[i]
	adeck = ankidecks[i]

	# Test file
	# tfile = 'test.md'
	# ftitle, flines = fileToMarkdown(tfile)
	# print(ftitle, flines)

	jtitle, jlines = joplinToMarkdown(jnote)
	# print(jtitle, jlines, '\n'*5)

	jheads, jmap = markdownToMap(jlines, jtitle, None)
	# print(jheads, jmap, '\n'*5)

	akeys, amap = ankiToMap(adeck)
	# print(akeys, amap[:10])


	compareTwoMaps(jmap, amap)

