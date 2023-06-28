print(sum(1/a if a else 2 for a in map(int, open(0).read().split()[1:])))
