#!/bin/python3

import os

def readconfig(file, handleList = False):
	config = {}
	with open(file, 'rt') as ifs:
		lines = ifs.readlines()
	for line in lines:
		line = line.strip()
		# Comments
		if line.startswith('#') or line =='':
			continue

		if line.count('=') != 1:
			print('Wrongly formatted line:')
			print(line)

		key,value = line.split('=')

		# Lists
		if handleList and value.count(',') > 0:
			
			# Single item lists and extra comma at the end
			if value[-1] == ',':
				value = value[:-1]


			l = value.split(',')
			# Maps
			if all([x.count(':')==1 for x in l]):
				m = {x.split(':')[0]:x.split(':')[1] for x in l}
				config[key] = m
			else:
				config[key] = l
		
		else:
			config[key] = value
	
	return config

	

readConfig=readconfig

