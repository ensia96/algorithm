_, *L, O = open(0)
n = len(L) // 2
for a, b in zip(L[:n], L[n:]):
    print("".join(O[int(i + j, 2)]for i, j in zip(a, b)if i > "/"))
