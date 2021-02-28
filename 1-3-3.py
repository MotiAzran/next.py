def is_funny(string):
    # return all([c == 'a' or c == 'h' for c in string])
    return len(string) == len([c for c in string if c == 'a' or c == 'h'])
