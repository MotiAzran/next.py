with open('names.txt', 'r') as f:
    print(sum([len(line.strip()) for line in f]))
