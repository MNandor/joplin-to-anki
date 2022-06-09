#!/bin/python3


import sqlite3

from dep.readconfig import *
from dep.prln import prln

config = readconfig('joplin-to-anki.config', True)
file = config['ankifile']

def ankiToMap(deckID):
	db = sqlite3.connect(file)

	cur = db.cursor()


# 	cur.execute('select * from sqlite_master')
# 	return cur.fetchall()

	deckID = 1634122149747

	cur.execute('''
	select flds, tags, group_concat(fields.name, "\x1f")
	from notes
	left join cards
	on nid = notes.id
	left join fields
	on fields.ntid = notes.mid
	where did = ?
	group by notes.id
	''', (deckID, ))


	res = cur.fetchall()

	fres = []
	for item in res:
		tags = item[1]
		fields = item[2].split('\x1f')
		content = item[0].split('\x1f')

		data = {fields[i]:content[i] for i in range(len(fields))}
		data["tags"] = tags
	
		fres += [data]

	return fres
