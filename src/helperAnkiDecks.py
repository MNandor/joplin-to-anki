#!/bin/python3

import sqlite3

from readconfig import config
from dep.prln import prln

file = config['ankifile']

def showAnkiDecks():
	db = sqlite3.connect(f'file:{file}?immutable=1', uri=True)
	cur = db.cursor()

	cur.execute('''select id, name from decks''')

	sqlResult = cur.fetchall()

	prln(sqlResult)

showAnkiDecks()
