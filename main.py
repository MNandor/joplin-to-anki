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
	cur.execute('select body from notes where id = ?', (note,))
	res = cur.fetchall()

	if res == []:
		print(f'Error: missing note {note}')
		continue
	
	res = res[0][0].split('\n')

	
	tableToCsv(res)
	input()

