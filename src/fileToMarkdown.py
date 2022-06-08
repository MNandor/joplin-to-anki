#!/bin/python3

def fileToMarkdown(file):
	with open(file, 'rt') as ifs:
		lines = ifs.readlines()
	
	lines = [x.rstrip('\n') for x in lines]
	title = file.replace('.md', '')
	return (title, lines)

