#!/bin/python3

import sqlite3
from dep.readconfig import *

config = readconfig('joplin-to-anki.config', True)

file = config['joplinfile']

def joplinToMarkdown(note):
	print(f'Accessing database at {file}')

	con = sqlite3.connect(file)
	cur = con.cursor()

	# Todo: allow both unique ID and "Note Title" formats
	print(f'Trying note {note}')
	cur.execute('select title, body from notes where id = ?', (note,))
	res = cur.fetchall()

	if res == []:
		print(f'Error: missing note {note}')
		return None
	
	title = res[0][0]
	body = res[0][1]

	return (title, body.split('\n'))


