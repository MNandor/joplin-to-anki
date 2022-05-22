#!/bin/python3

import re

# Used for modifying the field's content when taken from Joplin
# Feel free to change this according to your preferences
# My version removes HTML and certain markdown syntax such as `code`
def deformatter(field, noteTitle, columnTitle):

	# HTML
	field = re.sub('<[^<>]*>', '', field)
	# `code`
	field = re.sub('^`([^`]*)`$', '\\1', field)

	return field
