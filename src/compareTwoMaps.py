#!/bin/python3

from deformatter import *
from dep.readconfig import *
from mapToList import *


# red = '\033[91m'
normal = '\033[0m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
pink = '\033[95m'
teal = '\033[96m'


configs = readconfig('joplin-to-anki.config')
DONTSHOWIFOK = bool(configs['dontshowifok'])
DONTSHOWIFSIM = bool(configs['dontshowifsim'])
DONTSHOWIFREF = bool(configs['dontshowifref'])

print(DONTSHOWIFOK, DONTSHOWIFSIM)

# We assume 1st is Joplin and 2nd is Anki for now. 
def compareTwoMaps(orgJoplin, orgAnki):

	compJoplin = [deformatItem(x, False) for x in orgJoplin]
	compAnki = [deformatItem(x, True) for x in orgAnki]

	for i in compAnki:
		del i['sortfield']

	resJoplin = []
	resAnki = []
	resCommon = []
	resSimilar = []

	for item in compJoplin:
		# Check if compare map perfectly matches one from Anki.
		if item in compAnki:
			resCommon += [item]
			continue


		# Check if there's a Similar card
		# - at least one field is in common
		# - that field doesn't match with any other Joplin or Anki cards
		found = False
		for k, v in item.items():
			matches = [x for x in compAnki if v in x.values()]
			if len(matches) == 1 and (k == 'j2aref' or (k in matches[0].keys() and matches[0][k] == v) ):
				resSimilar += [(item, matches[0])]
				found = True
				break
		
		# Base case: found only in Joplin
		if not found:
			resJoplin += [item]
	
	_simAnki = [x[1] for x in resSimilar]
	for item in compAnki:
		if item not in resCommon and item not in _simAnki:
			resAnki += [item]

	print('\n'*5+'Color Legend')
	print(yellow, 'Comparison', normal)
	print(green+f'{len(resCommon)} perfect matches'+normal)
	print(pink+f'{len(resSimilar)} Differences'+normal)
	print(blue+f'{len(resJoplin)} Joplin'+normal)
	print(teal+f'{len(resAnki)} Anki'+normal)
	
	if not DONTSHOWIFOK:
		print('\n'*5+'Common')
		for item in resCommon:

			print(yellow, item, normal)

			ind = compJoplin.index(item) 
			orgitem = orgJoplin[ind]
			print(blue, orgitem['j2aorgnum'], orgitem['j2aorgline'], normal)

			ind = compAnki.index(item)
			orgitem = orgAnki[ind]
			print(teal, orgitem, normal)
			print()

	foundSimilars = []
	foundRefs = []
	foundJonly = []
	foundAonly = []
	if not DONTSHOWIFSIM:
		print('\n'*5+'Similars')
		for s in resSimilar:
			jopitem, aitem = s

			jopitems = jopitem.copy()
			aitems = aitem.copy()


			
			for k in aitem.keys():
				if k not in jopitem.keys() or jopitem[k] != aitem[k]:
					aitems[k] = '[[['+aitem[k]+']]]'

			for k in jopitem.keys():
				if k not in aitem.keys() or aitem[k] != jopitem[k]:
					jopitems[k] = '[[['+jopitem[k]+']]]'

			jopitems = str(jopitems).replace('[[[', pink).replace(']]]', yellow)
			aitems = str(aitems).replace('[[[', pink).replace(']]]', yellow)


			ind = compJoplin.index(jopitem) 
			orgitemj = orgJoplin[ind]

			ind = compAnki.index(aitem)
			orgitema = orgAnki[ind]

			if 'j2aref' in orgitemj['j2aorgline']:
				if DONTSHOWIFREF:
					continue

				foundRefs += [(s, orgitemj, orgitema)]
			else:
				foundSimilars += [(s, orgitemj, orgitema)]

			print(yellow, jopitems, normal)
			print(blue, orgitemj['j2aorgnum'], orgitemj['j2aorgline'], normal)

			print(yellow, aitems, normal)
			print(teal, orgitema, normal)
			print()



	print('\n'*5+'Joplin Only')
	for item in resJoplin: 
		print(yellow, item, normal)

		ind = compJoplin.index(item) 
		orgitem = orgJoplin[ind]

		foundJonly += [orgitem]
		print(blue, orgitem['j2aorgnum'], orgitem['j2aorgline'], normal)
		print()

	print('\n'*5+'Anki Only')
	for item in resAnki:
		print(yellow, item, normal)

		ind = compAnki.index(item)
		orgitem = orgAnki[ind]
		foundAonly += [orgitem]
		print(teal, orgitem, normal)
		print()

	

	if len(foundSimilars) > 0 and input('Want to generate update file (y/n)?') == 'y':
		exportUpdateAnkiExisting(foundSimilars)

	if len(foundRefs) > 0 and input('Want to generate reference-update file (y/n)?') == 'y':
		exportUpdateAnkiExisting(foundRefs)

	if len(foundJonly) > 0 and input('Want to generate J>A addition file (y/n)?') == 'y':
		exportAddtoAnki(foundJonly)

	if len(foundAonly) > 0 and input('Want to generate A>J addition file (y/n)?') == 'y':
		exportAddtoJoplin(foundAonly)

def exportUpdateAnkiExisting(resSimilar):
	result = []

	inp = chooseFromKeys([x[1] for x in resSimilar])

	print(inp)
	for s in resSimilar:
		joplin = s[1]
		anki = s[2]
		print(blue, joplin, normal)
		print(teal, anki, normal)
		print()

		obj = {}

		for k in inp:
			obj[k] = joplin[k]

		result += [obj]
	

	mapToList(inp, result)

def exportAddtoAnki(resJoplin):
	keys = []
	for i in resJoplin:
		print(blue, i, normal)
		keys += i.keys()
	
	keys = list(set(keys))

	mapToList(keys, resJoplin)


def chooseFromKeys(data):
	
	keys = set()
	for i in data:
		keys |= i.keys()
	keys = list(keys)

	print('What order (left to right) would you like your table to be in?')
	print('Pick from the values below. Example input (no spaces): Front,Back,Notes')
	print(keys)

	inp = input().split(',')

	if any([i not in keys for i in inp]):
		print('Bad input!')
		return []

	return inp


def exportAddtoJoplin(resAnki):

	inp = chooseFromKeys(resAnki)


	print('|'.join(inp))
	print('|'.join(['-' for _ in inp]))
	for item in resAnki:
		print('|'.join([item[x] for x in inp]))
