import itertools

cash = [20] * 3 + [10] * 5 + [5] * 2 + [1] * 5
g = (comb for i in range(len(cash)) for comb in itertools.combinations(cash, i) if sum(comb) == 100)
print(len(set(list(g))))
