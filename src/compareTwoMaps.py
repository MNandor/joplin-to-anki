#!/bin/python3


# We assume 1st is Joplin and 2nd is Anki for now. 
def compareTwoMaps(joplin, anki):
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
	for item in common: print(item)

	print('\n'*5+'Joplin Only')
	for item in jonly: print(item)

	print('\n'*5+'Anki Only')
	for item in aonly: print(item)
