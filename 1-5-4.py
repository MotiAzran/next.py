with open('names.txt', 'r') as in_file:
	with open('name_length.txt', 'w') as out_file:
		out_file.write('\n'.join([str(len(name.strip())) for name in in_file]))
