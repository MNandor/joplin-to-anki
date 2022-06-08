#!/bin/python3


import sqlite3

from readconfig import *
from prln import prln

config = readconfig('joplin-to-anki.config', True)
file = config['ankifile']

db = sqlite3.connect(file)

cur = db.cursor()

cur.execute('select * from sqlite_master')
# cur.execute('select * from notes')

res = cur.fetchall()

print(res[1])


cur.execute('select flds from notes')
res = cur.fetchall()
res = res[200][0].split('\x1f')
print(res)
# prln(res)
