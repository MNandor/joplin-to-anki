#!/bin/python3

import re

# Used for modifying the field's content when taken from Joplin
# Feel free to change this according to your preferences
# My version removes HTML and certain markdown syntax such as `code`


def deformatItem(item, isAnki):
	result = {}
	
	for key, value in item.items():
		if value == '':
			continue

		# Todo 'tags' should not be ignored, just for testing
		if key in ['j2aorgnum', 'j2aorgline', 'tags']:
			continue

		value = deformatField(value, key, isAnki)
		result[key] = value
	
	return result

def deformatField(field, fieldTitle, isAnki):
	field = field.lower().strip()

	# HTML
	field = re.sub('<[^<>]*>', '', field)
	# `code`
	field = re.sub('^`([^`]*)`$', '\\1', field)

	if fieldTitle == 'Front':
		if field.startswith('how to '): field = field.replace('how to ', '')
		if field.endswith('?'): field = field.replace('?', '')
	

	return field
