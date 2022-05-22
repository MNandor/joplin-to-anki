#!/bin/python3


'''
script written at 3am
technically it works but its ugly as sin
should this be a vim script instead?

anyways, takes all markdown tables
and turns their content into a csv
works precisely only in the cases I would use it for and nothing else
'''

import pyperclip
import re
from prln import prln


# Anki tags work ideally
# "tag::subtag" counts as "tag"
# "tageeee" does not count as "tag"
# They also appear in the Card Browser right



def tableToCsv(lines):

	totalHeaders = []
	currentHeaders = []

	result = []
	# 0 means we're not in a table
	columnCount = 0

	ignoreHeadings = False

	for i, line in enumerate(lines):
		# First line will never be a marker
		if i == 0:
			continue

		# These are code blocks
		# They will never contain tables, so skip them
		# Also end any currently active tables
		if line.startswith('    ') or line.startswith('\t'):
			columnCount = 0
			currentHeaders = []
			continue



		# If not currently in a table
		if columnCount == 0:
			# Note: because the current line is either irrelevant,
			# or the line under a table's headers,
			# we can safely modify it during our checks

			# We can ignore surrounding whitespace
			line = line.strip()

			# ---: used to signal right-align. Not relevant to us
			line = line.replace(":", "-")


			# The following formats result in identical tables
			#  ----|----
			# |----|----|

			if line.startswith('|'): line = line[1:]
			if line.endswith('|'): line = line[:-1]


			# Check if current line is a table heading underline
			if re.match('^[-|]+$', line) and line.count('|')*line.count('-') != 0:

				# If so, we need to process the line above: the heading
				above = lines[i-1].strip()

				# Same as before, ignore | on the sides
				if above.startswith('|'): above = above[1:]
				if above.endswith('|'): above = above[:-1]


				# The heading and the underline shouldn't conflict,
				# But if they do, the heading determines the columns
				currentHeaders = above.split('|')
				columnCount = len(currentHeaders)
				
				# We keep a shared lsit of headers
				# Add to that
				for head in currentHeaders:
					if head not in totalHeaders:
						totalHeaders += [head]
				continue
			else:

				# Normal line
				# Todo handle headings here
				continue
		# If currently reading table rows
		else:
			line = lines[i].strip()

			# At least 1 | is required to continue table
			if line.count('|') == 0:
				columnCount = 0
				currentHeaders = []
				continue

			# Ignore | on sides.
			# Yes, this works right if doen after the check above
			if line.startswith('|'): line = line[1:]
			if line.endswith('|'): line = line[:-1]

			# Optional: get rid of html
			# line = re.sub('<[^<>]*>', '', line)

			# Split line
			# Note: if we have fewer fields than the header defined, don't throw an error
			# Just consider those fields empty instead
			# If we have more, the extra fields are ignored
			line = line.split('|')
			line = line + ['']*99


			# Collect data to results
			obj = {}	
			for i, head in enumerate(currentHeaders):
				obj[head] = line[i]
			result += [obj]
			continue
		
	# User-friendly printing
	ll = []
	ll += [[x for x in totalHeaders]]
	ll += [['-' for x in totalHeaders]]
	for d in result:
		ll += [[d[x] if x in d.keys() else '' for x in totalHeaders]]
	prln (ll)


	# Display numbers for Anki's "Column x maps to" feature
	for i, head in enumerate(totalHeaders):
		print(f'{i+1} maps to {head}')

	# Export to a file
	with open ("tableresult.txt", "wt") as ofs:
		for d in result:
			for head in totalHeaders:
				if head in d.keys():
					ofs.write(d[head] + '\t')
				else:
					ofs.write('\t')
			ofs.write('\n')

	





if __name__ == '__main__':
	print("Open your Joplin file and CTRL-A CTRL-C it, then press Enter")

	input()

	text = pyperclip.paste()


	test = '''
1|2|3
-|-|-
aaa|bbb|ccc
aa|bb
aaa|bbb|ccc

|one|two|three|
|-|-|-|
|aaa|bbb|ccc|
|aa|bb|
|aaa|bbb|ccc|
|aaa||ccc|


asdasd|asd
---

1|2|3
-|-|-
|aaa|bbb|ccc
|aa|bb|
aaa|bbb|ccc|

|one|two|three|
|-|-|-|
aaa|bbb|ccc|
aa|bb
|aaa|bbb|ccc
|aaa||ccc|
'''




	lines = text.split("\n")

	tableToCsv(lines)
