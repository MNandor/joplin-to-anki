#!/bin/python3

import sqlite3
from dep.readconfig import *

config = readconfig('joplin-to-anki.config', True)

file = config['joplinfile']
notes = config['joplinnotes']

def joplinToMarkdown():
	print(f'Accessing database at {file}')

	con = sqlite3.connect(file)
	cur = con.cursor()

	result = []

	for note in notes:
		# Todo: allow both unique ID and "Note Title" formats
		print(f'Trying note {note}')
		cur.execute('select title, body from notes where id = ?', (note,))
		res = cur.fetchall()

		if res == []:
			print(f'Error: missing note {note}')
			continue
		
		title = res[0][0]
		body = res[0][1]

		result += [(title, body.split('\n'))]


	return result
