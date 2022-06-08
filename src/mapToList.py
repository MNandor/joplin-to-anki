#!/bin/python3

	# User-friendly printing
	ll = []
	ll += [[x for x in totalHeaders]]
	ll += [['-' for x in totalHeaders]]
	for d in result:
		ll += [[d[x] if x in d.keys() else '' for x in totalHeaders]]
	prln (ll)


	# Display numbers for Anki's "Column x maps to" feature
	for i, head in enumerate(totalHeaders):
		print(f'{i+1} maps to {head}')

	# Export to a file
	with open (f"table-{title}.txt", "wt") as ofs:
		for d in result:
			for head in totalHeaders:
				if head in d.keys():
					ofs.write(d[head] + '\t')
				else:
					ofs.write('\t')
			ofs.write('\n')

