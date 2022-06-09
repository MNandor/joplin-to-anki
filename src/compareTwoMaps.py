#!/bin/python3

from deformatter import *

# We assume 1st is Joplin and 2nd is Anki for now. 
def compareTwoMaps(joplinorg, ankiorg):

	joplin = [deformatItem(x) for x in joplinorg]
	anki = [deformatItem(x) for x in ankiorg]

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
	for item in common:
		ind = joplin.index(item) 
		orgitem = joplinorg[ind]
		print(orgitem['j2aorgnum'], orgitem['j2aorgline'])
		print(item)

	print('\n'*5+'Joplin Only')
	for item in jonly: 
		ind = joplin.index(item) 
		orgitem = joplinorg[ind]
		print(orgitem['j2aorgnum'], orgitem['j2aorgline'])
		print(item)

	print('\n'*5+'Anki Only')
	for item in aonly: print(item)
