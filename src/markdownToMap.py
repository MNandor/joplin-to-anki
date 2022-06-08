#!/bin/python3


import re
def markdownToMap(lines, title, deformatter):

	totalHeaders = []
	totalHeaders += ['tags']
	currentHeaders = []

	result = []
	# 0 means we're not in a table
	columnCount = 0

	ignoreHeadings = False

	markdownHeadings = [title.lower().replace(' ','-')]

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
				# Check if we're in markdown heading
				headingDepth = 0
				while line.startswith('#'):
					headingDepth += 1
					line = line[1:]

				# Store in the list
				# Markdown headings are a tree structure:
				# Forget about deeper headings when higher level changes
				if headingDepth != 0:

					print(headingDepth, line)

					depthDiff = len(markdownHeadings) - headingDepth
					if depthDiff == 0:
						markdownHeadings += ['']
					elif depthDiff < 0:
						print('Warning, wrong heading structure: ', line)
						markdownHeadings += ['MISSING']*(-depthDiff+1)


					line = line.strip().lower().replace(' ', '-')
					markdownHeadings[headingDepth] = line
					markdownHeadings = markdownHeadings[:headingDepth+1]



				
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

			# Split line
			# Note: if we have fewer fields than the header defined, don't throw an error
			# Just consider those fields empty instead
			# If we have more, the extra fields are ignored
			line = line.split('|')
			line = line + ['']*99


			# Collect data to results
			obj = {}	
			for i, head in enumerate(currentHeaders):
				if deformatter != None:
					line[i] = deformatter(line[i], title, head)
				obj[head] = line[i]
			result += [obj]


			# Add a tag based on the note's title and sections
			# Note: Anki tags allow for nesting:
			# "tag::subtag" counts as "tag"
			# "tageeee" does not count as "tag"
			# They also appear in the Card Browser right
			headingTag = '::'.join(markdownHeadings)
			if 'tags' in obj.keys():
				obj['tags']+=','+headingTag
			else:
				obj['tags']=headingTag

			continue
	return result		

