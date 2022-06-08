#!/bin/python3

from joplinToMarkdown import *
from fileToMarkdown import *
from markdownToMap import *

# todo make fileToMarkdown work on a list of files
a = joplinToMarkdown()[0]
b = fileToMarkdown('test.md')



aa = markdownToMap(a[1], a[0], None)
bb = markdownToMap(b[1], b[0], None)

print(bb)
# 	tableToCsv(body, title, deformatter)
