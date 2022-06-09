#!/bin/python3

from deformatter import *


# red = '\033[91m'
normal = '\033[0m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
pink = '\033[95m'
teal = '\033[96m'

# We assume 1st is Joplin and 2nd is Anki for now. 
def compareTwoMaps(joplinorg, ankiorg):

	joplin = [deformatItem(x, False) for x in joplinorg]
	anki = [deformatItem(x, True) for x in ankiorg]

	jonly = []
	aonly = []
	common = []
	similars = []

	for item in joplin:
		if item in anki:
			common += [item]
		elif 'Front' in item.keys() and any(['Front' in x.keys() and x['Front'] == item['Front'] for x in anki]):
			similars += [item['Front']] # todo don't harcode 'Front'
		else:
			jonly += [item]
	
	for item in anki:
		if item not in common and ('Front' not in item.keys() or item['Front'] not in similars):
			aonly += [item]

	print('\n'*5+'Color Legend')
	print(yellow, 'Comparison', normal)
	print(blue, 'Joplin', normal)
	print(teal, 'Anki', normal)
	print(pink, 'Differences', normal)
	
	print('\n'*5+'Common')
	for item in common:
		print(yellow, item, normal)

		ind = joplin.index(item) 
		orgitem = joplinorg[ind]
		print(blue, orgitem['j2aorgnum'], orgitem['j2aorgline'], normal)

		ind = anki.index(item)
		orgitem = ankiorg[ind]
		print(teal, orgitem, normal)
		print()

	print('\n'*5+'Similars')
	for s in similars:
		aitem = [x for x in anki if 'Front' in x.keys() and x['Front'] == s][0]
		jopitem = [x for x in joplin if 'Front' in x.keys() and x['Front'] == s][0]

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


		print(yellow, jopitems, normal)
		ind = joplin.index(jopitem) 
		orgitem = joplinorg[ind]
		print(blue, orgitem['j2aorgnum'], orgitem['j2aorgline'], normal)

		print(yellow, aitems, normal)
		ind = anki.index(aitem)
		orgitem = ankiorg[ind]
		print(teal, orgitem, normal)
		print()


	print('\n'*5+'Joplin Only')
	for item in jonly: 
		print(yellow, item, normal)

		ind = joplin.index(item) 
		orgitem = joplinorg[ind]
		print(blue, orgitem['j2aorgnum'], orgitem['j2aorgline'], normal)
		print()

	print('\n'*5+'Anki Only')
	for item in aonly:
		print(yellow, item, normal)

		ind = anki.index(item)
		orgitem = ankiorg[ind]
		print(teal, orgitem, normal)
		print()
