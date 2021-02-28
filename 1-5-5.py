length = int(input('Enter name length: '))
with open('names.txt', 'r') as f:
	print('\n'.join([name.strip() for name in f if len(name.strip()) == length]))
