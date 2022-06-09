#!/bin/python3

import sqlite3

from dep.readconfig import *
from dep.prln import prln

config = readconfig('joplin-to-anki.config', True)
file = config['ankifile']

def ankiToMap(deckID):
	db = sqlite3.connect(file)
	cur = db.cursor()

	cur.execute('''
	select flds, tags, group_concat(fields.name, "\x1f")
	from notes
	left join cards
	on nid = notes.id
	left join fields
	on fields.ntid = notes.mid
	where did = ?
	group by notes.id
	''',
	(deckID,)
	)

	sqlResult = cur.fetchall()

	result = []
	for item in sqlResult:
		tags = item[1]
		tags = tags.strip().replace(' ', ',')
		fields = item[2].split('\x1f')
		content = item[0].split('\x1f')

		data = {fields[i]:content[i] for i in range(len(fields))}
		data["tags"] = tags
	
		result += [data]

	keys = set()
	for item in result:
		for key in item.keys():
			if key not in keys:
				keys.add(key)

	return list(keys), result
