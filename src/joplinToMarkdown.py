#!/bin/python3

import sqlite3
from readconfig import config

file = config['joplinfile']

def joplinToMarkdown(note, noteBooksOnly = False):
# 	print(f'Accessing database at {file}')

	con = sqlite3.connect(file)
	cur = con.cursor()

	# Todo: allow both unique ID and "Note Title" formats
# 	print(f'Trying note {note}')
	cur.execute('select title, body from notes where id = ?', (note,))
	res = cur.fetchall()

	if res != []: # note
		title = res[0][0]
		body = res[0][1]

		if noteBooksOnly:
			return (None, None)

		return (title, body.split('\n'))

	else: # notebook
		cur.execute('select title from folders where id = ?', (note,))
		bigtitle = cur.fetchone()[0]

		bodies = ''

		cur.execute('select title, body from notes where parent_id = ? order by [order] desc', (note,))
		res = cur.fetchall()

		for note in res:
			title = note[0]
			body = note[1]

			bodies += '# '+title+'\n\n'
			bodies += body+'\n\n'

		return (bigtitle, bodies.split('\n'))
	

