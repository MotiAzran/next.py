with open('names.txt', 'r') as f:
	names = f.readlines()
	min_len = min([len(name) for name in names])
	print('\n'.join([name.strip() for name in names if len(name) == min_len]))
