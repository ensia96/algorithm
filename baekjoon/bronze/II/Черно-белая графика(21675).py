_, *L, O = open(0)
for i, j in zip(L, L[len(L) // 2:]):
    print(*[O[int(x + y, 2)]for x, y in zip(i, j[:-1])], sep='')
