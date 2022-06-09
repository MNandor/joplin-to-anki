#!/bin/python3

from joplinToMarkdown import *
from fileToMarkdown import *
from markdownToMap import *
from mapToList import *
from ankiToMap import *

# todo make fileToMarkdown work on a list of files
# a = joplinToMarkdown()[0]
# b = fileToMarkdown('test.md')



# aheads, aa = markdownToMap(a[1], a[0], None)
# bheads, bb = markdownToMap(b[1], b[0], None)

# mapToList(aheads, aa)
# mapToList(bheads, bb)

a = ankiToMap(None)
print(a)


# 	tableToCsv(body, title, deformatter)
