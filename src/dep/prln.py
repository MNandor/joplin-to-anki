#!/bin/python3 -i


USE_TERMINAL_WIDTH = True
# Read terminal size
defaultWidth = -1
if USE_TERMINAL_WIDTH: 
	import os

# Print a list, nicely formatted
def prln(l,  width=-1, separator='|'):

	if USE_TERMINAL_WIDTH and width == -1:
		width = os.get_terminal_size().columns
	elif width == -1:
		width = 1e4
	
	SEPLEN = len(separator)

	# Count Columns
	columnCount = max([len(x) for x in l])

	# Calculate the maximum width of each column
	columnWidths = []
	for column in range(columnCount):
		# If not all data is the same length,
		# Ignore lines that don't span to this column
		relevant = [x for x in l if len(x) > column]
		
		maxWidth = max([len(str(x[column])) for x in relevant])
		columnWidths += [maxWidth]

	# If we can't fit, we need to truncate some columns
	availableChars = width - (columnCount + 1)*SEPLEN
	if sum(columnWidths) > availableChars:
		availableForOne = availableChars / columnCount
		totalToSplit = availableChars
		splitAmong = []

		# Columns that take up less than the average
		# Get to keep their width
		for i, w in enumerate(columnWidths):
			if w <= availableForOne:
				totalToSplit -= w	
			else:
				splitAmong += [i]

		reducedWidth = totalToSplit // len(splitAmong)

		for offender in splitAmong:
			columnWidths[offender] = reducedWidth

	
	# Actually do the printing
	vertline = lambda: 	print('-'*(sum(columnWidths)+(columnCount+1)*SEPLEN ))

	vertline()
	for line in l:
		print(separator, end='')
		for c in range(columnCount):
			w = columnWidths[c]
			item = ''
			if len(line) > c:
				item = line[c]

			if len(str(item)) < w:
				if isinstance(item, int) or isinstance(item, float):
					item = str(item).rjust(w, ' ')
				else:
					item = str(item).ljust(w, ' ')
			if len(str(item)) > w:
				item = str(item)[:w-3]+"..."


			print(item, end=separator)
		print()
	vertline()
	





if __name__ == '__main__':

	a = [
	(5, "asd"),
	(55555555555555, "a", "asd"),
	("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "asd", "asd")
	]

	b = [
	('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'The quick, brown fox jumps over the lazy dog.'),
	('', 'The quick, brown fox jumps over the lazy dog.'),
	]

	prln(a, 80)
	prln(a, 40, ' | ')
	prln(a)
	prln(b, 80)
	prln(b, 80, separator="____")
