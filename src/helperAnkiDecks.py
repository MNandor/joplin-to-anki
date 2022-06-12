#!/bin/python3

import sqlite3

from dep.readconfig import *
from dep.prln import prln

config = readconfig('joplin-to-anki.config', True)
file = config['ankifile']

def showAnkiDecks():
	db = sqlite3.connect(f'file:{file}?immutable=1', uri=True)
	cur = db.cursor()

	cur.execute('''select id, name from decks''')

	sqlResult = cur.fetchall()

	prln(sqlResult)

showAnkiDecks()
