#!/bin/python3

import sqlite3
from readconfig import *
from tabletocsv import tableToCsv

config = readconfig('joplin-to-anki.config', True)
file = config['file']

print(f'Accessing database at {file}')

con = sqlite3.connect(file)
cur = con.cursor()


for note in config['notes']:
	print(f'Trying note {note}')
	cur.execute('select title, body from notes where id = ?', (note,))
	res = cur.fetchall()

	if res == []:
		print(f'Error: missing note {note}')
		continue
	
	title = res[0][0]
	body = res[0][1].split('\n')

	
	tableToCsv(body, title)
	input()

