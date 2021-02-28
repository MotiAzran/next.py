with open('names.txt', 'r') as f:
	print(max(f.readlines(), key=len))
