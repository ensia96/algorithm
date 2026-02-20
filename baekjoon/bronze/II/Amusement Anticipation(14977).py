for L in [*open(0)][1::2]:
    *L, = map(int, L.split()[::-1])
    f = 0
    print(sum(f := f or a - b != L[0] - L[1]for a, b in zip(L, L[1:])) + 1)
