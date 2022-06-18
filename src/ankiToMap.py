#!/bin/python3

import sqlite3

from dep.readconfig import *
from dep.prln import prln

config = readconfig('joplin-to-anki.config', True)
file = config['ankifile']

def ankiToMap(deckID):
	db = sqlite3.connect(f'file:{file}?immutable=1', uri=True)
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
		tags = tags.strip()
		fields = item[2].split('\x1f')
		content = item[0].split('\x1f')

		print(fields)
		
		# Correction: if multiple card types are made from the same note type,
		# Then the column names are repeated in the database
		# Get rid of duplicates without changing sort order
		f = []
		for i in fields:
			if i not in f:
				f += [i]
		fields = f

		data = {fields[i]:content[i] for i in range(len(fields))}
		data["tags"] = tags

		if 'j2aignore' in tags:
			continue
	
		result += [data]

	keys = set()
	for item in result:
		for key in item.keys():
			if key not in keys:
				keys.add(key)

	return list(keys), result
