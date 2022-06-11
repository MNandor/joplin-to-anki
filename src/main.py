#!/bin/python3

from joplinToMarkdown import *
from fileToMarkdown import *
from markdownToMap import *
from mapToList import *
from ankiToMap import *
from compareTwoMaps import *

joplinnotes = config['joplinnotes']
ankidecks = config['ankidecks']

# For now let's only do one of each
jnote = joplinnotes[0]
adeck = ankidecks[0]

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

mapToList(jheads, jmap)

# compareTwoMaps(jmap, amap)
