#!/bin/python3

import sqlite3
from dep.readconfig import *

config = readconfig('joplin-to-anki.config', True)

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
	

if __name__ == '__main__':
	import re
	import pyperclip
	joplinnotes = config['joplinnotes'][::-1]

	for i in range(len(joplinnotes)):
		jnote = joplinnotes[i]
		jtitle, jlines = joplinToMarkdown(jnote, True)

		if jtitle == None:
			continue

		print('\n'*5+jtitle+'\n'*2)
		body = '\n'.join(jlines)

		pattern = re.compile(r'(# .*)\n*\1', re.MULTILINE)
		body = re.sub(pattern, r'\1\n', body)

		print(body)
		pyperclip.copy(body)
		input('Press enter for next')


