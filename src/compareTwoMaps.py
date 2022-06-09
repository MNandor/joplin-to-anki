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

	for item in joplin:
		if item in anki:
			common += [item]
		else:
			jonly += [item]
	
	for item in anki:
		if item not in common:
			aonly += [item]

	print('\n'*5+'Common')
	print(yellow, 'Comparison', normal)
	print(blue, 'Joplin', normal)
	print(teal, 'Anki', normal)
	
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
