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
		if value != '':
			result[key] = value
	
	return result

def deformatField(field, fieldTitle, isAnki):
	field = field.lower().strip()

	# HTML
	field = re.sub('<[^<>]*>', '', field)
	# Images
	field = re.sub('<img[^<>]*>', '', field)
	# `code`
	field = re.sub('^`([^`]*)`$', '\\1', field)

	if field.startswith('how to '): field = field.replace('how to ', '')
	if field.startswith('how do you '): field = field.replace('how do you ', '')
	if field.startswith('what\'s the '): field = field.replace('what\'s the ', '')
	if field.endswith('?'): field = field.replace('?', '')

	field = html.unescape(field)
	

	if not isAnki:
		field = field.replace('\\`', '`')

	# Anki cloze is best displayed as code block in Joplin
	field = field.replace('{{c1::', '`')
	field = field.replace('{{c2::', '`')
	field = field.replace('{{c3::', '`')
	field = field.replace('}}', '`')
	

	return field

def deformatToHugo(text):

	# Get rid of repeated h1 tags
	pattern = re.compile(r'(# .*)\n*\1', re.MULTILINE)

	text = re.sub(pattern, r'\1\n', text)

	# Replace ++underline++ with Hugo shortcode
	text = re.sub(r"\+\+([^\+]+)\+\+", r"{{< ul >}}\1{{< / ul >}}", text)

	# Remove HTML style tags
	text = re.sub(r"<style>.*?</style>", "", text, flags=re.DOTALL)

	return text
