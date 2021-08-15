a = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
d = {c: i + 3 for i, s in enumerate(a) for c in s}

print(sum(map(lambda x: d[x], input())))
