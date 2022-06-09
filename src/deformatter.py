#!/bin/python3

import re

# Used for modifying the field's content when taken from Joplin
# Feel free to change this according to your preferences
# My version removes HTML and certain markdown syntax such as `code`


def deformatItem(item):
	result = {}
	
	for key, value in item.items():
		if value == '':
			continue

		value = deformatField(value, key)
		result[key] = value
	
	return result

def deformatField(field, fieldTitle):

	# HTML
	field = re.sub('<[^<>]*>', '', field)
	# `code`
	field = re.sub('^`([^`]*)`$', '\\1', field)

	return field
