#!/bin/python3

from dep.prln import *
import subprocess

def mapToList(totalHeaders, theMap):
	if 'j2aorgline' in totalHeaders: totalHeaders.remove('j2aorgline')
	if 'j2aorgnum' in totalHeaders: totalHeaders.remove('j2aorgnum')
	title = 'latest'
	# User-friendly printing
	ll = []
	ll += [[x for x in totalHeaders]]
	ll += [['-' for x in totalHeaders]]
	for d in theMap:
		ll += [[d[x] if x in d.keys() else '' for x in totalHeaders]]
	prln (ll)


	# Display numbers for Anki's "Column x maps to" feature
	for i, head in enumerate(totalHeaders):
		print(f'{i+1} maps to {head}')

# 	Export to a file
	with open (f"table-{title}.txt", "wt") as ofs:
		for d in theMap:
			line = [d[head] if head in d.keys() else '' for head in totalHeaders]
			line = '\t'.join(line)
			ofs.write(line+'\n')
	
	subprocess.run(['vim', f'table-{title}.txt'])

