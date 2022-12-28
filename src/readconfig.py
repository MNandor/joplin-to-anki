#!/bin/python3

config = {}

pairs = [
	('<@@>',
	'8377d2bb146642eeb0ad1f767fad203c',
	'1651769543636',),
]

config['joplinnotes'] = [x[1] for x in pairs]
config['ankidecks'] = [x[2] for x in pairs]



config['joplinfile']='/home/n/.config/joplin-desktop/database.sqlite'
config['ankifile']='/home/n/.local/share/Anki2/User 1/collection.anki2'
config['dontshowifok']=True
config['dontshowifsim']=False
config['dontshowifref']=True

def readconfig():
	return config

readConfig=readconfig
