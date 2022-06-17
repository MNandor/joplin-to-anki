#!/bin/python3

import re
import html

# Used for modifying the field's content when taken from Joplin
# Feel free to change this according to your preferences
# My version removes HTML and certain markdown syntax such as `code`


def deformatItem(item, isAnki):
	result = {}
	
	for key, value in item.items():
		if value == '':
			continue

		if key in ['j2aorgnum', 'j2aorgline', 'Mnemonic']:
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
		if field.startswith('how do you '): field = field.replace('how do you ', '')
		if field.startswith('what\'s the '): field = field.replace('what\'s the ', '')
		if field.endswith('?'): field = field.replace('?', '')

	field = html.unescape(field)
	

	if not isAnki:
		field = field.replace('\\`', '`')
	

	return field
